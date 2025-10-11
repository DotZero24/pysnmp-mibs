# SNMP MIB module (INFINERA-PM-GROUPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-GROUPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:05 2025
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

(HCPerfIntervalCount,) = mibBuilder.importSymbols(
    "HC-PerfHist-TC-MIB",
    "HCPerfIntervalCount")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(perfMon,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "perfMon")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

groupTpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 9)
)
if mibBuilder.loadTexts:
    groupTpPmMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GroupTpPmRealTable_Object = MibTable
groupTpPmRealTable = _GroupTpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 9, 1)
)
if mibBuilder.loadTexts:
    groupTpPmRealTable.setStatus("current")
_GroupTpPmRealEntry_Object = MibTableRow
groupTpPmRealEntry = _GroupTpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 9, 1, 1)
)
groupTpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    groupTpPmRealEntry.setStatus("current")
_GroupTpPmRealDtpRxCV_Type = Counter64
_GroupTpPmRealDtpRxCV_Object = MibTableColumn
groupTpPmRealDtpRxCV = _GroupTpPmRealDtpRxCV_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 9, 1, 1, 1),
    _GroupTpPmRealDtpRxCV_Type()
)
groupTpPmRealDtpRxCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupTpPmRealDtpRxCV.setStatus("current")
_GroupTpPmRealDtpRxES_Type = Integer32
_GroupTpPmRealDtpRxES_Object = MibTableColumn
groupTpPmRealDtpRxES = _GroupTpPmRealDtpRxES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 9, 1, 1, 2),
    _GroupTpPmRealDtpRxES_Type()
)
groupTpPmRealDtpRxES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupTpPmRealDtpRxES.setStatus("current")
_GroupTpPmRealDtpRxSES_Type = Integer32
_GroupTpPmRealDtpRxSES_Object = MibTableColumn
groupTpPmRealDtpRxSES = _GroupTpPmRealDtpRxSES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 9, 1, 1, 3),
    _GroupTpPmRealDtpRxSES_Type()
)
groupTpPmRealDtpRxSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupTpPmRealDtpRxSES.setStatus("current")
_GroupTpPmRealDtpRxUAS_Type = Integer32
_GroupTpPmRealDtpRxUAS_Object = MibTableColumn
groupTpPmRealDtpRxUAS = _GroupTpPmRealDtpRxUAS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 9, 1, 1, 4),
    _GroupTpPmRealDtpRxUAS_Type()
)
groupTpPmRealDtpRxUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupTpPmRealDtpRxUAS.setStatus("current")
_GroupTpPmRealDtpTxCV_Type = Counter64
_GroupTpPmRealDtpTxCV_Object = MibTableColumn
groupTpPmRealDtpTxCV = _GroupTpPmRealDtpTxCV_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 9, 1, 1, 5),
    _GroupTpPmRealDtpTxCV_Type()
)
groupTpPmRealDtpTxCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupTpPmRealDtpTxCV.setStatus("current")
_GroupTpPmRealDtpTxES_Type = Integer32
_GroupTpPmRealDtpTxES_Object = MibTableColumn
groupTpPmRealDtpTxES = _GroupTpPmRealDtpTxES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 9, 1, 1, 6),
    _GroupTpPmRealDtpTxES_Type()
)
groupTpPmRealDtpTxES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupTpPmRealDtpTxES.setStatus("current")
_GroupTpPmRealDtpTxSES_Type = Integer32
_GroupTpPmRealDtpTxSES_Object = MibTableColumn
groupTpPmRealDtpTxSES = _GroupTpPmRealDtpTxSES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 9, 1, 1, 7),
    _GroupTpPmRealDtpTxSES_Type()
)
groupTpPmRealDtpTxSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupTpPmRealDtpTxSES.setStatus("current")
_GroupTpPmRealDtpTxUAS_Type = Integer32
_GroupTpPmRealDtpTxUAS_Object = MibTableColumn
groupTpPmRealDtpTxUAS = _GroupTpPmRealDtpTxUAS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 9, 1, 1, 8),
    _GroupTpPmRealDtpTxUAS_Type()
)
groupTpPmRealDtpTxUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupTpPmRealDtpTxUAS.setStatus("current")
_GroupTpPmTable_Object = MibTable
groupTpPmTable = _GroupTpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 9, 2)
)
if mibBuilder.loadTexts:
    groupTpPmTable.setStatus("current")
_GroupTpPmEntry_Object = MibTableRow
groupTpPmEntry = _GroupTpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 9, 2, 1)
)
groupTpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-GROUPTP-MIB", "groupTpPmSampleDuration"),
    (0, "INFINERA-PM-GROUPTP-MIB", "groupTpPmTimestamp"),
)
if mibBuilder.loadTexts:
    groupTpPmEntry.setStatus("current")


class _GroupTpPmTimestamp_Type(Integer32):
    """Custom type groupTpPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_GroupTpPmTimestamp_Type.__name__ = "Integer32"
_GroupTpPmTimestamp_Object = MibTableColumn
groupTpPmTimestamp = _GroupTpPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 9, 2, 1, 1),
    _GroupTpPmTimestamp_Type()
)
groupTpPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    groupTpPmTimestamp.setStatus("current")


class _GroupTpPmSampleDuration_Type(Integer32):
    """Custom type groupTpPmSampleDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fifteenMinutes", 1),
          ("day", 2))
    )


_GroupTpPmSampleDuration_Type.__name__ = "Integer32"
_GroupTpPmSampleDuration_Object = MibTableColumn
groupTpPmSampleDuration = _GroupTpPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 9, 2, 1, 2),
    _GroupTpPmSampleDuration_Type()
)
groupTpPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    groupTpPmSampleDuration.setStatus("current")
_GroupTpPmValidity_Type = TruthValue
_GroupTpPmValidity_Object = MibTableColumn
groupTpPmValidity = _GroupTpPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 9, 2, 1, 3),
    _GroupTpPmValidity_Type()
)
groupTpPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupTpPmValidity.setStatus("current")
_GroupTpPmDtpRxCV_Type = HCPerfIntervalCount
_GroupTpPmDtpRxCV_Object = MibTableColumn
groupTpPmDtpRxCV = _GroupTpPmDtpRxCV_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 9, 2, 1, 4),
    _GroupTpPmDtpRxCV_Type()
)
groupTpPmDtpRxCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupTpPmDtpRxCV.setStatus("current")
_GroupTpPmDtpRxES_Type = Integer32
_GroupTpPmDtpRxES_Object = MibTableColumn
groupTpPmDtpRxES = _GroupTpPmDtpRxES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 9, 2, 1, 5),
    _GroupTpPmDtpRxES_Type()
)
groupTpPmDtpRxES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupTpPmDtpRxES.setStatus("current")
_GroupTpPmDtpRxSES_Type = Integer32
_GroupTpPmDtpRxSES_Object = MibTableColumn
groupTpPmDtpRxSES = _GroupTpPmDtpRxSES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 9, 2, 1, 6),
    _GroupTpPmDtpRxSES_Type()
)
groupTpPmDtpRxSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupTpPmDtpRxSES.setStatus("current")
_GroupTpPmDtpRxUAS_Type = Integer32
_GroupTpPmDtpRxUAS_Object = MibTableColumn
groupTpPmDtpRxUAS = _GroupTpPmDtpRxUAS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 9, 2, 1, 7),
    _GroupTpPmDtpRxUAS_Type()
)
groupTpPmDtpRxUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupTpPmDtpRxUAS.setStatus("current")
_GroupTpPmDtpTxCV_Type = HCPerfIntervalCount
_GroupTpPmDtpTxCV_Object = MibTableColumn
groupTpPmDtpTxCV = _GroupTpPmDtpTxCV_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 9, 2, 1, 8),
    _GroupTpPmDtpTxCV_Type()
)
groupTpPmDtpTxCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupTpPmDtpTxCV.setStatus("current")
_GroupTpPmDtpTxES_Type = Integer32
_GroupTpPmDtpTxES_Object = MibTableColumn
groupTpPmDtpTxES = _GroupTpPmDtpTxES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 9, 2, 1, 9),
    _GroupTpPmDtpTxES_Type()
)
groupTpPmDtpTxES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupTpPmDtpTxES.setStatus("current")
_GroupTpPmDtpTxSES_Type = Integer32
_GroupTpPmDtpTxSES_Object = MibTableColumn
groupTpPmDtpTxSES = _GroupTpPmDtpTxSES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 9, 2, 1, 10),
    _GroupTpPmDtpTxSES_Type()
)
groupTpPmDtpTxSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupTpPmDtpTxSES.setStatus("current")
_GroupTpPmDtpTxUAS_Type = Integer32
_GroupTpPmDtpTxUAS_Object = MibTableColumn
groupTpPmDtpTxUAS = _GroupTpPmDtpTxUAS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 9, 2, 1, 11),
    _GroupTpPmDtpTxUAS_Type()
)
groupTpPmDtpTxUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupTpPmDtpTxUAS.setStatus("current")
_GroupTpPmConformance_ObjectIdentity = ObjectIdentity
groupTpPmConformance = _GroupTpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 9, 3)
)
_GroupTpPmCompliances_ObjectIdentity = ObjectIdentity
groupTpPmCompliances = _GroupTpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 9, 3, 1)
)
_GroupTpPmGroups_ObjectIdentity = ObjectIdentity
groupTpPmGroups = _GroupTpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 9, 3, 2)
)

# Managed Objects groups

groupTpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 9, 3, 2, 1)
)
groupTpPmGroup.setObjects(
      *(("INFINERA-PM-GROUPTP-MIB", "groupTpPmValidity"),
        ("INFINERA-PM-GROUPTP-MIB", "groupTpPmDtpRxCV"),
        ("INFINERA-PM-GROUPTP-MIB", "groupTpPmDtpRxES"),
        ("INFINERA-PM-GROUPTP-MIB", "groupTpPmDtpRxSES"),
        ("INFINERA-PM-GROUPTP-MIB", "groupTpPmDtpRxUAS"),
        ("INFINERA-PM-GROUPTP-MIB", "groupTpPmDtpTxCV"),
        ("INFINERA-PM-GROUPTP-MIB", "groupTpPmDtpTxES"),
        ("INFINERA-PM-GROUPTP-MIB", "groupTpPmDtpTxSES"),
        ("INFINERA-PM-GROUPTP-MIB", "groupTpPmDtpTxUAS"))
)
if mibBuilder.loadTexts:
    groupTpPmGroup.setStatus("current")

groupTpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 9, 3, 2, 2)
)
groupTpPmRealGroup.setObjects(
      *(("INFINERA-PM-GROUPTP-MIB", "groupTpPmRealDtpRxCV"),
        ("INFINERA-PM-GROUPTP-MIB", "groupTpPmRealDtpRxES"),
        ("INFINERA-PM-GROUPTP-MIB", "groupTpPmRealDtpRxSES"),
        ("INFINERA-PM-GROUPTP-MIB", "groupTpPmRealDtpRxUAS"),
        ("INFINERA-PM-GROUPTP-MIB", "groupTpPmRealDtpTxCV"),
        ("INFINERA-PM-GROUPTP-MIB", "groupTpPmRealDtpTxES"),
        ("INFINERA-PM-GROUPTP-MIB", "groupTpPmRealDtpTxSES"),
        ("INFINERA-PM-GROUPTP-MIB", "groupTpPmRealDtpTxUAS"))
)
if mibBuilder.loadTexts:
    groupTpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

groupTpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 9, 3, 1, 1)
)
groupTpPmCompliance.setObjects(
    ("INFINERA-PM-GROUPTP-MIB", "groupTpPmGroup")
)
if mibBuilder.loadTexts:
    groupTpPmCompliance.setStatus(
        "current"
    )

groupTpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 9, 3, 1, 2)
)
groupTpPmRealCompliance.setObjects(
    ("INFINERA-PM-GROUPTP-MIB", "groupTpPmRealGroup")
)
if mibBuilder.loadTexts:
    groupTpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-GROUPTP-MIB",
    **{"groupTpPmMIB": groupTpPmMIB,
       "groupTpPmRealTable": groupTpPmRealTable,
       "groupTpPmRealEntry": groupTpPmRealEntry,
       "groupTpPmRealDtpRxCV": groupTpPmRealDtpRxCV,
       "groupTpPmRealDtpRxES": groupTpPmRealDtpRxES,
       "groupTpPmRealDtpRxSES": groupTpPmRealDtpRxSES,
       "groupTpPmRealDtpRxUAS": groupTpPmRealDtpRxUAS,
       "groupTpPmRealDtpTxCV": groupTpPmRealDtpTxCV,
       "groupTpPmRealDtpTxES": groupTpPmRealDtpTxES,
       "groupTpPmRealDtpTxSES": groupTpPmRealDtpTxSES,
       "groupTpPmRealDtpTxUAS": groupTpPmRealDtpTxUAS,
       "groupTpPmTable": groupTpPmTable,
       "groupTpPmEntry": groupTpPmEntry,
       "groupTpPmTimestamp": groupTpPmTimestamp,
       "groupTpPmSampleDuration": groupTpPmSampleDuration,
       "groupTpPmValidity": groupTpPmValidity,
       "groupTpPmDtpRxCV": groupTpPmDtpRxCV,
       "groupTpPmDtpRxES": groupTpPmDtpRxES,
       "groupTpPmDtpRxSES": groupTpPmDtpRxSES,
       "groupTpPmDtpRxUAS": groupTpPmDtpRxUAS,
       "groupTpPmDtpTxCV": groupTpPmDtpTxCV,
       "groupTpPmDtpTxES": groupTpPmDtpTxES,
       "groupTpPmDtpTxSES": groupTpPmDtpTxSES,
       "groupTpPmDtpTxUAS": groupTpPmDtpTxUAS,
       "groupTpPmConformance": groupTpPmConformance,
       "groupTpPmCompliances": groupTpPmCompliances,
       "groupTpPmCompliance": groupTpPmCompliance,
       "groupTpPmRealCompliance": groupTpPmRealCompliance,
       "groupTpPmGroups": groupTpPmGroups,
       "groupTpPmGroup": groupTpPmGroup,
       "groupTpPmRealGroup": groupTpPmRealGroup}
)
