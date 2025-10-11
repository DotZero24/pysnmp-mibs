# SNMP MIB module (SUPERMICRO-SNOOP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-SNOOP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:02:54 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(PortList,
 VlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fssnoop = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105)
)
if mibBuilder.loadTexts:
    fssnoop.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class InnerVlanIndex(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )



# MIB Managed Objects in the order of their OIDs

_FsSnoopSystem_ObjectIdentity = ObjectIdentity
fsSnoopSystem = _FsSnoopSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 1)
)
_FsSnoopInst_ObjectIdentity = ObjectIdentity
fsSnoopInst = _FsSnoopInst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 2)
)
_FsSnoopInstanceGlobalTable_Object = MibTable
fsSnoopInstanceGlobalTable = _FsSnoopInstanceGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 2, 1)
)
if mibBuilder.loadTexts:
    fsSnoopInstanceGlobalTable.setStatus("current")
_FsSnoopInstanceGlobalEntry_Object = MibTableRow
fsSnoopInstanceGlobalEntry = _FsSnoopInstanceGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 2, 1, 1)
)
fsSnoopInstanceGlobalEntry.setIndexNames(
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopInstanceGlobalInstId"),
)
if mibBuilder.loadTexts:
    fsSnoopInstanceGlobalEntry.setStatus("current")


class _FsSnoopInstanceGlobalInstId_Type(Integer32):
    """Custom type fsSnoopInstanceGlobalInstId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsSnoopInstanceGlobalInstId_Type.__name__ = "Integer32"
_FsSnoopInstanceGlobalInstId_Object = MibTableColumn
fsSnoopInstanceGlobalInstId = _FsSnoopInstanceGlobalInstId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 2, 1, 1, 1),
    _FsSnoopInstanceGlobalInstId_Type()
)
fsSnoopInstanceGlobalInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopInstanceGlobalInstId.setStatus("current")


class _FsSnoopInstanceGlobalMcastFwdMode_Type(Integer32):
    """Custom type fsSnoopInstanceGlobalMcastFwdMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipbased", 1),
          ("macbased", 2))
    )


_FsSnoopInstanceGlobalMcastFwdMode_Type.__name__ = "Integer32"
_FsSnoopInstanceGlobalMcastFwdMode_Object = MibTableColumn
fsSnoopInstanceGlobalMcastFwdMode = _FsSnoopInstanceGlobalMcastFwdMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 2, 1, 1, 2),
    _FsSnoopInstanceGlobalMcastFwdMode_Type()
)
fsSnoopInstanceGlobalMcastFwdMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopInstanceGlobalMcastFwdMode.setStatus("current")


class _FsSnoopInstanceGlobalSystemControl_Type(Integer32):
    """Custom type fsSnoopInstanceGlobalSystemControl based on Integer32"""
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


_FsSnoopInstanceGlobalSystemControl_Type.__name__ = "Integer32"
_FsSnoopInstanceGlobalSystemControl_Object = MibTableColumn
fsSnoopInstanceGlobalSystemControl = _FsSnoopInstanceGlobalSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 2, 1, 1, 3),
    _FsSnoopInstanceGlobalSystemControl_Type()
)
fsSnoopInstanceGlobalSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopInstanceGlobalSystemControl.setStatus("current")


class _FsSnoopInstanceGlobalLeaveConfigLevel_Type(Integer32):
    """Custom type fsSnoopInstanceGlobalLeaveConfigLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vlanbased", 1),
          ("portbased", 2))
    )


_FsSnoopInstanceGlobalLeaveConfigLevel_Type.__name__ = "Integer32"
_FsSnoopInstanceGlobalLeaveConfigLevel_Object = MibTableColumn
fsSnoopInstanceGlobalLeaveConfigLevel = _FsSnoopInstanceGlobalLeaveConfigLevel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 2, 1, 1, 4),
    _FsSnoopInstanceGlobalLeaveConfigLevel_Type()
)
fsSnoopInstanceGlobalLeaveConfigLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopInstanceGlobalLeaveConfigLevel.setStatus("current")


class _FsSnoopInstanceGlobalEnhancedMode_Type(Integer32):
    """Custom type fsSnoopInstanceGlobalEnhancedMode based on Integer32"""
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


_FsSnoopInstanceGlobalEnhancedMode_Type.__name__ = "Integer32"
_FsSnoopInstanceGlobalEnhancedMode_Object = MibTableColumn
fsSnoopInstanceGlobalEnhancedMode = _FsSnoopInstanceGlobalEnhancedMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 2, 1, 1, 5),
    _FsSnoopInstanceGlobalEnhancedMode_Type()
)
fsSnoopInstanceGlobalEnhancedMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSnoopInstanceGlobalEnhancedMode.setStatus("current")


class _FsSnoopInstanceGlobalReportProcessConfigLevel_Type(Integer32):
    """Custom type fsSnoopInstanceGlobalReportProcessConfigLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonrouterports", 1),
          ("allports", 2))
    )


_FsSnoopInstanceGlobalReportProcessConfigLevel_Type.__name__ = "Integer32"
_FsSnoopInstanceGlobalReportProcessConfigLevel_Object = MibTableColumn
fsSnoopInstanceGlobalReportProcessConfigLevel = _FsSnoopInstanceGlobalReportProcessConfigLevel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 2, 1, 1, 6),
    _FsSnoopInstanceGlobalReportProcessConfigLevel_Type()
)
fsSnoopInstanceGlobalReportProcessConfigLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopInstanceGlobalReportProcessConfigLevel.setStatus("current")


class _FsSnoopInstanceGlobalSparseMode_Type(Integer32):
    """Custom type fsSnoopInstanceGlobalSparseMode based on Integer32"""
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


_FsSnoopInstanceGlobalSparseMode_Type.__name__ = "Integer32"
_FsSnoopInstanceGlobalSparseMode_Object = MibTableColumn
fsSnoopInstanceGlobalSparseMode = _FsSnoopInstanceGlobalSparseMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 2, 1, 1, 7),
    _FsSnoopInstanceGlobalSparseMode_Type()
)
fsSnoopInstanceGlobalSparseMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSnoopInstanceGlobalSparseMode.setStatus("current")


class _FsSnoopInstanceGlobalMulticastFilterStatus_Type(Integer32):
    """Custom type fsSnoopInstanceGlobalMulticastFilterStatus based on Integer32"""
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


_FsSnoopInstanceGlobalMulticastFilterStatus_Type.__name__ = "Integer32"
_FsSnoopInstanceGlobalMulticastFilterStatus_Object = MibTableColumn
fsSnoopInstanceGlobalMulticastFilterStatus = _FsSnoopInstanceGlobalMulticastFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 2, 1, 1, 8),
    _FsSnoopInstanceGlobalMulticastFilterStatus_Type()
)
fsSnoopInstanceGlobalMulticastFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopInstanceGlobalMulticastFilterStatus.setStatus("current")
_FsSnoopInstanceConfigTable_Object = MibTable
fsSnoopInstanceConfigTable = _FsSnoopInstanceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 2, 2)
)
if mibBuilder.loadTexts:
    fsSnoopInstanceConfigTable.setStatus("current")
_FsSnoopInstanceConfigEntry_Object = MibTableRow
fsSnoopInstanceConfigEntry = _FsSnoopInstanceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 2, 2, 1)
)
fsSnoopInstanceConfigEntry.setIndexNames(
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopInstanceConfigInstId"),
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopInetAddressType"),
)
if mibBuilder.loadTexts:
    fsSnoopInstanceConfigEntry.setStatus("current")


class _FsSnoopInstanceConfigInstId_Type(Integer32):
    """Custom type fsSnoopInstanceConfigInstId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsSnoopInstanceConfigInstId_Type.__name__ = "Integer32"
_FsSnoopInstanceConfigInstId_Object = MibTableColumn
fsSnoopInstanceConfigInstId = _FsSnoopInstanceConfigInstId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 2, 2, 1, 1),
    _FsSnoopInstanceConfigInstId_Type()
)
fsSnoopInstanceConfigInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopInstanceConfigInstId.setStatus("current")
_FsSnoopInetAddressType_Type = InetAddressType
_FsSnoopInetAddressType_Object = MibTableColumn
fsSnoopInetAddressType = _FsSnoopInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 2, 2, 1, 2),
    _FsSnoopInetAddressType_Type()
)
fsSnoopInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopInetAddressType.setStatus("current")


class _FsSnoopStatus_Type(Integer32):
    """Custom type fsSnoopStatus based on Integer32"""
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


_FsSnoopStatus_Type.__name__ = "Integer32"
_FsSnoopStatus_Object = MibTableColumn
fsSnoopStatus = _FsSnoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 2, 2, 1, 3),
    _FsSnoopStatus_Type()
)
fsSnoopStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopStatus.setStatus("current")


class _FsSnoopProxyReportingStatus_Type(Integer32):
    """Custom type fsSnoopProxyReportingStatus based on Integer32"""
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


_FsSnoopProxyReportingStatus_Type.__name__ = "Integer32"
_FsSnoopProxyReportingStatus_Object = MibTableColumn
fsSnoopProxyReportingStatus = _FsSnoopProxyReportingStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 2, 2, 1, 4),
    _FsSnoopProxyReportingStatus_Type()
)
fsSnoopProxyReportingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopProxyReportingStatus.setStatus("current")


class _FsSnoopRouterPortPurgeInterval_Type(Integer32):
    """Custom type fsSnoopRouterPortPurgeInterval based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_FsSnoopRouterPortPurgeInterval_Type.__name__ = "Integer32"
_FsSnoopRouterPortPurgeInterval_Object = MibTableColumn
fsSnoopRouterPortPurgeInterval = _FsSnoopRouterPortPurgeInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 2, 2, 1, 5),
    _FsSnoopRouterPortPurgeInterval_Type()
)
fsSnoopRouterPortPurgeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopRouterPortPurgeInterval.setStatus("deprecated")


class _FsSnoopPortPurgeInterval_Type(Integer32):
    """Custom type fsSnoopPortPurgeInterval based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(130, 1225),
    )


_FsSnoopPortPurgeInterval_Type.__name__ = "Integer32"
_FsSnoopPortPurgeInterval_Object = MibTableColumn
fsSnoopPortPurgeInterval = _FsSnoopPortPurgeInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 2, 2, 1, 6),
    _FsSnoopPortPurgeInterval_Type()
)
fsSnoopPortPurgeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopPortPurgeInterval.setStatus("deprecated")


class _FsSnoopReportForwardInterval_Type(Integer32):
    """Custom type fsSnoopReportForwardInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_FsSnoopReportForwardInterval_Type.__name__ = "Integer32"
_FsSnoopReportForwardInterval_Object = MibTableColumn
fsSnoopReportForwardInterval = _FsSnoopReportForwardInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 2, 2, 1, 7),
    _FsSnoopReportForwardInterval_Type()
)
fsSnoopReportForwardInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopReportForwardInterval.setStatus("current")


class _FsSnoopRetryCount_Type(Integer32):
    """Custom type fsSnoopRetryCount based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_FsSnoopRetryCount_Type.__name__ = "Integer32"
_FsSnoopRetryCount_Object = MibTableColumn
fsSnoopRetryCount = _FsSnoopRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 2, 2, 1, 8),
    _FsSnoopRetryCount_Type()
)
fsSnoopRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopRetryCount.setStatus("current")


class _FsSnoopGrpQueryInterval_Type(Integer32):
    """Custom type fsSnoopGrpQueryInterval based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_FsSnoopGrpQueryInterval_Type.__name__ = "Integer32"
_FsSnoopGrpQueryInterval_Object = MibTableColumn
fsSnoopGrpQueryInterval = _FsSnoopGrpQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 2, 2, 1, 9),
    _FsSnoopGrpQueryInterval_Type()
)
fsSnoopGrpQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopGrpQueryInterval.setStatus("current")


class _FsSnoopReportFwdOnAllPorts_Type(Integer32):
    """Custom type fsSnoopReportFwdOnAllPorts based on Integer32"""
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
        *(("allports", 1),
          ("rtrports", 2),
          ("nonedgeports", 3))
    )


_FsSnoopReportFwdOnAllPorts_Type.__name__ = "Integer32"
_FsSnoopReportFwdOnAllPorts_Object = MibTableColumn
fsSnoopReportFwdOnAllPorts = _FsSnoopReportFwdOnAllPorts_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 2, 2, 1, 10),
    _FsSnoopReportFwdOnAllPorts_Type()
)
fsSnoopReportFwdOnAllPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopReportFwdOnAllPorts.setStatus("current")
_FsSnoopTraceOption_Type = Integer32
_FsSnoopTraceOption_Object = MibTableColumn
fsSnoopTraceOption = _FsSnoopTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 2, 2, 1, 11),
    _FsSnoopTraceOption_Type()
)
fsSnoopTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopTraceOption.setStatus("current")


class _FsSnoopOperStatus_Type(Integer32):
    """Custom type fsSnoopOperStatus based on Integer32"""
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


_FsSnoopOperStatus_Type.__name__ = "Integer32"
_FsSnoopOperStatus_Object = MibTableColumn
fsSnoopOperStatus = _FsSnoopOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 2, 2, 1, 12),
    _FsSnoopOperStatus_Type()
)
fsSnoopOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopOperStatus.setStatus("current")


class _FsSnoopSendQueryOnTopoChange_Type(Integer32):
    """Custom type fsSnoopSendQueryOnTopoChange based on Integer32"""
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


_FsSnoopSendQueryOnTopoChange_Type.__name__ = "Integer32"
_FsSnoopSendQueryOnTopoChange_Object = MibTableColumn
fsSnoopSendQueryOnTopoChange = _FsSnoopSendQueryOnTopoChange_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 2, 2, 1, 13),
    _FsSnoopSendQueryOnTopoChange_Type()
)
fsSnoopSendQueryOnTopoChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopSendQueryOnTopoChange.setStatus("current")


class _FsSnoopSendLeaveOnTopoChange_Type(Integer32):
    """Custom type fsSnoopSendLeaveOnTopoChange based on Integer32"""
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


_FsSnoopSendLeaveOnTopoChange_Type.__name__ = "Integer32"
_FsSnoopSendLeaveOnTopoChange_Object = MibTableColumn
fsSnoopSendLeaveOnTopoChange = _FsSnoopSendLeaveOnTopoChange_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 2, 2, 1, 14),
    _FsSnoopSendLeaveOnTopoChange_Type()
)
fsSnoopSendLeaveOnTopoChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopSendLeaveOnTopoChange.setStatus("current")


class _FsSnoopFilterStatus_Type(Integer32):
    """Custom type fsSnoopFilterStatus based on Integer32"""
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


_FsSnoopFilterStatus_Type.__name__ = "Integer32"
_FsSnoopFilterStatus_Object = MibTableColumn
fsSnoopFilterStatus = _FsSnoopFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 2, 2, 1, 15),
    _FsSnoopFilterStatus_Type()
)
fsSnoopFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopFilterStatus.setStatus("current")


class _FsSnoopMulticastVlanStatus_Type(Integer32):
    """Custom type fsSnoopMulticastVlanStatus based on Integer32"""
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


_FsSnoopMulticastVlanStatus_Type.__name__ = "Integer32"
_FsSnoopMulticastVlanStatus_Object = MibTableColumn
fsSnoopMulticastVlanStatus = _FsSnoopMulticastVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 2, 2, 1, 16),
    _FsSnoopMulticastVlanStatus_Type()
)
fsSnoopMulticastVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopMulticastVlanStatus.setStatus("current")


class _FsSnoopProxyStatus_Type(Integer32):
    """Custom type fsSnoopProxyStatus based on Integer32"""
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


_FsSnoopProxyStatus_Type.__name__ = "Integer32"
_FsSnoopProxyStatus_Object = MibTableColumn
fsSnoopProxyStatus = _FsSnoopProxyStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 2, 2, 1, 17),
    _FsSnoopProxyStatus_Type()
)
fsSnoopProxyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopProxyStatus.setStatus("current")


class _FsSnoopQueryFwdOnAllPorts_Type(Integer32):
    """Custom type fsSnoopQueryFwdOnAllPorts based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allports", 1),
          ("nonrtrports", 2))
    )


_FsSnoopQueryFwdOnAllPorts_Type.__name__ = "Integer32"
_FsSnoopQueryFwdOnAllPorts_Object = MibTableColumn
fsSnoopQueryFwdOnAllPorts = _FsSnoopQueryFwdOnAllPorts_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 2, 2, 1, 18),
    _FsSnoopQueryFwdOnAllPorts_Type()
)
fsSnoopQueryFwdOnAllPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopQueryFwdOnAllPorts.setStatus("current")
_FsSnoopFwdGroupsCnt_Type = Integer32
_FsSnoopFwdGroupsCnt_Object = MibTableColumn
fsSnoopFwdGroupsCnt = _FsSnoopFwdGroupsCnt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 2, 2, 1, 19),
    _FsSnoopFwdGroupsCnt_Type()
)
fsSnoopFwdGroupsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopFwdGroupsCnt.setStatus("current")
_FsSnoopVlan_ObjectIdentity = ObjectIdentity
fsSnoopVlan = _FsSnoopVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3)
)
_FsSnoopVlanMcastMacFwdTable_Object = MibTable
fsSnoopVlanMcastMacFwdTable = _FsSnoopVlanMcastMacFwdTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 1)
)
if mibBuilder.loadTexts:
    fsSnoopVlanMcastMacFwdTable.setStatus("current")
_FsSnoopVlanMcastMacFwdEntry_Object = MibTableRow
fsSnoopVlanMcastMacFwdEntry = _FsSnoopVlanMcastMacFwdEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 1, 1)
)
fsSnoopVlanMcastMacFwdEntry.setIndexNames(
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopVlanMcastMacFwdInstId"),
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopVlanMcastMacFwdVlanId"),
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopVlanMcastMacFwdInetAddressType"),
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopVlanMcastMacFwdGroupAddress"),
)
if mibBuilder.loadTexts:
    fsSnoopVlanMcastMacFwdEntry.setStatus("current")


class _FsSnoopVlanMcastMacFwdInstId_Type(Integer32):
    """Custom type fsSnoopVlanMcastMacFwdInstId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsSnoopVlanMcastMacFwdInstId_Type.__name__ = "Integer32"
_FsSnoopVlanMcastMacFwdInstId_Object = MibTableColumn
fsSnoopVlanMcastMacFwdInstId = _FsSnoopVlanMcastMacFwdInstId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 1, 1, 1),
    _FsSnoopVlanMcastMacFwdInstId_Type()
)
fsSnoopVlanMcastMacFwdInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopVlanMcastMacFwdInstId.setStatus("current")


class _FsSnoopVlanMcastMacFwdVlanId_Type(Integer32):
    """Custom type fsSnoopVlanMcastMacFwdVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsSnoopVlanMcastMacFwdVlanId_Type.__name__ = "Integer32"
_FsSnoopVlanMcastMacFwdVlanId_Object = MibTableColumn
fsSnoopVlanMcastMacFwdVlanId = _FsSnoopVlanMcastMacFwdVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 1, 1, 2),
    _FsSnoopVlanMcastMacFwdVlanId_Type()
)
fsSnoopVlanMcastMacFwdVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopVlanMcastMacFwdVlanId.setStatus("current")
_FsSnoopVlanMcastMacFwdInetAddressType_Type = InetAddressType
_FsSnoopVlanMcastMacFwdInetAddressType_Object = MibTableColumn
fsSnoopVlanMcastMacFwdInetAddressType = _FsSnoopVlanMcastMacFwdInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 1, 1, 3),
    _FsSnoopVlanMcastMacFwdInetAddressType_Type()
)
fsSnoopVlanMcastMacFwdInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopVlanMcastMacFwdInetAddressType.setStatus("current")
_FsSnoopVlanMcastMacFwdGroupAddress_Type = MacAddress
_FsSnoopVlanMcastMacFwdGroupAddress_Object = MibTableColumn
fsSnoopVlanMcastMacFwdGroupAddress = _FsSnoopVlanMcastMacFwdGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 1, 1, 4),
    _FsSnoopVlanMcastMacFwdGroupAddress_Type()
)
fsSnoopVlanMcastMacFwdGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopVlanMcastMacFwdGroupAddress.setStatus("current")
_FsSnoopVlanMcastMacFwdPortList_Type = PortList
_FsSnoopVlanMcastMacFwdPortList_Object = MibTableColumn
fsSnoopVlanMcastMacFwdPortList = _FsSnoopVlanMcastMacFwdPortList_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 1, 1, 5),
    _FsSnoopVlanMcastMacFwdPortList_Type()
)
fsSnoopVlanMcastMacFwdPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopVlanMcastMacFwdPortList.setStatus("current")
_FsSnoopVlanMcastMacFwdLocalPortList_Type = PortList
_FsSnoopVlanMcastMacFwdLocalPortList_Object = MibTableColumn
fsSnoopVlanMcastMacFwdLocalPortList = _FsSnoopVlanMcastMacFwdLocalPortList_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 1, 1, 6),
    _FsSnoopVlanMcastMacFwdLocalPortList_Type()
)
fsSnoopVlanMcastMacFwdLocalPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopVlanMcastMacFwdLocalPortList.setStatus("current")
_FsSnoopVlanMcastMacFwdEntryFlag_Type = Integer32
_FsSnoopVlanMcastMacFwdEntryFlag_Object = MibTableColumn
fsSnoopVlanMcastMacFwdEntryFlag = _FsSnoopVlanMcastMacFwdEntryFlag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 1, 1, 7),
    _FsSnoopVlanMcastMacFwdEntryFlag_Type()
)
fsSnoopVlanMcastMacFwdEntryFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopVlanMcastMacFwdEntryFlag.setStatus("current")
_FsSnoopVlanMcastIpFwdTable_Object = MibTable
fsSnoopVlanMcastIpFwdTable = _FsSnoopVlanMcastIpFwdTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 2)
)
if mibBuilder.loadTexts:
    fsSnoopVlanMcastIpFwdTable.setStatus("deprecated")
_FsSnoopVlanMcastIpFwdEntry_Object = MibTableRow
fsSnoopVlanMcastIpFwdEntry = _FsSnoopVlanMcastIpFwdEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 2, 1)
)
fsSnoopVlanMcastIpFwdEntry.setIndexNames(
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopVlanMcastIpFwdInstId"),
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopVlanMcastIpFwdVlanId"),
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopVlanMcastIpFwdAddressType"),
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopVlanMcastIpFwdSourceAddress"),
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopVlanMcastIpFwdGroupAddress"),
)
if mibBuilder.loadTexts:
    fsSnoopVlanMcastIpFwdEntry.setStatus("deprecated")


class _FsSnoopVlanMcastIpFwdInstId_Type(Integer32):
    """Custom type fsSnoopVlanMcastIpFwdInstId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsSnoopVlanMcastIpFwdInstId_Type.__name__ = "Integer32"
_FsSnoopVlanMcastIpFwdInstId_Object = MibTableColumn
fsSnoopVlanMcastIpFwdInstId = _FsSnoopVlanMcastIpFwdInstId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 2, 1, 1),
    _FsSnoopVlanMcastIpFwdInstId_Type()
)
fsSnoopVlanMcastIpFwdInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopVlanMcastIpFwdInstId.setStatus("deprecated")


class _FsSnoopVlanMcastIpFwdVlanId_Type(Integer32):
    """Custom type fsSnoopVlanMcastIpFwdVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsSnoopVlanMcastIpFwdVlanId_Type.__name__ = "Integer32"
_FsSnoopVlanMcastIpFwdVlanId_Object = MibTableColumn
fsSnoopVlanMcastIpFwdVlanId = _FsSnoopVlanMcastIpFwdVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 2, 1, 2),
    _FsSnoopVlanMcastIpFwdVlanId_Type()
)
fsSnoopVlanMcastIpFwdVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopVlanMcastIpFwdVlanId.setStatus("deprecated")
_FsSnoopVlanMcastIpFwdAddressType_Type = InetAddressType
_FsSnoopVlanMcastIpFwdAddressType_Object = MibTableColumn
fsSnoopVlanMcastIpFwdAddressType = _FsSnoopVlanMcastIpFwdAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 2, 1, 3),
    _FsSnoopVlanMcastIpFwdAddressType_Type()
)
fsSnoopVlanMcastIpFwdAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopVlanMcastIpFwdAddressType.setStatus("deprecated")


class _FsSnoopVlanMcastIpFwdSourceAddress_Type(InetAddress):
    """Custom type fsSnoopVlanMcastIpFwdSourceAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsSnoopVlanMcastIpFwdSourceAddress_Type.__name__ = "InetAddress"
_FsSnoopVlanMcastIpFwdSourceAddress_Object = MibTableColumn
fsSnoopVlanMcastIpFwdSourceAddress = _FsSnoopVlanMcastIpFwdSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 2, 1, 4),
    _FsSnoopVlanMcastIpFwdSourceAddress_Type()
)
fsSnoopVlanMcastIpFwdSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopVlanMcastIpFwdSourceAddress.setStatus("deprecated")


class _FsSnoopVlanMcastIpFwdGroupAddress_Type(InetAddress):
    """Custom type fsSnoopVlanMcastIpFwdGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsSnoopVlanMcastIpFwdGroupAddress_Type.__name__ = "InetAddress"
_FsSnoopVlanMcastIpFwdGroupAddress_Object = MibTableColumn
fsSnoopVlanMcastIpFwdGroupAddress = _FsSnoopVlanMcastIpFwdGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 2, 1, 5),
    _FsSnoopVlanMcastIpFwdGroupAddress_Type()
)
fsSnoopVlanMcastIpFwdGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopVlanMcastIpFwdGroupAddress.setStatus("deprecated")
_FsSnoopVlanMcastIpFwdPortList_Type = PortList
_FsSnoopVlanMcastIpFwdPortList_Object = MibTableColumn
fsSnoopVlanMcastIpFwdPortList = _FsSnoopVlanMcastIpFwdPortList_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 2, 1, 6),
    _FsSnoopVlanMcastIpFwdPortList_Type()
)
fsSnoopVlanMcastIpFwdPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopVlanMcastIpFwdPortList.setStatus("deprecated")
_FsSnoopVlanMcastIpFwdEntryFlag_Type = Integer32
_FsSnoopVlanMcastIpFwdEntryFlag_Object = MibTableColumn
fsSnoopVlanMcastIpFwdEntryFlag = _FsSnoopVlanMcastIpFwdEntryFlag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 2, 1, 7),
    _FsSnoopVlanMcastIpFwdEntryFlag_Type()
)
fsSnoopVlanMcastIpFwdEntryFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopVlanMcastIpFwdEntryFlag.setStatus("current")
_FsSnoopVlanRouterTable_Object = MibTable
fsSnoopVlanRouterTable = _FsSnoopVlanRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 3)
)
if mibBuilder.loadTexts:
    fsSnoopVlanRouterTable.setStatus("current")
_FsSnoopVlanRouterEntry_Object = MibTableRow
fsSnoopVlanRouterEntry = _FsSnoopVlanRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 3, 1)
)
fsSnoopVlanRouterEntry.setIndexNames(
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopVlanRouterInstId"),
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopVlanRouterVlanId"),
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopVlanRouterInetAddressType"),
)
if mibBuilder.loadTexts:
    fsSnoopVlanRouterEntry.setStatus("current")


class _FsSnoopVlanRouterInstId_Type(Integer32):
    """Custom type fsSnoopVlanRouterInstId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsSnoopVlanRouterInstId_Type.__name__ = "Integer32"
_FsSnoopVlanRouterInstId_Object = MibTableColumn
fsSnoopVlanRouterInstId = _FsSnoopVlanRouterInstId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 3, 1, 1),
    _FsSnoopVlanRouterInstId_Type()
)
fsSnoopVlanRouterInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopVlanRouterInstId.setStatus("current")


class _FsSnoopVlanRouterVlanId_Type(Integer32):
    """Custom type fsSnoopVlanRouterVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsSnoopVlanRouterVlanId_Type.__name__ = "Integer32"
_FsSnoopVlanRouterVlanId_Object = MibTableColumn
fsSnoopVlanRouterVlanId = _FsSnoopVlanRouterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 3, 1, 2),
    _FsSnoopVlanRouterVlanId_Type()
)
fsSnoopVlanRouterVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopVlanRouterVlanId.setStatus("current")
_FsSnoopVlanRouterInetAddressType_Type = InetAddressType
_FsSnoopVlanRouterInetAddressType_Object = MibTableColumn
fsSnoopVlanRouterInetAddressType = _FsSnoopVlanRouterInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 3, 1, 3),
    _FsSnoopVlanRouterInetAddressType_Type()
)
fsSnoopVlanRouterInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopVlanRouterInetAddressType.setStatus("current")
_FsSnoopVlanRouterPortList_Type = PortList
_FsSnoopVlanRouterPortList_Object = MibTableColumn
fsSnoopVlanRouterPortList = _FsSnoopVlanRouterPortList_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 3, 1, 4),
    _FsSnoopVlanRouterPortList_Type()
)
fsSnoopVlanRouterPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopVlanRouterPortList.setStatus("current")
_FsSnoopVlanRouterLocalPortList_Type = PortList
_FsSnoopVlanRouterLocalPortList_Object = MibTableColumn
fsSnoopVlanRouterLocalPortList = _FsSnoopVlanRouterLocalPortList_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 3, 1, 5),
    _FsSnoopVlanRouterLocalPortList_Type()
)
fsSnoopVlanRouterLocalPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopVlanRouterLocalPortList.setStatus("current")
_FsSnoopVlanFilterTable_Object = MibTable
fsSnoopVlanFilterTable = _FsSnoopVlanFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 4)
)
if mibBuilder.loadTexts:
    fsSnoopVlanFilterTable.setStatus("current")
_FsSnoopVlanFilterEntry_Object = MibTableRow
fsSnoopVlanFilterEntry = _FsSnoopVlanFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 4, 1)
)
fsSnoopVlanFilterEntry.setIndexNames(
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopVlanFilterInstId"),
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopVlanFilterVlanId"),
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopVlanFilterInetAddressType"),
)
if mibBuilder.loadTexts:
    fsSnoopVlanFilterEntry.setStatus("current")


class _FsSnoopVlanFilterInstId_Type(Integer32):
    """Custom type fsSnoopVlanFilterInstId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsSnoopVlanFilterInstId_Type.__name__ = "Integer32"
_FsSnoopVlanFilterInstId_Object = MibTableColumn
fsSnoopVlanFilterInstId = _FsSnoopVlanFilterInstId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 4, 1, 1),
    _FsSnoopVlanFilterInstId_Type()
)
fsSnoopVlanFilterInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopVlanFilterInstId.setStatus("current")


class _FsSnoopVlanFilterVlanId_Type(Integer32):
    """Custom type fsSnoopVlanFilterVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsSnoopVlanFilterVlanId_Type.__name__ = "Integer32"
_FsSnoopVlanFilterVlanId_Object = MibTableColumn
fsSnoopVlanFilterVlanId = _FsSnoopVlanFilterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 4, 1, 2),
    _FsSnoopVlanFilterVlanId_Type()
)
fsSnoopVlanFilterVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopVlanFilterVlanId.setStatus("current")
_FsSnoopVlanFilterInetAddressType_Type = InetAddressType
_FsSnoopVlanFilterInetAddressType_Object = MibTableColumn
fsSnoopVlanFilterInetAddressType = _FsSnoopVlanFilterInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 4, 1, 3),
    _FsSnoopVlanFilterInetAddressType_Type()
)
fsSnoopVlanFilterInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopVlanFilterInetAddressType.setStatus("current")


class _FsSnoopVlanSnoopStatus_Type(Integer32):
    """Custom type fsSnoopVlanSnoopStatus based on Integer32"""
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


_FsSnoopVlanSnoopStatus_Type.__name__ = "Integer32"
_FsSnoopVlanSnoopStatus_Object = MibTableColumn
fsSnoopVlanSnoopStatus = _FsSnoopVlanSnoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 4, 1, 4),
    _FsSnoopVlanSnoopStatus_Type()
)
fsSnoopVlanSnoopStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopVlanSnoopStatus.setStatus("current")


class _FsSnoopVlanOperatingVersion_Type(Integer32):
    """Custom type fsSnoopVlanOperatingVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2),
          ("v3", 3))
    )


_FsSnoopVlanOperatingVersion_Type.__name__ = "Integer32"
_FsSnoopVlanOperatingVersion_Object = MibTableColumn
fsSnoopVlanOperatingVersion = _FsSnoopVlanOperatingVersion_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 4, 1, 5),
    _FsSnoopVlanOperatingVersion_Type()
)
fsSnoopVlanOperatingVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopVlanOperatingVersion.setStatus("deprecated")


class _FsSnoopVlanCfgOperVersion_Type(Integer32):
    """Custom type fsSnoopVlanCfgOperVersion based on Integer32"""
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
        *(("v1", 1),
          ("v2", 2),
          ("v3", 3))
    )


_FsSnoopVlanCfgOperVersion_Type.__name__ = "Integer32"
_FsSnoopVlanCfgOperVersion_Object = MibTableColumn
fsSnoopVlanCfgOperVersion = _FsSnoopVlanCfgOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 4, 1, 6),
    _FsSnoopVlanCfgOperVersion_Type()
)
fsSnoopVlanCfgOperVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopVlanCfgOperVersion.setStatus("deprecated")


class _FsSnoopVlanFastLeave_Type(Integer32):
    """Custom type fsSnoopVlanFastLeave based on Integer32"""
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


_FsSnoopVlanFastLeave_Type.__name__ = "Integer32"
_FsSnoopVlanFastLeave_Object = MibTableColumn
fsSnoopVlanFastLeave = _FsSnoopVlanFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 4, 1, 7),
    _FsSnoopVlanFastLeave_Type()
)
fsSnoopVlanFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopVlanFastLeave.setStatus("current")


class _FsSnoopVlanQuerier_Type(Integer32):
    """Custom type fsSnoopVlanQuerier based on Integer32"""
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


_FsSnoopVlanQuerier_Type.__name__ = "Integer32"
_FsSnoopVlanQuerier_Object = MibTableColumn
fsSnoopVlanQuerier = _FsSnoopVlanQuerier_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 4, 1, 8),
    _FsSnoopVlanQuerier_Type()
)
fsSnoopVlanQuerier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopVlanQuerier.setStatus("current")


class _FsSnoopVlanCfgQuerier_Type(Integer32):
    """Custom type fsSnoopVlanCfgQuerier based on Integer32"""
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


_FsSnoopVlanCfgQuerier_Type.__name__ = "Integer32"
_FsSnoopVlanCfgQuerier_Object = MibTableColumn
fsSnoopVlanCfgQuerier = _FsSnoopVlanCfgQuerier_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 4, 1, 9),
    _FsSnoopVlanCfgQuerier_Type()
)
fsSnoopVlanCfgQuerier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopVlanCfgQuerier.setStatus("current")


class _FsSnoopVlanQueryInterval_Type(Integer32):
    """Custom type fsSnoopVlanQueryInterval based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_FsSnoopVlanQueryInterval_Type.__name__ = "Integer32"
_FsSnoopVlanQueryInterval_Object = MibTableColumn
fsSnoopVlanQueryInterval = _FsSnoopVlanQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 4, 1, 10),
    _FsSnoopVlanQueryInterval_Type()
)
fsSnoopVlanQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopVlanQueryInterval.setStatus("current")
_FsSnoopVlanRtrPortList_Type = PortList
_FsSnoopVlanRtrPortList_Object = MibTableColumn
fsSnoopVlanRtrPortList = _FsSnoopVlanRtrPortList_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 4, 1, 11),
    _FsSnoopVlanRtrPortList_Type()
)
fsSnoopVlanRtrPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopVlanRtrPortList.setStatus("current")
_FsSnoopVlanRowStatus_Type = RowStatus
_FsSnoopVlanRowStatus_Object = MibTableColumn
fsSnoopVlanRowStatus = _FsSnoopVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 4, 1, 12),
    _FsSnoopVlanRowStatus_Type()
)
fsSnoopVlanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopVlanRowStatus.setStatus("current")


class _FsSnoopVlanStartupQueryCount_Type(Integer32):
    """Custom type fsSnoopVlanStartupQueryCount based on Integer32"""
    defaultValue = 2


_FsSnoopVlanStartupQueryCount_Type.__name__ = "Integer32"
_FsSnoopVlanStartupQueryCount_Object = MibTableColumn
fsSnoopVlanStartupQueryCount = _FsSnoopVlanStartupQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 4, 1, 13),
    _FsSnoopVlanStartupQueryCount_Type()
)
fsSnoopVlanStartupQueryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopVlanStartupQueryCount.setStatus("current")


class _FsSnoopVlanStartupQueryInterval_Type(Integer32):
    """Custom type fsSnoopVlanStartupQueryInterval based on Integer32"""
    defaultValue = 31

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 150),
    )


_FsSnoopVlanStartupQueryInterval_Type.__name__ = "Integer32"
_FsSnoopVlanStartupQueryInterval_Object = MibTableColumn
fsSnoopVlanStartupQueryInterval = _FsSnoopVlanStartupQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 4, 1, 14),
    _FsSnoopVlanStartupQueryInterval_Type()
)
fsSnoopVlanStartupQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopVlanStartupQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    fsSnoopVlanStartupQueryInterval.setUnits("seconds")


class _FsSnoopVlanOtherQuerierPresentInterval_Type(Integer32):
    """Custom type fsSnoopVlanOtherQuerierPresentInterval based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 1235),
    )


_FsSnoopVlanOtherQuerierPresentInterval_Type.__name__ = "Integer32"
_FsSnoopVlanOtherQuerierPresentInterval_Object = MibTableColumn
fsSnoopVlanOtherQuerierPresentInterval = _FsSnoopVlanOtherQuerierPresentInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 4, 1, 15),
    _FsSnoopVlanOtherQuerierPresentInterval_Type()
)
fsSnoopVlanOtherQuerierPresentInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopVlanOtherQuerierPresentInterval.setStatus("current")
if mibBuilder.loadTexts:
    fsSnoopVlanOtherQuerierPresentInterval.setUnits("seconds")
_FsSnoopVlanMcastGroupTable_Object = MibTable
fsSnoopVlanMcastGroupTable = _FsSnoopVlanMcastGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 5)
)
if mibBuilder.loadTexts:
    fsSnoopVlanMcastGroupTable.setStatus("current")
_FsSnoopVlanMcastGroupEntry_Object = MibTableRow
fsSnoopVlanMcastGroupEntry = _FsSnoopVlanMcastGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 5, 1)
)
fsSnoopVlanMcastGroupEntry.setIndexNames(
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopVlanMcastGroupInstanceId"),
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopVlanMcastGroupOuterVlanId"),
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopVlanMcastGroupInetAddressType"),
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopVlanMcastGroupAddress"),
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopVlanMcastGroupInnerVlanId"),
)
if mibBuilder.loadTexts:
    fsSnoopVlanMcastGroupEntry.setStatus("current")


class _FsSnoopVlanMcastGroupInstanceId_Type(Integer32):
    """Custom type fsSnoopVlanMcastGroupInstanceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsSnoopVlanMcastGroupInstanceId_Type.__name__ = "Integer32"
_FsSnoopVlanMcastGroupInstanceId_Object = MibTableColumn
fsSnoopVlanMcastGroupInstanceId = _FsSnoopVlanMcastGroupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 5, 1, 1),
    _FsSnoopVlanMcastGroupInstanceId_Type()
)
fsSnoopVlanMcastGroupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopVlanMcastGroupInstanceId.setStatus("current")
_FsSnoopVlanMcastGroupOuterVlanId_Type = VlanIndex
_FsSnoopVlanMcastGroupOuterVlanId_Object = MibTableColumn
fsSnoopVlanMcastGroupOuterVlanId = _FsSnoopVlanMcastGroupOuterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 5, 1, 2),
    _FsSnoopVlanMcastGroupOuterVlanId_Type()
)
fsSnoopVlanMcastGroupOuterVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopVlanMcastGroupOuterVlanId.setStatus("current")
_FsSnoopVlanMcastGroupInetAddressType_Type = InetAddressType
_FsSnoopVlanMcastGroupInetAddressType_Object = MibTableColumn
fsSnoopVlanMcastGroupInetAddressType = _FsSnoopVlanMcastGroupInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 5, 1, 3),
    _FsSnoopVlanMcastGroupInetAddressType_Type()
)
fsSnoopVlanMcastGroupInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopVlanMcastGroupInetAddressType.setStatus("current")


class _FsSnoopVlanMcastGroupAddress_Type(InetAddress):
    """Custom type fsSnoopVlanMcastGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsSnoopVlanMcastGroupAddress_Type.__name__ = "InetAddress"
_FsSnoopVlanMcastGroupAddress_Object = MibTableColumn
fsSnoopVlanMcastGroupAddress = _FsSnoopVlanMcastGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 5, 1, 4),
    _FsSnoopVlanMcastGroupAddress_Type()
)
fsSnoopVlanMcastGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopVlanMcastGroupAddress.setStatus("current")
_FsSnoopVlanMcastGroupInnerVlanId_Type = InnerVlanIndex
_FsSnoopVlanMcastGroupInnerVlanId_Object = MibTableColumn
fsSnoopVlanMcastGroupInnerVlanId = _FsSnoopVlanMcastGroupInnerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 5, 1, 5),
    _FsSnoopVlanMcastGroupInnerVlanId_Type()
)
fsSnoopVlanMcastGroupInnerVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopVlanMcastGroupInnerVlanId.setStatus("current")
_FsSnoopVlanMcastGroupPortList_Type = PortList
_FsSnoopVlanMcastGroupPortList_Object = MibTableColumn
fsSnoopVlanMcastGroupPortList = _FsSnoopVlanMcastGroupPortList_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 5, 1, 6),
    _FsSnoopVlanMcastGroupPortList_Type()
)
fsSnoopVlanMcastGroupPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopVlanMcastGroupPortList.setStatus("current")
_FsSnoopVlanMcastGroupLocalPortList_Type = PortList
_FsSnoopVlanMcastGroupLocalPortList_Object = MibTableColumn
fsSnoopVlanMcastGroupLocalPortList = _FsSnoopVlanMcastGroupLocalPortList_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 5, 1, 7),
    _FsSnoopVlanMcastGroupLocalPortList_Type()
)
fsSnoopVlanMcastGroupLocalPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopVlanMcastGroupLocalPortList.setStatus("current")
_FsSnoopVlanMcastReceiverTable_Object = MibTable
fsSnoopVlanMcastReceiverTable = _FsSnoopVlanMcastReceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 6)
)
if mibBuilder.loadTexts:
    fsSnoopVlanMcastReceiverTable.setStatus("current")
_FsSnoopVlanMcastReceiverEntry_Object = MibTableRow
fsSnoopVlanMcastReceiverEntry = _FsSnoopVlanMcastReceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 6, 1)
)
fsSnoopVlanMcastReceiverEntry.setIndexNames(
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopVlanMcastGroupInstanceId"),
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopVlanMcastGroupOuterVlanId"),
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopVlanMcastGroupInetAddressType"),
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopVlanMcastGroupAddress"),
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopVlanMcastGroupInnerVlanId"),
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopVlanMcastReceiverPortIndex"),
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopVlanMcastReceiverHostAddress"),
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopVlanMcastReceiverSourceAddress"),
)
if mibBuilder.loadTexts:
    fsSnoopVlanMcastReceiverEntry.setStatus("current")
_FsSnoopVlanMcastReceiverPortIndex_Type = InterfaceIndex
_FsSnoopVlanMcastReceiverPortIndex_Object = MibTableColumn
fsSnoopVlanMcastReceiverPortIndex = _FsSnoopVlanMcastReceiverPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 6, 1, 1),
    _FsSnoopVlanMcastReceiverPortIndex_Type()
)
fsSnoopVlanMcastReceiverPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopVlanMcastReceiverPortIndex.setStatus("current")


class _FsSnoopVlanMcastReceiverHostAddress_Type(InetAddress):
    """Custom type fsSnoopVlanMcastReceiverHostAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsSnoopVlanMcastReceiverHostAddress_Type.__name__ = "InetAddress"
_FsSnoopVlanMcastReceiverHostAddress_Object = MibTableColumn
fsSnoopVlanMcastReceiverHostAddress = _FsSnoopVlanMcastReceiverHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 6, 1, 2),
    _FsSnoopVlanMcastReceiverHostAddress_Type()
)
fsSnoopVlanMcastReceiverHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopVlanMcastReceiverHostAddress.setStatus("current")


class _FsSnoopVlanMcastReceiverSourceAddress_Type(InetAddress):
    """Custom type fsSnoopVlanMcastReceiverSourceAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsSnoopVlanMcastReceiverSourceAddress_Type.__name__ = "InetAddress"
_FsSnoopVlanMcastReceiverSourceAddress_Object = MibTableColumn
fsSnoopVlanMcastReceiverSourceAddress = _FsSnoopVlanMcastReceiverSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 6, 1, 3),
    _FsSnoopVlanMcastReceiverSourceAddress_Type()
)
fsSnoopVlanMcastReceiverSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopVlanMcastReceiverSourceAddress.setStatus("current")


class _FsSnoopVlanMcastReceiverFilterMode_Type(Integer32):
    """Custom type fsSnoopVlanMcastReceiverFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("include", 1),
          ("exclude", 2))
    )


_FsSnoopVlanMcastReceiverFilterMode_Type.__name__ = "Integer32"
_FsSnoopVlanMcastReceiverFilterMode_Object = MibTableColumn
fsSnoopVlanMcastReceiverFilterMode = _FsSnoopVlanMcastReceiverFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 6, 1, 4),
    _FsSnoopVlanMcastReceiverFilterMode_Type()
)
fsSnoopVlanMcastReceiverFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopVlanMcastReceiverFilterMode.setStatus("current")
_FsSnoopVlanIpFwdTable_Object = MibTable
fsSnoopVlanIpFwdTable = _FsSnoopVlanIpFwdTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 7)
)
if mibBuilder.loadTexts:
    fsSnoopVlanIpFwdTable.setStatus("current")
_FsSnoopVlanIpFwdEntry_Object = MibTableRow
fsSnoopVlanIpFwdEntry = _FsSnoopVlanIpFwdEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 7, 1)
)
fsSnoopVlanIpFwdEntry.setIndexNames(
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopVlanIpFwdInstanceId"),
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopVlanIpFwdOuterVlanId"),
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopVlanIpFwdInetAddressType"),
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopVlanIpFwdSourceAddress"),
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopVlanIpFwdGroupAddress"),
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopVlanIpFwdInnerVlanId"),
)
if mibBuilder.loadTexts:
    fsSnoopVlanIpFwdEntry.setStatus("current")


class _FsSnoopVlanIpFwdInstanceId_Type(Integer32):
    """Custom type fsSnoopVlanIpFwdInstanceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsSnoopVlanIpFwdInstanceId_Type.__name__ = "Integer32"
_FsSnoopVlanIpFwdInstanceId_Object = MibTableColumn
fsSnoopVlanIpFwdInstanceId = _FsSnoopVlanIpFwdInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 7, 1, 1),
    _FsSnoopVlanIpFwdInstanceId_Type()
)
fsSnoopVlanIpFwdInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopVlanIpFwdInstanceId.setStatus("current")
_FsSnoopVlanIpFwdOuterVlanId_Type = VlanIndex
_FsSnoopVlanIpFwdOuterVlanId_Object = MibTableColumn
fsSnoopVlanIpFwdOuterVlanId = _FsSnoopVlanIpFwdOuterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 7, 1, 2),
    _FsSnoopVlanIpFwdOuterVlanId_Type()
)
fsSnoopVlanIpFwdOuterVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopVlanIpFwdOuterVlanId.setStatus("current")
_FsSnoopVlanIpFwdInetAddressType_Type = InetAddressType
_FsSnoopVlanIpFwdInetAddressType_Object = MibTableColumn
fsSnoopVlanIpFwdInetAddressType = _FsSnoopVlanIpFwdInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 7, 1, 3),
    _FsSnoopVlanIpFwdInetAddressType_Type()
)
fsSnoopVlanIpFwdInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopVlanIpFwdInetAddressType.setStatus("current")
_FsSnoopVlanIpFwdSourceAddress_Type = InetAddress
_FsSnoopVlanIpFwdSourceAddress_Object = MibTableColumn
fsSnoopVlanIpFwdSourceAddress = _FsSnoopVlanIpFwdSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 7, 1, 4),
    _FsSnoopVlanIpFwdSourceAddress_Type()
)
fsSnoopVlanIpFwdSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopVlanIpFwdSourceAddress.setStatus("current")
_FsSnoopVlanIpFwdGroupAddress_Type = InetAddress
_FsSnoopVlanIpFwdGroupAddress_Object = MibTableColumn
fsSnoopVlanIpFwdGroupAddress = _FsSnoopVlanIpFwdGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 7, 1, 5),
    _FsSnoopVlanIpFwdGroupAddress_Type()
)
fsSnoopVlanIpFwdGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopVlanIpFwdGroupAddress.setStatus("current")
_FsSnoopVlanIpFwdInnerVlanId_Type = InnerVlanIndex
_FsSnoopVlanIpFwdInnerVlanId_Object = MibTableColumn
fsSnoopVlanIpFwdInnerVlanId = _FsSnoopVlanIpFwdInnerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 7, 1, 6),
    _FsSnoopVlanIpFwdInnerVlanId_Type()
)
fsSnoopVlanIpFwdInnerVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopVlanIpFwdInnerVlanId.setStatus("current")
_FsSnoopVlanIpFwdPortList_Type = PortList
_FsSnoopVlanIpFwdPortList_Object = MibTableColumn
fsSnoopVlanIpFwdPortList = _FsSnoopVlanIpFwdPortList_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 7, 1, 7),
    _FsSnoopVlanIpFwdPortList_Type()
)
fsSnoopVlanIpFwdPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopVlanIpFwdPortList.setStatus("current")
_FsSnoopVlanIpFwdLocalPortList_Type = PortList
_FsSnoopVlanIpFwdLocalPortList_Object = MibTableColumn
fsSnoopVlanIpFwdLocalPortList = _FsSnoopVlanIpFwdLocalPortList_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 7, 1, 8),
    _FsSnoopVlanIpFwdLocalPortList_Type()
)
fsSnoopVlanIpFwdLocalPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopVlanIpFwdLocalPortList.setStatus("current")
_FsSnoopVlanFilterXTable_Object = MibTable
fsSnoopVlanFilterXTable = _FsSnoopVlanFilterXTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 8)
)
if mibBuilder.loadTexts:
    fsSnoopVlanFilterXTable.setStatus("current")
_FsSnoopVlanFilterXEntry_Object = MibTableRow
fsSnoopVlanFilterXEntry = _FsSnoopVlanFilterXEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 8, 1)
)
if mibBuilder.loadTexts:
    fsSnoopVlanFilterXEntry.setStatus("current")
_FsSnoopVlanBlkRtrPortList_Type = PortList
_FsSnoopVlanBlkRtrPortList_Object = MibTableColumn
fsSnoopVlanBlkRtrPortList = _FsSnoopVlanBlkRtrPortList_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 8, 1, 1),
    _FsSnoopVlanBlkRtrPortList_Type()
)
fsSnoopVlanBlkRtrPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopVlanBlkRtrPortList.setStatus("current")


class _FsSnoopVlanFilterMaxLimitType_Type(Integer32):
    """Custom type fsSnoopVlanFilterMaxLimitType based on Integer32"""
    defaultValue = 0

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
          ("groups", 1),
          ("channels", 2))
    )


_FsSnoopVlanFilterMaxLimitType_Type.__name__ = "Integer32"
_FsSnoopVlanFilterMaxLimitType_Object = MibTableColumn
fsSnoopVlanFilterMaxLimitType = _FsSnoopVlanFilterMaxLimitType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 8, 1, 2),
    _FsSnoopVlanFilterMaxLimitType_Type()
)
fsSnoopVlanFilterMaxLimitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopVlanFilterMaxLimitType.setStatus("current")


class _FsSnoopVlanFilterMaxLimit_Type(Unsigned32):
    """Custom type fsSnoopVlanFilterMaxLimit based on Unsigned32"""
    defaultValue = 0


_FsSnoopVlanFilterMaxLimit_Type.__name__ = "Unsigned32"
_FsSnoopVlanFilterMaxLimit_Object = MibTableColumn
fsSnoopVlanFilterMaxLimit = _FsSnoopVlanFilterMaxLimit_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 8, 1, 3),
    _FsSnoopVlanFilterMaxLimit_Type()
)
fsSnoopVlanFilterMaxLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopVlanFilterMaxLimit.setStatus("current")


class _FsSnoopVlanFilter8021pPriority_Type(Integer32):
    """Custom type fsSnoopVlanFilter8021pPriority based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsSnoopVlanFilter8021pPriority_Type.__name__ = "Integer32"
_FsSnoopVlanFilter8021pPriority_Object = MibTableColumn
fsSnoopVlanFilter8021pPriority = _FsSnoopVlanFilter8021pPriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 8, 1, 4),
    _FsSnoopVlanFilter8021pPriority_Type()
)
fsSnoopVlanFilter8021pPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopVlanFilter8021pPriority.setStatus("current")


class _FsSnoopVlanFilterDropReports_Type(Integer32):
    """Custom type fsSnoopVlanFilterDropReports based on Integer32"""
    defaultValue = 0

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
        *(("none", 0),
          ("igmpv1", 1),
          ("igmpv2", 2),
          ("all", 3))
    )


_FsSnoopVlanFilterDropReports_Type.__name__ = "Integer32"
_FsSnoopVlanFilterDropReports_Object = MibTableColumn
fsSnoopVlanFilterDropReports = _FsSnoopVlanFilterDropReports_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 8, 1, 5),
    _FsSnoopVlanFilterDropReports_Type()
)
fsSnoopVlanFilterDropReports.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopVlanFilterDropReports.setStatus("current")


class _FsSnoopVlanMulticastProfileId_Type(Unsigned32):
    """Custom type fsSnoopVlanMulticastProfileId based on Unsigned32"""
    defaultValue = 0


_FsSnoopVlanMulticastProfileId_Type.__name__ = "Unsigned32"
_FsSnoopVlanMulticastProfileId_Object = MibTableColumn
fsSnoopVlanMulticastProfileId = _FsSnoopVlanMulticastProfileId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 8, 1, 6),
    _FsSnoopVlanMulticastProfileId_Type()
)
fsSnoopVlanMulticastProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopVlanMulticastProfileId.setStatus("current")
_FsSnoopVlanPortPurgeInterval_Type = Integer32
_FsSnoopVlanPortPurgeInterval_Object = MibTableColumn
fsSnoopVlanPortPurgeInterval = _FsSnoopVlanPortPurgeInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 8, 1, 7),
    _FsSnoopVlanPortPurgeInterval_Type()
)
fsSnoopVlanPortPurgeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopVlanPortPurgeInterval.setStatus("current")


class _FsSnoopVlanMaxResponseTime_Type(Integer32):
    """Custom type fsSnoopVlanMaxResponseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65025),
    )


_FsSnoopVlanMaxResponseTime_Type.__name__ = "Integer32"
_FsSnoopVlanMaxResponseTime_Object = MibTableColumn
fsSnoopVlanMaxResponseTime = _FsSnoopVlanMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 8, 1, 8),
    _FsSnoopVlanMaxResponseTime_Type()
)
fsSnoopVlanMaxResponseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSnoopVlanMaxResponseTime.setStatus("current")
_FsSnoopVlanRtrLocalPortList_Type = PortList
_FsSnoopVlanRtrLocalPortList_Object = MibTableColumn
fsSnoopVlanRtrLocalPortList = _FsSnoopVlanRtrLocalPortList_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 8, 1, 9),
    _FsSnoopVlanRtrLocalPortList_Type()
)
fsSnoopVlanRtrLocalPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopVlanRtrLocalPortList.setStatus("current")
_FsSnoopVlanBlkRtrLocalPortList_Type = PortList
_FsSnoopVlanBlkRtrLocalPortList_Object = MibTableColumn
fsSnoopVlanBlkRtrLocalPortList = _FsSnoopVlanBlkRtrLocalPortList_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 8, 1, 10),
    _FsSnoopVlanBlkRtrLocalPortList_Type()
)
fsSnoopVlanBlkRtrLocalPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopVlanBlkRtrLocalPortList.setStatus("current")
_FsSnoopVlanStaticMcastGrpTable_Object = MibTable
fsSnoopVlanStaticMcastGrpTable = _FsSnoopVlanStaticMcastGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 9)
)
if mibBuilder.loadTexts:
    fsSnoopVlanStaticMcastGrpTable.setStatus("current")
_FsSnoopVlanStaticMcastGrpEntry_Object = MibTableRow
fsSnoopVlanStaticMcastGrpEntry = _FsSnoopVlanStaticMcastGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 9, 1)
)
fsSnoopVlanStaticMcastGrpEntry.setIndexNames(
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopVlanStaticMcastGrpInstId"),
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopVlanStaticMcastGrpVlanId"),
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopVlanStaticMcastGrpAddressType"),
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopVlanStaticMcastGrpSourceAddress"),
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopVlanStaticMcastGrpGroupAddress"),
)
if mibBuilder.loadTexts:
    fsSnoopVlanStaticMcastGrpEntry.setStatus("current")


class _FsSnoopVlanStaticMcastGrpInstId_Type(Integer32):
    """Custom type fsSnoopVlanStaticMcastGrpInstId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsSnoopVlanStaticMcastGrpInstId_Type.__name__ = "Integer32"
_FsSnoopVlanStaticMcastGrpInstId_Object = MibTableColumn
fsSnoopVlanStaticMcastGrpInstId = _FsSnoopVlanStaticMcastGrpInstId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 9, 1, 1),
    _FsSnoopVlanStaticMcastGrpInstId_Type()
)
fsSnoopVlanStaticMcastGrpInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopVlanStaticMcastGrpInstId.setStatus("current")


class _FsSnoopVlanStaticMcastGrpVlanId_Type(Integer32):
    """Custom type fsSnoopVlanStaticMcastGrpVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsSnoopVlanStaticMcastGrpVlanId_Type.__name__ = "Integer32"
_FsSnoopVlanStaticMcastGrpVlanId_Object = MibTableColumn
fsSnoopVlanStaticMcastGrpVlanId = _FsSnoopVlanStaticMcastGrpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 9, 1, 2),
    _FsSnoopVlanStaticMcastGrpVlanId_Type()
)
fsSnoopVlanStaticMcastGrpVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopVlanStaticMcastGrpVlanId.setStatus("current")
_FsSnoopVlanStaticMcastGrpAddressType_Type = InetAddressType
_FsSnoopVlanStaticMcastGrpAddressType_Object = MibTableColumn
fsSnoopVlanStaticMcastGrpAddressType = _FsSnoopVlanStaticMcastGrpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 9, 1, 3),
    _FsSnoopVlanStaticMcastGrpAddressType_Type()
)
fsSnoopVlanStaticMcastGrpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopVlanStaticMcastGrpAddressType.setStatus("current")
_FsSnoopVlanStaticMcastGrpSourceAddress_Type = InetAddress
_FsSnoopVlanStaticMcastGrpSourceAddress_Object = MibTableColumn
fsSnoopVlanStaticMcastGrpSourceAddress = _FsSnoopVlanStaticMcastGrpSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 9, 1, 4),
    _FsSnoopVlanStaticMcastGrpSourceAddress_Type()
)
fsSnoopVlanStaticMcastGrpSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopVlanStaticMcastGrpSourceAddress.setStatus("current")
_FsSnoopVlanStaticMcastGrpGroupAddress_Type = InetAddress
_FsSnoopVlanStaticMcastGrpGroupAddress_Object = MibTableColumn
fsSnoopVlanStaticMcastGrpGroupAddress = _FsSnoopVlanStaticMcastGrpGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 9, 1, 5),
    _FsSnoopVlanStaticMcastGrpGroupAddress_Type()
)
fsSnoopVlanStaticMcastGrpGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopVlanStaticMcastGrpGroupAddress.setStatus("current")
_FsSnoopVlanStaticMcastGrpPortList_Type = PortList
_FsSnoopVlanStaticMcastGrpPortList_Object = MibTableColumn
fsSnoopVlanStaticMcastGrpPortList = _FsSnoopVlanStaticMcastGrpPortList_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 9, 1, 6),
    _FsSnoopVlanStaticMcastGrpPortList_Type()
)
fsSnoopVlanStaticMcastGrpPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopVlanStaticMcastGrpPortList.setStatus("current")
_FsSnoopVlanStaticMcastGrpRowStatus_Type = RowStatus
_FsSnoopVlanStaticMcastGrpRowStatus_Object = MibTableColumn
fsSnoopVlanStaticMcastGrpRowStatus = _FsSnoopVlanStaticMcastGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 3, 9, 1, 7),
    _FsSnoopVlanStaticMcastGrpRowStatus_Type()
)
fsSnoopVlanStaticMcastGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSnoopVlanStaticMcastGrpRowStatus.setStatus("current")
_FsSnoopStats_ObjectIdentity = ObjectIdentity
fsSnoopStats = _FsSnoopStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 4)
)
_FsSnoopStatsTable_Object = MibTable
fsSnoopStatsTable = _FsSnoopStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 4, 1)
)
if mibBuilder.loadTexts:
    fsSnoopStatsTable.setStatus("current")
_FsSnoopStatsEntry_Object = MibTableRow
fsSnoopStatsEntry = _FsSnoopStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 4, 1, 1)
)
fsSnoopStatsEntry.setIndexNames(
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopStatsInstId"),
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopStatsVlanId"),
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopStatsInetAddressType"),
)
if mibBuilder.loadTexts:
    fsSnoopStatsEntry.setStatus("current")


class _FsSnoopStatsInstId_Type(Integer32):
    """Custom type fsSnoopStatsInstId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsSnoopStatsInstId_Type.__name__ = "Integer32"
_FsSnoopStatsInstId_Object = MibTableColumn
fsSnoopStatsInstId = _FsSnoopStatsInstId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 4, 1, 1, 1),
    _FsSnoopStatsInstId_Type()
)
fsSnoopStatsInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopStatsInstId.setStatus("current")


class _FsSnoopStatsVlanId_Type(Integer32):
    """Custom type fsSnoopStatsVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsSnoopStatsVlanId_Type.__name__ = "Integer32"
_FsSnoopStatsVlanId_Object = MibTableColumn
fsSnoopStatsVlanId = _FsSnoopStatsVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 4, 1, 1, 2),
    _FsSnoopStatsVlanId_Type()
)
fsSnoopStatsVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopStatsVlanId.setStatus("current")
_FsSnoopStatsInetAddressType_Type = InetAddressType
_FsSnoopStatsInetAddressType_Object = MibTableColumn
fsSnoopStatsInetAddressType = _FsSnoopStatsInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 4, 1, 1, 3),
    _FsSnoopStatsInetAddressType_Type()
)
fsSnoopStatsInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopStatsInetAddressType.setStatus("current")
_FsSnoopStatsRxGenQueries_Type = Counter32
_FsSnoopStatsRxGenQueries_Object = MibTableColumn
fsSnoopStatsRxGenQueries = _FsSnoopStatsRxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 4, 1, 1, 4),
    _FsSnoopStatsRxGenQueries_Type()
)
fsSnoopStatsRxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopStatsRxGenQueries.setStatus("current")
_FsSnoopStatsRxGrpQueries_Type = Counter32
_FsSnoopStatsRxGrpQueries_Object = MibTableColumn
fsSnoopStatsRxGrpQueries = _FsSnoopStatsRxGrpQueries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 4, 1, 1, 5),
    _FsSnoopStatsRxGrpQueries_Type()
)
fsSnoopStatsRxGrpQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopStatsRxGrpQueries.setStatus("current")
_FsSnoopStatsRxGrpAndSrcQueries_Type = Counter32
_FsSnoopStatsRxGrpAndSrcQueries_Object = MibTableColumn
fsSnoopStatsRxGrpAndSrcQueries = _FsSnoopStatsRxGrpAndSrcQueries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 4, 1, 1, 6),
    _FsSnoopStatsRxGrpAndSrcQueries_Type()
)
fsSnoopStatsRxGrpAndSrcQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopStatsRxGrpAndSrcQueries.setStatus("current")
_FsSnoopStatsRxAsmReports_Type = Counter32
_FsSnoopStatsRxAsmReports_Object = MibTableColumn
fsSnoopStatsRxAsmReports = _FsSnoopStatsRxAsmReports_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 4, 1, 1, 7),
    _FsSnoopStatsRxAsmReports_Type()
)
fsSnoopStatsRxAsmReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopStatsRxAsmReports.setStatus("current")
_FsSnoopStatsRxSsmReports_Type = Counter32
_FsSnoopStatsRxSsmReports_Object = MibTableColumn
fsSnoopStatsRxSsmReports = _FsSnoopStatsRxSsmReports_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 4, 1, 1, 8),
    _FsSnoopStatsRxSsmReports_Type()
)
fsSnoopStatsRxSsmReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopStatsRxSsmReports.setStatus("current")
_FsSnoopStatsRxSsmIsInMsgs_Type = Counter32
_FsSnoopStatsRxSsmIsInMsgs_Object = MibTableColumn
fsSnoopStatsRxSsmIsInMsgs = _FsSnoopStatsRxSsmIsInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 4, 1, 1, 9),
    _FsSnoopStatsRxSsmIsInMsgs_Type()
)
fsSnoopStatsRxSsmIsInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopStatsRxSsmIsInMsgs.setStatus("current")
_FsSnoopStatsRxSsmIsExMsgs_Type = Counter32
_FsSnoopStatsRxSsmIsExMsgs_Object = MibTableColumn
fsSnoopStatsRxSsmIsExMsgs = _FsSnoopStatsRxSsmIsExMsgs_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 4, 1, 1, 10),
    _FsSnoopStatsRxSsmIsExMsgs_Type()
)
fsSnoopStatsRxSsmIsExMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopStatsRxSsmIsExMsgs.setStatus("current")
_FsSnoopStatsRxSsmToInMsgs_Type = Counter32
_FsSnoopStatsRxSsmToInMsgs_Object = MibTableColumn
fsSnoopStatsRxSsmToInMsgs = _FsSnoopStatsRxSsmToInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 4, 1, 1, 11),
    _FsSnoopStatsRxSsmToInMsgs_Type()
)
fsSnoopStatsRxSsmToInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopStatsRxSsmToInMsgs.setStatus("current")
_FsSnoopStatsRxSsmToExMsgs_Type = Counter32
_FsSnoopStatsRxSsmToExMsgs_Object = MibTableColumn
fsSnoopStatsRxSsmToExMsgs = _FsSnoopStatsRxSsmToExMsgs_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 4, 1, 1, 12),
    _FsSnoopStatsRxSsmToExMsgs_Type()
)
fsSnoopStatsRxSsmToExMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopStatsRxSsmToExMsgs.setStatus("current")
_FsSnoopStatsRxSsmAllowMsgs_Type = Counter32
_FsSnoopStatsRxSsmAllowMsgs_Object = MibTableColumn
fsSnoopStatsRxSsmAllowMsgs = _FsSnoopStatsRxSsmAllowMsgs_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 4, 1, 1, 13),
    _FsSnoopStatsRxSsmAllowMsgs_Type()
)
fsSnoopStatsRxSsmAllowMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopStatsRxSsmAllowMsgs.setStatus("current")
_FsSnoopStatsRxSsmBlockMsgs_Type = Counter32
_FsSnoopStatsRxSsmBlockMsgs_Object = MibTableColumn
fsSnoopStatsRxSsmBlockMsgs = _FsSnoopStatsRxSsmBlockMsgs_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 4, 1, 1, 14),
    _FsSnoopStatsRxSsmBlockMsgs_Type()
)
fsSnoopStatsRxSsmBlockMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopStatsRxSsmBlockMsgs.setStatus("current")
_FsSnoopStatsRxAsmLeaves_Type = Counter32
_FsSnoopStatsRxAsmLeaves_Object = MibTableColumn
fsSnoopStatsRxAsmLeaves = _FsSnoopStatsRxAsmLeaves_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 4, 1, 1, 15),
    _FsSnoopStatsRxAsmLeaves_Type()
)
fsSnoopStatsRxAsmLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopStatsRxAsmLeaves.setStatus("current")
_FsSnoopStatsTxGenQueries_Type = Counter32
_FsSnoopStatsTxGenQueries_Object = MibTableColumn
fsSnoopStatsTxGenQueries = _FsSnoopStatsTxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 4, 1, 1, 16),
    _FsSnoopStatsTxGenQueries_Type()
)
fsSnoopStatsTxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopStatsTxGenQueries.setStatus("current")
_FsSnoopStatsTxGrpQueries_Type = Counter32
_FsSnoopStatsTxGrpQueries_Object = MibTableColumn
fsSnoopStatsTxGrpQueries = _FsSnoopStatsTxGrpQueries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 4, 1, 1, 17),
    _FsSnoopStatsTxGrpQueries_Type()
)
fsSnoopStatsTxGrpQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopStatsTxGrpQueries.setStatus("current")
_FsSnoopStatsTxGrpAndSrcQueries_Type = Counter32
_FsSnoopStatsTxGrpAndSrcQueries_Object = MibTableColumn
fsSnoopStatsTxGrpAndSrcQueries = _FsSnoopStatsTxGrpAndSrcQueries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 4, 1, 1, 18),
    _FsSnoopStatsTxGrpAndSrcQueries_Type()
)
fsSnoopStatsTxGrpAndSrcQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopStatsTxGrpAndSrcQueries.setStatus("current")
_FsSnoopStatsTxAsmReports_Type = Counter32
_FsSnoopStatsTxAsmReports_Object = MibTableColumn
fsSnoopStatsTxAsmReports = _FsSnoopStatsTxAsmReports_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 4, 1, 1, 19),
    _FsSnoopStatsTxAsmReports_Type()
)
fsSnoopStatsTxAsmReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopStatsTxAsmReports.setStatus("current")
_FsSnoopStatsTxSsmReports_Type = Counter32
_FsSnoopStatsTxSsmReports_Object = MibTableColumn
fsSnoopStatsTxSsmReports = _FsSnoopStatsTxSsmReports_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 4, 1, 1, 20),
    _FsSnoopStatsTxSsmReports_Type()
)
fsSnoopStatsTxSsmReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopStatsTxSsmReports.setStatus("current")
_FsSnoopStatsTxAsmLeaves_Type = Counter32
_FsSnoopStatsTxAsmLeaves_Object = MibTableColumn
fsSnoopStatsTxAsmLeaves = _FsSnoopStatsTxAsmLeaves_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 4, 1, 1, 21),
    _FsSnoopStatsTxAsmLeaves_Type()
)
fsSnoopStatsTxAsmLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopStatsTxAsmLeaves.setStatus("current")
_FsSnoopStatsDroppedPkts_Type = Counter32
_FsSnoopStatsDroppedPkts_Object = MibTableColumn
fsSnoopStatsDroppedPkts = _FsSnoopStatsDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 4, 1, 1, 22),
    _FsSnoopStatsDroppedPkts_Type()
)
fsSnoopStatsDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopStatsDroppedPkts.setStatus("current")
_FsSnoopStatsUnsuccessfulJoins_Type = Counter32
_FsSnoopStatsUnsuccessfulJoins_Object = MibTableColumn
fsSnoopStatsUnsuccessfulJoins = _FsSnoopStatsUnsuccessfulJoins_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 4, 1, 1, 23),
    _FsSnoopStatsUnsuccessfulJoins_Type()
)
fsSnoopStatsUnsuccessfulJoins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopStatsUnsuccessfulJoins.setStatus("current")
_FsSnoopStatsActiveJoins_Type = Counter32
_FsSnoopStatsActiveJoins_Object = MibTableColumn
fsSnoopStatsActiveJoins = _FsSnoopStatsActiveJoins_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 4, 1, 1, 24),
    _FsSnoopStatsActiveJoins_Type()
)
fsSnoopStatsActiveJoins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopStatsActiveJoins.setStatus("current")
_FsSnoopStatsActiveGroups_Type = Counter32
_FsSnoopStatsActiveGroups_Object = MibTableColumn
fsSnoopStatsActiveGroups = _FsSnoopStatsActiveGroups_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 4, 1, 1, 25),
    _FsSnoopStatsActiveGroups_Type()
)
fsSnoopStatsActiveGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopStatsActiveGroups.setStatus("current")
_FsSnoopPort_ObjectIdentity = ObjectIdentity
fsSnoopPort = _FsSnoopPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 5)
)
_FsSnoopPortTable_Object = MibTable
fsSnoopPortTable = _FsSnoopPortTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 5, 1)
)
if mibBuilder.loadTexts:
    fsSnoopPortTable.setStatus("current")
_FsSnoopPortEntry_Object = MibTableRow
fsSnoopPortEntry = _FsSnoopPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 5, 1, 1)
)
fsSnoopPortEntry.setIndexNames(
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopPortIndex"),
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopPortInetAddressType"),
)
if mibBuilder.loadTexts:
    fsSnoopPortEntry.setStatus("current")
_FsSnoopPortIndex_Type = InterfaceIndex
_FsSnoopPortIndex_Object = MibTableColumn
fsSnoopPortIndex = _FsSnoopPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 5, 1, 1, 1),
    _FsSnoopPortIndex_Type()
)
fsSnoopPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopPortIndex.setStatus("current")
_FsSnoopPortInetAddressType_Type = InetAddressType
_FsSnoopPortInetAddressType_Object = MibTableColumn
fsSnoopPortInetAddressType = _FsSnoopPortInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 5, 1, 1, 2),
    _FsSnoopPortInetAddressType_Type()
)
fsSnoopPortInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopPortInetAddressType.setStatus("current")


class _FsSnoopPortLeaveMode_Type(Integer32):
    """Custom type fsSnoopPortLeaveMode based on Integer32"""
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
        *(("explicithosttrack", 1),
          ("fastleave", 2),
          ("normalleave", 3))
    )


_FsSnoopPortLeaveMode_Type.__name__ = "Integer32"
_FsSnoopPortLeaveMode_Object = MibTableColumn
fsSnoopPortLeaveMode = _FsSnoopPortLeaveMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 5, 1, 1, 3),
    _FsSnoopPortLeaveMode_Type()
)
fsSnoopPortLeaveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopPortLeaveMode.setStatus("current")


class _FsSnoopPortRateLimit_Type(Unsigned32):
    """Custom type fsSnoopPortRateLimit based on Unsigned32"""
    defaultValue = 4294967295


_FsSnoopPortRateLimit_Type.__name__ = "Unsigned32"
_FsSnoopPortRateLimit_Object = MibTableColumn
fsSnoopPortRateLimit = _FsSnoopPortRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 5, 1, 1, 4),
    _FsSnoopPortRateLimit_Type()
)
fsSnoopPortRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopPortRateLimit.setStatus("current")


class _FsSnoopPortMaxLimitType_Type(Integer32):
    """Custom type fsSnoopPortMaxLimitType based on Integer32"""
    defaultValue = 0

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
          ("groups", 1),
          ("channels", 2))
    )


_FsSnoopPortMaxLimitType_Type.__name__ = "Integer32"
_FsSnoopPortMaxLimitType_Object = MibTableColumn
fsSnoopPortMaxLimitType = _FsSnoopPortMaxLimitType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 5, 1, 1, 5),
    _FsSnoopPortMaxLimitType_Type()
)
fsSnoopPortMaxLimitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopPortMaxLimitType.setStatus("current")


class _FsSnoopPortMaxLimit_Type(Unsigned32):
    """Custom type fsSnoopPortMaxLimit based on Unsigned32"""
    defaultValue = 0


_FsSnoopPortMaxLimit_Type.__name__ = "Unsigned32"
_FsSnoopPortMaxLimit_Object = MibTableColumn
fsSnoopPortMaxLimit = _FsSnoopPortMaxLimit_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 5, 1, 1, 6),
    _FsSnoopPortMaxLimit_Type()
)
fsSnoopPortMaxLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopPortMaxLimit.setStatus("current")


class _FsSnoopPortProfileId_Type(Unsigned32):
    """Custom type fsSnoopPortProfileId based on Unsigned32"""
    defaultValue = 0


_FsSnoopPortProfileId_Type.__name__ = "Unsigned32"
_FsSnoopPortProfileId_Object = MibTableColumn
fsSnoopPortProfileId = _FsSnoopPortProfileId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 5, 1, 1, 7),
    _FsSnoopPortProfileId_Type()
)
fsSnoopPortProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopPortProfileId.setStatus("current")
_FsSnoopPortMemberCnt_Type = Unsigned32
_FsSnoopPortMemberCnt_Object = MibTableColumn
fsSnoopPortMemberCnt = _FsSnoopPortMemberCnt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 5, 1, 1, 8),
    _FsSnoopPortMemberCnt_Type()
)
fsSnoopPortMemberCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopPortMemberCnt.setStatus("current")
_FsSnoopPortMaxBandwidthLimit_Type = Unsigned32
_FsSnoopPortMaxBandwidthLimit_Object = MibTableColumn
fsSnoopPortMaxBandwidthLimit = _FsSnoopPortMaxBandwidthLimit_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 5, 1, 1, 9),
    _FsSnoopPortMaxBandwidthLimit_Type()
)
fsSnoopPortMaxBandwidthLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopPortMaxBandwidthLimit.setStatus("current")


class _FsSnoopPortDropReports_Type(Integer32):
    """Custom type fsSnoopPortDropReports based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("drop", 2))
    )


_FsSnoopPortDropReports_Type.__name__ = "Integer32"
_FsSnoopPortDropReports_Object = MibTableColumn
fsSnoopPortDropReports = _FsSnoopPortDropReports_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 5, 1, 1, 10),
    _FsSnoopPortDropReports_Type()
)
fsSnoopPortDropReports.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopPortDropReports.setStatus("current")
_FsSnoopPortRowStatus_Type = RowStatus
_FsSnoopPortRowStatus_Object = MibTableColumn
fsSnoopPortRowStatus = _FsSnoopPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 5, 1, 1, 11),
    _FsSnoopPortRowStatus_Type()
)
fsSnoopPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSnoopPortRowStatus.setStatus("current")
_FsSnoopEnhPortTable_Object = MibTable
fsSnoopEnhPortTable = _FsSnoopEnhPortTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 5, 2)
)
if mibBuilder.loadTexts:
    fsSnoopEnhPortTable.setStatus("current")
_FsSnoopEnhPortEntry_Object = MibTableRow
fsSnoopEnhPortEntry = _FsSnoopEnhPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 5, 2, 1)
)
fsSnoopEnhPortEntry.setIndexNames(
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopEnhPortIndex"),
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopEnhPortInnerVlanId"),
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopEnhPortInetAddressType"),
)
if mibBuilder.loadTexts:
    fsSnoopEnhPortEntry.setStatus("current")
_FsSnoopEnhPortIndex_Type = InterfaceIndex
_FsSnoopEnhPortIndex_Object = MibTableColumn
fsSnoopEnhPortIndex = _FsSnoopEnhPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 5, 2, 1, 1),
    _FsSnoopEnhPortIndex_Type()
)
fsSnoopEnhPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopEnhPortIndex.setStatus("current")
_FsSnoopEnhPortInnerVlanId_Type = InnerVlanIndex
_FsSnoopEnhPortInnerVlanId_Object = MibTableColumn
fsSnoopEnhPortInnerVlanId = _FsSnoopEnhPortInnerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 5, 2, 1, 2),
    _FsSnoopEnhPortInnerVlanId_Type()
)
fsSnoopEnhPortInnerVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopEnhPortInnerVlanId.setStatus("current")
_FsSnoopEnhPortInetAddressType_Type = InetAddressType
_FsSnoopEnhPortInetAddressType_Object = MibTableColumn
fsSnoopEnhPortInetAddressType = _FsSnoopEnhPortInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 5, 2, 1, 3),
    _FsSnoopEnhPortInetAddressType_Type()
)
fsSnoopEnhPortInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopEnhPortInetAddressType.setStatus("current")


class _FsSnoopEnhPortLeaveMode_Type(Integer32):
    """Custom type fsSnoopEnhPortLeaveMode based on Integer32"""
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
        *(("explicithosttrack", 1),
          ("fastleave", 2),
          ("normalleave", 3))
    )


_FsSnoopEnhPortLeaveMode_Type.__name__ = "Integer32"
_FsSnoopEnhPortLeaveMode_Object = MibTableColumn
fsSnoopEnhPortLeaveMode = _FsSnoopEnhPortLeaveMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 5, 2, 1, 4),
    _FsSnoopEnhPortLeaveMode_Type()
)
fsSnoopEnhPortLeaveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopEnhPortLeaveMode.setStatus("current")


class _FsSnoopEnhPortRateLimit_Type(Unsigned32):
    """Custom type fsSnoopEnhPortRateLimit based on Unsigned32"""
    defaultValue = 4294967295


_FsSnoopEnhPortRateLimit_Type.__name__ = "Unsigned32"
_FsSnoopEnhPortRateLimit_Object = MibTableColumn
fsSnoopEnhPortRateLimit = _FsSnoopEnhPortRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 5, 2, 1, 5),
    _FsSnoopEnhPortRateLimit_Type()
)
fsSnoopEnhPortRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopEnhPortRateLimit.setStatus("current")


class _FsSnoopEnhPortMaxLimitType_Type(Integer32):
    """Custom type fsSnoopEnhPortMaxLimitType based on Integer32"""
    defaultValue = 0

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
          ("groups", 1),
          ("channels", 2))
    )


_FsSnoopEnhPortMaxLimitType_Type.__name__ = "Integer32"
_FsSnoopEnhPortMaxLimitType_Object = MibTableColumn
fsSnoopEnhPortMaxLimitType = _FsSnoopEnhPortMaxLimitType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 5, 2, 1, 6),
    _FsSnoopEnhPortMaxLimitType_Type()
)
fsSnoopEnhPortMaxLimitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopEnhPortMaxLimitType.setStatus("current")


class _FsSnoopEnhPortMaxLimit_Type(Unsigned32):
    """Custom type fsSnoopEnhPortMaxLimit based on Unsigned32"""
    defaultValue = 0


_FsSnoopEnhPortMaxLimit_Type.__name__ = "Unsigned32"
_FsSnoopEnhPortMaxLimit_Object = MibTableColumn
fsSnoopEnhPortMaxLimit = _FsSnoopEnhPortMaxLimit_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 5, 2, 1, 7),
    _FsSnoopEnhPortMaxLimit_Type()
)
fsSnoopEnhPortMaxLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopEnhPortMaxLimit.setStatus("current")


class _FsSnoopEnhPortProfileId_Type(Unsigned32):
    """Custom type fsSnoopEnhPortProfileId based on Unsigned32"""
    defaultValue = 0


_FsSnoopEnhPortProfileId_Type.__name__ = "Unsigned32"
_FsSnoopEnhPortProfileId_Object = MibTableColumn
fsSnoopEnhPortProfileId = _FsSnoopEnhPortProfileId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 5, 2, 1, 8),
    _FsSnoopEnhPortProfileId_Type()
)
fsSnoopEnhPortProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopEnhPortProfileId.setStatus("current")
_FsSnoopEnhPortMemberCnt_Type = Unsigned32
_FsSnoopEnhPortMemberCnt_Object = MibTableColumn
fsSnoopEnhPortMemberCnt = _FsSnoopEnhPortMemberCnt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 5, 2, 1, 9),
    _FsSnoopEnhPortMemberCnt_Type()
)
fsSnoopEnhPortMemberCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopEnhPortMemberCnt.setStatus("current")
_FsSnoopEnhPortMaxBandwidthLimit_Type = Unsigned32
_FsSnoopEnhPortMaxBandwidthLimit_Object = MibTableColumn
fsSnoopEnhPortMaxBandwidthLimit = _FsSnoopEnhPortMaxBandwidthLimit_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 5, 2, 1, 10),
    _FsSnoopEnhPortMaxBandwidthLimit_Type()
)
fsSnoopEnhPortMaxBandwidthLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopEnhPortMaxBandwidthLimit.setStatus("current")


class _FsSnoopEnhPortDropReports_Type(Integer32):
    """Custom type fsSnoopEnhPortDropReports based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("drop", 2))
    )


_FsSnoopEnhPortDropReports_Type.__name__ = "Integer32"
_FsSnoopEnhPortDropReports_Object = MibTableColumn
fsSnoopEnhPortDropReports = _FsSnoopEnhPortDropReports_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 5, 2, 1, 11),
    _FsSnoopEnhPortDropReports_Type()
)
fsSnoopEnhPortDropReports.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopEnhPortDropReports.setStatus("current")
_FsSnoopEnhPortRowStatus_Type = RowStatus
_FsSnoopEnhPortRowStatus_Object = MibTableColumn
fsSnoopEnhPortRowStatus = _FsSnoopEnhPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 5, 2, 1, 12),
    _FsSnoopEnhPortRowStatus_Type()
)
fsSnoopEnhPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSnoopEnhPortRowStatus.setStatus("current")
_FsSnoopRtrPortTable_Object = MibTable
fsSnoopRtrPortTable = _FsSnoopRtrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 5, 3)
)
if mibBuilder.loadTexts:
    fsSnoopRtrPortTable.setStatus("current")
_FsSnoopRtrPortEntry_Object = MibTableRow
fsSnoopRtrPortEntry = _FsSnoopRtrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 5, 3, 1)
)
fsSnoopRtrPortEntry.setIndexNames(
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopRtrPortIndex"),
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopRtrPortVlanId"),
    (0, "SUPERMICRO-SNOOP-MIB", "fsSnoopRtrPortInetAddressType"),
)
if mibBuilder.loadTexts:
    fsSnoopRtrPortEntry.setStatus("current")
_FsSnoopRtrPortIndex_Type = InterfaceIndex
_FsSnoopRtrPortIndex_Object = MibTableColumn
fsSnoopRtrPortIndex = _FsSnoopRtrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 5, 3, 1, 1),
    _FsSnoopRtrPortIndex_Type()
)
fsSnoopRtrPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopRtrPortIndex.setStatus("current")
_FsSnoopRtrPortVlanId_Type = VlanIndex
_FsSnoopRtrPortVlanId_Object = MibTableColumn
fsSnoopRtrPortVlanId = _FsSnoopRtrPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 5, 3, 1, 2),
    _FsSnoopRtrPortVlanId_Type()
)
fsSnoopRtrPortVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopRtrPortVlanId.setStatus("current")
_FsSnoopRtrPortInetAddressType_Type = InetAddressType
_FsSnoopRtrPortInetAddressType_Object = MibTableColumn
fsSnoopRtrPortInetAddressType = _FsSnoopRtrPortInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 5, 3, 1, 3),
    _FsSnoopRtrPortInetAddressType_Type()
)
fsSnoopRtrPortInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnoopRtrPortInetAddressType.setStatus("current")


class _FsSnoopRtrPortOperVersion_Type(Integer32):
    """Custom type fsSnoopRtrPortOperVersion based on Integer32"""
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
        *(("v1", 1),
          ("v2", 2),
          ("v3", 3))
    )


_FsSnoopRtrPortOperVersion_Type.__name__ = "Integer32"
_FsSnoopRtrPortOperVersion_Object = MibTableColumn
fsSnoopRtrPortOperVersion = _FsSnoopRtrPortOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 5, 3, 1, 4),
    _FsSnoopRtrPortOperVersion_Type()
)
fsSnoopRtrPortOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopRtrPortOperVersion.setStatus("current")


class _FsSnoopRtrPortCfgOperVersion_Type(Integer32):
    """Custom type fsSnoopRtrPortCfgOperVersion based on Integer32"""
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
        *(("v1", 1),
          ("v2", 2),
          ("v3", 3))
    )


_FsSnoopRtrPortCfgOperVersion_Type.__name__ = "Integer32"
_FsSnoopRtrPortCfgOperVersion_Object = MibTableColumn
fsSnoopRtrPortCfgOperVersion = _FsSnoopRtrPortCfgOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 5, 3, 1, 5),
    _FsSnoopRtrPortCfgOperVersion_Type()
)
fsSnoopRtrPortCfgOperVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopRtrPortCfgOperVersion.setStatus("current")


class _FsSnoopOlderQuerierInterval_Type(Integer32):
    """Custom type fsSnoopOlderQuerierInterval based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_FsSnoopOlderQuerierInterval_Type.__name__ = "Integer32"
_FsSnoopOlderQuerierInterval_Object = MibTableColumn
fsSnoopOlderQuerierInterval = _FsSnoopOlderQuerierInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 5, 3, 1, 6),
    _FsSnoopOlderQuerierInterval_Type()
)
fsSnoopOlderQuerierInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnoopOlderQuerierInterval.setStatus("current")
_FsSnoopV3QuerierInterval_Type = Integer32
_FsSnoopV3QuerierInterval_Object = MibTableColumn
fsSnoopV3QuerierInterval = _FsSnoopV3QuerierInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 5, 3, 1, 7),
    _FsSnoopV3QuerierInterval_Type()
)
fsSnoopV3QuerierInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopV3QuerierInterval.setStatus("current")
_FsXSnoopRtrPortTable_Object = MibTable
fsXSnoopRtrPortTable = _FsXSnoopRtrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 5, 4)
)
if mibBuilder.loadTexts:
    fsXSnoopRtrPortTable.setStatus("current")
_FsXSnoopRtrPortEntry_Object = MibTableRow
fsXSnoopRtrPortEntry = _FsXSnoopRtrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 5, 4, 1)
)
if mibBuilder.loadTexts:
    fsXSnoopRtrPortEntry.setStatus("current")
_FsXSnoopRtrPortRowStatus_Type = RowStatus
_FsXSnoopRtrPortRowStatus_Object = MibTableColumn
fsXSnoopRtrPortRowStatus = _FsXSnoopRtrPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 5, 4, 1, 1),
    _FsXSnoopRtrPortRowStatus_Type()
)
fsXSnoopRtrPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsXSnoopRtrPortRowStatus.setStatus("current")
_FsSnoopTrapObjects_ObjectIdentity = ObjectIdentity
fsSnoopTrapObjects = _FsSnoopTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 6)
)
_FsSnoopTrapObjectsTable_Object = MibTable
fsSnoopTrapObjectsTable = _FsSnoopTrapObjectsTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 6, 5)
)
if mibBuilder.loadTexts:
    fsSnoopTrapObjectsTable.setStatus("current")
_FsSnoopTrapObjectsEntry_Object = MibTableRow
fsSnoopTrapObjectsEntry = _FsSnoopTrapObjectsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 6, 5, 1)
)
if mibBuilder.loadTexts:
    fsSnoopTrapObjectsEntry.setStatus("current")


class _FsSnoopTrapHwErrType_Type(Integer32):
    """Custom type fsSnoopTrapHwErrType based on Integer32"""
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
        *(("hardwareCreate", 0),
          ("hardwareDelete", 1),
          ("hardwarePortAdd", 2),
          ("hardwarePortDelete", 3))
    )


_FsSnoopTrapHwErrType_Type.__name__ = "Integer32"
_FsSnoopTrapHwErrType_Object = MibTableColumn
fsSnoopTrapHwErrType = _FsSnoopTrapHwErrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 6, 5, 1, 1),
    _FsSnoopTrapHwErrType_Type()
)
fsSnoopTrapHwErrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSnoopTrapHwErrType.setStatus("current")
_FsSnoopNotifications_ObjectIdentity = ObjectIdentity
fsSnoopNotifications = _FsSnoopNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 7)
)
_FsSnoopTraps_ObjectIdentity = ObjectIdentity
fsSnoopTraps = _FsSnoopTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 7, 0)
)
fsSnoopVlanFilterEntry.registerAugmentions(
    ("SUPERMICRO-SNOOP-MIB",
     "fsSnoopVlanFilterXEntry")
)
fsSnoopVlanFilterXEntry.setIndexNames(*fsSnoopVlanFilterEntry.getIndexNames())
fsSnoopRtrPortEntry.registerAugmentions(
    ("SUPERMICRO-SNOOP-MIB",
     "fsXSnoopRtrPortEntry")
)
fsXSnoopRtrPortEntry.setIndexNames(*fsSnoopRtrPortEntry.getIndexNames())
fsSnoopVlanIpFwdEntry.registerAugmentions(
    ("SUPERMICRO-SNOOP-MIB",
     "fsSnoopTrapObjectsEntry")
)
fsSnoopTrapObjectsEntry.setIndexNames(*fsSnoopVlanIpFwdEntry.getIndexNames())

# Managed Objects groups


# Notification objects

fsSnoopHwFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 105, 7, 0, 1)
)
fsSnoopHwFailureTrap.setObjects(
    ("SUPERMICRO-SNOOP-MIB", "fsSnoopTrapHwErrType")
)
if mibBuilder.loadTexts:
    fsSnoopHwFailureTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-SNOOP-MIB",
    **{"InnerVlanIndex": InnerVlanIndex,
       "fssnoop": fssnoop,
       "fsSnoopSystem": fsSnoopSystem,
       "fsSnoopInst": fsSnoopInst,
       "fsSnoopInstanceGlobalTable": fsSnoopInstanceGlobalTable,
       "fsSnoopInstanceGlobalEntry": fsSnoopInstanceGlobalEntry,
       "fsSnoopInstanceGlobalInstId": fsSnoopInstanceGlobalInstId,
       "fsSnoopInstanceGlobalMcastFwdMode": fsSnoopInstanceGlobalMcastFwdMode,
       "fsSnoopInstanceGlobalSystemControl": fsSnoopInstanceGlobalSystemControl,
       "fsSnoopInstanceGlobalLeaveConfigLevel": fsSnoopInstanceGlobalLeaveConfigLevel,
       "fsSnoopInstanceGlobalEnhancedMode": fsSnoopInstanceGlobalEnhancedMode,
       "fsSnoopInstanceGlobalReportProcessConfigLevel": fsSnoopInstanceGlobalReportProcessConfigLevel,
       "fsSnoopInstanceGlobalSparseMode": fsSnoopInstanceGlobalSparseMode,
       "fsSnoopInstanceGlobalMulticastFilterStatus": fsSnoopInstanceGlobalMulticastFilterStatus,
       "fsSnoopInstanceConfigTable": fsSnoopInstanceConfigTable,
       "fsSnoopInstanceConfigEntry": fsSnoopInstanceConfigEntry,
       "fsSnoopInstanceConfigInstId": fsSnoopInstanceConfigInstId,
       "fsSnoopInetAddressType": fsSnoopInetAddressType,
       "fsSnoopStatus": fsSnoopStatus,
       "fsSnoopProxyReportingStatus": fsSnoopProxyReportingStatus,
       "fsSnoopRouterPortPurgeInterval": fsSnoopRouterPortPurgeInterval,
       "fsSnoopPortPurgeInterval": fsSnoopPortPurgeInterval,
       "fsSnoopReportForwardInterval": fsSnoopReportForwardInterval,
       "fsSnoopRetryCount": fsSnoopRetryCount,
       "fsSnoopGrpQueryInterval": fsSnoopGrpQueryInterval,
       "fsSnoopReportFwdOnAllPorts": fsSnoopReportFwdOnAllPorts,
       "fsSnoopTraceOption": fsSnoopTraceOption,
       "fsSnoopOperStatus": fsSnoopOperStatus,
       "fsSnoopSendQueryOnTopoChange": fsSnoopSendQueryOnTopoChange,
       "fsSnoopSendLeaveOnTopoChange": fsSnoopSendLeaveOnTopoChange,
       "fsSnoopFilterStatus": fsSnoopFilterStatus,
       "fsSnoopMulticastVlanStatus": fsSnoopMulticastVlanStatus,
       "fsSnoopProxyStatus": fsSnoopProxyStatus,
       "fsSnoopQueryFwdOnAllPorts": fsSnoopQueryFwdOnAllPorts,
       "fsSnoopFwdGroupsCnt": fsSnoopFwdGroupsCnt,
       "fsSnoopVlan": fsSnoopVlan,
       "fsSnoopVlanMcastMacFwdTable": fsSnoopVlanMcastMacFwdTable,
       "fsSnoopVlanMcastMacFwdEntry": fsSnoopVlanMcastMacFwdEntry,
       "fsSnoopVlanMcastMacFwdInstId": fsSnoopVlanMcastMacFwdInstId,
       "fsSnoopVlanMcastMacFwdVlanId": fsSnoopVlanMcastMacFwdVlanId,
       "fsSnoopVlanMcastMacFwdInetAddressType": fsSnoopVlanMcastMacFwdInetAddressType,
       "fsSnoopVlanMcastMacFwdGroupAddress": fsSnoopVlanMcastMacFwdGroupAddress,
       "fsSnoopVlanMcastMacFwdPortList": fsSnoopVlanMcastMacFwdPortList,
       "fsSnoopVlanMcastMacFwdLocalPortList": fsSnoopVlanMcastMacFwdLocalPortList,
       "fsSnoopVlanMcastMacFwdEntryFlag": fsSnoopVlanMcastMacFwdEntryFlag,
       "fsSnoopVlanMcastIpFwdTable": fsSnoopVlanMcastIpFwdTable,
       "fsSnoopVlanMcastIpFwdEntry": fsSnoopVlanMcastIpFwdEntry,
       "fsSnoopVlanMcastIpFwdInstId": fsSnoopVlanMcastIpFwdInstId,
       "fsSnoopVlanMcastIpFwdVlanId": fsSnoopVlanMcastIpFwdVlanId,
       "fsSnoopVlanMcastIpFwdAddressType": fsSnoopVlanMcastIpFwdAddressType,
       "fsSnoopVlanMcastIpFwdSourceAddress": fsSnoopVlanMcastIpFwdSourceAddress,
       "fsSnoopVlanMcastIpFwdGroupAddress": fsSnoopVlanMcastIpFwdGroupAddress,
       "fsSnoopVlanMcastIpFwdPortList": fsSnoopVlanMcastIpFwdPortList,
       "fsSnoopVlanMcastIpFwdEntryFlag": fsSnoopVlanMcastIpFwdEntryFlag,
       "fsSnoopVlanRouterTable": fsSnoopVlanRouterTable,
       "fsSnoopVlanRouterEntry": fsSnoopVlanRouterEntry,
       "fsSnoopVlanRouterInstId": fsSnoopVlanRouterInstId,
       "fsSnoopVlanRouterVlanId": fsSnoopVlanRouterVlanId,
       "fsSnoopVlanRouterInetAddressType": fsSnoopVlanRouterInetAddressType,
       "fsSnoopVlanRouterPortList": fsSnoopVlanRouterPortList,
       "fsSnoopVlanRouterLocalPortList": fsSnoopVlanRouterLocalPortList,
       "fsSnoopVlanFilterTable": fsSnoopVlanFilterTable,
       "fsSnoopVlanFilterEntry": fsSnoopVlanFilterEntry,
       "fsSnoopVlanFilterInstId": fsSnoopVlanFilterInstId,
       "fsSnoopVlanFilterVlanId": fsSnoopVlanFilterVlanId,
       "fsSnoopVlanFilterInetAddressType": fsSnoopVlanFilterInetAddressType,
       "fsSnoopVlanSnoopStatus": fsSnoopVlanSnoopStatus,
       "fsSnoopVlanOperatingVersion": fsSnoopVlanOperatingVersion,
       "fsSnoopVlanCfgOperVersion": fsSnoopVlanCfgOperVersion,
       "fsSnoopVlanFastLeave": fsSnoopVlanFastLeave,
       "fsSnoopVlanQuerier": fsSnoopVlanQuerier,
       "fsSnoopVlanCfgQuerier": fsSnoopVlanCfgQuerier,
       "fsSnoopVlanQueryInterval": fsSnoopVlanQueryInterval,
       "fsSnoopVlanRtrPortList": fsSnoopVlanRtrPortList,
       "fsSnoopVlanRowStatus": fsSnoopVlanRowStatus,
       "fsSnoopVlanStartupQueryCount": fsSnoopVlanStartupQueryCount,
       "fsSnoopVlanStartupQueryInterval": fsSnoopVlanStartupQueryInterval,
       "fsSnoopVlanOtherQuerierPresentInterval": fsSnoopVlanOtherQuerierPresentInterval,
       "fsSnoopVlanMcastGroupTable": fsSnoopVlanMcastGroupTable,
       "fsSnoopVlanMcastGroupEntry": fsSnoopVlanMcastGroupEntry,
       "fsSnoopVlanMcastGroupInstanceId": fsSnoopVlanMcastGroupInstanceId,
       "fsSnoopVlanMcastGroupOuterVlanId": fsSnoopVlanMcastGroupOuterVlanId,
       "fsSnoopVlanMcastGroupInetAddressType": fsSnoopVlanMcastGroupInetAddressType,
       "fsSnoopVlanMcastGroupAddress": fsSnoopVlanMcastGroupAddress,
       "fsSnoopVlanMcastGroupInnerVlanId": fsSnoopVlanMcastGroupInnerVlanId,
       "fsSnoopVlanMcastGroupPortList": fsSnoopVlanMcastGroupPortList,
       "fsSnoopVlanMcastGroupLocalPortList": fsSnoopVlanMcastGroupLocalPortList,
       "fsSnoopVlanMcastReceiverTable": fsSnoopVlanMcastReceiverTable,
       "fsSnoopVlanMcastReceiverEntry": fsSnoopVlanMcastReceiverEntry,
       "fsSnoopVlanMcastReceiverPortIndex": fsSnoopVlanMcastReceiverPortIndex,
       "fsSnoopVlanMcastReceiverHostAddress": fsSnoopVlanMcastReceiverHostAddress,
       "fsSnoopVlanMcastReceiverSourceAddress": fsSnoopVlanMcastReceiverSourceAddress,
       "fsSnoopVlanMcastReceiverFilterMode": fsSnoopVlanMcastReceiverFilterMode,
       "fsSnoopVlanIpFwdTable": fsSnoopVlanIpFwdTable,
       "fsSnoopVlanIpFwdEntry": fsSnoopVlanIpFwdEntry,
       "fsSnoopVlanIpFwdInstanceId": fsSnoopVlanIpFwdInstanceId,
       "fsSnoopVlanIpFwdOuterVlanId": fsSnoopVlanIpFwdOuterVlanId,
       "fsSnoopVlanIpFwdInetAddressType": fsSnoopVlanIpFwdInetAddressType,
       "fsSnoopVlanIpFwdSourceAddress": fsSnoopVlanIpFwdSourceAddress,
       "fsSnoopVlanIpFwdGroupAddress": fsSnoopVlanIpFwdGroupAddress,
       "fsSnoopVlanIpFwdInnerVlanId": fsSnoopVlanIpFwdInnerVlanId,
       "fsSnoopVlanIpFwdPortList": fsSnoopVlanIpFwdPortList,
       "fsSnoopVlanIpFwdLocalPortList": fsSnoopVlanIpFwdLocalPortList,
       "fsSnoopVlanFilterXTable": fsSnoopVlanFilterXTable,
       "fsSnoopVlanFilterXEntry": fsSnoopVlanFilterXEntry,
       "fsSnoopVlanBlkRtrPortList": fsSnoopVlanBlkRtrPortList,
       "fsSnoopVlanFilterMaxLimitType": fsSnoopVlanFilterMaxLimitType,
       "fsSnoopVlanFilterMaxLimit": fsSnoopVlanFilterMaxLimit,
       "fsSnoopVlanFilter8021pPriority": fsSnoopVlanFilter8021pPriority,
       "fsSnoopVlanFilterDropReports": fsSnoopVlanFilterDropReports,
       "fsSnoopVlanMulticastProfileId": fsSnoopVlanMulticastProfileId,
       "fsSnoopVlanPortPurgeInterval": fsSnoopVlanPortPurgeInterval,
       "fsSnoopVlanMaxResponseTime": fsSnoopVlanMaxResponseTime,
       "fsSnoopVlanRtrLocalPortList": fsSnoopVlanRtrLocalPortList,
       "fsSnoopVlanBlkRtrLocalPortList": fsSnoopVlanBlkRtrLocalPortList,
       "fsSnoopVlanStaticMcastGrpTable": fsSnoopVlanStaticMcastGrpTable,
       "fsSnoopVlanStaticMcastGrpEntry": fsSnoopVlanStaticMcastGrpEntry,
       "fsSnoopVlanStaticMcastGrpInstId": fsSnoopVlanStaticMcastGrpInstId,
       "fsSnoopVlanStaticMcastGrpVlanId": fsSnoopVlanStaticMcastGrpVlanId,
       "fsSnoopVlanStaticMcastGrpAddressType": fsSnoopVlanStaticMcastGrpAddressType,
       "fsSnoopVlanStaticMcastGrpSourceAddress": fsSnoopVlanStaticMcastGrpSourceAddress,
       "fsSnoopVlanStaticMcastGrpGroupAddress": fsSnoopVlanStaticMcastGrpGroupAddress,
       "fsSnoopVlanStaticMcastGrpPortList": fsSnoopVlanStaticMcastGrpPortList,
       "fsSnoopVlanStaticMcastGrpRowStatus": fsSnoopVlanStaticMcastGrpRowStatus,
       "fsSnoopStats": fsSnoopStats,
       "fsSnoopStatsTable": fsSnoopStatsTable,
       "fsSnoopStatsEntry": fsSnoopStatsEntry,
       "fsSnoopStatsInstId": fsSnoopStatsInstId,
       "fsSnoopStatsVlanId": fsSnoopStatsVlanId,
       "fsSnoopStatsInetAddressType": fsSnoopStatsInetAddressType,
       "fsSnoopStatsRxGenQueries": fsSnoopStatsRxGenQueries,
       "fsSnoopStatsRxGrpQueries": fsSnoopStatsRxGrpQueries,
       "fsSnoopStatsRxGrpAndSrcQueries": fsSnoopStatsRxGrpAndSrcQueries,
       "fsSnoopStatsRxAsmReports": fsSnoopStatsRxAsmReports,
       "fsSnoopStatsRxSsmReports": fsSnoopStatsRxSsmReports,
       "fsSnoopStatsRxSsmIsInMsgs": fsSnoopStatsRxSsmIsInMsgs,
       "fsSnoopStatsRxSsmIsExMsgs": fsSnoopStatsRxSsmIsExMsgs,
       "fsSnoopStatsRxSsmToInMsgs": fsSnoopStatsRxSsmToInMsgs,
       "fsSnoopStatsRxSsmToExMsgs": fsSnoopStatsRxSsmToExMsgs,
       "fsSnoopStatsRxSsmAllowMsgs": fsSnoopStatsRxSsmAllowMsgs,
       "fsSnoopStatsRxSsmBlockMsgs": fsSnoopStatsRxSsmBlockMsgs,
       "fsSnoopStatsRxAsmLeaves": fsSnoopStatsRxAsmLeaves,
       "fsSnoopStatsTxGenQueries": fsSnoopStatsTxGenQueries,
       "fsSnoopStatsTxGrpQueries": fsSnoopStatsTxGrpQueries,
       "fsSnoopStatsTxGrpAndSrcQueries": fsSnoopStatsTxGrpAndSrcQueries,
       "fsSnoopStatsTxAsmReports": fsSnoopStatsTxAsmReports,
       "fsSnoopStatsTxSsmReports": fsSnoopStatsTxSsmReports,
       "fsSnoopStatsTxAsmLeaves": fsSnoopStatsTxAsmLeaves,
       "fsSnoopStatsDroppedPkts": fsSnoopStatsDroppedPkts,
       "fsSnoopStatsUnsuccessfulJoins": fsSnoopStatsUnsuccessfulJoins,
       "fsSnoopStatsActiveJoins": fsSnoopStatsActiveJoins,
       "fsSnoopStatsActiveGroups": fsSnoopStatsActiveGroups,
       "fsSnoopPort": fsSnoopPort,
       "fsSnoopPortTable": fsSnoopPortTable,
       "fsSnoopPortEntry": fsSnoopPortEntry,
       "fsSnoopPortIndex": fsSnoopPortIndex,
       "fsSnoopPortInetAddressType": fsSnoopPortInetAddressType,
       "fsSnoopPortLeaveMode": fsSnoopPortLeaveMode,
       "fsSnoopPortRateLimit": fsSnoopPortRateLimit,
       "fsSnoopPortMaxLimitType": fsSnoopPortMaxLimitType,
       "fsSnoopPortMaxLimit": fsSnoopPortMaxLimit,
       "fsSnoopPortProfileId": fsSnoopPortProfileId,
       "fsSnoopPortMemberCnt": fsSnoopPortMemberCnt,
       "fsSnoopPortMaxBandwidthLimit": fsSnoopPortMaxBandwidthLimit,
       "fsSnoopPortDropReports": fsSnoopPortDropReports,
       "fsSnoopPortRowStatus": fsSnoopPortRowStatus,
       "fsSnoopEnhPortTable": fsSnoopEnhPortTable,
       "fsSnoopEnhPortEntry": fsSnoopEnhPortEntry,
       "fsSnoopEnhPortIndex": fsSnoopEnhPortIndex,
       "fsSnoopEnhPortInnerVlanId": fsSnoopEnhPortInnerVlanId,
       "fsSnoopEnhPortInetAddressType": fsSnoopEnhPortInetAddressType,
       "fsSnoopEnhPortLeaveMode": fsSnoopEnhPortLeaveMode,
       "fsSnoopEnhPortRateLimit": fsSnoopEnhPortRateLimit,
       "fsSnoopEnhPortMaxLimitType": fsSnoopEnhPortMaxLimitType,
       "fsSnoopEnhPortMaxLimit": fsSnoopEnhPortMaxLimit,
       "fsSnoopEnhPortProfileId": fsSnoopEnhPortProfileId,
       "fsSnoopEnhPortMemberCnt": fsSnoopEnhPortMemberCnt,
       "fsSnoopEnhPortMaxBandwidthLimit": fsSnoopEnhPortMaxBandwidthLimit,
       "fsSnoopEnhPortDropReports": fsSnoopEnhPortDropReports,
       "fsSnoopEnhPortRowStatus": fsSnoopEnhPortRowStatus,
       "fsSnoopRtrPortTable": fsSnoopRtrPortTable,
       "fsSnoopRtrPortEntry": fsSnoopRtrPortEntry,
       "fsSnoopRtrPortIndex": fsSnoopRtrPortIndex,
       "fsSnoopRtrPortVlanId": fsSnoopRtrPortVlanId,
       "fsSnoopRtrPortInetAddressType": fsSnoopRtrPortInetAddressType,
       "fsSnoopRtrPortOperVersion": fsSnoopRtrPortOperVersion,
       "fsSnoopRtrPortCfgOperVersion": fsSnoopRtrPortCfgOperVersion,
       "fsSnoopOlderQuerierInterval": fsSnoopOlderQuerierInterval,
       "fsSnoopV3QuerierInterval": fsSnoopV3QuerierInterval,
       "fsXSnoopRtrPortTable": fsXSnoopRtrPortTable,
       "fsXSnoopRtrPortEntry": fsXSnoopRtrPortEntry,
       "fsXSnoopRtrPortRowStatus": fsXSnoopRtrPortRowStatus,
       "fsSnoopTrapObjects": fsSnoopTrapObjects,
       "fsSnoopTrapObjectsTable": fsSnoopTrapObjectsTable,
       "fsSnoopTrapObjectsEntry": fsSnoopTrapObjectsEntry,
       "fsSnoopTrapHwErrType": fsSnoopTrapHwErrType,
       "fsSnoopNotifications": fsSnoopNotifications,
       "fsSnoopTraps": fsSnoopTraps,
       "fsSnoopHwFailureTrap": fsSnoopHwFailureTrap}
)
