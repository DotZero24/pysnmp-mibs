# SNMP MIB module (NEWTEC-TERMINAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-TERMINAL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:04:13 2025
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

(ntcFunction,) = mibBuilder.importSymbols(
    "NEWTEC-MAIN-MIB",
    "ntcFunction")

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

ntcTerminal = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2900)
)
if mibBuilder.loadTexts:
    ntcTerminal.setRevisions(
        ("2013-01-08 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcTermObjects_ObjectIdentity = ObjectIdentity
ntcTermObjects = _NtcTermObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2900, 1)
)
if mibBuilder.loadTexts:
    ntcTermObjects.setStatus("current")


class _NtcTermId_Type(Unsigned32):
    """Custom type ntcTermId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65277),
    )


_NtcTermId_Type.__name__ = "Unsigned32"
_NtcTermId_Object = MibScalar
ntcTermId = _NtcTermId_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2900, 1, 1),
    _NtcTermId_Type()
)
ntcTermId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTermId.setStatus("current")
_NtcTermConformance_ObjectIdentity = ObjectIdentity
ntcTermConformance = _NtcTermConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2900, 2)
)
if mibBuilder.loadTexts:
    ntcTermConformance.setStatus("current")
_NtcTermConfCompliance_ObjectIdentity = ObjectIdentity
ntcTermConfCompliance = _NtcTermConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2900, 2, 1)
)
if mibBuilder.loadTexts:
    ntcTermConfCompliance.setStatus("current")
_NtcTermConfGroup_ObjectIdentity = ObjectIdentity
ntcTermConfGroup = _NtcTermConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2900, 2, 2)
)
if mibBuilder.loadTexts:
    ntcTermConfGroup.setStatus("current")

# Managed Objects groups

ntcTermConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2900, 2, 2, 1)
)
ntcTermConfGrpV1Standard.setObjects(
    ("NEWTEC-TERMINAL-MIB", "ntcTermId")
)
if mibBuilder.loadTexts:
    ntcTermConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcTermConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2900, 2, 1, 1)
)
ntcTermConfCompV1Standard.setObjects(
    ("NEWTEC-TERMINAL-MIB", "ntcTermConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcTermConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-TERMINAL-MIB",
    **{"ntcTerminal": ntcTerminal,
       "ntcTermObjects": ntcTermObjects,
       "ntcTermId": ntcTermId,
       "ntcTermConformance": ntcTermConformance,
       "ntcTermConfCompliance": ntcTermConfCompliance,
       "ntcTermConfCompV1Standard": ntcTermConfCompV1Standard,
       "ntcTermConfGroup": ntcTermConfGroup,
       "ntcTermConfGrpV1Standard": ntcTermConfGrpV1Standard}
)
