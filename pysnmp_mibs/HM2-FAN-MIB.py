# SNMP MIB module (HM2-FAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hirschmann/HM2-FAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:53:40 2025
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

(hm2UnitIndex,) = mibBuilder.importSymbols(
    "HM2-DEVMGMT-MIB",
    "hm2UnitIndex")

(hm2ConfigurationMibs,) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "hm2ConfigurationMibs")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

hm2FanMgmtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 13)
)
if mibBuilder.loadTexts:
    hm2FanMgmtMib.setRevisions(
        ("2017-04-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Hm2FanModuleStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 1),
          ("available-and-ok", 2),
          ("available-but-failure", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Hm2FanMgmtMibNotifications_ObjectIdentity = ObjectIdentity
hm2FanMgmtMibNotifications = _Hm2FanMgmtMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 13, 0)
)
_Hm2FanMgmtMibObjects_ObjectIdentity = ObjectIdentity
hm2FanMgmtMibObjects = _Hm2FanMgmtMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 13, 1)
)
_Hm2FanMgmtGroup_ObjectIdentity = ObjectIdentity
hm2FanMgmtGroup = _Hm2FanMgmtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 13, 1, 1)
)
_Hm2FanMgmtGlobalGroup_ObjectIdentity = ObjectIdentity
hm2FanMgmtGlobalGroup = _Hm2FanMgmtGlobalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 13, 1, 1, 1)
)
_Hm2FanMgmtMaxSuppModulesPerUnit_Type = Unsigned32
_Hm2FanMgmtMaxSuppModulesPerUnit_Object = MibScalar
hm2FanMgmtMaxSuppModulesPerUnit = _Hm2FanMgmtMaxSuppModulesPerUnit_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 13, 1, 1, 1, 1),
    _Hm2FanMgmtMaxSuppModulesPerUnit_Type()
)
hm2FanMgmtMaxSuppModulesPerUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2FanMgmtMaxSuppModulesPerUnit.setStatus("current")
_Hm2FanMgmtMaxSuppFanPerModule_Type = Unsigned32
_Hm2FanMgmtMaxSuppFanPerModule_Object = MibScalar
hm2FanMgmtMaxSuppFanPerModule = _Hm2FanMgmtMaxSuppFanPerModule_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 13, 1, 1, 1, 2),
    _Hm2FanMgmtMaxSuppFanPerModule_Type()
)
hm2FanMgmtMaxSuppFanPerModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2FanMgmtMaxSuppFanPerModule.setStatus("current")
_Hm2FanModuleMgmtTable_Object = MibTable
hm2FanModuleMgmtTable = _Hm2FanModuleMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 13, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hm2FanModuleMgmtTable.setStatus("current")
_Hm2FanModuleMgmtEntry_Object = MibTableRow
hm2FanModuleMgmtEntry = _Hm2FanModuleMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 13, 1, 1, 2, 1)
)
hm2FanModuleMgmtEntry.setIndexNames(
    (0, "HM2-DEVMGMT-MIB", "hm2UnitIndex"),
    (0, "HM2-FAN-MIB", "hm2FanModuleMgmtId"),
)
if mibBuilder.loadTexts:
    hm2FanModuleMgmtEntry.setStatus("current")
_Hm2FanModuleMgmtId_Type = Unsigned32
_Hm2FanModuleMgmtId_Object = MibTableColumn
hm2FanModuleMgmtId = _Hm2FanModuleMgmtId_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 13, 1, 1, 2, 1, 1),
    _Hm2FanModuleMgmtId_Type()
)
hm2FanModuleMgmtId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hm2FanModuleMgmtId.setStatus("current")
_Hm2FanModuleMgmtStatus_Type = Hm2FanModuleStatus
_Hm2FanModuleMgmtStatus_Object = MibTableColumn
hm2FanModuleMgmtStatus = _Hm2FanModuleMgmtStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 13, 1, 1, 2, 1, 2),
    _Hm2FanModuleMgmtStatus_Type()
)
hm2FanModuleMgmtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2FanModuleMgmtStatus.setStatus("current")
_Hm2FanMgmtTable_Object = MibTable
hm2FanMgmtTable = _Hm2FanMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 13, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hm2FanMgmtTable.setStatus("current")
_Hm2FanMgmtEntry_Object = MibTableRow
hm2FanMgmtEntry = _Hm2FanMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 13, 1, 1, 3, 1)
)
hm2FanMgmtEntry.setIndexNames(
    (0, "HM2-DEVMGMT-MIB", "hm2UnitIndex"),
    (0, "HM2-FAN-MIB", "hm2FanModuleMgmtId"),
    (0, "HM2-FAN-MIB", "hm2FanMgmtFanId"),
)
if mibBuilder.loadTexts:
    hm2FanMgmtEntry.setStatus("current")
_Hm2FanMgmtFanId_Type = Unsigned32
_Hm2FanMgmtFanId_Object = MibTableColumn
hm2FanMgmtFanId = _Hm2FanMgmtFanId_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 13, 1, 1, 3, 1, 1),
    _Hm2FanMgmtFanId_Type()
)
hm2FanMgmtFanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hm2FanMgmtFanId.setStatus("current")
_Hm2FanMgmtStatus_Type = Hm2FanModuleStatus
_Hm2FanMgmtStatus_Object = MibTableColumn
hm2FanMgmtStatus = _Hm2FanMgmtStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 13, 1, 1, 3, 1, 2),
    _Hm2FanMgmtStatus_Type()
)
hm2FanMgmtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2FanMgmtStatus.setStatus("current")

# Managed Objects groups


# Notification objects

hm2FanMgmtModuleNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 13, 0, 1)
)
hm2FanMgmtModuleNotification.setObjects(
      *(("HM2-DEVMGMT-MIB", "hm2UnitIndex"),
        ("HM2-FAN-MIB", "hm2FanModuleMgmtId"),
        ("HM2-FAN-MIB", "hm2FanModuleMgmtStatus"))
)
if mibBuilder.loadTexts:
    hm2FanMgmtModuleNotification.setStatus(
        "current"
    )

hm2FanMgmtFanNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 13, 0, 2)
)
hm2FanMgmtFanNotification.setObjects(
      *(("HM2-DEVMGMT-MIB", "hm2UnitIndex"),
        ("HM2-FAN-MIB", "hm2FanModuleMgmtId"),
        ("HM2-FAN-MIB", "hm2FanMgmtFanId"),
        ("HM2-FAN-MIB", "hm2FanMgmtStatus"))
)
if mibBuilder.loadTexts:
    hm2FanMgmtFanNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-FAN-MIB",
    **{"Hm2FanModuleStatus": Hm2FanModuleStatus,
       "hm2FanMgmtMib": hm2FanMgmtMib,
       "hm2FanMgmtMibNotifications": hm2FanMgmtMibNotifications,
       "hm2FanMgmtModuleNotification": hm2FanMgmtModuleNotification,
       "hm2FanMgmtFanNotification": hm2FanMgmtFanNotification,
       "hm2FanMgmtMibObjects": hm2FanMgmtMibObjects,
       "hm2FanMgmtGroup": hm2FanMgmtGroup,
       "hm2FanMgmtGlobalGroup": hm2FanMgmtGlobalGroup,
       "hm2FanMgmtMaxSuppModulesPerUnit": hm2FanMgmtMaxSuppModulesPerUnit,
       "hm2FanMgmtMaxSuppFanPerModule": hm2FanMgmtMaxSuppFanPerModule,
       "hm2FanModuleMgmtTable": hm2FanModuleMgmtTable,
       "hm2FanModuleMgmtEntry": hm2FanModuleMgmtEntry,
       "hm2FanModuleMgmtId": hm2FanModuleMgmtId,
       "hm2FanModuleMgmtStatus": hm2FanModuleMgmtStatus,
       "hm2FanMgmtTable": hm2FanMgmtTable,
       "hm2FanMgmtEntry": hm2FanMgmtEntry,
       "hm2FanMgmtFanId": hm2FanMgmtFanId,
       "hm2FanMgmtStatus": hm2FanMgmtStatus}
)
