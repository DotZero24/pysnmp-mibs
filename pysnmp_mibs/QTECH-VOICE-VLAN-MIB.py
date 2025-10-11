# SNMP MIB module (QTECH-VOICE-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-VOICE-VLAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:57:22 2025
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "QTECH-TC",
    "IfIndex")

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

qtechVoiceVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 52)
)
if mibBuilder.loadTexts:
    qtechVoiceVlanMIB.setRevisions(
        ("2009-06-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechVoiceVlanMIBObjects_ObjectIdentity = ObjectIdentity
qtechVoiceVlanMIBObjects = _QtechVoiceVlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 52, 1)
)
_QtechVoiceVlanOuiTable_Object = MibTable
qtechVoiceVlanOuiTable = _QtechVoiceVlanOuiTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 52, 1, 1)
)
if mibBuilder.loadTexts:
    qtechVoiceVlanOuiTable.setStatus("current")
_QtechVoiceVlanOuiEntry_Object = MibTableRow
qtechVoiceVlanOuiEntry = _QtechVoiceVlanOuiEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 52, 1, 1, 1)
)
qtechVoiceVlanOuiEntry.setIndexNames(
    (0, "QTECH-VOICE-VLAN-MIB", "qtechVoiceVlanOuiAddress"),
)
if mibBuilder.loadTexts:
    qtechVoiceVlanOuiEntry.setStatus("current")
_QtechVoiceVlanOuiAddress_Type = MacAddress
_QtechVoiceVlanOuiAddress_Object = MibTableColumn
qtechVoiceVlanOuiAddress = _QtechVoiceVlanOuiAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 52, 1, 1, 1, 1),
    _QtechVoiceVlanOuiAddress_Type()
)
qtechVoiceVlanOuiAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVoiceVlanOuiAddress.setStatus("current")
_QtechVoiceVlanOuiMask_Type = MacAddress
_QtechVoiceVlanOuiMask_Object = MibTableColumn
qtechVoiceVlanOuiMask = _QtechVoiceVlanOuiMask_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 52, 1, 1, 1, 2),
    _QtechVoiceVlanOuiMask_Type()
)
qtechVoiceVlanOuiMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechVoiceVlanOuiMask.setStatus("current")


class _QtechVoiceVlanOuiDescription_Type(OctetString):
    """Custom type qtechVoiceVlanOuiDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_QtechVoiceVlanOuiDescription_Type.__name__ = "OctetString"
_QtechVoiceVlanOuiDescription_Object = MibTableColumn
qtechVoiceVlanOuiDescription = _QtechVoiceVlanOuiDescription_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 52, 1, 1, 1, 3),
    _QtechVoiceVlanOuiDescription_Type()
)
qtechVoiceVlanOuiDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechVoiceVlanOuiDescription.setStatus("current")
_QtechVoiceVlanOuiRowStatus_Type = RowStatus
_QtechVoiceVlanOuiRowStatus_Object = MibTableColumn
qtechVoiceVlanOuiRowStatus = _QtechVoiceVlanOuiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 52, 1, 1, 1, 4),
    _QtechVoiceVlanOuiRowStatus_Type()
)
qtechVoiceVlanOuiRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechVoiceVlanOuiRowStatus.setStatus("current")
_QtechVoiceVlanEnabledId_Type = Integer32
_QtechVoiceVlanEnabledId_Object = MibScalar
qtechVoiceVlanEnabledId = _QtechVoiceVlanEnabledId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 52, 1, 2),
    _QtechVoiceVlanEnabledId_Type()
)
qtechVoiceVlanEnabledId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechVoiceVlanEnabledId.setStatus("current")
_QtechVoiceVlanPortEnableTable_Object = MibTable
qtechVoiceVlanPortEnableTable = _QtechVoiceVlanPortEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 52, 1, 3)
)
if mibBuilder.loadTexts:
    qtechVoiceVlanPortEnableTable.setStatus("current")
_QtechVoiceVlanPortEnableEntry_Object = MibTableRow
qtechVoiceVlanPortEnableEntry = _QtechVoiceVlanPortEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 52, 1, 3, 1)
)
qtechVoiceVlanPortEnableEntry.setIndexNames(
    (0, "QTECH-VOICE-VLAN-MIB", "qtechVoiceVlanPortEnableIfIndex"),
)
if mibBuilder.loadTexts:
    qtechVoiceVlanPortEnableEntry.setStatus("current")
_QtechVoiceVlanPortEnableIfIndex_Type = IfIndex
_QtechVoiceVlanPortEnableIfIndex_Object = MibTableColumn
qtechVoiceVlanPortEnableIfIndex = _QtechVoiceVlanPortEnableIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 52, 1, 3, 1, 1),
    _QtechVoiceVlanPortEnableIfIndex_Type()
)
qtechVoiceVlanPortEnableIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechVoiceVlanPortEnableIfIndex.setStatus("current")
_QtechVoiceVlanPortStatus_Type = EnabledStatus
_QtechVoiceVlanPortStatus_Object = MibTableColumn
qtechVoiceVlanPortStatus = _QtechVoiceVlanPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 52, 1, 3, 1, 2),
    _QtechVoiceVlanPortStatus_Type()
)
qtechVoiceVlanPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechVoiceVlanPortStatus.setStatus("current")


class _QtechVoiceVlanAgingTime_Type(Integer32):
    """Custom type qtechVoiceVlanAgingTime based on Integer32"""
    defaultValue = 1440

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 10000),
    )


_QtechVoiceVlanAgingTime_Type.__name__ = "Integer32"
_QtechVoiceVlanAgingTime_Object = MibScalar
qtechVoiceVlanAgingTime = _QtechVoiceVlanAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 52, 1, 4),
    _QtechVoiceVlanAgingTime_Type()
)
qtechVoiceVlanAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechVoiceVlanAgingTime.setStatus("current")


class _QtechVoiceVlanSecurityState_Type(Integer32):
    """Custom type qtechVoiceVlanSecurityState based on Integer32"""
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


_QtechVoiceVlanSecurityState_Type.__name__ = "Integer32"
_QtechVoiceVlanSecurityState_Object = MibScalar
qtechVoiceVlanSecurityState = _QtechVoiceVlanSecurityState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 52, 1, 5),
    _QtechVoiceVlanSecurityState_Type()
)
qtechVoiceVlanSecurityState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechVoiceVlanSecurityState.setStatus("current")


class _QtechVoiceVlanCos_Type(Integer32):
    """Custom type qtechVoiceVlanCos based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QtechVoiceVlanCos_Type.__name__ = "Integer32"
_QtechVoiceVlanCos_Object = MibScalar
qtechVoiceVlanCos = _QtechVoiceVlanCos_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 52, 1, 6),
    _QtechVoiceVlanCos_Type()
)
qtechVoiceVlanCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechVoiceVlanCos.setStatus("current")


class _QtechVoiceVlanDscp_Type(Integer32):
    """Custom type qtechVoiceVlanDscp based on Integer32"""
    defaultValue = 46


_QtechVoiceVlanDscp_Type.__name__ = "Integer32"
_QtechVoiceVlanDscp_Object = MibScalar
qtechVoiceVlanDscp = _QtechVoiceVlanDscp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 52, 1, 7),
    _QtechVoiceVlanDscp_Type()
)
qtechVoiceVlanDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechVoiceVlanDscp.setStatus("current")
_QtechVoiceVlanPortModeTable_Object = MibTable
qtechVoiceVlanPortModeTable = _QtechVoiceVlanPortModeTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 52, 1, 8)
)
if mibBuilder.loadTexts:
    qtechVoiceVlanPortModeTable.setStatus("current")
_QtechVoiceVlanPortModeEntry_Object = MibTableRow
qtechVoiceVlanPortModeEntry = _QtechVoiceVlanPortModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 52, 1, 8, 1)
)
qtechVoiceVlanPortModeEntry.setIndexNames(
    (0, "QTECH-VOICE-VLAN-MIB", "qtechVoiceVlanPortIfIndex"),
)
if mibBuilder.loadTexts:
    qtechVoiceVlanPortModeEntry.setStatus("current")
_QtechVoiceVlanPortIfIndex_Type = IfIndex
_QtechVoiceVlanPortIfIndex_Object = MibTableColumn
qtechVoiceVlanPortIfIndex = _QtechVoiceVlanPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 52, 1, 8, 1, 1),
    _QtechVoiceVlanPortIfIndex_Type()
)
qtechVoiceVlanPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechVoiceVlanPortIfIndex.setStatus("current")


class _QtechVoiceVlanPortMode_Type(Integer32):
    """Custom type qtechVoiceVlanPortMode based on Integer32"""
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


_QtechVoiceVlanPortMode_Type.__name__ = "Integer32"
_QtechVoiceVlanPortMode_Object = MibTableColumn
qtechVoiceVlanPortMode = _QtechVoiceVlanPortMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 52, 1, 8, 1, 2),
    _QtechVoiceVlanPortMode_Type()
)
qtechVoiceVlanPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechVoiceVlanPortMode.setStatus("current")
_QtechVoiceVlanMacTable_Object = MibTable
qtechVoiceVlanMacTable = _QtechVoiceVlanMacTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 52, 1, 9)
)
if mibBuilder.loadTexts:
    qtechVoiceVlanMacTable.setStatus("current")
_QtechVoiceVlanMacEntry_Object = MibTableRow
qtechVoiceVlanMacEntry = _QtechVoiceVlanMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 52, 1, 9, 1)
)
qtechVoiceVlanMacEntry.setIndexNames(
    (0, "QTECH-VOICE-VLAN-MIB", "qtechVoiceVlanMacAddress"),
    (0, "QTECH-VOICE-VLAN-MIB", "qtechVoiceVlanMacIfIndex"),
)
if mibBuilder.loadTexts:
    qtechVoiceVlanMacEntry.setStatus("current")
_QtechVoiceVlanMacAddress_Type = MacAddress
_QtechVoiceVlanMacAddress_Object = MibTableColumn
qtechVoiceVlanMacAddress = _QtechVoiceVlanMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 52, 1, 9, 1, 1),
    _QtechVoiceVlanMacAddress_Type()
)
qtechVoiceVlanMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVoiceVlanMacAddress.setStatus("current")
_QtechVoiceVlanMacIfIndex_Type = IfIndex
_QtechVoiceVlanMacIfIndex_Object = MibTableColumn
qtechVoiceVlanMacIfIndex = _QtechVoiceVlanMacIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 52, 1, 9, 1, 2),
    _QtechVoiceVlanMacIfIndex_Type()
)
qtechVoiceVlanMacIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVoiceVlanMacIfIndex.setStatus("current")


class _QtechVoiceVlanMacDescription_Type(OctetString):
    """Custom type qtechVoiceVlanMacDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_QtechVoiceVlanMacDescription_Type.__name__ = "OctetString"
_QtechVoiceVlanMacDescription_Object = MibTableColumn
qtechVoiceVlanMacDescription = _QtechVoiceVlanMacDescription_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 52, 1, 9, 1, 3),
    _QtechVoiceVlanMacDescription_Type()
)
qtechVoiceVlanMacDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVoiceVlanMacDescription.setStatus("current")
_QtechVoiceVlanMIBConformance_ObjectIdentity = ObjectIdentity
qtechVoiceVlanMIBConformance = _QtechVoiceVlanMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 52, 2)
)
_QtechVoiceVlanMIBCompliances_ObjectIdentity = ObjectIdentity
qtechVoiceVlanMIBCompliances = _QtechVoiceVlanMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 52, 2, 1)
)
_QtechVoiceVlanMIBGroups_ObjectIdentity = ObjectIdentity
qtechVoiceVlanMIBGroups = _QtechVoiceVlanMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 52, 2, 2)
)

# Managed Objects groups

qtechVoiceVlanMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 52, 2, 2, 1)
)
qtechVoiceVlanMIBGroup.setObjects(
      *(("QTECH-VOICE-VLAN-MIB", "qtechVoiceVlanOuiAddress"),
        ("QTECH-VOICE-VLAN-MIB", "qtechVoiceVlanOuiMask"),
        ("QTECH-VOICE-VLAN-MIB", "qtechVoiceVlanOuiDescription"),
        ("QTECH-VOICE-VLAN-MIB", "qtechVoiceVlanOuiRowStatus"),
        ("QTECH-VOICE-VLAN-MIB", "qtechVoiceVlanEnabledId"),
        ("QTECH-VOICE-VLAN-MIB", "qtechVoiceVlanPortStatus"),
        ("QTECH-VOICE-VLAN-MIB", "qtechVoiceVlanAgingTime"),
        ("QTECH-VOICE-VLAN-MIB", "qtechVoiceVlanSecurityState"),
        ("QTECH-VOICE-VLAN-MIB", "qtechVoiceVlanCos"),
        ("QTECH-VOICE-VLAN-MIB", "qtechVoiceVlanDscp"),
        ("QTECH-VOICE-VLAN-MIB", "qtechVoiceVlanPortMode"),
        ("QTECH-VOICE-VLAN-MIB", "qtechVoiceVlanMacAddress"),
        ("QTECH-VOICE-VLAN-MIB", "qtechVoiceVlanMacIfIndex"),
        ("QTECH-VOICE-VLAN-MIB", "qtechVoiceVlanMacDescription"))
)
if mibBuilder.loadTexts:
    qtechVoiceVlanMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechVoiceVlanMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 52, 2, 1, 1)
)
qtechVoiceVlanMIBCompliance.setObjects(
    ("QTECH-VOICE-VLAN-MIB", "qtechVoiceVlanMIBGroup")
)
if mibBuilder.loadTexts:
    qtechVoiceVlanMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-VOICE-VLAN-MIB",
    **{"qtechVoiceVlanMIB": qtechVoiceVlanMIB,
       "qtechVoiceVlanMIBObjects": qtechVoiceVlanMIBObjects,
       "qtechVoiceVlanOuiTable": qtechVoiceVlanOuiTable,
       "qtechVoiceVlanOuiEntry": qtechVoiceVlanOuiEntry,
       "qtechVoiceVlanOuiAddress": qtechVoiceVlanOuiAddress,
       "qtechVoiceVlanOuiMask": qtechVoiceVlanOuiMask,
       "qtechVoiceVlanOuiDescription": qtechVoiceVlanOuiDescription,
       "qtechVoiceVlanOuiRowStatus": qtechVoiceVlanOuiRowStatus,
       "qtechVoiceVlanEnabledId": qtechVoiceVlanEnabledId,
       "qtechVoiceVlanPortEnableTable": qtechVoiceVlanPortEnableTable,
       "qtechVoiceVlanPortEnableEntry": qtechVoiceVlanPortEnableEntry,
       "qtechVoiceVlanPortEnableIfIndex": qtechVoiceVlanPortEnableIfIndex,
       "qtechVoiceVlanPortStatus": qtechVoiceVlanPortStatus,
       "qtechVoiceVlanAgingTime": qtechVoiceVlanAgingTime,
       "qtechVoiceVlanSecurityState": qtechVoiceVlanSecurityState,
       "qtechVoiceVlanCos": qtechVoiceVlanCos,
       "qtechVoiceVlanDscp": qtechVoiceVlanDscp,
       "qtechVoiceVlanPortModeTable": qtechVoiceVlanPortModeTable,
       "qtechVoiceVlanPortModeEntry": qtechVoiceVlanPortModeEntry,
       "qtechVoiceVlanPortIfIndex": qtechVoiceVlanPortIfIndex,
       "qtechVoiceVlanPortMode": qtechVoiceVlanPortMode,
       "qtechVoiceVlanMacTable": qtechVoiceVlanMacTable,
       "qtechVoiceVlanMacEntry": qtechVoiceVlanMacEntry,
       "qtechVoiceVlanMacAddress": qtechVoiceVlanMacAddress,
       "qtechVoiceVlanMacIfIndex": qtechVoiceVlanMacIfIndex,
       "qtechVoiceVlanMacDescription": qtechVoiceVlanMacDescription,
       "qtechVoiceVlanMIBConformance": qtechVoiceVlanMIBConformance,
       "qtechVoiceVlanMIBCompliances": qtechVoiceVlanMIBCompliances,
       "qtechVoiceVlanMIBCompliance": qtechVoiceVlanMIBCompliance,
       "qtechVoiceVlanMIBGroups": qtechVoiceVlanMIBGroups,
       "qtechVoiceVlanMIBGroup": qtechVoiceVlanMIBGroup}
)
