# SNMP MIB module (FS-VM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-VM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:13:26 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "FS-TC",
    "ConfigStatus",
    "IfIndex")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsVMMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96)
)
if mibBuilder.loadTexts:
    fsVMMIB.setRevisions(
        ("2012-08-22 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsVMMIBObjects_ObjectIdentity = ObjectIdentity
fsVMMIBObjects = _FsVMMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1)
)
_FsVMFuncVMSupport_Type = ConfigStatus
_FsVMFuncVMSupport_Object = MibScalar
fsVMFuncVMSupport = _FsVMFuncVMSupport_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 1),
    _FsVMFuncVMSupport_Type()
)
fsVMFuncVMSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVMFuncVMSupport.setStatus("current")
_FsVMTrapCfgNotifyStatus_Type = ConfigStatus
_FsVMTrapCfgNotifyStatus_Object = MibScalar
fsVMTrapCfgNotifyStatus = _FsVMTrapCfgNotifyStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 2),
    _FsVMTrapCfgNotifyStatus_Type()
)
fsVMTrapCfgNotifyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVMTrapCfgNotifyStatus.setStatus("current")
_FsVMTrapCfgHistorySize_Type = Unsigned32
_FsVMTrapCfgHistorySize_Object = MibScalar
fsVMTrapCfgHistorySize = _FsVMTrapCfgHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 3),
    _FsVMTrapCfgHistorySize_Type()
)
fsVMTrapCfgHistorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVMTrapCfgHistorySize.setStatus("current")
_FsVMInfoTable_Object = MibTable
fsVMInfoTable = _FsVMInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 4)
)
if mibBuilder.loadTexts:
    fsVMInfoTable.setStatus("current")
_FsVMInfoEntry_Object = MibTableRow
fsVMInfoEntry = _FsVMInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 4, 1)
)
fsVMInfoEntry.setIndexNames(
    (0, "FS-VM-MIB", "fsVMInfoVMMac"),
    (0, "FS-VM-MIB", "fsVMInfoVMGroup"),
)
if mibBuilder.loadTexts:
    fsVMInfoEntry.setStatus("current")
_FsVMInfoVMMac_Type = MacAddress
_FsVMInfoVMMac_Object = MibTableColumn
fsVMInfoVMMac = _FsVMInfoVMMac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 4, 1, 1),
    _FsVMInfoVMMac_Type()
)
fsVMInfoVMMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVMInfoVMMac.setStatus("current")
_FsVMInfoVMGroup_Type = Integer32
_FsVMInfoVMGroup_Object = MibTableColumn
fsVMInfoVMGroup = _FsVMInfoVMGroup_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 4, 1, 2),
    _FsVMInfoVMGroup_Type()
)
fsVMInfoVMGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVMInfoVMGroup.setStatus("current")
_FsVMInfoRowStatus_Type = RowStatus
_FsVMInfoRowStatus_Object = MibTableColumn
fsVMInfoRowStatus = _FsVMInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 4, 1, 3),
    _FsVMInfoRowStatus_Type()
)
fsVMInfoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsVMInfoRowStatus.setStatus("current")
_FsVMGroupInfoTable_Object = MibTable
fsVMGroupInfoTable = _FsVMGroupInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 5)
)
if mibBuilder.loadTexts:
    fsVMGroupInfoTable.setStatus("current")
_FsVMGroupInfoEntry_Object = MibTableRow
fsVMGroupInfoEntry = _FsVMGroupInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 5, 1)
)
fsVMGroupInfoEntry.setIndexNames(
    (0, "FS-VM-MIB", "fsVMGroupInfoGroupName"),
)
if mibBuilder.loadTexts:
    fsVMGroupInfoEntry.setStatus("current")
_FsVMGroupInfoGroupName_Type = Integer32
_FsVMGroupInfoGroupName_Object = MibTableColumn
fsVMGroupInfoGroupName = _FsVMGroupInfoGroupName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 5, 1, 1),
    _FsVMGroupInfoGroupName_Type()
)
fsVMGroupInfoGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVMGroupInfoGroupName.setStatus("current")
_FsVMGroupInfoProfileCfg_Type = ConfigStatus
_FsVMGroupInfoProfileCfg_Object = MibTableColumn
fsVMGroupInfoProfileCfg = _FsVMGroupInfoProfileCfg_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 5, 1, 2),
    _FsVMGroupInfoProfileCfg_Type()
)
fsVMGroupInfoProfileCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVMGroupInfoProfileCfg.setStatus("current")


class _FsVMGroupInfoProfileName_Type(DisplayString):
    """Custom type fsVMGroupInfoProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsVMGroupInfoProfileName_Type.__name__ = "DisplayString"
_FsVMGroupInfoProfileName_Object = MibTableColumn
fsVMGroupInfoProfileName = _FsVMGroupInfoProfileName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 5, 1, 3),
    _FsVMGroupInfoProfileName_Type()
)
fsVMGroupInfoProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVMGroupInfoProfileName.setStatus("current")
_FsVMGroupInfoRowStatus_Type = RowStatus
_FsVMGroupInfoRowStatus_Object = MibTableColumn
fsVMGroupInfoRowStatus = _FsVMGroupInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 5, 1, 4),
    _FsVMGroupInfoRowStatus_Type()
)
fsVMGroupInfoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsVMGroupInfoRowStatus.setStatus("current")
_FsVMProfileTable_Object = MibTable
fsVMProfileTable = _FsVMProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 6)
)
if mibBuilder.loadTexts:
    fsVMProfileTable.setStatus("current")
_FsVMProfileEntry_Object = MibTableRow
fsVMProfileEntry = _FsVMProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 6, 1)
)
fsVMProfileEntry.setIndexNames(
    (0, "FS-VM-MIB", "fsVMProfileName"),
)
if mibBuilder.loadTexts:
    fsVMProfileEntry.setStatus("current")


class _FsVMProfileName_Type(DisplayString):
    """Custom type fsVMProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsVMProfileName_Type.__name__ = "DisplayString"
_FsVMProfileName_Object = MibTableColumn
fsVMProfileName = _FsVMProfileName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 6, 1, 1),
    _FsVMProfileName_Type()
)
fsVMProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVMProfileName.setStatus("current")


class _FsVMProfileAclIn_Type(DisplayString):
    """Custom type fsVMProfileAclIn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_FsVMProfileAclIn_Type.__name__ = "DisplayString"
_FsVMProfileAclIn_Object = MibTableColumn
fsVMProfileAclIn = _FsVMProfileAclIn_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 6, 1, 2),
    _FsVMProfileAclIn_Type()
)
fsVMProfileAclIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVMProfileAclIn.setStatus("current")


class _FsVMProfileAclOut_Type(DisplayString):
    """Custom type fsVMProfileAclOut based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_FsVMProfileAclOut_Type.__name__ = "DisplayString"
_FsVMProfileAclOut_Object = MibTableColumn
fsVMProfileAclOut = _FsVMProfileAclOut_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 6, 1, 3),
    _FsVMProfileAclOut_Type()
)
fsVMProfileAclOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVMProfileAclOut.setStatus("current")
_FsVMProfileTxRate_Type = Unsigned32
_FsVMProfileTxRate_Object = MibTableColumn
fsVMProfileTxRate = _FsVMProfileTxRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 6, 1, 4),
    _FsVMProfileTxRate_Type()
)
fsVMProfileTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVMProfileTxRate.setStatus("current")
_FsVMProfileTxBurst_Type = Integer32
_FsVMProfileTxBurst_Object = MibTableColumn
fsVMProfileTxBurst = _FsVMProfileTxBurst_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 6, 1, 5),
    _FsVMProfileTxBurst_Type()
)
fsVMProfileTxBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVMProfileTxBurst.setStatus("current")
_FsVMProfileRxRate_Type = Unsigned32
_FsVMProfileRxRate_Object = MibTableColumn
fsVMProfileRxRate = _FsVMProfileRxRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 6, 1, 6),
    _FsVMProfileRxRate_Type()
)
fsVMProfileRxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVMProfileRxRate.setStatus("current")
_FsVMProfileRxBurst_Type = Integer32
_FsVMProfileRxBurst_Object = MibTableColumn
fsVMProfileRxBurst = _FsVMProfileRxBurst_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 6, 1, 7),
    _FsVMProfileRxBurst_Type()
)
fsVMProfileRxBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVMProfileRxBurst.setStatus("current")
_FsVMProfileRowStatus_Type = RowStatus
_FsVMProfileRowStatus_Object = MibTableColumn
fsVMProfileRowStatus = _FsVMProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 6, 1, 8),
    _FsVMProfileRowStatus_Type()
)
fsVMProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsVMProfileRowStatus.setStatus("current")


class _FsVMProfileQosTrustMode_Type(Integer32):
    """Custom type fsVMProfileQosTrustMode based on Integer32"""
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
        *(("not-trust", 0),
          ("trust-cos", 1),
          ("trust-dscp", 2),
          ("trust-ip-precedence", 3))
    )


_FsVMProfileQosTrustMode_Type.__name__ = "Integer32"
_FsVMProfileQosTrustMode_Object = MibTableColumn
fsVMProfileQosTrustMode = _FsVMProfileQosTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 6, 1, 9),
    _FsVMProfileQosTrustMode_Type()
)
fsVMProfileQosTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVMProfileQosTrustMode.setStatus("current")


class _FsVMProfileQosDefCos_Type(Integer32):
    """Custom type fsVMProfileQosDefCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            8
        )
    )
    namedValues = NamedValues(
        ("invalid", 8)
    )


_FsVMProfileQosDefCos_Type.__name__ = "Integer32"
_FsVMProfileQosDefCos_Object = MibTableColumn
fsVMProfileQosDefCos = _FsVMProfileQosDefCos_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 6, 1, 10),
    _FsVMProfileQosDefCos_Type()
)
fsVMProfileQosDefCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVMProfileQosDefCos.setStatus("current")


class _FsVMProfileQosRxPolicyMap_Type(DisplayString):
    """Custom type fsVMProfileQosRxPolicyMap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsVMProfileQosRxPolicyMap_Type.__name__ = "DisplayString"
_FsVMProfileQosRxPolicyMap_Object = MibTableColumn
fsVMProfileQosRxPolicyMap = _FsVMProfileQosRxPolicyMap_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 6, 1, 11),
    _FsVMProfileQosRxPolicyMap_Type()
)
fsVMProfileQosRxPolicyMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVMProfileQosRxPolicyMap.setStatus("current")
_FsVMLocInfoTable_Object = MibTable
fsVMLocInfoTable = _FsVMLocInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 7)
)
if mibBuilder.loadTexts:
    fsVMLocInfoTable.setStatus("current")
_FsVMLocInfoEntry_Object = MibTableRow
fsVMLocInfoEntry = _FsVMLocInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 7, 1)
)
fsVMLocInfoEntry.setIndexNames(
    (0, "FS-VM-MIB", "fsVMLocInfoVMMac"),
    (0, "FS-VM-MIB", "fsVMLocInfoPort"),
)
if mibBuilder.loadTexts:
    fsVMLocInfoEntry.setStatus("current")
_FsVMLocInfoVMMac_Type = MacAddress
_FsVMLocInfoVMMac_Object = MibTableColumn
fsVMLocInfoVMMac = _FsVMLocInfoVMMac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 7, 1, 1),
    _FsVMLocInfoVMMac_Type()
)
fsVMLocInfoVMMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVMLocInfoVMMac.setStatus("current")
_FsVMLocInfoPort_Type = IfIndex
_FsVMLocInfoPort_Object = MibTableColumn
fsVMLocInfoPort = _FsVMLocInfoPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 7, 1, 2),
    _FsVMLocInfoPort_Type()
)
fsVMLocInfoPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVMLocInfoPort.setStatus("current")
_FsVMLocInfoType_Type = Unsigned32
_FsVMLocInfoType_Object = MibTableColumn
fsVMLocInfoType = _FsVMLocInfoType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 7, 1, 3),
    _FsVMLocInfoType_Type()
)
fsVMLocInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVMLocInfoType.setStatus("current")
_FsVMLocInfoRowStatus_Type = RowStatus
_FsVMLocInfoRowStatus_Object = MibTableColumn
fsVMLocInfoRowStatus = _FsVMLocInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 7, 1, 4),
    _FsVMLocInfoRowStatus_Type()
)
fsVMLocInfoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsVMLocInfoRowStatus.setStatus("current")
_FsVMPortInfoTable_Object = MibTable
fsVMPortInfoTable = _FsVMPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 8)
)
if mibBuilder.loadTexts:
    fsVMPortInfoTable.setStatus("current")
_FsVMPortInfoEntry_Object = MibTableRow
fsVMPortInfoEntry = _FsVMPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 8, 1)
)
fsVMPortInfoEntry.setIndexNames(
    (0, "FS-VM-MIB", "fsVMPortInfoPort"),
)
if mibBuilder.loadTexts:
    fsVMPortInfoEntry.setStatus("current")
_FsVMPortInfoPort_Type = IfIndex
_FsVMPortInfoPort_Object = MibTableColumn
fsVMPortInfoPort = _FsVMPortInfoPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 8, 1, 1),
    _FsVMPortInfoPort_Type()
)
fsVMPortInfoPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVMPortInfoPort.setStatus("current")
_FsVMPortInfoStatus_Type = ConfigStatus
_FsVMPortInfoStatus_Object = MibTableColumn
fsVMPortInfoStatus = _FsVMPortInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 8, 1, 2),
    _FsVMPortInfoStatus_Type()
)
fsVMPortInfoStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVMPortInfoStatus.setStatus("current")
_FsVMPortInfoReflectStatus_Type = ConfigStatus
_FsVMPortInfoReflectStatus_Object = MibTableColumn
fsVMPortInfoReflectStatus = _FsVMPortInfoReflectStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 8, 1, 3),
    _FsVMPortInfoReflectStatus_Type()
)
fsVMPortInfoReflectStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVMPortInfoReflectStatus.setStatus("current")
_FsVMPortTrapCfgTable_Object = MibTable
fsVMPortTrapCfgTable = _FsVMPortTrapCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 9)
)
if mibBuilder.loadTexts:
    fsVMPortTrapCfgTable.setStatus("current")
_FsVMPortTrapCfgEntry_Object = MibTableRow
fsVMPortTrapCfgEntry = _FsVMPortTrapCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 9, 1)
)
fsVMPortTrapCfgEntry.setIndexNames(
    (0, "FS-VM-MIB", "fsVMPortTrapCfgPort"),
)
if mibBuilder.loadTexts:
    fsVMPortTrapCfgEntry.setStatus("current")
_FsVMPortTrapCfgPort_Type = IfIndex
_FsVMPortTrapCfgPort_Object = MibTableColumn
fsVMPortTrapCfgPort = _FsVMPortTrapCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 9, 1, 1),
    _FsVMPortTrapCfgPort_Type()
)
fsVMPortTrapCfgPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVMPortTrapCfgPort.setStatus("current")
_FsVMPortTrapCfgNotifyStatus_Type = ConfigStatus
_FsVMPortTrapCfgNotifyStatus_Object = MibTableColumn
fsVMPortTrapCfgNotifyStatus = _FsVMPortTrapCfgNotifyStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 9, 1, 2),
    _FsVMPortTrapCfgNotifyStatus_Type()
)
fsVMPortTrapCfgNotifyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVMPortTrapCfgNotifyStatus.setStatus("current")
_FsVMInfoChgTable_Object = MibTable
fsVMInfoChgTable = _FsVMInfoChgTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 10)
)
if mibBuilder.loadTexts:
    fsVMInfoChgTable.setStatus("current")
_FsVMInfoChgEntry_Object = MibTableRow
fsVMInfoChgEntry = _FsVMInfoChgEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 10, 1)
)
fsVMInfoChgEntry.setIndexNames(
    (0, "FS-VM-MIB", "fsVMInfoChgVMMac"),
    (0, "FS-VM-MIB", "fsVMInfoChgVlan"),
)
if mibBuilder.loadTexts:
    fsVMInfoChgEntry.setStatus("current")
_FsVMInfoChgVMMac_Type = MacAddress
_FsVMInfoChgVMMac_Object = MibTableColumn
fsVMInfoChgVMMac = _FsVMInfoChgVMMac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 10, 1, 1),
    _FsVMInfoChgVMMac_Type()
)
fsVMInfoChgVMMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsVMInfoChgVMMac.setStatus("current")
_FsVMInfoChgVlan_Type = VlanId
_FsVMInfoChgVlan_Object = MibTableColumn
fsVMInfoChgVlan = _FsVMInfoChgVlan_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 10, 1, 2),
    _FsVMInfoChgVlan_Type()
)
fsVMInfoChgVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsVMInfoChgVlan.setStatus("current")
_FsVMInfoChgPort_Type = IfIndex
_FsVMInfoChgPort_Object = MibTableColumn
fsVMInfoChgPort = _FsVMInfoChgPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 10, 1, 3),
    _FsVMInfoChgPort_Type()
)
fsVMInfoChgPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsVMInfoChgPort.setStatus("current")


class _FsVMInfoChgAction_Type(DisplayString):
    """Custom type fsVMInfoChgAction based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsVMInfoChgAction_Type.__name__ = "DisplayString"
_FsVMInfoChgAction_Object = MibTableColumn
fsVMInfoChgAction = _FsVMInfoChgAction_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 10, 1, 4),
    _FsVMInfoChgAction_Type()
)
fsVMInfoChgAction.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsVMInfoChgAction.setStatus("current")
_FsVMInfoChgDate_Type = DateAndTime
_FsVMInfoChgDate_Object = MibTableColumn
fsVMInfoChgDate = _FsVMInfoChgDate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 10, 1, 5),
    _FsVMInfoChgDate_Type()
)
fsVMInfoChgDate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsVMInfoChgDate.setStatus("current")
_FsVMOuiInfoTable_Object = MibTable
fsVMOuiInfoTable = _FsVMOuiInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 11)
)
if mibBuilder.loadTexts:
    fsVMOuiInfoTable.setStatus("current")
_FsVMOuiInfoEntry_Object = MibTableRow
fsVMOuiInfoEntry = _FsVMOuiInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 11, 1)
)
fsVMOuiInfoEntry.setIndexNames(
    (0, "FS-VM-MIB", "fsVMOuiInfoOui"),
)
if mibBuilder.loadTexts:
    fsVMOuiInfoEntry.setStatus("current")
_FsVMOuiInfoOui_Type = MacAddress
_FsVMOuiInfoOui_Object = MibTableColumn
fsVMOuiInfoOui = _FsVMOuiInfoOui_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 11, 1, 1),
    _FsVMOuiInfoOui_Type()
)
fsVMOuiInfoOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVMOuiInfoOui.setStatus("current")
_FsVMOuiInfoRowStatus_Type = RowStatus
_FsVMOuiInfoRowStatus_Object = MibTableColumn
fsVMOuiInfoRowStatus = _FsVMOuiInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 11, 1, 2),
    _FsVMOuiInfoRowStatus_Type()
)
fsVMOuiInfoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsVMOuiInfoRowStatus.setStatus("current")
_FsVMRateMin_Type = Unsigned32
_FsVMRateMin_Object = MibScalar
fsVMRateMin = _FsVMRateMin_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 12),
    _FsVMRateMin_Type()
)
fsVMRateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVMRateMin.setStatus("current")
_FsVMRateMax_Type = Unsigned32
_FsVMRateMax_Object = MibScalar
fsVMRateMax = _FsVMRateMax_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 13),
    _FsVMRateMax_Type()
)
fsVMRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVMRateMax.setStatus("current")
_FsVMBurstMin_Type = Unsigned32
_FsVMBurstMin_Object = MibScalar
fsVMBurstMin = _FsVMBurstMin_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 14),
    _FsVMBurstMin_Type()
)
fsVMBurstMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVMBurstMin.setStatus("current")
_FsVMBurstMax_Type = Unsigned32
_FsVMBurstMax_Object = MibScalar
fsVMBurstMax = _FsVMBurstMax_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 1, 15),
    _FsVMBurstMax_Type()
)
fsVMBurstMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVMBurstMax.setStatus("current")
_FsVMMIBTraps_ObjectIdentity = ObjectIdentity
fsVMMIBTraps = _FsVMMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 2)
)
_FsVMMIBConformance_ObjectIdentity = ObjectIdentity
fsVMMIBConformance = _FsVMMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 3)
)
_FsVMMIBCompliances_ObjectIdentity = ObjectIdentity
fsVMMIBCompliances = _FsVMMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 3, 1)
)
_FsVMMIBGroups_ObjectIdentity = ObjectIdentity
fsVMMIBGroups = _FsVMMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 3, 2)
)

# Managed Objects groups

fsVMMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 3, 2, 1)
)
fsVMMIBGroup.setObjects(
      *(("FS-VM-MIB", "fsVMFuncVMSupport"),
        ("FS-VM-MIB", "fsVMTrapCfgNotifyStatus"),
        ("FS-VM-MIB", "fsVMTrapCfgHistorySize"),
        ("FS-VM-MIB", "fsVMRateMin"),
        ("FS-VM-MIB", "fsVMRateMax"),
        ("FS-VM-MIB", "fsVMBurstMin"),
        ("FS-VM-MIB", "fsVMBurstMax"),
        ("FS-VM-MIB", "fsVMInfoVMMac"),
        ("FS-VM-MIB", "fsVMInfoVMGroup"),
        ("FS-VM-MIB", "fsVMInfoRowStatus"),
        ("FS-VM-MIB", "fsVMGroupInfoGroupName"),
        ("FS-VM-MIB", "fsVMGroupInfoProfileCfg"),
        ("FS-VM-MIB", "fsVMGroupInfoProfileName"),
        ("FS-VM-MIB", "fsVMGroupInfoRowStatus"),
        ("FS-VM-MIB", "fsVMProfileName"),
        ("FS-VM-MIB", "fsVMProfileAclIn"),
        ("FS-VM-MIB", "fsVMProfileAclOut"),
        ("FS-VM-MIB", "fsVMProfileTxRate"),
        ("FS-VM-MIB", "fsVMProfileTxBurst"),
        ("FS-VM-MIB", "fsVMProfileRxRate"),
        ("FS-VM-MIB", "fsVMProfileRxBurst"),
        ("FS-VM-MIB", "fsVMProfileRowStatus"),
        ("FS-VM-MIB", "fsVMProfileQosTrustMode"),
        ("FS-VM-MIB", "fsVMProfileQosDefCos"),
        ("FS-VM-MIB", "fsVMProfileQosRxPolicyMap"),
        ("FS-VM-MIB", "fsVMLocInfoVMMac"),
        ("FS-VM-MIB", "fsVMLocInfoPort"),
        ("FS-VM-MIB", "fsVMLocInfoType"),
        ("FS-VM-MIB", "fsVMLocInfoRowStatus"),
        ("FS-VM-MIB", "fsVMPortInfoPort"),
        ("FS-VM-MIB", "fsVMPortInfoStatus"),
        ("FS-VM-MIB", "fsVMPortInfoReflectStatus"),
        ("FS-VM-MIB", "fsVMPortTrapCfgPort"),
        ("FS-VM-MIB", "fsVMPortTrapCfgNotifyStatus"),
        ("FS-VM-MIB", "fsVMInfoChgVMMac"),
        ("FS-VM-MIB", "fsVMInfoChgVlan"),
        ("FS-VM-MIB", "fsVMInfoChgPort"),
        ("FS-VM-MIB", "fsVMInfoChgAction"),
        ("FS-VM-MIB", "fsVMInfoChgDate"),
        ("FS-VM-MIB", "fsVMOuiInfoOui"),
        ("FS-VM-MIB", "fsVMOuiInfoRowStatus"))
)
if mibBuilder.loadTexts:
    fsVMMIBGroup.setStatus("current")


# Notification objects

fsVMsupMIBTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 2, 1)
)
fsVMsupMIBTrap.setObjects(
      *(("FS-VM-MIB", "fsVMInfoChgVMMac"),
        ("FS-VM-MIB", "fsVMInfoChgVlan"),
        ("FS-VM-MIB", "fsVMInfoChgPort"),
        ("FS-VM-MIB", "fsVMInfoChgAction"),
        ("FS-VM-MIB", "fsVMInfoChgDate"))
)
if mibBuilder.loadTexts:
    fsVMsupMIBTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

fsVMMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 96, 3, 1, 1)
)
fsVMMIBCompliance.setObjects(
    ("FS-VM-MIB", "fsVMMIBGroup")
)
if mibBuilder.loadTexts:
    fsVMMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-VM-MIB",
    **{"fsVMMIB": fsVMMIB,
       "fsVMMIBObjects": fsVMMIBObjects,
       "fsVMFuncVMSupport": fsVMFuncVMSupport,
       "fsVMTrapCfgNotifyStatus": fsVMTrapCfgNotifyStatus,
       "fsVMTrapCfgHistorySize": fsVMTrapCfgHistorySize,
       "fsVMInfoTable": fsVMInfoTable,
       "fsVMInfoEntry": fsVMInfoEntry,
       "fsVMInfoVMMac": fsVMInfoVMMac,
       "fsVMInfoVMGroup": fsVMInfoVMGroup,
       "fsVMInfoRowStatus": fsVMInfoRowStatus,
       "fsVMGroupInfoTable": fsVMGroupInfoTable,
       "fsVMGroupInfoEntry": fsVMGroupInfoEntry,
       "fsVMGroupInfoGroupName": fsVMGroupInfoGroupName,
       "fsVMGroupInfoProfileCfg": fsVMGroupInfoProfileCfg,
       "fsVMGroupInfoProfileName": fsVMGroupInfoProfileName,
       "fsVMGroupInfoRowStatus": fsVMGroupInfoRowStatus,
       "fsVMProfileTable": fsVMProfileTable,
       "fsVMProfileEntry": fsVMProfileEntry,
       "fsVMProfileName": fsVMProfileName,
       "fsVMProfileAclIn": fsVMProfileAclIn,
       "fsVMProfileAclOut": fsVMProfileAclOut,
       "fsVMProfileTxRate": fsVMProfileTxRate,
       "fsVMProfileTxBurst": fsVMProfileTxBurst,
       "fsVMProfileRxRate": fsVMProfileRxRate,
       "fsVMProfileRxBurst": fsVMProfileRxBurst,
       "fsVMProfileRowStatus": fsVMProfileRowStatus,
       "fsVMProfileQosTrustMode": fsVMProfileQosTrustMode,
       "fsVMProfileQosDefCos": fsVMProfileQosDefCos,
       "fsVMProfileQosRxPolicyMap": fsVMProfileQosRxPolicyMap,
       "fsVMLocInfoTable": fsVMLocInfoTable,
       "fsVMLocInfoEntry": fsVMLocInfoEntry,
       "fsVMLocInfoVMMac": fsVMLocInfoVMMac,
       "fsVMLocInfoPort": fsVMLocInfoPort,
       "fsVMLocInfoType": fsVMLocInfoType,
       "fsVMLocInfoRowStatus": fsVMLocInfoRowStatus,
       "fsVMPortInfoTable": fsVMPortInfoTable,
       "fsVMPortInfoEntry": fsVMPortInfoEntry,
       "fsVMPortInfoPort": fsVMPortInfoPort,
       "fsVMPortInfoStatus": fsVMPortInfoStatus,
       "fsVMPortInfoReflectStatus": fsVMPortInfoReflectStatus,
       "fsVMPortTrapCfgTable": fsVMPortTrapCfgTable,
       "fsVMPortTrapCfgEntry": fsVMPortTrapCfgEntry,
       "fsVMPortTrapCfgPort": fsVMPortTrapCfgPort,
       "fsVMPortTrapCfgNotifyStatus": fsVMPortTrapCfgNotifyStatus,
       "fsVMInfoChgTable": fsVMInfoChgTable,
       "fsVMInfoChgEntry": fsVMInfoChgEntry,
       "fsVMInfoChgVMMac": fsVMInfoChgVMMac,
       "fsVMInfoChgVlan": fsVMInfoChgVlan,
       "fsVMInfoChgPort": fsVMInfoChgPort,
       "fsVMInfoChgAction": fsVMInfoChgAction,
       "fsVMInfoChgDate": fsVMInfoChgDate,
       "fsVMOuiInfoTable": fsVMOuiInfoTable,
       "fsVMOuiInfoEntry": fsVMOuiInfoEntry,
       "fsVMOuiInfoOui": fsVMOuiInfoOui,
       "fsVMOuiInfoRowStatus": fsVMOuiInfoRowStatus,
       "fsVMRateMin": fsVMRateMin,
       "fsVMRateMax": fsVMRateMax,
       "fsVMBurstMin": fsVMBurstMin,
       "fsVMBurstMax": fsVMBurstMax,
       "fsVMMIBTraps": fsVMMIBTraps,
       "fsVMsupMIBTrap": fsVMsupMIBTrap,
       "fsVMMIBConformance": fsVMMIBConformance,
       "fsVMMIBCompliances": fsVMMIBCompliances,
       "fsVMMIBCompliance": fsVMMIBCompliance,
       "fsVMMIBGroups": fsVMMIBGroups,
       "fsVMMIBGroup": fsVMMIBGroup}
)
