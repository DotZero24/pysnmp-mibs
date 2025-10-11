# SNMP MIB module (OA-TRAP-MESSAGES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OA-TRAP-MESSAGES-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:04:41 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

nbDeviceTrapMessages = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 27)
)
if mibBuilder.loadTexts:
    nbDeviceTrapMessages.setRevisions(
        ("2007-10-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nbase_ObjectIdentity = ObjectIdentity
nbase = _Nbase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629)
)
_NbSwitchG1_ObjectIdentity = ObjectIdentity
nbSwitchG1 = _NbSwitchG1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1)
)
_NbSwitchG1Il_ObjectIdentity = ObjectIdentity
nbSwitchG1Il = _NbSwitchG1Il_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50)
)
_NbDeviceConfig_ObjectIdentity = ObjectIdentity
nbDeviceConfig = _NbDeviceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11)
)
_NbDevGen_ObjectIdentity = ObjectIdentity
nbDevGen = _NbDevGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1)
)
_OaDevTrapsNotifications_ObjectIdentity = ObjectIdentity
oaDevTrapsNotifications = _OaDevTrapsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 27, 0)
)
_OaDevTrapsGen_ObjectIdentity = ObjectIdentity
oaDevTrapsGen = _OaDevTrapsGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 27, 1)
)


class _OaDevTrapsGenSupport_Type(Integer32):
    """Custom type oaDevTrapsGenSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supported", 2))
    )


_OaDevTrapsGenSupport_Type.__name__ = "Integer32"
_OaDevTrapsGenSupport_Object = MibScalar
oaDevTrapsGenSupport = _OaDevTrapsGenSupport_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 27, 1, 1),
    _OaDevTrapsGenSupport_Type()
)
oaDevTrapsGenSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDevTrapsGenSupport.setStatus("current")
_OaDevTrapsPorts_ObjectIdentity = ObjectIdentity
oaDevTrapsPorts = _OaDevTrapsPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 27, 5)
)
_OaDevTrapsPortsTable_Object = MibTable
oaDevTrapsPortsTable = _OaDevTrapsPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 27, 5, 3)
)
if mibBuilder.loadTexts:
    oaDevTrapsPortsTable.setStatus("current")
_OaDevTrapsPortsEntry_Object = MibTableRow
oaDevTrapsPortsEntry = _OaDevTrapsPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 27, 5, 3, 1)
)
oaDevTrapsPortsEntry.setIndexNames(
    (0, "OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfIndex"),
)
if mibBuilder.loadTexts:
    oaDevTrapsPortsEntry.setStatus("current")


class _OaDevTrapsPortsIfIndex_Type(Integer32):
    """Custom type oaDevTrapsPortsIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OaDevTrapsPortsIfIndex_Type.__name__ = "Integer32"
_OaDevTrapsPortsIfIndex_Object = MibTableColumn
oaDevTrapsPortsIfIndex = _OaDevTrapsPortsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 27, 5, 3, 1, 1),
    _OaDevTrapsPortsIfIndex_Type()
)
oaDevTrapsPortsIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    oaDevTrapsPortsIfIndex.setStatus("current")


class _OaDevTrapsPortsSlotNumber_Type(Integer32):
    """Custom type oaDevTrapsPortsSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_OaDevTrapsPortsSlotNumber_Type.__name__ = "Integer32"
_OaDevTrapsPortsSlotNumber_Object = MibTableColumn
oaDevTrapsPortsSlotNumber = _OaDevTrapsPortsSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 27, 5, 3, 1, 2),
    _OaDevTrapsPortsSlotNumber_Type()
)
oaDevTrapsPortsSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDevTrapsPortsSlotNumber.setStatus("current")


class _OaDevTrapsPortsSlotPortNumber_Type(Integer32):
    """Custom type oaDevTrapsPortsSlotPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_OaDevTrapsPortsSlotPortNumber_Type.__name__ = "Integer32"
_OaDevTrapsPortsSlotPortNumber_Object = MibTableColumn
oaDevTrapsPortsSlotPortNumber = _OaDevTrapsPortsSlotPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 27, 5, 3, 1, 3),
    _OaDevTrapsPortsSlotPortNumber_Type()
)
oaDevTrapsPortsSlotPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDevTrapsPortsSlotPortNumber.setStatus("current")


class _OaDevTrapsPortsIfAlias_Type(DisplayString):
    """Custom type oaDevTrapsPortsIfAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OaDevTrapsPortsIfAlias_Type.__name__ = "DisplayString"
_OaDevTrapsPortsIfAlias_Object = MibTableColumn
oaDevTrapsPortsIfAlias = _OaDevTrapsPortsIfAlias_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 27, 5, 3, 1, 4),
    _OaDevTrapsPortsIfAlias_Type()
)
oaDevTrapsPortsIfAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDevTrapsPortsIfAlias.setStatus("current")
_OaDevTrapsConformance_ObjectIdentity = ObjectIdentity
oaDevTrapsConformance = _OaDevTrapsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 27, 101)
)
_OaDevTrapsMIBCompliances_ObjectIdentity = ObjectIdentity
oaDevTrapsMIBCompliances = _OaDevTrapsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 27, 101, 1)
)
_OaDevTrapsMIBGroups_ObjectIdentity = ObjectIdentity
oaDevTrapsMIBGroups = _OaDevTrapsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 27, 101, 2)
)

# Managed Objects groups

oaDevTrapsGenGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 27, 101, 2, 1)
)
oaDevTrapsGenGroup.setObjects(
    ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsGenSupport")
)
if mibBuilder.loadTexts:
    oaDevTrapsGenGroup.setStatus("current")

oaDevTrapsPortsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 27, 101, 2, 2)
)
oaDevTrapsPortsGroup.setObjects(
      *(("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsSlotNumber"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsSlotPortNumber"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaDevTrapsPortsGroup.setStatus("current")


# Notification objects

oaDevTrapsLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 27, 0, 203)
)
oaDevTrapsLinkDown.setObjects(
      *(("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsSlotNumber"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsSlotPortNumber"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaDevTrapsLinkDown.setStatus(
        "current"
    )

oaDevTrapsLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 27, 0, 204)
)
oaDevTrapsLinkUp.setObjects(
      *(("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsSlotNumber"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsSlotPortNumber"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaDevTrapsLinkUp.setStatus(
        "current"
    )


# Notifications groups

oaDevTrapsPortsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 27, 101, 2, 3)
)
oaDevTrapsPortsNotificationGroup.setObjects(
      *(("OA-TRAP-MESSAGES-MIB", "oaDevTrapsLinkDown"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsLinkUp"))
)
if mibBuilder.loadTexts:
    oaDevTrapsPortsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

oaDevTrapsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 27, 101, 1, 1)
)
oaDevTrapsMIBCompliance.setObjects(
      *(("OA-TRAP-MESSAGES-MIB", "oaDevTrapsGenGroup"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsGroup"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsNotificationGroup"))
)
if mibBuilder.loadTexts:
    oaDevTrapsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OA-TRAP-MESSAGES-MIB",
    **{"nbase": nbase,
       "nbSwitchG1": nbSwitchG1,
       "nbSwitchG1Il": nbSwitchG1Il,
       "nbDeviceConfig": nbDeviceConfig,
       "nbDevGen": nbDevGen,
       "nbDeviceTrapMessages": nbDeviceTrapMessages,
       "oaDevTrapsNotifications": oaDevTrapsNotifications,
       "oaDevTrapsLinkDown": oaDevTrapsLinkDown,
       "oaDevTrapsLinkUp": oaDevTrapsLinkUp,
       "oaDevTrapsGen": oaDevTrapsGen,
       "oaDevTrapsGenSupport": oaDevTrapsGenSupport,
       "oaDevTrapsPorts": oaDevTrapsPorts,
       "oaDevTrapsPortsTable": oaDevTrapsPortsTable,
       "oaDevTrapsPortsEntry": oaDevTrapsPortsEntry,
       "oaDevTrapsPortsIfIndex": oaDevTrapsPortsIfIndex,
       "oaDevTrapsPortsSlotNumber": oaDevTrapsPortsSlotNumber,
       "oaDevTrapsPortsSlotPortNumber": oaDevTrapsPortsSlotPortNumber,
       "oaDevTrapsPortsIfAlias": oaDevTrapsPortsIfAlias,
       "oaDevTrapsConformance": oaDevTrapsConformance,
       "oaDevTrapsMIBCompliances": oaDevTrapsMIBCompliances,
       "oaDevTrapsMIBCompliance": oaDevTrapsMIBCompliance,
       "oaDevTrapsMIBGroups": oaDevTrapsMIBGroups,
       "oaDevTrapsGenGroup": oaDevTrapsGenGroup,
       "oaDevTrapsPortsGroup": oaDevTrapsPortsGroup,
       "oaDevTrapsPortsNotificationGroup": oaDevTrapsPortsNotificationGroup}
)
