# SNMP MIB module (MY-AAA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ruijie/MY-AAA-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:34:36 2025
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

(myMgmt,) = mibBuilder.importSymbols(
    "MY-SMI",
    "myMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "MY-TC",
    "ConfigStatus",
    "IfIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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

myAAAMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19)
)
if mibBuilder.loadTexts:
    myAAAMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MyAAAMIBObjects_ObjectIdentity = ObjectIdentity
myAAAMIBObjects = _MyAAAMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1)
)
_MyDot1xAuthObjects_ObjectIdentity = ObjectIdentity
myDot1xAuthObjects = _MyDot1xAuthObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1)
)


class _MyDot1xAuthStatus_Type(EnabledStatus):
    """Custom type myDot1xAuthStatus based on EnabledStatus"""
    defaultValue = 2


_MyDot1xAuthStatus_Type.__name__ = "EnabledStatus"
_MyDot1xAuthStatus_Object = MibScalar
myDot1xAuthStatus = _MyDot1xAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 1),
    _MyDot1xAuthStatus_Type()
)
myDot1xAuthStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myDot1xAuthStatus.setStatus("current")


class _MyDot1xAuthObjectsQuietPeriod_Type(Unsigned32):
    """Custom type myDot1xAuthObjectsQuietPeriod based on Unsigned32"""
    defaultValue = 60


_MyDot1xAuthObjectsQuietPeriod_Type.__name__ = "Unsigned32"
_MyDot1xAuthObjectsQuietPeriod_Object = MibScalar
myDot1xAuthObjectsQuietPeriod = _MyDot1xAuthObjectsQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 2),
    _MyDot1xAuthObjectsQuietPeriod_Type()
)
myDot1xAuthObjectsQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myDot1xAuthObjectsQuietPeriod.setStatus("current")


class _MyDot1xAuthObjectsTxPeriod_Type(Unsigned32):
    """Custom type myDot1xAuthObjectsTxPeriod based on Unsigned32"""
    defaultValue = 30


_MyDot1xAuthObjectsTxPeriod_Type.__name__ = "Unsigned32"
_MyDot1xAuthObjectsTxPeriod_Object = MibScalar
myDot1xAuthObjectsTxPeriod = _MyDot1xAuthObjectsTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 3),
    _MyDot1xAuthObjectsTxPeriod_Type()
)
myDot1xAuthObjectsTxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myDot1xAuthObjectsTxPeriod.setStatus("current")


class _MyDot1xAuthObjectsSuppTimeout_Type(Unsigned32):
    """Custom type myDot1xAuthObjectsSuppTimeout based on Unsigned32"""
    defaultValue = 30


_MyDot1xAuthObjectsSuppTimeout_Type.__name__ = "Unsigned32"
_MyDot1xAuthObjectsSuppTimeout_Object = MibScalar
myDot1xAuthObjectsSuppTimeout = _MyDot1xAuthObjectsSuppTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 4),
    _MyDot1xAuthObjectsSuppTimeout_Type()
)
myDot1xAuthObjectsSuppTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myDot1xAuthObjectsSuppTimeout.setStatus("current")


class _MyDot1xAuthObjectsServerTimeout_Type(Unsigned32):
    """Custom type myDot1xAuthObjectsServerTimeout based on Unsigned32"""
    defaultValue = 30


_MyDot1xAuthObjectsServerTimeout_Type.__name__ = "Unsigned32"
_MyDot1xAuthObjectsServerTimeout_Object = MibScalar
myDot1xAuthObjectsServerTimeout = _MyDot1xAuthObjectsServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 5),
    _MyDot1xAuthObjectsServerTimeout_Type()
)
myDot1xAuthObjectsServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myDot1xAuthObjectsServerTimeout.setStatus("current")


class _MyDot1xAuthObjectsMaxReq_Type(Unsigned32):
    """Custom type myDot1xAuthObjectsMaxReq based on Unsigned32"""
    defaultValue = 2


_MyDot1xAuthObjectsMaxReq_Type.__name__ = "Unsigned32"
_MyDot1xAuthObjectsMaxReq_Object = MibScalar
myDot1xAuthObjectsMaxReq = _MyDot1xAuthObjectsMaxReq_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 6),
    _MyDot1xAuthObjectsMaxReq_Type()
)
myDot1xAuthObjectsMaxReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myDot1xAuthObjectsMaxReq.setStatus("current")


class _MyDot1xAuthObjectsReAuthPeriod_Type(Unsigned32):
    """Custom type myDot1xAuthObjectsReAuthPeriod based on Unsigned32"""
    defaultValue = 3600


_MyDot1xAuthObjectsReAuthPeriod_Type.__name__ = "Unsigned32"
_MyDot1xAuthObjectsReAuthPeriod_Object = MibScalar
myDot1xAuthObjectsReAuthPeriod = _MyDot1xAuthObjectsReAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 7),
    _MyDot1xAuthObjectsReAuthPeriod_Type()
)
myDot1xAuthObjectsReAuthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myDot1xAuthObjectsReAuthPeriod.setStatus("current")


class _MyDot1xAuthObjectsMaxReauth_Type(Unsigned32):
    """Custom type myDot1xAuthObjectsMaxReauth based on Unsigned32"""
    defaultValue = 2


_MyDot1xAuthObjectsMaxReauth_Type.__name__ = "Unsigned32"
_MyDot1xAuthObjectsMaxReauth_Object = MibScalar
myDot1xAuthObjectsMaxReauth = _MyDot1xAuthObjectsMaxReauth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 8),
    _MyDot1xAuthObjectsMaxReauth_Type()
)
myDot1xAuthObjectsMaxReauth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myDot1xAuthObjectsMaxReauth.setStatus("current")


class _MyDot1xAuthObjectsReAuthEnable_Type(EnabledStatus):
    """Custom type myDot1xAuthObjectsReAuthEnable based on EnabledStatus"""
    defaultValue = 2


_MyDot1xAuthObjectsReAuthEnable_Type.__name__ = "EnabledStatus"
_MyDot1xAuthObjectsReAuthEnable_Object = MibScalar
myDot1xAuthObjectsReAuthEnable = _MyDot1xAuthObjectsReAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 9),
    _MyDot1xAuthObjectsReAuthEnable_Type()
)
myDot1xAuthObjectsReAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myDot1xAuthObjectsReAuthEnable.setStatus("current")
_MyDot1xAuthObjectsConfigTable_Object = MibTable
myDot1xAuthObjectsConfigTable = _MyDot1xAuthObjectsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 10)
)
if mibBuilder.loadTexts:
    myDot1xAuthObjectsConfigTable.setStatus("current")
_MyDot1xAuthObjectsConfigEntry_Object = MibTableRow
myDot1xAuthObjectsConfigEntry = _MyDot1xAuthObjectsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 10, 1)
)
myDot1xAuthObjectsConfigEntry.setIndexNames(
    (0, "MY-AAA-MIB", "myDot1xAuthObjectsConfigFdbId"),
    (0, "MY-AAA-MIB", "myDot1xAuthObjectsConfigAddr"),
)
if mibBuilder.loadTexts:
    myDot1xAuthObjectsConfigEntry.setStatus("current")
_MyDot1xAuthObjectsConfigFdbId_Type = Unsigned32
_MyDot1xAuthObjectsConfigFdbId_Object = MibTableColumn
myDot1xAuthObjectsConfigFdbId = _MyDot1xAuthObjectsConfigFdbId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 10, 1, 1),
    _MyDot1xAuthObjectsConfigFdbId_Type()
)
myDot1xAuthObjectsConfigFdbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myDot1xAuthObjectsConfigFdbId.setStatus("current")
_MyDot1xAuthObjectsConfigAddr_Type = MacAddress
_MyDot1xAuthObjectsConfigAddr_Object = MibTableColumn
myDot1xAuthObjectsConfigAddr = _MyDot1xAuthObjectsConfigAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 10, 1, 2),
    _MyDot1xAuthObjectsConfigAddr_Type()
)
myDot1xAuthObjectsConfigAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myDot1xAuthObjectsConfigAddr.setStatus("current")


class _MyDot1xAuthObjectsPaeState_Type(Integer32):
    """Custom type myDot1xAuthObjectsPaeState based on Integer32"""
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


_MyDot1xAuthObjectsPaeState_Type.__name__ = "Integer32"
_MyDot1xAuthObjectsPaeState_Object = MibTableColumn
myDot1xAuthObjectsPaeState = _MyDot1xAuthObjectsPaeState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 10, 1, 3),
    _MyDot1xAuthObjectsPaeState_Type()
)
myDot1xAuthObjectsPaeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myDot1xAuthObjectsPaeState.setStatus("current")


class _MyDot1xAuthObjectsBackendAuthState_Type(Integer32):
    """Custom type myDot1xAuthObjectsBackendAuthState based on Integer32"""
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


_MyDot1xAuthObjectsBackendAuthState_Type.__name__ = "Integer32"
_MyDot1xAuthObjectsBackendAuthState_Object = MibTableColumn
myDot1xAuthObjectsBackendAuthState = _MyDot1xAuthObjectsBackendAuthState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 10, 1, 4),
    _MyDot1xAuthObjectsBackendAuthState_Type()
)
myDot1xAuthObjectsBackendAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myDot1xAuthObjectsBackendAuthState.setStatus("current")


class _MyDot1xAuthObjectsAuthControlledPortStatus_Type(Integer32):
    """Custom type myDot1xAuthObjectsAuthControlledPortStatus based on Integer32"""
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


_MyDot1xAuthObjectsAuthControlledPortStatus_Type.__name__ = "Integer32"
_MyDot1xAuthObjectsAuthControlledPortStatus_Object = MibTableColumn
myDot1xAuthObjectsAuthControlledPortStatus = _MyDot1xAuthObjectsAuthControlledPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 10, 1, 5),
    _MyDot1xAuthObjectsAuthControlledPortStatus_Type()
)
myDot1xAuthObjectsAuthControlledPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myDot1xAuthObjectsAuthControlledPortStatus.setStatus("current")
_MyDot1xAuthObjectsKeyTxEnabled_Type = TruthValue
_MyDot1xAuthObjectsKeyTxEnabled_Object = MibTableColumn
myDot1xAuthObjectsKeyTxEnabled = _MyDot1xAuthObjectsKeyTxEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 10, 1, 6),
    _MyDot1xAuthObjectsKeyTxEnabled_Type()
)
myDot1xAuthObjectsKeyTxEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myDot1xAuthObjectsKeyTxEnabled.setStatus("current")
_MyDot1xAuthObjectsIfIndex_Type = IfIndex
_MyDot1xAuthObjectsIfIndex_Object = MibTableColumn
myDot1xAuthObjectsIfIndex = _MyDot1xAuthObjectsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 10, 1, 7),
    _MyDot1xAuthObjectsIfIndex_Type()
)
myDot1xAuthObjectsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myDot1xAuthObjectsIfIndex.setStatus("current")
_MyDot1xAuthObjectsStatsTable_Object = MibTable
myDot1xAuthObjectsStatsTable = _MyDot1xAuthObjectsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 11)
)
if mibBuilder.loadTexts:
    myDot1xAuthObjectsStatsTable.setStatus("current")
_MyDot1xAuthStatsEntry_Object = MibTableRow
myDot1xAuthStatsEntry = _MyDot1xAuthStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 11, 1)
)
myDot1xAuthStatsEntry.setIndexNames(
    (0, "MY-AAA-MIB", "myDot1xAuthObjectsStatsFdbId"),
    (0, "MY-AAA-MIB", "myDot1xAuthObjectsStatsAddr"),
)
if mibBuilder.loadTexts:
    myDot1xAuthStatsEntry.setStatus("current")
_MyDot1xAuthObjectsStatsFdbId_Type = Unsigned32
_MyDot1xAuthObjectsStatsFdbId_Object = MibTableColumn
myDot1xAuthObjectsStatsFdbId = _MyDot1xAuthObjectsStatsFdbId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 11, 1, 1),
    _MyDot1xAuthObjectsStatsFdbId_Type()
)
myDot1xAuthObjectsStatsFdbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myDot1xAuthObjectsStatsFdbId.setStatus("current")
_MyDot1xAuthObjectsStatsAddr_Type = MacAddress
_MyDot1xAuthObjectsStatsAddr_Object = MibTableColumn
myDot1xAuthObjectsStatsAddr = _MyDot1xAuthObjectsStatsAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 11, 1, 2),
    _MyDot1xAuthObjectsStatsAddr_Type()
)
myDot1xAuthObjectsStatsAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myDot1xAuthObjectsStatsAddr.setStatus("current")
_MyDot1xAuthObjectsEapolFramesRx_Type = Counter32
_MyDot1xAuthObjectsEapolFramesRx_Object = MibTableColumn
myDot1xAuthObjectsEapolFramesRx = _MyDot1xAuthObjectsEapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 11, 1, 3),
    _MyDot1xAuthObjectsEapolFramesRx_Type()
)
myDot1xAuthObjectsEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myDot1xAuthObjectsEapolFramesRx.setStatus("current")
_MyDot1xAuthObjectsEapolFramesTx_Type = Counter32
_MyDot1xAuthObjectsEapolFramesTx_Object = MibTableColumn
myDot1xAuthObjectsEapolFramesTx = _MyDot1xAuthObjectsEapolFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 11, 1, 4),
    _MyDot1xAuthObjectsEapolFramesTx_Type()
)
myDot1xAuthObjectsEapolFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myDot1xAuthObjectsEapolFramesTx.setStatus("current")
_MyDot1xAuthObjectsEapolMyFramesRx_Type = Counter32
_MyDot1xAuthObjectsEapolMyFramesRx_Object = MibTableColumn
myDot1xAuthObjectsEapolMyFramesRx = _MyDot1xAuthObjectsEapolMyFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 11, 1, 5),
    _MyDot1xAuthObjectsEapolMyFramesRx_Type()
)
myDot1xAuthObjectsEapolMyFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myDot1xAuthObjectsEapolMyFramesRx.setStatus("current")
_MyDot1xAuthObjectsEapolLogoffFramesRx_Type = Counter32
_MyDot1xAuthObjectsEapolLogoffFramesRx_Object = MibTableColumn
myDot1xAuthObjectsEapolLogoffFramesRx = _MyDot1xAuthObjectsEapolLogoffFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 11, 1, 6),
    _MyDot1xAuthObjectsEapolLogoffFramesRx_Type()
)
myDot1xAuthObjectsEapolLogoffFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myDot1xAuthObjectsEapolLogoffFramesRx.setStatus("current")
_MyDot1xAuthObjectsEapolRespIdFramesRx_Type = Counter32
_MyDot1xAuthObjectsEapolRespIdFramesRx_Object = MibTableColumn
myDot1xAuthObjectsEapolRespIdFramesRx = _MyDot1xAuthObjectsEapolRespIdFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 11, 1, 7),
    _MyDot1xAuthObjectsEapolRespIdFramesRx_Type()
)
myDot1xAuthObjectsEapolRespIdFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myDot1xAuthObjectsEapolRespIdFramesRx.setStatus("current")
_MyDot1xAuthObjectsEapolRespFramesRx_Type = Counter32
_MyDot1xAuthObjectsEapolRespFramesRx_Object = MibTableColumn
myDot1xAuthObjectsEapolRespFramesRx = _MyDot1xAuthObjectsEapolRespFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 11, 1, 8),
    _MyDot1xAuthObjectsEapolRespFramesRx_Type()
)
myDot1xAuthObjectsEapolRespFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myDot1xAuthObjectsEapolRespFramesRx.setStatus("current")
_MyDot1xAuthObjectsEapolReqIdFramesTx_Type = Counter32
_MyDot1xAuthObjectsEapolReqIdFramesTx_Object = MibTableColumn
myDot1xAuthObjectsEapolReqIdFramesTx = _MyDot1xAuthObjectsEapolReqIdFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 11, 1, 9),
    _MyDot1xAuthObjectsEapolReqIdFramesTx_Type()
)
myDot1xAuthObjectsEapolReqIdFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myDot1xAuthObjectsEapolReqIdFramesTx.setStatus("current")
_MyDot1xAuthObjectsEapolReqFramesTx_Type = Counter32
_MyDot1xAuthObjectsEapolReqFramesTx_Object = MibTableColumn
myDot1xAuthObjectsEapolReqFramesTx = _MyDot1xAuthObjectsEapolReqFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 11, 1, 10),
    _MyDot1xAuthObjectsEapolReqFramesTx_Type()
)
myDot1xAuthObjectsEapolReqFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myDot1xAuthObjectsEapolReqFramesTx.setStatus("current")
_MyDot1xAuthObjectsInvalidEapolFramesRx_Type = Counter32
_MyDot1xAuthObjectsInvalidEapolFramesRx_Object = MibTableColumn
myDot1xAuthObjectsInvalidEapolFramesRx = _MyDot1xAuthObjectsInvalidEapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 11, 1, 11),
    _MyDot1xAuthObjectsInvalidEapolFramesRx_Type()
)
myDot1xAuthObjectsInvalidEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myDot1xAuthObjectsInvalidEapolFramesRx.setStatus("current")
_MyDot1xAuthObjectsEapLengthErrorFramesRx_Type = Counter32
_MyDot1xAuthObjectsEapLengthErrorFramesRx_Object = MibTableColumn
myDot1xAuthObjectsEapLengthErrorFramesRx = _MyDot1xAuthObjectsEapLengthErrorFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 11, 1, 12),
    _MyDot1xAuthObjectsEapLengthErrorFramesRx_Type()
)
myDot1xAuthObjectsEapLengthErrorFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myDot1xAuthObjectsEapLengthErrorFramesRx.setStatus("current")
_MyDot1xAuthObjectsLastEapolFrameVersion_Type = Unsigned32
_MyDot1xAuthObjectsLastEapolFrameVersion_Object = MibTableColumn
myDot1xAuthObjectsLastEapolFrameVersion = _MyDot1xAuthObjectsLastEapolFrameVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 11, 1, 13),
    _MyDot1xAuthObjectsLastEapolFrameVersion_Type()
)
myDot1xAuthObjectsLastEapolFrameVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myDot1xAuthObjectsLastEapolFrameVersion.setStatus("current")
_MyDot1xAuthObjectsLastEapolFrameSource_Type = MacAddress
_MyDot1xAuthObjectsLastEapolFrameSource_Object = MibTableColumn
myDot1xAuthObjectsLastEapolFrameSource = _MyDot1xAuthObjectsLastEapolFrameSource_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 11, 1, 14),
    _MyDot1xAuthObjectsLastEapolFrameSource_Type()
)
myDot1xAuthObjectsLastEapolFrameSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myDot1xAuthObjectsLastEapolFrameSource.setStatus("current")
_MyDot1xCurrentUserNumber_Type = Counter32
_MyDot1xCurrentUserNumber_Object = MibScalar
myDot1xCurrentUserNumber = _MyDot1xCurrentUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 12),
    _MyDot1xCurrentUserNumber_Type()
)
myDot1xCurrentUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myDot1xCurrentUserNumber.setStatus("current")
_MyDot1xCurrentAuthenticatedUserNumber_Type = Counter32
_MyDot1xCurrentAuthenticatedUserNumber_Object = MibScalar
myDot1xCurrentAuthenticatedUserNumber = _MyDot1xCurrentAuthenticatedUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 13),
    _MyDot1xCurrentAuthenticatedUserNumber_Type()
)
myDot1xCurrentAuthenticatedUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myDot1xCurrentAuthenticatedUserNumber.setStatus("current")


class _MyDot1xAccountStatus_Type(EnabledStatus):
    """Custom type myDot1xAccountStatus based on EnabledStatus"""
    defaultValue = 2


_MyDot1xAccountStatus_Type.__name__ = "EnabledStatus"
_MyDot1xAccountStatus_Object = MibScalar
myDot1xAccountStatus = _MyDot1xAccountStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 14),
    _MyDot1xAccountStatus_Type()
)
myDot1xAccountStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myDot1xAccountStatus.setStatus("current")
_MyAuthIfTable_Object = MibTable
myAuthIfTable = _MyAuthIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 15)
)
if mibBuilder.loadTexts:
    myAuthIfTable.setStatus("current")
_MyAuthIfEntry_Object = MibTableRow
myAuthIfEntry = _MyAuthIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 15, 1)
)
myAuthIfEntry.setIndexNames(
    (0, "MY-AAA-MIB", "myAuthIf"),
)
if mibBuilder.loadTexts:
    myAuthIfEntry.setStatus("current")
_MyAuthIf_Type = IfIndex
_MyAuthIf_Object = MibTableColumn
myAuthIf = _MyAuthIf_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 15, 1, 1),
    _MyAuthIf_Type()
)
myAuthIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myAuthIf.setStatus("current")


class _MyAuthIfStatus_Type(EnabledStatus):
    """Custom type myAuthIfStatus based on EnabledStatus"""
    defaultValue = 2


_MyAuthIfStatus_Type.__name__ = "EnabledStatus"
_MyAuthIfStatus_Object = MibTableColumn
myAuthIfStatus = _MyAuthIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 15, 1, 2),
    _MyAuthIfStatus_Type()
)
myAuthIfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAuthIfStatus.setStatus("current")


class _MyAuthenticationMode_Type(Integer32):
    """Custom type myAuthenticationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eap-md5", 1),
          ("chap", 2))
    )


_MyAuthenticationMode_Type.__name__ = "Integer32"
_MyAuthenticationMode_Object = MibScalar
myAuthenticationMode = _MyAuthenticationMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 16),
    _MyAuthenticationMode_Type()
)
myAuthenticationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAuthenticationMode.setStatus("current")
_MyDot1xAccountUpdateStatus_Type = EnabledStatus
_MyDot1xAccountUpdateStatus_Object = MibScalar
myDot1xAccountUpdateStatus = _MyDot1xAccountUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 17),
    _MyDot1xAccountUpdateStatus_Type()
)
myDot1xAccountUpdateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myDot1xAccountUpdateStatus.setStatus("current")


class _MyDot1xAcctInterimInterval_Type(Unsigned32):
    """Custom type myDot1xAcctInterimInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 65535),
    )


_MyDot1xAcctInterimInterval_Type.__name__ = "Unsigned32"
_MyDot1xAcctInterimInterval_Object = MibScalar
myDot1xAcctInterimInterval = _MyDot1xAcctInterimInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 18),
    _MyDot1xAcctInterimInterval_Type()
)
myDot1xAcctInterimInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myDot1xAcctInterimInterval.setStatus("current")
_MyDot1xEapolTagEnabled_Type = EnabledStatus
_MyDot1xEapolTagEnabled_Object = MibScalar
myDot1xEapolTagEnabled = _MyDot1xEapolTagEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 19),
    _MyDot1xEapolTagEnabled_Type()
)
myDot1xEapolTagEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myDot1xEapolTagEnabled.setStatus("current")
_MyAAAServerObjects_ObjectIdentity = ObjectIdentity
myAAAServerObjects = _MyAAAServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2)
)
_MyAAAAuthenServerIpAddr_Type = IpAddress
_MyAAAAuthenServerIpAddr_Object = MibScalar
myAAAAuthenServerIpAddr = _MyAAAAuthenServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 1),
    _MyAAAAuthenServerIpAddr_Type()
)
myAAAAuthenServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAAAAuthenServerIpAddr.setStatus("current")


class _MyAAAAuthenServerAuthenPort_Type(Integer32):
    """Custom type myAAAAuthenServerAuthenPort based on Integer32"""
    defaultValue = 1812

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MyAAAAuthenServerAuthenPort_Type.__name__ = "Integer32"
_MyAAAAuthenServerAuthenPort_Object = MibScalar
myAAAAuthenServerAuthenPort = _MyAAAAuthenServerAuthenPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 2),
    _MyAAAAuthenServerAuthenPort_Type()
)
myAAAAuthenServerAuthenPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAAAAuthenServerAuthenPort.setStatus("current")


class _MyAAAServerObjectsAcctPort_Type(Integer32):
    """Custom type myAAAServerObjectsAcctPort based on Integer32"""
    defaultValue = 1813

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MyAAAServerObjectsAcctPort_Type.__name__ = "Integer32"
_MyAAAServerObjectsAcctPort_Object = MibScalar
myAAAServerObjectsAcctPort = _MyAAAServerObjectsAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 3),
    _MyAAAServerObjectsAcctPort_Type()
)
myAAAServerObjectsAcctPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAAAServerObjectsAcctPort.setStatus("current")


class _MyAAAKeyStrOfAAAServer_Type(DisplayString):
    """Custom type myAAAKeyStrOfAAAServer based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_MyAAAKeyStrOfAAAServer_Type.__name__ = "DisplayString"
_MyAAAKeyStrOfAAAServer_Object = MibScalar
myAAAKeyStrOfAAAServer = _MyAAAKeyStrOfAAAServer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 4),
    _MyAAAKeyStrOfAAAServer_Type()
)
myAAAKeyStrOfAAAServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAAAKeyStrOfAAAServer.setStatus("current")
_MyAAAAccountServerIpAddr_Type = IpAddress
_MyAAAAccountServerIpAddr_Object = MibScalar
myAAAAccountServerIpAddr = _MyAAAAccountServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 5),
    _MyAAAAccountServerIpAddr_Type()
)
myAAAAccountServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAAAAccountServerIpAddr.setStatus("current")
_MyAAAAccountBackUpServerIpAddr_Type = IpAddress
_MyAAAAccountBackUpServerIpAddr_Object = MibScalar
myAAAAccountBackUpServerIpAddr = _MyAAAAccountBackUpServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 6),
    _MyAAAAccountBackUpServerIpAddr_Type()
)
myAAAAccountBackUpServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAAAAccountBackUpServerIpAddr.setStatus("current")
_MyAAAAuthenBackUpServerIpAddr_Type = IpAddress
_MyAAAAuthenBackUpServerIpAddr_Object = MibScalar
myAAAAuthenBackUpServerIpAddr = _MyAAAAuthenBackUpServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 7),
    _MyAAAAuthenBackUpServerIpAddr_Type()
)
myAAAAuthenBackUpServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAAAAuthenBackUpServerIpAddr.setStatus("current")
_MyAuthUserObjects_ObjectIdentity = ObjectIdentity
myAuthUserObjects = _MyAuthUserObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3)
)
_MyAuthAddrTable_Object = MibTable
myAuthAddrTable = _MyAuthAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3, 1)
)
if mibBuilder.loadTexts:
    myAuthAddrTable.setStatus("current")
_MyAuthAddrEntry_Object = MibTableRow
myAuthAddrEntry = _MyAuthAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3, 1, 1)
)
myAuthAddrEntry.setIndexNames(
    (0, "MY-AAA-MIB", "myAuthPort"),
    (0, "MY-AAA-MIB", "myAuthMacAddress"),
)
if mibBuilder.loadTexts:
    myAuthAddrEntry.setStatus("current")
_MyAuthPort_Type = IfIndex
_MyAuthPort_Object = MibTableColumn
myAuthPort = _MyAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3, 1, 1, 1),
    _MyAuthPort_Type()
)
myAuthPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myAuthPort.setStatus("current")
_MyAuthMacAddress_Type = MacAddress
_MyAuthMacAddress_Object = MibTableColumn
myAuthMacAddress = _MyAuthMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3, 1, 1, 2),
    _MyAuthMacAddress_Type()
)
myAuthMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myAuthMacAddress.setStatus("current")


class _MyAuthAddrStatus_Type(Integer32):
    """Custom type myAuthAddrStatus based on Integer32"""
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


_MyAuthAddrStatus_Type.__name__ = "Integer32"
_MyAuthAddrStatus_Object = MibTableColumn
myAuthAddrStatus = _MyAuthAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3, 1, 1, 3),
    _MyAuthAddrStatus_Type()
)
myAuthAddrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAuthAddrStatus.setStatus("current")
_MyAuthUserTable_Object = MibTable
myAuthUserTable = _MyAuthUserTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3, 2)
)
if mibBuilder.loadTexts:
    myAuthUserTable.setStatus("current")
_MyAuthUserEntry_Object = MibTableRow
myAuthUserEntry = _MyAuthUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3, 2, 1)
)
myAuthUserEntry.setIndexNames(
    (0, "MY-AAA-MIB", "myAuthUserFdbId"),
    (0, "MY-AAA-MIB", "myAuthUserMacAddress"),
)
if mibBuilder.loadTexts:
    myAuthUserEntry.setStatus("current")
_MyAuthUserFdbId_Type = Unsigned32
_MyAuthUserFdbId_Object = MibTableColumn
myAuthUserFdbId = _MyAuthUserFdbId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3, 2, 1, 1),
    _MyAuthUserFdbId_Type()
)
myAuthUserFdbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myAuthUserFdbId.setStatus("current")
_MyAuthUserMacAddress_Type = MacAddress
_MyAuthUserMacAddress_Object = MibTableColumn
myAuthUserMacAddress = _MyAuthUserMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3, 2, 1, 2),
    _MyAuthUserMacAddress_Type()
)
myAuthUserMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myAuthUserMacAddress.setStatus("current")
_MyAuthUserName_Type = DisplayString
_MyAuthUserName_Object = MibTableColumn
myAuthUserName = _MyAuthUserName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3, 2, 1, 3),
    _MyAuthUserName_Type()
)
myAuthUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myAuthUserName.setStatus("current")
_MyAuthUserSessionId_Type = DisplayString
_MyAuthUserSessionId_Object = MibTableColumn
myAuthUserSessionId = _MyAuthUserSessionId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3, 2, 1, 4),
    _MyAuthUserSessionId_Type()
)
myAuthUserSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myAuthUserSessionId.setStatus("current")
_MyAuthUserIpAddr_Type = IpAddress
_MyAuthUserIpAddr_Object = MibTableColumn
myAuthUserIpAddr = _MyAuthUserIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3, 2, 1, 5),
    _MyAuthUserIpAddr_Type()
)
myAuthUserIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myAuthUserIpAddr.setStatus("current")
_MyAuthUserPort_Type = Integer32
_MyAuthUserPort_Object = MibTableColumn
myAuthUserPort = _MyAuthUserPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3, 2, 1, 6),
    _MyAuthUserPort_Type()
)
myAuthUserPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myAuthUserPort.setStatus("current")
_MyAuthUserStatus_Type = ConfigStatus
_MyAuthUserStatus_Object = MibTableColumn
myAuthUserStatus = _MyAuthUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3, 2, 1, 7),
    _MyAuthUserStatus_Type()
)
myAuthUserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAuthUserStatus.setStatus("current")


class _MyAuthUserForVPNDel_Type(DisplayString):
    """Custom type myAuthUserForVPNDel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_MyAuthUserForVPNDel_Type.__name__ = "DisplayString"
_MyAuthUserForVPNDel_Object = MibScalar
myAuthUserForVPNDel = _MyAuthUserForVPNDel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3, 3),
    _MyAuthUserForVPNDel_Type()
)
myAuthUserForVPNDel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAuthUserForVPNDel.setStatus("current")
_MyAuthModeObjects_ObjectIdentity = ObjectIdentity
myAuthModeObjects = _MyAuthModeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 4)
)


class _MyIpAuthorizationMode_Type(Integer32):
    """Custom type myIpAuthorizationMode based on Integer32"""
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


_MyIpAuthorizationMode_Type.__name__ = "Integer32"
_MyIpAuthorizationMode_Object = MibScalar
myIpAuthorizationMode = _MyIpAuthorizationMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 4, 1),
    _MyIpAuthorizationMode_Type()
)
myIpAuthorizationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIpAuthorizationMode.setStatus("current")
_MyClientProbeObjects_ObjectIdentity = ObjectIdentity
myClientProbeObjects = _MyClientProbeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 5)
)
_MyClientProbeEnabledStatus_Type = EnabledStatus
_MyClientProbeEnabledStatus_Object = MibScalar
myClientProbeEnabledStatus = _MyClientProbeEnabledStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 5, 1),
    _MyClientProbeEnabledStatus_Type()
)
myClientProbeEnabledStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myClientProbeEnabledStatus.setStatus("current")
_MyClientProbeHelloInterval_Type = Unsigned32
_MyClientProbeHelloInterval_Object = MibScalar
myClientProbeHelloInterval = _MyClientProbeHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 5, 2),
    _MyClientProbeHelloInterval_Type()
)
myClientProbeHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myClientProbeHelloInterval.setStatus("current")
_MyClientProbeAliveInteval_Type = Unsigned32
_MyClientProbeAliveInteval_Object = MibScalar
myClientProbeAliveInteval = _MyClientProbeAliveInteval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 5, 3),
    _MyClientProbeAliveInteval_Type()
)
myClientProbeAliveInteval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myClientProbeAliveInteval.setStatus("current")
_MyAAAMIBConformance_ObjectIdentity = ObjectIdentity
myAAAMIBConformance = _MyAAAMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 2)
)
_MyAAAMIBCompliances_ObjectIdentity = ObjectIdentity
myAAAMIBCompliances = _MyAAAMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 2, 1)
)
_MyAAAMIBGroups_ObjectIdentity = ObjectIdentity
myAAAMIBGroups = _MyAAAMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 2, 2)
)

# Managed Objects groups

myDot1xAuthMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 2, 2, 1)
)
myDot1xAuthMIBGroup.setObjects(
      *(("MY-AAA-MIB", "myDot1xAuthStatus"),
        ("MY-AAA-MIB", "myDot1xAuthObjectsQuietPeriod"),
        ("MY-AAA-MIB", "myDot1xAuthObjectsTxPeriod"),
        ("MY-AAA-MIB", "myDot1xAuthObjectsSuppTimeout"),
        ("MY-AAA-MIB", "myDot1xAuthObjectsServerTimeout"),
        ("MY-AAA-MIB", "myDot1xAuthObjectsMaxReq"),
        ("MY-AAA-MIB", "myDot1xAuthObjectsReAuthPeriod"),
        ("MY-AAA-MIB", "myDot1xAuthObjectsReAuthEnable"),
        ("MY-AAA-MIB", "myDot1xAuthObjectsConfigFdbId"),
        ("MY-AAA-MIB", "myDot1xAuthObjectsConfigAddr"),
        ("MY-AAA-MIB", "myDot1xAuthObjectsPaeState"),
        ("MY-AAA-MIB", "myDot1xAuthObjectsBackendAuthState"),
        ("MY-AAA-MIB", "myDot1xAuthObjectsAuthControlledPortStatus"),
        ("MY-AAA-MIB", "myDot1xAuthObjectsKeyTxEnabled"),
        ("MY-AAA-MIB", "myDot1xAuthObjectsIfIndex"),
        ("MY-AAA-MIB", "myDot1xAuthObjectsStatsFdbId"),
        ("MY-AAA-MIB", "myDot1xAuthObjectsStatsAddr"),
        ("MY-AAA-MIB", "myDot1xAuthObjectsEapolFramesRx"),
        ("MY-AAA-MIB", "myDot1xAuthObjectsEapolFramesTx"),
        ("MY-AAA-MIB", "myDot1xAuthObjectsEapolMyFramesRx"),
        ("MY-AAA-MIB", "myDot1xAuthObjectsEapolLogoffFramesRx"),
        ("MY-AAA-MIB", "myDot1xAuthObjectsEapolRespIdFramesRx"),
        ("MY-AAA-MIB", "myDot1xAuthObjectsEapolRespFramesRx"),
        ("MY-AAA-MIB", "myDot1xAuthObjectsEapolReqIdFramesTx"),
        ("MY-AAA-MIB", "myDot1xAuthObjectsEapolReqFramesTx"),
        ("MY-AAA-MIB", "myDot1xAuthObjectsInvalidEapolFramesRx"),
        ("MY-AAA-MIB", "myDot1xAuthObjectsEapLengthErrorFramesRx"),
        ("MY-AAA-MIB", "myDot1xAuthObjectsLastEapolFrameVersion"),
        ("MY-AAA-MIB", "myDot1xAuthObjectsLastEapolFrameSource"),
        ("MY-AAA-MIB", "myDot1xCurrentUserNumber"),
        ("MY-AAA-MIB", "myDot1xCurrentAuthenticatedUserNumber"),
        ("MY-AAA-MIB", "myDot1xAuthObjectsMaxReauth"),
        ("MY-AAA-MIB", "myAuthIf"),
        ("MY-AAA-MIB", "myAuthIfStatus"),
        ("MY-AAA-MIB", "myAuthenticationMode"))
)
if mibBuilder.loadTexts:
    myDot1xAuthMIBGroup.setStatus("current")

myAAAServerMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 2, 2, 2)
)
myAAAServerMIBGroup.setObjects(
      *(("MY-AAA-MIB", "myAAAAuthenServerIpAddr"),
        ("MY-AAA-MIB", "myAAAAuthenServerAuthenPort"),
        ("MY-AAA-MIB", "myAAAServerObjectsAcctPort"),
        ("MY-AAA-MIB", "myAAAKeyStrOfAAAServer"),
        ("MY-AAA-MIB", "myAAAAccountServerIpAddr"),
        ("MY-AAA-MIB", "myAAAAccountBackUpServerIpAddr"),
        ("MY-AAA-MIB", "myAAAAuthenBackUpServerIpAddr"))
)
if mibBuilder.loadTexts:
    myAAAServerMIBGroup.setStatus("current")

myAuthAddrMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 2, 2, 3)
)
myAuthAddrMIBGroup.setObjects(
      *(("MY-AAA-MIB", "myAuthMacAddress"),
        ("MY-AAA-MIB", "myAuthPort"),
        ("MY-AAA-MIB", "myAuthAddrStatus"),
        ("MY-AAA-MIB", "myAuthUserFdbId"),
        ("MY-AAA-MIB", "myAuthUserMacAddress"),
        ("MY-AAA-MIB", "myAuthUserName"),
        ("MY-AAA-MIB", "myAuthUserSessionId"),
        ("MY-AAA-MIB", "myAuthUserIpAddr"),
        ("MY-AAA-MIB", "myAuthUserPort"),
        ("MY-AAA-MIB", "myAuthUserStatus"))
)
if mibBuilder.loadTexts:
    myAuthAddrMIBGroup.setStatus("current")

myAuthModeMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 2, 2, 4)
)
myAuthModeMIBGroup.setObjects(
    ("MY-AAA-MIB", "myIpAuthorizationMode")
)
if mibBuilder.loadTexts:
    myAuthModeMIBGroup.setStatus("current")

myClientProbeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 2, 2, 5)
)
myClientProbeGroup.setObjects(
      *(("MY-AAA-MIB", "myClientProbeEnabledStatus"),
        ("MY-AAA-MIB", "myClientProbeHelloInterval"),
        ("MY-AAA-MIB", "myClientProbeAliveInteval"))
)
if mibBuilder.loadTexts:
    myClientProbeGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

myAAAMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 2, 1, 1)
)
myAAAMIBCompliance.setObjects(
      *(("MY-AAA-MIB", "myDot1xAuthMIBGroup"),
        ("MY-AAA-MIB", "myAAAServerMIBGroup"),
        ("MY-AAA-MIB", "myAuthAddrMIBGroup"),
        ("MY-AAA-MIB", "myAuthModeMIBGroup"),
        ("MY-AAA-MIB", "myClientProbeGroup"))
)
if mibBuilder.loadTexts:
    myAAAMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MY-AAA-MIB",
    **{"myAAAMIB": myAAAMIB,
       "myAAAMIBObjects": myAAAMIBObjects,
       "myDot1xAuthObjects": myDot1xAuthObjects,
       "myDot1xAuthStatus": myDot1xAuthStatus,
       "myDot1xAuthObjectsQuietPeriod": myDot1xAuthObjectsQuietPeriod,
       "myDot1xAuthObjectsTxPeriod": myDot1xAuthObjectsTxPeriod,
       "myDot1xAuthObjectsSuppTimeout": myDot1xAuthObjectsSuppTimeout,
       "myDot1xAuthObjectsServerTimeout": myDot1xAuthObjectsServerTimeout,
       "myDot1xAuthObjectsMaxReq": myDot1xAuthObjectsMaxReq,
       "myDot1xAuthObjectsReAuthPeriod": myDot1xAuthObjectsReAuthPeriod,
       "myDot1xAuthObjectsMaxReauth": myDot1xAuthObjectsMaxReauth,
       "myDot1xAuthObjectsReAuthEnable": myDot1xAuthObjectsReAuthEnable,
       "myDot1xAuthObjectsConfigTable": myDot1xAuthObjectsConfigTable,
       "myDot1xAuthObjectsConfigEntry": myDot1xAuthObjectsConfigEntry,
       "myDot1xAuthObjectsConfigFdbId": myDot1xAuthObjectsConfigFdbId,
       "myDot1xAuthObjectsConfigAddr": myDot1xAuthObjectsConfigAddr,
       "myDot1xAuthObjectsPaeState": myDot1xAuthObjectsPaeState,
       "myDot1xAuthObjectsBackendAuthState": myDot1xAuthObjectsBackendAuthState,
       "myDot1xAuthObjectsAuthControlledPortStatus": myDot1xAuthObjectsAuthControlledPortStatus,
       "myDot1xAuthObjectsKeyTxEnabled": myDot1xAuthObjectsKeyTxEnabled,
       "myDot1xAuthObjectsIfIndex": myDot1xAuthObjectsIfIndex,
       "myDot1xAuthObjectsStatsTable": myDot1xAuthObjectsStatsTable,
       "myDot1xAuthStatsEntry": myDot1xAuthStatsEntry,
       "myDot1xAuthObjectsStatsFdbId": myDot1xAuthObjectsStatsFdbId,
       "myDot1xAuthObjectsStatsAddr": myDot1xAuthObjectsStatsAddr,
       "myDot1xAuthObjectsEapolFramesRx": myDot1xAuthObjectsEapolFramesRx,
       "myDot1xAuthObjectsEapolFramesTx": myDot1xAuthObjectsEapolFramesTx,
       "myDot1xAuthObjectsEapolMyFramesRx": myDot1xAuthObjectsEapolMyFramesRx,
       "myDot1xAuthObjectsEapolLogoffFramesRx": myDot1xAuthObjectsEapolLogoffFramesRx,
       "myDot1xAuthObjectsEapolRespIdFramesRx": myDot1xAuthObjectsEapolRespIdFramesRx,
       "myDot1xAuthObjectsEapolRespFramesRx": myDot1xAuthObjectsEapolRespFramesRx,
       "myDot1xAuthObjectsEapolReqIdFramesTx": myDot1xAuthObjectsEapolReqIdFramesTx,
       "myDot1xAuthObjectsEapolReqFramesTx": myDot1xAuthObjectsEapolReqFramesTx,
       "myDot1xAuthObjectsInvalidEapolFramesRx": myDot1xAuthObjectsInvalidEapolFramesRx,
       "myDot1xAuthObjectsEapLengthErrorFramesRx": myDot1xAuthObjectsEapLengthErrorFramesRx,
       "myDot1xAuthObjectsLastEapolFrameVersion": myDot1xAuthObjectsLastEapolFrameVersion,
       "myDot1xAuthObjectsLastEapolFrameSource": myDot1xAuthObjectsLastEapolFrameSource,
       "myDot1xCurrentUserNumber": myDot1xCurrentUserNumber,
       "myDot1xCurrentAuthenticatedUserNumber": myDot1xCurrentAuthenticatedUserNumber,
       "myDot1xAccountStatus": myDot1xAccountStatus,
       "myAuthIfTable": myAuthIfTable,
       "myAuthIfEntry": myAuthIfEntry,
       "myAuthIf": myAuthIf,
       "myAuthIfStatus": myAuthIfStatus,
       "myAuthenticationMode": myAuthenticationMode,
       "myDot1xAccountUpdateStatus": myDot1xAccountUpdateStatus,
       "myDot1xAcctInterimInterval": myDot1xAcctInterimInterval,
       "myDot1xEapolTagEnabled": myDot1xEapolTagEnabled,
       "myAAAServerObjects": myAAAServerObjects,
       "myAAAAuthenServerIpAddr": myAAAAuthenServerIpAddr,
       "myAAAAuthenServerAuthenPort": myAAAAuthenServerAuthenPort,
       "myAAAServerObjectsAcctPort": myAAAServerObjectsAcctPort,
       "myAAAKeyStrOfAAAServer": myAAAKeyStrOfAAAServer,
       "myAAAAccountServerIpAddr": myAAAAccountServerIpAddr,
       "myAAAAccountBackUpServerIpAddr": myAAAAccountBackUpServerIpAddr,
       "myAAAAuthenBackUpServerIpAddr": myAAAAuthenBackUpServerIpAddr,
       "myAuthUserObjects": myAuthUserObjects,
       "myAuthAddrTable": myAuthAddrTable,
       "myAuthAddrEntry": myAuthAddrEntry,
       "myAuthPort": myAuthPort,
       "myAuthMacAddress": myAuthMacAddress,
       "myAuthAddrStatus": myAuthAddrStatus,
       "myAuthUserTable": myAuthUserTable,
       "myAuthUserEntry": myAuthUserEntry,
       "myAuthUserFdbId": myAuthUserFdbId,
       "myAuthUserMacAddress": myAuthUserMacAddress,
       "myAuthUserName": myAuthUserName,
       "myAuthUserSessionId": myAuthUserSessionId,
       "myAuthUserIpAddr": myAuthUserIpAddr,
       "myAuthUserPort": myAuthUserPort,
       "myAuthUserStatus": myAuthUserStatus,
       "myAuthUserForVPNDel": myAuthUserForVPNDel,
       "myAuthModeObjects": myAuthModeObjects,
       "myIpAuthorizationMode": myIpAuthorizationMode,
       "myClientProbeObjects": myClientProbeObjects,
       "myClientProbeEnabledStatus": myClientProbeEnabledStatus,
       "myClientProbeHelloInterval": myClientProbeHelloInterval,
       "myClientProbeAliveInteval": myClientProbeAliveInteval,
       "myAAAMIBConformance": myAAAMIBConformance,
       "myAAAMIBCompliances": myAAAMIBCompliances,
       "myAAAMIBCompliance": myAAAMIBCompliance,
       "myAAAMIBGroups": myAAAMIBGroups,
       "myDot1xAuthMIBGroup": myDot1xAuthMIBGroup,
       "myAAAServerMIBGroup": myAAAServerMIBGroup,
       "myAuthAddrMIBGroup": myAuthAddrMIBGroup,
       "myAuthModeMIBGroup": myAuthModeMIBGroup,
       "myClientProbeGroup": myClientProbeGroup}
)
