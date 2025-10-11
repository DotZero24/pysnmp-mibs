# SNMP MIB module (QTECH-VM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-VM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:56:30 2025
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

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "QTECH-TC",
    "ConfigStatus",
    "IfIndex")

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

qtechVMMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96)
)
if mibBuilder.loadTexts:
    qtechVMMIB.setRevisions(
        ("2012-08-22 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechVMMIBObjects_ObjectIdentity = ObjectIdentity
qtechVMMIBObjects = _QtechVMMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1)
)
_QtechVMFuncVMSupport_Type = ConfigStatus
_QtechVMFuncVMSupport_Object = MibScalar
qtechVMFuncVMSupport = _QtechVMFuncVMSupport_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 1),
    _QtechVMFuncVMSupport_Type()
)
qtechVMFuncVMSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechVMFuncVMSupport.setStatus("current")
_QtechVMTrapCfgNotifyStatus_Type = ConfigStatus
_QtechVMTrapCfgNotifyStatus_Object = MibScalar
qtechVMTrapCfgNotifyStatus = _QtechVMTrapCfgNotifyStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 2),
    _QtechVMTrapCfgNotifyStatus_Type()
)
qtechVMTrapCfgNotifyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechVMTrapCfgNotifyStatus.setStatus("current")
_QtechVMTrapCfgHistorySize_Type = Unsigned32
_QtechVMTrapCfgHistorySize_Object = MibScalar
qtechVMTrapCfgHistorySize = _QtechVMTrapCfgHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 3),
    _QtechVMTrapCfgHistorySize_Type()
)
qtechVMTrapCfgHistorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechVMTrapCfgHistorySize.setStatus("current")
_QtechVMInfoTable_Object = MibTable
qtechVMInfoTable = _QtechVMInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 4)
)
if mibBuilder.loadTexts:
    qtechVMInfoTable.setStatus("current")
_QtechVMInfoEntry_Object = MibTableRow
qtechVMInfoEntry = _QtechVMInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 4, 1)
)
qtechVMInfoEntry.setIndexNames(
    (0, "QTECH-VM-MIB", "qtechVMInfoVMMac"),
    (0, "QTECH-VM-MIB", "qtechVMInfoVMGroup"),
)
if mibBuilder.loadTexts:
    qtechVMInfoEntry.setStatus("current")
_QtechVMInfoVMMac_Type = MacAddress
_QtechVMInfoVMMac_Object = MibTableColumn
qtechVMInfoVMMac = _QtechVMInfoVMMac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 4, 1, 1),
    _QtechVMInfoVMMac_Type()
)
qtechVMInfoVMMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVMInfoVMMac.setStatus("current")
_QtechVMInfoVMGroup_Type = Integer32
_QtechVMInfoVMGroup_Object = MibTableColumn
qtechVMInfoVMGroup = _QtechVMInfoVMGroup_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 4, 1, 2),
    _QtechVMInfoVMGroup_Type()
)
qtechVMInfoVMGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVMInfoVMGroup.setStatus("current")
_QtechVMInfoRowStatus_Type = RowStatus
_QtechVMInfoRowStatus_Object = MibTableColumn
qtechVMInfoRowStatus = _QtechVMInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 4, 1, 3),
    _QtechVMInfoRowStatus_Type()
)
qtechVMInfoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechVMInfoRowStatus.setStatus("current")
_QtechVMGroupInfoTable_Object = MibTable
qtechVMGroupInfoTable = _QtechVMGroupInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 5)
)
if mibBuilder.loadTexts:
    qtechVMGroupInfoTable.setStatus("current")
_QtechVMGroupInfoEntry_Object = MibTableRow
qtechVMGroupInfoEntry = _QtechVMGroupInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 5, 1)
)
qtechVMGroupInfoEntry.setIndexNames(
    (0, "QTECH-VM-MIB", "qtechVMGroupInfoGroupName"),
)
if mibBuilder.loadTexts:
    qtechVMGroupInfoEntry.setStatus("current")
_QtechVMGroupInfoGroupName_Type = Integer32
_QtechVMGroupInfoGroupName_Object = MibTableColumn
qtechVMGroupInfoGroupName = _QtechVMGroupInfoGroupName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 5, 1, 1),
    _QtechVMGroupInfoGroupName_Type()
)
qtechVMGroupInfoGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVMGroupInfoGroupName.setStatus("current")
_QtechVMGroupInfoProfileCfg_Type = ConfigStatus
_QtechVMGroupInfoProfileCfg_Object = MibTableColumn
qtechVMGroupInfoProfileCfg = _QtechVMGroupInfoProfileCfg_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 5, 1, 2),
    _QtechVMGroupInfoProfileCfg_Type()
)
qtechVMGroupInfoProfileCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechVMGroupInfoProfileCfg.setStatus("current")


class _QtechVMGroupInfoProfileName_Type(DisplayString):
    """Custom type qtechVMGroupInfoProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechVMGroupInfoProfileName_Type.__name__ = "DisplayString"
_QtechVMGroupInfoProfileName_Object = MibTableColumn
qtechVMGroupInfoProfileName = _QtechVMGroupInfoProfileName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 5, 1, 3),
    _QtechVMGroupInfoProfileName_Type()
)
qtechVMGroupInfoProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechVMGroupInfoProfileName.setStatus("current")
_QtechVMGroupInfoRowStatus_Type = RowStatus
_QtechVMGroupInfoRowStatus_Object = MibTableColumn
qtechVMGroupInfoRowStatus = _QtechVMGroupInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 5, 1, 4),
    _QtechVMGroupInfoRowStatus_Type()
)
qtechVMGroupInfoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechVMGroupInfoRowStatus.setStatus("current")
_QtechVMProfileTable_Object = MibTable
qtechVMProfileTable = _QtechVMProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 6)
)
if mibBuilder.loadTexts:
    qtechVMProfileTable.setStatus("current")
_QtechVMProfileEntry_Object = MibTableRow
qtechVMProfileEntry = _QtechVMProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 6, 1)
)
qtechVMProfileEntry.setIndexNames(
    (0, "QTECH-VM-MIB", "qtechVMProfileName"),
)
if mibBuilder.loadTexts:
    qtechVMProfileEntry.setStatus("current")


class _QtechVMProfileName_Type(DisplayString):
    """Custom type qtechVMProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechVMProfileName_Type.__name__ = "DisplayString"
_QtechVMProfileName_Object = MibTableColumn
qtechVMProfileName = _QtechVMProfileName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 6, 1, 1),
    _QtechVMProfileName_Type()
)
qtechVMProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVMProfileName.setStatus("current")


class _QtechVMProfileAclIn_Type(DisplayString):
    """Custom type qtechVMProfileAclIn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_QtechVMProfileAclIn_Type.__name__ = "DisplayString"
_QtechVMProfileAclIn_Object = MibTableColumn
qtechVMProfileAclIn = _QtechVMProfileAclIn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 6, 1, 2),
    _QtechVMProfileAclIn_Type()
)
qtechVMProfileAclIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechVMProfileAclIn.setStatus("current")


class _QtechVMProfileAclOut_Type(DisplayString):
    """Custom type qtechVMProfileAclOut based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_QtechVMProfileAclOut_Type.__name__ = "DisplayString"
_QtechVMProfileAclOut_Object = MibTableColumn
qtechVMProfileAclOut = _QtechVMProfileAclOut_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 6, 1, 3),
    _QtechVMProfileAclOut_Type()
)
qtechVMProfileAclOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechVMProfileAclOut.setStatus("current")
_QtechVMProfileTxRate_Type = Unsigned32
_QtechVMProfileTxRate_Object = MibTableColumn
qtechVMProfileTxRate = _QtechVMProfileTxRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 6, 1, 4),
    _QtechVMProfileTxRate_Type()
)
qtechVMProfileTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechVMProfileTxRate.setStatus("current")
_QtechVMProfileTxBurst_Type = Integer32
_QtechVMProfileTxBurst_Object = MibTableColumn
qtechVMProfileTxBurst = _QtechVMProfileTxBurst_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 6, 1, 5),
    _QtechVMProfileTxBurst_Type()
)
qtechVMProfileTxBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechVMProfileTxBurst.setStatus("current")
_QtechVMProfileRxRate_Type = Unsigned32
_QtechVMProfileRxRate_Object = MibTableColumn
qtechVMProfileRxRate = _QtechVMProfileRxRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 6, 1, 6),
    _QtechVMProfileRxRate_Type()
)
qtechVMProfileRxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechVMProfileRxRate.setStatus("current")
_QtechVMProfileRxBurst_Type = Integer32
_QtechVMProfileRxBurst_Object = MibTableColumn
qtechVMProfileRxBurst = _QtechVMProfileRxBurst_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 6, 1, 7),
    _QtechVMProfileRxBurst_Type()
)
qtechVMProfileRxBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechVMProfileRxBurst.setStatus("current")
_QtechVMProfileRowStatus_Type = RowStatus
_QtechVMProfileRowStatus_Object = MibTableColumn
qtechVMProfileRowStatus = _QtechVMProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 6, 1, 8),
    _QtechVMProfileRowStatus_Type()
)
qtechVMProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechVMProfileRowStatus.setStatus("current")


class _QtechVMProfileQosTrustMode_Type(Integer32):
    """Custom type qtechVMProfileQosTrustMode based on Integer32"""
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


_QtechVMProfileQosTrustMode_Type.__name__ = "Integer32"
_QtechVMProfileQosTrustMode_Object = MibTableColumn
qtechVMProfileQosTrustMode = _QtechVMProfileQosTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 6, 1, 9),
    _QtechVMProfileQosTrustMode_Type()
)
qtechVMProfileQosTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechVMProfileQosTrustMode.setStatus("current")


class _QtechVMProfileQosDefCos_Type(Integer32):
    """Custom type qtechVMProfileQosDefCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            8
        )
    )
    namedValues = NamedValues(
        ("invalid", 8)
    )


_QtechVMProfileQosDefCos_Type.__name__ = "Integer32"
_QtechVMProfileQosDefCos_Object = MibTableColumn
qtechVMProfileQosDefCos = _QtechVMProfileQosDefCos_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 6, 1, 10),
    _QtechVMProfileQosDefCos_Type()
)
qtechVMProfileQosDefCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechVMProfileQosDefCos.setStatus("current")


class _QtechVMProfileQosRxPolicyMap_Type(DisplayString):
    """Custom type qtechVMProfileQosRxPolicyMap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechVMProfileQosRxPolicyMap_Type.__name__ = "DisplayString"
_QtechVMProfileQosRxPolicyMap_Object = MibTableColumn
qtechVMProfileQosRxPolicyMap = _QtechVMProfileQosRxPolicyMap_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 6, 1, 11),
    _QtechVMProfileQosRxPolicyMap_Type()
)
qtechVMProfileQosRxPolicyMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechVMProfileQosRxPolicyMap.setStatus("current")
_QtechVMLocInfoTable_Object = MibTable
qtechVMLocInfoTable = _QtechVMLocInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 7)
)
if mibBuilder.loadTexts:
    qtechVMLocInfoTable.setStatus("current")
_QtechVMLocInfoEntry_Object = MibTableRow
qtechVMLocInfoEntry = _QtechVMLocInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 7, 1)
)
qtechVMLocInfoEntry.setIndexNames(
    (0, "QTECH-VM-MIB", "qtechVMLocInfoVMMac"),
    (0, "QTECH-VM-MIB", "qtechVMLocInfoPort"),
)
if mibBuilder.loadTexts:
    qtechVMLocInfoEntry.setStatus("current")
_QtechVMLocInfoVMMac_Type = MacAddress
_QtechVMLocInfoVMMac_Object = MibTableColumn
qtechVMLocInfoVMMac = _QtechVMLocInfoVMMac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 7, 1, 1),
    _QtechVMLocInfoVMMac_Type()
)
qtechVMLocInfoVMMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVMLocInfoVMMac.setStatus("current")
_QtechVMLocInfoPort_Type = IfIndex
_QtechVMLocInfoPort_Object = MibTableColumn
qtechVMLocInfoPort = _QtechVMLocInfoPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 7, 1, 2),
    _QtechVMLocInfoPort_Type()
)
qtechVMLocInfoPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVMLocInfoPort.setStatus("current")
_QtechVMLocInfoType_Type = Unsigned32
_QtechVMLocInfoType_Object = MibTableColumn
qtechVMLocInfoType = _QtechVMLocInfoType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 7, 1, 3),
    _QtechVMLocInfoType_Type()
)
qtechVMLocInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVMLocInfoType.setStatus("current")
_QtechVMLocInfoRowStatus_Type = RowStatus
_QtechVMLocInfoRowStatus_Object = MibTableColumn
qtechVMLocInfoRowStatus = _QtechVMLocInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 7, 1, 4),
    _QtechVMLocInfoRowStatus_Type()
)
qtechVMLocInfoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechVMLocInfoRowStatus.setStatus("current")
_QtechVMPortInfoTable_Object = MibTable
qtechVMPortInfoTable = _QtechVMPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 8)
)
if mibBuilder.loadTexts:
    qtechVMPortInfoTable.setStatus("current")
_QtechVMPortInfoEntry_Object = MibTableRow
qtechVMPortInfoEntry = _QtechVMPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 8, 1)
)
qtechVMPortInfoEntry.setIndexNames(
    (0, "QTECH-VM-MIB", "qtechVMPortInfoPort"),
)
if mibBuilder.loadTexts:
    qtechVMPortInfoEntry.setStatus("current")
_QtechVMPortInfoPort_Type = IfIndex
_QtechVMPortInfoPort_Object = MibTableColumn
qtechVMPortInfoPort = _QtechVMPortInfoPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 8, 1, 1),
    _QtechVMPortInfoPort_Type()
)
qtechVMPortInfoPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVMPortInfoPort.setStatus("current")
_QtechVMPortInfoStatus_Type = ConfigStatus
_QtechVMPortInfoStatus_Object = MibTableColumn
qtechVMPortInfoStatus = _QtechVMPortInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 8, 1, 2),
    _QtechVMPortInfoStatus_Type()
)
qtechVMPortInfoStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechVMPortInfoStatus.setStatus("current")
_QtechVMPortInfoReflectStatus_Type = ConfigStatus
_QtechVMPortInfoReflectStatus_Object = MibTableColumn
qtechVMPortInfoReflectStatus = _QtechVMPortInfoReflectStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 8, 1, 3),
    _QtechVMPortInfoReflectStatus_Type()
)
qtechVMPortInfoReflectStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechVMPortInfoReflectStatus.setStatus("current")
_QtechVMPortTrapCfgTable_Object = MibTable
qtechVMPortTrapCfgTable = _QtechVMPortTrapCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 9)
)
if mibBuilder.loadTexts:
    qtechVMPortTrapCfgTable.setStatus("current")
_QtechVMPortTrapCfgEntry_Object = MibTableRow
qtechVMPortTrapCfgEntry = _QtechVMPortTrapCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 9, 1)
)
qtechVMPortTrapCfgEntry.setIndexNames(
    (0, "QTECH-VM-MIB", "qtechVMPortTrapCfgPort"),
)
if mibBuilder.loadTexts:
    qtechVMPortTrapCfgEntry.setStatus("current")
_QtechVMPortTrapCfgPort_Type = IfIndex
_QtechVMPortTrapCfgPort_Object = MibTableColumn
qtechVMPortTrapCfgPort = _QtechVMPortTrapCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 9, 1, 1),
    _QtechVMPortTrapCfgPort_Type()
)
qtechVMPortTrapCfgPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVMPortTrapCfgPort.setStatus("current")
_QtechVMPortTrapCfgNotifyStatus_Type = ConfigStatus
_QtechVMPortTrapCfgNotifyStatus_Object = MibTableColumn
qtechVMPortTrapCfgNotifyStatus = _QtechVMPortTrapCfgNotifyStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 9, 1, 2),
    _QtechVMPortTrapCfgNotifyStatus_Type()
)
qtechVMPortTrapCfgNotifyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechVMPortTrapCfgNotifyStatus.setStatus("current")
_QtechVMInfoChgTable_Object = MibTable
qtechVMInfoChgTable = _QtechVMInfoChgTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 10)
)
if mibBuilder.loadTexts:
    qtechVMInfoChgTable.setStatus("current")
_QtechVMInfoChgEntry_Object = MibTableRow
qtechVMInfoChgEntry = _QtechVMInfoChgEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 10, 1)
)
qtechVMInfoChgEntry.setIndexNames(
    (0, "QTECH-VM-MIB", "qtechVMInfoChgVMMac"),
    (0, "QTECH-VM-MIB", "qtechVMInfoChgVlan"),
)
if mibBuilder.loadTexts:
    qtechVMInfoChgEntry.setStatus("current")
_QtechVMInfoChgVMMac_Type = MacAddress
_QtechVMInfoChgVMMac_Object = MibTableColumn
qtechVMInfoChgVMMac = _QtechVMInfoChgVMMac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 10, 1, 1),
    _QtechVMInfoChgVMMac_Type()
)
qtechVMInfoChgVMMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechVMInfoChgVMMac.setStatus("current")
_QtechVMInfoChgVlan_Type = VlanId
_QtechVMInfoChgVlan_Object = MibTableColumn
qtechVMInfoChgVlan = _QtechVMInfoChgVlan_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 10, 1, 2),
    _QtechVMInfoChgVlan_Type()
)
qtechVMInfoChgVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechVMInfoChgVlan.setStatus("current")
_QtechVMInfoChgPort_Type = IfIndex
_QtechVMInfoChgPort_Object = MibTableColumn
qtechVMInfoChgPort = _QtechVMInfoChgPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 10, 1, 3),
    _QtechVMInfoChgPort_Type()
)
qtechVMInfoChgPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechVMInfoChgPort.setStatus("current")


class _QtechVMInfoChgAction_Type(DisplayString):
    """Custom type qtechVMInfoChgAction based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechVMInfoChgAction_Type.__name__ = "DisplayString"
_QtechVMInfoChgAction_Object = MibTableColumn
qtechVMInfoChgAction = _QtechVMInfoChgAction_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 10, 1, 4),
    _QtechVMInfoChgAction_Type()
)
qtechVMInfoChgAction.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechVMInfoChgAction.setStatus("current")
_QtechVMInfoChgDate_Type = DateAndTime
_QtechVMInfoChgDate_Object = MibTableColumn
qtechVMInfoChgDate = _QtechVMInfoChgDate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 10, 1, 5),
    _QtechVMInfoChgDate_Type()
)
qtechVMInfoChgDate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechVMInfoChgDate.setStatus("current")
_QtechVMOuiInfoTable_Object = MibTable
qtechVMOuiInfoTable = _QtechVMOuiInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 11)
)
if mibBuilder.loadTexts:
    qtechVMOuiInfoTable.setStatus("current")
_QtechVMOuiInfoEntry_Object = MibTableRow
qtechVMOuiInfoEntry = _QtechVMOuiInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 11, 1)
)
qtechVMOuiInfoEntry.setIndexNames(
    (0, "QTECH-VM-MIB", "qtechVMOuiInfoOui"),
)
if mibBuilder.loadTexts:
    qtechVMOuiInfoEntry.setStatus("current")
_QtechVMOuiInfoOui_Type = MacAddress
_QtechVMOuiInfoOui_Object = MibTableColumn
qtechVMOuiInfoOui = _QtechVMOuiInfoOui_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 11, 1, 1),
    _QtechVMOuiInfoOui_Type()
)
qtechVMOuiInfoOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVMOuiInfoOui.setStatus("current")
_QtechVMOuiInfoRowStatus_Type = RowStatus
_QtechVMOuiInfoRowStatus_Object = MibTableColumn
qtechVMOuiInfoRowStatus = _QtechVMOuiInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 11, 1, 2),
    _QtechVMOuiInfoRowStatus_Type()
)
qtechVMOuiInfoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechVMOuiInfoRowStatus.setStatus("current")
_QtechVMRateMin_Type = Unsigned32
_QtechVMRateMin_Object = MibScalar
qtechVMRateMin = _QtechVMRateMin_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 12),
    _QtechVMRateMin_Type()
)
qtechVMRateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVMRateMin.setStatus("current")
_QtechVMRateMax_Type = Unsigned32
_QtechVMRateMax_Object = MibScalar
qtechVMRateMax = _QtechVMRateMax_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 13),
    _QtechVMRateMax_Type()
)
qtechVMRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVMRateMax.setStatus("current")
_QtechVMBurstMin_Type = Unsigned32
_QtechVMBurstMin_Object = MibScalar
qtechVMBurstMin = _QtechVMBurstMin_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 14),
    _QtechVMBurstMin_Type()
)
qtechVMBurstMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVMBurstMin.setStatus("current")
_QtechVMBurstMax_Type = Unsigned32
_QtechVMBurstMax_Object = MibScalar
qtechVMBurstMax = _QtechVMBurstMax_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 1, 15),
    _QtechVMBurstMax_Type()
)
qtechVMBurstMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVMBurstMax.setStatus("current")
_QtechVMMIBTraps_ObjectIdentity = ObjectIdentity
qtechVMMIBTraps = _QtechVMMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 2)
)
_QtechVMMIBConformance_ObjectIdentity = ObjectIdentity
qtechVMMIBConformance = _QtechVMMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 3)
)
_QtechVMMIBCompliances_ObjectIdentity = ObjectIdentity
qtechVMMIBCompliances = _QtechVMMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 3, 1)
)
_QtechVMMIBGroups_ObjectIdentity = ObjectIdentity
qtechVMMIBGroups = _QtechVMMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 3, 2)
)

# Managed Objects groups

qtechVMMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 3, 2, 1)
)
qtechVMMIBGroup.setObjects(
      *(("QTECH-VM-MIB", "qtechVMFuncVMSupport"),
        ("QTECH-VM-MIB", "qtechVMTrapCfgNotifyStatus"),
        ("QTECH-VM-MIB", "qtechVMTrapCfgHistorySize"),
        ("QTECH-VM-MIB", "qtechVMRateMin"),
        ("QTECH-VM-MIB", "qtechVMRateMax"),
        ("QTECH-VM-MIB", "qtechVMBurstMin"),
        ("QTECH-VM-MIB", "qtechVMBurstMax"),
        ("QTECH-VM-MIB", "qtechVMInfoVMMac"),
        ("QTECH-VM-MIB", "qtechVMInfoVMGroup"),
        ("QTECH-VM-MIB", "qtechVMInfoRowStatus"),
        ("QTECH-VM-MIB", "qtechVMGroupInfoGroupName"),
        ("QTECH-VM-MIB", "qtechVMGroupInfoProfileCfg"),
        ("QTECH-VM-MIB", "qtechVMGroupInfoProfileName"),
        ("QTECH-VM-MIB", "qtechVMGroupInfoRowStatus"),
        ("QTECH-VM-MIB", "qtechVMProfileName"),
        ("QTECH-VM-MIB", "qtechVMProfileAclIn"),
        ("QTECH-VM-MIB", "qtechVMProfileAclOut"),
        ("QTECH-VM-MIB", "qtechVMProfileTxRate"),
        ("QTECH-VM-MIB", "qtechVMProfileTxBurst"),
        ("QTECH-VM-MIB", "qtechVMProfileRxRate"),
        ("QTECH-VM-MIB", "qtechVMProfileRxBurst"),
        ("QTECH-VM-MIB", "qtechVMProfileRowStatus"),
        ("QTECH-VM-MIB", "qtechVMProfileQosTrustMode"),
        ("QTECH-VM-MIB", "qtechVMProfileQosDefCos"),
        ("QTECH-VM-MIB", "qtechVMProfileQosRxPolicyMap"),
        ("QTECH-VM-MIB", "qtechVMLocInfoVMMac"),
        ("QTECH-VM-MIB", "qtechVMLocInfoPort"),
        ("QTECH-VM-MIB", "qtechVMLocInfoType"),
        ("QTECH-VM-MIB", "qtechVMLocInfoRowStatus"),
        ("QTECH-VM-MIB", "qtechVMPortInfoPort"),
        ("QTECH-VM-MIB", "qtechVMPortInfoStatus"),
        ("QTECH-VM-MIB", "qtechVMPortInfoReflectStatus"),
        ("QTECH-VM-MIB", "qtechVMPortTrapCfgPort"),
        ("QTECH-VM-MIB", "qtechVMPortTrapCfgNotifyStatus"),
        ("QTECH-VM-MIB", "qtechVMInfoChgVMMac"),
        ("QTECH-VM-MIB", "qtechVMInfoChgVlan"),
        ("QTECH-VM-MIB", "qtechVMInfoChgPort"),
        ("QTECH-VM-MIB", "qtechVMInfoChgAction"),
        ("QTECH-VM-MIB", "qtechVMInfoChgDate"),
        ("QTECH-VM-MIB", "qtechVMOuiInfoOui"),
        ("QTECH-VM-MIB", "qtechVMOuiInfoRowStatus"))
)
if mibBuilder.loadTexts:
    qtechVMMIBGroup.setStatus("current")


# Notification objects

qtechVMsupMIBTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 2, 1)
)
qtechVMsupMIBTrap.setObjects(
      *(("QTECH-VM-MIB", "qtechVMInfoChgVMMac"),
        ("QTECH-VM-MIB", "qtechVMInfoChgVlan"),
        ("QTECH-VM-MIB", "qtechVMInfoChgPort"),
        ("QTECH-VM-MIB", "qtechVMInfoChgAction"),
        ("QTECH-VM-MIB", "qtechVMInfoChgDate"))
)
if mibBuilder.loadTexts:
    qtechVMsupMIBTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

qtechVMMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 96, 3, 1, 1)
)
qtechVMMIBCompliance.setObjects(
    ("QTECH-VM-MIB", "qtechVMMIBGroup")
)
if mibBuilder.loadTexts:
    qtechVMMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-VM-MIB",
    **{"qtechVMMIB": qtechVMMIB,
       "qtechVMMIBObjects": qtechVMMIBObjects,
       "qtechVMFuncVMSupport": qtechVMFuncVMSupport,
       "qtechVMTrapCfgNotifyStatus": qtechVMTrapCfgNotifyStatus,
       "qtechVMTrapCfgHistorySize": qtechVMTrapCfgHistorySize,
       "qtechVMInfoTable": qtechVMInfoTable,
       "qtechVMInfoEntry": qtechVMInfoEntry,
       "qtechVMInfoVMMac": qtechVMInfoVMMac,
       "qtechVMInfoVMGroup": qtechVMInfoVMGroup,
       "qtechVMInfoRowStatus": qtechVMInfoRowStatus,
       "qtechVMGroupInfoTable": qtechVMGroupInfoTable,
       "qtechVMGroupInfoEntry": qtechVMGroupInfoEntry,
       "qtechVMGroupInfoGroupName": qtechVMGroupInfoGroupName,
       "qtechVMGroupInfoProfileCfg": qtechVMGroupInfoProfileCfg,
       "qtechVMGroupInfoProfileName": qtechVMGroupInfoProfileName,
       "qtechVMGroupInfoRowStatus": qtechVMGroupInfoRowStatus,
       "qtechVMProfileTable": qtechVMProfileTable,
       "qtechVMProfileEntry": qtechVMProfileEntry,
       "qtechVMProfileName": qtechVMProfileName,
       "qtechVMProfileAclIn": qtechVMProfileAclIn,
       "qtechVMProfileAclOut": qtechVMProfileAclOut,
       "qtechVMProfileTxRate": qtechVMProfileTxRate,
       "qtechVMProfileTxBurst": qtechVMProfileTxBurst,
       "qtechVMProfileRxRate": qtechVMProfileRxRate,
       "qtechVMProfileRxBurst": qtechVMProfileRxBurst,
       "qtechVMProfileRowStatus": qtechVMProfileRowStatus,
       "qtechVMProfileQosTrustMode": qtechVMProfileQosTrustMode,
       "qtechVMProfileQosDefCos": qtechVMProfileQosDefCos,
       "qtechVMProfileQosRxPolicyMap": qtechVMProfileQosRxPolicyMap,
       "qtechVMLocInfoTable": qtechVMLocInfoTable,
       "qtechVMLocInfoEntry": qtechVMLocInfoEntry,
       "qtechVMLocInfoVMMac": qtechVMLocInfoVMMac,
       "qtechVMLocInfoPort": qtechVMLocInfoPort,
       "qtechVMLocInfoType": qtechVMLocInfoType,
       "qtechVMLocInfoRowStatus": qtechVMLocInfoRowStatus,
       "qtechVMPortInfoTable": qtechVMPortInfoTable,
       "qtechVMPortInfoEntry": qtechVMPortInfoEntry,
       "qtechVMPortInfoPort": qtechVMPortInfoPort,
       "qtechVMPortInfoStatus": qtechVMPortInfoStatus,
       "qtechVMPortInfoReflectStatus": qtechVMPortInfoReflectStatus,
       "qtechVMPortTrapCfgTable": qtechVMPortTrapCfgTable,
       "qtechVMPortTrapCfgEntry": qtechVMPortTrapCfgEntry,
       "qtechVMPortTrapCfgPort": qtechVMPortTrapCfgPort,
       "qtechVMPortTrapCfgNotifyStatus": qtechVMPortTrapCfgNotifyStatus,
       "qtechVMInfoChgTable": qtechVMInfoChgTable,
       "qtechVMInfoChgEntry": qtechVMInfoChgEntry,
       "qtechVMInfoChgVMMac": qtechVMInfoChgVMMac,
       "qtechVMInfoChgVlan": qtechVMInfoChgVlan,
       "qtechVMInfoChgPort": qtechVMInfoChgPort,
       "qtechVMInfoChgAction": qtechVMInfoChgAction,
       "qtechVMInfoChgDate": qtechVMInfoChgDate,
       "qtechVMOuiInfoTable": qtechVMOuiInfoTable,
       "qtechVMOuiInfoEntry": qtechVMOuiInfoEntry,
       "qtechVMOuiInfoOui": qtechVMOuiInfoOui,
       "qtechVMOuiInfoRowStatus": qtechVMOuiInfoRowStatus,
       "qtechVMRateMin": qtechVMRateMin,
       "qtechVMRateMax": qtechVMRateMax,
       "qtechVMBurstMin": qtechVMBurstMin,
       "qtechVMBurstMax": qtechVMBurstMax,
       "qtechVMMIBTraps": qtechVMMIBTraps,
       "qtechVMsupMIBTrap": qtechVMsupMIBTrap,
       "qtechVMMIBConformance": qtechVMMIBConformance,
       "qtechVMMIBCompliances": qtechVMMIBCompliances,
       "qtechVMMIBCompliance": qtechVMMIBCompliance,
       "qtechVMMIBGroups": qtechVMMIBGroups,
       "qtechVMMIBGroup": qtechVMMIBGroup}
)
