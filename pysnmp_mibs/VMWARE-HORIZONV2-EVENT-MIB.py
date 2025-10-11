# SNMP MIB module (VMWARE-HORIZONV2-EVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/vmware/VMWARE-HORIZONV2-EVENT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:23:20 2025
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(vmwHorizonv2,) = mibBuilder.importSymbols(
    "VMWARE-ROOT-MIB",
    "vmwHorizonv2")


# MODULE-IDENTITY

vmwHorizonv2MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 150, 1)
)
if mibBuilder.loadTexts:
    vmwHorizonv2MIB.setRevisions(
        ("2023-07-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VmwHorizonv2Notifications_ObjectIdentity = ObjectIdentity
vmwHorizonv2Notifications = _VmwHorizonv2Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 150, 0)
)
_VmwHorizonv2MIBConformance_ObjectIdentity = ObjectIdentity
vmwHorizonv2MIBConformance = _VmwHorizonv2MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 150, 1, 1)
)
_VmwHorizonv2MIBCompliances_ObjectIdentity = ObjectIdentity
vmwHorizonv2MIBCompliances = _VmwHorizonv2MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 150, 1, 1, 1)
)
_VmwHorizonv2MIBGroups_ObjectIdentity = ObjectIdentity
vmwHorizonv2MIBGroups = _VmwHorizonv2MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 150, 1, 1, 2)
)
_VmwHorizonv2LicenseEvents_ObjectIdentity = ObjectIdentity
vmwHorizonv2LicenseEvents = _VmwHorizonv2LicenseEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 150, 5)
)
_VmwHorizonv2LicenseFailureStatus_Type = SnmpAdminString
_VmwHorizonv2LicenseFailureStatus_Object = MibScalar
vmwHorizonv2LicenseFailureStatus = _VmwHorizonv2LicenseFailureStatus_Object(
    (1, 3, 6, 1, 4, 1, 6876, 150, 5, 1),
    _VmwHorizonv2LicenseFailureStatus_Type()
)
vmwHorizonv2LicenseFailureStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwHorizonv2LicenseFailureStatus.setStatus("current")

# Managed Objects groups

vmwHorizonv2ObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 150, 1, 1, 2, 1)
)
vmwHorizonv2ObjectGroup.setObjects(
    ("VMWARE-HORIZONV2-EVENT-MIB", "vmwHorizonv2LicenseFailureStatus")
)
if mibBuilder.loadTexts:
    vmwHorizonv2ObjectGroup.setStatus("current")


# Notification objects

vmwHorizonv2LicenseEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 150, 0, 2)
)
vmwHorizonv2LicenseEventTrap.setObjects(
    ("VMWARE-HORIZONV2-EVENT-MIB", "vmwHorizonv2LicenseFailureStatus")
)
if mibBuilder.loadTexts:
    vmwHorizonv2LicenseEventTrap.setStatus(
        "current"
    )


# Notifications groups

vmwHorizonv2NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 150, 1, 1, 2, 2)
)
vmwHorizonv2NotificationGroup.setObjects(
    ("VMWARE-HORIZONV2-EVENT-MIB", "vmwHorizonv2LicenseEventTrap")
)
if mibBuilder.loadTexts:
    vmwHorizonv2NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vmwHorizonv2MIBBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 150, 1, 1, 1, 1)
)
vmwHorizonv2MIBBasicCompliance.setObjects(
      *(("VMWARE-HORIZONV2-EVENT-MIB", "vmwHorizonv2NotificationGroup"),
        ("VMWARE-HORIZONV2-EVENT-MIB", "vmwHorizonv2ObjectGroup"))
)
if mibBuilder.loadTexts:
    vmwHorizonv2MIBBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMWARE-HORIZONV2-EVENT-MIB",
    **{"vmwHorizonv2Notifications": vmwHorizonv2Notifications,
       "vmwHorizonv2LicenseEventTrap": vmwHorizonv2LicenseEventTrap,
       "vmwHorizonv2MIB": vmwHorizonv2MIB,
       "vmwHorizonv2MIBConformance": vmwHorizonv2MIBConformance,
       "vmwHorizonv2MIBCompliances": vmwHorizonv2MIBCompliances,
       "vmwHorizonv2MIBBasicCompliance": vmwHorizonv2MIBBasicCompliance,
       "vmwHorizonv2MIBGroups": vmwHorizonv2MIBGroups,
       "vmwHorizonv2ObjectGroup": vmwHorizonv2ObjectGroup,
       "vmwHorizonv2NotificationGroup": vmwHorizonv2NotificationGroup,
       "vmwHorizonv2LicenseEvents": vmwHorizonv2LicenseEvents,
       "vmwHorizonv2LicenseFailureStatus": vmwHorizonv2LicenseFailureStatus}
)
