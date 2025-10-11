# SNMP MIB module (ELTEX-MES-ISS-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-ISS-VLAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:51:27 2025
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

(dot1qFutureVlanPortEntry,
 dot1qFutureVlanPortMacMapEntry) = mibBuilder.importSymbols(
    "ARICENT-VLAN-MIB",
    "dot1qFutureVlanPortEntry",
    "dot1qFutureVlanPortMacMapEntry")

(fsDot1qVlanContextId,) = mibBuilder.importSymbols(
    "ARICENTQ-BRIDGE-MIB",
    "fsDot1qVlanContextId")

(eltMesIss,) = mibBuilder.importSymbols(
    "ELTEX-MES-ISS-MIB",
    "eltMesIss")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(VlanIndex,
 dot1qVlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex",
    "dot1qVlanIndex")

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

eltMesIssVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3)
)
if mibBuilder.loadTexts:
    eltMesIssVlanMIB.setRevisions(
        ("2023-02-15 00:00",
         "2022-12-06 00:00",
         "2022-10-10 00:00",
         "2022-08-05 00:00",
         "2021-06-29 00:00",
         "2019-12-12 00:00",
         "2018-12-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EltMesIssPortSecurityMode(TextualConvention, Integer32):
    status = "current"
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
        *(("disabled", 1),
          ("dynamic", 2),
          ("secure-permanent", 3),
          ("secure-delete-on-reset", 4))
    )



# MIB Managed Objects in the order of their OIDs

_EltMesIssVlanObjects_ObjectIdentity = ObjectIdentity
eltMesIssVlanObjects = _EltMesIssVlanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1)
)
_EltMesIssVlanGlobals_ObjectIdentity = ObjectIdentity
eltMesIssVlanGlobals = _EltMesIssVlanGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 1)
)
_EltMesIssVlanFdbPortTable_Object = MibTable
eltMesIssVlanFdbPortTable = _EltMesIssVlanFdbPortTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    eltMesIssVlanFdbPortTable.setStatus("current")
_EltMesIssVlanFdbPortEntry_Object = MibTableRow
eltMesIssVlanFdbPortEntry = _EltMesIssVlanFdbPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 1, 1, 1)
)
eltMesIssVlanFdbPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ELTEX-MES-ISS-VLAN-MIB", "eltMesIssVlanFdbPortVlanId"),
    (0, "ELTEX-MES-ISS-VLAN-MIB", "eltMesIssVlanFdbPortMacAddress"),
)
if mibBuilder.loadTexts:
    eltMesIssVlanFdbPortEntry.setStatus("current")
_EltMesIssVlanFdbPortVlanId_Type = VlanIndex
_EltMesIssVlanFdbPortVlanId_Object = MibTableColumn
eltMesIssVlanFdbPortVlanId = _EltMesIssVlanFdbPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 1, 1, 1, 1),
    _EltMesIssVlanFdbPortVlanId_Type()
)
eltMesIssVlanFdbPortVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssVlanFdbPortVlanId.setStatus("current")
_EltMesIssVlanFdbPortMacAddress_Type = MacAddress
_EltMesIssVlanFdbPortMacAddress_Object = MibTableColumn
eltMesIssVlanFdbPortMacAddress = _EltMesIssVlanFdbPortMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 1, 1, 1, 2),
    _EltMesIssVlanFdbPortMacAddress_Type()
)
eltMesIssVlanFdbPortMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssVlanFdbPortMacAddress.setStatus("current")


class _EltMesIssVlanFdbPortEntryStatus_Type(Integer32):
    """Custom type eltMesIssVlanFdbPortEntryStatus based on Integer32"""
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


_EltMesIssVlanFdbPortEntryStatus_Type.__name__ = "Integer32"
_EltMesIssVlanFdbPortEntryStatus_Object = MibTableColumn
eltMesIssVlanFdbPortEntryStatus = _EltMesIssVlanFdbPortEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 1, 1, 1, 3),
    _EltMesIssVlanFdbPortEntryStatus_Type()
)
eltMesIssVlanFdbPortEntryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssVlanFdbPortEntryStatus.setStatus("current")


class _EltMesIssVoiceVlanGlobalVlanIndex_Type(VlanIndex):
    """Custom type eltMesIssVoiceVlanGlobalVlanIndex based on VlanIndex"""
    defaultValue = 0


_EltMesIssVoiceVlanGlobalVlanIndex_Type.__name__ = "VlanIndex"
_EltMesIssVoiceVlanGlobalVlanIndex_Object = MibScalar
eltMesIssVoiceVlanGlobalVlanIndex = _EltMesIssVoiceVlanGlobalVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 1, 2),
    _EltMesIssVoiceVlanGlobalVlanIndex_Type()
)
eltMesIssVoiceVlanGlobalVlanIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssVoiceVlanGlobalVlanIndex.setStatus("current")
_EltMesIssVlanPortConfig_ObjectIdentity = ObjectIdentity
eltMesIssVlanPortConfig = _EltMesIssVlanPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 2)
)
_EltMesIssVlanPortTable_Object = MibTable
eltMesIssVlanPortTable = _EltMesIssVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eltMesIssVlanPortTable.setStatus("current")
_EltMesIssVlanPortEntry_Object = MibTableRow
eltMesIssVlanPortEntry = _EltMesIssVlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    eltMesIssVlanPortEntry.setStatus("current")


class _EltMesIssVlanDot1qTunnelStatus_Type(TruthValue):
    """Custom type eltMesIssVlanDot1qTunnelStatus based on TruthValue"""
    defaultValue = 2


_EltMesIssVlanDot1qTunnelStatus_Type.__name__ = "TruthValue"
_EltMesIssVlanDot1qTunnelStatus_Object = MibTableColumn
eltMesIssVlanDot1qTunnelStatus = _EltMesIssVlanDot1qTunnelStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 2, 1, 1, 1),
    _EltMesIssVlanDot1qTunnelStatus_Type()
)
eltMesIssVlanDot1qTunnelStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssVlanDot1qTunnelStatus.setStatus("current")
_EltMesIssVlanPortSecurityMacLimit_Type = Unsigned32
_EltMesIssVlanPortSecurityMacLimit_Object = MibTableColumn
eltMesIssVlanPortSecurityMacLimit = _EltMesIssVlanPortSecurityMacLimit_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 2, 1, 1, 2),
    _EltMesIssVlanPortSecurityMacLimit_Type()
)
eltMesIssVlanPortSecurityMacLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssVlanPortSecurityMacLimit.setStatus("current")


class _EltMesIssVlanPortSecurityStatus_Type(TruthValue):
    """Custom type eltMesIssVlanPortSecurityStatus based on TruthValue"""
    defaultValue = 2


_EltMesIssVlanPortSecurityStatus_Type.__name__ = "TruthValue"
_EltMesIssVlanPortSecurityStatus_Object = MibTableColumn
eltMesIssVlanPortSecurityStatus = _EltMesIssVlanPortSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 2, 1, 1, 3),
    _EltMesIssVlanPortSecurityStatus_Type()
)
eltMesIssVlanPortSecurityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssVlanPortSecurityStatus.setStatus("current")
_EltMesIssVlanPortSecurityMode_Type = EltMesIssPortSecurityMode
_EltMesIssVlanPortSecurityMode_Object = MibTableColumn
eltMesIssVlanPortSecurityMode = _EltMesIssVlanPortSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 2, 1, 1, 4),
    _EltMesIssVlanPortSecurityMode_Type()
)
eltMesIssVlanPortSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssVlanPortSecurityMode.setStatus("current")


class _EltMesIssVlanPortDefaultVlanTagged_Type(TruthValue):
    """Custom type eltMesIssVlanPortDefaultVlanTagged based on TruthValue"""
    defaultValue = 2


_EltMesIssVlanPortDefaultVlanTagged_Type.__name__ = "TruthValue"
_EltMesIssVlanPortDefaultVlanTagged_Object = MibTableColumn
eltMesIssVlanPortDefaultVlanTagged = _EltMesIssVlanPortDefaultVlanTagged_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 2, 1, 1, 5),
    _EltMesIssVlanPortDefaultVlanTagged_Type()
)
eltMesIssVlanPortDefaultVlanTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssVlanPortDefaultVlanTagged.setStatus("current")


class _EltMesIssVlanPortMvrVlanId_Type(Unsigned32):
    """Custom type eltMesIssVlanPortMvrVlanId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_EltMesIssVlanPortMvrVlanId_Type.__name__ = "Unsigned32"
_EltMesIssVlanPortMvrVlanId_Object = MibTableColumn
eltMesIssVlanPortMvrVlanId = _EltMesIssVlanPortMvrVlanId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 2, 1, 1, 6),
    _EltMesIssVlanPortMvrVlanId_Type()
)
eltMesIssVlanPortMvrVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssVlanPortMvrVlanId.setStatus("current")


class _EltMesIssVlanPortMvrVlanTagged_Type(TruthValue):
    """Custom type eltMesIssVlanPortMvrVlanTagged based on TruthValue"""
    defaultValue = 2


_EltMesIssVlanPortMvrVlanTagged_Type.__name__ = "TruthValue"
_EltMesIssVlanPortMvrVlanTagged_Object = MibTableColumn
eltMesIssVlanPortMvrVlanTagged = _EltMesIssVlanPortMvrVlanTagged_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 2, 1, 1, 7),
    _EltMesIssVlanPortMvrVlanTagged_Type()
)
eltMesIssVlanPortMvrVlanTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssVlanPortMvrVlanTagged.setStatus("current")


class _EltMesIssVlanPortDefaultVlanForbidden_Type(TruthValue):
    """Custom type eltMesIssVlanPortDefaultVlanForbidden based on TruthValue"""
    defaultValue = 2


_EltMesIssVlanPortDefaultVlanForbidden_Type.__name__ = "TruthValue"
_EltMesIssVlanPortDefaultVlanForbidden_Object = MibTableColumn
eltMesIssVlanPortDefaultVlanForbidden = _EltMesIssVlanPortDefaultVlanForbidden_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 2, 1, 1, 8),
    _EltMesIssVlanPortDefaultVlanForbidden_Type()
)
eltMesIssVlanPortDefaultVlanForbidden.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssVlanPortDefaultVlanForbidden.setStatus("current")


class _EltMesIssVlanPortEgressFiltering_Type(TruthValue):
    """Custom type eltMesIssVlanPortEgressFiltering based on TruthValue"""
    defaultValue = 1


_EltMesIssVlanPortEgressFiltering_Type.__name__ = "TruthValue"
_EltMesIssVlanPortEgressFiltering_Object = MibTableColumn
eltMesIssVlanPortEgressFiltering = _EltMesIssVlanPortEgressFiltering_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 2, 1, 1, 9),
    _EltMesIssVlanPortEgressFiltering_Type()
)
eltMesIssVlanPortEgressFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssVlanPortEgressFiltering.setStatus("current")
_EltMesIssVlanPortMacMapTable_Object = MibTable
eltMesIssVlanPortMacMapTable = _EltMesIssVlanPortMacMapTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    eltMesIssVlanPortMacMapTable.setStatus("deprecated")
_EltMesIssVlanPortMacMapEntry_Object = MibTableRow
eltMesIssVlanPortMacMapEntry = _EltMesIssVlanPortMacMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    eltMesIssVlanPortMacMapEntry.setStatus("deprecated")
_EltMesIssVlanPortMacMapMask_Type = MacAddress
_EltMesIssVlanPortMacMapMask_Object = MibTableColumn
eltMesIssVlanPortMacMapMask = _EltMesIssVlanPortMacMapMask_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 2, 2, 1, 1),
    _EltMesIssVlanPortMacMapMask_Type()
)
eltMesIssVlanPortMacMapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssVlanPortMacMapMask.setStatus("deprecated")
_EltMesIssMacBasedVlanPortTable_Object = MibTable
eltMesIssMacBasedVlanPortTable = _EltMesIssMacBasedVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 2, 3)
)
if mibBuilder.loadTexts:
    eltMesIssMacBasedVlanPortTable.setStatus("current")
_EltMesIssMacBasedVlanPortEntry_Object = MibTableRow
eltMesIssMacBasedVlanPortEntry = _EltMesIssMacBasedVlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 2, 3, 1)
)
eltMesIssMacBasedVlanPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ELTEX-MES-ISS-VLAN-MIB", "eltMesIssMacBasedVlanPortGroupId"),
)
if mibBuilder.loadTexts:
    eltMesIssMacBasedVlanPortEntry.setStatus("current")


class _EltMesIssMacBasedVlanPortGroupId_Type(Integer32):
    """Custom type eltMesIssMacBasedVlanPortGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EltMesIssMacBasedVlanPortGroupId_Type.__name__ = "Integer32"
_EltMesIssMacBasedVlanPortGroupId_Object = MibTableColumn
eltMesIssMacBasedVlanPortGroupId = _EltMesIssMacBasedVlanPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 2, 3, 1, 1),
    _EltMesIssMacBasedVlanPortGroupId_Type()
)
eltMesIssMacBasedVlanPortGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssMacBasedVlanPortGroupId.setStatus("current")
_EltMesIssMacBasedVlanPortGroupVid_Type = VlanIndex
_EltMesIssMacBasedVlanPortGroupVid_Object = MibTableColumn
eltMesIssMacBasedVlanPortGroupVid = _EltMesIssMacBasedVlanPortGroupVid_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 2, 3, 1, 2),
    _EltMesIssMacBasedVlanPortGroupVid_Type()
)
eltMesIssMacBasedVlanPortGroupVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltMesIssMacBasedVlanPortGroupVid.setStatus("current")


class _EltMesIssMacBasedVlanPortMcastBcastOption_Type(Integer32):
    """Custom type eltMesIssMacBasedVlanPortMcastBcastOption based on Integer32"""
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
          ("suppress", 2))
    )


_EltMesIssMacBasedVlanPortMcastBcastOption_Type.__name__ = "Integer32"
_EltMesIssMacBasedVlanPortMcastBcastOption_Object = MibTableColumn
eltMesIssMacBasedVlanPortMcastBcastOption = _EltMesIssMacBasedVlanPortMcastBcastOption_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 2, 3, 1, 3),
    _EltMesIssMacBasedVlanPortMcastBcastOption_Type()
)
eltMesIssMacBasedVlanPortMcastBcastOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssMacBasedVlanPortMcastBcastOption.setStatus("current")
_EltMesIssMacBasedVlanPortRowStatus_Type = RowStatus
_EltMesIssMacBasedVlanPortRowStatus_Object = MibTableColumn
eltMesIssMacBasedVlanPortRowStatus = _EltMesIssMacBasedVlanPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 2, 3, 1, 4),
    _EltMesIssMacBasedVlanPortRowStatus_Type()
)
eltMesIssMacBasedVlanPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltMesIssMacBasedVlanPortRowStatus.setStatus("current")
_EltMesIssVoiceVlanPortTable_Object = MibTable
eltMesIssVoiceVlanPortTable = _EltMesIssVoiceVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 2, 4)
)
if mibBuilder.loadTexts:
    eltMesIssVoiceVlanPortTable.setStatus("current")
_EltMesIssVoiceVlanPortEntry_Object = MibTableRow
eltMesIssVoiceVlanPortEntry = _EltMesIssVoiceVlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 2, 4, 1)
)
eltMesIssVoiceVlanPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eltMesIssVoiceVlanPortEntry.setStatus("current")


class _EltMesIssVoiceVlanPortEnable_Type(TruthValue):
    """Custom type eltMesIssVoiceVlanPortEnable based on TruthValue"""
    defaultValue = 2


_EltMesIssVoiceVlanPortEnable_Type.__name__ = "TruthValue"
_EltMesIssVoiceVlanPortEnable_Object = MibTableColumn
eltMesIssVoiceVlanPortEnable = _EltMesIssVoiceVlanPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 2, 4, 1, 1),
    _EltMesIssVoiceVlanPortEnable_Type()
)
eltMesIssVoiceVlanPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssVoiceVlanPortEnable.setStatus("current")


class _EltMesIssVoiceVlanPortVlanIndex_Type(VlanIndex):
    """Custom type eltMesIssVoiceVlanPortVlanIndex based on VlanIndex"""
    defaultValue = 0


_EltMesIssVoiceVlanPortVlanIndex_Type.__name__ = "VlanIndex"
_EltMesIssVoiceVlanPortVlanIndex_Object = MibTableColumn
eltMesIssVoiceVlanPortVlanIndex = _EltMesIssVoiceVlanPortVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 2, 4, 1, 2),
    _EltMesIssVoiceVlanPortVlanIndex_Type()
)
eltMesIssVoiceVlanPortVlanIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssVoiceVlanPortVlanIndex.setStatus("current")


class _EltMesIssVoiceVlanPortAuthenticationBypass_Type(TruthValue):
    """Custom type eltMesIssVoiceVlanPortAuthenticationBypass based on TruthValue"""
    defaultValue = 2


_EltMesIssVoiceVlanPortAuthenticationBypass_Type.__name__ = "TruthValue"
_EltMesIssVoiceVlanPortAuthenticationBypass_Object = MibTableColumn
eltMesIssVoiceVlanPortAuthenticationBypass = _EltMesIssVoiceVlanPortAuthenticationBypass_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 2, 4, 1, 3),
    _EltMesIssVoiceVlanPortAuthenticationBypass_Type()
)
eltMesIssVoiceVlanPortAuthenticationBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssVoiceVlanPortAuthenticationBypass.setStatus("current")
_EltMesIssVlanConfig_ObjectIdentity = ObjectIdentity
eltMesIssVlanConfig = _EltMesIssVlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 3)
)
_EltMesIssDot1qVlanStaticTable_Object = MibTable
eltMesIssDot1qVlanStaticTable = _EltMesIssDot1qVlanStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    eltMesIssDot1qVlanStaticTable.setStatus("current")
_EltMesIssDot1qVlanStaticEntry_Object = MibTableRow
eltMesIssDot1qVlanStaticEntry = _EltMesIssDot1qVlanStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 3, 1, 1)
)
eltMesIssDot1qVlanStaticEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    eltMesIssDot1qVlanStaticEntry.setStatus("current")


class _EltMesIssDot1qVlanStaticCos_Type(Integer32):
    """Custom type eltMesIssDot1qVlanStaticCos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_EltMesIssDot1qVlanStaticCos_Type.__name__ = "Integer32"
_EltMesIssDot1qVlanStaticCos_Object = MibTableColumn
eltMesIssDot1qVlanStaticCos = _EltMesIssDot1qVlanStaticCos_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 3, 1, 1, 1),
    _EltMesIssDot1qVlanStaticCos_Type()
)
eltMesIssDot1qVlanStaticCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssDot1qVlanStaticCos.setStatus("current")
_EltMesIssMacBasedVlanGroupTable_Object = MibTable
eltMesIssMacBasedVlanGroupTable = _EltMesIssMacBasedVlanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    eltMesIssMacBasedVlanGroupTable.setStatus("current")
_EltMesIssMacBasedVlanGroupEntry_Object = MibTableRow
eltMesIssMacBasedVlanGroupEntry = _EltMesIssMacBasedVlanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 3, 2, 1)
)
eltMesIssMacBasedVlanGroupEntry.setIndexNames(
    (0, "ELTEX-MES-ISS-VLAN-MIB", "eltMesIssMacBasedVlanMacAddress"),
    (0, "ELTEX-MES-ISS-VLAN-MIB", "eltMesIssMacBasedVlanMacMask"),
)
if mibBuilder.loadTexts:
    eltMesIssMacBasedVlanGroupEntry.setStatus("current")
_EltMesIssMacBasedVlanMacAddress_Type = MacAddress
_EltMesIssMacBasedVlanMacAddress_Object = MibTableColumn
eltMesIssMacBasedVlanMacAddress = _EltMesIssMacBasedVlanMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 3, 2, 1, 1),
    _EltMesIssMacBasedVlanMacAddress_Type()
)
eltMesIssMacBasedVlanMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssMacBasedVlanMacAddress.setStatus("current")
_EltMesIssMacBasedVlanMacMask_Type = MacAddress
_EltMesIssMacBasedVlanMacMask_Object = MibTableColumn
eltMesIssMacBasedVlanMacMask = _EltMesIssMacBasedVlanMacMask_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 3, 2, 1, 2),
    _EltMesIssMacBasedVlanMacMask_Type()
)
eltMesIssMacBasedVlanMacMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssMacBasedVlanMacMask.setStatus("current")


class _EltMesIssMacBasedVlanGroupId_Type(Integer32):
    """Custom type eltMesIssMacBasedVlanGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EltMesIssMacBasedVlanGroupId_Type.__name__ = "Integer32"
_EltMesIssMacBasedVlanGroupId_Object = MibTableColumn
eltMesIssMacBasedVlanGroupId = _EltMesIssMacBasedVlanGroupId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 3, 2, 1, 3),
    _EltMesIssMacBasedVlanGroupId_Type()
)
eltMesIssMacBasedVlanGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltMesIssMacBasedVlanGroupId.setStatus("current")
_EltMesIssMacBasedVlanGroupRowStatus_Type = RowStatus
_EltMesIssMacBasedVlanGroupRowStatus_Object = MibTableColumn
eltMesIssMacBasedVlanGroupRowStatus = _EltMesIssMacBasedVlanGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 3, 2, 1, 4),
    _EltMesIssMacBasedVlanGroupRowStatus_Type()
)
eltMesIssMacBasedVlanGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltMesIssMacBasedVlanGroupRowStatus.setStatus("current")
_EltMesIssVoiceVlanOUITable_Object = MibTable
eltMesIssVoiceVlanOUITable = _EltMesIssVoiceVlanOUITable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 3, 3)
)
if mibBuilder.loadTexts:
    eltMesIssVoiceVlanOUITable.setStatus("current")
_EltMesIssVoiceVlanOUIEntry_Object = MibTableRow
eltMesIssVoiceVlanOUIEntry = _EltMesIssVoiceVlanOUIEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 3, 3, 1)
)
eltMesIssVoiceVlanOUIEntry.setIndexNames(
    (0, "ELTEX-MES-ISS-VLAN-MIB", "eltMesIssVoiceVlanOUIPrefix"),
)
if mibBuilder.loadTexts:
    eltMesIssVoiceVlanOUIEntry.setStatus("current")


class _EltMesIssVoiceVlanOUIPrefix_Type(OctetString):
    """Custom type eltMesIssVoiceVlanOUIPrefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_EltMesIssVoiceVlanOUIPrefix_Type.__name__ = "OctetString"
_EltMesIssVoiceVlanOUIPrefix_Object = MibTableColumn
eltMesIssVoiceVlanOUIPrefix = _EltMesIssVoiceVlanOUIPrefix_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 3, 3, 1, 1),
    _EltMesIssVoiceVlanOUIPrefix_Type()
)
eltMesIssVoiceVlanOUIPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssVoiceVlanOUIPrefix.setStatus("current")


class _EltMesIssVoiceVlanOUIDescription_Type(DisplayString):
    """Custom type eltMesIssVoiceVlanOUIDescription based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EltMesIssVoiceVlanOUIDescription_Type.__name__ = "DisplayString"
_EltMesIssVoiceVlanOUIDescription_Object = MibTableColumn
eltMesIssVoiceVlanOUIDescription = _EltMesIssVoiceVlanOUIDescription_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 3, 3, 1, 2),
    _EltMesIssVoiceVlanOUIDescription_Type()
)
eltMesIssVoiceVlanOUIDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssVoiceVlanOUIDescription.setStatus("current")
_EltMesIssVoiceVlanOUIEntryRowStatus_Type = RowStatus
_EltMesIssVoiceVlanOUIEntryRowStatus_Object = MibTableColumn
eltMesIssVoiceVlanOUIEntryRowStatus = _EltMesIssVoiceVlanOUIEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 3, 3, 1, 3),
    _EltMesIssVoiceVlanOUIEntryRowStatus_Type()
)
eltMesIssVoiceVlanOUIEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltMesIssVoiceVlanOUIEntryRowStatus.setStatus("current")
_EltMesIssVlanStatistics_ObjectIdentity = ObjectIdentity
eltMesIssVlanStatistics = _EltMesIssVlanStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 4)
)
_EltMesIssVlanCurrentTable_Object = MibTable
eltMesIssVlanCurrentTable = _EltMesIssVlanCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    eltMesIssVlanCurrentTable.setStatus("current")
_EltMesIssVlanCurrentEntry_Object = MibTableRow
eltMesIssVlanCurrentEntry = _EltMesIssVlanCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 4, 1, 1)
)
eltMesIssVlanCurrentEntry.setIndexNames(
    (0, "ARICENTQ-BRIDGE-MIB", "fsDot1qVlanContextId"),
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    eltMesIssVlanCurrentEntry.setStatus("current")
_EltMesIssVlanFdbId_Type = Unsigned32
_EltMesIssVlanFdbId_Object = MibTableColumn
eltMesIssVlanFdbId = _EltMesIssVlanFdbId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 4, 1, 1, 1),
    _EltMesIssVlanFdbId_Type()
)
eltMesIssVlanFdbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssVlanFdbId.setStatus("current")


class _EltMesIssVlanStatus_Type(Integer32):
    """Custom type eltMesIssVlanStatus based on Integer32"""
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


_EltMesIssVlanStatus_Type.__name__ = "Integer32"
_EltMesIssVlanStatus_Object = MibTableColumn
eltMesIssVlanStatus = _EltMesIssVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 4, 1, 1, 2),
    _EltMesIssVlanStatus_Type()
)
eltMesIssVlanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssVlanStatus.setStatus("current")
_EltMesIssVlanCreationTime_Type = TimeTicks
_EltMesIssVlanCreationTime_Object = MibTableColumn
eltMesIssVlanCreationTime = _EltMesIssVlanCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 4, 1, 1, 3),
    _EltMesIssVlanCreationTime_Type()
)
eltMesIssVlanCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssVlanCreationTime.setStatus("current")
_EltMesIssPortSecViolationObjects_ObjectIdentity = ObjectIdentity
eltMesIssPortSecViolationObjects = _EltMesIssPortSecViolationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 5)
)
_EltMesIssPortSecLastViolationAddress_Type = MacAddress
_EltMesIssPortSecLastViolationAddress_Object = MibScalar
eltMesIssPortSecLastViolationAddress = _EltMesIssPortSecLastViolationAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 5, 1),
    _EltMesIssPortSecLastViolationAddress_Type()
)
eltMesIssPortSecLastViolationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssPortSecLastViolationAddress.setStatus("current")
_EltMesIssPortSecViolationNotifications_ObjectIdentity = ObjectIdentity
eltMesIssPortSecViolationNotifications = _EltMesIssPortSecViolationNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 6)
)
_EltMesIssPortSecViolationNotificationsPrefix_ObjectIdentity = ObjectIdentity
eltMesIssPortSecViolationNotificationsPrefix = _EltMesIssPortSecViolationNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 6, 0)
)
dot1qFutureVlanPortEntry.registerAugmentions(
    ("ELTEX-MES-ISS-VLAN-MIB",
     "eltMesIssVlanPortEntry")
)
eltMesIssVlanPortEntry.setIndexNames(*dot1qFutureVlanPortEntry.getIndexNames())
dot1qFutureVlanPortMacMapEntry.registerAugmentions(
    ("ELTEX-MES-ISS-VLAN-MIB",
     "eltMesIssVlanPortMacMapEntry")
)
eltMesIssVlanPortMacMapEntry.setIndexNames(*dot1qFutureVlanPortMacMapEntry.getIndexNames())

# Managed Objects groups


# Notification objects

eltMesIssVlanLastMacConstraintTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3, 1, 6, 0, 1)
)
eltMesIssVlanLastMacConstraintTrap.setObjects(
      *(("ELTEX-MES-ISS-VLAN-MIB", "eltMesIssPortSecLastViolationAddress"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    eltMesIssVlanLastMacConstraintTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-ISS-VLAN-MIB",
    **{"EltMesIssPortSecurityMode": EltMesIssPortSecurityMode,
       "eltMesIssVlanMIB": eltMesIssVlanMIB,
       "eltMesIssVlanObjects": eltMesIssVlanObjects,
       "eltMesIssVlanGlobals": eltMesIssVlanGlobals,
       "eltMesIssVlanFdbPortTable": eltMesIssVlanFdbPortTable,
       "eltMesIssVlanFdbPortEntry": eltMesIssVlanFdbPortEntry,
       "eltMesIssVlanFdbPortVlanId": eltMesIssVlanFdbPortVlanId,
       "eltMesIssVlanFdbPortMacAddress": eltMesIssVlanFdbPortMacAddress,
       "eltMesIssVlanFdbPortEntryStatus": eltMesIssVlanFdbPortEntryStatus,
       "eltMesIssVoiceVlanGlobalVlanIndex": eltMesIssVoiceVlanGlobalVlanIndex,
       "eltMesIssVlanPortConfig": eltMesIssVlanPortConfig,
       "eltMesIssVlanPortTable": eltMesIssVlanPortTable,
       "eltMesIssVlanPortEntry": eltMesIssVlanPortEntry,
       "eltMesIssVlanDot1qTunnelStatus": eltMesIssVlanDot1qTunnelStatus,
       "eltMesIssVlanPortSecurityMacLimit": eltMesIssVlanPortSecurityMacLimit,
       "eltMesIssVlanPortSecurityStatus": eltMesIssVlanPortSecurityStatus,
       "eltMesIssVlanPortSecurityMode": eltMesIssVlanPortSecurityMode,
       "eltMesIssVlanPortDefaultVlanTagged": eltMesIssVlanPortDefaultVlanTagged,
       "eltMesIssVlanPortMvrVlanId": eltMesIssVlanPortMvrVlanId,
       "eltMesIssVlanPortMvrVlanTagged": eltMesIssVlanPortMvrVlanTagged,
       "eltMesIssVlanPortDefaultVlanForbidden": eltMesIssVlanPortDefaultVlanForbidden,
       "eltMesIssVlanPortEgressFiltering": eltMesIssVlanPortEgressFiltering,
       "eltMesIssVlanPortMacMapTable": eltMesIssVlanPortMacMapTable,
       "eltMesIssVlanPortMacMapEntry": eltMesIssVlanPortMacMapEntry,
       "eltMesIssVlanPortMacMapMask": eltMesIssVlanPortMacMapMask,
       "eltMesIssMacBasedVlanPortTable": eltMesIssMacBasedVlanPortTable,
       "eltMesIssMacBasedVlanPortEntry": eltMesIssMacBasedVlanPortEntry,
       "eltMesIssMacBasedVlanPortGroupId": eltMesIssMacBasedVlanPortGroupId,
       "eltMesIssMacBasedVlanPortGroupVid": eltMesIssMacBasedVlanPortGroupVid,
       "eltMesIssMacBasedVlanPortMcastBcastOption": eltMesIssMacBasedVlanPortMcastBcastOption,
       "eltMesIssMacBasedVlanPortRowStatus": eltMesIssMacBasedVlanPortRowStatus,
       "eltMesIssVoiceVlanPortTable": eltMesIssVoiceVlanPortTable,
       "eltMesIssVoiceVlanPortEntry": eltMesIssVoiceVlanPortEntry,
       "eltMesIssVoiceVlanPortEnable": eltMesIssVoiceVlanPortEnable,
       "eltMesIssVoiceVlanPortVlanIndex": eltMesIssVoiceVlanPortVlanIndex,
       "eltMesIssVoiceVlanPortAuthenticationBypass": eltMesIssVoiceVlanPortAuthenticationBypass,
       "eltMesIssVlanConfig": eltMesIssVlanConfig,
       "eltMesIssDot1qVlanStaticTable": eltMesIssDot1qVlanStaticTable,
       "eltMesIssDot1qVlanStaticEntry": eltMesIssDot1qVlanStaticEntry,
       "eltMesIssDot1qVlanStaticCos": eltMesIssDot1qVlanStaticCos,
       "eltMesIssMacBasedVlanGroupTable": eltMesIssMacBasedVlanGroupTable,
       "eltMesIssMacBasedVlanGroupEntry": eltMesIssMacBasedVlanGroupEntry,
       "eltMesIssMacBasedVlanMacAddress": eltMesIssMacBasedVlanMacAddress,
       "eltMesIssMacBasedVlanMacMask": eltMesIssMacBasedVlanMacMask,
       "eltMesIssMacBasedVlanGroupId": eltMesIssMacBasedVlanGroupId,
       "eltMesIssMacBasedVlanGroupRowStatus": eltMesIssMacBasedVlanGroupRowStatus,
       "eltMesIssVoiceVlanOUITable": eltMesIssVoiceVlanOUITable,
       "eltMesIssVoiceVlanOUIEntry": eltMesIssVoiceVlanOUIEntry,
       "eltMesIssVoiceVlanOUIPrefix": eltMesIssVoiceVlanOUIPrefix,
       "eltMesIssVoiceVlanOUIDescription": eltMesIssVoiceVlanOUIDescription,
       "eltMesIssVoiceVlanOUIEntryRowStatus": eltMesIssVoiceVlanOUIEntryRowStatus,
       "eltMesIssVlanStatistics": eltMesIssVlanStatistics,
       "eltMesIssVlanCurrentTable": eltMesIssVlanCurrentTable,
       "eltMesIssVlanCurrentEntry": eltMesIssVlanCurrentEntry,
       "eltMesIssVlanFdbId": eltMesIssVlanFdbId,
       "eltMesIssVlanStatus": eltMesIssVlanStatus,
       "eltMesIssVlanCreationTime": eltMesIssVlanCreationTime,
       "eltMesIssPortSecViolationObjects": eltMesIssPortSecViolationObjects,
       "eltMesIssPortSecLastViolationAddress": eltMesIssPortSecLastViolationAddress,
       "eltMesIssPortSecViolationNotifications": eltMesIssPortSecViolationNotifications,
       "eltMesIssPortSecViolationNotificationsPrefix": eltMesIssPortSecViolationNotificationsPrefix,
       "eltMesIssVlanLastMacConstraintTrap": eltMesIssVlanLastMacConstraintTrap}
)
