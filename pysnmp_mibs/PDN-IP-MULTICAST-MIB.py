# SNMP MIB module (PDN-IP-MULTICAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/paradyne/PDN-IP-MULTICAST-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:01:05 2025
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

(pdn_common,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-common")

(SwitchState,) = mibBuilder.importSymbols(
    "PDN-TC",
    "SwitchState")

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

pdnIpMcastMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48)
)
if mibBuilder.loadTexts:
    pdnIpMcastMIB.setRevisions(
        ("2003-05-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PdnIpMcastNotifications_ObjectIdentity = ObjectIdentity
pdnIpMcastNotifications = _PdnIpMcastNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 0)
)
_PdnIpMcastObjects_ObjectIdentity = ObjectIdentity
pdnIpMcastObjects = _PdnIpMcastObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 1)
)
_PdnIgmpProxy_ObjectIdentity = ObjectIdentity
pdnIgmpProxy = _PdnIgmpProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 1, 1)
)


class _PdnIgmpProxyEnableDisable_Type(SwitchState):
    """Custom type pdnIgmpProxyEnableDisable based on SwitchState"""
    defaultValue = 2


_PdnIgmpProxyEnableDisable_Type.__name__ = "SwitchState"
_PdnIgmpProxyEnableDisable_Object = MibScalar
pdnIgmpProxyEnableDisable = _PdnIgmpProxyEnableDisable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 1, 1, 1),
    _PdnIgmpProxyEnableDisable_Type()
)
pdnIgmpProxyEnableDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnIgmpProxyEnableDisable.setStatus("current")


class _PdnIgmpProxyReportSummaryEnableDisable_Type(SwitchState):
    """Custom type pdnIgmpProxyReportSummaryEnableDisable based on SwitchState"""
    defaultValue = 2


_PdnIgmpProxyReportSummaryEnableDisable_Type.__name__ = "SwitchState"
_PdnIgmpProxyReportSummaryEnableDisable_Object = MibScalar
pdnIgmpProxyReportSummaryEnableDisable = _PdnIgmpProxyReportSummaryEnableDisable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 1, 1, 2),
    _PdnIgmpProxyReportSummaryEnableDisable_Type()
)
pdnIgmpProxyReportSummaryEnableDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnIgmpProxyReportSummaryEnableDisable.setStatus("current")
_PdnIpMcastStats_ObjectIdentity = ObjectIdentity
pdnIpMcastStats = _PdnIpMcastStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 1, 2)
)
_PdnIpMcastAFNs_ObjectIdentity = ObjectIdentity
pdnIpMcastAFNs = _PdnIpMcastAFNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 2)
)
_PdnIpMcastConformance_ObjectIdentity = ObjectIdentity
pdnIpMcastConformance = _PdnIpMcastConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 3)
)
_PdnIpMcastCompliances_ObjectIdentity = ObjectIdentity
pdnIpMcastCompliances = _PdnIpMcastCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 3, 1)
)
_PdnIpMcastGroups_ObjectIdentity = ObjectIdentity
pdnIpMcastGroups = _PdnIpMcastGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 3, 2)
)
_PdnIpMcaseObjGroups_ObjectIdentity = ObjectIdentity
pdnIpMcaseObjGroups = _PdnIpMcaseObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 3, 2, 1)
)
_PdnIpMcastAfnGroups_ObjectIdentity = ObjectIdentity
pdnIpMcastAfnGroups = _PdnIpMcastAfnGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 3, 2, 2)
)
_PdnIpMcaseNtfyGroups_ObjectIdentity = ObjectIdentity
pdnIpMcaseNtfyGroups = _PdnIpMcaseNtfyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 3, 2, 3)
)

# Managed Objects groups

pdnIgmpProxyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 3, 2, 1, 1)
)
pdnIgmpProxyGroup.setObjects(
      *(("PDN-IP-MULTICAST-MIB", "pdnIgmpProxyEnableDisable"),
        ("PDN-IP-MULTICAST-MIB", "pdnIgmpProxyReportSummaryEnableDisable"))
)
if mibBuilder.loadTexts:
    pdnIgmpProxyGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pdnIpMcastMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 3, 1, 1)
)
pdnIpMcastMIBCompliance.setObjects(
    ("PDN-IP-MULTICAST-MIB", "pdnIgmpProxyGroup")
)
if mibBuilder.loadTexts:
    pdnIpMcastMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-IP-MULTICAST-MIB",
    **{"pdnIpMcastMIB": pdnIpMcastMIB,
       "pdnIpMcastNotifications": pdnIpMcastNotifications,
       "pdnIpMcastObjects": pdnIpMcastObjects,
       "pdnIgmpProxy": pdnIgmpProxy,
       "pdnIgmpProxyEnableDisable": pdnIgmpProxyEnableDisable,
       "pdnIgmpProxyReportSummaryEnableDisable": pdnIgmpProxyReportSummaryEnableDisable,
       "pdnIpMcastStats": pdnIpMcastStats,
       "pdnIpMcastAFNs": pdnIpMcastAFNs,
       "pdnIpMcastConformance": pdnIpMcastConformance,
       "pdnIpMcastCompliances": pdnIpMcastCompliances,
       "pdnIpMcastMIBCompliance": pdnIpMcastMIBCompliance,
       "pdnIpMcastGroups": pdnIpMcastGroups,
       "pdnIpMcaseObjGroups": pdnIpMcaseObjGroups,
       "pdnIgmpProxyGroup": pdnIgmpProxyGroup,
       "pdnIpMcastAfnGroups": pdnIpMcastAfnGroups,
       "pdnIpMcaseNtfyGroups": pdnIpMcaseNtfyGroups}
)
