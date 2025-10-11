# SNMP MIB module (NG700-GREENETHERNET-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/netgear/NG700-GREENETHERNET-PRIVATE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:26:35 2025
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

(ng700smartswitch,) = mibBuilder.importSymbols(
    "NETGEAR-REF-MIB",
    "ng700smartswitch")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

fastPathGreenEthernet = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 11, 500)
)
if mibBuilder.loadTexts:
    fastPathGreenEthernet.setRevisions(
        ("2019-07-12 15:00",
         "2011-05-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentGreenEthernet_ObjectIdentity = ObjectIdentity
agentGreenEthernet = _AgentGreenEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 11, 500, 1)
)
_AgentGreenEthernetTable_Object = MibTable
agentGreenEthernetTable = _AgentGreenEthernetTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 500, 1, 1)
)
if mibBuilder.loadTexts:
    agentGreenEthernetTable.setStatus("current")
_AgentGreenEthernetEntry_Object = MibTableRow
agentGreenEthernetEntry = _AgentGreenEthernetEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 500, 1, 1, 1)
)
agentGreenEthernetEntry.setIndexNames(
    (0, "NG700-GREENETHERNET-PRIVATE-MIB", "agentEthernetIntfIndex"),
)
if mibBuilder.loadTexts:
    agentGreenEthernetEntry.setStatus("current")


class _AgentEthernetIntfIndex_Type(Integer32):
    """Custom type agentEthernetIntfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_AgentEthernetIntfIndex_Type.__name__ = "Integer32"
_AgentEthernetIntfIndex_Object = MibTableColumn
agentEthernetIntfIndex = _AgentEthernetIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 500, 1, 1, 1, 1),
    _AgentEthernetIntfIndex_Type()
)
agentEthernetIntfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentEthernetIntfIndex.setStatus("current")


class _AgentGreenEnergyDetectMode_Type(Integer32):
    """Custom type agentGreenEnergyDetectMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AgentGreenEnergyDetectMode_Type.__name__ = "Integer32"
_AgentGreenEnergyDetectMode_Object = MibTableColumn
agentGreenEnergyDetectMode = _AgentGreenEnergyDetectMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 500, 1, 1, 1, 2),
    _AgentGreenEnergyDetectMode_Type()
)
agentGreenEnergyDetectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentGreenEnergyDetectMode.setStatus("current")


class _AgentGreenEnergyDetectOperStatus_Type(Integer32):
    """Custom type agentGreenEnergyDetectOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("in-active", 0),
          ("active", 1))
    )


_AgentGreenEnergyDetectOperStatus_Type.__name__ = "Integer32"
_AgentGreenEnergyDetectOperStatus_Object = MibTableColumn
agentGreenEnergyDetectOperStatus = _AgentGreenEnergyDetectOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 500, 1, 1, 1, 3),
    _AgentGreenEnergyDetectOperStatus_Type()
)
agentGreenEnergyDetectOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentGreenEnergyDetectOperStatus.setStatus("current")


class _AgentGreenEnergyDetectOperReason_Type(DisplayString):
    """Custom type agentGreenEnergyDetectOperReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AgentGreenEnergyDetectOperReason_Type.__name__ = "DisplayString"
_AgentGreenEnergyDetectOperReason_Object = MibTableColumn
agentGreenEnergyDetectOperReason = _AgentGreenEnergyDetectOperReason_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 500, 1, 1, 1, 4),
    _AgentGreenEnergyDetectOperReason_Type()
)
agentGreenEnergyDetectOperReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentGreenEnergyDetectOperReason.setStatus("current")


class _AgentGreenAutoShortReachMode_Type(Integer32):
    """Custom type agentGreenAutoShortReachMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AgentGreenAutoShortReachMode_Type.__name__ = "Integer32"
_AgentGreenAutoShortReachMode_Object = MibTableColumn
agentGreenAutoShortReachMode = _AgentGreenAutoShortReachMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 500, 1, 1, 1, 5),
    _AgentGreenAutoShortReachMode_Type()
)
agentGreenAutoShortReachMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentGreenAutoShortReachMode.setStatus("current")


class _AgentGreenForceShortReachMode_Type(Integer32):
    """Custom type agentGreenForceShortReachMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AgentGreenForceShortReachMode_Type.__name__ = "Integer32"
_AgentGreenForceShortReachMode_Object = MibTableColumn
agentGreenForceShortReachMode = _AgentGreenForceShortReachMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 500, 1, 1, 1, 6),
    _AgentGreenForceShortReachMode_Type()
)
agentGreenForceShortReachMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentGreenForceShortReachMode.setStatus("current")


class _AgentGreenShortReachOperStatus_Type(Integer32):
    """Custom type agentGreenShortReachOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("in-active", 2))
    )


_AgentGreenShortReachOperStatus_Type.__name__ = "Integer32"
_AgentGreenShortReachOperStatus_Object = MibTableColumn
agentGreenShortReachOperStatus = _AgentGreenShortReachOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 500, 1, 1, 1, 7),
    _AgentGreenShortReachOperStatus_Type()
)
agentGreenShortReachOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentGreenShortReachOperStatus.setStatus("current")


class _AgentGreenShortReachOperReason_Type(DisplayString):
    """Custom type agentGreenShortReachOperReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AgentGreenShortReachOperReason_Type.__name__ = "DisplayString"
_AgentGreenShortReachOperReason_Object = MibTableColumn
agentGreenShortReachOperReason = _AgentGreenShortReachOperReason_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 500, 1, 1, 1, 8),
    _AgentGreenShortReachOperReason_Type()
)
agentGreenShortReachOperReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentGreenShortReachOperReason.setStatus("current")


class _AgentGreenEeeMode_Type(Integer32):
    """Custom type agentGreenEeeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AgentGreenEeeMode_Type.__name__ = "Integer32"
_AgentGreenEeeMode_Object = MibTableColumn
agentGreenEeeMode = _AgentGreenEeeMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 500, 1, 1, 1, 9),
    _AgentGreenEeeMode_Type()
)
agentGreenEeeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentGreenEeeMode.setStatus("current")


class _AgentGreenEeeTxWakeTime_Type(Integer32):
    """Custom type agentGreenEeeTxWakeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2560),
    )


_AgentGreenEeeTxWakeTime_Type.__name__ = "Integer32"
_AgentGreenEeeTxWakeTime_Object = MibTableColumn
agentGreenEeeTxWakeTime = _AgentGreenEeeTxWakeTime_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 500, 1, 1, 1, 10),
    _AgentGreenEeeTxWakeTime_Type()
)
agentGreenEeeTxWakeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentGreenEeeTxWakeTime.setStatus("current")


class _AgentGreenEeeTxIdleTime_Type(Integer32):
    """Custom type agentGreenEeeTxIdleTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2560),
    )


_AgentGreenEeeTxIdleTime_Type.__name__ = "Integer32"
_AgentGreenEeeTxIdleTime_Object = MibTableColumn
agentGreenEeeTxIdleTime = _AgentGreenEeeTxIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 500, 1, 1, 1, 11),
    _AgentGreenEeeTxIdleTime_Type()
)
agentGreenEeeTxIdleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentGreenEeeTxIdleTime.setStatus("current")


class _AgentGreenCumEnergySaving_Type(Integer32):
    """Custom type agentGreenCumEnergySaving based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2560),
    )


_AgentGreenCumEnergySaving_Type.__name__ = "Integer32"
_AgentGreenCumEnergySaving_Object = MibTableColumn
agentGreenCumEnergySaving = _AgentGreenCumEnergySaving_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 500, 1, 1, 1, 12),
    _AgentGreenCumEnergySaving_Type()
)
agentGreenCumEnergySaving.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentGreenCumEnergySaving.setStatus("current")
_AgentGreenIntfEeeLpiHistoryTable_Object = MibTable
agentGreenIntfEeeLpiHistoryTable = _AgentGreenIntfEeeLpiHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 500, 1, 2)
)
if mibBuilder.loadTexts:
    agentGreenIntfEeeLpiHistoryTable.setStatus("current")
_AgentGreenIntfEeeLpiHistoryEntry_Object = MibTableRow
agentGreenIntfEeeLpiHistoryEntry = _AgentGreenIntfEeeLpiHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 500, 1, 2, 1)
)
agentGreenIntfEeeLpiHistoryEntry.setIndexNames(
    (0, "NG700-GREENETHERNET-PRIVATE-MIB", "agentGreenEeeLpiHistoryIntfIndex"),
    (0, "NG700-GREENETHERNET-PRIVATE-MIB", "agentGreenEeeLpiHistoryIntfSampleIndex"),
)
if mibBuilder.loadTexts:
    agentGreenIntfEeeLpiHistoryEntry.setStatus("current")


class _AgentGreenEeeLpiHistoryIntfIndex_Type(Integer32):
    """Custom type agentGreenEeeLpiHistoryIntfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_AgentGreenEeeLpiHistoryIntfIndex_Type.__name__ = "Integer32"
_AgentGreenEeeLpiHistoryIntfIndex_Object = MibTableColumn
agentGreenEeeLpiHistoryIntfIndex = _AgentGreenEeeLpiHistoryIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 500, 1, 2, 1, 1),
    _AgentGreenEeeLpiHistoryIntfIndex_Type()
)
agentGreenEeeLpiHistoryIntfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentGreenEeeLpiHistoryIntfIndex.setStatus("current")


class _AgentGreenEeeLpiHistoryIntfSampleIndex_Type(Integer32):
    """Custom type agentGreenEeeLpiHistoryIntfSampleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AgentGreenEeeLpiHistoryIntfSampleIndex_Type.__name__ = "Integer32"
_AgentGreenEeeLpiHistoryIntfSampleIndex_Object = MibTableColumn
agentGreenEeeLpiHistoryIntfSampleIndex = _AgentGreenEeeLpiHistoryIntfSampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 500, 1, 2, 1, 2),
    _AgentGreenEeeLpiHistoryIntfSampleIndex_Type()
)
agentGreenEeeLpiHistoryIntfSampleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentGreenEeeLpiHistoryIntfSampleIndex.setStatus("current")


class _AgentGreenEeeLpiHistoryIntfSampleTime_Type(DisplayString):
    """Custom type agentGreenEeeLpiHistoryIntfSampleTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AgentGreenEeeLpiHistoryIntfSampleTime_Type.__name__ = "DisplayString"
_AgentGreenEeeLpiHistoryIntfSampleTime_Object = MibTableColumn
agentGreenEeeLpiHistoryIntfSampleTime = _AgentGreenEeeLpiHistoryIntfSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 500, 1, 2, 1, 3),
    _AgentGreenEeeLpiHistoryIntfSampleTime_Type()
)
agentGreenEeeLpiHistoryIntfSampleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentGreenEeeLpiHistoryIntfSampleTime.setStatus("current")


class _AgentGreenEeeLpiHistoryIntfPercentLpiTime_Type(Integer32):
    """Custom type agentGreenEeeLpiHistoryIntfPercentLpiTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2560),
    )


_AgentGreenEeeLpiHistoryIntfPercentLpiTime_Type.__name__ = "Integer32"
_AgentGreenEeeLpiHistoryIntfPercentLpiTime_Object = MibTableColumn
agentGreenEeeLpiHistoryIntfPercentLpiTime = _AgentGreenEeeLpiHistoryIntfPercentLpiTime_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 500, 1, 2, 1, 4),
    _AgentGreenEeeLpiHistoryIntfPercentLpiTime_Type()
)
agentGreenEeeLpiHistoryIntfPercentLpiTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentGreenEeeLpiHistoryIntfPercentLpiTime.setStatus("current")


class _AgentGreenEeeLpiHistoryIntfPercentLpiTimeTotal_Type(Integer32):
    """Custom type agentGreenEeeLpiHistoryIntfPercentLpiTimeTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2560),
    )


_AgentGreenEeeLpiHistoryIntfPercentLpiTimeTotal_Type.__name__ = "Integer32"
_AgentGreenEeeLpiHistoryIntfPercentLpiTimeTotal_Object = MibTableColumn
agentGreenEeeLpiHistoryIntfPercentLpiTimeTotal = _AgentGreenEeeLpiHistoryIntfPercentLpiTimeTotal_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 500, 1, 2, 1, 5),
    _AgentGreenEeeLpiHistoryIntfPercentLpiTimeTotal_Type()
)
agentGreenEeeLpiHistoryIntfPercentLpiTimeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentGreenEeeLpiHistoryIntfPercentLpiTimeTotal.setStatus("current")
_AgentGreenUnitFeatureTable_Object = MibTable
agentGreenUnitFeatureTable = _AgentGreenUnitFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 500, 1, 3)
)
if mibBuilder.loadTexts:
    agentGreenUnitFeatureTable.setStatus("current")
_AgentGreenUnitFeatureEntry_Object = MibTableRow
agentGreenUnitFeatureEntry = _AgentGreenUnitFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 500, 1, 3, 1)
)
agentGreenUnitFeatureEntry.setIndexNames(
    (0, "NG700-GREENETHERNET-PRIVATE-MIB", "agentGreenUnitIndex"),
)
if mibBuilder.loadTexts:
    agentGreenUnitFeatureEntry.setStatus("current")


class _AgentGreenUnitIndex_Type(Integer32):
    """Custom type agentGreenUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AgentGreenUnitIndex_Type.__name__ = "Integer32"
_AgentGreenUnitIndex_Object = MibTableColumn
agentGreenUnitIndex = _AgentGreenUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 500, 1, 3, 1, 1),
    _AgentGreenUnitIndex_Type()
)
agentGreenUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentGreenUnitIndex.setStatus("current")


class _AgentGreenFeatureList_Type(DisplayString):
    """Custom type agentGreenFeatureList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_AgentGreenFeatureList_Type.__name__ = "DisplayString"
_AgentGreenFeatureList_Object = MibTableColumn
agentGreenFeatureList = _AgentGreenFeatureList_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 500, 1, 3, 1, 2),
    _AgentGreenFeatureList_Type()
)
agentGreenFeatureList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentGreenFeatureList.setStatus("current")


class _AgentGreenEeeLpiHistoryIntfSampleInterval_Type(Integer32):
    """Custom type agentGreenEeeLpiHistoryIntfSampleInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 36000),
    )


_AgentGreenEeeLpiHistoryIntfSampleInterval_Type.__name__ = "Integer32"
_AgentGreenEeeLpiHistoryIntfSampleInterval_Object = MibScalar
agentGreenEeeLpiHistoryIntfSampleInterval = _AgentGreenEeeLpiHistoryIntfSampleInterval_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 500, 1, 4),
    _AgentGreenEeeLpiHistoryIntfSampleInterval_Type()
)
agentGreenEeeLpiHistoryIntfSampleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentGreenEeeLpiHistoryIntfSampleInterval.setStatus("current")


class _AgentGreenEeeLpiHistoryIntfMaxSamples_Type(Integer32):
    """Custom type agentGreenEeeLpiHistoryIntfMaxSamples based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 168),
    )


_AgentGreenEeeLpiHistoryIntfMaxSamples_Type.__name__ = "Integer32"
_AgentGreenEeeLpiHistoryIntfMaxSamples_Object = MibScalar
agentGreenEeeLpiHistoryIntfMaxSamples = _AgentGreenEeeLpiHistoryIntfMaxSamples_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 500, 1, 5),
    _AgentGreenEeeLpiHistoryIntfMaxSamples_Type()
)
agentGreenEeeLpiHistoryIntfMaxSamples.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentGreenEeeLpiHistoryIntfMaxSamples.setStatus("current")


class _AgentGreenEeeLpiHistoryLpiTimePerStack_Type(Integer32):
    """Custom type agentGreenEeeLpiHistoryLpiTimePerStack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AgentGreenEeeLpiHistoryLpiTimePerStack_Type.__name__ = "Integer32"
_AgentGreenEeeLpiHistoryLpiTimePerStack_Object = MibScalar
agentGreenEeeLpiHistoryLpiTimePerStack = _AgentGreenEeeLpiHistoryLpiTimePerStack_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 500, 1, 6),
    _AgentGreenEeeLpiHistoryLpiTimePerStack_Type()
)
agentGreenEeeLpiHistoryLpiTimePerStack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentGreenEeeLpiHistoryLpiTimePerStack.setStatus("current")


class _AgentGreenStackCumEnergySaving_Type(Integer32):
    """Custom type agentGreenStackCumEnergySaving based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2560),
    )


_AgentGreenStackCumEnergySaving_Type.__name__ = "Integer32"
_AgentGreenStackCumEnergySaving_Object = MibScalar
agentGreenStackCumEnergySaving = _AgentGreenStackCumEnergySaving_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 500, 1, 7),
    _AgentGreenStackCumEnergySaving_Type()
)
agentGreenStackCumEnergySaving.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentGreenStackCumEnergySaving.setStatus("current")


class _AgentGreenStackCurPowerConsumption_Type(Integer32):
    """Custom type agentGreenStackCurPowerConsumption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2560),
    )


_AgentGreenStackCurPowerConsumption_Type.__name__ = "Integer32"
_AgentGreenStackCurPowerConsumption_Object = MibScalar
agentGreenStackCurPowerConsumption = _AgentGreenStackCurPowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 500, 1, 8),
    _AgentGreenStackCurPowerConsumption_Type()
)
agentGreenStackCurPowerConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentGreenStackCurPowerConsumption.setStatus("current")


class _AgentGreenStackPowerSaving_Type(Integer32):
    """Custom type agentGreenStackPowerSaving based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2560),
    )


_AgentGreenStackPowerSaving_Type.__name__ = "Integer32"
_AgentGreenStackPowerSaving_Object = MibScalar
agentGreenStackPowerSaving = _AgentGreenStackPowerSaving_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 500, 1, 9),
    _AgentGreenStackPowerSaving_Type()
)
agentGreenStackPowerSaving.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentGreenStackPowerSaving.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NG700-GREENETHERNET-PRIVATE-MIB",
    **{"fastPathGreenEthernet": fastPathGreenEthernet,
       "agentGreenEthernet": agentGreenEthernet,
       "agentGreenEthernetTable": agentGreenEthernetTable,
       "agentGreenEthernetEntry": agentGreenEthernetEntry,
       "agentEthernetIntfIndex": agentEthernetIntfIndex,
       "agentGreenEnergyDetectMode": agentGreenEnergyDetectMode,
       "agentGreenEnergyDetectOperStatus": agentGreenEnergyDetectOperStatus,
       "agentGreenEnergyDetectOperReason": agentGreenEnergyDetectOperReason,
       "agentGreenAutoShortReachMode": agentGreenAutoShortReachMode,
       "agentGreenForceShortReachMode": agentGreenForceShortReachMode,
       "agentGreenShortReachOperStatus": agentGreenShortReachOperStatus,
       "agentGreenShortReachOperReason": agentGreenShortReachOperReason,
       "agentGreenEeeMode": agentGreenEeeMode,
       "agentGreenEeeTxWakeTime": agentGreenEeeTxWakeTime,
       "agentGreenEeeTxIdleTime": agentGreenEeeTxIdleTime,
       "agentGreenCumEnergySaving": agentGreenCumEnergySaving,
       "agentGreenIntfEeeLpiHistoryTable": agentGreenIntfEeeLpiHistoryTable,
       "agentGreenIntfEeeLpiHistoryEntry": agentGreenIntfEeeLpiHistoryEntry,
       "agentGreenEeeLpiHistoryIntfIndex": agentGreenEeeLpiHistoryIntfIndex,
       "agentGreenEeeLpiHistoryIntfSampleIndex": agentGreenEeeLpiHistoryIntfSampleIndex,
       "agentGreenEeeLpiHistoryIntfSampleTime": agentGreenEeeLpiHistoryIntfSampleTime,
       "agentGreenEeeLpiHistoryIntfPercentLpiTime": agentGreenEeeLpiHistoryIntfPercentLpiTime,
       "agentGreenEeeLpiHistoryIntfPercentLpiTimeTotal": agentGreenEeeLpiHistoryIntfPercentLpiTimeTotal,
       "agentGreenUnitFeatureTable": agentGreenUnitFeatureTable,
       "agentGreenUnitFeatureEntry": agentGreenUnitFeatureEntry,
       "agentGreenUnitIndex": agentGreenUnitIndex,
       "agentGreenFeatureList": agentGreenFeatureList,
       "agentGreenEeeLpiHistoryIntfSampleInterval": agentGreenEeeLpiHistoryIntfSampleInterval,
       "agentGreenEeeLpiHistoryIntfMaxSamples": agentGreenEeeLpiHistoryIntfMaxSamples,
       "agentGreenEeeLpiHistoryLpiTimePerStack": agentGreenEeeLpiHistoryLpiTimePerStack,
       "agentGreenStackCumEnergySaving": agentGreenStackCumEnergySaving,
       "agentGreenStackCurPowerConsumption": agentGreenStackCurPowerConsumption,
       "agentGreenStackPowerSaving": agentGreenStackPowerSaving}
)
