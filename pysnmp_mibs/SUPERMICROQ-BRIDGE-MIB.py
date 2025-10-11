# SNMP MIB module (SUPERMICROQ-BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICROQ-BRIDGE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:04:56 2025
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

(TimeFilter,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "TimeFilter")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(fsDot1dBasePort,
 fsDot1dBridge) = mibBuilder.importSymbols(
    "SUPERMICRO-MIStdBRIDGE-MIB",
    "fsDot1dBasePort",
    "fsDot1dBridge")

(EnabledStatus,) = mibBuilder.importSymbols(
    "SUPERMICROP-BRIDGE-MIB",
    "EnabledStatus")


# MODULE-IDENTITY

fsQBridgeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7)
)
if mibBuilder.loadTexts:
    fsQBridgeMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanIndex(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"


class VlanId(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



# MIB Managed Objects in the order of their OIDs

_FsQBridgeMIBObjects_ObjectIdentity = ObjectIdentity
fsQBridgeMIBObjects = _FsQBridgeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1)
)
_FsDot1qBase_ObjectIdentity = ObjectIdentity
fsDot1qBase = _FsDot1qBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 1)
)
_FsDot1qBaseTable_Object = MibTable
fsDot1qBaseTable = _FsDot1qBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fsDot1qBaseTable.setStatus("current")
_FsDot1qBaseEntry_Object = MibTableRow
fsDot1qBaseEntry = _FsDot1qBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 1, 1, 1)
)
fsDot1qBaseEntry.setIndexNames(
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qVlanContextId"),
)
if mibBuilder.loadTexts:
    fsDot1qBaseEntry.setStatus("current")


class _FsDot1qVlanContextId_Type(Integer32):
    """Custom type fsDot1qVlanContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsDot1qVlanContextId_Type.__name__ = "Integer32"
_FsDot1qVlanContextId_Object = MibTableColumn
fsDot1qVlanContextId = _FsDot1qVlanContextId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 1, 1, 1, 1),
    _FsDot1qVlanContextId_Type()
)
fsDot1qVlanContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDot1qVlanContextId.setStatus("current")


class _FsDot1qVlanVersionNumber_Type(Integer32):
    """Custom type fsDot1qVlanVersionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("version1", 1)
    )


_FsDot1qVlanVersionNumber_Type.__name__ = "Integer32"
_FsDot1qVlanVersionNumber_Object = MibTableColumn
fsDot1qVlanVersionNumber = _FsDot1qVlanVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 1, 1, 1, 2),
    _FsDot1qVlanVersionNumber_Type()
)
fsDot1qVlanVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1qVlanVersionNumber.setStatus("current")
_FsDot1qMaxVlanId_Type = VlanId
_FsDot1qMaxVlanId_Object = MibTableColumn
fsDot1qMaxVlanId = _FsDot1qMaxVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 1, 1, 1, 3),
    _FsDot1qMaxVlanId_Type()
)
fsDot1qMaxVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1qMaxVlanId.setStatus("current")
_FsDot1qMaxSupportedVlans_Type = Unsigned32
_FsDot1qMaxSupportedVlans_Object = MibTableColumn
fsDot1qMaxSupportedVlans = _FsDot1qMaxSupportedVlans_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 1, 1, 1, 4),
    _FsDot1qMaxSupportedVlans_Type()
)
fsDot1qMaxSupportedVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1qMaxSupportedVlans.setStatus("current")
_FsDot1qNumVlans_Type = Unsigned32
_FsDot1qNumVlans_Object = MibTableColumn
fsDot1qNumVlans = _FsDot1qNumVlans_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 1, 1, 1, 5),
    _FsDot1qNumVlans_Type()
)
fsDot1qNumVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1qNumVlans.setStatus("current")
_FsDot1qGvrpStatus_Type = EnabledStatus
_FsDot1qGvrpStatus_Object = MibTableColumn
fsDot1qGvrpStatus = _FsDot1qGvrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 1, 1, 1, 6),
    _FsDot1qGvrpStatus_Type()
)
fsDot1qGvrpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1qGvrpStatus.setStatus("current")
_FsDot1qTp_ObjectIdentity = ObjectIdentity
fsDot1qTp = _FsDot1qTp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 2)
)
_FsDot1qFdbTable_Object = MibTable
fsDot1qFdbTable = _FsDot1qFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fsDot1qFdbTable.setStatus("current")
_FsDot1qFdbEntry_Object = MibTableRow
fsDot1qFdbEntry = _FsDot1qFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 2, 1, 1)
)
fsDot1qFdbEntry.setIndexNames(
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qVlanContextId"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qFdbId"),
)
if mibBuilder.loadTexts:
    fsDot1qFdbEntry.setStatus("current")
_FsDot1qFdbId_Type = Unsigned32
_FsDot1qFdbId_Object = MibTableColumn
fsDot1qFdbId = _FsDot1qFdbId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 2, 1, 1, 1),
    _FsDot1qFdbId_Type()
)
fsDot1qFdbId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDot1qFdbId.setStatus("current")
_FsDot1qFdbDynamicCount_Type = Counter32
_FsDot1qFdbDynamicCount_Object = MibTableColumn
fsDot1qFdbDynamicCount = _FsDot1qFdbDynamicCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 2, 1, 1, 2),
    _FsDot1qFdbDynamicCount_Type()
)
fsDot1qFdbDynamicCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1qFdbDynamicCount.setStatus("current")
_FsDot1qTpFdbTable_Object = MibTable
fsDot1qTpFdbTable = _FsDot1qTpFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 2, 2)
)
if mibBuilder.loadTexts:
    fsDot1qTpFdbTable.setStatus("current")
_FsDot1qTpFdbEntry_Object = MibTableRow
fsDot1qTpFdbEntry = _FsDot1qTpFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 2, 2, 1)
)
fsDot1qTpFdbEntry.setIndexNames(
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qVlanContextId"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qFdbId"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qTpFdbAddress"),
)
if mibBuilder.loadTexts:
    fsDot1qTpFdbEntry.setStatus("current")
_FsDot1qTpFdbAddress_Type = MacAddress
_FsDot1qTpFdbAddress_Object = MibTableColumn
fsDot1qTpFdbAddress = _FsDot1qTpFdbAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 2, 2, 1, 1),
    _FsDot1qTpFdbAddress_Type()
)
fsDot1qTpFdbAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDot1qTpFdbAddress.setStatus("current")


class _FsDot1qTpFdbPort_Type(Integer32):
    """Custom type fsDot1qTpFdbPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsDot1qTpFdbPort_Type.__name__ = "Integer32"
_FsDot1qTpFdbPort_Object = MibTableColumn
fsDot1qTpFdbPort = _FsDot1qTpFdbPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 2, 2, 1, 2),
    _FsDot1qTpFdbPort_Type()
)
fsDot1qTpFdbPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1qTpFdbPort.setStatus("current")


class _FsDot1qTpFdbStatus_Type(Integer32):
    """Custom type fsDot1qTpFdbStatus based on Integer32"""
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
        *(("other", 1),
          ("invalid", 2),
          ("learned", 3),
          ("self", 4),
          ("mgmt", 5))
    )


_FsDot1qTpFdbStatus_Type.__name__ = "Integer32"
_FsDot1qTpFdbStatus_Object = MibTableColumn
fsDot1qTpFdbStatus = _FsDot1qTpFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 2, 2, 1, 3),
    _FsDot1qTpFdbStatus_Type()
)
fsDot1qTpFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1qTpFdbStatus.setStatus("current")
_FsDot1qTpFdbPw_Type = Unsigned32
_FsDot1qTpFdbPw_Object = MibTableColumn
fsDot1qTpFdbPw = _FsDot1qTpFdbPw_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 2, 2, 1, 4),
    _FsDot1qTpFdbPw_Type()
)
fsDot1qTpFdbPw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1qTpFdbPw.setStatus("current")
_FsDot1qTpGroupTable_Object = MibTable
fsDot1qTpGroupTable = _FsDot1qTpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 2, 3)
)
if mibBuilder.loadTexts:
    fsDot1qTpGroupTable.setStatus("current")
_FsDot1qTpGroupEntry_Object = MibTableRow
fsDot1qTpGroupEntry = _FsDot1qTpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 2, 3, 1)
)
fsDot1qTpGroupEntry.setIndexNames(
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qVlanContextId"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qVlanIndex"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qTpGroupAddress"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qTpPort"),
)
if mibBuilder.loadTexts:
    fsDot1qTpGroupEntry.setStatus("current")
_FsDot1qVlanIndex_Type = VlanIndex
_FsDot1qVlanIndex_Object = MibTableColumn
fsDot1qVlanIndex = _FsDot1qVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 2, 3, 1, 1),
    _FsDot1qVlanIndex_Type()
)
fsDot1qVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDot1qVlanIndex.setStatus("current")
_FsDot1qTpGroupAddress_Type = MacAddress
_FsDot1qTpGroupAddress_Object = MibTableColumn
fsDot1qTpGroupAddress = _FsDot1qTpGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 2, 3, 1, 2),
    _FsDot1qTpGroupAddress_Type()
)
fsDot1qTpGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDot1qTpGroupAddress.setStatus("current")


class _FsDot1qTpPort_Type(Integer32):
    """Custom type fsDot1qTpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsDot1qTpPort_Type.__name__ = "Integer32"
_FsDot1qTpPort_Object = MibTableColumn
fsDot1qTpPort = _FsDot1qTpPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 2, 3, 1, 3),
    _FsDot1qTpPort_Type()
)
fsDot1qTpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDot1qTpPort.setStatus("current")
_FsDot1qTpGroupIsLearnt_Type = TruthValue
_FsDot1qTpGroupIsLearnt_Object = MibTableColumn
fsDot1qTpGroupIsLearnt = _FsDot1qTpGroupIsLearnt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 2, 3, 1, 4),
    _FsDot1qTpGroupIsLearnt_Type()
)
fsDot1qTpGroupIsLearnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1qTpGroupIsLearnt.setStatus("current")
_FsDot1qForwardAllLearntPortTable_Object = MibTable
fsDot1qForwardAllLearntPortTable = _FsDot1qForwardAllLearntPortTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 2, 4)
)
if mibBuilder.loadTexts:
    fsDot1qForwardAllLearntPortTable.setStatus("current")
_FsDot1qForwardAllLearntPortEntry_Object = MibTableRow
fsDot1qForwardAllLearntPortEntry = _FsDot1qForwardAllLearntPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 2, 4, 1)
)
fsDot1qForwardAllLearntPortEntry.setIndexNames(
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qVlanContextId"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qVlanIndex"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qTpPort"),
)
if mibBuilder.loadTexts:
    fsDot1qForwardAllLearntPortEntry.setStatus("current")
_FsDot1qForwardAllIsLearnt_Type = TruthValue
_FsDot1qForwardAllIsLearnt_Object = MibTableColumn
fsDot1qForwardAllIsLearnt = _FsDot1qForwardAllIsLearnt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 2, 4, 1, 1),
    _FsDot1qForwardAllIsLearnt_Type()
)
fsDot1qForwardAllIsLearnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1qForwardAllIsLearnt.setStatus("current")
_FsDot1qForwardAllStatusTable_Object = MibTable
fsDot1qForwardAllStatusTable = _FsDot1qForwardAllStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 2, 5)
)
if mibBuilder.loadTexts:
    fsDot1qForwardAllStatusTable.setStatus("current")
_FsDot1qForwardAllStatusEntry_Object = MibTableRow
fsDot1qForwardAllStatusEntry = _FsDot1qForwardAllStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 2, 5, 1)
)
fsDot1qForwardAllStatusEntry.setIndexNames(
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qVlanContextId"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    fsDot1qForwardAllStatusEntry.setStatus("current")
_FsDot1qForwardAllRowStatus_Type = RowStatus
_FsDot1qForwardAllRowStatus_Object = MibTableColumn
fsDot1qForwardAllRowStatus = _FsDot1qForwardAllRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 2, 5, 1, 1),
    _FsDot1qForwardAllRowStatus_Type()
)
fsDot1qForwardAllRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDot1qForwardAllRowStatus.setStatus("current")
_FsDot1qForwardAllPortConfigTable_Object = MibTable
fsDot1qForwardAllPortConfigTable = _FsDot1qForwardAllPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 2, 6)
)
if mibBuilder.loadTexts:
    fsDot1qForwardAllPortConfigTable.setStatus("current")
_FsDot1qForwardAllPortConfigEntry_Object = MibTableRow
fsDot1qForwardAllPortConfigEntry = _FsDot1qForwardAllPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 2, 6, 1)
)
fsDot1qForwardAllPortConfigEntry.setIndexNames(
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qVlanContextId"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qVlanIndex"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qTpPort"),
)
if mibBuilder.loadTexts:
    fsDot1qForwardAllPortConfigEntry.setStatus("current")


class _FsDot1qForwardAllPort_Type(Integer32):
    """Custom type fsDot1qForwardAllPort based on Integer32"""
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
        *(("addMember", 1),
          ("addForbidden", 2),
          ("delMember", 3),
          ("delForbidden", 4))
    )


_FsDot1qForwardAllPort_Type.__name__ = "Integer32"
_FsDot1qForwardAllPort_Object = MibTableColumn
fsDot1qForwardAllPort = _FsDot1qForwardAllPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 2, 6, 1, 1),
    _FsDot1qForwardAllPort_Type()
)
fsDot1qForwardAllPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1qForwardAllPort.setStatus("current")
_FsDot1qForwardUnregLearntPortTable_Object = MibTable
fsDot1qForwardUnregLearntPortTable = _FsDot1qForwardUnregLearntPortTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 2, 7)
)
if mibBuilder.loadTexts:
    fsDot1qForwardUnregLearntPortTable.setStatus("current")
_FsDot1qForwardUnregLearntPortEntry_Object = MibTableRow
fsDot1qForwardUnregLearntPortEntry = _FsDot1qForwardUnregLearntPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 2, 7, 1)
)
fsDot1qForwardUnregLearntPortEntry.setIndexNames(
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qVlanContextId"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qVlanIndex"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qTpPort"),
)
if mibBuilder.loadTexts:
    fsDot1qForwardUnregLearntPortEntry.setStatus("current")
_FsDot1qForwardUnregIsLearnt_Type = TruthValue
_FsDot1qForwardUnregIsLearnt_Object = MibTableColumn
fsDot1qForwardUnregIsLearnt = _FsDot1qForwardUnregIsLearnt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 2, 7, 1, 1),
    _FsDot1qForwardUnregIsLearnt_Type()
)
fsDot1qForwardUnregIsLearnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1qForwardUnregIsLearnt.setStatus("current")
_FsDot1qForwardUnregStatusTable_Object = MibTable
fsDot1qForwardUnregStatusTable = _FsDot1qForwardUnregStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 2, 8)
)
if mibBuilder.loadTexts:
    fsDot1qForwardUnregStatusTable.setStatus("current")
_FsDot1qForwardUnregStatusEntry_Object = MibTableRow
fsDot1qForwardUnregStatusEntry = _FsDot1qForwardUnregStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 2, 8, 1)
)
fsDot1qForwardUnregStatusEntry.setIndexNames(
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qVlanContextId"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    fsDot1qForwardUnregStatusEntry.setStatus("current")
_FsDot1qForwardUnregRowStatus_Type = RowStatus
_FsDot1qForwardUnregRowStatus_Object = MibTableColumn
fsDot1qForwardUnregRowStatus = _FsDot1qForwardUnregRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 2, 8, 1, 1),
    _FsDot1qForwardUnregRowStatus_Type()
)
fsDot1qForwardUnregRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDot1qForwardUnregRowStatus.setStatus("current")
_FsDot1qForwardUnregPortConfigTable_Object = MibTable
fsDot1qForwardUnregPortConfigTable = _FsDot1qForwardUnregPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 2, 9)
)
if mibBuilder.loadTexts:
    fsDot1qForwardUnregPortConfigTable.setStatus("current")
_FsDot1qForwardUnregPortConfigEntry_Object = MibTableRow
fsDot1qForwardUnregPortConfigEntry = _FsDot1qForwardUnregPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 2, 9, 1)
)
fsDot1qForwardUnregPortConfigEntry.setIndexNames(
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qVlanContextId"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qVlanIndex"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qTpPort"),
)
if mibBuilder.loadTexts:
    fsDot1qForwardUnregPortConfigEntry.setStatus("current")


class _FsDot1qForwardUnregPort_Type(Integer32):
    """Custom type fsDot1qForwardUnregPort based on Integer32"""
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
        *(("addMember", 1),
          ("addForbidden", 2),
          ("delMember", 3),
          ("delForbidden", 4))
    )


_FsDot1qForwardUnregPort_Type.__name__ = "Integer32"
_FsDot1qForwardUnregPort_Object = MibTableColumn
fsDot1qForwardUnregPort = _FsDot1qForwardUnregPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 2, 9, 1, 1),
    _FsDot1qForwardUnregPort_Type()
)
fsDot1qForwardUnregPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1qForwardUnregPort.setStatus("current")
_FsDot1qStatic_ObjectIdentity = ObjectIdentity
fsDot1qStatic = _FsDot1qStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 3)
)
_FsDot1qStaticUnicastTable_Object = MibTable
fsDot1qStaticUnicastTable = _FsDot1qStaticUnicastTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 3, 1)
)
if mibBuilder.loadTexts:
    fsDot1qStaticUnicastTable.setStatus("current")
_FsDot1qStaticUnicastEntry_Object = MibTableRow
fsDot1qStaticUnicastEntry = _FsDot1qStaticUnicastEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 3, 1, 1)
)
fsDot1qStaticUnicastEntry.setIndexNames(
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qVlanContextId"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qFdbId"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qStaticUnicastAddress"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qStaticUnicastReceivePort"),
)
if mibBuilder.loadTexts:
    fsDot1qStaticUnicastEntry.setStatus("current")
_FsDot1qStaticUnicastAddress_Type = MacAddress
_FsDot1qStaticUnicastAddress_Object = MibTableColumn
fsDot1qStaticUnicastAddress = _FsDot1qStaticUnicastAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 3, 1, 1, 1),
    _FsDot1qStaticUnicastAddress_Type()
)
fsDot1qStaticUnicastAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDot1qStaticUnicastAddress.setStatus("current")


class _FsDot1qStaticUnicastReceivePort_Type(Integer32):
    """Custom type fsDot1qStaticUnicastReceivePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsDot1qStaticUnicastReceivePort_Type.__name__ = "Integer32"
_FsDot1qStaticUnicastReceivePort_Object = MibTableColumn
fsDot1qStaticUnicastReceivePort = _FsDot1qStaticUnicastReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 3, 1, 1, 2),
    _FsDot1qStaticUnicastReceivePort_Type()
)
fsDot1qStaticUnicastReceivePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDot1qStaticUnicastReceivePort.setStatus("current")
_FsDot1qStaticUnicastRowStatus_Type = RowStatus
_FsDot1qStaticUnicastRowStatus_Object = MibTableColumn
fsDot1qStaticUnicastRowStatus = _FsDot1qStaticUnicastRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 3, 1, 1, 3),
    _FsDot1qStaticUnicastRowStatus_Type()
)
fsDot1qStaticUnicastRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDot1qStaticUnicastRowStatus.setStatus("current")


class _FsDot1qStaticUnicastStatus_Type(Integer32):
    """Custom type fsDot1qStaticUnicastStatus based on Integer32"""
    defaultValue = 3

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
        *(("other", 1),
          ("invalid", 2),
          ("permanent", 3),
          ("deleteOnReset", 4),
          ("deleteOnTimeout", 5))
    )


_FsDot1qStaticUnicastStatus_Type.__name__ = "Integer32"
_FsDot1qStaticUnicastStatus_Object = MibTableColumn
fsDot1qStaticUnicastStatus = _FsDot1qStaticUnicastStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 3, 1, 1, 4),
    _FsDot1qStaticUnicastStatus_Type()
)
fsDot1qStaticUnicastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1qStaticUnicastStatus.setStatus("current")
_FsDot1qStaticAllowedToGoTable_Object = MibTable
fsDot1qStaticAllowedToGoTable = _FsDot1qStaticAllowedToGoTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 3, 2)
)
if mibBuilder.loadTexts:
    fsDot1qStaticAllowedToGoTable.setStatus("current")
_FsDot1qStaticAllowedToGoEntry_Object = MibTableRow
fsDot1qStaticAllowedToGoEntry = _FsDot1qStaticAllowedToGoEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 3, 2, 1)
)
fsDot1qStaticAllowedToGoEntry.setIndexNames(
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qVlanContextId"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qFdbId"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qStaticUnicastAddress"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qStaticUnicastReceivePort"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qTpPort"),
)
if mibBuilder.loadTexts:
    fsDot1qStaticAllowedToGoEntry.setStatus("current")
_FsDot1qStaticAllowedIsMember_Type = TruthValue
_FsDot1qStaticAllowedIsMember_Object = MibTableColumn
fsDot1qStaticAllowedIsMember = _FsDot1qStaticAllowedIsMember_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 3, 2, 1, 1),
    _FsDot1qStaticAllowedIsMember_Type()
)
fsDot1qStaticAllowedIsMember.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1qStaticAllowedIsMember.setStatus("current")
_FsDot1qStaticMulticastTable_Object = MibTable
fsDot1qStaticMulticastTable = _FsDot1qStaticMulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 3, 3)
)
if mibBuilder.loadTexts:
    fsDot1qStaticMulticastTable.setStatus("current")
_FsDot1qStaticMulticastEntry_Object = MibTableRow
fsDot1qStaticMulticastEntry = _FsDot1qStaticMulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 3, 3, 1)
)
fsDot1qStaticMulticastEntry.setIndexNames(
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qVlanContextId"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qVlanIndex"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qStaticMulticastAddress"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qStaticMulticastReceivePort"),
)
if mibBuilder.loadTexts:
    fsDot1qStaticMulticastEntry.setStatus("current")
_FsDot1qStaticMulticastAddress_Type = MacAddress
_FsDot1qStaticMulticastAddress_Object = MibTableColumn
fsDot1qStaticMulticastAddress = _FsDot1qStaticMulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 3, 3, 1, 1),
    _FsDot1qStaticMulticastAddress_Type()
)
fsDot1qStaticMulticastAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDot1qStaticMulticastAddress.setStatus("current")


class _FsDot1qStaticMulticastReceivePort_Type(Integer32):
    """Custom type fsDot1qStaticMulticastReceivePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsDot1qStaticMulticastReceivePort_Type.__name__ = "Integer32"
_FsDot1qStaticMulticastReceivePort_Object = MibTableColumn
fsDot1qStaticMulticastReceivePort = _FsDot1qStaticMulticastReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 3, 3, 1, 2),
    _FsDot1qStaticMulticastReceivePort_Type()
)
fsDot1qStaticMulticastReceivePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDot1qStaticMulticastReceivePort.setStatus("current")
_FsDot1qStaticMulticastRowStatus_Type = RowStatus
_FsDot1qStaticMulticastRowStatus_Object = MibTableColumn
fsDot1qStaticMulticastRowStatus = _FsDot1qStaticMulticastRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 3, 3, 1, 3),
    _FsDot1qStaticMulticastRowStatus_Type()
)
fsDot1qStaticMulticastRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDot1qStaticMulticastRowStatus.setStatus("current")


class _FsDot1qStaticMulticastStatus_Type(Integer32):
    """Custom type fsDot1qStaticMulticastStatus based on Integer32"""
    defaultValue = 3

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
        *(("other", 1),
          ("invalid", 2),
          ("permanent", 3),
          ("deleteOnReset", 4),
          ("deleteOnTimeout", 5))
    )


_FsDot1qStaticMulticastStatus_Type.__name__ = "Integer32"
_FsDot1qStaticMulticastStatus_Object = MibTableColumn
fsDot1qStaticMulticastStatus = _FsDot1qStaticMulticastStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 3, 3, 1, 4),
    _FsDot1qStaticMulticastStatus_Type()
)
fsDot1qStaticMulticastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1qStaticMulticastStatus.setStatus("current")
_FsDot1qStaticMcastPortTable_Object = MibTable
fsDot1qStaticMcastPortTable = _FsDot1qStaticMcastPortTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 3, 4)
)
if mibBuilder.loadTexts:
    fsDot1qStaticMcastPortTable.setStatus("current")
_FsDot1qStaticMcastPortEntry_Object = MibTableRow
fsDot1qStaticMcastPortEntry = _FsDot1qStaticMcastPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 3, 4, 1)
)
fsDot1qStaticMcastPortEntry.setIndexNames(
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qVlanContextId"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qVlanIndex"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qStaticMulticastAddress"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qStaticMulticastReceivePort"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qTpPort"),
)
if mibBuilder.loadTexts:
    fsDot1qStaticMcastPortEntry.setStatus("current")


class _FsDot1qStaticMcastPort_Type(Integer32):
    """Custom type fsDot1qStaticMcastPort based on Integer32"""
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
        *(("addMember", 1),
          ("addForbidden", 2),
          ("delMember", 3),
          ("delForbidden", 4))
    )


_FsDot1qStaticMcastPort_Type.__name__ = "Integer32"
_FsDot1qStaticMcastPort_Object = MibTableColumn
fsDot1qStaticMcastPort = _FsDot1qStaticMcastPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 3, 4, 1, 1),
    _FsDot1qStaticMcastPort_Type()
)
fsDot1qStaticMcastPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1qStaticMcastPort.setStatus("current")
_FsDot1qVlan_ObjectIdentity = ObjectIdentity
fsDot1qVlan = _FsDot1qVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4)
)
_FsDot1qVlanNumDeletesTable_Object = MibTable
fsDot1qVlanNumDeletesTable = _FsDot1qVlanNumDeletesTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 1)
)
if mibBuilder.loadTexts:
    fsDot1qVlanNumDeletesTable.setStatus("current")
_FsDot1qVlanNumDeletesEntry_Object = MibTableRow
fsDot1qVlanNumDeletesEntry = _FsDot1qVlanNumDeletesEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 1, 1)
)
fsDot1qVlanNumDeletesEntry.setIndexNames(
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qVlanContextId"),
)
if mibBuilder.loadTexts:
    fsDot1qVlanNumDeletesEntry.setStatus("current")
_FsDot1qVlanNumDeletes_Type = Counter32
_FsDot1qVlanNumDeletes_Object = MibTableColumn
fsDot1qVlanNumDeletes = _FsDot1qVlanNumDeletes_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 1, 1, 1),
    _FsDot1qVlanNumDeletes_Type()
)
fsDot1qVlanNumDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1qVlanNumDeletes.setStatus("current")
_FsDot1qVlanCurrentTable_Object = MibTable
fsDot1qVlanCurrentTable = _FsDot1qVlanCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 2)
)
if mibBuilder.loadTexts:
    fsDot1qVlanCurrentTable.setStatus("current")
_FsDot1qVlanCurrentEntry_Object = MibTableRow
fsDot1qVlanCurrentEntry = _FsDot1qVlanCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 2, 1)
)
fsDot1qVlanCurrentEntry.setIndexNames(
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qVlanContextId"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qVlanTimeMark"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    fsDot1qVlanCurrentEntry.setStatus("current")
_FsDot1qVlanTimeMark_Type = TimeFilter
_FsDot1qVlanTimeMark_Object = MibTableColumn
fsDot1qVlanTimeMark = _FsDot1qVlanTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 2, 1, 1),
    _FsDot1qVlanTimeMark_Type()
)
fsDot1qVlanTimeMark.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDot1qVlanTimeMark.setStatus("current")
_FsDot1qVlanFdbId_Type = Unsigned32
_FsDot1qVlanFdbId_Object = MibTableColumn
fsDot1qVlanFdbId = _FsDot1qVlanFdbId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 2, 1, 2),
    _FsDot1qVlanFdbId_Type()
)
fsDot1qVlanFdbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1qVlanFdbId.setStatus("current")


class _FsDot1qVlanStatus_Type(Integer32):
    """Custom type fsDot1qVlanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("permanent", 2),
          ("dynamicGvrp", 3))
    )


_FsDot1qVlanStatus_Type.__name__ = "Integer32"
_FsDot1qVlanStatus_Object = MibTableColumn
fsDot1qVlanStatus = _FsDot1qVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 2, 1, 3),
    _FsDot1qVlanStatus_Type()
)
fsDot1qVlanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1qVlanStatus.setStatus("current")
_FsDot1qVlanCreationTime_Type = TimeTicks
_FsDot1qVlanCreationTime_Object = MibTableColumn
fsDot1qVlanCreationTime = _FsDot1qVlanCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 2, 1, 4),
    _FsDot1qVlanCreationTime_Type()
)
fsDot1qVlanCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1qVlanCreationTime.setStatus("current")
_FsDot1qVlanEgressPortTable_Object = MibTable
fsDot1qVlanEgressPortTable = _FsDot1qVlanEgressPortTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 3)
)
if mibBuilder.loadTexts:
    fsDot1qVlanEgressPortTable.setStatus("current")
_FsDot1qVlanEgressPortEntry_Object = MibTableRow
fsDot1qVlanEgressPortEntry = _FsDot1qVlanEgressPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 3, 1)
)
fsDot1qVlanEgressPortEntry.setIndexNames(
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qVlanContextId"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qVlanTimeMark"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qVlanIndex"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qTpPort"),
)
if mibBuilder.loadTexts:
    fsDot1qVlanEgressPortEntry.setStatus("current")


class _FsDot1qVlanCurrentEgressPort_Type(Integer32):
    """Custom type fsDot1qVlanCurrentEgressPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tagged", 1),
          ("untagged", 2))
    )


_FsDot1qVlanCurrentEgressPort_Type.__name__ = "Integer32"
_FsDot1qVlanCurrentEgressPort_Object = MibTableColumn
fsDot1qVlanCurrentEgressPort = _FsDot1qVlanCurrentEgressPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 3, 1, 1),
    _FsDot1qVlanCurrentEgressPort_Type()
)
fsDot1qVlanCurrentEgressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1qVlanCurrentEgressPort.setStatus("current")
_FsDot1qVlanStaticTable_Object = MibTable
fsDot1qVlanStaticTable = _FsDot1qVlanStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 4)
)
if mibBuilder.loadTexts:
    fsDot1qVlanStaticTable.setStatus("current")
_FsDot1qVlanStaticEntry_Object = MibTableRow
fsDot1qVlanStaticEntry = _FsDot1qVlanStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 4, 1)
)
fsDot1qVlanStaticEntry.setIndexNames(
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qVlanContextId"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    fsDot1qVlanStaticEntry.setStatus("current")


class _FsDot1qVlanStaticName_Type(SnmpAdminString):
    """Custom type fsDot1qVlanStaticName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsDot1qVlanStaticName_Type.__name__ = "SnmpAdminString"
_FsDot1qVlanStaticName_Object = MibTableColumn
fsDot1qVlanStaticName = _FsDot1qVlanStaticName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 4, 1, 1),
    _FsDot1qVlanStaticName_Type()
)
fsDot1qVlanStaticName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDot1qVlanStaticName.setStatus("current")
_FsDot1qVlanStaticRowStatus_Type = RowStatus
_FsDot1qVlanStaticRowStatus_Object = MibTableColumn
fsDot1qVlanStaticRowStatus = _FsDot1qVlanStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 4, 1, 2),
    _FsDot1qVlanStaticRowStatus_Type()
)
fsDot1qVlanStaticRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDot1qVlanStaticRowStatus.setStatus("current")
_FsDot1qVlanStaticPortConfigTable_Object = MibTable
fsDot1qVlanStaticPortConfigTable = _FsDot1qVlanStaticPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 5)
)
if mibBuilder.loadTexts:
    fsDot1qVlanStaticPortConfigTable.setStatus("current")
_FsDot1qVlanStaticPortConfigEntry_Object = MibTableRow
fsDot1qVlanStaticPortConfigEntry = _FsDot1qVlanStaticPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 5, 1)
)
fsDot1qVlanStaticPortConfigEntry.setIndexNames(
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qVlanContextId"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qVlanIndex"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qTpPort"),
)
if mibBuilder.loadTexts:
    fsDot1qVlanStaticPortConfigEntry.setStatus("current")


class _FsDot1qVlanStaticPort_Type(Integer32):
    """Custom type fsDot1qVlanStaticPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("addTagged", 1),
          ("addUntagged", 2),
          ("addForbidden", 3),
          ("delTagged", 4),
          ("delUntagged", 5),
          ("delForbidden", 6))
    )


_FsDot1qVlanStaticPort_Type.__name__ = "Integer32"
_FsDot1qVlanStaticPort_Object = MibTableColumn
fsDot1qVlanStaticPort = _FsDot1qVlanStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 5, 1, 1),
    _FsDot1qVlanStaticPort_Type()
)
fsDot1qVlanStaticPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1qVlanStaticPort.setStatus("current")
_FsDot1qNextFreeLocalVlanIndexTable_Object = MibTable
fsDot1qNextFreeLocalVlanIndexTable = _FsDot1qNextFreeLocalVlanIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 6)
)
if mibBuilder.loadTexts:
    fsDot1qNextFreeLocalVlanIndexTable.setStatus("current")
_FsDot1qNextFreeLocalVlanIndexEntry_Object = MibTableRow
fsDot1qNextFreeLocalVlanIndexEntry = _FsDot1qNextFreeLocalVlanIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 6, 1)
)
fsDot1qNextFreeLocalVlanIndexEntry.setIndexNames(
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qVlanContextId"),
)
if mibBuilder.loadTexts:
    fsDot1qNextFreeLocalVlanIndexEntry.setStatus("current")


class _FsDot1qNextFreeLocalVlanIndex_Type(Integer32):
    """Custom type fsDot1qNextFreeLocalVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4096, 2147483647),
    )


_FsDot1qNextFreeLocalVlanIndex_Type.__name__ = "Integer32"
_FsDot1qNextFreeLocalVlanIndex_Object = MibTableColumn
fsDot1qNextFreeLocalVlanIndex = _FsDot1qNextFreeLocalVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 6, 1, 1),
    _FsDot1qNextFreeLocalVlanIndex_Type()
)
fsDot1qNextFreeLocalVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1qNextFreeLocalVlanIndex.setStatus("current")
_FsDot1qPortVlanTable_Object = MibTable
fsDot1qPortVlanTable = _FsDot1qPortVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 7)
)
if mibBuilder.loadTexts:
    fsDot1qPortVlanTable.setStatus("current")
_FsDot1qPortVlanEntry_Object = MibTableRow
fsDot1qPortVlanEntry = _FsDot1qPortVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 7, 1)
)
fsDot1qPortVlanEntry.setIndexNames(
    (0, "SUPERMICRO-MIStdBRIDGE-MIB", "fsDot1dBasePort"),
)
if mibBuilder.loadTexts:
    fsDot1qPortVlanEntry.setStatus("current")


class _FsDot1qPvid_Type(VlanIndex):
    """Custom type fsDot1qPvid based on VlanIndex"""
    defaultValue = 1


_FsDot1qPvid_Type.__name__ = "VlanIndex"
_FsDot1qPvid_Object = MibTableColumn
fsDot1qPvid = _FsDot1qPvid_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 7, 1, 1),
    _FsDot1qPvid_Type()
)
fsDot1qPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1qPvid.setStatus("current")


class _FsDot1qPortAcceptableFrameTypes_Type(Integer32):
    """Custom type fsDot1qPortAcceptableFrameTypes based on Integer32"""
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
        *(("admitAll", 1),
          ("admitOnlyVlanTagged", 2),
          ("admitOnlyUntaggedAndPriorityTagged", 3))
    )


_FsDot1qPortAcceptableFrameTypes_Type.__name__ = "Integer32"
_FsDot1qPortAcceptableFrameTypes_Object = MibTableColumn
fsDot1qPortAcceptableFrameTypes = _FsDot1qPortAcceptableFrameTypes_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 7, 1, 2),
    _FsDot1qPortAcceptableFrameTypes_Type()
)
fsDot1qPortAcceptableFrameTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1qPortAcceptableFrameTypes.setStatus("current")


class _FsDot1qPortIngressFiltering_Type(TruthValue):
    """Custom type fsDot1qPortIngressFiltering based on TruthValue"""
    defaultValue = 1


_FsDot1qPortIngressFiltering_Type.__name__ = "TruthValue"
_FsDot1qPortIngressFiltering_Object = MibTableColumn
fsDot1qPortIngressFiltering = _FsDot1qPortIngressFiltering_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 7, 1, 3),
    _FsDot1qPortIngressFiltering_Type()
)
fsDot1qPortIngressFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1qPortIngressFiltering.setStatus("current")


class _FsDot1qPortGvrpStatus_Type(EnabledStatus):
    """Custom type fsDot1qPortGvrpStatus based on EnabledStatus"""
    defaultValue = 1


_FsDot1qPortGvrpStatus_Type.__name__ = "EnabledStatus"
_FsDot1qPortGvrpStatus_Object = MibTableColumn
fsDot1qPortGvrpStatus = _FsDot1qPortGvrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 7, 1, 4),
    _FsDot1qPortGvrpStatus_Type()
)
fsDot1qPortGvrpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1qPortGvrpStatus.setStatus("current")
_FsDot1qPortGvrpFailedRegistrations_Type = Counter32
_FsDot1qPortGvrpFailedRegistrations_Object = MibTableColumn
fsDot1qPortGvrpFailedRegistrations = _FsDot1qPortGvrpFailedRegistrations_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 7, 1, 5),
    _FsDot1qPortGvrpFailedRegistrations_Type()
)
fsDot1qPortGvrpFailedRegistrations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1qPortGvrpFailedRegistrations.setStatus("current")
_FsDot1qPortGvrpLastPduOrigin_Type = MacAddress
_FsDot1qPortGvrpLastPduOrigin_Object = MibTableColumn
fsDot1qPortGvrpLastPduOrigin = _FsDot1qPortGvrpLastPduOrigin_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 7, 1, 6),
    _FsDot1qPortGvrpLastPduOrigin_Type()
)
fsDot1qPortGvrpLastPduOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1qPortGvrpLastPduOrigin.setStatus("current")


class _FsDot1qPortRestrictedVlanRegistration_Type(TruthValue):
    """Custom type fsDot1qPortRestrictedVlanRegistration based on TruthValue"""
    defaultValue = 2


_FsDot1qPortRestrictedVlanRegistration_Type.__name__ = "TruthValue"
_FsDot1qPortRestrictedVlanRegistration_Object = MibTableColumn
fsDot1qPortRestrictedVlanRegistration = _FsDot1qPortRestrictedVlanRegistration_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 7, 1, 7),
    _FsDot1qPortRestrictedVlanRegistration_Type()
)
fsDot1qPortRestrictedVlanRegistration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1qPortRestrictedVlanRegistration.setStatus("current")
_FsDot1qPortVlanStatisticsTable_Object = MibTable
fsDot1qPortVlanStatisticsTable = _FsDot1qPortVlanStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 8)
)
if mibBuilder.loadTexts:
    fsDot1qPortVlanStatisticsTable.setStatus("current")
_FsDot1qPortVlanStatisticsEntry_Object = MibTableRow
fsDot1qPortVlanStatisticsEntry = _FsDot1qPortVlanStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 8, 1)
)
fsDot1qPortVlanStatisticsEntry.setIndexNames(
    (0, "SUPERMICRO-MIStdBRIDGE-MIB", "fsDot1dBasePort"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    fsDot1qPortVlanStatisticsEntry.setStatus("current")
_FsDot1qTpVlanPortInFrames_Type = Counter32
_FsDot1qTpVlanPortInFrames_Object = MibTableColumn
fsDot1qTpVlanPortInFrames = _FsDot1qTpVlanPortInFrames_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 8, 1, 1),
    _FsDot1qTpVlanPortInFrames_Type()
)
fsDot1qTpVlanPortInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1qTpVlanPortInFrames.setStatus("current")
_FsDot1qTpVlanPortOutFrames_Type = Counter32
_FsDot1qTpVlanPortOutFrames_Object = MibTableColumn
fsDot1qTpVlanPortOutFrames = _FsDot1qTpVlanPortOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 8, 1, 2),
    _FsDot1qTpVlanPortOutFrames_Type()
)
fsDot1qTpVlanPortOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1qTpVlanPortOutFrames.setStatus("current")
_FsDot1qTpVlanPortInDiscards_Type = Counter32
_FsDot1qTpVlanPortInDiscards_Object = MibTableColumn
fsDot1qTpVlanPortInDiscards = _FsDot1qTpVlanPortInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 8, 1, 3),
    _FsDot1qTpVlanPortInDiscards_Type()
)
fsDot1qTpVlanPortInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1qTpVlanPortInDiscards.setStatus("current")
_FsDot1qTpVlanPortInOverflowFrames_Type = Counter32
_FsDot1qTpVlanPortInOverflowFrames_Object = MibTableColumn
fsDot1qTpVlanPortInOverflowFrames = _FsDot1qTpVlanPortInOverflowFrames_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 8, 1, 4),
    _FsDot1qTpVlanPortInOverflowFrames_Type()
)
fsDot1qTpVlanPortInOverflowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1qTpVlanPortInOverflowFrames.setStatus("current")
_FsDot1qTpVlanPortOutOverflowFrames_Type = Counter32
_FsDot1qTpVlanPortOutOverflowFrames_Object = MibTableColumn
fsDot1qTpVlanPortOutOverflowFrames = _FsDot1qTpVlanPortOutOverflowFrames_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 8, 1, 5),
    _FsDot1qTpVlanPortOutOverflowFrames_Type()
)
fsDot1qTpVlanPortOutOverflowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1qTpVlanPortOutOverflowFrames.setStatus("current")
_FsDot1qTpVlanPortInOverflowDiscards_Type = Counter32
_FsDot1qTpVlanPortInOverflowDiscards_Object = MibTableColumn
fsDot1qTpVlanPortInOverflowDiscards = _FsDot1qTpVlanPortInOverflowDiscards_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 8, 1, 6),
    _FsDot1qTpVlanPortInOverflowDiscards_Type()
)
fsDot1qTpVlanPortInOverflowDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1qTpVlanPortInOverflowDiscards.setStatus("current")
_FsDot1qPortVlanHCStatisticsTable_Object = MibTable
fsDot1qPortVlanHCStatisticsTable = _FsDot1qPortVlanHCStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 9)
)
if mibBuilder.loadTexts:
    fsDot1qPortVlanHCStatisticsTable.setStatus("current")
_FsDot1qPortVlanHCStatisticsEntry_Object = MibTableRow
fsDot1qPortVlanHCStatisticsEntry = _FsDot1qPortVlanHCStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 9, 1)
)
fsDot1qPortVlanHCStatisticsEntry.setIndexNames(
    (0, "SUPERMICRO-MIStdBRIDGE-MIB", "fsDot1dBasePort"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    fsDot1qPortVlanHCStatisticsEntry.setStatus("current")
_FsDot1qTpVlanPortHCInFrames_Type = Counter64
_FsDot1qTpVlanPortHCInFrames_Object = MibTableColumn
fsDot1qTpVlanPortHCInFrames = _FsDot1qTpVlanPortHCInFrames_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 9, 1, 1),
    _FsDot1qTpVlanPortHCInFrames_Type()
)
fsDot1qTpVlanPortHCInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1qTpVlanPortHCInFrames.setStatus("current")
_FsDot1qTpVlanPortHCOutFrames_Type = Counter64
_FsDot1qTpVlanPortHCOutFrames_Object = MibTableColumn
fsDot1qTpVlanPortHCOutFrames = _FsDot1qTpVlanPortHCOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 9, 1, 2),
    _FsDot1qTpVlanPortHCOutFrames_Type()
)
fsDot1qTpVlanPortHCOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1qTpVlanPortHCOutFrames.setStatus("current")
_FsDot1qTpVlanPortHCInDiscards_Type = Counter64
_FsDot1qTpVlanPortHCInDiscards_Object = MibTableColumn
fsDot1qTpVlanPortHCInDiscards = _FsDot1qTpVlanPortHCInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 9, 1, 3),
    _FsDot1qTpVlanPortHCInDiscards_Type()
)
fsDot1qTpVlanPortHCInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1qTpVlanPortHCInDiscards.setStatus("current")
_FsDot1qLearningConstraintsTable_Object = MibTable
fsDot1qLearningConstraintsTable = _FsDot1qLearningConstraintsTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 10)
)
if mibBuilder.loadTexts:
    fsDot1qLearningConstraintsTable.setStatus("current")
_FsDot1qLearningConstraintsEntry_Object = MibTableRow
fsDot1qLearningConstraintsEntry = _FsDot1qLearningConstraintsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 10, 1)
)
fsDot1qLearningConstraintsEntry.setIndexNames(
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qVlanContextId"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qConstraintVlan"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qConstraintSet"),
)
if mibBuilder.loadTexts:
    fsDot1qLearningConstraintsEntry.setStatus("current")
_FsDot1qConstraintVlan_Type = VlanIndex
_FsDot1qConstraintVlan_Object = MibTableColumn
fsDot1qConstraintVlan = _FsDot1qConstraintVlan_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 10, 1, 1),
    _FsDot1qConstraintVlan_Type()
)
fsDot1qConstraintVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDot1qConstraintVlan.setStatus("current")


class _FsDot1qConstraintSet_Type(Integer32):
    """Custom type fsDot1qConstraintSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsDot1qConstraintSet_Type.__name__ = "Integer32"
_FsDot1qConstraintSet_Object = MibTableColumn
fsDot1qConstraintSet = _FsDot1qConstraintSet_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 10, 1, 2),
    _FsDot1qConstraintSet_Type()
)
fsDot1qConstraintSet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDot1qConstraintSet.setStatus("current")


class _FsDot1qConstraintType_Type(Integer32):
    """Custom type fsDot1qConstraintType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("independent", 1),
          ("shared", 2))
    )


_FsDot1qConstraintType_Type.__name__ = "Integer32"
_FsDot1qConstraintType_Object = MibTableColumn
fsDot1qConstraintType = _FsDot1qConstraintType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 10, 1, 3),
    _FsDot1qConstraintType_Type()
)
fsDot1qConstraintType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDot1qConstraintType.setStatus("current")
_FsDot1qConstraintStatus_Type = RowStatus
_FsDot1qConstraintStatus_Object = MibTableColumn
fsDot1qConstraintStatus = _FsDot1qConstraintStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 10, 1, 4),
    _FsDot1qConstraintStatus_Type()
)
fsDot1qConstraintStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDot1qConstraintStatus.setStatus("current")
_FsDot1qConstraintDefaultTable_Object = MibTable
fsDot1qConstraintDefaultTable = _FsDot1qConstraintDefaultTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 11)
)
if mibBuilder.loadTexts:
    fsDot1qConstraintDefaultTable.setStatus("current")
_FsDot1qConstraintDefaultEntry_Object = MibTableRow
fsDot1qConstraintDefaultEntry = _FsDot1qConstraintDefaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 11, 1)
)
fsDot1qConstraintDefaultEntry.setIndexNames(
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qVlanContextId"),
)
if mibBuilder.loadTexts:
    fsDot1qConstraintDefaultEntry.setStatus("current")


class _FsDot1qConstraintSetDefault_Type(Integer32):
    """Custom type fsDot1qConstraintSetDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsDot1qConstraintSetDefault_Type.__name__ = "Integer32"
_FsDot1qConstraintSetDefault_Object = MibTableColumn
fsDot1qConstraintSetDefault = _FsDot1qConstraintSetDefault_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 11, 1, 1),
    _FsDot1qConstraintSetDefault_Type()
)
fsDot1qConstraintSetDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1qConstraintSetDefault.setStatus("current")


class _FsDot1qConstraintTypeDefault_Type(Integer32):
    """Custom type fsDot1qConstraintTypeDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("independent", 1),
          ("shared", 2))
    )


_FsDot1qConstraintTypeDefault_Type.__name__ = "Integer32"
_FsDot1qConstraintTypeDefault_Object = MibTableColumn
fsDot1qConstraintTypeDefault = _FsDot1qConstraintTypeDefault_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 4, 11, 1, 2),
    _FsDot1qConstraintTypeDefault_Type()
)
fsDot1qConstraintTypeDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1qConstraintTypeDefault.setStatus("current")
_FsDot1vProtocol_ObjectIdentity = ObjectIdentity
fsDot1vProtocol = _FsDot1vProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 5)
)
_FsDot1vProtocolGroupTable_Object = MibTable
fsDot1vProtocolGroupTable = _FsDot1vProtocolGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 5, 1)
)
if mibBuilder.loadTexts:
    fsDot1vProtocolGroupTable.setStatus("current")
_FsDot1vProtocolGroupEntry_Object = MibTableRow
fsDot1vProtocolGroupEntry = _FsDot1vProtocolGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 5, 1, 1)
)
fsDot1vProtocolGroupEntry.setIndexNames(
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1qVlanContextId"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1vProtocolTemplateFrameType"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1vProtocolTemplateProtocolValue"),
)
if mibBuilder.loadTexts:
    fsDot1vProtocolGroupEntry.setStatus("current")


class _FsDot1vProtocolTemplateFrameType_Type(Integer32):
    """Custom type fsDot1vProtocolTemplateFrameType based on Integer32"""
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
        *(("ethernet", 1),
          ("rfc1042", 2),
          ("snap8021H", 3),
          ("snapOther", 4),
          ("llcOther", 5))
    )


_FsDot1vProtocolTemplateFrameType_Type.__name__ = "Integer32"
_FsDot1vProtocolTemplateFrameType_Object = MibTableColumn
fsDot1vProtocolTemplateFrameType = _FsDot1vProtocolTemplateFrameType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 5, 1, 1, 1),
    _FsDot1vProtocolTemplateFrameType_Type()
)
fsDot1vProtocolTemplateFrameType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDot1vProtocolTemplateFrameType.setStatus("current")


class _FsDot1vProtocolTemplateProtocolValue_Type(OctetString):
    """Custom type fsDot1vProtocolTemplateProtocolValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
        ValueSizeConstraint(5, 5),
    )


_FsDot1vProtocolTemplateProtocolValue_Type.__name__ = "OctetString"
_FsDot1vProtocolTemplateProtocolValue_Object = MibTableColumn
fsDot1vProtocolTemplateProtocolValue = _FsDot1vProtocolTemplateProtocolValue_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 5, 1, 1, 2),
    _FsDot1vProtocolTemplateProtocolValue_Type()
)
fsDot1vProtocolTemplateProtocolValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDot1vProtocolTemplateProtocolValue.setStatus("current")


class _FsDot1vProtocolGroupId_Type(Integer32):
    """Custom type fsDot1vProtocolGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsDot1vProtocolGroupId_Type.__name__ = "Integer32"
_FsDot1vProtocolGroupId_Object = MibTableColumn
fsDot1vProtocolGroupId = _FsDot1vProtocolGroupId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 5, 1, 1, 3),
    _FsDot1vProtocolGroupId_Type()
)
fsDot1vProtocolGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDot1vProtocolGroupId.setStatus("current")
_FsDot1vProtocolGroupRowStatus_Type = RowStatus
_FsDot1vProtocolGroupRowStatus_Object = MibTableColumn
fsDot1vProtocolGroupRowStatus = _FsDot1vProtocolGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 5, 1, 1, 4),
    _FsDot1vProtocolGroupRowStatus_Type()
)
fsDot1vProtocolGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDot1vProtocolGroupRowStatus.setStatus("current")
_FsDot1vProtocolPortTable_Object = MibTable
fsDot1vProtocolPortTable = _FsDot1vProtocolPortTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 5, 2)
)
if mibBuilder.loadTexts:
    fsDot1vProtocolPortTable.setStatus("current")
_FsDot1vProtocolPortEntry_Object = MibTableRow
fsDot1vProtocolPortEntry = _FsDot1vProtocolPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 5, 2, 1)
)
fsDot1vProtocolPortEntry.setIndexNames(
    (0, "SUPERMICRO-MIStdBRIDGE-MIB", "fsDot1dBasePort"),
    (0, "SUPERMICROQ-BRIDGE-MIB", "fsDot1vProtocolPortGroupId"),
)
if mibBuilder.loadTexts:
    fsDot1vProtocolPortEntry.setStatus("current")


class _FsDot1vProtocolPortGroupId_Type(Integer32):
    """Custom type fsDot1vProtocolPortGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsDot1vProtocolPortGroupId_Type.__name__ = "Integer32"
_FsDot1vProtocolPortGroupId_Object = MibTableColumn
fsDot1vProtocolPortGroupId = _FsDot1vProtocolPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 5, 2, 1, 1),
    _FsDot1vProtocolPortGroupId_Type()
)
fsDot1vProtocolPortGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDot1vProtocolPortGroupId.setStatus("current")


class _FsDot1vProtocolPortGroupVid_Type(Integer32):
    """Custom type fsDot1vProtocolPortGroupVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsDot1vProtocolPortGroupVid_Type.__name__ = "Integer32"
_FsDot1vProtocolPortGroupVid_Object = MibTableColumn
fsDot1vProtocolPortGroupVid = _FsDot1vProtocolPortGroupVid_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 5, 2, 1, 2),
    _FsDot1vProtocolPortGroupVid_Type()
)
fsDot1vProtocolPortGroupVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDot1vProtocolPortGroupVid.setStatus("current")
_FsDot1vProtocolPortRowStatus_Type = RowStatus
_FsDot1vProtocolPortRowStatus_Object = MibTableColumn
fsDot1vProtocolPortRowStatus = _FsDot1vProtocolPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 7, 1, 5, 2, 1, 3),
    _FsDot1vProtocolPortRowStatus_Type()
)
fsDot1vProtocolPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDot1vProtocolPortRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICROQ-BRIDGE-MIB",
    **{"VlanIndex": VlanIndex,
       "VlanId": VlanId,
       "fsQBridgeMIB": fsQBridgeMIB,
       "fsQBridgeMIBObjects": fsQBridgeMIBObjects,
       "fsDot1qBase": fsDot1qBase,
       "fsDot1qBaseTable": fsDot1qBaseTable,
       "fsDot1qBaseEntry": fsDot1qBaseEntry,
       "fsDot1qVlanContextId": fsDot1qVlanContextId,
       "fsDot1qVlanVersionNumber": fsDot1qVlanVersionNumber,
       "fsDot1qMaxVlanId": fsDot1qMaxVlanId,
       "fsDot1qMaxSupportedVlans": fsDot1qMaxSupportedVlans,
       "fsDot1qNumVlans": fsDot1qNumVlans,
       "fsDot1qGvrpStatus": fsDot1qGvrpStatus,
       "fsDot1qTp": fsDot1qTp,
       "fsDot1qFdbTable": fsDot1qFdbTable,
       "fsDot1qFdbEntry": fsDot1qFdbEntry,
       "fsDot1qFdbId": fsDot1qFdbId,
       "fsDot1qFdbDynamicCount": fsDot1qFdbDynamicCount,
       "fsDot1qTpFdbTable": fsDot1qTpFdbTable,
       "fsDot1qTpFdbEntry": fsDot1qTpFdbEntry,
       "fsDot1qTpFdbAddress": fsDot1qTpFdbAddress,
       "fsDot1qTpFdbPort": fsDot1qTpFdbPort,
       "fsDot1qTpFdbStatus": fsDot1qTpFdbStatus,
       "fsDot1qTpFdbPw": fsDot1qTpFdbPw,
       "fsDot1qTpGroupTable": fsDot1qTpGroupTable,
       "fsDot1qTpGroupEntry": fsDot1qTpGroupEntry,
       "fsDot1qVlanIndex": fsDot1qVlanIndex,
       "fsDot1qTpGroupAddress": fsDot1qTpGroupAddress,
       "fsDot1qTpPort": fsDot1qTpPort,
       "fsDot1qTpGroupIsLearnt": fsDot1qTpGroupIsLearnt,
       "fsDot1qForwardAllLearntPortTable": fsDot1qForwardAllLearntPortTable,
       "fsDot1qForwardAllLearntPortEntry": fsDot1qForwardAllLearntPortEntry,
       "fsDot1qForwardAllIsLearnt": fsDot1qForwardAllIsLearnt,
       "fsDot1qForwardAllStatusTable": fsDot1qForwardAllStatusTable,
       "fsDot1qForwardAllStatusEntry": fsDot1qForwardAllStatusEntry,
       "fsDot1qForwardAllRowStatus": fsDot1qForwardAllRowStatus,
       "fsDot1qForwardAllPortConfigTable": fsDot1qForwardAllPortConfigTable,
       "fsDot1qForwardAllPortConfigEntry": fsDot1qForwardAllPortConfigEntry,
       "fsDot1qForwardAllPort": fsDot1qForwardAllPort,
       "fsDot1qForwardUnregLearntPortTable": fsDot1qForwardUnregLearntPortTable,
       "fsDot1qForwardUnregLearntPortEntry": fsDot1qForwardUnregLearntPortEntry,
       "fsDot1qForwardUnregIsLearnt": fsDot1qForwardUnregIsLearnt,
       "fsDot1qForwardUnregStatusTable": fsDot1qForwardUnregStatusTable,
       "fsDot1qForwardUnregStatusEntry": fsDot1qForwardUnregStatusEntry,
       "fsDot1qForwardUnregRowStatus": fsDot1qForwardUnregRowStatus,
       "fsDot1qForwardUnregPortConfigTable": fsDot1qForwardUnregPortConfigTable,
       "fsDot1qForwardUnregPortConfigEntry": fsDot1qForwardUnregPortConfigEntry,
       "fsDot1qForwardUnregPort": fsDot1qForwardUnregPort,
       "fsDot1qStatic": fsDot1qStatic,
       "fsDot1qStaticUnicastTable": fsDot1qStaticUnicastTable,
       "fsDot1qStaticUnicastEntry": fsDot1qStaticUnicastEntry,
       "fsDot1qStaticUnicastAddress": fsDot1qStaticUnicastAddress,
       "fsDot1qStaticUnicastReceivePort": fsDot1qStaticUnicastReceivePort,
       "fsDot1qStaticUnicastRowStatus": fsDot1qStaticUnicastRowStatus,
       "fsDot1qStaticUnicastStatus": fsDot1qStaticUnicastStatus,
       "fsDot1qStaticAllowedToGoTable": fsDot1qStaticAllowedToGoTable,
       "fsDot1qStaticAllowedToGoEntry": fsDot1qStaticAllowedToGoEntry,
       "fsDot1qStaticAllowedIsMember": fsDot1qStaticAllowedIsMember,
       "fsDot1qStaticMulticastTable": fsDot1qStaticMulticastTable,
       "fsDot1qStaticMulticastEntry": fsDot1qStaticMulticastEntry,
       "fsDot1qStaticMulticastAddress": fsDot1qStaticMulticastAddress,
       "fsDot1qStaticMulticastReceivePort": fsDot1qStaticMulticastReceivePort,
       "fsDot1qStaticMulticastRowStatus": fsDot1qStaticMulticastRowStatus,
       "fsDot1qStaticMulticastStatus": fsDot1qStaticMulticastStatus,
       "fsDot1qStaticMcastPortTable": fsDot1qStaticMcastPortTable,
       "fsDot1qStaticMcastPortEntry": fsDot1qStaticMcastPortEntry,
       "fsDot1qStaticMcastPort": fsDot1qStaticMcastPort,
       "fsDot1qVlan": fsDot1qVlan,
       "fsDot1qVlanNumDeletesTable": fsDot1qVlanNumDeletesTable,
       "fsDot1qVlanNumDeletesEntry": fsDot1qVlanNumDeletesEntry,
       "fsDot1qVlanNumDeletes": fsDot1qVlanNumDeletes,
       "fsDot1qVlanCurrentTable": fsDot1qVlanCurrentTable,
       "fsDot1qVlanCurrentEntry": fsDot1qVlanCurrentEntry,
       "fsDot1qVlanTimeMark": fsDot1qVlanTimeMark,
       "fsDot1qVlanFdbId": fsDot1qVlanFdbId,
       "fsDot1qVlanStatus": fsDot1qVlanStatus,
       "fsDot1qVlanCreationTime": fsDot1qVlanCreationTime,
       "fsDot1qVlanEgressPortTable": fsDot1qVlanEgressPortTable,
       "fsDot1qVlanEgressPortEntry": fsDot1qVlanEgressPortEntry,
       "fsDot1qVlanCurrentEgressPort": fsDot1qVlanCurrentEgressPort,
       "fsDot1qVlanStaticTable": fsDot1qVlanStaticTable,
       "fsDot1qVlanStaticEntry": fsDot1qVlanStaticEntry,
       "fsDot1qVlanStaticName": fsDot1qVlanStaticName,
       "fsDot1qVlanStaticRowStatus": fsDot1qVlanStaticRowStatus,
       "fsDot1qVlanStaticPortConfigTable": fsDot1qVlanStaticPortConfigTable,
       "fsDot1qVlanStaticPortConfigEntry": fsDot1qVlanStaticPortConfigEntry,
       "fsDot1qVlanStaticPort": fsDot1qVlanStaticPort,
       "fsDot1qNextFreeLocalVlanIndexTable": fsDot1qNextFreeLocalVlanIndexTable,
       "fsDot1qNextFreeLocalVlanIndexEntry": fsDot1qNextFreeLocalVlanIndexEntry,
       "fsDot1qNextFreeLocalVlanIndex": fsDot1qNextFreeLocalVlanIndex,
       "fsDot1qPortVlanTable": fsDot1qPortVlanTable,
       "fsDot1qPortVlanEntry": fsDot1qPortVlanEntry,
       "fsDot1qPvid": fsDot1qPvid,
       "fsDot1qPortAcceptableFrameTypes": fsDot1qPortAcceptableFrameTypes,
       "fsDot1qPortIngressFiltering": fsDot1qPortIngressFiltering,
       "fsDot1qPortGvrpStatus": fsDot1qPortGvrpStatus,
       "fsDot1qPortGvrpFailedRegistrations": fsDot1qPortGvrpFailedRegistrations,
       "fsDot1qPortGvrpLastPduOrigin": fsDot1qPortGvrpLastPduOrigin,
       "fsDot1qPortRestrictedVlanRegistration": fsDot1qPortRestrictedVlanRegistration,
       "fsDot1qPortVlanStatisticsTable": fsDot1qPortVlanStatisticsTable,
       "fsDot1qPortVlanStatisticsEntry": fsDot1qPortVlanStatisticsEntry,
       "fsDot1qTpVlanPortInFrames": fsDot1qTpVlanPortInFrames,
       "fsDot1qTpVlanPortOutFrames": fsDot1qTpVlanPortOutFrames,
       "fsDot1qTpVlanPortInDiscards": fsDot1qTpVlanPortInDiscards,
       "fsDot1qTpVlanPortInOverflowFrames": fsDot1qTpVlanPortInOverflowFrames,
       "fsDot1qTpVlanPortOutOverflowFrames": fsDot1qTpVlanPortOutOverflowFrames,
       "fsDot1qTpVlanPortInOverflowDiscards": fsDot1qTpVlanPortInOverflowDiscards,
       "fsDot1qPortVlanHCStatisticsTable": fsDot1qPortVlanHCStatisticsTable,
       "fsDot1qPortVlanHCStatisticsEntry": fsDot1qPortVlanHCStatisticsEntry,
       "fsDot1qTpVlanPortHCInFrames": fsDot1qTpVlanPortHCInFrames,
       "fsDot1qTpVlanPortHCOutFrames": fsDot1qTpVlanPortHCOutFrames,
       "fsDot1qTpVlanPortHCInDiscards": fsDot1qTpVlanPortHCInDiscards,
       "fsDot1qLearningConstraintsTable": fsDot1qLearningConstraintsTable,
       "fsDot1qLearningConstraintsEntry": fsDot1qLearningConstraintsEntry,
       "fsDot1qConstraintVlan": fsDot1qConstraintVlan,
       "fsDot1qConstraintSet": fsDot1qConstraintSet,
       "fsDot1qConstraintType": fsDot1qConstraintType,
       "fsDot1qConstraintStatus": fsDot1qConstraintStatus,
       "fsDot1qConstraintDefaultTable": fsDot1qConstraintDefaultTable,
       "fsDot1qConstraintDefaultEntry": fsDot1qConstraintDefaultEntry,
       "fsDot1qConstraintSetDefault": fsDot1qConstraintSetDefault,
       "fsDot1qConstraintTypeDefault": fsDot1qConstraintTypeDefault,
       "fsDot1vProtocol": fsDot1vProtocol,
       "fsDot1vProtocolGroupTable": fsDot1vProtocolGroupTable,
       "fsDot1vProtocolGroupEntry": fsDot1vProtocolGroupEntry,
       "fsDot1vProtocolTemplateFrameType": fsDot1vProtocolTemplateFrameType,
       "fsDot1vProtocolTemplateProtocolValue": fsDot1vProtocolTemplateProtocolValue,
       "fsDot1vProtocolGroupId": fsDot1vProtocolGroupId,
       "fsDot1vProtocolGroupRowStatus": fsDot1vProtocolGroupRowStatus,
       "fsDot1vProtocolPortTable": fsDot1vProtocolPortTable,
       "fsDot1vProtocolPortEntry": fsDot1vProtocolPortEntry,
       "fsDot1vProtocolPortGroupId": fsDot1vProtocolPortGroupId,
       "fsDot1vProtocolPortGroupVid": fsDot1vProtocolPortGroupVid,
       "fsDot1vProtocolPortRowStatus": fsDot1vProtocolPortRowStatus}
)
