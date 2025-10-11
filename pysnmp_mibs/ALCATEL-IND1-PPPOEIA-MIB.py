# SNMP MIB module (ALCATEL-IND1-PPPOEIA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alcatel/ALCATEL-IND1-PPPOEIA-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:09:13 2025
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

(softentIND1PPPoEIA,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1PPPoEIA")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

alcatelIND1PPPoEIAMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1PPPoEIAMIB.setRevisions(
        ("2011-01-24 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PPPoEIACircuitIDFieldType(TextualConvention, Integer32):
    status = "current"
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
        *(("none", 0),
          ("base-mac", 1),
          ("system-name", 2),
          ("user-string", 3),
          ("interface-alias", 4),
          ("vlan", 5),
          ("interface", 6),
          ("cvlan", 7))
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1PPPoEIAMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1PPPoEIAMIBObjects = _AlcatelIND1PPPoEIAMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1PPPoEIAMIBObjects.setStatus("current")


class _AlaPPPoEIAGlobalStatus_Type(Integer32):
    """Custom type alaPPPoEIAGlobalStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaPPPoEIAGlobalStatus_Type.__name__ = "Integer32"
_AlaPPPoEIAGlobalStatus_Object = MibScalar
alaPPPoEIAGlobalStatus = _AlaPPPoEIAGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 1, 1),
    _AlaPPPoEIAGlobalStatus_Type()
)
alaPPPoEIAGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPPPoEIAGlobalStatus.setStatus("current")


class _AlaPPPoEIAGlobalAccessNodeIDFormatType_Type(Integer32):
    """Custom type alaPPPoEIAGlobalAccessNodeIDFormatType based on Integer32"""
    defaultValue = 1

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
        *(("base-mac", 1),
          ("system-name", 2),
          ("mgnt-address", 3),
          ("user-string", 4))
    )


_AlaPPPoEIAGlobalAccessNodeIDFormatType_Type.__name__ = "Integer32"
_AlaPPPoEIAGlobalAccessNodeIDFormatType_Object = MibScalar
alaPPPoEIAGlobalAccessNodeIDFormatType = _AlaPPPoEIAGlobalAccessNodeIDFormatType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 1, 2),
    _AlaPPPoEIAGlobalAccessNodeIDFormatType_Type()
)
alaPPPoEIAGlobalAccessNodeIDFormatType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPPPoEIAGlobalAccessNodeIDFormatType.setStatus("current")


class _AlaPPPoEIAGlobalAccessNodeIDStringValue_Type(SnmpAdminString):
    """Custom type alaPPPoEIAGlobalAccessNodeIDStringValue based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaPPPoEIAGlobalAccessNodeIDStringValue_Type.__name__ = "SnmpAdminString"
_AlaPPPoEIAGlobalAccessNodeIDStringValue_Object = MibScalar
alaPPPoEIAGlobalAccessNodeIDStringValue = _AlaPPPoEIAGlobalAccessNodeIDStringValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 1, 3),
    _AlaPPPoEIAGlobalAccessNodeIDStringValue_Type()
)
alaPPPoEIAGlobalAccessNodeIDStringValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPPPoEIAGlobalAccessNodeIDStringValue.setStatus("current")


class _AlaPPPoEIAGlobalCircuitIDFormatType_Type(Integer32):
    """Custom type alaPPPoEIAGlobalCircuitIDFormatType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("ascii", 2),
          ("atm", 3))
    )


_AlaPPPoEIAGlobalCircuitIDFormatType_Type.__name__ = "Integer32"
_AlaPPPoEIAGlobalCircuitIDFormatType_Object = MibScalar
alaPPPoEIAGlobalCircuitIDFormatType = _AlaPPPoEIAGlobalCircuitIDFormatType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 1, 4),
    _AlaPPPoEIAGlobalCircuitIDFormatType_Type()
)
alaPPPoEIAGlobalCircuitIDFormatType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPPPoEIAGlobalCircuitIDFormatType.setStatus("current")


class _AlaPPPoEIAGlobalCircuitIDField1_Type(PPPoEIACircuitIDFieldType):
    """Custom type alaPPPoEIAGlobalCircuitIDField1 based on PPPoEIACircuitIDFieldType"""
    defaultValue = 0


_AlaPPPoEIAGlobalCircuitIDField1_Type.__name__ = "PPPoEIACircuitIDFieldType"
_AlaPPPoEIAGlobalCircuitIDField1_Object = MibScalar
alaPPPoEIAGlobalCircuitIDField1 = _AlaPPPoEIAGlobalCircuitIDField1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 1, 5),
    _AlaPPPoEIAGlobalCircuitIDField1_Type()
)
alaPPPoEIAGlobalCircuitIDField1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPPPoEIAGlobalCircuitIDField1.setStatus("current")


class _AlaPPPoEIAGlobalCircuitIDField1StrVal_Type(SnmpAdminString):
    """Custom type alaPPPoEIAGlobalCircuitIDField1StrVal based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaPPPoEIAGlobalCircuitIDField1StrVal_Type.__name__ = "SnmpAdminString"
_AlaPPPoEIAGlobalCircuitIDField1StrVal_Object = MibScalar
alaPPPoEIAGlobalCircuitIDField1StrVal = _AlaPPPoEIAGlobalCircuitIDField1StrVal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 1, 6),
    _AlaPPPoEIAGlobalCircuitIDField1StrVal_Type()
)
alaPPPoEIAGlobalCircuitIDField1StrVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPPPoEIAGlobalCircuitIDField1StrVal.setStatus("current")


class _AlaPPPoEIAGlobalCircuitIDField2_Type(PPPoEIACircuitIDFieldType):
    """Custom type alaPPPoEIAGlobalCircuitIDField2 based on PPPoEIACircuitIDFieldType"""
    defaultValue = 0


_AlaPPPoEIAGlobalCircuitIDField2_Type.__name__ = "PPPoEIACircuitIDFieldType"
_AlaPPPoEIAGlobalCircuitIDField2_Object = MibScalar
alaPPPoEIAGlobalCircuitIDField2 = _AlaPPPoEIAGlobalCircuitIDField2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 1, 7),
    _AlaPPPoEIAGlobalCircuitIDField2_Type()
)
alaPPPoEIAGlobalCircuitIDField2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPPPoEIAGlobalCircuitIDField2.setStatus("current")


class _AlaPPPoEIAGlobalCircuitIDField2StrVal_Type(SnmpAdminString):
    """Custom type alaPPPoEIAGlobalCircuitIDField2StrVal based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaPPPoEIAGlobalCircuitIDField2StrVal_Type.__name__ = "SnmpAdminString"
_AlaPPPoEIAGlobalCircuitIDField2StrVal_Object = MibScalar
alaPPPoEIAGlobalCircuitIDField2StrVal = _AlaPPPoEIAGlobalCircuitIDField2StrVal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 1, 8),
    _AlaPPPoEIAGlobalCircuitIDField2StrVal_Type()
)
alaPPPoEIAGlobalCircuitIDField2StrVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPPPoEIAGlobalCircuitIDField2StrVal.setStatus("current")


class _AlaPPPoEIAGlobalCircuitIDField3_Type(PPPoEIACircuitIDFieldType):
    """Custom type alaPPPoEIAGlobalCircuitIDField3 based on PPPoEIACircuitIDFieldType"""
    defaultValue = 0


_AlaPPPoEIAGlobalCircuitIDField3_Type.__name__ = "PPPoEIACircuitIDFieldType"
_AlaPPPoEIAGlobalCircuitIDField3_Object = MibScalar
alaPPPoEIAGlobalCircuitIDField3 = _AlaPPPoEIAGlobalCircuitIDField3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 1, 9),
    _AlaPPPoEIAGlobalCircuitIDField3_Type()
)
alaPPPoEIAGlobalCircuitIDField3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPPPoEIAGlobalCircuitIDField3.setStatus("current")


class _AlaPPPoEIAGlobalCircuitIDField3StrVal_Type(SnmpAdminString):
    """Custom type alaPPPoEIAGlobalCircuitIDField3StrVal based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaPPPoEIAGlobalCircuitIDField3StrVal_Type.__name__ = "SnmpAdminString"
_AlaPPPoEIAGlobalCircuitIDField3StrVal_Object = MibScalar
alaPPPoEIAGlobalCircuitIDField3StrVal = _AlaPPPoEIAGlobalCircuitIDField3StrVal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 1, 10),
    _AlaPPPoEIAGlobalCircuitIDField3StrVal_Type()
)
alaPPPoEIAGlobalCircuitIDField3StrVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPPPoEIAGlobalCircuitIDField3StrVal.setStatus("current")


class _AlaPPPoEIAGlobalCircuitIDField4_Type(PPPoEIACircuitIDFieldType):
    """Custom type alaPPPoEIAGlobalCircuitIDField4 based on PPPoEIACircuitIDFieldType"""
    defaultValue = 0


_AlaPPPoEIAGlobalCircuitIDField4_Type.__name__ = "PPPoEIACircuitIDFieldType"
_AlaPPPoEIAGlobalCircuitIDField4_Object = MibScalar
alaPPPoEIAGlobalCircuitIDField4 = _AlaPPPoEIAGlobalCircuitIDField4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 1, 11),
    _AlaPPPoEIAGlobalCircuitIDField4_Type()
)
alaPPPoEIAGlobalCircuitIDField4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPPPoEIAGlobalCircuitIDField4.setStatus("current")


class _AlaPPPoEIAGlobalCircuitIDField4StrVal_Type(SnmpAdminString):
    """Custom type alaPPPoEIAGlobalCircuitIDField4StrVal based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaPPPoEIAGlobalCircuitIDField4StrVal_Type.__name__ = "SnmpAdminString"
_AlaPPPoEIAGlobalCircuitIDField4StrVal_Object = MibScalar
alaPPPoEIAGlobalCircuitIDField4StrVal = _AlaPPPoEIAGlobalCircuitIDField4StrVal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 1, 12),
    _AlaPPPoEIAGlobalCircuitIDField4StrVal_Type()
)
alaPPPoEIAGlobalCircuitIDField4StrVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPPPoEIAGlobalCircuitIDField4StrVal.setStatus("current")


class _AlaPPPoEIAGlobalCircuitIDField5_Type(PPPoEIACircuitIDFieldType):
    """Custom type alaPPPoEIAGlobalCircuitIDField5 based on PPPoEIACircuitIDFieldType"""
    defaultValue = 0


_AlaPPPoEIAGlobalCircuitIDField5_Type.__name__ = "PPPoEIACircuitIDFieldType"
_AlaPPPoEIAGlobalCircuitIDField5_Object = MibScalar
alaPPPoEIAGlobalCircuitIDField5 = _AlaPPPoEIAGlobalCircuitIDField5_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 1, 13),
    _AlaPPPoEIAGlobalCircuitIDField5_Type()
)
alaPPPoEIAGlobalCircuitIDField5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPPPoEIAGlobalCircuitIDField5.setStatus("current")


class _AlaPPPoEIAGlobalCircuitIDField5StrVal_Type(SnmpAdminString):
    """Custom type alaPPPoEIAGlobalCircuitIDField5StrVal based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaPPPoEIAGlobalCircuitIDField5StrVal_Type.__name__ = "SnmpAdminString"
_AlaPPPoEIAGlobalCircuitIDField5StrVal_Object = MibScalar
alaPPPoEIAGlobalCircuitIDField5StrVal = _AlaPPPoEIAGlobalCircuitIDField5StrVal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 1, 14),
    _AlaPPPoEIAGlobalCircuitIDField5StrVal_Type()
)
alaPPPoEIAGlobalCircuitIDField5StrVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPPPoEIAGlobalCircuitIDField5StrVal.setStatus("current")


class _AlaPPPoEIAGlobalCircuitIDDelimiter_Type(OctetString):
    """Custom type alaPPPoEIAGlobalCircuitIDDelimiter based on OctetString"""
    defaultValue = OctetString(":")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_AlaPPPoEIAGlobalCircuitIDDelimiter_Type.__name__ = "OctetString"
_AlaPPPoEIAGlobalCircuitIDDelimiter_Object = MibScalar
alaPPPoEIAGlobalCircuitIDDelimiter = _AlaPPPoEIAGlobalCircuitIDDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 1, 15),
    _AlaPPPoEIAGlobalCircuitIDDelimiter_Type()
)
alaPPPoEIAGlobalCircuitIDDelimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPPPoEIAGlobalCircuitIDDelimiter.setStatus("current")


class _AlaPPPoEIAGlobalRemoteIDFormatType_Type(Integer32):
    """Custom type alaPPPoEIAGlobalRemoteIDFormatType based on Integer32"""
    defaultValue = 1

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
        *(("base-mac", 1),
          ("system-name", 2),
          ("mgnt-address", 3),
          ("user-string", 4))
    )


_AlaPPPoEIAGlobalRemoteIDFormatType_Type.__name__ = "Integer32"
_AlaPPPoEIAGlobalRemoteIDFormatType_Object = MibScalar
alaPPPoEIAGlobalRemoteIDFormatType = _AlaPPPoEIAGlobalRemoteIDFormatType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 1, 16),
    _AlaPPPoEIAGlobalRemoteIDFormatType_Type()
)
alaPPPoEIAGlobalRemoteIDFormatType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPPPoEIAGlobalRemoteIDFormatType.setStatus("current")


class _AlaPPPoEIAGlobalRemoteIDStringValue_Type(SnmpAdminString):
    """Custom type alaPPPoEIAGlobalRemoteIDStringValue based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaPPPoEIAGlobalRemoteIDStringValue_Type.__name__ = "SnmpAdminString"
_AlaPPPoEIAGlobalRemoteIDStringValue_Object = MibScalar
alaPPPoEIAGlobalRemoteIDStringValue = _AlaPPPoEIAGlobalRemoteIDStringValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 1, 17),
    _AlaPPPoEIAGlobalRemoteIDStringValue_Type()
)
alaPPPoEIAGlobalRemoteIDStringValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPPPoEIAGlobalRemoteIDStringValue.setStatus("current")


class _AlaPPPoEIAGlobalClearStats_Type(Integer32):
    """Custom type alaPPPoEIAGlobalClearStats based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_AlaPPPoEIAGlobalClearStats_Type.__name__ = "Integer32"
_AlaPPPoEIAGlobalClearStats_Object = MibScalar
alaPPPoEIAGlobalClearStats = _AlaPPPoEIAGlobalClearStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 1, 18),
    _AlaPPPoEIAGlobalClearStats_Type()
)
alaPPPoEIAGlobalClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPPPoEIAGlobalClearStats.setStatus("current")
_AlaPPPoEIAPortConfig_ObjectIdentity = ObjectIdentity
alaPPPoEIAPortConfig = _AlaPPPoEIAPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 1, 19)
)
_AlaPPPoEIAPortConfigTable_Object = MibTable
alaPPPoEIAPortConfigTable = _AlaPPPoEIAPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 1, 19, 1)
)
if mibBuilder.loadTexts:
    alaPPPoEIAPortConfigTable.setStatus("current")
_AlaPPPoEIAPortConfigEntry_Object = MibTableRow
alaPPPoEIAPortConfigEntry = _AlaPPPoEIAPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 1, 19, 1, 1)
)
alaPPPoEIAPortConfigEntry.setIndexNames(
    (0, "ALCATEL-IND1-PPPOEIA-MIB", "alaPPPoEIAPortConfigIfIndex"),
)
if mibBuilder.loadTexts:
    alaPPPoEIAPortConfigEntry.setStatus("current")
_AlaPPPoEIAPortConfigIfIndex_Type = InterfaceIndex
_AlaPPPoEIAPortConfigIfIndex_Object = MibTableColumn
alaPPPoEIAPortConfigIfIndex = _AlaPPPoEIAPortConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 1, 19, 1, 1, 1),
    _AlaPPPoEIAPortConfigIfIndex_Type()
)
alaPPPoEIAPortConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPPPoEIAPortConfigIfIndex.setStatus("current")


class _AlaPPPoEIAPortConfigStatus_Type(Integer32):
    """Custom type alaPPPoEIAPortConfigStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaPPPoEIAPortConfigStatus_Type.__name__ = "Integer32"
_AlaPPPoEIAPortConfigStatus_Object = MibTableColumn
alaPPPoEIAPortConfigStatus = _AlaPPPoEIAPortConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 1, 19, 1, 1, 2),
    _AlaPPPoEIAPortConfigStatus_Type()
)
alaPPPoEIAPortConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPPPoEIAPortConfigStatus.setStatus("current")


class _AlaPPPoEIAPortConfigTrustMode_Type(Integer32):
    """Custom type alaPPPoEIAPortConfigTrustMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("trusted", 2))
    )


_AlaPPPoEIAPortConfigTrustMode_Type.__name__ = "Integer32"
_AlaPPPoEIAPortConfigTrustMode_Object = MibTableColumn
alaPPPoEIAPortConfigTrustMode = _AlaPPPoEIAPortConfigTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 1, 19, 1, 1, 3),
    _AlaPPPoEIAPortConfigTrustMode_Type()
)
alaPPPoEIAPortConfigTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPPPoEIAPortConfigTrustMode.setStatus("current")
_AlaPPPoEIAStats_ObjectIdentity = ObjectIdentity
alaPPPoEIAStats = _AlaPPPoEIAStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 1, 20)
)
_AlaPPPoEIAStatsTable_Object = MibTable
alaPPPoEIAStatsTable = _AlaPPPoEIAStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 1, 20, 1)
)
if mibBuilder.loadTexts:
    alaPPPoEIAStatsTable.setStatus("current")
_AlaPPPoEIAStatsEntry_Object = MibTableRow
alaPPPoEIAStatsEntry = _AlaPPPoEIAStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 1, 20, 1, 1)
)
alaPPPoEIAStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-PPPOEIA-MIB", "alaPPPoEIAStatsIfIndex"),
)
if mibBuilder.loadTexts:
    alaPPPoEIAStatsEntry.setStatus("current")
_AlaPPPoEIAStatsIfIndex_Type = InterfaceIndex
_AlaPPPoEIAStatsIfIndex_Object = MibTableColumn
alaPPPoEIAStatsIfIndex = _AlaPPPoEIAStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 1, 20, 1, 1, 1),
    _AlaPPPoEIAStatsIfIndex_Type()
)
alaPPPoEIAStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPPPoEIAStatsIfIndex.setStatus("current")


class _AlaPPPoEIAStatsClearStats_Type(Integer32):
    """Custom type alaPPPoEIAStatsClearStats based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_AlaPPPoEIAStatsClearStats_Type.__name__ = "Integer32"
_AlaPPPoEIAStatsClearStats_Object = MibTableColumn
alaPPPoEIAStatsClearStats = _AlaPPPoEIAStatsClearStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 1, 20, 1, 1, 2),
    _AlaPPPoEIAStatsClearStats_Type()
)
alaPPPoEIAStatsClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPPPoEIAStatsClearStats.setStatus("current")
_AlaPPPoEIAStatsPADIRxCounter_Type = Counter32
_AlaPPPoEIAStatsPADIRxCounter_Object = MibTableColumn
alaPPPoEIAStatsPADIRxCounter = _AlaPPPoEIAStatsPADIRxCounter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 1, 20, 1, 1, 3),
    _AlaPPPoEIAStatsPADIRxCounter_Type()
)
alaPPPoEIAStatsPADIRxCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPPPoEIAStatsPADIRxCounter.setStatus("current")
_AlaPPPoEIAStatsPADRRxCounter_Type = Counter32
_AlaPPPoEIAStatsPADRRxCounter_Object = MibTableColumn
alaPPPoEIAStatsPADRRxCounter = _AlaPPPoEIAStatsPADRRxCounter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 1, 20, 1, 1, 4),
    _AlaPPPoEIAStatsPADRRxCounter_Type()
)
alaPPPoEIAStatsPADRRxCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPPPoEIAStatsPADRRxCounter.setStatus("current")
_AlaPPPoEIAStatsPADTRxCounter_Type = Counter32
_AlaPPPoEIAStatsPADTRxCounter_Object = MibTableColumn
alaPPPoEIAStatsPADTRxCounter = _AlaPPPoEIAStatsPADTRxCounter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 1, 20, 1, 1, 5),
    _AlaPPPoEIAStatsPADTRxCounter_Type()
)
alaPPPoEIAStatsPADTRxCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPPPoEIAStatsPADTRxCounter.setStatus("current")
_AlaPPPoEIAStatsPADIRxDiscardCounter_Type = Counter32
_AlaPPPoEIAStatsPADIRxDiscardCounter_Object = MibTableColumn
alaPPPoEIAStatsPADIRxDiscardCounter = _AlaPPPoEIAStatsPADIRxDiscardCounter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 1, 20, 1, 1, 6),
    _AlaPPPoEIAStatsPADIRxDiscardCounter_Type()
)
alaPPPoEIAStatsPADIRxDiscardCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPPPoEIAStatsPADIRxDiscardCounter.setStatus("current")
_AlaPPPoEIAStatsPADRRxDiscardCounter_Type = Counter32
_AlaPPPoEIAStatsPADRRxDiscardCounter_Object = MibTableColumn
alaPPPoEIAStatsPADRRxDiscardCounter = _AlaPPPoEIAStatsPADRRxDiscardCounter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 1, 20, 1, 1, 7),
    _AlaPPPoEIAStatsPADRRxDiscardCounter_Type()
)
alaPPPoEIAStatsPADRRxDiscardCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPPPoEIAStatsPADRRxDiscardCounter.setStatus("current")
_AlaPPPoEIAStatsPADTRxDiscardCounter_Type = Counter32
_AlaPPPoEIAStatsPADTRxDiscardCounter_Object = MibTableColumn
alaPPPoEIAStatsPADTRxDiscardCounter = _AlaPPPoEIAStatsPADTRxDiscardCounter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 1, 20, 1, 1, 8),
    _AlaPPPoEIAStatsPADTRxDiscardCounter_Type()
)
alaPPPoEIAStatsPADTRxDiscardCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPPPoEIAStatsPADTRxDiscardCounter.setStatus("current")
_AlaPPPoEIAStatsPADORxDiscardCounter_Type = Counter32
_AlaPPPoEIAStatsPADORxDiscardCounter_Object = MibTableColumn
alaPPPoEIAStatsPADORxDiscardCounter = _AlaPPPoEIAStatsPADORxDiscardCounter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 1, 20, 1, 1, 9),
    _AlaPPPoEIAStatsPADORxDiscardCounter_Type()
)
alaPPPoEIAStatsPADORxDiscardCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPPPoEIAStatsPADORxDiscardCounter.setStatus("current")
_AlaPPPoEIAStatsPADSRxDiscardCounter_Type = Counter32
_AlaPPPoEIAStatsPADSRxDiscardCounter_Object = MibTableColumn
alaPPPoEIAStatsPADSRxDiscardCounter = _AlaPPPoEIAStatsPADSRxDiscardCounter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 1, 20, 1, 1, 10),
    _AlaPPPoEIAStatsPADSRxDiscardCounter_Type()
)
alaPPPoEIAStatsPADSRxDiscardCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPPPoEIAStatsPADSRxDiscardCounter.setStatus("current")
_AlcatelIND1PPPoEIAMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1PPPoEIAMIBConformance = _AlcatelIND1PPPoEIAMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1PPPoEIAMIBConformance.setStatus("current")
_AlcatelIND1PPPoEIAMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1PPPoEIAMIBGroups = _AlcatelIND1PPPoEIAMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1PPPoEIAMIBGroups.setStatus("current")
_AlcatelIND1PPPoEIAMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1PPPoEIAMIBCompliances = _AlcatelIND1PPPoEIAMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1PPPoEIAMIBCompliances.setStatus("current")

# Managed Objects groups

alaPPPoEIAGlobalConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 2, 1, 1)
)
alaPPPoEIAGlobalConfigGroup.setObjects(
      *(("ALCATEL-IND1-PPPOEIA-MIB", "alaPPPoEIAGlobalStatus"),
        ("ALCATEL-IND1-PPPOEIA-MIB", "alaPPPoEIAGlobalAccessNodeIDFormatType"),
        ("ALCATEL-IND1-PPPOEIA-MIB", "alaPPPoEIAGlobalAccessNodeIDStringValue"),
        ("ALCATEL-IND1-PPPOEIA-MIB", "alaPPPoEIAGlobalCircuitIDFormatType"),
        ("ALCATEL-IND1-PPPOEIA-MIB", "alaPPPoEIAGlobalCircuitIDField1"),
        ("ALCATEL-IND1-PPPOEIA-MIB", "alaPPPoEIAGlobalCircuitIDField1StrVal"),
        ("ALCATEL-IND1-PPPOEIA-MIB", "alaPPPoEIAGlobalCircuitIDField2"),
        ("ALCATEL-IND1-PPPOEIA-MIB", "alaPPPoEIAGlobalCircuitIDField2StrVal"),
        ("ALCATEL-IND1-PPPOEIA-MIB", "alaPPPoEIAGlobalCircuitIDField3"),
        ("ALCATEL-IND1-PPPOEIA-MIB", "alaPPPoEIAGlobalCircuitIDField3StrVal"),
        ("ALCATEL-IND1-PPPOEIA-MIB", "alaPPPoEIAGlobalCircuitIDField4"),
        ("ALCATEL-IND1-PPPOEIA-MIB", "alaPPPoEIAGlobalCircuitIDField4StrVal"),
        ("ALCATEL-IND1-PPPOEIA-MIB", "alaPPPoEIAGlobalCircuitIDField5"),
        ("ALCATEL-IND1-PPPOEIA-MIB", "alaPPPoEIAGlobalCircuitIDField5StrVal"),
        ("ALCATEL-IND1-PPPOEIA-MIB", "alaPPPoEIAGlobalCircuitIDDelimiter"),
        ("ALCATEL-IND1-PPPOEIA-MIB", "alaPPPoEIAGlobalRemoteIDFormatType"),
        ("ALCATEL-IND1-PPPOEIA-MIB", "alaPPPoEIAGlobalRemoteIDStringValue"),
        ("ALCATEL-IND1-PPPOEIA-MIB", "alaPPPoEIAGlobalClearStats"))
)
if mibBuilder.loadTexts:
    alaPPPoEIAGlobalConfigGroup.setStatus("current")

alaPPPoEIAPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 2, 1, 2)
)
alaPPPoEIAPortConfigGroup.setObjects(
      *(("ALCATEL-IND1-PPPOEIA-MIB", "alaPPPoEIAPortConfigStatus"),
        ("ALCATEL-IND1-PPPOEIA-MIB", "alaPPPoEIAPortConfigTrustMode"))
)
if mibBuilder.loadTexts:
    alaPPPoEIAPortConfigGroup.setStatus("current")

alaPPPoEIAStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 2, 1, 3)
)
alaPPPoEIAStatsGroup.setObjects(
      *(("ALCATEL-IND1-PPPOEIA-MIB", "alaPPPoEIAStatsClearStats"),
        ("ALCATEL-IND1-PPPOEIA-MIB", "alaPPPoEIAStatsPADIRxCounter"),
        ("ALCATEL-IND1-PPPOEIA-MIB", "alaPPPoEIAStatsPADRRxCounter"),
        ("ALCATEL-IND1-PPPOEIA-MIB", "alaPPPoEIAStatsPADTRxCounter"),
        ("ALCATEL-IND1-PPPOEIA-MIB", "alaPPPoEIAStatsPADIRxDiscardCounter"),
        ("ALCATEL-IND1-PPPOEIA-MIB", "alaPPPoEIAStatsPADRRxDiscardCounter"),
        ("ALCATEL-IND1-PPPOEIA-MIB", "alaPPPoEIAStatsPADTRxDiscardCounter"),
        ("ALCATEL-IND1-PPPOEIA-MIB", "alaPPPoEIAStatsPADORxDiscardCounter"),
        ("ALCATEL-IND1-PPPOEIA-MIB", "alaPPPoEIAStatsPADSRxDiscardCounter"))
)
if mibBuilder.loadTexts:
    alaPPPoEIAStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1PPPoEIAMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 64, 1, 2, 2, 1)
)
alcatelIND1PPPoEIAMIBCompliance.setObjects(
      *(("ALCATEL-IND1-PPPOEIA-MIB", "alaPPPoEIAGlobalConfigGroup"),
        ("ALCATEL-IND1-PPPOEIA-MIB", "alaPPPoEIAPortConfigGroup"),
        ("ALCATEL-IND1-PPPOEIA-MIB", "alaPPPoEIAStatsGroup"))
)
if mibBuilder.loadTexts:
    alcatelIND1PPPoEIAMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-PPPOEIA-MIB",
    **{"PPPoEIACircuitIDFieldType": PPPoEIACircuitIDFieldType,
       "alcatelIND1PPPoEIAMIB": alcatelIND1PPPoEIAMIB,
       "alcatelIND1PPPoEIAMIBObjects": alcatelIND1PPPoEIAMIBObjects,
       "alaPPPoEIAGlobalStatus": alaPPPoEIAGlobalStatus,
       "alaPPPoEIAGlobalAccessNodeIDFormatType": alaPPPoEIAGlobalAccessNodeIDFormatType,
       "alaPPPoEIAGlobalAccessNodeIDStringValue": alaPPPoEIAGlobalAccessNodeIDStringValue,
       "alaPPPoEIAGlobalCircuitIDFormatType": alaPPPoEIAGlobalCircuitIDFormatType,
       "alaPPPoEIAGlobalCircuitIDField1": alaPPPoEIAGlobalCircuitIDField1,
       "alaPPPoEIAGlobalCircuitIDField1StrVal": alaPPPoEIAGlobalCircuitIDField1StrVal,
       "alaPPPoEIAGlobalCircuitIDField2": alaPPPoEIAGlobalCircuitIDField2,
       "alaPPPoEIAGlobalCircuitIDField2StrVal": alaPPPoEIAGlobalCircuitIDField2StrVal,
       "alaPPPoEIAGlobalCircuitIDField3": alaPPPoEIAGlobalCircuitIDField3,
       "alaPPPoEIAGlobalCircuitIDField3StrVal": alaPPPoEIAGlobalCircuitIDField3StrVal,
       "alaPPPoEIAGlobalCircuitIDField4": alaPPPoEIAGlobalCircuitIDField4,
       "alaPPPoEIAGlobalCircuitIDField4StrVal": alaPPPoEIAGlobalCircuitIDField4StrVal,
       "alaPPPoEIAGlobalCircuitIDField5": alaPPPoEIAGlobalCircuitIDField5,
       "alaPPPoEIAGlobalCircuitIDField5StrVal": alaPPPoEIAGlobalCircuitIDField5StrVal,
       "alaPPPoEIAGlobalCircuitIDDelimiter": alaPPPoEIAGlobalCircuitIDDelimiter,
       "alaPPPoEIAGlobalRemoteIDFormatType": alaPPPoEIAGlobalRemoteIDFormatType,
       "alaPPPoEIAGlobalRemoteIDStringValue": alaPPPoEIAGlobalRemoteIDStringValue,
       "alaPPPoEIAGlobalClearStats": alaPPPoEIAGlobalClearStats,
       "alaPPPoEIAPortConfig": alaPPPoEIAPortConfig,
       "alaPPPoEIAPortConfigTable": alaPPPoEIAPortConfigTable,
       "alaPPPoEIAPortConfigEntry": alaPPPoEIAPortConfigEntry,
       "alaPPPoEIAPortConfigIfIndex": alaPPPoEIAPortConfigIfIndex,
       "alaPPPoEIAPortConfigStatus": alaPPPoEIAPortConfigStatus,
       "alaPPPoEIAPortConfigTrustMode": alaPPPoEIAPortConfigTrustMode,
       "alaPPPoEIAStats": alaPPPoEIAStats,
       "alaPPPoEIAStatsTable": alaPPPoEIAStatsTable,
       "alaPPPoEIAStatsEntry": alaPPPoEIAStatsEntry,
       "alaPPPoEIAStatsIfIndex": alaPPPoEIAStatsIfIndex,
       "alaPPPoEIAStatsClearStats": alaPPPoEIAStatsClearStats,
       "alaPPPoEIAStatsPADIRxCounter": alaPPPoEIAStatsPADIRxCounter,
       "alaPPPoEIAStatsPADRRxCounter": alaPPPoEIAStatsPADRRxCounter,
       "alaPPPoEIAStatsPADTRxCounter": alaPPPoEIAStatsPADTRxCounter,
       "alaPPPoEIAStatsPADIRxDiscardCounter": alaPPPoEIAStatsPADIRxDiscardCounter,
       "alaPPPoEIAStatsPADRRxDiscardCounter": alaPPPoEIAStatsPADRRxDiscardCounter,
       "alaPPPoEIAStatsPADTRxDiscardCounter": alaPPPoEIAStatsPADTRxDiscardCounter,
       "alaPPPoEIAStatsPADORxDiscardCounter": alaPPPoEIAStatsPADORxDiscardCounter,
       "alaPPPoEIAStatsPADSRxDiscardCounter": alaPPPoEIAStatsPADSRxDiscardCounter,
       "alcatelIND1PPPoEIAMIBConformance": alcatelIND1PPPoEIAMIBConformance,
       "alcatelIND1PPPoEIAMIBGroups": alcatelIND1PPPoEIAMIBGroups,
       "alaPPPoEIAGlobalConfigGroup": alaPPPoEIAGlobalConfigGroup,
       "alaPPPoEIAPortConfigGroup": alaPPPoEIAPortConfigGroup,
       "alaPPPoEIAStatsGroup": alaPPPoEIAStatsGroup,
       "alcatelIND1PPPoEIAMIBCompliances": alcatelIND1PPPoEIAMIBCompliances,
       "alcatelIND1PPPoEIAMIBCompliance": alcatelIND1PPPoEIAMIBCompliance}
)
