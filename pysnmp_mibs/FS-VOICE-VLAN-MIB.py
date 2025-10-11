# SNMP MIB module (FS-VOICE-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-VOICE-VLAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:12:27 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "FS-TC",
    "IfIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fsVoiceVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 52)
)
if mibBuilder.loadTexts:
    fsVoiceVlanMIB.setRevisions(
        ("2009-06-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsVoiceVlanMIBObjects_ObjectIdentity = ObjectIdentity
fsVoiceVlanMIBObjects = _FsVoiceVlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 52, 1)
)
_FsVoiceVlanOuiTable_Object = MibTable
fsVoiceVlanOuiTable = _FsVoiceVlanOuiTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 52, 1, 1)
)
if mibBuilder.loadTexts:
    fsVoiceVlanOuiTable.setStatus("current")
_FsVoiceVlanOuiEntry_Object = MibTableRow
fsVoiceVlanOuiEntry = _FsVoiceVlanOuiEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 52, 1, 1, 1)
)
fsVoiceVlanOuiEntry.setIndexNames(
    (0, "FS-VOICE-VLAN-MIB", "fsVoiceVlanOuiAddress"),
)
if mibBuilder.loadTexts:
    fsVoiceVlanOuiEntry.setStatus("current")
_FsVoiceVlanOuiAddress_Type = MacAddress
_FsVoiceVlanOuiAddress_Object = MibTableColumn
fsVoiceVlanOuiAddress = _FsVoiceVlanOuiAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 52, 1, 1, 1, 1),
    _FsVoiceVlanOuiAddress_Type()
)
fsVoiceVlanOuiAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVoiceVlanOuiAddress.setStatus("current")
_FsVoiceVlanOuiMask_Type = MacAddress
_FsVoiceVlanOuiMask_Object = MibTableColumn
fsVoiceVlanOuiMask = _FsVoiceVlanOuiMask_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 52, 1, 1, 1, 2),
    _FsVoiceVlanOuiMask_Type()
)
fsVoiceVlanOuiMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVoiceVlanOuiMask.setStatus("current")


class _FsVoiceVlanOuiDescription_Type(OctetString):
    """Custom type fsVoiceVlanOuiDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_FsVoiceVlanOuiDescription_Type.__name__ = "OctetString"
_FsVoiceVlanOuiDescription_Object = MibTableColumn
fsVoiceVlanOuiDescription = _FsVoiceVlanOuiDescription_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 52, 1, 1, 1, 3),
    _FsVoiceVlanOuiDescription_Type()
)
fsVoiceVlanOuiDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVoiceVlanOuiDescription.setStatus("current")
_FsVoiceVlanOuiRowStatus_Type = RowStatus
_FsVoiceVlanOuiRowStatus_Object = MibTableColumn
fsVoiceVlanOuiRowStatus = _FsVoiceVlanOuiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 52, 1, 1, 1, 4),
    _FsVoiceVlanOuiRowStatus_Type()
)
fsVoiceVlanOuiRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVoiceVlanOuiRowStatus.setStatus("current")
_FsVoiceVlanEnabledId_Type = Integer32
_FsVoiceVlanEnabledId_Object = MibScalar
fsVoiceVlanEnabledId = _FsVoiceVlanEnabledId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 52, 1, 2),
    _FsVoiceVlanEnabledId_Type()
)
fsVoiceVlanEnabledId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVoiceVlanEnabledId.setStatus("current")
_FsVoiceVlanPortEnableTable_Object = MibTable
fsVoiceVlanPortEnableTable = _FsVoiceVlanPortEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 52, 1, 3)
)
if mibBuilder.loadTexts:
    fsVoiceVlanPortEnableTable.setStatus("current")
_FsVoiceVlanPortEnableEntry_Object = MibTableRow
fsVoiceVlanPortEnableEntry = _FsVoiceVlanPortEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 52, 1, 3, 1)
)
fsVoiceVlanPortEnableEntry.setIndexNames(
    (0, "FS-VOICE-VLAN-MIB", "fsVoiceVlanPortEnableIfIndex"),
)
if mibBuilder.loadTexts:
    fsVoiceVlanPortEnableEntry.setStatus("current")
_FsVoiceVlanPortEnableIfIndex_Type = IfIndex
_FsVoiceVlanPortEnableIfIndex_Object = MibTableColumn
fsVoiceVlanPortEnableIfIndex = _FsVoiceVlanPortEnableIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 52, 1, 3, 1, 1),
    _FsVoiceVlanPortEnableIfIndex_Type()
)
fsVoiceVlanPortEnableIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsVoiceVlanPortEnableIfIndex.setStatus("current")
_FsVoiceVlanPortStatus_Type = EnabledStatus
_FsVoiceVlanPortStatus_Object = MibTableColumn
fsVoiceVlanPortStatus = _FsVoiceVlanPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 52, 1, 3, 1, 2),
    _FsVoiceVlanPortStatus_Type()
)
fsVoiceVlanPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVoiceVlanPortStatus.setStatus("current")


class _FsVoiceVlanAgingTime_Type(Integer32):
    """Custom type fsVoiceVlanAgingTime based on Integer32"""
    defaultValue = 1440

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 10000),
    )


_FsVoiceVlanAgingTime_Type.__name__ = "Integer32"
_FsVoiceVlanAgingTime_Object = MibScalar
fsVoiceVlanAgingTime = _FsVoiceVlanAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 52, 1, 4),
    _FsVoiceVlanAgingTime_Type()
)
fsVoiceVlanAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVoiceVlanAgingTime.setStatus("current")


class _FsVoiceVlanSecurityState_Type(Integer32):
    """Custom type fsVoiceVlanSecurityState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("security", 1),
          ("normal", 2))
    )


_FsVoiceVlanSecurityState_Type.__name__ = "Integer32"
_FsVoiceVlanSecurityState_Object = MibScalar
fsVoiceVlanSecurityState = _FsVoiceVlanSecurityState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 52, 1, 5),
    _FsVoiceVlanSecurityState_Type()
)
fsVoiceVlanSecurityState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVoiceVlanSecurityState.setStatus("current")


class _FsVoiceVlanCos_Type(Integer32):
    """Custom type fsVoiceVlanCos based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsVoiceVlanCos_Type.__name__ = "Integer32"
_FsVoiceVlanCos_Object = MibScalar
fsVoiceVlanCos = _FsVoiceVlanCos_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 52, 1, 6),
    _FsVoiceVlanCos_Type()
)
fsVoiceVlanCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVoiceVlanCos.setStatus("current")


class _FsVoiceVlanDscp_Type(Integer32):
    """Custom type fsVoiceVlanDscp based on Integer32"""
    defaultValue = 46


_FsVoiceVlanDscp_Type.__name__ = "Integer32"
_FsVoiceVlanDscp_Object = MibScalar
fsVoiceVlanDscp = _FsVoiceVlanDscp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 52, 1, 7),
    _FsVoiceVlanDscp_Type()
)
fsVoiceVlanDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVoiceVlanDscp.setStatus("current")
_FsVoiceVlanPortModeTable_Object = MibTable
fsVoiceVlanPortModeTable = _FsVoiceVlanPortModeTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 52, 1, 8)
)
if mibBuilder.loadTexts:
    fsVoiceVlanPortModeTable.setStatus("current")
_FsVoiceVlanPortModeEntry_Object = MibTableRow
fsVoiceVlanPortModeEntry = _FsVoiceVlanPortModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 52, 1, 8, 1)
)
fsVoiceVlanPortModeEntry.setIndexNames(
    (0, "FS-VOICE-VLAN-MIB", "fsVoiceVlanPortIfIndex"),
)
if mibBuilder.loadTexts:
    fsVoiceVlanPortModeEntry.setStatus("current")
_FsVoiceVlanPortIfIndex_Type = IfIndex
_FsVoiceVlanPortIfIndex_Object = MibTableColumn
fsVoiceVlanPortIfIndex = _FsVoiceVlanPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 52, 1, 8, 1, 1),
    _FsVoiceVlanPortIfIndex_Type()
)
fsVoiceVlanPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsVoiceVlanPortIfIndex.setStatus("current")


class _FsVoiceVlanPortMode_Type(Integer32):
    """Custom type fsVoiceVlanPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_FsVoiceVlanPortMode_Type.__name__ = "Integer32"
_FsVoiceVlanPortMode_Object = MibTableColumn
fsVoiceVlanPortMode = _FsVoiceVlanPortMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 52, 1, 8, 1, 2),
    _FsVoiceVlanPortMode_Type()
)
fsVoiceVlanPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVoiceVlanPortMode.setStatus("current")
_FsVoiceVlanMacTable_Object = MibTable
fsVoiceVlanMacTable = _FsVoiceVlanMacTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 52, 1, 9)
)
if mibBuilder.loadTexts:
    fsVoiceVlanMacTable.setStatus("current")
_FsVoiceVlanMacEntry_Object = MibTableRow
fsVoiceVlanMacEntry = _FsVoiceVlanMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 52, 1, 9, 1)
)
fsVoiceVlanMacEntry.setIndexNames(
    (0, "FS-VOICE-VLAN-MIB", "fsVoiceVlanMacAddress"),
    (0, "FS-VOICE-VLAN-MIB", "fsVoiceVlanMacIfIndex"),
)
if mibBuilder.loadTexts:
    fsVoiceVlanMacEntry.setStatus("current")
_FsVoiceVlanMacAddress_Type = MacAddress
_FsVoiceVlanMacAddress_Object = MibTableColumn
fsVoiceVlanMacAddress = _FsVoiceVlanMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 52, 1, 9, 1, 1),
    _FsVoiceVlanMacAddress_Type()
)
fsVoiceVlanMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVoiceVlanMacAddress.setStatus("current")
_FsVoiceVlanMacIfIndex_Type = IfIndex
_FsVoiceVlanMacIfIndex_Object = MibTableColumn
fsVoiceVlanMacIfIndex = _FsVoiceVlanMacIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 52, 1, 9, 1, 2),
    _FsVoiceVlanMacIfIndex_Type()
)
fsVoiceVlanMacIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVoiceVlanMacIfIndex.setStatus("current")


class _FsVoiceVlanMacDescription_Type(OctetString):
    """Custom type fsVoiceVlanMacDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_FsVoiceVlanMacDescription_Type.__name__ = "OctetString"
_FsVoiceVlanMacDescription_Object = MibTableColumn
fsVoiceVlanMacDescription = _FsVoiceVlanMacDescription_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 52, 1, 9, 1, 3),
    _FsVoiceVlanMacDescription_Type()
)
fsVoiceVlanMacDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVoiceVlanMacDescription.setStatus("current")
_FsVoiceVlanMIBConformance_ObjectIdentity = ObjectIdentity
fsVoiceVlanMIBConformance = _FsVoiceVlanMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 52, 2)
)
_FsVoiceVlanMIBCompliances_ObjectIdentity = ObjectIdentity
fsVoiceVlanMIBCompliances = _FsVoiceVlanMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 52, 2, 1)
)
_FsVoiceVlanMIBGroups_ObjectIdentity = ObjectIdentity
fsVoiceVlanMIBGroups = _FsVoiceVlanMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 52, 2, 2)
)

# Managed Objects groups

fsVoiceVlanMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 52, 2, 2, 1)
)
fsVoiceVlanMIBGroup.setObjects(
      *(("FS-VOICE-VLAN-MIB", "fsVoiceVlanOuiAddress"),
        ("FS-VOICE-VLAN-MIB", "fsVoiceVlanOuiMask"),
        ("FS-VOICE-VLAN-MIB", "fsVoiceVlanOuiDescription"),
        ("FS-VOICE-VLAN-MIB", "fsVoiceVlanOuiRowStatus"),
        ("FS-VOICE-VLAN-MIB", "fsVoiceVlanEnabledId"),
        ("FS-VOICE-VLAN-MIB", "fsVoiceVlanPortStatus"),
        ("FS-VOICE-VLAN-MIB", "fsVoiceVlanAgingTime"),
        ("FS-VOICE-VLAN-MIB", "fsVoiceVlanSecurityState"),
        ("FS-VOICE-VLAN-MIB", "fsVoiceVlanCos"),
        ("FS-VOICE-VLAN-MIB", "fsVoiceVlanDscp"),
        ("FS-VOICE-VLAN-MIB", "fsVoiceVlanPortMode"),
        ("FS-VOICE-VLAN-MIB", "fsVoiceVlanMacAddress"),
        ("FS-VOICE-VLAN-MIB", "fsVoiceVlanMacIfIndex"),
        ("FS-VOICE-VLAN-MIB", "fsVoiceVlanMacDescription"))
)
if mibBuilder.loadTexts:
    fsVoiceVlanMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsVoiceVlanMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 52, 2, 1, 1)
)
fsVoiceVlanMIBCompliance.setObjects(
    ("FS-VOICE-VLAN-MIB", "fsVoiceVlanMIBGroup")
)
if mibBuilder.loadTexts:
    fsVoiceVlanMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-VOICE-VLAN-MIB",
    **{"fsVoiceVlanMIB": fsVoiceVlanMIB,
       "fsVoiceVlanMIBObjects": fsVoiceVlanMIBObjects,
       "fsVoiceVlanOuiTable": fsVoiceVlanOuiTable,
       "fsVoiceVlanOuiEntry": fsVoiceVlanOuiEntry,
       "fsVoiceVlanOuiAddress": fsVoiceVlanOuiAddress,
       "fsVoiceVlanOuiMask": fsVoiceVlanOuiMask,
       "fsVoiceVlanOuiDescription": fsVoiceVlanOuiDescription,
       "fsVoiceVlanOuiRowStatus": fsVoiceVlanOuiRowStatus,
       "fsVoiceVlanEnabledId": fsVoiceVlanEnabledId,
       "fsVoiceVlanPortEnableTable": fsVoiceVlanPortEnableTable,
       "fsVoiceVlanPortEnableEntry": fsVoiceVlanPortEnableEntry,
       "fsVoiceVlanPortEnableIfIndex": fsVoiceVlanPortEnableIfIndex,
       "fsVoiceVlanPortStatus": fsVoiceVlanPortStatus,
       "fsVoiceVlanAgingTime": fsVoiceVlanAgingTime,
       "fsVoiceVlanSecurityState": fsVoiceVlanSecurityState,
       "fsVoiceVlanCos": fsVoiceVlanCos,
       "fsVoiceVlanDscp": fsVoiceVlanDscp,
       "fsVoiceVlanPortModeTable": fsVoiceVlanPortModeTable,
       "fsVoiceVlanPortModeEntry": fsVoiceVlanPortModeEntry,
       "fsVoiceVlanPortIfIndex": fsVoiceVlanPortIfIndex,
       "fsVoiceVlanPortMode": fsVoiceVlanPortMode,
       "fsVoiceVlanMacTable": fsVoiceVlanMacTable,
       "fsVoiceVlanMacEntry": fsVoiceVlanMacEntry,
       "fsVoiceVlanMacAddress": fsVoiceVlanMacAddress,
       "fsVoiceVlanMacIfIndex": fsVoiceVlanMacIfIndex,
       "fsVoiceVlanMacDescription": fsVoiceVlanMacDescription,
       "fsVoiceVlanMIBConformance": fsVoiceVlanMIBConformance,
       "fsVoiceVlanMIBCompliances": fsVoiceVlanMIBCompliances,
       "fsVoiceVlanMIBCompliance": fsVoiceVlanMIBCompliance,
       "fsVoiceVlanMIBGroups": fsVoiceVlanMIBGroups,
       "fsVoiceVlanMIBGroup": fsVoiceVlanMIBGroup}
)
