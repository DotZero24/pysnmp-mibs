# SNMP MIB module (RAISECOM-BFD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-BFD-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:24 2025
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

(raisecomAgent,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "raisecomAgent")

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
 Opaque,
 TimeTicks,
 Unsigned32,
 iso,
 mib_2,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "iso",
    "mib-2",
    "zeroDotZero")

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

(EnableVar,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar")


# MODULE-IDENTITY

raisecomBfd = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35)
)
if mibBuilder.loadTexts:
    raisecomBfd.setRevisions(
        ("2011-04-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class BfdSessIndexTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class BfdIntervalTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class BfdMultiplierTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class BfdDiagTC(TextualConvention, Integer32):
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



class BfdSessTypeTC(TextualConvention, Integer32):
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



class BfdSessOperModeTC(TextualConvention, Integer32):
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



class BfdCtrlDestPortNumberTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class BfdCtrlSourcePortNumberTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class BfdSessStateTC(TextualConvention, Integer32):
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



class BfdSessAuthenticationTypeTC(TextualConvention, Integer32):
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



class BfdSessionAuthenticationKeyTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x "
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 252),
    )



# MIB Managed Objects in the order of their OIDs

_RaisecomBfdNotifications_ObjectIdentity = ObjectIdentity
raisecomBfdNotifications = _RaisecomBfdNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 0)
)
_RaisecomBfdObjects_ObjectIdentity = ObjectIdentity
raisecomBfdObjects = _RaisecomBfdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1)
)
_RaisecomBfdScalarObjects_ObjectIdentity = ObjectIdentity
raisecomBfdScalarObjects = _RaisecomBfdScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 1)
)


class _RaisecomBfdAdminStatus_Type(Integer32):
    """Custom type raisecomBfdAdminStatus based on Integer32"""
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


_RaisecomBfdAdminStatus_Type.__name__ = "Integer32"
_RaisecomBfdAdminStatus_Object = MibScalar
raisecomBfdAdminStatus = _RaisecomBfdAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 1, 1),
    _RaisecomBfdAdminStatus_Type()
)
raisecomBfdAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomBfdAdminStatus.setStatus("current")


class _RaisecomBfdSessNotificationsEnable_Type(TruthValue):
    """Custom type raisecomBfdSessNotificationsEnable based on TruthValue"""
    defaultValue = 2


_RaisecomBfdSessNotificationsEnable_Type.__name__ = "TruthValue"
_RaisecomBfdSessNotificationsEnable_Object = MibScalar
raisecomBfdSessNotificationsEnable = _RaisecomBfdSessNotificationsEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 1, 2),
    _RaisecomBfdSessNotificationsEnable_Type()
)
raisecomBfdSessNotificationsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomBfdSessNotificationsEnable.setStatus("current")


class _RaisecomBfdRoleMode_Type(Integer32):
    """Custom type raisecomBfdRoleMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activeRole", 1),
          ("passiveRole", 2))
    )


_RaisecomBfdRoleMode_Type.__name__ = "Integer32"
_RaisecomBfdRoleMode_Object = MibScalar
raisecomBfdRoleMode = _RaisecomBfdRoleMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 1, 3),
    _RaisecomBfdRoleMode_Type()
)
raisecomBfdRoleMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomBfdRoleMode.setStatus("current")
_RaisecomBfdEchoSourceIpType_Type = InetAddressType
_RaisecomBfdEchoSourceIpType_Object = MibScalar
raisecomBfdEchoSourceIpType = _RaisecomBfdEchoSourceIpType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 1, 4),
    _RaisecomBfdEchoSourceIpType_Type()
)
raisecomBfdEchoSourceIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomBfdEchoSourceIpType.setStatus("current")
_RaisecomBfdEchoSourceIpAddr_Type = InetAddress
_RaisecomBfdEchoSourceIpAddr_Object = MibScalar
raisecomBfdEchoSourceIpAddr = _RaisecomBfdEchoSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 1, 5),
    _RaisecomBfdEchoSourceIpAddr_Type()
)
raisecomBfdEchoSourceIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomBfdEchoSourceIpAddr.setStatus("current")


class _RaisecomBfdAllSessionsStatisticsClear_Type(EnableVar):
    """Custom type raisecomBfdAllSessionsStatisticsClear based on EnableVar"""
    defaultValue = 2


_RaisecomBfdAllSessionsStatisticsClear_Type.__name__ = "EnableVar"
_RaisecomBfdAllSessionsStatisticsClear_Object = MibScalar
raisecomBfdAllSessionsStatisticsClear = _RaisecomBfdAllSessionsStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 1, 6),
    _RaisecomBfdAllSessionsStatisticsClear_Type()
)
raisecomBfdAllSessionsStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomBfdAllSessionsStatisticsClear.setStatus("current")
_RaisecomBfdSessTable_Object = MibTable
raisecomBfdSessTable = _RaisecomBfdSessTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 2)
)
if mibBuilder.loadTexts:
    raisecomBfdSessTable.setStatus("current")
_RaisecomBfdSessEntry_Object = MibTableRow
raisecomBfdSessEntry = _RaisecomBfdSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 2, 1)
)
raisecomBfdSessEntry.setIndexNames(
    (0, "RAISECOM-BFD-MIB", "raisecomBfdSessIndex"),
)
if mibBuilder.loadTexts:
    raisecomBfdSessEntry.setStatus("current")
_RaisecomBfdSessIndex_Type = BfdSessIndexTC
_RaisecomBfdSessIndex_Object = MibTableColumn
raisecomBfdSessIndex = _RaisecomBfdSessIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 2, 1, 1),
    _RaisecomBfdSessIndex_Type()
)
raisecomBfdSessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomBfdSessIndex.setStatus("current")


class _RaisecomBfdSessVersionNumber_Type(Unsigned32):
    """Custom type raisecomBfdSessVersionNumber based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RaisecomBfdSessVersionNumber_Type.__name__ = "Unsigned32"
_RaisecomBfdSessVersionNumber_Object = MibTableColumn
raisecomBfdSessVersionNumber = _RaisecomBfdSessVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 2, 1, 2),
    _RaisecomBfdSessVersionNumber_Type()
)
raisecomBfdSessVersionNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomBfdSessVersionNumber.setStatus("current")
_RaisecomBfdSessType_Type = BfdSessTypeTC
_RaisecomBfdSessType_Object = MibTableColumn
raisecomBfdSessType = _RaisecomBfdSessType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 2, 1, 3),
    _RaisecomBfdSessType_Type()
)
raisecomBfdSessType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomBfdSessType.setStatus("current")


class _RaisecomBfdSessDiscriminator_Type(Unsigned32):
    """Custom type raisecomBfdSessDiscriminator based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RaisecomBfdSessDiscriminator_Type.__name__ = "Unsigned32"
_RaisecomBfdSessDiscriminator_Object = MibTableColumn
raisecomBfdSessDiscriminator = _RaisecomBfdSessDiscriminator_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 2, 1, 4),
    _RaisecomBfdSessDiscriminator_Type()
)
raisecomBfdSessDiscriminator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomBfdSessDiscriminator.setStatus("current")


class _RaisecomBfdSessRemoteDiscr_Type(Unsigned32):
    """Custom type raisecomBfdSessRemoteDiscr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_RaisecomBfdSessRemoteDiscr_Type.__name__ = "Unsigned32"
_RaisecomBfdSessRemoteDiscr_Object = MibTableColumn
raisecomBfdSessRemoteDiscr = _RaisecomBfdSessRemoteDiscr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 2, 1, 5),
    _RaisecomBfdSessRemoteDiscr_Type()
)
raisecomBfdSessRemoteDiscr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomBfdSessRemoteDiscr.setStatus("current")


class _RaisecomBfdSessDestinationUdpPort_Type(BfdCtrlDestPortNumberTC):
    """Custom type raisecomBfdSessDestinationUdpPort based on BfdCtrlDestPortNumberTC"""
    defaultValue = 0


_RaisecomBfdSessDestinationUdpPort_Type.__name__ = "BfdCtrlDestPortNumberTC"
_RaisecomBfdSessDestinationUdpPort_Object = MibTableColumn
raisecomBfdSessDestinationUdpPort = _RaisecomBfdSessDestinationUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 2, 1, 6),
    _RaisecomBfdSessDestinationUdpPort_Type()
)
raisecomBfdSessDestinationUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomBfdSessDestinationUdpPort.setStatus("current")


class _RaisecomBfdSessSourceUdpPort_Type(BfdCtrlSourcePortNumberTC):
    """Custom type raisecomBfdSessSourceUdpPort based on BfdCtrlSourcePortNumberTC"""
    defaultValue = 0


_RaisecomBfdSessSourceUdpPort_Type.__name__ = "BfdCtrlSourcePortNumberTC"
_RaisecomBfdSessSourceUdpPort_Object = MibTableColumn
raisecomBfdSessSourceUdpPort = _RaisecomBfdSessSourceUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 2, 1, 7),
    _RaisecomBfdSessSourceUdpPort_Type()
)
raisecomBfdSessSourceUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomBfdSessSourceUdpPort.setStatus("current")


class _RaisecomBfdSessEchoSourceUdpPort_Type(InetPortNumber):
    """Custom type raisecomBfdSessEchoSourceUdpPort based on InetPortNumber"""
    defaultValue = 0


_RaisecomBfdSessEchoSourceUdpPort_Type.__name__ = "InetPortNumber"
_RaisecomBfdSessEchoSourceUdpPort_Object = MibTableColumn
raisecomBfdSessEchoSourceUdpPort = _RaisecomBfdSessEchoSourceUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 2, 1, 8),
    _RaisecomBfdSessEchoSourceUdpPort_Type()
)
raisecomBfdSessEchoSourceUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomBfdSessEchoSourceUdpPort.setStatus("current")


class _RaisecomBfdSessAdminStatus_Type(Integer32):
    """Custom type raisecomBfdSessAdminStatus based on Integer32"""
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


_RaisecomBfdSessAdminStatus_Type.__name__ = "Integer32"
_RaisecomBfdSessAdminStatus_Object = MibTableColumn
raisecomBfdSessAdminStatus = _RaisecomBfdSessAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 2, 1, 9),
    _RaisecomBfdSessAdminStatus_Type()
)
raisecomBfdSessAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomBfdSessAdminStatus.setStatus("current")


class _RaisecomBfdSessState_Type(BfdSessStateTC):
    """Custom type raisecomBfdSessState based on BfdSessStateTC"""
    defaultValue = 2


_RaisecomBfdSessState_Type.__name__ = "BfdSessStateTC"
_RaisecomBfdSessState_Object = MibTableColumn
raisecomBfdSessState = _RaisecomBfdSessState_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 2, 1, 10),
    _RaisecomBfdSessState_Type()
)
raisecomBfdSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomBfdSessState.setStatus("current")


class _RaisecomBfdSessRemoteHeardFlag_Type(TruthValue):
    """Custom type raisecomBfdSessRemoteHeardFlag based on TruthValue"""
    defaultValue = 2


_RaisecomBfdSessRemoteHeardFlag_Type.__name__ = "TruthValue"
_RaisecomBfdSessRemoteHeardFlag_Object = MibTableColumn
raisecomBfdSessRemoteHeardFlag = _RaisecomBfdSessRemoteHeardFlag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 2, 1, 11),
    _RaisecomBfdSessRemoteHeardFlag_Type()
)
raisecomBfdSessRemoteHeardFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomBfdSessRemoteHeardFlag.setStatus("current")
_RaisecomBfdSessDiag_Type = BfdDiagTC
_RaisecomBfdSessDiag_Object = MibTableColumn
raisecomBfdSessDiag = _RaisecomBfdSessDiag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 2, 1, 12),
    _RaisecomBfdSessDiag_Type()
)
raisecomBfdSessDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomBfdSessDiag.setStatus("current")
_RaisecomBfdSessOperMode_Type = BfdSessOperModeTC
_RaisecomBfdSessOperMode_Object = MibTableColumn
raisecomBfdSessOperMode = _RaisecomBfdSessOperMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 2, 1, 13),
    _RaisecomBfdSessOperMode_Type()
)
raisecomBfdSessOperMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomBfdSessOperMode.setStatus("current")


class _RaisecomBfdSessDemandModeDesiredFlag_Type(TruthValue):
    """Custom type raisecomBfdSessDemandModeDesiredFlag based on TruthValue"""
    defaultValue = 2


_RaisecomBfdSessDemandModeDesiredFlag_Type.__name__ = "TruthValue"
_RaisecomBfdSessDemandModeDesiredFlag_Object = MibTableColumn
raisecomBfdSessDemandModeDesiredFlag = _RaisecomBfdSessDemandModeDesiredFlag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 2, 1, 14),
    _RaisecomBfdSessDemandModeDesiredFlag_Type()
)
raisecomBfdSessDemandModeDesiredFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomBfdSessDemandModeDesiredFlag.setStatus("current")


class _RaisecomBfdSessControlPlaneIndepFlag_Type(TruthValue):
    """Custom type raisecomBfdSessControlPlaneIndepFlag based on TruthValue"""
    defaultValue = 2


_RaisecomBfdSessControlPlaneIndepFlag_Type.__name__ = "TruthValue"
_RaisecomBfdSessControlPlaneIndepFlag_Object = MibTableColumn
raisecomBfdSessControlPlaneIndepFlag = _RaisecomBfdSessControlPlaneIndepFlag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 2, 1, 15),
    _RaisecomBfdSessControlPlaneIndepFlag_Type()
)
raisecomBfdSessControlPlaneIndepFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomBfdSessControlPlaneIndepFlag.setStatus("current")


class _RaisecomBfdSessMultipointFlag_Type(TruthValue):
    """Custom type raisecomBfdSessMultipointFlag based on TruthValue"""
    defaultValue = 2


_RaisecomBfdSessMultipointFlag_Type.__name__ = "TruthValue"
_RaisecomBfdSessMultipointFlag_Object = MibTableColumn
raisecomBfdSessMultipointFlag = _RaisecomBfdSessMultipointFlag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 2, 1, 16),
    _RaisecomBfdSessMultipointFlag_Type()
)
raisecomBfdSessMultipointFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomBfdSessMultipointFlag.setStatus("current")
_RaisecomBfdSessInterface_Type = InterfaceIndexOrZero
_RaisecomBfdSessInterface_Object = MibTableColumn
raisecomBfdSessInterface = _RaisecomBfdSessInterface_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 2, 1, 17),
    _RaisecomBfdSessInterface_Type()
)
raisecomBfdSessInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomBfdSessInterface.setStatus("current")
_RaisecomBfdSessSrcAddrType_Type = InetAddressType
_RaisecomBfdSessSrcAddrType_Object = MibTableColumn
raisecomBfdSessSrcAddrType = _RaisecomBfdSessSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 2, 1, 18),
    _RaisecomBfdSessSrcAddrType_Type()
)
raisecomBfdSessSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomBfdSessSrcAddrType.setStatus("current")
_RaisecomBfdSessSrcAddr_Type = InetAddress
_RaisecomBfdSessSrcAddr_Object = MibTableColumn
raisecomBfdSessSrcAddr = _RaisecomBfdSessSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 2, 1, 19),
    _RaisecomBfdSessSrcAddr_Type()
)
raisecomBfdSessSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomBfdSessSrcAddr.setStatus("current")
_RaisecomBfdSessDstAddrType_Type = InetAddressType
_RaisecomBfdSessDstAddrType_Object = MibTableColumn
raisecomBfdSessDstAddrType = _RaisecomBfdSessDstAddrType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 2, 1, 20),
    _RaisecomBfdSessDstAddrType_Type()
)
raisecomBfdSessDstAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomBfdSessDstAddrType.setStatus("current")
_RaisecomBfdSessDstAddr_Type = InetAddress
_RaisecomBfdSessDstAddr_Object = MibTableColumn
raisecomBfdSessDstAddr = _RaisecomBfdSessDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 2, 1, 21),
    _RaisecomBfdSessDstAddr_Type()
)
raisecomBfdSessDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomBfdSessDstAddr.setStatus("current")


class _RaisecomBfdSessGTSM_Type(TruthValue):
    """Custom type raisecomBfdSessGTSM based on TruthValue"""
    defaultValue = 2


_RaisecomBfdSessGTSM_Type.__name__ = "TruthValue"
_RaisecomBfdSessGTSM_Object = MibTableColumn
raisecomBfdSessGTSM = _RaisecomBfdSessGTSM_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 2, 1, 22),
    _RaisecomBfdSessGTSM_Type()
)
raisecomBfdSessGTSM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomBfdSessGTSM.setStatus("current")


class _RaisecomBfdSessGTSMTTL_Type(Unsigned32):
    """Custom type raisecomBfdSessGTSMTTL based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RaisecomBfdSessGTSMTTL_Type.__name__ = "Unsigned32"
_RaisecomBfdSessGTSMTTL_Object = MibTableColumn
raisecomBfdSessGTSMTTL = _RaisecomBfdSessGTSMTTL_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 2, 1, 23),
    _RaisecomBfdSessGTSMTTL_Type()
)
raisecomBfdSessGTSMTTL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomBfdSessGTSMTTL.setStatus("current")
_RaisecomBfdSessDesiredMinTxInterval_Type = BfdIntervalTC
_RaisecomBfdSessDesiredMinTxInterval_Object = MibTableColumn
raisecomBfdSessDesiredMinTxInterval = _RaisecomBfdSessDesiredMinTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 2, 1, 24),
    _RaisecomBfdSessDesiredMinTxInterval_Type()
)
raisecomBfdSessDesiredMinTxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomBfdSessDesiredMinTxInterval.setStatus("current")
_RaisecomBfdSessReqMinRxInterval_Type = BfdIntervalTC
_RaisecomBfdSessReqMinRxInterval_Object = MibTableColumn
raisecomBfdSessReqMinRxInterval = _RaisecomBfdSessReqMinRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 2, 1, 25),
    _RaisecomBfdSessReqMinRxInterval_Type()
)
raisecomBfdSessReqMinRxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomBfdSessReqMinRxInterval.setStatus("current")
_RaisecomBfdSessReqMinEchoRxInterval_Type = BfdIntervalTC
_RaisecomBfdSessReqMinEchoRxInterval_Object = MibTableColumn
raisecomBfdSessReqMinEchoRxInterval = _RaisecomBfdSessReqMinEchoRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 2, 1, 26),
    _RaisecomBfdSessReqMinEchoRxInterval_Type()
)
raisecomBfdSessReqMinEchoRxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomBfdSessReqMinEchoRxInterval.setStatus("current")
_RaisecomBfdSessDetectMult_Type = BfdMultiplierTC
_RaisecomBfdSessDetectMult_Object = MibTableColumn
raisecomBfdSessDetectMult = _RaisecomBfdSessDetectMult_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 2, 1, 27),
    _RaisecomBfdSessDetectMult_Type()
)
raisecomBfdSessDetectMult.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomBfdSessDetectMult.setStatus("current")
_RaisecomBfdSessNegotiatedInterval_Type = BfdIntervalTC
_RaisecomBfdSessNegotiatedInterval_Object = MibTableColumn
raisecomBfdSessNegotiatedInterval = _RaisecomBfdSessNegotiatedInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 2, 1, 28),
    _RaisecomBfdSessNegotiatedInterval_Type()
)
raisecomBfdSessNegotiatedInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomBfdSessNegotiatedInterval.setStatus("current")
_RaisecomBfdSessNegotiatedEchoInterval_Type = BfdIntervalTC
_RaisecomBfdSessNegotiatedEchoInterval_Object = MibTableColumn
raisecomBfdSessNegotiatedEchoInterval = _RaisecomBfdSessNegotiatedEchoInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 2, 1, 29),
    _RaisecomBfdSessNegotiatedEchoInterval_Type()
)
raisecomBfdSessNegotiatedEchoInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomBfdSessNegotiatedEchoInterval.setStatus("current")
_RaisecomBfdSessNegotiatedDetectMult_Type = BfdMultiplierTC
_RaisecomBfdSessNegotiatedDetectMult_Object = MibTableColumn
raisecomBfdSessNegotiatedDetectMult = _RaisecomBfdSessNegotiatedDetectMult_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 2, 1, 30),
    _RaisecomBfdSessNegotiatedDetectMult_Type()
)
raisecomBfdSessNegotiatedDetectMult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomBfdSessNegotiatedDetectMult.setStatus("current")


class _RaisecomBfdSessAuthPresFlag_Type(TruthValue):
    """Custom type raisecomBfdSessAuthPresFlag based on TruthValue"""
    defaultValue = 2


_RaisecomBfdSessAuthPresFlag_Type.__name__ = "TruthValue"
_RaisecomBfdSessAuthPresFlag_Object = MibTableColumn
raisecomBfdSessAuthPresFlag = _RaisecomBfdSessAuthPresFlag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 2, 1, 31),
    _RaisecomBfdSessAuthPresFlag_Type()
)
raisecomBfdSessAuthPresFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomBfdSessAuthPresFlag.setStatus("current")


class _RaisecomBfdSessAuthenticationType_Type(BfdSessAuthenticationTypeTC):
    """Custom type raisecomBfdSessAuthenticationType based on BfdSessAuthenticationTypeTC"""
    defaultValue = -1


_RaisecomBfdSessAuthenticationType_Type.__name__ = "BfdSessAuthenticationTypeTC"
_RaisecomBfdSessAuthenticationType_Object = MibTableColumn
raisecomBfdSessAuthenticationType = _RaisecomBfdSessAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 2, 1, 32),
    _RaisecomBfdSessAuthenticationType_Type()
)
raisecomBfdSessAuthenticationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomBfdSessAuthenticationType.setStatus("current")


class _RaisecomBfdSessAuthenticationKeyID_Type(Integer32):
    """Custom type raisecomBfdSessAuthenticationKeyID based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_RaisecomBfdSessAuthenticationKeyID_Type.__name__ = "Integer32"
_RaisecomBfdSessAuthenticationKeyID_Object = MibTableColumn
raisecomBfdSessAuthenticationKeyID = _RaisecomBfdSessAuthenticationKeyID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 2, 1, 33),
    _RaisecomBfdSessAuthenticationKeyID_Type()
)
raisecomBfdSessAuthenticationKeyID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomBfdSessAuthenticationKeyID.setStatus("current")
_RaisecomBfdSessAuthenticationKey_Type = BfdSessionAuthenticationKeyTC
_RaisecomBfdSessAuthenticationKey_Object = MibTableColumn
raisecomBfdSessAuthenticationKey = _RaisecomBfdSessAuthenticationKey_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 2, 1, 34),
    _RaisecomBfdSessAuthenticationKey_Type()
)
raisecomBfdSessAuthenticationKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomBfdSessAuthenticationKey.setStatus("current")
_RaisecomBfdSessStorType_Type = StorageType
_RaisecomBfdSessStorType_Object = MibTableColumn
raisecomBfdSessStorType = _RaisecomBfdSessStorType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 2, 1, 35),
    _RaisecomBfdSessStorType_Type()
)
raisecomBfdSessStorType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomBfdSessStorType.setStatus("current")
_RaisecomBfdSessRowStatus_Type = RowStatus
_RaisecomBfdSessRowStatus_Object = MibTableColumn
raisecomBfdSessRowStatus = _RaisecomBfdSessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 2, 1, 36),
    _RaisecomBfdSessRowStatus_Type()
)
raisecomBfdSessRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomBfdSessRowStatus.setStatus("current")


class _RaisecomBfdSessTemplateName_Type(OctetString):
    """Custom type raisecomBfdSessTemplateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RaisecomBfdSessTemplateName_Type.__name__ = "OctetString"
_RaisecomBfdSessTemplateName_Object = MibTableColumn
raisecomBfdSessTemplateName = _RaisecomBfdSessTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 2, 1, 37),
    _RaisecomBfdSessTemplateName_Type()
)
raisecomBfdSessTemplateName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomBfdSessTemplateName.setStatus("current")
_RaisecomBfdSessPerfTable_Object = MibTable
raisecomBfdSessPerfTable = _RaisecomBfdSessPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 3)
)
if mibBuilder.loadTexts:
    raisecomBfdSessPerfTable.setStatus("current")
_RaisecomBfdSessPerfEntry_Object = MibTableRow
raisecomBfdSessPerfEntry = _RaisecomBfdSessPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 3, 1)
)
if mibBuilder.loadTexts:
    raisecomBfdSessPerfEntry.setStatus("current")
_RaisecomBfdSessPerfCtrlPktIn_Type = Counter32
_RaisecomBfdSessPerfCtrlPktIn_Object = MibTableColumn
raisecomBfdSessPerfCtrlPktIn = _RaisecomBfdSessPerfCtrlPktIn_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 3, 1, 1),
    _RaisecomBfdSessPerfCtrlPktIn_Type()
)
raisecomBfdSessPerfCtrlPktIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomBfdSessPerfCtrlPktIn.setStatus("current")
_RaisecomBfdSessPerfCtrlPktOut_Type = Counter32
_RaisecomBfdSessPerfCtrlPktOut_Object = MibTableColumn
raisecomBfdSessPerfCtrlPktOut = _RaisecomBfdSessPerfCtrlPktOut_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 3, 1, 2),
    _RaisecomBfdSessPerfCtrlPktOut_Type()
)
raisecomBfdSessPerfCtrlPktOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomBfdSessPerfCtrlPktOut.setStatus("current")
_RaisecomBfdSessPerfCtrlPktDrop_Type = Counter32
_RaisecomBfdSessPerfCtrlPktDrop_Object = MibTableColumn
raisecomBfdSessPerfCtrlPktDrop = _RaisecomBfdSessPerfCtrlPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 3, 1, 3),
    _RaisecomBfdSessPerfCtrlPktDrop_Type()
)
raisecomBfdSessPerfCtrlPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomBfdSessPerfCtrlPktDrop.setStatus("current")
_RaisecomBfdSessPerfCtrlPktDropLastTime_Type = TimeStamp
_RaisecomBfdSessPerfCtrlPktDropLastTime_Object = MibTableColumn
raisecomBfdSessPerfCtrlPktDropLastTime = _RaisecomBfdSessPerfCtrlPktDropLastTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 3, 1, 4),
    _RaisecomBfdSessPerfCtrlPktDropLastTime_Type()
)
raisecomBfdSessPerfCtrlPktDropLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomBfdSessPerfCtrlPktDropLastTime.setStatus("current")
_RaisecomBfdSessPerfEchoPktIn_Type = Counter32
_RaisecomBfdSessPerfEchoPktIn_Object = MibTableColumn
raisecomBfdSessPerfEchoPktIn = _RaisecomBfdSessPerfEchoPktIn_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 3, 1, 5),
    _RaisecomBfdSessPerfEchoPktIn_Type()
)
raisecomBfdSessPerfEchoPktIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomBfdSessPerfEchoPktIn.setStatus("current")
_RaisecomBfdSessPerfEchoPktOut_Type = Counter32
_RaisecomBfdSessPerfEchoPktOut_Object = MibTableColumn
raisecomBfdSessPerfEchoPktOut = _RaisecomBfdSessPerfEchoPktOut_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 3, 1, 6),
    _RaisecomBfdSessPerfEchoPktOut_Type()
)
raisecomBfdSessPerfEchoPktOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomBfdSessPerfEchoPktOut.setStatus("current")
_RaisecomBfdSessPerfEchoPktDrop_Type = Counter32
_RaisecomBfdSessPerfEchoPktDrop_Object = MibTableColumn
raisecomBfdSessPerfEchoPktDrop = _RaisecomBfdSessPerfEchoPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 3, 1, 7),
    _RaisecomBfdSessPerfEchoPktDrop_Type()
)
raisecomBfdSessPerfEchoPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomBfdSessPerfEchoPktDrop.setStatus("current")
_RaisecomBfdSessPerfEchoPktDropLastTime_Type = TimeStamp
_RaisecomBfdSessPerfEchoPktDropLastTime_Object = MibTableColumn
raisecomBfdSessPerfEchoPktDropLastTime = _RaisecomBfdSessPerfEchoPktDropLastTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 3, 1, 8),
    _RaisecomBfdSessPerfEchoPktDropLastTime_Type()
)
raisecomBfdSessPerfEchoPktDropLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomBfdSessPerfEchoPktDropLastTime.setStatus("current")
_RaisecomBfdSessUpTime_Type = TimeStamp
_RaisecomBfdSessUpTime_Object = MibTableColumn
raisecomBfdSessUpTime = _RaisecomBfdSessUpTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 3, 1, 9),
    _RaisecomBfdSessUpTime_Type()
)
raisecomBfdSessUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomBfdSessUpTime.setStatus("current")
_RaisecomBfdSessPerfLastSessDownTime_Type = TimeStamp
_RaisecomBfdSessPerfLastSessDownTime_Object = MibTableColumn
raisecomBfdSessPerfLastSessDownTime = _RaisecomBfdSessPerfLastSessDownTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 3, 1, 10),
    _RaisecomBfdSessPerfLastSessDownTime_Type()
)
raisecomBfdSessPerfLastSessDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomBfdSessPerfLastSessDownTime.setStatus("current")
_RaisecomBfdSessPerfLastCommLostDiag_Type = BfdDiagTC
_RaisecomBfdSessPerfLastCommLostDiag_Object = MibTableColumn
raisecomBfdSessPerfLastCommLostDiag = _RaisecomBfdSessPerfLastCommLostDiag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 3, 1, 11),
    _RaisecomBfdSessPerfLastCommLostDiag_Type()
)
raisecomBfdSessPerfLastCommLostDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomBfdSessPerfLastCommLostDiag.setStatus("current")
_RaisecomBfdSessPerfSessUpCount_Type = Counter32
_RaisecomBfdSessPerfSessUpCount_Object = MibTableColumn
raisecomBfdSessPerfSessUpCount = _RaisecomBfdSessPerfSessUpCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 3, 1, 12),
    _RaisecomBfdSessPerfSessUpCount_Type()
)
raisecomBfdSessPerfSessUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomBfdSessPerfSessUpCount.setStatus("current")
_RaisecomBfdSessPerfDiscTime_Type = TimeStamp
_RaisecomBfdSessPerfDiscTime_Object = MibTableColumn
raisecomBfdSessPerfDiscTime = _RaisecomBfdSessPerfDiscTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 3, 1, 13),
    _RaisecomBfdSessPerfDiscTime_Type()
)
raisecomBfdSessPerfDiscTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomBfdSessPerfDiscTime.setStatus("current")
_RaisecomBfdSessPerfCtrlPktInHC_Type = Counter64
_RaisecomBfdSessPerfCtrlPktInHC_Object = MibTableColumn
raisecomBfdSessPerfCtrlPktInHC = _RaisecomBfdSessPerfCtrlPktInHC_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 3, 1, 14),
    _RaisecomBfdSessPerfCtrlPktInHC_Type()
)
raisecomBfdSessPerfCtrlPktInHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomBfdSessPerfCtrlPktInHC.setStatus("current")
_RaisecomBfdSessPerfCtrlPktOutHC_Type = Counter64
_RaisecomBfdSessPerfCtrlPktOutHC_Object = MibTableColumn
raisecomBfdSessPerfCtrlPktOutHC = _RaisecomBfdSessPerfCtrlPktOutHC_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 3, 1, 15),
    _RaisecomBfdSessPerfCtrlPktOutHC_Type()
)
raisecomBfdSessPerfCtrlPktOutHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomBfdSessPerfCtrlPktOutHC.setStatus("current")
_RaisecomBfdSessPerfCtrlPktDropHC_Type = Counter64
_RaisecomBfdSessPerfCtrlPktDropHC_Object = MibTableColumn
raisecomBfdSessPerfCtrlPktDropHC = _RaisecomBfdSessPerfCtrlPktDropHC_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 3, 1, 16),
    _RaisecomBfdSessPerfCtrlPktDropHC_Type()
)
raisecomBfdSessPerfCtrlPktDropHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomBfdSessPerfCtrlPktDropHC.setStatus("current")
_RaisecomBfdSessPerfEchoPktInHC_Type = Counter64
_RaisecomBfdSessPerfEchoPktInHC_Object = MibTableColumn
raisecomBfdSessPerfEchoPktInHC = _RaisecomBfdSessPerfEchoPktInHC_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 3, 1, 17),
    _RaisecomBfdSessPerfEchoPktInHC_Type()
)
raisecomBfdSessPerfEchoPktInHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomBfdSessPerfEchoPktInHC.setStatus("current")
_RaisecomBfdSessPerfEchoPktOutHC_Type = Counter64
_RaisecomBfdSessPerfEchoPktOutHC_Object = MibTableColumn
raisecomBfdSessPerfEchoPktOutHC = _RaisecomBfdSessPerfEchoPktOutHC_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 3, 1, 18),
    _RaisecomBfdSessPerfEchoPktOutHC_Type()
)
raisecomBfdSessPerfEchoPktOutHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomBfdSessPerfEchoPktOutHC.setStatus("current")
_RaisecomBfdSessPerfEchoPktDropHC_Type = Counter64
_RaisecomBfdSessPerfEchoPktDropHC_Object = MibTableColumn
raisecomBfdSessPerfEchoPktDropHC = _RaisecomBfdSessPerfEchoPktDropHC_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 3, 1, 19),
    _RaisecomBfdSessPerfEchoPktDropHC_Type()
)
raisecomBfdSessPerfEchoPktDropHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomBfdSessPerfEchoPktDropHC.setStatus("current")
_RaisecomBfdSessDiscMapTable_Object = MibTable
raisecomBfdSessDiscMapTable = _RaisecomBfdSessDiscMapTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 4)
)
if mibBuilder.loadTexts:
    raisecomBfdSessDiscMapTable.setStatus("current")
_RaisecomBfdSessDiscMapEntry_Object = MibTableRow
raisecomBfdSessDiscMapEntry = _RaisecomBfdSessDiscMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 4, 1)
)
raisecomBfdSessDiscMapEntry.setIndexNames(
    (0, "RAISECOM-BFD-MIB", "raisecomBfdSessDiscriminator"),
)
if mibBuilder.loadTexts:
    raisecomBfdSessDiscMapEntry.setStatus("current")
_RaisecomBfdSessDiscMapIndex_Type = BfdSessIndexTC
_RaisecomBfdSessDiscMapIndex_Object = MibTableColumn
raisecomBfdSessDiscMapIndex = _RaisecomBfdSessDiscMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 4, 1, 1),
    _RaisecomBfdSessDiscMapIndex_Type()
)
raisecomBfdSessDiscMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomBfdSessDiscMapIndex.setStatus("current")
_RaisecomBfdSessIpMapTable_Object = MibTable
raisecomBfdSessIpMapTable = _RaisecomBfdSessIpMapTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 5)
)
if mibBuilder.loadTexts:
    raisecomBfdSessIpMapTable.setStatus("current")
_RaisecomBfdSessIpMapEntry_Object = MibTableRow
raisecomBfdSessIpMapEntry = _RaisecomBfdSessIpMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 5, 1)
)
raisecomBfdSessIpMapEntry.setIndexNames(
    (0, "RAISECOM-BFD-MIB", "raisecomBfdSessInterface"),
    (0, "RAISECOM-BFD-MIB", "raisecomBfdSessSrcAddrType"),
    (0, "RAISECOM-BFD-MIB", "raisecomBfdSessSrcAddr"),
    (0, "RAISECOM-BFD-MIB", "raisecomBfdSessDstAddrType"),
    (0, "RAISECOM-BFD-MIB", "raisecomBfdSessDstAddr"),
)
if mibBuilder.loadTexts:
    raisecomBfdSessIpMapEntry.setStatus("current")
_RaisecomBfdSessIpMapIndex_Type = BfdSessIndexTC
_RaisecomBfdSessIpMapIndex_Object = MibTableColumn
raisecomBfdSessIpMapIndex = _RaisecomBfdSessIpMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 5, 1, 1),
    _RaisecomBfdSessIpMapIndex_Type()
)
raisecomBfdSessIpMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomBfdSessIpMapIndex.setStatus("current")
_RaisecomBfdIfTable_Object = MibTable
raisecomBfdIfTable = _RaisecomBfdIfTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 6)
)
if mibBuilder.loadTexts:
    raisecomBfdIfTable.setStatus("current")
_RaisecomBfdIfEntry_Object = MibTableRow
raisecomBfdIfEntry = _RaisecomBfdIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 6, 1)
)
raisecomBfdIfEntry.setIndexNames(
    (0, "RAISECOM-BFD-MIB", "raisecomBfdIfIndex"),
)
if mibBuilder.loadTexts:
    raisecomBfdIfEntry.setStatus("current")
_RaisecomBfdIfIndex_Type = Unsigned32
_RaisecomBfdIfIndex_Object = MibTableColumn
raisecomBfdIfIndex = _RaisecomBfdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 6, 1, 1),
    _RaisecomBfdIfIndex_Type()
)
raisecomBfdIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomBfdIfIndex.setStatus("current")


class _RaisecomBfdIfDesiredMinTxInterval_Type(Unsigned32):
    """Custom type raisecomBfdIfDesiredMinTxInterval based on Unsigned32"""
    defaultValue = 500


_RaisecomBfdIfDesiredMinTxInterval_Type.__name__ = "Unsigned32"
_RaisecomBfdIfDesiredMinTxInterval_Object = MibTableColumn
raisecomBfdIfDesiredMinTxInterval = _RaisecomBfdIfDesiredMinTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 6, 1, 2),
    _RaisecomBfdIfDesiredMinTxInterval_Type()
)
raisecomBfdIfDesiredMinTxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomBfdIfDesiredMinTxInterval.setStatus("current")


class _RaisecomBfdIfReqMinRxInterval_Type(Unsigned32):
    """Custom type raisecomBfdIfReqMinRxInterval based on Unsigned32"""
    defaultValue = 500


_RaisecomBfdIfReqMinRxInterval_Type.__name__ = "Unsigned32"
_RaisecomBfdIfReqMinRxInterval_Object = MibTableColumn
raisecomBfdIfReqMinRxInterval = _RaisecomBfdIfReqMinRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 6, 1, 3),
    _RaisecomBfdIfReqMinRxInterval_Type()
)
raisecomBfdIfReqMinRxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomBfdIfReqMinRxInterval.setStatus("current")


class _RaisecomBfdIfDetectMult_Type(Unsigned32):
    """Custom type raisecomBfdIfDetectMult based on Unsigned32"""
    defaultValue = 3


_RaisecomBfdIfDetectMult_Type.__name__ = "Unsigned32"
_RaisecomBfdIfDetectMult_Object = MibTableColumn
raisecomBfdIfDetectMult = _RaisecomBfdIfDetectMult_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 6, 1, 4),
    _RaisecomBfdIfDetectMult_Type()
)
raisecomBfdIfDetectMult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomBfdIfDetectMult.setStatus("current")


class _RaisecomBfdIfReqMinEchoRxInterval_Type(Unsigned32):
    """Custom type raisecomBfdIfReqMinEchoRxInterval based on Unsigned32"""
    defaultValue = 500


_RaisecomBfdIfReqMinEchoRxInterval_Type.__name__ = "Unsigned32"
_RaisecomBfdIfReqMinEchoRxInterval_Object = MibTableColumn
raisecomBfdIfReqMinEchoRxInterval = _RaisecomBfdIfReqMinEchoRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 6, 1, 5),
    _RaisecomBfdIfReqMinEchoRxInterval_Type()
)
raisecomBfdIfReqMinEchoRxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomBfdIfReqMinEchoRxInterval.setStatus("current")


class _RaisecomBfdIfAuthPresFlag_Type(TruthValue):
    """Custom type raisecomBfdIfAuthPresFlag based on TruthValue"""
    defaultValue = 2


_RaisecomBfdIfAuthPresFlag_Type.__name__ = "TruthValue"
_RaisecomBfdIfAuthPresFlag_Object = MibTableColumn
raisecomBfdIfAuthPresFlag = _RaisecomBfdIfAuthPresFlag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 6, 1, 6),
    _RaisecomBfdIfAuthPresFlag_Type()
)
raisecomBfdIfAuthPresFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomBfdIfAuthPresFlag.setStatus("current")


class _RaisecomBfdIfAuthenticationType_Type(BfdSessAuthenticationTypeTC):
    """Custom type raisecomBfdIfAuthenticationType based on BfdSessAuthenticationTypeTC"""
    defaultValue = -1


_RaisecomBfdIfAuthenticationType_Type.__name__ = "BfdSessAuthenticationTypeTC"
_RaisecomBfdIfAuthenticationType_Object = MibTableColumn
raisecomBfdIfAuthenticationType = _RaisecomBfdIfAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 6, 1, 7),
    _RaisecomBfdIfAuthenticationType_Type()
)
raisecomBfdIfAuthenticationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomBfdIfAuthenticationType.setStatus("current")


class _RaisecomBfdIfAuthenticationKeyID_Type(Integer32):
    """Custom type raisecomBfdIfAuthenticationKeyID based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_RaisecomBfdIfAuthenticationKeyID_Type.__name__ = "Integer32"
_RaisecomBfdIfAuthenticationKeyID_Object = MibTableColumn
raisecomBfdIfAuthenticationKeyID = _RaisecomBfdIfAuthenticationKeyID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 6, 1, 8),
    _RaisecomBfdIfAuthenticationKeyID_Type()
)
raisecomBfdIfAuthenticationKeyID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomBfdIfAuthenticationKeyID.setStatus("current")
_RaisecomBfdIfAuthenticationKey_Type = BfdSessionAuthenticationKeyTC
_RaisecomBfdIfAuthenticationKey_Object = MibTableColumn
raisecomBfdIfAuthenticationKey = _RaisecomBfdIfAuthenticationKey_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 6, 1, 9),
    _RaisecomBfdIfAuthenticationKey_Type()
)
raisecomBfdIfAuthenticationKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomBfdIfAuthenticationKey.setStatus("current")


class _RaisecomBfdIfDemandModeDesiredFlag_Type(TruthValue):
    """Custom type raisecomBfdIfDemandModeDesiredFlag based on TruthValue"""
    defaultValue = 2


_RaisecomBfdIfDemandModeDesiredFlag_Type.__name__ = "TruthValue"
_RaisecomBfdIfDemandModeDesiredFlag_Object = MibTableColumn
raisecomBfdIfDemandModeDesiredFlag = _RaisecomBfdIfDemandModeDesiredFlag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 6, 1, 10),
    _RaisecomBfdIfDemandModeDesiredFlag_Type()
)
raisecomBfdIfDemandModeDesiredFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomBfdIfDemandModeDesiredFlag.setStatus("current")
_RaisecomBfdTemplateTable_Object = MibTable
raisecomBfdTemplateTable = _RaisecomBfdTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 7)
)
if mibBuilder.loadTexts:
    raisecomBfdTemplateTable.setStatus("current")
_RaisecomBfdTemplateEntry_Object = MibTableRow
raisecomBfdTemplateEntry = _RaisecomBfdTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 7, 1)
)
raisecomBfdTemplateEntry.setIndexNames(
    (0, "RAISECOM-BFD-MIB", "raisecomBfdTemplateName"),
)
if mibBuilder.loadTexts:
    raisecomBfdTemplateEntry.setStatus("current")


class _RaisecomBfdTemplateName_Type(OctetString):
    """Custom type raisecomBfdTemplateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RaisecomBfdTemplateName_Type.__name__ = "OctetString"
_RaisecomBfdTemplateName_Object = MibTableColumn
raisecomBfdTemplateName = _RaisecomBfdTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 7, 1, 1),
    _RaisecomBfdTemplateName_Type()
)
raisecomBfdTemplateName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomBfdTemplateName.setStatus("current")
_RaisecomBfdTemplateType_Type = BfdSessTypeTC
_RaisecomBfdTemplateType_Object = MibTableColumn
raisecomBfdTemplateType = _RaisecomBfdTemplateType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 7, 1, 2),
    _RaisecomBfdTemplateType_Type()
)
raisecomBfdTemplateType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomBfdTemplateType.setStatus("current")


class _RaisecomBfdTemplateDesiredMinTxInterval_Type(Unsigned32):
    """Custom type raisecomBfdTemplateDesiredMinTxInterval based on Unsigned32"""
    defaultValue = 500


_RaisecomBfdTemplateDesiredMinTxInterval_Type.__name__ = "Unsigned32"
_RaisecomBfdTemplateDesiredMinTxInterval_Object = MibTableColumn
raisecomBfdTemplateDesiredMinTxInterval = _RaisecomBfdTemplateDesiredMinTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 7, 1, 3),
    _RaisecomBfdTemplateDesiredMinTxInterval_Type()
)
raisecomBfdTemplateDesiredMinTxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomBfdTemplateDesiredMinTxInterval.setStatus("current")


class _RaisecomBfdTemplateReqMinRxInterval_Type(Unsigned32):
    """Custom type raisecomBfdTemplateReqMinRxInterval based on Unsigned32"""
    defaultValue = 500


_RaisecomBfdTemplateReqMinRxInterval_Type.__name__ = "Unsigned32"
_RaisecomBfdTemplateReqMinRxInterval_Object = MibTableColumn
raisecomBfdTemplateReqMinRxInterval = _RaisecomBfdTemplateReqMinRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 7, 1, 4),
    _RaisecomBfdTemplateReqMinRxInterval_Type()
)
raisecomBfdTemplateReqMinRxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomBfdTemplateReqMinRxInterval.setStatus("current")


class _RaisecomBfdTemplateDetectMult_Type(Unsigned32):
    """Custom type raisecomBfdTemplateDetectMult based on Unsigned32"""
    defaultValue = 3


_RaisecomBfdTemplateDetectMult_Type.__name__ = "Unsigned32"
_RaisecomBfdTemplateDetectMult_Object = MibTableColumn
raisecomBfdTemplateDetectMult = _RaisecomBfdTemplateDetectMult_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 7, 1, 5),
    _RaisecomBfdTemplateDetectMult_Type()
)
raisecomBfdTemplateDetectMult.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomBfdTemplateDetectMult.setStatus("current")


class _RaisecomBfdTemplateAuthPresFlag_Type(TruthValue):
    """Custom type raisecomBfdTemplateAuthPresFlag based on TruthValue"""
    defaultValue = 2


_RaisecomBfdTemplateAuthPresFlag_Type.__name__ = "TruthValue"
_RaisecomBfdTemplateAuthPresFlag_Object = MibTableColumn
raisecomBfdTemplateAuthPresFlag = _RaisecomBfdTemplateAuthPresFlag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 7, 1, 6),
    _RaisecomBfdTemplateAuthPresFlag_Type()
)
raisecomBfdTemplateAuthPresFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomBfdTemplateAuthPresFlag.setStatus("current")


class _RaisecomBfdTemplateAuthenticationType_Type(BfdSessAuthenticationTypeTC):
    """Custom type raisecomBfdTemplateAuthenticationType based on BfdSessAuthenticationTypeTC"""
    defaultValue = -1


_RaisecomBfdTemplateAuthenticationType_Type.__name__ = "BfdSessAuthenticationTypeTC"
_RaisecomBfdTemplateAuthenticationType_Object = MibTableColumn
raisecomBfdTemplateAuthenticationType = _RaisecomBfdTemplateAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 7, 1, 7),
    _RaisecomBfdTemplateAuthenticationType_Type()
)
raisecomBfdTemplateAuthenticationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomBfdTemplateAuthenticationType.setStatus("current")


class _RaisecomBfdTemplateAuthenticationKeyID_Type(Integer32):
    """Custom type raisecomBfdTemplateAuthenticationKeyID based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_RaisecomBfdTemplateAuthenticationKeyID_Type.__name__ = "Integer32"
_RaisecomBfdTemplateAuthenticationKeyID_Object = MibTableColumn
raisecomBfdTemplateAuthenticationKeyID = _RaisecomBfdTemplateAuthenticationKeyID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 7, 1, 8),
    _RaisecomBfdTemplateAuthenticationKeyID_Type()
)
raisecomBfdTemplateAuthenticationKeyID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomBfdTemplateAuthenticationKeyID.setStatus("current")
_RaisecomBfdTemplateAuthenticationKey_Type = BfdSessionAuthenticationKeyTC
_RaisecomBfdTemplateAuthenticationKey_Object = MibTableColumn
raisecomBfdTemplateAuthenticationKey = _RaisecomBfdTemplateAuthenticationKey_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 7, 1, 9),
    _RaisecomBfdTemplateAuthenticationKey_Type()
)
raisecomBfdTemplateAuthenticationKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomBfdTemplateAuthenticationKey.setStatus("current")


class _RaisecomBfdTemplateDemandModeDesiredFlag_Type(TruthValue):
    """Custom type raisecomBfdTemplateDemandModeDesiredFlag based on TruthValue"""
    defaultValue = 2


_RaisecomBfdTemplateDemandModeDesiredFlag_Type.__name__ = "TruthValue"
_RaisecomBfdTemplateDemandModeDesiredFlag_Object = MibTableColumn
raisecomBfdTemplateDemandModeDesiredFlag = _RaisecomBfdTemplateDemandModeDesiredFlag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 7, 1, 10),
    _RaisecomBfdTemplateDemandModeDesiredFlag_Type()
)
raisecomBfdTemplateDemandModeDesiredFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomBfdTemplateDemandModeDesiredFlag.setStatus("current")
_RaisecomBfdTemplateRowStatus_Type = RowStatus
_RaisecomBfdTemplateRowStatus_Object = MibTableColumn
raisecomBfdTemplateRowStatus = _RaisecomBfdTemplateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 1, 7, 1, 11),
    _RaisecomBfdTemplateRowStatus_Type()
)
raisecomBfdTemplateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomBfdTemplateRowStatus.setStatus("current")
_RaisecomBfdConformance_ObjectIdentity = ObjectIdentity
raisecomBfdConformance = _RaisecomBfdConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 2)
)
_RaisecomBfdGroups_ObjectIdentity = ObjectIdentity
raisecomBfdGroups = _RaisecomBfdGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 2, 1)
)
_RaisecomBfdCompliances_ObjectIdentity = ObjectIdentity
raisecomBfdCompliances = _RaisecomBfdCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 2, 2)
)
raisecomBfdSessEntry.registerAugmentions(
    ("RAISECOM-BFD-MIB",
     "raisecomBfdSessPerfEntry")
)
raisecomBfdSessPerfEntry.setIndexNames(*raisecomBfdSessEntry.getIndexNames())

# Managed Objects groups


# Notification objects

raisecomBfdSessUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 0, 1)
)
raisecomBfdSessUp.setObjects(
      *(("RAISECOM-BFD-MIB", "raisecomBfdSessDiag"),
        ("RAISECOM-BFD-MIB", "raisecomBfdSessDiag"))
)
if mibBuilder.loadTexts:
    raisecomBfdSessUp.setStatus(
        "current"
    )

raisecomBfdSessDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 35, 0, 2)
)
raisecomBfdSessDown.setObjects(
      *(("RAISECOM-BFD-MIB", "raisecomBfdSessDiag"),
        ("RAISECOM-BFD-MIB", "raisecomBfdSessDiag"))
)
if mibBuilder.loadTexts:
    raisecomBfdSessDown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-BFD-MIB",
    **{"BfdSessIndexTC": BfdSessIndexTC,
       "BfdIntervalTC": BfdIntervalTC,
       "BfdMultiplierTC": BfdMultiplierTC,
       "BfdDiagTC": BfdDiagTC,
       "BfdSessTypeTC": BfdSessTypeTC,
       "BfdSessOperModeTC": BfdSessOperModeTC,
       "BfdCtrlDestPortNumberTC": BfdCtrlDestPortNumberTC,
       "BfdCtrlSourcePortNumberTC": BfdCtrlSourcePortNumberTC,
       "BfdSessStateTC": BfdSessStateTC,
       "BfdSessAuthenticationTypeTC": BfdSessAuthenticationTypeTC,
       "BfdSessionAuthenticationKeyTC": BfdSessionAuthenticationKeyTC,
       "raisecomBfd": raisecomBfd,
       "raisecomBfdNotifications": raisecomBfdNotifications,
       "raisecomBfdSessUp": raisecomBfdSessUp,
       "raisecomBfdSessDown": raisecomBfdSessDown,
       "raisecomBfdObjects": raisecomBfdObjects,
       "raisecomBfdScalarObjects": raisecomBfdScalarObjects,
       "raisecomBfdAdminStatus": raisecomBfdAdminStatus,
       "raisecomBfdSessNotificationsEnable": raisecomBfdSessNotificationsEnable,
       "raisecomBfdRoleMode": raisecomBfdRoleMode,
       "raisecomBfdEchoSourceIpType": raisecomBfdEchoSourceIpType,
       "raisecomBfdEchoSourceIpAddr": raisecomBfdEchoSourceIpAddr,
       "raisecomBfdAllSessionsStatisticsClear": raisecomBfdAllSessionsStatisticsClear,
       "raisecomBfdSessTable": raisecomBfdSessTable,
       "raisecomBfdSessEntry": raisecomBfdSessEntry,
       "raisecomBfdSessIndex": raisecomBfdSessIndex,
       "raisecomBfdSessVersionNumber": raisecomBfdSessVersionNumber,
       "raisecomBfdSessType": raisecomBfdSessType,
       "raisecomBfdSessDiscriminator": raisecomBfdSessDiscriminator,
       "raisecomBfdSessRemoteDiscr": raisecomBfdSessRemoteDiscr,
       "raisecomBfdSessDestinationUdpPort": raisecomBfdSessDestinationUdpPort,
       "raisecomBfdSessSourceUdpPort": raisecomBfdSessSourceUdpPort,
       "raisecomBfdSessEchoSourceUdpPort": raisecomBfdSessEchoSourceUdpPort,
       "raisecomBfdSessAdminStatus": raisecomBfdSessAdminStatus,
       "raisecomBfdSessState": raisecomBfdSessState,
       "raisecomBfdSessRemoteHeardFlag": raisecomBfdSessRemoteHeardFlag,
       "raisecomBfdSessDiag": raisecomBfdSessDiag,
       "raisecomBfdSessOperMode": raisecomBfdSessOperMode,
       "raisecomBfdSessDemandModeDesiredFlag": raisecomBfdSessDemandModeDesiredFlag,
       "raisecomBfdSessControlPlaneIndepFlag": raisecomBfdSessControlPlaneIndepFlag,
       "raisecomBfdSessMultipointFlag": raisecomBfdSessMultipointFlag,
       "raisecomBfdSessInterface": raisecomBfdSessInterface,
       "raisecomBfdSessSrcAddrType": raisecomBfdSessSrcAddrType,
       "raisecomBfdSessSrcAddr": raisecomBfdSessSrcAddr,
       "raisecomBfdSessDstAddrType": raisecomBfdSessDstAddrType,
       "raisecomBfdSessDstAddr": raisecomBfdSessDstAddr,
       "raisecomBfdSessGTSM": raisecomBfdSessGTSM,
       "raisecomBfdSessGTSMTTL": raisecomBfdSessGTSMTTL,
       "raisecomBfdSessDesiredMinTxInterval": raisecomBfdSessDesiredMinTxInterval,
       "raisecomBfdSessReqMinRxInterval": raisecomBfdSessReqMinRxInterval,
       "raisecomBfdSessReqMinEchoRxInterval": raisecomBfdSessReqMinEchoRxInterval,
       "raisecomBfdSessDetectMult": raisecomBfdSessDetectMult,
       "raisecomBfdSessNegotiatedInterval": raisecomBfdSessNegotiatedInterval,
       "raisecomBfdSessNegotiatedEchoInterval": raisecomBfdSessNegotiatedEchoInterval,
       "raisecomBfdSessNegotiatedDetectMult": raisecomBfdSessNegotiatedDetectMult,
       "raisecomBfdSessAuthPresFlag": raisecomBfdSessAuthPresFlag,
       "raisecomBfdSessAuthenticationType": raisecomBfdSessAuthenticationType,
       "raisecomBfdSessAuthenticationKeyID": raisecomBfdSessAuthenticationKeyID,
       "raisecomBfdSessAuthenticationKey": raisecomBfdSessAuthenticationKey,
       "raisecomBfdSessStorType": raisecomBfdSessStorType,
       "raisecomBfdSessRowStatus": raisecomBfdSessRowStatus,
       "raisecomBfdSessTemplateName": raisecomBfdSessTemplateName,
       "raisecomBfdSessPerfTable": raisecomBfdSessPerfTable,
       "raisecomBfdSessPerfEntry": raisecomBfdSessPerfEntry,
       "raisecomBfdSessPerfCtrlPktIn": raisecomBfdSessPerfCtrlPktIn,
       "raisecomBfdSessPerfCtrlPktOut": raisecomBfdSessPerfCtrlPktOut,
       "raisecomBfdSessPerfCtrlPktDrop": raisecomBfdSessPerfCtrlPktDrop,
       "raisecomBfdSessPerfCtrlPktDropLastTime": raisecomBfdSessPerfCtrlPktDropLastTime,
       "raisecomBfdSessPerfEchoPktIn": raisecomBfdSessPerfEchoPktIn,
       "raisecomBfdSessPerfEchoPktOut": raisecomBfdSessPerfEchoPktOut,
       "raisecomBfdSessPerfEchoPktDrop": raisecomBfdSessPerfEchoPktDrop,
       "raisecomBfdSessPerfEchoPktDropLastTime": raisecomBfdSessPerfEchoPktDropLastTime,
       "raisecomBfdSessUpTime": raisecomBfdSessUpTime,
       "raisecomBfdSessPerfLastSessDownTime": raisecomBfdSessPerfLastSessDownTime,
       "raisecomBfdSessPerfLastCommLostDiag": raisecomBfdSessPerfLastCommLostDiag,
       "raisecomBfdSessPerfSessUpCount": raisecomBfdSessPerfSessUpCount,
       "raisecomBfdSessPerfDiscTime": raisecomBfdSessPerfDiscTime,
       "raisecomBfdSessPerfCtrlPktInHC": raisecomBfdSessPerfCtrlPktInHC,
       "raisecomBfdSessPerfCtrlPktOutHC": raisecomBfdSessPerfCtrlPktOutHC,
       "raisecomBfdSessPerfCtrlPktDropHC": raisecomBfdSessPerfCtrlPktDropHC,
       "raisecomBfdSessPerfEchoPktInHC": raisecomBfdSessPerfEchoPktInHC,
       "raisecomBfdSessPerfEchoPktOutHC": raisecomBfdSessPerfEchoPktOutHC,
       "raisecomBfdSessPerfEchoPktDropHC": raisecomBfdSessPerfEchoPktDropHC,
       "raisecomBfdSessDiscMapTable": raisecomBfdSessDiscMapTable,
       "raisecomBfdSessDiscMapEntry": raisecomBfdSessDiscMapEntry,
       "raisecomBfdSessDiscMapIndex": raisecomBfdSessDiscMapIndex,
       "raisecomBfdSessIpMapTable": raisecomBfdSessIpMapTable,
       "raisecomBfdSessIpMapEntry": raisecomBfdSessIpMapEntry,
       "raisecomBfdSessIpMapIndex": raisecomBfdSessIpMapIndex,
       "raisecomBfdIfTable": raisecomBfdIfTable,
       "raisecomBfdIfEntry": raisecomBfdIfEntry,
       "raisecomBfdIfIndex": raisecomBfdIfIndex,
       "raisecomBfdIfDesiredMinTxInterval": raisecomBfdIfDesiredMinTxInterval,
       "raisecomBfdIfReqMinRxInterval": raisecomBfdIfReqMinRxInterval,
       "raisecomBfdIfDetectMult": raisecomBfdIfDetectMult,
       "raisecomBfdIfReqMinEchoRxInterval": raisecomBfdIfReqMinEchoRxInterval,
       "raisecomBfdIfAuthPresFlag": raisecomBfdIfAuthPresFlag,
       "raisecomBfdIfAuthenticationType": raisecomBfdIfAuthenticationType,
       "raisecomBfdIfAuthenticationKeyID": raisecomBfdIfAuthenticationKeyID,
       "raisecomBfdIfAuthenticationKey": raisecomBfdIfAuthenticationKey,
       "raisecomBfdIfDemandModeDesiredFlag": raisecomBfdIfDemandModeDesiredFlag,
       "raisecomBfdTemplateTable": raisecomBfdTemplateTable,
       "raisecomBfdTemplateEntry": raisecomBfdTemplateEntry,
       "raisecomBfdTemplateName": raisecomBfdTemplateName,
       "raisecomBfdTemplateType": raisecomBfdTemplateType,
       "raisecomBfdTemplateDesiredMinTxInterval": raisecomBfdTemplateDesiredMinTxInterval,
       "raisecomBfdTemplateReqMinRxInterval": raisecomBfdTemplateReqMinRxInterval,
       "raisecomBfdTemplateDetectMult": raisecomBfdTemplateDetectMult,
       "raisecomBfdTemplateAuthPresFlag": raisecomBfdTemplateAuthPresFlag,
       "raisecomBfdTemplateAuthenticationType": raisecomBfdTemplateAuthenticationType,
       "raisecomBfdTemplateAuthenticationKeyID": raisecomBfdTemplateAuthenticationKeyID,
       "raisecomBfdTemplateAuthenticationKey": raisecomBfdTemplateAuthenticationKey,
       "raisecomBfdTemplateDemandModeDesiredFlag": raisecomBfdTemplateDemandModeDesiredFlag,
       "raisecomBfdTemplateRowStatus": raisecomBfdTemplateRowStatus,
       "raisecomBfdConformance": raisecomBfdConformance,
       "raisecomBfdGroups": raisecomBfdGroups,
       "raisecomBfdCompliances": raisecomBfdCompliances}
)
