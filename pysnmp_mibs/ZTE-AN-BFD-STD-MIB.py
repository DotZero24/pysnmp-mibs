# SNMP MIB module (ZTE-AN-BFD-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-BFD-STD-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:09 2025
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

(zxAn,) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "zxAn")


# MODULE-IDENTITY

zxAnBfdStdMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16)
)
if mibBuilder.loadTexts:
    zxAnBfdStdMib.setRevisions(
        ("2010-03-03 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ZxAnBfdStdSessIndexTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class ZxAnBfdStdInterval(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class ZxAnBfdStdMultiplier(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class ZxAnBfdStdDiag(TextualConvention, Integer32):
    status = "current"
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("controlDetectionTimeExpired", 1),
          ("echoFunctionFailed", 2),
          ("neighborSignaledSessionDown", 3),
          ("forwardingPlaneReset", 4),
          ("pathDown", 5),
          ("concatenatedPathDown", 6),
          ("administrativelyDown", 7),
          ("reverseConcatenatedPathDown", 8),
          ("noDiagnostic", 99))
    )



# MIB Managed Objects in the order of their OIDs

_ZxAnBfdStdNotifications_ObjectIdentity = ObjectIdentity
zxAnBfdStdNotifications = _ZxAnBfdStdNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 0)
)
_ZxAnBfdStdObjects_ObjectIdentity = ObjectIdentity
zxAnBfdStdObjects = _ZxAnBfdStdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1)
)
_ZxAnBfdStdGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnBfdStdGlobalObjects = _ZxAnBfdStdGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 1)
)


class _ZxAnBfdStdAdminStatus_Type(Integer32):
    """Custom type zxAnBfdStdAdminStatus based on Integer32"""
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


_ZxAnBfdStdAdminStatus_Type.__name__ = "Integer32"
_ZxAnBfdStdAdminStatus_Object = MibScalar
zxAnBfdStdAdminStatus = _ZxAnBfdStdAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 1, 1),
    _ZxAnBfdStdAdminStatus_Type()
)
zxAnBfdStdAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnBfdStdAdminStatus.setStatus("current")


class _ZxAnBfdStdSessTrapsEnable_Type(TruthValue):
    """Custom type zxAnBfdStdSessTrapsEnable based on TruthValue"""
    defaultValue = 2


_ZxAnBfdStdSessTrapsEnable_Type.__name__ = "TruthValue"
_ZxAnBfdStdSessTrapsEnable_Object = MibScalar
zxAnBfdStdSessTrapsEnable = _ZxAnBfdStdSessTrapsEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 1, 2),
    _ZxAnBfdStdSessTrapsEnable_Type()
)
zxAnBfdStdSessTrapsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnBfdStdSessTrapsEnable.setStatus("current")
_ZxAnBfdStdSessTable_Object = MibTable
zxAnBfdStdSessTable = _ZxAnBfdStdSessTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 2)
)
if mibBuilder.loadTexts:
    zxAnBfdStdSessTable.setStatus("current")
_ZxAnBfdStdSessEntry_Object = MibTableRow
zxAnBfdStdSessEntry = _ZxAnBfdStdSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 2, 1)
)
zxAnBfdStdSessEntry.setIndexNames(
    (0, "ZTE-AN-BFD-STD-MIB", "zxAnBfdStdSessIndex"),
)
if mibBuilder.loadTexts:
    zxAnBfdStdSessEntry.setStatus("current")
_ZxAnBfdStdSessIndex_Type = ZxAnBfdStdSessIndexTC
_ZxAnBfdStdSessIndex_Object = MibTableColumn
zxAnBfdStdSessIndex = _ZxAnBfdStdSessIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 2, 1, 1),
    _ZxAnBfdStdSessIndex_Type()
)
zxAnBfdStdSessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnBfdStdSessIndex.setStatus("current")


class _ZxAnBfdStdSessVersionNumber_Type(Unsigned32):
    """Custom type zxAnBfdStdSessVersionNumber based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnBfdStdSessVersionNumber_Type.__name__ = "Unsigned32"
_ZxAnBfdStdSessVersionNumber_Object = MibTableColumn
zxAnBfdStdSessVersionNumber = _ZxAnBfdStdSessVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 2, 1, 2),
    _ZxAnBfdStdSessVersionNumber_Type()
)
zxAnBfdStdSessVersionNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBfdStdSessVersionNumber.setStatus("current")


class _ZxAnBfdStdSessType_Type(Integer32):
    """Custom type zxAnBfdStdSessType based on Integer32"""
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
        *(("singleHop", 1),
          ("multiHopTotallyArbitraryPaths", 2),
          ("multiHopOutOfBandSignaling", 3),
          ("multiHopUnidirectionalLinks", 4))
    )


_ZxAnBfdStdSessType_Type.__name__ = "Integer32"
_ZxAnBfdStdSessType_Object = MibTableColumn
zxAnBfdStdSessType = _ZxAnBfdStdSessType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 2, 1, 3),
    _ZxAnBfdStdSessType_Type()
)
zxAnBfdStdSessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdStdSessType.setStatus("current")


class _ZxAnBfdStdSessMHopUniLinkMode_Type(Integer32):
    """Custom type zxAnBfdStdSessMHopUniLinkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("active", 2),
          ("passive", 3))
    )


_ZxAnBfdStdSessMHopUniLinkMode_Type.__name__ = "Integer32"
_ZxAnBfdStdSessMHopUniLinkMode_Object = MibTableColumn
zxAnBfdStdSessMHopUniLinkMode = _ZxAnBfdStdSessMHopUniLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 2, 1, 4),
    _ZxAnBfdStdSessMHopUniLinkMode_Type()
)
zxAnBfdStdSessMHopUniLinkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdStdSessMHopUniLinkMode.setStatus("current")


class _ZxAnBfdStdSessDiscriminator_Type(Unsigned32):
    """Custom type zxAnBfdStdSessDiscriminator based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ZxAnBfdStdSessDiscriminator_Type.__name__ = "Unsigned32"
_ZxAnBfdStdSessDiscriminator_Object = MibTableColumn
zxAnBfdStdSessDiscriminator = _ZxAnBfdStdSessDiscriminator_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 2, 1, 5),
    _ZxAnBfdStdSessDiscriminator_Type()
)
zxAnBfdStdSessDiscriminator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdStdSessDiscriminator.setStatus("current")


class _ZxAnBfdStdSessRemoteDiscr_Type(Unsigned32):
    """Custom type zxAnBfdStdSessRemoteDiscr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_ZxAnBfdStdSessRemoteDiscr_Type.__name__ = "Unsigned32"
_ZxAnBfdStdSessRemoteDiscr_Object = MibTableColumn
zxAnBfdStdSessRemoteDiscr = _ZxAnBfdStdSessRemoteDiscr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 2, 1, 6),
    _ZxAnBfdStdSessRemoteDiscr_Type()
)
zxAnBfdStdSessRemoteDiscr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdStdSessRemoteDiscr.setStatus("current")


class _ZxAnBfdStdSessDestinationUdpPort_Type(InetPortNumber):
    """Custom type zxAnBfdStdSessDestinationUdpPort based on InetPortNumber"""
    defaultValue = 0


_ZxAnBfdStdSessDestinationUdpPort_Type.__name__ = "InetPortNumber"
_ZxAnBfdStdSessDestinationUdpPort_Object = MibTableColumn
zxAnBfdStdSessDestinationUdpPort = _ZxAnBfdStdSessDestinationUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 2, 1, 7),
    _ZxAnBfdStdSessDestinationUdpPort_Type()
)
zxAnBfdStdSessDestinationUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdStdSessDestinationUdpPort.setStatus("current")


class _ZxAnBfdStdSessSourceUdpPort_Type(InetPortNumber):
    """Custom type zxAnBfdStdSessSourceUdpPort based on InetPortNumber"""
    defaultValue = 0


_ZxAnBfdStdSessSourceUdpPort_Type.__name__ = "InetPortNumber"
_ZxAnBfdStdSessSourceUdpPort_Object = MibTableColumn
zxAnBfdStdSessSourceUdpPort = _ZxAnBfdStdSessSourceUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 2, 1, 8),
    _ZxAnBfdStdSessSourceUdpPort_Type()
)
zxAnBfdStdSessSourceUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBfdStdSessSourceUdpPort.setStatus("current")


class _ZxAnBfdStdSessEchoSourceUdpPort_Type(InetPortNumber):
    """Custom type zxAnBfdStdSessEchoSourceUdpPort based on InetPortNumber"""
    defaultValue = 0


_ZxAnBfdStdSessEchoSourceUdpPort_Type.__name__ = "InetPortNumber"
_ZxAnBfdStdSessEchoSourceUdpPort_Object = MibTableColumn
zxAnBfdStdSessEchoSourceUdpPort = _ZxAnBfdStdSessEchoSourceUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 2, 1, 9),
    _ZxAnBfdStdSessEchoSourceUdpPort_Type()
)
zxAnBfdStdSessEchoSourceUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBfdStdSessEchoSourceUdpPort.setStatus("current")


class _ZxAnBfdStdSessAdminStatus_Type(Integer32):
    """Custom type zxAnBfdStdSessAdminStatus based on Integer32"""
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


_ZxAnBfdStdSessAdminStatus_Type.__name__ = "Integer32"
_ZxAnBfdStdSessAdminStatus_Object = MibTableColumn
zxAnBfdStdSessAdminStatus = _ZxAnBfdStdSessAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 2, 1, 10),
    _ZxAnBfdStdSessAdminStatus_Type()
)
zxAnBfdStdSessAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBfdStdSessAdminStatus.setStatus("current")


class _ZxAnBfdStdSessState_Type(Integer32):
    """Custom type zxAnBfdStdSessState based on Integer32"""
    defaultValue = 2

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


_ZxAnBfdStdSessState_Type.__name__ = "Integer32"
_ZxAnBfdStdSessState_Object = MibTableColumn
zxAnBfdStdSessState = _ZxAnBfdStdSessState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 2, 1, 11),
    _ZxAnBfdStdSessState_Type()
)
zxAnBfdStdSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdStdSessState.setStatus("current")


class _ZxAnBfdStdSessRemoteHeardFlag_Type(TruthValue):
    """Custom type zxAnBfdStdSessRemoteHeardFlag based on TruthValue"""
    defaultValue = 2


_ZxAnBfdStdSessRemoteHeardFlag_Type.__name__ = "TruthValue"
_ZxAnBfdStdSessRemoteHeardFlag_Object = MibTableColumn
zxAnBfdStdSessRemoteHeardFlag = _ZxAnBfdStdSessRemoteHeardFlag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 2, 1, 12),
    _ZxAnBfdStdSessRemoteHeardFlag_Type()
)
zxAnBfdStdSessRemoteHeardFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdStdSessRemoteHeardFlag.setStatus("current")
_ZxAnBfdStdSessDiag_Type = ZxAnBfdStdDiag
_ZxAnBfdStdSessDiag_Object = MibTableColumn
zxAnBfdStdSessDiag = _ZxAnBfdStdSessDiag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 2, 1, 13),
    _ZxAnBfdStdSessDiag_Type()
)
zxAnBfdStdSessDiag.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zxAnBfdStdSessDiag.setStatus("current")


class _ZxAnBfdStdSessOperMode_Type(Integer32):
    """Custom type zxAnBfdStdSessOperMode based on Integer32"""
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


_ZxAnBfdStdSessOperMode_Type.__name__ = "Integer32"
_ZxAnBfdStdSessOperMode_Object = MibTableColumn
zxAnBfdStdSessOperMode = _ZxAnBfdStdSessOperMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 2, 1, 14),
    _ZxAnBfdStdSessOperMode_Type()
)
zxAnBfdStdSessOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdStdSessOperMode.setStatus("current")


class _ZxAnBfdStdSessDesiredDmdMode_Type(TruthValue):
    """Custom type zxAnBfdStdSessDesiredDmdMode based on TruthValue"""
    defaultValue = 2


_ZxAnBfdStdSessDesiredDmdMode_Type.__name__ = "TruthValue"
_ZxAnBfdStdSessDesiredDmdMode_Object = MibTableColumn
zxAnBfdStdSessDesiredDmdMode = _ZxAnBfdStdSessDesiredDmdMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 2, 1, 15),
    _ZxAnBfdStdSessDesiredDmdMode_Type()
)
zxAnBfdStdSessDesiredDmdMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBfdStdSessDesiredDmdMode.setStatus("current")


class _ZxAnBfdStdSessCtrlPlaneIndep_Type(TruthValue):
    """Custom type zxAnBfdStdSessCtrlPlaneIndep based on TruthValue"""
    defaultValue = 2


_ZxAnBfdStdSessCtrlPlaneIndep_Type.__name__ = "TruthValue"
_ZxAnBfdStdSessCtrlPlaneIndep_Object = MibTableColumn
zxAnBfdStdSessCtrlPlaneIndep = _ZxAnBfdStdSessCtrlPlaneIndep_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 2, 1, 16),
    _ZxAnBfdStdSessCtrlPlaneIndep_Type()
)
zxAnBfdStdSessCtrlPlaneIndep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdStdSessCtrlPlaneIndep.setStatus("current")


class _ZxAnBfdStdSessMultipointFlag_Type(TruthValue):
    """Custom type zxAnBfdStdSessMultipointFlag based on TruthValue"""
    defaultValue = 2


_ZxAnBfdStdSessMultipointFlag_Type.__name__ = "TruthValue"
_ZxAnBfdStdSessMultipointFlag_Object = MibTableColumn
zxAnBfdStdSessMultipointFlag = _ZxAnBfdStdSessMultipointFlag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 2, 1, 17),
    _ZxAnBfdStdSessMultipointFlag_Type()
)
zxAnBfdStdSessMultipointFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdStdSessMultipointFlag.setStatus("current")
_ZxAnBfdStdSessInterface_Type = InterfaceIndexOrZero
_ZxAnBfdStdSessInterface_Object = MibTableColumn
zxAnBfdStdSessInterface = _ZxAnBfdStdSessInterface_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 2, 1, 18),
    _ZxAnBfdStdSessInterface_Type()
)
zxAnBfdStdSessInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBfdStdSessInterface.setStatus("current")
_ZxAnBfdStdSessPeerIpAddrType_Type = InetAddressType
_ZxAnBfdStdSessPeerIpAddrType_Object = MibTableColumn
zxAnBfdStdSessPeerIpAddrType = _ZxAnBfdStdSessPeerIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 2, 1, 19),
    _ZxAnBfdStdSessPeerIpAddrType_Type()
)
zxAnBfdStdSessPeerIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBfdStdSessPeerIpAddrType.setStatus("current")
_ZxAnBfdStdSessPeerIpAddr_Type = InetAddress
_ZxAnBfdStdSessPeerIpAddr_Object = MibTableColumn
zxAnBfdStdSessPeerIpAddr = _ZxAnBfdStdSessPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 2, 1, 20),
    _ZxAnBfdStdSessPeerIpAddr_Type()
)
zxAnBfdStdSessPeerIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBfdStdSessPeerIpAddr.setStatus("current")


class _ZxAnBfdStdSessGTSM_Type(TruthValue):
    """Custom type zxAnBfdStdSessGTSM based on TruthValue"""
    defaultValue = 2


_ZxAnBfdStdSessGTSM_Type.__name__ = "TruthValue"
_ZxAnBfdStdSessGTSM_Object = MibTableColumn
zxAnBfdStdSessGTSM = _ZxAnBfdStdSessGTSM_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 2, 1, 21),
    _ZxAnBfdStdSessGTSM_Type()
)
zxAnBfdStdSessGTSM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBfdStdSessGTSM.setStatus("current")


class _ZxAnBfdStdSessGTSMTTL_Type(Unsigned32):
    """Custom type zxAnBfdStdSessGTSMTTL based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnBfdStdSessGTSMTTL_Type.__name__ = "Unsigned32"
_ZxAnBfdStdSessGTSMTTL_Object = MibTableColumn
zxAnBfdStdSessGTSMTTL = _ZxAnBfdStdSessGTSMTTL_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 2, 1, 22),
    _ZxAnBfdStdSessGTSMTTL_Type()
)
zxAnBfdStdSessGTSMTTL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBfdStdSessGTSMTTL.setStatus("current")
_ZxAnBfdStdSessDesiredMinTxIntv_Type = ZxAnBfdStdInterval
_ZxAnBfdStdSessDesiredMinTxIntv_Object = MibTableColumn
zxAnBfdStdSessDesiredMinTxIntv = _ZxAnBfdStdSessDesiredMinTxIntv_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 2, 1, 23),
    _ZxAnBfdStdSessDesiredMinTxIntv_Type()
)
zxAnBfdStdSessDesiredMinTxIntv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBfdStdSessDesiredMinTxIntv.setStatus("current")
_ZxAnBfdStdSessReqMinRxIntv_Type = ZxAnBfdStdInterval
_ZxAnBfdStdSessReqMinRxIntv_Object = MibTableColumn
zxAnBfdStdSessReqMinRxIntv = _ZxAnBfdStdSessReqMinRxIntv_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 2, 1, 24),
    _ZxAnBfdStdSessReqMinRxIntv_Type()
)
zxAnBfdStdSessReqMinRxIntv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBfdStdSessReqMinRxIntv.setStatus("current")
_ZxAnBfdStdSessReqMinEchoRxIntv_Type = ZxAnBfdStdInterval
_ZxAnBfdStdSessReqMinEchoRxIntv_Object = MibTableColumn
zxAnBfdStdSessReqMinEchoRxIntv = _ZxAnBfdStdSessReqMinEchoRxIntv_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 2, 1, 25),
    _ZxAnBfdStdSessReqMinEchoRxIntv_Type()
)
zxAnBfdStdSessReqMinEchoRxIntv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBfdStdSessReqMinEchoRxIntv.setStatus("current")
_ZxAnBfdStdSessDetectMult_Type = ZxAnBfdStdMultiplier
_ZxAnBfdStdSessDetectMult_Object = MibTableColumn
zxAnBfdStdSessDetectMult = _ZxAnBfdStdSessDetectMult_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 2, 1, 26),
    _ZxAnBfdStdSessDetectMult_Type()
)
zxAnBfdStdSessDetectMult.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBfdStdSessDetectMult.setStatus("current")
_ZxAnBfdStdSessNegInterval_Type = ZxAnBfdStdInterval
_ZxAnBfdStdSessNegInterval_Object = MibTableColumn
zxAnBfdStdSessNegInterval = _ZxAnBfdStdSessNegInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 2, 1, 27),
    _ZxAnBfdStdSessNegInterval_Type()
)
zxAnBfdStdSessNegInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdStdSessNegInterval.setStatus("current")
_ZxAnBfdStdSessNegEchoInterval_Type = ZxAnBfdStdInterval
_ZxAnBfdStdSessNegEchoInterval_Object = MibTableColumn
zxAnBfdStdSessNegEchoInterval = _ZxAnBfdStdSessNegEchoInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 2, 1, 28),
    _ZxAnBfdStdSessNegEchoInterval_Type()
)
zxAnBfdStdSessNegEchoInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdStdSessNegEchoInterval.setStatus("current")
_ZxAnBfdStdSessNegDetectMult_Type = ZxAnBfdStdMultiplier
_ZxAnBfdStdSessNegDetectMult_Object = MibTableColumn
zxAnBfdStdSessNegDetectMult = _ZxAnBfdStdSessNegDetectMult_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 2, 1, 29),
    _ZxAnBfdStdSessNegDetectMult_Type()
)
zxAnBfdStdSessNegDetectMult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdStdSessNegDetectMult.setStatus("current")


class _ZxAnBfdStdSessAuthPresFlag_Type(TruthValue):
    """Custom type zxAnBfdStdSessAuthPresFlag based on TruthValue"""
    defaultValue = 2


_ZxAnBfdStdSessAuthPresFlag_Type.__name__ = "TruthValue"
_ZxAnBfdStdSessAuthPresFlag_Object = MibTableColumn
zxAnBfdStdSessAuthPresFlag = _ZxAnBfdStdSessAuthPresFlag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 2, 1, 30),
    _ZxAnBfdStdSessAuthPresFlag_Type()
)
zxAnBfdStdSessAuthPresFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdStdSessAuthPresFlag.setStatus("current")


class _ZxAnBfdStdSessAuthType_Type(Integer32):
    """Custom type zxAnBfdStdSessAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              99)
        )
    )
    namedValues = NamedValues(
        *(("simplePassword", 1),
          ("keyedMD5", 2),
          ("meticulousKeyedMD5", 3),
          ("keyedSHA1", 4),
          ("meticulousKeyedSHA1", 5),
          ("reserved", 99))
    )


_ZxAnBfdStdSessAuthType_Type.__name__ = "Integer32"
_ZxAnBfdStdSessAuthType_Object = MibTableColumn
zxAnBfdStdSessAuthType = _ZxAnBfdStdSessAuthType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 2, 1, 31),
    _ZxAnBfdStdSessAuthType_Type()
)
zxAnBfdStdSessAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBfdStdSessAuthType.setStatus("current")


class _ZxAnBfdStdSessAuthKeyID_Type(Integer32):
    """Custom type zxAnBfdStdSessAuthKeyID based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_ZxAnBfdStdSessAuthKeyID_Type.__name__ = "Integer32"
_ZxAnBfdStdSessAuthKeyID_Object = MibTableColumn
zxAnBfdStdSessAuthKeyID = _ZxAnBfdStdSessAuthKeyID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 2, 1, 32),
    _ZxAnBfdStdSessAuthKeyID_Type()
)
zxAnBfdStdSessAuthKeyID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBfdStdSessAuthKeyID.setStatus("current")


class _ZxAnBfdStdSessAuthKey_Type(OctetString):
    """Custom type zxAnBfdStdSessAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 252),
    )


_ZxAnBfdStdSessAuthKey_Type.__name__ = "OctetString"
_ZxAnBfdStdSessAuthKey_Object = MibTableColumn
zxAnBfdStdSessAuthKey = _ZxAnBfdStdSessAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 2, 1, 33),
    _ZxAnBfdStdSessAuthKey_Type()
)
zxAnBfdStdSessAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBfdStdSessAuthKey.setStatus("current")
_ZxAnBfdStdSessIpAddrType_Type = InetAddressType
_ZxAnBfdStdSessIpAddrType_Object = MibTableColumn
zxAnBfdStdSessIpAddrType = _ZxAnBfdStdSessIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 2, 1, 34),
    _ZxAnBfdStdSessIpAddrType_Type()
)
zxAnBfdStdSessIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBfdStdSessIpAddrType.setStatus("current")
_ZxAnBfdStdSessIpAddr_Type = InetAddress
_ZxAnBfdStdSessIpAddr_Object = MibTableColumn
zxAnBfdStdSessIpAddr = _ZxAnBfdStdSessIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 2, 1, 35),
    _ZxAnBfdStdSessIpAddr_Type()
)
zxAnBfdStdSessIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBfdStdSessIpAddr.setStatus("current")


class _ZxAnBfdStdSessAppType_Type(Integer32):
    """Custom type zxAnBfdStdSessAppType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128,
              256,
              512,
              1024,
              2048)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 1),
          ("ospf", 2),
          ("isis", 4),
          ("rsvp", 8),
          ("ldp", 16),
          ("static", 32),
          ("rsvpLsp", 64),
          ("ldpLsp", 128),
          ("vrrp", 256),
          ("pbr", 512),
          ("pw", 1024),
          ("pim", 2048))
    )


_ZxAnBfdStdSessAppType_Type.__name__ = "Integer32"
_ZxAnBfdStdSessAppType_Object = MibTableColumn
zxAnBfdStdSessAppType = _ZxAnBfdStdSessAppType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 2, 1, 36),
    _ZxAnBfdStdSessAppType_Type()
)
zxAnBfdStdSessAppType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBfdStdSessAppType.setStatus("current")
_ZxAnBfdStdSessStorType_Type = StorageType
_ZxAnBfdStdSessStorType_Object = MibTableColumn
zxAnBfdStdSessStorType = _ZxAnBfdStdSessStorType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 2, 1, 60),
    _ZxAnBfdStdSessStorType_Type()
)
zxAnBfdStdSessStorType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBfdStdSessStorType.setStatus("current")
_ZxAnBfdStdSessRowStatus_Type = RowStatus
_ZxAnBfdStdSessRowStatus_Object = MibTableColumn
zxAnBfdStdSessRowStatus = _ZxAnBfdStdSessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 2, 1, 61),
    _ZxAnBfdStdSessRowStatus_Type()
)
zxAnBfdStdSessRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBfdStdSessRowStatus.setStatus("current")
_ZxAnBfdStdSessPerfTable_Object = MibTable
zxAnBfdStdSessPerfTable = _ZxAnBfdStdSessPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 3)
)
if mibBuilder.loadTexts:
    zxAnBfdStdSessPerfTable.setStatus("current")
_ZxAnBfdStdSessPerfEntry_Object = MibTableRow
zxAnBfdStdSessPerfEntry = _ZxAnBfdStdSessPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 3, 1)
)
if mibBuilder.loadTexts:
    zxAnBfdStdSessPerfEntry.setStatus("current")
_ZxAnBfdStdSessPerfCtrlPktIn_Type = Counter32
_ZxAnBfdStdSessPerfCtrlPktIn_Object = MibTableColumn
zxAnBfdStdSessPerfCtrlPktIn = _ZxAnBfdStdSessPerfCtrlPktIn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 3, 1, 1),
    _ZxAnBfdStdSessPerfCtrlPktIn_Type()
)
zxAnBfdStdSessPerfCtrlPktIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdStdSessPerfCtrlPktIn.setStatus("current")
_ZxAnBfdStdSessPerfCtrlPktOut_Type = Counter32
_ZxAnBfdStdSessPerfCtrlPktOut_Object = MibTableColumn
zxAnBfdStdSessPerfCtrlPktOut = _ZxAnBfdStdSessPerfCtrlPktOut_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 3, 1, 2),
    _ZxAnBfdStdSessPerfCtrlPktOut_Type()
)
zxAnBfdStdSessPerfCtrlPktOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdStdSessPerfCtrlPktOut.setStatus("current")
_ZxAnBfdStdSessPerfCtrlPktDrop_Type = Counter32
_ZxAnBfdStdSessPerfCtrlPktDrop_Object = MibTableColumn
zxAnBfdStdSessPerfCtrlPktDrop = _ZxAnBfdStdSessPerfCtrlPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 3, 1, 3),
    _ZxAnBfdStdSessPerfCtrlPktDrop_Type()
)
zxAnBfdStdSessPerfCtrlPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdStdSessPerfCtrlPktDrop.setStatus("current")
_ZxAnBfdStdSessPerfCtrlPktDLT_Type = TimeStamp
_ZxAnBfdStdSessPerfCtrlPktDLT_Object = MibTableColumn
zxAnBfdStdSessPerfCtrlPktDLT = _ZxAnBfdStdSessPerfCtrlPktDLT_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 3, 1, 4),
    _ZxAnBfdStdSessPerfCtrlPktDLT_Type()
)
zxAnBfdStdSessPerfCtrlPktDLT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdStdSessPerfCtrlPktDLT.setStatus("current")
_ZxAnBfdStdSessPerfEchoPktIn_Type = Counter32
_ZxAnBfdStdSessPerfEchoPktIn_Object = MibTableColumn
zxAnBfdStdSessPerfEchoPktIn = _ZxAnBfdStdSessPerfEchoPktIn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 3, 1, 5),
    _ZxAnBfdStdSessPerfEchoPktIn_Type()
)
zxAnBfdStdSessPerfEchoPktIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdStdSessPerfEchoPktIn.setStatus("current")
_ZxAnBfdStdSessPerfEchoPktOut_Type = Counter32
_ZxAnBfdStdSessPerfEchoPktOut_Object = MibTableColumn
zxAnBfdStdSessPerfEchoPktOut = _ZxAnBfdStdSessPerfEchoPktOut_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 3, 1, 6),
    _ZxAnBfdStdSessPerfEchoPktOut_Type()
)
zxAnBfdStdSessPerfEchoPktOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdStdSessPerfEchoPktOut.setStatus("current")
_ZxAnBfdStdSessPerfEchoPktDrop_Type = Counter32
_ZxAnBfdStdSessPerfEchoPktDrop_Object = MibTableColumn
zxAnBfdStdSessPerfEchoPktDrop = _ZxAnBfdStdSessPerfEchoPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 3, 1, 7),
    _ZxAnBfdStdSessPerfEchoPktDrop_Type()
)
zxAnBfdStdSessPerfEchoPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdStdSessPerfEchoPktDrop.setStatus("current")
_ZxAnBfdStdSessPerfEchoPktDLT_Type = TimeStamp
_ZxAnBfdStdSessPerfEchoPktDLT_Object = MibTableColumn
zxAnBfdStdSessPerfEchoPktDLT = _ZxAnBfdStdSessPerfEchoPktDLT_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 3, 1, 8),
    _ZxAnBfdStdSessPerfEchoPktDLT_Type()
)
zxAnBfdStdSessPerfEchoPktDLT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdStdSessPerfEchoPktDLT.setStatus("current")
_ZxAnBfdStdSessUpTime_Type = TimeStamp
_ZxAnBfdStdSessUpTime_Object = MibTableColumn
zxAnBfdStdSessUpTime = _ZxAnBfdStdSessUpTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 3, 1, 9),
    _ZxAnBfdStdSessUpTime_Type()
)
zxAnBfdStdSessUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdStdSessUpTime.setStatus("current")
_ZxAnBfdStdSessPerfLastSessDT_Type = TimeStamp
_ZxAnBfdStdSessPerfLastSessDT_Object = MibTableColumn
zxAnBfdStdSessPerfLastSessDT = _ZxAnBfdStdSessPerfLastSessDT_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 3, 1, 10),
    _ZxAnBfdStdSessPerfLastSessDT_Type()
)
zxAnBfdStdSessPerfLastSessDT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdStdSessPerfLastSessDT.setStatus("current")
_ZxAnBfdStdSessPerfLastCommLDC_Type = ZxAnBfdStdDiag
_ZxAnBfdStdSessPerfLastCommLDC_Object = MibTableColumn
zxAnBfdStdSessPerfLastCommLDC = _ZxAnBfdStdSessPerfLastCommLDC_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 3, 1, 11),
    _ZxAnBfdStdSessPerfLastCommLDC_Type()
)
zxAnBfdStdSessPerfLastCommLDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdStdSessPerfLastCommLDC.setStatus("current")
_ZxAnBfdStdSessPerfSessUpCount_Type = Counter32
_ZxAnBfdStdSessPerfSessUpCount_Object = MibTableColumn
zxAnBfdStdSessPerfSessUpCount = _ZxAnBfdStdSessPerfSessUpCount_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 3, 1, 12),
    _ZxAnBfdStdSessPerfSessUpCount_Type()
)
zxAnBfdStdSessPerfSessUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdStdSessPerfSessUpCount.setStatus("current")
_ZxAnBfdStdSessPerfDiscTime_Type = TimeStamp
_ZxAnBfdStdSessPerfDiscTime_Object = MibTableColumn
zxAnBfdStdSessPerfDiscTime = _ZxAnBfdStdSessPerfDiscTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 3, 1, 13),
    _ZxAnBfdStdSessPerfDiscTime_Type()
)
zxAnBfdStdSessPerfDiscTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdStdSessPerfDiscTime.setStatus("current")
_ZxAnBfdStdSessPerfCtrlPktInHC_Type = Counter64
_ZxAnBfdStdSessPerfCtrlPktInHC_Object = MibTableColumn
zxAnBfdStdSessPerfCtrlPktInHC = _ZxAnBfdStdSessPerfCtrlPktInHC_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 3, 1, 14),
    _ZxAnBfdStdSessPerfCtrlPktInHC_Type()
)
zxAnBfdStdSessPerfCtrlPktInHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdStdSessPerfCtrlPktInHC.setStatus("current")
_ZxAnBfdStdSessPerfCtrlPktOutHC_Type = Counter64
_ZxAnBfdStdSessPerfCtrlPktOutHC_Object = MibTableColumn
zxAnBfdStdSessPerfCtrlPktOutHC = _ZxAnBfdStdSessPerfCtrlPktOutHC_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 3, 1, 15),
    _ZxAnBfdStdSessPerfCtrlPktOutHC_Type()
)
zxAnBfdStdSessPerfCtrlPktOutHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdStdSessPerfCtrlPktOutHC.setStatus("current")
_ZxAnBfdStdSessPerfCtrlPktDropHC_Type = Counter64
_ZxAnBfdStdSessPerfCtrlPktDropHC_Object = MibTableColumn
zxAnBfdStdSessPerfCtrlPktDropHC = _ZxAnBfdStdSessPerfCtrlPktDropHC_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 3, 1, 16),
    _ZxAnBfdStdSessPerfCtrlPktDropHC_Type()
)
zxAnBfdStdSessPerfCtrlPktDropHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdStdSessPerfCtrlPktDropHC.setStatus("current")
_ZxAnBfdStdSessPerfEchoPktInHC_Type = Counter64
_ZxAnBfdStdSessPerfEchoPktInHC_Object = MibTableColumn
zxAnBfdStdSessPerfEchoPktInHC = _ZxAnBfdStdSessPerfEchoPktInHC_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 3, 1, 17),
    _ZxAnBfdStdSessPerfEchoPktInHC_Type()
)
zxAnBfdStdSessPerfEchoPktInHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdStdSessPerfEchoPktInHC.setStatus("current")
_ZxAnBfdStdSessPerfEchoPktOutHC_Type = Counter64
_ZxAnBfdStdSessPerfEchoPktOutHC_Object = MibTableColumn
zxAnBfdStdSessPerfEchoPktOutHC = _ZxAnBfdStdSessPerfEchoPktOutHC_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 3, 1, 18),
    _ZxAnBfdStdSessPerfEchoPktOutHC_Type()
)
zxAnBfdStdSessPerfEchoPktOutHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdStdSessPerfEchoPktOutHC.setStatus("current")
_ZxAnBfdStdSessPerfEchoPktDropHC_Type = Counter64
_ZxAnBfdStdSessPerfEchoPktDropHC_Object = MibTableColumn
zxAnBfdStdSessPerfEchoPktDropHC = _ZxAnBfdStdSessPerfEchoPktDropHC_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 3, 1, 19),
    _ZxAnBfdStdSessPerfEchoPktDropHC_Type()
)
zxAnBfdStdSessPerfEchoPktDropHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdStdSessPerfEchoPktDropHC.setStatus("current")
_ZxAnBfdStdSessDiscMapTable_Object = MibTable
zxAnBfdStdSessDiscMapTable = _ZxAnBfdStdSessDiscMapTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 4)
)
if mibBuilder.loadTexts:
    zxAnBfdStdSessDiscMapTable.setStatus("current")
_ZxAnBfdStdSessDiscMapEntry_Object = MibTableRow
zxAnBfdStdSessDiscMapEntry = _ZxAnBfdStdSessDiscMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 4, 1)
)
zxAnBfdStdSessDiscMapEntry.setIndexNames(
    (0, "ZTE-AN-BFD-STD-MIB", "zxAnBfdStdSessDiscIndex"),
)
if mibBuilder.loadTexts:
    zxAnBfdStdSessDiscMapEntry.setStatus("current")


class _ZxAnBfdStdSessDiscIndex_Type(Unsigned32):
    """Custom type zxAnBfdStdSessDiscIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ZxAnBfdStdSessDiscIndex_Type.__name__ = "Unsigned32"
_ZxAnBfdStdSessDiscIndex_Object = MibTableColumn
zxAnBfdStdSessDiscIndex = _ZxAnBfdStdSessDiscIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 4, 1, 1),
    _ZxAnBfdStdSessDiscIndex_Type()
)
zxAnBfdStdSessDiscIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnBfdStdSessDiscIndex.setStatus("current")
_ZxAnBfdStdSessDiscMapIndex_Type = ZxAnBfdStdSessIndexTC
_ZxAnBfdStdSessDiscMapIndex_Object = MibTableColumn
zxAnBfdStdSessDiscMapIndex = _ZxAnBfdStdSessDiscMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 4, 1, 2),
    _ZxAnBfdStdSessDiscMapIndex_Type()
)
zxAnBfdStdSessDiscMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdStdSessDiscMapIndex.setStatus("current")
_ZxAnBfdStdSessIpMapTable_Object = MibTable
zxAnBfdStdSessIpMapTable = _ZxAnBfdStdSessIpMapTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 5)
)
if mibBuilder.loadTexts:
    zxAnBfdStdSessIpMapTable.setStatus("current")
_ZxAnBfdStdSessIpMapEntry_Object = MibTableRow
zxAnBfdStdSessIpMapEntry = _ZxAnBfdStdSessIpMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 5, 1)
)
zxAnBfdStdSessIpMapEntry.setIndexNames(
    (0, "ZTE-AN-BFD-STD-MIB", "zxAnBfdStdSessIfIndex"),
    (0, "ZTE-AN-BFD-STD-MIB", "zxAnBfdStdSessPeerIpAddressType"),
    (0, "ZTE-AN-BFD-STD-MIB", "zxAnBfdStdSessPeerIpAddress"),
)
if mibBuilder.loadTexts:
    zxAnBfdStdSessIpMapEntry.setStatus("current")
_ZxAnBfdStdSessIfIndex_Type = InterfaceIndexOrZero
_ZxAnBfdStdSessIfIndex_Object = MibTableColumn
zxAnBfdStdSessIfIndex = _ZxAnBfdStdSessIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 5, 1, 1),
    _ZxAnBfdStdSessIfIndex_Type()
)
zxAnBfdStdSessIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnBfdStdSessIfIndex.setStatus("current")
_ZxAnBfdStdSessPeerIpAddressType_Type = InetAddressType
_ZxAnBfdStdSessPeerIpAddressType_Object = MibTableColumn
zxAnBfdStdSessPeerIpAddressType = _ZxAnBfdStdSessPeerIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 5, 1, 2),
    _ZxAnBfdStdSessPeerIpAddressType_Type()
)
zxAnBfdStdSessPeerIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnBfdStdSessPeerIpAddressType.setStatus("current")
_ZxAnBfdStdSessPeerIpAddress_Type = InetAddress
_ZxAnBfdStdSessPeerIpAddress_Object = MibTableColumn
zxAnBfdStdSessPeerIpAddress = _ZxAnBfdStdSessPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 5, 1, 3),
    _ZxAnBfdStdSessPeerIpAddress_Type()
)
zxAnBfdStdSessPeerIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnBfdStdSessPeerIpAddress.setStatus("current")
_ZxAnBfdStdSessIpMapIndex_Type = ZxAnBfdStdSessIndexTC
_ZxAnBfdStdSessIpMapIndex_Object = MibTableColumn
zxAnBfdStdSessIpMapIndex = _ZxAnBfdStdSessIpMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 1, 5, 1, 4),
    _ZxAnBfdStdSessIpMapIndex_Type()
)
zxAnBfdStdSessIpMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdStdSessIpMapIndex.setStatus("current")
_ZxAnBfdStdConformance_ObjectIdentity = ObjectIdentity
zxAnBfdStdConformance = _ZxAnBfdStdConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 2)
)
zxAnBfdStdSessEntry.registerAugmentions(
    ("ZTE-AN-BFD-STD-MIB",
     "zxAnBfdStdSessPerfEntry")
)
zxAnBfdStdSessPerfEntry.setIndexNames(*zxAnBfdStdSessEntry.getIndexNames())

# Managed Objects groups


# Notification objects

zxAnBfdStdSessUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 0, 1)
)
zxAnBfdStdSessUp.setObjects(
      *(("ZTE-AN-BFD-STD-MIB", "zxAnBfdStdSessDiag"),
        ("ZTE-AN-BFD-STD-MIB", "zxAnBfdStdSessDiag"))
)
if mibBuilder.loadTexts:
    zxAnBfdStdSessUp.setStatus(
        "current"
    )

zxAnBfdStdSessDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 16, 0, 2)
)
zxAnBfdStdSessDown.setObjects(
      *(("ZTE-AN-BFD-STD-MIB", "zxAnBfdStdSessDiag"),
        ("ZTE-AN-BFD-STD-MIB", "zxAnBfdStdSessDiag"))
)
if mibBuilder.loadTexts:
    zxAnBfdStdSessDown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-BFD-STD-MIB",
    **{"ZxAnBfdStdSessIndexTC": ZxAnBfdStdSessIndexTC,
       "ZxAnBfdStdInterval": ZxAnBfdStdInterval,
       "ZxAnBfdStdMultiplier": ZxAnBfdStdMultiplier,
       "ZxAnBfdStdDiag": ZxAnBfdStdDiag,
       "zxAnBfdStdMib": zxAnBfdStdMib,
       "zxAnBfdStdNotifications": zxAnBfdStdNotifications,
       "zxAnBfdStdSessUp": zxAnBfdStdSessUp,
       "zxAnBfdStdSessDown": zxAnBfdStdSessDown,
       "zxAnBfdStdObjects": zxAnBfdStdObjects,
       "zxAnBfdStdGlobalObjects": zxAnBfdStdGlobalObjects,
       "zxAnBfdStdAdminStatus": zxAnBfdStdAdminStatus,
       "zxAnBfdStdSessTrapsEnable": zxAnBfdStdSessTrapsEnable,
       "zxAnBfdStdSessTable": zxAnBfdStdSessTable,
       "zxAnBfdStdSessEntry": zxAnBfdStdSessEntry,
       "zxAnBfdStdSessIndex": zxAnBfdStdSessIndex,
       "zxAnBfdStdSessVersionNumber": zxAnBfdStdSessVersionNumber,
       "zxAnBfdStdSessType": zxAnBfdStdSessType,
       "zxAnBfdStdSessMHopUniLinkMode": zxAnBfdStdSessMHopUniLinkMode,
       "zxAnBfdStdSessDiscriminator": zxAnBfdStdSessDiscriminator,
       "zxAnBfdStdSessRemoteDiscr": zxAnBfdStdSessRemoteDiscr,
       "zxAnBfdStdSessDestinationUdpPort": zxAnBfdStdSessDestinationUdpPort,
       "zxAnBfdStdSessSourceUdpPort": zxAnBfdStdSessSourceUdpPort,
       "zxAnBfdStdSessEchoSourceUdpPort": zxAnBfdStdSessEchoSourceUdpPort,
       "zxAnBfdStdSessAdminStatus": zxAnBfdStdSessAdminStatus,
       "zxAnBfdStdSessState": zxAnBfdStdSessState,
       "zxAnBfdStdSessRemoteHeardFlag": zxAnBfdStdSessRemoteHeardFlag,
       "zxAnBfdStdSessDiag": zxAnBfdStdSessDiag,
       "zxAnBfdStdSessOperMode": zxAnBfdStdSessOperMode,
       "zxAnBfdStdSessDesiredDmdMode": zxAnBfdStdSessDesiredDmdMode,
       "zxAnBfdStdSessCtrlPlaneIndep": zxAnBfdStdSessCtrlPlaneIndep,
       "zxAnBfdStdSessMultipointFlag": zxAnBfdStdSessMultipointFlag,
       "zxAnBfdStdSessInterface": zxAnBfdStdSessInterface,
       "zxAnBfdStdSessPeerIpAddrType": zxAnBfdStdSessPeerIpAddrType,
       "zxAnBfdStdSessPeerIpAddr": zxAnBfdStdSessPeerIpAddr,
       "zxAnBfdStdSessGTSM": zxAnBfdStdSessGTSM,
       "zxAnBfdStdSessGTSMTTL": zxAnBfdStdSessGTSMTTL,
       "zxAnBfdStdSessDesiredMinTxIntv": zxAnBfdStdSessDesiredMinTxIntv,
       "zxAnBfdStdSessReqMinRxIntv": zxAnBfdStdSessReqMinRxIntv,
       "zxAnBfdStdSessReqMinEchoRxIntv": zxAnBfdStdSessReqMinEchoRxIntv,
       "zxAnBfdStdSessDetectMult": zxAnBfdStdSessDetectMult,
       "zxAnBfdStdSessNegInterval": zxAnBfdStdSessNegInterval,
       "zxAnBfdStdSessNegEchoInterval": zxAnBfdStdSessNegEchoInterval,
       "zxAnBfdStdSessNegDetectMult": zxAnBfdStdSessNegDetectMult,
       "zxAnBfdStdSessAuthPresFlag": zxAnBfdStdSessAuthPresFlag,
       "zxAnBfdStdSessAuthType": zxAnBfdStdSessAuthType,
       "zxAnBfdStdSessAuthKeyID": zxAnBfdStdSessAuthKeyID,
       "zxAnBfdStdSessAuthKey": zxAnBfdStdSessAuthKey,
       "zxAnBfdStdSessIpAddrType": zxAnBfdStdSessIpAddrType,
       "zxAnBfdStdSessIpAddr": zxAnBfdStdSessIpAddr,
       "zxAnBfdStdSessAppType": zxAnBfdStdSessAppType,
       "zxAnBfdStdSessStorType": zxAnBfdStdSessStorType,
       "zxAnBfdStdSessRowStatus": zxAnBfdStdSessRowStatus,
       "zxAnBfdStdSessPerfTable": zxAnBfdStdSessPerfTable,
       "zxAnBfdStdSessPerfEntry": zxAnBfdStdSessPerfEntry,
       "zxAnBfdStdSessPerfCtrlPktIn": zxAnBfdStdSessPerfCtrlPktIn,
       "zxAnBfdStdSessPerfCtrlPktOut": zxAnBfdStdSessPerfCtrlPktOut,
       "zxAnBfdStdSessPerfCtrlPktDrop": zxAnBfdStdSessPerfCtrlPktDrop,
       "zxAnBfdStdSessPerfCtrlPktDLT": zxAnBfdStdSessPerfCtrlPktDLT,
       "zxAnBfdStdSessPerfEchoPktIn": zxAnBfdStdSessPerfEchoPktIn,
       "zxAnBfdStdSessPerfEchoPktOut": zxAnBfdStdSessPerfEchoPktOut,
       "zxAnBfdStdSessPerfEchoPktDrop": zxAnBfdStdSessPerfEchoPktDrop,
       "zxAnBfdStdSessPerfEchoPktDLT": zxAnBfdStdSessPerfEchoPktDLT,
       "zxAnBfdStdSessUpTime": zxAnBfdStdSessUpTime,
       "zxAnBfdStdSessPerfLastSessDT": zxAnBfdStdSessPerfLastSessDT,
       "zxAnBfdStdSessPerfLastCommLDC": zxAnBfdStdSessPerfLastCommLDC,
       "zxAnBfdStdSessPerfSessUpCount": zxAnBfdStdSessPerfSessUpCount,
       "zxAnBfdStdSessPerfDiscTime": zxAnBfdStdSessPerfDiscTime,
       "zxAnBfdStdSessPerfCtrlPktInHC": zxAnBfdStdSessPerfCtrlPktInHC,
       "zxAnBfdStdSessPerfCtrlPktOutHC": zxAnBfdStdSessPerfCtrlPktOutHC,
       "zxAnBfdStdSessPerfCtrlPktDropHC": zxAnBfdStdSessPerfCtrlPktDropHC,
       "zxAnBfdStdSessPerfEchoPktInHC": zxAnBfdStdSessPerfEchoPktInHC,
       "zxAnBfdStdSessPerfEchoPktOutHC": zxAnBfdStdSessPerfEchoPktOutHC,
       "zxAnBfdStdSessPerfEchoPktDropHC": zxAnBfdStdSessPerfEchoPktDropHC,
       "zxAnBfdStdSessDiscMapTable": zxAnBfdStdSessDiscMapTable,
       "zxAnBfdStdSessDiscMapEntry": zxAnBfdStdSessDiscMapEntry,
       "zxAnBfdStdSessDiscIndex": zxAnBfdStdSessDiscIndex,
       "zxAnBfdStdSessDiscMapIndex": zxAnBfdStdSessDiscMapIndex,
       "zxAnBfdStdSessIpMapTable": zxAnBfdStdSessIpMapTable,
       "zxAnBfdStdSessIpMapEntry": zxAnBfdStdSessIpMapEntry,
       "zxAnBfdStdSessIfIndex": zxAnBfdStdSessIfIndex,
       "zxAnBfdStdSessPeerIpAddressType": zxAnBfdStdSessPeerIpAddressType,
       "zxAnBfdStdSessPeerIpAddress": zxAnBfdStdSessPeerIpAddress,
       "zxAnBfdStdSessIpMapIndex": zxAnBfdStdSessIpMapIndex,
       "zxAnBfdStdConformance": zxAnBfdStdConformance}
)
