# SNMP MIB module (LUM-PW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-PW-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:17 2025
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
 lumPwMIB) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumModules",
    "lumPwMIB")

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
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

lumPwMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 41)
)
if mibBuilder.loadTexts:
    lumPwMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2016-11-30 00:00",
         "2012-12-20 00:00",
         "2011-12-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumPwConfs_ObjectIdentity = ObjectIdentity
lumPwConfs = _LumPwConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 1)
)
_LumPwGroups_ObjectIdentity = ObjectIdentity
lumPwGroups = _LumPwGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 1, 1)
)
_LumPwCompl_ObjectIdentity = ObjectIdentity
lumPwCompl = _LumPwCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 1, 2)
)
_LumPwMIBObjects_ObjectIdentity = ObjectIdentity
lumPwMIBObjects = _LumPwMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2)
)
_PwGeneral_ObjectIdentity = ObjectIdentity
pwGeneral = _PwGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 1)
)
_PwGeneralLastChangeTime_Type = DateAndTime
_PwGeneralLastChangeTime_Object = MibScalar
pwGeneralLastChangeTime = _PwGeneralLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 1, 1),
    _PwGeneralLastChangeTime_Type()
)
pwGeneralLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwGeneralLastChangeTime.setStatus("current")
_PwGeneralStateLastChangeTime_Type = DateAndTime
_PwGeneralStateLastChangeTime_Object = MibScalar
pwGeneralStateLastChangeTime = _PwGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 1, 2),
    _PwGeneralStateLastChangeTime_Type()
)
pwGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwGeneralStateLastChangeTime.setStatus("current")
_PwGeneralPwGenericTableSize_Type = Unsigned32
_PwGeneralPwGenericTableSize_Object = MibScalar
pwGeneralPwGenericTableSize = _PwGeneralPwGenericTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 1, 3),
    _PwGeneralPwGenericTableSize_Type()
)
pwGeneralPwGenericTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwGeneralPwGenericTableSize.setStatus("current")
_PwGeneralPwMplsTableSize_Type = Unsigned32
_PwGeneralPwMplsTableSize_Object = MibScalar
pwGeneralPwMplsTableSize = _PwGeneralPwMplsTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 1, 4),
    _PwGeneralPwMplsTableSize_Type()
)
pwGeneralPwMplsTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwGeneralPwMplsTableSize.setStatus("current")
_PwGeneralPwEnetTableSize_Type = Unsigned32
_PwGeneralPwEnetTableSize_Object = MibScalar
pwGeneralPwEnetTableSize = _PwGeneralPwEnetTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 1, 5),
    _PwGeneralPwEnetTableSize_Type()
)
pwGeneralPwEnetTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwGeneralPwEnetTableSize.setStatus("current")
_PwGeneralPwMspwTableSize_Type = Unsigned32
_PwGeneralPwMspwTableSize_Object = MibScalar
pwGeneralPwMspwTableSize = _PwGeneralPwMspwTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 1, 6),
    _PwGeneralPwMspwTableSize_Type()
)
pwGeneralPwMspwTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwGeneralPwMspwTableSize.setStatus("current")
_PwGenericList_ObjectIdentity = ObjectIdentity
pwGenericList = _PwGenericList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 2)
)
_PwGenericTable_Object = MibTable
pwGenericTable = _PwGenericTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 2, 1)
)
if mibBuilder.loadTexts:
    pwGenericTable.setStatus("current")
_PwGenericEntry_Object = MibTableRow
pwGenericEntry = _PwGenericEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 2, 1, 1)
)
pwGenericEntry.setIndexNames(
    (0, "LUM-PW-MIB", "pwGenericIndex"),
)
if mibBuilder.loadTexts:
    pwGenericEntry.setStatus("current")


class _PwGenericIndex_Type(Unsigned32):
    """Custom type pwGenericIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PwGenericIndex_Type.__name__ = "Unsigned32"
_PwGenericIndex_Object = MibTableColumn
pwGenericIndex = _PwGenericIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 2, 1, 1, 1),
    _PwGenericIndex_Type()
)
pwGenericIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwGenericIndex.setStatus("current")
_PwGenericName_Type = MgmtNameString
_PwGenericName_Object = MibTableColumn
pwGenericName = _PwGenericName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 2, 1, 1, 2),
    _PwGenericName_Type()
)
pwGenericName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwGenericName.setStatus("current")


class _PwGenericIdentifier_Type(DisplayString):
    """Custom type pwGenericIdentifier based on DisplayString"""
    defaultValue = OctetString("")


_PwGenericIdentifier_Type.__name__ = "DisplayString"
_PwGenericIdentifier_Object = MibTableColumn
pwGenericIdentifier = _PwGenericIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 2, 1, 1, 3),
    _PwGenericIdentifier_Type()
)
pwGenericIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwGenericIdentifier.setStatus("current")


class _PwGenericInternalReference_Type(Unsigned32):
    """Custom type pwGenericInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PwGenericInternalReference_Type.__name__ = "Unsigned32"
_PwGenericInternalReference_Object = MibTableColumn
pwGenericInternalReference = _PwGenericInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 2, 1, 1, 4),
    _PwGenericInternalReference_Type()
)
pwGenericInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwGenericInternalReference.setStatus("current")


class _PwGenericDescr_Type(DisplayString):
    """Custom type pwGenericDescr based on DisplayString"""
    defaultValue = OctetString("")


_PwGenericDescr_Type.__name__ = "DisplayString"
_PwGenericDescr_Object = MibTableColumn
pwGenericDescr = _PwGenericDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 2, 1, 1, 5),
    _PwGenericDescr_Type()
)
pwGenericDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwGenericDescr.setStatus("current")


class _PwGenericOutboundLabel_Type(MplsLabel):
    """Custom type pwGenericOutboundLabel based on MplsLabel"""
    defaultValue = 0


_PwGenericOutboundLabel_Type.__name__ = "MplsLabel"
_PwGenericOutboundLabel_Object = MibTableColumn
pwGenericOutboundLabel = _PwGenericOutboundLabel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 2, 1, 1, 6),
    _PwGenericOutboundLabel_Type()
)
pwGenericOutboundLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwGenericOutboundLabel.setStatus("current")


class _PwGenericInboundLabel_Type(MplsLabel):
    """Custom type pwGenericInboundLabel based on MplsLabel"""
    defaultValue = 0


_PwGenericInboundLabel_Type.__name__ = "MplsLabel"
_PwGenericInboundLabel_Object = MibTableColumn
pwGenericInboundLabel = _PwGenericInboundLabel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 2, 1, 1, 7),
    _PwGenericInboundLabel_Type()
)
pwGenericInboundLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwGenericInboundLabel.setStatus("current")


class _PwGenericInPackets_Type(Counter64):
    """Custom type pwGenericInPackets based on Counter64"""
    defaultValue = 0


_PwGenericInPackets_Type.__name__ = "Counter64"
_PwGenericInPackets_Object = MibTableColumn
pwGenericInPackets = _PwGenericInPackets_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 2, 1, 1, 8),
    _PwGenericInPackets_Type()
)
pwGenericInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwGenericInPackets.setStatus("current")


class _PwGenericInBytes_Type(Counter64):
    """Custom type pwGenericInBytes based on Counter64"""
    defaultValue = 0


_PwGenericInBytes_Type.__name__ = "Counter64"
_PwGenericInBytes_Object = MibTableColumn
pwGenericInBytes = _PwGenericInBytes_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 2, 1, 1, 9),
    _PwGenericInBytes_Type()
)
pwGenericInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwGenericInBytes.setStatus("current")


class _PwGenericOutPackets_Type(Counter64):
    """Custom type pwGenericOutPackets based on Counter64"""
    defaultValue = 0


_PwGenericOutPackets_Type.__name__ = "Counter64"
_PwGenericOutPackets_Object = MibTableColumn
pwGenericOutPackets = _PwGenericOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 2, 1, 1, 10),
    _PwGenericOutPackets_Type()
)
pwGenericOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwGenericOutPackets.setStatus("current")


class _PwGenericOutBytes_Type(Counter64):
    """Custom type pwGenericOutBytes based on Counter64"""
    defaultValue = 0


_PwGenericOutBytes_Type.__name__ = "Counter64"
_PwGenericOutBytes_Object = MibTableColumn
pwGenericOutBytes = _PwGenericOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 2, 1, 1, 11),
    _PwGenericOutBytes_Type()
)
pwGenericOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwGenericOutBytes.setStatus("current")


class _PwGenericResetCont_Type(Integer32):
    """Custom type pwGenericResetCont based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_PwGenericResetCont_Type.__name__ = "Integer32"
_PwGenericResetCont_Object = MibTableColumn
pwGenericResetCont = _PwGenericResetCont_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 2, 1, 1, 12),
    _PwGenericResetCont_Type()
)
pwGenericResetCont.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwGenericResetCont.setStatus("current")
_PwGenericRowStatus_Type = RowStatus
_PwGenericRowStatus_Object = MibTableColumn
pwGenericRowStatus = _PwGenericRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 2, 1, 1, 13),
    _PwGenericRowStatus_Type()
)
pwGenericRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwGenericRowStatus.setStatus("current")


class _PwGenericPwType_Type(Integer32):
    """Custom type pwGenericPwType based on Integer32"""
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
          ("multiSeg", 2))
    )


_PwGenericPwType_Type.__name__ = "Integer32"
_PwGenericPwType_Object = MibTableColumn
pwGenericPwType = _PwGenericPwType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 2, 1, 1, 14),
    _PwGenericPwType_Type()
)
pwGenericPwType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwGenericPwType.setStatus("current")


class _PwGenericTrafficClass_Type(Integer32):
    """Custom type pwGenericTrafficClass based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_PwGenericTrafficClass_Type.__name__ = "Integer32"
_PwGenericTrafficClass_Object = MibTableColumn
pwGenericTrafficClass = _PwGenericTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 2, 1, 1, 15),
    _PwGenericTrafficClass_Type()
)
pwGenericTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwGenericTrafficClass.setStatus("current")


class _PwGenericReservedBW_Type(Unsigned32):
    """Custom type pwGenericReservedBW based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_PwGenericReservedBW_Type.__name__ = "Unsigned32"
_PwGenericReservedBW_Object = MibTableColumn
pwGenericReservedBW = _PwGenericReservedBW_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 2, 1, 1, 16),
    _PwGenericReservedBW_Type()
)
pwGenericReservedBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwGenericReservedBW.setStatus("current")


class _PwGenericPwNumber_Type(Unsigned32):
    """Custom type pwGenericPwNumber based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_PwGenericPwNumber_Type.__name__ = "Unsigned32"
_PwGenericPwNumber_Object = MibTableColumn
pwGenericPwNumber = _PwGenericPwNumber_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 2, 1, 1, 17),
    _PwGenericPwNumber_Type()
)
pwGenericPwNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwGenericPwNumber.setStatus("current")


class _PwGenericConfigurationSet_Type(Integer32):
    """Custom type pwGenericConfigurationSet based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_PwGenericConfigurationSet_Type.__name__ = "Integer32"
_PwGenericConfigurationSet_Object = MibTableColumn
pwGenericConfigurationSet = _PwGenericConfigurationSet_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 2, 1, 1, 18),
    _PwGenericConfigurationSet_Type()
)
pwGenericConfigurationSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwGenericConfigurationSet.setStatus("current")


class _PwGenericFlowLabel_Type(Integer32):
    """Custom type pwGenericFlowLabel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_PwGenericFlowLabel_Type.__name__ = "Integer32"
_PwGenericFlowLabel_Object = MibTableColumn
pwGenericFlowLabel = _PwGenericFlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 2, 1, 1, 19),
    _PwGenericFlowLabel_Type()
)
pwGenericFlowLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwGenericFlowLabel.setStatus("current")
_PwMplsList_ObjectIdentity = ObjectIdentity
pwMplsList = _PwMplsList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 3)
)
_PwMplsTable_Object = MibTable
pwMplsTable = _PwMplsTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 3, 1)
)
if mibBuilder.loadTexts:
    pwMplsTable.setStatus("current")
_PwMplsEntry_Object = MibTableRow
pwMplsEntry = _PwMplsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 3, 1, 1)
)
pwMplsEntry.setIndexNames(
    (0, "LUM-PW-MIB", "pwMplsIndex"),
)
if mibBuilder.loadTexts:
    pwMplsEntry.setStatus("current")


class _PwMplsIndex_Type(Unsigned32):
    """Custom type pwMplsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PwMplsIndex_Type.__name__ = "Unsigned32"
_PwMplsIndex_Object = MibTableColumn
pwMplsIndex = _PwMplsIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 3, 1, 1, 1),
    _PwMplsIndex_Type()
)
pwMplsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwMplsIndex.setStatus("current")
_PwMplsName_Type = MgmtNameString
_PwMplsName_Object = MibTableColumn
pwMplsName = _PwMplsName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 3, 1, 1, 2),
    _PwMplsName_Type()
)
pwMplsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwMplsName.setStatus("current")


class _PwMplsIdentifier_Type(DisplayString):
    """Custom type pwMplsIdentifier based on DisplayString"""
    defaultValue = OctetString("")


_PwMplsIdentifier_Type.__name__ = "DisplayString"
_PwMplsIdentifier_Object = MibTableColumn
pwMplsIdentifier = _PwMplsIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 3, 1, 1, 3),
    _PwMplsIdentifier_Type()
)
pwMplsIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwMplsIdentifier.setStatus("current")


class _PwMplsInternalReference_Type(Unsigned32):
    """Custom type pwMplsInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PwMplsInternalReference_Type.__name__ = "Unsigned32"
_PwMplsInternalReference_Object = MibTableColumn
pwMplsInternalReference = _PwMplsInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 3, 1, 1, 4),
    _PwMplsInternalReference_Type()
)
pwMplsInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwMplsInternalReference.setStatus("current")


class _PwMplsOutboundTunnelId_Type(DisplayString):
    """Custom type pwMplsOutboundTunnelId based on DisplayString"""
    defaultValue = OctetString("")


_PwMplsOutboundTunnelId_Type.__name__ = "DisplayString"
_PwMplsOutboundTunnelId_Object = MibTableColumn
pwMplsOutboundTunnelId = _PwMplsOutboundTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 3, 1, 1, 5),
    _PwMplsOutboundTunnelId_Type()
)
pwMplsOutboundTunnelId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwMplsOutboundTunnelId.setStatus("current")
_PwMplsAssociateTunnel_Type = CommandString
_PwMplsAssociateTunnel_Object = MibTableColumn
pwMplsAssociateTunnel = _PwMplsAssociateTunnel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 3, 1, 1, 6),
    _PwMplsAssociateTunnel_Type()
)
pwMplsAssociateTunnel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwMplsAssociateTunnel.setStatus("deprecated")
_PwMplsRowStatus_Type = RowStatus
_PwMplsRowStatus_Object = MibTableColumn
pwMplsRowStatus = _PwMplsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 3, 1, 1, 7),
    _PwMplsRowStatus_Type()
)
pwMplsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwMplsRowStatus.setStatus("current")
_PwEnetList_ObjectIdentity = ObjectIdentity
pwEnetList = _PwEnetList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 4)
)
_PwEnetTable_Object = MibTable
pwEnetTable = _PwEnetTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 4, 1)
)
if mibBuilder.loadTexts:
    pwEnetTable.setStatus("current")
_PwEnetEntry_Object = MibTableRow
pwEnetEntry = _PwEnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 4, 1, 1)
)
pwEnetEntry.setIndexNames(
    (0, "LUM-PW-MIB", "pwEnetIndex"),
)
if mibBuilder.loadTexts:
    pwEnetEntry.setStatus("current")


class _PwEnetIndex_Type(Unsigned32):
    """Custom type pwEnetIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PwEnetIndex_Type.__name__ = "Unsigned32"
_PwEnetIndex_Object = MibTableColumn
pwEnetIndex = _PwEnetIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 4, 1, 1, 1),
    _PwEnetIndex_Type()
)
pwEnetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwEnetIndex.setStatus("current")
_PwEnetName_Type = MgmtNameString
_PwEnetName_Object = MibTableColumn
pwEnetName = _PwEnetName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 4, 1, 1, 2),
    _PwEnetName_Type()
)
pwEnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwEnetName.setStatus("current")


class _PwEnetIdentifier_Type(DisplayString):
    """Custom type pwEnetIdentifier based on DisplayString"""
    defaultValue = OctetString("")


_PwEnetIdentifier_Type.__name__ = "DisplayString"
_PwEnetIdentifier_Object = MibTableColumn
pwEnetIdentifier = _PwEnetIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 4, 1, 1, 3),
    _PwEnetIdentifier_Type()
)
pwEnetIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwEnetIdentifier.setStatus("current")


class _PwEnetInternalReference_Type(Unsigned32):
    """Custom type pwEnetInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PwEnetInternalReference_Type.__name__ = "Unsigned32"
_PwEnetInternalReference_Object = MibTableColumn
pwEnetInternalReference = _PwEnetInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 4, 1, 1, 4),
    _PwEnetInternalReference_Type()
)
pwEnetInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwEnetInternalReference.setStatus("current")


class _PwEnetPortVlan_Type(Unsigned32):
    """Custom type pwEnetPortVlan based on Unsigned32"""
    defaultValue = 4095

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_PwEnetPortVlan_Type.__name__ = "Unsigned32"
_PwEnetPortVlan_Object = MibTableColumn
pwEnetPortVlan = _PwEnetPortVlan_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 4, 1, 1, 5),
    _PwEnetPortVlan_Type()
)
pwEnetPortVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwEnetPortVlan.setStatus("current")


class _PwEnetPortIndex_Type(Unsigned32):
    """Custom type pwEnetPortIndex based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PwEnetPortIndex_Type.__name__ = "Unsigned32"
_PwEnetPortIndex_Object = MibTableColumn
pwEnetPortIndex = _PwEnetPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 4, 1, 1, 6),
    _PwEnetPortIndex_Type()
)
pwEnetPortIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwEnetPortIndex.setStatus("current")


class _PwEnetPortName_Type(DisplayString):
    """Custom type pwEnetPortName based on DisplayString"""
    defaultValue = OctetString("")


_PwEnetPortName_Type.__name__ = "DisplayString"
_PwEnetPortName_Object = MibTableColumn
pwEnetPortName = _PwEnetPortName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 4, 1, 1, 7),
    _PwEnetPortName_Type()
)
pwEnetPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwEnetPortName.setStatus("current")


class _PwEnetTpid_Type(Integer32):
    """Custom type pwEnetTpid based on Integer32"""
    defaultValue = 3

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
        *(("undefined", 0),
          ("anyTag", 1),
          ("qTag0x8100", 2),
          ("sTag0x88a8", 3))
    )


_PwEnetTpid_Type.__name__ = "Integer32"
_PwEnetTpid_Object = MibTableColumn
pwEnetTpid = _PwEnetTpid_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 4, 1, 1, 8),
    _PwEnetTpid_Type()
)
pwEnetTpid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwEnetTpid.setStatus("current")
_PwEnetRowStatus_Type = RowStatus
_PwEnetRowStatus_Object = MibTableColumn
pwEnetRowStatus = _PwEnetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 4, 1, 1, 9),
    _PwEnetRowStatus_Type()
)
pwEnetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwEnetRowStatus.setStatus("current")


class _PwEnetClassification_Type(DisplayString):
    """Custom type pwEnetClassification based on DisplayString"""
    defaultValue = OctetString("")


_PwEnetClassification_Type.__name__ = "DisplayString"
_PwEnetClassification_Object = MibTableColumn
pwEnetClassification = _PwEnetClassification_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 4, 1, 1, 10),
    _PwEnetClassification_Type()
)
pwEnetClassification.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwEnetClassification.setStatus("current")


class _PwEnetFecType_Type(Integer32):
    """Custom type pwEnetFecType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port", 0),
          ("portVlan", 1),
          ("classification", 2))
    )


_PwEnetFecType_Type.__name__ = "Integer32"
_PwEnetFecType_Object = MibTableColumn
pwEnetFecType = _PwEnetFecType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 4, 1, 1, 11),
    _PwEnetFecType_Type()
)
pwEnetFecType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwEnetFecType.setStatus("current")


class _PwEnetSdTagVlanActionIngress_Type(Integer32):
    """Custom type pwEnetSdTagVlanActionIngress based on Integer32"""
    defaultValue = 0

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
        *(("noAction", 0),
          ("swap", 1),
          ("push", 2),
          ("pop", 3))
    )


_PwEnetSdTagVlanActionIngress_Type.__name__ = "Integer32"
_PwEnetSdTagVlanActionIngress_Object = MibTableColumn
pwEnetSdTagVlanActionIngress = _PwEnetSdTagVlanActionIngress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 4, 1, 1, 12),
    _PwEnetSdTagVlanActionIngress_Type()
)
pwEnetSdTagVlanActionIngress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwEnetSdTagVlanActionIngress.setStatus("current")


class _PwEnetSdTagVlanIngress_Type(Unsigned32):
    """Custom type pwEnetSdTagVlanIngress based on Unsigned32"""
    defaultValue = 4095

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_PwEnetSdTagVlanIngress_Type.__name__ = "Unsigned32"
_PwEnetSdTagVlanIngress_Object = MibTableColumn
pwEnetSdTagVlanIngress = _PwEnetSdTagVlanIngress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 4, 1, 1, 13),
    _PwEnetSdTagVlanIngress_Type()
)
pwEnetSdTagVlanIngress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwEnetSdTagVlanIngress.setStatus("current")


class _PwEnetSdTagVlanActionEgress_Type(Integer32):
    """Custom type pwEnetSdTagVlanActionEgress based on Integer32"""
    defaultValue = 0

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
        *(("noAction", 0),
          ("swap", 1),
          ("push", 2),
          ("pop", 3))
    )


_PwEnetSdTagVlanActionEgress_Type.__name__ = "Integer32"
_PwEnetSdTagVlanActionEgress_Object = MibTableColumn
pwEnetSdTagVlanActionEgress = _PwEnetSdTagVlanActionEgress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 4, 1, 1, 14),
    _PwEnetSdTagVlanActionEgress_Type()
)
pwEnetSdTagVlanActionEgress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwEnetSdTagVlanActionEgress.setStatus("current")


class _PwEnetSdTagVlanEgress_Type(Unsigned32):
    """Custom type pwEnetSdTagVlanEgress based on Unsigned32"""
    defaultValue = 4095

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_PwEnetSdTagVlanEgress_Type.__name__ = "Unsigned32"
_PwEnetSdTagVlanEgress_Object = MibTableColumn
pwEnetSdTagVlanEgress = _PwEnetSdTagVlanEgress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 4, 1, 1, 15),
    _PwEnetSdTagVlanEgress_Type()
)
pwEnetSdTagVlanEgress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwEnetSdTagVlanEgress.setStatus("current")


class _PwEnetOpMode_Type(Integer32):
    """Custom type pwEnetOpMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transparent", 0),
          ("raw", 1),
          ("tagged", 2))
    )


_PwEnetOpMode_Type.__name__ = "Integer32"
_PwEnetOpMode_Object = MibTableColumn
pwEnetOpMode = _PwEnetOpMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 4, 1, 1, 16),
    _PwEnetOpMode_Type()
)
pwEnetOpMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwEnetOpMode.setStatus("current")


class _PwEnetIfNo_Type(PortNumber):
    """Custom type pwEnetIfNo based on PortNumber"""
    defaultValue = 0


_PwEnetIfNo_Type.__name__ = "PortNumber"
_PwEnetIfNo_Object = MibTableColumn
pwEnetIfNo = _PwEnetIfNo_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 4, 1, 1, 17),
    _PwEnetIfNo_Type()
)
pwEnetIfNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwEnetIfNo.setStatus("current")


class _PwEnetTxPort_Type(PortNumber):
    """Custom type pwEnetTxPort based on PortNumber"""
    defaultValue = 0


_PwEnetTxPort_Type.__name__ = "PortNumber"
_PwEnetTxPort_Object = MibTableColumn
pwEnetTxPort = _PwEnetTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 4, 1, 1, 18),
    _PwEnetTxPort_Type()
)
pwEnetTxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwEnetTxPort.setStatus("current")


class _PwEnetInterfaceName_Type(DisplayString):
    """Custom type pwEnetInterfaceName based on DisplayString"""
    defaultValue = OctetString(" ")


_PwEnetInterfaceName_Type.__name__ = "DisplayString"
_PwEnetInterfaceName_Object = MibTableColumn
pwEnetInterfaceName = _PwEnetInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 4, 1, 1, 19),
    _PwEnetInterfaceName_Type()
)
pwEnetInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwEnetInterfaceName.setStatus("current")
_PwMspwList_ObjectIdentity = ObjectIdentity
pwMspwList = _PwMspwList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 5)
)
_PwMspwTable_Object = MibTable
pwMspwTable = _PwMspwTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 5, 1)
)
if mibBuilder.loadTexts:
    pwMspwTable.setStatus("current")
_PwMspwEntry_Object = MibTableRow
pwMspwEntry = _PwMspwEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 5, 1, 1)
)
pwMspwEntry.setIndexNames(
    (0, "LUM-PW-MIB", "pwMspwIndex"),
)
if mibBuilder.loadTexts:
    pwMspwEntry.setStatus("current")


class _PwMspwIndex_Type(Unsigned32):
    """Custom type pwMspwIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PwMspwIndex_Type.__name__ = "Unsigned32"
_PwMspwIndex_Object = MibTableColumn
pwMspwIndex = _PwMspwIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 5, 1, 1, 1),
    _PwMspwIndex_Type()
)
pwMspwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwMspwIndex.setStatus("current")
_PwMspwName_Type = MgmtNameString
_PwMspwName_Object = MibTableColumn
pwMspwName = _PwMspwName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 5, 1, 1, 2),
    _PwMspwName_Type()
)
pwMspwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwMspwName.setStatus("current")
_PwMspwIdentifier_Type = DisplayString
_PwMspwIdentifier_Object = MibTableColumn
pwMspwIdentifier = _PwMspwIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 5, 1, 1, 3),
    _PwMspwIdentifier_Type()
)
pwMspwIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwMspwIdentifier.setStatus("current")


class _PwMspwInternalReference_Type(Unsigned32):
    """Custom type pwMspwInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PwMspwInternalReference_Type.__name__ = "Unsigned32"
_PwMspwInternalReference_Object = MibTableColumn
pwMspwInternalReference = _PwMspwInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 5, 1, 1, 4),
    _PwMspwInternalReference_Type()
)
pwMspwInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwMspwInternalReference.setStatus("current")
_PwMspwEastInboundLabel_Type = MplsLabel
_PwMspwEastInboundLabel_Object = MibTableColumn
pwMspwEastInboundLabel = _PwMspwEastInboundLabel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 5, 1, 1, 5),
    _PwMspwEastInboundLabel_Type()
)
pwMspwEastInboundLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwMspwEastInboundLabel.setStatus("current")
_PwMspwEastOutboundLabel_Type = MplsLabel
_PwMspwEastOutboundLabel_Object = MibTableColumn
pwMspwEastOutboundLabel = _PwMspwEastOutboundLabel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 5, 1, 1, 6),
    _PwMspwEastOutboundLabel_Type()
)
pwMspwEastOutboundLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwMspwEastOutboundLabel.setStatus("current")
_PwMspwEastOutboundTunnelId_Type = DisplayString
_PwMspwEastOutboundTunnelId_Object = MibTableColumn
pwMspwEastOutboundTunnelId = _PwMspwEastOutboundTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 5, 1, 1, 7),
    _PwMspwEastOutboundTunnelId_Type()
)
pwMspwEastOutboundTunnelId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwMspwEastOutboundTunnelId.setStatus("current")
_PwMspwWestInboundLabel_Type = MplsLabel
_PwMspwWestInboundLabel_Object = MibTableColumn
pwMspwWestInboundLabel = _PwMspwWestInboundLabel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 5, 1, 1, 8),
    _PwMspwWestInboundLabel_Type()
)
pwMspwWestInboundLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwMspwWestInboundLabel.setStatus("current")
_PwMspwWestOutboundLabel_Type = MplsLabel
_PwMspwWestOutboundLabel_Object = MibTableColumn
pwMspwWestOutboundLabel = _PwMspwWestOutboundLabel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 5, 1, 1, 9),
    _PwMspwWestOutboundLabel_Type()
)
pwMspwWestOutboundLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwMspwWestOutboundLabel.setStatus("current")
_PwMspwWestOutboundTunnelId_Type = DisplayString
_PwMspwWestOutboundTunnelId_Object = MibTableColumn
pwMspwWestOutboundTunnelId = _PwMspwWestOutboundTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 5, 1, 1, 10),
    _PwMspwWestOutboundTunnelId_Type()
)
pwMspwWestOutboundTunnelId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwMspwWestOutboundTunnelId.setStatus("current")
_PwMspwRowStatus_Type = RowStatus
_PwMspwRowStatus_Object = MibTableColumn
pwMspwRowStatus = _PwMspwRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 2, 5, 1, 1, 11),
    _PwMspwRowStatus_Type()
)
pwMspwRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwMspwRowStatus.setStatus("current")

# Managed Objects groups

pwGeneralGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 1, 1, 1)
)
pwGeneralGroupV1.setObjects(
      *(("LUM-PW-MIB", "pwGeneralLastChangeTime"),
        ("LUM-PW-MIB", "pwGeneralStateLastChangeTime"),
        ("LUM-PW-MIB", "pwGeneralPwGenericTableSize"),
        ("LUM-PW-MIB", "pwGeneralPwMplsTableSize"),
        ("LUM-PW-MIB", "pwGeneralPwEnetTableSize"))
)
if mibBuilder.loadTexts:
    pwGeneralGroupV1.setStatus("deprecated")

pwGenericGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 1, 1, 2)
)
pwGenericGroupV1.setObjects(
      *(("LUM-PW-MIB", "pwGenericIndex"),
        ("LUM-PW-MIB", "pwGenericName"),
        ("LUM-PW-MIB", "pwGenericIdentifier"),
        ("LUM-PW-MIB", "pwGenericInternalReference"),
        ("LUM-PW-MIB", "pwGenericDescr"),
        ("LUM-PW-MIB", "pwGenericOutboundLabel"),
        ("LUM-PW-MIB", "pwGenericInboundLabel"),
        ("LUM-PW-MIB", "pwGenericInPackets"),
        ("LUM-PW-MIB", "pwGenericInBytes"),
        ("LUM-PW-MIB", "pwGenericOutPackets"),
        ("LUM-PW-MIB", "pwGenericOutBytes"),
        ("LUM-PW-MIB", "pwGenericResetCont"),
        ("LUM-PW-MIB", "pwGenericRowStatus"))
)
if mibBuilder.loadTexts:
    pwGenericGroupV1.setStatus("deprecated")

pwMplsGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 1, 1, 3)
)
pwMplsGroupV1.setObjects(
      *(("LUM-PW-MIB", "pwMplsIndex"),
        ("LUM-PW-MIB", "pwMplsName"),
        ("LUM-PW-MIB", "pwMplsIdentifier"),
        ("LUM-PW-MIB", "pwMplsInternalReference"),
        ("LUM-PW-MIB", "pwMplsOutboundTunnelId"),
        ("LUM-PW-MIB", "pwMplsAssociateTunnel"))
)
if mibBuilder.loadTexts:
    pwMplsGroupV1.setStatus("deprecated")

pwEnetGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 1, 1, 4)
)
pwEnetGroupV1.setObjects(
      *(("LUM-PW-MIB", "pwEnetIndex"),
        ("LUM-PW-MIB", "pwEnetName"),
        ("LUM-PW-MIB", "pwEnetIdentifier"),
        ("LUM-PW-MIB", "pwEnetInternalReference"),
        ("LUM-PW-MIB", "pwEnetPortVlan"),
        ("LUM-PW-MIB", "pwEnetPortIndex"),
        ("LUM-PW-MIB", "pwEnetPortName"),
        ("LUM-PW-MIB", "pwEnetTpid"),
        ("LUM-PW-MIB", "pwEnetRowStatus"))
)
if mibBuilder.loadTexts:
    pwEnetGroupV1.setStatus("deprecated")

pwEnetGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 1, 1, 5)
)
pwEnetGroupV2.setObjects(
      *(("LUM-PW-MIB", "pwEnetIndex"),
        ("LUM-PW-MIB", "pwEnetName"),
        ("LUM-PW-MIB", "pwEnetIdentifier"),
        ("LUM-PW-MIB", "pwEnetInternalReference"),
        ("LUM-PW-MIB", "pwEnetPortVlan"),
        ("LUM-PW-MIB", "pwEnetPortIndex"),
        ("LUM-PW-MIB", "pwEnetPortName"),
        ("LUM-PW-MIB", "pwEnetTpid"),
        ("LUM-PW-MIB", "pwEnetRowStatus"),
        ("LUM-PW-MIB", "pwEnetClassification"),
        ("LUM-PW-MIB", "pwEnetFecType"),
        ("LUM-PW-MIB", "pwEnetSdTagVlanActionIngress"),
        ("LUM-PW-MIB", "pwEnetSdTagVlanIngress"),
        ("LUM-PW-MIB", "pwEnetSdTagVlanActionEgress"),
        ("LUM-PW-MIB", "pwEnetSdTagVlanEgress"),
        ("LUM-PW-MIB", "pwEnetOpMode"))
)
if mibBuilder.loadTexts:
    pwEnetGroupV2.setStatus("deprecated")

pwGeneralGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 1, 1, 6)
)
pwGeneralGroupV2.setObjects(
      *(("LUM-PW-MIB", "pwGeneralLastChangeTime"),
        ("LUM-PW-MIB", "pwGeneralStateLastChangeTime"),
        ("LUM-PW-MIB", "pwGeneralPwGenericTableSize"),
        ("LUM-PW-MIB", "pwGeneralPwMplsTableSize"),
        ("LUM-PW-MIB", "pwGeneralPwEnetTableSize"),
        ("LUM-PW-MIB", "pwGeneralPwMspwTableSize"))
)
if mibBuilder.loadTexts:
    pwGeneralGroupV2.setStatus("current")

pwMspwGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 1, 1, 7)
)
pwMspwGroupV1.setObjects(
      *(("LUM-PW-MIB", "pwMspwIndex"),
        ("LUM-PW-MIB", "pwMspwName"),
        ("LUM-PW-MIB", "pwMspwIdentifier"),
        ("LUM-PW-MIB", "pwMspwInternalReference"),
        ("LUM-PW-MIB", "pwMspwEastInboundLabel"),
        ("LUM-PW-MIB", "pwMspwEastOutboundLabel"),
        ("LUM-PW-MIB", "pwMspwEastOutboundTunnelId"),
        ("LUM-PW-MIB", "pwMspwWestInboundLabel"),
        ("LUM-PW-MIB", "pwMspwWestOutboundLabel"),
        ("LUM-PW-MIB", "pwMspwWestOutboundTunnelId"),
        ("LUM-PW-MIB", "pwMspwRowStatus"))
)
if mibBuilder.loadTexts:
    pwMspwGroupV1.setStatus("current")

pwGenericGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 1, 1, 8)
)
pwGenericGroupV2.setObjects(
      *(("LUM-PW-MIB", "pwGenericIndex"),
        ("LUM-PW-MIB", "pwGenericName"),
        ("LUM-PW-MIB", "pwGenericIdentifier"),
        ("LUM-PW-MIB", "pwGenericInternalReference"),
        ("LUM-PW-MIB", "pwGenericDescr"),
        ("LUM-PW-MIB", "pwGenericOutboundLabel"),
        ("LUM-PW-MIB", "pwGenericInboundLabel"),
        ("LUM-PW-MIB", "pwGenericInPackets"),
        ("LUM-PW-MIB", "pwGenericInBytes"),
        ("LUM-PW-MIB", "pwGenericOutPackets"),
        ("LUM-PW-MIB", "pwGenericOutBytes"),
        ("LUM-PW-MIB", "pwGenericResetCont"),
        ("LUM-PW-MIB", "pwGenericRowStatus"),
        ("LUM-PW-MIB", "pwGenericPwType"),
        ("LUM-PW-MIB", "pwGenericTrafficClass"),
        ("LUM-PW-MIB", "pwGenericReservedBW"))
)
if mibBuilder.loadTexts:
    pwGenericGroupV2.setStatus("deprecated")

pwEnetGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 1, 1, 9)
)
pwEnetGroupV3.setObjects(
      *(("LUM-PW-MIB", "pwEnetIndex"),
        ("LUM-PW-MIB", "pwEnetName"),
        ("LUM-PW-MIB", "pwEnetIdentifier"),
        ("LUM-PW-MIB", "pwEnetInternalReference"),
        ("LUM-PW-MIB", "pwEnetPortVlan"),
        ("LUM-PW-MIB", "pwEnetPortIndex"),
        ("LUM-PW-MIB", "pwEnetPortName"),
        ("LUM-PW-MIB", "pwEnetTpid"),
        ("LUM-PW-MIB", "pwEnetRowStatus"),
        ("LUM-PW-MIB", "pwEnetClassification"),
        ("LUM-PW-MIB", "pwEnetFecType"),
        ("LUM-PW-MIB", "pwEnetSdTagVlanActionIngress"),
        ("LUM-PW-MIB", "pwEnetSdTagVlanIngress"),
        ("LUM-PW-MIB", "pwEnetSdTagVlanActionEgress"),
        ("LUM-PW-MIB", "pwEnetSdTagVlanEgress"),
        ("LUM-PW-MIB", "pwEnetOpMode"),
        ("LUM-PW-MIB", "pwEnetIfNo"),
        ("LUM-PW-MIB", "pwEnetTxPort"),
        ("LUM-PW-MIB", "pwEnetInterfaceName"))
)
if mibBuilder.loadTexts:
    pwEnetGroupV3.setStatus("current")

pwGenericGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 1, 1, 10)
)
pwGenericGroupV3.setObjects(
      *(("LUM-PW-MIB", "pwGenericIndex"),
        ("LUM-PW-MIB", "pwGenericName"),
        ("LUM-PW-MIB", "pwGenericIdentifier"),
        ("LUM-PW-MIB", "pwGenericInternalReference"),
        ("LUM-PW-MIB", "pwGenericDescr"),
        ("LUM-PW-MIB", "pwGenericOutboundLabel"),
        ("LUM-PW-MIB", "pwGenericInboundLabel"),
        ("LUM-PW-MIB", "pwGenericInPackets"),
        ("LUM-PW-MIB", "pwGenericInBytes"),
        ("LUM-PW-MIB", "pwGenericOutPackets"),
        ("LUM-PW-MIB", "pwGenericOutBytes"),
        ("LUM-PW-MIB", "pwGenericResetCont"),
        ("LUM-PW-MIB", "pwGenericRowStatus"),
        ("LUM-PW-MIB", "pwGenericPwType"),
        ("LUM-PW-MIB", "pwGenericTrafficClass"),
        ("LUM-PW-MIB", "pwGenericReservedBW"),
        ("LUM-PW-MIB", "pwGenericPwNumber"),
        ("LUM-PW-MIB", "pwGenericConfigurationSet"),
        ("LUM-PW-MIB", "pwGenericFlowLabel"))
)
if mibBuilder.loadTexts:
    pwGenericGroupV3.setStatus("current")

pwMplsGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 1, 1, 11)
)
pwMplsGroupV2.setObjects(
      *(("LUM-PW-MIB", "pwMplsIndex"),
        ("LUM-PW-MIB", "pwMplsName"),
        ("LUM-PW-MIB", "pwMplsIdentifier"),
        ("LUM-PW-MIB", "pwMplsInternalReference"),
        ("LUM-PW-MIB", "pwMplsOutboundTunnelId"))
)
if mibBuilder.loadTexts:
    pwMplsGroupV2.setStatus("deprecated")

pwMplsGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 1, 1, 12)
)
pwMplsGroupV3.setObjects(
      *(("LUM-PW-MIB", "pwMplsIndex"),
        ("LUM-PW-MIB", "pwMplsName"),
        ("LUM-PW-MIB", "pwMplsIdentifier"),
        ("LUM-PW-MIB", "pwMplsInternalReference"),
        ("LUM-PW-MIB", "pwMplsOutboundTunnelId"),
        ("LUM-PW-MIB", "pwMplsRowStatus"))
)
if mibBuilder.loadTexts:
    pwMplsGroupV3.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumPwBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 1, 2, 1)
)
lumPwBasicComplV1.setObjects(
      *(("LUM-PW-MIB", "pwGeneralGroupV1"),
        ("LUM-PW-MIB", "pwGenericGroupV1"),
        ("LUM-PW-MIB", "pwMplsGroupV1"),
        ("LUM-PW-MIB", "pwEnetGroupV1"))
)
if mibBuilder.loadTexts:
    lumPwBasicComplV1.setStatus(
        "deprecated"
    )

lumPwBasicComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 1, 2, 2)
)
lumPwBasicComplV2.setObjects(
      *(("LUM-PW-MIB", "pwGeneralGroupV2"),
        ("LUM-PW-MIB", "pwGenericGroupV2"),
        ("LUM-PW-MIB", "pwMplsGroupV1"),
        ("LUM-PW-MIB", "pwEnetGroupV2"),
        ("LUM-PW-MIB", "pwMspwGroupV1"))
)
if mibBuilder.loadTexts:
    lumPwBasicComplV2.setStatus(
        "deprecated"
    )

lumPwBasicComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 1, 2, 3)
)
lumPwBasicComplV3.setObjects(
      *(("LUM-PW-MIB", "pwGeneralGroupV2"),
        ("LUM-PW-MIB", "pwGenericGroupV3"),
        ("LUM-PW-MIB", "pwMplsGroupV2"),
        ("LUM-PW-MIB", "pwEnetGroupV3"),
        ("LUM-PW-MIB", "pwMspwGroupV1"))
)
if mibBuilder.loadTexts:
    lumPwBasicComplV3.setStatus(
        "deprecated"
    )

lumPwBasicComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41, 1, 2, 4)
)
lumPwBasicComplV4.setObjects(
      *(("LUM-PW-MIB", "pwGeneralGroupV2"),
        ("LUM-PW-MIB", "pwGenericGroupV3"),
        ("LUM-PW-MIB", "pwMplsGroupV3"),
        ("LUM-PW-MIB", "pwEnetGroupV3"),
        ("LUM-PW-MIB", "pwMspwGroupV1"))
)
if mibBuilder.loadTexts:
    lumPwBasicComplV4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-PW-MIB",
    **{"lumPwMIBModule": lumPwMIBModule,
       "lumPwConfs": lumPwConfs,
       "lumPwGroups": lumPwGroups,
       "pwGeneralGroupV1": pwGeneralGroupV1,
       "pwGenericGroupV1": pwGenericGroupV1,
       "pwMplsGroupV1": pwMplsGroupV1,
       "pwEnetGroupV1": pwEnetGroupV1,
       "pwEnetGroupV2": pwEnetGroupV2,
       "pwGeneralGroupV2": pwGeneralGroupV2,
       "pwMspwGroupV1": pwMspwGroupV1,
       "pwGenericGroupV2": pwGenericGroupV2,
       "pwEnetGroupV3": pwEnetGroupV3,
       "pwGenericGroupV3": pwGenericGroupV3,
       "pwMplsGroupV2": pwMplsGroupV2,
       "pwMplsGroupV3": pwMplsGroupV3,
       "lumPwCompl": lumPwCompl,
       "lumPwBasicComplV1": lumPwBasicComplV1,
       "lumPwBasicComplV2": lumPwBasicComplV2,
       "lumPwBasicComplV3": lumPwBasicComplV3,
       "lumPwBasicComplV4": lumPwBasicComplV4,
       "lumPwMIBObjects": lumPwMIBObjects,
       "pwGeneral": pwGeneral,
       "pwGeneralLastChangeTime": pwGeneralLastChangeTime,
       "pwGeneralStateLastChangeTime": pwGeneralStateLastChangeTime,
       "pwGeneralPwGenericTableSize": pwGeneralPwGenericTableSize,
       "pwGeneralPwMplsTableSize": pwGeneralPwMplsTableSize,
       "pwGeneralPwEnetTableSize": pwGeneralPwEnetTableSize,
       "pwGeneralPwMspwTableSize": pwGeneralPwMspwTableSize,
       "pwGenericList": pwGenericList,
       "pwGenericTable": pwGenericTable,
       "pwGenericEntry": pwGenericEntry,
       "pwGenericIndex": pwGenericIndex,
       "pwGenericName": pwGenericName,
       "pwGenericIdentifier": pwGenericIdentifier,
       "pwGenericInternalReference": pwGenericInternalReference,
       "pwGenericDescr": pwGenericDescr,
       "pwGenericOutboundLabel": pwGenericOutboundLabel,
       "pwGenericInboundLabel": pwGenericInboundLabel,
       "pwGenericInPackets": pwGenericInPackets,
       "pwGenericInBytes": pwGenericInBytes,
       "pwGenericOutPackets": pwGenericOutPackets,
       "pwGenericOutBytes": pwGenericOutBytes,
       "pwGenericResetCont": pwGenericResetCont,
       "pwGenericRowStatus": pwGenericRowStatus,
       "pwGenericPwType": pwGenericPwType,
       "pwGenericTrafficClass": pwGenericTrafficClass,
       "pwGenericReservedBW": pwGenericReservedBW,
       "pwGenericPwNumber": pwGenericPwNumber,
       "pwGenericConfigurationSet": pwGenericConfigurationSet,
       "pwGenericFlowLabel": pwGenericFlowLabel,
       "pwMplsList": pwMplsList,
       "pwMplsTable": pwMplsTable,
       "pwMplsEntry": pwMplsEntry,
       "pwMplsIndex": pwMplsIndex,
       "pwMplsName": pwMplsName,
       "pwMplsIdentifier": pwMplsIdentifier,
       "pwMplsInternalReference": pwMplsInternalReference,
       "pwMplsOutboundTunnelId": pwMplsOutboundTunnelId,
       "pwMplsAssociateTunnel": pwMplsAssociateTunnel,
       "pwMplsRowStatus": pwMplsRowStatus,
       "pwEnetList": pwEnetList,
       "pwEnetTable": pwEnetTable,
       "pwEnetEntry": pwEnetEntry,
       "pwEnetIndex": pwEnetIndex,
       "pwEnetName": pwEnetName,
       "pwEnetIdentifier": pwEnetIdentifier,
       "pwEnetInternalReference": pwEnetInternalReference,
       "pwEnetPortVlan": pwEnetPortVlan,
       "pwEnetPortIndex": pwEnetPortIndex,
       "pwEnetPortName": pwEnetPortName,
       "pwEnetTpid": pwEnetTpid,
       "pwEnetRowStatus": pwEnetRowStatus,
       "pwEnetClassification": pwEnetClassification,
       "pwEnetFecType": pwEnetFecType,
       "pwEnetSdTagVlanActionIngress": pwEnetSdTagVlanActionIngress,
       "pwEnetSdTagVlanIngress": pwEnetSdTagVlanIngress,
       "pwEnetSdTagVlanActionEgress": pwEnetSdTagVlanActionEgress,
       "pwEnetSdTagVlanEgress": pwEnetSdTagVlanEgress,
       "pwEnetOpMode": pwEnetOpMode,
       "pwEnetIfNo": pwEnetIfNo,
       "pwEnetTxPort": pwEnetTxPort,
       "pwEnetInterfaceName": pwEnetInterfaceName,
       "pwMspwList": pwMspwList,
       "pwMspwTable": pwMspwTable,
       "pwMspwEntry": pwMspwEntry,
       "pwMspwIndex": pwMspwIndex,
       "pwMspwName": pwMspwName,
       "pwMspwIdentifier": pwMspwIdentifier,
       "pwMspwInternalReference": pwMspwInternalReference,
       "pwMspwEastInboundLabel": pwMspwEastInboundLabel,
       "pwMspwEastOutboundLabel": pwMspwEastOutboundLabel,
       "pwMspwEastOutboundTunnelId": pwMspwEastOutboundTunnelId,
       "pwMspwWestInboundLabel": pwMspwWestInboundLabel,
       "pwMspwWestOutboundLabel": pwMspwWestOutboundLabel,
       "pwMspwWestOutboundTunnelId": pwMspwWestOutboundTunnelId,
       "pwMspwRowStatus": pwMspwRowStatus}
)
