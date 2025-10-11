# SNMP MIB module (STONESOFT-IPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/forcepoint/STONESOFT-IPS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:06:27 2025
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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")

(stonesoftIPS,
 stonesoftModules) = mibBuilder.importSymbols(
    "STONESOFT-SMI-MIB",
    "stonesoftIPS",
    "stonesoftModules")


# MODULE-IDENTITY

stonesoftIPSMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 3, 3)
)
if mibBuilder.loadTexts:
    stonesoftIPSMibModule.setRevisions(
        ("2007-01-04 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpsObjects_ObjectIdentity = ObjectIdentity
ipsObjects = _IpsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 5, 5, 1)
)
_IpsSoftwareVersion_Type = DisplayString
_IpsSoftwareVersion_Object = MibScalar
ipsSoftwareVersion = _IpsSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 5, 1, 1),
    _IpsSoftwareVersion_Type()
)
ipsSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsSoftwareVersion.setStatus("current")
_IpsSecurityPolicy_Type = DisplayString
_IpsSecurityPolicy_Object = MibScalar
ipsSecurityPolicy = _IpsSecurityPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 5, 1, 2),
    _IpsSecurityPolicy_Type()
)
ipsSecurityPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsSecurityPolicy.setStatus("current")
_IpsPolicyTime_Type = TimeStamp
_IpsPolicyTime_Object = MibScalar
ipsPolicyTime = _IpsPolicyTime_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 5, 1, 3),
    _IpsPolicyTime_Type()
)
ipsPolicyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsPolicyTime.setStatus("current")
_IpsEvents_ObjectIdentity = ObjectIdentity
ipsEvents = _IpsEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 5, 5, 2)
)
_IpsEventsV2_ObjectIdentity = ObjectIdentity
ipsEventsV2 = _IpsEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 5, 5, 2, 0)
)
_IpsConformance_ObjectIdentity = ObjectIdentity
ipsConformance = _IpsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 5, 5, 3)
)
_IpsGroups_ObjectIdentity = ObjectIdentity
ipsGroups = _IpsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 5, 5, 3, 1)
)
_IpsCompliances_ObjectIdentity = ObjectIdentity
ipsCompliances = _IpsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 5, 5, 3, 2)
)

# Managed Objects groups

ipsGeneralInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1369, 5, 5, 3, 1, 1)
)
ipsGeneralInformationGroup.setObjects(
      *(("STONESOFT-IPS-MIB", "ipsSoftwareVersion"),
        ("STONESOFT-IPS-MIB", "ipsSecurityPolicy"),
        ("STONESOFT-IPS-MIB", "ipsPolicyTime"))
)
if mibBuilder.loadTexts:
    ipsGeneralInformationGroup.setStatus("current")


# Notification objects

ipsPolicyInstall = NotificationType(
    (1, 3, 6, 1, 4, 1, 1369, 5, 5, 2, 0, 1)
)
ipsPolicyInstall.setObjects(
    ("STONESOFT-IPS-MIB", "ipsSecurityPolicy")
)
if mibBuilder.loadTexts:
    ipsPolicyInstall.setStatus(
        "current"
    )


# Notifications groups

ipsGeneralNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1369, 5, 5, 3, 1, 2)
)
ipsGeneralNotificationsGroup.setObjects(
    ("STONESOFT-IPS-MIB", "ipsPolicyInstall")
)
if mibBuilder.loadTexts:
    ipsGeneralNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ipsCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1369, 5, 5, 3, 2, 1)
)
ipsCompliance1.setObjects(
      *(("STONESOFT-IPS-MIB", "ipsGeneralInformationGroup"),
        ("STONESOFT-IPS-MIB", "ipsGeneralNotificationsGroup"))
)
if mibBuilder.loadTexts:
    ipsCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STONESOFT-IPS-MIB",
    **{"stonesoftIPSMibModule": stonesoftIPSMibModule,
       "ipsObjects": ipsObjects,
       "ipsSoftwareVersion": ipsSoftwareVersion,
       "ipsSecurityPolicy": ipsSecurityPolicy,
       "ipsPolicyTime": ipsPolicyTime,
       "ipsEvents": ipsEvents,
       "ipsEventsV2": ipsEventsV2,
       "ipsPolicyInstall": ipsPolicyInstall,
       "ipsConformance": ipsConformance,
       "ipsGroups": ipsGroups,
       "ipsGeneralInformationGroup": ipsGeneralInformationGroup,
       "ipsGeneralNotificationsGroup": ipsGeneralNotificationsGroup,
       "ipsCompliances": ipsCompliances,
       "ipsCompliance1": ipsCompliance1}
)
