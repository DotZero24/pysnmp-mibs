# SNMP MIB module (OS-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OS-PORT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:05:17 2025
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

(VlanIdOrNone,) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "VlanIdOrNone")

(PortIndex,
 PortIndexOrNone,
 PortList,
 oaOptiSwitch) = mibBuilder.importSymbols(
    "OS-COMMON-TC-MIB",
    "PortIndex",
    "PortIndexOrNone",
    "PortList",
    "oaOptiSwitch")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

osPort = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1)
)
if mibBuilder.loadTexts:
    osPort.setRevisions(
        ("2020-08-27 00:00",
         "2019-12-26 00:00",
         "2019-07-23 00:00",
         "2018-12-09 00:00",
         "2015-04-30 00:00",
         "2014-06-09 00:00",
         "2014-02-11 00:00",
         "2013-09-17 00:00",
         "2012-09-23 00:00",
         "2012-06-24 00:00",
         "2012-05-29 00:00",
         "2010-11-02 00:00",
         "2010-10-20 00:00",
         "2010-08-05 00:00",
         "2010-04-18 00:00",
         "2008-01-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SupportValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supported", 2))
    )



class BuffersProfileIndex(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )



class L2CtrlProcess(TextualConvention, Integer32):
    status = "current"
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
          ("drop", 2),
          ("peer", 3),
          ("tunnel", 4))
    )



class PortEntryValidator(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )



class LastError(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 160),
    )



# MIB Managed Objects in the order of their OIDs

_OsPortNotifications_ObjectIdentity = ObjectIdentity
osPortNotifications = _OsPortNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 0)
)
_OsPortCfg_ObjectIdentity = ObjectIdentity
osPortCfg = _OsPortCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 1)
)
_OsPortCfgSupport_Type = SupportValue
_OsPortCfgSupport_Object = MibScalar
osPortCfgSupport = _OsPortCfgSupport_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 1, 1),
    _OsPortCfgSupport_Type()
)
osPortCfgSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortCfgSupport.setStatus("current")
_OsPortCfgMaxNumberOfPort_Type = PortIndex
_OsPortCfgMaxNumberOfPort_Object = MibScalar
osPortCfgMaxNumberOfPort = _OsPortCfgMaxNumberOfPort_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 1, 2),
    _OsPortCfgMaxNumberOfPort_Type()
)
osPortCfgMaxNumberOfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortCfgMaxNumberOfPort.setStatus("current")
_OsPortCfgBaseTrunkPortIndex_Type = PortIndex
_OsPortCfgBaseTrunkPortIndex_Object = MibScalar
osPortCfgBaseTrunkPortIndex = _OsPortCfgBaseTrunkPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 1, 3),
    _OsPortCfgBaseTrunkPortIndex_Type()
)
osPortCfgBaseTrunkPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortCfgBaseTrunkPortIndex.setStatus("current")


class _OsPortCfgMaxNumberOfSl_Type(Unsigned32):
    """Custom type osPortCfgMaxNumberOfSl based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8190),
    )


_OsPortCfgMaxNumberOfSl_Type.__name__ = "Unsigned32"
_OsPortCfgMaxNumberOfSl_Object = MibScalar
osPortCfgMaxNumberOfSl = _OsPortCfgMaxNumberOfSl_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 1, 4),
    _OsPortCfgMaxNumberOfSl_Type()
)
osPortCfgMaxNumberOfSl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortCfgMaxNumberOfSl.setStatus("current")


class _OsPortCfgMaxTrunkId_Type(Integer32):
    """Custom type osPortCfgMaxTrunkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_OsPortCfgMaxTrunkId_Type.__name__ = "Integer32"
_OsPortCfgMaxTrunkId_Object = MibScalar
osPortCfgMaxTrunkId = _OsPortCfgMaxTrunkId_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 1, 5),
    _OsPortCfgMaxTrunkId_Type()
)
osPortCfgMaxTrunkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortCfgMaxTrunkId.setStatus("current")
_OsPortTrunkLastError_Type = LastError
_OsPortTrunkLastError_Object = MibScalar
osPortTrunkLastError = _OsPortTrunkLastError_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 1, 12),
    _OsPortTrunkLastError_Type()
)
osPortTrunkLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortTrunkLastError.setStatus("current")


class _OsPortCntEgressClearAll_Type(Integer32):
    """Custom type osPortCntEgressClearAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("clear", 2))
    )


_OsPortCntEgressClearAll_Type.__name__ = "Integer32"
_OsPortCntEgressClearAll_Object = MibScalar
osPortCntEgressClearAll = _OsPortCntEgressClearAll_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 1, 13),
    _OsPortCntEgressClearAll_Type()
)
osPortCntEgressClearAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPortCntEgressClearAll.setStatus("current")
_OsPortTable_Object = MibTable
osPortTable = _OsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 2)
)
if mibBuilder.loadTexts:
    osPortTable.setStatus("current")
_OsPortEntry_Object = MibTableRow
osPortEntry = _OsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 2, 1)
)
osPortEntry.setIndexNames(
    (0, "OS-PORT-MIB", "osPortIndex"),
)
if mibBuilder.loadTexts:
    osPortEntry.setStatus("current")
_OsPortIndex_Type = PortIndex
_OsPortIndex_Object = MibTableColumn
osPortIndex = _OsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 2, 1, 1),
    _OsPortIndex_Type()
)
osPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osPortIndex.setStatus("current")


class _OsPortDescription_Type(DisplayString):
    """Custom type osPortDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_OsPortDescription_Type.__name__ = "DisplayString"
_OsPortDescription_Object = MibTableColumn
osPortDescription = _OsPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 2, 1, 3),
    _OsPortDescription_Type()
)
osPortDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPortDescription.setStatus("current")
_OsPortLink_Type = TruthValue
_OsPortLink_Object = MibTableColumn
osPortLink = _OsPortLink_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 2, 1, 5),
    _OsPortLink_Type()
)
osPortLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortLink.setStatus("current")


class _OsPortAdminSpeed_Type(Integer32):
    """Custom type osPortAdminSpeed based on Integer32"""
    defaultValue = 2

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
        *(("other", 1),
          ("auto", 2),
          ("s10", 3),
          ("s100", 4),
          ("s1000", 5),
          ("s10000", 6),
          ("s2500", 7))
    )


_OsPortAdminSpeed_Type.__name__ = "Integer32"
_OsPortAdminSpeed_Object = MibTableColumn
osPortAdminSpeed = _OsPortAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 2, 1, 6),
    _OsPortAdminSpeed_Type()
)
osPortAdminSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPortAdminSpeed.setStatus("current")
_OsPortOperSpeed_Type = Gauge32
_OsPortOperSpeed_Object = MibTableColumn
osPortOperSpeed = _OsPortOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 2, 1, 7),
    _OsPortOperSpeed_Type()
)
osPortOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortOperSpeed.setStatus("current")


class _OsPortDuplex_Type(Integer32):
    """Custom type osPortDuplex based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("full", 3),
          ("half", 4))
    )


_OsPortDuplex_Type.__name__ = "Integer32"
_OsPortDuplex_Object = MibTableColumn
osPortDuplex = _OsPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 2, 1, 9),
    _OsPortDuplex_Type()
)
osPortDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPortDuplex.setStatus("current")


class _OsPortAdminState_Type(Integer32):
    """Custom type osPortAdminState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("enable", 2),
          ("disableByMgmt", 3))
    )


_OsPortAdminState_Type.__name__ = "Integer32"
_OsPortAdminState_Object = MibTableColumn
osPortAdminState = _OsPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 2, 1, 10),
    _OsPortAdminState_Type()
)
osPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPortAdminState.setStatus("current")


class _OsPortOperState_Type(Integer32):
    """Custom type osPortOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("enabled", 2),
          ("disabledByMgmt", 3),
          ("disabledByReboot", 4),
          ("isolatedByLinkFlapGuard", 5),
          ("isolatedByLinkReflection", 6),
          ("isolatedByLinkProtection", 7),
          ("isolatedByStpLinkReflection", 8),
          ("isolatedByHotSwap", 9),
          ("isolatedByHa", 10),
          ("isolatedByStpPortLoop", 11),
          ("isolatedByStpOverRate", 12),
          ("isolatedByEthoamOverRate", 13),
          ("isolatedByEfmOverRate", 14),
          ("isolatedByDot1xOverRate", 15),
          ("isolatedByDot1agOverRate", 16),
          ("isolatedByLacpOverRate", 17),
          ("isolatedByAhOverRate", 18),
          ("isolatedByUdld", 19),
          ("isolatedByShdslLinkDown", 20),
          ("isolatedByL2TpOverRate", 21),
          ("isolatedByTdmLinkProtection", 22),
          ("isolatedByMplsLinkProtection", 23),
          ("isolatedByMacFlapLoopGuard", 24))
    )


_OsPortOperState_Type.__name__ = "Integer32"
_OsPortOperState_Object = MibTableColumn
osPortOperState = _OsPortOperState_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 2, 1, 11),
    _OsPortOperState_Type()
)
osPortOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortOperState.setStatus("current")


class _OsPortBlockReason_Type(Bits):
    """Custom type osPortBlockReason based on Bits"""
    namedValues = NamedValues(
        *(("other", 0),
          ("reserve", 1),
          ("enabled", 2),
          ("blockedByStp", 3),
          ("blockedByDot1X", 4),
          ("blockedByLacp", 5),
          ("blockedByAh", 6),
          ("blockedByErp", 7))
    )

_OsPortBlockReason_Type.__name__ = "Bits"
_OsPortBlockReason_Object = MibTableColumn
osPortBlockReason = _OsPortBlockReason_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 2, 1, 12),
    _OsPortBlockReason_Type()
)
osPortBlockReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortBlockReason.setStatus("current")


class _OsPortBuffersProfileIndex_Type(BuffersProfileIndex):
    """Custom type osPortBuffersProfileIndex based on BuffersProfileIndex"""
    defaultValue = 1


_OsPortBuffersProfileIndex_Type.__name__ = "BuffersProfileIndex"
_OsPortBuffersProfileIndex_Object = MibTableColumn
osPortBuffersProfileIndex = _OsPortBuffersProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 2, 1, 50),
    _OsPortBuffersProfileIndex_Type()
)
osPortBuffersProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPortBuffersProfileIndex.setStatus("current")
_OsPortTrunkIndex_Type = PortIndexOrNone
_OsPortTrunkIndex_Object = MibTableColumn
osPortTrunkIndex = _OsPortTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 2, 1, 60),
    _OsPortTrunkIndex_Type()
)
osPortTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortTrunkIndex.setStatus("current")


class _OsPortLacpAdminMode_Type(Integer32):
    """Custom type osPortLacpAdminMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("active", 3),
          ("passive", 4),
          ("rapid", 5))
    )


_OsPortLacpAdminMode_Type.__name__ = "Integer32"
_OsPortLacpAdminMode_Object = MibTableColumn
osPortLacpAdminMode = _OsPortLacpAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 2, 1, 61),
    _OsPortLacpAdminMode_Type()
)
osPortLacpAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPortLacpAdminMode.setStatus("current")


class _OsPortLacpOperState_Type(Integer32):
    """Custom type osPortLacpOperState based on Integer32"""
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
        *(("other", 1),
          ("nonLacp", 2),
          ("blocked", 3),
          ("enabled", 4))
    )


_OsPortLacpOperState_Type.__name__ = "Integer32"
_OsPortLacpOperState_Object = MibTableColumn
osPortLacpOperState = _OsPortLacpOperState_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 2, 1, 62),
    _OsPortLacpOperState_Type()
)
osPortLacpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortLacpOperState.setStatus("current")


class _OsPortMtuSize_Type(Unsigned32):
    """Custom type osPortMtuSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 16000),
    )


_OsPortMtuSize_Type.__name__ = "Unsigned32"
_OsPortMtuSize_Object = MibTableColumn
osPortMtuSize = _OsPortMtuSize_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 2, 1, 66),
    _OsPortMtuSize_Type()
)
osPortMtuSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPortMtuSize.setStatus("current")


class _OsPortQosMarkingVpt_Type(Integer32):
    """Custom type osPortQosMarkingVpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("vpt", 2),
          ("dscp", 3),
          ("vptdscp", 4),
          ("none", 5))
    )


_OsPortQosMarkingVpt_Type.__name__ = "Integer32"
_OsPortQosMarkingVpt_Object = MibTableColumn
osPortQosMarkingVpt = _OsPortQosMarkingVpt_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 2, 1, 70),
    _OsPortQosMarkingVpt_Type()
)
osPortQosMarkingVpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPortQosMarkingVpt.setStatus("current")


class _OsPortQosTrust_Type(Integer32):
    """Custom type osPortQosTrust based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("l2", 2),
          ("l3", 3),
          ("l2l3", 4),
          ("port", 5))
    )


_OsPortQosTrust_Type.__name__ = "Integer32"
_OsPortQosTrust_Object = MibTableColumn
osPortQosTrust = _OsPortQosTrust_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 2, 1, 71),
    _OsPortQosTrust_Type()
)
osPortQosTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPortQosTrust.setStatus("current")


class _OsPortRemarkingDei_Type(Integer32):
    """Custom type osPortRemarkingDei based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("preserveDei", 1),
          ("remarkDei", 2))
    )


_OsPortRemarkingDei_Type.__name__ = "Integer32"
_OsPortRemarkingDei_Object = MibTableColumn
osPortRemarkingDei = _OsPortRemarkingDei_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 2, 1, 72),
    _OsPortRemarkingDei_Type()
)
osPortRemarkingDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPortRemarkingDei.setStatus("current")


class _OsPortSl_Type(Unsigned32):
    """Custom type osPortSl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8190),
    )


_OsPortSl_Type.__name__ = "Unsigned32"
_OsPortSl_Object = MibTableColumn
osPortSl = _OsPortSl_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 2, 1, 78),
    _OsPortSl_Type()
)
osPortSl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPortSl.setStatus("current")


class _OsPortTagType_Type(Integer32):
    """Custom type osPortTagType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("tagged", 2),
          ("untaggedSingleVlan", 3),
          ("untaggedMultiVlans", 4),
          ("hybrid", 5),
          ("qInQ", 6))
    )


_OsPortTagType_Type.__name__ = "Integer32"
_OsPortTagType_Object = MibTableColumn
osPortTagType = _OsPortTagType_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 2, 1, 80),
    _OsPortTagType_Type()
)
osPortTagType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPortTagType.setStatus("current")
_OsPortTagDefaultTag_Type = VlanIdOrNone
_OsPortTagDefaultTag_Object = MibTableColumn
osPortTagDefaultTag = _OsPortTagDefaultTag_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 2, 1, 81),
    _OsPortTagDefaultTag_Type()
)
osPortTagDefaultTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPortTagDefaultTag.setStatus("current")
_OsPortL2CtrlDot1x_Type = L2CtrlProcess
_OsPortL2CtrlDot1x_Object = MibTableColumn
osPortL2CtrlDot1x = _OsPortL2CtrlDot1x_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 2, 1, 83),
    _OsPortL2CtrlDot1x_Type()
)
osPortL2CtrlDot1x.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortL2CtrlDot1x.setStatus("current")
_OsPortL2CtrlLACP_Type = L2CtrlProcess
_OsPortL2CtrlLACP_Object = MibTableColumn
osPortL2CtrlLACP = _OsPortL2CtrlLACP_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 2, 1, 84),
    _OsPortL2CtrlLACP_Type()
)
osPortL2CtrlLACP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortL2CtrlLACP.setStatus("current")
_OsPortL2CtrlSTP_Type = L2CtrlProcess
_OsPortL2CtrlSTP_Object = MibTableColumn
osPortL2CtrlSTP = _OsPortL2CtrlSTP_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 2, 1, 85),
    _OsPortL2CtrlSTP_Type()
)
osPortL2CtrlSTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPortL2CtrlSTP.setStatus("current")
_OsPortL2CtrlGVRP_Type = L2CtrlProcess
_OsPortL2CtrlGVRP_Object = MibTableColumn
osPortL2CtrlGVRP = _OsPortL2CtrlGVRP_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 2, 1, 86),
    _OsPortL2CtrlGVRP_Type()
)
osPortL2CtrlGVRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortL2CtrlGVRP.setStatus("current")
_OsPortL2CtrlPause_Type = L2CtrlProcess
_OsPortL2CtrlPause_Object = MibTableColumn
osPortL2CtrlPause = _OsPortL2CtrlPause_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 2, 1, 87),
    _OsPortL2CtrlPause_Type()
)
osPortL2CtrlPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortL2CtrlPause.setStatus("current")
_OsPortL2CtrlLinkOAM_Type = L2CtrlProcess
_OsPortL2CtrlLinkOAM_Object = MibTableColumn
osPortL2CtrlLinkOAM = _OsPortL2CtrlLinkOAM_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 2, 1, 88),
    _OsPortL2CtrlLinkOAM_Type()
)
osPortL2CtrlLinkOAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortL2CtrlLinkOAM.setStatus("current")
_OsPortL2CtrlELMI_Type = L2CtrlProcess
_OsPortL2CtrlELMI_Object = MibTableColumn
osPortL2CtrlELMI = _OsPortL2CtrlELMI_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 2, 1, 89),
    _OsPortL2CtrlELMI_Type()
)
osPortL2CtrlELMI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortL2CtrlELMI.setStatus("current")
_OsPortL2CtrlLLDP_Type = L2CtrlProcess
_OsPortL2CtrlLLDP_Object = MibTableColumn
osPortL2CtrlLLDP = _OsPortL2CtrlLLDP_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 2, 1, 90),
    _OsPortL2CtrlLLDP_Type()
)
osPortL2CtrlLLDP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortL2CtrlLLDP.setStatus("current")
_OsPortL2CtrlDTP_Type = L2CtrlProcess
_OsPortL2CtrlDTP_Object = MibTableColumn
osPortL2CtrlDTP = _OsPortL2CtrlDTP_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 2, 1, 91),
    _OsPortL2CtrlDTP_Type()
)
osPortL2CtrlDTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPortL2CtrlDTP.setStatus("current")
_OsPortL2CtrlPAGP_Type = L2CtrlProcess
_OsPortL2CtrlPAGP_Object = MibTableColumn
osPortL2CtrlPAGP = _OsPortL2CtrlPAGP_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 2, 1, 92),
    _OsPortL2CtrlPAGP_Type()
)
osPortL2CtrlPAGP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPortL2CtrlPAGP.setStatus("current")
_OsPortL2CtrlVTP_Type = L2CtrlProcess
_OsPortL2CtrlVTP_Object = MibTableColumn
osPortL2CtrlVTP = _OsPortL2CtrlVTP_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 2, 1, 95),
    _OsPortL2CtrlVTP_Type()
)
osPortL2CtrlVTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPortL2CtrlVTP.setStatus("current")
_OsPortL2CtrlCDP_Type = L2CtrlProcess
_OsPortL2CtrlCDP_Object = MibTableColumn
osPortL2CtrlCDP = _OsPortL2CtrlCDP_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 2, 1, 96),
    _OsPortL2CtrlCDP_Type()
)
osPortL2CtrlCDP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPortL2CtrlCDP.setStatus("current")
_OsPortL2CtrlPVST_Type = L2CtrlProcess
_OsPortL2CtrlPVST_Object = MibTableColumn
osPortL2CtrlPVST = _OsPortL2CtrlPVST_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 2, 1, 97),
    _OsPortL2CtrlPVST_Type()
)
osPortL2CtrlPVST.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPortL2CtrlPVST.setStatus("current")


class _OsPortAdminMediaSelect_Type(Integer32):
    """Custom type osPortAdminMediaSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("sfp", 2),
          ("sfp100", 3),
          ("copper", 4),
          ("auto", 5),
          ("sgmii", 6),
          ("sfpPlus", 7),
          ("sfpAutoDetect", 8))
    )


_OsPortAdminMediaSelect_Type.__name__ = "Integer32"
_OsPortAdminMediaSelect_Object = MibTableColumn
osPortAdminMediaSelect = _OsPortAdminMediaSelect_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 2, 1, 98),
    _OsPortAdminMediaSelect_Type()
)
osPortAdminMediaSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPortAdminMediaSelect.setStatus("current")


class _OsPortOperMediaSelect_Type(Integer32):
    """Custom type osPortOperMediaSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("sfp", 2),
          ("sfp100", 3),
          ("copper", 4),
          ("sgmii", 6),
          ("sfpPlus", 7),
          ("sfpAutoDetect", 8))
    )


_OsPortOperMediaSelect_Type.__name__ = "Integer32"
_OsPortOperMediaSelect_Object = MibTableColumn
osPortOperMediaSelect = _OsPortOperMediaSelect_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 2, 1, 99),
    _OsPortOperMediaSelect_Type()
)
osPortOperMediaSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortOperMediaSelect.setStatus("current")


class _OsPortLanType_Type(Integer32):
    """Custom type osPortLanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("eth10", 2),
          ("eth100", 3),
          ("eth10or100", 4),
          ("eth100B", 5),
          ("eth1000B", 6),
          ("atmLane", 7),
          ("eth100Grp", 8),
          ("eth10or100Grp", 9),
          ("fddi", 10),
          ("eth100or1000", 11),
          ("eth10hpna", 12),
          ("eth100or1000amp", 13),
          ("eth10or100overVDSL", 14),
          ("eth1000", 15),
          ("eth10or100or1000", 16),
          ("eth10000", 17),
          ("ethLAG", 18),
          ("eth1000or10000", 19))
    )


_OsPortLanType_Type.__name__ = "Integer32"
_OsPortLanType_Object = MibTableColumn
osPortLanType = _OsPortLanType_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 2, 1, 100),
    _OsPortLanType_Type()
)
osPortLanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortLanType.setStatus("current")


class _OsPortIfType_Type(Integer32):
    """Custom type osPortIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37)
        )
    )
    namedValues = NamedValues(
        *(("aui", 1),
          ("tp", 2),
          ("auiTp", 3),
          ("tpfd", 4),
          ("coax", 5),
          ("foMm", 6),
          ("foSm", 7),
          ("none", 8),
          ("foSxM", 9),
          ("foLxM", 10),
          ("foLxS1", 11),
          ("foLxS2", 12),
          ("foLxS3", 13),
          ("foM", 14),
          ("foMX", 15),
          ("foS1", 16),
          ("foS2", 17),
          ("foS3", 18),
          ("foLxS4", 19),
          ("foLxS5", 20),
          ("foS4", 21),
          ("foS5", 22),
          ("foM10", 23),
          ("foGMX", 24),
          ("foS1A", 25),
          ("foPAL", 26),
          ("foXFP", 27),
          ("foSFPtp", 28),
          ("foSFP", 29),
          ("foSFPfoSFP100FXtp", 30),
          ("foSFP100FX", 31),
          ("foSFPfoSFP100FX", 32),
          ("foSFPdirect", 33),
          ("tpSHDSL", 34),
          ("portTrunk", 35),
          ("internalPort", 36),
          ("foSFPplus", 37))
    )


_OsPortIfType_Type.__name__ = "Integer32"
_OsPortIfType_Object = MibTableColumn
osPortIfType = _OsPortIfType_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 2, 1, 101),
    _OsPortIfType_Type()
)
osPortIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortIfType.setStatus("current")
_OsPortLastError_Type = LastError
_OsPortLastError_Object = MibTableColumn
osPortLastError = _OsPortLastError_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 2, 1, 102),
    _OsPortLastError_Type()
)
osPortLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortLastError.setStatus("current")
_OsPortShapeTable_Object = MibTable
osPortShapeTable = _OsPortShapeTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 3)
)
if mibBuilder.loadTexts:
    osPortShapeTable.setStatus("current")
_OsPortShapeEntry_Object = MibTableRow
osPortShapeEntry = _OsPortShapeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 3, 1)
)
osPortShapeEntry.setIndexNames(
    (0, "OS-PORT-MIB", "osPortIndex"),
    (0, "OS-PORT-MIB", "osPortShapeDir"),
    (0, "OS-PORT-MIB", "osPortShapeQId"),
)
if mibBuilder.loadTexts:
    osPortShapeEntry.setStatus("current")


class _OsPortShapeDir_Type(Integer32):
    """Custom type osPortShapeDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("egressShaping", 1),
          ("ingressShaping", 2))
    )


_OsPortShapeDir_Type.__name__ = "Integer32"
_OsPortShapeDir_Object = MibTableColumn
osPortShapeDir = _OsPortShapeDir_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 3, 1, 3),
    _OsPortShapeDir_Type()
)
osPortShapeDir.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osPortShapeDir.setStatus("current")


class _OsPortShapeQId_Type(Unsigned32):
    """Custom type osPortShapeQId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8190),
        ValueRangeConstraint(8191, 8191),
    )


_OsPortShapeQId_Type.__name__ = "Unsigned32"
_OsPortShapeQId_Object = MibTableColumn
osPortShapeQId = _OsPortShapeQId_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 3, 1, 4),
    _OsPortShapeQId_Type()
)
osPortShapeQId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osPortShapeQId.setStatus("current")
_OsPortShapeRate_Type = Gauge32
_OsPortShapeRate_Object = MibTableColumn
osPortShapeRate = _OsPortShapeRate_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 3, 1, 6),
    _OsPortShapeRate_Type()
)
osPortShapeRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPortShapeRate.setStatus("current")
if mibBuilder.loadTexts:
    osPortShapeRate.setUnits("kilobits per second")
_OsPortShapeBurstSize_Type = Gauge32
_OsPortShapeBurstSize_Object = MibTableColumn
osPortShapeBurstSize = _OsPortShapeBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 3, 1, 7),
    _OsPortShapeBurstSize_Type()
)
osPortShapeBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPortShapeBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    osPortShapeBurstSize.setUnits("KBytes")
_OsPortShapeLastError_Type = LastError
_OsPortShapeLastError_Object = MibTableColumn
osPortShapeLastError = _OsPortShapeLastError_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 3, 1, 8),
    _OsPortShapeLastError_Type()
)
osPortShapeLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortShapeLastError.setStatus("current")
_OsPortShapeLocked_Type = TruthValue
_OsPortShapeLocked_Object = MibTableColumn
osPortShapeLocked = _OsPortShapeLocked_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 3, 1, 15),
    _OsPortShapeLocked_Type()
)
osPortShapeLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortShapeLocked.setStatus("current")
_OsPortShapeAdminStatus_Type = PortEntryValidator
_OsPortShapeAdminStatus_Object = MibTableColumn
osPortShapeAdminStatus = _OsPortShapeAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 3, 1, 17),
    _OsPortShapeAdminStatus_Type()
)
osPortShapeAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPortShapeAdminStatus.setStatus("current")
_OsPortTrunkTable_Object = MibTable
osPortTrunkTable = _OsPortTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 4)
)
if mibBuilder.loadTexts:
    osPortTrunkTable.setStatus("current")
_OsPortTrunkEntry_Object = MibTableRow
osPortTrunkEntry = _OsPortTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 4, 1)
)
osPortTrunkEntry.setIndexNames(
    (0, "OS-PORT-MIB", "osPortTrunkId"),
)
if mibBuilder.loadTexts:
    osPortTrunkEntry.setStatus("current")


class _OsPortTrunkId_Type(Integer32):
    """Custom type osPortTrunkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_OsPortTrunkId_Type.__name__ = "Integer32"
_OsPortTrunkId_Object = MibTableColumn
osPortTrunkId = _OsPortTrunkId_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 4, 1, 3),
    _OsPortTrunkId_Type()
)
osPortTrunkId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osPortTrunkId.setStatus("current")
_OsPortTrunkIndexId_Type = Integer32
_OsPortTrunkIndexId_Object = MibTableColumn
osPortTrunkIndexId = _OsPortTrunkIndexId_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 4, 1, 4),
    _OsPortTrunkIndexId_Type()
)
osPortTrunkIndexId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortTrunkIndexId.setStatus("current")
_OsPortTrunkMembers_Type = PortList
_OsPortTrunkMembers_Object = MibTableColumn
osPortTrunkMembers = _OsPortTrunkMembers_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 4, 1, 5),
    _OsPortTrunkMembers_Type()
)
osPortTrunkMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPortTrunkMembers.setStatus("current")
_OsPortTrunkAdminStatus_Type = PortEntryValidator
_OsPortTrunkAdminStatus_Object = MibTableColumn
osPortTrunkAdminStatus = _OsPortTrunkAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 4, 1, 6),
    _OsPortTrunkAdminStatus_Type()
)
osPortTrunkAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPortTrunkAdminStatus.setStatus("current")
_OsPortTrunkNumOfMembers_Type = Integer32
_OsPortTrunkNumOfMembers_Object = MibTableColumn
osPortTrunkNumOfMembers = _OsPortTrunkNumOfMembers_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 4, 1, 7),
    _OsPortTrunkNumOfMembers_Type()
)
osPortTrunkNumOfMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortTrunkNumOfMembers.setStatus("current")
_OsPortCntTable_Object = MibTable
osPortCntTable = _OsPortCntTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 5)
)
if mibBuilder.loadTexts:
    osPortCntTable.setStatus("current")
_OsPortCntEntry_Object = MibTableRow
osPortCntEntry = _OsPortCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    osPortCntEntry.setStatus("current")


class _OsPortCntClearAll_Type(Integer32):
    """Custom type osPortCntClearAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("clear", 2))
    )


_OsPortCntClearAll_Type.__name__ = "Integer32"
_OsPortCntClearAll_Object = MibTableColumn
osPortCntClearAll = _OsPortCntClearAll_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 5, 1, 2),
    _OsPortCntClearAll_Type()
)
osPortCntClearAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPortCntClearAll.setStatus("current")
_OsPortCntRecvBytes_Type = Counter64
_OsPortCntRecvBytes_Object = MibTableColumn
osPortCntRecvBytes = _OsPortCntRecvBytes_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 5, 1, 3),
    _OsPortCntRecvBytes_Type()
)
osPortCntRecvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortCntRecvBytes.setStatus("current")
_OsPortCntRecvPacks_Type = Counter64
_OsPortCntRecvPacks_Object = MibTableColumn
osPortCntRecvPacks = _OsPortCntRecvPacks_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 5, 1, 4),
    _OsPortCntRecvPacks_Type()
)
osPortCntRecvPacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortCntRecvPacks.setStatus("current")
_OsPortCntRecvUniPacks_Type = Counter64
_OsPortCntRecvUniPacks_Object = MibTableColumn
osPortCntRecvUniPacks = _OsPortCntRecvUniPacks_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 5, 1, 5),
    _OsPortCntRecvUniPacks_Type()
)
osPortCntRecvUniPacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortCntRecvUniPacks.setStatus("current")
_OsPortCntRecvBroadPacks_Type = Counter64
_OsPortCntRecvBroadPacks_Object = MibTableColumn
osPortCntRecvBroadPacks = _OsPortCntRecvBroadPacks_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 5, 1, 6),
    _OsPortCntRecvBroadPacks_Type()
)
osPortCntRecvBroadPacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortCntRecvBroadPacks.setStatus("current")
_OsPortCntRecvMultiPacks_Type = Counter64
_OsPortCntRecvMultiPacks_Object = MibTableColumn
osPortCntRecvMultiPacks = _OsPortCntRecvMultiPacks_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 5, 1, 7),
    _OsPortCntRecvMultiPacks_Type()
)
osPortCntRecvMultiPacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortCntRecvMultiPacks.setStatus("current")
_OsPortCntSentBytes_Type = Counter64
_OsPortCntSentBytes_Object = MibTableColumn
osPortCntSentBytes = _OsPortCntSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 5, 1, 8),
    _OsPortCntSentBytes_Type()
)
osPortCntSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortCntSentBytes.setStatus("current")
_OsPortCntSentPacks_Type = Counter64
_OsPortCntSentPacks_Object = MibTableColumn
osPortCntSentPacks = _OsPortCntSentPacks_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 5, 1, 9),
    _OsPortCntSentPacks_Type()
)
osPortCntSentPacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortCntSentPacks.setStatus("current")
_OsPortCntSentUniPacks_Type = Counter64
_OsPortCntSentUniPacks_Object = MibTableColumn
osPortCntSentUniPacks = _OsPortCntSentUniPacks_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 5, 1, 10),
    _OsPortCntSentUniPacks_Type()
)
osPortCntSentUniPacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortCntSentUniPacks.setStatus("current")
_OsPortCntSentBroadPacks_Type = Counter64
_OsPortCntSentBroadPacks_Object = MibTableColumn
osPortCntSentBroadPacks = _OsPortCntSentBroadPacks_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 5, 1, 11),
    _OsPortCntSentBroadPacks_Type()
)
osPortCntSentBroadPacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortCntSentBroadPacks.setStatus("current")
_OsPortCntSentMultiPacks_Type = Counter64
_OsPortCntSentMultiPacks_Object = MibTableColumn
osPortCntSentMultiPacks = _OsPortCntSentMultiPacks_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 5, 1, 12),
    _OsPortCntSentMultiPacks_Type()
)
osPortCntSentMultiPacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortCntSentMultiPacks.setStatus("current")
_OsPortCntRecvCRCorAlignmentErrs_Type = Counter64
_OsPortCntRecvCRCorAlignmentErrs_Object = MibTableColumn
osPortCntRecvCRCorAlignmentErrs = _OsPortCntRecvCRCorAlignmentErrs_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 5, 1, 13),
    _OsPortCntRecvCRCorAlignmentErrs_Type()
)
osPortCntRecvCRCorAlignmentErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortCntRecvCRCorAlignmentErrs.setStatus("current")
_OsPortCntRecvShortPacks_Type = Counter64
_OsPortCntRecvShortPacks_Object = MibTableColumn
osPortCntRecvShortPacks = _OsPortCntRecvShortPacks_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 5, 1, 14),
    _OsPortCntRecvShortPacks_Type()
)
osPortCntRecvShortPacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortCntRecvShortPacks.setStatus("current")
_OsPortCntRecvLongPacks_Type = Counter64
_OsPortCntRecvLongPacks_Object = MibTableColumn
osPortCntRecvLongPacks = _OsPortCntRecvLongPacks_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 5, 1, 15),
    _OsPortCntRecvLongPacks_Type()
)
osPortCntRecvLongPacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortCntRecvLongPacks.setStatus("current")
_OsPortCntRecvFragmentPacks_Type = Counter64
_OsPortCntRecvFragmentPacks_Object = MibTableColumn
osPortCntRecvFragmentPacks = _OsPortCntRecvFragmentPacks_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 5, 1, 16),
    _OsPortCntRecvFragmentPacks_Type()
)
osPortCntRecvFragmentPacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortCntRecvFragmentPacks.setStatus("current")
_OsPortCntRecvJabberPacks_Type = Counter64
_OsPortCntRecvJabberPacks_Object = MibTableColumn
osPortCntRecvJabberPacks = _OsPortCntRecvJabberPacks_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 5, 1, 17),
    _OsPortCntRecvJabberPacks_Type()
)
osPortCntRecvJabberPacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortCntRecvJabberPacks.setStatus("current")
_OsPortCntRecvAndSentCollisions_Type = Counter64
_OsPortCntRecvAndSentCollisions_Object = MibTableColumn
osPortCntRecvAndSentCollisions = _OsPortCntRecvAndSentCollisions_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 5, 1, 18),
    _OsPortCntRecvAndSentCollisions_Type()
)
osPortCntRecvAndSentCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortCntRecvAndSentCollisions.setStatus("current")
_OsPortCntRecvUpTo64octsPacks_Type = Counter64
_OsPortCntRecvUpTo64octsPacks_Object = MibTableColumn
osPortCntRecvUpTo64octsPacks = _OsPortCntRecvUpTo64octsPacks_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 5, 1, 19),
    _OsPortCntRecvUpTo64octsPacks_Type()
)
osPortCntRecvUpTo64octsPacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortCntRecvUpTo64octsPacks.setStatus("current")
_OsPortCntRecv65to127octsPacks_Type = Counter64
_OsPortCntRecv65to127octsPacks_Object = MibTableColumn
osPortCntRecv65to127octsPacks = _OsPortCntRecv65to127octsPacks_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 5, 1, 20),
    _OsPortCntRecv65to127octsPacks_Type()
)
osPortCntRecv65to127octsPacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortCntRecv65to127octsPacks.setStatus("current")
_OsPortCntRecv128to255octsPacks_Type = Counter64
_OsPortCntRecv128to255octsPacks_Object = MibTableColumn
osPortCntRecv128to255octsPacks = _OsPortCntRecv128to255octsPacks_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 5, 1, 22),
    _OsPortCntRecv128to255octsPacks_Type()
)
osPortCntRecv128to255octsPacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortCntRecv128to255octsPacks.setStatus("current")
_OsPortCntRecv256to511octsPacks_Type = Counter64
_OsPortCntRecv256to511octsPacks_Object = MibTableColumn
osPortCntRecv256to511octsPacks = _OsPortCntRecv256to511octsPacks_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 5, 1, 23),
    _OsPortCntRecv256to511octsPacks_Type()
)
osPortCntRecv256to511octsPacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortCntRecv256to511octsPacks.setStatus("current")
_OsPortCntRecv512to1023octsPacks_Type = Counter64
_OsPortCntRecv512to1023octsPacks_Object = MibTableColumn
osPortCntRecv512to1023octsPacks = _OsPortCntRecv512to1023octsPacks_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 5, 1, 24),
    _OsPortCntRecv512to1023octsPacks_Type()
)
osPortCntRecv512to1023octsPacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortCntRecv512to1023octsPacks.setStatus("current")
_OsPortCntRecvAbove1023octsPacks_Type = Counter64
_OsPortCntRecvAbove1023octsPacks_Object = MibTableColumn
osPortCntRecvAbove1023octsPacks = _OsPortCntRecvAbove1023octsPacks_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 5, 1, 25),
    _OsPortCntRecvAbove1023octsPacks_Type()
)
osPortCntRecvAbove1023octsPacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortCntRecvAbove1023octsPacks.setStatus("current")
_OsPortCntLateCollisions_Type = Counter64
_OsPortCntLateCollisions_Object = MibTableColumn
osPortCntLateCollisions = _OsPortCntLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 5, 1, 41),
    _OsPortCntLateCollisions_Type()
)
osPortCntLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortCntLateCollisions.setStatus("current")
_OsPortCntRecvBadBytes_Type = Counter64
_OsPortCntRecvBadBytes_Object = MibTableColumn
osPortCntRecvBadBytes = _OsPortCntRecvBadBytes_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 5, 1, 42),
    _OsPortCntRecvBadBytes_Type()
)
osPortCntRecvBadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortCntRecvBadBytes.setStatus("current")


class _OsPortCntEgressClear_Type(Integer32):
    """Custom type osPortCntEgressClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("clear", 2))
    )


_OsPortCntEgressClear_Type.__name__ = "Integer32"
_OsPortCntEgressClear_Object = MibTableColumn
osPortCntEgressClear = _OsPortCntEgressClear_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 5, 1, 43),
    _OsPortCntEgressClear_Type()
)
osPortCntEgressClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPortCntEgressClear.setStatus("current")
_OsPortShapeParametersTable_Object = MibTable
osPortShapeParametersTable = _OsPortShapeParametersTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 6)
)
if mibBuilder.loadTexts:
    osPortShapeParametersTable.setStatus("current")
_OsPortShapeParametersEntry_Object = MibTableRow
osPortShapeParametersEntry = _OsPortShapeParametersEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 6, 1)
)
osPortShapeParametersEntry.setIndexNames(
    (0, "OS-PORT-MIB", "osPortIndex"),
    (0, "OS-PORT-MIB", "osPortShapeDir"),
)
if mibBuilder.loadTexts:
    osPortShapeParametersEntry.setStatus("current")


class _OsPortShapeCapability_Type(Integer32):
    """Custom type osPortShapeCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 1),
          ("available", 2))
    )


_OsPortShapeCapability_Type.__name__ = "Integer32"
_OsPortShapeCapability_Object = MibTableColumn
osPortShapeCapability = _OsPortShapeCapability_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 6, 1, 1),
    _OsPortShapeCapability_Type()
)
osPortShapeCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortShapeCapability.setStatus("current")
_OsPortShapeMinRate_Type = Gauge32
_OsPortShapeMinRate_Object = MibTableColumn
osPortShapeMinRate = _OsPortShapeMinRate_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 6, 1, 2),
    _OsPortShapeMinRate_Type()
)
osPortShapeMinRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortShapeMinRate.setStatus("current")
if mibBuilder.loadTexts:
    osPortShapeMinRate.setUnits("kilobits per second")
_OsPortShapeMaxRate_Type = Gauge32
_OsPortShapeMaxRate_Object = MibTableColumn
osPortShapeMaxRate = _OsPortShapeMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 6, 1, 3),
    _OsPortShapeMaxRate_Type()
)
osPortShapeMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortShapeMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    osPortShapeMaxRate.setUnits("kilobits per second")
_OsPortShapeMinBurstSize_Type = Gauge32
_OsPortShapeMinBurstSize_Object = MibTableColumn
osPortShapeMinBurstSize = _OsPortShapeMinBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 6, 1, 4),
    _OsPortShapeMinBurstSize_Type()
)
osPortShapeMinBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortShapeMinBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    osPortShapeMinBurstSize.setUnits("KBytes")
_OsPortShapeMaxBurstSize_Type = Gauge32
_OsPortShapeMaxBurstSize_Object = MibTableColumn
osPortShapeMaxBurstSize = _OsPortShapeMaxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 6, 1, 5),
    _OsPortShapeMaxBurstSize_Type()
)
osPortShapeMaxBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortShapeMaxBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    osPortShapeMaxBurstSize.setUnits("KBytes")
_OsPortBuffersProfileTable_Object = MibTable
osPortBuffersProfileTable = _OsPortBuffersProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 7)
)
if mibBuilder.loadTexts:
    osPortBuffersProfileTable.setStatus("current")
_OsPortBuffersProfileEntry_Object = MibTableRow
osPortBuffersProfileEntry = _OsPortBuffersProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 7, 1)
)
osPortBuffersProfileEntry.setIndexNames(
    (0, "OS-PORT-MIB", "osBufferProfileIndex"),
    (0, "OS-PORT-MIB", "osBufferProfileServiceLevel"),
)
if mibBuilder.loadTexts:
    osPortBuffersProfileEntry.setStatus("current")
_OsBufferProfileIndex_Type = BuffersProfileIndex
_OsBufferProfileIndex_Object = MibTableColumn
osBufferProfileIndex = _OsBufferProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 7, 1, 1),
    _OsBufferProfileIndex_Type()
)
osBufferProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osBufferProfileIndex.setStatus("current")


class _OsBufferProfileServiceLevel_Type(Unsigned32):
    """Custom type osBufferProfileServiceLevel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_OsBufferProfileServiceLevel_Type.__name__ = "Unsigned32"
_OsBufferProfileServiceLevel_Object = MibTableColumn
osBufferProfileServiceLevel = _OsBufferProfileServiceLevel_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 7, 1, 2),
    _OsBufferProfileServiceLevel_Type()
)
osBufferProfileServiceLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osBufferProfileServiceLevel.setStatus("current")


class _OsBuffersProfileDescriptorsGreen_Type(Unsigned32):
    """Custom type osBuffersProfileDescriptorsGreen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_OsBuffersProfileDescriptorsGreen_Type.__name__ = "Unsigned32"
_OsBuffersProfileDescriptorsGreen_Object = MibTableColumn
osBuffersProfileDescriptorsGreen = _OsBuffersProfileDescriptorsGreen_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 7, 1, 3),
    _OsBuffersProfileDescriptorsGreen_Type()
)
osBuffersProfileDescriptorsGreen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osBuffersProfileDescriptorsGreen.setStatus("current")


class _OsBuffersProfileDescriptorsYellow_Type(Unsigned32):
    """Custom type osBuffersProfileDescriptorsYellow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_OsBuffersProfileDescriptorsYellow_Type.__name__ = "Unsigned32"
_OsBuffersProfileDescriptorsYellow_Object = MibTableColumn
osBuffersProfileDescriptorsYellow = _OsBuffersProfileDescriptorsYellow_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 7, 1, 4),
    _OsBuffersProfileDescriptorsYellow_Type()
)
osBuffersProfileDescriptorsYellow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osBuffersProfileDescriptorsYellow.setStatus("current")


class _OsBuffersProfileDescriptorsRed_Type(Unsigned32):
    """Custom type osBuffersProfileDescriptorsRed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_OsBuffersProfileDescriptorsRed_Type.__name__ = "Unsigned32"
_OsBuffersProfileDescriptorsRed_Object = MibTableColumn
osBuffersProfileDescriptorsRed = _OsBuffersProfileDescriptorsRed_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 7, 1, 5),
    _OsBuffersProfileDescriptorsRed_Type()
)
osBuffersProfileDescriptorsRed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osBuffersProfileDescriptorsRed.setStatus("current")


class _OsBuffersProfileBuffersGreen_Type(Unsigned32):
    """Custom type osBuffersProfileBuffersGreen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_OsBuffersProfileBuffersGreen_Type.__name__ = "Unsigned32"
_OsBuffersProfileBuffersGreen_Object = MibTableColumn
osBuffersProfileBuffersGreen = _OsBuffersProfileBuffersGreen_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 7, 1, 6),
    _OsBuffersProfileBuffersGreen_Type()
)
osBuffersProfileBuffersGreen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osBuffersProfileBuffersGreen.setStatus("current")


class _OsBuffersProfileBuffersYellow_Type(Unsigned32):
    """Custom type osBuffersProfileBuffersYellow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_OsBuffersProfileBuffersYellow_Type.__name__ = "Unsigned32"
_OsBuffersProfileBuffersYellow_Object = MibTableColumn
osBuffersProfileBuffersYellow = _OsBuffersProfileBuffersYellow_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 7, 1, 7),
    _OsBuffersProfileBuffersYellow_Type()
)
osBuffersProfileBuffersYellow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osBuffersProfileBuffersYellow.setStatus("current")


class _OsBuffersProfileBuffersRed_Type(Unsigned32):
    """Custom type osBuffersProfileBuffersRed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_OsBuffersProfileBuffersRed_Type.__name__ = "Unsigned32"
_OsBuffersProfileBuffersRed_Object = MibTableColumn
osBuffersProfileBuffersRed = _OsBuffersProfileBuffersRed_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 7, 1, 8),
    _OsBuffersProfileBuffersRed_Type()
)
osBuffersProfileBuffersRed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osBuffersProfileBuffersRed.setStatus("current")


class _OsBuffersProfileWredThresholdGreen_Type(Unsigned32):
    """Custom type osBuffersProfileWredThresholdGreen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_OsBuffersProfileWredThresholdGreen_Type.__name__ = "Unsigned32"
_OsBuffersProfileWredThresholdGreen_Object = MibTableColumn
osBuffersProfileWredThresholdGreen = _OsBuffersProfileWredThresholdGreen_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 7, 1, 9),
    _OsBuffersProfileWredThresholdGreen_Type()
)
osBuffersProfileWredThresholdGreen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osBuffersProfileWredThresholdGreen.setStatus("current")
if mibBuilder.loadTexts:
    osBuffersProfileWredThresholdGreen.setUnits("Percentage")


class _OsBuffersProfileWredThresholdYellow_Type(Unsigned32):
    """Custom type osBuffersProfileWredThresholdYellow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_OsBuffersProfileWredThresholdYellow_Type.__name__ = "Unsigned32"
_OsBuffersProfileWredThresholdYellow_Object = MibTableColumn
osBuffersProfileWredThresholdYellow = _OsBuffersProfileWredThresholdYellow_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 7, 1, 10),
    _OsBuffersProfileWredThresholdYellow_Type()
)
osBuffersProfileWredThresholdYellow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osBuffersProfileWredThresholdYellow.setStatus("current")
if mibBuilder.loadTexts:
    osBuffersProfileWredThresholdYellow.setUnits("Percentage")


class _OsBuffersProfileWredThresholdRed_Type(Unsigned32):
    """Custom type osBuffersProfileWredThresholdRed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_OsBuffersProfileWredThresholdRed_Type.__name__ = "Unsigned32"
_OsBuffersProfileWredThresholdRed_Object = MibTableColumn
osBuffersProfileWredThresholdRed = _OsBuffersProfileWredThresholdRed_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 7, 1, 11),
    _OsBuffersProfileWredThresholdRed_Type()
)
osBuffersProfileWredThresholdRed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osBuffersProfileWredThresholdRed.setStatus("current")
if mibBuilder.loadTexts:
    osBuffersProfileWredThresholdRed.setUnits("Percentage")
_OsPortBuffersCfg_ObjectIdentity = ObjectIdentity
osPortBuffersCfg = _OsPortBuffersCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 8)
)


class _OsPortBuffersShared_Type(Integer32):
    """Custom type osPortBuffersShared based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_OsPortBuffersShared_Type.__name__ = "Integer32"
_OsPortBuffersShared_Object = MibScalar
osPortBuffersShared = _OsPortBuffersShared_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 8, 1),
    _OsPortBuffersShared_Type()
)
osPortBuffersShared.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPortBuffersShared.setStatus("current")


class _OsPortBuffersWRED_Type(Integer32):
    """Custom type osPortBuffersWRED based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_OsPortBuffersWRED_Type.__name__ = "Integer32"
_OsPortBuffersWRED_Object = MibScalar
osPortBuffersWRED = _OsPortBuffersWRED_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 8, 2),
    _OsPortBuffersWRED_Type()
)
osPortBuffersWRED.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPortBuffersWRED.setStatus("current")
_OsPortEthTypeTable_Object = MibTable
osPortEthTypeTable = _OsPortEthTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 9)
)
if mibBuilder.loadTexts:
    osPortEthTypeTable.setStatus("current")
_OsPortEthTypeEntry_Object = MibTableRow
osPortEthTypeEntry = _OsPortEthTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 9, 1)
)
osPortEthTypeEntry.setIndexNames(
    (0, "OS-PORT-MIB", "osPortIndex"),
)
if mibBuilder.loadTexts:
    osPortEthTypeEntry.setStatus("current")


class _OsPortEthType_Type(Integer32):
    """Custom type osPortEthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("coreEth1", 1),
          ("coreEth2", 2))
    )


_OsPortEthType_Type.__name__ = "Integer32"
_OsPortEthType_Object = MibTableColumn
osPortEthType = _OsPortEthType_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 9, 1, 1),
    _OsPortEthType_Type()
)
osPortEthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPortEthType.setStatus("current")
_OsPortEgressCntTable_Object = MibTable
osPortEgressCntTable = _OsPortEgressCntTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 10)
)
if mibBuilder.loadTexts:
    osPortEgressCntTable.setStatus("current")
_OsPortEgressCntEntry_Object = MibTableRow
osPortEgressCntEntry = _OsPortEgressCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 10, 1)
)
osPortEgressCntEntry.setIndexNames(
    (0, "OS-PORT-MIB", "osPortIndex"),
    (0, "OS-PORT-MIB", "osBufferProfileServiceLevel"),
    (0, "OS-PORT-MIB", "osPortEgressUnits"),
    (0, "OS-PORT-MIB", "osPortEgressValueType"),
)
if mibBuilder.loadTexts:
    osPortEgressCntEntry.setStatus("current")


class _OsPortEgressUnits_Type(Integer32):
    """Custom type osPortEgressUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bytes", 1),
          ("packets", 2))
    )


_OsPortEgressUnits_Type.__name__ = "Integer32"
_OsPortEgressUnits_Object = MibTableColumn
osPortEgressUnits = _OsPortEgressUnits_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 10, 1, 3),
    _OsPortEgressUnits_Type()
)
osPortEgressUnits.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osPortEgressUnits.setStatus("current")


class _OsPortEgressValueType_Type(Integer32):
    """Custom type osPortEgressValueType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("passOther", 2),
          ("passGreen", 3),
          ("drop", 4),
          ("dropOther", 5),
          ("dropGreen", 6))
    )


_OsPortEgressValueType_Type.__name__ = "Integer32"
_OsPortEgressValueType_Object = MibTableColumn
osPortEgressValueType = _OsPortEgressValueType_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 10, 1, 4),
    _OsPortEgressValueType_Type()
)
osPortEgressValueType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osPortEgressValueType.setStatus("current")
_OsPortEgressCounter_Type = Counter64
_OsPortEgressCounter_Object = MibTableColumn
osPortEgressCounter = _OsPortEgressCounter_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 10, 1, 5),
    _OsPortEgressCounter_Type()
)
osPortEgressCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortEgressCounter.setStatus("current")
_OsPortTrunkExtTable_Object = MibTable
osPortTrunkExtTable = _OsPortTrunkExtTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 14)
)
if mibBuilder.loadTexts:
    osPortTrunkExtTable.setStatus("current")
_OsPortTrunkExtEntry_Object = MibTableRow
osPortTrunkExtEntry = _OsPortTrunkExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 14, 1)
)
osPortTrunkExtEntry.setIndexNames(
    (0, "OS-PORT-MIB", "osPortTrunkId"),
)
if mibBuilder.loadTexts:
    osPortTrunkExtEntry.setStatus("current")


class _OsPortTrunkMaxPortBundle_Type(Integer32):
    """Custom type osPortTrunkMaxPortBundle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_OsPortTrunkMaxPortBundle_Type.__name__ = "Integer32"
_OsPortTrunkMaxPortBundle_Object = MibTableColumn
osPortTrunkMaxPortBundle = _OsPortTrunkMaxPortBundle_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 14, 1, 3),
    _OsPortTrunkMaxPortBundle_Type()
)
osPortTrunkMaxPortBundle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPortTrunkMaxPortBundle.setStatus("current")


class _OsPortTrunkRevertive_Type(TruthValue):
    """Custom type osPortTrunkRevertive based on TruthValue"""
    defaultValue = 2


_OsPortTrunkRevertive_Type.__name__ = "TruthValue"
_OsPortTrunkRevertive_Object = MibTableColumn
osPortTrunkRevertive = _OsPortTrunkRevertive_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 14, 1, 4),
    _OsPortTrunkRevertive_Type()
)
osPortTrunkRevertive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPortTrunkRevertive.setStatus("current")


class _OsPortTrunkFastSwitchover_Type(TruthValue):
    """Custom type osPortTrunkFastSwitchover based on TruthValue"""
    defaultValue = 2


_OsPortTrunkFastSwitchover_Type.__name__ = "TruthValue"
_OsPortTrunkFastSwitchover_Object = MibTableColumn
osPortTrunkFastSwitchover = _OsPortTrunkFastSwitchover_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 14, 1, 5),
    _OsPortTrunkFastSwitchover_Type()
)
osPortTrunkFastSwitchover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPortTrunkFastSwitchover.setStatus("current")


class _OsPortTrunkLowerThreshold_Type(Integer32):
    """Custom type osPortTrunkLowerThreshold based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_OsPortTrunkLowerThreshold_Type.__name__ = "Integer32"
_OsPortTrunkLowerThreshold_Object = MibTableColumn
osPortTrunkLowerThreshold = _OsPortTrunkLowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 14, 1, 6),
    _OsPortTrunkLowerThreshold_Type()
)
osPortTrunkLowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPortTrunkLowerThreshold.setStatus("current")


class _OsPortTrunkHigherThreshold_Type(Integer32):
    """Custom type osPortTrunkHigherThreshold based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_OsPortTrunkHigherThreshold_Type.__name__ = "Integer32"
_OsPortTrunkHigherThreshold_Object = MibTableColumn
osPortTrunkHigherThreshold = _OsPortTrunkHigherThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 14, 1, 7),
    _OsPortTrunkHigherThreshold_Type()
)
osPortTrunkHigherThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPortTrunkHigherThreshold.setStatus("current")
_OsPortTrunkTearDown_Type = TruthValue
_OsPortTrunkTearDown_Object = MibTableColumn
osPortTrunkTearDown = _OsPortTrunkTearDown_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 14, 1, 17),
    _OsPortTrunkTearDown_Type()
)
osPortTrunkTearDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPortTrunkTearDown.setStatus("current")
_OsPortFloodLimitTable_Object = MibTable
osPortFloodLimitTable = _OsPortFloodLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 15)
)
if mibBuilder.loadTexts:
    osPortFloodLimitTable.setStatus("current")
_OsPortFloodLimitEntry_Object = MibTableRow
osPortFloodLimitEntry = _OsPortFloodLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 15, 1)
)
osPortFloodLimitEntry.setIndexNames(
    (0, "OS-PORT-MIB", "osPortIndex"),
)
if mibBuilder.loadTexts:
    osPortFloodLimitEntry.setStatus("current")


class _OsPortFloodLimitTypes_Type(Bits):
    """Custom type osPortFloodLimitTypes based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("unknownUnicast", 0),
          ("multicast", 1),
          ("broadcast", 2),
          ("tcpSyn", 3),
          ("reserved", 4),
          ("deleteAll", 5))
    )

_OsPortFloodLimitTypes_Type.__name__ = "Bits"
_OsPortFloodLimitTypes_Object = MibTableColumn
osPortFloodLimitTypes = _OsPortFloodLimitTypes_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 15, 1, 5),
    _OsPortFloodLimitTypes_Type()
)
osPortFloodLimitTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPortFloodLimitTypes.setStatus("current")


class _OsPortFloodLimitRate_Type(Gauge32):
    """Custom type osPortFloodLimitRate based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_OsPortFloodLimitRate_Type.__name__ = "Gauge32"
_OsPortFloodLimitRate_Object = MibTableColumn
osPortFloodLimitRate = _OsPortFloodLimitRate_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 15, 1, 6),
    _OsPortFloodLimitRate_Type()
)
osPortFloodLimitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPortFloodLimitRate.setStatus("current")
if mibBuilder.loadTexts:
    osPortFloodLimitRate.setUnits("Kbits/sec")
_OsPortGen_ObjectIdentity = ObjectIdentity
osPortGen = _OsPortGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 70)
)
_OsPortMflgMac_Type = MacAddress
_OsPortMflgMac_Object = MibScalar
osPortMflgMac = _OsPortMflgMac_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 70, 3),
    _OsPortMflgMac_Type()
)
osPortMflgMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    osPortMflgMac.setStatus("current")
_OsPortConformance_ObjectIdentity = ObjectIdentity
osPortConformance = _OsPortConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 101)
)
_OsPortMIBCompliances_ObjectIdentity = ObjectIdentity
osPortMIBCompliances = _OsPortMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 101, 1)
)
_OsPortMIBGroups_ObjectIdentity = ObjectIdentity
osPortMIBGroups = _OsPortMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 101, 2)
)
_OsPortCoreEgressEth_ObjectIdentity = ObjectIdentity
osPortCoreEgressEth = _OsPortCoreEgressEth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 102)
)


class _OsPortEthType1_Type(OctetString):
    """Custom type osPortEthType1 based on OctetString"""
    defaultHexValue = "8100"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_OsPortEthType1_Type.__name__ = "OctetString"
_OsPortEthType1_Object = MibScalar
osPortEthType1 = _OsPortEthType1_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 102, 1),
    _OsPortEthType1_Type()
)
osPortEthType1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPortEthType1.setStatus("current")


class _OsPortEthType2_Type(OctetString):
    """Custom type osPortEthType2 based on OctetString"""
    defaultHexValue = "8100"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_OsPortEthType2_Type.__name__ = "OctetString"
_OsPortEthType2_Object = MibScalar
osPortEthType2 = _OsPortEthType2_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 102, 2),
    _OsPortEthType2_Type()
)
osPortEthType2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPortEthType2.setStatus("current")
osPortEntry.registerAugmentions(
    ("OS-PORT-MIB",
     "osPortCntEntry")
)
osPortCntEntry.setIndexNames(*osPortEntry.getIndexNames())

# Managed Objects groups

osPortMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 101, 2, 1)
)
osPortMandatoryGroup.setObjects(
      *(("OS-PORT-MIB", "osPortCfgSupport"),
        ("OS-PORT-MIB", "osPortCfgMaxNumberOfPort"),
        ("OS-PORT-MIB", "osPortCfgBaseTrunkPortIndex"),
        ("OS-PORT-MIB", "osPortCfgMaxNumberOfSl"),
        ("OS-PORT-MIB", "osPortCfgMaxTrunkId"),
        ("OS-PORT-MIB", "osPortDescription"),
        ("OS-PORT-MIB", "osPortLink"),
        ("OS-PORT-MIB", "osPortAdminSpeed"),
        ("OS-PORT-MIB", "osPortOperSpeed"),
        ("OS-PORT-MIB", "osPortDuplex"),
        ("OS-PORT-MIB", "osPortAdminState"),
        ("OS-PORT-MIB", "osPortOperState"),
        ("OS-PORT-MIB", "osPortBlockReason"),
        ("OS-PORT-MIB", "osPortBuffersProfileIndex"),
        ("OS-PORT-MIB", "osPortTrunkIndex"),
        ("OS-PORT-MIB", "osPortLacpAdminMode"),
        ("OS-PORT-MIB", "osPortLacpOperState"),
        ("OS-PORT-MIB", "osPortMtuSize"),
        ("OS-PORT-MIB", "osPortQosMarkingVpt"),
        ("OS-PORT-MIB", "osPortQosTrust"),
        ("OS-PORT-MIB", "osPortRemarkingDei"),
        ("OS-PORT-MIB", "osPortSl"),
        ("OS-PORT-MIB", "osPortTagType"),
        ("OS-PORT-MIB", "osPortTagDefaultTag"),
        ("OS-PORT-MIB", "osPortL2CtrlDot1x"),
        ("OS-PORT-MIB", "osPortL2CtrlLACP"),
        ("OS-PORT-MIB", "osPortL2CtrlSTP"),
        ("OS-PORT-MIB", "osPortL2CtrlGVRP"),
        ("OS-PORT-MIB", "osPortL2CtrlPause"),
        ("OS-PORT-MIB", "osPortL2CtrlLinkOAM"),
        ("OS-PORT-MIB", "osPortL2CtrlELMI"),
        ("OS-PORT-MIB", "osPortL2CtrlLLDP"),
        ("OS-PORT-MIB", "osPortL2CtrlDTP"),
        ("OS-PORT-MIB", "osPortL2CtrlPAGP"),
        ("OS-PORT-MIB", "osPortL2CtrlVTP"),
        ("OS-PORT-MIB", "osPortL2CtrlCDP"),
        ("OS-PORT-MIB", "osPortL2CtrlPVST"),
        ("OS-PORT-MIB", "osPortAdminMediaSelect"),
        ("OS-PORT-MIB", "osPortOperMediaSelect"),
        ("OS-PORT-MIB", "osPortLanType"),
        ("OS-PORT-MIB", "osPortIfType"),
        ("OS-PORT-MIB", "osPortLastError"),
        ("OS-PORT-MIB", "osPortEthType1"),
        ("OS-PORT-MIB", "osPortEthType2"),
        ("OS-PORT-MIB", "osPortShapeRate"),
        ("OS-PORT-MIB", "osPortShapeBurstSize"),
        ("OS-PORT-MIB", "osPortShapeLastError"),
        ("OS-PORT-MIB", "osPortShapeLocked"),
        ("OS-PORT-MIB", "osPortShapeAdminStatus"),
        ("OS-PORT-MIB", "osPortShapeCapability"),
        ("OS-PORT-MIB", "osPortShapeMinRate"),
        ("OS-PORT-MIB", "osPortShapeMaxRate"),
        ("OS-PORT-MIB", "osPortShapeMinBurstSize"),
        ("OS-PORT-MIB", "osPortShapeMaxBurstSize"),
        ("OS-PORT-MIB", "osBuffersProfileDescriptorsGreen"),
        ("OS-PORT-MIB", "osBuffersProfileDescriptorsYellow"),
        ("OS-PORT-MIB", "osBuffersProfileDescriptorsRed"),
        ("OS-PORT-MIB", "osBuffersProfileBuffersGreen"),
        ("OS-PORT-MIB", "osBuffersProfileBuffersYellow"),
        ("OS-PORT-MIB", "osBuffersProfileBuffersRed"),
        ("OS-PORT-MIB", "osBuffersProfileWredThresholdGreen"),
        ("OS-PORT-MIB", "osBuffersProfileWredThresholdYellow"),
        ("OS-PORT-MIB", "osBuffersProfileWredThresholdRed"),
        ("OS-PORT-MIB", "osPortBuffersShared"),
        ("OS-PORT-MIB", "osPortBuffersWRED"),
        ("OS-PORT-MIB", "osPortMflgMac"),
        ("OS-PORT-MIB", "osPortTrunkIndexId"),
        ("OS-PORT-MIB", "osPortTrunkMembers"),
        ("OS-PORT-MIB", "osPortTrunkAdminStatus"),
        ("OS-PORT-MIB", "osPortTrunkNumOfMembers"),
        ("OS-PORT-MIB", "osPortTrunkLastError"),
        ("OS-PORT-MIB", "osPortCntEgressClearAll"),
        ("OS-PORT-MIB", "osPortTrunkMaxPortBundle"),
        ("OS-PORT-MIB", "osPortTrunkRevertive"),
        ("OS-PORT-MIB", "osPortTrunkFastSwitchover"),
        ("OS-PORT-MIB", "osPortTrunkLowerThreshold"),
        ("OS-PORT-MIB", "osPortTrunkHigherThreshold"),
        ("OS-PORT-MIB", "osPortTrunkTearDown"),
        ("OS-PORT-MIB", "osPortCntClearAll"),
        ("OS-PORT-MIB", "osPortCntRecvBytes"),
        ("OS-PORT-MIB", "osPortCntRecvPacks"),
        ("OS-PORT-MIB", "osPortCntRecvUniPacks"),
        ("OS-PORT-MIB", "osPortCntRecvBroadPacks"),
        ("OS-PORT-MIB", "osPortCntRecvMultiPacks"),
        ("OS-PORT-MIB", "osPortCntSentBytes"),
        ("OS-PORT-MIB", "osPortCntSentPacks"),
        ("OS-PORT-MIB", "osPortCntSentUniPacks"),
        ("OS-PORT-MIB", "osPortCntSentBroadPacks"),
        ("OS-PORT-MIB", "osPortCntSentMultiPacks"),
        ("OS-PORT-MIB", "osPortCntRecvCRCorAlignmentErrs"),
        ("OS-PORT-MIB", "osPortCntRecvShortPacks"),
        ("OS-PORT-MIB", "osPortCntRecvLongPacks"),
        ("OS-PORT-MIB", "osPortCntRecvFragmentPacks"),
        ("OS-PORT-MIB", "osPortCntRecvJabberPacks"),
        ("OS-PORT-MIB", "osPortCntRecvAndSentCollisions"),
        ("OS-PORT-MIB", "osPortCntRecvUpTo64octsPacks"),
        ("OS-PORT-MIB", "osPortCntRecv65to127octsPacks"),
        ("OS-PORT-MIB", "osPortCntRecv128to255octsPacks"),
        ("OS-PORT-MIB", "osPortCntRecv256to511octsPacks"),
        ("OS-PORT-MIB", "osPortCntRecv512to1023octsPacks"),
        ("OS-PORT-MIB", "osPortCntRecvAbove1023octsPacks"),
        ("OS-PORT-MIB", "osPortCntLateCollisions"),
        ("OS-PORT-MIB", "osPortCntRecvBadBytes"),
        ("OS-PORT-MIB", "osPortEthType"),
        ("OS-PORT-MIB", "osPortEgressCounter"),
        ("OS-PORT-MIB", "osPortCntEgressClear"),
        ("OS-PORT-MIB", "osPortFloodLimitTypes"),
        ("OS-PORT-MIB", "osPortFloodLimitRate"))
)
if mibBuilder.loadTexts:
    osPortMandatoryGroup.setStatus("current")


# Notification objects

osPortMgmtEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 0, 1)
)
osPortMgmtEnabled.setObjects(
    ("OS-PORT-MIB", "osPortDescription")
)
if mibBuilder.loadTexts:
    osPortMgmtEnabled.setStatus(
        "current"
    )

osPortMgmtDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 0, 2)
)
osPortMgmtDisabled.setObjects(
    ("OS-PORT-MIB", "osPortDescription")
)
if mibBuilder.loadTexts:
    osPortMgmtDisabled.setStatus(
        "current"
    )

osPortSfpInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 0, 3)
)
osPortSfpInserted.setObjects(
    ("OS-PORT-MIB", "osPortDescription")
)
if mibBuilder.loadTexts:
    osPortSfpInserted.setStatus(
        "current"
    )

osPortSfpRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 0, 4)
)
osPortSfpRemoved.setObjects(
    ("OS-PORT-MIB", "osPortDescription")
)
if mibBuilder.loadTexts:
    osPortSfpRemoved.setStatus(
        "current"
    )

osPortSfpI2cFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 0, 5)
)
osPortSfpI2cFailure.setObjects(
    ("OS-PORT-MIB", "osPortOperState")
)
if mibBuilder.loadTexts:
    osPortSfpI2cFailure.setStatus(
        "current"
    )

osPortSfpI2cRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 0, 6)
)
osPortSfpI2cRecovery.setObjects(
    ("OS-PORT-MIB", "osPortOperState")
)
if mibBuilder.loadTexts:
    osPortSfpI2cRecovery.setStatus(
        "current"
    )

osPortSfpAutoDetectErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 0, 7)
)
osPortSfpAutoDetectErr.setObjects(
    ("OS-PORT-MIB", "osPortLastError")
)
if mibBuilder.loadTexts:
    osPortSfpAutoDetectErr.setStatus(
        "current"
    )

osPortIsolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 0, 8)
)
osPortIsolation.setObjects(
      *(("OS-PORT-MIB", "osPortOperState"),
        ("OS-PORT-MIB", "osPortMflgMac"))
)
if mibBuilder.loadTexts:
    osPortIsolation.setStatus(
        "current"
    )

osPortRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 0, 9)
)
osPortRecovery.setObjects(
    ("OS-PORT-MIB", "osPortOperState")
)
if mibBuilder.loadTexts:
    osPortRecovery.setStatus(
        "current"
    )


# Notifications groups

osPortNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 101, 2, 2)
)
osPortNotificationsGroup.setObjects(
      *(("OS-PORT-MIB", "osPortMgmtEnabled"),
        ("OS-PORT-MIB", "osPortMgmtDisabled"),
        ("OS-PORT-MIB", "osPortSfpInserted"),
        ("OS-PORT-MIB", "osPortSfpRemoved"),
        ("OS-PORT-MIB", "osPortSfpI2cFailure"),
        ("OS-PORT-MIB", "osPortSfpI2cRecovery"),
        ("OS-PORT-MIB", "osPortSfpAutoDetectErr"),
        ("OS-PORT-MIB", "osPortIsolation"),
        ("OS-PORT-MIB", "osPortRecovery"))
)
if mibBuilder.loadTexts:
    osPortNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

osPortMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6926, 2, 1, 101, 1, 1)
)
osPortMIBCompliance.setObjects(
      *(("OS-PORT-MIB", "osPortMandatoryGroup"),
        ("OS-PORT-MIB", "osPortNotificationsGroup"))
)
if mibBuilder.loadTexts:
    osPortMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OS-PORT-MIB",
    **{"SupportValue": SupportValue,
       "BuffersProfileIndex": BuffersProfileIndex,
       "L2CtrlProcess": L2CtrlProcess,
       "PortEntryValidator": PortEntryValidator,
       "LastError": LastError,
       "osPort": osPort,
       "osPortNotifications": osPortNotifications,
       "osPortMgmtEnabled": osPortMgmtEnabled,
       "osPortMgmtDisabled": osPortMgmtDisabled,
       "osPortSfpInserted": osPortSfpInserted,
       "osPortSfpRemoved": osPortSfpRemoved,
       "osPortSfpI2cFailure": osPortSfpI2cFailure,
       "osPortSfpI2cRecovery": osPortSfpI2cRecovery,
       "osPortSfpAutoDetectErr": osPortSfpAutoDetectErr,
       "osPortIsolation": osPortIsolation,
       "osPortRecovery": osPortRecovery,
       "osPortCfg": osPortCfg,
       "osPortCfgSupport": osPortCfgSupport,
       "osPortCfgMaxNumberOfPort": osPortCfgMaxNumberOfPort,
       "osPortCfgBaseTrunkPortIndex": osPortCfgBaseTrunkPortIndex,
       "osPortCfgMaxNumberOfSl": osPortCfgMaxNumberOfSl,
       "osPortCfgMaxTrunkId": osPortCfgMaxTrunkId,
       "osPortTrunkLastError": osPortTrunkLastError,
       "osPortCntEgressClearAll": osPortCntEgressClearAll,
       "osPortTable": osPortTable,
       "osPortEntry": osPortEntry,
       "osPortIndex": osPortIndex,
       "osPortDescription": osPortDescription,
       "osPortLink": osPortLink,
       "osPortAdminSpeed": osPortAdminSpeed,
       "osPortOperSpeed": osPortOperSpeed,
       "osPortDuplex": osPortDuplex,
       "osPortAdminState": osPortAdminState,
       "osPortOperState": osPortOperState,
       "osPortBlockReason": osPortBlockReason,
       "osPortBuffersProfileIndex": osPortBuffersProfileIndex,
       "osPortTrunkIndex": osPortTrunkIndex,
       "osPortLacpAdminMode": osPortLacpAdminMode,
       "osPortLacpOperState": osPortLacpOperState,
       "osPortMtuSize": osPortMtuSize,
       "osPortQosMarkingVpt": osPortQosMarkingVpt,
       "osPortQosTrust": osPortQosTrust,
       "osPortRemarkingDei": osPortRemarkingDei,
       "osPortSl": osPortSl,
       "osPortTagType": osPortTagType,
       "osPortTagDefaultTag": osPortTagDefaultTag,
       "osPortL2CtrlDot1x": osPortL2CtrlDot1x,
       "osPortL2CtrlLACP": osPortL2CtrlLACP,
       "osPortL2CtrlSTP": osPortL2CtrlSTP,
       "osPortL2CtrlGVRP": osPortL2CtrlGVRP,
       "osPortL2CtrlPause": osPortL2CtrlPause,
       "osPortL2CtrlLinkOAM": osPortL2CtrlLinkOAM,
       "osPortL2CtrlELMI": osPortL2CtrlELMI,
       "osPortL2CtrlLLDP": osPortL2CtrlLLDP,
       "osPortL2CtrlDTP": osPortL2CtrlDTP,
       "osPortL2CtrlPAGP": osPortL2CtrlPAGP,
       "osPortL2CtrlVTP": osPortL2CtrlVTP,
       "osPortL2CtrlCDP": osPortL2CtrlCDP,
       "osPortL2CtrlPVST": osPortL2CtrlPVST,
       "osPortAdminMediaSelect": osPortAdminMediaSelect,
       "osPortOperMediaSelect": osPortOperMediaSelect,
       "osPortLanType": osPortLanType,
       "osPortIfType": osPortIfType,
       "osPortLastError": osPortLastError,
       "osPortShapeTable": osPortShapeTable,
       "osPortShapeEntry": osPortShapeEntry,
       "osPortShapeDir": osPortShapeDir,
       "osPortShapeQId": osPortShapeQId,
       "osPortShapeRate": osPortShapeRate,
       "osPortShapeBurstSize": osPortShapeBurstSize,
       "osPortShapeLastError": osPortShapeLastError,
       "osPortShapeLocked": osPortShapeLocked,
       "osPortShapeAdminStatus": osPortShapeAdminStatus,
       "osPortTrunkTable": osPortTrunkTable,
       "osPortTrunkEntry": osPortTrunkEntry,
       "osPortTrunkId": osPortTrunkId,
       "osPortTrunkIndexId": osPortTrunkIndexId,
       "osPortTrunkMembers": osPortTrunkMembers,
       "osPortTrunkAdminStatus": osPortTrunkAdminStatus,
       "osPortTrunkNumOfMembers": osPortTrunkNumOfMembers,
       "osPortCntTable": osPortCntTable,
       "osPortCntEntry": osPortCntEntry,
       "osPortCntClearAll": osPortCntClearAll,
       "osPortCntRecvBytes": osPortCntRecvBytes,
       "osPortCntRecvPacks": osPortCntRecvPacks,
       "osPortCntRecvUniPacks": osPortCntRecvUniPacks,
       "osPortCntRecvBroadPacks": osPortCntRecvBroadPacks,
       "osPortCntRecvMultiPacks": osPortCntRecvMultiPacks,
       "osPortCntSentBytes": osPortCntSentBytes,
       "osPortCntSentPacks": osPortCntSentPacks,
       "osPortCntSentUniPacks": osPortCntSentUniPacks,
       "osPortCntSentBroadPacks": osPortCntSentBroadPacks,
       "osPortCntSentMultiPacks": osPortCntSentMultiPacks,
       "osPortCntRecvCRCorAlignmentErrs": osPortCntRecvCRCorAlignmentErrs,
       "osPortCntRecvShortPacks": osPortCntRecvShortPacks,
       "osPortCntRecvLongPacks": osPortCntRecvLongPacks,
       "osPortCntRecvFragmentPacks": osPortCntRecvFragmentPacks,
       "osPortCntRecvJabberPacks": osPortCntRecvJabberPacks,
       "osPortCntRecvAndSentCollisions": osPortCntRecvAndSentCollisions,
       "osPortCntRecvUpTo64octsPacks": osPortCntRecvUpTo64octsPacks,
       "osPortCntRecv65to127octsPacks": osPortCntRecv65to127octsPacks,
       "osPortCntRecv128to255octsPacks": osPortCntRecv128to255octsPacks,
       "osPortCntRecv256to511octsPacks": osPortCntRecv256to511octsPacks,
       "osPortCntRecv512to1023octsPacks": osPortCntRecv512to1023octsPacks,
       "osPortCntRecvAbove1023octsPacks": osPortCntRecvAbove1023octsPacks,
       "osPortCntLateCollisions": osPortCntLateCollisions,
       "osPortCntRecvBadBytes": osPortCntRecvBadBytes,
       "osPortCntEgressClear": osPortCntEgressClear,
       "osPortShapeParametersTable": osPortShapeParametersTable,
       "osPortShapeParametersEntry": osPortShapeParametersEntry,
       "osPortShapeCapability": osPortShapeCapability,
       "osPortShapeMinRate": osPortShapeMinRate,
       "osPortShapeMaxRate": osPortShapeMaxRate,
       "osPortShapeMinBurstSize": osPortShapeMinBurstSize,
       "osPortShapeMaxBurstSize": osPortShapeMaxBurstSize,
       "osPortBuffersProfileTable": osPortBuffersProfileTable,
       "osPortBuffersProfileEntry": osPortBuffersProfileEntry,
       "osBufferProfileIndex": osBufferProfileIndex,
       "osBufferProfileServiceLevel": osBufferProfileServiceLevel,
       "osBuffersProfileDescriptorsGreen": osBuffersProfileDescriptorsGreen,
       "osBuffersProfileDescriptorsYellow": osBuffersProfileDescriptorsYellow,
       "osBuffersProfileDescriptorsRed": osBuffersProfileDescriptorsRed,
       "osBuffersProfileBuffersGreen": osBuffersProfileBuffersGreen,
       "osBuffersProfileBuffersYellow": osBuffersProfileBuffersYellow,
       "osBuffersProfileBuffersRed": osBuffersProfileBuffersRed,
       "osBuffersProfileWredThresholdGreen": osBuffersProfileWredThresholdGreen,
       "osBuffersProfileWredThresholdYellow": osBuffersProfileWredThresholdYellow,
       "osBuffersProfileWredThresholdRed": osBuffersProfileWredThresholdRed,
       "osPortBuffersCfg": osPortBuffersCfg,
       "osPortBuffersShared": osPortBuffersShared,
       "osPortBuffersWRED": osPortBuffersWRED,
       "osPortEthTypeTable": osPortEthTypeTable,
       "osPortEthTypeEntry": osPortEthTypeEntry,
       "osPortEthType": osPortEthType,
       "osPortEgressCntTable": osPortEgressCntTable,
       "osPortEgressCntEntry": osPortEgressCntEntry,
       "osPortEgressUnits": osPortEgressUnits,
       "osPortEgressValueType": osPortEgressValueType,
       "osPortEgressCounter": osPortEgressCounter,
       "osPortTrunkExtTable": osPortTrunkExtTable,
       "osPortTrunkExtEntry": osPortTrunkExtEntry,
       "osPortTrunkMaxPortBundle": osPortTrunkMaxPortBundle,
       "osPortTrunkRevertive": osPortTrunkRevertive,
       "osPortTrunkFastSwitchover": osPortTrunkFastSwitchover,
       "osPortTrunkLowerThreshold": osPortTrunkLowerThreshold,
       "osPortTrunkHigherThreshold": osPortTrunkHigherThreshold,
       "osPortTrunkTearDown": osPortTrunkTearDown,
       "osPortFloodLimitTable": osPortFloodLimitTable,
       "osPortFloodLimitEntry": osPortFloodLimitEntry,
       "osPortFloodLimitTypes": osPortFloodLimitTypes,
       "osPortFloodLimitRate": osPortFloodLimitRate,
       "osPortGen": osPortGen,
       "osPortMflgMac": osPortMflgMac,
       "osPortConformance": osPortConformance,
       "osPortMIBCompliances": osPortMIBCompliances,
       "osPortMIBCompliance": osPortMIBCompliance,
       "osPortMIBGroups": osPortMIBGroups,
       "osPortMandatoryGroup": osPortMandatoryGroup,
       "osPortNotificationsGroup": osPortNotificationsGroup,
       "osPortCoreEgressEth": osPortCoreEgressEth,
       "osPortEthType1": osPortEthType1,
       "osPortEthType2": osPortEthType2}
)
