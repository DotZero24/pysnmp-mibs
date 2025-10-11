# SNMP MIB module (MX-TELEPHONY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-TELEPHONY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:54 2025
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

(mediatrixConfig,) = mibBuilder.importSymbols(
    "MX-SMI",
    "mediatrixConfig")

(MxEnableState,) = mibBuilder.importSymbols(
    "MX-TC",
    "MxEnableState")

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

telephonyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 25)
)
if mibBuilder.loadTexts:
    telephonyMIB.setRevisions(
        ("2012-07-03 00:00",
         "2012-06-08 00:00",
         "2010-01-18 00:00",
         "2007-11-13 00:00",
         "2007-08-06 00:00",
         "2007-04-18 00:00",
         "2007-03-21 00:00",
         "2007-01-03 00:00",
         "2006-04-28 00:00",
         "2005-09-28 00:00",
         "2004-11-12 00:00",
         "2004-08-03 00:00",
         "2004-08-02 00:00",
         "2004-07-21 00:00",
         "2004-07-14 00:00",
         "2004-06-15 00:00",
         "2003-10-20 00:00",
         "2003-08-15 00:00",
         "2003-07-03 00:00",
         "2003-06-06 00:00",
         "2003-05-01 00:00",
         "2003-01-13 00:00",
         "2003-01-14 00:00",
         "2002-11-25 00:00",
         "2002-10-09 00:00",
         "2002-03-29 00:00",
         "2001-11-05 00:00",
         "2001-08-29 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TelephonyMIBObjects_ObjectIdentity = ObjectIdentity
telephonyMIBObjects = _TelephonyMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 25, 1)
)


class _TelephonyIpSignalingProtocolSelection_Type(Integer32):
    """Custom type telephonyIpSignalingProtocolSelection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              99)
        )
    )
    namedValues = NamedValues(
        *(("mgcp", 1),
          ("sip", 2),
          ("ncs", 3),
          ("h323", 4),
          ("proprietary", 99))
    )


_TelephonyIpSignalingProtocolSelection_Type.__name__ = "Integer32"
_TelephonyIpSignalingProtocolSelection_Object = MibScalar
telephonyIpSignalingProtocolSelection = _TelephonyIpSignalingProtocolSelection_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 25, 1, 3),
    _TelephonyIpSignalingProtocolSelection_Type()
)
telephonyIpSignalingProtocolSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyIpSignalingProtocolSelection.setStatus("current")


class _TelephonyIpSignalingProtocolProprietary_Type(OctetString):
    """Custom type telephonyIpSignalingProtocolProprietary based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TelephonyIpSignalingProtocolProprietary_Type.__name__ = "OctetString"
_TelephonyIpSignalingProtocolProprietary_Object = MibScalar
telephonyIpSignalingProtocolProprietary = _TelephonyIpSignalingProtocolProprietary_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 25, 1, 4),
    _TelephonyIpSignalingProtocolProprietary_Type()
)
telephonyIpSignalingProtocolProprietary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telephonyIpSignalingProtocolProprietary.setStatus("current")


class _TelephonyCountrySelection_Type(Integer32):
    """Custom type telephonyCountrySelection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              100,
              101,
              102,
              110,
              111,
              120,
              130)
        )
    )
    namedValues = NamedValues(
        *(("northAmerica1", 1),
          ("northAmerica2", 2),
          ("austria", 3),
          ("france", 4),
          ("germany1", 5),
          ("germany2", 6),
          ("uk", 7),
          ("italy", 8),
          ("spain", 9),
          ("switzerland", 10),
          ("sweden", 11),
          ("australia1", 12),
          ("japan", 13),
          ("israel", 14),
          ("thailand", 15),
          ("indonesia", 16),
          ("australia2", 17),
          ("china", 18),
          ("hongKong", 19),
          ("malaysia", 20),
          ("russia", 21),
          ("netherlands", 22),
          ("brazil", 23),
          ("uae", 24),
          ("mexico", 25),
          ("denmark", 26),
          ("australia3", 27),
          ("newZealand", 28),
          ("austria2", 29),
          ("germany3", 30),
          ("czechRepublic", 31),
          ("chile1", 32),
          ("chile2", 33),
          ("uae2", 34),
          ("southAfrica", 35),
          ("uk-bellcore", 100),
          ("uk-cca", 101),
          ("uk-etsi-fsk", 102),
          ("france-etsi-fsk", 110),
          ("france-etsi-dtmf", 111),
          ("austria-etsi-fsk", 120),
          ("austria2-etsi-fsk", 130))
    )


_TelephonyCountrySelection_Type.__name__ = "Integer32"
_TelephonyCountrySelection_Object = MibScalar
telephonyCountrySelection = _TelephonyCountrySelection_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 25, 1, 6),
    _TelephonyCountrySelection_Type()
)
telephonyCountrySelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyCountrySelection.setStatus("current")
_TelephonySpecificCountrySelectionTable_Object = MibTable
telephonySpecificCountrySelectionTable = _TelephonySpecificCountrySelectionTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 25, 1, 10)
)
if mibBuilder.loadTexts:
    telephonySpecificCountrySelectionTable.setStatus("current")
_TelephonySpecificCountrySelectionEntry_Object = MibTableRow
telephonySpecificCountrySelectionEntry = _TelephonySpecificCountrySelectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 25, 1, 10, 1)
)
telephonySpecificCountrySelectionEntry.setIndexNames(
    (0, "MX-TELEPHONY-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    telephonySpecificCountrySelectionEntry.setStatus("current")


class _TelephonySpecificCountrySelectionEnableConfig_Type(MxEnableState):
    """Custom type telephonySpecificCountrySelectionEnableConfig based on MxEnableState"""
    defaultValue = 0


_TelephonySpecificCountrySelectionEnableConfig_Type.__name__ = "MxEnableState"
_TelephonySpecificCountrySelectionEnableConfig_Object = MibTableColumn
telephonySpecificCountrySelectionEnableConfig = _TelephonySpecificCountrySelectionEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 25, 1, 10, 1, 10),
    _TelephonySpecificCountrySelectionEnableConfig_Type()
)
telephonySpecificCountrySelectionEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonySpecificCountrySelectionEnableConfig.setStatus("current")


class _TelephonySpecificCountrySelectionCountry_Type(Integer32):
    """Custom type telephonySpecificCountrySelectionCountry based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              100,
              101,
              102,
              110,
              111,
              120,
              130)
        )
    )
    namedValues = NamedValues(
        *(("northAmerica1", 1),
          ("northAmerica2", 2),
          ("austria", 3),
          ("france", 4),
          ("germany1", 5),
          ("germany2", 6),
          ("uk", 7),
          ("italy", 8),
          ("spain", 9),
          ("switzerland", 10),
          ("sweden", 11),
          ("australia1", 12),
          ("japan", 13),
          ("israel", 14),
          ("thailand", 15),
          ("indonesia", 16),
          ("australia2", 17),
          ("china", 18),
          ("hongKong", 19),
          ("malaysia", 20),
          ("russia", 21),
          ("netherlands", 22),
          ("brazil", 23),
          ("uae", 24),
          ("mexico", 25),
          ("denmark", 26),
          ("australia3", 27),
          ("newZealand", 28),
          ("austria2", 29),
          ("germany3", 30),
          ("czechRepublic", 31),
          ("chile1", 32),
          ("chile2", 33),
          ("uae2", 34),
          ("southAfrica", 35),
          ("uk-bellcore", 100),
          ("uk-cca", 101),
          ("uk-etsi-fsk", 102),
          ("france-etsi-fsk", 110),
          ("france-etsi-dtmf", 111),
          ("austria-etsi-fsk", 120),
          ("austria2-etsi-fsk", 130))
    )


_TelephonySpecificCountrySelectionCountry_Type.__name__ = "Integer32"
_TelephonySpecificCountrySelectionCountry_Object = MibTableColumn
telephonySpecificCountrySelectionCountry = _TelephonySpecificCountrySelectionCountry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 25, 1, 10, 1, 20),
    _TelephonySpecificCountrySelectionCountry_Type()
)
telephonySpecificCountrySelectionCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonySpecificCountrySelectionCountry.setStatus("current")
_CountryCustomizationToneGroup_ObjectIdentity = ObjectIdentity
countryCustomizationToneGroup = _CountryCustomizationToneGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 25, 1, 500)
)
_CountryCustomizationToneTable_Object = MibTable
countryCustomizationToneTable = _CountryCustomizationToneTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 25, 1, 500, 200)
)
if mibBuilder.loadTexts:
    countryCustomizationToneTable.setStatus("current")
_CountryCustomizationToneEntry_Object = MibTableRow
countryCustomizationToneEntry = _CountryCustomizationToneEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 25, 1, 500, 200, 1)
)
countryCustomizationToneEntry.setIndexNames(
    (0, "MX-TELEPHONY-MIB", "countryCustomizationToneTone"),
)
if mibBuilder.loadTexts:
    countryCustomizationToneEntry.setStatus("current")


class _CountryCustomizationToneTone_Type(Integer32):
    """Custom type countryCustomizationToneTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400,
              600,
              700,
              800,
              900,
              1000,
              1100,
              1200,
              1300)
        )
    )
    namedValues = NamedValues(
        *(("busy", 100),
          ("confirmation", 200),
          ("congestion", 300),
          ("dial", 400),
          ("intercept", 600),
          ("messageWaiting", 700),
          ("preemption", 800),
          ("reorder", 900),
          ("ringback", 1000),
          ("roh", 1100),
          ("sit", 1200),
          ("stutter", 1300))
    )


_CountryCustomizationToneTone_Type.__name__ = "Integer32"
_CountryCustomizationToneTone_Object = MibTableColumn
countryCustomizationToneTone = _CountryCustomizationToneTone_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 25, 1, 500, 200, 1, 100),
    _CountryCustomizationToneTone_Type()
)
countryCustomizationToneTone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    countryCustomizationToneTone.setStatus("current")


class _CountryCustomizationToneOverride_Type(MxEnableState):
    """Custom type countryCustomizationToneOverride based on MxEnableState"""
    defaultValue = 0


_CountryCustomizationToneOverride_Type.__name__ = "MxEnableState"
_CountryCustomizationToneOverride_Object = MibTableColumn
countryCustomizationToneOverride = _CountryCustomizationToneOverride_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 25, 1, 500, 200, 1, 200),
    _CountryCustomizationToneOverride_Type()
)
countryCustomizationToneOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    countryCustomizationToneOverride.setStatus("current")


class _CountryCustomizationTonePattern_Type(OctetString):
    """Custom type countryCustomizationTonePattern based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_CountryCustomizationTonePattern_Type.__name__ = "OctetString"
_CountryCustomizationTonePattern_Object = MibTableColumn
countryCustomizationTonePattern = _CountryCustomizationTonePattern_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 25, 1, 500, 200, 1, 300),
    _CountryCustomizationTonePattern_Type()
)
countryCustomizationTonePattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    countryCustomizationTonePattern.setStatus("current")
_CountryCustomizationTonePerPortTable_Object = MibTable
countryCustomizationTonePerPortTable = _CountryCustomizationTonePerPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 25, 1, 500, 300)
)
if mibBuilder.loadTexts:
    countryCustomizationTonePerPortTable.setStatus("current")
_CountryCustomizationTonePerPortEntry_Object = MibTableRow
countryCustomizationTonePerPortEntry = _CountryCustomizationTonePerPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 25, 1, 500, 300, 1)
)
countryCustomizationTonePerPortEntry.setIndexNames(
    (0, "MX-TELEPHONY-MIB", "ifIndex"),
    (0, "MX-TELEPHONY-MIB", "countryCustomizationTonePerPortTone"),
)
if mibBuilder.loadTexts:
    countryCustomizationTonePerPortEntry.setStatus("current")


class _CountryCustomizationTonePerPortTone_Type(Integer32):
    """Custom type countryCustomizationTonePerPortTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400,
              600,
              700,
              800,
              900,
              1000,
              1100,
              1200,
              1300)
        )
    )
    namedValues = NamedValues(
        *(("busy", 100),
          ("confirmation", 200),
          ("congestion", 300),
          ("dial", 400),
          ("intercept", 600),
          ("messageWaiting", 700),
          ("preemption", 800),
          ("reorder", 900),
          ("ringback", 1000),
          ("roh", 1100),
          ("sit", 1200),
          ("stutter", 1300))
    )


_CountryCustomizationTonePerPortTone_Type.__name__ = "Integer32"
_CountryCustomizationTonePerPortTone_Object = MibTableColumn
countryCustomizationTonePerPortTone = _CountryCustomizationTonePerPortTone_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 25, 1, 500, 300, 1, 100),
    _CountryCustomizationTonePerPortTone_Type()
)
countryCustomizationTonePerPortTone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    countryCustomizationTonePerPortTone.setStatus("current")


class _CountryCustomizationTonePerPortOverride_Type(MxEnableState):
    """Custom type countryCustomizationTonePerPortOverride based on MxEnableState"""
    defaultValue = 0


_CountryCustomizationTonePerPortOverride_Type.__name__ = "MxEnableState"
_CountryCustomizationTonePerPortOverride_Object = MibTableColumn
countryCustomizationTonePerPortOverride = _CountryCustomizationTonePerPortOverride_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 25, 1, 500, 300, 1, 200),
    _CountryCustomizationTonePerPortOverride_Type()
)
countryCustomizationTonePerPortOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    countryCustomizationTonePerPortOverride.setStatus("current")


class _CountryCustomizationTonePerPortPattern_Type(OctetString):
    """Custom type countryCustomizationTonePerPortPattern based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_CountryCustomizationTonePerPortPattern_Type.__name__ = "OctetString"
_CountryCustomizationTonePerPortPattern_Object = MibTableColumn
countryCustomizationTonePerPortPattern = _CountryCustomizationTonePerPortPattern_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 25, 1, 500, 300, 1, 300),
    _CountryCustomizationTonePerPortPattern_Type()
)
countryCustomizationTonePerPortPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    countryCustomizationTonePerPortPattern.setStatus("current")
_TelephonyConformance_ObjectIdentity = ObjectIdentity
telephonyConformance = _TelephonyConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 25, 2)
)
_TelephonyCompliances_ObjectIdentity = ObjectIdentity
telephonyCompliances = _TelephonyCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 25, 2, 1)
)
_TelephonyGroups_ObjectIdentity = ObjectIdentity
telephonyGroups = _TelephonyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 25, 2, 2)
)

# Managed Objects groups

telephonyGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 25, 2, 2, 1)
)
telephonyGroupVer1.setObjects(
      *(("MX-TELEPHONY-MIB", "telephonyIpSignalingProtocolSelection"),
        ("MX-TELEPHONY-MIB", "telephonyIpSignalingProtocolProprietary"),
        ("MX-TELEPHONY-MIB", "telephonyCountrySelection"),
        ("MX-TELEPHONY-MIB", "telephonySpecificCountrySelectionTable"))
)
if mibBuilder.loadTexts:
    telephonyGroupVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

telephonyComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 15, 25, 2, 1, 1)
)
telephonyComplVer1.setObjects(
    ("MX-TELEPHONY-MIB", "telephonyGroupVer1")
)
if mibBuilder.loadTexts:
    telephonyComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-TELEPHONY-MIB",
    **{"telephonyMIB": telephonyMIB,
       "telephonyMIBObjects": telephonyMIBObjects,
       "telephonyIpSignalingProtocolSelection": telephonyIpSignalingProtocolSelection,
       "telephonyIpSignalingProtocolProprietary": telephonyIpSignalingProtocolProprietary,
       "telephonyCountrySelection": telephonyCountrySelection,
       "telephonySpecificCountrySelectionTable": telephonySpecificCountrySelectionTable,
       "telephonySpecificCountrySelectionEntry": telephonySpecificCountrySelectionEntry,
       "telephonySpecificCountrySelectionEnableConfig": telephonySpecificCountrySelectionEnableConfig,
       "telephonySpecificCountrySelectionCountry": telephonySpecificCountrySelectionCountry,
       "countryCustomizationToneGroup": countryCustomizationToneGroup,
       "countryCustomizationToneTable": countryCustomizationToneTable,
       "countryCustomizationToneEntry": countryCustomizationToneEntry,
       "countryCustomizationToneTone": countryCustomizationToneTone,
       "countryCustomizationToneOverride": countryCustomizationToneOverride,
       "countryCustomizationTonePattern": countryCustomizationTonePattern,
       "countryCustomizationTonePerPortTable": countryCustomizationTonePerPortTable,
       "countryCustomizationTonePerPortEntry": countryCustomizationTonePerPortEntry,
       "countryCustomizationTonePerPortTone": countryCustomizationTonePerPortTone,
       "countryCustomizationTonePerPortOverride": countryCustomizationTonePerPortOverride,
       "countryCustomizationTonePerPortPattern": countryCustomizationTonePerPortPattern,
       "telephonyConformance": telephonyConformance,
       "telephonyCompliances": telephonyCompliances,
       "telephonyComplVer1": telephonyComplVer1,
       "telephonyGroups": telephonyGroups,
       "telephonyGroupVer1": telephonyGroupVer1}
)
