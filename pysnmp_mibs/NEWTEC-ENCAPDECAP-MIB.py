# SNMP MIB module (NEWTEC-ENCAPDECAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-ENCAPDECAP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:04:18 2025
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

ntcEncapDecap = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2220)
)
if mibBuilder.loadTexts:
    ntcEncapDecap.setRevisions(
        ("2014-02-03 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcEncapDecapObjects_ObjectIdentity = ObjectIdentity
ntcEncapDecapObjects = _NtcEncapDecapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2220, 1)
)
if mibBuilder.loadTexts:
    ntcEncapDecapObjects.setStatus("current")


class _NtcEncapDecapForwardingMode_Type(Integer32):
    """Custom type ntcEncapDecapForwardingMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("l2", 0),
          ("l3", 1))
    )


_NtcEncapDecapForwardingMode_Type.__name__ = "Integer32"
_NtcEncapDecapForwardingMode_Object = MibScalar
ntcEncapDecapForwardingMode = _NtcEncapDecapForwardingMode_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2220, 1, 1),
    _NtcEncapDecapForwardingMode_Type()
)
ntcEncapDecapForwardingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcEncapDecapForwardingMode.setStatus("current")
_NtcEncapDecapConformance_ObjectIdentity = ObjectIdentity
ntcEncapDecapConformance = _NtcEncapDecapConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2220, 2)
)
if mibBuilder.loadTexts:
    ntcEncapDecapConformance.setStatus("current")
_NtcEncapDecapConfCompliance_ObjectIdentity = ObjectIdentity
ntcEncapDecapConfCompliance = _NtcEncapDecapConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2220, 2, 1)
)
if mibBuilder.loadTexts:
    ntcEncapDecapConfCompliance.setStatus("current")
_NtcEncapDecapConfGroup_ObjectIdentity = ObjectIdentity
ntcEncapDecapConfGroup = _NtcEncapDecapConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2220, 2, 2)
)
if mibBuilder.loadTexts:
    ntcEncapDecapConfGroup.setStatus("current")

# Managed Objects groups

ntcEncapDecapConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2220, 2, 2, 1)
)
ntcEncapDecapConfGrpV1Standard.setObjects(
    ("NEWTEC-ENCAPDECAP-MIB", "ntcEncapDecapForwardingMode")
)
if mibBuilder.loadTexts:
    ntcEncapDecapConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcEncapDecapConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2220, 2, 1, 1)
)
ntcEncapDecapConfCompV1Standard.setObjects(
    ("NEWTEC-ENCAPDECAP-MIB", "ntcEncapDecapConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcEncapDecapConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-ENCAPDECAP-MIB",
    **{"ntcEncapDecap": ntcEncapDecap,
       "ntcEncapDecapObjects": ntcEncapDecapObjects,
       "ntcEncapDecapForwardingMode": ntcEncapDecapForwardingMode,
       "ntcEncapDecapConformance": ntcEncapDecapConformance,
       "ntcEncapDecapConfCompliance": ntcEncapDecapConfCompliance,
       "ntcEncapDecapConfCompV1Standard": ntcEncapDecapConfCompV1Standard,
       "ntcEncapDecapConfGroup": ntcEncapDecapConfGroup,
       "ntcEncapDecapConfGrpV1Standard": ntcEncapDecapConfGrpV1Standard}
)
