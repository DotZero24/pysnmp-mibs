# SNMP MIB module (ARICENT-PROP-PBB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-PROP-PBB-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:43:29 2025
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

(PriorityCodePoint,) = mibBuilder.importSymbols(
    "ARICENT-DOT1AD-MIB",
    "PriorityCodePoint")

(fsPbbCBPServiceMappingBackboneSid,
 fsPbbPipIfIndex) = mibBuilder.importSymbols(
    "ARICENT-PBB-MIB",
    "fsPbbCBPServiceMappingBackboneSid",
    "fsPbbPipIfIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

aricentProviderBackboneBridgeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15)
)
if mibBuilder.loadTexts:
    aricentProviderBackboneBridgeMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsPbbSystem_ObjectIdentity = ObjectIdentity
fsPbbSystem = _FsPbbSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 1)
)


class _FsPbbShutdownStatus_Type(Integer32):
    """Custom type fsPbbShutdownStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("shutdown", 2))
    )


_FsPbbShutdownStatus_Type.__name__ = "Integer32"
_FsPbbShutdownStatus_Object = MibScalar
fsPbbShutdownStatus = _FsPbbShutdownStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 1, 1),
    _FsPbbShutdownStatus_Type()
)
fsPbbShutdownStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbbShutdownStatus.setStatus("current")


class _FsPbbGlbOUI_Type(OctetString):
    """Custom type fsPbbGlbOUI based on OctetString"""
    defaultValue = OctetString("00:1E:83")


_FsPbbGlbOUI_Type.__name__ = "OctetString"
_FsPbbGlbOUI_Object = MibScalar
fsPbbGlbOUI = _FsPbbGlbOUI_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 1, 2),
    _FsPbbGlbOUI_Type()
)
fsPbbGlbOUI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbbGlbOUI.setStatus("current")


class _FsPbbMaxNoOfISID_Type(Integer32):
    """Custom type fsPbbMaxNoOfISID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777214),
    )


_FsPbbMaxNoOfISID_Type.__name__ = "Integer32"
_FsPbbMaxNoOfISID_Object = MibScalar
fsPbbMaxNoOfISID = _FsPbbMaxNoOfISID_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 1, 3),
    _FsPbbMaxNoOfISID_Type()
)
fsPbbMaxNoOfISID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbbMaxNoOfISID.setStatus("deprecated")
_FsPbbMaxNoOfISIDPerContext_Type = Integer32
_FsPbbMaxNoOfISIDPerContext_Object = MibScalar
fsPbbMaxNoOfISIDPerContext = _FsPbbMaxNoOfISIDPerContext_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 1, 4),
    _FsPbbMaxNoOfISIDPerContext_Type()
)
fsPbbMaxNoOfISIDPerContext.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbbMaxNoOfISIDPerContext.setStatus("deprecated")
_FsPbbMaxPortsPerISID_Type = Integer32
_FsPbbMaxPortsPerISID_Object = MibScalar
fsPbbMaxPortsPerISID = _FsPbbMaxPortsPerISID_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 1, 5),
    _FsPbbMaxPortsPerISID_Type()
)
fsPbbMaxPortsPerISID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbbMaxPortsPerISID.setStatus("deprecated")
_FsPbbMaxPortsPerISIDPerContext_Type = Integer32
_FsPbbMaxPortsPerISIDPerContext_Object = MibScalar
fsPbbMaxPortsPerISIDPerContext = _FsPbbMaxPortsPerISIDPerContext_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 1, 6),
    _FsPbbMaxPortsPerISIDPerContext_Type()
)
fsPbbMaxPortsPerISIDPerContext.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbbMaxPortsPerISIDPerContext.setStatus("deprecated")
_FsPbbMaxCurrentNoOfISID_Type = Integer32
_FsPbbMaxCurrentNoOfISID_Object = MibScalar
fsPbbMaxCurrentNoOfISID = _FsPbbMaxCurrentNoOfISID_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 1, 7),
    _FsPbbMaxCurrentNoOfISID_Type()
)
fsPbbMaxCurrentNoOfISID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbbMaxCurrentNoOfISID.setStatus("deprecated")
_FsPbbMaxCurrentISIDPerContext_Type = Integer32
_FsPbbMaxCurrentISIDPerContext_Object = MibScalar
fsPbbMaxCurrentISIDPerContext = _FsPbbMaxCurrentISIDPerContext_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 1, 8),
    _FsPbbMaxCurrentISIDPerContext_Type()
)
fsPbbMaxCurrentISIDPerContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbbMaxCurrentISIDPerContext.setStatus("deprecated")
_FsPbbMaxCurrentPortsPerISID_Type = Integer32
_FsPbbMaxCurrentPortsPerISID_Object = MibScalar
fsPbbMaxCurrentPortsPerISID = _FsPbbMaxCurrentPortsPerISID_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 1, 9),
    _FsPbbMaxCurrentPortsPerISID_Type()
)
fsPbbMaxCurrentPortsPerISID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbbMaxCurrentPortsPerISID.setStatus("deprecated")
_FsPbbMaxCurrPortsPerISIDContext_Type = Integer32
_FsPbbMaxCurrPortsPerISIDContext_Object = MibScalar
fsPbbMaxCurrPortsPerISIDContext = _FsPbbMaxCurrPortsPerISIDContext_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 1, 10),
    _FsPbbMaxCurrPortsPerISIDContext_Type()
)
fsPbbMaxCurrPortsPerISIDContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbbMaxCurrPortsPerISIDContext.setStatus("deprecated")


class _FsPbbTraceInput_Type(DisplayString):
    """Custom type fsPbbTraceInput based on DisplayString"""
    defaultValue = OctetString("critical")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 288),
    )


_FsPbbTraceInput_Type.__name__ = "DisplayString"
_FsPbbTraceInput_Object = MibScalar
fsPbbTraceInput = _FsPbbTraceInput_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 1, 11),
    _FsPbbTraceInput_Type()
)
fsPbbTraceInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbbTraceInput.setStatus("current")


class _FsPbbTraceOption_Type(Integer32):
    """Custom type fsPbbTraceOption based on Integer32"""
    defaultValue = 256


_FsPbbTraceOption_Type.__name__ = "Integer32"
_FsPbbTraceOption_Object = MibScalar
fsPbbTraceOption = _FsPbbTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 1, 12),
    _FsPbbTraceOption_Type()
)
fsPbbTraceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbbTraceOption.setStatus("current")
_FsPbbISIDConfig_ObjectIdentity = ObjectIdentity
fsPbbISIDConfig = _FsPbbISIDConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 2)
)
_FsPbbISIDOUITable_Object = MibTable
fsPbbISIDOUITable = _FsPbbISIDOUITable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 2, 1)
)
if mibBuilder.loadTexts:
    fsPbbISIDOUITable.setStatus("current")
_FsPbbISIDOUIEntry_Object = MibTableRow
fsPbbISIDOUIEntry = _FsPbbISIDOUIEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 2, 1, 1)
)
fsPbbISIDOUIEntry.setIndexNames(
    (0, "ARICENT-PROP-PBB-MIB", "fsPbbContextId"),
    (0, "ARICENT-PBB-MIB", "fsPbbCBPServiceMappingBackboneSid"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsPbbISIDOUIEntry.setStatus("current")


class _FsPbbContextId_Type(Integer32):
    """Custom type fsPbbContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsPbbContextId_Type.__name__ = "Integer32"
_FsPbbContextId_Object = MibTableColumn
fsPbbContextId = _FsPbbContextId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 2, 1, 1, 1),
    _FsPbbContextId_Type()
)
fsPbbContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPbbContextId.setStatus("current")
_FsPbbOUI_Type = OctetString
_FsPbbOUI_Object = MibTableColumn
fsPbbOUI = _FsPbbOUI_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 2, 1, 1, 2),
    _FsPbbOUI_Type()
)
fsPbbOUI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbbOUI.setStatus("current")
_FsPbbOUIRowStatus_Type = RowStatus
_FsPbbOUIRowStatus_Object = MibTableColumn
fsPbbOUIRowStatus = _FsPbbOUIRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 2, 1, 1, 3),
    _FsPbbOUIRowStatus_Type()
)
fsPbbOUIRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPbbOUIRowStatus.setStatus("current")
_FsPbbPortConfig_ObjectIdentity = ObjectIdentity
fsPbbPortConfig = _FsPbbPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 3)
)
_FsPbbPortPisidTable_Object = MibTable
fsPbbPortPisidTable = _FsPbbPortPisidTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 3, 1)
)
if mibBuilder.loadTexts:
    fsPbbPortPisidTable.setStatus("current")
_FsPbbPortPisidEntry_Object = MibTableRow
fsPbbPortPisidEntry = _FsPbbPortPisidEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 3, 1, 1)
)
fsPbbPortPisidEntry.setIndexNames(
    (0, "ARICENT-PROP-PBB-MIB", "fsPbbContextId"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsPbbPortPisidEntry.setStatus("current")
_FsPbbPortPisid_Type = Integer32
_FsPbbPortPisid_Object = MibTableColumn
fsPbbPortPisid = _FsPbbPortPisid_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 3, 1, 1, 1),
    _FsPbbPortPisid_Type()
)
fsPbbPortPisid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbbPortPisid.setStatus("current")
_FsPbbPIsidRowStatus_Type = RowStatus
_FsPbbPIsidRowStatus_Object = MibTableColumn
fsPbbPIsidRowStatus = _FsPbbPIsidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 3, 1, 1, 2),
    _FsPbbPIsidRowStatus_Type()
)
fsPbbPIsidRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPbbPIsidRowStatus.setStatus("current")
_FsPbbPortTable_Object = MibTable
fsPbbPortTable = _FsPbbPortTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 3, 2)
)
if mibBuilder.loadTexts:
    fsPbbPortTable.setStatus("current")
_FsPbbPortEntry_Object = MibTableRow
fsPbbPortEntry = _FsPbbPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 3, 2, 1)
)
fsPbbPortEntry.setIndexNames(
    (0, "ARICENT-PBB-MIB", "fsPbbPipIfIndex"),
)
if mibBuilder.loadTexts:
    fsPbbPortEntry.setStatus("current")


class _FsPbbPortPcpSelectionRow_Type(PriorityCodePoint):
    """Custom type fsPbbPortPcpSelectionRow based on PriorityCodePoint"""
    defaultValue = 1


_FsPbbPortPcpSelectionRow_Type.__name__ = "PriorityCodePoint"
_FsPbbPortPcpSelectionRow_Object = MibTableColumn
fsPbbPortPcpSelectionRow = _FsPbbPortPcpSelectionRow_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 3, 2, 1, 1),
    _FsPbbPortPcpSelectionRow_Type()
)
fsPbbPortPcpSelectionRow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbbPortPcpSelectionRow.setStatus("current")


class _FsPbbPortUseDei_Type(TruthValue):
    """Custom type fsPbbPortUseDei based on TruthValue"""
    defaultValue = 2


_FsPbbPortUseDei_Type.__name__ = "TruthValue"
_FsPbbPortUseDei_Object = MibTableColumn
fsPbbPortUseDei = _FsPbbPortUseDei_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 3, 2, 1, 2),
    _FsPbbPortUseDei_Type()
)
fsPbbPortUseDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbbPortUseDei.setStatus("current")


class _FsPbbPortReqDropEncoding_Type(TruthValue):
    """Custom type fsPbbPortReqDropEncoding based on TruthValue"""
    defaultValue = 2


_FsPbbPortReqDropEncoding_Type.__name__ = "TruthValue"
_FsPbbPortReqDropEncoding_Object = MibTableColumn
fsPbbPortReqDropEncoding = _FsPbbPortReqDropEncoding_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 3, 2, 1, 3),
    _FsPbbPortReqDropEncoding_Type()
)
fsPbbPortReqDropEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbbPortReqDropEncoding.setStatus("current")
_FsPbbPcpDecodingTable_Object = MibTable
fsPbbPcpDecodingTable = _FsPbbPcpDecodingTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 3, 3)
)
if mibBuilder.loadTexts:
    fsPbbPcpDecodingTable.setStatus("current")
_FsPbbPcpDecodingEntry_Object = MibTableRow
fsPbbPcpDecodingEntry = _FsPbbPcpDecodingEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 3, 3, 1)
)
fsPbbPcpDecodingEntry.setIndexNames(
    (0, "ARICENT-PBB-MIB", "fsPbbPipIfIndex"),
    (0, "ARICENT-PROP-PBB-MIB", "fsPbbPcpDecodingPcpSelRow"),
    (0, "ARICENT-PROP-PBB-MIB", "fsPbbPcpDecodingPcpValue"),
)
if mibBuilder.loadTexts:
    fsPbbPcpDecodingEntry.setStatus("current")
_FsPbbPcpDecodingPcpSelRow_Type = PriorityCodePoint
_FsPbbPcpDecodingPcpSelRow_Object = MibTableColumn
fsPbbPcpDecodingPcpSelRow = _FsPbbPcpDecodingPcpSelRow_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 3, 3, 1, 1),
    _FsPbbPcpDecodingPcpSelRow_Type()
)
fsPbbPcpDecodingPcpSelRow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPbbPcpDecodingPcpSelRow.setStatus("current")


class _FsPbbPcpDecodingPcpValue_Type(Integer32):
    """Custom type fsPbbPcpDecodingPcpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsPbbPcpDecodingPcpValue_Type.__name__ = "Integer32"
_FsPbbPcpDecodingPcpValue_Object = MibTableColumn
fsPbbPcpDecodingPcpValue = _FsPbbPcpDecodingPcpValue_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 3, 3, 1, 2),
    _FsPbbPcpDecodingPcpValue_Type()
)
fsPbbPcpDecodingPcpValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPbbPcpDecodingPcpValue.setStatus("current")


class _FsPbbPcpDecodingPriority_Type(Integer32):
    """Custom type fsPbbPcpDecodingPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsPbbPcpDecodingPriority_Type.__name__ = "Integer32"
_FsPbbPcpDecodingPriority_Object = MibTableColumn
fsPbbPcpDecodingPriority = _FsPbbPcpDecodingPriority_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 3, 3, 1, 3),
    _FsPbbPcpDecodingPriority_Type()
)
fsPbbPcpDecodingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbbPcpDecodingPriority.setStatus("current")
_FsPbbPcpDecodingDropEligible_Type = TruthValue
_FsPbbPcpDecodingDropEligible_Object = MibTableColumn
fsPbbPcpDecodingDropEligible = _FsPbbPcpDecodingDropEligible_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 3, 3, 1, 4),
    _FsPbbPcpDecodingDropEligible_Type()
)
fsPbbPcpDecodingDropEligible.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbbPcpDecodingDropEligible.setStatus("current")
_FsPbbPcpEncodingTable_Object = MibTable
fsPbbPcpEncodingTable = _FsPbbPcpEncodingTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 3, 4)
)
if mibBuilder.loadTexts:
    fsPbbPcpEncodingTable.setStatus("current")
_FsPbbPcpEncodingEntry_Object = MibTableRow
fsPbbPcpEncodingEntry = _FsPbbPcpEncodingEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 3, 4, 1)
)
fsPbbPcpEncodingEntry.setIndexNames(
    (0, "ARICENT-PBB-MIB", "fsPbbPipIfIndex"),
    (0, "ARICENT-PROP-PBB-MIB", "fsPbbPcpEncodingPcpSelRow"),
    (0, "ARICENT-PROP-PBB-MIB", "fsPbbPcpEncodingPriority"),
    (0, "ARICENT-PROP-PBB-MIB", "fsPbbPcpEncodingDropEligible"),
)
if mibBuilder.loadTexts:
    fsPbbPcpEncodingEntry.setStatus("current")
_FsPbbPcpEncodingPcpSelRow_Type = PriorityCodePoint
_FsPbbPcpEncodingPcpSelRow_Object = MibTableColumn
fsPbbPcpEncodingPcpSelRow = _FsPbbPcpEncodingPcpSelRow_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 3, 4, 1, 1),
    _FsPbbPcpEncodingPcpSelRow_Type()
)
fsPbbPcpEncodingPcpSelRow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPbbPcpEncodingPcpSelRow.setStatus("current")


class _FsPbbPcpEncodingPriority_Type(Integer32):
    """Custom type fsPbbPcpEncodingPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsPbbPcpEncodingPriority_Type.__name__ = "Integer32"
_FsPbbPcpEncodingPriority_Object = MibTableColumn
fsPbbPcpEncodingPriority = _FsPbbPcpEncodingPriority_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 3, 4, 1, 2),
    _FsPbbPcpEncodingPriority_Type()
)
fsPbbPcpEncodingPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPbbPcpEncodingPriority.setStatus("current")
_FsPbbPcpEncodingDropEligible_Type = TruthValue
_FsPbbPcpEncodingDropEligible_Object = MibTableColumn
fsPbbPcpEncodingDropEligible = _FsPbbPcpEncodingDropEligible_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 3, 4, 1, 3),
    _FsPbbPcpEncodingDropEligible_Type()
)
fsPbbPcpEncodingDropEligible.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPbbPcpEncodingDropEligible.setStatus("current")


class _FsPbbPcpEncodingPcpValue_Type(Integer32):
    """Custom type fsPbbPcpEncodingPcpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsPbbPcpEncodingPcpValue_Type.__name__ = "Integer32"
_FsPbbPcpEncodingPcpValue_Object = MibTableColumn
fsPbbPcpEncodingPcpValue = _FsPbbPcpEncodingPcpValue_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 3, 4, 1, 4),
    _FsPbbPcpEncodingPcpValue_Type()
)
fsPbbPcpEncodingPcpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbbPcpEncodingPcpValue.setStatus("current")
_FsPbbInstanceConfig_ObjectIdentity = ObjectIdentity
fsPbbInstanceConfig = _FsPbbInstanceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 4)
)
_FsPbbInstanceTable_Object = MibTable
fsPbbInstanceTable = _FsPbbInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 4, 1)
)
if mibBuilder.loadTexts:
    fsPbbInstanceTable.setStatus("current")
_FsPbbInstanceEntry_Object = MibTableRow
fsPbbInstanceEntry = _FsPbbInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 4, 1, 1)
)
fsPbbInstanceEntry.setIndexNames(
    (0, "ARICENT-PROP-PBB-MIB", "fsPbbInstanceId"),
)
if mibBuilder.loadTexts:
    fsPbbInstanceEntry.setStatus("current")


class _FsPbbInstanceId_Type(Integer32):
    """Custom type fsPbbInstanceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsPbbInstanceId_Type.__name__ = "Integer32"
_FsPbbInstanceId_Object = MibTableColumn
fsPbbInstanceId = _FsPbbInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 4, 1, 1, 1),
    _FsPbbInstanceId_Type()
)
fsPbbInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPbbInstanceId.setStatus("current")
_FsPbbInstanceMacAddr_Type = MacAddress
_FsPbbInstanceMacAddr_Object = MibTableColumn
fsPbbInstanceMacAddr = _FsPbbInstanceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 4, 1, 1, 2),
    _FsPbbInstanceMacAddr_Type()
)
fsPbbInstanceMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbbInstanceMacAddr.setStatus("current")


class _FsPbbInstanceName_Type(DisplayString):
    """Custom type fsPbbInstanceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsPbbInstanceName_Type.__name__ = "DisplayString"
_FsPbbInstanceName_Object = MibTableColumn
fsPbbInstanceName = _FsPbbInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 4, 1, 1, 3),
    _FsPbbInstanceName_Type()
)
fsPbbInstanceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbbInstanceName.setStatus("current")
_FsPbbInstanceIComponents_Type = Unsigned32
_FsPbbInstanceIComponents_Object = MibTableColumn
fsPbbInstanceIComponents = _FsPbbInstanceIComponents_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 4, 1, 1, 4),
    _FsPbbInstanceIComponents_Type()
)
fsPbbInstanceIComponents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbbInstanceIComponents.setStatus("current")
_FsPbbInstanceBComponents_Type = Unsigned32
_FsPbbInstanceBComponents_Object = MibTableColumn
fsPbbInstanceBComponents = _FsPbbInstanceBComponents_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 4, 1, 1, 5),
    _FsPbbInstanceBComponents_Type()
)
fsPbbInstanceBComponents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbbInstanceBComponents.setStatus("current")
_FsPbbInstanceBebPorts_Type = Unsigned32
_FsPbbInstanceBebPorts_Object = MibTableColumn
fsPbbInstanceBebPorts = _FsPbbInstanceBebPorts_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 4, 1, 1, 6),
    _FsPbbInstanceBebPorts_Type()
)
fsPbbInstanceBebPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbbInstanceBebPorts.setStatus("current")
_FsPbbInstanceRowStatus_Type = RowStatus
_FsPbbInstanceRowStatus_Object = MibTableColumn
fsPbbInstanceRowStatus = _FsPbbInstanceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 4, 1, 1, 7),
    _FsPbbInstanceRowStatus_Type()
)
fsPbbInstanceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPbbInstanceRowStatus.setStatus("current")
_FsPbbInstanceMappingTable_Object = MibTable
fsPbbInstanceMappingTable = _FsPbbInstanceMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 4, 2)
)
if mibBuilder.loadTexts:
    fsPbbInstanceMappingTable.setStatus("current")
_FsPbbInstanceMappingEntry_Object = MibTableRow
fsPbbInstanceMappingEntry = _FsPbbInstanceMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 4, 2, 1)
)
fsPbbInstanceMappingEntry.setIndexNames(
    (0, "ARICENT-PROP-PBB-MIB", "fsPbbContextId"),
)
if mibBuilder.loadTexts:
    fsPbbInstanceMappingEntry.setStatus("current")


class _FsPbbContextToInstanceId_Type(Integer32):
    """Custom type fsPbbContextToInstanceId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsPbbContextToInstanceId_Type.__name__ = "Integer32"
_FsPbbContextToInstanceId_Object = MibTableColumn
fsPbbContextToInstanceId = _FsPbbContextToInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 15, 4, 2, 1, 1),
    _FsPbbContextToInstanceId_Type()
)
fsPbbContextToInstanceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbbContextToInstanceId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-PROP-PBB-MIB",
    **{"aricentProviderBackboneBridgeMIB": aricentProviderBackboneBridgeMIB,
       "fsPbbSystem": fsPbbSystem,
       "fsPbbShutdownStatus": fsPbbShutdownStatus,
       "fsPbbGlbOUI": fsPbbGlbOUI,
       "fsPbbMaxNoOfISID": fsPbbMaxNoOfISID,
       "fsPbbMaxNoOfISIDPerContext": fsPbbMaxNoOfISIDPerContext,
       "fsPbbMaxPortsPerISID": fsPbbMaxPortsPerISID,
       "fsPbbMaxPortsPerISIDPerContext": fsPbbMaxPortsPerISIDPerContext,
       "fsPbbMaxCurrentNoOfISID": fsPbbMaxCurrentNoOfISID,
       "fsPbbMaxCurrentISIDPerContext": fsPbbMaxCurrentISIDPerContext,
       "fsPbbMaxCurrentPortsPerISID": fsPbbMaxCurrentPortsPerISID,
       "fsPbbMaxCurrPortsPerISIDContext": fsPbbMaxCurrPortsPerISIDContext,
       "fsPbbTraceInput": fsPbbTraceInput,
       "fsPbbTraceOption": fsPbbTraceOption,
       "fsPbbISIDConfig": fsPbbISIDConfig,
       "fsPbbISIDOUITable": fsPbbISIDOUITable,
       "fsPbbISIDOUIEntry": fsPbbISIDOUIEntry,
       "fsPbbContextId": fsPbbContextId,
       "fsPbbOUI": fsPbbOUI,
       "fsPbbOUIRowStatus": fsPbbOUIRowStatus,
       "fsPbbPortConfig": fsPbbPortConfig,
       "fsPbbPortPisidTable": fsPbbPortPisidTable,
       "fsPbbPortPisidEntry": fsPbbPortPisidEntry,
       "fsPbbPortPisid": fsPbbPortPisid,
       "fsPbbPIsidRowStatus": fsPbbPIsidRowStatus,
       "fsPbbPortTable": fsPbbPortTable,
       "fsPbbPortEntry": fsPbbPortEntry,
       "fsPbbPortPcpSelectionRow": fsPbbPortPcpSelectionRow,
       "fsPbbPortUseDei": fsPbbPortUseDei,
       "fsPbbPortReqDropEncoding": fsPbbPortReqDropEncoding,
       "fsPbbPcpDecodingTable": fsPbbPcpDecodingTable,
       "fsPbbPcpDecodingEntry": fsPbbPcpDecodingEntry,
       "fsPbbPcpDecodingPcpSelRow": fsPbbPcpDecodingPcpSelRow,
       "fsPbbPcpDecodingPcpValue": fsPbbPcpDecodingPcpValue,
       "fsPbbPcpDecodingPriority": fsPbbPcpDecodingPriority,
       "fsPbbPcpDecodingDropEligible": fsPbbPcpDecodingDropEligible,
       "fsPbbPcpEncodingTable": fsPbbPcpEncodingTable,
       "fsPbbPcpEncodingEntry": fsPbbPcpEncodingEntry,
       "fsPbbPcpEncodingPcpSelRow": fsPbbPcpEncodingPcpSelRow,
       "fsPbbPcpEncodingPriority": fsPbbPcpEncodingPriority,
       "fsPbbPcpEncodingDropEligible": fsPbbPcpEncodingDropEligible,
       "fsPbbPcpEncodingPcpValue": fsPbbPcpEncodingPcpValue,
       "fsPbbInstanceConfig": fsPbbInstanceConfig,
       "fsPbbInstanceTable": fsPbbInstanceTable,
       "fsPbbInstanceEntry": fsPbbInstanceEntry,
       "fsPbbInstanceId": fsPbbInstanceId,
       "fsPbbInstanceMacAddr": fsPbbInstanceMacAddr,
       "fsPbbInstanceName": fsPbbInstanceName,
       "fsPbbInstanceIComponents": fsPbbInstanceIComponents,
       "fsPbbInstanceBComponents": fsPbbInstanceBComponents,
       "fsPbbInstanceBebPorts": fsPbbInstanceBebPorts,
       "fsPbbInstanceRowStatus": fsPbbInstanceRowStatus,
       "fsPbbInstanceMappingTable": fsPbbInstanceMappingTable,
       "fsPbbInstanceMappingEntry": fsPbbInstanceMappingEntry,
       "fsPbbContextToInstanceId": fsPbbContextToInstanceId}
)
