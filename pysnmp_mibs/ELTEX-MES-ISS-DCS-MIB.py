# SNMP MIB module (ELTEX-MES-ISS-DCS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-ISS-DCS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:50:58 2025
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

(eltMesIss,) = mibBuilder.importSymbols(
    "ELTEX-MES-ISS-MIB",
    "eltMesIss")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eltMesIssDcsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 13)
)
if mibBuilder.loadTexts:
    eltMesIssDcsMIB.setRevisions(
        ("2021-08-18 00:00",
         "2020-05-19 00:00",
         "2019-08-14 00:00",
         "2019-05-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EltMesIssDcsProtocol(TextualConvention, Integer32):
    status = "current"
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
        *(("dhcpv4", 1),
          ("dhcpv6", 2),
          ("pppoeia", 3),
          ("dhcpv4-relay", 4))
    )



class EltMesIssDcsOptionFormat(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tr101", 1),
          ("userdefined", 2))
    )



class EltMesIssDcsOptionDataEncoding(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("binary", 2))
    )



class EltMesIssDcsCircuitIdTr101Format(TextualConvention, Integer32):
    status = "current"
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
        *(("sp", 1),
          ("sv", 2),
          ("pv", 3),
          ("spv", 4))
    )



class EltMesIssDcsCircuitIdTr101Delimiter(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("std", 1),
          ("hash", 2),
          ("dot", 3),
          ("comma", 4),
          ("semicolon", 5),
          ("slash", 6),
          ("space", 7))
    )



# MIB Managed Objects in the order of their OIDs

_EltMesIssDcsObjects_ObjectIdentity = ObjectIdentity
eltMesIssDcsObjects = _EltMesIssDcsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 13, 1)
)
_EltMesIssDcsGlobals_ObjectIdentity = ObjectIdentity
eltMesIssDcsGlobals = _EltMesIssDcsGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 13, 1, 1)
)
_EltMesIssDcsOption82Table_Object = MibTable
eltMesIssDcsOption82Table = _EltMesIssDcsOption82Table_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 13, 1, 1, 1)
)
if mibBuilder.loadTexts:
    eltMesIssDcsOption82Table.setStatus("current")
_EltMesIssDcsOption82Entry_Object = MibTableRow
eltMesIssDcsOption82Entry = _EltMesIssDcsOption82Entry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 13, 1, 1, 1, 1)
)
eltMesIssDcsOption82Entry.setIndexNames(
    (0, "ELTEX-MES-ISS-DCS-MIB", "eltMesIssDcsOption82ProtocolType"),
)
if mibBuilder.loadTexts:
    eltMesIssDcsOption82Entry.setStatus("current")
_EltMesIssDcsOption82ProtocolType_Type = EltMesIssDcsProtocol
_EltMesIssDcsOption82ProtocolType_Object = MibTableColumn
eltMesIssDcsOption82ProtocolType = _EltMesIssDcsOption82ProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 13, 1, 1, 1, 1, 1),
    _EltMesIssDcsOption82ProtocolType_Type()
)
eltMesIssDcsOption82ProtocolType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssDcsOption82ProtocolType.setStatus("current")


class _EltMesIssDcsOption82Enabled_Type(TruthValue):
    """Custom type eltMesIssDcsOption82Enabled based on TruthValue"""
    defaultValue = 2


_EltMesIssDcsOption82Enabled_Type.__name__ = "TruthValue"
_EltMesIssDcsOption82Enabled_Object = MibTableColumn
eltMesIssDcsOption82Enabled = _EltMesIssDcsOption82Enabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 13, 1, 1, 1, 1, 2),
    _EltMesIssDcsOption82Enabled_Type()
)
eltMesIssDcsOption82Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssDcsOption82Enabled.setStatus("current")


class _EltMesIssDcsOption82CircuitIdFormat_Type(EltMesIssDcsOptionFormat):
    """Custom type eltMesIssDcsOption82CircuitIdFormat based on EltMesIssDcsOptionFormat"""
    defaultValue = 1


_EltMesIssDcsOption82CircuitIdFormat_Type.__name__ = "EltMesIssDcsOptionFormat"
_EltMesIssDcsOption82CircuitIdFormat_Object = MibTableColumn
eltMesIssDcsOption82CircuitIdFormat = _EltMesIssDcsOption82CircuitIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 13, 1, 1, 1, 1, 3),
    _EltMesIssDcsOption82CircuitIdFormat_Type()
)
eltMesIssDcsOption82CircuitIdFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssDcsOption82CircuitIdFormat.setStatus("current")
_EltMesIssDcsCircuitIdTr101Table_Object = MibTable
eltMesIssDcsCircuitIdTr101Table = _EltMesIssDcsCircuitIdTr101Table_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 13, 1, 1, 2)
)
if mibBuilder.loadTexts:
    eltMesIssDcsCircuitIdTr101Table.setStatus("current")
_EltMesIssDcsCircuitIdTr101Entry_Object = MibTableRow
eltMesIssDcsCircuitIdTr101Entry = _EltMesIssDcsCircuitIdTr101Entry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 13, 1, 1, 2, 1)
)
eltMesIssDcsCircuitIdTr101Entry.setIndexNames(
    (0, "ELTEX-MES-ISS-DCS-MIB", "eltMesIssDcsCircuitIdTr101Index"),
)
if mibBuilder.loadTexts:
    eltMesIssDcsCircuitIdTr101Entry.setStatus("current")
_EltMesIssDcsCircuitIdTr101Index_Type = EltMesIssDcsProtocol
_EltMesIssDcsCircuitIdTr101Index_Object = MibTableColumn
eltMesIssDcsCircuitIdTr101Index = _EltMesIssDcsCircuitIdTr101Index_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 13, 1, 1, 2, 1, 1),
    _EltMesIssDcsCircuitIdTr101Index_Type()
)
eltMesIssDcsCircuitIdTr101Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssDcsCircuitIdTr101Index.setStatus("current")


class _EltMesIssDcsCircuitIdTr101AccessNodeId_Type(DisplayString):
    """Custom type eltMesIssDcsCircuitIdTr101AccessNodeId based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_EltMesIssDcsCircuitIdTr101AccessNodeId_Type.__name__ = "DisplayString"
_EltMesIssDcsCircuitIdTr101AccessNodeId_Object = MibTableColumn
eltMesIssDcsCircuitIdTr101AccessNodeId = _EltMesIssDcsCircuitIdTr101AccessNodeId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 13, 1, 1, 2, 1, 2),
    _EltMesIssDcsCircuitIdTr101AccessNodeId_Type()
)
eltMesIssDcsCircuitIdTr101AccessNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssDcsCircuitIdTr101AccessNodeId.setStatus("current")


class _EltMesIssDcsCircuitIdTr101Format_Type(EltMesIssDcsCircuitIdTr101Format):
    """Custom type eltMesIssDcsCircuitIdTr101Format based on EltMesIssDcsCircuitIdTr101Format"""
    defaultValue = 4


_EltMesIssDcsCircuitIdTr101Format_Type.__name__ = "EltMesIssDcsCircuitIdTr101Format"
_EltMesIssDcsCircuitIdTr101Format_Object = MibTableColumn
eltMesIssDcsCircuitIdTr101Format = _EltMesIssDcsCircuitIdTr101Format_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 13, 1, 1, 2, 1, 3),
    _EltMesIssDcsCircuitIdTr101Format_Type()
)
eltMesIssDcsCircuitIdTr101Format.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssDcsCircuitIdTr101Format.setStatus("current")


class _EltMesIssDcsCircuitIdTr101Delimiter_Type(EltMesIssDcsCircuitIdTr101Delimiter):
    """Custom type eltMesIssDcsCircuitIdTr101Delimiter based on EltMesIssDcsCircuitIdTr101Delimiter"""
    defaultValue = 1


_EltMesIssDcsCircuitIdTr101Delimiter_Type.__name__ = "EltMesIssDcsCircuitIdTr101Delimiter"
_EltMesIssDcsCircuitIdTr101Delimiter_Object = MibTableColumn
eltMesIssDcsCircuitIdTr101Delimiter = _EltMesIssDcsCircuitIdTr101Delimiter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 13, 1, 1, 2, 1, 4),
    _EltMesIssDcsCircuitIdTr101Delimiter_Type()
)
eltMesIssDcsCircuitIdTr101Delimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssDcsCircuitIdTr101Delimiter.setStatus("current")
_EltMesIssDcsCircuitIdUserDefinedTable_Object = MibTable
eltMesIssDcsCircuitIdUserDefinedTable = _EltMesIssDcsCircuitIdUserDefinedTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 13, 1, 1, 3)
)
if mibBuilder.loadTexts:
    eltMesIssDcsCircuitIdUserDefinedTable.setStatus("current")
_EltMesIssDcsCircuitIdUserDefinedEntry_Object = MibTableRow
eltMesIssDcsCircuitIdUserDefinedEntry = _EltMesIssDcsCircuitIdUserDefinedEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 13, 1, 1, 3, 1)
)
eltMesIssDcsCircuitIdUserDefinedEntry.setIndexNames(
    (0, "ELTEX-MES-ISS-DCS-MIB", "eltMesIssDcsCircuitIdUserDefinedIndex"),
)
if mibBuilder.loadTexts:
    eltMesIssDcsCircuitIdUserDefinedEntry.setStatus("current")
_EltMesIssDcsCircuitIdUserDefinedIndex_Type = EltMesIssDcsProtocol
_EltMesIssDcsCircuitIdUserDefinedIndex_Object = MibTableColumn
eltMesIssDcsCircuitIdUserDefinedIndex = _EltMesIssDcsCircuitIdUserDefinedIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 13, 1, 1, 3, 1, 1),
    _EltMesIssDcsCircuitIdUserDefinedIndex_Type()
)
eltMesIssDcsCircuitIdUserDefinedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssDcsCircuitIdUserDefinedIndex.setStatus("current")


class _EltMesIssDcsCircuitIdUserDefinedString_Type(DisplayString):
    """Custom type eltMesIssDcsCircuitIdUserDefinedString based on DisplayString"""
    defaultValue = OctetString("%h %p %v")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_EltMesIssDcsCircuitIdUserDefinedString_Type.__name__ = "DisplayString"
_EltMesIssDcsCircuitIdUserDefinedString_Object = MibTableColumn
eltMesIssDcsCircuitIdUserDefinedString = _EltMesIssDcsCircuitIdUserDefinedString_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 13, 1, 1, 3, 1, 2),
    _EltMesIssDcsCircuitIdUserDefinedString_Type()
)
eltMesIssDcsCircuitIdUserDefinedString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssDcsCircuitIdUserDefinedString.setStatus("current")


class _EltMesIssDcsCircuitIdUserDefinedDataEncoding_Type(EltMesIssDcsOptionDataEncoding):
    """Custom type eltMesIssDcsCircuitIdUserDefinedDataEncoding based on EltMesIssDcsOptionDataEncoding"""
    defaultValue = 1


_EltMesIssDcsCircuitIdUserDefinedDataEncoding_Type.__name__ = "EltMesIssDcsOptionDataEncoding"
_EltMesIssDcsCircuitIdUserDefinedDataEncoding_Object = MibTableColumn
eltMesIssDcsCircuitIdUserDefinedDataEncoding = _EltMesIssDcsCircuitIdUserDefinedDataEncoding_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 13, 1, 1, 3, 1, 3),
    _EltMesIssDcsCircuitIdUserDefinedDataEncoding_Type()
)
eltMesIssDcsCircuitIdUserDefinedDataEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssDcsCircuitIdUserDefinedDataEncoding.setStatus("current")


class _EltMesIssDcsCircuitIdUserDefinedSubtypesEnabled_Type(TruthValue):
    """Custom type eltMesIssDcsCircuitIdUserDefinedSubtypesEnabled based on TruthValue"""
    defaultValue = 2


_EltMesIssDcsCircuitIdUserDefinedSubtypesEnabled_Type.__name__ = "TruthValue"
_EltMesIssDcsCircuitIdUserDefinedSubtypesEnabled_Object = MibTableColumn
eltMesIssDcsCircuitIdUserDefinedSubtypesEnabled = _EltMesIssDcsCircuitIdUserDefinedSubtypesEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 13, 1, 1, 3, 1, 4),
    _EltMesIssDcsCircuitIdUserDefinedSubtypesEnabled_Type()
)
eltMesIssDcsCircuitIdUserDefinedSubtypesEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssDcsCircuitIdUserDefinedSubtypesEnabled.setStatus("current")
_EltMesIssDcsRemoteIdUserDefinedTable_Object = MibTable
eltMesIssDcsRemoteIdUserDefinedTable = _EltMesIssDcsRemoteIdUserDefinedTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 13, 1, 1, 4)
)
if mibBuilder.loadTexts:
    eltMesIssDcsRemoteIdUserDefinedTable.setStatus("current")
_EltMesIssDcsRemoteIdUserDefinedEntry_Object = MibTableRow
eltMesIssDcsRemoteIdUserDefinedEntry = _EltMesIssDcsRemoteIdUserDefinedEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 13, 1, 1, 4, 1)
)
eltMesIssDcsRemoteIdUserDefinedEntry.setIndexNames(
    (0, "ELTEX-MES-ISS-DCS-MIB", "eltMesIssDcsRemoteIdUserDefinedIndex"),
)
if mibBuilder.loadTexts:
    eltMesIssDcsRemoteIdUserDefinedEntry.setStatus("current")
_EltMesIssDcsRemoteIdUserDefinedIndex_Type = EltMesIssDcsProtocol
_EltMesIssDcsRemoteIdUserDefinedIndex_Object = MibTableColumn
eltMesIssDcsRemoteIdUserDefinedIndex = _EltMesIssDcsRemoteIdUserDefinedIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 13, 1, 1, 4, 1, 1),
    _EltMesIssDcsRemoteIdUserDefinedIndex_Type()
)
eltMesIssDcsRemoteIdUserDefinedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssDcsRemoteIdUserDefinedIndex.setStatus("current")


class _EltMesIssDcsRemoteIdUserDefinedString_Type(DisplayString):
    """Custom type eltMesIssDcsRemoteIdUserDefinedString based on DisplayString"""
    defaultValue = OctetString("%h %p %v")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_EltMesIssDcsRemoteIdUserDefinedString_Type.__name__ = "DisplayString"
_EltMesIssDcsRemoteIdUserDefinedString_Object = MibTableColumn
eltMesIssDcsRemoteIdUserDefinedString = _EltMesIssDcsRemoteIdUserDefinedString_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 13, 1, 1, 4, 1, 2),
    _EltMesIssDcsRemoteIdUserDefinedString_Type()
)
eltMesIssDcsRemoteIdUserDefinedString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssDcsRemoteIdUserDefinedString.setStatus("current")


class _EltMesIssDcsRemoteIdUserDefinedDataEncoding_Type(EltMesIssDcsOptionDataEncoding):
    """Custom type eltMesIssDcsRemoteIdUserDefinedDataEncoding based on EltMesIssDcsOptionDataEncoding"""
    defaultValue = 1


_EltMesIssDcsRemoteIdUserDefinedDataEncoding_Type.__name__ = "EltMesIssDcsOptionDataEncoding"
_EltMesIssDcsRemoteIdUserDefinedDataEncoding_Object = MibTableColumn
eltMesIssDcsRemoteIdUserDefinedDataEncoding = _EltMesIssDcsRemoteIdUserDefinedDataEncoding_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 13, 1, 1, 4, 1, 3),
    _EltMesIssDcsRemoteIdUserDefinedDataEncoding_Type()
)
eltMesIssDcsRemoteIdUserDefinedDataEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssDcsRemoteIdUserDefinedDataEncoding.setStatus("current")


class _EltMesIssDcsRemoteIdUserDefinedSubtypesEnabled_Type(TruthValue):
    """Custom type eltMesIssDcsRemoteIdUserDefinedSubtypesEnabled based on TruthValue"""
    defaultValue = 2


_EltMesIssDcsRemoteIdUserDefinedSubtypesEnabled_Type.__name__ = "TruthValue"
_EltMesIssDcsRemoteIdUserDefinedSubtypesEnabled_Object = MibTableColumn
eltMesIssDcsRemoteIdUserDefinedSubtypesEnabled = _EltMesIssDcsRemoteIdUserDefinedSubtypesEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 13, 1, 1, 4, 1, 4),
    _EltMesIssDcsRemoteIdUserDefinedSubtypesEnabled_Type()
)
eltMesIssDcsRemoteIdUserDefinedSubtypesEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssDcsRemoteIdUserDefinedSubtypesEnabled.setStatus("current")
_EltMesIssDcsPortInfoOptTable_Object = MibTable
eltMesIssDcsPortInfoOptTable = _EltMesIssDcsPortInfoOptTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 13, 1, 1, 5)
)
if mibBuilder.loadTexts:
    eltMesIssDcsPortInfoOptTable.setStatus("current")
_EltMesIssDcsPortInfoOptEntry_Object = MibTableRow
eltMesIssDcsPortInfoOptEntry = _EltMesIssDcsPortInfoOptEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 13, 1, 1, 5, 1)
)
eltMesIssDcsPortInfoOptEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ELTEX-MES-ISS-DCS-MIB", "eltMesIssDcsPortInfoOptProtocolType"),
)
if mibBuilder.loadTexts:
    eltMesIssDcsPortInfoOptEntry.setStatus("current")
_EltMesIssDcsPortInfoOptProtocolType_Type = EltMesIssDcsProtocol
_EltMesIssDcsPortInfoOptProtocolType_Object = MibTableColumn
eltMesIssDcsPortInfoOptProtocolType = _EltMesIssDcsPortInfoOptProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 13, 1, 1, 5, 1, 1),
    _EltMesIssDcsPortInfoOptProtocolType_Type()
)
eltMesIssDcsPortInfoOptProtocolType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssDcsPortInfoOptProtocolType.setStatus("current")


class _EltMesIssDcsPortInfoOptEnabled_Type(TruthValue):
    """Custom type eltMesIssDcsPortInfoOptEnabled based on TruthValue"""
    defaultValue = 2


_EltMesIssDcsPortInfoOptEnabled_Type.__name__ = "TruthValue"
_EltMesIssDcsPortInfoOptEnabled_Object = MibTableColumn
eltMesIssDcsPortInfoOptEnabled = _EltMesIssDcsPortInfoOptEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 13, 1, 1, 5, 1, 2),
    _EltMesIssDcsPortInfoOptEnabled_Type()
)
eltMesIssDcsPortInfoOptEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssDcsPortInfoOptEnabled.setStatus("current")
_EltMesIssDcsVlanInfoOptTable_Object = MibTable
eltMesIssDcsVlanInfoOptTable = _EltMesIssDcsVlanInfoOptTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 13, 1, 1, 6)
)
if mibBuilder.loadTexts:
    eltMesIssDcsVlanInfoOptTable.setStatus("current")
_EltMesIssDcsVlanInfoOptEntry_Object = MibTableRow
eltMesIssDcsVlanInfoOptEntry = _EltMesIssDcsVlanInfoOptEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 13, 1, 1, 6, 1)
)
eltMesIssDcsVlanInfoOptEntry.setIndexNames(
    (0, "ELTEX-MES-ISS-DCS-MIB", "eltMesIssDcsVlanInfoOptVlanId"),
    (0, "ELTEX-MES-ISS-DCS-MIB", "eltMesIssDcsVlanInfoOptProtocolType"),
)
if mibBuilder.loadTexts:
    eltMesIssDcsVlanInfoOptEntry.setStatus("current")
_EltMesIssDcsVlanInfoOptVlanId_Type = VlanId
_EltMesIssDcsVlanInfoOptVlanId_Object = MibTableColumn
eltMesIssDcsVlanInfoOptVlanId = _EltMesIssDcsVlanInfoOptVlanId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 13, 1, 1, 6, 1, 1),
    _EltMesIssDcsVlanInfoOptVlanId_Type()
)
eltMesIssDcsVlanInfoOptVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssDcsVlanInfoOptVlanId.setStatus("current")
_EltMesIssDcsVlanInfoOptProtocolType_Type = EltMesIssDcsProtocol
_EltMesIssDcsVlanInfoOptProtocolType_Object = MibTableColumn
eltMesIssDcsVlanInfoOptProtocolType = _EltMesIssDcsVlanInfoOptProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 13, 1, 1, 6, 1, 2),
    _EltMesIssDcsVlanInfoOptProtocolType_Type()
)
eltMesIssDcsVlanInfoOptProtocolType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssDcsVlanInfoOptProtocolType.setStatus("current")


class _EltMesIssDcsVlanInfoOptEnabled_Type(TruthValue):
    """Custom type eltMesIssDcsVlanInfoOptEnabled based on TruthValue"""
    defaultValue = 2


_EltMesIssDcsVlanInfoOptEnabled_Type.__name__ = "TruthValue"
_EltMesIssDcsVlanInfoOptEnabled_Object = MibTableColumn
eltMesIssDcsVlanInfoOptEnabled = _EltMesIssDcsVlanInfoOptEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 13, 1, 1, 6, 1, 3),
    _EltMesIssDcsVlanInfoOptEnabled_Type()
)
eltMesIssDcsVlanInfoOptEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssDcsVlanInfoOptEnabled.setStatus("current")
_EltMesIssDcsVlanInfoOptRowStatus_Type = RowStatus
_EltMesIssDcsVlanInfoOptRowStatus_Object = MibTableColumn
eltMesIssDcsVlanInfoOptRowStatus = _EltMesIssDcsVlanInfoOptRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 13, 1, 1, 6, 1, 4),
    _EltMesIssDcsVlanInfoOptRowStatus_Type()
)
eltMesIssDcsVlanInfoOptRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssDcsVlanInfoOptRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-ISS-DCS-MIB",
    **{"EltMesIssDcsProtocol": EltMesIssDcsProtocol,
       "EltMesIssDcsOptionFormat": EltMesIssDcsOptionFormat,
       "EltMesIssDcsOptionDataEncoding": EltMesIssDcsOptionDataEncoding,
       "EltMesIssDcsCircuitIdTr101Format": EltMesIssDcsCircuitIdTr101Format,
       "EltMesIssDcsCircuitIdTr101Delimiter": EltMesIssDcsCircuitIdTr101Delimiter,
       "eltMesIssDcsMIB": eltMesIssDcsMIB,
       "eltMesIssDcsObjects": eltMesIssDcsObjects,
       "eltMesIssDcsGlobals": eltMesIssDcsGlobals,
       "eltMesIssDcsOption82Table": eltMesIssDcsOption82Table,
       "eltMesIssDcsOption82Entry": eltMesIssDcsOption82Entry,
       "eltMesIssDcsOption82ProtocolType": eltMesIssDcsOption82ProtocolType,
       "eltMesIssDcsOption82Enabled": eltMesIssDcsOption82Enabled,
       "eltMesIssDcsOption82CircuitIdFormat": eltMesIssDcsOption82CircuitIdFormat,
       "eltMesIssDcsCircuitIdTr101Table": eltMesIssDcsCircuitIdTr101Table,
       "eltMesIssDcsCircuitIdTr101Entry": eltMesIssDcsCircuitIdTr101Entry,
       "eltMesIssDcsCircuitIdTr101Index": eltMesIssDcsCircuitIdTr101Index,
       "eltMesIssDcsCircuitIdTr101AccessNodeId": eltMesIssDcsCircuitIdTr101AccessNodeId,
       "eltMesIssDcsCircuitIdTr101Format": eltMesIssDcsCircuitIdTr101Format,
       "eltMesIssDcsCircuitIdTr101Delimiter": eltMesIssDcsCircuitIdTr101Delimiter,
       "eltMesIssDcsCircuitIdUserDefinedTable": eltMesIssDcsCircuitIdUserDefinedTable,
       "eltMesIssDcsCircuitIdUserDefinedEntry": eltMesIssDcsCircuitIdUserDefinedEntry,
       "eltMesIssDcsCircuitIdUserDefinedIndex": eltMesIssDcsCircuitIdUserDefinedIndex,
       "eltMesIssDcsCircuitIdUserDefinedString": eltMesIssDcsCircuitIdUserDefinedString,
       "eltMesIssDcsCircuitIdUserDefinedDataEncoding": eltMesIssDcsCircuitIdUserDefinedDataEncoding,
       "eltMesIssDcsCircuitIdUserDefinedSubtypesEnabled": eltMesIssDcsCircuitIdUserDefinedSubtypesEnabled,
       "eltMesIssDcsRemoteIdUserDefinedTable": eltMesIssDcsRemoteIdUserDefinedTable,
       "eltMesIssDcsRemoteIdUserDefinedEntry": eltMesIssDcsRemoteIdUserDefinedEntry,
       "eltMesIssDcsRemoteIdUserDefinedIndex": eltMesIssDcsRemoteIdUserDefinedIndex,
       "eltMesIssDcsRemoteIdUserDefinedString": eltMesIssDcsRemoteIdUserDefinedString,
       "eltMesIssDcsRemoteIdUserDefinedDataEncoding": eltMesIssDcsRemoteIdUserDefinedDataEncoding,
       "eltMesIssDcsRemoteIdUserDefinedSubtypesEnabled": eltMesIssDcsRemoteIdUserDefinedSubtypesEnabled,
       "eltMesIssDcsPortInfoOptTable": eltMesIssDcsPortInfoOptTable,
       "eltMesIssDcsPortInfoOptEntry": eltMesIssDcsPortInfoOptEntry,
       "eltMesIssDcsPortInfoOptProtocolType": eltMesIssDcsPortInfoOptProtocolType,
       "eltMesIssDcsPortInfoOptEnabled": eltMesIssDcsPortInfoOptEnabled,
       "eltMesIssDcsVlanInfoOptTable": eltMesIssDcsVlanInfoOptTable,
       "eltMesIssDcsVlanInfoOptEntry": eltMesIssDcsVlanInfoOptEntry,
       "eltMesIssDcsVlanInfoOptVlanId": eltMesIssDcsVlanInfoOptVlanId,
       "eltMesIssDcsVlanInfoOptProtocolType": eltMesIssDcsVlanInfoOptProtocolType,
       "eltMesIssDcsVlanInfoOptEnabled": eltMesIssDcsVlanInfoOptEnabled,
       "eltMesIssDcsVlanInfoOptRowStatus": eltMesIssDcsVlanInfoOptRowStatus}
)
