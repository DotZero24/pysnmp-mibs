# SNMP MIB module (G6-SCRIPTDATA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/microsens/G6-SCRIPTDATA-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:15 2025
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

(g6,) = mibBuilder.importSymbols(
    "MICROSENS-G6-MIB",
    "g6")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

management = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3)
)
if mibBuilder.loadTexts:
    management.setRevisions(
        ("2018-02-12 16:19",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Scriptdata_ObjectIdentity = ObjectIdentity
scriptdata = _Scriptdata_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 77)
)
_ParameterTable_Object = MibTable
parameterTable = _ParameterTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 77, 1)
)
if mibBuilder.loadTexts:
    parameterTable.setStatus("current")
_ParameterEntry_Object = MibTableRow
parameterEntry = _ParameterEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 77, 1, 1)
)
parameterEntry.setIndexNames(
    (0, "G6-SCRIPTDATA-MIB", "parameterIndex"),
)
if mibBuilder.loadTexts:
    parameterEntry.setStatus("current")


class _ParameterIndex_Type(Integer32):
    """Custom type parameterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_ParameterIndex_Type.__name__ = "Integer32"
_ParameterIndex_Object = MibTableColumn
parameterIndex = _ParameterIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 77, 1, 1, 1),
    _ParameterIndex_Type()
)
parameterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    parameterIndex.setStatus("current")
_ParameterName_Type = DisplayString
_ParameterName_Object = MibTableColumn
parameterName = _ParameterName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 77, 1, 1, 2),
    _ParameterName_Type()
)
parameterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parameterName.setStatus("current")
_ParameterValue_Type = DisplayString
_ParameterValue_Object = MibTableColumn
parameterValue = _ParameterValue_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 77, 1, 1, 3),
    _ParameterValue_Type()
)
parameterValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parameterValue.setStatus("current")
_VariablesTable_Object = MibTable
variablesTable = _VariablesTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 77, 100)
)
if mibBuilder.loadTexts:
    variablesTable.setStatus("current")
_VariablesEntry_Object = MibTableRow
variablesEntry = _VariablesEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 77, 100, 1)
)
variablesEntry.setIndexNames(
    (0, "G6-SCRIPTDATA-MIB", "variablesIndex"),
)
if mibBuilder.loadTexts:
    variablesEntry.setStatus("current")


class _VariablesIndex_Type(Integer32):
    """Custom type variablesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_VariablesIndex_Type.__name__ = "Integer32"
_VariablesIndex_Object = MibTableColumn
variablesIndex = _VariablesIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 77, 100, 1, 1),
    _VariablesIndex_Type()
)
variablesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    variablesIndex.setStatus("current")
_VariablesName_Type = DisplayString
_VariablesName_Object = MibTableColumn
variablesName = _VariablesName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 77, 100, 1, 2),
    _VariablesName_Type()
)
variablesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    variablesName.setStatus("current")
_VariablesValue_Type = DisplayString
_VariablesValue_Object = MibTableColumn
variablesValue = _VariablesValue_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 77, 100, 1, 3),
    _VariablesValue_Type()
)
variablesValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    variablesValue.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "G6-SCRIPTDATA-MIB",
    **{"management": management,
       "scriptdata": scriptdata,
       "parameterTable": parameterTable,
       "parameterEntry": parameterEntry,
       "parameterIndex": parameterIndex,
       "parameterName": parameterName,
       "parameterValue": parameterValue,
       "variablesTable": variablesTable,
       "variablesEntry": variablesEntry,
       "variablesIndex": variablesIndex,
       "variablesName": variablesName,
       "variablesValue": variablesValue}
)
