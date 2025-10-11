# SNMP MIB module (CAMBIUM-NETWORKS-CABLE-DIAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/cambium/CAMBIUM-NETWORKS-CABLE-DIAG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:07:44 2025
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
 enterprises,
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
    "enterprises",
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

cnCableDiagMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 24, 7)
)
if mibBuilder.loadTexts:
    cnCableDiagMib.setRevisions(
        ("2020-11-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CnCableDiagObjects_ObjectIdentity = ObjectIdentity
cnCableDiagObjects = _CnCableDiagObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 24, 7, 0)
)
_CnCableDiagPortTable_Object = MibTable
cnCableDiagPortTable = _CnCableDiagPortTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 7, 0, 1)
)
if mibBuilder.loadTexts:
    cnCableDiagPortTable.setStatus("current")
_CnCableDiagPortEntry_Object = MibTableRow
cnCableDiagPortEntry = _CnCableDiagPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 7, 0, 1, 1)
)
cnCableDiagPortEntry.setIndexNames(
    (0, "CAMBIUM-NETWORKS-CABLE-DIAG-MIB", "cnCableDiagPortIndex"),
)
if mibBuilder.loadTexts:
    cnCableDiagPortEntry.setStatus("current")


class _CnCableDiagPortIndex_Type(Integer32):
    """Custom type cnCableDiagPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CnCableDiagPortIndex_Type.__name__ = "Integer32"
_CnCableDiagPortIndex_Object = MibTableColumn
cnCableDiagPortIndex = _CnCableDiagPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 7, 0, 1, 1, 1),
    _CnCableDiagPortIndex_Type()
)
cnCableDiagPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnCableDiagPortIndex.setStatus("current")


class _CnCableDiagTestResultPair1_Type(Integer32):
    """Custom type cnCableDiagTestResultPair1 based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("pair-ok", 1),
          ("pair-open", 2),
          ("same-pair-short", 3),
          ("cross-pair-short", 4),
          ("pair-busy", 5),
          ("test-in-progress", 6),
          ("test-failed", 7),
          ("no-test", 8))
    )


_CnCableDiagTestResultPair1_Type.__name__ = "Integer32"
_CnCableDiagTestResultPair1_Object = MibTableColumn
cnCableDiagTestResultPair1 = _CnCableDiagTestResultPair1_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 7, 0, 1, 1, 2),
    _CnCableDiagTestResultPair1_Type()
)
cnCableDiagTestResultPair1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCableDiagTestResultPair1.setStatus("current")


class _CnCableDiagTestResultPair2_Type(Integer32):
    """Custom type cnCableDiagTestResultPair2 based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("pair-ok", 1),
          ("pair-open", 2),
          ("same-pair-short", 3),
          ("cross-pair-short", 4),
          ("pair-busy", 5),
          ("test-in-progress", 6),
          ("test-failed", 7),
          ("no-test", 8))
    )


_CnCableDiagTestResultPair2_Type.__name__ = "Integer32"
_CnCableDiagTestResultPair2_Object = MibTableColumn
cnCableDiagTestResultPair2 = _CnCableDiagTestResultPair2_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 7, 0, 1, 1, 3),
    _CnCableDiagTestResultPair2_Type()
)
cnCableDiagTestResultPair2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCableDiagTestResultPair2.setStatus("current")


class _CnCableDiagTestResultPair3_Type(Integer32):
    """Custom type cnCableDiagTestResultPair3 based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("pair-ok", 1),
          ("pair-open", 2),
          ("same-pair-short", 3),
          ("cross-pair-short", 4),
          ("pair-busy", 5),
          ("test-in-progress", 6),
          ("test-failed", 7),
          ("no-test", 8))
    )


_CnCableDiagTestResultPair3_Type.__name__ = "Integer32"
_CnCableDiagTestResultPair3_Object = MibTableColumn
cnCableDiagTestResultPair3 = _CnCableDiagTestResultPair3_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 7, 0, 1, 1, 4),
    _CnCableDiagTestResultPair3_Type()
)
cnCableDiagTestResultPair3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCableDiagTestResultPair3.setStatus("current")


class _CnCableDiagTestResultPair4_Type(Integer32):
    """Custom type cnCableDiagTestResultPair4 based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("pair-ok", 1),
          ("pair-open", 2),
          ("same-pair-short", 3),
          ("cross-pair-short", 4),
          ("pair-busy", 5),
          ("test-in-progress", 6),
          ("test-failed", 7),
          ("no-test", 8))
    )


_CnCableDiagTestResultPair4_Type.__name__ = "Integer32"
_CnCableDiagTestResultPair4_Object = MibTableColumn
cnCableDiagTestResultPair4 = _CnCableDiagTestResultPair4_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 7, 0, 1, 1, 5),
    _CnCableDiagTestResultPair4_Type()
)
cnCableDiagTestResultPair4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCableDiagTestResultPair4.setStatus("current")


class _CnCableDiagFaultLengthPair1_Type(Integer32):
    """Custom type cnCableDiagFaultLengthPair1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CnCableDiagFaultLengthPair1_Type.__name__ = "Integer32"
_CnCableDiagFaultLengthPair1_Object = MibTableColumn
cnCableDiagFaultLengthPair1 = _CnCableDiagFaultLengthPair1_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 7, 0, 1, 1, 6),
    _CnCableDiagFaultLengthPair1_Type()
)
cnCableDiagFaultLengthPair1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCableDiagFaultLengthPair1.setStatus("current")


class _CnCableDiagFaultLengthPair2_Type(Integer32):
    """Custom type cnCableDiagFaultLengthPair2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CnCableDiagFaultLengthPair2_Type.__name__ = "Integer32"
_CnCableDiagFaultLengthPair2_Object = MibTableColumn
cnCableDiagFaultLengthPair2 = _CnCableDiagFaultLengthPair2_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 7, 0, 1, 1, 7),
    _CnCableDiagFaultLengthPair2_Type()
)
cnCableDiagFaultLengthPair2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCableDiagFaultLengthPair2.setStatus("current")


class _CnCableDiagFaultLengthPair3_Type(Integer32):
    """Custom type cnCableDiagFaultLengthPair3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CnCableDiagFaultLengthPair3_Type.__name__ = "Integer32"
_CnCableDiagFaultLengthPair3_Object = MibTableColumn
cnCableDiagFaultLengthPair3 = _CnCableDiagFaultLengthPair3_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 7, 0, 1, 1, 8),
    _CnCableDiagFaultLengthPair3_Type()
)
cnCableDiagFaultLengthPair3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCableDiagFaultLengthPair3.setStatus("current")


class _CnCableDiagFaultLengthPair4_Type(Integer32):
    """Custom type cnCableDiagFaultLengthPair4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CnCableDiagFaultLengthPair4_Type.__name__ = "Integer32"
_CnCableDiagFaultLengthPair4_Object = MibTableColumn
cnCableDiagFaultLengthPair4 = _CnCableDiagFaultLengthPair4_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 7, 0, 1, 1, 9),
    _CnCableDiagFaultLengthPair4_Type()
)
cnCableDiagFaultLengthPair4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCableDiagFaultLengthPair4.setStatus("current")


class _CnCableDiagTimeStamp_Type(Integer32):
    """Custom type cnCableDiagTimeStamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CnCableDiagTimeStamp_Type.__name__ = "Integer32"
_CnCableDiagTimeStamp_Object = MibTableColumn
cnCableDiagTimeStamp = _CnCableDiagTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 7, 0, 1, 1, 10),
    _CnCableDiagTimeStamp_Type()
)
cnCableDiagTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCableDiagTimeStamp.setStatus("current")


class _CnCableDiagStartTest_Type(Integer32):
    """Custom type cnCableDiagStartTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start-test", 1),
          ("default-value", 2))
    )


_CnCableDiagStartTest_Type.__name__ = "Integer32"
_CnCableDiagStartTest_Object = MibTableColumn
cnCableDiagStartTest = _CnCableDiagStartTest_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 7, 0, 1, 1, 11),
    _CnCableDiagStartTest_Type()
)
cnCableDiagStartTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnCableDiagStartTest.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAMBIUM-NETWORKS-CABLE-DIAG-MIB",
    **{"cnCableDiagMib": cnCableDiagMib,
       "cnCableDiagObjects": cnCableDiagObjects,
       "cnCableDiagPortTable": cnCableDiagPortTable,
       "cnCableDiagPortEntry": cnCableDiagPortEntry,
       "cnCableDiagPortIndex": cnCableDiagPortIndex,
       "cnCableDiagTestResultPair1": cnCableDiagTestResultPair1,
       "cnCableDiagTestResultPair2": cnCableDiagTestResultPair2,
       "cnCableDiagTestResultPair3": cnCableDiagTestResultPair3,
       "cnCableDiagTestResultPair4": cnCableDiagTestResultPair4,
       "cnCableDiagFaultLengthPair1": cnCableDiagFaultLengthPair1,
       "cnCableDiagFaultLengthPair2": cnCableDiagFaultLengthPair2,
       "cnCableDiagFaultLengthPair3": cnCableDiagFaultLengthPair3,
       "cnCableDiagFaultLengthPair4": cnCableDiagFaultLengthPair4,
       "cnCableDiagTimeStamp": cnCableDiagTimeStamp,
       "cnCableDiagStartTest": cnCableDiagStartTest}
)
