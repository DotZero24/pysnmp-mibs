# SNMP MIB module (ADTRAN-PERFORMANCE-MONITORING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-PERFORMANCE-MONITORING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:32:33 2025
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

(adGenPerformanceMonitoring,
 adGenPerformanceMonitoringID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenPerformanceMonitoring",
    "adGenPerformanceMonitoringID")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

adGenPerformanceMonitoringMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 23, 1)
)
if mibBuilder.loadTexts:
    adGenPerformanceMonitoringMIB.setRevisions(
        ("2012-02-06 00:00",
         "2010-03-31 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AdGenPmAttributeName(TextualConvention, OctetString):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class AdGenPmFunctionName(TextualConvention, OctetString):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



# MIB Managed Objects in the order of their OIDs

_AdGenPmStats_ObjectIdentity = ObjectIdentity
adGenPmStats = _AdGenPmStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 23, 1)
)
_AdGenPm15MinCurrentIntervalStatsTable_Object = MibTable
adGenPm15MinCurrentIntervalStatsTable = _AdGenPm15MinCurrentIntervalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 23, 1, 1)
)
if mibBuilder.loadTexts:
    adGenPm15MinCurrentIntervalStatsTable.setStatus("current")
_AdGenPm15MinCurrentIntervalStatsEntry_Object = MibTableRow
adGenPm15MinCurrentIntervalStatsEntry = _AdGenPm15MinCurrentIntervalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 23, 1, 1, 1)
)
adGenPm15MinCurrentIntervalStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-PERFORMANCE-MONITORING-MIB", "adGenPm15MinCurrentIntervalStatsAttribute"),
)
if mibBuilder.loadTexts:
    adGenPm15MinCurrentIntervalStatsEntry.setStatus("current")
_AdGenPm15MinCurrentIntervalStatsAttribute_Type = AdGenPmAttributeName
_AdGenPm15MinCurrentIntervalStatsAttribute_Object = MibTableColumn
adGenPm15MinCurrentIntervalStatsAttribute = _AdGenPm15MinCurrentIntervalStatsAttribute_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 23, 1, 1, 1, 1),
    _AdGenPm15MinCurrentIntervalStatsAttribute_Type()
)
adGenPm15MinCurrentIntervalStatsAttribute.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenPm15MinCurrentIntervalStatsAttribute.setStatus("current")
_AdGenPm15MinCurrentIntervalStatsValue_Type = Counter32
_AdGenPm15MinCurrentIntervalStatsValue_Object = MibTableColumn
adGenPm15MinCurrentIntervalStatsValue = _AdGenPm15MinCurrentIntervalStatsValue_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 23, 1, 1, 1, 2),
    _AdGenPm15MinCurrentIntervalStatsValue_Type()
)
adGenPm15MinCurrentIntervalStatsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPm15MinCurrentIntervalStatsValue.setStatus("current")
_AdGenPm15MinCurrentIntervalStatsHCValue_Type = Counter64
_AdGenPm15MinCurrentIntervalStatsHCValue_Object = MibTableColumn
adGenPm15MinCurrentIntervalStatsHCValue = _AdGenPm15MinCurrentIntervalStatsHCValue_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 23, 1, 1, 1, 3),
    _AdGenPm15MinCurrentIntervalStatsHCValue_Type()
)
adGenPm15MinCurrentIntervalStatsHCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPm15MinCurrentIntervalStatsHCValue.setStatus("current")
_AdGenPm15MinCurrentIntervalStatsValid_Type = TruthValue
_AdGenPm15MinCurrentIntervalStatsValid_Object = MibTableColumn
adGenPm15MinCurrentIntervalStatsValid = _AdGenPm15MinCurrentIntervalStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 23, 1, 1, 1, 4),
    _AdGenPm15MinCurrentIntervalStatsValid_Type()
)
adGenPm15MinCurrentIntervalStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPm15MinCurrentIntervalStatsValid.setStatus("current")
_AdGenPm15MinIntervalStatsTable_Object = MibTable
adGenPm15MinIntervalStatsTable = _AdGenPm15MinIntervalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 23, 1, 2)
)
if mibBuilder.loadTexts:
    adGenPm15MinIntervalStatsTable.setStatus("current")
_AdGenPm15MinIntervalStatsEntry_Object = MibTableRow
adGenPm15MinIntervalStatsEntry = _AdGenPm15MinIntervalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 23, 1, 2, 1)
)
adGenPm15MinIntervalStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-PERFORMANCE-MONITORING-MIB", "adGenPm15MinIntervalStatsAttribute"),
    (0, "ADTRAN-PERFORMANCE-MONITORING-MIB", "adGenPm15MinIntervalStatsInterval"),
)
if mibBuilder.loadTexts:
    adGenPm15MinIntervalStatsEntry.setStatus("current")


class _AdGenPm15MinIntervalStatsInterval_Type(Integer32):
    """Custom type adGenPm15MinIntervalStatsInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AdGenPm15MinIntervalStatsInterval_Type.__name__ = "Integer32"
_AdGenPm15MinIntervalStatsInterval_Object = MibTableColumn
adGenPm15MinIntervalStatsInterval = _AdGenPm15MinIntervalStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 23, 1, 2, 1, 1),
    _AdGenPm15MinIntervalStatsInterval_Type()
)
adGenPm15MinIntervalStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenPm15MinIntervalStatsInterval.setStatus("current")
_AdGenPm15MinIntervalStatsAttribute_Type = AdGenPmAttributeName
_AdGenPm15MinIntervalStatsAttribute_Object = MibTableColumn
adGenPm15MinIntervalStatsAttribute = _AdGenPm15MinIntervalStatsAttribute_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 23, 1, 2, 1, 2),
    _AdGenPm15MinIntervalStatsAttribute_Type()
)
adGenPm15MinIntervalStatsAttribute.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenPm15MinIntervalStatsAttribute.setStatus("current")
_AdGenPm15MinIntervalStatsValue_Type = Counter32
_AdGenPm15MinIntervalStatsValue_Object = MibTableColumn
adGenPm15MinIntervalStatsValue = _AdGenPm15MinIntervalStatsValue_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 23, 1, 2, 1, 3),
    _AdGenPm15MinIntervalStatsValue_Type()
)
adGenPm15MinIntervalStatsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPm15MinIntervalStatsValue.setStatus("current")
_AdGenPm15MinIntervalStatsHCValue_Type = Counter64
_AdGenPm15MinIntervalStatsHCValue_Object = MibTableColumn
adGenPm15MinIntervalStatsHCValue = _AdGenPm15MinIntervalStatsHCValue_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 23, 1, 2, 1, 4),
    _AdGenPm15MinIntervalStatsHCValue_Type()
)
adGenPm15MinIntervalStatsHCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPm15MinIntervalStatsHCValue.setStatus("current")
_AdGenPm15MinIntervalStatsValid_Type = TruthValue
_AdGenPm15MinIntervalStatsValid_Object = MibTableColumn
adGenPm15MinIntervalStatsValid = _AdGenPm15MinIntervalStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 23, 1, 2, 1, 5),
    _AdGenPm15MinIntervalStatsValid_Type()
)
adGenPm15MinIntervalStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPm15MinIntervalStatsValid.setStatus("current")
_AdGenPm24HrCurrentStatsTable_Object = MibTable
adGenPm24HrCurrentStatsTable = _AdGenPm24HrCurrentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 23, 1, 3)
)
if mibBuilder.loadTexts:
    adGenPm24HrCurrentStatsTable.setStatus("current")
_AdGenPm24HrCurrentStatsEntry_Object = MibTableRow
adGenPm24HrCurrentStatsEntry = _AdGenPm24HrCurrentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 23, 1, 3, 1)
)
adGenPm24HrCurrentStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-PERFORMANCE-MONITORING-MIB", "adGenPm24HrCurrentStatsAttribute"),
)
if mibBuilder.loadTexts:
    adGenPm24HrCurrentStatsEntry.setStatus("current")
_AdGenPm24HrCurrentStatsAttribute_Type = AdGenPmAttributeName
_AdGenPm24HrCurrentStatsAttribute_Object = MibTableColumn
adGenPm24HrCurrentStatsAttribute = _AdGenPm24HrCurrentStatsAttribute_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 23, 1, 3, 1, 1),
    _AdGenPm24HrCurrentStatsAttribute_Type()
)
adGenPm24HrCurrentStatsAttribute.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenPm24HrCurrentStatsAttribute.setStatus("current")
_AdGenPm24HrCurrentStatsValue_Type = Counter32
_AdGenPm24HrCurrentStatsValue_Object = MibTableColumn
adGenPm24HrCurrentStatsValue = _AdGenPm24HrCurrentStatsValue_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 23, 1, 3, 1, 2),
    _AdGenPm24HrCurrentStatsValue_Type()
)
adGenPm24HrCurrentStatsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPm24HrCurrentStatsValue.setStatus("current")
_AdGenPm24HrCurrentStatsHCValue_Type = Counter64
_AdGenPm24HrCurrentStatsHCValue_Object = MibTableColumn
adGenPm24HrCurrentStatsHCValue = _AdGenPm24HrCurrentStatsHCValue_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 23, 1, 3, 1, 3),
    _AdGenPm24HrCurrentStatsHCValue_Type()
)
adGenPm24HrCurrentStatsHCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPm24HrCurrentStatsHCValue.setStatus("current")
_AdGenPm24HrCurrentStatsValid_Type = TruthValue
_AdGenPm24HrCurrentStatsValid_Object = MibTableColumn
adGenPm24HrCurrentStatsValid = _AdGenPm24HrCurrentStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 23, 1, 3, 1, 4),
    _AdGenPm24HrCurrentStatsValid_Type()
)
adGenPm24HrCurrentStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPm24HrCurrentStatsValid.setStatus("current")
_AdGenPm24HrIntervalStatsTable_Object = MibTable
adGenPm24HrIntervalStatsTable = _AdGenPm24HrIntervalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 23, 1, 4)
)
if mibBuilder.loadTexts:
    adGenPm24HrIntervalStatsTable.setStatus("current")
_AdGenPm24HrIntervalStatsEntry_Object = MibTableRow
adGenPm24HrIntervalStatsEntry = _AdGenPm24HrIntervalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 23, 1, 4, 1)
)
adGenPm24HrIntervalStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-PERFORMANCE-MONITORING-MIB", "adGenPm24HrIntervalStatsAttribute"),
    (0, "ADTRAN-PERFORMANCE-MONITORING-MIB", "adGenPm24HrIntervalStatsInterval"),
)
if mibBuilder.loadTexts:
    adGenPm24HrIntervalStatsEntry.setStatus("current")
_AdGenPm24HrIntervalStatsAttribute_Type = AdGenPmAttributeName
_AdGenPm24HrIntervalStatsAttribute_Object = MibTableColumn
adGenPm24HrIntervalStatsAttribute = _AdGenPm24HrIntervalStatsAttribute_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 23, 1, 4, 1, 1),
    _AdGenPm24HrIntervalStatsAttribute_Type()
)
adGenPm24HrIntervalStatsAttribute.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenPm24HrIntervalStatsAttribute.setStatus("current")


class _AdGenPm24HrIntervalStatsInterval_Type(Integer32):
    """Custom type adGenPm24HrIntervalStatsInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AdGenPm24HrIntervalStatsInterval_Type.__name__ = "Integer32"
_AdGenPm24HrIntervalStatsInterval_Object = MibTableColumn
adGenPm24HrIntervalStatsInterval = _AdGenPm24HrIntervalStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 23, 1, 4, 1, 2),
    _AdGenPm24HrIntervalStatsInterval_Type()
)
adGenPm24HrIntervalStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenPm24HrIntervalStatsInterval.setStatus("current")
_AdGenPm24HrIntervalStatsValue_Type = Counter32
_AdGenPm24HrIntervalStatsValue_Object = MibTableColumn
adGenPm24HrIntervalStatsValue = _AdGenPm24HrIntervalStatsValue_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 23, 1, 4, 1, 3),
    _AdGenPm24HrIntervalStatsValue_Type()
)
adGenPm24HrIntervalStatsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPm24HrIntervalStatsValue.setStatus("current")
_AdGenPm24HrIntervalStatsHCValue_Type = Counter64
_AdGenPm24HrIntervalStatsHCValue_Object = MibTableColumn
adGenPm24HrIntervalStatsHCValue = _AdGenPm24HrIntervalStatsHCValue_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 23, 1, 4, 1, 4),
    _AdGenPm24HrIntervalStatsHCValue_Type()
)
adGenPm24HrIntervalStatsHCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPm24HrIntervalStatsHCValue.setStatus("current")
_AdGenPm24HrIntervalStatsValid_Type = TruthValue
_AdGenPm24HrIntervalStatsValid_Object = MibTableColumn
adGenPm24HrIntervalStatsValid = _AdGenPm24HrIntervalStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 23, 1, 4, 1, 5),
    _AdGenPm24HrIntervalStatsValid_Type()
)
adGenPm24HrIntervalStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPm24HrIntervalStatsValid.setStatus("current")
_AdGenPmProvisioning_ObjectIdentity = ObjectIdentity
adGenPmProvisioning = _AdGenPmProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 23, 2)
)
_AdGenPmStatsResetTable_Object = MibTable
adGenPmStatsResetTable = _AdGenPmStatsResetTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 23, 2, 1)
)
if mibBuilder.loadTexts:
    adGenPmStatsResetTable.setStatus("current")
_AdGenPmStatsResetEntry_Object = MibTableRow
adGenPmStatsResetEntry = _AdGenPmStatsResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 23, 2, 1, 1)
)
adGenPmStatsResetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-PERFORMANCE-MONITORING-MIB", "adGenPmStatsAttribute"),
)
if mibBuilder.loadTexts:
    adGenPmStatsResetEntry.setStatus("current")
_AdGenPmStatsAttribute_Type = AdGenPmAttributeName
_AdGenPmStatsAttribute_Object = MibTableColumn
adGenPmStatsAttribute = _AdGenPmStatsAttribute_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 23, 2, 1, 1, 1),
    _AdGenPmStatsAttribute_Type()
)
adGenPmStatsAttribute.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenPmStatsAttribute.setStatus("current")
_AdGenPmStats15MinReset_Type = Integer32
_AdGenPmStats15MinReset_Object = MibTableColumn
adGenPmStats15MinReset = _AdGenPmStats15MinReset_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 23, 2, 1, 1, 2),
    _AdGenPmStats15MinReset_Type()
)
adGenPmStats15MinReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPmStats15MinReset.setStatus("current")
_AdGenPmStats24HrReset_Type = Integer32
_AdGenPmStats24HrReset_Object = MibTableColumn
adGenPmStats24HrReset = _AdGenPmStats24HrReset_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 23, 2, 1, 1, 3),
    _AdGenPmStats24HrReset_Type()
)
adGenPmStats24HrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPmStats24HrReset.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-PERFORMANCE-MONITORING-MIB",
    **{"AdGenPmAttributeName": AdGenPmAttributeName,
       "AdGenPmFunctionName": AdGenPmFunctionName,
       "adGenPmStats": adGenPmStats,
       "adGenPm15MinCurrentIntervalStatsTable": adGenPm15MinCurrentIntervalStatsTable,
       "adGenPm15MinCurrentIntervalStatsEntry": adGenPm15MinCurrentIntervalStatsEntry,
       "adGenPm15MinCurrentIntervalStatsAttribute": adGenPm15MinCurrentIntervalStatsAttribute,
       "adGenPm15MinCurrentIntervalStatsValue": adGenPm15MinCurrentIntervalStatsValue,
       "adGenPm15MinCurrentIntervalStatsHCValue": adGenPm15MinCurrentIntervalStatsHCValue,
       "adGenPm15MinCurrentIntervalStatsValid": adGenPm15MinCurrentIntervalStatsValid,
       "adGenPm15MinIntervalStatsTable": adGenPm15MinIntervalStatsTable,
       "adGenPm15MinIntervalStatsEntry": adGenPm15MinIntervalStatsEntry,
       "adGenPm15MinIntervalStatsInterval": adGenPm15MinIntervalStatsInterval,
       "adGenPm15MinIntervalStatsAttribute": adGenPm15MinIntervalStatsAttribute,
       "adGenPm15MinIntervalStatsValue": adGenPm15MinIntervalStatsValue,
       "adGenPm15MinIntervalStatsHCValue": adGenPm15MinIntervalStatsHCValue,
       "adGenPm15MinIntervalStatsValid": adGenPm15MinIntervalStatsValid,
       "adGenPm24HrCurrentStatsTable": adGenPm24HrCurrentStatsTable,
       "adGenPm24HrCurrentStatsEntry": adGenPm24HrCurrentStatsEntry,
       "adGenPm24HrCurrentStatsAttribute": adGenPm24HrCurrentStatsAttribute,
       "adGenPm24HrCurrentStatsValue": adGenPm24HrCurrentStatsValue,
       "adGenPm24HrCurrentStatsHCValue": adGenPm24HrCurrentStatsHCValue,
       "adGenPm24HrCurrentStatsValid": adGenPm24HrCurrentStatsValid,
       "adGenPm24HrIntervalStatsTable": adGenPm24HrIntervalStatsTable,
       "adGenPm24HrIntervalStatsEntry": adGenPm24HrIntervalStatsEntry,
       "adGenPm24HrIntervalStatsAttribute": adGenPm24HrIntervalStatsAttribute,
       "adGenPm24HrIntervalStatsInterval": adGenPm24HrIntervalStatsInterval,
       "adGenPm24HrIntervalStatsValue": adGenPm24HrIntervalStatsValue,
       "adGenPm24HrIntervalStatsHCValue": adGenPm24HrIntervalStatsHCValue,
       "adGenPm24HrIntervalStatsValid": adGenPm24HrIntervalStatsValid,
       "adGenPmProvisioning": adGenPmProvisioning,
       "adGenPmStatsResetTable": adGenPmStatsResetTable,
       "adGenPmStatsResetEntry": adGenPmStatsResetEntry,
       "adGenPmStatsAttribute": adGenPmStatsAttribute,
       "adGenPmStats15MinReset": adGenPmStats15MinReset,
       "adGenPmStats24HrReset": adGenPmStats24HrReset,
       "adGenPerformanceMonitoringMIB": adGenPerformanceMonitoringMIB}
)
