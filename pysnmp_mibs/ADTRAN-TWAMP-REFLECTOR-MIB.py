# SNMP MIB module (ADTRAN-TWAMP-REFLECTOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-TWAMP-REFLECTOR-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:32:34 2025
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

(adShared,) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adShared")

(adGenTWAMPReflector,
 adTWAMPReflectorID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-EOCU-MIB",
    "adGenTWAMPReflector",
    "adTWAMPReflectorID")

(InterfaceIndex,
 OwnerString,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "OwnerString",
    "ifIndex")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

adtranTwampReflectorMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 69, 5, 1)
)
if mibBuilder.loadTexts:
    adtranTwampReflectorMib.setRevisions(
        ("2008-01-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdTWAMPReflectorObjects_ObjectIdentity = ObjectIdentity
adTWAMPReflectorObjects = _AdTWAMPReflectorObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1)
)
_AdTWAMPReflectorAppl_ObjectIdentity = ObjectIdentity
adTWAMPReflectorAppl = _AdTWAMPReflectorAppl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 1)
)


class _AdTWAMPReflectorApplClearCounters_Type(Integer32):
    """Custom type adTWAMPReflectorApplClearCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearCounters", 1)
    )


_AdTWAMPReflectorApplClearCounters_Type.__name__ = "Integer32"
_AdTWAMPReflectorApplClearCounters_Object = MibScalar
adTWAMPReflectorApplClearCounters = _AdTWAMPReflectorApplClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 1, 1),
    _AdTWAMPReflectorApplClearCounters_Type()
)
adTWAMPReflectorApplClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTWAMPReflectorApplClearCounters.setStatus("current")
_AdTWAMPReflectorCtrl_ObjectIdentity = ObjectIdentity
adTWAMPReflectorCtrl = _AdTWAMPReflectorCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 2)
)


class _AdTWAMPReflectorCtrlEnable_Type(Integer32):
    """Custom type adTWAMPReflectorCtrlEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AdTWAMPReflectorCtrlEnable_Type.__name__ = "Integer32"
_AdTWAMPReflectorCtrlEnable_Object = MibScalar
adTWAMPReflectorCtrlEnable = _AdTWAMPReflectorCtrlEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 2, 1),
    _AdTWAMPReflectorCtrlEnable_Type()
)
adTWAMPReflectorCtrlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTWAMPReflectorCtrlEnable.setStatus("current")


class _AdTWAMPReflectorCtrlTCPport_Type(Integer32):
    """Custom type adTWAMPReflectorCtrlTCPport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AdTWAMPReflectorCtrlTCPport_Type.__name__ = "Integer32"
_AdTWAMPReflectorCtrlTCPport_Object = MibScalar
adTWAMPReflectorCtrlTCPport = _AdTWAMPReflectorCtrlTCPport_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 2, 2),
    _AdTWAMPReflectorCtrlTCPport_Type()
)
adTWAMPReflectorCtrlTCPport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTWAMPReflectorCtrlTCPport.setStatus("current")
if mibBuilder.loadTexts:
    adTWAMPReflectorCtrlTCPport.setUnits("octets")


class _AdTWAMPReflectorCtrlMaxSessions_Type(Integer32):
    """Custom type adTWAMPReflectorCtrlMaxSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AdTWAMPReflectorCtrlMaxSessions_Type.__name__ = "Integer32"
_AdTWAMPReflectorCtrlMaxSessions_Object = MibScalar
adTWAMPReflectorCtrlMaxSessions = _AdTWAMPReflectorCtrlMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 2, 3),
    _AdTWAMPReflectorCtrlMaxSessions_Type()
)
adTWAMPReflectorCtrlMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTWAMPReflectorCtrlMaxSessions.setStatus("current")
if mibBuilder.loadTexts:
    adTWAMPReflectorCtrlMaxSessions.setUnits("octets")


class _AdTWAMPReflectorCtrlTimeout_Type(Integer32):
    """Custom type adTWAMPReflectorCtrlTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AdTWAMPReflectorCtrlTimeout_Type.__name__ = "Integer32"
_AdTWAMPReflectorCtrlTimeout_Object = MibScalar
adTWAMPReflectorCtrlTimeout = _AdTWAMPReflectorCtrlTimeout_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 2, 4),
    _AdTWAMPReflectorCtrlTimeout_Type()
)
adTWAMPReflectorCtrlTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTWAMPReflectorCtrlTimeout.setStatus("current")
if mibBuilder.loadTexts:
    adTWAMPReflectorCtrlTimeout.setUnits("octets")


class _AdTWAMPReflectorCtrlTestTimeout_Type(Integer32):
    """Custom type adTWAMPReflectorCtrlTestTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AdTWAMPReflectorCtrlTestTimeout_Type.__name__ = "Integer32"
_AdTWAMPReflectorCtrlTestTimeout_Object = MibScalar
adTWAMPReflectorCtrlTestTimeout = _AdTWAMPReflectorCtrlTestTimeout_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 2, 5),
    _AdTWAMPReflectorCtrlTestTimeout_Type()
)
adTWAMPReflectorCtrlTestTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTWAMPReflectorCtrlTestTimeout.setStatus("current")
if mibBuilder.loadTexts:
    adTWAMPReflectorCtrlTestTimeout.setUnits("octets")
_AdTWAMPReflectorTestUDPportRange_Type = OctetString
_AdTWAMPReflectorTestUDPportRange_Object = MibScalar
adTWAMPReflectorTestUDPportRange = _AdTWAMPReflectorTestUDPportRange_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 2, 6),
    _AdTWAMPReflectorTestUDPportRange_Type()
)
adTWAMPReflectorTestUDPportRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTWAMPReflectorTestUDPportRange.setStatus("current")
_AdTWAMPReflectorStats_ObjectIdentity = ObjectIdentity
adTWAMPReflectorStats = _AdTWAMPReflectorStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 3)
)
_AdTWAMPReflectorStatsRxTestPkts_Type = Gauge32
_AdTWAMPReflectorStatsRxTestPkts_Object = MibScalar
adTWAMPReflectorStatsRxTestPkts = _AdTWAMPReflectorStatsRxTestPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 3, 1),
    _AdTWAMPReflectorStatsRxTestPkts_Type()
)
adTWAMPReflectorStatsRxTestPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTWAMPReflectorStatsRxTestPkts.setStatus("current")
_AdTWAMPReflectorStatsTxTestPkts_Type = Gauge32
_AdTWAMPReflectorStatsTxTestPkts_Object = MibScalar
adTWAMPReflectorStatsTxTestPkts = _AdTWAMPReflectorStatsTxTestPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 3, 2),
    _AdTWAMPReflectorStatsTxTestPkts_Type()
)
adTWAMPReflectorStatsTxTestPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTWAMPReflectorStatsTxTestPkts.setStatus("current")
_AdTWAMPReflectorStatsSessionsOpened_Type = Gauge32
_AdTWAMPReflectorStatsSessionsOpened_Object = MibScalar
adTWAMPReflectorStatsSessionsOpened = _AdTWAMPReflectorStatsSessionsOpened_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 3, 3),
    _AdTWAMPReflectorStatsSessionsOpened_Type()
)
adTWAMPReflectorStatsSessionsOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTWAMPReflectorStatsSessionsOpened.setStatus("current")
_AdTWAMPReflectorStatsSessionsClosed_Type = Gauge32
_AdTWAMPReflectorStatsSessionsClosed_Object = MibScalar
adTWAMPReflectorStatsSessionsClosed = _AdTWAMPReflectorStatsSessionsClosed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 3, 4),
    _AdTWAMPReflectorStatsSessionsClosed_Type()
)
adTWAMPReflectorStatsSessionsClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTWAMPReflectorStatsSessionsClosed.setStatus("current")
_AdTWAMPReflectorStatsSessionsRejected_Type = Gauge32
_AdTWAMPReflectorStatsSessionsRejected_Object = MibScalar
adTWAMPReflectorStatsSessionsRejected = _AdTWAMPReflectorStatsSessionsRejected_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 3, 5),
    _AdTWAMPReflectorStatsSessionsRejected_Type()
)
adTWAMPReflectorStatsSessionsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTWAMPReflectorStatsSessionsRejected.setStatus("current")
_AdTWAMPReflectorStatsSessionsActive_Type = Gauge32
_AdTWAMPReflectorStatsSessionsActive_Object = MibScalar
adTWAMPReflectorStatsSessionsActive = _AdTWAMPReflectorStatsSessionsActive_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 3, 6),
    _AdTWAMPReflectorStatsSessionsActive_Type()
)
adTWAMPReflectorStatsSessionsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTWAMPReflectorStatsSessionsActive.setStatus("current")
_AdTWAMPReflectorStatsTestSessionsOpened_Type = Gauge32
_AdTWAMPReflectorStatsTestSessionsOpened_Object = MibScalar
adTWAMPReflectorStatsTestSessionsOpened = _AdTWAMPReflectorStatsTestSessionsOpened_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 3, 7),
    _AdTWAMPReflectorStatsTestSessionsOpened_Type()
)
adTWAMPReflectorStatsTestSessionsOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTWAMPReflectorStatsTestSessionsOpened.setStatus("current")
_AdTWAMPReflectorStatsTestSessionsClosed_Type = Gauge32
_AdTWAMPReflectorStatsTestSessionsClosed_Object = MibScalar
adTWAMPReflectorStatsTestSessionsClosed = _AdTWAMPReflectorStatsTestSessionsClosed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 3, 8),
    _AdTWAMPReflectorStatsTestSessionsClosed_Type()
)
adTWAMPReflectorStatsTestSessionsClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTWAMPReflectorStatsTestSessionsClosed.setStatus("current")
_AdTWAMPReflectorStatsTestSessionsRejected_Type = Gauge32
_AdTWAMPReflectorStatsTestSessionsRejected_Object = MibScalar
adTWAMPReflectorStatsTestSessionsRejected = _AdTWAMPReflectorStatsTestSessionsRejected_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 3, 9),
    _AdTWAMPReflectorStatsTestSessionsRejected_Type()
)
adTWAMPReflectorStatsTestSessionsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTWAMPReflectorStatsTestSessionsRejected.setStatus("current")
_AdTWAMPReflectorStatsTestSessionsActive_Type = Gauge32
_AdTWAMPReflectorStatsTestSessionsActive_Object = MibScalar
adTWAMPReflectorStatsTestSessionsActive = _AdTWAMPReflectorStatsTestSessionsActive_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 3, 10),
    _AdTWAMPReflectorStatsTestSessionsActive_Type()
)
adTWAMPReflectorStatsTestSessionsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTWAMPReflectorStatsTestSessionsActive.setStatus("current")
_AdTWAMPVerboseServerStatsTable_Object = MibTable
adTWAMPVerboseServerStatsTable = _AdTWAMPVerboseServerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 3, 11)
)
if mibBuilder.loadTexts:
    adTWAMPVerboseServerStatsTable.setStatus("current")
_AdTWAMPVerboseServerStatsEntry_Object = MibTableRow
adTWAMPVerboseServerStatsEntry = _AdTWAMPVerboseServerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 3, 11, 1)
)
adTWAMPVerboseServerStatsEntry.setIndexNames(
    (0, "ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPClientIpAddress"),
    (0, "ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPClientTcpSourcePort"),
)
if mibBuilder.loadTexts:
    adTWAMPVerboseServerStatsEntry.setStatus("current")
_AdTWAMPClientIpAddress_Type = IpAddress
_AdTWAMPClientIpAddress_Object = MibTableColumn
adTWAMPClientIpAddress = _AdTWAMPClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 3, 11, 1, 1),
    _AdTWAMPClientIpAddress_Type()
)
adTWAMPClientIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adTWAMPClientIpAddress.setStatus("current")
_AdTWAMPClientTcpSourcePort_Type = Integer32
_AdTWAMPClientTcpSourcePort_Object = MibTableColumn
adTWAMPClientTcpSourcePort = _AdTWAMPClientTcpSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 3, 11, 1, 2),
    _AdTWAMPClientTcpSourcePort_Type()
)
adTWAMPClientTcpSourcePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adTWAMPClientTcpSourcePort.setStatus("current")
_AdTWAMPClientTcpDestPort_Type = Integer32
_AdTWAMPClientTcpDestPort_Object = MibTableColumn
adTWAMPClientTcpDestPort = _AdTWAMPClientTcpDestPort_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 3, 11, 1, 3),
    _AdTWAMPClientTcpDestPort_Type()
)
adTWAMPClientTcpDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTWAMPClientTcpDestPort.setStatus("current")


class _AdTWAMPVerboseServerStatsState_Type(Integer32):
    """Custom type adTWAMPVerboseServerStatsState based on Integer32"""
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
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("initialized", 1),
          ("opening", 2),
          ("setup", 3),
          ("starting", 4),
          ("active", 5),
          ("registerSession", 6),
          ("acceptSession", 7),
          ("startSessions", 8),
          ("startAck", 9),
          ("stopSessions", 10),
          ("stopAck", 11),
          ("closed", 12),
          ("reserved", 13),
          ("unknown", 14))
    )


_AdTWAMPVerboseServerStatsState_Type.__name__ = "Integer32"
_AdTWAMPVerboseServerStatsState_Object = MibTableColumn
adTWAMPVerboseServerStatsState = _AdTWAMPVerboseServerStatsState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 3, 11, 1, 4),
    _AdTWAMPVerboseServerStatsState_Type()
)
adTWAMPVerboseServerStatsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTWAMPVerboseServerStatsState.setStatus("current")
_AdTWAMPVerboseServerStatsRxTestPkts_Type = Integer32
_AdTWAMPVerboseServerStatsRxTestPkts_Object = MibTableColumn
adTWAMPVerboseServerStatsRxTestPkts = _AdTWAMPVerboseServerStatsRxTestPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 3, 11, 1, 5),
    _AdTWAMPVerboseServerStatsRxTestPkts_Type()
)
adTWAMPVerboseServerStatsRxTestPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTWAMPVerboseServerStatsRxTestPkts.setStatus("current")
_AdTWAMPVerboseServerStatsTxTestPkts_Type = Integer32
_AdTWAMPVerboseServerStatsTxTestPkts_Object = MibTableColumn
adTWAMPVerboseServerStatsTxTestPkts = _AdTWAMPVerboseServerStatsTxTestPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 3, 11, 1, 6),
    _AdTWAMPVerboseServerStatsTxTestPkts_Type()
)
adTWAMPVerboseServerStatsTxTestPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTWAMPVerboseServerStatsTxTestPkts.setStatus("current")


class _AdTWAMPVerboseServerStatsAuthMode_Type(Integer32):
    """Custom type adTWAMPVerboseServerStatsAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unauthenticated", 1),
          ("authenticated", 2),
          ("encrypted", 3))
    )


_AdTWAMPVerboseServerStatsAuthMode_Type.__name__ = "Integer32"
_AdTWAMPVerboseServerStatsAuthMode_Object = MibTableColumn
adTWAMPVerboseServerStatsAuthMode = _AdTWAMPVerboseServerStatsAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 3, 11, 1, 7),
    _AdTWAMPVerboseServerStatsAuthMode_Type()
)
adTWAMPVerboseServerStatsAuthMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTWAMPVerboseServerStatsAuthMode.setStatus("current")
_AdTWAMPVerboseServerStatsServTmo_Type = Integer32
_AdTWAMPVerboseServerStatsServTmo_Object = MibTableColumn
adTWAMPVerboseServerStatsServTmo = _AdTWAMPVerboseServerStatsServTmo_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 3, 11, 1, 8),
    _AdTWAMPVerboseServerStatsServTmo_Type()
)
adTWAMPVerboseServerStatsServTmo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTWAMPVerboseServerStatsServTmo.setStatus("current")
_AdTWAMPVerboseServerStatsServTmoRemaining_Type = Integer32
_AdTWAMPVerboseServerStatsServTmoRemaining_Object = MibTableColumn
adTWAMPVerboseServerStatsServTmoRemaining = _AdTWAMPVerboseServerStatsServTmoRemaining_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 3, 11, 1, 9),
    _AdTWAMPVerboseServerStatsServTmoRemaining_Type()
)
adTWAMPVerboseServerStatsServTmoRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTWAMPVerboseServerStatsServTmoRemaining.setStatus("current")


class _AdTWAMPVerboseServerStatsServTmoStatus_Type(Integer32):
    """Custom type adTWAMPVerboseServerStatsServTmoStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("suspendedForActiveTestSession", 2),
          ("serverClosurePending", 3))
    )


_AdTWAMPVerboseServerStatsServTmoStatus_Type.__name__ = "Integer32"
_AdTWAMPVerboseServerStatsServTmoStatus_Object = MibTableColumn
adTWAMPVerboseServerStatsServTmoStatus = _AdTWAMPVerboseServerStatsServTmoStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 3, 11, 1, 10),
    _AdTWAMPVerboseServerStatsServTmoStatus_Type()
)
adTWAMPVerboseServerStatsServTmoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTWAMPVerboseServerStatsServTmoStatus.setStatus("current")
_AdTWAMPVerboseReflectorStatsTable_Object = MibTable
adTWAMPVerboseReflectorStatsTable = _AdTWAMPVerboseReflectorStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 3, 12)
)
if mibBuilder.loadTexts:
    adTWAMPVerboseReflectorStatsTable.setStatus("current")
_AdTWAMPVerboseReflectorStatsEntry_Object = MibTableRow
adTWAMPVerboseReflectorStatsEntry = _AdTWAMPVerboseReflectorStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 3, 12, 1)
)
adTWAMPVerboseReflectorStatsEntry.setIndexNames(
    (0, "ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPSenderIpAddress"),
    (0, "ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPSenderUdpDestPort"),
)
if mibBuilder.loadTexts:
    adTWAMPVerboseReflectorStatsEntry.setStatus("current")
_AdTWAMPSenderIpAddress_Type = IpAddress
_AdTWAMPSenderIpAddress_Object = MibTableColumn
adTWAMPSenderIpAddress = _AdTWAMPSenderIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 3, 12, 1, 1),
    _AdTWAMPSenderIpAddress_Type()
)
adTWAMPSenderIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adTWAMPSenderIpAddress.setStatus("current")
_AdTWAMPSenderUdpDestPort_Type = Integer32
_AdTWAMPSenderUdpDestPort_Object = MibTableColumn
adTWAMPSenderUdpDestPort = _AdTWAMPSenderUdpDestPort_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 3, 12, 1, 2),
    _AdTWAMPSenderUdpDestPort_Type()
)
adTWAMPSenderUdpDestPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adTWAMPSenderUdpDestPort.setStatus("current")
_AdTWAMPSenderUdpSourcePort_Type = Integer32
_AdTWAMPSenderUdpSourcePort_Object = MibTableColumn
adTWAMPSenderUdpSourcePort = _AdTWAMPSenderUdpSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 3, 12, 1, 3),
    _AdTWAMPSenderUdpSourcePort_Type()
)
adTWAMPSenderUdpSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTWAMPSenderUdpSourcePort.setStatus("current")
_AdTWAMPAssociatedClientIpAddress_Type = IpAddress
_AdTWAMPAssociatedClientIpAddress_Object = MibTableColumn
adTWAMPAssociatedClientIpAddress = _AdTWAMPAssociatedClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 3, 12, 1, 4),
    _AdTWAMPAssociatedClientIpAddress_Type()
)
adTWAMPAssociatedClientIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTWAMPAssociatedClientIpAddress.setStatus("current")
_AdTWAMPAssociatedClientTcpSourcePort_Type = Integer32
_AdTWAMPAssociatedClientTcpSourcePort_Object = MibTableColumn
adTWAMPAssociatedClientTcpSourcePort = _AdTWAMPAssociatedClientTcpSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 3, 12, 1, 5),
    _AdTWAMPAssociatedClientTcpSourcePort_Type()
)
adTWAMPAssociatedClientTcpSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTWAMPAssociatedClientTcpSourcePort.setStatus("current")


class _AdTWAMPVerboseReflectorStatsState_Type(Integer32):
    """Custom type adTWAMPVerboseReflectorStatsState based on Integer32"""
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
        *(("initialized", 1),
          ("waitingToStart", 2),
          ("inProgress", 3),
          ("stopping", 4),
          ("stopped", 5),
          ("exception", 6),
          ("unknown", 7))
    )


_AdTWAMPVerboseReflectorStatsState_Type.__name__ = "Integer32"
_AdTWAMPVerboseReflectorStatsState_Object = MibTableColumn
adTWAMPVerboseReflectorStatsState = _AdTWAMPVerboseReflectorStatsState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 3, 12, 1, 6),
    _AdTWAMPVerboseReflectorStatsState_Type()
)
adTWAMPVerboseReflectorStatsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTWAMPVerboseReflectorStatsState.setStatus("current")
_AdTWAMPVerboseReflectorStatsRxTestPkts_Type = Integer32
_AdTWAMPVerboseReflectorStatsRxTestPkts_Object = MibTableColumn
adTWAMPVerboseReflectorStatsRxTestPkts = _AdTWAMPVerboseReflectorStatsRxTestPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 3, 12, 1, 7),
    _AdTWAMPVerboseReflectorStatsRxTestPkts_Type()
)
adTWAMPVerboseReflectorStatsRxTestPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTWAMPVerboseReflectorStatsRxTestPkts.setStatus("current")
_AdTWAMPVerboseReflectorStatsTxTestPkts_Type = Integer32
_AdTWAMPVerboseReflectorStatsTxTestPkts_Object = MibTableColumn
adTWAMPVerboseReflectorStatsTxTestPkts = _AdTWAMPVerboseReflectorStatsTxTestPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 3, 12, 1, 8),
    _AdTWAMPVerboseReflectorStatsTxTestPkts_Type()
)
adTWAMPVerboseReflectorStatsTxTestPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTWAMPVerboseReflectorStatsTxTestPkts.setStatus("current")
_AdTWAMPVerboseReflectorStatsPaddingLength_Type = Integer32
_AdTWAMPVerboseReflectorStatsPaddingLength_Object = MibTableColumn
adTWAMPVerboseReflectorStatsPaddingLength = _AdTWAMPVerboseReflectorStatsPaddingLength_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 3, 12, 1, 9),
    _AdTWAMPVerboseReflectorStatsPaddingLength_Type()
)
adTWAMPVerboseReflectorStatsPaddingLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTWAMPVerboseReflectorStatsPaddingLength.setStatus("current")
_AdTWAMPVerboseReflectorStatsTypePDescriptor_Type = Integer32
_AdTWAMPVerboseReflectorStatsTypePDescriptor_Object = MibTableColumn
adTWAMPVerboseReflectorStatsTypePDescriptor = _AdTWAMPVerboseReflectorStatsTypePDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 3, 12, 1, 10),
    _AdTWAMPVerboseReflectorStatsTypePDescriptor_Type()
)
adTWAMPVerboseReflectorStatsTypePDescriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTWAMPVerboseReflectorStatsTypePDescriptor.setStatus("current")
_AdTWAMPVerboseReflectorStatsPacketTimeout_Type = Integer32
_AdTWAMPVerboseReflectorStatsPacketTimeout_Object = MibTableColumn
adTWAMPVerboseReflectorStatsPacketTimeout = _AdTWAMPVerboseReflectorStatsPacketTimeout_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 3, 12, 1, 11),
    _AdTWAMPVerboseReflectorStatsPacketTimeout_Type()
)
adTWAMPVerboseReflectorStatsPacketTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTWAMPVerboseReflectorStatsPacketTimeout.setStatus("current")
_AdTWAMPVerboseReflectorStatsTestTmo_Type = Integer32
_AdTWAMPVerboseReflectorStatsTestTmo_Object = MibTableColumn
adTWAMPVerboseReflectorStatsTestTmo = _AdTWAMPVerboseReflectorStatsTestTmo_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 3, 12, 1, 12),
    _AdTWAMPVerboseReflectorStatsTestTmo_Type()
)
adTWAMPVerboseReflectorStatsTestTmo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTWAMPVerboseReflectorStatsTestTmo.setStatus("current")
_AdTWAMPVerboseReflectorStatsTestTmoRemaining_Type = Integer32
_AdTWAMPVerboseReflectorStatsTestTmoRemaining_Object = MibTableColumn
adTWAMPVerboseReflectorStatsTestTmoRemaining = _AdTWAMPVerboseReflectorStatsTestTmoRemaining_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 3, 12, 1, 13),
    _AdTWAMPVerboseReflectorStatsTestTmoRemaining_Type()
)
adTWAMPVerboseReflectorStatsTestTmoRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTWAMPVerboseReflectorStatsTestTmoRemaining.setStatus("current")


class _AdTWAMPVerboseReflectorStatsTestTmoStatus_Type(Integer32):
    """Custom type adTWAMPVerboseReflectorStatsTestTmoStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("waitingOnPacketTimeout", 2))
    )


_AdTWAMPVerboseReflectorStatsTestTmoStatus_Type.__name__ = "Integer32"
_AdTWAMPVerboseReflectorStatsTestTmoStatus_Object = MibTableColumn
adTWAMPVerboseReflectorStatsTestTmoStatus = _AdTWAMPVerboseReflectorStatsTestTmoStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 3, 12, 1, 14),
    _AdTWAMPVerboseReflectorStatsTestTmoStatus_Type()
)
adTWAMPVerboseReflectorStatsTestTmoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTWAMPVerboseReflectorStatsTestTmoStatus.setStatus("current")
_AdTWAMPReflectorLookup_ObjectIdentity = ObjectIdentity
adTWAMPReflectorLookup = _AdTWAMPReflectorLookup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 4)
)
_AdTWAMPAssociationTable_Object = MibTable
adTWAMPAssociationTable = _AdTWAMPAssociationTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 4, 1)
)
if mibBuilder.loadTexts:
    adTWAMPAssociationTable.setStatus("current")
_AdTWAMPAssociationEntry_Object = MibTableRow
adTWAMPAssociationEntry = _AdTWAMPAssociationEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 4, 1, 1)
)
adTWAMPAssociationEntry.setIndexNames(
    (0, "ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPClientIpAddress"),
    (0, "ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPClientTcpSourcePort"),
    (0, "ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPSenderIpAddress"),
    (0, "ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPSenderUdpDestPort"),
)
if mibBuilder.loadTexts:
    adTWAMPAssociationEntry.setStatus("current")
_AdTWAMPNumOfSpawnedReflectors_Type = Integer32
_AdTWAMPNumOfSpawnedReflectors_Object = MibTableColumn
adTWAMPNumOfSpawnedReflectors = _AdTWAMPNumOfSpawnedReflectors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 1, 4, 1, 1, 1),
    _AdTWAMPNumOfSpawnedReflectors_Type()
)
adTWAMPNumOfSpawnedReflectors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTWAMPNumOfSpawnedReflectors.setStatus("current")
_AdTWAMPReflectorMibConformance_ObjectIdentity = ObjectIdentity
adTWAMPReflectorMibConformance = _AdTWAMPReflectorMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 2)
)
_AdTWAMPReflectorMibGroups_ObjectIdentity = ObjectIdentity
adTWAMPReflectorMibGroups = _AdTWAMPReflectorMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 2, 1)
)

# Managed Objects groups

adTWAMPReflectorApplGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 2, 1, 1)
)
adTWAMPReflectorApplGroupRev1.setObjects(
    ("ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPReflectorApplClearCounters")
)
if mibBuilder.loadTexts:
    adTWAMPReflectorApplGroupRev1.setStatus("current")

adTWAMPReflectorCtrlGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 2, 1, 2)
)
adTWAMPReflectorCtrlGroupRev1.setObjects(
      *(("ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPReflectorCtrlTCPport"),
        ("ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPReflectorCtrlMaxSessions"),
        ("ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPReflectorCtrlEnable"),
        ("ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPReflectorCtrlTimeout"),
        ("ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPReflectorCtrlTestTimeout"))
)
if mibBuilder.loadTexts:
    adTWAMPReflectorCtrlGroupRev1.setStatus("current")

adTWAMPReflectorStatsGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 2, 1, 3)
)
adTWAMPReflectorStatsGroupRev1.setObjects(
      *(("ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPReflectorStatsRxTestPkts"),
        ("ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPReflectorStatsTxTestPkts"),
        ("ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPReflectorStatsSessionsOpened"),
        ("ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPReflectorStatsSessionsClosed"),
        ("ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPReflectorStatsSessionsRejected"),
        ("ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPReflectorStatsSessionsActive"),
        ("ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPReflectorStatsTestSessionsOpened"),
        ("ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPReflectorStatsTestSessionsClosed"),
        ("ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPReflectorStatsTestSessionsRejected"),
        ("ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPReflectorStatsTestSessionsActive"),
        ("ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPClientTcpDestPort"),
        ("ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPVerboseServerStatsState"),
        ("ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPVerboseServerStatsRxTestPkts"),
        ("ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPVerboseServerStatsTxTestPkts"),
        ("ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPVerboseServerStatsAuthMode"),
        ("ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPVerboseServerStatsServTmo"),
        ("ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPVerboseServerStatsServTmoRemaining"),
        ("ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPVerboseServerStatsServTmoStatus"),
        ("ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPSenderUdpSourcePort"),
        ("ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPAssociatedClientIpAddress"),
        ("ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPAssociatedClientTcpSourcePort"),
        ("ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPVerboseReflectorStatsState"),
        ("ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPVerboseReflectorStatsRxTestPkts"),
        ("ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPVerboseReflectorStatsTxTestPkts"),
        ("ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPVerboseReflectorStatsPaddingLength"),
        ("ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPVerboseReflectorStatsTypePDescriptor"),
        ("ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPVerboseReflectorStatsPacketTimeout"),
        ("ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPVerboseReflectorStatsTestTmo"),
        ("ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPVerboseReflectorStatsTestTmoRemaining"),
        ("ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPVerboseReflectorStatsTestTmoStatus"))
)
if mibBuilder.loadTexts:
    adTWAMPReflectorStatsGroupRev1.setStatus("current")

adTWAMPReflectorLookupGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5, 2, 1, 4)
)
adTWAMPReflectorLookupGroupRev1.setObjects(
    ("ADTRAN-TWAMP-REFLECTOR-MIB", "adTWAMPNumOfSpawnedReflectors")
)
if mibBuilder.loadTexts:
    adTWAMPReflectorLookupGroupRev1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-TWAMP-REFLECTOR-MIB",
    **{"adTWAMPReflectorObjects": adTWAMPReflectorObjects,
       "adTWAMPReflectorAppl": adTWAMPReflectorAppl,
       "adTWAMPReflectorApplClearCounters": adTWAMPReflectorApplClearCounters,
       "adTWAMPReflectorCtrl": adTWAMPReflectorCtrl,
       "adTWAMPReflectorCtrlEnable": adTWAMPReflectorCtrlEnable,
       "adTWAMPReflectorCtrlTCPport": adTWAMPReflectorCtrlTCPport,
       "adTWAMPReflectorCtrlMaxSessions": adTWAMPReflectorCtrlMaxSessions,
       "adTWAMPReflectorCtrlTimeout": adTWAMPReflectorCtrlTimeout,
       "adTWAMPReflectorCtrlTestTimeout": adTWAMPReflectorCtrlTestTimeout,
       "adTWAMPReflectorTestUDPportRange": adTWAMPReflectorTestUDPportRange,
       "adTWAMPReflectorStats": adTWAMPReflectorStats,
       "adTWAMPReflectorStatsRxTestPkts": adTWAMPReflectorStatsRxTestPkts,
       "adTWAMPReflectorStatsTxTestPkts": adTWAMPReflectorStatsTxTestPkts,
       "adTWAMPReflectorStatsSessionsOpened": adTWAMPReflectorStatsSessionsOpened,
       "adTWAMPReflectorStatsSessionsClosed": adTWAMPReflectorStatsSessionsClosed,
       "adTWAMPReflectorStatsSessionsRejected": adTWAMPReflectorStatsSessionsRejected,
       "adTWAMPReflectorStatsSessionsActive": adTWAMPReflectorStatsSessionsActive,
       "adTWAMPReflectorStatsTestSessionsOpened": adTWAMPReflectorStatsTestSessionsOpened,
       "adTWAMPReflectorStatsTestSessionsClosed": adTWAMPReflectorStatsTestSessionsClosed,
       "adTWAMPReflectorStatsTestSessionsRejected": adTWAMPReflectorStatsTestSessionsRejected,
       "adTWAMPReflectorStatsTestSessionsActive": adTWAMPReflectorStatsTestSessionsActive,
       "adTWAMPVerboseServerStatsTable": adTWAMPVerboseServerStatsTable,
       "adTWAMPVerboseServerStatsEntry": adTWAMPVerboseServerStatsEntry,
       "adTWAMPClientIpAddress": adTWAMPClientIpAddress,
       "adTWAMPClientTcpSourcePort": adTWAMPClientTcpSourcePort,
       "adTWAMPClientTcpDestPort": adTWAMPClientTcpDestPort,
       "adTWAMPVerboseServerStatsState": adTWAMPVerboseServerStatsState,
       "adTWAMPVerboseServerStatsRxTestPkts": adTWAMPVerboseServerStatsRxTestPkts,
       "adTWAMPVerboseServerStatsTxTestPkts": adTWAMPVerboseServerStatsTxTestPkts,
       "adTWAMPVerboseServerStatsAuthMode": adTWAMPVerboseServerStatsAuthMode,
       "adTWAMPVerboseServerStatsServTmo": adTWAMPVerboseServerStatsServTmo,
       "adTWAMPVerboseServerStatsServTmoRemaining": adTWAMPVerboseServerStatsServTmoRemaining,
       "adTWAMPVerboseServerStatsServTmoStatus": adTWAMPVerboseServerStatsServTmoStatus,
       "adTWAMPVerboseReflectorStatsTable": adTWAMPVerboseReflectorStatsTable,
       "adTWAMPVerboseReflectorStatsEntry": adTWAMPVerboseReflectorStatsEntry,
       "adTWAMPSenderIpAddress": adTWAMPSenderIpAddress,
       "adTWAMPSenderUdpDestPort": adTWAMPSenderUdpDestPort,
       "adTWAMPSenderUdpSourcePort": adTWAMPSenderUdpSourcePort,
       "adTWAMPAssociatedClientIpAddress": adTWAMPAssociatedClientIpAddress,
       "adTWAMPAssociatedClientTcpSourcePort": adTWAMPAssociatedClientTcpSourcePort,
       "adTWAMPVerboseReflectorStatsState": adTWAMPVerboseReflectorStatsState,
       "adTWAMPVerboseReflectorStatsRxTestPkts": adTWAMPVerboseReflectorStatsRxTestPkts,
       "adTWAMPVerboseReflectorStatsTxTestPkts": adTWAMPVerboseReflectorStatsTxTestPkts,
       "adTWAMPVerboseReflectorStatsPaddingLength": adTWAMPVerboseReflectorStatsPaddingLength,
       "adTWAMPVerboseReflectorStatsTypePDescriptor": adTWAMPVerboseReflectorStatsTypePDescriptor,
       "adTWAMPVerboseReflectorStatsPacketTimeout": adTWAMPVerboseReflectorStatsPacketTimeout,
       "adTWAMPVerboseReflectorStatsTestTmo": adTWAMPVerboseReflectorStatsTestTmo,
       "adTWAMPVerboseReflectorStatsTestTmoRemaining": adTWAMPVerboseReflectorStatsTestTmoRemaining,
       "adTWAMPVerboseReflectorStatsTestTmoStatus": adTWAMPVerboseReflectorStatsTestTmoStatus,
       "adTWAMPReflectorLookup": adTWAMPReflectorLookup,
       "adTWAMPAssociationTable": adTWAMPAssociationTable,
       "adTWAMPAssociationEntry": adTWAMPAssociationEntry,
       "adTWAMPNumOfSpawnedReflectors": adTWAMPNumOfSpawnedReflectors,
       "adTWAMPReflectorMibConformance": adTWAMPReflectorMibConformance,
       "adTWAMPReflectorMibGroups": adTWAMPReflectorMibGroups,
       "adTWAMPReflectorApplGroupRev1": adTWAMPReflectorApplGroupRev1,
       "adTWAMPReflectorCtrlGroupRev1": adTWAMPReflectorCtrlGroupRev1,
       "adTWAMPReflectorStatsGroupRev1": adTWAMPReflectorStatsGroupRev1,
       "adTWAMPReflectorLookupGroupRev1": adTWAMPReflectorLookupGroupRev1,
       "adtranTwampReflectorMib": adtranTwampReflectorMib}
)
