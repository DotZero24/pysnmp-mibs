# SNMP MIB module (ISIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alcatel-ent1/ISIS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:07:56 2025
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

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TruthValue")


# MODULE-IDENTITY

isisMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 37)
)
if mibBuilder.loadTexts:
    isisMIB.setRevisions(
        ("2002-05-06 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class OSINSAddress(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )



class SystemID(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )



class LinkStatePDUID(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class AdminState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )



class UpTime(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"


class LSPBuffSize(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16000),
    )



class LevelState(TextualConvention, Integer32):
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
        *(("off", 1),
          ("on", 2),
          ("waiting", 3),
          ("overloaded", 4))
    )



class SupportedProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(129,
              204,
              205)
        )
    )
    namedValues = NamedValues(
        *(("iso8473", 129),
          ("ip", 204),
          ("ipV6", 205))
    )



class DefaultMetric(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )



class MetricType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("external", 2))
    )



class MetricStyle(TextualConvention, Integer32):
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



class ISLevel(TextualConvention, Integer32):
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
        *(("area", 1),
          ("domain", 2),
          ("none", 3))
    )



class IsisPDUHeader(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )



class CircuitID(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 9),
    )



class ISPriority(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )



# MIB Managed Objects in the order of their OIDs

_IsisObjects_ObjectIdentity = ObjectIdentity
isisObjects = _IsisObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 37, 1)
)
_IsisSystem_ObjectIdentity = ObjectIdentity
isisSystem = _IsisSystem_ObjectIdentity(
    (1, 3, 6, 1, 3, 37, 1, 1)
)
if mibBuilder.loadTexts:
    isisSystem.setStatus("current")
_IsisSysTable_Object = MibTable
isisSysTable = _IsisSysTable_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 1)
)
if mibBuilder.loadTexts:
    isisSysTable.setStatus("current")
_IsisSysEntry_Object = MibTableRow
isisSysEntry = _IsisSysEntry_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 1, 1)
)
isisSysEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
)
if mibBuilder.loadTexts:
    isisSysEntry.setStatus("current")


class _IsisSysInstance_Type(Integer32):
    """Custom type isisSysInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_IsisSysInstance_Type.__name__ = "Integer32"
_IsisSysInstance_Object = MibTableColumn
isisSysInstance = _IsisSysInstance_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 1, 1, 1),
    _IsisSysInstance_Type()
)
isisSysInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisSysInstance.setStatus("current")


class _IsisSysVersion_Type(DisplayString):
    """Custom type isisSysVersion based on DisplayString"""
    defaultValue = OctetString("1")


_IsisSysVersion_Type.__name__ = "DisplayString"
_IsisSysVersion_Object = MibTableColumn
isisSysVersion = _IsisSysVersion_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 1, 1, 2),
    _IsisSysVersion_Type()
)
isisSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysVersion.setStatus("current")


class _IsisSysType_Type(Integer32):
    """Custom type isisSysType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("level1IS", 1),
          ("level2IS", 2),
          ("level1L2IS", 3))
    )


_IsisSysType_Type.__name__ = "Integer32"
_IsisSysType_Object = MibTableColumn
isisSysType = _IsisSysType_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 1, 1, 3),
    _IsisSysType_Type()
)
isisSysType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysType.setStatus("current")
_IsisSysID_Type = SystemID
_IsisSysID_Object = MibTableColumn
isisSysID = _IsisSysID_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 1, 1, 4),
    _IsisSysID_Type()
)
isisSysID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysID.setStatus("current")


class _IsisSysMaxPathSplits_Type(Integer32):
    """Custom type isisSysMaxPathSplits based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_IsisSysMaxPathSplits_Type.__name__ = "Integer32"
_IsisSysMaxPathSplits_Object = MibTableColumn
isisSysMaxPathSplits = _IsisSysMaxPathSplits_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 1, 1, 5),
    _IsisSysMaxPathSplits_Type()
)
isisSysMaxPathSplits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysMaxPathSplits.setStatus("current")


class _IsisSysMaxLSPGenInt_Type(Integer32):
    """Custom type isisSysMaxLSPGenInt based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsisSysMaxLSPGenInt_Type.__name__ = "Integer32"
_IsisSysMaxLSPGenInt_Object = MibTableColumn
isisSysMaxLSPGenInt = _IsisSysMaxLSPGenInt_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 1, 1, 6),
    _IsisSysMaxLSPGenInt_Type()
)
isisSysMaxLSPGenInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysMaxLSPGenInt.setStatus("current")
if mibBuilder.loadTexts:
    isisSysMaxLSPGenInt.setUnits("seconds")


class _IsisSysOrigL1LSPBuffSize_Type(LSPBuffSize):
    """Custom type isisSysOrigL1LSPBuffSize based on LSPBuffSize"""
    defaultValue = 1492


_IsisSysOrigL1LSPBuffSize_Type.__name__ = "LSPBuffSize"
_IsisSysOrigL1LSPBuffSize_Object = MibTableColumn
isisSysOrigL1LSPBuffSize = _IsisSysOrigL1LSPBuffSize_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 1, 1, 7),
    _IsisSysOrigL1LSPBuffSize_Type()
)
isisSysOrigL1LSPBuffSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysOrigL1LSPBuffSize.setStatus("current")


class _IsisSysMaxAreaAddresses_Type(Integer32):
    """Custom type isisSysMaxAreaAddresses based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 254),
    )


_IsisSysMaxAreaAddresses_Type.__name__ = "Integer32"
_IsisSysMaxAreaAddresses_Object = MibTableColumn
isisSysMaxAreaAddresses = _IsisSysMaxAreaAddresses_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 1, 1, 8),
    _IsisSysMaxAreaAddresses_Type()
)
isisSysMaxAreaAddresses.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysMaxAreaAddresses.setStatus("current")


class _IsisSysMinL1LSPGenInt_Type(Integer32):
    """Custom type isisSysMinL1LSPGenInt based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsisSysMinL1LSPGenInt_Type.__name__ = "Integer32"
_IsisSysMinL1LSPGenInt_Object = MibTableColumn
isisSysMinL1LSPGenInt = _IsisSysMinL1LSPGenInt_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 1, 1, 9),
    _IsisSysMinL1LSPGenInt_Type()
)
isisSysMinL1LSPGenInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysMinL1LSPGenInt.setStatus("current")
if mibBuilder.loadTexts:
    isisSysMinL1LSPGenInt.setUnits("seconds")


class _IsisSysMinL2LSPGenInt_Type(Integer32):
    """Custom type isisSysMinL2LSPGenInt based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsisSysMinL2LSPGenInt_Type.__name__ = "Integer32"
_IsisSysMinL2LSPGenInt_Object = MibTableColumn
isisSysMinL2LSPGenInt = _IsisSysMinL2LSPGenInt_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 1, 1, 10),
    _IsisSysMinL2LSPGenInt_Type()
)
isisSysMinL2LSPGenInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysMinL2LSPGenInt.setStatus("current")
if mibBuilder.loadTexts:
    isisSysMinL2LSPGenInt.setUnits("seconds")


class _IsisSysPollESHelloRate_Type(Integer32):
    """Custom type isisSysPollESHelloRate based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsisSysPollESHelloRate_Type.__name__ = "Integer32"
_IsisSysPollESHelloRate_Object = MibTableColumn
isisSysPollESHelloRate = _IsisSysPollESHelloRate_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 1, 1, 11),
    _IsisSysPollESHelloRate_Type()
)
isisSysPollESHelloRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysPollESHelloRate.setStatus("current")
if mibBuilder.loadTexts:
    isisSysPollESHelloRate.setUnits("seconds")


class _IsisSysWaitTime_Type(Integer32):
    """Custom type isisSysWaitTime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsisSysWaitTime_Type.__name__ = "Integer32"
_IsisSysWaitTime_Object = MibTableColumn
isisSysWaitTime = _IsisSysWaitTime_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 1, 1, 12),
    _IsisSysWaitTime_Type()
)
isisSysWaitTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysWaitTime.setStatus("current")
if mibBuilder.loadTexts:
    isisSysWaitTime.setUnits("seconds")


class _IsisSysAdminState_Type(AdminState):
    """Custom type isisSysAdminState based on AdminState"""
    defaultValue = 1


_IsisSysAdminState_Type.__name__ = "AdminState"
_IsisSysAdminState_Object = MibTableColumn
isisSysAdminState = _IsisSysAdminState_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 1, 1, 13),
    _IsisSysAdminState_Type()
)
isisSysAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysAdminState.setStatus("current")
_IsisSysL1State_Type = LevelState
_IsisSysL1State_Object = MibTableColumn
isisSysL1State = _IsisSysL1State_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 1, 1, 14),
    _IsisSysL1State_Type()
)
isisSysL1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysL1State.setStatus("current")


class _IsisSysOrigL2LSPBuffSize_Type(LSPBuffSize):
    """Custom type isisSysOrigL2LSPBuffSize based on LSPBuffSize"""
    defaultValue = 1492


_IsisSysOrigL2LSPBuffSize_Type.__name__ = "LSPBuffSize"
_IsisSysOrigL2LSPBuffSize_Object = MibTableColumn
isisSysOrigL2LSPBuffSize = _IsisSysOrigL2LSPBuffSize_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 1, 1, 15),
    _IsisSysOrigL2LSPBuffSize_Type()
)
isisSysOrigL2LSPBuffSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysOrigL2LSPBuffSize.setStatus("current")
_IsisSysL2State_Type = LevelState
_IsisSysL2State_Object = MibTableColumn
isisSysL2State = _IsisSysL2State_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 1, 1, 16),
    _IsisSysL2State_Type()
)
isisSysL2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysL2State.setStatus("current")


class _IsisSysLogAdjacencyChanges_Type(TruthValue):
    """Custom type isisSysLogAdjacencyChanges based on TruthValue"""
    defaultValue = 2


_IsisSysLogAdjacencyChanges_Type.__name__ = "TruthValue"
_IsisSysLogAdjacencyChanges_Object = MibTableColumn
isisSysLogAdjacencyChanges = _IsisSysLogAdjacencyChanges_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 1, 1, 17),
    _IsisSysLogAdjacencyChanges_Type()
)
isisSysLogAdjacencyChanges.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysLogAdjacencyChanges.setStatus("current")


class _IsisSysMaxAreaCheck_Type(TruthValue):
    """Custom type isisSysMaxAreaCheck based on TruthValue"""
    defaultValue = 1


_IsisSysMaxAreaCheck_Type.__name__ = "TruthValue"
_IsisSysMaxAreaCheck_Object = MibTableColumn
isisSysMaxAreaCheck = _IsisSysMaxAreaCheck_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 1, 1, 18),
    _IsisSysMaxAreaCheck_Type()
)
isisSysMaxAreaCheck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysMaxAreaCheck.setStatus("current")
_IsisSysNextCircIndex_Type = TestAndIncr
_IsisSysNextCircIndex_Object = MibTableColumn
isisSysNextCircIndex = _IsisSysNextCircIndex_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 1, 1, 19),
    _IsisSysNextCircIndex_Type()
)
isisSysNextCircIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysNextCircIndex.setStatus("current")


class _IsisSysExistState_Type(RowStatus):
    """Custom type isisSysExistState based on RowStatus"""
    defaultValue = 1


_IsisSysExistState_Type.__name__ = "RowStatus"
_IsisSysExistState_Object = MibTableColumn
isisSysExistState = _IsisSysExistState_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 1, 1, 20),
    _IsisSysExistState_Type()
)
isisSysExistState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysExistState.setStatus("current")


class _IsisSysL2toL1Leaking_Type(TruthValue):
    """Custom type isisSysL2toL1Leaking based on TruthValue"""
    defaultValue = 2


_IsisSysL2toL1Leaking_Type.__name__ = "TruthValue"
_IsisSysL2toL1Leaking_Object = MibTableColumn
isisSysL2toL1Leaking = _IsisSysL2toL1Leaking_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 1, 1, 21),
    _IsisSysL2toL1Leaking_Type()
)
isisSysL2toL1Leaking.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysL2toL1Leaking.setStatus("current")


class _IsisSysSetOverload_Type(Integer32):
    """Custom type isisSysSetOverload based on Integer32"""
    defaultValue = 4

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
        *(("setL1Overload", 1),
          ("setL2Overload", 2),
          ("setL1L2Overload", 3),
          ("overloadClear", 4))
    )


_IsisSysSetOverload_Type.__name__ = "Integer32"
_IsisSysSetOverload_Object = MibTableColumn
isisSysSetOverload = _IsisSysSetOverload_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 1, 1, 22),
    _IsisSysSetOverload_Type()
)
isisSysSetOverload.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysSetOverload.setStatus("current")


class _IsisSysL1MetricStyle_Type(MetricStyle):
    """Custom type isisSysL1MetricStyle based on MetricStyle"""
    defaultValue = 1


_IsisSysL1MetricStyle_Type.__name__ = "MetricStyle"
_IsisSysL1MetricStyle_Object = MibTableColumn
isisSysL1MetricStyle = _IsisSysL1MetricStyle_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 1, 1, 23),
    _IsisSysL1MetricStyle_Type()
)
isisSysL1MetricStyle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysL1MetricStyle.setStatus("current")


class _IsisSysL1SPFConsiders_Type(MetricStyle):
    """Custom type isisSysL1SPFConsiders based on MetricStyle"""
    defaultValue = 1


_IsisSysL1SPFConsiders_Type.__name__ = "MetricStyle"
_IsisSysL1SPFConsiders_Object = MibTableColumn
isisSysL1SPFConsiders = _IsisSysL1SPFConsiders_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 1, 1, 24),
    _IsisSysL1SPFConsiders_Type()
)
isisSysL1SPFConsiders.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysL1SPFConsiders.setStatus("current")


class _IsisSysL2MetricStyle_Type(MetricStyle):
    """Custom type isisSysL2MetricStyle based on MetricStyle"""
    defaultValue = 1


_IsisSysL2MetricStyle_Type.__name__ = "MetricStyle"
_IsisSysL2MetricStyle_Object = MibTableColumn
isisSysL2MetricStyle = _IsisSysL2MetricStyle_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 1, 1, 25),
    _IsisSysL2MetricStyle_Type()
)
isisSysL2MetricStyle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysL2MetricStyle.setStatus("current")


class _IsisSysL2SPFConsiders_Type(MetricStyle):
    """Custom type isisSysL2SPFConsiders based on MetricStyle"""
    defaultValue = 1


_IsisSysL2SPFConsiders_Type.__name__ = "MetricStyle"
_IsisSysL2SPFConsiders_Object = MibTableColumn
isisSysL2SPFConsiders = _IsisSysL2SPFConsiders_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 1, 1, 26),
    _IsisSysL2SPFConsiders_Type()
)
isisSysL2SPFConsiders.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysL2SPFConsiders.setStatus("current")


class _IsisSysTEEnabled_Type(ISLevel):
    """Custom type isisSysTEEnabled based on ISLevel"""
    defaultValue = 3


_IsisSysTEEnabled_Type.__name__ = "ISLevel"
_IsisSysTEEnabled_Object = MibTableColumn
isisSysTEEnabled = _IsisSysTEEnabled_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 1, 1, 27),
    _IsisSysTEEnabled_Type()
)
isisSysTEEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysTEEnabled.setStatus("current")


class _IsisSysMaxAge_Type(Integer32):
    """Custom type isisSysMaxAge based on Integer32"""
    defaultValue = 1200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1200, 65535),
    )


_IsisSysMaxAge_Type.__name__ = "Integer32"
_IsisSysMaxAge_Object = MibTableColumn
isisSysMaxAge = _IsisSysMaxAge_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 1, 1, 28),
    _IsisSysMaxAge_Type()
)
isisSysMaxAge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysMaxAge.setStatus("current")
if mibBuilder.loadTexts:
    isisSysMaxAge.setUnits("seconds")


class _IsisSysReceiveLSPBufferSize_Type(Integer32):
    """Custom type isisSysReceiveLSPBufferSize based on Integer32"""
    defaultValue = 1492

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1492, 65535),
    )


_IsisSysReceiveLSPBufferSize_Type.__name__ = "Integer32"
_IsisSysReceiveLSPBufferSize_Object = MibTableColumn
isisSysReceiveLSPBufferSize = _IsisSysReceiveLSPBufferSize_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 1, 1, 29),
    _IsisSysReceiveLSPBufferSize_Type()
)
isisSysReceiveLSPBufferSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysReceiveLSPBufferSize.setStatus("current")
if mibBuilder.loadTexts:
    isisSysReceiveLSPBufferSize.setUnits("bytes")
_IsisManAreaAddrTable_Object = MibTable
isisManAreaAddrTable = _IsisManAreaAddrTable_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 2)
)
if mibBuilder.loadTexts:
    isisManAreaAddrTable.setStatus("current")
_IsisManAreaAddrEntry_Object = MibTableRow
isisManAreaAddrEntry = _IsisManAreaAddrEntry_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 2, 1)
)
isisManAreaAddrEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "ISIS-MIB", "isisManAreaAddr"),
)
if mibBuilder.loadTexts:
    isisManAreaAddrEntry.setStatus("current")
_IsisManAreaAddr_Type = OSINSAddress
_IsisManAreaAddr_Object = MibTableColumn
isisManAreaAddr = _IsisManAreaAddr_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 2, 1, 1),
    _IsisManAreaAddr_Type()
)
isisManAreaAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisManAreaAddr.setStatus("current")


class _IsisManAreaAddrExistState_Type(RowStatus):
    """Custom type isisManAreaAddrExistState based on RowStatus"""
    defaultValue = 1


_IsisManAreaAddrExistState_Type.__name__ = "RowStatus"
_IsisManAreaAddrExistState_Object = MibTableColumn
isisManAreaAddrExistState = _IsisManAreaAddrExistState_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 2, 1, 2),
    _IsisManAreaAddrExistState_Type()
)
isisManAreaAddrExistState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisManAreaAddrExistState.setStatus("current")
_IsisAreaAddrTable_Object = MibTable
isisAreaAddrTable = _IsisAreaAddrTable_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 3)
)
if mibBuilder.loadTexts:
    isisAreaAddrTable.setStatus("current")
_IsisAreaAddrEntry_Object = MibTableRow
isisAreaAddrEntry = _IsisAreaAddrEntry_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 3, 1)
)
isisAreaAddrEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "ISIS-MIB", "isisAreaAddr"),
)
if mibBuilder.loadTexts:
    isisAreaAddrEntry.setStatus("current")
_IsisAreaAddr_Type = OSINSAddress
_IsisAreaAddr_Object = MibTableColumn
isisAreaAddr = _IsisAreaAddr_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 3, 1, 1),
    _IsisAreaAddr_Type()
)
isisAreaAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisAreaAddr.setStatus("current")
_IsisSysProtSuppTable_Object = MibTable
isisSysProtSuppTable = _IsisSysProtSuppTable_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 4)
)
if mibBuilder.loadTexts:
    isisSysProtSuppTable.setStatus("current")
_IsisSysProtSuppEntry_Object = MibTableRow
isisSysProtSuppEntry = _IsisSysProtSuppEntry_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 4, 1)
)
isisSysProtSuppEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "ISIS-MIB", "isisSysProtSuppProtocol"),
)
if mibBuilder.loadTexts:
    isisSysProtSuppEntry.setStatus("current")
_IsisSysProtSuppProtocol_Type = SupportedProtocol
_IsisSysProtSuppProtocol_Object = MibTableColumn
isisSysProtSuppProtocol = _IsisSysProtSuppProtocol_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 4, 1, 1),
    _IsisSysProtSuppProtocol_Type()
)
isisSysProtSuppProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisSysProtSuppProtocol.setStatus("current")


class _IsisSysProtSuppExistState_Type(RowStatus):
    """Custom type isisSysProtSuppExistState based on RowStatus"""
    defaultValue = 1


_IsisSysProtSuppExistState_Type.__name__ = "RowStatus"
_IsisSysProtSuppExistState_Object = MibTableColumn
isisSysProtSuppExistState = _IsisSysProtSuppExistState_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 4, 1, 2),
    _IsisSysProtSuppExistState_Type()
)
isisSysProtSuppExistState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysProtSuppExistState.setStatus("current")
_IsisSummAddrTable_Object = MibTable
isisSummAddrTable = _IsisSummAddrTable_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 5)
)
if mibBuilder.loadTexts:
    isisSummAddrTable.setStatus("current")
_IsisSummAddrEntry_Object = MibTableRow
isisSummAddrEntry = _IsisSummAddrEntry_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 5, 1)
)
isisSummAddrEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "ISIS-MIB", "isisSummAddressType"),
    (0, "ISIS-MIB", "isisSummAddress"),
    (0, "ISIS-MIB", "isisSummAddrPrefixLen"),
)
if mibBuilder.loadTexts:
    isisSummAddrEntry.setStatus("current")
_IsisSummAddressType_Type = InetAddressType
_IsisSummAddressType_Object = MibTableColumn
isisSummAddressType = _IsisSummAddressType_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 5, 1, 1),
    _IsisSummAddressType_Type()
)
isisSummAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisSummAddressType.setStatus("current")


class _IsisSummAddress_Type(InetAddress):
    """Custom type isisSummAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_IsisSummAddress_Type.__name__ = "InetAddress"
_IsisSummAddress_Object = MibTableColumn
isisSummAddress = _IsisSummAddress_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 5, 1, 2),
    _IsisSummAddress_Type()
)
isisSummAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisSummAddress.setStatus("current")


class _IsisSummAddrPrefixLen_Type(InetAddressPrefixLength):
    """Custom type isisSummAddrPrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_IsisSummAddrPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_IsisSummAddrPrefixLen_Object = MibTableColumn
isisSummAddrPrefixLen = _IsisSummAddrPrefixLen_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 5, 1, 3),
    _IsisSummAddrPrefixLen_Type()
)
isisSummAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisSummAddrPrefixLen.setStatus("current")


class _IsisSummAddrExistState_Type(RowStatus):
    """Custom type isisSummAddrExistState based on RowStatus"""
    defaultValue = 1


_IsisSummAddrExistState_Type.__name__ = "RowStatus"
_IsisSummAddrExistState_Object = MibTableColumn
isisSummAddrExistState = _IsisSummAddrExistState_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 5, 1, 4),
    _IsisSummAddrExistState_Type()
)
isisSummAddrExistState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSummAddrExistState.setStatus("current")


class _IsisSummAddrAdminState_Type(Integer32):
    """Custom type isisSummAddrAdminState based on Integer32"""
    defaultValue = 4

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
        *(("summaryL1", 1),
          ("summaryL2", 2),
          ("summaryL1L2", 3),
          ("summaryOff", 4))
    )


_IsisSummAddrAdminState_Type.__name__ = "Integer32"
_IsisSummAddrAdminState_Object = MibTableColumn
isisSummAddrAdminState = _IsisSummAddrAdminState_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 5, 1, 5),
    _IsisSummAddrAdminState_Type()
)
isisSummAddrAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSummAddrAdminState.setStatus("current")


class _IsisSummAddrMetric_Type(DefaultMetric):
    """Custom type isisSummAddrMetric based on DefaultMetric"""
    defaultValue = 20


_IsisSummAddrMetric_Type.__name__ = "DefaultMetric"
_IsisSummAddrMetric_Object = MibTableColumn
isisSummAddrMetric = _IsisSummAddrMetric_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 5, 1, 6),
    _IsisSummAddrMetric_Type()
)
isisSummAddrMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSummAddrMetric.setStatus("current")
_IsisSysStatsTable_Object = MibTable
isisSysStatsTable = _IsisSysStatsTable_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 6)
)
if mibBuilder.loadTexts:
    isisSysStatsTable.setStatus("current")
_IsisSysStatsEntry_Object = MibTableRow
isisSysStatsEntry = _IsisSysStatsEntry_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 6, 1)
)
isisSysStatsEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "ISIS-MIB", "isisSysStatLevel"),
)
if mibBuilder.loadTexts:
    isisSysStatsEntry.setStatus("current")


class _IsisSysStatLevel_Type(Integer32):
    """Custom type isisSysStatLevel based on Integer32"""
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


_IsisSysStatLevel_Type.__name__ = "Integer32"
_IsisSysStatLevel_Object = MibTableColumn
isisSysStatLevel = _IsisSysStatLevel_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 6, 1, 1),
    _IsisSysStatLevel_Type()
)
isisSysStatLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisSysStatLevel.setStatus("current")
_IsisSysStatCorrLSPs_Type = Counter32
_IsisSysStatCorrLSPs_Object = MibTableColumn
isisSysStatCorrLSPs = _IsisSysStatCorrLSPs_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 6, 1, 2),
    _IsisSysStatCorrLSPs_Type()
)
isisSysStatCorrLSPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatCorrLSPs.setStatus("current")
if mibBuilder.loadTexts:
    isisSysStatCorrLSPs.setUnits("frames")
_IsisSysStatAuthTypeFails_Type = Counter32
_IsisSysStatAuthTypeFails_Object = MibTableColumn
isisSysStatAuthTypeFails = _IsisSysStatAuthTypeFails_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 6, 1, 3),
    _IsisSysStatAuthTypeFails_Type()
)
isisSysStatAuthTypeFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatAuthTypeFails.setStatus("current")
if mibBuilder.loadTexts:
    isisSysStatAuthTypeFails.setUnits("frames")
_IsisSysStatAuthFails_Type = Counter32
_IsisSysStatAuthFails_Object = MibTableColumn
isisSysStatAuthFails = _IsisSysStatAuthFails_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 6, 1, 4),
    _IsisSysStatAuthFails_Type()
)
isisSysStatAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatAuthFails.setStatus("current")
if mibBuilder.loadTexts:
    isisSysStatAuthFails.setUnits("frames")
_IsisSysStatLSPDbaseOloads_Type = Counter32
_IsisSysStatLSPDbaseOloads_Object = MibTableColumn
isisSysStatLSPDbaseOloads = _IsisSysStatLSPDbaseOloads_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 6, 1, 5),
    _IsisSysStatLSPDbaseOloads_Type()
)
isisSysStatLSPDbaseOloads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatLSPDbaseOloads.setStatus("current")
_IsisSysStatManAddrDropFromAreas_Type = Counter32
_IsisSysStatManAddrDropFromAreas_Object = MibTableColumn
isisSysStatManAddrDropFromAreas = _IsisSysStatManAddrDropFromAreas_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 6, 1, 6),
    _IsisSysStatManAddrDropFromAreas_Type()
)
isisSysStatManAddrDropFromAreas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatManAddrDropFromAreas.setStatus("current")
_IsisSysStatAttmptToExMaxSeqNums_Type = Counter32
_IsisSysStatAttmptToExMaxSeqNums_Object = MibTableColumn
isisSysStatAttmptToExMaxSeqNums = _IsisSysStatAttmptToExMaxSeqNums_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 6, 1, 7),
    _IsisSysStatAttmptToExMaxSeqNums_Type()
)
isisSysStatAttmptToExMaxSeqNums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatAttmptToExMaxSeqNums.setStatus("current")
_IsisSysStatSeqNumSkips_Type = Counter32
_IsisSysStatSeqNumSkips_Object = MibTableColumn
isisSysStatSeqNumSkips = _IsisSysStatSeqNumSkips_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 6, 1, 8),
    _IsisSysStatSeqNumSkips_Type()
)
isisSysStatSeqNumSkips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatSeqNumSkips.setStatus("current")
_IsisSysStatOwnLSPPurges_Type = Counter32
_IsisSysStatOwnLSPPurges_Object = MibTableColumn
isisSysStatOwnLSPPurges = _IsisSysStatOwnLSPPurges_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 6, 1, 9),
    _IsisSysStatOwnLSPPurges_Type()
)
isisSysStatOwnLSPPurges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatOwnLSPPurges.setStatus("current")
_IsisSysStatIDFieldLenMismatches_Type = Counter32
_IsisSysStatIDFieldLenMismatches_Object = MibTableColumn
isisSysStatIDFieldLenMismatches = _IsisSysStatIDFieldLenMismatches_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 6, 1, 10),
    _IsisSysStatIDFieldLenMismatches_Type()
)
isisSysStatIDFieldLenMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatIDFieldLenMismatches.setStatus("current")
if mibBuilder.loadTexts:
    isisSysStatIDFieldLenMismatches.setUnits("frames")
_IsisSysStatMaxAreaAddrMismatches_Type = Counter32
_IsisSysStatMaxAreaAddrMismatches_Object = MibTableColumn
isisSysStatMaxAreaAddrMismatches = _IsisSysStatMaxAreaAddrMismatches_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 6, 1, 11),
    _IsisSysStatMaxAreaAddrMismatches_Type()
)
isisSysStatMaxAreaAddrMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatMaxAreaAddrMismatches.setStatus("current")
if mibBuilder.loadTexts:
    isisSysStatMaxAreaAddrMismatches.setUnits("frames")
_IsisSysStatPartChanges_Type = Counter32
_IsisSysStatPartChanges_Object = MibTableColumn
isisSysStatPartChanges = _IsisSysStatPartChanges_Object(
    (1, 3, 6, 1, 3, 37, 1, 1, 6, 1, 12),
    _IsisSysStatPartChanges_Type()
)
isisSysStatPartChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatPartChanges.setStatus("current")
_IsisCirc_ObjectIdentity = ObjectIdentity
isisCirc = _IsisCirc_ObjectIdentity(
    (1, 3, 6, 1, 3, 37, 1, 2)
)
if mibBuilder.loadTexts:
    isisCirc.setStatus("current")
_IsisCircTable_Object = MibTable
isisCircTable = _IsisCircTable_Object(
    (1, 3, 6, 1, 3, 37, 1, 2, 1)
)
if mibBuilder.loadTexts:
    isisCircTable.setStatus("current")
_IsisCircEntry_Object = MibTableRow
isisCircEntry = _IsisCircEntry_Object(
    (1, 3, 6, 1, 3, 37, 1, 2, 1, 1)
)
isisCircEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "ISIS-MIB", "isisCircIndex"),
)
if mibBuilder.loadTexts:
    isisCircEntry.setStatus("current")


class _IsisCircIndex_Type(Integer32):
    """Custom type isisCircIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000000),
    )


_IsisCircIndex_Type.__name__ = "Integer32"
_IsisCircIndex_Object = MibTableColumn
isisCircIndex = _IsisCircIndex_Object(
    (1, 3, 6, 1, 3, 37, 1, 2, 1, 1, 1),
    _IsisCircIndex_Type()
)
isisCircIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisCircIndex.setStatus("current")
_IsisCircIfIndex_Type = Integer32
_IsisCircIfIndex_Object = MibTableColumn
isisCircIfIndex = _IsisCircIfIndex_Object(
    (1, 3, 6, 1, 3, 37, 1, 2, 1, 1, 2),
    _IsisCircIfIndex_Type()
)
isisCircIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircIfIndex.setStatus("current")
_IsisCircIfSubIndex_Type = Integer32
_IsisCircIfSubIndex_Object = MibTableColumn
isisCircIfSubIndex = _IsisCircIfSubIndex_Object(
    (1, 3, 6, 1, 3, 37, 1, 2, 1, 1, 3),
    _IsisCircIfSubIndex_Type()
)
isisCircIfSubIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircIfSubIndex.setStatus("current")


class _IsisCircLocalID_Type(Integer32):
    """Custom type isisCircLocalID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IsisCircLocalID_Type.__name__ = "Integer32"
_IsisCircLocalID_Object = MibTableColumn
isisCircLocalID = _IsisCircLocalID_Object(
    (1, 3, 6, 1, 3, 37, 1, 2, 1, 1, 4),
    _IsisCircLocalID_Type()
)
isisCircLocalID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircLocalID.setStatus("current")


class _IsisCircAdminState_Type(AdminState):
    """Custom type isisCircAdminState based on AdminState"""
    defaultValue = 1


_IsisCircAdminState_Type.__name__ = "AdminState"
_IsisCircAdminState_Object = MibTableColumn
isisCircAdminState = _IsisCircAdminState_Object(
    (1, 3, 6, 1, 3, 37, 1, 2, 1, 1, 5),
    _IsisCircAdminState_Type()
)
isisCircAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircAdminState.setStatus("current")


class _IsisCircExistState_Type(RowStatus):
    """Custom type isisCircExistState based on RowStatus"""
    defaultValue = 1


_IsisCircExistState_Type.__name__ = "RowStatus"
_IsisCircExistState_Object = MibTableColumn
isisCircExistState = _IsisCircExistState_Object(
    (1, 3, 6, 1, 3, 37, 1, 2, 1, 1, 6),
    _IsisCircExistState_Type()
)
isisCircExistState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircExistState.setStatus("current")


class _IsisCircType_Type(Integer32):
    """Custom type isisCircType based on Integer32"""
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
        *(("broadcast", 1),
          ("ptToPt", 2),
          ("staticIn", 3),
          ("staticOut", 4),
          ("dA", 5))
    )


_IsisCircType_Type.__name__ = "Integer32"
_IsisCircType_Object = MibTableColumn
isisCircType = _IsisCircType_Object(
    (1, 3, 6, 1, 3, 37, 1, 2, 1, 1, 7),
    _IsisCircType_Type()
)
isisCircType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircType.setStatus("current")


class _IsisCircExtDomain_Type(TruthValue):
    """Custom type isisCircExtDomain based on TruthValue"""
    defaultValue = 2


_IsisCircExtDomain_Type.__name__ = "TruthValue"
_IsisCircExtDomain_Object = MibTableColumn
isisCircExtDomain = _IsisCircExtDomain_Object(
    (1, 3, 6, 1, 3, 37, 1, 2, 1, 1, 8),
    _IsisCircExtDomain_Type()
)
isisCircExtDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircExtDomain.setStatus("current")
_IsisCircAdjChanges_Type = Counter32
_IsisCircAdjChanges_Object = MibTableColumn
isisCircAdjChanges = _IsisCircAdjChanges_Object(
    (1, 3, 6, 1, 3, 37, 1, 2, 1, 1, 9),
    _IsisCircAdjChanges_Type()
)
isisCircAdjChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircAdjChanges.setStatus("current")
_IsisCircInitFails_Type = Counter32
_IsisCircInitFails_Object = MibTableColumn
isisCircInitFails = _IsisCircInitFails_Object(
    (1, 3, 6, 1, 3, 37, 1, 2, 1, 1, 10),
    _IsisCircInitFails_Type()
)
isisCircInitFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircInitFails.setStatus("current")
_IsisCircRejAdjs_Type = Counter32
_IsisCircRejAdjs_Object = MibTableColumn
isisCircRejAdjs = _IsisCircRejAdjs_Object(
    (1, 3, 6, 1, 3, 37, 1, 2, 1, 1, 11),
    _IsisCircRejAdjs_Type()
)
isisCircRejAdjs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircRejAdjs.setStatus("current")
_IsisCircOutCtrlPDUs_Type = Counter32
_IsisCircOutCtrlPDUs_Object = MibTableColumn
isisCircOutCtrlPDUs = _IsisCircOutCtrlPDUs_Object(
    (1, 3, 6, 1, 3, 37, 1, 2, 1, 1, 12),
    _IsisCircOutCtrlPDUs_Type()
)
isisCircOutCtrlPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircOutCtrlPDUs.setStatus("current")
if mibBuilder.loadTexts:
    isisCircOutCtrlPDUs.setUnits("frames")
_IsisCircInCtrlPDUs_Type = Counter32
_IsisCircInCtrlPDUs_Object = MibTableColumn
isisCircInCtrlPDUs = _IsisCircInCtrlPDUs_Object(
    (1, 3, 6, 1, 3, 37, 1, 2, 1, 1, 13),
    _IsisCircInCtrlPDUs_Type()
)
isisCircInCtrlPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircInCtrlPDUs.setStatus("current")
if mibBuilder.loadTexts:
    isisCircInCtrlPDUs.setUnits("frames")
_IsisCircIDFieldLenMismatches_Type = Counter32
_IsisCircIDFieldLenMismatches_Object = MibTableColumn
isisCircIDFieldLenMismatches = _IsisCircIDFieldLenMismatches_Object(
    (1, 3, 6, 1, 3, 37, 1, 2, 1, 1, 14),
    _IsisCircIDFieldLenMismatches_Type()
)
isisCircIDFieldLenMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircIDFieldLenMismatches.setStatus("current")
if mibBuilder.loadTexts:
    isisCircIDFieldLenMismatches.setUnits("frames")


class _IsisCircLevel_Type(Integer32):
    """Custom type isisCircLevel based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("level1", 1),
          ("level2", 2),
          ("level1L2", 3))
    )


_IsisCircLevel_Type.__name__ = "Integer32"
_IsisCircLevel_Object = MibTableColumn
isisCircLevel = _IsisCircLevel_Object(
    (1, 3, 6, 1, 3, 37, 1, 2, 1, 1, 15),
    _IsisCircLevel_Type()
)
isisCircLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircLevel.setStatus("current")


class _IsisCircMCAddr_Type(Integer32):
    """Custom type isisCircMCAddr based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("group", 1),
          ("functional", 2))
    )


_IsisCircMCAddr_Type.__name__ = "Integer32"
_IsisCircMCAddr_Object = MibTableColumn
isisCircMCAddr = _IsisCircMCAddr_Object(
    (1, 3, 6, 1, 3, 37, 1, 2, 1, 1, 16),
    _IsisCircMCAddr_Type()
)
isisCircMCAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircMCAddr.setStatus("current")
_IsisCircPtToPtCircID_Type = CircuitID
_IsisCircPtToPtCircID_Object = MibTableColumn
isisCircPtToPtCircID = _IsisCircPtToPtCircID_Object(
    (1, 3, 6, 1, 3, 37, 1, 2, 1, 1, 17),
    _IsisCircPtToPtCircID_Type()
)
isisCircPtToPtCircID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircPtToPtCircID.setStatus("current")


class _IsisCircPassiveCircuit_Type(TruthValue):
    """Custom type isisCircPassiveCircuit based on TruthValue"""
    defaultValue = 2


_IsisCircPassiveCircuit_Type.__name__ = "TruthValue"
_IsisCircPassiveCircuit_Object = MibTableColumn
isisCircPassiveCircuit = _IsisCircPassiveCircuit_Object(
    (1, 3, 6, 1, 3, 37, 1, 2, 1, 1, 18),
    _IsisCircPassiveCircuit_Type()
)
isisCircPassiveCircuit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircPassiveCircuit.setStatus("current")


class _IsisCircMeshGroupEnabled_Type(Integer32):
    """Custom type isisCircMeshGroupEnabled based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("blocked", 2),
          ("set", 3))
    )


_IsisCircMeshGroupEnabled_Type.__name__ = "Integer32"
_IsisCircMeshGroupEnabled_Object = MibTableColumn
isisCircMeshGroupEnabled = _IsisCircMeshGroupEnabled_Object(
    (1, 3, 6, 1, 3, 37, 1, 2, 1, 1, 19),
    _IsisCircMeshGroupEnabled_Type()
)
isisCircMeshGroupEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircMeshGroupEnabled.setStatus("current")


class _IsisCircMeshGroup_Type(Integer32):
    """Custom type isisCircMeshGroup based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000000),
    )


_IsisCircMeshGroup_Type.__name__ = "Integer32"
_IsisCircMeshGroup_Object = MibTableColumn
isisCircMeshGroup = _IsisCircMeshGroup_Object(
    (1, 3, 6, 1, 3, 37, 1, 2, 1, 1, 20),
    _IsisCircMeshGroup_Type()
)
isisCircMeshGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircMeshGroup.setStatus("current")


class _IsisCircSmallHellos_Type(AdminState):
    """Custom type isisCircSmallHellos based on AdminState"""
    defaultValue = 1


_IsisCircSmallHellos_Type.__name__ = "AdminState"
_IsisCircSmallHellos_Object = MibTableColumn
isisCircSmallHellos = _IsisCircSmallHellos_Object(
    (1, 3, 6, 1, 3, 37, 1, 2, 1, 1, 21),
    _IsisCircSmallHellos_Type()
)
isisCircSmallHellos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircSmallHellos.setStatus("current")
_IsisCircUpTime_Type = UpTime
_IsisCircUpTime_Object = MibTableColumn
isisCircUpTime = _IsisCircUpTime_Object(
    (1, 3, 6, 1, 3, 37, 1, 2, 1, 1, 22),
    _IsisCircUpTime_Type()
)
isisCircUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircUpTime.setStatus("current")
if mibBuilder.loadTexts:
    isisCircUpTime.setUnits("seconds")
_IsisCircLevelValues_ObjectIdentity = ObjectIdentity
isisCircLevelValues = _IsisCircLevelValues_ObjectIdentity(
    (1, 3, 6, 1, 3, 37, 1, 3)
)
if mibBuilder.loadTexts:
    isisCircLevelValues.setStatus("current")
_IsisCircLevelTable_Object = MibTable
isisCircLevelTable = _IsisCircLevelTable_Object(
    (1, 3, 6, 1, 3, 37, 1, 3, 1)
)
if mibBuilder.loadTexts:
    isisCircLevelTable.setStatus("current")
_IsisCircLevelEntry_Object = MibTableRow
isisCircLevelEntry = _IsisCircLevelEntry_Object(
    (1, 3, 6, 1, 3, 37, 1, 3, 1, 1)
)
isisCircLevelEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "ISIS-MIB", "isisCircIndex"),
    (0, "ISIS-MIB", "isisCircLevelIndex"),
)
if mibBuilder.loadTexts:
    isisCircLevelEntry.setStatus("current")


class _IsisCircLevelIndex_Type(Integer32):
    """Custom type isisCircLevelIndex based on Integer32"""
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


_IsisCircLevelIndex_Type.__name__ = "Integer32"
_IsisCircLevelIndex_Object = MibTableColumn
isisCircLevelIndex = _IsisCircLevelIndex_Object(
    (1, 3, 6, 1, 3, 37, 1, 3, 1, 1, 1),
    _IsisCircLevelIndex_Type()
)
isisCircLevelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisCircLevelIndex.setStatus("current")


class _IsisCircLevelMetric_Type(DefaultMetric):
    """Custom type isisCircLevelMetric based on DefaultMetric"""
    defaultValue = 10


_IsisCircLevelMetric_Type.__name__ = "DefaultMetric"
_IsisCircLevelMetric_Object = MibTableColumn
isisCircLevelMetric = _IsisCircLevelMetric_Object(
    (1, 3, 6, 1, 3, 37, 1, 3, 1, 1, 2),
    _IsisCircLevelMetric_Type()
)
isisCircLevelMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircLevelMetric.setStatus("current")


class _IsisCircLevelISPriority_Type(ISPriority):
    """Custom type isisCircLevelISPriority based on ISPriority"""
    defaultValue = 64


_IsisCircLevelISPriority_Type.__name__ = "ISPriority"
_IsisCircLevelISPriority_Object = MibTableColumn
isisCircLevelISPriority = _IsisCircLevelISPriority_Object(
    (1, 3, 6, 1, 3, 37, 1, 3, 1, 1, 3),
    _IsisCircLevelISPriority_Type()
)
isisCircLevelISPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircLevelISPriority.setStatus("current")


class _IsisCircLevelDesIS_Type(OctetString):
    """Custom type isisCircLevelDesIS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_IsisCircLevelDesIS_Type.__name__ = "OctetString"
_IsisCircLevelDesIS_Object = MibTableColumn
isisCircLevelDesIS = _IsisCircLevelDesIS_Object(
    (1, 3, 6, 1, 3, 37, 1, 3, 1, 1, 4),
    _IsisCircLevelDesIS_Type()
)
isisCircLevelDesIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircLevelDesIS.setStatus("current")
_IsisCircLevelLANDesISChanges_Type = Counter32
_IsisCircLevelLANDesISChanges_Object = MibTableColumn
isisCircLevelLANDesISChanges = _IsisCircLevelLANDesISChanges_Object(
    (1, 3, 6, 1, 3, 37, 1, 3, 1, 1, 5),
    _IsisCircLevelLANDesISChanges_Type()
)
isisCircLevelLANDesISChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircLevelLANDesISChanges.setStatus("current")


class _IsisCircLevelHelloMultiplier_Type(Integer32):
    """Custom type isisCircLevelHelloMultiplier based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 100),
    )


_IsisCircLevelHelloMultiplier_Type.__name__ = "Integer32"
_IsisCircLevelHelloMultiplier_Object = MibTableColumn
isisCircLevelHelloMultiplier = _IsisCircLevelHelloMultiplier_Object(
    (1, 3, 6, 1, 3, 37, 1, 3, 1, 1, 6),
    _IsisCircLevelHelloMultiplier_Type()
)
isisCircLevelHelloMultiplier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircLevelHelloMultiplier.setStatus("current")


class _IsisCircLevelHelloTimer_Type(Integer32):
    """Custom type isisCircLevelHelloTimer based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600000),
    )


_IsisCircLevelHelloTimer_Type.__name__ = "Integer32"
_IsisCircLevelHelloTimer_Object = MibTableColumn
isisCircLevelHelloTimer = _IsisCircLevelHelloTimer_Object(
    (1, 3, 6, 1, 3, 37, 1, 3, 1, 1, 7),
    _IsisCircLevelHelloTimer_Type()
)
isisCircLevelHelloTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircLevelHelloTimer.setStatus("current")
if mibBuilder.loadTexts:
    isisCircLevelHelloTimer.setUnits("milliseconds")


class _IsisCircLevelDRHelloTimer_Type(Integer32):
    """Custom type isisCircLevelDRHelloTimer based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 120000),
    )


_IsisCircLevelDRHelloTimer_Type.__name__ = "Integer32"
_IsisCircLevelDRHelloTimer_Object = MibTableColumn
isisCircLevelDRHelloTimer = _IsisCircLevelDRHelloTimer_Object(
    (1, 3, 6, 1, 3, 37, 1, 3, 1, 1, 8),
    _IsisCircLevelDRHelloTimer_Type()
)
isisCircLevelDRHelloTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircLevelDRHelloTimer.setStatus("current")
if mibBuilder.loadTexts:
    isisCircLevelDRHelloTimer.setUnits("milliseconds")


class _IsisCircLevelLSPThrottle_Type(Integer32):
    """Custom type isisCircLevelLSPThrottle based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsisCircLevelLSPThrottle_Type.__name__ = "Integer32"
_IsisCircLevelLSPThrottle_Object = MibTableColumn
isisCircLevelLSPThrottle = _IsisCircLevelLSPThrottle_Object(
    (1, 3, 6, 1, 3, 37, 1, 3, 1, 1, 9),
    _IsisCircLevelLSPThrottle_Type()
)
isisCircLevelLSPThrottle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircLevelLSPThrottle.setStatus("current")
if mibBuilder.loadTexts:
    isisCircLevelLSPThrottle.setUnits("milliseconds")


class _IsisCircLevelMinLSPRetransInt_Type(Integer32):
    """Custom type isisCircLevelMinLSPRetransInt based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_IsisCircLevelMinLSPRetransInt_Type.__name__ = "Integer32"
_IsisCircLevelMinLSPRetransInt_Object = MibTableColumn
isisCircLevelMinLSPRetransInt = _IsisCircLevelMinLSPRetransInt_Object(
    (1, 3, 6, 1, 3, 37, 1, 3, 1, 1, 10),
    _IsisCircLevelMinLSPRetransInt_Type()
)
isisCircLevelMinLSPRetransInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircLevelMinLSPRetransInt.setStatus("current")
if mibBuilder.loadTexts:
    isisCircLevelMinLSPRetransInt.setUnits("seconds")


class _IsisCircLevelCSNPInterval_Type(Integer32):
    """Custom type isisCircLevelCSNPInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_IsisCircLevelCSNPInterval_Type.__name__ = "Integer32"
_IsisCircLevelCSNPInterval_Object = MibTableColumn
isisCircLevelCSNPInterval = _IsisCircLevelCSNPInterval_Object(
    (1, 3, 6, 1, 3, 37, 1, 3, 1, 1, 11),
    _IsisCircLevelCSNPInterval_Type()
)
isisCircLevelCSNPInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircLevelCSNPInterval.setStatus("current")
if mibBuilder.loadTexts:
    isisCircLevelCSNPInterval.setUnits("seconds")


class _IsisCircLevelPartSNPInterval_Type(Integer32):
    """Custom type isisCircLevelPartSNPInterval based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_IsisCircLevelPartSNPInterval_Type.__name__ = "Integer32"
_IsisCircLevelPartSNPInterval_Object = MibTableColumn
isisCircLevelPartSNPInterval = _IsisCircLevelPartSNPInterval_Object(
    (1, 3, 6, 1, 3, 37, 1, 3, 1, 1, 12),
    _IsisCircLevelPartSNPInterval_Type()
)
isisCircLevelPartSNPInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircLevelPartSNPInterval.setStatus("current")
if mibBuilder.loadTexts:
    isisCircLevelPartSNPInterval.setUnits("seconds")
_IsisCircPDUCounters_ObjectIdentity = ObjectIdentity
isisCircPDUCounters = _IsisCircPDUCounters_ObjectIdentity(
    (1, 3, 6, 1, 3, 37, 1, 4)
)
if mibBuilder.loadTexts:
    isisCircPDUCounters.setStatus("current")
_IsisPacketCountTable_Object = MibTable
isisPacketCountTable = _IsisPacketCountTable_Object(
    (1, 3, 6, 1, 3, 37, 1, 4, 1)
)
if mibBuilder.loadTexts:
    isisPacketCountTable.setStatus("current")
_IsisPacketCountEntry_Object = MibTableRow
isisPacketCountEntry = _IsisPacketCountEntry_Object(
    (1, 3, 6, 1, 3, 37, 1, 4, 1, 1)
)
isisPacketCountEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "ISIS-MIB", "isisCircIndex"),
    (0, "ISIS-MIB", "isisPacketCountLevel"),
    (0, "ISIS-MIB", "isisPacketCountDirection"),
)
if mibBuilder.loadTexts:
    isisPacketCountEntry.setStatus("current")


class _IsisPacketCountLevel_Type(Integer32):
    """Custom type isisPacketCountLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level1", 1),
          ("level2", 2))
    )


_IsisPacketCountLevel_Type.__name__ = "Integer32"
_IsisPacketCountLevel_Object = MibTableColumn
isisPacketCountLevel = _IsisPacketCountLevel_Object(
    (1, 3, 6, 1, 3, 37, 1, 4, 1, 1, 1),
    _IsisPacketCountLevel_Type()
)
isisPacketCountLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisPacketCountLevel.setStatus("current")


class _IsisPacketCountDirection_Type(Integer32):
    """Custom type isisPacketCountDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sending", 1),
          ("receiving", 2))
    )


_IsisPacketCountDirection_Type.__name__ = "Integer32"
_IsisPacketCountDirection_Object = MibTableColumn
isisPacketCountDirection = _IsisPacketCountDirection_Object(
    (1, 3, 6, 1, 3, 37, 1, 4, 1, 1, 2),
    _IsisPacketCountDirection_Type()
)
isisPacketCountDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisPacketCountDirection.setStatus("current")
_IsisPacketCountHello_Type = Counter32
_IsisPacketCountHello_Object = MibTableColumn
isisPacketCountHello = _IsisPacketCountHello_Object(
    (1, 3, 6, 1, 3, 37, 1, 4, 1, 1, 3),
    _IsisPacketCountHello_Type()
)
isisPacketCountHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisPacketCountHello.setStatus("current")
if mibBuilder.loadTexts:
    isisPacketCountHello.setUnits("frames")
_IsisPacketCountLSP_Type = Counter32
_IsisPacketCountLSP_Object = MibTableColumn
isisPacketCountLSP = _IsisPacketCountLSP_Object(
    (1, 3, 6, 1, 3, 37, 1, 4, 1, 1, 4),
    _IsisPacketCountLSP_Type()
)
isisPacketCountLSP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisPacketCountLSP.setStatus("current")
if mibBuilder.loadTexts:
    isisPacketCountLSP.setUnits("frames")
_IsisPacketCountCSNP_Type = Counter32
_IsisPacketCountCSNP_Object = MibTableColumn
isisPacketCountCSNP = _IsisPacketCountCSNP_Object(
    (1, 3, 6, 1, 3, 37, 1, 4, 1, 1, 5),
    _IsisPacketCountCSNP_Type()
)
isisPacketCountCSNP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisPacketCountCSNP.setStatus("current")
if mibBuilder.loadTexts:
    isisPacketCountCSNP.setUnits("frames")
_IsisPacketCountPSNP_Type = Counter32
_IsisPacketCountPSNP_Object = MibTableColumn
isisPacketCountPSNP = _IsisPacketCountPSNP_Object(
    (1, 3, 6, 1, 3, 37, 1, 4, 1, 1, 6),
    _IsisPacketCountPSNP_Type()
)
isisPacketCountPSNP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisPacketCountPSNP.setStatus("current")
if mibBuilder.loadTexts:
    isisPacketCountPSNP.setUnits("frames")
_IsisISAdj_ObjectIdentity = ObjectIdentity
isisISAdj = _IsisISAdj_ObjectIdentity(
    (1, 3, 6, 1, 3, 37, 1, 5)
)
if mibBuilder.loadTexts:
    isisISAdj.setStatus("current")
_IsisISAdjTable_Object = MibTable
isisISAdjTable = _IsisISAdjTable_Object(
    (1, 3, 6, 1, 3, 37, 1, 5, 1)
)
if mibBuilder.loadTexts:
    isisISAdjTable.setStatus("current")
_IsisISAdjEntry_Object = MibTableRow
isisISAdjEntry = _IsisISAdjEntry_Object(
    (1, 3, 6, 1, 3, 37, 1, 5, 1, 1)
)
isisISAdjEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "ISIS-MIB", "isisCircIndex"),
    (0, "ISIS-MIB", "isisISAdjIndex"),
)
if mibBuilder.loadTexts:
    isisISAdjEntry.setStatus("current")


class _IsisISAdjIndex_Type(Integer32):
    """Custom type isisISAdjIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000000),
    )


_IsisISAdjIndex_Type.__name__ = "Integer32"
_IsisISAdjIndex_Object = MibTableColumn
isisISAdjIndex = _IsisISAdjIndex_Object(
    (1, 3, 6, 1, 3, 37, 1, 5, 1, 1, 1),
    _IsisISAdjIndex_Type()
)
isisISAdjIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisISAdjIndex.setStatus("current")


class _IsisISAdjState_Type(Integer32):
    """Custom type isisISAdjState based on Integer32"""
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


_IsisISAdjState_Type.__name__ = "Integer32"
_IsisISAdjState_Object = MibTableColumn
isisISAdjState = _IsisISAdjState_Object(
    (1, 3, 6, 1, 3, 37, 1, 5, 1, 1, 2),
    _IsisISAdjState_Type()
)
isisISAdjState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjState.setStatus("current")
_IsisISAdjNeighSNPAAddress_Type = OSINSAddress
_IsisISAdjNeighSNPAAddress_Object = MibTableColumn
isisISAdjNeighSNPAAddress = _IsisISAdjNeighSNPAAddress_Object(
    (1, 3, 6, 1, 3, 37, 1, 5, 1, 1, 3),
    _IsisISAdjNeighSNPAAddress_Type()
)
isisISAdjNeighSNPAAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjNeighSNPAAddress.setStatus("current")


class _IsisISAdjNeighSysType_Type(Integer32):
    """Custom type isisISAdjNeighSysType based on Integer32"""
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


_IsisISAdjNeighSysType_Type.__name__ = "Integer32"
_IsisISAdjNeighSysType_Object = MibTableColumn
isisISAdjNeighSysType = _IsisISAdjNeighSysType_Object(
    (1, 3, 6, 1, 3, 37, 1, 5, 1, 1, 4),
    _IsisISAdjNeighSysType_Type()
)
isisISAdjNeighSysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjNeighSysType.setStatus("current")


class _IsisISAdjNeighSysID_Type(OctetString):
    """Custom type isisISAdjNeighSysID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_IsisISAdjNeighSysID_Type.__name__ = "OctetString"
_IsisISAdjNeighSysID_Object = MibTableColumn
isisISAdjNeighSysID = _IsisISAdjNeighSysID_Object(
    (1, 3, 6, 1, 3, 37, 1, 5, 1, 1, 5),
    _IsisISAdjNeighSysID_Type()
)
isisISAdjNeighSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjNeighSysID.setStatus("current")


class _IsisISAdjUsage_Type(Integer32):
    """Custom type isisISAdjUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("level1", 1),
          ("level2", 2),
          ("level1and2", 3))
    )


_IsisISAdjUsage_Type.__name__ = "Integer32"
_IsisISAdjUsage_Object = MibTableColumn
isisISAdjUsage = _IsisISAdjUsage_Object(
    (1, 3, 6, 1, 3, 37, 1, 5, 1, 1, 6),
    _IsisISAdjUsage_Type()
)
isisISAdjUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjUsage.setStatus("current")


class _IsisISAdjHoldTimer_Type(Integer32):
    """Custom type isisISAdjHoldTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsisISAdjHoldTimer_Type.__name__ = "Integer32"
_IsisISAdjHoldTimer_Object = MibTableColumn
isisISAdjHoldTimer = _IsisISAdjHoldTimer_Object(
    (1, 3, 6, 1, 3, 37, 1, 5, 1, 1, 7),
    _IsisISAdjHoldTimer_Type()
)
isisISAdjHoldTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjHoldTimer.setStatus("current")
if mibBuilder.loadTexts:
    isisISAdjHoldTimer.setUnits("seconds")
_IsisISAdjNeighPriority_Type = ISPriority
_IsisISAdjNeighPriority_Object = MibTableColumn
isisISAdjNeighPriority = _IsisISAdjNeighPriority_Object(
    (1, 3, 6, 1, 3, 37, 1, 5, 1, 1, 8),
    _IsisISAdjNeighPriority_Type()
)
isisISAdjNeighPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjNeighPriority.setStatus("current")
_IsisISAdjUpTime_Type = UpTime
_IsisISAdjUpTime_Object = MibTableColumn
isisISAdjUpTime = _IsisISAdjUpTime_Object(
    (1, 3, 6, 1, 3, 37, 1, 5, 1, 1, 9),
    _IsisISAdjUpTime_Type()
)
isisISAdjUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjUpTime.setStatus("current")
if mibBuilder.loadTexts:
    isisISAdjUpTime.setUnits("seconds")
_IsisISAdjAreaAddrTable_Object = MibTable
isisISAdjAreaAddrTable = _IsisISAdjAreaAddrTable_Object(
    (1, 3, 6, 1, 3, 37, 1, 5, 2)
)
if mibBuilder.loadTexts:
    isisISAdjAreaAddrTable.setStatus("current")
_IsisISAdjAreaAddrEntry_Object = MibTableRow
isisISAdjAreaAddrEntry = _IsisISAdjAreaAddrEntry_Object(
    (1, 3, 6, 1, 3, 37, 1, 5, 2, 1)
)
isisISAdjAreaAddrEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "ISIS-MIB", "isisCircIndex"),
    (0, "ISIS-MIB", "isisISAdjIndex"),
    (0, "ISIS-MIB", "isisISAdjAreaAddrIndex"),
    (0, "ISIS-MIB", "isisISAdjAreaAddress"),
)
if mibBuilder.loadTexts:
    isisISAdjAreaAddrEntry.setStatus("current")


class _IsisISAdjAreaAddrIndex_Type(Integer32):
    """Custom type isisISAdjAreaAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000000),
    )


_IsisISAdjAreaAddrIndex_Type.__name__ = "Integer32"
_IsisISAdjAreaAddrIndex_Object = MibTableColumn
isisISAdjAreaAddrIndex = _IsisISAdjAreaAddrIndex_Object(
    (1, 3, 6, 1, 3, 37, 1, 5, 2, 1, 1),
    _IsisISAdjAreaAddrIndex_Type()
)
isisISAdjAreaAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisISAdjAreaAddrIndex.setStatus("current")
_IsisISAdjAreaAddress_Type = OSINSAddress
_IsisISAdjAreaAddress_Object = MibTableColumn
isisISAdjAreaAddress = _IsisISAdjAreaAddress_Object(
    (1, 3, 6, 1, 3, 37, 1, 5, 2, 1, 2),
    _IsisISAdjAreaAddress_Type()
)
isisISAdjAreaAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjAreaAddress.setStatus("current")
_IsisISAdjIPAddrTable_Object = MibTable
isisISAdjIPAddrTable = _IsisISAdjIPAddrTable_Object(
    (1, 3, 6, 1, 3, 37, 1, 5, 3)
)
if mibBuilder.loadTexts:
    isisISAdjIPAddrTable.setStatus("current")
_IsisISAdjIPAddrEntry_Object = MibTableRow
isisISAdjIPAddrEntry = _IsisISAdjIPAddrEntry_Object(
    (1, 3, 6, 1, 3, 37, 1, 5, 3, 1)
)
isisISAdjIPAddrEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "ISIS-MIB", "isisCircIndex"),
    (0, "ISIS-MIB", "isisISAdjIndex"),
    (0, "ISIS-MIB", "isisISAdjIPAddrIndex"),
)
if mibBuilder.loadTexts:
    isisISAdjIPAddrEntry.setStatus("current")


class _IsisISAdjIPAddrIndex_Type(Integer32):
    """Custom type isisISAdjIPAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000000),
    )


_IsisISAdjIPAddrIndex_Type.__name__ = "Integer32"
_IsisISAdjIPAddrIndex_Object = MibTableColumn
isisISAdjIPAddrIndex = _IsisISAdjIPAddrIndex_Object(
    (1, 3, 6, 1, 3, 37, 1, 5, 3, 1, 1),
    _IsisISAdjIPAddrIndex_Type()
)
isisISAdjIPAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisISAdjIPAddrIndex.setStatus("current")
_IsisISAdjIPAddressType_Type = InetAddressType
_IsisISAdjIPAddressType_Object = MibTableColumn
isisISAdjIPAddressType = _IsisISAdjIPAddressType_Object(
    (1, 3, 6, 1, 3, 37, 1, 5, 3, 1, 2),
    _IsisISAdjIPAddressType_Type()
)
isisISAdjIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjIPAddressType.setStatus("current")


class _IsisISAdjIPAddress_Type(InetAddress):
    """Custom type isisISAdjIPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_IsisISAdjIPAddress_Type.__name__ = "InetAddress"
_IsisISAdjIPAddress_Object = MibTableColumn
isisISAdjIPAddress = _IsisISAdjIPAddress_Object(
    (1, 3, 6, 1, 3, 37, 1, 5, 3, 1, 3),
    _IsisISAdjIPAddress_Type()
)
isisISAdjIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjIPAddress.setStatus("current")
_IsisISAdjProtSuppTable_Object = MibTable
isisISAdjProtSuppTable = _IsisISAdjProtSuppTable_Object(
    (1, 3, 6, 1, 3, 37, 1, 5, 4)
)
if mibBuilder.loadTexts:
    isisISAdjProtSuppTable.setStatus("current")
_IsisISAdjProtSuppEntry_Object = MibTableRow
isisISAdjProtSuppEntry = _IsisISAdjProtSuppEntry_Object(
    (1, 3, 6, 1, 3, 37, 1, 5, 4, 1)
)
isisISAdjProtSuppEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "ISIS-MIB", "isisCircIndex"),
    (0, "ISIS-MIB", "isisISAdjProtSuppIndex"),
    (0, "ISIS-MIB", "isisISAdjProtSuppProtocol"),
)
if mibBuilder.loadTexts:
    isisISAdjProtSuppEntry.setStatus("current")


class _IsisISAdjProtSuppIndex_Type(Integer32):
    """Custom type isisISAdjProtSuppIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000000),
    )


_IsisISAdjProtSuppIndex_Type.__name__ = "Integer32"
_IsisISAdjProtSuppIndex_Object = MibTableColumn
isisISAdjProtSuppIndex = _IsisISAdjProtSuppIndex_Object(
    (1, 3, 6, 1, 3, 37, 1, 5, 4, 1, 1),
    _IsisISAdjProtSuppIndex_Type()
)
isisISAdjProtSuppIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisISAdjProtSuppIndex.setStatus("current")
_IsisISAdjProtSuppProtocol_Type = SupportedProtocol
_IsisISAdjProtSuppProtocol_Object = MibTableColumn
isisISAdjProtSuppProtocol = _IsisISAdjProtSuppProtocol_Object(
    (1, 3, 6, 1, 3, 37, 1, 5, 4, 1, 2),
    _IsisISAdjProtSuppProtocol_Type()
)
isisISAdjProtSuppProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjProtSuppProtocol.setStatus("current")
_IsisReachAddr_ObjectIdentity = ObjectIdentity
isisReachAddr = _IsisReachAddr_ObjectIdentity(
    (1, 3, 6, 1, 3, 37, 1, 6)
)
if mibBuilder.loadTexts:
    isisReachAddr.setStatus("current")
_IsisIPReachAddr_ObjectIdentity = ObjectIdentity
isisIPReachAddr = _IsisIPReachAddr_ObjectIdentity(
    (1, 3, 6, 1, 3, 37, 1, 7)
)
if mibBuilder.loadTexts:
    isisIPReachAddr.setStatus("current")
_IsisIPRATable_Object = MibTable
isisIPRATable = _IsisIPRATable_Object(
    (1, 3, 6, 1, 3, 37, 1, 7, 1)
)
if mibBuilder.loadTexts:
    isisIPRATable.setStatus("current")
_IsisIPRAEntry_Object = MibTableRow
isisIPRAEntry = _IsisIPRAEntry_Object(
    (1, 3, 6, 1, 3, 37, 1, 7, 1, 1)
)
isisIPRAEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "ISIS-MIB", "isisIPRAType"),
    (0, "ISIS-MIB", "isisIPRAIndex"),
)
if mibBuilder.loadTexts:
    isisIPRAEntry.setStatus("current")


class _IsisIPRAIndex_Type(Integer32):
    """Custom type isisIPRAIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000000),
    )


_IsisIPRAIndex_Type.__name__ = "Integer32"
_IsisIPRAIndex_Object = MibTableColumn
isisIPRAIndex = _IsisIPRAIndex_Object(
    (1, 3, 6, 1, 3, 37, 1, 7, 1, 1, 1),
    _IsisIPRAIndex_Type()
)
isisIPRAIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisIPRAIndex.setStatus("current")


class _IsisIPRAType_Type(Integer32):
    """Custom type isisIPRAType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("automatic", 2))
    )


_IsisIPRAType_Type.__name__ = "Integer32"
_IsisIPRAType_Object = MibTableColumn
isisIPRAType = _IsisIPRAType_Object(
    (1, 3, 6, 1, 3, 37, 1, 7, 1, 1, 2),
    _IsisIPRAType_Type()
)
isisIPRAType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisIPRAType.setStatus("current")
_IsisIPRADestType_Type = InetAddressType
_IsisIPRADestType_Object = MibTableColumn
isisIPRADestType = _IsisIPRADestType_Object(
    (1, 3, 6, 1, 3, 37, 1, 7, 1, 1, 3),
    _IsisIPRADestType_Type()
)
isisIPRADestType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisIPRADestType.setStatus("current")


class _IsisIPRADest_Type(InetAddress):
    """Custom type isisIPRADest based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_IsisIPRADest_Type.__name__ = "InetAddress"
_IsisIPRADest_Object = MibTableColumn
isisIPRADest = _IsisIPRADest_Object(
    (1, 3, 6, 1, 3, 37, 1, 7, 1, 1, 4),
    _IsisIPRADest_Type()
)
isisIPRADest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisIPRADest.setStatus("current")


class _IsisIPRADestPrefixLen_Type(InetAddressPrefixLength):
    """Custom type isisIPRADestPrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_IsisIPRADestPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_IsisIPRADestPrefixLen_Object = MibTableColumn
isisIPRADestPrefixLen = _IsisIPRADestPrefixLen_Object(
    (1, 3, 6, 1, 3, 37, 1, 7, 1, 1, 5),
    _IsisIPRADestPrefixLen_Type()
)
isisIPRADestPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisIPRADestPrefixLen.setStatus("current")


class _IsisIPRAExistState_Type(RowStatus):
    """Custom type isisIPRAExistState based on RowStatus"""
    defaultValue = 1


_IsisIPRAExistState_Type.__name__ = "RowStatus"
_IsisIPRAExistState_Object = MibTableColumn
isisIPRAExistState = _IsisIPRAExistState_Object(
    (1, 3, 6, 1, 3, 37, 1, 7, 1, 1, 6),
    _IsisIPRAExistState_Type()
)
isisIPRAExistState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisIPRAExistState.setStatus("current")


class _IsisIPRAAdminState_Type(AdminState):
    """Custom type isisIPRAAdminState based on AdminState"""
    defaultValue = 1


_IsisIPRAAdminState_Type.__name__ = "AdminState"
_IsisIPRAAdminState_Object = MibTableColumn
isisIPRAAdminState = _IsisIPRAAdminState_Object(
    (1, 3, 6, 1, 3, 37, 1, 7, 1, 1, 7),
    _IsisIPRAAdminState_Type()
)
isisIPRAAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisIPRAAdminState.setStatus("current")


class _IsisIPRAMetric_Type(DefaultMetric):
    """Custom type isisIPRAMetric based on DefaultMetric"""
    defaultValue = 20


_IsisIPRAMetric_Type.__name__ = "DefaultMetric"
_IsisIPRAMetric_Object = MibTableColumn
isisIPRAMetric = _IsisIPRAMetric_Object(
    (1, 3, 6, 1, 3, 37, 1, 7, 1, 1, 8),
    _IsisIPRAMetric_Type()
)
isisIPRAMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisIPRAMetric.setStatus("current")


class _IsisIPRAMetricType_Type(MetricType):
    """Custom type isisIPRAMetricType based on MetricType"""
    defaultValue = 1


_IsisIPRAMetricType_Type.__name__ = "MetricType"
_IsisIPRAMetricType_Object = MibTableColumn
isisIPRAMetricType = _IsisIPRAMetricType_Object(
    (1, 3, 6, 1, 3, 37, 1, 7, 1, 1, 9),
    _IsisIPRAMetricType_Type()
)
isisIPRAMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisIPRAMetricType.setStatus("current")


class _IsisIPRASNPAAddress_Type(OSINSAddress):
    """Custom type isisIPRASNPAAddress based on OSINSAddress"""
    defaultHexValue = ""


_IsisIPRASNPAAddress_Type.__name__ = "OSINSAddress"
_IsisIPRASNPAAddress_Object = MibTableColumn
isisIPRASNPAAddress = _IsisIPRASNPAAddress_Object(
    (1, 3, 6, 1, 3, 37, 1, 7, 1, 1, 10),
    _IsisIPRASNPAAddress_Type()
)
isisIPRASNPAAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisIPRASNPAAddress.setStatus("current")
_IsisNotification_ObjectIdentity = ObjectIdentity
isisNotification = _IsisNotification_ObjectIdentity(
    (1, 3, 6, 1, 3, 37, 1, 8)
)
if mibBuilder.loadTexts:
    isisNotification.setStatus("current")
_IsisNotificationTable_Object = MibTable
isisNotificationTable = _IsisNotificationTable_Object(
    (1, 3, 6, 1, 3, 37, 1, 8, 1)
)
if mibBuilder.loadTexts:
    isisNotificationTable.setStatus("current")
_IsisNotificationEntry_Object = MibTableRow
isisNotificationEntry = _IsisNotificationEntry_Object(
    (1, 3, 6, 1, 3, 37, 1, 8, 1, 1)
)
isisNotificationEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
)
if mibBuilder.loadTexts:
    isisNotificationEntry.setStatus("current")
_IsisTrapLSPID_Type = LinkStatePDUID
_IsisTrapLSPID_Object = MibTableColumn
isisTrapLSPID = _IsisTrapLSPID_Object(
    (1, 3, 6, 1, 3, 37, 1, 8, 1, 1, 1),
    _IsisTrapLSPID_Type()
)
isisTrapLSPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisTrapLSPID.setStatus("current")
_IsisSystemLevel_Type = ISLevel
_IsisSystemLevel_Object = MibTableColumn
isisSystemLevel = _IsisSystemLevel_Object(
    (1, 3, 6, 1, 3, 37, 1, 8, 1, 1, 2),
    _IsisSystemLevel_Type()
)
isisSystemLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSystemLevel.setStatus("current")
_IsisPDUFragment_Type = IsisPDUHeader
_IsisPDUFragment_Object = MibTableColumn
isisPDUFragment = _IsisPDUFragment_Object(
    (1, 3, 6, 1, 3, 37, 1, 8, 1, 1, 3),
    _IsisPDUFragment_Type()
)
isisPDUFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisPDUFragment.setStatus("current")


class _IsisFieldLen_Type(Integer32):
    """Custom type isisFieldLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IsisFieldLen_Type.__name__ = "Integer32"
_IsisFieldLen_Object = MibTableColumn
isisFieldLen = _IsisFieldLen_Object(
    (1, 3, 6, 1, 3, 37, 1, 8, 1, 1, 4),
    _IsisFieldLen_Type()
)
isisFieldLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisFieldLen.setStatus("current")


class _IsisMaxAreaAddress_Type(Integer32):
    """Custom type isisMaxAreaAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IsisMaxAreaAddress_Type.__name__ = "Integer32"
_IsisMaxAreaAddress_Object = MibTableColumn
isisMaxAreaAddress = _IsisMaxAreaAddress_Object(
    (1, 3, 6, 1, 3, 37, 1, 8, 1, 1, 5),
    _IsisMaxAreaAddress_Type()
)
isisMaxAreaAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisMaxAreaAddress.setStatus("current")


class _IsisProtocolVersion_Type(Integer32):
    """Custom type isisProtocolVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IsisProtocolVersion_Type.__name__ = "Integer32"
_IsisProtocolVersion_Object = MibTableColumn
isisProtocolVersion = _IsisProtocolVersion_Object(
    (1, 3, 6, 1, 3, 37, 1, 8, 1, 1, 6),
    _IsisProtocolVersion_Type()
)
isisProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisProtocolVersion.setStatus("current")


class _IsisLSPSize_Type(Integer32):
    """Custom type isisLSPSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IsisLSPSize_Type.__name__ = "Integer32"
_IsisLSPSize_Object = MibTableColumn
isisLSPSize = _IsisLSPSize_Object(
    (1, 3, 6, 1, 3, 37, 1, 8, 1, 1, 7),
    _IsisLSPSize_Type()
)
isisLSPSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisLSPSize.setStatus("current")


class _IsisOriginatingBufferSize_Type(Integer32):
    """Custom type isisOriginatingBufferSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IsisOriginatingBufferSize_Type.__name__ = "Integer32"
_IsisOriginatingBufferSize_Object = MibTableColumn
isisOriginatingBufferSize = _IsisOriginatingBufferSize_Object(
    (1, 3, 6, 1, 3, 37, 1, 8, 1, 1, 8),
    _IsisOriginatingBufferSize_Type()
)
isisOriginatingBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisOriginatingBufferSize.setStatus("current")


class _IsisProtocolsSupported_Type(OctetString):
    """Custom type isisProtocolsSupported based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IsisProtocolsSupported_Type.__name__ = "OctetString"
_IsisProtocolsSupported_Object = MibTableColumn
isisProtocolsSupported = _IsisProtocolsSupported_Object(
    (1, 3, 6, 1, 3, 37, 1, 8, 1, 1, 9),
    _IsisProtocolsSupported_Type()
)
isisProtocolsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisProtocolsSupported.setStatus("current")
_IsisNotifications_ObjectIdentity = ObjectIdentity
isisNotifications = _IsisNotifications_ObjectIdentity(
    (1, 3, 6, 1, 3, 37, 2)
)
_IsisTrapPrefix_ObjectIdentity = ObjectIdentity
isisTrapPrefix = _IsisTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 3, 37, 2, 0)
)
_IsisConformance_ObjectIdentity = ObjectIdentity
isisConformance = _IsisConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 37, 3)
)
_IsisGroups_ObjectIdentity = ObjectIdentity
isisGroups = _IsisGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 37, 3, 1)
)
_IsisCompliances_ObjectIdentity = ObjectIdentity
isisCompliances = _IsisCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 37, 3, 2)
)

# Managed Objects groups

isisSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 37, 3, 1, 1)
)
isisSystemGroup.setObjects(
      *(("ISIS-MIB", "isisSysVersion"),
        ("ISIS-MIB", "isisSysType"),
        ("ISIS-MIB", "isisSysID"),
        ("ISIS-MIB", "isisSysMaxPathSplits"),
        ("ISIS-MIB", "isisSysMaxLSPGenInt"),
        ("ISIS-MIB", "isisSysOrigL1LSPBuffSize"),
        ("ISIS-MIB", "isisSysMaxAreaAddresses"),
        ("ISIS-MIB", "isisSysMinL1LSPGenInt"),
        ("ISIS-MIB", "isisSysMinL2LSPGenInt"),
        ("ISIS-MIB", "isisSysPollESHelloRate"),
        ("ISIS-MIB", "isisSysWaitTime"),
        ("ISIS-MIB", "isisSysAdminState"),
        ("ISIS-MIB", "isisSysL1State"),
        ("ISIS-MIB", "isisSysOrigL2LSPBuffSize"),
        ("ISIS-MIB", "isisSysL2State"),
        ("ISIS-MIB", "isisSysLogAdjacencyChanges"),
        ("ISIS-MIB", "isisSysMaxAreaCheck"),
        ("ISIS-MIB", "isisSysNextCircIndex"),
        ("ISIS-MIB", "isisSysExistState"),
        ("ISIS-MIB", "isisSysL2toL1Leaking"),
        ("ISIS-MIB", "isisSysSetOverload"),
        ("ISIS-MIB", "isisSysL1MetricStyle"),
        ("ISIS-MIB", "isisSysL1SPFConsiders"),
        ("ISIS-MIB", "isisSysL2MetricStyle"),
        ("ISIS-MIB", "isisSysL2SPFConsiders"),
        ("ISIS-MIB", "isisSysTEEnabled"),
        ("ISIS-MIB", "isisSysMaxAge"),
        ("ISIS-MIB", "isisSysReceiveLSPBufferSize"),
        ("ISIS-MIB", "isisManAreaAddrExistState"),
        ("ISIS-MIB", "isisAreaAddr"),
        ("ISIS-MIB", "isisSysProtSuppExistState"),
        ("ISIS-MIB", "isisSummAddrExistState"),
        ("ISIS-MIB", "isisSummAddrAdminState"),
        ("ISIS-MIB", "isisSummAddrMetric"),
        ("ISIS-MIB", "isisSysStatCorrLSPs"),
        ("ISIS-MIB", "isisSysStatLSPDbaseOloads"),
        ("ISIS-MIB", "isisSysStatManAddrDropFromAreas"),
        ("ISIS-MIB", "isisSysStatAttmptToExMaxSeqNums"),
        ("ISIS-MIB", "isisSysStatSeqNumSkips"),
        ("ISIS-MIB", "isisSysStatOwnLSPPurges"),
        ("ISIS-MIB", "isisSysStatIDFieldLenMismatches"),
        ("ISIS-MIB", "isisSysStatMaxAreaAddrMismatches"),
        ("ISIS-MIB", "isisSysStatPartChanges"),
        ("ISIS-MIB", "isisSysStatAuthTypeFails"),
        ("ISIS-MIB", "isisSysStatAuthFails"))
)
if mibBuilder.loadTexts:
    isisSystemGroup.setStatus("current")

isisCircuitGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 37, 3, 1, 2)
)
isisCircuitGroup.setObjects(
      *(("ISIS-MIB", "isisCircIfSubIndex"),
        ("ISIS-MIB", "isisCircLocalID"),
        ("ISIS-MIB", "isisCircAdminState"),
        ("ISIS-MIB", "isisCircExistState"),
        ("ISIS-MIB", "isisCircType"),
        ("ISIS-MIB", "isisCircExtDomain"),
        ("ISIS-MIB", "isisCircAdjChanges"),
        ("ISIS-MIB", "isisCircInitFails"),
        ("ISIS-MIB", "isisCircRejAdjs"),
        ("ISIS-MIB", "isisCircOutCtrlPDUs"),
        ("ISIS-MIB", "isisCircInCtrlPDUs"),
        ("ISIS-MIB", "isisCircIDFieldLenMismatches"),
        ("ISIS-MIB", "isisCircLevel"),
        ("ISIS-MIB", "isisCircMCAddr"),
        ("ISIS-MIB", "isisCircPtToPtCircID"),
        ("ISIS-MIB", "isisCircPassiveCircuit"),
        ("ISIS-MIB", "isisCircMeshGroupEnabled"),
        ("ISIS-MIB", "isisCircMeshGroup"),
        ("ISIS-MIB", "isisCircSmallHellos"),
        ("ISIS-MIB", "isisCircUpTime"),
        ("ISIS-MIB", "isisCircIfIndex"),
        ("ISIS-MIB", "isisCircLevelMetric"),
        ("ISIS-MIB", "isisCircLevelISPriority"),
        ("ISIS-MIB", "isisCircLevelDesIS"),
        ("ISIS-MIB", "isisCircLevelLANDesISChanges"),
        ("ISIS-MIB", "isisCircLevelHelloMultiplier"),
        ("ISIS-MIB", "isisCircLevelHelloTimer"),
        ("ISIS-MIB", "isisCircLevelDRHelloTimer"),
        ("ISIS-MIB", "isisCircLevelLSPThrottle"),
        ("ISIS-MIB", "isisCircLevelMinLSPRetransInt"),
        ("ISIS-MIB", "isisCircLevelCSNPInterval"),
        ("ISIS-MIB", "isisCircLevelPartSNPInterval"))
)
if mibBuilder.loadTexts:
    isisCircuitGroup.setStatus("current")

isisISAdjGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 37, 3, 1, 3)
)
isisISAdjGroup.setObjects(
      *(("ISIS-MIB", "isisISAdjState"),
        ("ISIS-MIB", "isisISAdjNeighSNPAAddress"),
        ("ISIS-MIB", "isisISAdjNeighSysType"),
        ("ISIS-MIB", "isisISAdjNeighSysID"),
        ("ISIS-MIB", "isisISAdjUsage"),
        ("ISIS-MIB", "isisISAdjHoldTimer"),
        ("ISIS-MIB", "isisISAdjNeighPriority"),
        ("ISIS-MIB", "isisISAdjUpTime"),
        ("ISIS-MIB", "isisISAdjAreaAddress"),
        ("ISIS-MIB", "isisISAdjIPAddressType"),
        ("ISIS-MIB", "isisISAdjIPAddress"),
        ("ISIS-MIB", "isisISAdjProtSuppProtocol"))
)
if mibBuilder.loadTexts:
    isisISAdjGroup.setStatus("current")

isisNotificationObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 37, 3, 1, 4)
)
isisNotificationObjectGroup.setObjects(
      *(("ISIS-MIB", "isisSystemLevel"),
        ("ISIS-MIB", "isisTrapLSPID"),
        ("ISIS-MIB", "isisPDUFragment"),
        ("ISIS-MIB", "isisFieldLen"),
        ("ISIS-MIB", "isisMaxAreaAddress"),
        ("ISIS-MIB", "isisProtocolVersion"),
        ("ISIS-MIB", "isisLSPSize"),
        ("ISIS-MIB", "isisOriginatingBufferSize"),
        ("ISIS-MIB", "isisProtocolsSupported"))
)
if mibBuilder.loadTexts:
    isisNotificationObjectGroup.setStatus("current")

isisISPDUCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 37, 3, 1, 6)
)
isisISPDUCounterGroup.setObjects(
      *(("ISIS-MIB", "isisPacketCountHello"),
        ("ISIS-MIB", "isisPacketCountLSP"),
        ("ISIS-MIB", "isisPacketCountCSNP"),
        ("ISIS-MIB", "isisPacketCountPSNP"))
)
if mibBuilder.loadTexts:
    isisISPDUCounterGroup.setStatus("current")

isisISIPRADestGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 37, 3, 1, 8)
)
isisISIPRADestGroup.setObjects(
      *(("ISIS-MIB", "isisIPRADestType"),
        ("ISIS-MIB", "isisIPRADest"),
        ("ISIS-MIB", "isisIPRADestPrefixLen"),
        ("ISIS-MIB", "isisIPRAExistState"),
        ("ISIS-MIB", "isisIPRAAdminState"),
        ("ISIS-MIB", "isisIPRAMetric"),
        ("ISIS-MIB", "isisIPRAMetricType"),
        ("ISIS-MIB", "isisIPRASNPAAddress"))
)
if mibBuilder.loadTexts:
    isisISIPRADestGroup.setStatus("current")


# Notification objects

isisDatabaseOverload = NotificationType(
    (1, 3, 6, 1, 3, 37, 2, 0, 1)
)
isisDatabaseOverload.setObjects(
      *(("ISIS-MIB", "isisSystemLevel"),
        ("ISIS-MIB", "isisSysL1State"),
        ("ISIS-MIB", "isisSysL2State"))
)
if mibBuilder.loadTexts:
    isisDatabaseOverload.setStatus(
        "current"
    )

isisManualAddressDrops = NotificationType(
    (1, 3, 6, 1, 3, 37, 2, 0, 2)
)
isisManualAddressDrops.setObjects(
    ("ISIS-MIB", "isisManAreaAddrExistState")
)
if mibBuilder.loadTexts:
    isisManualAddressDrops.setStatus(
        "current"
    )

isisCorruptedLSPDetected = NotificationType(
    (1, 3, 6, 1, 3, 37, 2, 0, 3)
)
isisCorruptedLSPDetected.setObjects(
      *(("ISIS-MIB", "isisSystemLevel"),
        ("ISIS-MIB", "isisTrapLSPID"))
)
if mibBuilder.loadTexts:
    isisCorruptedLSPDetected.setStatus(
        "current"
    )

isisAttemptToExceedMaxSequence = NotificationType(
    (1, 3, 6, 1, 3, 37, 2, 0, 4)
)
isisAttemptToExceedMaxSequence.setObjects(
      *(("ISIS-MIB", "isisSystemLevel"),
        ("ISIS-MIB", "isisTrapLSPID"))
)
if mibBuilder.loadTexts:
    isisAttemptToExceedMaxSequence.setStatus(
        "current"
    )

isisIDLenMismatch = NotificationType(
    (1, 3, 6, 1, 3, 37, 2, 0, 5)
)
isisIDLenMismatch.setObjects(
      *(("ISIS-MIB", "isisFieldLen"),
        ("ISIS-MIB", "isisCircIfIndex"),
        ("ISIS-MIB", "isisPDUFragment"))
)
if mibBuilder.loadTexts:
    isisIDLenMismatch.setStatus(
        "current"
    )

isisMaxAreaAddressesMismatch = NotificationType(
    (1, 3, 6, 1, 3, 37, 2, 0, 6)
)
isisMaxAreaAddressesMismatch.setObjects(
      *(("ISIS-MIB", "isisMaxAreaAddress"),
        ("ISIS-MIB", "isisCircIfIndex"),
        ("ISIS-MIB", "isisPDUFragment"))
)
if mibBuilder.loadTexts:
    isisMaxAreaAddressesMismatch.setStatus(
        "current"
    )

isisOwnLSPPurge = NotificationType(
    (1, 3, 6, 1, 3, 37, 2, 0, 7)
)
isisOwnLSPPurge.setObjects(
      *(("ISIS-MIB", "isisCircIfIndex"),
        ("ISIS-MIB", "isisTrapLSPID"),
        ("ISIS-MIB", "isisSystemLevel"))
)
if mibBuilder.loadTexts:
    isisOwnLSPPurge.setStatus(
        "current"
    )

isisSequenceNumberSkip = NotificationType(
    (1, 3, 6, 1, 3, 37, 2, 0, 8)
)
isisSequenceNumberSkip.setObjects(
      *(("ISIS-MIB", "isisTrapLSPID"),
        ("ISIS-MIB", "isisCircIfIndex"),
        ("ISIS-MIB", "isisSystemLevel"))
)
if mibBuilder.loadTexts:
    isisSequenceNumberSkip.setStatus(
        "current"
    )

isisAuthenticationTypeFailure = NotificationType(
    (1, 3, 6, 1, 3, 37, 2, 0, 9)
)
isisAuthenticationTypeFailure.setObjects(
      *(("ISIS-MIB", "isisSystemLevel"),
        ("ISIS-MIB", "isisPDUFragment"),
        ("ISIS-MIB", "isisCircIfIndex"))
)
if mibBuilder.loadTexts:
    isisAuthenticationTypeFailure.setStatus(
        "current"
    )

isisAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 3, 37, 2, 0, 10)
)
isisAuthenticationFailure.setObjects(
      *(("ISIS-MIB", "isisSystemLevel"),
        ("ISIS-MIB", "isisPDUFragment"),
        ("ISIS-MIB", "isisCircIfIndex"))
)
if mibBuilder.loadTexts:
    isisAuthenticationFailure.setStatus(
        "current"
    )

isisVersionSkew = NotificationType(
    (1, 3, 6, 1, 3, 37, 2, 0, 11)
)
isisVersionSkew.setObjects(
      *(("ISIS-MIB", "isisProtocolVersion"),
        ("ISIS-MIB", "isisSystemLevel"),
        ("ISIS-MIB", "isisPDUFragment"),
        ("ISIS-MIB", "isisCircIfIndex"))
)
if mibBuilder.loadTexts:
    isisVersionSkew.setStatus(
        "current"
    )

isisAreaMismatch = NotificationType(
    (1, 3, 6, 1, 3, 37, 2, 0, 12)
)
isisAreaMismatch.setObjects(
      *(("ISIS-MIB", "isisLSPSize"),
        ("ISIS-MIB", "isisSystemLevel"),
        ("ISIS-MIB", "isisCircIfIndex"),
        ("ISIS-MIB", "isisPDUFragment"))
)
if mibBuilder.loadTexts:
    isisAreaMismatch.setStatus(
        "current"
    )

isisRejectedAdjacency = NotificationType(
    (1, 3, 6, 1, 3, 37, 2, 0, 13)
)
isisRejectedAdjacency.setObjects(
      *(("ISIS-MIB", "isisSystemLevel"),
        ("ISIS-MIB", "isisCircIfIndex"))
)
if mibBuilder.loadTexts:
    isisRejectedAdjacency.setStatus(
        "current"
    )

isisLSPTooLargeToPropagate = NotificationType(
    (1, 3, 6, 1, 3, 37, 2, 0, 14)
)
isisLSPTooLargeToPropagate.setObjects(
      *(("ISIS-MIB", "isisLSPSize"),
        ("ISIS-MIB", "isisSystemLevel"),
        ("ISIS-MIB", "isisTrapLSPID"),
        ("ISIS-MIB", "isisCircIfIndex"))
)
if mibBuilder.loadTexts:
    isisLSPTooLargeToPropagate.setStatus(
        "current"
    )

isisOriginatingLSPBufferSizeMismatch = NotificationType(
    (1, 3, 6, 1, 3, 37, 2, 0, 15)
)
isisOriginatingLSPBufferSizeMismatch.setObjects(
      *(("ISIS-MIB", "isisOriginatingBufferSize"),
        ("ISIS-MIB", "isisSystemLevel"),
        ("ISIS-MIB", "isisTrapLSPID"),
        ("ISIS-MIB", "isisCircIfIndex"))
)
if mibBuilder.loadTexts:
    isisOriginatingLSPBufferSizeMismatch.setStatus(
        "current"
    )

isisProtocolsSupportedMismatch = NotificationType(
    (1, 3, 6, 1, 3, 37, 2, 0, 16)
)
isisProtocolsSupportedMismatch.setObjects(
      *(("ISIS-MIB", "isisProtocolsSupported"),
        ("ISIS-MIB", "isisSystemLevel"),
        ("ISIS-MIB", "isisTrapLSPID"),
        ("ISIS-MIB", "isisCircIfIndex"))
)
if mibBuilder.loadTexts:
    isisProtocolsSupportedMismatch.setStatus(
        "current"
    )


# Notifications groups

isisNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 3, 37, 3, 1, 5)
)
isisNotificationGroup.setObjects(
      *(("ISIS-MIB", "isisDatabaseOverload"),
        ("ISIS-MIB", "isisManualAddressDrops"),
        ("ISIS-MIB", "isisCorruptedLSPDetected"),
        ("ISIS-MIB", "isisAttemptToExceedMaxSequence"),
        ("ISIS-MIB", "isisIDLenMismatch"),
        ("ISIS-MIB", "isisMaxAreaAddressesMismatch"),
        ("ISIS-MIB", "isisOwnLSPPurge"),
        ("ISIS-MIB", "isisSequenceNumberSkip"),
        ("ISIS-MIB", "isisAuthenticationTypeFailure"),
        ("ISIS-MIB", "isisAuthenticationFailure"),
        ("ISIS-MIB", "isisVersionSkew"),
        ("ISIS-MIB", "isisAreaMismatch"),
        ("ISIS-MIB", "isisRejectedAdjacency"),
        ("ISIS-MIB", "isisLSPTooLargeToPropagate"),
        ("ISIS-MIB", "isisOriginatingLSPBufferSizeMismatch"),
        ("ISIS-MIB", "isisProtocolsSupportedMismatch"))
)
if mibBuilder.loadTexts:
    isisNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

isisCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 37, 3, 2, 1)
)
isisCompliance.setObjects(
      *(("ISIS-MIB", "isisSystemGroup"),
        ("ISIS-MIB", "isisCircuitGroup"),
        ("ISIS-MIB", "isisISAdjGroup"),
        ("ISIS-MIB", "isisNotificationObjectGroup"),
        ("ISIS-MIB", "isisISPDUCounterGroup"),
        ("ISIS-MIB", "isisISIPRADestGroup"),
        ("ISIS-MIB", "isisNotificationGroup"))
)
if mibBuilder.loadTexts:
    isisCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ISIS-MIB",
    **{"OSINSAddress": OSINSAddress,
       "SystemID": SystemID,
       "LinkStatePDUID": LinkStatePDUID,
       "AdminState": AdminState,
       "UpTime": UpTime,
       "LSPBuffSize": LSPBuffSize,
       "LevelState": LevelState,
       "SupportedProtocol": SupportedProtocol,
       "DefaultMetric": DefaultMetric,
       "MetricType": MetricType,
       "MetricStyle": MetricStyle,
       "ISLevel": ISLevel,
       "IsisPDUHeader": IsisPDUHeader,
       "CircuitID": CircuitID,
       "ISPriority": ISPriority,
       "isisMIB": isisMIB,
       "isisObjects": isisObjects,
       "isisSystem": isisSystem,
       "isisSysTable": isisSysTable,
       "isisSysEntry": isisSysEntry,
       "isisSysInstance": isisSysInstance,
       "isisSysVersion": isisSysVersion,
       "isisSysType": isisSysType,
       "isisSysID": isisSysID,
       "isisSysMaxPathSplits": isisSysMaxPathSplits,
       "isisSysMaxLSPGenInt": isisSysMaxLSPGenInt,
       "isisSysOrigL1LSPBuffSize": isisSysOrigL1LSPBuffSize,
       "isisSysMaxAreaAddresses": isisSysMaxAreaAddresses,
       "isisSysMinL1LSPGenInt": isisSysMinL1LSPGenInt,
       "isisSysMinL2LSPGenInt": isisSysMinL2LSPGenInt,
       "isisSysPollESHelloRate": isisSysPollESHelloRate,
       "isisSysWaitTime": isisSysWaitTime,
       "isisSysAdminState": isisSysAdminState,
       "isisSysL1State": isisSysL1State,
       "isisSysOrigL2LSPBuffSize": isisSysOrigL2LSPBuffSize,
       "isisSysL2State": isisSysL2State,
       "isisSysLogAdjacencyChanges": isisSysLogAdjacencyChanges,
       "isisSysMaxAreaCheck": isisSysMaxAreaCheck,
       "isisSysNextCircIndex": isisSysNextCircIndex,
       "isisSysExistState": isisSysExistState,
       "isisSysL2toL1Leaking": isisSysL2toL1Leaking,
       "isisSysSetOverload": isisSysSetOverload,
       "isisSysL1MetricStyle": isisSysL1MetricStyle,
       "isisSysL1SPFConsiders": isisSysL1SPFConsiders,
       "isisSysL2MetricStyle": isisSysL2MetricStyle,
       "isisSysL2SPFConsiders": isisSysL2SPFConsiders,
       "isisSysTEEnabled": isisSysTEEnabled,
       "isisSysMaxAge": isisSysMaxAge,
       "isisSysReceiveLSPBufferSize": isisSysReceiveLSPBufferSize,
       "isisManAreaAddrTable": isisManAreaAddrTable,
       "isisManAreaAddrEntry": isisManAreaAddrEntry,
       "isisManAreaAddr": isisManAreaAddr,
       "isisManAreaAddrExistState": isisManAreaAddrExistState,
       "isisAreaAddrTable": isisAreaAddrTable,
       "isisAreaAddrEntry": isisAreaAddrEntry,
       "isisAreaAddr": isisAreaAddr,
       "isisSysProtSuppTable": isisSysProtSuppTable,
       "isisSysProtSuppEntry": isisSysProtSuppEntry,
       "isisSysProtSuppProtocol": isisSysProtSuppProtocol,
       "isisSysProtSuppExistState": isisSysProtSuppExistState,
       "isisSummAddrTable": isisSummAddrTable,
       "isisSummAddrEntry": isisSummAddrEntry,
       "isisSummAddressType": isisSummAddressType,
       "isisSummAddress": isisSummAddress,
       "isisSummAddrPrefixLen": isisSummAddrPrefixLen,
       "isisSummAddrExistState": isisSummAddrExistState,
       "isisSummAddrAdminState": isisSummAddrAdminState,
       "isisSummAddrMetric": isisSummAddrMetric,
       "isisSysStatsTable": isisSysStatsTable,
       "isisSysStatsEntry": isisSysStatsEntry,
       "isisSysStatLevel": isisSysStatLevel,
       "isisSysStatCorrLSPs": isisSysStatCorrLSPs,
       "isisSysStatAuthTypeFails": isisSysStatAuthTypeFails,
       "isisSysStatAuthFails": isisSysStatAuthFails,
       "isisSysStatLSPDbaseOloads": isisSysStatLSPDbaseOloads,
       "isisSysStatManAddrDropFromAreas": isisSysStatManAddrDropFromAreas,
       "isisSysStatAttmptToExMaxSeqNums": isisSysStatAttmptToExMaxSeqNums,
       "isisSysStatSeqNumSkips": isisSysStatSeqNumSkips,
       "isisSysStatOwnLSPPurges": isisSysStatOwnLSPPurges,
       "isisSysStatIDFieldLenMismatches": isisSysStatIDFieldLenMismatches,
       "isisSysStatMaxAreaAddrMismatches": isisSysStatMaxAreaAddrMismatches,
       "isisSysStatPartChanges": isisSysStatPartChanges,
       "isisCirc": isisCirc,
       "isisCircTable": isisCircTable,
       "isisCircEntry": isisCircEntry,
       "isisCircIndex": isisCircIndex,
       "isisCircIfIndex": isisCircIfIndex,
       "isisCircIfSubIndex": isisCircIfSubIndex,
       "isisCircLocalID": isisCircLocalID,
       "isisCircAdminState": isisCircAdminState,
       "isisCircExistState": isisCircExistState,
       "isisCircType": isisCircType,
       "isisCircExtDomain": isisCircExtDomain,
       "isisCircAdjChanges": isisCircAdjChanges,
       "isisCircInitFails": isisCircInitFails,
       "isisCircRejAdjs": isisCircRejAdjs,
       "isisCircOutCtrlPDUs": isisCircOutCtrlPDUs,
       "isisCircInCtrlPDUs": isisCircInCtrlPDUs,
       "isisCircIDFieldLenMismatches": isisCircIDFieldLenMismatches,
       "isisCircLevel": isisCircLevel,
       "isisCircMCAddr": isisCircMCAddr,
       "isisCircPtToPtCircID": isisCircPtToPtCircID,
       "isisCircPassiveCircuit": isisCircPassiveCircuit,
       "isisCircMeshGroupEnabled": isisCircMeshGroupEnabled,
       "isisCircMeshGroup": isisCircMeshGroup,
       "isisCircSmallHellos": isisCircSmallHellos,
       "isisCircUpTime": isisCircUpTime,
       "isisCircLevelValues": isisCircLevelValues,
       "isisCircLevelTable": isisCircLevelTable,
       "isisCircLevelEntry": isisCircLevelEntry,
       "isisCircLevelIndex": isisCircLevelIndex,
       "isisCircLevelMetric": isisCircLevelMetric,
       "isisCircLevelISPriority": isisCircLevelISPriority,
       "isisCircLevelDesIS": isisCircLevelDesIS,
       "isisCircLevelLANDesISChanges": isisCircLevelLANDesISChanges,
       "isisCircLevelHelloMultiplier": isisCircLevelHelloMultiplier,
       "isisCircLevelHelloTimer": isisCircLevelHelloTimer,
       "isisCircLevelDRHelloTimer": isisCircLevelDRHelloTimer,
       "isisCircLevelLSPThrottle": isisCircLevelLSPThrottle,
       "isisCircLevelMinLSPRetransInt": isisCircLevelMinLSPRetransInt,
       "isisCircLevelCSNPInterval": isisCircLevelCSNPInterval,
       "isisCircLevelPartSNPInterval": isisCircLevelPartSNPInterval,
       "isisCircPDUCounters": isisCircPDUCounters,
       "isisPacketCountTable": isisPacketCountTable,
       "isisPacketCountEntry": isisPacketCountEntry,
       "isisPacketCountLevel": isisPacketCountLevel,
       "isisPacketCountDirection": isisPacketCountDirection,
       "isisPacketCountHello": isisPacketCountHello,
       "isisPacketCountLSP": isisPacketCountLSP,
       "isisPacketCountCSNP": isisPacketCountCSNP,
       "isisPacketCountPSNP": isisPacketCountPSNP,
       "isisISAdj": isisISAdj,
       "isisISAdjTable": isisISAdjTable,
       "isisISAdjEntry": isisISAdjEntry,
       "isisISAdjIndex": isisISAdjIndex,
       "isisISAdjState": isisISAdjState,
       "isisISAdjNeighSNPAAddress": isisISAdjNeighSNPAAddress,
       "isisISAdjNeighSysType": isisISAdjNeighSysType,
       "isisISAdjNeighSysID": isisISAdjNeighSysID,
       "isisISAdjUsage": isisISAdjUsage,
       "isisISAdjHoldTimer": isisISAdjHoldTimer,
       "isisISAdjNeighPriority": isisISAdjNeighPriority,
       "isisISAdjUpTime": isisISAdjUpTime,
       "isisISAdjAreaAddrTable": isisISAdjAreaAddrTable,
       "isisISAdjAreaAddrEntry": isisISAdjAreaAddrEntry,
       "isisISAdjAreaAddrIndex": isisISAdjAreaAddrIndex,
       "isisISAdjAreaAddress": isisISAdjAreaAddress,
       "isisISAdjIPAddrTable": isisISAdjIPAddrTable,
       "isisISAdjIPAddrEntry": isisISAdjIPAddrEntry,
       "isisISAdjIPAddrIndex": isisISAdjIPAddrIndex,
       "isisISAdjIPAddressType": isisISAdjIPAddressType,
       "isisISAdjIPAddress": isisISAdjIPAddress,
       "isisISAdjProtSuppTable": isisISAdjProtSuppTable,
       "isisISAdjProtSuppEntry": isisISAdjProtSuppEntry,
       "isisISAdjProtSuppIndex": isisISAdjProtSuppIndex,
       "isisISAdjProtSuppProtocol": isisISAdjProtSuppProtocol,
       "isisReachAddr": isisReachAddr,
       "isisIPReachAddr": isisIPReachAddr,
       "isisIPRATable": isisIPRATable,
       "isisIPRAEntry": isisIPRAEntry,
       "isisIPRAIndex": isisIPRAIndex,
       "isisIPRAType": isisIPRAType,
       "isisIPRADestType": isisIPRADestType,
       "isisIPRADest": isisIPRADest,
       "isisIPRADestPrefixLen": isisIPRADestPrefixLen,
       "isisIPRAExistState": isisIPRAExistState,
       "isisIPRAAdminState": isisIPRAAdminState,
       "isisIPRAMetric": isisIPRAMetric,
       "isisIPRAMetricType": isisIPRAMetricType,
       "isisIPRASNPAAddress": isisIPRASNPAAddress,
       "isisNotification": isisNotification,
       "isisNotificationTable": isisNotificationTable,
       "isisNotificationEntry": isisNotificationEntry,
       "isisTrapLSPID": isisTrapLSPID,
       "isisSystemLevel": isisSystemLevel,
       "isisPDUFragment": isisPDUFragment,
       "isisFieldLen": isisFieldLen,
       "isisMaxAreaAddress": isisMaxAreaAddress,
       "isisProtocolVersion": isisProtocolVersion,
       "isisLSPSize": isisLSPSize,
       "isisOriginatingBufferSize": isisOriginatingBufferSize,
       "isisProtocolsSupported": isisProtocolsSupported,
       "isisNotifications": isisNotifications,
       "isisTrapPrefix": isisTrapPrefix,
       "isisDatabaseOverload": isisDatabaseOverload,
       "isisManualAddressDrops": isisManualAddressDrops,
       "isisCorruptedLSPDetected": isisCorruptedLSPDetected,
       "isisAttemptToExceedMaxSequence": isisAttemptToExceedMaxSequence,
       "isisIDLenMismatch": isisIDLenMismatch,
       "isisMaxAreaAddressesMismatch": isisMaxAreaAddressesMismatch,
       "isisOwnLSPPurge": isisOwnLSPPurge,
       "isisSequenceNumberSkip": isisSequenceNumberSkip,
       "isisAuthenticationTypeFailure": isisAuthenticationTypeFailure,
       "isisAuthenticationFailure": isisAuthenticationFailure,
       "isisVersionSkew": isisVersionSkew,
       "isisAreaMismatch": isisAreaMismatch,
       "isisRejectedAdjacency": isisRejectedAdjacency,
       "isisLSPTooLargeToPropagate": isisLSPTooLargeToPropagate,
       "isisOriginatingLSPBufferSizeMismatch": isisOriginatingLSPBufferSizeMismatch,
       "isisProtocolsSupportedMismatch": isisProtocolsSupportedMismatch,
       "isisConformance": isisConformance,
       "isisGroups": isisGroups,
       "isisSystemGroup": isisSystemGroup,
       "isisCircuitGroup": isisCircuitGroup,
       "isisISAdjGroup": isisISAdjGroup,
       "isisNotificationObjectGroup": isisNotificationObjectGroup,
       "isisNotificationGroup": isisNotificationGroup,
       "isisISPDUCounterGroup": isisISPDUCounterGroup,
       "isisISIPRADestGroup": isisISIPRADestGroup,
       "isisCompliances": isisCompliances,
       "isisCompliance": isisCompliance}
)
