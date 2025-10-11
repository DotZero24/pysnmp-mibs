# SNMP MIB module (LUM-ICCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-ICCP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:57 2025
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

(lumIccpMIB,
 lumModules) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumIccpMIB",
    "lumModules")

(CommandString,
 FaultStatus,
 MgmtNameString) = mibBuilder.importSymbols(
    "LUM-TC",
    "CommandString",
    "FaultStatus",
    "MgmtNameString")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

lumIccpMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 61)
)
if mibBuilder.loadTexts:
    lumIccpMIBModule.setRevisions(
        ("2017-09-01 00:00",
         "2017-06-15 00:00",
         "2015-01-14 00:00",
         "2014-11-05 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class IccpLabel(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )



class IccpIdentifier(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_LumIccpConfs_ObjectIdentity = ObjectIdentity
lumIccpConfs = _LumIccpConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 1)
)
_LumIccpGroups_ObjectIdentity = ObjectIdentity
lumIccpGroups = _LumIccpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 1, 1)
)
_LumIccpCompl_ObjectIdentity = ObjectIdentity
lumIccpCompl = _LumIccpCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 1, 2)
)
_LumIccpMIBObjects_ObjectIdentity = ObjectIdentity
lumIccpMIBObjects = _LumIccpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 2)
)
_IccpGeneral_ObjectIdentity = ObjectIdentity
iccpGeneral = _IccpGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 2, 1)
)
_IccpGeneralLastChangeTime_Type = DateAndTime
_IccpGeneralLastChangeTime_Object = MibScalar
iccpGeneralLastChangeTime = _IccpGeneralLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 2, 1, 1),
    _IccpGeneralLastChangeTime_Type()
)
iccpGeneralLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iccpGeneralLastChangeTime.setStatus("current")
_IccpGeneralStateLastChangeTime_Type = DateAndTime
_IccpGeneralStateLastChangeTime_Object = MibScalar
iccpGeneralStateLastChangeTime = _IccpGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 2, 1, 2),
    _IccpGeneralStateLastChangeTime_Type()
)
iccpGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iccpGeneralStateLastChangeTime.setStatus("current")
_IccpGeneralIccpNodeTableSize_Type = Unsigned32
_IccpGeneralIccpNodeTableSize_Object = MibScalar
iccpGeneralIccpNodeTableSize = _IccpGeneralIccpNodeTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 2, 1, 3),
    _IccpGeneralIccpNodeTableSize_Type()
)
iccpGeneralIccpNodeTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iccpGeneralIccpNodeTableSize.setStatus("current")
_IccpGeneralIccpRgTableSize_Type = Unsigned32
_IccpGeneralIccpRgTableSize_Object = MibScalar
iccpGeneralIccpRgTableSize = _IccpGeneralIccpRgTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 2, 1, 4),
    _IccpGeneralIccpRgTableSize_Type()
)
iccpGeneralIccpRgTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iccpGeneralIccpRgTableSize.setStatus("current")
_IccpNodeList_ObjectIdentity = ObjectIdentity
iccpNodeList = _IccpNodeList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 2, 2)
)
_IccpNodeTable_Object = MibTable
iccpNodeTable = _IccpNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 2, 2, 1)
)
if mibBuilder.loadTexts:
    iccpNodeTable.setStatus("current")
_IccpNodeEntry_Object = MibTableRow
iccpNodeEntry = _IccpNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 2, 2, 1, 1)
)
iccpNodeEntry.setIndexNames(
    (0, "LUM-ICCP-MIB", "iccpNodeIndex"),
)
if mibBuilder.loadTexts:
    iccpNodeEntry.setStatus("current")


class _IccpNodeIndex_Type(Unsigned32):
    """Custom type iccpNodeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IccpNodeIndex_Type.__name__ = "Unsigned32"
_IccpNodeIndex_Object = MibTableColumn
iccpNodeIndex = _IccpNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 2, 2, 1, 1, 1),
    _IccpNodeIndex_Type()
)
iccpNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iccpNodeIndex.setStatus("current")
_IccpNodeName_Type = MgmtNameString
_IccpNodeName_Object = MibTableColumn
iccpNodeName = _IccpNodeName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 2, 2, 1, 1, 2),
    _IccpNodeName_Type()
)
iccpNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iccpNodeName.setStatus("current")


class _IccpNodeSystemMacAddress_Type(DisplayString):
    """Custom type iccpNodeSystemMacAddress based on DisplayString"""
    defaultValue = OctetString("")


_IccpNodeSystemMacAddress_Type.__name__ = "DisplayString"
_IccpNodeSystemMacAddress_Object = MibTableColumn
iccpNodeSystemMacAddress = _IccpNodeSystemMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 2, 2, 1, 1, 3),
    _IccpNodeSystemMacAddress_Type()
)
iccpNodeSystemMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iccpNodeSystemMacAddress.setStatus("current")
_IccpNodeCreateIccpRg_Type = CommandString
_IccpNodeCreateIccpRg_Object = MibTableColumn
iccpNodeCreateIccpRg = _IccpNodeCreateIccpRg_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 2, 2, 1, 1, 4),
    _IccpNodeCreateIccpRg_Type()
)
iccpNodeCreateIccpRg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iccpNodeCreateIccpRg.setStatus("current")


class _IccpNodeInternalReference_Type(Unsigned32):
    """Custom type iccpNodeInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IccpNodeInternalReference_Type.__name__ = "Unsigned32"
_IccpNodeInternalReference_Object = MibTableColumn
iccpNodeInternalReference = _IccpNodeInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 2, 2, 1, 1, 5),
    _IccpNodeInternalReference_Type()
)
iccpNodeInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iccpNodeInternalReference.setStatus("current")
_IccpRgList_ObjectIdentity = ObjectIdentity
iccpRgList = _IccpRgList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 2, 3)
)
_IccpRgTable_Object = MibTable
iccpRgTable = _IccpRgTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 2, 3, 1)
)
if mibBuilder.loadTexts:
    iccpRgTable.setStatus("current")
_IccpRgEntry_Object = MibTableRow
iccpRgEntry = _IccpRgEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 2, 3, 1, 1)
)
iccpRgEntry.setIndexNames(
    (0, "LUM-ICCP-MIB", "iccpRgIndex"),
)
if mibBuilder.loadTexts:
    iccpRgEntry.setStatus("current")


class _IccpRgIndex_Type(Unsigned32):
    """Custom type iccpRgIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IccpRgIndex_Type.__name__ = "Unsigned32"
_IccpRgIndex_Object = MibTableColumn
iccpRgIndex = _IccpRgIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 2, 3, 1, 1, 1),
    _IccpRgIndex_Type()
)
iccpRgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iccpRgIndex.setStatus("current")
_IccpRgName_Type = MgmtNameString
_IccpRgName_Object = MibTableColumn
iccpRgName = _IccpRgName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 2, 3, 1, 1, 2),
    _IccpRgName_Type()
)
iccpRgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iccpRgName.setStatus("current")


class _IccpRgDescr_Type(DisplayString):
    """Custom type iccpRgDescr based on DisplayString"""
    defaultValue = OctetString("")


_IccpRgDescr_Type.__name__ = "DisplayString"
_IccpRgDescr_Object = MibTableColumn
iccpRgDescr = _IccpRgDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 2, 3, 1, 1, 3),
    _IccpRgDescr_Type()
)
iccpRgDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccpRgDescr.setStatus("current")


class _IccpRgRedundancyGroupId_Type(Unsigned32):
    """Custom type iccpRgRedundancyGroupId based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_IccpRgRedundancyGroupId_Type.__name__ = "Unsigned32"
_IccpRgRedundancyGroupId_Object = MibTableColumn
iccpRgRedundancyGroupId = _IccpRgRedundancyGroupId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 2, 3, 1, 1, 4),
    _IccpRgRedundancyGroupId_Type()
)
iccpRgRedundancyGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccpRgRedundancyGroupId.setStatus("current")


class _IccpRgRedundancyObjectId_Type(Unsigned32):
    """Custom type iccpRgRedundancyObjectId based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_IccpRgRedundancyObjectId_Type.__name__ = "Unsigned32"
_IccpRgRedundancyObjectId_Object = MibTableColumn
iccpRgRedundancyObjectId = _IccpRgRedundancyObjectId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 2, 3, 1, 1, 5),
    _IccpRgRedundancyObjectId_Type()
)
iccpRgRedundancyObjectId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccpRgRedundancyObjectId.setStatus("current")
_IccpRgPeerMacAddress_Type = MacAddress
_IccpRgPeerMacAddress_Object = MibTableColumn
iccpRgPeerMacAddress = _IccpRgPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 2, 3, 1, 1, 6),
    _IccpRgPeerMacAddress_Type()
)
iccpRgPeerMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccpRgPeerMacAddress.setStatus("current")


class _IccpRgPortId_Type(Unsigned32):
    """Custom type iccpRgPortId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_IccpRgPortId_Type.__name__ = "Unsigned32"
_IccpRgPortId_Object = MibTableColumn
iccpRgPortId = _IccpRgPortId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 2, 3, 1, 1, 7),
    _IccpRgPortId_Type()
)
iccpRgPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iccpRgPortId.setStatus("current")


class _IccpRgMepName_Type(DisplayString):
    """Custom type iccpRgMepName based on DisplayString"""
    defaultValue = OctetString("")


_IccpRgMepName_Type.__name__ = "DisplayString"
_IccpRgMepName_Object = MibTableColumn
iccpRgMepName = _IccpRgMepName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 2, 3, 1, 1, 8),
    _IccpRgMepName_Type()
)
iccpRgMepName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccpRgMepName.setStatus("current")


class _IccpRgMepMaid_Type(DisplayString):
    """Custom type iccpRgMepMaid based on DisplayString"""
    defaultValue = OctetString("")


_IccpRgMepMaid_Type.__name__ = "DisplayString"
_IccpRgMepMaid_Object = MibTableColumn
iccpRgMepMaid = _IccpRgMepMaid_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 2, 3, 1, 1, 9),
    _IccpRgMepMaid_Type()
)
iccpRgMepMaid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccpRgMepMaid.setStatus("current")


class _IccpRgMepId_Type(Unsigned32):
    """Custom type iccpRgMepId based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_IccpRgMepId_Type.__name__ = "Unsigned32"
_IccpRgMepId_Object = MibTableColumn
iccpRgMepId = _IccpRgMepId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 2, 3, 1, 1, 10),
    _IccpRgMepId_Type()
)
iccpRgMepId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccpRgMepId.setStatus("current")


class _IccpRgMegGroupId_Type(Unsigned32):
    """Custom type iccpRgMegGroupId based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_IccpRgMegGroupId_Type.__name__ = "Unsigned32"
_IccpRgMegGroupId_Object = MibTableColumn
iccpRgMegGroupId = _IccpRgMegGroupId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 2, 3, 1, 1, 11),
    _IccpRgMegGroupId_Type()
)
iccpRgMegGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iccpRgMegGroupId.setStatus("current")


class _IccpRgMegLevel_Type(Unsigned32):
    """Custom type iccpRgMegLevel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_IccpRgMegLevel_Type.__name__ = "Unsigned32"
_IccpRgMegLevel_Object = MibTableColumn
iccpRgMegLevel = _IccpRgMegLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 2, 3, 1, 1, 12),
    _IccpRgMegLevel_Type()
)
iccpRgMegLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iccpRgMegLevel.setStatus("current")


class _IccpRgVlanId_Type(Unsigned32):
    """Custom type iccpRgVlanId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_IccpRgVlanId_Type.__name__ = "Unsigned32"
_IccpRgVlanId_Object = MibTableColumn
iccpRgVlanId = _IccpRgVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 2, 3, 1, 1, 13),
    _IccpRgVlanId_Type()
)
iccpRgVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iccpRgVlanId.setStatus("current")


class _IccpRgState_Type(Integer32):
    """Custom type iccpRgState based on Integer32"""
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
        *(("nonExistent", 1),
          ("connecting", 2),
          ("operational", 3),
          ("undefined", 4))
    )


_IccpRgState_Type.__name__ = "Integer32"
_IccpRgState_Object = MibTableColumn
iccpRgState = _IccpRgState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 2, 3, 1, 1, 14),
    _IccpRgState_Type()
)
iccpRgState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iccpRgState.setStatus("current")


class _IccpRgApplicationState_Type(Integer32):
    """Custom type iccpRgApplicationState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("nonExistent", 1),
          ("reset", 2),
          ("connectSent", 3),
          ("connectReceive", 4),
          ("connecting", 5),
          ("operational", 6),
          ("undefined", 7))
    )


_IccpRgApplicationState_Type.__name__ = "Integer32"
_IccpRgApplicationState_Object = MibTableColumn
iccpRgApplicationState = _IccpRgApplicationState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 2, 3, 1, 1, 15),
    _IccpRgApplicationState_Type()
)
iccpRgApplicationState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iccpRgApplicationState.setStatus("current")


class _IccpRgInternalReference_Type(Unsigned32):
    """Custom type iccpRgInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IccpRgInternalReference_Type.__name__ = "Unsigned32"
_IccpRgInternalReference_Object = MibTableColumn
iccpRgInternalReference = _IccpRgInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 2, 3, 1, 1, 16),
    _IccpRgInternalReference_Type()
)
iccpRgInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iccpRgInternalReference.setStatus("current")


class _IccpRgApplication_Type(Integer32):
    """Custom type iccpRgApplication based on Integer32"""
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
        *(("none", 1),
          ("mLacp", 2),
          ("pwRed", 3),
          ("mLacpAndIccp", 4))
    )


_IccpRgApplication_Type.__name__ = "Integer32"
_IccpRgApplication_Object = MibTableColumn
iccpRgApplication = _IccpRgApplication_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 2, 3, 1, 1, 17),
    _IccpRgApplication_Type()
)
iccpRgApplication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iccpRgApplication.setStatus("current")
_IccpRgCreateMcLag_Type = CommandString
_IccpRgCreateMcLag_Object = MibTableColumn
iccpRgCreateMcLag = _IccpRgCreateMcLag_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 2, 3, 1, 1, 18),
    _IccpRgCreateMcLag_Type()
)
iccpRgCreateMcLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iccpRgCreateMcLag.setStatus("current")
_IccpRgCommunicationFailure_Type = FaultStatus
_IccpRgCommunicationFailure_Object = MibTableColumn
iccpRgCommunicationFailure = _IccpRgCommunicationFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 2, 3, 1, 1, 19),
    _IccpRgCommunicationFailure_Type()
)
iccpRgCommunicationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iccpRgCommunicationFailure.setStatus("current")

# Managed Objects groups

iccpGeneralGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 1, 1, 1)
)
iccpGeneralGroupV1.setObjects(
      *(("LUM-ICCP-MIB", "iccpGeneralLastChangeTime"),
        ("LUM-ICCP-MIB", "iccpGeneralStateLastChangeTime"),
        ("LUM-ICCP-MIB", "iccpGeneralIccpNodeTableSize"))
)
if mibBuilder.loadTexts:
    iccpGeneralGroupV1.setStatus("current")

iccpNodeGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 1, 1, 2)
)
iccpNodeGroupV1.setObjects(
      *(("LUM-ICCP-MIB", "iccpNodeIndex"),
        ("LUM-ICCP-MIB", "iccpNodeSystemMacAddress"),
        ("LUM-ICCP-MIB", "iccpNodeCreateIccpRg"),
        ("LUM-ICCP-MIB", "iccpNodeInternalReference"))
)
if mibBuilder.loadTexts:
    iccpNodeGroupV1.setStatus("current")

iccpRgGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 1, 1, 3)
)
iccpRgGroupV1.setObjects(
      *(("LUM-ICCP-MIB", "iccpRgIndex"),
        ("LUM-ICCP-MIB", "iccpRgName"),
        ("LUM-ICCP-MIB", "iccpRgDescr"),
        ("LUM-ICCP-MIB", "iccpRgRedundancyGroupId"),
        ("LUM-ICCP-MIB", "iccpRgRedundancyObjectId"),
        ("LUM-ICCP-MIB", "iccpRgPeerMacAddress"),
        ("LUM-ICCP-MIB", "iccpRgPortId"),
        ("LUM-ICCP-MIB", "iccpRgMepName"),
        ("LUM-ICCP-MIB", "iccpRgMepMaid"),
        ("LUM-ICCP-MIB", "iccpRgMepId"),
        ("LUM-ICCP-MIB", "iccpRgMegGroupId"),
        ("LUM-ICCP-MIB", "iccpRgMegLevel"),
        ("LUM-ICCP-MIB", "iccpRgVlanId"),
        ("LUM-ICCP-MIB", "iccpRgState"),
        ("LUM-ICCP-MIB", "iccpRgApplicationState"),
        ("LUM-ICCP-MIB", "iccpRgInternalReference"),
        ("LUM-ICCP-MIB", "iccpRgApplication"),
        ("LUM-ICCP-MIB", "iccpRgCreateMcLag"),
        ("LUM-ICCP-MIB", "iccpRgCommunicationFailure"))
)
if mibBuilder.loadTexts:
    iccpRgGroupV1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumIccpBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61, 1, 2, 1)
)
lumIccpBasicComplV1.setObjects(
      *(("LUM-ICCP-MIB", "iccpNodeGroupV1"),
        ("LUM-ICCP-MIB", "iccpRgGroupV1"))
)
if mibBuilder.loadTexts:
    lumIccpBasicComplV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-ICCP-MIB",
    **{"IccpLabel": IccpLabel,
       "IccpIdentifier": IccpIdentifier,
       "lumIccpMIBModule": lumIccpMIBModule,
       "lumIccpConfs": lumIccpConfs,
       "lumIccpGroups": lumIccpGroups,
       "iccpGeneralGroupV1": iccpGeneralGroupV1,
       "iccpNodeGroupV1": iccpNodeGroupV1,
       "iccpRgGroupV1": iccpRgGroupV1,
       "lumIccpCompl": lumIccpCompl,
       "lumIccpBasicComplV1": lumIccpBasicComplV1,
       "lumIccpMIBObjects": lumIccpMIBObjects,
       "iccpGeneral": iccpGeneral,
       "iccpGeneralLastChangeTime": iccpGeneralLastChangeTime,
       "iccpGeneralStateLastChangeTime": iccpGeneralStateLastChangeTime,
       "iccpGeneralIccpNodeTableSize": iccpGeneralIccpNodeTableSize,
       "iccpGeneralIccpRgTableSize": iccpGeneralIccpRgTableSize,
       "iccpNodeList": iccpNodeList,
       "iccpNodeTable": iccpNodeTable,
       "iccpNodeEntry": iccpNodeEntry,
       "iccpNodeIndex": iccpNodeIndex,
       "iccpNodeName": iccpNodeName,
       "iccpNodeSystemMacAddress": iccpNodeSystemMacAddress,
       "iccpNodeCreateIccpRg": iccpNodeCreateIccpRg,
       "iccpNodeInternalReference": iccpNodeInternalReference,
       "iccpRgList": iccpRgList,
       "iccpRgTable": iccpRgTable,
       "iccpRgEntry": iccpRgEntry,
       "iccpRgIndex": iccpRgIndex,
       "iccpRgName": iccpRgName,
       "iccpRgDescr": iccpRgDescr,
       "iccpRgRedundancyGroupId": iccpRgRedundancyGroupId,
       "iccpRgRedundancyObjectId": iccpRgRedundancyObjectId,
       "iccpRgPeerMacAddress": iccpRgPeerMacAddress,
       "iccpRgPortId": iccpRgPortId,
       "iccpRgMepName": iccpRgMepName,
       "iccpRgMepMaid": iccpRgMepMaid,
       "iccpRgMepId": iccpRgMepId,
       "iccpRgMegGroupId": iccpRgMegGroupId,
       "iccpRgMegLevel": iccpRgMegLevel,
       "iccpRgVlanId": iccpRgVlanId,
       "iccpRgState": iccpRgState,
       "iccpRgApplicationState": iccpRgApplicationState,
       "iccpRgInternalReference": iccpRgInternalReference,
       "iccpRgApplication": iccpRgApplication,
       "iccpRgCreateMcLag": iccpRgCreateMcLag,
       "iccpRgCommunicationFailure": iccpRgCommunicationFailure}
)
