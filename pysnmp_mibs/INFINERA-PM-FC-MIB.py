# SNMP MIB module (INFINERA-PM-FC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-FC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:13 2025
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

(InfnSampleDuration,
 InfnServiceType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnSampleDuration",
    "InfnServiceType")

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

fcPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23)
)
if mibBuilder.loadTexts:
    fcPmMIB.setRevisions(
        ("2009-07-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FcPmRealTable_Object = MibTable
fcPmRealTable = _FcPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 1)
)
if mibBuilder.loadTexts:
    fcPmRealTable.setStatus("current")
_FcPmRealEntry_Object = MibTableRow
fcPmRealEntry = _FcPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 1, 1)
)
fcPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fcPmRealEntry.setStatus("current")
_FcPmRealRxPcsICG_Type = HCPerfIntervalCount
_FcPmRealRxPcsICG_Object = MibTableColumn
fcPmRealRxPcsICG = _FcPmRealRxPcsICG_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 1, 1, 1),
    _FcPmRealRxPcsICG_Type()
)
fcPmRealRxPcsICG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmRealRxPcsICG.setStatus("current")
_FcPmRealTxPcsICG_Type = HCPerfIntervalCount
_FcPmRealTxPcsICG_Object = MibTableColumn
fcPmRealTxPcsICG = _FcPmRealTxPcsICG_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 1, 1, 2),
    _FcPmRealTxPcsICG_Type()
)
fcPmRealTxPcsICG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmRealTxPcsICG.setStatus("current")
_FcPmRealRxPcsSESS_Type = Integer32
_FcPmRealRxPcsSESS_Object = MibTableColumn
fcPmRealRxPcsSESS = _FcPmRealRxPcsSESS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 1, 1, 3),
    _FcPmRealRxPcsSESS_Type()
)
fcPmRealRxPcsSESS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmRealRxPcsSESS.setStatus("current")
_FcPmRealTxPcsSESS_Type = Integer32
_FcPmRealTxPcsSESS_Object = MibTableColumn
fcPmRealTxPcsSESS = _FcPmRealTxPcsSESS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 1, 1, 4),
    _FcPmRealTxPcsSESS_Type()
)
fcPmRealTxPcsSESS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmRealTxPcsSESS.setStatus("current")
_FcPmRealRxPcsSES_Type = Integer32
_FcPmRealRxPcsSES_Object = MibTableColumn
fcPmRealRxPcsSES = _FcPmRealRxPcsSES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 1, 1, 5),
    _FcPmRealRxPcsSES_Type()
)
fcPmRealRxPcsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmRealRxPcsSES.setStatus("current")
_FcPmRealTxPcsSES_Type = Integer32
_FcPmRealTxPcsSES_Object = MibTableColumn
fcPmRealTxPcsSES = _FcPmRealTxPcsSES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 1, 1, 6),
    _FcPmRealTxPcsSES_Type()
)
fcPmRealTxPcsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmRealTxPcsSES.setStatus("current")
_FcPmRealRxPcsES_Type = Integer32
_FcPmRealRxPcsES_Object = MibTableColumn
fcPmRealRxPcsES = _FcPmRealRxPcsES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 1, 1, 7),
    _FcPmRealRxPcsES_Type()
)
fcPmRealRxPcsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmRealRxPcsES.setStatus("current")
_FcPmRealTxPcsES_Type = Integer32
_FcPmRealTxPcsES_Object = MibTableColumn
fcPmRealTxPcsES = _FcPmRealTxPcsES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 1, 1, 8),
    _FcPmRealTxPcsES_Type()
)
fcPmRealTxPcsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmRealTxPcsES.setStatus("current")
_FcPmRealRxFrames_Type = HCPerfIntervalCount
_FcPmRealRxFrames_Object = MibTableColumn
fcPmRealRxFrames = _FcPmRealRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 1, 1, 9),
    _FcPmRealRxFrames_Type()
)
fcPmRealRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmRealRxFrames.setStatus("current")
_FcPmRealTxFrames_Type = HCPerfIntervalCount
_FcPmRealTxFrames_Object = MibTableColumn
fcPmRealTxFrames = _FcPmRealTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 1, 1, 10),
    _FcPmRealTxFrames_Type()
)
fcPmRealTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmRealTxFrames.setStatus("current")
_FcPmRealRxErroredFrames_Type = HCPerfIntervalCount
_FcPmRealRxErroredFrames_Object = MibTableColumn
fcPmRealRxErroredFrames = _FcPmRealRxErroredFrames_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 1, 1, 11),
    _FcPmRealRxErroredFrames_Type()
)
fcPmRealRxErroredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmRealRxErroredFrames.setStatus("current")
_FcPmRealTxErroredFrames_Type = HCPerfIntervalCount
_FcPmRealTxErroredFrames_Object = MibTableColumn
fcPmRealTxErroredFrames = _FcPmRealTxErroredFrames_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 1, 1, 12),
    _FcPmRealTxErroredFrames_Type()
)
fcPmRealTxErroredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmRealTxErroredFrames.setStatus("current")
_FcPmRealRxOctets_Type = HCPerfIntervalCount
_FcPmRealRxOctets_Object = MibTableColumn
fcPmRealRxOctets = _FcPmRealRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 1, 1, 13),
    _FcPmRealRxOctets_Type()
)
fcPmRealRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmRealRxOctets.setStatus("current")
_FcPmRealTxOctets_Type = HCPerfIntervalCount
_FcPmRealTxOctets_Object = MibTableColumn
fcPmRealTxOctets = _FcPmRealTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 1, 1, 14),
    _FcPmRealTxOctets_Type()
)
fcPmRealTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmRealTxOctets.setStatus("current")
_FcPmRealRxErroredOctets_Type = HCPerfIntervalCount
_FcPmRealRxErroredOctets_Object = MibTableColumn
fcPmRealRxErroredOctets = _FcPmRealRxErroredOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 1, 1, 15),
    _FcPmRealRxErroredOctets_Type()
)
fcPmRealRxErroredOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmRealRxErroredOctets.setStatus("current")
_FcPmRealTxErroredOctets_Type = HCPerfIntervalCount
_FcPmRealTxErroredOctets_Object = MibTableColumn
fcPmRealTxErroredOctets = _FcPmRealTxErroredOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 1, 1, 16),
    _FcPmRealTxErroredOctets_Type()
)
fcPmRealTxErroredOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmRealTxErroredOctets.setStatus("current")
_FcPmRealRxFcSES_Type = Integer32
_FcPmRealRxFcSES_Object = MibTableColumn
fcPmRealRxFcSES = _FcPmRealRxFcSES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 1, 1, 17),
    _FcPmRealRxFcSES_Type()
)
fcPmRealRxFcSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmRealRxFcSES.setStatus("current")
_FcPmRealTxFcSES_Type = Integer32
_FcPmRealTxFcSES_Object = MibTableColumn
fcPmRealTxFcSES = _FcPmRealTxFcSES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 1, 1, 18),
    _FcPmRealTxFcSES_Type()
)
fcPmRealTxFcSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmRealTxFcSES.setStatus("current")
_FcPmRealLineTestSigSyncErr_Type = Integer32
_FcPmRealLineTestSigSyncErr_Object = MibTableColumn
fcPmRealLineTestSigSyncErr = _FcPmRealLineTestSigSyncErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 1, 1, 19),
    _FcPmRealLineTestSigSyncErr_Type()
)
fcPmRealLineTestSigSyncErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmRealLineTestSigSyncErr.setStatus("obsolete")
_FcPmRealLineTestSigErr_Type = Integer32
_FcPmRealLineTestSigErr_Object = MibTableColumn
fcPmRealLineTestSigErr = _FcPmRealLineTestSigErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 1, 1, 20),
    _FcPmRealLineTestSigErr_Type()
)
fcPmRealLineTestSigErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmRealLineTestSigErr.setStatus("obsolete")
_FcPmRealTribTestSigSyncErr_Type = Integer32
_FcPmRealTribTestSigSyncErr_Object = MibTableColumn
fcPmRealTribTestSigSyncErr = _FcPmRealTribTestSigSyncErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 1, 1, 21),
    _FcPmRealTribTestSigSyncErr_Type()
)
fcPmRealTribTestSigSyncErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmRealTribTestSigSyncErr.setStatus("obsolete")
_FcPmRealTribTestSigErr_Type = Integer32
_FcPmRealTribTestSigErr_Object = MibTableColumn
fcPmRealTribTestSigErr = _FcPmRealTribTestSigErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 1, 1, 22),
    _FcPmRealTribTestSigErr_Type()
)
fcPmRealTribTestSigErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmRealTribTestSigErr.setStatus("obsolete")
_FcPmTable_Object = MibTable
fcPmTable = _FcPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 2)
)
if mibBuilder.loadTexts:
    fcPmTable.setStatus("current")
_FcPmEntry_Object = MibTableRow
fcPmEntry = _FcPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 2, 1)
)
fcPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-FC-MIB", "fcPmSampleDuration"),
    (0, "INFINERA-PM-FC-MIB", "fcPmTimestamp"),
)
if mibBuilder.loadTexts:
    fcPmEntry.setStatus("current")


class _FcPmTimestamp_Type(Integer32):
    """Custom type fcPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FcPmTimestamp_Type.__name__ = "Integer32"
_FcPmTimestamp_Object = MibTableColumn
fcPmTimestamp = _FcPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 2, 1, 1),
    _FcPmTimestamp_Type()
)
fcPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcPmTimestamp.setStatus("current")
_FcPmSampleDuration_Type = InfnSampleDuration
_FcPmSampleDuration_Object = MibTableColumn
fcPmSampleDuration = _FcPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 2, 1, 2),
    _FcPmSampleDuration_Type()
)
fcPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcPmSampleDuration.setStatus("current")
_FcPmValidity_Type = TruthValue
_FcPmValidity_Object = MibTableColumn
fcPmValidity = _FcPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 2, 1, 3),
    _FcPmValidity_Type()
)
fcPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmValidity.setStatus("current")
_FcPmRxPcsICG_Type = HCPerfIntervalCount
_FcPmRxPcsICG_Object = MibTableColumn
fcPmRxPcsICG = _FcPmRxPcsICG_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 2, 1, 4),
    _FcPmRxPcsICG_Type()
)
fcPmRxPcsICG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmRxPcsICG.setStatus("current")
_FcPmTxPcsICG_Type = HCPerfIntervalCount
_FcPmTxPcsICG_Object = MibTableColumn
fcPmTxPcsICG = _FcPmTxPcsICG_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 2, 1, 5),
    _FcPmTxPcsICG_Type()
)
fcPmTxPcsICG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmTxPcsICG.setStatus("current")
_FcPmRxPcsSESS_Type = Integer32
_FcPmRxPcsSESS_Object = MibTableColumn
fcPmRxPcsSESS = _FcPmRxPcsSESS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 2, 1, 6),
    _FcPmRxPcsSESS_Type()
)
fcPmRxPcsSESS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmRxPcsSESS.setStatus("current")
_FcPmTxPcsSESS_Type = Integer32
_FcPmTxPcsSESS_Object = MibTableColumn
fcPmTxPcsSESS = _FcPmTxPcsSESS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 2, 1, 7),
    _FcPmTxPcsSESS_Type()
)
fcPmTxPcsSESS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmTxPcsSESS.setStatus("current")
_FcPmRxPcsSES_Type = Integer32
_FcPmRxPcsSES_Object = MibTableColumn
fcPmRxPcsSES = _FcPmRxPcsSES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 2, 1, 8),
    _FcPmRxPcsSES_Type()
)
fcPmRxPcsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmRxPcsSES.setStatus("current")
_FcPmTxPcsSES_Type = Integer32
_FcPmTxPcsSES_Object = MibTableColumn
fcPmTxPcsSES = _FcPmTxPcsSES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 2, 1, 9),
    _FcPmTxPcsSES_Type()
)
fcPmTxPcsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmTxPcsSES.setStatus("current")
_FcPmRxPcsES_Type = Integer32
_FcPmRxPcsES_Object = MibTableColumn
fcPmRxPcsES = _FcPmRxPcsES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 2, 1, 10),
    _FcPmRxPcsES_Type()
)
fcPmRxPcsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmRxPcsES.setStatus("current")
_FcPmTxPcsES_Type = Integer32
_FcPmTxPcsES_Object = MibTableColumn
fcPmTxPcsES = _FcPmTxPcsES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 2, 1, 11),
    _FcPmTxPcsES_Type()
)
fcPmTxPcsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmTxPcsES.setStatus("current")
_FcPmRxFrames_Type = HCPerfIntervalCount
_FcPmRxFrames_Object = MibTableColumn
fcPmRxFrames = _FcPmRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 2, 1, 12),
    _FcPmRxFrames_Type()
)
fcPmRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmRxFrames.setStatus("current")
_FcPmTxFrames_Type = HCPerfIntervalCount
_FcPmTxFrames_Object = MibTableColumn
fcPmTxFrames = _FcPmTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 2, 1, 13),
    _FcPmTxFrames_Type()
)
fcPmTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmTxFrames.setStatus("current")
_FcPmRxErroredFrames_Type = HCPerfIntervalCount
_FcPmRxErroredFrames_Object = MibTableColumn
fcPmRxErroredFrames = _FcPmRxErroredFrames_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 2, 1, 14),
    _FcPmRxErroredFrames_Type()
)
fcPmRxErroredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmRxErroredFrames.setStatus("current")
_FcPmTxErroredFrames_Type = HCPerfIntervalCount
_FcPmTxErroredFrames_Object = MibTableColumn
fcPmTxErroredFrames = _FcPmTxErroredFrames_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 2, 1, 15),
    _FcPmTxErroredFrames_Type()
)
fcPmTxErroredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmTxErroredFrames.setStatus("current")
_FcPmRxOctets_Type = HCPerfIntervalCount
_FcPmRxOctets_Object = MibTableColumn
fcPmRxOctets = _FcPmRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 2, 1, 16),
    _FcPmRxOctets_Type()
)
fcPmRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmRxOctets.setStatus("current")
_FcPmTxOctets_Type = HCPerfIntervalCount
_FcPmTxOctets_Object = MibTableColumn
fcPmTxOctets = _FcPmTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 2, 1, 17),
    _FcPmTxOctets_Type()
)
fcPmTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmTxOctets.setStatus("current")
_FcPmRxErroredOctets_Type = HCPerfIntervalCount
_FcPmRxErroredOctets_Object = MibTableColumn
fcPmRxErroredOctets = _FcPmRxErroredOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 2, 1, 18),
    _FcPmRxErroredOctets_Type()
)
fcPmRxErroredOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmRxErroredOctets.setStatus("current")
_FcPmTxErroredOctets_Type = HCPerfIntervalCount
_FcPmTxErroredOctets_Object = MibTableColumn
fcPmTxErroredOctets = _FcPmTxErroredOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 2, 1, 19),
    _FcPmTxErroredOctets_Type()
)
fcPmTxErroredOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmTxErroredOctets.setStatus("current")
_FcPmRxFcSES_Type = Integer32
_FcPmRxFcSES_Object = MibTableColumn
fcPmRxFcSES = _FcPmRxFcSES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 2, 1, 20),
    _FcPmRxFcSES_Type()
)
fcPmRxFcSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmRxFcSES.setStatus("current")
_FcPmTxFcSES_Type = Integer32
_FcPmTxFcSES_Object = MibTableColumn
fcPmTxFcSES = _FcPmTxFcSES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 2, 1, 21),
    _FcPmTxFcSES_Type()
)
fcPmTxFcSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmTxFcSES.setStatus("current")
_FcPmCircuitId_Type = DisplayString
_FcPmCircuitId_Object = MibTableColumn
fcPmCircuitId = _FcPmCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 2, 1, 22),
    _FcPmCircuitId_Type()
)
fcPmCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmCircuitId.setStatus("current")
_FcPmPayloadType_Type = InfnServiceType
_FcPmPayloadType_Object = MibTableColumn
fcPmPayloadType = _FcPmPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 2, 1, 23),
    _FcPmPayloadType_Type()
)
fcPmPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmPayloadType.setStatus("current")
_FcPmLineTestSigSyncErr_Type = Integer32
_FcPmLineTestSigSyncErr_Object = MibTableColumn
fcPmLineTestSigSyncErr = _FcPmLineTestSigSyncErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 2, 1, 24),
    _FcPmLineTestSigSyncErr_Type()
)
fcPmLineTestSigSyncErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmLineTestSigSyncErr.setStatus("obsolete")
_FcPmLineTestSigErr_Type = Integer32
_FcPmLineTestSigErr_Object = MibTableColumn
fcPmLineTestSigErr = _FcPmLineTestSigErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 2, 1, 25),
    _FcPmLineTestSigErr_Type()
)
fcPmLineTestSigErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmLineTestSigErr.setStatus("obsolete")
_FcPmTribTestSigSyncErr_Type = Integer32
_FcPmTribTestSigSyncErr_Object = MibTableColumn
fcPmTribTestSigSyncErr = _FcPmTribTestSigSyncErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 2, 1, 26),
    _FcPmTribTestSigSyncErr_Type()
)
fcPmTribTestSigSyncErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmTribTestSigSyncErr.setStatus("obsolete")
_FcPmTribTestSigErr_Type = Integer32
_FcPmTribTestSigErr_Object = MibTableColumn
fcPmTribTestSigErr = _FcPmTribTestSigErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 2, 1, 27),
    _FcPmTribTestSigErr_Type()
)
fcPmTribTestSigErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPmTribTestSigErr.setStatus("obsolete")
_FcPmConformance_ObjectIdentity = ObjectIdentity
fcPmConformance = _FcPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 3)
)
_FcPmCompliances_ObjectIdentity = ObjectIdentity
fcPmCompliances = _FcPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 3, 1)
)
_FcPmGroups_ObjectIdentity = ObjectIdentity
fcPmGroups = _FcPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 3, 2)
)

# Managed Objects groups

fcPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 3, 2, 1)
)
fcPmGroup.setObjects(
      *(("INFINERA-PM-FC-MIB", "fcPmTimestamp"),
        ("INFINERA-PM-FC-MIB", "fcPmSampleDuration"),
        ("INFINERA-PM-FC-MIB", "fcPmValidity"),
        ("INFINERA-PM-FC-MIB", "fcPmRxPcsICG"),
        ("INFINERA-PM-FC-MIB", "fcPmTxPcsICG"),
        ("INFINERA-PM-FC-MIB", "fcPmRxPcsSESS"),
        ("INFINERA-PM-FC-MIB", "fcPmTxPcsSESS"),
        ("INFINERA-PM-FC-MIB", "fcPmRxPcsSES"),
        ("INFINERA-PM-FC-MIB", "fcPmTxPcsSES"),
        ("INFINERA-PM-FC-MIB", "fcPmRxPcsES"),
        ("INFINERA-PM-FC-MIB", "fcPmTxPcsES"),
        ("INFINERA-PM-FC-MIB", "fcPmRxFrames"),
        ("INFINERA-PM-FC-MIB", "fcPmTxFrames"),
        ("INFINERA-PM-FC-MIB", "fcPmRxErroredFrames"),
        ("INFINERA-PM-FC-MIB", "fcPmTxErroredFrames"),
        ("INFINERA-PM-FC-MIB", "fcPmRxOctets"),
        ("INFINERA-PM-FC-MIB", "fcPmTxOctets"),
        ("INFINERA-PM-FC-MIB", "fcPmRxErroredOctets"),
        ("INFINERA-PM-FC-MIB", "fcPmTxErroredOctets"),
        ("INFINERA-PM-FC-MIB", "fcPmRxFcSES"),
        ("INFINERA-PM-FC-MIB", "fcPmTxFcSES"),
        ("INFINERA-PM-FC-MIB", "fcPmLineTestSigSyncErr"),
        ("INFINERA-PM-FC-MIB", "fcPmLineTestSigErr"),
        ("INFINERA-PM-FC-MIB", "fcPmTribTestSigSyncErr"),
        ("INFINERA-PM-FC-MIB", "fcPmTribTestSigErr"))
)
if mibBuilder.loadTexts:
    fcPmGroup.setStatus("current")

fcPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 3, 2, 2)
)
fcPmRealGroup.setObjects(
      *(("INFINERA-PM-FC-MIB", "fcPmRealRxPcsICG"),
        ("INFINERA-PM-FC-MIB", "fcPmRealTxPcsICG"),
        ("INFINERA-PM-FC-MIB", "fcPmRealRxPcsSESS"),
        ("INFINERA-PM-FC-MIB", "fcPmRealTxPcsSESS"),
        ("INFINERA-PM-FC-MIB", "fcPmRealRxPcsSES"),
        ("INFINERA-PM-FC-MIB", "fcPmRealTxPcsSES"),
        ("INFINERA-PM-FC-MIB", "fcPmRealRxPcsES"),
        ("INFINERA-PM-FC-MIB", "fcPmRealTxPcsES"),
        ("INFINERA-PM-FC-MIB", "fcPmRealRxFrames"),
        ("INFINERA-PM-FC-MIB", "fcPmRealTxFrames"),
        ("INFINERA-PM-FC-MIB", "fcPmRealRxErroredFrames"),
        ("INFINERA-PM-FC-MIB", "fcPmRealTxErroredFrames"),
        ("INFINERA-PM-FC-MIB", "fcPmRealRxOctets"),
        ("INFINERA-PM-FC-MIB", "fcPmRealTxOctets"),
        ("INFINERA-PM-FC-MIB", "fcPmRealRxErroredOctets"),
        ("INFINERA-PM-FC-MIB", "fcPmRealTxErroredOctets"),
        ("INFINERA-PM-FC-MIB", "fcPmRealRxFcSES"),
        ("INFINERA-PM-FC-MIB", "fcPmRealTxFcSES"),
        ("INFINERA-PM-FC-MIB", "fcPmRealLineTestSigSyncErr"),
        ("INFINERA-PM-FC-MIB", "fcPmRealLineTestSigErr"),
        ("INFINERA-PM-FC-MIB", "fcPmRealTribTestSigSyncErr"),
        ("INFINERA-PM-FC-MIB", "fcPmRealTribTestSigErr"))
)
if mibBuilder.loadTexts:
    fcPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fcPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 3, 1, 1)
)
fcPmCompliance.setObjects(
    ("INFINERA-PM-FC-MIB", "fcPmGroup")
)
if mibBuilder.loadTexts:
    fcPmCompliance.setStatus(
        "current"
    )

fcPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 23, 3, 1, 2)
)
fcPmRealCompliance.setObjects(
    ("INFINERA-PM-FC-MIB", "fcPmRealGroup")
)
if mibBuilder.loadTexts:
    fcPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-FC-MIB",
    **{"fcPmMIB": fcPmMIB,
       "fcPmRealTable": fcPmRealTable,
       "fcPmRealEntry": fcPmRealEntry,
       "fcPmRealRxPcsICG": fcPmRealRxPcsICG,
       "fcPmRealTxPcsICG": fcPmRealTxPcsICG,
       "fcPmRealRxPcsSESS": fcPmRealRxPcsSESS,
       "fcPmRealTxPcsSESS": fcPmRealTxPcsSESS,
       "fcPmRealRxPcsSES": fcPmRealRxPcsSES,
       "fcPmRealTxPcsSES": fcPmRealTxPcsSES,
       "fcPmRealRxPcsES": fcPmRealRxPcsES,
       "fcPmRealTxPcsES": fcPmRealTxPcsES,
       "fcPmRealRxFrames": fcPmRealRxFrames,
       "fcPmRealTxFrames": fcPmRealTxFrames,
       "fcPmRealRxErroredFrames": fcPmRealRxErroredFrames,
       "fcPmRealTxErroredFrames": fcPmRealTxErroredFrames,
       "fcPmRealRxOctets": fcPmRealRxOctets,
       "fcPmRealTxOctets": fcPmRealTxOctets,
       "fcPmRealRxErroredOctets": fcPmRealRxErroredOctets,
       "fcPmRealTxErroredOctets": fcPmRealTxErroredOctets,
       "fcPmRealRxFcSES": fcPmRealRxFcSES,
       "fcPmRealTxFcSES": fcPmRealTxFcSES,
       "fcPmRealLineTestSigSyncErr": fcPmRealLineTestSigSyncErr,
       "fcPmRealLineTestSigErr": fcPmRealLineTestSigErr,
       "fcPmRealTribTestSigSyncErr": fcPmRealTribTestSigSyncErr,
       "fcPmRealTribTestSigErr": fcPmRealTribTestSigErr,
       "fcPmTable": fcPmTable,
       "fcPmEntry": fcPmEntry,
       "fcPmTimestamp": fcPmTimestamp,
       "fcPmSampleDuration": fcPmSampleDuration,
       "fcPmValidity": fcPmValidity,
       "fcPmRxPcsICG": fcPmRxPcsICG,
       "fcPmTxPcsICG": fcPmTxPcsICG,
       "fcPmRxPcsSESS": fcPmRxPcsSESS,
       "fcPmTxPcsSESS": fcPmTxPcsSESS,
       "fcPmRxPcsSES": fcPmRxPcsSES,
       "fcPmTxPcsSES": fcPmTxPcsSES,
       "fcPmRxPcsES": fcPmRxPcsES,
       "fcPmTxPcsES": fcPmTxPcsES,
       "fcPmRxFrames": fcPmRxFrames,
       "fcPmTxFrames": fcPmTxFrames,
       "fcPmRxErroredFrames": fcPmRxErroredFrames,
       "fcPmTxErroredFrames": fcPmTxErroredFrames,
       "fcPmRxOctets": fcPmRxOctets,
       "fcPmTxOctets": fcPmTxOctets,
       "fcPmRxErroredOctets": fcPmRxErroredOctets,
       "fcPmTxErroredOctets": fcPmTxErroredOctets,
       "fcPmRxFcSES": fcPmRxFcSES,
       "fcPmTxFcSES": fcPmTxFcSES,
       "fcPmCircuitId": fcPmCircuitId,
       "fcPmPayloadType": fcPmPayloadType,
       "fcPmLineTestSigSyncErr": fcPmLineTestSigSyncErr,
       "fcPmLineTestSigErr": fcPmLineTestSigErr,
       "fcPmTribTestSigSyncErr": fcPmTribTestSigSyncErr,
       "fcPmTribTestSigErr": fcPmTribTestSigErr,
       "fcPmConformance": fcPmConformance,
       "fcPmCompliances": fcPmCompliances,
       "fcPmCompliance": fcPmCompliance,
       "fcPmRealCompliance": fcPmRealCompliance,
       "fcPmGroups": fcPmGroups,
       "fcPmGroup": fcPmGroup,
       "fcPmRealGroup": fcPmRealGroup}
)
