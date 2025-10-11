# SNMP MIB module (H3C-RES-MON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-RES-MON-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:20:29 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cResMon = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 169)
)
if mibBuilder.loadTexts:
    h3cResMon.setRevisions(
        ("2017-04-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cResMonScalarObjects_ObjectIdentity = ObjectIdentity
h3cResMonScalarObjects = _H3cResMonScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 169, 1)
)
_H3cResMonMinorResendEnable_Type = TruthValue
_H3cResMonMinorResendEnable_Object = MibScalar
h3cResMonMinorResendEnable = _H3cResMonMinorResendEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 169, 1, 1),
    _H3cResMonMinorResendEnable_Type()
)
h3cResMonMinorResendEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cResMonMinorResendEnable.setStatus("current")


class _H3cResMonOutputEnable_Type(Bits):
    """Custom type h3cResMonOutputEnable based on Bits"""
    namedValues = NamedValues(
        *(("syslog", 0),
          ("snmpNotification", 1),
          ("netconfEvent", 2))
    )

_H3cResMonOutputEnable_Type.__name__ = "Bits"
_H3cResMonOutputEnable_Object = MibScalar
h3cResMonOutputEnable = _H3cResMonOutputEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 169, 1, 2),
    _H3cResMonOutputEnable_Type()
)
h3cResMonOutputEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cResMonOutputEnable.setStatus("current")
_H3cResMonTables_ObjectIdentity = ObjectIdentity
h3cResMonTables = _H3cResMonTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 169, 2)
)
_H3cResMonConfigTable_Object = MibTable
h3cResMonConfigTable = _H3cResMonConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 169, 2, 1)
)
if mibBuilder.loadTexts:
    h3cResMonConfigTable.setStatus("current")
_H3cResMonConfigEntry_Object = MibTableRow
h3cResMonConfigEntry = _H3cResMonConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 169, 2, 1, 1)
)
h3cResMonConfigEntry.setIndexNames(
    (0, "H3C-RES-MON-MIB", "h3cResMonChassisIndex"),
    (0, "H3C-RES-MON-MIB", "h3cResMonSlotIndex"),
    (0, "H3C-RES-MON-MIB", "h3cResMonCpuIndex"),
    (0, "H3C-RES-MON-MIB", "h3cResMonResourceName"),
)
if mibBuilder.loadTexts:
    h3cResMonConfigEntry.setStatus("current")
_H3cResMonChassisIndex_Type = Unsigned32
_H3cResMonChassisIndex_Object = MibTableColumn
h3cResMonChassisIndex = _H3cResMonChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 169, 2, 1, 1, 1),
    _H3cResMonChassisIndex_Type()
)
h3cResMonChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cResMonChassisIndex.setStatus("current")
_H3cResMonSlotIndex_Type = Unsigned32
_H3cResMonSlotIndex_Object = MibTableColumn
h3cResMonSlotIndex = _H3cResMonSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 169, 2, 1, 1, 2),
    _H3cResMonSlotIndex_Type()
)
h3cResMonSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cResMonSlotIndex.setStatus("current")
_H3cResMonCpuIndex_Type = Unsigned32
_H3cResMonCpuIndex_Object = MibTableColumn
h3cResMonCpuIndex = _H3cResMonCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 169, 2, 1, 1, 3),
    _H3cResMonCpuIndex_Type()
)
h3cResMonCpuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cResMonCpuIndex.setStatus("current")


class _H3cResMonResourceName_Type(OctetString):
    """Custom type h3cResMonResourceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H3cResMonResourceName_Type.__name__ = "OctetString"
_H3cResMonResourceName_Object = MibTableColumn
h3cResMonResourceName = _H3cResMonResourceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 169, 2, 1, 1, 4),
    _H3cResMonResourceName_Type()
)
h3cResMonResourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cResMonResourceName.setStatus("current")


class _H3cResMonThresholdUnit_Type(Integer32):
    """Custom type h3cResMonThresholdUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absolute", 1),
          ("percentage", 2))
    )


_H3cResMonThresholdUnit_Type.__name__ = "Integer32"
_H3cResMonThresholdUnit_Object = MibTableColumn
h3cResMonThresholdUnit = _H3cResMonThresholdUnit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 169, 2, 1, 1, 5),
    _H3cResMonThresholdUnit_Type()
)
h3cResMonThresholdUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cResMonThresholdUnit.setStatus("current")
_H3cResMonMinorThreshold_Type = Unsigned32
_H3cResMonMinorThreshold_Object = MibTableColumn
h3cResMonMinorThreshold = _H3cResMonMinorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 169, 2, 1, 1, 6),
    _H3cResMonMinorThreshold_Type()
)
h3cResMonMinorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cResMonMinorThreshold.setStatus("current")
_H3cResMonSevereThreshold_Type = Unsigned32
_H3cResMonSevereThreshold_Object = MibTableColumn
h3cResMonSevereThreshold = _H3cResMonSevereThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 169, 2, 1, 1, 7),
    _H3cResMonSevereThreshold_Type()
)
h3cResMonSevereThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cResMonSevereThreshold.setStatus("current")
_H3cResMonInfoTable_Object = MibTable
h3cResMonInfoTable = _H3cResMonInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 169, 2, 2)
)
if mibBuilder.loadTexts:
    h3cResMonInfoTable.setStatus("current")
_H3cResMonInfoEntry_Object = MibTableRow
h3cResMonInfoEntry = _H3cResMonInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 169, 2, 2, 1)
)
h3cResMonInfoEntry.setIndexNames(
    (0, "H3C-RES-MON-MIB", "h3cResMonChassisIndex"),
    (0, "H3C-RES-MON-MIB", "h3cResMonSlotIndex"),
    (0, "H3C-RES-MON-MIB", "h3cResMonCpuIndex"),
    (0, "H3C-RES-MON-MIB", "h3cResMonResourceName"),
)
if mibBuilder.loadTexts:
    h3cResMonInfoEntry.setStatus("current")


class _H3cResMonUnit_Type(Integer32):
    """Custom type h3cResMonUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absolute", 1),
          ("percentage", 2))
    )


_H3cResMonUnit_Type.__name__ = "Integer32"
_H3cResMonUnit_Object = MibTableColumn
h3cResMonUnit = _H3cResMonUnit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 169, 2, 2, 1, 1),
    _H3cResMonUnit_Type()
)
h3cResMonUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cResMonUnit.setStatus("current")
_H3cResMonCurrent_Type = Unsigned32
_H3cResMonCurrent_Object = MibTableColumn
h3cResMonCurrent = _H3cResMonCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 169, 2, 2, 1, 2),
    _H3cResMonCurrent_Type()
)
h3cResMonCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cResMonCurrent.setStatus("current")
_H3cResMonFree_Type = Unsigned32
_H3cResMonFree_Object = MibTableColumn
h3cResMonFree = _H3cResMonFree_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 169, 2, 2, 1, 3),
    _H3cResMonFree_Type()
)
h3cResMonFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cResMonFree.setStatus("current")
_H3cResMonTotal_Type = Unsigned32
_H3cResMonTotal_Object = MibTableColumn
h3cResMonTotal = _H3cResMonTotal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 169, 2, 2, 1, 4),
    _H3cResMonTotal_Type()
)
h3cResMonTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cResMonTotal.setStatus("current")
_H3cResMonNotification_ObjectIdentity = ObjectIdentity
h3cResMonNotification = _H3cResMonNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 169, 3)
)
_H3cResMonTrapPrefix_ObjectIdentity = ObjectIdentity
h3cResMonTrapPrefix = _H3cResMonTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 169, 3, 0)
)
_H3cResMonTrapInfor_ObjectIdentity = ObjectIdentity
h3cResMonTrapInfor = _H3cResMonTrapInfor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 169, 3, 1)
)


class _H3cResMonAdditionalInfo_Type(OctetString):
    """Custom type h3cResMonAdditionalInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cResMonAdditionalInfo_Type.__name__ = "OctetString"
_H3cResMonAdditionalInfo_Object = MibScalar
h3cResMonAdditionalInfo = _H3cResMonAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 169, 3, 1, 1),
    _H3cResMonAdditionalInfo_Type()
)
h3cResMonAdditionalInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cResMonAdditionalInfo.setStatus("current")

# Managed Objects groups


# Notification objects

h3cResMonMinorNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 169, 3, 0, 1)
)
h3cResMonMinorNotification.setObjects(
      *(("H3C-RES-MON-MIB", "h3cResMonChassisIndex"),
        ("H3C-RES-MON-MIB", "h3cResMonSlotIndex"),
        ("H3C-RES-MON-MIB", "h3cResMonCpuIndex"),
        ("H3C-RES-MON-MIB", "h3cResMonResourceName"),
        ("H3C-RES-MON-MIB", "h3cResMonThresholdUnit"),
        ("H3C-RES-MON-MIB", "h3cResMonMinorThreshold"),
        ("H3C-RES-MON-MIB", "h3cResMonSevereThreshold"),
        ("H3C-RES-MON-MIB", "h3cResMonCurrent"),
        ("H3C-RES-MON-MIB", "h3cResMonFree"),
        ("H3C-RES-MON-MIB", "h3cResMonTotal"),
        ("H3C-RES-MON-MIB", "h3cResMonAdditionalInfo"))
)
if mibBuilder.loadTexts:
    h3cResMonMinorNotification.setStatus(
        "current"
    )

h3cResMonMinorRecoverNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 169, 3, 0, 2)
)
h3cResMonMinorRecoverNotification.setObjects(
      *(("H3C-RES-MON-MIB", "h3cResMonChassisIndex"),
        ("H3C-RES-MON-MIB", "h3cResMonSlotIndex"),
        ("H3C-RES-MON-MIB", "h3cResMonCpuIndex"),
        ("H3C-RES-MON-MIB", "h3cResMonResourceName"),
        ("H3C-RES-MON-MIB", "h3cResMonThresholdUnit"),
        ("H3C-RES-MON-MIB", "h3cResMonMinorThreshold"),
        ("H3C-RES-MON-MIB", "h3cResMonSevereThreshold"),
        ("H3C-RES-MON-MIB", "h3cResMonCurrent"),
        ("H3C-RES-MON-MIB", "h3cResMonFree"),
        ("H3C-RES-MON-MIB", "h3cResMonTotal"),
        ("H3C-RES-MON-MIB", "h3cResMonAdditionalInfo"))
)
if mibBuilder.loadTexts:
    h3cResMonMinorRecoverNotification.setStatus(
        "current"
    )

h3cResMonSevereNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 169, 3, 0, 3)
)
h3cResMonSevereNotification.setObjects(
      *(("H3C-RES-MON-MIB", "h3cResMonChassisIndex"),
        ("H3C-RES-MON-MIB", "h3cResMonSlotIndex"),
        ("H3C-RES-MON-MIB", "h3cResMonCpuIndex"),
        ("H3C-RES-MON-MIB", "h3cResMonResourceName"),
        ("H3C-RES-MON-MIB", "h3cResMonThresholdUnit"),
        ("H3C-RES-MON-MIB", "h3cResMonMinorThreshold"),
        ("H3C-RES-MON-MIB", "h3cResMonSevereThreshold"),
        ("H3C-RES-MON-MIB", "h3cResMonCurrent"),
        ("H3C-RES-MON-MIB", "h3cResMonFree"),
        ("H3C-RES-MON-MIB", "h3cResMonTotal"),
        ("H3C-RES-MON-MIB", "h3cResMonAdditionalInfo"))
)
if mibBuilder.loadTexts:
    h3cResMonSevereNotification.setStatus(
        "current"
    )

h3cResMonSevereRecoverNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 169, 3, 0, 4)
)
h3cResMonSevereRecoverNotification.setObjects(
      *(("H3C-RES-MON-MIB", "h3cResMonChassisIndex"),
        ("H3C-RES-MON-MIB", "h3cResMonSlotIndex"),
        ("H3C-RES-MON-MIB", "h3cResMonCpuIndex"),
        ("H3C-RES-MON-MIB", "h3cResMonResourceName"),
        ("H3C-RES-MON-MIB", "h3cResMonThresholdUnit"),
        ("H3C-RES-MON-MIB", "h3cResMonMinorThreshold"),
        ("H3C-RES-MON-MIB", "h3cResMonSevereThreshold"),
        ("H3C-RES-MON-MIB", "h3cResMonCurrent"),
        ("H3C-RES-MON-MIB", "h3cResMonFree"),
        ("H3C-RES-MON-MIB", "h3cResMonTotal"),
        ("H3C-RES-MON-MIB", "h3cResMonAdditionalInfo"))
)
if mibBuilder.loadTexts:
    h3cResMonSevereRecoverNotification.setStatus(
        "current"
    )

h3cResMonUsedUpNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 169, 3, 0, 5)
)
h3cResMonUsedUpNotification.setObjects(
      *(("H3C-RES-MON-MIB", "h3cResMonChassisIndex"),
        ("H3C-RES-MON-MIB", "h3cResMonSlotIndex"),
        ("H3C-RES-MON-MIB", "h3cResMonCpuIndex"),
        ("H3C-RES-MON-MIB", "h3cResMonResourceName"),
        ("H3C-RES-MON-MIB", "h3cResMonThresholdUnit"),
        ("H3C-RES-MON-MIB", "h3cResMonMinorThreshold"),
        ("H3C-RES-MON-MIB", "h3cResMonSevereThreshold"),
        ("H3C-RES-MON-MIB", "h3cResMonCurrent"),
        ("H3C-RES-MON-MIB", "h3cResMonFree"),
        ("H3C-RES-MON-MIB", "h3cResMonTotal"),
        ("H3C-RES-MON-MIB", "h3cResMonAdditionalInfo"))
)
if mibBuilder.loadTexts:
    h3cResMonUsedUpNotification.setStatus(
        "current"
    )

h3cResMonUsedUpRecoverNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 169, 3, 0, 6)
)
h3cResMonUsedUpRecoverNotification.setObjects(
      *(("H3C-RES-MON-MIB", "h3cResMonChassisIndex"),
        ("H3C-RES-MON-MIB", "h3cResMonSlotIndex"),
        ("H3C-RES-MON-MIB", "h3cResMonCpuIndex"),
        ("H3C-RES-MON-MIB", "h3cResMonResourceName"),
        ("H3C-RES-MON-MIB", "h3cResMonThresholdUnit"),
        ("H3C-RES-MON-MIB", "h3cResMonMinorThreshold"),
        ("H3C-RES-MON-MIB", "h3cResMonSevereThreshold"),
        ("H3C-RES-MON-MIB", "h3cResMonCurrent"),
        ("H3C-RES-MON-MIB", "h3cResMonFree"),
        ("H3C-RES-MON-MIB", "h3cResMonTotal"),
        ("H3C-RES-MON-MIB", "h3cResMonAdditionalInfo"))
)
if mibBuilder.loadTexts:
    h3cResMonUsedUpRecoverNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-RES-MON-MIB",
    **{"h3cResMon": h3cResMon,
       "h3cResMonScalarObjects": h3cResMonScalarObjects,
       "h3cResMonMinorResendEnable": h3cResMonMinorResendEnable,
       "h3cResMonOutputEnable": h3cResMonOutputEnable,
       "h3cResMonTables": h3cResMonTables,
       "h3cResMonConfigTable": h3cResMonConfigTable,
       "h3cResMonConfigEntry": h3cResMonConfigEntry,
       "h3cResMonChassisIndex": h3cResMonChassisIndex,
       "h3cResMonSlotIndex": h3cResMonSlotIndex,
       "h3cResMonCpuIndex": h3cResMonCpuIndex,
       "h3cResMonResourceName": h3cResMonResourceName,
       "h3cResMonThresholdUnit": h3cResMonThresholdUnit,
       "h3cResMonMinorThreshold": h3cResMonMinorThreshold,
       "h3cResMonSevereThreshold": h3cResMonSevereThreshold,
       "h3cResMonInfoTable": h3cResMonInfoTable,
       "h3cResMonInfoEntry": h3cResMonInfoEntry,
       "h3cResMonUnit": h3cResMonUnit,
       "h3cResMonCurrent": h3cResMonCurrent,
       "h3cResMonFree": h3cResMonFree,
       "h3cResMonTotal": h3cResMonTotal,
       "h3cResMonNotification": h3cResMonNotification,
       "h3cResMonTrapPrefix": h3cResMonTrapPrefix,
       "h3cResMonMinorNotification": h3cResMonMinorNotification,
       "h3cResMonMinorRecoverNotification": h3cResMonMinorRecoverNotification,
       "h3cResMonSevereNotification": h3cResMonSevereNotification,
       "h3cResMonSevereRecoverNotification": h3cResMonSevereRecoverNotification,
       "h3cResMonUsedUpNotification": h3cResMonUsedUpNotification,
       "h3cResMonUsedUpRecoverNotification": h3cResMonUsedUpRecoverNotification,
       "h3cResMonTrapInfor": h3cResMonTrapInfor,
       "h3cResMonAdditionalInfo": h3cResMonAdditionalInfo}
)
