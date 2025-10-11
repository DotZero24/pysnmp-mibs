# SNMP MIB module (ARICENT-DHCPv6-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-DHCPv6-CLIENT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:44:36 2025
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
 enterprises,
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
    "enterprises",
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

fsdhcpv6clnt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 43)
)
if mibBuilder.loadTexts:
    fsdhcpv6clnt.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FsDhcp6ClntDuidValue(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )



class FsDhcp6ClntDuidType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dtLlt", 1),
          ("dtEn", 2),
          ("dtLl", 3))
    )



# MIB Managed Objects in the order of their OIDs

_FsDhcp6ClntNotify_ObjectIdentity = ObjectIdentity
fsDhcp6ClntNotify = _FsDhcp6ClntNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 43, 0)
)
_FsDhcp6ClntSystem_ObjectIdentity = ObjectIdentity
fsDhcp6ClntSystem = _FsDhcp6ClntSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 43, 1)
)


class _FsDhcp6ClntTrapAdminControl_Type(Bits):
    """Custom type fsDhcp6ClntTrapAdminControl based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("trapInvalidPacketIn", 1),
          ("trapHmacAuthFail", 2))
    )

_FsDhcp6ClntTrapAdminControl_Type.__name__ = "Bits"
_FsDhcp6ClntTrapAdminControl_Object = MibScalar
fsDhcp6ClntTrapAdminControl = _FsDhcp6ClntTrapAdminControl_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 43, 1, 1),
    _FsDhcp6ClntTrapAdminControl_Type()
)
fsDhcp6ClntTrapAdminControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDhcp6ClntTrapAdminControl.setStatus("current")


class _FsDhcp6ClntDebugTrace_Type(DisplayString):
    """Custom type fsDhcp6ClntDebugTrace based on DisplayString"""
    defaultValue = OctetString("critical")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_FsDhcp6ClntDebugTrace_Type.__name__ = "DisplayString"
_FsDhcp6ClntDebugTrace_Object = MibScalar
fsDhcp6ClntDebugTrace = _FsDhcp6ClntDebugTrace_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 43, 1, 2),
    _FsDhcp6ClntDebugTrace_Type()
)
fsDhcp6ClntDebugTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDhcp6ClntDebugTrace.setStatus("current")


class _FsDhcp6ClntSysLogAdminStatus_Type(Integer32):
    """Custom type fsDhcp6ClntSysLogAdminStatus based on Integer32"""
    defaultValue = 2

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


_FsDhcp6ClntSysLogAdminStatus_Type.__name__ = "Integer32"
_FsDhcp6ClntSysLogAdminStatus_Object = MibScalar
fsDhcp6ClntSysLogAdminStatus = _FsDhcp6ClntSysLogAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 43, 1, 3),
    _FsDhcp6ClntSysLogAdminStatus_Type()
)
fsDhcp6ClntSysLogAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDhcp6ClntSysLogAdminStatus.setStatus("current")


class _FsDhcp6ClntListenPort_Type(Integer32):
    """Custom type fsDhcp6ClntListenPort based on Integer32"""
    defaultValue = 546

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsDhcp6ClntListenPort_Type.__name__ = "Integer32"
_FsDhcp6ClntListenPort_Object = MibScalar
fsDhcp6ClntListenPort = _FsDhcp6ClntListenPort_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 43, 1, 4),
    _FsDhcp6ClntListenPort_Type()
)
fsDhcp6ClntListenPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDhcp6ClntListenPort.setStatus("current")


class _FsDhcp6ClntTransmitPort_Type(Integer32):
    """Custom type fsDhcp6ClntTransmitPort based on Integer32"""
    defaultValue = 547

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsDhcp6ClntTransmitPort_Type.__name__ = "Integer32"
_FsDhcp6ClntTransmitPort_Object = MibScalar
fsDhcp6ClntTransmitPort = _FsDhcp6ClntTransmitPort_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 43, 1, 5),
    _FsDhcp6ClntTransmitPort_Type()
)
fsDhcp6ClntTransmitPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDhcp6ClntTransmitPort.setStatus("current")
_FsDhcp6ClntConfig_ObjectIdentity = ObjectIdentity
fsDhcp6ClntConfig = _FsDhcp6ClntConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 43, 2)
)
_FsDhcp6ClntIfTable_Object = MibTable
fsDhcp6ClntIfTable = _FsDhcp6ClntIfTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 43, 2, 1)
)
if mibBuilder.loadTexts:
    fsDhcp6ClntIfTable.setStatus("current")
_FsDhcp6ClntIfEntry_Object = MibTableRow
fsDhcp6ClntIfEntry = _FsDhcp6ClntIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 43, 2, 1, 1)
)
fsDhcp6ClntIfEntry.setIndexNames(
    (0, "ARICENT-DHCPv6-CLIENT-MIB", "fsDhcp6ClntIfIndex"),
)
if mibBuilder.loadTexts:
    fsDhcp6ClntIfEntry.setStatus("current")


class _FsDhcp6ClntIfIndex_Type(Integer32):
    """Custom type fsDhcp6ClntIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsDhcp6ClntIfIndex_Type.__name__ = "Integer32"
_FsDhcp6ClntIfIndex_Object = MibTableColumn
fsDhcp6ClntIfIndex = _FsDhcp6ClntIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 43, 2, 1, 1, 1),
    _FsDhcp6ClntIfIndex_Type()
)
fsDhcp6ClntIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDhcp6ClntIfIndex.setStatus("current")


class _FsDhcp6ClntIfSrvAddress_Type(OctetString):
    """Custom type fsDhcp6ClntIfSrvAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsDhcp6ClntIfSrvAddress_Type.__name__ = "OctetString"
_FsDhcp6ClntIfSrvAddress_Object = MibTableColumn
fsDhcp6ClntIfSrvAddress = _FsDhcp6ClntIfSrvAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 43, 2, 1, 1, 2),
    _FsDhcp6ClntIfSrvAddress_Type()
)
fsDhcp6ClntIfSrvAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcp6ClntIfSrvAddress.setStatus("current")


class _FsDhcp6ClntIfDuidType_Type(FsDhcp6ClntDuidType):
    """Custom type fsDhcp6ClntIfDuidType based on FsDhcp6ClntDuidType"""
    defaultValue = 1


_FsDhcp6ClntIfDuidType_Type.__name__ = "FsDhcp6ClntDuidType"
_FsDhcp6ClntIfDuidType_Object = MibTableColumn
fsDhcp6ClntIfDuidType = _FsDhcp6ClntIfDuidType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 43, 2, 1, 1, 3),
    _FsDhcp6ClntIfDuidType_Type()
)
fsDhcp6ClntIfDuidType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcp6ClntIfDuidType.setStatus("current")
_FsDhcp6ClntIfDuid_Type = FsDhcp6ClntDuidValue
_FsDhcp6ClntIfDuid_Object = MibTableColumn
fsDhcp6ClntIfDuid = _FsDhcp6ClntIfDuid_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 43, 2, 1, 1, 4),
    _FsDhcp6ClntIfDuid_Type()
)
fsDhcp6ClntIfDuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcp6ClntIfDuid.setStatus("current")


class _FsDhcp6ClntIfDuidIfIndex_Type(Integer32):
    """Custom type fsDhcp6ClntIfDuidIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsDhcp6ClntIfDuidIfIndex_Type.__name__ = "Integer32"
_FsDhcp6ClntIfDuidIfIndex_Object = MibTableColumn
fsDhcp6ClntIfDuidIfIndex = _FsDhcp6ClntIfDuidIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 43, 2, 1, 1, 5),
    _FsDhcp6ClntIfDuidIfIndex_Type()
)
fsDhcp6ClntIfDuidIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcp6ClntIfDuidIfIndex.setStatus("current")


class _FsDhcp6ClntIfMaxRetCount_Type(Integer32):
    """Custom type fsDhcp6ClntIfMaxRetCount based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_FsDhcp6ClntIfMaxRetCount_Type.__name__ = "Integer32"
_FsDhcp6ClntIfMaxRetCount_Object = MibTableColumn
fsDhcp6ClntIfMaxRetCount = _FsDhcp6ClntIfMaxRetCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 43, 2, 1, 1, 6),
    _FsDhcp6ClntIfMaxRetCount_Type()
)
fsDhcp6ClntIfMaxRetCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcp6ClntIfMaxRetCount.setStatus("current")


class _FsDhcp6ClntIfMaxRetDelay_Type(Integer32):
    """Custom type fsDhcp6ClntIfMaxRetDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsDhcp6ClntIfMaxRetDelay_Type.__name__ = "Integer32"
_FsDhcp6ClntIfMaxRetDelay_Object = MibTableColumn
fsDhcp6ClntIfMaxRetDelay = _FsDhcp6ClntIfMaxRetDelay_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 43, 2, 1, 1, 7),
    _FsDhcp6ClntIfMaxRetDelay_Type()
)
fsDhcp6ClntIfMaxRetDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcp6ClntIfMaxRetDelay.setStatus("current")
if mibBuilder.loadTexts:
    fsDhcp6ClntIfMaxRetDelay.setUnits("seconds")


class _FsDhcp6ClntIfMaxRetTime_Type(Integer32):
    """Custom type fsDhcp6ClntIfMaxRetTime based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_FsDhcp6ClntIfMaxRetTime_Type.__name__ = "Integer32"
_FsDhcp6ClntIfMaxRetTime_Object = MibTableColumn
fsDhcp6ClntIfMaxRetTime = _FsDhcp6ClntIfMaxRetTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 43, 2, 1, 1, 8),
    _FsDhcp6ClntIfMaxRetTime_Type()
)
fsDhcp6ClntIfMaxRetTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcp6ClntIfMaxRetTime.setStatus("current")
if mibBuilder.loadTexts:
    fsDhcp6ClntIfMaxRetTime.setUnits("seconds")


class _FsDhcp6ClntIfInitRetTime_Type(Integer32):
    """Custom type fsDhcp6ClntIfInitRetTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsDhcp6ClntIfInitRetTime_Type.__name__ = "Integer32"
_FsDhcp6ClntIfInitRetTime_Object = MibTableColumn
fsDhcp6ClntIfInitRetTime = _FsDhcp6ClntIfInitRetTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 43, 2, 1, 1, 9),
    _FsDhcp6ClntIfInitRetTime_Type()
)
fsDhcp6ClntIfInitRetTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcp6ClntIfInitRetTime.setStatus("current")
if mibBuilder.loadTexts:
    fsDhcp6ClntIfInitRetTime.setUnits("seconds")
_FsDhcp6ClntIfCurrRetTime_Type = Integer32
_FsDhcp6ClntIfCurrRetTime_Object = MibTableColumn
fsDhcp6ClntIfCurrRetTime = _FsDhcp6ClntIfCurrRetTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 43, 2, 1, 1, 10),
    _FsDhcp6ClntIfCurrRetTime_Type()
)
fsDhcp6ClntIfCurrRetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcp6ClntIfCurrRetTime.setStatus("current")
if mibBuilder.loadTexts:
    fsDhcp6ClntIfCurrRetTime.setUnits("seconds")


class _FsDhcp6ClntIfMinRefreshTime_Type(Unsigned32):
    """Custom type fsDhcp6ClntIfMinRefreshTime based on Unsigned32"""
    defaultValue = 86400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4294967295),
    )


_FsDhcp6ClntIfMinRefreshTime_Type.__name__ = "Unsigned32"
_FsDhcp6ClntIfMinRefreshTime_Object = MibTableColumn
fsDhcp6ClntIfMinRefreshTime = _FsDhcp6ClntIfMinRefreshTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 43, 2, 1, 1, 11),
    _FsDhcp6ClntIfMinRefreshTime_Type()
)
fsDhcp6ClntIfMinRefreshTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcp6ClntIfMinRefreshTime.setStatus("current")
if mibBuilder.loadTexts:
    fsDhcp6ClntIfMinRefreshTime.setUnits("seconds")


class _FsDhcp6ClntIfCurrRefreshTime_Type(Unsigned32):
    """Custom type fsDhcp6ClntIfCurrRefreshTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4294967295),
    )


_FsDhcp6ClntIfCurrRefreshTime_Type.__name__ = "Unsigned32"
_FsDhcp6ClntIfCurrRefreshTime_Object = MibTableColumn
fsDhcp6ClntIfCurrRefreshTime = _FsDhcp6ClntIfCurrRefreshTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 43, 2, 1, 1, 12),
    _FsDhcp6ClntIfCurrRefreshTime_Type()
)
fsDhcp6ClntIfCurrRefreshTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcp6ClntIfCurrRefreshTime.setStatus("current")
if mibBuilder.loadTexts:
    fsDhcp6ClntIfCurrRefreshTime.setUnits("seconds")


class _FsDhcp6ClntIfRealmName_Type(OctetString):
    """Custom type fsDhcp6ClntIfRealmName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_FsDhcp6ClntIfRealmName_Type.__name__ = "OctetString"
_FsDhcp6ClntIfRealmName_Object = MibTableColumn
fsDhcp6ClntIfRealmName = _FsDhcp6ClntIfRealmName_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 43, 2, 1, 1, 13),
    _FsDhcp6ClntIfRealmName_Type()
)
fsDhcp6ClntIfRealmName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcp6ClntIfRealmName.setStatus("current")


class _FsDhcp6ClntIfKey_Type(OctetString):
    """Custom type fsDhcp6ClntIfKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FsDhcp6ClntIfKey_Type.__name__ = "OctetString"
_FsDhcp6ClntIfKey_Object = MibTableColumn
fsDhcp6ClntIfKey = _FsDhcp6ClntIfKey_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 43, 2, 1, 1, 14),
    _FsDhcp6ClntIfKey_Type()
)
fsDhcp6ClntIfKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcp6ClntIfKey.setStatus("current")


class _FsDhcp6ClntIfKeyId_Type(Unsigned32):
    """Custom type fsDhcp6ClntIfKeyId based on Unsigned32"""
    defaultValue = 1


_FsDhcp6ClntIfKeyId_Type.__name__ = "Unsigned32"
_FsDhcp6ClntIfKeyId_Object = MibTableColumn
fsDhcp6ClntIfKeyId = _FsDhcp6ClntIfKeyId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 43, 2, 1, 1, 15),
    _FsDhcp6ClntIfKeyId_Type()
)
fsDhcp6ClntIfKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcp6ClntIfKeyId.setStatus("current")
_FsDhcp6ClntIfInformOut_Type = Counter32
_FsDhcp6ClntIfInformOut_Object = MibTableColumn
fsDhcp6ClntIfInformOut = _FsDhcp6ClntIfInformOut_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 43, 2, 1, 1, 16),
    _FsDhcp6ClntIfInformOut_Type()
)
fsDhcp6ClntIfInformOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcp6ClntIfInformOut.setStatus("current")
_FsDhcp6ClntIfReplyIn_Type = Counter32
_FsDhcp6ClntIfReplyIn_Object = MibTableColumn
fsDhcp6ClntIfReplyIn = _FsDhcp6ClntIfReplyIn_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 43, 2, 1, 1, 17),
    _FsDhcp6ClntIfReplyIn_Type()
)
fsDhcp6ClntIfReplyIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcp6ClntIfReplyIn.setStatus("current")
_FsDhcp6ClntIfInvalidPktIn_Type = Counter32
_FsDhcp6ClntIfInvalidPktIn_Object = MibTableColumn
fsDhcp6ClntIfInvalidPktIn = _FsDhcp6ClntIfInvalidPktIn_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 43, 2, 1, 1, 18),
    _FsDhcp6ClntIfInvalidPktIn_Type()
)
fsDhcp6ClntIfInvalidPktIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcp6ClntIfInvalidPktIn.setStatus("current")
_FsDhcp6ClntIfHmacFailCount_Type = Counter32
_FsDhcp6ClntIfHmacFailCount_Object = MibTableColumn
fsDhcp6ClntIfHmacFailCount = _FsDhcp6ClntIfHmacFailCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 43, 2, 1, 1, 19),
    _FsDhcp6ClntIfHmacFailCount_Type()
)
fsDhcp6ClntIfHmacFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcp6ClntIfHmacFailCount.setStatus("current")
_FsDhcp6ClntIfCounterRest_Type = TruthValue
_FsDhcp6ClntIfCounterRest_Object = MibTableColumn
fsDhcp6ClntIfCounterRest = _FsDhcp6ClntIfCounterRest_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 43, 2, 1, 1, 20),
    _FsDhcp6ClntIfCounterRest_Type()
)
fsDhcp6ClntIfCounterRest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcp6ClntIfCounterRest.setStatus("current")
_FsDhcp6ClntIfRowStatus_Type = RowStatus
_FsDhcp6ClntIfRowStatus_Object = MibTableColumn
fsDhcp6ClntIfRowStatus = _FsDhcp6ClntIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 43, 2, 1, 1, 21),
    _FsDhcp6ClntIfRowStatus_Type()
)
fsDhcp6ClntIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcp6ClntIfRowStatus.setStatus("current")
_FsDhcp6ClntOptionTable_Object = MibTable
fsDhcp6ClntOptionTable = _FsDhcp6ClntOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 43, 2, 2)
)
if mibBuilder.loadTexts:
    fsDhcp6ClntOptionTable.setStatus("current")
_FsDhcp6ClntOptionEntry_Object = MibTableRow
fsDhcp6ClntOptionEntry = _FsDhcp6ClntOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 43, 2, 2, 1)
)
fsDhcp6ClntOptionEntry.setIndexNames(
    (0, "ARICENT-DHCPv6-CLIENT-MIB", "fsDhcp6ClntIfIndex"),
    (0, "ARICENT-DHCPv6-CLIENT-MIB", "fsDhcp6ClntOptionType"),
)
if mibBuilder.loadTexts:
    fsDhcp6ClntOptionEntry.setStatus("current")


class _FsDhcp6ClntOptionType_Type(Integer32):
    """Custom type fsDhcp6ClntOptionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsDhcp6ClntOptionType_Type.__name__ = "Integer32"
_FsDhcp6ClntOptionType_Object = MibTableColumn
fsDhcp6ClntOptionType = _FsDhcp6ClntOptionType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 43, 2, 2, 1, 1),
    _FsDhcp6ClntOptionType_Type()
)
fsDhcp6ClntOptionType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDhcp6ClntOptionType.setStatus("current")
_FsDhcp6ClntOptionLength_Type = Integer32
_FsDhcp6ClntOptionLength_Object = MibTableColumn
fsDhcp6ClntOptionLength = _FsDhcp6ClntOptionLength_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 43, 2, 2, 1, 2),
    _FsDhcp6ClntOptionLength_Type()
)
fsDhcp6ClntOptionLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcp6ClntOptionLength.setStatus("current")


class _FsDhcp6ClntOptionValue_Type(OctetString):
    """Custom type fsDhcp6ClntOptionValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_FsDhcp6ClntOptionValue_Type.__name__ = "OctetString"
_FsDhcp6ClntOptionValue_Object = MibTableColumn
fsDhcp6ClntOptionValue = _FsDhcp6ClntOptionValue_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 43, 2, 2, 1, 3),
    _FsDhcp6ClntOptionValue_Type()
)
fsDhcp6ClntOptionValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcp6ClntOptionValue.setStatus("current")

# Managed Objects groups


# Notification objects

fsDhcp6ClntInvalidPacketTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 43, 0, 1)
)
fsDhcp6ClntInvalidPacketTrap.setObjects(
    ("ARICENT-DHCPv6-CLIENT-MIB", "fsDhcp6ClntIfInvalidPktIn")
)
if mibBuilder.loadTexts:
    fsDhcp6ClntInvalidPacketTrap.setStatus(
        "current"
    )

fsDhcp6ClntHmacAuthenticationFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 43, 0, 2)
)
fsDhcp6ClntHmacAuthenticationFailTrap.setObjects(
    ("ARICENT-DHCPv6-CLIENT-MIB", "fsDhcp6ClntIfHmacFailCount")
)
if mibBuilder.loadTexts:
    fsDhcp6ClntHmacAuthenticationFailTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-DHCPv6-CLIENT-MIB",
    **{"FsDhcp6ClntDuidValue": FsDhcp6ClntDuidValue,
       "FsDhcp6ClntDuidType": FsDhcp6ClntDuidType,
       "fsdhcpv6clnt": fsdhcpv6clnt,
       "fsDhcp6ClntNotify": fsDhcp6ClntNotify,
       "fsDhcp6ClntInvalidPacketTrap": fsDhcp6ClntInvalidPacketTrap,
       "fsDhcp6ClntHmacAuthenticationFailTrap": fsDhcp6ClntHmacAuthenticationFailTrap,
       "fsDhcp6ClntSystem": fsDhcp6ClntSystem,
       "fsDhcp6ClntTrapAdminControl": fsDhcp6ClntTrapAdminControl,
       "fsDhcp6ClntDebugTrace": fsDhcp6ClntDebugTrace,
       "fsDhcp6ClntSysLogAdminStatus": fsDhcp6ClntSysLogAdminStatus,
       "fsDhcp6ClntListenPort": fsDhcp6ClntListenPort,
       "fsDhcp6ClntTransmitPort": fsDhcp6ClntTransmitPort,
       "fsDhcp6ClntConfig": fsDhcp6ClntConfig,
       "fsDhcp6ClntIfTable": fsDhcp6ClntIfTable,
       "fsDhcp6ClntIfEntry": fsDhcp6ClntIfEntry,
       "fsDhcp6ClntIfIndex": fsDhcp6ClntIfIndex,
       "fsDhcp6ClntIfSrvAddress": fsDhcp6ClntIfSrvAddress,
       "fsDhcp6ClntIfDuidType": fsDhcp6ClntIfDuidType,
       "fsDhcp6ClntIfDuid": fsDhcp6ClntIfDuid,
       "fsDhcp6ClntIfDuidIfIndex": fsDhcp6ClntIfDuidIfIndex,
       "fsDhcp6ClntIfMaxRetCount": fsDhcp6ClntIfMaxRetCount,
       "fsDhcp6ClntIfMaxRetDelay": fsDhcp6ClntIfMaxRetDelay,
       "fsDhcp6ClntIfMaxRetTime": fsDhcp6ClntIfMaxRetTime,
       "fsDhcp6ClntIfInitRetTime": fsDhcp6ClntIfInitRetTime,
       "fsDhcp6ClntIfCurrRetTime": fsDhcp6ClntIfCurrRetTime,
       "fsDhcp6ClntIfMinRefreshTime": fsDhcp6ClntIfMinRefreshTime,
       "fsDhcp6ClntIfCurrRefreshTime": fsDhcp6ClntIfCurrRefreshTime,
       "fsDhcp6ClntIfRealmName": fsDhcp6ClntIfRealmName,
       "fsDhcp6ClntIfKey": fsDhcp6ClntIfKey,
       "fsDhcp6ClntIfKeyId": fsDhcp6ClntIfKeyId,
       "fsDhcp6ClntIfInformOut": fsDhcp6ClntIfInformOut,
       "fsDhcp6ClntIfReplyIn": fsDhcp6ClntIfReplyIn,
       "fsDhcp6ClntIfInvalidPktIn": fsDhcp6ClntIfInvalidPktIn,
       "fsDhcp6ClntIfHmacFailCount": fsDhcp6ClntIfHmacFailCount,
       "fsDhcp6ClntIfCounterRest": fsDhcp6ClntIfCounterRest,
       "fsDhcp6ClntIfRowStatus": fsDhcp6ClntIfRowStatus,
       "fsDhcp6ClntOptionTable": fsDhcp6ClntOptionTable,
       "fsDhcp6ClntOptionEntry": fsDhcp6ClntOptionEntry,
       "fsDhcp6ClntOptionType": fsDhcp6ClntOptionType,
       "fsDhcp6ClntOptionLength": fsDhcp6ClntOptionLength,
       "fsDhcp6ClntOptionValue": fsDhcp6ClntOptionValue}
)
