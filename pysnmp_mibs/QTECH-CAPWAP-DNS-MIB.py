# SNMP MIB module (QTECH-CAPWAP-DNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-CAPWAP-DNS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:58:33 2025
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

(qtechIfIndex,) = mibBuilder.importSymbols(
    "QTECH-INTERFACE-MIB",
    "qtechIfIndex")

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

qtechCapwapDnsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 88)
)
if mibBuilder.loadTexts:
    qtechCapwapDnsMIB.setRevisions(
        ("2010-07-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechCapwapDnsMIBObjects_ObjectIdentity = ObjectIdentity
qtechCapwapDnsMIBObjects = _QtechCapwapDnsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 88, 0)
)
_QtechCapwapDnsGlobalConfig_ObjectIdentity = ObjectIdentity
qtechCapwapDnsGlobalConfig = _QtechCapwapDnsGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 88, 0, 1)
)
_QtechLDnsFirstServer_Type = IpAddress
_QtechLDnsFirstServer_Object = MibScalar
qtechLDnsFirstServer = _QtechLDnsFirstServer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 88, 0, 1, 1),
    _QtechLDnsFirstServer_Type()
)
qtechLDnsFirstServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechLDnsFirstServer.setStatus("current")
_QtechLDnsSecondServer_Type = IpAddress
_QtechLDnsSecondServer_Object = MibScalar
qtechLDnsSecondServer = _QtechLDnsSecondServer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 88, 0, 1, 2),
    _QtechLDnsSecondServer_Type()
)
qtechLDnsSecondServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechLDnsSecondServer.setStatus("current")
_QtechCapwapDnsMIBConformance_ObjectIdentity = ObjectIdentity
qtechCapwapDnsMIBConformance = _QtechCapwapDnsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 88, 2)
)
_QtechCapwapDnsMIBCompliances_ObjectIdentity = ObjectIdentity
qtechCapwapDnsMIBCompliances = _QtechCapwapDnsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 88, 2, 1)
)
_QtechCapwapDnsMIBGroups_ObjectIdentity = ObjectIdentity
qtechCapwapDnsMIBGroups = _QtechCapwapDnsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 88, 2, 2)
)

# Managed Objects groups

qtechCapwapDnsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 88, 2, 2, 1)
)
qtechCapwapDnsMIBGroup.setObjects(
      *(("QTECH-CAPWAP-DNS-MIB", "qtechLDnsFirstServer"),
        ("QTECH-CAPWAP-DNS-MIB", "qtechLDnsSecondServer"))
)
if mibBuilder.loadTexts:
    qtechCapwapDnsMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechCapwapDnsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 88, 2, 1, 1)
)
qtechCapwapDnsMIBCompliance.setObjects(
    ("QTECH-CAPWAP-DNS-MIB", "qtechCapwapDnsMIBGroup")
)
if mibBuilder.loadTexts:
    qtechCapwapDnsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-CAPWAP-DNS-MIB",
    **{"qtechCapwapDnsMIB": qtechCapwapDnsMIB,
       "qtechCapwapDnsMIBObjects": qtechCapwapDnsMIBObjects,
       "qtechCapwapDnsGlobalConfig": qtechCapwapDnsGlobalConfig,
       "qtechLDnsFirstServer": qtechLDnsFirstServer,
       "qtechLDnsSecondServer": qtechLDnsSecondServer,
       "qtechCapwapDnsMIBConformance": qtechCapwapDnsMIBConformance,
       "qtechCapwapDnsMIBCompliances": qtechCapwapDnsMIBCompliances,
       "qtechCapwapDnsMIBCompliance": qtechCapwapDnsMIBCompliance,
       "qtechCapwapDnsMIBGroups": qtechCapwapDnsMIBGroups,
       "qtechCapwapDnsMIBGroup": qtechCapwapDnsMIBGroup}
)
