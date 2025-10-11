# SNMP MIB module (MX-ANALOG-SCN-GATEWAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-ANALOG-SCN-GATEWAY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:48 2025
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

analogScnGwMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 85)
)
if mibBuilder.loadTexts:
    analogScnGwMIB.setRevisions(
        ("2005-10-27 00:00",
         "2003-08-12 00:00",
         "2003-03-25 00:00",
         "2003-02-25 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AnalogScnGwMIBObjects_ObjectIdentity = ObjectIdentity
analogScnGwMIBObjects = _AnalogScnGwMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 85, 1)
)
_AnalogScnGwIfDialingTable_Object = MibTable
analogScnGwIfDialingTable = _AnalogScnGwIfDialingTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 85, 1, 10)
)
if mibBuilder.loadTexts:
    analogScnGwIfDialingTable.setStatus("current")
_AnalogScnGwIfDialingEntry_Object = MibTableRow
analogScnGwIfDialingEntry = _AnalogScnGwIfDialingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 85, 1, 10, 5)
)
analogScnGwIfDialingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    analogScnGwIfDialingEntry.setStatus("current")


class _AnalogScnGwDialPrefix_Type(OctetString):
    """Custom type analogScnGwDialPrefix based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AnalogScnGwDialPrefix_Type.__name__ = "OctetString"
_AnalogScnGwDialPrefix_Object = MibTableColumn
analogScnGwDialPrefix = _AnalogScnGwDialPrefix_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 85, 1, 10, 5, 10),
    _AnalogScnGwDialPrefix_Type()
)
analogScnGwDialPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogScnGwDialPrefix.setStatus("current")


class _AnalogScnGwPreDialDelay_Type(Unsigned32):
    """Custom type analogScnGwPreDialDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_AnalogScnGwPreDialDelay_Type.__name__ = "Unsigned32"
_AnalogScnGwPreDialDelay_Object = MibTableColumn
analogScnGwPreDialDelay = _AnalogScnGwPreDialDelay_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 85, 1, 10, 5, 15),
    _AnalogScnGwPreDialDelay_Type()
)
analogScnGwPreDialDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogScnGwPreDialDelay.setStatus("current")


class _AnalogScnGwInterDigitDialDelay_Type(Unsigned32):
    """Custom type analogScnGwInterDigitDialDelay based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 600),
    )


_AnalogScnGwInterDigitDialDelay_Type.__name__ = "Unsigned32"
_AnalogScnGwInterDigitDialDelay_Object = MibTableColumn
analogScnGwInterDigitDialDelay = _AnalogScnGwInterDigitDialDelay_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 85, 1, 10, 5, 20),
    _AnalogScnGwInterDigitDialDelay_Type()
)
analogScnGwInterDigitDialDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogScnGwInterDigitDialDelay.setStatus("current")


class _AnalogScnGwDtmfDuration_Type(Unsigned32):
    """Custom type analogScnGwDtmfDuration based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 600),
    )


_AnalogScnGwDtmfDuration_Type.__name__ = "Unsigned32"
_AnalogScnGwDtmfDuration_Object = MibTableColumn
analogScnGwDtmfDuration = _AnalogScnGwDtmfDuration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 85, 1, 10, 5, 25),
    _AnalogScnGwDtmfDuration_Type()
)
analogScnGwDtmfDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogScnGwDtmfDuration.setStatus("current")


class _AnalogScnGwDialEnable_Type(MxEnableState):
    """Custom type analogScnGwDialEnable based on MxEnableState"""
    defaultValue = 1


_AnalogScnGwDialEnable_Type.__name__ = "MxEnableState"
_AnalogScnGwDialEnable_Object = MibTableColumn
analogScnGwDialEnable = _AnalogScnGwDialEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 85, 1, 10, 5, 75),
    _AnalogScnGwDialEnable_Type()
)
analogScnGwDialEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogScnGwDialEnable.setStatus("current")
_AnalogScnGwConformance_ObjectIdentity = ObjectIdentity
analogScnGwConformance = _AnalogScnGwConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 85, 5)
)
_AnalogScnGwCompliances_ObjectIdentity = ObjectIdentity
analogScnGwCompliances = _AnalogScnGwCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 85, 5, 1)
)
_AnalogScnGwGroups_ObjectIdentity = ObjectIdentity
analogScnGwGroups = _AnalogScnGwGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 85, 5, 5)
)

# Managed Objects groups

analogScnGwDialingVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 85, 5, 5, 10)
)
analogScnGwDialingVer1.setObjects(
      *(("MX-ANALOG-SCN-GATEWAY-MIB", "analogScnGwDialPrefix"),
        ("MX-ANALOG-SCN-GATEWAY-MIB", "analogScnGwPreDialDelay"),
        ("MX-ANALOG-SCN-GATEWAY-MIB", "analogScnGwInterDigitDialDelay"),
        ("MX-ANALOG-SCN-GATEWAY-MIB", "analogScnGwDtmfDuration"),
        ("MX-ANALOG-SCN-GATEWAY-MIB", "analogScnGwDialEnable"))
)
if mibBuilder.loadTexts:
    analogScnGwDialingVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

analogScnGwComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 15, 85, 5, 1, 1)
)
analogScnGwComplVer1.setObjects(
    ("MX-ANALOG-SCN-GATEWAY-MIB", "analogScnGwDialingVer1")
)
if mibBuilder.loadTexts:
    analogScnGwComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-ANALOG-SCN-GATEWAY-MIB",
    **{"analogScnGwMIB": analogScnGwMIB,
       "analogScnGwMIBObjects": analogScnGwMIBObjects,
       "analogScnGwIfDialingTable": analogScnGwIfDialingTable,
       "analogScnGwIfDialingEntry": analogScnGwIfDialingEntry,
       "analogScnGwDialPrefix": analogScnGwDialPrefix,
       "analogScnGwPreDialDelay": analogScnGwPreDialDelay,
       "analogScnGwInterDigitDialDelay": analogScnGwInterDigitDialDelay,
       "analogScnGwDtmfDuration": analogScnGwDtmfDuration,
       "analogScnGwDialEnable": analogScnGwDialEnable,
       "analogScnGwConformance": analogScnGwConformance,
       "analogScnGwCompliances": analogScnGwCompliances,
       "analogScnGwComplVer1": analogScnGwComplVer1,
       "analogScnGwGroups": analogScnGwGroups,
       "analogScnGwDialingVer1": analogScnGwDialingVer1}
)
