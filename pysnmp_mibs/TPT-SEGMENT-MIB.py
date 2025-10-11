# SNMP MIB module (TPT-SEGMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/trendmicro/TPT-SEGMENT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:06:05 2025
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

(tpt_tpa_objs,) = mibBuilder.importSymbols(
    "TPT-TPAMIBS-MIB",
    "tpt-tpa-objs")


# MODULE-IDENTITY

tpt_segment_objs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 19)
)
if mibBuilder.loadTexts:
    tpt_segment_objs.setRevisions(
        ("2016-05-25 18:54",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SegmentSflowStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("error", 2),
          ("not-applicable", 3))
    )



# MIB Managed Objects in the order of their OIDs

_SegmentTable_Object = MibTable
segmentTable = _SegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 19, 1)
)
if mibBuilder.loadTexts:
    segmentTable.setStatus("current")
_SegmentEntry_Object = MibTableRow
segmentEntry = _SegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 19, 1, 1)
)
segmentEntry.setIndexNames(
    (0, "TPT-SEGMENT-MIB", "slotIndex"),
    (0, "TPT-SEGMENT-MIB", "segmentIndex"),
)
if mibBuilder.loadTexts:
    segmentEntry.setStatus("current")
_SlotIndex_Type = Unsigned32
_SlotIndex_Object = MibTableColumn
slotIndex = _SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 19, 1, 1, 1),
    _SlotIndex_Type()
)
slotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotIndex.setStatus("current")
_SegmentIndex_Type = Unsigned32
_SegmentIndex_Object = MibTableColumn
segmentIndex = _SegmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 19, 1, 1, 2),
    _SegmentIndex_Type()
)
segmentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentIndex.setStatus("current")
_SegmentSflowStatus_Type = SegmentSflowStatus
_SegmentSflowStatus_Object = MibTableColumn
segmentSflowStatus = _SegmentSflowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 19, 1, 1, 3),
    _SegmentSflowStatus_Type()
)
segmentSflowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentSflowStatus.setStatus("current")
_SFlowDivisor_Type = Unsigned32
_SFlowDivisor_Object = MibTableColumn
sFlowDivisor = _SFlowDivisor_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 19, 1, 1, 4),
    _SFlowDivisor_Type()
)
sFlowDivisor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFlowDivisor.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPT-SEGMENT-MIB",
    **{"SegmentSflowStatus": SegmentSflowStatus,
       "tpt-segment-objs": tpt_segment_objs,
       "segmentTable": segmentTable,
       "segmentEntry": segmentEntry,
       "slotIndex": slotIndex,
       "segmentIndex": segmentIndex,
       "segmentSflowStatus": segmentSflowStatus,
       "sFlowDivisor": sFlowDivisor}
)
