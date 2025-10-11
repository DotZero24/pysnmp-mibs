# SNMP MIB module (FS-BFD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-BFD-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:13:53 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

fsBfdMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48)
)
if mibBuilder.loadTexts:
    fsBfdMIB.setRevisions(
        ("2012-04-14 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FSBfdSessIndexTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class FSBfdIntervalTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class FSBfdMultiplierTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class FSBfdDiagTC(TextualConvention, Integer32):
    status = "current"
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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("noDiagnostic", 0),
          ("controlDetectionTimeExpired", 1),
          ("echoFunctionFailed", 2),
          ("neighborSignaledSessionDown", 3),
          ("forwardingPlaneReset", 4),
          ("pathDown", 5),
          ("concatenatedPathDown", 6),
          ("administrativelyDown", 7),
          ("reverseConcatenatedPathDown", 8))
    )



class FSBfdSessTypeTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("singleHop", 1),
          ("multiHopTotallyArbitraryPaths", 2),
          ("multiHopOutOfBandSignaling", 3),
          ("multiHopUnidirectionalLinks", 4),
          ("multiPointHead", 5),
          ("multiPointTail", 6))
    )



class FSBfdSessOperModeTC(TextualConvention, Integer32):
    status = "current"
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
        *(("asyncModeWEchoFunction", 1),
          ("asynchModeWOEchoFunction", 2),
          ("demandModeWEchoFunction", 3),
          ("demandModeWOEchoFunction", 4))
    )



class FSBfdCtrlDestPortNumberTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class FSBfdCtrlSourcePortNumberTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class FSBfdSessStateTC(TextualConvention, Integer32):
    status = "current"
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
        *(("adminDown", 1),
          ("down", 2),
          ("init", 3),
          ("up", 4),
          ("failing", 5))
    )



class FSBfdSessAuthenticationTypeTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noAuthentication", -1),
          ("reserved", 0),
          ("simplePassword", 1),
          ("keyedMD5", 2),
          ("meticulousKeyedMD5", 3),
          ("keyedSHA1", 4),
          ("meticulousKeyedSHA1", 5))
    )



class FSBfdSessionAuthenticationKeyTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x "
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 252),
    )



# MIB Managed Objects in the order of their OIDs

_FsBfdNotifications_ObjectIdentity = ObjectIdentity
fsBfdNotifications = _FsBfdNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 0)
)
_FsBfdObjects_ObjectIdentity = ObjectIdentity
fsBfdObjects = _FsBfdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1)
)
_FsBfdScalarObjects_ObjectIdentity = ObjectIdentity
fsBfdScalarObjects = _FsBfdScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 1)
)


class _FsBfdAdminStatus_Type(Integer32):
    """Custom type fsBfdAdminStatus based on Integer32"""
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


_FsBfdAdminStatus_Type.__name__ = "Integer32"
_FsBfdAdminStatus_Object = MibScalar
fsBfdAdminStatus = _FsBfdAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 1, 1),
    _FsBfdAdminStatus_Type()
)
fsBfdAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBfdAdminStatus.setStatus("current")


class _FsBfdSessNotificationsEnable_Type(TruthValue):
    """Custom type fsBfdSessNotificationsEnable based on TruthValue"""
    defaultValue = 2


_FsBfdSessNotificationsEnable_Type.__name__ = "TruthValue"
_FsBfdSessNotificationsEnable_Object = MibScalar
fsBfdSessNotificationsEnable = _FsBfdSessNotificationsEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 1, 2),
    _FsBfdSessNotificationsEnable_Type()
)
fsBfdSessNotificationsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBfdSessNotificationsEnable.setStatus("current")
_FsBfdSessTable_Object = MibTable
fsBfdSessTable = _FsBfdSessTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2)
)
if mibBuilder.loadTexts:
    fsBfdSessTable.setStatus("current")
_FsBfdSessEntry_Object = MibTableRow
fsBfdSessEntry = _FsBfdSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1)
)
fsBfdSessEntry.setIndexNames(
    (0, "FS-BFD-MIB", "fsBfdSessIndex"),
)
if mibBuilder.loadTexts:
    fsBfdSessEntry.setStatus("current")
_FsBfdSessIndex_Type = FSBfdSessIndexTC
_FsBfdSessIndex_Object = MibTableColumn
fsBfdSessIndex = _FsBfdSessIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 1),
    _FsBfdSessIndex_Type()
)
fsBfdSessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsBfdSessIndex.setStatus("current")


class _FsBfdSessVersionNumber_Type(Unsigned32):
    """Custom type fsBfdSessVersionNumber based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsBfdSessVersionNumber_Type.__name__ = "Unsigned32"
_FsBfdSessVersionNumber_Object = MibTableColumn
fsBfdSessVersionNumber = _FsBfdSessVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 2),
    _FsBfdSessVersionNumber_Type()
)
fsBfdSessVersionNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsBfdSessVersionNumber.setStatus("current")
_FsBfdSessType_Type = FSBfdSessTypeTC
_FsBfdSessType_Object = MibTableColumn
fsBfdSessType = _FsBfdSessType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 3),
    _FsBfdSessType_Type()
)
fsBfdSessType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsBfdSessType.setStatus("current")


class _FsBfdSessDiscriminator_Type(Unsigned32):
    """Custom type fsBfdSessDiscriminator based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FsBfdSessDiscriminator_Type.__name__ = "Unsigned32"
_FsBfdSessDiscriminator_Object = MibTableColumn
fsBfdSessDiscriminator = _FsBfdSessDiscriminator_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 4),
    _FsBfdSessDiscriminator_Type()
)
fsBfdSessDiscriminator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBfdSessDiscriminator.setStatus("current")


class _FsBfdSessRemoteDiscr_Type(Unsigned32):
    """Custom type fsBfdSessRemoteDiscr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_FsBfdSessRemoteDiscr_Type.__name__ = "Unsigned32"
_FsBfdSessRemoteDiscr_Object = MibTableColumn
fsBfdSessRemoteDiscr = _FsBfdSessRemoteDiscr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 5),
    _FsBfdSessRemoteDiscr_Type()
)
fsBfdSessRemoteDiscr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBfdSessRemoteDiscr.setStatus("current")


class _FsBfdSessDestinationUdpPort_Type(FSBfdCtrlDestPortNumberTC):
    """Custom type fsBfdSessDestinationUdpPort based on FSBfdCtrlDestPortNumberTC"""
    defaultValue = 0


_FsBfdSessDestinationUdpPort_Type.__name__ = "FSBfdCtrlDestPortNumberTC"
_FsBfdSessDestinationUdpPort_Object = MibTableColumn
fsBfdSessDestinationUdpPort = _FsBfdSessDestinationUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 6),
    _FsBfdSessDestinationUdpPort_Type()
)
fsBfdSessDestinationUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsBfdSessDestinationUdpPort.setStatus("current")


class _FsBfdSessSourceUdpPort_Type(FSBfdCtrlSourcePortNumberTC):
    """Custom type fsBfdSessSourceUdpPort based on FSBfdCtrlSourcePortNumberTC"""
    defaultValue = 0


_FsBfdSessSourceUdpPort_Type.__name__ = "FSBfdCtrlSourcePortNumberTC"
_FsBfdSessSourceUdpPort_Object = MibTableColumn
fsBfdSessSourceUdpPort = _FsBfdSessSourceUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 7),
    _FsBfdSessSourceUdpPort_Type()
)
fsBfdSessSourceUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsBfdSessSourceUdpPort.setStatus("current")


class _FsBfdSessEchoSourceUdpPort_Type(InetPortNumber):
    """Custom type fsBfdSessEchoSourceUdpPort based on InetPortNumber"""
    defaultValue = 0


_FsBfdSessEchoSourceUdpPort_Type.__name__ = "InetPortNumber"
_FsBfdSessEchoSourceUdpPort_Object = MibTableColumn
fsBfdSessEchoSourceUdpPort = _FsBfdSessEchoSourceUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 8),
    _FsBfdSessEchoSourceUdpPort_Type()
)
fsBfdSessEchoSourceUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsBfdSessEchoSourceUdpPort.setStatus("current")


class _FsBfdSessAdminStatus_Type(Integer32):
    """Custom type fsBfdSessAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stop", 1),
          ("start", 2))
    )


_FsBfdSessAdminStatus_Type.__name__ = "Integer32"
_FsBfdSessAdminStatus_Object = MibTableColumn
fsBfdSessAdminStatus = _FsBfdSessAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 9),
    _FsBfdSessAdminStatus_Type()
)
fsBfdSessAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsBfdSessAdminStatus.setStatus("current")


class _FsBfdSessState_Type(FSBfdSessStateTC):
    """Custom type fsBfdSessState based on FSBfdSessStateTC"""
    defaultValue = 2


_FsBfdSessState_Type.__name__ = "FSBfdSessStateTC"
_FsBfdSessState_Object = MibTableColumn
fsBfdSessState = _FsBfdSessState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 10),
    _FsBfdSessState_Type()
)
fsBfdSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBfdSessState.setStatus("current")


class _FsBfdSessRemoteHeardFlag_Type(TruthValue):
    """Custom type fsBfdSessRemoteHeardFlag based on TruthValue"""
    defaultValue = 2


_FsBfdSessRemoteHeardFlag_Type.__name__ = "TruthValue"
_FsBfdSessRemoteHeardFlag_Object = MibTableColumn
fsBfdSessRemoteHeardFlag = _FsBfdSessRemoteHeardFlag_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 11),
    _FsBfdSessRemoteHeardFlag_Type()
)
fsBfdSessRemoteHeardFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBfdSessRemoteHeardFlag.setStatus("current")
_FsBfdSessDiag_Type = FSBfdDiagTC
_FsBfdSessDiag_Object = MibTableColumn
fsBfdSessDiag = _FsBfdSessDiag_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 12),
    _FsBfdSessDiag_Type()
)
fsBfdSessDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBfdSessDiag.setStatus("current")
_FsBfdSessOperMode_Type = FSBfdSessOperModeTC
_FsBfdSessOperMode_Object = MibTableColumn
fsBfdSessOperMode = _FsBfdSessOperMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 13),
    _FsBfdSessOperMode_Type()
)
fsBfdSessOperMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsBfdSessOperMode.setStatus("current")


class _FsBfdSessDemandModeDesiredFlag_Type(TruthValue):
    """Custom type fsBfdSessDemandModeDesiredFlag based on TruthValue"""
    defaultValue = 2


_FsBfdSessDemandModeDesiredFlag_Type.__name__ = "TruthValue"
_FsBfdSessDemandModeDesiredFlag_Object = MibTableColumn
fsBfdSessDemandModeDesiredFlag = _FsBfdSessDemandModeDesiredFlag_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 14),
    _FsBfdSessDemandModeDesiredFlag_Type()
)
fsBfdSessDemandModeDesiredFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsBfdSessDemandModeDesiredFlag.setStatus("current")


class _FsBfdSessControlPlaneIndepFlag_Type(TruthValue):
    """Custom type fsBfdSessControlPlaneIndepFlag based on TruthValue"""
    defaultValue = 2


_FsBfdSessControlPlaneIndepFlag_Type.__name__ = "TruthValue"
_FsBfdSessControlPlaneIndepFlag_Object = MibTableColumn
fsBfdSessControlPlaneIndepFlag = _FsBfdSessControlPlaneIndepFlag_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 15),
    _FsBfdSessControlPlaneIndepFlag_Type()
)
fsBfdSessControlPlaneIndepFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsBfdSessControlPlaneIndepFlag.setStatus("current")


class _FsBfdSessMultipointFlag_Type(TruthValue):
    """Custom type fsBfdSessMultipointFlag based on TruthValue"""
    defaultValue = 2


_FsBfdSessMultipointFlag_Type.__name__ = "TruthValue"
_FsBfdSessMultipointFlag_Object = MibTableColumn
fsBfdSessMultipointFlag = _FsBfdSessMultipointFlag_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 16),
    _FsBfdSessMultipointFlag_Type()
)
fsBfdSessMultipointFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsBfdSessMultipointFlag.setStatus("current")
_FsBfdSessInterface_Type = InterfaceIndexOrZero
_FsBfdSessInterface_Object = MibTableColumn
fsBfdSessInterface = _FsBfdSessInterface_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 17),
    _FsBfdSessInterface_Type()
)
fsBfdSessInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsBfdSessInterface.setStatus("current")
_FsBfdSessSrcAddrType_Type = InetAddressType
_FsBfdSessSrcAddrType_Object = MibTableColumn
fsBfdSessSrcAddrType = _FsBfdSessSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 18),
    _FsBfdSessSrcAddrType_Type()
)
fsBfdSessSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsBfdSessSrcAddrType.setStatus("current")
_FsBfdSessSrcAddr_Type = InetAddress
_FsBfdSessSrcAddr_Object = MibTableColumn
fsBfdSessSrcAddr = _FsBfdSessSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 19),
    _FsBfdSessSrcAddr_Type()
)
fsBfdSessSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsBfdSessSrcAddr.setStatus("current")
_FsBfdSessDstAddrType_Type = InetAddressType
_FsBfdSessDstAddrType_Object = MibTableColumn
fsBfdSessDstAddrType = _FsBfdSessDstAddrType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 20),
    _FsBfdSessDstAddrType_Type()
)
fsBfdSessDstAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsBfdSessDstAddrType.setStatus("current")
_FsBfdSessDstAddr_Type = InetAddress
_FsBfdSessDstAddr_Object = MibTableColumn
fsBfdSessDstAddr = _FsBfdSessDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 21),
    _FsBfdSessDstAddr_Type()
)
fsBfdSessDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsBfdSessDstAddr.setStatus("current")


class _FsBfdSessGTSM_Type(TruthValue):
    """Custom type fsBfdSessGTSM based on TruthValue"""
    defaultValue = 2


_FsBfdSessGTSM_Type.__name__ = "TruthValue"
_FsBfdSessGTSM_Object = MibTableColumn
fsBfdSessGTSM = _FsBfdSessGTSM_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 22),
    _FsBfdSessGTSM_Type()
)
fsBfdSessGTSM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsBfdSessGTSM.setStatus("current")


class _FsBfdSessGTSMTTL_Type(Unsigned32):
    """Custom type fsBfdSessGTSMTTL based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsBfdSessGTSMTTL_Type.__name__ = "Unsigned32"
_FsBfdSessGTSMTTL_Object = MibTableColumn
fsBfdSessGTSMTTL = _FsBfdSessGTSMTTL_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 23),
    _FsBfdSessGTSMTTL_Type()
)
fsBfdSessGTSMTTL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsBfdSessGTSMTTL.setStatus("current")
_FsBfdSessDesiredMinTxInterval_Type = FSBfdIntervalTC
_FsBfdSessDesiredMinTxInterval_Object = MibTableColumn
fsBfdSessDesiredMinTxInterval = _FsBfdSessDesiredMinTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 24),
    _FsBfdSessDesiredMinTxInterval_Type()
)
fsBfdSessDesiredMinTxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsBfdSessDesiredMinTxInterval.setStatus("current")
_FsBfdSessReqMinRxInterval_Type = FSBfdIntervalTC
_FsBfdSessReqMinRxInterval_Object = MibTableColumn
fsBfdSessReqMinRxInterval = _FsBfdSessReqMinRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 25),
    _FsBfdSessReqMinRxInterval_Type()
)
fsBfdSessReqMinRxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsBfdSessReqMinRxInterval.setStatus("current")
_FsBfdSessReqMinEchoRxInterval_Type = FSBfdIntervalTC
_FsBfdSessReqMinEchoRxInterval_Object = MibTableColumn
fsBfdSessReqMinEchoRxInterval = _FsBfdSessReqMinEchoRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 26),
    _FsBfdSessReqMinEchoRxInterval_Type()
)
fsBfdSessReqMinEchoRxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsBfdSessReqMinEchoRxInterval.setStatus("current")
_FsBfdSessDetectMult_Type = FSBfdMultiplierTC
_FsBfdSessDetectMult_Object = MibTableColumn
fsBfdSessDetectMult = _FsBfdSessDetectMult_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 27),
    _FsBfdSessDetectMult_Type()
)
fsBfdSessDetectMult.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsBfdSessDetectMult.setStatus("current")
_FsBfdSessNegotiatedInterval_Type = FSBfdIntervalTC
_FsBfdSessNegotiatedInterval_Object = MibTableColumn
fsBfdSessNegotiatedInterval = _FsBfdSessNegotiatedInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 28),
    _FsBfdSessNegotiatedInterval_Type()
)
fsBfdSessNegotiatedInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBfdSessNegotiatedInterval.setStatus("current")
_FsBfdSessNegotiatedEchoInterval_Type = FSBfdIntervalTC
_FsBfdSessNegotiatedEchoInterval_Object = MibTableColumn
fsBfdSessNegotiatedEchoInterval = _FsBfdSessNegotiatedEchoInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 29),
    _FsBfdSessNegotiatedEchoInterval_Type()
)
fsBfdSessNegotiatedEchoInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBfdSessNegotiatedEchoInterval.setStatus("current")
_FsBfdSessNegotiatedDetectMult_Type = FSBfdMultiplierTC
_FsBfdSessNegotiatedDetectMult_Object = MibTableColumn
fsBfdSessNegotiatedDetectMult = _FsBfdSessNegotiatedDetectMult_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 30),
    _FsBfdSessNegotiatedDetectMult_Type()
)
fsBfdSessNegotiatedDetectMult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBfdSessNegotiatedDetectMult.setStatus("current")


class _FsBfdSessAuthPresFlag_Type(TruthValue):
    """Custom type fsBfdSessAuthPresFlag based on TruthValue"""
    defaultValue = 2


_FsBfdSessAuthPresFlag_Type.__name__ = "TruthValue"
_FsBfdSessAuthPresFlag_Object = MibTableColumn
fsBfdSessAuthPresFlag = _FsBfdSessAuthPresFlag_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 31),
    _FsBfdSessAuthPresFlag_Type()
)
fsBfdSessAuthPresFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsBfdSessAuthPresFlag.setStatus("current")


class _FsBfdSessAuthenticationType_Type(FSBfdSessAuthenticationTypeTC):
    """Custom type fsBfdSessAuthenticationType based on FSBfdSessAuthenticationTypeTC"""
    defaultValue = -1


_FsBfdSessAuthenticationType_Type.__name__ = "FSBfdSessAuthenticationTypeTC"
_FsBfdSessAuthenticationType_Object = MibTableColumn
fsBfdSessAuthenticationType = _FsBfdSessAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 32),
    _FsBfdSessAuthenticationType_Type()
)
fsBfdSessAuthenticationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsBfdSessAuthenticationType.setStatus("current")


class _FsBfdSessAuthenticationKeyID_Type(Integer32):
    """Custom type fsBfdSessAuthenticationKeyID based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_FsBfdSessAuthenticationKeyID_Type.__name__ = "Integer32"
_FsBfdSessAuthenticationKeyID_Object = MibTableColumn
fsBfdSessAuthenticationKeyID = _FsBfdSessAuthenticationKeyID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 33),
    _FsBfdSessAuthenticationKeyID_Type()
)
fsBfdSessAuthenticationKeyID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsBfdSessAuthenticationKeyID.setStatus("current")
_FsBfdSessAuthenticationKey_Type = FSBfdSessionAuthenticationKeyTC
_FsBfdSessAuthenticationKey_Object = MibTableColumn
fsBfdSessAuthenticationKey = _FsBfdSessAuthenticationKey_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 34),
    _FsBfdSessAuthenticationKey_Type()
)
fsBfdSessAuthenticationKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsBfdSessAuthenticationKey.setStatus("current")
_FsBfdSessStorageType_Type = StorageType
_FsBfdSessStorageType_Object = MibTableColumn
fsBfdSessStorageType = _FsBfdSessStorageType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 35),
    _FsBfdSessStorageType_Type()
)
fsBfdSessStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsBfdSessStorageType.setStatus("current")
_FsBfdSessRowStatus_Type = RowStatus
_FsBfdSessRowStatus_Object = MibTableColumn
fsBfdSessRowStatus = _FsBfdSessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 36),
    _FsBfdSessRowStatus_Type()
)
fsBfdSessRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsBfdSessRowStatus.setStatus("current")


class _FsBfdSessIfName_Type(DisplayString):
    """Custom type fsBfdSessIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsBfdSessIfName_Type.__name__ = "DisplayString"
_FsBfdSessIfName_Object = MibTableColumn
fsBfdSessIfName = _FsBfdSessIfName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 37),
    _FsBfdSessIfName_Type()
)
fsBfdSessIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsBfdSessIfName.setStatus("current")


class _FsBfdSessIfDes_Type(DisplayString):
    """Custom type fsBfdSessIfDes based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsBfdSessIfDes_Type.__name__ = "DisplayString"
_FsBfdSessIfDes_Object = MibTableColumn
fsBfdSessIfDes = _FsBfdSessIfDes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 38),
    _FsBfdSessIfDes_Type()
)
fsBfdSessIfDes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsBfdSessIfDes.setStatus("current")
_FsBfdSessPerfTable_Object = MibTable
fsBfdSessPerfTable = _FsBfdSessPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3)
)
if mibBuilder.loadTexts:
    fsBfdSessPerfTable.setStatus("current")
_FsBfdSessPerfEntry_Object = MibTableRow
fsBfdSessPerfEntry = _FsBfdSessPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3, 1)
)
if mibBuilder.loadTexts:
    fsBfdSessPerfEntry.setStatus("current")
_FsBfdSessPerfCtrlPktIn_Type = Counter32
_FsBfdSessPerfCtrlPktIn_Object = MibTableColumn
fsBfdSessPerfCtrlPktIn = _FsBfdSessPerfCtrlPktIn_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3, 1, 1),
    _FsBfdSessPerfCtrlPktIn_Type()
)
fsBfdSessPerfCtrlPktIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBfdSessPerfCtrlPktIn.setStatus("current")
_FsBfdSessPerfCtrlPktOut_Type = Counter32
_FsBfdSessPerfCtrlPktOut_Object = MibTableColumn
fsBfdSessPerfCtrlPktOut = _FsBfdSessPerfCtrlPktOut_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3, 1, 2),
    _FsBfdSessPerfCtrlPktOut_Type()
)
fsBfdSessPerfCtrlPktOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBfdSessPerfCtrlPktOut.setStatus("current")
_FsBfdSessPerfCtrlPktDrop_Type = Counter32
_FsBfdSessPerfCtrlPktDrop_Object = MibTableColumn
fsBfdSessPerfCtrlPktDrop = _FsBfdSessPerfCtrlPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3, 1, 3),
    _FsBfdSessPerfCtrlPktDrop_Type()
)
fsBfdSessPerfCtrlPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBfdSessPerfCtrlPktDrop.setStatus("current")
_FsBfdSessPerfCtrlPktDropLastTime_Type = TimeStamp
_FsBfdSessPerfCtrlPktDropLastTime_Object = MibTableColumn
fsBfdSessPerfCtrlPktDropLastTime = _FsBfdSessPerfCtrlPktDropLastTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3, 1, 4),
    _FsBfdSessPerfCtrlPktDropLastTime_Type()
)
fsBfdSessPerfCtrlPktDropLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBfdSessPerfCtrlPktDropLastTime.setStatus("current")
_FsBfdSessPerfEchoPktIn_Type = Counter32
_FsBfdSessPerfEchoPktIn_Object = MibTableColumn
fsBfdSessPerfEchoPktIn = _FsBfdSessPerfEchoPktIn_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3, 1, 5),
    _FsBfdSessPerfEchoPktIn_Type()
)
fsBfdSessPerfEchoPktIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBfdSessPerfEchoPktIn.setStatus("current")
_FsBfdSessPerfEchoPktOut_Type = Counter32
_FsBfdSessPerfEchoPktOut_Object = MibTableColumn
fsBfdSessPerfEchoPktOut = _FsBfdSessPerfEchoPktOut_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3, 1, 6),
    _FsBfdSessPerfEchoPktOut_Type()
)
fsBfdSessPerfEchoPktOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBfdSessPerfEchoPktOut.setStatus("current")
_FsBfdSessPerfEchoPktDrop_Type = Counter32
_FsBfdSessPerfEchoPktDrop_Object = MibTableColumn
fsBfdSessPerfEchoPktDrop = _FsBfdSessPerfEchoPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3, 1, 7),
    _FsBfdSessPerfEchoPktDrop_Type()
)
fsBfdSessPerfEchoPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBfdSessPerfEchoPktDrop.setStatus("current")
_FsBfdSessPerfEchoPktDropLastTime_Type = TimeStamp
_FsBfdSessPerfEchoPktDropLastTime_Object = MibTableColumn
fsBfdSessPerfEchoPktDropLastTime = _FsBfdSessPerfEchoPktDropLastTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3, 1, 8),
    _FsBfdSessPerfEchoPktDropLastTime_Type()
)
fsBfdSessPerfEchoPktDropLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBfdSessPerfEchoPktDropLastTime.setStatus("current")
_FsBfdSessUpTime_Type = TimeStamp
_FsBfdSessUpTime_Object = MibTableColumn
fsBfdSessUpTime = _FsBfdSessUpTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3, 1, 9),
    _FsBfdSessUpTime_Type()
)
fsBfdSessUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBfdSessUpTime.setStatus("current")
_FsBfdSessPerfLastSessDownTime_Type = TimeStamp
_FsBfdSessPerfLastSessDownTime_Object = MibTableColumn
fsBfdSessPerfLastSessDownTime = _FsBfdSessPerfLastSessDownTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3, 1, 10),
    _FsBfdSessPerfLastSessDownTime_Type()
)
fsBfdSessPerfLastSessDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBfdSessPerfLastSessDownTime.setStatus("current")
_FsBfdSessPerfLastCommLostDiag_Type = FSBfdDiagTC
_FsBfdSessPerfLastCommLostDiag_Object = MibTableColumn
fsBfdSessPerfLastCommLostDiag = _FsBfdSessPerfLastCommLostDiag_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3, 1, 11),
    _FsBfdSessPerfLastCommLostDiag_Type()
)
fsBfdSessPerfLastCommLostDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBfdSessPerfLastCommLostDiag.setStatus("current")
_FsBfdSessPerfSessUpCount_Type = Counter32
_FsBfdSessPerfSessUpCount_Object = MibTableColumn
fsBfdSessPerfSessUpCount = _FsBfdSessPerfSessUpCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3, 1, 12),
    _FsBfdSessPerfSessUpCount_Type()
)
fsBfdSessPerfSessUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBfdSessPerfSessUpCount.setStatus("current")
_FsBfdSessPerfDiscTime_Type = TimeStamp
_FsBfdSessPerfDiscTime_Object = MibTableColumn
fsBfdSessPerfDiscTime = _FsBfdSessPerfDiscTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3, 1, 13),
    _FsBfdSessPerfDiscTime_Type()
)
fsBfdSessPerfDiscTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBfdSessPerfDiscTime.setStatus("current")
_FsBfdSessPerfCtrlPktInHC_Type = Counter64
_FsBfdSessPerfCtrlPktInHC_Object = MibTableColumn
fsBfdSessPerfCtrlPktInHC = _FsBfdSessPerfCtrlPktInHC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3, 1, 14),
    _FsBfdSessPerfCtrlPktInHC_Type()
)
fsBfdSessPerfCtrlPktInHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBfdSessPerfCtrlPktInHC.setStatus("current")
_FsBfdSessPerfCtrlPktOutHC_Type = Counter64
_FsBfdSessPerfCtrlPktOutHC_Object = MibTableColumn
fsBfdSessPerfCtrlPktOutHC = _FsBfdSessPerfCtrlPktOutHC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3, 1, 15),
    _FsBfdSessPerfCtrlPktOutHC_Type()
)
fsBfdSessPerfCtrlPktOutHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBfdSessPerfCtrlPktOutHC.setStatus("current")
_FsBfdSessPerfCtrlPktDropHC_Type = Counter64
_FsBfdSessPerfCtrlPktDropHC_Object = MibTableColumn
fsBfdSessPerfCtrlPktDropHC = _FsBfdSessPerfCtrlPktDropHC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3, 1, 16),
    _FsBfdSessPerfCtrlPktDropHC_Type()
)
fsBfdSessPerfCtrlPktDropHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBfdSessPerfCtrlPktDropHC.setStatus("current")
_FsBfdSessPerfEchoPktInHC_Type = Counter64
_FsBfdSessPerfEchoPktInHC_Object = MibTableColumn
fsBfdSessPerfEchoPktInHC = _FsBfdSessPerfEchoPktInHC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3, 1, 17),
    _FsBfdSessPerfEchoPktInHC_Type()
)
fsBfdSessPerfEchoPktInHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBfdSessPerfEchoPktInHC.setStatus("current")
_FsBfdSessPerfEchoPktOutHC_Type = Counter64
_FsBfdSessPerfEchoPktOutHC_Object = MibTableColumn
fsBfdSessPerfEchoPktOutHC = _FsBfdSessPerfEchoPktOutHC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3, 1, 18),
    _FsBfdSessPerfEchoPktOutHC_Type()
)
fsBfdSessPerfEchoPktOutHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBfdSessPerfEchoPktOutHC.setStatus("current")
_FsBfdSessPerfEchoPktDropHC_Type = Counter64
_FsBfdSessPerfEchoPktDropHC_Object = MibTableColumn
fsBfdSessPerfEchoPktDropHC = _FsBfdSessPerfEchoPktDropHC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3, 1, 19),
    _FsBfdSessPerfEchoPktDropHC_Type()
)
fsBfdSessPerfEchoPktDropHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBfdSessPerfEchoPktDropHC.setStatus("current")
_FsBfdSessDiscMapTable_Object = MibTable
fsBfdSessDiscMapTable = _FsBfdSessDiscMapTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 4)
)
if mibBuilder.loadTexts:
    fsBfdSessDiscMapTable.setStatus("current")
_FsBfdSessDiscMapEntry_Object = MibTableRow
fsBfdSessDiscMapEntry = _FsBfdSessDiscMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 4, 1)
)
fsBfdSessDiscMapEntry.setIndexNames(
    (0, "FS-BFD-MIB", "fsBfdSessDiscriminator"),
)
if mibBuilder.loadTexts:
    fsBfdSessDiscMapEntry.setStatus("current")
_FsBfdSessDiscMapIndex_Type = FSBfdSessIndexTC
_FsBfdSessDiscMapIndex_Object = MibTableColumn
fsBfdSessDiscMapIndex = _FsBfdSessDiscMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 4, 1, 1),
    _FsBfdSessDiscMapIndex_Type()
)
fsBfdSessDiscMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBfdSessDiscMapIndex.setStatus("current")
_FsBfdSessDiscMapStorageType_Type = StorageType
_FsBfdSessDiscMapStorageType_Object = MibTableColumn
fsBfdSessDiscMapStorageType = _FsBfdSessDiscMapStorageType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 4, 1, 2),
    _FsBfdSessDiscMapStorageType_Type()
)
fsBfdSessDiscMapStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsBfdSessDiscMapStorageType.setStatus("current")
_FsBfdSessDiscMapRowStatus_Type = RowStatus
_FsBfdSessDiscMapRowStatus_Object = MibTableColumn
fsBfdSessDiscMapRowStatus = _FsBfdSessDiscMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 4, 1, 3),
    _FsBfdSessDiscMapRowStatus_Type()
)
fsBfdSessDiscMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsBfdSessDiscMapRowStatus.setStatus("current")
_FsBfdSessIpMapTable_Object = MibTable
fsBfdSessIpMapTable = _FsBfdSessIpMapTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 5)
)
if mibBuilder.loadTexts:
    fsBfdSessIpMapTable.setStatus("current")
_FsBfdSessIpMapEntry_Object = MibTableRow
fsBfdSessIpMapEntry = _FsBfdSessIpMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 5, 1)
)
fsBfdSessIpMapEntry.setIndexNames(
    (0, "FS-BFD-MIB", "fsBfdSessInterface"),
    (0, "FS-BFD-MIB", "fsBfdSessSrcAddrType"),
    (0, "FS-BFD-MIB", "fsBfdSessSrcAddr"),
    (0, "FS-BFD-MIB", "fsBfdSessDstAddrType"),
    (0, "FS-BFD-MIB", "fsBfdSessDstAddr"),
)
if mibBuilder.loadTexts:
    fsBfdSessIpMapEntry.setStatus("current")
_FsBfdSessIpMapIndex_Type = FSBfdSessIndexTC
_FsBfdSessIpMapIndex_Object = MibTableColumn
fsBfdSessIpMapIndex = _FsBfdSessIpMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 5, 1, 1),
    _FsBfdSessIpMapIndex_Type()
)
fsBfdSessIpMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBfdSessIpMapIndex.setStatus("current")
_FsBfdSessIpMapStorageType_Type = StorageType
_FsBfdSessIpMapStorageType_Object = MibTableColumn
fsBfdSessIpMapStorageType = _FsBfdSessIpMapStorageType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 5, 1, 2),
    _FsBfdSessIpMapStorageType_Type()
)
fsBfdSessIpMapStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsBfdSessIpMapStorageType.setStatus("current")
_FsBfdSessIpMapRowStatus_Type = RowStatus
_FsBfdSessIpMapRowStatus_Object = MibTableColumn
fsBfdSessIpMapRowStatus = _FsBfdSessIpMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 5, 1, 3),
    _FsBfdSessIpMapRowStatus_Type()
)
fsBfdSessIpMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsBfdSessIpMapRowStatus.setStatus("current")
_FsBfdConformance_ObjectIdentity = ObjectIdentity
fsBfdConformance = _FsBfdConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 2)
)
_FsBfdGroups_ObjectIdentity = ObjectIdentity
fsBfdGroups = _FsBfdGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 2, 1)
)
_FsBfdCompliances_ObjectIdentity = ObjectIdentity
fsBfdCompliances = _FsBfdCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 2, 2)
)
fsBfdSessEntry.registerAugmentions(
    ("FS-BFD-MIB",
     "fsBfdSessPerfEntry")
)
fsBfdSessPerfEntry.setIndexNames(*fsBfdSessEntry.getIndexNames())

# Managed Objects groups

fsBfdSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 2, 1, 1)
)
fsBfdSessionGroup.setObjects(
      *(("FS-BFD-MIB", "fsBfdAdminStatus"),
        ("FS-BFD-MIB", "fsBfdSessNotificationsEnable"),
        ("FS-BFD-MIB", "fsBfdSessVersionNumber"),
        ("FS-BFD-MIB", "fsBfdSessType"),
        ("FS-BFD-MIB", "fsBfdSessDestinationUdpPort"),
        ("FS-BFD-MIB", "fsBfdSessSourceUdpPort"),
        ("FS-BFD-MIB", "fsBfdSessEchoSourceUdpPort"),
        ("FS-BFD-MIB", "fsBfdSessAdminStatus"),
        ("FS-BFD-MIB", "fsBfdSessOperMode"),
        ("FS-BFD-MIB", "fsBfdSessDemandModeDesiredFlag"),
        ("FS-BFD-MIB", "fsBfdSessControlPlaneIndepFlag"),
        ("FS-BFD-MIB", "fsBfdSessMultipointFlag"),
        ("FS-BFD-MIB", "fsBfdSessInterface"),
        ("FS-BFD-MIB", "fsBfdSessSrcAddrType"),
        ("FS-BFD-MIB", "fsBfdSessSrcAddr"),
        ("FS-BFD-MIB", "fsBfdSessDstAddrType"),
        ("FS-BFD-MIB", "fsBfdSessDstAddr"),
        ("FS-BFD-MIB", "fsBfdSessGTSM"),
        ("FS-BFD-MIB", "fsBfdSessGTSMTTL"),
        ("FS-BFD-MIB", "fsBfdSessDesiredMinTxInterval"),
        ("FS-BFD-MIB", "fsBfdSessReqMinRxInterval"),
        ("FS-BFD-MIB", "fsBfdSessReqMinEchoRxInterval"),
        ("FS-BFD-MIB", "fsBfdSessDetectMult"),
        ("FS-BFD-MIB", "fsBfdSessAuthPresFlag"),
        ("FS-BFD-MIB", "fsBfdSessAuthenticationType"),
        ("FS-BFD-MIB", "fsBfdSessAuthenticationKeyID"),
        ("FS-BFD-MIB", "fsBfdSessAuthenticationKey"),
        ("FS-BFD-MIB", "fsBfdSessStorageType"),
        ("FS-BFD-MIB", "fsBfdSessRowStatus"),
        ("FS-BFD-MIB", "fsBfdSessDiscMapStorageType"),
        ("FS-BFD-MIB", "fsBfdSessDiscMapRowStatus"),
        ("FS-BFD-MIB", "fsBfdSessIpMapStorageType"),
        ("FS-BFD-MIB", "fsBfdSessIpMapRowStatus"))
)
if mibBuilder.loadTexts:
    fsBfdSessionGroup.setStatus("current")

fsBfdSessionReadOnlyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 2, 1, 2)
)
fsBfdSessionReadOnlyGroup.setObjects(
      *(("FS-BFD-MIB", "fsBfdSessDiscriminator"),
        ("FS-BFD-MIB", "fsBfdSessRemoteDiscr"),
        ("FS-BFD-MIB", "fsBfdSessState"),
        ("FS-BFD-MIB", "fsBfdSessRemoteHeardFlag"),
        ("FS-BFD-MIB", "fsBfdSessDiag"),
        ("FS-BFD-MIB", "fsBfdSessNegotiatedInterval"),
        ("FS-BFD-MIB", "fsBfdSessNegotiatedEchoInterval"),
        ("FS-BFD-MIB", "fsBfdSessNegotiatedDetectMult"),
        ("FS-BFD-MIB", "fsBfdSessDiscMapIndex"),
        ("FS-BFD-MIB", "fsBfdSessIpMapIndex"))
)
if mibBuilder.loadTexts:
    fsBfdSessionReadOnlyGroup.setStatus("current")

fsBfdSessionPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 2, 1, 3)
)
fsBfdSessionPerfGroup.setObjects(
      *(("FS-BFD-MIB", "fsBfdSessPerfCtrlPktIn"),
        ("FS-BFD-MIB", "fsBfdSessPerfCtrlPktOut"),
        ("FS-BFD-MIB", "fsBfdSessPerfCtrlPktDrop"),
        ("FS-BFD-MIB", "fsBfdSessPerfCtrlPktDropLastTime"),
        ("FS-BFD-MIB", "fsBfdSessPerfEchoPktIn"),
        ("FS-BFD-MIB", "fsBfdSessPerfEchoPktOut"),
        ("FS-BFD-MIB", "fsBfdSessPerfEchoPktDrop"),
        ("FS-BFD-MIB", "fsBfdSessPerfEchoPktDropLastTime"),
        ("FS-BFD-MIB", "fsBfdSessUpTime"),
        ("FS-BFD-MIB", "fsBfdSessPerfLastSessDownTime"),
        ("FS-BFD-MIB", "fsBfdSessPerfLastCommLostDiag"),
        ("FS-BFD-MIB", "fsBfdSessPerfSessUpCount"),
        ("FS-BFD-MIB", "fsBfdSessPerfDiscTime"))
)
if mibBuilder.loadTexts:
    fsBfdSessionPerfGroup.setStatus("current")

fsBfdSessionPerfHCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 2, 1, 4)
)
fsBfdSessionPerfHCGroup.setObjects(
      *(("FS-BFD-MIB", "fsBfdSessPerfCtrlPktInHC"),
        ("FS-BFD-MIB", "fsBfdSessPerfCtrlPktOutHC"),
        ("FS-BFD-MIB", "fsBfdSessPerfCtrlPktDropHC"),
        ("FS-BFD-MIB", "fsBfdSessPerfEchoPktInHC"),
        ("FS-BFD-MIB", "fsBfdSessPerfEchoPktOutHC"),
        ("FS-BFD-MIB", "fsBfdSessPerfEchoPktDropHC"))
)
if mibBuilder.loadTexts:
    fsBfdSessionPerfHCGroup.setStatus("current")


# Notification objects

fsBfdSessUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 0, 1)
)
fsBfdSessUp.setObjects(
      *(("FS-BFD-MIB", "fsBfdSessDiag"),
        ("FS-BFD-MIB", "fsBfdSessDiag"),
        ("FS-BFD-MIB", "fsBfdSessInterface"),
        ("FS-BFD-MIB", "fsBfdSessIfName"),
        ("FS-BFD-MIB", "fsBfdSessIfDes"))
)
if mibBuilder.loadTexts:
    fsBfdSessUp.setStatus(
        "current"
    )

fsBfdSessDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 0, 2)
)
fsBfdSessDown.setObjects(
      *(("FS-BFD-MIB", "fsBfdSessDiag"),
        ("FS-BFD-MIB", "fsBfdSessDiag"),
        ("FS-BFD-MIB", "fsBfdSessInterface"),
        ("FS-BFD-MIB", "fsBfdSessIfName"),
        ("FS-BFD-MIB", "fsBfdSessIfDes"))
)
if mibBuilder.loadTexts:
    fsBfdSessDown.setStatus(
        "current"
    )


# Notifications groups

fsBfdNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 2, 1, 5)
)
fsBfdNotificationGroup.setObjects(
      *(("FS-BFD-MIB", "fsBfdSessUp"),
        ("FS-BFD-MIB", "fsBfdSessDown"))
)
if mibBuilder.loadTexts:
    fsBfdNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

fsBfdModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 2, 2, 1)
)
fsBfdModuleFullCompliance.setObjects(
      *(("FS-BFD-MIB", "fsBfdSessionGroup"),
        ("FS-BFD-MIB", "fsBfdSessionReadOnlyGroup"),
        ("FS-BFD-MIB", "fsBfdSessionPerfGroup"),
        ("FS-BFD-MIB", "fsBfdNotificationGroup"),
        ("FS-BFD-MIB", "fsBfdSessionPerfHCGroup"))
)
if mibBuilder.loadTexts:
    fsBfdModuleFullCompliance.setStatus(
        "current"
    )

fsBfdModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 2, 2, 2)
)
fsBfdModuleReadOnlyCompliance.setObjects(
      *(("FS-BFD-MIB", "fsBfdSessionGroup"),
        ("FS-BFD-MIB", "fsBfdSessionReadOnlyGroup"),
        ("FS-BFD-MIB", "fsBfdSessionPerfGroup"),
        ("FS-BFD-MIB", "fsBfdNotificationGroup"),
        ("FS-BFD-MIB", "fsBfdSessionPerfHCGroup"))
)
if mibBuilder.loadTexts:
    fsBfdModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-BFD-MIB",
    **{"FSBfdSessIndexTC": FSBfdSessIndexTC,
       "FSBfdIntervalTC": FSBfdIntervalTC,
       "FSBfdMultiplierTC": FSBfdMultiplierTC,
       "FSBfdDiagTC": FSBfdDiagTC,
       "FSBfdSessTypeTC": FSBfdSessTypeTC,
       "FSBfdSessOperModeTC": FSBfdSessOperModeTC,
       "FSBfdCtrlDestPortNumberTC": FSBfdCtrlDestPortNumberTC,
       "FSBfdCtrlSourcePortNumberTC": FSBfdCtrlSourcePortNumberTC,
       "FSBfdSessStateTC": FSBfdSessStateTC,
       "FSBfdSessAuthenticationTypeTC": FSBfdSessAuthenticationTypeTC,
       "FSBfdSessionAuthenticationKeyTC": FSBfdSessionAuthenticationKeyTC,
       "fsBfdMIB": fsBfdMIB,
       "fsBfdNotifications": fsBfdNotifications,
       "fsBfdSessUp": fsBfdSessUp,
       "fsBfdSessDown": fsBfdSessDown,
       "fsBfdObjects": fsBfdObjects,
       "fsBfdScalarObjects": fsBfdScalarObjects,
       "fsBfdAdminStatus": fsBfdAdminStatus,
       "fsBfdSessNotificationsEnable": fsBfdSessNotificationsEnable,
       "fsBfdSessTable": fsBfdSessTable,
       "fsBfdSessEntry": fsBfdSessEntry,
       "fsBfdSessIndex": fsBfdSessIndex,
       "fsBfdSessVersionNumber": fsBfdSessVersionNumber,
       "fsBfdSessType": fsBfdSessType,
       "fsBfdSessDiscriminator": fsBfdSessDiscriminator,
       "fsBfdSessRemoteDiscr": fsBfdSessRemoteDiscr,
       "fsBfdSessDestinationUdpPort": fsBfdSessDestinationUdpPort,
       "fsBfdSessSourceUdpPort": fsBfdSessSourceUdpPort,
       "fsBfdSessEchoSourceUdpPort": fsBfdSessEchoSourceUdpPort,
       "fsBfdSessAdminStatus": fsBfdSessAdminStatus,
       "fsBfdSessState": fsBfdSessState,
       "fsBfdSessRemoteHeardFlag": fsBfdSessRemoteHeardFlag,
       "fsBfdSessDiag": fsBfdSessDiag,
       "fsBfdSessOperMode": fsBfdSessOperMode,
       "fsBfdSessDemandModeDesiredFlag": fsBfdSessDemandModeDesiredFlag,
       "fsBfdSessControlPlaneIndepFlag": fsBfdSessControlPlaneIndepFlag,
       "fsBfdSessMultipointFlag": fsBfdSessMultipointFlag,
       "fsBfdSessInterface": fsBfdSessInterface,
       "fsBfdSessSrcAddrType": fsBfdSessSrcAddrType,
       "fsBfdSessSrcAddr": fsBfdSessSrcAddr,
       "fsBfdSessDstAddrType": fsBfdSessDstAddrType,
       "fsBfdSessDstAddr": fsBfdSessDstAddr,
       "fsBfdSessGTSM": fsBfdSessGTSM,
       "fsBfdSessGTSMTTL": fsBfdSessGTSMTTL,
       "fsBfdSessDesiredMinTxInterval": fsBfdSessDesiredMinTxInterval,
       "fsBfdSessReqMinRxInterval": fsBfdSessReqMinRxInterval,
       "fsBfdSessReqMinEchoRxInterval": fsBfdSessReqMinEchoRxInterval,
       "fsBfdSessDetectMult": fsBfdSessDetectMult,
       "fsBfdSessNegotiatedInterval": fsBfdSessNegotiatedInterval,
       "fsBfdSessNegotiatedEchoInterval": fsBfdSessNegotiatedEchoInterval,
       "fsBfdSessNegotiatedDetectMult": fsBfdSessNegotiatedDetectMult,
       "fsBfdSessAuthPresFlag": fsBfdSessAuthPresFlag,
       "fsBfdSessAuthenticationType": fsBfdSessAuthenticationType,
       "fsBfdSessAuthenticationKeyID": fsBfdSessAuthenticationKeyID,
       "fsBfdSessAuthenticationKey": fsBfdSessAuthenticationKey,
       "fsBfdSessStorageType": fsBfdSessStorageType,
       "fsBfdSessRowStatus": fsBfdSessRowStatus,
       "fsBfdSessIfName": fsBfdSessIfName,
       "fsBfdSessIfDes": fsBfdSessIfDes,
       "fsBfdSessPerfTable": fsBfdSessPerfTable,
       "fsBfdSessPerfEntry": fsBfdSessPerfEntry,
       "fsBfdSessPerfCtrlPktIn": fsBfdSessPerfCtrlPktIn,
       "fsBfdSessPerfCtrlPktOut": fsBfdSessPerfCtrlPktOut,
       "fsBfdSessPerfCtrlPktDrop": fsBfdSessPerfCtrlPktDrop,
       "fsBfdSessPerfCtrlPktDropLastTime": fsBfdSessPerfCtrlPktDropLastTime,
       "fsBfdSessPerfEchoPktIn": fsBfdSessPerfEchoPktIn,
       "fsBfdSessPerfEchoPktOut": fsBfdSessPerfEchoPktOut,
       "fsBfdSessPerfEchoPktDrop": fsBfdSessPerfEchoPktDrop,
       "fsBfdSessPerfEchoPktDropLastTime": fsBfdSessPerfEchoPktDropLastTime,
       "fsBfdSessUpTime": fsBfdSessUpTime,
       "fsBfdSessPerfLastSessDownTime": fsBfdSessPerfLastSessDownTime,
       "fsBfdSessPerfLastCommLostDiag": fsBfdSessPerfLastCommLostDiag,
       "fsBfdSessPerfSessUpCount": fsBfdSessPerfSessUpCount,
       "fsBfdSessPerfDiscTime": fsBfdSessPerfDiscTime,
       "fsBfdSessPerfCtrlPktInHC": fsBfdSessPerfCtrlPktInHC,
       "fsBfdSessPerfCtrlPktOutHC": fsBfdSessPerfCtrlPktOutHC,
       "fsBfdSessPerfCtrlPktDropHC": fsBfdSessPerfCtrlPktDropHC,
       "fsBfdSessPerfEchoPktInHC": fsBfdSessPerfEchoPktInHC,
       "fsBfdSessPerfEchoPktOutHC": fsBfdSessPerfEchoPktOutHC,
       "fsBfdSessPerfEchoPktDropHC": fsBfdSessPerfEchoPktDropHC,
       "fsBfdSessDiscMapTable": fsBfdSessDiscMapTable,
       "fsBfdSessDiscMapEntry": fsBfdSessDiscMapEntry,
       "fsBfdSessDiscMapIndex": fsBfdSessDiscMapIndex,
       "fsBfdSessDiscMapStorageType": fsBfdSessDiscMapStorageType,
       "fsBfdSessDiscMapRowStatus": fsBfdSessDiscMapRowStatus,
       "fsBfdSessIpMapTable": fsBfdSessIpMapTable,
       "fsBfdSessIpMapEntry": fsBfdSessIpMapEntry,
       "fsBfdSessIpMapIndex": fsBfdSessIpMapIndex,
       "fsBfdSessIpMapStorageType": fsBfdSessIpMapStorageType,
       "fsBfdSessIpMapRowStatus": fsBfdSessIpMapRowStatus,
       "fsBfdConformance": fsBfdConformance,
       "fsBfdGroups": fsBfdGroups,
       "fsBfdSessionGroup": fsBfdSessionGroup,
       "fsBfdSessionReadOnlyGroup": fsBfdSessionReadOnlyGroup,
       "fsBfdSessionPerfGroup": fsBfdSessionPerfGroup,
       "fsBfdSessionPerfHCGroup": fsBfdSessionPerfHCGroup,
       "fsBfdNotificationGroup": fsBfdNotificationGroup,
       "fsBfdCompliances": fsBfdCompliances,
       "fsBfdModuleFullCompliance": fsBfdModuleFullCompliance,
       "fsBfdModuleReadOnlyCompliance": fsBfdModuleReadOnlyCompliance}
)
