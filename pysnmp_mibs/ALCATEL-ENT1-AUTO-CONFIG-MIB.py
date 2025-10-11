# SNMP MIB module (ALCATEL-ENT1-AUTO-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alcatel-ent1/ALCATEL-ENT1-AUTO-CONFIG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:10:38 2025
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

(softentIND1AutoConfig,) = mibBuilder.importSymbols(
    "ALCATEL-ENT1-BASE",
    "softentIND1AutoConfig")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alaAUTOCONFIGMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 83, 1)
)
if mibBuilder.loadTexts:
    alaAUTOCONFIGMIB.setRevisions(
        ("2012-05-04 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlaAUTOCONFIGMIBNotifications_ObjectIdentity = ObjectIdentity
alaAUTOCONFIGMIBNotifications = _AlaAUTOCONFIGMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 83, 1, 0)
)
_AlaAUTOCONFIGMIBObjects_ObjectIdentity = ObjectIdentity
alaAUTOCONFIGMIBObjects = _AlaAUTOCONFIGMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 83, 1, 1)
)
if mibBuilder.loadTexts:
    alaAUTOCONFIGMIBObjects.setStatus("current")
_AlaAUTOCONFIGGlobal_ObjectIdentity = ObjectIdentity
alaAUTOCONFIGGlobal = _AlaAUTOCONFIGGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 83, 1, 1, 1)
)


class _AlaAutoConfigAbort_Type(Integer32):
    """Custom type alaAutoConfigAbort based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaAutoConfigAbort_Type.__name__ = "Integer32"
_AlaAutoConfigAbort_Object = MibScalar
alaAutoConfigAbort = _AlaAutoConfigAbort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 83, 1, 1, 1, 1),
    _AlaAutoConfigAbort_Type()
)
alaAutoConfigAbort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAutoConfigAbort.setStatus("current")
_AlaAUTOCONFIGNotificationObjects_ObjectIdentity = ObjectIdentity
alaAUTOCONFIGNotificationObjects = _AlaAUTOCONFIGNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 83, 1, 1, 2)
)
_AlaAutoConfigTrapsObj_ObjectIdentity = ObjectIdentity
alaAutoConfigTrapsObj = _AlaAutoConfigTrapsObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 83, 1, 1, 3)
)


class _AlaAutoConfigAutoFabricEnableTrap_Type(Integer32):
    """Custom type alaAutoConfigAutoFabricEnableTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaAutoConfigAutoFabricEnableTrap_Type.__name__ = "Integer32"
_AlaAutoConfigAutoFabricEnableTrap_Object = MibScalar
alaAutoConfigAutoFabricEnableTrap = _AlaAutoConfigAutoFabricEnableTrap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 83, 1, 1, 3, 1),
    _AlaAutoConfigAutoFabricEnableTrap_Type()
)
alaAutoConfigAutoFabricEnableTrap.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaAutoConfigAutoFabricEnableTrap.setStatus("current")
_AlaAUTOCONFIGMIBConformance_ObjectIdentity = ObjectIdentity
alaAUTOCONFIGMIBConformance = _AlaAUTOCONFIGMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 83, 1, 2)
)
if mibBuilder.loadTexts:
    alaAUTOCONFIGMIBConformance.setStatus("current")
_AlaAUTOCONFIGMIBGroups_ObjectIdentity = ObjectIdentity
alaAUTOCONFIGMIBGroups = _AlaAUTOCONFIGMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 83, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alaAUTOCONFIGMIBGroups.setStatus("current")
_AlaAUTOCONFIGMIBCompliances_ObjectIdentity = ObjectIdentity
alaAUTOCONFIGMIBCompliances = _AlaAUTOCONFIGMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 83, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alaAUTOCONFIGMIBCompliances.setStatus("current")

# Managed Objects groups

alaAutoConfigGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 83, 1, 2, 1, 2)
)
alaAutoConfigGlobalGroup.setObjects(
      *(("ALCATEL-ENT1-AUTO-CONFIG-MIB", "alaAutoConfigAbort"),
        ("ALCATEL-ENT1-AUTO-CONFIG-MIB", "alaAutoConfigAutoFabricEnableTrap"))
)
if mibBuilder.loadTexts:
    alaAutoConfigGlobalGroup.setStatus("current")


# Notification objects

alaAutoConfigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 83, 1, 0, 1)
)
alaAutoConfigTrap.setObjects(
    ("ALCATEL-ENT1-AUTO-CONFIG-MIB", "alaAutoConfigAutoFabricEnableTrap")
)
if mibBuilder.loadTexts:
    alaAutoConfigTrap.setStatus(
        "current"
    )


# Notifications groups

alaAUTOCONFIGNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 83, 1, 2, 1, 1)
)
alaAUTOCONFIGNotificationGroup.setObjects(
    ("ALCATEL-ENT1-AUTO-CONFIG-MIB", "alaAutoConfigTrap")
)
if mibBuilder.loadTexts:
    alaAUTOCONFIGNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alaAUTOCONFIGMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 83, 1, 2, 2, 1)
)
alaAUTOCONFIGMIBCompliance.setObjects(
    ("ALCATEL-ENT1-AUTO-CONFIG-MIB", "alaAUTOCONFIGNotificationGroup")
)
if mibBuilder.loadTexts:
    alaAUTOCONFIGMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-ENT1-AUTO-CONFIG-MIB",
    **{"alaAUTOCONFIGMIB": alaAUTOCONFIGMIB,
       "alaAUTOCONFIGMIBNotifications": alaAUTOCONFIGMIBNotifications,
       "alaAutoConfigTrap": alaAutoConfigTrap,
       "alaAUTOCONFIGMIBObjects": alaAUTOCONFIGMIBObjects,
       "alaAUTOCONFIGGlobal": alaAUTOCONFIGGlobal,
       "alaAutoConfigAbort": alaAutoConfigAbort,
       "alaAUTOCONFIGNotificationObjects": alaAUTOCONFIGNotificationObjects,
       "alaAutoConfigTrapsObj": alaAutoConfigTrapsObj,
       "alaAutoConfigAutoFabricEnableTrap": alaAutoConfigAutoFabricEnableTrap,
       "alaAUTOCONFIGMIBConformance": alaAUTOCONFIGMIBConformance,
       "alaAUTOCONFIGMIBGroups": alaAUTOCONFIGMIBGroups,
       "alaAUTOCONFIGNotificationGroup": alaAUTOCONFIGNotificationGroup,
       "alaAutoConfigGlobalGroup": alaAutoConfigGlobalGroup,
       "alaAUTOCONFIGMIBCompliances": alaAUTOCONFIGMIBCompliances,
       "alaAUTOCONFIGMIBCompliance": alaAUTOCONFIGMIBCompliance}
)
