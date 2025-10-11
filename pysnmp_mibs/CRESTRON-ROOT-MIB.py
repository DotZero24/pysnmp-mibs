# SNMP MIB module (CRESTRON-ROOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/crestron/CRESTRON-ROOT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:03:47 2025
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

crestron = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3212)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TcpPort(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class UdpPort(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class Digital(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CrestronAdmin_ObjectIdentity = ObjectIdentity
crestronAdmin = _CrestronAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 1)
)
_CrestronNotifications_ObjectIdentity = ObjectIdentity
crestronNotifications = _CrestronNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 2)
)
_CrestronObjects_ObjectIdentity = ObjectIdentity
crestronObjects = _CrestronObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 3)
)
_CrestronRootMIBVersion_Type = Integer32
_CrestronRootMIBVersion_Object = MibScalar
crestronRootMIBVersion = _CrestronRootMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 3212, 3, 1),
    _CrestronRootMIBVersion_Type()
)
crestronRootMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crestronRootMIBVersion.setStatus("current")
_CrestronConformance_ObjectIdentity = ObjectIdentity
crestronConformance = _CrestronConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 5)
)
_CrestronCompliances_ObjectIdentity = ObjectIdentity
crestronCompliances = _CrestronCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 5, 2)
)
_CrestronGroups_ObjectIdentity = ObjectIdentity
crestronGroups = _CrestronGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 5, 3)
)
_CrestronCommon_ObjectIdentity = ObjectIdentity
crestronCommon = _CrestronCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 6)
)
_CrestronControl_ObjectIdentity = ObjectIdentity
crestronControl = _CrestronControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 7)
)
_CrestronTouch_ObjectIdentity = ObjectIdentity
crestronTouch = _CrestronTouch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 8)
)

# Managed Objects groups

crestronRootAllObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3212, 5, 3, 1)
)
crestronRootAllObjects.setObjects(
    ("CRESTRON-ROOT-MIB", "crestronRootMIBVersion")
)
if mibBuilder.loadTexts:
    crestronRootAllObjects.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CRESTRON-ROOT-MIB",
    **{"TcpPort": TcpPort,
       "UdpPort": UdpPort,
       "Digital": Digital,
       "crestron": crestron,
       "crestronAdmin": crestronAdmin,
       "crestronNotifications": crestronNotifications,
       "crestronObjects": crestronObjects,
       "crestronRootMIBVersion": crestronRootMIBVersion,
       "crestronConformance": crestronConformance,
       "crestronCompliances": crestronCompliances,
       "crestronGroups": crestronGroups,
       "crestronRootAllObjects": crestronRootAllObjects,
       "crestronCommon": crestronCommon,
       "crestronControl": crestronControl,
       "crestronTouch": crestronTouch}
)
