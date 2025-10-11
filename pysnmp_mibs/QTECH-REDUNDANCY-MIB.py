# SNMP MIB module (QTECH-REDUNDANCY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-REDUNDANCY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:15 2025
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

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

qtechRedundancyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 34)
)
if mibBuilder.loadTexts:
    qtechRedundancyMIB.setRevisions(
        ("2003-09-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechRedundancyMIBObjects_ObjectIdentity = ObjectIdentity
qtechRedundancyMIBObjects = _QtechRedundancyMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 34, 1)
)
_QtechRedundancyForceSwitchover_Type = Integer32
_QtechRedundancyForceSwitchover_Object = MibScalar
qtechRedundancyForceSwitchover = _QtechRedundancyForceSwitchover_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 34, 1, 1),
    _QtechRedundancyForceSwitchover_Type()
)
qtechRedundancyForceSwitchover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRedundancyForceSwitchover.setStatus("current")


class _QtechMainCPU_Type(Integer32):
    """Custom type qtechMainCPU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("increasing", 0),
          ("decreasing", 1))
    )


_QtechMainCPU_Type.__name__ = "Integer32"
_QtechMainCPU_Object = MibScalar
qtechMainCPU = _QtechMainCPU_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 34, 1, 2),
    _QtechMainCPU_Type()
)
qtechMainCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMainCPU.setStatus("current")
_QtechPluggableMIBObjects_ObjectIdentity = ObjectIdentity
qtechPluggableMIBObjects = _QtechPluggableMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 34, 2)
)
_QtechPluggableModuleInfoTable_Object = MibTable
qtechPluggableModuleInfoTable = _QtechPluggableModuleInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 34, 2, 1)
)
if mibBuilder.loadTexts:
    qtechPluggableModuleInfoTable.setStatus("current")
_QtechPluggableModuleInfoEntry_Object = MibTableRow
qtechPluggableModuleInfoEntry = _QtechPluggableModuleInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 34, 2, 1, 1)
)
qtechPluggableModuleInfoEntry.setIndexNames(
    (0, "QTECH-REDUNDANCY-MIB", "qtechPluggableModuleInfoDeviceIndex"),
    (0, "QTECH-REDUNDANCY-MIB", "qtechPluggableModuleInfoSlotIndex"),
)
if mibBuilder.loadTexts:
    qtechPluggableModuleInfoEntry.setStatus("current")
_QtechPluggableModuleInfoDeviceIndex_Type = Integer32
_QtechPluggableModuleInfoDeviceIndex_Object = MibTableColumn
qtechPluggableModuleInfoDeviceIndex = _QtechPluggableModuleInfoDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 34, 2, 1, 1, 1),
    _QtechPluggableModuleInfoDeviceIndex_Type()
)
qtechPluggableModuleInfoDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPluggableModuleInfoDeviceIndex.setStatus("current")
_QtechPluggableModuleInfoSlotIndex_Type = Integer32
_QtechPluggableModuleInfoSlotIndex_Object = MibTableColumn
qtechPluggableModuleInfoSlotIndex = _QtechPluggableModuleInfoSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 34, 2, 1, 1, 2),
    _QtechPluggableModuleInfoSlotIndex_Type()
)
qtechPluggableModuleInfoSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPluggableModuleInfoSlotIndex.setStatus("current")


class _QtechPluggableModuleStatus_Type(Integer32):
    """Custom type qtechPluggableModuleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("ok", 1),
          ("installed", 2),
          ("conflict", 3),
          ("removed", 4),
          ("uninstalled", 5),
          ("verIncompatible", 6),
          ("cannot-qtechup", 7),
          ("resetting", 8),
          ("master", 9),
          ("backup", 10))
    )


_QtechPluggableModuleStatus_Type.__name__ = "Integer32"
_QtechPluggableModuleStatus_Object = MibTableColumn
qtechPluggableModuleStatus = _QtechPluggableModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 34, 2, 1, 1, 3),
    _QtechPluggableModuleStatus_Type()
)
qtechPluggableModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPluggableModuleStatus.setStatus("current")


class _QtechPluggableModuleConfigType_Type(Integer32):
    """Custom type qtechPluggableModuleConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("m6800-24T-4SFP-4GT", 1),
          ("m6800-32T-4SFP-GT", 2),
          ("m6800-32FMT", 3),
          ("m6800-12GB", 4),
          ("m6800-24SFP", 5),
          ("m6800-12SFP-GT", 6),
          ("m6800-1XENPAK", 7),
          ("m6800-2XENPAK", 8),
          ("m6800-MSC", 9),
          ("m6800-CM", 10),
          ("m6800-24GT-8SFP", 11))
    )


_QtechPluggableModuleConfigType_Type.__name__ = "Integer32"
_QtechPluggableModuleConfigType_Object = MibTableColumn
qtechPluggableModuleConfigType = _QtechPluggableModuleConfigType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 34, 2, 1, 1, 4),
    _QtechPluggableModuleConfigType_Type()
)
qtechPluggableModuleConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPluggableModuleConfigType.setStatus("current")


class _QtechPluggableModuleConfigSwVer_Type(DisplayString):
    """Custom type qtechPluggableModuleConfigSwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechPluggableModuleConfigSwVer_Type.__name__ = "DisplayString"
_QtechPluggableModuleConfigSwVer_Object = MibTableColumn
qtechPluggableModuleConfigSwVer = _QtechPluggableModuleConfigSwVer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 34, 2, 1, 1, 5),
    _QtechPluggableModuleConfigSwVer_Type()
)
qtechPluggableModuleConfigSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPluggableModuleConfigSwVer.setStatus("current")


class _QtechPluggableModuleOnlineSwVer_Type(DisplayString):
    """Custom type qtechPluggableModuleOnlineSwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechPluggableModuleOnlineSwVer_Type.__name__ = "DisplayString"
_QtechPluggableModuleOnlineSwVer_Object = MibTableColumn
qtechPluggableModuleOnlineSwVer = _QtechPluggableModuleOnlineSwVer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 34, 2, 1, 1, 6),
    _QtechPluggableModuleOnlineSwVer_Type()
)
qtechPluggableModuleOnlineSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPluggableModuleOnlineSwVer.setStatus("current")


class _QtechPluggableModuleConfigInfoDescr_Type(DisplayString):
    """Custom type qtechPluggableModuleConfigInfoDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechPluggableModuleConfigInfoDescr_Type.__name__ = "DisplayString"
_QtechPluggableModuleConfigInfoDescr_Object = MibTableColumn
qtechPluggableModuleConfigInfoDescr = _QtechPluggableModuleConfigInfoDescr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 34, 2, 1, 1, 7),
    _QtechPluggableModuleConfigInfoDescr_Type()
)
qtechPluggableModuleConfigInfoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPluggableModuleConfigInfoDescr.setStatus("current")


class _QtechPluggableModuleOnlineInfoDescr_Type(DisplayString):
    """Custom type qtechPluggableModuleOnlineInfoDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechPluggableModuleOnlineInfoDescr_Type.__name__ = "DisplayString"
_QtechPluggableModuleOnlineInfoDescr_Object = MibTableColumn
qtechPluggableModuleOnlineInfoDescr = _QtechPluggableModuleOnlineInfoDescr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 34, 2, 1, 1, 8),
    _QtechPluggableModuleOnlineInfoDescr_Type()
)
qtechPluggableModuleOnlineInfoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPluggableModuleOnlineInfoDescr.setStatus("current")
_QtechPluggableModuleConfigPortsNum_Type = Integer32
_QtechPluggableModuleConfigPortsNum_Object = MibTableColumn
qtechPluggableModuleConfigPortsNum = _QtechPluggableModuleConfigPortsNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 34, 2, 1, 1, 9),
    _QtechPluggableModuleConfigPortsNum_Type()
)
qtechPluggableModuleConfigPortsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPluggableModuleConfigPortsNum.setStatus("current")
_QtechPluggableModuleOnlinePortsNum_Type = Integer32
_QtechPluggableModuleOnlinePortsNum_Object = MibTableColumn
qtechPluggableModuleOnlinePortsNum = _QtechPluggableModuleOnlinePortsNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 34, 2, 1, 1, 10),
    _QtechPluggableModuleOnlinePortsNum_Type()
)
qtechPluggableModuleOnlinePortsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPluggableModuleOnlinePortsNum.setStatus("current")


class _QtechPluggableModuleAction_Type(Integer32):
    """Custom type qtechPluggableModuleAction based on Integer32"""
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
          ("reset", 1),
          ("clearAllConf", 2),
          ("uninstall", 3))
    )


_QtechPluggableModuleAction_Type.__name__ = "Integer32"
_QtechPluggableModuleAction_Object = MibTableColumn
qtechPluggableModuleAction = _QtechPluggableModuleAction_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 34, 2, 1, 1, 11),
    _QtechPluggableModuleAction_Type()
)
qtechPluggableModuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPluggableModuleAction.setStatus("current")
_QtechRedundancyMIBConformance_ObjectIdentity = ObjectIdentity
qtechRedundancyMIBConformance = _QtechRedundancyMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 34, 3)
)
_QtechRedundancyMIBCompliances_ObjectIdentity = ObjectIdentity
qtechRedundancyMIBCompliances = _QtechRedundancyMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 34, 3, 1)
)
_QtechRedundancyMIBGroups_ObjectIdentity = ObjectIdentity
qtechRedundancyMIBGroups = _QtechRedundancyMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 34, 3, 2)
)

# Managed Objects groups

qtechRedundancyMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 34, 3, 2, 1)
)
qtechRedundancyMIBGroup.setObjects(
      *(("QTECH-REDUNDANCY-MIB", "qtechRedundancyForceSwitchover"),
        ("QTECH-REDUNDANCY-MIB", "qtechMainCPU"),
        ("QTECH-REDUNDANCY-MIB", "qtechPluggableModuleInfoDeviceIndex"),
        ("QTECH-REDUNDANCY-MIB", "qtechPluggableModuleInfoSlotIndex"),
        ("QTECH-REDUNDANCY-MIB", "qtechPluggableModuleStatus"),
        ("QTECH-REDUNDANCY-MIB", "qtechPluggableModuleConfigType"),
        ("QTECH-REDUNDANCY-MIB", "qtechPluggableModuleConfigSwVer"),
        ("QTECH-REDUNDANCY-MIB", "qtechPluggableModuleOnlineSwVer"),
        ("QTECH-REDUNDANCY-MIB", "qtechPluggableModuleConfigInfoDescr"),
        ("QTECH-REDUNDANCY-MIB", "qtechPluggableModuleOnlineInfoDescr"),
        ("QTECH-REDUNDANCY-MIB", "qtechPluggableModuleConfigPortsNum"),
        ("QTECH-REDUNDANCY-MIB", "qtechPluggableModuleOnlinePortsNum"),
        ("QTECH-REDUNDANCY-MIB", "qtechPluggableModuleAction"))
)
if mibBuilder.loadTexts:
    qtechRedundancyMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechRedundancyMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 34, 3, 1, 1)
)
qtechRedundancyMIBCompliance.setObjects(
    ("QTECH-REDUNDANCY-MIB", "qtechRedundancyMIBGroup")
)
if mibBuilder.loadTexts:
    qtechRedundancyMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-REDUNDANCY-MIB",
    **{"qtechRedundancyMIB": qtechRedundancyMIB,
       "qtechRedundancyMIBObjects": qtechRedundancyMIBObjects,
       "qtechRedundancyForceSwitchover": qtechRedundancyForceSwitchover,
       "qtechMainCPU": qtechMainCPU,
       "qtechPluggableMIBObjects": qtechPluggableMIBObjects,
       "qtechPluggableModuleInfoTable": qtechPluggableModuleInfoTable,
       "qtechPluggableModuleInfoEntry": qtechPluggableModuleInfoEntry,
       "qtechPluggableModuleInfoDeviceIndex": qtechPluggableModuleInfoDeviceIndex,
       "qtechPluggableModuleInfoSlotIndex": qtechPluggableModuleInfoSlotIndex,
       "qtechPluggableModuleStatus": qtechPluggableModuleStatus,
       "qtechPluggableModuleConfigType": qtechPluggableModuleConfigType,
       "qtechPluggableModuleConfigSwVer": qtechPluggableModuleConfigSwVer,
       "qtechPluggableModuleOnlineSwVer": qtechPluggableModuleOnlineSwVer,
       "qtechPluggableModuleConfigInfoDescr": qtechPluggableModuleConfigInfoDescr,
       "qtechPluggableModuleOnlineInfoDescr": qtechPluggableModuleOnlineInfoDescr,
       "qtechPluggableModuleConfigPortsNum": qtechPluggableModuleConfigPortsNum,
       "qtechPluggableModuleOnlinePortsNum": qtechPluggableModuleOnlinePortsNum,
       "qtechPluggableModuleAction": qtechPluggableModuleAction,
       "qtechRedundancyMIBConformance": qtechRedundancyMIBConformance,
       "qtechRedundancyMIBCompliances": qtechRedundancyMIBCompliances,
       "qtechRedundancyMIBCompliance": qtechRedundancyMIBCompliance,
       "qtechRedundancyMIBGroups": qtechRedundancyMIBGroups,
       "qtechRedundancyMIBGroup": qtechRedundancyMIBGroup}
)
