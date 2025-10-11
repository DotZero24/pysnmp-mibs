# SNMP MIB module (MX-NCS-COMPATIBILITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-NCS-COMPATIBILITY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:28 2025
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

ncsCompatibilityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 15)
)
if mibBuilder.loadTexts:
    ncsCompatibilityMIB.setRevisions(
        ("2008-12-03 00:00",
         "1902-08-28 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NcsCompatibilityMIBObjects_ObjectIdentity = ObjectIdentity
ncsCompatibilityMIBObjects = _NcsCompatibilityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 15, 1)
)


class _NcsCompatibilityRtpPayloadType18EncodingName_Type(Integer32):
    """Custom type ncsCompatibilityRtpPayloadType18EncodingName based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("g729", 0),
          ("g729A", 1))
    )


_NcsCompatibilityRtpPayloadType18EncodingName_Type.__name__ = "Integer32"
_NcsCompatibilityRtpPayloadType18EncodingName_Object = MibScalar
ncsCompatibilityRtpPayloadType18EncodingName = _NcsCompatibilityRtpPayloadType18EncodingName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 15, 1, 5),
    _NcsCompatibilityRtpPayloadType18EncodingName_Type()
)
ncsCompatibilityRtpPayloadType18EncodingName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncsCompatibilityRtpPayloadType18EncodingName.setStatus("current")


class _NcsCompatibilityVersion_Type(Integer32):
    """Custom type ncsCompatibilityVersion based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mgcp01Ncs10", 0),
          ("fakeMgcp10Ncs10", 1))
    )


_NcsCompatibilityVersion_Type.__name__ = "Integer32"
_NcsCompatibilityVersion_Object = MibScalar
ncsCompatibilityVersion = _NcsCompatibilityVersion_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 15, 1, 100),
    _NcsCompatibilityVersion_Type()
)
ncsCompatibilityVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncsCompatibilityVersion.setStatus("current")
_NcsCompatibilityConformance_ObjectIdentity = ObjectIdentity
ncsCompatibilityConformance = _NcsCompatibilityConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 15, 2)
)
_NcsCompatibilityCompliances_ObjectIdentity = ObjectIdentity
ncsCompatibilityCompliances = _NcsCompatibilityCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 15, 2, 1)
)
_NcsCompatibilityGroups_ObjectIdentity = ObjectIdentity
ncsCompatibilityGroups = _NcsCompatibilityGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 15, 2, 2)
)

# Managed Objects groups

ncsCompatibilityBasicGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 99, 15, 2, 2, 10)
)
ncsCompatibilityBasicGroupVer1.setObjects(
      *(("MX-NCS-COMPATIBILITY-MIB", "ncsCompatibilityRtpPayloadType18EncodingName"),
        ("MX-NCS-COMPATIBILITY-MIB", "ncsCompatibilityVersion"))
)
if mibBuilder.loadTexts:
    ncsCompatibilityBasicGroupVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ncsCompatibilityComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 99, 15, 2, 1, 10)
)
ncsCompatibilityComplVer1.setObjects(
    ("MX-NCS-COMPATIBILITY-MIB", "ncsCompatibilityBasicGroupVer1")
)
if mibBuilder.loadTexts:
    ncsCompatibilityComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-NCS-COMPATIBILITY-MIB",
    **{"ncsCompatibilityMIB": ncsCompatibilityMIB,
       "ncsCompatibilityMIBObjects": ncsCompatibilityMIBObjects,
       "ncsCompatibilityRtpPayloadType18EncodingName": ncsCompatibilityRtpPayloadType18EncodingName,
       "ncsCompatibilityVersion": ncsCompatibilityVersion,
       "ncsCompatibilityConformance": ncsCompatibilityConformance,
       "ncsCompatibilityCompliances": ncsCompatibilityCompliances,
       "ncsCompatibilityComplVer1": ncsCompatibilityComplVer1,
       "ncsCompatibilityGroups": ncsCompatibilityGroups,
       "ncsCompatibilityBasicGroupVer1": ncsCompatibilityBasicGroupVer1}
)
