# SNMP MIB module (CRESTRON-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/crestron/CRESTRON-SYSTEM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:03:45 2025
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

(crestronCommon,) = mibBuilder.importSymbols(
    "CRESTRON-ROOT-MIB",
    "crestronCommon")

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

crestronSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 6, 1)
)
if mibBuilder.loadTexts:
    crestronSystem.setRevisions(
        ("2003-08-18 12:19",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CrestronSysMIBVersion_Type = Integer32
_CrestronSysMIBVersion_Object = MibScalar
crestronSysMIBVersion = _CrestronSysMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 3212, 6, 1, 1),
    _CrestronSysMIBVersion_Type()
)
crestronSysMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crestronSysMIBVersion.setStatus("current")
_CrestronSysAdmin_ObjectIdentity = ObjectIdentity
crestronSysAdmin = _CrestronSysAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 6, 1, 2)
)
_CrestronSysNotifications_ObjectIdentity = ObjectIdentity
crestronSysNotifications = _CrestronSysNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 6, 1, 3)
)
_CrestronSysTrapMsg_Type = DisplayString
_CrestronSysTrapMsg_Object = MibScalar
crestronSysTrapMsg = _CrestronSysTrapMsg_Object(
    (1, 3, 6, 1, 4, 1, 3212, 6, 1, 3, 1),
    _CrestronSysTrapMsg_Type()
)
crestronSysTrapMsg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    crestronSysTrapMsg.setStatus("current")
_CrestronSysObjects_ObjectIdentity = ObjectIdentity
crestronSysObjects = _CrestronSysObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 6, 1, 4)
)
_CrestronSysErrors_ObjectIdentity = ObjectIdentity
crestronSysErrors = _CrestronSysErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 6, 1, 4, 2)
)
_CrestronSysInterfaces_ObjectIdentity = ObjectIdentity
crestronSysInterfaces = _CrestronSysInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 6, 1, 4, 4)
)
_CrestronSysInterfacesCount_Type = Counter32
_CrestronSysInterfacesCount_Object = MibScalar
crestronSysInterfacesCount = _CrestronSysInterfacesCount_Object(
    (1, 3, 6, 1, 4, 1, 3212, 6, 1, 4, 4, 1),
    _CrestronSysInterfacesCount_Type()
)
crestronSysInterfacesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crestronSysInterfacesCount.setStatus("current")
_CrestronSysInterfacesTable_Object = MibTable
crestronSysInterfacesTable = _CrestronSysInterfacesTable_Object(
    (1, 3, 6, 1, 4, 1, 3212, 6, 1, 4, 4, 2)
)
if mibBuilder.loadTexts:
    crestronSysInterfacesTable.setStatus("current")
_CrestronSysInterfacesEntry_Object = MibTableRow
crestronSysInterfacesEntry = _CrestronSysInterfacesEntry_Object(
    (1, 3, 6, 1, 4, 1, 3212, 6, 1, 4, 4, 2, 1)
)
crestronSysInterfacesEntry.setIndexNames(
    (0, "CRESTRON-SYSTEM-MIB", "crestronSysInterfacesId"),
)
if mibBuilder.loadTexts:
    crestronSysInterfacesEntry.setStatus("current")


class _CrestronSysInterfacesId_Type(Integer32):
    """Custom type crestronSysInterfacesId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CrestronSysInterfacesId_Type.__name__ = "Integer32"
_CrestronSysInterfacesId_Object = MibTableColumn
crestronSysInterfacesId = _CrestronSysInterfacesId_Object(
    (1, 3, 6, 1, 4, 1, 3212, 6, 1, 4, 4, 2, 1, 1),
    _CrestronSysInterfacesId_Type()
)
crestronSysInterfacesId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crestronSysInterfacesId.setStatus("current")
_CrestronSysInterfacesRxOverruns_Type = Integer32
_CrestronSysInterfacesRxOverruns_Object = MibTableColumn
crestronSysInterfacesRxOverruns = _CrestronSysInterfacesRxOverruns_Object(
    (1, 3, 6, 1, 4, 1, 3212, 6, 1, 4, 4, 2, 1, 2),
    _CrestronSysInterfacesRxOverruns_Type()
)
crestronSysInterfacesRxOverruns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crestronSysInterfacesRxOverruns.setStatus("current")
_CrestronSysInterfacesTxAllocFailed_Type = Integer32
_CrestronSysInterfacesTxAllocFailed_Object = MibTableColumn
crestronSysInterfacesTxAllocFailed = _CrestronSysInterfacesTxAllocFailed_Object(
    (1, 3, 6, 1, 4, 1, 3212, 6, 1, 4, 4, 2, 1, 3),
    _CrestronSysInterfacesTxAllocFailed_Type()
)
crestronSysInterfacesTxAllocFailed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crestronSysInterfacesTxAllocFailed.setStatus("current")
_CrestronSysInterfacesTxAllocTimeoput_Type = Integer32
_CrestronSysInterfacesTxAllocTimeoput_Object = MibTableColumn
crestronSysInterfacesTxAllocTimeoput = _CrestronSysInterfacesTxAllocTimeoput_Object(
    (1, 3, 6, 1, 4, 1, 3212, 6, 1, 4, 4, 2, 1, 4),
    _CrestronSysInterfacesTxAllocTimeoput_Type()
)
crestronSysInterfacesTxAllocTimeoput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crestronSysInterfacesTxAllocTimeoput.setStatus("current")
_CrestronSysConformance_ObjectIdentity = ObjectIdentity
crestronSysConformance = _CrestronSysConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 6, 1, 5)
)
_CrestronSysCompliances_ObjectIdentity = ObjectIdentity
crestronSysCompliances = _CrestronSysCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 6, 1, 5, 1)
)
_CrestronSysGroups_ObjectIdentity = ObjectIdentity
crestronSysGroups = _CrestronSysGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 6, 1, 5, 2)
)

# Managed Objects groups

crestronSystemAllObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3212, 6, 1, 5, 2, 1)
)
crestronSystemAllObjects.setObjects(
      *(("CRESTRON-SYSTEM-MIB", "crestronSysMIBVersion"),
        ("CRESTRON-SYSTEM-MIB", "crestronSysTrapMsg"),
        ("CRESTRON-SYSTEM-MIB", "crestronSysInterfacesCount"),
        ("CRESTRON-SYSTEM-MIB", "crestronSysInterfacesId"),
        ("CRESTRON-SYSTEM-MIB", "crestronSysInterfacesRxOverruns"),
        ("CRESTRON-SYSTEM-MIB", "crestronSysInterfacesTxAllocFailed"),
        ("CRESTRON-SYSTEM-MIB", "crestronSysInterfacesTxAllocTimeoput"))
)
if mibBuilder.loadTexts:
    crestronSystemAllObjects.setStatus("current")


# Notification objects

crestronSysTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3212, 6, 1, 3, 2)
)
crestronSysTrap.setObjects(
    ("CRESTRON-SYSTEM-MIB", "crestronSysTrapMsg")
)
if mibBuilder.loadTexts:
    crestronSysTrap.setStatus(
        "current"
    )


# Notifications groups

crestronSystemAllTraps = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3212, 6, 1, 5, 2, 6)
)
crestronSystemAllTraps.setObjects(
    ("CRESTRON-SYSTEM-MIB", "crestronSysTrap")
)
if mibBuilder.loadTexts:
    crestronSystemAllTraps.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CRESTRON-SYSTEM-MIB",
    **{"crestronSystem": crestronSystem,
       "crestronSysMIBVersion": crestronSysMIBVersion,
       "crestronSysAdmin": crestronSysAdmin,
       "crestronSysNotifications": crestronSysNotifications,
       "crestronSysTrapMsg": crestronSysTrapMsg,
       "crestronSysTrap": crestronSysTrap,
       "crestronSysObjects": crestronSysObjects,
       "crestronSysErrors": crestronSysErrors,
       "crestronSysInterfaces": crestronSysInterfaces,
       "crestronSysInterfacesCount": crestronSysInterfacesCount,
       "crestronSysInterfacesTable": crestronSysInterfacesTable,
       "crestronSysInterfacesEntry": crestronSysInterfacesEntry,
       "crestronSysInterfacesId": crestronSysInterfacesId,
       "crestronSysInterfacesRxOverruns": crestronSysInterfacesRxOverruns,
       "crestronSysInterfacesTxAllocFailed": crestronSysInterfacesTxAllocFailed,
       "crestronSysInterfacesTxAllocTimeoput": crestronSysInterfacesTxAllocTimeoput,
       "crestronSysConformance": crestronSysConformance,
       "crestronSysCompliances": crestronSysCompliances,
       "crestronSysGroups": crestronSysGroups,
       "crestronSystemAllObjects": crestronSystemAllObjects,
       "crestronSystemAllTraps": crestronSystemAllTraps}
)
