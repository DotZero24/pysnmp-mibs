# SNMP MIB module (MX-SYSTEM-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-SYSTEM-MGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:37 2025
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

(mediatrixMgmt,) = mibBuilder.importSymbols(
    "MX-SMI",
    "mediatrixMgmt")

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

sysMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 10, 15)
)
if mibBuilder.loadTexts:
    sysMgmtMIB.setRevisions(
        ("2010-03-01 00:00",
         "1901-08-29 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SysMgmtMIBObjects_ObjectIdentity = ObjectIdentity
sysMgmtMIBObjects = _SysMgmtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 10, 15, 1)
)


class _SysMacAddress_Type(OctetString):
    """Custom type sysMacAddress based on OctetString"""
    defaultValue = OctetString(" ")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_SysMacAddress_Type.__name__ = "OctetString"
_SysMacAddress_Object = MibScalar
sysMacAddress = _SysMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 15, 1, 1),
    _SysMacAddress_Type()
)
sysMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMacAddress.setStatus("current")


class _SysHardwareVersion_Type(OctetString):
    """Custom type sysHardwareVersion based on OctetString"""
    defaultValue = OctetString(" ")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SysHardwareVersion_Type.__name__ = "OctetString"
_SysHardwareVersion_Object = MibScalar
sysHardwareVersion = _SysHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 15, 1, 2),
    _SysHardwareVersion_Type()
)
sysHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHardwareVersion.setStatus("current")


class _SysSoftwareVersion_Type(OctetString):
    """Custom type sysSoftwareVersion based on OctetString"""
    defaultValue = OctetString(" ")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SysSoftwareVersion_Type.__name__ = "OctetString"
_SysSoftwareVersion_Object = MibScalar
sysSoftwareVersion = _SysSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 15, 1, 3),
    _SysSoftwareVersion_Type()
)
sysSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSoftwareVersion.setStatus("current")


class _SysMibVersion_Type(OctetString):
    """Custom type sysMibVersion based on OctetString"""
    defaultValue = OctetString(" ")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SysMibVersion_Type.__name__ = "OctetString"
_SysMibVersion_Object = MibScalar
sysMibVersion = _SysMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 15, 1, 4),
    _SysMibVersion_Type()
)
sysMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMibVersion.setStatus("current")


class _SysSerialNumber_Type(OctetString):
    """Custom type sysSerialNumber based on OctetString"""
    defaultValue = OctetString(" ")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_SysSerialNumber_Type.__name__ = "OctetString"
_SysSerialNumber_Object = MibScalar
sysSerialNumber = _SysSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 15, 1, 5),
    _SysSerialNumber_Type()
)
sysSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSerialNumber.setStatus("current")
_SysMgmtConformance_ObjectIdentity = ObjectIdentity
sysMgmtConformance = _SysMgmtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 10, 15, 2)
)
_SysMgmtCompliances_ObjectIdentity = ObjectIdentity
sysMgmtCompliances = _SysMgmtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 10, 15, 2, 1)
)
_SysMgmtGroups_ObjectIdentity = ObjectIdentity
sysMgmtGroups = _SysMgmtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 10, 15, 2, 2)
)

# Managed Objects groups

sysMgmtGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 10, 15, 2, 2, 1)
)
sysMgmtGroupVer1.setObjects(
      *(("MX-SYSTEM-MGMT-MIB", "sysMacAddress"),
        ("MX-SYSTEM-MGMT-MIB", "sysHardwareVersion"),
        ("MX-SYSTEM-MGMT-MIB", "sysSoftwareVersion"),
        ("MX-SYSTEM-MGMT-MIB", "sysMibVersion"),
        ("MX-SYSTEM-MGMT-MIB", "sysSerialNumber"))
)
if mibBuilder.loadTexts:
    sysMgmtGroupVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

sysMgmtComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 10, 15, 2, 1, 1)
)
sysMgmtComplVer1.setObjects(
    ("MX-SYSTEM-MGMT-MIB", "sysMgmtGroupVer1")
)
if mibBuilder.loadTexts:
    sysMgmtComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-SYSTEM-MGMT-MIB",
    **{"sysMgmtMIB": sysMgmtMIB,
       "sysMgmtMIBObjects": sysMgmtMIBObjects,
       "sysMacAddress": sysMacAddress,
       "sysHardwareVersion": sysHardwareVersion,
       "sysSoftwareVersion": sysSoftwareVersion,
       "sysMibVersion": sysMibVersion,
       "sysSerialNumber": sysSerialNumber,
       "sysMgmtConformance": sysMgmtConformance,
       "sysMgmtCompliances": sysMgmtCompliances,
       "sysMgmtComplVer1": sysMgmtComplVer1,
       "sysMgmtGroups": sysMgmtGroups,
       "sysMgmtGroupVer1": sysMgmtGroupVer1}
)
