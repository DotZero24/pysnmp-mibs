# SNMP MIB module (PKTC-DECT-SIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rfc/PKTC-DECT-SIP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:20:33 2025
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

(pktcApplicationMibs,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "pktcApplicationMibs")

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


# MODULE-IDENTITY

pktcDectSipMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 5)
)
if mibBuilder.loadTexts:
    pktcDectSipMib.setRevisions(
        ("2009-02-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PktcDectSipNotifications_ObjectIdentity = ObjectIdentity
pktcDectSipNotifications = _PktcDectSipNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 5, 0)
)
_PktcDectSipObjects_ObjectIdentity = ObjectIdentity
pktcDectSipObjects = _PktcDectSipObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 5, 1)
)
_PktcDectSipCFVDis_ObjectIdentity = ObjectIdentity
pktcDectSipCFVDis = _PktcDectSipCFVDis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 5, 1, 1)
)


class _PktcDectSipCFVDisNewFwdCalls_Type(SnmpAdminString):
    """Custom type pktcDectSipCFVDisNewFwdCalls based on SnmpAdminString"""
    defaultValue = OctetString("")


_PktcDectSipCFVDisNewFwdCalls_Type.__name__ = "SnmpAdminString"
_PktcDectSipCFVDisNewFwdCalls_Object = MibScalar
pktcDectSipCFVDisNewFwdCalls = _PktcDectSipCFVDisNewFwdCalls_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 5, 1, 1, 1),
    _PktcDectSipCFVDisNewFwdCalls_Type()
)
pktcDectSipCFVDisNewFwdCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcDectSipCFVDisNewFwdCalls.setStatus("current")


class _PktcDectSipCFVDisActStat_Type(SnmpAdminString):
    """Custom type pktcDectSipCFVDisActStat based on SnmpAdminString"""
    defaultValue = OctetString("")


_PktcDectSipCFVDisActStat_Type.__name__ = "SnmpAdminString"
_PktcDectSipCFVDisActStat_Object = MibScalar
pktcDectSipCFVDisActStat = _PktcDectSipCFVDisActStat_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 5, 1, 1, 2),
    _PktcDectSipCFVDisActStat_Type()
)
pktcDectSipCFVDisActStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcDectSipCFVDisActStat.setStatus("current")
_PktcDectSipSCFDis_ObjectIdentity = ObjectIdentity
pktcDectSipSCFDis = _PktcDectSipSCFDis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 5, 1, 2)
)


class _PktcDectSipSCFDisNewFwdCalls_Type(SnmpAdminString):
    """Custom type pktcDectSipSCFDisNewFwdCalls based on SnmpAdminString"""
    defaultValue = OctetString("")


_PktcDectSipSCFDisNewFwdCalls_Type.__name__ = "SnmpAdminString"
_PktcDectSipSCFDisNewFwdCalls_Object = MibScalar
pktcDectSipSCFDisNewFwdCalls = _PktcDectSipSCFDisNewFwdCalls_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 5, 1, 2, 1),
    _PktcDectSipSCFDisNewFwdCalls_Type()
)
pktcDectSipSCFDisNewFwdCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcDectSipSCFDisNewFwdCalls.setStatus("current")
_PktcDectSipDNDDis_ObjectIdentity = ObjectIdentity
pktcDectSipDNDDis = _PktcDectSipDNDDis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 5, 1, 3)
)


class _PktcDectSipDNDDisActStat_Type(SnmpAdminString):
    """Custom type pktcDectSipDNDDisActStat based on SnmpAdminString"""
    defaultValue = OctetString("")


_PktcDectSipDNDDisActStat_Type.__name__ = "SnmpAdminString"
_PktcDectSipDNDDisActStat_Object = MibScalar
pktcDectSipDNDDisActStat = _PktcDectSipDNDDisActStat_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 5, 1, 3, 1),
    _PktcDectSipDNDDisActStat_Type()
)
pktcDectSipDNDDisActStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcDectSipDNDDisActStat.setStatus("current")
_PktcDectSipMibConformance_ObjectIdentity = ObjectIdentity
pktcDectSipMibConformance = _PktcDectSipMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 5, 2)
)
_PktcDectSipMibCompliances_ObjectIdentity = ObjectIdentity
pktcDectSipMibCompliances = _PktcDectSipMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 5, 2, 1)
)
_PktcDectSipMibGroups_ObjectIdentity = ObjectIdentity
pktcDectSipMibGroups = _PktcDectSipMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 5, 2, 2)
)

# Managed Objects groups

pktcDectSipGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 5, 2, 2, 1)
)
pktcDectSipGroup.setObjects(
      *(("PKTC-DECT-SIP-MIB", "pktcDectSipCFVDisNewFwdCalls"),
        ("PKTC-DECT-SIP-MIB", "pktcDectSipCFVDisActStat"),
        ("PKTC-DECT-SIP-MIB", "pktcDectSipSCFDisNewFwdCalls"),
        ("PKTC-DECT-SIP-MIB", "pktcDectSipDNDDisActStat"))
)
if mibBuilder.loadTexts:
    pktcDectSipGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pktcDectSipCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 5, 2, 1, 1)
)
pktcDectSipCompliance.setObjects(
    ("PKTC-DECT-SIP-MIB", "pktcDectSipGroup")
)
if mibBuilder.loadTexts:
    pktcDectSipCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PKTC-DECT-SIP-MIB",
    **{"pktcDectSipMib": pktcDectSipMib,
       "pktcDectSipNotifications": pktcDectSipNotifications,
       "pktcDectSipObjects": pktcDectSipObjects,
       "pktcDectSipCFVDis": pktcDectSipCFVDis,
       "pktcDectSipCFVDisNewFwdCalls": pktcDectSipCFVDisNewFwdCalls,
       "pktcDectSipCFVDisActStat": pktcDectSipCFVDisActStat,
       "pktcDectSipSCFDis": pktcDectSipSCFDis,
       "pktcDectSipSCFDisNewFwdCalls": pktcDectSipSCFDisNewFwdCalls,
       "pktcDectSipDNDDis": pktcDectSipDNDDis,
       "pktcDectSipDNDDisActStat": pktcDectSipDNDDisActStat,
       "pktcDectSipMibConformance": pktcDectSipMibConformance,
       "pktcDectSipMibCompliances": pktcDectSipMibCompliances,
       "pktcDectSipCompliance": pktcDectSipCompliance,
       "pktcDectSipMibGroups": pktcDectSipMibGroups,
       "pktcDectSipGroup": pktcDectSipGroup}
)
