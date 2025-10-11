# SNMP MIB module (QTECH-BFD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-BFD-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:08 2025
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

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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

qtechBfdMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48)
)
if mibBuilder.loadTexts:
    qtechBfdMIB.setRevisions(
        ("2012-04-14 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class QtechBfdSessIndexTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class QtechBfdIntervalTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class QtechBfdMultiplierTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class QtechBfdDiagTC(TextualConvention, Integer32):
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



class QtechBfdSessTypeTC(TextualConvention, Integer32):
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



class QtechBfdSessOperModeTC(TextualConvention, Integer32):
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



class QtechBfdCtrlDestPortNumberTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class QtechBfdCtrlSourcePortNumberTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class QtechBfdSessStateTC(TextualConvention, Integer32):
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



class QtechBfdSessAuthenticationTypeTC(TextualConvention, Integer32):
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



class QtechBfdSessionAuthenticationKeyTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x "
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 252),
    )



# MIB Managed Objects in the order of their OIDs

_QtechBfdNotifications_ObjectIdentity = ObjectIdentity
qtechBfdNotifications = _QtechBfdNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 0)
)
_QtechBfdObjects_ObjectIdentity = ObjectIdentity
qtechBfdObjects = _QtechBfdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1)
)
_QtechBfdScalarObjects_ObjectIdentity = ObjectIdentity
qtechBfdScalarObjects = _QtechBfdScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 1)
)


class _QtechBfdAdminStatus_Type(Integer32):
    """Custom type qtechBfdAdminStatus based on Integer32"""
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


_QtechBfdAdminStatus_Type.__name__ = "Integer32"
_QtechBfdAdminStatus_Object = MibScalar
qtechBfdAdminStatus = _QtechBfdAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 1, 1),
    _QtechBfdAdminStatus_Type()
)
qtechBfdAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechBfdAdminStatus.setStatus("current")


class _QtechBfdSessNotificationsEnable_Type(TruthValue):
    """Custom type qtechBfdSessNotificationsEnable based on TruthValue"""
    defaultValue = 2


_QtechBfdSessNotificationsEnable_Type.__name__ = "TruthValue"
_QtechBfdSessNotificationsEnable_Object = MibScalar
qtechBfdSessNotificationsEnable = _QtechBfdSessNotificationsEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 1, 2),
    _QtechBfdSessNotificationsEnable_Type()
)
qtechBfdSessNotificationsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechBfdSessNotificationsEnable.setStatus("current")
_QtechBfdSessTable_Object = MibTable
qtechBfdSessTable = _QtechBfdSessTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2)
)
if mibBuilder.loadTexts:
    qtechBfdSessTable.setStatus("current")
_QtechBfdSessEntry_Object = MibTableRow
qtechBfdSessEntry = _QtechBfdSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1)
)
qtechBfdSessEntry.setIndexNames(
    (0, "QTECH-BFD-MIB", "qtechBfdSessIndex"),
)
if mibBuilder.loadTexts:
    qtechBfdSessEntry.setStatus("current")
_QtechBfdSessIndex_Type = QtechBfdSessIndexTC
_QtechBfdSessIndex_Object = MibTableColumn
qtechBfdSessIndex = _QtechBfdSessIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 1),
    _QtechBfdSessIndex_Type()
)
qtechBfdSessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechBfdSessIndex.setStatus("current")


class _QtechBfdSessVersionNumber_Type(Unsigned32):
    """Custom type qtechBfdSessVersionNumber based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QtechBfdSessVersionNumber_Type.__name__ = "Unsigned32"
_QtechBfdSessVersionNumber_Object = MibTableColumn
qtechBfdSessVersionNumber = _QtechBfdSessVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 2),
    _QtechBfdSessVersionNumber_Type()
)
qtechBfdSessVersionNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechBfdSessVersionNumber.setStatus("current")
_QtechBfdSessType_Type = QtechBfdSessTypeTC
_QtechBfdSessType_Object = MibTableColumn
qtechBfdSessType = _QtechBfdSessType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 3),
    _QtechBfdSessType_Type()
)
qtechBfdSessType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechBfdSessType.setStatus("current")


class _QtechBfdSessDiscriminator_Type(Unsigned32):
    """Custom type qtechBfdSessDiscriminator based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_QtechBfdSessDiscriminator_Type.__name__ = "Unsigned32"
_QtechBfdSessDiscriminator_Object = MibTableColumn
qtechBfdSessDiscriminator = _QtechBfdSessDiscriminator_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 4),
    _QtechBfdSessDiscriminator_Type()
)
qtechBfdSessDiscriminator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBfdSessDiscriminator.setStatus("current")


class _QtechBfdSessRemoteDiscr_Type(Unsigned32):
    """Custom type qtechBfdSessRemoteDiscr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_QtechBfdSessRemoteDiscr_Type.__name__ = "Unsigned32"
_QtechBfdSessRemoteDiscr_Object = MibTableColumn
qtechBfdSessRemoteDiscr = _QtechBfdSessRemoteDiscr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 5),
    _QtechBfdSessRemoteDiscr_Type()
)
qtechBfdSessRemoteDiscr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBfdSessRemoteDiscr.setStatus("current")


class _QtechBfdSessDestinationUdpPort_Type(QtechBfdCtrlDestPortNumberTC):
    """Custom type qtechBfdSessDestinationUdpPort based on QtechBfdCtrlDestPortNumberTC"""
    defaultValue = 0


_QtechBfdSessDestinationUdpPort_Type.__name__ = "QtechBfdCtrlDestPortNumberTC"
_QtechBfdSessDestinationUdpPort_Object = MibTableColumn
qtechBfdSessDestinationUdpPort = _QtechBfdSessDestinationUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 6),
    _QtechBfdSessDestinationUdpPort_Type()
)
qtechBfdSessDestinationUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechBfdSessDestinationUdpPort.setStatus("current")


class _QtechBfdSessSourceUdpPort_Type(QtechBfdCtrlSourcePortNumberTC):
    """Custom type qtechBfdSessSourceUdpPort based on QtechBfdCtrlSourcePortNumberTC"""
    defaultValue = 0


_QtechBfdSessSourceUdpPort_Type.__name__ = "QtechBfdCtrlSourcePortNumberTC"
_QtechBfdSessSourceUdpPort_Object = MibTableColumn
qtechBfdSessSourceUdpPort = _QtechBfdSessSourceUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 7),
    _QtechBfdSessSourceUdpPort_Type()
)
qtechBfdSessSourceUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechBfdSessSourceUdpPort.setStatus("current")


class _QtechBfdSessEchoSourceUdpPort_Type(InetPortNumber):
    """Custom type qtechBfdSessEchoSourceUdpPort based on InetPortNumber"""
    defaultValue = 0


_QtechBfdSessEchoSourceUdpPort_Type.__name__ = "InetPortNumber"
_QtechBfdSessEchoSourceUdpPort_Object = MibTableColumn
qtechBfdSessEchoSourceUdpPort = _QtechBfdSessEchoSourceUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 8),
    _QtechBfdSessEchoSourceUdpPort_Type()
)
qtechBfdSessEchoSourceUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechBfdSessEchoSourceUdpPort.setStatus("current")


class _QtechBfdSessAdminStatus_Type(Integer32):
    """Custom type qtechBfdSessAdminStatus based on Integer32"""
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


_QtechBfdSessAdminStatus_Type.__name__ = "Integer32"
_QtechBfdSessAdminStatus_Object = MibTableColumn
qtechBfdSessAdminStatus = _QtechBfdSessAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 9),
    _QtechBfdSessAdminStatus_Type()
)
qtechBfdSessAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechBfdSessAdminStatus.setStatus("current")


class _QtechBfdSessState_Type(QtechBfdSessStateTC):
    """Custom type qtechBfdSessState based on QtechBfdSessStateTC"""
    defaultValue = 2


_QtechBfdSessState_Type.__name__ = "QtechBfdSessStateTC"
_QtechBfdSessState_Object = MibTableColumn
qtechBfdSessState = _QtechBfdSessState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 10),
    _QtechBfdSessState_Type()
)
qtechBfdSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBfdSessState.setStatus("current")


class _QtechBfdSessRemoteHeardFlag_Type(TruthValue):
    """Custom type qtechBfdSessRemoteHeardFlag based on TruthValue"""
    defaultValue = 2


_QtechBfdSessRemoteHeardFlag_Type.__name__ = "TruthValue"
_QtechBfdSessRemoteHeardFlag_Object = MibTableColumn
qtechBfdSessRemoteHeardFlag = _QtechBfdSessRemoteHeardFlag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 11),
    _QtechBfdSessRemoteHeardFlag_Type()
)
qtechBfdSessRemoteHeardFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBfdSessRemoteHeardFlag.setStatus("current")
_QtechBfdSessDiag_Type = QtechBfdDiagTC
_QtechBfdSessDiag_Object = MibTableColumn
qtechBfdSessDiag = _QtechBfdSessDiag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 12),
    _QtechBfdSessDiag_Type()
)
qtechBfdSessDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBfdSessDiag.setStatus("current")
_QtechBfdSessOperMode_Type = QtechBfdSessOperModeTC
_QtechBfdSessOperMode_Object = MibTableColumn
qtechBfdSessOperMode = _QtechBfdSessOperMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 13),
    _QtechBfdSessOperMode_Type()
)
qtechBfdSessOperMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechBfdSessOperMode.setStatus("current")


class _QtechBfdSessDemandModeDesiredFlag_Type(TruthValue):
    """Custom type qtechBfdSessDemandModeDesiredFlag based on TruthValue"""
    defaultValue = 2


_QtechBfdSessDemandModeDesiredFlag_Type.__name__ = "TruthValue"
_QtechBfdSessDemandModeDesiredFlag_Object = MibTableColumn
qtechBfdSessDemandModeDesiredFlag = _QtechBfdSessDemandModeDesiredFlag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 14),
    _QtechBfdSessDemandModeDesiredFlag_Type()
)
qtechBfdSessDemandModeDesiredFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechBfdSessDemandModeDesiredFlag.setStatus("current")


class _QtechBfdSessControlPlaneIndepFlag_Type(TruthValue):
    """Custom type qtechBfdSessControlPlaneIndepFlag based on TruthValue"""
    defaultValue = 2


_QtechBfdSessControlPlaneIndepFlag_Type.__name__ = "TruthValue"
_QtechBfdSessControlPlaneIndepFlag_Object = MibTableColumn
qtechBfdSessControlPlaneIndepFlag = _QtechBfdSessControlPlaneIndepFlag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 15),
    _QtechBfdSessControlPlaneIndepFlag_Type()
)
qtechBfdSessControlPlaneIndepFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechBfdSessControlPlaneIndepFlag.setStatus("current")


class _QtechBfdSessMultipointFlag_Type(TruthValue):
    """Custom type qtechBfdSessMultipointFlag based on TruthValue"""
    defaultValue = 2


_QtechBfdSessMultipointFlag_Type.__name__ = "TruthValue"
_QtechBfdSessMultipointFlag_Object = MibTableColumn
qtechBfdSessMultipointFlag = _QtechBfdSessMultipointFlag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 16),
    _QtechBfdSessMultipointFlag_Type()
)
qtechBfdSessMultipointFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechBfdSessMultipointFlag.setStatus("current")
_QtechBfdSessInterface_Type = InterfaceIndexOrZero
_QtechBfdSessInterface_Object = MibTableColumn
qtechBfdSessInterface = _QtechBfdSessInterface_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 17),
    _QtechBfdSessInterface_Type()
)
qtechBfdSessInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechBfdSessInterface.setStatus("current")
_QtechBfdSessSrcAddrType_Type = InetAddressType
_QtechBfdSessSrcAddrType_Object = MibTableColumn
qtechBfdSessSrcAddrType = _QtechBfdSessSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 18),
    _QtechBfdSessSrcAddrType_Type()
)
qtechBfdSessSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechBfdSessSrcAddrType.setStatus("current")
_QtechBfdSessSrcAddr_Type = InetAddress
_QtechBfdSessSrcAddr_Object = MibTableColumn
qtechBfdSessSrcAddr = _QtechBfdSessSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 19),
    _QtechBfdSessSrcAddr_Type()
)
qtechBfdSessSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechBfdSessSrcAddr.setStatus("current")
_QtechBfdSessDstAddrType_Type = InetAddressType
_QtechBfdSessDstAddrType_Object = MibTableColumn
qtechBfdSessDstAddrType = _QtechBfdSessDstAddrType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 20),
    _QtechBfdSessDstAddrType_Type()
)
qtechBfdSessDstAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechBfdSessDstAddrType.setStatus("current")
_QtechBfdSessDstAddr_Type = InetAddress
_QtechBfdSessDstAddr_Object = MibTableColumn
qtechBfdSessDstAddr = _QtechBfdSessDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 21),
    _QtechBfdSessDstAddr_Type()
)
qtechBfdSessDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechBfdSessDstAddr.setStatus("current")


class _QtechBfdSessGTSM_Type(TruthValue):
    """Custom type qtechBfdSessGTSM based on TruthValue"""
    defaultValue = 2


_QtechBfdSessGTSM_Type.__name__ = "TruthValue"
_QtechBfdSessGTSM_Object = MibTableColumn
qtechBfdSessGTSM = _QtechBfdSessGTSM_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 22),
    _QtechBfdSessGTSM_Type()
)
qtechBfdSessGTSM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechBfdSessGTSM.setStatus("current")


class _QtechBfdSessGTSMTTL_Type(Unsigned32):
    """Custom type qtechBfdSessGTSMTTL based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QtechBfdSessGTSMTTL_Type.__name__ = "Unsigned32"
_QtechBfdSessGTSMTTL_Object = MibTableColumn
qtechBfdSessGTSMTTL = _QtechBfdSessGTSMTTL_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 23),
    _QtechBfdSessGTSMTTL_Type()
)
qtechBfdSessGTSMTTL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechBfdSessGTSMTTL.setStatus("current")
_QtechBfdSessDesiredMinTxInterval_Type = QtechBfdIntervalTC
_QtechBfdSessDesiredMinTxInterval_Object = MibTableColumn
qtechBfdSessDesiredMinTxInterval = _QtechBfdSessDesiredMinTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 24),
    _QtechBfdSessDesiredMinTxInterval_Type()
)
qtechBfdSessDesiredMinTxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechBfdSessDesiredMinTxInterval.setStatus("current")
_QtechBfdSessReqMinRxInterval_Type = QtechBfdIntervalTC
_QtechBfdSessReqMinRxInterval_Object = MibTableColumn
qtechBfdSessReqMinRxInterval = _QtechBfdSessReqMinRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 25),
    _QtechBfdSessReqMinRxInterval_Type()
)
qtechBfdSessReqMinRxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechBfdSessReqMinRxInterval.setStatus("current")
_QtechBfdSessReqMinEchoRxInterval_Type = QtechBfdIntervalTC
_QtechBfdSessReqMinEchoRxInterval_Object = MibTableColumn
qtechBfdSessReqMinEchoRxInterval = _QtechBfdSessReqMinEchoRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 26),
    _QtechBfdSessReqMinEchoRxInterval_Type()
)
qtechBfdSessReqMinEchoRxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechBfdSessReqMinEchoRxInterval.setStatus("current")
_QtechBfdSessDetectMult_Type = QtechBfdMultiplierTC
_QtechBfdSessDetectMult_Object = MibTableColumn
qtechBfdSessDetectMult = _QtechBfdSessDetectMult_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 27),
    _QtechBfdSessDetectMult_Type()
)
qtechBfdSessDetectMult.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechBfdSessDetectMult.setStatus("current")
_QtechBfdSessNegotiatedInterval_Type = QtechBfdIntervalTC
_QtechBfdSessNegotiatedInterval_Object = MibTableColumn
qtechBfdSessNegotiatedInterval = _QtechBfdSessNegotiatedInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 28),
    _QtechBfdSessNegotiatedInterval_Type()
)
qtechBfdSessNegotiatedInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBfdSessNegotiatedInterval.setStatus("current")
_QtechBfdSessNegotiatedEchoInterval_Type = QtechBfdIntervalTC
_QtechBfdSessNegotiatedEchoInterval_Object = MibTableColumn
qtechBfdSessNegotiatedEchoInterval = _QtechBfdSessNegotiatedEchoInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 29),
    _QtechBfdSessNegotiatedEchoInterval_Type()
)
qtechBfdSessNegotiatedEchoInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBfdSessNegotiatedEchoInterval.setStatus("current")
_QtechBfdSessNegotiatedDetectMult_Type = QtechBfdMultiplierTC
_QtechBfdSessNegotiatedDetectMult_Object = MibTableColumn
qtechBfdSessNegotiatedDetectMult = _QtechBfdSessNegotiatedDetectMult_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 30),
    _QtechBfdSessNegotiatedDetectMult_Type()
)
qtechBfdSessNegotiatedDetectMult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBfdSessNegotiatedDetectMult.setStatus("current")


class _QtechBfdSessAuthPresFlag_Type(TruthValue):
    """Custom type qtechBfdSessAuthPresFlag based on TruthValue"""
    defaultValue = 2


_QtechBfdSessAuthPresFlag_Type.__name__ = "TruthValue"
_QtechBfdSessAuthPresFlag_Object = MibTableColumn
qtechBfdSessAuthPresFlag = _QtechBfdSessAuthPresFlag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 31),
    _QtechBfdSessAuthPresFlag_Type()
)
qtechBfdSessAuthPresFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechBfdSessAuthPresFlag.setStatus("current")


class _QtechBfdSessAuthenticationType_Type(QtechBfdSessAuthenticationTypeTC):
    """Custom type qtechBfdSessAuthenticationType based on QtechBfdSessAuthenticationTypeTC"""
    defaultValue = -1


_QtechBfdSessAuthenticationType_Type.__name__ = "QtechBfdSessAuthenticationTypeTC"
_QtechBfdSessAuthenticationType_Object = MibTableColumn
qtechBfdSessAuthenticationType = _QtechBfdSessAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 32),
    _QtechBfdSessAuthenticationType_Type()
)
qtechBfdSessAuthenticationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechBfdSessAuthenticationType.setStatus("current")


class _QtechBfdSessAuthenticationKeyID_Type(Integer32):
    """Custom type qtechBfdSessAuthenticationKeyID based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_QtechBfdSessAuthenticationKeyID_Type.__name__ = "Integer32"
_QtechBfdSessAuthenticationKeyID_Object = MibTableColumn
qtechBfdSessAuthenticationKeyID = _QtechBfdSessAuthenticationKeyID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 33),
    _QtechBfdSessAuthenticationKeyID_Type()
)
qtechBfdSessAuthenticationKeyID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechBfdSessAuthenticationKeyID.setStatus("current")
_QtechBfdSessAuthenticationKey_Type = QtechBfdSessionAuthenticationKeyTC
_QtechBfdSessAuthenticationKey_Object = MibTableColumn
qtechBfdSessAuthenticationKey = _QtechBfdSessAuthenticationKey_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 34),
    _QtechBfdSessAuthenticationKey_Type()
)
qtechBfdSessAuthenticationKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechBfdSessAuthenticationKey.setStatus("current")
_QtechBfdSessStorageType_Type = StorageType
_QtechBfdSessStorageType_Object = MibTableColumn
qtechBfdSessStorageType = _QtechBfdSessStorageType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 35),
    _QtechBfdSessStorageType_Type()
)
qtechBfdSessStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechBfdSessStorageType.setStatus("current")
_QtechBfdSessRowStatus_Type = RowStatus
_QtechBfdSessRowStatus_Object = MibTableColumn
qtechBfdSessRowStatus = _QtechBfdSessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 36),
    _QtechBfdSessRowStatus_Type()
)
qtechBfdSessRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechBfdSessRowStatus.setStatus("current")
_QtechBfdSessPerfTable_Object = MibTable
qtechBfdSessPerfTable = _QtechBfdSessPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3)
)
if mibBuilder.loadTexts:
    qtechBfdSessPerfTable.setStatus("current")
_QtechBfdSessPerfEntry_Object = MibTableRow
qtechBfdSessPerfEntry = _QtechBfdSessPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3, 1)
)
if mibBuilder.loadTexts:
    qtechBfdSessPerfEntry.setStatus("current")
_QtechBfdSessPerfCtrlPktIn_Type = Counter32
_QtechBfdSessPerfCtrlPktIn_Object = MibTableColumn
qtechBfdSessPerfCtrlPktIn = _QtechBfdSessPerfCtrlPktIn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3, 1, 1),
    _QtechBfdSessPerfCtrlPktIn_Type()
)
qtechBfdSessPerfCtrlPktIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBfdSessPerfCtrlPktIn.setStatus("current")
_QtechBfdSessPerfCtrlPktOut_Type = Counter32
_QtechBfdSessPerfCtrlPktOut_Object = MibTableColumn
qtechBfdSessPerfCtrlPktOut = _QtechBfdSessPerfCtrlPktOut_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3, 1, 2),
    _QtechBfdSessPerfCtrlPktOut_Type()
)
qtechBfdSessPerfCtrlPktOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBfdSessPerfCtrlPktOut.setStatus("current")
_QtechBfdSessPerfCtrlPktDrop_Type = Counter32
_QtechBfdSessPerfCtrlPktDrop_Object = MibTableColumn
qtechBfdSessPerfCtrlPktDrop = _QtechBfdSessPerfCtrlPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3, 1, 3),
    _QtechBfdSessPerfCtrlPktDrop_Type()
)
qtechBfdSessPerfCtrlPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBfdSessPerfCtrlPktDrop.setStatus("current")
_QtechBfdSessPerfCtrlPktDropLastTime_Type = TimeStamp
_QtechBfdSessPerfCtrlPktDropLastTime_Object = MibTableColumn
qtechBfdSessPerfCtrlPktDropLastTime = _QtechBfdSessPerfCtrlPktDropLastTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3, 1, 4),
    _QtechBfdSessPerfCtrlPktDropLastTime_Type()
)
qtechBfdSessPerfCtrlPktDropLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBfdSessPerfCtrlPktDropLastTime.setStatus("current")
_QtechBfdSessPerfEchoPktIn_Type = Counter32
_QtechBfdSessPerfEchoPktIn_Object = MibTableColumn
qtechBfdSessPerfEchoPktIn = _QtechBfdSessPerfEchoPktIn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3, 1, 5),
    _QtechBfdSessPerfEchoPktIn_Type()
)
qtechBfdSessPerfEchoPktIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBfdSessPerfEchoPktIn.setStatus("current")
_QtechBfdSessPerfEchoPktOut_Type = Counter32
_QtechBfdSessPerfEchoPktOut_Object = MibTableColumn
qtechBfdSessPerfEchoPktOut = _QtechBfdSessPerfEchoPktOut_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3, 1, 6),
    _QtechBfdSessPerfEchoPktOut_Type()
)
qtechBfdSessPerfEchoPktOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBfdSessPerfEchoPktOut.setStatus("current")
_QtechBfdSessPerfEchoPktDrop_Type = Counter32
_QtechBfdSessPerfEchoPktDrop_Object = MibTableColumn
qtechBfdSessPerfEchoPktDrop = _QtechBfdSessPerfEchoPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3, 1, 7),
    _QtechBfdSessPerfEchoPktDrop_Type()
)
qtechBfdSessPerfEchoPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBfdSessPerfEchoPktDrop.setStatus("current")
_QtechBfdSessPerfEchoPktDropLastTime_Type = TimeStamp
_QtechBfdSessPerfEchoPktDropLastTime_Object = MibTableColumn
qtechBfdSessPerfEchoPktDropLastTime = _QtechBfdSessPerfEchoPktDropLastTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3, 1, 8),
    _QtechBfdSessPerfEchoPktDropLastTime_Type()
)
qtechBfdSessPerfEchoPktDropLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBfdSessPerfEchoPktDropLastTime.setStatus("current")
_QtechBfdSessUpTime_Type = TimeStamp
_QtechBfdSessUpTime_Object = MibTableColumn
qtechBfdSessUpTime = _QtechBfdSessUpTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3, 1, 9),
    _QtechBfdSessUpTime_Type()
)
qtechBfdSessUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBfdSessUpTime.setStatus("current")
_QtechBfdSessPerfLastSessDownTime_Type = TimeStamp
_QtechBfdSessPerfLastSessDownTime_Object = MibTableColumn
qtechBfdSessPerfLastSessDownTime = _QtechBfdSessPerfLastSessDownTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3, 1, 10),
    _QtechBfdSessPerfLastSessDownTime_Type()
)
qtechBfdSessPerfLastSessDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBfdSessPerfLastSessDownTime.setStatus("current")
_QtechBfdSessPerfLastCommLostDiag_Type = QtechBfdDiagTC
_QtechBfdSessPerfLastCommLostDiag_Object = MibTableColumn
qtechBfdSessPerfLastCommLostDiag = _QtechBfdSessPerfLastCommLostDiag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3, 1, 11),
    _QtechBfdSessPerfLastCommLostDiag_Type()
)
qtechBfdSessPerfLastCommLostDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBfdSessPerfLastCommLostDiag.setStatus("current")
_QtechBfdSessPerfSessUpCount_Type = Counter32
_QtechBfdSessPerfSessUpCount_Object = MibTableColumn
qtechBfdSessPerfSessUpCount = _QtechBfdSessPerfSessUpCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3, 1, 12),
    _QtechBfdSessPerfSessUpCount_Type()
)
qtechBfdSessPerfSessUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBfdSessPerfSessUpCount.setStatus("current")
_QtechBfdSessPerfDiscTime_Type = TimeStamp
_QtechBfdSessPerfDiscTime_Object = MibTableColumn
qtechBfdSessPerfDiscTime = _QtechBfdSessPerfDiscTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3, 1, 13),
    _QtechBfdSessPerfDiscTime_Type()
)
qtechBfdSessPerfDiscTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBfdSessPerfDiscTime.setStatus("current")
_QtechBfdSessPerfCtrlPktInHC_Type = Counter64
_QtechBfdSessPerfCtrlPktInHC_Object = MibTableColumn
qtechBfdSessPerfCtrlPktInHC = _QtechBfdSessPerfCtrlPktInHC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3, 1, 14),
    _QtechBfdSessPerfCtrlPktInHC_Type()
)
qtechBfdSessPerfCtrlPktInHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBfdSessPerfCtrlPktInHC.setStatus("current")
_QtechBfdSessPerfCtrlPktOutHC_Type = Counter64
_QtechBfdSessPerfCtrlPktOutHC_Object = MibTableColumn
qtechBfdSessPerfCtrlPktOutHC = _QtechBfdSessPerfCtrlPktOutHC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3, 1, 15),
    _QtechBfdSessPerfCtrlPktOutHC_Type()
)
qtechBfdSessPerfCtrlPktOutHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBfdSessPerfCtrlPktOutHC.setStatus("current")
_QtechBfdSessPerfCtrlPktDropHC_Type = Counter64
_QtechBfdSessPerfCtrlPktDropHC_Object = MibTableColumn
qtechBfdSessPerfCtrlPktDropHC = _QtechBfdSessPerfCtrlPktDropHC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3, 1, 16),
    _QtechBfdSessPerfCtrlPktDropHC_Type()
)
qtechBfdSessPerfCtrlPktDropHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBfdSessPerfCtrlPktDropHC.setStatus("current")
_QtechBfdSessPerfEchoPktInHC_Type = Counter64
_QtechBfdSessPerfEchoPktInHC_Object = MibTableColumn
qtechBfdSessPerfEchoPktInHC = _QtechBfdSessPerfEchoPktInHC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3, 1, 17),
    _QtechBfdSessPerfEchoPktInHC_Type()
)
qtechBfdSessPerfEchoPktInHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBfdSessPerfEchoPktInHC.setStatus("current")
_QtechBfdSessPerfEchoPktOutHC_Type = Counter64
_QtechBfdSessPerfEchoPktOutHC_Object = MibTableColumn
qtechBfdSessPerfEchoPktOutHC = _QtechBfdSessPerfEchoPktOutHC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3, 1, 18),
    _QtechBfdSessPerfEchoPktOutHC_Type()
)
qtechBfdSessPerfEchoPktOutHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBfdSessPerfEchoPktOutHC.setStatus("current")
_QtechBfdSessPerfEchoPktDropHC_Type = Counter64
_QtechBfdSessPerfEchoPktDropHC_Object = MibTableColumn
qtechBfdSessPerfEchoPktDropHC = _QtechBfdSessPerfEchoPktDropHC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3, 1, 19),
    _QtechBfdSessPerfEchoPktDropHC_Type()
)
qtechBfdSessPerfEchoPktDropHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBfdSessPerfEchoPktDropHC.setStatus("current")
_QtechBfdSessDiscMapTable_Object = MibTable
qtechBfdSessDiscMapTable = _QtechBfdSessDiscMapTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 4)
)
if mibBuilder.loadTexts:
    qtechBfdSessDiscMapTable.setStatus("current")
_QtechBfdSessDiscMapEntry_Object = MibTableRow
qtechBfdSessDiscMapEntry = _QtechBfdSessDiscMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 4, 1)
)
qtechBfdSessDiscMapEntry.setIndexNames(
    (0, "QTECH-BFD-MIB", "qtechBfdSessDiscriminator"),
)
if mibBuilder.loadTexts:
    qtechBfdSessDiscMapEntry.setStatus("current")
_QtechBfdSessDiscMapIndex_Type = QtechBfdSessIndexTC
_QtechBfdSessDiscMapIndex_Object = MibTableColumn
qtechBfdSessDiscMapIndex = _QtechBfdSessDiscMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 4, 1, 1),
    _QtechBfdSessDiscMapIndex_Type()
)
qtechBfdSessDiscMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBfdSessDiscMapIndex.setStatus("current")
_QtechBfdSessDiscMapStorageType_Type = StorageType
_QtechBfdSessDiscMapStorageType_Object = MibTableColumn
qtechBfdSessDiscMapStorageType = _QtechBfdSessDiscMapStorageType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 4, 1, 2),
    _QtechBfdSessDiscMapStorageType_Type()
)
qtechBfdSessDiscMapStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechBfdSessDiscMapStorageType.setStatus("current")
_QtechBfdSessDiscMapRowStatus_Type = RowStatus
_QtechBfdSessDiscMapRowStatus_Object = MibTableColumn
qtechBfdSessDiscMapRowStatus = _QtechBfdSessDiscMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 4, 1, 3),
    _QtechBfdSessDiscMapRowStatus_Type()
)
qtechBfdSessDiscMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechBfdSessDiscMapRowStatus.setStatus("current")
_QtechBfdSessIpMapTable_Object = MibTable
qtechBfdSessIpMapTable = _QtechBfdSessIpMapTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 5)
)
if mibBuilder.loadTexts:
    qtechBfdSessIpMapTable.setStatus("current")
_QtechBfdSessIpMapEntry_Object = MibTableRow
qtechBfdSessIpMapEntry = _QtechBfdSessIpMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 5, 1)
)
qtechBfdSessIpMapEntry.setIndexNames(
    (0, "QTECH-BFD-MIB", "qtechBfdSessInterface"),
    (0, "QTECH-BFD-MIB", "qtechBfdSessSrcAddrType"),
    (0, "QTECH-BFD-MIB", "qtechBfdSessSrcAddr"),
    (0, "QTECH-BFD-MIB", "qtechBfdSessDstAddrType"),
    (0, "QTECH-BFD-MIB", "qtechBfdSessDstAddr"),
)
if mibBuilder.loadTexts:
    qtechBfdSessIpMapEntry.setStatus("current")
_QtechBfdSessIpMapIndex_Type = QtechBfdSessIndexTC
_QtechBfdSessIpMapIndex_Object = MibTableColumn
qtechBfdSessIpMapIndex = _QtechBfdSessIpMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 5, 1, 1),
    _QtechBfdSessIpMapIndex_Type()
)
qtechBfdSessIpMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBfdSessIpMapIndex.setStatus("current")
_QtechBfdSessIpMapStorageType_Type = StorageType
_QtechBfdSessIpMapStorageType_Object = MibTableColumn
qtechBfdSessIpMapStorageType = _QtechBfdSessIpMapStorageType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 5, 1, 2),
    _QtechBfdSessIpMapStorageType_Type()
)
qtechBfdSessIpMapStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechBfdSessIpMapStorageType.setStatus("current")
_QtechBfdSessIpMapRowStatus_Type = RowStatus
_QtechBfdSessIpMapRowStatus_Object = MibTableColumn
qtechBfdSessIpMapRowStatus = _QtechBfdSessIpMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 5, 1, 3),
    _QtechBfdSessIpMapRowStatus_Type()
)
qtechBfdSessIpMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechBfdSessIpMapRowStatus.setStatus("current")
_QtechBfdConformance_ObjectIdentity = ObjectIdentity
qtechBfdConformance = _QtechBfdConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 2)
)
_QtechBfdGroups_ObjectIdentity = ObjectIdentity
qtechBfdGroups = _QtechBfdGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 2, 1)
)
_QtechBfdCompliances_ObjectIdentity = ObjectIdentity
qtechBfdCompliances = _QtechBfdCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 2, 2)
)
qtechBfdSessEntry.registerAugmentions(
    ("QTECH-BFD-MIB",
     "qtechBfdSessPerfEntry")
)
qtechBfdSessPerfEntry.setIndexNames(*qtechBfdSessEntry.getIndexNames())

# Managed Objects groups

qtechBfdSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 2, 1, 1)
)
qtechBfdSessionGroup.setObjects(
      *(("QTECH-BFD-MIB", "qtechBfdAdminStatus"),
        ("QTECH-BFD-MIB", "qtechBfdSessNotificationsEnable"),
        ("QTECH-BFD-MIB", "qtechBfdSessVersionNumber"),
        ("QTECH-BFD-MIB", "qtechBfdSessType"),
        ("QTECH-BFD-MIB", "qtechBfdSessDestinationUdpPort"),
        ("QTECH-BFD-MIB", "qtechBfdSessSourceUdpPort"),
        ("QTECH-BFD-MIB", "qtechBfdSessEchoSourceUdpPort"),
        ("QTECH-BFD-MIB", "qtechBfdSessAdminStatus"),
        ("QTECH-BFD-MIB", "qtechBfdSessOperMode"),
        ("QTECH-BFD-MIB", "qtechBfdSessDemandModeDesiredFlag"),
        ("QTECH-BFD-MIB", "qtechBfdSessControlPlaneIndepFlag"),
        ("QTECH-BFD-MIB", "qtechBfdSessMultipointFlag"),
        ("QTECH-BFD-MIB", "qtechBfdSessInterface"),
        ("QTECH-BFD-MIB", "qtechBfdSessSrcAddrType"),
        ("QTECH-BFD-MIB", "qtechBfdSessSrcAddr"),
        ("QTECH-BFD-MIB", "qtechBfdSessDstAddrType"),
        ("QTECH-BFD-MIB", "qtechBfdSessDstAddr"),
        ("QTECH-BFD-MIB", "qtechBfdSessGTSM"),
        ("QTECH-BFD-MIB", "qtechBfdSessGTSMTTL"),
        ("QTECH-BFD-MIB", "qtechBfdSessDesiredMinTxInterval"),
        ("QTECH-BFD-MIB", "qtechBfdSessReqMinRxInterval"),
        ("QTECH-BFD-MIB", "qtechBfdSessReqMinEchoRxInterval"),
        ("QTECH-BFD-MIB", "qtechBfdSessDetectMult"),
        ("QTECH-BFD-MIB", "qtechBfdSessAuthPresFlag"),
        ("QTECH-BFD-MIB", "qtechBfdSessAuthenticationType"),
        ("QTECH-BFD-MIB", "qtechBfdSessAuthenticationKeyID"),
        ("QTECH-BFD-MIB", "qtechBfdSessAuthenticationKey"),
        ("QTECH-BFD-MIB", "qtechBfdSessStorageType"),
        ("QTECH-BFD-MIB", "qtechBfdSessRowStatus"),
        ("QTECH-BFD-MIB", "qtechBfdSessDiscMapStorageType"),
        ("QTECH-BFD-MIB", "qtechBfdSessDiscMapRowStatus"),
        ("QTECH-BFD-MIB", "qtechBfdSessIpMapStorageType"),
        ("QTECH-BFD-MIB", "qtechBfdSessIpMapRowStatus"))
)
if mibBuilder.loadTexts:
    qtechBfdSessionGroup.setStatus("current")

qtechBfdSessionReadOnlyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 2, 1, 2)
)
qtechBfdSessionReadOnlyGroup.setObjects(
      *(("QTECH-BFD-MIB", "qtechBfdSessDiscriminator"),
        ("QTECH-BFD-MIB", "qtechBfdSessRemoteDiscr"),
        ("QTECH-BFD-MIB", "qtechBfdSessState"),
        ("QTECH-BFD-MIB", "qtechBfdSessRemoteHeardFlag"),
        ("QTECH-BFD-MIB", "qtechBfdSessDiag"),
        ("QTECH-BFD-MIB", "qtechBfdSessNegotiatedInterval"),
        ("QTECH-BFD-MIB", "qtechBfdSessNegotiatedEchoInterval"),
        ("QTECH-BFD-MIB", "qtechBfdSessNegotiatedDetectMult"),
        ("QTECH-BFD-MIB", "qtechBfdSessDiscMapIndex"),
        ("QTECH-BFD-MIB", "qtechBfdSessIpMapIndex"))
)
if mibBuilder.loadTexts:
    qtechBfdSessionReadOnlyGroup.setStatus("current")

qtechBfdSessionPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 2, 1, 3)
)
qtechBfdSessionPerfGroup.setObjects(
      *(("QTECH-BFD-MIB", "qtechBfdSessPerfCtrlPktIn"),
        ("QTECH-BFD-MIB", "qtechBfdSessPerfCtrlPktOut"),
        ("QTECH-BFD-MIB", "qtechBfdSessPerfCtrlPktDrop"),
        ("QTECH-BFD-MIB", "qtechBfdSessPerfCtrlPktDropLastTime"),
        ("QTECH-BFD-MIB", "qtechBfdSessPerfEchoPktIn"),
        ("QTECH-BFD-MIB", "qtechBfdSessPerfEchoPktOut"),
        ("QTECH-BFD-MIB", "qtechBfdSessPerfEchoPktDrop"),
        ("QTECH-BFD-MIB", "qtechBfdSessPerfEchoPktDropLastTime"),
        ("QTECH-BFD-MIB", "qtechBfdSessUpTime"),
        ("QTECH-BFD-MIB", "qtechBfdSessPerfLastSessDownTime"),
        ("QTECH-BFD-MIB", "qtechBfdSessPerfLastCommLostDiag"),
        ("QTECH-BFD-MIB", "qtechBfdSessPerfSessUpCount"),
        ("QTECH-BFD-MIB", "qtechBfdSessPerfDiscTime"))
)
if mibBuilder.loadTexts:
    qtechBfdSessionPerfGroup.setStatus("current")

qtechBfdSessionPerfHCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 2, 1, 4)
)
qtechBfdSessionPerfHCGroup.setObjects(
      *(("QTECH-BFD-MIB", "qtechBfdSessPerfCtrlPktInHC"),
        ("QTECH-BFD-MIB", "qtechBfdSessPerfCtrlPktOutHC"),
        ("QTECH-BFD-MIB", "qtechBfdSessPerfCtrlPktDropHC"),
        ("QTECH-BFD-MIB", "qtechBfdSessPerfEchoPktInHC"),
        ("QTECH-BFD-MIB", "qtechBfdSessPerfEchoPktOutHC"),
        ("QTECH-BFD-MIB", "qtechBfdSessPerfEchoPktDropHC"))
)
if mibBuilder.loadTexts:
    qtechBfdSessionPerfHCGroup.setStatus("current")


# Notification objects

qtechBfdSessUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 0, 1)
)
qtechBfdSessUp.setObjects(
      *(("QTECH-BFD-MIB", "qtechBfdSessDiag"),
        ("QTECH-BFD-MIB", "qtechBfdSessDiag"))
)
if mibBuilder.loadTexts:
    qtechBfdSessUp.setStatus(
        "current"
    )

qtechBfdSessDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 0, 2)
)
qtechBfdSessDown.setObjects(
      *(("QTECH-BFD-MIB", "qtechBfdSessDiag"),
        ("QTECH-BFD-MIB", "qtechBfdSessDiag"))
)
if mibBuilder.loadTexts:
    qtechBfdSessDown.setStatus(
        "current"
    )


# Notifications groups

qtechBfdNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 2, 1, 5)
)
qtechBfdNotificationGroup.setObjects(
      *(("QTECH-BFD-MIB", "qtechBfdSessUp"),
        ("QTECH-BFD-MIB", "qtechBfdSessDown"))
)
if mibBuilder.loadTexts:
    qtechBfdNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

qtechBfdModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 2, 2, 1)
)
qtechBfdModuleFullCompliance.setObjects(
      *(("QTECH-BFD-MIB", "qtechBfdSessionGroup"),
        ("QTECH-BFD-MIB", "qtechBfdSessionReadOnlyGroup"),
        ("QTECH-BFD-MIB", "qtechBfdSessionPerfGroup"),
        ("QTECH-BFD-MIB", "qtechBfdNotificationGroup"),
        ("QTECH-BFD-MIB", "qtechBfdSessionPerfHCGroup"))
)
if mibBuilder.loadTexts:
    qtechBfdModuleFullCompliance.setStatus(
        "current"
    )

qtechBfdModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 2, 2, 2)
)
qtechBfdModuleReadOnlyCompliance.setObjects(
      *(("QTECH-BFD-MIB", "qtechBfdSessionGroup"),
        ("QTECH-BFD-MIB", "qtechBfdSessionReadOnlyGroup"),
        ("QTECH-BFD-MIB", "qtechBfdSessionPerfGroup"),
        ("QTECH-BFD-MIB", "qtechBfdNotificationGroup"),
        ("QTECH-BFD-MIB", "qtechBfdSessionPerfHCGroup"))
)
if mibBuilder.loadTexts:
    qtechBfdModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-BFD-MIB",
    **{"QtechBfdSessIndexTC": QtechBfdSessIndexTC,
       "QtechBfdIntervalTC": QtechBfdIntervalTC,
       "QtechBfdMultiplierTC": QtechBfdMultiplierTC,
       "QtechBfdDiagTC": QtechBfdDiagTC,
       "QtechBfdSessTypeTC": QtechBfdSessTypeTC,
       "QtechBfdSessOperModeTC": QtechBfdSessOperModeTC,
       "QtechBfdCtrlDestPortNumberTC": QtechBfdCtrlDestPortNumberTC,
       "QtechBfdCtrlSourcePortNumberTC": QtechBfdCtrlSourcePortNumberTC,
       "QtechBfdSessStateTC": QtechBfdSessStateTC,
       "QtechBfdSessAuthenticationTypeTC": QtechBfdSessAuthenticationTypeTC,
       "QtechBfdSessionAuthenticationKeyTC": QtechBfdSessionAuthenticationKeyTC,
       "qtechBfdMIB": qtechBfdMIB,
       "qtechBfdNotifications": qtechBfdNotifications,
       "qtechBfdSessUp": qtechBfdSessUp,
       "qtechBfdSessDown": qtechBfdSessDown,
       "qtechBfdObjects": qtechBfdObjects,
       "qtechBfdScalarObjects": qtechBfdScalarObjects,
       "qtechBfdAdminStatus": qtechBfdAdminStatus,
       "qtechBfdSessNotificationsEnable": qtechBfdSessNotificationsEnable,
       "qtechBfdSessTable": qtechBfdSessTable,
       "qtechBfdSessEntry": qtechBfdSessEntry,
       "qtechBfdSessIndex": qtechBfdSessIndex,
       "qtechBfdSessVersionNumber": qtechBfdSessVersionNumber,
       "qtechBfdSessType": qtechBfdSessType,
       "qtechBfdSessDiscriminator": qtechBfdSessDiscriminator,
       "qtechBfdSessRemoteDiscr": qtechBfdSessRemoteDiscr,
       "qtechBfdSessDestinationUdpPort": qtechBfdSessDestinationUdpPort,
       "qtechBfdSessSourceUdpPort": qtechBfdSessSourceUdpPort,
       "qtechBfdSessEchoSourceUdpPort": qtechBfdSessEchoSourceUdpPort,
       "qtechBfdSessAdminStatus": qtechBfdSessAdminStatus,
       "qtechBfdSessState": qtechBfdSessState,
       "qtechBfdSessRemoteHeardFlag": qtechBfdSessRemoteHeardFlag,
       "qtechBfdSessDiag": qtechBfdSessDiag,
       "qtechBfdSessOperMode": qtechBfdSessOperMode,
       "qtechBfdSessDemandModeDesiredFlag": qtechBfdSessDemandModeDesiredFlag,
       "qtechBfdSessControlPlaneIndepFlag": qtechBfdSessControlPlaneIndepFlag,
       "qtechBfdSessMultipointFlag": qtechBfdSessMultipointFlag,
       "qtechBfdSessInterface": qtechBfdSessInterface,
       "qtechBfdSessSrcAddrType": qtechBfdSessSrcAddrType,
       "qtechBfdSessSrcAddr": qtechBfdSessSrcAddr,
       "qtechBfdSessDstAddrType": qtechBfdSessDstAddrType,
       "qtechBfdSessDstAddr": qtechBfdSessDstAddr,
       "qtechBfdSessGTSM": qtechBfdSessGTSM,
       "qtechBfdSessGTSMTTL": qtechBfdSessGTSMTTL,
       "qtechBfdSessDesiredMinTxInterval": qtechBfdSessDesiredMinTxInterval,
       "qtechBfdSessReqMinRxInterval": qtechBfdSessReqMinRxInterval,
       "qtechBfdSessReqMinEchoRxInterval": qtechBfdSessReqMinEchoRxInterval,
       "qtechBfdSessDetectMult": qtechBfdSessDetectMult,
       "qtechBfdSessNegotiatedInterval": qtechBfdSessNegotiatedInterval,
       "qtechBfdSessNegotiatedEchoInterval": qtechBfdSessNegotiatedEchoInterval,
       "qtechBfdSessNegotiatedDetectMult": qtechBfdSessNegotiatedDetectMult,
       "qtechBfdSessAuthPresFlag": qtechBfdSessAuthPresFlag,
       "qtechBfdSessAuthenticationType": qtechBfdSessAuthenticationType,
       "qtechBfdSessAuthenticationKeyID": qtechBfdSessAuthenticationKeyID,
       "qtechBfdSessAuthenticationKey": qtechBfdSessAuthenticationKey,
       "qtechBfdSessStorageType": qtechBfdSessStorageType,
       "qtechBfdSessRowStatus": qtechBfdSessRowStatus,
       "qtechBfdSessPerfTable": qtechBfdSessPerfTable,
       "qtechBfdSessPerfEntry": qtechBfdSessPerfEntry,
       "qtechBfdSessPerfCtrlPktIn": qtechBfdSessPerfCtrlPktIn,
       "qtechBfdSessPerfCtrlPktOut": qtechBfdSessPerfCtrlPktOut,
       "qtechBfdSessPerfCtrlPktDrop": qtechBfdSessPerfCtrlPktDrop,
       "qtechBfdSessPerfCtrlPktDropLastTime": qtechBfdSessPerfCtrlPktDropLastTime,
       "qtechBfdSessPerfEchoPktIn": qtechBfdSessPerfEchoPktIn,
       "qtechBfdSessPerfEchoPktOut": qtechBfdSessPerfEchoPktOut,
       "qtechBfdSessPerfEchoPktDrop": qtechBfdSessPerfEchoPktDrop,
       "qtechBfdSessPerfEchoPktDropLastTime": qtechBfdSessPerfEchoPktDropLastTime,
       "qtechBfdSessUpTime": qtechBfdSessUpTime,
       "qtechBfdSessPerfLastSessDownTime": qtechBfdSessPerfLastSessDownTime,
       "qtechBfdSessPerfLastCommLostDiag": qtechBfdSessPerfLastCommLostDiag,
       "qtechBfdSessPerfSessUpCount": qtechBfdSessPerfSessUpCount,
       "qtechBfdSessPerfDiscTime": qtechBfdSessPerfDiscTime,
       "qtechBfdSessPerfCtrlPktInHC": qtechBfdSessPerfCtrlPktInHC,
       "qtechBfdSessPerfCtrlPktOutHC": qtechBfdSessPerfCtrlPktOutHC,
       "qtechBfdSessPerfCtrlPktDropHC": qtechBfdSessPerfCtrlPktDropHC,
       "qtechBfdSessPerfEchoPktInHC": qtechBfdSessPerfEchoPktInHC,
       "qtechBfdSessPerfEchoPktOutHC": qtechBfdSessPerfEchoPktOutHC,
       "qtechBfdSessPerfEchoPktDropHC": qtechBfdSessPerfEchoPktDropHC,
       "qtechBfdSessDiscMapTable": qtechBfdSessDiscMapTable,
       "qtechBfdSessDiscMapEntry": qtechBfdSessDiscMapEntry,
       "qtechBfdSessDiscMapIndex": qtechBfdSessDiscMapIndex,
       "qtechBfdSessDiscMapStorageType": qtechBfdSessDiscMapStorageType,
       "qtechBfdSessDiscMapRowStatus": qtechBfdSessDiscMapRowStatus,
       "qtechBfdSessIpMapTable": qtechBfdSessIpMapTable,
       "qtechBfdSessIpMapEntry": qtechBfdSessIpMapEntry,
       "qtechBfdSessIpMapIndex": qtechBfdSessIpMapIndex,
       "qtechBfdSessIpMapStorageType": qtechBfdSessIpMapStorageType,
       "qtechBfdSessIpMapRowStatus": qtechBfdSessIpMapRowStatus,
       "qtechBfdConformance": qtechBfdConformance,
       "qtechBfdGroups": qtechBfdGroups,
       "qtechBfdSessionGroup": qtechBfdSessionGroup,
       "qtechBfdSessionReadOnlyGroup": qtechBfdSessionReadOnlyGroup,
       "qtechBfdSessionPerfGroup": qtechBfdSessionPerfGroup,
       "qtechBfdSessionPerfHCGroup": qtechBfdSessionPerfHCGroup,
       "qtechBfdNotificationGroup": qtechBfdNotificationGroup,
       "qtechBfdCompliances": qtechBfdCompliances,
       "qtechBfdModuleFullCompliance": qtechBfdModuleFullCompliance,
       "qtechBfdModuleReadOnlyCompliance": qtechBfdModuleReadOnlyCompliance}
)
