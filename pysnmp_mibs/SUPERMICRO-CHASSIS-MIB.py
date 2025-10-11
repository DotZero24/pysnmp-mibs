# SNMP MIB module (SUPERMICRO-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-CHASSIS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:03:12 2025
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

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

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

mbsmIssGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 81, 100)
)
if mibBuilder.loadTexts:
    mbsmIssGroup.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MbsmIssScalarGroup_ObjectIdentity = ObjectIdentity
mbsmIssScalarGroup = _MbsmIssScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 81, 100, 1)
)


class _MbsmMaxNumOfLCSlots_Type(Integer32):
    """Custom type mbsmMaxNumOfLCSlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MbsmMaxNumOfLCSlots_Type.__name__ = "Integer32"
_MbsmMaxNumOfLCSlots_Object = MibScalar
mbsmMaxNumOfLCSlots = _MbsmMaxNumOfLCSlots_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 81, 100, 1, 1),
    _MbsmMaxNumOfLCSlots_Type()
)
mbsmMaxNumOfLCSlots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbsmMaxNumOfLCSlots.setStatus("current")


class _MbsmMaxNumOfSlots_Type(Integer32):
    """Custom type mbsmMaxNumOfSlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MbsmMaxNumOfSlots_Type.__name__ = "Integer32"
_MbsmMaxNumOfSlots_Object = MibScalar
mbsmMaxNumOfSlots = _MbsmMaxNumOfSlots_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 81, 100, 1, 2),
    _MbsmMaxNumOfSlots_Type()
)
mbsmMaxNumOfSlots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbsmMaxNumOfSlots.setStatus("current")


class _MbsmMaxNumOfPortsPerLC_Type(Integer32):
    """Custom type mbsmMaxNumOfPortsPerLC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MbsmMaxNumOfPortsPerLC_Type.__name__ = "Integer32"
_MbsmMaxNumOfPortsPerLC_Object = MibScalar
mbsmMaxNumOfPortsPerLC = _MbsmMaxNumOfPortsPerLC_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 81, 100, 1, 3),
    _MbsmMaxNumOfPortsPerLC_Type()
)
mbsmMaxNumOfPortsPerLC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbsmMaxNumOfPortsPerLC.setStatus("current")


class _MbsmLoadSharingFlag_Type(Integer32):
    """Custom type mbsmLoadSharingFlag based on Integer32"""
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


_MbsmLoadSharingFlag_Type.__name__ = "Integer32"
_MbsmLoadSharingFlag_Object = MibScalar
mbsmLoadSharingFlag = _MbsmLoadSharingFlag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 81, 100, 1, 4),
    _MbsmLoadSharingFlag_Type()
)
mbsmLoadSharingFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbsmLoadSharingFlag.setStatus("current")
_MbsmSlotModuleMapTable_Object = MibTable
mbsmSlotModuleMapTable = _MbsmSlotModuleMapTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 81, 100, 2)
)
if mibBuilder.loadTexts:
    mbsmSlotModuleMapTable.setStatus("current")
_MbsmSlotModuleMapEntry_Object = MibTableRow
mbsmSlotModuleMapEntry = _MbsmSlotModuleMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 81, 100, 2, 1)
)
mbsmSlotModuleMapEntry.setIndexNames(
    (0, "SUPERMICRO-CHASSIS-MIB", "mbsmSlotId"),
)
if mibBuilder.loadTexts:
    mbsmSlotModuleMapEntry.setStatus("current")


class _MbsmSlotId_Type(Integer32):
    """Custom type mbsmSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MbsmSlotId_Type.__name__ = "Integer32"
_MbsmSlotId_Object = MibTableColumn
mbsmSlotId = _MbsmSlotId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 81, 100, 2, 1, 1),
    _MbsmSlotId_Type()
)
mbsmSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbsmSlotId.setStatus("current")


class _MbsmSlotModuleType_Type(Integer32):
    """Custom type mbsmSlotModuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lineCard", 1),
          ("controlCard", 2))
    )


_MbsmSlotModuleType_Type.__name__ = "Integer32"
_MbsmSlotModuleType_Object = MibTableColumn
mbsmSlotModuleType = _MbsmSlotModuleType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 81, 100, 2, 1, 2),
    _MbsmSlotModuleType_Type()
)
mbsmSlotModuleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mbsmSlotModuleType.setStatus("current")
_MbsmSlotModuleStatus_Type = RowStatus
_MbsmSlotModuleStatus_Object = MibTableColumn
mbsmSlotModuleStatus = _MbsmSlotModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 81, 100, 2, 1, 3),
    _MbsmSlotModuleStatus_Type()
)
mbsmSlotModuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mbsmSlotModuleStatus.setStatus("current")
_MbsmLCTypeTable_Object = MibTable
mbsmLCTypeTable = _MbsmLCTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 81, 100, 3)
)
if mibBuilder.loadTexts:
    mbsmLCTypeTable.setStatus("current")
_MbsmLCTypeEntry_Object = MibTableRow
mbsmLCTypeEntry = _MbsmLCTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 81, 100, 3, 1)
)
mbsmLCTypeEntry.setIndexNames(
    (0, "SUPERMICRO-CHASSIS-MIB", "mbsmLCIndex"),
)
if mibBuilder.loadTexts:
    mbsmLCTypeEntry.setStatus("current")


class _MbsmLCIndex_Type(Integer32):
    """Custom type mbsmLCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MbsmLCIndex_Type.__name__ = "Integer32"
_MbsmLCIndex_Object = MibTableColumn
mbsmLCIndex = _MbsmLCIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 81, 100, 3, 1, 1),
    _MbsmLCIndex_Type()
)
mbsmLCIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbsmLCIndex.setStatus("current")


class _MbsmLCName_Type(DisplayString):
    """Custom type mbsmLCName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MbsmLCName_Type.__name__ = "DisplayString"
_MbsmLCName_Object = MibTableColumn
mbsmLCName = _MbsmLCName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 81, 100, 3, 1, 2),
    _MbsmLCName_Type()
)
mbsmLCName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mbsmLCName.setStatus("current")


class _MbsmLCMaxPorts_Type(Integer32):
    """Custom type mbsmLCMaxPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MbsmLCMaxPorts_Type.__name__ = "Integer32"
_MbsmLCMaxPorts_Object = MibTableColumn
mbsmLCMaxPorts = _MbsmLCMaxPorts_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 81, 100, 3, 1, 3),
    _MbsmLCMaxPorts_Type()
)
mbsmLCMaxPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mbsmLCMaxPorts.setStatus("current")
_MbsmLCRowStatus_Type = RowStatus
_MbsmLCRowStatus_Object = MibTableColumn
mbsmLCRowStatus = _MbsmLCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 81, 100, 3, 1, 4),
    _MbsmLCRowStatus_Type()
)
mbsmLCRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mbsmLCRowStatus.setStatus("current")
_MbsmLCPortInfoTable_Object = MibTable
mbsmLCPortInfoTable = _MbsmLCPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 81, 100, 4)
)
if mibBuilder.loadTexts:
    mbsmLCPortInfoTable.setStatus("current")
_MbsmLCPortInfoEntry_Object = MibTableRow
mbsmLCPortInfoEntry = _MbsmLCPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 81, 100, 4, 1)
)
mbsmLCPortInfoEntry.setIndexNames(
    (0, "SUPERMICRO-CHASSIS-MIB", "mbsmLCIndex"),
    (0, "SUPERMICRO-CHASSIS-MIB", "mbsmLCPortIndex"),
)
if mibBuilder.loadTexts:
    mbsmLCPortInfoEntry.setStatus("current")


class _MbsmLCPortIndex_Type(Integer32):
    """Custom type mbsmLCPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MbsmLCPortIndex_Type.__name__ = "Integer32"
_MbsmLCPortIndex_Object = MibTableColumn
mbsmLCPortIndex = _MbsmLCPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 81, 100, 4, 1, 1),
    _MbsmLCPortIndex_Type()
)
mbsmLCPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbsmLCPortIndex.setStatus("current")
_MbsmLCPortIfType_Type = IANAifType
_MbsmLCPortIfType_Object = MibTableColumn
mbsmLCPortIfType = _MbsmLCPortIfType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 81, 100, 4, 1, 2),
    _MbsmLCPortIfType_Type()
)
mbsmLCPortIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbsmLCPortIfType.setStatus("current")
_MbsmLCPortSpeed_Type = Gauge32
_MbsmLCPortSpeed_Object = MibTableColumn
mbsmLCPortSpeed = _MbsmLCPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 81, 100, 4, 1, 3),
    _MbsmLCPortSpeed_Type()
)
mbsmLCPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbsmLCPortSpeed.setStatus("current")
_MbsmLCPortHighSpeed_Type = Gauge32
_MbsmLCPortHighSpeed_Object = MibTableColumn
mbsmLCPortHighSpeed = _MbsmLCPortHighSpeed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 81, 100, 4, 1, 4),
    _MbsmLCPortHighSpeed_Type()
)
mbsmLCPortHighSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbsmLCPortHighSpeed.setStatus("current")
_MbsmLCConfigTable_Object = MibTable
mbsmLCConfigTable = _MbsmLCConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 81, 100, 5)
)
if mibBuilder.loadTexts:
    mbsmLCConfigTable.setStatus("current")
_MbsmLCConfigEntry_Object = MibTableRow
mbsmLCConfigEntry = _MbsmLCConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 81, 100, 5, 1)
)
mbsmLCConfigEntry.setIndexNames(
    (0, "SUPERMICRO-CHASSIS-MIB", "mbsmLCConfigSlotId"),
)
if mibBuilder.loadTexts:
    mbsmLCConfigEntry.setStatus("current")


class _MbsmLCConfigSlotId_Type(Integer32):
    """Custom type mbsmLCConfigSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MbsmLCConfigSlotId_Type.__name__ = "Integer32"
_MbsmLCConfigSlotId_Object = MibTableColumn
mbsmLCConfigSlotId = _MbsmLCConfigSlotId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 81, 100, 5, 1, 1),
    _MbsmLCConfigSlotId_Type()
)
mbsmLCConfigSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbsmLCConfigSlotId.setStatus("current")
_MbsmLCConfigCardName_Type = DisplayString
_MbsmLCConfigCardName_Object = MibTableColumn
mbsmLCConfigCardName = _MbsmLCConfigCardName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 81, 100, 5, 1, 2),
    _MbsmLCConfigCardName_Type()
)
mbsmLCConfigCardName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mbsmLCConfigCardName.setStatus("current")


class _MbsmLCConfigStatus_Type(Integer32):
    """Custom type mbsmLCConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 0),
          ("static", 1))
    )


_MbsmLCConfigStatus_Type.__name__ = "Integer32"
_MbsmLCConfigStatus_Object = MibTableColumn
mbsmLCConfigStatus = _MbsmLCConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 81, 100, 5, 1, 3),
    _MbsmLCConfigStatus_Type()
)
mbsmLCConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mbsmLCConfigStatus.setStatus("current")
_MbsmIssTrapGroup_ObjectIdentity = ObjectIdentity
mbsmIssTrapGroup = _MbsmIssTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 81, 100, 6)
)

# Managed Objects groups


# Notification objects

mbsmConfigErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 81, 100, 6, 1)
)
mbsmConfigErrTrap.setObjects(
      *(("SUPERMICRO-CHASSIS-MIB", "mbsmSlotId"),
        ("SUPERMICRO-CHASSIS-MIB", "mbsmSlotModuleType"),
        ("SUPERMICRO-CHASSIS-MIB", "mbsmSlotModuleStatus"),
        ("SUPERMICRO-CHASSIS-MIB", "mbsmLCConfigCardName"))
)
if mibBuilder.loadTexts:
    mbsmConfigErrTrap.setStatus(
        "current"
    )

mbsmCardInsertedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 81, 100, 6, 2)
)
mbsmCardInsertedTrap.setObjects(
    ("SUPERMICRO-CHASSIS-MIB", "mbsmSlotId")
)
if mibBuilder.loadTexts:
    mbsmCardInsertedTrap.setStatus(
        "current"
    )

mbsmCardRemovedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 81, 100, 6, 3)
)
mbsmCardRemovedTrap.setObjects(
    ("SUPERMICRO-CHASSIS-MIB", "mbsmSlotId")
)
if mibBuilder.loadTexts:
    mbsmCardRemovedTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-CHASSIS-MIB",
    **{"mbsmIssGroup": mbsmIssGroup,
       "mbsmIssScalarGroup": mbsmIssScalarGroup,
       "mbsmMaxNumOfLCSlots": mbsmMaxNumOfLCSlots,
       "mbsmMaxNumOfSlots": mbsmMaxNumOfSlots,
       "mbsmMaxNumOfPortsPerLC": mbsmMaxNumOfPortsPerLC,
       "mbsmLoadSharingFlag": mbsmLoadSharingFlag,
       "mbsmSlotModuleMapTable": mbsmSlotModuleMapTable,
       "mbsmSlotModuleMapEntry": mbsmSlotModuleMapEntry,
       "mbsmSlotId": mbsmSlotId,
       "mbsmSlotModuleType": mbsmSlotModuleType,
       "mbsmSlotModuleStatus": mbsmSlotModuleStatus,
       "mbsmLCTypeTable": mbsmLCTypeTable,
       "mbsmLCTypeEntry": mbsmLCTypeEntry,
       "mbsmLCIndex": mbsmLCIndex,
       "mbsmLCName": mbsmLCName,
       "mbsmLCMaxPorts": mbsmLCMaxPorts,
       "mbsmLCRowStatus": mbsmLCRowStatus,
       "mbsmLCPortInfoTable": mbsmLCPortInfoTable,
       "mbsmLCPortInfoEntry": mbsmLCPortInfoEntry,
       "mbsmLCPortIndex": mbsmLCPortIndex,
       "mbsmLCPortIfType": mbsmLCPortIfType,
       "mbsmLCPortSpeed": mbsmLCPortSpeed,
       "mbsmLCPortHighSpeed": mbsmLCPortHighSpeed,
       "mbsmLCConfigTable": mbsmLCConfigTable,
       "mbsmLCConfigEntry": mbsmLCConfigEntry,
       "mbsmLCConfigSlotId": mbsmLCConfigSlotId,
       "mbsmLCConfigCardName": mbsmLCConfigCardName,
       "mbsmLCConfigStatus": mbsmLCConfigStatus,
       "mbsmIssTrapGroup": mbsmIssTrapGroup,
       "mbsmConfigErrTrap": mbsmConfigErrTrap,
       "mbsmCardInsertedTrap": mbsmCardInsertedTrap,
       "mbsmCardRemovedTrap": mbsmCardRemovedTrap}
)
