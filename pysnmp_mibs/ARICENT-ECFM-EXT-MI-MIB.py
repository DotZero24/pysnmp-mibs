# SNMP MIB module (ARICENT-ECFM-EXT-MI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-ECFM-EXT-MI-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:43:38 2025
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

(FsMIEcfmCcmInterval,
 FsMIEcfmConfigErrors,
 FsMIEcfmFngState,
 FsMIEcfmHighestDefectPri,
 FsMIEcfmIdPermission,
 FsMIEcfmLowestAlarmPri,
 FsMIEcfmMDLevel,
 FsMIEcfmMDLevelOrNone,
 FsMIEcfmMaintAssocName,
 FsMIEcfmMaintAssocNameType,
 FsMIEcfmMepDefects,
 FsMIEcfmMepId,
 FsMIEcfmMepIdOrZero,
 FsMIEcfmMhfCreation,
 FsMIEcfmMpDirection,
 FsMIEcfmTransmitStatus,
 fsMIEcfmContextId,
 fsMIEcfmMdIndex) = mibBuilder.importSymbols(
    "ARICENT-ECFM-MI-MIB",
    "FsMIEcfmCcmInterval",
    "FsMIEcfmConfigErrors",
    "FsMIEcfmFngState",
    "FsMIEcfmHighestDefectPri",
    "FsMIEcfmIdPermission",
    "FsMIEcfmLowestAlarmPri",
    "FsMIEcfmMDLevel",
    "FsMIEcfmMDLevelOrNone",
    "FsMIEcfmMaintAssocName",
    "FsMIEcfmMaintAssocNameType",
    "FsMIEcfmMepDefects",
    "FsMIEcfmMepId",
    "FsMIEcfmMepIdOrZero",
    "FsMIEcfmMhfCreation",
    "FsMIEcfmMpDirection",
    "FsMIEcfmTransmitStatus",
    "fsMIEcfmContextId",
    "fsMIEcfmMdIndex")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

fsMIEcfmExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13)
)
if mibBuilder.loadTexts:
    fsMIEcfmExtMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ServiceSelectorType(TextualConvention, Integer32):
    status = "current"
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
        *(("vlanId", 1),
          ("isid", 2),
          ("mplsTunnelLsp", 3),
          ("mplsPseudoWire", 4))
    )



class ServiceSelectorValueOrNone(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )



class ServiceSelectorValue(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



# MIB Managed Objects in the order of their OIDs

_FsMIEcfmExtMIBObjects_ObjectIdentity = ObjectIdentity
fsMIEcfmExtMIBObjects = _FsMIEcfmExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1)
)
_FsMIEcfmExtSystem_ObjectIdentity = ObjectIdentity
fsMIEcfmExtSystem = _FsMIEcfmExtSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 1)
)
_FsMIEcfmExtStackTable_Object = MibTable
fsMIEcfmExtStackTable = _FsMIEcfmExtStackTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fsMIEcfmExtStackTable.setStatus("current")
_FsMIEcfmExtStackEntry_Object = MibTableRow
fsMIEcfmExtStackEntry = _FsMIEcfmExtStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 1, 1, 1)
)
fsMIEcfmExtStackEntry.setIndexNames(
    (0, "ARICENT-ECFM-EXT-MI-MIB", "fsMIEcfmExtStackIfIndex"),
    (0, "ARICENT-ECFM-EXT-MI-MIB", "fsMIEcfmExtStackServiceSelectorType"),
    (0, "ARICENT-ECFM-EXT-MI-MIB", "fsMIEcfmExtStackServiceSelectorOrNone"),
    (0, "ARICENT-ECFM-EXT-MI-MIB", "fsMIEcfmExtStackMdLevel"),
    (0, "ARICENT-ECFM-EXT-MI-MIB", "fsMIEcfmExtStackDirection"),
)
if mibBuilder.loadTexts:
    fsMIEcfmExtStackEntry.setStatus("current")
_FsMIEcfmExtStackIfIndex_Type = InterfaceIndex
_FsMIEcfmExtStackIfIndex_Object = MibTableColumn
fsMIEcfmExtStackIfIndex = _FsMIEcfmExtStackIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 1, 1, 1, 1),
    _FsMIEcfmExtStackIfIndex_Type()
)
fsMIEcfmExtStackIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmExtStackIfIndex.setStatus("current")
_FsMIEcfmExtStackServiceSelectorType_Type = ServiceSelectorType
_FsMIEcfmExtStackServiceSelectorType_Object = MibTableColumn
fsMIEcfmExtStackServiceSelectorType = _FsMIEcfmExtStackServiceSelectorType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 1, 1, 1, 2),
    _FsMIEcfmExtStackServiceSelectorType_Type()
)
fsMIEcfmExtStackServiceSelectorType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmExtStackServiceSelectorType.setStatus("current")
_FsMIEcfmExtStackServiceSelectorOrNone_Type = ServiceSelectorValueOrNone
_FsMIEcfmExtStackServiceSelectorOrNone_Object = MibTableColumn
fsMIEcfmExtStackServiceSelectorOrNone = _FsMIEcfmExtStackServiceSelectorOrNone_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 1, 1, 1, 3),
    _FsMIEcfmExtStackServiceSelectorOrNone_Type()
)
fsMIEcfmExtStackServiceSelectorOrNone.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmExtStackServiceSelectorOrNone.setStatus("current")
_FsMIEcfmExtStackMdLevel_Type = FsMIEcfmMDLevel
_FsMIEcfmExtStackMdLevel_Object = MibTableColumn
fsMIEcfmExtStackMdLevel = _FsMIEcfmExtStackMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 1, 1, 1, 4),
    _FsMIEcfmExtStackMdLevel_Type()
)
fsMIEcfmExtStackMdLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmExtStackMdLevel.setStatus("current")
_FsMIEcfmExtStackDirection_Type = FsMIEcfmMpDirection
_FsMIEcfmExtStackDirection_Object = MibTableColumn
fsMIEcfmExtStackDirection = _FsMIEcfmExtStackDirection_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 1, 1, 1, 5),
    _FsMIEcfmExtStackDirection_Type()
)
fsMIEcfmExtStackDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmExtStackDirection.setStatus("current")
_FsMIEcfmExtStackMdIndex_Type = Unsigned32
_FsMIEcfmExtStackMdIndex_Object = MibTableColumn
fsMIEcfmExtStackMdIndex = _FsMIEcfmExtStackMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 1, 1, 1, 6),
    _FsMIEcfmExtStackMdIndex_Type()
)
fsMIEcfmExtStackMdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmExtStackMdIndex.setStatus("current")
_FsMIEcfmExtStackMaIndex_Type = Unsigned32
_FsMIEcfmExtStackMaIndex_Object = MibTableColumn
fsMIEcfmExtStackMaIndex = _FsMIEcfmExtStackMaIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 1, 1, 1, 7),
    _FsMIEcfmExtStackMaIndex_Type()
)
fsMIEcfmExtStackMaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmExtStackMaIndex.setStatus("current")
_FsMIEcfmExtStackMepId_Type = FsMIEcfmMepIdOrZero
_FsMIEcfmExtStackMepId_Object = MibTableColumn
fsMIEcfmExtStackMepId = _FsMIEcfmExtStackMepId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 1, 1, 1, 8),
    _FsMIEcfmExtStackMepId_Type()
)
fsMIEcfmExtStackMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmExtStackMepId.setStatus("current")
_FsMIEcfmExtStackMacAddress_Type = MacAddress
_FsMIEcfmExtStackMacAddress_Object = MibTableColumn
fsMIEcfmExtStackMacAddress = _FsMIEcfmExtStackMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 1, 1, 1, 9),
    _FsMIEcfmExtStackMacAddress_Type()
)
fsMIEcfmExtStackMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmExtStackMacAddress.setStatus("current")
_FsMIEcfmExtConfigErrorListTable_Object = MibTable
fsMIEcfmExtConfigErrorListTable = _FsMIEcfmExtConfigErrorListTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 1, 2)
)
if mibBuilder.loadTexts:
    fsMIEcfmExtConfigErrorListTable.setStatus("current")
_FsMIEcfmExtConfigErrorListEntry_Object = MibTableRow
fsMIEcfmExtConfigErrorListEntry = _FsMIEcfmExtConfigErrorListEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 1, 2, 1)
)
fsMIEcfmExtConfigErrorListEntry.setIndexNames(
    (0, "ARICENT-ECFM-EXT-MI-MIB", "fsMIEcfmExtConfigErrorListSelectorType"),
    (0, "ARICENT-ECFM-EXT-MI-MIB", "fsMIEcfmExtConfigErrorListSelector"),
    (0, "ARICENT-ECFM-EXT-MI-MIB", "fsMIEcfmExtConfigErrorListIfIndex"),
)
if mibBuilder.loadTexts:
    fsMIEcfmExtConfigErrorListEntry.setStatus("current")
_FsMIEcfmExtConfigErrorListSelectorType_Type = ServiceSelectorType
_FsMIEcfmExtConfigErrorListSelectorType_Object = MibTableColumn
fsMIEcfmExtConfigErrorListSelectorType = _FsMIEcfmExtConfigErrorListSelectorType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 1, 2, 1, 1),
    _FsMIEcfmExtConfigErrorListSelectorType_Type()
)
fsMIEcfmExtConfigErrorListSelectorType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmExtConfigErrorListSelectorType.setStatus("current")
_FsMIEcfmExtConfigErrorListSelector_Type = ServiceSelectorValue
_FsMIEcfmExtConfigErrorListSelector_Object = MibTableColumn
fsMIEcfmExtConfigErrorListSelector = _FsMIEcfmExtConfigErrorListSelector_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 1, 2, 1, 2),
    _FsMIEcfmExtConfigErrorListSelector_Type()
)
fsMIEcfmExtConfigErrorListSelector.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmExtConfigErrorListSelector.setStatus("current")
_FsMIEcfmExtConfigErrorListIfIndex_Type = InterfaceIndex
_FsMIEcfmExtConfigErrorListIfIndex_Object = MibTableColumn
fsMIEcfmExtConfigErrorListIfIndex = _FsMIEcfmExtConfigErrorListIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 1, 2, 1, 3),
    _FsMIEcfmExtConfigErrorListIfIndex_Type()
)
fsMIEcfmExtConfigErrorListIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmExtConfigErrorListIfIndex.setStatus("current")
_FsMIEcfmExtConfigErrorListErrorType_Type = FsMIEcfmConfigErrors
_FsMIEcfmExtConfigErrorListErrorType_Object = MibTableColumn
fsMIEcfmExtConfigErrorListErrorType = _FsMIEcfmExtConfigErrorListErrorType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 1, 2, 1, 4),
    _FsMIEcfmExtConfigErrorListErrorType_Type()
)
fsMIEcfmExtConfigErrorListErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmExtConfigErrorListErrorType.setStatus("current")
_FsMIEcfmExtMipTable_Object = MibTable
fsMIEcfmExtMipTable = _FsMIEcfmExtMipTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 1, 3)
)
if mibBuilder.loadTexts:
    fsMIEcfmExtMipTable.setStatus("current")
_FsMIEcfmExtMipEntry_Object = MibTableRow
fsMIEcfmExtMipEntry = _FsMIEcfmExtMipEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 1, 3, 1)
)
fsMIEcfmExtMipEntry.setIndexNames(
    (0, "ARICENT-ECFM-EXT-MI-MIB", "fsMIEcfmExtMipIfIndex"),
    (0, "ARICENT-ECFM-EXT-MI-MIB", "fsMIEcfmExtMipMdLevel"),
    (0, "ARICENT-ECFM-EXT-MI-MIB", "fsMIEcfmExtMipSelectorType"),
    (0, "ARICENT-ECFM-EXT-MI-MIB", "fsMIEcfmExtMipPrimarySelector"),
)
if mibBuilder.loadTexts:
    fsMIEcfmExtMipEntry.setStatus("current")
_FsMIEcfmExtMipIfIndex_Type = InterfaceIndex
_FsMIEcfmExtMipIfIndex_Object = MibTableColumn
fsMIEcfmExtMipIfIndex = _FsMIEcfmExtMipIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 1, 3, 1, 1),
    _FsMIEcfmExtMipIfIndex_Type()
)
fsMIEcfmExtMipIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmExtMipIfIndex.setStatus("current")


class _FsMIEcfmExtMipMdLevel_Type(Integer32):
    """Custom type fsMIEcfmExtMipMdLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsMIEcfmExtMipMdLevel_Type.__name__ = "Integer32"
_FsMIEcfmExtMipMdLevel_Object = MibTableColumn
fsMIEcfmExtMipMdLevel = _FsMIEcfmExtMipMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 1, 3, 1, 2),
    _FsMIEcfmExtMipMdLevel_Type()
)
fsMIEcfmExtMipMdLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmExtMipMdLevel.setStatus("current")
_FsMIEcfmExtMipSelectorType_Type = ServiceSelectorType
_FsMIEcfmExtMipSelectorType_Object = MibTableColumn
fsMIEcfmExtMipSelectorType = _FsMIEcfmExtMipSelectorType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 1, 3, 1, 3),
    _FsMIEcfmExtMipSelectorType_Type()
)
fsMIEcfmExtMipSelectorType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmExtMipSelectorType.setStatus("current")
_FsMIEcfmExtMipPrimarySelector_Type = ServiceSelectorValue
_FsMIEcfmExtMipPrimarySelector_Object = MibTableColumn
fsMIEcfmExtMipPrimarySelector = _FsMIEcfmExtMipPrimarySelector_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 1, 3, 1, 4),
    _FsMIEcfmExtMipPrimarySelector_Type()
)
fsMIEcfmExtMipPrimarySelector.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmExtMipPrimarySelector.setStatus("current")
_FsMIEcfmExtMipActive_Type = TruthValue
_FsMIEcfmExtMipActive_Object = MibTableColumn
fsMIEcfmExtMipActive = _FsMIEcfmExtMipActive_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 1, 3, 1, 5),
    _FsMIEcfmExtMipActive_Type()
)
fsMIEcfmExtMipActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMipActive.setStatus("current")
_FsMIEcfmExtMipRowStatus_Type = RowStatus
_FsMIEcfmExtMipRowStatus_Object = MibTableColumn
fsMIEcfmExtMipRowStatus = _FsMIEcfmExtMipRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 1, 3, 1, 6),
    _FsMIEcfmExtMipRowStatus_Type()
)
fsMIEcfmExtMipRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMipRowStatus.setStatus("current")
_FsMIEcfmExtContext_ObjectIdentity = ObjectIdentity
fsMIEcfmExtContext = _FsMIEcfmExtContext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2)
)
_FsMIEcfmExtDefaultMdTable_Object = MibTable
fsMIEcfmExtDefaultMdTable = _FsMIEcfmExtDefaultMdTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fsMIEcfmExtDefaultMdTable.setStatus("current")
_FsMIEcfmExtDefaultMdEntry_Object = MibTableRow
fsMIEcfmExtDefaultMdEntry = _FsMIEcfmExtDefaultMdEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 1, 1)
)
fsMIEcfmExtDefaultMdEntry.setIndexNames(
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmContextId"),
    (0, "ARICENT-ECFM-EXT-MI-MIB", "fsMIEcfmExtDefaultMdPrimarySelectorType"),
    (0, "ARICENT-ECFM-EXT-MI-MIB", "fsMIEcfmExtDefaultMdPrimarySelector"),
)
if mibBuilder.loadTexts:
    fsMIEcfmExtDefaultMdEntry.setStatus("current")
_FsMIEcfmExtDefaultMdPrimarySelectorType_Type = ServiceSelectorType
_FsMIEcfmExtDefaultMdPrimarySelectorType_Object = MibTableColumn
fsMIEcfmExtDefaultMdPrimarySelectorType = _FsMIEcfmExtDefaultMdPrimarySelectorType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 1, 1, 1),
    _FsMIEcfmExtDefaultMdPrimarySelectorType_Type()
)
fsMIEcfmExtDefaultMdPrimarySelectorType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmExtDefaultMdPrimarySelectorType.setStatus("current")
_FsMIEcfmExtDefaultMdPrimarySelector_Type = ServiceSelectorValue
_FsMIEcfmExtDefaultMdPrimarySelector_Object = MibTableColumn
fsMIEcfmExtDefaultMdPrimarySelector = _FsMIEcfmExtDefaultMdPrimarySelector_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 1, 1, 2),
    _FsMIEcfmExtDefaultMdPrimarySelector_Type()
)
fsMIEcfmExtDefaultMdPrimarySelector.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmExtDefaultMdPrimarySelector.setStatus("current")
_FsMIEcfmExtDefaultMdStatus_Type = TruthValue
_FsMIEcfmExtDefaultMdStatus_Object = MibTableColumn
fsMIEcfmExtDefaultMdStatus = _FsMIEcfmExtDefaultMdStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 1, 1, 3),
    _FsMIEcfmExtDefaultMdStatus_Type()
)
fsMIEcfmExtDefaultMdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmExtDefaultMdStatus.setStatus("current")


class _FsMIEcfmExtDefaultMdLevel_Type(FsMIEcfmMDLevelOrNone):
    """Custom type fsMIEcfmExtDefaultMdLevel based on FsMIEcfmMDLevelOrNone"""
    defaultValue = -1


_FsMIEcfmExtDefaultMdLevel_Type.__name__ = "FsMIEcfmMDLevelOrNone"
_FsMIEcfmExtDefaultMdLevel_Object = MibTableColumn
fsMIEcfmExtDefaultMdLevel = _FsMIEcfmExtDefaultMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 1, 1, 4),
    _FsMIEcfmExtDefaultMdLevel_Type()
)
fsMIEcfmExtDefaultMdLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmExtDefaultMdLevel.setStatus("current")


class _FsMIEcfmExtDefaultMdMhfCreation_Type(FsMIEcfmMhfCreation):
    """Custom type fsMIEcfmExtDefaultMdMhfCreation based on FsMIEcfmMhfCreation"""
    defaultValue = 4


_FsMIEcfmExtDefaultMdMhfCreation_Type.__name__ = "FsMIEcfmMhfCreation"
_FsMIEcfmExtDefaultMdMhfCreation_Object = MibTableColumn
fsMIEcfmExtDefaultMdMhfCreation = _FsMIEcfmExtDefaultMdMhfCreation_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 1, 1, 5),
    _FsMIEcfmExtDefaultMdMhfCreation_Type()
)
fsMIEcfmExtDefaultMdMhfCreation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmExtDefaultMdMhfCreation.setStatus("current")


class _FsMIEcfmExtDefaultMdIdPermission_Type(FsMIEcfmIdPermission):
    """Custom type fsMIEcfmExtDefaultMdIdPermission based on FsMIEcfmIdPermission"""
    defaultValue = 5


_FsMIEcfmExtDefaultMdIdPermission_Type.__name__ = "FsMIEcfmIdPermission"
_FsMIEcfmExtDefaultMdIdPermission_Object = MibTableColumn
fsMIEcfmExtDefaultMdIdPermission = _FsMIEcfmExtDefaultMdIdPermission_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 1, 1, 6),
    _FsMIEcfmExtDefaultMdIdPermission_Type()
)
fsMIEcfmExtDefaultMdIdPermission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmExtDefaultMdIdPermission.setStatus("current")
_FsMIEcfmExtMaTable_Object = MibTable
fsMIEcfmExtMaTable = _FsMIEcfmExtMaTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 2)
)
if mibBuilder.loadTexts:
    fsMIEcfmExtMaTable.setStatus("current")
_FsMIEcfmExtMaEntry_Object = MibTableRow
fsMIEcfmExtMaEntry = _FsMIEcfmExtMaEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 2, 1)
)
fsMIEcfmExtMaEntry.setIndexNames(
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmContextId"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmMdIndex"),
    (0, "ARICENT-ECFM-EXT-MI-MIB", "fsMIEcfmExtMaIndex"),
    (0, "ARICENT-ECFM-EXT-MI-MIB", "fsMIEcfmExtMaPrimarySelectorType"),
    (0, "ARICENT-ECFM-EXT-MI-MIB", "fsMIEcfmExtMaPrimarySelectorOrNone"),
)
if mibBuilder.loadTexts:
    fsMIEcfmExtMaEntry.setStatus("current")


class _FsMIEcfmExtMaIndex_Type(Unsigned32):
    """Custom type fsMIEcfmExtMaIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FsMIEcfmExtMaIndex_Type.__name__ = "Unsigned32"
_FsMIEcfmExtMaIndex_Object = MibTableColumn
fsMIEcfmExtMaIndex = _FsMIEcfmExtMaIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 2, 1, 1),
    _FsMIEcfmExtMaIndex_Type()
)
fsMIEcfmExtMaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmExtMaIndex.setStatus("current")
_FsMIEcfmExtMaPrimarySelectorType_Type = ServiceSelectorType
_FsMIEcfmExtMaPrimarySelectorType_Object = MibTableColumn
fsMIEcfmExtMaPrimarySelectorType = _FsMIEcfmExtMaPrimarySelectorType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 2, 1, 2),
    _FsMIEcfmExtMaPrimarySelectorType_Type()
)
fsMIEcfmExtMaPrimarySelectorType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmExtMaPrimarySelectorType.setStatus("current")
_FsMIEcfmExtMaPrimarySelectorOrNone_Type = ServiceSelectorValueOrNone
_FsMIEcfmExtMaPrimarySelectorOrNone_Object = MibTableColumn
fsMIEcfmExtMaPrimarySelectorOrNone = _FsMIEcfmExtMaPrimarySelectorOrNone_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 2, 1, 3),
    _FsMIEcfmExtMaPrimarySelectorOrNone_Type()
)
fsMIEcfmExtMaPrimarySelectorOrNone.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmExtMaPrimarySelectorOrNone.setStatus("current")
_FsMIEcfmExtMaFormat_Type = FsMIEcfmMaintAssocNameType
_FsMIEcfmExtMaFormat_Object = MibTableColumn
fsMIEcfmExtMaFormat = _FsMIEcfmExtMaFormat_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 2, 1, 4),
    _FsMIEcfmExtMaFormat_Type()
)
fsMIEcfmExtMaFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMaFormat.setStatus("current")
_FsMIEcfmExtMaName_Type = FsMIEcfmMaintAssocName
_FsMIEcfmExtMaName_Object = MibTableColumn
fsMIEcfmExtMaName = _FsMIEcfmExtMaName_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 2, 1, 5),
    _FsMIEcfmExtMaName_Type()
)
fsMIEcfmExtMaName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMaName.setStatus("current")


class _FsMIEcfmExtMaMhfCreation_Type(FsMIEcfmMhfCreation):
    """Custom type fsMIEcfmExtMaMhfCreation based on FsMIEcfmMhfCreation"""
    defaultValue = 4


_FsMIEcfmExtMaMhfCreation_Type.__name__ = "FsMIEcfmMhfCreation"
_FsMIEcfmExtMaMhfCreation_Object = MibTableColumn
fsMIEcfmExtMaMhfCreation = _FsMIEcfmExtMaMhfCreation_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 2, 1, 6),
    _FsMIEcfmExtMaMhfCreation_Type()
)
fsMIEcfmExtMaMhfCreation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMaMhfCreation.setStatus("current")


class _FsMIEcfmExtMaIdPermission_Type(FsMIEcfmIdPermission):
    """Custom type fsMIEcfmExtMaIdPermission based on FsMIEcfmIdPermission"""
    defaultValue = 5


_FsMIEcfmExtMaIdPermission_Type.__name__ = "FsMIEcfmIdPermission"
_FsMIEcfmExtMaIdPermission_Object = MibTableColumn
fsMIEcfmExtMaIdPermission = _FsMIEcfmExtMaIdPermission_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 2, 1, 7),
    _FsMIEcfmExtMaIdPermission_Type()
)
fsMIEcfmExtMaIdPermission.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMaIdPermission.setStatus("current")


class _FsMIEcfmExtMaCcmInterval_Type(FsMIEcfmCcmInterval):
    """Custom type fsMIEcfmExtMaCcmInterval based on FsMIEcfmCcmInterval"""
    defaultValue = 4


_FsMIEcfmExtMaCcmInterval_Type.__name__ = "FsMIEcfmCcmInterval"
_FsMIEcfmExtMaCcmInterval_Object = MibTableColumn
fsMIEcfmExtMaCcmInterval = _FsMIEcfmExtMaCcmInterval_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 2, 1, 8),
    _FsMIEcfmExtMaCcmInterval_Type()
)
fsMIEcfmExtMaCcmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMaCcmInterval.setStatus("current")
_FsMIEcfmExtMaNumberOfVids_Type = Unsigned32
_FsMIEcfmExtMaNumberOfVids_Object = MibTableColumn
fsMIEcfmExtMaNumberOfVids = _FsMIEcfmExtMaNumberOfVids_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 2, 1, 9),
    _FsMIEcfmExtMaNumberOfVids_Type()
)
fsMIEcfmExtMaNumberOfVids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmExtMaNumberOfVids.setStatus("current")
_FsMIEcfmExtMaRowStatus_Type = RowStatus
_FsMIEcfmExtMaRowStatus_Object = MibTableColumn
fsMIEcfmExtMaRowStatus = _FsMIEcfmExtMaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 2, 1, 10),
    _FsMIEcfmExtMaRowStatus_Type()
)
fsMIEcfmExtMaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMaRowStatus.setStatus("current")


class _FsMIEcfmExtMaCrosscheckStatus_Type(Integer32):
    """Custom type fsMIEcfmExtMaCrosscheckStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FsMIEcfmExtMaCrosscheckStatus_Type.__name__ = "Integer32"
_FsMIEcfmExtMaCrosscheckStatus_Object = MibTableColumn
fsMIEcfmExtMaCrosscheckStatus = _FsMIEcfmExtMaCrosscheckStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 2, 1, 11),
    _FsMIEcfmExtMaCrosscheckStatus_Type()
)
fsMIEcfmExtMaCrosscheckStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmExtMaCrosscheckStatus.setStatus("current")
_FsMIEcfmExtMepTable_Object = MibTable
fsMIEcfmExtMepTable = _FsMIEcfmExtMepTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3)
)
if mibBuilder.loadTexts:
    fsMIEcfmExtMepTable.setStatus("current")
_FsMIEcfmExtMepEntry_Object = MibTableRow
fsMIEcfmExtMepEntry = _FsMIEcfmExtMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1)
)
fsMIEcfmExtMepEntry.setIndexNames(
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmContextId"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmMdIndex"),
    (0, "ARICENT-ECFM-EXT-MI-MIB", "fsMIEcfmExtMaIndex"),
    (0, "ARICENT-ECFM-EXT-MI-MIB", "fsMIEcfmExtMepIdentifier"),
)
if mibBuilder.loadTexts:
    fsMIEcfmExtMepEntry.setStatus("current")
_FsMIEcfmExtMepIdentifier_Type = FsMIEcfmMepId
_FsMIEcfmExtMepIdentifier_Object = MibTableColumn
fsMIEcfmExtMepIdentifier = _FsMIEcfmExtMepIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 1),
    _FsMIEcfmExtMepIdentifier_Type()
)
fsMIEcfmExtMepIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepIdentifier.setStatus("current")
_FsMIEcfmExtMepIfIndex_Type = InterfaceIndex
_FsMIEcfmExtMepIfIndex_Object = MibTableColumn
fsMIEcfmExtMepIfIndex = _FsMIEcfmExtMepIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 2),
    _FsMIEcfmExtMepIfIndex_Type()
)
fsMIEcfmExtMepIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepIfIndex.setStatus("current")
_FsMIEcfmExtMepDirection_Type = FsMIEcfmMpDirection
_FsMIEcfmExtMepDirection_Object = MibTableColumn
fsMIEcfmExtMepDirection = _FsMIEcfmExtMepDirection_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 3),
    _FsMIEcfmExtMepDirection_Type()
)
fsMIEcfmExtMepDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepDirection.setStatus("current")


class _FsMIEcfmExtMepPrimaryVidOrIsid_Type(Unsigned32):
    """Custom type fsMIEcfmExtMepPrimaryVidOrIsid based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_FsMIEcfmExtMepPrimaryVidOrIsid_Type.__name__ = "Unsigned32"
_FsMIEcfmExtMepPrimaryVidOrIsid_Object = MibTableColumn
fsMIEcfmExtMepPrimaryVidOrIsid = _FsMIEcfmExtMepPrimaryVidOrIsid_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 4),
    _FsMIEcfmExtMepPrimaryVidOrIsid_Type()
)
fsMIEcfmExtMepPrimaryVidOrIsid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepPrimaryVidOrIsid.setStatus("current")


class _FsMIEcfmExtMepActive_Type(TruthValue):
    """Custom type fsMIEcfmExtMepActive based on TruthValue"""
    defaultValue = 2


_FsMIEcfmExtMepActive_Type.__name__ = "TruthValue"
_FsMIEcfmExtMepActive_Object = MibTableColumn
fsMIEcfmExtMepActive = _FsMIEcfmExtMepActive_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 5),
    _FsMIEcfmExtMepActive_Type()
)
fsMIEcfmExtMepActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepActive.setStatus("current")


class _FsMIEcfmExtMepFngState_Type(FsMIEcfmFngState):
    """Custom type fsMIEcfmExtMepFngState based on FsMIEcfmFngState"""
    defaultValue = 1


_FsMIEcfmExtMepFngState_Type.__name__ = "FsMIEcfmFngState"
_FsMIEcfmExtMepFngState_Object = MibTableColumn
fsMIEcfmExtMepFngState = _FsMIEcfmExtMepFngState_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 6),
    _FsMIEcfmExtMepFngState_Type()
)
fsMIEcfmExtMepFngState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepFngState.setStatus("current")


class _FsMIEcfmExtMepCciEnabled_Type(TruthValue):
    """Custom type fsMIEcfmExtMepCciEnabled based on TruthValue"""
    defaultValue = 2


_FsMIEcfmExtMepCciEnabled_Type.__name__ = "TruthValue"
_FsMIEcfmExtMepCciEnabled_Object = MibTableColumn
fsMIEcfmExtMepCciEnabled = _FsMIEcfmExtMepCciEnabled_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 7),
    _FsMIEcfmExtMepCciEnabled_Type()
)
fsMIEcfmExtMepCciEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepCciEnabled.setStatus("current")


class _FsMIEcfmExtMepCcmLtmPriority_Type(Unsigned32):
    """Custom type fsMIEcfmExtMepCcmLtmPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsMIEcfmExtMepCcmLtmPriority_Type.__name__ = "Unsigned32"
_FsMIEcfmExtMepCcmLtmPriority_Object = MibTableColumn
fsMIEcfmExtMepCcmLtmPriority = _FsMIEcfmExtMepCcmLtmPriority_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 8),
    _FsMIEcfmExtMepCcmLtmPriority_Type()
)
fsMIEcfmExtMepCcmLtmPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepCcmLtmPriority.setStatus("current")
_FsMIEcfmExtMepMacAddress_Type = MacAddress
_FsMIEcfmExtMepMacAddress_Object = MibTableColumn
fsMIEcfmExtMepMacAddress = _FsMIEcfmExtMepMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 9),
    _FsMIEcfmExtMepMacAddress_Type()
)
fsMIEcfmExtMepMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepMacAddress.setStatus("current")


class _FsMIEcfmExtMepLowPrDef_Type(FsMIEcfmLowestAlarmPri):
    """Custom type fsMIEcfmExtMepLowPrDef based on FsMIEcfmLowestAlarmPri"""
    defaultValue = 2


_FsMIEcfmExtMepLowPrDef_Type.__name__ = "FsMIEcfmLowestAlarmPri"
_FsMIEcfmExtMepLowPrDef_Object = MibTableColumn
fsMIEcfmExtMepLowPrDef = _FsMIEcfmExtMepLowPrDef_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 10),
    _FsMIEcfmExtMepLowPrDef_Type()
)
fsMIEcfmExtMepLowPrDef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepLowPrDef.setStatus("current")


class _FsMIEcfmExtMepFngAlarmTime_Type(TimeInterval):
    """Custom type fsMIEcfmExtMepFngAlarmTime based on TimeInterval"""
    defaultValue = 250

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(250, 1000),
    )


_FsMIEcfmExtMepFngAlarmTime_Type.__name__ = "TimeInterval"
_FsMIEcfmExtMepFngAlarmTime_Object = MibTableColumn
fsMIEcfmExtMepFngAlarmTime = _FsMIEcfmExtMepFngAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 11),
    _FsMIEcfmExtMepFngAlarmTime_Type()
)
fsMIEcfmExtMepFngAlarmTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepFngAlarmTime.setStatus("current")


class _FsMIEcfmExtMepFngResetTime_Type(TimeInterval):
    """Custom type fsMIEcfmExtMepFngResetTime based on TimeInterval"""
    defaultValue = 1000

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(250, 1000),
    )


_FsMIEcfmExtMepFngResetTime_Type.__name__ = "TimeInterval"
_FsMIEcfmExtMepFngResetTime_Object = MibTableColumn
fsMIEcfmExtMepFngResetTime = _FsMIEcfmExtMepFngResetTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 12),
    _FsMIEcfmExtMepFngResetTime_Type()
)
fsMIEcfmExtMepFngResetTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepFngResetTime.setStatus("current")
_FsMIEcfmExtMepHighestPrDefect_Type = FsMIEcfmHighestDefectPri
_FsMIEcfmExtMepHighestPrDefect_Object = MibTableColumn
fsMIEcfmExtMepHighestPrDefect = _FsMIEcfmExtMepHighestPrDefect_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 13),
    _FsMIEcfmExtMepHighestPrDefect_Type()
)
fsMIEcfmExtMepHighestPrDefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepHighestPrDefect.setStatus("current")
_FsMIEcfmExtMepDefects_Type = FsMIEcfmMepDefects
_FsMIEcfmExtMepDefects_Object = MibTableColumn
fsMIEcfmExtMepDefects = _FsMIEcfmExtMepDefects_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 14),
    _FsMIEcfmExtMepDefects_Type()
)
fsMIEcfmExtMepDefects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepDefects.setStatus("current")


class _FsMIEcfmExtMepErrorCcmLastFailure_Type(OctetString):
    """Custom type fsMIEcfmExtMepErrorCcmLastFailure based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1522),
    )


_FsMIEcfmExtMepErrorCcmLastFailure_Type.__name__ = "OctetString"
_FsMIEcfmExtMepErrorCcmLastFailure_Object = MibTableColumn
fsMIEcfmExtMepErrorCcmLastFailure = _FsMIEcfmExtMepErrorCcmLastFailure_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 15),
    _FsMIEcfmExtMepErrorCcmLastFailure_Type()
)
fsMIEcfmExtMepErrorCcmLastFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepErrorCcmLastFailure.setStatus("current")


class _FsMIEcfmExtMepXconCcmLastFailure_Type(OctetString):
    """Custom type fsMIEcfmExtMepXconCcmLastFailure based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1522),
    )


_FsMIEcfmExtMepXconCcmLastFailure_Type.__name__ = "OctetString"
_FsMIEcfmExtMepXconCcmLastFailure_Object = MibTableColumn
fsMIEcfmExtMepXconCcmLastFailure = _FsMIEcfmExtMepXconCcmLastFailure_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 16),
    _FsMIEcfmExtMepXconCcmLastFailure_Type()
)
fsMIEcfmExtMepXconCcmLastFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepXconCcmLastFailure.setStatus("current")
_FsMIEcfmExtMepCcmSequenceErrors_Type = Unsigned32
_FsMIEcfmExtMepCcmSequenceErrors_Object = MibTableColumn
fsMIEcfmExtMepCcmSequenceErrors = _FsMIEcfmExtMepCcmSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 17),
    _FsMIEcfmExtMepCcmSequenceErrors_Type()
)
fsMIEcfmExtMepCcmSequenceErrors.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepCcmSequenceErrors.setStatus("current")
_FsMIEcfmExtMepCciSentCcms_Type = Unsigned32
_FsMIEcfmExtMepCciSentCcms_Object = MibTableColumn
fsMIEcfmExtMepCciSentCcms = _FsMIEcfmExtMepCciSentCcms_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 18),
    _FsMIEcfmExtMepCciSentCcms_Type()
)
fsMIEcfmExtMepCciSentCcms.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepCciSentCcms.setStatus("current")
_FsMIEcfmExtMepNextLbmTransId_Type = Unsigned32
_FsMIEcfmExtMepNextLbmTransId_Object = MibTableColumn
fsMIEcfmExtMepNextLbmTransId = _FsMIEcfmExtMepNextLbmTransId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 19),
    _FsMIEcfmExtMepNextLbmTransId_Type()
)
fsMIEcfmExtMepNextLbmTransId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepNextLbmTransId.setStatus("current")
_FsMIEcfmExtMepLbrIn_Type = Unsigned32
_FsMIEcfmExtMepLbrIn_Object = MibTableColumn
fsMIEcfmExtMepLbrIn = _FsMIEcfmExtMepLbrIn_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 20),
    _FsMIEcfmExtMepLbrIn_Type()
)
fsMIEcfmExtMepLbrIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepLbrIn.setStatus("current")
_FsMIEcfmExtMepLbrInOutOfOrder_Type = Unsigned32
_FsMIEcfmExtMepLbrInOutOfOrder_Object = MibTableColumn
fsMIEcfmExtMepLbrInOutOfOrder = _FsMIEcfmExtMepLbrInOutOfOrder_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 21),
    _FsMIEcfmExtMepLbrInOutOfOrder_Type()
)
fsMIEcfmExtMepLbrInOutOfOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepLbrInOutOfOrder.setStatus("current")
_FsMIEcfmExtMepLbrBadMsdu_Type = Unsigned32
_FsMIEcfmExtMepLbrBadMsdu_Object = MibTableColumn
fsMIEcfmExtMepLbrBadMsdu = _FsMIEcfmExtMepLbrBadMsdu_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 22),
    _FsMIEcfmExtMepLbrBadMsdu_Type()
)
fsMIEcfmExtMepLbrBadMsdu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepLbrBadMsdu.setStatus("current")
_FsMIEcfmExtMepLtmNextSeqNumber_Type = Unsigned32
_FsMIEcfmExtMepLtmNextSeqNumber_Object = MibTableColumn
fsMIEcfmExtMepLtmNextSeqNumber = _FsMIEcfmExtMepLtmNextSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 23),
    _FsMIEcfmExtMepLtmNextSeqNumber_Type()
)
fsMIEcfmExtMepLtmNextSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepLtmNextSeqNumber.setStatus("current")
_FsMIEcfmExtMepUnexpLtrIn_Type = Unsigned32
_FsMIEcfmExtMepUnexpLtrIn_Object = MibTableColumn
fsMIEcfmExtMepUnexpLtrIn = _FsMIEcfmExtMepUnexpLtrIn_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 24),
    _FsMIEcfmExtMepUnexpLtrIn_Type()
)
fsMIEcfmExtMepUnexpLtrIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepUnexpLtrIn.setStatus("current")
_FsMIEcfmExtMepLbrOut_Type = Unsigned32
_FsMIEcfmExtMepLbrOut_Object = MibTableColumn
fsMIEcfmExtMepLbrOut = _FsMIEcfmExtMepLbrOut_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 25),
    _FsMIEcfmExtMepLbrOut_Type()
)
fsMIEcfmExtMepLbrOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepLbrOut.setStatus("current")


class _FsMIEcfmExtMepTransmitLbmStatus_Type(FsMIEcfmTransmitStatus):
    """Custom type fsMIEcfmExtMepTransmitLbmStatus based on FsMIEcfmTransmitStatus"""
    defaultValue = 0


_FsMIEcfmExtMepTransmitLbmStatus_Type.__name__ = "FsMIEcfmTransmitStatus"
_FsMIEcfmExtMepTransmitLbmStatus_Object = MibTableColumn
fsMIEcfmExtMepTransmitLbmStatus = _FsMIEcfmExtMepTransmitLbmStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 26),
    _FsMIEcfmExtMepTransmitLbmStatus_Type()
)
fsMIEcfmExtMepTransmitLbmStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepTransmitLbmStatus.setStatus("current")
_FsMIEcfmExtMepTransmitLbmDestMacAddress_Type = MacAddress
_FsMIEcfmExtMepTransmitLbmDestMacAddress_Object = MibTableColumn
fsMIEcfmExtMepTransmitLbmDestMacAddress = _FsMIEcfmExtMepTransmitLbmDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 27),
    _FsMIEcfmExtMepTransmitLbmDestMacAddress_Type()
)
fsMIEcfmExtMepTransmitLbmDestMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepTransmitLbmDestMacAddress.setStatus("current")
_FsMIEcfmExtMepTransmitLbmDestMepId_Type = FsMIEcfmMepIdOrZero
_FsMIEcfmExtMepTransmitLbmDestMepId_Object = MibTableColumn
fsMIEcfmExtMepTransmitLbmDestMepId = _FsMIEcfmExtMepTransmitLbmDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 28),
    _FsMIEcfmExtMepTransmitLbmDestMepId_Type()
)
fsMIEcfmExtMepTransmitLbmDestMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepTransmitLbmDestMepId.setStatus("current")
_FsMIEcfmExtMepTransmitLbmDestIsMepId_Type = TruthValue
_FsMIEcfmExtMepTransmitLbmDestIsMepId_Object = MibTableColumn
fsMIEcfmExtMepTransmitLbmDestIsMepId = _FsMIEcfmExtMepTransmitLbmDestIsMepId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 29),
    _FsMIEcfmExtMepTransmitLbmDestIsMepId_Type()
)
fsMIEcfmExtMepTransmitLbmDestIsMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepTransmitLbmDestIsMepId.setStatus("current")


class _FsMIEcfmExtMepTransmitLbmMessages_Type(Integer32):
    """Custom type fsMIEcfmExtMepTransmitLbmMessages based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FsMIEcfmExtMepTransmitLbmMessages_Type.__name__ = "Integer32"
_FsMIEcfmExtMepTransmitLbmMessages_Object = MibTableColumn
fsMIEcfmExtMepTransmitLbmMessages = _FsMIEcfmExtMepTransmitLbmMessages_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 30),
    _FsMIEcfmExtMepTransmitLbmMessages_Type()
)
fsMIEcfmExtMepTransmitLbmMessages.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepTransmitLbmMessages.setStatus("current")


class _FsMIEcfmExtMepTransmitLbmDataTlv_Type(OctetString):
    """Custom type fsMIEcfmExtMepTransmitLbmDataTlv based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1500),
    )


_FsMIEcfmExtMepTransmitLbmDataTlv_Type.__name__ = "OctetString"
_FsMIEcfmExtMepTransmitLbmDataTlv_Object = MibTableColumn
fsMIEcfmExtMepTransmitLbmDataTlv = _FsMIEcfmExtMepTransmitLbmDataTlv_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 31),
    _FsMIEcfmExtMepTransmitLbmDataTlv_Type()
)
fsMIEcfmExtMepTransmitLbmDataTlv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepTransmitLbmDataTlv.setStatus("current")


class _FsMIEcfmExtMepTransmitLbmVlanIsidPriority_Type(Integer32):
    """Custom type fsMIEcfmExtMepTransmitLbmVlanIsidPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsMIEcfmExtMepTransmitLbmVlanIsidPriority_Type.__name__ = "Integer32"
_FsMIEcfmExtMepTransmitLbmVlanIsidPriority_Object = MibTableColumn
fsMIEcfmExtMepTransmitLbmVlanIsidPriority = _FsMIEcfmExtMepTransmitLbmVlanIsidPriority_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 32),
    _FsMIEcfmExtMepTransmitLbmVlanIsidPriority_Type()
)
fsMIEcfmExtMepTransmitLbmVlanIsidPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepTransmitLbmVlanIsidPriority.setStatus("current")


class _FsMIEcfmExtMepTransmitLbmVlanIsidDropEnable_Type(TruthValue):
    """Custom type fsMIEcfmExtMepTransmitLbmVlanIsidDropEnable based on TruthValue"""
    defaultValue = 1


_FsMIEcfmExtMepTransmitLbmVlanIsidDropEnable_Type.__name__ = "TruthValue"
_FsMIEcfmExtMepTransmitLbmVlanIsidDropEnable_Object = MibTableColumn
fsMIEcfmExtMepTransmitLbmVlanIsidDropEnable = _FsMIEcfmExtMepTransmitLbmVlanIsidDropEnable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 33),
    _FsMIEcfmExtMepTransmitLbmVlanIsidDropEnable_Type()
)
fsMIEcfmExtMepTransmitLbmVlanIsidDropEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepTransmitLbmVlanIsidDropEnable.setStatus("current")


class _FsMIEcfmExtMepTransmitLbmResultOK_Type(TruthValue):
    """Custom type fsMIEcfmExtMepTransmitLbmResultOK based on TruthValue"""
    defaultValue = 1


_FsMIEcfmExtMepTransmitLbmResultOK_Type.__name__ = "TruthValue"
_FsMIEcfmExtMepTransmitLbmResultOK_Object = MibTableColumn
fsMIEcfmExtMepTransmitLbmResultOK = _FsMIEcfmExtMepTransmitLbmResultOK_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 34),
    _FsMIEcfmExtMepTransmitLbmResultOK_Type()
)
fsMIEcfmExtMepTransmitLbmResultOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepTransmitLbmResultOK.setStatus("current")
_FsMIEcfmExtMepTransmitLbmSeqNumber_Type = Unsigned32
_FsMIEcfmExtMepTransmitLbmSeqNumber_Object = MibTableColumn
fsMIEcfmExtMepTransmitLbmSeqNumber = _FsMIEcfmExtMepTransmitLbmSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 35),
    _FsMIEcfmExtMepTransmitLbmSeqNumber_Type()
)
fsMIEcfmExtMepTransmitLbmSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepTransmitLbmSeqNumber.setStatus("current")


class _FsMIEcfmExtMepTransmitLtmStatus_Type(FsMIEcfmTransmitStatus):
    """Custom type fsMIEcfmExtMepTransmitLtmStatus based on FsMIEcfmTransmitStatus"""
    defaultValue = 0


_FsMIEcfmExtMepTransmitLtmStatus_Type.__name__ = "FsMIEcfmTransmitStatus"
_FsMIEcfmExtMepTransmitLtmStatus_Object = MibTableColumn
fsMIEcfmExtMepTransmitLtmStatus = _FsMIEcfmExtMepTransmitLtmStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 36),
    _FsMIEcfmExtMepTransmitLtmStatus_Type()
)
fsMIEcfmExtMepTransmitLtmStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepTransmitLtmStatus.setStatus("current")


class _FsMIEcfmExtMepTransmitLtmFlags_Type(Bits):
    """Custom type fsMIEcfmExtMepTransmitLtmFlags based on Bits"""
    defaultHexValue = ""

    namedValues = NamedValues(
        ("useFDBonly", 0)
    )

_FsMIEcfmExtMepTransmitLtmFlags_Type.__name__ = "Bits"
_FsMIEcfmExtMepTransmitLtmFlags_Object = MibTableColumn
fsMIEcfmExtMepTransmitLtmFlags = _FsMIEcfmExtMepTransmitLtmFlags_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 37),
    _FsMIEcfmExtMepTransmitLtmFlags_Type()
)
fsMIEcfmExtMepTransmitLtmFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepTransmitLtmFlags.setStatus("current")
_FsMIEcfmExtMepTransmitLtmTargetMacAddress_Type = MacAddress
_FsMIEcfmExtMepTransmitLtmTargetMacAddress_Object = MibTableColumn
fsMIEcfmExtMepTransmitLtmTargetMacAddress = _FsMIEcfmExtMepTransmitLtmTargetMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 38),
    _FsMIEcfmExtMepTransmitLtmTargetMacAddress_Type()
)
fsMIEcfmExtMepTransmitLtmTargetMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepTransmitLtmTargetMacAddress.setStatus("current")
_FsMIEcfmExtMepTransmitLtmTargetMepId_Type = FsMIEcfmMepIdOrZero
_FsMIEcfmExtMepTransmitLtmTargetMepId_Object = MibTableColumn
fsMIEcfmExtMepTransmitLtmTargetMepId = _FsMIEcfmExtMepTransmitLtmTargetMepId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 39),
    _FsMIEcfmExtMepTransmitLtmTargetMepId_Type()
)
fsMIEcfmExtMepTransmitLtmTargetMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepTransmitLtmTargetMepId.setStatus("current")
_FsMIEcfmExtMepTransmitLtmTargetIsMepId_Type = TruthValue
_FsMIEcfmExtMepTransmitLtmTargetIsMepId_Object = MibTableColumn
fsMIEcfmExtMepTransmitLtmTargetIsMepId = _FsMIEcfmExtMepTransmitLtmTargetIsMepId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 40),
    _FsMIEcfmExtMepTransmitLtmTargetIsMepId_Type()
)
fsMIEcfmExtMepTransmitLtmTargetIsMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepTransmitLtmTargetIsMepId.setStatus("current")


class _FsMIEcfmExtMepTransmitLtmTtl_Type(Unsigned32):
    """Custom type fsMIEcfmExtMepTransmitLtmTtl based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIEcfmExtMepTransmitLtmTtl_Type.__name__ = "Unsigned32"
_FsMIEcfmExtMepTransmitLtmTtl_Object = MibTableColumn
fsMIEcfmExtMepTransmitLtmTtl = _FsMIEcfmExtMepTransmitLtmTtl_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 41),
    _FsMIEcfmExtMepTransmitLtmTtl_Type()
)
fsMIEcfmExtMepTransmitLtmTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepTransmitLtmTtl.setStatus("current")


class _FsMIEcfmExtMepTransmitLtmResult_Type(TruthValue):
    """Custom type fsMIEcfmExtMepTransmitLtmResult based on TruthValue"""
    defaultValue = 1


_FsMIEcfmExtMepTransmitLtmResult_Type.__name__ = "TruthValue"
_FsMIEcfmExtMepTransmitLtmResult_Object = MibTableColumn
fsMIEcfmExtMepTransmitLtmResult = _FsMIEcfmExtMepTransmitLtmResult_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 42),
    _FsMIEcfmExtMepTransmitLtmResult_Type()
)
fsMIEcfmExtMepTransmitLtmResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepTransmitLtmResult.setStatus("current")
_FsMIEcfmExtMepTransmitLtmSeqNumber_Type = Unsigned32
_FsMIEcfmExtMepTransmitLtmSeqNumber_Object = MibTableColumn
fsMIEcfmExtMepTransmitLtmSeqNumber = _FsMIEcfmExtMepTransmitLtmSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 43),
    _FsMIEcfmExtMepTransmitLtmSeqNumber_Type()
)
fsMIEcfmExtMepTransmitLtmSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepTransmitLtmSeqNumber.setStatus("current")


class _FsMIEcfmExtMepTransmitLtmEgressIdentifier_Type(OctetString):
    """Custom type fsMIEcfmExtMepTransmitLtmEgressIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FsMIEcfmExtMepTransmitLtmEgressIdentifier_Type.__name__ = "OctetString"
_FsMIEcfmExtMepTransmitLtmEgressIdentifier_Object = MibTableColumn
fsMIEcfmExtMepTransmitLtmEgressIdentifier = _FsMIEcfmExtMepTransmitLtmEgressIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 44),
    _FsMIEcfmExtMepTransmitLtmEgressIdentifier_Type()
)
fsMIEcfmExtMepTransmitLtmEgressIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepTransmitLtmEgressIdentifier.setStatus("current")
_FsMIEcfmExtMepRowStatus_Type = RowStatus
_FsMIEcfmExtMepRowStatus_Object = MibTableColumn
fsMIEcfmExtMepRowStatus = _FsMIEcfmExtMepRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 45),
    _FsMIEcfmExtMepRowStatus_Type()
)
fsMIEcfmExtMepRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepRowStatus.setStatus("current")


class _FsMIEcfmExtMepCcmOffload_Type(Integer32):
    """Custom type fsMIEcfmExtMepCcmOffload based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FsMIEcfmExtMepCcmOffload_Type.__name__ = "Integer32"
_FsMIEcfmExtMepCcmOffload_Object = MibTableColumn
fsMIEcfmExtMepCcmOffload = _FsMIEcfmExtMepCcmOffload_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 13, 1, 2, 3, 1, 46),
    _FsMIEcfmExtMepCcmOffload_Type()
)
fsMIEcfmExtMepCcmOffload.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmExtMepCcmOffload.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-ECFM-EXT-MI-MIB",
    **{"ServiceSelectorType": ServiceSelectorType,
       "ServiceSelectorValueOrNone": ServiceSelectorValueOrNone,
       "ServiceSelectorValue": ServiceSelectorValue,
       "fsMIEcfmExtMIB": fsMIEcfmExtMIB,
       "fsMIEcfmExtMIBObjects": fsMIEcfmExtMIBObjects,
       "fsMIEcfmExtSystem": fsMIEcfmExtSystem,
       "fsMIEcfmExtStackTable": fsMIEcfmExtStackTable,
       "fsMIEcfmExtStackEntry": fsMIEcfmExtStackEntry,
       "fsMIEcfmExtStackIfIndex": fsMIEcfmExtStackIfIndex,
       "fsMIEcfmExtStackServiceSelectorType": fsMIEcfmExtStackServiceSelectorType,
       "fsMIEcfmExtStackServiceSelectorOrNone": fsMIEcfmExtStackServiceSelectorOrNone,
       "fsMIEcfmExtStackMdLevel": fsMIEcfmExtStackMdLevel,
       "fsMIEcfmExtStackDirection": fsMIEcfmExtStackDirection,
       "fsMIEcfmExtStackMdIndex": fsMIEcfmExtStackMdIndex,
       "fsMIEcfmExtStackMaIndex": fsMIEcfmExtStackMaIndex,
       "fsMIEcfmExtStackMepId": fsMIEcfmExtStackMepId,
       "fsMIEcfmExtStackMacAddress": fsMIEcfmExtStackMacAddress,
       "fsMIEcfmExtConfigErrorListTable": fsMIEcfmExtConfigErrorListTable,
       "fsMIEcfmExtConfigErrorListEntry": fsMIEcfmExtConfigErrorListEntry,
       "fsMIEcfmExtConfigErrorListSelectorType": fsMIEcfmExtConfigErrorListSelectorType,
       "fsMIEcfmExtConfigErrorListSelector": fsMIEcfmExtConfigErrorListSelector,
       "fsMIEcfmExtConfigErrorListIfIndex": fsMIEcfmExtConfigErrorListIfIndex,
       "fsMIEcfmExtConfigErrorListErrorType": fsMIEcfmExtConfigErrorListErrorType,
       "fsMIEcfmExtMipTable": fsMIEcfmExtMipTable,
       "fsMIEcfmExtMipEntry": fsMIEcfmExtMipEntry,
       "fsMIEcfmExtMipIfIndex": fsMIEcfmExtMipIfIndex,
       "fsMIEcfmExtMipMdLevel": fsMIEcfmExtMipMdLevel,
       "fsMIEcfmExtMipSelectorType": fsMIEcfmExtMipSelectorType,
       "fsMIEcfmExtMipPrimarySelector": fsMIEcfmExtMipPrimarySelector,
       "fsMIEcfmExtMipActive": fsMIEcfmExtMipActive,
       "fsMIEcfmExtMipRowStatus": fsMIEcfmExtMipRowStatus,
       "fsMIEcfmExtContext": fsMIEcfmExtContext,
       "fsMIEcfmExtDefaultMdTable": fsMIEcfmExtDefaultMdTable,
       "fsMIEcfmExtDefaultMdEntry": fsMIEcfmExtDefaultMdEntry,
       "fsMIEcfmExtDefaultMdPrimarySelectorType": fsMIEcfmExtDefaultMdPrimarySelectorType,
       "fsMIEcfmExtDefaultMdPrimarySelector": fsMIEcfmExtDefaultMdPrimarySelector,
       "fsMIEcfmExtDefaultMdStatus": fsMIEcfmExtDefaultMdStatus,
       "fsMIEcfmExtDefaultMdLevel": fsMIEcfmExtDefaultMdLevel,
       "fsMIEcfmExtDefaultMdMhfCreation": fsMIEcfmExtDefaultMdMhfCreation,
       "fsMIEcfmExtDefaultMdIdPermission": fsMIEcfmExtDefaultMdIdPermission,
       "fsMIEcfmExtMaTable": fsMIEcfmExtMaTable,
       "fsMIEcfmExtMaEntry": fsMIEcfmExtMaEntry,
       "fsMIEcfmExtMaIndex": fsMIEcfmExtMaIndex,
       "fsMIEcfmExtMaPrimarySelectorType": fsMIEcfmExtMaPrimarySelectorType,
       "fsMIEcfmExtMaPrimarySelectorOrNone": fsMIEcfmExtMaPrimarySelectorOrNone,
       "fsMIEcfmExtMaFormat": fsMIEcfmExtMaFormat,
       "fsMIEcfmExtMaName": fsMIEcfmExtMaName,
       "fsMIEcfmExtMaMhfCreation": fsMIEcfmExtMaMhfCreation,
       "fsMIEcfmExtMaIdPermission": fsMIEcfmExtMaIdPermission,
       "fsMIEcfmExtMaCcmInterval": fsMIEcfmExtMaCcmInterval,
       "fsMIEcfmExtMaNumberOfVids": fsMIEcfmExtMaNumberOfVids,
       "fsMIEcfmExtMaRowStatus": fsMIEcfmExtMaRowStatus,
       "fsMIEcfmExtMaCrosscheckStatus": fsMIEcfmExtMaCrosscheckStatus,
       "fsMIEcfmExtMepTable": fsMIEcfmExtMepTable,
       "fsMIEcfmExtMepEntry": fsMIEcfmExtMepEntry,
       "fsMIEcfmExtMepIdentifier": fsMIEcfmExtMepIdentifier,
       "fsMIEcfmExtMepIfIndex": fsMIEcfmExtMepIfIndex,
       "fsMIEcfmExtMepDirection": fsMIEcfmExtMepDirection,
       "fsMIEcfmExtMepPrimaryVidOrIsid": fsMIEcfmExtMepPrimaryVidOrIsid,
       "fsMIEcfmExtMepActive": fsMIEcfmExtMepActive,
       "fsMIEcfmExtMepFngState": fsMIEcfmExtMepFngState,
       "fsMIEcfmExtMepCciEnabled": fsMIEcfmExtMepCciEnabled,
       "fsMIEcfmExtMepCcmLtmPriority": fsMIEcfmExtMepCcmLtmPriority,
       "fsMIEcfmExtMepMacAddress": fsMIEcfmExtMepMacAddress,
       "fsMIEcfmExtMepLowPrDef": fsMIEcfmExtMepLowPrDef,
       "fsMIEcfmExtMepFngAlarmTime": fsMIEcfmExtMepFngAlarmTime,
       "fsMIEcfmExtMepFngResetTime": fsMIEcfmExtMepFngResetTime,
       "fsMIEcfmExtMepHighestPrDefect": fsMIEcfmExtMepHighestPrDefect,
       "fsMIEcfmExtMepDefects": fsMIEcfmExtMepDefects,
       "fsMIEcfmExtMepErrorCcmLastFailure": fsMIEcfmExtMepErrorCcmLastFailure,
       "fsMIEcfmExtMepXconCcmLastFailure": fsMIEcfmExtMepXconCcmLastFailure,
       "fsMIEcfmExtMepCcmSequenceErrors": fsMIEcfmExtMepCcmSequenceErrors,
       "fsMIEcfmExtMepCciSentCcms": fsMIEcfmExtMepCciSentCcms,
       "fsMIEcfmExtMepNextLbmTransId": fsMIEcfmExtMepNextLbmTransId,
       "fsMIEcfmExtMepLbrIn": fsMIEcfmExtMepLbrIn,
       "fsMIEcfmExtMepLbrInOutOfOrder": fsMIEcfmExtMepLbrInOutOfOrder,
       "fsMIEcfmExtMepLbrBadMsdu": fsMIEcfmExtMepLbrBadMsdu,
       "fsMIEcfmExtMepLtmNextSeqNumber": fsMIEcfmExtMepLtmNextSeqNumber,
       "fsMIEcfmExtMepUnexpLtrIn": fsMIEcfmExtMepUnexpLtrIn,
       "fsMIEcfmExtMepLbrOut": fsMIEcfmExtMepLbrOut,
       "fsMIEcfmExtMepTransmitLbmStatus": fsMIEcfmExtMepTransmitLbmStatus,
       "fsMIEcfmExtMepTransmitLbmDestMacAddress": fsMIEcfmExtMepTransmitLbmDestMacAddress,
       "fsMIEcfmExtMepTransmitLbmDestMepId": fsMIEcfmExtMepTransmitLbmDestMepId,
       "fsMIEcfmExtMepTransmitLbmDestIsMepId": fsMIEcfmExtMepTransmitLbmDestIsMepId,
       "fsMIEcfmExtMepTransmitLbmMessages": fsMIEcfmExtMepTransmitLbmMessages,
       "fsMIEcfmExtMepTransmitLbmDataTlv": fsMIEcfmExtMepTransmitLbmDataTlv,
       "fsMIEcfmExtMepTransmitLbmVlanIsidPriority": fsMIEcfmExtMepTransmitLbmVlanIsidPriority,
       "fsMIEcfmExtMepTransmitLbmVlanIsidDropEnable": fsMIEcfmExtMepTransmitLbmVlanIsidDropEnable,
       "fsMIEcfmExtMepTransmitLbmResultOK": fsMIEcfmExtMepTransmitLbmResultOK,
       "fsMIEcfmExtMepTransmitLbmSeqNumber": fsMIEcfmExtMepTransmitLbmSeqNumber,
       "fsMIEcfmExtMepTransmitLtmStatus": fsMIEcfmExtMepTransmitLtmStatus,
       "fsMIEcfmExtMepTransmitLtmFlags": fsMIEcfmExtMepTransmitLtmFlags,
       "fsMIEcfmExtMepTransmitLtmTargetMacAddress": fsMIEcfmExtMepTransmitLtmTargetMacAddress,
       "fsMIEcfmExtMepTransmitLtmTargetMepId": fsMIEcfmExtMepTransmitLtmTargetMepId,
       "fsMIEcfmExtMepTransmitLtmTargetIsMepId": fsMIEcfmExtMepTransmitLtmTargetIsMepId,
       "fsMIEcfmExtMepTransmitLtmTtl": fsMIEcfmExtMepTransmitLtmTtl,
       "fsMIEcfmExtMepTransmitLtmResult": fsMIEcfmExtMepTransmitLtmResult,
       "fsMIEcfmExtMepTransmitLtmSeqNumber": fsMIEcfmExtMepTransmitLtmSeqNumber,
       "fsMIEcfmExtMepTransmitLtmEgressIdentifier": fsMIEcfmExtMepTransmitLtmEgressIdentifier,
       "fsMIEcfmExtMepRowStatus": fsMIEcfmExtMepRowStatus,
       "fsMIEcfmExtMepCcmOffload": fsMIEcfmExtMepCcmOffload}
)
