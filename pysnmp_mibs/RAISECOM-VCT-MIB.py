# SNMP MIB module (RAISECOM-VCT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-VCT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:09 2025
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

(raisecomAgent,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "raisecomAgent")

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

raisecomVct = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 14)
)
if mibBuilder.loadTexts:
    raisecomVct.setRevisions(
        ("2006-09-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RaisecomVctPortObjects_ObjectIdentity = ObjectIdentity
raisecomVctPortObjects = _RaisecomVctPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 14, 1)
)
_RaisecomVctPortTable_Object = MibTable
raisecomVctPortTable = _RaisecomVctPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 14, 1, 1)
)
if mibBuilder.loadTexts:
    raisecomVctPortTable.setStatus("current")
_RaisecomVctPortEntry_Object = MibTableRow
raisecomVctPortEntry = _RaisecomVctPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 14, 1, 1, 1)
)
raisecomVctPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    raisecomVctPortEntry.setStatus("current")


class _RaisecomVctPortAttribute_Type(Integer32):
    """Custom type raisecomVctPortAttribute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unSupported", 1),
          ("neverIssued", 2),
          ("issued", 3),
          ("testing", 4))
    )


_RaisecomVctPortAttribute_Type.__name__ = "Integer32"
_RaisecomVctPortAttribute_Object = MibTableColumn
raisecomVctPortAttribute = _RaisecomVctPortAttribute_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 14, 1, 1, 1, 1),
    _RaisecomVctPortAttribute_Type()
)
raisecomVctPortAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomVctPortAttribute.setStatus("current")


class _RaisecomVctPortIssuedTime_Type(OctetString):
    """Custom type raisecomVctPortIssuedTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RaisecomVctPortIssuedTime_Type.__name__ = "OctetString"
_RaisecomVctPortIssuedTime_Object = MibTableColumn
raisecomVctPortIssuedTime = _RaisecomVctPortIssuedTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 14, 1, 1, 1, 2),
    _RaisecomVctPortIssuedTime_Type()
)
raisecomVctPortIssuedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomVctPortIssuedTime.setStatus("current")


class _RaisecomVctPortCableTXStatus_Type(Integer32):
    """Custom type raisecomVctPortCableTXStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("open", 2),
          ("shorted", 3),
          ("error", 4),
          ("invalidation", 5))
    )


_RaisecomVctPortCableTXStatus_Type.__name__ = "Integer32"
_RaisecomVctPortCableTXStatus_Object = MibTableColumn
raisecomVctPortCableTXStatus = _RaisecomVctPortCableTXStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 14, 1, 1, 1, 3),
    _RaisecomVctPortCableTXStatus_Type()
)
raisecomVctPortCableTXStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomVctPortCableTXStatus.setStatus("current")
_RaisecomVctPortCableTXLength_Type = Integer32
_RaisecomVctPortCableTXLength_Object = MibTableColumn
raisecomVctPortCableTXLength = _RaisecomVctPortCableTXLength_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 14, 1, 1, 1, 4),
    _RaisecomVctPortCableTXLength_Type()
)
raisecomVctPortCableTXLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomVctPortCableTXLength.setStatus("current")


class _RaisecomVctPortCableRXStatus_Type(Integer32):
    """Custom type raisecomVctPortCableRXStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("open", 2),
          ("shorted", 3),
          ("error", 4),
          ("invalidation", 5))
    )


_RaisecomVctPortCableRXStatus_Type.__name__ = "Integer32"
_RaisecomVctPortCableRXStatus_Object = MibTableColumn
raisecomVctPortCableRXStatus = _RaisecomVctPortCableRXStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 14, 1, 1, 1, 5),
    _RaisecomVctPortCableRXStatus_Type()
)
raisecomVctPortCableRXStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomVctPortCableRXStatus.setStatus("current")
_RaisecomVctPortCableRXLength_Type = Integer32
_RaisecomVctPortCableRXLength_Object = MibTableColumn
raisecomVctPortCableRXLength = _RaisecomVctPortCableRXLength_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 14, 1, 1, 1, 6),
    _RaisecomVctPortCableRXLength_Type()
)
raisecomVctPortCableRXLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomVctPortCableRXLength.setStatus("current")


class _RaisecomVctPortCableTX2Status_Type(Integer32):
    """Custom type raisecomVctPortCableTX2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("open", 2),
          ("shorted", 3),
          ("error", 4),
          ("invalidation", 5))
    )


_RaisecomVctPortCableTX2Status_Type.__name__ = "Integer32"
_RaisecomVctPortCableTX2Status_Object = MibTableColumn
raisecomVctPortCableTX2Status = _RaisecomVctPortCableTX2Status_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 14, 1, 1, 1, 7),
    _RaisecomVctPortCableTX2Status_Type()
)
raisecomVctPortCableTX2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomVctPortCableTX2Status.setStatus("current")
_RaisecomVctPortCableTX2Length_Type = Integer32
_RaisecomVctPortCableTX2Length_Object = MibTableColumn
raisecomVctPortCableTX2Length = _RaisecomVctPortCableTX2Length_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 14, 1, 1, 1, 8),
    _RaisecomVctPortCableTX2Length_Type()
)
raisecomVctPortCableTX2Length.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomVctPortCableTX2Length.setStatus("current")


class _RaisecomVctPortCableRX2Status_Type(Integer32):
    """Custom type raisecomVctPortCableRX2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("open", 2),
          ("shorted", 3),
          ("error", 4),
          ("invalidation", 5))
    )


_RaisecomVctPortCableRX2Status_Type.__name__ = "Integer32"
_RaisecomVctPortCableRX2Status_Object = MibTableColumn
raisecomVctPortCableRX2Status = _RaisecomVctPortCableRX2Status_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 14, 1, 1, 1, 9),
    _RaisecomVctPortCableRX2Status_Type()
)
raisecomVctPortCableRX2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomVctPortCableRX2Status.setStatus("current")
_RaisecomVctPortCableRX2Length_Type = Integer32
_RaisecomVctPortCableRX2Length_Object = MibTableColumn
raisecomVctPortCableRX2Length = _RaisecomVctPortCableRX2Length_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 14, 1, 1, 1, 10),
    _RaisecomVctPortCableRX2Length_Type()
)
raisecomVctPortCableRX2Length.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomVctPortCableRX2Length.setStatus("current")
_RaisecomVctPortCableLengthFuzz_Type = Integer32
_RaisecomVctPortCableLengthFuzz_Object = MibTableColumn
raisecomVctPortCableLengthFuzz = _RaisecomVctPortCableLengthFuzz_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 14, 1, 1, 1, 11),
    _RaisecomVctPortCableLengthFuzz_Type()
)
raisecomVctPortCableLengthFuzz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomVctPortCableLengthFuzz.setStatus("current")
_RaisecomVctPortStartTest_Type = Integer32
_RaisecomVctPortStartTest_Object = MibScalar
raisecomVctPortStartTest = _RaisecomVctPortStartTest_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 14, 1, 2),
    _RaisecomVctPortStartTest_Type()
)
raisecomVctPortStartTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomVctPortStartTest.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-VCT-MIB",
    **{"raisecomVct": raisecomVct,
       "raisecomVctPortObjects": raisecomVctPortObjects,
       "raisecomVctPortTable": raisecomVctPortTable,
       "raisecomVctPortEntry": raisecomVctPortEntry,
       "raisecomVctPortAttribute": raisecomVctPortAttribute,
       "raisecomVctPortIssuedTime": raisecomVctPortIssuedTime,
       "raisecomVctPortCableTXStatus": raisecomVctPortCableTXStatus,
       "raisecomVctPortCableTXLength": raisecomVctPortCableTXLength,
       "raisecomVctPortCableRXStatus": raisecomVctPortCableRXStatus,
       "raisecomVctPortCableRXLength": raisecomVctPortCableRXLength,
       "raisecomVctPortCableTX2Status": raisecomVctPortCableTX2Status,
       "raisecomVctPortCableTX2Length": raisecomVctPortCableTX2Length,
       "raisecomVctPortCableRX2Status": raisecomVctPortCableRX2Status,
       "raisecomVctPortCableRX2Length": raisecomVctPortCableRX2Length,
       "raisecomVctPortCableLengthFuzz": raisecomVctPortCableLengthFuzz,
       "raisecomVctPortStartTest": raisecomVctPortStartTest}
)
