# SNMP MIB module (MAIPU-QUEUE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/maipu/MAIPU-QUEUE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:11:01 2025
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

(mpMgmt,) = mibBuilder.importSymbols(
    "MAIPU-SMI",
    "mpMgmt")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

maipuQueueMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Maipu_ObjectIdentity = ObjectIdentity
maipu = _Maipu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651)
)
_MpMgmt2_ObjectIdentity = ObjectIdentity
mpMgmt2 = _MpMgmt2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6)
)
_MpRouterTech_ObjectIdentity = ObjectIdentity
mpRouterTech = _MpRouterTech_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2)
)
_MpRtQoSv2_ObjectIdentity = ObjectIdentity
mpRtQoSv2 = _MpRtQoSv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3)
)
_MaipuQueueObjects_ObjectIdentity = ObjectIdentity
maipuQueueObjects = _MaipuQueueObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1)
)
_MpQueueConfig_ObjectIdentity = ObjectIdentity
mpQueueConfig = _MpQueueConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 1)
)
_MpQInterfaceCfgTable_Object = MibTable
mpQInterfaceCfgTable = _MpQInterfaceCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mpQInterfaceCfgTable.setStatus("current")
_MpQInterfaceCfgEntry_Object = MibTableRow
mpQInterfaceCfgEntry = _MpQInterfaceCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 1, 1, 1)
)
mpQInterfaceCfgEntry.setIndexNames(
    (0, "MAIPU-QUEUE-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mpQInterfaceCfgEntry.setStatus("current")


class _MpQIFCfgQType_Type(Integer32):
    """Custom type mpQIFCfgQType based on Integer32"""
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
        *(("fifo", 1),
          ("priority", 2),
          ("custom", 3),
          ("weightedFair", 4))
    )


_MpQIFCfgQType_Type.__name__ = "Integer32"
_MpQIFCfgQType_Object = MibTableColumn
mpQIFCfgQType = _MpQIFCfgQType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 1, 1, 1, 1),
    _MpQIFCfgQType_Type()
)
mpQIFCfgQType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpQIFCfgQType.setStatus("current")
_MpQIFCfgQueues_Type = Integer32
_MpQIFCfgQueues_Object = MibTableColumn
mpQIFCfgQueues = _MpQIFCfgQueues_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 1, 1, 1, 2),
    _MpQIFCfgQueues_Type()
)
mpQIFCfgQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpQIFCfgQueues.setStatus("current")
_MpQFrameRelayVCCfgTable_Object = MibTable
mpQFrameRelayVCCfgTable = _MpQFrameRelayVCCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    mpQFrameRelayVCCfgTable.setStatus("current")
_MpQFrameRelayVCCfgEntry_Object = MibTableRow
mpQFrameRelayVCCfgEntry = _MpQFrameRelayVCCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 1, 2, 1)
)
mpQFrameRelayVCCfgEntry.setIndexNames(
    (0, "MAIPU-QUEUE-MIB", "ifIndex"),
    (0, "MAIPU-QUEUE-MIB", "mpQFRCfgDLCI"),
)
if mibBuilder.loadTexts:
    mpQFrameRelayVCCfgEntry.setStatus("current")


class _MpQFRCfgDLCI_Type(Unsigned32):
    """Custom type mpQFRCfgDLCI based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1007),
    )


_MpQFRCfgDLCI_Type.__name__ = "Unsigned32"
_MpQFRCfgDLCI_Object = MibTableColumn
mpQFRCfgDLCI = _MpQFRCfgDLCI_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 1, 2, 1, 1),
    _MpQFRCfgDLCI_Type()
)
mpQFRCfgDLCI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpQFRCfgDLCI.setStatus("current")


class _MpQFRCfgQType_Type(Integer32):
    """Custom type mpQFRCfgQType based on Integer32"""
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
        *(("fifo", 1),
          ("priority", 2),
          ("custom", 3),
          ("weightedFair", 4))
    )


_MpQFRCfgQType_Type.__name__ = "Integer32"
_MpQFRCfgQType_Object = MibTableColumn
mpQFRCfgQType = _MpQFRCfgQType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 1, 2, 1, 2),
    _MpQFRCfgQType_Type()
)
mpQFRCfgQType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpQFRCfgQType.setStatus("current")
_MpQFRCfgQueues_Type = Integer32
_MpQFRCfgQueues_Object = MibTableColumn
mpQFRCfgQueues = _MpQFRCfgQueues_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 1, 2, 1, 3),
    _MpQFRCfgQueues_Type()
)
mpQFRCfgQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpQFRCfgQueues.setStatus("current")
_MpQATMPVCCfgTable_Object = MibTable
mpQATMPVCCfgTable = _MpQATMPVCCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    mpQATMPVCCfgTable.setStatus("current")
_MpQATMPVCCfgEntry_Object = MibTableRow
mpQATMPVCCfgEntry = _MpQATMPVCCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 1, 3, 1)
)
mpQATMPVCCfgEntry.setIndexNames(
    (0, "MAIPU-QUEUE-MIB", "ifIndex"),
    (0, "MAIPU-QUEUE-MIB", "mpQATMCfgVPI"),
    (0, "MAIPU-QUEUE-MIB", "mpQATMCfgVCI"),
)
if mibBuilder.loadTexts:
    mpQATMPVCCfgEntry.setStatus("current")


class _MpQATMCfgVPI_Type(Unsigned32):
    """Custom type mpQATMCfgVPI based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MpQATMCfgVPI_Type.__name__ = "Unsigned32"
_MpQATMCfgVPI_Object = MibTableColumn
mpQATMCfgVPI = _MpQATMCfgVPI_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 1, 3, 1, 1),
    _MpQATMCfgVPI_Type()
)
mpQATMCfgVPI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpQATMCfgVPI.setStatus("current")


class _MpQATMCfgVCI_Type(Unsigned32):
    """Custom type mpQATMCfgVCI based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MpQATMCfgVCI_Type.__name__ = "Unsigned32"
_MpQATMCfgVCI_Object = MibTableColumn
mpQATMCfgVCI = _MpQATMCfgVCI_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 1, 3, 1, 2),
    _MpQATMCfgVCI_Type()
)
mpQATMCfgVCI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpQATMCfgVCI.setStatus("current")


class _MpQATMCfgQType_Type(Integer32):
    """Custom type mpQATMCfgQType based on Integer32"""
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
        *(("fifo", 1),
          ("priority", 2),
          ("custom", 3),
          ("weightedFair", 4))
    )


_MpQATMCfgQType_Type.__name__ = "Integer32"
_MpQATMCfgQType_Object = MibTableColumn
mpQATMCfgQType = _MpQATMCfgQType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 1, 3, 1, 3),
    _MpQATMCfgQType_Type()
)
mpQATMCfgQType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpQATMCfgQType.setStatus("current")
_MpQATMCfgQueues_Type = Integer32
_MpQATMCfgQueues_Object = MibTableColumn
mpQATMCfgQueues = _MpQATMCfgQueues_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 1, 3, 1, 4),
    _MpQATMCfgQueues_Type()
)
mpQATMCfgQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpQATMCfgQueues.setStatus("current")
_MpQueueStats_ObjectIdentity = ObjectIdentity
mpQueueStats = _MpQueueStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 2)
)
_MpQInterfaceStatTable_Object = MibTable
mpQInterfaceStatTable = _MpQInterfaceStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mpQInterfaceStatTable.setStatus("current")
_MpQInterfaceStatEntry_Object = MibTableRow
mpQInterfaceStatEntry = _MpQInterfaceStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 2, 1, 1)
)
mpQInterfaceStatEntry.setIndexNames(
    (0, "MAIPU-QUEUE-MIB", "ifIndex"),
    (0, "MAIPU-QUEUE-MIB", "mpQIFstatQNumber"),
)
if mibBuilder.loadTexts:
    mpQInterfaceStatEntry.setStatus("current")


class _MpQIFstatQNumber_Type(Integer32):
    """Custom type mpQIFstatQNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MpQIFstatQNumber_Type.__name__ = "Integer32"
_MpQIFstatQNumber_Object = MibTableColumn
mpQIFstatQNumber = _MpQIFstatQNumber_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 2, 1, 1, 1),
    _MpQIFstatQNumber_Type()
)
mpQIFstatQNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpQIFstatQNumber.setStatus("current")


class _MpQIFstatDepthUnit_Type(Integer32):
    """Custom type mpQIFstatDepthUnit based on Integer32"""
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
        *(("packets", 1),
          ("bytes", 2),
          ("cells", 3),
          ("ms", 4),
          ("us", 5))
    )


_MpQIFstatDepthUnit_Type.__name__ = "Integer32"
_MpQIFstatDepthUnit_Object = MibTableColumn
mpQIFstatDepthUnit = _MpQIFstatDepthUnit_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 2, 1, 1, 2),
    _MpQIFstatDepthUnit_Type()
)
mpQIFstatDepthUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpQIFstatDepthUnit.setStatus("current")
_MpQIFstatCurrentDepth_Type = Gauge32
_MpQIFstatCurrentDepth_Object = MibTableColumn
mpQIFstatCurrentDepth = _MpQIFstatCurrentDepth_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 2, 1, 1, 3),
    _MpQIFstatCurrentDepth_Type()
)
mpQIFstatCurrentDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpQIFstatCurrentDepth.setStatus("current")
_MpQIFstatMaxDepth_Type = Integer32
_MpQIFstatMaxDepth_Object = MibTableColumn
mpQIFstatMaxDepth = _MpQIFstatMaxDepth_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 2, 1, 1, 4),
    _MpQIFstatMaxDepth_Type()
)
mpQIFstatMaxDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpQIFstatMaxDepth.setStatus("current")
_MpQIFstatTransmitPkt64_Type = Counter64
_MpQIFstatTransmitPkt64_Object = MibTableColumn
mpQIFstatTransmitPkt64 = _MpQIFstatTransmitPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 2, 1, 1, 5),
    _MpQIFstatTransmitPkt64_Type()
)
mpQIFstatTransmitPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpQIFstatTransmitPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpQIFstatTransmitPkt64.setUnits("packets")
_MpQIFstatDiscardPkt64_Type = Counter64
_MpQIFstatDiscardPkt64_Object = MibTableColumn
mpQIFstatDiscardPkt64 = _MpQIFstatDiscardPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 2, 1, 1, 6),
    _MpQIFstatDiscardPkt64_Type()
)
mpQIFstatDiscardPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpQIFstatDiscardPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpQIFstatDiscardPkt64.setUnits("packets")
_MpQFrameRelayVCStatTable_Object = MibTable
mpQFrameRelayVCStatTable = _MpQFrameRelayVCStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mpQFrameRelayVCStatTable.setStatus("current")
_MpQFrameRelayVCStatEntry_Object = MibTableRow
mpQFrameRelayVCStatEntry = _MpQFrameRelayVCStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 2, 2, 1)
)
mpQFrameRelayVCStatEntry.setIndexNames(
    (0, "MAIPU-QUEUE-MIB", "ifIndex"),
    (0, "MAIPU-QUEUE-MIB", "mpQFRCfgDLCI"),
    (0, "MAIPU-QUEUE-MIB", "mpQFRstatQNumber"),
)
if mibBuilder.loadTexts:
    mpQFrameRelayVCStatEntry.setStatus("current")


class _MpQFRstatQNumber_Type(Integer32):
    """Custom type mpQFRstatQNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MpQFRstatQNumber_Type.__name__ = "Integer32"
_MpQFRstatQNumber_Object = MibTableColumn
mpQFRstatQNumber = _MpQFRstatQNumber_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 2, 2, 1, 1),
    _MpQFRstatQNumber_Type()
)
mpQFRstatQNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpQFRstatQNumber.setStatus("current")


class _MpQFRstatDepthUnit_Type(Integer32):
    """Custom type mpQFRstatDepthUnit based on Integer32"""
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
        *(("packets", 1),
          ("bytes", 2),
          ("cells", 3),
          ("ms", 4),
          ("us", 5))
    )


_MpQFRstatDepthUnit_Type.__name__ = "Integer32"
_MpQFRstatDepthUnit_Object = MibTableColumn
mpQFRstatDepthUnit = _MpQFRstatDepthUnit_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 2, 2, 1, 2),
    _MpQFRstatDepthUnit_Type()
)
mpQFRstatDepthUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpQFRstatDepthUnit.setStatus("current")
_MpQFRstatCurrentDepth_Type = Gauge32
_MpQFRstatCurrentDepth_Object = MibTableColumn
mpQFRstatCurrentDepth = _MpQFRstatCurrentDepth_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 2, 2, 1, 3),
    _MpQFRstatCurrentDepth_Type()
)
mpQFRstatCurrentDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpQFRstatCurrentDepth.setStatus("current")
_MpQFRstatMaxDepth_Type = Integer32
_MpQFRstatMaxDepth_Object = MibTableColumn
mpQFRstatMaxDepth = _MpQFRstatMaxDepth_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 2, 2, 1, 4),
    _MpQFRstatMaxDepth_Type()
)
mpQFRstatMaxDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpQFRstatMaxDepth.setStatus("current")
_MpQFRstatTransmitPkt64_Type = Counter64
_MpQFRstatTransmitPkt64_Object = MibTableColumn
mpQFRstatTransmitPkt64 = _MpQFRstatTransmitPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 2, 2, 1, 5),
    _MpQFRstatTransmitPkt64_Type()
)
mpQFRstatTransmitPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpQFRstatTransmitPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpQFRstatTransmitPkt64.setUnits("packets")
_MpQFRstatDiscardPkt64_Type = Counter64
_MpQFRstatDiscardPkt64_Object = MibTableColumn
mpQFRstatDiscardPkt64 = _MpQFRstatDiscardPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 2, 2, 1, 6),
    _MpQFRstatDiscardPkt64_Type()
)
mpQFRstatDiscardPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpQFRstatDiscardPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpQFRstatDiscardPkt64.setUnits("packets")
_MpQATMPVCStatTable_Object = MibTable
mpQATMPVCStatTable = _MpQATMPVCStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 2, 3)
)
if mibBuilder.loadTexts:
    mpQATMPVCStatTable.setStatus("current")
_MpQATMPVCStatEntry_Object = MibTableRow
mpQATMPVCStatEntry = _MpQATMPVCStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 2, 3, 1)
)
mpQATMPVCStatEntry.setIndexNames(
    (0, "MAIPU-QUEUE-MIB", "ifIndex"),
    (0, "MAIPU-QUEUE-MIB", "mpQATMCfgVPI"),
    (0, "MAIPU-QUEUE-MIB", "mpQATMCfgVCI"),
    (0, "MAIPU-QUEUE-MIB", "mpQATMstatQNumber"),
)
if mibBuilder.loadTexts:
    mpQATMPVCStatEntry.setStatus("current")


class _MpQATMstatQNumber_Type(Integer32):
    """Custom type mpQATMstatQNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MpQATMstatQNumber_Type.__name__ = "Integer32"
_MpQATMstatQNumber_Object = MibTableColumn
mpQATMstatQNumber = _MpQATMstatQNumber_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 2, 3, 1, 1),
    _MpQATMstatQNumber_Type()
)
mpQATMstatQNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpQATMstatQNumber.setStatus("current")


class _MpQATMstatDepthUnit_Type(Integer32):
    """Custom type mpQATMstatDepthUnit based on Integer32"""
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
        *(("packets", 1),
          ("bytes", 2),
          ("cells", 3),
          ("ms", 4),
          ("us", 5))
    )


_MpQATMstatDepthUnit_Type.__name__ = "Integer32"
_MpQATMstatDepthUnit_Object = MibTableColumn
mpQATMstatDepthUnit = _MpQATMstatDepthUnit_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 2, 3, 1, 2),
    _MpQATMstatDepthUnit_Type()
)
mpQATMstatDepthUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpQATMstatDepthUnit.setStatus("current")
_MpQATMstatCurrentDepth_Type = Gauge32
_MpQATMstatCurrentDepth_Object = MibTableColumn
mpQATMstatCurrentDepth = _MpQATMstatCurrentDepth_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 2, 3, 1, 3),
    _MpQATMstatCurrentDepth_Type()
)
mpQATMstatCurrentDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpQATMstatCurrentDepth.setStatus("current")
_MpQATMstatMaxDepth_Type = Integer32
_MpQATMstatMaxDepth_Object = MibTableColumn
mpQATMstatMaxDepth = _MpQATMstatMaxDepth_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 2, 3, 1, 4),
    _MpQATMstatMaxDepth_Type()
)
mpQATMstatMaxDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpQATMstatMaxDepth.setStatus("current")
_MpQATMstatTransmitPkt64_Type = Counter64
_MpQATMstatTransmitPkt64_Object = MibTableColumn
mpQATMstatTransmitPkt64 = _MpQATMstatTransmitPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 2, 3, 1, 5),
    _MpQATMstatTransmitPkt64_Type()
)
mpQATMstatTransmitPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpQATMstatTransmitPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpQATMstatTransmitPkt64.setUnits("packets")
_MpQATMstatDiscardPkt64_Type = Counter64
_MpQATMstatDiscardPkt64_Object = MibTableColumn
mpQATMstatDiscardPkt64 = _MpQATMstatDiscardPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 3, 1, 2, 3, 1, 6),
    _MpQATMstatDiscardPkt64_Type()
)
mpQATMstatDiscardPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpQATMstatDiscardPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpQATMstatDiscardPkt64.setUnits("packets")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MAIPU-QUEUE-MIB",
    **{"maipu": maipu,
       "mpMgmt2": mpMgmt2,
       "mpRouterTech": mpRouterTech,
       "mpRtQoSv2": mpRtQoSv2,
       "maipuQueueMIB": maipuQueueMIB,
       "maipuQueueObjects": maipuQueueObjects,
       "mpQueueConfig": mpQueueConfig,
       "mpQInterfaceCfgTable": mpQInterfaceCfgTable,
       "mpQInterfaceCfgEntry": mpQInterfaceCfgEntry,
       "mpQIFCfgQType": mpQIFCfgQType,
       "mpQIFCfgQueues": mpQIFCfgQueues,
       "mpQFrameRelayVCCfgTable": mpQFrameRelayVCCfgTable,
       "mpQFrameRelayVCCfgEntry": mpQFrameRelayVCCfgEntry,
       "mpQFRCfgDLCI": mpQFRCfgDLCI,
       "mpQFRCfgQType": mpQFRCfgQType,
       "mpQFRCfgQueues": mpQFRCfgQueues,
       "mpQATMPVCCfgTable": mpQATMPVCCfgTable,
       "mpQATMPVCCfgEntry": mpQATMPVCCfgEntry,
       "mpQATMCfgVPI": mpQATMCfgVPI,
       "mpQATMCfgVCI": mpQATMCfgVCI,
       "mpQATMCfgQType": mpQATMCfgQType,
       "mpQATMCfgQueues": mpQATMCfgQueues,
       "mpQueueStats": mpQueueStats,
       "mpQInterfaceStatTable": mpQInterfaceStatTable,
       "mpQInterfaceStatEntry": mpQInterfaceStatEntry,
       "mpQIFstatQNumber": mpQIFstatQNumber,
       "mpQIFstatDepthUnit": mpQIFstatDepthUnit,
       "mpQIFstatCurrentDepth": mpQIFstatCurrentDepth,
       "mpQIFstatMaxDepth": mpQIFstatMaxDepth,
       "mpQIFstatTransmitPkt64": mpQIFstatTransmitPkt64,
       "mpQIFstatDiscardPkt64": mpQIFstatDiscardPkt64,
       "mpQFrameRelayVCStatTable": mpQFrameRelayVCStatTable,
       "mpQFrameRelayVCStatEntry": mpQFrameRelayVCStatEntry,
       "mpQFRstatQNumber": mpQFRstatQNumber,
       "mpQFRstatDepthUnit": mpQFRstatDepthUnit,
       "mpQFRstatCurrentDepth": mpQFRstatCurrentDepth,
       "mpQFRstatMaxDepth": mpQFRstatMaxDepth,
       "mpQFRstatTransmitPkt64": mpQFRstatTransmitPkt64,
       "mpQFRstatDiscardPkt64": mpQFRstatDiscardPkt64,
       "mpQATMPVCStatTable": mpQATMPVCStatTable,
       "mpQATMPVCStatEntry": mpQATMPVCStatEntry,
       "mpQATMstatQNumber": mpQATMstatQNumber,
       "mpQATMstatDepthUnit": mpQATMstatDepthUnit,
       "mpQATMstatCurrentDepth": mpQATMstatCurrentDepth,
       "mpQATMstatMaxDepth": mpQATMstatMaxDepth,
       "mpQATMstatTransmitPkt64": mpQATMstatTransmitPkt64,
       "mpQATMstatDiscardPkt64": mpQATMstatDiscardPkt64}
)
