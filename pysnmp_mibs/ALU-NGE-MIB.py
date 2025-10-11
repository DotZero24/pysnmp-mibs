# SNMP MIB module (ALU-NGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/ALU-NGE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:03:41 2025
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

(aluSARConfs,
 aluSARMIBModules,
 aluSARNotifyPrefix,
 aluSARObjs) = mibBuilder.importSymbols(
    "ALU-SAR-GLOBAL-MIB",
    "aluSARConfs",
    "aluSARMIBModules",
    "aluSARNotifyPrefix",
    "aluSARObjs")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")

(tmnxCardSlotNum,
 tmnxChassisIndex,
 tmnxMDASlotNum) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "tmnxCardSlotNum",
    "tmnxChassisIndex",
    "tmnxMDASlotNum")

(TEntryId,
 TFilterID,
 TFilterScope) = mibBuilder.importSymbols(
    "TIMETRA-FILTER-MIB",
    "TEntryId",
    "TFilterID",
    "TFilterScope")

(sdpBindBaseStatsEntry,
 sdpInfoEntry) = mibBuilder.importSymbols(
    "TIMETRA-SDP-MIB",
    "sdpBindBaseStatsEntry",
    "sdpInfoEntry")

(svcBaseInfoEntry,) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "svcBaseInfoEntry")

(IpAddressPrefixLength,
 TIpProtocol,
 TItemDescription,
 TLNamedItemOrEmpty,
 TOperator,
 TTcpUdpPort) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "IpAddressPrefixLength",
    "TIpProtocol",
    "TItemDescription",
    "TLNamedItemOrEmpty",
    "TOperator",
    "TTcpUdpPort")

(vRtrID,
 vRtrIfStatsEntry) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID",
    "vRtrIfStatsEntry")

(tmnxWlanGwSoftGreIfEntry,) = mibBuilder.importSymbols(
    "TIMETRA-WLAN-GW-MIB",
    "tmnxWlanGwSoftGreIfEntry")


# MODULE-IDENTITY

aluNgeMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 1, 3, 18)
)
if mibBuilder.loadTexts:
    aluNgeMIBModule.setRevisions(
        ("2014-07-04 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AluNgeKeygroupId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )



class AluNgeKeygroupIdOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )



class AluNgeAuthAlgorithm(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sha256", 1),
          ("sha512", 2))
    )



class AluNgeEncrAlgorithm(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aes128", 1),
          ("aes256", 2))
    )



class AluNgeKeygroupSpiId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )



class AluNgeKeygroupSpiIdOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )



# MIB Managed Objects in the order of their OIDs

_AluNgeMIBConformance_ObjectIdentity = ObjectIdentity
aluNgeMIBConformance = _AluNgeMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 20)
)
_AluNgeCompliances_ObjectIdentity = ObjectIdentity
aluNgeCompliances = _AluNgeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 20, 1)
)
_AluNgeGroups_ObjectIdentity = ObjectIdentity
aluNgeGroups = _AluNgeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 20, 2)
)
_AluNgeObjs_ObjectIdentity = ObjectIdentity
aluNgeObjs = _AluNgeObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20)
)
_AluNgeSystemObjs_ObjectIdentity = ObjectIdentity
aluNgeSystemObjs = _AluNgeSystemObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 1)
)


class _AluNgeLabel_Type(Unsigned32):
    """Custom type aluNgeLabel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(32, 2047),
    )


_AluNgeLabel_Type.__name__ = "Unsigned32"
_AluNgeLabel_Object = MibScalar
aluNgeLabel = _AluNgeLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 1, 1),
    _AluNgeLabel_Type()
)
aluNgeLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluNgeLabel.setStatus("current")
_AluNgeKeygroupObjs_ObjectIdentity = ObjectIdentity
aluNgeKeygroupObjs = _AluNgeKeygroupObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 2)
)
_AluNgeKeygroupTable_Object = MibTable
aluNgeKeygroupTable = _AluNgeKeygroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 2, 1)
)
if mibBuilder.loadTexts:
    aluNgeKeygroupTable.setStatus("current")
_AluNgeKeygroupEntry_Object = MibTableRow
aluNgeKeygroupEntry = _AluNgeKeygroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 2, 1, 1)
)
aluNgeKeygroupEntry.setIndexNames(
    (0, "ALU-NGE-MIB", "aluNgeKeygroupId"),
)
if mibBuilder.loadTexts:
    aluNgeKeygroupEntry.setStatus("current")
_AluNgeKeygroupId_Type = AluNgeKeygroupId
_AluNgeKeygroupId_Object = MibTableColumn
aluNgeKeygroupId = _AluNgeKeygroupId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 2, 1, 1, 1),
    _AluNgeKeygroupId_Type()
)
aluNgeKeygroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluNgeKeygroupId.setStatus("current")
_AluNgeKeygroupRowStatus_Type = RowStatus
_AluNgeKeygroupRowStatus_Object = MibTableColumn
aluNgeKeygroupRowStatus = _AluNgeKeygroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 2, 1, 1, 2),
    _AluNgeKeygroupRowStatus_Type()
)
aluNgeKeygroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeKeygroupRowStatus.setStatus("current")


class _AluNgeKeygroupDescription_Type(TItemDescription):
    """Custom type aluNgeKeygroupDescription based on TItemDescription"""
    defaultValue = OctetString("")


_AluNgeKeygroupDescription_Type.__name__ = "TItemDescription"
_AluNgeKeygroupDescription_Object = MibTableColumn
aluNgeKeygroupDescription = _AluNgeKeygroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 2, 1, 1, 3),
    _AluNgeKeygroupDescription_Type()
)
aluNgeKeygroupDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeKeygroupDescription.setStatus("current")


class _AluNgeKeygroupAuthAlgorithm_Type(AluNgeAuthAlgorithm):
    """Custom type aluNgeKeygroupAuthAlgorithm based on AluNgeAuthAlgorithm"""
    defaultValue = 1


_AluNgeKeygroupAuthAlgorithm_Type.__name__ = "AluNgeAuthAlgorithm"
_AluNgeKeygroupAuthAlgorithm_Object = MibTableColumn
aluNgeKeygroupAuthAlgorithm = _AluNgeKeygroupAuthAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 2, 1, 1, 4),
    _AluNgeKeygroupAuthAlgorithm_Type()
)
aluNgeKeygroupAuthAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeKeygroupAuthAlgorithm.setStatus("current")


class _AluNgeKeygroupEncrAlgorithm_Type(AluNgeEncrAlgorithm):
    """Custom type aluNgeKeygroupEncrAlgorithm based on AluNgeEncrAlgorithm"""
    defaultValue = 1


_AluNgeKeygroupEncrAlgorithm_Type.__name__ = "AluNgeEncrAlgorithm"
_AluNgeKeygroupEncrAlgorithm_Object = MibTableColumn
aluNgeKeygroupEncrAlgorithm = _AluNgeKeygroupEncrAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 2, 1, 1, 5),
    _AluNgeKeygroupEncrAlgorithm_Type()
)
aluNgeKeygroupEncrAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeKeygroupEncrAlgorithm.setStatus("current")


class _AluNgeKeygroupActiveOutboundSa_Type(AluNgeKeygroupSpiIdOrZero):
    """Custom type aluNgeKeygroupActiveOutboundSa based on AluNgeKeygroupSpiIdOrZero"""
    defaultValue = 0


_AluNgeKeygroupActiveOutboundSa_Type.__name__ = "AluNgeKeygroupSpiIdOrZero"
_AluNgeKeygroupActiveOutboundSa_Object = MibTableColumn
aluNgeKeygroupActiveOutboundSa = _AluNgeKeygroupActiveOutboundSa_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 2, 1, 1, 6),
    _AluNgeKeygroupActiveOutboundSa_Type()
)
aluNgeKeygroupActiveOutboundSa.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeKeygroupActiveOutboundSa.setStatus("current")
_AluNgeKeygroupOutboundSaActivateTime_Type = TimeStamp
_AluNgeKeygroupOutboundSaActivateTime_Object = MibTableColumn
aluNgeKeygroupOutboundSaActivateTime = _AluNgeKeygroupOutboundSaActivateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 2, 1, 1, 7),
    _AluNgeKeygroupOutboundSaActivateTime_Type()
)
aluNgeKeygroupOutboundSaActivateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupOutboundSaActivateTime.setStatus("current")


class _AluNgeKeygroupName_Type(TLNamedItemOrEmpty):
    """Custom type aluNgeKeygroupName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_AluNgeKeygroupName_Type.__name__ = "TLNamedItemOrEmpty"
_AluNgeKeygroupName_Object = MibTableColumn
aluNgeKeygroupName = _AluNgeKeygroupName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 2, 1, 1, 8),
    _AluNgeKeygroupName_Type()
)
aluNgeKeygroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeKeygroupName.setStatus("current")
_AluNgeKeygroupSpiObjs_ObjectIdentity = ObjectIdentity
aluNgeKeygroupSpiObjs = _AluNgeKeygroupSpiObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 3)
)
_AluNgeKeygroupSpiTable_Object = MibTable
aluNgeKeygroupSpiTable = _AluNgeKeygroupSpiTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 3, 1)
)
if mibBuilder.loadTexts:
    aluNgeKeygroupSpiTable.setStatus("current")
_AluNgeKeygroupSpiEntry_Object = MibTableRow
aluNgeKeygroupSpiEntry = _AluNgeKeygroupSpiEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 3, 1, 1)
)
aluNgeKeygroupSpiEntry.setIndexNames(
    (0, "ALU-NGE-MIB", "aluNgeKeygroupId"),
    (0, "ALU-NGE-MIB", "aluNgeKeygroupSpiId"),
)
if mibBuilder.loadTexts:
    aluNgeKeygroupSpiEntry.setStatus("current")
_AluNgeKeygroupSpiId_Type = AluNgeKeygroupSpiId
_AluNgeKeygroupSpiId_Object = MibTableColumn
aluNgeKeygroupSpiId = _AluNgeKeygroupSpiId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 3, 1, 1, 1),
    _AluNgeKeygroupSpiId_Type()
)
aluNgeKeygroupSpiId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluNgeKeygroupSpiId.setStatus("current")
_AluNgeKeygroupSpiRowStatus_Type = RowStatus
_AluNgeKeygroupSpiRowStatus_Object = MibTableColumn
aluNgeKeygroupSpiRowStatus = _AluNgeKeygroupSpiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 3, 1, 1, 2),
    _AluNgeKeygroupSpiRowStatus_Type()
)
aluNgeKeygroupSpiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeKeygroupSpiRowStatus.setStatus("current")


class _AluNgeKeygroupSpiAuthKey_Type(OctetString):
    """Custom type aluNgeKeygroupSpiAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AluNgeKeygroupSpiAuthKey_Type.__name__ = "OctetString"
_AluNgeKeygroupSpiAuthKey_Object = MibTableColumn
aluNgeKeygroupSpiAuthKey = _AluNgeKeygroupSpiAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 3, 1, 1, 3),
    _AluNgeKeygroupSpiAuthKey_Type()
)
aluNgeKeygroupSpiAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeKeygroupSpiAuthKey.setStatus("current")


class _AluNgeKeygroupSpiEncrKey_Type(OctetString):
    """Custom type aluNgeKeygroupSpiEncrKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AluNgeKeygroupSpiEncrKey_Type.__name__ = "OctetString"
_AluNgeKeygroupSpiEncrKey_Object = MibTableColumn
aluNgeKeygroupSpiEncrKey = _AluNgeKeygroupSpiEncrKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 3, 1, 1, 4),
    _AluNgeKeygroupSpiEncrKey_Type()
)
aluNgeKeygroupSpiEncrKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeKeygroupSpiEncrKey.setStatus("current")
_AluNgeKeygroupSpiInstallTime_Type = TimeStamp
_AluNgeKeygroupSpiInstallTime_Object = MibTableColumn
aluNgeKeygroupSpiInstallTime = _AluNgeKeygroupSpiInstallTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 3, 1, 1, 5),
    _AluNgeKeygroupSpiInstallTime_Type()
)
aluNgeKeygroupSpiInstallTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupSpiInstallTime.setStatus("current")
_AluNgeKeygroupSpiKeyCRC_Type = Unsigned32
_AluNgeKeygroupSpiKeyCRC_Object = MibTableColumn
aluNgeKeygroupSpiKeyCRC = _AluNgeKeygroupSpiKeyCRC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 3, 1, 1, 6),
    _AluNgeKeygroupSpiKeyCRC_Type()
)
aluNgeKeygroupSpiKeyCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupSpiKeyCRC.setStatus("current")
_AluNgeKeygroupSdpBindingObjs_ObjectIdentity = ObjectIdentity
aluNgeKeygroupSdpBindingObjs = _AluNgeKeygroupSdpBindingObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 4)
)
_AluNgeKeygroupSdpBindingTable_Object = MibTable
aluNgeKeygroupSdpBindingTable = _AluNgeKeygroupSdpBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 4, 1)
)
if mibBuilder.loadTexts:
    aluNgeKeygroupSdpBindingTable.setStatus("current")
_AluNgeKeygroupSdpBindingEntry_Object = MibTableRow
aluNgeKeygroupSdpBindingEntry = _AluNgeKeygroupSdpBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 4, 1, 1)
)
if mibBuilder.loadTexts:
    aluNgeKeygroupSdpBindingEntry.setStatus("current")


class _AluNgeKeygroupSdpBindingInbound_Type(AluNgeKeygroupIdOrZero):
    """Custom type aluNgeKeygroupSdpBindingInbound based on AluNgeKeygroupIdOrZero"""
    defaultValue = 0


_AluNgeKeygroupSdpBindingInbound_Type.__name__ = "AluNgeKeygroupIdOrZero"
_AluNgeKeygroupSdpBindingInbound_Object = MibTableColumn
aluNgeKeygroupSdpBindingInbound = _AluNgeKeygroupSdpBindingInbound_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 4, 1, 1, 1),
    _AluNgeKeygroupSdpBindingInbound_Type()
)
aluNgeKeygroupSdpBindingInbound.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeKeygroupSdpBindingInbound.setStatus("current")


class _AluNgeKeygroupSdpBindingOutbound_Type(AluNgeKeygroupIdOrZero):
    """Custom type aluNgeKeygroupSdpBindingOutbound based on AluNgeKeygroupIdOrZero"""
    defaultValue = 0


_AluNgeKeygroupSdpBindingOutbound_Type.__name__ = "AluNgeKeygroupIdOrZero"
_AluNgeKeygroupSdpBindingOutbound_Object = MibTableColumn
aluNgeKeygroupSdpBindingOutbound = _AluNgeKeygroupSdpBindingOutbound_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 4, 1, 1, 2),
    _AluNgeKeygroupSdpBindingOutbound_Type()
)
aluNgeKeygroupSdpBindingOutbound.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeKeygroupSdpBindingOutbound.setStatus("current")
_AluNgeKeygroupVrfBindingObjs_ObjectIdentity = ObjectIdentity
aluNgeKeygroupVrfBindingObjs = _AluNgeKeygroupVrfBindingObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 5)
)
_AluNgeKeygroupVrfBindingTable_Object = MibTable
aluNgeKeygroupVrfBindingTable = _AluNgeKeygroupVrfBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 5, 1)
)
if mibBuilder.loadTexts:
    aluNgeKeygroupVrfBindingTable.setStatus("current")
_AluNgeKeygroupVrfBindingEntry_Object = MibTableRow
aluNgeKeygroupVrfBindingEntry = _AluNgeKeygroupVrfBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 5, 1, 1)
)
if mibBuilder.loadTexts:
    aluNgeKeygroupVrfBindingEntry.setStatus("current")


class _AluNgeKeygroupVrfBindingInbound_Type(AluNgeKeygroupIdOrZero):
    """Custom type aluNgeKeygroupVrfBindingInbound based on AluNgeKeygroupIdOrZero"""
    defaultValue = 0


_AluNgeKeygroupVrfBindingInbound_Type.__name__ = "AluNgeKeygroupIdOrZero"
_AluNgeKeygroupVrfBindingInbound_Object = MibTableColumn
aluNgeKeygroupVrfBindingInbound = _AluNgeKeygroupVrfBindingInbound_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 5, 1, 1, 1),
    _AluNgeKeygroupVrfBindingInbound_Type()
)
aluNgeKeygroupVrfBindingInbound.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeKeygroupVrfBindingInbound.setStatus("current")


class _AluNgeKeygroupVrfBindingOutbound_Type(AluNgeKeygroupIdOrZero):
    """Custom type aluNgeKeygroupVrfBindingOutbound based on AluNgeKeygroupIdOrZero"""
    defaultValue = 0


_AluNgeKeygroupVrfBindingOutbound_Type.__name__ = "AluNgeKeygroupIdOrZero"
_AluNgeKeygroupVrfBindingOutbound_Object = MibTableColumn
aluNgeKeygroupVrfBindingOutbound = _AluNgeKeygroupVrfBindingOutbound_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 5, 1, 1, 2),
    _AluNgeKeygroupVrfBindingOutbound_Type()
)
aluNgeKeygroupVrfBindingOutbound.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeKeygroupVrfBindingOutbound.setStatus("current")
_AluNgeStatsObjs_ObjectIdentity = ObjectIdentity
aluNgeStatsObjs = _AluNgeStatsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6)
)
_AluNgeMdaStatsTable_Object = MibTable
aluNgeMdaStatsTable = _AluNgeMdaStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 1)
)
if mibBuilder.loadTexts:
    aluNgeMdaStatsTable.setStatus("current")
_AluNgeMdaStatsEntry_Object = MibTableRow
aluNgeMdaStatsEntry = _AluNgeMdaStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 1, 1)
)
aluNgeMdaStatsEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
)
if mibBuilder.loadTexts:
    aluNgeMdaStatsEntry.setStatus("current")
_AluNgeMdaEncryptPkts_Type = Counter64
_AluNgeMdaEncryptPkts_Object = MibTableColumn
aluNgeMdaEncryptPkts = _AluNgeMdaEncryptPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 1, 1, 1),
    _AluNgeMdaEncryptPkts_Type()
)
aluNgeMdaEncryptPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeMdaEncryptPkts.setStatus("current")
_AluNgeMdaEncryptBytes_Type = Counter64
_AluNgeMdaEncryptBytes_Object = MibTableColumn
aluNgeMdaEncryptBytes = _AluNgeMdaEncryptBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 1, 1, 2),
    _AluNgeMdaEncryptBytes_Type()
)
aluNgeMdaEncryptBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeMdaEncryptBytes.setStatus("current")
_AluNgeMdaDecryptPkts_Type = Counter64
_AluNgeMdaDecryptPkts_Object = MibTableColumn
aluNgeMdaDecryptPkts = _AluNgeMdaDecryptPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 1, 1, 3),
    _AluNgeMdaDecryptPkts_Type()
)
aluNgeMdaDecryptPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeMdaDecryptPkts.setStatus("current")
_AluNgeMdaDecryptBytes_Type = Counter64
_AluNgeMdaDecryptBytes_Object = MibTableColumn
aluNgeMdaDecryptBytes = _AluNgeMdaDecryptBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 1, 1, 4),
    _AluNgeMdaDecryptBytes_Type()
)
aluNgeMdaDecryptBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeMdaDecryptBytes.setStatus("current")
_AluNgeMdaOutDropPkts_Type = Counter32
_AluNgeMdaOutDropPkts_Object = MibTableColumn
aluNgeMdaOutDropPkts = _AluNgeMdaOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 1, 1, 5),
    _AluNgeMdaOutDropPkts_Type()
)
aluNgeMdaOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeMdaOutDropPkts.setStatus("current")
_AluNgeMdaOutDropUnsupportedUplink_Type = Counter32
_AluNgeMdaOutDropUnsupportedUplink_Object = MibTableColumn
aluNgeMdaOutDropUnsupportedUplink = _AluNgeMdaOutDropUnsupportedUplink_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 1, 1, 6),
    _AluNgeMdaOutDropUnsupportedUplink_Type()
)
aluNgeMdaOutDropUnsupportedUplink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeMdaOutDropUnsupportedUplink.setStatus("current")
_AluNgeMdaOutDropEnqueueError_Type = Counter32
_AluNgeMdaOutDropEnqueueError_Object = MibTableColumn
aluNgeMdaOutDropEnqueueError = _AluNgeMdaOutDropEnqueueError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 1, 1, 7),
    _AluNgeMdaOutDropEnqueueError_Type()
)
aluNgeMdaOutDropEnqueueError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeMdaOutDropEnqueueError.setStatus("current")
_AluNgeMdaInDropPkts_Type = Counter32
_AluNgeMdaInDropPkts_Object = MibTableColumn
aluNgeMdaInDropPkts = _AluNgeMdaInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 1, 1, 8),
    _AluNgeMdaInDropPkts_Type()
)
aluNgeMdaInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeMdaInDropPkts.setStatus("current")
_AluNgeMdaInDropInvalidSpi_Type = Counter32
_AluNgeMdaInDropInvalidSpi_Object = MibTableColumn
aluNgeMdaInDropInvalidSpi = _AluNgeMdaInDropInvalidSpi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 1, 1, 9),
    _AluNgeMdaInDropInvalidSpi_Type()
)
aluNgeMdaInDropInvalidSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeMdaInDropInvalidSpi.setStatus("current")
_AluNgeMdaInDropAuthFailure_Type = Counter32
_AluNgeMdaInDropAuthFailure_Object = MibTableColumn
aluNgeMdaInDropAuthFailure = _AluNgeMdaInDropAuthFailure_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 1, 1, 10),
    _AluNgeMdaInDropAuthFailure_Type()
)
aluNgeMdaInDropAuthFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeMdaInDropAuthFailure.setStatus("current")
_AluNgeMdaInDropPaddingFailure_Type = Counter32
_AluNgeMdaInDropPaddingFailure_Object = MibTableColumn
aluNgeMdaInDropPaddingFailure = _AluNgeMdaInDropPaddingFailure_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 1, 1, 11),
    _AluNgeMdaInDropPaddingFailure_Type()
)
aluNgeMdaInDropPaddingFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeMdaInDropPaddingFailure.setStatus("current")
_AluNgeMdaInDropEnqueueError_Type = Counter32
_AluNgeMdaInDropEnqueueError_Object = MibTableColumn
aluNgeMdaInDropEnqueueError = _AluNgeMdaInDropEnqueueError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 1, 1, 12),
    _AluNgeMdaInDropEnqueueError_Type()
)
aluNgeMdaInDropEnqueueError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeMdaInDropEnqueueError.setStatus("current")
_AluNgeMdaInDropControlWordMismatch_Type = Counter32
_AluNgeMdaInDropControlWordMismatch_Object = MibTableColumn
aluNgeMdaInDropControlWordMismatch = _AluNgeMdaInDropControlWordMismatch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 1, 1, 13),
    _AluNgeMdaInDropControlWordMismatch_Type()
)
aluNgeMdaInDropControlWordMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeMdaInDropControlWordMismatch.setStatus("current")
_AluNgeKeygroupStatsTable_Object = MibTable
aluNgeKeygroupStatsTable = _AluNgeKeygroupStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 2)
)
if mibBuilder.loadTexts:
    aluNgeKeygroupStatsTable.setStatus("current")
_AluNgeKeygroupStatsEntry_Object = MibTableRow
aluNgeKeygroupStatsEntry = _AluNgeKeygroupStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 2, 1)
)
aluNgeKeygroupStatsEntry.setIndexNames(
    (0, "ALU-NGE-MIB", "aluNgeKeygroupId"),
)
if mibBuilder.loadTexts:
    aluNgeKeygroupStatsEntry.setStatus("current")
_AluNgeKeygroupEncryptPkts_Type = Counter64
_AluNgeKeygroupEncryptPkts_Object = MibTableColumn
aluNgeKeygroupEncryptPkts = _AluNgeKeygroupEncryptPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 2, 1, 1),
    _AluNgeKeygroupEncryptPkts_Type()
)
aluNgeKeygroupEncryptPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupEncryptPkts.setStatus("current")
_AluNgeKeygroupEncryptBytes_Type = Counter64
_AluNgeKeygroupEncryptBytes_Object = MibTableColumn
aluNgeKeygroupEncryptBytes = _AluNgeKeygroupEncryptBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 2, 1, 2),
    _AluNgeKeygroupEncryptBytes_Type()
)
aluNgeKeygroupEncryptBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupEncryptBytes.setStatus("current")
_AluNgeKeygroupDecryptPkts_Type = Counter64
_AluNgeKeygroupDecryptPkts_Object = MibTableColumn
aluNgeKeygroupDecryptPkts = _AluNgeKeygroupDecryptPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 2, 1, 3),
    _AluNgeKeygroupDecryptPkts_Type()
)
aluNgeKeygroupDecryptPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupDecryptPkts.setStatus("current")
_AluNgeKeygroupDecryptBytes_Type = Counter64
_AluNgeKeygroupDecryptBytes_Object = MibTableColumn
aluNgeKeygroupDecryptBytes = _AluNgeKeygroupDecryptBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 2, 1, 4),
    _AluNgeKeygroupDecryptBytes_Type()
)
aluNgeKeygroupDecryptBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupDecryptBytes.setStatus("current")
_AluNgeKeygroupOutDropPkts_Type = Counter32
_AluNgeKeygroupOutDropPkts_Object = MibTableColumn
aluNgeKeygroupOutDropPkts = _AluNgeKeygroupOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 2, 1, 5),
    _AluNgeKeygroupOutDropPkts_Type()
)
aluNgeKeygroupOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupOutDropPkts.setStatus("current")
_AluNgeKeygroupOutDropUnsupportedUplink_Type = Counter32
_AluNgeKeygroupOutDropUnsupportedUplink_Object = MibTableColumn
aluNgeKeygroupOutDropUnsupportedUplink = _AluNgeKeygroupOutDropUnsupportedUplink_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 2, 1, 6),
    _AluNgeKeygroupOutDropUnsupportedUplink_Type()
)
aluNgeKeygroupOutDropUnsupportedUplink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupOutDropUnsupportedUplink.setStatus("current")
_AluNgeKeygroupOutDropEnqueueError_Type = Counter32
_AluNgeKeygroupOutDropEnqueueError_Object = MibTableColumn
aluNgeKeygroupOutDropEnqueueError = _AluNgeKeygroupOutDropEnqueueError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 2, 1, 7),
    _AluNgeKeygroupOutDropEnqueueError_Type()
)
aluNgeKeygroupOutDropEnqueueError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupOutDropEnqueueError.setStatus("current")
_AluNgeKeygroupOutDropOther_Type = Counter32
_AluNgeKeygroupOutDropOther_Object = MibTableColumn
aluNgeKeygroupOutDropOther = _AluNgeKeygroupOutDropOther_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 2, 1, 8),
    _AluNgeKeygroupOutDropOther_Type()
)
aluNgeKeygroupOutDropOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupOutDropOther.setStatus("current")
_AluNgeKeygroupInDropPkts_Type = Counter32
_AluNgeKeygroupInDropPkts_Object = MibTableColumn
aluNgeKeygroupInDropPkts = _AluNgeKeygroupInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 2, 1, 9),
    _AluNgeKeygroupInDropPkts_Type()
)
aluNgeKeygroupInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupInDropPkts.setStatus("current")
_AluNgeKeygroupInDropInvalidSpi_Type = Counter32
_AluNgeKeygroupInDropInvalidSpi_Object = MibTableColumn
aluNgeKeygroupInDropInvalidSpi = _AluNgeKeygroupInDropInvalidSpi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 2, 1, 10),
    _AluNgeKeygroupInDropInvalidSpi_Type()
)
aluNgeKeygroupInDropInvalidSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupInDropInvalidSpi.setStatus("current")
_AluNgeKeygroupInDropAuthFailure_Type = Counter32
_AluNgeKeygroupInDropAuthFailure_Object = MibTableColumn
aluNgeKeygroupInDropAuthFailure = _AluNgeKeygroupInDropAuthFailure_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 2, 1, 11),
    _AluNgeKeygroupInDropAuthFailure_Type()
)
aluNgeKeygroupInDropAuthFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupInDropAuthFailure.setStatus("current")
_AluNgeKeygroupInDropPaddingFailure_Type = Counter32
_AluNgeKeygroupInDropPaddingFailure_Object = MibTableColumn
aluNgeKeygroupInDropPaddingFailure = _AluNgeKeygroupInDropPaddingFailure_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 2, 1, 12),
    _AluNgeKeygroupInDropPaddingFailure_Type()
)
aluNgeKeygroupInDropPaddingFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupInDropPaddingFailure.setStatus("current")
_AluNgeKeygroupInDropEnqueueError_Type = Counter32
_AluNgeKeygroupInDropEnqueueError_Object = MibTableColumn
aluNgeKeygroupInDropEnqueueError = _AluNgeKeygroupInDropEnqueueError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 2, 1, 13),
    _AluNgeKeygroupInDropEnqueueError_Type()
)
aluNgeKeygroupInDropEnqueueError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupInDropEnqueueError.setStatus("current")
_AluNgeKeygroupInDropControlWordMismatch_Type = Counter32
_AluNgeKeygroupInDropControlWordMismatch_Object = MibTableColumn
aluNgeKeygroupInDropControlWordMismatch = _AluNgeKeygroupInDropControlWordMismatch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 2, 1, 14),
    _AluNgeKeygroupInDropControlWordMismatch_Type()
)
aluNgeKeygroupInDropControlWordMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupInDropControlWordMismatch.setStatus("current")
_AluNgeKeygroupInDropOther_Type = Counter32
_AluNgeKeygroupInDropOther_Object = MibTableColumn
aluNgeKeygroupInDropOther = _AluNgeKeygroupInDropOther_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 2, 1, 15),
    _AluNgeKeygroupInDropOther_Type()
)
aluNgeKeygroupInDropOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupInDropOther.setStatus("current")
_AluNgeKeygroupInLastDropSpi_Type = Unsigned32
_AluNgeKeygroupInLastDropSpi_Object = MibTableColumn
aluNgeKeygroupInLastDropSpi = _AluNgeKeygroupInLastDropSpi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 2, 1, 16),
    _AluNgeKeygroupInLastDropSpi_Type()
)
aluNgeKeygroupInLastDropSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupInLastDropSpi.setStatus("current")
_AluNgeKeygroupSpiStatsTable_Object = MibTable
aluNgeKeygroupSpiStatsTable = _AluNgeKeygroupSpiStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 3)
)
if mibBuilder.loadTexts:
    aluNgeKeygroupSpiStatsTable.setStatus("current")
_AluNgeKeygroupSpiStatsEntry_Object = MibTableRow
aluNgeKeygroupSpiStatsEntry = _AluNgeKeygroupSpiStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 3, 1)
)
aluNgeKeygroupSpiStatsEntry.setIndexNames(
    (0, "ALU-NGE-MIB", "aluNgeKeygroupId"),
    (0, "ALU-NGE-MIB", "aluNgeKeygroupSpiId"),
)
if mibBuilder.loadTexts:
    aluNgeKeygroupSpiStatsEntry.setStatus("current")
_AluNgeKeygroupSpiEncryptPkts_Type = Counter64
_AluNgeKeygroupSpiEncryptPkts_Object = MibTableColumn
aluNgeKeygroupSpiEncryptPkts = _AluNgeKeygroupSpiEncryptPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 3, 1, 1),
    _AluNgeKeygroupSpiEncryptPkts_Type()
)
aluNgeKeygroupSpiEncryptPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupSpiEncryptPkts.setStatus("current")
_AluNgeKeygroupSpiEncryptBytes_Type = Counter64
_AluNgeKeygroupSpiEncryptBytes_Object = MibTableColumn
aluNgeKeygroupSpiEncryptBytes = _AluNgeKeygroupSpiEncryptBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 3, 1, 2),
    _AluNgeKeygroupSpiEncryptBytes_Type()
)
aluNgeKeygroupSpiEncryptBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupSpiEncryptBytes.setStatus("current")
_AluNgeKeygroupSpiDecryptPkts_Type = Counter64
_AluNgeKeygroupSpiDecryptPkts_Object = MibTableColumn
aluNgeKeygroupSpiDecryptPkts = _AluNgeKeygroupSpiDecryptPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 3, 1, 3),
    _AluNgeKeygroupSpiDecryptPkts_Type()
)
aluNgeKeygroupSpiDecryptPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupSpiDecryptPkts.setStatus("current")
_AluNgeKeygroupSpiDecryptBytes_Type = Counter64
_AluNgeKeygroupSpiDecryptBytes_Object = MibTableColumn
aluNgeKeygroupSpiDecryptBytes = _AluNgeKeygroupSpiDecryptBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 3, 1, 4),
    _AluNgeKeygroupSpiDecryptBytes_Type()
)
aluNgeKeygroupSpiDecryptBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupSpiDecryptBytes.setStatus("current")
_AluNgeKeygroupSpiOutDropPkts_Type = Counter32
_AluNgeKeygroupSpiOutDropPkts_Object = MibTableColumn
aluNgeKeygroupSpiOutDropPkts = _AluNgeKeygroupSpiOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 3, 1, 5),
    _AluNgeKeygroupSpiOutDropPkts_Type()
)
aluNgeKeygroupSpiOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupSpiOutDropPkts.setStatus("current")
_AluNgeKeygroupSpiOutDropEnqueueError_Type = Counter32
_AluNgeKeygroupSpiOutDropEnqueueError_Object = MibTableColumn
aluNgeKeygroupSpiOutDropEnqueueError = _AluNgeKeygroupSpiOutDropEnqueueError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 3, 1, 6),
    _AluNgeKeygroupSpiOutDropEnqueueError_Type()
)
aluNgeKeygroupSpiOutDropEnqueueError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupSpiOutDropEnqueueError.setStatus("current")
_AluNgeKeygroupSpiOutDropOther_Type = Counter32
_AluNgeKeygroupSpiOutDropOther_Object = MibTableColumn
aluNgeKeygroupSpiOutDropOther = _AluNgeKeygroupSpiOutDropOther_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 3, 1, 7),
    _AluNgeKeygroupSpiOutDropOther_Type()
)
aluNgeKeygroupSpiOutDropOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupSpiOutDropOther.setStatus("current")
_AluNgeKeygroupSpiInDropPkts_Type = Counter32
_AluNgeKeygroupSpiInDropPkts_Object = MibTableColumn
aluNgeKeygroupSpiInDropPkts = _AluNgeKeygroupSpiInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 3, 1, 8),
    _AluNgeKeygroupSpiInDropPkts_Type()
)
aluNgeKeygroupSpiInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupSpiInDropPkts.setStatus("current")
_AluNgeKeygroupSpiInDropAuthFailure_Type = Counter32
_AluNgeKeygroupSpiInDropAuthFailure_Object = MibTableColumn
aluNgeKeygroupSpiInDropAuthFailure = _AluNgeKeygroupSpiInDropAuthFailure_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 3, 1, 9),
    _AluNgeKeygroupSpiInDropAuthFailure_Type()
)
aluNgeKeygroupSpiInDropAuthFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupSpiInDropAuthFailure.setStatus("current")
_AluNgeKeygroupSpiInDropPaddingFailure_Type = Counter32
_AluNgeKeygroupSpiInDropPaddingFailure_Object = MibTableColumn
aluNgeKeygroupSpiInDropPaddingFailure = _AluNgeKeygroupSpiInDropPaddingFailure_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 3, 1, 10),
    _AluNgeKeygroupSpiInDropPaddingFailure_Type()
)
aluNgeKeygroupSpiInDropPaddingFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupSpiInDropPaddingFailure.setStatus("current")
_AluNgeKeygroupSpiInDropEnqueueError_Type = Counter32
_AluNgeKeygroupSpiInDropEnqueueError_Object = MibTableColumn
aluNgeKeygroupSpiInDropEnqueueError = _AluNgeKeygroupSpiInDropEnqueueError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 3, 1, 11),
    _AluNgeKeygroupSpiInDropEnqueueError_Type()
)
aluNgeKeygroupSpiInDropEnqueueError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupSpiInDropEnqueueError.setStatus("current")
_AluNgeKeygroupSpiInDropControlWordMismatch_Type = Counter32
_AluNgeKeygroupSpiInDropControlWordMismatch_Object = MibTableColumn
aluNgeKeygroupSpiInDropControlWordMismatch = _AluNgeKeygroupSpiInDropControlWordMismatch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 3, 1, 12),
    _AluNgeKeygroupSpiInDropControlWordMismatch_Type()
)
aluNgeKeygroupSpiInDropControlWordMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupSpiInDropControlWordMismatch.setStatus("current")
_AluNgeKeygroupSpiInDropOther_Type = Counter32
_AluNgeKeygroupSpiInDropOther_Object = MibTableColumn
aluNgeKeygroupSpiInDropOther = _AluNgeKeygroupSpiInDropOther_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 3, 1, 13),
    _AluNgeKeygroupSpiInDropOther_Type()
)
aluNgeKeygroupSpiInDropOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupSpiInDropOther.setStatus("current")
_AluNgeKeygroupSdpBindStatsTable_Object = MibTable
aluNgeKeygroupSdpBindStatsTable = _AluNgeKeygroupSdpBindStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 4)
)
if mibBuilder.loadTexts:
    aluNgeKeygroupSdpBindStatsTable.setStatus("current")
_AluNgeKeygroupSdpBindStatsEntry_Object = MibTableRow
aluNgeKeygroupSdpBindStatsEntry = _AluNgeKeygroupSdpBindStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 4, 1)
)
if mibBuilder.loadTexts:
    aluNgeKeygroupSdpBindStatsEntry.setStatus("current")
_AluNgeKeygroupSdpBindEncryptPkts_Type = Counter64
_AluNgeKeygroupSdpBindEncryptPkts_Object = MibTableColumn
aluNgeKeygroupSdpBindEncryptPkts = _AluNgeKeygroupSdpBindEncryptPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 4, 1, 1),
    _AluNgeKeygroupSdpBindEncryptPkts_Type()
)
aluNgeKeygroupSdpBindEncryptPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupSdpBindEncryptPkts.setStatus("current")
_AluNgeKeygroupSdpBindEncryptBytes_Type = Counter64
_AluNgeKeygroupSdpBindEncryptBytes_Object = MibTableColumn
aluNgeKeygroupSdpBindEncryptBytes = _AluNgeKeygroupSdpBindEncryptBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 4, 1, 2),
    _AluNgeKeygroupSdpBindEncryptBytes_Type()
)
aluNgeKeygroupSdpBindEncryptBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupSdpBindEncryptBytes.setStatus("current")
_AluNgeKeygroupSdpBindDecryptPkts_Type = Counter64
_AluNgeKeygroupSdpBindDecryptPkts_Object = MibTableColumn
aluNgeKeygroupSdpBindDecryptPkts = _AluNgeKeygroupSdpBindDecryptPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 4, 1, 3),
    _AluNgeKeygroupSdpBindDecryptPkts_Type()
)
aluNgeKeygroupSdpBindDecryptPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupSdpBindDecryptPkts.setStatus("current")
_AluNgeKeygroupSdpBindDecryptBytes_Type = Counter64
_AluNgeKeygroupSdpBindDecryptBytes_Object = MibTableColumn
aluNgeKeygroupSdpBindDecryptBytes = _AluNgeKeygroupSdpBindDecryptBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 4, 1, 4),
    _AluNgeKeygroupSdpBindDecryptBytes_Type()
)
aluNgeKeygroupSdpBindDecryptBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupSdpBindDecryptBytes.setStatus("current")
_AluNgeKeygroupSdpBindIngDropOtherPkts_Type = Counter32
_AluNgeKeygroupSdpBindIngDropOtherPkts_Object = MibTableColumn
aluNgeKeygroupSdpBindIngDropOtherPkts = _AluNgeKeygroupSdpBindIngDropOtherPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 4, 1, 5),
    _AluNgeKeygroupSdpBindIngDropOtherPkts_Type()
)
aluNgeKeygroupSdpBindIngDropOtherPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupSdpBindIngDropOtherPkts.setStatus("current")
_AluNgeKeygroupSdpBindEgDropPkts_Type = Counter32
_AluNgeKeygroupSdpBindEgDropPkts_Object = MibTableColumn
aluNgeKeygroupSdpBindEgDropPkts = _AluNgeKeygroupSdpBindEgDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 4, 1, 6),
    _AluNgeKeygroupSdpBindEgDropPkts_Type()
)
aluNgeKeygroupSdpBindEgDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupSdpBindEgDropPkts.setStatus("current")
_AluNgeKeygroupSdpBindIngDropInvalidSpi_Type = Counter32
_AluNgeKeygroupSdpBindIngDropInvalidSpi_Object = MibTableColumn
aluNgeKeygroupSdpBindIngDropInvalidSpi = _AluNgeKeygroupSdpBindIngDropInvalidSpi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 6, 4, 1, 7),
    _AluNgeKeygroupSdpBindIngDropInvalidSpi_Type()
)
aluNgeKeygroupSdpBindIngDropInvalidSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupSdpBindIngDropInvalidSpi.setStatus("current")
_AluNgeKeygroupNameObjs_ObjectIdentity = ObjectIdentity
aluNgeKeygroupNameObjs = _AluNgeKeygroupNameObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 7)
)
_AluNgeKeygroupNameTable_Object = MibTable
aluNgeKeygroupNameTable = _AluNgeKeygroupNameTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 7, 1)
)
if mibBuilder.loadTexts:
    aluNgeKeygroupNameTable.setStatus("current")
_AluNgeKeygroupNameEntry_Object = MibTableRow
aluNgeKeygroupNameEntry = _AluNgeKeygroupNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 7, 1, 1)
)
aluNgeKeygroupNameEntry.setIndexNames(
    (0, "ALU-NGE-MIB", "aluNgeKeygroupName"),
)
if mibBuilder.loadTexts:
    aluNgeKeygroupNameEntry.setStatus("current")
_AluNgeKeygroupNameId_Type = AluNgeKeygroupId
_AluNgeKeygroupNameId_Object = MibTableColumn
aluNgeKeygroupNameId = _AluNgeKeygroupNameId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 7, 1, 1, 1),
    _AluNgeKeygroupNameId_Type()
)
aluNgeKeygroupNameId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupNameId.setStatus("current")
_AluNgeKeygroupNameRowStatus_Type = RowStatus
_AluNgeKeygroupNameRowStatus_Object = MibTableColumn
aluNgeKeygroupNameRowStatus = _AluNgeKeygroupNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 7, 1, 1, 2),
    _AluNgeKeygroupNameRowStatus_Type()
)
aluNgeKeygroupNameRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeKeygroupNameRowStatus.setStatus("current")
_AluNgeNotifyObjs_ObjectIdentity = ObjectIdentity
aluNgeNotifyObjs = _AluNgeNotifyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 8)
)
_AluNgeKeygroupRIBindingObjs_ObjectIdentity = ObjectIdentity
aluNgeKeygroupRIBindingObjs = _AluNgeKeygroupRIBindingObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 9)
)
_AluNgeKeygroupRIBindingTable_Object = MibTable
aluNgeKeygroupRIBindingTable = _AluNgeKeygroupRIBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 9, 1)
)
if mibBuilder.loadTexts:
    aluNgeKeygroupRIBindingTable.setStatus("current")
_AluNgeKeygroupRIBindingEntry_Object = MibTableRow
aluNgeKeygroupRIBindingEntry = _AluNgeKeygroupRIBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 9, 1, 1)
)
aluNgeKeygroupRIBindingEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALU-NGE-MIB", "aluNgeKeygroupRIBindingIfIndex"),
)
if mibBuilder.loadTexts:
    aluNgeKeygroupRIBindingEntry.setStatus("current")
_AluNgeKeygroupRIBindingIfIndex_Type = InterfaceIndex
_AluNgeKeygroupRIBindingIfIndex_Object = MibTableColumn
aluNgeKeygroupRIBindingIfIndex = _AluNgeKeygroupRIBindingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 9, 1, 1, 1),
    _AluNgeKeygroupRIBindingIfIndex_Type()
)
aluNgeKeygroupRIBindingIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluNgeKeygroupRIBindingIfIndex.setStatus("current")
_AluNgeKeygroupRIBindingRowStatus_Type = RowStatus
_AluNgeKeygroupRIBindingRowStatus_Object = MibTableColumn
aluNgeKeygroupRIBindingRowStatus = _AluNgeKeygroupRIBindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 9, 1, 1, 2),
    _AluNgeKeygroupRIBindingRowStatus_Type()
)
aluNgeKeygroupRIBindingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeKeygroupRIBindingRowStatus.setStatus("current")


class _AluNgeKeygroupRIBindingInbound_Type(AluNgeKeygroupIdOrZero):
    """Custom type aluNgeKeygroupRIBindingInbound based on AluNgeKeygroupIdOrZero"""
    defaultValue = 0


_AluNgeKeygroupRIBindingInbound_Type.__name__ = "AluNgeKeygroupIdOrZero"
_AluNgeKeygroupRIBindingInbound_Object = MibTableColumn
aluNgeKeygroupRIBindingInbound = _AluNgeKeygroupRIBindingInbound_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 9, 1, 1, 3),
    _AluNgeKeygroupRIBindingInbound_Type()
)
aluNgeKeygroupRIBindingInbound.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeKeygroupRIBindingInbound.setStatus("current")


class _AluNgeKeygroupRIBindingOutbound_Type(AluNgeKeygroupIdOrZero):
    """Custom type aluNgeKeygroupRIBindingOutbound based on AluNgeKeygroupIdOrZero"""
    defaultValue = 0


_AluNgeKeygroupRIBindingOutbound_Type.__name__ = "AluNgeKeygroupIdOrZero"
_AluNgeKeygroupRIBindingOutbound_Object = MibTableColumn
aluNgeKeygroupRIBindingOutbound = _AluNgeKeygroupRIBindingOutbound_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 9, 1, 1, 4),
    _AluNgeKeygroupRIBindingOutbound_Type()
)
aluNgeKeygroupRIBindingOutbound.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeKeygroupRIBindingOutbound.setStatus("current")


class _AluNgeKeygroupRIBindInExceptId_Type(TFilterID):
    """Custom type aluNgeKeygroupRIBindInExceptId based on TFilterID"""
    defaultValue = 0


_AluNgeKeygroupRIBindInExceptId_Type.__name__ = "TFilterID"
_AluNgeKeygroupRIBindInExceptId_Object = MibTableColumn
aluNgeKeygroupRIBindInExceptId = _AluNgeKeygroupRIBindInExceptId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 9, 1, 1, 5),
    _AluNgeKeygroupRIBindInExceptId_Type()
)
aluNgeKeygroupRIBindInExceptId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeKeygroupRIBindInExceptId.setStatus("current")


class _AluNgeKeygroupRIBindOutExceptId_Type(TFilterID):
    """Custom type aluNgeKeygroupRIBindOutExceptId based on TFilterID"""
    defaultValue = 0


_AluNgeKeygroupRIBindOutExceptId_Type.__name__ = "TFilterID"
_AluNgeKeygroupRIBindOutExceptId_Object = MibTableColumn
aluNgeKeygroupRIBindOutExceptId = _AluNgeKeygroupRIBindOutExceptId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 9, 1, 1, 6),
    _AluNgeKeygroupRIBindOutExceptId_Type()
)
aluNgeKeygroupRIBindOutExceptId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeKeygroupRIBindOutExceptId.setStatus("current")
_AluNgeKeygroupEthBindingObjs_ObjectIdentity = ObjectIdentity
aluNgeKeygroupEthBindingObjs = _AluNgeKeygroupEthBindingObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 10)
)
_AluNgeIPExceptObjs_ObjectIdentity = ObjectIdentity
aluNgeIPExceptObjs = _AluNgeIPExceptObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 11)
)
_AluNgeIPExceptionTable_Object = MibTable
aluNgeIPExceptionTable = _AluNgeIPExceptionTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 11, 1)
)
if mibBuilder.loadTexts:
    aluNgeIPExceptionTable.setStatus("current")
_AluNgeIPExceptionEntry_Object = MibTableRow
aluNgeIPExceptionEntry = _AluNgeIPExceptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 11, 1, 1)
)
aluNgeIPExceptionEntry.setIndexNames(
    (0, "ALU-NGE-MIB", "aluNgeIPExceptionId"),
)
if mibBuilder.loadTexts:
    aluNgeIPExceptionEntry.setStatus("current")
_AluNgeIPExceptionId_Type = TFilterID
_AluNgeIPExceptionId_Object = MibTableColumn
aluNgeIPExceptionId = _AluNgeIPExceptionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 11, 1, 1, 1),
    _AluNgeIPExceptionId_Type()
)
aluNgeIPExceptionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluNgeIPExceptionId.setStatus("current")
_AluNgeIPExceptionRowStatus_Type = RowStatus
_AluNgeIPExceptionRowStatus_Object = MibTableColumn
aluNgeIPExceptionRowStatus = _AluNgeIPExceptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 11, 1, 1, 2),
    _AluNgeIPExceptionRowStatus_Type()
)
aluNgeIPExceptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeIPExceptionRowStatus.setStatus("current")


class _AluNgeIPExceptionScope_Type(TFilterScope):
    """Custom type aluNgeIPExceptionScope based on TFilterScope"""
    defaultValue = 2


_AluNgeIPExceptionScope_Type.__name__ = "TFilterScope"
_AluNgeIPExceptionScope_Object = MibTableColumn
aluNgeIPExceptionScope = _AluNgeIPExceptionScope_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 11, 1, 1, 3),
    _AluNgeIPExceptionScope_Type()
)
aluNgeIPExceptionScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeIPExceptionScope.setStatus("current")


class _AluNgeIPExceptionDescription_Type(TItemDescription):
    """Custom type aluNgeIPExceptionDescription based on TItemDescription"""
    defaultValue = OctetString("")


_AluNgeIPExceptionDescription_Type.__name__ = "TItemDescription"
_AluNgeIPExceptionDescription_Object = MibTableColumn
aluNgeIPExceptionDescription = _AluNgeIPExceptionDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 11, 1, 1, 4),
    _AluNgeIPExceptionDescription_Type()
)
aluNgeIPExceptionDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeIPExceptionDescription.setStatus("current")


class _AluNgeIPExceptionName_Type(TLNamedItemOrEmpty):
    """Custom type aluNgeIPExceptionName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_AluNgeIPExceptionName_Type.__name__ = "TLNamedItemOrEmpty"
_AluNgeIPExceptionName_Object = MibTableColumn
aluNgeIPExceptionName = _AluNgeIPExceptionName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 11, 1, 1, 5),
    _AluNgeIPExceptionName_Type()
)
aluNgeIPExceptionName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeIPExceptionName.setStatus("current")
_AluNgeIPExceptNameTableLastChgd_Type = Counter64
_AluNgeIPExceptNameTableLastChgd_Object = MibScalar
aluNgeIPExceptNameTableLastChgd = _AluNgeIPExceptNameTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 11, 2),
    _AluNgeIPExceptNameTableLastChgd_Type()
)
aluNgeIPExceptNameTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeIPExceptNameTableLastChgd.setStatus("current")
_AluNgeIPExceptionNameTable_Object = MibTable
aluNgeIPExceptionNameTable = _AluNgeIPExceptionNameTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 11, 3)
)
if mibBuilder.loadTexts:
    aluNgeIPExceptionNameTable.setStatus("current")
_AluNgeIPExceptionNameEntry_Object = MibTableRow
aluNgeIPExceptionNameEntry = _AluNgeIPExceptionNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 11, 3, 1)
)
aluNgeIPExceptionNameEntry.setIndexNames(
    (0, "ALU-NGE-MIB", "aluNgeIPExceptionName"),
)
if mibBuilder.loadTexts:
    aluNgeIPExceptionNameEntry.setStatus("current")
_AluNgeIPExceptionNameId_Type = TFilterID
_AluNgeIPExceptionNameId_Object = MibTableColumn
aluNgeIPExceptionNameId = _AluNgeIPExceptionNameId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 11, 3, 1, 1),
    _AluNgeIPExceptionNameId_Type()
)
aluNgeIPExceptionNameId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeIPExceptionNameId.setStatus("current")
_AluNgeIPExceptionNameRowStatus_Type = RowStatus
_AluNgeIPExceptionNameRowStatus_Object = MibTableColumn
aluNgeIPExceptionNameRowStatus = _AluNgeIPExceptionNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 11, 3, 1, 2),
    _AluNgeIPExceptionNameRowStatus_Type()
)
aluNgeIPExceptionNameRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeIPExceptionNameRowStatus.setStatus("current")
_AluNgeIPExceptionNameLastChanged_Type = TimeStamp
_AluNgeIPExceptionNameLastChanged_Object = MibTableColumn
aluNgeIPExceptionNameLastChanged = _AluNgeIPExceptionNameLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 11, 3, 1, 3),
    _AluNgeIPExceptionNameLastChanged_Type()
)
aluNgeIPExceptionNameLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeIPExceptionNameLastChanged.setStatus("current")
_AluNgeIPExceptionParamsTable_Object = MibTable
aluNgeIPExceptionParamsTable = _AluNgeIPExceptionParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 11, 4)
)
if mibBuilder.loadTexts:
    aluNgeIPExceptionParamsTable.setStatus("current")
_AluNgeIPExceptionParamsEntry_Object = MibTableRow
aluNgeIPExceptionParamsEntry = _AluNgeIPExceptionParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 11, 4, 1)
)
aluNgeIPExceptionParamsEntry.setIndexNames(
    (0, "ALU-NGE-MIB", "aluNgeIPExceptionId"),
    (0, "ALU-NGE-MIB", "aluNgeIPExceptionParamsId"),
)
if mibBuilder.loadTexts:
    aluNgeIPExceptionParamsEntry.setStatus("current")
_AluNgeIPExceptionParamsId_Type = TEntryId
_AluNgeIPExceptionParamsId_Object = MibTableColumn
aluNgeIPExceptionParamsId = _AluNgeIPExceptionParamsId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 11, 4, 1, 1),
    _AluNgeIPExceptionParamsId_Type()
)
aluNgeIPExceptionParamsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluNgeIPExceptionParamsId.setStatus("current")
_AluNgeIPExceptionParamsRowStatus_Type = RowStatus
_AluNgeIPExceptionParamsRowStatus_Object = MibTableColumn
aluNgeIPExceptionParamsRowStatus = _AluNgeIPExceptionParamsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 11, 4, 1, 2),
    _AluNgeIPExceptionParamsRowStatus_Type()
)
aluNgeIPExceptionParamsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeIPExceptionParamsRowStatus.setStatus("current")


class _AluNgeIPExceptParamsDescription_Type(TItemDescription):
    """Custom type aluNgeIPExceptParamsDescription based on TItemDescription"""
    defaultValue = OctetString("")


_AluNgeIPExceptParamsDescription_Type.__name__ = "TItemDescription"
_AluNgeIPExceptParamsDescription_Object = MibTableColumn
aluNgeIPExceptParamsDescription = _AluNgeIPExceptParamsDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 11, 4, 1, 3),
    _AluNgeIPExceptParamsDescription_Type()
)
aluNgeIPExceptParamsDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeIPExceptParamsDescription.setStatus("current")


class _AluNgeIPExceptParamsSourceIpAddr_Type(IpAddress):
    """Custom type aluNgeIPExceptParamsSourceIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_AluNgeIPExceptParamsSourceIpAddr_Type.__name__ = "IpAddress"
_AluNgeIPExceptParamsSourceIpAddr_Object = MibTableColumn
aluNgeIPExceptParamsSourceIpAddr = _AluNgeIPExceptParamsSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 11, 4, 1, 4),
    _AluNgeIPExceptParamsSourceIpAddr_Type()
)
aluNgeIPExceptParamsSourceIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeIPExceptParamsSourceIpAddr.setStatus("current")


class _AluNgeIPExceptParamsSourceIpMask_Type(IpAddressPrefixLength):
    """Custom type aluNgeIPExceptParamsSourceIpMask based on IpAddressPrefixLength"""
    defaultValue = 0


_AluNgeIPExceptParamsSourceIpMask_Type.__name__ = "IpAddressPrefixLength"
_AluNgeIPExceptParamsSourceIpMask_Object = MibTableColumn
aluNgeIPExceptParamsSourceIpMask = _AluNgeIPExceptParamsSourceIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 11, 4, 1, 5),
    _AluNgeIPExceptParamsSourceIpMask_Type()
)
aluNgeIPExceptParamsSourceIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeIPExceptParamsSourceIpMask.setStatus("current")


class _AluNgeIPExceptParamsDestIpAddr_Type(IpAddress):
    """Custom type aluNgeIPExceptParamsDestIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_AluNgeIPExceptParamsDestIpAddr_Type.__name__ = "IpAddress"
_AluNgeIPExceptParamsDestIpAddr_Object = MibTableColumn
aluNgeIPExceptParamsDestIpAddr = _AluNgeIPExceptParamsDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 11, 4, 1, 6),
    _AluNgeIPExceptParamsDestIpAddr_Type()
)
aluNgeIPExceptParamsDestIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeIPExceptParamsDestIpAddr.setStatus("current")


class _AluNgeIPExceptParamsDestIpMask_Type(IpAddressPrefixLength):
    """Custom type aluNgeIPExceptParamsDestIpMask based on IpAddressPrefixLength"""
    defaultValue = 0


_AluNgeIPExceptParamsDestIpMask_Type.__name__ = "IpAddressPrefixLength"
_AluNgeIPExceptParamsDestIpMask_Object = MibTableColumn
aluNgeIPExceptParamsDestIpMask = _AluNgeIPExceptParamsDestIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 11, 4, 1, 7),
    _AluNgeIPExceptParamsDestIpMask_Type()
)
aluNgeIPExceptParamsDestIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeIPExceptParamsDestIpMask.setStatus("current")


class _AluNgeIPExceptParamsProtocol_Type(TIpProtocol):
    """Custom type aluNgeIPExceptParamsProtocol based on TIpProtocol"""
    defaultValue = -1


_AluNgeIPExceptParamsProtocol_Type.__name__ = "TIpProtocol"
_AluNgeIPExceptParamsProtocol_Object = MibTableColumn
aluNgeIPExceptParamsProtocol = _AluNgeIPExceptParamsProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 11, 4, 1, 8),
    _AluNgeIPExceptParamsProtocol_Type()
)
aluNgeIPExceptParamsProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeIPExceptParamsProtocol.setStatus("current")


class _AluNgeIPExceptParamsSrcPortVal1_Type(TTcpUdpPort):
    """Custom type aluNgeIPExceptParamsSrcPortVal1 based on TTcpUdpPort"""
    defaultValue = 0


_AluNgeIPExceptParamsSrcPortVal1_Type.__name__ = "TTcpUdpPort"
_AluNgeIPExceptParamsSrcPortVal1_Object = MibTableColumn
aluNgeIPExceptParamsSrcPortVal1 = _AluNgeIPExceptParamsSrcPortVal1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 11, 4, 1, 9),
    _AluNgeIPExceptParamsSrcPortVal1_Type()
)
aluNgeIPExceptParamsSrcPortVal1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeIPExceptParamsSrcPortVal1.setStatus("current")


class _AluNgeIPExceptParamsSrcPortVal2_Type(TTcpUdpPort):
    """Custom type aluNgeIPExceptParamsSrcPortVal2 based on TTcpUdpPort"""
    defaultValue = 0


_AluNgeIPExceptParamsSrcPortVal2_Type.__name__ = "TTcpUdpPort"
_AluNgeIPExceptParamsSrcPortVal2_Object = MibTableColumn
aluNgeIPExceptParamsSrcPortVal2 = _AluNgeIPExceptParamsSrcPortVal2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 11, 4, 1, 10),
    _AluNgeIPExceptParamsSrcPortVal2_Type()
)
aluNgeIPExceptParamsSrcPortVal2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeIPExceptParamsSrcPortVal2.setStatus("current")


class _AluNgeIPExceptParamsSrcPortOpr_Type(TOperator):
    """Custom type aluNgeIPExceptParamsSrcPortOpr based on TOperator"""
    defaultValue = 0


_AluNgeIPExceptParamsSrcPortOpr_Type.__name__ = "TOperator"
_AluNgeIPExceptParamsSrcPortOpr_Object = MibTableColumn
aluNgeIPExceptParamsSrcPortOpr = _AluNgeIPExceptParamsSrcPortOpr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 11, 4, 1, 11),
    _AluNgeIPExceptParamsSrcPortOpr_Type()
)
aluNgeIPExceptParamsSrcPortOpr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeIPExceptParamsSrcPortOpr.setStatus("current")


class _AluNgeIPExceptParamsDestPortVal1_Type(TTcpUdpPort):
    """Custom type aluNgeIPExceptParamsDestPortVal1 based on TTcpUdpPort"""
    defaultValue = 0


_AluNgeIPExceptParamsDestPortVal1_Type.__name__ = "TTcpUdpPort"
_AluNgeIPExceptParamsDestPortVal1_Object = MibTableColumn
aluNgeIPExceptParamsDestPortVal1 = _AluNgeIPExceptParamsDestPortVal1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 11, 4, 1, 12),
    _AluNgeIPExceptParamsDestPortVal1_Type()
)
aluNgeIPExceptParamsDestPortVal1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeIPExceptParamsDestPortVal1.setStatus("current")


class _AluNgeIPExceptParamsDestPortVal2_Type(TTcpUdpPort):
    """Custom type aluNgeIPExceptParamsDestPortVal2 based on TTcpUdpPort"""
    defaultValue = 0


_AluNgeIPExceptParamsDestPortVal2_Type.__name__ = "TTcpUdpPort"
_AluNgeIPExceptParamsDestPortVal2_Object = MibTableColumn
aluNgeIPExceptParamsDestPortVal2 = _AluNgeIPExceptParamsDestPortVal2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 11, 4, 1, 13),
    _AluNgeIPExceptParamsDestPortVal2_Type()
)
aluNgeIPExceptParamsDestPortVal2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeIPExceptParamsDestPortVal2.setStatus("current")


class _AluNgeIPExceptParamsDestPortOpr_Type(TOperator):
    """Custom type aluNgeIPExceptParamsDestPortOpr based on TOperator"""
    defaultValue = 0


_AluNgeIPExceptParamsDestPortOpr_Type.__name__ = "TOperator"
_AluNgeIPExceptParamsDestPortOpr_Object = MibTableColumn
aluNgeIPExceptParamsDestPortOpr = _AluNgeIPExceptParamsDestPortOpr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 11, 4, 1, 14),
    _AluNgeIPExceptParamsDestPortOpr_Type()
)
aluNgeIPExceptParamsDestPortOpr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeIPExceptParamsDestPortOpr.setStatus("current")


class _AluNgeIPExceptParamsIcmpCode_Type(Integer32):
    """Custom type aluNgeIPExceptParamsIcmpCode based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_AluNgeIPExceptParamsIcmpCode_Type.__name__ = "Integer32"
_AluNgeIPExceptParamsIcmpCode_Object = MibTableColumn
aluNgeIPExceptParamsIcmpCode = _AluNgeIPExceptParamsIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 11, 4, 1, 15),
    _AluNgeIPExceptParamsIcmpCode_Type()
)
aluNgeIPExceptParamsIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeIPExceptParamsIcmpCode.setStatus("current")


class _AluNgeIPExceptParamsIcmpType_Type(Integer32):
    """Custom type aluNgeIPExceptParamsIcmpType based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_AluNgeIPExceptParamsIcmpType_Type.__name__ = "Integer32"
_AluNgeIPExceptParamsIcmpType_Object = MibTableColumn
aluNgeIPExceptParamsIcmpType = _AluNgeIPExceptParamsIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 11, 4, 1, 16),
    _AluNgeIPExceptParamsIcmpType_Type()
)
aluNgeIPExceptParamsIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeIPExceptParamsIcmpType.setStatus("current")
_AluNgeIPExceptParmSrcIpFullMask_Type = IpAddress
_AluNgeIPExceptParmSrcIpFullMask_Object = MibTableColumn
aluNgeIPExceptParmSrcIpFullMask = _AluNgeIPExceptParmSrcIpFullMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 11, 4, 1, 17),
    _AluNgeIPExceptParmSrcIpFullMask_Type()
)
aluNgeIPExceptParmSrcIpFullMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeIPExceptParmSrcIpFullMask.setStatus("current")
_AluNgeIPExceptParmDestIpFullMask_Type = IpAddress
_AluNgeIPExceptParmDestIpFullMask_Object = MibTableColumn
aluNgeIPExceptParmDestIpFullMask = _AluNgeIPExceptParmDestIpFullMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 11, 4, 1, 18),
    _AluNgeIPExceptParmDestIpFullMask_Type()
)
aluNgeIPExceptParmDestIpFullMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeIPExceptParmDestIpFullMask.setStatus("current")
_AluNgeIPExceptIngressHitCount_Type = Counter64
_AluNgeIPExceptIngressHitCount_Object = MibTableColumn
aluNgeIPExceptIngressHitCount = _AluNgeIPExceptIngressHitCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 11, 4, 1, 19),
    _AluNgeIPExceptIngressHitCount_Type()
)
aluNgeIPExceptIngressHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeIPExceptIngressHitCount.setStatus("current")
_AluNgeIPExceptEgressHitCount_Type = Counter64
_AluNgeIPExceptEgressHitCount_Object = MibTableColumn
aluNgeIPExceptEgressHitCount = _AluNgeIPExceptEgressHitCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 11, 4, 1, 20),
    _AluNgeIPExceptEgressHitCount_Type()
)
aluNgeIPExceptEgressHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeIPExceptEgressHitCount.setStatus("current")
_AluNgeIPExceptIngrHitByteCount_Type = Counter64
_AluNgeIPExceptIngrHitByteCount_Object = MibTableColumn
aluNgeIPExceptIngrHitByteCount = _AluNgeIPExceptIngrHitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 11, 4, 1, 21),
    _AluNgeIPExceptIngrHitByteCount_Type()
)
aluNgeIPExceptIngrHitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeIPExceptIngrHitByteCount.setStatus("current")
_AluNgeIPExceptEgressHitByteCount_Type = Counter64
_AluNgeIPExceptEgressHitByteCount_Object = MibTableColumn
aluNgeIPExceptEgressHitByteCount = _AluNgeIPExceptEgressHitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 11, 4, 1, 22),
    _AluNgeIPExceptEgressHitByteCount_Type()
)
aluNgeIPExceptEgressHitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluNgeIPExceptEgressHitByteCount.setStatus("current")
_AluNgeKeygroupWlanGwBindingObjs_ObjectIdentity = ObjectIdentity
aluNgeKeygroupWlanGwBindingObjs = _AluNgeKeygroupWlanGwBindingObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 12)
)
_AluNgeKeygroupWlanGwBindingTable_Object = MibTable
aluNgeKeygroupWlanGwBindingTable = _AluNgeKeygroupWlanGwBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 12, 1)
)
if mibBuilder.loadTexts:
    aluNgeKeygroupWlanGwBindingTable.setStatus("current")
_AluNgeKeygroupWlanGwBindingEntry_Object = MibTableRow
aluNgeKeygroupWlanGwBindingEntry = _AluNgeKeygroupWlanGwBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 12, 1, 1)
)
if mibBuilder.loadTexts:
    aluNgeKeygroupWlanGwBindingEntry.setStatus("current")


class _AluNgeKeygroupWlanGwBindingInbound_Type(AluNgeKeygroupIdOrZero):
    """Custom type aluNgeKeygroupWlanGwBindingInbound based on AluNgeKeygroupIdOrZero"""
    defaultValue = 0


_AluNgeKeygroupWlanGwBindingInbound_Type.__name__ = "AluNgeKeygroupIdOrZero"
_AluNgeKeygroupWlanGwBindingInbound_Object = MibTableColumn
aluNgeKeygroupWlanGwBindingInbound = _AluNgeKeygroupWlanGwBindingInbound_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 12, 1, 1, 1),
    _AluNgeKeygroupWlanGwBindingInbound_Type()
)
aluNgeKeygroupWlanGwBindingInbound.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeKeygroupWlanGwBindingInbound.setStatus("current")


class _AluNgeKeygroupWlanGwBindingOutbound_Type(AluNgeKeygroupIdOrZero):
    """Custom type aluNgeKeygroupWlanGwBindingOutbound based on AluNgeKeygroupIdOrZero"""
    defaultValue = 0


_AluNgeKeygroupWlanGwBindingOutbound_Type.__name__ = "AluNgeKeygroupIdOrZero"
_AluNgeKeygroupWlanGwBindingOutbound_Object = MibTableColumn
aluNgeKeygroupWlanGwBindingOutbound = _AluNgeKeygroupWlanGwBindingOutbound_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 20, 12, 1, 1, 2),
    _AluNgeKeygroupWlanGwBindingOutbound_Type()
)
aluNgeKeygroupWlanGwBindingOutbound.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluNgeKeygroupWlanGwBindingOutbound.setStatus("current")
_AluNgeNotificationsPrefix_ObjectIdentity = ObjectIdentity
aluNgeNotificationsPrefix = _AluNgeNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 16)
)
_AluNgeNotifications_ObjectIdentity = ObjectIdentity
aluNgeNotifications = _AluNgeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 16, 0)
)
sdpInfoEntry.registerAugmentions(
    ("ALU-NGE-MIB",
     "aluNgeKeygroupSdpBindingEntry")
)
aluNgeKeygroupSdpBindingEntry.setIndexNames(*sdpInfoEntry.getIndexNames())
svcBaseInfoEntry.registerAugmentions(
    ("ALU-NGE-MIB",
     "aluNgeKeygroupVrfBindingEntry")
)
aluNgeKeygroupVrfBindingEntry.setIndexNames(*svcBaseInfoEntry.getIndexNames())
sdpBindBaseStatsEntry.registerAugmentions(
    ("ALU-NGE-MIB",
     "aluNgeKeygroupSdpBindStatsEntry")
)
aluNgeKeygroupSdpBindStatsEntry.setIndexNames(*sdpBindBaseStatsEntry.getIndexNames())
tmnxWlanGwSoftGreIfEntry.registerAugmentions(
    ("ALU-NGE-MIB",
     "aluNgeKeygroupWlanGwBindingEntry")
)
aluNgeKeygroupWlanGwBindingEntry.setIndexNames(*tmnxWlanGwSoftGreIfEntry.getIndexNames())

# Managed Objects groups

aluNgeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 20, 2, 1)
)
aluNgeGroup.setObjects(
      *(("ALU-NGE-MIB", "aluNgeLabel"),
        ("ALU-NGE-MIB", "aluNgeKeygroupRowStatus"),
        ("ALU-NGE-MIB", "aluNgeKeygroupDescription"),
        ("ALU-NGE-MIB", "aluNgeKeygroupAuthAlgorithm"),
        ("ALU-NGE-MIB", "aluNgeKeygroupEncrAlgorithm"),
        ("ALU-NGE-MIB", "aluNgeKeygroupActiveOutboundSa"),
        ("ALU-NGE-MIB", "aluNgeKeygroupOutboundSaActivateTime"),
        ("ALU-NGE-MIB", "aluNgeKeygroupName"),
        ("ALU-NGE-MIB", "aluNgeKeygroupSpiRowStatus"),
        ("ALU-NGE-MIB", "aluNgeKeygroupSpiAuthKey"),
        ("ALU-NGE-MIB", "aluNgeKeygroupSpiEncrKey"),
        ("ALU-NGE-MIB", "aluNgeKeygroupSpiInstallTime"),
        ("ALU-NGE-MIB", "aluNgeKeygroupSpiKeyCRC"),
        ("ALU-NGE-MIB", "aluNgeKeygroupSdpBindingInbound"),
        ("ALU-NGE-MIB", "aluNgeKeygroupSdpBindingOutbound"),
        ("ALU-NGE-MIB", "aluNgeKeygroupVrfBindingInbound"),
        ("ALU-NGE-MIB", "aluNgeKeygroupVrfBindingOutbound"),
        ("ALU-NGE-MIB", "aluNgeKeygroupNameId"),
        ("ALU-NGE-MIB", "aluNgeKeygroupNameRowStatus"))
)
if mibBuilder.loadTexts:
    aluNgeGroup.setStatus("current")

aluNgeStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 20, 2, 2)
)
aluNgeStatsGroup.setObjects(
      *(("ALU-NGE-MIB", "aluNgeMdaEncryptPkts"),
        ("ALU-NGE-MIB", "aluNgeMdaEncryptBytes"),
        ("ALU-NGE-MIB", "aluNgeMdaDecryptPkts"),
        ("ALU-NGE-MIB", "aluNgeMdaDecryptBytes"),
        ("ALU-NGE-MIB", "aluNgeMdaOutDropPkts"),
        ("ALU-NGE-MIB", "aluNgeMdaOutDropUnsupportedUplink"),
        ("ALU-NGE-MIB", "aluNgeMdaOutDropEnqueueError"),
        ("ALU-NGE-MIB", "aluNgeMdaInDropPkts"),
        ("ALU-NGE-MIB", "aluNgeMdaInDropInvalidSpi"),
        ("ALU-NGE-MIB", "aluNgeMdaInDropAuthFailure"),
        ("ALU-NGE-MIB", "aluNgeMdaInDropPaddingFailure"),
        ("ALU-NGE-MIB", "aluNgeMdaInDropEnqueueError"),
        ("ALU-NGE-MIB", "aluNgeMdaInDropControlWordMismatch"),
        ("ALU-NGE-MIB", "aluNgeKeygroupEncryptPkts"),
        ("ALU-NGE-MIB", "aluNgeKeygroupEncryptBytes"),
        ("ALU-NGE-MIB", "aluNgeKeygroupDecryptPkts"),
        ("ALU-NGE-MIB", "aluNgeKeygroupDecryptBytes"),
        ("ALU-NGE-MIB", "aluNgeKeygroupOutDropPkts"),
        ("ALU-NGE-MIB", "aluNgeKeygroupOutDropUnsupportedUplink"),
        ("ALU-NGE-MIB", "aluNgeKeygroupOutDropEnqueueError"),
        ("ALU-NGE-MIB", "aluNgeKeygroupOutDropOther"),
        ("ALU-NGE-MIB", "aluNgeKeygroupInDropPkts"),
        ("ALU-NGE-MIB", "aluNgeKeygroupInDropInvalidSpi"),
        ("ALU-NGE-MIB", "aluNgeKeygroupInDropAuthFailure"),
        ("ALU-NGE-MIB", "aluNgeKeygroupInDropPaddingFailure"),
        ("ALU-NGE-MIB", "aluNgeKeygroupInDropEnqueueError"),
        ("ALU-NGE-MIB", "aluNgeKeygroupInDropControlWordMismatch"),
        ("ALU-NGE-MIB", "aluNgeKeygroupInDropOther"),
        ("ALU-NGE-MIB", "aluNgeKeygroupInLastDropSpi"),
        ("ALU-NGE-MIB", "aluNgeKeygroupSpiEncryptPkts"),
        ("ALU-NGE-MIB", "aluNgeKeygroupSpiEncryptBytes"),
        ("ALU-NGE-MIB", "aluNgeKeygroupSpiDecryptPkts"),
        ("ALU-NGE-MIB", "aluNgeKeygroupSpiDecryptBytes"),
        ("ALU-NGE-MIB", "aluNgeKeygroupSpiOutDropPkts"),
        ("ALU-NGE-MIB", "aluNgeKeygroupSpiOutDropEnqueueError"),
        ("ALU-NGE-MIB", "aluNgeKeygroupSpiOutDropOther"),
        ("ALU-NGE-MIB", "aluNgeKeygroupSpiInDropPkts"),
        ("ALU-NGE-MIB", "aluNgeKeygroupSpiInDropAuthFailure"),
        ("ALU-NGE-MIB", "aluNgeKeygroupSpiInDropPaddingFailure"),
        ("ALU-NGE-MIB", "aluNgeKeygroupSpiInDropEnqueueError"),
        ("ALU-NGE-MIB", "aluNgeKeygroupSpiInDropControlWordMismatch"),
        ("ALU-NGE-MIB", "aluNgeKeygroupSpiInDropOther"),
        ("ALU-NGE-MIB", "aluNgeKeygroupSdpBindEncryptPkts"),
        ("ALU-NGE-MIB", "aluNgeKeygroupSdpBindEncryptBytes"),
        ("ALU-NGE-MIB", "aluNgeKeygroupSdpBindDecryptPkts"),
        ("ALU-NGE-MIB", "aluNgeKeygroupSdpBindDecryptBytes"),
        ("ALU-NGE-MIB", "aluNgeKeygroupSdpBindIngDropOtherPkts"),
        ("ALU-NGE-MIB", "aluNgeKeygroupSdpBindEgDropPkts"),
        ("ALU-NGE-MIB", "aluNgeKeygroupSdpBindIngDropInvalidSpi"))
)
if mibBuilder.loadTexts:
    aluNgeStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aluNgeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 20, 1, 1)
)
aluNgeCompliance.setObjects(
      *(("ALU-NGE-MIB", "aluNgeGroup"),
        ("ALU-NGE-MIB", "aluNgeStatsGroup"))
)
if mibBuilder.loadTexts:
    aluNgeCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALU-NGE-MIB",
    **{"AluNgeKeygroupId": AluNgeKeygroupId,
       "AluNgeKeygroupIdOrZero": AluNgeKeygroupIdOrZero,
       "AluNgeAuthAlgorithm": AluNgeAuthAlgorithm,
       "AluNgeEncrAlgorithm": AluNgeEncrAlgorithm,
       "AluNgeKeygroupSpiId": AluNgeKeygroupSpiId,
       "AluNgeKeygroupSpiIdOrZero": AluNgeKeygroupSpiIdOrZero,
       "aluNgeMIBModule": aluNgeMIBModule,
       "aluNgeMIBConformance": aluNgeMIBConformance,
       "aluNgeCompliances": aluNgeCompliances,
       "aluNgeCompliance": aluNgeCompliance,
       "aluNgeGroups": aluNgeGroups,
       "aluNgeGroup": aluNgeGroup,
       "aluNgeStatsGroup": aluNgeStatsGroup,
       "aluNgeObjs": aluNgeObjs,
       "aluNgeSystemObjs": aluNgeSystemObjs,
       "aluNgeLabel": aluNgeLabel,
       "aluNgeKeygroupObjs": aluNgeKeygroupObjs,
       "aluNgeKeygroupTable": aluNgeKeygroupTable,
       "aluNgeKeygroupEntry": aluNgeKeygroupEntry,
       "aluNgeKeygroupId": aluNgeKeygroupId,
       "aluNgeKeygroupRowStatus": aluNgeKeygroupRowStatus,
       "aluNgeKeygroupDescription": aluNgeKeygroupDescription,
       "aluNgeKeygroupAuthAlgorithm": aluNgeKeygroupAuthAlgorithm,
       "aluNgeKeygroupEncrAlgorithm": aluNgeKeygroupEncrAlgorithm,
       "aluNgeKeygroupActiveOutboundSa": aluNgeKeygroupActiveOutboundSa,
       "aluNgeKeygroupOutboundSaActivateTime": aluNgeKeygroupOutboundSaActivateTime,
       "aluNgeKeygroupName": aluNgeKeygroupName,
       "aluNgeKeygroupSpiObjs": aluNgeKeygroupSpiObjs,
       "aluNgeKeygroupSpiTable": aluNgeKeygroupSpiTable,
       "aluNgeKeygroupSpiEntry": aluNgeKeygroupSpiEntry,
       "aluNgeKeygroupSpiId": aluNgeKeygroupSpiId,
       "aluNgeKeygroupSpiRowStatus": aluNgeKeygroupSpiRowStatus,
       "aluNgeKeygroupSpiAuthKey": aluNgeKeygroupSpiAuthKey,
       "aluNgeKeygroupSpiEncrKey": aluNgeKeygroupSpiEncrKey,
       "aluNgeKeygroupSpiInstallTime": aluNgeKeygroupSpiInstallTime,
       "aluNgeKeygroupSpiKeyCRC": aluNgeKeygroupSpiKeyCRC,
       "aluNgeKeygroupSdpBindingObjs": aluNgeKeygroupSdpBindingObjs,
       "aluNgeKeygroupSdpBindingTable": aluNgeKeygroupSdpBindingTable,
       "aluNgeKeygroupSdpBindingEntry": aluNgeKeygroupSdpBindingEntry,
       "aluNgeKeygroupSdpBindingInbound": aluNgeKeygroupSdpBindingInbound,
       "aluNgeKeygroupSdpBindingOutbound": aluNgeKeygroupSdpBindingOutbound,
       "aluNgeKeygroupVrfBindingObjs": aluNgeKeygroupVrfBindingObjs,
       "aluNgeKeygroupVrfBindingTable": aluNgeKeygroupVrfBindingTable,
       "aluNgeKeygroupVrfBindingEntry": aluNgeKeygroupVrfBindingEntry,
       "aluNgeKeygroupVrfBindingInbound": aluNgeKeygroupVrfBindingInbound,
       "aluNgeKeygroupVrfBindingOutbound": aluNgeKeygroupVrfBindingOutbound,
       "aluNgeStatsObjs": aluNgeStatsObjs,
       "aluNgeMdaStatsTable": aluNgeMdaStatsTable,
       "aluNgeMdaStatsEntry": aluNgeMdaStatsEntry,
       "aluNgeMdaEncryptPkts": aluNgeMdaEncryptPkts,
       "aluNgeMdaEncryptBytes": aluNgeMdaEncryptBytes,
       "aluNgeMdaDecryptPkts": aluNgeMdaDecryptPkts,
       "aluNgeMdaDecryptBytes": aluNgeMdaDecryptBytes,
       "aluNgeMdaOutDropPkts": aluNgeMdaOutDropPkts,
       "aluNgeMdaOutDropUnsupportedUplink": aluNgeMdaOutDropUnsupportedUplink,
       "aluNgeMdaOutDropEnqueueError": aluNgeMdaOutDropEnqueueError,
       "aluNgeMdaInDropPkts": aluNgeMdaInDropPkts,
       "aluNgeMdaInDropInvalidSpi": aluNgeMdaInDropInvalidSpi,
       "aluNgeMdaInDropAuthFailure": aluNgeMdaInDropAuthFailure,
       "aluNgeMdaInDropPaddingFailure": aluNgeMdaInDropPaddingFailure,
       "aluNgeMdaInDropEnqueueError": aluNgeMdaInDropEnqueueError,
       "aluNgeMdaInDropControlWordMismatch": aluNgeMdaInDropControlWordMismatch,
       "aluNgeKeygroupStatsTable": aluNgeKeygroupStatsTable,
       "aluNgeKeygroupStatsEntry": aluNgeKeygroupStatsEntry,
       "aluNgeKeygroupEncryptPkts": aluNgeKeygroupEncryptPkts,
       "aluNgeKeygroupEncryptBytes": aluNgeKeygroupEncryptBytes,
       "aluNgeKeygroupDecryptPkts": aluNgeKeygroupDecryptPkts,
       "aluNgeKeygroupDecryptBytes": aluNgeKeygroupDecryptBytes,
       "aluNgeKeygroupOutDropPkts": aluNgeKeygroupOutDropPkts,
       "aluNgeKeygroupOutDropUnsupportedUplink": aluNgeKeygroupOutDropUnsupportedUplink,
       "aluNgeKeygroupOutDropEnqueueError": aluNgeKeygroupOutDropEnqueueError,
       "aluNgeKeygroupOutDropOther": aluNgeKeygroupOutDropOther,
       "aluNgeKeygroupInDropPkts": aluNgeKeygroupInDropPkts,
       "aluNgeKeygroupInDropInvalidSpi": aluNgeKeygroupInDropInvalidSpi,
       "aluNgeKeygroupInDropAuthFailure": aluNgeKeygroupInDropAuthFailure,
       "aluNgeKeygroupInDropPaddingFailure": aluNgeKeygroupInDropPaddingFailure,
       "aluNgeKeygroupInDropEnqueueError": aluNgeKeygroupInDropEnqueueError,
       "aluNgeKeygroupInDropControlWordMismatch": aluNgeKeygroupInDropControlWordMismatch,
       "aluNgeKeygroupInDropOther": aluNgeKeygroupInDropOther,
       "aluNgeKeygroupInLastDropSpi": aluNgeKeygroupInLastDropSpi,
       "aluNgeKeygroupSpiStatsTable": aluNgeKeygroupSpiStatsTable,
       "aluNgeKeygroupSpiStatsEntry": aluNgeKeygroupSpiStatsEntry,
       "aluNgeKeygroupSpiEncryptPkts": aluNgeKeygroupSpiEncryptPkts,
       "aluNgeKeygroupSpiEncryptBytes": aluNgeKeygroupSpiEncryptBytes,
       "aluNgeKeygroupSpiDecryptPkts": aluNgeKeygroupSpiDecryptPkts,
       "aluNgeKeygroupSpiDecryptBytes": aluNgeKeygroupSpiDecryptBytes,
       "aluNgeKeygroupSpiOutDropPkts": aluNgeKeygroupSpiOutDropPkts,
       "aluNgeKeygroupSpiOutDropEnqueueError": aluNgeKeygroupSpiOutDropEnqueueError,
       "aluNgeKeygroupSpiOutDropOther": aluNgeKeygroupSpiOutDropOther,
       "aluNgeKeygroupSpiInDropPkts": aluNgeKeygroupSpiInDropPkts,
       "aluNgeKeygroupSpiInDropAuthFailure": aluNgeKeygroupSpiInDropAuthFailure,
       "aluNgeKeygroupSpiInDropPaddingFailure": aluNgeKeygroupSpiInDropPaddingFailure,
       "aluNgeKeygroupSpiInDropEnqueueError": aluNgeKeygroupSpiInDropEnqueueError,
       "aluNgeKeygroupSpiInDropControlWordMismatch": aluNgeKeygroupSpiInDropControlWordMismatch,
       "aluNgeKeygroupSpiInDropOther": aluNgeKeygroupSpiInDropOther,
       "aluNgeKeygroupSdpBindStatsTable": aluNgeKeygroupSdpBindStatsTable,
       "aluNgeKeygroupSdpBindStatsEntry": aluNgeKeygroupSdpBindStatsEntry,
       "aluNgeKeygroupSdpBindEncryptPkts": aluNgeKeygroupSdpBindEncryptPkts,
       "aluNgeKeygroupSdpBindEncryptBytes": aluNgeKeygroupSdpBindEncryptBytes,
       "aluNgeKeygroupSdpBindDecryptPkts": aluNgeKeygroupSdpBindDecryptPkts,
       "aluNgeKeygroupSdpBindDecryptBytes": aluNgeKeygroupSdpBindDecryptBytes,
       "aluNgeKeygroupSdpBindIngDropOtherPkts": aluNgeKeygroupSdpBindIngDropOtherPkts,
       "aluNgeKeygroupSdpBindEgDropPkts": aluNgeKeygroupSdpBindEgDropPkts,
       "aluNgeKeygroupSdpBindIngDropInvalidSpi": aluNgeKeygroupSdpBindIngDropInvalidSpi,
       "aluNgeKeygroupNameObjs": aluNgeKeygroupNameObjs,
       "aluNgeKeygroupNameTable": aluNgeKeygroupNameTable,
       "aluNgeKeygroupNameEntry": aluNgeKeygroupNameEntry,
       "aluNgeKeygroupNameId": aluNgeKeygroupNameId,
       "aluNgeKeygroupNameRowStatus": aluNgeKeygroupNameRowStatus,
       "aluNgeNotifyObjs": aluNgeNotifyObjs,
       "aluNgeKeygroupRIBindingObjs": aluNgeKeygroupRIBindingObjs,
       "aluNgeKeygroupRIBindingTable": aluNgeKeygroupRIBindingTable,
       "aluNgeKeygroupRIBindingEntry": aluNgeKeygroupRIBindingEntry,
       "aluNgeKeygroupRIBindingIfIndex": aluNgeKeygroupRIBindingIfIndex,
       "aluNgeKeygroupRIBindingRowStatus": aluNgeKeygroupRIBindingRowStatus,
       "aluNgeKeygroupRIBindingInbound": aluNgeKeygroupRIBindingInbound,
       "aluNgeKeygroupRIBindingOutbound": aluNgeKeygroupRIBindingOutbound,
       "aluNgeKeygroupRIBindInExceptId": aluNgeKeygroupRIBindInExceptId,
       "aluNgeKeygroupRIBindOutExceptId": aluNgeKeygroupRIBindOutExceptId,
       "aluNgeKeygroupEthBindingObjs": aluNgeKeygroupEthBindingObjs,
       "aluNgeIPExceptObjs": aluNgeIPExceptObjs,
       "aluNgeIPExceptionTable": aluNgeIPExceptionTable,
       "aluNgeIPExceptionEntry": aluNgeIPExceptionEntry,
       "aluNgeIPExceptionId": aluNgeIPExceptionId,
       "aluNgeIPExceptionRowStatus": aluNgeIPExceptionRowStatus,
       "aluNgeIPExceptionScope": aluNgeIPExceptionScope,
       "aluNgeIPExceptionDescription": aluNgeIPExceptionDescription,
       "aluNgeIPExceptionName": aluNgeIPExceptionName,
       "aluNgeIPExceptNameTableLastChgd": aluNgeIPExceptNameTableLastChgd,
       "aluNgeIPExceptionNameTable": aluNgeIPExceptionNameTable,
       "aluNgeIPExceptionNameEntry": aluNgeIPExceptionNameEntry,
       "aluNgeIPExceptionNameId": aluNgeIPExceptionNameId,
       "aluNgeIPExceptionNameRowStatus": aluNgeIPExceptionNameRowStatus,
       "aluNgeIPExceptionNameLastChanged": aluNgeIPExceptionNameLastChanged,
       "aluNgeIPExceptionParamsTable": aluNgeIPExceptionParamsTable,
       "aluNgeIPExceptionParamsEntry": aluNgeIPExceptionParamsEntry,
       "aluNgeIPExceptionParamsId": aluNgeIPExceptionParamsId,
       "aluNgeIPExceptionParamsRowStatus": aluNgeIPExceptionParamsRowStatus,
       "aluNgeIPExceptParamsDescription": aluNgeIPExceptParamsDescription,
       "aluNgeIPExceptParamsSourceIpAddr": aluNgeIPExceptParamsSourceIpAddr,
       "aluNgeIPExceptParamsSourceIpMask": aluNgeIPExceptParamsSourceIpMask,
       "aluNgeIPExceptParamsDestIpAddr": aluNgeIPExceptParamsDestIpAddr,
       "aluNgeIPExceptParamsDestIpMask": aluNgeIPExceptParamsDestIpMask,
       "aluNgeIPExceptParamsProtocol": aluNgeIPExceptParamsProtocol,
       "aluNgeIPExceptParamsSrcPortVal1": aluNgeIPExceptParamsSrcPortVal1,
       "aluNgeIPExceptParamsSrcPortVal2": aluNgeIPExceptParamsSrcPortVal2,
       "aluNgeIPExceptParamsSrcPortOpr": aluNgeIPExceptParamsSrcPortOpr,
       "aluNgeIPExceptParamsDestPortVal1": aluNgeIPExceptParamsDestPortVal1,
       "aluNgeIPExceptParamsDestPortVal2": aluNgeIPExceptParamsDestPortVal2,
       "aluNgeIPExceptParamsDestPortOpr": aluNgeIPExceptParamsDestPortOpr,
       "aluNgeIPExceptParamsIcmpCode": aluNgeIPExceptParamsIcmpCode,
       "aluNgeIPExceptParamsIcmpType": aluNgeIPExceptParamsIcmpType,
       "aluNgeIPExceptParmSrcIpFullMask": aluNgeIPExceptParmSrcIpFullMask,
       "aluNgeIPExceptParmDestIpFullMask": aluNgeIPExceptParmDestIpFullMask,
       "aluNgeIPExceptIngressHitCount": aluNgeIPExceptIngressHitCount,
       "aluNgeIPExceptEgressHitCount": aluNgeIPExceptEgressHitCount,
       "aluNgeIPExceptIngrHitByteCount": aluNgeIPExceptIngrHitByteCount,
       "aluNgeIPExceptEgressHitByteCount": aluNgeIPExceptEgressHitByteCount,
       "aluNgeKeygroupWlanGwBindingObjs": aluNgeKeygroupWlanGwBindingObjs,
       "aluNgeKeygroupWlanGwBindingTable": aluNgeKeygroupWlanGwBindingTable,
       "aluNgeKeygroupWlanGwBindingEntry": aluNgeKeygroupWlanGwBindingEntry,
       "aluNgeKeygroupWlanGwBindingInbound": aluNgeKeygroupWlanGwBindingInbound,
       "aluNgeKeygroupWlanGwBindingOutbound": aluNgeKeygroupWlanGwBindingOutbound,
       "aluNgeNotificationsPrefix": aluNgeNotificationsPrefix,
       "aluNgeNotifications": aluNgeNotifications}
)
