# SNMP MIB module (TN-RMD-CFM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TN-RMD-CFM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:50:17 2025
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

(Dot1agCfmCcmInterval,
 Dot1agCfmMDLevel,
 Dot1agCfmMaintAssocName,
 Dot1agCfmMaintAssocNameType,
 Dot1agCfmMaintDomainName,
 Dot1agCfmMaintDomainNameType,
 Dot1agCfmMepId,
 Dot1agCfmMpDirection,
 VlanIdOrNone) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmCcmInterval",
    "Dot1agCfmMDLevel",
    "Dot1agCfmMaintAssocName",
    "Dot1agCfmMaintAssocNameType",
    "Dot1agCfmMaintDomainName",
    "Dot1agCfmMaintDomainNameType",
    "Dot1agCfmMepId",
    "Dot1agCfmMpDirection",
    "VlanIdOrNone")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(tnRmdSystemId,) = mibBuilder.importSymbols(
    "TN-RMD-SYSTEM-MIB",
    "tnRmdSystemId")

(tnRmdMIBModules,
 tnRmdObjs) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnRmdMIBModules",
    "tnRmdObjs")

(tnSysSwitchId,) = mibBuilder.importSymbols(
    "TROPIC-SYSTEM-MIB",
    "tnSysSwitchId")


# MODULE-IDENTITY

tnRmdCfmMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 5, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tnRmdCfmMibModule.setRevisions(
        ("2020-11-13 12:00",
         "2020-11-06 12:00",
         "2020-10-09 12:00",
         "2018-02-23 12:00",
         "2016-11-16 00:00",
         "2012-11-28 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TnRmdCfmDmInitiatorSessionMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cfmDmInitiatorSessionModeNormal", 0),
          ("cfmDmInitiatorSessionModeTest", 1))
    )



class TnRmdCfmDmTestMeasurementInterval(TextualConvention, Unsigned32):
    status = "current"


class TnRmdCfmInitiatorSessionState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cfmInitiatorSessionRunning", 0),
          ("cfmInitiatorSessionStopped", 1))
    )



class TnRmdCfmInitiatorSessionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cfmInitiatorSessionTypeOnDemand", 0),
          ("cfmInitiatorSessionTypeProActive", 1))
    )



class TnRmdCfmMegId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(48, 48),
    )
    fixed_length = 48



class TnRmdCfmMepDefect(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("unl", 0),
          ("mmg", 1),
          ("unm", 2),
          ("loc", 3),
          ("rdi", 4),
          ("unp", 5),
          ("unpr", 6))
    )


class TnRmdCfmMepNumber(TextualConvention, Unsigned32):
    status = "current"


class TnRmdCfmMeasurementInterval(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 3600000),
    )



class IEEE8021PriorityValue(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



# MIB Managed Objects in the order of their OIDs

_TnRmdCfmObjects_ObjectIdentity = ObjectIdentity
tnRmdCfmObjects = _TnRmdCfmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1)
)
_TnRmdCfmAttributeTotal_Type = Integer32
_TnRmdCfmAttributeTotal_Object = MibScalar
tnRmdCfmAttributeTotal = _TnRmdCfmAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 1),
    _TnRmdCfmAttributeTotal_Type()
)
tnRmdCfmAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdCfmAttributeTotal.setStatus("current")
_TnRmdSystemCfmTable_Object = MibTable
tnRmdSystemCfmTable = _TnRmdSystemCfmTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tnRmdSystemCfmTable.setStatus("current")
_TnRmdSystemCfmEntry_Object = MibTableRow
tnRmdSystemCfmEntry = _TnRmdSystemCfmEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 2, 1)
)
tnRmdSystemCfmEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-RMD-SYSTEM-MIB", "tnRmdSystemId"),
)
if mibBuilder.loadTexts:
    tnRmdSystemCfmEntry.setStatus("current")
_TnRmdSystemCfmMaxNrMeps_Type = Unsigned32
_TnRmdSystemCfmMaxNrMeps_Object = MibTableColumn
tnRmdSystemCfmMaxNrMeps = _TnRmdSystemCfmMaxNrMeps_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 2, 1, 1),
    _TnRmdSystemCfmMaxNrMeps_Type()
)
tnRmdSystemCfmMaxNrMeps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdSystemCfmMaxNrMeps.setStatus("current")
_TnRmdSystemCfmLmMaxNrPriorityLevels_Type = Unsigned32
_TnRmdSystemCfmLmMaxNrPriorityLevels_Object = MibTableColumn
tnRmdSystemCfmLmMaxNrPriorityLevels = _TnRmdSystemCfmLmMaxNrPriorityLevels_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 2, 1, 2),
    _TnRmdSystemCfmLmMaxNrPriorityLevels_Type()
)
tnRmdSystemCfmLmMaxNrPriorityLevels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdSystemCfmLmMaxNrPriorityLevels.setStatus("current")
_TnRmdSystemCfmDmUpdateLocalTime_Type = TruthValue
_TnRmdSystemCfmDmUpdateLocalTime_Object = MibTableColumn
tnRmdSystemCfmDmUpdateLocalTime = _TnRmdSystemCfmDmUpdateLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 2, 1, 3),
    _TnRmdSystemCfmDmUpdateLocalTime_Type()
)
tnRmdSystemCfmDmUpdateLocalTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnRmdSystemCfmDmUpdateLocalTime.setStatus("current")
_TnRmdCfmMepTable_Object = MibTable
tnRmdCfmMepTable = _TnRmdCfmMepTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tnRmdCfmMepTable.setStatus("current")
_TnRmdCfmMepEntry_Object = MibTableRow
tnRmdCfmMepEntry = _TnRmdCfmMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1)
)
tnRmdCfmMepEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-RMD-SYSTEM-MIB", "tnRmdSystemId"),
    (0, "TN-RMD-CFM-MIB", "tnRmdCfmMepNumber"),
)
if mibBuilder.loadTexts:
    tnRmdCfmMepEntry.setStatus("current")
_TnRmdCfmMepNumber_Type = TnRmdCfmMepNumber
_TnRmdCfmMepNumber_Object = MibTableColumn
tnRmdCfmMepNumber = _TnRmdCfmMepNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 1),
    _TnRmdCfmMepNumber_Type()
)
tnRmdCfmMepNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRmdCfmMepNumber.setStatus("current")
_TnRmdCfmMepMdIndex_Type = Unsigned32
_TnRmdCfmMepMdIndex_Object = MibTableColumn
tnRmdCfmMepMdIndex = _TnRmdCfmMepMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 2),
    _TnRmdCfmMepMdIndex_Type()
)
tnRmdCfmMepMdIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepMdIndex.setStatus("current")


class _TnRmdCfmMepMdFormat_Type(Dot1agCfmMaintDomainNameType):
    """Custom type tnRmdCfmMepMdFormat based on Dot1agCfmMaintDomainNameType"""
    defaultValue = 4


_TnRmdCfmMepMdFormat_Type.__name__ = "Dot1agCfmMaintDomainNameType"
_TnRmdCfmMepMdFormat_Object = MibTableColumn
tnRmdCfmMepMdFormat = _TnRmdCfmMepMdFormat_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 3),
    _TnRmdCfmMepMdFormat_Type()
)
tnRmdCfmMepMdFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepMdFormat.setStatus("current")


class _TnRmdCfmMepMdName_Type(Dot1agCfmMaintDomainName):
    """Custom type tnRmdCfmMepMdName based on Dot1agCfmMaintDomainName"""
    defaultValue = OctetString("DEFAULT")


_TnRmdCfmMepMdName_Type.__name__ = "Dot1agCfmMaintDomainName"
_TnRmdCfmMepMdName_Object = MibTableColumn
tnRmdCfmMepMdName = _TnRmdCfmMepMdName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 4),
    _TnRmdCfmMepMdName_Type()
)
tnRmdCfmMepMdName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepMdName.setStatus("current")
_TnRmdCfmMepMaIndex_Type = Unsigned32
_TnRmdCfmMepMaIndex_Object = MibTableColumn
tnRmdCfmMepMaIndex = _TnRmdCfmMepMaIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 5),
    _TnRmdCfmMepMaIndex_Type()
)
tnRmdCfmMepMaIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepMaIndex.setStatus("current")
_TnRmdCfmMepMaNetFormat_Type = Dot1agCfmMaintAssocNameType
_TnRmdCfmMepMaNetFormat_Object = MibTableColumn
tnRmdCfmMepMaNetFormat = _TnRmdCfmMepMaNetFormat_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 6),
    _TnRmdCfmMepMaNetFormat_Type()
)
tnRmdCfmMepMaNetFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepMaNetFormat.setStatus("current")
_TnRmdCfmMepMaNetName_Type = Dot1agCfmMaintAssocName
_TnRmdCfmMepMaNetName_Object = MibTableColumn
tnRmdCfmMepMaNetName = _TnRmdCfmMepMaNetName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 7),
    _TnRmdCfmMepMaNetName_Type()
)
tnRmdCfmMepMaNetName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepMaNetName.setStatus("current")
_TnRmdCfmMepMdLevel_Type = Dot1agCfmMDLevel
_TnRmdCfmMepMdLevel_Object = MibTableColumn
tnRmdCfmMepMdLevel = _TnRmdCfmMepMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 8),
    _TnRmdCfmMepMdLevel_Type()
)
tnRmdCfmMepMdLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepMdLevel.setStatus("current")
_TnRmdCfmMepMegId_Type = TnRmdCfmMegId
_TnRmdCfmMepMegId_Object = MibTableColumn
tnRmdCfmMepMegId = _TnRmdCfmMepMegId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 9),
    _TnRmdCfmMepMegId_Type()
)
tnRmdCfmMepMegId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepMegId.setStatus("current")
_TnRmdCfmMepDirection_Type = Dot1agCfmMpDirection
_TnRmdCfmMepDirection_Object = MibTableColumn
tnRmdCfmMepDirection = _TnRmdCfmMepDirection_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 10),
    _TnRmdCfmMepDirection_Type()
)
tnRmdCfmMepDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdCfmMepDirection.setStatus("current")
_TnRmdCfmMepLocalId_Type = Dot1agCfmMepId
_TnRmdCfmMepLocalId_Object = MibTableColumn
tnRmdCfmMepLocalId = _TnRmdCfmMepLocalId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 11),
    _TnRmdCfmMepLocalId_Type()
)
tnRmdCfmMepLocalId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepLocalId.setStatus("current")
_TnRmdCfmMepEnabled_Type = TruthValue
_TnRmdCfmMepEnabled_Object = MibTableColumn
tnRmdCfmMepEnabled = _TnRmdCfmMepEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 12),
    _TnRmdCfmMepEnabled_Type()
)
tnRmdCfmMepEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepEnabled.setStatus("current")
_TnRmdCfmMepCcmEnabled_Type = TruthValue
_TnRmdCfmMepCcmEnabled_Object = MibTableColumn
tnRmdCfmMepCcmEnabled = _TnRmdCfmMepCcmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 13),
    _TnRmdCfmMepCcmEnabled_Type()
)
tnRmdCfmMepCcmEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepCcmEnabled.setStatus("current")
_TnRmdCfmMepLbrEnabled_Type = TruthValue
_TnRmdCfmMepLbrEnabled_Object = MibTableColumn
tnRmdCfmMepLbrEnabled = _TnRmdCfmMepLbrEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 14),
    _TnRmdCfmMepLbrEnabled_Type()
)
tnRmdCfmMepLbrEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepLbrEnabled.setStatus("current")
_TnRmdCfmMepCcmInterval_Type = Dot1agCfmCcmInterval
_TnRmdCfmMepCcmInterval_Object = MibTableColumn
tnRmdCfmMepCcmInterval = _TnRmdCfmMepCcmInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 15),
    _TnRmdCfmMepCcmInterval_Type()
)
tnRmdCfmMepCcmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepCcmInterval.setStatus("current")
_TnRmdCfmMepIfIndex_Type = InterfaceIndexOrZero
_TnRmdCfmMepIfIndex_Object = MibTableColumn
tnRmdCfmMepIfIndex = _TnRmdCfmMepIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 16),
    _TnRmdCfmMepIfIndex_Type()
)
tnRmdCfmMepIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepIfIndex.setStatus("current")
_TnRmdCfmMepVlanId_Type = VlanIdOrNone
_TnRmdCfmMepVlanId_Object = MibTableColumn
tnRmdCfmMepVlanId = _TnRmdCfmMepVlanId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 17),
    _TnRmdCfmMepVlanId_Type()
)
tnRmdCfmMepVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepVlanId.setStatus("current")
_TnRmdCfmMepDefect_Type = TnRmdCfmMepDefect
_TnRmdCfmMepDefect_Object = MibTableColumn
tnRmdCfmMepDefect = _TnRmdCfmMepDefect_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 18),
    _TnRmdCfmMepDefect_Type()
)
tnRmdCfmMepDefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdCfmMepDefect.setStatus("current")
_TnRmdCfmMepRowStatus_Type = RowStatus
_TnRmdCfmMepRowStatus_Object = MibTableColumn
tnRmdCfmMepRowStatus = _TnRmdCfmMepRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 19),
    _TnRmdCfmMepRowStatus_Type()
)
tnRmdCfmMepRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepRowStatus.setStatus("current")


class _TnRmdCfmMepEvcLoopbackEnabled_Type(TruthValue):
    """Custom type tnRmdCfmMepEvcLoopbackEnabled based on TruthValue"""
    defaultValue = 2


_TnRmdCfmMepEvcLoopbackEnabled_Type.__name__ = "TruthValue"
_TnRmdCfmMepEvcLoopbackEnabled_Object = MibTableColumn
tnRmdCfmMepEvcLoopbackEnabled = _TnRmdCfmMepEvcLoopbackEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 20),
    _TnRmdCfmMepEvcLoopbackEnabled_Type()
)
tnRmdCfmMepEvcLoopbackEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepEvcLoopbackEnabled.setStatus("current")
_TnRmdCfmRemoteMepTable_Object = MibTable
tnRmdCfmRemoteMepTable = _TnRmdCfmRemoteMepTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 4)
)
if mibBuilder.loadTexts:
    tnRmdCfmRemoteMepTable.setStatus("current")
_TnRmdCfmRemoteMepEntry_Object = MibTableRow
tnRmdCfmRemoteMepEntry = _TnRmdCfmRemoteMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 4, 1)
)
tnRmdCfmRemoteMepEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-RMD-SYSTEM-MIB", "tnRmdSystemId"),
    (0, "TN-RMD-CFM-MIB", "tnRmdCfmMepNumber"),
    (0, "TN-RMD-CFM-MIB", "tnRmdCfmRemoteMepId"),
)
if mibBuilder.loadTexts:
    tnRmdCfmRemoteMepEntry.setStatus("current")
_TnRmdCfmRemoteMepId_Type = Dot1agCfmMepId
_TnRmdCfmRemoteMepId_Object = MibTableColumn
tnRmdCfmRemoteMepId = _TnRmdCfmRemoteMepId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 4, 1, 1),
    _TnRmdCfmRemoteMepId_Type()
)
tnRmdCfmRemoteMepId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRmdCfmRemoteMepId.setStatus("current")
_TnRmdCfmRemoteMepRowStatus_Type = RowStatus
_TnRmdCfmRemoteMepRowStatus_Object = MibTableColumn
tnRmdCfmRemoteMepRowStatus = _TnRmdCfmRemoteMepRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 4, 1, 2),
    _TnRmdCfmRemoteMepRowStatus_Type()
)
tnRmdCfmRemoteMepRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmRemoteMepRowStatus.setStatus("current")
_TnRmdCfmMepDmTable_Object = MibTable
tnRmdCfmMepDmTable = _TnRmdCfmMepDmTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 5)
)
if mibBuilder.loadTexts:
    tnRmdCfmMepDmTable.setStatus("current")
_TnRmdCfmMepDmEntry_Object = MibTableRow
tnRmdCfmMepDmEntry = _TnRmdCfmMepDmEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 5, 1)
)
tnRmdCfmMepDmEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-RMD-SYSTEM-MIB", "tnRmdSystemId"),
    (0, "TN-RMD-CFM-MIB", "tnRmdCfmMepNumber"),
)
if mibBuilder.loadTexts:
    tnRmdCfmMepDmEntry.setStatus("current")
_TnRmdCfmMepDmResponder_Type = TruthValue
_TnRmdCfmMepDmResponder_Object = MibTableColumn
tnRmdCfmMepDmResponder = _TnRmdCfmMepDmResponder_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 5, 1, 1),
    _TnRmdCfmMepDmResponder_Type()
)
tnRmdCfmMepDmResponder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnRmdCfmMepDmResponder.setStatus("current")
_TnRmdCfmMepDmInitiatorSessionTable_Object = MibTable
tnRmdCfmMepDmInitiatorSessionTable = _TnRmdCfmMepDmInitiatorSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 6)
)
if mibBuilder.loadTexts:
    tnRmdCfmMepDmInitiatorSessionTable.setStatus("current")
_TnRmdCfmMepDmInitiatorSessionEntry_Object = MibTableRow
tnRmdCfmMepDmInitiatorSessionEntry = _TnRmdCfmMepDmInitiatorSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 6, 1)
)
tnRmdCfmMepDmInitiatorSessionEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-RMD-SYSTEM-MIB", "tnRmdSystemId"),
    (0, "TN-RMD-CFM-MIB", "tnRmdCfmMepNumber"),
    (0, "TN-RMD-CFM-MIB", "tnRmdCfmMepDmInitiatorSessionNumber"),
)
if mibBuilder.loadTexts:
    tnRmdCfmMepDmInitiatorSessionEntry.setStatus("current")
_TnRmdCfmMepDmInitiatorSessionNumber_Type = Unsigned32
_TnRmdCfmMepDmInitiatorSessionNumber_Object = MibTableColumn
tnRmdCfmMepDmInitiatorSessionNumber = _TnRmdCfmMepDmInitiatorSessionNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 6, 1, 1),
    _TnRmdCfmMepDmInitiatorSessionNumber_Type()
)
tnRmdCfmMepDmInitiatorSessionNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRmdCfmMepDmInitiatorSessionNumber.setStatus("current")
_TnRmdCfmMepDmInitiatorSessionType_Type = TnRmdCfmInitiatorSessionType
_TnRmdCfmMepDmInitiatorSessionType_Object = MibTableColumn
tnRmdCfmMepDmInitiatorSessionType = _TnRmdCfmMepDmInitiatorSessionType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 6, 1, 2),
    _TnRmdCfmMepDmInitiatorSessionType_Type()
)
tnRmdCfmMepDmInitiatorSessionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepDmInitiatorSessionType.setStatus("current")
_TnRmdCfmMepDmInitiatorSessionMode_Type = TnRmdCfmDmInitiatorSessionMode
_TnRmdCfmMepDmInitiatorSessionMode_Object = MibTableColumn
tnRmdCfmMepDmInitiatorSessionMode = _TnRmdCfmMepDmInitiatorSessionMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 6, 1, 3),
    _TnRmdCfmMepDmInitiatorSessionMode_Type()
)
tnRmdCfmMepDmInitiatorSessionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepDmInitiatorSessionMode.setStatus("current")
_TnRmdCfmMepDmInitiatorSessionInterval_Type = TnRmdCfmMeasurementInterval
_TnRmdCfmMepDmInitiatorSessionInterval_Object = MibTableColumn
tnRmdCfmMepDmInitiatorSessionInterval = _TnRmdCfmMepDmInitiatorSessionInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 6, 1, 4),
    _TnRmdCfmMepDmInitiatorSessionInterval_Type()
)
tnRmdCfmMepDmInitiatorSessionInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepDmInitiatorSessionInterval.setStatus("current")
_TnRmdCfmMepDmInitiatorSessionTestInterval_Type = TnRmdCfmDmTestMeasurementInterval
_TnRmdCfmMepDmInitiatorSessionTestInterval_Object = MibTableColumn
tnRmdCfmMepDmInitiatorSessionTestInterval = _TnRmdCfmMepDmInitiatorSessionTestInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 6, 1, 5),
    _TnRmdCfmMepDmInitiatorSessionTestInterval_Type()
)
tnRmdCfmMepDmInitiatorSessionTestInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepDmInitiatorSessionTestInterval.setStatus("current")
_TnRmdCfmMepDmInitiatorSessionPriority_Type = IEEE8021PriorityValue
_TnRmdCfmMepDmInitiatorSessionPriority_Object = MibTableColumn
tnRmdCfmMepDmInitiatorSessionPriority = _TnRmdCfmMepDmInitiatorSessionPriority_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 6, 1, 6),
    _TnRmdCfmMepDmInitiatorSessionPriority_Type()
)
tnRmdCfmMepDmInitiatorSessionPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepDmInitiatorSessionPriority.setStatus("current")
_TnRmdCfmMepDmInitiatorSessionDropEligible_Type = TruthValue
_TnRmdCfmMepDmInitiatorSessionDropEligible_Object = MibTableColumn
tnRmdCfmMepDmInitiatorSessionDropEligible = _TnRmdCfmMepDmInitiatorSessionDropEligible_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 6, 1, 7),
    _TnRmdCfmMepDmInitiatorSessionDropEligible_Type()
)
tnRmdCfmMepDmInitiatorSessionDropEligible.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepDmInitiatorSessionDropEligible.setStatus("current")
_TnRmdCfmMepDmInitiatorSessionDestMac_Type = MacAddress
_TnRmdCfmMepDmInitiatorSessionDestMac_Object = MibTableColumn
tnRmdCfmMepDmInitiatorSessionDestMac = _TnRmdCfmMepDmInitiatorSessionDestMac_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 6, 1, 8),
    _TnRmdCfmMepDmInitiatorSessionDestMac_Type()
)
tnRmdCfmMepDmInitiatorSessionDestMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepDmInitiatorSessionDestMac.setStatus("current")
_TnRmdCfmMepDmInitiatorSessionInsertTestIdTlv_Type = TruthValue
_TnRmdCfmMepDmInitiatorSessionInsertTestIdTlv_Object = MibTableColumn
tnRmdCfmMepDmInitiatorSessionInsertTestIdTlv = _TnRmdCfmMepDmInitiatorSessionInsertTestIdTlv_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 6, 1, 9),
    _TnRmdCfmMepDmInitiatorSessionInsertTestIdTlv_Type()
)
tnRmdCfmMepDmInitiatorSessionInsertTestIdTlv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepDmInitiatorSessionInsertTestIdTlv.setStatus("current")
_TnRmdCfmMepDmInitiatorSessionTestId_Type = Unsigned32
_TnRmdCfmMepDmInitiatorSessionTestId_Object = MibTableColumn
tnRmdCfmMepDmInitiatorSessionTestId = _TnRmdCfmMepDmInitiatorSessionTestId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 6, 1, 10),
    _TnRmdCfmMepDmInitiatorSessionTestId_Type()
)
tnRmdCfmMepDmInitiatorSessionTestId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepDmInitiatorSessionTestId.setStatus("current")
_TnRmdCfmMepDmInitiatorSessionFrameLength_Type = Unsigned32
_TnRmdCfmMepDmInitiatorSessionFrameLength_Object = MibTableColumn
tnRmdCfmMepDmInitiatorSessionFrameLength = _TnRmdCfmMepDmInitiatorSessionFrameLength_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 6, 1, 11),
    _TnRmdCfmMepDmInitiatorSessionFrameLength_Type()
)
tnRmdCfmMepDmInitiatorSessionFrameLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepDmInitiatorSessionFrameLength.setStatus("current")
_TnRmdCfmMepDmInitiatorSessionState_Type = TnRmdCfmInitiatorSessionState
_TnRmdCfmMepDmInitiatorSessionState_Object = MibTableColumn
tnRmdCfmMepDmInitiatorSessionState = _TnRmdCfmMepDmInitiatorSessionState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 6, 1, 12),
    _TnRmdCfmMepDmInitiatorSessionState_Type()
)
tnRmdCfmMepDmInitiatorSessionState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepDmInitiatorSessionState.setStatus("current")
_TnRmdCfmMepDmInitiatorSessionRowStatus_Type = RowStatus
_TnRmdCfmMepDmInitiatorSessionRowStatus_Object = MibTableColumn
tnRmdCfmMepDmInitiatorSessionRowStatus = _TnRmdCfmMepDmInitiatorSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 6, 1, 13),
    _TnRmdCfmMepDmInitiatorSessionRowStatus_Type()
)
tnRmdCfmMepDmInitiatorSessionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepDmInitiatorSessionRowStatus.setStatus("current")
_TnRmdCfmMepSlmTable_Object = MibTable
tnRmdCfmMepSlmTable = _TnRmdCfmMepSlmTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 11)
)
if mibBuilder.loadTexts:
    tnRmdCfmMepSlmTable.setStatus("current")
_TnRmdCfmMepSlmEntry_Object = MibTableRow
tnRmdCfmMepSlmEntry = _TnRmdCfmMepSlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 11, 1)
)
tnRmdCfmMepSlmEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-RMD-SYSTEM-MIB", "tnRmdSystemId"),
    (0, "TN-RMD-CFM-MIB", "tnRmdCfmMepNumber"),
)
if mibBuilder.loadTexts:
    tnRmdCfmMepSlmEntry.setStatus("current")
_TnRmdCfmMepSlmResponder_Type = TruthValue
_TnRmdCfmMepSlmResponder_Object = MibTableColumn
tnRmdCfmMepSlmResponder = _TnRmdCfmMepSlmResponder_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 11, 1, 1),
    _TnRmdCfmMepSlmResponder_Type()
)
tnRmdCfmMepSlmResponder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnRmdCfmMepSlmResponder.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-RMD-CFM-MIB",
    **{"TnRmdCfmDmInitiatorSessionMode": TnRmdCfmDmInitiatorSessionMode,
       "TnRmdCfmDmTestMeasurementInterval": TnRmdCfmDmTestMeasurementInterval,
       "TnRmdCfmInitiatorSessionState": TnRmdCfmInitiatorSessionState,
       "TnRmdCfmInitiatorSessionType": TnRmdCfmInitiatorSessionType,
       "TnRmdCfmMegId": TnRmdCfmMegId,
       "TnRmdCfmMepDefect": TnRmdCfmMepDefect,
       "TnRmdCfmMepNumber": TnRmdCfmMepNumber,
       "TnRmdCfmMeasurementInterval": TnRmdCfmMeasurementInterval,
       "IEEE8021PriorityValue": IEEE8021PriorityValue,
       "tnRmdCfmMibModule": tnRmdCfmMibModule,
       "tnRmdCfmObjects": tnRmdCfmObjects,
       "tnRmdCfmAttributeTotal": tnRmdCfmAttributeTotal,
       "tnRmdSystemCfmTable": tnRmdSystemCfmTable,
       "tnRmdSystemCfmEntry": tnRmdSystemCfmEntry,
       "tnRmdSystemCfmMaxNrMeps": tnRmdSystemCfmMaxNrMeps,
       "tnRmdSystemCfmLmMaxNrPriorityLevels": tnRmdSystemCfmLmMaxNrPriorityLevels,
       "tnRmdSystemCfmDmUpdateLocalTime": tnRmdSystemCfmDmUpdateLocalTime,
       "tnRmdCfmMepTable": tnRmdCfmMepTable,
       "tnRmdCfmMepEntry": tnRmdCfmMepEntry,
       "tnRmdCfmMepNumber": tnRmdCfmMepNumber,
       "tnRmdCfmMepMdIndex": tnRmdCfmMepMdIndex,
       "tnRmdCfmMepMdFormat": tnRmdCfmMepMdFormat,
       "tnRmdCfmMepMdName": tnRmdCfmMepMdName,
       "tnRmdCfmMepMaIndex": tnRmdCfmMepMaIndex,
       "tnRmdCfmMepMaNetFormat": tnRmdCfmMepMaNetFormat,
       "tnRmdCfmMepMaNetName": tnRmdCfmMepMaNetName,
       "tnRmdCfmMepMdLevel": tnRmdCfmMepMdLevel,
       "tnRmdCfmMepMegId": tnRmdCfmMepMegId,
       "tnRmdCfmMepDirection": tnRmdCfmMepDirection,
       "tnRmdCfmMepLocalId": tnRmdCfmMepLocalId,
       "tnRmdCfmMepEnabled": tnRmdCfmMepEnabled,
       "tnRmdCfmMepCcmEnabled": tnRmdCfmMepCcmEnabled,
       "tnRmdCfmMepLbrEnabled": tnRmdCfmMepLbrEnabled,
       "tnRmdCfmMepCcmInterval": tnRmdCfmMepCcmInterval,
       "tnRmdCfmMepIfIndex": tnRmdCfmMepIfIndex,
       "tnRmdCfmMepVlanId": tnRmdCfmMepVlanId,
       "tnRmdCfmMepDefect": tnRmdCfmMepDefect,
       "tnRmdCfmMepRowStatus": tnRmdCfmMepRowStatus,
       "tnRmdCfmMepEvcLoopbackEnabled": tnRmdCfmMepEvcLoopbackEnabled,
       "tnRmdCfmRemoteMepTable": tnRmdCfmRemoteMepTable,
       "tnRmdCfmRemoteMepEntry": tnRmdCfmRemoteMepEntry,
       "tnRmdCfmRemoteMepId": tnRmdCfmRemoteMepId,
       "tnRmdCfmRemoteMepRowStatus": tnRmdCfmRemoteMepRowStatus,
       "tnRmdCfmMepDmTable": tnRmdCfmMepDmTable,
       "tnRmdCfmMepDmEntry": tnRmdCfmMepDmEntry,
       "tnRmdCfmMepDmResponder": tnRmdCfmMepDmResponder,
       "tnRmdCfmMepDmInitiatorSessionTable": tnRmdCfmMepDmInitiatorSessionTable,
       "tnRmdCfmMepDmInitiatorSessionEntry": tnRmdCfmMepDmInitiatorSessionEntry,
       "tnRmdCfmMepDmInitiatorSessionNumber": tnRmdCfmMepDmInitiatorSessionNumber,
       "tnRmdCfmMepDmInitiatorSessionType": tnRmdCfmMepDmInitiatorSessionType,
       "tnRmdCfmMepDmInitiatorSessionMode": tnRmdCfmMepDmInitiatorSessionMode,
       "tnRmdCfmMepDmInitiatorSessionInterval": tnRmdCfmMepDmInitiatorSessionInterval,
       "tnRmdCfmMepDmInitiatorSessionTestInterval": tnRmdCfmMepDmInitiatorSessionTestInterval,
       "tnRmdCfmMepDmInitiatorSessionPriority": tnRmdCfmMepDmInitiatorSessionPriority,
       "tnRmdCfmMepDmInitiatorSessionDropEligible": tnRmdCfmMepDmInitiatorSessionDropEligible,
       "tnRmdCfmMepDmInitiatorSessionDestMac": tnRmdCfmMepDmInitiatorSessionDestMac,
       "tnRmdCfmMepDmInitiatorSessionInsertTestIdTlv": tnRmdCfmMepDmInitiatorSessionInsertTestIdTlv,
       "tnRmdCfmMepDmInitiatorSessionTestId": tnRmdCfmMepDmInitiatorSessionTestId,
       "tnRmdCfmMepDmInitiatorSessionFrameLength": tnRmdCfmMepDmInitiatorSessionFrameLength,
       "tnRmdCfmMepDmInitiatorSessionState": tnRmdCfmMepDmInitiatorSessionState,
       "tnRmdCfmMepDmInitiatorSessionRowStatus": tnRmdCfmMepDmInitiatorSessionRowStatus,
       "tnRmdCfmMepSlmTable": tnRmdCfmMepSlmTable,
       "tnRmdCfmMepSlmEntry": tnRmdCfmMepSlmEntry,
       "tnRmdCfmMepSlmResponder": tnRmdCfmMepSlmResponder}
)
