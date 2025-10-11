# SNMP MIB module (ARICENT-FSB-MI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-FSB-MI-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:42:31 2025
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

fsMIFsbMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102)
)
if mibBuilder.loadTexts:
    fsMIFsbMIB.setRevisions(
        ("2015-06-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsMIFsbContext_ObjectIdentity = ObjectIdentity
fsMIFsbContext = _FsMIFsbContext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 1)
)
_FsMIFsbContextTable_Object = MibTable
fsMIFsbContextTable = _FsMIFsbContextTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 1, 1)
)
if mibBuilder.loadTexts:
    fsMIFsbContextTable.setStatus("current")
_FsMIFsbContextEntry_Object = MibTableRow
fsMIFsbContextEntry = _FsMIFsbContextEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 1, 1, 1)
)
fsMIFsbContextEntry.setIndexNames(
    (0, "ARICENT-FSB-MI-MIB", "fsMIFsbContextId"),
)
if mibBuilder.loadTexts:
    fsMIFsbContextEntry.setStatus("current")
_FsMIFsbContextId_Type = Unsigned32
_FsMIFsbContextId_Object = MibTableColumn
fsMIFsbContextId = _FsMIFsbContextId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 1, 1, 1, 1),
    _FsMIFsbContextId_Type()
)
fsMIFsbContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIFsbContextId.setStatus("current")


class _FsMIFsbSystemControl_Type(Integer32):
    """Custom type fsMIFsbSystemControl based on Integer32"""
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


_FsMIFsbSystemControl_Type.__name__ = "Integer32"
_FsMIFsbSystemControl_Object = MibTableColumn
fsMIFsbSystemControl = _FsMIFsbSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 1, 1, 1, 2),
    _FsMIFsbSystemControl_Type()
)
fsMIFsbSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsbSystemControl.setStatus("current")


class _FsMIFsbModuleStatus_Type(Integer32):
    """Custom type fsMIFsbModuleStatus based on Integer32"""
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


_FsMIFsbModuleStatus_Type.__name__ = "Integer32"
_FsMIFsbModuleStatus_Object = MibTableColumn
fsMIFsbModuleStatus = _FsMIFsbModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 1, 1, 1, 3),
    _FsMIFsbModuleStatus_Type()
)
fsMIFsbModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsbModuleStatus.setStatus("current")


class _FsMIFsbFcMapMode_Type(Integer32):
    """Custom type fsMIFsbFcMapMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("global", 1),
          ("vlan", 2))
    )


_FsMIFsbFcMapMode_Type.__name__ = "Integer32"
_FsMIFsbFcMapMode_Object = MibTableColumn
fsMIFsbFcMapMode = _FsMIFsbFcMapMode_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 1, 1, 1, 4),
    _FsMIFsbFcMapMode_Type()
)
fsMIFsbFcMapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsbFcMapMode.setStatus("current")


class _FsMIFsbFcmap_Type(OctetString):
    """Custom type fsMIFsbFcmap based on OctetString"""
    defaultHexValue = "0EFC00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_FsMIFsbFcmap_Type.__name__ = "OctetString"
_FsMIFsbFcmap_Object = MibTableColumn
fsMIFsbFcmap = _FsMIFsbFcmap_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 1, 1, 1, 5),
    _FsMIFsbFcmap_Type()
)
fsMIFsbFcmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsbFcmap.setStatus("current")


class _FsMIFsbHouseKeepingTimePeriod_Type(Unsigned32):
    """Custom type fsMIFsbHouseKeepingTimePeriod based on Unsigned32"""
    defaultValue = 300


_FsMIFsbHouseKeepingTimePeriod_Type.__name__ = "Unsigned32"
_FsMIFsbHouseKeepingTimePeriod_Object = MibTableColumn
fsMIFsbHouseKeepingTimePeriod = _FsMIFsbHouseKeepingTimePeriod_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 1, 1, 1, 6),
    _FsMIFsbHouseKeepingTimePeriod_Type()
)
fsMIFsbHouseKeepingTimePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsbHouseKeepingTimePeriod.setStatus("current")


class _FsMIFsbTraceOption_Type(Integer32):
    """Custom type fsMIFsbTraceOption based on Integer32"""
    defaultValue = 0


_FsMIFsbTraceOption_Type.__name__ = "Integer32"
_FsMIFsbTraceOption_Object = MibTableColumn
fsMIFsbTraceOption = _FsMIFsbTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 1, 1, 1, 7),
    _FsMIFsbTraceOption_Type()
)
fsMIFsbTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsbTraceOption.setStatus("current")


class _FsMIFsbTrapStatus_Type(Integer32):
    """Custom type fsMIFsbTrapStatus based on Integer32"""
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


_FsMIFsbTrapStatus_Type.__name__ = "Integer32"
_FsMIFsbTrapStatus_Object = MibTableColumn
fsMIFsbTrapStatus = _FsMIFsbTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 1, 1, 1, 8),
    _FsMIFsbTrapStatus_Type()
)
fsMIFsbTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsbTrapStatus.setStatus("current")
_FsMIFsbClearStats_Type = TruthValue
_FsMIFsbClearStats_Object = MibTableColumn
fsMIFsbClearStats = _FsMIFsbClearStats_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 1, 1, 1, 9),
    _FsMIFsbClearStats_Type()
)
fsMIFsbClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsbClearStats.setStatus("current")
_FsMIFsbDefaultVlanId_Type = VlanId
_FsMIFsbDefaultVlanId_Object = MibTableColumn
fsMIFsbDefaultVlanId = _FsMIFsbDefaultVlanId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 1, 1, 1, 10),
    _FsMIFsbDefaultVlanId_Type()
)
fsMIFsbDefaultVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsbDefaultVlanId.setStatus("current")
_FsMIFsbRowStatus_Type = RowStatus
_FsMIFsbRowStatus_Object = MibTableColumn
fsMIFsbRowStatus = _FsMIFsbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 1, 1, 1, 11),
    _FsMIFsbRowStatus_Type()
)
fsMIFsbRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsbRowStatus.setStatus("current")
_FsMIFsbFIPSnoopingTable_Object = MibTable
fsMIFsbFIPSnoopingTable = _FsMIFsbFIPSnoopingTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 1, 2)
)
if mibBuilder.loadTexts:
    fsMIFsbFIPSnoopingTable.setStatus("current")
_FsMIFsbFIPSnoopingEntry_Object = MibTableRow
fsMIFsbFIPSnoopingEntry = _FsMIFsbFIPSnoopingEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 1, 2, 1)
)
fsMIFsbFIPSnoopingEntry.setIndexNames(
    (0, "ARICENT-FSB-MI-MIB", "fsMIFsbContextId"),
    (0, "ARICENT-FSB-MI-MIB", "fsMIFsbFIPSnoopingVlanIndex"),
)
if mibBuilder.loadTexts:
    fsMIFsbFIPSnoopingEntry.setStatus("current")
_FsMIFsbFIPSnoopingVlanIndex_Type = VlanId
_FsMIFsbFIPSnoopingVlanIndex_Object = MibTableColumn
fsMIFsbFIPSnoopingVlanIndex = _FsMIFsbFIPSnoopingVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 1, 2, 1, 1),
    _FsMIFsbFIPSnoopingVlanIndex_Type()
)
fsMIFsbFIPSnoopingVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIFsbFIPSnoopingVlanIndex.setStatus("current")


class _FsMIFsbFIPSnoopingFcmap_Type(OctetString):
    """Custom type fsMIFsbFIPSnoopingFcmap based on OctetString"""
    defaultHexValue = "0EFC00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_FsMIFsbFIPSnoopingFcmap_Type.__name__ = "OctetString"
_FsMIFsbFIPSnoopingFcmap_Object = MibTableColumn
fsMIFsbFIPSnoopingFcmap = _FsMIFsbFIPSnoopingFcmap_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 1, 2, 1, 2),
    _FsMIFsbFIPSnoopingFcmap_Type()
)
fsMIFsbFIPSnoopingFcmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsbFIPSnoopingFcmap.setStatus("current")


class _FsMIFsbFIPSnoopingEnabledStatus_Type(Integer32):
    """Custom type fsMIFsbFIPSnoopingEnabledStatus based on Integer32"""
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


_FsMIFsbFIPSnoopingEnabledStatus_Type.__name__ = "Integer32"
_FsMIFsbFIPSnoopingEnabledStatus_Object = MibTableColumn
fsMIFsbFIPSnoopingEnabledStatus = _FsMIFsbFIPSnoopingEnabledStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 1, 2, 1, 3),
    _FsMIFsbFIPSnoopingEnabledStatus_Type()
)
fsMIFsbFIPSnoopingEnabledStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsbFIPSnoopingEnabledStatus.setStatus("current")
_FsMIFsbFIPSnoopingRowStatus_Type = RowStatus
_FsMIFsbFIPSnoopingRowStatus_Object = MibTableColumn
fsMIFsbFIPSnoopingRowStatus = _FsMIFsbFIPSnoopingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 1, 2, 1, 4),
    _FsMIFsbFIPSnoopingRowStatus_Type()
)
fsMIFsbFIPSnoopingRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsbFIPSnoopingRowStatus.setStatus("current")
_FsMIFsbSystem_ObjectIdentity = ObjectIdentity
fsMIFsbSystem = _FsMIFsbSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 2)
)
_FsMIFsbIntfTable_Object = MibTable
fsMIFsbIntfTable = _FsMIFsbIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 2, 1)
)
if mibBuilder.loadTexts:
    fsMIFsbIntfTable.setStatus("current")
_FsMIFsbIntfEntry_Object = MibTableRow
fsMIFsbIntfEntry = _FsMIFsbIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 2, 1, 1)
)
fsMIFsbIntfEntry.setIndexNames(
    (0, "ARICENT-FSB-MI-MIB", "fsMIFsbIntfVlanIndex"),
    (0, "ARICENT-FSB-MI-MIB", "fsMIFsbIntfIfIndex"),
)
if mibBuilder.loadTexts:
    fsMIFsbIntfEntry.setStatus("current")
_FsMIFsbIntfVlanIndex_Type = VlanId
_FsMIFsbIntfVlanIndex_Object = MibTableColumn
fsMIFsbIntfVlanIndex = _FsMIFsbIntfVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 2, 1, 1, 1),
    _FsMIFsbIntfVlanIndex_Type()
)
fsMIFsbIntfVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIFsbIntfVlanIndex.setStatus("current")
_FsMIFsbIntfIfIndex_Type = InterfaceIndex
_FsMIFsbIntfIfIndex_Object = MibTableColumn
fsMIFsbIntfIfIndex = _FsMIFsbIntfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 2, 1, 1, 2),
    _FsMIFsbIntfIfIndex_Type()
)
fsMIFsbIntfIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIFsbIntfIfIndex.setStatus("current")


class _FsMIFsbIntfPortRole_Type(Integer32):
    """Custom type fsMIFsbIntfPortRole based on Integer32"""
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
        *(("enodefacing", 1),
          ("fcffacing", 2),
          ("both", 3))
    )


_FsMIFsbIntfPortRole_Type.__name__ = "Integer32"
_FsMIFsbIntfPortRole_Object = MibTableColumn
fsMIFsbIntfPortRole = _FsMIFsbIntfPortRole_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 2, 1, 1, 3),
    _FsMIFsbIntfPortRole_Type()
)
fsMIFsbIntfPortRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsbIntfPortRole.setStatus("current")
_FsMIFsbIntfRowStatus_Type = RowStatus
_FsMIFsbIntfRowStatus_Object = MibTableColumn
fsMIFsbIntfRowStatus = _FsMIFsbIntfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 2, 1, 1, 4),
    _FsMIFsbIntfRowStatus_Type()
)
fsMIFsbIntfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsbIntfRowStatus.setStatus("current")
_FsMIFsbFIPSessionTable_Object = MibTable
fsMIFsbFIPSessionTable = _FsMIFsbFIPSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 2, 2)
)
if mibBuilder.loadTexts:
    fsMIFsbFIPSessionTable.setStatus("current")
_FsMIFsbFIPSessionEntry_Object = MibTableRow
fsMIFsbFIPSessionEntry = _FsMIFsbFIPSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 2, 2, 1)
)
fsMIFsbFIPSessionEntry.setIndexNames(
    (0, "ARICENT-FSB-MI-MIB", "fsMIFsbFIPSessionVlanId"),
    (0, "ARICENT-FSB-MI-MIB", "fsMIFsbFIPSessionEnodeIfIndex"),
    (0, "ARICENT-FSB-MI-MIB", "fsMIFsbFIPSessionEnodeMacAddress"),
    (0, "ARICENT-FSB-MI-MIB", "fsMIFsbFIPSessionFcfMacAddress"),
    (0, "ARICENT-FSB-MI-MIB", "fsMIFsbFIPSessionFCoEMacAddress"),
)
if mibBuilder.loadTexts:
    fsMIFsbFIPSessionEntry.setStatus("current")
_FsMIFsbFIPSessionVlanId_Type = VlanId
_FsMIFsbFIPSessionVlanId_Object = MibTableColumn
fsMIFsbFIPSessionVlanId = _FsMIFsbFIPSessionVlanId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 2, 2, 1, 1),
    _FsMIFsbFIPSessionVlanId_Type()
)
fsMIFsbFIPSessionVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIFsbFIPSessionVlanId.setStatus("current")
_FsMIFsbFIPSessionEnodeIfIndex_Type = InterfaceIndex
_FsMIFsbFIPSessionEnodeIfIndex_Object = MibTableColumn
fsMIFsbFIPSessionEnodeIfIndex = _FsMIFsbFIPSessionEnodeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 2, 2, 1, 2),
    _FsMIFsbFIPSessionEnodeIfIndex_Type()
)
fsMIFsbFIPSessionEnodeIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIFsbFIPSessionEnodeIfIndex.setStatus("current")
_FsMIFsbFIPSessionEnodeMacAddress_Type = MacAddress
_FsMIFsbFIPSessionEnodeMacAddress_Object = MibTableColumn
fsMIFsbFIPSessionEnodeMacAddress = _FsMIFsbFIPSessionEnodeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 2, 2, 1, 3),
    _FsMIFsbFIPSessionEnodeMacAddress_Type()
)
fsMIFsbFIPSessionEnodeMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIFsbFIPSessionEnodeMacAddress.setStatus("current")
_FsMIFsbFIPSessionFcfMacAddress_Type = MacAddress
_FsMIFsbFIPSessionFcfMacAddress_Object = MibTableColumn
fsMIFsbFIPSessionFcfMacAddress = _FsMIFsbFIPSessionFcfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 2, 2, 1, 4),
    _FsMIFsbFIPSessionFcfMacAddress_Type()
)
fsMIFsbFIPSessionFcfMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIFsbFIPSessionFcfMacAddress.setStatus("current")
_FsMIFsbFIPSessionFCoEMacAddress_Type = MacAddress
_FsMIFsbFIPSessionFCoEMacAddress_Object = MibTableColumn
fsMIFsbFIPSessionFCoEMacAddress = _FsMIFsbFIPSessionFCoEMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 2, 2, 1, 5),
    _FsMIFsbFIPSessionFCoEMacAddress_Type()
)
fsMIFsbFIPSessionFCoEMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIFsbFIPSessionFCoEMacAddress.setStatus("current")


class _FsMIFsbFIPSessionFcMap_Type(OctetString):
    """Custom type fsMIFsbFIPSessionFcMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_FsMIFsbFIPSessionFcMap_Type.__name__ = "OctetString"
_FsMIFsbFIPSessionFcMap_Object = MibTableColumn
fsMIFsbFIPSessionFcMap = _FsMIFsbFIPSessionFcMap_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 2, 2, 1, 6),
    _FsMIFsbFIPSessionFcMap_Type()
)
fsMIFsbFIPSessionFcMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsbFIPSessionFcMap.setStatus("current")
_FsMIFsbFIPSessionFcfIfIndex_Type = InterfaceIndex
_FsMIFsbFIPSessionFcfIfIndex_Object = MibTableColumn
fsMIFsbFIPSessionFcfIfIndex = _FsMIFsbFIPSessionFcfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 2, 2, 1, 7),
    _FsMIFsbFIPSessionFcfIfIndex_Type()
)
fsMIFsbFIPSessionFcfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsbFIPSessionFcfIfIndex.setStatus("current")


class _FsMIFsbFIPSessionFcfNameId_Type(OctetString):
    """Custom type fsMIFsbFIPSessionFcfNameId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_FsMIFsbFIPSessionFcfNameId_Type.__name__ = "OctetString"
_FsMIFsbFIPSessionFcfNameId_Object = MibTableColumn
fsMIFsbFIPSessionFcfNameId = _FsMIFsbFIPSessionFcfNameId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 2, 2, 1, 8),
    _FsMIFsbFIPSessionFcfNameId_Type()
)
fsMIFsbFIPSessionFcfNameId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsbFIPSessionFcfNameId.setStatus("current")


class _FsMIFsbFIPSessionFcId_Type(OctetString):
    """Custom type fsMIFsbFIPSessionFcId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_FsMIFsbFIPSessionFcId_Type.__name__ = "OctetString"
_FsMIFsbFIPSessionFcId_Object = MibTableColumn
fsMIFsbFIPSessionFcId = _FsMIFsbFIPSessionFcId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 2, 2, 1, 9),
    _FsMIFsbFIPSessionFcId_Type()
)
fsMIFsbFIPSessionFcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsbFIPSessionFcId.setStatus("current")


class _FsMIFsbFIPSessionEnodeConnectType_Type(Integer32):
    """Custom type fsMIFsbFIPSessionEnodeConnectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flogi", 1),
          ("fdisc", 2))
    )


_FsMIFsbFIPSessionEnodeConnectType_Type.__name__ = "Integer32"
_FsMIFsbFIPSessionEnodeConnectType_Object = MibTableColumn
fsMIFsbFIPSessionEnodeConnectType = _FsMIFsbFIPSessionEnodeConnectType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 2, 2, 1, 10),
    _FsMIFsbFIPSessionEnodeConnectType_Type()
)
fsMIFsbFIPSessionEnodeConnectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsbFIPSessionEnodeConnectType.setStatus("current")
_FsMIFsbFIPSessionHouseKeepingTimerStatus_Type = TruthValue
_FsMIFsbFIPSessionHouseKeepingTimerStatus_Object = MibTableColumn
fsMIFsbFIPSessionHouseKeepingTimerStatus = _FsMIFsbFIPSessionHouseKeepingTimerStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 2, 2, 1, 11),
    _FsMIFsbFIPSessionHouseKeepingTimerStatus_Type()
)
fsMIFsbFIPSessionHouseKeepingTimerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsbFIPSessionHouseKeepingTimerStatus.setStatus("current")
_FsMIFsbFcfTable_Object = MibTable
fsMIFsbFcfTable = _FsMIFsbFcfTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 2, 3)
)
if mibBuilder.loadTexts:
    fsMIFsbFcfTable.setStatus("current")
_FsMIFsbFcfEntry_Object = MibTableRow
fsMIFsbFcfEntry = _FsMIFsbFcfEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 2, 3, 1)
)
fsMIFsbFcfEntry.setIndexNames(
    (0, "ARICENT-FSB-MI-MIB", "fsMIFsbFcfVlanId"),
    (0, "ARICENT-FSB-MI-MIB", "fsMIFsbFcfIfIndex"),
    (0, "ARICENT-FSB-MI-MIB", "fsMIFsbFcfMacAddress"),
)
if mibBuilder.loadTexts:
    fsMIFsbFcfEntry.setStatus("current")
_FsMIFsbFcfVlanId_Type = VlanId
_FsMIFsbFcfVlanId_Object = MibTableColumn
fsMIFsbFcfVlanId = _FsMIFsbFcfVlanId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 2, 3, 1, 1),
    _FsMIFsbFcfVlanId_Type()
)
fsMIFsbFcfVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIFsbFcfVlanId.setStatus("current")
_FsMIFsbFcfIfIndex_Type = InterfaceIndex
_FsMIFsbFcfIfIndex_Object = MibTableColumn
fsMIFsbFcfIfIndex = _FsMIFsbFcfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 2, 3, 1, 2),
    _FsMIFsbFcfIfIndex_Type()
)
fsMIFsbFcfIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIFsbFcfIfIndex.setStatus("current")
_FsMIFsbFcfMacAddress_Type = MacAddress
_FsMIFsbFcfMacAddress_Object = MibTableColumn
fsMIFsbFcfMacAddress = _FsMIFsbFcfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 2, 3, 1, 3),
    _FsMIFsbFcfMacAddress_Type()
)
fsMIFsbFcfMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIFsbFcfMacAddress.setStatus("current")


class _FsMIFsbFcfFcMap_Type(OctetString):
    """Custom type fsMIFsbFcfFcMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_FsMIFsbFcfFcMap_Type.__name__ = "OctetString"
_FsMIFsbFcfFcMap_Object = MibTableColumn
fsMIFsbFcfFcMap = _FsMIFsbFcfFcMap_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 2, 3, 1, 4),
    _FsMIFsbFcfFcMap_Type()
)
fsMIFsbFcfFcMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsbFcfFcMap.setStatus("current")


class _FsMIFsbFcfAddressingMode_Type(Integer32):
    """Custom type fsMIFsbFcfAddressingMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fpma", 1),
          ("spma", 2))
    )


_FsMIFsbFcfAddressingMode_Type.__name__ = "Integer32"
_FsMIFsbFcfAddressingMode_Object = MibTableColumn
fsMIFsbFcfAddressingMode = _FsMIFsbFcfAddressingMode_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 2, 3, 1, 5),
    _FsMIFsbFcfAddressingMode_Type()
)
fsMIFsbFcfAddressingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsbFcfAddressingMode.setStatus("current")
_FsMIFsbFcfEnodeLoginCount_Type = Integer32
_FsMIFsbFcfEnodeLoginCount_Object = MibTableColumn
fsMIFsbFcfEnodeLoginCount = _FsMIFsbFcfEnodeLoginCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 2, 3, 1, 6),
    _FsMIFsbFcfEnodeLoginCount_Type()
)
fsMIFsbFcfEnodeLoginCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsbFcfEnodeLoginCount.setStatus("current")


class _FsMIFsbFcfNameId_Type(OctetString):
    """Custom type fsMIFsbFcfNameId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_FsMIFsbFcfNameId_Type.__name__ = "OctetString"
_FsMIFsbFcfNameId_Object = MibTableColumn
fsMIFsbFcfNameId = _FsMIFsbFcfNameId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 2, 3, 1, 7),
    _FsMIFsbFcfNameId_Type()
)
fsMIFsbFcfNameId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsbFcfNameId.setStatus("current")


class _FsMIFsbFcfFabricName_Type(OctetString):
    """Custom type fsMIFsbFcfFabricName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_FsMIFsbFcfFabricName_Type.__name__ = "OctetString"
_FsMIFsbFcfFabricName_Object = MibTableColumn
fsMIFsbFcfFabricName = _FsMIFsbFcfFabricName_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 2, 3, 1, 8),
    _FsMIFsbFcfFabricName_Type()
)
fsMIFsbFcfFabricName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsbFcfFabricName.setStatus("current")
_FsMIFsbStatistics_ObjectIdentity = ObjectIdentity
fsMIFsbStatistics = _FsMIFsbStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 3)
)
_FsMIFsbGlobalStatsTable_Object = MibTable
fsMIFsbGlobalStatsTable = _FsMIFsbGlobalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 3, 1)
)
if mibBuilder.loadTexts:
    fsMIFsbGlobalStatsTable.setStatus("current")
_FsMIFsbGlobalStatsEntry_Object = MibTableRow
fsMIFsbGlobalStatsEntry = _FsMIFsbGlobalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 3, 1, 1)
)
fsMIFsbGlobalStatsEntry.setIndexNames(
    (0, "ARICENT-FSB-MI-MIB", "fsMIFsbContextId"),
)
if mibBuilder.loadTexts:
    fsMIFsbGlobalStatsEntry.setStatus("current")
_FsMIFsbGlobalStatsVlanRequests_Type = Counter32
_FsMIFsbGlobalStatsVlanRequests_Object = MibTableColumn
fsMIFsbGlobalStatsVlanRequests = _FsMIFsbGlobalStatsVlanRequests_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 3, 1, 1, 1),
    _FsMIFsbGlobalStatsVlanRequests_Type()
)
fsMIFsbGlobalStatsVlanRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsbGlobalStatsVlanRequests.setStatus("current")
_FsMIFsbGlobalStatsVlanNotification_Type = Counter32
_FsMIFsbGlobalStatsVlanNotification_Object = MibTableColumn
fsMIFsbGlobalStatsVlanNotification = _FsMIFsbGlobalStatsVlanNotification_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 3, 1, 1, 2),
    _FsMIFsbGlobalStatsVlanNotification_Type()
)
fsMIFsbGlobalStatsVlanNotification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsbGlobalStatsVlanNotification.setStatus("current")
_FsMIFsbVlanStatsTable_Object = MibTable
fsMIFsbVlanStatsTable = _FsMIFsbVlanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 3, 2)
)
if mibBuilder.loadTexts:
    fsMIFsbVlanStatsTable.setStatus("current")
_FsMIFsbVlanStatsEntry_Object = MibTableRow
fsMIFsbVlanStatsEntry = _FsMIFsbVlanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 3, 2, 1)
)
fsMIFsbVlanStatsEntry.setIndexNames(
    (0, "ARICENT-FSB-MI-MIB", "fsMIFsbContextId"),
    (0, "ARICENT-FSB-MI-MIB", "fsMIFsbFIPSnoopingVlanIndex"),
)
if mibBuilder.loadTexts:
    fsMIFsbVlanStatsEntry.setStatus("current")
_FsMIFsbVlanStatsUnicastDisAdv_Type = Counter32
_FsMIFsbVlanStatsUnicastDisAdv_Object = MibTableColumn
fsMIFsbVlanStatsUnicastDisAdv = _FsMIFsbVlanStatsUnicastDisAdv_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 3, 2, 1, 1),
    _FsMIFsbVlanStatsUnicastDisAdv_Type()
)
fsMIFsbVlanStatsUnicastDisAdv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsbVlanStatsUnicastDisAdv.setStatus("current")
_FsMIFsbVlanStatsMulticastDisAdv_Type = Counter32
_FsMIFsbVlanStatsMulticastDisAdv_Object = MibTableColumn
fsMIFsbVlanStatsMulticastDisAdv = _FsMIFsbVlanStatsMulticastDisAdv_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 3, 2, 1, 2),
    _FsMIFsbVlanStatsMulticastDisAdv_Type()
)
fsMIFsbVlanStatsMulticastDisAdv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsbVlanStatsMulticastDisAdv.setStatus("current")
_FsMIFsbVlanStatsUnicastDisSol_Type = Counter32
_FsMIFsbVlanStatsUnicastDisSol_Object = MibTableColumn
fsMIFsbVlanStatsUnicastDisSol = _FsMIFsbVlanStatsUnicastDisSol_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 3, 2, 1, 3),
    _FsMIFsbVlanStatsUnicastDisSol_Type()
)
fsMIFsbVlanStatsUnicastDisSol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsbVlanStatsUnicastDisSol.setStatus("current")
_FsMIFsbVlanStatsMulticastDisSol_Type = Counter32
_FsMIFsbVlanStatsMulticastDisSol_Object = MibTableColumn
fsMIFsbVlanStatsMulticastDisSol = _FsMIFsbVlanStatsMulticastDisSol_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 3, 2, 1, 4),
    _FsMIFsbVlanStatsMulticastDisSol_Type()
)
fsMIFsbVlanStatsMulticastDisSol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsbVlanStatsMulticastDisSol.setStatus("current")
_FsMIFsbVlanStatsFLOGICount_Type = Counter32
_FsMIFsbVlanStatsFLOGICount_Object = MibTableColumn
fsMIFsbVlanStatsFLOGICount = _FsMIFsbVlanStatsFLOGICount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 3, 2, 1, 5),
    _FsMIFsbVlanStatsFLOGICount_Type()
)
fsMIFsbVlanStatsFLOGICount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsbVlanStatsFLOGICount.setStatus("current")
_FsMIFsbVlanStatsFDISCCount_Type = Counter32
_FsMIFsbVlanStatsFDISCCount_Object = MibTableColumn
fsMIFsbVlanStatsFDISCCount = _FsMIFsbVlanStatsFDISCCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 3, 2, 1, 6),
    _FsMIFsbVlanStatsFDISCCount_Type()
)
fsMIFsbVlanStatsFDISCCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsbVlanStatsFDISCCount.setStatus("current")
_FsMIFsbVlanStatsLOGOCount_Type = Counter32
_FsMIFsbVlanStatsLOGOCount_Object = MibTableColumn
fsMIFsbVlanStatsLOGOCount = _FsMIFsbVlanStatsLOGOCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 3, 2, 1, 7),
    _FsMIFsbVlanStatsLOGOCount_Type()
)
fsMIFsbVlanStatsLOGOCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsbVlanStatsLOGOCount.setStatus("current")
_FsMIFsbVlanStatsFLOGIAcceptCount_Type = Counter32
_FsMIFsbVlanStatsFLOGIAcceptCount_Object = MibTableColumn
fsMIFsbVlanStatsFLOGIAcceptCount = _FsMIFsbVlanStatsFLOGIAcceptCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 3, 2, 1, 8),
    _FsMIFsbVlanStatsFLOGIAcceptCount_Type()
)
fsMIFsbVlanStatsFLOGIAcceptCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsbVlanStatsFLOGIAcceptCount.setStatus("current")
_FsMIFsbVlanStatsFLOGIRejectCount_Type = Counter32
_FsMIFsbVlanStatsFLOGIRejectCount_Object = MibTableColumn
fsMIFsbVlanStatsFLOGIRejectCount = _FsMIFsbVlanStatsFLOGIRejectCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 3, 2, 1, 9),
    _FsMIFsbVlanStatsFLOGIRejectCount_Type()
)
fsMIFsbVlanStatsFLOGIRejectCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsbVlanStatsFLOGIRejectCount.setStatus("current")
_FsMIFsbVlanStatsFDISCAcceptCount_Type = Counter32
_FsMIFsbVlanStatsFDISCAcceptCount_Object = MibTableColumn
fsMIFsbVlanStatsFDISCAcceptCount = _FsMIFsbVlanStatsFDISCAcceptCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 3, 2, 1, 10),
    _FsMIFsbVlanStatsFDISCAcceptCount_Type()
)
fsMIFsbVlanStatsFDISCAcceptCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsbVlanStatsFDISCAcceptCount.setStatus("current")
_FsMIFsbVlanStatsFDISCRejectCount_Type = Counter32
_FsMIFsbVlanStatsFDISCRejectCount_Object = MibTableColumn
fsMIFsbVlanStatsFDISCRejectCount = _FsMIFsbVlanStatsFDISCRejectCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 3, 2, 1, 11),
    _FsMIFsbVlanStatsFDISCRejectCount_Type()
)
fsMIFsbVlanStatsFDISCRejectCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsbVlanStatsFDISCRejectCount.setStatus("current")
_FsMIFsbVlanStatsLOGOAcceptCount_Type = Counter32
_FsMIFsbVlanStatsLOGOAcceptCount_Object = MibTableColumn
fsMIFsbVlanStatsLOGOAcceptCount = _FsMIFsbVlanStatsLOGOAcceptCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 3, 2, 1, 12),
    _FsMIFsbVlanStatsLOGOAcceptCount_Type()
)
fsMIFsbVlanStatsLOGOAcceptCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsbVlanStatsLOGOAcceptCount.setStatus("current")
_FsMIFsbVlanStatsLOGORejectCount_Type = Counter32
_FsMIFsbVlanStatsLOGORejectCount_Object = MibTableColumn
fsMIFsbVlanStatsLOGORejectCount = _FsMIFsbVlanStatsLOGORejectCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 3, 2, 1, 13),
    _FsMIFsbVlanStatsLOGORejectCount_Type()
)
fsMIFsbVlanStatsLOGORejectCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsbVlanStatsLOGORejectCount.setStatus("current")
_FsMIFsbVlanStatsClearLinkCount_Type = Counter32
_FsMIFsbVlanStatsClearLinkCount_Object = MibTableColumn
fsMIFsbVlanStatsClearLinkCount = _FsMIFsbVlanStatsClearLinkCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 3, 2, 1, 14),
    _FsMIFsbVlanStatsClearLinkCount_Type()
)
fsMIFsbVlanStatsClearLinkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsbVlanStatsClearLinkCount.setStatus("current")
_FsMIFsbVlanFcMapMisMatchCount_Type = Counter32
_FsMIFsbVlanFcMapMisMatchCount_Object = MibTableColumn
fsMIFsbVlanFcMapMisMatchCount = _FsMIFsbVlanFcMapMisMatchCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 3, 2, 1, 15),
    _FsMIFsbVlanFcMapMisMatchCount_Type()
)
fsMIFsbVlanFcMapMisMatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsbVlanFcMapMisMatchCount.setStatus("current")
_FsMIFsbVlanMTUMisMatchCount_Type = Counter32
_FsMIFsbVlanMTUMisMatchCount_Object = MibTableColumn
fsMIFsbVlanMTUMisMatchCount = _FsMIFsbVlanMTUMisMatchCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 3, 2, 1, 16),
    _FsMIFsbVlanMTUMisMatchCount_Type()
)
fsMIFsbVlanMTUMisMatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsbVlanMTUMisMatchCount.setStatus("current")
_FsMIFsbVlanACLFailureCount_Type = Counter32
_FsMIFsbVlanACLFailureCount_Object = MibTableColumn
fsMIFsbVlanACLFailureCount = _FsMIFsbVlanACLFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 3, 2, 1, 17),
    _FsMIFsbVlanACLFailureCount_Type()
)
fsMIFsbVlanACLFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsbVlanACLFailureCount.setStatus("current")
_FsMIFsbVlanInvalidFIPFramesCount_Type = Counter32
_FsMIFsbVlanInvalidFIPFramesCount_Object = MibTableColumn
fsMIFsbVlanInvalidFIPFramesCount = _FsMIFsbVlanInvalidFIPFramesCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 3, 2, 1, 18),
    _FsMIFsbVlanInvalidFIPFramesCount_Type()
)
fsMIFsbVlanInvalidFIPFramesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsbVlanInvalidFIPFramesCount.setStatus("current")
_FsMIFsbVlanFCFDiscoveryTimeoutsCount_Type = Counter32
_FsMIFsbVlanFCFDiscoveryTimeoutsCount_Object = MibTableColumn
fsMIFsbVlanFCFDiscoveryTimeoutsCount = _FsMIFsbVlanFCFDiscoveryTimeoutsCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 3, 2, 1, 19),
    _FsMIFsbVlanFCFDiscoveryTimeoutsCount_Type()
)
fsMIFsbVlanFCFDiscoveryTimeoutsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsbVlanFCFDiscoveryTimeoutsCount.setStatus("current")
_FsMIFsbSessStatsTable_Object = MibTable
fsMIFsbSessStatsTable = _FsMIFsbSessStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 3, 3)
)
if mibBuilder.loadTexts:
    fsMIFsbSessStatsTable.setStatus("current")
_FsMIFsbSessStatsEntry_Object = MibTableRow
fsMIFsbSessStatsEntry = _FsMIFsbSessStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 3, 3, 1)
)
fsMIFsbSessStatsEntry.setIndexNames(
    (0, "ARICENT-FSB-MI-MIB", "fsMIFsbSessStatsVlanId"),
    (0, "ARICENT-FSB-MI-MIB", "fsMIFsbSessStatsEnodeIfIndex"),
    (0, "ARICENT-FSB-MI-MIB", "fsMIFsbSessStatsEnodeMacAddress"),
    (0, "ARICENT-FSB-MI-MIB", "fsMIFsbSessStatsFcfMacAddress"),
    (0, "ARICENT-FSB-MI-MIB", "fsMIFsbSessStatsFCoEMacAddress"),
)
if mibBuilder.loadTexts:
    fsMIFsbSessStatsEntry.setStatus("current")


class _FsMIFsbSessStatsVlanId_Type(Integer32):
    """Custom type fsMIFsbSessStatsVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FsMIFsbSessStatsVlanId_Type.__name__ = "Integer32"
_FsMIFsbSessStatsVlanId_Object = MibTableColumn
fsMIFsbSessStatsVlanId = _FsMIFsbSessStatsVlanId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 3, 3, 1, 1),
    _FsMIFsbSessStatsVlanId_Type()
)
fsMIFsbSessStatsVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIFsbSessStatsVlanId.setStatus("current")
_FsMIFsbSessStatsEnodeIfIndex_Type = InterfaceIndex
_FsMIFsbSessStatsEnodeIfIndex_Object = MibTableColumn
fsMIFsbSessStatsEnodeIfIndex = _FsMIFsbSessStatsEnodeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 3, 3, 1, 2),
    _FsMIFsbSessStatsEnodeIfIndex_Type()
)
fsMIFsbSessStatsEnodeIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIFsbSessStatsEnodeIfIndex.setStatus("current")
_FsMIFsbSessStatsEnodeMacAddress_Type = MacAddress
_FsMIFsbSessStatsEnodeMacAddress_Object = MibTableColumn
fsMIFsbSessStatsEnodeMacAddress = _FsMIFsbSessStatsEnodeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 3, 3, 1, 3),
    _FsMIFsbSessStatsEnodeMacAddress_Type()
)
fsMIFsbSessStatsEnodeMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIFsbSessStatsEnodeMacAddress.setStatus("current")
_FsMIFsbSessStatsFcfMacAddress_Type = MacAddress
_FsMIFsbSessStatsFcfMacAddress_Object = MibTableColumn
fsMIFsbSessStatsFcfMacAddress = _FsMIFsbSessStatsFcfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 3, 3, 1, 4),
    _FsMIFsbSessStatsFcfMacAddress_Type()
)
fsMIFsbSessStatsFcfMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIFsbSessStatsFcfMacAddress.setStatus("current")
_FsMIFsbSessStatsFCoEMacAddress_Type = MacAddress
_FsMIFsbSessStatsFCoEMacAddress_Object = MibTableColumn
fsMIFsbSessStatsFCoEMacAddress = _FsMIFsbSessStatsFCoEMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 3, 3, 1, 5),
    _FsMIFsbSessStatsFCoEMacAddress_Type()
)
fsMIFsbSessStatsFCoEMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIFsbSessStatsFCoEMacAddress.setStatus("current")
_FsMIFsbSessStatsEnodeKeepAliveCount_Type = Counter32
_FsMIFsbSessStatsEnodeKeepAliveCount_Object = MibTableColumn
fsMIFsbSessStatsEnodeKeepAliveCount = _FsMIFsbSessStatsEnodeKeepAliveCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 3, 3, 1, 6),
    _FsMIFsbSessStatsEnodeKeepAliveCount_Type()
)
fsMIFsbSessStatsEnodeKeepAliveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsbSessStatsEnodeKeepAliveCount.setStatus("current")
_FsMIFsbSessStatsVNPortKeepAliveCount_Type = Counter32
_FsMIFsbSessStatsVNPortKeepAliveCount_Object = MibTableColumn
fsMIFsbSessStatsVNPortKeepAliveCount = _FsMIFsbSessStatsVNPortKeepAliveCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 3, 3, 1, 7),
    _FsMIFsbSessStatsVNPortKeepAliveCount_Type()
)
fsMIFsbSessStatsVNPortKeepAliveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsbSessStatsVNPortKeepAliveCount.setStatus("current")
_FsMIFsbNotificationObjects_ObjectIdentity = ObjectIdentity
fsMIFsbNotificationObjects = _FsMIFsbNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 4)
)
_FsMIFsbTrapObjects_ObjectIdentity = ObjectIdentity
fsMIFsbTrapObjects = _FsMIFsbTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 4, 1)
)
_FsMIFsbSessionVlanId_Type = VlanId
_FsMIFsbSessionVlanId_Object = MibScalar
fsMIFsbSessionVlanId = _FsMIFsbSessionVlanId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 4, 1, 1),
    _FsMIFsbSessionVlanId_Type()
)
fsMIFsbSessionVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMIFsbSessionVlanId.setStatus("current")
_FsMIFsbSessionEnodeIfIndex_Type = InterfaceIndex
_FsMIFsbSessionEnodeIfIndex_Object = MibScalar
fsMIFsbSessionEnodeIfIndex = _FsMIFsbSessionEnodeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 4, 1, 2),
    _FsMIFsbSessionEnodeIfIndex_Type()
)
fsMIFsbSessionEnodeIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMIFsbSessionEnodeIfIndex.setStatus("current")
_FsMIFsbSessionEnodeMacAddress_Type = MacAddress
_FsMIFsbSessionEnodeMacAddress_Object = MibScalar
fsMIFsbSessionEnodeMacAddress = _FsMIFsbSessionEnodeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 4, 1, 3),
    _FsMIFsbSessionEnodeMacAddress_Type()
)
fsMIFsbSessionEnodeMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMIFsbSessionEnodeMacAddress.setStatus("current")
_FsMIFsbNotifications_ObjectIdentity = ObjectIdentity
fsMIFsbNotifications = _FsMIFsbNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 5)
)
_FsMIFsbTraps_ObjectIdentity = ObjectIdentity
fsMIFsbTraps = _FsMIFsbTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 5, 0)
)

# Managed Objects groups


# Notification objects

fsMIFsbFIPSessionClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 5, 0, 1)
)
fsMIFsbFIPSessionClear.setObjects(
      *(("ARICENT-FSB-MI-MIB", "fsMIFsbSessionVlanId"),
        ("ARICENT-FSB-MI-MIB", "fsMIFsbSessionEnodeIfIndex"),
        ("ARICENT-FSB-MI-MIB", "fsMIFsbSessionEnodeMacAddress"))
)
if mibBuilder.loadTexts:
    fsMIFsbFIPSessionClear.setStatus(
        "current"
    )

fsMIFsbFcmapMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 5, 0, 2)
)
fsMIFsbFcmapMismatch.setObjects(
      *(("ARICENT-FSB-MI-MIB", "fsMIFsbSessionVlanId"),
        ("ARICENT-FSB-MI-MIB", "fsMIFsbSessionEnodeIfIndex"),
        ("ARICENT-FSB-MI-MIB", "fsMIFsbSessionEnodeMacAddress"))
)
if mibBuilder.loadTexts:
    fsMIFsbFcmapMismatch.setStatus(
        "current"
    )

fsMIFsbMTUMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 5, 0, 3)
)
fsMIFsbMTUMismatch.setObjects(
      *(("ARICENT-FSB-MI-MIB", "fsMIFsbSessionVlanId"),
        ("ARICENT-FSB-MI-MIB", "fsMIFsbSessionEnodeIfIndex"),
        ("ARICENT-FSB-MI-MIB", "fsMIFsbSessionEnodeMacAddress"))
)
if mibBuilder.loadTexts:
    fsMIFsbMTUMismatch.setStatus(
        "current"
    )

fsMIFsbAclFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 102, 5, 0, 4)
)
fsMIFsbAclFailure.setObjects(
      *(("ARICENT-FSB-MI-MIB", "fsMIFsbSessionVlanId"),
        ("ARICENT-FSB-MI-MIB", "fsMIFsbSessionEnodeIfIndex"),
        ("ARICENT-FSB-MI-MIB", "fsMIFsbSessionEnodeMacAddress"))
)
if mibBuilder.loadTexts:
    fsMIFsbAclFailure.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-FSB-MI-MIB",
    **{"fsMIFsbMIB": fsMIFsbMIB,
       "fsMIFsbContext": fsMIFsbContext,
       "fsMIFsbContextTable": fsMIFsbContextTable,
       "fsMIFsbContextEntry": fsMIFsbContextEntry,
       "fsMIFsbContextId": fsMIFsbContextId,
       "fsMIFsbSystemControl": fsMIFsbSystemControl,
       "fsMIFsbModuleStatus": fsMIFsbModuleStatus,
       "fsMIFsbFcMapMode": fsMIFsbFcMapMode,
       "fsMIFsbFcmap": fsMIFsbFcmap,
       "fsMIFsbHouseKeepingTimePeriod": fsMIFsbHouseKeepingTimePeriod,
       "fsMIFsbTraceOption": fsMIFsbTraceOption,
       "fsMIFsbTrapStatus": fsMIFsbTrapStatus,
       "fsMIFsbClearStats": fsMIFsbClearStats,
       "fsMIFsbDefaultVlanId": fsMIFsbDefaultVlanId,
       "fsMIFsbRowStatus": fsMIFsbRowStatus,
       "fsMIFsbFIPSnoopingTable": fsMIFsbFIPSnoopingTable,
       "fsMIFsbFIPSnoopingEntry": fsMIFsbFIPSnoopingEntry,
       "fsMIFsbFIPSnoopingVlanIndex": fsMIFsbFIPSnoopingVlanIndex,
       "fsMIFsbFIPSnoopingFcmap": fsMIFsbFIPSnoopingFcmap,
       "fsMIFsbFIPSnoopingEnabledStatus": fsMIFsbFIPSnoopingEnabledStatus,
       "fsMIFsbFIPSnoopingRowStatus": fsMIFsbFIPSnoopingRowStatus,
       "fsMIFsbSystem": fsMIFsbSystem,
       "fsMIFsbIntfTable": fsMIFsbIntfTable,
       "fsMIFsbIntfEntry": fsMIFsbIntfEntry,
       "fsMIFsbIntfVlanIndex": fsMIFsbIntfVlanIndex,
       "fsMIFsbIntfIfIndex": fsMIFsbIntfIfIndex,
       "fsMIFsbIntfPortRole": fsMIFsbIntfPortRole,
       "fsMIFsbIntfRowStatus": fsMIFsbIntfRowStatus,
       "fsMIFsbFIPSessionTable": fsMIFsbFIPSessionTable,
       "fsMIFsbFIPSessionEntry": fsMIFsbFIPSessionEntry,
       "fsMIFsbFIPSessionVlanId": fsMIFsbFIPSessionVlanId,
       "fsMIFsbFIPSessionEnodeIfIndex": fsMIFsbFIPSessionEnodeIfIndex,
       "fsMIFsbFIPSessionEnodeMacAddress": fsMIFsbFIPSessionEnodeMacAddress,
       "fsMIFsbFIPSessionFcfMacAddress": fsMIFsbFIPSessionFcfMacAddress,
       "fsMIFsbFIPSessionFCoEMacAddress": fsMIFsbFIPSessionFCoEMacAddress,
       "fsMIFsbFIPSessionFcMap": fsMIFsbFIPSessionFcMap,
       "fsMIFsbFIPSessionFcfIfIndex": fsMIFsbFIPSessionFcfIfIndex,
       "fsMIFsbFIPSessionFcfNameId": fsMIFsbFIPSessionFcfNameId,
       "fsMIFsbFIPSessionFcId": fsMIFsbFIPSessionFcId,
       "fsMIFsbFIPSessionEnodeConnectType": fsMIFsbFIPSessionEnodeConnectType,
       "fsMIFsbFIPSessionHouseKeepingTimerStatus": fsMIFsbFIPSessionHouseKeepingTimerStatus,
       "fsMIFsbFcfTable": fsMIFsbFcfTable,
       "fsMIFsbFcfEntry": fsMIFsbFcfEntry,
       "fsMIFsbFcfVlanId": fsMIFsbFcfVlanId,
       "fsMIFsbFcfIfIndex": fsMIFsbFcfIfIndex,
       "fsMIFsbFcfMacAddress": fsMIFsbFcfMacAddress,
       "fsMIFsbFcfFcMap": fsMIFsbFcfFcMap,
       "fsMIFsbFcfAddressingMode": fsMIFsbFcfAddressingMode,
       "fsMIFsbFcfEnodeLoginCount": fsMIFsbFcfEnodeLoginCount,
       "fsMIFsbFcfNameId": fsMIFsbFcfNameId,
       "fsMIFsbFcfFabricName": fsMIFsbFcfFabricName,
       "fsMIFsbStatistics": fsMIFsbStatistics,
       "fsMIFsbGlobalStatsTable": fsMIFsbGlobalStatsTable,
       "fsMIFsbGlobalStatsEntry": fsMIFsbGlobalStatsEntry,
       "fsMIFsbGlobalStatsVlanRequests": fsMIFsbGlobalStatsVlanRequests,
       "fsMIFsbGlobalStatsVlanNotification": fsMIFsbGlobalStatsVlanNotification,
       "fsMIFsbVlanStatsTable": fsMIFsbVlanStatsTable,
       "fsMIFsbVlanStatsEntry": fsMIFsbVlanStatsEntry,
       "fsMIFsbVlanStatsUnicastDisAdv": fsMIFsbVlanStatsUnicastDisAdv,
       "fsMIFsbVlanStatsMulticastDisAdv": fsMIFsbVlanStatsMulticastDisAdv,
       "fsMIFsbVlanStatsUnicastDisSol": fsMIFsbVlanStatsUnicastDisSol,
       "fsMIFsbVlanStatsMulticastDisSol": fsMIFsbVlanStatsMulticastDisSol,
       "fsMIFsbVlanStatsFLOGICount": fsMIFsbVlanStatsFLOGICount,
       "fsMIFsbVlanStatsFDISCCount": fsMIFsbVlanStatsFDISCCount,
       "fsMIFsbVlanStatsLOGOCount": fsMIFsbVlanStatsLOGOCount,
       "fsMIFsbVlanStatsFLOGIAcceptCount": fsMIFsbVlanStatsFLOGIAcceptCount,
       "fsMIFsbVlanStatsFLOGIRejectCount": fsMIFsbVlanStatsFLOGIRejectCount,
       "fsMIFsbVlanStatsFDISCAcceptCount": fsMIFsbVlanStatsFDISCAcceptCount,
       "fsMIFsbVlanStatsFDISCRejectCount": fsMIFsbVlanStatsFDISCRejectCount,
       "fsMIFsbVlanStatsLOGOAcceptCount": fsMIFsbVlanStatsLOGOAcceptCount,
       "fsMIFsbVlanStatsLOGORejectCount": fsMIFsbVlanStatsLOGORejectCount,
       "fsMIFsbVlanStatsClearLinkCount": fsMIFsbVlanStatsClearLinkCount,
       "fsMIFsbVlanFcMapMisMatchCount": fsMIFsbVlanFcMapMisMatchCount,
       "fsMIFsbVlanMTUMisMatchCount": fsMIFsbVlanMTUMisMatchCount,
       "fsMIFsbVlanACLFailureCount": fsMIFsbVlanACLFailureCount,
       "fsMIFsbVlanInvalidFIPFramesCount": fsMIFsbVlanInvalidFIPFramesCount,
       "fsMIFsbVlanFCFDiscoveryTimeoutsCount": fsMIFsbVlanFCFDiscoveryTimeoutsCount,
       "fsMIFsbSessStatsTable": fsMIFsbSessStatsTable,
       "fsMIFsbSessStatsEntry": fsMIFsbSessStatsEntry,
       "fsMIFsbSessStatsVlanId": fsMIFsbSessStatsVlanId,
       "fsMIFsbSessStatsEnodeIfIndex": fsMIFsbSessStatsEnodeIfIndex,
       "fsMIFsbSessStatsEnodeMacAddress": fsMIFsbSessStatsEnodeMacAddress,
       "fsMIFsbSessStatsFcfMacAddress": fsMIFsbSessStatsFcfMacAddress,
       "fsMIFsbSessStatsFCoEMacAddress": fsMIFsbSessStatsFCoEMacAddress,
       "fsMIFsbSessStatsEnodeKeepAliveCount": fsMIFsbSessStatsEnodeKeepAliveCount,
       "fsMIFsbSessStatsVNPortKeepAliveCount": fsMIFsbSessStatsVNPortKeepAliveCount,
       "fsMIFsbNotificationObjects": fsMIFsbNotificationObjects,
       "fsMIFsbTrapObjects": fsMIFsbTrapObjects,
       "fsMIFsbSessionVlanId": fsMIFsbSessionVlanId,
       "fsMIFsbSessionEnodeIfIndex": fsMIFsbSessionEnodeIfIndex,
       "fsMIFsbSessionEnodeMacAddress": fsMIFsbSessionEnodeMacAddress,
       "fsMIFsbNotifications": fsMIFsbNotifications,
       "fsMIFsbTraps": fsMIFsbTraps,
       "fsMIFsbFIPSessionClear": fsMIFsbFIPSessionClear,
       "fsMIFsbFcmapMismatch": fsMIFsbFcmapMismatch,
       "fsMIFsbMTUMismatch": fsMIFsbMTUMismatch,
       "fsMIFsbAclFailure": fsMIFsbAclFailure}
)
