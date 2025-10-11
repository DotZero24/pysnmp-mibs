# SNMP MIB module (SUPERMICRO-PTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-PTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:04:15 2025
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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

fsPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45)
)
if mibBuilder.loadTexts:
    fsPtpMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FsPtpPortNumber(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"


# MIB Managed Objects in the order of their OIDs

_FsPtpObjects_ObjectIdentity = ObjectIdentity
fsPtpObjects = _FsPtpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1)
)
_FsPtpGeneralGroup_ObjectIdentity = ObjectIdentity
fsPtpGeneralGroup = _FsPtpGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 1)
)


class _FsPtpGlobalSysCtrl_Type(Integer32):
    """Custom type fsPtpGlobalSysCtrl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("shutdown", 2))
    )


_FsPtpGlobalSysCtrl_Type.__name__ = "Integer32"
_FsPtpGlobalSysCtrl_Object = MibScalar
fsPtpGlobalSysCtrl = _FsPtpGlobalSysCtrl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 1, 1),
    _FsPtpGlobalSysCtrl_Type()
)
fsPtpGlobalSysCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpGlobalSysCtrl.setStatus("current")


class _FsPtpGblTraceOption_Type(DisplayString):
    """Custom type fsPtpGblTraceOption based on DisplayString"""
    defaultValue = OctetString("critical")


_FsPtpGblTraceOption_Type.__name__ = "DisplayString"
_FsPtpGblTraceOption_Object = MibScalar
fsPtpGblTraceOption = _FsPtpGblTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 1, 2),
    _FsPtpGblTraceOption_Type()
)
fsPtpGblTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpGblTraceOption.setStatus("current")


class _FsPtpPrimaryContext_Type(Integer32):
    """Custom type fsPtpPrimaryContext based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsPtpPrimaryContext_Type.__name__ = "Integer32"
_FsPtpPrimaryContext_Object = MibScalar
fsPtpPrimaryContext = _FsPtpPrimaryContext_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 1, 3),
    _FsPtpPrimaryContext_Type()
)
fsPtpPrimaryContext.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpPrimaryContext.setStatus("current")
_FsPtpTable_Object = MibTable
fsPtpTable = _FsPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 1, 4)
)
if mibBuilder.loadTexts:
    fsPtpTable.setStatus("current")
_FsPtpEntry_Object = MibTableRow
fsPtpEntry = _FsPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 1, 4, 1)
)
fsPtpEntry.setIndexNames(
    (0, "SUPERMICRO-PTP-MIB", "fsPtpContextId"),
)
if mibBuilder.loadTexts:
    fsPtpEntry.setStatus("current")


class _FsPtpContextId_Type(Integer32):
    """Custom type fsPtpContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsPtpContextId_Type.__name__ = "Integer32"
_FsPtpContextId_Object = MibTableColumn
fsPtpContextId = _FsPtpContextId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 1, 4, 1, 1),
    _FsPtpContextId_Type()
)
fsPtpContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPtpContextId.setStatus("current")


class _FsPtpAdminStatus_Type(Integer32):
    """Custom type fsPtpAdminStatus based on Integer32"""
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


_FsPtpAdminStatus_Type.__name__ = "Integer32"
_FsPtpAdminStatus_Object = MibTableColumn
fsPtpAdminStatus = _FsPtpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 1, 4, 1, 2),
    _FsPtpAdminStatus_Type()
)
fsPtpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpAdminStatus.setStatus("current")


class _FsPtpTraceOption_Type(DisplayString):
    """Custom type fsPtpTraceOption based on DisplayString"""
    defaultValue = OctetString("critical")


_FsPtpTraceOption_Type.__name__ = "DisplayString"
_FsPtpTraceOption_Object = MibTableColumn
fsPtpTraceOption = _FsPtpTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 1, 4, 1, 3),
    _FsPtpTraceOption_Type()
)
fsPtpTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpTraceOption.setStatus("current")


class _FsPtpContextType_Type(Integer32):
    """Custom type fsPtpContextType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("l2Context", 1),
          ("l3Context", 2),
          ("l2Andl3Context", 3))
    )


_FsPtpContextType_Type.__name__ = "Integer32"
_FsPtpContextType_Object = MibTableColumn
fsPtpContextType = _FsPtpContextType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 1, 4, 1, 4),
    _FsPtpContextType_Type()
)
fsPtpContextType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpContextType.setStatus("current")


class _FsPtpPrimaryDomain_Type(Integer32):
    """Custom type fsPtpPrimaryDomain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsPtpPrimaryDomain_Type.__name__ = "Integer32"
_FsPtpPrimaryDomain_Object = MibTableColumn
fsPtpPrimaryDomain = _FsPtpPrimaryDomain_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 1, 4, 1, 5),
    _FsPtpPrimaryDomain_Type()
)
fsPtpPrimaryDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpPrimaryDomain.setStatus("current")
_FsPtpContextRowStatus_Type = RowStatus
_FsPtpContextRowStatus_Object = MibTableColumn
fsPtpContextRowStatus = _FsPtpContextRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 1, 4, 1, 6),
    _FsPtpContextRowStatus_Type()
)
fsPtpContextRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPtpContextRowStatus.setStatus("current")
_FsPtpDomainDataSet_ObjectIdentity = ObjectIdentity
fsPtpDomainDataSet = _FsPtpDomainDataSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 2)
)
_FsPtpDomainDataSetTable_Object = MibTable
fsPtpDomainDataSetTable = _FsPtpDomainDataSetTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fsPtpDomainDataSetTable.setStatus("current")
_FsPtpDomainDataSetEntry_Object = MibTableRow
fsPtpDomainDataSetEntry = _FsPtpDomainDataSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 2, 1, 1)
)
fsPtpDomainDataSetEntry.setIndexNames(
    (0, "SUPERMICRO-PTP-MIB", "fsPtpContextId"),
    (0, "SUPERMICRO-PTP-MIB", "fsPtpDomainNumber"),
)
if mibBuilder.loadTexts:
    fsPtpDomainDataSetEntry.setStatus("current")


class _FsPtpDomainNumber_Type(Integer32):
    """Custom type fsPtpDomainNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsPtpDomainNumber_Type.__name__ = "Integer32"
_FsPtpDomainNumber_Object = MibTableColumn
fsPtpDomainNumber = _FsPtpDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 2, 1, 1, 1),
    _FsPtpDomainNumber_Type()
)
fsPtpDomainNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPtpDomainNumber.setStatus("current")


class _FsPtpDomainClockMode_Type(Integer32):
    """Custom type fsPtpDomainClockMode based on Integer32"""
    defaultValue = 4

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
        *(("boundary", 1),
          ("ordinary", 2),
          ("transparent", 3),
          ("forward", 4),
          ("management", 5))
    )


_FsPtpDomainClockMode_Type.__name__ = "Integer32"
_FsPtpDomainClockMode_Object = MibTableColumn
fsPtpDomainClockMode = _FsPtpDomainClockMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 2, 1, 1, 2),
    _FsPtpDomainClockMode_Type()
)
fsPtpDomainClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpDomainClockMode.setStatus("current")


class _FsPtpDomainClockIdentity_Type(OctetString):
    """Custom type fsPtpDomainClockIdentity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FsPtpDomainClockIdentity_Type.__name__ = "OctetString"
_FsPtpDomainClockIdentity_Object = MibTableColumn
fsPtpDomainClockIdentity = _FsPtpDomainClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 2, 1, 1, 3),
    _FsPtpDomainClockIdentity_Type()
)
fsPtpDomainClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpDomainClockIdentity.setStatus("current")
_FsPtpDomainGMClusterQueryInterval_Type = Integer32
_FsPtpDomainGMClusterQueryInterval_Object = MibTableColumn
fsPtpDomainGMClusterQueryInterval = _FsPtpDomainGMClusterQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 2, 1, 1, 4),
    _FsPtpDomainGMClusterQueryInterval_Type()
)
fsPtpDomainGMClusterQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpDomainGMClusterQueryInterval.setStatus("current")
_FsPtpDomainRowStatus_Type = RowStatus
_FsPtpDomainRowStatus_Object = MibTableColumn
fsPtpDomainRowStatus = _FsPtpDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 2, 1, 1, 5),
    _FsPtpDomainRowStatus_Type()
)
fsPtpDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPtpDomainRowStatus.setStatus("current")
_FsPtpDefaultDataSet_ObjectIdentity = ObjectIdentity
fsPtpDefaultDataSet = _FsPtpDefaultDataSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 3)
)
_FsPtpClockDataSetTable_Object = MibTable
fsPtpClockDataSetTable = _FsPtpClockDataSetTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 3, 1)
)
if mibBuilder.loadTexts:
    fsPtpClockDataSetTable.setStatus("current")
_FsPtpClockDataSetEntry_Object = MibTableRow
fsPtpClockDataSetEntry = _FsPtpClockDataSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    fsPtpClockDataSetEntry.setStatus("current")


class _FsPtpClockIdentity_Type(OctetString):
    """Custom type fsPtpClockIdentity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FsPtpClockIdentity_Type.__name__ = "OctetString"
_FsPtpClockIdentity_Object = MibTableColumn
fsPtpClockIdentity = _FsPtpClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 3, 1, 1, 1),
    _FsPtpClockIdentity_Type()
)
fsPtpClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpClockIdentity.setStatus("current")


class _FsPtpClockTwoStepFlag_Type(TruthValue):
    """Custom type fsPtpClockTwoStepFlag based on TruthValue"""
    defaultValue = 2


_FsPtpClockTwoStepFlag_Type.__name__ = "TruthValue"
_FsPtpClockTwoStepFlag_Object = MibTableColumn
fsPtpClockTwoStepFlag = _FsPtpClockTwoStepFlag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 3, 1, 1, 2),
    _FsPtpClockTwoStepFlag_Type()
)
fsPtpClockTwoStepFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpClockTwoStepFlag.setStatus("current")


class _FsPtpClockNumberPorts_Type(Integer32):
    """Custom type fsPtpClockNumberPorts based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_FsPtpClockNumberPorts_Type.__name__ = "Integer32"
_FsPtpClockNumberPorts_Object = MibTableColumn
fsPtpClockNumberPorts = _FsPtpClockNumberPorts_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 3, 1, 1, 3),
    _FsPtpClockNumberPorts_Type()
)
fsPtpClockNumberPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpClockNumberPorts.setStatus("current")


class _FsPtpClockClass_Type(Integer32):
    """Custom type fsPtpClockClass based on Integer32"""
    defaultValue = 248

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsPtpClockClass_Type.__name__ = "Integer32"
_FsPtpClockClass_Object = MibTableColumn
fsPtpClockClass = _FsPtpClockClass_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 3, 1, 1, 4),
    _FsPtpClockClass_Type()
)
fsPtpClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpClockClass.setStatus("current")


class _FsPtpClockAccuracy_Type(Integer32):
    """Custom type fsPtpClockAccuracy based on Integer32"""
    defaultValue = 254

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsPtpClockAccuracy_Type.__name__ = "Integer32"
_FsPtpClockAccuracy_Object = MibTableColumn
fsPtpClockAccuracy = _FsPtpClockAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 3, 1, 1, 5),
    _FsPtpClockAccuracy_Type()
)
fsPtpClockAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpClockAccuracy.setStatus("current")


class _FsPtpClockOffsetScaledLogVariance_Type(Integer32):
    """Custom type fsPtpClockOffsetScaledLogVariance based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsPtpClockOffsetScaledLogVariance_Type.__name__ = "Integer32"
_FsPtpClockOffsetScaledLogVariance_Object = MibTableColumn
fsPtpClockOffsetScaledLogVariance = _FsPtpClockOffsetScaledLogVariance_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 3, 1, 1, 6),
    _FsPtpClockOffsetScaledLogVariance_Type()
)
fsPtpClockOffsetScaledLogVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpClockOffsetScaledLogVariance.setStatus("current")


class _FsPtpClockPriority1_Type(Integer32):
    """Custom type fsPtpClockPriority1 based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsPtpClockPriority1_Type.__name__ = "Integer32"
_FsPtpClockPriority1_Object = MibTableColumn
fsPtpClockPriority1 = _FsPtpClockPriority1_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 3, 1, 1, 7),
    _FsPtpClockPriority1_Type()
)
fsPtpClockPriority1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpClockPriority1.setStatus("current")


class _FsPtpClockPriority2_Type(Integer32):
    """Custom type fsPtpClockPriority2 based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsPtpClockPriority2_Type.__name__ = "Integer32"
_FsPtpClockPriority2_Object = MibTableColumn
fsPtpClockPriority2 = _FsPtpClockPriority2_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 3, 1, 1, 8),
    _FsPtpClockPriority2_Type()
)
fsPtpClockPriority2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpClockPriority2.setStatus("current")


class _FsPtpClockSlaveOnly_Type(TruthValue):
    """Custom type fsPtpClockSlaveOnly based on TruthValue"""
    defaultValue = 2


_FsPtpClockSlaveOnly_Type.__name__ = "TruthValue"
_FsPtpClockSlaveOnly_Object = MibTableColumn
fsPtpClockSlaveOnly = _FsPtpClockSlaveOnly_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 3, 1, 1, 9),
    _FsPtpClockSlaveOnly_Type()
)
fsPtpClockSlaveOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpClockSlaveOnly.setStatus("current")


class _FsPtpClockPathTraceOption_Type(TruthValue):
    """Custom type fsPtpClockPathTraceOption based on TruthValue"""
    defaultValue = 2


_FsPtpClockPathTraceOption_Type.__name__ = "TruthValue"
_FsPtpClockPathTraceOption_Object = MibTableColumn
fsPtpClockPathTraceOption = _FsPtpClockPathTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 3, 1, 1, 10),
    _FsPtpClockPathTraceOption_Type()
)
fsPtpClockPathTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpClockPathTraceOption.setStatus("current")


class _FsPtpClockAccMasterMaxSize_Type(Integer32):
    """Custom type fsPtpClockAccMasterMaxSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsPtpClockAccMasterMaxSize_Type.__name__ = "Integer32"
_FsPtpClockAccMasterMaxSize_Object = MibTableColumn
fsPtpClockAccMasterMaxSize = _FsPtpClockAccMasterMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 3, 1, 1, 11),
    _FsPtpClockAccMasterMaxSize_Type()
)
fsPtpClockAccMasterMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpClockAccMasterMaxSize.setStatus("current")


class _FsPtpClockSecurityEnabled_Type(TruthValue):
    """Custom type fsPtpClockSecurityEnabled based on TruthValue"""
    defaultValue = 2


_FsPtpClockSecurityEnabled_Type.__name__ = "TruthValue"
_FsPtpClockSecurityEnabled_Object = MibTableColumn
fsPtpClockSecurityEnabled = _FsPtpClockSecurityEnabled_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 3, 1, 1, 12),
    _FsPtpClockSecurityEnabled_Type()
)
fsPtpClockSecurityEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpClockSecurityEnabled.setStatus("current")


class _FsPtpClockNumOfSA_Type(Unsigned32):
    """Custom type fsPtpClockNumOfSA based on Unsigned32"""
    defaultValue = 128


_FsPtpClockNumOfSA_Type.__name__ = "Unsigned32"
_FsPtpClockNumOfSA_Object = MibTableColumn
fsPtpClockNumOfSA = _FsPtpClockNumOfSA_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 3, 1, 1, 13),
    _FsPtpClockNumOfSA_Type()
)
fsPtpClockNumOfSA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpClockNumOfSA.setStatus("current")
_FsPtpCurrentDataSet_ObjectIdentity = ObjectIdentity
fsPtpCurrentDataSet = _FsPtpCurrentDataSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 4)
)
_FsPtpCurrentDataSetTable_Object = MibTable
fsPtpCurrentDataSetTable = _FsPtpCurrentDataSetTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 4, 1)
)
if mibBuilder.loadTexts:
    fsPtpCurrentDataSetTable.setStatus("current")
_FsPtpCurrentDataSetEntry_Object = MibTableRow
fsPtpCurrentDataSetEntry = _FsPtpCurrentDataSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    fsPtpCurrentDataSetEntry.setStatus("current")
_FsPtpCurrentStepsRemoved_Type = Integer32
_FsPtpCurrentStepsRemoved_Object = MibTableColumn
fsPtpCurrentStepsRemoved = _FsPtpCurrentStepsRemoved_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 4, 1, 1, 1),
    _FsPtpCurrentStepsRemoved_Type()
)
fsPtpCurrentStepsRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpCurrentStepsRemoved.setStatus("current")
_FsPtpCurrentOffsetFromMaster_Type = DisplayString
_FsPtpCurrentOffsetFromMaster_Object = MibTableColumn
fsPtpCurrentOffsetFromMaster = _FsPtpCurrentOffsetFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 4, 1, 1, 2),
    _FsPtpCurrentOffsetFromMaster_Type()
)
fsPtpCurrentOffsetFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpCurrentOffsetFromMaster.setStatus("current")
_FsPtpCurrentMeanPathDelay_Type = DisplayString
_FsPtpCurrentMeanPathDelay_Object = MibTableColumn
fsPtpCurrentMeanPathDelay = _FsPtpCurrentMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 4, 1, 1, 3),
    _FsPtpCurrentMeanPathDelay_Type()
)
fsPtpCurrentMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpCurrentMeanPathDelay.setStatus("current")
_FsPtpCurrentMasterToSlaveDelay_Type = DisplayString
_FsPtpCurrentMasterToSlaveDelay_Object = MibTableColumn
fsPtpCurrentMasterToSlaveDelay = _FsPtpCurrentMasterToSlaveDelay_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 4, 1, 1, 4),
    _FsPtpCurrentMasterToSlaveDelay_Type()
)
fsPtpCurrentMasterToSlaveDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpCurrentMasterToSlaveDelay.setStatus("current")
_FsPtpCurrentSlaveToMasterDelay_Type = DisplayString
_FsPtpCurrentSlaveToMasterDelay_Object = MibTableColumn
fsPtpCurrentSlaveToMasterDelay = _FsPtpCurrentSlaveToMasterDelay_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 4, 1, 1, 5),
    _FsPtpCurrentSlaveToMasterDelay_Type()
)
fsPtpCurrentSlaveToMasterDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpCurrentSlaveToMasterDelay.setStatus("current")
_FsPtpParentDataSet_ObjectIdentity = ObjectIdentity
fsPtpParentDataSet = _FsPtpParentDataSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 5)
)
_FsPtpParentDataSetTable_Object = MibTable
fsPtpParentDataSetTable = _FsPtpParentDataSetTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 5, 1)
)
if mibBuilder.loadTexts:
    fsPtpParentDataSetTable.setStatus("current")
_FsPtpParentDataSetEntry_Object = MibTableRow
fsPtpParentDataSetEntry = _FsPtpParentDataSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    fsPtpParentDataSetEntry.setStatus("current")


class _FsPtpParentClockIdentity_Type(OctetString):
    """Custom type fsPtpParentClockIdentity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FsPtpParentClockIdentity_Type.__name__ = "OctetString"
_FsPtpParentClockIdentity_Object = MibTableColumn
fsPtpParentClockIdentity = _FsPtpParentClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 5, 1, 1, 1),
    _FsPtpParentClockIdentity_Type()
)
fsPtpParentClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpParentClockIdentity.setStatus("current")
_FsPtpParentPortNumber_Type = FsPtpPortNumber
_FsPtpParentPortNumber_Object = MibTableColumn
fsPtpParentPortNumber = _FsPtpParentPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 5, 1, 1, 2),
    _FsPtpParentPortNumber_Type()
)
fsPtpParentPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpParentPortNumber.setStatus("current")


class _FsPtpParentStats_Type(TruthValue):
    """Custom type fsPtpParentStats based on TruthValue"""
    defaultValue = 2


_FsPtpParentStats_Type.__name__ = "TruthValue"
_FsPtpParentStats_Object = MibTableColumn
fsPtpParentStats = _FsPtpParentStats_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 5, 1, 1, 3),
    _FsPtpParentStats_Type()
)
fsPtpParentStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpParentStats.setStatus("current")


class _FsPtpParentObservedOffsetScaledLogVariance_Type(Integer32):
    """Custom type fsPtpParentObservedOffsetScaledLogVariance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsPtpParentObservedOffsetScaledLogVariance_Type.__name__ = "Integer32"
_FsPtpParentObservedOffsetScaledLogVariance_Object = MibTableColumn
fsPtpParentObservedOffsetScaledLogVariance = _FsPtpParentObservedOffsetScaledLogVariance_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 5, 1, 1, 4),
    _FsPtpParentObservedOffsetScaledLogVariance_Type()
)
fsPtpParentObservedOffsetScaledLogVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpParentObservedOffsetScaledLogVariance.setStatus("current")
_FsPtpParentObservedClockPhaseChangeRate_Type = Integer32
_FsPtpParentObservedClockPhaseChangeRate_Object = MibTableColumn
fsPtpParentObservedClockPhaseChangeRate = _FsPtpParentObservedClockPhaseChangeRate_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 5, 1, 1, 5),
    _FsPtpParentObservedClockPhaseChangeRate_Type()
)
fsPtpParentObservedClockPhaseChangeRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpParentObservedClockPhaseChangeRate.setStatus("current")


class _FsPtpParentGMClockIdentity_Type(OctetString):
    """Custom type fsPtpParentGMClockIdentity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FsPtpParentGMClockIdentity_Type.__name__ = "OctetString"
_FsPtpParentGMClockIdentity_Object = MibTableColumn
fsPtpParentGMClockIdentity = _FsPtpParentGMClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 5, 1, 1, 6),
    _FsPtpParentGMClockIdentity_Type()
)
fsPtpParentGMClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpParentGMClockIdentity.setStatus("current")


class _FsPtpParentGMClockClass_Type(Integer32):
    """Custom type fsPtpParentGMClockClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsPtpParentGMClockClass_Type.__name__ = "Integer32"
_FsPtpParentGMClockClass_Object = MibTableColumn
fsPtpParentGMClockClass = _FsPtpParentGMClockClass_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 5, 1, 1, 7),
    _FsPtpParentGMClockClass_Type()
)
fsPtpParentGMClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpParentGMClockClass.setStatus("current")


class _FsPtpParentGMClockAccuracy_Type(Integer32):
    """Custom type fsPtpParentGMClockAccuracy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsPtpParentGMClockAccuracy_Type.__name__ = "Integer32"
_FsPtpParentGMClockAccuracy_Object = MibTableColumn
fsPtpParentGMClockAccuracy = _FsPtpParentGMClockAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 5, 1, 1, 8),
    _FsPtpParentGMClockAccuracy_Type()
)
fsPtpParentGMClockAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpParentGMClockAccuracy.setStatus("current")


class _FsPtpParentGMClockOffsetScaledLogVariance_Type(Integer32):
    """Custom type fsPtpParentGMClockOffsetScaledLogVariance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsPtpParentGMClockOffsetScaledLogVariance_Type.__name__ = "Integer32"
_FsPtpParentGMClockOffsetScaledLogVariance_Object = MibTableColumn
fsPtpParentGMClockOffsetScaledLogVariance = _FsPtpParentGMClockOffsetScaledLogVariance_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 5, 1, 1, 9),
    _FsPtpParentGMClockOffsetScaledLogVariance_Type()
)
fsPtpParentGMClockOffsetScaledLogVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpParentGMClockOffsetScaledLogVariance.setStatus("current")


class _FsPtpParentGMPriority1_Type(Integer32):
    """Custom type fsPtpParentGMPriority1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsPtpParentGMPriority1_Type.__name__ = "Integer32"
_FsPtpParentGMPriority1_Object = MibTableColumn
fsPtpParentGMPriority1 = _FsPtpParentGMPriority1_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 5, 1, 1, 10),
    _FsPtpParentGMPriority1_Type()
)
fsPtpParentGMPriority1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpParentGMPriority1.setStatus("current")


class _FsPtpParentGMPriority2_Type(Integer32):
    """Custom type fsPtpParentGMPriority2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsPtpParentGMPriority2_Type.__name__ = "Integer32"
_FsPtpParentGMPriority2_Object = MibTableColumn
fsPtpParentGMPriority2 = _FsPtpParentGMPriority2_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 5, 1, 1, 11),
    _FsPtpParentGMPriority2_Type()
)
fsPtpParentGMPriority2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpParentGMPriority2.setStatus("current")
_FsPtpParentClockObservedDrift_Type = Integer32
_FsPtpParentClockObservedDrift_Object = MibTableColumn
fsPtpParentClockObservedDrift = _FsPtpParentClockObservedDrift_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 5, 1, 1, 12),
    _FsPtpParentClockObservedDrift_Type()
)
fsPtpParentClockObservedDrift.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpParentClockObservedDrift.setStatus("current")
_FsPtpGlobalTimeProportiesDataSet_ObjectIdentity = ObjectIdentity
fsPtpGlobalTimeProportiesDataSet = _FsPtpGlobalTimeProportiesDataSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 6)
)
_FsPtpTimeDataSetTable_Object = MibTable
fsPtpTimeDataSetTable = _FsPtpTimeDataSetTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 6, 1)
)
if mibBuilder.loadTexts:
    fsPtpTimeDataSetTable.setStatus("current")
_FsPtpTimeDataSetEntry_Object = MibTableRow
fsPtpTimeDataSetEntry = _FsPtpTimeDataSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    fsPtpTimeDataSetEntry.setStatus("current")


class _FsPtpTimeCurrentUTCOffset_Type(Integer32):
    """Custom type fsPtpTimeCurrentUTCOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsPtpTimeCurrentUTCOffset_Type.__name__ = "Integer32"
_FsPtpTimeCurrentUTCOffset_Object = MibTableColumn
fsPtpTimeCurrentUTCOffset = _FsPtpTimeCurrentUTCOffset_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 6, 1, 1, 1),
    _FsPtpTimeCurrentUTCOffset_Type()
)
fsPtpTimeCurrentUTCOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpTimeCurrentUTCOffset.setStatus("current")
_FsPtpTimeCurrentUTCOffsetValid_Type = TruthValue
_FsPtpTimeCurrentUTCOffsetValid_Object = MibTableColumn
fsPtpTimeCurrentUTCOffsetValid = _FsPtpTimeCurrentUTCOffsetValid_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 6, 1, 1, 2),
    _FsPtpTimeCurrentUTCOffsetValid_Type()
)
fsPtpTimeCurrentUTCOffsetValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpTimeCurrentUTCOffsetValid.setStatus("current")
_FsPtpTimeLeap59_Type = TruthValue
_FsPtpTimeLeap59_Object = MibTableColumn
fsPtpTimeLeap59 = _FsPtpTimeLeap59_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 6, 1, 1, 3),
    _FsPtpTimeLeap59_Type()
)
fsPtpTimeLeap59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpTimeLeap59.setStatus("current")
_FsPtpTimeLeap61_Type = TruthValue
_FsPtpTimeLeap61_Object = MibTableColumn
fsPtpTimeLeap61 = _FsPtpTimeLeap61_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 6, 1, 1, 4),
    _FsPtpTimeLeap61_Type()
)
fsPtpTimeLeap61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpTimeLeap61.setStatus("current")
_FsPtpTimeTimeTraceable_Type = TruthValue
_FsPtpTimeTimeTraceable_Object = MibTableColumn
fsPtpTimeTimeTraceable = _FsPtpTimeTimeTraceable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 6, 1, 1, 5),
    _FsPtpTimeTimeTraceable_Type()
)
fsPtpTimeTimeTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpTimeTimeTraceable.setStatus("current")
_FsPtpTimeFrequencyTraceable_Type = TruthValue
_FsPtpTimeFrequencyTraceable_Object = MibTableColumn
fsPtpTimeFrequencyTraceable = _FsPtpTimeFrequencyTraceable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 6, 1, 1, 6),
    _FsPtpTimeFrequencyTraceable_Type()
)
fsPtpTimeFrequencyTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpTimeFrequencyTraceable.setStatus("current")


class _FsPtpTimeTimeSource_Type(Integer32):
    """Custom type fsPtpTimeTimeSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              32,
              48,
              64,
              80,
              96,
              144,
              160,
              255)
        )
    )
    namedValues = NamedValues(
        *(("atomicclock", 16),
          ("gps", 32),
          ("terrestrialradio", 48),
          ("ptp", 64),
          ("ntp", 80),
          ("handset", 96),
          ("other", 144),
          ("internaloscillator", 160),
          ("reserved", 255))
    )


_FsPtpTimeTimeSource_Type.__name__ = "Integer32"
_FsPtpTimeTimeSource_Object = MibTableColumn
fsPtpTimeTimeSource = _FsPtpTimeTimeSource_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 6, 1, 1, 7),
    _FsPtpTimeTimeSource_Type()
)
fsPtpTimeTimeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpTimeTimeSource.setStatus("current")
_FsPtpPortConfigurationDataSet_ObjectIdentity = ObjectIdentity
fsPtpPortConfigurationDataSet = _FsPtpPortConfigurationDataSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 7)
)
_FsPtpPortConfigDataSetTable_Object = MibTable
fsPtpPortConfigDataSetTable = _FsPtpPortConfigDataSetTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 7, 1)
)
if mibBuilder.loadTexts:
    fsPtpPortConfigDataSetTable.setStatus("current")
_FsPtpPortConfigDataSetEntry_Object = MibTableRow
fsPtpPortConfigDataSetEntry = _FsPtpPortConfigDataSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 7, 1, 1)
)
fsPtpPortConfigDataSetEntry.setIndexNames(
    (0, "SUPERMICRO-PTP-MIB", "fsPtpContextId"),
    (0, "SUPERMICRO-PTP-MIB", "fsPtpDomainNumber"),
    (0, "SUPERMICRO-PTP-MIB", "fsPtpPortIndex"),
)
if mibBuilder.loadTexts:
    fsPtpPortConfigDataSetEntry.setStatus("current")


class _FsPtpPortIndex_Type(FsPtpPortNumber):
    """Custom type fsPtpPortIndex based on FsPtpPortNumber"""
    subtypeSpec = FsPtpPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsPtpPortIndex_Type.__name__ = "FsPtpPortNumber"
_FsPtpPortIndex_Object = MibTableColumn
fsPtpPortIndex = _FsPtpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 7, 1, 1, 1),
    _FsPtpPortIndex_Type()
)
fsPtpPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPtpPortIndex.setStatus("current")


class _FsPtpPortClockIdentity_Type(OctetString):
    """Custom type fsPtpPortClockIdentity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FsPtpPortClockIdentity_Type.__name__ = "OctetString"
_FsPtpPortClockIdentity_Object = MibTableColumn
fsPtpPortClockIdentity = _FsPtpPortClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 7, 1, 1, 2),
    _FsPtpPortClockIdentity_Type()
)
fsPtpPortClockIdentity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpPortClockIdentity.setStatus("current")


class _FsPtpPortInterfaceType_Type(Integer32):
    """Custom type fsPtpPortInterfaceType based on Integer32"""
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
              65534)
        )
    )
    namedValues = NamedValues(
        *(("udpipv4", 1),
          ("udpipv6", 2),
          ("ieee8023", 3),
          ("devicenet", 4),
          ("controlnet", 5),
          ("profitnet", 6),
          ("ieee8021", 7),
          ("unknown", 65534))
    )


_FsPtpPortInterfaceType_Type.__name__ = "Integer32"
_FsPtpPortInterfaceType_Object = MibTableColumn
fsPtpPortInterfaceType = _FsPtpPortInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 7, 1, 1, 3),
    _FsPtpPortInterfaceType_Type()
)
fsPtpPortInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpPortInterfaceType.setStatus("current")
_FsPtpPortIfaceNumber_Type = Integer32
_FsPtpPortIfaceNumber_Object = MibTableColumn
fsPtpPortIfaceNumber = _FsPtpPortIfaceNumber_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 7, 1, 1, 4),
    _FsPtpPortIfaceNumber_Type()
)
fsPtpPortIfaceNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpPortIfaceNumber.setStatus("current")


class _FsPtpPortState_Type(Integer32):
    """Custom type fsPtpPortState based on Integer32"""
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
        *(("faulty", 0),
          ("disabled", 1),
          ("initializing", 2),
          ("listening", 3),
          ("uncalibrated", 4),
          ("slave", 5),
          ("premaster", 6),
          ("master", 7),
          ("passive", 8))
    )


_FsPtpPortState_Type.__name__ = "Integer32"
_FsPtpPortState_Object = MibTableColumn
fsPtpPortState = _FsPtpPortState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 7, 1, 1, 5),
    _FsPtpPortState_Type()
)
fsPtpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpPortState.setStatus("current")


class _FsPtpPortMinDelayReqInterval_Type(Integer32):
    """Custom type fsPtpPortMinDelayReqInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_FsPtpPortMinDelayReqInterval_Type.__name__ = "Integer32"
_FsPtpPortMinDelayReqInterval_Object = MibTableColumn
fsPtpPortMinDelayReqInterval = _FsPtpPortMinDelayReqInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 7, 1, 1, 6),
    _FsPtpPortMinDelayReqInterval_Type()
)
fsPtpPortMinDelayReqInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpPortMinDelayReqInterval.setStatus("current")
_FsPtpPortPeerMeanPathDelay_Type = DisplayString
_FsPtpPortPeerMeanPathDelay_Object = MibTableColumn
fsPtpPortPeerMeanPathDelay = _FsPtpPortPeerMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 7, 1, 1, 7),
    _FsPtpPortPeerMeanPathDelay_Type()
)
fsPtpPortPeerMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpPortPeerMeanPathDelay.setStatus("current")


class _FsPtpPortAnnounceInterval_Type(Integer32):
    """Custom type fsPtpPortAnnounceInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_FsPtpPortAnnounceInterval_Type.__name__ = "Integer32"
_FsPtpPortAnnounceInterval_Object = MibTableColumn
fsPtpPortAnnounceInterval = _FsPtpPortAnnounceInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 7, 1, 1, 8),
    _FsPtpPortAnnounceInterval_Type()
)
fsPtpPortAnnounceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpPortAnnounceInterval.setStatus("current")


class _FsPtpPortAnnounceReceiptTimeout_Type(Integer32):
    """Custom type fsPtpPortAnnounceReceiptTimeout based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_FsPtpPortAnnounceReceiptTimeout_Type.__name__ = "Integer32"
_FsPtpPortAnnounceReceiptTimeout_Object = MibTableColumn
fsPtpPortAnnounceReceiptTimeout = _FsPtpPortAnnounceReceiptTimeout_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 7, 1, 1, 9),
    _FsPtpPortAnnounceReceiptTimeout_Type()
)
fsPtpPortAnnounceReceiptTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpPortAnnounceReceiptTimeout.setStatus("current")


class _FsPtpPortSyncInterval_Type(Integer32):
    """Custom type fsPtpPortSyncInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1),
    )


_FsPtpPortSyncInterval_Type.__name__ = "Integer32"
_FsPtpPortSyncInterval_Object = MibTableColumn
fsPtpPortSyncInterval = _FsPtpPortSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 7, 1, 1, 10),
    _FsPtpPortSyncInterval_Type()
)
fsPtpPortSyncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpPortSyncInterval.setStatus("current")


class _FsPtpPortSynclimit_Type(DisplayString):
    """Custom type fsPtpPortSynclimit based on DisplayString"""
    defaultValue = OctetString("1000000000")


_FsPtpPortSynclimit_Type.__name__ = "DisplayString"
_FsPtpPortSynclimit_Object = MibTableColumn
fsPtpPortSynclimit = _FsPtpPortSynclimit_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 7, 1, 1, 11),
    _FsPtpPortSynclimit_Type()
)
fsPtpPortSynclimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpPortSynclimit.setStatus("current")


class _FsPtpPortDelayMechanism_Type(Integer32):
    """Custom type fsPtpPortDelayMechanism based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("endtoend", 1),
          ("peertopeer", 2),
          ("disabled", 255))
    )


_FsPtpPortDelayMechanism_Type.__name__ = "Integer32"
_FsPtpPortDelayMechanism_Object = MibTableColumn
fsPtpPortDelayMechanism = _FsPtpPortDelayMechanism_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 7, 1, 1, 12),
    _FsPtpPortDelayMechanism_Type()
)
fsPtpPortDelayMechanism.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpPortDelayMechanism.setStatus("current")


class _FsPtpPortMinPdelayReqInterval_Type(Integer32):
    """Custom type fsPtpPortMinPdelayReqInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_FsPtpPortMinPdelayReqInterval_Type.__name__ = "Integer32"
_FsPtpPortMinPdelayReqInterval_Object = MibTableColumn
fsPtpPortMinPdelayReqInterval = _FsPtpPortMinPdelayReqInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 7, 1, 1, 13),
    _FsPtpPortMinPdelayReqInterval_Type()
)
fsPtpPortMinPdelayReqInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpPortMinPdelayReqInterval.setStatus("current")


class _FsPtpPortVersionNumber_Type(Integer32):
    """Custom type fsPtpPortVersionNumber based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_FsPtpPortVersionNumber_Type.__name__ = "Integer32"
_FsPtpPortVersionNumber_Object = MibTableColumn
fsPtpPortVersionNumber = _FsPtpPortVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 7, 1, 1, 14),
    _FsPtpPortVersionNumber_Type()
)
fsPtpPortVersionNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpPortVersionNumber.setStatus("current")


class _FsPtpPortUnicastNegOption_Type(TruthValue):
    """Custom type fsPtpPortUnicastNegOption based on TruthValue"""
    defaultValue = 2


_FsPtpPortUnicastNegOption_Type.__name__ = "TruthValue"
_FsPtpPortUnicastNegOption_Object = MibTableColumn
fsPtpPortUnicastNegOption = _FsPtpPortUnicastNegOption_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 7, 1, 1, 15),
    _FsPtpPortUnicastNegOption_Type()
)
fsPtpPortUnicastNegOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpPortUnicastNegOption.setStatus("current")


class _FsPtpPortUnicastMasterMaxSize_Type(Integer32):
    """Custom type fsPtpPortUnicastMasterMaxSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsPtpPortUnicastMasterMaxSize_Type.__name__ = "Integer32"
_FsPtpPortUnicastMasterMaxSize_Object = MibTableColumn
fsPtpPortUnicastMasterMaxSize = _FsPtpPortUnicastMasterMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 7, 1, 1, 16),
    _FsPtpPortUnicastMasterMaxSize_Type()
)
fsPtpPortUnicastMasterMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpPortUnicastMasterMaxSize.setStatus("current")


class _FsPtpPortAccMasterEnabled_Type(TruthValue):
    """Custom type fsPtpPortAccMasterEnabled based on TruthValue"""
    defaultValue = 2


_FsPtpPortAccMasterEnabled_Type.__name__ = "TruthValue"
_FsPtpPortAccMasterEnabled_Object = MibTableColumn
fsPtpPortAccMasterEnabled = _FsPtpPortAccMasterEnabled_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 7, 1, 1, 17),
    _FsPtpPortAccMasterEnabled_Type()
)
fsPtpPortAccMasterEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpPortAccMasterEnabled.setStatus("current")


class _FsPtpPortNumOfAltMaster_Type(Integer32):
    """Custom type fsPtpPortNumOfAltMaster based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsPtpPortNumOfAltMaster_Type.__name__ = "Integer32"
_FsPtpPortNumOfAltMaster_Object = MibTableColumn
fsPtpPortNumOfAltMaster = _FsPtpPortNumOfAltMaster_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 7, 1, 1, 18),
    _FsPtpPortNumOfAltMaster_Type()
)
fsPtpPortNumOfAltMaster.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpPortNumOfAltMaster.setStatus("current")


class _FsPtpPortAltMulcastSync_Type(TruthValue):
    """Custom type fsPtpPortAltMulcastSync based on TruthValue"""
    defaultValue = 2


_FsPtpPortAltMulcastSync_Type.__name__ = "TruthValue"
_FsPtpPortAltMulcastSync_Object = MibTableColumn
fsPtpPortAltMulcastSync = _FsPtpPortAltMulcastSync_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 7, 1, 1, 19),
    _FsPtpPortAltMulcastSync_Type()
)
fsPtpPortAltMulcastSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpPortAltMulcastSync.setStatus("current")


class _FsPtpPortAltMulcastSyncInterval_Type(Integer32):
    """Custom type fsPtpPortAltMulcastSyncInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsPtpPortAltMulcastSyncInterval_Type.__name__ = "Integer32"
_FsPtpPortAltMulcastSyncInterval_Object = MibTableColumn
fsPtpPortAltMulcastSyncInterval = _FsPtpPortAltMulcastSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 7, 1, 1, 20),
    _FsPtpPortAltMulcastSyncInterval_Type()
)
fsPtpPortAltMulcastSyncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpPortAltMulcastSyncInterval.setStatus("current")


class _FsPtpPortPtpStatus_Type(TruthValue):
    """Custom type fsPtpPortPtpStatus based on TruthValue"""
    defaultValue = 2


_FsPtpPortPtpStatus_Type.__name__ = "TruthValue"
_FsPtpPortPtpStatus_Object = MibTableColumn
fsPtpPortPtpStatus = _FsPtpPortPtpStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 7, 1, 1, 21),
    _FsPtpPortPtpStatus_Type()
)
fsPtpPortPtpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpPortPtpStatus.setStatus("current")
_FsPtpPortRcvdAnnounceMsgCnt_Type = Unsigned32
_FsPtpPortRcvdAnnounceMsgCnt_Object = MibTableColumn
fsPtpPortRcvdAnnounceMsgCnt = _FsPtpPortRcvdAnnounceMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 7, 1, 1, 22),
    _FsPtpPortRcvdAnnounceMsgCnt_Type()
)
fsPtpPortRcvdAnnounceMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpPortRcvdAnnounceMsgCnt.setStatus("current")
_FsPtpPortRcvdSyncMsgCnt_Type = Unsigned32
_FsPtpPortRcvdSyncMsgCnt_Object = MibTableColumn
fsPtpPortRcvdSyncMsgCnt = _FsPtpPortRcvdSyncMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 7, 1, 1, 23),
    _FsPtpPortRcvdSyncMsgCnt_Type()
)
fsPtpPortRcvdSyncMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpPortRcvdSyncMsgCnt.setStatus("current")
_FsPtpPortRcvdDelayReqMsgCnt_Type = Unsigned32
_FsPtpPortRcvdDelayReqMsgCnt_Object = MibTableColumn
fsPtpPortRcvdDelayReqMsgCnt = _FsPtpPortRcvdDelayReqMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 7, 1, 1, 24),
    _FsPtpPortRcvdDelayReqMsgCnt_Type()
)
fsPtpPortRcvdDelayReqMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpPortRcvdDelayReqMsgCnt.setStatus("current")
_FsPtpPortRcvdDelayRespMsgCnt_Type = Unsigned32
_FsPtpPortRcvdDelayRespMsgCnt_Object = MibTableColumn
fsPtpPortRcvdDelayRespMsgCnt = _FsPtpPortRcvdDelayRespMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 7, 1, 1, 25),
    _FsPtpPortRcvdDelayRespMsgCnt_Type()
)
fsPtpPortRcvdDelayRespMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpPortRcvdDelayRespMsgCnt.setStatus("current")
_FsPtpPortTransDelayReqMsgCnt_Type = Unsigned32
_FsPtpPortTransDelayReqMsgCnt_Object = MibTableColumn
fsPtpPortTransDelayReqMsgCnt = _FsPtpPortTransDelayReqMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 7, 1, 1, 26),
    _FsPtpPortTransDelayReqMsgCnt_Type()
)
fsPtpPortTransDelayReqMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpPortTransDelayReqMsgCnt.setStatus("current")
_FsPtpPortDiscardedMsgCnt_Type = Unsigned32
_FsPtpPortDiscardedMsgCnt_Object = MibTableColumn
fsPtpPortDiscardedMsgCnt = _FsPtpPortDiscardedMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 7, 1, 1, 27),
    _FsPtpPortDiscardedMsgCnt_Type()
)
fsPtpPortDiscardedMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpPortDiscardedMsgCnt.setStatus("current")
_FsPtpPortRowStatus_Type = RowStatus
_FsPtpPortRowStatus_Object = MibTableColumn
fsPtpPortRowStatus = _FsPtpPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 7, 1, 1, 28),
    _FsPtpPortRowStatus_Type()
)
fsPtpPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPtpPortRowStatus.setStatus("current")
_FsPtpForeignMasterDataSet_ObjectIdentity = ObjectIdentity
fsPtpForeignMasterDataSet = _FsPtpForeignMasterDataSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 8)
)
_FsPtpForeignMasterDataSetTable_Object = MibTable
fsPtpForeignMasterDataSetTable = _FsPtpForeignMasterDataSetTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 8, 1)
)
if mibBuilder.loadTexts:
    fsPtpForeignMasterDataSetTable.setStatus("current")
_FsPtpForeignMasterDataSetEntry_Object = MibTableRow
fsPtpForeignMasterDataSetEntry = _FsPtpForeignMasterDataSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 8, 1, 1)
)
fsPtpForeignMasterDataSetEntry.setIndexNames(
    (0, "SUPERMICRO-PTP-MIB", "fsPtpContextId"),
    (0, "SUPERMICRO-PTP-MIB", "fsPtpDomainNumber"),
    (0, "SUPERMICRO-PTP-MIB", "fsPtpForeignMasterClockIdentity"),
    (0, "SUPERMICRO-PTP-MIB", "fsPtpForeignMasterPortIndex"),
    (0, "SUPERMICRO-PTP-MIB", "fsPtpPortIndex"),
)
if mibBuilder.loadTexts:
    fsPtpForeignMasterDataSetEntry.setStatus("current")


class _FsPtpForeignMasterClockIdentity_Type(OctetString):
    """Custom type fsPtpForeignMasterClockIdentity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FsPtpForeignMasterClockIdentity_Type.__name__ = "OctetString"
_FsPtpForeignMasterClockIdentity_Object = MibTableColumn
fsPtpForeignMasterClockIdentity = _FsPtpForeignMasterClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 8, 1, 1, 1),
    _FsPtpForeignMasterClockIdentity_Type()
)
fsPtpForeignMasterClockIdentity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPtpForeignMasterClockIdentity.setStatus("current")


class _FsPtpForeignMasterPortIndex_Type(FsPtpPortNumber):
    """Custom type fsPtpForeignMasterPortIndex based on FsPtpPortNumber"""
    subtypeSpec = FsPtpPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsPtpForeignMasterPortIndex_Type.__name__ = "FsPtpPortNumber"
_FsPtpForeignMasterPortIndex_Object = MibTableColumn
fsPtpForeignMasterPortIndex = _FsPtpForeignMasterPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 8, 1, 1, 2),
    _FsPtpForeignMasterPortIndex_Type()
)
fsPtpForeignMasterPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPtpForeignMasterPortIndex.setStatus("current")
_FsPtpForeignMasterAnnounceMsgs_Type = Integer32
_FsPtpForeignMasterAnnounceMsgs_Object = MibTableColumn
fsPtpForeignMasterAnnounceMsgs = _FsPtpForeignMasterAnnounceMsgs_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 8, 1, 1, 3),
    _FsPtpForeignMasterAnnounceMsgs_Type()
)
fsPtpForeignMasterAnnounceMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpForeignMasterAnnounceMsgs.setStatus("current")
_FsPtpTransparentDataSet_ObjectIdentity = ObjectIdentity
fsPtpTransparentDataSet = _FsPtpTransparentDataSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 9)
)
_FsPtpTransparentDataSetTable_Object = MibTable
fsPtpTransparentDataSetTable = _FsPtpTransparentDataSetTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 9, 1)
)
if mibBuilder.loadTexts:
    fsPtpTransparentDataSetTable.setStatus("current")
_FsPtpTransparentDataSetEntry_Object = MibTableRow
fsPtpTransparentDataSetEntry = _FsPtpTransparentDataSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    fsPtpTransparentDataSetEntry.setStatus("current")


class _FsPtpTransparentClockIdentity_Type(OctetString):
    """Custom type fsPtpTransparentClockIdentity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FsPtpTransparentClockIdentity_Type.__name__ = "OctetString"
_FsPtpTransparentClockIdentity_Object = MibTableColumn
fsPtpTransparentClockIdentity = _FsPtpTransparentClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 9, 1, 1, 1),
    _FsPtpTransparentClockIdentity_Type()
)
fsPtpTransparentClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpTransparentClockIdentity.setStatus("current")


class _FsPtpTransparentClockTwoStepFlag_Type(TruthValue):
    """Custom type fsPtpTransparentClockTwoStepFlag based on TruthValue"""
    defaultValue = 2


_FsPtpTransparentClockTwoStepFlag_Type.__name__ = "TruthValue"
_FsPtpTransparentClockTwoStepFlag_Object = MibTableColumn
fsPtpTransparentClockTwoStepFlag = _FsPtpTransparentClockTwoStepFlag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 9, 1, 1, 2),
    _FsPtpTransparentClockTwoStepFlag_Type()
)
fsPtpTransparentClockTwoStepFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpTransparentClockTwoStepFlag.setStatus("current")


class _FsPtpTransparentClockNumberPorts_Type(Integer32):
    """Custom type fsPtpTransparentClockNumberPorts based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_FsPtpTransparentClockNumberPorts_Type.__name__ = "Integer32"
_FsPtpTransparentClockNumberPorts_Object = MibTableColumn
fsPtpTransparentClockNumberPorts = _FsPtpTransparentClockNumberPorts_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 9, 1, 1, 3),
    _FsPtpTransparentClockNumberPorts_Type()
)
fsPtpTransparentClockNumberPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpTransparentClockNumberPorts.setStatus("current")


class _FsPtpTransparentClockDelaymechanism_Type(Integer32):
    """Custom type fsPtpTransparentClockDelaymechanism based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("endtoend", 1),
          ("peertopeer", 2))
    )


_FsPtpTransparentClockDelaymechanism_Type.__name__ = "Integer32"
_FsPtpTransparentClockDelaymechanism_Object = MibTableColumn
fsPtpTransparentClockDelaymechanism = _FsPtpTransparentClockDelaymechanism_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 9, 1, 1, 4),
    _FsPtpTransparentClockDelaymechanism_Type()
)
fsPtpTransparentClockDelaymechanism.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpTransparentClockDelaymechanism.setStatus("current")


class _FsPtpTransparentClockPrimaryDomain_Type(Integer32):
    """Custom type fsPtpTransparentClockPrimaryDomain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsPtpTransparentClockPrimaryDomain_Type.__name__ = "Integer32"
_FsPtpTransparentClockPrimaryDomain_Object = MibTableColumn
fsPtpTransparentClockPrimaryDomain = _FsPtpTransparentClockPrimaryDomain_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 9, 1, 1, 5),
    _FsPtpTransparentClockPrimaryDomain_Type()
)
fsPtpTransparentClockPrimaryDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpTransparentClockPrimaryDomain.setStatus("current")
_FsPtpTransparentPortDataSet_ObjectIdentity = ObjectIdentity
fsPtpTransparentPortDataSet = _FsPtpTransparentPortDataSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 10)
)
_FsPtpTransparentPortDataSetTable_Object = MibTable
fsPtpTransparentPortDataSetTable = _FsPtpTransparentPortDataSetTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 10, 1)
)
if mibBuilder.loadTexts:
    fsPtpTransparentPortDataSetTable.setStatus("current")
_FsPtpTransparentPortDataSetEntry_Object = MibTableRow
fsPtpTransparentPortDataSetEntry = _FsPtpTransparentPortDataSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 10, 1, 1)
)
fsPtpTransparentPortDataSetEntry.setIndexNames(
    (0, "SUPERMICRO-PTP-MIB", "fsPtpContextId"),
    (0, "SUPERMICRO-PTP-MIB", "fsPtpDomainNumber"),
    (0, "SUPERMICRO-PTP-MIB", "fsPtpTransparentPortIndex"),
)
if mibBuilder.loadTexts:
    fsPtpTransparentPortDataSetEntry.setStatus("current")


class _FsPtpTransparentPortIndex_Type(FsPtpPortNumber):
    """Custom type fsPtpTransparentPortIndex based on FsPtpPortNumber"""
    subtypeSpec = FsPtpPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsPtpTransparentPortIndex_Type.__name__ = "FsPtpPortNumber"
_FsPtpTransparentPortIndex_Object = MibTableColumn
fsPtpTransparentPortIndex = _FsPtpTransparentPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 10, 1, 1, 1),
    _FsPtpTransparentPortIndex_Type()
)
fsPtpTransparentPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPtpTransparentPortIndex.setStatus("current")


class _FsPtpTransparentPortInterfaceType_Type(Integer32):
    """Custom type fsPtpTransparentPortInterfaceType based on Integer32"""
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
              65534)
        )
    )
    namedValues = NamedValues(
        *(("udpipv4", 1),
          ("udpipv6", 2),
          ("ieee8023", 3),
          ("devicenet", 4),
          ("controlnet", 5),
          ("profitnet", 6),
          ("ieee8021", 7),
          ("unknown", 65534))
    )


_FsPtpTransparentPortInterfaceType_Type.__name__ = "Integer32"
_FsPtpTransparentPortInterfaceType_Object = MibTableColumn
fsPtpTransparentPortInterfaceType = _FsPtpTransparentPortInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 10, 1, 1, 2),
    _FsPtpTransparentPortInterfaceType_Type()
)
fsPtpTransparentPortInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpTransparentPortInterfaceType.setStatus("current")
_FsPtpTransparentPortIfaceNumber_Type = Integer32
_FsPtpTransparentPortIfaceNumber_Object = MibTableColumn
fsPtpTransparentPortIfaceNumber = _FsPtpTransparentPortIfaceNumber_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 10, 1, 1, 3),
    _FsPtpTransparentPortIfaceNumber_Type()
)
fsPtpTransparentPortIfaceNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpTransparentPortIfaceNumber.setStatus("current")


class _FsPtpTransparentPortClockIdentity_Type(OctetString):
    """Custom type fsPtpTransparentPortClockIdentity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FsPtpTransparentPortClockIdentity_Type.__name__ = "OctetString"
_FsPtpTransparentPortClockIdentity_Object = MibTableColumn
fsPtpTransparentPortClockIdentity = _FsPtpTransparentPortClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 10, 1, 1, 4),
    _FsPtpTransparentPortClockIdentity_Type()
)
fsPtpTransparentPortClockIdentity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpTransparentPortClockIdentity.setStatus("current")


class _FsPtpTransparentPortMinPdelayReqInterval_Type(Integer32):
    """Custom type fsPtpTransparentPortMinPdelayReqInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_FsPtpTransparentPortMinPdelayReqInterval_Type.__name__ = "Integer32"
_FsPtpTransparentPortMinPdelayReqInterval_Object = MibTableColumn
fsPtpTransparentPortMinPdelayReqInterval = _FsPtpTransparentPortMinPdelayReqInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 10, 1, 1, 5),
    _FsPtpTransparentPortMinPdelayReqInterval_Type()
)
fsPtpTransparentPortMinPdelayReqInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpTransparentPortMinPdelayReqInterval.setStatus("current")


class _FsPtpTransparentPortFaultyFlag_Type(TruthValue):
    """Custom type fsPtpTransparentPortFaultyFlag based on TruthValue"""
    defaultValue = 2


_FsPtpTransparentPortFaultyFlag_Type.__name__ = "TruthValue"
_FsPtpTransparentPortFaultyFlag_Object = MibTableColumn
fsPtpTransparentPortFaultyFlag = _FsPtpTransparentPortFaultyFlag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 10, 1, 1, 6),
    _FsPtpTransparentPortFaultyFlag_Type()
)
fsPtpTransparentPortFaultyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpTransparentPortFaultyFlag.setStatus("current")
_FsPtpTransparentPortPeerMeanPathDelay_Type = DisplayString
_FsPtpTransparentPortPeerMeanPathDelay_Object = MibTableColumn
fsPtpTransparentPortPeerMeanPathDelay = _FsPtpTransparentPortPeerMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 10, 1, 1, 7),
    _FsPtpTransparentPortPeerMeanPathDelay_Type()
)
fsPtpTransparentPortPeerMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpTransparentPortPeerMeanPathDelay.setStatus("current")


class _FsPtpTransparentPortPtpStatus_Type(TruthValue):
    """Custom type fsPtpTransparentPortPtpStatus based on TruthValue"""
    defaultValue = 2


_FsPtpTransparentPortPtpStatus_Type.__name__ = "TruthValue"
_FsPtpTransparentPortPtpStatus_Object = MibTableColumn
fsPtpTransparentPortPtpStatus = _FsPtpTransparentPortPtpStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 10, 1, 1, 8),
    _FsPtpTransparentPortPtpStatus_Type()
)
fsPtpTransparentPortPtpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpTransparentPortPtpStatus.setStatus("current")
_FsPtpTransparentPortRowStatus_Type = RowStatus
_FsPtpTransparentPortRowStatus_Object = MibTableColumn
fsPtpTransparentPortRowStatus = _FsPtpTransparentPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 10, 1, 1, 9),
    _FsPtpTransparentPortRowStatus_Type()
)
fsPtpTransparentPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpTransparentPortRowStatus.setStatus("current")
_FsPtpGrandMasterClusterDataSet_ObjectIdentity = ObjectIdentity
fsPtpGrandMasterClusterDataSet = _FsPtpGrandMasterClusterDataSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 11)
)
_FsPtpGrandMasterClusterDataSetTable_Object = MibTable
fsPtpGrandMasterClusterDataSetTable = _FsPtpGrandMasterClusterDataSetTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 11, 1)
)
if mibBuilder.loadTexts:
    fsPtpGrandMasterClusterDataSetTable.setStatus("current")
_FsPtpGrandMasterClusterDataSetEntry_Object = MibTableRow
fsPtpGrandMasterClusterDataSetEntry = _FsPtpGrandMasterClusterDataSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 11, 1, 1)
)
fsPtpGrandMasterClusterDataSetEntry.setIndexNames(
    (0, "SUPERMICRO-PTP-MIB", "fsPtpContextId"),
    (0, "SUPERMICRO-PTP-MIB", "fsPtpDomainNumber"),
    (0, "SUPERMICRO-PTP-MIB", "fsPtpGrandMasterClusterNetworkProtocol"),
    (0, "SUPERMICRO-PTP-MIB", "fsPtpGrandMasterClusterAddLength"),
    (0, "SUPERMICRO-PTP-MIB", "fsPtpGrandMasterClusterAddr"),
)
if mibBuilder.loadTexts:
    fsPtpGrandMasterClusterDataSetEntry.setStatus("current")


class _FsPtpGrandMasterClusterNetworkProtocol_Type(Integer32):
    """Custom type fsPtpGrandMasterClusterNetworkProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsPtpGrandMasterClusterNetworkProtocol_Type.__name__ = "Integer32"
_FsPtpGrandMasterClusterNetworkProtocol_Object = MibTableColumn
fsPtpGrandMasterClusterNetworkProtocol = _FsPtpGrandMasterClusterNetworkProtocol_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 11, 1, 1, 1),
    _FsPtpGrandMasterClusterNetworkProtocol_Type()
)
fsPtpGrandMasterClusterNetworkProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPtpGrandMasterClusterNetworkProtocol.setStatus("current")


class _FsPtpGrandMasterClusterAddLength_Type(Integer32):
    """Custom type fsPtpGrandMasterClusterAddLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FsPtpGrandMasterClusterAddLength_Type.__name__ = "Integer32"
_FsPtpGrandMasterClusterAddLength_Object = MibTableColumn
fsPtpGrandMasterClusterAddLength = _FsPtpGrandMasterClusterAddLength_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 11, 1, 1, 2),
    _FsPtpGrandMasterClusterAddLength_Type()
)
fsPtpGrandMasterClusterAddLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPtpGrandMasterClusterAddLength.setStatus("current")


class _FsPtpGrandMasterClusterAddr_Type(OctetString):
    """Custom type fsPtpGrandMasterClusterAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_FsPtpGrandMasterClusterAddr_Type.__name__ = "OctetString"
_FsPtpGrandMasterClusterAddr_Object = MibTableColumn
fsPtpGrandMasterClusterAddr = _FsPtpGrandMasterClusterAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 11, 1, 1, 3),
    _FsPtpGrandMasterClusterAddr_Type()
)
fsPtpGrandMasterClusterAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPtpGrandMasterClusterAddr.setStatus("current")
_FsPtpGrandMasterClusterRowStatus_Type = RowStatus
_FsPtpGrandMasterClusterRowStatus_Object = MibTableColumn
fsPtpGrandMasterClusterRowStatus = _FsPtpGrandMasterClusterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 11, 1, 1, 4),
    _FsPtpGrandMasterClusterRowStatus_Type()
)
fsPtpGrandMasterClusterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpGrandMasterClusterRowStatus.setStatus("current")
_FsPtpUnicastMasterDataSet_ObjectIdentity = ObjectIdentity
fsPtpUnicastMasterDataSet = _FsPtpUnicastMasterDataSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 12)
)
_FsPtpUnicastMasterDataSetTable_Object = MibTable
fsPtpUnicastMasterDataSetTable = _FsPtpUnicastMasterDataSetTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 12, 1)
)
if mibBuilder.loadTexts:
    fsPtpUnicastMasterDataSetTable.setStatus("current")
_FsPtpUnicastMasterDataSetEntry_Object = MibTableRow
fsPtpUnicastMasterDataSetEntry = _FsPtpUnicastMasterDataSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 12, 1, 1)
)
fsPtpUnicastMasterDataSetEntry.setIndexNames(
    (0, "SUPERMICRO-PTP-MIB", "fsPtpContextId"),
    (0, "SUPERMICRO-PTP-MIB", "fsPtpDomainNumber"),
    (0, "SUPERMICRO-PTP-MIB", "fsPtpPortIndex"),
    (0, "SUPERMICRO-PTP-MIB", "fsPtpUnicastMasterNetworkProtocol"),
    (0, "SUPERMICRO-PTP-MIB", "fsPtpUnicastMasterAddLength"),
    (0, "SUPERMICRO-PTP-MIB", "fsPtpUnicastMasterAddr"),
)
if mibBuilder.loadTexts:
    fsPtpUnicastMasterDataSetEntry.setStatus("current")


class _FsPtpUnicastMasterNetworkProtocol_Type(Integer32):
    """Custom type fsPtpUnicastMasterNetworkProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsPtpUnicastMasterNetworkProtocol_Type.__name__ = "Integer32"
_FsPtpUnicastMasterNetworkProtocol_Object = MibTableColumn
fsPtpUnicastMasterNetworkProtocol = _FsPtpUnicastMasterNetworkProtocol_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 12, 1, 1, 1),
    _FsPtpUnicastMasterNetworkProtocol_Type()
)
fsPtpUnicastMasterNetworkProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPtpUnicastMasterNetworkProtocol.setStatus("current")


class _FsPtpUnicastMasterAddLength_Type(Integer32):
    """Custom type fsPtpUnicastMasterAddLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FsPtpUnicastMasterAddLength_Type.__name__ = "Integer32"
_FsPtpUnicastMasterAddLength_Object = MibTableColumn
fsPtpUnicastMasterAddLength = _FsPtpUnicastMasterAddLength_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 12, 1, 1, 2),
    _FsPtpUnicastMasterAddLength_Type()
)
fsPtpUnicastMasterAddLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPtpUnicastMasterAddLength.setStatus("current")


class _FsPtpUnicastMasterAddr_Type(OctetString):
    """Custom type fsPtpUnicastMasterAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_FsPtpUnicastMasterAddr_Type.__name__ = "OctetString"
_FsPtpUnicastMasterAddr_Object = MibTableColumn
fsPtpUnicastMasterAddr = _FsPtpUnicastMasterAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 12, 1, 1, 3),
    _FsPtpUnicastMasterAddr_Type()
)
fsPtpUnicastMasterAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPtpUnicastMasterAddr.setStatus("current")
_FsPtpUnicastMasterRowStatus_Type = RowStatus
_FsPtpUnicastMasterRowStatus_Object = MibTableColumn
fsPtpUnicastMasterRowStatus = _FsPtpUnicastMasterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 12, 1, 1, 4),
    _FsPtpUnicastMasterRowStatus_Type()
)
fsPtpUnicastMasterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpUnicastMasterRowStatus.setStatus("current")
_FsPtpAccMasterDataSet_ObjectIdentity = ObjectIdentity
fsPtpAccMasterDataSet = _FsPtpAccMasterDataSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 13)
)
_FsPtpAccMasterDataSetTable_Object = MibTable
fsPtpAccMasterDataSetTable = _FsPtpAccMasterDataSetTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 13, 1)
)
if mibBuilder.loadTexts:
    fsPtpAccMasterDataSetTable.setStatus("current")
_FsPtpAccMasterDataSetEntry_Object = MibTableRow
fsPtpAccMasterDataSetEntry = _FsPtpAccMasterDataSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 13, 1, 1)
)
fsPtpAccMasterDataSetEntry.setIndexNames(
    (0, "SUPERMICRO-PTP-MIB", "fsPtpContextId"),
    (0, "SUPERMICRO-PTP-MIB", "fsPtpDomainNumber"),
    (0, "SUPERMICRO-PTP-MIB", "fsPtpAccMasterNetworkProtocol"),
    (0, "SUPERMICRO-PTP-MIB", "fsPtpAccMasterAddLength"),
    (0, "SUPERMICRO-PTP-MIB", "fsPtpAccMasterAddr"),
)
if mibBuilder.loadTexts:
    fsPtpAccMasterDataSetEntry.setStatus("current")


class _FsPtpAccMasterNetworkProtocol_Type(Integer32):
    """Custom type fsPtpAccMasterNetworkProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsPtpAccMasterNetworkProtocol_Type.__name__ = "Integer32"
_FsPtpAccMasterNetworkProtocol_Object = MibTableColumn
fsPtpAccMasterNetworkProtocol = _FsPtpAccMasterNetworkProtocol_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 13, 1, 1, 1),
    _FsPtpAccMasterNetworkProtocol_Type()
)
fsPtpAccMasterNetworkProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPtpAccMasterNetworkProtocol.setStatus("current")


class _FsPtpAccMasterAddLength_Type(Integer32):
    """Custom type fsPtpAccMasterAddLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FsPtpAccMasterAddLength_Type.__name__ = "Integer32"
_FsPtpAccMasterAddLength_Object = MibTableColumn
fsPtpAccMasterAddLength = _FsPtpAccMasterAddLength_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 13, 1, 1, 2),
    _FsPtpAccMasterAddLength_Type()
)
fsPtpAccMasterAddLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPtpAccMasterAddLength.setStatus("current")


class _FsPtpAccMasterAddr_Type(OctetString):
    """Custom type fsPtpAccMasterAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_FsPtpAccMasterAddr_Type.__name__ = "OctetString"
_FsPtpAccMasterAddr_Object = MibTableColumn
fsPtpAccMasterAddr = _FsPtpAccMasterAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 13, 1, 1, 3),
    _FsPtpAccMasterAddr_Type()
)
fsPtpAccMasterAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPtpAccMasterAddr.setStatus("current")
_FsPtpAccMasterAlternatePriority_Type = Integer32
_FsPtpAccMasterAlternatePriority_Object = MibTableColumn
fsPtpAccMasterAlternatePriority = _FsPtpAccMasterAlternatePriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 13, 1, 1, 4),
    _FsPtpAccMasterAlternatePriority_Type()
)
fsPtpAccMasterAlternatePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpAccMasterAlternatePriority.setStatus("current")
_FsPtpAccMasterRowStatus_Type = RowStatus
_FsPtpAccMasterRowStatus_Object = MibTableColumn
fsPtpAccMasterRowStatus = _FsPtpAccMasterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 13, 1, 1, 5),
    _FsPtpAccMasterRowStatus_Type()
)
fsPtpAccMasterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpAccMasterRowStatus.setStatus("current")
_FsPtpSecKeyDataSet_ObjectIdentity = ObjectIdentity
fsPtpSecKeyDataSet = _FsPtpSecKeyDataSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 14)
)
_FsPtpSecKeyDataSetTable_Object = MibTable
fsPtpSecKeyDataSetTable = _FsPtpSecKeyDataSetTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 14, 1)
)
if mibBuilder.loadTexts:
    fsPtpSecKeyDataSetTable.setStatus("current")
_FsPtpSecKeyDataSetEntry_Object = MibTableRow
fsPtpSecKeyDataSetEntry = _FsPtpSecKeyDataSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 14, 1, 1)
)
fsPtpSecKeyDataSetEntry.setIndexNames(
    (0, "SUPERMICRO-PTP-MIB", "fsPtpContextId"),
    (0, "SUPERMICRO-PTP-MIB", "fsPtpDomainNumber"),
    (0, "SUPERMICRO-PTP-MIB", "fsPtpSecKeyId"),
)
if mibBuilder.loadTexts:
    fsPtpSecKeyDataSetEntry.setStatus("current")


class _FsPtpSecKeyId_Type(Integer32):
    """Custom type fsPtpSecKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsPtpSecKeyId_Type.__name__ = "Integer32"
_FsPtpSecKeyId_Object = MibTableColumn
fsPtpSecKeyId = _FsPtpSecKeyId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 14, 1, 1, 1),
    _FsPtpSecKeyId_Type()
)
fsPtpSecKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPtpSecKeyId.setStatus("current")


class _FsPtpSecKeyAlgorithmId_Type(Integer32):
    """Custom type fsPtpSecKeyAlgorithmId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hmacSha196", 1),
          ("hmacSha256128", 2))
    )


_FsPtpSecKeyAlgorithmId_Type.__name__ = "Integer32"
_FsPtpSecKeyAlgorithmId_Object = MibTableColumn
fsPtpSecKeyAlgorithmId = _FsPtpSecKeyAlgorithmId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 14, 1, 1, 2),
    _FsPtpSecKeyAlgorithmId_Type()
)
fsPtpSecKeyAlgorithmId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpSecKeyAlgorithmId.setStatus("current")
_FsPtpSecKeyLength_Type = Integer32
_FsPtpSecKeyLength_Object = MibTableColumn
fsPtpSecKeyLength = _FsPtpSecKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 14, 1, 1, 3),
    _FsPtpSecKeyLength_Type()
)
fsPtpSecKeyLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpSecKeyLength.setStatus("current")
_FsPtpSecKey_Type = OctetString
_FsPtpSecKey_Object = MibTableColumn
fsPtpSecKey = _FsPtpSecKey_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 14, 1, 1, 4),
    _FsPtpSecKey_Type()
)
fsPtpSecKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpSecKey.setStatus("current")
_FsPtpSecKeyStartTime_Type = TimeStamp
_FsPtpSecKeyStartTime_Object = MibTableColumn
fsPtpSecKeyStartTime = _FsPtpSecKeyStartTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 14, 1, 1, 5),
    _FsPtpSecKeyStartTime_Type()
)
fsPtpSecKeyStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpSecKeyStartTime.setStatus("current")
_FsPtpSecKeyExpirationTime_Type = TimeStamp
_FsPtpSecKeyExpirationTime_Object = MibTableColumn
fsPtpSecKeyExpirationTime = _FsPtpSecKeyExpirationTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 14, 1, 1, 6),
    _FsPtpSecKeyExpirationTime_Type()
)
fsPtpSecKeyExpirationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpSecKeyExpirationTime.setStatus("current")


class _FsPtpSecKeyValid_Type(TruthValue):
    """Custom type fsPtpSecKeyValid based on TruthValue"""
    defaultValue = 2


_FsPtpSecKeyValid_Type.__name__ = "TruthValue"
_FsPtpSecKeyValid_Object = MibTableColumn
fsPtpSecKeyValid = _FsPtpSecKeyValid_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 14, 1, 1, 7),
    _FsPtpSecKeyValid_Type()
)
fsPtpSecKeyValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpSecKeyValid.setStatus("current")
_FsPtpSecKeyRowStatus_Type = RowStatus
_FsPtpSecKeyRowStatus_Object = MibTableColumn
fsPtpSecKeyRowStatus = _FsPtpSecKeyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 14, 1, 1, 8),
    _FsPtpSecKeyRowStatus_Type()
)
fsPtpSecKeyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPtpSecKeyRowStatus.setStatus("current")
_FsPtpSADataSet_ObjectIdentity = ObjectIdentity
fsPtpSADataSet = _FsPtpSADataSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 15)
)
_FsPtpSADataSetTable_Object = MibTable
fsPtpSADataSetTable = _FsPtpSADataSetTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 15, 1)
)
if mibBuilder.loadTexts:
    fsPtpSADataSetTable.setStatus("current")
_FsPtpSADataSetEntry_Object = MibTableRow
fsPtpSADataSetEntry = _FsPtpSADataSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 15, 1, 1)
)
fsPtpSADataSetEntry.setIndexNames(
    (0, "SUPERMICRO-PTP-MIB", "fsPtpContextId"),
    (0, "SUPERMICRO-PTP-MIB", "fsPtpDomainNumber"),
    (0, "SUPERMICRO-PTP-MIB", "fsPtpSAId"),
)
if mibBuilder.loadTexts:
    fsPtpSADataSetEntry.setStatus("current")


class _FsPtpSAId_Type(Integer32):
    """Custom type fsPtpSAId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsPtpSAId_Type.__name__ = "Integer32"
_FsPtpSAId_Object = MibTableColumn
fsPtpSAId = _FsPtpSAId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 15, 1, 1, 1),
    _FsPtpSAId_Type()
)
fsPtpSAId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPtpSAId.setStatus("current")
_FsPtpSASrcPortNumber_Type = FsPtpPortNumber
_FsPtpSASrcPortNumber_Object = MibTableColumn
fsPtpSASrcPortNumber = _FsPtpSASrcPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 15, 1, 1, 2),
    _FsPtpSASrcPortNumber_Type()
)
fsPtpSASrcPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpSASrcPortNumber.setStatus("current")
_FsPtpSASrcAddrLength_Type = Integer32
_FsPtpSASrcAddrLength_Object = MibTableColumn
fsPtpSASrcAddrLength = _FsPtpSASrcAddrLength_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 15, 1, 1, 3),
    _FsPtpSASrcAddrLength_Type()
)
fsPtpSASrcAddrLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpSASrcAddrLength.setStatus("current")
_FsPtpSASrcAddr_Type = OctetString
_FsPtpSASrcAddr_Object = MibTableColumn
fsPtpSASrcAddr = _FsPtpSASrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 15, 1, 1, 4),
    _FsPtpSASrcAddr_Type()
)
fsPtpSASrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpSASrcAddr.setStatus("current")
_FsPtpSADstPortNumber_Type = FsPtpPortNumber
_FsPtpSADstPortNumber_Object = MibTableColumn
fsPtpSADstPortNumber = _FsPtpSADstPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 15, 1, 1, 5),
    _FsPtpSADstPortNumber_Type()
)
fsPtpSADstPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpSADstPortNumber.setStatus("current")
_FsPtpSADstAddrLength_Type = Integer32
_FsPtpSADstAddrLength_Object = MibTableColumn
fsPtpSADstAddrLength = _FsPtpSADstAddrLength_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 15, 1, 1, 6),
    _FsPtpSADstAddrLength_Type()
)
fsPtpSADstAddrLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpSADstAddrLength.setStatus("current")
_FsPtpSADstAddr_Type = OctetString
_FsPtpSADstAddr_Object = MibTableColumn
fsPtpSADstAddr = _FsPtpSADstAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 15, 1, 1, 7),
    _FsPtpSADstAddr_Type()
)
fsPtpSADstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpSADstAddr.setStatus("current")


class _FsPtpSASrcClockIdentity_Type(OctetString):
    """Custom type fsPtpSASrcClockIdentity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FsPtpSASrcClockIdentity_Type.__name__ = "OctetString"
_FsPtpSASrcClockIdentity_Object = MibTableColumn
fsPtpSASrcClockIdentity = _FsPtpSASrcClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 15, 1, 1, 8),
    _FsPtpSASrcClockIdentity_Type()
)
fsPtpSASrcClockIdentity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpSASrcClockIdentity.setStatus("current")


class _FsPtpSADstClockIdentity_Type(OctetString):
    """Custom type fsPtpSADstClockIdentity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FsPtpSADstClockIdentity_Type.__name__ = "OctetString"
_FsPtpSADstClockIdentity_Object = MibTableColumn
fsPtpSADstClockIdentity = _FsPtpSADstClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 15, 1, 1, 9),
    _FsPtpSADstClockIdentity_Type()
)
fsPtpSADstClockIdentity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpSADstClockIdentity.setStatus("current")
_FsPtpSAReplayCounter_Type = Integer32
_FsPtpSAReplayCounter_Object = MibTableColumn
fsPtpSAReplayCounter = _FsPtpSAReplayCounter_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 15, 1, 1, 10),
    _FsPtpSAReplayCounter_Type()
)
fsPtpSAReplayCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpSAReplayCounter.setStatus("current")
_FsPtpSALifeTimeId_Type = Integer32
_FsPtpSALifeTimeId_Object = MibTableColumn
fsPtpSALifeTimeId = _FsPtpSALifeTimeId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 15, 1, 1, 11),
    _FsPtpSALifeTimeId_Type()
)
fsPtpSALifeTimeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpSALifeTimeId.setStatus("current")
_FsPtpSAKeyId_Type = Integer32
_FsPtpSAKeyId_Object = MibTableColumn
fsPtpSAKeyId = _FsPtpSAKeyId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 15, 1, 1, 12),
    _FsPtpSAKeyId_Type()
)
fsPtpSAKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpSAKeyId.setStatus("current")
_FsPtpSANextLifeTimeId_Type = Integer32
_FsPtpSANextLifeTimeId_Object = MibTableColumn
fsPtpSANextLifeTimeId = _FsPtpSANextLifeTimeId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 15, 1, 1, 13),
    _FsPtpSANextLifeTimeId_Type()
)
fsPtpSANextLifeTimeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpSANextLifeTimeId.setStatus("current")
_FsPtpSANextKeyId_Type = Integer32
_FsPtpSANextKeyId_Object = MibTableColumn
fsPtpSANextKeyId = _FsPtpSANextKeyId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 15, 1, 1, 14),
    _FsPtpSANextKeyId_Type()
)
fsPtpSANextKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpSANextKeyId.setStatus("current")


class _FsPtpSATrustState_Type(Integer32):
    """Custom type fsPtpSATrustState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("untrusted", 0),
          ("trusted", 1))
    )


_FsPtpSATrustState_Type.__name__ = "Integer32"
_FsPtpSATrustState_Object = MibTableColumn
fsPtpSATrustState = _FsPtpSATrustState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 15, 1, 1, 15),
    _FsPtpSATrustState_Type()
)
fsPtpSATrustState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpSATrustState.setStatus("current")
_FsPtpSATrustTimer_Type = Integer32
_FsPtpSATrustTimer_Object = MibTableColumn
fsPtpSATrustTimer = _FsPtpSATrustTimer_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 15, 1, 1, 16),
    _FsPtpSATrustTimer_Type()
)
fsPtpSATrustTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpSATrustTimer.setStatus("current")
_FsPtpSATrustTimeout_Type = Integer32
_FsPtpSATrustTimeout_Object = MibTableColumn
fsPtpSATrustTimeout = _FsPtpSATrustTimeout_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 15, 1, 1, 17),
    _FsPtpSATrustTimeout_Type()
)
fsPtpSATrustTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpSATrustTimeout.setStatus("current")


class _FsPtpSAChallengeState_Type(Integer32):
    """Custom type fsPtpSAChallengeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("challenging", 1))
    )


_FsPtpSAChallengeState_Type.__name__ = "Integer32"
_FsPtpSAChallengeState_Object = MibTableColumn
fsPtpSAChallengeState = _FsPtpSAChallengeState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 15, 1, 1, 18),
    _FsPtpSAChallengeState_Type()
)
fsPtpSAChallengeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpSAChallengeState.setStatus("current")
_FsPtpSAChallengeTimer_Type = Integer32
_FsPtpSAChallengeTimer_Object = MibTableColumn
fsPtpSAChallengeTimer = _FsPtpSAChallengeTimer_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 15, 1, 1, 19),
    _FsPtpSAChallengeTimer_Type()
)
fsPtpSAChallengeTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpSAChallengeTimer.setStatus("current")
_FsPtpSAChallengeTimeOut_Type = Integer32
_FsPtpSAChallengeTimeOut_Object = MibTableColumn
fsPtpSAChallengeTimeOut = _FsPtpSAChallengeTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 15, 1, 1, 20),
    _FsPtpSAChallengeTimeOut_Type()
)
fsPtpSAChallengeTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpSAChallengeTimeOut.setStatus("current")
_FsPtpSARequestNonce_Type = Integer32
_FsPtpSARequestNonce_Object = MibTableColumn
fsPtpSARequestNonce = _FsPtpSARequestNonce_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 15, 1, 1, 21),
    _FsPtpSARequestNonce_Type()
)
fsPtpSARequestNonce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpSARequestNonce.setStatus("current")
_FsPtpSAResponseNonce_Type = Integer32
_FsPtpSAResponseNonce_Object = MibTableColumn
fsPtpSAResponseNonce = _FsPtpSAResponseNonce_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 15, 1, 1, 22),
    _FsPtpSAResponseNonce_Type()
)
fsPtpSAResponseNonce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpSAResponseNonce.setStatus("current")
_FsPtpSAChallengeRequired_Type = TruthValue
_FsPtpSAChallengeRequired_Object = MibTableColumn
fsPtpSAChallengeRequired = _FsPtpSAChallengeRequired_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 15, 1, 1, 23),
    _FsPtpSAChallengeRequired_Type()
)
fsPtpSAChallengeRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpSAChallengeRequired.setStatus("current")
_FsPtpSAResponseRequired_Type = TruthValue
_FsPtpSAResponseRequired_Object = MibTableColumn
fsPtpSAResponseRequired = _FsPtpSAResponseRequired_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 15, 1, 1, 24),
    _FsPtpSAResponseRequired_Type()
)
fsPtpSAResponseRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpSAResponseRequired.setStatus("current")


class _FsPtpSATypeField_Type(Integer32):
    """Custom type fsPtpSATypeField based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FsPtpSATypeField_Type.__name__ = "Integer32"
_FsPtpSATypeField_Object = MibTableColumn
fsPtpSATypeField = _FsPtpSATypeField_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 15, 1, 1, 25),
    _FsPtpSATypeField_Type()
)
fsPtpSATypeField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpSATypeField.setStatus("current")


class _FsPtpSADirection_Type(Integer32):
    """Custom type fsPtpSADirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("in", 0),
          ("out", 1))
    )


_FsPtpSADirection_Type.__name__ = "Integer32"
_FsPtpSADirection_Object = MibTableColumn
fsPtpSADirection = _FsPtpSADirection_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 15, 1, 1, 26),
    _FsPtpSADirection_Type()
)
fsPtpSADirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpSADirection.setStatus("current")
_FsPtpSARowStatus_Type = RowStatus
_FsPtpSARowStatus_Object = MibTableColumn
fsPtpSARowStatus = _FsPtpSARowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 15, 1, 1, 27),
    _FsPtpSARowStatus_Type()
)
fsPtpSARowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPtpSARowStatus.setStatus("current")
_FsPtpAltTimeScaleDataSet_ObjectIdentity = ObjectIdentity
fsPtpAltTimeScaleDataSet = _FsPtpAltTimeScaleDataSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 16)
)
_FsPtpAltTimeScaleDataSetTable_Object = MibTable
fsPtpAltTimeScaleDataSetTable = _FsPtpAltTimeScaleDataSetTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 16, 1)
)
if mibBuilder.loadTexts:
    fsPtpAltTimeScaleDataSetTable.setStatus("current")
_FsPtpAltTimeScaleDataSetEntry_Object = MibTableRow
fsPtpAltTimeScaleDataSetEntry = _FsPtpAltTimeScaleDataSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 16, 1, 1)
)
fsPtpAltTimeScaleDataSetEntry.setIndexNames(
    (0, "SUPERMICRO-PTP-MIB", "fsPtpContextId"),
    (0, "SUPERMICRO-PTP-MIB", "fsPtpDomainNumber"),
    (0, "SUPERMICRO-PTP-MIB", "fsPtpAltTimeScaleKeyId"),
)
if mibBuilder.loadTexts:
    fsPtpAltTimeScaleDataSetEntry.setStatus("current")


class _FsPtpAltTimeScaleKeyId_Type(Integer32):
    """Custom type fsPtpAltTimeScaleKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_FsPtpAltTimeScaleKeyId_Type.__name__ = "Integer32"
_FsPtpAltTimeScaleKeyId_Object = MibTableColumn
fsPtpAltTimeScaleKeyId = _FsPtpAltTimeScaleKeyId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 16, 1, 1, 1),
    _FsPtpAltTimeScaleKeyId_Type()
)
fsPtpAltTimeScaleKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPtpAltTimeScaleKeyId.setStatus("current")
_FsPtpAltTimeScalecurrentOffset_Type = Integer32
_FsPtpAltTimeScalecurrentOffset_Object = MibTableColumn
fsPtpAltTimeScalecurrentOffset = _FsPtpAltTimeScalecurrentOffset_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 16, 1, 1, 2),
    _FsPtpAltTimeScalecurrentOffset_Type()
)
fsPtpAltTimeScalecurrentOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpAltTimeScalecurrentOffset.setStatus("current")
_FsPtpAltTimeScalejumpSeconds_Type = Integer32
_FsPtpAltTimeScalejumpSeconds_Object = MibTableColumn
fsPtpAltTimeScalejumpSeconds = _FsPtpAltTimeScalejumpSeconds_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 16, 1, 1, 3),
    _FsPtpAltTimeScalejumpSeconds_Type()
)
fsPtpAltTimeScalejumpSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpAltTimeScalejumpSeconds.setStatus("current")


class _FsPtpAltTimeScaletimeOfNextJump_Type(OctetString):
    """Custom type fsPtpAltTimeScaletimeOfNextJump based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_FsPtpAltTimeScaletimeOfNextJump_Type.__name__ = "OctetString"
_FsPtpAltTimeScaletimeOfNextJump_Object = MibTableColumn
fsPtpAltTimeScaletimeOfNextJump = _FsPtpAltTimeScaletimeOfNextJump_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 16, 1, 1, 4),
    _FsPtpAltTimeScaletimeOfNextJump_Type()
)
fsPtpAltTimeScaletimeOfNextJump.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpAltTimeScaletimeOfNextJump.setStatus("current")


class _FsPtpAltTimeScaledisplayName_Type(OctetString):
    """Custom type fsPtpAltTimeScaledisplayName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_FsPtpAltTimeScaledisplayName_Type.__name__ = "OctetString"
_FsPtpAltTimeScaledisplayName_Object = MibTableColumn
fsPtpAltTimeScaledisplayName = _FsPtpAltTimeScaledisplayName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 16, 1, 1, 5),
    _FsPtpAltTimeScaledisplayName_Type()
)
fsPtpAltTimeScaledisplayName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpAltTimeScaledisplayName.setStatus("current")
_FsPtpAltTimeScaleRowStatus_Type = RowStatus
_FsPtpAltTimeScaleRowStatus_Object = MibTableColumn
fsPtpAltTimeScaleRowStatus = _FsPtpAltTimeScaleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 1, 16, 1, 1, 6),
    _FsPtpAltTimeScaleRowStatus_Type()
)
fsPtpAltTimeScaleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPtpAltTimeScaleRowStatus.setStatus("current")
_FsPtpNotifications_ObjectIdentity = ObjectIdentity
fsPtpNotifications = _FsPtpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 2)
)
_FsPtpTrap_ObjectIdentity = ObjectIdentity
fsPtpTrap = _FsPtpTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 2, 0)
)


class _FsPtpTrapContextName_Type(DisplayString):
    """Custom type fsPtpTrapContextName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsPtpTrapContextName_Type.__name__ = "DisplayString"
_FsPtpTrapContextName_Object = MibScalar
fsPtpTrapContextName = _FsPtpTrapContextName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 2, 1),
    _FsPtpTrapContextName_Type()
)
fsPtpTrapContextName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsPtpTrapContextName.setStatus("current")
_FsPtpTrapDomainNumber_Type = Integer32
_FsPtpTrapDomainNumber_Object = MibScalar
fsPtpTrapDomainNumber = _FsPtpTrapDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 2, 2),
    _FsPtpTrapDomainNumber_Type()
)
fsPtpTrapDomainNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsPtpTrapDomainNumber.setStatus("current")


class _FsPtpGlobalErrTrapType_Type(Integer32):
    """Custom type fsPtpGlobalErrTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("memfail", 1),
          ("bufffail", 2),
          ("syncfault", 3),
          ("accmasterfault", 4),
          ("gmfault", 5))
    )


_FsPtpGlobalErrTrapType_Type.__name__ = "Integer32"
_FsPtpGlobalErrTrapType_Object = MibScalar
fsPtpGlobalErrTrapType = _FsPtpGlobalErrTrapType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 2, 3),
    _FsPtpGlobalErrTrapType_Type()
)
fsPtpGlobalErrTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtpGlobalErrTrapType.setStatus("current")
_FsPtpNotification_Type = OctetString
_FsPtpNotification_Object = MibScalar
fsPtpNotification = _FsPtpNotification_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 2, 4),
    _FsPtpNotification_Type()
)
fsPtpNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtpNotification.setStatus("current")
fsPtpDomainDataSetEntry.registerAugmentions(
    ("SUPERMICRO-PTP-MIB",
     "fsPtpClockDataSetEntry")
)
fsPtpClockDataSetEntry.setIndexNames(*fsPtpDomainDataSetEntry.getIndexNames())
fsPtpDomainDataSetEntry.registerAugmentions(
    ("SUPERMICRO-PTP-MIB",
     "fsPtpCurrentDataSetEntry")
)
fsPtpCurrentDataSetEntry.setIndexNames(*fsPtpDomainDataSetEntry.getIndexNames())
fsPtpDomainDataSetEntry.registerAugmentions(
    ("SUPERMICRO-PTP-MIB",
     "fsPtpParentDataSetEntry")
)
fsPtpParentDataSetEntry.setIndexNames(*fsPtpDomainDataSetEntry.getIndexNames())
fsPtpDomainDataSetEntry.registerAugmentions(
    ("SUPERMICRO-PTP-MIB",
     "fsPtpTimeDataSetEntry")
)
fsPtpTimeDataSetEntry.setIndexNames(*fsPtpDomainDataSetEntry.getIndexNames())
fsPtpDomainDataSetEntry.registerAugmentions(
    ("SUPERMICRO-PTP-MIB",
     "fsPtpTransparentDataSetEntry")
)
fsPtpTransparentDataSetEntry.setIndexNames(*fsPtpDomainDataSetEntry.getIndexNames())

# Managed Objects groups


# Notification objects

fsPtpPortStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 2, 0, 1)
)
fsPtpPortStateChangeTrap.setObjects(
      *(("SUPERMICRO-PTP-MIB", "fsPtpTrapContextName"),
        ("SUPERMICRO-PTP-MIB", "fsPtpPortState"))
)
if mibBuilder.loadTexts:
    fsPtpPortStateChangeTrap.setStatus(
        "current"
    )

fsPtpGlobalErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 2, 0, 2)
)
fsPtpGlobalErrorTrap.setObjects(
    ("SUPERMICRO-PTP-MIB", "fsPtpGlobalErrTrapType")
)
if mibBuilder.loadTexts:
    fsPtpGlobalErrorTrap.setStatus(
        "current"
    )

fsPtpAdminChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 2, 0, 3)
)
fsPtpAdminChangeTrap.setObjects(
      *(("SUPERMICRO-PTP-MIB", "fsPtpTrapContextName"),
        ("SUPERMICRO-PTP-MIB", "fsPtpAdminStatus"))
)
if mibBuilder.loadTexts:
    fsPtpAdminChangeTrap.setStatus(
        "current"
    )

fsPtpSysCtrlChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 2, 0, 4)
)
fsPtpSysCtrlChangeTrap.setObjects(
      *(("SUPERMICRO-PTP-MIB", "fsPtpTrapContextName"),
        ("SUPERMICRO-PTP-MIB", "fsPtpContextRowStatus"))
)
if mibBuilder.loadTexts:
    fsPtpSysCtrlChangeTrap.setStatus(
        "current"
    )

fsPtpUnicastOptionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 2, 0, 5)
)
fsPtpUnicastOptionTrap.setObjects(
      *(("SUPERMICRO-PTP-MIB", "fsPtpTrapContextName"),
        ("SUPERMICRO-PTP-MIB", "fsPtpPortUnicastNegOption"))
)
if mibBuilder.loadTexts:
    fsPtpUnicastOptionTrap.setStatus(
        "current"
    )

fsPtpPortPtpStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 2, 0, 6)
)
fsPtpPortPtpStatusTrap.setObjects(
      *(("SUPERMICRO-PTP-MIB", "fsPtpTrapContextName"),
        ("SUPERMICRO-PTP-MIB", "fsPtpPortPtpStatus"))
)
if mibBuilder.loadTexts:
    fsPtpPortPtpStatusTrap.setStatus(
        "current"
    )

fsPtpSyncFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 2, 0, 7)
)
fsPtpSyncFaultTrap.setObjects(
      *(("SUPERMICRO-PTP-MIB", "fsPtpTrapContextName"),
        ("SUPERMICRO-PTP-MIB", "fsPtpTrapDomainNumber"),
        ("SUPERMICRO-PTP-MIB", "fsPtpGlobalErrTrapType"))
)
if mibBuilder.loadTexts:
    fsPtpSyncFaultTrap.setStatus(
        "current"
    )

fsPtpAccMasterFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 2, 0, 8)
)
fsPtpAccMasterFaultTrap.setObjects(
      *(("SUPERMICRO-PTP-MIB", "fsPtpTrapContextName"),
        ("SUPERMICRO-PTP-MIB", "fsPtpTrapDomainNumber"),
        ("SUPERMICRO-PTP-MIB", "fsPtpGlobalErrTrapType"))
)
if mibBuilder.loadTexts:
    fsPtpAccMasterFaultTrap.setStatus(
        "current"
    )

fsPtpGrandMasterFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 45, 2, 0, 9)
)
fsPtpGrandMasterFaultTrap.setObjects(
      *(("SUPERMICRO-PTP-MIB", "fsPtpTrapContextName"),
        ("SUPERMICRO-PTP-MIB", "fsPtpTrapDomainNumber"),
        ("SUPERMICRO-PTP-MIB", "fsPtpGlobalErrTrapType"))
)
if mibBuilder.loadTexts:
    fsPtpGrandMasterFaultTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-PTP-MIB",
    **{"FsPtpPortNumber": FsPtpPortNumber,
       "fsPtpMIB": fsPtpMIB,
       "fsPtpObjects": fsPtpObjects,
       "fsPtpGeneralGroup": fsPtpGeneralGroup,
       "fsPtpGlobalSysCtrl": fsPtpGlobalSysCtrl,
       "fsPtpGblTraceOption": fsPtpGblTraceOption,
       "fsPtpPrimaryContext": fsPtpPrimaryContext,
       "fsPtpTable": fsPtpTable,
       "fsPtpEntry": fsPtpEntry,
       "fsPtpContextId": fsPtpContextId,
       "fsPtpAdminStatus": fsPtpAdminStatus,
       "fsPtpTraceOption": fsPtpTraceOption,
       "fsPtpContextType": fsPtpContextType,
       "fsPtpPrimaryDomain": fsPtpPrimaryDomain,
       "fsPtpContextRowStatus": fsPtpContextRowStatus,
       "fsPtpDomainDataSet": fsPtpDomainDataSet,
       "fsPtpDomainDataSetTable": fsPtpDomainDataSetTable,
       "fsPtpDomainDataSetEntry": fsPtpDomainDataSetEntry,
       "fsPtpDomainNumber": fsPtpDomainNumber,
       "fsPtpDomainClockMode": fsPtpDomainClockMode,
       "fsPtpDomainClockIdentity": fsPtpDomainClockIdentity,
       "fsPtpDomainGMClusterQueryInterval": fsPtpDomainGMClusterQueryInterval,
       "fsPtpDomainRowStatus": fsPtpDomainRowStatus,
       "fsPtpDefaultDataSet": fsPtpDefaultDataSet,
       "fsPtpClockDataSetTable": fsPtpClockDataSetTable,
       "fsPtpClockDataSetEntry": fsPtpClockDataSetEntry,
       "fsPtpClockIdentity": fsPtpClockIdentity,
       "fsPtpClockTwoStepFlag": fsPtpClockTwoStepFlag,
       "fsPtpClockNumberPorts": fsPtpClockNumberPorts,
       "fsPtpClockClass": fsPtpClockClass,
       "fsPtpClockAccuracy": fsPtpClockAccuracy,
       "fsPtpClockOffsetScaledLogVariance": fsPtpClockOffsetScaledLogVariance,
       "fsPtpClockPriority1": fsPtpClockPriority1,
       "fsPtpClockPriority2": fsPtpClockPriority2,
       "fsPtpClockSlaveOnly": fsPtpClockSlaveOnly,
       "fsPtpClockPathTraceOption": fsPtpClockPathTraceOption,
       "fsPtpClockAccMasterMaxSize": fsPtpClockAccMasterMaxSize,
       "fsPtpClockSecurityEnabled": fsPtpClockSecurityEnabled,
       "fsPtpClockNumOfSA": fsPtpClockNumOfSA,
       "fsPtpCurrentDataSet": fsPtpCurrentDataSet,
       "fsPtpCurrentDataSetTable": fsPtpCurrentDataSetTable,
       "fsPtpCurrentDataSetEntry": fsPtpCurrentDataSetEntry,
       "fsPtpCurrentStepsRemoved": fsPtpCurrentStepsRemoved,
       "fsPtpCurrentOffsetFromMaster": fsPtpCurrentOffsetFromMaster,
       "fsPtpCurrentMeanPathDelay": fsPtpCurrentMeanPathDelay,
       "fsPtpCurrentMasterToSlaveDelay": fsPtpCurrentMasterToSlaveDelay,
       "fsPtpCurrentSlaveToMasterDelay": fsPtpCurrentSlaveToMasterDelay,
       "fsPtpParentDataSet": fsPtpParentDataSet,
       "fsPtpParentDataSetTable": fsPtpParentDataSetTable,
       "fsPtpParentDataSetEntry": fsPtpParentDataSetEntry,
       "fsPtpParentClockIdentity": fsPtpParentClockIdentity,
       "fsPtpParentPortNumber": fsPtpParentPortNumber,
       "fsPtpParentStats": fsPtpParentStats,
       "fsPtpParentObservedOffsetScaledLogVariance": fsPtpParentObservedOffsetScaledLogVariance,
       "fsPtpParentObservedClockPhaseChangeRate": fsPtpParentObservedClockPhaseChangeRate,
       "fsPtpParentGMClockIdentity": fsPtpParentGMClockIdentity,
       "fsPtpParentGMClockClass": fsPtpParentGMClockClass,
       "fsPtpParentGMClockAccuracy": fsPtpParentGMClockAccuracy,
       "fsPtpParentGMClockOffsetScaledLogVariance": fsPtpParentGMClockOffsetScaledLogVariance,
       "fsPtpParentGMPriority1": fsPtpParentGMPriority1,
       "fsPtpParentGMPriority2": fsPtpParentGMPriority2,
       "fsPtpParentClockObservedDrift": fsPtpParentClockObservedDrift,
       "fsPtpGlobalTimeProportiesDataSet": fsPtpGlobalTimeProportiesDataSet,
       "fsPtpTimeDataSetTable": fsPtpTimeDataSetTable,
       "fsPtpTimeDataSetEntry": fsPtpTimeDataSetEntry,
       "fsPtpTimeCurrentUTCOffset": fsPtpTimeCurrentUTCOffset,
       "fsPtpTimeCurrentUTCOffsetValid": fsPtpTimeCurrentUTCOffsetValid,
       "fsPtpTimeLeap59": fsPtpTimeLeap59,
       "fsPtpTimeLeap61": fsPtpTimeLeap61,
       "fsPtpTimeTimeTraceable": fsPtpTimeTimeTraceable,
       "fsPtpTimeFrequencyTraceable": fsPtpTimeFrequencyTraceable,
       "fsPtpTimeTimeSource": fsPtpTimeTimeSource,
       "fsPtpPortConfigurationDataSet": fsPtpPortConfigurationDataSet,
       "fsPtpPortConfigDataSetTable": fsPtpPortConfigDataSetTable,
       "fsPtpPortConfigDataSetEntry": fsPtpPortConfigDataSetEntry,
       "fsPtpPortIndex": fsPtpPortIndex,
       "fsPtpPortClockIdentity": fsPtpPortClockIdentity,
       "fsPtpPortInterfaceType": fsPtpPortInterfaceType,
       "fsPtpPortIfaceNumber": fsPtpPortIfaceNumber,
       "fsPtpPortState": fsPtpPortState,
       "fsPtpPortMinDelayReqInterval": fsPtpPortMinDelayReqInterval,
       "fsPtpPortPeerMeanPathDelay": fsPtpPortPeerMeanPathDelay,
       "fsPtpPortAnnounceInterval": fsPtpPortAnnounceInterval,
       "fsPtpPortAnnounceReceiptTimeout": fsPtpPortAnnounceReceiptTimeout,
       "fsPtpPortSyncInterval": fsPtpPortSyncInterval,
       "fsPtpPortSynclimit": fsPtpPortSynclimit,
       "fsPtpPortDelayMechanism": fsPtpPortDelayMechanism,
       "fsPtpPortMinPdelayReqInterval": fsPtpPortMinPdelayReqInterval,
       "fsPtpPortVersionNumber": fsPtpPortVersionNumber,
       "fsPtpPortUnicastNegOption": fsPtpPortUnicastNegOption,
       "fsPtpPortUnicastMasterMaxSize": fsPtpPortUnicastMasterMaxSize,
       "fsPtpPortAccMasterEnabled": fsPtpPortAccMasterEnabled,
       "fsPtpPortNumOfAltMaster": fsPtpPortNumOfAltMaster,
       "fsPtpPortAltMulcastSync": fsPtpPortAltMulcastSync,
       "fsPtpPortAltMulcastSyncInterval": fsPtpPortAltMulcastSyncInterval,
       "fsPtpPortPtpStatus": fsPtpPortPtpStatus,
       "fsPtpPortRcvdAnnounceMsgCnt": fsPtpPortRcvdAnnounceMsgCnt,
       "fsPtpPortRcvdSyncMsgCnt": fsPtpPortRcvdSyncMsgCnt,
       "fsPtpPortRcvdDelayReqMsgCnt": fsPtpPortRcvdDelayReqMsgCnt,
       "fsPtpPortRcvdDelayRespMsgCnt": fsPtpPortRcvdDelayRespMsgCnt,
       "fsPtpPortTransDelayReqMsgCnt": fsPtpPortTransDelayReqMsgCnt,
       "fsPtpPortDiscardedMsgCnt": fsPtpPortDiscardedMsgCnt,
       "fsPtpPortRowStatus": fsPtpPortRowStatus,
       "fsPtpForeignMasterDataSet": fsPtpForeignMasterDataSet,
       "fsPtpForeignMasterDataSetTable": fsPtpForeignMasterDataSetTable,
       "fsPtpForeignMasterDataSetEntry": fsPtpForeignMasterDataSetEntry,
       "fsPtpForeignMasterClockIdentity": fsPtpForeignMasterClockIdentity,
       "fsPtpForeignMasterPortIndex": fsPtpForeignMasterPortIndex,
       "fsPtpForeignMasterAnnounceMsgs": fsPtpForeignMasterAnnounceMsgs,
       "fsPtpTransparentDataSet": fsPtpTransparentDataSet,
       "fsPtpTransparentDataSetTable": fsPtpTransparentDataSetTable,
       "fsPtpTransparentDataSetEntry": fsPtpTransparentDataSetEntry,
       "fsPtpTransparentClockIdentity": fsPtpTransparentClockIdentity,
       "fsPtpTransparentClockTwoStepFlag": fsPtpTransparentClockTwoStepFlag,
       "fsPtpTransparentClockNumberPorts": fsPtpTransparentClockNumberPorts,
       "fsPtpTransparentClockDelaymechanism": fsPtpTransparentClockDelaymechanism,
       "fsPtpTransparentClockPrimaryDomain": fsPtpTransparentClockPrimaryDomain,
       "fsPtpTransparentPortDataSet": fsPtpTransparentPortDataSet,
       "fsPtpTransparentPortDataSetTable": fsPtpTransparentPortDataSetTable,
       "fsPtpTransparentPortDataSetEntry": fsPtpTransparentPortDataSetEntry,
       "fsPtpTransparentPortIndex": fsPtpTransparentPortIndex,
       "fsPtpTransparentPortInterfaceType": fsPtpTransparentPortInterfaceType,
       "fsPtpTransparentPortIfaceNumber": fsPtpTransparentPortIfaceNumber,
       "fsPtpTransparentPortClockIdentity": fsPtpTransparentPortClockIdentity,
       "fsPtpTransparentPortMinPdelayReqInterval": fsPtpTransparentPortMinPdelayReqInterval,
       "fsPtpTransparentPortFaultyFlag": fsPtpTransparentPortFaultyFlag,
       "fsPtpTransparentPortPeerMeanPathDelay": fsPtpTransparentPortPeerMeanPathDelay,
       "fsPtpTransparentPortPtpStatus": fsPtpTransparentPortPtpStatus,
       "fsPtpTransparentPortRowStatus": fsPtpTransparentPortRowStatus,
       "fsPtpGrandMasterClusterDataSet": fsPtpGrandMasterClusterDataSet,
       "fsPtpGrandMasterClusterDataSetTable": fsPtpGrandMasterClusterDataSetTable,
       "fsPtpGrandMasterClusterDataSetEntry": fsPtpGrandMasterClusterDataSetEntry,
       "fsPtpGrandMasterClusterNetworkProtocol": fsPtpGrandMasterClusterNetworkProtocol,
       "fsPtpGrandMasterClusterAddLength": fsPtpGrandMasterClusterAddLength,
       "fsPtpGrandMasterClusterAddr": fsPtpGrandMasterClusterAddr,
       "fsPtpGrandMasterClusterRowStatus": fsPtpGrandMasterClusterRowStatus,
       "fsPtpUnicastMasterDataSet": fsPtpUnicastMasterDataSet,
       "fsPtpUnicastMasterDataSetTable": fsPtpUnicastMasterDataSetTable,
       "fsPtpUnicastMasterDataSetEntry": fsPtpUnicastMasterDataSetEntry,
       "fsPtpUnicastMasterNetworkProtocol": fsPtpUnicastMasterNetworkProtocol,
       "fsPtpUnicastMasterAddLength": fsPtpUnicastMasterAddLength,
       "fsPtpUnicastMasterAddr": fsPtpUnicastMasterAddr,
       "fsPtpUnicastMasterRowStatus": fsPtpUnicastMasterRowStatus,
       "fsPtpAccMasterDataSet": fsPtpAccMasterDataSet,
       "fsPtpAccMasterDataSetTable": fsPtpAccMasterDataSetTable,
       "fsPtpAccMasterDataSetEntry": fsPtpAccMasterDataSetEntry,
       "fsPtpAccMasterNetworkProtocol": fsPtpAccMasterNetworkProtocol,
       "fsPtpAccMasterAddLength": fsPtpAccMasterAddLength,
       "fsPtpAccMasterAddr": fsPtpAccMasterAddr,
       "fsPtpAccMasterAlternatePriority": fsPtpAccMasterAlternatePriority,
       "fsPtpAccMasterRowStatus": fsPtpAccMasterRowStatus,
       "fsPtpSecKeyDataSet": fsPtpSecKeyDataSet,
       "fsPtpSecKeyDataSetTable": fsPtpSecKeyDataSetTable,
       "fsPtpSecKeyDataSetEntry": fsPtpSecKeyDataSetEntry,
       "fsPtpSecKeyId": fsPtpSecKeyId,
       "fsPtpSecKeyAlgorithmId": fsPtpSecKeyAlgorithmId,
       "fsPtpSecKeyLength": fsPtpSecKeyLength,
       "fsPtpSecKey": fsPtpSecKey,
       "fsPtpSecKeyStartTime": fsPtpSecKeyStartTime,
       "fsPtpSecKeyExpirationTime": fsPtpSecKeyExpirationTime,
       "fsPtpSecKeyValid": fsPtpSecKeyValid,
       "fsPtpSecKeyRowStatus": fsPtpSecKeyRowStatus,
       "fsPtpSADataSet": fsPtpSADataSet,
       "fsPtpSADataSetTable": fsPtpSADataSetTable,
       "fsPtpSADataSetEntry": fsPtpSADataSetEntry,
       "fsPtpSAId": fsPtpSAId,
       "fsPtpSASrcPortNumber": fsPtpSASrcPortNumber,
       "fsPtpSASrcAddrLength": fsPtpSASrcAddrLength,
       "fsPtpSASrcAddr": fsPtpSASrcAddr,
       "fsPtpSADstPortNumber": fsPtpSADstPortNumber,
       "fsPtpSADstAddrLength": fsPtpSADstAddrLength,
       "fsPtpSADstAddr": fsPtpSADstAddr,
       "fsPtpSASrcClockIdentity": fsPtpSASrcClockIdentity,
       "fsPtpSADstClockIdentity": fsPtpSADstClockIdentity,
       "fsPtpSAReplayCounter": fsPtpSAReplayCounter,
       "fsPtpSALifeTimeId": fsPtpSALifeTimeId,
       "fsPtpSAKeyId": fsPtpSAKeyId,
       "fsPtpSANextLifeTimeId": fsPtpSANextLifeTimeId,
       "fsPtpSANextKeyId": fsPtpSANextKeyId,
       "fsPtpSATrustState": fsPtpSATrustState,
       "fsPtpSATrustTimer": fsPtpSATrustTimer,
       "fsPtpSATrustTimeout": fsPtpSATrustTimeout,
       "fsPtpSAChallengeState": fsPtpSAChallengeState,
       "fsPtpSAChallengeTimer": fsPtpSAChallengeTimer,
       "fsPtpSAChallengeTimeOut": fsPtpSAChallengeTimeOut,
       "fsPtpSARequestNonce": fsPtpSARequestNonce,
       "fsPtpSAResponseNonce": fsPtpSAResponseNonce,
       "fsPtpSAChallengeRequired": fsPtpSAChallengeRequired,
       "fsPtpSAResponseRequired": fsPtpSAResponseRequired,
       "fsPtpSATypeField": fsPtpSATypeField,
       "fsPtpSADirection": fsPtpSADirection,
       "fsPtpSARowStatus": fsPtpSARowStatus,
       "fsPtpAltTimeScaleDataSet": fsPtpAltTimeScaleDataSet,
       "fsPtpAltTimeScaleDataSetTable": fsPtpAltTimeScaleDataSetTable,
       "fsPtpAltTimeScaleDataSetEntry": fsPtpAltTimeScaleDataSetEntry,
       "fsPtpAltTimeScaleKeyId": fsPtpAltTimeScaleKeyId,
       "fsPtpAltTimeScalecurrentOffset": fsPtpAltTimeScalecurrentOffset,
       "fsPtpAltTimeScalejumpSeconds": fsPtpAltTimeScalejumpSeconds,
       "fsPtpAltTimeScaletimeOfNextJump": fsPtpAltTimeScaletimeOfNextJump,
       "fsPtpAltTimeScaledisplayName": fsPtpAltTimeScaledisplayName,
       "fsPtpAltTimeScaleRowStatus": fsPtpAltTimeScaleRowStatus,
       "fsPtpNotifications": fsPtpNotifications,
       "fsPtpTrap": fsPtpTrap,
       "fsPtpPortStateChangeTrap": fsPtpPortStateChangeTrap,
       "fsPtpGlobalErrorTrap": fsPtpGlobalErrorTrap,
       "fsPtpAdminChangeTrap": fsPtpAdminChangeTrap,
       "fsPtpSysCtrlChangeTrap": fsPtpSysCtrlChangeTrap,
       "fsPtpUnicastOptionTrap": fsPtpUnicastOptionTrap,
       "fsPtpPortPtpStatusTrap": fsPtpPortPtpStatusTrap,
       "fsPtpSyncFaultTrap": fsPtpSyncFaultTrap,
       "fsPtpAccMasterFaultTrap": fsPtpAccMasterFaultTrap,
       "fsPtpGrandMasterFaultTrap": fsPtpGrandMasterFaultTrap,
       "fsPtpTrapContextName": fsPtpTrapContextName,
       "fsPtpTrapDomainNumber": fsPtpTrapDomainNumber,
       "fsPtpGlobalErrTrapType": fsPtpGlobalErrTrapType,
       "fsPtpNotification": fsPtpNotification}
)
