# SNMP MIB module (RC002-REMOTEII-DEVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RC002-REMOTEII-DEVICE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:36 2025
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

(rcftChassisIndex,
 rcftMibObjects,
 rcftSlotIndex) = mibBuilder.importSymbols(
    "RAISECOM-RCFT-MIB",
    "rcftChassisIndex",
    "rcftMibObjects",
    "rcftSlotIndex")

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
 PhysAddress,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

rcftRemoteIIDeviceMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7)
)
if mibBuilder.loadTexts:
    rcftRemoteIIDeviceMib.setRevisions(
        ("1905-07-06 00:00",
         "1909-02-09 00:00",
         "1909-03-06 15:00",
         "1909-03-23 00:00",
         "1909-04-15 00:00",
         "1909-09-02 10:00",
         "1909-09-08 14:30",
         "1910-04-28 17:34",
         "1910-10-22 16:57")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcftRemoteIIDeviceSystemMIB_ObjectIdentity = ObjectIdentity
rcftRemoteIIDeviceSystemMIB = _RcftRemoteIIDeviceSystemMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 1)
)
_RcftRemoteIIDeviceSysObjects_ObjectIdentity = ObjectIdentity
rcftRemoteIIDeviceSysObjects = _RcftRemoteIIDeviceSysObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 1, 1)
)
_RcftRemoteIIDeviceSysTable_Object = MibTable
rcftRemoteIIDeviceSysTable = _RcftRemoteIIDeviceSysTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteIIDeviceSysTable.setStatus("current")
_RcftRemoteIIDeviceSysEntry_Object = MibTableRow
rcftRemoteIIDeviceSysEntry = _RcftRemoteIIDeviceSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 1, 1, 1, 1)
)
rcftRemoteIIDeviceSysEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-REMOTEII-DEVICE-MIB", "rcftRemoteIIDeviceIndex"),
)
if mibBuilder.loadTexts:
    rcftRemoteIIDeviceSysEntry.setStatus("current")
_RcftRemoteIIDeviceIndex_Type = Integer32
_RcftRemoteIIDeviceIndex_Object = MibTableColumn
rcftRemoteIIDeviceIndex = _RcftRemoteIIDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 1, 1, 1, 1, 1),
    _RcftRemoteIIDeviceIndex_Type()
)
rcftRemoteIIDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIDeviceIndex.setStatus("current")


class _RcftRemoteIIDeviceExist_Type(Integer32):
    """Custom type rcftRemoteIIDeviceExist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exist", 1),
          ("noexist", 2))
    )


_RcftRemoteIIDeviceExist_Type.__name__ = "Integer32"
_RcftRemoteIIDeviceExist_Object = MibTableColumn
rcftRemoteIIDeviceExist = _RcftRemoteIIDeviceExist_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 1, 1, 1, 1, 2),
    _RcftRemoteIIDeviceExist_Type()
)
rcftRemoteIIDeviceExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIDeviceExist.setStatus("current")


class _RcftRemoteIIDeviceType_Type(Integer32):
    """Custom type rcftRemoteIIDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(30001,
              30002,
              30003,
              30004,
              30005,
              30006,
              30007,
              30008,
              30009,
              30010,
              30011,
              30012,
              30013,
              30014,
              30015,
              30016,
              30017,
              30019,
              30020,
              30021,
              30022,
              30023,
              30024,
              30025,
              30026,
              30027,
              30028,
              30029,
              30030,
              65025,
              65026,
              65027)
        )
    )
    namedValues = NamedValues(
        *(("rcftTypeRC501-FE-REV-C", 30001),
          ("rcftTypeRC601-FE-REV-C", 30002),
          ("rcftTypeRC511-FE-REV-A", 30003),
          ("rcftTypeRC511-4FE-REV-A", 30004),
          ("rcftTypeRC601-FE-REV-E", 30005),
          ("rcftTypeRC511-FE-C-REV-A", 30006),
          ("rcftTypeRC513-FE-REV-A", 30007),
          ("rcftTypeRC513-FE-C-REV-A", 30008),
          ("rcftTypeRC532-FE-REV-A", 30009),
          ("rcftTypeRC531-FE-REV-A", 30010),
          ("rcftTypeRC532-2FE-REV-A", 30011),
          ("rcftTypeRC512-FE-DoubleFiber-S-REV-A", 30012),
          ("rcftTypeRC512-FE-SingleFiber-S-REV-A", 30013),
          ("rcftTypeRC512-FE-DoubleFiber-C-REV-A", 30014),
          ("rcftTypeRC512-FE-SingleFiber-C-REV-A", 30015),
          ("rcftTypeRC512-FE-SS34-S-REV-A", 30016),
          ("rcftTypeRC512-FE-SS34-C-REV-A", 30017),
          ("rcftTypeRC512-FE-SS13-SLAVE", 30019),
          ("rcftTypeRC512-FE-SS23-SLAVE", 30020),
          ("rcftTypeRC512-FE-SS34-SLAVE", 30021),
          ("rcftTypeRC552-FE-REV-A-SLAVE-NEW", 30022),
          ("rcftTypeRC511-4FE-REV-B-SLAVE", 30023),
          ("rcftTypeRC521H-FE-DoubleFiber-S", 30024),
          ("rcftTypeRC521H-FE-SingleFiber-S", 30025),
          ("rcftTypeRC521H-FE-S", 30026),
          ("rcftTypeRC522E-FE-REMOTE", 30027),
          ("rcftTypeRC521E-FE", 30028),
          ("rcftTypeRC512-FE", 30029),
          ("rcftTypeRC512-FE-SLAVE", 30030),
          ("rcftTypeTS1000-UNCONFIG-PRODUCT", 65025),
          ("rcftTypeRC521-FE-REV-C", 65026),
          ("rcftTypeRC521-FE-REV-D", 65027))
    )


_RcftRemoteIIDeviceType_Type.__name__ = "Integer32"
_RcftRemoteIIDeviceType_Object = MibTableColumn
rcftRemoteIIDeviceType = _RcftRemoteIIDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 1, 1, 1, 1, 3),
    _RcftRemoteIIDeviceType_Type()
)
rcftRemoteIIDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIDeviceType.setStatus("current")
_RcftRemoteIIDeviceToRDeviceID_Type = Integer32
_RcftRemoteIIDeviceToRDeviceID_Object = MibTableColumn
rcftRemoteIIDeviceToRDeviceID = _RcftRemoteIIDeviceToRDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 1, 1, 1, 1, 4),
    _RcftRemoteIIDeviceToRDeviceID_Type()
)
rcftRemoteIIDeviceToRDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIDeviceToRDeviceID.setStatus("current")


class _RcftRemoteIIDeviceToRPortType_Type(Integer32):
    """Custom type rcftRemoteIIDeviceToRPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethport", 1),
          ("optical", 2),
          ("e1port", 3))
    )


_RcftRemoteIIDeviceToRPortType_Type.__name__ = "Integer32"
_RcftRemoteIIDeviceToRPortType_Object = MibTableColumn
rcftRemoteIIDeviceToRPortType = _RcftRemoteIIDeviceToRPortType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 1, 1, 1, 1, 5),
    _RcftRemoteIIDeviceToRPortType_Type()
)
rcftRemoteIIDeviceToRPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIDeviceToRPortType.setStatus("current")
_RcftRemoteIIDeviceToRPortIndex_Type = Integer32
_RcftRemoteIIDeviceToRPortIndex_Object = MibTableColumn
rcftRemoteIIDeviceToRPortIndex = _RcftRemoteIIDeviceToRPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 1, 1, 1, 1, 6),
    _RcftRemoteIIDeviceToRPortIndex_Type()
)
rcftRemoteIIDeviceToRPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIDeviceToRPortIndex.setStatus("current")


class _RcftRemoteIIDeviceVersionInfo_Type(OctetString):
    """Custom type rcftRemoteIIDeviceVersionInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_RcftRemoteIIDeviceVersionInfo_Type.__name__ = "OctetString"
_RcftRemoteIIDeviceVersionInfo_Object = MibTableColumn
rcftRemoteIIDeviceVersionInfo = _RcftRemoteIIDeviceVersionInfo_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 1, 1, 1, 1, 7),
    _RcftRemoteIIDeviceVersionInfo_Type()
)
rcftRemoteIIDeviceVersionInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIDeviceVersionInfo.setStatus("current")
_RcftRemoteIISysTemperature_Type = Integer32
_RcftRemoteIISysTemperature_Object = MibTableColumn
rcftRemoteIISysTemperature = _RcftRemoteIISysTemperature_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 1, 1, 1, 1, 8),
    _RcftRemoteIISysTemperature_Type()
)
rcftRemoteIISysTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIISysTemperature.setStatus("current")


class _RcftRemoteIISysVoltageStatus_Type(Integer32):
    """Custom type rcftRemoteIISysVoltageStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("toohigh", 2),
          ("toolow", 3))
    )


_RcftRemoteIISysVoltageStatus_Type.__name__ = "Integer32"
_RcftRemoteIISysVoltageStatus_Object = MibTableColumn
rcftRemoteIISysVoltageStatus = _RcftRemoteIISysVoltageStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 1, 1, 1, 1, 9),
    _RcftRemoteIISysVoltageStatus_Type()
)
rcftRemoteIISysVoltageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIISysVoltageStatus.setStatus("current")


class _RcftRemoteIIDeviceFrameLen_Type(Integer32):
    """Custom type rcftRemoteIIDeviceFrameLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("framelen1916B", 1),
          ("framelen1536B", 2))
    )


_RcftRemoteIIDeviceFrameLen_Type.__name__ = "Integer32"
_RcftRemoteIIDeviceFrameLen_Object = MibTableColumn
rcftRemoteIIDeviceFrameLen = _RcftRemoteIIDeviceFrameLen_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 1, 1, 1, 1, 10),
    _RcftRemoteIIDeviceFrameLen_Type()
)
rcftRemoteIIDeviceFrameLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteIIDeviceFrameLen.setStatus("current")


class _RcftRemoteIIDeviceOrder_Type(Integer32):
    """Custom type rcftRemoteIIDeviceOrder based on Integer32"""
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
        *(("reset", 1),
          ("reqInfoStart", 2),
          ("reqInfoStop", 3),
          ("linePortInsideLoopEnable", 4),
          ("linePortOutsideLoopEnable", 5),
          ("linePortInsideLoopDisable", 6),
          ("linePortOutsideLoopDisable", 7))
    )


_RcftRemoteIIDeviceOrder_Type.__name__ = "Integer32"
_RcftRemoteIIDeviceOrder_Object = MibTableColumn
rcftRemoteIIDeviceOrder = _RcftRemoteIIDeviceOrder_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 1, 1, 1, 1, 11),
    _RcftRemoteIIDeviceOrder_Type()
)
rcftRemoteIIDeviceOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteIIDeviceOrder.setStatus("current")


class _RcftRemoteIIDeviceConfigFlag_Type(Integer32):
    """Custom type rcftRemoteIIDeviceConfigFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("set", 1)
    )


_RcftRemoteIIDeviceConfigFlag_Type.__name__ = "Integer32"
_RcftRemoteIIDeviceConfigFlag_Object = MibTableColumn
rcftRemoteIIDeviceConfigFlag = _RcftRemoteIIDeviceConfigFlag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 1, 1, 1, 1, 12),
    _RcftRemoteIIDeviceConfigFlag_Type()
)
rcftRemoteIIDeviceConfigFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteIIDeviceConfigFlag.setStatus("current")
_RcftRemoteIIDeviceStatus_Type = Integer32
_RcftRemoteIIDeviceStatus_Object = MibTableColumn
rcftRemoteIIDeviceStatus = _RcftRemoteIIDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 1, 1, 1, 1, 13),
    _RcftRemoteIIDeviceStatus_Type()
)
rcftRemoteIIDeviceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteIIDeviceStatus.setStatus("current")
_RcftRemoteIIDeviceVenderCode_Type = Integer32
_RcftRemoteIIDeviceVenderCode_Object = MibTableColumn
rcftRemoteIIDeviceVenderCode = _RcftRemoteIIDeviceVenderCode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 1, 1, 1, 1, 14),
    _RcftRemoteIIDeviceVenderCode_Type()
)
rcftRemoteIIDeviceVenderCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIDeviceVenderCode.setStatus("current")
_RcftRemoteIIDeviceModelID_Type = Integer32
_RcftRemoteIIDeviceModelID_Object = MibTableColumn
rcftRemoteIIDeviceModelID = _RcftRemoteIIDeviceModelID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 1, 1, 1, 1, 15),
    _RcftRemoteIIDeviceModelID_Type()
)
rcftRemoteIIDeviceModelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIDeviceModelID.setStatus("current")
_RcftRemoteIIDeviceLoopBackStatus_Type = Integer32
_RcftRemoteIIDeviceLoopBackStatus_Object = MibTableColumn
rcftRemoteIIDeviceLoopBackStatus = _RcftRemoteIIDeviceLoopBackStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 1, 1, 1, 1, 16),
    _RcftRemoteIIDeviceLoopBackStatus_Type()
)
rcftRemoteIIDeviceLoopBackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIDeviceLoopBackStatus.setStatus("current")
_RcftRemoteIIDeviceLoopBackMode_Type = Integer32
_RcftRemoteIIDeviceLoopBackMode_Object = MibTableColumn
rcftRemoteIIDeviceLoopBackMode = _RcftRemoteIIDeviceLoopBackMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 1, 1, 1, 1, 17),
    _RcftRemoteIIDeviceLoopBackMode_Type()
)
rcftRemoteIIDeviceLoopBackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteIIDeviceLoopBackMode.setStatus("current")
_RcftRemoteIIDeviceVLANType_Type = Integer32
_RcftRemoteIIDeviceVLANType_Object = MibTableColumn
rcftRemoteIIDeviceVLANType = _RcftRemoteIIDeviceVLANType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 1, 1, 1, 1, 18),
    _RcftRemoteIIDeviceVLANType_Type()
)
rcftRemoteIIDeviceVLANType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteIIDeviceVLANType.setStatus("current")
_RcftRemoteIIQosEnable_Type = Integer32
_RcftRemoteIIQosEnable_Object = MibTableColumn
rcftRemoteIIQosEnable = _RcftRemoteIIQosEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 1, 1, 1, 1, 19),
    _RcftRemoteIIQosEnable_Type()
)
rcftRemoteIIQosEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteIIQosEnable.setStatus("current")
_RcftRemoteIIBaseCOS_Type = Integer32
_RcftRemoteIIBaseCOS_Object = MibTableColumn
rcftRemoteIIBaseCOS = _RcftRemoteIIBaseCOS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 1, 1, 1, 1, 20),
    _RcftRemoteIIBaseCOS_Type()
)
rcftRemoteIIBaseCOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteIIBaseCOS.setStatus("current")
_RcftRemoteIIQueuesPolicy_Type = Integer32
_RcftRemoteIIQueuesPolicy_Object = MibTableColumn
rcftRemoteIIQueuesPolicy = _RcftRemoteIIQueuesPolicy_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 1, 1, 1, 1, 21),
    _RcftRemoteIIQueuesPolicy_Type()
)
rcftRemoteIIQueuesPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteIIQueuesPolicy.setStatus("current")
_RcftRemoteIIDeviceQoSPolicy_Type = Integer32
_RcftRemoteIIDeviceQoSPolicy_Object = MibTableColumn
rcftRemoteIIDeviceQoSPolicy = _RcftRemoteIIDeviceQoSPolicy_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 1, 1, 1, 1, 22),
    _RcftRemoteIIDeviceQoSPolicy_Type()
)
rcftRemoteIIDeviceQoSPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteIIDeviceQoSPolicy.setStatus("current")


class _RcftRemoteIIDeviceMibUse_Type(Integer32):
    """Custom type rcftRemoteIIDeviceMibUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mib002", 1),
          ("rccomlib", 2))
    )


_RcftRemoteIIDeviceMibUse_Type.__name__ = "Integer32"
_RcftRemoteIIDeviceMibUse_Object = MibTableColumn
rcftRemoteIIDeviceMibUse = _RcftRemoteIIDeviceMibUse_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 1, 1, 1, 1, 23),
    _RcftRemoteIIDeviceMibUse_Type()
)
rcftRemoteIIDeviceMibUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIDeviceMibUse.setStatus("current")
_RcftRemoteIIDeviceConfigFlagTable_Object = MibTable
rcftRemoteIIDeviceConfigFlagTable = _RcftRemoteIIDeviceConfigFlagTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 1, 1, 2)
)
if mibBuilder.loadTexts:
    rcftRemoteIIDeviceConfigFlagTable.setStatus("current")
_RcftRemoteIIDeviceConfigFlagEntry_Object = MibTableRow
rcftRemoteIIDeviceConfigFlagEntry = _RcftRemoteIIDeviceConfigFlagEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 1, 1, 2, 1)
)
rcftRemoteIIDeviceConfigFlagEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-REMOTEII-DEVICE-MIB", "rcftRemoteIIDeviceIndex"),
)
if mibBuilder.loadTexts:
    rcftRemoteIIDeviceConfigFlagEntry.setStatus("current")
_RcftRemoteIIDeviceConfigFinishFlag_Type = Integer32
_RcftRemoteIIDeviceConfigFinishFlag_Object = MibTableColumn
rcftRemoteIIDeviceConfigFinishFlag = _RcftRemoteIIDeviceConfigFinishFlag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 1, 1, 2, 1, 1),
    _RcftRemoteIIDeviceConfigFinishFlag_Type()
)
rcftRemoteIIDeviceConfigFinishFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteIIDeviceConfigFinishFlag.setStatus("current")
_RcftRemoteIIDeviceSysTraps_ObjectIdentity = ObjectIdentity
rcftRemoteIIDeviceSysTraps = _RcftRemoteIIDeviceSysTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 1, 2)
)
_RcftRemoteIIDeviceEthMIB_ObjectIdentity = ObjectIdentity
rcftRemoteIIDeviceEthMIB = _RcftRemoteIIDeviceEthMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2)
)
_RcftRemoteIIDeviceEthFeMIB_ObjectIdentity = ObjectIdentity
rcftRemoteIIDeviceEthFeMIB = _RcftRemoteIIDeviceEthFeMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 1)
)
_RcftRemoteIIDeviceEthFeObjects_ObjectIdentity = ObjectIdentity
rcftRemoteIIDeviceEthFeObjects = _RcftRemoteIIDeviceEthFeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 1, 1)
)
_RcftRemoteIIEthFePortTable_Object = MibTable
rcftRemoteIIEthFePortTable = _RcftRemoteIIEthFePortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteIIEthFePortTable.setStatus("current")
_RcftRemoteIIEthFePortEntry_Object = MibTableRow
rcftRemoteIIEthFePortEntry = _RcftRemoteIIEthFePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 1, 1, 1, 1)
)
rcftRemoteIIEthFePortEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-REMOTEII-DEVICE-MIB", "rcftRemoteIIDeviceIndex"),
    (0, "RC002-REMOTEII-DEVICE-MIB", "rcftRemoteIIEthFeIndex"),
)
if mibBuilder.loadTexts:
    rcftRemoteIIEthFePortEntry.setStatus("current")
_RcftRemoteIIEthFeIndex_Type = Integer32
_RcftRemoteIIEthFeIndex_Object = MibTableColumn
rcftRemoteIIEthFeIndex = _RcftRemoteIIEthFeIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 1, 1, 1, 1, 1),
    _RcftRemoteIIEthFeIndex_Type()
)
rcftRemoteIIEthFeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFeIndex.setStatus("current")


class _RcftRemoteIIEthFeLinkStatus_Type(Integer32):
    """Custom type rcftRemoteIIEthFeLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkup", 1),
          ("linkdown", 2))
    )


_RcftRemoteIIEthFeLinkStatus_Type.__name__ = "Integer32"
_RcftRemoteIIEthFeLinkStatus_Object = MibTableColumn
rcftRemoteIIEthFeLinkStatus = _RcftRemoteIIEthFeLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 1, 1, 1, 1, 2),
    _RcftRemoteIIEthFeLinkStatus_Type()
)
rcftRemoteIIEthFeLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFeLinkStatus.setStatus("current")


class _RcftRemoteIIEthFeShutDown_Type(Integer32):
    """Custom type rcftRemoteIIEthFeShutDown based on Integer32"""
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
        *(("open", 1),
          ("close", 2),
          ("closebyLocalOtherPortFault", 3),
          ("closebyOppositeFePortFault", 4),
          ("closebyLoopBack", 5))
    )


_RcftRemoteIIEthFeShutDown_Type.__name__ = "Integer32"
_RcftRemoteIIEthFeShutDown_Object = MibTableColumn
rcftRemoteIIEthFeShutDown = _RcftRemoteIIEthFeShutDown_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 1, 1, 1, 1, 3),
    _RcftRemoteIIEthFeShutDown_Type()
)
rcftRemoteIIEthFeShutDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFeShutDown.setStatus("current")


class _RcftRemoteIIEthFeAutoNegotiation_Type(Integer32):
    """Custom type rcftRemoteIIEthFeAutoNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manul", 2))
    )


_RcftRemoteIIEthFeAutoNegotiation_Type.__name__ = "Integer32"
_RcftRemoteIIEthFeAutoNegotiation_Object = MibTableColumn
rcftRemoteIIEthFeAutoNegotiation = _RcftRemoteIIEthFeAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 1, 1, 1, 1, 4),
    _RcftRemoteIIEthFeAutoNegotiation_Type()
)
rcftRemoteIIEthFeAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFeAutoNegotiation.setStatus("current")


class _RcftRemoteIIEthFeSpeed_Type(Integer32):
    """Custom type rcftRemoteIIEthFeSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              16)
        )
    )
    namedValues = NamedValues(
        *(("rcft10Mbps", 1),
          ("rcft100Mbps", 2),
          ("rcft1000Mbps", 3),
          ("rcft10Gbps", 4),
          ("other", 16))
    )


_RcftRemoteIIEthFeSpeed_Type.__name__ = "Integer32"
_RcftRemoteIIEthFeSpeed_Object = MibTableColumn
rcftRemoteIIEthFeSpeed = _RcftRemoteIIEthFeSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 1, 1, 1, 1, 5),
    _RcftRemoteIIEthFeSpeed_Type()
)
rcftRemoteIIEthFeSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFeSpeed.setStatus("current")


class _RcftRemoteIIEthFeDuplex_Type(Integer32):
    """Custom type rcftRemoteIIEthFeDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 1),
          ("half-duplex", 2))
    )


_RcftRemoteIIEthFeDuplex_Type.__name__ = "Integer32"
_RcftRemoteIIEthFeDuplex_Object = MibTableColumn
rcftRemoteIIEthFeDuplex = _RcftRemoteIIEthFeDuplex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 1, 1, 1, 1, 6),
    _RcftRemoteIIEthFeDuplex_Type()
)
rcftRemoteIIEthFeDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFeDuplex.setStatus("current")
_RcftRemoteIIEthFeRestrictSpeed_Type = Integer32
_RcftRemoteIIEthFeRestrictSpeed_Object = MibTableColumn
rcftRemoteIIEthFeRestrictSpeed = _RcftRemoteIIEthFeRestrictSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 1, 1, 1, 1, 7),
    _RcftRemoteIIEthFeRestrictSpeed_Type()
)
rcftRemoteIIEthFeRestrictSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFeRestrictSpeed.setStatus("current")


class _RcftRemoteIIEthFeFaultPass_Type(Integer32):
    """Custom type rcftRemoteIIEthFeFaultPass based on Integer32"""
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


_RcftRemoteIIEthFeFaultPass_Type.__name__ = "Integer32"
_RcftRemoteIIEthFeFaultPass_Object = MibTableColumn
rcftRemoteIIEthFeFaultPass = _RcftRemoteIIEthFeFaultPass_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 1, 1, 1, 1, 8),
    _RcftRemoteIIEthFeFaultPass_Type()
)
rcftRemoteIIEthFeFaultPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFeFaultPass.setStatus("current")


class _RcftRemoteIIEthFeDisabledByRemoteTP_Type(Integer32):
    """Custom type rcftRemoteIIEthFeDisabledByRemoteTP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("close", 2))
    )


_RcftRemoteIIEthFeDisabledByRemoteTP_Type.__name__ = "Integer32"
_RcftRemoteIIEthFeDisabledByRemoteTP_Object = MibTableColumn
rcftRemoteIIEthFeDisabledByRemoteTP = _RcftRemoteIIEthFeDisabledByRemoteTP_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 1, 1, 1, 1, 9),
    _RcftRemoteIIEthFeDisabledByRemoteTP_Type()
)
rcftRemoteIIEthFeDisabledByRemoteTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFeDisabledByRemoteTP.setStatus("current")


class _RcftRemoteIIEthFeDisabledByFxToFeFP_Type(Integer32):
    """Custom type rcftRemoteIIEthFeDisabledByFxToFeFP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("close", 2))
    )


_RcftRemoteIIEthFeDisabledByFxToFeFP_Type.__name__ = "Integer32"
_RcftRemoteIIEthFeDisabledByFxToFeFP_Object = MibTableColumn
rcftRemoteIIEthFeDisabledByFxToFeFP = _RcftRemoteIIEthFeDisabledByFxToFeFP_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 1, 1, 1, 1, 10),
    _RcftRemoteIIEthFeDisabledByFxToFeFP_Type()
)
rcftRemoteIIEthFeDisabledByFxToFeFP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFeDisabledByFxToFeFP.setStatus("current")
_RcftRemoteIIEthFeTxRestrictSpeed_Type = Integer32
_RcftRemoteIIEthFeTxRestrictSpeed_Object = MibTableColumn
rcftRemoteIIEthFeTxRestrictSpeed = _RcftRemoteIIEthFeTxRestrictSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 1, 1, 1, 1, 11),
    _RcftRemoteIIEthFeTxRestrictSpeed_Type()
)
rcftRemoteIIEthFeTxRestrictSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFeTxRestrictSpeed.setStatus("current")


class _RcftRemoteIIEthFeTag_Type(Integer32):
    """Custom type rcftRemoteIIEthFeTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tag", 1),
          ("untag", 2))
    )


_RcftRemoteIIEthFeTag_Type.__name__ = "Integer32"
_RcftRemoteIIEthFeTag_Object = MibTableColumn
rcftRemoteIIEthFeTag = _RcftRemoteIIEthFeTag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 1, 1, 1, 1, 12),
    _RcftRemoteIIEthFeTag_Type()
)
rcftRemoteIIEthFeTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFeTag.setStatus("current")
_RcftRemoteIIEthFePVID_Type = Integer32
_RcftRemoteIIEthFePVID_Object = MibTableColumn
rcftRemoteIIEthFePVID = _RcftRemoteIIEthFePVID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 1, 1, 1, 1, 13),
    _RcftRemoteIIEthFePVID_Type()
)
rcftRemoteIIEthFePVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFePVID.setStatus("current")
_RcftRemoteIIEthFeQoSPolicy_Type = Integer32
_RcftRemoteIIEthFeQoSPolicy_Object = MibTableColumn
rcftRemoteIIEthFeQoSPolicy = _RcftRemoteIIEthFeQoSPolicy_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 1, 1, 1, 1, 14),
    _RcftRemoteIIEthFeQoSPolicy_Type()
)
rcftRemoteIIEthFeQoSPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFeQoSPolicy.setStatus("current")
_RcftRemoteIIEthFeStatisticTable_Object = MibTable
rcftRemoteIIEthFeStatisticTable = _RcftRemoteIIEthFeStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    rcftRemoteIIEthFeStatisticTable.setStatus("current")
_RcftRemoteIIEthFeStatisticEntry_Object = MibTableRow
rcftRemoteIIEthFeStatisticEntry = _RcftRemoteIIEthFeStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteIIEthFeStatisticEntry.setStatus("current")
_RcftRemoteIIEthFeTxPackets_Type = Counter32
_RcftRemoteIIEthFeTxPackets_Object = MibTableColumn
rcftRemoteIIEthFeTxPackets = _RcftRemoteIIEthFeTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 1, 1, 2, 1, 1),
    _RcftRemoteIIEthFeTxPackets_Type()
)
rcftRemoteIIEthFeTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFeTxPackets.setStatus("current")
_RcftRemoteIIEthFeTxBytes_Type = Counter32
_RcftRemoteIIEthFeTxBytes_Object = MibTableColumn
rcftRemoteIIEthFeTxBytes = _RcftRemoteIIEthFeTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 1, 1, 2, 1, 2),
    _RcftRemoteIIEthFeTxBytes_Type()
)
rcftRemoteIIEthFeTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFeTxBytes.setStatus("current")
_RcftRemoteIIEthFeRxPackets_Type = Counter32
_RcftRemoteIIEthFeRxPackets_Object = MibTableColumn
rcftRemoteIIEthFeRxPackets = _RcftRemoteIIEthFeRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 1, 1, 2, 1, 3),
    _RcftRemoteIIEthFeRxPackets_Type()
)
rcftRemoteIIEthFeRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFeRxPackets.setStatus("current")
_RcftRemoteIIEthFeRxBytes_Type = Counter32
_RcftRemoteIIEthFeRxBytes_Object = MibTableColumn
rcftRemoteIIEthFeRxBytes = _RcftRemoteIIEthFeRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 1, 1, 2, 1, 4),
    _RcftRemoteIIEthFeRxBytes_Type()
)
rcftRemoteIIEthFeRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFeRxBytes.setStatus("current")
_RcftRemoteIIEthFeRxLostPackets_Type = Counter32
_RcftRemoteIIEthFeRxLostPackets_Object = MibTableColumn
rcftRemoteIIEthFeRxLostPackets = _RcftRemoteIIEthFeRxLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 1, 1, 2, 1, 5),
    _RcftRemoteIIEthFeRxLostPackets_Type()
)
rcftRemoteIIEthFeRxLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFeRxLostPackets.setStatus("current")
_RcftRemoteIIEthFeFluxTimer_Type = Counter32
_RcftRemoteIIEthFeFluxTimer_Object = MibTableColumn
rcftRemoteIIEthFeFluxTimer = _RcftRemoteIIEthFeFluxTimer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 1, 1, 2, 1, 6),
    _RcftRemoteIIEthFeFluxTimer_Type()
)
rcftRemoteIIEthFeFluxTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFeFluxTimer.setStatus("current")
_RcftRemoteIIEthFeTxLostPackets_Type = Counter32
_RcftRemoteIIEthFeTxLostPackets_Object = MibTableColumn
rcftRemoteIIEthFeTxLostPackets = _RcftRemoteIIEthFeTxLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 1, 1, 2, 1, 7),
    _RcftRemoteIIEthFeTxLostPackets_Type()
)
rcftRemoteIIEthFeTxLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFeTxLostPackets.setStatus("current")
_RcftRemoteIIEthFePortConfTable_Object = MibTable
rcftRemoteIIEthFePortConfTable = _RcftRemoteIIEthFePortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    rcftRemoteIIEthFePortConfTable.setStatus("current")
_RcftRemoteIIEthFePortConfEntry_Object = MibTableRow
rcftRemoteIIEthFePortConfEntry = _RcftRemoteIIEthFePortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 1, 1, 3, 1)
)
rcftRemoteIIEthFePortConfEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-REMOTEII-DEVICE-MIB", "rcftRemoteIIDeviceIndex"),
    (0, "RC002-REMOTEII-DEVICE-MIB", "rcftRemoteIIEthFeIndex"),
)
if mibBuilder.loadTexts:
    rcftRemoteIIEthFePortConfEntry.setStatus("current")


class _RcftRemoteIIEthFeConfSpeed_Type(Integer32):
    """Custom type rcftRemoteIIEthFeConfSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              16)
        )
    )
    namedValues = NamedValues(
        *(("rcft10Mbps", 1),
          ("rcft100Mbps", 2),
          ("rcft1000Mbps", 3),
          ("rcft10Gbps", 4),
          ("other", 16))
    )


_RcftRemoteIIEthFeConfSpeed_Type.__name__ = "Integer32"
_RcftRemoteIIEthFeConfSpeed_Object = MibTableColumn
rcftRemoteIIEthFeConfSpeed = _RcftRemoteIIEthFeConfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 1, 1, 3, 1, 1),
    _RcftRemoteIIEthFeConfSpeed_Type()
)
rcftRemoteIIEthFeConfSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFeConfSpeed.setStatus("current")


class _RcftRemoteIIEthFeConfDuplex_Type(Integer32):
    """Custom type rcftRemoteIIEthFeConfDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 1),
          ("half-duplex", 2))
    )


_RcftRemoteIIEthFeConfDuplex_Type.__name__ = "Integer32"
_RcftRemoteIIEthFeConfDuplex_Object = MibTableColumn
rcftRemoteIIEthFeConfDuplex = _RcftRemoteIIEthFeConfDuplex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 1, 1, 3, 1, 2),
    _RcftRemoteIIEthFeConfDuplex_Type()
)
rcftRemoteIIEthFeConfDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFeConfDuplex.setStatus("current")
_RcftRemoteIIDeviceEthFeTraps_ObjectIdentity = ObjectIdentity
rcftRemoteIIDeviceEthFeTraps = _RcftRemoteIIDeviceEthFeTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 1, 2)
)
_RcftRemoteIIDeviceEthFxMIB_ObjectIdentity = ObjectIdentity
rcftRemoteIIDeviceEthFxMIB = _RcftRemoteIIDeviceEthFxMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2)
)
_RcftRemoteIIDeviceEthFxObjects_ObjectIdentity = ObjectIdentity
rcftRemoteIIDeviceEthFxObjects = _RcftRemoteIIDeviceEthFxObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1)
)
_RcftRemoteIIEthFxPortTable_Object = MibTable
rcftRemoteIIEthFxPortTable = _RcftRemoteIIEthFxPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxPortTable.setStatus("current")
_RcftRemoteIIEthFxPortEntry_Object = MibTableRow
rcftRemoteIIEthFxPortEntry = _RcftRemoteIIEthFxPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 1, 1)
)
rcftRemoteIIEthFxPortEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-REMOTEII-DEVICE-MIB", "rcftRemoteIIDeviceIndex"),
    (0, "RC002-REMOTEII-DEVICE-MIB", "rcftRemoteIIEthFxIndex"),
)
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxPortEntry.setStatus("current")
_RcftRemoteIIEthFxIndex_Type = Integer32
_RcftRemoteIIEthFxIndex_Object = MibTableColumn
rcftRemoteIIEthFxIndex = _RcftRemoteIIEthFxIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 1, 1, 1),
    _RcftRemoteIIEthFxIndex_Type()
)
rcftRemoteIIEthFxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxIndex.setStatus("current")


class _RcftRemoteIIEthFxPortRLK_Type(Integer32):
    """Custom type rcftRemoteIIEthFxPortRLK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("link", 1),
          ("unlink", 2))
    )


_RcftRemoteIIEthFxPortRLK_Type.__name__ = "Integer32"
_RcftRemoteIIEthFxPortRLK_Object = MibTableColumn
rcftRemoteIIEthFxPortRLK = _RcftRemoteIIEthFxPortRLK_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 1, 1, 2),
    _RcftRemoteIIEthFxPortRLK_Type()
)
rcftRemoteIIEthFxPortRLK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxPortRLK.setStatus("current")


class _RcftRemoteIIEthFxPortTLK_Type(Integer32):
    """Custom type rcftRemoteIIEthFxPortTLK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("link", 1),
          ("unlink", 2))
    )


_RcftRemoteIIEthFxPortTLK_Type.__name__ = "Integer32"
_RcftRemoteIIEthFxPortTLK_Object = MibTableColumn
rcftRemoteIIEthFxPortTLK = _RcftRemoteIIEthFxPortTLK_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 1, 1, 3),
    _RcftRemoteIIEthFxPortTLK_Type()
)
rcftRemoteIIEthFxPortTLK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxPortTLK.setStatus("current")


class _RcftRemoteIIEthFxPortSD_Type(Integer32):
    """Custom type rcftRemoteIIEthFxPortSD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("sd", 2))
    )


_RcftRemoteIIEthFxPortSD_Type.__name__ = "Integer32"
_RcftRemoteIIEthFxPortSD_Object = MibTableColumn
rcftRemoteIIEthFxPortSD = _RcftRemoteIIEthFxPortSD_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 1, 1, 4),
    _RcftRemoteIIEthFxPortSD_Type()
)
rcftRemoteIIEthFxPortSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxPortSD.setStatus("current")


class _RcftRemoteIIEthFxPortTxPowerAbnormal_Type(Integer32):
    """Custom type rcftRemoteIIEthFxPortTxPowerAbnormal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("abnormal", 2))
    )


_RcftRemoteIIEthFxPortTxPowerAbnormal_Type.__name__ = "Integer32"
_RcftRemoteIIEthFxPortTxPowerAbnormal_Object = MibTableColumn
rcftRemoteIIEthFxPortTxPowerAbnormal = _RcftRemoteIIEthFxPortTxPowerAbnormal_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 1, 1, 5),
    _RcftRemoteIIEthFxPortTxPowerAbnormal_Type()
)
rcftRemoteIIEthFxPortTxPowerAbnormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxPortTxPowerAbnormal.setStatus("current")


class _RcftRemoteIIEthFxPortRxSensitiveAbnormal_Type(Integer32):
    """Custom type rcftRemoteIIEthFxPortRxSensitiveAbnormal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("abnormal", 2))
    )


_RcftRemoteIIEthFxPortRxSensitiveAbnormal_Type.__name__ = "Integer32"
_RcftRemoteIIEthFxPortRxSensitiveAbnormal_Object = MibTableColumn
rcftRemoteIIEthFxPortRxSensitiveAbnormal = _RcftRemoteIIEthFxPortRxSensitiveAbnormal_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 1, 1, 6),
    _RcftRemoteIIEthFxPortRxSensitiveAbnormal_Type()
)
rcftRemoteIIEthFxPortRxSensitiveAbnormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxPortRxSensitiveAbnormal.setStatus("current")


class _RcftRemoteIIEthFxPortLaserAbnormal_Type(Integer32):
    """Custom type rcftRemoteIIEthFxPortLaserAbnormal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("abnormal", 2))
    )


_RcftRemoteIIEthFxPortLaserAbnormal_Type.__name__ = "Integer32"
_RcftRemoteIIEthFxPortLaserAbnormal_Object = MibTableColumn
rcftRemoteIIEthFxPortLaserAbnormal = _RcftRemoteIIEthFxPortLaserAbnormal_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 1, 1, 7),
    _RcftRemoteIIEthFxPortLaserAbnormal_Type()
)
rcftRemoteIIEthFxPortLaserAbnormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxPortLaserAbnormal.setStatus("current")


class _RcftRemoteIIEthFxPortModuleType_Type(Integer32):
    """Custom type rcftRemoteIIEthFxPortModuleType based on Integer32"""
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
              100)
        )
    )
    namedValues = NamedValues(
        *(("optical-M", 1),
          ("optical-S1", 2),
          ("optical-S2", 3),
          ("optical-S3", 4),
          ("optical-SS13", 5),
          ("optical-SS15", 6),
          ("optical-SS23", 7),
          ("optical-SS25", 8),
          ("optical-SS34", 9),
          ("optical-SS35", 10),
          ("unknown-type", 100))
    )


_RcftRemoteIIEthFxPortModuleType_Type.__name__ = "Integer32"
_RcftRemoteIIEthFxPortModuleType_Object = MibTableColumn
rcftRemoteIIEthFxPortModuleType = _RcftRemoteIIEthFxPortModuleType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 1, 1, 8),
    _RcftRemoteIIEthFxPortModuleType_Type()
)
rcftRemoteIIEthFxPortModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxPortModuleType.setStatus("current")


class _RcftRemoteIIEthFxPortFaultPass_Type(Integer32):
    """Custom type rcftRemoteIIEthFxPortFaultPass based on Integer32"""
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


_RcftRemoteIIEthFxPortFaultPass_Type.__name__ = "Integer32"
_RcftRemoteIIEthFxPortFaultPass_Object = MibTableColumn
rcftRemoteIIEthFxPortFaultPass = _RcftRemoteIIEthFxPortFaultPass_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 1, 1, 9),
    _RcftRemoteIIEthFxPortFaultPass_Type()
)
rcftRemoteIIEthFxPortFaultPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxPortFaultPass.setStatus("current")


class _RcftRemoteIIEthFxPortLink_Type(Integer32):
    """Custom type rcftRemoteIIEthFxPortLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("link", 1),
          ("unlink", 2))
    )


_RcftRemoteIIEthFxPortLink_Type.__name__ = "Integer32"
_RcftRemoteIIEthFxPortLink_Object = MibTableColumn
rcftRemoteIIEthFxPortLink = _RcftRemoteIIEthFxPortLink_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 1, 1, 10),
    _RcftRemoteIIEthFxPortLink_Type()
)
rcftRemoteIIEthFxPortLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxPortLink.setStatus("current")


class _RcftRemoteIIEthFxRxToTxFaultPass_Type(Integer32):
    """Custom type rcftRemoteIIEthFxRxToTxFaultPass based on Integer32"""
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


_RcftRemoteIIEthFxRxToTxFaultPass_Type.__name__ = "Integer32"
_RcftRemoteIIEthFxRxToTxFaultPass_Object = MibTableColumn
rcftRemoteIIEthFxRxToTxFaultPass = _RcftRemoteIIEthFxRxToTxFaultPass_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 1, 1, 11),
    _RcftRemoteIIEthFxRxToTxFaultPass_Type()
)
rcftRemoteIIEthFxRxToTxFaultPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxRxToTxFaultPass.setStatus("current")


class _RcftRemoteIIEthFxTxDisabledByFR_Type(Integer32):
    """Custom type rcftRemoteIIEthFxTxDisabledByFR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("close", 2))
    )


_RcftRemoteIIEthFxTxDisabledByFR_Type.__name__ = "Integer32"
_RcftRemoteIIEthFxTxDisabledByFR_Object = MibTableColumn
rcftRemoteIIEthFxTxDisabledByFR = _RcftRemoteIIEthFxTxDisabledByFR_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 1, 1, 12),
    _RcftRemoteIIEthFxTxDisabledByFR_Type()
)
rcftRemoteIIEthFxTxDisabledByFR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxTxDisabledByFR.setStatus("current")


class _RcftRemoteIIEthFxShutDown_Type(Integer32):
    """Custom type rcftRemoteIIEthFxShutDown based on Integer32"""
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
        *(("open", 1),
          ("close", 2),
          ("closeByFP", 3),
          ("closeByALS", 4),
          ("closeByLP", 5))
    )


_RcftRemoteIIEthFxShutDown_Type.__name__ = "Integer32"
_RcftRemoteIIEthFxShutDown_Object = MibTableColumn
rcftRemoteIIEthFxShutDown = _RcftRemoteIIEthFxShutDown_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 1, 1, 13),
    _RcftRemoteIIEthFxShutDown_Type()
)
rcftRemoteIIEthFxShutDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxShutDown.setStatus("current")


class _RcftRemoteIIEthFxPortAutoNegotiation_Type(Integer32):
    """Custom type rcftRemoteIIEthFxPortAutoNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manul", 2))
    )


_RcftRemoteIIEthFxPortAutoNegotiation_Type.__name__ = "Integer32"
_RcftRemoteIIEthFxPortAutoNegotiation_Object = MibTableColumn
rcftRemoteIIEthFxPortAutoNegotiation = _RcftRemoteIIEthFxPortAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 1, 1, 14),
    _RcftRemoteIIEthFxPortAutoNegotiation_Type()
)
rcftRemoteIIEthFxPortAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxPortAutoNegotiation.setStatus("current")


class _RcftRemoteIIEthFxPortOptHeadType_Type(Integer32):
    """Custom type rcftRemoteIIEthFxPortOptHeadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sfpType", 1),
          ("normal", 2))
    )


_RcftRemoteIIEthFxPortOptHeadType_Type.__name__ = "Integer32"
_RcftRemoteIIEthFxPortOptHeadType_Object = MibTableColumn
rcftRemoteIIEthFxPortOptHeadType = _RcftRemoteIIEthFxPortOptHeadType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 1, 1, 15),
    _RcftRemoteIIEthFxPortOptHeadType_Type()
)
rcftRemoteIIEthFxPortOptHeadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxPortOptHeadType.setStatus("current")


class _RcftRemoteIIEthFxSfpRXLOS_Type(Integer32):
    """Custom type rcftRemoteIIEthFxSfpRXLOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("alarm", 2))
    )


_RcftRemoteIIEthFxSfpRXLOS_Type.__name__ = "Integer32"
_RcftRemoteIIEthFxSfpRXLOS_Object = MibTableColumn
rcftRemoteIIEthFxSfpRXLOS = _RcftRemoteIIEthFxSfpRXLOS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 1, 1, 16),
    _RcftRemoteIIEthFxSfpRXLOS_Type()
)
rcftRemoteIIEthFxSfpRXLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxSfpRXLOS.setStatus("current")


class _RcftRemoteIIEthFxSfpTXDisable_Type(Integer32):
    """Custom type rcftRemoteIIEthFxSfpTXDisable based on Integer32"""
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


_RcftRemoteIIEthFxSfpTXDisable_Type.__name__ = "Integer32"
_RcftRemoteIIEthFxSfpTXDisable_Object = MibTableColumn
rcftRemoteIIEthFxSfpTXDisable = _RcftRemoteIIEthFxSfpTXDisable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 1, 1, 17),
    _RcftRemoteIIEthFxSfpTXDisable_Type()
)
rcftRemoteIIEthFxSfpTXDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxSfpTXDisable.setStatus("current")


class _RcftRemoteIIEthFxSfpExist_Type(Integer32):
    """Custom type rcftRemoteIIEthFxSfpExist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exist", 1),
          ("notExist", 2))
    )


_RcftRemoteIIEthFxSfpExist_Type.__name__ = "Integer32"
_RcftRemoteIIEthFxSfpExist_Object = MibTableColumn
rcftRemoteIIEthFxSfpExist = _RcftRemoteIIEthFxSfpExist_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 1, 1, 18),
    _RcftRemoteIIEthFxSfpExist_Type()
)
rcftRemoteIIEthFxSfpExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxSfpExist.setStatus("current")


class _RcftRemoteIIEthFxSfpSpeedStatus_Type(Integer32):
    """Custom type rcftRemoteIIEthFxSfpSpeedStatus based on Integer32"""
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
        *(("unknown", 1),
          ("speed155M", 2),
          ("speed622M", 3),
          ("speed1250M", 4),
          ("speed2500M", 5))
    )


_RcftRemoteIIEthFxSfpSpeedStatus_Type.__name__ = "Integer32"
_RcftRemoteIIEthFxSfpSpeedStatus_Object = MibTableColumn
rcftRemoteIIEthFxSfpSpeedStatus = _RcftRemoteIIEthFxSfpSpeedStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 1, 1, 19),
    _RcftRemoteIIEthFxSfpSpeedStatus_Type()
)
rcftRemoteIIEthFxSfpSpeedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxSfpSpeedStatus.setStatus("current")
_RcftRemoteIIEthFxSfpTransportDistance_Type = Integer32
_RcftRemoteIIEthFxSfpTransportDistance_Object = MibTableColumn
rcftRemoteIIEthFxSfpTransportDistance = _RcftRemoteIIEthFxSfpTransportDistance_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 1, 1, 20),
    _RcftRemoteIIEthFxSfpTransportDistance_Type()
)
rcftRemoteIIEthFxSfpTransportDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxSfpTransportDistance.setStatus("current")
_RcftRemoteIIEthFxSfpWaveLength_Type = Integer32
_RcftRemoteIIEthFxSfpWaveLength_Object = MibTableColumn
rcftRemoteIIEthFxSfpWaveLength = _RcftRemoteIIEthFxSfpWaveLength_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 1, 1, 21),
    _RcftRemoteIIEthFxSfpWaveLength_Type()
)
rcftRemoteIIEthFxSfpWaveLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxSfpWaveLength.setStatus("current")


class _RcftRemoteIIEthFxSfpManufactory_Type(OctetString):
    """Custom type rcftRemoteIIEthFxSfpManufactory based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RcftRemoteIIEthFxSfpManufactory_Type.__name__ = "OctetString"
_RcftRemoteIIEthFxSfpManufactory_Object = MibTableColumn
rcftRemoteIIEthFxSfpManufactory = _RcftRemoteIIEthFxSfpManufactory_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 1, 1, 22),
    _RcftRemoteIIEthFxSfpManufactory_Type()
)
rcftRemoteIIEthFxSfpManufactory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxSfpManufactory.setStatus("current")


class _RcftRemoteIIEthFxSfpProductType_Type(OctetString):
    """Custom type rcftRemoteIIEthFxSfpProductType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RcftRemoteIIEthFxSfpProductType_Type.__name__ = "OctetString"
_RcftRemoteIIEthFxSfpProductType_Object = MibTableColumn
rcftRemoteIIEthFxSfpProductType = _RcftRemoteIIEthFxSfpProductType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 1, 1, 23),
    _RcftRemoteIIEthFxSfpProductType_Type()
)
rcftRemoteIIEthFxSfpProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxSfpProductType.setStatus("current")


class _RcftRemoteIIEthFxSfpVersion_Type(OctetString):
    """Custom type rcftRemoteIIEthFxSfpVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_RcftRemoteIIEthFxSfpVersion_Type.__name__ = "OctetString"
_RcftRemoteIIEthFxSfpVersion_Object = MibTableColumn
rcftRemoteIIEthFxSfpVersion = _RcftRemoteIIEthFxSfpVersion_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 1, 1, 24),
    _RcftRemoteIIEthFxSfpVersion_Type()
)
rcftRemoteIIEthFxSfpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxSfpVersion.setStatus("current")


class _RcftRemoteIIEthFxSfpWaterMask_Type(OctetString):
    """Custom type rcftRemoteIIEthFxSfpWaterMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RcftRemoteIIEthFxSfpWaterMask_Type.__name__ = "OctetString"
_RcftRemoteIIEthFxSfpWaterMask_Object = MibTableColumn
rcftRemoteIIEthFxSfpWaterMask = _RcftRemoteIIEthFxSfpWaterMask_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 1, 1, 25),
    _RcftRemoteIIEthFxSfpWaterMask_Type()
)
rcftRemoteIIEthFxSfpWaterMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxSfpWaterMask.setStatus("current")


class _RcftRemoteIIEthFxSfpMediaType_Type(Integer32):
    """Custom type rcftRemoteIIEthFxSfpMediaType based on Integer32"""
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
        *(("unknown", 1),
          ("fiber9u125u", 2),
          ("fiber50u125u", 3),
          ("fiber625u125u", 4),
          ("copper", 5))
    )


_RcftRemoteIIEthFxSfpMediaType_Type.__name__ = "Integer32"
_RcftRemoteIIEthFxSfpMediaType_Object = MibTableColumn
rcftRemoteIIEthFxSfpMediaType = _RcftRemoteIIEthFxSfpMediaType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 1, 1, 26),
    _RcftRemoteIIEthFxSfpMediaType_Type()
)
rcftRemoteIIEthFxSfpMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxSfpMediaType.setStatus("current")


class _RcftRemoteIIEthFxSfpModuleType_Type(Integer32):
    """Custom type rcftRemoteIIEthFxSfpModuleType based on Integer32"""
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
          ("gbic", 2),
          ("sff", 3),
          ("sfp", 4))
    )


_RcftRemoteIIEthFxSfpModuleType_Type.__name__ = "Integer32"
_RcftRemoteIIEthFxSfpModuleType_Object = MibTableColumn
rcftRemoteIIEthFxSfpModuleType = _RcftRemoteIIEthFxSfpModuleType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 1, 1, 27),
    _RcftRemoteIIEthFxSfpModuleType_Type()
)
rcftRemoteIIEthFxSfpModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxSfpModuleType.setStatus("current")


class _RcftRemoteIIEthFxSfpOpticalInterface_Type(Integer32):
    """Custom type rcftRemoteIIEthFxSfpOpticalInterface based on Integer32"""
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
          ("sc", 2),
          ("lc", 3),
          ("rj45", 4))
    )


_RcftRemoteIIEthFxSfpOpticalInterface_Type.__name__ = "Integer32"
_RcftRemoteIIEthFxSfpOpticalInterface_Object = MibTableColumn
rcftRemoteIIEthFxSfpOpticalInterface = _RcftRemoteIIEthFxSfpOpticalInterface_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 1, 1, 28),
    _RcftRemoteIIEthFxSfpOpticalInterface_Type()
)
rcftRemoteIIEthFxSfpOpticalInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxSfpOpticalInterface.setStatus("current")


class _RcftRemoteIIEthFxUntag_Type(Integer32):
    """Custom type rcftRemoteIIEthFxUntag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("untag", 1),
          ("tag", 2))
    )


_RcftRemoteIIEthFxUntag_Type.__name__ = "Integer32"
_RcftRemoteIIEthFxUntag_Object = MibTableColumn
rcftRemoteIIEthFxUntag = _RcftRemoteIIEthFxUntag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 1, 1, 29),
    _RcftRemoteIIEthFxUntag_Type()
)
rcftRemoteIIEthFxUntag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxUntag.setStatus("current")
_RcftRemoteIIEthFxPVID_Type = Integer32
_RcftRemoteIIEthFxPVID_Object = MibTableColumn
rcftRemoteIIEthFxPVID = _RcftRemoteIIEthFxPVID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 1, 1, 30),
    _RcftRemoteIIEthFxPVID_Type()
)
rcftRemoteIIEthFxPVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxPVID.setStatus("current")
_RcftRemoteIIEthFxStatisticTable_Object = MibTable
rcftRemoteIIEthFxStatisticTable = _RcftRemoteIIEthFxStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxStatisticTable.setStatus("current")
_RcftRemoteIIEthFxStatisticEntry_Object = MibTableRow
rcftRemoteIIEthFxStatisticEntry = _RcftRemoteIIEthFxStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxStatisticEntry.setStatus("current")
_RcftRemoteIIEthFxTxPackets_Type = Counter32
_RcftRemoteIIEthFxTxPackets_Object = MibTableColumn
rcftRemoteIIEthFxTxPackets = _RcftRemoteIIEthFxTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 2, 1, 1),
    _RcftRemoteIIEthFxTxPackets_Type()
)
rcftRemoteIIEthFxTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxTxPackets.setStatus("current")
_RcftRemoteIIEthFxTxBytes_Type = Counter32
_RcftRemoteIIEthFxTxBytes_Object = MibTableColumn
rcftRemoteIIEthFxTxBytes = _RcftRemoteIIEthFxTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 2, 1, 2),
    _RcftRemoteIIEthFxTxBytes_Type()
)
rcftRemoteIIEthFxTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxTxBytes.setStatus("current")
_RcftRemoteIIEthFxRxPackets_Type = Counter32
_RcftRemoteIIEthFxRxPackets_Object = MibTableColumn
rcftRemoteIIEthFxRxPackets = _RcftRemoteIIEthFxRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 2, 1, 3),
    _RcftRemoteIIEthFxRxPackets_Type()
)
rcftRemoteIIEthFxRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxRxPackets.setStatus("current")
_RcftRemoteIIEthFxRxBytes_Type = Counter32
_RcftRemoteIIEthFxRxBytes_Object = MibTableColumn
rcftRemoteIIEthFxRxBytes = _RcftRemoteIIEthFxRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 2, 1, 4),
    _RcftRemoteIIEthFxRxBytes_Type()
)
rcftRemoteIIEthFxRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxRxBytes.setStatus("current")
_RcftRemoteIIEthFxRxLostPackets_Type = Counter32
_RcftRemoteIIEthFxRxLostPackets_Object = MibTableColumn
rcftRemoteIIEthFxRxLostPackets = _RcftRemoteIIEthFxRxLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 2, 1, 5),
    _RcftRemoteIIEthFxRxLostPackets_Type()
)
rcftRemoteIIEthFxRxLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxRxLostPackets.setStatus("current")
_RcftRemoteIIEthFxFluxTimer_Type = Counter32
_RcftRemoteIIEthFxFluxTimer_Object = MibTableColumn
rcftRemoteIIEthFxFluxTimer = _RcftRemoteIIEthFxFluxTimer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 2, 1, 6),
    _RcftRemoteIIEthFxFluxTimer_Type()
)
rcftRemoteIIEthFxFluxTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxFluxTimer.setStatus("current")
_RcftRemoteIIEthFxTxLostPackets_Type = Counter32
_RcftRemoteIIEthFxTxLostPackets_Object = MibTableColumn
rcftRemoteIIEthFxTxLostPackets = _RcftRemoteIIEthFxTxLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 1, 2, 1, 7),
    _RcftRemoteIIEthFxTxLostPackets_Type()
)
rcftRemoteIIEthFxTxLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxTxLostPackets.setStatus("current")
_RcftRemoteIIDeviceEthFxTraps_ObjectIdentity = ObjectIdentity
rcftRemoteIIDeviceEthFxTraps = _RcftRemoteIIDeviceEthFxTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 2)
)
_RcftRemoteIIDeviceVLANMIB_ObjectIdentity = ObjectIdentity
rcftRemoteIIDeviceVLANMIB = _RcftRemoteIIDeviceVLANMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 3)
)
_RcftRemoteIIDeviceVLANObjects_ObjectIdentity = ObjectIdentity
rcftRemoteIIDeviceVLANObjects = _RcftRemoteIIDeviceVLANObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 3, 1)
)
_RcftRemoteIIDeviceVLANTable_Object = MibTable
rcftRemoteIIDeviceVLANTable = _RcftRemoteIIDeviceVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 3, 1, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteIIDeviceVLANTable.setStatus("current")
_RcftRemoteIIDeviceVLANEntry_Object = MibTableRow
rcftRemoteIIDeviceVLANEntry = _RcftRemoteIIDeviceVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 3, 1, 1, 1)
)
rcftRemoteIIDeviceVLANEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-REMOTEII-DEVICE-MIB", "rcftRemoteIIDeviceIndex"),
    (0, "RC002-REMOTEII-DEVICE-MIB", "rcftRemoteIIVLANIndex"),
)
if mibBuilder.loadTexts:
    rcftRemoteIIDeviceVLANEntry.setStatus("current")
_RcftRemoteIIVLANIndex_Type = Integer32
_RcftRemoteIIVLANIndex_Object = MibTableColumn
rcftRemoteIIVLANIndex = _RcftRemoteIIVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 3, 1, 1, 1, 1),
    _RcftRemoteIIVLANIndex_Type()
)
rcftRemoteIIVLANIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteIIVLANIndex.setStatus("current")
_RcftRemoteIIVLANStatus_Type = Integer32
_RcftRemoteIIVLANStatus_Object = MibTableColumn
rcftRemoteIIVLANStatus = _RcftRemoteIIVLANStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 3, 1, 1, 1, 2),
    _RcftRemoteIIVLANStatus_Type()
)
rcftRemoteIIVLANStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteIIVLANStatus.setStatus("current")
_RcftRemoteIIVLANmember_Type = Integer32
_RcftRemoteIIVLANmember_Object = MibTableColumn
rcftRemoteIIVLANmember = _RcftRemoteIIVLANmember_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 3, 1, 1, 1, 3),
    _RcftRemoteIIVLANmember_Type()
)
rcftRemoteIIVLANmember.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteIIVLANmember.setStatus("current")
_RcftRemoteIIVID_Type = Integer32
_RcftRemoteIIVID_Object = MibTableColumn
rcftRemoteIIVID = _RcftRemoteIIVID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 3, 1, 1, 1, 4),
    _RcftRemoteIIVID_Type()
)
rcftRemoteIIVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteIIVID.setStatus("current")
rcftRemoteIIEthFePortEntry.registerAugmentions(
    ("RC002-REMOTEII-DEVICE-MIB",
     "rcftRemoteIIEthFeStatisticEntry")
)
rcftRemoteIIEthFeStatisticEntry.setIndexNames(*rcftRemoteIIEthFePortEntry.getIndexNames())
rcftRemoteIIEthFxPortEntry.registerAugmentions(
    ("RC002-REMOTEII-DEVICE-MIB",
     "rcftRemoteIIEthFxStatisticEntry")
)
rcftRemoteIIEthFxStatisticEntry.setIndexNames(*rcftRemoteIIEthFxPortEntry.getIndexNames())

# Managed Objects groups


# Notification objects

rcftRemoteIIDevExistTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 1, 2, 1)
)
rcftRemoteIIDevExistTrap.setObjects(
    ("RC002-REMOTEII-DEVICE-MIB", "rcftRemoteIIDeviceExist")
)
if mibBuilder.loadTexts:
    rcftRemoteIIDevExistTrap.setStatus(
        "current"
    )

rcftRemoteIIDevVoltTooHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 1, 2, 2)
)
rcftRemoteIIDevVoltTooHighTrap.setObjects(
    ("RC002-REMOTEII-DEVICE-MIB", "rcftRemoteIISysVoltageStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteIIDevVoltTooHighTrap.setStatus(
        "current"
    )

rcftRemoteIIDevVoltTooLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 1, 2, 3)
)
rcftRemoteIIDevVoltTooLowTrap.setObjects(
    ("RC002-REMOTEII-DEVICE-MIB", "rcftRemoteIISysVoltageStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteIIDevVoltTooLowTrap.setStatus(
        "current"
    )

rcftRemoteIIDevTmptTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 1, 2, 4)
)
rcftRemoteIIDevTmptTrap.setObjects(
    ("RC002-REMOTEII-DEVICE-MIB", "rcftRemoteIISysTemperature")
)
if mibBuilder.loadTexts:
    rcftRemoteIIDevTmptTrap.setStatus(
        "current"
    )

rcftRemoteIIEthFeLinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 1, 2, 1)
)
rcftRemoteIIEthFeLinkTrap.setObjects(
    ("RC002-REMOTEII-DEVICE-MIB", "rcftRemoteIIEthFeLinkStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteIIEthFeLinkTrap.setStatus(
        "current"
    )

rcftRemoteIIEthFxPortRLKTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 2, 1)
)
rcftRemoteIIEthFxPortRLKTrap.setObjects(
    ("RC002-REMOTEII-DEVICE-MIB", "rcftRemoteIIEthFxPortRLK")
)
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxPortRLKTrap.setStatus(
        "current"
    )

rcftRemoteIIEthFxPortTLKTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 2, 2)
)
rcftRemoteIIEthFxPortTLKTrap.setObjects(
    ("RC002-REMOTEII-DEVICE-MIB", "rcftRemoteIIEthFxPortTLK")
)
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxPortTLKTrap.setStatus(
        "current"
    )

rcftRemoteIIEthFxPortTxPowerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 2, 3)
)
rcftRemoteIIEthFxPortTxPowerTrap.setObjects(
    ("RC002-REMOTEII-DEVICE-MIB", "rcftRemoteIIEthFxPortTxPowerAbnormal")
)
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxPortTxPowerTrap.setStatus(
        "current"
    )

rcftRemoteIIEthFxPortRxSensitiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 2, 4)
)
rcftRemoteIIEthFxPortRxSensitiveTrap.setObjects(
    ("RC002-REMOTEII-DEVICE-MIB", "rcftRemoteIIEthFxPortRxSensitiveAbnormal")
)
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxPortRxSensitiveTrap.setStatus(
        "current"
    )

rcftRemoteIIEthFxPortLaserTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 2, 5)
)
rcftRemoteIIEthFxPortLaserTrap.setObjects(
    ("RC002-REMOTEII-DEVICE-MIB", "rcftRemoteIIEthFxPortLaserAbnormal")
)
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxPortLaserTrap.setStatus(
        "current"
    )

rcftRemoteIIEthFxPortSDTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 2, 6)
)
rcftRemoteIIEthFxPortSDTrap.setObjects(
    ("RC002-REMOTEII-DEVICE-MIB", "rcftRemoteIIEthFxPortSD")
)
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxPortSDTrap.setStatus(
        "current"
    )

rcftRemoteIIEthFxPortLinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 2, 7)
)
rcftRemoteIIEthFxPortLinkTrap.setObjects(
    ("RC002-REMOTEII-DEVICE-MIB", "rcftRemoteIIEthFxPortLink")
)
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxPortLinkTrap.setStatus(
        "current"
    )

rcftRemoteIIEthFxPortSfpRXLOSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 2, 8)
)
rcftRemoteIIEthFxPortSfpRXLOSTrap.setObjects(
    ("RC002-REMOTEII-DEVICE-MIB", "rcftRemoteIIEthFxSfpRXLOS")
)
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxPortSfpRXLOSTrap.setStatus(
        "current"
    )

rcftRemoteIIEthFxPortSfpExistTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 7, 2, 2, 2, 9)
)
rcftRemoteIIEthFxPortSfpExistTrap.setObjects(
    ("RC002-REMOTEII-DEVICE-MIB", "rcftRemoteIIEthFxSfpExist")
)
if mibBuilder.loadTexts:
    rcftRemoteIIEthFxPortSfpExistTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RC002-REMOTEII-DEVICE-MIB",
    **{"rcftRemoteIIDeviceMib": rcftRemoteIIDeviceMib,
       "rcftRemoteIIDeviceSystemMIB": rcftRemoteIIDeviceSystemMIB,
       "rcftRemoteIIDeviceSysObjects": rcftRemoteIIDeviceSysObjects,
       "rcftRemoteIIDeviceSysTable": rcftRemoteIIDeviceSysTable,
       "rcftRemoteIIDeviceSysEntry": rcftRemoteIIDeviceSysEntry,
       "rcftRemoteIIDeviceIndex": rcftRemoteIIDeviceIndex,
       "rcftRemoteIIDeviceExist": rcftRemoteIIDeviceExist,
       "rcftRemoteIIDeviceType": rcftRemoteIIDeviceType,
       "rcftRemoteIIDeviceToRDeviceID": rcftRemoteIIDeviceToRDeviceID,
       "rcftRemoteIIDeviceToRPortType": rcftRemoteIIDeviceToRPortType,
       "rcftRemoteIIDeviceToRPortIndex": rcftRemoteIIDeviceToRPortIndex,
       "rcftRemoteIIDeviceVersionInfo": rcftRemoteIIDeviceVersionInfo,
       "rcftRemoteIISysTemperature": rcftRemoteIISysTemperature,
       "rcftRemoteIISysVoltageStatus": rcftRemoteIISysVoltageStatus,
       "rcftRemoteIIDeviceFrameLen": rcftRemoteIIDeviceFrameLen,
       "rcftRemoteIIDeviceOrder": rcftRemoteIIDeviceOrder,
       "rcftRemoteIIDeviceConfigFlag": rcftRemoteIIDeviceConfigFlag,
       "rcftRemoteIIDeviceStatus": rcftRemoteIIDeviceStatus,
       "rcftRemoteIIDeviceVenderCode": rcftRemoteIIDeviceVenderCode,
       "rcftRemoteIIDeviceModelID": rcftRemoteIIDeviceModelID,
       "rcftRemoteIIDeviceLoopBackStatus": rcftRemoteIIDeviceLoopBackStatus,
       "rcftRemoteIIDeviceLoopBackMode": rcftRemoteIIDeviceLoopBackMode,
       "rcftRemoteIIDeviceVLANType": rcftRemoteIIDeviceVLANType,
       "rcftRemoteIIQosEnable": rcftRemoteIIQosEnable,
       "rcftRemoteIIBaseCOS": rcftRemoteIIBaseCOS,
       "rcftRemoteIIQueuesPolicy": rcftRemoteIIQueuesPolicy,
       "rcftRemoteIIDeviceQoSPolicy": rcftRemoteIIDeviceQoSPolicy,
       "rcftRemoteIIDeviceMibUse": rcftRemoteIIDeviceMibUse,
       "rcftRemoteIIDeviceConfigFlagTable": rcftRemoteIIDeviceConfigFlagTable,
       "rcftRemoteIIDeviceConfigFlagEntry": rcftRemoteIIDeviceConfigFlagEntry,
       "rcftRemoteIIDeviceConfigFinishFlag": rcftRemoteIIDeviceConfigFinishFlag,
       "rcftRemoteIIDeviceSysTraps": rcftRemoteIIDeviceSysTraps,
       "rcftRemoteIIDevExistTrap": rcftRemoteIIDevExistTrap,
       "rcftRemoteIIDevVoltTooHighTrap": rcftRemoteIIDevVoltTooHighTrap,
       "rcftRemoteIIDevVoltTooLowTrap": rcftRemoteIIDevVoltTooLowTrap,
       "rcftRemoteIIDevTmptTrap": rcftRemoteIIDevTmptTrap,
       "rcftRemoteIIDeviceEthMIB": rcftRemoteIIDeviceEthMIB,
       "rcftRemoteIIDeviceEthFeMIB": rcftRemoteIIDeviceEthFeMIB,
       "rcftRemoteIIDeviceEthFeObjects": rcftRemoteIIDeviceEthFeObjects,
       "rcftRemoteIIEthFePortTable": rcftRemoteIIEthFePortTable,
       "rcftRemoteIIEthFePortEntry": rcftRemoteIIEthFePortEntry,
       "rcftRemoteIIEthFeIndex": rcftRemoteIIEthFeIndex,
       "rcftRemoteIIEthFeLinkStatus": rcftRemoteIIEthFeLinkStatus,
       "rcftRemoteIIEthFeShutDown": rcftRemoteIIEthFeShutDown,
       "rcftRemoteIIEthFeAutoNegotiation": rcftRemoteIIEthFeAutoNegotiation,
       "rcftRemoteIIEthFeSpeed": rcftRemoteIIEthFeSpeed,
       "rcftRemoteIIEthFeDuplex": rcftRemoteIIEthFeDuplex,
       "rcftRemoteIIEthFeRestrictSpeed": rcftRemoteIIEthFeRestrictSpeed,
       "rcftRemoteIIEthFeFaultPass": rcftRemoteIIEthFeFaultPass,
       "rcftRemoteIIEthFeDisabledByRemoteTP": rcftRemoteIIEthFeDisabledByRemoteTP,
       "rcftRemoteIIEthFeDisabledByFxToFeFP": rcftRemoteIIEthFeDisabledByFxToFeFP,
       "rcftRemoteIIEthFeTxRestrictSpeed": rcftRemoteIIEthFeTxRestrictSpeed,
       "rcftRemoteIIEthFeTag": rcftRemoteIIEthFeTag,
       "rcftRemoteIIEthFePVID": rcftRemoteIIEthFePVID,
       "rcftRemoteIIEthFeQoSPolicy": rcftRemoteIIEthFeQoSPolicy,
       "rcftRemoteIIEthFeStatisticTable": rcftRemoteIIEthFeStatisticTable,
       "rcftRemoteIIEthFeStatisticEntry": rcftRemoteIIEthFeStatisticEntry,
       "rcftRemoteIIEthFeTxPackets": rcftRemoteIIEthFeTxPackets,
       "rcftRemoteIIEthFeTxBytes": rcftRemoteIIEthFeTxBytes,
       "rcftRemoteIIEthFeRxPackets": rcftRemoteIIEthFeRxPackets,
       "rcftRemoteIIEthFeRxBytes": rcftRemoteIIEthFeRxBytes,
       "rcftRemoteIIEthFeRxLostPackets": rcftRemoteIIEthFeRxLostPackets,
       "rcftRemoteIIEthFeFluxTimer": rcftRemoteIIEthFeFluxTimer,
       "rcftRemoteIIEthFeTxLostPackets": rcftRemoteIIEthFeTxLostPackets,
       "rcftRemoteIIEthFePortConfTable": rcftRemoteIIEthFePortConfTable,
       "rcftRemoteIIEthFePortConfEntry": rcftRemoteIIEthFePortConfEntry,
       "rcftRemoteIIEthFeConfSpeed": rcftRemoteIIEthFeConfSpeed,
       "rcftRemoteIIEthFeConfDuplex": rcftRemoteIIEthFeConfDuplex,
       "rcftRemoteIIDeviceEthFeTraps": rcftRemoteIIDeviceEthFeTraps,
       "rcftRemoteIIEthFeLinkTrap": rcftRemoteIIEthFeLinkTrap,
       "rcftRemoteIIDeviceEthFxMIB": rcftRemoteIIDeviceEthFxMIB,
       "rcftRemoteIIDeviceEthFxObjects": rcftRemoteIIDeviceEthFxObjects,
       "rcftRemoteIIEthFxPortTable": rcftRemoteIIEthFxPortTable,
       "rcftRemoteIIEthFxPortEntry": rcftRemoteIIEthFxPortEntry,
       "rcftRemoteIIEthFxIndex": rcftRemoteIIEthFxIndex,
       "rcftRemoteIIEthFxPortRLK": rcftRemoteIIEthFxPortRLK,
       "rcftRemoteIIEthFxPortTLK": rcftRemoteIIEthFxPortTLK,
       "rcftRemoteIIEthFxPortSD": rcftRemoteIIEthFxPortSD,
       "rcftRemoteIIEthFxPortTxPowerAbnormal": rcftRemoteIIEthFxPortTxPowerAbnormal,
       "rcftRemoteIIEthFxPortRxSensitiveAbnormal": rcftRemoteIIEthFxPortRxSensitiveAbnormal,
       "rcftRemoteIIEthFxPortLaserAbnormal": rcftRemoteIIEthFxPortLaserAbnormal,
       "rcftRemoteIIEthFxPortModuleType": rcftRemoteIIEthFxPortModuleType,
       "rcftRemoteIIEthFxPortFaultPass": rcftRemoteIIEthFxPortFaultPass,
       "rcftRemoteIIEthFxPortLink": rcftRemoteIIEthFxPortLink,
       "rcftRemoteIIEthFxRxToTxFaultPass": rcftRemoteIIEthFxRxToTxFaultPass,
       "rcftRemoteIIEthFxTxDisabledByFR": rcftRemoteIIEthFxTxDisabledByFR,
       "rcftRemoteIIEthFxShutDown": rcftRemoteIIEthFxShutDown,
       "rcftRemoteIIEthFxPortAutoNegotiation": rcftRemoteIIEthFxPortAutoNegotiation,
       "rcftRemoteIIEthFxPortOptHeadType": rcftRemoteIIEthFxPortOptHeadType,
       "rcftRemoteIIEthFxSfpRXLOS": rcftRemoteIIEthFxSfpRXLOS,
       "rcftRemoteIIEthFxSfpTXDisable": rcftRemoteIIEthFxSfpTXDisable,
       "rcftRemoteIIEthFxSfpExist": rcftRemoteIIEthFxSfpExist,
       "rcftRemoteIIEthFxSfpSpeedStatus": rcftRemoteIIEthFxSfpSpeedStatus,
       "rcftRemoteIIEthFxSfpTransportDistance": rcftRemoteIIEthFxSfpTransportDistance,
       "rcftRemoteIIEthFxSfpWaveLength": rcftRemoteIIEthFxSfpWaveLength,
       "rcftRemoteIIEthFxSfpManufactory": rcftRemoteIIEthFxSfpManufactory,
       "rcftRemoteIIEthFxSfpProductType": rcftRemoteIIEthFxSfpProductType,
       "rcftRemoteIIEthFxSfpVersion": rcftRemoteIIEthFxSfpVersion,
       "rcftRemoteIIEthFxSfpWaterMask": rcftRemoteIIEthFxSfpWaterMask,
       "rcftRemoteIIEthFxSfpMediaType": rcftRemoteIIEthFxSfpMediaType,
       "rcftRemoteIIEthFxSfpModuleType": rcftRemoteIIEthFxSfpModuleType,
       "rcftRemoteIIEthFxSfpOpticalInterface": rcftRemoteIIEthFxSfpOpticalInterface,
       "rcftRemoteIIEthFxUntag": rcftRemoteIIEthFxUntag,
       "rcftRemoteIIEthFxPVID": rcftRemoteIIEthFxPVID,
       "rcftRemoteIIEthFxStatisticTable": rcftRemoteIIEthFxStatisticTable,
       "rcftRemoteIIEthFxStatisticEntry": rcftRemoteIIEthFxStatisticEntry,
       "rcftRemoteIIEthFxTxPackets": rcftRemoteIIEthFxTxPackets,
       "rcftRemoteIIEthFxTxBytes": rcftRemoteIIEthFxTxBytes,
       "rcftRemoteIIEthFxRxPackets": rcftRemoteIIEthFxRxPackets,
       "rcftRemoteIIEthFxRxBytes": rcftRemoteIIEthFxRxBytes,
       "rcftRemoteIIEthFxRxLostPackets": rcftRemoteIIEthFxRxLostPackets,
       "rcftRemoteIIEthFxFluxTimer": rcftRemoteIIEthFxFluxTimer,
       "rcftRemoteIIEthFxTxLostPackets": rcftRemoteIIEthFxTxLostPackets,
       "rcftRemoteIIDeviceEthFxTraps": rcftRemoteIIDeviceEthFxTraps,
       "rcftRemoteIIEthFxPortRLKTrap": rcftRemoteIIEthFxPortRLKTrap,
       "rcftRemoteIIEthFxPortTLKTrap": rcftRemoteIIEthFxPortTLKTrap,
       "rcftRemoteIIEthFxPortTxPowerTrap": rcftRemoteIIEthFxPortTxPowerTrap,
       "rcftRemoteIIEthFxPortRxSensitiveTrap": rcftRemoteIIEthFxPortRxSensitiveTrap,
       "rcftRemoteIIEthFxPortLaserTrap": rcftRemoteIIEthFxPortLaserTrap,
       "rcftRemoteIIEthFxPortSDTrap": rcftRemoteIIEthFxPortSDTrap,
       "rcftRemoteIIEthFxPortLinkTrap": rcftRemoteIIEthFxPortLinkTrap,
       "rcftRemoteIIEthFxPortSfpRXLOSTrap": rcftRemoteIIEthFxPortSfpRXLOSTrap,
       "rcftRemoteIIEthFxPortSfpExistTrap": rcftRemoteIIEthFxPortSfpExistTrap,
       "rcftRemoteIIDeviceVLANMIB": rcftRemoteIIDeviceVLANMIB,
       "rcftRemoteIIDeviceVLANObjects": rcftRemoteIIDeviceVLANObjects,
       "rcftRemoteIIDeviceVLANTable": rcftRemoteIIDeviceVLANTable,
       "rcftRemoteIIDeviceVLANEntry": rcftRemoteIIDeviceVLANEntry,
       "rcftRemoteIIVLANIndex": rcftRemoteIIVLANIndex,
       "rcftRemoteIIVLANStatus": rcftRemoteIIVLANStatus,
       "rcftRemoteIIVLANmember": rcftRemoteIIVLANmember,
       "rcftRemoteIIVID": rcftRemoteIIVID}
)
