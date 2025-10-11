# SNMP MIB module (ZYXEL-SERVICE-REGISTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zyxel/ZYXEL-SERVICE-REGISTER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:01:40 2025
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

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelServiceRegister = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 118)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelServiceRegisterSetup_ObjectIdentity = ObjectIdentity
zyxelServiceRegisterSetup = _ZyxelServiceRegisterSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 118, 1)
)
_ZyxelServiceRegisterStatus_ObjectIdentity = ObjectIdentity
zyxelServiceRegisterStatus = _ZyxelServiceRegisterStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 118, 2)
)
_ZyxelServiceRegisterServiceTable_Object = MibTable
zyxelServiceRegisterServiceTable = _ZyxelServiceRegisterServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 118, 2, 1)
)
if mibBuilder.loadTexts:
    zyxelServiceRegisterServiceTable.setStatus("current")
_ZyxelServiceRegisterServiceEntry_Object = MibTableRow
zyxelServiceRegisterServiceEntry = _ZyxelServiceRegisterServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 118, 2, 1, 1)
)
zyxelServiceRegisterServiceEntry.setIndexNames(
    (0, "ZYXEL-SERVICE-REGISTER-MIB", "zyServiceRegisterServiceName"),
)
if mibBuilder.loadTexts:
    zyxelServiceRegisterServiceEntry.setStatus("current")
_ZyServiceRegisterServiceName_Type = OctetString
_ZyServiceRegisterServiceName_Object = MibTableColumn
zyServiceRegisterServiceName = _ZyServiceRegisterServiceName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 118, 2, 1, 1, 1),
    _ZyServiceRegisterServiceName_Type()
)
zyServiceRegisterServiceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyServiceRegisterServiceName.setStatus("current")


class _ZyServiceRegisterServiceStatus_Type(Integer32):
    """Custom type zyServiceRegisterServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notLicensed", 0),
          ("licensed", 1))
    )


_ZyServiceRegisterServiceStatus_Type.__name__ = "Integer32"
_ZyServiceRegisterServiceStatus_Object = MibTableColumn
zyServiceRegisterServiceStatus = _ZyServiceRegisterServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 118, 2, 1, 1, 2),
    _ZyServiceRegisterServiceStatus_Type()
)
zyServiceRegisterServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyServiceRegisterServiceStatus.setStatus("current")


class _ZyServiceRegisterServiceType_Type(Integer32):
    """Custom type zyServiceRegisterServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("trial", 1),
          ("standard", 2))
    )


_ZyServiceRegisterServiceType_Type.__name__ = "Integer32"
_ZyServiceRegisterServiceType_Object = MibTableColumn
zyServiceRegisterServiceType = _ZyServiceRegisterServiceType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 118, 2, 1, 1, 3),
    _ZyServiceRegisterServiceType_Type()
)
zyServiceRegisterServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyServiceRegisterServiceType.setStatus("current")
_ZyServiceRegisterServiceExpiration_Type = Integer32
_ZyServiceRegisterServiceExpiration_Object = MibTableColumn
zyServiceRegisterServiceExpiration = _ZyServiceRegisterServiceExpiration_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 118, 2, 1, 1, 4),
    _ZyServiceRegisterServiceExpiration_Type()
)
zyServiceRegisterServiceExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyServiceRegisterServiceExpiration.setStatus("current")
_ZyxelServiceRegisterTrapInfoObjects_ObjectIdentity = ObjectIdentity
zyxelServiceRegisterTrapInfoObjects = _ZyxelServiceRegisterTrapInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 118, 3)
)
_ZyxelServiceRegisterNotifications_ObjectIdentity = ObjectIdentity
zyxelServiceRegisterNotifications = _ZyxelServiceRegisterNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 118, 4)
)

# Managed Objects groups


# Notification objects

zyServiceRegisterTheServiceHasExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 118, 4, 1)
)
zyServiceRegisterTheServiceHasExpired.setObjects(
    ("ZYXEL-SERVICE-REGISTER-MIB", "zyServiceRegisterServiceName")
)
if mibBuilder.loadTexts:
    zyServiceRegisterTheServiceHasExpired.setStatus(
        "current"
    )

zyServiceRegisterTheServiceIsDueToExpireInSomeHours = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 118, 4, 2)
)
zyServiceRegisterTheServiceIsDueToExpireInSomeHours.setObjects(
      *(("ZYXEL-SERVICE-REGISTER-MIB", "zyServiceRegisterServiceName"),
        ("ZYXEL-SERVICE-REGISTER-MIB", "zyServiceRegisterServiceExpiration"))
)
if mibBuilder.loadTexts:
    zyServiceRegisterTheServiceIsDueToExpireInSomeHours.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-SERVICE-REGISTER-MIB",
    **{"zyxelServiceRegister": zyxelServiceRegister,
       "zyxelServiceRegisterSetup": zyxelServiceRegisterSetup,
       "zyxelServiceRegisterStatus": zyxelServiceRegisterStatus,
       "zyxelServiceRegisterServiceTable": zyxelServiceRegisterServiceTable,
       "zyxelServiceRegisterServiceEntry": zyxelServiceRegisterServiceEntry,
       "zyServiceRegisterServiceName": zyServiceRegisterServiceName,
       "zyServiceRegisterServiceStatus": zyServiceRegisterServiceStatus,
       "zyServiceRegisterServiceType": zyServiceRegisterServiceType,
       "zyServiceRegisterServiceExpiration": zyServiceRegisterServiceExpiration,
       "zyxelServiceRegisterTrapInfoObjects": zyxelServiceRegisterTrapInfoObjects,
       "zyxelServiceRegisterNotifications": zyxelServiceRegisterNotifications,
       "zyServiceRegisterTheServiceHasExpired": zyServiceRegisterTheServiceHasExpired,
       "zyServiceRegisterTheServiceIsDueToExpireInSomeHours": zyServiceRegisterTheServiceIsDueToExpireInSomeHours}
)
