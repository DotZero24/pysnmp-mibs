# SNMP MIB module (ELTEX-MES-COUNTERS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-COUNTERS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:50:42 2025
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

(eltMesCountersMIB,) = mibBuilder.importSymbols(
    "ELTEX-MES-MNG-MIB",
    "eltMesCountersMIB")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

(rlQosAceTidxAclIndex,
 rlQosAceTidxIndex) = mibBuilder.importSymbols(
    "RADLAN-QOS-CLI-MIB",
    "rlQosAceTidxAclIndex",
    "rlQosAceTidxIndex")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesCountersMIBObjects_ObjectIdentity = ObjectIdentity
eltMesCountersMIBObjects = _EltMesCountersMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 8, 1)
)
_EltMesCountersGlobal_ObjectIdentity = ObjectIdentity
eltMesCountersGlobal = _EltMesCountersGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 8, 1, 1)
)
_EltMesCountersVlan_ObjectIdentity = ObjectIdentity
eltMesCountersVlan = _EltMesCountersVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 8, 1, 1, 1)
)


class _EltCountersVlanLowIn_Type(TruthValue):
    """Custom type eltCountersVlanLowIn based on TruthValue"""
    defaultValue = 2


_EltCountersVlanLowIn_Type.__name__ = "TruthValue"
_EltCountersVlanLowIn_Object = MibScalar
eltCountersVlanLowIn = _EltCountersVlanLowIn_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 8, 1, 1, 1, 1),
    _EltCountersVlanLowIn_Type()
)
eltCountersVlanLowIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltCountersVlanLowIn.setStatus("current")


class _EltCountersVlanHighIn_Type(TruthValue):
    """Custom type eltCountersVlanHighIn based on TruthValue"""
    defaultValue = 2


_EltCountersVlanHighIn_Type.__name__ = "TruthValue"
_EltCountersVlanHighIn_Object = MibScalar
eltCountersVlanHighIn = _EltCountersVlanHighIn_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 8, 1, 1, 1, 2),
    _EltCountersVlanHighIn_Type()
)
eltCountersVlanHighIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltCountersVlanHighIn.setStatus("current")


class _EltCountersVlanLowOut_Type(TruthValue):
    """Custom type eltCountersVlanLowOut based on TruthValue"""
    defaultValue = 2


_EltCountersVlanLowOut_Type.__name__ = "TruthValue"
_EltCountersVlanLowOut_Object = MibScalar
eltCountersVlanLowOut = _EltCountersVlanLowOut_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 8, 1, 1, 1, 3),
    _EltCountersVlanLowOut_Type()
)
eltCountersVlanLowOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltCountersVlanLowOut.setStatus("current")


class _EltCountersVlanHighOut_Type(TruthValue):
    """Custom type eltCountersVlanHighOut based on TruthValue"""
    defaultValue = 2


_EltCountersVlanHighOut_Type.__name__ = "TruthValue"
_EltCountersVlanHighOut_Object = MibScalar
eltCountersVlanHighOut = _EltCountersVlanHighOut_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 8, 1, 1, 1, 4),
    _EltCountersVlanHighOut_Type()
)
eltCountersVlanHighOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltCountersVlanHighOut.setStatus("current")


class _EltCountersVlanClear1to1023_Type(OctetString):
    """Custom type eltCountersVlanClear1to1023 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltCountersVlanClear1to1023_Type.__name__ = "OctetString"
_EltCountersVlanClear1to1023_Object = MibScalar
eltCountersVlanClear1to1023 = _EltCountersVlanClear1to1023_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 8, 1, 1, 1, 5),
    _EltCountersVlanClear1to1023_Type()
)
eltCountersVlanClear1to1023.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltCountersVlanClear1to1023.setStatus("current")


class _EltCountersVlanClear1024to2047_Type(OctetString):
    """Custom type eltCountersVlanClear1024to2047 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltCountersVlanClear1024to2047_Type.__name__ = "OctetString"
_EltCountersVlanClear1024to2047_Object = MibScalar
eltCountersVlanClear1024to2047 = _EltCountersVlanClear1024to2047_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 8, 1, 1, 1, 6),
    _EltCountersVlanClear1024to2047_Type()
)
eltCountersVlanClear1024to2047.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltCountersVlanClear1024to2047.setStatus("current")


class _EltCountersVlanClear2048to3071_Type(OctetString):
    """Custom type eltCountersVlanClear2048to3071 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltCountersVlanClear2048to3071_Type.__name__ = "OctetString"
_EltCountersVlanClear2048to3071_Object = MibScalar
eltCountersVlanClear2048to3071 = _EltCountersVlanClear2048to3071_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 8, 1, 1, 1, 7),
    _EltCountersVlanClear2048to3071_Type()
)
eltCountersVlanClear2048to3071.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltCountersVlanClear2048to3071.setStatus("current")


class _EltCountersVlanClear3072to4094_Type(OctetString):
    """Custom type eltCountersVlanClear3072to4094 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltCountersVlanClear3072to4094_Type.__name__ = "OctetString"
_EltCountersVlanClear3072to4094_Object = MibScalar
eltCountersVlanClear3072to4094 = _EltCountersVlanClear3072to4094_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 8, 1, 1, 1, 8),
    _EltCountersVlanClear3072to4094_Type()
)
eltCountersVlanClear3072to4094.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltCountersVlanClear3072to4094.setStatus("current")
_EltMesCountersQos_ObjectIdentity = ObjectIdentity
eltMesCountersQos = _EltMesCountersQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 8, 1, 1, 2)
)


class _EltCountersQosStatisticsEnable_Type(TruthValue):
    """Custom type eltCountersQosStatisticsEnable based on TruthValue"""
    defaultValue = 2


_EltCountersQosStatisticsEnable_Type.__name__ = "TruthValue"
_EltCountersQosStatisticsEnable_Object = MibScalar
eltCountersQosStatisticsEnable = _EltCountersQosStatisticsEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 8, 1, 1, 2, 1),
    _EltCountersQosStatisticsEnable_Type()
)
eltCountersQosStatisticsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltCountersQosStatisticsEnable.setStatus("current")


class _EltCountersQosStatisticsClear_Type(PortList):
    """Custom type eltCountersQosStatisticsClear based on PortList"""
    defaultHexValue = "00"


_EltCountersQosStatisticsClear_Type.__name__ = "PortList"
_EltCountersQosStatisticsClear_Object = MibScalar
eltCountersQosStatisticsClear = _EltCountersQosStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 8, 1, 1, 2, 2),
    _EltCountersQosStatisticsClear_Type()
)
eltCountersQosStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltCountersQosStatisticsClear.setStatus("current")
_EltMesCountersAce_ObjectIdentity = ObjectIdentity
eltMesCountersAce = _EltMesCountersAce_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 8, 1, 1, 3)
)


class _EltCountersPortAceStatisticsEnable_Type(TruthValue):
    """Custom type eltCountersPortAceStatisticsEnable based on TruthValue"""
    defaultValue = 2


_EltCountersPortAceStatisticsEnable_Type.__name__ = "TruthValue"
_EltCountersPortAceStatisticsEnable_Object = MibScalar
eltCountersPortAceStatisticsEnable = _EltCountersPortAceStatisticsEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 8, 1, 1, 3, 1),
    _EltCountersPortAceStatisticsEnable_Type()
)
eltCountersPortAceStatisticsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltCountersPortAceStatisticsEnable.setStatus("current")


class _EltCountersVlanAceStatisticsEnable_Type(TruthValue):
    """Custom type eltCountersVlanAceStatisticsEnable based on TruthValue"""
    defaultValue = 2


_EltCountersVlanAceStatisticsEnable_Type.__name__ = "TruthValue"
_EltCountersVlanAceStatisticsEnable_Object = MibScalar
eltCountersVlanAceStatisticsEnable = _EltCountersVlanAceStatisticsEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 8, 1, 1, 3, 2),
    _EltCountersVlanAceStatisticsEnable_Type()
)
eltCountersVlanAceStatisticsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltCountersVlanAceStatisticsEnable.setStatus("current")
_EltCountersAceStatisticsClear_Type = TruthValue
_EltCountersAceStatisticsClear_Object = MibScalar
eltCountersAceStatisticsClear = _EltCountersAceStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 8, 1, 1, 3, 3),
    _EltCountersAceStatisticsClear_Type()
)
eltCountersAceStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltCountersAceStatisticsClear.setStatus("current")
_EltMesCountersStatistics_ObjectIdentity = ObjectIdentity
eltMesCountersStatistics = _EltMesCountersStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 8, 1, 2)
)
_EltMesCountersQosStatistics_ObjectIdentity = ObjectIdentity
eltMesCountersQosStatistics = _EltMesCountersQosStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 8, 1, 2, 1)
)
_EltCountersQosIfQueueTable_Object = MibTable
eltCountersQosIfQueueTable = _EltCountersQosIfQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 8, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    eltCountersQosIfQueueTable.setStatus("current")
_EltCountersQosIfQueueEntry_Object = MibTableRow
eltCountersQosIfQueueEntry = _EltCountersQosIfQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 8, 1, 2, 1, 1, 1)
)
eltCountersQosIfQueueEntry.setIndexNames(
    (0, "ELTEX-MES-COUNTERS-MIB", "eltCountersQosIfIndex"),
    (0, "ELTEX-MES-COUNTERS-MIB", "eltCountersQosQueueIndex"),
    (0, "ELTEX-MES-COUNTERS-MIB", "eltCountersQosDP"),
)
if mibBuilder.loadTexts:
    eltCountersQosIfQueueEntry.setStatus("current")
_EltCountersQosIfIndex_Type = InterfaceIndex
_EltCountersQosIfIndex_Object = MibTableColumn
eltCountersQosIfIndex = _EltCountersQosIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 8, 1, 2, 1, 1, 1, 1),
    _EltCountersQosIfIndex_Type()
)
eltCountersQosIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltCountersQosIfIndex.setStatus("current")


class _EltCountersQosQueueIndex_Type(Integer32):
    """Custom type eltCountersQosQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_EltCountersQosQueueIndex_Type.__name__ = "Integer32"
_EltCountersQosQueueIndex_Object = MibTableColumn
eltCountersQosQueueIndex = _EltCountersQosQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 8, 1, 2, 1, 1, 1, 2),
    _EltCountersQosQueueIndex_Type()
)
eltCountersQosQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltCountersQosQueueIndex.setStatus("current")


class _EltCountersQosDP_Type(Integer32):
    """Custom type eltCountersQosDP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_EltCountersQosDP_Type.__name__ = "Integer32"
_EltCountersQosDP_Object = MibTableColumn
eltCountersQosDP = _EltCountersQosDP_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 8, 1, 2, 1, 1, 1, 3),
    _EltCountersQosDP_Type()
)
eltCountersQosDP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltCountersQosDP.setStatus("current")
_EltCountersQosOctetsDroppedCounter_Type = Counter64
_EltCountersQosOctetsDroppedCounter_Object = MibTableColumn
eltCountersQosOctetsDroppedCounter = _EltCountersQosOctetsDroppedCounter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 8, 1, 2, 1, 1, 1, 4),
    _EltCountersQosOctetsDroppedCounter_Type()
)
eltCountersQosOctetsDroppedCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltCountersQosOctetsDroppedCounter.setStatus("current")
_EltCountersQosPktsDroppedCounter_Type = Counter64
_EltCountersQosPktsDroppedCounter_Object = MibTableColumn
eltCountersQosPktsDroppedCounter = _EltCountersQosPktsDroppedCounter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 8, 1, 2, 1, 1, 1, 5),
    _EltCountersQosPktsDroppedCounter_Type()
)
eltCountersQosPktsDroppedCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltCountersQosPktsDroppedCounter.setStatus("current")
_EltCountersQosOctetsPassedCounter_Type = Counter64
_EltCountersQosOctetsPassedCounter_Object = MibTableColumn
eltCountersQosOctetsPassedCounter = _EltCountersQosOctetsPassedCounter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 8, 1, 2, 1, 1, 1, 6),
    _EltCountersQosOctetsPassedCounter_Type()
)
eltCountersQosOctetsPassedCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltCountersQosOctetsPassedCounter.setStatus("current")
_EltCountersQosPktsPassedCounter_Type = Counter64
_EltCountersQosPktsPassedCounter_Object = MibTableColumn
eltCountersQosPktsPassedCounter = _EltCountersQosPktsPassedCounter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 8, 1, 2, 1, 1, 1, 7),
    _EltCountersQosPktsPassedCounter_Type()
)
eltCountersQosPktsPassedCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltCountersQosPktsPassedCounter.setStatus("current")
_EltMesCountersAceStatistics_ObjectIdentity = ObjectIdentity
eltMesCountersAceStatistics = _EltMesCountersAceStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 8, 1, 2, 2)
)
_EltCountersAceTable_Object = MibTable
eltCountersAceTable = _EltCountersAceTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 8, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    eltCountersAceTable.setStatus("current")
_EltCountersAceEntry_Object = MibTableRow
eltCountersAceEntry = _EltCountersAceEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 8, 1, 2, 2, 1, 1)
)
eltCountersAceEntry.setIndexNames(
    (0, "RADLAN-QOS-CLI-MIB", "rlQosAceTidxAclIndex"),
    (0, "RADLAN-QOS-CLI-MIB", "rlQosAceTidxIndex"),
)
if mibBuilder.loadTexts:
    eltCountersAceEntry.setStatus("current")


class _EltCountersAceHitCounterStatus_Type(Integer32):
    """Custom type eltCountersAceHitCounterStatus based on Integer32"""
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


_EltCountersAceHitCounterStatus_Type.__name__ = "Integer32"
_EltCountersAceHitCounterStatus_Object = MibTableColumn
eltCountersAceHitCounterStatus = _EltCountersAceHitCounterStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 8, 1, 2, 2, 1, 1, 1),
    _EltCountersAceHitCounterStatus_Type()
)
eltCountersAceHitCounterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltCountersAceHitCounterStatus.setStatus("current")
_EltCountersAceHitCounterValue_Type = Counter64
_EltCountersAceHitCounterValue_Object = MibTableColumn
eltCountersAceHitCounterValue = _EltCountersAceHitCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 8, 1, 2, 2, 1, 1, 2),
    _EltCountersAceHitCounterValue_Type()
)
eltCountersAceHitCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltCountersAceHitCounterValue.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-COUNTERS-MIB",
    **{"eltMesCountersMIBObjects": eltMesCountersMIBObjects,
       "eltMesCountersGlobal": eltMesCountersGlobal,
       "eltMesCountersVlan": eltMesCountersVlan,
       "eltCountersVlanLowIn": eltCountersVlanLowIn,
       "eltCountersVlanHighIn": eltCountersVlanHighIn,
       "eltCountersVlanLowOut": eltCountersVlanLowOut,
       "eltCountersVlanHighOut": eltCountersVlanHighOut,
       "eltCountersVlanClear1to1023": eltCountersVlanClear1to1023,
       "eltCountersVlanClear1024to2047": eltCountersVlanClear1024to2047,
       "eltCountersVlanClear2048to3071": eltCountersVlanClear2048to3071,
       "eltCountersVlanClear3072to4094": eltCountersVlanClear3072to4094,
       "eltMesCountersQos": eltMesCountersQos,
       "eltCountersQosStatisticsEnable": eltCountersQosStatisticsEnable,
       "eltCountersQosStatisticsClear": eltCountersQosStatisticsClear,
       "eltMesCountersAce": eltMesCountersAce,
       "eltCountersPortAceStatisticsEnable": eltCountersPortAceStatisticsEnable,
       "eltCountersVlanAceStatisticsEnable": eltCountersVlanAceStatisticsEnable,
       "eltCountersAceStatisticsClear": eltCountersAceStatisticsClear,
       "eltMesCountersStatistics": eltMesCountersStatistics,
       "eltMesCountersQosStatistics": eltMesCountersQosStatistics,
       "eltCountersQosIfQueueTable": eltCountersQosIfQueueTable,
       "eltCountersQosIfQueueEntry": eltCountersQosIfQueueEntry,
       "eltCountersQosIfIndex": eltCountersQosIfIndex,
       "eltCountersQosQueueIndex": eltCountersQosQueueIndex,
       "eltCountersQosDP": eltCountersQosDP,
       "eltCountersQosOctetsDroppedCounter": eltCountersQosOctetsDroppedCounter,
       "eltCountersQosPktsDroppedCounter": eltCountersQosPktsDroppedCounter,
       "eltCountersQosOctetsPassedCounter": eltCountersQosOctetsPassedCounter,
       "eltCountersQosPktsPassedCounter": eltCountersQosPktsPassedCounter,
       "eltMesCountersAceStatistics": eltMesCountersAceStatistics,
       "eltCountersAceTable": eltCountersAceTable,
       "eltCountersAceEntry": eltCountersAceEntry,
       "eltCountersAceHitCounterStatus": eltCountersAceHitCounterStatus,
       "eltCountersAceHitCounterValue": eltCountersAceHitCounterValue}
)
