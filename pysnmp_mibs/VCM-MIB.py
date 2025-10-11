# SNMP MIB module (VCM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/VCM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:44:28 2025
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fsVcmMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93)
)
if mibBuilder.loadTexts:
    fsVcmMib.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsVcmConfig_ObjectIdentity = ObjectIdentity
fsVcmConfig = _FsVcmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 1)
)


class _FsVcmTraceOption_Type(Integer32):
    """Custom type fsVcmTraceOption based on Integer32"""
    defaultValue = 0


_FsVcmTraceOption_Type.__name__ = "Integer32"
_FsVcmTraceOption_Object = MibScalar
fsVcmTraceOption = _FsVcmTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 1, 1),
    _FsVcmTraceOption_Type()
)
fsVcmTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVcmTraceOption.setStatus("current")
_FsVcmConfigTable_Object = MibTable
fsVcmConfigTable = _FsVcmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 1, 2)
)
if mibBuilder.loadTexts:
    fsVcmConfigTable.setStatus("current")
_FsVcmConfigEntry_Object = MibTableRow
fsVcmConfigEntry = _FsVcmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 1, 2, 1)
)
fsVcmConfigEntry.setIndexNames(
    (0, "VCM-MIB", "fsVCId"),
)
if mibBuilder.loadTexts:
    fsVcmConfigEntry.setStatus("current")


class _FsVCId_Type(Integer32):
    """Custom type fsVCId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsVCId_Type.__name__ = "Integer32"
_FsVCId_Object = MibTableColumn
fsVCId = _FsVCId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 1, 2, 1, 1),
    _FsVCId_Type()
)
fsVCId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsVCId.setStatus("current")
_FsVCNextFreeHlPortId_Type = InterfaceIndexOrZero
_FsVCNextFreeHlPortId_Object = MibTableColumn
fsVCNextFreeHlPortId = _FsVCNextFreeHlPortId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 1, 2, 1, 2),
    _FsVCNextFreeHlPortId_Type()
)
fsVCNextFreeHlPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVCNextFreeHlPortId.setStatus("current")
_FsVCMacAddress_Type = MacAddress
_FsVCMacAddress_Object = MibTableColumn
fsVCMacAddress = _FsVCMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 1, 2, 1, 3),
    _FsVCMacAddress_Type()
)
fsVCMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVCMacAddress.setStatus("current")


class _FsVcAlias_Type(DisplayString):
    """Custom type fsVcAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsVcAlias_Type.__name__ = "DisplayString"
_FsVcAlias_Object = MibTableColumn
fsVcAlias = _FsVcAlias_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 1, 2, 1, 4),
    _FsVcAlias_Type()
)
fsVcAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVcAlias.setStatus("current")


class _FsVcCxtType_Type(Integer32):
    """Custom type fsVcCxtType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("l2Context", 1),
          ("l3Context", 2),
          ("both", 3))
    )


_FsVcCxtType_Type.__name__ = "Integer32"
_FsVcCxtType_Object = MibTableColumn
fsVcCxtType = _FsVcCxtType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 1, 2, 1, 5),
    _FsVcCxtType_Type()
)
fsVcCxtType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVcCxtType.setStatus("current")
_FsVCStatus_Type = RowStatus
_FsVCStatus_Object = MibTableColumn
fsVCStatus = _FsVCStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 1, 2, 1, 6),
    _FsVCStatus_Type()
)
fsVCStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsVCStatus.setStatus("current")
_FsVRMacAddress_Type = MacAddress
_FsVRMacAddress_Object = MibTableColumn
fsVRMacAddress = _FsVRMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 1, 2, 1, 7),
    _FsVRMacAddress_Type()
)
fsVRMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVRMacAddress.setStatus("current")
_FsVcmIfMappingTable_Object = MibTable
fsVcmIfMappingTable = _FsVcmIfMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 1, 3)
)
if mibBuilder.loadTexts:
    fsVcmIfMappingTable.setStatus("current")
_FsVcmIfMappingEntry_Object = MibTableRow
fsVcmIfMappingEntry = _FsVcmIfMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 1, 3, 1)
)
fsVcmIfMappingEntry.setIndexNames(
    (0, "VCM-MIB", "fsVcmIfIndex"),
)
if mibBuilder.loadTexts:
    fsVcmIfMappingEntry.setStatus("current")
_FsVcmIfIndex_Type = InterfaceIndex
_FsVcmIfIndex_Object = MibTableColumn
fsVcmIfIndex = _FsVcmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 1, 3, 1, 1),
    _FsVcmIfIndex_Type()
)
fsVcmIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsVcmIfIndex.setStatus("current")


class _FsVcId_Type(Integer32):
    """Custom type fsVcId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_FsVcId_Type.__name__ = "Integer32"
_FsVcId_Object = MibTableColumn
fsVcId = _FsVcId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 1, 3, 1, 2),
    _FsVcId_Type()
)
fsVcId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVcId.setStatus("current")
_FsVcHlPortId_Type = InterfaceIndexOrZero
_FsVcHlPortId_Object = MibTableColumn
fsVcHlPortId = _FsVcHlPortId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 1, 3, 1, 3),
    _FsVcHlPortId_Type()
)
fsVcHlPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVcHlPortId.setStatus("current")


class _FsVcL2ContextId_Type(Integer32):
    """Custom type fsVcL2ContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsVcL2ContextId_Type.__name__ = "Integer32"
_FsVcL2ContextId_Object = MibTableColumn
fsVcL2ContextId = _FsVcL2ContextId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 1, 3, 1, 4),
    _FsVcL2ContextId_Type()
)
fsVcL2ContextId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVcL2ContextId.setStatus("current")
_FsVcIfRowStatus_Type = RowStatus
_FsVcIfRowStatus_Object = MibTableColumn
fsVcIfRowStatus = _FsVcIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 1, 3, 1, 5),
    _FsVcIfRowStatus_Type()
)
fsVcIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsVcIfRowStatus.setStatus("current")
_FsVcmL2CxtAndVlanToIPIfaceMapTable_Object = MibTable
fsVcmL2CxtAndVlanToIPIfaceMapTable = _FsVcmL2CxtAndVlanToIPIfaceMapTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 1, 4)
)
if mibBuilder.loadTexts:
    fsVcmL2CxtAndVlanToIPIfaceMapTable.setStatus("current")
_FsVcmL2CxtAndVlanToIPIfaceMapEntry_Object = MibTableRow
fsVcmL2CxtAndVlanToIPIfaceMapEntry = _FsVcmL2CxtAndVlanToIPIfaceMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 1, 4, 1)
)
fsVcmL2CxtAndVlanToIPIfaceMapEntry.setIndexNames(
    (0, "VCM-MIB", "fsVcmL2VcId"),
    (0, "VCM-MIB", "fsVcmVlanId"),
)
if mibBuilder.loadTexts:
    fsVcmL2CxtAndVlanToIPIfaceMapEntry.setStatus("current")


class _FsVcmL2VcId_Type(Integer32):
    """Custom type fsVcmL2VcId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsVcmL2VcId_Type.__name__ = "Integer32"
_FsVcmL2VcId_Object = MibTableColumn
fsVcmL2VcId = _FsVcmL2VcId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 1, 4, 1, 1),
    _FsVcmL2VcId_Type()
)
fsVcmL2VcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsVcmL2VcId.setStatus("current")


class _FsVcmVlanId_Type(Integer32):
    """Custom type fsVcmVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsVcmVlanId_Type.__name__ = "Integer32"
_FsVcmVlanId_Object = MibTableColumn
fsVcmVlanId = _FsVcmVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 1, 4, 1, 2),
    _FsVcmVlanId_Type()
)
fsVcmVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsVcmVlanId.setStatus("current")


class _FsVcmL2VcName_Type(DisplayString):
    """Custom type fsVcmL2VcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsVcmL2VcName_Type.__name__ = "DisplayString"
_FsVcmL2VcName_Object = MibTableColumn
fsVcmL2VcName = _FsVcmL2VcName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 1, 4, 1, 3),
    _FsVcmL2VcName_Type()
)
fsVcmL2VcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVcmL2VcName.setStatus("current")
_FsVcmIPIfIndex_Type = InterfaceIndex
_FsVcmIPIfIndex_Object = MibTableColumn
fsVcmIPIfIndex = _FsVcmIPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 1, 4, 1, 4),
    _FsVcmIPIfIndex_Type()
)
fsVcmIPIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVcmIPIfIndex.setStatus("current")
_FsVcConfigExtTable_Object = MibTable
fsVcConfigExtTable = _FsVcConfigExtTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 1, 5)
)
if mibBuilder.loadTexts:
    fsVcConfigExtTable.setStatus("current")
_FsVcConfigExtEntry_Object = MibTableRow
fsVcConfigExtEntry = _FsVcConfigExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 1, 5, 1)
)
if mibBuilder.loadTexts:
    fsVcConfigExtEntry.setStatus("current")


class _FsVcOwner_Type(DisplayString):
    """Custom type fsVcOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FsVcOwner_Type.__name__ = "DisplayString"
_FsVcOwner_Object = MibTableColumn
fsVcOwner = _FsVcOwner_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 1, 5, 1, 1),
    _FsVcOwner_Type()
)
fsVcOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVcOwner.setStatus("current")
_FsVcmFreeVcIdTable_Object = MibTable
fsVcmFreeVcIdTable = _FsVcmFreeVcIdTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 1, 6)
)
if mibBuilder.loadTexts:
    fsVcmFreeVcIdTable.setStatus("current")
_FsVcmFreeVcIdEntry_Object = MibTableRow
fsVcmFreeVcIdEntry = _FsVcmFreeVcIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 1, 6, 1)
)
fsVcmFreeVcIdEntry.setIndexNames(
    (0, "VCM-MIB", "fsVcmFreeVcId"),
)
if mibBuilder.loadTexts:
    fsVcmFreeVcIdEntry.setStatus("current")


class _FsVcmFreeVcId_Type(Integer32):
    """Custom type fsVcmFreeVcId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsVcmFreeVcId_Type.__name__ = "Integer32"
_FsVcmFreeVcId_Object = MibTableColumn
fsVcmFreeVcId = _FsVcmFreeVcId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 1, 6, 1, 1),
    _FsVcmFreeVcId_Type()
)
fsVcmFreeVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVcmFreeVcId.setStatus("current")
_FsVcmTraps_ObjectIdentity = ObjectIdentity
fsVcmTraps = _FsVcmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 2)
)
_FsVcmAppContextConfig_ObjectIdentity = ObjectIdentity
fsVcmAppContextConfig = _FsVcmAppContextConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 3)
)


class _FsVcmFirmwareUpgradeCxt_Type(Integer32):
    """Custom type fsVcmFirmwareUpgradeCxt based on Integer32"""
    defaultValue = 1


_FsVcmFirmwareUpgradeCxt_Type.__name__ = "Integer32"
_FsVcmFirmwareUpgradeCxt_Object = MibScalar
fsVcmFirmwareUpgradeCxt = _FsVcmFirmwareUpgradeCxt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 3, 1),
    _FsVcmFirmwareUpgradeCxt_Type()
)
fsVcmFirmwareUpgradeCxt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVcmFirmwareUpgradeCxt.setStatus("current")


class _FsVcmFileCopyCxt_Type(Integer32):
    """Custom type fsVcmFileCopyCxt based on Integer32"""
    defaultValue = 1


_FsVcmFileCopyCxt_Type.__name__ = "Integer32"
_FsVcmFileCopyCxt_Object = MibScalar
fsVcmFileCopyCxt = _FsVcmFileCopyCxt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 3, 2),
    _FsVcmFileCopyCxt_Type()
)
fsVcmFileCopyCxt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVcmFileCopyCxt.setStatus("current")


class _FsVcmCoredumpPutCxt_Type(Integer32):
    """Custom type fsVcmCoredumpPutCxt based on Integer32"""
    defaultValue = 1


_FsVcmCoredumpPutCxt_Type.__name__ = "Integer32"
_FsVcmCoredumpPutCxt_Object = MibScalar
fsVcmCoredumpPutCxt = _FsVcmCoredumpPutCxt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 3, 3),
    _FsVcmCoredumpPutCxt_Type()
)
fsVcmCoredumpPutCxt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVcmCoredumpPutCxt.setStatus("current")


class _FsVcmSyslogClientCxt_Type(Integer32):
    """Custom type fsVcmSyslogClientCxt based on Integer32"""
    defaultValue = 1


_FsVcmSyslogClientCxt_Type.__name__ = "Integer32"
_FsVcmSyslogClientCxt_Object = MibScalar
fsVcmSyslogClientCxt = _FsVcmSyslogClientCxt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 3, 4),
    _FsVcmSyslogClientCxt_Type()
)
fsVcmSyslogClientCxt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVcmSyslogClientCxt.setStatus("current")


class _FsVcmSnmpTrapClientCxt_Type(Integer32):
    """Custom type fsVcmSnmpTrapClientCxt based on Integer32"""
    defaultValue = 1


_FsVcmSnmpTrapClientCxt_Type.__name__ = "Integer32"
_FsVcmSnmpTrapClientCxt_Object = MibScalar
fsVcmSnmpTrapClientCxt = _FsVcmSnmpTrapClientCxt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 3, 5),
    _FsVcmSnmpTrapClientCxt_Type()
)
fsVcmSnmpTrapClientCxt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVcmSnmpTrapClientCxt.setStatus("current")


class _FsVcmSntpClientCxt_Type(Integer32):
    """Custom type fsVcmSntpClientCxt based on Integer32"""
    defaultValue = 1


_FsVcmSntpClientCxt_Type.__name__ = "Integer32"
_FsVcmSntpClientCxt_Object = MibScalar
fsVcmSntpClientCxt = _FsVcmSntpClientCxt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 3, 6),
    _FsVcmSntpClientCxt_Type()
)
fsVcmSntpClientCxt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVcmSntpClientCxt.setStatus("current")


class _FsVcmSnmpAgentxCxt_Type(Integer32):
    """Custom type fsVcmSnmpAgentxCxt based on Integer32"""
    defaultValue = 1


_FsVcmSnmpAgentxCxt_Type.__name__ = "Integer32"
_FsVcmSnmpAgentxCxt_Object = MibScalar
fsVcmSnmpAgentxCxt = _FsVcmSnmpAgentxCxt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 3, 7),
    _FsVcmSnmpAgentxCxt_Type()
)
fsVcmSnmpAgentxCxt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVcmSnmpAgentxCxt.setStatus("current")


class _FsVcmTacacsClientCxt_Type(Integer32):
    """Custom type fsVcmTacacsClientCxt based on Integer32"""
    defaultValue = 1


_FsVcmTacacsClientCxt_Type.__name__ = "Integer32"
_FsVcmTacacsClientCxt_Object = MibScalar
fsVcmTacacsClientCxt = _FsVcmTacacsClientCxt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 3, 8),
    _FsVcmTacacsClientCxt_Type()
)
fsVcmTacacsClientCxt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVcmTacacsClientCxt.setStatus("current")


class _FsVcmRadiusClientCxt_Type(Integer32):
    """Custom type fsVcmRadiusClientCxt based on Integer32"""
    defaultValue = 1


_FsVcmRadiusClientCxt_Type.__name__ = "Integer32"
_FsVcmRadiusClientCxt_Object = MibScalar
fsVcmRadiusClientCxt = _FsVcmRadiusClientCxt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 3, 9),
    _FsVcmRadiusClientCxt_Type()
)
fsVcmRadiusClientCxt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVcmRadiusClientCxt.setStatus("current")
fsVcmConfigEntry.registerAugmentions(
    ("VCM-MIB",
     "fsVcConfigExtEntry")
)
fsVcConfigExtEntry.setIndexNames(*fsVcmConfigEntry.getIndexNames())

# Managed Objects groups


# Notification objects

fsVcmContextCreatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 2, 1)
)
fsVcmContextCreatedTrap.setObjects(
    ("VCM-MIB", "fsVCId")
)
if mibBuilder.loadTexts:
    fsVcmContextCreatedTrap.setStatus(
        "current"
    )

fsVcmContextDeletedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 93, 2, 2)
)
fsVcmContextDeletedTrap.setObjects(
    ("VCM-MIB", "fsVCId")
)
if mibBuilder.loadTexts:
    fsVcmContextDeletedTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VCM-MIB",
    **{"fsVcmMib": fsVcmMib,
       "fsVcmConfig": fsVcmConfig,
       "fsVcmTraceOption": fsVcmTraceOption,
       "fsVcmConfigTable": fsVcmConfigTable,
       "fsVcmConfigEntry": fsVcmConfigEntry,
       "fsVCId": fsVCId,
       "fsVCNextFreeHlPortId": fsVCNextFreeHlPortId,
       "fsVCMacAddress": fsVCMacAddress,
       "fsVcAlias": fsVcAlias,
       "fsVcCxtType": fsVcCxtType,
       "fsVCStatus": fsVCStatus,
       "fsVRMacAddress": fsVRMacAddress,
       "fsVcmIfMappingTable": fsVcmIfMappingTable,
       "fsVcmIfMappingEntry": fsVcmIfMappingEntry,
       "fsVcmIfIndex": fsVcmIfIndex,
       "fsVcId": fsVcId,
       "fsVcHlPortId": fsVcHlPortId,
       "fsVcL2ContextId": fsVcL2ContextId,
       "fsVcIfRowStatus": fsVcIfRowStatus,
       "fsVcmL2CxtAndVlanToIPIfaceMapTable": fsVcmL2CxtAndVlanToIPIfaceMapTable,
       "fsVcmL2CxtAndVlanToIPIfaceMapEntry": fsVcmL2CxtAndVlanToIPIfaceMapEntry,
       "fsVcmL2VcId": fsVcmL2VcId,
       "fsVcmVlanId": fsVcmVlanId,
       "fsVcmL2VcName": fsVcmL2VcName,
       "fsVcmIPIfIndex": fsVcmIPIfIndex,
       "fsVcConfigExtTable": fsVcConfigExtTable,
       "fsVcConfigExtEntry": fsVcConfigExtEntry,
       "fsVcOwner": fsVcOwner,
       "fsVcmFreeVcIdTable": fsVcmFreeVcIdTable,
       "fsVcmFreeVcIdEntry": fsVcmFreeVcIdEntry,
       "fsVcmFreeVcId": fsVcmFreeVcId,
       "fsVcmTraps": fsVcmTraps,
       "fsVcmContextCreatedTrap": fsVcmContextCreatedTrap,
       "fsVcmContextDeletedTrap": fsVcmContextDeletedTrap,
       "fsVcmAppContextConfig": fsVcmAppContextConfig,
       "fsVcmFirmwareUpgradeCxt": fsVcmFirmwareUpgradeCxt,
       "fsVcmFileCopyCxt": fsVcmFileCopyCxt,
       "fsVcmCoredumpPutCxt": fsVcmCoredumpPutCxt,
       "fsVcmSyslogClientCxt": fsVcmSyslogClientCxt,
       "fsVcmSnmpTrapClientCxt": fsVcmSnmpTrapClientCxt,
       "fsVcmSntpClientCxt": fsVcmSntpClientCxt,
       "fsVcmSnmpAgentxCxt": fsVcmSnmpAgentxCxt,
       "fsVcmTacacsClientCxt": fsVcmTacacsClientCxt,
       "fsVcmRadiusClientCxt": fsVcmRadiusClientCxt}
)
