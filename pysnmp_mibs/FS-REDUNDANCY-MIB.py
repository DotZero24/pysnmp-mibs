# SNMP MIB module (FS-REDUNDANCY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-REDUNDANCY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:15:31 2025
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

fsRedundancyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 34)
)
if mibBuilder.loadTexts:
    fsRedundancyMIB.setRevisions(
        ("2003-09-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsRedundancyMIBObjects_ObjectIdentity = ObjectIdentity
fsRedundancyMIBObjects = _FsRedundancyMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 34, 1)
)
_FsRedundancyForceSwitchover_Type = Integer32
_FsRedundancyForceSwitchover_Object = MibScalar
fsRedundancyForceSwitchover = _FsRedundancyForceSwitchover_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 34, 1, 1),
    _FsRedundancyForceSwitchover_Type()
)
fsRedundancyForceSwitchover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRedundancyForceSwitchover.setStatus("current")


class _FsMainCPU_Type(Integer32):
    """Custom type fsMainCPU based on Integer32"""
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


_FsMainCPU_Type.__name__ = "Integer32"
_FsMainCPU_Object = MibScalar
fsMainCPU = _FsMainCPU_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 34, 1, 2),
    _FsMainCPU_Type()
)
fsMainCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMainCPU.setStatus("current")
_FsPluggableMIBObjects_ObjectIdentity = ObjectIdentity
fsPluggableMIBObjects = _FsPluggableMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 34, 2)
)
_FsPluggableModuleInfoTable_Object = MibTable
fsPluggableModuleInfoTable = _FsPluggableModuleInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 34, 2, 1)
)
if mibBuilder.loadTexts:
    fsPluggableModuleInfoTable.setStatus("current")
_FsPluggableModuleInfoEntry_Object = MibTableRow
fsPluggableModuleInfoEntry = _FsPluggableModuleInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 34, 2, 1, 1)
)
fsPluggableModuleInfoEntry.setIndexNames(
    (0, "FS-REDUNDANCY-MIB", "fsPluggableModuleInfoDeviceIndex"),
    (0, "FS-REDUNDANCY-MIB", "fsPluggableModuleInfoSlotIndex"),
)
if mibBuilder.loadTexts:
    fsPluggableModuleInfoEntry.setStatus("current")
_FsPluggableModuleInfoDeviceIndex_Type = Integer32
_FsPluggableModuleInfoDeviceIndex_Object = MibTableColumn
fsPluggableModuleInfoDeviceIndex = _FsPluggableModuleInfoDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 34, 2, 1, 1, 1),
    _FsPluggableModuleInfoDeviceIndex_Type()
)
fsPluggableModuleInfoDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPluggableModuleInfoDeviceIndex.setStatus("current")
_FsPluggableModuleInfoSlotIndex_Type = Integer32
_FsPluggableModuleInfoSlotIndex_Object = MibTableColumn
fsPluggableModuleInfoSlotIndex = _FsPluggableModuleInfoSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 34, 2, 1, 1, 2),
    _FsPluggableModuleInfoSlotIndex_Type()
)
fsPluggableModuleInfoSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPluggableModuleInfoSlotIndex.setStatus("current")


class _FsPluggableModuleStatus_Type(Integer32):
    """Custom type fsPluggableModuleStatus based on Integer32"""
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
          ("cannot-fsup", 7),
          ("resetting", 8),
          ("master", 9),
          ("backup", 10))
    )


_FsPluggableModuleStatus_Type.__name__ = "Integer32"
_FsPluggableModuleStatus_Object = MibTableColumn
fsPluggableModuleStatus = _FsPluggableModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 34, 2, 1, 1, 3),
    _FsPluggableModuleStatus_Type()
)
fsPluggableModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPluggableModuleStatus.setStatus("current")


class _FsPluggableModuleConfigType_Type(Integer32):
    """Custom type fsPluggableModuleConfigType based on Integer32"""
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


_FsPluggableModuleConfigType_Type.__name__ = "Integer32"
_FsPluggableModuleConfigType_Object = MibTableColumn
fsPluggableModuleConfigType = _FsPluggableModuleConfigType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 34, 2, 1, 1, 4),
    _FsPluggableModuleConfigType_Type()
)
fsPluggableModuleConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPluggableModuleConfigType.setStatus("current")


class _FsPluggableModuleConfigSwVer_Type(DisplayString):
    """Custom type fsPluggableModuleConfigSwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsPluggableModuleConfigSwVer_Type.__name__ = "DisplayString"
_FsPluggableModuleConfigSwVer_Object = MibTableColumn
fsPluggableModuleConfigSwVer = _FsPluggableModuleConfigSwVer_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 34, 2, 1, 1, 5),
    _FsPluggableModuleConfigSwVer_Type()
)
fsPluggableModuleConfigSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPluggableModuleConfigSwVer.setStatus("current")


class _FsPluggableModuleOnlineSwVer_Type(DisplayString):
    """Custom type fsPluggableModuleOnlineSwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsPluggableModuleOnlineSwVer_Type.__name__ = "DisplayString"
_FsPluggableModuleOnlineSwVer_Object = MibTableColumn
fsPluggableModuleOnlineSwVer = _FsPluggableModuleOnlineSwVer_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 34, 2, 1, 1, 6),
    _FsPluggableModuleOnlineSwVer_Type()
)
fsPluggableModuleOnlineSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPluggableModuleOnlineSwVer.setStatus("current")


class _FsPluggableModuleConfigInfoDescr_Type(DisplayString):
    """Custom type fsPluggableModuleConfigInfoDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsPluggableModuleConfigInfoDescr_Type.__name__ = "DisplayString"
_FsPluggableModuleConfigInfoDescr_Object = MibTableColumn
fsPluggableModuleConfigInfoDescr = _FsPluggableModuleConfigInfoDescr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 34, 2, 1, 1, 7),
    _FsPluggableModuleConfigInfoDescr_Type()
)
fsPluggableModuleConfigInfoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPluggableModuleConfigInfoDescr.setStatus("current")


class _FsPluggableModuleOnlineInfoDescr_Type(DisplayString):
    """Custom type fsPluggableModuleOnlineInfoDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsPluggableModuleOnlineInfoDescr_Type.__name__ = "DisplayString"
_FsPluggableModuleOnlineInfoDescr_Object = MibTableColumn
fsPluggableModuleOnlineInfoDescr = _FsPluggableModuleOnlineInfoDescr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 34, 2, 1, 1, 8),
    _FsPluggableModuleOnlineInfoDescr_Type()
)
fsPluggableModuleOnlineInfoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPluggableModuleOnlineInfoDescr.setStatus("current")
_FsPluggableModuleConfigPortsNum_Type = Integer32
_FsPluggableModuleConfigPortsNum_Object = MibTableColumn
fsPluggableModuleConfigPortsNum = _FsPluggableModuleConfigPortsNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 34, 2, 1, 1, 9),
    _FsPluggableModuleConfigPortsNum_Type()
)
fsPluggableModuleConfigPortsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPluggableModuleConfigPortsNum.setStatus("current")
_FsPluggableModuleOnlinePortsNum_Type = Integer32
_FsPluggableModuleOnlinePortsNum_Object = MibTableColumn
fsPluggableModuleOnlinePortsNum = _FsPluggableModuleOnlinePortsNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 34, 2, 1, 1, 10),
    _FsPluggableModuleOnlinePortsNum_Type()
)
fsPluggableModuleOnlinePortsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPluggableModuleOnlinePortsNum.setStatus("current")


class _FsPluggableModuleAction_Type(Integer32):
    """Custom type fsPluggableModuleAction based on Integer32"""
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


_FsPluggableModuleAction_Type.__name__ = "Integer32"
_FsPluggableModuleAction_Object = MibTableColumn
fsPluggableModuleAction = _FsPluggableModuleAction_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 34, 2, 1, 1, 11),
    _FsPluggableModuleAction_Type()
)
fsPluggableModuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPluggableModuleAction.setStatus("current")
_FsRedundancyMIBConformance_ObjectIdentity = ObjectIdentity
fsRedundancyMIBConformance = _FsRedundancyMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 34, 3)
)
_FsRedundancyMIBCompliances_ObjectIdentity = ObjectIdentity
fsRedundancyMIBCompliances = _FsRedundancyMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 34, 3, 1)
)
_FsRedundancyMIBGroups_ObjectIdentity = ObjectIdentity
fsRedundancyMIBGroups = _FsRedundancyMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 34, 3, 2)
)

# Managed Objects groups

fsRedundancyMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 34, 3, 2, 1)
)
fsRedundancyMIBGroup.setObjects(
      *(("FS-REDUNDANCY-MIB", "fsRedundancyForceSwitchover"),
        ("FS-REDUNDANCY-MIB", "fsMainCPU"),
        ("FS-REDUNDANCY-MIB", "fsPluggableModuleInfoDeviceIndex"),
        ("FS-REDUNDANCY-MIB", "fsPluggableModuleInfoSlotIndex"),
        ("FS-REDUNDANCY-MIB", "fsPluggableModuleStatus"),
        ("FS-REDUNDANCY-MIB", "fsPluggableModuleConfigType"),
        ("FS-REDUNDANCY-MIB", "fsPluggableModuleConfigSwVer"),
        ("FS-REDUNDANCY-MIB", "fsPluggableModuleOnlineSwVer"),
        ("FS-REDUNDANCY-MIB", "fsPluggableModuleConfigInfoDescr"),
        ("FS-REDUNDANCY-MIB", "fsPluggableModuleOnlineInfoDescr"),
        ("FS-REDUNDANCY-MIB", "fsPluggableModuleConfigPortsNum"),
        ("FS-REDUNDANCY-MIB", "fsPluggableModuleOnlinePortsNum"),
        ("FS-REDUNDANCY-MIB", "fsPluggableModuleAction"))
)
if mibBuilder.loadTexts:
    fsRedundancyMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsRedundancyMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 34, 3, 1, 1)
)
fsRedundancyMIBCompliance.setObjects(
    ("FS-REDUNDANCY-MIB", "fsRedundancyMIBGroup")
)
if mibBuilder.loadTexts:
    fsRedundancyMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-REDUNDANCY-MIB",
    **{"fsRedundancyMIB": fsRedundancyMIB,
       "fsRedundancyMIBObjects": fsRedundancyMIBObjects,
       "fsRedundancyForceSwitchover": fsRedundancyForceSwitchover,
       "fsMainCPU": fsMainCPU,
       "fsPluggableMIBObjects": fsPluggableMIBObjects,
       "fsPluggableModuleInfoTable": fsPluggableModuleInfoTable,
       "fsPluggableModuleInfoEntry": fsPluggableModuleInfoEntry,
       "fsPluggableModuleInfoDeviceIndex": fsPluggableModuleInfoDeviceIndex,
       "fsPluggableModuleInfoSlotIndex": fsPluggableModuleInfoSlotIndex,
       "fsPluggableModuleStatus": fsPluggableModuleStatus,
       "fsPluggableModuleConfigType": fsPluggableModuleConfigType,
       "fsPluggableModuleConfigSwVer": fsPluggableModuleConfigSwVer,
       "fsPluggableModuleOnlineSwVer": fsPluggableModuleOnlineSwVer,
       "fsPluggableModuleConfigInfoDescr": fsPluggableModuleConfigInfoDescr,
       "fsPluggableModuleOnlineInfoDescr": fsPluggableModuleOnlineInfoDescr,
       "fsPluggableModuleConfigPortsNum": fsPluggableModuleConfigPortsNum,
       "fsPluggableModuleOnlinePortsNum": fsPluggableModuleOnlinePortsNum,
       "fsPluggableModuleAction": fsPluggableModuleAction,
       "fsRedundancyMIBConformance": fsRedundancyMIBConformance,
       "fsRedundancyMIBCompliances": fsRedundancyMIBCompliances,
       "fsRedundancyMIBCompliance": fsRedundancyMIBCompliance,
       "fsRedundancyMIBGroups": fsRedundancyMIBGroups,
       "fsRedundancyMIBGroup": fsRedundancyMIBGroup}
)
