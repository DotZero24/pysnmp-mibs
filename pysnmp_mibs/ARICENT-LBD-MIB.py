# SNMP MIB module (ARICENT-LBD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-LBD-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:43:46 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

futureLbdMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 123)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsLbdSystems_ObjectIdentity = ObjectIdentity
fsLbdSystems = _FsLbdSystems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 123, 1)
)


class _FsLbdSystemControl_Type(Integer32):
    """Custom type fsLbdSystemControl based on Integer32"""
    defaultValue = 1

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


_FsLbdSystemControl_Type.__name__ = "Integer32"
_FsLbdSystemControl_Object = MibScalar
fsLbdSystemControl = _FsLbdSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 123, 1, 1),
    _FsLbdSystemControl_Type()
)
fsLbdSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLbdSystemControl.setStatus("current")


class _FsLbdModuleStatus_Type(Integer32):
    """Custom type fsLbdModuleStatus based on Integer32"""
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


_FsLbdModuleStatus_Type.__name__ = "Integer32"
_FsLbdModuleStatus_Object = MibScalar
fsLbdModuleStatus = _FsLbdModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 123, 1, 2),
    _FsLbdModuleStatus_Type()
)
fsLbdModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLbdModuleStatus.setStatus("current")


class _FsLbdTransmitInterval_Type(Integer32):
    """Custom type fsLbdTransmitInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_FsLbdTransmitInterval_Type.__name__ = "Integer32"
_FsLbdTransmitInterval_Object = MibScalar
fsLbdTransmitInterval = _FsLbdTransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 123, 1, 3),
    _FsLbdTransmitInterval_Type()
)
fsLbdTransmitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLbdTransmitInterval.setStatus("current")
_FsLbdDestMacAddress_Type = MacAddress
_FsLbdDestMacAddress_Object = MibScalar
fsLbdDestMacAddress = _FsLbdDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 123, 1, 4),
    _FsLbdDestMacAddress_Type()
)
fsLbdDestMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLbdDestMacAddress.setStatus("current")


class _FsLbdTraceOption_Type(Integer32):
    """Custom type fsLbdTraceOption based on Integer32"""
    defaultValue = 8


_FsLbdTraceOption_Type.__name__ = "Integer32"
_FsLbdTraceOption_Object = MibScalar
fsLbdTraceOption = _FsLbdTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 123, 1, 5),
    _FsLbdTraceOption_Type()
)
fsLbdTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLbdTraceOption.setStatus("current")
_FsLbdConfig_ObjectIdentity = ObjectIdentity
fsLbdConfig = _FsLbdConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 123, 2)
)
_FsLbdPortTable_Object = MibTable
fsLbdPortTable = _FsLbdPortTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 123, 2, 1)
)
if mibBuilder.loadTexts:
    fsLbdPortTable.setStatus("current")
_FsLbdPortEntry_Object = MibTableRow
fsLbdPortEntry = _FsLbdPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 123, 2, 1, 1)
)
fsLbdPortEntry.setIndexNames(
    (0, "ARICENT-LBD-MIB", "fsLbdPortId"),
)
if mibBuilder.loadTexts:
    fsLbdPortEntry.setStatus("current")
_FsLbdPortId_Type = Integer32
_FsLbdPortId_Object = MibTableColumn
fsLbdPortId = _FsLbdPortId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 123, 2, 1, 1, 1),
    _FsLbdPortId_Type()
)
fsLbdPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsLbdPortId.setStatus("current")


class _FsLbdLoopDetectStatus_Type(Integer32):
    """Custom type fsLbdLoopDetectStatus based on Integer32"""
    defaultValue = 1

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


_FsLbdLoopDetectStatus_Type.__name__ = "Integer32"
_FsLbdLoopDetectStatus_Object = MibTableColumn
fsLbdLoopDetectStatus = _FsLbdLoopDetectStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 123, 2, 1, 1, 2),
    _FsLbdLoopDetectStatus_Type()
)
fsLbdLoopDetectStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLbdLoopDetectStatus.setStatus("current")
_FsLbdTxCount_Type = Counter32
_FsLbdTxCount_Object = MibTableColumn
fsLbdTxCount = _FsLbdTxCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 123, 2, 1, 1, 3),
    _FsLbdTxCount_Type()
)
fsLbdTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLbdTxCount.setStatus("current")
_FsLbdRxCount_Type = Counter32
_FsLbdRxCount_Object = MibTableColumn
fsLbdRxCount = _FsLbdRxCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 123, 2, 1, 1, 4),
    _FsLbdRxCount_Type()
)
fsLbdRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLbdRxCount.setStatus("current")


class _FsLbdPortStatus_Type(Integer32):
    """Custom type fsLbdPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noloopback", 0),
          ("loopback", 1))
    )


_FsLbdPortStatus_Type.__name__ = "Integer32"
_FsLbdPortStatus_Object = MibTableColumn
fsLbdPortStatus = _FsLbdPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 123, 2, 1, 1, 5),
    _FsLbdPortStatus_Type()
)
fsLbdPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLbdPortStatus.setStatus("current")
_FsLbdPktTxFromPort_Type = Integer32
_FsLbdPktTxFromPort_Object = MibTableColumn
fsLbdPktTxFromPort = _FsLbdPktTxFromPort_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 123, 2, 1, 1, 6),
    _FsLbdPktTxFromPort_Type()
)
fsLbdPktTxFromPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLbdPktTxFromPort.setStatus("current")
_FsLbdPortRowStatus_Type = RowStatus
_FsLbdPortRowStatus_Object = MibTableColumn
fsLbdPortRowStatus = _FsLbdPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 123, 2, 1, 1, 7),
    _FsLbdPortRowStatus_Type()
)
fsLbdPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLbdPortRowStatus.setStatus("current")


class _FsLbdClearStats_Type(TruthValue):
    """Custom type fsLbdClearStats based on TruthValue"""
    defaultValue = 2


_FsLbdClearStats_Type.__name__ = "TruthValue"
_FsLbdClearStats_Object = MibTableColumn
fsLbdClearStats = _FsLbdClearStats_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 123, 2, 1, 1, 8),
    _FsLbdClearStats_Type()
)
fsLbdClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLbdClearStats.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-LBD-MIB",
    **{"futureLbdMIB": futureLbdMIB,
       "fsLbdSystems": fsLbdSystems,
       "fsLbdSystemControl": fsLbdSystemControl,
       "fsLbdModuleStatus": fsLbdModuleStatus,
       "fsLbdTransmitInterval": fsLbdTransmitInterval,
       "fsLbdDestMacAddress": fsLbdDestMacAddress,
       "fsLbdTraceOption": fsLbdTraceOption,
       "fsLbdConfig": fsLbdConfig,
       "fsLbdPortTable": fsLbdPortTable,
       "fsLbdPortEntry": fsLbdPortEntry,
       "fsLbdPortId": fsLbdPortId,
       "fsLbdLoopDetectStatus": fsLbdLoopDetectStatus,
       "fsLbdTxCount": fsLbdTxCount,
       "fsLbdRxCount": fsLbdRxCount,
       "fsLbdPortStatus": fsLbdPortStatus,
       "fsLbdPktTxFromPort": fsLbdPktTxFromPort,
       "fsLbdPortRowStatus": fsLbdPortRowStatus,
       "fsLbdClearStats": fsLbdClearStats}
)
