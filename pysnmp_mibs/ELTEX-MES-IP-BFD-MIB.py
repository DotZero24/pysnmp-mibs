# SNMP MIB module (ELTEX-MES-IP-BFD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-IP-BFD-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:50:31 2025
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
    "CISCO-TC",
    "InterfaceIndexOrZero")

(eltMes,) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMes")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eltMesIpBfd = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 6)
)
if mibBuilder.loadTexts:
    eltMesIpBfd.setRevisions(
        ("2014-03-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EltIpBfdInterval(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(150, 1000),
    )



class EltIpBfdDiag(TextualConvention, Integer32):
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
              8,
              16,
              255)
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
          ("reverseConcatenatedPathDown", 8),
          ("misconnectivity", 16),
          ("noContact", 255))
    )



class EltIpBfdState(TextualConvention, Integer32):
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
        *(("adminDown", 1),
          ("down", 2),
          ("init", 3),
          ("up", 4))
    )



# MIB Managed Objects in the order of their OIDs

_EltIpBfdSessConfigTable_Object = MibTable
eltIpBfdSessConfigTable = _EltIpBfdSessConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 6, 3)
)
if mibBuilder.loadTexts:
    eltIpBfdSessConfigTable.setStatus("current")
_EltIpBfdSessConfigEntry_Object = MibTableRow
eltIpBfdSessConfigEntry = _EltIpBfdSessConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 6, 3, 1)
)
eltIpBfdSessConfigEntry.setIndexNames(
    (0, "ELTEX-MES-IP-BFD-MIB", "eltIpBfdSessConfigIfIndex"),
    (0, "ELTEX-MES-IP-BFD-MIB", "eltIpBfdSessConfigAddrType"),
    (0, "ELTEX-MES-IP-BFD-MIB", "eltIpBfdSessConfigAddr"),
    (0, "ELTEX-MES-IP-BFD-MIB", "eltIpBfdSessConfigLocalAddrType"),
    (0, "ELTEX-MES-IP-BFD-MIB", "eltIpBfdSessConfigLocalAddr"),
)
if mibBuilder.loadTexts:
    eltIpBfdSessConfigEntry.setStatus("current")
_EltIpBfdSessConfigIfIndex_Type = InterfaceIndexOrZero
_EltIpBfdSessConfigIfIndex_Object = MibTableColumn
eltIpBfdSessConfigIfIndex = _EltIpBfdSessConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 6, 3, 1, 1),
    _EltIpBfdSessConfigIfIndex_Type()
)
eltIpBfdSessConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltIpBfdSessConfigIfIndex.setStatus("current")
_EltIpBfdSessConfigAddrType_Type = InetAddressType
_EltIpBfdSessConfigAddrType_Object = MibTableColumn
eltIpBfdSessConfigAddrType = _EltIpBfdSessConfigAddrType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 6, 3, 1, 2),
    _EltIpBfdSessConfigAddrType_Type()
)
eltIpBfdSessConfigAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltIpBfdSessConfigAddrType.setStatus("current")


class _EltIpBfdSessConfigAddr_Type(InetAddress):
    """Custom type eltIpBfdSessConfigAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_EltIpBfdSessConfigAddr_Type.__name__ = "InetAddress"
_EltIpBfdSessConfigAddr_Object = MibTableColumn
eltIpBfdSessConfigAddr = _EltIpBfdSessConfigAddr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 6, 3, 1, 3),
    _EltIpBfdSessConfigAddr_Type()
)
eltIpBfdSessConfigAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltIpBfdSessConfigAddr.setStatus("current")
_EltIpBfdSessConfigLocalAddrType_Type = InetAddressType
_EltIpBfdSessConfigLocalAddrType_Object = MibTableColumn
eltIpBfdSessConfigLocalAddrType = _EltIpBfdSessConfigLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 6, 3, 1, 4),
    _EltIpBfdSessConfigLocalAddrType_Type()
)
eltIpBfdSessConfigLocalAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltIpBfdSessConfigLocalAddrType.setStatus("current")


class _EltIpBfdSessConfigLocalAddr_Type(InetAddress):
    """Custom type eltIpBfdSessConfigLocalAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_EltIpBfdSessConfigLocalAddr_Type.__name__ = "InetAddress"
_EltIpBfdSessConfigLocalAddr_Object = MibTableColumn
eltIpBfdSessConfigLocalAddr = _EltIpBfdSessConfigLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 6, 3, 1, 5),
    _EltIpBfdSessConfigLocalAddr_Type()
)
eltIpBfdSessConfigLocalAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltIpBfdSessConfigLocalAddr.setStatus("current")
_EltIpBfdSessConfigRowStatus_Type = RowStatus
_EltIpBfdSessConfigRowStatus_Object = MibTableColumn
eltIpBfdSessConfigRowStatus = _EltIpBfdSessConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 6, 3, 1, 6),
    _EltIpBfdSessConfigRowStatus_Type()
)
eltIpBfdSessConfigRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpBfdSessConfigRowStatus.setStatus("current")


class _EltIpBfdSessConfigDesiredMinTxIntvl_Type(EltIpBfdInterval):
    """Custom type eltIpBfdSessConfigDesiredMinTxIntvl based on EltIpBfdInterval"""
    defaultValue = 150


_EltIpBfdSessConfigDesiredMinTxIntvl_Type.__name__ = "EltIpBfdInterval"
_EltIpBfdSessConfigDesiredMinTxIntvl_Object = MibTableColumn
eltIpBfdSessConfigDesiredMinTxIntvl = _EltIpBfdSessConfigDesiredMinTxIntvl_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 6, 3, 1, 7),
    _EltIpBfdSessConfigDesiredMinTxIntvl_Type()
)
eltIpBfdSessConfigDesiredMinTxIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpBfdSessConfigDesiredMinTxIntvl.setStatus("current")


class _EltIpBfdSessConfigReqMinRxInterval_Type(EltIpBfdInterval):
    """Custom type eltIpBfdSessConfigReqMinRxInterval based on EltIpBfdInterval"""
    defaultValue = 150


_EltIpBfdSessConfigReqMinRxInterval_Type.__name__ = "EltIpBfdInterval"
_EltIpBfdSessConfigReqMinRxInterval_Object = MibTableColumn
eltIpBfdSessConfigReqMinRxInterval = _EltIpBfdSessConfigReqMinRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 6, 3, 1, 8),
    _EltIpBfdSessConfigReqMinRxInterval_Type()
)
eltIpBfdSessConfigReqMinRxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpBfdSessConfigReqMinRxInterval.setStatus("current")


class _EltIpBfdSessConfigDetectMult_Type(Unsigned32):
    """Custom type eltIpBfdSessConfigDetectMult based on Unsigned32"""
    defaultValue = 3


_EltIpBfdSessConfigDetectMult_Type.__name__ = "Unsigned32"
_EltIpBfdSessConfigDetectMult_Object = MibTableColumn
eltIpBfdSessConfigDetectMult = _EltIpBfdSessConfigDetectMult_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 6, 3, 1, 9),
    _EltIpBfdSessConfigDetectMult_Type()
)
eltIpBfdSessConfigDetectMult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpBfdSessConfigDetectMult.setStatus("current")
_EltIpBfdSessStateTable_Object = MibTable
eltIpBfdSessStateTable = _EltIpBfdSessStateTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 6, 4)
)
if mibBuilder.loadTexts:
    eltIpBfdSessStateTable.setStatus("current")
_EltIpBfdSessStateEntry_Object = MibTableRow
eltIpBfdSessStateEntry = _EltIpBfdSessStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 6, 4, 1)
)
eltIpBfdSessStateEntry.setIndexNames(
    (0, "ELTEX-MES-IP-BFD-MIB", "eltIpBfdSessStateIfIndex"),
    (0, "ELTEX-MES-IP-BFD-MIB", "eltIpBfdSessStatePeerAddrType"),
    (0, "ELTEX-MES-IP-BFD-MIB", "eltIpBfdSessStatePeerAddr"),
    (0, "ELTEX-MES-IP-BFD-MIB", "eltIpBfdSessStateLocalAddrType"),
    (0, "ELTEX-MES-IP-BFD-MIB", "eltIpBfdSessStateLocalAddr"),
    (0, "ELTEX-MES-IP-BFD-MIB", "eltIpBfdSessStateRemoteDiscr"),
)
if mibBuilder.loadTexts:
    eltIpBfdSessStateEntry.setStatus("current")
_EltIpBfdSessStateIfIndex_Type = InterfaceIndexOrZero
_EltIpBfdSessStateIfIndex_Object = MibTableColumn
eltIpBfdSessStateIfIndex = _EltIpBfdSessStateIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 6, 4, 1, 1),
    _EltIpBfdSessStateIfIndex_Type()
)
eltIpBfdSessStateIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltIpBfdSessStateIfIndex.setStatus("current")
_EltIpBfdSessStatePeerAddrType_Type = InetAddressType
_EltIpBfdSessStatePeerAddrType_Object = MibTableColumn
eltIpBfdSessStatePeerAddrType = _EltIpBfdSessStatePeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 6, 4, 1, 2),
    _EltIpBfdSessStatePeerAddrType_Type()
)
eltIpBfdSessStatePeerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltIpBfdSessStatePeerAddrType.setStatus("current")
_EltIpBfdSessStatePeerAddr_Type = InetAddress
_EltIpBfdSessStatePeerAddr_Object = MibTableColumn
eltIpBfdSessStatePeerAddr = _EltIpBfdSessStatePeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 6, 4, 1, 3),
    _EltIpBfdSessStatePeerAddr_Type()
)
eltIpBfdSessStatePeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltIpBfdSessStatePeerAddr.setStatus("current")
_EltIpBfdSessStateLocalAddrType_Type = InetAddressType
_EltIpBfdSessStateLocalAddrType_Object = MibTableColumn
eltIpBfdSessStateLocalAddrType = _EltIpBfdSessStateLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 6, 4, 1, 4),
    _EltIpBfdSessStateLocalAddrType_Type()
)
eltIpBfdSessStateLocalAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltIpBfdSessStateLocalAddrType.setStatus("current")


class _EltIpBfdSessStateLocalAddr_Type(InetAddress):
    """Custom type eltIpBfdSessStateLocalAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_EltIpBfdSessStateLocalAddr_Type.__name__ = "InetAddress"
_EltIpBfdSessStateLocalAddr_Object = MibTableColumn
eltIpBfdSessStateLocalAddr = _EltIpBfdSessStateLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 6, 4, 1, 5),
    _EltIpBfdSessStateLocalAddr_Type()
)
eltIpBfdSessStateLocalAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltIpBfdSessStateLocalAddr.setStatus("current")


class _EltIpBfdSessStateRemoteDiscr_Type(Unsigned32):
    """Custom type eltIpBfdSessStateRemoteDiscr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_EltIpBfdSessStateRemoteDiscr_Type.__name__ = "Unsigned32"
_EltIpBfdSessStateRemoteDiscr_Object = MibTableColumn
eltIpBfdSessStateRemoteDiscr = _EltIpBfdSessStateRemoteDiscr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 6, 4, 1, 6),
    _EltIpBfdSessStateRemoteDiscr_Type()
)
eltIpBfdSessStateRemoteDiscr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltIpBfdSessStateRemoteDiscr.setStatus("current")
_EltIpBfdSessStateState_Type = EltIpBfdState
_EltIpBfdSessStateState_Object = MibTableColumn
eltIpBfdSessStateState = _EltIpBfdSessStateState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 6, 4, 1, 7),
    _EltIpBfdSessStateState_Type()
)
eltIpBfdSessStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltIpBfdSessStateState.setStatus("current")
_EltIpBfdSessStateDiag_Type = EltIpBfdDiag
_EltIpBfdSessStateDiag_Object = MibTableColumn
eltIpBfdSessStateDiag = _EltIpBfdSessStateDiag_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 6, 4, 1, 8),
    _EltIpBfdSessStateDiag_Type()
)
eltIpBfdSessStateDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltIpBfdSessStateDiag.setStatus("current")
_EltIpBfdSessStateOperIfIndex_Type = InterfaceIndexOrZero
_EltIpBfdSessStateOperIfIndex_Object = MibTableColumn
eltIpBfdSessStateOperIfIndex = _EltIpBfdSessStateOperIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 6, 4, 1, 9),
    _EltIpBfdSessStateOperIfIndex_Type()
)
eltIpBfdSessStateOperIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltIpBfdSessStateOperIfIndex.setStatus("current")
_EltIpBfdSessStateOperPeerAddrType_Type = InetAddressType
_EltIpBfdSessStateOperPeerAddrType_Object = MibTableColumn
eltIpBfdSessStateOperPeerAddrType = _EltIpBfdSessStateOperPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 6, 4, 1, 10),
    _EltIpBfdSessStateOperPeerAddrType_Type()
)
eltIpBfdSessStateOperPeerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltIpBfdSessStateOperPeerAddrType.setStatus("current")
_EltIpBfdSessStateOperPeerAddr_Type = InetAddress
_EltIpBfdSessStateOperPeerAddr_Object = MibTableColumn
eltIpBfdSessStateOperPeerAddr = _EltIpBfdSessStateOperPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 6, 4, 1, 11),
    _EltIpBfdSessStateOperPeerAddr_Type()
)
eltIpBfdSessStateOperPeerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltIpBfdSessStateOperPeerAddr.setStatus("current")
_EltIpBfdSessStateOperLocalAddrType_Type = InetAddressType
_EltIpBfdSessStateOperLocalAddrType_Object = MibTableColumn
eltIpBfdSessStateOperLocalAddrType = _EltIpBfdSessStateOperLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 6, 4, 1, 12),
    _EltIpBfdSessStateOperLocalAddrType_Type()
)
eltIpBfdSessStateOperLocalAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltIpBfdSessStateOperLocalAddrType.setStatus("current")
_EltIpBfdSessStateOperLocalAddr_Type = InetAddress
_EltIpBfdSessStateOperLocalAddr_Object = MibTableColumn
eltIpBfdSessStateOperLocalAddr = _EltIpBfdSessStateOperLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 6, 4, 1, 13),
    _EltIpBfdSessStateOperLocalAddr_Type()
)
eltIpBfdSessStateOperLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltIpBfdSessStateOperLocalAddr.setStatus("current")
_EltIpBfdSessStateOperRemoteDiscr_Type = Unsigned32
_EltIpBfdSessStateOperRemoteDiscr_Object = MibTableColumn
eltIpBfdSessStateOperRemoteDiscr = _EltIpBfdSessStateOperRemoteDiscr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 6, 4, 1, 14),
    _EltIpBfdSessStateOperRemoteDiscr_Type()
)
eltIpBfdSessStateOperRemoteDiscr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltIpBfdSessStateOperRemoteDiscr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-IP-BFD-MIB",
    **{"EltIpBfdInterval": EltIpBfdInterval,
       "EltIpBfdDiag": EltIpBfdDiag,
       "EltIpBfdState": EltIpBfdState,
       "eltMesIpBfd": eltMesIpBfd,
       "eltIpBfdSessConfigTable": eltIpBfdSessConfigTable,
       "eltIpBfdSessConfigEntry": eltIpBfdSessConfigEntry,
       "eltIpBfdSessConfigIfIndex": eltIpBfdSessConfigIfIndex,
       "eltIpBfdSessConfigAddrType": eltIpBfdSessConfigAddrType,
       "eltIpBfdSessConfigAddr": eltIpBfdSessConfigAddr,
       "eltIpBfdSessConfigLocalAddrType": eltIpBfdSessConfigLocalAddrType,
       "eltIpBfdSessConfigLocalAddr": eltIpBfdSessConfigLocalAddr,
       "eltIpBfdSessConfigRowStatus": eltIpBfdSessConfigRowStatus,
       "eltIpBfdSessConfigDesiredMinTxIntvl": eltIpBfdSessConfigDesiredMinTxIntvl,
       "eltIpBfdSessConfigReqMinRxInterval": eltIpBfdSessConfigReqMinRxInterval,
       "eltIpBfdSessConfigDetectMult": eltIpBfdSessConfigDetectMult,
       "eltIpBfdSessStateTable": eltIpBfdSessStateTable,
       "eltIpBfdSessStateEntry": eltIpBfdSessStateEntry,
       "eltIpBfdSessStateIfIndex": eltIpBfdSessStateIfIndex,
       "eltIpBfdSessStatePeerAddrType": eltIpBfdSessStatePeerAddrType,
       "eltIpBfdSessStatePeerAddr": eltIpBfdSessStatePeerAddr,
       "eltIpBfdSessStateLocalAddrType": eltIpBfdSessStateLocalAddrType,
       "eltIpBfdSessStateLocalAddr": eltIpBfdSessStateLocalAddr,
       "eltIpBfdSessStateRemoteDiscr": eltIpBfdSessStateRemoteDiscr,
       "eltIpBfdSessStateState": eltIpBfdSessStateState,
       "eltIpBfdSessStateDiag": eltIpBfdSessStateDiag,
       "eltIpBfdSessStateOperIfIndex": eltIpBfdSessStateOperIfIndex,
       "eltIpBfdSessStateOperPeerAddrType": eltIpBfdSessStateOperPeerAddrType,
       "eltIpBfdSessStateOperPeerAddr": eltIpBfdSessStateOperPeerAddr,
       "eltIpBfdSessStateOperLocalAddrType": eltIpBfdSessStateOperLocalAddrType,
       "eltIpBfdSessStateOperLocalAddr": eltIpBfdSessStateOperLocalAddr,
       "eltIpBfdSessStateOperRemoteDiscr": eltIpBfdSessStateOperRemoteDiscr}
)
