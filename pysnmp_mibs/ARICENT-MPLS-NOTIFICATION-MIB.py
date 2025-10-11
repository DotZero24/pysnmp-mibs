# SNMP MIB module (ARICENT-MPLS-NOTIFICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-MPLS-NOTIFICATION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:43:41 2025
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

(PwIndexType,) = mibBuilder.importSymbols(
    "PW-TC-STD-MIB",
    "PwIndexType")

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
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsMplsNotificationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 13, 10)
)
if mibBuilder.loadTexts:
    fsMplsNotificationMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsMplsNotifications_ObjectIdentity = ObjectIdentity
fsMplsNotifications = _FsMplsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 13, 10, 0)
)


class _FsMplsPwNotifStatusStr_Type(DisplayString):
    """Custom type fsMplsPwNotifStatusStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_FsMplsPwNotifStatusStr_Type.__name__ = "DisplayString"
_FsMplsPwNotifStatusStr_Object = MibScalar
fsMplsPwNotifStatusStr = _FsMplsPwNotifStatusStr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 10, 0, 1),
    _FsMplsPwNotifStatusStr_Type()
)
fsMplsPwNotifStatusStr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMplsPwNotifStatusStr.setStatus("current")
_FsMplsPwIndex_Type = PwIndexType
_FsMplsPwIndex_Object = MibScalar
fsMplsPwIndex = _FsMplsPwIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 10, 0, 2),
    _FsMplsPwIndex_Type()
)
fsMplsPwIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMplsPwIndex.setStatus("current")
_FsMplsNotifConfig_ObjectIdentity = ObjectIdentity
fsMplsNotifConfig = _FsMplsNotifConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 13, 10, 1)
)


class _FsMplsPwStatusNotifEnable_Type(TruthValue):
    """Custom type fsMplsPwStatusNotifEnable based on TruthValue"""
    defaultValue = 2


_FsMplsPwStatusNotifEnable_Type.__name__ = "TruthValue"
_FsMplsPwStatusNotifEnable_Object = MibScalar
fsMplsPwStatusNotifEnable = _FsMplsPwStatusNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 10, 1, 1),
    _FsMplsPwStatusNotifEnable_Type()
)
fsMplsPwStatusNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsPwStatusNotifEnable.setStatus("current")


class _FsMplsPwOAMStatusNotifEnable_Type(TruthValue):
    """Custom type fsMplsPwOAMStatusNotifEnable based on TruthValue"""
    defaultValue = 2


_FsMplsPwOAMStatusNotifEnable_Type.__name__ = "TruthValue"
_FsMplsPwOAMStatusNotifEnable_Object = MibScalar
fsMplsPwOAMStatusNotifEnable = _FsMplsPwOAMStatusNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 10, 1, 2),
    _FsMplsPwOAMStatusNotifEnable_Type()
)
fsMplsPwOAMStatusNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsPwOAMStatusNotifEnable.setStatus("deprecated")

# Managed Objects groups


# Notification objects

fsMplsPwOamStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 13, 10, 0, 3)
)
fsMplsPwOamStatus.setObjects(
      *(("ARICENT-MPLS-NOTIFICATION-MIB", "fsMplsPwIndex"),
        ("ARICENT-MPLS-NOTIFICATION-MIB", "fsMplsPwNotifStatusStr"))
)
if mibBuilder.loadTexts:
    fsMplsPwOamStatus.setStatus(
        "deprecated"
    )

fsMplsPwStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 13, 10, 0, 4)
)
fsMplsPwStatus.setObjects(
      *(("ARICENT-MPLS-NOTIFICATION-MIB", "fsMplsPwIndex"),
        ("ARICENT-MPLS-NOTIFICATION-MIB", "fsMplsPwNotifStatusStr"))
)
if mibBuilder.loadTexts:
    fsMplsPwStatus.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-MPLS-NOTIFICATION-MIB",
    **{"fsMplsNotificationMIB": fsMplsNotificationMIB,
       "fsMplsNotifications": fsMplsNotifications,
       "fsMplsPwNotifStatusStr": fsMplsPwNotifStatusStr,
       "fsMplsPwIndex": fsMplsPwIndex,
       "fsMplsPwOamStatus": fsMplsPwOamStatus,
       "fsMplsPwStatus": fsMplsPwStatus,
       "fsMplsNotifConfig": fsMplsNotifConfig,
       "fsMplsPwStatusNotifEnable": fsMplsPwStatusNotifEnable,
       "fsMplsPwOAMStatusNotifEnable": fsMplsPwOAMStatusNotifEnable}
)
