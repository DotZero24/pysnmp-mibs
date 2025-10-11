# SNMP MIB module (HPTCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HPTCP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:40:48 2025
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

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

hpicfTcpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79)
)
if mibBuilder.loadTexts:
    hpicfTcpMib.setRevisions(
        ("2010-09-30 15:25",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpTcpObjects_ObjectIdentity = ObjectIdentity
hpTcpObjects = _HpTcpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79, 1)
)
_HpTcpOutRstsWithAck_Type = Counter32
_HpTcpOutRstsWithAck_Object = MibScalar
hpTcpOutRstsWithAck = _HpTcpOutRstsWithAck_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79, 1, 1),
    _HpTcpOutRstsWithAck_Type()
)
hpTcpOutRstsWithAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpTcpOutRstsWithAck.setStatus("current")
_HpTcpConformance_ObjectIdentity = ObjectIdentity
hpTcpConformance = _HpTcpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79, 2)
)
_HpTcpGroups_ObjectIdentity = ObjectIdentity
hpTcpGroups = _HpTcpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79, 2, 1)
)
_HpTcpCompliances_ObjectIdentity = ObjectIdentity
hpTcpCompliances = _HpTcpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79, 2, 2)
)

# Managed Objects groups

hpTcpBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79, 2, 1, 1)
)
hpTcpBaseGroup.setObjects(
    ("HPTCP-MIB", "hpTcpOutRstsWithAck")
)
if mibBuilder.loadTexts:
    hpTcpBaseGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpTcpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79, 2, 2, 1)
)
hpTcpCompliance.setObjects(
    ("HPTCP-MIB", "hpTcpBaseGroup")
)
if mibBuilder.loadTexts:
    hpTcpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPTCP-MIB",
    **{"hpicfTcpMib": hpicfTcpMib,
       "hpTcpObjects": hpTcpObjects,
       "hpTcpOutRstsWithAck": hpTcpOutRstsWithAck,
       "hpTcpConformance": hpTcpConformance,
       "hpTcpGroups": hpTcpGroups,
       "hpTcpBaseGroup": hpTcpBaseGroup,
       "hpTcpCompliances": hpTcpCompliances,
       "hpTcpCompliance": hpTcpCompliance}
)
