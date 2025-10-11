# SNMP MIB module (CCK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/radware/CCK-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:15:19 2025
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

(RowStatus,
 TruthValue,
 rndErrorDesc,
 rndErrorSeverity,
 rsCCK) = mibBuilder.importSymbols(
    "RADWARE-MIB",
    "RowStatus",
    "TruthValue",
    "rndErrorDesc",
    "rndErrorSeverity",
    "rsCCK")

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



class NetNumber(OctetString):
    """Custom type NetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsCCKElementTable_Object = MibTable
rsCCKElementTable = _RsCCKElementTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 1)
)
if mibBuilder.loadTexts:
    rsCCKElementTable.setStatus("mandatory")
_RsCCKElementEntry_Object = MibTableRow
rsCCKElementEntry = _RsCCKElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 1, 1)
)
rsCCKElementEntry.setIndexNames(
    (0, "CCK-MIB", "rsCCKElementId"),
)
if mibBuilder.loadTexts:
    rsCCKElementEntry.setStatus("mandatory")
_RsCCKElementId_Type = Integer32
_RsCCKElementId_Object = MibTableColumn
rsCCKElementId = _RsCCKElementId_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 1, 1, 1),
    _RsCCKElementId_Type()
)
rsCCKElementId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCCKElementId.setStatus("mandatory")


class _RsCCKElementDescription_Type(DisplayString):
    """Custom type rsCCKElementDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RsCCKElementDescription_Type.__name__ = "DisplayString"
_RsCCKElementDescription_Object = MibTableColumn
rsCCKElementDescription = _RsCCKElementDescription_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 1, 1, 2),
    _RsCCKElementDescription_Type()
)
rsCCKElementDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCCKElementDescription.setStatus("mandatory")


class _RsCCKElementGroup_Type(DisplayString):
    """Custom type rsCCKElementGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RsCCKElementGroup_Type.__name__ = "DisplayString"
_RsCCKElementGroup_Object = MibTableColumn
rsCCKElementGroup = _RsCCKElementGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 1, 1, 3),
    _RsCCKElementGroup_Type()
)
rsCCKElementGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCCKElementGroup.setStatus("mandatory")


class _RsCCKElementIsActive_Type(Integer32):
    """Custom type rsCCKElementIsActive based on Integer32"""
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


_RsCCKElementIsActive_Type.__name__ = "Integer32"
_RsCCKElementIsActive_Object = MibTableColumn
rsCCKElementIsActive = _RsCCKElementIsActive_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 1, 1, 4),
    _RsCCKElementIsActive_Type()
)
rsCCKElementIsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCCKElementIsActive.setStatus("mandatory")


class _RsCCKElementIsAvailable_Type(Integer32):
    """Custom type rsCCKElementIsAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("unavailable", 2),
          ("nonewsessions", 3))
    )


_RsCCKElementIsAvailable_Type.__name__ = "Integer32"
_RsCCKElementIsAvailable_Object = MibTableColumn
rsCCKElementIsAvailable = _RsCCKElementIsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 1, 1, 5),
    _RsCCKElementIsAvailable_Type()
)
rsCCKElementIsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCCKElementIsAvailable.setStatus("mandatory")
_RsCCKElementDftAddr_Type = IpAddress
_RsCCKElementDftAddr_Object = MibTableColumn
rsCCKElementDftAddr = _RsCCKElementDftAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 1, 1, 6),
    _RsCCKElementDftAddr_Type()
)
rsCCKElementDftAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCCKElementDftAddr.setStatus("mandatory")
_RsCCKElementRowStatus_Type = RowStatus
_RsCCKElementRowStatus_Object = MibTableColumn
rsCCKElementRowStatus = _RsCCKElementRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 1, 1, 7),
    _RsCCKElementRowStatus_Type()
)
rsCCKElementRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCCKElementRowStatus.setStatus("mandatory")
_RsCCKElementLoadFactor_Type = Integer32
_RsCCKElementLoadFactor_Object = MibTableColumn
rsCCKElementLoadFactor = _RsCCKElementLoadFactor_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 1, 1, 8),
    _RsCCKElementLoadFactor_Type()
)
rsCCKElementLoadFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCCKElementLoadFactor.setStatus("mandatory")
_RsCCKElementUptimePct_Type = Integer32
_RsCCKElementUptimePct_Object = MibTableColumn
rsCCKElementUptimePct = _RsCCKElementUptimePct_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 1, 1, 9),
    _RsCCKElementUptimePct_Type()
)
rsCCKElementUptimePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCCKElementUptimePct.setStatus("mandatory")
_RsCCKElementSuccessCnt_Type = Integer32
_RsCCKElementSuccessCnt_Object = MibTableColumn
rsCCKElementSuccessCnt = _RsCCKElementSuccessCnt_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 1, 1, 10),
    _RsCCKElementSuccessCnt_Type()
)
rsCCKElementSuccessCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCCKElementSuccessCnt.setStatus("mandatory")
_RsCCKElementFailCnt_Type = Integer32
_RsCCKElementFailCnt_Object = MibTableColumn
rsCCKElementFailCnt = _RsCCKElementFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 1, 1, 11),
    _RsCCKElementFailCnt_Type()
)
rsCCKElementFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCCKElementFailCnt.setStatus("mandatory")
_RsCCKHealthChkTable_Object = MibTable
rsCCKHealthChkTable = _RsCCKHealthChkTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 2)
)
if mibBuilder.loadTexts:
    rsCCKHealthChkTable.setStatus("mandatory")
_RsCCKHealthChkEntry_Object = MibTableRow
rsCCKHealthChkEntry = _RsCCKHealthChkEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 2, 1)
)
rsCCKHealthChkEntry.setIndexNames(
    (0, "CCK-MIB", "rsCCKHealthChkName"),
)
if mibBuilder.loadTexts:
    rsCCKHealthChkEntry.setStatus("mandatory")


class _RsCCKHealthChkName_Type(DisplayString):
    """Custom type rsCCKHealthChkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RsCCKHealthChkName_Type.__name__ = "DisplayString"
_RsCCKHealthChkName_Object = MibTableColumn
rsCCKHealthChkName = _RsCCKHealthChkName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 2, 1, 1),
    _RsCCKHealthChkName_Type()
)
rsCCKHealthChkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCCKHealthChkName.setStatus("mandatory")
_RsCCKHealthChkId_Type = Integer32
_RsCCKHealthChkId_Object = MibTableColumn
rsCCKHealthChkId = _RsCCKHealthChkId_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 2, 1, 2),
    _RsCCKHealthChkId_Type()
)
rsCCKHealthChkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKHealthChkId.setStatus("mandatory")
_RsCCKHealthChkMethod_Type = Integer32
_RsCCKHealthChkMethod_Object = MibTableColumn
rsCCKHealthChkMethod = _RsCCKHealthChkMethod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 2, 1, 3),
    _RsCCKHealthChkMethod_Type()
)
rsCCKHealthChkMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKHealthChkMethod.setStatus("mandatory")


class _RsCCKHealthChkStatus_Type(Integer32):
    """Custom type rsCCKHealthChkStatus based on Integer32"""
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
        *(("unknown", 1),
          ("failed", 2),
          ("passed", 3),
          ("nonewsessions", 4))
    )


_RsCCKHealthChkStatus_Type.__name__ = "Integer32"
_RsCCKHealthChkStatus_Object = MibTableColumn
rsCCKHealthChkStatus = _RsCCKHealthChkStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 2, 1, 4),
    _RsCCKHealthChkStatus_Type()
)
rsCCKHealthChkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCCKHealthChkStatus.setStatus("mandatory")
_RsCCKHealthChkDstAddr_Type = IpAddress
_RsCCKHealthChkDstAddr_Object = MibTableColumn
rsCCKHealthChkDstAddr = _RsCCKHealthChkDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 2, 1, 5),
    _RsCCKHealthChkDstAddr_Type()
)
rsCCKHealthChkDstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKHealthChkDstAddr.setStatus("mandatory")
_RsCCKHealthChkNextHop_Type = IpAddress
_RsCCKHealthChkNextHop_Object = MibTableColumn
rsCCKHealthChkNextHop = _RsCCKHealthChkNextHop_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 2, 1, 6),
    _RsCCKHealthChkNextHop_Type()
)
rsCCKHealthChkNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKHealthChkNextHop.setStatus("mandatory")
_RsCCKHealthChkDstPort_Type = Integer32
_RsCCKHealthChkDstPort_Object = MibTableColumn
rsCCKHealthChkDstPort = _RsCCKHealthChkDstPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 2, 1, 7),
    _RsCCKHealthChkDstPort_Type()
)
rsCCKHealthChkDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKHealthChkDstPort.setStatus("mandatory")


class _RsCCKHealthChkArguments_Type(DisplayString):
    """Custom type rsCCKHealthChkArguments based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RsCCKHealthChkArguments_Type.__name__ = "DisplayString"
_RsCCKHealthChkArguments_Object = MibTableColumn
rsCCKHealthChkArguments = _RsCCKHealthChkArguments_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 2, 1, 8),
    _RsCCKHealthChkArguments_Type()
)
rsCCKHealthChkArguments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKHealthChkArguments.setStatus("mandatory")


class _RsCCKHealthChkInterval_Type(Integer32):
    """Custom type rsCCKHealthChkInterval based on Integer32"""
    defaultValue = 10


_RsCCKHealthChkInterval_Type.__name__ = "Integer32"
_RsCCKHealthChkInterval_Object = MibTableColumn
rsCCKHealthChkInterval = _RsCCKHealthChkInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 2, 1, 9),
    _RsCCKHealthChkInterval_Type()
)
rsCCKHealthChkInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKHealthChkInterval.setStatus("mandatory")


class _RsCCKHealthChkRetries_Type(Integer32):
    """Custom type rsCCKHealthChkRetries based on Integer32"""
    defaultValue = 5


_RsCCKHealthChkRetries_Type.__name__ = "Integer32"
_RsCCKHealthChkRetries_Object = MibTableColumn
rsCCKHealthChkRetries = _RsCCKHealthChkRetries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 2, 1, 10),
    _RsCCKHealthChkRetries_Type()
)
rsCCKHealthChkRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKHealthChkRetries.setStatus("mandatory")


class _RsCCKHealthChkTimeout_Type(Integer32):
    """Custom type rsCCKHealthChkTimeout based on Integer32"""
    defaultValue = 5


_RsCCKHealthChkTimeout_Type.__name__ = "Integer32"
_RsCCKHealthChkTimeout_Object = MibTableColumn
rsCCKHealthChkTimeout = _RsCCKHealthChkTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 2, 1, 11),
    _RsCCKHealthChkTimeout_Type()
)
rsCCKHealthChkTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKHealthChkTimeout.setStatus("mandatory")
_RsCCKHealthChkRowStatus_Type = RowStatus
_RsCCKHealthChkRowStatus_Object = MibTableColumn
rsCCKHealthChkRowStatus = _RsCCKHealthChkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 2, 1, 12),
    _RsCCKHealthChkRowStatus_Type()
)
rsCCKHealthChkRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKHealthChkRowStatus.setStatus("mandatory")
_RsCCKHealthChkNNSTimeout_Type = Integer32
_RsCCKHealthChkNNSTimeout_Object = MibTableColumn
rsCCKHealthChkNNSTimeout = _RsCCKHealthChkNNSTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 2, 1, 13),
    _RsCCKHealthChkNNSTimeout_Type()
)
rsCCKHealthChkNNSTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKHealthChkNNSTimeout.setStatus("mandatory")


class _RsCCKHealthChkTrckLoad_Type(Integer32):
    """Custom type rsCCKHealthChkTrckLoad based on Integer32"""
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


_RsCCKHealthChkTrckLoad_Type.__name__ = "Integer32"
_RsCCKHealthChkTrckLoad_Object = MibTableColumn
rsCCKHealthChkTrckLoad = _RsCCKHealthChkTrckLoad_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 2, 1, 14),
    _RsCCKHealthChkTrckLoad_Type()
)
rsCCKHealthChkTrckLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKHealthChkTrckLoad.setStatus("mandatory")
_RsCCKHealthChkLoadFactor_Type = Integer32
_RsCCKHealthChkLoadFactor_Object = MibTableColumn
rsCCKHealthChkLoadFactor = _RsCCKHealthChkLoadFactor_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 2, 1, 15),
    _RsCCKHealthChkLoadFactor_Type()
)
rsCCKHealthChkLoadFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCCKHealthChkLoadFactor.setStatus("mandatory")


class _RsCCKHealthChkRevResult_Type(Integer32):
    """Custom type rsCCKHealthChkRevResult based on Integer32"""
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


_RsCCKHealthChkRevResult_Type.__name__ = "Integer32"
_RsCCKHealthChkRevResult_Object = MibTableColumn
rsCCKHealthChkRevResult = _RsCCKHealthChkRevResult_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 2, 1, 16),
    _RsCCKHealthChkRevResult_Type()
)
rsCCKHealthChkRevResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKHealthChkRevResult.setStatus("mandatory")
_RsCCKHealthChkUptimePct_Type = Integer32
_RsCCKHealthChkUptimePct_Object = MibTableColumn
rsCCKHealthChkUptimePct = _RsCCKHealthChkUptimePct_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 2, 1, 17),
    _RsCCKHealthChkUptimePct_Type()
)
rsCCKHealthChkUptimePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCCKHealthChkUptimePct.setStatus("mandatory")
_RsCCKHealthChkSuccessCnt_Type = Integer32
_RsCCKHealthChkSuccessCnt_Object = MibTableColumn
rsCCKHealthChkSuccessCnt = _RsCCKHealthChkSuccessCnt_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 2, 1, 18),
    _RsCCKHealthChkSuccessCnt_Type()
)
rsCCKHealthChkSuccessCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCCKHealthChkSuccessCnt.setStatus("mandatory")
_RsCCKHealthChkFailCnt_Type = Integer32
_RsCCKHealthChkFailCnt_Object = MibTableColumn
rsCCKHealthChkFailCnt = _RsCCKHealthChkFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 2, 1, 19),
    _RsCCKHealthChkFailCnt_Type()
)
rsCCKHealthChkFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCCKHealthChkFailCnt.setStatus("mandatory")
_RsCCKHealthChkDuration_Type = Integer32
_RsCCKHealthChkDuration_Object = MibTableColumn
rsCCKHealthChkDuration = _RsCCKHealthChkDuration_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 2, 1, 20),
    _RsCCKHealthChkDuration_Type()
)
rsCCKHealthChkDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCCKHealthChkDuration.setStatus("mandatory")


class _RsCCKHealthChkServerSpoof_Type(Integer32):
    """Custom type rsCCKHealthChkServerSpoof based on Integer32"""
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


_RsCCKHealthChkServerSpoof_Type.__name__ = "Integer32"
_RsCCKHealthChkServerSpoof_Object = MibTableColumn
rsCCKHealthChkServerSpoof = _RsCCKHealthChkServerSpoof_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 2, 1, 21),
    _RsCCKHealthChkServerSpoof_Type()
)
rsCCKHealthChkServerSpoof.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKHealthChkServerSpoof.setStatus("mandatory")


class _RsCCKHealthChkDstHost_Type(DisplayString):
    """Custom type rsCCKHealthChkDstHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RsCCKHealthChkDstHost_Type.__name__ = "DisplayString"
_RsCCKHealthChkDstHost_Object = MibTableColumn
rsCCKHealthChkDstHost = _RsCCKHealthChkDstHost_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 2, 1, 22),
    _RsCCKHealthChkDstHost_Type()
)
rsCCKHealthChkDstHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKHealthChkDstHost.setStatus("mandatory")
_RsCCKChkBindingTable_Object = MibTable
rsCCKChkBindingTable = _RsCCKChkBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 3)
)
if mibBuilder.loadTexts:
    rsCCKChkBindingTable.setStatus("mandatory")
_RsCCKChkBindingEntry_Object = MibTableRow
rsCCKChkBindingEntry = _RsCCKChkBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 3, 1)
)
rsCCKChkBindingEntry.setIndexNames(
    (0, "CCK-MIB", "rsCCKChkBindingHealthChk"),
    (0, "CCK-MIB", "rsCCKChkBindingElement"),
)
if mibBuilder.loadTexts:
    rsCCKChkBindingEntry.setStatus("mandatory")
_RsCCKChkBindingHealthChk_Type = Integer32
_RsCCKChkBindingHealthChk_Object = MibTableColumn
rsCCKChkBindingHealthChk = _RsCCKChkBindingHealthChk_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 3, 1, 1),
    _RsCCKChkBindingHealthChk_Type()
)
rsCCKChkBindingHealthChk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCCKChkBindingHealthChk.setStatus("mandatory")
_RsCCKChkBindingElement_Type = Integer32
_RsCCKChkBindingElement_Object = MibTableColumn
rsCCKChkBindingElement = _RsCCKChkBindingElement_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 3, 1, 2),
    _RsCCKChkBindingElement_Type()
)
rsCCKChkBindingElement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCCKChkBindingElement.setStatus("mandatory")
_RsCCKChkBindingGroup_Type = Integer32
_RsCCKChkBindingGroup_Object = MibTableColumn
rsCCKChkBindingGroup = _RsCCKChkBindingGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 3, 1, 3),
    _RsCCKChkBindingGroup_Type()
)
rsCCKChkBindingGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKChkBindingGroup.setStatus("mandatory")


class _RsCCKChkBindingMandatory_Type(Integer32):
    """Custom type rsCCKChkBindingMandatory based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ismandatory", 1),
          ("isnon-mandatory", 2))
    )


_RsCCKChkBindingMandatory_Type.__name__ = "Integer32"
_RsCCKChkBindingMandatory_Object = MibTableColumn
rsCCKChkBindingMandatory = _RsCCKChkBindingMandatory_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 3, 1, 4),
    _RsCCKChkBindingMandatory_Type()
)
rsCCKChkBindingMandatory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKChkBindingMandatory.setStatus("mandatory")
_RsCCKChkBindingRowStatus_Type = RowStatus
_RsCCKChkBindingRowStatus_Object = MibTableColumn
rsCCKChkBindingRowStatus = _RsCCKChkBindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 3, 1, 5),
    _RsCCKChkBindingRowStatus_Type()
)
rsCCKChkBindingRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKChkBindingRowStatus.setStatus("mandatory")
_RsCCKChkMethodTable_Object = MibTable
rsCCKChkMethodTable = _RsCCKChkMethodTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 4)
)
if mibBuilder.loadTexts:
    rsCCKChkMethodTable.setStatus("mandatory")
_RsCCKChkMethodEntry_Object = MibTableRow
rsCCKChkMethodEntry = _RsCCKChkMethodEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 4, 1)
)
rsCCKChkMethodEntry.setIndexNames(
    (0, "CCK-MIB", "rsCCKChkMethodId"),
)
if mibBuilder.loadTexts:
    rsCCKChkMethodEntry.setStatus("mandatory")
_RsCCKChkMethodId_Type = Integer32
_RsCCKChkMethodId_Object = MibTableColumn
rsCCKChkMethodId = _RsCCKChkMethodId_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 4, 1, 1),
    _RsCCKChkMethodId_Type()
)
rsCCKChkMethodId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCCKChkMethodId.setStatus("mandatory")


class _RsCCKChkMethodDescription_Type(DisplayString):
    """Custom type rsCCKChkMethodDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RsCCKChkMethodDescription_Type.__name__ = "DisplayString"
_RsCCKChkMethodDescription_Object = MibTableColumn
rsCCKChkMethodDescription = _RsCCKChkMethodDescription_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 4, 1, 2),
    _RsCCKChkMethodDescription_Type()
)
rsCCKChkMethodDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCCKChkMethodDescription.setStatus("mandatory")
_RsCCKChkMethodRowStatus_Type = RowStatus
_RsCCKChkMethodRowStatus_Object = MibTableColumn
rsCCKChkMethodRowStatus = _RsCCKChkMethodRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 4, 1, 3),
    _RsCCKChkMethodRowStatus_Type()
)
rsCCKChkMethodRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCCKChkMethodRowStatus.setStatus("mandatory")
_RsCCKPktSequenceTable_Object = MibTable
rsCCKPktSequenceTable = _RsCCKPktSequenceTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 5)
)
if mibBuilder.loadTexts:
    rsCCKPktSequenceTable.setStatus("mandatory")
_RsCCKPktSequenceEntry_Object = MibTableRow
rsCCKPktSequenceEntry = _RsCCKPktSequenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 5, 1)
)
rsCCKPktSequenceEntry.setIndexNames(
    (0, "CCK-MIB", "rsCCKPktSequenceSeqId"),
    (0, "CCK-MIB", "rsCCKPktSequencePktId"),
)
if mibBuilder.loadTexts:
    rsCCKPktSequenceEntry.setStatus("mandatory")
_RsCCKPktSequenceSeqId_Type = Integer32
_RsCCKPktSequenceSeqId_Object = MibTableColumn
rsCCKPktSequenceSeqId = _RsCCKPktSequenceSeqId_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 5, 1, 1),
    _RsCCKPktSequenceSeqId_Type()
)
rsCCKPktSequenceSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCCKPktSequenceSeqId.setStatus("mandatory")
_RsCCKPktSequencePktId_Type = Integer32
_RsCCKPktSequencePktId_Object = MibTableColumn
rsCCKPktSequencePktId = _RsCCKPktSequencePktId_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 5, 1, 2),
    _RsCCKPktSequencePktId_Type()
)
rsCCKPktSequencePktId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCCKPktSequencePktId.setStatus("mandatory")


class _RsCCKPktSequenceType_Type(Integer32):
    """Custom type rsCCKPktSequenceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("send", 1),
          ("recieve", 2))
    )


_RsCCKPktSequenceType_Type.__name__ = "Integer32"
_RsCCKPktSequenceType_Object = MibTableColumn
rsCCKPktSequenceType = _RsCCKPktSequenceType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 5, 1, 3),
    _RsCCKPktSequenceType_Type()
)
rsCCKPktSequenceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKPktSequenceType.setStatus("mandatory")


class _RsCCKPktSequenceString_Type(DisplayString):
    """Custom type rsCCKPktSequenceString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RsCCKPktSequenceString_Type.__name__ = "DisplayString"
_RsCCKPktSequenceString_Object = MibTableColumn
rsCCKPktSequenceString = _RsCCKPktSequenceString_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 5, 1, 4),
    _RsCCKPktSequenceString_Type()
)
rsCCKPktSequenceString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKPktSequenceString.setStatus("mandatory")


class _RsCCKPktSequenceDescription_Type(DisplayString):
    """Custom type rsCCKPktSequenceDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RsCCKPktSequenceDescription_Type.__name__ = "DisplayString"
_RsCCKPktSequenceDescription_Object = MibTableColumn
rsCCKPktSequenceDescription = _RsCCKPktSequenceDescription_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 5, 1, 5),
    _RsCCKPktSequenceDescription_Type()
)
rsCCKPktSequenceDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKPktSequenceDescription.setStatus("mandatory")
_RsCCKPktSequenceRowStatus_Type = RowStatus
_RsCCKPktSequenceRowStatus_Object = MibTableColumn
rsCCKPktSequenceRowStatus = _RsCCKPktSequenceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 5, 1, 6),
    _RsCCKPktSequenceRowStatus_Type()
)
rsCCKPktSequenceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKPktSequenceRowStatus.setStatus("mandatory")


class _RsCCKPktSequenceCompareMtd_Type(Integer32):
    """Custom type rsCCKPktSequenceCompareMtd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("regex", 1),
          ("binary", 2))
    )


_RsCCKPktSequenceCompareMtd_Type.__name__ = "Integer32"
_RsCCKPktSequenceCompareMtd_Object = MibTableColumn
rsCCKPktSequenceCompareMtd = _RsCCKPktSequenceCompareMtd_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 5, 1, 7),
    _RsCCKPktSequenceCompareMtd_Type()
)
rsCCKPktSequenceCompareMtd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKPktSequenceCompareMtd.setStatus("mandatory")


class _RsCCKArgDelimiter_Type(DisplayString):
    """Custom type rsCCKArgDelimiter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_RsCCKArgDelimiter_Type.__name__ = "DisplayString"
_RsCCKArgDelimiter_Object = MibScalar
rsCCKArgDelimiter = _RsCCKArgDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 6),
    _RsCCKArgDelimiter_Type()
)
rsCCKArgDelimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKArgDelimiter.setStatus("mandatory")
_RsCCKNextElementId_Type = Integer32
_RsCCKNextElementId_Object = MibScalar
rsCCKNextElementId = _RsCCKNextElementId_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 7),
    _RsCCKNextElementId_Type()
)
rsCCKNextElementId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKNextElementId.setStatus("mandatory")
_RsCCKNextCheckId_Type = Integer32
_RsCCKNextCheckId_Object = MibScalar
rsCCKNextCheckId = _RsCCKNextCheckId_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 8),
    _RsCCKNextCheckId_Type()
)
rsCCKNextCheckId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKNextCheckId.setStatus("mandatory")


class _RsCCKStatus_Type(Integer32):
    """Custom type rsCCKStatus based on Integer32"""
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


_RsCCKStatus_Type.__name__ = "Integer32"
_RsCCKStatus_Object = MibScalar
rsCCKStatus = _RsCCKStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 9),
    _RsCCKStatus_Type()
)
rsCCKStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKStatus.setStatus("mandatory")


class _RsCCKLoadSamples_Type(Integer32):
    """Custom type rsCCKLoadSamples based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_RsCCKLoadSamples_Type.__name__ = "Integer32"
_RsCCKLoadSamples_Object = MibScalar
rsCCKLoadSamples = _RsCCKLoadSamples_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 10),
    _RsCCKLoadSamples_Type()
)
rsCCKLoadSamples.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKLoadSamples.setStatus("mandatory")


class _RsCCKCertFile_Type(DisplayString):
    """Custom type rsCCKCertFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_RsCCKCertFile_Type.__name__ = "DisplayString"
_RsCCKCertFile_Object = MibScalar
rsCCKCertFile = _RsCCKCertFile_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 11),
    _RsCCKCertFile_Type()
)
rsCCKCertFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKCertFile.setStatus("mandatory")


class _RsCCKKeyFile_Type(DisplayString):
    """Custom type rsCCKKeyFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_RsCCKKeyFile_Type.__name__ = "DisplayString"
_RsCCKKeyFile_Object = MibScalar
rsCCKKeyFile = _RsCCKKeyFile_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 12),
    _RsCCKKeyFile_Type()
)
rsCCKKeyFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKKeyFile.setStatus("mandatory")
_RsCCKDiameterArgsTable_Object = MibTable
rsCCKDiameterArgsTable = _RsCCKDiameterArgsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 13)
)
if mibBuilder.loadTexts:
    rsCCKDiameterArgsTable.setStatus("mandatory")
_RsCCKDiameterArgsEntry_Object = MibTableRow
rsCCKDiameterArgsEntry = _RsCCKDiameterArgsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 13, 1)
)
rsCCKDiameterArgsEntry.setIndexNames(
    (0, "CCK-MIB", "rsCCKDiameterArgsName"),
)
if mibBuilder.loadTexts:
    rsCCKDiameterArgsEntry.setStatus("mandatory")
_RsCCKDiameterArgsName_Type = DisplayString
_RsCCKDiameterArgsName_Object = MibTableColumn
rsCCKDiameterArgsName = _RsCCKDiameterArgsName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 13, 1, 1),
    _RsCCKDiameterArgsName_Type()
)
rsCCKDiameterArgsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKDiameterArgsName.setStatus("mandatory")
_RsCCKDiameterArgsOriginHost_Type = DisplayString
_RsCCKDiameterArgsOriginHost_Object = MibTableColumn
rsCCKDiameterArgsOriginHost = _RsCCKDiameterArgsOriginHost_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 13, 1, 2),
    _RsCCKDiameterArgsOriginHost_Type()
)
rsCCKDiameterArgsOriginHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKDiameterArgsOriginHost.setStatus("mandatory")
_RsCCKDiameterArgsOriginRealm_Type = DisplayString
_RsCCKDiameterArgsOriginRealm_Object = MibTableColumn
rsCCKDiameterArgsOriginRealm = _RsCCKDiameterArgsOriginRealm_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 13, 1, 3),
    _RsCCKDiameterArgsOriginRealm_Type()
)
rsCCKDiameterArgsOriginRealm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKDiameterArgsOriginRealm.setStatus("mandatory")
_RsCCKDiameterArgsProductName_Type = DisplayString
_RsCCKDiameterArgsProductName_Object = MibTableColumn
rsCCKDiameterArgsProductName = _RsCCKDiameterArgsProductName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 13, 1, 4),
    _RsCCKDiameterArgsProductName_Type()
)
rsCCKDiameterArgsProductName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKDiameterArgsProductName.setStatus("mandatory")


class _RsCCKDiameterArgsAuthAppID_Type(Unsigned32):
    """Custom type rsCCKDiameterArgsAuthAppID based on Unsigned32"""
    defaultValue = 0


_RsCCKDiameterArgsAuthAppID_Type.__name__ = "Unsigned32"
_RsCCKDiameterArgsAuthAppID_Object = MibTableColumn
rsCCKDiameterArgsAuthAppID = _RsCCKDiameterArgsAuthAppID_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 13, 1, 5),
    _RsCCKDiameterArgsAuthAppID_Type()
)
rsCCKDiameterArgsAuthAppID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKDiameterArgsAuthAppID.setStatus("optional")


class _RsCCKDiameterArgsAuthSessState_Type(Integer32):
    """Custom type rsCCKDiameterArgsAuthSessState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("state-maintained", 0),
          ("no-state-maintained", 1))
    )


_RsCCKDiameterArgsAuthSessState_Type.__name__ = "Integer32"
_RsCCKDiameterArgsAuthSessState_Object = MibTableColumn
rsCCKDiameterArgsAuthSessState = _RsCCKDiameterArgsAuthSessState_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 13, 1, 6),
    _RsCCKDiameterArgsAuthSessState_Type()
)
rsCCKDiameterArgsAuthSessState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKDiameterArgsAuthSessState.setStatus("optional")


class _RsCCKDiameterArgsDestRealm_Type(DisplayString):
    """Custom type rsCCKDiameterArgsDestRealm based on DisplayString"""
    defaultValue = OctetString("")


_RsCCKDiameterArgsDestRealm_Type.__name__ = "DisplayString"
_RsCCKDiameterArgsDestRealm_Object = MibTableColumn
rsCCKDiameterArgsDestRealm = _RsCCKDiameterArgsDestRealm_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 13, 1, 7),
    _RsCCKDiameterArgsDestRealm_Type()
)
rsCCKDiameterArgsDestRealm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKDiameterArgsDestRealm.setStatus("optional")


class _RsCCKDiameterArgsDestHost_Type(DisplayString):
    """Custom type rsCCKDiameterArgsDestHost based on DisplayString"""
    defaultValue = OctetString("")


_RsCCKDiameterArgsDestHost_Type.__name__ = "DisplayString"
_RsCCKDiameterArgsDestHost_Object = MibTableColumn
rsCCKDiameterArgsDestHost = _RsCCKDiameterArgsDestHost_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 13, 1, 8),
    _RsCCKDiameterArgsDestHost_Type()
)
rsCCKDiameterArgsDestHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKDiameterArgsDestHost.setStatus("optional")


class _RsCCKDiameterArgsPublicID_Type(DisplayString):
    """Custom type rsCCKDiameterArgsPublicID based on DisplayString"""
    defaultValue = OctetString("")


_RsCCKDiameterArgsPublicID_Type.__name__ = "DisplayString"
_RsCCKDiameterArgsPublicID_Object = MibTableColumn
rsCCKDiameterArgsPublicID = _RsCCKDiameterArgsPublicID_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 13, 1, 9),
    _RsCCKDiameterArgsPublicID_Type()
)
rsCCKDiameterArgsPublicID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKDiameterArgsPublicID.setStatus("optional")


class _RsCCKDiameterArgsDisconnectCause_Type(Integer32):
    """Custom type rsCCKDiameterArgsDisconnectCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rebooting", 0),
          ("busy", 1),
          ("do-not-want-to-talk-to-you", 2))
    )


_RsCCKDiameterArgsDisconnectCause_Type.__name__ = "Integer32"
_RsCCKDiameterArgsDisconnectCause_Object = MibTableColumn
rsCCKDiameterArgsDisconnectCause = _RsCCKDiameterArgsDisconnectCause_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 13, 1, 10),
    _RsCCKDiameterArgsDisconnectCause_Type()
)
rsCCKDiameterArgsDisconnectCause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKDiameterArgsDisconnectCause.setStatus("mandatory")


class _RsCCKDiameterArgsAppMessType_Type(Integer32):
    """Custom type rsCCKDiameterArgsAppMessType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lir", 0),
          ("user-defined", 1),
          ("none", 2))
    )


_RsCCKDiameterArgsAppMessType_Type.__name__ = "Integer32"
_RsCCKDiameterArgsAppMessType_Object = MibTableColumn
rsCCKDiameterArgsAppMessType = _RsCCKDiameterArgsAppMessType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 13, 1, 11),
    _RsCCKDiameterArgsAppMessType_Type()
)
rsCCKDiameterArgsAppMessType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKDiameterArgsAppMessType.setStatus("mandatory")


class _RsCCKDiameterArgsAppMessPresent_Type(Integer32):
    """Custom type rsCCKDiameterArgsAppMessPresent based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2),
          ("na", 3))
    )


_RsCCKDiameterArgsAppMessPresent_Type.__name__ = "Integer32"
_RsCCKDiameterArgsAppMessPresent_Object = MibTableColumn
rsCCKDiameterArgsAppMessPresent = _RsCCKDiameterArgsAppMessPresent_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 13, 1, 12),
    _RsCCKDiameterArgsAppMessPresent_Type()
)
rsCCKDiameterArgsAppMessPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCCKDiameterArgsAppMessPresent.setStatus("mandatory")


class _RsCCKDiameterArgsDescription_Type(DisplayString):
    """Custom type rsCCKDiameterArgsDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RsCCKDiameterArgsDescription_Type.__name__ = "DisplayString"
_RsCCKDiameterArgsDescription_Object = MibTableColumn
rsCCKDiameterArgsDescription = _RsCCKDiameterArgsDescription_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 13, 1, 13),
    _RsCCKDiameterArgsDescription_Type()
)
rsCCKDiameterArgsDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKDiameterArgsDescription.setStatus("mandatory")


class _RsCCKDiameterArgsResultCodes_Type(DisplayString):
    """Custom type rsCCKDiameterArgsResultCodes based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RsCCKDiameterArgsResultCodes_Type.__name__ = "DisplayString"
_RsCCKDiameterArgsResultCodes_Object = MibTableColumn
rsCCKDiameterArgsResultCodes = _RsCCKDiameterArgsResultCodes_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 13, 1, 14),
    _RsCCKDiameterArgsResultCodes_Type()
)
rsCCKDiameterArgsResultCodes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKDiameterArgsResultCodes.setStatus("mandatory")
_RsCCKDiameterArgsVendorID_Type = Unsigned32
_RsCCKDiameterArgsVendorID_Object = MibTableColumn
rsCCKDiameterArgsVendorID = _RsCCKDiameterArgsVendorID_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 13, 1, 15),
    _RsCCKDiameterArgsVendorID_Type()
)
rsCCKDiameterArgsVendorID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKDiameterArgsVendorID.setStatus("mandatory")
_RsCCKDiameterArgsRowStatus_Type = RowStatus
_RsCCKDiameterArgsRowStatus_Object = MibTableColumn
rsCCKDiameterArgsRowStatus = _RsCCKDiameterArgsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 13, 1, 16),
    _RsCCKDiameterArgsRowStatus_Type()
)
rsCCKDiameterArgsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKDiameterArgsRowStatus.setStatus("mandatory")
_RsCCKDiameterBinaryFileTable_Object = MibTable
rsCCKDiameterBinaryFileTable = _RsCCKDiameterBinaryFileTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 14)
)
if mibBuilder.loadTexts:
    rsCCKDiameterBinaryFileTable.setStatus("mandatory")
_RsCCKDiameterBinaryFileEntry_Object = MibTableRow
rsCCKDiameterBinaryFileEntry = _RsCCKDiameterBinaryFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 14, 1)
)
rsCCKDiameterBinaryFileEntry.setIndexNames(
    (0, "CCK-MIB", "rsCCKDiameterBinaryFileArgsSetName"),
)
if mibBuilder.loadTexts:
    rsCCKDiameterBinaryFileEntry.setStatus("mandatory")
_RsCCKDiameterBinaryFileArgsSetName_Type = DisplayString
_RsCCKDiameterBinaryFileArgsSetName_Object = MibTableColumn
rsCCKDiameterBinaryFileArgsSetName = _RsCCKDiameterBinaryFileArgsSetName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 14, 1, 1),
    _RsCCKDiameterBinaryFileArgsSetName_Type()
)
rsCCKDiameterBinaryFileArgsSetName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKDiameterBinaryFileArgsSetName.setStatus("mandatory")
_RsCCKDiameterBinaryFileData1_Type = DisplayString
_RsCCKDiameterBinaryFileData1_Object = MibTableColumn
rsCCKDiameterBinaryFileData1 = _RsCCKDiameterBinaryFileData1_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 14, 1, 2),
    _RsCCKDiameterBinaryFileData1_Type()
)
rsCCKDiameterBinaryFileData1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKDiameterBinaryFileData1.setStatus("mandatory")
_RsCCKDiameterBinaryFileData2_Type = DisplayString
_RsCCKDiameterBinaryFileData2_Object = MibTableColumn
rsCCKDiameterBinaryFileData2 = _RsCCKDiameterBinaryFileData2_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 14, 1, 3),
    _RsCCKDiameterBinaryFileData2_Type()
)
rsCCKDiameterBinaryFileData2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKDiameterBinaryFileData2.setStatus("mandatory")
_RsCCKDiameterBinaryFileData3_Type = DisplayString
_RsCCKDiameterBinaryFileData3_Object = MibTableColumn
rsCCKDiameterBinaryFileData3 = _RsCCKDiameterBinaryFileData3_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 14, 1, 4),
    _RsCCKDiameterBinaryFileData3_Type()
)
rsCCKDiameterBinaryFileData3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKDiameterBinaryFileData3.setStatus("mandatory")
_RsCCKDiameterBinaryFileData4_Type = DisplayString
_RsCCKDiameterBinaryFileData4_Object = MibTableColumn
rsCCKDiameterBinaryFileData4 = _RsCCKDiameterBinaryFileData4_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 14, 1, 5),
    _RsCCKDiameterBinaryFileData4_Type()
)
rsCCKDiameterBinaryFileData4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKDiameterBinaryFileData4.setStatus("mandatory")
_RsCCKDiameterBinaryFileTotalLength_Type = Unsigned32
_RsCCKDiameterBinaryFileTotalLength_Object = MibTableColumn
rsCCKDiameterBinaryFileTotalLength = _RsCCKDiameterBinaryFileTotalLength_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 14, 1, 6),
    _RsCCKDiameterBinaryFileTotalLength_Type()
)
rsCCKDiameterBinaryFileTotalLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKDiameterBinaryFileTotalLength.setStatus("mandatory")
_RsCCKDiameterBinaryFileRowStatus_Type = RowStatus
_RsCCKDiameterBinaryFileRowStatus_Object = MibTableColumn
rsCCKDiameterBinaryFileRowStatus = _RsCCKDiameterBinaryFileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 14, 1, 7),
    _RsCCKDiameterBinaryFileRowStatus_Type()
)
rsCCKDiameterBinaryFileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKDiameterBinaryFileRowStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects

rsCCKElemIsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 0, 1)
)
rsCCKElemIsUp.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsCCKElemIsUp.setStatus(
        ""
    )

rsCCKElemIsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 0, 2)
)
rsCCKElemIsDown.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsCCKElemIsDown.setStatus(
        ""
    )

rsCCKElemIsNNS = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 0, 3)
)
rsCCKElemIsNNS.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsCCKElemIsNNS.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CCK-MIB",
    **{"NetNumber": NetNumber,
       "rsCCKElemIsUp": rsCCKElemIsUp,
       "rsCCKElemIsDown": rsCCKElemIsDown,
       "rsCCKElemIsNNS": rsCCKElemIsNNS,
       "rsCCKElementTable": rsCCKElementTable,
       "rsCCKElementEntry": rsCCKElementEntry,
       "rsCCKElementId": rsCCKElementId,
       "rsCCKElementDescription": rsCCKElementDescription,
       "rsCCKElementGroup": rsCCKElementGroup,
       "rsCCKElementIsActive": rsCCKElementIsActive,
       "rsCCKElementIsAvailable": rsCCKElementIsAvailable,
       "rsCCKElementDftAddr": rsCCKElementDftAddr,
       "rsCCKElementRowStatus": rsCCKElementRowStatus,
       "rsCCKElementLoadFactor": rsCCKElementLoadFactor,
       "rsCCKElementUptimePct": rsCCKElementUptimePct,
       "rsCCKElementSuccessCnt": rsCCKElementSuccessCnt,
       "rsCCKElementFailCnt": rsCCKElementFailCnt,
       "rsCCKHealthChkTable": rsCCKHealthChkTable,
       "rsCCKHealthChkEntry": rsCCKHealthChkEntry,
       "rsCCKHealthChkName": rsCCKHealthChkName,
       "rsCCKHealthChkId": rsCCKHealthChkId,
       "rsCCKHealthChkMethod": rsCCKHealthChkMethod,
       "rsCCKHealthChkStatus": rsCCKHealthChkStatus,
       "rsCCKHealthChkDstAddr": rsCCKHealthChkDstAddr,
       "rsCCKHealthChkNextHop": rsCCKHealthChkNextHop,
       "rsCCKHealthChkDstPort": rsCCKHealthChkDstPort,
       "rsCCKHealthChkArguments": rsCCKHealthChkArguments,
       "rsCCKHealthChkInterval": rsCCKHealthChkInterval,
       "rsCCKHealthChkRetries": rsCCKHealthChkRetries,
       "rsCCKHealthChkTimeout": rsCCKHealthChkTimeout,
       "rsCCKHealthChkRowStatus": rsCCKHealthChkRowStatus,
       "rsCCKHealthChkNNSTimeout": rsCCKHealthChkNNSTimeout,
       "rsCCKHealthChkTrckLoad": rsCCKHealthChkTrckLoad,
       "rsCCKHealthChkLoadFactor": rsCCKHealthChkLoadFactor,
       "rsCCKHealthChkRevResult": rsCCKHealthChkRevResult,
       "rsCCKHealthChkUptimePct": rsCCKHealthChkUptimePct,
       "rsCCKHealthChkSuccessCnt": rsCCKHealthChkSuccessCnt,
       "rsCCKHealthChkFailCnt": rsCCKHealthChkFailCnt,
       "rsCCKHealthChkDuration": rsCCKHealthChkDuration,
       "rsCCKHealthChkServerSpoof": rsCCKHealthChkServerSpoof,
       "rsCCKHealthChkDstHost": rsCCKHealthChkDstHost,
       "rsCCKChkBindingTable": rsCCKChkBindingTable,
       "rsCCKChkBindingEntry": rsCCKChkBindingEntry,
       "rsCCKChkBindingHealthChk": rsCCKChkBindingHealthChk,
       "rsCCKChkBindingElement": rsCCKChkBindingElement,
       "rsCCKChkBindingGroup": rsCCKChkBindingGroup,
       "rsCCKChkBindingMandatory": rsCCKChkBindingMandatory,
       "rsCCKChkBindingRowStatus": rsCCKChkBindingRowStatus,
       "rsCCKChkMethodTable": rsCCKChkMethodTable,
       "rsCCKChkMethodEntry": rsCCKChkMethodEntry,
       "rsCCKChkMethodId": rsCCKChkMethodId,
       "rsCCKChkMethodDescription": rsCCKChkMethodDescription,
       "rsCCKChkMethodRowStatus": rsCCKChkMethodRowStatus,
       "rsCCKPktSequenceTable": rsCCKPktSequenceTable,
       "rsCCKPktSequenceEntry": rsCCKPktSequenceEntry,
       "rsCCKPktSequenceSeqId": rsCCKPktSequenceSeqId,
       "rsCCKPktSequencePktId": rsCCKPktSequencePktId,
       "rsCCKPktSequenceType": rsCCKPktSequenceType,
       "rsCCKPktSequenceString": rsCCKPktSequenceString,
       "rsCCKPktSequenceDescription": rsCCKPktSequenceDescription,
       "rsCCKPktSequenceRowStatus": rsCCKPktSequenceRowStatus,
       "rsCCKPktSequenceCompareMtd": rsCCKPktSequenceCompareMtd,
       "rsCCKArgDelimiter": rsCCKArgDelimiter,
       "rsCCKNextElementId": rsCCKNextElementId,
       "rsCCKNextCheckId": rsCCKNextCheckId,
       "rsCCKStatus": rsCCKStatus,
       "rsCCKLoadSamples": rsCCKLoadSamples,
       "rsCCKCertFile": rsCCKCertFile,
       "rsCCKKeyFile": rsCCKKeyFile,
       "rsCCKDiameterArgsTable": rsCCKDiameterArgsTable,
       "rsCCKDiameterArgsEntry": rsCCKDiameterArgsEntry,
       "rsCCKDiameterArgsName": rsCCKDiameterArgsName,
       "rsCCKDiameterArgsOriginHost": rsCCKDiameterArgsOriginHost,
       "rsCCKDiameterArgsOriginRealm": rsCCKDiameterArgsOriginRealm,
       "rsCCKDiameterArgsProductName": rsCCKDiameterArgsProductName,
       "rsCCKDiameterArgsAuthAppID": rsCCKDiameterArgsAuthAppID,
       "rsCCKDiameterArgsAuthSessState": rsCCKDiameterArgsAuthSessState,
       "rsCCKDiameterArgsDestRealm": rsCCKDiameterArgsDestRealm,
       "rsCCKDiameterArgsDestHost": rsCCKDiameterArgsDestHost,
       "rsCCKDiameterArgsPublicID": rsCCKDiameterArgsPublicID,
       "rsCCKDiameterArgsDisconnectCause": rsCCKDiameterArgsDisconnectCause,
       "rsCCKDiameterArgsAppMessType": rsCCKDiameterArgsAppMessType,
       "rsCCKDiameterArgsAppMessPresent": rsCCKDiameterArgsAppMessPresent,
       "rsCCKDiameterArgsDescription": rsCCKDiameterArgsDescription,
       "rsCCKDiameterArgsResultCodes": rsCCKDiameterArgsResultCodes,
       "rsCCKDiameterArgsVendorID": rsCCKDiameterArgsVendorID,
       "rsCCKDiameterArgsRowStatus": rsCCKDiameterArgsRowStatus,
       "rsCCKDiameterBinaryFileTable": rsCCKDiameterBinaryFileTable,
       "rsCCKDiameterBinaryFileEntry": rsCCKDiameterBinaryFileEntry,
       "rsCCKDiameterBinaryFileArgsSetName": rsCCKDiameterBinaryFileArgsSetName,
       "rsCCKDiameterBinaryFileData1": rsCCKDiameterBinaryFileData1,
       "rsCCKDiameterBinaryFileData2": rsCCKDiameterBinaryFileData2,
       "rsCCKDiameterBinaryFileData3": rsCCKDiameterBinaryFileData3,
       "rsCCKDiameterBinaryFileData4": rsCCKDiameterBinaryFileData4,
       "rsCCKDiameterBinaryFileTotalLength": rsCCKDiameterBinaryFileTotalLength,
       "rsCCKDiameterBinaryFileRowStatus": rsCCKDiameterBinaryFileRowStatus}
)
