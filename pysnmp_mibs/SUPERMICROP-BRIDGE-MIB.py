# SNMP MIB module (SUPERMICROP-BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICROP-BRIDGE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:04:57 2025
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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")

(fsDot1dBasePort,
 fsDot1dBasePortEntry,
 fsDot1dBridge,
 fsDot1dTp,
 fsDot1dTpPort) = mibBuilder.importSymbols(
    "SUPERMICRO-MIStdBRIDGE-MIB",
    "fsDot1dBasePort",
    "fsDot1dBasePortEntry",
    "fsDot1dBridge",
    "fsDot1dTp",
    "fsDot1dTpPort")


# MODULE-IDENTITY

fsPBridgeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6)
)
if mibBuilder.loadTexts:
    fsPBridgeMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EnabledStatus(TextualConvention, Integer32):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_FsDot1dTpHCPortTable_Object = MibTable
fsDot1dTpHCPortTable = _FsDot1dTpHCPortTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 4, 5)
)
if mibBuilder.loadTexts:
    fsDot1dTpHCPortTable.setStatus("current")
_FsDot1dTpHCPortEntry_Object = MibTableRow
fsDot1dTpHCPortEntry = _FsDot1dTpHCPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 4, 5, 1)
)
fsDot1dTpHCPortEntry.setIndexNames(
    (0, "SUPERMICRO-MIStdBRIDGE-MIB", "fsDot1dTpPort"),
)
if mibBuilder.loadTexts:
    fsDot1dTpHCPortEntry.setStatus("current")
_FsDot1dTpHCPortInFrames_Type = Counter64
_FsDot1dTpHCPortInFrames_Object = MibTableColumn
fsDot1dTpHCPortInFrames = _FsDot1dTpHCPortInFrames_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 4, 5, 1, 1),
    _FsDot1dTpHCPortInFrames_Type()
)
fsDot1dTpHCPortInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1dTpHCPortInFrames.setStatus("current")
_FsDot1dTpHCPortOutFrames_Type = Counter64
_FsDot1dTpHCPortOutFrames_Object = MibTableColumn
fsDot1dTpHCPortOutFrames = _FsDot1dTpHCPortOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 4, 5, 1, 2),
    _FsDot1dTpHCPortOutFrames_Type()
)
fsDot1dTpHCPortOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1dTpHCPortOutFrames.setStatus("current")
_FsDot1dTpHCPortInDiscards_Type = Counter64
_FsDot1dTpHCPortInDiscards_Object = MibTableColumn
fsDot1dTpHCPortInDiscards = _FsDot1dTpHCPortInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 4, 5, 1, 3),
    _FsDot1dTpHCPortInDiscards_Type()
)
fsDot1dTpHCPortInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1dTpHCPortInDiscards.setStatus("current")
_FsDot1dTpPortOverflowTable_Object = MibTable
fsDot1dTpPortOverflowTable = _FsDot1dTpPortOverflowTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 4, 6)
)
if mibBuilder.loadTexts:
    fsDot1dTpPortOverflowTable.setStatus("current")
_FsDot1dTpPortOverflowEntry_Object = MibTableRow
fsDot1dTpPortOverflowEntry = _FsDot1dTpPortOverflowEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 4, 6, 1)
)
fsDot1dTpPortOverflowEntry.setIndexNames(
    (0, "SUPERMICRO-MIStdBRIDGE-MIB", "fsDot1dTpPort"),
)
if mibBuilder.loadTexts:
    fsDot1dTpPortOverflowEntry.setStatus("current")
_FsDot1dTpPortInOverflowFrames_Type = Counter32
_FsDot1dTpPortInOverflowFrames_Object = MibTableColumn
fsDot1dTpPortInOverflowFrames = _FsDot1dTpPortInOverflowFrames_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 4, 6, 1, 1),
    _FsDot1dTpPortInOverflowFrames_Type()
)
fsDot1dTpPortInOverflowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1dTpPortInOverflowFrames.setStatus("current")
_FsDot1dTpPortOutOverflowFrames_Type = Counter32
_FsDot1dTpPortOutOverflowFrames_Object = MibTableColumn
fsDot1dTpPortOutOverflowFrames = _FsDot1dTpPortOutOverflowFrames_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 4, 6, 1, 2),
    _FsDot1dTpPortOutOverflowFrames_Type()
)
fsDot1dTpPortOutOverflowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1dTpPortOutOverflowFrames.setStatus("current")
_FsDot1dTpPortInOverflowDiscards_Type = Counter32
_FsDot1dTpPortInOverflowDiscards_Object = MibTableColumn
fsDot1dTpPortInOverflowDiscards = _FsDot1dTpPortInOverflowDiscards_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 4, 6, 1, 3),
    _FsDot1dTpPortInOverflowDiscards_Type()
)
fsDot1dTpPortInOverflowDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1dTpPortInOverflowDiscards.setStatus("current")
_FsPBridgeMIBObjects_ObjectIdentity = ObjectIdentity
fsPBridgeMIBObjects = _FsPBridgeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 1)
)
_FsDot1dExtBase_ObjectIdentity = ObjectIdentity
fsDot1dExtBase = _FsDot1dExtBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 1, 1)
)
_FsDot1dExtBaseTable_Object = MibTable
fsDot1dExtBaseTable = _FsDot1dExtBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fsDot1dExtBaseTable.setStatus("current")
_FsDot1dExtBaseEntry_Object = MibTableRow
fsDot1dExtBaseEntry = _FsDot1dExtBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 1, 1, 1, 1)
)
fsDot1dExtBaseEntry.setIndexNames(
    (0, "SUPERMICROP-BRIDGE-MIB", "fsDot1dBridgeContextId"),
)
if mibBuilder.loadTexts:
    fsDot1dExtBaseEntry.setStatus("current")


class _FsDot1dBridgeContextId_Type(Integer32):
    """Custom type fsDot1dBridgeContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsDot1dBridgeContextId_Type.__name__ = "Integer32"
_FsDot1dBridgeContextId_Object = MibTableColumn
fsDot1dBridgeContextId = _FsDot1dBridgeContextId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 1, 1, 1, 1, 1),
    _FsDot1dBridgeContextId_Type()
)
fsDot1dBridgeContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDot1dBridgeContextId.setStatus("current")


class _FsDot1dDeviceCapabilities_Type(Bits):
    """Custom type fsDot1dDeviceCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("dot1dExtendedFilteringServices", 0),
          ("dot1dTrafficClasses", 1),
          ("dot1qStaticEntryIndividualPort", 2),
          ("dot1qIVLCapable", 3),
          ("dot1qSVLCapable", 4),
          ("dot1qHybridCapable", 5),
          ("dot1qConfigurablePvidTagging", 6),
          ("dot1dLocalVlanCapable", 7))
    )

_FsDot1dDeviceCapabilities_Type.__name__ = "Bits"
_FsDot1dDeviceCapabilities_Object = MibTableColumn
fsDot1dDeviceCapabilities = _FsDot1dDeviceCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 1, 1, 1, 1, 2),
    _FsDot1dDeviceCapabilities_Type()
)
fsDot1dDeviceCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1dDeviceCapabilities.setStatus("current")


class _FsDot1dTrafficClassesEnabled_Type(TruthValue):
    """Custom type fsDot1dTrafficClassesEnabled based on TruthValue"""
    defaultValue = 1


_FsDot1dTrafficClassesEnabled_Type.__name__ = "TruthValue"
_FsDot1dTrafficClassesEnabled_Object = MibTableColumn
fsDot1dTrafficClassesEnabled = _FsDot1dTrafficClassesEnabled_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 1, 1, 1, 1, 3),
    _FsDot1dTrafficClassesEnabled_Type()
)
fsDot1dTrafficClassesEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1dTrafficClassesEnabled.setStatus("current")
_FsDot1dGmrpStatus_Type = EnabledStatus
_FsDot1dGmrpStatus_Object = MibTableColumn
fsDot1dGmrpStatus = _FsDot1dGmrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 1, 1, 1, 1, 4),
    _FsDot1dGmrpStatus_Type()
)
fsDot1dGmrpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1dGmrpStatus.setStatus("current")
_FsDot1dPortCapabilitiesTable_Object = MibTable
fsDot1dPortCapabilitiesTable = _FsDot1dPortCapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 1, 1, 2)
)
if mibBuilder.loadTexts:
    fsDot1dPortCapabilitiesTable.setStatus("current")
_FsDot1dPortCapabilitiesEntry_Object = MibTableRow
fsDot1dPortCapabilitiesEntry = _FsDot1dPortCapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fsDot1dPortCapabilitiesEntry.setStatus("current")


class _FsDot1dPortCapabilities_Type(Bits):
    """Custom type fsDot1dPortCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("dot1qDot1qTagging", 0),
          ("dot1qConfigurableAcceptableFrameTypes", 1),
          ("dot1qIngressFiltering", 2))
    )

_FsDot1dPortCapabilities_Type.__name__ = "Bits"
_FsDot1dPortCapabilities_Object = MibTableColumn
fsDot1dPortCapabilities = _FsDot1dPortCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 1, 1, 2, 1, 1),
    _FsDot1dPortCapabilities_Type()
)
fsDot1dPortCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1dPortCapabilities.setStatus("current")
_FsDot1dPriority_ObjectIdentity = ObjectIdentity
fsDot1dPriority = _FsDot1dPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 1, 2)
)
_FsDot1dPortPriorityTable_Object = MibTable
fsDot1dPortPriorityTable = _FsDot1dPortPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fsDot1dPortPriorityTable.setStatus("current")
_FsDot1dPortPriorityEntry_Object = MibTableRow
fsDot1dPortPriorityEntry = _FsDot1dPortPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fsDot1dPortPriorityEntry.setStatus("current")


class _FsDot1dPortDefaultUserPriority_Type(Integer32):
    """Custom type fsDot1dPortDefaultUserPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsDot1dPortDefaultUserPriority_Type.__name__ = "Integer32"
_FsDot1dPortDefaultUserPriority_Object = MibTableColumn
fsDot1dPortDefaultUserPriority = _FsDot1dPortDefaultUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 1, 2, 1, 1, 1),
    _FsDot1dPortDefaultUserPriority_Type()
)
fsDot1dPortDefaultUserPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1dPortDefaultUserPriority.setStatus("current")


class _FsDot1dPortNumTrafficClasses_Type(Integer32):
    """Custom type fsDot1dPortNumTrafficClasses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_FsDot1dPortNumTrafficClasses_Type.__name__ = "Integer32"
_FsDot1dPortNumTrafficClasses_Object = MibTableColumn
fsDot1dPortNumTrafficClasses = _FsDot1dPortNumTrafficClasses_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 1, 2, 1, 1, 2),
    _FsDot1dPortNumTrafficClasses_Type()
)
fsDot1dPortNumTrafficClasses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1dPortNumTrafficClasses.setStatus("current")
_FsDot1dUserPriorityRegenTable_Object = MibTable
fsDot1dUserPriorityRegenTable = _FsDot1dUserPriorityRegenTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 1, 2, 2)
)
if mibBuilder.loadTexts:
    fsDot1dUserPriorityRegenTable.setStatus("current")
_FsDot1dUserPriorityRegenEntry_Object = MibTableRow
fsDot1dUserPriorityRegenEntry = _FsDot1dUserPriorityRegenEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 1, 2, 2, 1)
)
fsDot1dUserPriorityRegenEntry.setIndexNames(
    (0, "SUPERMICRO-MIStdBRIDGE-MIB", "fsDot1dBasePort"),
    (0, "SUPERMICROP-BRIDGE-MIB", "fsDot1dUserPriority"),
)
if mibBuilder.loadTexts:
    fsDot1dUserPriorityRegenEntry.setStatus("current")


class _FsDot1dUserPriority_Type(Integer32):
    """Custom type fsDot1dUserPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsDot1dUserPriority_Type.__name__ = "Integer32"
_FsDot1dUserPriority_Object = MibTableColumn
fsDot1dUserPriority = _FsDot1dUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 1, 2, 2, 1, 1),
    _FsDot1dUserPriority_Type()
)
fsDot1dUserPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDot1dUserPriority.setStatus("current")


class _FsDot1dRegenUserPriority_Type(Integer32):
    """Custom type fsDot1dRegenUserPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsDot1dRegenUserPriority_Type.__name__ = "Integer32"
_FsDot1dRegenUserPriority_Object = MibTableColumn
fsDot1dRegenUserPriority = _FsDot1dRegenUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 1, 2, 2, 1, 2),
    _FsDot1dRegenUserPriority_Type()
)
fsDot1dRegenUserPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1dRegenUserPriority.setStatus("current")
_FsDot1dTrafficClassTable_Object = MibTable
fsDot1dTrafficClassTable = _FsDot1dTrafficClassTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 1, 2, 3)
)
if mibBuilder.loadTexts:
    fsDot1dTrafficClassTable.setStatus("current")
_FsDot1dTrafficClassEntry_Object = MibTableRow
fsDot1dTrafficClassEntry = _FsDot1dTrafficClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 1, 2, 3, 1)
)
fsDot1dTrafficClassEntry.setIndexNames(
    (0, "SUPERMICRO-MIStdBRIDGE-MIB", "fsDot1dBasePort"),
    (0, "SUPERMICROP-BRIDGE-MIB", "fsDot1dTrafficClassPriority"),
)
if mibBuilder.loadTexts:
    fsDot1dTrafficClassEntry.setStatus("current")


class _FsDot1dTrafficClassPriority_Type(Integer32):
    """Custom type fsDot1dTrafficClassPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsDot1dTrafficClassPriority_Type.__name__ = "Integer32"
_FsDot1dTrafficClassPriority_Object = MibTableColumn
fsDot1dTrafficClassPriority = _FsDot1dTrafficClassPriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 1, 2, 3, 1, 1),
    _FsDot1dTrafficClassPriority_Type()
)
fsDot1dTrafficClassPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDot1dTrafficClassPriority.setStatus("current")


class _FsDot1dTrafficClass_Type(Integer32):
    """Custom type fsDot1dTrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsDot1dTrafficClass_Type.__name__ = "Integer32"
_FsDot1dTrafficClass_Object = MibTableColumn
fsDot1dTrafficClass = _FsDot1dTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 1, 2, 3, 1, 2),
    _FsDot1dTrafficClass_Type()
)
fsDot1dTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1dTrafficClass.setStatus("current")
_FsDot1dPortOutboundAccessPriorityTable_Object = MibTable
fsDot1dPortOutboundAccessPriorityTable = _FsDot1dPortOutboundAccessPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 1, 2, 4)
)
if mibBuilder.loadTexts:
    fsDot1dPortOutboundAccessPriorityTable.setStatus("current")
_FsDot1dPortOutboundAccessPriorityEntry_Object = MibTableRow
fsDot1dPortOutboundAccessPriorityEntry = _FsDot1dPortOutboundAccessPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 1, 2, 4, 1)
)
fsDot1dPortOutboundAccessPriorityEntry.setIndexNames(
    (0, "SUPERMICRO-MIStdBRIDGE-MIB", "fsDot1dBasePort"),
    (0, "SUPERMICROP-BRIDGE-MIB", "fsDot1dRegenUserPriority"),
)
if mibBuilder.loadTexts:
    fsDot1dPortOutboundAccessPriorityEntry.setStatus("current")


class _FsDot1dPortOutboundAccessPriority_Type(Integer32):
    """Custom type fsDot1dPortOutboundAccessPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsDot1dPortOutboundAccessPriority_Type.__name__ = "Integer32"
_FsDot1dPortOutboundAccessPriority_Object = MibTableColumn
fsDot1dPortOutboundAccessPriority = _FsDot1dPortOutboundAccessPriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 1, 2, 4, 1, 1),
    _FsDot1dPortOutboundAccessPriority_Type()
)
fsDot1dPortOutboundAccessPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1dPortOutboundAccessPriority.setStatus("current")
_FsDot1dGarp_ObjectIdentity = ObjectIdentity
fsDot1dGarp = _FsDot1dGarp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 1, 3)
)
_FsDot1dPortGarpTable_Object = MibTable
fsDot1dPortGarpTable = _FsDot1dPortGarpTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 1, 3, 1)
)
if mibBuilder.loadTexts:
    fsDot1dPortGarpTable.setStatus("current")
_FsDot1dPortGarpEntry_Object = MibTableRow
fsDot1dPortGarpEntry = _FsDot1dPortGarpEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    fsDot1dPortGarpEntry.setStatus("current")


class _FsDot1dPortGarpJoinTime_Type(TimeInterval):
    """Custom type fsDot1dPortGarpJoinTime based on TimeInterval"""
    defaultValue = 20


_FsDot1dPortGarpJoinTime_Type.__name__ = "TimeInterval"
_FsDot1dPortGarpJoinTime_Object = MibTableColumn
fsDot1dPortGarpJoinTime = _FsDot1dPortGarpJoinTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 1, 3, 1, 1, 1),
    _FsDot1dPortGarpJoinTime_Type()
)
fsDot1dPortGarpJoinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1dPortGarpJoinTime.setStatus("current")


class _FsDot1dPortGarpLeaveTime_Type(TimeInterval):
    """Custom type fsDot1dPortGarpLeaveTime based on TimeInterval"""
    defaultValue = 60


_FsDot1dPortGarpLeaveTime_Type.__name__ = "TimeInterval"
_FsDot1dPortGarpLeaveTime_Object = MibTableColumn
fsDot1dPortGarpLeaveTime = _FsDot1dPortGarpLeaveTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 1, 3, 1, 1, 2),
    _FsDot1dPortGarpLeaveTime_Type()
)
fsDot1dPortGarpLeaveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1dPortGarpLeaveTime.setStatus("current")


class _FsDot1dPortGarpLeaveAllTime_Type(TimeInterval):
    """Custom type fsDot1dPortGarpLeaveAllTime based on TimeInterval"""
    defaultValue = 1000


_FsDot1dPortGarpLeaveAllTime_Type.__name__ = "TimeInterval"
_FsDot1dPortGarpLeaveAllTime_Object = MibTableColumn
fsDot1dPortGarpLeaveAllTime = _FsDot1dPortGarpLeaveAllTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 1, 3, 1, 1, 3),
    _FsDot1dPortGarpLeaveAllTime_Type()
)
fsDot1dPortGarpLeaveAllTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1dPortGarpLeaveAllTime.setStatus("current")
_FsDot1dGmrp_ObjectIdentity = ObjectIdentity
fsDot1dGmrp = _FsDot1dGmrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 1, 4)
)
_FsDot1dPortGmrpTable_Object = MibTable
fsDot1dPortGmrpTable = _FsDot1dPortGmrpTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 1, 4, 1)
)
if mibBuilder.loadTexts:
    fsDot1dPortGmrpTable.setStatus("current")
_FsDot1dPortGmrpEntry_Object = MibTableRow
fsDot1dPortGmrpEntry = _FsDot1dPortGmrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    fsDot1dPortGmrpEntry.setStatus("current")


class _FsDot1dPortGmrpStatus_Type(EnabledStatus):
    """Custom type fsDot1dPortGmrpStatus based on EnabledStatus"""
    defaultValue = 1


_FsDot1dPortGmrpStatus_Type.__name__ = "EnabledStatus"
_FsDot1dPortGmrpStatus_Object = MibTableColumn
fsDot1dPortGmrpStatus = _FsDot1dPortGmrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 1, 4, 1, 1, 1),
    _FsDot1dPortGmrpStatus_Type()
)
fsDot1dPortGmrpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1dPortGmrpStatus.setStatus("current")
_FsDot1dPortGmrpFailedRegistrations_Type = Counter32
_FsDot1dPortGmrpFailedRegistrations_Object = MibTableColumn
fsDot1dPortGmrpFailedRegistrations = _FsDot1dPortGmrpFailedRegistrations_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 1, 4, 1, 1, 2),
    _FsDot1dPortGmrpFailedRegistrations_Type()
)
fsDot1dPortGmrpFailedRegistrations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1dPortGmrpFailedRegistrations.setStatus("current")
_FsDot1dPortGmrpLastPduOrigin_Type = MacAddress
_FsDot1dPortGmrpLastPduOrigin_Object = MibTableColumn
fsDot1dPortGmrpLastPduOrigin = _FsDot1dPortGmrpLastPduOrigin_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 1, 4, 1, 1, 3),
    _FsDot1dPortGmrpLastPduOrigin_Type()
)
fsDot1dPortGmrpLastPduOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1dPortGmrpLastPduOrigin.setStatus("current")


class _FsDot1dPortRestrictedGroupRegistration_Type(TruthValue):
    """Custom type fsDot1dPortRestrictedGroupRegistration based on TruthValue"""
    defaultValue = 2


_FsDot1dPortRestrictedGroupRegistration_Type.__name__ = "TruthValue"
_FsDot1dPortRestrictedGroupRegistration_Object = MibTableColumn
fsDot1dPortRestrictedGroupRegistration = _FsDot1dPortRestrictedGroupRegistration_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 1, 4, 1, 1, 4),
    _FsDot1dPortRestrictedGroupRegistration_Type()
)
fsDot1dPortRestrictedGroupRegistration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1dPortRestrictedGroupRegistration.setStatus("current")
_FsPBridgeConformance_ObjectIdentity = ObjectIdentity
fsPBridgeConformance = _FsPBridgeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 2)
)
_FsPBridgeGroups_ObjectIdentity = ObjectIdentity
fsPBridgeGroups = _FsPBridgeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 2, 1)
)
_FsPBridgeCompliances_ObjectIdentity = ObjectIdentity
fsPBridgeCompliances = _FsPBridgeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 2, 2)
)
fsDot1dBasePortEntry.registerAugmentions(
    ("SUPERMICROP-BRIDGE-MIB",
     "fsDot1dPortCapabilitiesEntry")
)
fsDot1dPortCapabilitiesEntry.setIndexNames(*fsDot1dBasePortEntry.getIndexNames())
fsDot1dBasePortEntry.registerAugmentions(
    ("SUPERMICROP-BRIDGE-MIB",
     "fsDot1dPortPriorityEntry")
)
fsDot1dPortPriorityEntry.setIndexNames(*fsDot1dBasePortEntry.getIndexNames())
fsDot1dBasePortEntry.registerAugmentions(
    ("SUPERMICROP-BRIDGE-MIB",
     "fsDot1dPortGarpEntry")
)
fsDot1dPortGarpEntry.setIndexNames(*fsDot1dBasePortEntry.getIndexNames())
fsDot1dBasePortEntry.registerAugmentions(
    ("SUPERMICROP-BRIDGE-MIB",
     "fsDot1dPortGmrpEntry")
)
fsDot1dPortGmrpEntry.setIndexNames(*fsDot1dBasePortEntry.getIndexNames())

# Managed Objects groups

fsPBridgeExtCapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 2, 1, 1)
)
fsPBridgeExtCapGroup.setObjects(
      *(("SUPERMICROP-BRIDGE-MIB", "fsDot1dDeviceCapabilities"),
        ("SUPERMICROP-BRIDGE-MIB", "fsDot1dPortCapabilities"))
)
if mibBuilder.loadTexts:
    fsPBridgeExtCapGroup.setStatus("current")

fsPBridgeDeviceGmrpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 2, 1, 2)
)
fsPBridgeDeviceGmrpGroup.setObjects(
    ("SUPERMICROP-BRIDGE-MIB", "fsDot1dGmrpStatus")
)
if mibBuilder.loadTexts:
    fsPBridgeDeviceGmrpGroup.setStatus("current")

fsPBridgeDevicePriorityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 2, 1, 3)
)
fsPBridgeDevicePriorityGroup.setObjects(
    ("SUPERMICROP-BRIDGE-MIB", "fsDot1dTrafficClassesEnabled")
)
if mibBuilder.loadTexts:
    fsPBridgeDevicePriorityGroup.setStatus("current")

fsPBridgeDefaultPriorityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 2, 1, 4)
)
fsPBridgeDefaultPriorityGroup.setObjects(
    ("SUPERMICROP-BRIDGE-MIB", "fsDot1dPortDefaultUserPriority")
)
if mibBuilder.loadTexts:
    fsPBridgeDefaultPriorityGroup.setStatus("current")

fsPBridgeRegenPriorityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 2, 1, 5)
)
fsPBridgeRegenPriorityGroup.setObjects(
    ("SUPERMICROP-BRIDGE-MIB", "fsDot1dRegenUserPriority")
)
if mibBuilder.loadTexts:
    fsPBridgeRegenPriorityGroup.setStatus("current")

fsPBridgePriorityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 2, 1, 6)
)
fsPBridgePriorityGroup.setObjects(
      *(("SUPERMICROP-BRIDGE-MIB", "fsDot1dPortNumTrafficClasses"),
        ("SUPERMICROP-BRIDGE-MIB", "fsDot1dTrafficClass"))
)
if mibBuilder.loadTexts:
    fsPBridgePriorityGroup.setStatus("current")

fsPBridgeAccessPriorityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 2, 1, 7)
)
fsPBridgeAccessPriorityGroup.setObjects(
    ("SUPERMICROP-BRIDGE-MIB", "fsDot1dPortOutboundAccessPriority")
)
if mibBuilder.loadTexts:
    fsPBridgeAccessPriorityGroup.setStatus("current")

fsPBridgePortGarpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 2, 1, 8)
)
fsPBridgePortGarpGroup.setObjects(
      *(("SUPERMICROP-BRIDGE-MIB", "fsDot1dPortGarpJoinTime"),
        ("SUPERMICROP-BRIDGE-MIB", "fsDot1dPortGarpLeaveTime"),
        ("SUPERMICROP-BRIDGE-MIB", "fsDot1dPortGarpLeaveAllTime"))
)
if mibBuilder.loadTexts:
    fsPBridgePortGarpGroup.setStatus("current")

fsPBridgePortGmrpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 2, 1, 9)
)
fsPBridgePortGmrpGroup.setObjects(
      *(("SUPERMICROP-BRIDGE-MIB", "fsDot1dPortGmrpStatus"),
        ("SUPERMICROP-BRIDGE-MIB", "fsDot1dPortGmrpFailedRegistrations"),
        ("SUPERMICROP-BRIDGE-MIB", "fsDot1dPortGmrpLastPduOrigin"),
        ("SUPERMICROP-BRIDGE-MIB", "fsDot1dPortRestrictedGroupRegistration"))
)
if mibBuilder.loadTexts:
    fsPBridgePortGmrpGroup.setStatus("current")

fsPBridgeHCPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 2, 1, 10)
)
fsPBridgeHCPortGroup.setObjects(
      *(("SUPERMICROP-BRIDGE-MIB", "fsDot1dTpHCPortInFrames"),
        ("SUPERMICROP-BRIDGE-MIB", "fsDot1dTpHCPortOutFrames"),
        ("SUPERMICROP-BRIDGE-MIB", "fsDot1dTpHCPortInDiscards"))
)
if mibBuilder.loadTexts:
    fsPBridgeHCPortGroup.setStatus("current")

fsPBridgePortOverflowGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 2, 1, 11)
)
fsPBridgePortOverflowGroup.setObjects(
      *(("SUPERMICROP-BRIDGE-MIB", "fsDot1dTpPortInOverflowFrames"),
        ("SUPERMICROP-BRIDGE-MIB", "fsDot1dTpPortOutOverflowFrames"),
        ("SUPERMICROP-BRIDGE-MIB", "fsDot1dTpPortInOverflowDiscards"))
)
if mibBuilder.loadTexts:
    fsPBridgePortOverflowGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsPBridgeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 6, 2, 2, 1)
)
fsPBridgeCompliance.setObjects(
      *(("SUPERMICROP-BRIDGE-MIB", "fsPBridgeExtCapGroup"),
        ("SUPERMICROP-BRIDGE-MIB", "fsPBridgeDeviceGmrpGroup"),
        ("SUPERMICROP-BRIDGE-MIB", "fsPBridgeDevicePriorityGroup"),
        ("SUPERMICROP-BRIDGE-MIB", "fsPBridgeDefaultPriorityGroup"),
        ("SUPERMICROP-BRIDGE-MIB", "fsPBridgeRegenPriorityGroup"),
        ("SUPERMICROP-BRIDGE-MIB", "fsPBridgePriorityGroup"),
        ("SUPERMICROP-BRIDGE-MIB", "fsPBridgeAccessPriorityGroup"),
        ("SUPERMICROP-BRIDGE-MIB", "fsPBridgePortGarpGroup"),
        ("SUPERMICROP-BRIDGE-MIB", "fsPBridgePortGmrpGroup"),
        ("SUPERMICROP-BRIDGE-MIB", "fsPBridgeHCPortGroup"),
        ("SUPERMICROP-BRIDGE-MIB", "fsPBridgePortOverflowGroup"))
)
if mibBuilder.loadTexts:
    fsPBridgeCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICROP-BRIDGE-MIB",
    **{"EnabledStatus": EnabledStatus,
       "fsDot1dTpHCPortTable": fsDot1dTpHCPortTable,
       "fsDot1dTpHCPortEntry": fsDot1dTpHCPortEntry,
       "fsDot1dTpHCPortInFrames": fsDot1dTpHCPortInFrames,
       "fsDot1dTpHCPortOutFrames": fsDot1dTpHCPortOutFrames,
       "fsDot1dTpHCPortInDiscards": fsDot1dTpHCPortInDiscards,
       "fsDot1dTpPortOverflowTable": fsDot1dTpPortOverflowTable,
       "fsDot1dTpPortOverflowEntry": fsDot1dTpPortOverflowEntry,
       "fsDot1dTpPortInOverflowFrames": fsDot1dTpPortInOverflowFrames,
       "fsDot1dTpPortOutOverflowFrames": fsDot1dTpPortOutOverflowFrames,
       "fsDot1dTpPortInOverflowDiscards": fsDot1dTpPortInOverflowDiscards,
       "fsPBridgeMIB": fsPBridgeMIB,
       "fsPBridgeMIBObjects": fsPBridgeMIBObjects,
       "fsDot1dExtBase": fsDot1dExtBase,
       "fsDot1dExtBaseTable": fsDot1dExtBaseTable,
       "fsDot1dExtBaseEntry": fsDot1dExtBaseEntry,
       "fsDot1dBridgeContextId": fsDot1dBridgeContextId,
       "fsDot1dDeviceCapabilities": fsDot1dDeviceCapabilities,
       "fsDot1dTrafficClassesEnabled": fsDot1dTrafficClassesEnabled,
       "fsDot1dGmrpStatus": fsDot1dGmrpStatus,
       "fsDot1dPortCapabilitiesTable": fsDot1dPortCapabilitiesTable,
       "fsDot1dPortCapabilitiesEntry": fsDot1dPortCapabilitiesEntry,
       "fsDot1dPortCapabilities": fsDot1dPortCapabilities,
       "fsDot1dPriority": fsDot1dPriority,
       "fsDot1dPortPriorityTable": fsDot1dPortPriorityTable,
       "fsDot1dPortPriorityEntry": fsDot1dPortPriorityEntry,
       "fsDot1dPortDefaultUserPriority": fsDot1dPortDefaultUserPriority,
       "fsDot1dPortNumTrafficClasses": fsDot1dPortNumTrafficClasses,
       "fsDot1dUserPriorityRegenTable": fsDot1dUserPriorityRegenTable,
       "fsDot1dUserPriorityRegenEntry": fsDot1dUserPriorityRegenEntry,
       "fsDot1dUserPriority": fsDot1dUserPriority,
       "fsDot1dRegenUserPriority": fsDot1dRegenUserPriority,
       "fsDot1dTrafficClassTable": fsDot1dTrafficClassTable,
       "fsDot1dTrafficClassEntry": fsDot1dTrafficClassEntry,
       "fsDot1dTrafficClassPriority": fsDot1dTrafficClassPriority,
       "fsDot1dTrafficClass": fsDot1dTrafficClass,
       "fsDot1dPortOutboundAccessPriorityTable": fsDot1dPortOutboundAccessPriorityTable,
       "fsDot1dPortOutboundAccessPriorityEntry": fsDot1dPortOutboundAccessPriorityEntry,
       "fsDot1dPortOutboundAccessPriority": fsDot1dPortOutboundAccessPriority,
       "fsDot1dGarp": fsDot1dGarp,
       "fsDot1dPortGarpTable": fsDot1dPortGarpTable,
       "fsDot1dPortGarpEntry": fsDot1dPortGarpEntry,
       "fsDot1dPortGarpJoinTime": fsDot1dPortGarpJoinTime,
       "fsDot1dPortGarpLeaveTime": fsDot1dPortGarpLeaveTime,
       "fsDot1dPortGarpLeaveAllTime": fsDot1dPortGarpLeaveAllTime,
       "fsDot1dGmrp": fsDot1dGmrp,
       "fsDot1dPortGmrpTable": fsDot1dPortGmrpTable,
       "fsDot1dPortGmrpEntry": fsDot1dPortGmrpEntry,
       "fsDot1dPortGmrpStatus": fsDot1dPortGmrpStatus,
       "fsDot1dPortGmrpFailedRegistrations": fsDot1dPortGmrpFailedRegistrations,
       "fsDot1dPortGmrpLastPduOrigin": fsDot1dPortGmrpLastPduOrigin,
       "fsDot1dPortRestrictedGroupRegistration": fsDot1dPortRestrictedGroupRegistration,
       "fsPBridgeConformance": fsPBridgeConformance,
       "fsPBridgeGroups": fsPBridgeGroups,
       "fsPBridgeExtCapGroup": fsPBridgeExtCapGroup,
       "fsPBridgeDeviceGmrpGroup": fsPBridgeDeviceGmrpGroup,
       "fsPBridgeDevicePriorityGroup": fsPBridgeDevicePriorityGroup,
       "fsPBridgeDefaultPriorityGroup": fsPBridgeDefaultPriorityGroup,
       "fsPBridgeRegenPriorityGroup": fsPBridgeRegenPriorityGroup,
       "fsPBridgePriorityGroup": fsPBridgePriorityGroup,
       "fsPBridgeAccessPriorityGroup": fsPBridgeAccessPriorityGroup,
       "fsPBridgePortGarpGroup": fsPBridgePortGarpGroup,
       "fsPBridgePortGmrpGroup": fsPBridgePortGmrpGroup,
       "fsPBridgeHCPortGroup": fsPBridgeHCPortGroup,
       "fsPBridgePortOverflowGroup": fsPBridgePortOverflowGroup,
       "fsPBridgeCompliances": fsPBridgeCompliances,
       "fsPBridgeCompliance": fsPBridgeCompliance}
)
