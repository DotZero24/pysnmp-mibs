# SNMP MIB module (OS-ETHOAM-MD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OS-ETHOAM-MD-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:04:40 2025
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

(EntryValidator,
 PortList,
 oaOptiSwitch) = mibBuilder.importSymbols(
    "OS-COMMON-TC-MIB",
    "EntryValidator",
    "PortList",
    "oaOptiSwitch")

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

osEthOamMd = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 13)
)
if mibBuilder.loadTexts:
    osEthOamMd.setRevisions(
        ("2010-08-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OsEthOamMdCapabilities_ObjectIdentity = ObjectIdentity
osEthOamMdCapabilities = _OsEthOamMdCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 13, 1)
)


class _OsEthOamMdSupport_Type(Integer32):
    """Custom type osEthOamMdSupport based on Integer32"""
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


_OsEthOamMdSupport_Type.__name__ = "Integer32"
_OsEthOamMdSupport_Object = MibScalar
osEthOamMdSupport = _OsEthOamMdSupport_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 13, 1, 1),
    _OsEthOamMdSupport_Type()
)
osEthOamMdSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamMdSupport.setStatus("current")
_OsEthOamMdTable_Object = MibTable
osEthOamMdTable = _OsEthOamMdTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 13, 2)
)
if mibBuilder.loadTexts:
    osEthOamMdTable.setStatus("current")
_OsEthOamMdEntry_Object = MibTableRow
osEthOamMdEntry = _OsEthOamMdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 13, 2, 1)
)
osEthOamMdEntry.setIndexNames(
    (0, "OS-ETHOAM-MD-MIB", "osEthOamMdLevel"),
)
if mibBuilder.loadTexts:
    osEthOamMdEntry.setStatus("current")


class _OsEthOamMdLevel_Type(Integer32):
    """Custom type osEthOamMdLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_OsEthOamMdLevel_Type.__name__ = "Integer32"
_OsEthOamMdLevel_Object = MibTableColumn
osEthOamMdLevel = _OsEthOamMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 13, 2, 1, 1),
    _OsEthOamMdLevel_Type()
)
osEthOamMdLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osEthOamMdLevel.setStatus("current")


class _OsEthOamMdFormat_Type(Integer32):
    """Custom type osEthOamMdFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("dnsLikeName", 2),
          ("macAddressAndUint", 3),
          ("charString", 4))
    )


_OsEthOamMdFormat_Type.__name__ = "Integer32"
_OsEthOamMdFormat_Object = MibTableColumn
osEthOamMdFormat = _OsEthOamMdFormat_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 13, 2, 1, 2),
    _OsEthOamMdFormat_Type()
)
osEthOamMdFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    osEthOamMdFormat.setStatus("current")


class _OsEthOamMdName_Type(OctetString):
    """Custom type osEthOamMdName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 43),
    )


_OsEthOamMdName_Type.__name__ = "OctetString"
_OsEthOamMdName_Object = MibTableColumn
osEthOamMdName = _OsEthOamMdName_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 13, 2, 1, 3),
    _OsEthOamMdName_Type()
)
osEthOamMdName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    osEthOamMdName.setStatus("current")
_OsEthOamMdCPorts_Type = PortList
_OsEthOamMdCPorts_Object = MibTableColumn
osEthOamMdCPorts = _OsEthOamMdCPorts_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 13, 2, 1, 4),
    _OsEthOamMdCPorts_Type()
)
osEthOamMdCPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osEthOamMdCPorts.setStatus("current")
_OsEthOamMdAdminStatus_Type = EntryValidator
_OsEthOamMdAdminStatus_Object = MibTableColumn
osEthOamMdAdminStatus = _OsEthOamMdAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 13, 2, 1, 90),
    _OsEthOamMdAdminStatus_Type()
)
osEthOamMdAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    osEthOamMdAdminStatus.setStatus("current")
_OsEthOamMdConformance_ObjectIdentity = ObjectIdentity
osEthOamMdConformance = _OsEthOamMdConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 13, 100)
)
_OsEthOamMdMIBCompliances_ObjectIdentity = ObjectIdentity
osEthOamMdMIBCompliances = _OsEthOamMdMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 13, 100, 1)
)
_OsEthOamMdMIBGroups_ObjectIdentity = ObjectIdentity
osEthOamMdMIBGroups = _OsEthOamMdMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 13, 100, 2)
)

# Managed Objects groups

osEthOamMdMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 2, 13, 100, 2, 1)
)
osEthOamMdMandatoryGroup.setObjects(
      *(("OS-ETHOAM-MD-MIB", "osEthOamMdSupport"),
        ("OS-ETHOAM-MD-MIB", "osEthOamMdFormat"),
        ("OS-ETHOAM-MD-MIB", "osEthOamMdName"),
        ("OS-ETHOAM-MD-MIB", "osEthOamMdCPorts"),
        ("OS-ETHOAM-MD-MIB", "osEthOamMdAdminStatus"))
)
if mibBuilder.loadTexts:
    osEthOamMdMandatoryGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

osEthOamMdMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6926, 2, 13, 100, 1, 1)
)
osEthOamMdMIBCompliance.setObjects(
    ("OS-ETHOAM-MD-MIB", "osEthOamMdMandatoryGroup")
)
if mibBuilder.loadTexts:
    osEthOamMdMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OS-ETHOAM-MD-MIB",
    **{"osEthOamMd": osEthOamMd,
       "osEthOamMdCapabilities": osEthOamMdCapabilities,
       "osEthOamMdSupport": osEthOamMdSupport,
       "osEthOamMdTable": osEthOamMdTable,
       "osEthOamMdEntry": osEthOamMdEntry,
       "osEthOamMdLevel": osEthOamMdLevel,
       "osEthOamMdFormat": osEthOamMdFormat,
       "osEthOamMdName": osEthOamMdName,
       "osEthOamMdCPorts": osEthOamMdCPorts,
       "osEthOamMdAdminStatus": osEthOamMdAdminStatus,
       "osEthOamMdConformance": osEthOamMdConformance,
       "osEthOamMdMIBCompliances": osEthOamMdMIBCompliances,
       "osEthOamMdMIBCompliance": osEthOamMdMIBCompliance,
       "osEthOamMdMIBGroups": osEthOamMdMIBGroups,
       "osEthOamMdMandatoryGroup": osEthOamMdMandatoryGroup}
)
