# SNMP MIB module (PDN-MPD-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/paradyne/PDN-MPD-EXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:00:49 2025
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

(pdnMpdExt,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdnMpdExt")

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

pdnMpdExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 44, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PdnMpdExtSecurityMode(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("none", 0),
          ("snmpv1NoAuthNoPriv", 1),
          ("snmpv2cNoAuthNoPriv", 2),
          ("snmpv3NoAuthNoPriv", 3),
          ("snmpv3AuthNoPriv", 4),
          ("snmpv3AuthPriv", 5))
    )


# MIB Managed Objects in the order of their OIDs

_PdnMpdExtMIBObjects_ObjectIdentity = ObjectIdentity
pdnMpdExtMIBObjects = _PdnMpdExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 44, 1, 1)
)
_PdnMpdExtSecurityModeConfig_Type = PdnMpdExtSecurityMode
_PdnMpdExtSecurityModeConfig_Object = MibScalar
pdnMpdExtSecurityModeConfig = _PdnMpdExtSecurityModeConfig_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 44, 1, 1, 1),
    _PdnMpdExtSecurityModeConfig_Type()
)
pdnMpdExtSecurityModeConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnMpdExtSecurityModeConfig.setStatus("current")
_PdnMpdExtMIBConformance_ObjectIdentity = ObjectIdentity
pdnMpdExtMIBConformance = _PdnMpdExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 44, 1, 2)
)
_PdnMpdExtCompliances_ObjectIdentity = ObjectIdentity
pdnMpdExtCompliances = _PdnMpdExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 44, 1, 2, 1)
)
_PdnMpdExtGroups_ObjectIdentity = ObjectIdentity
pdnMpdExtGroups = _PdnMpdExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 44, 1, 2, 2)
)

# Managed Objects groups

pdnMpdExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 44, 1, 2, 2, 1)
)
pdnMpdExtGroup.setObjects(
    ("PDN-MPD-EXT-MIB", "pdnMpdExtSecurityModeConfig")
)
if mibBuilder.loadTexts:
    pdnMpdExtGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pdnMpdExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 44, 1, 2, 1, 1)
)
pdnMpdExtCompliance.setObjects(
    ("PDN-MPD-EXT-MIB", "pdnMpdExtGroup")
)
if mibBuilder.loadTexts:
    pdnMpdExtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-MPD-EXT-MIB",
    **{"PdnMpdExtSecurityMode": PdnMpdExtSecurityMode,
       "pdnMpdExtMIB": pdnMpdExtMIB,
       "pdnMpdExtMIBObjects": pdnMpdExtMIBObjects,
       "pdnMpdExtSecurityModeConfig": pdnMpdExtSecurityModeConfig,
       "pdnMpdExtMIBConformance": pdnMpdExtMIBConformance,
       "pdnMpdExtCompliances": pdnMpdExtCompliances,
       "pdnMpdExtCompliance": pdnMpdExtCompliance,
       "pdnMpdExtGroups": pdnMpdExtGroups,
       "pdnMpdExtGroup": pdnMpdExtGroup}
)
