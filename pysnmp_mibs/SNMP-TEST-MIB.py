# SNMP MIB module (SNMP-TEST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/radlan/SNMP-TEST-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:11:11 2025
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

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

(rlSnmpTestSimulatedVariables,) = mibBuilder.importSymbols(
    "RADLAN-rndApplications",
    "rlSnmpTestSimulatedVariables")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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


# Types definitions


# TEXTUAL-CONVENTIONS



class KeyBits(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("firstKey", 0),
          ("secondKey", 1),
          ("thirdKey", 2),
          ("fourthKey", 3),
          ("fifthKey", 4))
    )


class FieldBits(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("firstField", 0),
          ("secondField", 1),
          ("thirdField", 2),
          ("fourthField", 3),
          ("fifthField", 4))
    )


# MIB Managed Objects in the order of their OIDs

_RlSnmpTestMibVersion_Type = Integer32
_RlSnmpTestMibVersion_Object = MibScalar
rlSnmpTestMibVersion = _RlSnmpTestMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 9, 1),
    _RlSnmpTestMibVersion_Type()
)
rlSnmpTestMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSnmpTestMibVersion.setStatus("current")
_RlSetsTestTable_Object = MibTable
rlSetsTestTable = _RlSetsTestTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 9, 2)
)
if mibBuilder.loadTexts:
    rlSetsTestTable.setStatus("current")
_RlSetsTestEntry_Object = MibTableRow
rlSetsTestEntry = _RlSetsTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 9, 2, 1)
)
rlSetsTestEntry.setIndexNames(
    (0, "SNMP-TEST-MIB", "rlSetsEntryBitsKey"),
    (0, "SNMP-TEST-MIB", "rlSetsEntryPortListKey"),
)
if mibBuilder.loadTexts:
    rlSetsTestEntry.setStatus("current")


class _RlSetsEntryBitsKey_Type(KeyBits):
    """Custom type rlSetsEntryBitsKey based on KeyBits"""
    subtypeSpec = KeyBits.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("firstKey", 0),
          ("secondKey", 1),
          ("thirdKey", 2),
          ("fifthKey", 4))
    )


_RlSetsEntryBitsKey_Type.__name__ = "KeyBits"
_RlSetsEntryBitsKey_Object = MibTableColumn
rlSetsEntryBitsKey = _RlSetsEntryBitsKey_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 9, 2, 1, 1),
    _RlSetsEntryBitsKey_Type()
)
rlSetsEntryBitsKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSetsEntryBitsKey.setStatus("current")
_RlSetsEntryPortListKey_Type = PortList
_RlSetsEntryPortListKey_Object = MibTableColumn
rlSetsEntryPortListKey = _RlSetsEntryPortListKey_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 9, 2, 1, 2),
    _RlSetsEntryPortListKey_Type()
)
rlSetsEntryPortListKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSetsEntryPortListKey.setStatus("current")


class _RlSetsEntryBitsField_Type(FieldBits):
    """Custom type rlSetsEntryBitsField based on FieldBits"""
    subtypeSpec = FieldBits.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("firstField", 0),
          ("secondField", 1),
          ("thirdField", 2),
          ("fifthField", 4))
    )


_RlSetsEntryBitsField_Type.__name__ = "FieldBits"
_RlSetsEntryBitsField_Object = MibTableColumn
rlSetsEntryBitsField = _RlSetsEntryBitsField_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 9, 2, 1, 3),
    _RlSetsEntryBitsField_Type()
)
rlSetsEntryBitsField.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlSetsEntryBitsField.setStatus("current")
_RlSetsEntryPortListField_Type = PortList
_RlSetsEntryPortListField_Object = MibTableColumn
rlSetsEntryPortListField = _RlSetsEntryPortListField_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 9, 2, 1, 4),
    _RlSetsEntryPortListField_Type()
)
rlSetsEntryPortListField.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlSetsEntryPortListField.setStatus("current")
_RlSetsEntryCounter64Field_Type = Counter64
_RlSetsEntryCounter64Field_Object = MibTableColumn
rlSetsEntryCounter64Field = _RlSetsEntryCounter64Field_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 9, 2, 1, 5),
    _RlSetsEntryCounter64Field_Type()
)
rlSetsEntryCounter64Field.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlSetsEntryCounter64Field.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNMP-TEST-MIB",
    **{"KeyBits": KeyBits,
       "FieldBits": FieldBits,
       "rlSnmpTestMibVersion": rlSnmpTestMibVersion,
       "rlSetsTestTable": rlSetsTestTable,
       "rlSetsTestEntry": rlSetsTestEntry,
       "rlSetsEntryBitsKey": rlSetsEntryBitsKey,
       "rlSetsEntryPortListKey": rlSetsEntryPortListKey,
       "rlSetsEntryBitsField": rlSetsEntryBitsField,
       "rlSetsEntryPortListField": rlSetsEntryPortListField,
       "rlSetsEntryCounter64Field": rlSetsEntryCounter64Field}
)
