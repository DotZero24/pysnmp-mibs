# SNMP MIB module (STATEFUL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/radware/STATEFUL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:15:08 2025
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

(ipAddrEntry,) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipAddrEntry")

(rsSTATEFUL,) = mibBuilder.importSymbols(
    "RADWARE-MIB",
    "rsSTATEFUL")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class TruthValue(Integer32):
    """Custom type TruthValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )





class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2),
          ("notReady", 3),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6))
    )





class NetNumber(OctetString):
    """Custom type NetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _RsStatefulInspectionStatus_Type(Integer32):
    """Custom type rsStatefulInspectionStatus based on Integer32"""
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


_RsStatefulInspectionStatus_Type.__name__ = "Integer32"
_RsStatefulInspectionStatus_Object = MibScalar
rsStatefulInspectionStatus = _RsStatefulInspectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 1),
    _RsStatefulInspectionStatus_Type()
)
rsStatefulInspectionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsStatefulInspectionStatus.setStatus("mandatory")


class _RsStatefulInspectionActionMode_Type(Integer32):
    """Custom type rsStatefulInspectionActionMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("block", 2))
    )


_RsStatefulInspectionActionMode_Type.__name__ = "Integer32"
_RsStatefulInspectionActionMode_Object = MibScalar
rsStatefulInspectionActionMode = _RsStatefulInspectionActionMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 2),
    _RsStatefulInspectionActionMode_Type()
)
rsStatefulInspectionActionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsStatefulInspectionActionMode.setStatus("mandatory")
_RsStatefulPolicyTable_Object = MibTable
rsStatefulPolicyTable = _RsStatefulPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 3)
)
if mibBuilder.loadTexts:
    rsStatefulPolicyTable.setStatus("mandatory")
_RsStatefulPolicyEntry_Object = MibTableRow
rsStatefulPolicyEntry = _RsStatefulPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 3, 1)
)
rsStatefulPolicyEntry.setIndexNames(
    (0, "STATEFUL-MIB", "rsSTATFULPolicyName"),
)
if mibBuilder.loadTexts:
    rsStatefulPolicyEntry.setStatus("mandatory")


class _RsSTATFULPolicyName_Type(DisplayString):
    """Custom type rsSTATFULPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsSTATFULPolicyName_Type.__name__ = "DisplayString"
_RsSTATFULPolicyName_Object = MibTableColumn
rsSTATFULPolicyName = _RsSTATFULPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 3, 1, 1),
    _RsSTATFULPolicyName_Type()
)
rsSTATFULPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSTATFULPolicyName.setStatus("mandatory")


class _RsSTATFULPolicyProfileName_Type(DisplayString):
    """Custom type rsSTATFULPolicyProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsSTATFULPolicyProfileName_Type.__name__ = "DisplayString"
_RsSTATFULPolicyProfileName_Object = MibTableColumn
rsSTATFULPolicyProfileName = _RsSTATFULPolicyProfileName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 3, 1, 2),
    _RsSTATFULPolicyProfileName_Type()
)
rsSTATFULPolicyProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSTATFULPolicyProfileName.setStatus("mandatory")


class _RsSTATFULPolicySourceNet_Type(DisplayString):
    """Custom type rsSTATFULPolicySourceNet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsSTATFULPolicySourceNet_Type.__name__ = "DisplayString"
_RsSTATFULPolicySourceNet_Object = MibTableColumn
rsSTATFULPolicySourceNet = _RsSTATFULPolicySourceNet_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 3, 1, 3),
    _RsSTATFULPolicySourceNet_Type()
)
rsSTATFULPolicySourceNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSTATFULPolicySourceNet.setStatus("mandatory")


class _RsSTATFULPolicyDestinationNet_Type(DisplayString):
    """Custom type rsSTATFULPolicyDestinationNet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsSTATFULPolicyDestinationNet_Type.__name__ = "DisplayString"
_RsSTATFULPolicyDestinationNet_Object = MibTableColumn
rsSTATFULPolicyDestinationNet = _RsSTATFULPolicyDestinationNet_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 3, 1, 4),
    _RsSTATFULPolicyDestinationNet_Type()
)
rsSTATFULPolicyDestinationNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSTATFULPolicyDestinationNet.setStatus("mandatory")


class _RsSTATFULPolicyPhysicalPortGroup_Type(DisplayString):
    """Custom type rsSTATFULPolicyPhysicalPortGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsSTATFULPolicyPhysicalPortGroup_Type.__name__ = "DisplayString"
_RsSTATFULPolicyPhysicalPortGroup_Object = MibTableColumn
rsSTATFULPolicyPhysicalPortGroup = _RsSTATFULPolicyPhysicalPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 3, 1, 5),
    _RsSTATFULPolicyPhysicalPortGroup_Type()
)
rsSTATFULPolicyPhysicalPortGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSTATFULPolicyPhysicalPortGroup.setStatus("mandatory")


class _RsSTATFULPolicyVlanTagGroup_Type(DisplayString):
    """Custom type rsSTATFULPolicyVlanTagGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsSTATFULPolicyVlanTagGroup_Type.__name__ = "DisplayString"
_RsSTATFULPolicyVlanTagGroup_Object = MibTableColumn
rsSTATFULPolicyVlanTagGroup = _RsSTATFULPolicyVlanTagGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 3, 1, 6),
    _RsSTATFULPolicyVlanTagGroup_Type()
)
rsSTATFULPolicyVlanTagGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSTATFULPolicyVlanTagGroup.setStatus("mandatory")


class _RsSTATFULPolicyOperationalStatus_Type(Integer32):
    """Custom type rsSTATFULPolicyOperationalStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_RsSTATFULPolicyOperationalStatus_Type.__name__ = "Integer32"
_RsSTATFULPolicyOperationalStatus_Object = MibTableColumn
rsSTATFULPolicyOperationalStatus = _RsSTATFULPolicyOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 3, 1, 7),
    _RsSTATFULPolicyOperationalStatus_Type()
)
rsSTATFULPolicyOperationalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSTATFULPolicyOperationalStatus.setStatus("mandatory")
_RsSTATFULPolicyStatus_Type = RowStatus
_RsSTATFULPolicyStatus_Object = MibTableColumn
rsSTATFULPolicyStatus = _RsSTATFULPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 3, 1, 8),
    _RsSTATFULPolicyStatus_Type()
)
rsSTATFULPolicyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSTATFULPolicyStatus.setStatus("mandatory")


class _RsSTATFULPolicyAction_Type(Integer32):
    """Custom type rsSTATFULPolicyAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("report", 0),
          ("block", 1))
    )


_RsSTATFULPolicyAction_Type.__name__ = "Integer32"
_RsSTATFULPolicyAction_Object = MibTableColumn
rsSTATFULPolicyAction = _RsSTATFULPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 3, 1, 9),
    _RsSTATFULPolicyAction_Type()
)
rsSTATFULPolicyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSTATFULPolicyAction.setStatus("mandatory")


class _RsSTATFULPolicyPacketReport_Type(Integer32):
    """Custom type rsSTATFULPolicyPacketReport based on Integer32"""
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


_RsSTATFULPolicyPacketReport_Type.__name__ = "Integer32"
_RsSTATFULPolicyPacketReport_Object = MibTableColumn
rsSTATFULPolicyPacketReport = _RsSTATFULPolicyPacketReport_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 3, 1, 10),
    _RsSTATFULPolicyPacketReport_Type()
)
rsSTATFULPolicyPacketReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSTATFULPolicyPacketReport.setStatus("mandatory")
_RsStatefulProfileTable_Object = MibTable
rsStatefulProfileTable = _RsStatefulProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 4)
)
if mibBuilder.loadTexts:
    rsStatefulProfileTable.setStatus("mandatory")
_RsStatefulProfileEntry_Object = MibTableRow
rsStatefulProfileEntry = _RsStatefulProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 4, 1)
)
rsStatefulProfileEntry.setIndexNames(
    (0, "STATEFUL-MIB", "rsSTATFULProfileName"),
)
if mibBuilder.loadTexts:
    rsStatefulProfileEntry.setStatus("mandatory")


class _RsSTATFULProfileName_Type(DisplayString):
    """Custom type rsSTATFULProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsSTATFULProfileName_Type.__name__ = "DisplayString"
_RsSTATFULProfileName_Object = MibTableColumn
rsSTATFULProfileName = _RsSTATFULProfileName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 4, 1, 1),
    _RsSTATFULProfileName_Type()
)
rsSTATFULProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSTATFULProfileName.setStatus("mandatory")
_RsSTATFULProfileStatus_Type = RowStatus
_RsSTATFULProfileStatus_Object = MibTableColumn
rsSTATFULProfileStatus = _RsSTATFULProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 4, 1, 2),
    _RsSTATFULProfileStatus_Type()
)
rsSTATFULProfileStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSTATFULProfileStatus.setStatus("mandatory")


class _RsSTATFULProfileactThreshold_Type(Integer32):
    """Custom type rsSTATFULProfileactThreshold based on Integer32"""
    defaultValue = 5000


_RsSTATFULProfileactThreshold_Type.__name__ = "Integer32"
_RsSTATFULProfileactThreshold_Object = MibTableColumn
rsSTATFULProfileactThreshold = _RsSTATFULProfileactThreshold_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 4, 1, 3),
    _RsSTATFULProfileactThreshold_Type()
)
rsSTATFULProfileactThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSTATFULProfileactThreshold.setStatus("mandatory")


class _RsSTATFULProfiletermThreshold_Type(Integer32):
    """Custom type rsSTATFULProfiletermThreshold based on Integer32"""
    defaultValue = 4000


_RsSTATFULProfiletermThreshold_Type.__name__ = "Integer32"
_RsSTATFULProfiletermThreshold_Object = MibTableColumn
rsSTATFULProfiletermThreshold = _RsSTATFULProfiletermThreshold_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 4, 1, 4),
    _RsSTATFULProfiletermThreshold_Type()
)
rsSTATFULProfiletermThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSTATFULProfiletermThreshold.setStatus("mandatory")


class _RsSTATFULProfilesynAckAllow_Type(Integer32):
    """Custom type rsSTATFULProfilesynAckAllow based on Integer32"""
    defaultValue = 1

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


_RsSTATFULProfilesynAckAllow_Type.__name__ = "Integer32"
_RsSTATFULProfilesynAckAllow_Object = MibTableColumn
rsSTATFULProfilesynAckAllow = _RsSTATFULProfilesynAckAllow_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 4, 1, 5),
    _RsSTATFULProfilesynAckAllow_Type()
)
rsSTATFULProfilesynAckAllow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSTATFULProfilesynAckAllow.setStatus("mandatory")


class _RsSTATFULProfilePacketTraceStatus_Type(Integer32):
    """Custom type rsSTATFULProfilePacketTraceStatus based on Integer32"""
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


_RsSTATFULProfilePacketTraceStatus_Type.__name__ = "Integer32"
_RsSTATFULProfilePacketTraceStatus_Object = MibTableColumn
rsSTATFULProfilePacketTraceStatus = _RsSTATFULProfilePacketTraceStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 4, 1, 6),
    _RsSTATFULProfilePacketTraceStatus_Type()
)
rsSTATFULProfilePacketTraceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSTATFULProfilePacketTraceStatus.setStatus("mandatory")


class _RsSTATFULProfilePacketReportStatus_Type(Integer32):
    """Custom type rsSTATFULProfilePacketReportStatus based on Integer32"""
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


_RsSTATFULProfilePacketReportStatus_Type.__name__ = "Integer32"
_RsSTATFULProfilePacketReportStatus_Object = MibTableColumn
rsSTATFULProfilePacketReportStatus = _RsSTATFULProfilePacketReportStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 4, 1, 7),
    _RsSTATFULProfilePacketReportStatus_Type()
)
rsSTATFULProfilePacketReportStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSTATFULProfilePacketReportStatus.setStatus("mandatory")


class _RsSTATFULProfileRisk_Type(Integer32):
    """Custom type rsSTATFULProfileRisk based on Integer32"""
    defaultValue = 2

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
        *(("info", 1),
          ("low", 2),
          ("medium", 3),
          ("high", 4))
    )


_RsSTATFULProfileRisk_Type.__name__ = "Integer32"
_RsSTATFULProfileRisk_Object = MibTableColumn
rsSTATFULProfileRisk = _RsSTATFULProfileRisk_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 4, 1, 8),
    _RsSTATFULProfileRisk_Type()
)
rsSTATFULProfileRisk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSTATFULProfileRisk.setStatus("mandatory")


class _RsSTATFULProfileAction_Type(Integer32):
    """Custom type rsSTATFULProfileAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("report", 0),
          ("block", 1))
    )


_RsSTATFULProfileAction_Type.__name__ = "Integer32"
_RsSTATFULProfileAction_Object = MibTableColumn
rsSTATFULProfileAction = _RsSTATFULProfileAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 4, 1, 9),
    _RsSTATFULProfileAction_Type()
)
rsSTATFULProfileAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSTATFULProfileAction.setStatus("mandatory")
_RsStatefulProtocolAgingTable_Object = MibTable
rsStatefulProtocolAgingTable = _RsStatefulProtocolAgingTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 5)
)
if mibBuilder.loadTexts:
    rsStatefulProtocolAgingTable.setStatus("mandatory")
_RsStatefulProtocolAgingEntry_Object = MibTableRow
rsStatefulProtocolAgingEntry = _RsStatefulProtocolAgingEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 5, 1)
)
rsStatefulProtocolAgingEntry.setIndexNames(
    (0, "STATEFUL-MIB", "rsSTATFULProtocolAgingIndex"),
)
if mibBuilder.loadTexts:
    rsStatefulProtocolAgingEntry.setStatus("mandatory")
_RsSTATFULProtocolAgingIndex_Type = Integer32
_RsSTATFULProtocolAgingIndex_Object = MibTableColumn
rsSTATFULProtocolAgingIndex = _RsSTATFULProtocolAgingIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 5, 1, 1),
    _RsSTATFULProtocolAgingIndex_Type()
)
rsSTATFULProtocolAgingIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSTATFULProtocolAgingIndex.setStatus("mandatory")


class _RsSTATFULProtocolName_Type(DisplayString):
    """Custom type rsSTATFULProtocolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsSTATFULProtocolName_Type.__name__ = "DisplayString"
_RsSTATFULProtocolName_Object = MibTableColumn
rsSTATFULProtocolName = _RsSTATFULProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 5, 1, 2),
    _RsSTATFULProtocolName_Type()
)
rsSTATFULProtocolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSTATFULProtocolName.setStatus("mandatory")
_RsSTATFULProtocolAgingValue_Type = Integer32
_RsSTATFULProtocolAgingValue_Object = MibTableColumn
rsSTATFULProtocolAgingValue = _RsSTATFULProtocolAgingValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 5, 1, 3),
    _RsSTATFULProtocolAgingValue_Type()
)
rsSTATFULProtocolAgingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSTATFULProtocolAgingValue.setStatus("mandatory")


class _RsStatefulStartupMode_Type(Integer32):
    """Custom type rsStatefulStartupMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("graceful", 3))
    )


_RsStatefulStartupMode_Type.__name__ = "Integer32"
_RsStatefulStartupMode_Object = MibScalar
rsStatefulStartupMode = _RsStatefulStartupMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 6),
    _RsStatefulStartupMode_Type()
)
rsStatefulStartupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsStatefulStartupMode.setStatus("mandatory")


class _RsStatefulStartupTimer_Type(Integer32):
    """Custom type rsStatefulStartupTimer based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsStatefulStartupTimer_Type.__name__ = "Integer32"
_RsStatefulStartupTimer_Object = MibScalar
rsStatefulStartupTimer = _RsStatefulStartupTimer_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 7),
    _RsStatefulStartupTimer_Type()
)
rsStatefulStartupTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsStatefulStartupTimer.setStatus("mandatory")


class _RsStatefulInspectionState_Type(Integer32):
    """Custom type rsStatefulInspectionState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_RsStatefulInspectionState_Type.__name__ = "Integer32"
_RsStatefulInspectionState_Object = MibScalar
rsStatefulInspectionState = _RsStatefulInspectionState_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 8),
    _RsStatefulInspectionState_Type()
)
rsStatefulInspectionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsStatefulInspectionState.setStatus("mandatory")
_RsStatefulStatisticsTable_Object = MibTable
rsStatefulStatisticsTable = _RsStatefulStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 9)
)
if mibBuilder.loadTexts:
    rsStatefulStatisticsTable.setStatus("mandatory")
_RsStatefulStatisticsEntry_Object = MibTableRow
rsStatefulStatisticsEntry = _RsStatefulStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 9, 1)
)
rsStatefulStatisticsEntry.setIndexNames(
    (0, "STATEFUL-MIB", "rsSTATFULStatisticsIndex"),
)
if mibBuilder.loadTexts:
    rsStatefulStatisticsEntry.setStatus("mandatory")
_RsSTATFULStatisticsIndex_Type = Integer32
_RsSTATFULStatisticsIndex_Object = MibTableColumn
rsSTATFULStatisticsIndex = _RsSTATFULStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 9, 1, 1),
    _RsSTATFULStatisticsIndex_Type()
)
rsSTATFULStatisticsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSTATFULStatisticsIndex.setStatus("mandatory")


class _RsSTATFULStatisticsProtocolName_Type(DisplayString):
    """Custom type rsSTATFULStatisticsProtocolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsSTATFULStatisticsProtocolName_Type.__name__ = "DisplayString"
_RsSTATFULStatisticsProtocolName_Object = MibTableColumn
rsSTATFULStatisticsProtocolName = _RsSTATFULStatisticsProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 9, 1, 2),
    _RsSTATFULStatisticsProtocolName_Type()
)
rsSTATFULStatisticsProtocolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSTATFULStatisticsProtocolName.setStatus("mandatory")
_RsSTATFULStatisticsEstablished_Type = Integer32
_RsSTATFULStatisticsEstablished_Object = MibTableColumn
rsSTATFULStatisticsEstablished = _RsSTATFULStatisticsEstablished_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 9, 1, 3),
    _RsSTATFULStatisticsEstablished_Type()
)
rsSTATFULStatisticsEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSTATFULStatisticsEstablished.setStatus("mandatory")
_RsSTATFULStatisticsTainted_Type = Integer32
_RsSTATFULStatisticsTainted_Object = MibTableColumn
rsSTATFULStatisticsTainted = _RsSTATFULStatisticsTainted_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 9, 1, 4),
    _RsSTATFULStatisticsTainted_Type()
)
rsSTATFULStatisticsTainted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSTATFULStatisticsTainted.setStatus("mandatory")
_RsStatefulReportThresholdTable_Object = MibTable
rsStatefulReportThresholdTable = _RsStatefulReportThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 10)
)
if mibBuilder.loadTexts:
    rsStatefulReportThresholdTable.setStatus("mandatory")
_RsStatefulReportThresholdEntry_Object = MibTableRow
rsStatefulReportThresholdEntry = _RsStatefulReportThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 10, 1)
)
rsStatefulReportThresholdEntry.setIndexNames(
    (0, "STATEFUL-MIB", "rsSTATFULReportThresholdRisk"),
)
if mibBuilder.loadTexts:
    rsStatefulReportThresholdEntry.setStatus("mandatory")


class _RsSTATFULReportThresholdRisk_Type(DisplayString):
    """Custom type rsSTATFULReportThresholdRisk based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsSTATFULReportThresholdRisk_Type.__name__ = "DisplayString"
_RsSTATFULReportThresholdRisk_Object = MibTableColumn
rsSTATFULReportThresholdRisk = _RsSTATFULReportThresholdRisk_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 10, 1, 1),
    _RsSTATFULReportThresholdRisk_Type()
)
rsSTATFULReportThresholdRisk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSTATFULReportThresholdRisk.setStatus("mandatory")
_RsSTATFULReportThresholdValue_Type = Integer32
_RsSTATFULReportThresholdValue_Object = MibTableColumn
rsSTATFULReportThresholdValue = _RsSTATFULReportThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 10, 1, 2),
    _RsSTATFULReportThresholdValue_Type()
)
rsSTATFULReportThresholdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSTATFULReportThresholdValue.setStatus("mandatory")


class _RsStatefulMidflowStatus_Type(Integer32):
    """Custom type rsStatefulMidflowStatus based on Integer32"""
    defaultValue = 1

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


_RsStatefulMidflowStatus_Type.__name__ = "Integer32"
_RsStatefulMidflowStatus_Object = MibScalar
rsStatefulMidflowStatus = _RsStatefulMidflowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 11),
    _RsStatefulMidflowStatus_Type()
)
rsStatefulMidflowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsStatefulMidflowStatus.setStatus("mandatory")


class _RsStatefulMidflowAction_Type(Integer32):
    """Custom type rsStatefulMidflowAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("report-only", 0),
          ("drop", 1))
    )


_RsStatefulMidflowAction_Type.__name__ = "Integer32"
_RsStatefulMidflowAction_Object = MibScalar
rsStatefulMidflowAction = _RsStatefulMidflowAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 12),
    _RsStatefulMidflowAction_Type()
)
rsStatefulMidflowAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsStatefulMidflowAction.setStatus("mandatory")


class _RsStatefulMidflowTermThreshold_Type(Integer32):
    """Custom type rsStatefulMidflowTermThreshold based on Integer32"""
    defaultValue = 0


_RsStatefulMidflowTermThreshold_Type.__name__ = "Integer32"
_RsStatefulMidflowTermThreshold_Object = MibScalar
rsStatefulMidflowTermThreshold = _RsStatefulMidflowTermThreshold_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 13),
    _RsStatefulMidflowTermThreshold_Type()
)
rsStatefulMidflowTermThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsStatefulMidflowTermThreshold.setStatus("mandatory")


class _RsStatefulMidflowActThreshold_Type(Integer32):
    """Custom type rsStatefulMidflowActThreshold based on Integer32"""
    defaultValue = 0


_RsStatefulMidflowActThreshold_Type.__name__ = "Integer32"
_RsStatefulMidflowActThreshold_Object = MibScalar
rsStatefulMidflowActThreshold = _RsStatefulMidflowActThreshold_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 14),
    _RsStatefulMidflowActThreshold_Type()
)
rsStatefulMidflowActThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsStatefulMidflowActThreshold.setStatus("mandatory")


class _RsStatefulMidflowPacketTraceStatus_Type(Integer32):
    """Custom type rsStatefulMidflowPacketTraceStatus based on Integer32"""
    defaultValue = 1

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


_RsStatefulMidflowPacketTraceStatus_Type.__name__ = "Integer32"
_RsStatefulMidflowPacketTraceStatus_Object = MibScalar
rsStatefulMidflowPacketTraceStatus = _RsStatefulMidflowPacketTraceStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 15),
    _RsStatefulMidflowPacketTraceStatus_Type()
)
rsStatefulMidflowPacketTraceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsStatefulMidflowPacketTraceStatus.setStatus("mandatory")


class _RsStatefulMidflowAttackRisk_Type(Integer32):
    """Custom type rsStatefulMidflowAttackRisk based on Integer32"""
    defaultValue = 2

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
        *(("info", 1),
          ("low", 2),
          ("medium", 3),
          ("high", 4))
    )


_RsStatefulMidflowAttackRisk_Type.__name__ = "Integer32"
_RsStatefulMidflowAttackRisk_Object = MibScalar
rsStatefulMidflowAttackRisk = _RsStatefulMidflowAttackRisk_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 16),
    _RsStatefulMidflowAttackRisk_Type()
)
rsStatefulMidflowAttackRisk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsStatefulMidflowAttackRisk.setStatus("mandatory")


class _RsStatefulUpdatePoliciesTimer_Type(Integer32):
    """Custom type rsStatefulUpdatePoliciesTimer based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsStatefulUpdatePoliciesTimer_Type.__name__ = "Integer32"
_RsStatefulUpdatePoliciesTimer_Object = MibScalar
rsStatefulUpdatePoliciesTimer = _RsStatefulUpdatePoliciesTimer_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 17),
    _RsStatefulUpdatePoliciesTimer_Type()
)
rsStatefulUpdatePoliciesTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsStatefulUpdatePoliciesTimer.setStatus("mandatory")


class _RsStatefulSessionTableFullTimer_Type(Integer32):
    """Custom type rsStatefulSessionTableFullTimer based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsStatefulSessionTableFullTimer_Type.__name__ = "Integer32"
_RsStatefulSessionTableFullTimer_Object = MibScalar
rsStatefulSessionTableFullTimer = _RsStatefulSessionTableFullTimer_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 18),
    _RsStatefulSessionTableFullTimer_Type()
)
rsStatefulSessionTableFullTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsStatefulSessionTableFullTimer.setStatus("mandatory")


class _RsStatefulOverloadTimer_Type(Integer32):
    """Custom type rsStatefulOverloadTimer based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsStatefulOverloadTimer_Type.__name__ = "Integer32"
_RsStatefulOverloadTimer_Object = MibScalar
rsStatefulOverloadTimer = _RsStatefulOverloadTimer_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 118, 19),
    _RsStatefulOverloadTimer_Type()
)
rsStatefulOverloadTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsStatefulOverloadTimer.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STATEFUL-MIB",
    **{"TruthValue": TruthValue,
       "RowStatus": RowStatus,
       "NetNumber": NetNumber,
       "rsStatefulInspectionStatus": rsStatefulInspectionStatus,
       "rsStatefulInspectionActionMode": rsStatefulInspectionActionMode,
       "rsStatefulPolicyTable": rsStatefulPolicyTable,
       "rsStatefulPolicyEntry": rsStatefulPolicyEntry,
       "rsSTATFULPolicyName": rsSTATFULPolicyName,
       "rsSTATFULPolicyProfileName": rsSTATFULPolicyProfileName,
       "rsSTATFULPolicySourceNet": rsSTATFULPolicySourceNet,
       "rsSTATFULPolicyDestinationNet": rsSTATFULPolicyDestinationNet,
       "rsSTATFULPolicyPhysicalPortGroup": rsSTATFULPolicyPhysicalPortGroup,
       "rsSTATFULPolicyVlanTagGroup": rsSTATFULPolicyVlanTagGroup,
       "rsSTATFULPolicyOperationalStatus": rsSTATFULPolicyOperationalStatus,
       "rsSTATFULPolicyStatus": rsSTATFULPolicyStatus,
       "rsSTATFULPolicyAction": rsSTATFULPolicyAction,
       "rsSTATFULPolicyPacketReport": rsSTATFULPolicyPacketReport,
       "rsStatefulProfileTable": rsStatefulProfileTable,
       "rsStatefulProfileEntry": rsStatefulProfileEntry,
       "rsSTATFULProfileName": rsSTATFULProfileName,
       "rsSTATFULProfileStatus": rsSTATFULProfileStatus,
       "rsSTATFULProfileactThreshold": rsSTATFULProfileactThreshold,
       "rsSTATFULProfiletermThreshold": rsSTATFULProfiletermThreshold,
       "rsSTATFULProfilesynAckAllow": rsSTATFULProfilesynAckAllow,
       "rsSTATFULProfilePacketTraceStatus": rsSTATFULProfilePacketTraceStatus,
       "rsSTATFULProfilePacketReportStatus": rsSTATFULProfilePacketReportStatus,
       "rsSTATFULProfileRisk": rsSTATFULProfileRisk,
       "rsSTATFULProfileAction": rsSTATFULProfileAction,
       "rsStatefulProtocolAgingTable": rsStatefulProtocolAgingTable,
       "rsStatefulProtocolAgingEntry": rsStatefulProtocolAgingEntry,
       "rsSTATFULProtocolAgingIndex": rsSTATFULProtocolAgingIndex,
       "rsSTATFULProtocolName": rsSTATFULProtocolName,
       "rsSTATFULProtocolAgingValue": rsSTATFULProtocolAgingValue,
       "rsStatefulStartupMode": rsStatefulStartupMode,
       "rsStatefulStartupTimer": rsStatefulStartupTimer,
       "rsStatefulInspectionState": rsStatefulInspectionState,
       "rsStatefulStatisticsTable": rsStatefulStatisticsTable,
       "rsStatefulStatisticsEntry": rsStatefulStatisticsEntry,
       "rsSTATFULStatisticsIndex": rsSTATFULStatisticsIndex,
       "rsSTATFULStatisticsProtocolName": rsSTATFULStatisticsProtocolName,
       "rsSTATFULStatisticsEstablished": rsSTATFULStatisticsEstablished,
       "rsSTATFULStatisticsTainted": rsSTATFULStatisticsTainted,
       "rsStatefulReportThresholdTable": rsStatefulReportThresholdTable,
       "rsStatefulReportThresholdEntry": rsStatefulReportThresholdEntry,
       "rsSTATFULReportThresholdRisk": rsSTATFULReportThresholdRisk,
       "rsSTATFULReportThresholdValue": rsSTATFULReportThresholdValue,
       "rsStatefulMidflowStatus": rsStatefulMidflowStatus,
       "rsStatefulMidflowAction": rsStatefulMidflowAction,
       "rsStatefulMidflowTermThreshold": rsStatefulMidflowTermThreshold,
       "rsStatefulMidflowActThreshold": rsStatefulMidflowActThreshold,
       "rsStatefulMidflowPacketTraceStatus": rsStatefulMidflowPacketTraceStatus,
       "rsStatefulMidflowAttackRisk": rsStatefulMidflowAttackRisk,
       "rsStatefulUpdatePoliciesTimer": rsStatefulUpdatePoliciesTimer,
       "rsStatefulSessionTableFullTimer": rsStatefulSessionTableFullTimer,
       "rsStatefulOverloadTimer": rsStatefulOverloadTimer}
)
