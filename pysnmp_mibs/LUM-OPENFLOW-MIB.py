# SNMP MIB module (LUM-OPENFLOW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-OPENFLOW-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:33 2025
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
 lumOpenflowMIB) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumModules",
    "lumOpenflowMIB")

(CommandString,
 MgmtNameString,
 SlotNumber,
 SubrackNumber) = mibBuilder.importSymbols(
    "LUM-TC",
    "CommandString",
    "MgmtNameString",
    "SlotNumber",
    "SubrackNumber")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

lumOpenflowMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 69)
)
if mibBuilder.loadTexts:
    lumOpenflowMIBModule.setRevisions(
        ("2018-09-01 00:00",
         "2017-06-15 00:00",
         "2016-11-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumOpenflowConfs_ObjectIdentity = ObjectIdentity
lumOpenflowConfs = _LumOpenflowConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 1)
)
_LumOpenflowGroups_ObjectIdentity = ObjectIdentity
lumOpenflowGroups = _LumOpenflowGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 1, 1)
)
_LumOpenflowCompl_ObjectIdentity = ObjectIdentity
lumOpenflowCompl = _LumOpenflowCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 1, 2)
)
_LumOpenflowMIBObjects_ObjectIdentity = ObjectIdentity
lumOpenflowMIBObjects = _LumOpenflowMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2)
)
_OpenflowGeneral_ObjectIdentity = ObjectIdentity
openflowGeneral = _OpenflowGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 1)
)
_OpenflowGeneralConfigLastChangeTime_Type = DateAndTime
_OpenflowGeneralConfigLastChangeTime_Object = MibScalar
openflowGeneralConfigLastChangeTime = _OpenflowGeneralConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 1, 1),
    _OpenflowGeneralConfigLastChangeTime_Type()
)
openflowGeneralConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openflowGeneralConfigLastChangeTime.setStatus("current")
_OpenflowGeneralStateLastChangeTime_Type = DateAndTime
_OpenflowGeneralStateLastChangeTime_Object = MibScalar
openflowGeneralStateLastChangeTime = _OpenflowGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 1, 2),
    _OpenflowGeneralStateLastChangeTime_Type()
)
openflowGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openflowGeneralStateLastChangeTime.setStatus("current")
_OpenflowGeneralLogicalSwitchTableSize_Type = Unsigned32
_OpenflowGeneralLogicalSwitchTableSize_Object = MibScalar
openflowGeneralLogicalSwitchTableSize = _OpenflowGeneralLogicalSwitchTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 1, 3),
    _OpenflowGeneralLogicalSwitchTableSize_Type()
)
openflowGeneralLogicalSwitchTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openflowGeneralLogicalSwitchTableSize.setStatus("current")
_OpenflowGeneralGenericTableSize_Type = Unsigned32
_OpenflowGeneralGenericTableSize_Object = MibScalar
openflowGeneralGenericTableSize = _OpenflowGeneralGenericTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 1, 4),
    _OpenflowGeneralGenericTableSize_Type()
)
openflowGeneralGenericTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openflowGeneralGenericTableSize.setStatus("current")
_OpenflowGeneralConnectionTableSize_Type = Unsigned32
_OpenflowGeneralConnectionTableSize_Object = MibScalar
openflowGeneralConnectionTableSize = _OpenflowGeneralConnectionTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 1, 5),
    _OpenflowGeneralConnectionTableSize_Type()
)
openflowGeneralConnectionTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openflowGeneralConnectionTableSize.setStatus("current")
_OpenflowGeneralDiagnosticsTableSize_Type = Unsigned32
_OpenflowGeneralDiagnosticsTableSize_Object = MibScalar
openflowGeneralDiagnosticsTableSize = _OpenflowGeneralDiagnosticsTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 1, 6),
    _OpenflowGeneralDiagnosticsTableSize_Type()
)
openflowGeneralDiagnosticsTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openflowGeneralDiagnosticsTableSize.setStatus("current")
_OpenflowGeneralLogTableSize_Type = Unsigned32
_OpenflowGeneralLogTableSize_Object = MibScalar
openflowGeneralLogTableSize = _OpenflowGeneralLogTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 1, 7),
    _OpenflowGeneralLogTableSize_Type()
)
openflowGeneralLogTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openflowGeneralLogTableSize.setStatus("current")
_OpenflowLogicalSwitchList_ObjectIdentity = ObjectIdentity
openflowLogicalSwitchList = _OpenflowLogicalSwitchList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 2)
)
_OpenflowLogicalSwitchTable_Object = MibTable
openflowLogicalSwitchTable = _OpenflowLogicalSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 2, 1)
)
if mibBuilder.loadTexts:
    openflowLogicalSwitchTable.setStatus("current")
_OpenflowLogicalSwitchEntry_Object = MibTableRow
openflowLogicalSwitchEntry = _OpenflowLogicalSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 2, 1, 1)
)
openflowLogicalSwitchEntry.setIndexNames(
    (0, "LUM-OPENFLOW-MIB", "openflowLogicalSwitchIndex"),
)
if mibBuilder.loadTexts:
    openflowLogicalSwitchEntry.setStatus("current")
_OpenflowLogicalSwitchName_Type = MgmtNameString
_OpenflowLogicalSwitchName_Object = MibTableColumn
openflowLogicalSwitchName = _OpenflowLogicalSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 2, 1, 1, 1),
    _OpenflowLogicalSwitchName_Type()
)
openflowLogicalSwitchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openflowLogicalSwitchName.setStatus("current")


class _OpenflowLogicalSwitchIndex_Type(Unsigned32):
    """Custom type openflowLogicalSwitchIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OpenflowLogicalSwitchIndex_Type.__name__ = "Unsigned32"
_OpenflowLogicalSwitchIndex_Object = MibTableColumn
openflowLogicalSwitchIndex = _OpenflowLogicalSwitchIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 2, 1, 1, 2),
    _OpenflowLogicalSwitchIndex_Type()
)
openflowLogicalSwitchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openflowLogicalSwitchIndex.setStatus("current")
_OpenflowLogicalSwitchDescr_Type = DisplayString
_OpenflowLogicalSwitchDescr_Object = MibTableColumn
openflowLogicalSwitchDescr = _OpenflowLogicalSwitchDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 2, 1, 1, 3),
    _OpenflowLogicalSwitchDescr_Type()
)
openflowLogicalSwitchDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    openflowLogicalSwitchDescr.setStatus("current")


class _OpenflowLogicalSwitchIdentity_Type(Unsigned32):
    """Custom type openflowLogicalSwitchIdentity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OpenflowLogicalSwitchIdentity_Type.__name__ = "Unsigned32"
_OpenflowLogicalSwitchIdentity_Object = MibTableColumn
openflowLogicalSwitchIdentity = _OpenflowLogicalSwitchIdentity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 2, 1, 1, 4),
    _OpenflowLogicalSwitchIdentity_Type()
)
openflowLogicalSwitchIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openflowLogicalSwitchIdentity.setStatus("current")


class _OpenflowLogicalSwitchMacAddress_Type(OctetString):
    """Custom type openflowLogicalSwitchMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_OpenflowLogicalSwitchMacAddress_Type.__name__ = "OctetString"
_OpenflowLogicalSwitchMacAddress_Object = MibTableColumn
openflowLogicalSwitchMacAddress = _OpenflowLogicalSwitchMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 2, 1, 1, 5),
    _OpenflowLogicalSwitchMacAddress_Type()
)
openflowLogicalSwitchMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    openflowLogicalSwitchMacAddress.setStatus("current")
_OpenflowLogicalSwitchDpId_Type = DisplayString
_OpenflowLogicalSwitchDpId_Object = MibTableColumn
openflowLogicalSwitchDpId = _OpenflowLogicalSwitchDpId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 2, 1, 1, 6),
    _OpenflowLogicalSwitchDpId_Type()
)
openflowLogicalSwitchDpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openflowLogicalSwitchDpId.setStatus("current")
_OpenflowLogicalSwitchAssociateCxn_Type = CommandString
_OpenflowLogicalSwitchAssociateCxn_Object = MibTableColumn
openflowLogicalSwitchAssociateCxn = _OpenflowLogicalSwitchAssociateCxn_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 2, 1, 1, 7),
    _OpenflowLogicalSwitchAssociateCxn_Type()
)
openflowLogicalSwitchAssociateCxn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openflowLogicalSwitchAssociateCxn.setStatus("current")
_OpenflowLogicalSwitchSubrack_Type = SubrackNumber
_OpenflowLogicalSwitchSubrack_Object = MibTableColumn
openflowLogicalSwitchSubrack = _OpenflowLogicalSwitchSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 2, 1, 1, 8),
    _OpenflowLogicalSwitchSubrack_Type()
)
openflowLogicalSwitchSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    openflowLogicalSwitchSubrack.setStatus("current")
_OpenflowLogicalSwitchSlot_Type = SlotNumber
_OpenflowLogicalSwitchSlot_Object = MibTableColumn
openflowLogicalSwitchSlot = _OpenflowLogicalSwitchSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 2, 1, 1, 9),
    _OpenflowLogicalSwitchSlot_Type()
)
openflowLogicalSwitchSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    openflowLogicalSwitchSlot.setStatus("current")
_OpenflowLogicalSwitchGetTracelogs_Type = CommandString
_OpenflowLogicalSwitchGetTracelogs_Object = MibTableColumn
openflowLogicalSwitchGetTracelogs = _OpenflowLogicalSwitchGetTracelogs_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 2, 1, 1, 10),
    _OpenflowLogicalSwitchGetTracelogs_Type()
)
openflowLogicalSwitchGetTracelogs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openflowLogicalSwitchGetTracelogs.setStatus("current")
_OpenflowLogicalSwitchOfVersion_Type = DisplayString
_OpenflowLogicalSwitchOfVersion_Object = MibTableColumn
openflowLogicalSwitchOfVersion = _OpenflowLogicalSwitchOfVersion_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 2, 1, 1, 11),
    _OpenflowLogicalSwitchOfVersion_Type()
)
openflowLogicalSwitchOfVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openflowLogicalSwitchOfVersion.setStatus("current")
_OpenflowConnectionList_ObjectIdentity = ObjectIdentity
openflowConnectionList = _OpenflowConnectionList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 3)
)
_OpenflowConnectionTable_Object = MibTable
openflowConnectionTable = _OpenflowConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 3, 1)
)
if mibBuilder.loadTexts:
    openflowConnectionTable.setStatus("current")
_OpenflowConnectionEntry_Object = MibTableRow
openflowConnectionEntry = _OpenflowConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 3, 1, 1)
)
openflowConnectionEntry.setIndexNames(
    (0, "LUM-OPENFLOW-MIB", "openflowConnectionIndex"),
)
if mibBuilder.loadTexts:
    openflowConnectionEntry.setStatus("current")
_OpenflowConnectionName_Type = MgmtNameString
_OpenflowConnectionName_Object = MibTableColumn
openflowConnectionName = _OpenflowConnectionName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 3, 1, 1, 1),
    _OpenflowConnectionName_Type()
)
openflowConnectionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openflowConnectionName.setStatus("current")


class _OpenflowConnectionIndex_Type(Unsigned32):
    """Custom type openflowConnectionIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OpenflowConnectionIndex_Type.__name__ = "Unsigned32"
_OpenflowConnectionIndex_Object = MibTableColumn
openflowConnectionIndex = _OpenflowConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 3, 1, 1, 2),
    _OpenflowConnectionIndex_Type()
)
openflowConnectionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openflowConnectionIndex.setStatus("current")
_OpenflowConnectionDescr_Type = DisplayString
_OpenflowConnectionDescr_Object = MibTableColumn
openflowConnectionDescr = _OpenflowConnectionDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 3, 1, 1, 3),
    _OpenflowConnectionDescr_Type()
)
openflowConnectionDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    openflowConnectionDescr.setStatus("current")


class _OpenflowConnectionIdentity_Type(Unsigned32):
    """Custom type openflowConnectionIdentity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OpenflowConnectionIdentity_Type.__name__ = "Unsigned32"
_OpenflowConnectionIdentity_Object = MibTableColumn
openflowConnectionIdentity = _OpenflowConnectionIdentity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 3, 1, 1, 4),
    _OpenflowConnectionIdentity_Type()
)
openflowConnectionIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openflowConnectionIdentity.setStatus("current")


class _OpenflowConnectionSwitchIdentity_Type(Unsigned32):
    """Custom type openflowConnectionSwitchIdentity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OpenflowConnectionSwitchIdentity_Type.__name__ = "Unsigned32"
_OpenflowConnectionSwitchIdentity_Object = MibTableColumn
openflowConnectionSwitchIdentity = _OpenflowConnectionSwitchIdentity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 3, 1, 1, 5),
    _OpenflowConnectionSwitchIdentity_Type()
)
openflowConnectionSwitchIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openflowConnectionSwitchIdentity.setStatus("current")
_OpenflowConnectionIpv4Addr_Type = IpAddress
_OpenflowConnectionIpv4Addr_Object = MibTableColumn
openflowConnectionIpv4Addr = _OpenflowConnectionIpv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 3, 1, 1, 6),
    _OpenflowConnectionIpv4Addr_Type()
)
openflowConnectionIpv4Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    openflowConnectionIpv4Addr.setStatus("current")


class _OpenflowConnectionTcpPort_Type(Unsigned32):
    """Custom type openflowConnectionTcpPort based on Unsigned32"""
    defaultValue = 6653

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OpenflowConnectionTcpPort_Type.__name__ = "Unsigned32"
_OpenflowConnectionTcpPort_Object = MibTableColumn
openflowConnectionTcpPort = _OpenflowConnectionTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 3, 1, 1, 7),
    _OpenflowConnectionTcpPort_Type()
)
openflowConnectionTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openflowConnectionTcpPort.setStatus("current")


class _OpenflowConnectionState_Type(Integer32):
    """Custom type openflowConnectionState based on Integer32"""
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
        *(("disconnected", 1),
          ("connecting", 2),
          ("connected", 3),
          ("disconnecting", 4))
    )


_OpenflowConnectionState_Type.__name__ = "Integer32"
_OpenflowConnectionState_Object = MibTableColumn
openflowConnectionState = _OpenflowConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 3, 1, 1, 8),
    _OpenflowConnectionState_Type()
)
openflowConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openflowConnectionState.setStatus("current")


class _OpenflowConnectionRole_Type(Integer32):
    """Custom type openflowConnectionRole based on Integer32"""
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
          ("equal", 2),
          ("master", 3),
          ("slave", 4))
    )


_OpenflowConnectionRole_Type.__name__ = "Integer32"
_OpenflowConnectionRole_Object = MibTableColumn
openflowConnectionRole = _OpenflowConnectionRole_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 3, 1, 1, 9),
    _OpenflowConnectionRole_Type()
)
openflowConnectionRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openflowConnectionRole.setStatus("current")
_OpenflowConnectionOfVersion_Type = DisplayString
_OpenflowConnectionOfVersion_Object = MibTableColumn
openflowConnectionOfVersion = _OpenflowConnectionOfVersion_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 3, 1, 1, 10),
    _OpenflowConnectionOfVersion_Type()
)
openflowConnectionOfVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openflowConnectionOfVersion.setStatus("current")
_OpenflowConnectionSubrack_Type = SubrackNumber
_OpenflowConnectionSubrack_Object = MibTableColumn
openflowConnectionSubrack = _OpenflowConnectionSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 3, 1, 1, 11),
    _OpenflowConnectionSubrack_Type()
)
openflowConnectionSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    openflowConnectionSubrack.setStatus("current")
_OpenflowConnectionSlot_Type = SlotNumber
_OpenflowConnectionSlot_Object = MibTableColumn
openflowConnectionSlot = _OpenflowConnectionSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 3, 1, 1, 12),
    _OpenflowConnectionSlot_Type()
)
openflowConnectionSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    openflowConnectionSlot.setStatus("current")
_OpenflowGenericList_ObjectIdentity = ObjectIdentity
openflowGenericList = _OpenflowGenericList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 4)
)
_OpenflowGenericTable_Object = MibTable
openflowGenericTable = _OpenflowGenericTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 4, 1)
)
if mibBuilder.loadTexts:
    openflowGenericTable.setStatus("current")
_OpenflowGenericEntry_Object = MibTableRow
openflowGenericEntry = _OpenflowGenericEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 4, 1, 1)
)
openflowGenericEntry.setIndexNames(
    (0, "LUM-OPENFLOW-MIB", "openflowGenericIndex"),
)
if mibBuilder.loadTexts:
    openflowGenericEntry.setStatus("current")


class _OpenflowGenericIndex_Type(Unsigned32):
    """Custom type openflowGenericIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OpenflowGenericIndex_Type.__name__ = "Unsigned32"
_OpenflowGenericIndex_Object = MibTableColumn
openflowGenericIndex = _OpenflowGenericIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 4, 1, 1, 1),
    _OpenflowGenericIndex_Type()
)
openflowGenericIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openflowGenericIndex.setStatus("current")
_OpenflowGenericName_Type = MgmtNameString
_OpenflowGenericName_Object = MibTableColumn
openflowGenericName = _OpenflowGenericName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 4, 1, 1, 2),
    _OpenflowGenericName_Type()
)
openflowGenericName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openflowGenericName.setStatus("current")


class _OpenflowGenericSubrack_Type(Unsigned32):
    """Custom type openflowGenericSubrack based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OpenflowGenericSubrack_Type.__name__ = "Unsigned32"
_OpenflowGenericSubrack_Object = MibTableColumn
openflowGenericSubrack = _OpenflowGenericSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 4, 1, 1, 3),
    _OpenflowGenericSubrack_Type()
)
openflowGenericSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openflowGenericSubrack.setStatus("current")


class _OpenflowGenericSlot_Type(Unsigned32):
    """Custom type openflowGenericSlot based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OpenflowGenericSlot_Type.__name__ = "Unsigned32"
_OpenflowGenericSlot_Object = MibTableColumn
openflowGenericSlot = _OpenflowGenericSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 4, 1, 1, 4),
    _OpenflowGenericSlot_Type()
)
openflowGenericSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openflowGenericSlot.setStatus("current")
_OpenflowGenericCreateOFLS_Type = CommandString
_OpenflowGenericCreateOFLS_Object = MibTableColumn
openflowGenericCreateOFLS = _OpenflowGenericCreateOFLS_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 4, 1, 1, 5),
    _OpenflowGenericCreateOFLS_Type()
)
openflowGenericCreateOFLS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openflowGenericCreateOFLS.setStatus("current")
_OpenflowDiagnosticsList_ObjectIdentity = ObjectIdentity
openflowDiagnosticsList = _OpenflowDiagnosticsList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 5)
)
_OpenflowDiagnosticsTable_Object = MibTable
openflowDiagnosticsTable = _OpenflowDiagnosticsTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 5, 1)
)
if mibBuilder.loadTexts:
    openflowDiagnosticsTable.setStatus("current")
_OpenflowDiagnosticsEntry_Object = MibTableRow
openflowDiagnosticsEntry = _OpenflowDiagnosticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 5, 1, 1)
)
openflowDiagnosticsEntry.setIndexNames(
    (0, "LUM-OPENFLOW-MIB", "openflowDiagnosticsIndex"),
)
if mibBuilder.loadTexts:
    openflowDiagnosticsEntry.setStatus("current")


class _OpenflowDiagnosticsIndex_Type(Unsigned32):
    """Custom type openflowDiagnosticsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OpenflowDiagnosticsIndex_Type.__name__ = "Unsigned32"
_OpenflowDiagnosticsIndex_Object = MibTableColumn
openflowDiagnosticsIndex = _OpenflowDiagnosticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 5, 1, 1, 1),
    _OpenflowDiagnosticsIndex_Type()
)
openflowDiagnosticsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openflowDiagnosticsIndex.setStatus("current")
_OpenflowDiagnosticsName_Type = MgmtNameString
_OpenflowDiagnosticsName_Object = MibTableColumn
openflowDiagnosticsName = _OpenflowDiagnosticsName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 5, 1, 1, 2),
    _OpenflowDiagnosticsName_Type()
)
openflowDiagnosticsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openflowDiagnosticsName.setStatus("current")
_OpenflowDiagnosticsIpv4Addr_Type = IpAddress
_OpenflowDiagnosticsIpv4Addr_Object = MibTableColumn
openflowDiagnosticsIpv4Addr = _OpenflowDiagnosticsIpv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 5, 1, 1, 3),
    _OpenflowDiagnosticsIpv4Addr_Type()
)
openflowDiagnosticsIpv4Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    openflowDiagnosticsIpv4Addr.setStatus("current")


class _OpenflowDiagnosticsTcpPort_Type(Unsigned32):
    """Custom type openflowDiagnosticsTcpPort based on Unsigned32"""
    defaultValue = 9999

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OpenflowDiagnosticsTcpPort_Type.__name__ = "Unsigned32"
_OpenflowDiagnosticsTcpPort_Object = MibTableColumn
openflowDiagnosticsTcpPort = _OpenflowDiagnosticsTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 5, 1, 1, 4),
    _OpenflowDiagnosticsTcpPort_Type()
)
openflowDiagnosticsTcpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    openflowDiagnosticsTcpPort.setStatus("current")


class _OpenflowDiagnosticsLogServerType_Type(Integer32):
    """Custom type openflowDiagnosticsLogServerType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("syslog", 1),
          ("notApplicable", 2147483647))
    )


_OpenflowDiagnosticsLogServerType_Type.__name__ = "Integer32"
_OpenflowDiagnosticsLogServerType_Object = MibTableColumn
openflowDiagnosticsLogServerType = _OpenflowDiagnosticsLogServerType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 5, 1, 1, 5),
    _OpenflowDiagnosticsLogServerType_Type()
)
openflowDiagnosticsLogServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    openflowDiagnosticsLogServerType.setStatus("current")
_OpenflowDiagnosticsConfigure_Type = CommandString
_OpenflowDiagnosticsConfigure_Object = MibTableColumn
openflowDiagnosticsConfigure = _OpenflowDiagnosticsConfigure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 5, 1, 1, 6),
    _OpenflowDiagnosticsConfigure_Type()
)
openflowDiagnosticsConfigure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openflowDiagnosticsConfigure.setStatus("current")
_OpenflowDiagnosticsSubrack_Type = SubrackNumber
_OpenflowDiagnosticsSubrack_Object = MibTableColumn
openflowDiagnosticsSubrack = _OpenflowDiagnosticsSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 5, 1, 1, 7),
    _OpenflowDiagnosticsSubrack_Type()
)
openflowDiagnosticsSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openflowDiagnosticsSubrack.setStatus("current")
_OpenflowLogList_ObjectIdentity = ObjectIdentity
openflowLogList = _OpenflowLogList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 6)
)
_OpenflowLogTable_Object = MibTable
openflowLogTable = _OpenflowLogTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 6, 1)
)
if mibBuilder.loadTexts:
    openflowLogTable.setStatus("current")
_OpenflowLogEntry_Object = MibTableRow
openflowLogEntry = _OpenflowLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 6, 1, 1)
)
openflowLogEntry.setIndexNames(
    (0, "LUM-OPENFLOW-MIB", "openflowLogIndex"),
)
if mibBuilder.loadTexts:
    openflowLogEntry.setStatus("current")


class _OpenflowLogIndex_Type(Unsigned32):
    """Custom type openflowLogIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OpenflowLogIndex_Type.__name__ = "Unsigned32"
_OpenflowLogIndex_Object = MibTableColumn
openflowLogIndex = _OpenflowLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 6, 1, 1, 1),
    _OpenflowLogIndex_Type()
)
openflowLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openflowLogIndex.setStatus("current")
_OpenflowLogName_Type = MgmtNameString
_OpenflowLogName_Object = MibTableColumn
openflowLogName = _OpenflowLogName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 6, 1, 1, 2),
    _OpenflowLogName_Type()
)
openflowLogName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openflowLogName.setStatus("current")


class _OpenflowLogSubrack_Type(Unsigned32):
    """Custom type openflowLogSubrack based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OpenflowLogSubrack_Type.__name__ = "Unsigned32"
_OpenflowLogSubrack_Object = MibTableColumn
openflowLogSubrack = _OpenflowLogSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 6, 1, 1, 3),
    _OpenflowLogSubrack_Type()
)
openflowLogSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openflowLogSubrack.setStatus("current")
_OpenflowLogCreateOFDiagnostics_Type = CommandString
_OpenflowLogCreateOFDiagnostics_Object = MibTableColumn
openflowLogCreateOFDiagnostics = _OpenflowLogCreateOFDiagnostics_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 2, 6, 1, 1, 4),
    _OpenflowLogCreateOFDiagnostics_Type()
)
openflowLogCreateOFDiagnostics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openflowLogCreateOFDiagnostics.setStatus("current")

# Managed Objects groups

openflowGeneralGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 1, 1, 1)
)
openflowGeneralGroupV1.setObjects(
      *(("LUM-OPENFLOW-MIB", "openflowGeneralConfigLastChangeTime"),
        ("LUM-OPENFLOW-MIB", "openflowGeneralStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    openflowGeneralGroupV1.setStatus("current")

openflowLogicalSwitchGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 1, 1, 2)
)
openflowLogicalSwitchGroupV1.setObjects(
      *(("LUM-OPENFLOW-MIB", "openflowLogicalSwitchName"),
        ("LUM-OPENFLOW-MIB", "openflowLogicalSwitchIndex"),
        ("LUM-OPENFLOW-MIB", "openflowLogicalSwitchDescr"),
        ("LUM-OPENFLOW-MIB", "openflowLogicalSwitchIdentity"),
        ("LUM-OPENFLOW-MIB", "openflowLogicalSwitchMacAddress"),
        ("LUM-OPENFLOW-MIB", "openflowLogicalSwitchDpId"),
        ("LUM-OPENFLOW-MIB", "openflowLogicalSwitchSubrack"),
        ("LUM-OPENFLOW-MIB", "openflowLogicalSwitchSlot"))
)
if mibBuilder.loadTexts:
    openflowLogicalSwitchGroupV1.setStatus("deprecated")

openflowConnectionGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 1, 1, 3)
)
openflowConnectionGroupV1.setObjects(
      *(("LUM-OPENFLOW-MIB", "openflowConnectionName"),
        ("LUM-OPENFLOW-MIB", "openflowConnectionIndex"),
        ("LUM-OPENFLOW-MIB", "openflowConnectionDescr"),
        ("LUM-OPENFLOW-MIB", "openflowConnectionIdentity"),
        ("LUM-OPENFLOW-MIB", "openflowConnectionSwitchIdentity"),
        ("LUM-OPENFLOW-MIB", "openflowConnectionIpv4Addr"),
        ("LUM-OPENFLOW-MIB", "openflowConnectionTcpPort"),
        ("LUM-OPENFLOW-MIB", "openflowConnectionState"),
        ("LUM-OPENFLOW-MIB", "openflowConnectionRole"),
        ("LUM-OPENFLOW-MIB", "openflowConnectionOfVersion"),
        ("LUM-OPENFLOW-MIB", "openflowConnectionSubrack"),
        ("LUM-OPENFLOW-MIB", "openflowConnectionSlot"))
)
if mibBuilder.loadTexts:
    openflowConnectionGroupV1.setStatus("current")

openflowGenericGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 1, 1, 4)
)
openflowGenericGroupV1.setObjects(
      *(("LUM-OPENFLOW-MIB", "openflowGenericIndex"),
        ("LUM-OPENFLOW-MIB", "openflowGenericName"),
        ("LUM-OPENFLOW-MIB", "openflowGenericSubrack"),
        ("LUM-OPENFLOW-MIB", "openflowGenericSlot"),
        ("LUM-OPENFLOW-MIB", "openflowGenericCreateOFLS"))
)
if mibBuilder.loadTexts:
    openflowGenericGroupV1.setStatus("current")

openflowLogicalSwitchGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 1, 1, 5)
)
openflowLogicalSwitchGroupV2.setObjects(
      *(("LUM-OPENFLOW-MIB", "openflowLogicalSwitchName"),
        ("LUM-OPENFLOW-MIB", "openflowLogicalSwitchIndex"),
        ("LUM-OPENFLOW-MIB", "openflowLogicalSwitchDescr"),
        ("LUM-OPENFLOW-MIB", "openflowLogicalSwitchIdentity"),
        ("LUM-OPENFLOW-MIB", "openflowLogicalSwitchMacAddress"),
        ("LUM-OPENFLOW-MIB", "openflowLogicalSwitchDpId"),
        ("LUM-OPENFLOW-MIB", "openflowLogicalSwitchAssociateCxn"),
        ("LUM-OPENFLOW-MIB", "openflowLogicalSwitchGetTracelogs"),
        ("LUM-OPENFLOW-MIB", "openflowLogicalSwitchOfVersion"),
        ("LUM-OPENFLOW-MIB", "openflowLogicalSwitchSubrack"),
        ("LUM-OPENFLOW-MIB", "openflowLogicalSwitchSlot"))
)
if mibBuilder.loadTexts:
    openflowLogicalSwitchGroupV2.setStatus("current")

openflowDiagnosticsGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 1, 1, 6)
)
openflowDiagnosticsGroupV1.setObjects(
      *(("LUM-OPENFLOW-MIB", "openflowDiagnosticsIndex"),
        ("LUM-OPENFLOW-MIB", "openflowDiagnosticsName"),
        ("LUM-OPENFLOW-MIB", "openflowDiagnosticsIpv4Addr"),
        ("LUM-OPENFLOW-MIB", "openflowDiagnosticsTcpPort"),
        ("LUM-OPENFLOW-MIB", "openflowDiagnosticsLogServerType"),
        ("LUM-OPENFLOW-MIB", "openflowDiagnosticsConfigure"),
        ("LUM-OPENFLOW-MIB", "openflowDiagnosticsSubrack"))
)
if mibBuilder.loadTexts:
    openflowDiagnosticsGroupV1.setStatus("current")

openflowLogGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 1, 1, 7)
)
openflowLogGroupV1.setObjects(
      *(("LUM-OPENFLOW-MIB", "openflowLogIndex"),
        ("LUM-OPENFLOW-MIB", "openflowLogName"),
        ("LUM-OPENFLOW-MIB", "openflowLogSubrack"),
        ("LUM-OPENFLOW-MIB", "openflowLogCreateOFDiagnostics"))
)
if mibBuilder.loadTexts:
    openflowLogGroupV1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumOpenflowComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 1, 2, 1)
)
lumOpenflowComplV1.setObjects(
      *(("LUM-OPENFLOW-MIB", "openflowGeneralGroupV1"),
        ("LUM-OPENFLOW-MIB", "openflowLogicalSwitchGroupV1"),
        ("LUM-OPENFLOW-MIB", "openflowConnectionGroupV1"),
        ("LUM-OPENFLOW-MIB", "openflowGenericGroupV1"))
)
if mibBuilder.loadTexts:
    lumOpenflowComplV1.setStatus(
        "deprecated"
    )

lumOpenflowComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 1, 2, 2)
)
lumOpenflowComplV2.setObjects(
      *(("LUM-OPENFLOW-MIB", "openflowGeneralGroupV1"),
        ("LUM-OPENFLOW-MIB", "openflowLogicalSwitchGroupV1"),
        ("LUM-OPENFLOW-MIB", "openflowConnectionGroupV1"),
        ("LUM-OPENFLOW-MIB", "openflowGenericGroupV1"))
)
if mibBuilder.loadTexts:
    lumOpenflowComplV2.setStatus(
        "deprecated"
    )

lumOpenflowComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69, 1, 2, 3)
)
lumOpenflowComplV3.setObjects(
      *(("LUM-OPENFLOW-MIB", "openflowGeneralGroupV1"),
        ("LUM-OPENFLOW-MIB", "openflowLogicalSwitchGroupV2"),
        ("LUM-OPENFLOW-MIB", "openflowConnectionGroupV1"),
        ("LUM-OPENFLOW-MIB", "openflowGenericGroupV1"),
        ("LUM-OPENFLOW-MIB", "openflowDiagnosticsGroupV1"),
        ("LUM-OPENFLOW-MIB", "openflowLogGroupV1"))
)
if mibBuilder.loadTexts:
    lumOpenflowComplV3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-OPENFLOW-MIB",
    **{"lumOpenflowMIBModule": lumOpenflowMIBModule,
       "lumOpenflowConfs": lumOpenflowConfs,
       "lumOpenflowGroups": lumOpenflowGroups,
       "openflowGeneralGroupV1": openflowGeneralGroupV1,
       "openflowLogicalSwitchGroupV1": openflowLogicalSwitchGroupV1,
       "openflowConnectionGroupV1": openflowConnectionGroupV1,
       "openflowGenericGroupV1": openflowGenericGroupV1,
       "openflowLogicalSwitchGroupV2": openflowLogicalSwitchGroupV2,
       "openflowDiagnosticsGroupV1": openflowDiagnosticsGroupV1,
       "openflowLogGroupV1": openflowLogGroupV1,
       "lumOpenflowCompl": lumOpenflowCompl,
       "lumOpenflowComplV1": lumOpenflowComplV1,
       "lumOpenflowComplV2": lumOpenflowComplV2,
       "lumOpenflowComplV3": lumOpenflowComplV3,
       "lumOpenflowMIBObjects": lumOpenflowMIBObjects,
       "openflowGeneral": openflowGeneral,
       "openflowGeneralConfigLastChangeTime": openflowGeneralConfigLastChangeTime,
       "openflowGeneralStateLastChangeTime": openflowGeneralStateLastChangeTime,
       "openflowGeneralLogicalSwitchTableSize": openflowGeneralLogicalSwitchTableSize,
       "openflowGeneralGenericTableSize": openflowGeneralGenericTableSize,
       "openflowGeneralConnectionTableSize": openflowGeneralConnectionTableSize,
       "openflowGeneralDiagnosticsTableSize": openflowGeneralDiagnosticsTableSize,
       "openflowGeneralLogTableSize": openflowGeneralLogTableSize,
       "openflowLogicalSwitchList": openflowLogicalSwitchList,
       "openflowLogicalSwitchTable": openflowLogicalSwitchTable,
       "openflowLogicalSwitchEntry": openflowLogicalSwitchEntry,
       "openflowLogicalSwitchName": openflowLogicalSwitchName,
       "openflowLogicalSwitchIndex": openflowLogicalSwitchIndex,
       "openflowLogicalSwitchDescr": openflowLogicalSwitchDescr,
       "openflowLogicalSwitchIdentity": openflowLogicalSwitchIdentity,
       "openflowLogicalSwitchMacAddress": openflowLogicalSwitchMacAddress,
       "openflowLogicalSwitchDpId": openflowLogicalSwitchDpId,
       "openflowLogicalSwitchAssociateCxn": openflowLogicalSwitchAssociateCxn,
       "openflowLogicalSwitchSubrack": openflowLogicalSwitchSubrack,
       "openflowLogicalSwitchSlot": openflowLogicalSwitchSlot,
       "openflowLogicalSwitchGetTracelogs": openflowLogicalSwitchGetTracelogs,
       "openflowLogicalSwitchOfVersion": openflowLogicalSwitchOfVersion,
       "openflowConnectionList": openflowConnectionList,
       "openflowConnectionTable": openflowConnectionTable,
       "openflowConnectionEntry": openflowConnectionEntry,
       "openflowConnectionName": openflowConnectionName,
       "openflowConnectionIndex": openflowConnectionIndex,
       "openflowConnectionDescr": openflowConnectionDescr,
       "openflowConnectionIdentity": openflowConnectionIdentity,
       "openflowConnectionSwitchIdentity": openflowConnectionSwitchIdentity,
       "openflowConnectionIpv4Addr": openflowConnectionIpv4Addr,
       "openflowConnectionTcpPort": openflowConnectionTcpPort,
       "openflowConnectionState": openflowConnectionState,
       "openflowConnectionRole": openflowConnectionRole,
       "openflowConnectionOfVersion": openflowConnectionOfVersion,
       "openflowConnectionSubrack": openflowConnectionSubrack,
       "openflowConnectionSlot": openflowConnectionSlot,
       "openflowGenericList": openflowGenericList,
       "openflowGenericTable": openflowGenericTable,
       "openflowGenericEntry": openflowGenericEntry,
       "openflowGenericIndex": openflowGenericIndex,
       "openflowGenericName": openflowGenericName,
       "openflowGenericSubrack": openflowGenericSubrack,
       "openflowGenericSlot": openflowGenericSlot,
       "openflowGenericCreateOFLS": openflowGenericCreateOFLS,
       "openflowDiagnosticsList": openflowDiagnosticsList,
       "openflowDiagnosticsTable": openflowDiagnosticsTable,
       "openflowDiagnosticsEntry": openflowDiagnosticsEntry,
       "openflowDiagnosticsIndex": openflowDiagnosticsIndex,
       "openflowDiagnosticsName": openflowDiagnosticsName,
       "openflowDiagnosticsIpv4Addr": openflowDiagnosticsIpv4Addr,
       "openflowDiagnosticsTcpPort": openflowDiagnosticsTcpPort,
       "openflowDiagnosticsLogServerType": openflowDiagnosticsLogServerType,
       "openflowDiagnosticsConfigure": openflowDiagnosticsConfigure,
       "openflowDiagnosticsSubrack": openflowDiagnosticsSubrack,
       "openflowLogList": openflowLogList,
       "openflowLogTable": openflowLogTable,
       "openflowLogEntry": openflowLogEntry,
       "openflowLogIndex": openflowLogIndex,
       "openflowLogName": openflowLogName,
       "openflowLogSubrack": openflowLogSubrack,
       "openflowLogCreateOFDiagnostics": openflowLogCreateOFDiagnostics}
)
