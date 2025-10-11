# SNMP MIB module (DES7200-REDUNDANCY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DES7200-REDUNDANCY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:48:36 2025
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

(myMgmt,) = mibBuilder.importSymbols(
    "DES7200-SMI",
    "myMgmt")

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

myRedundancyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 34)
)
if mibBuilder.loadTexts:
    myRedundancyMIB.setRevisions(
        ("2003-09-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MyRedundancyMIBObjects_ObjectIdentity = ObjectIdentity
myRedundancyMIBObjects = _MyRedundancyMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 34, 1)
)
_MyRedundancyForceSwitchover_Type = Integer32
_MyRedundancyForceSwitchover_Object = MibScalar
myRedundancyForceSwitchover = _MyRedundancyForceSwitchover_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 34, 1, 1),
    _MyRedundancyForceSwitchover_Type()
)
myRedundancyForceSwitchover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myRedundancyForceSwitchover.setStatus("current")


class _MyMainCPU_Type(Integer32):
    """Custom type myMainCPU based on Integer32"""
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


_MyMainCPU_Type.__name__ = "Integer32"
_MyMainCPU_Object = MibScalar
myMainCPU = _MyMainCPU_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 34, 1, 2),
    _MyMainCPU_Type()
)
myMainCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myMainCPU.setStatus("current")
_MyPluggableMIBObjects_ObjectIdentity = ObjectIdentity
myPluggableMIBObjects = _MyPluggableMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 34, 2)
)
_MyPluggableModuleInfoTable_Object = MibTable
myPluggableModuleInfoTable = _MyPluggableModuleInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 34, 2, 1)
)
if mibBuilder.loadTexts:
    myPluggableModuleInfoTable.setStatus("current")
_MyPluggableModuleInfoEntry_Object = MibTableRow
myPluggableModuleInfoEntry = _MyPluggableModuleInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 34, 2, 1, 1)
)
myPluggableModuleInfoEntry.setIndexNames(
    (0, "DES7200-REDUNDANCY-MIB", "myPluggableModuleInfoDeviceIndex"),
    (0, "DES7200-REDUNDANCY-MIB", "myPluggableModuleInfoSlotIndex"),
)
if mibBuilder.loadTexts:
    myPluggableModuleInfoEntry.setStatus("current")
_MyPluggableModuleInfoDeviceIndex_Type = Integer32
_MyPluggableModuleInfoDeviceIndex_Object = MibTableColumn
myPluggableModuleInfoDeviceIndex = _MyPluggableModuleInfoDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 34, 2, 1, 1, 1),
    _MyPluggableModuleInfoDeviceIndex_Type()
)
myPluggableModuleInfoDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myPluggableModuleInfoDeviceIndex.setStatus("current")
_MyPluggableModuleInfoSlotIndex_Type = Integer32
_MyPluggableModuleInfoSlotIndex_Object = MibTableColumn
myPluggableModuleInfoSlotIndex = _MyPluggableModuleInfoSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 34, 2, 1, 1, 2),
    _MyPluggableModuleInfoSlotIndex_Type()
)
myPluggableModuleInfoSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myPluggableModuleInfoSlotIndex.setStatus("current")


class _MyPluggableModuleStatus_Type(Integer32):
    """Custom type myPluggableModuleStatus based on Integer32"""
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
          ("cannot-myup", 7),
          ("resetting", 8),
          ("master", 9),
          ("backup", 10))
    )


_MyPluggableModuleStatus_Type.__name__ = "Integer32"
_MyPluggableModuleStatus_Object = MibTableColumn
myPluggableModuleStatus = _MyPluggableModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 34, 2, 1, 1, 3),
    _MyPluggableModuleStatus_Type()
)
myPluggableModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myPluggableModuleStatus.setStatus("current")


class _MyPluggableModuleConfigType_Type(Integer32):
    """Custom type myPluggableModuleConfigType based on Integer32"""
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


_MyPluggableModuleConfigType_Type.__name__ = "Integer32"
_MyPluggableModuleConfigType_Object = MibTableColumn
myPluggableModuleConfigType = _MyPluggableModuleConfigType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 34, 2, 1, 1, 4),
    _MyPluggableModuleConfigType_Type()
)
myPluggableModuleConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myPluggableModuleConfigType.setStatus("current")


class _MyPluggableModuleConfigSwVer_Type(DisplayString):
    """Custom type myPluggableModuleConfigSwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MyPluggableModuleConfigSwVer_Type.__name__ = "DisplayString"
_MyPluggableModuleConfigSwVer_Object = MibTableColumn
myPluggableModuleConfigSwVer = _MyPluggableModuleConfigSwVer_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 34, 2, 1, 1, 5),
    _MyPluggableModuleConfigSwVer_Type()
)
myPluggableModuleConfigSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myPluggableModuleConfigSwVer.setStatus("current")


class _MyPluggableModuleOnlineSwVer_Type(DisplayString):
    """Custom type myPluggableModuleOnlineSwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MyPluggableModuleOnlineSwVer_Type.__name__ = "DisplayString"
_MyPluggableModuleOnlineSwVer_Object = MibTableColumn
myPluggableModuleOnlineSwVer = _MyPluggableModuleOnlineSwVer_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 34, 2, 1, 1, 6),
    _MyPluggableModuleOnlineSwVer_Type()
)
myPluggableModuleOnlineSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myPluggableModuleOnlineSwVer.setStatus("current")


class _MyPluggableModuleConfigInfoDescr_Type(DisplayString):
    """Custom type myPluggableModuleConfigInfoDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MyPluggableModuleConfigInfoDescr_Type.__name__ = "DisplayString"
_MyPluggableModuleConfigInfoDescr_Object = MibTableColumn
myPluggableModuleConfigInfoDescr = _MyPluggableModuleConfigInfoDescr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 34, 2, 1, 1, 7),
    _MyPluggableModuleConfigInfoDescr_Type()
)
myPluggableModuleConfigInfoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myPluggableModuleConfigInfoDescr.setStatus("current")


class _MyPluggableModuleOnlineInfoDescr_Type(DisplayString):
    """Custom type myPluggableModuleOnlineInfoDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MyPluggableModuleOnlineInfoDescr_Type.__name__ = "DisplayString"
_MyPluggableModuleOnlineInfoDescr_Object = MibTableColumn
myPluggableModuleOnlineInfoDescr = _MyPluggableModuleOnlineInfoDescr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 34, 2, 1, 1, 8),
    _MyPluggableModuleOnlineInfoDescr_Type()
)
myPluggableModuleOnlineInfoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myPluggableModuleOnlineInfoDescr.setStatus("current")
_MyPluggableModuleConfigPortsNum_Type = Integer32
_MyPluggableModuleConfigPortsNum_Object = MibTableColumn
myPluggableModuleConfigPortsNum = _MyPluggableModuleConfigPortsNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 34, 2, 1, 1, 9),
    _MyPluggableModuleConfigPortsNum_Type()
)
myPluggableModuleConfigPortsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myPluggableModuleConfigPortsNum.setStatus("current")
_MyPluggableModuleOnlinePortsNum_Type = Integer32
_MyPluggableModuleOnlinePortsNum_Object = MibTableColumn
myPluggableModuleOnlinePortsNum = _MyPluggableModuleOnlinePortsNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 34, 2, 1, 1, 10),
    _MyPluggableModuleOnlinePortsNum_Type()
)
myPluggableModuleOnlinePortsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myPluggableModuleOnlinePortsNum.setStatus("current")


class _MyPluggableModuleAction_Type(Integer32):
    """Custom type myPluggableModuleAction based on Integer32"""
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


_MyPluggableModuleAction_Type.__name__ = "Integer32"
_MyPluggableModuleAction_Object = MibTableColumn
myPluggableModuleAction = _MyPluggableModuleAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 34, 2, 1, 1, 11),
    _MyPluggableModuleAction_Type()
)
myPluggableModuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myPluggableModuleAction.setStatus("current")
_MyRedundancyMIBConformance_ObjectIdentity = ObjectIdentity
myRedundancyMIBConformance = _MyRedundancyMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 34, 3)
)
_MyRedundancyMIBCompliances_ObjectIdentity = ObjectIdentity
myRedundancyMIBCompliances = _MyRedundancyMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 34, 3, 1)
)
_MyRedundancyMIBGroups_ObjectIdentity = ObjectIdentity
myRedundancyMIBGroups = _MyRedundancyMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 34, 3, 2)
)

# Managed Objects groups

myRedundancyMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 34, 3, 2, 1)
)
myRedundancyMIBGroup.setObjects(
      *(("DES7200-REDUNDANCY-MIB", "myRedundancyForceSwitchover"),
        ("DES7200-REDUNDANCY-MIB", "myMainCPU"),
        ("DES7200-REDUNDANCY-MIB", "myPluggableModuleInfoDeviceIndex"),
        ("DES7200-REDUNDANCY-MIB", "myPluggableModuleInfoSlotIndex"),
        ("DES7200-REDUNDANCY-MIB", "myPluggableModuleStatus"),
        ("DES7200-REDUNDANCY-MIB", "myPluggableModuleConfigType"),
        ("DES7200-REDUNDANCY-MIB", "myPluggableModuleConfigSwVer"),
        ("DES7200-REDUNDANCY-MIB", "myPluggableModuleOnlineSwVer"),
        ("DES7200-REDUNDANCY-MIB", "myPluggableModuleConfigInfoDescr"),
        ("DES7200-REDUNDANCY-MIB", "myPluggableModuleOnlineInfoDescr"),
        ("DES7200-REDUNDANCY-MIB", "myPluggableModuleConfigPortsNum"),
        ("DES7200-REDUNDANCY-MIB", "myPluggableModuleOnlinePortsNum"),
        ("DES7200-REDUNDANCY-MIB", "myPluggableModuleAction"))
)
if mibBuilder.loadTexts:
    myRedundancyMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

myRedundancyMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 34, 3, 1, 1)
)
myRedundancyMIBCompliance.setObjects(
    ("DES7200-REDUNDANCY-MIB", "myRedundancyMIBGroup")
)
if mibBuilder.loadTexts:
    myRedundancyMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DES7200-REDUNDANCY-MIB",
    **{"myRedundancyMIB": myRedundancyMIB,
       "myRedundancyMIBObjects": myRedundancyMIBObjects,
       "myRedundancyForceSwitchover": myRedundancyForceSwitchover,
       "myMainCPU": myMainCPU,
       "myPluggableMIBObjects": myPluggableMIBObjects,
       "myPluggableModuleInfoTable": myPluggableModuleInfoTable,
       "myPluggableModuleInfoEntry": myPluggableModuleInfoEntry,
       "myPluggableModuleInfoDeviceIndex": myPluggableModuleInfoDeviceIndex,
       "myPluggableModuleInfoSlotIndex": myPluggableModuleInfoSlotIndex,
       "myPluggableModuleStatus": myPluggableModuleStatus,
       "myPluggableModuleConfigType": myPluggableModuleConfigType,
       "myPluggableModuleConfigSwVer": myPluggableModuleConfigSwVer,
       "myPluggableModuleOnlineSwVer": myPluggableModuleOnlineSwVer,
       "myPluggableModuleConfigInfoDescr": myPluggableModuleConfigInfoDescr,
       "myPluggableModuleOnlineInfoDescr": myPluggableModuleOnlineInfoDescr,
       "myPluggableModuleConfigPortsNum": myPluggableModuleConfigPortsNum,
       "myPluggableModuleOnlinePortsNum": myPluggableModuleOnlinePortsNum,
       "myPluggableModuleAction": myPluggableModuleAction,
       "myRedundancyMIBConformance": myRedundancyMIBConformance,
       "myRedundancyMIBCompliances": myRedundancyMIBCompliances,
       "myRedundancyMIBCompliance": myRedundancyMIBCompliance,
       "myRedundancyMIBGroups": myRedundancyMIBGroups,
       "myRedundancyMIBGroup": myRedundancyMIBGroup}
)
