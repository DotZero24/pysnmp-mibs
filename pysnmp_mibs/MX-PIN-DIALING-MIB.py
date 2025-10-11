# SNMP MIB module (MX-PIN-DIALING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-PIN-DIALING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:56 2025
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

(mediatrixExperimental,) = mibBuilder.importSymbols(
    "MX-SMI",
    "mediatrixExperimental")

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

pinDialingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 90)
)
if mibBuilder.loadTexts:
    pinDialingMIB.setRevisions(
        ("2006-03-06 00:00",
         "2004-08-19 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PinDialingMIBObjects_ObjectIdentity = ObjectIdentity
pinDialingMIBObjects = _PinDialingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 90, 1)
)
_PinDialingIfTable_Object = MibTable
pinDialingIfTable = _PinDialingIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 90, 1, 10)
)
if mibBuilder.loadTexts:
    pinDialingIfTable.setStatus("current")
_PinDialingIfEntry_Object = MibTableRow
pinDialingIfEntry = _PinDialingIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 90, 1, 10, 1)
)
pinDialingIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pinDialingIfEntry.setStatus("current")


class _PinDialingEnable_Type(MxEnableState):
    """Custom type pinDialingEnable based on MxEnableState"""
    defaultValue = 0


_PinDialingEnable_Type.__name__ = "MxEnableState"
_PinDialingEnable_Object = MibTableColumn
pinDialingEnable = _PinDialingEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 90, 1, 10, 1, 10),
    _PinDialingEnable_Type()
)
pinDialingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pinDialingEnable.setStatus("current")


class _PinDialingPin_Type(OctetString):
    """Custom type pinDialingPin based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PinDialingPin_Type.__name__ = "OctetString"
_PinDialingPin_Object = MibTableColumn
pinDialingPin = _PinDialingPin_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 90, 1, 10, 1, 20),
    _PinDialingPin_Type()
)
pinDialingPin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pinDialingPin.setStatus("current")


class _PinDialingDelay_Type(Unsigned32):
    """Custom type pinDialingDelay based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300000),
    )


_PinDialingDelay_Type.__name__ = "Unsigned32"
_PinDialingDelay_Object = MibTableColumn
pinDialingDelay = _PinDialingDelay_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 90, 1, 10, 1, 30),
    _PinDialingDelay_Type()
)
pinDialingDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pinDialingDelay.setStatus("current")
_PinDialingConformance_ObjectIdentity = ObjectIdentity
pinDialingConformance = _PinDialingConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 90, 2)
)
_PinDialingCompliances_ObjectIdentity = ObjectIdentity
pinDialingCompliances = _PinDialingCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 90, 2, 1)
)
_PinDialingGroups_ObjectIdentity = ObjectIdentity
pinDialingGroups = _PinDialingGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 90, 2, 2)
)

# Managed Objects groups

pinDialingGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 99, 90, 2, 2, 1)
)
pinDialingGroupVer1.setObjects(
      *(("MX-PIN-DIALING-MIB", "pinDialingEnable"),
        ("MX-PIN-DIALING-MIB", "pinDialingPin"),
        ("MX-PIN-DIALING-MIB", "pinDialingDelay"))
)
if mibBuilder.loadTexts:
    pinDialingGroupVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pinDialingBasicComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 99, 90, 2, 1, 1)
)
pinDialingBasicComplVer1.setObjects(
    ("MX-PIN-DIALING-MIB", "pinDialingGroupVer1")
)
if mibBuilder.loadTexts:
    pinDialingBasicComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-PIN-DIALING-MIB",
    **{"pinDialingMIB": pinDialingMIB,
       "pinDialingMIBObjects": pinDialingMIBObjects,
       "pinDialingIfTable": pinDialingIfTable,
       "pinDialingIfEntry": pinDialingIfEntry,
       "pinDialingEnable": pinDialingEnable,
       "pinDialingPin": pinDialingPin,
       "pinDialingDelay": pinDialingDelay,
       "pinDialingConformance": pinDialingConformance,
       "pinDialingCompliances": pinDialingCompliances,
       "pinDialingBasicComplVer1": pinDialingBasicComplVer1,
       "pinDialingGroups": pinDialingGroups,
       "pinDialingGroupVer1": pinDialingGroupVer1}
)
