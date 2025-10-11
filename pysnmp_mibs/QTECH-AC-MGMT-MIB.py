# SNMP MIB module (QTECH-AC-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-AC-MGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:02 2025
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

(capwapBaseNtfAuthenMethod,
 capwapBaseNtfChannelDownReason,
 capwapBaseNtfChannelType) = mibBuilder.importSymbols(
    "CAPWAP-BASE-MIB",
    "capwapBaseNtfAuthenMethod",
    "capwapBaseNtfChannelDownReason",
    "capwapBaseNtfChannelType")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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


# MODULE-IDENTITY

qtechAcMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56)
)
if mibBuilder.loadTexts:
    qtechAcMgmtMIB.setRevisions(
        ("2009-09-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechAcMgmtAcMIBObjects_ObjectIdentity = ObjectIdentity
qtechAcMgmtAcMIBObjects = _QtechAcMgmtAcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1)
)
_QtechAcMgmtAc_ObjectIdentity = ObjectIdentity
qtechAcMgmtAc = _QtechAcMgmtAc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1)
)


class _QtechAcStaLimit_Type(Integer32):
    """Custom type qtechAcStaLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QtechAcStaLimit_Type.__name__ = "Integer32"
_QtechAcStaLimit_Object = MibScalar
qtechAcStaLimit = _QtechAcStaLimit_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 1),
    _QtechAcStaLimit_Type()
)
qtechAcStaLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcStaLimit.setStatus("current")


class _QtechAcWtpLimit_Type(Integer32):
    """Custom type qtechAcWtpLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QtechAcWtpLimit_Type.__name__ = "Integer32"
_QtechAcWtpLimit_Object = MibScalar
qtechAcWtpLimit = _QtechAcWtpLimit_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 2),
    _QtechAcWtpLimit_Type()
)
qtechAcWtpLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcWtpLimit.setStatus("current")


class _QtechAcRMacField_Type(Integer32):
    """Custom type qtechAcRMacField based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechAcRMacField_Type.__name__ = "Integer32"
_QtechAcRMacField_Object = MibScalar
qtechAcRMacField = _QtechAcRMacField_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 3),
    _QtechAcRMacField_Type()
)
qtechAcRMacField.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcRMacField.setStatus("current")


class _QtechAcDataDtls_Type(Integer32):
    """Custom type qtechAcDataDtls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechAcDataDtls_Type.__name__ = "Integer32"
_QtechAcDataDtls_Object = MibScalar
qtechAcDataDtls = _QtechAcDataDtls_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 4),
    _QtechAcDataDtls_Type()
)
qtechAcDataDtls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcDataDtls.setStatus("current")


class _QtechAcEcnSupport_Type(Integer32):
    """Custom type qtechAcEcnSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechAcEcnSupport_Type.__name__ = "Integer32"
_QtechAcEcnSupport_Object = MibScalar
qtechAcEcnSupport = _QtechAcEcnSupport_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 5),
    _QtechAcEcnSupport_Type()
)
qtechAcEcnSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcEcnSupport.setStatus("current")
_QtechAcAcIpTable_Object = MibTable
qtechAcAcIpTable = _QtechAcAcIpTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 6)
)
if mibBuilder.loadTexts:
    qtechAcAcIpTable.setStatus("current")
_QtechAcAcIpTableEntry_Object = MibTableRow
qtechAcAcIpTableEntry = _QtechAcAcIpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 6, 1)
)
qtechAcAcIpTableEntry.setIndexNames(
    (0, "QTECH-AC-MGMT-MIB", "qtechAcAcIpIndex"),
)
if mibBuilder.loadTexts:
    qtechAcAcIpTableEntry.setStatus("current")


class _QtechAcAcIpIndex_Type(Integer32):
    """Custom type qtechAcAcIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_QtechAcAcIpIndex_Type.__name__ = "Integer32"
_QtechAcAcIpIndex_Object = MibTableColumn
qtechAcAcIpIndex = _QtechAcAcIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 6, 1, 1),
    _QtechAcAcIpIndex_Type()
)
qtechAcAcIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcAcIpIndex.setStatus("current")
_QtechAcBackAcIp_Type = IpAddress
_QtechAcBackAcIp_Object = MibTableColumn
qtechAcBackAcIp = _QtechAcBackAcIp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 6, 1, 2),
    _QtechAcBackAcIp_Type()
)
qtechAcBackAcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcBackAcIp.setStatus("current")
_QtechAcAcIpRS_Type = RowStatus
_QtechAcAcIpRS_Object = MibTableColumn
qtechAcAcIpRS = _QtechAcAcIpRS_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 6, 1, 3),
    _QtechAcAcIpRS_Type()
)
qtechAcAcIpRS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcAcIpRS.setStatus("current")


class _QtechAcMtu_Type(Integer32):
    """Custom type qtechAcMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_QtechAcMtu_Type.__name__ = "Integer32"
_QtechAcMtu_Object = MibScalar
qtechAcMtu = _QtechAcMtu_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 7),
    _QtechAcMtu_Type()
)
qtechAcMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcMtu.setStatus("current")


class _QtechAcAcName_Type(DisplayString):
    """Custom type qtechAcAcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QtechAcAcName_Type.__name__ = "DisplayString"
_QtechAcAcName_Object = MibScalar
qtechAcAcName = _QtechAcAcName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 8),
    _QtechAcAcName_Type()
)
qtechAcAcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcAcName.setStatus("current")


class _QtechAcLocation_Type(DisplayString):
    """Custom type qtechAcLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_QtechAcLocation_Type.__name__ = "DisplayString"
_QtechAcLocation_Object = MibScalar
qtechAcLocation = _QtechAcLocation_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 9),
    _QtechAcLocation_Type()
)
qtechAcLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcLocation.setStatus("current")


class _QtechAcResetAp_Type(DisplayString):
    """Custom type qtechAcResetAp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_QtechAcResetAp_Type.__name__ = "DisplayString"
_QtechAcResetAp_Object = MibScalar
qtechAcResetAp = _QtechAcResetAp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 10),
    _QtechAcResetAp_Type()
)
qtechAcResetAp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcResetAp.setStatus("current")


class _QtechAcApNum_Type(Integer32):
    """Custom type qtechAcApNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 800),
    )


_QtechAcApNum_Type.__name__ = "Integer32"
_QtechAcApNum_Object = MibScalar
qtechAcApNum = _QtechAcApNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 11),
    _QtechAcApNum_Type()
)
qtechAcApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcApNum.setStatus("current")
_QtechAc80211aRateTable_Object = MibTable
qtechAc80211aRateTable = _QtechAc80211aRateTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 12)
)
if mibBuilder.loadTexts:
    qtechAc80211aRateTable.setStatus("current")
_QtechAc80211aRateEntry_Object = MibTableRow
qtechAc80211aRateEntry = _QtechAc80211aRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 12, 1)
)
qtechAc80211aRateEntry.setIndexNames(
    (0, "QTECH-AC-MGMT-MIB", "qtechAc80211aRate"),
)
if mibBuilder.loadTexts:
    qtechAc80211aRateEntry.setStatus("current")


class _QtechAc80211aRate_Type(Integer32):
    """Custom type qtechAc80211aRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_QtechAc80211aRate_Type.__name__ = "Integer32"
_QtechAc80211aRate_Object = MibTableColumn
qtechAc80211aRate = _QtechAc80211aRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 12, 1, 1),
    _QtechAc80211aRate_Type()
)
qtechAc80211aRate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechAc80211aRate.setStatus("current")


class _QtechAc80211aRateType_Type(Integer32):
    """Custom type qtechAc80211aRateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_QtechAc80211aRateType_Type.__name__ = "Integer32"
_QtechAc80211aRateType_Object = MibTableColumn
qtechAc80211aRateType = _QtechAc80211aRateType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 12, 1, 2),
    _QtechAc80211aRateType_Type()
)
qtechAc80211aRateType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAc80211aRateType.setStatus("current")
_QtechAc80211bRateTable_Object = MibTable
qtechAc80211bRateTable = _QtechAc80211bRateTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 13)
)
if mibBuilder.loadTexts:
    qtechAc80211bRateTable.setStatus("current")
_QtechAc80211bRateEntry_Object = MibTableRow
qtechAc80211bRateEntry = _QtechAc80211bRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 13, 1)
)
qtechAc80211bRateEntry.setIndexNames(
    (0, "QTECH-AC-MGMT-MIB", "qtechAc80211bRate"),
)
if mibBuilder.loadTexts:
    qtechAc80211bRateEntry.setStatus("current")


class _QtechAc80211bRate_Type(Integer32):
    """Custom type qtechAc80211bRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_QtechAc80211bRate_Type.__name__ = "Integer32"
_QtechAc80211bRate_Object = MibTableColumn
qtechAc80211bRate = _QtechAc80211bRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 13, 1, 1),
    _QtechAc80211bRate_Type()
)
qtechAc80211bRate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechAc80211bRate.setStatus("current")


class _QtechAc80211bRateType_Type(Integer32):
    """Custom type qtechAc80211bRateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_QtechAc80211bRateType_Type.__name__ = "Integer32"
_QtechAc80211bRateType_Object = MibTableColumn
qtechAc80211bRateType = _QtechAc80211bRateType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 13, 1, 2),
    _QtechAc80211bRateType_Type()
)
qtechAc80211bRateType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAc80211bRateType.setStatus("current")


class _QtechAcFallback_Type(Integer32):
    """Custom type qtechAcFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_QtechAcFallback_Type.__name__ = "Integer32"
_QtechAcFallback_Object = MibScalar
qtechAcFallback = _QtechAcFallback_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 14),
    _QtechAcFallback_Type()
)
qtechAcFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcFallback.setStatus("current")


class _QtechAcStaNum_Type(Integer32):
    """Custom type qtechAcStaNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24000),
    )


_QtechAcStaNum_Type.__name__ = "Integer32"
_QtechAcStaNum_Object = MibScalar
qtechAcStaNum = _QtechAcStaNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 15),
    _QtechAcStaNum_Type()
)
qtechAcStaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcStaNum.setStatus("current")
_QtechAcMacAddr_Type = MacAddress
_QtechAcMacAddr_Object = MibScalar
qtechAcMacAddr = _QtechAcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 16),
    _QtechAcMacAddr_Type()
)
qtechAcMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcMacAddr.setStatus("current")


class _QtechAcDescriptor_Type(DisplayString):
    """Custom type qtechAcDescriptor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_QtechAcDescriptor_Type.__name__ = "DisplayString"
_QtechAcDescriptor_Object = MibScalar
qtechAcDescriptor = _QtechAcDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 17),
    _QtechAcDescriptor_Type()
)
qtechAcDescriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcDescriptor.setStatus("current")


class _QtechAcPID_Type(DisplayString):
    """Custom type qtechAcPID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_QtechAcPID_Type.__name__ = "DisplayString"
_QtechAcPID_Object = MibScalar
qtechAcPID = _QtechAcPID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 18),
    _QtechAcPID_Type()
)
qtechAcPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcPID.setStatus("current")


class _QtechAcHwId_Type(DisplayString):
    """Custom type qtechAcHwId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_QtechAcHwId_Type.__name__ = "DisplayString"
_QtechAcHwId_Object = MibScalar
qtechAcHwId = _QtechAcHwId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 19),
    _QtechAcHwId_Type()
)
qtechAcHwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcHwId.setStatus("current")


class _QtechAcSN_Type(DisplayString):
    """Custom type qtechAcSN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_QtechAcSN_Type.__name__ = "DisplayString"
_QtechAcSN_Object = MibScalar
qtechAcSN = _QtechAcSN_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 20),
    _QtechAcSN_Type()
)
qtechAcSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcSN.setStatus("current")
_QtechAcTemp_Type = Integer32
_QtechAcTemp_Object = MibScalar
qtechAcTemp = _QtechAcTemp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 21),
    _QtechAcTemp_Type()
)
qtechAcTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcTemp.setStatus("current")


class _QtechAcAPUpDownCtrl_Type(Integer32):
    """Custom type qtechAcAPUpDownCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechAcAPUpDownCtrl_Type.__name__ = "Integer32"
_QtechAcAPUpDownCtrl_Object = MibScalar
qtechAcAPUpDownCtrl = _QtechAcAPUpDownCtrl_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 22),
    _QtechAcAPUpDownCtrl_Type()
)
qtechAcAPUpDownCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcAPUpDownCtrl.setStatus("current")


class _QtechAcAPJoinFailCtrl_Type(Integer32):
    """Custom type qtechAcAPJoinFailCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechAcAPJoinFailCtrl_Type.__name__ = "Integer32"
_QtechAcAPJoinFailCtrl_Object = MibScalar
qtechAcAPJoinFailCtrl = _QtechAcAPJoinFailCtrl_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 23),
    _QtechAcAPJoinFailCtrl_Type()
)
qtechAcAPJoinFailCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcAPJoinFailCtrl.setStatus("current")


class _QtechAcAPDecryEroReportCtrl_Type(Integer32):
    """Custom type qtechAcAPDecryEroReportCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechAcAPDecryEroReportCtrl_Type.__name__ = "Integer32"
_QtechAcAPDecryEroReportCtrl_Object = MibScalar
qtechAcAPDecryEroReportCtrl = _QtechAcAPDecryEroReportCtrl_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 24),
    _QtechAcAPDecryEroReportCtrl_Type()
)
qtechAcAPDecryEroReportCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcAPDecryEroReportCtrl.setStatus("current")


class _QtechAcApImageUpdtCtrl_Type(Integer32):
    """Custom type qtechAcApImageUpdtCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechAcApImageUpdtCtrl_Type.__name__ = "Integer32"
_QtechAcApImageUpdtCtrl_Object = MibScalar
qtechAcApImageUpdtCtrl = _QtechAcApImageUpdtCtrl_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 25),
    _QtechAcApImageUpdtCtrl_Type()
)
qtechAcApImageUpdtCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcApImageUpdtCtrl.setStatus("current")
_QtechAcApConfigMsgEroCtrl_Type = Integer32
_QtechAcApConfigMsgEroCtrl_Object = MibScalar
qtechAcApConfigMsgEroCtrl = _QtechAcApConfigMsgEroCtrl_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 26),
    _QtechAcApConfigMsgEroCtrl_Type()
)
qtechAcApConfigMsgEroCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcApConfigMsgEroCtrl.setStatus("current")
_QtechAcApRadioOperStatuCtrl_Type = Integer32
_QtechAcApRadioOperStatuCtrl_Object = MibScalar
qtechAcApRadioOperStatuCtrl = _QtechAcApRadioOperStatuCtrl_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 27),
    _QtechAcApRadioOperStatuCtrl_Type()
)
qtechAcApRadioOperStatuCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcApRadioOperStatuCtrl.setStatus("current")
_QtechAcApAuthenFailCtrl_Type = Integer32
_QtechAcApAuthenFailCtrl_Object = MibScalar
qtechAcApAuthenFailCtrl = _QtechAcApAuthenFailCtrl_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 28),
    _QtechAcApAuthenFailCtrl_Type()
)
qtechAcApAuthenFailCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcApAuthenFailCtrl.setStatus("current")
_QtechAcApTimestampCtrl_Type = Integer32
_QtechAcApTimestampCtrl_Object = MibScalar
qtechAcApTimestampCtrl = _QtechAcApTimestampCtrl_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 29),
    _QtechAcApTimestampCtrl_Type()
)
qtechAcApTimestampCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcApTimestampCtrl.setStatus("current")
_QtechAcStaOperCtrl_Type = Integer32
_QtechAcStaOperCtrl_Object = MibScalar
qtechAcStaOperCtrl = _QtechAcStaOperCtrl_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 30),
    _QtechAcStaOperCtrl_Type()
)
qtechAcStaOperCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcStaOperCtrl.setStatus("current")


class _QtechAcType_Type(Integer32):
    """Custom type qtechAcType based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("ws5302", 1),
          ("ws5708", 2),
          ("m8600ws", 3),
          ("ws3302", 4),
          ("m12000ws", 5),
          ("ws5504", 6),
          ("ws6108", 7),
          ("ws6816", 8),
          ("m18000-WS-ED", 9),
          ("m8600E-WS-ED", 10),
          ("eg2000", 11))
    )


_QtechAcType_Type.__name__ = "Integer32"
_QtechAcType_Object = MibScalar
qtechAcType = _QtechAcType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 31),
    _QtechAcType_Type()
)
qtechAcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcType.setStatus("current")


class _QtechAcNeid_Type(DisplayString):
    """Custom type qtechAcNeid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_QtechAcNeid_Type.__name__ = "DisplayString"
_QtechAcNeid_Object = MibScalar
qtechAcNeid = _QtechAcNeid_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 32),
    _QtechAcNeid_Type()
)
qtechAcNeid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcNeid.setStatus("current")


class _QtechAcManufacturer_Type(DisplayString):
    """Custom type qtechAcManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_QtechAcManufacturer_Type.__name__ = "DisplayString"
_QtechAcManufacturer_Object = MibScalar
qtechAcManufacturer = _QtechAcManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 33),
    _QtechAcManufacturer_Type()
)
qtechAcManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcManufacturer.setStatus("current")


class _QtechAcSwVer_Type(DisplayString):
    """Custom type qtechAcSwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_QtechAcSwVer_Type.__name__ = "DisplayString"
_QtechAcSwVer_Object = MibScalar
qtechAcSwVer = _QtechAcSwVer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 34),
    _QtechAcSwVer_Type()
)
qtechAcSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcSwVer.setStatus("current")


class _QtechAcSwManufacturer_Type(DisplayString):
    """Custom type qtechAcSwManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_QtechAcSwManufacturer_Type.__name__ = "DisplayString"
_QtechAcSwManufacturer_Object = MibScalar
qtechAcSwManufacturer = _QtechAcSwManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 35),
    _QtechAcSwManufacturer_Type()
)
qtechAcSwManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcSwManufacturer.setStatus("current")
_QtechAcStaResourceNotEnough_Type = Integer32
_QtechAcStaResourceNotEnough_Object = MibScalar
qtechAcStaResourceNotEnough = _QtechAcStaResourceNotEnough_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 36),
    _QtechAcStaResourceNotEnough_Type()
)
qtechAcStaResourceNotEnough.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcStaResourceNotEnough.setStatus("current")
_QtechAcPppoeClientAct_Type = Integer32
_QtechAcPppoeClientAct_Object = MibScalar
qtechAcPppoeClientAct = _QtechAcPppoeClientAct_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 37),
    _QtechAcPppoeClientAct_Type()
)
qtechAcPppoeClientAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcPppoeClientAct.setStatus("current")
_QtechAcPppoeClientMax_Type = Integer32
_QtechAcPppoeClientMax_Object = MibScalar
qtechAcPppoeClientMax = _QtechAcPppoeClientMax_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 38),
    _QtechAcPppoeClientMax_Type()
)
qtechAcPppoeClientMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcPppoeClientMax.setStatus("current")
_QtechAcStaActThredhold_Type = Integer32
_QtechAcStaActThredhold_Object = MibScalar
qtechAcStaActThredhold = _QtechAcStaActThredhold_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 39),
    _QtechAcStaActThredhold_Type()
)
qtechAcStaActThredhold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcStaActThredhold.setStatus("current")
_QtechAcStaDisactThredhold_Type = Integer32
_QtechAcStaDisactThredhold_Object = MibScalar
qtechAcStaDisactThredhold = _QtechAcStaDisactThredhold_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 40),
    _QtechAcStaDisactThredhold_Type()
)
qtechAcStaDisactThredhold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcStaDisactThredhold.setStatus("current")
_QtechAcStaTotalRoamThredhold_Type = Integer32
_QtechAcStaTotalRoamThredhold_Object = MibScalar
qtechAcStaTotalRoamThredhold = _QtechAcStaTotalRoamThredhold_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 41),
    _QtechAcStaTotalRoamThredhold_Type()
)
qtechAcStaTotalRoamThredhold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcStaTotalRoamThredhold.setStatus("current")
_QtechAcStaPerRoamThredhold_Type = Integer32
_QtechAcStaPerRoamThredhold_Object = MibScalar
qtechAcStaPerRoamThredhold = _QtechAcStaPerRoamThredhold_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 42),
    _QtechAcStaPerRoamThredhold_Type()
)
qtechAcStaPerRoamThredhold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcStaPerRoamThredhold.setStatus("current")


class _QtechAcStaOffLineRemainTime_Type(Integer32):
    """Custom type qtechAcStaOffLineRemainTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 365),
    )


_QtechAcStaOffLineRemainTime_Type.__name__ = "Integer32"
_QtechAcStaOffLineRemainTime_Object = MibScalar
qtechAcStaOffLineRemainTime = _QtechAcStaOffLineRemainTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 43),
    _QtechAcStaOffLineRemainTime_Type()
)
qtechAcStaOffLineRemainTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcStaOffLineRemainTime.setStatus("current")


class _QtechAcStaOffLineNumber_Type(Integer32):
    """Custom type qtechAcStaOffLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_QtechAcStaOffLineNumber_Type.__name__ = "Integer32"
_QtechAcStaOffLineNumber_Object = MibScalar
qtechAcStaOffLineNumber = _QtechAcStaOffLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 44),
    _QtechAcStaOffLineNumber_Type()
)
qtechAcStaOffLineNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcStaOffLineNumber.setStatus("current")
_QtechAcStaOffLineDelSingle_Type = MacAddress
_QtechAcStaOffLineDelSingle_Object = MibScalar
qtechAcStaOffLineDelSingle = _QtechAcStaOffLineDelSingle_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 45),
    _QtechAcStaOffLineDelSingle_Type()
)
qtechAcStaOffLineDelSingle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcStaOffLineDelSingle.setStatus("current")


class _QtechAcStaOffLineDelAll_Type(Integer32):
    """Custom type qtechAcStaOffLineDelAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_QtechAcStaOffLineDelAll_Type.__name__ = "Integer32"
_QtechAcStaOffLineDelAll_Object = MibScalar
qtechAcStaOffLineDelAll = _QtechAcStaOffLineDelAll_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 46),
    _QtechAcStaOffLineDelAll_Type()
)
qtechAcStaOffLineDelAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcStaOffLineDelAll.setStatus("current")


class _QtechAcRmOffLineApConfig_Type(DisplayString):
    """Custom type qtechAcRmOffLineApConfig based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_QtechAcRmOffLineApConfig_Type.__name__ = "DisplayString"
_QtechAcRmOffLineApConfig_Object = MibScalar
qtechAcRmOffLineApConfig = _QtechAcRmOffLineApConfig_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 47),
    _QtechAcRmOffLineApConfig_Type()
)
qtechAcRmOffLineApConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcRmOffLineApConfig.setStatus("current")
_QtechAcFlowBlGroupTable_Object = MibTable
qtechAcFlowBlGroupTable = _QtechAcFlowBlGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 48)
)
if mibBuilder.loadTexts:
    qtechAcFlowBlGroupTable.setStatus("current")
_QtechAcFlowBlGroupEntry_Object = MibTableRow
qtechAcFlowBlGroupEntry = _QtechAcFlowBlGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 48, 1)
)
qtechAcFlowBlGroupEntry.setIndexNames(
    (0, "QTECH-AC-MGMT-MIB", "qtechAcFlowBlGroupName"),
)
if mibBuilder.loadTexts:
    qtechAcFlowBlGroupEntry.setStatus("current")
_QtechAcFlowBlGroupName_Type = DisplayString
_QtechAcFlowBlGroupName_Object = MibTableColumn
qtechAcFlowBlGroupName = _QtechAcFlowBlGroupName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 48, 1, 1),
    _QtechAcFlowBlGroupName_Type()
)
qtechAcFlowBlGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcFlowBlGroupName.setStatus("current")
_QtechAcFlowBlApName1_Type = DisplayString
_QtechAcFlowBlApName1_Object = MibTableColumn
qtechAcFlowBlApName1 = _QtechAcFlowBlApName1_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 48, 1, 2),
    _QtechAcFlowBlApName1_Type()
)
qtechAcFlowBlApName1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcFlowBlApName1.setStatus("current")
_QtechAcFlowBlApName2_Type = DisplayString
_QtechAcFlowBlApName2_Object = MibTableColumn
qtechAcFlowBlApName2 = _QtechAcFlowBlApName2_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 48, 1, 3),
    _QtechAcFlowBlApName2_Type()
)
qtechAcFlowBlApName2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcFlowBlApName2.setStatus("current")
_QtechAcFlowBlApName3_Type = DisplayString
_QtechAcFlowBlApName3_Object = MibTableColumn
qtechAcFlowBlApName3 = _QtechAcFlowBlApName3_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 48, 1, 4),
    _QtechAcFlowBlApName3_Type()
)
qtechAcFlowBlApName3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcFlowBlApName3.setStatus("current")
_QtechAcFlowBlApName4_Type = DisplayString
_QtechAcFlowBlApName4_Object = MibTableColumn
qtechAcFlowBlApName4 = _QtechAcFlowBlApName4_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 48, 1, 5),
    _QtechAcFlowBlApName4_Type()
)
qtechAcFlowBlApName4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcFlowBlApName4.setStatus("current")
_QtechAcFlowBlApName5_Type = DisplayString
_QtechAcFlowBlApName5_Object = MibTableColumn
qtechAcFlowBlApName5 = _QtechAcFlowBlApName5_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 48, 1, 6),
    _QtechAcFlowBlApName5_Type()
)
qtechAcFlowBlApName5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcFlowBlApName5.setStatus("current")
_QtechAcFlowBlApName6_Type = DisplayString
_QtechAcFlowBlApName6_Object = MibTableColumn
qtechAcFlowBlApName6 = _QtechAcFlowBlApName6_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 48, 1, 7),
    _QtechAcFlowBlApName6_Type()
)
qtechAcFlowBlApName6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcFlowBlApName6.setStatus("current")
_QtechAcFlowBlApName7_Type = DisplayString
_QtechAcFlowBlApName7_Object = MibTableColumn
qtechAcFlowBlApName7 = _QtechAcFlowBlApName7_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 48, 1, 8),
    _QtechAcFlowBlApName7_Type()
)
qtechAcFlowBlApName7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcFlowBlApName7.setStatus("current")
_QtechAcFlowBlApName8_Type = DisplayString
_QtechAcFlowBlApName8_Object = MibTableColumn
qtechAcFlowBlApName8 = _QtechAcFlowBlApName8_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 48, 1, 9),
    _QtechAcFlowBlApName8_Type()
)
qtechAcFlowBlApName8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcFlowBlApName8.setStatus("current")
_QtechAcFlowBlApName9_Type = DisplayString
_QtechAcFlowBlApName9_Object = MibTableColumn
qtechAcFlowBlApName9 = _QtechAcFlowBlApName9_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 48, 1, 10),
    _QtechAcFlowBlApName9_Type()
)
qtechAcFlowBlApName9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcFlowBlApName9.setStatus("current")
_QtechAcFlowBlApName10_Type = DisplayString
_QtechAcFlowBlApName10_Object = MibTableColumn
qtechAcFlowBlApName10 = _QtechAcFlowBlApName10_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 48, 1, 11),
    _QtechAcFlowBlApName10_Type()
)
qtechAcFlowBlApName10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcFlowBlApName10.setStatus("current")


class _QtechAcFlowBlNum_Type(Integer32):
    """Custom type qtechAcFlowBlNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_QtechAcFlowBlNum_Type.__name__ = "Integer32"
_QtechAcFlowBlNum_Object = MibTableColumn
qtechAcFlowBlNum = _QtechAcFlowBlNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 48, 1, 12),
    _QtechAcFlowBlNum_Type()
)
qtechAcFlowBlNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcFlowBlNum.setStatus("current")
_QtechAcFlowBlRS_Type = RowStatus
_QtechAcFlowBlRS_Object = MibTableColumn
qtechAcFlowBlRS = _QtechAcFlowBlRS_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 48, 1, 13),
    _QtechAcFlowBlRS_Type()
)
qtechAcFlowBlRS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcFlowBlRS.setStatus("current")
_QtechAcFlowBlEnable_Type = Integer32
_QtechAcFlowBlEnable_Object = MibTableColumn
qtechAcFlowBlEnable = _QtechAcFlowBlEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 48, 1, 14),
    _QtechAcFlowBlEnable_Type()
)
qtechAcFlowBlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcFlowBlEnable.setStatus("current")
_QtechAcFlowBlBase_Type = Integer32
_QtechAcFlowBlBase_Object = MibTableColumn
qtechAcFlowBlBase = _QtechAcFlowBlBase_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 48, 1, 15),
    _QtechAcFlowBlBase_Type()
)
qtechAcFlowBlBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcFlowBlBase.setStatus("current")
_QtechAcFlowBlIsEnable_Type = TruthValue
_QtechAcFlowBlIsEnable_Object = MibTableColumn
qtechAcFlowBlIsEnable = _QtechAcFlowBlIsEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 48, 1, 16),
    _QtechAcFlowBlIsEnable_Type()
)
qtechAcFlowBlIsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcFlowBlIsEnable.setStatus("current")
_QtechAcNumBlGroupTable_Object = MibTable
qtechAcNumBlGroupTable = _QtechAcNumBlGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 49)
)
if mibBuilder.loadTexts:
    qtechAcNumBlGroupTable.setStatus("current")
_QtechAcNumBlGroupEntry_Object = MibTableRow
qtechAcNumBlGroupEntry = _QtechAcNumBlGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 49, 1)
)
qtechAcNumBlGroupEntry.setIndexNames(
    (0, "QTECH-AC-MGMT-MIB", "qtechAcNumBlGroupName"),
)
if mibBuilder.loadTexts:
    qtechAcNumBlGroupEntry.setStatus("current")
_QtechAcNumBlGroupName_Type = DisplayString
_QtechAcNumBlGroupName_Object = MibTableColumn
qtechAcNumBlGroupName = _QtechAcNumBlGroupName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 49, 1, 1),
    _QtechAcNumBlGroupName_Type()
)
qtechAcNumBlGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcNumBlGroupName.setStatus("current")
_QtechAcNumBlApName1_Type = DisplayString
_QtechAcNumBlApName1_Object = MibTableColumn
qtechAcNumBlApName1 = _QtechAcNumBlApName1_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 49, 1, 2),
    _QtechAcNumBlApName1_Type()
)
qtechAcNumBlApName1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcNumBlApName1.setStatus("current")
_QtechAcNumBlApName2_Type = DisplayString
_QtechAcNumBlApName2_Object = MibTableColumn
qtechAcNumBlApName2 = _QtechAcNumBlApName2_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 49, 1, 3),
    _QtechAcNumBlApName2_Type()
)
qtechAcNumBlApName2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcNumBlApName2.setStatus("current")
_QtechAcNumBlApName3_Type = DisplayString
_QtechAcNumBlApName3_Object = MibTableColumn
qtechAcNumBlApName3 = _QtechAcNumBlApName3_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 49, 1, 4),
    _QtechAcNumBlApName3_Type()
)
qtechAcNumBlApName3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcNumBlApName3.setStatus("current")
_QtechAcNumBlApName4_Type = DisplayString
_QtechAcNumBlApName4_Object = MibTableColumn
qtechAcNumBlApName4 = _QtechAcNumBlApName4_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 49, 1, 5),
    _QtechAcNumBlApName4_Type()
)
qtechAcNumBlApName4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcNumBlApName4.setStatus("current")
_QtechAcNumBlApName5_Type = DisplayString
_QtechAcNumBlApName5_Object = MibTableColumn
qtechAcNumBlApName5 = _QtechAcNumBlApName5_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 49, 1, 6),
    _QtechAcNumBlApName5_Type()
)
qtechAcNumBlApName5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcNumBlApName5.setStatus("current")
_QtechAcNumBlApName6_Type = DisplayString
_QtechAcNumBlApName6_Object = MibTableColumn
qtechAcNumBlApName6 = _QtechAcNumBlApName6_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 49, 1, 7),
    _QtechAcNumBlApName6_Type()
)
qtechAcNumBlApName6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcNumBlApName6.setStatus("current")
_QtechAcNumBlApName7_Type = DisplayString
_QtechAcNumBlApName7_Object = MibTableColumn
qtechAcNumBlApName7 = _QtechAcNumBlApName7_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 49, 1, 8),
    _QtechAcNumBlApName7_Type()
)
qtechAcNumBlApName7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcNumBlApName7.setStatus("current")
_QtechAcNumBlApName8_Type = DisplayString
_QtechAcNumBlApName8_Object = MibTableColumn
qtechAcNumBlApName8 = _QtechAcNumBlApName8_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 49, 1, 9),
    _QtechAcNumBlApName8_Type()
)
qtechAcNumBlApName8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcNumBlApName8.setStatus("current")
_QtechAcNumBlApName9_Type = DisplayString
_QtechAcNumBlApName9_Object = MibTableColumn
qtechAcNumBlApName9 = _QtechAcNumBlApName9_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 49, 1, 10),
    _QtechAcNumBlApName9_Type()
)
qtechAcNumBlApName9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcNumBlApName9.setStatus("current")
_QtechAcNumBlApName10_Type = DisplayString
_QtechAcNumBlApName10_Object = MibTableColumn
qtechAcNumBlApName10 = _QtechAcNumBlApName10_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 49, 1, 11),
    _QtechAcNumBlApName10_Type()
)
qtechAcNumBlApName10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcNumBlApName10.setStatus("current")


class _QtechAcNumBlNum_Type(Integer32):
    """Custom type qtechAcNumBlNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_QtechAcNumBlNum_Type.__name__ = "Integer32"
_QtechAcNumBlNum_Object = MibTableColumn
qtechAcNumBlNum = _QtechAcNumBlNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 49, 1, 12),
    _QtechAcNumBlNum_Type()
)
qtechAcNumBlNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcNumBlNum.setStatus("current")
_QtechAcNumBlRS_Type = RowStatus
_QtechAcNumBlRS_Object = MibTableColumn
qtechAcNumBlRS = _QtechAcNumBlRS_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 49, 1, 13),
    _QtechAcNumBlRS_Type()
)
qtechAcNumBlRS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcNumBlRS.setStatus("current")
_QtechAcNumBlEnable_Type = Integer32
_QtechAcNumBlEnable_Object = MibTableColumn
qtechAcNumBlEnable = _QtechAcNumBlEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 49, 1, 14),
    _QtechAcNumBlEnable_Type()
)
qtechAcNumBlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcNumBlEnable.setStatus("current")
_QtechAcNumBlIsEnable_Type = TruthValue
_QtechAcNumBlIsEnable_Object = MibTableColumn
qtechAcNumBlIsEnable = _QtechAcNumBlIsEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 49, 1, 15),
    _QtechAcNumBlIsEnable_Type()
)
qtechAcNumBlIsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcNumBlIsEnable.setStatus("current")
_QtechAcInAcRoamNum_Type = Integer32
_QtechAcInAcRoamNum_Object = MibScalar
qtechAcInAcRoamNum = _QtechAcInAcRoamNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 50),
    _QtechAcInAcRoamNum_Type()
)
qtechAcInAcRoamNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcInAcRoamNum.setStatus("current")
_QtechAcBetweenAcRoamInNum_Type = Integer32
_QtechAcBetweenAcRoamInNum_Object = MibScalar
qtechAcBetweenAcRoamInNum = _QtechAcBetweenAcRoamInNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 51),
    _QtechAcBetweenAcRoamInNum_Type()
)
qtechAcBetweenAcRoamInNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcBetweenAcRoamInNum.setStatus("current")
_QtechAcStaOnOverThrodOperCtrl_Type = Integer32
_QtechAcStaOnOverThrodOperCtrl_Object = MibScalar
qtechAcStaOnOverThrodOperCtrl = _QtechAcStaOnOverThrodOperCtrl_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 52),
    _QtechAcStaOnOverThrodOperCtrl_Type()
)
qtechAcStaOnOverThrodOperCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcStaOnOverThrodOperCtrl.setStatus("current")
_QtechAcStaOffOverThrodOperCtrl_Type = Integer32
_QtechAcStaOffOverThrodOperCtrl_Object = MibScalar
qtechAcStaOffOverThrodOperCtrl = _QtechAcStaOffOverThrodOperCtrl_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 53),
    _QtechAcStaOffOverThrodOperCtrl_Type()
)
qtechAcStaOffOverThrodOperCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcStaOffOverThrodOperCtrl.setStatus("current")
_QtechAcBetweenAcRoamOutNum_Type = Integer32
_QtechAcBetweenAcRoamOutNum_Object = MibScalar
qtechAcBetweenAcRoamOutNum = _QtechAcBetweenAcRoamOutNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 54),
    _QtechAcBetweenAcRoamOutNum_Type()
)
qtechAcBetweenAcRoamOutNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcBetweenAcRoamOutNum.setStatus("current")
_QtechAcCpusageSwitch_Type = Integer32
_QtechAcCpusageSwitch_Object = MibScalar
qtechAcCpusageSwitch = _QtechAcCpusageSwitch_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 55),
    _QtechAcCpusageSwitch_Type()
)
qtechAcCpusageSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcCpusageSwitch.setStatus("current")
_QtechAcCpuUsageTrapTimer_Type = Integer32
_QtechAcCpuUsageTrapTimer_Object = MibScalar
qtechAcCpuUsageTrapTimer = _QtechAcCpuUsageTrapTimer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 56),
    _QtechAcCpuUsageTrapTimer_Type()
)
qtechAcCpuUsageTrapTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcCpuUsageTrapTimer.setStatus("current")
_QtechAcStatTrapTimer_Type = Integer32
_QtechAcStatTrapTimer_Object = MibScalar
qtechAcStatTrapTimer = _QtechAcStatTrapTimer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 57),
    _QtechAcStatTrapTimer_Type()
)
qtechAcStatTrapTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcStatTrapTimer.setStatus("current")
_QtechAcHeartBeat_Type = Integer32
_QtechAcHeartBeat_Object = MibScalar
qtechAcHeartBeat = _QtechAcHeartBeat_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 58),
    _QtechAcHeartBeat_Type()
)
qtechAcHeartBeat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcHeartBeat.setStatus("current")
_QtechAcTotalApSupNum_Type = Integer32
_QtechAcTotalApSupNum_Object = MibScalar
qtechAcTotalApSupNum = _QtechAcTotalApSupNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 59),
    _QtechAcTotalApSupNum_Type()
)
qtechAcTotalApSupNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcTotalApSupNum.setStatus("current")
_QtechAcTotalStaSupNum_Type = Integer32
_QtechAcTotalStaSupNum_Object = MibScalar
qtechAcTotalStaSupNum = _QtechAcTotalStaSupNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 60),
    _QtechAcTotalStaSupNum_Type()
)
qtechAcTotalStaSupNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcTotalStaSupNum.setStatus("current")
_QtechAcTotalPppoeSupNum_Type = Integer32
_QtechAcTotalPppoeSupNum_Object = MibScalar
qtechAcTotalPppoeSupNum = _QtechAcTotalPppoeSupNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 61),
    _QtechAcTotalPppoeSupNum_Type()
)
qtechAcTotalPppoeSupNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcTotalPppoeSupNum.setStatus("current")
_QtechAcCurTotalApSupNum_Type = Integer32
_QtechAcCurTotalApSupNum_Object = MibScalar
qtechAcCurTotalApSupNum = _QtechAcCurTotalApSupNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 62),
    _QtechAcCurTotalApSupNum_Type()
)
qtechAcCurTotalApSupNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcCurTotalApSupNum.setStatus("current")
_QtechAcCurTotalStaSupNum_Type = Integer32
_QtechAcCurTotalStaSupNum_Object = MibScalar
qtechAcCurTotalStaSupNum = _QtechAcCurTotalStaSupNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 63),
    _QtechAcCurTotalStaSupNum_Type()
)
qtechAcCurTotalStaSupNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcCurTotalStaSupNum.setStatus("current")
_QtechAcCurTotalPppoeSupNum_Type = Integer32
_QtechAcCurTotalPppoeSupNum_Object = MibScalar
qtechAcCurTotalPppoeSupNum = _QtechAcCurTotalPppoeSupNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 64),
    _QtechAcCurTotalPppoeSupNum_Type()
)
qtechAcCurTotalPppoeSupNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcCurTotalPppoeSupNum.setStatus("current")
_QtechAcNasId_Type = DisplayString
_QtechAcNasId_Object = MibScalar
qtechAcNasId = _QtechAcNasId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 65),
    _QtechAcNasId_Type()
)
qtechAcNasId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcNasId.setStatus("current")
_QtechAcStaLimitLicense_Type = Integer32
_QtechAcStaLimitLicense_Object = MibScalar
qtechAcStaLimitLicense = _QtechAcStaLimitLicense_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 66),
    _QtechAcStaLimitLicense_Type()
)
qtechAcStaLimitLicense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcStaLimitLicense.setStatus("current")
_QtechAcWtpLimitLicense_Type = Integer32
_QtechAcWtpLimitLicense_Object = MibScalar
qtechAcWtpLimitLicense = _QtechAcWtpLimitLicense_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 67),
    _QtechAcWtpLimitLicense_Type()
)
qtechAcWtpLimitLicense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcWtpLimitLicense.setStatus("current")


class _QtechAcStaIpv6Num_Type(Integer32):
    """Custom type qtechAcStaIpv6Num based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24000),
    )


_QtechAcStaIpv6Num_Type.__name__ = "Integer32"
_QtechAcStaIpv6Num_Object = MibScalar
qtechAcStaIpv6Num = _QtechAcStaIpv6Num_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 68),
    _QtechAcStaIpv6Num_Type()
)
qtechAcStaIpv6Num.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcStaIpv6Num.setStatus("current")
_QtechAcIpv6_Type = DisplayString
_QtechAcIpv6_Object = MibScalar
qtechAcIpv6 = _QtechAcIpv6_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 69),
    _QtechAcIpv6_Type()
)
qtechAcIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcIpv6.setStatus("current")
_QtechAcIpv6Prefix_Type = DisplayString
_QtechAcIpv6Prefix_Object = MibScalar
qtechAcIpv6Prefix = _QtechAcIpv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 70),
    _QtechAcIpv6Prefix_Type()
)
qtechAcIpv6Prefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcIpv6Prefix.setStatus("current")


class _QtechAcIpv6Type_Type(Integer32):
    """Custom type qtechAcIpv6Type based on Integer32"""
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
        *(("unknown", 0),
          ("unicase", 1),
          ("anycase", 2),
          ("multicase", 3))
    )


_QtechAcIpv6Type_Type.__name__ = "Integer32"
_QtechAcIpv6Type_Object = MibScalar
qtechAcIpv6Type = _QtechAcIpv6Type_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 71),
    _QtechAcIpv6Type_Type()
)
qtechAcIpv6Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcIpv6Type.setStatus("current")
_QtechAcIpv6AddrType_Type = DisplayString
_QtechAcIpv6AddrType_Object = MibScalar
qtechAcIpv6AddrType = _QtechAcIpv6AddrType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 72),
    _QtechAcIpv6AddrType_Type()
)
qtechAcIpv6AddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcIpv6AddrType.setStatus("current")
_QtechAcKickClient_Type = MacAddress
_QtechAcKickClient_Object = MibScalar
qtechAcKickClient = _QtechAcKickClient_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 73),
    _QtechAcKickClient_Type()
)
qtechAcKickClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcKickClient.setStatus("current")
_QtechAcOpenStaNum_Type = Integer32
_QtechAcOpenStaNum_Object = MibScalar
qtechAcOpenStaNum = _QtechAcOpenStaNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 74),
    _QtechAcOpenStaNum_Type()
)
qtechAcOpenStaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcOpenStaNum.setStatus("current")
_QtechAcOpenStaAbnormalDownTimes_Type = Integer32
_QtechAcOpenStaAbnormalDownTimes_Object = MibScalar
qtechAcOpenStaAbnormalDownTimes = _QtechAcOpenStaAbnormalDownTimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 75),
    _QtechAcOpenStaAbnormalDownTimes_Type()
)
qtechAcOpenStaAbnormalDownTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcOpenStaAbnormalDownTimes.setStatus("current")
_QtechAcWepPskStaNum_Type = Integer32
_QtechAcWepPskStaNum_Object = MibScalar
qtechAcWepPskStaNum = _QtechAcWepPskStaNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 76),
    _QtechAcWepPskStaNum_Type()
)
qtechAcWepPskStaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcWepPskStaNum.setStatus("current")
_QtechAcWepPskStaAbnormalDownTimes_Type = Integer32
_QtechAcWepPskStaAbnormalDownTimes_Object = MibScalar
qtechAcWepPskStaAbnormalDownTimes = _QtechAcWepPskStaAbnormalDownTimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 1, 77),
    _QtechAcWepPskStaAbnormalDownTimes_Type()
)
qtechAcWepPskStaAbnormalDownTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcWepPskStaAbnormalDownTimes.setStatus("current")
_QtechAcMgmtAcIf_ObjectIdentity = ObjectIdentity
qtechAcMgmtAcIf = _QtechAcMgmtAcIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 1, 2)
)
_QtechAcMgmtApMIBObjects_ObjectIdentity = ObjectIdentity
qtechAcMgmtApMIBObjects = _QtechAcMgmtApMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2)
)
_QtechAcMgmtAp_ObjectIdentity = ObjectIdentity
qtechAcMgmtAp = _QtechAcMgmtAp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1)
)
_QtechApCfgTable_Object = MibTable
qtechApCfgTable = _QtechApCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1)
)
if mibBuilder.loadTexts:
    qtechApCfgTable.setStatus("current")
_QtechApCfgEntry_Object = MibTableRow
qtechApCfgEntry = _QtechApCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1)
)
qtechApCfgEntry.setIndexNames(
    (0, "QTECH-AC-MGMT-MIB", "qtechApMacAddr"),
)
if mibBuilder.loadTexts:
    qtechApCfgEntry.setStatus("current")
_QtechApMacAddr_Type = MacAddress
_QtechApMacAddr_Object = MibTableColumn
qtechApMacAddr = _QtechApMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 1),
    _QtechApMacAddr_Type()
)
qtechApMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApMacAddr.setStatus("current")


class _QtechApApName_Type(DisplayString):
    """Custom type qtechApApName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_QtechApApName_Type.__name__ = "DisplayString"
_QtechApApName_Object = MibTableColumn
qtechApApName = _QtechApApName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 2),
    _QtechApApName_Type()
)
qtechApApName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApApName.setStatus("current")


class _QtechApApgName_Type(DisplayString):
    """Custom type qtechApApgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_QtechApApgName_Type.__name__ = "DisplayString"
_QtechApApgName_Object = MibTableColumn
qtechApApgName = _QtechApApgName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 3),
    _QtechApApgName_Type()
)
qtechApApgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApApgName.setStatus("current")


class _QtechApDiscTimer_Type(Integer32):
    """Custom type qtechApDiscTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 180),
    )


_QtechApDiscTimer_Type.__name__ = "Integer32"
_QtechApDiscTimer_Object = MibTableColumn
qtechApDiscTimer = _QtechApDiscTimer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 4),
    _QtechApDiscTimer_Type()
)
qtechApDiscTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApDiscTimer.setStatus("current")


class _QtechApEchoReqTimer_Type(Integer32):
    """Custom type qtechApEchoReqTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_QtechApEchoReqTimer_Type.__name__ = "Integer32"
_QtechApEchoReqTimer_Object = MibTableColumn
qtechApEchoReqTimer = _QtechApEchoReqTimer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 5),
    _QtechApEchoReqTimer_Type()
)
qtechApEchoReqTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApEchoReqTimer.setStatus("current")


class _QtechApEroReportTimer_Type(Integer32):
    """Custom type qtechApEroReportTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1080),
    )


_QtechApEroReportTimer_Type.__name__ = "Integer32"
_QtechApEroReportTimer_Object = MibTableColumn
qtechApEroReportTimer = _QtechApEroReportTimer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 6),
    _QtechApEroReportTimer_Type()
)
qtechApEroReportTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApEroReportTimer.setStatus("current")


class _QtechApStaTimeoutTimer_Type(Integer32):
    """Custom type qtechApStaTimeoutTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2700),
    )


_QtechApStaTimeoutTimer_Type.__name__ = "Integer32"
_QtechApStaTimeoutTimer_Object = MibTableColumn
qtechApStaTimeoutTimer = _QtechApStaTimeoutTimer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 7),
    _QtechApStaTimeoutTimer_Type()
)
qtechApStaTimeoutTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApStaTimeoutTimer.setStatus("current")


class _QtechApStatisticsTimer_Type(Integer32):
    """Custom type qtechApStatisticsTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QtechApStatisticsTimer_Type.__name__ = "Integer32"
_QtechApStatisticsTimer_Object = MibTableColumn
qtechApStatisticsTimer = _QtechApStatisticsTimer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 8),
    _QtechApStatisticsTimer_Type()
)
qtechApStatisticsTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApStatisticsTimer.setStatus("current")


class _QtechApFallback_Type(Integer32):
    """Custom type qtechApFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_QtechApFallback_Type.__name__ = "Integer32"
_QtechApFallback_Object = MibTableColumn
qtechApFallback = _QtechApFallback_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 9),
    _QtechApFallback_Type()
)
qtechApFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApFallback.setStatus("current")


class _QtechApImageId_Type(DisplayString):
    """Custom type qtechApImageId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_QtechApImageId_Type.__name__ = "DisplayString"
_QtechApImageId_Object = MibTableColumn
qtechApImageId = _QtechApImageId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 10),
    _QtechApImageId_Type()
)
qtechApImageId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApImageId.setStatus("current")


class _QtechApIpDhcp_Type(Integer32):
    """Custom type qtechApIpDhcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechApIpDhcp_Type.__name__ = "Integer32"
_QtechApIpDhcp_Object = MibTableColumn
qtechApIpDhcp = _QtechApIpDhcp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 11),
    _QtechApIpDhcp_Type()
)
qtechApIpDhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApIpDhcp.setStatus("current")


class _QtechApLocation_Type(DisplayString):
    """Custom type qtechApLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_QtechApLocation_Type.__name__ = "DisplayString"
_QtechApLocation_Object = MibTableColumn
qtechApLocation = _QtechApLocation_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 12),
    _QtechApLocation_Type()
)
qtechApLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApLocation.setStatus("current")


class _QtechApWpsMfp_Type(Integer32):
    """Custom type qtechApWpsMfp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechApWpsMfp_Type.__name__ = "Integer32"
_QtechApWpsMfp_Object = MibTableColumn
qtechApWpsMfp = _QtechApWpsMfp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 13),
    _QtechApWpsMfp_Type()
)
qtechApWpsMfp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApWpsMfp.setStatus("current")


class _QtechApLastRebootReason_Type(Integer32):
    """Custom type qtechApLastRebootReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupport", 0),
          ("acInit", 1),
          ("linkFail", 2),
          ("sWFail", 3),
          ("hWFail", 4),
          ("otherFail", 5),
          ("unknown", 255))
    )


_QtechApLastRebootReason_Type.__name__ = "Integer32"
_QtechApLastRebootReason_Object = MibTableColumn
qtechApLastRebootReason = _QtechApLastRebootReason_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 14),
    _QtechApLastRebootReason_Type()
)
qtechApLastRebootReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApLastRebootReason.setStatus("current")


class _QtechApEthernetIfName_Type(DisplayString):
    """Custom type qtechApEthernetIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechApEthernetIfName_Type.__name__ = "DisplayString"
_QtechApEthernetIfName_Object = MibTableColumn
qtechApEthernetIfName = _QtechApEthernetIfName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 15),
    _QtechApEthernetIfName_Type()
)
qtechApEthernetIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApEthernetIfName.setStatus("current")
_QtechApEthernetIfMacAddress_Type = MacAddress
_QtechApEthernetIfMacAddress_Object = MibTableColumn
qtechApEthernetIfMacAddress = _QtechApEthernetIfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 16),
    _QtechApEthernetIfMacAddress_Type()
)
qtechApEthernetIfMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApEthernetIfMacAddress.setStatus("current")
_QtechApEthernetIfAdminStatus_Type = Integer32
_QtechApEthernetIfAdminStatus_Object = MibTableColumn
qtechApEthernetIfAdminStatus = _QtechApEthernetIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 17),
    _QtechApEthernetIfAdminStatus_Type()
)
qtechApEthernetIfAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApEthernetIfAdminStatus.setStatus("current")
_QtechApEthernetIfOperStatus_Type = Integer32
_QtechApEthernetIfOperStatus_Object = MibTableColumn
qtechApEthernetIfOperStatus = _QtechApEthernetIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 18),
    _QtechApEthernetIfOperStatus_Type()
)
qtechApEthernetIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApEthernetIfOperStatus.setStatus("current")
_QtechApEthernetIfRxUcastPkts_Type = Counter32
_QtechApEthernetIfRxUcastPkts_Object = MibTableColumn
qtechApEthernetIfRxUcastPkts = _QtechApEthernetIfRxUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 19),
    _QtechApEthernetIfRxUcastPkts_Type()
)
qtechApEthernetIfRxUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApEthernetIfRxUcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    qtechApEthernetIfRxUcastPkts.setUnits("packets")
_QtechApEthernetIfRxNUcastPkts_Type = Counter32
_QtechApEthernetIfRxNUcastPkts_Object = MibTableColumn
qtechApEthernetIfRxNUcastPkts = _QtechApEthernetIfRxNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 20),
    _QtechApEthernetIfRxNUcastPkts_Type()
)
qtechApEthernetIfRxNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApEthernetIfRxNUcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    qtechApEthernetIfRxNUcastPkts.setUnits("packets")
_QtechApEthernetIfTxUcastPkts_Type = Counter32
_QtechApEthernetIfTxUcastPkts_Object = MibTableColumn
qtechApEthernetIfTxUcastPkts = _QtechApEthernetIfTxUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 21),
    _QtechApEthernetIfTxUcastPkts_Type()
)
qtechApEthernetIfTxUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApEthernetIfTxUcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    qtechApEthernetIfTxUcastPkts.setUnits("packets")
_QtechApEthernetIfTxNUcastPkts_Type = Counter32
_QtechApEthernetIfTxNUcastPkts_Object = MibTableColumn
qtechApEthernetIfTxNUcastPkts = _QtechApEthernetIfTxNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 22),
    _QtechApEthernetIfTxNUcastPkts_Type()
)
qtechApEthernetIfTxNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApEthernetIfTxNUcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    qtechApEthernetIfTxNUcastPkts.setUnits("packets")


class _QtechApEthernetIfDuplex_Type(Integer32):
    """Custom type qtechApEthernetIfDuplex based on Integer32"""
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
          ("halfduplex", 2),
          ("fullduplex", 3),
          ("auto", 4))
    )


_QtechApEthernetIfDuplex_Type.__name__ = "Integer32"
_QtechApEthernetIfDuplex_Object = MibTableColumn
qtechApEthernetIfDuplex = _QtechApEthernetIfDuplex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 23),
    _QtechApEthernetIfDuplex_Type()
)
qtechApEthernetIfDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApEthernetIfDuplex.setStatus("current")
_QtechApEthernetIfLinkSpeed_Type = Integer32
_QtechApEthernetIfLinkSpeed_Object = MibTableColumn
qtechApEthernetIfLinkSpeed = _QtechApEthernetIfLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 24),
    _QtechApEthernetIfLinkSpeed_Type()
)
qtechApEthernetIfLinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApEthernetIfLinkSpeed.setStatus("current")


class _QtechApEthernetIfPOEPower_Type(Integer32):
    """Custom type qtechApEthernetIfPOEPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("drawn", 2),
          ("notdrawn", 3))
    )


_QtechApEthernetIfPOEPower_Type.__name__ = "Integer32"
_QtechApEthernetIfPOEPower_Object = MibTableColumn
qtechApEthernetIfPOEPower = _QtechApEthernetIfPOEPower_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 25),
    _QtechApEthernetIfPOEPower_Type()
)
qtechApEthernetIfPOEPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApEthernetIfPOEPower.setStatus("current")


class _QtechApAdminStatus_Type(Integer32):
    """Custom type qtechApAdminStatus based on Integer32"""
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


_QtechApAdminStatus_Type.__name__ = "Integer32"
_QtechApAdminStatus_Object = MibTableColumn
qtechApAdminStatus = _QtechApAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 26),
    _QtechApAdminStatus_Type()
)
qtechApAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApAdminStatus.setStatus("current")
_QtechApEthernetIfRxBoardPkts_Type = Counter32
_QtechApEthernetIfRxBoardPkts_Object = MibTableColumn
qtechApEthernetIfRxBoardPkts = _QtechApEthernetIfRxBoardPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 27),
    _QtechApEthernetIfRxBoardPkts_Type()
)
qtechApEthernetIfRxBoardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApEthernetIfRxBoardPkts.setStatus("current")
if mibBuilder.loadTexts:
    qtechApEthernetIfRxBoardPkts.setUnits("packets")
_QtechApEthernetIfRxMultiPkts_Type = Counter32
_QtechApEthernetIfRxMultiPkts_Object = MibTableColumn
qtechApEthernetIfRxMultiPkts = _QtechApEthernetIfRxMultiPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 28),
    _QtechApEthernetIfRxMultiPkts_Type()
)
qtechApEthernetIfRxMultiPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApEthernetIfRxMultiPkts.setStatus("current")
if mibBuilder.loadTexts:
    qtechApEthernetIfRxMultiPkts.setUnits("packets")
_QtechApEthernetIfTxBoardPkts_Type = Counter32
_QtechApEthernetIfTxBoardPkts_Object = MibTableColumn
qtechApEthernetIfTxBoardPkts = _QtechApEthernetIfTxBoardPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 29),
    _QtechApEthernetIfTxBoardPkts_Type()
)
qtechApEthernetIfTxBoardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApEthernetIfTxBoardPkts.setStatus("current")
if mibBuilder.loadTexts:
    qtechApEthernetIfTxBoardPkts.setUnits("packets")
_QtechApEthernetIfTxMultiPkts_Type = Counter32
_QtechApEthernetIfTxMultiPkts_Object = MibTableColumn
qtechApEthernetIfTxMultiPkts = _QtechApEthernetIfTxMultiPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 30),
    _QtechApEthernetIfTxMultiPkts_Type()
)
qtechApEthernetIfTxMultiPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApEthernetIfTxMultiPkts.setStatus("current")
if mibBuilder.loadTexts:
    qtechApEthernetIfTxMultiPkts.setUnits("packets")
_QtechApEthernetIfDropPkts_Type = Counter32
_QtechApEthernetIfDropPkts_Object = MibTableColumn
qtechApEthernetIfDropPkts = _QtechApEthernetIfDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 31),
    _QtechApEthernetIfDropPkts_Type()
)
qtechApEthernetIfDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApEthernetIfDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    qtechApEthernetIfDropPkts.setUnits("packets")
_QtechApSn_Type = DisplayString
_QtechApSn_Object = MibTableColumn
qtechApSn = _QtechApSn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 32),
    _QtechApSn_Type()
)
qtechApSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApSn.setStatus("current")
_QtechApIp_Type = IpAddress
_QtechApIp_Object = MibTableColumn
qtechApIp = _QtechApIp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 33),
    _QtechApIp_Type()
)
qtechApIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIp.setStatus("current")
_QtechApStaNum_Type = Integer32
_QtechApStaNum_Object = MibTableColumn
qtechApStaNum = _QtechApStaNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 34),
    _QtechApStaNum_Type()
)
qtechApStaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApStaNum.setStatus("current")


class _QtechApToFat_Type(Integer32):
    """Custom type qtechApToFat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechApToFat_Type.__name__ = "Integer32"
_QtechApToFat_Object = MibTableColumn
qtechApToFat = _QtechApToFat_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 35),
    _QtechApToFat_Type()
)
qtechApToFat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApToFat.setStatus("current")


class _QtechApId_Type(Integer32):
    """Custom type qtechApId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 800),
    )


_QtechApId_Type.__name__ = "Integer32"
_QtechApId_Object = MibTableColumn
qtechApId = _QtechApId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 36),
    _QtechApId_Type()
)
qtechApId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApId.setStatus("current")
_QtechApSwVer_Type = DisplayString
_QtechApSwVer_Object = MibTableColumn
qtechApSwVer = _QtechApSwVer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 37),
    _QtechApSwVer_Type()
)
qtechApSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApSwVer.setStatus("current")
_QtechApBootVer_Type = DisplayString
_QtechApBootVer_Object = MibTableColumn
qtechApBootVer = _QtechApBootVer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 38),
    _QtechApBootVer_Type()
)
qtechApBootVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApBootVer.setStatus("current")
_QtechApPID_Type = DisplayString
_QtechApPID_Object = MibTableColumn
qtechApPID = _QtechApPID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 39),
    _QtechApPID_Type()
)
qtechApPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApPID.setStatus("current")
_QtechApHwVer_Type = DisplayString
_QtechApHwVer_Object = MibTableColumn
qtechApHwVer = _QtechApHwVer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 40),
    _QtechApHwVer_Type()
)
qtechApHwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApHwVer.setStatus("current")


class _QtechApStaLimit_Type(Integer32):
    """Custom type qtechApStaLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_QtechApStaLimit_Type.__name__ = "Integer32"
_QtechApStaLimit_Object = MibTableColumn
qtechApStaLimit = _QtechApStaLimit_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 41),
    _QtechApStaLimit_Type()
)
qtechApStaLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApStaLimit.setStatus("current")


class _QtechApFactoryDefault_Type(Integer32):
    """Custom type qtechApFactoryDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("reset", 1))
    )


_QtechApFactoryDefault_Type.__name__ = "Integer32"
_QtechApFactoryDefault_Object = MibTableColumn
qtechApFactoryDefault = _QtechApFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 42),
    _QtechApFactoryDefault_Type()
)
qtechApFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApFactoryDefault.setStatus("current")
_QtechApCpuUsageTrapTimer_Type = Integer32
_QtechApCpuUsageTrapTimer_Object = MibTableColumn
qtechApCpuUsageTrapTimer = _QtechApCpuUsageTrapTimer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 43),
    _QtechApCpuUsageTrapTimer_Type()
)
qtechApCpuUsageTrapTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApCpuUsageTrapTimer.setStatus("current")
_QtechApStatTrapTimer_Type = Integer32
_QtechApStatTrapTimer_Object = MibTableColumn
qtechApStatTrapTimer = _QtechApStatTrapTimer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 44),
    _QtechApStatTrapTimer_Type()
)
qtechApStatTrapTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApStatTrapTimer.setStatus("current")
_QtechApLinkOnTimeInterval_Type = Integer32
_QtechApLinkOnTimeInterval_Object = MibTableColumn
qtechApLinkOnTimeInterval = _QtechApLinkOnTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 45),
    _QtechApLinkOnTimeInterval_Type()
)
qtechApLinkOnTimeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApLinkOnTimeInterval.setStatus("current")
_QtechApNetId_Type = DisplayString
_QtechApNetId_Object = MibTableColumn
qtechApNetId = _QtechApNetId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 46),
    _QtechApNetId_Type()
)
qtechApNetId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApNetId.setStatus("current")
_QtechApUptime_Type = DisplayString
_QtechApUptime_Object = MibTableColumn
qtechApUptime = _QtechApUptime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 47),
    _QtechApUptime_Type()
)
qtechApUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApUptime.setStatus("current")
_QtechApState_Type = Integer32
_QtechApState_Object = MibTableColumn
qtechApState = _QtechApState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 48),
    _QtechApState_Type()
)
qtechApState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApState.setStatus("current")
_QtechApNasId_Type = DisplayString
_QtechApNasId_Object = MibTableColumn
qtechApNasId = _QtechApNasId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 49),
    _QtechApNasId_Type()
)
qtechApNasId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApNasId.setStatus("current")
_QtechApCoverArea_Type = Integer32
_QtechApCoverArea_Object = MibTableColumn
qtechApCoverArea = _QtechApCoverArea_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 50),
    _QtechApCoverArea_Type()
)
qtechApCoverArea.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApCoverArea.setStatus("current")
_QtechApLinkOnTimeIntervalMs_Type = TimeTicks
_QtechApLinkOnTimeIntervalMs_Object = MibTableColumn
qtechApLinkOnTimeIntervalMs = _QtechApLinkOnTimeIntervalMs_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 51),
    _QtechApLinkOnTimeIntervalMs_Type()
)
qtechApLinkOnTimeIntervalMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApLinkOnTimeIntervalMs.setStatus("current")
_QtechApUptimeMs_Type = TimeTicks
_QtechApUptimeMs_Object = MibTableColumn
qtechApUptimeMs = _QtechApUptimeMs_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 52),
    _QtechApUptimeMs_Type()
)
qtechApUptimeMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApUptimeMs.setStatus("current")
_QtechApHbUptimeMs_Type = TimeTicks
_QtechApHbUptimeMs_Object = MibTableColumn
qtechApHbUptimeMs = _QtechApHbUptimeMs_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 53),
    _QtechApHbUptimeMs_Type()
)
qtechApHbUptimeMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApHbUptimeMs.setStatus("current")
_QtechApIpv6_Type = InetAddress
_QtechApIpv6_Object = MibTableColumn
qtechApIpv6 = _QtechApIpv6_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 54),
    _QtechApIpv6_Type()
)
qtechApIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIpv6.setStatus("current")
_QtechApIpv6Prefix_Type = DisplayString
_QtechApIpv6Prefix_Object = MibTableColumn
qtechApIpv6Prefix = _QtechApIpv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 55),
    _QtechApIpv6Prefix_Type()
)
qtechApIpv6Prefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIpv6Prefix.setStatus("current")
_QtechApIpv6PrefixLen_Type = Integer32
_QtechApIpv6PrefixLen_Object = MibTableColumn
qtechApIpv6PrefixLen = _QtechApIpv6PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 56),
    _QtechApIpv6PrefixLen_Type()
)
qtechApIpv6PrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIpv6PrefixLen.setStatus("current")


class _QtechApIpv6Type_Type(Integer32):
    """Custom type qtechApIpv6Type based on Integer32"""
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
        *(("unknown", 0),
          ("unicase", 1),
          ("anycase", 2),
          ("multicase", 3))
    )


_QtechApIpv6Type_Type.__name__ = "Integer32"
_QtechApIpv6Type_Object = MibTableColumn
qtechApIpv6Type = _QtechApIpv6Type_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 57),
    _QtechApIpv6Type_Type()
)
qtechApIpv6Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIpv6Type.setStatus("current")
_QtechApIpv6Gateway_Type = DisplayString
_QtechApIpv6Gateway_Object = MibTableColumn
qtechApIpv6Gateway = _QtechApIpv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 58),
    _QtechApIpv6Gateway_Type()
)
qtechApIpv6Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIpv6Gateway.setStatus("current")
_QtechApIpv6StaNum_Type = Integer32
_QtechApIpv6StaNum_Object = MibTableColumn
qtechApIpv6StaNum = _QtechApIpv6StaNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 1, 1, 59),
    _QtechApIpv6StaNum_Type()
)
qtechApIpv6StaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIpv6StaNum.setStatus("current")
_QtechApCfgRadioTable_Object = MibTable
qtechApCfgRadioTable = _QtechApCfgRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 2)
)
if mibBuilder.loadTexts:
    qtechApCfgRadioTable.setStatus("current")
_QtechApCfgRadioEntry_Object = MibTableRow
qtechApCfgRadioEntry = _QtechApCfgRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 2, 1)
)
qtechApCfgRadioEntry.setIndexNames(
    (0, "QTECH-AC-MGMT-MIB", "qtechApMacAddr"),
    (0, "QTECH-AC-MGMT-MIB", "qtechApCfgRadioId"),
)
if mibBuilder.loadTexts:
    qtechApCfgRadioEntry.setStatus("current")


class _QtechApCfgRadioId_Type(Integer32):
    """Custom type qtechApCfgRadioId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_QtechApCfgRadioId_Type.__name__ = "Integer32"
_QtechApCfgRadioId_Object = MibTableColumn
qtechApCfgRadioId = _QtechApCfgRadioId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 2, 1, 1),
    _QtechApCfgRadioId_Type()
)
qtechApCfgRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApCfgRadioId.setStatus("current")


class _QtechApRadioEn_Type(Integer32):
    """Custom type qtechApRadioEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechApRadioEn_Type.__name__ = "Integer32"
_QtechApRadioEn_Object = MibTableColumn
qtechApRadioEn = _QtechApRadioEn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 2, 1, 2),
    _QtechApRadioEn_Type()
)
qtechApRadioEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApRadioEn.setStatus("current")


class _QtechApTxPower_Type(Integer32):
    """Custom type qtechApTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_QtechApTxPower_Type.__name__ = "Integer32"
_QtechApTxPower_Object = MibTableColumn
qtechApTxPower = _QtechApTxPower_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 2, 1, 3),
    _QtechApTxPower_Type()
)
qtechApTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApTxPower.setStatus("current")


class _QtechApDtimPeriod_Type(Integer32):
    """Custom type qtechApDtimPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_QtechApDtimPeriod_Type.__name__ = "Integer32"
_QtechApDtimPeriod_Object = MibTableColumn
qtechApDtimPeriod = _QtechApDtimPeriod_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 2, 1, 4),
    _QtechApDtimPeriod_Type()
)
qtechApDtimPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApDtimPeriod.setStatus("current")


class _QtechApBeaconPeriod_Type(Integer32):
    """Custom type qtechApBeaconPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 1000),
    )


_QtechApBeaconPeriod_Type.__name__ = "Integer32"
_QtechApBeaconPeriod_Object = MibTableColumn
qtechApBeaconPeriod = _QtechApBeaconPeriod_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 2, 1, 5),
    _QtechApBeaconPeriod_Type()
)
qtechApBeaconPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApBeaconPeriod.setStatus("current")


class _QtechApCountry_Type(DisplayString):
    """Custom type qtechApCountry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QtechApCountry_Type.__name__ = "DisplayString"
_QtechApCountry_Object = MibTableColumn
qtechApCountry = _QtechApCountry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 2, 1, 6),
    _QtechApCountry_Type()
)
qtechApCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApCountry.setStatus("current")


class _QtechApPreaShort_Type(Integer32):
    """Custom type qtechApPreaShort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechApPreaShort_Type.__name__ = "Integer32"
_QtechApPreaShort_Object = MibTableColumn
qtechApPreaShort = _QtechApPreaShort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 2, 1, 7),
    _QtechApPreaShort_Type()
)
qtechApPreaShort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApPreaShort.setStatus("current")
_QtechApRadioBssid_Type = MacAddress
_QtechApRadioBssid_Object = MibTableColumn
qtechApRadioBssid = _QtechApRadioBssid_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 2, 1, 8),
    _QtechApRadioBssid_Type()
)
qtechApRadioBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApRadioBssid.setStatus("current")


class _QtechApTxPowerLevel_Type(Integer32):
    """Custom type qtechApTxPowerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_QtechApTxPowerLevel_Type.__name__ = "Integer32"
_QtechApTxPowerLevel_Object = MibTableColumn
qtechApTxPowerLevel = _QtechApTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 2, 1, 9),
    _QtechApTxPowerLevel_Type()
)
qtechApTxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApTxPowerLevel.setStatus("current")


class _QtechApTxPowerGlobal_Type(Integer32):
    """Custom type qtechApTxPowerGlobal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechApTxPowerGlobal_Type.__name__ = "Integer32"
_QtechApTxPowerGlobal_Object = MibTableColumn
qtechApTxPowerGlobal = _QtechApTxPowerGlobal_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 2, 1, 10),
    _QtechApTxPowerGlobal_Type()
)
qtechApTxPowerGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApTxPowerGlobal.setStatus("current")


class _QtechApCurChan_Type(Integer32):
    """Custom type qtechApCurChan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 165),
    )


_QtechApCurChan_Type.__name__ = "Integer32"
_QtechApCurChan_Object = MibTableColumn
qtechApCurChan = _QtechApCurChan_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 2, 1, 11),
    _QtechApCurChan_Type()
)
qtechApCurChan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApCurChan.setStatus("current")


class _QtechApRfGlobal_Type(Integer32):
    """Custom type qtechApRfGlobal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechApRfGlobal_Type.__name__ = "Integer32"
_QtechApRfGlobal_Object = MibTableColumn
qtechApRfGlobal = _QtechApRfGlobal_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 2, 1, 12),
    _QtechApRfGlobal_Type()
)
qtechApRfGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApRfGlobal.setStatus("current")


class _QtechApRadioType_Type(Integer32):
    """Custom type qtechApRadioType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_QtechApRadioType_Type.__name__ = "Integer32"
_QtechApRadioType_Object = MibTableColumn
qtechApRadioType = _QtechApRadioType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 2, 1, 13),
    _QtechApRadioType_Type()
)
qtechApRadioType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApRadioType.setStatus("current")


class _QtechApRadio11bSup_Type(Integer32):
    """Custom type qtechApRadio11bSup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_QtechApRadio11bSup_Type.__name__ = "Integer32"
_QtechApRadio11bSup_Object = MibTableColumn
qtechApRadio11bSup = _QtechApRadio11bSup_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 2, 1, 14),
    _QtechApRadio11bSup_Type()
)
qtechApRadio11bSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApRadio11bSup.setStatus("current")
_QtechApMaxTxPower_Type = Integer32
_QtechApMaxTxPower_Object = MibTableColumn
qtechApMaxTxPower = _QtechApMaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 2, 1, 15),
    _QtechApMaxTxPower_Type()
)
qtechApMaxTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApMaxTxPower.setStatus("current")
_QtechApMinTxPower_Type = Integer32
_QtechApMinTxPower_Object = MibTableColumn
qtechApMinTxPower = _QtechApMinTxPower_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 2, 1, 16),
    _QtechApMinTxPower_Type()
)
qtechApMinTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApMinTxPower.setStatus("current")
_QtechApCurTxPower_Type = Integer32
_QtechApCurTxPower_Object = MibTableColumn
qtechApCurTxPower = _QtechApCurTxPower_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 2, 1, 17),
    _QtechApCurTxPower_Type()
)
qtechApCurTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApCurTxPower.setStatus("current")
_QtechApMaxTxPowerPer_Type = Integer32
_QtechApMaxTxPowerPer_Object = MibTableColumn
qtechApMaxTxPowerPer = _QtechApMaxTxPowerPer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 2, 1, 18),
    _QtechApMaxTxPowerPer_Type()
)
qtechApMaxTxPowerPer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApMaxTxPowerPer.setStatus("current")
_QtechApMinTxPowerPer_Type = Integer32
_QtechApMinTxPowerPer_Object = MibTableColumn
qtechApMinTxPowerPer = _QtechApMinTxPowerPer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 2, 1, 19),
    _QtechApMinTxPowerPer_Type()
)
qtechApMinTxPowerPer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApMinTxPowerPer.setStatus("current")
_QtechApRadioRateCfgTable_Object = MibTable
qtechApRadioRateCfgTable = _QtechApRadioRateCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 3)
)
if mibBuilder.loadTexts:
    qtechApRadioRateCfgTable.setStatus("current")
_QtechApRadioRateCfgEntry_Object = MibTableRow
qtechApRadioRateCfgEntry = _QtechApRadioRateCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 3, 1)
)
qtechApRadioRateCfgEntry.setIndexNames(
    (0, "QTECH-AC-MGMT-MIB", "qtechApMacAddr"),
    (0, "QTECH-AC-MGMT-MIB", "qtechApCfgRadioId"),
    (0, "QTECH-AC-MGMT-MIB", "qtechApRadioRate"),
)
if mibBuilder.loadTexts:
    qtechApRadioRateCfgEntry.setStatus("current")


class _QtechApRadioRate_Type(Integer32):
    """Custom type qtechApRadioRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_QtechApRadioRate_Type.__name__ = "Integer32"
_QtechApRadioRate_Object = MibTableColumn
qtechApRadioRate = _QtechApRadioRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 3, 1, 1),
    _QtechApRadioRate_Type()
)
qtechApRadioRate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechApRadioRate.setStatus("current")


class _QtechApRadioRateType_Type(Integer32):
    """Custom type qtechApRadioRateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_QtechApRadioRateType_Type.__name__ = "Integer32"
_QtechApRadioRateType_Object = MibTableColumn
qtechApRadioRateType = _QtechApRadioRateType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 3, 1, 2),
    _QtechApRadioRateType_Type()
)
qtechApRadioRateType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApRadioRateType.setStatus("current")
_QtechApStaticIpCfgTable_Object = MibTable
qtechApStaticIpCfgTable = _QtechApStaticIpCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 4)
)
if mibBuilder.loadTexts:
    qtechApStaticIpCfgTable.setStatus("current")
_QtechApStaticIpCfgEntry_Object = MibTableRow
qtechApStaticIpCfgEntry = _QtechApStaticIpCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 4, 1)
)
qtechApStaticIpCfgEntry.setIndexNames(
    (0, "QTECH-AC-MGMT-MIB", "qtechApMacAddr"),
)
if mibBuilder.loadTexts:
    qtechApStaticIpCfgEntry.setStatus("current")
_QtechApIpAddr_Type = IpAddress
_QtechApIpAddr_Object = MibTableColumn
qtechApIpAddr = _QtechApIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 4, 1, 1),
    _QtechApIpAddr_Type()
)
qtechApIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApIpAddr.setStatus("current")
_QtechApIpMask_Type = IpAddress
_QtechApIpMask_Object = MibTableColumn
qtechApIpMask = _QtechApIpMask_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 4, 1, 2),
    _QtechApIpMask_Type()
)
qtechApIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApIpMask.setStatus("current")
_QtechApIpGetway_Type = IpAddress
_QtechApIpGetway_Object = MibTableColumn
qtechApIpGetway = _QtechApIpGetway_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 4, 1, 3),
    _QtechApIpGetway_Type()
)
qtechApIpGetway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApIpGetway.setStatus("current")
_QtechApStaticIpRS_Type = RowStatus
_QtechApStaticIpRS_Object = MibTableColumn
qtechApStaticIpRS = _QtechApStaticIpRS_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 4, 1, 4),
    _QtechApStaticIpRS_Type()
)
qtechApStaticIpRS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApStaticIpRS.setStatus("current")
_QtechApOfflineTable_Object = MibTable
qtechApOfflineTable = _QtechApOfflineTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 5)
)
if mibBuilder.loadTexts:
    qtechApOfflineTable.setStatus("current")
_QtechApOfflineEntry_Object = MibTableRow
qtechApOfflineEntry = _QtechApOfflineEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 5, 1)
)
qtechApOfflineEntry.setIndexNames(
    (0, "QTECH-AC-MGMT-MIB", "qtechApOffMacAddr"),
)
if mibBuilder.loadTexts:
    qtechApOfflineEntry.setStatus("current")
_QtechApOfftime_Type = Integer32
_QtechApOfftime_Object = MibTableColumn
qtechApOfftime = _QtechApOfftime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 5, 1, 1),
    _QtechApOfftime_Type()
)
qtechApOfftime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApOfftime.setStatus("current")


class _QtechApOffApName_Type(DisplayString):
    """Custom type qtechApOffApName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechApOffApName_Type.__name__ = "DisplayString"
_QtechApOffApName_Object = MibTableColumn
qtechApOffApName = _QtechApOffApName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 5, 1, 2),
    _QtechApOffApName_Type()
)
qtechApOffApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApOffApName.setStatus("current")
_QtechApOffMacAddr_Type = MacAddress
_QtechApOffMacAddr_Object = MibTableColumn
qtechApOffMacAddr = _QtechApOffMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 5, 1, 3),
    _QtechApOffMacAddr_Type()
)
qtechApOffMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApOffMacAddr.setStatus("current")
_QtechApBackupStateTable_Object = MibTable
qtechApBackupStateTable = _QtechApBackupStateTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 6)
)
if mibBuilder.loadTexts:
    qtechApBackupStateTable.setStatus("current")
_QtechApBackupStateEntry_Object = MibTableRow
qtechApBackupStateEntry = _QtechApBackupStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 6, 1)
)
qtechApBackupStateEntry.setIndexNames(
    (0, "QTECH-AC-MGMT-MIB", "qtechApMacAddr"),
)
if mibBuilder.loadTexts:
    qtechApBackupStateEntry.setStatus("current")


class _QtechApBackupState_Type(Integer32):
    """Custom type qtechApBackupState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("master", 1),
          ("slave", 2))
    )


_QtechApBackupState_Type.__name__ = "Integer32"
_QtechApBackupState_Object = MibTableColumn
qtechApBackupState = _QtechApBackupState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 1, 6, 1, 1),
    _QtechApBackupState_Type()
)
qtechApBackupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApBackupState.setStatus("current")
_QtechAcMgmtApIf_ObjectIdentity = ObjectIdentity
qtechAcMgmtApIf = _QtechAcMgmtApIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 2, 2)
)
_QtechAcMgmtApgMIBObjects_ObjectIdentity = ObjectIdentity
qtechAcMgmtApgMIBObjects = _QtechAcMgmtApgMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 3)
)
_QtechAcMgmtApg_ObjectIdentity = ObjectIdentity
qtechAcMgmtApg = _QtechAcMgmtApg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 3, 1)
)
_QtechApgCfgTable_Object = MibTable
qtechApgCfgTable = _QtechApgCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 3, 1, 1)
)
if mibBuilder.loadTexts:
    qtechApgCfgTable.setStatus("current")
_QtechApgCfgEntry_Object = MibTableRow
qtechApgCfgEntry = _QtechApgCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 3, 1, 1, 1)
)
qtechApgCfgEntry.setIndexNames(
    (0, "QTECH-AC-MGMT-MIB", "qtechApgApgName"),
)
if mibBuilder.loadTexts:
    qtechApgCfgEntry.setStatus("current")


class _QtechApgApgName_Type(DisplayString):
    """Custom type qtechApgApgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_QtechApgApgName_Type.__name__ = "DisplayString"
_QtechApgApgName_Object = MibTableColumn
qtechApgApgName = _QtechApgApgName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 3, 1, 1, 1, 1),
    _QtechApgApgName_Type()
)
qtechApgApgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApgApgName.setStatus("current")


class _QtechApgDiscTimer_Type(Integer32):
    """Custom type qtechApgDiscTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 180),
    )


_QtechApgDiscTimer_Type.__name__ = "Integer32"
_QtechApgDiscTimer_Object = MibTableColumn
qtechApgDiscTimer = _QtechApgDiscTimer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 3, 1, 1, 1, 2),
    _QtechApgDiscTimer_Type()
)
qtechApgDiscTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApgDiscTimer.setStatus("current")


class _QtechApgEchoReqTimer_Type(Integer32):
    """Custom type qtechApgEchoReqTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_QtechApgEchoReqTimer_Type.__name__ = "Integer32"
_QtechApgEchoReqTimer_Object = MibTableColumn
qtechApgEchoReqTimer = _QtechApgEchoReqTimer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 3, 1, 1, 1, 3),
    _QtechApgEchoReqTimer_Type()
)
qtechApgEchoReqTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApgEchoReqTimer.setStatus("current")


class _QtechApgEroReportTimer_Type(Integer32):
    """Custom type qtechApgEroReportTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1080),
    )


_QtechApgEroReportTimer_Type.__name__ = "Integer32"
_QtechApgEroReportTimer_Object = MibTableColumn
qtechApgEroReportTimer = _QtechApgEroReportTimer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 3, 1, 1, 1, 4),
    _QtechApgEroReportTimer_Type()
)
qtechApgEroReportTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApgEroReportTimer.setStatus("current")


class _QtechApgStaTimeoutTimer_Type(Integer32):
    """Custom type qtechApgStaTimeoutTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_QtechApgStaTimeoutTimer_Type.__name__ = "Integer32"
_QtechApgStaTimeoutTimer_Object = MibTableColumn
qtechApgStaTimeoutTimer = _QtechApgStaTimeoutTimer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 3, 1, 1, 1, 5),
    _QtechApgStaTimeoutTimer_Type()
)
qtechApgStaTimeoutTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApgStaTimeoutTimer.setStatus("current")


class _QtechApgStatisticsTimer_Type(Integer32):
    """Custom type qtechApgStatisticsTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QtechApgStatisticsTimer_Type.__name__ = "Integer32"
_QtechApgStatisticsTimer_Object = MibTableColumn
qtechApgStatisticsTimer = _QtechApgStatisticsTimer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 3, 1, 1, 1, 6),
    _QtechApgStatisticsTimer_Type()
)
qtechApgStatisticsTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApgStatisticsTimer.setStatus("current")


class _QtechApgFallback_Type(Integer32):
    """Custom type qtechApgFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_QtechApgFallback_Type.__name__ = "Integer32"
_QtechApgFallback_Object = MibTableColumn
qtechApgFallback = _QtechApgFallback_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 3, 1, 1, 1, 7),
    _QtechApgFallback_Type()
)
qtechApgFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApgFallback.setStatus("current")


class _QtechApgImageId_Type(DisplayString):
    """Custom type qtechApgImageId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_QtechApgImageId_Type.__name__ = "DisplayString"
_QtechApgImageId_Object = MibTableColumn
qtechApgImageId = _QtechApgImageId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 3, 1, 1, 1, 8),
    _QtechApgImageId_Type()
)
qtechApgImageId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApgImageId.setStatus("current")


class _QtechApgCreatEn_Type(Integer32):
    """Custom type qtechApgCreatEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechApgCreatEn_Type.__name__ = "Integer32"
_QtechApgCreatEn_Object = MibTableColumn
qtechApgCreatEn = _QtechApgCreatEn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 3, 1, 1, 1, 9),
    _QtechApgCreatEn_Type()
)
qtechApgCreatEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApgCreatEn.setStatus("current")
_QtechApgCfgRadioTable_Object = MibTable
qtechApgCfgRadioTable = _QtechApgCfgRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 3, 1, 2)
)
if mibBuilder.loadTexts:
    qtechApgCfgRadioTable.setStatus("current")
_QtechApgCfgRadioEntry_Object = MibTableRow
qtechApgCfgRadioEntry = _QtechApgCfgRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 3, 1, 2, 1)
)
qtechApgCfgRadioEntry.setIndexNames(
    (0, "QTECH-AC-MGMT-MIB", "qtechApgApgName"),
    (0, "QTECH-AC-MGMT-MIB", "qtechApgEnableRadioId"),
)
if mibBuilder.loadTexts:
    qtechApgCfgRadioEntry.setStatus("current")


class _QtechApgEnableRadioId_Type(Integer32):
    """Custom type qtechApgEnableRadioId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_QtechApgEnableRadioId_Type.__name__ = "Integer32"
_QtechApgEnableRadioId_Object = MibTableColumn
qtechApgEnableRadioId = _QtechApgEnableRadioId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 3, 1, 2, 1, 1),
    _QtechApgEnableRadioId_Type()
)
qtechApgEnableRadioId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechApgEnableRadioId.setStatus("current")


class _QtechApgEnableRadioEn_Type(Integer32):
    """Custom type qtechApgEnableRadioEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechApgEnableRadioEn_Type.__name__ = "Integer32"
_QtechApgEnableRadioEn_Object = MibTableColumn
qtechApgEnableRadioEn = _QtechApgEnableRadioEn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 3, 1, 2, 1, 2),
    _QtechApgEnableRadioEn_Type()
)
qtechApgEnableRadioEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApgEnableRadioEn.setStatus("current")
_QtechApgIntfMapTable_Object = MibTable
qtechApgIntfMapTable = _QtechApgIntfMapTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 3, 1, 3)
)
if mibBuilder.loadTexts:
    qtechApgIntfMapTable.setStatus("current")
_QtechApgIntfMapEntry_Object = MibTableRow
qtechApgIntfMapEntry = _QtechApgIntfMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 3, 1, 3, 1)
)
qtechApgIntfMapEntry.setIndexNames(
    (0, "QTECH-AC-MGMT-MIB", "qtechApgApgName"),
    (0, "QTECH-AC-MGMT-MIB", "qtechApgWlanIndex"),
)
if mibBuilder.loadTexts:
    qtechApgIntfMapEntry.setStatus("current")


class _QtechApgWlanIndex_Type(Integer32):
    """Custom type qtechApgWlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_QtechApgWlanIndex_Type.__name__ = "Integer32"
_QtechApgWlanIndex_Object = MibTableColumn
qtechApgWlanIndex = _QtechApgWlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 3, 1, 3, 1, 1),
    _QtechApgWlanIndex_Type()
)
qtechApgWlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApgWlanIndex.setStatus("current")


class _QtechApgWlanId_Type(Integer32):
    """Custom type qtechApgWlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_QtechApgWlanId_Type.__name__ = "Integer32"
_QtechApgWlanId_Object = MibTableColumn
qtechApgWlanId = _QtechApgWlanId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 3, 1, 3, 1, 2),
    _QtechApgWlanId_Type()
)
qtechApgWlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApgWlanId.setStatus("current")


class _QtechApgVlanId_Type(Integer32):
    """Custom type qtechApgVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_QtechApgVlanId_Type.__name__ = "Integer32"
_QtechApgVlanId_Object = MibTableColumn
qtechApgVlanId = _QtechApgVlanId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 3, 1, 3, 1, 3),
    _QtechApgVlanId_Type()
)
qtechApgVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApgVlanId.setStatus("current")


class _QtechApgRadioId_Type(Integer32):
    """Custom type qtechApgRadioId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_QtechApgRadioId_Type.__name__ = "Integer32"
_QtechApgRadioId_Object = MibTableColumn
qtechApgRadioId = _QtechApgRadioId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 3, 1, 3, 1, 4),
    _QtechApgRadioId_Type()
)
qtechApgRadioId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApgRadioId.setStatus("current")
_QtechApgWlanIntfMapRS_Type = RowStatus
_QtechApgWlanIntfMapRS_Object = MibTableColumn
qtechApgWlanIntfMapRS = _QtechApgWlanIntfMapRS_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 3, 1, 3, 1, 5),
    _QtechApgWlanIntfMapRS_Type()
)
qtechApgWlanIntfMapRS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApgWlanIntfMapRS.setStatus("current")
_QtechAcMgmtApgIf_ObjectIdentity = ObjectIdentity
qtechAcMgmtApgIf = _QtechAcMgmtApgIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 3, 2)
)
_QtechAcMgmtWlanMIBObjects_ObjectIdentity = ObjectIdentity
qtechAcMgmtWlanMIBObjects = _QtechAcMgmtWlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 4)
)
_QtechAcMgmtWlan_ObjectIdentity = ObjectIdentity
qtechAcMgmtWlan = _QtechAcMgmtWlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 4, 1)
)
_QtechWlanCfgTable_Object = MibTable
qtechWlanCfgTable = _QtechWlanCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 4, 1, 1)
)
if mibBuilder.loadTexts:
    qtechWlanCfgTable.setStatus("current")
_QtechWlanCfgEntry_Object = MibTableRow
qtechWlanCfgEntry = _QtechWlanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 4, 1, 1, 1)
)
qtechWlanCfgEntry.setIndexNames(
    (0, "QTECH-AC-MGMT-MIB", "qtechWlanId"),
)
if mibBuilder.loadTexts:
    qtechWlanCfgEntry.setStatus("current")


class _QtechWlanId_Type(Integer32):
    """Custom type qtechWlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_QtechWlanId_Type.__name__ = "Integer32"
_QtechWlanId_Object = MibTableColumn
qtechWlanId = _QtechWlanId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 4, 1, 1, 1, 1),
    _QtechWlanId_Type()
)
qtechWlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechWlanId.setStatus("current")


class _QtechWlanShort_Type(Integer32):
    """Custom type qtechWlanShort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_QtechWlanShort_Type.__name__ = "Integer32"
_QtechWlanShort_Object = MibTableColumn
qtechWlanShort = _QtechWlanShort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 4, 1, 1, 1, 2),
    _QtechWlanShort_Type()
)
qtechWlanShort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWlanShort.setStatus("current")


class _QtechWlanSpctMgmt_Type(Integer32):
    """Custom type qtechWlanSpctMgmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechWlanSpctMgmt_Type.__name__ = "Integer32"
_QtechWlanSpctMgmt_Object = MibTableColumn
qtechWlanSpctMgmt = _QtechWlanSpctMgmt_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 4, 1, 1, 1, 3),
    _QtechWlanSpctMgmt_Type()
)
qtechWlanSpctMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWlanSpctMgmt.setStatus("current")


class _QtechWlanEnQos_Type(Integer32):
    """Custom type qtechWlanEnQos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechWlanEnQos_Type.__name__ = "Integer32"
_QtechWlanEnQos_Object = MibTableColumn
qtechWlanEnQos = _QtechWlanEnQos_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 4, 1, 1, 1, 4),
    _QtechWlanEnQos_Type()
)
qtechWlanEnQos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWlanEnQos.setStatus("current")


class _QtechWlanShortSlotTime_Type(Integer32):
    """Custom type qtechWlanShortSlotTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechWlanShortSlotTime_Type.__name__ = "Integer32"
_QtechWlanShortSlotTime_Object = MibTableColumn
qtechWlanShortSlotTime = _QtechWlanShortSlotTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 4, 1, 1, 1, 5),
    _QtechWlanShortSlotTime_Type()
)
qtechWlanShortSlotTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWlanShortSlotTime.setStatus("current")


class _QtechWlanEnableApsd_Type(Integer32):
    """Custom type qtechWlanEnableApsd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechWlanEnableApsd_Type.__name__ = "Integer32"
_QtechWlanEnableApsd_Object = MibTableColumn
qtechWlanEnableApsd = _QtechWlanEnableApsd_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 4, 1, 1, 1, 6),
    _QtechWlanEnableApsd_Type()
)
qtechWlanEnableApsd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWlanEnableApsd.setStatus("current")


class _QtechWlanAckType_Type(Integer32):
    """Custom type qtechWlanAckType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechWlanAckType_Type.__name__ = "Integer32"
_QtechWlanAckType_Object = MibTableColumn
qtechWlanAckType = _QtechWlanAckType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 4, 1, 1, 1, 7),
    _QtechWlanAckType_Type()
)
qtechWlanAckType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWlanAckType.setStatus("current")


class _QtechWlanTunnelType_Type(Integer32):
    """Custom type qtechWlanTunnelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_QtechWlanTunnelType_Type.__name__ = "Integer32"
_QtechWlanTunnelType_Object = MibTableColumn
qtechWlanTunnelType = _QtechWlanTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 4, 1, 1, 1, 8),
    _QtechWlanTunnelType_Type()
)
qtechWlanTunnelType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWlanTunnelType.setStatus("current")


class _QtechWlanBroadSsid_Type(Integer32):
    """Custom type qtechWlanBroadSsid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechWlanBroadSsid_Type.__name__ = "Integer32"
_QtechWlanBroadSsid_Object = MibTableColumn
qtechWlanBroadSsid = _QtechWlanBroadSsid_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 4, 1, 1, 1, 9),
    _QtechWlanBroadSsid_Type()
)
qtechWlanBroadSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWlanBroadSsid.setStatus("current")


class _QtechWlanRts_Type(Integer32):
    """Custom type qtechWlanRts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QtechWlanRts_Type.__name__ = "Integer32"
_QtechWlanRts_Object = MibTableColumn
qtechWlanRts = _QtechWlanRts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 4, 1, 1, 1, 10),
    _QtechWlanRts_Type()
)
qtechWlanRts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWlanRts.setStatus("current")


class _QtechWlanShortTry_Type(Integer32):
    """Custom type qtechWlanShortTry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QtechWlanShortTry_Type.__name__ = "Integer32"
_QtechWlanShortTry_Object = MibTableColumn
qtechWlanShortTry = _QtechWlanShortTry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 4, 1, 1, 1, 11),
    _QtechWlanShortTry_Type()
)
qtechWlanShortTry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWlanShortTry.setStatus("current")


class _QtechWlanLongTry_Type(Integer32):
    """Custom type qtechWlanLongTry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QtechWlanLongTry_Type.__name__ = "Integer32"
_QtechWlanLongTry_Object = MibTableColumn
qtechWlanLongTry = _QtechWlanLongTry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 4, 1, 1, 1, 12),
    _QtechWlanLongTry_Type()
)
qtechWlanLongTry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWlanLongTry.setStatus("current")
_QtechWlanStaNum_Type = Integer32
_QtechWlanStaNum_Object = MibTableColumn
qtechWlanStaNum = _QtechWlanStaNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 4, 1, 1, 1, 13),
    _QtechWlanStaNum_Type()
)
qtechWlanStaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechWlanStaNum.setStatus("current")
_QtechWlanNasId_Type = DisplayString
_QtechWlanNasId_Object = MibTableColumn
qtechWlanNasId = _QtechWlanNasId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 4, 1, 1, 1, 14),
    _QtechWlanNasId_Type()
)
qtechWlanNasId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWlanNasId.setStatus("current")
_QtechWlanWlanCreatTable_Object = MibTable
qtechWlanWlanCreatTable = _QtechWlanWlanCreatTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 4, 1, 2)
)
if mibBuilder.loadTexts:
    qtechWlanWlanCreatTable.setStatus("current")
_QtechWlanWlanCreatEntry_Object = MibTableRow
qtechWlanWlanCreatEntry = _QtechWlanWlanCreatEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 4, 1, 2, 1)
)
qtechWlanWlanCreatEntry.setIndexNames(
    (0, "QTECH-AC-MGMT-MIB", "qtechWlanId"),
)
if mibBuilder.loadTexts:
    qtechWlanWlanCreatEntry.setStatus("current")


class _QtechWlanWlanSsid_Type(DisplayString):
    """Custom type qtechWlanWlanSsid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_QtechWlanWlanSsid_Type.__name__ = "DisplayString"
_QtechWlanWlanSsid_Object = MibTableColumn
qtechWlanWlanSsid = _QtechWlanWlanSsid_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 4, 1, 2, 1, 1),
    _QtechWlanWlanSsid_Type()
)
qtechWlanWlanSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWlanWlanSsid.setStatus("current")


class _QtechWlanWlanProfile_Type(DisplayString):
    """Custom type qtechWlanWlanProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_QtechWlanWlanProfile_Type.__name__ = "DisplayString"
_QtechWlanWlanProfile_Object = MibTableColumn
qtechWlanWlanProfile = _QtechWlanWlanProfile_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 4, 1, 2, 1, 2),
    _QtechWlanWlanProfile_Type()
)
qtechWlanWlanProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWlanWlanProfile.setStatus("current")
_QtechWlanCreateMapRS_Type = RowStatus
_QtechWlanCreateMapRS_Object = MibTableColumn
qtechWlanCreateMapRS = _QtechWlanCreateMapRS_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 4, 1, 2, 1, 3),
    _QtechWlanCreateMapRS_Type()
)
qtechWlanCreateMapRS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWlanCreateMapRS.setStatus("current")
_QtechWlanChanBandTable_Object = MibTable
qtechWlanChanBandTable = _QtechWlanChanBandTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 4, 1, 3)
)
if mibBuilder.loadTexts:
    qtechWlanChanBandTable.setStatus("current")
_QtechWlanChanBandEntry_Object = MibTableRow
qtechWlanChanBandEntry = _QtechWlanChanBandEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 4, 1, 3, 1)
)
qtechWlanChanBandEntry.setIndexNames(
    (0, "QTECH-AC-MGMT-MIB", "qtechWlanId"),
    (0, "QTECH-AC-MGMT-MIB", "qtechWlanBandV"),
)
if mibBuilder.loadTexts:
    qtechWlanChanBandEntry.setStatus("current")


class _QtechWlanBandV_Type(Integer32):
    """Custom type qtechWlanBandV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_QtechWlanBandV_Type.__name__ = "Integer32"
_QtechWlanBandV_Object = MibTableColumn
qtechWlanBandV = _QtechWlanBandV_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 4, 1, 3, 1, 1),
    _QtechWlanBandV_Type()
)
qtechWlanBandV.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechWlanBandV.setStatus("current")


class _QtechWlanChanV_Type(Integer32):
    """Custom type qtechWlanChanV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QtechWlanChanV_Type.__name__ = "Integer32"
_QtechWlanChanV_Object = MibTableColumn
qtechWlanChanV = _QtechWlanChanV_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 4, 1, 3, 1, 2),
    _QtechWlanChanV_Type()
)
qtechWlanChanV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWlanChanV.setStatus("current")


class _QtechWlanChanBandEn_Type(Integer32):
    """Custom type qtechWlanChanBandEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechWlanChanBandEn_Type.__name__ = "Integer32"
_QtechWlanChanBandEn_Object = MibTableColumn
qtechWlanChanBandEn = _QtechWlanChanBandEn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 4, 1, 3, 1, 3),
    _QtechWlanChanBandEn_Type()
)
qtechWlanChanBandEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWlanChanBandEn.setStatus("current")
_QtechWlanChanBandRS_Type = RowStatus
_QtechWlanChanBandRS_Object = MibTableColumn
qtechWlanChanBandRS = _QtechWlanChanBandRS_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 4, 1, 3, 1, 4),
    _QtechWlanChanBandRS_Type()
)
qtechWlanChanBandRS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWlanChanBandRS.setStatus("current")
_QtechWlanLimitChanTable_Object = MibTable
qtechWlanLimitChanTable = _QtechWlanLimitChanTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 4, 1, 4)
)
if mibBuilder.loadTexts:
    qtechWlanLimitChanTable.setStatus("current")
_QtechWlanLimitChanEntry_Object = MibTableRow
qtechWlanLimitChanEntry = _QtechWlanLimitChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 4, 1, 4, 1)
)
qtechWlanLimitChanEntry.setIndexNames(
    (0, "QTECH-AC-MGMT-MIB", "qtechWlanId"),
)
if mibBuilder.loadTexts:
    qtechWlanLimitChanEntry.setStatus("current")


class _QtechWlanLimitChanFirstV_Type(Integer32):
    """Custom type qtechWlanLimitChanFirstV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QtechWlanLimitChanFirstV_Type.__name__ = "Integer32"
_QtechWlanLimitChanFirstV_Object = MibTableColumn
qtechWlanLimitChanFirstV = _QtechWlanLimitChanFirstV_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 4, 1, 4, 1, 1),
    _QtechWlanLimitChanFirstV_Type()
)
qtechWlanLimitChanFirstV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWlanLimitChanFirstV.setStatus("current")


class _QtechWlanLimitChanNumV_Type(Integer32):
    """Custom type qtechWlanLimitChanNumV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_QtechWlanLimitChanNumV_Type.__name__ = "Integer32"
_QtechWlanLimitChanNumV_Object = MibTableColumn
qtechWlanLimitChanNumV = _QtechWlanLimitChanNumV_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 4, 1, 4, 1, 2),
    _QtechWlanLimitChanNumV_Type()
)
qtechWlanLimitChanNumV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWlanLimitChanNumV.setStatus("current")


class _QtechWlanLimitChanMaxTxPowerLv_Type(Integer32):
    """Custom type qtechWlanLimitChanMaxTxPowerLv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_QtechWlanLimitChanMaxTxPowerLv_Type.__name__ = "Integer32"
_QtechWlanLimitChanMaxTxPowerLv_Object = MibTableColumn
qtechWlanLimitChanMaxTxPowerLv = _QtechWlanLimitChanMaxTxPowerLv_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 4, 1, 4, 1, 3),
    _QtechWlanLimitChanMaxTxPowerLv_Type()
)
qtechWlanLimitChanMaxTxPowerLv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWlanLimitChanMaxTxPowerLv.setStatus("current")
_QtechWlanLimitChanRS_Type = RowStatus
_QtechWlanLimitChanRS_Object = MibTableColumn
qtechWlanLimitChanRS = _QtechWlanLimitChanRS_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 4, 1, 4, 1, 4),
    _QtechWlanLimitChanRS_Type()
)
qtechWlanLimitChanRS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWlanLimitChanRS.setStatus("current")
_QtechAcMgmtWlanIf_ObjectIdentity = ObjectIdentity
qtechAcMgmtWlanIf = _QtechAcMgmtWlanIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 4, 2)
)
_QtechAcMgmtStaMIBObjects_ObjectIdentity = ObjectIdentity
qtechAcMgmtStaMIBObjects = _QtechAcMgmtStaMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 5)
)
_QtechAcMgmtSta_ObjectIdentity = ObjectIdentity
qtechAcMgmtSta = _QtechAcMgmtSta_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 5, 1)
)
_QtechStaTable_Object = MibTable
qtechStaTable = _QtechStaTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 5, 1, 1)
)
if mibBuilder.loadTexts:
    qtechStaTable.setStatus("current")
_QtechStaEntry_Object = MibTableRow
qtechStaEntry = _QtechStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 5, 1, 1, 1)
)
qtechStaEntry.setIndexNames(
    (0, "QTECH-AC-MGMT-MIB", "qtechStaMacAddr"),
)
if mibBuilder.loadTexts:
    qtechStaEntry.setStatus("current")
_QtechStaMacAddr_Type = MacAddress
_QtechStaMacAddr_Object = MibTableColumn
qtechStaMacAddr = _QtechStaMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 5, 1, 1, 1, 1),
    _QtechStaMacAddr_Type()
)
qtechStaMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaMacAddr.setStatus("current")
_QtechStaApMacAddr_Type = MacAddress
_QtechStaApMacAddr_Object = MibTableColumn
qtechStaApMacAddr = _QtechStaApMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 5, 1, 1, 1, 2),
    _QtechStaApMacAddr_Type()
)
qtechStaApMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaApMacAddr.setStatus("current")
_QtechStaVlan_Type = Integer32
_QtechStaVlan_Object = MibTableColumn
qtechStaVlan = _QtechStaVlan_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 5, 1, 1, 1, 3),
    _QtechStaVlan_Type()
)
qtechStaVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaVlan.setStatus("current")
_QtechStaWlanId_Type = Integer32
_QtechStaWlanId_Object = MibTableColumn
qtechStaWlanId = _QtechStaWlanId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 5, 1, 1, 1, 4),
    _QtechStaWlanId_Type()
)
qtechStaWlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaWlanId.setStatus("current")
_QtechStaIp_Type = IpAddress
_QtechStaIp_Object = MibTableColumn
qtechStaIp = _QtechStaIp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 5, 1, 1, 1, 5),
    _QtechStaIp_Type()
)
qtechStaIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaIp.setStatus("current")
_QtechStaApIp_Type = IpAddress
_QtechStaApIp_Object = MibTableColumn
qtechStaApIp = _QtechStaApIp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 5, 1, 1, 1, 6),
    _QtechStaApIp_Type()
)
qtechStaApIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaApIp.setStatus("current")
_QtechStaApRadioId_Type = Integer32
_QtechStaApRadioId_Object = MibTableColumn
qtechStaApRadioId = _QtechStaApRadioId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 5, 1, 1, 1, 7),
    _QtechStaApRadioId_Type()
)
qtechStaApRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaApRadioId.setStatus("current")
_QtechStaApRadioType_Type = Integer32
_QtechStaApRadioType_Object = MibTableColumn
qtechStaApRadioType = _QtechStaApRadioType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 5, 1, 1, 1, 8),
    _QtechStaApRadioType_Type()
)
qtechStaApRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaApRadioType.setStatus("current")
_QtechStaAssoType_Type = Integer32
_QtechStaAssoType_Object = MibTableColumn
qtechStaAssoType = _QtechStaAssoType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 5, 1, 1, 1, 9),
    _QtechStaAssoType_Type()
)
qtechStaAssoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaAssoType.setStatus("current")
_QtechStaAuthType_Type = Integer32
_QtechStaAuthType_Object = MibTableColumn
qtechStaAuthType = _QtechStaAuthType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 5, 1, 1, 1, 10),
    _QtechStaAuthType_Type()
)
qtechStaAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaAuthType.setStatus("current")
_QtechStaRoamTimesPerMin_Type = Integer32
_QtechStaRoamTimesPerMin_Object = MibTableColumn
qtechStaRoamTimesPerMin = _QtechStaRoamTimesPerMin_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 5, 1, 1, 1, 11),
    _QtechStaRoamTimesPerMin_Type()
)
qtechStaRoamTimesPerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaRoamTimesPerMin.setStatus("current")
_QtechStaOnTimesPerHour_Type = Integer32
_QtechStaOnTimesPerHour_Object = MibTableColumn
qtechStaOnTimesPerHour = _QtechStaOnTimesPerHour_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 5, 1, 1, 1, 12),
    _QtechStaOnTimesPerHour_Type()
)
qtechStaOnTimesPerHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaOnTimesPerHour.setStatus("current")
_QtechStaOffTimesPerHour_Type = Integer32
_QtechStaOffTimesPerHour_Object = MibTableColumn
qtechStaOffTimesPerHour = _QtechStaOffTimesPerHour_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 5, 1, 1, 1, 13),
    _QtechStaOffTimesPerHour_Type()
)
qtechStaOffTimesPerHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaOffTimesPerHour.setStatus("current")
_QtechStaIpv6_Type = InetAddress
_QtechStaIpv6_Object = MibTableColumn
qtechStaIpv6 = _QtechStaIpv6_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 5, 1, 1, 1, 14),
    _QtechStaIpv6_Type()
)
qtechStaIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaIpv6.setStatus("current")


class _QtechStaAssoAuthMode_Type(Integer32):
    """Custom type qtechStaAssoAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("open", 0),
          ("wep", 1),
          ("dot1x-wep", 2),
          ("dot1x-wpa", 3),
          ("dot1x-wpa2", 4),
          ("mab", 5),
          ("psk-wpa", 6),
          ("psk-wpa2", 7),
          ("wapi", 8))
    )


_QtechStaAssoAuthMode_Type.__name__ = "Integer32"
_QtechStaAssoAuthMode_Object = MibTableColumn
qtechStaAssoAuthMode = _QtechStaAssoAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 5, 1, 1, 1, 15),
    _QtechStaAssoAuthMode_Type()
)
qtechStaAssoAuthMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaAssoAuthMode.setStatus("current")


class _QtechStaNetAuthMode_Type(Integer32):
    """Custom type qtechStaNetAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("open", 0),
          ("web", 1))
    )


_QtechStaNetAuthMode_Type.__name__ = "Integer32"
_QtechStaNetAuthMode_Object = MibTableColumn
qtechStaNetAuthMode = _QtechStaNetAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 5, 1, 1, 1, 16),
    _QtechStaNetAuthMode_Type()
)
qtechStaNetAuthMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaNetAuthMode.setStatus("current")
_QtechStaSsid_Type = DisplayString
_QtechStaSsid_Object = MibTableColumn
qtechStaSsid = _QtechStaSsid_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 5, 1, 1, 1, 17),
    _QtechStaSsid_Type()
)
qtechStaSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaSsid.setStatus("current")
_QtechStaLinkRate_Type = Integer32
_QtechStaLinkRate_Object = MibTableColumn
qtechStaLinkRate = _QtechStaLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 5, 1, 1, 1, 18),
    _QtechStaLinkRate_Type()
)
qtechStaLinkRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaLinkRate.setStatus("current")
_QtechStaCurChan_Type = Integer32
_QtechStaCurChan_Object = MibTableColumn
qtechStaCurChan = _QtechStaCurChan_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 5, 1, 1, 1, 19),
    _QtechStaCurChan_Type()
)
qtechStaCurChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaCurChan.setStatus("current")


class _QtechStaClientType_Type(DisplayString):
    """Custom type qtechStaClientType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_QtechStaClientType_Type.__name__ = "DisplayString"
_QtechStaClientType_Object = MibTableColumn
qtechStaClientType = _QtechStaClientType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 5, 1, 1, 1, 20),
    _QtechStaClientType_Type()
)
qtechStaClientType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaClientType.setStatus("current")
_QtechStaRssi_Type = Integer32
_QtechStaRssi_Object = MibTableColumn
qtechStaRssi = _QtechStaRssi_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 5, 1, 1, 1, 21),
    _QtechStaRssi_Type()
)
qtechStaRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaRssi.setStatus("current")
_QtechStaUserName_Type = DisplayString
_QtechStaUserName_Object = MibTableColumn
qtechStaUserName = _QtechStaUserName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 5, 1, 1, 1, 22),
    _QtechStaUserName_Type()
)
qtechStaUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaUserName.setStatus("current")
_QtechStaTerminalType_Type = DisplayString
_QtechStaTerminalType_Object = MibTableColumn
qtechStaTerminalType = _QtechStaTerminalType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 5, 1, 1, 1, 23),
    _QtechStaTerminalType_Type()
)
qtechStaTerminalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaTerminalType.setStatus("current")
_QtechStaOnlineTime_Type = DisplayString
_QtechStaOnlineTime_Object = MibTableColumn
qtechStaOnlineTime = _QtechStaOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 5, 1, 1, 1, 24),
    _QtechStaOnlineTime_Type()
)
qtechStaOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaOnlineTime.setStatus("current")
_QtechStaUpTimeInterval_Type = Integer32
_QtechStaUpTimeInterval_Object = MibTableColumn
qtechStaUpTimeInterval = _QtechStaUpTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 5, 1, 1, 1, 25),
    _QtechStaUpTimeInterval_Type()
)
qtechStaUpTimeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaUpTimeInterval.setStatus("current")
_QtechAcMgmtStaIf_ObjectIdentity = ObjectIdentity
qtechAcMgmtStaIf = _QtechAcMgmtStaIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 5, 2)
)
_QtechAcMgmtNotificationsMIBObjects_ObjectIdentity = ObjectIdentity
qtechAcMgmtNotificationsMIBObjects = _QtechAcMgmtNotificationsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6)
)
_QtechAcMgmtNtfObjects_ObjectIdentity = ObjectIdentity
qtechAcMgmtNtfObjects = _QtechAcMgmtNtfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 1)
)
_QtechNotifyApMac_Type = MacAddress
_QtechNotifyApMac_Object = MibScalar
qtechNotifyApMac = _QtechNotifyApMac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 1, 1),
    _QtechNotifyApMac_Type()
)
qtechNotifyApMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechNotifyApMac.setStatus("current")
_QtechNotifyStaMac_Type = MacAddress
_QtechNotifyStaMac_Object = MibScalar
qtechNotifyStaMac = _QtechNotifyStaMac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 1, 2),
    _QtechNotifyStaMac_Type()
)
qtechNotifyStaMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechNotifyStaMac.setStatus("current")
_QtechNotifyApIp_Type = IpAddress
_QtechNotifyApIp_Object = MibScalar
qtechNotifyApIp = _QtechNotifyApIp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 1, 3),
    _QtechNotifyApIp_Type()
)
qtechNotifyApIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechNotifyApIp.setStatus("current")
_QtechNotifyStaIp_Type = IpAddress
_QtechNotifyStaIp_Object = MibScalar
qtechNotifyStaIp = _QtechNotifyStaIp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 1, 4),
    _QtechNotifyStaIp_Type()
)
qtechNotifyStaIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechNotifyStaIp.setStatus("current")
_QtechNotifyStaOperType_Type = Integer32
_QtechNotifyStaOperType_Object = MibScalar
qtechNotifyStaOperType = _QtechNotifyStaOperType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 1, 5),
    _QtechNotifyStaOperType_Type()
)
qtechNotifyStaOperType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechNotifyStaOperType.setStatus("current")


class _QtechNotifyStaApRadioId_Type(Integer32):
    """Custom type qtechNotifyStaApRadioId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_QtechNotifyStaApRadioId_Type.__name__ = "Integer32"
_QtechNotifyStaApRadioId_Object = MibScalar
qtechNotifyStaApRadioId = _QtechNotifyStaApRadioId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 1, 6),
    _QtechNotifyStaApRadioId_Type()
)
qtechNotifyStaApRadioId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechNotifyStaApRadioId.setStatus("current")


class _QtechNotifyStaApRadioType_Type(Integer32):
    """Custom type qtechNotifyStaApRadioType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_QtechNotifyStaApRadioType_Type.__name__ = "Integer32"
_QtechNotifyStaApRadioType_Object = MibScalar
qtechNotifyStaApRadioType = _QtechNotifyStaApRadioType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 1, 7),
    _QtechNotifyStaApRadioType_Type()
)
qtechNotifyStaApRadioType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechNotifyStaApRadioType.setStatus("current")


class _QtechNotifyStaVlanId_Type(Integer32):
    """Custom type qtechNotifyStaVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_QtechNotifyStaVlanId_Type.__name__ = "Integer32"
_QtechNotifyStaVlanId_Object = MibScalar
qtechNotifyStaVlanId = _QtechNotifyStaVlanId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 1, 8),
    _QtechNotifyStaVlanId_Type()
)
qtechNotifyStaVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechNotifyStaVlanId.setStatus("current")


class _QtechNotifyStaWlanId_Type(Integer32):
    """Custom type qtechNotifyStaWlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_QtechNotifyStaWlanId_Type.__name__ = "Integer32"
_QtechNotifyStaWlanId_Object = MibScalar
qtechNotifyStaWlanId = _QtechNotifyStaWlanId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 1, 9),
    _QtechNotifyStaWlanId_Type()
)
qtechNotifyStaWlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechNotifyStaWlanId.setStatus("current")


class _QtechNotifyAcMBChangeV_Type(Integer32):
    """Custom type qtechNotifyAcMBChangeV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_QtechNotifyAcMBChangeV_Type.__name__ = "Integer32"
_QtechNotifyAcMBChangeV_Object = MibScalar
qtechNotifyAcMBChangeV = _QtechNotifyAcMBChangeV_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 1, 10),
    _QtechNotifyAcMBChangeV_Type()
)
qtechNotifyAcMBChangeV.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechNotifyAcMBChangeV.setStatus("current")


class _QtechNotifyStaOperTimes_Type(Integer32):
    """Custom type qtechNotifyStaOperTimes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QtechNotifyStaOperTimes_Type.__name__ = "Integer32"
_QtechNotifyStaOperTimes_Object = MibScalar
qtechNotifyStaOperTimes = _QtechNotifyStaOperTimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 1, 11),
    _QtechNotifyStaOperTimes_Type()
)
qtechNotifyStaOperTimes.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechNotifyStaOperTimes.setStatus("current")
_QtechNotifyAcPowerIndex_Type = Integer32
_QtechNotifyAcPowerIndex_Object = MibScalar
qtechNotifyAcPowerIndex = _QtechNotifyAcPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 1, 12),
    _QtechNotifyAcPowerIndex_Type()
)
qtechNotifyAcPowerIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechNotifyAcPowerIndex.setStatus("current")
_QtechNotifyAcPowerStatu_Type = Integer32
_QtechNotifyAcPowerStatu_Object = MibScalar
qtechNotifyAcPowerStatu = _QtechNotifyAcPowerStatu_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 1, 13),
    _QtechNotifyAcPowerStatu_Type()
)
qtechNotifyAcPowerStatu.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechNotifyAcPowerStatu.setStatus("current")
_QtechNotifyTime_Type = DisplayString
_QtechNotifyTime_Object = MibScalar
qtechNotifyTime = _QtechNotifyTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 1, 14),
    _QtechNotifyTime_Type()
)
qtechNotifyTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechNotifyTime.setStatus("current")
_QtechNotifyOldVer_Type = DisplayString
_QtechNotifyOldVer_Object = MibScalar
qtechNotifyOldVer = _QtechNotifyOldVer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 1, 15),
    _QtechNotifyOldVer_Type()
)
qtechNotifyOldVer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechNotifyOldVer.setStatus("current")
_QtechNotifyNewVer_Type = DisplayString
_QtechNotifyNewVer_Object = MibScalar
qtechNotifyNewVer = _QtechNotifyNewVer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 1, 16),
    _QtechNotifyNewVer_Type()
)
qtechNotifyNewVer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechNotifyNewVer.setStatus("current")


class _QtechNotifyVerUpdtReason_Type(Integer32):
    """Custom type qtechNotifyVerUpdtReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_QtechNotifyVerUpdtReason_Type.__name__ = "Integer32"
_QtechNotifyVerUpdtReason_Object = MibScalar
qtechNotifyVerUpdtReason = _QtechNotifyVerUpdtReason_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 1, 17),
    _QtechNotifyVerUpdtReason_Type()
)
qtechNotifyVerUpdtReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechNotifyVerUpdtReason.setStatus("current")
_QtechNotifyStaIpv6_Type = InetAddress
_QtechNotifyStaIpv6_Object = MibScalar
qtechNotifyStaIpv6 = _QtechNotifyStaIpv6_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 1, 18),
    _QtechNotifyStaIpv6_Type()
)
qtechNotifyStaIpv6.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechNotifyStaIpv6.setStatus("current")


class _QtechNotifyStaAssoAuthMode_Type(Integer32):
    """Custom type qtechNotifyStaAssoAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("open", 0),
          ("wep", 1),
          ("dot1x-wep", 2),
          ("dot1x-wpa", 3),
          ("dot1x-wpa2", 4),
          ("mab", 5),
          ("psk-wpa", 6),
          ("psk-wpa2", 7),
          ("wapi", 8))
    )


_QtechNotifyStaAssoAuthMode_Type.__name__ = "Integer32"
_QtechNotifyStaAssoAuthMode_Object = MibScalar
qtechNotifyStaAssoAuthMode = _QtechNotifyStaAssoAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 1, 19),
    _QtechNotifyStaAssoAuthMode_Type()
)
qtechNotifyStaAssoAuthMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechNotifyStaAssoAuthMode.setStatus("current")


class _QtechNotifyStaNetAuthMode_Type(Integer32):
    """Custom type qtechNotifyStaNetAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("open", 0),
          ("web", 1))
    )


_QtechNotifyStaNetAuthMode_Type.__name__ = "Integer32"
_QtechNotifyStaNetAuthMode_Object = MibScalar
qtechNotifyStaNetAuthMode = _QtechNotifyStaNetAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 1, 20),
    _QtechNotifyStaNetAuthMode_Type()
)
qtechNotifyStaNetAuthMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechNotifyStaNetAuthMode.setStatus("current")
_QtechNotifyStaSsid_Type = DisplayString
_QtechNotifyStaSsid_Object = MibScalar
qtechNotifyStaSsid = _QtechNotifyStaSsid_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 1, 21),
    _QtechNotifyStaSsid_Type()
)
qtechNotifyStaSsid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechNotifyStaSsid.setStatus("current")
_QtechNotifyStaLinkRate_Type = Integer32
_QtechNotifyStaLinkRate_Object = MibScalar
qtechNotifyStaLinkRate = _QtechNotifyStaLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 1, 22),
    _QtechNotifyStaLinkRate_Type()
)
qtechNotifyStaLinkRate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechNotifyStaLinkRate.setStatus("current")
_QtechNotifyStaCurChan_Type = Integer32
_QtechNotifyStaCurChan_Object = MibScalar
qtechNotifyStaCurChan = _QtechNotifyStaCurChan_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 1, 23),
    _QtechNotifyStaCurChan_Type()
)
qtechNotifyStaCurChan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechNotifyStaCurChan.setStatus("current")
_QtechNotifyStaClientType_Type = DisplayString
_QtechNotifyStaClientType_Object = MibScalar
qtechNotifyStaClientType = _QtechNotifyStaClientType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 1, 24),
    _QtechNotifyStaClientType_Type()
)
qtechNotifyStaClientType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechNotifyStaClientType.setStatus("current")
_QtechNotifyStaRssi_Type = Integer32
_QtechNotifyStaRssi_Object = MibScalar
qtechNotifyStaRssi = _QtechNotifyStaRssi_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 1, 25),
    _QtechNotifyStaRssi_Type()
)
qtechNotifyStaRssi.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechNotifyStaRssi.setStatus("current")
_QtechNotifyStaReason_Type = DisplayString
_QtechNotifyStaReason_Object = MibScalar
qtechNotifyStaReason = _QtechNotifyStaReason_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 1, 26),
    _QtechNotifyStaReason_Type()
)
qtechNotifyStaReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechNotifyStaReason.setStatus("current")
_QtechNotifyStaTimestamp_Type = Integer32
_QtechNotifyStaTimestamp_Object = MibScalar
qtechNotifyStaTimestamp = _QtechNotifyStaTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 1, 27),
    _QtechNotifyStaTimestamp_Type()
)
qtechNotifyStaTimestamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechNotifyStaTimestamp.setStatus("current")
_QtechNotifyStaOnlineTimeval_Type = Integer32
_QtechNotifyStaOnlineTimeval_Object = MibScalar
qtechNotifyStaOnlineTimeval = _QtechNotifyStaOnlineTimeval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 1, 28),
    _QtechNotifyStaOnlineTimeval_Type()
)
qtechNotifyStaOnlineTimeval.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechNotifyStaOnlineTimeval.setStatus("current")
_QtechNotifyStaIpv4Upflow_Type = Integer32
_QtechNotifyStaIpv4Upflow_Object = MibScalar
qtechNotifyStaIpv4Upflow = _QtechNotifyStaIpv4Upflow_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 1, 29),
    _QtechNotifyStaIpv4Upflow_Type()
)
qtechNotifyStaIpv4Upflow.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechNotifyStaIpv4Upflow.setStatus("current")
_QtechNotifyStaIpv4Downflow_Type = Integer32
_QtechNotifyStaIpv4Downflow_Object = MibScalar
qtechNotifyStaIpv4Downflow = _QtechNotifyStaIpv4Downflow_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 1, 30),
    _QtechNotifyStaIpv4Downflow_Type()
)
qtechNotifyStaIpv4Downflow.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechNotifyStaIpv4Downflow.setStatus("current")
_QtechAcMgmtNotifications_ObjectIdentity = ObjectIdentity
qtechAcMgmtNotifications = _QtechAcMgmtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 2)
)
_QtechAcMgmtAcMIBConformance_ObjectIdentity = ObjectIdentity
qtechAcMgmtAcMIBConformance = _QtechAcMgmtAcMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 7)
)
_QtechAcMgmtAcMIBCompliances_ObjectIdentity = ObjectIdentity
qtechAcMgmtAcMIBCompliances = _QtechAcMgmtAcMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 7, 1)
)
_QtechAcMgmtAcMIBGroups_ObjectIdentity = ObjectIdentity
qtechAcMgmtAcMIBGroups = _QtechAcMgmtAcMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 7, 2)
)

# Managed Objects groups

qtechAcMgmtAcMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 7, 2, 1)
)
qtechAcMgmtAcMIBGroup.setObjects(
      *(("QTECH-AC-MGMT-MIB", "qtechAcStaLimit"),
        ("QTECH-AC-MGMT-MIB", "qtechAcWtpLimit"),
        ("QTECH-AC-MGMT-MIB", "qtechAcRMacField"),
        ("QTECH-AC-MGMT-MIB", "qtechAcDataDtls"),
        ("QTECH-AC-MGMT-MIB", "qtechAcEcnSupport"),
        ("QTECH-AC-MGMT-MIB", "qtechAcBackAcIp"),
        ("QTECH-AC-MGMT-MIB", "qtechAcMtu"),
        ("QTECH-AC-MGMT-MIB", "qtechAcAcName"),
        ("QTECH-AC-MGMT-MIB", "qtechAcLocation"),
        ("QTECH-AC-MGMT-MIB", "qtechAcResetAp"),
        ("QTECH-AC-MGMT-MIB", "qtechAcApNum"),
        ("QTECH-AC-MGMT-MIB", "qtechAc80211aRateType"),
        ("QTECH-AC-MGMT-MIB", "qtechAc80211bRateType"),
        ("QTECH-AC-MGMT-MIB", "qtechAcFallback"),
        ("QTECH-AC-MGMT-MIB", "qtechAcStaNum"),
        ("QTECH-AC-MGMT-MIB", "qtechAcMacAddr"),
        ("QTECH-AC-MGMT-MIB", "qtechAcDescriptor"),
        ("QTECH-AC-MGMT-MIB", "qtechAcPID"),
        ("QTECH-AC-MGMT-MIB", "qtechAcHwId"),
        ("QTECH-AC-MGMT-MIB", "qtechAcSN"),
        ("QTECH-AC-MGMT-MIB", "qtechAcTemp"),
        ("QTECH-AC-MGMT-MIB", "qtechAcAPUpDownCtrl"),
        ("QTECH-AC-MGMT-MIB", "qtechAcAPJoinFailCtrl"),
        ("QTECH-AC-MGMT-MIB", "qtechAcAPDecryEroReportCtrl"),
        ("QTECH-AC-MGMT-MIB", "qtechAcApImageUpdtCtrl"),
        ("QTECH-AC-MGMT-MIB", "qtechAcApConfigMsgEroCtrl"),
        ("QTECH-AC-MGMT-MIB", "qtechAcApRadioOperStatuCtrl"),
        ("QTECH-AC-MGMT-MIB", "qtechAcApAuthenFailCtrl"),
        ("QTECH-AC-MGMT-MIB", "qtechAcApTimestampCtrl"),
        ("QTECH-AC-MGMT-MIB", "qtechAcStaOperCtrl"),
        ("QTECH-AC-MGMT-MIB", "qtechAcType"),
        ("QTECH-AC-MGMT-MIB", "qtechAcNeid"),
        ("QTECH-AC-MGMT-MIB", "qtechAcManufacturer"),
        ("QTECH-AC-MGMT-MIB", "qtechAcSwVer"),
        ("QTECH-AC-MGMT-MIB", "qtechAcSwManufacturer"),
        ("QTECH-AC-MGMT-MIB", "qtechAcStaResourceNotEnough"),
        ("QTECH-AC-MGMT-MIB", "qtechAcPppoeClientAct"),
        ("QTECH-AC-MGMT-MIB", "qtechAcPppoeClientMax"),
        ("QTECH-AC-MGMT-MIB", "qtechAcStaActThredhold"),
        ("QTECH-AC-MGMT-MIB", "qtechAcStaDisactThredhold"),
        ("QTECH-AC-MGMT-MIB", "qtechAcStaTotalRoamThredhold"),
        ("QTECH-AC-MGMT-MIB", "qtechAcStaPerRoamThredhold"),
        ("QTECH-AC-MGMT-MIB", "qtechAcStaOffLineRemainTime"),
        ("QTECH-AC-MGMT-MIB", "qtechAcStaOffLineNumber"),
        ("QTECH-AC-MGMT-MIB", "qtechAcStaOffLineDelSingle"),
        ("QTECH-AC-MGMT-MIB", "qtechAcStaOffLineDelAll"),
        ("QTECH-AC-MGMT-MIB", "qtechAcRmOffLineApConfig"),
        ("QTECH-AC-MGMT-MIB", "qtechAcFlowBlApName1"),
        ("QTECH-AC-MGMT-MIB", "qtechAcFlowBlApName2"),
        ("QTECH-AC-MGMT-MIB", "qtechAcFlowBlApName3"),
        ("QTECH-AC-MGMT-MIB", "qtechAcFlowBlApName4"),
        ("QTECH-AC-MGMT-MIB", "qtechAcFlowBlApName5"),
        ("QTECH-AC-MGMT-MIB", "qtechAcFlowBlApName6"),
        ("QTECH-AC-MGMT-MIB", "qtechAcFlowBlApName7"),
        ("QTECH-AC-MGMT-MIB", "qtechAcFlowBlApName8"),
        ("QTECH-AC-MGMT-MIB", "qtechAcFlowBlApName9"),
        ("QTECH-AC-MGMT-MIB", "qtechAcFlowBlApName10"),
        ("QTECH-AC-MGMT-MIB", "qtechAcFlowBlNum"),
        ("QTECH-AC-MGMT-MIB", "qtechAcFlowBlRS"),
        ("QTECH-AC-MGMT-MIB", "qtechAcNumBlApName1"),
        ("QTECH-AC-MGMT-MIB", "qtechAcNumBlApName2"),
        ("QTECH-AC-MGMT-MIB", "qtechAcNumBlApName3"),
        ("QTECH-AC-MGMT-MIB", "qtechAcNumBlApName4"),
        ("QTECH-AC-MGMT-MIB", "qtechAcNumBlApName5"),
        ("QTECH-AC-MGMT-MIB", "qtechAcNumBlApName6"),
        ("QTECH-AC-MGMT-MIB", "qtechAcNumBlApName7"),
        ("QTECH-AC-MGMT-MIB", "qtechAcNumBlApName8"),
        ("QTECH-AC-MGMT-MIB", "qtechAcNumBlApName9"),
        ("QTECH-AC-MGMT-MIB", "qtechAcNumBlApName10"),
        ("QTECH-AC-MGMT-MIB", "qtechAcNumBlNum"),
        ("QTECH-AC-MGMT-MIB", "qtechAcNumBlRS"),
        ("QTECH-AC-MGMT-MIB", "qtechAcInAcRoamNum"),
        ("QTECH-AC-MGMT-MIB", "qtechAcBetweenAcRoamInNum"),
        ("QTECH-AC-MGMT-MIB", "qtechAcStaOnOverThrodOperCtrl"),
        ("QTECH-AC-MGMT-MIB", "qtechAcStaOffOverThrodOperCtrl"),
        ("QTECH-AC-MGMT-MIB", "qtechAcBetweenAcRoamOutNum"),
        ("QTECH-AC-MGMT-MIB", "qtechAcCpusageSwitch"),
        ("QTECH-AC-MGMT-MIB", "qtechAcCpuUsageTrapTimer"),
        ("QTECH-AC-MGMT-MIB", "qtechAcStatTrapTimer"),
        ("QTECH-AC-MGMT-MIB", "qtechAcHeartBeat"),
        ("QTECH-AC-MGMT-MIB", "qtechAcTotalApSupNum"),
        ("QTECH-AC-MGMT-MIB", "qtechAcTotalStaSupNum"),
        ("QTECH-AC-MGMT-MIB", "qtechAcTotalPppoeSupNum"),
        ("QTECH-AC-MGMT-MIB", "qtechAcCurTotalApSupNum"),
        ("QTECH-AC-MGMT-MIB", "qtechAcCurTotalStaSupNum"),
        ("QTECH-AC-MGMT-MIB", "qtechAcCurTotalPppoeSupNum"),
        ("QTECH-AC-MGMT-MIB", "qtechAcNasId"),
        ("QTECH-AC-MGMT-MIB", "qtechAcStaLimitLicense"),
        ("QTECH-AC-MGMT-MIB", "qtechAcWtpLimitLicense"),
        ("QTECH-AC-MGMT-MIB", "qtechAcStaIpv6Num"),
        ("QTECH-AC-MGMT-MIB", "qtechAcIpv6"),
        ("QTECH-AC-MGMT-MIB", "qtechAcIpv6Prefix"),
        ("QTECH-AC-MGMT-MIB", "qtechAcIpv6Type"),
        ("QTECH-AC-MGMT-MIB", "qtechAcIpv6AddrType"),
        ("QTECH-AC-MGMT-MIB", "qtechApApName"),
        ("QTECH-AC-MGMT-MIB", "qtechApApgName"),
        ("QTECH-AC-MGMT-MIB", "qtechApDiscTimer"),
        ("QTECH-AC-MGMT-MIB", "qtechApEchoReqTimer"),
        ("QTECH-AC-MGMT-MIB", "qtechApEroReportTimer"),
        ("QTECH-AC-MGMT-MIB", "qtechApStaTimeoutTimer"),
        ("QTECH-AC-MGMT-MIB", "qtechApStatisticsTimer"),
        ("QTECH-AC-MGMT-MIB", "qtechApFallback"),
        ("QTECH-AC-MGMT-MIB", "qtechApImageId"),
        ("QTECH-AC-MGMT-MIB", "qtechApIpDhcp"),
        ("QTECH-AC-MGMT-MIB", "qtechApLocation"),
        ("QTECH-AC-MGMT-MIB", "qtechApWpsMfp"),
        ("QTECH-AC-MGMT-MIB", "qtechApLastRebootReason"),
        ("QTECH-AC-MGMT-MIB", "qtechApEthernetIfName"),
        ("QTECH-AC-MGMT-MIB", "qtechApEthernetIfMacAddress"),
        ("QTECH-AC-MGMT-MIB", "qtechApEthernetIfAdminStatus"),
        ("QTECH-AC-MGMT-MIB", "qtechApEthernetIfOperStatus"),
        ("QTECH-AC-MGMT-MIB", "qtechApEthernetIfRxUcastPkts"),
        ("QTECH-AC-MGMT-MIB", "qtechApEthernetIfRxNUcastPkts"),
        ("QTECH-AC-MGMT-MIB", "qtechApEthernetIfTxUcastPkts"),
        ("QTECH-AC-MGMT-MIB", "qtechApEthernetIfTxNUcastPkts"),
        ("QTECH-AC-MGMT-MIB", "qtechApEthernetIfDuplex"),
        ("QTECH-AC-MGMT-MIB", "qtechApEthernetIfLinkSpeed"),
        ("QTECH-AC-MGMT-MIB", "qtechApEthernetIfPOEPower"),
        ("QTECH-AC-MGMT-MIB", "qtechApAdminStatus"),
        ("QTECH-AC-MGMT-MIB", "qtechApEthernetIfRxBoardPkts"),
        ("QTECH-AC-MGMT-MIB", "qtechApEthernetIfRxMultiPkts"),
        ("QTECH-AC-MGMT-MIB", "qtechApEthernetIfTxBoardPkts"),
        ("QTECH-AC-MGMT-MIB", "qtechApEthernetIfTxMultiPkts"),
        ("QTECH-AC-MGMT-MIB", "qtechApEthernetIfDropPkts"),
        ("QTECH-AC-MGMT-MIB", "qtechApSn"),
        ("QTECH-AC-MGMT-MIB", "qtechApIp"),
        ("QTECH-AC-MGMT-MIB", "qtechApStaNum"),
        ("QTECH-AC-MGMT-MIB", "qtechApToFat"),
        ("QTECH-AC-MGMT-MIB", "qtechApId"),
        ("QTECH-AC-MGMT-MIB", "qtechApSwVer"),
        ("QTECH-AC-MGMT-MIB", "qtechApBootVer"),
        ("QTECH-AC-MGMT-MIB", "qtechApPID"),
        ("QTECH-AC-MGMT-MIB", "qtechApHwVer"),
        ("QTECH-AC-MGMT-MIB", "qtechApStaLimit"),
        ("QTECH-AC-MGMT-MIB", "qtechApFactoryDefault"),
        ("QTECH-AC-MGMT-MIB", "qtechApCpuUsageTrapTimer"),
        ("QTECH-AC-MGMT-MIB", "qtechApStatTrapTimer"),
        ("QTECH-AC-MGMT-MIB", "qtechApLinkOnTimeInterval"),
        ("QTECH-AC-MGMT-MIB", "qtechApNetId"),
        ("QTECH-AC-MGMT-MIB", "qtechApUptime"),
        ("QTECH-AC-MGMT-MIB", "qtechApOfftime"),
        ("QTECH-AC-MGMT-MIB", "qtechApState"),
        ("QTECH-AC-MGMT-MIB", "qtechApNasId"),
        ("QTECH-AC-MGMT-MIB", "qtechApCoverArea"),
        ("QTECH-AC-MGMT-MIB", "qtechApLinkOnTimeIntervalMs"),
        ("QTECH-AC-MGMT-MIB", "qtechApUptimeMs"),
        ("QTECH-AC-MGMT-MIB", "qtechApHbUptimeMs"),
        ("QTECH-AC-MGMT-MIB", "qtechApIpv6"),
        ("QTECH-AC-MGMT-MIB", "qtechApIpv6Prefix"),
        ("QTECH-AC-MGMT-MIB", "qtechApIpv6PrefixLen"),
        ("QTECH-AC-MGMT-MIB", "qtechApIpv6Type"),
        ("QTECH-AC-MGMT-MIB", "qtechApIpv6Gateway"),
        ("QTECH-AC-MGMT-MIB", "qtechApIpv6StaNum"),
        ("QTECH-AC-MGMT-MIB", "qtechApRadioEn"),
        ("QTECH-AC-MGMT-MIB", "qtechApTxPower"),
        ("QTECH-AC-MGMT-MIB", "qtechApDtimPeriod"),
        ("QTECH-AC-MGMT-MIB", "qtechApBeaconPeriod"),
        ("QTECH-AC-MGMT-MIB", "qtechApCountry"),
        ("QTECH-AC-MGMT-MIB", "qtechApPreaShort"),
        ("QTECH-AC-MGMT-MIB", "qtechApRadioBssid"),
        ("QTECH-AC-MGMT-MIB", "qtechApTxPowerLevel"),
        ("QTECH-AC-MGMT-MIB", "qtechApTxPowerGlobal"),
        ("QTECH-AC-MGMT-MIB", "qtechApCurChan"),
        ("QTECH-AC-MGMT-MIB", "qtechApRfGlobal"),
        ("QTECH-AC-MGMT-MIB", "qtechApRadioRateType"),
        ("QTECH-AC-MGMT-MIB", "qtechApRadioType"),
        ("QTECH-AC-MGMT-MIB", "qtechApRadio11bSup"),
        ("QTECH-AC-MGMT-MIB", "qtechApMaxTxPower"),
        ("QTECH-AC-MGMT-MIB", "qtechApMinTxPower"),
        ("QTECH-AC-MGMT-MIB", "qtechApCurTxPower"),
        ("QTECH-AC-MGMT-MIB", "qtechApMaxTxPowerPer"),
        ("QTECH-AC-MGMT-MIB", "qtechApMinTxPowerPer"),
        ("QTECH-AC-MGMT-MIB", "qtechApIpAddr"),
        ("QTECH-AC-MGMT-MIB", "qtechApIpMask"),
        ("QTECH-AC-MGMT-MIB", "qtechApIpGetway"),
        ("QTECH-AC-MGMT-MIB", "qtechApStaticIpRS"),
        ("QTECH-AC-MGMT-MIB", "qtechApgDiscTimer"),
        ("QTECH-AC-MGMT-MIB", "qtechApgEchoReqTimer"),
        ("QTECH-AC-MGMT-MIB", "qtechApgEroReportTimer"),
        ("QTECH-AC-MGMT-MIB", "qtechApgStaTimeoutTimer"),
        ("QTECH-AC-MGMT-MIB", "qtechApgStatisticsTimer"),
        ("QTECH-AC-MGMT-MIB", "qtechApgFallback"),
        ("QTECH-AC-MGMT-MIB", "qtechApgImageId"),
        ("QTECH-AC-MGMT-MIB", "qtechApgCreatEn"),
        ("QTECH-AC-MGMT-MIB", "qtechApgEnableRadioEn"),
        ("QTECH-AC-MGMT-MIB", "qtechApgWlanId"),
        ("QTECH-AC-MGMT-MIB", "qtechApgVlanId"),
        ("QTECH-AC-MGMT-MIB", "qtechApgWlanIntfMapRS"),
        ("QTECH-AC-MGMT-MIB", "qtechWlanShort"),
        ("QTECH-AC-MGMT-MIB", "qtechWlanSpctMgmt"),
        ("QTECH-AC-MGMT-MIB", "qtechWlanEnQos"),
        ("QTECH-AC-MGMT-MIB", "qtechWlanShortSlotTime"),
        ("QTECH-AC-MGMT-MIB", "qtechWlanEnableApsd"),
        ("QTECH-AC-MGMT-MIB", "qtechWlanAckType"),
        ("QTECH-AC-MGMT-MIB", "qtechWlanTunnelType"),
        ("QTECH-AC-MGMT-MIB", "qtechWlanBroadSsid"),
        ("QTECH-AC-MGMT-MIB", "qtechWlanWlanSsid"),
        ("QTECH-AC-MGMT-MIB", "qtechWlanWlanProfile"),
        ("QTECH-AC-MGMT-MIB", "qtechWlanCreateMapRS"),
        ("QTECH-AC-MGMT-MIB", "qtechWlanRts"),
        ("QTECH-AC-MGMT-MIB", "qtechWlanShortTry"),
        ("QTECH-AC-MGMT-MIB", "qtechWlanLongTry"),
        ("QTECH-AC-MGMT-MIB", "qtechWlanStaNum"),
        ("QTECH-AC-MGMT-MIB", "qtechWlanNasId"),
        ("QTECH-AC-MGMT-MIB", "qtechWlanChanV"),
        ("QTECH-AC-MGMT-MIB", "qtechWlanChanBandEn"),
        ("QTECH-AC-MGMT-MIB", "qtechWlanLimitChanRS"),
        ("QTECH-AC-MGMT-MIB", "qtechWlanChanBandRS"),
        ("QTECH-AC-MGMT-MIB", "qtechStaApMacAddr"),
        ("QTECH-AC-MGMT-MIB", "qtechStaVlan"),
        ("QTECH-AC-MGMT-MIB", "qtechStaWlanId"),
        ("QTECH-AC-MGMT-MIB", "qtechStaIp"),
        ("QTECH-AC-MGMT-MIB", "qtechStaApIp"),
        ("QTECH-AC-MGMT-MIB", "qtechStaApRadioId"),
        ("QTECH-AC-MGMT-MIB", "qtechStaApRadioType"),
        ("QTECH-AC-MGMT-MIB", "qtechStaAssoType"),
        ("QTECH-AC-MGMT-MIB", "qtechStaAuthType"),
        ("QTECH-AC-MGMT-MIB", "qtechStaRoamTimesPerMin"),
        ("QTECH-AC-MGMT-MIB", "qtechStaOnTimesPerHour"),
        ("QTECH-AC-MGMT-MIB", "qtechStaOffTimesPerHour"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyApMac"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaMac"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyApIp"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaIp"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaOperType"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaApRadioId"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaApRadioType"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaVlanId"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaWlanId"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyTime"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyOldVer"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyNewVer"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyVerUpdtReason"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyAcMBChangeV"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaOperTimes"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyAcPowerIndex"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyAcPowerStatu"),
        ("QTECH-AC-MGMT-MIB", "qtechAcKickClient"),
        ("QTECH-AC-MGMT-MIB", "qtechAcOpenStaNum"),
        ("QTECH-AC-MGMT-MIB", "qtechAcOpenStaAbnormalDownTimes"),
        ("QTECH-AC-MGMT-MIB", "qtechAcWepPskStaNum"),
        ("QTECH-AC-MGMT-MIB", "qtechAcWepPskStaAbnormalDownTimes"))
)
if mibBuilder.loadTexts:
    qtechAcMgmtAcMIBGroup.setStatus("current")


# Notification objects

qtechNotifyApTimeStampFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 2, 1)
)
qtechNotifyApTimeStampFail.setObjects(
    ("QTECH-AC-MGMT-MIB", "qtechNotifyApMac")
)
if mibBuilder.loadTexts:
    qtechNotifyApTimeStampFail.setStatus(
        "current"
    )

qtechNotifyStaOper = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 2, 2)
)
qtechNotifyStaOper.setObjects(
      *(("QTECH-AC-MGMT-MIB", "qtechNotifyApMac"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaMac"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyApIp"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaIp"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaOperType"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaApRadioId"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaApRadioType"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaVlanId"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaWlanId"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyTime"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaIpv6"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaAssoAuthMode"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaNetAuthMode"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaSsid"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaLinkRate"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaCurChan"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaClientType"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaRssi"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaReason"))
)
if mibBuilder.loadTexts:
    qtechNotifyStaOper.setStatus(
        "current"
    )

qtechNotifyAcMBChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 2, 3)
)
qtechNotifyAcMBChange.setObjects(
    ("QTECH-AC-MGMT-MIB", "qtechNotifyAcMBChangeV")
)
if mibBuilder.loadTexts:
    qtechNotifyAcMBChange.setStatus(
        "current"
    )

qtechNotifyApSwUpdtFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 2, 4)
)
qtechNotifyApSwUpdtFail.setObjects(
      *(("QTECH-AC-MGMT-MIB", "qtechNotifyApMac"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyOldVer"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyNewVer"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyVerUpdtReason"))
)
if mibBuilder.loadTexts:
    qtechNotifyApSwUpdtFail.setStatus(
        "current"
    )

qtechNotifyStaActOverThredhold = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 2, 5)
)
qtechNotifyStaActOverThredhold.setObjects(
      *(("QTECH-AC-MGMT-MIB", "qtechNotifyApMac"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaMac"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaApRadioId"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaApRadioType"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaOperTimes"))
)
if mibBuilder.loadTexts:
    qtechNotifyStaActOverThredhold.setStatus(
        "current"
    )

qtechNotifyStaDisactOverThredhold = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 2, 6)
)
qtechNotifyStaDisactOverThredhold.setObjects(
      *(("QTECH-AC-MGMT-MIB", "qtechNotifyApMac"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaMac"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaApRadioId"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaApRadioType"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaOperTimes"))
)
if mibBuilder.loadTexts:
    qtechNotifyStaDisactOverThredhold.setStatus(
        "current"
    )

qtechNotifyStaRoamTotal = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 2, 7)
)
qtechNotifyStaRoamTotal.setObjects(
      *(("QTECH-AC-MGMT-MIB", "qtechNotifyApMac"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaMac"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaApRadioId"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaApRadioType"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaOperTimes"))
)
if mibBuilder.loadTexts:
    qtechNotifyStaRoamTotal.setStatus(
        "current"
    )

qtechNotifyStaRoamPerMin = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 2, 8)
)
qtechNotifyStaRoamPerMin.setObjects(
      *(("QTECH-AC-MGMT-MIB", "qtechNotifyApMac"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaMac"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaApRadioId"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaApRadioType"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaOperTimes"))
)
if mibBuilder.loadTexts:
    qtechNotifyStaRoamPerMin.setStatus(
        "current"
    )

qtechNotifyAcPowerStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 2, 9)
)
qtechNotifyAcPowerStatus.setObjects(
      *(("QTECH-AC-MGMT-MIB", "qtechNotifyAcPowerIndex"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyAcPowerStatu"))
)
if mibBuilder.loadTexts:
    qtechNotifyAcPowerStatus.setStatus(
        "current"
    )

qtechNotify86PowerOffAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 2, 10)
)
qtechNotify86PowerOffAlarm.setObjects(
    ("QTECH-AC-MGMT-MIB", "qtechNotifyAcPowerIndex")
)
if mibBuilder.loadTexts:
    qtechNotify86PowerOffAlarm.setStatus(
        "current"
    )

qtechNotify86PowerOffAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 2, 11)
)
qtechNotify86PowerOffAlarmClear.setObjects(
    ("QTECH-AC-MGMT-MIB", "qtechNotifyAcPowerIndex")
)
if mibBuilder.loadTexts:
    qtechNotify86PowerOffAlarmClear.setStatus(
        "current"
    )

qtechNotifyApSwUpdtSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 2, 12)
)
qtechNotifyApSwUpdtSuccess.setObjects(
      *(("QTECH-AC-MGMT-MIB", "qtechNotifyApMac"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyOldVer"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyNewVer"))
)
if mibBuilder.loadTexts:
    qtechNotifyApSwUpdtSuccess.setStatus(
        "current"
    )

qtechNotifyApUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 2, 13)
)
qtechNotifyApUp.setObjects(
      *(("QTECH-AC-MGMT-MIB", "qtechApMacAddr"),
        ("CAPWAP-BASE-MIB", "capwapBaseNtfChannelType"),
        ("CAPWAP-BASE-MIB", "capwapBaseNtfAuthenMethod"))
)
if mibBuilder.loadTexts:
    qtechNotifyApUp.setStatus(
        "current"
    )

qtechNotifyApDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 2, 14)
)
qtechNotifyApDown.setObjects(
      *(("QTECH-AC-MGMT-MIB", "qtechApMacAddr"),
        ("CAPWAP-BASE-MIB", "capwapBaseNtfChannelType"),
        ("CAPWAP-BASE-MIB", "capwapBaseNtfChannelDownReason"))
)
if mibBuilder.loadTexts:
    qtechNotifyApDown.setStatus(
        "current"
    )

qtechNotifyApSwUpdtFailApMac = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 2, 15)
)
qtechNotifyApSwUpdtFailApMac.setObjects(
      *(("QTECH-AC-MGMT-MIB", "qtechApMacAddr"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyOldVer"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyNewVer"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyVerUpdtReason"))
)
if mibBuilder.loadTexts:
    qtechNotifyApSwUpdtFailApMac.setStatus(
        "current"
    )

qtechNotifyApTimeStampFailApMac = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 2, 16)
)
qtechNotifyApTimeStampFailApMac.setObjects(
    ("QTECH-AC-MGMT-MIB", "qtechApMacAddr")
)
if mibBuilder.loadTexts:
    qtechNotifyApTimeStampFailApMac.setStatus(
        "current"
    )

qtechNotifyStaOperAlternate = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 6, 2, 17)
)
qtechNotifyStaOperAlternate.setObjects(
      *(("QTECH-AC-MGMT-MIB", "qtechNotifyStaOperType"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaMac"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaIp"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyApMac"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyApIp"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaApRadioId"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaApRadioType"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaWlanId"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaSsid"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaVlanId"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaLinkRate"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaCurChan"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaRssi"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaTimestamp"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaOnlineTimeval"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaIpv4Upflow"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaIpv4Downflow"))
)
if mibBuilder.loadTexts:
    qtechNotifyStaOperAlternate.setStatus(
        "current"
    )


# Notifications groups

qtechAcMgmtAcTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 7, 2, 2)
)
qtechAcMgmtAcTrapGroup.setObjects(
      *(("QTECH-AC-MGMT-MIB", "qtechNotifyApTimeStampFail"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaOper"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyAcMBChange"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyApSwUpdtFail"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaActOverThredhold"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaDisactOverThredhold"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaRoamTotal"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyStaRoamPerMin"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyAcPowerStatus"),
        ("QTECH-AC-MGMT-MIB", "qtechNotify86PowerOffAlarm"),
        ("QTECH-AC-MGMT-MIB", "qtechNotify86PowerOffAlarmClear"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyApSwUpdtSuccess"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyApUp"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyApDown"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyApSwUpdtFailApMac"),
        ("QTECH-AC-MGMT-MIB", "qtechNotifyApTimeStampFailApMac"))
)
if mibBuilder.loadTexts:
    qtechAcMgmtAcTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

qtechAcMgmtAcMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 56, 7, 1, 1)
)
qtechAcMgmtAcMIBCompliance.setObjects(
      *(("QTECH-AC-MGMT-MIB", "qtechAcMgmtAcMIBGroup"),
        ("QTECH-AC-MGMT-MIB", "qtechAcMgmtAcTrapGroup"))
)
if mibBuilder.loadTexts:
    qtechAcMgmtAcMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-AC-MGMT-MIB",
    **{"qtechAcMgmtMIB": qtechAcMgmtMIB,
       "qtechAcMgmtAcMIBObjects": qtechAcMgmtAcMIBObjects,
       "qtechAcMgmtAc": qtechAcMgmtAc,
       "qtechAcStaLimit": qtechAcStaLimit,
       "qtechAcWtpLimit": qtechAcWtpLimit,
       "qtechAcRMacField": qtechAcRMacField,
       "qtechAcDataDtls": qtechAcDataDtls,
       "qtechAcEcnSupport": qtechAcEcnSupport,
       "qtechAcAcIpTable": qtechAcAcIpTable,
       "qtechAcAcIpTableEntry": qtechAcAcIpTableEntry,
       "qtechAcAcIpIndex": qtechAcAcIpIndex,
       "qtechAcBackAcIp": qtechAcBackAcIp,
       "qtechAcAcIpRS": qtechAcAcIpRS,
       "qtechAcMtu": qtechAcMtu,
       "qtechAcAcName": qtechAcAcName,
       "qtechAcLocation": qtechAcLocation,
       "qtechAcResetAp": qtechAcResetAp,
       "qtechAcApNum": qtechAcApNum,
       "qtechAc80211aRateTable": qtechAc80211aRateTable,
       "qtechAc80211aRateEntry": qtechAc80211aRateEntry,
       "qtechAc80211aRate": qtechAc80211aRate,
       "qtechAc80211aRateType": qtechAc80211aRateType,
       "qtechAc80211bRateTable": qtechAc80211bRateTable,
       "qtechAc80211bRateEntry": qtechAc80211bRateEntry,
       "qtechAc80211bRate": qtechAc80211bRate,
       "qtechAc80211bRateType": qtechAc80211bRateType,
       "qtechAcFallback": qtechAcFallback,
       "qtechAcStaNum": qtechAcStaNum,
       "qtechAcMacAddr": qtechAcMacAddr,
       "qtechAcDescriptor": qtechAcDescriptor,
       "qtechAcPID": qtechAcPID,
       "qtechAcHwId": qtechAcHwId,
       "qtechAcSN": qtechAcSN,
       "qtechAcTemp": qtechAcTemp,
       "qtechAcAPUpDownCtrl": qtechAcAPUpDownCtrl,
       "qtechAcAPJoinFailCtrl": qtechAcAPJoinFailCtrl,
       "qtechAcAPDecryEroReportCtrl": qtechAcAPDecryEroReportCtrl,
       "qtechAcApImageUpdtCtrl": qtechAcApImageUpdtCtrl,
       "qtechAcApConfigMsgEroCtrl": qtechAcApConfigMsgEroCtrl,
       "qtechAcApRadioOperStatuCtrl": qtechAcApRadioOperStatuCtrl,
       "qtechAcApAuthenFailCtrl": qtechAcApAuthenFailCtrl,
       "qtechAcApTimestampCtrl": qtechAcApTimestampCtrl,
       "qtechAcStaOperCtrl": qtechAcStaOperCtrl,
       "qtechAcType": qtechAcType,
       "qtechAcNeid": qtechAcNeid,
       "qtechAcManufacturer": qtechAcManufacturer,
       "qtechAcSwVer": qtechAcSwVer,
       "qtechAcSwManufacturer": qtechAcSwManufacturer,
       "qtechAcStaResourceNotEnough": qtechAcStaResourceNotEnough,
       "qtechAcPppoeClientAct": qtechAcPppoeClientAct,
       "qtechAcPppoeClientMax": qtechAcPppoeClientMax,
       "qtechAcStaActThredhold": qtechAcStaActThredhold,
       "qtechAcStaDisactThredhold": qtechAcStaDisactThredhold,
       "qtechAcStaTotalRoamThredhold": qtechAcStaTotalRoamThredhold,
       "qtechAcStaPerRoamThredhold": qtechAcStaPerRoamThredhold,
       "qtechAcStaOffLineRemainTime": qtechAcStaOffLineRemainTime,
       "qtechAcStaOffLineNumber": qtechAcStaOffLineNumber,
       "qtechAcStaOffLineDelSingle": qtechAcStaOffLineDelSingle,
       "qtechAcStaOffLineDelAll": qtechAcStaOffLineDelAll,
       "qtechAcRmOffLineApConfig": qtechAcRmOffLineApConfig,
       "qtechAcFlowBlGroupTable": qtechAcFlowBlGroupTable,
       "qtechAcFlowBlGroupEntry": qtechAcFlowBlGroupEntry,
       "qtechAcFlowBlGroupName": qtechAcFlowBlGroupName,
       "qtechAcFlowBlApName1": qtechAcFlowBlApName1,
       "qtechAcFlowBlApName2": qtechAcFlowBlApName2,
       "qtechAcFlowBlApName3": qtechAcFlowBlApName3,
       "qtechAcFlowBlApName4": qtechAcFlowBlApName4,
       "qtechAcFlowBlApName5": qtechAcFlowBlApName5,
       "qtechAcFlowBlApName6": qtechAcFlowBlApName6,
       "qtechAcFlowBlApName7": qtechAcFlowBlApName7,
       "qtechAcFlowBlApName8": qtechAcFlowBlApName8,
       "qtechAcFlowBlApName9": qtechAcFlowBlApName9,
       "qtechAcFlowBlApName10": qtechAcFlowBlApName10,
       "qtechAcFlowBlNum": qtechAcFlowBlNum,
       "qtechAcFlowBlRS": qtechAcFlowBlRS,
       "qtechAcFlowBlEnable": qtechAcFlowBlEnable,
       "qtechAcFlowBlBase": qtechAcFlowBlBase,
       "qtechAcFlowBlIsEnable": qtechAcFlowBlIsEnable,
       "qtechAcNumBlGroupTable": qtechAcNumBlGroupTable,
       "qtechAcNumBlGroupEntry": qtechAcNumBlGroupEntry,
       "qtechAcNumBlGroupName": qtechAcNumBlGroupName,
       "qtechAcNumBlApName1": qtechAcNumBlApName1,
       "qtechAcNumBlApName2": qtechAcNumBlApName2,
       "qtechAcNumBlApName3": qtechAcNumBlApName3,
       "qtechAcNumBlApName4": qtechAcNumBlApName4,
       "qtechAcNumBlApName5": qtechAcNumBlApName5,
       "qtechAcNumBlApName6": qtechAcNumBlApName6,
       "qtechAcNumBlApName7": qtechAcNumBlApName7,
       "qtechAcNumBlApName8": qtechAcNumBlApName8,
       "qtechAcNumBlApName9": qtechAcNumBlApName9,
       "qtechAcNumBlApName10": qtechAcNumBlApName10,
       "qtechAcNumBlNum": qtechAcNumBlNum,
       "qtechAcNumBlRS": qtechAcNumBlRS,
       "qtechAcNumBlEnable": qtechAcNumBlEnable,
       "qtechAcNumBlIsEnable": qtechAcNumBlIsEnable,
       "qtechAcInAcRoamNum": qtechAcInAcRoamNum,
       "qtechAcBetweenAcRoamInNum": qtechAcBetweenAcRoamInNum,
       "qtechAcStaOnOverThrodOperCtrl": qtechAcStaOnOverThrodOperCtrl,
       "qtechAcStaOffOverThrodOperCtrl": qtechAcStaOffOverThrodOperCtrl,
       "qtechAcBetweenAcRoamOutNum": qtechAcBetweenAcRoamOutNum,
       "qtechAcCpusageSwitch": qtechAcCpusageSwitch,
       "qtechAcCpuUsageTrapTimer": qtechAcCpuUsageTrapTimer,
       "qtechAcStatTrapTimer": qtechAcStatTrapTimer,
       "qtechAcHeartBeat": qtechAcHeartBeat,
       "qtechAcTotalApSupNum": qtechAcTotalApSupNum,
       "qtechAcTotalStaSupNum": qtechAcTotalStaSupNum,
       "qtechAcTotalPppoeSupNum": qtechAcTotalPppoeSupNum,
       "qtechAcCurTotalApSupNum": qtechAcCurTotalApSupNum,
       "qtechAcCurTotalStaSupNum": qtechAcCurTotalStaSupNum,
       "qtechAcCurTotalPppoeSupNum": qtechAcCurTotalPppoeSupNum,
       "qtechAcNasId": qtechAcNasId,
       "qtechAcStaLimitLicense": qtechAcStaLimitLicense,
       "qtechAcWtpLimitLicense": qtechAcWtpLimitLicense,
       "qtechAcStaIpv6Num": qtechAcStaIpv6Num,
       "qtechAcIpv6": qtechAcIpv6,
       "qtechAcIpv6Prefix": qtechAcIpv6Prefix,
       "qtechAcIpv6Type": qtechAcIpv6Type,
       "qtechAcIpv6AddrType": qtechAcIpv6AddrType,
       "qtechAcKickClient": qtechAcKickClient,
       "qtechAcOpenStaNum": qtechAcOpenStaNum,
       "qtechAcOpenStaAbnormalDownTimes": qtechAcOpenStaAbnormalDownTimes,
       "qtechAcWepPskStaNum": qtechAcWepPskStaNum,
       "qtechAcWepPskStaAbnormalDownTimes": qtechAcWepPskStaAbnormalDownTimes,
       "qtechAcMgmtAcIf": qtechAcMgmtAcIf,
       "qtechAcMgmtApMIBObjects": qtechAcMgmtApMIBObjects,
       "qtechAcMgmtAp": qtechAcMgmtAp,
       "qtechApCfgTable": qtechApCfgTable,
       "qtechApCfgEntry": qtechApCfgEntry,
       "qtechApMacAddr": qtechApMacAddr,
       "qtechApApName": qtechApApName,
       "qtechApApgName": qtechApApgName,
       "qtechApDiscTimer": qtechApDiscTimer,
       "qtechApEchoReqTimer": qtechApEchoReqTimer,
       "qtechApEroReportTimer": qtechApEroReportTimer,
       "qtechApStaTimeoutTimer": qtechApStaTimeoutTimer,
       "qtechApStatisticsTimer": qtechApStatisticsTimer,
       "qtechApFallback": qtechApFallback,
       "qtechApImageId": qtechApImageId,
       "qtechApIpDhcp": qtechApIpDhcp,
       "qtechApLocation": qtechApLocation,
       "qtechApWpsMfp": qtechApWpsMfp,
       "qtechApLastRebootReason": qtechApLastRebootReason,
       "qtechApEthernetIfName": qtechApEthernetIfName,
       "qtechApEthernetIfMacAddress": qtechApEthernetIfMacAddress,
       "qtechApEthernetIfAdminStatus": qtechApEthernetIfAdminStatus,
       "qtechApEthernetIfOperStatus": qtechApEthernetIfOperStatus,
       "qtechApEthernetIfRxUcastPkts": qtechApEthernetIfRxUcastPkts,
       "qtechApEthernetIfRxNUcastPkts": qtechApEthernetIfRxNUcastPkts,
       "qtechApEthernetIfTxUcastPkts": qtechApEthernetIfTxUcastPkts,
       "qtechApEthernetIfTxNUcastPkts": qtechApEthernetIfTxNUcastPkts,
       "qtechApEthernetIfDuplex": qtechApEthernetIfDuplex,
       "qtechApEthernetIfLinkSpeed": qtechApEthernetIfLinkSpeed,
       "qtechApEthernetIfPOEPower": qtechApEthernetIfPOEPower,
       "qtechApAdminStatus": qtechApAdminStatus,
       "qtechApEthernetIfRxBoardPkts": qtechApEthernetIfRxBoardPkts,
       "qtechApEthernetIfRxMultiPkts": qtechApEthernetIfRxMultiPkts,
       "qtechApEthernetIfTxBoardPkts": qtechApEthernetIfTxBoardPkts,
       "qtechApEthernetIfTxMultiPkts": qtechApEthernetIfTxMultiPkts,
       "qtechApEthernetIfDropPkts": qtechApEthernetIfDropPkts,
       "qtechApSn": qtechApSn,
       "qtechApIp": qtechApIp,
       "qtechApStaNum": qtechApStaNum,
       "qtechApToFat": qtechApToFat,
       "qtechApId": qtechApId,
       "qtechApSwVer": qtechApSwVer,
       "qtechApBootVer": qtechApBootVer,
       "qtechApPID": qtechApPID,
       "qtechApHwVer": qtechApHwVer,
       "qtechApStaLimit": qtechApStaLimit,
       "qtechApFactoryDefault": qtechApFactoryDefault,
       "qtechApCpuUsageTrapTimer": qtechApCpuUsageTrapTimer,
       "qtechApStatTrapTimer": qtechApStatTrapTimer,
       "qtechApLinkOnTimeInterval": qtechApLinkOnTimeInterval,
       "qtechApNetId": qtechApNetId,
       "qtechApUptime": qtechApUptime,
       "qtechApState": qtechApState,
       "qtechApNasId": qtechApNasId,
       "qtechApCoverArea": qtechApCoverArea,
       "qtechApLinkOnTimeIntervalMs": qtechApLinkOnTimeIntervalMs,
       "qtechApUptimeMs": qtechApUptimeMs,
       "qtechApHbUptimeMs": qtechApHbUptimeMs,
       "qtechApIpv6": qtechApIpv6,
       "qtechApIpv6Prefix": qtechApIpv6Prefix,
       "qtechApIpv6PrefixLen": qtechApIpv6PrefixLen,
       "qtechApIpv6Type": qtechApIpv6Type,
       "qtechApIpv6Gateway": qtechApIpv6Gateway,
       "qtechApIpv6StaNum": qtechApIpv6StaNum,
       "qtechApCfgRadioTable": qtechApCfgRadioTable,
       "qtechApCfgRadioEntry": qtechApCfgRadioEntry,
       "qtechApCfgRadioId": qtechApCfgRadioId,
       "qtechApRadioEn": qtechApRadioEn,
       "qtechApTxPower": qtechApTxPower,
       "qtechApDtimPeriod": qtechApDtimPeriod,
       "qtechApBeaconPeriod": qtechApBeaconPeriod,
       "qtechApCountry": qtechApCountry,
       "qtechApPreaShort": qtechApPreaShort,
       "qtechApRadioBssid": qtechApRadioBssid,
       "qtechApTxPowerLevel": qtechApTxPowerLevel,
       "qtechApTxPowerGlobal": qtechApTxPowerGlobal,
       "qtechApCurChan": qtechApCurChan,
       "qtechApRfGlobal": qtechApRfGlobal,
       "qtechApRadioType": qtechApRadioType,
       "qtechApRadio11bSup": qtechApRadio11bSup,
       "qtechApMaxTxPower": qtechApMaxTxPower,
       "qtechApMinTxPower": qtechApMinTxPower,
       "qtechApCurTxPower": qtechApCurTxPower,
       "qtechApMaxTxPowerPer": qtechApMaxTxPowerPer,
       "qtechApMinTxPowerPer": qtechApMinTxPowerPer,
       "qtechApRadioRateCfgTable": qtechApRadioRateCfgTable,
       "qtechApRadioRateCfgEntry": qtechApRadioRateCfgEntry,
       "qtechApRadioRate": qtechApRadioRate,
       "qtechApRadioRateType": qtechApRadioRateType,
       "qtechApStaticIpCfgTable": qtechApStaticIpCfgTable,
       "qtechApStaticIpCfgEntry": qtechApStaticIpCfgEntry,
       "qtechApIpAddr": qtechApIpAddr,
       "qtechApIpMask": qtechApIpMask,
       "qtechApIpGetway": qtechApIpGetway,
       "qtechApStaticIpRS": qtechApStaticIpRS,
       "qtechApOfflineTable": qtechApOfflineTable,
       "qtechApOfflineEntry": qtechApOfflineEntry,
       "qtechApOfftime": qtechApOfftime,
       "qtechApOffApName": qtechApOffApName,
       "qtechApOffMacAddr": qtechApOffMacAddr,
       "qtechApBackupStateTable": qtechApBackupStateTable,
       "qtechApBackupStateEntry": qtechApBackupStateEntry,
       "qtechApBackupState": qtechApBackupState,
       "qtechAcMgmtApIf": qtechAcMgmtApIf,
       "qtechAcMgmtApgMIBObjects": qtechAcMgmtApgMIBObjects,
       "qtechAcMgmtApg": qtechAcMgmtApg,
       "qtechApgCfgTable": qtechApgCfgTable,
       "qtechApgCfgEntry": qtechApgCfgEntry,
       "qtechApgApgName": qtechApgApgName,
       "qtechApgDiscTimer": qtechApgDiscTimer,
       "qtechApgEchoReqTimer": qtechApgEchoReqTimer,
       "qtechApgEroReportTimer": qtechApgEroReportTimer,
       "qtechApgStaTimeoutTimer": qtechApgStaTimeoutTimer,
       "qtechApgStatisticsTimer": qtechApgStatisticsTimer,
       "qtechApgFallback": qtechApgFallback,
       "qtechApgImageId": qtechApgImageId,
       "qtechApgCreatEn": qtechApgCreatEn,
       "qtechApgCfgRadioTable": qtechApgCfgRadioTable,
       "qtechApgCfgRadioEntry": qtechApgCfgRadioEntry,
       "qtechApgEnableRadioId": qtechApgEnableRadioId,
       "qtechApgEnableRadioEn": qtechApgEnableRadioEn,
       "qtechApgIntfMapTable": qtechApgIntfMapTable,
       "qtechApgIntfMapEntry": qtechApgIntfMapEntry,
       "qtechApgWlanIndex": qtechApgWlanIndex,
       "qtechApgWlanId": qtechApgWlanId,
       "qtechApgVlanId": qtechApgVlanId,
       "qtechApgRadioId": qtechApgRadioId,
       "qtechApgWlanIntfMapRS": qtechApgWlanIntfMapRS,
       "qtechAcMgmtApgIf": qtechAcMgmtApgIf,
       "qtechAcMgmtWlanMIBObjects": qtechAcMgmtWlanMIBObjects,
       "qtechAcMgmtWlan": qtechAcMgmtWlan,
       "qtechWlanCfgTable": qtechWlanCfgTable,
       "qtechWlanCfgEntry": qtechWlanCfgEntry,
       "qtechWlanId": qtechWlanId,
       "qtechWlanShort": qtechWlanShort,
       "qtechWlanSpctMgmt": qtechWlanSpctMgmt,
       "qtechWlanEnQos": qtechWlanEnQos,
       "qtechWlanShortSlotTime": qtechWlanShortSlotTime,
       "qtechWlanEnableApsd": qtechWlanEnableApsd,
       "qtechWlanAckType": qtechWlanAckType,
       "qtechWlanTunnelType": qtechWlanTunnelType,
       "qtechWlanBroadSsid": qtechWlanBroadSsid,
       "qtechWlanRts": qtechWlanRts,
       "qtechWlanShortTry": qtechWlanShortTry,
       "qtechWlanLongTry": qtechWlanLongTry,
       "qtechWlanStaNum": qtechWlanStaNum,
       "qtechWlanNasId": qtechWlanNasId,
       "qtechWlanWlanCreatTable": qtechWlanWlanCreatTable,
       "qtechWlanWlanCreatEntry": qtechWlanWlanCreatEntry,
       "qtechWlanWlanSsid": qtechWlanWlanSsid,
       "qtechWlanWlanProfile": qtechWlanWlanProfile,
       "qtechWlanCreateMapRS": qtechWlanCreateMapRS,
       "qtechWlanChanBandTable": qtechWlanChanBandTable,
       "qtechWlanChanBandEntry": qtechWlanChanBandEntry,
       "qtechWlanBandV": qtechWlanBandV,
       "qtechWlanChanV": qtechWlanChanV,
       "qtechWlanChanBandEn": qtechWlanChanBandEn,
       "qtechWlanChanBandRS": qtechWlanChanBandRS,
       "qtechWlanLimitChanTable": qtechWlanLimitChanTable,
       "qtechWlanLimitChanEntry": qtechWlanLimitChanEntry,
       "qtechWlanLimitChanFirstV": qtechWlanLimitChanFirstV,
       "qtechWlanLimitChanNumV": qtechWlanLimitChanNumV,
       "qtechWlanLimitChanMaxTxPowerLv": qtechWlanLimitChanMaxTxPowerLv,
       "qtechWlanLimitChanRS": qtechWlanLimitChanRS,
       "qtechAcMgmtWlanIf": qtechAcMgmtWlanIf,
       "qtechAcMgmtStaMIBObjects": qtechAcMgmtStaMIBObjects,
       "qtechAcMgmtSta": qtechAcMgmtSta,
       "qtechStaTable": qtechStaTable,
       "qtechStaEntry": qtechStaEntry,
       "qtechStaMacAddr": qtechStaMacAddr,
       "qtechStaApMacAddr": qtechStaApMacAddr,
       "qtechStaVlan": qtechStaVlan,
       "qtechStaWlanId": qtechStaWlanId,
       "qtechStaIp": qtechStaIp,
       "qtechStaApIp": qtechStaApIp,
       "qtechStaApRadioId": qtechStaApRadioId,
       "qtechStaApRadioType": qtechStaApRadioType,
       "qtechStaAssoType": qtechStaAssoType,
       "qtechStaAuthType": qtechStaAuthType,
       "qtechStaRoamTimesPerMin": qtechStaRoamTimesPerMin,
       "qtechStaOnTimesPerHour": qtechStaOnTimesPerHour,
       "qtechStaOffTimesPerHour": qtechStaOffTimesPerHour,
       "qtechStaIpv6": qtechStaIpv6,
       "qtechStaAssoAuthMode": qtechStaAssoAuthMode,
       "qtechStaNetAuthMode": qtechStaNetAuthMode,
       "qtechStaSsid": qtechStaSsid,
       "qtechStaLinkRate": qtechStaLinkRate,
       "qtechStaCurChan": qtechStaCurChan,
       "qtechStaClientType": qtechStaClientType,
       "qtechStaRssi": qtechStaRssi,
       "qtechStaUserName": qtechStaUserName,
       "qtechStaTerminalType": qtechStaTerminalType,
       "qtechStaOnlineTime": qtechStaOnlineTime,
       "qtechStaUpTimeInterval": qtechStaUpTimeInterval,
       "qtechAcMgmtStaIf": qtechAcMgmtStaIf,
       "qtechAcMgmtNotificationsMIBObjects": qtechAcMgmtNotificationsMIBObjects,
       "qtechAcMgmtNtfObjects": qtechAcMgmtNtfObjects,
       "qtechNotifyApMac": qtechNotifyApMac,
       "qtechNotifyStaMac": qtechNotifyStaMac,
       "qtechNotifyApIp": qtechNotifyApIp,
       "qtechNotifyStaIp": qtechNotifyStaIp,
       "qtechNotifyStaOperType": qtechNotifyStaOperType,
       "qtechNotifyStaApRadioId": qtechNotifyStaApRadioId,
       "qtechNotifyStaApRadioType": qtechNotifyStaApRadioType,
       "qtechNotifyStaVlanId": qtechNotifyStaVlanId,
       "qtechNotifyStaWlanId": qtechNotifyStaWlanId,
       "qtechNotifyAcMBChangeV": qtechNotifyAcMBChangeV,
       "qtechNotifyStaOperTimes": qtechNotifyStaOperTimes,
       "qtechNotifyAcPowerIndex": qtechNotifyAcPowerIndex,
       "qtechNotifyAcPowerStatu": qtechNotifyAcPowerStatu,
       "qtechNotifyTime": qtechNotifyTime,
       "qtechNotifyOldVer": qtechNotifyOldVer,
       "qtechNotifyNewVer": qtechNotifyNewVer,
       "qtechNotifyVerUpdtReason": qtechNotifyVerUpdtReason,
       "qtechNotifyStaIpv6": qtechNotifyStaIpv6,
       "qtechNotifyStaAssoAuthMode": qtechNotifyStaAssoAuthMode,
       "qtechNotifyStaNetAuthMode": qtechNotifyStaNetAuthMode,
       "qtechNotifyStaSsid": qtechNotifyStaSsid,
       "qtechNotifyStaLinkRate": qtechNotifyStaLinkRate,
       "qtechNotifyStaCurChan": qtechNotifyStaCurChan,
       "qtechNotifyStaClientType": qtechNotifyStaClientType,
       "qtechNotifyStaRssi": qtechNotifyStaRssi,
       "qtechNotifyStaReason": qtechNotifyStaReason,
       "qtechNotifyStaTimestamp": qtechNotifyStaTimestamp,
       "qtechNotifyStaOnlineTimeval": qtechNotifyStaOnlineTimeval,
       "qtechNotifyStaIpv4Upflow": qtechNotifyStaIpv4Upflow,
       "qtechNotifyStaIpv4Downflow": qtechNotifyStaIpv4Downflow,
       "qtechAcMgmtNotifications": qtechAcMgmtNotifications,
       "qtechNotifyApTimeStampFail": qtechNotifyApTimeStampFail,
       "qtechNotifyStaOper": qtechNotifyStaOper,
       "qtechNotifyAcMBChange": qtechNotifyAcMBChange,
       "qtechNotifyApSwUpdtFail": qtechNotifyApSwUpdtFail,
       "qtechNotifyStaActOverThredhold": qtechNotifyStaActOverThredhold,
       "qtechNotifyStaDisactOverThredhold": qtechNotifyStaDisactOverThredhold,
       "qtechNotifyStaRoamTotal": qtechNotifyStaRoamTotal,
       "qtechNotifyStaRoamPerMin": qtechNotifyStaRoamPerMin,
       "qtechNotifyAcPowerStatus": qtechNotifyAcPowerStatus,
       "qtechNotify86PowerOffAlarm": qtechNotify86PowerOffAlarm,
       "qtechNotify86PowerOffAlarmClear": qtechNotify86PowerOffAlarmClear,
       "qtechNotifyApSwUpdtSuccess": qtechNotifyApSwUpdtSuccess,
       "qtechNotifyApUp": qtechNotifyApUp,
       "qtechNotifyApDown": qtechNotifyApDown,
       "qtechNotifyApSwUpdtFailApMac": qtechNotifyApSwUpdtFailApMac,
       "qtechNotifyApTimeStampFailApMac": qtechNotifyApTimeStampFailApMac,
       "qtechNotifyStaOperAlternate": qtechNotifyStaOperAlternate,
       "qtechAcMgmtAcMIBConformance": qtechAcMgmtAcMIBConformance,
       "qtechAcMgmtAcMIBCompliances": qtechAcMgmtAcMIBCompliances,
       "qtechAcMgmtAcMIBCompliance": qtechAcMgmtAcMIBCompliance,
       "qtechAcMgmtAcMIBGroups": qtechAcMgmtAcMIBGroups,
       "qtechAcMgmtAcMIBGroup": qtechAcMgmtAcMIBGroup,
       "qtechAcMgmtAcTrapGroup": qtechAcMgmtAcTrapGroup}
)
