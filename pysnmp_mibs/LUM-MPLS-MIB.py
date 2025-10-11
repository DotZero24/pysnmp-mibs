# SNMP MIB module (LUM-MPLS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-MPLS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:04 2025
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

(lumModules,
 lumMplsMIB) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumModules",
    "lumMplsMIB")

(CommandString,
 MgmtNameString,
 MplsLabel,
 PortNumber) = mibBuilder.importSymbols(
    "LUM-TC",
    "CommandString",
    "MgmtNameString",
    "MplsLabel",
    "PortNumber")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

lumMplsMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 40)
)
if mibBuilder.loadTexts:
    lumMplsMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2016-11-30 00:00",
         "2015-01-23 00:00",
         "2013-10-11 00:00",
         "2013-04-01 00:00",
         "2012-12-20 00:00",
         "2012-03-01 00:00",
         "2011-12-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MplsIdentifier(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_LumMplsConfs_ObjectIdentity = ObjectIdentity
lumMplsConfs = _LumMplsConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 1)
)
_LumMplsGroups_ObjectIdentity = ObjectIdentity
lumMplsGroups = _LumMplsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 1, 1)
)
_LumMplsCompl_ObjectIdentity = ObjectIdentity
lumMplsCompl = _LumMplsCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 1, 2)
)
_LumMplsMIBObjects_ObjectIdentity = ObjectIdentity
lumMplsMIBObjects = _LumMplsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2)
)
_MplsGeneral_ObjectIdentity = ObjectIdentity
mplsGeneral = _MplsGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 1)
)
_MplsGeneralLastChangeTime_Type = DateAndTime
_MplsGeneralLastChangeTime_Object = MibScalar
mplsGeneralLastChangeTime = _MplsGeneralLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 1, 1),
    _MplsGeneralLastChangeTime_Type()
)
mplsGeneralLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsGeneralLastChangeTime.setStatus("current")
_MplsGeneralStateLastChangeTime_Type = DateAndTime
_MplsGeneralStateLastChangeTime_Object = MibScalar
mplsGeneralStateLastChangeTime = _MplsGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 1, 2),
    _MplsGeneralStateLastChangeTime_Type()
)
mplsGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsGeneralStateLastChangeTime.setStatus("current")
_MplsGeneralMplsIfTableSize_Type = Unsigned32
_MplsGeneralMplsIfTableSize_Object = MibScalar
mplsGeneralMplsIfTableSize = _MplsGeneralMplsIfTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 1, 3),
    _MplsGeneralMplsIfTableSize_Type()
)
mplsGeneralMplsIfTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsGeneralMplsIfTableSize.setStatus("current")
_MplsGeneralMplsXCTableSize_Type = Unsigned32
_MplsGeneralMplsXCTableSize_Object = MibScalar
mplsGeneralMplsXCTableSize = _MplsGeneralMplsXCTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 1, 4),
    _MplsGeneralMplsXCTableSize_Type()
)
mplsGeneralMplsXCTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsGeneralMplsXCTableSize.setStatus("current")
_MplsGeneralMplsTunnelTableSize_Type = Unsigned32
_MplsGeneralMplsTunnelTableSize_Object = MibScalar
mplsGeneralMplsTunnelTableSize = _MplsGeneralMplsTunnelTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 1, 5),
    _MplsGeneralMplsTunnelTableSize_Type()
)
mplsGeneralMplsTunnelTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsGeneralMplsTunnelTableSize.setStatus("current")
_MplsGeneralMplsNodeTableSize_Type = Unsigned32
_MplsGeneralMplsNodeTableSize_Object = MibScalar
mplsGeneralMplsNodeTableSize = _MplsGeneralMplsNodeTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 1, 6),
    _MplsGeneralMplsNodeTableSize_Type()
)
mplsGeneralMplsNodeTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsGeneralMplsNodeTableSize.setStatus("current")
_MplsGeneralMplsLspTableSize_Type = Unsigned32
_MplsGeneralMplsLspTableSize_Object = MibScalar
mplsGeneralMplsLspTableSize = _MplsGeneralMplsLspTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 1, 7),
    _MplsGeneralMplsLspTableSize_Type()
)
mplsGeneralMplsLspTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsGeneralMplsLspTableSize.setStatus("current")
_MplsGeneralMplsTnlXLspTableSize_Type = Unsigned32
_MplsGeneralMplsTnlXLspTableSize_Object = MibScalar
mplsGeneralMplsTnlXLspTableSize = _MplsGeneralMplsTnlXLspTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 1, 8),
    _MplsGeneralMplsTnlXLspTableSize_Type()
)
mplsGeneralMplsTnlXLspTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsGeneralMplsTnlXLspTableSize.setStatus("current")
_MplsIfList_ObjectIdentity = ObjectIdentity
mplsIfList = _MplsIfList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 2)
)
_MplsIfTable_Object = MibTable
mplsIfTable = _MplsIfTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mplsIfTable.setStatus("current")
_MplsIfEntry_Object = MibTableRow
mplsIfEntry = _MplsIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 2, 1, 1)
)
mplsIfEntry.setIndexNames(
    (0, "LUM-MPLS-MIB", "mplsIfIndex"),
)
if mibBuilder.loadTexts:
    mplsIfEntry.setStatus("current")


class _MplsIfIndex_Type(Unsigned32):
    """Custom type mplsIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsIfIndex_Type.__name__ = "Unsigned32"
_MplsIfIndex_Object = MibTableColumn
mplsIfIndex = _MplsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 2, 1, 1, 1),
    _MplsIfIndex_Type()
)
mplsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsIfIndex.setStatus("current")
_MplsIfName_Type = MgmtNameString
_MplsIfName_Object = MibTableColumn
mplsIfName = _MplsIfName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 2, 1, 1, 2),
    _MplsIfName_Type()
)
mplsIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsIfName.setStatus("current")


class _MplsIfSubrack_Type(Unsigned32):
    """Custom type mplsIfSubrack based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsIfSubrack_Type.__name__ = "Unsigned32"
_MplsIfSubrack_Object = MibTableColumn
mplsIfSubrack = _MplsIfSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 2, 1, 1, 3),
    _MplsIfSubrack_Type()
)
mplsIfSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsIfSubrack.setStatus("current")


class _MplsIfSlot_Type(Unsigned32):
    """Custom type mplsIfSlot based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsIfSlot_Type.__name__ = "Unsigned32"
_MplsIfSlot_Object = MibTableColumn
mplsIfSlot = _MplsIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 2, 1, 1, 4),
    _MplsIfSlot_Type()
)
mplsIfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsIfSlot.setStatus("current")


class _MplsIfTxPort_Type(PortNumber):
    """Custom type mplsIfTxPort based on PortNumber"""
    defaultValue = 0


_MplsIfTxPort_Type.__name__ = "PortNumber"
_MplsIfTxPort_Object = MibTableColumn
mplsIfTxPort = _MplsIfTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 2, 1, 1, 5),
    _MplsIfTxPort_Type()
)
mplsIfTxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsIfTxPort.setStatus("current")


class _MplsIfPortIndex_Type(Unsigned32):
    """Custom type mplsIfPortIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsIfPortIndex_Type.__name__ = "Unsigned32"
_MplsIfPortIndex_Object = MibTableColumn
mplsIfPortIndex = _MplsIfPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 2, 1, 1, 6),
    _MplsIfPortIndex_Type()
)
mplsIfPortIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsIfPortIndex.setStatus("current")
_MplsIfPortName_Type = DisplayString
_MplsIfPortName_Object = MibTableColumn
mplsIfPortName = _MplsIfPortName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 2, 1, 1, 7),
    _MplsIfPortName_Type()
)
mplsIfPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsIfPortName.setStatus("current")


class _MplsIfInternalReference_Type(Unsigned32):
    """Custom type mplsIfInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MplsIfInternalReference_Type.__name__ = "Unsigned32"
_MplsIfInternalReference_Object = MibTableColumn
mplsIfInternalReference = _MplsIfInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 2, 1, 1, 8),
    _MplsIfInternalReference_Type()
)
mplsIfInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsIfInternalReference.setStatus("current")


class _MplsIfAdminStatus_Type(Integer32):
    """Custom type mplsIfAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_MplsIfAdminStatus_Type.__name__ = "Integer32"
_MplsIfAdminStatus_Object = MibTableColumn
mplsIfAdminStatus = _MplsIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 2, 1, 1, 9),
    _MplsIfAdminStatus_Type()
)
mplsIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsIfAdminStatus.setStatus("current")


class _MplsIfIdentifier_Type(DisplayString):
    """Custom type mplsIfIdentifier based on DisplayString"""
    defaultValue = OctetString("")


_MplsIfIdentifier_Type.__name__ = "DisplayString"
_MplsIfIdentifier_Object = MibTableColumn
mplsIfIdentifier = _MplsIfIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 2, 1, 1, 10),
    _MplsIfIdentifier_Type()
)
mplsIfIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsIfIdentifier.setStatus("current")
_MplsIfNextHopMacAddress_Type = MacAddress
_MplsIfNextHopMacAddress_Object = MibTableColumn
mplsIfNextHopMacAddress = _MplsIfNextHopMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 2, 1, 1, 11),
    _MplsIfNextHopMacAddress_Type()
)
mplsIfNextHopMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsIfNextHopMacAddress.setStatus("current")
_MplsIfInterfaceMacAddress_Type = MacAddress
_MplsIfInterfaceMacAddress_Object = MibTableColumn
mplsIfInterfaceMacAddress = _MplsIfInterfaceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 2, 1, 1, 12),
    _MplsIfInterfaceMacAddress_Type()
)
mplsIfInterfaceMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsIfInterfaceMacAddress.setStatus("current")


class _MplsIfVlan_Type(Unsigned32):
    """Custom type mplsIfVlan based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_MplsIfVlan_Type.__name__ = "Unsigned32"
_MplsIfVlan_Object = MibTableColumn
mplsIfVlan = _MplsIfVlan_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 2, 1, 1, 13),
    _MplsIfVlan_Type()
)
mplsIfVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsIfVlan.setStatus("current")
_MplsIfRowStatus_Type = RowStatus
_MplsIfRowStatus_Object = MibTableColumn
mplsIfRowStatus = _MplsIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 2, 1, 1, 14),
    _MplsIfRowStatus_Type()
)
mplsIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsIfRowStatus.setStatus("current")


class _MplsIfIfNo_Type(PortNumber):
    """Custom type mplsIfIfNo based on PortNumber"""
    defaultValue = 1


_MplsIfIfNo_Type.__name__ = "PortNumber"
_MplsIfIfNo_Object = MibTableColumn
mplsIfIfNo = _MplsIfIfNo_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 2, 1, 1, 15),
    _MplsIfIfNo_Type()
)
mplsIfIfNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsIfIfNo.setStatus("current")


class _MplsIfResourceType_Type(Integer32):
    """Custom type mplsIfResourceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port", 1),
          ("lag", 2))
    )


_MplsIfResourceType_Type.__name__ = "Integer32"
_MplsIfResourceType_Object = MibTableColumn
mplsIfResourceType = _MplsIfResourceType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 2, 1, 1, 16),
    _MplsIfResourceType_Type()
)
mplsIfResourceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsIfResourceType.setStatus("current")


class _MplsIfLagId_Type(MgmtNameString):
    """Custom type mplsIfLagId based on MgmtNameString"""
    defaultValue = OctetString("")


_MplsIfLagId_Type.__name__ = "MgmtNameString"
_MplsIfLagId_Object = MibTableColumn
mplsIfLagId = _MplsIfLagId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 2, 1, 1, 17),
    _MplsIfLagId_Type()
)
mplsIfLagId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsIfLagId.setStatus("current")
_MplsXCList_ObjectIdentity = ObjectIdentity
mplsXCList = _MplsXCList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 3)
)
_MplsXCTable_Object = MibTable
mplsXCTable = _MplsXCTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 3, 1)
)
if mibBuilder.loadTexts:
    mplsXCTable.setStatus("current")
_MplsXCEntry_Object = MibTableRow
mplsXCEntry = _MplsXCEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 3, 1, 1)
)
mplsXCEntry.setIndexNames(
    (0, "LUM-MPLS-MIB", "mplsXCIndex"),
)
if mibBuilder.loadTexts:
    mplsXCEntry.setStatus("current")


class _MplsXCIndex_Type(Unsigned32):
    """Custom type mplsXCIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsXCIndex_Type.__name__ = "Unsigned32"
_MplsXCIndex_Object = MibTableColumn
mplsXCIndex = _MplsXCIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 3, 1, 1, 1),
    _MplsXCIndex_Type()
)
mplsXCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsXCIndex.setStatus("current")
_MplsXCName_Type = MgmtNameString
_MplsXCName_Object = MibTableColumn
mplsXCName = _MplsXCName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 3, 1, 1, 2),
    _MplsXCName_Type()
)
mplsXCName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsXCName.setStatus("current")


class _MplsXCInternalReference_Type(Unsigned32):
    """Custom type mplsXCInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MplsXCInternalReference_Type.__name__ = "Unsigned32"
_MplsXCInternalReference_Object = MibTableColumn
mplsXCInternalReference = _MplsXCInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 3, 1, 1, 3),
    _MplsXCInternalReference_Type()
)
mplsXCInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsXCInternalReference.setStatus("current")


class _MplsXCIdentifier_Type(DisplayString):
    """Custom type mplsXCIdentifier based on DisplayString"""
    defaultValue = OctetString("")


_MplsXCIdentifier_Type.__name__ = "DisplayString"
_MplsXCIdentifier_Object = MibTableColumn
mplsXCIdentifier = _MplsXCIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 3, 1, 1, 4),
    _MplsXCIdentifier_Type()
)
mplsXCIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsXCIdentifier.setStatus("current")


class _MplsXCInSegmentIfIndex_Type(Unsigned32):
    """Custom type mplsXCInSegmentIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MplsXCInSegmentIfIndex_Type.__name__ = "Unsigned32"
_MplsXCInSegmentIfIndex_Object = MibTableColumn
mplsXCInSegmentIfIndex = _MplsXCInSegmentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 3, 1, 1, 5),
    _MplsXCInSegmentIfIndex_Type()
)
mplsXCInSegmentIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsXCInSegmentIfIndex.setStatus("current")
_MplsXCInSegmentIfName_Type = DisplayString
_MplsXCInSegmentIfName_Object = MibTableColumn
mplsXCInSegmentIfName = _MplsXCInSegmentIfName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 3, 1, 1, 6),
    _MplsXCInSegmentIfName_Type()
)
mplsXCInSegmentIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsXCInSegmentIfName.setStatus("current")
_MplsXCInSegmentLabel_Type = MplsLabel
_MplsXCInSegmentLabel_Object = MibTableColumn
mplsXCInSegmentLabel = _MplsXCInSegmentLabel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 3, 1, 1, 7),
    _MplsXCInSegmentLabel_Type()
)
mplsXCInSegmentLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsXCInSegmentLabel.setStatus("current")


class _MplsXCOutSegmentIfIndex_Type(Unsigned32):
    """Custom type mplsXCOutSegmentIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MplsXCOutSegmentIfIndex_Type.__name__ = "Unsigned32"
_MplsXCOutSegmentIfIndex_Object = MibTableColumn
mplsXCOutSegmentIfIndex = _MplsXCOutSegmentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 3, 1, 1, 8),
    _MplsXCOutSegmentIfIndex_Type()
)
mplsXCOutSegmentIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsXCOutSegmentIfIndex.setStatus("current")
_MplsXCOutSegmentIfName_Type = DisplayString
_MplsXCOutSegmentIfName_Object = MibTableColumn
mplsXCOutSegmentIfName = _MplsXCOutSegmentIfName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 3, 1, 1, 9),
    _MplsXCOutSegmentIfName_Type()
)
mplsXCOutSegmentIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsXCOutSegmentIfName.setStatus("current")
_MplsXCOutSegmentLabel_Type = MplsLabel
_MplsXCOutSegmentLabel_Object = MibTableColumn
mplsXCOutSegmentLabel = _MplsXCOutSegmentLabel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 3, 1, 1, 10),
    _MplsXCOutSegmentLabel_Type()
)
mplsXCOutSegmentLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsXCOutSegmentLabel.setStatus("current")
_MplsXCRowStatus_Type = RowStatus
_MplsXCRowStatus_Object = MibTableColumn
mplsXCRowStatus = _MplsXCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 3, 1, 1, 11),
    _MplsXCRowStatus_Type()
)
mplsXCRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsXCRowStatus.setStatus("current")
_MplsTunnelList_ObjectIdentity = ObjectIdentity
mplsTunnelList = _MplsTunnelList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 4)
)
_MplsTunnelTable_Object = MibTable
mplsTunnelTable = _MplsTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 4, 1)
)
if mibBuilder.loadTexts:
    mplsTunnelTable.setStatus("current")
_MplsTunnelEntry_Object = MibTableRow
mplsTunnelEntry = _MplsTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 4, 1, 1)
)
mplsTunnelEntry.setIndexNames(
    (0, "LUM-MPLS-MIB", "mplsTunnelIndex"),
)
if mibBuilder.loadTexts:
    mplsTunnelEntry.setStatus("current")


class _MplsTunnelIndex_Type(Unsigned32):
    """Custom type mplsTunnelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsTunnelIndex_Type.__name__ = "Unsigned32"
_MplsTunnelIndex_Object = MibTableColumn
mplsTunnelIndex = _MplsTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 4, 1, 1, 1),
    _MplsTunnelIndex_Type()
)
mplsTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelIndex.setStatus("current")


class _MplsTunnelInternalReference_Type(Unsigned32):
    """Custom type mplsTunnelInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MplsTunnelInternalReference_Type.__name__ = "Unsigned32"
_MplsTunnelInternalReference_Object = MibTableColumn
mplsTunnelInternalReference = _MplsTunnelInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 4, 1, 1, 2),
    _MplsTunnelInternalReference_Type()
)
mplsTunnelInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelInternalReference.setStatus("current")


class _MplsTunnelIdentifier_Type(DisplayString):
    """Custom type mplsTunnelIdentifier based on DisplayString"""
    defaultValue = OctetString("")


_MplsTunnelIdentifier_Type.__name__ = "DisplayString"
_MplsTunnelIdentifier_Object = MibTableColumn
mplsTunnelIdentifier = _MplsTunnelIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 4, 1, 1, 3),
    _MplsTunnelIdentifier_Type()
)
mplsTunnelIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelIdentifier.setStatus("current")
_MplsTunnelName_Type = MgmtNameString
_MplsTunnelName_Object = MibTableColumn
mplsTunnelName = _MplsTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 4, 1, 1, 4),
    _MplsTunnelName_Type()
)
mplsTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelName.setStatus("current")


class _MplsTunnelActiveLSP_Type(DisplayString):
    """Custom type mplsTunnelActiveLSP based on DisplayString"""
    defaultValue = OctetString("")


_MplsTunnelActiveLSP_Type.__name__ = "DisplayString"
_MplsTunnelActiveLSP_Object = MibTableColumn
mplsTunnelActiveLSP = _MplsTunnelActiveLSP_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 4, 1, 1, 5),
    _MplsTunnelActiveLSP_Type()
)
mplsTunnelActiveLSP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelActiveLSP.setStatus("current")


class _MplsTunnelActiveLspIndex_Type(Unsigned32):
    """Custom type mplsTunnelActiveLspIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsTunnelActiveLspIndex_Type.__name__ = "Unsigned32"
_MplsTunnelActiveLspIndex_Object = MibTableColumn
mplsTunnelActiveLspIndex = _MplsTunnelActiveLspIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 4, 1, 1, 6),
    _MplsTunnelActiveLspIndex_Type()
)
mplsTunnelActiveLspIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelActiveLspIndex.setStatus("current")


class _MplsTunnelState_Type(Integer32):
    """Custom type mplsTunnelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2),
          ("unknown", 3))
    )


_MplsTunnelState_Type.__name__ = "Integer32"
_MplsTunnelState_Object = MibTableColumn
mplsTunnelState = _MplsTunnelState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 4, 1, 1, 7),
    _MplsTunnelState_Type()
)
mplsTunnelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelState.setStatus("current")


class _MplsTunnelSrcNodeId_Type(Unsigned32):
    """Custom type mplsTunnelSrcNodeId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MplsTunnelSrcNodeId_Type.__name__ = "Unsigned32"
_MplsTunnelSrcNodeId_Object = MibTableColumn
mplsTunnelSrcNodeId = _MplsTunnelSrcNodeId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 4, 1, 1, 8),
    _MplsTunnelSrcNodeId_Type()
)
mplsTunnelSrcNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelSrcNodeId.setStatus("current")


class _MplsTunnelSrcTunnelId_Type(MplsIdentifier):
    """Custom type mplsTunnelSrcTunnelId based on MplsIdentifier"""
    defaultValue = 0


_MplsTunnelSrcTunnelId_Type.__name__ = "MplsIdentifier"
_MplsTunnelSrcTunnelId_Object = MibTableColumn
mplsTunnelSrcTunnelId = _MplsTunnelSrcTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 4, 1, 1, 9),
    _MplsTunnelSrcTunnelId_Type()
)
mplsTunnelSrcTunnelId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsTunnelSrcTunnelId.setStatus("current")


class _MplsTunnelDestNodeId_Type(Unsigned32):
    """Custom type mplsTunnelDestNodeId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MplsTunnelDestNodeId_Type.__name__ = "Unsigned32"
_MplsTunnelDestNodeId_Object = MibTableColumn
mplsTunnelDestNodeId = _MplsTunnelDestNodeId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 4, 1, 1, 10),
    _MplsTunnelDestNodeId_Type()
)
mplsTunnelDestNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsTunnelDestNodeId.setStatus("current")


class _MplsTunnelDestTunnelId_Type(MplsIdentifier):
    """Custom type mplsTunnelDestTunnelId based on MplsIdentifier"""
    defaultValue = 0


_MplsTunnelDestTunnelId_Type.__name__ = "MplsIdentifier"
_MplsTunnelDestTunnelId_Object = MibTableColumn
mplsTunnelDestTunnelId = _MplsTunnelDestTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 4, 1, 1, 11),
    _MplsTunnelDestTunnelId_Type()
)
mplsTunnelDestTunnelId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsTunnelDestTunnelId.setStatus("current")
_MplsTunnelExtId_Type = DisplayString
_MplsTunnelExtId_Object = MibTableColumn
mplsTunnelExtId = _MplsTunnelExtId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 4, 1, 1, 12),
    _MplsTunnelExtId_Type()
)
mplsTunnelExtId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelExtId.setStatus("current")
_MplsTunnelAssociateLSP_Type = CommandString
_MplsTunnelAssociateLSP_Object = MibTableColumn
mplsTunnelAssociateLSP = _MplsTunnelAssociateLSP_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 4, 1, 1, 13),
    _MplsTunnelAssociateLSP_Type()
)
mplsTunnelAssociateLSP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelAssociateLSP.setStatus("current")
_MplsTunnelRowStatus_Type = RowStatus
_MplsTunnelRowStatus_Object = MibTableColumn
mplsTunnelRowStatus = _MplsTunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 4, 1, 1, 14),
    _MplsTunnelRowStatus_Type()
)
mplsTunnelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelRowStatus.setStatus("current")


class _MplsTunnelLinearProtection_Type(DisplayString):
    """Custom type mplsTunnelLinearProtection based on DisplayString"""
    defaultValue = OctetString("none")


_MplsTunnelLinearProtection_Type.__name__ = "DisplayString"
_MplsTunnelLinearProtection_Object = MibTableColumn
mplsTunnelLinearProtection = _MplsTunnelLinearProtection_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 4, 1, 1, 15),
    _MplsTunnelLinearProtection_Type()
)
mplsTunnelLinearProtection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelLinearProtection.setStatus("current")


class _MplsTunnelProtectionState_Type(Integer32):
    """Custom type mplsTunnelProtectionState based on Integer32"""
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
        *(("fullyworking", 1),
          ("degraded", 2),
          ("failed", 3),
          ("unknown", 4))
    )


_MplsTunnelProtectionState_Type.__name__ = "Integer32"
_MplsTunnelProtectionState_Object = MibTableColumn
mplsTunnelProtectionState = _MplsTunnelProtectionState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 4, 1, 1, 16),
    _MplsTunnelProtectionState_Type()
)
mplsTunnelProtectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelProtectionState.setStatus("current")
_MplsTunnelAssociateLinearProt_Type = CommandString
_MplsTunnelAssociateLinearProt_Object = MibTableColumn
mplsTunnelAssociateLinearProt = _MplsTunnelAssociateLinearProt_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 4, 1, 1, 17),
    _MplsTunnelAssociateLinearProt_Type()
)
mplsTunnelAssociateLinearProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelAssociateLinearProt.setStatus("current")


class _MplsTunnelGlobalId_Type(Unsigned32):
    """Custom type mplsTunnelGlobalId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MplsTunnelGlobalId_Type.__name__ = "Unsigned32"
_MplsTunnelGlobalId_Object = MibTableColumn
mplsTunnelGlobalId = _MplsTunnelGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 4, 1, 1, 18),
    _MplsTunnelGlobalId_Type()
)
mplsTunnelGlobalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelGlobalId.setStatus("current")


class _MplsTunnelDestGlobalId_Type(Unsigned32):
    """Custom type mplsTunnelDestGlobalId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MplsTunnelDestGlobalId_Type.__name__ = "Unsigned32"
_MplsTunnelDestGlobalId_Object = MibTableColumn
mplsTunnelDestGlobalId = _MplsTunnelDestGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 4, 1, 1, 19),
    _MplsTunnelDestGlobalId_Type()
)
mplsTunnelDestGlobalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsTunnelDestGlobalId.setStatus("current")
_MplsTunnelWorkingLSP_Type = DisplayString
_MplsTunnelWorkingLSP_Object = MibTableColumn
mplsTunnelWorkingLSP = _MplsTunnelWorkingLSP_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 4, 1, 1, 20),
    _MplsTunnelWorkingLSP_Type()
)
mplsTunnelWorkingLSP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelWorkingLSP.setStatus("current")
_MplsTunnelProtectionLSP_Type = DisplayString
_MplsTunnelProtectionLSP_Object = MibTableColumn
mplsTunnelProtectionLSP = _MplsTunnelProtectionLSP_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 4, 1, 1, 21),
    _MplsTunnelProtectionLSP_Type()
)
mplsTunnelProtectionLSP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelProtectionLSP.setStatus("current")


class _MplsTunnelReservedBW_Type(Unsigned32):
    """Custom type mplsTunnelReservedBW based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MplsTunnelReservedBW_Type.__name__ = "Unsigned32"
_MplsTunnelReservedBW_Object = MibTableColumn
mplsTunnelReservedBW = _MplsTunnelReservedBW_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 4, 1, 1, 22),
    _MplsTunnelReservedBW_Type()
)
mplsTunnelReservedBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsTunnelReservedBW.setStatus("current")
_MplsTunnelBookedBW_Type = Counter64
_MplsTunnelBookedBW_Object = MibTableColumn
mplsTunnelBookedBW = _MplsTunnelBookedBW_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 4, 1, 1, 23),
    _MplsTunnelBookedBW_Type()
)
mplsTunnelBookedBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelBookedBW.setStatus("current")


class _MplsTunnelDescr_Type(DisplayString):
    """Custom type mplsTunnelDescr based on DisplayString"""
    defaultValue = OctetString("")


_MplsTunnelDescr_Type.__name__ = "DisplayString"
_MplsTunnelDescr_Object = MibTableColumn
mplsTunnelDescr = _MplsTunnelDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 4, 1, 1, 24),
    _MplsTunnelDescr_Type()
)
mplsTunnelDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsTunnelDescr.setStatus("current")
_MplsNodeList_ObjectIdentity = ObjectIdentity
mplsNodeList = _MplsNodeList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 5)
)
_MplsNodeTable_Object = MibTable
mplsNodeTable = _MplsNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 5, 1)
)
if mibBuilder.loadTexts:
    mplsNodeTable.setStatus("current")
_MplsNodeEntry_Object = MibTableRow
mplsNodeEntry = _MplsNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 5, 1, 1)
)
mplsNodeEntry.setIndexNames(
    (0, "LUM-MPLS-MIB", "mplsNodeIndex"),
)
if mibBuilder.loadTexts:
    mplsNodeEntry.setStatus("current")


class _MplsNodeIndex_Type(Unsigned32):
    """Custom type mplsNodeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsNodeIndex_Type.__name__ = "Unsigned32"
_MplsNodeIndex_Object = MibTableColumn
mplsNodeIndex = _MplsNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 5, 1, 1, 1),
    _MplsNodeIndex_Type()
)
mplsNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsNodeIndex.setStatus("current")
_MplsNodeName_Type = MgmtNameString
_MplsNodeName_Object = MibTableColumn
mplsNodeName = _MplsNodeName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 5, 1, 1, 2),
    _MplsNodeName_Type()
)
mplsNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsNodeName.setStatus("current")


class _MplsNodeSubrack_Type(Unsigned32):
    """Custom type mplsNodeSubrack based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsNodeSubrack_Type.__name__ = "Unsigned32"
_MplsNodeSubrack_Object = MibTableColumn
mplsNodeSubrack = _MplsNodeSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 5, 1, 1, 3),
    _MplsNodeSubrack_Type()
)
mplsNodeSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsNodeSubrack.setStatus("current")


class _MplsNodeSlot_Type(Unsigned32):
    """Custom type mplsNodeSlot based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsNodeSlot_Type.__name__ = "Unsigned32"
_MplsNodeSlot_Object = MibTableColumn
mplsNodeSlot = _MplsNodeSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 5, 1, 1, 4),
    _MplsNodeSlot_Type()
)
mplsNodeSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsNodeSlot.setStatus("current")


class _MplsNodeIccIdStr_Type(OctetString):
    """Custom type mplsNodeIccIdStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_MplsNodeIccIdStr_Type.__name__ = "OctetString"
_MplsNodeIccIdStr_Object = MibTableColumn
mplsNodeIccIdStr = _MplsNodeIccIdStr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 5, 1, 1, 5),
    _MplsNodeIccIdStr_Type()
)
mplsNodeIccIdStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsNodeIccIdStr.setStatus("current")


class _MplsNodeIdNum_Type(Unsigned32):
    """Custom type mplsNodeIdNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MplsNodeIdNum_Type.__name__ = "Unsigned32"
_MplsNodeIdNum_Object = MibTableColumn
mplsNodeIdNum = _MplsNodeIdNum_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 5, 1, 1, 6),
    _MplsNodeIdNum_Type()
)
mplsNodeIdNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsNodeIdNum.setStatus("current")
_MplsNodeCreateXC_Type = CommandString
_MplsNodeCreateXC_Object = MibTableColumn
mplsNodeCreateXC = _MplsNodeCreateXC_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 5, 1, 1, 7),
    _MplsNodeCreateXC_Type()
)
mplsNodeCreateXC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsNodeCreateXC.setStatus("current")
_MplsNodeCreateTunnel_Type = CommandString
_MplsNodeCreateTunnel_Object = MibTableColumn
mplsNodeCreateTunnel = _MplsNodeCreateTunnel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 5, 1, 1, 8),
    _MplsNodeCreateTunnel_Type()
)
mplsNodeCreateTunnel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsNodeCreateTunnel.setStatus("current")
_MplsNodeCreateLsp_Type = CommandString
_MplsNodeCreateLsp_Object = MibTableColumn
mplsNodeCreateLsp = _MplsNodeCreateLsp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 5, 1, 1, 9),
    _MplsNodeCreateLsp_Type()
)
mplsNodeCreateLsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsNodeCreateLsp.setStatus("current")
_MplsNodeCreatePw_Type = CommandString
_MplsNodeCreatePw_Object = MibTableColumn
mplsNodeCreatePw = _MplsNodeCreatePw_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 5, 1, 1, 10),
    _MplsNodeCreatePw_Type()
)
mplsNodeCreatePw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsNodeCreatePw.setStatus("current")
_MplsNodeCreateIf_Type = CommandString
_MplsNodeCreateIf_Object = MibTableColumn
mplsNodeCreateIf = _MplsNodeCreateIf_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 5, 1, 1, 11),
    _MplsNodeCreateIf_Type()
)
mplsNodeCreateIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsNodeCreateIf.setStatus("current")


class _MplsNodeLinearProtMode_Type(Integer32):
    """Custom type mplsNodeLinearProtMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonRevertive", 1),
          ("revertive", 2))
    )


_MplsNodeLinearProtMode_Type.__name__ = "Integer32"
_MplsNodeLinearProtMode_Object = MibTableColumn
mplsNodeLinearProtMode = _MplsNodeLinearProtMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 5, 1, 1, 12),
    _MplsNodeLinearProtMode_Type()
)
mplsNodeLinearProtMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsNodeLinearProtMode.setStatus("current")


class _MplsNodeLinearProtWtrTimer_Type(Unsigned32):
    """Custom type mplsNodeLinearProtWtrTimer based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 720),
    )


_MplsNodeLinearProtWtrTimer_Type.__name__ = "Unsigned32"
_MplsNodeLinearProtWtrTimer_Object = MibTableColumn
mplsNodeLinearProtWtrTimer = _MplsNodeLinearProtWtrTimer_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 5, 1, 1, 13),
    _MplsNodeLinearProtWtrTimer_Type()
)
mplsNodeLinearProtWtrTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsNodeLinearProtWtrTimer.setStatus("current")


class _MplsNodeLPContMsgInterval_Type(Unsigned32):
    """Custom type mplsNodeLPContMsgInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_MplsNodeLPContMsgInterval_Type.__name__ = "Unsigned32"
_MplsNodeLPContMsgInterval_Object = MibTableColumn
mplsNodeLPContMsgInterval = _MplsNodeLPContMsgInterval_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 5, 1, 1, 14),
    _MplsNodeLPContMsgInterval_Type()
)
mplsNodeLPContMsgInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsNodeLPContMsgInterval.setStatus("current")


class _MplsNodeLPRapidMsgInterval_Type(Unsigned32):
    """Custom type mplsNodeLPRapidMsgInterval based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_MplsNodeLPRapidMsgInterval_Type.__name__ = "Unsigned32"
_MplsNodeLPRapidMsgInterval_Object = MibTableColumn
mplsNodeLPRapidMsgInterval = _MplsNodeLPRapidMsgInterval_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 5, 1, 1, 15),
    _MplsNodeLPRapidMsgInterval_Type()
)
mplsNodeLPRapidMsgInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsNodeLPRapidMsgInterval.setStatus("current")


class _MplsNodeGlobalId_Type(Unsigned32):
    """Custom type mplsNodeGlobalId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MplsNodeGlobalId_Type.__name__ = "Unsigned32"
_MplsNodeGlobalId_Object = MibTableColumn
mplsNodeGlobalId = _MplsNodeGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 5, 1, 1, 16),
    _MplsNodeGlobalId_Type()
)
mplsNodeGlobalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsNodeGlobalId.setStatus("current")
_MplsNodeCreateMsPw_Type = CommandString
_MplsNodeCreateMsPw_Object = MibTableColumn
mplsNodeCreateMsPw = _MplsNodeCreateMsPw_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 5, 1, 1, 17),
    _MplsNodeCreateMsPw_Type()
)
mplsNodeCreateMsPw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsNodeCreateMsPw.setStatus("current")
_MplsNodeCreateLsp2_Type = CommandString
_MplsNodeCreateLsp2_Object = MibTableColumn
mplsNodeCreateLsp2 = _MplsNodeCreateLsp2_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 5, 1, 1, 18),
    _MplsNodeCreateLsp2_Type()
)
mplsNodeCreateLsp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsNodeCreateLsp2.setStatus("current")
_MplsNodeCreateTunnelAdvanced_Type = CommandString
_MplsNodeCreateTunnelAdvanced_Object = MibTableColumn
mplsNodeCreateTunnelAdvanced = _MplsNodeCreateTunnelAdvanced_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 5, 1, 1, 19),
    _MplsNodeCreateTunnelAdvanced_Type()
)
mplsNodeCreateTunnelAdvanced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsNodeCreateTunnelAdvanced.setStatus("current")
_MplsNodeCreateLspAdvanced_Type = CommandString
_MplsNodeCreateLspAdvanced_Object = MibTableColumn
mplsNodeCreateLspAdvanced = _MplsNodeCreateLspAdvanced_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 5, 1, 1, 20),
    _MplsNodeCreateLspAdvanced_Type()
)
mplsNodeCreateLspAdvanced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsNodeCreateLspAdvanced.setStatus("current")
_MplsNodeCreatePwGeneric_Type = CommandString
_MplsNodeCreatePwGeneric_Object = MibTableColumn
mplsNodeCreatePwGeneric = _MplsNodeCreatePwGeneric_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 5, 1, 1, 21),
    _MplsNodeCreatePwGeneric_Type()
)
mplsNodeCreatePwGeneric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsNodeCreatePwGeneric.setStatus("current")
_MplsNodeCreatePwMpls_Type = CommandString
_MplsNodeCreatePwMpls_Object = MibTableColumn
mplsNodeCreatePwMpls = _MplsNodeCreatePwMpls_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 5, 1, 1, 22),
    _MplsNodeCreatePwMpls_Type()
)
mplsNodeCreatePwMpls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsNodeCreatePwMpls.setStatus("current")
_MplsNodeCreatePwEnet_Type = CommandString
_MplsNodeCreatePwEnet_Object = MibTableColumn
mplsNodeCreatePwEnet = _MplsNodeCreatePwEnet_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 5, 1, 1, 23),
    _MplsNodeCreatePwEnet_Type()
)
mplsNodeCreatePwEnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsNodeCreatePwEnet.setStatus("current")
_MplsNodeCreateBfdTemplate_Type = CommandString
_MplsNodeCreateBfdTemplate_Object = MibTableColumn
mplsNodeCreateBfdTemplate = _MplsNodeCreateBfdTemplate_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 5, 1, 1, 24),
    _MplsNodeCreateBfdTemplate_Type()
)
mplsNodeCreateBfdTemplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsNodeCreateBfdTemplate.setStatus("current")
_MplsNodeCreateXCAdvanced_Type = CommandString
_MplsNodeCreateXCAdvanced_Object = MibTableColumn
mplsNodeCreateXCAdvanced = _MplsNodeCreateXCAdvanced_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 5, 1, 1, 25),
    _MplsNodeCreateXCAdvanced_Type()
)
mplsNodeCreateXCAdvanced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsNodeCreateXCAdvanced.setStatus("current")
_MplsLspList_ObjectIdentity = ObjectIdentity
mplsLspList = _MplsLspList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 6)
)
_MplsLspTable_Object = MibTable
mplsLspTable = _MplsLspTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 6, 1)
)
if mibBuilder.loadTexts:
    mplsLspTable.setStatus("current")
_MplsLspEntry_Object = MibTableRow
mplsLspEntry = _MplsLspEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 6, 1, 1)
)
mplsLspEntry.setIndexNames(
    (0, "LUM-MPLS-MIB", "mplsLspIndex"),
)
if mibBuilder.loadTexts:
    mplsLspEntry.setStatus("current")


class _MplsLspIndex_Type(Unsigned32):
    """Custom type mplsLspIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsLspIndex_Type.__name__ = "Unsigned32"
_MplsLspIndex_Object = MibTableColumn
mplsLspIndex = _MplsLspIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 6, 1, 1, 1),
    _MplsLspIndex_Type()
)
mplsLspIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspIndex.setStatus("current")
_MplsLspName_Type = MgmtNameString
_MplsLspName_Object = MibTableColumn
mplsLspName = _MplsLspName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 6, 1, 1, 2),
    _MplsLspName_Type()
)
mplsLspName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspName.setStatus("current")


class _MplsLspInternalReference_Type(Unsigned32):
    """Custom type mplsLspInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MplsLspInternalReference_Type.__name__ = "Unsigned32"
_MplsLspInternalReference_Object = MibTableColumn
mplsLspInternalReference = _MplsLspInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 6, 1, 1, 3),
    _MplsLspInternalReference_Type()
)
mplsLspInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLspInternalReference.setStatus("current")


class _MplsLspIdentifier_Type(DisplayString):
    """Custom type mplsLspIdentifier based on DisplayString"""
    defaultValue = OctetString("")


_MplsLspIdentifier_Type.__name__ = "DisplayString"
_MplsLspIdentifier_Object = MibTableColumn
mplsLspIdentifier = _MplsLspIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 6, 1, 1, 4),
    _MplsLspIdentifier_Type()
)
mplsLspIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLspIdentifier.setStatus("current")


class _MplsLspState_Type(Integer32):
    """Custom type mplsLspState based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("unknown", 3))
    )


_MplsLspState_Type.__name__ = "Integer32"
_MplsLspState_Object = MibTableColumn
mplsLspState = _MplsLspState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 6, 1, 1, 5),
    _MplsLspState_Type()
)
mplsLspState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspState.setStatus("current")


class _MplsLspRole_Type(Integer32):
    """Custom type mplsLspRole based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("edge", 1),
          ("transit", 2))
    )


_MplsLspRole_Type.__name__ = "Integer32"
_MplsLspRole_Object = MibTableColumn
mplsLspRole = _MplsLspRole_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 6, 1, 1, 6),
    _MplsLspRole_Type()
)
mplsLspRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLspRole.setStatus("current")


class _MplsLspForwardXCId_Type(DisplayString):
    """Custom type mplsLspForwardXCId based on DisplayString"""
    defaultValue = OctetString("")


_MplsLspForwardXCId_Type.__name__ = "DisplayString"
_MplsLspForwardXCId_Object = MibTableColumn
mplsLspForwardXCId = _MplsLspForwardXCId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 6, 1, 1, 7),
    _MplsLspForwardXCId_Type()
)
mplsLspForwardXCId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLspForwardXCId.setStatus("current")


class _MplsLspReverseXCId_Type(DisplayString):
    """Custom type mplsLspReverseXCId based on DisplayString"""
    defaultValue = OctetString("")


_MplsLspReverseXCId_Type.__name__ = "DisplayString"
_MplsLspReverseXCId_Object = MibTableColumn
mplsLspReverseXCId = _MplsLspReverseXCId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 6, 1, 1, 8),
    _MplsLspReverseXCId_Type()
)
mplsLspReverseXCId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLspReverseXCId.setStatus("current")


class _MplsLspPriority_Type(Integer32):
    """Custom type mplsLspPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_MplsLspPriority_Type.__name__ = "Integer32"
_MplsLspPriority_Object = MibTableColumn
mplsLspPriority = _MplsLspPriority_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 6, 1, 1, 9),
    _MplsLspPriority_Type()
)
mplsLspPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLspPriority.setStatus("current")


class _MplsLspSrcNodeId_Type(Unsigned32):
    """Custom type mplsLspSrcNodeId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MplsLspSrcNodeId_Type.__name__ = "Unsigned32"
_MplsLspSrcNodeId_Object = MibTableColumn
mplsLspSrcNodeId = _MplsLspSrcNodeId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 6, 1, 1, 10),
    _MplsLspSrcNodeId_Type()
)
mplsLspSrcNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLspSrcNodeId.setStatus("current")


class _MplsLspDestNodeId_Type(Unsigned32):
    """Custom type mplsLspDestNodeId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MplsLspDestNodeId_Type.__name__ = "Unsigned32"
_MplsLspDestNodeId_Object = MibTableColumn
mplsLspDestNodeId = _MplsLspDestNodeId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 6, 1, 1, 11),
    _MplsLspDestNodeId_Type()
)
mplsLspDestNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLspDestNodeId.setStatus("current")


class _MplsLspSrcTunnelId_Type(Unsigned32):
    """Custom type mplsLspSrcTunnelId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MplsLspSrcTunnelId_Type.__name__ = "Unsigned32"
_MplsLspSrcTunnelId_Object = MibTableColumn
mplsLspSrcTunnelId = _MplsLspSrcTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 6, 1, 1, 12),
    _MplsLspSrcTunnelId_Type()
)
mplsLspSrcTunnelId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLspSrcTunnelId.setStatus("current")


class _MplsLspDestTunnelId_Type(Unsigned32):
    """Custom type mplsLspDestTunnelId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MplsLspDestTunnelId_Type.__name__ = "Unsigned32"
_MplsLspDestTunnelId_Object = MibTableColumn
mplsLspDestTunnelId = _MplsLspDestTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 6, 1, 1, 13),
    _MplsLspDestTunnelId_Type()
)
mplsLspDestTunnelId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLspDestTunnelId.setStatus("current")


class _MplsLspLspId_Type(Unsigned32):
    """Custom type mplsLspLspId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MplsLspLspId_Type.__name__ = "Unsigned32"
_MplsLspLspId_Object = MibTableColumn
mplsLspLspId = _MplsLspLspId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 6, 1, 1, 14),
    _MplsLspLspId_Type()
)
mplsLspLspId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsLspLspId.setStatus("current")


class _MplsLspExtId_Type(DisplayString):
    """Custom type mplsLspExtId based on DisplayString"""
    defaultValue = OctetString("")


_MplsLspExtId_Type.__name__ = "DisplayString"
_MplsLspExtId_Object = MibTableColumn
mplsLspExtId = _MplsLspExtId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 6, 1, 1, 15),
    _MplsLspExtId_Type()
)
mplsLspExtId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspExtId.setStatus("current")


class _MplsLspIntTunnelId_Type(DisplayString):
    """Custom type mplsLspIntTunnelId based on DisplayString"""
    defaultValue = OctetString("")


_MplsLspIntTunnelId_Type.__name__ = "DisplayString"
_MplsLspIntTunnelId_Object = MibTableColumn
mplsLspIntTunnelId = _MplsLspIntTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 6, 1, 1, 16),
    _MplsLspIntTunnelId_Type()
)
mplsLspIntTunnelId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLspIntTunnelId.setStatus("current")
_MplsLspRowStatus_Type = RowStatus
_MplsLspRowStatus_Object = MibTableColumn
mplsLspRowStatus = _MplsLspRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 6, 1, 1, 17),
    _MplsLspRowStatus_Type()
)
mplsLspRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLspRowStatus.setStatus("current")


class _MplsLspBFDSession_Type(DisplayString):
    """Custom type mplsLspBFDSession based on DisplayString"""
    defaultValue = OctetString("")


_MplsLspBFDSession_Type.__name__ = "DisplayString"
_MplsLspBFDSession_Object = MibTableColumn
mplsLspBFDSession = _MplsLspBFDSession_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 6, 1, 1, 18),
    _MplsLspBFDSession_Type()
)
mplsLspBFDSession.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLspBFDSession.setStatus("current")
_MplsLspCreateBFD_Type = CommandString
_MplsLspCreateBFD_Object = MibTableColumn
mplsLspCreateBFD = _MplsLspCreateBFD_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 6, 1, 1, 19),
    _MplsLspCreateBFD_Type()
)
mplsLspCreateBFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspCreateBFD.setStatus("current")


class _MplsLspTrafficClass_Type(Unsigned32):
    """Custom type mplsLspTrafficClass based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MplsLspTrafficClass_Type.__name__ = "Unsigned32"
_MplsLspTrafficClass_Object = MibTableColumn
mplsLspTrafficClass = _MplsLspTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 6, 1, 1, 20),
    _MplsLspTrafficClass_Type()
)
mplsLspTrafficClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLspTrafficClass.setStatus("deprecated")


class _MplsLspGlobalId_Type(Unsigned32):
    """Custom type mplsLspGlobalId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MplsLspGlobalId_Type.__name__ = "Unsigned32"
_MplsLspGlobalId_Object = MibTableColumn
mplsLspGlobalId = _MplsLspGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 6, 1, 1, 21),
    _MplsLspGlobalId_Type()
)
mplsLspGlobalId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLspGlobalId.setStatus("current")


class _MplsLspDestGlobalId_Type(Unsigned32):
    """Custom type mplsLspDestGlobalId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MplsLspDestGlobalId_Type.__name__ = "Unsigned32"
_MplsLspDestGlobalId_Object = MibTableColumn
mplsLspDestGlobalId = _MplsLspDestGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 6, 1, 1, 22),
    _MplsLspDestGlobalId_Type()
)
mplsLspDestGlobalId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLspDestGlobalId.setStatus("current")


class _MplsLspReservedBW_Type(Unsigned32):
    """Custom type mplsLspReservedBW based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MplsLspReservedBW_Type.__name__ = "Unsigned32"
_MplsLspReservedBW_Object = MibTableColumn
mplsLspReservedBW = _MplsLspReservedBW_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 6, 1, 1, 23),
    _MplsLspReservedBW_Type()
)
mplsLspReservedBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsLspReservedBW.setStatus("current")


class _MplsLspDescr_Type(DisplayString):
    """Custom type mplsLspDescr based on DisplayString"""
    defaultValue = OctetString("")


_MplsLspDescr_Type.__name__ = "DisplayString"
_MplsLspDescr_Object = MibTableColumn
mplsLspDescr = _MplsLspDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 6, 1, 1, 24),
    _MplsLspDescr_Type()
)
mplsLspDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsLspDescr.setStatus("current")
_MplsLspCreateBFDAdvanced_Type = CommandString
_MplsLspCreateBFDAdvanced_Object = MibTableColumn
mplsLspCreateBFDAdvanced = _MplsLspCreateBFDAdvanced_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 6, 1, 1, 25),
    _MplsLspCreateBFDAdvanced_Type()
)
mplsLspCreateBFDAdvanced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspCreateBFDAdvanced.setStatus("current")
_MplsTnlXLspList_ObjectIdentity = ObjectIdentity
mplsTnlXLspList = _MplsTnlXLspList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 7)
)
_MplsTnlXLspTable_Object = MibTable
mplsTnlXLspTable = _MplsTnlXLspTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 7, 1)
)
if mibBuilder.loadTexts:
    mplsTnlXLspTable.setStatus("current")
_MplsTnlXLspEntry_Object = MibTableRow
mplsTnlXLspEntry = _MplsTnlXLspEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 7, 1, 1)
)
mplsTnlXLspEntry.setIndexNames(
    (0, "LUM-MPLS-MIB", "mplsTnlXLspIndex"),
)
if mibBuilder.loadTexts:
    mplsTnlXLspEntry.setStatus("current")


class _MplsTnlXLspIndex_Type(Unsigned32):
    """Custom type mplsTnlXLspIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsTnlXLspIndex_Type.__name__ = "Unsigned32"
_MplsTnlXLspIndex_Object = MibTableColumn
mplsTnlXLspIndex = _MplsTnlXLspIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 7, 1, 1, 1),
    _MplsTnlXLspIndex_Type()
)
mplsTnlXLspIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTnlXLspIndex.setStatus("current")
_MplsTnlXLspName_Type = MgmtNameString
_MplsTnlXLspName_Object = MibTableColumn
mplsTnlXLspName = _MplsTnlXLspName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 7, 1, 1, 2),
    _MplsTnlXLspName_Type()
)
mplsTnlXLspName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTnlXLspName.setStatus("current")


class _MplsTnlXLspInternalReference_Type(Unsigned32):
    """Custom type mplsTnlXLspInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MplsTnlXLspInternalReference_Type.__name__ = "Unsigned32"
_MplsTnlXLspInternalReference_Object = MibTableColumn
mplsTnlXLspInternalReference = _MplsTnlXLspInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 7, 1, 1, 3),
    _MplsTnlXLspInternalReference_Type()
)
mplsTnlXLspInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTnlXLspInternalReference.setStatus("current")


class _MplsTnlXLspTunnelId_Type(DisplayString):
    """Custom type mplsTnlXLspTunnelId based on DisplayString"""
    defaultValue = OctetString("")


_MplsTnlXLspTunnelId_Type.__name__ = "DisplayString"
_MplsTnlXLspTunnelId_Object = MibTableColumn
mplsTnlXLspTunnelId = _MplsTnlXLspTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 7, 1, 1, 4),
    _MplsTnlXLspTunnelId_Type()
)
mplsTnlXLspTunnelId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTnlXLspTunnelId.setStatus("current")


class _MplsTnlXLspLspId_Type(DisplayString):
    """Custom type mplsTnlXLspLspId based on DisplayString"""
    defaultValue = OctetString("")


_MplsTnlXLspLspId_Type.__name__ = "DisplayString"
_MplsTnlXLspLspId_Object = MibTableColumn
mplsTnlXLspLspId = _MplsTnlXLspLspId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 7, 1, 1, 5),
    _MplsTnlXLspLspId_Type()
)
mplsTnlXLspLspId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTnlXLspLspId.setStatus("current")
_MplsTnlXLspRowStatus_Type = RowStatus
_MplsTnlXLspRowStatus_Object = MibTableColumn
mplsTnlXLspRowStatus = _MplsTnlXLspRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 2, 7, 1, 1, 6),
    _MplsTnlXLspRowStatus_Type()
)
mplsTnlXLspRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTnlXLspRowStatus.setStatus("current")

# Managed Objects groups

mplsGeneralGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 1, 1, 1)
)
mplsGeneralGroupV1.setObjects(
      *(("LUM-MPLS-MIB", "mplsGeneralLastChangeTime"),
        ("LUM-MPLS-MIB", "mplsGeneralStateLastChangeTime"),
        ("LUM-MPLS-MIB", "mplsGeneralMplsIfTableSize"),
        ("LUM-MPLS-MIB", "mplsGeneralMplsXCTableSize"),
        ("LUM-MPLS-MIB", "mplsGeneralMplsTunnelTableSize"),
        ("LUM-MPLS-MIB", "mplsGeneralMplsLspTableSize"),
        ("LUM-MPLS-MIB", "mplsGeneralMplsTnlXLspTableSize"))
)
if mibBuilder.loadTexts:
    mplsGeneralGroupV1.setStatus("current")

mplsIfGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 1, 1, 2)
)
mplsIfGroupV1.setObjects(
      *(("LUM-MPLS-MIB", "mplsIfIndex"),
        ("LUM-MPLS-MIB", "mplsIfName"),
        ("LUM-MPLS-MIB", "mplsIfSubrack"),
        ("LUM-MPLS-MIB", "mplsIfSlot"),
        ("LUM-MPLS-MIB", "mplsIfTxPort"),
        ("LUM-MPLS-MIB", "mplsIfPortIndex"),
        ("LUM-MPLS-MIB", "mplsIfPortName"),
        ("LUM-MPLS-MIB", "mplsIfInternalReference"),
        ("LUM-MPLS-MIB", "mplsIfAdminStatus"),
        ("LUM-MPLS-MIB", "mplsIfIdentifier"),
        ("LUM-MPLS-MIB", "mplsIfNextHopMacAddress"),
        ("LUM-MPLS-MIB", "mplsIfInterfaceMacAddress"),
        ("LUM-MPLS-MIB", "mplsIfVlan"),
        ("LUM-MPLS-MIB", "mplsIfRowStatus"))
)
if mibBuilder.loadTexts:
    mplsIfGroupV1.setStatus("deprecated")

mplsXCGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 1, 1, 3)
)
mplsXCGroupV1.setObjects(
      *(("LUM-MPLS-MIB", "mplsXCIndex"),
        ("LUM-MPLS-MIB", "mplsXCName"),
        ("LUM-MPLS-MIB", "mplsXCInternalReference"),
        ("LUM-MPLS-MIB", "mplsXCIdentifier"),
        ("LUM-MPLS-MIB", "mplsXCInSegmentIfIndex"),
        ("LUM-MPLS-MIB", "mplsXCInSegmentIfName"),
        ("LUM-MPLS-MIB", "mplsXCInSegmentLabel"),
        ("LUM-MPLS-MIB", "mplsXCOutSegmentIfIndex"),
        ("LUM-MPLS-MIB", "mplsXCOutSegmentIfName"),
        ("LUM-MPLS-MIB", "mplsXCOutSegmentLabel"),
        ("LUM-MPLS-MIB", "mplsXCRowStatus"))
)
if mibBuilder.loadTexts:
    mplsXCGroupV1.setStatus("current")

mplsTunnelGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 1, 1, 4)
)
mplsTunnelGroupV1.setObjects(
      *(("LUM-MPLS-MIB", "mplsTunnelIndex"),
        ("LUM-MPLS-MIB", "mplsTunnelInternalReference"),
        ("LUM-MPLS-MIB", "mplsTunnelIdentifier"),
        ("LUM-MPLS-MIB", "mplsTunnelName"),
        ("LUM-MPLS-MIB", "mplsTunnelActiveLSP"),
        ("LUM-MPLS-MIB", "mplsTunnelActiveLspIndex"),
        ("LUM-MPLS-MIB", "mplsTunnelSrcNodeId"),
        ("LUM-MPLS-MIB", "mplsTunnelSrcTunnelId"),
        ("LUM-MPLS-MIB", "mplsTunnelDestNodeId"),
        ("LUM-MPLS-MIB", "mplsTunnelDestTunnelId"),
        ("LUM-MPLS-MIB", "mplsTunnelExtId"),
        ("LUM-MPLS-MIB", "mplsTunnelAssociateLSP"),
        ("LUM-MPLS-MIB", "mplsTunnelRowStatus"))
)
if mibBuilder.loadTexts:
    mplsTunnelGroupV1.setStatus("deprecated")

mplsNodeGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 1, 1, 5)
)
mplsNodeGroupV1.setObjects(
      *(("LUM-MPLS-MIB", "mplsNodeIndex"),
        ("LUM-MPLS-MIB", "mplsNodeName"),
        ("LUM-MPLS-MIB", "mplsNodeSubrack"),
        ("LUM-MPLS-MIB", "mplsNodeSlot"),
        ("LUM-MPLS-MIB", "mplsNodeIccIdStr"),
        ("LUM-MPLS-MIB", "mplsNodeIdNum"),
        ("LUM-MPLS-MIB", "mplsNodeCreateXC"),
        ("LUM-MPLS-MIB", "mplsNodeCreateTunnel"),
        ("LUM-MPLS-MIB", "mplsNodeCreateLsp"),
        ("LUM-MPLS-MIB", "mplsNodeCreatePw"),
        ("LUM-MPLS-MIB", "mplsNodeCreateIf"))
)
if mibBuilder.loadTexts:
    mplsNodeGroupV1.setStatus("deprecated")

mplsLspGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 1, 1, 6)
)
mplsLspGroupV1.setObjects(
      *(("LUM-MPLS-MIB", "mplsLspIndex"),
        ("LUM-MPLS-MIB", "mplsLspName"),
        ("LUM-MPLS-MIB", "mplsLspInternalReference"),
        ("LUM-MPLS-MIB", "mplsLspIdentifier"),
        ("LUM-MPLS-MIB", "mplsLspState"),
        ("LUM-MPLS-MIB", "mplsLspRole"),
        ("LUM-MPLS-MIB", "mplsLspForwardXCId"),
        ("LUM-MPLS-MIB", "mplsLspReverseXCId"),
        ("LUM-MPLS-MIB", "mplsLspPriority"),
        ("LUM-MPLS-MIB", "mplsLspSrcNodeId"),
        ("LUM-MPLS-MIB", "mplsLspDestNodeId"),
        ("LUM-MPLS-MIB", "mplsLspSrcTunnelId"),
        ("LUM-MPLS-MIB", "mplsLspDestTunnelId"),
        ("LUM-MPLS-MIB", "mplsLspLspId"),
        ("LUM-MPLS-MIB", "mplsLspExtId"),
        ("LUM-MPLS-MIB", "mplsLspIntTunnelId"),
        ("LUM-MPLS-MIB", "mplsLspRowStatus"))
)
if mibBuilder.loadTexts:
    mplsLspGroupV1.setStatus("deprecated")

mplsTnlXLspV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 1, 1, 7)
)
mplsTnlXLspV1.setObjects(
      *(("LUM-MPLS-MIB", "mplsTnlXLspIndex"),
        ("LUM-MPLS-MIB", "mplsTnlXLspName"),
        ("LUM-MPLS-MIB", "mplsTnlXLspInternalReference"),
        ("LUM-MPLS-MIB", "mplsTnlXLspTunnelId"),
        ("LUM-MPLS-MIB", "mplsTnlXLspLspId"),
        ("LUM-MPLS-MIB", "mplsTnlXLspRowStatus"))
)
if mibBuilder.loadTexts:
    mplsTnlXLspV1.setStatus("current")

mplsTunnelGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 1, 1, 8)
)
mplsTunnelGroupV2.setObjects(
      *(("LUM-MPLS-MIB", "mplsTunnelIndex"),
        ("LUM-MPLS-MIB", "mplsTunnelInternalReference"),
        ("LUM-MPLS-MIB", "mplsTunnelIdentifier"),
        ("LUM-MPLS-MIB", "mplsTunnelName"),
        ("LUM-MPLS-MIB", "mplsTunnelActiveLSP"),
        ("LUM-MPLS-MIB", "mplsTunnelActiveLspIndex"),
        ("LUM-MPLS-MIB", "mplsTunnelSrcNodeId"),
        ("LUM-MPLS-MIB", "mplsTunnelSrcTunnelId"),
        ("LUM-MPLS-MIB", "mplsTunnelDestNodeId"),
        ("LUM-MPLS-MIB", "mplsTunnelDestTunnelId"),
        ("LUM-MPLS-MIB", "mplsTunnelExtId"),
        ("LUM-MPLS-MIB", "mplsTunnelAssociateLSP"),
        ("LUM-MPLS-MIB", "mplsTunnelRowStatus"),
        ("LUM-MPLS-MIB", "mplsTunnelLinearProtection"),
        ("LUM-MPLS-MIB", "mplsTunnelProtectionState"),
        ("LUM-MPLS-MIB", "mplsTunnelAssociateLinearProt"),
        ("LUM-MPLS-MIB", "mplsTunnelGlobalId"),
        ("LUM-MPLS-MIB", "mplsTunnelDestGlobalId"),
        ("LUM-MPLS-MIB", "mplsTunnelWorkingLSP"),
        ("LUM-MPLS-MIB", "mplsTunnelProtectionLSP"))
)
if mibBuilder.loadTexts:
    mplsTunnelGroupV2.setStatus("deprecated")

mplsNodeGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 1, 1, 9)
)
mplsNodeGroupV2.setObjects(
      *(("LUM-MPLS-MIB", "mplsNodeIndex"),
        ("LUM-MPLS-MIB", "mplsNodeName"),
        ("LUM-MPLS-MIB", "mplsNodeSubrack"),
        ("LUM-MPLS-MIB", "mplsNodeSlot"),
        ("LUM-MPLS-MIB", "mplsNodeIccIdStr"),
        ("LUM-MPLS-MIB", "mplsNodeIdNum"),
        ("LUM-MPLS-MIB", "mplsNodeCreateXC"),
        ("LUM-MPLS-MIB", "mplsNodeCreateTunnel"),
        ("LUM-MPLS-MIB", "mplsNodeCreateLsp"),
        ("LUM-MPLS-MIB", "mplsNodeCreatePw"),
        ("LUM-MPLS-MIB", "mplsNodeCreateIf"),
        ("LUM-MPLS-MIB", "mplsNodeLinearProtMode"),
        ("LUM-MPLS-MIB", "mplsNodeLinearProtWtrTimer"),
        ("LUM-MPLS-MIB", "mplsNodeLPContMsgInterval"),
        ("LUM-MPLS-MIB", "mplsNodeLPRapidMsgInterval"))
)
if mibBuilder.loadTexts:
    mplsNodeGroupV2.setStatus("deprecated")

mplsLspGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 1, 1, 10)
)
mplsLspGroupV2.setObjects(
      *(("LUM-MPLS-MIB", "mplsLspIndex"),
        ("LUM-MPLS-MIB", "mplsLspName"),
        ("LUM-MPLS-MIB", "mplsLspInternalReference"),
        ("LUM-MPLS-MIB", "mplsLspIdentifier"),
        ("LUM-MPLS-MIB", "mplsLspState"),
        ("LUM-MPLS-MIB", "mplsLspRole"),
        ("LUM-MPLS-MIB", "mplsLspForwardXCId"),
        ("LUM-MPLS-MIB", "mplsLspReverseXCId"),
        ("LUM-MPLS-MIB", "mplsLspPriority"),
        ("LUM-MPLS-MIB", "mplsLspSrcNodeId"),
        ("LUM-MPLS-MIB", "mplsLspDestNodeId"),
        ("LUM-MPLS-MIB", "mplsLspSrcTunnelId"),
        ("LUM-MPLS-MIB", "mplsLspDestTunnelId"),
        ("LUM-MPLS-MIB", "mplsLspLspId"),
        ("LUM-MPLS-MIB", "mplsLspExtId"),
        ("LUM-MPLS-MIB", "mplsLspIntTunnelId"),
        ("LUM-MPLS-MIB", "mplsLspRowStatus"),
        ("LUM-MPLS-MIB", "mplsLspBFDSession"),
        ("LUM-MPLS-MIB", "mplsLspCreateBFD"),
        ("LUM-MPLS-MIB", "mplsLspTrafficClass"),
        ("LUM-MPLS-MIB", "mplsLspGlobalId"),
        ("LUM-MPLS-MIB", "mplsLspDestGlobalId"))
)
if mibBuilder.loadTexts:
    mplsLspGroupV2.setStatus("deprecated")

mplsNodeGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 1, 1, 11)
)
mplsNodeGroupV3.setObjects(
      *(("LUM-MPLS-MIB", "mplsNodeIndex"),
        ("LUM-MPLS-MIB", "mplsNodeName"),
        ("LUM-MPLS-MIB", "mplsNodeSubrack"),
        ("LUM-MPLS-MIB", "mplsNodeSlot"),
        ("LUM-MPLS-MIB", "mplsNodeIccIdStr"),
        ("LUM-MPLS-MIB", "mplsNodeIdNum"),
        ("LUM-MPLS-MIB", "mplsNodeCreateXC"),
        ("LUM-MPLS-MIB", "mplsNodeCreateTunnel"),
        ("LUM-MPLS-MIB", "mplsNodeCreateLsp"),
        ("LUM-MPLS-MIB", "mplsNodeCreatePw"),
        ("LUM-MPLS-MIB", "mplsNodeCreateIf"),
        ("LUM-MPLS-MIB", "mplsNodeLinearProtMode"),
        ("LUM-MPLS-MIB", "mplsNodeLinearProtWtrTimer"),
        ("LUM-MPLS-MIB", "mplsNodeLPContMsgInterval"),
        ("LUM-MPLS-MIB", "mplsNodeLPRapidMsgInterval"),
        ("LUM-MPLS-MIB", "mplsNodeCreateMsPw"))
)
if mibBuilder.loadTexts:
    mplsNodeGroupV3.setStatus("deprecated")

mplsTunnelGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 1, 1, 12)
)
mplsTunnelGroupV3.setObjects(
      *(("LUM-MPLS-MIB", "mplsTunnelIndex"),
        ("LUM-MPLS-MIB", "mplsTunnelInternalReference"),
        ("LUM-MPLS-MIB", "mplsTunnelIdentifier"),
        ("LUM-MPLS-MIB", "mplsTunnelName"),
        ("LUM-MPLS-MIB", "mplsTunnelActiveLSP"),
        ("LUM-MPLS-MIB", "mplsTunnelActiveLspIndex"),
        ("LUM-MPLS-MIB", "mplsTunnelSrcNodeId"),
        ("LUM-MPLS-MIB", "mplsTunnelSrcTunnelId"),
        ("LUM-MPLS-MIB", "mplsTunnelDestNodeId"),
        ("LUM-MPLS-MIB", "mplsTunnelDestTunnelId"),
        ("LUM-MPLS-MIB", "mplsTunnelExtId"),
        ("LUM-MPLS-MIB", "mplsTunnelAssociateLSP"),
        ("LUM-MPLS-MIB", "mplsTunnelRowStatus"),
        ("LUM-MPLS-MIB", "mplsTunnelLinearProtection"),
        ("LUM-MPLS-MIB", "mplsTunnelProtectionState"),
        ("LUM-MPLS-MIB", "mplsTunnelAssociateLinearProt"),
        ("LUM-MPLS-MIB", "mplsTunnelGlobalId"),
        ("LUM-MPLS-MIB", "mplsTunnelDestGlobalId"),
        ("LUM-MPLS-MIB", "mplsTunnelWorkingLSP"),
        ("LUM-MPLS-MIB", "mplsTunnelProtectionLSP"),
        ("LUM-MPLS-MIB", "mplsTunnelReservedBW"),
        ("LUM-MPLS-MIB", "mplsTunnelBookedBW"))
)
if mibBuilder.loadTexts:
    mplsTunnelGroupV3.setStatus("deprecated")

mplsLspGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 1, 1, 13)
)
mplsLspGroupV3.setObjects(
      *(("LUM-MPLS-MIB", "mplsLspIndex"),
        ("LUM-MPLS-MIB", "mplsLspName"),
        ("LUM-MPLS-MIB", "mplsLspInternalReference"),
        ("LUM-MPLS-MIB", "mplsLspIdentifier"),
        ("LUM-MPLS-MIB", "mplsLspState"),
        ("LUM-MPLS-MIB", "mplsLspRole"),
        ("LUM-MPLS-MIB", "mplsLspForwardXCId"),
        ("LUM-MPLS-MIB", "mplsLspReverseXCId"),
        ("LUM-MPLS-MIB", "mplsLspPriority"),
        ("LUM-MPLS-MIB", "mplsLspSrcNodeId"),
        ("LUM-MPLS-MIB", "mplsLspDestNodeId"),
        ("LUM-MPLS-MIB", "mplsLspSrcTunnelId"),
        ("LUM-MPLS-MIB", "mplsLspDestTunnelId"),
        ("LUM-MPLS-MIB", "mplsLspLspId"),
        ("LUM-MPLS-MIB", "mplsLspExtId"),
        ("LUM-MPLS-MIB", "mplsLspIntTunnelId"),
        ("LUM-MPLS-MIB", "mplsLspRowStatus"),
        ("LUM-MPLS-MIB", "mplsLspBFDSession"),
        ("LUM-MPLS-MIB", "mplsLspCreateBFD"),
        ("LUM-MPLS-MIB", "mplsLspTrafficClass"),
        ("LUM-MPLS-MIB", "mplsLspGlobalId"),
        ("LUM-MPLS-MIB", "mplsLspDestGlobalId"),
        ("LUM-MPLS-MIB", "mplsLspReservedBW"))
)
if mibBuilder.loadTexts:
    mplsLspGroupV3.setStatus("deprecated")

mplsNodeGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 1, 1, 14)
)
mplsNodeGroupV4.setObjects(
      *(("LUM-MPLS-MIB", "mplsNodeIndex"),
        ("LUM-MPLS-MIB", "mplsNodeName"),
        ("LUM-MPLS-MIB", "mplsNodeSubrack"),
        ("LUM-MPLS-MIB", "mplsNodeSlot"),
        ("LUM-MPLS-MIB", "mplsNodeIccIdStr"),
        ("LUM-MPLS-MIB", "mplsNodeIdNum"),
        ("LUM-MPLS-MIB", "mplsNodeCreateXC"),
        ("LUM-MPLS-MIB", "mplsNodeCreateTunnel"),
        ("LUM-MPLS-MIB", "mplsNodeCreateLsp"),
        ("LUM-MPLS-MIB", "mplsNodeCreatePw"),
        ("LUM-MPLS-MIB", "mplsNodeCreateIf"),
        ("LUM-MPLS-MIB", "mplsNodeLinearProtMode"),
        ("LUM-MPLS-MIB", "mplsNodeLinearProtWtrTimer"),
        ("LUM-MPLS-MIB", "mplsNodeLPContMsgInterval"),
        ("LUM-MPLS-MIB", "mplsNodeLPRapidMsgInterval"),
        ("LUM-MPLS-MIB", "mplsNodeCreateMsPw"),
        ("LUM-MPLS-MIB", "mplsNodeCreateLsp2"))
)
if mibBuilder.loadTexts:
    mplsNodeGroupV4.setStatus("deprecated")

mplsLspGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 1, 1, 15)
)
mplsLspGroupV4.setObjects(
      *(("LUM-MPLS-MIB", "mplsLspIndex"),
        ("LUM-MPLS-MIB", "mplsLspName"),
        ("LUM-MPLS-MIB", "mplsLspInternalReference"),
        ("LUM-MPLS-MIB", "mplsLspIdentifier"),
        ("LUM-MPLS-MIB", "mplsLspState"),
        ("LUM-MPLS-MIB", "mplsLspRole"),
        ("LUM-MPLS-MIB", "mplsLspForwardXCId"),
        ("LUM-MPLS-MIB", "mplsLspReverseXCId"),
        ("LUM-MPLS-MIB", "mplsLspPriority"),
        ("LUM-MPLS-MIB", "mplsLspSrcNodeId"),
        ("LUM-MPLS-MIB", "mplsLspDestNodeId"),
        ("LUM-MPLS-MIB", "mplsLspSrcTunnelId"),
        ("LUM-MPLS-MIB", "mplsLspDestTunnelId"),
        ("LUM-MPLS-MIB", "mplsLspLspId"),
        ("LUM-MPLS-MIB", "mplsLspExtId"),
        ("LUM-MPLS-MIB", "mplsLspIntTunnelId"),
        ("LUM-MPLS-MIB", "mplsLspRowStatus"),
        ("LUM-MPLS-MIB", "mplsLspBFDSession"),
        ("LUM-MPLS-MIB", "mplsLspCreateBFD"),
        ("LUM-MPLS-MIB", "mplsLspTrafficClass"),
        ("LUM-MPLS-MIB", "mplsLspGlobalId"),
        ("LUM-MPLS-MIB", "mplsLspDestGlobalId"),
        ("LUM-MPLS-MIB", "mplsLspReservedBW"),
        ("LUM-MPLS-MIB", "mplsLspDescr"))
)
if mibBuilder.loadTexts:
    mplsLspGroupV4.setStatus("deprecated")

mplsTunnelGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 1, 1, 16)
)
mplsTunnelGroupV4.setObjects(
      *(("LUM-MPLS-MIB", "mplsTunnelIndex"),
        ("LUM-MPLS-MIB", "mplsTunnelInternalReference"),
        ("LUM-MPLS-MIB", "mplsTunnelIdentifier"),
        ("LUM-MPLS-MIB", "mplsTunnelName"),
        ("LUM-MPLS-MIB", "mplsTunnelActiveLSP"),
        ("LUM-MPLS-MIB", "mplsTunnelActiveLspIndex"),
        ("LUM-MPLS-MIB", "mplsTunnelSrcNodeId"),
        ("LUM-MPLS-MIB", "mplsTunnelSrcTunnelId"),
        ("LUM-MPLS-MIB", "mplsTunnelDestNodeId"),
        ("LUM-MPLS-MIB", "mplsTunnelDestTunnelId"),
        ("LUM-MPLS-MIB", "mplsTunnelExtId"),
        ("LUM-MPLS-MIB", "mplsTunnelAssociateLSP"),
        ("LUM-MPLS-MIB", "mplsTunnelRowStatus"),
        ("LUM-MPLS-MIB", "mplsTunnelLinearProtection"),
        ("LUM-MPLS-MIB", "mplsTunnelProtectionState"),
        ("LUM-MPLS-MIB", "mplsTunnelAssociateLinearProt"),
        ("LUM-MPLS-MIB", "mplsTunnelGlobalId"),
        ("LUM-MPLS-MIB", "mplsTunnelDestGlobalId"),
        ("LUM-MPLS-MIB", "mplsTunnelWorkingLSP"),
        ("LUM-MPLS-MIB", "mplsTunnelProtectionLSP"),
        ("LUM-MPLS-MIB", "mplsTunnelReservedBW"),
        ("LUM-MPLS-MIB", "mplsTunnelBookedBW"),
        ("LUM-MPLS-MIB", "mplsTunnelDescr"))
)
if mibBuilder.loadTexts:
    mplsTunnelGroupV4.setStatus("current")

mplsIfGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 1, 1, 17)
)
mplsIfGroupV2.setObjects(
      *(("LUM-MPLS-MIB", "mplsIfIndex"),
        ("LUM-MPLS-MIB", "mplsIfName"),
        ("LUM-MPLS-MIB", "mplsIfSubrack"),
        ("LUM-MPLS-MIB", "mplsIfSlot"),
        ("LUM-MPLS-MIB", "mplsIfTxPort"),
        ("LUM-MPLS-MIB", "mplsIfPortIndex"),
        ("LUM-MPLS-MIB", "mplsIfPortName"),
        ("LUM-MPLS-MIB", "mplsIfInternalReference"),
        ("LUM-MPLS-MIB", "mplsIfAdminStatus"),
        ("LUM-MPLS-MIB", "mplsIfIdentifier"),
        ("LUM-MPLS-MIB", "mplsIfNextHopMacAddress"),
        ("LUM-MPLS-MIB", "mplsIfInterfaceMacAddress"),
        ("LUM-MPLS-MIB", "mplsIfVlan"),
        ("LUM-MPLS-MIB", "mplsIfRowStatus"),
        ("LUM-MPLS-MIB", "mplsIfIfNo"),
        ("LUM-MPLS-MIB", "mplsIfResourceType"),
        ("LUM-MPLS-MIB", "mplsIfLagId"))
)
if mibBuilder.loadTexts:
    mplsIfGroupV2.setStatus("current")

mplsNodeGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 1, 1, 18)
)
mplsNodeGroupV5.setObjects(
      *(("LUM-MPLS-MIB", "mplsNodeIndex"),
        ("LUM-MPLS-MIB", "mplsNodeName"),
        ("LUM-MPLS-MIB", "mplsNodeSubrack"),
        ("LUM-MPLS-MIB", "mplsNodeSlot"),
        ("LUM-MPLS-MIB", "mplsNodeIccIdStr"),
        ("LUM-MPLS-MIB", "mplsNodeIdNum"),
        ("LUM-MPLS-MIB", "mplsNodeCreateXC"),
        ("LUM-MPLS-MIB", "mplsNodeCreateTunnel"),
        ("LUM-MPLS-MIB", "mplsNodeCreateLsp"),
        ("LUM-MPLS-MIB", "mplsNodeCreatePw"),
        ("LUM-MPLS-MIB", "mplsNodeCreateIf"),
        ("LUM-MPLS-MIB", "mplsNodeLinearProtMode"),
        ("LUM-MPLS-MIB", "mplsNodeLinearProtWtrTimer"),
        ("LUM-MPLS-MIB", "mplsNodeLPContMsgInterval"),
        ("LUM-MPLS-MIB", "mplsNodeLPRapidMsgInterval"),
        ("LUM-MPLS-MIB", "mplsNodeCreateMsPw"),
        ("LUM-MPLS-MIB", "mplsNodeCreateLsp2"),
        ("LUM-MPLS-MIB", "mplsNodeCreateTunnelAdvanced"),
        ("LUM-MPLS-MIB", "mplsNodeCreateLspAdvanced"),
        ("LUM-MPLS-MIB", "mplsNodeCreatePwGeneric"),
        ("LUM-MPLS-MIB", "mplsNodeCreatePwMpls"),
        ("LUM-MPLS-MIB", "mplsNodeCreatePwEnet"),
        ("LUM-MPLS-MIB", "mplsNodeCreateBfdTemplate"),
        ("LUM-MPLS-MIB", "mplsNodeCreateXCAdvanced"))
)
if mibBuilder.loadTexts:
    mplsNodeGroupV5.setStatus("current")

mplsLspGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 1, 1, 19)
)
mplsLspGroupV5.setObjects(
      *(("LUM-MPLS-MIB", "mplsLspIndex"),
        ("LUM-MPLS-MIB", "mplsLspName"),
        ("LUM-MPLS-MIB", "mplsLspInternalReference"),
        ("LUM-MPLS-MIB", "mplsLspIdentifier"),
        ("LUM-MPLS-MIB", "mplsLspState"),
        ("LUM-MPLS-MIB", "mplsLspRole"),
        ("LUM-MPLS-MIB", "mplsLspForwardXCId"),
        ("LUM-MPLS-MIB", "mplsLspReverseXCId"),
        ("LUM-MPLS-MIB", "mplsLspPriority"),
        ("LUM-MPLS-MIB", "mplsLspSrcNodeId"),
        ("LUM-MPLS-MIB", "mplsLspDestNodeId"),
        ("LUM-MPLS-MIB", "mplsLspSrcTunnelId"),
        ("LUM-MPLS-MIB", "mplsLspDestTunnelId"),
        ("LUM-MPLS-MIB", "mplsLspLspId"),
        ("LUM-MPLS-MIB", "mplsLspExtId"),
        ("LUM-MPLS-MIB", "mplsLspIntTunnelId"),
        ("LUM-MPLS-MIB", "mplsLspRowStatus"),
        ("LUM-MPLS-MIB", "mplsLspBFDSession"),
        ("LUM-MPLS-MIB", "mplsLspCreateBFD"),
        ("LUM-MPLS-MIB", "mplsLspTrafficClass"),
        ("LUM-MPLS-MIB", "mplsLspGlobalId"),
        ("LUM-MPLS-MIB", "mplsLspDestGlobalId"),
        ("LUM-MPLS-MIB", "mplsLspReservedBW"),
        ("LUM-MPLS-MIB", "mplsLspDescr"),
        ("LUM-MPLS-MIB", "mplsLspCreateBFDAdvanced"))
)
if mibBuilder.loadTexts:
    mplsLspGroupV5.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumMplsBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 1, 2, 1)
)
lumMplsBasicComplV1.setObjects(
      *(("LUM-MPLS-MIB", "mplsGeneralGroupV1"),
        ("LUM-MPLS-MIB", "mplsIfGroupV1"),
        ("LUM-MPLS-MIB", "mplsXCGroupV1"),
        ("LUM-MPLS-MIB", "mplsTunnelGroupV2"),
        ("LUM-MPLS-MIB", "mplsNodeGroupV1"),
        ("LUM-MPLS-MIB", "mplsLspGroupV1"),
        ("LUM-MPLS-MIB", "mplsTnlXLspV1"))
)
if mibBuilder.loadTexts:
    lumMplsBasicComplV1.setStatus(
        "deprecated"
    )

lumMplsBasicComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 1, 2, 2)
)
lumMplsBasicComplV2.setObjects(
      *(("LUM-MPLS-MIB", "mplsGeneralGroupV1"),
        ("LUM-MPLS-MIB", "mplsIfGroupV1"),
        ("LUM-MPLS-MIB", "mplsXCGroupV1"),
        ("LUM-MPLS-MIB", "mplsTunnelGroupV2"),
        ("LUM-MPLS-MIB", "mplsNodeGroupV2"),
        ("LUM-MPLS-MIB", "mplsLspGroupV2"),
        ("LUM-MPLS-MIB", "mplsTnlXLspV1"))
)
if mibBuilder.loadTexts:
    lumMplsBasicComplV2.setStatus(
        "deprecated"
    )

lumMplsBasicComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 1, 2, 3)
)
lumMplsBasicComplV3.setObjects(
      *(("LUM-MPLS-MIB", "mplsGeneralGroupV1"),
        ("LUM-MPLS-MIB", "mplsIfGroupV1"),
        ("LUM-MPLS-MIB", "mplsXCGroupV1"),
        ("LUM-MPLS-MIB", "mplsTunnelGroupV3"),
        ("LUM-MPLS-MIB", "mplsNodeGroupV3"),
        ("LUM-MPLS-MIB", "mplsLspGroupV3"),
        ("LUM-MPLS-MIB", "mplsTnlXLspV1"))
)
if mibBuilder.loadTexts:
    lumMplsBasicComplV3.setStatus(
        "deprecated"
    )

lumMplsBasicComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 1, 2, 4)
)
lumMplsBasicComplV4.setObjects(
      *(("LUM-MPLS-MIB", "mplsGeneralGroupV1"),
        ("LUM-MPLS-MIB", "mplsIfGroupV1"),
        ("LUM-MPLS-MIB", "mplsXCGroupV1"),
        ("LUM-MPLS-MIB", "mplsTunnelGroupV3"),
        ("LUM-MPLS-MIB", "mplsNodeGroupV3"),
        ("LUM-MPLS-MIB", "mplsLspGroupV3"),
        ("LUM-MPLS-MIB", "mplsTnlXLspV1"))
)
if mibBuilder.loadTexts:
    lumMplsBasicComplV4.setStatus(
        "deprecated"
    )

lumMplsBasicComplV5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 1, 2, 5)
)
lumMplsBasicComplV5.setObjects(
      *(("LUM-MPLS-MIB", "mplsGeneralGroupV1"),
        ("LUM-MPLS-MIB", "mplsIfGroupV1"),
        ("LUM-MPLS-MIB", "mplsXCGroupV1"),
        ("LUM-MPLS-MIB", "mplsTunnelGroupV3"),
        ("LUM-MPLS-MIB", "mplsNodeGroupV4"),
        ("LUM-MPLS-MIB", "mplsLspGroupV3"),
        ("LUM-MPLS-MIB", "mplsTnlXLspV1"))
)
if mibBuilder.loadTexts:
    lumMplsBasicComplV5.setStatus(
        "deprecated"
    )

lumMplsBasicComplV6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 1, 2, 6)
)
lumMplsBasicComplV6.setObjects(
      *(("LUM-MPLS-MIB", "mplsGeneralGroupV1"),
        ("LUM-MPLS-MIB", "mplsIfGroupV1"),
        ("LUM-MPLS-MIB", "mplsXCGroupV1"),
        ("LUM-MPLS-MIB", "mplsTunnelGroupV4"),
        ("LUM-MPLS-MIB", "mplsNodeGroupV4"),
        ("LUM-MPLS-MIB", "mplsLspGroupV4"),
        ("LUM-MPLS-MIB", "mplsTnlXLspV1"))
)
if mibBuilder.loadTexts:
    lumMplsBasicComplV6.setStatus(
        "deprecated"
    )

lumMplsBasicComplV7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 1, 2, 7)
)
lumMplsBasicComplV7.setObjects(
      *(("LUM-MPLS-MIB", "mplsGeneralGroupV1"),
        ("LUM-MPLS-MIB", "mplsIfGroupV2"),
        ("LUM-MPLS-MIB", "mplsXCGroupV1"),
        ("LUM-MPLS-MIB", "mplsTunnelGroupV4"),
        ("LUM-MPLS-MIB", "mplsNodeGroupV4"),
        ("LUM-MPLS-MIB", "mplsLspGroupV4"),
        ("LUM-MPLS-MIB", "mplsTnlXLspV1"))
)
if mibBuilder.loadTexts:
    lumMplsBasicComplV7.setStatus(
        "deprecated"
    )

lumMplsBasicComplV8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40, 1, 2, 8)
)
lumMplsBasicComplV8.setObjects(
      *(("LUM-MPLS-MIB", "mplsGeneralGroupV1"),
        ("LUM-MPLS-MIB", "mplsIfGroupV2"),
        ("LUM-MPLS-MIB", "mplsXCGroupV1"),
        ("LUM-MPLS-MIB", "mplsTunnelGroupV4"),
        ("LUM-MPLS-MIB", "mplsNodeGroupV5"),
        ("LUM-MPLS-MIB", "mplsLspGroupV5"),
        ("LUM-MPLS-MIB", "mplsTnlXLspV1"))
)
if mibBuilder.loadTexts:
    lumMplsBasicComplV8.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-MPLS-MIB",
    **{"MplsIdentifier": MplsIdentifier,
       "lumMplsMIBModule": lumMplsMIBModule,
       "lumMplsConfs": lumMplsConfs,
       "lumMplsGroups": lumMplsGroups,
       "mplsGeneralGroupV1": mplsGeneralGroupV1,
       "mplsIfGroupV1": mplsIfGroupV1,
       "mplsXCGroupV1": mplsXCGroupV1,
       "mplsTunnelGroupV1": mplsTunnelGroupV1,
       "mplsNodeGroupV1": mplsNodeGroupV1,
       "mplsLspGroupV1": mplsLspGroupV1,
       "mplsTnlXLspV1": mplsTnlXLspV1,
       "mplsTunnelGroupV2": mplsTunnelGroupV2,
       "mplsNodeGroupV2": mplsNodeGroupV2,
       "mplsLspGroupV2": mplsLspGroupV2,
       "mplsNodeGroupV3": mplsNodeGroupV3,
       "mplsTunnelGroupV3": mplsTunnelGroupV3,
       "mplsLspGroupV3": mplsLspGroupV3,
       "mplsNodeGroupV4": mplsNodeGroupV4,
       "mplsLspGroupV4": mplsLspGroupV4,
       "mplsTunnelGroupV4": mplsTunnelGroupV4,
       "mplsIfGroupV2": mplsIfGroupV2,
       "mplsNodeGroupV5": mplsNodeGroupV5,
       "mplsLspGroupV5": mplsLspGroupV5,
       "lumMplsCompl": lumMplsCompl,
       "lumMplsBasicComplV1": lumMplsBasicComplV1,
       "lumMplsBasicComplV2": lumMplsBasicComplV2,
       "lumMplsBasicComplV3": lumMplsBasicComplV3,
       "lumMplsBasicComplV4": lumMplsBasicComplV4,
       "lumMplsBasicComplV5": lumMplsBasicComplV5,
       "lumMplsBasicComplV6": lumMplsBasicComplV6,
       "lumMplsBasicComplV7": lumMplsBasicComplV7,
       "lumMplsBasicComplV8": lumMplsBasicComplV8,
       "lumMplsMIBObjects": lumMplsMIBObjects,
       "mplsGeneral": mplsGeneral,
       "mplsGeneralLastChangeTime": mplsGeneralLastChangeTime,
       "mplsGeneralStateLastChangeTime": mplsGeneralStateLastChangeTime,
       "mplsGeneralMplsIfTableSize": mplsGeneralMplsIfTableSize,
       "mplsGeneralMplsXCTableSize": mplsGeneralMplsXCTableSize,
       "mplsGeneralMplsTunnelTableSize": mplsGeneralMplsTunnelTableSize,
       "mplsGeneralMplsNodeTableSize": mplsGeneralMplsNodeTableSize,
       "mplsGeneralMplsLspTableSize": mplsGeneralMplsLspTableSize,
       "mplsGeneralMplsTnlXLspTableSize": mplsGeneralMplsTnlXLspTableSize,
       "mplsIfList": mplsIfList,
       "mplsIfTable": mplsIfTable,
       "mplsIfEntry": mplsIfEntry,
       "mplsIfIndex": mplsIfIndex,
       "mplsIfName": mplsIfName,
       "mplsIfSubrack": mplsIfSubrack,
       "mplsIfSlot": mplsIfSlot,
       "mplsIfTxPort": mplsIfTxPort,
       "mplsIfPortIndex": mplsIfPortIndex,
       "mplsIfPortName": mplsIfPortName,
       "mplsIfInternalReference": mplsIfInternalReference,
       "mplsIfAdminStatus": mplsIfAdminStatus,
       "mplsIfIdentifier": mplsIfIdentifier,
       "mplsIfNextHopMacAddress": mplsIfNextHopMacAddress,
       "mplsIfInterfaceMacAddress": mplsIfInterfaceMacAddress,
       "mplsIfVlan": mplsIfVlan,
       "mplsIfRowStatus": mplsIfRowStatus,
       "mplsIfIfNo": mplsIfIfNo,
       "mplsIfResourceType": mplsIfResourceType,
       "mplsIfLagId": mplsIfLagId,
       "mplsXCList": mplsXCList,
       "mplsXCTable": mplsXCTable,
       "mplsXCEntry": mplsXCEntry,
       "mplsXCIndex": mplsXCIndex,
       "mplsXCName": mplsXCName,
       "mplsXCInternalReference": mplsXCInternalReference,
       "mplsXCIdentifier": mplsXCIdentifier,
       "mplsXCInSegmentIfIndex": mplsXCInSegmentIfIndex,
       "mplsXCInSegmentIfName": mplsXCInSegmentIfName,
       "mplsXCInSegmentLabel": mplsXCInSegmentLabel,
       "mplsXCOutSegmentIfIndex": mplsXCOutSegmentIfIndex,
       "mplsXCOutSegmentIfName": mplsXCOutSegmentIfName,
       "mplsXCOutSegmentLabel": mplsXCOutSegmentLabel,
       "mplsXCRowStatus": mplsXCRowStatus,
       "mplsTunnelList": mplsTunnelList,
       "mplsTunnelTable": mplsTunnelTable,
       "mplsTunnelEntry": mplsTunnelEntry,
       "mplsTunnelIndex": mplsTunnelIndex,
       "mplsTunnelInternalReference": mplsTunnelInternalReference,
       "mplsTunnelIdentifier": mplsTunnelIdentifier,
       "mplsTunnelName": mplsTunnelName,
       "mplsTunnelActiveLSP": mplsTunnelActiveLSP,
       "mplsTunnelActiveLspIndex": mplsTunnelActiveLspIndex,
       "mplsTunnelState": mplsTunnelState,
       "mplsTunnelSrcNodeId": mplsTunnelSrcNodeId,
       "mplsTunnelSrcTunnelId": mplsTunnelSrcTunnelId,
       "mplsTunnelDestNodeId": mplsTunnelDestNodeId,
       "mplsTunnelDestTunnelId": mplsTunnelDestTunnelId,
       "mplsTunnelExtId": mplsTunnelExtId,
       "mplsTunnelAssociateLSP": mplsTunnelAssociateLSP,
       "mplsTunnelRowStatus": mplsTunnelRowStatus,
       "mplsTunnelLinearProtection": mplsTunnelLinearProtection,
       "mplsTunnelProtectionState": mplsTunnelProtectionState,
       "mplsTunnelAssociateLinearProt": mplsTunnelAssociateLinearProt,
       "mplsTunnelGlobalId": mplsTunnelGlobalId,
       "mplsTunnelDestGlobalId": mplsTunnelDestGlobalId,
       "mplsTunnelWorkingLSP": mplsTunnelWorkingLSP,
       "mplsTunnelProtectionLSP": mplsTunnelProtectionLSP,
       "mplsTunnelReservedBW": mplsTunnelReservedBW,
       "mplsTunnelBookedBW": mplsTunnelBookedBW,
       "mplsTunnelDescr": mplsTunnelDescr,
       "mplsNodeList": mplsNodeList,
       "mplsNodeTable": mplsNodeTable,
       "mplsNodeEntry": mplsNodeEntry,
       "mplsNodeIndex": mplsNodeIndex,
       "mplsNodeName": mplsNodeName,
       "mplsNodeSubrack": mplsNodeSubrack,
       "mplsNodeSlot": mplsNodeSlot,
       "mplsNodeIccIdStr": mplsNodeIccIdStr,
       "mplsNodeIdNum": mplsNodeIdNum,
       "mplsNodeCreateXC": mplsNodeCreateXC,
       "mplsNodeCreateTunnel": mplsNodeCreateTunnel,
       "mplsNodeCreateLsp": mplsNodeCreateLsp,
       "mplsNodeCreatePw": mplsNodeCreatePw,
       "mplsNodeCreateIf": mplsNodeCreateIf,
       "mplsNodeLinearProtMode": mplsNodeLinearProtMode,
       "mplsNodeLinearProtWtrTimer": mplsNodeLinearProtWtrTimer,
       "mplsNodeLPContMsgInterval": mplsNodeLPContMsgInterval,
       "mplsNodeLPRapidMsgInterval": mplsNodeLPRapidMsgInterval,
       "mplsNodeGlobalId": mplsNodeGlobalId,
       "mplsNodeCreateMsPw": mplsNodeCreateMsPw,
       "mplsNodeCreateLsp2": mplsNodeCreateLsp2,
       "mplsNodeCreateTunnelAdvanced": mplsNodeCreateTunnelAdvanced,
       "mplsNodeCreateLspAdvanced": mplsNodeCreateLspAdvanced,
       "mplsNodeCreatePwGeneric": mplsNodeCreatePwGeneric,
       "mplsNodeCreatePwMpls": mplsNodeCreatePwMpls,
       "mplsNodeCreatePwEnet": mplsNodeCreatePwEnet,
       "mplsNodeCreateBfdTemplate": mplsNodeCreateBfdTemplate,
       "mplsNodeCreateXCAdvanced": mplsNodeCreateXCAdvanced,
       "mplsLspList": mplsLspList,
       "mplsLspTable": mplsLspTable,
       "mplsLspEntry": mplsLspEntry,
       "mplsLspIndex": mplsLspIndex,
       "mplsLspName": mplsLspName,
       "mplsLspInternalReference": mplsLspInternalReference,
       "mplsLspIdentifier": mplsLspIdentifier,
       "mplsLspState": mplsLspState,
       "mplsLspRole": mplsLspRole,
       "mplsLspForwardXCId": mplsLspForwardXCId,
       "mplsLspReverseXCId": mplsLspReverseXCId,
       "mplsLspPriority": mplsLspPriority,
       "mplsLspSrcNodeId": mplsLspSrcNodeId,
       "mplsLspDestNodeId": mplsLspDestNodeId,
       "mplsLspSrcTunnelId": mplsLspSrcTunnelId,
       "mplsLspDestTunnelId": mplsLspDestTunnelId,
       "mplsLspLspId": mplsLspLspId,
       "mplsLspExtId": mplsLspExtId,
       "mplsLspIntTunnelId": mplsLspIntTunnelId,
       "mplsLspRowStatus": mplsLspRowStatus,
       "mplsLspBFDSession": mplsLspBFDSession,
       "mplsLspCreateBFD": mplsLspCreateBFD,
       "mplsLspTrafficClass": mplsLspTrafficClass,
       "mplsLspGlobalId": mplsLspGlobalId,
       "mplsLspDestGlobalId": mplsLspDestGlobalId,
       "mplsLspReservedBW": mplsLspReservedBW,
       "mplsLspDescr": mplsLspDescr,
       "mplsLspCreateBFDAdvanced": mplsLspCreateBFDAdvanced,
       "mplsTnlXLspList": mplsTnlXLspList,
       "mplsTnlXLspTable": mplsTnlXLspTable,
       "mplsTnlXLspEntry": mplsTnlXLspEntry,
       "mplsTnlXLspIndex": mplsTnlXLspIndex,
       "mplsTnlXLspName": mplsTnlXLspName,
       "mplsTnlXLspInternalReference": mplsTnlXLspInternalReference,
       "mplsTnlXLspTunnelId": mplsTnlXLspTunnelId,
       "mplsTnlXLspLspId": mplsTnlXLspLspId,
       "mplsTnlXLspRowStatus": mplsTnlXLspRowStatus}
)
