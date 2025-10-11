# SNMP MIB module (MX-SIP-DEBUG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-SIP-DEBUG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:38 2025
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

(mediatrixExperimental,) = mibBuilder.importSymbols(
    "MX-SMI",
    "mediatrixExperimental")

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

sipDebugMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 23)
)
if mibBuilder.loadTexts:
    sipDebugMIB.setRevisions(
        ("1903-11-13 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SipDebugMIBObjects_ObjectIdentity = ObjectIdentity
sipDebugMIBObjects = _SipDebugMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 23, 1)
)


class _SipDebugContextSnapshotTime_Type(Unsigned32):
    """Custom type sipDebugContextSnapshotTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10080),
    )


_SipDebugContextSnapshotTime_Type.__name__ = "Unsigned32"
_SipDebugContextSnapshotTime_Object = MibScalar
sipDebugContextSnapshotTime = _SipDebugContextSnapshotTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 23, 1, 5),
    _SipDebugContextSnapshotTime_Type()
)
sipDebugContextSnapshotTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipDebugContextSnapshotTime.setStatus("current")
_SipDebugConformance_ObjectIdentity = ObjectIdentity
sipDebugConformance = _SipDebugConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 23, 2)
)
_SipDebugCompliances_ObjectIdentity = ObjectIdentity
sipDebugCompliances = _SipDebugCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 23, 2, 1)
)
_SipDebugGroups_ObjectIdentity = ObjectIdentity
sipDebugGroups = _SipDebugGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 23, 2, 2)
)

# Managed Objects groups

sipDebugGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 99, 23, 2, 2, 5)
)
sipDebugGroupVer1.setObjects(
    ("MX-SIP-DEBUG-MIB", "sipDebugContextSnapshotTime")
)
if mibBuilder.loadTexts:
    sipDebugGroupVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

sipDebugBasicComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 99, 23, 2, 1, 1)
)
sipDebugBasicComplVer1.setObjects(
    ("MX-SIP-DEBUG-MIB", "sipDebugGroupVer1")
)
if mibBuilder.loadTexts:
    sipDebugBasicComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-SIP-DEBUG-MIB",
    **{"sipDebugMIB": sipDebugMIB,
       "sipDebugMIBObjects": sipDebugMIBObjects,
       "sipDebugContextSnapshotTime": sipDebugContextSnapshotTime,
       "sipDebugConformance": sipDebugConformance,
       "sipDebugCompliances": sipDebugCompliances,
       "sipDebugBasicComplVer1": sipDebugBasicComplVer1,
       "sipDebugGroups": sipDebugGroups,
       "sipDebugGroupVer1": sipDebugGroupVer1}
)
