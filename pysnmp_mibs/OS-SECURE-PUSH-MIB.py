# SNMP MIB module (OS-SECURE-PUSH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OS-SECURE-PUSH-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:03:51 2025
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

(oaOptiSwitch,) = mibBuilder.importSymbols(
    "OS-COMMON-TC-MIB",
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

osSecurePush = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 24)
)
if mibBuilder.loadTexts:
    osSecurePush.setRevisions(
        ("2012-12-19 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OsSecurePushGeneral_ObjectIdentity = ObjectIdentity
osSecurePushGeneral = _OsSecurePushGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 24, 1)
)


class _OsSecurePushSupport_Type(Integer32):
    """Custom type osSecurePushSupport based on Integer32"""
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


_OsSecurePushSupport_Type.__name__ = "Integer32"
_OsSecurePushSupport_Object = MibScalar
osSecurePushSupport = _OsSecurePushSupport_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 24, 1, 1),
    _OsSecurePushSupport_Type()
)
osSecurePushSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osSecurePushSupport.setStatus("current")


class _OsSecurePushConfAdminStatus_Type(Integer32):
    """Custom type osSecurePushConfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("askFromServer", 2))
    )


_OsSecurePushConfAdminStatus_Type.__name__ = "Integer32"
_OsSecurePushConfAdminStatus_Object = MibScalar
osSecurePushConfAdminStatus = _OsSecurePushConfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 24, 1, 2),
    _OsSecurePushConfAdminStatus_Type()
)
osSecurePushConfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osSecurePushConfAdminStatus.setStatus("current")
_OsSecurePushConformance_ObjectIdentity = ObjectIdentity
osSecurePushConformance = _OsSecurePushConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 24, 100)
)
_OsSecurePushMIBCompliances_ObjectIdentity = ObjectIdentity
osSecurePushMIBCompliances = _OsSecurePushMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 24, 100, 1)
)
_OsSecurePushMIBGroups_ObjectIdentity = ObjectIdentity
osSecurePushMIBGroups = _OsSecurePushMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 24, 100, 2)
)

# Managed Objects groups

osSecurePushMibMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 2, 24, 100, 2, 1)
)
osSecurePushMibMandatoryGroup.setObjects(
      *(("OS-SECURE-PUSH-MIB", "osSecurePushSupport"),
        ("OS-SECURE-PUSH-MIB", "osSecurePushConfAdminStatus"))
)
if mibBuilder.loadTexts:
    osSecurePushMibMandatoryGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

osSecurePushMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6926, 2, 24, 100, 1, 1)
)
osSecurePushMIBCompliance.setObjects(
    ("OS-SECURE-PUSH-MIB", "osSecurePushMibMandatoryGroup")
)
if mibBuilder.loadTexts:
    osSecurePushMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OS-SECURE-PUSH-MIB",
    **{"osSecurePush": osSecurePush,
       "osSecurePushGeneral": osSecurePushGeneral,
       "osSecurePushSupport": osSecurePushSupport,
       "osSecurePushConfAdminStatus": osSecurePushConfAdminStatus,
       "osSecurePushConformance": osSecurePushConformance,
       "osSecurePushMIBCompliances": osSecurePushMIBCompliances,
       "osSecurePushMIBCompliance": osSecurePushMIBCompliance,
       "osSecurePushMIBGroups": osSecurePushMIBGroups,
       "osSecurePushMibMandatoryGroup": osSecurePushMibMandatoryGroup}
)
