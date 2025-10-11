# SNMP MIB module (INFINERA-PM-DTPCTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-DTPCTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:35 2025
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

dtpCtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 6)
)
if mibBuilder.loadTexts:
    dtpCtpPmMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DtpCtpPmRealTable_Object = MibTable
dtpCtpPmRealTable = _DtpCtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 6, 1)
)
if mibBuilder.loadTexts:
    dtpCtpPmRealTable.setStatus("current")
_DtpCtpPmRealEntry_Object = MibTableRow
dtpCtpPmRealEntry = _DtpCtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 6, 1, 1)
)
dtpCtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dtpCtpPmRealEntry.setStatus("current")
_DtpCtpPmRealDtpRxCV_Type = Counter64
_DtpCtpPmRealDtpRxCV_Object = MibTableColumn
dtpCtpPmRealDtpRxCV = _DtpCtpPmRealDtpRxCV_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 6, 1, 1, 1),
    _DtpCtpPmRealDtpRxCV_Type()
)
dtpCtpPmRealDtpRxCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpCtpPmRealDtpRxCV.setStatus("current")
_DtpCtpPmRealDtpRxES_Type = Integer32
_DtpCtpPmRealDtpRxES_Object = MibTableColumn
dtpCtpPmRealDtpRxES = _DtpCtpPmRealDtpRxES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 6, 1, 1, 2),
    _DtpCtpPmRealDtpRxES_Type()
)
dtpCtpPmRealDtpRxES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpCtpPmRealDtpRxES.setStatus("current")
_DtpCtpPmRealDtpRxSES_Type = Integer32
_DtpCtpPmRealDtpRxSES_Object = MibTableColumn
dtpCtpPmRealDtpRxSES = _DtpCtpPmRealDtpRxSES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 6, 1, 1, 3),
    _DtpCtpPmRealDtpRxSES_Type()
)
dtpCtpPmRealDtpRxSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpCtpPmRealDtpRxSES.setStatus("current")
_DtpCtpPmRealDtpRxUAS_Type = Integer32
_DtpCtpPmRealDtpRxUAS_Object = MibTableColumn
dtpCtpPmRealDtpRxUAS = _DtpCtpPmRealDtpRxUAS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 6, 1, 1, 4),
    _DtpCtpPmRealDtpRxUAS_Type()
)
dtpCtpPmRealDtpRxUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpCtpPmRealDtpRxUAS.setStatus("current")
_DtpCtpPmRealDtpTxCV_Type = Counter64
_DtpCtpPmRealDtpTxCV_Object = MibTableColumn
dtpCtpPmRealDtpTxCV = _DtpCtpPmRealDtpTxCV_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 6, 1, 1, 5),
    _DtpCtpPmRealDtpTxCV_Type()
)
dtpCtpPmRealDtpTxCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpCtpPmRealDtpTxCV.setStatus("current")
_DtpCtpPmRealDtpTxES_Type = Integer32
_DtpCtpPmRealDtpTxES_Object = MibTableColumn
dtpCtpPmRealDtpTxES = _DtpCtpPmRealDtpTxES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 6, 1, 1, 6),
    _DtpCtpPmRealDtpTxES_Type()
)
dtpCtpPmRealDtpTxES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpCtpPmRealDtpTxES.setStatus("current")
_DtpCtpPmRealDtpTxSES_Type = Integer32
_DtpCtpPmRealDtpTxSES_Object = MibTableColumn
dtpCtpPmRealDtpTxSES = _DtpCtpPmRealDtpTxSES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 6, 1, 1, 7),
    _DtpCtpPmRealDtpTxSES_Type()
)
dtpCtpPmRealDtpTxSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpCtpPmRealDtpTxSES.setStatus("current")
_DtpCtpPmRealDtpTxUAS_Type = Integer32
_DtpCtpPmRealDtpTxUAS_Object = MibTableColumn
dtpCtpPmRealDtpTxUAS = _DtpCtpPmRealDtpTxUAS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 6, 1, 1, 8),
    _DtpCtpPmRealDtpTxUAS_Type()
)
dtpCtpPmRealDtpTxUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpCtpPmRealDtpTxUAS.setStatus("current")
_DtpCtpPmRealPrbsSyncErr_Type = Integer32
_DtpCtpPmRealPrbsSyncErr_Object = MibTableColumn
dtpCtpPmRealPrbsSyncErr = _DtpCtpPmRealPrbsSyncErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 6, 1, 1, 9),
    _DtpCtpPmRealPrbsSyncErr_Type()
)
dtpCtpPmRealPrbsSyncErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpCtpPmRealPrbsSyncErr.setStatus("current")
_DtpCtpPmRealPrbsErr_Type = Integer32
_DtpCtpPmRealPrbsErr_Object = MibTableColumn
dtpCtpPmRealPrbsErr = _DtpCtpPmRealPrbsErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 6, 1, 1, 10),
    _DtpCtpPmRealPrbsErr_Type()
)
dtpCtpPmRealPrbsErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpCtpPmRealPrbsErr.setStatus("current")
_DtpCtpPmRealInternalCV_Type = Counter64
_DtpCtpPmRealInternalCV_Object = MibTableColumn
dtpCtpPmRealInternalCV = _DtpCtpPmRealInternalCV_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 6, 1, 1, 11),
    _DtpCtpPmRealInternalCV_Type()
)
dtpCtpPmRealInternalCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpCtpPmRealInternalCV.setStatus("current")
_DtpCtpPmTable_Object = MibTable
dtpCtpPmTable = _DtpCtpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 6, 2)
)
if mibBuilder.loadTexts:
    dtpCtpPmTable.setStatus("current")
_DtpCtpPmEntry_Object = MibTableRow
dtpCtpPmEntry = _DtpCtpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 6, 2, 1)
)
dtpCtpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-DTPCTP-MIB", "dtpCtpPmSampleDuration"),
    (0, "INFINERA-PM-DTPCTP-MIB", "dtpCtpPmTimestamp"),
)
if mibBuilder.loadTexts:
    dtpCtpPmEntry.setStatus("current")


class _DtpCtpPmTimestamp_Type(Integer32):
    """Custom type dtpCtpPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DtpCtpPmTimestamp_Type.__name__ = "Integer32"
_DtpCtpPmTimestamp_Object = MibTableColumn
dtpCtpPmTimestamp = _DtpCtpPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 6, 2, 1, 1),
    _DtpCtpPmTimestamp_Type()
)
dtpCtpPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dtpCtpPmTimestamp.setStatus("current")


class _DtpCtpPmSampleDuration_Type(Integer32):
    """Custom type dtpCtpPmSampleDuration based on Integer32"""
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


_DtpCtpPmSampleDuration_Type.__name__ = "Integer32"
_DtpCtpPmSampleDuration_Object = MibTableColumn
dtpCtpPmSampleDuration = _DtpCtpPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 6, 2, 1, 2),
    _DtpCtpPmSampleDuration_Type()
)
dtpCtpPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dtpCtpPmSampleDuration.setStatus("current")
_DtpCtpPmValidity_Type = TruthValue
_DtpCtpPmValidity_Object = MibTableColumn
dtpCtpPmValidity = _DtpCtpPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 6, 2, 1, 3),
    _DtpCtpPmValidity_Type()
)
dtpCtpPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpCtpPmValidity.setStatus("current")
_DtpCtpPmDtpRxCV_Type = HCPerfIntervalCount
_DtpCtpPmDtpRxCV_Object = MibTableColumn
dtpCtpPmDtpRxCV = _DtpCtpPmDtpRxCV_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 6, 2, 1, 4),
    _DtpCtpPmDtpRxCV_Type()
)
dtpCtpPmDtpRxCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpCtpPmDtpRxCV.setStatus("current")
_DtpCtpPmDtpRxES_Type = Integer32
_DtpCtpPmDtpRxES_Object = MibTableColumn
dtpCtpPmDtpRxES = _DtpCtpPmDtpRxES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 6, 2, 1, 5),
    _DtpCtpPmDtpRxES_Type()
)
dtpCtpPmDtpRxES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpCtpPmDtpRxES.setStatus("current")
_DtpCtpPmDtpRxSES_Type = Integer32
_DtpCtpPmDtpRxSES_Object = MibTableColumn
dtpCtpPmDtpRxSES = _DtpCtpPmDtpRxSES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 6, 2, 1, 6),
    _DtpCtpPmDtpRxSES_Type()
)
dtpCtpPmDtpRxSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpCtpPmDtpRxSES.setStatus("current")
_DtpCtpPmDtpRxUAS_Type = Integer32
_DtpCtpPmDtpRxUAS_Object = MibTableColumn
dtpCtpPmDtpRxUAS = _DtpCtpPmDtpRxUAS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 6, 2, 1, 7),
    _DtpCtpPmDtpRxUAS_Type()
)
dtpCtpPmDtpRxUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpCtpPmDtpRxUAS.setStatus("current")
_DtpCtpPmDtpTxCV_Type = HCPerfIntervalCount
_DtpCtpPmDtpTxCV_Object = MibTableColumn
dtpCtpPmDtpTxCV = _DtpCtpPmDtpTxCV_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 6, 2, 1, 8),
    _DtpCtpPmDtpTxCV_Type()
)
dtpCtpPmDtpTxCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpCtpPmDtpTxCV.setStatus("current")
_DtpCtpPmDtpTxES_Type = Integer32
_DtpCtpPmDtpTxES_Object = MibTableColumn
dtpCtpPmDtpTxES = _DtpCtpPmDtpTxES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 6, 2, 1, 9),
    _DtpCtpPmDtpTxES_Type()
)
dtpCtpPmDtpTxES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpCtpPmDtpTxES.setStatus("current")
_DtpCtpPmDtpTxSES_Type = Integer32
_DtpCtpPmDtpTxSES_Object = MibTableColumn
dtpCtpPmDtpTxSES = _DtpCtpPmDtpTxSES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 6, 2, 1, 10),
    _DtpCtpPmDtpTxSES_Type()
)
dtpCtpPmDtpTxSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpCtpPmDtpTxSES.setStatus("current")
_DtpCtpPmDtpTxUAS_Type = Integer32
_DtpCtpPmDtpTxUAS_Object = MibTableColumn
dtpCtpPmDtpTxUAS = _DtpCtpPmDtpTxUAS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 6, 2, 1, 11),
    _DtpCtpPmDtpTxUAS_Type()
)
dtpCtpPmDtpTxUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpCtpPmDtpTxUAS.setStatus("current")
_DtpCtpPmConformance_ObjectIdentity = ObjectIdentity
dtpCtpPmConformance = _DtpCtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 6, 3)
)
_DtpCtpPmCompliances_ObjectIdentity = ObjectIdentity
dtpCtpPmCompliances = _DtpCtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 6, 3, 1)
)
_DtpCtpPmGroups_ObjectIdentity = ObjectIdentity
dtpCtpPmGroups = _DtpCtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 6, 3, 2)
)

# Managed Objects groups

dtpCtpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 6, 3, 2, 1)
)
dtpCtpPmGroup.setObjects(
      *(("INFINERA-PM-DTPCTP-MIB", "dtpCtpPmValidity"),
        ("INFINERA-PM-DTPCTP-MIB", "dtpCtpPmDtpRxCV"),
        ("INFINERA-PM-DTPCTP-MIB", "dtpCtpPmDtpRxES"),
        ("INFINERA-PM-DTPCTP-MIB", "dtpCtpPmDtpRxSES"),
        ("INFINERA-PM-DTPCTP-MIB", "dtpCtpPmDtpRxUAS"),
        ("INFINERA-PM-DTPCTP-MIB", "dtpCtpPmDtpTxCV"),
        ("INFINERA-PM-DTPCTP-MIB", "dtpCtpPmDtpTxES"),
        ("INFINERA-PM-DTPCTP-MIB", "dtpCtpPmDtpTxSES"),
        ("INFINERA-PM-DTPCTP-MIB", "dtpCtpPmDtpTxUAS"))
)
if mibBuilder.loadTexts:
    dtpCtpPmGroup.setStatus("current")

dtpCtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 6, 3, 2, 2)
)
dtpCtpPmRealGroup.setObjects(
      *(("INFINERA-PM-DTPCTP-MIB", "dtpCtpPmRealDtpRxCV"),
        ("INFINERA-PM-DTPCTP-MIB", "dtpCtpPmRealDtpRxES"),
        ("INFINERA-PM-DTPCTP-MIB", "dtpCtpPmRealDtpRxSES"),
        ("INFINERA-PM-DTPCTP-MIB", "dtpCtpPmRealDtpRxUAS"),
        ("INFINERA-PM-DTPCTP-MIB", "dtpCtpPmRealDtpTxCV"),
        ("INFINERA-PM-DTPCTP-MIB", "dtpCtpPmRealDtpTxES"),
        ("INFINERA-PM-DTPCTP-MIB", "dtpCtpPmRealDtpTxSES"),
        ("INFINERA-PM-DTPCTP-MIB", "dtpCtpPmRealDtpTxUAS"),
        ("INFINERA-PM-DTPCTP-MIB", "dtpCtpPmRealPrbsSyncErr"),
        ("INFINERA-PM-DTPCTP-MIB", "dtpCtpPmRealPrbsErr"),
        ("INFINERA-PM-DTPCTP-MIB", "dtpCtpPmRealInternalCV"))
)
if mibBuilder.loadTexts:
    dtpCtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dtpCtpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 6, 3, 1, 1)
)
dtpCtpPmCompliance.setObjects(
    ("INFINERA-PM-DTPCTP-MIB", "dtpCtpPmGroup")
)
if mibBuilder.loadTexts:
    dtpCtpPmCompliance.setStatus(
        "current"
    )

dtpCtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 6, 3, 1, 2)
)
dtpCtpPmRealCompliance.setObjects(
    ("INFINERA-PM-DTPCTP-MIB", "dtpCtpPmRealGroup")
)
if mibBuilder.loadTexts:
    dtpCtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-DTPCTP-MIB",
    **{"dtpCtpPmMIB": dtpCtpPmMIB,
       "dtpCtpPmRealTable": dtpCtpPmRealTable,
       "dtpCtpPmRealEntry": dtpCtpPmRealEntry,
       "dtpCtpPmRealDtpRxCV": dtpCtpPmRealDtpRxCV,
       "dtpCtpPmRealDtpRxES": dtpCtpPmRealDtpRxES,
       "dtpCtpPmRealDtpRxSES": dtpCtpPmRealDtpRxSES,
       "dtpCtpPmRealDtpRxUAS": dtpCtpPmRealDtpRxUAS,
       "dtpCtpPmRealDtpTxCV": dtpCtpPmRealDtpTxCV,
       "dtpCtpPmRealDtpTxES": dtpCtpPmRealDtpTxES,
       "dtpCtpPmRealDtpTxSES": dtpCtpPmRealDtpTxSES,
       "dtpCtpPmRealDtpTxUAS": dtpCtpPmRealDtpTxUAS,
       "dtpCtpPmRealPrbsSyncErr": dtpCtpPmRealPrbsSyncErr,
       "dtpCtpPmRealPrbsErr": dtpCtpPmRealPrbsErr,
       "dtpCtpPmRealInternalCV": dtpCtpPmRealInternalCV,
       "dtpCtpPmTable": dtpCtpPmTable,
       "dtpCtpPmEntry": dtpCtpPmEntry,
       "dtpCtpPmTimestamp": dtpCtpPmTimestamp,
       "dtpCtpPmSampleDuration": dtpCtpPmSampleDuration,
       "dtpCtpPmValidity": dtpCtpPmValidity,
       "dtpCtpPmDtpRxCV": dtpCtpPmDtpRxCV,
       "dtpCtpPmDtpRxES": dtpCtpPmDtpRxES,
       "dtpCtpPmDtpRxSES": dtpCtpPmDtpRxSES,
       "dtpCtpPmDtpRxUAS": dtpCtpPmDtpRxUAS,
       "dtpCtpPmDtpTxCV": dtpCtpPmDtpTxCV,
       "dtpCtpPmDtpTxES": dtpCtpPmDtpTxES,
       "dtpCtpPmDtpTxSES": dtpCtpPmDtpTxSES,
       "dtpCtpPmDtpTxUAS": dtpCtpPmDtpTxUAS,
       "dtpCtpPmConformance": dtpCtpPmConformance,
       "dtpCtpPmCompliances": dtpCtpPmCompliances,
       "dtpCtpPmCompliance": dtpCtpPmCompliance,
       "dtpCtpPmRealCompliance": dtpCtpPmRealCompliance,
       "dtpCtpPmGroups": dtpCtpPmGroups,
       "dtpCtpPmGroup": dtpCtpPmGroup,
       "dtpCtpPmRealGroup": dtpCtpPmRealGroup}
)
