# SNMP MIB module (ENTERASYS-IEEE8021-CFM-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/enterasys/ENTERASYS-IEEE8021-CFM-EXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:46:51 2025
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(Dot1agCfmFngState,
 Dot1agCfmHighestDefectPri,
 Dot1agCfmLowestAlarmPri,
 Dot1agCfmMDLevel,
 Dot1agCfmMepDefects,
 Dot1agCfmMpDirection,
 dot1agCfmMaIndex,
 dot1agCfmMdIndex,
 dot1agCfmMepEntry) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmFngState",
    "Dot1agCfmHighestDefectPri",
    "Dot1agCfmLowestAlarmPri",
    "Dot1agCfmMDLevel",
    "Dot1agCfmMepDefects",
    "Dot1agCfmMpDirection",
    "dot1agCfmMaIndex",
    "dot1agCfmMdIndex",
    "dot1agCfmMepEntry")

(IEEE8021PbbComponentIdentifier,
 IEEE8021ServiceSelectorType,
 IEEE8021ServiceSelectorValue) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021PbbComponentIdentifier",
    "IEEE8021ServiceSelectorType",
    "IEEE8021ServiceSelectorValue")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

etsysIeee8021CfmMibExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524)
)
if mibBuilder.loadTexts:
    etsysIeee8021CfmMibExtMIB.setRevisions(
        ("2013-02-15 17:17",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EtsysIeee8021CfmExtMemPoolMaxSize(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5000),
    )



class EtsysIeee8021CfmExtMemPool(TextualConvention, Integer32):
    status = "current"
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
        *(("memPoolMD", 1),
          ("memPoolMA", 2),
          ("memPoolMEP", 3),
          ("memPoolMAMEP", 4),
          ("memPoolRMEP", 5),
          ("memPoolMHF", 6),
          ("memPoolMACOMP", 7))
    )



# MIB Managed Objects in the order of their OIDs

_EtsysIeee8021CfmMibExtObjects_ObjectIdentity = ObjectIdentity
etsysIeee8021CfmMibExtObjects = _EtsysIeee8021CfmMibExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1)
)
_EtsysIeee8021CfmExtGlobal_ObjectIdentity = ObjectIdentity
etsysIeee8021CfmExtGlobal = _EtsysIeee8021CfmExtGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 1)
)


class _EtsysIeee8021CfmExtStatus_Type(EnabledStatus):
    """Custom type etsysIeee8021CfmExtStatus based on EnabledStatus"""
    defaultValue = 2


_EtsysIeee8021CfmExtStatus_Type.__name__ = "EnabledStatus"
_EtsysIeee8021CfmExtStatus_Object = MibScalar
etsysIeee8021CfmExtStatus = _EtsysIeee8021CfmExtStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 1, 1),
    _EtsysIeee8021CfmExtStatus_Type()
)
etsysIeee8021CfmExtStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysIeee8021CfmExtStatus.setStatus("current")
_EtsysIeee8021CfmExtMemPoolTable_Object = MibTable
etsysIeee8021CfmExtMemPoolTable = _EtsysIeee8021CfmExtMemPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 1, 2)
)
if mibBuilder.loadTexts:
    etsysIeee8021CfmExtMemPoolTable.setStatus("current")
_EtsysIeee8021CfmExtMemPoolEntry_Object = MibTableRow
etsysIeee8021CfmExtMemPoolEntry = _EtsysIeee8021CfmExtMemPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 1, 2, 1)
)
etsysIeee8021CfmExtMemPoolEntry.setIndexNames(
    (0, "ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmExtMemPoolIndex"),
)
if mibBuilder.loadTexts:
    etsysIeee8021CfmExtMemPoolEntry.setStatus("current")
_EtsysIeee8021CfmExtMemPoolIndex_Type = EtsysIeee8021CfmExtMemPool
_EtsysIeee8021CfmExtMemPoolIndex_Object = MibTableColumn
etsysIeee8021CfmExtMemPoolIndex = _EtsysIeee8021CfmExtMemPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 1, 2, 1, 1),
    _EtsysIeee8021CfmExtMemPoolIndex_Type()
)
etsysIeee8021CfmExtMemPoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysIeee8021CfmExtMemPoolIndex.setStatus("current")
_EtsysIeee8021CfmExtMemPoolSize_Type = EtsysIeee8021CfmExtMemPoolMaxSize
_EtsysIeee8021CfmExtMemPoolSize_Object = MibTableColumn
etsysIeee8021CfmExtMemPoolSize = _EtsysIeee8021CfmExtMemPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 1, 2, 1, 2),
    _EtsysIeee8021CfmExtMemPoolSize_Type()
)
etsysIeee8021CfmExtMemPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIeee8021CfmExtMemPoolSize.setStatus("current")
_EtsysIeee8021CfmExtMemPoolInUse_Type = EtsysIeee8021CfmExtMemPoolMaxSize
_EtsysIeee8021CfmExtMemPoolInUse_Object = MibTableColumn
etsysIeee8021CfmExtMemPoolInUse = _EtsysIeee8021CfmExtMemPoolInUse_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 1, 2, 1, 3),
    _EtsysIeee8021CfmExtMemPoolInUse_Type()
)
etsysIeee8021CfmExtMemPoolInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIeee8021CfmExtMemPoolInUse.setStatus("current")
_EtsysIeee8021CfmExtMemPoolHighWaterMark_Type = EtsysIeee8021CfmExtMemPoolMaxSize
_EtsysIeee8021CfmExtMemPoolHighWaterMark_Object = MibTableColumn
etsysIeee8021CfmExtMemPoolHighWaterMark = _EtsysIeee8021CfmExtMemPoolHighWaterMark_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 1, 2, 1, 4),
    _EtsysIeee8021CfmExtMemPoolHighWaterMark_Type()
)
etsysIeee8021CfmExtMemPoolHighWaterMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIeee8021CfmExtMemPoolHighWaterMark.setStatus("current")
_EtsysIeee8021CfmMipCcmDbTable_Object = MibTable
etsysIeee8021CfmMipCcmDbTable = _EtsysIeee8021CfmMipCcmDbTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 1, 3)
)
if mibBuilder.loadTexts:
    etsysIeee8021CfmMipCcmDbTable.setStatus("current")
_EtsysIeee8021CfmMipCcmDbEntry_Object = MibTableRow
etsysIeee8021CfmMipCcmDbEntry = _EtsysIeee8021CfmMipCcmDbEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 1, 3, 1)
)
etsysIeee8021CfmMipCcmDbEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmMipCcmDbMpIdentifier"),
    (0, "ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmMipCcmDbFid"),
    (0, "ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmMipCcmDbMacAddress"),
)
if mibBuilder.loadTexts:
    etsysIeee8021CfmMipCcmDbEntry.setStatus("current")


class _EtsysIeee8021CfmMipCcmDbMpIdentifier_Type(Unsigned32):
    """Custom type etsysIeee8021CfmMipCcmDbMpIdentifier based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
        ValueRangeConstraint(16383, 32767),
    )


_EtsysIeee8021CfmMipCcmDbMpIdentifier_Type.__name__ = "Unsigned32"
_EtsysIeee8021CfmMipCcmDbMpIdentifier_Object = MibTableColumn
etsysIeee8021CfmMipCcmDbMpIdentifier = _EtsysIeee8021CfmMipCcmDbMpIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 1, 3, 1, 1),
    _EtsysIeee8021CfmMipCcmDbMpIdentifier_Type()
)
etsysIeee8021CfmMipCcmDbMpIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysIeee8021CfmMipCcmDbMpIdentifier.setStatus("current")


class _EtsysIeee8021CfmMipCcmDbFid_Type(Unsigned32):
    """Custom type etsysIeee8021CfmMipCcmDbFid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_EtsysIeee8021CfmMipCcmDbFid_Type.__name__ = "Unsigned32"
_EtsysIeee8021CfmMipCcmDbFid_Object = MibTableColumn
etsysIeee8021CfmMipCcmDbFid = _EtsysIeee8021CfmMipCcmDbFid_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 1, 3, 1, 2),
    _EtsysIeee8021CfmMipCcmDbFid_Type()
)
etsysIeee8021CfmMipCcmDbFid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysIeee8021CfmMipCcmDbFid.setStatus("current")
_EtsysIeee8021CfmMipCcmDbMacAddress_Type = MacAddress
_EtsysIeee8021CfmMipCcmDbMacAddress_Object = MibTableColumn
etsysIeee8021CfmMipCcmDbMacAddress = _EtsysIeee8021CfmMipCcmDbMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 1, 3, 1, 3),
    _EtsysIeee8021CfmMipCcmDbMacAddress_Type()
)
etsysIeee8021CfmMipCcmDbMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysIeee8021CfmMipCcmDbMacAddress.setStatus("current")
_EtsysIeee8021CfmMipCcmDbMpIfIndex_Type = InterfaceIndexOrZero
_EtsysIeee8021CfmMipCcmDbMpIfIndex_Object = MibTableColumn
etsysIeee8021CfmMipCcmDbMpIfIndex = _EtsysIeee8021CfmMipCcmDbMpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 1, 3, 1, 4),
    _EtsysIeee8021CfmMipCcmDbMpIfIndex_Type()
)
etsysIeee8021CfmMipCcmDbMpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIeee8021CfmMipCcmDbMpIfIndex.setStatus("current")
_EtsysIeee8021CfmMipCcmDbMpMdLevel_Type = Dot1agCfmMDLevel
_EtsysIeee8021CfmMipCcmDbMpMdLevel_Object = MibTableColumn
etsysIeee8021CfmMipCcmDbMpMdLevel = _EtsysIeee8021CfmMipCcmDbMpMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 1, 3, 1, 5),
    _EtsysIeee8021CfmMipCcmDbMpMdLevel_Type()
)
etsysIeee8021CfmMipCcmDbMpMdLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIeee8021CfmMipCcmDbMpMdLevel.setStatus("current")
_EtsysIeee8021CfmMipCcmDbMpDirection_Type = Dot1agCfmMpDirection
_EtsysIeee8021CfmMipCcmDbMpDirection_Object = MibTableColumn
etsysIeee8021CfmMipCcmDbMpDirection = _EtsysIeee8021CfmMipCcmDbMpDirection_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 1, 3, 1, 6),
    _EtsysIeee8021CfmMipCcmDbMpDirection_Type()
)
etsysIeee8021CfmMipCcmDbMpDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIeee8021CfmMipCcmDbMpDirection.setStatus("current")
_EtsysIeee8021CfmMipCcmDbLearnedIfIndex_Type = InterfaceIndexOrZero
_EtsysIeee8021CfmMipCcmDbLearnedIfIndex_Object = MibTableColumn
etsysIeee8021CfmMipCcmDbLearnedIfIndex = _EtsysIeee8021CfmMipCcmDbLearnedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 1, 3, 1, 7),
    _EtsysIeee8021CfmMipCcmDbLearnedIfIndex_Type()
)
etsysIeee8021CfmMipCcmDbLearnedIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIeee8021CfmMipCcmDbLearnedIfIndex.setStatus("current")
_EtsysIeee8021CfmMipCcmDbTimeStamp_Type = TimeStamp
_EtsysIeee8021CfmMipCcmDbTimeStamp_Object = MibTableColumn
etsysIeee8021CfmMipCcmDbTimeStamp = _EtsysIeee8021CfmMipCcmDbTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 1, 3, 1, 8),
    _EtsysIeee8021CfmMipCcmDbTimeStamp_Type()
)
etsysIeee8021CfmMipCcmDbTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIeee8021CfmMipCcmDbTimeStamp.setStatus("current")
_EtsysIeee8021CfmMipCcmDbComponentId_Type = IEEE8021PbbComponentIdentifier
_EtsysIeee8021CfmMipCcmDbComponentId_Object = MibTableColumn
etsysIeee8021CfmMipCcmDbComponentId = _EtsysIeee8021CfmMipCcmDbComponentId_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 1, 3, 1, 9),
    _EtsysIeee8021CfmMipCcmDbComponentId_Type()
)
etsysIeee8021CfmMipCcmDbComponentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIeee8021CfmMipCcmDbComponentId.setStatus("current")
_EtsysIeee8021CfmMipCcmDbPrimarySelectorType_Type = IEEE8021ServiceSelectorType
_EtsysIeee8021CfmMipCcmDbPrimarySelectorType_Object = MibTableColumn
etsysIeee8021CfmMipCcmDbPrimarySelectorType = _EtsysIeee8021CfmMipCcmDbPrimarySelectorType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 1, 3, 1, 10),
    _EtsysIeee8021CfmMipCcmDbPrimarySelectorType_Type()
)
etsysIeee8021CfmMipCcmDbPrimarySelectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIeee8021CfmMipCcmDbPrimarySelectorType.setStatus("current")
_EtsysIeee8021CfmMipCcmDbPrimarySelector_Type = IEEE8021ServiceSelectorValue
_EtsysIeee8021CfmMipCcmDbPrimarySelector_Object = MibTableColumn
etsysIeee8021CfmMipCcmDbPrimarySelector = _EtsysIeee8021CfmMipCcmDbPrimarySelector_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 1, 3, 1, 11),
    _EtsysIeee8021CfmMipCcmDbPrimarySelector_Type()
)
etsysIeee8021CfmMipCcmDbPrimarySelector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIeee8021CfmMipCcmDbPrimarySelector.setStatus("current")


class _EtsysIeee8021CfmClearBridgeCcmDatabase_Type(TruthValue):
    """Custom type etsysIeee8021CfmClearBridgeCcmDatabase based on TruthValue"""
    defaultValue = 2


_EtsysIeee8021CfmClearBridgeCcmDatabase_Type.__name__ = "TruthValue"
_EtsysIeee8021CfmClearBridgeCcmDatabase_Object = MibScalar
etsysIeee8021CfmClearBridgeCcmDatabase = _EtsysIeee8021CfmClearBridgeCcmDatabase_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 1, 4),
    _EtsysIeee8021CfmClearBridgeCcmDatabase_Type()
)
etsysIeee8021CfmClearBridgeCcmDatabase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysIeee8021CfmClearBridgeCcmDatabase.setStatus("current")
_EtsysIeee8021CfmExtMep_ObjectIdentity = ObjectIdentity
etsysIeee8021CfmExtMep = _EtsysIeee8021CfmExtMep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 2)
)
_EtsysIeee8021CfmExtMepTable_Object = MibTable
etsysIeee8021CfmExtMepTable = _EtsysIeee8021CfmExtMepTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 2, 1)
)
if mibBuilder.loadTexts:
    etsysIeee8021CfmExtMepTable.setStatus("current")
_EtsysIeee8021CfmExtMepEntry_Object = MibTableRow
etsysIeee8021CfmExtMepEntry = _EtsysIeee8021CfmExtMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    etsysIeee8021CfmExtMepEntry.setStatus("current")


class _EtsysIeee8021CfmExtMepLowPrDefSyslog_Type(Dot1agCfmLowestAlarmPri):
    """Custom type etsysIeee8021CfmExtMepLowPrDefSyslog based on Dot1agCfmLowestAlarmPri"""
    defaultValue = 2


_EtsysIeee8021CfmExtMepLowPrDefSyslog_Type.__name__ = "Dot1agCfmLowestAlarmPri"
_EtsysIeee8021CfmExtMepLowPrDefSyslog_Object = MibTableColumn
etsysIeee8021CfmExtMepLowPrDefSyslog = _EtsysIeee8021CfmExtMepLowPrDefSyslog_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 2, 1, 1, 1),
    _EtsysIeee8021CfmExtMepLowPrDefSyslog_Type()
)
etsysIeee8021CfmExtMepLowPrDefSyslog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysIeee8021CfmExtMepLowPrDefSyslog.setStatus("current")
_EtsysIeee8021CfmExtMepFngStateSyslog_Type = Dot1agCfmFngState
_EtsysIeee8021CfmExtMepFngStateSyslog_Object = MibTableColumn
etsysIeee8021CfmExtMepFngStateSyslog = _EtsysIeee8021CfmExtMepFngStateSyslog_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 2, 1, 1, 2),
    _EtsysIeee8021CfmExtMepFngStateSyslog_Type()
)
etsysIeee8021CfmExtMepFngStateSyslog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIeee8021CfmExtMepFngStateSyslog.setStatus("current")
_EtsysIeee8021CfmExtMepHighestPrDefectSyslog_Type = Dot1agCfmHighestDefectPri
_EtsysIeee8021CfmExtMepHighestPrDefectSyslog_Object = MibTableColumn
etsysIeee8021CfmExtMepHighestPrDefectSyslog = _EtsysIeee8021CfmExtMepHighestPrDefectSyslog_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 2, 1, 1, 3),
    _EtsysIeee8021CfmExtMepHighestPrDefectSyslog_Type()
)
etsysIeee8021CfmExtMepHighestPrDefectSyslog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIeee8021CfmExtMepHighestPrDefectSyslog.setStatus("current")
_EtsysIeee8021CfmExtMepDefectsSyslog_Type = Dot1agCfmMepDefects
_EtsysIeee8021CfmExtMepDefectsSyslog_Object = MibTableColumn
etsysIeee8021CfmExtMepDefectsSyslog = _EtsysIeee8021CfmExtMepDefectsSyslog_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 2, 1, 1, 4),
    _EtsysIeee8021CfmExtMepDefectsSyslog_Type()
)
etsysIeee8021CfmExtMepDefectsSyslog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIeee8021CfmExtMepDefectsSyslog.setStatus("current")
_EtsysIeee8021CfmExtMepClearCcmDatabase_Type = TruthValue
_EtsysIeee8021CfmExtMepClearCcmDatabase_Object = MibTableColumn
etsysIeee8021CfmExtMepClearCcmDatabase = _EtsysIeee8021CfmExtMepClearCcmDatabase_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 2, 1, 1, 5),
    _EtsysIeee8021CfmExtMepClearCcmDatabase_Type()
)
etsysIeee8021CfmExtMepClearCcmDatabase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysIeee8021CfmExtMepClearCcmDatabase.setStatus("current")
_EtsysIeee8021CfmExtRxDiscardCount_Type = Counter32
_EtsysIeee8021CfmExtRxDiscardCount_Object = MibTableColumn
etsysIeee8021CfmExtRxDiscardCount = _EtsysIeee8021CfmExtRxDiscardCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 2, 1, 1, 6),
    _EtsysIeee8021CfmExtRxDiscardCount_Type()
)
etsysIeee8021CfmExtRxDiscardCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIeee8021CfmExtRxDiscardCount.setStatus("current")
_EtsysIeee8021CfmExtRxForwardCount_Type = Counter32
_EtsysIeee8021CfmExtRxForwardCount_Object = MibTableColumn
etsysIeee8021CfmExtRxForwardCount = _EtsysIeee8021CfmExtRxForwardCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 2, 1, 1, 7),
    _EtsysIeee8021CfmExtRxForwardCount_Type()
)
etsysIeee8021CfmExtRxForwardCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIeee8021CfmExtRxForwardCount.setStatus("current")
_EtsysIeee8021CfmExtRxErrorCount_Type = Counter32
_EtsysIeee8021CfmExtRxErrorCount_Object = MibTableColumn
etsysIeee8021CfmExtRxErrorCount = _EtsysIeee8021CfmExtRxErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 2, 1, 1, 8),
    _EtsysIeee8021CfmExtRxErrorCount_Type()
)
etsysIeee8021CfmExtRxErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIeee8021CfmExtRxErrorCount.setStatus("current")
_EtsysIeee8021CfmExtTxErrorCount_Type = Counter32
_EtsysIeee8021CfmExtTxErrorCount_Object = MibTableColumn
etsysIeee8021CfmExtTxErrorCount = _EtsysIeee8021CfmExtTxErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 2, 1, 1, 9),
    _EtsysIeee8021CfmExtTxErrorCount_Type()
)
etsysIeee8021CfmExtTxErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIeee8021CfmExtTxErrorCount.setStatus("current")
_EtsysIeee8021CfmExtMepRxCcmCount_Type = Counter32
_EtsysIeee8021CfmExtMepRxCcmCount_Object = MibTableColumn
etsysIeee8021CfmExtMepRxCcmCount = _EtsysIeee8021CfmExtMepRxCcmCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 2, 1, 1, 10),
    _EtsysIeee8021CfmExtMepRxCcmCount_Type()
)
etsysIeee8021CfmExtMepRxCcmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIeee8021CfmExtMepRxCcmCount.setStatus("current")
_EtsysIeee8021CfmExtMepRxCcmErrCount_Type = Counter32
_EtsysIeee8021CfmExtMepRxCcmErrCount_Object = MibTableColumn
etsysIeee8021CfmExtMepRxCcmErrCount = _EtsysIeee8021CfmExtMepRxCcmErrCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 2, 1, 1, 11),
    _EtsysIeee8021CfmExtMepRxCcmErrCount_Type()
)
etsysIeee8021CfmExtMepRxCcmErrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIeee8021CfmExtMepRxCcmErrCount.setStatus("current")
_EtsysIeee8021CfmExtMepRxCcmXconCount_Type = Counter32
_EtsysIeee8021CfmExtMepRxCcmXconCount_Object = MibTableColumn
etsysIeee8021CfmExtMepRxCcmXconCount = _EtsysIeee8021CfmExtMepRxCcmXconCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 2, 1, 1, 12),
    _EtsysIeee8021CfmExtMepRxCcmXconCount_Type()
)
etsysIeee8021CfmExtMepRxCcmXconCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIeee8021CfmExtMepRxCcmXconCount.setStatus("current")
_EtsysIeee8021CfmExtMepTxCcmCount_Type = Counter32
_EtsysIeee8021CfmExtMepTxCcmCount_Object = MibTableColumn
etsysIeee8021CfmExtMepTxCcmCount = _EtsysIeee8021CfmExtMepTxCcmCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 2, 1, 1, 13),
    _EtsysIeee8021CfmExtMepTxCcmCount_Type()
)
etsysIeee8021CfmExtMepTxCcmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIeee8021CfmExtMepTxCcmCount.setStatus("current")
_EtsysIeee8021CfmExtMepTxCcmErrCount_Type = Counter32
_EtsysIeee8021CfmExtMepTxCcmErrCount_Object = MibTableColumn
etsysIeee8021CfmExtMepTxCcmErrCount = _EtsysIeee8021CfmExtMepTxCcmErrCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 2, 1, 1, 14),
    _EtsysIeee8021CfmExtMepTxCcmErrCount_Type()
)
etsysIeee8021CfmExtMepTxCcmErrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIeee8021CfmExtMepTxCcmErrCount.setStatus("current")
_EtsysIeee8021CfmExtMepRxLbmCount_Type = Counter32
_EtsysIeee8021CfmExtMepRxLbmCount_Object = MibTableColumn
etsysIeee8021CfmExtMepRxLbmCount = _EtsysIeee8021CfmExtMepRxLbmCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 2, 1, 1, 15),
    _EtsysIeee8021CfmExtMepRxLbmCount_Type()
)
etsysIeee8021CfmExtMepRxLbmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIeee8021CfmExtMepRxLbmCount.setStatus("current")
_EtsysIeee8021CfmExtMepTxLbmCount_Type = Counter32
_EtsysIeee8021CfmExtMepTxLbmCount_Object = MibTableColumn
etsysIeee8021CfmExtMepTxLbmCount = _EtsysIeee8021CfmExtMepTxLbmCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 2, 1, 1, 16),
    _EtsysIeee8021CfmExtMepTxLbmCount_Type()
)
etsysIeee8021CfmExtMepTxLbmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIeee8021CfmExtMepTxLbmCount.setStatus("current")
_EtsysIeee8021CfmExtMepRxLbrCount_Type = Counter32
_EtsysIeee8021CfmExtMepRxLbrCount_Object = MibTableColumn
etsysIeee8021CfmExtMepRxLbrCount = _EtsysIeee8021CfmExtMepRxLbrCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 2, 1, 1, 17),
    _EtsysIeee8021CfmExtMepRxLbrCount_Type()
)
etsysIeee8021CfmExtMepRxLbrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIeee8021CfmExtMepRxLbrCount.setStatus("current")
_EtsysIeee8021CfmExtMepTxLbrCount_Type = Counter32
_EtsysIeee8021CfmExtMepTxLbrCount_Object = MibTableColumn
etsysIeee8021CfmExtMepTxLbrCount = _EtsysIeee8021CfmExtMepTxLbrCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 2, 1, 1, 18),
    _EtsysIeee8021CfmExtMepTxLbrCount_Type()
)
etsysIeee8021CfmExtMepTxLbrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIeee8021CfmExtMepTxLbrCount.setStatus("current")
_EtsysIeee8021CfmExtMepRxLtmCount_Type = Counter32
_EtsysIeee8021CfmExtMepRxLtmCount_Object = MibTableColumn
etsysIeee8021CfmExtMepRxLtmCount = _EtsysIeee8021CfmExtMepRxLtmCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 2, 1, 1, 19),
    _EtsysIeee8021CfmExtMepRxLtmCount_Type()
)
etsysIeee8021CfmExtMepRxLtmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIeee8021CfmExtMepRxLtmCount.setStatus("current")
_EtsysIeee8021CfmExtMepTxLtmCount_Type = Counter32
_EtsysIeee8021CfmExtMepTxLtmCount_Object = MibTableColumn
etsysIeee8021CfmExtMepTxLtmCount = _EtsysIeee8021CfmExtMepTxLtmCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 2, 1, 1, 20),
    _EtsysIeee8021CfmExtMepTxLtmCount_Type()
)
etsysIeee8021CfmExtMepTxLtmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIeee8021CfmExtMepTxLtmCount.setStatus("current")
_EtsysIeee8021CfmExtMepRxLtrCount_Type = Counter32
_EtsysIeee8021CfmExtMepRxLtrCount_Object = MibTableColumn
etsysIeee8021CfmExtMepRxLtrCount = _EtsysIeee8021CfmExtMepRxLtrCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 2, 1, 1, 21),
    _EtsysIeee8021CfmExtMepRxLtrCount_Type()
)
etsysIeee8021CfmExtMepRxLtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIeee8021CfmExtMepRxLtrCount.setStatus("current")
_EtsysIeee8021CfmExtMepTxLtrCount_Type = Counter32
_EtsysIeee8021CfmExtMepTxLtrCount_Object = MibTableColumn
etsysIeee8021CfmExtMepTxLtrCount = _EtsysIeee8021CfmExtMepTxLtrCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 2, 1, 1, 22),
    _EtsysIeee8021CfmExtMepTxLtrCount_Type()
)
etsysIeee8021CfmExtMepTxLtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIeee8021CfmExtMepTxLtrCount.setStatus("current")
_EtsysIeee8021CfmExtMepClearMepCounters_Type = TruthValue
_EtsysIeee8021CfmExtMepClearMepCounters_Object = MibTableColumn
etsysIeee8021CfmExtMepClearMepCounters = _EtsysIeee8021CfmExtMepClearMepCounters_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 1, 2, 1, 1, 23),
    _EtsysIeee8021CfmExtMepClearMepCounters_Type()
)
etsysIeee8021CfmExtMepClearMepCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysIeee8021CfmExtMepClearMepCounters.setStatus("current")
_EtsysIeee8021CfmMibExtConformance_ObjectIdentity = ObjectIdentity
etsysIeee8021CfmMibExtConformance = _EtsysIeee8021CfmMibExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 2)
)
_EtsysIeee8021CfmMibExtGroups_ObjectIdentity = ObjectIdentity
etsysIeee8021CfmMibExtGroups = _EtsysIeee8021CfmMibExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 2, 1)
)
_EtsysIeee8021CfmMibExtCompliances_ObjectIdentity = ObjectIdentity
etsysIeee8021CfmMibExtCompliances = _EtsysIeee8021CfmMibExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 2, 2)
)
dot1agCfmMepEntry.registerAugmentions(
    ("ENTERASYS-IEEE8021-CFM-EXT-MIB",
     "etsysIeee8021CfmExtMepEntry")
)
etsysIeee8021CfmExtMepEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())

# Managed Objects groups

etsysIeee8021CfmExtStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 2, 1, 1)
)
etsysIeee8021CfmExtStatusGroup.setObjects(
    ("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmExtStatus")
)
if mibBuilder.loadTexts:
    etsysIeee8021CfmExtStatusGroup.setStatus("current")

etsysIeee8021CfmExtMemPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 2, 1, 2)
)
etsysIeee8021CfmExtMemPoolGroup.setObjects(
      *(("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmExtMemPoolSize"),
        ("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmExtMemPoolInUse"),
        ("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmExtMemPoolHighWaterMark"))
)
if mibBuilder.loadTexts:
    etsysIeee8021CfmExtMemPoolGroup.setStatus("current")

etsysIeee8021CfmExtMepGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 2, 1, 3)
)
etsysIeee8021CfmExtMepGroup.setObjects(
      *(("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmExtMepLowPrDefSyslog"),
        ("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmExtMepFngStateSyslog"),
        ("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmExtMepHighestPrDefectSyslog"),
        ("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmExtMepDefectsSyslog"),
        ("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmExtMepClearCcmDatabase"),
        ("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmExtRxDiscardCount"),
        ("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmExtRxForwardCount"),
        ("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmExtRxErrorCount"),
        ("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmExtTxErrorCount"),
        ("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmExtMepRxCcmCount"),
        ("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmExtMepRxCcmErrCount"),
        ("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmExtMepRxCcmXconCount"),
        ("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmExtMepTxCcmCount"),
        ("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmExtMepTxCcmErrCount"),
        ("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmExtMepRxLbmCount"),
        ("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmExtMepTxLbmCount"),
        ("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmExtMepRxLbrCount"),
        ("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmExtMepTxLbrCount"),
        ("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmExtMepRxLtmCount"),
        ("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmExtMepTxLtmCount"),
        ("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmExtMepRxLtrCount"),
        ("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmExtMepTxLtrCount"),
        ("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmExtMepClearMepCounters"))
)
if mibBuilder.loadTexts:
    etsysIeee8021CfmExtMepGroup.setStatus("current")

etsysIeee8021CfmExtMipGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 2, 1, 4)
)
etsysIeee8021CfmExtMipGroup.setObjects(
      *(("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmMipCcmDbMpIfIndex"),
        ("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmMipCcmDbMpMdLevel"),
        ("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmMipCcmDbMpDirection"),
        ("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmMipCcmDbLearnedIfIndex"),
        ("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmMipCcmDbTimeStamp"),
        ("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmMipCcmDbComponentId"),
        ("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmMipCcmDbPrimarySelectorType"),
        ("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmMipCcmDbPrimarySelector"))
)
if mibBuilder.loadTexts:
    etsysIeee8021CfmExtMipGroup.setStatus("current")

etsysIeee8021CfmClearBridgeCcmDatabaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 2, 1, 5)
)
etsysIeee8021CfmClearBridgeCcmDatabaseGroup.setObjects(
    ("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmClearBridgeCcmDatabase")
)
if mibBuilder.loadTexts:
    etsysIeee8021CfmClearBridgeCcmDatabaseGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysIeee8021CfmMibExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 524, 2, 2, 1)
)
etsysIeee8021CfmMibExtCompliance.setObjects(
      *(("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmExtStatusGroup"),
        ("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmExtMemPoolGroup"),
        ("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmExtMepGroup"),
        ("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmExtMipGroup"),
        ("ENTERASYS-IEEE8021-CFM-EXT-MIB", "etsysIeee8021CfmClearBridgeCcmDatabaseGroup"))
)
if mibBuilder.loadTexts:
    etsysIeee8021CfmMibExtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-IEEE8021-CFM-EXT-MIB",
    **{"EtsysIeee8021CfmExtMemPoolMaxSize": EtsysIeee8021CfmExtMemPoolMaxSize,
       "EtsysIeee8021CfmExtMemPool": EtsysIeee8021CfmExtMemPool,
       "etsysIeee8021CfmMibExtMIB": etsysIeee8021CfmMibExtMIB,
       "etsysIeee8021CfmMibExtObjects": etsysIeee8021CfmMibExtObjects,
       "etsysIeee8021CfmExtGlobal": etsysIeee8021CfmExtGlobal,
       "etsysIeee8021CfmExtStatus": etsysIeee8021CfmExtStatus,
       "etsysIeee8021CfmExtMemPoolTable": etsysIeee8021CfmExtMemPoolTable,
       "etsysIeee8021CfmExtMemPoolEntry": etsysIeee8021CfmExtMemPoolEntry,
       "etsysIeee8021CfmExtMemPoolIndex": etsysIeee8021CfmExtMemPoolIndex,
       "etsysIeee8021CfmExtMemPoolSize": etsysIeee8021CfmExtMemPoolSize,
       "etsysIeee8021CfmExtMemPoolInUse": etsysIeee8021CfmExtMemPoolInUse,
       "etsysIeee8021CfmExtMemPoolHighWaterMark": etsysIeee8021CfmExtMemPoolHighWaterMark,
       "etsysIeee8021CfmMipCcmDbTable": etsysIeee8021CfmMipCcmDbTable,
       "etsysIeee8021CfmMipCcmDbEntry": etsysIeee8021CfmMipCcmDbEntry,
       "etsysIeee8021CfmMipCcmDbMpIdentifier": etsysIeee8021CfmMipCcmDbMpIdentifier,
       "etsysIeee8021CfmMipCcmDbFid": etsysIeee8021CfmMipCcmDbFid,
       "etsysIeee8021CfmMipCcmDbMacAddress": etsysIeee8021CfmMipCcmDbMacAddress,
       "etsysIeee8021CfmMipCcmDbMpIfIndex": etsysIeee8021CfmMipCcmDbMpIfIndex,
       "etsysIeee8021CfmMipCcmDbMpMdLevel": etsysIeee8021CfmMipCcmDbMpMdLevel,
       "etsysIeee8021CfmMipCcmDbMpDirection": etsysIeee8021CfmMipCcmDbMpDirection,
       "etsysIeee8021CfmMipCcmDbLearnedIfIndex": etsysIeee8021CfmMipCcmDbLearnedIfIndex,
       "etsysIeee8021CfmMipCcmDbTimeStamp": etsysIeee8021CfmMipCcmDbTimeStamp,
       "etsysIeee8021CfmMipCcmDbComponentId": etsysIeee8021CfmMipCcmDbComponentId,
       "etsysIeee8021CfmMipCcmDbPrimarySelectorType": etsysIeee8021CfmMipCcmDbPrimarySelectorType,
       "etsysIeee8021CfmMipCcmDbPrimarySelector": etsysIeee8021CfmMipCcmDbPrimarySelector,
       "etsysIeee8021CfmClearBridgeCcmDatabase": etsysIeee8021CfmClearBridgeCcmDatabase,
       "etsysIeee8021CfmExtMep": etsysIeee8021CfmExtMep,
       "etsysIeee8021CfmExtMepTable": etsysIeee8021CfmExtMepTable,
       "etsysIeee8021CfmExtMepEntry": etsysIeee8021CfmExtMepEntry,
       "etsysIeee8021CfmExtMepLowPrDefSyslog": etsysIeee8021CfmExtMepLowPrDefSyslog,
       "etsysIeee8021CfmExtMepFngStateSyslog": etsysIeee8021CfmExtMepFngStateSyslog,
       "etsysIeee8021CfmExtMepHighestPrDefectSyslog": etsysIeee8021CfmExtMepHighestPrDefectSyslog,
       "etsysIeee8021CfmExtMepDefectsSyslog": etsysIeee8021CfmExtMepDefectsSyslog,
       "etsysIeee8021CfmExtMepClearCcmDatabase": etsysIeee8021CfmExtMepClearCcmDatabase,
       "etsysIeee8021CfmExtRxDiscardCount": etsysIeee8021CfmExtRxDiscardCount,
       "etsysIeee8021CfmExtRxForwardCount": etsysIeee8021CfmExtRxForwardCount,
       "etsysIeee8021CfmExtRxErrorCount": etsysIeee8021CfmExtRxErrorCount,
       "etsysIeee8021CfmExtTxErrorCount": etsysIeee8021CfmExtTxErrorCount,
       "etsysIeee8021CfmExtMepRxCcmCount": etsysIeee8021CfmExtMepRxCcmCount,
       "etsysIeee8021CfmExtMepRxCcmErrCount": etsysIeee8021CfmExtMepRxCcmErrCount,
       "etsysIeee8021CfmExtMepRxCcmXconCount": etsysIeee8021CfmExtMepRxCcmXconCount,
       "etsysIeee8021CfmExtMepTxCcmCount": etsysIeee8021CfmExtMepTxCcmCount,
       "etsysIeee8021CfmExtMepTxCcmErrCount": etsysIeee8021CfmExtMepTxCcmErrCount,
       "etsysIeee8021CfmExtMepRxLbmCount": etsysIeee8021CfmExtMepRxLbmCount,
       "etsysIeee8021CfmExtMepTxLbmCount": etsysIeee8021CfmExtMepTxLbmCount,
       "etsysIeee8021CfmExtMepRxLbrCount": etsysIeee8021CfmExtMepRxLbrCount,
       "etsysIeee8021CfmExtMepTxLbrCount": etsysIeee8021CfmExtMepTxLbrCount,
       "etsysIeee8021CfmExtMepRxLtmCount": etsysIeee8021CfmExtMepRxLtmCount,
       "etsysIeee8021CfmExtMepTxLtmCount": etsysIeee8021CfmExtMepTxLtmCount,
       "etsysIeee8021CfmExtMepRxLtrCount": etsysIeee8021CfmExtMepRxLtrCount,
       "etsysIeee8021CfmExtMepTxLtrCount": etsysIeee8021CfmExtMepTxLtrCount,
       "etsysIeee8021CfmExtMepClearMepCounters": etsysIeee8021CfmExtMepClearMepCounters,
       "etsysIeee8021CfmMibExtConformance": etsysIeee8021CfmMibExtConformance,
       "etsysIeee8021CfmMibExtGroups": etsysIeee8021CfmMibExtGroups,
       "etsysIeee8021CfmExtStatusGroup": etsysIeee8021CfmExtStatusGroup,
       "etsysIeee8021CfmExtMemPoolGroup": etsysIeee8021CfmExtMemPoolGroup,
       "etsysIeee8021CfmExtMepGroup": etsysIeee8021CfmExtMepGroup,
       "etsysIeee8021CfmExtMipGroup": etsysIeee8021CfmExtMipGroup,
       "etsysIeee8021CfmClearBridgeCcmDatabaseGroup": etsysIeee8021CfmClearBridgeCcmDatabaseGroup,
       "etsysIeee8021CfmMibExtCompliances": etsysIeee8021CfmMibExtCompliances,
       "etsysIeee8021CfmMibExtCompliance": etsysIeee8021CfmMibExtCompliance}
)
