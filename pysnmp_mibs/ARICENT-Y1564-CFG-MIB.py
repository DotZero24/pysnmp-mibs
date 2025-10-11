# SNMP MIB module (ARICENT-Y1564-CFG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-Y1564-CFG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:42:58 2025
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

(IEEE8021PriorityCodePoint,) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021PriorityCodePoint")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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

fsY1564 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88)
)
if mibBuilder.loadTexts:
    fsY1564.setRevisions(
        ("2014-06-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsY1564Context_ObjectIdentity = ObjectIdentity
fsY1564Context = _FsY1564Context_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 1)
)
_FsY1564ContextTable_Object = MibTable
fsY1564ContextTable = _FsY1564ContextTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 1, 1)
)
if mibBuilder.loadTexts:
    fsY1564ContextTable.setStatus("current")
_FsY1564ContextEntry_Object = MibTableRow
fsY1564ContextEntry = _FsY1564ContextEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 1, 1, 1)
)
fsY1564ContextEntry.setIndexNames(
    (0, "ARICENT-Y1564-CFG-MIB", "fsY1564ContextId"),
)
if mibBuilder.loadTexts:
    fsY1564ContextEntry.setStatus("current")
_FsY1564ContextId_Type = Unsigned32
_FsY1564ContextId_Object = MibTableColumn
fsY1564ContextId = _FsY1564ContextId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 1, 1, 1, 1),
    _FsY1564ContextId_Type()
)
fsY1564ContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsY1564ContextId.setStatus("current")


class _FsY1564ContextName_Type(DisplayString):
    """Custom type fsY1564ContextName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsY1564ContextName_Type.__name__ = "DisplayString"
_FsY1564ContextName_Object = MibTableColumn
fsY1564ContextName = _FsY1564ContextName_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 1, 1, 1, 2),
    _FsY1564ContextName_Type()
)
fsY1564ContextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564ContextName.setStatus("current")


class _FsY1564ContextSystemControl_Type(Integer32):
    """Custom type fsY1564ContextSystemControl based on Integer32"""
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


_FsY1564ContextSystemControl_Type.__name__ = "Integer32"
_FsY1564ContextSystemControl_Object = MibTableColumn
fsY1564ContextSystemControl = _FsY1564ContextSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 1, 1, 1, 3),
    _FsY1564ContextSystemControl_Type()
)
fsY1564ContextSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsY1564ContextSystemControl.setStatus("current")


class _FsY1564ContextModuleStatus_Type(Integer32):
    """Custom type fsY1564ContextModuleStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FsY1564ContextModuleStatus_Type.__name__ = "Integer32"
_FsY1564ContextModuleStatus_Object = MibTableColumn
fsY1564ContextModuleStatus = _FsY1564ContextModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 1, 1, 1, 4),
    _FsY1564ContextModuleStatus_Type()
)
fsY1564ContextModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsY1564ContextModuleStatus.setStatus("current")


class _FsY1564ContextTraceOption_Type(Unsigned32):
    """Custom type fsY1564ContextTraceOption based on Unsigned32"""
    defaultValue = 32

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsY1564ContextTraceOption_Type.__name__ = "Unsigned32"
_FsY1564ContextTraceOption_Object = MibTableColumn
fsY1564ContextTraceOption = _FsY1564ContextTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 1, 1, 1, 5),
    _FsY1564ContextTraceOption_Type()
)
fsY1564ContextTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsY1564ContextTraceOption.setStatus("current")


class _FsY1564ContextTrapStatus_Type(Integer32):
    """Custom type fsY1564ContextTrapStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FsY1564ContextTrapStatus_Type.__name__ = "Integer32"
_FsY1564ContextTrapStatus_Object = MibTableColumn
fsY1564ContextTrapStatus = _FsY1564ContextTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 1, 1, 1, 6),
    _FsY1564ContextTrapStatus_Type()
)
fsY1564ContextTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsY1564ContextTrapStatus.setStatus("current")
_FsY1564ContextNumOfConfTestRunning_Type = Unsigned32
_FsY1564ContextNumOfConfTestRunning_Object = MibTableColumn
fsY1564ContextNumOfConfTestRunning = _FsY1564ContextNumOfConfTestRunning_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 1, 1, 1, 7),
    _FsY1564ContextNumOfConfTestRunning_Type()
)
fsY1564ContextNumOfConfTestRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564ContextNumOfConfTestRunning.setStatus("current")
_FsY1564ContextNumOfPerfTestRunning_Type = Unsigned32
_FsY1564ContextNumOfPerfTestRunning_Object = MibTableColumn
fsY1564ContextNumOfPerfTestRunning = _FsY1564ContextNumOfPerfTestRunning_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 1, 1, 1, 8),
    _FsY1564ContextNumOfPerfTestRunning_Type()
)
fsY1564ContextNumOfPerfTestRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564ContextNumOfPerfTestRunning.setStatus("current")
_FsY1564Sla_ObjectIdentity = ObjectIdentity
fsY1564Sla = _FsY1564Sla_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 2)
)
_FsY1564SlaTable_Object = MibTable
fsY1564SlaTable = _FsY1564SlaTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 2, 1)
)
if mibBuilder.loadTexts:
    fsY1564SlaTable.setStatus("current")
_FsY1564SlaEntry_Object = MibTableRow
fsY1564SlaEntry = _FsY1564SlaEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 2, 1, 1)
)
fsY1564SlaEntry.setIndexNames(
    (0, "ARICENT-Y1564-CFG-MIB", "fsY1564ContextId"),
    (0, "ARICENT-Y1564-CFG-MIB", "fsY1564SlaId"),
)
if mibBuilder.loadTexts:
    fsY1564SlaEntry.setStatus("current")


class _FsY1564SlaId_Type(Unsigned32):
    """Custom type fsY1564SlaId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FsY1564SlaId_Type.__name__ = "Unsigned32"
_FsY1564SlaId_Object = MibTableColumn
fsY1564SlaId = _FsY1564SlaId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 2, 1, 1, 1),
    _FsY1564SlaId_Type()
)
fsY1564SlaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsY1564SlaId.setStatus("current")
_FsY1564SlaEvcIndex_Type = VlanId
_FsY1564SlaEvcIndex_Object = MibTableColumn
fsY1564SlaEvcIndex = _FsY1564SlaEvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 2, 1, 1, 2),
    _FsY1564SlaEvcIndex_Type()
)
fsY1564SlaEvcIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsY1564SlaEvcIndex.setStatus("current")


class _FsY1564SlaMEG_Type(Unsigned32):
    """Custom type fsY1564SlaMEG based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsY1564SlaMEG_Type.__name__ = "Unsigned32"
_FsY1564SlaMEG_Object = MibTableColumn
fsY1564SlaMEG = _FsY1564SlaMEG_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 2, 1, 1, 3),
    _FsY1564SlaMEG_Type()
)
fsY1564SlaMEG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsY1564SlaMEG.setStatus("current")


class _FsY1564SlaME_Type(Unsigned32):
    """Custom type fsY1564SlaME based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsY1564SlaME_Type.__name__ = "Unsigned32"
_FsY1564SlaME_Object = MibTableColumn
fsY1564SlaME = _FsY1564SlaME_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 2, 1, 1, 4),
    _FsY1564SlaME_Type()
)
fsY1564SlaME.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsY1564SlaME.setStatus("current")


class _FsY1564SlaMEP_Type(Unsigned32):
    """Custom type fsY1564SlaMEP based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_FsY1564SlaMEP_Type.__name__ = "Unsigned32"
_FsY1564SlaMEP_Object = MibTableColumn
fsY1564SlaMEP = _FsY1564SlaMEP_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 2, 1, 1, 5),
    _FsY1564SlaMEP_Type()
)
fsY1564SlaMEP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsY1564SlaMEP.setStatus("current")


class _FsY1564SlaSacId_Type(Unsigned32):
    """Custom type fsY1564SlaSacId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_FsY1564SlaSacId_Type.__name__ = "Unsigned32"
_FsY1564SlaSacId_Object = MibTableColumn
fsY1564SlaSacId = _FsY1564SlaSacId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 2, 1, 1, 6),
    _FsY1564SlaSacId_Type()
)
fsY1564SlaSacId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsY1564SlaSacId.setStatus("current")


class _FsY1564SlaTrafProfileId_Type(Unsigned32):
    """Custom type fsY1564SlaTrafProfileId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FsY1564SlaTrafProfileId_Type.__name__ = "Unsigned32"
_FsY1564SlaTrafProfileId_Object = MibTableColumn
fsY1564SlaTrafProfileId = _FsY1564SlaTrafProfileId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 2, 1, 1, 7),
    _FsY1564SlaTrafProfileId_Type()
)
fsY1564SlaTrafProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsY1564SlaTrafProfileId.setStatus("current")


class _FsY1564SlaStepLoadRate_Type(Integer32):
    """Custom type fsY1564SlaStepLoadRate based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_FsY1564SlaStepLoadRate_Type.__name__ = "Integer32"
_FsY1564SlaStepLoadRate_Object = MibTableColumn
fsY1564SlaStepLoadRate = _FsY1564SlaStepLoadRate_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 2, 1, 1, 8),
    _FsY1564SlaStepLoadRate_Type()
)
fsY1564SlaStepLoadRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsY1564SlaStepLoadRate.setStatus("current")


class _FsY1564SlaConfTestDuration_Type(Integer32):
    """Custom type fsY1564SlaConfTestDuration based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60),
    )


_FsY1564SlaConfTestDuration_Type.__name__ = "Integer32"
_FsY1564SlaConfTestDuration_Object = MibTableColumn
fsY1564SlaConfTestDuration = _FsY1564SlaConfTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 2, 1, 1, 9),
    _FsY1564SlaConfTestDuration_Type()
)
fsY1564SlaConfTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsY1564SlaConfTestDuration.setStatus("current")


class _FsY1564SlaTestStatus_Type(Integer32):
    """Custom type fsY1564SlaTestStatus based on Integer32"""
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
          ("stop", 2))
    )


_FsY1564SlaTestStatus_Type.__name__ = "Integer32"
_FsY1564SlaTestStatus_Object = MibTableColumn
fsY1564SlaTestStatus = _FsY1564SlaTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 2, 1, 1, 10),
    _FsY1564SlaTestStatus_Type()
)
fsY1564SlaTestStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsY1564SlaTestStatus.setStatus("current")


class _FsY1564SlaServiceConfId_Type(Unsigned32):
    """Custom type fsY1564SlaServiceConfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FsY1564SlaServiceConfId_Type.__name__ = "Unsigned32"
_FsY1564SlaServiceConfId_Object = MibTableColumn
fsY1564SlaServiceConfId = _FsY1564SlaServiceConfId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 2, 1, 1, 11),
    _FsY1564SlaServiceConfId_Type()
)
fsY1564SlaServiceConfId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsY1564SlaServiceConfId.setStatus("current")


class _FsY1564SlaColorMode_Type(Integer32):
    """Custom type fsY1564SlaColorMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("colorAware", 1),
          ("colorBlind", 2))
    )


_FsY1564SlaColorMode_Type.__name__ = "Integer32"
_FsY1564SlaColorMode_Object = MibTableColumn
fsY1564SlaColorMode = _FsY1564SlaColorMode_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 2, 1, 1, 12),
    _FsY1564SlaColorMode_Type()
)
fsY1564SlaColorMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564SlaColorMode.setStatus("current")
_FsY1564SlaCoupFlag_Type = TruthValue
_FsY1564SlaCoupFlag_Object = MibTableColumn
fsY1564SlaCoupFlag = _FsY1564SlaCoupFlag_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 2, 1, 1, 13),
    _FsY1564SlaCoupFlag_Type()
)
fsY1564SlaCoupFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564SlaCoupFlag.setStatus("current")


class _FsY1564SlaCIR_Type(Unsigned32):
    """Custom type fsY1564SlaCIR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10485760),
    )


_FsY1564SlaCIR_Type.__name__ = "Unsigned32"
_FsY1564SlaCIR_Object = MibTableColumn
fsY1564SlaCIR = _FsY1564SlaCIR_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 2, 1, 1, 14),
    _FsY1564SlaCIR_Type()
)
fsY1564SlaCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564SlaCIR.setStatus("current")


class _FsY1564SlaCBS_Type(Unsigned32):
    """Custom type fsY1564SlaCBS based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10485760),
    )


_FsY1564SlaCBS_Type.__name__ = "Unsigned32"
_FsY1564SlaCBS_Object = MibTableColumn
fsY1564SlaCBS = _FsY1564SlaCBS_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 2, 1, 1, 15),
    _FsY1564SlaCBS_Type()
)
fsY1564SlaCBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564SlaCBS.setStatus("current")
if mibBuilder.loadTexts:
    fsY1564SlaCBS.setUnits("Bytes")


class _FsY1564SlaEIR_Type(Unsigned32):
    """Custom type fsY1564SlaEIR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10485760),
    )


_FsY1564SlaEIR_Type.__name__ = "Unsigned32"
_FsY1564SlaEIR_Object = MibTableColumn
fsY1564SlaEIR = _FsY1564SlaEIR_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 2, 1, 1, 16),
    _FsY1564SlaEIR_Type()
)
fsY1564SlaEIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564SlaEIR.setStatus("current")


class _FsY1564SlaEBS_Type(Unsigned32):
    """Custom type fsY1564SlaEBS based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10485760),
    )


_FsY1564SlaEBS_Type.__name__ = "Unsigned32"
_FsY1564SlaEBS_Object = MibTableColumn
fsY1564SlaEBS = _FsY1564SlaEBS_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 2, 1, 1, 17),
    _FsY1564SlaEBS_Type()
)
fsY1564SlaEBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564SlaEBS.setStatus("current")
if mibBuilder.loadTexts:
    fsY1564SlaEBS.setUnits("Bytes")


class _FsY1564SlaTrafPolicing_Type(Integer32):
    """Custom type fsY1564SlaTrafPolicing based on Integer32"""
    defaultValue = 1

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


_FsY1564SlaTrafPolicing_Type.__name__ = "Integer32"
_FsY1564SlaTrafPolicing_Object = MibTableColumn
fsY1564SlaTrafPolicing = _FsY1564SlaTrafPolicing_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 2, 1, 1, 18),
    _FsY1564SlaTrafPolicing_Type()
)
fsY1564SlaTrafPolicing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsY1564SlaTrafPolicing.setStatus("current")


class _FsY1564SlaTestSelector_Type(Integer32):
    """Custom type fsY1564SlaTestSelector based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsY1564SlaTestSelector_Type.__name__ = "Integer32"
_FsY1564SlaTestSelector_Object = MibTableColumn
fsY1564SlaTestSelector = _FsY1564SlaTestSelector_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 2, 1, 1, 19),
    _FsY1564SlaTestSelector_Type()
)
fsY1564SlaTestSelector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsY1564SlaTestSelector.setStatus("current")


class _FsY1564SlaCurrentTestMode_Type(Integer32):
    """Custom type fsY1564SlaCurrentTestMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsY1564SlaCurrentTestMode_Type.__name__ = "Integer32"
_FsY1564SlaCurrentTestMode_Object = MibTableColumn
fsY1564SlaCurrentTestMode = _FsY1564SlaCurrentTestMode_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 2, 1, 1, 20),
    _FsY1564SlaCurrentTestMode_Type()
)
fsY1564SlaCurrentTestMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564SlaCurrentTestMode.setStatus("current")


class _FsY1564SlaCurrentTestState_Type(Integer32):
    """Custom type fsY1564SlaCurrentTestState based on Integer32"""
    defaultValue = 1

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
        *(("notInitiated", 1),
          ("completed", 2),
          ("inProgress", 3),
          ("aborted", 4))
    )


_FsY1564SlaCurrentTestState_Type.__name__ = "Integer32"
_FsY1564SlaCurrentTestState_Object = MibTableColumn
fsY1564SlaCurrentTestState = _FsY1564SlaCurrentTestState_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 2, 1, 1, 21),
    _FsY1564SlaCurrentTestState_Type()
)
fsY1564SlaCurrentTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564SlaCurrentTestState.setStatus("current")
_FsY1564SlaRowStatus_Type = RowStatus
_FsY1564SlaRowStatus_Object = MibTableColumn
fsY1564SlaRowStatus = _FsY1564SlaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 2, 1, 1, 22),
    _FsY1564SlaRowStatus_Type()
)
fsY1564SlaRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsY1564SlaRowStatus.setStatus("current")
_FsY1564TrafProf_ObjectIdentity = ObjectIdentity
fsY1564TrafProf = _FsY1564TrafProf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 3)
)
_FsY1564TrafProfTable_Object = MibTable
fsY1564TrafProfTable = _FsY1564TrafProfTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 3, 1)
)
if mibBuilder.loadTexts:
    fsY1564TrafProfTable.setStatus("current")
_FsY1564TrafProfEntry_Object = MibTableRow
fsY1564TrafProfEntry = _FsY1564TrafProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 3, 1, 1)
)
fsY1564TrafProfEntry.setIndexNames(
    (0, "ARICENT-Y1564-CFG-MIB", "fsY1564ContextId"),
    (0, "ARICENT-Y1564-CFG-MIB", "fsY1564TrafProfId"),
)
if mibBuilder.loadTexts:
    fsY1564TrafProfEntry.setStatus("current")


class _FsY1564TrafProfId_Type(Unsigned32):
    """Custom type fsY1564TrafProfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FsY1564TrafProfId_Type.__name__ = "Unsigned32"
_FsY1564TrafProfId_Object = MibTableColumn
fsY1564TrafProfId = _FsY1564TrafProfId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 3, 1, 1, 1),
    _FsY1564TrafProfId_Type()
)
fsY1564TrafProfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsY1564TrafProfId.setStatus("current")


class _FsY1564TrafProfDir_Type(Integer32):
    """Custom type fsY1564TrafProfDir based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("internal", 2))
    )


_FsY1564TrafProfDir_Type.__name__ = "Integer32"
_FsY1564TrafProfDir_Object = MibTableColumn
fsY1564TrafProfDir = _FsY1564TrafProfDir_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 3, 1, 1, 2),
    _FsY1564TrafProfDir_Type()
)
fsY1564TrafProfDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsY1564TrafProfDir.setStatus("current")


class _FsY1564TrafProfPktSize_Type(Integer32):
    """Custom type fsY1564TrafProfPktSize based on Integer32"""
    defaultValue = 512

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1518),
    )


_FsY1564TrafProfPktSize_Type.__name__ = "Integer32"
_FsY1564TrafProfPktSize_Object = MibTableColumn
fsY1564TrafProfPktSize = _FsY1564TrafProfPktSize_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 3, 1, 1, 3),
    _FsY1564TrafProfPktSize_Type()
)
fsY1564TrafProfPktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsY1564TrafProfPktSize.setStatus("current")


class _FsY1564TrafProfPayload_Type(OctetString):
    """Custom type fsY1564TrafProfPayload based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FsY1564TrafProfPayload_Type.__name__ = "OctetString"
_FsY1564TrafProfPayload_Object = MibTableColumn
fsY1564TrafProfPayload = _FsY1564TrafProfPayload_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 3, 1, 1, 4),
    _FsY1564TrafProfPayload_Type()
)
fsY1564TrafProfPayload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsY1564TrafProfPayload.setStatus("current")
_FsY1564TrafProfOptEmixPktSize_Type = DisplayString
_FsY1564TrafProfOptEmixPktSize_Object = MibTableColumn
fsY1564TrafProfOptEmixPktSize = _FsY1564TrafProfOptEmixPktSize_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 3, 1, 1, 5),
    _FsY1564TrafProfOptEmixPktSize_Type()
)
fsY1564TrafProfOptEmixPktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsY1564TrafProfOptEmixPktSize.setStatus("current")
_FsY1564TrafProfPCP_Type = IEEE8021PriorityCodePoint
_FsY1564TrafProfPCP_Object = MibTableColumn
fsY1564TrafProfPCP = _FsY1564TrafProfPCP_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 3, 1, 1, 6),
    _FsY1564TrafProfPCP_Type()
)
fsY1564TrafProfPCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsY1564TrafProfPCP.setStatus("current")
_FsY1564TrafProfRowStatus_Type = RowStatus
_FsY1564TrafProfRowStatus_Object = MibTableColumn
fsY1564TrafProfRowStatus = _FsY1564TrafProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 3, 1, 1, 7),
    _FsY1564TrafProfRowStatus_Type()
)
fsY1564TrafProfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsY1564TrafProfRowStatus.setStatus("current")
_FsY1564Sac_ObjectIdentity = ObjectIdentity
fsY1564Sac = _FsY1564Sac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 4)
)
_FsY1564SacTable_Object = MibTable
fsY1564SacTable = _FsY1564SacTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 4, 1)
)
if mibBuilder.loadTexts:
    fsY1564SacTable.setStatus("current")
_FsY1564SacEntry_Object = MibTableRow
fsY1564SacEntry = _FsY1564SacEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 4, 1, 1)
)
fsY1564SacEntry.setIndexNames(
    (0, "ARICENT-Y1564-CFG-MIB", "fsY1564ContextId"),
    (0, "ARICENT-Y1564-CFG-MIB", "fsY1564SacId"),
)
if mibBuilder.loadTexts:
    fsY1564SacEntry.setStatus("current")


class _FsY1564SacId_Type(Unsigned32):
    """Custom type fsY1564SacId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FsY1564SacId_Type.__name__ = "Unsigned32"
_FsY1564SacId_Object = MibTableColumn
fsY1564SacId = _FsY1564SacId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 4, 1, 1, 1),
    _FsY1564SacId_Type()
)
fsY1564SacId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsY1564SacId.setStatus("current")


class _FsY1564SacInfoRate_Type(Integer32):
    """Custom type fsY1564SacInfoRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FsY1564SacInfoRate_Type.__name__ = "Integer32"
_FsY1564SacInfoRate_Object = MibTableColumn
fsY1564SacInfoRate = _FsY1564SacInfoRate_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 4, 1, 1, 2),
    _FsY1564SacInfoRate_Type()
)
fsY1564SacInfoRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsY1564SacInfoRate.setStatus("current")


class _FsY1564SacFrLossRatio_Type(Integer32):
    """Custom type fsY1564SacFrLossRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsY1564SacFrLossRatio_Type.__name__ = "Integer32"
_FsY1564SacFrLossRatio_Object = MibTableColumn
fsY1564SacFrLossRatio = _FsY1564SacFrLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 4, 1, 1, 3),
    _FsY1564SacFrLossRatio_Type()
)
fsY1564SacFrLossRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsY1564SacFrLossRatio.setStatus("current")
_FsY1564SacFrTransDelay_Type = Integer32
_FsY1564SacFrTransDelay_Object = MibTableColumn
fsY1564SacFrTransDelay = _FsY1564SacFrTransDelay_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 4, 1, 1, 4),
    _FsY1564SacFrTransDelay_Type()
)
fsY1564SacFrTransDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsY1564SacFrTransDelay.setStatus("current")
_FsY1564SacFrDelayVar_Type = Integer32
_FsY1564SacFrDelayVar_Object = MibTableColumn
fsY1564SacFrDelayVar = _FsY1564SacFrDelayVar_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 4, 1, 1, 5),
    _FsY1564SacFrDelayVar_Type()
)
fsY1564SacFrDelayVar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsY1564SacFrDelayVar.setStatus("current")


class _FsY1564SacAvailability_Type(OctetString):
    """Custom type fsY1564SacAvailability based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_FsY1564SacAvailability_Type.__name__ = "OctetString"
_FsY1564SacAvailability_Object = MibTableColumn
fsY1564SacAvailability = _FsY1564SacAvailability_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 4, 1, 1, 6),
    _FsY1564SacAvailability_Type()
)
fsY1564SacAvailability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsY1564SacAvailability.setStatus("current")
_FsY1564SacRowStatus_Type = RowStatus
_FsY1564SacRowStatus_Object = MibTableColumn
fsY1564SacRowStatus = _FsY1564SacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 4, 1, 1, 7),
    _FsY1564SacRowStatus_Type()
)
fsY1564SacRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsY1564SacRowStatus.setStatus("current")
_FsY1564ServiceConf_ObjectIdentity = ObjectIdentity
fsY1564ServiceConf = _FsY1564ServiceConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 5)
)
_FsY1564ServiceConfTable_Object = MibTable
fsY1564ServiceConfTable = _FsY1564ServiceConfTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 5, 1)
)
if mibBuilder.loadTexts:
    fsY1564ServiceConfTable.setStatus("current")
_FsY1564ServiceConfEntry_Object = MibTableRow
fsY1564ServiceConfEntry = _FsY1564ServiceConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 5, 1, 1)
)
fsY1564ServiceConfEntry.setIndexNames(
    (0, "ARICENT-Y1564-CFG-MIB", "fsY1564ContextId"),
    (0, "ARICENT-Y1564-CFG-MIB", "fsY1564ServiceConfId"),
)
if mibBuilder.loadTexts:
    fsY1564ServiceConfEntry.setStatus("current")


class _FsY1564ServiceConfId_Type(Unsigned32):
    """Custom type fsY1564ServiceConfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FsY1564ServiceConfId_Type.__name__ = "Unsigned32"
_FsY1564ServiceConfId_Object = MibTableColumn
fsY1564ServiceConfId = _FsY1564ServiceConfId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 5, 1, 1, 1),
    _FsY1564ServiceConfId_Type()
)
fsY1564ServiceConfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsY1564ServiceConfId.setStatus("current")


class _FsY1564ServiceConfColorMode_Type(Integer32):
    """Custom type fsY1564ServiceConfColorMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("colorAware", 1),
          ("colorBlind", 2))
    )


_FsY1564ServiceConfColorMode_Type.__name__ = "Integer32"
_FsY1564ServiceConfColorMode_Object = MibTableColumn
fsY1564ServiceConfColorMode = _FsY1564ServiceConfColorMode_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 5, 1, 1, 2),
    _FsY1564ServiceConfColorMode_Type()
)
fsY1564ServiceConfColorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsY1564ServiceConfColorMode.setStatus("current")
_FsY1564ServiceConfCoupFlag_Type = TruthValue
_FsY1564ServiceConfCoupFlag_Object = MibTableColumn
fsY1564ServiceConfCoupFlag = _FsY1564ServiceConfCoupFlag_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 5, 1, 1, 3),
    _FsY1564ServiceConfCoupFlag_Type()
)
fsY1564ServiceConfCoupFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsY1564ServiceConfCoupFlag.setStatus("current")


class _FsY1564ServiceConfCIR_Type(Unsigned32):
    """Custom type fsY1564ServiceConfCIR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10485760),
    )


_FsY1564ServiceConfCIR_Type.__name__ = "Unsigned32"
_FsY1564ServiceConfCIR_Object = MibTableColumn
fsY1564ServiceConfCIR = _FsY1564ServiceConfCIR_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 5, 1, 1, 4),
    _FsY1564ServiceConfCIR_Type()
)
fsY1564ServiceConfCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsY1564ServiceConfCIR.setStatus("current")


class _FsY1564ServiceConfCBS_Type(Unsigned32):
    """Custom type fsY1564ServiceConfCBS based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10485760),
    )


_FsY1564ServiceConfCBS_Type.__name__ = "Unsigned32"
_FsY1564ServiceConfCBS_Object = MibTableColumn
fsY1564ServiceConfCBS = _FsY1564ServiceConfCBS_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 5, 1, 1, 5),
    _FsY1564ServiceConfCBS_Type()
)
fsY1564ServiceConfCBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsY1564ServiceConfCBS.setStatus("current")


class _FsY1564ServiceConfEIR_Type(Unsigned32):
    """Custom type fsY1564ServiceConfEIR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10485760),
    )


_FsY1564ServiceConfEIR_Type.__name__ = "Unsigned32"
_FsY1564ServiceConfEIR_Object = MibTableColumn
fsY1564ServiceConfEIR = _FsY1564ServiceConfEIR_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 5, 1, 1, 6),
    _FsY1564ServiceConfEIR_Type()
)
fsY1564ServiceConfEIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsY1564ServiceConfEIR.setStatus("current")


class _FsY1564ServiceConfEBS_Type(Unsigned32):
    """Custom type fsY1564ServiceConfEBS based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10485760),
    )


_FsY1564ServiceConfEBS_Type.__name__ = "Unsigned32"
_FsY1564ServiceConfEBS_Object = MibTableColumn
fsY1564ServiceConfEBS = _FsY1564ServiceConfEBS_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 5, 1, 1, 7),
    _FsY1564ServiceConfEBS_Type()
)
fsY1564ServiceConfEBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsY1564ServiceConfEBS.setStatus("current")
_FsY1564ServiceConfRowStatus_Type = RowStatus
_FsY1564ServiceConfRowStatus_Object = MibTableColumn
fsY1564ServiceConfRowStatus = _FsY1564ServiceConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 5, 1, 1, 8),
    _FsY1564ServiceConfRowStatus_Type()
)
fsY1564ServiceConfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsY1564ServiceConfRowStatus.setStatus("current")
_FsY1564ConfigTest_ObjectIdentity = ObjectIdentity
fsY1564ConfigTest = _FsY1564ConfigTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6)
)
_FsY1564ConfigTestReportTable_Object = MibTable
fsY1564ConfigTestReportTable = _FsY1564ConfigTestReportTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6, 1)
)
if mibBuilder.loadTexts:
    fsY1564ConfigTestReportTable.setStatus("current")
_FsY1564ConfigTestReportEntry_Object = MibTableRow
fsY1564ConfigTestReportEntry = _FsY1564ConfigTestReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6, 1, 1)
)
fsY1564ConfigTestReportEntry.setIndexNames(
    (0, "ARICENT-Y1564-CFG-MIB", "fsY1564ContextId"),
    (0, "ARICENT-Y1564-CFG-MIB", "fsY1564ConfigTestReportSlaId"),
    (0, "ARICENT-Y1564-CFG-MIB", "fsY1564ConfigTestReportFrSize"),
    (0, "ARICENT-Y1564-CFG-MIB", "fsY1564ConfigTestCurrentTestMode"),
    (0, "ARICENT-Y1564-CFG-MIB", "fsY1564ConfigTestReportStepId"),
)
if mibBuilder.loadTexts:
    fsY1564ConfigTestReportEntry.setStatus("current")


class _FsY1564ConfigTestReportSlaId_Type(Unsigned32):
    """Custom type fsY1564ConfigTestReportSlaId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FsY1564ConfigTestReportSlaId_Type.__name__ = "Unsigned32"
_FsY1564ConfigTestReportSlaId_Object = MibTableColumn
fsY1564ConfigTestReportSlaId = _FsY1564ConfigTestReportSlaId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6, 1, 1, 1),
    _FsY1564ConfigTestReportSlaId_Type()
)
fsY1564ConfigTestReportSlaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsY1564ConfigTestReportSlaId.setStatus("current")


class _FsY1564ConfigTestReportFrSize_Type(Integer32):
    """Custom type fsY1564ConfigTestReportFrSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1518),
    )


_FsY1564ConfigTestReportFrSize_Type.__name__ = "Integer32"
_FsY1564ConfigTestReportFrSize_Object = MibTableColumn
fsY1564ConfigTestReportFrSize = _FsY1564ConfigTestReportFrSize_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6, 1, 1, 2),
    _FsY1564ConfigTestReportFrSize_Type()
)
fsY1564ConfigTestReportFrSize.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsY1564ConfigTestReportFrSize.setStatus("current")


class _FsY1564ConfigTestCurrentTestMode_Type(Integer32):
    """Custom type fsY1564ConfigTestCurrentTestMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsY1564ConfigTestCurrentTestMode_Type.__name__ = "Integer32"
_FsY1564ConfigTestCurrentTestMode_Object = MibTableColumn
fsY1564ConfigTestCurrentTestMode = _FsY1564ConfigTestCurrentTestMode_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6, 1, 1, 3),
    _FsY1564ConfigTestCurrentTestMode_Type()
)
fsY1564ConfigTestCurrentTestMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsY1564ConfigTestCurrentTestMode.setStatus("current")


class _FsY1564ConfigTestReportStepId_Type(Integer32):
    """Custom type fsY1564ConfigTestReportStepId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FsY1564ConfigTestReportStepId_Type.__name__ = "Integer32"
_FsY1564ConfigTestReportStepId_Object = MibTableColumn
fsY1564ConfigTestReportStepId = _FsY1564ConfigTestReportStepId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6, 1, 1, 4),
    _FsY1564ConfigTestReportStepId_Type()
)
fsY1564ConfigTestReportStepId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsY1564ConfigTestReportStepId.setStatus("current")


class _FsY1564ConfigTestReportResult_Type(Integer32):
    """Custom type fsY1564ConfigTestReportResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("fail", 2))
    )


_FsY1564ConfigTestReportResult_Type.__name__ = "Integer32"
_FsY1564ConfigTestReportResult_Object = MibTableColumn
fsY1564ConfigTestReportResult = _FsY1564ConfigTestReportResult_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6, 1, 1, 5),
    _FsY1564ConfigTestReportResult_Type()
)
fsY1564ConfigTestReportResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564ConfigTestReportResult.setStatus("current")
_FsY1564ConfigTestReportIrMin_Type = Unsigned32
_FsY1564ConfigTestReportIrMin_Object = MibTableColumn
fsY1564ConfigTestReportIrMin = _FsY1564ConfigTestReportIrMin_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6, 1, 1, 6),
    _FsY1564ConfigTestReportIrMin_Type()
)
fsY1564ConfigTestReportIrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564ConfigTestReportIrMin.setStatus("current")
_FsY1564ConfigTestReportIrMean_Type = Unsigned32
_FsY1564ConfigTestReportIrMean_Object = MibTableColumn
fsY1564ConfigTestReportIrMean = _FsY1564ConfigTestReportIrMean_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6, 1, 1, 7),
    _FsY1564ConfigTestReportIrMean_Type()
)
fsY1564ConfigTestReportIrMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564ConfigTestReportIrMean.setStatus("current")
_FsY1564ConfigTestReportIrMax_Type = Unsigned32
_FsY1564ConfigTestReportIrMax_Object = MibTableColumn
fsY1564ConfigTestReportIrMax = _FsY1564ConfigTestReportIrMax_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6, 1, 1, 8),
    _FsY1564ConfigTestReportIrMax_Type()
)
fsY1564ConfigTestReportIrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564ConfigTestReportIrMax.setStatus("current")
_FsY1564ConfigTestReportFrLossCnt_Type = Unsigned32
_FsY1564ConfigTestReportFrLossCnt_Object = MibTableColumn
fsY1564ConfigTestReportFrLossCnt = _FsY1564ConfigTestReportFrLossCnt_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6, 1, 1, 9),
    _FsY1564ConfigTestReportFrLossCnt_Type()
)
fsY1564ConfigTestReportFrLossCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564ConfigTestReportFrLossCnt.setStatus("current")
_FsY1564ConfigTestReportFrLossRatio_Type = Unsigned32
_FsY1564ConfigTestReportFrLossRatio_Object = MibTableColumn
fsY1564ConfigTestReportFrLossRatio = _FsY1564ConfigTestReportFrLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6, 1, 1, 10),
    _FsY1564ConfigTestReportFrLossRatio_Type()
)
fsY1564ConfigTestReportFrLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564ConfigTestReportFrLossRatio.setStatus("current")
_FsY1564ConfigTestReportFrTxDelayMin_Type = Unsigned32
_FsY1564ConfigTestReportFrTxDelayMin_Object = MibTableColumn
fsY1564ConfigTestReportFrTxDelayMin = _FsY1564ConfigTestReportFrTxDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6, 1, 1, 11),
    _FsY1564ConfigTestReportFrTxDelayMin_Type()
)
fsY1564ConfigTestReportFrTxDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564ConfigTestReportFrTxDelayMin.setStatus("current")
_FsY1564ConfigTestReportFrTxDelayMean_Type = Unsigned32
_FsY1564ConfigTestReportFrTxDelayMean_Object = MibTableColumn
fsY1564ConfigTestReportFrTxDelayMean = _FsY1564ConfigTestReportFrTxDelayMean_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6, 1, 1, 12),
    _FsY1564ConfigTestReportFrTxDelayMean_Type()
)
fsY1564ConfigTestReportFrTxDelayMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564ConfigTestReportFrTxDelayMean.setStatus("current")
_FsY1564ConfigTestReportFrTxDelayMax_Type = Unsigned32
_FsY1564ConfigTestReportFrTxDelayMax_Object = MibTableColumn
fsY1564ConfigTestReportFrTxDelayMax = _FsY1564ConfigTestReportFrTxDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6, 1, 1, 13),
    _FsY1564ConfigTestReportFrTxDelayMax_Type()
)
fsY1564ConfigTestReportFrTxDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564ConfigTestReportFrTxDelayMax.setStatus("current")
_FsY1564ConfigTestReportFrDelayVarMin_Type = Unsigned32
_FsY1564ConfigTestReportFrDelayVarMin_Object = MibTableColumn
fsY1564ConfigTestReportFrDelayVarMin = _FsY1564ConfigTestReportFrDelayVarMin_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6, 1, 1, 14),
    _FsY1564ConfigTestReportFrDelayVarMin_Type()
)
fsY1564ConfigTestReportFrDelayVarMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564ConfigTestReportFrDelayVarMin.setStatus("current")
_FsY1564ConfigTestReportFrDelayVarMean_Type = Unsigned32
_FsY1564ConfigTestReportFrDelayVarMean_Object = MibTableColumn
fsY1564ConfigTestReportFrDelayVarMean = _FsY1564ConfigTestReportFrDelayVarMean_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6, 1, 1, 15),
    _FsY1564ConfigTestReportFrDelayVarMean_Type()
)
fsY1564ConfigTestReportFrDelayVarMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564ConfigTestReportFrDelayVarMean.setStatus("current")
_FsY1564ConfigTestReportFrDelayVarMax_Type = Unsigned32
_FsY1564ConfigTestReportFrDelayVarMax_Object = MibTableColumn
fsY1564ConfigTestReportFrDelayVarMax = _FsY1564ConfigTestReportFrDelayVarMax_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6, 1, 1, 16),
    _FsY1564ConfigTestReportFrDelayVarMax_Type()
)
fsY1564ConfigTestReportFrDelayVarMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564ConfigTestReportFrDelayVarMax.setStatus("current")
_FsY1564ConfigTestReportTestStartTime_Type = TimeStamp
_FsY1564ConfigTestReportTestStartTime_Object = MibTableColumn
fsY1564ConfigTestReportTestStartTime = _FsY1564ConfigTestReportTestStartTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6, 1, 1, 17),
    _FsY1564ConfigTestReportTestStartTime_Type()
)
fsY1564ConfigTestReportTestStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564ConfigTestReportTestStartTime.setStatus("current")
_FsY1564ConfigTestReportTestEndTime_Type = TimeStamp
_FsY1564ConfigTestReportTestEndTime_Object = MibTableColumn
fsY1564ConfigTestReportTestEndTime = _FsY1564ConfigTestReportTestEndTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6, 1, 1, 18),
    _FsY1564ConfigTestReportTestEndTime_Type()
)
fsY1564ConfigTestReportTestEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564ConfigTestReportTestEndTime.setStatus("current")
_FsY1564PerformanceTest_ObjectIdentity = ObjectIdentity
fsY1564PerformanceTest = _FsY1564PerformanceTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 7)
)
_FsY1564PerformanceTestTable_Object = MibTable
fsY1564PerformanceTestTable = _FsY1564PerformanceTestTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 7, 1)
)
if mibBuilder.loadTexts:
    fsY1564PerformanceTestTable.setStatus("current")
_FsY1564PerformanceTestEntry_Object = MibTableRow
fsY1564PerformanceTestEntry = _FsY1564PerformanceTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 7, 1, 1)
)
fsY1564PerformanceTestEntry.setIndexNames(
    (0, "ARICENT-Y1564-CFG-MIB", "fsY1564ContextId"),
    (0, "ARICENT-Y1564-CFG-MIB", "fsY1564PerformanceTestIndex"),
)
if mibBuilder.loadTexts:
    fsY1564PerformanceTestEntry.setStatus("current")


class _FsY1564PerformanceTestIndex_Type(Unsigned32):
    """Custom type fsY1564PerformanceTestIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FsY1564PerformanceTestIndex_Type.__name__ = "Unsigned32"
_FsY1564PerformanceTestIndex_Object = MibTableColumn
fsY1564PerformanceTestIndex = _FsY1564PerformanceTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 7, 1, 1, 1),
    _FsY1564PerformanceTestIndex_Type()
)
fsY1564PerformanceTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsY1564PerformanceTestIndex.setStatus("current")


class _FsY1564PerformanceTestSlaList_Type(OctetString):
    """Custom type fsY1564PerformanceTestSlaList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_FsY1564PerformanceTestSlaList_Type.__name__ = "OctetString"
_FsY1564PerformanceTestSlaList_Object = MibTableColumn
fsY1564PerformanceTestSlaList = _FsY1564PerformanceTestSlaList_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 7, 1, 1, 2),
    _FsY1564PerformanceTestSlaList_Type()
)
fsY1564PerformanceTestSlaList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsY1564PerformanceTestSlaList.setStatus("current")


class _FsY1564PerformanceTestDuration_Type(Integer32):
    """Custom type fsY1564PerformanceTestDuration based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("interval15min", 1),
          ("interval2hour", 2),
          ("interval24hour", 3))
    )


_FsY1564PerformanceTestDuration_Type.__name__ = "Integer32"
_FsY1564PerformanceTestDuration_Object = MibTableColumn
fsY1564PerformanceTestDuration = _FsY1564PerformanceTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 7, 1, 1, 3),
    _FsY1564PerformanceTestDuration_Type()
)
fsY1564PerformanceTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsY1564PerformanceTestDuration.setStatus("current")


class _FsY1564PerformanceTestStatus_Type(Integer32):
    """Custom type fsY1564PerformanceTestStatus based on Integer32"""
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
          ("stop", 2))
    )


_FsY1564PerformanceTestStatus_Type.__name__ = "Integer32"
_FsY1564PerformanceTestStatus_Object = MibTableColumn
fsY1564PerformanceTestStatus = _FsY1564PerformanceTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 7, 1, 1, 4),
    _FsY1564PerformanceTestStatus_Type()
)
fsY1564PerformanceTestStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsY1564PerformanceTestStatus.setStatus("current")
_FsY1564PerformanceTestRowStatus_Type = RowStatus
_FsY1564PerformanceTestRowStatus_Object = MibTableColumn
fsY1564PerformanceTestRowStatus = _FsY1564PerformanceTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 7, 1, 1, 5),
    _FsY1564PerformanceTestRowStatus_Type()
)
fsY1564PerformanceTestRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsY1564PerformanceTestRowStatus.setStatus("current")
_FsY1564PerfTestReport_ObjectIdentity = ObjectIdentity
fsY1564PerfTestReport = _FsY1564PerfTestReport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 8)
)
_FsY1564PerfTestReportTable_Object = MibTable
fsY1564PerfTestReportTable = _FsY1564PerfTestReportTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 8, 1)
)
if mibBuilder.loadTexts:
    fsY1564PerfTestReportTable.setStatus("current")
_FsY1564PerfTestReportEntry_Object = MibTableRow
fsY1564PerfTestReportEntry = _FsY1564PerfTestReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 8, 1, 1)
)
fsY1564PerfTestReportEntry.setIndexNames(
    (0, "ARICENT-Y1564-CFG-MIB", "fsY1564ContextId"),
    (0, "ARICENT-Y1564-CFG-MIB", "fsY1564SlaId"),
    (0, "ARICENT-Y1564-CFG-MIB", "fsY1564PerformanceTestIndex"),
    (0, "ARICENT-Y1564-CFG-MIB", "fsY1564PerfTestReportFrSize"),
)
if mibBuilder.loadTexts:
    fsY1564PerfTestReportEntry.setStatus("current")


class _FsY1564PerfTestReportFrSize_Type(Integer32):
    """Custom type fsY1564PerfTestReportFrSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1518),
    )


_FsY1564PerfTestReportFrSize_Type.__name__ = "Integer32"
_FsY1564PerfTestReportFrSize_Object = MibTableColumn
fsY1564PerfTestReportFrSize = _FsY1564PerfTestReportFrSize_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 8, 1, 1, 1),
    _FsY1564PerfTestReportFrSize_Type()
)
fsY1564PerfTestReportFrSize.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsY1564PerfTestReportFrSize.setStatus("current")


class _FsY1564PerfTestReportResult_Type(Integer32):
    """Custom type fsY1564PerfTestReportResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("fail", 2))
    )


_FsY1564PerfTestReportResult_Type.__name__ = "Integer32"
_FsY1564PerfTestReportResult_Object = MibTableColumn
fsY1564PerfTestReportResult = _FsY1564PerfTestReportResult_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 8, 1, 1, 2),
    _FsY1564PerfTestReportResult_Type()
)
fsY1564PerfTestReportResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564PerfTestReportResult.setStatus("current")
_FsY1564PerfTestReportIrMin_Type = Unsigned32
_FsY1564PerfTestReportIrMin_Object = MibTableColumn
fsY1564PerfTestReportIrMin = _FsY1564PerfTestReportIrMin_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 8, 1, 1, 3),
    _FsY1564PerfTestReportIrMin_Type()
)
fsY1564PerfTestReportIrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564PerfTestReportIrMin.setStatus("current")
_FsY1564PerfTestReportIrMean_Type = Unsigned32
_FsY1564PerfTestReportIrMean_Object = MibTableColumn
fsY1564PerfTestReportIrMean = _FsY1564PerfTestReportIrMean_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 8, 1, 1, 4),
    _FsY1564PerfTestReportIrMean_Type()
)
fsY1564PerfTestReportIrMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564PerfTestReportIrMean.setStatus("current")
_FsY1564PerfTestReportIrMax_Type = Unsigned32
_FsY1564PerfTestReportIrMax_Object = MibTableColumn
fsY1564PerfTestReportIrMax = _FsY1564PerfTestReportIrMax_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 8, 1, 1, 5),
    _FsY1564PerfTestReportIrMax_Type()
)
fsY1564PerfTestReportIrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564PerfTestReportIrMax.setStatus("current")
_FsY1564PerfTestReportFrLossCnt_Type = Unsigned32
_FsY1564PerfTestReportFrLossCnt_Object = MibTableColumn
fsY1564PerfTestReportFrLossCnt = _FsY1564PerfTestReportFrLossCnt_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 8, 1, 1, 6),
    _FsY1564PerfTestReportFrLossCnt_Type()
)
fsY1564PerfTestReportFrLossCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564PerfTestReportFrLossCnt.setStatus("current")
_FsY1564PerfTestReportFrLossRatio_Type = Unsigned32
_FsY1564PerfTestReportFrLossRatio_Object = MibTableColumn
fsY1564PerfTestReportFrLossRatio = _FsY1564PerfTestReportFrLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 8, 1, 1, 7),
    _FsY1564PerfTestReportFrLossRatio_Type()
)
fsY1564PerfTestReportFrLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564PerfTestReportFrLossRatio.setStatus("current")
_FsY1564PerfTestReportFrTxDelayMin_Type = Unsigned32
_FsY1564PerfTestReportFrTxDelayMin_Object = MibTableColumn
fsY1564PerfTestReportFrTxDelayMin = _FsY1564PerfTestReportFrTxDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 8, 1, 1, 8),
    _FsY1564PerfTestReportFrTxDelayMin_Type()
)
fsY1564PerfTestReportFrTxDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564PerfTestReportFrTxDelayMin.setStatus("current")
_FsY1564PerfTestReportFrTxDelayMean_Type = Unsigned32
_FsY1564PerfTestReportFrTxDelayMean_Object = MibTableColumn
fsY1564PerfTestReportFrTxDelayMean = _FsY1564PerfTestReportFrTxDelayMean_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 8, 1, 1, 9),
    _FsY1564PerfTestReportFrTxDelayMean_Type()
)
fsY1564PerfTestReportFrTxDelayMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564PerfTestReportFrTxDelayMean.setStatus("current")
_FsY1564PerfTestReportFrTxDelayMax_Type = Unsigned32
_FsY1564PerfTestReportFrTxDelayMax_Object = MibTableColumn
fsY1564PerfTestReportFrTxDelayMax = _FsY1564PerfTestReportFrTxDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 8, 1, 1, 10),
    _FsY1564PerfTestReportFrTxDelayMax_Type()
)
fsY1564PerfTestReportFrTxDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564PerfTestReportFrTxDelayMax.setStatus("current")
_FsY1564PerfTestReportFrDelayVarMin_Type = Unsigned32
_FsY1564PerfTestReportFrDelayVarMin_Object = MibTableColumn
fsY1564PerfTestReportFrDelayVarMin = _FsY1564PerfTestReportFrDelayVarMin_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 8, 1, 1, 11),
    _FsY1564PerfTestReportFrDelayVarMin_Type()
)
fsY1564PerfTestReportFrDelayVarMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564PerfTestReportFrDelayVarMin.setStatus("current")
_FsY1564PerfTestReportFrDelayVarMean_Type = Unsigned32
_FsY1564PerfTestReportFrDelayVarMean_Object = MibTableColumn
fsY1564PerfTestReportFrDelayVarMean = _FsY1564PerfTestReportFrDelayVarMean_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 8, 1, 1, 12),
    _FsY1564PerfTestReportFrDelayVarMean_Type()
)
fsY1564PerfTestReportFrDelayVarMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564PerfTestReportFrDelayVarMean.setStatus("current")
_FsY1564PerfTestReportFrDelayVarMax_Type = Unsigned32
_FsY1564PerfTestReportFrDelayVarMax_Object = MibTableColumn
fsY1564PerfTestReportFrDelayVarMax = _FsY1564PerfTestReportFrDelayVarMax_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 8, 1, 1, 13),
    _FsY1564PerfTestReportFrDelayVarMax_Type()
)
fsY1564PerfTestReportFrDelayVarMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564PerfTestReportFrDelayVarMax.setStatus("current")


class _FsY1564PerfTestReportAvailability_Type(OctetString):
    """Custom type fsY1564PerfTestReportAvailability based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_FsY1564PerfTestReportAvailability_Type.__name__ = "OctetString"
_FsY1564PerfTestReportAvailability_Object = MibTableColumn
fsY1564PerfTestReportAvailability = _FsY1564PerfTestReportAvailability_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 8, 1, 1, 14),
    _FsY1564PerfTestReportAvailability_Type()
)
fsY1564PerfTestReportAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564PerfTestReportAvailability.setStatus("current")
_FsY1564PerfTestReportUnavailableCount_Type = Unsigned32
_FsY1564PerfTestReportUnavailableCount_Object = MibTableColumn
fsY1564PerfTestReportUnavailableCount = _FsY1564PerfTestReportUnavailableCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 8, 1, 1, 15),
    _FsY1564PerfTestReportUnavailableCount_Type()
)
fsY1564PerfTestReportUnavailableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564PerfTestReportUnavailableCount.setStatus("current")
_FsY1564PerfTestReportTestStartTime_Type = TimeStamp
_FsY1564PerfTestReportTestStartTime_Object = MibTableColumn
fsY1564PerfTestReportTestStartTime = _FsY1564PerfTestReportTestStartTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 8, 1, 1, 16),
    _FsY1564PerfTestReportTestStartTime_Type()
)
fsY1564PerfTestReportTestStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564PerfTestReportTestStartTime.setStatus("current")
_FsY1564PerfTestReportTestEndTime_Type = TimeStamp
_FsY1564PerfTestReportTestEndTime_Object = MibTableColumn
fsY1564PerfTestReportTestEndTime = _FsY1564PerfTestReportTestEndTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 8, 1, 1, 17),
    _FsY1564PerfTestReportTestEndTime_Type()
)
fsY1564PerfTestReportTestEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsY1564PerfTestReportTestEndTime.setStatus("current")
_FsY1564Notification_ObjectIdentity = ObjectIdentity
fsY1564Notification = _FsY1564Notification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 9)
)
_FsY1564Traps_ObjectIdentity = ObjectIdentity
fsY1564Traps = _FsY1564Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 9, 0)
)
_FsY1564TrapObjects_ObjectIdentity = ObjectIdentity
fsY1564TrapObjects = _FsY1564TrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 9, 1)
)
_FsY1564TrapSlaId_Type = TruthValue
_FsY1564TrapSlaId_Object = MibScalar
fsY1564TrapSlaId = _FsY1564TrapSlaId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 9, 1, 1),
    _FsY1564TrapSlaId_Type()
)
fsY1564TrapSlaId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsY1564TrapSlaId.setStatus("current")


class _FsY1564TypeOfFailure_Type(DisplayString):
    """Custom type fsY1564TypeOfFailure based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsY1564TypeOfFailure_Type.__name__ = "DisplayString"
_FsY1564TypeOfFailure_Object = MibScalar
fsY1564TypeOfFailure = _FsY1564TypeOfFailure_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 9, 1, 2),
    _FsY1564TypeOfFailure_Type()
)
fsY1564TypeOfFailure.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsY1564TypeOfFailure.setStatus("current")

# Managed Objects groups


# Notification objects

fsY1564FailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 9, 0, 1)
)
fsY1564FailureTrap.setObjects(
      *(("ARICENT-Y1564-CFG-MIB", "fsY1564ContextName"),
        ("ARICENT-Y1564-CFG-MIB", "fsY1564TrapSlaId"),
        ("ARICENT-Y1564-CFG-MIB", "fsY1564TypeOfFailure"))
)
if mibBuilder.loadTexts:
    fsY1564FailureTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-Y1564-CFG-MIB",
    **{"fsY1564": fsY1564,
       "fsY1564Context": fsY1564Context,
       "fsY1564ContextTable": fsY1564ContextTable,
       "fsY1564ContextEntry": fsY1564ContextEntry,
       "fsY1564ContextId": fsY1564ContextId,
       "fsY1564ContextName": fsY1564ContextName,
       "fsY1564ContextSystemControl": fsY1564ContextSystemControl,
       "fsY1564ContextModuleStatus": fsY1564ContextModuleStatus,
       "fsY1564ContextTraceOption": fsY1564ContextTraceOption,
       "fsY1564ContextTrapStatus": fsY1564ContextTrapStatus,
       "fsY1564ContextNumOfConfTestRunning": fsY1564ContextNumOfConfTestRunning,
       "fsY1564ContextNumOfPerfTestRunning": fsY1564ContextNumOfPerfTestRunning,
       "fsY1564Sla": fsY1564Sla,
       "fsY1564SlaTable": fsY1564SlaTable,
       "fsY1564SlaEntry": fsY1564SlaEntry,
       "fsY1564SlaId": fsY1564SlaId,
       "fsY1564SlaEvcIndex": fsY1564SlaEvcIndex,
       "fsY1564SlaMEG": fsY1564SlaMEG,
       "fsY1564SlaME": fsY1564SlaME,
       "fsY1564SlaMEP": fsY1564SlaMEP,
       "fsY1564SlaSacId": fsY1564SlaSacId,
       "fsY1564SlaTrafProfileId": fsY1564SlaTrafProfileId,
       "fsY1564SlaStepLoadRate": fsY1564SlaStepLoadRate,
       "fsY1564SlaConfTestDuration": fsY1564SlaConfTestDuration,
       "fsY1564SlaTestStatus": fsY1564SlaTestStatus,
       "fsY1564SlaServiceConfId": fsY1564SlaServiceConfId,
       "fsY1564SlaColorMode": fsY1564SlaColorMode,
       "fsY1564SlaCoupFlag": fsY1564SlaCoupFlag,
       "fsY1564SlaCIR": fsY1564SlaCIR,
       "fsY1564SlaCBS": fsY1564SlaCBS,
       "fsY1564SlaEIR": fsY1564SlaEIR,
       "fsY1564SlaEBS": fsY1564SlaEBS,
       "fsY1564SlaTrafPolicing": fsY1564SlaTrafPolicing,
       "fsY1564SlaTestSelector": fsY1564SlaTestSelector,
       "fsY1564SlaCurrentTestMode": fsY1564SlaCurrentTestMode,
       "fsY1564SlaCurrentTestState": fsY1564SlaCurrentTestState,
       "fsY1564SlaRowStatus": fsY1564SlaRowStatus,
       "fsY1564TrafProf": fsY1564TrafProf,
       "fsY1564TrafProfTable": fsY1564TrafProfTable,
       "fsY1564TrafProfEntry": fsY1564TrafProfEntry,
       "fsY1564TrafProfId": fsY1564TrafProfId,
       "fsY1564TrafProfDir": fsY1564TrafProfDir,
       "fsY1564TrafProfPktSize": fsY1564TrafProfPktSize,
       "fsY1564TrafProfPayload": fsY1564TrafProfPayload,
       "fsY1564TrafProfOptEmixPktSize": fsY1564TrafProfOptEmixPktSize,
       "fsY1564TrafProfPCP": fsY1564TrafProfPCP,
       "fsY1564TrafProfRowStatus": fsY1564TrafProfRowStatus,
       "fsY1564Sac": fsY1564Sac,
       "fsY1564SacTable": fsY1564SacTable,
       "fsY1564SacEntry": fsY1564SacEntry,
       "fsY1564SacId": fsY1564SacId,
       "fsY1564SacInfoRate": fsY1564SacInfoRate,
       "fsY1564SacFrLossRatio": fsY1564SacFrLossRatio,
       "fsY1564SacFrTransDelay": fsY1564SacFrTransDelay,
       "fsY1564SacFrDelayVar": fsY1564SacFrDelayVar,
       "fsY1564SacAvailability": fsY1564SacAvailability,
       "fsY1564SacRowStatus": fsY1564SacRowStatus,
       "fsY1564ServiceConf": fsY1564ServiceConf,
       "fsY1564ServiceConfTable": fsY1564ServiceConfTable,
       "fsY1564ServiceConfEntry": fsY1564ServiceConfEntry,
       "fsY1564ServiceConfId": fsY1564ServiceConfId,
       "fsY1564ServiceConfColorMode": fsY1564ServiceConfColorMode,
       "fsY1564ServiceConfCoupFlag": fsY1564ServiceConfCoupFlag,
       "fsY1564ServiceConfCIR": fsY1564ServiceConfCIR,
       "fsY1564ServiceConfCBS": fsY1564ServiceConfCBS,
       "fsY1564ServiceConfEIR": fsY1564ServiceConfEIR,
       "fsY1564ServiceConfEBS": fsY1564ServiceConfEBS,
       "fsY1564ServiceConfRowStatus": fsY1564ServiceConfRowStatus,
       "fsY1564ConfigTest": fsY1564ConfigTest,
       "fsY1564ConfigTestReportTable": fsY1564ConfigTestReportTable,
       "fsY1564ConfigTestReportEntry": fsY1564ConfigTestReportEntry,
       "fsY1564ConfigTestReportSlaId": fsY1564ConfigTestReportSlaId,
       "fsY1564ConfigTestReportFrSize": fsY1564ConfigTestReportFrSize,
       "fsY1564ConfigTestCurrentTestMode": fsY1564ConfigTestCurrentTestMode,
       "fsY1564ConfigTestReportStepId": fsY1564ConfigTestReportStepId,
       "fsY1564ConfigTestReportResult": fsY1564ConfigTestReportResult,
       "fsY1564ConfigTestReportIrMin": fsY1564ConfigTestReportIrMin,
       "fsY1564ConfigTestReportIrMean": fsY1564ConfigTestReportIrMean,
       "fsY1564ConfigTestReportIrMax": fsY1564ConfigTestReportIrMax,
       "fsY1564ConfigTestReportFrLossCnt": fsY1564ConfigTestReportFrLossCnt,
       "fsY1564ConfigTestReportFrLossRatio": fsY1564ConfigTestReportFrLossRatio,
       "fsY1564ConfigTestReportFrTxDelayMin": fsY1564ConfigTestReportFrTxDelayMin,
       "fsY1564ConfigTestReportFrTxDelayMean": fsY1564ConfigTestReportFrTxDelayMean,
       "fsY1564ConfigTestReportFrTxDelayMax": fsY1564ConfigTestReportFrTxDelayMax,
       "fsY1564ConfigTestReportFrDelayVarMin": fsY1564ConfigTestReportFrDelayVarMin,
       "fsY1564ConfigTestReportFrDelayVarMean": fsY1564ConfigTestReportFrDelayVarMean,
       "fsY1564ConfigTestReportFrDelayVarMax": fsY1564ConfigTestReportFrDelayVarMax,
       "fsY1564ConfigTestReportTestStartTime": fsY1564ConfigTestReportTestStartTime,
       "fsY1564ConfigTestReportTestEndTime": fsY1564ConfigTestReportTestEndTime,
       "fsY1564PerformanceTest": fsY1564PerformanceTest,
       "fsY1564PerformanceTestTable": fsY1564PerformanceTestTable,
       "fsY1564PerformanceTestEntry": fsY1564PerformanceTestEntry,
       "fsY1564PerformanceTestIndex": fsY1564PerformanceTestIndex,
       "fsY1564PerformanceTestSlaList": fsY1564PerformanceTestSlaList,
       "fsY1564PerformanceTestDuration": fsY1564PerformanceTestDuration,
       "fsY1564PerformanceTestStatus": fsY1564PerformanceTestStatus,
       "fsY1564PerformanceTestRowStatus": fsY1564PerformanceTestRowStatus,
       "fsY1564PerfTestReport": fsY1564PerfTestReport,
       "fsY1564PerfTestReportTable": fsY1564PerfTestReportTable,
       "fsY1564PerfTestReportEntry": fsY1564PerfTestReportEntry,
       "fsY1564PerfTestReportFrSize": fsY1564PerfTestReportFrSize,
       "fsY1564PerfTestReportResult": fsY1564PerfTestReportResult,
       "fsY1564PerfTestReportIrMin": fsY1564PerfTestReportIrMin,
       "fsY1564PerfTestReportIrMean": fsY1564PerfTestReportIrMean,
       "fsY1564PerfTestReportIrMax": fsY1564PerfTestReportIrMax,
       "fsY1564PerfTestReportFrLossCnt": fsY1564PerfTestReportFrLossCnt,
       "fsY1564PerfTestReportFrLossRatio": fsY1564PerfTestReportFrLossRatio,
       "fsY1564PerfTestReportFrTxDelayMin": fsY1564PerfTestReportFrTxDelayMin,
       "fsY1564PerfTestReportFrTxDelayMean": fsY1564PerfTestReportFrTxDelayMean,
       "fsY1564PerfTestReportFrTxDelayMax": fsY1564PerfTestReportFrTxDelayMax,
       "fsY1564PerfTestReportFrDelayVarMin": fsY1564PerfTestReportFrDelayVarMin,
       "fsY1564PerfTestReportFrDelayVarMean": fsY1564PerfTestReportFrDelayVarMean,
       "fsY1564PerfTestReportFrDelayVarMax": fsY1564PerfTestReportFrDelayVarMax,
       "fsY1564PerfTestReportAvailability": fsY1564PerfTestReportAvailability,
       "fsY1564PerfTestReportUnavailableCount": fsY1564PerfTestReportUnavailableCount,
       "fsY1564PerfTestReportTestStartTime": fsY1564PerfTestReportTestStartTime,
       "fsY1564PerfTestReportTestEndTime": fsY1564PerfTestReportTestEndTime,
       "fsY1564Notification": fsY1564Notification,
       "fsY1564Traps": fsY1564Traps,
       "fsY1564FailureTrap": fsY1564FailureTrap,
       "fsY1564TrapObjects": fsY1564TrapObjects,
       "fsY1564TrapSlaId": fsY1564TrapSlaId,
       "fsY1564TypeOfFailure": fsY1564TypeOfFailure}
)
