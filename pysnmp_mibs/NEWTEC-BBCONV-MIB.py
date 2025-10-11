# SNMP MIB module (NEWTEC-BBCONV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-BBCONV-MIB
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

ntcBBandConverter = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 10500)
)
if mibBuilder.loadTexts:
    ntcBBandConverter.setRevisions(
        ("2017-07-10 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcBbcObjects_ObjectIdentity = ObjectIdentity
ntcBbcObjects = _NtcBbcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 10500, 1)
)
if mibBuilder.loadTexts:
    ntcBbcObjects.setStatus("current")
_NtcBbcConf_ObjectIdentity = ObjectIdentity
ntcBbcConf = _NtcBbcConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 10500, 1, 1)
)
if mibBuilder.loadTexts:
    ntcBbcConf.setStatus("current")


class _NtcBbcConfEnable_Type(Integer32):
    """Custom type ntcBbcConfEnable based on Integer32"""
    defaultValue = 0

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


_NtcBbcConfEnable_Type.__name__ = "Integer32"
_NtcBbcConfEnable_Object = MibScalar
ntcBbcConfEnable = _NtcBbcConfEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 10500, 1, 1, 1),
    _NtcBbcConfEnable_Type()
)
ntcBbcConfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcBbcConfEnable.setStatus("current")


class _NtcBbcConfSelection_Type(Integer32):
    """Custom type ntcBbcConfSelection based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("abandRHCP99W", 0),
          ("abandLHCP99W", 1),
          ("bbandRHCP99W", 2),
          ("bbandLHCP99W", 3),
          ("abandRHCP103W", 4),
          ("abandLHCP103W", 5),
          ("bbandRHCP103W", 6),
          ("bbandLHCP103W", 7))
    )


_NtcBbcConfSelection_Type.__name__ = "Integer32"
_NtcBbcConfSelection_Object = MibScalar
ntcBbcConfSelection = _NtcBbcConfSelection_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 10500, 1, 1, 2),
    _NtcBbcConfSelection_Type()
)
ntcBbcConfSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcBbcConfSelection.setStatus("current")
_NtcBbcConformance_ObjectIdentity = ObjectIdentity
ntcBbcConformance = _NtcBbcConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 10500, 2)
)
if mibBuilder.loadTexts:
    ntcBbcConformance.setStatus("current")
_NtcBbcConfCompliance_ObjectIdentity = ObjectIdentity
ntcBbcConfCompliance = _NtcBbcConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 10500, 2, 1)
)
if mibBuilder.loadTexts:
    ntcBbcConfCompliance.setStatus("current")
_NtcBbcConfGroup_ObjectIdentity = ObjectIdentity
ntcBbcConfGroup = _NtcBbcConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 10500, 2, 2)
)
if mibBuilder.loadTexts:
    ntcBbcConfGroup.setStatus("current")

# Managed Objects groups

ntcBbcConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 10500, 2, 2, 1)
)
ntcBbcConfGrpV1Standard.setObjects(
      *(("NEWTEC-BBCONV-MIB", "ntcBbcConfEnable"),
        ("NEWTEC-BBCONV-MIB", "ntcBbcConfSelection"))
)
if mibBuilder.loadTexts:
    ntcBbcConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcBbcConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 10500, 2, 1, 1)
)
ntcBbcConfCompV1Standard.setObjects(
    ("NEWTEC-BBCONV-MIB", "ntcBbcConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcBbcConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-BBCONV-MIB",
    **{"ntcBBandConverter": ntcBBandConverter,
       "ntcBbcObjects": ntcBbcObjects,
       "ntcBbcConf": ntcBbcConf,
       "ntcBbcConfEnable": ntcBbcConfEnable,
       "ntcBbcConfSelection": ntcBbcConfSelection,
       "ntcBbcConformance": ntcBbcConformance,
       "ntcBbcConfCompliance": ntcBbcConfCompliance,
       "ntcBbcConfCompV1Standard": ntcBbcConfCompV1Standard,
       "ntcBbcConfGroup": ntcBbcConfGroup,
       "ntcBbcConfGrpV1Standard": ntcBbcConfGrpV1Standard}
)
