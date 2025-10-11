# SNMP MIB module (ZTE-AN-BFD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-BFD-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:34 2025
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

(InetAddress,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(ZxAnIfindex,
 zxAn) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "ZxAnIfindex",
    "zxAn")


# MODULE-IDENTITY

zxAnBfdMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 15)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnBfdMibObjects_ObjectIdentity = ObjectIdentity
zxAnBfdMibObjects = _ZxAnBfdMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 15, 1)
)
_ZxAnBfdSessTable_Object = MibTable
zxAnBfdSessTable = _ZxAnBfdSessTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 15, 1, 20)
)
if mibBuilder.loadTexts:
    zxAnBfdSessTable.setStatus("current")
_ZxAnBfdSessEntry_Object = MibTableRow
zxAnBfdSessEntry = _ZxAnBfdSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 15, 1, 20, 1)
)
zxAnBfdSessEntry.setIndexNames(
    (0, "ZTE-AN-BFD-MIB", "zxAnBfdSessApplicationType"),
    (0, "ZTE-AN-BFD-MIB", "zxAnBfdL3IfVlan"),
)
if mibBuilder.loadTexts:
    zxAnBfdSessEntry.setStatus("current")


class _ZxAnBfdSessApplicationType_Type(Integer32):
    """Custom type zxAnBfdSessApplicationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("uaps", 1)
    )


_ZxAnBfdSessApplicationType_Type.__name__ = "Integer32"
_ZxAnBfdSessApplicationType_Object = MibTableColumn
zxAnBfdSessApplicationType = _ZxAnBfdSessApplicationType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 15, 1, 20, 1, 1),
    _ZxAnBfdSessApplicationType_Type()
)
zxAnBfdSessApplicationType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnBfdSessApplicationType.setStatus("current")


class _ZxAnBfdL3IfVlan_Type(Integer32):
    """Custom type zxAnBfdL3IfVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxAnBfdL3IfVlan_Type.__name__ = "Integer32"
_ZxAnBfdL3IfVlan_Object = MibTableColumn
zxAnBfdL3IfVlan = _ZxAnBfdL3IfVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 15, 1, 20, 1, 2),
    _ZxAnBfdL3IfVlan_Type()
)
zxAnBfdL3IfVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnBfdL3IfVlan.setStatus("current")


class _ZxAnBfdSessDiscriminator_Type(Integer32):
    """Custom type zxAnBfdSessDiscriminator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZxAnBfdSessDiscriminator_Type.__name__ = "Integer32"
_ZxAnBfdSessDiscriminator_Object = MibTableColumn
zxAnBfdSessDiscriminator = _ZxAnBfdSessDiscriminator_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 15, 1, 20, 1, 3),
    _ZxAnBfdSessDiscriminator_Type()
)
zxAnBfdSessDiscriminator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdSessDiscriminator.setStatus("current")


class _ZxAnBfdSessRemoteDiscr_Type(Integer32):
    """Custom type zxAnBfdSessRemoteDiscr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZxAnBfdSessRemoteDiscr_Type.__name__ = "Integer32"
_ZxAnBfdSessRemoteDiscr_Object = MibTableColumn
zxAnBfdSessRemoteDiscr = _ZxAnBfdSessRemoteDiscr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 15, 1, 20, 1, 4),
    _ZxAnBfdSessRemoteDiscr_Type()
)
zxAnBfdSessRemoteDiscr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdSessRemoteDiscr.setStatus("current")


class _ZxAnBfdSessUdpPort_Type(Integer32):
    """Custom type zxAnBfdSessUdpPort based on Integer32"""
    defaultValue = 0


_ZxAnBfdSessUdpPort_Type.__name__ = "Integer32"
_ZxAnBfdSessUdpPort_Object = MibTableColumn
zxAnBfdSessUdpPort = _ZxAnBfdSessUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 15, 1, 20, 1, 5),
    _ZxAnBfdSessUdpPort_Type()
)
zxAnBfdSessUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdSessUdpPort.setStatus("current")


class _ZxAnBfdSessState_Type(Integer32):
    """Custom type zxAnBfdSessState based on Integer32"""
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


_ZxAnBfdSessState_Type.__name__ = "Integer32"
_ZxAnBfdSessState_Object = MibTableColumn
zxAnBfdSessState = _ZxAnBfdSessState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 15, 1, 20, 1, 6),
    _ZxAnBfdSessState_Type()
)
zxAnBfdSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdSessState.setStatus("current")


class _ZxAnBfdSessDemandModeDesiredFlag_Type(TruthValue):
    """Custom type zxAnBfdSessDemandModeDesiredFlag based on TruthValue"""
    defaultValue = 2


_ZxAnBfdSessDemandModeDesiredFlag_Type.__name__ = "TruthValue"
_ZxAnBfdSessDemandModeDesiredFlag_Object = MibTableColumn
zxAnBfdSessDemandModeDesiredFlag = _ZxAnBfdSessDemandModeDesiredFlag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 15, 1, 20, 1, 7),
    _ZxAnBfdSessDemandModeDesiredFlag_Type()
)
zxAnBfdSessDemandModeDesiredFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdSessDemandModeDesiredFlag.setStatus("current")


class _ZxAnBfdSessEchoFuncModeDesiredFlag_Type(TruthValue):
    """Custom type zxAnBfdSessEchoFuncModeDesiredFlag based on TruthValue"""
    defaultValue = 2


_ZxAnBfdSessEchoFuncModeDesiredFlag_Type.__name__ = "TruthValue"
_ZxAnBfdSessEchoFuncModeDesiredFlag_Object = MibTableColumn
zxAnBfdSessEchoFuncModeDesiredFlag = _ZxAnBfdSessEchoFuncModeDesiredFlag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 15, 1, 20, 1, 8),
    _ZxAnBfdSessEchoFuncModeDesiredFlag_Type()
)
zxAnBfdSessEchoFuncModeDesiredFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdSessEchoFuncModeDesiredFlag.setStatus("current")


class _ZxAnBfdSessLocalAddrType_Type(Integer32):
    """Custom type zxAnBfdSessLocalAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_ZxAnBfdSessLocalAddrType_Type.__name__ = "Integer32"
_ZxAnBfdSessLocalAddrType_Object = MibTableColumn
zxAnBfdSessLocalAddrType = _ZxAnBfdSessLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 15, 1, 20, 1, 9),
    _ZxAnBfdSessLocalAddrType_Type()
)
zxAnBfdSessLocalAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdSessLocalAddrType.setStatus("current")
_ZxAnBfdSessLocalAddr_Type = InetAddress
_ZxAnBfdSessLocalAddr_Object = MibTableColumn
zxAnBfdSessLocalAddr = _ZxAnBfdSessLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 15, 1, 20, 1, 10),
    _ZxAnBfdSessLocalAddr_Type()
)
zxAnBfdSessLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdSessLocalAddr.setStatus("current")


class _ZxAnBfdSessRemoteAddrType_Type(Integer32):
    """Custom type zxAnBfdSessRemoteAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_ZxAnBfdSessRemoteAddrType_Type.__name__ = "Integer32"
_ZxAnBfdSessRemoteAddrType_Object = MibTableColumn
zxAnBfdSessRemoteAddrType = _ZxAnBfdSessRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 15, 1, 20, 1, 11),
    _ZxAnBfdSessRemoteAddrType_Type()
)
zxAnBfdSessRemoteAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdSessRemoteAddrType.setStatus("current")
_ZxAnBfdSessRemoteAddr_Type = InetAddress
_ZxAnBfdSessRemoteAddr_Object = MibTableColumn
zxAnBfdSessRemoteAddr = _ZxAnBfdSessRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 15, 1, 20, 1, 12),
    _ZxAnBfdSessRemoteAddr_Type()
)
zxAnBfdSessRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdSessRemoteAddr.setStatus("current")
_ZxAnBfdSessDesiredMinTxInterval_Type = Integer32
_ZxAnBfdSessDesiredMinTxInterval_Object = MibTableColumn
zxAnBfdSessDesiredMinTxInterval = _ZxAnBfdSessDesiredMinTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 15, 1, 20, 1, 13),
    _ZxAnBfdSessDesiredMinTxInterval_Type()
)
zxAnBfdSessDesiredMinTxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnBfdSessDesiredMinTxInterval.setStatus("current")
_ZxAnBfdSessRequiredMinRxInterval_Type = Integer32
_ZxAnBfdSessRequiredMinRxInterval_Object = MibTableColumn
zxAnBfdSessRequiredMinRxInterval = _ZxAnBfdSessRequiredMinRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 15, 1, 20, 1, 14),
    _ZxAnBfdSessRequiredMinRxInterval_Type()
)
zxAnBfdSessRequiredMinRxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnBfdSessRequiredMinRxInterval.setStatus("current")
_ZxAnBfdSessDetectMult_Type = Integer32
_ZxAnBfdSessDetectMult_Object = MibTableColumn
zxAnBfdSessDetectMult = _ZxAnBfdSessDetectMult_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 15, 1, 20, 1, 15),
    _ZxAnBfdSessDetectMult_Type()
)
zxAnBfdSessDetectMult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnBfdSessDetectMult.setStatus("current")


class _ZxAnBfdSessDownDiag_Type(Integer32):
    """Custom type zxAnBfdSessDownDiag based on Integer32"""
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
        *(("noDiagnostic", 1),
          ("controlDetectionTimeExpired", 2),
          ("echoFunctionFailed", 3),
          ("neighborSignaledSessionDown", 4),
          ("forwardingPlaneReset", 5),
          ("pathDown", 6),
          ("concatenatedPathDown", 7),
          ("administrativelyDown", 8),
          ("reverseConcatenatedPathDown", 9))
    )


_ZxAnBfdSessDownDiag_Type.__name__ = "Integer32"
_ZxAnBfdSessDownDiag_Object = MibTableColumn
zxAnBfdSessDownDiag = _ZxAnBfdSessDownDiag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 15, 1, 20, 1, 16),
    _ZxAnBfdSessDownDiag_Type()
)
zxAnBfdSessDownDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdSessDownDiag.setStatus("current")
_ZxAnBfdSessPerfTable_Object = MibTable
zxAnBfdSessPerfTable = _ZxAnBfdSessPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 15, 1, 21)
)
if mibBuilder.loadTexts:
    zxAnBfdSessPerfTable.setStatus("current")
_ZxAnBfdSessPerfEntry_Object = MibTableRow
zxAnBfdSessPerfEntry = _ZxAnBfdSessPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 15, 1, 21, 1)
)
if mibBuilder.loadTexts:
    zxAnBfdSessPerfEntry.setStatus("current")
_ZxAnBfdSessPerfPktIn_Type = Counter32
_ZxAnBfdSessPerfPktIn_Object = MibTableColumn
zxAnBfdSessPerfPktIn = _ZxAnBfdSessPerfPktIn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 15, 1, 21, 1, 1),
    _ZxAnBfdSessPerfPktIn_Type()
)
zxAnBfdSessPerfPktIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdSessPerfPktIn.setStatus("current")
_ZxAnBfdSessPerfPktOut_Type = Counter32
_ZxAnBfdSessPerfPktOut_Object = MibTableColumn
zxAnBfdSessPerfPktOut = _ZxAnBfdSessPerfPktOut_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 15, 1, 21, 1, 2),
    _ZxAnBfdSessPerfPktOut_Type()
)
zxAnBfdSessPerfPktOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdSessPerfPktOut.setStatus("current")
_ZxAnBfdSessPerfUpTime_Type = TimeStamp
_ZxAnBfdSessPerfUpTime_Object = MibTableColumn
zxAnBfdSessPerfUpTime = _ZxAnBfdSessPerfUpTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 15, 1, 21, 1, 3),
    _ZxAnBfdSessPerfUpTime_Type()
)
zxAnBfdSessPerfUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdSessPerfUpTime.setStatus("current")
_ZxAnBfdSessPerfDownTime_Type = TimeStamp
_ZxAnBfdSessPerfDownTime_Object = MibTableColumn
zxAnBfdSessPerfDownTime = _ZxAnBfdSessPerfDownTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 15, 1, 21, 1, 4),
    _ZxAnBfdSessPerfDownTime_Type()
)
zxAnBfdSessPerfDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBfdSessPerfDownTime.setStatus("current")
zxAnBfdSessEntry.registerAugmentions(
    ("ZTE-AN-BFD-MIB",
     "zxAnBfdSessPerfEntry")
)
zxAnBfdSessPerfEntry.setIndexNames(*zxAnBfdSessEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-BFD-MIB",
    **{"zxAnBfdMib": zxAnBfdMib,
       "zxAnBfdMibObjects": zxAnBfdMibObjects,
       "zxAnBfdSessTable": zxAnBfdSessTable,
       "zxAnBfdSessEntry": zxAnBfdSessEntry,
       "zxAnBfdSessApplicationType": zxAnBfdSessApplicationType,
       "zxAnBfdL3IfVlan": zxAnBfdL3IfVlan,
       "zxAnBfdSessDiscriminator": zxAnBfdSessDiscriminator,
       "zxAnBfdSessRemoteDiscr": zxAnBfdSessRemoteDiscr,
       "zxAnBfdSessUdpPort": zxAnBfdSessUdpPort,
       "zxAnBfdSessState": zxAnBfdSessState,
       "zxAnBfdSessDemandModeDesiredFlag": zxAnBfdSessDemandModeDesiredFlag,
       "zxAnBfdSessEchoFuncModeDesiredFlag": zxAnBfdSessEchoFuncModeDesiredFlag,
       "zxAnBfdSessLocalAddrType": zxAnBfdSessLocalAddrType,
       "zxAnBfdSessLocalAddr": zxAnBfdSessLocalAddr,
       "zxAnBfdSessRemoteAddrType": zxAnBfdSessRemoteAddrType,
       "zxAnBfdSessRemoteAddr": zxAnBfdSessRemoteAddr,
       "zxAnBfdSessDesiredMinTxInterval": zxAnBfdSessDesiredMinTxInterval,
       "zxAnBfdSessRequiredMinRxInterval": zxAnBfdSessRequiredMinRxInterval,
       "zxAnBfdSessDetectMult": zxAnBfdSessDetectMult,
       "zxAnBfdSessDownDiag": zxAnBfdSessDownDiag,
       "zxAnBfdSessPerfTable": zxAnBfdSessPerfTable,
       "zxAnBfdSessPerfEntry": zxAnBfdSessPerfEntry,
       "zxAnBfdSessPerfPktIn": zxAnBfdSessPerfPktIn,
       "zxAnBfdSessPerfPktOut": zxAnBfdSessPerfPktOut,
       "zxAnBfdSessPerfUpTime": zxAnBfdSessPerfUpTime,
       "zxAnBfdSessPerfDownTime": zxAnBfdSessPerfDownTime}
)
