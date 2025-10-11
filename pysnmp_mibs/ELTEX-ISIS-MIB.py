# SNMP MIB module (ELTEX-ISIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-ISIS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:50:46 2025
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

(eltexLtd,) = mibBuilder.importSymbols(
    "ELTEX-SMI-ACTUAL",
    "eltexLtd")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

eltexIsisMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 55)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EltexIsisSystemID(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6



class EltexIsisAdminState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )



class EltexNETAddress(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )



class EltexIsisOperStatus(TextualConvention, Integer32):
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
        *(("operStatusUp", 1),
          ("operStatusDown", 2),
          ("operStatusGoingUp", 3),
          ("operStatusGoingDown", 4),
          ("operStatusActFailed", 5))
    )



class EltexIsisISLevel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("area", 1),
          ("domain", 2))
    )



class EltexIsisLinkStatePDUID(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class EltexIsisISPriority(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )



class EltexIsisMetricStyle(TextualConvention, Integer32):
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
        *(("narrow", 1),
          ("wide", 2),
          ("both", 3))
    )



class EltexIsisWideMetric(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )



class EltexIsisAuthType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("simplePassword", 1),
          ("hmac-md5", 2))
    )



class EltexIsisHelloPaddingAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("adaptive", 2))
    )



# MIB Managed Objects in the order of their OIDs

_EltexIsisObjects_ObjectIdentity = ObjectIdentity
eltexIsisObjects = _EltexIsisObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1)
)
_EltexIsisSystem_ObjectIdentity = ObjectIdentity
eltexIsisSystem = _EltexIsisSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 1)
)
_EltexIsisSysTable_Object = MibTable
eltexIsisSysTable = _EltexIsisSysTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 1, 1)
)
if mibBuilder.loadTexts:
    eltexIsisSysTable.setStatus("current")
_EltexIsisSysEntry_Object = MibTableRow
eltexIsisSysEntry = _EltexIsisSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 1, 1, 1)
)
eltexIsisSysEntry.setIndexNames(
    (0, "ELTEX-ISIS-MIB", "eltexIsisSysInstance"),
)
if mibBuilder.loadTexts:
    eltexIsisSysEntry.setStatus("current")


class _EltexIsisSysInstance_Type(Integer32):
    """Custom type eltexIsisSysInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EltexIsisSysInstance_Type.__name__ = "Integer32"
_EltexIsisSysInstance_Object = MibTableColumn
eltexIsisSysInstance = _EltexIsisSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 1, 1, 1, 1),
    _EltexIsisSysInstance_Type()
)
eltexIsisSysInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexIsisSysInstance.setStatus("current")


class _EltexIsisSysType_Type(Integer32):
    """Custom type eltexIsisSysType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("reserved", 0),
          ("level1IS", 1),
          ("level2IS", 2),
          ("level1L2IS", 3))
    )


_EltexIsisSysType_Type.__name__ = "Integer32"
_EltexIsisSysType_Object = MibTableColumn
eltexIsisSysType = _EltexIsisSysType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 1, 1, 1, 2),
    _EltexIsisSysType_Type()
)
eltexIsisSysType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexIsisSysType.setStatus("current")
_EltexIsisSysID_Type = EltexIsisSystemID
_EltexIsisSysID_Object = MibTableColumn
eltexIsisSysID = _EltexIsisSysID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 1, 1, 1, 3),
    _EltexIsisSysID_Type()
)
eltexIsisSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIsisSysID.setStatus("current")


class _EltexIsisSysAdminState_Type(EltexIsisAdminState):
    """Custom type eltexIsisSysAdminState based on EltexIsisAdminState"""
    defaultValue = 2


_EltexIsisSysAdminState_Type.__name__ = "EltexIsisAdminState"
_EltexIsisSysAdminState_Object = MibTableColumn
eltexIsisSysAdminState = _EltexIsisSysAdminState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 1, 1, 1, 4),
    _EltexIsisSysAdminState_Type()
)
eltexIsisSysAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexIsisSysAdminState.setStatus("current")
_EltexIsisSysOperState_Type = EltexIsisOperStatus
_EltexIsisSysOperState_Object = MibTableColumn
eltexIsisSysOperState = _EltexIsisSysOperState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 1, 1, 1, 5),
    _EltexIsisSysOperState_Type()
)
eltexIsisSysOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIsisSysOperState.setStatus("current")
_EltexIsisSysRowStatus_Type = RowStatus
_EltexIsisSysRowStatus_Object = MibTableColumn
eltexIsisSysRowStatus = _EltexIsisSysRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 1, 1, 1, 6),
    _EltexIsisSysRowStatus_Type()
)
eltexIsisSysRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexIsisSysRowStatus.setStatus("current")


class _EltexIsisSysMaxAge_Type(Unsigned32):
    """Custom type eltexIsisSysMaxAge based on Unsigned32"""
    defaultValue = 1200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(350, 65535),
    )


_EltexIsisSysMaxAge_Type.__name__ = "Unsigned32"
_EltexIsisSysMaxAge_Object = MibTableColumn
eltexIsisSysMaxAge = _EltexIsisSysMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 1, 1, 1, 7),
    _EltexIsisSysMaxAge_Type()
)
eltexIsisSysMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIsisSysMaxAge.setStatus("current")


class _EltexIsisSysMaxLSPGenInt_Type(Unsigned32):
    """Custom type eltexIsisSysMaxLSPGenInt based on Unsigned32"""
    defaultValue = 900

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65235),
    )


_EltexIsisSysMaxLSPGenInt_Type.__name__ = "Unsigned32"
_EltexIsisSysMaxLSPGenInt_Object = MibTableColumn
eltexIsisSysMaxLSPGenInt = _EltexIsisSysMaxLSPGenInt_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 1, 1, 1, 8),
    _EltexIsisSysMaxLSPGenInt_Type()
)
eltexIsisSysMaxLSPGenInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIsisSysMaxLSPGenInt.setStatus("current")


class _EltexIsisSysCalcMaxDelay_Type(Unsigned32):
    """Custom type eltexIsisSysCalcMaxDelay based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_EltexIsisSysCalcMaxDelay_Type.__name__ = "Unsigned32"
_EltexIsisSysCalcMaxDelay_Object = MibTableColumn
eltexIsisSysCalcMaxDelay = _EltexIsisSysCalcMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 1, 1, 1, 9),
    _EltexIsisSysCalcMaxDelay_Type()
)
eltexIsisSysCalcMaxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIsisSysCalcMaxDelay.setStatus("current")


class _EltexIsisSysCalcThrshUpdStart_Type(Unsigned32):
    """Custom type eltexIsisSysCalcThrshUpdStart based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_EltexIsisSysCalcThrshUpdStart_Type.__name__ = "Unsigned32"
_EltexIsisSysCalcThrshUpdStart_Object = MibTableColumn
eltexIsisSysCalcThrshUpdStart = _EltexIsisSysCalcThrshUpdStart_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 1, 1, 1, 10),
    _EltexIsisSysCalcThrshUpdStart_Type()
)
eltexIsisSysCalcThrshUpdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIsisSysCalcThrshUpdStart.setStatus("current")


class _EltexIsisSysCalcThrshUpdRestart_Type(Unsigned32):
    """Custom type eltexIsisSysCalcThrshUpdRestart based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_EltexIsisSysCalcThrshUpdRestart_Type.__name__ = "Unsigned32"
_EltexIsisSysCalcThrshUpdRestart_Object = MibTableColumn
eltexIsisSysCalcThrshUpdRestart = _EltexIsisSysCalcThrshUpdRestart_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 1, 1, 1, 11),
    _EltexIsisSysCalcThrshUpdRestart_Type()
)
eltexIsisSysCalcThrshUpdRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIsisSysCalcThrshUpdRestart.setStatus("current")


class _EltexIsisSysCalcThrshRestartLimit_Type(Unsigned32):
    """Custom type eltexIsisSysCalcThrshRestartLimit based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_EltexIsisSysCalcThrshRestartLimit_Type.__name__ = "Unsigned32"
_EltexIsisSysCalcThrshRestartLimit_Object = MibTableColumn
eltexIsisSysCalcThrshRestartLimit = _EltexIsisSysCalcThrshRestartLimit_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 1, 1, 1, 12),
    _EltexIsisSysCalcThrshRestartLimit_Type()
)
eltexIsisSysCalcThrshRestartLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIsisSysCalcThrshRestartLimit.setStatus("current")


class _EltexIsisSysHostNameDynamic_Type(TruthValue):
    """Custom type eltexIsisSysHostNameDynamic based on TruthValue"""
    defaultValue = 1


_EltexIsisSysHostNameDynamic_Type.__name__ = "TruthValue"
_EltexIsisSysHostNameDynamic_Object = MibTableColumn
eltexIsisSysHostNameDynamic = _EltexIsisSysHostNameDynamic_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 1, 1, 1, 13),
    _EltexIsisSysHostNameDynamic_Type()
)
eltexIsisSysHostNameDynamic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIsisSysHostNameDynamic.setStatus("current")
_EltexIsisNetAddrTable_Object = MibTable
eltexIsisNetAddrTable = _EltexIsisNetAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 1, 2)
)
if mibBuilder.loadTexts:
    eltexIsisNetAddrTable.setStatus("current")
_EltexIsisNetAddrEntry_Object = MibTableRow
eltexIsisNetAddrEntry = _EltexIsisNetAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 1, 2, 1)
)
eltexIsisNetAddrEntry.setIndexNames(
    (0, "ELTEX-ISIS-MIB", "eltexIsisSysInstance"),
    (0, "ELTEX-ISIS-MIB", "eltexIsisNetAddr"),
)
if mibBuilder.loadTexts:
    eltexIsisNetAddrEntry.setStatus("current")
_EltexIsisNetAddr_Type = EltexNETAddress
_EltexIsisNetAddr_Object = MibTableColumn
eltexIsisNetAddr = _EltexIsisNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 1, 2, 1, 1),
    _EltexIsisNetAddr_Type()
)
eltexIsisNetAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexIsisNetAddr.setStatus("current")
_EltexIsisNetAddrRowStatus_Type = RowStatus
_EltexIsisNetAddrRowStatus_Object = MibTableColumn
eltexIsisNetAddrRowStatus = _EltexIsisNetAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 1, 2, 1, 2),
    _EltexIsisNetAddrRowStatus_Type()
)
eltexIsisNetAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexIsisNetAddrRowStatus.setStatus("current")
_EltexIsisSysLevelTable_Object = MibTable
eltexIsisSysLevelTable = _EltexIsisSysLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 1, 3)
)
if mibBuilder.loadTexts:
    eltexIsisSysLevelTable.setStatus("current")
_EltexIsisSysLevelEntry_Object = MibTableRow
eltexIsisSysLevelEntry = _EltexIsisSysLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 1, 3, 1)
)
eltexIsisSysLevelEntry.setIndexNames(
    (0, "ELTEX-ISIS-MIB", "eltexIsisSysInstance"),
    (0, "ELTEX-ISIS-MIB", "eltexIsisSysLevelIndex"),
)
if mibBuilder.loadTexts:
    eltexIsisSysLevelEntry.setStatus("current")


class _EltexIsisSysLevelIndex_Type(Integer32):
    """Custom type eltexIsisSysLevelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level1IS", 1),
          ("level2IS", 2))
    )


_EltexIsisSysLevelIndex_Type.__name__ = "Integer32"
_EltexIsisSysLevelIndex_Object = MibTableColumn
eltexIsisSysLevelIndex = _EltexIsisSysLevelIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 1, 3, 1, 1),
    _EltexIsisSysLevelIndex_Type()
)
eltexIsisSysLevelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexIsisSysLevelIndex.setStatus("current")


class _EltexIsisSysLevelMinLSPGenInt_Type(Unsigned32):
    """Custom type eltexIsisSysLevelMinLSPGenInt based on Unsigned32"""
    defaultValue = 30000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 65535000),
    )


_EltexIsisSysLevelMinLSPGenInt_Type.__name__ = "Unsigned32"
_EltexIsisSysLevelMinLSPGenInt_Object = MibTableColumn
eltexIsisSysLevelMinLSPGenInt = _EltexIsisSysLevelMinLSPGenInt_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 1, 3, 1, 2),
    _EltexIsisSysLevelMinLSPGenInt_Type()
)
eltexIsisSysLevelMinLSPGenInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIsisSysLevelMinLSPGenInt.setStatus("current")


class _EltexIsisSysLevelMetricStyle_Type(EltexIsisMetricStyle):
    """Custom type eltexIsisSysLevelMetricStyle based on EltexIsisMetricStyle"""
    defaultValue = 3


_EltexIsisSysLevelMetricStyle_Type.__name__ = "EltexIsisMetricStyle"
_EltexIsisSysLevelMetricStyle_Object = MibTableColumn
eltexIsisSysLevelMetricStyle = _EltexIsisSysLevelMetricStyle_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 1, 3, 1, 3),
    _EltexIsisSysLevelMetricStyle_Type()
)
eltexIsisSysLevelMetricStyle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIsisSysLevelMetricStyle.setStatus("current")
_EltexIsisSysLevelAuthType_Type = EltexIsisAuthType
_EltexIsisSysLevelAuthType_Object = MibTableColumn
eltexIsisSysLevelAuthType = _EltexIsisSysLevelAuthType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 1, 3, 1, 4),
    _EltexIsisSysLevelAuthType_Type()
)
eltexIsisSysLevelAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIsisSysLevelAuthType.setStatus("current")


class _EltexIsisSysLevelAuthKey_Type(OctetString):
    """Custom type eltexIsisSysLevelAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_EltexIsisSysLevelAuthKey_Type.__name__ = "OctetString"
_EltexIsisSysLevelAuthKey_Object = MibTableColumn
eltexIsisSysLevelAuthKey = _EltexIsisSysLevelAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 1, 3, 1, 5),
    _EltexIsisSysLevelAuthKey_Type()
)
eltexIsisSysLevelAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIsisSysLevelAuthKey.setStatus("current")


class _EltexIsisSysLevelAuthKeyChain_Type(OctetString):
    """Custom type eltexIsisSysLevelAuthKeyChain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EltexIsisSysLevelAuthKeyChain_Type.__name__ = "OctetString"
_EltexIsisSysLevelAuthKeyChain_Object = MibTableColumn
eltexIsisSysLevelAuthKeyChain = _EltexIsisSysLevelAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 1, 3, 1, 6),
    _EltexIsisSysLevelAuthKeyChain_Type()
)
eltexIsisSysLevelAuthKeyChain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIsisSysLevelAuthKeyChain.setStatus("current")


class _EltexIsisSysLevelOrigLSPBuffSize_Type(Unsigned32):
    """Custom type eltexIsisSysLevelOrigLSPBuffSize based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 9000),
    )


_EltexIsisSysLevelOrigLSPBuffSize_Type.__name__ = "Unsigned32"
_EltexIsisSysLevelOrigLSPBuffSize_Object = MibTableColumn
eltexIsisSysLevelOrigLSPBuffSize = _EltexIsisSysLevelOrigLSPBuffSize_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 1, 3, 1, 7),
    _EltexIsisSysLevelOrigLSPBuffSize_Type()
)
eltexIsisSysLevelOrigLSPBuffSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIsisSysLevelOrigLSPBuffSize.setStatus("current")
_EltexIsisRouterTable_Object = MibTable
eltexIsisRouterTable = _EltexIsisRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 1, 5)
)
if mibBuilder.loadTexts:
    eltexIsisRouterTable.setStatus("current")
_EltexIsisRouterEntry_Object = MibTableRow
eltexIsisRouterEntry = _EltexIsisRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 1, 5, 1)
)
eltexIsisRouterEntry.setIndexNames(
    (0, "ELTEX-ISIS-MIB", "eltexIsisSysInstance"),
    (0, "ELTEX-ISIS-MIB", "eltexIsisRouterSysID"),
    (0, "ELTEX-ISIS-MIB", "eltexIsisRouterLevel"),
)
if mibBuilder.loadTexts:
    eltexIsisRouterEntry.setStatus("current")
_EltexIsisRouterSysID_Type = EltexIsisSystemID
_EltexIsisRouterSysID_Object = MibTableColumn
eltexIsisRouterSysID = _EltexIsisRouterSysID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 1, 5, 1, 1),
    _EltexIsisRouterSysID_Type()
)
eltexIsisRouterSysID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexIsisRouterSysID.setStatus("current")
_EltexIsisRouterLevel_Type = EltexIsisISLevel
_EltexIsisRouterLevel_Object = MibTableColumn
eltexIsisRouterLevel = _EltexIsisRouterLevel_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 1, 5, 1, 2),
    _EltexIsisRouterLevel_Type()
)
eltexIsisRouterLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexIsisRouterLevel.setStatus("current")
_EltexIsisRouterHostName_Type = SnmpAdminString
_EltexIsisRouterHostName_Object = MibTableColumn
eltexIsisRouterHostName = _EltexIsisRouterHostName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 1, 5, 1, 3),
    _EltexIsisRouterHostName_Type()
)
eltexIsisRouterHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIsisRouterHostName.setStatus("current")
_EltexIsisCirc_ObjectIdentity = ObjectIdentity
eltexIsisCirc = _EltexIsisCirc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 2)
)
_EltexIsisCircTable_Object = MibTable
eltexIsisCircTable = _EltexIsisCircTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eltexIsisCircTable.setStatus("current")
_EltexIsisCircEntry_Object = MibTableRow
eltexIsisCircEntry = _EltexIsisCircEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 2, 1, 1)
)
eltexIsisCircEntry.setIndexNames(
    (0, "ELTEX-ISIS-MIB", "eltexIsisSysInstance"),
    (0, "ELTEX-ISIS-MIB", "eltexIsisCircIfindex"),
)
if mibBuilder.loadTexts:
    eltexIsisCircEntry.setStatus("current")
_EltexIsisCircIfindex_Type = InterfaceIndex
_EltexIsisCircIfindex_Object = MibTableColumn
eltexIsisCircIfindex = _EltexIsisCircIfindex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 2, 1, 1, 1),
    _EltexIsisCircIfindex_Type()
)
eltexIsisCircIfindex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexIsisCircIfindex.setStatus("current")
_EltexIsisCircRowStatus_Type = RowStatus
_EltexIsisCircRowStatus_Object = MibTableColumn
eltexIsisCircRowStatus = _EltexIsisCircRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 2, 1, 1, 2),
    _EltexIsisCircRowStatus_Type()
)
eltexIsisCircRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexIsisCircRowStatus.setStatus("current")


class _EltexIsisCircAdminState_Type(EltexIsisAdminState):
    """Custom type eltexIsisCircAdminState based on EltexIsisAdminState"""
    defaultValue = 2


_EltexIsisCircAdminState_Type.__name__ = "EltexIsisAdminState"
_EltexIsisCircAdminState_Object = MibTableColumn
eltexIsisCircAdminState = _EltexIsisCircAdminState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 2, 1, 1, 3),
    _EltexIsisCircAdminState_Type()
)
eltexIsisCircAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexIsisCircAdminState.setStatus("current")
_EltexIsisCircOperState_Type = EltexIsisOperStatus
_EltexIsisCircOperState_Object = MibTableColumn
eltexIsisCircOperState = _EltexIsisCircOperState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 2, 1, 1, 4),
    _EltexIsisCircOperState_Type()
)
eltexIsisCircOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIsisCircOperState.setStatus("current")


class _EltexIsisCircLevel_Type(Integer32):
    """Custom type eltexIsisCircLevel based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("reserved", 0),
          ("level1", 1),
          ("level2", 2),
          ("level1L2", 3))
    )


_EltexIsisCircLevel_Type.__name__ = "Integer32"
_EltexIsisCircLevel_Object = MibTableColumn
eltexIsisCircLevel = _EltexIsisCircLevel_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 2, 1, 1, 5),
    _EltexIsisCircLevel_Type()
)
eltexIsisCircLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexIsisCircLevel.setStatus("current")


class _EltexIsisCircPassiveCircuit_Type(TruthValue):
    """Custom type eltexIsisCircPassiveCircuit based on TruthValue"""
    defaultValue = 2


_EltexIsisCircPassiveCircuit_Type.__name__ = "TruthValue"
_EltexIsisCircPassiveCircuit_Object = MibTableColumn
eltexIsisCircPassiveCircuit = _EltexIsisCircPassiveCircuit_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 2, 1, 1, 6),
    _EltexIsisCircPassiveCircuit_Type()
)
eltexIsisCircPassiveCircuit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexIsisCircPassiveCircuit.setStatus("current")


class _EltexIsisCircPtToPt_Type(TruthValue):
    """Custom type eltexIsisCircPtToPt based on TruthValue"""
    defaultValue = 2


_EltexIsisCircPtToPt_Type.__name__ = "TruthValue"
_EltexIsisCircPtToPt_Object = MibTableColumn
eltexIsisCircPtToPt = _EltexIsisCircPtToPt_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 2, 1, 1, 7),
    _EltexIsisCircPtToPt_Type()
)
eltexIsisCircPtToPt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIsisCircPtToPt.setStatus("current")


class _EltexIsisCircHelloPadding_Type(EltexIsisHelloPaddingAction):
    """Custom type eltexIsisCircHelloPadding based on EltexIsisHelloPaddingAction"""
    defaultValue = 1


_EltexIsisCircHelloPadding_Type.__name__ = "EltexIsisHelloPaddingAction"
_EltexIsisCircHelloPadding_Object = MibTableColumn
eltexIsisCircHelloPadding = _EltexIsisCircHelloPadding_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 2, 1, 1, 8),
    _EltexIsisCircHelloPadding_Type()
)
eltexIsisCircHelloPadding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIsisCircHelloPadding.setStatus("current")


class _EltexIsisCircPDUBuffSize_Type(Unsigned32):
    """Custom type eltexIsisCircPDUBuffSize based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 9000),
    )


_EltexIsisCircPDUBuffSize_Type.__name__ = "Unsigned32"
_EltexIsisCircPDUBuffSize_Object = MibTableColumn
eltexIsisCircPDUBuffSize = _EltexIsisCircPDUBuffSize_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 2, 1, 1, 9),
    _EltexIsisCircPDUBuffSize_Type()
)
eltexIsisCircPDUBuffSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIsisCircPDUBuffSize.setStatus("current")
_EltexIsisCircLevelTable_Object = MibTable
eltexIsisCircLevelTable = _EltexIsisCircLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 2, 2)
)
if mibBuilder.loadTexts:
    eltexIsisCircLevelTable.setStatus("current")
_EltexIsisCircLevelEntry_Object = MibTableRow
eltexIsisCircLevelEntry = _EltexIsisCircLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 2, 2, 1)
)
eltexIsisCircLevelEntry.setIndexNames(
    (0, "ELTEX-ISIS-MIB", "eltexIsisSysInstance"),
    (0, "ELTEX-ISIS-MIB", "eltexIsisCircIfindex"),
    (0, "ELTEX-ISIS-MIB", "eltexIsisCircLevelIndex"),
)
if mibBuilder.loadTexts:
    eltexIsisCircLevelEntry.setStatus("current")


class _EltexIsisCircLevelIndex_Type(Integer32):
    """Custom type eltexIsisCircLevelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level1IS", 1),
          ("level2IS", 2))
    )


_EltexIsisCircLevelIndex_Type.__name__ = "Integer32"
_EltexIsisCircLevelIndex_Object = MibTableColumn
eltexIsisCircLevelIndex = _EltexIsisCircLevelIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 2, 2, 1, 1),
    _EltexIsisCircLevelIndex_Type()
)
eltexIsisCircLevelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexIsisCircLevelIndex.setStatus("current")
_EltexIsisCircLevelRowStatus_Type = RowStatus
_EltexIsisCircLevelRowStatus_Object = MibTableColumn
eltexIsisCircLevelRowStatus = _EltexIsisCircLevelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 2, 2, 1, 2),
    _EltexIsisCircLevelRowStatus_Type()
)
eltexIsisCircLevelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexIsisCircLevelRowStatus.setStatus("current")


class _EltexIsisCircLevelMetric_Type(EltexIsisWideMetric):
    """Custom type eltexIsisCircLevelMetric based on EltexIsisWideMetric"""
    defaultValue = 10


_EltexIsisCircLevelMetric_Type.__name__ = "EltexIsisWideMetric"
_EltexIsisCircLevelMetric_Object = MibTableColumn
eltexIsisCircLevelMetric = _EltexIsisCircLevelMetric_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 2, 2, 1, 3),
    _EltexIsisCircLevelMetric_Type()
)
eltexIsisCircLevelMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIsisCircLevelMetric.setStatus("current")
_EltexIsisCircLevelAuthType_Type = EltexIsisAuthType
_EltexIsisCircLevelAuthType_Object = MibTableColumn
eltexIsisCircLevelAuthType = _EltexIsisCircLevelAuthType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 2, 2, 1, 4),
    _EltexIsisCircLevelAuthType_Type()
)
eltexIsisCircLevelAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIsisCircLevelAuthType.setStatus("current")


class _EltexIsisCircLevelAuthKey_Type(OctetString):
    """Custom type eltexIsisCircLevelAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_EltexIsisCircLevelAuthKey_Type.__name__ = "OctetString"
_EltexIsisCircLevelAuthKey_Object = MibTableColumn
eltexIsisCircLevelAuthKey = _EltexIsisCircLevelAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 2, 2, 1, 5),
    _EltexIsisCircLevelAuthKey_Type()
)
eltexIsisCircLevelAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIsisCircLevelAuthKey.setStatus("current")


class _EltexIsisCircLevelAuthKeyChain_Type(OctetString):
    """Custom type eltexIsisCircLevelAuthKeyChain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EltexIsisCircLevelAuthKeyChain_Type.__name__ = "OctetString"
_EltexIsisCircLevelAuthKeyChain_Object = MibTableColumn
eltexIsisCircLevelAuthKeyChain = _EltexIsisCircLevelAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 2, 2, 1, 6),
    _EltexIsisCircLevelAuthKeyChain_Type()
)
eltexIsisCircLevelAuthKeyChain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIsisCircLevelAuthKeyChain.setStatus("current")
_EltexIsisCircLevelStatusTable_Object = MibTable
eltexIsisCircLevelStatusTable = _EltexIsisCircLevelStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 2, 4)
)
if mibBuilder.loadTexts:
    eltexIsisCircLevelStatusTable.setStatus("current")
_EltexIsisCircLevelStatusEntry_Object = MibTableRow
eltexIsisCircLevelStatusEntry = _EltexIsisCircLevelStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 2, 4, 1)
)
eltexIsisCircLevelStatusEntry.setIndexNames(
    (0, "ELTEX-ISIS-MIB", "eltexIsisSysInstance"),
    (0, "ELTEX-ISIS-MIB", "eltexIsisCircIfindex"),
    (0, "ELTEX-ISIS-MIB", "eltexIsisCircLevelIndex"),
)
if mibBuilder.loadTexts:
    eltexIsisCircLevelStatusEntry.setStatus("current")
_EltexIsisCircLevelStatusMetric_Type = Unsigned32
_EltexIsisCircLevelStatusMetric_Object = MibTableColumn
eltexIsisCircLevelStatusMetric = _EltexIsisCircLevelStatusMetric_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 2, 4, 1, 1),
    _EltexIsisCircLevelStatusMetric_Type()
)
eltexIsisCircLevelStatusMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIsisCircLevelStatusMetric.setStatus("current")
_EltexIsisISAdj_ObjectIdentity = ObjectIdentity
eltexIsisISAdj = _EltexIsisISAdj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 3)
)
_EltexIsisISAdjTable_Object = MibTable
eltexIsisISAdjTable = _EltexIsisISAdjTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 3, 1)
)
if mibBuilder.loadTexts:
    eltexIsisISAdjTable.setStatus("current")
_EltexIsisISAdjEntry_Object = MibTableRow
eltexIsisISAdjEntry = _EltexIsisISAdjEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 3, 1, 1)
)
eltexIsisISAdjEntry.setIndexNames(
    (0, "ELTEX-ISIS-MIB", "eltexIsisSysInstance"),
    (0, "ELTEX-ISIS-MIB", "eltexIsisCircIfindex"),
    (0, "ELTEX-ISIS-MIB", "eltexIsisISAdjIndex"),
)
if mibBuilder.loadTexts:
    eltexIsisISAdjEntry.setStatus("current")


class _EltexIsisISAdjIndex_Type(Integer32):
    """Custom type eltexIsisISAdjIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000000),
    )


_EltexIsisISAdjIndex_Type.__name__ = "Integer32"
_EltexIsisISAdjIndex_Object = MibTableColumn
eltexIsisISAdjIndex = _EltexIsisISAdjIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 3, 1, 1, 1),
    _EltexIsisISAdjIndex_Type()
)
eltexIsisISAdjIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexIsisISAdjIndex.setStatus("current")


class _EltexIsisISAdjState_Type(Integer32):
    """Custom type eltexIsisISAdjState based on Integer32"""
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
        *(("down", 1),
          ("initializing", 2),
          ("up", 3),
          ("failed", 4))
    )


_EltexIsisISAdjState_Type.__name__ = "Integer32"
_EltexIsisISAdjState_Object = MibTableColumn
eltexIsisISAdjState = _EltexIsisISAdjState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 3, 1, 1, 2),
    _EltexIsisISAdjState_Type()
)
eltexIsisISAdjState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIsisISAdjState.setStatus("current")


class _EltexIsisISAdj3WayState_Type(Integer32):
    """Custom type eltexIsisISAdj3WayState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 0),
          ("initializing", 1),
          ("down", 2),
          ("failed", 3))
    )


_EltexIsisISAdj3WayState_Type.__name__ = "Integer32"
_EltexIsisISAdj3WayState_Object = MibTableColumn
eltexIsisISAdj3WayState = _EltexIsisISAdj3WayState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 3, 1, 1, 3),
    _EltexIsisISAdj3WayState_Type()
)
eltexIsisISAdj3WayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIsisISAdj3WayState.setStatus("current")
_EltexIsisISAdjNeighSNPAAddress_Type = EltexNETAddress
_EltexIsisISAdjNeighSNPAAddress_Object = MibTableColumn
eltexIsisISAdjNeighSNPAAddress = _EltexIsisISAdjNeighSNPAAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 3, 1, 1, 4),
    _EltexIsisISAdjNeighSNPAAddress_Type()
)
eltexIsisISAdjNeighSNPAAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIsisISAdjNeighSNPAAddress.setStatus("current")


class _EltexIsisISAdjNeighSysType_Type(Integer32):
    """Custom type eltexIsisISAdjNeighSysType based on Integer32"""
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
        *(("l1IntermediateSystem", 1),
          ("l2IntermediateSystem", 2),
          ("l1L2IntermediateSystem", 3),
          ("unknown", 4))
    )


_EltexIsisISAdjNeighSysType_Type.__name__ = "Integer32"
_EltexIsisISAdjNeighSysType_Object = MibTableColumn
eltexIsisISAdjNeighSysType = _EltexIsisISAdjNeighSysType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 3, 1, 1, 5),
    _EltexIsisISAdjNeighSysType_Type()
)
eltexIsisISAdjNeighSysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIsisISAdjNeighSysType.setStatus("current")
_EltexIsisISAdjNeighSysID_Type = EltexIsisSystemID
_EltexIsisISAdjNeighSysID_Object = MibTableColumn
eltexIsisISAdjNeighSysID = _EltexIsisISAdjNeighSysID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 3, 1, 1, 6),
    _EltexIsisISAdjNeighSysID_Type()
)
eltexIsisISAdjNeighSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIsisISAdjNeighSysID.setStatus("current")
_EltexIsisISAdjNbrExtendedCircID_Type = Unsigned32
_EltexIsisISAdjNbrExtendedCircID_Object = MibTableColumn
eltexIsisISAdjNbrExtendedCircID = _EltexIsisISAdjNbrExtendedCircID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 3, 1, 1, 7),
    _EltexIsisISAdjNbrExtendedCircID_Type()
)
eltexIsisISAdjNbrExtendedCircID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIsisISAdjNbrExtendedCircID.setStatus("current")


class _EltexIsisISAdjUsage_Type(Integer32):
    """Custom type eltexIsisISAdjUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("reserved", 0),
          ("level1", 1),
          ("level2", 2),
          ("level1and2", 3))
    )


_EltexIsisISAdjUsage_Type.__name__ = "Integer32"
_EltexIsisISAdjUsage_Object = MibTableColumn
eltexIsisISAdjUsage = _EltexIsisISAdjUsage_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 3, 1, 1, 8),
    _EltexIsisISAdjUsage_Type()
)
eltexIsisISAdjUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIsisISAdjUsage.setStatus("current")


class _EltexIsisISAdjHoldTimer_Type(Unsigned32):
    """Custom type eltexIsisISAdjHoldTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EltexIsisISAdjHoldTimer_Type.__name__ = "Unsigned32"
_EltexIsisISAdjHoldTimer_Object = MibTableColumn
eltexIsisISAdjHoldTimer = _EltexIsisISAdjHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 3, 1, 1, 9),
    _EltexIsisISAdjHoldTimer_Type()
)
eltexIsisISAdjHoldTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIsisISAdjHoldTimer.setStatus("current")
if mibBuilder.loadTexts:
    eltexIsisISAdjHoldTimer.setUnits("seconds")
_EltexIsisISAdjNeighPriority_Type = EltexIsisISPriority
_EltexIsisISAdjNeighPriority_Object = MibTableColumn
eltexIsisISAdjNeighPriority = _EltexIsisISAdjNeighPriority_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 3, 1, 1, 10),
    _EltexIsisISAdjNeighPriority_Type()
)
eltexIsisISAdjNeighPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIsisISAdjNeighPriority.setStatus("current")
_EltexIsisISAdjLastUpTime_Type = TimeTicks
_EltexIsisISAdjLastUpTime_Object = MibTableColumn
eltexIsisISAdjLastUpTime = _EltexIsisISAdjLastUpTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 3, 1, 1, 11),
    _EltexIsisISAdjLastUpTime_Type()
)
eltexIsisISAdjLastUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIsisISAdjLastUpTime.setStatus("current")
if mibBuilder.loadTexts:
    eltexIsisISAdjLastUpTime.setUnits("seconds")
_EltexIsisISAdjRestartCapable_Type = TruthValue
_EltexIsisISAdjRestartCapable_Object = MibTableColumn
eltexIsisISAdjRestartCapable = _EltexIsisISAdjRestartCapable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 3, 1, 1, 12),
    _EltexIsisISAdjRestartCapable_Type()
)
eltexIsisISAdjRestartCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIsisISAdjRestartCapable.setStatus("current")


class _EltexIsisISAdjPeerRestartState_Type(Integer32):
    """Custom type eltexIsisISAdjPeerRestartState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notRestarting", 1),
          ("restartingNoHelp", 2),
          ("helpingRestart", 3))
    )


_EltexIsisISAdjPeerRestartState_Type.__name__ = "Integer32"
_EltexIsisISAdjPeerRestartState_Object = MibTableColumn
eltexIsisISAdjPeerRestartState = _EltexIsisISAdjPeerRestartState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 3, 1, 1, 13),
    _EltexIsisISAdjPeerRestartState_Type()
)
eltexIsisISAdjPeerRestartState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIsisISAdjPeerRestartState.setStatus("current")
_EltexIsisISAdjSuppressed_Type = TruthValue
_EltexIsisISAdjSuppressed_Object = MibTableColumn
eltexIsisISAdjSuppressed = _EltexIsisISAdjSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 3, 1, 1, 14),
    _EltexIsisISAdjSuppressed_Type()
)
eltexIsisISAdjSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIsisISAdjSuppressed.setStatus("current")


class _EltexIsisISAdjNeighLanID_Type(OctetString):
    """Custom type eltexIsisISAdjNeighLanID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_EltexIsisISAdjNeighLanID_Type.__name__ = "OctetString"
_EltexIsisISAdjNeighLanID_Object = MibTableColumn
eltexIsisISAdjNeighLanID = _EltexIsisISAdjNeighLanID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 3, 1, 1, 15),
    _EltexIsisISAdjNeighLanID_Type()
)
eltexIsisISAdjNeighLanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIsisISAdjNeighLanID.setStatus("current")
_EltexIsisISAdjNeighHostname_Type = SnmpAdminString
_EltexIsisISAdjNeighHostname_Object = MibTableColumn
eltexIsisISAdjNeighHostname = _EltexIsisISAdjNeighHostname_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 3, 1, 1, 16),
    _EltexIsisISAdjNeighHostname_Type()
)
eltexIsisISAdjNeighHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIsisISAdjNeighHostname.setStatus("current")
_EltexIsisISAdjNeighLanIDHostname_Type = SnmpAdminString
_EltexIsisISAdjNeighLanIDHostname_Object = MibTableColumn
eltexIsisISAdjNeighLanIDHostname = _EltexIsisISAdjNeighLanIDHostname_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 3, 1, 1, 17),
    _EltexIsisISAdjNeighLanIDHostname_Type()
)
eltexIsisISAdjNeighLanIDHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIsisISAdjNeighLanIDHostname.setStatus("current")
_EltexIsisISAdjAreaAddrTable_Object = MibTable
eltexIsisISAdjAreaAddrTable = _EltexIsisISAdjAreaAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 3, 2)
)
if mibBuilder.loadTexts:
    eltexIsisISAdjAreaAddrTable.setStatus("current")
_EltexIsisISAdjAreaAddrEntry_Object = MibTableRow
eltexIsisISAdjAreaAddrEntry = _EltexIsisISAdjAreaAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 3, 2, 1)
)
eltexIsisISAdjAreaAddrEntry.setIndexNames(
    (0, "ELTEX-ISIS-MIB", "eltexIsisSysInstance"),
    (0, "ELTEX-ISIS-MIB", "eltexIsisCircIfindex"),
    (0, "ELTEX-ISIS-MIB", "eltexIsisISAdjIndex"),
    (0, "ELTEX-ISIS-MIB", "eltexIsisISAdjAreaAddrIndex"),
)
if mibBuilder.loadTexts:
    eltexIsisISAdjAreaAddrEntry.setStatus("current")


class _EltexIsisISAdjAreaAddrIndex_Type(Integer32):
    """Custom type eltexIsisISAdjAreaAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000000),
    )


_EltexIsisISAdjAreaAddrIndex_Type.__name__ = "Integer32"
_EltexIsisISAdjAreaAddrIndex_Object = MibTableColumn
eltexIsisISAdjAreaAddrIndex = _EltexIsisISAdjAreaAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 3, 2, 1, 1),
    _EltexIsisISAdjAreaAddrIndex_Type()
)
eltexIsisISAdjAreaAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexIsisISAdjAreaAddrIndex.setStatus("current")
_EltexIsisISAdjAreaAddress_Type = EltexNETAddress
_EltexIsisISAdjAreaAddress_Object = MibTableColumn
eltexIsisISAdjAreaAddress = _EltexIsisISAdjAreaAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 3, 2, 1, 2),
    _EltexIsisISAdjAreaAddress_Type()
)
eltexIsisISAdjAreaAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIsisISAdjAreaAddress.setStatus("current")
_EltexIsisISAdjIPAddrTable_Object = MibTable
eltexIsisISAdjIPAddrTable = _EltexIsisISAdjIPAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 3, 3)
)
if mibBuilder.loadTexts:
    eltexIsisISAdjIPAddrTable.setStatus("current")
_EltexIsisISAdjIPAddrEntry_Object = MibTableRow
eltexIsisISAdjIPAddrEntry = _EltexIsisISAdjIPAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 3, 3, 1)
)
eltexIsisISAdjIPAddrEntry.setIndexNames(
    (0, "ELTEX-ISIS-MIB", "eltexIsisSysInstance"),
    (0, "ELTEX-ISIS-MIB", "eltexIsisCircIfindex"),
    (0, "ELTEX-ISIS-MIB", "eltexIsisISAdjIndex"),
    (0, "ELTEX-ISIS-MIB", "eltexIsisISAdjIPAddrIndex"),
)
if mibBuilder.loadTexts:
    eltexIsisISAdjIPAddrEntry.setStatus("current")


class _EltexIsisISAdjIPAddrIndex_Type(Integer32):
    """Custom type eltexIsisISAdjIPAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000000),
    )


_EltexIsisISAdjIPAddrIndex_Type.__name__ = "Integer32"
_EltexIsisISAdjIPAddrIndex_Object = MibTableColumn
eltexIsisISAdjIPAddrIndex = _EltexIsisISAdjIPAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 3, 3, 1, 1),
    _EltexIsisISAdjIPAddrIndex_Type()
)
eltexIsisISAdjIPAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexIsisISAdjIPAddrIndex.setStatus("current")
_EltexIsisISAdjIPAddrType_Type = InetAddressType
_EltexIsisISAdjIPAddrType_Object = MibTableColumn
eltexIsisISAdjIPAddrType = _EltexIsisISAdjIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 3, 3, 1, 2),
    _EltexIsisISAdjIPAddrType_Type()
)
eltexIsisISAdjIPAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIsisISAdjIPAddrType.setStatus("current")


class _EltexIsisISAdjIPAddrAddress_Type(InetAddress):
    """Custom type eltexIsisISAdjIPAddrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_EltexIsisISAdjIPAddrAddress_Type.__name__ = "InetAddress"
_EltexIsisISAdjIPAddrAddress_Object = MibTableColumn
eltexIsisISAdjIPAddrAddress = _EltexIsisISAdjIPAddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 3, 3, 1, 3),
    _EltexIsisISAdjIPAddrAddress_Type()
)
eltexIsisISAdjIPAddrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIsisISAdjIPAddrAddress.setStatus("current")
_EltexIsisLSPDataBase_ObjectIdentity = ObjectIdentity
eltexIsisLSPDataBase = _EltexIsisLSPDataBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 5)
)
_EltexIsisLSPSummaryTable_Object = MibTable
eltexIsisLSPSummaryTable = _EltexIsisLSPSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 5, 1)
)
if mibBuilder.loadTexts:
    eltexIsisLSPSummaryTable.setStatus("current")
_EltexIsisLSPSummaryEntry_Object = MibTableRow
eltexIsisLSPSummaryEntry = _EltexIsisLSPSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 5, 1, 1)
)
eltexIsisLSPSummaryEntry.setIndexNames(
    (0, "ELTEX-ISIS-MIB", "eltexIsisSysInstance"),
    (0, "ELTEX-ISIS-MIB", "eltexIsisLSPLevel"),
    (0, "ELTEX-ISIS-MIB", "eltexIsisLSPID"),
)
if mibBuilder.loadTexts:
    eltexIsisLSPSummaryEntry.setStatus("current")
_EltexIsisLSPLevel_Type = EltexIsisISLevel
_EltexIsisLSPLevel_Object = MibTableColumn
eltexIsisLSPLevel = _EltexIsisLSPLevel_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 5, 1, 1, 1),
    _EltexIsisLSPLevel_Type()
)
eltexIsisLSPLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexIsisLSPLevel.setStatus("current")
_EltexIsisLSPID_Type = EltexIsisLinkStatePDUID
_EltexIsisLSPID_Object = MibTableColumn
eltexIsisLSPID = _EltexIsisLSPID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 5, 1, 1, 2),
    _EltexIsisLSPID_Type()
)
eltexIsisLSPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexIsisLSPID.setStatus("current")
_EltexIsisLSPSeq_Type = Unsigned32
_EltexIsisLSPSeq_Object = MibTableColumn
eltexIsisLSPSeq = _EltexIsisLSPSeq_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 5, 1, 1, 3),
    _EltexIsisLSPSeq_Type()
)
eltexIsisLSPSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIsisLSPSeq.setStatus("current")
_EltexIsisLSPZeroLife_Type = TruthValue
_EltexIsisLSPZeroLife_Object = MibTableColumn
eltexIsisLSPZeroLife = _EltexIsisLSPZeroLife_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 5, 1, 1, 4),
    _EltexIsisLSPZeroLife_Type()
)
eltexIsisLSPZeroLife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIsisLSPZeroLife.setStatus("current")


class _EltexIsisLSPChecksum_Type(Unsigned32):
    """Custom type eltexIsisLSPChecksum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EltexIsisLSPChecksum_Type.__name__ = "Unsigned32"
_EltexIsisLSPChecksum_Object = MibTableColumn
eltexIsisLSPChecksum = _EltexIsisLSPChecksum_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 5, 1, 1, 5),
    _EltexIsisLSPChecksum_Type()
)
eltexIsisLSPChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIsisLSPChecksum.setStatus("current")


class _EltexIsisLSPLifetimeRemain_Type(Unsigned32):
    """Custom type eltexIsisLSPLifetimeRemain based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EltexIsisLSPLifetimeRemain_Type.__name__ = "Unsigned32"
_EltexIsisLSPLifetimeRemain_Object = MibTableColumn
eltexIsisLSPLifetimeRemain = _EltexIsisLSPLifetimeRemain_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 5, 1, 1, 6),
    _EltexIsisLSPLifetimeRemain_Type()
)
eltexIsisLSPLifetimeRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIsisLSPLifetimeRemain.setStatus("current")
if mibBuilder.loadTexts:
    eltexIsisLSPLifetimeRemain.setUnits("seconds")


class _EltexIsisLSPPDULength_Type(Unsigned32):
    """Custom type eltexIsisLSPPDULength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EltexIsisLSPPDULength_Type.__name__ = "Unsigned32"
_EltexIsisLSPPDULength_Object = MibTableColumn
eltexIsisLSPPDULength = _EltexIsisLSPPDULength_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 5, 1, 1, 7),
    _EltexIsisLSPPDULength_Type()
)
eltexIsisLSPPDULength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIsisLSPPDULength.setStatus("current")


class _EltexIsisLSPAttributes_Type(Unsigned32):
    """Custom type eltexIsisLSPAttributes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EltexIsisLSPAttributes_Type.__name__ = "Unsigned32"
_EltexIsisLSPAttributes_Object = MibTableColumn
eltexIsisLSPAttributes = _EltexIsisLSPAttributes_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 5, 1, 1, 8),
    _EltexIsisLSPAttributes_Type()
)
eltexIsisLSPAttributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIsisLSPAttributes.setStatus("current")
_EltexIsisLSPIDHostname_Type = SnmpAdminString
_EltexIsisLSPIDHostname_Object = MibTableColumn
eltexIsisLSPIDHostname = _EltexIsisLSPIDHostname_Object(
    (1, 3, 6, 1, 4, 1, 35265, 55, 1, 5, 1, 1, 9),
    _EltexIsisLSPIDHostname_Type()
)
eltexIsisLSPIDHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIsisLSPIDHostname.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-ISIS-MIB",
    **{"EltexIsisSystemID": EltexIsisSystemID,
       "EltexIsisAdminState": EltexIsisAdminState,
       "EltexNETAddress": EltexNETAddress,
       "EltexIsisOperStatus": EltexIsisOperStatus,
       "EltexIsisISLevel": EltexIsisISLevel,
       "EltexIsisLinkStatePDUID": EltexIsisLinkStatePDUID,
       "EltexIsisISPriority": EltexIsisISPriority,
       "EltexIsisMetricStyle": EltexIsisMetricStyle,
       "EltexIsisWideMetric": EltexIsisWideMetric,
       "EltexIsisAuthType": EltexIsisAuthType,
       "EltexIsisHelloPaddingAction": EltexIsisHelloPaddingAction,
       "eltexIsisMIB": eltexIsisMIB,
       "eltexIsisObjects": eltexIsisObjects,
       "eltexIsisSystem": eltexIsisSystem,
       "eltexIsisSysTable": eltexIsisSysTable,
       "eltexIsisSysEntry": eltexIsisSysEntry,
       "eltexIsisSysInstance": eltexIsisSysInstance,
       "eltexIsisSysType": eltexIsisSysType,
       "eltexIsisSysID": eltexIsisSysID,
       "eltexIsisSysAdminState": eltexIsisSysAdminState,
       "eltexIsisSysOperState": eltexIsisSysOperState,
       "eltexIsisSysRowStatus": eltexIsisSysRowStatus,
       "eltexIsisSysMaxAge": eltexIsisSysMaxAge,
       "eltexIsisSysMaxLSPGenInt": eltexIsisSysMaxLSPGenInt,
       "eltexIsisSysCalcMaxDelay": eltexIsisSysCalcMaxDelay,
       "eltexIsisSysCalcThrshUpdStart": eltexIsisSysCalcThrshUpdStart,
       "eltexIsisSysCalcThrshUpdRestart": eltexIsisSysCalcThrshUpdRestart,
       "eltexIsisSysCalcThrshRestartLimit": eltexIsisSysCalcThrshRestartLimit,
       "eltexIsisSysHostNameDynamic": eltexIsisSysHostNameDynamic,
       "eltexIsisNetAddrTable": eltexIsisNetAddrTable,
       "eltexIsisNetAddrEntry": eltexIsisNetAddrEntry,
       "eltexIsisNetAddr": eltexIsisNetAddr,
       "eltexIsisNetAddrRowStatus": eltexIsisNetAddrRowStatus,
       "eltexIsisSysLevelTable": eltexIsisSysLevelTable,
       "eltexIsisSysLevelEntry": eltexIsisSysLevelEntry,
       "eltexIsisSysLevelIndex": eltexIsisSysLevelIndex,
       "eltexIsisSysLevelMinLSPGenInt": eltexIsisSysLevelMinLSPGenInt,
       "eltexIsisSysLevelMetricStyle": eltexIsisSysLevelMetricStyle,
       "eltexIsisSysLevelAuthType": eltexIsisSysLevelAuthType,
       "eltexIsisSysLevelAuthKey": eltexIsisSysLevelAuthKey,
       "eltexIsisSysLevelAuthKeyChain": eltexIsisSysLevelAuthKeyChain,
       "eltexIsisSysLevelOrigLSPBuffSize": eltexIsisSysLevelOrigLSPBuffSize,
       "eltexIsisRouterTable": eltexIsisRouterTable,
       "eltexIsisRouterEntry": eltexIsisRouterEntry,
       "eltexIsisRouterSysID": eltexIsisRouterSysID,
       "eltexIsisRouterLevel": eltexIsisRouterLevel,
       "eltexIsisRouterHostName": eltexIsisRouterHostName,
       "eltexIsisCirc": eltexIsisCirc,
       "eltexIsisCircTable": eltexIsisCircTable,
       "eltexIsisCircEntry": eltexIsisCircEntry,
       "eltexIsisCircIfindex": eltexIsisCircIfindex,
       "eltexIsisCircRowStatus": eltexIsisCircRowStatus,
       "eltexIsisCircAdminState": eltexIsisCircAdminState,
       "eltexIsisCircOperState": eltexIsisCircOperState,
       "eltexIsisCircLevel": eltexIsisCircLevel,
       "eltexIsisCircPassiveCircuit": eltexIsisCircPassiveCircuit,
       "eltexIsisCircPtToPt": eltexIsisCircPtToPt,
       "eltexIsisCircHelloPadding": eltexIsisCircHelloPadding,
       "eltexIsisCircPDUBuffSize": eltexIsisCircPDUBuffSize,
       "eltexIsisCircLevelTable": eltexIsisCircLevelTable,
       "eltexIsisCircLevelEntry": eltexIsisCircLevelEntry,
       "eltexIsisCircLevelIndex": eltexIsisCircLevelIndex,
       "eltexIsisCircLevelRowStatus": eltexIsisCircLevelRowStatus,
       "eltexIsisCircLevelMetric": eltexIsisCircLevelMetric,
       "eltexIsisCircLevelAuthType": eltexIsisCircLevelAuthType,
       "eltexIsisCircLevelAuthKey": eltexIsisCircLevelAuthKey,
       "eltexIsisCircLevelAuthKeyChain": eltexIsisCircLevelAuthKeyChain,
       "eltexIsisCircLevelStatusTable": eltexIsisCircLevelStatusTable,
       "eltexIsisCircLevelStatusEntry": eltexIsisCircLevelStatusEntry,
       "eltexIsisCircLevelStatusMetric": eltexIsisCircLevelStatusMetric,
       "eltexIsisISAdj": eltexIsisISAdj,
       "eltexIsisISAdjTable": eltexIsisISAdjTable,
       "eltexIsisISAdjEntry": eltexIsisISAdjEntry,
       "eltexIsisISAdjIndex": eltexIsisISAdjIndex,
       "eltexIsisISAdjState": eltexIsisISAdjState,
       "eltexIsisISAdj3WayState": eltexIsisISAdj3WayState,
       "eltexIsisISAdjNeighSNPAAddress": eltexIsisISAdjNeighSNPAAddress,
       "eltexIsisISAdjNeighSysType": eltexIsisISAdjNeighSysType,
       "eltexIsisISAdjNeighSysID": eltexIsisISAdjNeighSysID,
       "eltexIsisISAdjNbrExtendedCircID": eltexIsisISAdjNbrExtendedCircID,
       "eltexIsisISAdjUsage": eltexIsisISAdjUsage,
       "eltexIsisISAdjHoldTimer": eltexIsisISAdjHoldTimer,
       "eltexIsisISAdjNeighPriority": eltexIsisISAdjNeighPriority,
       "eltexIsisISAdjLastUpTime": eltexIsisISAdjLastUpTime,
       "eltexIsisISAdjRestartCapable": eltexIsisISAdjRestartCapable,
       "eltexIsisISAdjPeerRestartState": eltexIsisISAdjPeerRestartState,
       "eltexIsisISAdjSuppressed": eltexIsisISAdjSuppressed,
       "eltexIsisISAdjNeighLanID": eltexIsisISAdjNeighLanID,
       "eltexIsisISAdjNeighHostname": eltexIsisISAdjNeighHostname,
       "eltexIsisISAdjNeighLanIDHostname": eltexIsisISAdjNeighLanIDHostname,
       "eltexIsisISAdjAreaAddrTable": eltexIsisISAdjAreaAddrTable,
       "eltexIsisISAdjAreaAddrEntry": eltexIsisISAdjAreaAddrEntry,
       "eltexIsisISAdjAreaAddrIndex": eltexIsisISAdjAreaAddrIndex,
       "eltexIsisISAdjAreaAddress": eltexIsisISAdjAreaAddress,
       "eltexIsisISAdjIPAddrTable": eltexIsisISAdjIPAddrTable,
       "eltexIsisISAdjIPAddrEntry": eltexIsisISAdjIPAddrEntry,
       "eltexIsisISAdjIPAddrIndex": eltexIsisISAdjIPAddrIndex,
       "eltexIsisISAdjIPAddrType": eltexIsisISAdjIPAddrType,
       "eltexIsisISAdjIPAddrAddress": eltexIsisISAdjIPAddrAddress,
       "eltexIsisLSPDataBase": eltexIsisLSPDataBase,
       "eltexIsisLSPSummaryTable": eltexIsisLSPSummaryTable,
       "eltexIsisLSPSummaryEntry": eltexIsisLSPSummaryEntry,
       "eltexIsisLSPLevel": eltexIsisLSPLevel,
       "eltexIsisLSPID": eltexIsisLSPID,
       "eltexIsisLSPSeq": eltexIsisLSPSeq,
       "eltexIsisLSPZeroLife": eltexIsisLSPZeroLife,
       "eltexIsisLSPChecksum": eltexIsisLSPChecksum,
       "eltexIsisLSPLifetimeRemain": eltexIsisLSPLifetimeRemain,
       "eltexIsisLSPPDULength": eltexIsisLSPPDULength,
       "eltexIsisLSPAttributes": eltexIsisLSPAttributes,
       "eltexIsisLSPIDHostname": eltexIsisLSPIDHostname}
)
