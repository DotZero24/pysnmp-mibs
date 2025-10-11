# SNMP MIB module (QTECH-AAA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-AAA-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:18 2025
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "QTECH-TC",
    "ConfigStatus",
    "IfIndex")

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

qtechAAAMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19)
)
if mibBuilder.loadTexts:
    qtechAAAMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechRadiusServerTrap_ObjectIdentity = ObjectIdentity
qtechRadiusServerTrap = _QtechRadiusServerTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 0)
)
_QtechAAAMIBObjects_ObjectIdentity = ObjectIdentity
qtechAAAMIBObjects = _QtechAAAMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1)
)
_QtechDot1xAuthObjects_ObjectIdentity = ObjectIdentity
qtechDot1xAuthObjects = _QtechDot1xAuthObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1)
)


class _QtechDot1xAuthStatus_Type(EnabledStatus):
    """Custom type qtechDot1xAuthStatus based on EnabledStatus"""
    defaultValue = 2


_QtechDot1xAuthStatus_Type.__name__ = "EnabledStatus"
_QtechDot1xAuthStatus_Object = MibScalar
qtechDot1xAuthStatus = _QtechDot1xAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 1),
    _QtechDot1xAuthStatus_Type()
)
qtechDot1xAuthStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot1xAuthStatus.setStatus("current")


class _QtechDot1xAuthObjectsQuietPeriod_Type(Unsigned32):
    """Custom type qtechDot1xAuthObjectsQuietPeriod based on Unsigned32"""
    defaultValue = 60


_QtechDot1xAuthObjectsQuietPeriod_Type.__name__ = "Unsigned32"
_QtechDot1xAuthObjectsQuietPeriod_Object = MibScalar
qtechDot1xAuthObjectsQuietPeriod = _QtechDot1xAuthObjectsQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 2),
    _QtechDot1xAuthObjectsQuietPeriod_Type()
)
qtechDot1xAuthObjectsQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot1xAuthObjectsQuietPeriod.setStatus("current")


class _QtechDot1xAuthObjectsTxPeriod_Type(Unsigned32):
    """Custom type qtechDot1xAuthObjectsTxPeriod based on Unsigned32"""
    defaultValue = 30


_QtechDot1xAuthObjectsTxPeriod_Type.__name__ = "Unsigned32"
_QtechDot1xAuthObjectsTxPeriod_Object = MibScalar
qtechDot1xAuthObjectsTxPeriod = _QtechDot1xAuthObjectsTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 3),
    _QtechDot1xAuthObjectsTxPeriod_Type()
)
qtechDot1xAuthObjectsTxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot1xAuthObjectsTxPeriod.setStatus("current")


class _QtechDot1xAuthObjectsSuppTimeout_Type(Unsigned32):
    """Custom type qtechDot1xAuthObjectsSuppTimeout based on Unsigned32"""
    defaultValue = 30


_QtechDot1xAuthObjectsSuppTimeout_Type.__name__ = "Unsigned32"
_QtechDot1xAuthObjectsSuppTimeout_Object = MibScalar
qtechDot1xAuthObjectsSuppTimeout = _QtechDot1xAuthObjectsSuppTimeout_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 4),
    _QtechDot1xAuthObjectsSuppTimeout_Type()
)
qtechDot1xAuthObjectsSuppTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot1xAuthObjectsSuppTimeout.setStatus("current")


class _QtechDot1xAuthObjectsServerTimeout_Type(Unsigned32):
    """Custom type qtechDot1xAuthObjectsServerTimeout based on Unsigned32"""
    defaultValue = 30


_QtechDot1xAuthObjectsServerTimeout_Type.__name__ = "Unsigned32"
_QtechDot1xAuthObjectsServerTimeout_Object = MibScalar
qtechDot1xAuthObjectsServerTimeout = _QtechDot1xAuthObjectsServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 5),
    _QtechDot1xAuthObjectsServerTimeout_Type()
)
qtechDot1xAuthObjectsServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot1xAuthObjectsServerTimeout.setStatus("current")


class _QtechDot1xAuthObjectsMaxReq_Type(Unsigned32):
    """Custom type qtechDot1xAuthObjectsMaxReq based on Unsigned32"""
    defaultValue = 2


_QtechDot1xAuthObjectsMaxReq_Type.__name__ = "Unsigned32"
_QtechDot1xAuthObjectsMaxReq_Object = MibScalar
qtechDot1xAuthObjectsMaxReq = _QtechDot1xAuthObjectsMaxReq_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 6),
    _QtechDot1xAuthObjectsMaxReq_Type()
)
qtechDot1xAuthObjectsMaxReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot1xAuthObjectsMaxReq.setStatus("current")


class _QtechDot1xAuthObjectsReAuthPeriod_Type(Unsigned32):
    """Custom type qtechDot1xAuthObjectsReAuthPeriod based on Unsigned32"""
    defaultValue = 3600


_QtechDot1xAuthObjectsReAuthPeriod_Type.__name__ = "Unsigned32"
_QtechDot1xAuthObjectsReAuthPeriod_Object = MibScalar
qtechDot1xAuthObjectsReAuthPeriod = _QtechDot1xAuthObjectsReAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 7),
    _QtechDot1xAuthObjectsReAuthPeriod_Type()
)
qtechDot1xAuthObjectsReAuthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot1xAuthObjectsReAuthPeriod.setStatus("current")


class _QtechDot1xAuthObjectsMaxReauth_Type(Unsigned32):
    """Custom type qtechDot1xAuthObjectsMaxReauth based on Unsigned32"""
    defaultValue = 2


_QtechDot1xAuthObjectsMaxReauth_Type.__name__ = "Unsigned32"
_QtechDot1xAuthObjectsMaxReauth_Object = MibScalar
qtechDot1xAuthObjectsMaxReauth = _QtechDot1xAuthObjectsMaxReauth_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 8),
    _QtechDot1xAuthObjectsMaxReauth_Type()
)
qtechDot1xAuthObjectsMaxReauth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot1xAuthObjectsMaxReauth.setStatus("current")


class _QtechDot1xAuthObjectsReAuthEnable_Type(EnabledStatus):
    """Custom type qtechDot1xAuthObjectsReAuthEnable based on EnabledStatus"""
    defaultValue = 2


_QtechDot1xAuthObjectsReAuthEnable_Type.__name__ = "EnabledStatus"
_QtechDot1xAuthObjectsReAuthEnable_Object = MibScalar
qtechDot1xAuthObjectsReAuthEnable = _QtechDot1xAuthObjectsReAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 9),
    _QtechDot1xAuthObjectsReAuthEnable_Type()
)
qtechDot1xAuthObjectsReAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot1xAuthObjectsReAuthEnable.setStatus("current")
_QtechDot1xAuthObjectsConfigTable_Object = MibTable
qtechDot1xAuthObjectsConfigTable = _QtechDot1xAuthObjectsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 10)
)
if mibBuilder.loadTexts:
    qtechDot1xAuthObjectsConfigTable.setStatus("current")
_QtechDot1xAuthObjectsConfigEntry_Object = MibTableRow
qtechDot1xAuthObjectsConfigEntry = _QtechDot1xAuthObjectsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 10, 1)
)
qtechDot1xAuthObjectsConfigEntry.setIndexNames(
    (0, "QTECH-AAA-MIB", "qtechDot1xAuthObjectsConfigFdbId"),
    (0, "QTECH-AAA-MIB", "qtechDot1xAuthObjectsConfigAddr"),
)
if mibBuilder.loadTexts:
    qtechDot1xAuthObjectsConfigEntry.setStatus("current")
_QtechDot1xAuthObjectsConfigFdbId_Type = Unsigned32
_QtechDot1xAuthObjectsConfigFdbId_Object = MibTableColumn
qtechDot1xAuthObjectsConfigFdbId = _QtechDot1xAuthObjectsConfigFdbId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 10, 1, 1),
    _QtechDot1xAuthObjectsConfigFdbId_Type()
)
qtechDot1xAuthObjectsConfigFdbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot1xAuthObjectsConfigFdbId.setStatus("current")
_QtechDot1xAuthObjectsConfigAddr_Type = MacAddress
_QtechDot1xAuthObjectsConfigAddr_Object = MibTableColumn
qtechDot1xAuthObjectsConfigAddr = _QtechDot1xAuthObjectsConfigAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 10, 1, 2),
    _QtechDot1xAuthObjectsConfigAddr_Type()
)
qtechDot1xAuthObjectsConfigAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot1xAuthObjectsConfigAddr.setStatus("current")


class _QtechDot1xAuthObjectsPaeState_Type(Integer32):
    """Custom type qtechDot1xAuthObjectsPaeState based on Integer32"""
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


_QtechDot1xAuthObjectsPaeState_Type.__name__ = "Integer32"
_QtechDot1xAuthObjectsPaeState_Object = MibTableColumn
qtechDot1xAuthObjectsPaeState = _QtechDot1xAuthObjectsPaeState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 10, 1, 3),
    _QtechDot1xAuthObjectsPaeState_Type()
)
qtechDot1xAuthObjectsPaeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot1xAuthObjectsPaeState.setStatus("current")


class _QtechDot1xAuthObjectsBackendAuthState_Type(Integer32):
    """Custom type qtechDot1xAuthObjectsBackendAuthState based on Integer32"""
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


_QtechDot1xAuthObjectsBackendAuthState_Type.__name__ = "Integer32"
_QtechDot1xAuthObjectsBackendAuthState_Object = MibTableColumn
qtechDot1xAuthObjectsBackendAuthState = _QtechDot1xAuthObjectsBackendAuthState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 10, 1, 4),
    _QtechDot1xAuthObjectsBackendAuthState_Type()
)
qtechDot1xAuthObjectsBackendAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot1xAuthObjectsBackendAuthState.setStatus("current")


class _QtechDot1xAuthObjectsAuthControlledPortStatus_Type(Integer32):
    """Custom type qtechDot1xAuthObjectsAuthControlledPortStatus based on Integer32"""
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


_QtechDot1xAuthObjectsAuthControlledPortStatus_Type.__name__ = "Integer32"
_QtechDot1xAuthObjectsAuthControlledPortStatus_Object = MibTableColumn
qtechDot1xAuthObjectsAuthControlledPortStatus = _QtechDot1xAuthObjectsAuthControlledPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 10, 1, 5),
    _QtechDot1xAuthObjectsAuthControlledPortStatus_Type()
)
qtechDot1xAuthObjectsAuthControlledPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot1xAuthObjectsAuthControlledPortStatus.setStatus("current")
_QtechDot1xAuthObjectsKeyTxEnabled_Type = TruthValue
_QtechDot1xAuthObjectsKeyTxEnabled_Object = MibTableColumn
qtechDot1xAuthObjectsKeyTxEnabled = _QtechDot1xAuthObjectsKeyTxEnabled_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 10, 1, 6),
    _QtechDot1xAuthObjectsKeyTxEnabled_Type()
)
qtechDot1xAuthObjectsKeyTxEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot1xAuthObjectsKeyTxEnabled.setStatus("current")
_QtechDot1xAuthObjectsIfIndex_Type = IfIndex
_QtechDot1xAuthObjectsIfIndex_Object = MibTableColumn
qtechDot1xAuthObjectsIfIndex = _QtechDot1xAuthObjectsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 10, 1, 7),
    _QtechDot1xAuthObjectsIfIndex_Type()
)
qtechDot1xAuthObjectsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot1xAuthObjectsIfIndex.setStatus("current")
_QtechDot1xAuthObjectsStatsTable_Object = MibTable
qtechDot1xAuthObjectsStatsTable = _QtechDot1xAuthObjectsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 11)
)
if mibBuilder.loadTexts:
    qtechDot1xAuthObjectsStatsTable.setStatus("current")
_QtechDot1xAuthStatsEntry_Object = MibTableRow
qtechDot1xAuthStatsEntry = _QtechDot1xAuthStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 11, 1)
)
qtechDot1xAuthStatsEntry.setIndexNames(
    (0, "QTECH-AAA-MIB", "qtechDot1xAuthObjectsStatsFdbId"),
    (0, "QTECH-AAA-MIB", "qtechDot1xAuthObjectsStatsAddr"),
)
if mibBuilder.loadTexts:
    qtechDot1xAuthStatsEntry.setStatus("current")
_QtechDot1xAuthObjectsStatsFdbId_Type = Unsigned32
_QtechDot1xAuthObjectsStatsFdbId_Object = MibTableColumn
qtechDot1xAuthObjectsStatsFdbId = _QtechDot1xAuthObjectsStatsFdbId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 11, 1, 1),
    _QtechDot1xAuthObjectsStatsFdbId_Type()
)
qtechDot1xAuthObjectsStatsFdbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot1xAuthObjectsStatsFdbId.setStatus("current")
_QtechDot1xAuthObjectsStatsAddr_Type = MacAddress
_QtechDot1xAuthObjectsStatsAddr_Object = MibTableColumn
qtechDot1xAuthObjectsStatsAddr = _QtechDot1xAuthObjectsStatsAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 11, 1, 2),
    _QtechDot1xAuthObjectsStatsAddr_Type()
)
qtechDot1xAuthObjectsStatsAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot1xAuthObjectsStatsAddr.setStatus("current")
_QtechDot1xAuthObjectsEapolFramesRx_Type = Counter32
_QtechDot1xAuthObjectsEapolFramesRx_Object = MibTableColumn
qtechDot1xAuthObjectsEapolFramesRx = _QtechDot1xAuthObjectsEapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 11, 1, 3),
    _QtechDot1xAuthObjectsEapolFramesRx_Type()
)
qtechDot1xAuthObjectsEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot1xAuthObjectsEapolFramesRx.setStatus("current")
_QtechDot1xAuthObjectsEapolFramesTx_Type = Counter32
_QtechDot1xAuthObjectsEapolFramesTx_Object = MibTableColumn
qtechDot1xAuthObjectsEapolFramesTx = _QtechDot1xAuthObjectsEapolFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 11, 1, 4),
    _QtechDot1xAuthObjectsEapolFramesTx_Type()
)
qtechDot1xAuthObjectsEapolFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot1xAuthObjectsEapolFramesTx.setStatus("current")
_QtechDot1xAuthObjectsEapolQtechFramesRx_Type = Counter32
_QtechDot1xAuthObjectsEapolQtechFramesRx_Object = MibTableColumn
qtechDot1xAuthObjectsEapolQtechFramesRx = _QtechDot1xAuthObjectsEapolQtechFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 11, 1, 5),
    _QtechDot1xAuthObjectsEapolQtechFramesRx_Type()
)
qtechDot1xAuthObjectsEapolQtechFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot1xAuthObjectsEapolQtechFramesRx.setStatus("current")
_QtechDot1xAuthObjectsEapolLogoffFramesRx_Type = Counter32
_QtechDot1xAuthObjectsEapolLogoffFramesRx_Object = MibTableColumn
qtechDot1xAuthObjectsEapolLogoffFramesRx = _QtechDot1xAuthObjectsEapolLogoffFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 11, 1, 6),
    _QtechDot1xAuthObjectsEapolLogoffFramesRx_Type()
)
qtechDot1xAuthObjectsEapolLogoffFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot1xAuthObjectsEapolLogoffFramesRx.setStatus("current")
_QtechDot1xAuthObjectsEapolRespIdFramesRx_Type = Counter32
_QtechDot1xAuthObjectsEapolRespIdFramesRx_Object = MibTableColumn
qtechDot1xAuthObjectsEapolRespIdFramesRx = _QtechDot1xAuthObjectsEapolRespIdFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 11, 1, 7),
    _QtechDot1xAuthObjectsEapolRespIdFramesRx_Type()
)
qtechDot1xAuthObjectsEapolRespIdFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot1xAuthObjectsEapolRespIdFramesRx.setStatus("current")
_QtechDot1xAuthObjectsEapolRespFramesRx_Type = Counter32
_QtechDot1xAuthObjectsEapolRespFramesRx_Object = MibTableColumn
qtechDot1xAuthObjectsEapolRespFramesRx = _QtechDot1xAuthObjectsEapolRespFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 11, 1, 8),
    _QtechDot1xAuthObjectsEapolRespFramesRx_Type()
)
qtechDot1xAuthObjectsEapolRespFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot1xAuthObjectsEapolRespFramesRx.setStatus("current")
_QtechDot1xAuthObjectsEapolReqIdFramesTx_Type = Counter32
_QtechDot1xAuthObjectsEapolReqIdFramesTx_Object = MibTableColumn
qtechDot1xAuthObjectsEapolReqIdFramesTx = _QtechDot1xAuthObjectsEapolReqIdFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 11, 1, 9),
    _QtechDot1xAuthObjectsEapolReqIdFramesTx_Type()
)
qtechDot1xAuthObjectsEapolReqIdFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot1xAuthObjectsEapolReqIdFramesTx.setStatus("current")
_QtechDot1xAuthObjectsEapolReqFramesTx_Type = Counter32
_QtechDot1xAuthObjectsEapolReqFramesTx_Object = MibTableColumn
qtechDot1xAuthObjectsEapolReqFramesTx = _QtechDot1xAuthObjectsEapolReqFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 11, 1, 10),
    _QtechDot1xAuthObjectsEapolReqFramesTx_Type()
)
qtechDot1xAuthObjectsEapolReqFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot1xAuthObjectsEapolReqFramesTx.setStatus("current")
_QtechDot1xAuthObjectsInvalidEapolFramesRx_Type = Counter32
_QtechDot1xAuthObjectsInvalidEapolFramesRx_Object = MibTableColumn
qtechDot1xAuthObjectsInvalidEapolFramesRx = _QtechDot1xAuthObjectsInvalidEapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 11, 1, 11),
    _QtechDot1xAuthObjectsInvalidEapolFramesRx_Type()
)
qtechDot1xAuthObjectsInvalidEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot1xAuthObjectsInvalidEapolFramesRx.setStatus("current")
_QtechDot1xAuthObjectsEapLengthErrorFramesRx_Type = Counter32
_QtechDot1xAuthObjectsEapLengthErrorFramesRx_Object = MibTableColumn
qtechDot1xAuthObjectsEapLengthErrorFramesRx = _QtechDot1xAuthObjectsEapLengthErrorFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 11, 1, 12),
    _QtechDot1xAuthObjectsEapLengthErrorFramesRx_Type()
)
qtechDot1xAuthObjectsEapLengthErrorFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot1xAuthObjectsEapLengthErrorFramesRx.setStatus("current")
_QtechDot1xAuthObjectsLastEapolFrameVersion_Type = Unsigned32
_QtechDot1xAuthObjectsLastEapolFrameVersion_Object = MibTableColumn
qtechDot1xAuthObjectsLastEapolFrameVersion = _QtechDot1xAuthObjectsLastEapolFrameVersion_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 11, 1, 13),
    _QtechDot1xAuthObjectsLastEapolFrameVersion_Type()
)
qtechDot1xAuthObjectsLastEapolFrameVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot1xAuthObjectsLastEapolFrameVersion.setStatus("current")
_QtechDot1xAuthObjectsLastEapolFrameSource_Type = MacAddress
_QtechDot1xAuthObjectsLastEapolFrameSource_Object = MibTableColumn
qtechDot1xAuthObjectsLastEapolFrameSource = _QtechDot1xAuthObjectsLastEapolFrameSource_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 11, 1, 14),
    _QtechDot1xAuthObjectsLastEapolFrameSource_Type()
)
qtechDot1xAuthObjectsLastEapolFrameSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot1xAuthObjectsLastEapolFrameSource.setStatus("current")
_QtechDot1xCurrentUserNumber_Type = Counter32
_QtechDot1xCurrentUserNumber_Object = MibScalar
qtechDot1xCurrentUserNumber = _QtechDot1xCurrentUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 12),
    _QtechDot1xCurrentUserNumber_Type()
)
qtechDot1xCurrentUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot1xCurrentUserNumber.setStatus("current")
_QtechDot1xCurrentAuthenticatedUserNumber_Type = Counter32
_QtechDot1xCurrentAuthenticatedUserNumber_Object = MibScalar
qtechDot1xCurrentAuthenticatedUserNumber = _QtechDot1xCurrentAuthenticatedUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 13),
    _QtechDot1xCurrentAuthenticatedUserNumber_Type()
)
qtechDot1xCurrentAuthenticatedUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot1xCurrentAuthenticatedUserNumber.setStatus("current")


class _QtechDot1xAccountStatus_Type(EnabledStatus):
    """Custom type qtechDot1xAccountStatus based on EnabledStatus"""
    defaultValue = 2


_QtechDot1xAccountStatus_Type.__name__ = "EnabledStatus"
_QtechDot1xAccountStatus_Object = MibScalar
qtechDot1xAccountStatus = _QtechDot1xAccountStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 14),
    _QtechDot1xAccountStatus_Type()
)
qtechDot1xAccountStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot1xAccountStatus.setStatus("current")
_QtechAuthIfTable_Object = MibTable
qtechAuthIfTable = _QtechAuthIfTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 15)
)
if mibBuilder.loadTexts:
    qtechAuthIfTable.setStatus("current")
_QtechAuthIfEntry_Object = MibTableRow
qtechAuthIfEntry = _QtechAuthIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 15, 1)
)
qtechAuthIfEntry.setIndexNames(
    (0, "QTECH-AAA-MIB", "qtechAuthIf"),
)
if mibBuilder.loadTexts:
    qtechAuthIfEntry.setStatus("current")
_QtechAuthIf_Type = IfIndex
_QtechAuthIf_Object = MibTableColumn
qtechAuthIf = _QtechAuthIf_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 15, 1, 1),
    _QtechAuthIf_Type()
)
qtechAuthIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAuthIf.setStatus("current")


class _QtechAuthIfStatus_Type(EnabledStatus):
    """Custom type qtechAuthIfStatus based on EnabledStatus"""
    defaultValue = 2


_QtechAuthIfStatus_Type.__name__ = "EnabledStatus"
_QtechAuthIfStatus_Object = MibTableColumn
qtechAuthIfStatus = _QtechAuthIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 15, 1, 2),
    _QtechAuthIfStatus_Type()
)
qtechAuthIfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAuthIfStatus.setStatus("current")


class _QtechAuthenticationMode_Type(Integer32):
    """Custom type qtechAuthenticationMode based on Integer32"""
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


_QtechAuthenticationMode_Type.__name__ = "Integer32"
_QtechAuthenticationMode_Object = MibScalar
qtechAuthenticationMode = _QtechAuthenticationMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 16),
    _QtechAuthenticationMode_Type()
)
qtechAuthenticationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAuthenticationMode.setStatus("current")
_QtechDot1xAccountUpdateStatus_Type = EnabledStatus
_QtechDot1xAccountUpdateStatus_Object = MibScalar
qtechDot1xAccountUpdateStatus = _QtechDot1xAccountUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 17),
    _QtechDot1xAccountUpdateStatus_Type()
)
qtechDot1xAccountUpdateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot1xAccountUpdateStatus.setStatus("current")


class _QtechDot1xAcctInterimInterval_Type(Unsigned32):
    """Custom type qtechDot1xAcctInterimInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 65535),
    )


_QtechDot1xAcctInterimInterval_Type.__name__ = "Unsigned32"
_QtechDot1xAcctInterimInterval_Object = MibScalar
qtechDot1xAcctInterimInterval = _QtechDot1xAcctInterimInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 18),
    _QtechDot1xAcctInterimInterval_Type()
)
qtechDot1xAcctInterimInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot1xAcctInterimInterval.setStatus("current")
_QtechDot1xEapolTagEnabled_Type = EnabledStatus
_QtechDot1xEapolTagEnabled_Object = MibScalar
qtechDot1xEapolTagEnabled = _QtechDot1xEapolTagEnabled_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 19),
    _QtechDot1xEapolTagEnabled_Type()
)
qtechDot1xEapolTagEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot1xEapolTagEnabled.setStatus("current")
_QtechDot1xIfUserMaxTable_Object = MibTable
qtechDot1xIfUserMaxTable = _QtechDot1xIfUserMaxTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 20)
)
if mibBuilder.loadTexts:
    qtechDot1xIfUserMaxTable.setStatus("current")
_QtechDot1xIfUserMaxEntry_Object = MibTableRow
qtechDot1xIfUserMaxEntry = _QtechDot1xIfUserMaxEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 20, 1)
)
qtechDot1xIfUserMaxEntry.setIndexNames(
    (0, "QTECH-AAA-MIB", "qtechDot1xIfUserMaxIndex"),
)
if mibBuilder.loadTexts:
    qtechDot1xIfUserMaxEntry.setStatus("current")
_QtechDot1xIfUserMaxIndex_Type = IfIndex
_QtechDot1xIfUserMaxIndex_Object = MibTableColumn
qtechDot1xIfUserMaxIndex = _QtechDot1xIfUserMaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 20, 1, 1),
    _QtechDot1xIfUserMaxIndex_Type()
)
qtechDot1xIfUserMaxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot1xIfUserMaxIndex.setStatus("current")


class _QtechDot1xIfUserMaxNum_Type(Unsigned32):
    """Custom type qtechDot1xIfUserMaxNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_QtechDot1xIfUserMaxNum_Type.__name__ = "Unsigned32"
_QtechDot1xIfUserMaxNum_Object = MibTableColumn
qtechDot1xIfUserMaxNum = _QtechDot1xIfUserMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 20, 1, 2),
    _QtechDot1xIfUserMaxNum_Type()
)
qtechDot1xIfUserMaxNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot1xIfUserMaxNum.setStatus("current")


class _QtechDot1xPseudoSrcmac_Type(EnabledStatus):
    """Custom type qtechDot1xPseudoSrcmac based on EnabledStatus"""
    defaultValue = 1


_QtechDot1xPseudoSrcmac_Type.__name__ = "EnabledStatus"
_QtechDot1xPseudoSrcmac_Object = MibScalar
qtechDot1xPseudoSrcmac = _QtechDot1xPseudoSrcmac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 21),
    _QtechDot1xPseudoSrcmac_Type()
)
qtechDot1xPseudoSrcmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot1xPseudoSrcmac.setStatus("current")
_QtechDot1xUserMIB_ObjectIdentity = ObjectIdentity
qtechDot1xUserMIB = _QtechDot1xUserMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 22)
)
_QtechDot1xUserTrapsObjects_ObjectIdentity = ObjectIdentity
qtechDot1xUserTrapsObjects = _QtechDot1xUserTrapsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 22, 1)
)
_QtechDot1xUserMac_Type = MacAddress
_QtechDot1xUserMac_Object = MibScalar
qtechDot1xUserMac = _QtechDot1xUserMac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 22, 1, 1),
    _QtechDot1xUserMac_Type()
)
qtechDot1xUserMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechDot1xUserMac.setStatus("current")
_QtechDot1xUserName_Type = DisplayString
_QtechDot1xUserName_Object = MibScalar
qtechDot1xUserName = _QtechDot1xUserName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 22, 1, 2),
    _QtechDot1xUserName_Type()
)
qtechDot1xUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechDot1xUserName.setStatus("current")
_QtechDot1xUserIp_Type = IpAddress
_QtechDot1xUserIp_Object = MibScalar
qtechDot1xUserIp = _QtechDot1xUserIp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 22, 1, 3),
    _QtechDot1xUserIp_Type()
)
qtechDot1xUserIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechDot1xUserIp.setStatus("current")
_QtechDot1xUserIpv6_Type = InetAddress
_QtechDot1xUserIpv6_Object = MibScalar
qtechDot1xUserIpv6 = _QtechDot1xUserIpv6_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 22, 1, 4),
    _QtechDot1xUserIpv6_Type()
)
qtechDot1xUserIpv6.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechDot1xUserIpv6.setStatus("current")


class _QtechDot1xUserWlanId_Type(Integer32):
    """Custom type qtechDot1xUserWlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_QtechDot1xUserWlanId_Type.__name__ = "Integer32"
_QtechDot1xUserWlanId_Object = MibScalar
qtechDot1xUserWlanId = _QtechDot1xUserWlanId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 22, 1, 5),
    _QtechDot1xUserWlanId_Type()
)
qtechDot1xUserWlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechDot1xUserWlanId.setStatus("current")


class _QtechDot1xUserVlanId_Type(Integer32):
    """Custom type qtechDot1xUserVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_QtechDot1xUserVlanId_Type.__name__ = "Integer32"
_QtechDot1xUserVlanId_Object = MibScalar
qtechDot1xUserVlanId = _QtechDot1xUserVlanId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 22, 1, 6),
    _QtechDot1xUserVlanId_Type()
)
qtechDot1xUserVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechDot1xUserVlanId.setStatus("current")
_QtechDot1xUserSsid_Type = DisplayString
_QtechDot1xUserSsid_Object = MibScalar
qtechDot1xUserSsid = _QtechDot1xUserSsid_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 22, 1, 7),
    _QtechDot1xUserSsid_Type()
)
qtechDot1xUserSsid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechDot1xUserSsid.setStatus("current")
_QtechDot1xUserApMac_Type = MacAddress
_QtechDot1xUserApMac_Object = MibScalar
qtechDot1xUserApMac = _QtechDot1xUserApMac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 22, 1, 8),
    _QtechDot1xUserApMac_Type()
)
qtechDot1xUserApMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechDot1xUserApMac.setStatus("current")
_QtechDot1xUserTerminalType_Type = DisplayString
_QtechDot1xUserTerminalType_Object = MibScalar
qtechDot1xUserTerminalType = _QtechDot1xUserTerminalType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 22, 1, 9),
    _QtechDot1xUserTerminalType_Type()
)
qtechDot1xUserTerminalType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechDot1xUserTerminalType.setStatus("current")


class _QtechDot1xUserOperType_Type(Integer32):
    """Custom type qtechDot1xUserOperType based on Integer32"""
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


_QtechDot1xUserOperType_Type.__name__ = "Integer32"
_QtechDot1xUserOperType_Object = MibScalar
qtechDot1xUserOperType = _QtechDot1xUserOperType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 22, 1, 10),
    _QtechDot1xUserOperType_Type()
)
qtechDot1xUserOperType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechDot1xUserOperType.setStatus("current")
_QtechDot1xUserTerminateCause_Type = Integer32
_QtechDot1xUserTerminateCause_Object = MibScalar
qtechDot1xUserTerminateCause = _QtechDot1xUserTerminateCause_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 22, 1, 11),
    _QtechDot1xUserTerminateCause_Type()
)
qtechDot1xUserTerminateCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechDot1xUserTerminateCause.setStatus("current")
_QtechDot1xUserReplyMessage_Type = DisplayString
_QtechDot1xUserReplyMessage_Object = MibScalar
qtechDot1xUserReplyMessage = _QtechDot1xUserReplyMessage_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 22, 1, 12),
    _QtechDot1xUserReplyMessage_Type()
)
qtechDot1xUserReplyMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechDot1xUserReplyMessage.setStatus("current")


class _QtechDot1xUserIfIndex_Type(Integer32):
    """Custom type qtechDot1xUserIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_QtechDot1xUserIfIndex_Type.__name__ = "Integer32"
_QtechDot1xUserIfIndex_Object = MibScalar
qtechDot1xUserIfIndex = _QtechDot1xUserIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 22, 1, 13),
    _QtechDot1xUserIfIndex_Type()
)
qtechDot1xUserIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechDot1xUserIfIndex.setStatus("current")
_QtechDot1xUserTraps_ObjectIdentity = ObjectIdentity
qtechDot1xUserTraps = _QtechDot1xUserTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 22, 2)
)
_QtechDot1xOnlineUserTable_Object = MibTable
qtechDot1xOnlineUserTable = _QtechDot1xOnlineUserTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 22, 3)
)
if mibBuilder.loadTexts:
    qtechDot1xOnlineUserTable.setStatus("current")
_QtechDot1xOnlineUserEntry_Object = MibTableRow
qtechDot1xOnlineUserEntry = _QtechDot1xOnlineUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 22, 3, 1)
)
qtechDot1xOnlineUserEntry.setIndexNames(
    (0, "QTECH-AAA-MIB", "qtechDot1xOnlineUserID"),
)
if mibBuilder.loadTexts:
    qtechDot1xOnlineUserEntry.setStatus("current")
_QtechDot1xOnlineUserID_Type = Integer32
_QtechDot1xOnlineUserID_Object = MibTableColumn
qtechDot1xOnlineUserID = _QtechDot1xOnlineUserID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 22, 3, 1, 1),
    _QtechDot1xOnlineUserID_Type()
)
qtechDot1xOnlineUserID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot1xOnlineUserID.setStatus("current")
_QtechDot1xOnlineUserName_Type = DisplayString
_QtechDot1xOnlineUserName_Object = MibTableColumn
qtechDot1xOnlineUserName = _QtechDot1xOnlineUserName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 22, 3, 1, 2),
    _QtechDot1xOnlineUserName_Type()
)
qtechDot1xOnlineUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot1xOnlineUserName.setStatus("current")
_QtechDot1xOnlineUserMacAddr_Type = MacAddress
_QtechDot1xOnlineUserMacAddr_Object = MibTableColumn
qtechDot1xOnlineUserMacAddr = _QtechDot1xOnlineUserMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 22, 3, 1, 3),
    _QtechDot1xOnlineUserMacAddr_Type()
)
qtechDot1xOnlineUserMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot1xOnlineUserMacAddr.setStatus("current")
_QtechDot1xOnlineUserIfIndex_Type = Integer32
_QtechDot1xOnlineUserIfIndex_Object = MibTableColumn
qtechDot1xOnlineUserIfIndex = _QtechDot1xOnlineUserIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 22, 3, 1, 4),
    _QtechDot1xOnlineUserIfIndex_Type()
)
qtechDot1xOnlineUserIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot1xOnlineUserIfIndex.setStatus("current")
_QtechDot1xOnlineUserVlanId_Type = Integer32
_QtechDot1xOnlineUserVlanId_Object = MibTableColumn
qtechDot1xOnlineUserVlanId = _QtechDot1xOnlineUserVlanId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 22, 3, 1, 5),
    _QtechDot1xOnlineUserVlanId_Type()
)
qtechDot1xOnlineUserVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot1xOnlineUserVlanId.setStatus("current")
_QtechDot1xOnlineUserIp_Type = IpAddress
_QtechDot1xOnlineUserIp_Object = MibTableColumn
qtechDot1xOnlineUserIp = _QtechDot1xOnlineUserIp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 22, 3, 1, 6),
    _QtechDot1xOnlineUserIp_Type()
)
qtechDot1xOnlineUserIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot1xOnlineUserIp.setStatus("current")
_QtechDot1xOnlineUserIpv6_Type = InetAddress
_QtechDot1xOnlineUserIpv6_Object = MibTableColumn
qtechDot1xOnlineUserIpv6 = _QtechDot1xOnlineUserIpv6_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 22, 3, 1, 7),
    _QtechDot1xOnlineUserIpv6_Type()
)
qtechDot1xOnlineUserIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot1xOnlineUserIpv6.setStatus("current")
_QtechDot1xAbnormalOfflineUserCount_Type = Counter64
_QtechDot1xAbnormalOfflineUserCount_Object = MibScalar
qtechDot1xAbnormalOfflineUserCount = _QtechDot1xAbnormalOfflineUserCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 23),
    _QtechDot1xAbnormalOfflineUserCount_Type()
)
qtechDot1xAbnormalOfflineUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot1xAbnormalOfflineUserCount.setStatus("current")
_QtechDot1xTotalAuthUserCount_Type = Counter64
_QtechDot1xTotalAuthUserCount_Object = MibScalar
qtechDot1xTotalAuthUserCount = _QtechDot1xTotalAuthUserCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 24),
    _QtechDot1xTotalAuthUserCount_Type()
)
qtechDot1xTotalAuthUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot1xTotalAuthUserCount.setStatus("current")
_QtechDot1xAuthSuccUserCount_Type = Counter64
_QtechDot1xAuthSuccUserCount_Object = MibScalar
qtechDot1xAuthSuccUserCount = _QtechDot1xAuthSuccUserCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 25),
    _QtechDot1xAuthSuccUserCount_Type()
)
qtechDot1xAuthSuccUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot1xAuthSuccUserCount.setStatus("current")
_QtechDot1xAuthFailUserCount_Type = Counter64
_QtechDot1xAuthFailUserCount_Object = MibScalar
qtechDot1xAuthFailUserCount = _QtechDot1xAuthFailUserCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 26),
    _QtechDot1xAuthFailUserCount_Type()
)
qtechDot1xAuthFailUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot1xAuthFailUserCount.setStatus("current")
_QtechAAAServerObjects_ObjectIdentity = ObjectIdentity
qtechAAAServerObjects = _QtechAAAServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2)
)


class _QtechAAAServerAuthPort_Type(Integer32):
    """Custom type qtechAAAServerAuthPort based on Integer32"""
    defaultValue = 1812

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QtechAAAServerAuthPort_Type.__name__ = "Integer32"
_QtechAAAServerAuthPort_Object = MibScalar
qtechAAAServerAuthPort = _QtechAAAServerAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 2),
    _QtechAAAServerAuthPort_Type()
)
qtechAAAServerAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAAAServerAuthPort.setStatus("current")


class _QtechAAAServerAcctPort_Type(Integer32):
    """Custom type qtechAAAServerAcctPort based on Integer32"""
    defaultValue = 1813

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QtechAAAServerAcctPort_Type.__name__ = "Integer32"
_QtechAAAServerAcctPort_Object = MibScalar
qtechAAAServerAcctPort = _QtechAAAServerAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 3),
    _QtechAAAServerAcctPort_Type()
)
qtechAAAServerAcctPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAAAServerAcctPort.setStatus("current")


class _QtechAAAServerRadiusKeyStr_Type(DisplayString):
    """Custom type qtechAAAServerRadiusKeyStr based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QtechAAAServerRadiusKeyStr_Type.__name__ = "DisplayString"
_QtechAAAServerRadiusKeyStr_Object = MibScalar
qtechAAAServerRadiusKeyStr = _QtechAAAServerRadiusKeyStr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 4),
    _QtechAAAServerRadiusKeyStr_Type()
)
qtechAAAServerRadiusKeyStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAAAServerRadiusKeyStr.setStatus("current")


class _QtechAAAServerTacplusKeyStr_Type(DisplayString):
    """Custom type qtechAAAServerTacplusKeyStr based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QtechAAAServerTacplusKeyStr_Type.__name__ = "DisplayString"
_QtechAAAServerTacplusKeyStr_Object = MibScalar
qtechAAAServerTacplusKeyStr = _QtechAAAServerTacplusKeyStr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 8),
    _QtechAAAServerTacplusKeyStr_Type()
)
qtechAAAServerTacplusKeyStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAAAServerTacplusKeyStr.setStatus("current")
_QtechAAAServerConfigTable_Object = MibTable
qtechAAAServerConfigTable = _QtechAAAServerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 9)
)
if mibBuilder.loadTexts:
    qtechAAAServerConfigTable.setStatus("current")
_QtechAAAServerConfigEntry_Object = MibTableRow
qtechAAAServerConfigEntry = _QtechAAAServerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 9, 1)
)
qtechAAAServerConfigEntry.setIndexNames(
    (0, "QTECH-AAA-MIB", "qtechAAAServerConfigProtocol"),
    (0, "QTECH-AAA-MIB", "qtechAAAServerConfigIndex"),
)
if mibBuilder.loadTexts:
    qtechAAAServerConfigEntry.setStatus("current")


class _QtechAAAServerConfigProtocol_Type(Integer32):
    """Custom type qtechAAAServerConfigProtocol based on Integer32"""
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


_QtechAAAServerConfigProtocol_Type.__name__ = "Integer32"
_QtechAAAServerConfigProtocol_Object = MibTableColumn
qtechAAAServerConfigProtocol = _QtechAAAServerConfigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 9, 1, 1),
    _QtechAAAServerConfigProtocol_Type()
)
qtechAAAServerConfigProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechAAAServerConfigProtocol.setStatus("current")


class _QtechAAAServerConfigIndex_Type(Unsigned32):
    """Custom type qtechAAAServerConfigIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_QtechAAAServerConfigIndex_Type.__name__ = "Unsigned32"
_QtechAAAServerConfigIndex_Object = MibTableColumn
qtechAAAServerConfigIndex = _QtechAAAServerConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 9, 1, 2),
    _QtechAAAServerConfigIndex_Type()
)
qtechAAAServerConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechAAAServerConfigIndex.setStatus("current")
_QtechAAAServerConfigAddressType_Type = InetAddressType
_QtechAAAServerConfigAddressType_Object = MibTableColumn
qtechAAAServerConfigAddressType = _QtechAAAServerConfigAddressType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 9, 1, 3),
    _QtechAAAServerConfigAddressType_Type()
)
qtechAAAServerConfigAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAAAServerConfigAddressType.setStatus("current")
_QtechAAAServerConfigAddress_Type = InetAddress
_QtechAAAServerConfigAddress_Object = MibTableColumn
qtechAAAServerConfigAddress = _QtechAAAServerConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 9, 1, 4),
    _QtechAAAServerConfigAddress_Type()
)
qtechAAAServerConfigAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAAAServerConfigAddress.setStatus("current")


class _QtechAAAServerConfigAuthPort_Type(Integer32):
    """Custom type qtechAAAServerConfigAuthPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QtechAAAServerConfigAuthPort_Type.__name__ = "Integer32"
_QtechAAAServerConfigAuthPort_Object = MibTableColumn
qtechAAAServerConfigAuthPort = _QtechAAAServerConfigAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 9, 1, 5),
    _QtechAAAServerConfigAuthPort_Type()
)
qtechAAAServerConfigAuthPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAAAServerConfigAuthPort.setStatus("current")


class _QtechAAAServerConfigAcctPort_Type(Integer32):
    """Custom type qtechAAAServerConfigAcctPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QtechAAAServerConfigAcctPort_Type.__name__ = "Integer32"
_QtechAAAServerConfigAcctPort_Object = MibTableColumn
qtechAAAServerConfigAcctPort = _QtechAAAServerConfigAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 9, 1, 6),
    _QtechAAAServerConfigAcctPort_Type()
)
qtechAAAServerConfigAcctPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAAAServerConfigAcctPort.setStatus("current")


class _QtechAAAServerConfigKeyStr_Type(DisplayString):
    """Custom type qtechAAAServerConfigKeyStr based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QtechAAAServerConfigKeyStr_Type.__name__ = "DisplayString"
_QtechAAAServerConfigKeyStr_Object = MibTableColumn
qtechAAAServerConfigKeyStr = _QtechAAAServerConfigKeyStr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 9, 1, 7),
    _QtechAAAServerConfigKeyStr_Type()
)
qtechAAAServerConfigKeyStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAAAServerConfigKeyStr.setStatus("current")
_QtechAAAServerConfigRowStatus_Type = RowStatus
_QtechAAAServerConfigRowStatus_Object = MibTableColumn
qtechAAAServerConfigRowStatus = _QtechAAAServerConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 9, 1, 8),
    _QtechAAAServerConfigRowStatus_Type()
)
qtechAAAServerConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAAAServerConfigRowStatus.setStatus("current")
_QtechAAARadiusGroupTable_Object = MibTable
qtechAAARadiusGroupTable = _QtechAAARadiusGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 10)
)
if mibBuilder.loadTexts:
    qtechAAARadiusGroupTable.setStatus("current")
_QtechAAARadiusGroupEntry_Object = MibTableRow
qtechAAARadiusGroupEntry = _QtechAAARadiusGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 10, 1)
)
qtechAAARadiusGroupEntry.setIndexNames(
    (0, "QTECH-AAA-MIB", "qtechAAARadiusGroupName"),
)
if mibBuilder.loadTexts:
    qtechAAARadiusGroupEntry.setStatus("current")


class _QtechAAARadiusGroupName_Type(DisplayString):
    """Custom type qtechAAARadiusGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_QtechAAARadiusGroupName_Type.__name__ = "DisplayString"
_QtechAAARadiusGroupName_Object = MibTableColumn
qtechAAARadiusGroupName = _QtechAAARadiusGroupName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 10, 1, 1),
    _QtechAAARadiusGroupName_Type()
)
qtechAAARadiusGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAAARadiusGroupName.setStatus("current")


class _QtechAAARadiusGroupVrf_Type(DisplayString):
    """Custom type qtechAAARadiusGroupVrf based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_QtechAAARadiusGroupVrf_Type.__name__ = "DisplayString"
_QtechAAARadiusGroupVrf_Object = MibTableColumn
qtechAAARadiusGroupVrf = _QtechAAARadiusGroupVrf_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 10, 1, 2),
    _QtechAAARadiusGroupVrf_Type()
)
qtechAAARadiusGroupVrf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAAARadiusGroupVrf.setStatus("current")
_QtechAAARadiusGroupRowStatus_Type = RowStatus
_QtechAAARadiusGroupRowStatus_Object = MibTableColumn
qtechAAARadiusGroupRowStatus = _QtechAAARadiusGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 10, 1, 3),
    _QtechAAARadiusGroupRowStatus_Type()
)
qtechAAARadiusGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAAARadiusGroupRowStatus.setStatus("current")
_QtechAAARadiusGroupServerTable_Object = MibTable
qtechAAARadiusGroupServerTable = _QtechAAARadiusGroupServerTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 11)
)
if mibBuilder.loadTexts:
    qtechAAARadiusGroupServerTable.setStatus("current")
_QtechAAARadiusGroupServerEntry_Object = MibTableRow
qtechAAARadiusGroupServerEntry = _QtechAAARadiusGroupServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 11, 1)
)
qtechAAARadiusGroupServerEntry.setIndexNames(
    (0, "QTECH-AAA-MIB", "qtechAAARadiusGroupName"),
    (0, "QTECH-AAA-MIB", "qtechAAARadiusGroupServerIndex"),
)
if mibBuilder.loadTexts:
    qtechAAARadiusGroupServerEntry.setStatus("current")


class _QtechAAARadiusGroupServerIndex_Type(Unsigned32):
    """Custom type qtechAAARadiusGroupServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_QtechAAARadiusGroupServerIndex_Type.__name__ = "Unsigned32"
_QtechAAARadiusGroupServerIndex_Object = MibTableColumn
qtechAAARadiusGroupServerIndex = _QtechAAARadiusGroupServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 11, 1, 1),
    _QtechAAARadiusGroupServerIndex_Type()
)
qtechAAARadiusGroupServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechAAARadiusGroupServerIndex.setStatus("current")
_QtechAAARadiusGroupServerAddressType_Type = InetAddressType
_QtechAAARadiusGroupServerAddressType_Object = MibTableColumn
qtechAAARadiusGroupServerAddressType = _QtechAAARadiusGroupServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 11, 1, 2),
    _QtechAAARadiusGroupServerAddressType_Type()
)
qtechAAARadiusGroupServerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAAARadiusGroupServerAddressType.setStatus("current")
_QtechAAARadiusGroupServerAddress_Type = InetAddress
_QtechAAARadiusGroupServerAddress_Object = MibTableColumn
qtechAAARadiusGroupServerAddress = _QtechAAARadiusGroupServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 11, 1, 3),
    _QtechAAARadiusGroupServerAddress_Type()
)
qtechAAARadiusGroupServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAAARadiusGroupServerAddress.setStatus("current")


class _QtechAAARadiusGroupServerAuthPort_Type(Integer32):
    """Custom type qtechAAARadiusGroupServerAuthPort based on Integer32"""
    defaultValue = 1812

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QtechAAARadiusGroupServerAuthPort_Type.__name__ = "Integer32"
_QtechAAARadiusGroupServerAuthPort_Object = MibTableColumn
qtechAAARadiusGroupServerAuthPort = _QtechAAARadiusGroupServerAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 11, 1, 4),
    _QtechAAARadiusGroupServerAuthPort_Type()
)
qtechAAARadiusGroupServerAuthPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAAARadiusGroupServerAuthPort.setStatus("current")


class _QtechAAARadiusGroupServerAcctPort_Type(Integer32):
    """Custom type qtechAAARadiusGroupServerAcctPort based on Integer32"""
    defaultValue = 1813

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QtechAAARadiusGroupServerAcctPort_Type.__name__ = "Integer32"
_QtechAAARadiusGroupServerAcctPort_Object = MibTableColumn
qtechAAARadiusGroupServerAcctPort = _QtechAAARadiusGroupServerAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 11, 1, 5),
    _QtechAAARadiusGroupServerAcctPort_Type()
)
qtechAAARadiusGroupServerAcctPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAAARadiusGroupServerAcctPort.setStatus("current")
_QtechAAARadiusGroupServerRowStatus_Type = RowStatus
_QtechAAARadiusGroupServerRowStatus_Object = MibTableColumn
qtechAAARadiusGroupServerRowStatus = _QtechAAARadiusGroupServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 11, 1, 6),
    _QtechAAARadiusGroupServerRowStatus_Type()
)
qtechAAARadiusGroupServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAAARadiusGroupServerRowStatus.setStatus("current")


class _QtechAAAServerTotalOnlineCount_Type(Integer32):
    """Custom type qtechAAAServerTotalOnlineCount based on Integer32"""
    defaultValue = 0


_QtechAAAServerTotalOnlineCount_Type.__name__ = "Integer32"
_QtechAAAServerTotalOnlineCount_Object = MibScalar
qtechAAAServerTotalOnlineCount = _QtechAAAServerTotalOnlineCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 12),
    _QtechAAAServerTotalOnlineCount_Type()
)
qtechAAAServerTotalOnlineCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAAAServerTotalOnlineCount.setStatus("current")


class _QtechAAAServerAbnormalOffline_Type(Counter32):
    """Custom type qtechAAAServerAbnormalOffline based on Counter32"""
    defaultValue = 0


_QtechAAAServerAbnormalOffline_Type.__name__ = "Counter32"
_QtechAAAServerAbnormalOffline_Object = MibScalar
qtechAAAServerAbnormalOffline = _QtechAAAServerAbnormalOffline_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 13),
    _QtechAAAServerAbnormalOffline_Type()
)
qtechAAAServerAbnormalOffline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAAAServerAbnormalOffline.setStatus("current")


class _QtechAAAServerRadiusAuthReqCount_Type(Counter32):
    """Custom type qtechAAAServerRadiusAuthReqCount based on Counter32"""
    defaultValue = 0


_QtechAAAServerRadiusAuthReqCount_Type.__name__ = "Counter32"
_QtechAAAServerRadiusAuthReqCount_Object = MibScalar
qtechAAAServerRadiusAuthReqCount = _QtechAAAServerRadiusAuthReqCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 14),
    _QtechAAAServerRadiusAuthReqCount_Type()
)
qtechAAAServerRadiusAuthReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAAAServerRadiusAuthReqCount.setStatus("current")


class _QtechAAAServerRadiusAuthRespCount_Type(Counter32):
    """Custom type qtechAAAServerRadiusAuthRespCount based on Counter32"""
    defaultValue = 0


_QtechAAAServerRadiusAuthRespCount_Type.__name__ = "Counter32"
_QtechAAAServerRadiusAuthRespCount_Object = MibScalar
qtechAAAServerRadiusAuthRespCount = _QtechAAAServerRadiusAuthRespCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 15),
    _QtechAAAServerRadiusAuthRespCount_Type()
)
qtechAAAServerRadiusAuthRespCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAAAServerRadiusAuthRespCount.setStatus("current")


class _QtechAAAServerRadiusAuthSuccessCount_Type(Counter32):
    """Custom type qtechAAAServerRadiusAuthSuccessCount based on Counter32"""
    defaultValue = 0


_QtechAAAServerRadiusAuthSuccessCount_Type.__name__ = "Counter32"
_QtechAAAServerRadiusAuthSuccessCount_Object = MibScalar
qtechAAAServerRadiusAuthSuccessCount = _QtechAAAServerRadiusAuthSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 16),
    _QtechAAAServerRadiusAuthSuccessCount_Type()
)
qtechAAAServerRadiusAuthSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAAAServerRadiusAuthSuccessCount.setStatus("current")


class _QtechAAAServerCurrOnlineUserCount_Type(Integer32):
    """Custom type qtechAAAServerCurrOnlineUserCount based on Integer32"""
    defaultValue = 0


_QtechAAAServerCurrOnlineUserCount_Type.__name__ = "Integer32"
_QtechAAAServerCurrOnlineUserCount_Object = MibScalar
qtechAAAServerCurrOnlineUserCount = _QtechAAAServerCurrOnlineUserCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 17),
    _QtechAAAServerCurrOnlineUserCount_Type()
)
qtechAAAServerCurrOnlineUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAAAServerCurrOnlineUserCount.setStatus("current")
_QtechAAAMasterAuthenServerConfigTable_Object = MibTable
qtechAAAMasterAuthenServerConfigTable = _QtechAAAMasterAuthenServerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 18)
)
if mibBuilder.loadTexts:
    qtechAAAMasterAuthenServerConfigTable.setStatus("current")
_QtechAAAMasterAuthenServerConfigEntry_Object = MibTableRow
qtechAAAMasterAuthenServerConfigEntry = _QtechAAAMasterAuthenServerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 18, 1)
)
qtechAAAMasterAuthenServerConfigEntry.setIndexNames(
    (0, "QTECH-AAA-MIB", "qtechAAAMasterAuthenServerConfigGrpName"),
    (0, "QTECH-AAA-MIB", "qtechAAAMasterAuthenServerConfigSrvIndex"),
)
if mibBuilder.loadTexts:
    qtechAAAMasterAuthenServerConfigEntry.setStatus("current")


class _QtechAAAMasterAuthenServerConfigGrpName_Type(DisplayString):
    """Custom type qtechAAAMasterAuthenServerConfigGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_QtechAAAMasterAuthenServerConfigGrpName_Type.__name__ = "DisplayString"
_QtechAAAMasterAuthenServerConfigGrpName_Object = MibTableColumn
qtechAAAMasterAuthenServerConfigGrpName = _QtechAAAMasterAuthenServerConfigGrpName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 18, 1, 1),
    _QtechAAAMasterAuthenServerConfigGrpName_Type()
)
qtechAAAMasterAuthenServerConfigGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechAAAMasterAuthenServerConfigGrpName.setStatus("current")


class _QtechAAAMasterAuthenServerConfigSrvIndex_Type(Unsigned32):
    """Custom type qtechAAAMasterAuthenServerConfigSrvIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_QtechAAAMasterAuthenServerConfigSrvIndex_Type.__name__ = "Unsigned32"
_QtechAAAMasterAuthenServerConfigSrvIndex_Object = MibTableColumn
qtechAAAMasterAuthenServerConfigSrvIndex = _QtechAAAMasterAuthenServerConfigSrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 18, 1, 2),
    _QtechAAAMasterAuthenServerConfigSrvIndex_Type()
)
qtechAAAMasterAuthenServerConfigSrvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechAAAMasterAuthenServerConfigSrvIndex.setStatus("current")
_QtechAAAMasterAuthenServerConfigAddress_Type = IpAddress
_QtechAAAMasterAuthenServerConfigAddress_Object = MibTableColumn
qtechAAAMasterAuthenServerConfigAddress = _QtechAAAMasterAuthenServerConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 18, 1, 3),
    _QtechAAAMasterAuthenServerConfigAddress_Type()
)
qtechAAAMasterAuthenServerConfigAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAAAMasterAuthenServerConfigAddress.setStatus("current")


class _QtechAAAMasterAuthenServerConfigAuthPort_Type(Integer32):
    """Custom type qtechAAAMasterAuthenServerConfigAuthPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QtechAAAMasterAuthenServerConfigAuthPort_Type.__name__ = "Integer32"
_QtechAAAMasterAuthenServerConfigAuthPort_Object = MibTableColumn
qtechAAAMasterAuthenServerConfigAuthPort = _QtechAAAMasterAuthenServerConfigAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 18, 1, 4),
    _QtechAAAMasterAuthenServerConfigAuthPort_Type()
)
qtechAAAMasterAuthenServerConfigAuthPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAAAMasterAuthenServerConfigAuthPort.setStatus("current")


class _QtechAAAMasterAuthenServerConfigAcctPort_Type(Integer32):
    """Custom type qtechAAAMasterAuthenServerConfigAcctPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QtechAAAMasterAuthenServerConfigAcctPort_Type.__name__ = "Integer32"
_QtechAAAMasterAuthenServerConfigAcctPort_Object = MibTableColumn
qtechAAAMasterAuthenServerConfigAcctPort = _QtechAAAMasterAuthenServerConfigAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 18, 1, 5),
    _QtechAAAMasterAuthenServerConfigAcctPort_Type()
)
qtechAAAMasterAuthenServerConfigAcctPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAAAMasterAuthenServerConfigAcctPort.setStatus("current")


class _QtechAAAMasterAuthenServerConfigKeyStr_Type(DisplayString):
    """Custom type qtechAAAMasterAuthenServerConfigKeyStr based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QtechAAAMasterAuthenServerConfigKeyStr_Type.__name__ = "DisplayString"
_QtechAAAMasterAuthenServerConfigKeyStr_Object = MibTableColumn
qtechAAAMasterAuthenServerConfigKeyStr = _QtechAAAMasterAuthenServerConfigKeyStr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 18, 1, 6),
    _QtechAAAMasterAuthenServerConfigKeyStr_Type()
)
qtechAAAMasterAuthenServerConfigKeyStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAAAMasterAuthenServerConfigKeyStr.setStatus("current")
_QtechAAAMasterAuthenServerConfigRowStatus_Type = RowStatus
_QtechAAAMasterAuthenServerConfigRowStatus_Object = MibTableColumn
qtechAAAMasterAuthenServerConfigRowStatus = _QtechAAAMasterAuthenServerConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 18, 1, 7),
    _QtechAAAMasterAuthenServerConfigRowStatus_Type()
)
qtechAAAMasterAuthenServerConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAAAMasterAuthenServerConfigRowStatus.setStatus("current")
_QtechAAABackAuthenServerConfigTable_Object = MibTable
qtechAAABackAuthenServerConfigTable = _QtechAAABackAuthenServerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 19)
)
if mibBuilder.loadTexts:
    qtechAAABackAuthenServerConfigTable.setStatus("current")
_QtechAAABackAuthenServerConfigEntry_Object = MibTableRow
qtechAAABackAuthenServerConfigEntry = _QtechAAABackAuthenServerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 19, 1)
)
qtechAAABackAuthenServerConfigEntry.setIndexNames(
    (0, "QTECH-AAA-MIB", "qtechAAABackAuthenServerConfigGrpName"),
    (0, "QTECH-AAA-MIB", "qtechAAABackAuthenServerConfigSrvIndex"),
)
if mibBuilder.loadTexts:
    qtechAAABackAuthenServerConfigEntry.setStatus("current")


class _QtechAAABackAuthenServerConfigGrpName_Type(DisplayString):
    """Custom type qtechAAABackAuthenServerConfigGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_QtechAAABackAuthenServerConfigGrpName_Type.__name__ = "DisplayString"
_QtechAAABackAuthenServerConfigGrpName_Object = MibTableColumn
qtechAAABackAuthenServerConfigGrpName = _QtechAAABackAuthenServerConfigGrpName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 19, 1, 1),
    _QtechAAABackAuthenServerConfigGrpName_Type()
)
qtechAAABackAuthenServerConfigGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechAAABackAuthenServerConfigGrpName.setStatus("current")


class _QtechAAABackAuthenServerConfigSrvIndex_Type(Unsigned32):
    """Custom type qtechAAABackAuthenServerConfigSrvIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_QtechAAABackAuthenServerConfigSrvIndex_Type.__name__ = "Unsigned32"
_QtechAAABackAuthenServerConfigSrvIndex_Object = MibTableColumn
qtechAAABackAuthenServerConfigSrvIndex = _QtechAAABackAuthenServerConfigSrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 19, 1, 2),
    _QtechAAABackAuthenServerConfigSrvIndex_Type()
)
qtechAAABackAuthenServerConfigSrvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechAAABackAuthenServerConfigSrvIndex.setStatus("current")
_QtechAAABackAuthenServerConfigAddress_Type = IpAddress
_QtechAAABackAuthenServerConfigAddress_Object = MibTableColumn
qtechAAABackAuthenServerConfigAddress = _QtechAAABackAuthenServerConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 19, 1, 3),
    _QtechAAABackAuthenServerConfigAddress_Type()
)
qtechAAABackAuthenServerConfigAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAAABackAuthenServerConfigAddress.setStatus("current")


class _QtechAAABackAuthenServerConfigAuthPort_Type(Integer32):
    """Custom type qtechAAABackAuthenServerConfigAuthPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QtechAAABackAuthenServerConfigAuthPort_Type.__name__ = "Integer32"
_QtechAAABackAuthenServerConfigAuthPort_Object = MibTableColumn
qtechAAABackAuthenServerConfigAuthPort = _QtechAAABackAuthenServerConfigAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 19, 1, 4),
    _QtechAAABackAuthenServerConfigAuthPort_Type()
)
qtechAAABackAuthenServerConfigAuthPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAAABackAuthenServerConfigAuthPort.setStatus("current")


class _QtechAAABackAuthenServerConfigAcctPort_Type(Integer32):
    """Custom type qtechAAABackAuthenServerConfigAcctPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QtechAAABackAuthenServerConfigAcctPort_Type.__name__ = "Integer32"
_QtechAAABackAuthenServerConfigAcctPort_Object = MibTableColumn
qtechAAABackAuthenServerConfigAcctPort = _QtechAAABackAuthenServerConfigAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 19, 1, 5),
    _QtechAAABackAuthenServerConfigAcctPort_Type()
)
qtechAAABackAuthenServerConfigAcctPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAAABackAuthenServerConfigAcctPort.setStatus("current")


class _QtechAAABackAuthenServerConfigKeyStr_Type(DisplayString):
    """Custom type qtechAAABackAuthenServerConfigKeyStr based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QtechAAABackAuthenServerConfigKeyStr_Type.__name__ = "DisplayString"
_QtechAAABackAuthenServerConfigKeyStr_Object = MibTableColumn
qtechAAABackAuthenServerConfigKeyStr = _QtechAAABackAuthenServerConfigKeyStr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 19, 1, 6),
    _QtechAAABackAuthenServerConfigKeyStr_Type()
)
qtechAAABackAuthenServerConfigKeyStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAAABackAuthenServerConfigKeyStr.setStatus("current")
_QtechAAABackAuthenServerConfigRowStatus_Type = RowStatus
_QtechAAABackAuthenServerConfigRowStatus_Object = MibTableColumn
qtechAAABackAuthenServerConfigRowStatus = _QtechAAABackAuthenServerConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 19, 1, 7),
    _QtechAAABackAuthenServerConfigRowStatus_Type()
)
qtechAAABackAuthenServerConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAAABackAuthenServerConfigRowStatus.setStatus("current")
_QtechAAAMasterAcctServerConfigTable_Object = MibTable
qtechAAAMasterAcctServerConfigTable = _QtechAAAMasterAcctServerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 20)
)
if mibBuilder.loadTexts:
    qtechAAAMasterAcctServerConfigTable.setStatus("current")
_QtechAAAMasterAcctServerConfigEntry_Object = MibTableRow
qtechAAAMasterAcctServerConfigEntry = _QtechAAAMasterAcctServerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 20, 1)
)
qtechAAAMasterAcctServerConfigEntry.setIndexNames(
    (0, "QTECH-AAA-MIB", "qtechAAAMasterAcctServerConfigGrpName"),
    (0, "QTECH-AAA-MIB", "qtechAAAMasterAcctServerConfigSrvIndex"),
)
if mibBuilder.loadTexts:
    qtechAAAMasterAcctServerConfigEntry.setStatus("current")


class _QtechAAAMasterAcctServerConfigGrpName_Type(DisplayString):
    """Custom type qtechAAAMasterAcctServerConfigGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_QtechAAAMasterAcctServerConfigGrpName_Type.__name__ = "DisplayString"
_QtechAAAMasterAcctServerConfigGrpName_Object = MibTableColumn
qtechAAAMasterAcctServerConfigGrpName = _QtechAAAMasterAcctServerConfigGrpName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 20, 1, 1),
    _QtechAAAMasterAcctServerConfigGrpName_Type()
)
qtechAAAMasterAcctServerConfigGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechAAAMasterAcctServerConfigGrpName.setStatus("current")


class _QtechAAAMasterAcctServerConfigSrvIndex_Type(Unsigned32):
    """Custom type qtechAAAMasterAcctServerConfigSrvIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_QtechAAAMasterAcctServerConfigSrvIndex_Type.__name__ = "Unsigned32"
_QtechAAAMasterAcctServerConfigSrvIndex_Object = MibTableColumn
qtechAAAMasterAcctServerConfigSrvIndex = _QtechAAAMasterAcctServerConfigSrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 20, 1, 2),
    _QtechAAAMasterAcctServerConfigSrvIndex_Type()
)
qtechAAAMasterAcctServerConfigSrvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechAAAMasterAcctServerConfigSrvIndex.setStatus("current")
_QtechAAAMasterAcctServerConfigAddress_Type = IpAddress
_QtechAAAMasterAcctServerConfigAddress_Object = MibTableColumn
qtechAAAMasterAcctServerConfigAddress = _QtechAAAMasterAcctServerConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 20, 1, 3),
    _QtechAAAMasterAcctServerConfigAddress_Type()
)
qtechAAAMasterAcctServerConfigAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAAAMasterAcctServerConfigAddress.setStatus("current")


class _QtechAAAMasterAcctServerConfigAuthPort_Type(Integer32):
    """Custom type qtechAAAMasterAcctServerConfigAuthPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QtechAAAMasterAcctServerConfigAuthPort_Type.__name__ = "Integer32"
_QtechAAAMasterAcctServerConfigAuthPort_Object = MibTableColumn
qtechAAAMasterAcctServerConfigAuthPort = _QtechAAAMasterAcctServerConfigAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 20, 1, 4),
    _QtechAAAMasterAcctServerConfigAuthPort_Type()
)
qtechAAAMasterAcctServerConfigAuthPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAAAMasterAcctServerConfigAuthPort.setStatus("current")


class _QtechAAAMasterAcctServerConfigAcctPort_Type(Integer32):
    """Custom type qtechAAAMasterAcctServerConfigAcctPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QtechAAAMasterAcctServerConfigAcctPort_Type.__name__ = "Integer32"
_QtechAAAMasterAcctServerConfigAcctPort_Object = MibTableColumn
qtechAAAMasterAcctServerConfigAcctPort = _QtechAAAMasterAcctServerConfigAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 20, 1, 5),
    _QtechAAAMasterAcctServerConfigAcctPort_Type()
)
qtechAAAMasterAcctServerConfigAcctPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAAAMasterAcctServerConfigAcctPort.setStatus("current")


class _QtechAAAMasterAcctServerConfigKeyStr_Type(DisplayString):
    """Custom type qtechAAAMasterAcctServerConfigKeyStr based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QtechAAAMasterAcctServerConfigKeyStr_Type.__name__ = "DisplayString"
_QtechAAAMasterAcctServerConfigKeyStr_Object = MibTableColumn
qtechAAAMasterAcctServerConfigKeyStr = _QtechAAAMasterAcctServerConfigKeyStr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 20, 1, 6),
    _QtechAAAMasterAcctServerConfigKeyStr_Type()
)
qtechAAAMasterAcctServerConfigKeyStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAAAMasterAcctServerConfigKeyStr.setStatus("current")
_QtechAAAMasterAcctServerConfigRowStatus_Type = RowStatus
_QtechAAAMasterAcctServerConfigRowStatus_Object = MibTableColumn
qtechAAAMasterAcctServerConfigRowStatus = _QtechAAAMasterAcctServerConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 20, 1, 7),
    _QtechAAAMasterAcctServerConfigRowStatus_Type()
)
qtechAAAMasterAcctServerConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAAAMasterAcctServerConfigRowStatus.setStatus("current")
_QtechAAABackAcctServerConfigTable_Object = MibTable
qtechAAABackAcctServerConfigTable = _QtechAAABackAcctServerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 21)
)
if mibBuilder.loadTexts:
    qtechAAABackAcctServerConfigTable.setStatus("current")
_QtechAAABackAcctServerConfigEntry_Object = MibTableRow
qtechAAABackAcctServerConfigEntry = _QtechAAABackAcctServerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 21, 1)
)
qtechAAABackAcctServerConfigEntry.setIndexNames(
    (0, "QTECH-AAA-MIB", "qtechAAABackAcctServerConfigGrpName"),
    (0, "QTECH-AAA-MIB", "qtechAAABackAcctServerConfigSrvIndex"),
)
if mibBuilder.loadTexts:
    qtechAAABackAcctServerConfigEntry.setStatus("current")


class _QtechAAABackAcctServerConfigGrpName_Type(DisplayString):
    """Custom type qtechAAABackAcctServerConfigGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_QtechAAABackAcctServerConfigGrpName_Type.__name__ = "DisplayString"
_QtechAAABackAcctServerConfigGrpName_Object = MibTableColumn
qtechAAABackAcctServerConfigGrpName = _QtechAAABackAcctServerConfigGrpName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 21, 1, 1),
    _QtechAAABackAcctServerConfigGrpName_Type()
)
qtechAAABackAcctServerConfigGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechAAABackAcctServerConfigGrpName.setStatus("current")


class _QtechAAABackAcctServerConfigSrvIndex_Type(Unsigned32):
    """Custom type qtechAAABackAcctServerConfigSrvIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_QtechAAABackAcctServerConfigSrvIndex_Type.__name__ = "Unsigned32"
_QtechAAABackAcctServerConfigSrvIndex_Object = MibTableColumn
qtechAAABackAcctServerConfigSrvIndex = _QtechAAABackAcctServerConfigSrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 21, 1, 2),
    _QtechAAABackAcctServerConfigSrvIndex_Type()
)
qtechAAABackAcctServerConfigSrvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechAAABackAcctServerConfigSrvIndex.setStatus("current")
_QtechAAABackAcctServerConfigAddress_Type = IpAddress
_QtechAAABackAcctServerConfigAddress_Object = MibTableColumn
qtechAAABackAcctServerConfigAddress = _QtechAAABackAcctServerConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 21, 1, 3),
    _QtechAAABackAcctServerConfigAddress_Type()
)
qtechAAABackAcctServerConfigAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAAABackAcctServerConfigAddress.setStatus("current")


class _QtechAAABackAcctServerConfigAuthPort_Type(Integer32):
    """Custom type qtechAAABackAcctServerConfigAuthPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QtechAAABackAcctServerConfigAuthPort_Type.__name__ = "Integer32"
_QtechAAABackAcctServerConfigAuthPort_Object = MibTableColumn
qtechAAABackAcctServerConfigAuthPort = _QtechAAABackAcctServerConfigAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 21, 1, 4),
    _QtechAAABackAcctServerConfigAuthPort_Type()
)
qtechAAABackAcctServerConfigAuthPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAAABackAcctServerConfigAuthPort.setStatus("current")


class _QtechAAABackAcctServerConfigAcctPort_Type(Integer32):
    """Custom type qtechAAABackAcctServerConfigAcctPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QtechAAABackAcctServerConfigAcctPort_Type.__name__ = "Integer32"
_QtechAAABackAcctServerConfigAcctPort_Object = MibTableColumn
qtechAAABackAcctServerConfigAcctPort = _QtechAAABackAcctServerConfigAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 21, 1, 5),
    _QtechAAABackAcctServerConfigAcctPort_Type()
)
qtechAAABackAcctServerConfigAcctPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAAABackAcctServerConfigAcctPort.setStatus("current")


class _QtechAAABackAcctServerConfigKeyStr_Type(DisplayString):
    """Custom type qtechAAABackAcctServerConfigKeyStr based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QtechAAABackAcctServerConfigKeyStr_Type.__name__ = "DisplayString"
_QtechAAABackAcctServerConfigKeyStr_Object = MibTableColumn
qtechAAABackAcctServerConfigKeyStr = _QtechAAABackAcctServerConfigKeyStr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 21, 1, 6),
    _QtechAAABackAcctServerConfigKeyStr_Type()
)
qtechAAABackAcctServerConfigKeyStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAAABackAcctServerConfigKeyStr.setStatus("current")
_QtechAAABackAcctServerConfigRowStatus_Type = RowStatus
_QtechAAABackAcctServerConfigRowStatus_Object = MibTableColumn
qtechAAABackAcctServerConfigRowStatus = _QtechAAABackAcctServerConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 21, 1, 7),
    _QtechAAABackAcctServerConfigRowStatus_Type()
)
qtechAAABackAcctServerConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAAABackAcctServerConfigRowStatus.setStatus("current")


class _QtechAAAServerTotalAuthUserCount_Type(Unsigned32):
    """Custom type qtechAAAServerTotalAuthUserCount based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_QtechAAAServerTotalAuthUserCount_Type.__name__ = "Unsigned32"
_QtechAAAServerTotalAuthUserCount_Object = MibScalar
qtechAAAServerTotalAuthUserCount = _QtechAAAServerTotalAuthUserCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 22),
    _QtechAAAServerTotalAuthUserCount_Type()
)
qtechAAAServerTotalAuthUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAAAServerTotalAuthUserCount.setStatus("current")


class _QtechAAAServerAuthSuccUserCount_Type(Unsigned32):
    """Custom type qtechAAAServerAuthSuccUserCount based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_QtechAAAServerAuthSuccUserCount_Type.__name__ = "Unsigned32"
_QtechAAAServerAuthSuccUserCount_Object = MibScalar
qtechAAAServerAuthSuccUserCount = _QtechAAAServerAuthSuccUserCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 23),
    _QtechAAAServerAuthSuccUserCount_Type()
)
qtechAAAServerAuthSuccUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAAAServerAuthSuccUserCount.setStatus("current")


class _QtechAAAServerDot1xOnlineUserCount_Type(Integer32):
    """Custom type qtechAAAServerDot1xOnlineUserCount based on Integer32"""
    defaultValue = 0


_QtechAAAServerDot1xOnlineUserCount_Type.__name__ = "Integer32"
_QtechAAAServerDot1xOnlineUserCount_Object = MibScalar
qtechAAAServerDot1xOnlineUserCount = _QtechAAAServerDot1xOnlineUserCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 24),
    _QtechAAAServerDot1xOnlineUserCount_Type()
)
qtechAAAServerDot1xOnlineUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAAAServerDot1xOnlineUserCount.setStatus("current")


class _QtechAAAServerMacOnlineUserCount_Type(Integer32):
    """Custom type qtechAAAServerMacOnlineUserCount based on Integer32"""
    defaultValue = 0


_QtechAAAServerMacOnlineUserCount_Type.__name__ = "Integer32"
_QtechAAAServerMacOnlineUserCount_Object = MibScalar
qtechAAAServerMacOnlineUserCount = _QtechAAAServerMacOnlineUserCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 25),
    _QtechAAAServerMacOnlineUserCount_Type()
)
qtechAAAServerMacOnlineUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAAAServerMacOnlineUserCount.setStatus("current")


class _QtechAAAServerWebOnlineUserCount_Type(Integer32):
    """Custom type qtechAAAServerWebOnlineUserCount based on Integer32"""
    defaultValue = 0


_QtechAAAServerWebOnlineUserCount_Type.__name__ = "Integer32"
_QtechAAAServerWebOnlineUserCount_Object = MibScalar
qtechAAAServerWebOnlineUserCount = _QtechAAAServerWebOnlineUserCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 26),
    _QtechAAAServerWebOnlineUserCount_Type()
)
qtechAAAServerWebOnlineUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAAAServerWebOnlineUserCount.setStatus("current")


class _QtechAAAServerTatalOnlineUserCount_Type(Integer32):
    """Custom type qtechAAAServerTatalOnlineUserCount based on Integer32"""
    defaultValue = 0


_QtechAAAServerTatalOnlineUserCount_Type.__name__ = "Integer32"
_QtechAAAServerTatalOnlineUserCount_Object = MibScalar
qtechAAAServerTatalOnlineUserCount = _QtechAAAServerTatalOnlineUserCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 27),
    _QtechAAAServerTatalOnlineUserCount_Type()
)
qtechAAAServerTatalOnlineUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAAAServerTatalOnlineUserCount.setStatus("current")
_QtechAAAServerIfOnlineUserTable_Object = MibTable
qtechAAAServerIfOnlineUserTable = _QtechAAAServerIfOnlineUserTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 28)
)
if mibBuilder.loadTexts:
    qtechAAAServerIfOnlineUserTable.setStatus("current")
_QtechAAAServerIfOnlineUserEntry_Object = MibTableRow
qtechAAAServerIfOnlineUserEntry = _QtechAAAServerIfOnlineUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 28, 1)
)
qtechAAAServerIfOnlineUserEntry.setIndexNames(
    (0, "QTECH-AAA-MIB", "qtechAAAServerIfOnlineUserIfIndex"),
)
if mibBuilder.loadTexts:
    qtechAAAServerIfOnlineUserEntry.setStatus("current")


class _QtechAAAServerIfOnlineUserIfIndex_Type(Unsigned32):
    """Custom type qtechAAAServerIfOnlineUserIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_QtechAAAServerIfOnlineUserIfIndex_Type.__name__ = "Unsigned32"
_QtechAAAServerIfOnlineUserIfIndex_Object = MibTableColumn
qtechAAAServerIfOnlineUserIfIndex = _QtechAAAServerIfOnlineUserIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 28, 1, 1),
    _QtechAAAServerIfOnlineUserIfIndex_Type()
)
qtechAAAServerIfOnlineUserIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechAAAServerIfOnlineUserIfIndex.setStatus("current")


class _QtechAAAServerIfOnlineUserDot1xCount_Type(Unsigned32):
    """Custom type qtechAAAServerIfOnlineUserDot1xCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_QtechAAAServerIfOnlineUserDot1xCount_Type.__name__ = "Unsigned32"
_QtechAAAServerIfOnlineUserDot1xCount_Object = MibTableColumn
qtechAAAServerIfOnlineUserDot1xCount = _QtechAAAServerIfOnlineUserDot1xCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 28, 1, 2),
    _QtechAAAServerIfOnlineUserDot1xCount_Type()
)
qtechAAAServerIfOnlineUserDot1xCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAAAServerIfOnlineUserDot1xCount.setStatus("current")


class _QtechAAAServerIfOnlineUserWebCount_Type(Unsigned32):
    """Custom type qtechAAAServerIfOnlineUserWebCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_QtechAAAServerIfOnlineUserWebCount_Type.__name__ = "Unsigned32"
_QtechAAAServerIfOnlineUserWebCount_Object = MibTableColumn
qtechAAAServerIfOnlineUserWebCount = _QtechAAAServerIfOnlineUserWebCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 28, 1, 3),
    _QtechAAAServerIfOnlineUserWebCount_Type()
)
qtechAAAServerIfOnlineUserWebCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAAAServerIfOnlineUserWebCount.setStatus("current")


class _QtechAAAServerIfOnlineUserMacCount_Type(Unsigned32):
    """Custom type qtechAAAServerIfOnlineUserMacCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_QtechAAAServerIfOnlineUserMacCount_Type.__name__ = "Unsigned32"
_QtechAAAServerIfOnlineUserMacCount_Object = MibTableColumn
qtechAAAServerIfOnlineUserMacCount = _QtechAAAServerIfOnlineUserMacCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 28, 1, 4),
    _QtechAAAServerIfOnlineUserMacCount_Type()
)
qtechAAAServerIfOnlineUserMacCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAAAServerIfOnlineUserMacCount.setStatus("current")


class _QtechAAAServerIfOnlineUserTotalCount_Type(Unsigned32):
    """Custom type qtechAAAServerIfOnlineUserTotalCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_QtechAAAServerIfOnlineUserTotalCount_Type.__name__ = "Unsigned32"
_QtechAAAServerIfOnlineUserTotalCount_Object = MibTableColumn
qtechAAAServerIfOnlineUserTotalCount = _QtechAAAServerIfOnlineUserTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 2, 28, 1, 5),
    _QtechAAAServerIfOnlineUserTotalCount_Type()
)
qtechAAAServerIfOnlineUserTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAAAServerIfOnlineUserTotalCount.setStatus("current")
_QtechAuthUserObjects_ObjectIdentity = ObjectIdentity
qtechAuthUserObjects = _QtechAuthUserObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 3)
)
_QtechAuthAddrTable_Object = MibTable
qtechAuthAddrTable = _QtechAuthAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 3, 1)
)
if mibBuilder.loadTexts:
    qtechAuthAddrTable.setStatus("current")
_QtechAuthAddrEntry_Object = MibTableRow
qtechAuthAddrEntry = _QtechAuthAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 3, 1, 1)
)
qtechAuthAddrEntry.setIndexNames(
    (0, "QTECH-AAA-MIB", "qtechAuthPort"),
    (0, "QTECH-AAA-MIB", "qtechAuthMacAddress"),
)
if mibBuilder.loadTexts:
    qtechAuthAddrEntry.setStatus("current")
_QtechAuthPort_Type = IfIndex
_QtechAuthPort_Object = MibTableColumn
qtechAuthPort = _QtechAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 3, 1, 1, 1),
    _QtechAuthPort_Type()
)
qtechAuthPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAuthPort.setStatus("current")
_QtechAuthMacAddress_Type = MacAddress
_QtechAuthMacAddress_Object = MibTableColumn
qtechAuthMacAddress = _QtechAuthMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 3, 1, 1, 2),
    _QtechAuthMacAddress_Type()
)
qtechAuthMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAuthMacAddress.setStatus("current")


class _QtechAuthAddrStatus_Type(Integer32):
    """Custom type qtechAuthAddrStatus based on Integer32"""
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


_QtechAuthAddrStatus_Type.__name__ = "Integer32"
_QtechAuthAddrStatus_Object = MibTableColumn
qtechAuthAddrStatus = _QtechAuthAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 3, 1, 1, 3),
    _QtechAuthAddrStatus_Type()
)
qtechAuthAddrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAuthAddrStatus.setStatus("current")
_QtechAuthUserTable_Object = MibTable
qtechAuthUserTable = _QtechAuthUserTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 3, 2)
)
if mibBuilder.loadTexts:
    qtechAuthUserTable.setStatus("current")
_QtechAuthUserEntry_Object = MibTableRow
qtechAuthUserEntry = _QtechAuthUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 3, 2, 1)
)
qtechAuthUserEntry.setIndexNames(
    (0, "QTECH-AAA-MIB", "qtechAuthUserFdbId"),
    (0, "QTECH-AAA-MIB", "qtechAuthUserMacAddress"),
)
if mibBuilder.loadTexts:
    qtechAuthUserEntry.setStatus("current")
_QtechAuthUserFdbId_Type = Unsigned32
_QtechAuthUserFdbId_Object = MibTableColumn
qtechAuthUserFdbId = _QtechAuthUserFdbId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 3, 2, 1, 1),
    _QtechAuthUserFdbId_Type()
)
qtechAuthUserFdbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAuthUserFdbId.setStatus("current")
_QtechAuthUserMacAddress_Type = MacAddress
_QtechAuthUserMacAddress_Object = MibTableColumn
qtechAuthUserMacAddress = _QtechAuthUserMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 3, 2, 1, 2),
    _QtechAuthUserMacAddress_Type()
)
qtechAuthUserMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAuthUserMacAddress.setStatus("current")
_QtechAuthUserName_Type = DisplayString
_QtechAuthUserName_Object = MibTableColumn
qtechAuthUserName = _QtechAuthUserName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 3, 2, 1, 3),
    _QtechAuthUserName_Type()
)
qtechAuthUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAuthUserName.setStatus("current")
_QtechAuthUserSessionId_Type = DisplayString
_QtechAuthUserSessionId_Object = MibTableColumn
qtechAuthUserSessionId = _QtechAuthUserSessionId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 3, 2, 1, 4),
    _QtechAuthUserSessionId_Type()
)
qtechAuthUserSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAuthUserSessionId.setStatus("current")
_QtechAuthUserIpAddr_Type = IpAddress
_QtechAuthUserIpAddr_Object = MibTableColumn
qtechAuthUserIpAddr = _QtechAuthUserIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 3, 2, 1, 5),
    _QtechAuthUserIpAddr_Type()
)
qtechAuthUserIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAuthUserIpAddr.setStatus("current")
_QtechAuthUserPort_Type = Integer32
_QtechAuthUserPort_Object = MibTableColumn
qtechAuthUserPort = _QtechAuthUserPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 3, 2, 1, 6),
    _QtechAuthUserPort_Type()
)
qtechAuthUserPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAuthUserPort.setStatus("current")
_QtechAuthUserStatus_Type = ConfigStatus
_QtechAuthUserStatus_Object = MibTableColumn
qtechAuthUserStatus = _QtechAuthUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 3, 2, 1, 7),
    _QtechAuthUserStatus_Type()
)
qtechAuthUserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAuthUserStatus.setStatus("current")


class _QtechAuthUserForVPNDel_Type(DisplayString):
    """Custom type qtechAuthUserForVPNDel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_QtechAuthUserForVPNDel_Type.__name__ = "DisplayString"
_QtechAuthUserForVPNDel_Object = MibScalar
qtechAuthUserForVPNDel = _QtechAuthUserForVPNDel_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 3, 3),
    _QtechAuthUserForVPNDel_Type()
)
qtechAuthUserForVPNDel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAuthUserForVPNDel.setStatus("current")
_QtechAuthModeObjects_ObjectIdentity = ObjectIdentity
qtechAuthModeObjects = _QtechAuthModeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 4)
)


class _QtechIpAuthorizationMode_Type(Integer32):
    """Custom type qtechIpAuthorizationMode based on Integer32"""
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
        *(("disable", 1),
          ("dhcpServer", 2),
          ("radiusServer", 3),
          ("supplicant", 4))
    )


_QtechIpAuthorizationMode_Type.__name__ = "Integer32"
_QtechIpAuthorizationMode_Object = MibScalar
qtechIpAuthorizationMode = _QtechIpAuthorizationMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 4, 1),
    _QtechIpAuthorizationMode_Type()
)
qtechIpAuthorizationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIpAuthorizationMode.setStatus("current")
_QtechClientProbeObjects_ObjectIdentity = ObjectIdentity
qtechClientProbeObjects = _QtechClientProbeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 5)
)
_QtechClientProbeEnabledStatus_Type = EnabledStatus
_QtechClientProbeEnabledStatus_Object = MibScalar
qtechClientProbeEnabledStatus = _QtechClientProbeEnabledStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 5, 1),
    _QtechClientProbeEnabledStatus_Type()
)
qtechClientProbeEnabledStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechClientProbeEnabledStatus.setStatus("current")
_QtechClientProbeHelloInterval_Type = Unsigned32
_QtechClientProbeHelloInterval_Object = MibScalar
qtechClientProbeHelloInterval = _QtechClientProbeHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 5, 2),
    _QtechClientProbeHelloInterval_Type()
)
qtechClientProbeHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechClientProbeHelloInterval.setStatus("current")
_QtechClientProbeAliveInteval_Type = Unsigned32
_QtechClientProbeAliveInteval_Object = MibScalar
qtechClientProbeAliveInteval = _QtechClientProbeAliveInteval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 5, 3),
    _QtechClientProbeAliveInteval_Type()
)
qtechClientProbeAliveInteval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechClientProbeAliveInteval.setStatus("current")
_QtechAAAConfigObjects_ObjectIdentity = ObjectIdentity
qtechAAAConfigObjects = _QtechAAAConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 6)
)
_QtechAuthenConfigObjects_ObjectIdentity = ObjectIdentity
qtechAuthenConfigObjects = _QtechAuthenConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 6, 1)
)
_QtechAuthenMethodListTable_Object = MibTable
qtechAuthenMethodListTable = _QtechAuthenMethodListTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    qtechAuthenMethodListTable.setStatus("current")
_QtechAuthenMethodListEntry_Object = MibTableRow
qtechAuthenMethodListEntry = _QtechAuthenMethodListEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 6, 1, 1, 1)
)
qtechAuthenMethodListEntry.setIndexNames(
    (0, "QTECH-AAA-MIB", "qtechAuthenMethodListType"),
    (0, "QTECH-AAA-MIB", "qtechAuthenMethodListName"),
)
if mibBuilder.loadTexts:
    qtechAuthenMethodListEntry.setStatus("current")


class _QtechAuthenMethodListType_Type(Integer32):
    """Custom type qtechAuthenMethodListType based on Integer32"""
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
        *(("login", 1),
          ("ppp", 2),
          ("dot1x", 3),
          ("enable", 4),
          ("web", 5),
          ("cmweb", 6),
          ("mt", 7))
    )


_QtechAuthenMethodListType_Type.__name__ = "Integer32"
_QtechAuthenMethodListType_Object = MibTableColumn
qtechAuthenMethodListType = _QtechAuthenMethodListType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 6, 1, 1, 1, 1),
    _QtechAuthenMethodListType_Type()
)
qtechAuthenMethodListType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAuthenMethodListType.setStatus("current")


class _QtechAuthenMethodListName_Type(DisplayString):
    """Custom type qtechAuthenMethodListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_QtechAuthenMethodListName_Type.__name__ = "DisplayString"
_QtechAuthenMethodListName_Object = MibTableColumn
qtechAuthenMethodListName = _QtechAuthenMethodListName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 6, 1, 1, 1, 2),
    _QtechAuthenMethodListName_Type()
)
qtechAuthenMethodListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAuthenMethodListName.setStatus("current")


class _QtechAuthenMethodListString_Type(DisplayString):
    """Custom type qtechAuthenMethodListString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_QtechAuthenMethodListString_Type.__name__ = "DisplayString"
_QtechAuthenMethodListString_Object = MibTableColumn
qtechAuthenMethodListString = _QtechAuthenMethodListString_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 6, 1, 1, 1, 3),
    _QtechAuthenMethodListString_Type()
)
qtechAuthenMethodListString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAuthenMethodListString.setStatus("current")
_QtechAuthenMethodListRowStatus_Type = RowStatus
_QtechAuthenMethodListRowStatus_Object = MibTableColumn
qtechAuthenMethodListRowStatus = _QtechAuthenMethodListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 6, 1, 1, 1, 4),
    _QtechAuthenMethodListRowStatus_Type()
)
qtechAuthenMethodListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAuthenMethodListRowStatus.setStatus("current")
_QtechAuthorConfigObjects_ObjectIdentity = ObjectIdentity
qtechAuthorConfigObjects = _QtechAuthorConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 6, 2)
)
_QtechAuthorMethodListTable_Object = MibTable
qtechAuthorMethodListTable = _QtechAuthorMethodListTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    qtechAuthorMethodListTable.setStatus("current")
_QtechAuthorMethodListEntry_Object = MibTableRow
qtechAuthorMethodListEntry = _QtechAuthorMethodListEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 6, 2, 1, 1)
)
qtechAuthorMethodListEntry.setIndexNames(
    (0, "QTECH-AAA-MIB", "qtechAuthorMethodListType"),
    (0, "QTECH-AAA-MIB", "qtechAuthorMethodListName"),
    (0, "QTECH-AAA-MIB", "qtechAuthorMethodListCmdLevel"),
)
if mibBuilder.loadTexts:
    qtechAuthorMethodListEntry.setStatus("current")


class _QtechAuthorMethodListType_Type(Integer32):
    """Custom type qtechAuthorMethodListType based on Integer32"""
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


_QtechAuthorMethodListType_Type.__name__ = "Integer32"
_QtechAuthorMethodListType_Object = MibTableColumn
qtechAuthorMethodListType = _QtechAuthorMethodListType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 6, 2, 1, 1, 1),
    _QtechAuthorMethodListType_Type()
)
qtechAuthorMethodListType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAuthorMethodListType.setStatus("current")


class _QtechAuthorMethodListName_Type(DisplayString):
    """Custom type qtechAuthorMethodListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_QtechAuthorMethodListName_Type.__name__ = "DisplayString"
_QtechAuthorMethodListName_Object = MibTableColumn
qtechAuthorMethodListName = _QtechAuthorMethodListName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 6, 2, 1, 1, 2),
    _QtechAuthorMethodListName_Type()
)
qtechAuthorMethodListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAuthorMethodListName.setStatus("current")


class _QtechAuthorMethodListCmdLevel_Type(Integer32):
    """Custom type qtechAuthorMethodListCmdLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_QtechAuthorMethodListCmdLevel_Type.__name__ = "Integer32"
_QtechAuthorMethodListCmdLevel_Object = MibTableColumn
qtechAuthorMethodListCmdLevel = _QtechAuthorMethodListCmdLevel_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 6, 2, 1, 1, 3),
    _QtechAuthorMethodListCmdLevel_Type()
)
qtechAuthorMethodListCmdLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAuthorMethodListCmdLevel.setStatus("current")


class _QtechAuthorMethodListString_Type(DisplayString):
    """Custom type qtechAuthorMethodListString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_QtechAuthorMethodListString_Type.__name__ = "DisplayString"
_QtechAuthorMethodListString_Object = MibTableColumn
qtechAuthorMethodListString = _QtechAuthorMethodListString_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 6, 2, 1, 1, 4),
    _QtechAuthorMethodListString_Type()
)
qtechAuthorMethodListString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAuthorMethodListString.setStatus("current")
_QtechAuthorMethodListRowStatus_Type = RowStatus
_QtechAuthorMethodListRowStatus_Object = MibTableColumn
qtechAuthorMethodListRowStatus = _QtechAuthorMethodListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 6, 2, 1, 1, 5),
    _QtechAuthorMethodListRowStatus_Type()
)
qtechAuthorMethodListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAuthorMethodListRowStatus.setStatus("current")
_QtechAcctConfigObjects_ObjectIdentity = ObjectIdentity
qtechAcctConfigObjects = _QtechAcctConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 6, 3)
)
_QtechAcctMethodListTable_Object = MibTable
qtechAcctMethodListTable = _QtechAcctMethodListTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 6, 3, 1)
)
if mibBuilder.loadTexts:
    qtechAcctMethodListTable.setStatus("current")
_QtechAcctMethodListEntry_Object = MibTableRow
qtechAcctMethodListEntry = _QtechAcctMethodListEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 6, 3, 1, 1)
)
qtechAcctMethodListEntry.setIndexNames(
    (0, "QTECH-AAA-MIB", "qtechAcctMethodListType"),
    (0, "QTECH-AAA-MIB", "qtechAcctMethodListName"),
    (0, "QTECH-AAA-MIB", "qtechAcctMethodListCmdLevel"),
)
if mibBuilder.loadTexts:
    qtechAcctMethodListEntry.setStatus("current")


class _QtechAcctMethodListType_Type(Integer32):
    """Custom type qtechAcctMethodListType based on Integer32"""
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


_QtechAcctMethodListType_Type.__name__ = "Integer32"
_QtechAcctMethodListType_Object = MibTableColumn
qtechAcctMethodListType = _QtechAcctMethodListType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 6, 3, 1, 1, 1),
    _QtechAcctMethodListType_Type()
)
qtechAcctMethodListType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcctMethodListType.setStatus("current")


class _QtechAcctMethodListName_Type(DisplayString):
    """Custom type qtechAcctMethodListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_QtechAcctMethodListName_Type.__name__ = "DisplayString"
_QtechAcctMethodListName_Object = MibTableColumn
qtechAcctMethodListName = _QtechAcctMethodListName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 6, 3, 1, 1, 2),
    _QtechAcctMethodListName_Type()
)
qtechAcctMethodListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcctMethodListName.setStatus("current")


class _QtechAcctMethodListMode_Type(Integer32):
    """Custom type qtechAcctMethodListMode based on Integer32"""
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


_QtechAcctMethodListMode_Type.__name__ = "Integer32"
_QtechAcctMethodListMode_Object = MibTableColumn
qtechAcctMethodListMode = _QtechAcctMethodListMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 6, 3, 1, 1, 3),
    _QtechAcctMethodListMode_Type()
)
qtechAcctMethodListMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAcctMethodListMode.setStatus("current")


class _QtechAcctMethodListCmdLevel_Type(Integer32):
    """Custom type qtechAcctMethodListCmdLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_QtechAcctMethodListCmdLevel_Type.__name__ = "Integer32"
_QtechAcctMethodListCmdLevel_Object = MibTableColumn
qtechAcctMethodListCmdLevel = _QtechAcctMethodListCmdLevel_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 6, 3, 1, 1, 4),
    _QtechAcctMethodListCmdLevel_Type()
)
qtechAcctMethodListCmdLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcctMethodListCmdLevel.setStatus("current")


class _QtechAcctMethodListString_Type(DisplayString):
    """Custom type qtechAcctMethodListString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_QtechAcctMethodListString_Type.__name__ = "DisplayString"
_QtechAcctMethodListString_Object = MibTableColumn
qtechAcctMethodListString = _QtechAcctMethodListString_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 6, 3, 1, 1, 5),
    _QtechAcctMethodListString_Type()
)
qtechAcctMethodListString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAcctMethodListString.setStatus("current")
_QtechAcctMethodListRowStatus_Type = RowStatus
_QtechAcctMethodListRowStatus_Object = MibTableColumn
qtechAcctMethodListRowStatus = _QtechAcctMethodListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 6, 3, 1, 1, 6),
    _QtechAcctMethodListRowStatus_Type()
)
qtechAcctMethodListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAcctMethodListRowStatus.setStatus("current")
_QtechAAAUserApplyObjects_ObjectIdentity = ObjectIdentity
qtechAAAUserApplyObjects = _QtechAAAUserApplyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 7)
)
_QtechAAADo1xApplyObjects_ObjectIdentity = ObjectIdentity
qtechAAADo1xApplyObjects = _QtechAAADo1xApplyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 7, 1)
)


class _QtechDot1xAuthenMethodList_Type(DisplayString):
    """Custom type qtechDot1xAuthenMethodList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_QtechDot1xAuthenMethodList_Type.__name__ = "DisplayString"
_QtechDot1xAuthenMethodList_Object = MibScalar
qtechDot1xAuthenMethodList = _QtechDot1xAuthenMethodList_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 7, 1, 1),
    _QtechDot1xAuthenMethodList_Type()
)
qtechDot1xAuthenMethodList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot1xAuthenMethodList.setStatus("current")


class _QtechDot1xAuthorMethodList_Type(DisplayString):
    """Custom type qtechDot1xAuthorMethodList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_QtechDot1xAuthorMethodList_Type.__name__ = "DisplayString"
_QtechDot1xAuthorMethodList_Object = MibScalar
qtechDot1xAuthorMethodList = _QtechDot1xAuthorMethodList_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 7, 1, 2),
    _QtechDot1xAuthorMethodList_Type()
)
qtechDot1xAuthorMethodList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot1xAuthorMethodList.setStatus("current")


class _QtechDot1xAcctMethodList_Type(DisplayString):
    """Custom type qtechDot1xAcctMethodList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_QtechDot1xAcctMethodList_Type.__name__ = "DisplayString"
_QtechDot1xAcctMethodList_Object = MibScalar
qtechDot1xAcctMethodList = _QtechDot1xAcctMethodList_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 7, 1, 3),
    _QtechDot1xAcctMethodList_Type()
)
qtechDot1xAcctMethodList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot1xAcctMethodList.setStatus("current")
_QtechRdASObjects_ObjectIdentity = ObjectIdentity
qtechRdASObjects = _QtechRdASObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 8)
)
_QtechRdASipInetAddreType_Type = InetAddressType
_QtechRdASipInetAddreType_Object = MibScalar
qtechRdASipInetAddreType = _QtechRdASipInetAddreType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 8, 1),
    _QtechRdASipInetAddreType_Type()
)
qtechRdASipInetAddreType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRdASipInetAddreType.setStatus("current")
_QtechRdASipInsetAddres_Type = InetAddress
_QtechRdASipInsetAddres_Object = MibScalar
qtechRdASipInsetAddres = _QtechRdASipInsetAddres_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 8, 2),
    _QtechRdASipInsetAddres_Type()
)
qtechRdASipInsetAddres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRdASipInsetAddres.setStatus("current")
_QtechAAAMIBConformance_ObjectIdentity = ObjectIdentity
qtechAAAMIBConformance = _QtechAAAMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 2)
)
_QtechAAAMIBCompliances_ObjectIdentity = ObjectIdentity
qtechAAAMIBCompliances = _QtechAAAMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 2, 1)
)
_QtechAAAMIBGroups_ObjectIdentity = ObjectIdentity
qtechAAAMIBGroups = _QtechAAAMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 2, 2)
)

# Managed Objects groups

qtechDot1xAuthMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 2, 2, 1)
)
qtechDot1xAuthMIBGroup.setObjects(
      *(("QTECH-AAA-MIB", "qtechDot1xAuthStatus"),
        ("QTECH-AAA-MIB", "qtechDot1xAuthObjectsQuietPeriod"),
        ("QTECH-AAA-MIB", "qtechDot1xAuthObjectsTxPeriod"),
        ("QTECH-AAA-MIB", "qtechDot1xAuthObjectsSuppTimeout"),
        ("QTECH-AAA-MIB", "qtechDot1xAuthObjectsServerTimeout"),
        ("QTECH-AAA-MIB", "qtechDot1xAuthObjectsMaxReq"),
        ("QTECH-AAA-MIB", "qtechDot1xAuthObjectsReAuthPeriod"),
        ("QTECH-AAA-MIB", "qtechDot1xAuthObjectsReAuthEnable"),
        ("QTECH-AAA-MIB", "qtechDot1xAuthObjectsConfigFdbId"),
        ("QTECH-AAA-MIB", "qtechDot1xAuthObjectsConfigAddr"),
        ("QTECH-AAA-MIB", "qtechDot1xAuthObjectsPaeState"),
        ("QTECH-AAA-MIB", "qtechDot1xAuthObjectsBackendAuthState"),
        ("QTECH-AAA-MIB", "qtechDot1xAuthObjectsAuthControlledPortStatus"),
        ("QTECH-AAA-MIB", "qtechDot1xAuthObjectsKeyTxEnabled"),
        ("QTECH-AAA-MIB", "qtechDot1xAuthObjectsIfIndex"),
        ("QTECH-AAA-MIB", "qtechDot1xAuthObjectsStatsFdbId"),
        ("QTECH-AAA-MIB", "qtechDot1xAuthObjectsStatsAddr"),
        ("QTECH-AAA-MIB", "qtechDot1xAuthObjectsEapolFramesRx"),
        ("QTECH-AAA-MIB", "qtechDot1xAuthObjectsEapolFramesTx"),
        ("QTECH-AAA-MIB", "qtechDot1xAuthObjectsEapolQtechFramesRx"),
        ("QTECH-AAA-MIB", "qtechDot1xAuthObjectsEapolLogoffFramesRx"),
        ("QTECH-AAA-MIB", "qtechDot1xAuthObjectsEapolRespIdFramesRx"),
        ("QTECH-AAA-MIB", "qtechDot1xAuthObjectsEapolRespFramesRx"),
        ("QTECH-AAA-MIB", "qtechDot1xAuthObjectsEapolReqIdFramesTx"),
        ("QTECH-AAA-MIB", "qtechDot1xAuthObjectsEapolReqFramesTx"),
        ("QTECH-AAA-MIB", "qtechDot1xAuthObjectsInvalidEapolFramesRx"),
        ("QTECH-AAA-MIB", "qtechDot1xAuthObjectsEapLengthErrorFramesRx"),
        ("QTECH-AAA-MIB", "qtechDot1xAuthObjectsLastEapolFrameVersion"),
        ("QTECH-AAA-MIB", "qtechDot1xAuthObjectsLastEapolFrameSource"),
        ("QTECH-AAA-MIB", "qtechDot1xCurrentUserNumber"),
        ("QTECH-AAA-MIB", "qtechDot1xCurrentAuthenticatedUserNumber"),
        ("QTECH-AAA-MIB", "qtechDot1xAuthObjectsMaxReauth"),
        ("QTECH-AAA-MIB", "qtechAuthIf"),
        ("QTECH-AAA-MIB", "qtechAuthIfStatus"),
        ("QTECH-AAA-MIB", "qtechAuthenticationMode"),
        ("QTECH-AAA-MIB", "qtechDot1xPseudoSrcmac"),
        ("QTECH-AAA-MIB", "qtechDot1xAbnormalOfflineUserCount"),
        ("QTECH-AAA-MIB", "qtechDot1xTotalAuthUserCount"),
        ("QTECH-AAA-MIB", "qtechDot1xAuthSuccUserCount"),
        ("QTECH-AAA-MIB", "qtechDot1xAuthFailUserCount"))
)
if mibBuilder.loadTexts:
    qtechDot1xAuthMIBGroup.setStatus("current")

qtechAAAServerMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 2, 2, 2)
)
qtechAAAServerMIBGroup.setObjects(
      *(("QTECH-AAA-MIB", "qtechAAAServerAuthPort"),
        ("QTECH-AAA-MIB", "qtechAAAServerAcctPort"),
        ("QTECH-AAA-MIB", "qtechAAAServerRadiusKeyStr"),
        ("QTECH-AAA-MIB", "qtechAAAServerTacplusKeyStr"),
        ("QTECH-AAA-MIB", "qtechAAAServerConfigAddressType"),
        ("QTECH-AAA-MIB", "qtechAAAServerConfigAddress"),
        ("QTECH-AAA-MIB", "qtechAAAServerConfigAuthPort"),
        ("QTECH-AAA-MIB", "qtechAAAServerConfigAcctPort"),
        ("QTECH-AAA-MIB", "qtechAAAServerConfigKeyStr"),
        ("QTECH-AAA-MIB", "qtechAAAServerConfigRowStatus"))
)
if mibBuilder.loadTexts:
    qtechAAAServerMIBGroup.setStatus("current")

qtechAuthAddrMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 2, 2, 3)
)
qtechAuthAddrMIBGroup.setObjects(
      *(("QTECH-AAA-MIB", "qtechAuthMacAddress"),
        ("QTECH-AAA-MIB", "qtechAuthPort"),
        ("QTECH-AAA-MIB", "qtechAuthAddrStatus"),
        ("QTECH-AAA-MIB", "qtechAuthUserFdbId"),
        ("QTECH-AAA-MIB", "qtechAuthUserMacAddress"),
        ("QTECH-AAA-MIB", "qtechAuthUserName"),
        ("QTECH-AAA-MIB", "qtechAuthUserSessionId"),
        ("QTECH-AAA-MIB", "qtechAuthUserIpAddr"),
        ("QTECH-AAA-MIB", "qtechAuthUserPort"),
        ("QTECH-AAA-MIB", "qtechAuthUserStatus"))
)
if mibBuilder.loadTexts:
    qtechAuthAddrMIBGroup.setStatus("current")

qtechAuthModeMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 2, 2, 4)
)
qtechAuthModeMIBGroup.setObjects(
    ("QTECH-AAA-MIB", "qtechIpAuthorizationMode")
)
if mibBuilder.loadTexts:
    qtechAuthModeMIBGroup.setStatus("current")

qtechClientProbeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 2, 2, 5)
)
qtechClientProbeGroup.setObjects(
      *(("QTECH-AAA-MIB", "qtechClientProbeEnabledStatus"),
        ("QTECH-AAA-MIB", "qtechClientProbeHelloInterval"),
        ("QTECH-AAA-MIB", "qtechClientProbeAliveInteval"))
)
if mibBuilder.loadTexts:
    qtechClientProbeGroup.setStatus("current")

qtechAAAConfigMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 2, 2, 6)
)
qtechAAAConfigMIBGroup.setObjects(
      *(("QTECH-AAA-MIB", "qtechAuthenMethodListType"),
        ("QTECH-AAA-MIB", "qtechAuthenMethodListName"),
        ("QTECH-AAA-MIB", "qtechAuthenMethodListString"),
        ("QTECH-AAA-MIB", "qtechAuthenMethodListRowStatus"),
        ("QTECH-AAA-MIB", "qtechAuthorMethodListType"),
        ("QTECH-AAA-MIB", "qtechAuthorMethodListName"),
        ("QTECH-AAA-MIB", "qtechAuthorMethodListCmdLevel"),
        ("QTECH-AAA-MIB", "qtechAuthorMethodListString"),
        ("QTECH-AAA-MIB", "qtechAuthorMethodListRowStatus"),
        ("QTECH-AAA-MIB", "qtechAcctMethodListType"),
        ("QTECH-AAA-MIB", "qtechAcctMethodListName"),
        ("QTECH-AAA-MIB", "qtechAcctMethodListMode"),
        ("QTECH-AAA-MIB", "qtechAcctMethodListCmdLevel"),
        ("QTECH-AAA-MIB", "qtechAcctMethodListString"),
        ("QTECH-AAA-MIB", "qtechAcctMethodListRowStatus"),
        ("QTECH-AAA-MIB", "qtechAAARadiusGroupName"),
        ("QTECH-AAA-MIB", "qtechAAARadiusGroupVrf"),
        ("QTECH-AAA-MIB", "qtechAAARadiusGroupRowStatus"),
        ("QTECH-AAA-MIB", "qtechAAARadiusGroupServerAddressType"),
        ("QTECH-AAA-MIB", "qtechAAARadiusGroupServerAddress"),
        ("QTECH-AAA-MIB", "qtechAAARadiusGroupServerAuthPort"),
        ("QTECH-AAA-MIB", "qtechAAARadiusGroupServerAcctPort"),
        ("QTECH-AAA-MIB", "qtechAAARadiusGroupServerRowStatus"))
)
if mibBuilder.loadTexts:
    qtechAAAConfigMIBGroup.setStatus("current")

qtechAAAUserApplyMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 2, 2, 7)
)
qtechAAAUserApplyMIBGroup.setObjects(
      *(("QTECH-AAA-MIB", "qtechDot1xAuthenMethodList"),
        ("QTECH-AAA-MIB", "qtechDot1xAuthorMethodList"),
        ("QTECH-AAA-MIB", "qtechDot1xAcctMethodList"))
)
if mibBuilder.loadTexts:
    qtechAAAUserApplyMIBGroup.setStatus("current")

qtechRdASGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 2, 2, 8)
)
qtechRdASGroup.setObjects(
      *(("QTECH-AAA-MIB", "qtechRdASipInetAddreType"),
        ("QTECH-AAA-MIB", "qtechRdASipInsetAddres"))
)
if mibBuilder.loadTexts:
    qtechRdASGroup.setStatus("current")


# Notification objects

qtechRadiusAuthServerDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 0, 1)
)
qtechRadiusAuthServerDownTrap.setObjects(
      *(("RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerAddress"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientServerPortNumber"))
)
if mibBuilder.loadTexts:
    qtechRadiusAuthServerDownTrap.setStatus(
        "current"
    )

qtechRadiusAccServerDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 0, 2)
)
qtechRadiusAccServerDownTrap.setObjects(
      *(("RADIUS-ACC-CLIENT-MIB", "radiusAccServerAddress"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientServerPortNumber"))
)
if mibBuilder.loadTexts:
    qtechRadiusAccServerDownTrap.setStatus(
        "current"
    )

qtechRadiusAuthServerRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 0, 3)
)
qtechRadiusAuthServerRecoverTrap.setObjects(
      *(("RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerAddress"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientServerPortNumber"))
)
if mibBuilder.loadTexts:
    qtechRadiusAuthServerRecoverTrap.setStatus(
        "current"
    )

qtechRadiusAccServerRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 0, 4)
)
qtechRadiusAccServerRecoverTrap.setObjects(
      *(("RADIUS-ACC-CLIENT-MIB", "radiusAccServerAddress"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientServerPortNumber"))
)
if mibBuilder.loadTexts:
    qtechRadiusAccServerRecoverTrap.setStatus(
        "current"
    )

qtechDot1xUserMgmtTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 22, 2, 1)
)
qtechDot1xUserMgmtTrap.setObjects(
      *(("QTECH-AAA-MIB", "qtechDot1xUserMac"),
        ("QTECH-AAA-MIB", "qtechDot1xUserName"),
        ("QTECH-AAA-MIB", "qtechDot1xUserIp"),
        ("QTECH-AAA-MIB", "qtechDot1xUserIpv6"),
        ("QTECH-AAA-MIB", "qtechDot1xUserWlanId"),
        ("QTECH-AAA-MIB", "qtechDot1xUserVlanId"),
        ("QTECH-AAA-MIB", "qtechDot1xUserSsid"),
        ("QTECH-AAA-MIB", "qtechDot1xUserApMac"),
        ("QTECH-AAA-MIB", "qtechDot1xUserTerminalType"),
        ("QTECH-AAA-MIB", "qtechDot1xUserOperType"),
        ("QTECH-AAA-MIB", "qtechDot1xUserTerminateCause"),
        ("QTECH-AAA-MIB", "qtechDot1xUserReplyMessage"),
        ("QTECH-AAA-MIB", "qtechDot1xUserIfIndex"))
)
if mibBuilder.loadTexts:
    qtechDot1xUserMgmtTrap.setStatus(
        "current"
    )

qtechDot1xWiredUserTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 1, 1, 22, 2, 2)
)
qtechDot1xWiredUserTrap.setObjects(
      *(("QTECH-AAA-MIB", "qtechDot1xUserMac"),
        ("QTECH-AAA-MIB", "qtechDot1xUserName"),
        ("QTECH-AAA-MIB", "qtechDot1xUserIfIndex"),
        ("QTECH-AAA-MIB", "qtechDot1xUserVlanId"),
        ("QTECH-AAA-MIB", "qtechDot1xUserIp"),
        ("QTECH-AAA-MIB", "qtechDot1xUserIpv6"),
        ("QTECH-AAA-MIB", "qtechDot1xUserOperType"),
        ("QTECH-AAA-MIB", "qtechDot1xUserTerminateCause"))
)
if mibBuilder.loadTexts:
    qtechDot1xWiredUserTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

qtechAAAMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 19, 2, 1, 1)
)
qtechAAAMIBCompliance.setObjects(
      *(("QTECH-AAA-MIB", "qtechDot1xAuthMIBGroup"),
        ("QTECH-AAA-MIB", "qtechAAAServerMIBGroup"),
        ("QTECH-AAA-MIB", "qtechAuthAddrMIBGroup"),
        ("QTECH-AAA-MIB", "qtechAuthModeMIBGroup"),
        ("QTECH-AAA-MIB", "qtechAAAConfigMIBGroup"),
        ("QTECH-AAA-MIB", "qtechAAAUserApplyMIBGroup"),
        ("QTECH-AAA-MIB", "qtechRdASGroup"),
        ("QTECH-AAA-MIB", "qtechClientProbeGroup"))
)
if mibBuilder.loadTexts:
    qtechAAAMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-AAA-MIB",
    **{"qtechAAAMIB": qtechAAAMIB,
       "qtechRadiusServerTrap": qtechRadiusServerTrap,
       "qtechRadiusAuthServerDownTrap": qtechRadiusAuthServerDownTrap,
       "qtechRadiusAccServerDownTrap": qtechRadiusAccServerDownTrap,
       "qtechRadiusAuthServerRecoverTrap": qtechRadiusAuthServerRecoverTrap,
       "qtechRadiusAccServerRecoverTrap": qtechRadiusAccServerRecoverTrap,
       "qtechAAAMIBObjects": qtechAAAMIBObjects,
       "qtechDot1xAuthObjects": qtechDot1xAuthObjects,
       "qtechDot1xAuthStatus": qtechDot1xAuthStatus,
       "qtechDot1xAuthObjectsQuietPeriod": qtechDot1xAuthObjectsQuietPeriod,
       "qtechDot1xAuthObjectsTxPeriod": qtechDot1xAuthObjectsTxPeriod,
       "qtechDot1xAuthObjectsSuppTimeout": qtechDot1xAuthObjectsSuppTimeout,
       "qtechDot1xAuthObjectsServerTimeout": qtechDot1xAuthObjectsServerTimeout,
       "qtechDot1xAuthObjectsMaxReq": qtechDot1xAuthObjectsMaxReq,
       "qtechDot1xAuthObjectsReAuthPeriod": qtechDot1xAuthObjectsReAuthPeriod,
       "qtechDot1xAuthObjectsMaxReauth": qtechDot1xAuthObjectsMaxReauth,
       "qtechDot1xAuthObjectsReAuthEnable": qtechDot1xAuthObjectsReAuthEnable,
       "qtechDot1xAuthObjectsConfigTable": qtechDot1xAuthObjectsConfigTable,
       "qtechDot1xAuthObjectsConfigEntry": qtechDot1xAuthObjectsConfigEntry,
       "qtechDot1xAuthObjectsConfigFdbId": qtechDot1xAuthObjectsConfigFdbId,
       "qtechDot1xAuthObjectsConfigAddr": qtechDot1xAuthObjectsConfigAddr,
       "qtechDot1xAuthObjectsPaeState": qtechDot1xAuthObjectsPaeState,
       "qtechDot1xAuthObjectsBackendAuthState": qtechDot1xAuthObjectsBackendAuthState,
       "qtechDot1xAuthObjectsAuthControlledPortStatus": qtechDot1xAuthObjectsAuthControlledPortStatus,
       "qtechDot1xAuthObjectsKeyTxEnabled": qtechDot1xAuthObjectsKeyTxEnabled,
       "qtechDot1xAuthObjectsIfIndex": qtechDot1xAuthObjectsIfIndex,
       "qtechDot1xAuthObjectsStatsTable": qtechDot1xAuthObjectsStatsTable,
       "qtechDot1xAuthStatsEntry": qtechDot1xAuthStatsEntry,
       "qtechDot1xAuthObjectsStatsFdbId": qtechDot1xAuthObjectsStatsFdbId,
       "qtechDot1xAuthObjectsStatsAddr": qtechDot1xAuthObjectsStatsAddr,
       "qtechDot1xAuthObjectsEapolFramesRx": qtechDot1xAuthObjectsEapolFramesRx,
       "qtechDot1xAuthObjectsEapolFramesTx": qtechDot1xAuthObjectsEapolFramesTx,
       "qtechDot1xAuthObjectsEapolQtechFramesRx": qtechDot1xAuthObjectsEapolQtechFramesRx,
       "qtechDot1xAuthObjectsEapolLogoffFramesRx": qtechDot1xAuthObjectsEapolLogoffFramesRx,
       "qtechDot1xAuthObjectsEapolRespIdFramesRx": qtechDot1xAuthObjectsEapolRespIdFramesRx,
       "qtechDot1xAuthObjectsEapolRespFramesRx": qtechDot1xAuthObjectsEapolRespFramesRx,
       "qtechDot1xAuthObjectsEapolReqIdFramesTx": qtechDot1xAuthObjectsEapolReqIdFramesTx,
       "qtechDot1xAuthObjectsEapolReqFramesTx": qtechDot1xAuthObjectsEapolReqFramesTx,
       "qtechDot1xAuthObjectsInvalidEapolFramesRx": qtechDot1xAuthObjectsInvalidEapolFramesRx,
       "qtechDot1xAuthObjectsEapLengthErrorFramesRx": qtechDot1xAuthObjectsEapLengthErrorFramesRx,
       "qtechDot1xAuthObjectsLastEapolFrameVersion": qtechDot1xAuthObjectsLastEapolFrameVersion,
       "qtechDot1xAuthObjectsLastEapolFrameSource": qtechDot1xAuthObjectsLastEapolFrameSource,
       "qtechDot1xCurrentUserNumber": qtechDot1xCurrentUserNumber,
       "qtechDot1xCurrentAuthenticatedUserNumber": qtechDot1xCurrentAuthenticatedUserNumber,
       "qtechDot1xAccountStatus": qtechDot1xAccountStatus,
       "qtechAuthIfTable": qtechAuthIfTable,
       "qtechAuthIfEntry": qtechAuthIfEntry,
       "qtechAuthIf": qtechAuthIf,
       "qtechAuthIfStatus": qtechAuthIfStatus,
       "qtechAuthenticationMode": qtechAuthenticationMode,
       "qtechDot1xAccountUpdateStatus": qtechDot1xAccountUpdateStatus,
       "qtechDot1xAcctInterimInterval": qtechDot1xAcctInterimInterval,
       "qtechDot1xEapolTagEnabled": qtechDot1xEapolTagEnabled,
       "qtechDot1xIfUserMaxTable": qtechDot1xIfUserMaxTable,
       "qtechDot1xIfUserMaxEntry": qtechDot1xIfUserMaxEntry,
       "qtechDot1xIfUserMaxIndex": qtechDot1xIfUserMaxIndex,
       "qtechDot1xIfUserMaxNum": qtechDot1xIfUserMaxNum,
       "qtechDot1xPseudoSrcmac": qtechDot1xPseudoSrcmac,
       "qtechDot1xUserMIB": qtechDot1xUserMIB,
       "qtechDot1xUserTrapsObjects": qtechDot1xUserTrapsObjects,
       "qtechDot1xUserMac": qtechDot1xUserMac,
       "qtechDot1xUserName": qtechDot1xUserName,
       "qtechDot1xUserIp": qtechDot1xUserIp,
       "qtechDot1xUserIpv6": qtechDot1xUserIpv6,
       "qtechDot1xUserWlanId": qtechDot1xUserWlanId,
       "qtechDot1xUserVlanId": qtechDot1xUserVlanId,
       "qtechDot1xUserSsid": qtechDot1xUserSsid,
       "qtechDot1xUserApMac": qtechDot1xUserApMac,
       "qtechDot1xUserTerminalType": qtechDot1xUserTerminalType,
       "qtechDot1xUserOperType": qtechDot1xUserOperType,
       "qtechDot1xUserTerminateCause": qtechDot1xUserTerminateCause,
       "qtechDot1xUserReplyMessage": qtechDot1xUserReplyMessage,
       "qtechDot1xUserIfIndex": qtechDot1xUserIfIndex,
       "qtechDot1xUserTraps": qtechDot1xUserTraps,
       "qtechDot1xUserMgmtTrap": qtechDot1xUserMgmtTrap,
       "qtechDot1xWiredUserTrap": qtechDot1xWiredUserTrap,
       "qtechDot1xOnlineUserTable": qtechDot1xOnlineUserTable,
       "qtechDot1xOnlineUserEntry": qtechDot1xOnlineUserEntry,
       "qtechDot1xOnlineUserID": qtechDot1xOnlineUserID,
       "qtechDot1xOnlineUserName": qtechDot1xOnlineUserName,
       "qtechDot1xOnlineUserMacAddr": qtechDot1xOnlineUserMacAddr,
       "qtechDot1xOnlineUserIfIndex": qtechDot1xOnlineUserIfIndex,
       "qtechDot1xOnlineUserVlanId": qtechDot1xOnlineUserVlanId,
       "qtechDot1xOnlineUserIp": qtechDot1xOnlineUserIp,
       "qtechDot1xOnlineUserIpv6": qtechDot1xOnlineUserIpv6,
       "qtechDot1xAbnormalOfflineUserCount": qtechDot1xAbnormalOfflineUserCount,
       "qtechDot1xTotalAuthUserCount": qtechDot1xTotalAuthUserCount,
       "qtechDot1xAuthSuccUserCount": qtechDot1xAuthSuccUserCount,
       "qtechDot1xAuthFailUserCount": qtechDot1xAuthFailUserCount,
       "qtechAAAServerObjects": qtechAAAServerObjects,
       "qtechAAAServerAuthPort": qtechAAAServerAuthPort,
       "qtechAAAServerAcctPort": qtechAAAServerAcctPort,
       "qtechAAAServerRadiusKeyStr": qtechAAAServerRadiusKeyStr,
       "qtechAAAServerTacplusKeyStr": qtechAAAServerTacplusKeyStr,
       "qtechAAAServerConfigTable": qtechAAAServerConfigTable,
       "qtechAAAServerConfigEntry": qtechAAAServerConfigEntry,
       "qtechAAAServerConfigProtocol": qtechAAAServerConfigProtocol,
       "qtechAAAServerConfigIndex": qtechAAAServerConfigIndex,
       "qtechAAAServerConfigAddressType": qtechAAAServerConfigAddressType,
       "qtechAAAServerConfigAddress": qtechAAAServerConfigAddress,
       "qtechAAAServerConfigAuthPort": qtechAAAServerConfigAuthPort,
       "qtechAAAServerConfigAcctPort": qtechAAAServerConfigAcctPort,
       "qtechAAAServerConfigKeyStr": qtechAAAServerConfigKeyStr,
       "qtechAAAServerConfigRowStatus": qtechAAAServerConfigRowStatus,
       "qtechAAARadiusGroupTable": qtechAAARadiusGroupTable,
       "qtechAAARadiusGroupEntry": qtechAAARadiusGroupEntry,
       "qtechAAARadiusGroupName": qtechAAARadiusGroupName,
       "qtechAAARadiusGroupVrf": qtechAAARadiusGroupVrf,
       "qtechAAARadiusGroupRowStatus": qtechAAARadiusGroupRowStatus,
       "qtechAAARadiusGroupServerTable": qtechAAARadiusGroupServerTable,
       "qtechAAARadiusGroupServerEntry": qtechAAARadiusGroupServerEntry,
       "qtechAAARadiusGroupServerIndex": qtechAAARadiusGroupServerIndex,
       "qtechAAARadiusGroupServerAddressType": qtechAAARadiusGroupServerAddressType,
       "qtechAAARadiusGroupServerAddress": qtechAAARadiusGroupServerAddress,
       "qtechAAARadiusGroupServerAuthPort": qtechAAARadiusGroupServerAuthPort,
       "qtechAAARadiusGroupServerAcctPort": qtechAAARadiusGroupServerAcctPort,
       "qtechAAARadiusGroupServerRowStatus": qtechAAARadiusGroupServerRowStatus,
       "qtechAAAServerTotalOnlineCount": qtechAAAServerTotalOnlineCount,
       "qtechAAAServerAbnormalOffline": qtechAAAServerAbnormalOffline,
       "qtechAAAServerRadiusAuthReqCount": qtechAAAServerRadiusAuthReqCount,
       "qtechAAAServerRadiusAuthRespCount": qtechAAAServerRadiusAuthRespCount,
       "qtechAAAServerRadiusAuthSuccessCount": qtechAAAServerRadiusAuthSuccessCount,
       "qtechAAAServerCurrOnlineUserCount": qtechAAAServerCurrOnlineUserCount,
       "qtechAAAMasterAuthenServerConfigTable": qtechAAAMasterAuthenServerConfigTable,
       "qtechAAAMasterAuthenServerConfigEntry": qtechAAAMasterAuthenServerConfigEntry,
       "qtechAAAMasterAuthenServerConfigGrpName": qtechAAAMasterAuthenServerConfigGrpName,
       "qtechAAAMasterAuthenServerConfigSrvIndex": qtechAAAMasterAuthenServerConfigSrvIndex,
       "qtechAAAMasterAuthenServerConfigAddress": qtechAAAMasterAuthenServerConfigAddress,
       "qtechAAAMasterAuthenServerConfigAuthPort": qtechAAAMasterAuthenServerConfigAuthPort,
       "qtechAAAMasterAuthenServerConfigAcctPort": qtechAAAMasterAuthenServerConfigAcctPort,
       "qtechAAAMasterAuthenServerConfigKeyStr": qtechAAAMasterAuthenServerConfigKeyStr,
       "qtechAAAMasterAuthenServerConfigRowStatus": qtechAAAMasterAuthenServerConfigRowStatus,
       "qtechAAABackAuthenServerConfigTable": qtechAAABackAuthenServerConfigTable,
       "qtechAAABackAuthenServerConfigEntry": qtechAAABackAuthenServerConfigEntry,
       "qtechAAABackAuthenServerConfigGrpName": qtechAAABackAuthenServerConfigGrpName,
       "qtechAAABackAuthenServerConfigSrvIndex": qtechAAABackAuthenServerConfigSrvIndex,
       "qtechAAABackAuthenServerConfigAddress": qtechAAABackAuthenServerConfigAddress,
       "qtechAAABackAuthenServerConfigAuthPort": qtechAAABackAuthenServerConfigAuthPort,
       "qtechAAABackAuthenServerConfigAcctPort": qtechAAABackAuthenServerConfigAcctPort,
       "qtechAAABackAuthenServerConfigKeyStr": qtechAAABackAuthenServerConfigKeyStr,
       "qtechAAABackAuthenServerConfigRowStatus": qtechAAABackAuthenServerConfigRowStatus,
       "qtechAAAMasterAcctServerConfigTable": qtechAAAMasterAcctServerConfigTable,
       "qtechAAAMasterAcctServerConfigEntry": qtechAAAMasterAcctServerConfigEntry,
       "qtechAAAMasterAcctServerConfigGrpName": qtechAAAMasterAcctServerConfigGrpName,
       "qtechAAAMasterAcctServerConfigSrvIndex": qtechAAAMasterAcctServerConfigSrvIndex,
       "qtechAAAMasterAcctServerConfigAddress": qtechAAAMasterAcctServerConfigAddress,
       "qtechAAAMasterAcctServerConfigAuthPort": qtechAAAMasterAcctServerConfigAuthPort,
       "qtechAAAMasterAcctServerConfigAcctPort": qtechAAAMasterAcctServerConfigAcctPort,
       "qtechAAAMasterAcctServerConfigKeyStr": qtechAAAMasterAcctServerConfigKeyStr,
       "qtechAAAMasterAcctServerConfigRowStatus": qtechAAAMasterAcctServerConfigRowStatus,
       "qtechAAABackAcctServerConfigTable": qtechAAABackAcctServerConfigTable,
       "qtechAAABackAcctServerConfigEntry": qtechAAABackAcctServerConfigEntry,
       "qtechAAABackAcctServerConfigGrpName": qtechAAABackAcctServerConfigGrpName,
       "qtechAAABackAcctServerConfigSrvIndex": qtechAAABackAcctServerConfigSrvIndex,
       "qtechAAABackAcctServerConfigAddress": qtechAAABackAcctServerConfigAddress,
       "qtechAAABackAcctServerConfigAuthPort": qtechAAABackAcctServerConfigAuthPort,
       "qtechAAABackAcctServerConfigAcctPort": qtechAAABackAcctServerConfigAcctPort,
       "qtechAAABackAcctServerConfigKeyStr": qtechAAABackAcctServerConfigKeyStr,
       "qtechAAABackAcctServerConfigRowStatus": qtechAAABackAcctServerConfigRowStatus,
       "qtechAAAServerTotalAuthUserCount": qtechAAAServerTotalAuthUserCount,
       "qtechAAAServerAuthSuccUserCount": qtechAAAServerAuthSuccUserCount,
       "qtechAAAServerDot1xOnlineUserCount": qtechAAAServerDot1xOnlineUserCount,
       "qtechAAAServerMacOnlineUserCount": qtechAAAServerMacOnlineUserCount,
       "qtechAAAServerWebOnlineUserCount": qtechAAAServerWebOnlineUserCount,
       "qtechAAAServerTatalOnlineUserCount": qtechAAAServerTatalOnlineUserCount,
       "qtechAAAServerIfOnlineUserTable": qtechAAAServerIfOnlineUserTable,
       "qtechAAAServerIfOnlineUserEntry": qtechAAAServerIfOnlineUserEntry,
       "qtechAAAServerIfOnlineUserIfIndex": qtechAAAServerIfOnlineUserIfIndex,
       "qtechAAAServerIfOnlineUserDot1xCount": qtechAAAServerIfOnlineUserDot1xCount,
       "qtechAAAServerIfOnlineUserWebCount": qtechAAAServerIfOnlineUserWebCount,
       "qtechAAAServerIfOnlineUserMacCount": qtechAAAServerIfOnlineUserMacCount,
       "qtechAAAServerIfOnlineUserTotalCount": qtechAAAServerIfOnlineUserTotalCount,
       "qtechAuthUserObjects": qtechAuthUserObjects,
       "qtechAuthAddrTable": qtechAuthAddrTable,
       "qtechAuthAddrEntry": qtechAuthAddrEntry,
       "qtechAuthPort": qtechAuthPort,
       "qtechAuthMacAddress": qtechAuthMacAddress,
       "qtechAuthAddrStatus": qtechAuthAddrStatus,
       "qtechAuthUserTable": qtechAuthUserTable,
       "qtechAuthUserEntry": qtechAuthUserEntry,
       "qtechAuthUserFdbId": qtechAuthUserFdbId,
       "qtechAuthUserMacAddress": qtechAuthUserMacAddress,
       "qtechAuthUserName": qtechAuthUserName,
       "qtechAuthUserSessionId": qtechAuthUserSessionId,
       "qtechAuthUserIpAddr": qtechAuthUserIpAddr,
       "qtechAuthUserPort": qtechAuthUserPort,
       "qtechAuthUserStatus": qtechAuthUserStatus,
       "qtechAuthUserForVPNDel": qtechAuthUserForVPNDel,
       "qtechAuthModeObjects": qtechAuthModeObjects,
       "qtechIpAuthorizationMode": qtechIpAuthorizationMode,
       "qtechClientProbeObjects": qtechClientProbeObjects,
       "qtechClientProbeEnabledStatus": qtechClientProbeEnabledStatus,
       "qtechClientProbeHelloInterval": qtechClientProbeHelloInterval,
       "qtechClientProbeAliveInteval": qtechClientProbeAliveInteval,
       "qtechAAAConfigObjects": qtechAAAConfigObjects,
       "qtechAuthenConfigObjects": qtechAuthenConfigObjects,
       "qtechAuthenMethodListTable": qtechAuthenMethodListTable,
       "qtechAuthenMethodListEntry": qtechAuthenMethodListEntry,
       "qtechAuthenMethodListType": qtechAuthenMethodListType,
       "qtechAuthenMethodListName": qtechAuthenMethodListName,
       "qtechAuthenMethodListString": qtechAuthenMethodListString,
       "qtechAuthenMethodListRowStatus": qtechAuthenMethodListRowStatus,
       "qtechAuthorConfigObjects": qtechAuthorConfigObjects,
       "qtechAuthorMethodListTable": qtechAuthorMethodListTable,
       "qtechAuthorMethodListEntry": qtechAuthorMethodListEntry,
       "qtechAuthorMethodListType": qtechAuthorMethodListType,
       "qtechAuthorMethodListName": qtechAuthorMethodListName,
       "qtechAuthorMethodListCmdLevel": qtechAuthorMethodListCmdLevel,
       "qtechAuthorMethodListString": qtechAuthorMethodListString,
       "qtechAuthorMethodListRowStatus": qtechAuthorMethodListRowStatus,
       "qtechAcctConfigObjects": qtechAcctConfigObjects,
       "qtechAcctMethodListTable": qtechAcctMethodListTable,
       "qtechAcctMethodListEntry": qtechAcctMethodListEntry,
       "qtechAcctMethodListType": qtechAcctMethodListType,
       "qtechAcctMethodListName": qtechAcctMethodListName,
       "qtechAcctMethodListMode": qtechAcctMethodListMode,
       "qtechAcctMethodListCmdLevel": qtechAcctMethodListCmdLevel,
       "qtechAcctMethodListString": qtechAcctMethodListString,
       "qtechAcctMethodListRowStatus": qtechAcctMethodListRowStatus,
       "qtechAAAUserApplyObjects": qtechAAAUserApplyObjects,
       "qtechAAADo1xApplyObjects": qtechAAADo1xApplyObjects,
       "qtechDot1xAuthenMethodList": qtechDot1xAuthenMethodList,
       "qtechDot1xAuthorMethodList": qtechDot1xAuthorMethodList,
       "qtechDot1xAcctMethodList": qtechDot1xAcctMethodList,
       "qtechRdASObjects": qtechRdASObjects,
       "qtechRdASipInetAddreType": qtechRdASipInetAddreType,
       "qtechRdASipInsetAddres": qtechRdASipInsetAddres,
       "qtechAAAMIBConformance": qtechAAAMIBConformance,
       "qtechAAAMIBCompliances": qtechAAAMIBCompliances,
       "qtechAAAMIBCompliance": qtechAAAMIBCompliance,
       "qtechAAAMIBGroups": qtechAAAMIBGroups,
       "qtechDot1xAuthMIBGroup": qtechDot1xAuthMIBGroup,
       "qtechAAAServerMIBGroup": qtechAAAServerMIBGroup,
       "qtechAuthAddrMIBGroup": qtechAuthAddrMIBGroup,
       "qtechAuthModeMIBGroup": qtechAuthModeMIBGroup,
       "qtechClientProbeGroup": qtechClientProbeGroup,
       "qtechAAAConfigMIBGroup": qtechAAAConfigMIBGroup,
       "qtechAAAUserApplyMIBGroup": qtechAAAUserApplyMIBGroup,
       "qtechRdASGroup": qtechRdASGroup}
)
