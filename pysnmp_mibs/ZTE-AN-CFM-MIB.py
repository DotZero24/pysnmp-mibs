# SNMP MIB module (ZTE-AN-CFM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-CFM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:26 2025
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

(Dot1agCfmMepIdOrZero,
 dot1agCfmMaIndex,
 dot1agCfmMaNetEntry,
 dot1agCfmMdIndex,
 dot1agCfmMepEntry,
 dot1agCfmMepIdentifier) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmMepIdOrZero",
    "dot1agCfmMaIndex",
    "dot1agCfmMaNetEntry",
    "dot1agCfmMdIndex",
    "dot1agCfmMepEntry",
    "dot1agCfmMepIdentifier")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(zxAn,) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "zxAn")


# MODULE-IDENTITY

zxAnCfmMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnCfmObjects_ObjectIdentity = ObjectIdentity
zxAnCfmObjects = _ZxAnCfmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1)
)
_ZxAnCfmGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnCfmGlobalObjects = _ZxAnCfmGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 1)
)


class _ZxAnCfmEnable_Type(Integer32):
    """Custom type zxAnCfmEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_ZxAnCfmEnable_Type.__name__ = "Integer32"
_ZxAnCfmEnable_Object = MibScalar
zxAnCfmEnable = _ZxAnCfmEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 1, 1),
    _ZxAnCfmEnable_Type()
)
zxAnCfmEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmEnable.setStatus("current")
_ZxAnCfmMa_ObjectIdentity = ObjectIdentity
zxAnCfmMa = _ZxAnCfmMa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 2)
)
_ZxAnCfmMaNetTable_Object = MibTable
zxAnCfmMaNetTable = _ZxAnCfmMaNetTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 2, 1)
)
if mibBuilder.loadTexts:
    zxAnCfmMaNetTable.setStatus("current")
_ZxAnCfmMaNetEntry_Object = MibTableRow
zxAnCfmMaNetEntry = _ZxAnCfmMaNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    zxAnCfmMaNetEntry.setStatus("current")


class _ZxAnCfmMaNetCcmDaType_Type(Integer32):
    """Custom type zxAnCfmMaNetCcmDaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicastclass1", 2))
    )


_ZxAnCfmMaNetCcmDaType_Type.__name__ = "Integer32"
_ZxAnCfmMaNetCcmDaType_Object = MibTableColumn
zxAnCfmMaNetCcmDaType = _ZxAnCfmMaNetCcmDaType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 2, 1, 1, 1),
    _ZxAnCfmMaNetCcmDaType_Type()
)
zxAnCfmMaNetCcmDaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMaNetCcmDaType.setStatus("current")


class _ZxAnCfmMaProtect_Type(Integer32):
    """Custom type zxAnCfmMaProtect based on Integer32"""
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
        *(("maProtectNothing", 1),
          ("cfmMaProtectVlan", 2),
          ("cfmMaProtectTunnel", 3),
          ("cfmMaProtectPort", 4),
          ("cfmMaProtectLink", 5))
    )


_ZxAnCfmMaProtect_Type.__name__ = "Integer32"
_ZxAnCfmMaProtect_Object = MibTableColumn
zxAnCfmMaProtect = _ZxAnCfmMaProtect_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 2, 1, 1, 2),
    _ZxAnCfmMaProtect_Type()
)
zxAnCfmMaProtect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMaProtect.setStatus("current")


class _ZxAnCfmMaTunnel_Type(Unsigned32):
    """Custom type zxAnCfmMaTunnel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ZxAnCfmMaTunnel_Type.__name__ = "Unsigned32"
_ZxAnCfmMaTunnel_Object = MibTableColumn
zxAnCfmMaTunnel = _ZxAnCfmMaTunnel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 2, 1, 1, 3),
    _ZxAnCfmMaTunnel_Type()
)
zxAnCfmMaTunnel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMaTunnel.setStatus("current")
_ZxAnCfmMep_ObjectIdentity = ObjectIdentity
zxAnCfmMep = _ZxAnCfmMep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3)
)
_ZxAnCfmMepTable_Object = MibTable
zxAnCfmMepTable = _ZxAnCfmMepTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1)
)
if mibBuilder.loadTexts:
    zxAnCfmMepTable.setStatus("current")
_ZxAnCfmMepEntry_Object = MibTableRow
zxAnCfmMepEntry = _ZxAnCfmMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    zxAnCfmMepEntry.setStatus("current")
_ZxAnCfmMepCcCheckEnable_Type = TruthValue
_ZxAnCfmMepCcCheckEnable_Object = MibTableColumn
zxAnCfmMepCcCheckEnable = _ZxAnCfmMepCcCheckEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 1),
    _ZxAnCfmMepCcCheckEnable_Type()
)
zxAnCfmMepCcCheckEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepCcCheckEnable.setStatus("current")
_ZxAnCfmMepLmEnable_Type = TruthValue
_ZxAnCfmMepLmEnable_Object = MibTableColumn
zxAnCfmMepLmEnable = _ZxAnCfmMepLmEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 2),
    _ZxAnCfmMepLmEnable_Type()
)
zxAnCfmMepLmEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepLmEnable.setStatus("current")
_ZxAnCfmMepDmEnable_Type = TruthValue
_ZxAnCfmMepDmEnable_Object = MibTableColumn
zxAnCfmMepDmEnable = _ZxAnCfmMepDmEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 3),
    _ZxAnCfmMepDmEnable_Type()
)
zxAnCfmMepDmEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepDmEnable.setStatus("current")


class _ZxAnCfmMepLbmTestType_Type(Integer32):
    """Custom type zxAnCfmMepLbmTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicastclass1", 2))
    )


_ZxAnCfmMepLbmTestType_Type.__name__ = "Integer32"
_ZxAnCfmMepLbmTestType_Object = MibTableColumn
zxAnCfmMepLbmTestType = _ZxAnCfmMepLbmTestType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 4),
    _ZxAnCfmMepLbmTestType_Type()
)
zxAnCfmMepLbmTestType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepLbmTestType.setStatus("current")


class _ZxAnCfmMepLbmAppType_Type(Integer32):
    """Custom type zxAnCfmMepLbmAppType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connectivity", 1),
          ("outofservicediagnostic", 2),
          ("inservicediagnostic", 3))
    )


_ZxAnCfmMepLbmAppType_Type.__name__ = "Integer32"
_ZxAnCfmMepLbmAppType_Object = MibTableColumn
zxAnCfmMepLbmAppType = _ZxAnCfmMepLbmAppType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 5),
    _ZxAnCfmMepLbmAppType_Type()
)
zxAnCfmMepLbmAppType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepLbmAppType.setStatus("current")
_ZxAnCfmMepLmTargetMacAddress_Type = MacAddress
_ZxAnCfmMepLmTargetMacAddress_Object = MibTableColumn
zxAnCfmMepLmTargetMacAddress = _ZxAnCfmMepLmTargetMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 6),
    _ZxAnCfmMepLmTargetMacAddress_Type()
)
zxAnCfmMepLmTargetMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepLmTargetMacAddress.setStatus("current")
_ZxAnCfmMepLmTargetMepId_Type = Dot1agCfmMepIdOrZero
_ZxAnCfmMepLmTargetMepId_Object = MibTableColumn
zxAnCfmMepLmTargetMepId = _ZxAnCfmMepLmTargetMepId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 7),
    _ZxAnCfmMepLmTargetMepId_Type()
)
zxAnCfmMepLmTargetMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepLmTargetMepId.setStatus("current")
_ZxAnCfmMepLmTargetIsMepId_Type = TruthValue
_ZxAnCfmMepLmTargetIsMepId_Object = MibTableColumn
zxAnCfmMepLmTargetIsMepId = _ZxAnCfmMepLmTargetIsMepId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 8),
    _ZxAnCfmMepLmTargetIsMepId_Type()
)
zxAnCfmMepLmTargetIsMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepLmTargetIsMepId.setStatus("current")


class _ZxAnCfmMepLmmDaType_Type(Integer32):
    """Custom type zxAnCfmMepLmmDaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicastclass1", 2))
    )


_ZxAnCfmMepLmmDaType_Type.__name__ = "Integer32"
_ZxAnCfmMepLmmDaType_Object = MibTableColumn
zxAnCfmMepLmmDaType = _ZxAnCfmMepLmmDaType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 9),
    _ZxAnCfmMepLmmDaType_Type()
)
zxAnCfmMepLmmDaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepLmmDaType.setStatus("current")


class _ZxAnCfmMepLmEndType_Type(Integer32):
    """Custom type zxAnCfmMepLmEndType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneended", 1),
          ("twoended", 2))
    )


_ZxAnCfmMepLmEndType_Type.__name__ = "Integer32"
_ZxAnCfmMepLmEndType_Object = MibTableColumn
zxAnCfmMepLmEndType = _ZxAnCfmMepLmEndType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 10),
    _ZxAnCfmMepLmEndType_Type()
)
zxAnCfmMepLmEndType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepLmEndType.setStatus("current")


class _ZxAnCfmMepLmInterval_Type(Integer32):
    """Custom type zxAnCfmMepLmInterval based on Integer32"""
    defaultValue = 5


_ZxAnCfmMepLmInterval_Type.__name__ = "Integer32"
_ZxAnCfmMepLmInterval_Object = MibTableColumn
zxAnCfmMepLmInterval = _ZxAnCfmMepLmInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 11),
    _ZxAnCfmMepLmInterval_Type()
)
zxAnCfmMepLmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepLmInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCfmMepLmInterval.setUnits("seconds")


class _ZxAnCfmMepLmDuration_Type(Integer32):
    """Custom type zxAnCfmMepLmDuration based on Integer32"""
    defaultValue = 60


_ZxAnCfmMepLmDuration_Type.__name__ = "Integer32"
_ZxAnCfmMepLmDuration_Object = MibTableColumn
zxAnCfmMepLmDuration = _ZxAnCfmMepLmDuration_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 12),
    _ZxAnCfmMepLmDuration_Type()
)
zxAnCfmMepLmDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepLmDuration.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCfmMepLmDuration.setUnits("seconds")


class _ZxAnCfmMepLmPriority_Type(Unsigned32):
    """Custom type zxAnCfmMepLmPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnCfmMepLmPriority_Type.__name__ = "Unsigned32"
_ZxAnCfmMepLmPriority_Object = MibTableColumn
zxAnCfmMepLmPriority = _ZxAnCfmMepLmPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 13),
    _ZxAnCfmMepLmPriority_Type()
)
zxAnCfmMepLmPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepLmPriority.setStatus("current")
_ZxAnCfmMepLmFarendLoss_Type = Integer32
_ZxAnCfmMepLmFarendLoss_Object = MibTableColumn
zxAnCfmMepLmFarendLoss = _ZxAnCfmMepLmFarendLoss_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 14),
    _ZxAnCfmMepLmFarendLoss_Type()
)
zxAnCfmMepLmFarendLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCfmMepLmFarendLoss.setStatus("current")
_ZxAnCfmMepLmNearendLoss_Type = Integer32
_ZxAnCfmMepLmNearendLoss_Object = MibTableColumn
zxAnCfmMepLmNearendLoss = _ZxAnCfmMepLmNearendLoss_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 15),
    _ZxAnCfmMepLmNearendLoss_Type()
)
zxAnCfmMepLmNearendLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCfmMepLmNearendLoss.setStatus("current")


class _ZxAnCfmMepLmLossRatio_Type(Integer32):
    """Custom type zxAnCfmMepLmLossRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnCfmMepLmLossRatio_Type.__name__ = "Integer32"
_ZxAnCfmMepLmLossRatio_Object = MibTableColumn
zxAnCfmMepLmLossRatio = _ZxAnCfmMepLmLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 16),
    _ZxAnCfmMepLmLossRatio_Type()
)
zxAnCfmMepLmLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCfmMepLmLossRatio.setStatus("current")


class _ZxAnCfmMepLmStatus_Type(TruthValue):
    """Custom type zxAnCfmMepLmStatus based on TruthValue"""
    defaultValue = 2


_ZxAnCfmMepLmStatus_Type.__name__ = "TruthValue"
_ZxAnCfmMepLmStatus_Object = MibTableColumn
zxAnCfmMepLmStatus = _ZxAnCfmMepLmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 17),
    _ZxAnCfmMepLmStatus_Type()
)
zxAnCfmMepLmStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepLmStatus.setStatus("current")


class _ZxAnCfmMepLmResultOk_Type(TruthValue):
    """Custom type zxAnCfmMepLmResultOk based on TruthValue"""
    defaultValue = 1


_ZxAnCfmMepLmResultOk_Type.__name__ = "TruthValue"
_ZxAnCfmMepLmResultOk_Object = MibTableColumn
zxAnCfmMepLmResultOk = _ZxAnCfmMepLmResultOk_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 18),
    _ZxAnCfmMepLmResultOk_Type()
)
zxAnCfmMepLmResultOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCfmMepLmResultOk.setStatus("current")


class _ZxAnCfmMepLmFarendLossRatio_Type(Integer32):
    """Custom type zxAnCfmMepLmFarendLossRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnCfmMepLmFarendLossRatio_Type.__name__ = "Integer32"
_ZxAnCfmMepLmFarendLossRatio_Object = MibTableColumn
zxAnCfmMepLmFarendLossRatio = _ZxAnCfmMepLmFarendLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 19),
    _ZxAnCfmMepLmFarendLossRatio_Type()
)
zxAnCfmMepLmFarendLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCfmMepLmFarendLossRatio.setStatus("current")
_ZxAnCfmMepDmTargetMacAddress_Type = MacAddress
_ZxAnCfmMepDmTargetMacAddress_Object = MibTableColumn
zxAnCfmMepDmTargetMacAddress = _ZxAnCfmMepDmTargetMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 30),
    _ZxAnCfmMepDmTargetMacAddress_Type()
)
zxAnCfmMepDmTargetMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepDmTargetMacAddress.setStatus("current")
_ZxAnCfmMepDmTargetMepId_Type = Dot1agCfmMepIdOrZero
_ZxAnCfmMepDmTargetMepId_Object = MibTableColumn
zxAnCfmMepDmTargetMepId = _ZxAnCfmMepDmTargetMepId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 31),
    _ZxAnCfmMepDmTargetMepId_Type()
)
zxAnCfmMepDmTargetMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepDmTargetMepId.setStatus("current")
_ZxAnCfmMepDmTargetIsMepId_Type = TruthValue
_ZxAnCfmMepDmTargetIsMepId_Object = MibTableColumn
zxAnCfmMepDmTargetIsMepId = _ZxAnCfmMepDmTargetIsMepId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 32),
    _ZxAnCfmMepDmTargetIsMepId_Type()
)
zxAnCfmMepDmTargetIsMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepDmTargetIsMepId.setStatus("current")


class _ZxAnCfmMep1dmDaType_Type(Integer32):
    """Custom type zxAnCfmMep1dmDaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicastclass1", 2))
    )


_ZxAnCfmMep1dmDaType_Type.__name__ = "Integer32"
_ZxAnCfmMep1dmDaType_Object = MibTableColumn
zxAnCfmMep1dmDaType = _ZxAnCfmMep1dmDaType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 33),
    _ZxAnCfmMep1dmDaType_Type()
)
zxAnCfmMep1dmDaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMep1dmDaType.setStatus("current")


class _ZxAnCfmMepDdmDaType_Type(Integer32):
    """Custom type zxAnCfmMepDdmDaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicastclass1", 2))
    )


_ZxAnCfmMepDdmDaType_Type.__name__ = "Integer32"
_ZxAnCfmMepDdmDaType_Object = MibTableColumn
zxAnCfmMepDdmDaType = _ZxAnCfmMepDdmDaType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 34),
    _ZxAnCfmMepDdmDaType_Type()
)
zxAnCfmMepDdmDaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepDdmDaType.setStatus("current")


class _ZxAnCfmMepDmWayType_Type(Integer32):
    """Custom type zxAnCfmMepDmWayType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneway", 1),
          ("twoway", 2))
    )


_ZxAnCfmMepDmWayType_Type.__name__ = "Integer32"
_ZxAnCfmMepDmWayType_Object = MibTableColumn
zxAnCfmMepDmWayType = _ZxAnCfmMepDmWayType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 35),
    _ZxAnCfmMepDmWayType_Type()
)
zxAnCfmMepDmWayType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepDmWayType.setStatus("current")


class _ZxAnCfmMepDmInterval_Type(Integer32):
    """Custom type zxAnCfmMepDmInterval based on Integer32"""
    defaultValue = 5


_ZxAnCfmMepDmInterval_Type.__name__ = "Integer32"
_ZxAnCfmMepDmInterval_Object = MibTableColumn
zxAnCfmMepDmInterval = _ZxAnCfmMepDmInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 36),
    _ZxAnCfmMepDmInterval_Type()
)
zxAnCfmMepDmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepDmInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCfmMepDmInterval.setUnits("seconds")


class _ZxAnCfmMepDmDuration_Type(Integer32):
    """Custom type zxAnCfmMepDmDuration based on Integer32"""
    defaultValue = 60


_ZxAnCfmMepDmDuration_Type.__name__ = "Integer32"
_ZxAnCfmMepDmDuration_Object = MibTableColumn
zxAnCfmMepDmDuration = _ZxAnCfmMepDmDuration_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 37),
    _ZxAnCfmMepDmDuration_Type()
)
zxAnCfmMepDmDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepDmDuration.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCfmMepDmDuration.setUnits("seconds")


class _ZxAnCfmMepDmPriority_Type(Unsigned32):
    """Custom type zxAnCfmMepDmPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnCfmMepDmPriority_Type.__name__ = "Unsigned32"
_ZxAnCfmMepDmPriority_Object = MibTableColumn
zxAnCfmMepDmPriority = _ZxAnCfmMepDmPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 38),
    _ZxAnCfmMepDmPriority_Type()
)
zxAnCfmMepDmPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepDmPriority.setStatus("current")
_ZxAnCfmMepDmOneWayAvgDelay_Type = Counter64
_ZxAnCfmMepDmOneWayAvgDelay_Object = MibTableColumn
zxAnCfmMepDmOneWayAvgDelay = _ZxAnCfmMepDmOneWayAvgDelay_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 39),
    _ZxAnCfmMepDmOneWayAvgDelay_Type()
)
zxAnCfmMepDmOneWayAvgDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCfmMepDmOneWayAvgDelay.setStatus("current")
_ZxAnCfmMepDmOneWayAvgDv_Type = Counter64
_ZxAnCfmMepDmOneWayAvgDv_Object = MibTableColumn
zxAnCfmMepDmOneWayAvgDv = _ZxAnCfmMepDmOneWayAvgDv_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 40),
    _ZxAnCfmMepDmOneWayAvgDv_Type()
)
zxAnCfmMepDmOneWayAvgDv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCfmMepDmOneWayAvgDv.setStatus("current")
_ZxAnCfmMepDmTwoWayAvgDelay_Type = Counter64
_ZxAnCfmMepDmTwoWayAvgDelay_Object = MibTableColumn
zxAnCfmMepDmTwoWayAvgDelay = _ZxAnCfmMepDmTwoWayAvgDelay_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 41),
    _ZxAnCfmMepDmTwoWayAvgDelay_Type()
)
zxAnCfmMepDmTwoWayAvgDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCfmMepDmTwoWayAvgDelay.setStatus("current")
_ZxAnCfmMepDmTwoWayAvgDv_Type = Counter64
_ZxAnCfmMepDmTwoWayAvgDv_Object = MibTableColumn
zxAnCfmMepDmTwoWayAvgDv = _ZxAnCfmMepDmTwoWayAvgDv_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 42),
    _ZxAnCfmMepDmTwoWayAvgDv_Type()
)
zxAnCfmMepDmTwoWayAvgDv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCfmMepDmTwoWayAvgDv.setStatus("current")


class _ZxAnCfmMepDmStatus_Type(TruthValue):
    """Custom type zxAnCfmMepDmStatus based on TruthValue"""
    defaultValue = 2


_ZxAnCfmMepDmStatus_Type.__name__ = "TruthValue"
_ZxAnCfmMepDmStatus_Object = MibTableColumn
zxAnCfmMepDmStatus = _ZxAnCfmMepDmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 43),
    _ZxAnCfmMepDmStatus_Type()
)
zxAnCfmMepDmStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepDmStatus.setStatus("current")


class _ZxAnCfmMepDmResultOk_Type(TruthValue):
    """Custom type zxAnCfmMepDmResultOk based on TruthValue"""
    defaultValue = 1


_ZxAnCfmMepDmResultOk_Type.__name__ = "TruthValue"
_ZxAnCfmMepDmResultOk_Object = MibTableColumn
zxAnCfmMepDmResultOk = _ZxAnCfmMepDmResultOk_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 44),
    _ZxAnCfmMepDmResultOk_Type()
)
zxAnCfmMepDmResultOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCfmMepDmResultOk.setStatus("current")


class _ZxAnCfmMepTestTlvLength_Type(Unsigned32):
    """Custom type zxAnCfmMepTestTlvLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_ZxAnCfmMepTestTlvLength_Type.__name__ = "Unsigned32"
_ZxAnCfmMepTestTlvLength_Object = MibTableColumn
zxAnCfmMepTestTlvLength = _ZxAnCfmMepTestTlvLength_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 54),
    _ZxAnCfmMepTestTlvLength_Type()
)
zxAnCfmMepTestTlvLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepTestTlvLength.setStatus("current")


class _ZxAnCfmMepTestEnable_Type(Integer32):
    """Custom type zxAnCfmMepTestEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnCfmMepTestEnable_Type.__name__ = "Integer32"
_ZxAnCfmMepTestEnable_Object = MibTableColumn
zxAnCfmMepTestEnable = _ZxAnCfmMepTestEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 55),
    _ZxAnCfmMepTestEnable_Type()
)
zxAnCfmMepTestEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepTestEnable.setStatus("current")


class _ZxAnCfmMepTestAppType_Type(Integer32):
    """Custom type zxAnCfmMepTestAppType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inServiceDiagnostic", 1),
          ("outOfServiceDiagnostic", 2))
    )


_ZxAnCfmMepTestAppType_Type.__name__ = "Integer32"
_ZxAnCfmMepTestAppType_Object = MibTableColumn
zxAnCfmMepTestAppType = _ZxAnCfmMepTestAppType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 56),
    _ZxAnCfmMepTestAppType_Type()
)
zxAnCfmMepTestAppType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepTestAppType.setStatus("current")
_ZxAnCfmMepTestDestMacAddress_Type = MacAddress
_ZxAnCfmMepTestDestMacAddress_Object = MibTableColumn
zxAnCfmMepTestDestMacAddress = _ZxAnCfmMepTestDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 57),
    _ZxAnCfmMepTestDestMacAddress_Type()
)
zxAnCfmMepTestDestMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepTestDestMacAddress.setStatus("current")
_ZxAnCfmMepTestDestMepId_Type = Dot1agCfmMepIdOrZero
_ZxAnCfmMepTestDestMepId_Object = MibTableColumn
zxAnCfmMepTestDestMepId = _ZxAnCfmMepTestDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 58),
    _ZxAnCfmMepTestDestMepId_Type()
)
zxAnCfmMepTestDestMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepTestDestMepId.setStatus("current")
_ZxAnCfmMepTestDestIsMepId_Type = TruthValue
_ZxAnCfmMepTestDestIsMepId_Object = MibTableColumn
zxAnCfmMepTestDestIsMepId = _ZxAnCfmMepTestDestIsMepId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 59),
    _ZxAnCfmMepTestDestIsMepId_Type()
)
zxAnCfmMepTestDestIsMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepTestDestIsMepId.setStatus("current")


class _ZxAnCfmMepTestInterval_Type(Integer32):
    """Custom type zxAnCfmMepTestInterval based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_ZxAnCfmMepTestInterval_Type.__name__ = "Integer32"
_ZxAnCfmMepTestInterval_Object = MibTableColumn
zxAnCfmMepTestInterval = _ZxAnCfmMepTestInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 60),
    _ZxAnCfmMepTestInterval_Type()
)
zxAnCfmMepTestInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepTestInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCfmMepTestInterval.setUnits("milliseconds")


class _ZxAnCfmMepTestDuration_Type(Integer32):
    """Custom type zxAnCfmMepTestDuration based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_ZxAnCfmMepTestDuration_Type.__name__ = "Integer32"
_ZxAnCfmMepTestDuration_Object = MibTableColumn
zxAnCfmMepTestDuration = _ZxAnCfmMepTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 61),
    _ZxAnCfmMepTestDuration_Type()
)
zxAnCfmMepTestDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepTestDuration.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCfmMepTestDuration.setUnits("seconds")


class _ZxAnCfmMepTestPriority_Type(Unsigned32):
    """Custom type zxAnCfmMepTestPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnCfmMepTestPriority_Type.__name__ = "Unsigned32"
_ZxAnCfmMepTestPriority_Object = MibTableColumn
zxAnCfmMepTestPriority = _ZxAnCfmMepTestPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 62),
    _ZxAnCfmMepTestPriority_Type()
)
zxAnCfmMepTestPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepTestPriority.setStatus("current")


class _ZxAnCfmMepTestDaType_Type(Integer32):
    """Custom type zxAnCfmMepTestDaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicastClass1", 2))
    )


_ZxAnCfmMepTestDaType_Type.__name__ = "Integer32"
_ZxAnCfmMepTestDaType_Object = MibTableColumn
zxAnCfmMepTestDaType = _ZxAnCfmMepTestDaType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 63),
    _ZxAnCfmMepTestDaType_Type()
)
zxAnCfmMepTestDaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepTestDaType.setStatus("current")


class _ZxAnCfmMepTestTlvEnable_Type(Integer32):
    """Custom type zxAnCfmMepTestTlvEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnCfmMepTestTlvEnable_Type.__name__ = "Integer32"
_ZxAnCfmMepTestTlvEnable_Object = MibTableColumn
zxAnCfmMepTestTlvEnable = _ZxAnCfmMepTestTlvEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 64),
    _ZxAnCfmMepTestTlvEnable_Type()
)
zxAnCfmMepTestTlvEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepTestTlvEnable.setStatus("current")


class _ZxAnCfmMepTestPattern_Type(Integer32):
    """Custom type zxAnCfmMepTestPattern based on Integer32"""
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
        *(("allZeroesWithoutCrc32", 1),
          ("allZeroesWithCrc32", 2),
          ("prbsWithoutCrc32", 3),
          ("prbsWithCrc32", 4))
    )


_ZxAnCfmMepTestPattern_Type.__name__ = "Integer32"
_ZxAnCfmMepTestPattern_Object = MibTableColumn
zxAnCfmMepTestPattern = _ZxAnCfmMepTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 65),
    _ZxAnCfmMepTestPattern_Type()
)
zxAnCfmMepTestPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepTestPattern.setStatus("current")


class _ZxAnCfmMepTestStatus_Type(TruthValue):
    """Custom type zxAnCfmMepTestStatus based on TruthValue"""
    defaultValue = 2


_ZxAnCfmMepTestStatus_Type.__name__ = "TruthValue"
_ZxAnCfmMepTestStatus_Object = MibTableColumn
zxAnCfmMepTestStatus = _ZxAnCfmMepTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 66),
    _ZxAnCfmMepTestStatus_Type()
)
zxAnCfmMepTestStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepTestStatus.setStatus("current")


class _ZxAnCfmMepTestResultOk_Type(TruthValue):
    """Custom type zxAnCfmMepTestResultOk based on TruthValue"""
    defaultValue = 1


_ZxAnCfmMepTestResultOk_Type.__name__ = "TruthValue"
_ZxAnCfmMepTestResultOk_Object = MibTableColumn
zxAnCfmMepTestResultOk = _ZxAnCfmMepTestResultOk_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 67),
    _ZxAnCfmMepTestResultOk_Type()
)
zxAnCfmMepTestResultOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCfmMepTestResultOk.setStatus("current")
_ZxAnCfmMepTestMsgSeqNumber_Type = Unsigned32
_ZxAnCfmMepTestMsgSeqNumber_Object = MibTableColumn
zxAnCfmMepTestMsgSeqNumber = _ZxAnCfmMepTestMsgSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 68),
    _ZxAnCfmMepTestMsgSeqNumber_Type()
)
zxAnCfmMepTestMsgSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCfmMepTestMsgSeqNumber.setStatus("current")
_ZxAnCfmMepTestNextMsgSeqNumber_Type = Unsigned32
_ZxAnCfmMepTestNextMsgSeqNumber_Object = MibTableColumn
zxAnCfmMepTestNextMsgSeqNumber = _ZxAnCfmMepTestNextMsgSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 69),
    _ZxAnCfmMepTestNextMsgSeqNumber_Type()
)
zxAnCfmMepTestNextMsgSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCfmMepTestNextMsgSeqNumber.setStatus("current")


class _ZxAnCfmMepTestTransmitRate_Type(Unsigned32):
    """Custom type zxAnCfmMepTestTransmitRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ZxAnCfmMepTestTransmitRate_Type.__name__ = "Unsigned32"
_ZxAnCfmMepTestTransmitRate_Object = MibTableColumn
zxAnCfmMepTestTransmitRate = _ZxAnCfmMepTestTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 70),
    _ZxAnCfmMepTestTransmitRate_Type()
)
zxAnCfmMepTestTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCfmMepTestTransmitRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCfmMepTestTransmitRate.setUnits("kbps")


class _ZxAnCfmMepTestFarendLossRatio_Type(Integer32):
    """Custom type zxAnCfmMepTestFarendLossRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnCfmMepTestFarendLossRatio_Type.__name__ = "Integer32"
_ZxAnCfmMepTestFarendLossRatio_Object = MibTableColumn
zxAnCfmMepTestFarendLossRatio = _ZxAnCfmMepTestFarendLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 71),
    _ZxAnCfmMepTestFarendLossRatio_Type()
)
zxAnCfmMepTestFarendLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCfmMepTestFarendLossRatio.setStatus("current")


class _ZxAnCfmMepTestFarendBitErrRatio_Type(Integer32):
    """Custom type zxAnCfmMepTestFarendBitErrRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnCfmMepTestFarendBitErrRatio_Type.__name__ = "Integer32"
_ZxAnCfmMepTestFarendBitErrRatio_Object = MibTableColumn
zxAnCfmMepTestFarendBitErrRatio = _ZxAnCfmMepTestFarendBitErrRatio_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 72),
    _ZxAnCfmMepTestFarendBitErrRatio_Type()
)
zxAnCfmMepTestFarendBitErrRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCfmMepTestFarendBitErrRatio.setStatus("current")


class _ZxAnCfmMepAisEnable_Type(Integer32):
    """Custom type zxAnCfmMepAisEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnCfmMepAisEnable_Type.__name__ = "Integer32"
_ZxAnCfmMepAisEnable_Object = MibTableColumn
zxAnCfmMepAisEnable = _ZxAnCfmMepAisEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 87),
    _ZxAnCfmMepAisEnable_Type()
)
zxAnCfmMepAisEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepAisEnable.setStatus("current")


class _ZxAnCfmMepLckEnable_Type(Integer32):
    """Custom type zxAnCfmMepLckEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnCfmMepLckEnable_Type.__name__ = "Integer32"
_ZxAnCfmMepLckEnable_Object = MibTableColumn
zxAnCfmMepLckEnable = _ZxAnCfmMepLckEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 88),
    _ZxAnCfmMepLckEnable_Type()
)
zxAnCfmMepLckEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepLckEnable.setStatus("current")


class _ZxAnCfmMepAisClientMegLevel_Type(Integer32):
    """Custom type zxAnCfmMepAisClientMegLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnCfmMepAisClientMegLevel_Type.__name__ = "Integer32"
_ZxAnCfmMepAisClientMegLevel_Object = MibTableColumn
zxAnCfmMepAisClientMegLevel = _ZxAnCfmMepAisClientMegLevel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 89),
    _ZxAnCfmMepAisClientMegLevel_Type()
)
zxAnCfmMepAisClientMegLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepAisClientMegLevel.setStatus("current")


class _ZxAnCfmMepLckClientMegLevel_Type(Integer32):
    """Custom type zxAnCfmMepLckClientMegLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnCfmMepLckClientMegLevel_Type.__name__ = "Integer32"
_ZxAnCfmMepLckClientMegLevel_Object = MibTableColumn
zxAnCfmMepLckClientMegLevel = _ZxAnCfmMepLckClientMegLevel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 90),
    _ZxAnCfmMepLckClientMegLevel_Type()
)
zxAnCfmMepLckClientMegLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepLckClientMegLevel.setStatus("current")


class _ZxAnCfmMepAisLckInterval_Type(Integer32):
    """Custom type zxAnCfmMepAisLckInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_ZxAnCfmMepAisLckInterval_Type.__name__ = "Integer32"
_ZxAnCfmMepAisLckInterval_Object = MibTableColumn
zxAnCfmMepAisLckInterval = _ZxAnCfmMepAisLckInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 91),
    _ZxAnCfmMepAisLckInterval_Type()
)
zxAnCfmMepAisLckInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepAisLckInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCfmMepAisLckInterval.setUnits("seconds")


class _ZxAnCfmMepAisPriority_Type(Unsigned32):
    """Custom type zxAnCfmMepAisPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnCfmMepAisPriority_Type.__name__ = "Unsigned32"
_ZxAnCfmMepAisPriority_Object = MibTableColumn
zxAnCfmMepAisPriority = _ZxAnCfmMepAisPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 92),
    _ZxAnCfmMepAisPriority_Type()
)
zxAnCfmMepAisPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepAisPriority.setStatus("current")


class _ZxAnCfmMepLckPriority_Type(Unsigned32):
    """Custom type zxAnCfmMepLckPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnCfmMepLckPriority_Type.__name__ = "Unsigned32"
_ZxAnCfmMepLckPriority_Object = MibTableColumn
zxAnCfmMepLckPriority = _ZxAnCfmMepLckPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 93),
    _ZxAnCfmMepLckPriority_Type()
)
zxAnCfmMepLckPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepLckPriority.setStatus("current")


class _ZxAnCfmMepAisDaType_Type(Integer32):
    """Custom type zxAnCfmMepAisDaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicastClass1", 2))
    )


_ZxAnCfmMepAisDaType_Type.__name__ = "Integer32"
_ZxAnCfmMepAisDaType_Object = MibTableColumn
zxAnCfmMepAisDaType = _ZxAnCfmMepAisDaType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 94),
    _ZxAnCfmMepAisDaType_Type()
)
zxAnCfmMepAisDaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepAisDaType.setStatus("current")


class _ZxAnCfmMepLckDaType_Type(Integer32):
    """Custom type zxAnCfmMepLckDaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicastClass1", 2))
    )


_ZxAnCfmMepLckDaType_Type.__name__ = "Integer32"
_ZxAnCfmMepLckDaType_Object = MibTableColumn
zxAnCfmMepLckDaType = _ZxAnCfmMepLckDaType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 95),
    _ZxAnCfmMepLckDaType_Type()
)
zxAnCfmMepLckDaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepLckDaType.setStatus("current")
_ZxAnCfmMepAisStatus_Type = TruthValue
_ZxAnCfmMepAisStatus_Object = MibTableColumn
zxAnCfmMepAisStatus = _ZxAnCfmMepAisStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 96),
    _ZxAnCfmMepAisStatus_Type()
)
zxAnCfmMepAisStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCfmMepAisStatus.setStatus("current")
_ZxAnCfmMepLckStatus_Type = TruthValue
_ZxAnCfmMepLckStatus_Object = MibTableColumn
zxAnCfmMepLckStatus = _ZxAnCfmMepLckStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 97),
    _ZxAnCfmMepLckStatus_Type()
)
zxAnCfmMepLckStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCfmMepLckStatus.setStatus("current")
_ZxAnCfmMepLckSendEnable_Type = TruthValue
_ZxAnCfmMepLckSendEnable_Object = MibTableColumn
zxAnCfmMepLckSendEnable = _ZxAnCfmMepLckSendEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 98),
    _ZxAnCfmMepLckSendEnable_Type()
)
zxAnCfmMepLckSendEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMepLckSendEnable.setStatus("current")
_ZxAnCfmMepRdiStatus_Type = TruthValue
_ZxAnCfmMepRdiStatus_Object = MibTableColumn
zxAnCfmMepRdiStatus = _ZxAnCfmMepRdiStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 1, 1, 99),
    _ZxAnCfmMepRdiStatus_Type()
)
zxAnCfmMepRdiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCfmMepRdiStatus.setStatus("current")
_ZxAnCfmRemoteMepConfTable_Object = MibTable
zxAnCfmRemoteMepConfTable = _ZxAnCfmRemoteMepConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 2)
)
if mibBuilder.loadTexts:
    zxAnCfmRemoteMepConfTable.setStatus("current")
_ZxAnCfmRemoteMepConfEntry_Object = MibTableRow
zxAnCfmRemoteMepConfEntry = _ZxAnCfmRemoteMepConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 2, 1)
)
zxAnCfmRemoteMepConfEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
)
if mibBuilder.loadTexts:
    zxAnCfmRemoteMepConfEntry.setStatus("current")
_ZxAnCfmRemoteMepMacAddress_Type = MacAddress
_ZxAnCfmRemoteMepMacAddress_Object = MibTableColumn
zxAnCfmRemoteMepMacAddress = _ZxAnCfmRemoteMepMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 2, 1, 1),
    _ZxAnCfmRemoteMepMacAddress_Type()
)
zxAnCfmRemoteMepMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmRemoteMepMacAddress.setStatus("current")
_ZxAnCfmRemoteMepConfRowStatus_Type = RowStatus
_ZxAnCfmRemoteMepConfRowStatus_Object = MibTableColumn
zxAnCfmRemoteMepConfRowStatus = _ZxAnCfmRemoteMepConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 2, 1, 20),
    _ZxAnCfmRemoteMepConfRowStatus_Type()
)
zxAnCfmRemoteMepConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmRemoteMepConfRowStatus.setStatus("current")
_ZxAnCfmMipTable_Object = MibTable
zxAnCfmMipTable = _ZxAnCfmMipTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 3)
)
if mibBuilder.loadTexts:
    zxAnCfmMipTable.setStatus("current")
_ZxAnCfmMipEntry_Object = MibTableRow
zxAnCfmMipEntry = _ZxAnCfmMipEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 3, 1)
)
zxAnCfmMipEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
)
if mibBuilder.loadTexts:
    zxAnCfmMipEntry.setStatus("current")
_ZxAnCfmMipIfIndex_Type = InterfaceIndexOrZero
_ZxAnCfmMipIfIndex_Object = MibTableColumn
zxAnCfmMipIfIndex = _ZxAnCfmMipIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 3, 1, 1),
    _ZxAnCfmMipIfIndex_Type()
)
zxAnCfmMipIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMipIfIndex.setStatus("current")
_ZxAnCfmMipRowStatus_Type = RowStatus
_ZxAnCfmMipRowStatus_Object = MibTableColumn
zxAnCfmMipRowStatus = _ZxAnCfmMipRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 3, 3, 1, 20),
    _ZxAnCfmMipRowStatus_Type()
)
zxAnCfmMipRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCfmMipRowStatus.setStatus("current")
_ZxAnCfmCompatibleObjects_ObjectIdentity = ObjectIdentity
zxAnCfmCompatibleObjects = _ZxAnCfmCompatibleObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 4)
)


class _ZxAnCfmCompatible_Type(OctetString):
    """Custom type zxAnCfmCompatible based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_ZxAnCfmCompatible_Type.__name__ = "OctetString"
_ZxAnCfmCompatible_Object = MibScalar
zxAnCfmCompatible = _ZxAnCfmCompatible_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 4, 1),
    _ZxAnCfmCompatible_Type()
)
zxAnCfmCompatible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCfmCompatible.setStatus("current")
_ZxAnCfmInterfaceObjects_ObjectIdentity = ObjectIdentity
zxAnCfmInterfaceObjects = _ZxAnCfmInterfaceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 5)
)
_ZxAnCfmIfTable_Object = MibTable
zxAnCfmIfTable = _ZxAnCfmIfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 5, 1)
)
if mibBuilder.loadTexts:
    zxAnCfmIfTable.setStatus("current")
_ZxAnCfmIfEntry_Object = MibTableRow
zxAnCfmIfEntry = _ZxAnCfmIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 5, 1, 1)
)
zxAnCfmIfEntry.setIndexNames(
    (0, "ZTE-AN-CFM-MIB", "zxAnCfmRack"),
    (0, "ZTE-AN-CFM-MIB", "zxAnCfmShelf"),
    (0, "ZTE-AN-CFM-MIB", "zxAnCfmSlot"),
    (0, "ZTE-AN-CFM-MIB", "zxAnCfmPort"),
    (0, "ZTE-AN-CFM-MIB", "zxAnCfmOnu"),
    (0, "ZTE-AN-CFM-MIB", "zxAnCfmIfType"),
    (0, "ZTE-AN-CFM-MIB", "zxAnCfmLogicalId"),
)
if mibBuilder.loadTexts:
    zxAnCfmIfEntry.setStatus("current")
_ZxAnCfmRack_Type = Integer32
_ZxAnCfmRack_Object = MibTableColumn
zxAnCfmRack = _ZxAnCfmRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 5, 1, 1, 1),
    _ZxAnCfmRack_Type()
)
zxAnCfmRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnCfmRack.setStatus("current")
_ZxAnCfmShelf_Type = Integer32
_ZxAnCfmShelf_Object = MibTableColumn
zxAnCfmShelf = _ZxAnCfmShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 5, 1, 1, 2),
    _ZxAnCfmShelf_Type()
)
zxAnCfmShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnCfmShelf.setStatus("current")
_ZxAnCfmSlot_Type = Integer32
_ZxAnCfmSlot_Object = MibTableColumn
zxAnCfmSlot = _ZxAnCfmSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 5, 1, 1, 3),
    _ZxAnCfmSlot_Type()
)
zxAnCfmSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnCfmSlot.setStatus("current")
_ZxAnCfmPort_Type = Integer32
_ZxAnCfmPort_Object = MibTableColumn
zxAnCfmPort = _ZxAnCfmPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 5, 1, 1, 4),
    _ZxAnCfmPort_Type()
)
zxAnCfmPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnCfmPort.setStatus("current")
_ZxAnCfmOnu_Type = Integer32
_ZxAnCfmOnu_Object = MibTableColumn
zxAnCfmOnu = _ZxAnCfmOnu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 5, 1, 1, 5),
    _ZxAnCfmOnu_Type()
)
zxAnCfmOnu.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnCfmOnu.setStatus("current")


class _ZxAnCfmIfType_Type(Integer32):
    """Custom type zxAnCfmIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5)
        )
    )
    namedValues = NamedValues(
        *(("physicalPort", 1),
          ("onuUni", 5))
    )


_ZxAnCfmIfType_Type.__name__ = "Integer32"
_ZxAnCfmIfType_Object = MibTableColumn
zxAnCfmIfType = _ZxAnCfmIfType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 5, 1, 1, 6),
    _ZxAnCfmIfType_Type()
)
zxAnCfmIfType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnCfmIfType.setStatus("current")
_ZxAnCfmLogicalId_Type = ObjectIdentifier
_ZxAnCfmLogicalId_Object = MibTableColumn
zxAnCfmLogicalId = _ZxAnCfmLogicalId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 5, 1, 1, 7),
    _ZxAnCfmLogicalId_Type()
)
zxAnCfmLogicalId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnCfmLogicalId.setStatus("current")


class _ZxAnCfmIfOamPduFilterEnable_Type(Integer32):
    """Custom type zxAnCfmIfOamPduFilterEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnCfmIfOamPduFilterEnable_Type.__name__ = "Integer32"
_ZxAnCfmIfOamPduFilterEnable_Object = MibTableColumn
zxAnCfmIfOamPduFilterEnable = _ZxAnCfmIfOamPduFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 1, 5, 1, 1, 8),
    _ZxAnCfmIfOamPduFilterEnable_Type()
)
zxAnCfmIfOamPduFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnCfmIfOamPduFilterEnable.setStatus("current")
_ZxAnCfmTrapObjects_ObjectIdentity = ObjectIdentity
zxAnCfmTrapObjects = _ZxAnCfmTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 62, 2)
)
dot1agCfmMaNetEntry.registerAugmentions(
    ("ZTE-AN-CFM-MIB",
     "zxAnCfmMaNetEntry")
)
zxAnCfmMaNetEntry.setIndexNames(*dot1agCfmMaNetEntry.getIndexNames())
dot1agCfmMepEntry.registerAugmentions(
    ("ZTE-AN-CFM-MIB",
     "zxAnCfmMepEntry")
)
zxAnCfmMepEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-CFM-MIB",
    **{"zxAnCfmMib": zxAnCfmMib,
       "zxAnCfmObjects": zxAnCfmObjects,
       "zxAnCfmGlobalObjects": zxAnCfmGlobalObjects,
       "zxAnCfmEnable": zxAnCfmEnable,
       "zxAnCfmMa": zxAnCfmMa,
       "zxAnCfmMaNetTable": zxAnCfmMaNetTable,
       "zxAnCfmMaNetEntry": zxAnCfmMaNetEntry,
       "zxAnCfmMaNetCcmDaType": zxAnCfmMaNetCcmDaType,
       "zxAnCfmMaProtect": zxAnCfmMaProtect,
       "zxAnCfmMaTunnel": zxAnCfmMaTunnel,
       "zxAnCfmMep": zxAnCfmMep,
       "zxAnCfmMepTable": zxAnCfmMepTable,
       "zxAnCfmMepEntry": zxAnCfmMepEntry,
       "zxAnCfmMepCcCheckEnable": zxAnCfmMepCcCheckEnable,
       "zxAnCfmMepLmEnable": zxAnCfmMepLmEnable,
       "zxAnCfmMepDmEnable": zxAnCfmMepDmEnable,
       "zxAnCfmMepLbmTestType": zxAnCfmMepLbmTestType,
       "zxAnCfmMepLbmAppType": zxAnCfmMepLbmAppType,
       "zxAnCfmMepLmTargetMacAddress": zxAnCfmMepLmTargetMacAddress,
       "zxAnCfmMepLmTargetMepId": zxAnCfmMepLmTargetMepId,
       "zxAnCfmMepLmTargetIsMepId": zxAnCfmMepLmTargetIsMepId,
       "zxAnCfmMepLmmDaType": zxAnCfmMepLmmDaType,
       "zxAnCfmMepLmEndType": zxAnCfmMepLmEndType,
       "zxAnCfmMepLmInterval": zxAnCfmMepLmInterval,
       "zxAnCfmMepLmDuration": zxAnCfmMepLmDuration,
       "zxAnCfmMepLmPriority": zxAnCfmMepLmPriority,
       "zxAnCfmMepLmFarendLoss": zxAnCfmMepLmFarendLoss,
       "zxAnCfmMepLmNearendLoss": zxAnCfmMepLmNearendLoss,
       "zxAnCfmMepLmLossRatio": zxAnCfmMepLmLossRatio,
       "zxAnCfmMepLmStatus": zxAnCfmMepLmStatus,
       "zxAnCfmMepLmResultOk": zxAnCfmMepLmResultOk,
       "zxAnCfmMepLmFarendLossRatio": zxAnCfmMepLmFarendLossRatio,
       "zxAnCfmMepDmTargetMacAddress": zxAnCfmMepDmTargetMacAddress,
       "zxAnCfmMepDmTargetMepId": zxAnCfmMepDmTargetMepId,
       "zxAnCfmMepDmTargetIsMepId": zxAnCfmMepDmTargetIsMepId,
       "zxAnCfmMep1dmDaType": zxAnCfmMep1dmDaType,
       "zxAnCfmMepDdmDaType": zxAnCfmMepDdmDaType,
       "zxAnCfmMepDmWayType": zxAnCfmMepDmWayType,
       "zxAnCfmMepDmInterval": zxAnCfmMepDmInterval,
       "zxAnCfmMepDmDuration": zxAnCfmMepDmDuration,
       "zxAnCfmMepDmPriority": zxAnCfmMepDmPriority,
       "zxAnCfmMepDmOneWayAvgDelay": zxAnCfmMepDmOneWayAvgDelay,
       "zxAnCfmMepDmOneWayAvgDv": zxAnCfmMepDmOneWayAvgDv,
       "zxAnCfmMepDmTwoWayAvgDelay": zxAnCfmMepDmTwoWayAvgDelay,
       "zxAnCfmMepDmTwoWayAvgDv": zxAnCfmMepDmTwoWayAvgDv,
       "zxAnCfmMepDmStatus": zxAnCfmMepDmStatus,
       "zxAnCfmMepDmResultOk": zxAnCfmMepDmResultOk,
       "zxAnCfmMepTestTlvLength": zxAnCfmMepTestTlvLength,
       "zxAnCfmMepTestEnable": zxAnCfmMepTestEnable,
       "zxAnCfmMepTestAppType": zxAnCfmMepTestAppType,
       "zxAnCfmMepTestDestMacAddress": zxAnCfmMepTestDestMacAddress,
       "zxAnCfmMepTestDestMepId": zxAnCfmMepTestDestMepId,
       "zxAnCfmMepTestDestIsMepId": zxAnCfmMepTestDestIsMepId,
       "zxAnCfmMepTestInterval": zxAnCfmMepTestInterval,
       "zxAnCfmMepTestDuration": zxAnCfmMepTestDuration,
       "zxAnCfmMepTestPriority": zxAnCfmMepTestPriority,
       "zxAnCfmMepTestDaType": zxAnCfmMepTestDaType,
       "zxAnCfmMepTestTlvEnable": zxAnCfmMepTestTlvEnable,
       "zxAnCfmMepTestPattern": zxAnCfmMepTestPattern,
       "zxAnCfmMepTestStatus": zxAnCfmMepTestStatus,
       "zxAnCfmMepTestResultOk": zxAnCfmMepTestResultOk,
       "zxAnCfmMepTestMsgSeqNumber": zxAnCfmMepTestMsgSeqNumber,
       "zxAnCfmMepTestNextMsgSeqNumber": zxAnCfmMepTestNextMsgSeqNumber,
       "zxAnCfmMepTestTransmitRate": zxAnCfmMepTestTransmitRate,
       "zxAnCfmMepTestFarendLossRatio": zxAnCfmMepTestFarendLossRatio,
       "zxAnCfmMepTestFarendBitErrRatio": zxAnCfmMepTestFarendBitErrRatio,
       "zxAnCfmMepAisEnable": zxAnCfmMepAisEnable,
       "zxAnCfmMepLckEnable": zxAnCfmMepLckEnable,
       "zxAnCfmMepAisClientMegLevel": zxAnCfmMepAisClientMegLevel,
       "zxAnCfmMepLckClientMegLevel": zxAnCfmMepLckClientMegLevel,
       "zxAnCfmMepAisLckInterval": zxAnCfmMepAisLckInterval,
       "zxAnCfmMepAisPriority": zxAnCfmMepAisPriority,
       "zxAnCfmMepLckPriority": zxAnCfmMepLckPriority,
       "zxAnCfmMepAisDaType": zxAnCfmMepAisDaType,
       "zxAnCfmMepLckDaType": zxAnCfmMepLckDaType,
       "zxAnCfmMepAisStatus": zxAnCfmMepAisStatus,
       "zxAnCfmMepLckStatus": zxAnCfmMepLckStatus,
       "zxAnCfmMepLckSendEnable": zxAnCfmMepLckSendEnable,
       "zxAnCfmMepRdiStatus": zxAnCfmMepRdiStatus,
       "zxAnCfmRemoteMepConfTable": zxAnCfmRemoteMepConfTable,
       "zxAnCfmRemoteMepConfEntry": zxAnCfmRemoteMepConfEntry,
       "zxAnCfmRemoteMepMacAddress": zxAnCfmRemoteMepMacAddress,
       "zxAnCfmRemoteMepConfRowStatus": zxAnCfmRemoteMepConfRowStatus,
       "zxAnCfmMipTable": zxAnCfmMipTable,
       "zxAnCfmMipEntry": zxAnCfmMipEntry,
       "zxAnCfmMipIfIndex": zxAnCfmMipIfIndex,
       "zxAnCfmMipRowStatus": zxAnCfmMipRowStatus,
       "zxAnCfmCompatibleObjects": zxAnCfmCompatibleObjects,
       "zxAnCfmCompatible": zxAnCfmCompatible,
       "zxAnCfmInterfaceObjects": zxAnCfmInterfaceObjects,
       "zxAnCfmIfTable": zxAnCfmIfTable,
       "zxAnCfmIfEntry": zxAnCfmIfEntry,
       "zxAnCfmRack": zxAnCfmRack,
       "zxAnCfmShelf": zxAnCfmShelf,
       "zxAnCfmSlot": zxAnCfmSlot,
       "zxAnCfmPort": zxAnCfmPort,
       "zxAnCfmOnu": zxAnCfmOnu,
       "zxAnCfmIfType": zxAnCfmIfType,
       "zxAnCfmLogicalId": zxAnCfmLogicalId,
       "zxAnCfmIfOamPduFilterEnable": zxAnCfmIfOamPduFilterEnable,
       "zxAnCfmTrapObjects": zxAnCfmTrapObjects}
)
