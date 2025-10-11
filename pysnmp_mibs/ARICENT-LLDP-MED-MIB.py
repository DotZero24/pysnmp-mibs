# SNMP MIB module (ARICENT-LLDP-MED-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-LLDP-MED-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:43:44 2025
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

(LldpXMedCapabilities,
 LldpXMedDeviceClass,
 LocationSubtype,
 PolicyAppType,
 lldpXMedLocLocationEntry,
 lldpXMedRemLocationSubtype) = mibBuilder.importSymbols(
    "LLDP-EXT-MED-MIB",
    "LldpXMedCapabilities",
    "LldpXMedDeviceClass",
    "LocationSubtype",
    "PolicyAppType",
    "lldpXMedLocLocationEntry",
    "lldpXMedRemLocationSubtype")

(LldpChassisId,
 lldpRemChassisId,
 lldpRemPortId) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "LldpChassisId",
    "lldpRemChassisId",
    "lldpRemPortId")

(lldpV2LocPortIfIndex,
 lldpV2PortConfigEntry,
 lldpV2RemIndex,
 lldpV2RemLocalDestMACAddress,
 lldpV2RemLocalIfIndex,
 lldpV2RemTimeMark) = mibBuilder.importSymbols(
    "LLDP-V2-MIB",
    "lldpV2LocPortIfIndex",
    "lldpV2PortConfigEntry",
    "lldpV2RemIndex",
    "lldpV2RemLocalDestMACAddress",
    "lldpV2RemLocalIfIndex",
    "lldpV2RemTimeMark")

(LldpV2ChassisId,
 LldpV2ChassisIdSubtype,
 LldpV2DestAddressTableIndex,
 LldpV2PortId) = mibBuilder.importSymbols(
    "LLDP-V2-TC-MIB",
    "LldpV2ChassisId",
    "LldpV2ChassisIdSubtype",
    "LldpV2DestAddressTableIndex",
    "LldpV2PortId")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsLldpMed = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101)
)
if mibBuilder.loadTexts:
    fsLldpMed.setRevisions(
        ("2015-06-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsLldpMedLocalConfig_ObjectIdentity = ObjectIdentity
fsLldpMedLocalConfig = _FsLldpMedLocalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 1)
)
_FsLldpMedPortConfigTable_Object = MibTable
fsLldpMedPortConfigTable = _FsLldpMedPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 1, 1)
)
if mibBuilder.loadTexts:
    fsLldpMedPortConfigTable.setStatus("current")
_FsLldpMedPortConfigEntry_Object = MibTableRow
fsLldpMedPortConfigEntry = _FsLldpMedPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fsLldpMedPortConfigEntry.setStatus("current")
_FsLldpMedPortCapSupported_Type = LldpXMedCapabilities
_FsLldpMedPortCapSupported_Object = MibTableColumn
fsLldpMedPortCapSupported = _FsLldpMedPortCapSupported_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 1, 1, 1, 1),
    _FsLldpMedPortCapSupported_Type()
)
fsLldpMedPortCapSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpMedPortCapSupported.setStatus("current")
_FsLldpMedPortConfigTLVsTxEnable_Type = LldpXMedCapabilities
_FsLldpMedPortConfigTLVsTxEnable_Object = MibTableColumn
fsLldpMedPortConfigTLVsTxEnable = _FsLldpMedPortConfigTLVsTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 1, 1, 1, 2),
    _FsLldpMedPortConfigTLVsTxEnable_Type()
)
fsLldpMedPortConfigTLVsTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLldpMedPortConfigTLVsTxEnable.setStatus("current")
_FsLldpMedLocMediaPolicyTable_Object = MibTable
fsLldpMedLocMediaPolicyTable = _FsLldpMedLocMediaPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 1, 2)
)
if mibBuilder.loadTexts:
    fsLldpMedLocMediaPolicyTable.setStatus("current")
_FsLldpMedLocMediaPolicyEntry_Object = MibTableRow
fsLldpMedLocMediaPolicyEntry = _FsLldpMedLocMediaPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 1, 2, 1)
)
fsLldpMedLocMediaPolicyEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
    (0, "ARICENT-LLDP-MED-MIB", "fsLldpMedLocMediaPolicyAppType"),
)
if mibBuilder.loadTexts:
    fsLldpMedLocMediaPolicyEntry.setStatus("current")
_FsLldpMedLocMediaPolicyAppType_Type = PolicyAppType
_FsLldpMedLocMediaPolicyAppType_Object = MibTableColumn
fsLldpMedLocMediaPolicyAppType = _FsLldpMedLocMediaPolicyAppType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 1, 2, 1, 1),
    _FsLldpMedLocMediaPolicyAppType_Type()
)
fsLldpMedLocMediaPolicyAppType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsLldpMedLocMediaPolicyAppType.setStatus("current")


class _FsLldpMedLocMediaPolicyVlanID_Type(Integer32):
    """Custom type fsLldpMedLocMediaPolicyVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(4095, 4095),
    )


_FsLldpMedLocMediaPolicyVlanID_Type.__name__ = "Integer32"
_FsLldpMedLocMediaPolicyVlanID_Object = MibTableColumn
fsLldpMedLocMediaPolicyVlanID = _FsLldpMedLocMediaPolicyVlanID_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 1, 2, 1, 2),
    _FsLldpMedLocMediaPolicyVlanID_Type()
)
fsLldpMedLocMediaPolicyVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLldpMedLocMediaPolicyVlanID.setStatus("current")


class _FsLldpMedLocMediaPolicyPriority_Type(Integer32):
    """Custom type fsLldpMedLocMediaPolicyPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsLldpMedLocMediaPolicyPriority_Type.__name__ = "Integer32"
_FsLldpMedLocMediaPolicyPriority_Object = MibTableColumn
fsLldpMedLocMediaPolicyPriority = _FsLldpMedLocMediaPolicyPriority_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 1, 2, 1, 3),
    _FsLldpMedLocMediaPolicyPriority_Type()
)
fsLldpMedLocMediaPolicyPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLldpMedLocMediaPolicyPriority.setStatus("current")


class _FsLldpMedLocMediaPolicyDscp_Type(Integer32):
    """Custom type fsLldpMedLocMediaPolicyDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_FsLldpMedLocMediaPolicyDscp_Type.__name__ = "Integer32"
_FsLldpMedLocMediaPolicyDscp_Object = MibTableColumn
fsLldpMedLocMediaPolicyDscp = _FsLldpMedLocMediaPolicyDscp_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 1, 2, 1, 4),
    _FsLldpMedLocMediaPolicyDscp_Type()
)
fsLldpMedLocMediaPolicyDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLldpMedLocMediaPolicyDscp.setStatus("current")
_FsLldpMedLocMediaPolicyUnknown_Type = TruthValue
_FsLldpMedLocMediaPolicyUnknown_Object = MibTableColumn
fsLldpMedLocMediaPolicyUnknown = _FsLldpMedLocMediaPolicyUnknown_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 1, 2, 1, 5),
    _FsLldpMedLocMediaPolicyUnknown_Type()
)
fsLldpMedLocMediaPolicyUnknown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLldpMedLocMediaPolicyUnknown.setStatus("current")
_FsLldpMedLocMediaPolicyTagged_Type = TruthValue
_FsLldpMedLocMediaPolicyTagged_Object = MibTableColumn
fsLldpMedLocMediaPolicyTagged = _FsLldpMedLocMediaPolicyTagged_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 1, 2, 1, 6),
    _FsLldpMedLocMediaPolicyTagged_Type()
)
fsLldpMedLocMediaPolicyTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLldpMedLocMediaPolicyTagged.setStatus("current")
_FsLldpMedLocMediaPolicyRowStatus_Type = RowStatus
_FsLldpMedLocMediaPolicyRowStatus_Object = MibTableColumn
fsLldpMedLocMediaPolicyRowStatus = _FsLldpMedLocMediaPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 1, 2, 1, 7),
    _FsLldpMedLocMediaPolicyRowStatus_Type()
)
fsLldpMedLocMediaPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsLldpMedLocMediaPolicyRowStatus.setStatus("current")
_FsLldpMedLocLocationTable_Object = MibTable
fsLldpMedLocLocationTable = _FsLldpMedLocLocationTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 1, 3)
)
if mibBuilder.loadTexts:
    fsLldpMedLocLocationTable.setStatus("current")
_FsLldpMedLocLocationEntry_Object = MibTableRow
fsLldpMedLocLocationEntry = _FsLldpMedLocLocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 1, 3, 1)
)
if mibBuilder.loadTexts:
    fsLldpMedLocLocationEntry.setStatus("current")
_FsLldpMedLocLocationRowStatus_Type = RowStatus
_FsLldpMedLocLocationRowStatus_Object = MibTableColumn
fsLldpMedLocLocationRowStatus = _FsLldpMedLocLocationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 1, 3, 1, 1),
    _FsLldpMedLocLocationRowStatus_Type()
)
fsLldpMedLocLocationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsLldpMedLocLocationRowStatus.setStatus("current")
_FsLldpMedRemoteConfig_ObjectIdentity = ObjectIdentity
fsLldpMedRemoteConfig = _FsLldpMedRemoteConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 2)
)
_FsLldpXMedRemCapabilitiesTable_Object = MibTable
fsLldpXMedRemCapabilitiesTable = _FsLldpXMedRemCapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 2, 1)
)
if mibBuilder.loadTexts:
    fsLldpXMedRemCapabilitiesTable.setStatus("current")
_FsLldpXMedRemCapabilitiesEntry_Object = MibTableRow
fsLldpXMedRemCapabilitiesEntry = _FsLldpXMedRemCapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 2, 1, 1)
)
fsLldpXMedRemCapabilitiesEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
)
if mibBuilder.loadTexts:
    fsLldpXMedRemCapabilitiesEntry.setStatus("current")
_FsLldpXMedRemCapSupported_Type = LldpXMedCapabilities
_FsLldpXMedRemCapSupported_Object = MibTableColumn
fsLldpXMedRemCapSupported = _FsLldpXMedRemCapSupported_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 2, 1, 1, 1),
    _FsLldpXMedRemCapSupported_Type()
)
fsLldpXMedRemCapSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpXMedRemCapSupported.setStatus("current")
_FsLldpXMedRemCapCurrent_Type = LldpXMedCapabilities
_FsLldpXMedRemCapCurrent_Object = MibTableColumn
fsLldpXMedRemCapCurrent = _FsLldpXMedRemCapCurrent_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 2, 1, 1, 2),
    _FsLldpXMedRemCapCurrent_Type()
)
fsLldpXMedRemCapCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpXMedRemCapCurrent.setStatus("current")
_FsLldpXMedRemDeviceClass_Type = LldpXMedDeviceClass
_FsLldpXMedRemDeviceClass_Object = MibTableColumn
fsLldpXMedRemDeviceClass = _FsLldpXMedRemDeviceClass_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 2, 1, 1, 3),
    _FsLldpXMedRemDeviceClass_Type()
)
fsLldpXMedRemDeviceClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpXMedRemDeviceClass.setStatus("current")
_FsLldpXMedRemMediaPolicyTable_Object = MibTable
fsLldpXMedRemMediaPolicyTable = _FsLldpXMedRemMediaPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 2, 2)
)
if mibBuilder.loadTexts:
    fsLldpXMedRemMediaPolicyTable.setStatus("current")
_FsLldpXMedRemMediaPolicyEntry_Object = MibTableRow
fsLldpXMedRemMediaPolicyEntry = _FsLldpXMedRemMediaPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 2, 2, 1)
)
fsLldpXMedRemMediaPolicyEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
    (0, "ARICENT-LLDP-MED-MIB", "fsLldpXMedRemMediaPolicyAppType"),
)
if mibBuilder.loadTexts:
    fsLldpXMedRemMediaPolicyEntry.setStatus("current")
_FsLldpXMedRemMediaPolicyAppType_Type = PolicyAppType
_FsLldpXMedRemMediaPolicyAppType_Object = MibTableColumn
fsLldpXMedRemMediaPolicyAppType = _FsLldpXMedRemMediaPolicyAppType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 2, 2, 1, 1),
    _FsLldpXMedRemMediaPolicyAppType_Type()
)
fsLldpXMedRemMediaPolicyAppType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsLldpXMedRemMediaPolicyAppType.setStatus("current")


class _FsLldpXMedRemMediaPolicyVlanID_Type(Integer32):
    """Custom type fsLldpXMedRemMediaPolicyVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(4095, 4095),
    )


_FsLldpXMedRemMediaPolicyVlanID_Type.__name__ = "Integer32"
_FsLldpXMedRemMediaPolicyVlanID_Object = MibTableColumn
fsLldpXMedRemMediaPolicyVlanID = _FsLldpXMedRemMediaPolicyVlanID_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 2, 2, 1, 2),
    _FsLldpXMedRemMediaPolicyVlanID_Type()
)
fsLldpXMedRemMediaPolicyVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpXMedRemMediaPolicyVlanID.setStatus("current")


class _FsLldpXMedRemMediaPolicyPriority_Type(Integer32):
    """Custom type fsLldpXMedRemMediaPolicyPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsLldpXMedRemMediaPolicyPriority_Type.__name__ = "Integer32"
_FsLldpXMedRemMediaPolicyPriority_Object = MibTableColumn
fsLldpXMedRemMediaPolicyPriority = _FsLldpXMedRemMediaPolicyPriority_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 2, 2, 1, 3),
    _FsLldpXMedRemMediaPolicyPriority_Type()
)
fsLldpXMedRemMediaPolicyPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpXMedRemMediaPolicyPriority.setStatus("current")


class _FsLldpXMedRemMediaPolicyDscp_Type(Integer32):
    """Custom type fsLldpXMedRemMediaPolicyDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_FsLldpXMedRemMediaPolicyDscp_Type.__name__ = "Integer32"
_FsLldpXMedRemMediaPolicyDscp_Object = MibTableColumn
fsLldpXMedRemMediaPolicyDscp = _FsLldpXMedRemMediaPolicyDscp_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 2, 2, 1, 4),
    _FsLldpXMedRemMediaPolicyDscp_Type()
)
fsLldpXMedRemMediaPolicyDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpXMedRemMediaPolicyDscp.setStatus("current")
_FsLldpXMedRemMediaPolicyUnknown_Type = TruthValue
_FsLldpXMedRemMediaPolicyUnknown_Object = MibTableColumn
fsLldpXMedRemMediaPolicyUnknown = _FsLldpXMedRemMediaPolicyUnknown_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 2, 2, 1, 5),
    _FsLldpXMedRemMediaPolicyUnknown_Type()
)
fsLldpXMedRemMediaPolicyUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpXMedRemMediaPolicyUnknown.setStatus("current")
_FsLldpXMedRemMediaPolicyTagged_Type = TruthValue
_FsLldpXMedRemMediaPolicyTagged_Object = MibTableColumn
fsLldpXMedRemMediaPolicyTagged = _FsLldpXMedRemMediaPolicyTagged_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 2, 2, 1, 6),
    _FsLldpXMedRemMediaPolicyTagged_Type()
)
fsLldpXMedRemMediaPolicyTagged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpXMedRemMediaPolicyTagged.setStatus("current")
_FsLldpXMedRemInventoryTable_Object = MibTable
fsLldpXMedRemInventoryTable = _FsLldpXMedRemInventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 2, 3)
)
if mibBuilder.loadTexts:
    fsLldpXMedRemInventoryTable.setStatus("current")
_FsLldpXMedRemInventoryEntry_Object = MibTableRow
fsLldpXMedRemInventoryEntry = _FsLldpXMedRemInventoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 2, 3, 1)
)
fsLldpXMedRemInventoryEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
)
if mibBuilder.loadTexts:
    fsLldpXMedRemInventoryEntry.setStatus("current")


class _FsLldpXMedRemHardwareRev_Type(SnmpAdminString):
    """Custom type fsLldpXMedRemHardwareRev based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsLldpXMedRemHardwareRev_Type.__name__ = "SnmpAdminString"
_FsLldpXMedRemHardwareRev_Object = MibTableColumn
fsLldpXMedRemHardwareRev = _FsLldpXMedRemHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 2, 3, 1, 1),
    _FsLldpXMedRemHardwareRev_Type()
)
fsLldpXMedRemHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpXMedRemHardwareRev.setStatus("current")


class _FsLldpXMedRemFirmwareRev_Type(SnmpAdminString):
    """Custom type fsLldpXMedRemFirmwareRev based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsLldpXMedRemFirmwareRev_Type.__name__ = "SnmpAdminString"
_FsLldpXMedRemFirmwareRev_Object = MibTableColumn
fsLldpXMedRemFirmwareRev = _FsLldpXMedRemFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 2, 3, 1, 2),
    _FsLldpXMedRemFirmwareRev_Type()
)
fsLldpXMedRemFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpXMedRemFirmwareRev.setStatus("current")


class _FsLldpXMedRemSoftwareRev_Type(SnmpAdminString):
    """Custom type fsLldpXMedRemSoftwareRev based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsLldpXMedRemSoftwareRev_Type.__name__ = "SnmpAdminString"
_FsLldpXMedRemSoftwareRev_Object = MibTableColumn
fsLldpXMedRemSoftwareRev = _FsLldpXMedRemSoftwareRev_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 2, 3, 1, 3),
    _FsLldpXMedRemSoftwareRev_Type()
)
fsLldpXMedRemSoftwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpXMedRemSoftwareRev.setStatus("current")


class _FsLldpXMedRemSerialNum_Type(SnmpAdminString):
    """Custom type fsLldpXMedRemSerialNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsLldpXMedRemSerialNum_Type.__name__ = "SnmpAdminString"
_FsLldpXMedRemSerialNum_Object = MibTableColumn
fsLldpXMedRemSerialNum = _FsLldpXMedRemSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 2, 3, 1, 4),
    _FsLldpXMedRemSerialNum_Type()
)
fsLldpXMedRemSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpXMedRemSerialNum.setStatus("current")


class _FsLldpXMedRemMfgName_Type(SnmpAdminString):
    """Custom type fsLldpXMedRemMfgName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsLldpXMedRemMfgName_Type.__name__ = "SnmpAdminString"
_FsLldpXMedRemMfgName_Object = MibTableColumn
fsLldpXMedRemMfgName = _FsLldpXMedRemMfgName_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 2, 3, 1, 5),
    _FsLldpXMedRemMfgName_Type()
)
fsLldpXMedRemMfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpXMedRemMfgName.setStatus("current")


class _FsLldpXMedRemModelName_Type(SnmpAdminString):
    """Custom type fsLldpXMedRemModelName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsLldpXMedRemModelName_Type.__name__ = "SnmpAdminString"
_FsLldpXMedRemModelName_Object = MibTableColumn
fsLldpXMedRemModelName = _FsLldpXMedRemModelName_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 2, 3, 1, 6),
    _FsLldpXMedRemModelName_Type()
)
fsLldpXMedRemModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpXMedRemModelName.setStatus("current")


class _FsLldpXMedRemAssetID_Type(SnmpAdminString):
    """Custom type fsLldpXMedRemAssetID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsLldpXMedRemAssetID_Type.__name__ = "SnmpAdminString"
_FsLldpXMedRemAssetID_Object = MibTableColumn
fsLldpXMedRemAssetID = _FsLldpXMedRemAssetID_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 2, 3, 1, 7),
    _FsLldpXMedRemAssetID_Type()
)
fsLldpXMedRemAssetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpXMedRemAssetID.setStatus("current")
_FsLldpXMedRemLocationTable_Object = MibTable
fsLldpXMedRemLocationTable = _FsLldpXMedRemLocationTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 2, 4)
)
if mibBuilder.loadTexts:
    fsLldpXMedRemLocationTable.setStatus("current")
_FsLldpXMedRemLocationEntry_Object = MibTableRow
fsLldpXMedRemLocationEntry = _FsLldpXMedRemLocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 2, 4, 1)
)
fsLldpXMedRemLocationEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
    (0, "LLDP-EXT-MED-MIB", "lldpXMedRemLocationSubtype"),
)
if mibBuilder.loadTexts:
    fsLldpXMedRemLocationEntry.setStatus("current")


class _FsLldpXMedRemLocationInfo_Type(OctetString):
    """Custom type fsLldpXMedRemLocationInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FsLldpXMedRemLocationInfo_Type.__name__ = "OctetString"
_FsLldpXMedRemLocationInfo_Object = MibTableColumn
fsLldpXMedRemLocationInfo = _FsLldpXMedRemLocationInfo_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 2, 4, 1, 1),
    _FsLldpXMedRemLocationInfo_Type()
)
fsLldpXMedRemLocationInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpXMedRemLocationInfo.setStatus("current")
_FsLldpXMedRemXPoEPDTable_Object = MibTable
fsLldpXMedRemXPoEPDTable = _FsLldpXMedRemXPoEPDTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 2, 5)
)
if mibBuilder.loadTexts:
    fsLldpXMedRemXPoEPDTable.setStatus("current")
_FsLldpXMedRemXPoEPDEntry_Object = MibTableRow
fsLldpXMedRemXPoEPDEntry = _FsLldpXMedRemXPoEPDEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 2, 5, 1)
)
fsLldpXMedRemXPoEPDEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
)
if mibBuilder.loadTexts:
    fsLldpXMedRemXPoEPDEntry.setStatus("current")


class _FsLldpXMedRemXPoEDeviceType_Type(Integer32):
    """Custom type fsLldpXMedRemXPoEDeviceType based on Integer32"""
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
        *(("unknown", 1),
          ("pseDevice", 2),
          ("pdDevice", 3),
          ("none", 4))
    )


_FsLldpXMedRemXPoEDeviceType_Type.__name__ = "Integer32"
_FsLldpXMedRemXPoEDeviceType_Object = MibTableColumn
fsLldpXMedRemXPoEDeviceType = _FsLldpXMedRemXPoEDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 2, 5, 1, 1),
    _FsLldpXMedRemXPoEDeviceType_Type()
)
fsLldpXMedRemXPoEDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpXMedRemXPoEDeviceType.setStatus("current")


class _FsLldpXMedRemXPoEPDPowerReq_Type(Gauge32):
    """Custom type fsLldpXMedRemXPoEPDPowerReq based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_FsLldpXMedRemXPoEPDPowerReq_Type.__name__ = "Gauge32"
_FsLldpXMedRemXPoEPDPowerReq_Object = MibTableColumn
fsLldpXMedRemXPoEPDPowerReq = _FsLldpXMedRemXPoEPDPowerReq_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 2, 5, 1, 2),
    _FsLldpXMedRemXPoEPDPowerReq_Type()
)
fsLldpXMedRemXPoEPDPowerReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpXMedRemXPoEPDPowerReq.setStatus("current")
if mibBuilder.loadTexts:
    fsLldpXMedRemXPoEPDPowerReq.setUnits("tenth of watt")


class _FsLldpXMedRemXPoEPDPowerSource_Type(Integer32):
    """Custom type fsLldpXMedRemXPoEPDPowerSource based on Integer32"""
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
        *(("unknown", 1),
          ("fromPSE", 2),
          ("local", 3),
          ("localAndPSE", 4))
    )


_FsLldpXMedRemXPoEPDPowerSource_Type.__name__ = "Integer32"
_FsLldpXMedRemXPoEPDPowerSource_Object = MibTableColumn
fsLldpXMedRemXPoEPDPowerSource = _FsLldpXMedRemXPoEPDPowerSource_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 2, 5, 1, 3),
    _FsLldpXMedRemXPoEPDPowerSource_Type()
)
fsLldpXMedRemXPoEPDPowerSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpXMedRemXPoEPDPowerSource.setStatus("current")


class _FsLldpXMedRemXPoEPDPowerPriority_Type(Integer32):
    """Custom type fsLldpXMedRemXPoEPDPowerPriority based on Integer32"""
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
        *(("unknown", 1),
          ("critical", 2),
          ("high", 3),
          ("low", 4))
    )


_FsLldpXMedRemXPoEPDPowerPriority_Type.__name__ = "Integer32"
_FsLldpXMedRemXPoEPDPowerPriority_Object = MibTableColumn
fsLldpXMedRemXPoEPDPowerPriority = _FsLldpXMedRemXPoEPDPowerPriority_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 2, 5, 1, 4),
    _FsLldpXMedRemXPoEPDPowerPriority_Type()
)
fsLldpXMedRemXPoEPDPowerPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpXMedRemXPoEPDPowerPriority.setStatus("current")
_FsLldpMedStatistics_ObjectIdentity = ObjectIdentity
fsLldpMedStatistics = _FsLldpMedStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 3)
)
_FsLldpMedStatsTable_Object = MibTable
fsLldpMedStatsTable = _FsLldpMedStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 3, 1)
)
if mibBuilder.loadTexts:
    fsLldpMedStatsTable.setStatus("current")
_FsLldpMedStatsEntry_Object = MibTableRow
fsLldpMedStatsEntry = _FsLldpMedStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 3, 1, 1)
)
fsLldpMedStatsEntry.setIndexNames(
    (0, "ARICENT-LLDP-MED-MIB", "fsLldpMedStatsIfIndex"),
    (0, "ARICENT-LLDP-MED-MIB", "fsLldpMedStatsDestMACAddress"),
)
if mibBuilder.loadTexts:
    fsLldpMedStatsEntry.setStatus("current")
_FsLldpMedStatsIfIndex_Type = InterfaceIndex
_FsLldpMedStatsIfIndex_Object = MibTableColumn
fsLldpMedStatsIfIndex = _FsLldpMedStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 3, 1, 1, 1),
    _FsLldpMedStatsIfIndex_Type()
)
fsLldpMedStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsLldpMedStatsIfIndex.setStatus("current")
_FsLldpMedStatsDestMACAddress_Type = LldpV2DestAddressTableIndex
_FsLldpMedStatsDestMACAddress_Object = MibTableColumn
fsLldpMedStatsDestMACAddress = _FsLldpMedStatsDestMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 3, 1, 1, 2),
    _FsLldpMedStatsDestMACAddress_Type()
)
fsLldpMedStatsDestMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsLldpMedStatsDestMACAddress.setStatus("current")
_FsLldpMedStatsTxFramesTotal_Type = Counter32
_FsLldpMedStatsTxFramesTotal_Object = MibTableColumn
fsLldpMedStatsTxFramesTotal = _FsLldpMedStatsTxFramesTotal_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 3, 1, 1, 3),
    _FsLldpMedStatsTxFramesTotal_Type()
)
fsLldpMedStatsTxFramesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpMedStatsTxFramesTotal.setStatus("current")
if mibBuilder.loadTexts:
    fsLldpMedStatsTxFramesTotal.setUnits("LLDP frames")
_FsLldpMedStatsRxFramesTotal_Type = Counter32
_FsLldpMedStatsRxFramesTotal_Object = MibTableColumn
fsLldpMedStatsRxFramesTotal = _FsLldpMedStatsRxFramesTotal_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 3, 1, 1, 4),
    _FsLldpMedStatsRxFramesTotal_Type()
)
fsLldpMedStatsRxFramesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpMedStatsRxFramesTotal.setStatus("current")
if mibBuilder.loadTexts:
    fsLldpMedStatsRxFramesTotal.setUnits("LLDP frames")
_FsLldpMedStatsRxFramesDiscardedTotal_Type = Counter32
_FsLldpMedStatsRxFramesDiscardedTotal_Object = MibTableColumn
fsLldpMedStatsRxFramesDiscardedTotal = _FsLldpMedStatsRxFramesDiscardedTotal_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 3, 1, 1, 5),
    _FsLldpMedStatsRxFramesDiscardedTotal_Type()
)
fsLldpMedStatsRxFramesDiscardedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpMedStatsRxFramesDiscardedTotal.setStatus("current")
if mibBuilder.loadTexts:
    fsLldpMedStatsRxFramesDiscardedTotal.setUnits("LLDP frames")
_FsLldpMedStatsRxTLVsDiscardedTotal_Type = Counter32
_FsLldpMedStatsRxTLVsDiscardedTotal_Object = MibTableColumn
fsLldpMedStatsRxTLVsDiscardedTotal = _FsLldpMedStatsRxTLVsDiscardedTotal_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 3, 1, 1, 6),
    _FsLldpMedStatsRxTLVsDiscardedTotal_Type()
)
fsLldpMedStatsRxTLVsDiscardedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpMedStatsRxTLVsDiscardedTotal.setStatus("current")
if mibBuilder.loadTexts:
    fsLldpMedStatsRxTLVsDiscardedTotal.setUnits("TLVs")
_FsLldpMedStatsRxCapTLVsDiscarded_Type = Counter32
_FsLldpMedStatsRxCapTLVsDiscarded_Object = MibTableColumn
fsLldpMedStatsRxCapTLVsDiscarded = _FsLldpMedStatsRxCapTLVsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 3, 1, 1, 7),
    _FsLldpMedStatsRxCapTLVsDiscarded_Type()
)
fsLldpMedStatsRxCapTLVsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpMedStatsRxCapTLVsDiscarded.setStatus("current")
if mibBuilder.loadTexts:
    fsLldpMedStatsRxCapTLVsDiscarded.setUnits("TLVs")
_FsLldpMedStatsRxPolicyTLVsDiscarded_Type = Counter32
_FsLldpMedStatsRxPolicyTLVsDiscarded_Object = MibTableColumn
fsLldpMedStatsRxPolicyTLVsDiscarded = _FsLldpMedStatsRxPolicyTLVsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 3, 1, 1, 8),
    _FsLldpMedStatsRxPolicyTLVsDiscarded_Type()
)
fsLldpMedStatsRxPolicyTLVsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpMedStatsRxPolicyTLVsDiscarded.setStatus("current")
if mibBuilder.loadTexts:
    fsLldpMedStatsRxPolicyTLVsDiscarded.setUnits("TLVs")
_FsLldpMedStatsRxInventoryTLVsDiscarded_Type = Counter32
_FsLldpMedStatsRxInventoryTLVsDiscarded_Object = MibTableColumn
fsLldpMedStatsRxInventoryTLVsDiscarded = _FsLldpMedStatsRxInventoryTLVsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 3, 1, 1, 9),
    _FsLldpMedStatsRxInventoryTLVsDiscarded_Type()
)
fsLldpMedStatsRxInventoryTLVsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpMedStatsRxInventoryTLVsDiscarded.setStatus("current")
if mibBuilder.loadTexts:
    fsLldpMedStatsRxInventoryTLVsDiscarded.setUnits("TLVs")
_FsLldpMedStatsRxLocationTLVsDiscarded_Type = Counter32
_FsLldpMedStatsRxLocationTLVsDiscarded_Object = MibTableColumn
fsLldpMedStatsRxLocationTLVsDiscarded = _FsLldpMedStatsRxLocationTLVsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 3, 1, 1, 10),
    _FsLldpMedStatsRxLocationTLVsDiscarded_Type()
)
fsLldpMedStatsRxLocationTLVsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpMedStatsRxLocationTLVsDiscarded.setStatus("current")
if mibBuilder.loadTexts:
    fsLldpMedStatsRxLocationTLVsDiscarded.setUnits("TLVs")
_FsLldpMedStatsRxExPowerMDITLVsDiscarded_Type = Counter32
_FsLldpMedStatsRxExPowerMDITLVsDiscarded_Object = MibTableColumn
fsLldpMedStatsRxExPowerMDITLVsDiscarded = _FsLldpMedStatsRxExPowerMDITLVsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 3, 1, 1, 11),
    _FsLldpMedStatsRxExPowerMDITLVsDiscarded_Type()
)
fsLldpMedStatsRxExPowerMDITLVsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpMedStatsRxExPowerMDITLVsDiscarded.setStatus("current")
if mibBuilder.loadTexts:
    fsLldpMedStatsRxExPowerMDITLVsDiscarded.setUnits("TLVs")


class _FsLldpMedStatsRxCapTLVsDiscardedReason_Type(DisplayString):
    """Custom type fsLldpMedStatsRxCapTLVsDiscardedReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsLldpMedStatsRxCapTLVsDiscardedReason_Type.__name__ = "DisplayString"
_FsLldpMedStatsRxCapTLVsDiscardedReason_Object = MibTableColumn
fsLldpMedStatsRxCapTLVsDiscardedReason = _FsLldpMedStatsRxCapTLVsDiscardedReason_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 3, 1, 1, 12),
    _FsLldpMedStatsRxCapTLVsDiscardedReason_Type()
)
fsLldpMedStatsRxCapTLVsDiscardedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpMedStatsRxCapTLVsDiscardedReason.setStatus("current")


class _FsLldpMedStatsRxPolicyDiscardedReason_Type(DisplayString):
    """Custom type fsLldpMedStatsRxPolicyDiscardedReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsLldpMedStatsRxPolicyDiscardedReason_Type.__name__ = "DisplayString"
_FsLldpMedStatsRxPolicyDiscardedReason_Object = MibTableColumn
fsLldpMedStatsRxPolicyDiscardedReason = _FsLldpMedStatsRxPolicyDiscardedReason_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 3, 1, 1, 13),
    _FsLldpMedStatsRxPolicyDiscardedReason_Type()
)
fsLldpMedStatsRxPolicyDiscardedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpMedStatsRxPolicyDiscardedReason.setStatus("current")


class _FsLldpMedStatsRxInventoryDiscardedReason_Type(DisplayString):
    """Custom type fsLldpMedStatsRxInventoryDiscardedReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsLldpMedStatsRxInventoryDiscardedReason_Type.__name__ = "DisplayString"
_FsLldpMedStatsRxInventoryDiscardedReason_Object = MibTableColumn
fsLldpMedStatsRxInventoryDiscardedReason = _FsLldpMedStatsRxInventoryDiscardedReason_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 3, 1, 1, 14),
    _FsLldpMedStatsRxInventoryDiscardedReason_Type()
)
fsLldpMedStatsRxInventoryDiscardedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpMedStatsRxInventoryDiscardedReason.setStatus("current")


class _FsLldpMedStatsRxLocationDiscardedReason_Type(DisplayString):
    """Custom type fsLldpMedStatsRxLocationDiscardedReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsLldpMedStatsRxLocationDiscardedReason_Type.__name__ = "DisplayString"
_FsLldpMedStatsRxLocationDiscardedReason_Object = MibTableColumn
fsLldpMedStatsRxLocationDiscardedReason = _FsLldpMedStatsRxLocationDiscardedReason_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 3, 1, 1, 15),
    _FsLldpMedStatsRxLocationDiscardedReason_Type()
)
fsLldpMedStatsRxLocationDiscardedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpMedStatsRxLocationDiscardedReason.setStatus("current")


class _FsLldpMedStatsRxExPowerDiscardedReason_Type(DisplayString):
    """Custom type fsLldpMedStatsRxExPowerDiscardedReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsLldpMedStatsRxExPowerDiscardedReason_Type.__name__ = "DisplayString"
_FsLldpMedStatsRxExPowerDiscardedReason_Object = MibTableColumn
fsLldpMedStatsRxExPowerDiscardedReason = _FsLldpMedStatsRxExPowerDiscardedReason_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 3, 1, 1, 16),
    _FsLldpMedStatsRxExPowerDiscardedReason_Type()
)
fsLldpMedStatsRxExPowerDiscardedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpMedStatsRxExPowerDiscardedReason.setStatus("current")


class _FsLldpMedClearStats_Type(TruthValue):
    """Custom type fsLldpMedClearStats based on TruthValue"""
    defaultValue = 2


_FsLldpMedClearStats_Type.__name__ = "TruthValue"
_FsLldpMedClearStats_Object = MibScalar
fsLldpMedClearStats = _FsLldpMedClearStats_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 3, 2),
    _FsLldpMedClearStats_Type()
)
fsLldpMedClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLldpMedClearStats.setStatus("current")
_FsLldpMedNotification_ObjectIdentity = ObjectIdentity
fsLldpMedNotification = _FsLldpMedNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 4)
)
_FsLldpMedTraps_ObjectIdentity = ObjectIdentity
fsLldpMedTraps = _FsLldpMedTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 4, 0)
)
_FsLldpMedNotifyObjects_ObjectIdentity = ObjectIdentity
fsLldpMedNotifyObjects = _FsLldpMedNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 5)
)
_FsLldpMedTrapObjects_ObjectIdentity = ObjectIdentity
fsLldpMedTrapObjects = _FsLldpMedTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 5, 1)
)
_FsLldpXMedMediaPolicyAppType_Type = PolicyAppType
_FsLldpXMedMediaPolicyAppType_Object = MibScalar
fsLldpXMedMediaPolicyAppType = _FsLldpXMedMediaPolicyAppType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 5, 1, 1),
    _FsLldpXMedMediaPolicyAppType_Type()
)
fsLldpXMedMediaPolicyAppType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsLldpXMedMediaPolicyAppType.setStatus("current")
lldpV2PortConfigEntry.registerAugmentions(
    ("ARICENT-LLDP-MED-MIB",
     "fsLldpMedPortConfigEntry")
)
fsLldpMedPortConfigEntry.setIndexNames(*lldpV2PortConfigEntry.getIndexNames())
lldpXMedLocLocationEntry.registerAugmentions(
    ("ARICENT-LLDP-MED-MIB",
     "fsLldpMedLocLocationEntry")
)
fsLldpMedLocLocationEntry.setIndexNames(*lldpXMedLocLocationEntry.getIndexNames())

# Managed Objects groups


# Notification objects

fsLldpMedPolicyMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 101, 4, 0, 1)
)
fsLldpMedPolicyMismatch.setObjects(
      *(("LLDP-MIB", "lldpRemChassisId"),
        ("LLDP-MIB", "lldpRemPortId"),
        ("ARICENT-LLDP-MED-MIB", "fsLldpXMedMediaPolicyAppType"))
)
if mibBuilder.loadTexts:
    fsLldpMedPolicyMismatch.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-LLDP-MED-MIB",
    **{"fsLldpMed": fsLldpMed,
       "fsLldpMedLocalConfig": fsLldpMedLocalConfig,
       "fsLldpMedPortConfigTable": fsLldpMedPortConfigTable,
       "fsLldpMedPortConfigEntry": fsLldpMedPortConfigEntry,
       "fsLldpMedPortCapSupported": fsLldpMedPortCapSupported,
       "fsLldpMedPortConfigTLVsTxEnable": fsLldpMedPortConfigTLVsTxEnable,
       "fsLldpMedLocMediaPolicyTable": fsLldpMedLocMediaPolicyTable,
       "fsLldpMedLocMediaPolicyEntry": fsLldpMedLocMediaPolicyEntry,
       "fsLldpMedLocMediaPolicyAppType": fsLldpMedLocMediaPolicyAppType,
       "fsLldpMedLocMediaPolicyVlanID": fsLldpMedLocMediaPolicyVlanID,
       "fsLldpMedLocMediaPolicyPriority": fsLldpMedLocMediaPolicyPriority,
       "fsLldpMedLocMediaPolicyDscp": fsLldpMedLocMediaPolicyDscp,
       "fsLldpMedLocMediaPolicyUnknown": fsLldpMedLocMediaPolicyUnknown,
       "fsLldpMedLocMediaPolicyTagged": fsLldpMedLocMediaPolicyTagged,
       "fsLldpMedLocMediaPolicyRowStatus": fsLldpMedLocMediaPolicyRowStatus,
       "fsLldpMedLocLocationTable": fsLldpMedLocLocationTable,
       "fsLldpMedLocLocationEntry": fsLldpMedLocLocationEntry,
       "fsLldpMedLocLocationRowStatus": fsLldpMedLocLocationRowStatus,
       "fsLldpMedRemoteConfig": fsLldpMedRemoteConfig,
       "fsLldpXMedRemCapabilitiesTable": fsLldpXMedRemCapabilitiesTable,
       "fsLldpXMedRemCapabilitiesEntry": fsLldpXMedRemCapabilitiesEntry,
       "fsLldpXMedRemCapSupported": fsLldpXMedRemCapSupported,
       "fsLldpXMedRemCapCurrent": fsLldpXMedRemCapCurrent,
       "fsLldpXMedRemDeviceClass": fsLldpXMedRemDeviceClass,
       "fsLldpXMedRemMediaPolicyTable": fsLldpXMedRemMediaPolicyTable,
       "fsLldpXMedRemMediaPolicyEntry": fsLldpXMedRemMediaPolicyEntry,
       "fsLldpXMedRemMediaPolicyAppType": fsLldpXMedRemMediaPolicyAppType,
       "fsLldpXMedRemMediaPolicyVlanID": fsLldpXMedRemMediaPolicyVlanID,
       "fsLldpXMedRemMediaPolicyPriority": fsLldpXMedRemMediaPolicyPriority,
       "fsLldpXMedRemMediaPolicyDscp": fsLldpXMedRemMediaPolicyDscp,
       "fsLldpXMedRemMediaPolicyUnknown": fsLldpXMedRemMediaPolicyUnknown,
       "fsLldpXMedRemMediaPolicyTagged": fsLldpXMedRemMediaPolicyTagged,
       "fsLldpXMedRemInventoryTable": fsLldpXMedRemInventoryTable,
       "fsLldpXMedRemInventoryEntry": fsLldpXMedRemInventoryEntry,
       "fsLldpXMedRemHardwareRev": fsLldpXMedRemHardwareRev,
       "fsLldpXMedRemFirmwareRev": fsLldpXMedRemFirmwareRev,
       "fsLldpXMedRemSoftwareRev": fsLldpXMedRemSoftwareRev,
       "fsLldpXMedRemSerialNum": fsLldpXMedRemSerialNum,
       "fsLldpXMedRemMfgName": fsLldpXMedRemMfgName,
       "fsLldpXMedRemModelName": fsLldpXMedRemModelName,
       "fsLldpXMedRemAssetID": fsLldpXMedRemAssetID,
       "fsLldpXMedRemLocationTable": fsLldpXMedRemLocationTable,
       "fsLldpXMedRemLocationEntry": fsLldpXMedRemLocationEntry,
       "fsLldpXMedRemLocationInfo": fsLldpXMedRemLocationInfo,
       "fsLldpXMedRemXPoEPDTable": fsLldpXMedRemXPoEPDTable,
       "fsLldpXMedRemXPoEPDEntry": fsLldpXMedRemXPoEPDEntry,
       "fsLldpXMedRemXPoEDeviceType": fsLldpXMedRemXPoEDeviceType,
       "fsLldpXMedRemXPoEPDPowerReq": fsLldpXMedRemXPoEPDPowerReq,
       "fsLldpXMedRemXPoEPDPowerSource": fsLldpXMedRemXPoEPDPowerSource,
       "fsLldpXMedRemXPoEPDPowerPriority": fsLldpXMedRemXPoEPDPowerPriority,
       "fsLldpMedStatistics": fsLldpMedStatistics,
       "fsLldpMedStatsTable": fsLldpMedStatsTable,
       "fsLldpMedStatsEntry": fsLldpMedStatsEntry,
       "fsLldpMedStatsIfIndex": fsLldpMedStatsIfIndex,
       "fsLldpMedStatsDestMACAddress": fsLldpMedStatsDestMACAddress,
       "fsLldpMedStatsTxFramesTotal": fsLldpMedStatsTxFramesTotal,
       "fsLldpMedStatsRxFramesTotal": fsLldpMedStatsRxFramesTotal,
       "fsLldpMedStatsRxFramesDiscardedTotal": fsLldpMedStatsRxFramesDiscardedTotal,
       "fsLldpMedStatsRxTLVsDiscardedTotal": fsLldpMedStatsRxTLVsDiscardedTotal,
       "fsLldpMedStatsRxCapTLVsDiscarded": fsLldpMedStatsRxCapTLVsDiscarded,
       "fsLldpMedStatsRxPolicyTLVsDiscarded": fsLldpMedStatsRxPolicyTLVsDiscarded,
       "fsLldpMedStatsRxInventoryTLVsDiscarded": fsLldpMedStatsRxInventoryTLVsDiscarded,
       "fsLldpMedStatsRxLocationTLVsDiscarded": fsLldpMedStatsRxLocationTLVsDiscarded,
       "fsLldpMedStatsRxExPowerMDITLVsDiscarded": fsLldpMedStatsRxExPowerMDITLVsDiscarded,
       "fsLldpMedStatsRxCapTLVsDiscardedReason": fsLldpMedStatsRxCapTLVsDiscardedReason,
       "fsLldpMedStatsRxPolicyDiscardedReason": fsLldpMedStatsRxPolicyDiscardedReason,
       "fsLldpMedStatsRxInventoryDiscardedReason": fsLldpMedStatsRxInventoryDiscardedReason,
       "fsLldpMedStatsRxLocationDiscardedReason": fsLldpMedStatsRxLocationDiscardedReason,
       "fsLldpMedStatsRxExPowerDiscardedReason": fsLldpMedStatsRxExPowerDiscardedReason,
       "fsLldpMedClearStats": fsLldpMedClearStats,
       "fsLldpMedNotification": fsLldpMedNotification,
       "fsLldpMedTraps": fsLldpMedTraps,
       "fsLldpMedPolicyMismatch": fsLldpMedPolicyMismatch,
       "fsLldpMedNotifyObjects": fsLldpMedNotifyObjects,
       "fsLldpMedTrapObjects": fsLldpMedTrapObjects,
       "fsLldpXMedMediaPolicyAppType": fsLldpXMedMediaPolicyAppType}
)
