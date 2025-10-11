# SNMP MIB module (IPE-ETH-RING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nec/IPE-ETH-RING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:53:46 2025
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
 Opaque,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class IpeAdminStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("down", 1),
          ("up", 2))
    )



class IpeEnableDisableValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("disabled", 1),
          ("enabled", 2))
    )



class IpeEtherRingIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )



class IpeEtherRingIndexOrZero(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )



class IpeEtherRingPortId(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )



class IpeEtherRingPortIdOrZero(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )



class IpeEtherRingProtoVersion(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("g8032v1", 1),
          ("g8032v2", 2))
    )



class IpeEtherRingVlanIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



class IpeMepIdOrZero(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )



class IpeRingType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("major", 1),
          ("sub", 2))
    )



class IpeVlanList(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512



# MIB Managed Objects in the order of their OIDs

_Nec_ObjectIdentity = ObjectIdentity
nec = _Nec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119)
)
_Nec_mib_ObjectIdentity = ObjectIdentity
nec_mib = _Nec_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2)
)
_NecProductDepend_ObjectIdentity = ObjectIdentity
necProductDepend = _NecProductDepend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3)
)
_RadioEquipment_ObjectIdentity = ObjectIdentity
radioEquipment = _RadioEquipment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69)
)
_PasoNeoIpe_common_ObjectIdentity = ObjectIdentity
pasoNeoIpe_common = _PasoNeoIpe_common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501)
)
_AlarmStatusGroup_ObjectIdentity = ObjectIdentity
alarmStatusGroup = _AlarmStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3)
)
_AsEtherRingGroup_ObjectIdentity = ObjectIdentity
asEtherRingGroup = _AsEtherRingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 39)
)
_AsEtherRingTable_Object = MibTable
asEtherRingTable = _AsEtherRingTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 39, 1)
)
if mibBuilder.loadTexts:
    asEtherRingTable.setStatus("current")
_AsEtherRingEntry_Object = MibTableRow
asEtherRingEntry = _AsEtherRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 39, 1, 1)
)
asEtherRingEntry.setIndexNames(
    (0, "IPE-ETH-RING-MIB", "asEtherRingRingIndex"),
)
if mibBuilder.loadTexts:
    asEtherRingEntry.setStatus("current")
_AsEtherRingRingIndex_Type = IpeEtherRingIndex
_AsEtherRingRingIndex_Object = MibTableColumn
asEtherRingRingIndex = _AsEtherRingRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 39, 1, 1, 1),
    _AsEtherRingRingIndex_Type()
)
asEtherRingRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asEtherRingRingIndex.setStatus("current")
_AsEtherRingNEAddress_Type = IpAddress
_AsEtherRingNEAddress_Object = MibTableColumn
asEtherRingNEAddress = _AsEtherRingNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 39, 1, 1, 2),
    _AsEtherRingNEAddress_Type()
)
asEtherRingNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asEtherRingNEAddress.setStatus("current")


class _AsEtherRingState_Type(Integer32):
    """Custom type asEtherRingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("disabled", 1),
          ("idle", 2),
          ("protection", 3),
          ("forced", 4),
          ("manual", 5),
          ("pending", 6))
    )


_AsEtherRingState_Type.__name__ = "Integer32"
_AsEtherRingState_Object = MibTableColumn
asEtherRingState = _AsEtherRingState_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 39, 1, 1, 3),
    _AsEtherRingState_Type()
)
asEtherRingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asEtherRingState.setStatus("current")


class _AsEtherRingCause_Type(Integer32):
    """Custom type asEtherRingCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("none", 1),
          ("localSf", 2),
          ("localNr", 3),
          ("remoteSf", 4),
          ("remoteNr", 5),
          ("localFs", 6),
          ("localMs", 7),
          ("remoteFs", 8),
          ("remoteMs", 9))
    )


_AsEtherRingCause_Type.__name__ = "Integer32"
_AsEtherRingCause_Object = MibTableColumn
asEtherRingCause = _AsEtherRingCause_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 39, 1, 1, 4),
    _AsEtherRingCause_Type()
)
asEtherRingCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asEtherRingCause.setStatus("current")


class _AsEtherRingMultiRplOwnerDetect_Type(Integer32):
    """Custom type asEtherRingMultiRplOwnerDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("none", 1),
          ("detected", 2))
    )


_AsEtherRingMultiRplOwnerDetect_Type.__name__ = "Integer32"
_AsEtherRingMultiRplOwnerDetect_Object = MibTableColumn
asEtherRingMultiRplOwnerDetect = _AsEtherRingMultiRplOwnerDetect_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 39, 1, 1, 5),
    _AsEtherRingMultiRplOwnerDetect_Type()
)
asEtherRingMultiRplOwnerDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asEtherRingMultiRplOwnerDetect.setStatus("current")
_AsEtherRingPortTable_Object = MibTable
asEtherRingPortTable = _AsEtherRingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 39, 2)
)
if mibBuilder.loadTexts:
    asEtherRingPortTable.setStatus("current")
_AsEtherRingPortEntry_Object = MibTableRow
asEtherRingPortEntry = _AsEtherRingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 39, 2, 1)
)
asEtherRingPortEntry.setIndexNames(
    (0, "IPE-ETH-RING-MIB", "asEtherRingPortRingIndex"),
    (0, "IPE-ETH-RING-MIB", "asEtherRingPortId"),
)
if mibBuilder.loadTexts:
    asEtherRingPortEntry.setStatus("current")
_AsEtherRingPortRingIndex_Type = IpeEtherRingIndex
_AsEtherRingPortRingIndex_Object = MibTableColumn
asEtherRingPortRingIndex = _AsEtherRingPortRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 39, 2, 1, 1),
    _AsEtherRingPortRingIndex_Type()
)
asEtherRingPortRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asEtherRingPortRingIndex.setStatus("current")
_AsEtherRingPortId_Type = IpeEtherRingPortId
_AsEtherRingPortId_Object = MibTableColumn
asEtherRingPortId = _AsEtherRingPortId_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 39, 2, 1, 2),
    _AsEtherRingPortId_Type()
)
asEtherRingPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asEtherRingPortId.setStatus("current")
_AsEtherRingPortNEAddress_Type = IpAddress
_AsEtherRingPortNEAddress_Object = MibTableColumn
asEtherRingPortNEAddress = _AsEtherRingPortNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 39, 2, 1, 3),
    _AsEtherRingPortNEAddress_Type()
)
asEtherRingPortNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asEtherRingPortNEAddress.setStatus("current")


class _AsEtherRingPortState_Type(Integer32):
    """Custom type asEtherRingPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("disabled", 1),
          ("initBlocking", 2),
          ("rplBlocking", 3),
          ("forwarding", 4),
          ("signalFail", 5),
          ("recovery", 6),
          ("waitToRestore", 7),
          ("forcedSwitch", 8),
          ("manualSwitch", 9),
          ("waitToBlock", 10))
    )


_AsEtherRingPortState_Type.__name__ = "Integer32"
_AsEtherRingPortState_Object = MibTableColumn
asEtherRingPortState = _AsEtherRingPortState_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 39, 2, 1, 4),
    _AsEtherRingPortState_Type()
)
asEtherRingPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asEtherRingPortState.setStatus("current")


class _AsEtherRingPortLoopDetect_Type(Integer32):
    """Custom type asEtherRingPortLoopDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("none", 1),
          ("detected", 2))
    )


_AsEtherRingPortLoopDetect_Type.__name__ = "Integer32"
_AsEtherRingPortLoopDetect_Object = MibTableColumn
asEtherRingPortLoopDetect = _AsEtherRingPortLoopDetect_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 39, 2, 1, 5),
    _AsEtherRingPortLoopDetect_Type()
)
asEtherRingPortLoopDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asEtherRingPortLoopDetect.setStatus("current")


class _AsEtherRingPortProtoTimeout_Type(Integer32):
    """Custom type asEtherRingPortProtoTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("none", 1),
          ("detected", 2))
    )


_AsEtherRingPortProtoTimeout_Type.__name__ = "Integer32"
_AsEtherRingPortProtoTimeout_Object = MibTableColumn
asEtherRingPortProtoTimeout = _AsEtherRingPortProtoTimeout_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 39, 2, 1, 6),
    _AsEtherRingPortProtoTimeout_Type()
)
asEtherRingPortProtoTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asEtherRingPortProtoTimeout.setStatus("current")
_ProvisioningGroup_ObjectIdentity = ObjectIdentity
provisioningGroup = _ProvisioningGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5)
)
_ProvEtherRingGroup_ObjectIdentity = ObjectIdentity
provEtherRingGroup = _ProvEtherRingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39)
)
_ProvEtherRingTable_Object = MibTable
provEtherRingTable = _ProvEtherRingTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 1)
)
if mibBuilder.loadTexts:
    provEtherRingTable.setStatus("current")
_ProvEtherRingEntry_Object = MibTableRow
provEtherRingEntry = _ProvEtherRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 1, 1)
)
provEtherRingEntry.setIndexNames(
    (0, "IPE-ETH-RING-MIB", "provEtherRingIndex"),
)
if mibBuilder.loadTexts:
    provEtherRingEntry.setStatus("current")
_ProvEtherRingIndex_Type = IpeEtherRingIndex
_ProvEtherRingIndex_Object = MibTableColumn
provEtherRingIndex = _ProvEtherRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 1, 1, 1),
    _ProvEtherRingIndex_Type()
)
provEtherRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provEtherRingIndex.setStatus("current")
_ProvEtherRingNEAddress_Type = IpAddress
_ProvEtherRingNEAddress_Object = MibTableColumn
provEtherRingNEAddress = _ProvEtherRingNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 1, 1, 2),
    _ProvEtherRingNEAddress_Type()
)
provEtherRingNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provEtherRingNEAddress.setStatus("current")


class _ProvEtherRingProtoVersion_Type(IpeEtherRingProtoVersion):
    """Custom type provEtherRingProtoVersion based on IpeEtherRingProtoVersion"""
    defaultValue = 2


_ProvEtherRingProtoVersion_Type.__name__ = "IpeEtherRingProtoVersion"
_ProvEtherRingProtoVersion_Object = MibTableColumn
provEtherRingProtoVersion = _ProvEtherRingProtoVersion_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 1, 1, 3),
    _ProvEtherRingProtoVersion_Type()
)
provEtherRingProtoVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provEtherRingProtoVersion.setStatus("current")


class _ProvEtherRingName_Type(DisplayString):
    """Custom type provEtherRingName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProvEtherRingName_Type.__name__ = "DisplayString"
_ProvEtherRingName_Object = MibTableColumn
provEtherRingName = _ProvEtherRingName_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 1, 1, 4),
    _ProvEtherRingName_Type()
)
provEtherRingName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provEtherRingName.setStatus("current")


class _ProvEtherRingAdminStatus_Type(IpeAdminStatus):
    """Custom type provEtherRingAdminStatus based on IpeAdminStatus"""
    defaultValue = 1


_ProvEtherRingAdminStatus_Type.__name__ = "IpeAdminStatus"
_ProvEtherRingAdminStatus_Object = MibTableColumn
provEtherRingAdminStatus = _ProvEtherRingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 1, 1, 5),
    _ProvEtherRingAdminStatus_Type()
)
provEtherRingAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provEtherRingAdminStatus.setStatus("current")
_ProvEtherRingRowStatus_Type = RowStatus
_ProvEtherRingRowStatus_Object = MibTableColumn
provEtherRingRowStatus = _ProvEtherRingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 1, 1, 6),
    _ProvEtherRingRowStatus_Type()
)
provEtherRingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provEtherRingRowStatus.setStatus("current")
_ProvEtherRingType_Type = IpeRingType
_ProvEtherRingType_Object = MibTableColumn
provEtherRingType = _ProvEtherRingType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 1, 1, 7),
    _ProvEtherRingType_Type()
)
provEtherRingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provEtherRingType.setStatus("current")
_ProvEtherRingInterConnTable_Object = MibTable
provEtherRingInterConnTable = _ProvEtherRingInterConnTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 2)
)
if mibBuilder.loadTexts:
    provEtherRingInterConnTable.setStatus("current")
_ProvEtherRingInterConnEntry_Object = MibTableRow
provEtherRingInterConnEntry = _ProvEtherRingInterConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 2, 1)
)
provEtherRingInterConnEntry.setIndexNames(
    (0, "IPE-ETH-RING-MIB", "provEtherRingInterConnRingIndex"),
)
if mibBuilder.loadTexts:
    provEtherRingInterConnEntry.setStatus("current")
_ProvEtherRingInterConnRingIndex_Type = IpeEtherRingIndex
_ProvEtherRingInterConnRingIndex_Object = MibTableColumn
provEtherRingInterConnRingIndex = _ProvEtherRingInterConnRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 2, 1, 1),
    _ProvEtherRingInterConnRingIndex_Type()
)
provEtherRingInterConnRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provEtherRingInterConnRingIndex.setStatus("current")
_ProvEtherRingInterConnNEAddress_Type = IpAddress
_ProvEtherRingInterConnNEAddress_Object = MibTableColumn
provEtherRingInterConnNEAddress = _ProvEtherRingInterConnNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 2, 1, 2),
    _ProvEtherRingInterConnNEAddress_Type()
)
provEtherRingInterConnNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provEtherRingInterConnNEAddress.setStatus("current")


class _ProvEtherRingInterConnProtoVersion_Type(IpeEtherRingProtoVersion):
    """Custom type provEtherRingInterConnProtoVersion based on IpeEtherRingProtoVersion"""
    defaultValue = 2


_ProvEtherRingInterConnProtoVersion_Type.__name__ = "IpeEtherRingProtoVersion"
_ProvEtherRingInterConnProtoVersion_Object = MibTableColumn
provEtherRingInterConnProtoVersion = _ProvEtherRingInterConnProtoVersion_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 2, 1, 3),
    _ProvEtherRingInterConnProtoVersion_Type()
)
provEtherRingInterConnProtoVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provEtherRingInterConnProtoVersion.setStatus("current")
_ProvEtherRingInterConnUpperRingIndex_Type = IpeEtherRingIndexOrZero
_ProvEtherRingInterConnUpperRingIndex_Object = MibTableColumn
provEtherRingInterConnUpperRingIndex = _ProvEtherRingInterConnUpperRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 2, 1, 4),
    _ProvEtherRingInterConnUpperRingIndex_Type()
)
provEtherRingInterConnUpperRingIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provEtherRingInterConnUpperRingIndex.setStatus("current")


class _ProvEtherRingInterConnName_Type(DisplayString):
    """Custom type provEtherRingInterConnName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProvEtherRingInterConnName_Type.__name__ = "DisplayString"
_ProvEtherRingInterConnName_Object = MibTableColumn
provEtherRingInterConnName = _ProvEtherRingInterConnName_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 2, 1, 5),
    _ProvEtherRingInterConnName_Type()
)
provEtherRingInterConnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provEtherRingInterConnName.setStatus("current")


class _ProvEtherRingInterConnAdminStatus_Type(IpeAdminStatus):
    """Custom type provEtherRingInterConnAdminStatus based on IpeAdminStatus"""
    defaultValue = 1


_ProvEtherRingInterConnAdminStatus_Type.__name__ = "IpeAdminStatus"
_ProvEtherRingInterConnAdminStatus_Object = MibTableColumn
provEtherRingInterConnAdminStatus = _ProvEtherRingInterConnAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 2, 1, 6),
    _ProvEtherRingInterConnAdminStatus_Type()
)
provEtherRingInterConnAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provEtherRingInterConnAdminStatus.setStatus("current")


class _ProvEtherRingInterConnFlushPropagate_Type(IpeEnableDisableValue):
    """Custom type provEtherRingInterConnFlushPropagate based on IpeEnableDisableValue"""
    defaultValue = 2


_ProvEtherRingInterConnFlushPropagate_Type.__name__ = "IpeEnableDisableValue"
_ProvEtherRingInterConnFlushPropagate_Object = MibTableColumn
provEtherRingInterConnFlushPropagate = _ProvEtherRingInterConnFlushPropagate_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 2, 1, 7),
    _ProvEtherRingInterConnFlushPropagate_Type()
)
provEtherRingInterConnFlushPropagate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provEtherRingInterConnFlushPropagate.setStatus("current")
_ProvEtherRingInterConnRowStatus_Type = RowStatus
_ProvEtherRingInterConnRowStatus_Object = MibTableColumn
provEtherRingInterConnRowStatus = _ProvEtherRingInterConnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 2, 1, 8),
    _ProvEtherRingInterConnRowStatus_Type()
)
provEtherRingInterConnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provEtherRingInterConnRowStatus.setStatus("current")
_ProvEtherRingPortTable_Object = MibTable
provEtherRingPortTable = _ProvEtherRingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 3)
)
if mibBuilder.loadTexts:
    provEtherRingPortTable.setStatus("current")
_ProvEtherRingPortEntry_Object = MibTableRow
provEtherRingPortEntry = _ProvEtherRingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 3, 1)
)
provEtherRingPortEntry.setIndexNames(
    (0, "IPE-ETH-RING-MIB", "provEtherRingPortRingIndex"),
    (0, "IPE-ETH-RING-MIB", "provEtherRingPortId"),
)
if mibBuilder.loadTexts:
    provEtherRingPortEntry.setStatus("current")
_ProvEtherRingPortRingIndex_Type = IpeEtherRingIndex
_ProvEtherRingPortRingIndex_Object = MibTableColumn
provEtherRingPortRingIndex = _ProvEtherRingPortRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 3, 1, 1),
    _ProvEtherRingPortRingIndex_Type()
)
provEtherRingPortRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provEtherRingPortRingIndex.setStatus("current")
_ProvEtherRingPortId_Type = IpeEtherRingPortId
_ProvEtherRingPortId_Object = MibTableColumn
provEtherRingPortId = _ProvEtherRingPortId_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 3, 1, 2),
    _ProvEtherRingPortId_Type()
)
provEtherRingPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provEtherRingPortId.setStatus("current")
_ProvEtherRingPortNEAddress_Type = IpAddress
_ProvEtherRingPortNEAddress_Object = MibTableColumn
provEtherRingPortNEAddress = _ProvEtherRingPortNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 3, 1, 3),
    _ProvEtherRingPortNEAddress_Type()
)
provEtherRingPortNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provEtherRingPortNEAddress.setStatus("current")
_ProvEtherRingPortRowStatus_Type = RowStatus
_ProvEtherRingPortRowStatus_Object = MibTableColumn
provEtherRingPortRowStatus = _ProvEtherRingPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 3, 1, 4),
    _ProvEtherRingPortRowStatus_Type()
)
provEtherRingPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provEtherRingPortRowStatus.setStatus("current")
_ProvEtherRingPortIfIndex_Type = InterfaceIndex
_ProvEtherRingPortIfIndex_Object = MibTableColumn
provEtherRingPortIfIndex = _ProvEtherRingPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 3, 1, 5),
    _ProvEtherRingPortIfIndex_Type()
)
provEtherRingPortIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provEtherRingPortIfIndex.setStatus("current")


class _ProvEtherRingPortLocDetectMep_Type(IpeMepIdOrZero):
    """Custom type provEtherRingPortLocDetectMep based on IpeMepIdOrZero"""
    defaultValue = 0


_ProvEtherRingPortLocDetectMep_Type.__name__ = "IpeMepIdOrZero"
_ProvEtherRingPortLocDetectMep_Object = MibTableColumn
provEtherRingPortLocDetectMep = _ProvEtherRingPortLocDetectMep_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 3, 1, 6),
    _ProvEtherRingPortLocDetectMep_Type()
)
provEtherRingPortLocDetectMep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provEtherRingPortLocDetectMep.setStatus("current")
_ProvEtherRingVirtualChannelTable_Object = MibTable
provEtherRingVirtualChannelTable = _ProvEtherRingVirtualChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 4)
)
if mibBuilder.loadTexts:
    provEtherRingVirtualChannelTable.setStatus("current")
_ProvEtherRingVirtualChannelEntry_Object = MibTableRow
provEtherRingVirtualChannelEntry = _ProvEtherRingVirtualChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 4, 1)
)
provEtherRingVirtualChannelEntry.setIndexNames(
    (0, "IPE-ETH-RING-MIB", "provEtherRingVirtualChannelRingIndex"),
)
if mibBuilder.loadTexts:
    provEtherRingVirtualChannelEntry.setStatus("current")
_ProvEtherRingVirtualChannelRingIndex_Type = IpeEtherRingIndex
_ProvEtherRingVirtualChannelRingIndex_Object = MibTableColumn
provEtherRingVirtualChannelRingIndex = _ProvEtherRingVirtualChannelRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 4, 1, 1),
    _ProvEtherRingVirtualChannelRingIndex_Type()
)
provEtherRingVirtualChannelRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provEtherRingVirtualChannelRingIndex.setStatus("current")
_ProvEtherRingVirtualChannelNEAddress_Type = IpAddress
_ProvEtherRingVirtualChannelNEAddress_Object = MibTableColumn
provEtherRingVirtualChannelNEAddress = _ProvEtherRingVirtualChannelNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 4, 1, 2),
    _ProvEtherRingVirtualChannelNEAddress_Type()
)
provEtherRingVirtualChannelNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provEtherRingVirtualChannelNEAddress.setStatus("current")


class _ProvEtherRingVirtualChannelEnabled_Type(IpeEnableDisableValue):
    """Custom type provEtherRingVirtualChannelEnabled based on IpeEnableDisableValue"""
    defaultValue = 2


_ProvEtherRingVirtualChannelEnabled_Type.__name__ = "IpeEnableDisableValue"
_ProvEtherRingVirtualChannelEnabled_Object = MibTableColumn
provEtherRingVirtualChannelEnabled = _ProvEtherRingVirtualChannelEnabled_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 4, 1, 3),
    _ProvEtherRingVirtualChannelEnabled_Type()
)
provEtherRingVirtualChannelEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provEtherRingVirtualChannelEnabled.setStatus("current")
_ProvEtherRingCtrlVlanTable_Object = MibTable
provEtherRingCtrlVlanTable = _ProvEtherRingCtrlVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 5)
)
if mibBuilder.loadTexts:
    provEtherRingCtrlVlanTable.setStatus("current")
_ProvEtherRingCtrlVlanEntry_Object = MibTableRow
provEtherRingCtrlVlanEntry = _ProvEtherRingCtrlVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 5, 1)
)
provEtherRingCtrlVlanEntry.setIndexNames(
    (0, "IPE-ETH-RING-MIB", "provEtherRingCtrlVlanRingIndex"),
)
if mibBuilder.loadTexts:
    provEtherRingCtrlVlanEntry.setStatus("current")
_ProvEtherRingCtrlVlanRingIndex_Type = IpeEtherRingIndex
_ProvEtherRingCtrlVlanRingIndex_Object = MibTableColumn
provEtherRingCtrlVlanRingIndex = _ProvEtherRingCtrlVlanRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 5, 1, 1),
    _ProvEtherRingCtrlVlanRingIndex_Type()
)
provEtherRingCtrlVlanRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provEtherRingCtrlVlanRingIndex.setStatus("current")
_ProvEtherRingCtrlVlanNEAddress_Type = IpAddress
_ProvEtherRingCtrlVlanNEAddress_Object = MibTableColumn
provEtherRingCtrlVlanNEAddress = _ProvEtherRingCtrlVlanNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 5, 1, 2),
    _ProvEtherRingCtrlVlanNEAddress_Type()
)
provEtherRingCtrlVlanNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provEtherRingCtrlVlanNEAddress.setStatus("current")
_ProvEtherRingCtrlVlanId_Type = IpeEtherRingVlanIndex
_ProvEtherRingCtrlVlanId_Object = MibTableColumn
provEtherRingCtrlVlanId = _ProvEtherRingCtrlVlanId_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 5, 1, 3),
    _ProvEtherRingCtrlVlanId_Type()
)
provEtherRingCtrlVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provEtherRingCtrlVlanId.setStatus("current")


class _ProvEtherRingCtrlVlanRingId_Type(Integer32):
    """Custom type provEtherRingCtrlVlanRingId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 239),
    )


_ProvEtherRingCtrlVlanRingId_Type.__name__ = "Integer32"
_ProvEtherRingCtrlVlanRingId_Object = MibTableColumn
provEtherRingCtrlVlanRingId = _ProvEtherRingCtrlVlanRingId_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 5, 1, 4),
    _ProvEtherRingCtrlVlanRingId_Type()
)
provEtherRingCtrlVlanRingId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provEtherRingCtrlVlanRingId.setStatus("current")


class _ProvEtherRingCtrlVlanMegLevel_Type(Integer32):
    """Custom type provEtherRingCtrlVlanMegLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ProvEtherRingCtrlVlanMegLevel_Type.__name__ = "Integer32"
_ProvEtherRingCtrlVlanMegLevel_Object = MibTableColumn
provEtherRingCtrlVlanMegLevel = _ProvEtherRingCtrlVlanMegLevel_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 5, 1, 5),
    _ProvEtherRingCtrlVlanMegLevel_Type()
)
provEtherRingCtrlVlanMegLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provEtherRingCtrlVlanMegLevel.setStatus("current")


class _ProvEtherRingCtrlVlanPriority_Type(Integer32):
    """Custom type provEtherRingCtrlVlanPriority based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ProvEtherRingCtrlVlanPriority_Type.__name__ = "Integer32"
_ProvEtherRingCtrlVlanPriority_Object = MibTableColumn
provEtherRingCtrlVlanPriority = _ProvEtherRingCtrlVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 5, 1, 6),
    _ProvEtherRingCtrlVlanPriority_Type()
)
provEtherRingCtrlVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provEtherRingCtrlVlanPriority.setStatus("current")
_ProvEtherRingMemberVlanTable_Object = MibTable
provEtherRingMemberVlanTable = _ProvEtherRingMemberVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 6)
)
if mibBuilder.loadTexts:
    provEtherRingMemberVlanTable.setStatus("current")
_ProvEtherRingMemberVlanEntry_Object = MibTableRow
provEtherRingMemberVlanEntry = _ProvEtherRingMemberVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 6, 1)
)
provEtherRingMemberVlanEntry.setIndexNames(
    (0, "IPE-ETH-RING-MIB", "provEtherRingMemberVlanRingIndex"),
)
if mibBuilder.loadTexts:
    provEtherRingMemberVlanEntry.setStatus("current")
_ProvEtherRingMemberVlanRingIndex_Type = IpeEtherRingIndex
_ProvEtherRingMemberVlanRingIndex_Object = MibTableColumn
provEtherRingMemberVlanRingIndex = _ProvEtherRingMemberVlanRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 6, 1, 1),
    _ProvEtherRingMemberVlanRingIndex_Type()
)
provEtherRingMemberVlanRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provEtherRingMemberVlanRingIndex.setStatus("current")
_ProvEtherRingMemberVlanNEAddress_Type = IpAddress
_ProvEtherRingMemberVlanNEAddress_Object = MibTableColumn
provEtherRingMemberVlanNEAddress = _ProvEtherRingMemberVlanNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 6, 1, 2),
    _ProvEtherRingMemberVlanNEAddress_Type()
)
provEtherRingMemberVlanNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provEtherRingMemberVlanNEAddress.setStatus("current")
_ProvEtherRingMemberVlanList_Type = IpeVlanList
_ProvEtherRingMemberVlanList_Object = MibTableColumn
provEtherRingMemberVlanList = _ProvEtherRingMemberVlanList_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 6, 1, 3),
    _ProvEtherRingMemberVlanList_Type()
)
provEtherRingMemberVlanList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provEtherRingMemberVlanList.setStatus("current")
_ProvEtherRingRPLPortTable_Object = MibTable
provEtherRingRPLPortTable = _ProvEtherRingRPLPortTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 7)
)
if mibBuilder.loadTexts:
    provEtherRingRPLPortTable.setStatus("current")
_ProvEtherRingRPLPortEntry_Object = MibTableRow
provEtherRingRPLPortEntry = _ProvEtherRingRPLPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 7, 1)
)
provEtherRingRPLPortEntry.setIndexNames(
    (0, "IPE-ETH-RING-MIB", "provEtherRingRPLPortRingIndex"),
)
if mibBuilder.loadTexts:
    provEtherRingRPLPortEntry.setStatus("current")
_ProvEtherRingRPLPortRingIndex_Type = IpeEtherRingIndex
_ProvEtherRingRPLPortRingIndex_Object = MibTableColumn
provEtherRingRPLPortRingIndex = _ProvEtherRingRPLPortRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 7, 1, 1),
    _ProvEtherRingRPLPortRingIndex_Type()
)
provEtherRingRPLPortRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provEtherRingRPLPortRingIndex.setStatus("current")
_ProvEtherRingRPLPortNEAddress_Type = IpAddress
_ProvEtherRingRPLPortNEAddress_Object = MibTableColumn
provEtherRingRPLPortNEAddress = _ProvEtherRingRPLPortNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 7, 1, 2),
    _ProvEtherRingRPLPortNEAddress_Type()
)
provEtherRingRPLPortNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provEtherRingRPLPortNEAddress.setStatus("current")


class _ProvEtherRingRPLPortEnable_Type(IpeEnableDisableValue):
    """Custom type provEtherRingRPLPortEnable based on IpeEnableDisableValue"""
    defaultValue = 1


_ProvEtherRingRPLPortEnable_Type.__name__ = "IpeEnableDisableValue"
_ProvEtherRingRPLPortEnable_Object = MibTableColumn
provEtherRingRPLPortEnable = _ProvEtherRingRPLPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 7, 1, 3),
    _ProvEtherRingRPLPortEnable_Type()
)
provEtherRingRPLPortEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provEtherRingRPLPortEnable.setStatus("current")


class _ProvEtherRingRPLPortId_Type(IpeEtherRingPortIdOrZero):
    """Custom type provEtherRingRPLPortId based on IpeEtherRingPortIdOrZero"""
    defaultValue = 0


_ProvEtherRingRPLPortId_Type.__name__ = "IpeEtherRingPortIdOrZero"
_ProvEtherRingRPLPortId_Object = MibTableColumn
provEtherRingRPLPortId = _ProvEtherRingRPLPortId_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 7, 1, 4),
    _ProvEtherRingRPLPortId_Type()
)
provEtherRingRPLPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provEtherRingRPLPortId.setStatus("current")


class _ProvEtherRingRPLMode_Type(Integer32):
    """Custom type provEtherRingRPLMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("revertive", 1),
          ("nonRevertive", 2))
    )


_ProvEtherRingRPLMode_Type.__name__ = "Integer32"
_ProvEtherRingRPLMode_Object = MibTableColumn
provEtherRingRPLMode = _ProvEtherRingRPLMode_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 7, 1, 5),
    _ProvEtherRingRPLMode_Type()
)
provEtherRingRPLMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provEtherRingRPLMode.setStatus("current")
_ProvEtherRingTimerTable_Object = MibTable
provEtherRingTimerTable = _ProvEtherRingTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 8)
)
if mibBuilder.loadTexts:
    provEtherRingTimerTable.setStatus("current")
_ProvEtherRingTimerEntry_Object = MibTableRow
provEtherRingTimerEntry = _ProvEtherRingTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 8, 1)
)
provEtherRingTimerEntry.setIndexNames(
    (0, "IPE-ETH-RING-MIB", "provEtherRingTimerRingIndex"),
)
if mibBuilder.loadTexts:
    provEtherRingTimerEntry.setStatus("current")
_ProvEtherRingTimerRingIndex_Type = IpeEtherRingIndex
_ProvEtherRingTimerRingIndex_Object = MibTableColumn
provEtherRingTimerRingIndex = _ProvEtherRingTimerRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 8, 1, 1),
    _ProvEtherRingTimerRingIndex_Type()
)
provEtherRingTimerRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provEtherRingTimerRingIndex.setStatus("current")
_ProvEtherRingTimerNEAddress_Type = IpAddress
_ProvEtherRingTimerNEAddress_Object = MibTableColumn
provEtherRingTimerNEAddress = _ProvEtherRingTimerNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 8, 1, 2),
    _ProvEtherRingTimerNEAddress_Type()
)
provEtherRingTimerNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provEtherRingTimerNEAddress.setStatus("current")


class _ProvEtherRingTimerWtrTimer_Type(Integer32):
    """Custom type provEtherRingTimerWtrTimer based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_ProvEtherRingTimerWtrTimer_Type.__name__ = "Integer32"
_ProvEtherRingTimerWtrTimer_Object = MibTableColumn
provEtherRingTimerWtrTimer = _ProvEtherRingTimerWtrTimer_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 8, 1, 3),
    _ProvEtherRingTimerWtrTimer_Type()
)
provEtherRingTimerWtrTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provEtherRingTimerWtrTimer.setStatus("current")
if mibBuilder.loadTexts:
    provEtherRingTimerWtrTimer.setUnits("minutes")


class _ProvEtherRingTimerGrdTimer_Type(Integer32):
    """Custom type provEtherRingTimerGrdTimer based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_ProvEtherRingTimerGrdTimer_Type.__name__ = "Integer32"
_ProvEtherRingTimerGrdTimer_Object = MibTableColumn
provEtherRingTimerGrdTimer = _ProvEtherRingTimerGrdTimer_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 8, 1, 4),
    _ProvEtherRingTimerGrdTimer_Type()
)
provEtherRingTimerGrdTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provEtherRingTimerGrdTimer.setStatus("current")
if mibBuilder.loadTexts:
    provEtherRingTimerGrdTimer.setUnits("10 milliseconds")
_ProvEtherRingExtraTimerTable_Object = MibTable
provEtherRingExtraTimerTable = _ProvEtherRingExtraTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 9)
)
if mibBuilder.loadTexts:
    provEtherRingExtraTimerTable.setStatus("current")
_ProvEtherRingExtraTimerEntry_Object = MibTableRow
provEtherRingExtraTimerEntry = _ProvEtherRingExtraTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 9, 1)
)
provEtherRingExtraTimerEntry.setIndexNames(
    (0, "IPE-ETH-RING-MIB", "provEtherRingExtraTimerRingIndex"),
)
if mibBuilder.loadTexts:
    provEtherRingExtraTimerEntry.setStatus("current")
_ProvEtherRingExtraTimerRingIndex_Type = IpeEtherRingIndex
_ProvEtherRingExtraTimerRingIndex_Object = MibTableColumn
provEtherRingExtraTimerRingIndex = _ProvEtherRingExtraTimerRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 9, 1, 1),
    _ProvEtherRingExtraTimerRingIndex_Type()
)
provEtherRingExtraTimerRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provEtherRingExtraTimerRingIndex.setStatus("current")
_ProvEtherRingExtraTimerNEAddress_Type = IpAddress
_ProvEtherRingExtraTimerNEAddress_Object = MibTableColumn
provEtherRingExtraTimerNEAddress = _ProvEtherRingExtraTimerNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 9, 1, 2),
    _ProvEtherRingExtraTimerNEAddress_Type()
)
provEtherRingExtraTimerNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provEtherRingExtraTimerNEAddress.setStatus("current")


class _ProvEtherRingExtraTimerFlushGrd_Type(Integer32):
    """Custom type provEtherRingExtraTimerFlushGrd based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_ProvEtherRingExtraTimerFlushGrd_Type.__name__ = "Integer32"
_ProvEtherRingExtraTimerFlushGrd_Object = MibTableColumn
provEtherRingExtraTimerFlushGrd = _ProvEtherRingExtraTimerFlushGrd_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 9, 1, 3),
    _ProvEtherRingExtraTimerFlushGrd_Type()
)
provEtherRingExtraTimerFlushGrd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provEtherRingExtraTimerFlushGrd.setStatus("current")
if mibBuilder.loadTexts:
    provEtherRingExtraTimerFlushGrd.setUnits("10 milliseconds")
_ProvEtherRingEquipmentTable_Object = MibTable
provEtherRingEquipmentTable = _ProvEtherRingEquipmentTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 10)
)
if mibBuilder.loadTexts:
    provEtherRingEquipmentTable.setStatus("current")
_ProvEtherRingEquipmentEntry_Object = MibTableRow
provEtherRingEquipmentEntry = _ProvEtherRingEquipmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 10, 1)
)
provEtherRingEquipmentEntry.setIndexNames(
    (0, "IPE-ETH-RING-MIB", "provEtherRingEquipmentIndex"),
)
if mibBuilder.loadTexts:
    provEtherRingEquipmentEntry.setStatus("current")


class _ProvEtherRingEquipmentIndex_Type(Integer32):
    """Custom type provEtherRingEquipmentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_ProvEtherRingEquipmentIndex_Type.__name__ = "Integer32"
_ProvEtherRingEquipmentIndex_Object = MibTableColumn
provEtherRingEquipmentIndex = _ProvEtherRingEquipmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 10, 1, 1),
    _ProvEtherRingEquipmentIndex_Type()
)
provEtherRingEquipmentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provEtherRingEquipmentIndex.setStatus("current")
_ProvEtherRingEquipmentNEAddress_Type = IpAddress
_ProvEtherRingEquipmentNEAddress_Object = MibTableColumn
provEtherRingEquipmentNEAddress = _ProvEtherRingEquipmentNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 10, 1, 2),
    _ProvEtherRingEquipmentNEAddress_Type()
)
provEtherRingEquipmentNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provEtherRingEquipmentNEAddress.setStatus("current")


class _ProvEtherRingEquipmentEnable_Type(IpeEnableDisableValue):
    """Custom type provEtherRingEquipmentEnable based on IpeEnableDisableValue"""
    defaultValue = 1


_ProvEtherRingEquipmentEnable_Type.__name__ = "IpeEnableDisableValue"
_ProvEtherRingEquipmentEnable_Object = MibTableColumn
provEtherRingEquipmentEnable = _ProvEtherRingEquipmentEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 39, 10, 1, 3),
    _ProvEtherRingEquipmentEnable_Type()
)
provEtherRingEquipmentEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provEtherRingEquipmentEnable.setStatus("current")
_MaintenanceGroup_ObjectIdentity = ObjectIdentity
maintenanceGroup = _MaintenanceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6)
)
_MaintEtherRingGroup_ObjectIdentity = ObjectIdentity
maintEtherRingGroup = _MaintEtherRingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 39)
)
_MaintEtherRingLoopDetectClearTable_Object = MibTable
maintEtherRingLoopDetectClearTable = _MaintEtherRingLoopDetectClearTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 39, 1)
)
if mibBuilder.loadTexts:
    maintEtherRingLoopDetectClearTable.setStatus("current")
_MaintEtherRingLoopDetectClearEntry_Object = MibTableRow
maintEtherRingLoopDetectClearEntry = _MaintEtherRingLoopDetectClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 39, 1, 1)
)
maintEtherRingLoopDetectClearEntry.setIndexNames(
    (0, "IPE-ETH-RING-MIB", "maintEtherRingLoopDetectClearRingId"),
    (0, "IPE-ETH-RING-MIB", "maintEtherRingLoopDetectClearPortId"),
)
if mibBuilder.loadTexts:
    maintEtherRingLoopDetectClearEntry.setStatus("current")
_MaintEtherRingLoopDetectClearRingId_Type = IpeEtherRingIndex
_MaintEtherRingLoopDetectClearRingId_Object = MibTableColumn
maintEtherRingLoopDetectClearRingId = _MaintEtherRingLoopDetectClearRingId_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 39, 1, 1, 1),
    _MaintEtherRingLoopDetectClearRingId_Type()
)
maintEtherRingLoopDetectClearRingId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    maintEtherRingLoopDetectClearRingId.setStatus("current")
_MaintEtherRingLoopDetectClearPortId_Type = IpeEtherRingPortId
_MaintEtherRingLoopDetectClearPortId_Object = MibTableColumn
maintEtherRingLoopDetectClearPortId = _MaintEtherRingLoopDetectClearPortId_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 39, 1, 1, 2),
    _MaintEtherRingLoopDetectClearPortId_Type()
)
maintEtherRingLoopDetectClearPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    maintEtherRingLoopDetectClearPortId.setStatus("current")
_MaintEtherRingLoopDetectClearNEAddress_Type = IpAddress
_MaintEtherRingLoopDetectClearNEAddress_Object = MibTableColumn
maintEtherRingLoopDetectClearNEAddress = _MaintEtherRingLoopDetectClearNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 39, 1, 1, 3),
    _MaintEtherRingLoopDetectClearNEAddress_Type()
)
maintEtherRingLoopDetectClearNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    maintEtherRingLoopDetectClearNEAddress.setStatus("current")


class _MaintEtherRingLoopDetectClearCommand_Type(Integer32):
    """Custom type maintEtherRingLoopDetectClearCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("none", 1),
          ("clear", 2))
    )


_MaintEtherRingLoopDetectClearCommand_Type.__name__ = "Integer32"
_MaintEtherRingLoopDetectClearCommand_Object = MibTableColumn
maintEtherRingLoopDetectClearCommand = _MaintEtherRingLoopDetectClearCommand_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 39, 1, 1, 4),
    _MaintEtherRingLoopDetectClearCommand_Type()
)
maintEtherRingLoopDetectClearCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintEtherRingLoopDetectClearCommand.setStatus("current")
_MaintEtherRingSwitchControlTable_Object = MibTable
maintEtherRingSwitchControlTable = _MaintEtherRingSwitchControlTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 39, 2)
)
if mibBuilder.loadTexts:
    maintEtherRingSwitchControlTable.setStatus("current")
_MaintEtherRingSwitchControlEntry_Object = MibTableRow
maintEtherRingSwitchControlEntry = _MaintEtherRingSwitchControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 39, 2, 1)
)
maintEtherRingSwitchControlEntry.setIndexNames(
    (0, "IPE-ETH-RING-MIB", "maintEtherRingSwitchControlRingId"),
    (0, "IPE-ETH-RING-MIB", "maintEtherRingSwitchControlPortId"),
)
if mibBuilder.loadTexts:
    maintEtherRingSwitchControlEntry.setStatus("current")
_MaintEtherRingSwitchControlRingId_Type = IpeEtherRingIndex
_MaintEtherRingSwitchControlRingId_Object = MibTableColumn
maintEtherRingSwitchControlRingId = _MaintEtherRingSwitchControlRingId_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 39, 2, 1, 1),
    _MaintEtherRingSwitchControlRingId_Type()
)
maintEtherRingSwitchControlRingId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    maintEtherRingSwitchControlRingId.setStatus("current")
_MaintEtherRingSwitchControlPortId_Type = IpeEtherRingPortId
_MaintEtherRingSwitchControlPortId_Object = MibTableColumn
maintEtherRingSwitchControlPortId = _MaintEtherRingSwitchControlPortId_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 39, 2, 1, 2),
    _MaintEtherRingSwitchControlPortId_Type()
)
maintEtherRingSwitchControlPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    maintEtherRingSwitchControlPortId.setStatus("current")
_MaintEtherRingSwitchControlNEAddress_Type = IpAddress
_MaintEtherRingSwitchControlNEAddress_Object = MibTableColumn
maintEtherRingSwitchControlNEAddress = _MaintEtherRingSwitchControlNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 39, 2, 1, 3),
    _MaintEtherRingSwitchControlNEAddress_Type()
)
maintEtherRingSwitchControlNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    maintEtherRingSwitchControlNEAddress.setStatus("current")


class _MaintEtherRingSwitchControlCommand_Type(Integer32):
    """Custom type maintEtherRingSwitchControlCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("none", 1),
          ("forced", 2),
          ("manual", 3),
          ("clear", 4))
    )


_MaintEtherRingSwitchControlCommand_Type.__name__ = "Integer32"
_MaintEtherRingSwitchControlCommand_Object = MibTableColumn
maintEtherRingSwitchControlCommand = _MaintEtherRingSwitchControlCommand_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 39, 2, 1, 4),
    _MaintEtherRingSwitchControlCommand_Type()
)
maintEtherRingSwitchControlCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintEtherRingSwitchControlCommand.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPE-ETH-RING-MIB",
    **{"IpeAdminStatus": IpeAdminStatus,
       "IpeEnableDisableValue": IpeEnableDisableValue,
       "IpeEtherRingIndex": IpeEtherRingIndex,
       "IpeEtherRingIndexOrZero": IpeEtherRingIndexOrZero,
       "IpeEtherRingPortId": IpeEtherRingPortId,
       "IpeEtherRingPortIdOrZero": IpeEtherRingPortIdOrZero,
       "IpeEtherRingProtoVersion": IpeEtherRingProtoVersion,
       "IpeEtherRingVlanIndex": IpeEtherRingVlanIndex,
       "IpeMepIdOrZero": IpeMepIdOrZero,
       "IpeRingType": IpeRingType,
       "IpeVlanList": IpeVlanList,
       "nec": nec,
       "nec-mib": nec_mib,
       "necProductDepend": necProductDepend,
       "radioEquipment": radioEquipment,
       "pasoNeoIpe-common": pasoNeoIpe_common,
       "alarmStatusGroup": alarmStatusGroup,
       "asEtherRingGroup": asEtherRingGroup,
       "asEtherRingTable": asEtherRingTable,
       "asEtherRingEntry": asEtherRingEntry,
       "asEtherRingRingIndex": asEtherRingRingIndex,
       "asEtherRingNEAddress": asEtherRingNEAddress,
       "asEtherRingState": asEtherRingState,
       "asEtherRingCause": asEtherRingCause,
       "asEtherRingMultiRplOwnerDetect": asEtherRingMultiRplOwnerDetect,
       "asEtherRingPortTable": asEtherRingPortTable,
       "asEtherRingPortEntry": asEtherRingPortEntry,
       "asEtherRingPortRingIndex": asEtherRingPortRingIndex,
       "asEtherRingPortId": asEtherRingPortId,
       "asEtherRingPortNEAddress": asEtherRingPortNEAddress,
       "asEtherRingPortState": asEtherRingPortState,
       "asEtherRingPortLoopDetect": asEtherRingPortLoopDetect,
       "asEtherRingPortProtoTimeout": asEtherRingPortProtoTimeout,
       "provisioningGroup": provisioningGroup,
       "provEtherRingGroup": provEtherRingGroup,
       "provEtherRingTable": provEtherRingTable,
       "provEtherRingEntry": provEtherRingEntry,
       "provEtherRingIndex": provEtherRingIndex,
       "provEtherRingNEAddress": provEtherRingNEAddress,
       "provEtherRingProtoVersion": provEtherRingProtoVersion,
       "provEtherRingName": provEtherRingName,
       "provEtherRingAdminStatus": provEtherRingAdminStatus,
       "provEtherRingRowStatus": provEtherRingRowStatus,
       "provEtherRingType": provEtherRingType,
       "provEtherRingInterConnTable": provEtherRingInterConnTable,
       "provEtherRingInterConnEntry": provEtherRingInterConnEntry,
       "provEtherRingInterConnRingIndex": provEtherRingInterConnRingIndex,
       "provEtherRingInterConnNEAddress": provEtherRingInterConnNEAddress,
       "provEtherRingInterConnProtoVersion": provEtherRingInterConnProtoVersion,
       "provEtherRingInterConnUpperRingIndex": provEtherRingInterConnUpperRingIndex,
       "provEtherRingInterConnName": provEtherRingInterConnName,
       "provEtherRingInterConnAdminStatus": provEtherRingInterConnAdminStatus,
       "provEtherRingInterConnFlushPropagate": provEtherRingInterConnFlushPropagate,
       "provEtherRingInterConnRowStatus": provEtherRingInterConnRowStatus,
       "provEtherRingPortTable": provEtherRingPortTable,
       "provEtherRingPortEntry": provEtherRingPortEntry,
       "provEtherRingPortRingIndex": provEtherRingPortRingIndex,
       "provEtherRingPortId": provEtherRingPortId,
       "provEtherRingPortNEAddress": provEtherRingPortNEAddress,
       "provEtherRingPortRowStatus": provEtherRingPortRowStatus,
       "provEtherRingPortIfIndex": provEtherRingPortIfIndex,
       "provEtherRingPortLocDetectMep": provEtherRingPortLocDetectMep,
       "provEtherRingVirtualChannelTable": provEtherRingVirtualChannelTable,
       "provEtherRingVirtualChannelEntry": provEtherRingVirtualChannelEntry,
       "provEtherRingVirtualChannelRingIndex": provEtherRingVirtualChannelRingIndex,
       "provEtherRingVirtualChannelNEAddress": provEtherRingVirtualChannelNEAddress,
       "provEtherRingVirtualChannelEnabled": provEtherRingVirtualChannelEnabled,
       "provEtherRingCtrlVlanTable": provEtherRingCtrlVlanTable,
       "provEtherRingCtrlVlanEntry": provEtherRingCtrlVlanEntry,
       "provEtherRingCtrlVlanRingIndex": provEtherRingCtrlVlanRingIndex,
       "provEtherRingCtrlVlanNEAddress": provEtherRingCtrlVlanNEAddress,
       "provEtherRingCtrlVlanId": provEtherRingCtrlVlanId,
       "provEtherRingCtrlVlanRingId": provEtherRingCtrlVlanRingId,
       "provEtherRingCtrlVlanMegLevel": provEtherRingCtrlVlanMegLevel,
       "provEtherRingCtrlVlanPriority": provEtherRingCtrlVlanPriority,
       "provEtherRingMemberVlanTable": provEtherRingMemberVlanTable,
       "provEtherRingMemberVlanEntry": provEtherRingMemberVlanEntry,
       "provEtherRingMemberVlanRingIndex": provEtherRingMemberVlanRingIndex,
       "provEtherRingMemberVlanNEAddress": provEtherRingMemberVlanNEAddress,
       "provEtherRingMemberVlanList": provEtherRingMemberVlanList,
       "provEtherRingRPLPortTable": provEtherRingRPLPortTable,
       "provEtherRingRPLPortEntry": provEtherRingRPLPortEntry,
       "provEtherRingRPLPortRingIndex": provEtherRingRPLPortRingIndex,
       "provEtherRingRPLPortNEAddress": provEtherRingRPLPortNEAddress,
       "provEtherRingRPLPortEnable": provEtherRingRPLPortEnable,
       "provEtherRingRPLPortId": provEtherRingRPLPortId,
       "provEtherRingRPLMode": provEtherRingRPLMode,
       "provEtherRingTimerTable": provEtherRingTimerTable,
       "provEtherRingTimerEntry": provEtherRingTimerEntry,
       "provEtherRingTimerRingIndex": provEtherRingTimerRingIndex,
       "provEtherRingTimerNEAddress": provEtherRingTimerNEAddress,
       "provEtherRingTimerWtrTimer": provEtherRingTimerWtrTimer,
       "provEtherRingTimerGrdTimer": provEtherRingTimerGrdTimer,
       "provEtherRingExtraTimerTable": provEtherRingExtraTimerTable,
       "provEtherRingExtraTimerEntry": provEtherRingExtraTimerEntry,
       "provEtherRingExtraTimerRingIndex": provEtherRingExtraTimerRingIndex,
       "provEtherRingExtraTimerNEAddress": provEtherRingExtraTimerNEAddress,
       "provEtherRingExtraTimerFlushGrd": provEtherRingExtraTimerFlushGrd,
       "provEtherRingEquipmentTable": provEtherRingEquipmentTable,
       "provEtherRingEquipmentEntry": provEtherRingEquipmentEntry,
       "provEtherRingEquipmentIndex": provEtherRingEquipmentIndex,
       "provEtherRingEquipmentNEAddress": provEtherRingEquipmentNEAddress,
       "provEtherRingEquipmentEnable": provEtherRingEquipmentEnable,
       "maintenanceGroup": maintenanceGroup,
       "maintEtherRingGroup": maintEtherRingGroup,
       "maintEtherRingLoopDetectClearTable": maintEtherRingLoopDetectClearTable,
       "maintEtherRingLoopDetectClearEntry": maintEtherRingLoopDetectClearEntry,
       "maintEtherRingLoopDetectClearRingId": maintEtherRingLoopDetectClearRingId,
       "maintEtherRingLoopDetectClearPortId": maintEtherRingLoopDetectClearPortId,
       "maintEtherRingLoopDetectClearNEAddress": maintEtherRingLoopDetectClearNEAddress,
       "maintEtherRingLoopDetectClearCommand": maintEtherRingLoopDetectClearCommand,
       "maintEtherRingSwitchControlTable": maintEtherRingSwitchControlTable,
       "maintEtherRingSwitchControlEntry": maintEtherRingSwitchControlEntry,
       "maintEtherRingSwitchControlRingId": maintEtherRingSwitchControlRingId,
       "maintEtherRingSwitchControlPortId": maintEtherRingSwitchControlPortId,
       "maintEtherRingSwitchControlNEAddress": maintEtherRingSwitchControlNEAddress,
       "maintEtherRingSwitchControlCommand": maintEtherRingSwitchControlCommand}
)
