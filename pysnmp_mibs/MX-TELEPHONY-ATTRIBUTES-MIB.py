# SNMP MIB module (MX-TELEPHONY-ATTRIBUTES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-TELEPHONY-ATTRIBUTES-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:25 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

telephonyAttributesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 70)
)
if mibBuilder.loadTexts:
    telephonyAttributesMIB.setRevisions(
        ("2010-10-05 00:00",
         "2006-11-27 00:00",
         "2005-07-04 00:00",
         "2003-05-16 00:00",
         "2003-04-30 00:00",
         "2003-03-18 00:00",
         "2003-03-03 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TelephonyAttributesMIBObjects_ObjectIdentity = ObjectIdentity
telephonyAttributesMIBObjects = _TelephonyAttributesMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 70, 1)
)
_TelephonyAttributesIfFeaturesTable_Object = MibTable
telephonyAttributesIfFeaturesTable = _TelephonyAttributesIfFeaturesTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 70, 1, 10)
)
if mibBuilder.loadTexts:
    telephonyAttributesIfFeaturesTable.setStatus("current")
_TelephonyAttributesIfFeaturesEntry_Object = MibTableRow
telephonyAttributesIfFeaturesEntry = _TelephonyAttributesIfFeaturesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 70, 1, 10, 1)
)
telephonyAttributesIfFeaturesEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    telephonyAttributesIfFeaturesEntry.setStatus("current")


class _TelephonyAttributesAutomaticCallEnable_Type(MxEnableState):
    """Custom type telephonyAttributesAutomaticCallEnable based on MxEnableState"""
    defaultValue = 0


_TelephonyAttributesAutomaticCallEnable_Type.__name__ = "MxEnableState"
_TelephonyAttributesAutomaticCallEnable_Object = MibTableColumn
telephonyAttributesAutomaticCallEnable = _TelephonyAttributesAutomaticCallEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 70, 1, 10, 1, 5),
    _TelephonyAttributesAutomaticCallEnable_Type()
)
telephonyAttributesAutomaticCallEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyAttributesAutomaticCallEnable.setStatus("current")


class _TelephonyAttributesAutomaticCallTargetAddress_Type(OctetString):
    """Custom type telephonyAttributesAutomaticCallTargetAddress based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TelephonyAttributesAutomaticCallTargetAddress_Type.__name__ = "OctetString"
_TelephonyAttributesAutomaticCallTargetAddress_Object = MibTableColumn
telephonyAttributesAutomaticCallTargetAddress = _TelephonyAttributesAutomaticCallTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 70, 1, 10, 1, 10),
    _TelephonyAttributesAutomaticCallTargetAddress_Type()
)
telephonyAttributesAutomaticCallTargetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyAttributesAutomaticCallTargetAddress.setStatus("current")


class _TelephonyAttributesCallDirectionRestriction_Type(Integer32):
    """Custom type telephonyAttributesCallDirectionRestriction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noRestriction", 0),
          ("scnToIpOnly", 1),
          ("ipToScnOnly", 2))
    )


_TelephonyAttributesCallDirectionRestriction_Type.__name__ = "Integer32"
_TelephonyAttributesCallDirectionRestriction_Object = MibTableColumn
telephonyAttributesCallDirectionRestriction = _TelephonyAttributesCallDirectionRestriction_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 70, 1, 10, 1, 15),
    _TelephonyAttributesCallDirectionRestriction_Type()
)
telephonyAttributesCallDirectionRestriction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyAttributesCallDirectionRestriction.setStatus("current")


class _TelephonyAttributesHookFlashProcessing_Type(Integer32):
    """Custom type telephonyAttributesHookFlashProcessing based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("processLocally", 0),
          ("transmitUsingSignalingProtocol", 1),
          ("outOfBandUsingRtp", 2))
    )


_TelephonyAttributesHookFlashProcessing_Type.__name__ = "Integer32"
_TelephonyAttributesHookFlashProcessing_Object = MibTableColumn
telephonyAttributesHookFlashProcessing = _TelephonyAttributesHookFlashProcessing_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 70, 1, 10, 1, 20),
    _TelephonyAttributesHookFlashProcessing_Type()
)
telephonyAttributesHookFlashProcessing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyAttributesHookFlashProcessing.setStatus("current")


class _TelephonyAttributesDelayedHotLineEnable_Type(MxEnableState):
    """Custom type telephonyAttributesDelayedHotLineEnable based on MxEnableState"""
    defaultValue = 0


_TelephonyAttributesDelayedHotLineEnable_Type.__name__ = "MxEnableState"
_TelephonyAttributesDelayedHotLineEnable_Object = MibTableColumn
telephonyAttributesDelayedHotLineEnable = _TelephonyAttributesDelayedHotLineEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 70, 1, 10, 1, 70),
    _TelephonyAttributesDelayedHotLineEnable_Type()
)
telephonyAttributesDelayedHotLineEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyAttributesDelayedHotLineEnable.setStatus("current")


class _TelephonyAttributesDelayedHotLineExtension_Type(MxEnableState):
    """Custom type telephonyAttributesDelayedHotLineExtension based on MxEnableState"""
    defaultValue = 0


_TelephonyAttributesDelayedHotLineExtension_Type.__name__ = "MxEnableState"
_TelephonyAttributesDelayedHotLineExtension_Object = MibTableColumn
telephonyAttributesDelayedHotLineExtension = _TelephonyAttributesDelayedHotLineExtension_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 70, 1, 10, 1, 120),
    _TelephonyAttributesDelayedHotLineExtension_Type()
)
telephonyAttributesDelayedHotLineExtension.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyAttributesDelayedHotLineExtension.setStatus("current")


class _TelephonyAttributesDelayedHotLineTargetAddress_Type(OctetString):
    """Custom type telephonyAttributesDelayedHotLineTargetAddress based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TelephonyAttributesDelayedHotLineTargetAddress_Type.__name__ = "OctetString"
_TelephonyAttributesDelayedHotLineTargetAddress_Object = MibTableColumn
telephonyAttributesDelayedHotLineTargetAddress = _TelephonyAttributesDelayedHotLineTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 70, 1, 10, 1, 170),
    _TelephonyAttributesDelayedHotLineTargetAddress_Type()
)
telephonyAttributesDelayedHotLineTargetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyAttributesDelayedHotLineTargetAddress.setStatus("current")


class _TelephonyAttributesAutomaticRejection_Type(Unsigned32):
    """Custom type telephonyAttributesAutomaticRejection based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_TelephonyAttributesAutomaticRejection_Type.__name__ = "Unsigned32"
_TelephonyAttributesAutomaticRejection_Object = MibScalar
telephonyAttributesAutomaticRejection = _TelephonyAttributesAutomaticRejection_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 70, 1, 10, 1, 220),
    _TelephonyAttributesAutomaticRejection_Type()
)
telephonyAttributesAutomaticRejection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyAttributesAutomaticRejection.setStatus("current")
_TelephonyAttributesIpAddressCallCustomization_ObjectIdentity = ObjectIdentity
telephonyAttributesIpAddressCallCustomization = _TelephonyAttributesIpAddressCallCustomization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 70, 1, 30)
)


class _TelephonyAttributesIpAddressCallEnable_Type(MxEnableState):
    """Custom type telephonyAttributesIpAddressCallEnable based on MxEnableState"""
    defaultValue = 0


_TelephonyAttributesIpAddressCallEnable_Type.__name__ = "MxEnableState"
_TelephonyAttributesIpAddressCallEnable_Object = MibScalar
telephonyAttributesIpAddressCallEnable = _TelephonyAttributesIpAddressCallEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 70, 1, 30, 5),
    _TelephonyAttributesIpAddressCallEnable_Type()
)
telephonyAttributesIpAddressCallEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyAttributesIpAddressCallEnable.setStatus("current")
_TelephonyAttributesConformance_ObjectIdentity = ObjectIdentity
telephonyAttributesConformance = _TelephonyAttributesConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 70, 2)
)
_TelephonyAttributesCompliances_ObjectIdentity = ObjectIdentity
telephonyAttributesCompliances = _TelephonyAttributesCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 70, 2, 1)
)
_TelephonyAttributesGroups_ObjectIdentity = ObjectIdentity
telephonyAttributesGroups = _TelephonyAttributesGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 70, 2, 5)
)

# Managed Objects groups

telephonyAttributesFeaturesTableVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 70, 2, 5, 10)
)
telephonyAttributesFeaturesTableVer1.setObjects(
      *(("MX-TELEPHONY-ATTRIBUTES-MIB", "telephonyAttributesAutomaticCallEnable"),
        ("MX-TELEPHONY-ATTRIBUTES-MIB", "telephonyAttributesAutomaticCallTargetAddress"),
        ("MX-TELEPHONY-ATTRIBUTES-MIB", "telephonyAttributesCallDirectionRestriction"),
        ("MX-TELEPHONY-ATTRIBUTES-MIB", "telephonyAttributesHookFlashProcessing"),
        ("MX-TELEPHONY-ATTRIBUTES-MIB", "telephonyAttributesDelayedHotLineEnable"),
        ("MX-TELEPHONY-ATTRIBUTES-MIB", "telephonyAttributesDelayedHotLineExtension"),
        ("MX-TELEPHONY-ATTRIBUTES-MIB", "telephonyAttributesDelayedHotLineTargetAddress"),
        ("MX-TELEPHONY-ATTRIBUTES-MIB", "telephonyAttributesAutomaticRejection"))
)
if mibBuilder.loadTexts:
    telephonyAttributesFeaturesTableVer1.setStatus("current")

telephonyAttributesIpAddressCallVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 70, 2, 5, 15)
)
telephonyAttributesIpAddressCallVer1.setObjects(
    ("MX-TELEPHONY-ATTRIBUTES-MIB", "telephonyAttributesIpAddressCallEnable")
)
if mibBuilder.loadTexts:
    telephonyAttributesIpAddressCallVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

telephonyAttributesComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 15, 70, 2, 1, 1)
)
telephonyAttributesComplVer1.setObjects(
      *(("MX-TELEPHONY-ATTRIBUTES-MIB", "telephonyAttributesFeaturesTableVer1"),
        ("MX-TELEPHONY-ATTRIBUTES-MIB", "telephonyAttributesIpAddressCallVer1"))
)
if mibBuilder.loadTexts:
    telephonyAttributesComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-TELEPHONY-ATTRIBUTES-MIB",
    **{"telephonyAttributesMIB": telephonyAttributesMIB,
       "telephonyAttributesMIBObjects": telephonyAttributesMIBObjects,
       "telephonyAttributesIfFeaturesTable": telephonyAttributesIfFeaturesTable,
       "telephonyAttributesIfFeaturesEntry": telephonyAttributesIfFeaturesEntry,
       "telephonyAttributesAutomaticCallEnable": telephonyAttributesAutomaticCallEnable,
       "telephonyAttributesAutomaticCallTargetAddress": telephonyAttributesAutomaticCallTargetAddress,
       "telephonyAttributesCallDirectionRestriction": telephonyAttributesCallDirectionRestriction,
       "telephonyAttributesHookFlashProcessing": telephonyAttributesHookFlashProcessing,
       "telephonyAttributesDelayedHotLineEnable": telephonyAttributesDelayedHotLineEnable,
       "telephonyAttributesDelayedHotLineExtension": telephonyAttributesDelayedHotLineExtension,
       "telephonyAttributesDelayedHotLineTargetAddress": telephonyAttributesDelayedHotLineTargetAddress,
       "telephonyAttributesAutomaticRejection": telephonyAttributesAutomaticRejection,
       "telephonyAttributesIpAddressCallCustomization": telephonyAttributesIpAddressCallCustomization,
       "telephonyAttributesIpAddressCallEnable": telephonyAttributesIpAddressCallEnable,
       "telephonyAttributesConformance": telephonyAttributesConformance,
       "telephonyAttributesCompliances": telephonyAttributesCompliances,
       "telephonyAttributesComplVer1": telephonyAttributesComplVer1,
       "telephonyAttributesGroups": telephonyAttributesGroups,
       "telephonyAttributesFeaturesTableVer1": telephonyAttributesFeaturesTableVer1,
       "telephonyAttributesIpAddressCallVer1": telephonyAttributesIpAddressCallVer1}
)
