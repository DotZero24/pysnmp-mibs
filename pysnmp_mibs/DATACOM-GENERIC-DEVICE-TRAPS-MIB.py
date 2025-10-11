# SNMP MIB module (DATACOM-GENERIC-DEVICE-TRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/datacom/DATACOM-GENERIC-DEVICE-TRAPS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:04:53 2025
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

(datacomGenericMIBs,
 datacomModules) = mibBuilder.importSymbols(
    "DATACOM-SMI",
    "datacomGenericMIBs",
    "datacomModules")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class DmDevIndex(Integer32):
    """Custom type DmDevIndex based on Integer32"""




class DmDevLocalIndex(Integer32):
    """Custom type DmDevLocalIndex based on Integer32"""




class DmSlotIndex(Integer32):
    """Custom type DmSlotIndex based on Integer32"""




class DmPortIndex(Integer32):
    """Custom type DmPortIndex based on Integer32"""




class DmTrapIndex(Integer32):
    """Custom type DmTrapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999999),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DatacomGenDvTrapsMIBModule_ObjectIdentity = ObjectIdentity
datacomGenDvTrapsMIBModule = _DatacomGenDvTrapsMIBModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 1, 24)
)
_DmGenDvTrapsMIB_ObjectIdentity = ObjectIdentity
dmGenDvTrapsMIB = _DmGenDvTrapsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4)
)
_DmGenDvTrapsInf_ObjectIdentity = ObjectIdentity
dmGenDvTrapsInf = _DmGenDvTrapsInf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 1)
)
_GenDvTrapsInfMibVersion_Type = DisplayString
_GenDvTrapsInfMibVersion_Object = MibScalar
genDvTrapsInfMibVersion = _GenDvTrapsInfMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 1, 1),
    _GenDvTrapsInfMibVersion_Type()
)
genDvTrapsInfMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvTrapsInfMibVersion.setStatus("mandatory")
_GenDvTrapsInfLastTrDevNo_Type = DmDevIndex
_GenDvTrapsInfLastTrDevNo_Object = MibScalar
genDvTrapsInfLastTrDevNo = _GenDvTrapsInfLastTrDevNo_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 1, 11),
    _GenDvTrapsInfLastTrDevNo_Type()
)
genDvTrapsInfLastTrDevNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvTrapsInfLastTrDevNo.setStatus("mandatory")
_GenDvTrapsInfLastTrDevLocalId_Type = DmDevLocalIndex
_GenDvTrapsInfLastTrDevLocalId_Object = MibScalar
genDvTrapsInfLastTrDevLocalId = _GenDvTrapsInfLastTrDevLocalId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 1, 12),
    _GenDvTrapsInfLastTrDevLocalId_Type()
)
genDvTrapsInfLastTrDevLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvTrapsInfLastTrDevLocalId.setStatus("mandatory")
_GenDvTrapsInfLastTrSlotNo_Type = DmSlotIndex
_GenDvTrapsInfLastTrSlotNo_Object = MibScalar
genDvTrapsInfLastTrSlotNo = _GenDvTrapsInfLastTrSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 1, 13),
    _GenDvTrapsInfLastTrSlotNo_Type()
)
genDvTrapsInfLastTrSlotNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvTrapsInfLastTrSlotNo.setStatus("mandatory")
_GenDvTrapsInfLastTrPortNo_Type = DmPortIndex
_GenDvTrapsInfLastTrPortNo_Object = MibScalar
genDvTrapsInfLastTrPortNo = _GenDvTrapsInfLastTrPortNo_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 1, 14),
    _GenDvTrapsInfLastTrPortNo_Type()
)
genDvTrapsInfLastTrPortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvTrapsInfLastTrPortNo.setStatus("mandatory")
_GenDvTrapsInfLastTrValue_Type = Integer32
_GenDvTrapsInfLastTrValue_Object = MibScalar
genDvTrapsInfLastTrValue = _GenDvTrapsInfLastTrValue_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 1, 15),
    _GenDvTrapsInfLastTrValue_Type()
)
genDvTrapsInfLastTrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvTrapsInfLastTrValue.setStatus("mandatory")
_GenDvTrapsInfLastTrType_Type = Integer32
_GenDvTrapsInfLastTrType_Object = MibScalar
genDvTrapsInfLastTrType = _GenDvTrapsInfLastTrType_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 1, 16),
    _GenDvTrapsInfLastTrType_Type()
)
genDvTrapsInfLastTrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvTrapsInfLastTrType.setStatus("mandatory")
_GenDvTrapsInfLastTrTimeStamp_Type = TimeTicks
_GenDvTrapsInfLastTrTimeStamp_Object = MibScalar
genDvTrapsInfLastTrTimeStamp = _GenDvTrapsInfLastTrTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 1, 17),
    _GenDvTrapsInfLastTrTimeStamp_Type()
)
genDvTrapsInfLastTrTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvTrapsInfLastTrTimeStamp.setStatus("mandatory")
_GenDvTrapsInfLastTrDeviceProduct_Type = ObjectIdentifier
_GenDvTrapsInfLastTrDeviceProduct_Object = MibScalar
genDvTrapsInfLastTrDeviceProduct = _GenDvTrapsInfLastTrDeviceProduct_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 1, 18),
    _GenDvTrapsInfLastTrDeviceProduct_Type()
)
genDvTrapsInfLastTrDeviceProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvTrapsInfLastTrDeviceProduct.setStatus("mandatory")
_GenDvTrapsInfLastTrAlarmId_Type = Integer32
_GenDvTrapsInfLastTrAlarmId_Object = MibScalar
genDvTrapsInfLastTrAlarmId = _GenDvTrapsInfLastTrAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 1, 19),
    _GenDvTrapsInfLastTrAlarmId_Type()
)
genDvTrapsInfLastTrAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvTrapsInfLastTrAlarmId.setStatus("mandatory")


class _GenDvTrapsInfLastTrAlarmVal_Type(Integer32):
    """Custom type genDvTrapsInfLastTrAlarmVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deactivated", 1),
          ("actived", 2),
          ("unstable", 3))
    )


_GenDvTrapsInfLastTrAlarmVal_Type.__name__ = "Integer32"
_GenDvTrapsInfLastTrAlarmVal_Object = MibScalar
genDvTrapsInfLastTrAlarmVal = _GenDvTrapsInfLastTrAlarmVal_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 1, 20),
    _GenDvTrapsInfLastTrAlarmVal_Type()
)
genDvTrapsInfLastTrAlarmVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvTrapsInfLastTrAlarmVal.setStatus("mandatory")
_GenDvTrapsInfLastTrUserName_Type = DisplayString
_GenDvTrapsInfLastTrUserName_Object = MibScalar
genDvTrapsInfLastTrUserName = _GenDvTrapsInfLastTrUserName_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 1, 21),
    _GenDvTrapsInfLastTrUserName_Type()
)
genDvTrapsInfLastTrUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvTrapsInfLastTrUserName.setStatus("mandatory")


class _GenDvTrapsInfLastTrAlarmSeverityVal_Type(Integer32):
    """Custom type genDvTrapsInfLastTrAlarmSeverityVal based on Integer32"""
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
        *(("info", 1),
          ("warning", 2),
          ("minor", 3),
          ("major", 4),
          ("critical", 5))
    )


_GenDvTrapsInfLastTrAlarmSeverityVal_Type.__name__ = "Integer32"
_GenDvTrapsInfLastTrAlarmSeverityVal_Object = MibScalar
genDvTrapsInfLastTrAlarmSeverityVal = _GenDvTrapsInfLastTrAlarmSeverityVal_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 1, 22),
    _GenDvTrapsInfLastTrAlarmSeverityVal_Type()
)
genDvTrapsInfLastTrAlarmSeverityVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvTrapsInfLastTrAlarmSeverityVal.setStatus("mandatory")
_GenDvTrapsInfLastTrChannel_Type = Integer32
_GenDvTrapsInfLastTrChannel_Object = MibScalar
genDvTrapsInfLastTrChannel = _GenDvTrapsInfLastTrChannel_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 1, 23),
    _GenDvTrapsInfLastTrChannel_Type()
)
genDvTrapsInfLastTrChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvTrapsInfLastTrChannel.setStatus("mandatory")
_GenDvTrapLicenseSN_Type = Integer32
_GenDvTrapLicenseSN_Object = MibScalar
genDvTrapLicenseSN = _GenDvTrapLicenseSN_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 1, 24),
    _GenDvTrapLicenseSN_Type()
)
genDvTrapLicenseSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvTrapLicenseSN.setStatus("mandatory")
_GenDvTrapLicenseExpire_Type = Integer32
_GenDvTrapLicenseExpire_Object = MibScalar
genDvTrapLicenseExpire = _GenDvTrapLicenseExpire_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 1, 25),
    _GenDvTrapLicenseExpire_Type()
)
genDvTrapLicenseExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvTrapLicenseExpire.setStatus("mandatory")


class _GenDvTrapsInfLastTrValueVlan_Type(Integer32):
    """Custom type genDvTrapsInfLastTrValueVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_GenDvTrapsInfLastTrValueVlan_Type.__name__ = "Integer32"
_GenDvTrapsInfLastTrValueVlan_Object = MibScalar
genDvTrapsInfLastTrValueVlan = _GenDvTrapsInfLastTrValueVlan_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 1, 26),
    _GenDvTrapsInfLastTrValueVlan_Type()
)
genDvTrapsInfLastTrValueVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvTrapsInfLastTrValueVlan.setStatus("mandatory")
_GenDvTrapsInfLastTrStringMac_Type = OctetString
_GenDvTrapsInfLastTrStringMac_Object = MibScalar
genDvTrapsInfLastTrStringMac = _GenDvTrapsInfLastTrStringMac_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 1, 27),
    _GenDvTrapsInfLastTrStringMac_Type()
)
genDvTrapsInfLastTrStringMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvTrapsInfLastTrStringMac.setStatus("mandatory")
_GenDvTrapsInfTable_Object = MibTable
genDvTrapsInfTable = _GenDvTrapsInfTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 1, 100)
)
if mibBuilder.loadTexts:
    genDvTrapsInfTable.setStatus("mandatory")
_GenDvTrapsInfEntry_Object = MibTableRow
genDvTrapsInfEntry = _GenDvTrapsInfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 1, 100, 1)
)
genDvTrapsInfEntry.setIndexNames(
    (0, "DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfIdxNo"),
)
if mibBuilder.loadTexts:
    genDvTrapsInfEntry.setStatus("mandatory")
_GenDvTrapsInfIdxNo_Type = DmTrapIndex
_GenDvTrapsInfIdxNo_Object = MibTableColumn
genDvTrapsInfIdxNo = _GenDvTrapsInfIdxNo_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 1, 100, 1, 1),
    _GenDvTrapsInfIdxNo_Type()
)
genDvTrapsInfIdxNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvTrapsInfIdxNo.setStatus("mandatory")
_GenDvTrapsInfObjectOid_Type = ObjectIdentifier
_GenDvTrapsInfObjectOid_Object = MibTableColumn
genDvTrapsInfObjectOid = _GenDvTrapsInfObjectOid_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 1, 100, 1, 2),
    _GenDvTrapsInfObjectOid_Type()
)
genDvTrapsInfObjectOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvTrapsInfObjectOid.setStatus("mandatory")
_GenDvTrapsInfObjIntegerVal_Type = Integer32
_GenDvTrapsInfObjIntegerVal_Object = MibTableColumn
genDvTrapsInfObjIntegerVal = _GenDvTrapsInfObjIntegerVal_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 1, 100, 1, 3),
    _GenDvTrapsInfObjIntegerVal_Type()
)
genDvTrapsInfObjIntegerVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvTrapsInfObjIntegerVal.setStatus("mandatory")
_GenDvTrapsInfObjTmTicksVal_Type = TimeTicks
_GenDvTrapsInfObjTmTicksVal_Object = MibTableColumn
genDvTrapsInfObjTmTicksVal = _GenDvTrapsInfObjTmTicksVal_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 1, 100, 1, 4),
    _GenDvTrapsInfObjTmTicksVal_Type()
)
genDvTrapsInfObjTmTicksVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvTrapsInfObjTmTicksVal.setStatus("mandatory")
_GenDvTrapsInfObjStringVal_Type = OctetString
_GenDvTrapsInfObjStringVal_Object = MibTableColumn
genDvTrapsInfObjStringVal = _GenDvTrapsInfObjStringVal_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 1, 100, 1, 5),
    _GenDvTrapsInfObjStringVal_Type()
)
genDvTrapsInfObjStringVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvTrapsInfObjStringVal.setStatus("mandatory")
_GenDvTrapsInfObjCounterVal_Type = Counter32
_GenDvTrapsInfObjCounterVal_Object = MibTableColumn
genDvTrapsInfObjCounterVal = _GenDvTrapsInfObjCounterVal_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 1, 100, 1, 6),
    _GenDvTrapsInfObjCounterVal_Type()
)
genDvTrapsInfObjCounterVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvTrapsInfObjCounterVal.setStatus("mandatory")
_GenDvTrapsInfObjGaugeVal_Type = Gauge32
_GenDvTrapsInfObjGaugeVal_Object = MibTableColumn
genDvTrapsInfObjGaugeVal = _GenDvTrapsInfObjGaugeVal_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 1, 100, 1, 7),
    _GenDvTrapsInfObjGaugeVal_Type()
)
genDvTrapsInfObjGaugeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvTrapsInfObjGaugeVal.setStatus("mandatory")

# Managed Objects groups


# Notification objects

mtGenDvInfInsertedDevTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 1)
)
mtGenDvInfInsertedDevTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDeviceProduct"))
)
if mibBuilder.loadTexts:
    mtGenDvInfInsertedDevTrap.setStatus(
        ""
    )

mtGenDvInfRemovedDevTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 2)
)
mtGenDvInfRemovedDevTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"))
)
if mibBuilder.loadTexts:
    mtGenDvInfRemovedDevTrap.setStatus(
        ""
    )

mtGenDvStSnmpManagementStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 51)
)
mtGenDvStSnmpManagementStatusTrap.setObjects(
    ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrValue")
)
if mibBuilder.loadTexts:
    mtGenDvStSnmpManagementStatusTrap.setStatus(
        ""
    )

mtGenDvStLatchedPossibleNewCfgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 52)
)
mtGenDvStLatchedPossibleNewCfgTrap.setObjects(
    ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrValue")
)
if mibBuilder.loadTexts:
    mtGenDvStLatchedPossibleNewCfgTrap.setStatus(
        ""
    )

agFwRemDownTempMemTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 61)
)
agFwRemDownTempMemTrap.setObjects(
    ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrValue")
)
if mibBuilder.loadTexts:
    agFwRemDownTempMemTrap.setStatus(
        ""
    )

agFwRemDownActionStTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 62)
)
agFwRemDownActionStTrap.setObjects(
    ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrValue")
)
if mibBuilder.loadTexts:
    agFwRemDownActionStTrap.setStatus(
        ""
    )

mtGenDvInfNumPortsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 100)
)
mtGenDvInfNumPortsTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrValue"))
)
if mibBuilder.loadTexts:
    mtGenDvInfNumPortsTrap.setStatus(
        ""
    )

mtGenDvInfTempRangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 601)
)
mtGenDvInfTempRangeTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrValue"))
)
if mibBuilder.loadTexts:
    mtGenDvInfTempRangeTrap.setStatus(
        ""
    )

mtGenDvInfFanFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 611)
)
mtGenDvInfFanFailTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrValue"))
)
if mibBuilder.loadTexts:
    mtGenDvInfFanFailTrap.setStatus(
        ""
    )

mtGenDvInfInsertedPortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 701)
)
mtGenDvInfInsertedPortTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"))
)
if mibBuilder.loadTexts:
    mtGenDvInfInsertedPortTrap.setStatus(
        ""
    )

mtGenDvInfRemovedPortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 702)
)
mtGenDvInfRemovedPortTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"))
)
if mibBuilder.loadTexts:
    mtGenDvInfRemovedPortTrap.setStatus(
        ""
    )

mtGenDvInfPortConfigModeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 809)
)
mtGenDvInfPortConfigModeTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrValue"))
)
if mibBuilder.loadTexts:
    mtGenDvInfPortConfigModeTrap.setStatus(
        ""
    )

mtGenDvInfPowerStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 901)
)
mtGenDvInfPowerStatusTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrValue"))
)
if mibBuilder.loadTexts:
    mtGenDvInfPowerStatusTrap.setStatus(
        ""
    )

smtGenDvStLinkStatusTribE1PpiExcSlipTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 13018)
)
smtGenDvStLinkStatusTribE1PpiExcSlipTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfObjectOid"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    smtGenDvStLinkStatusTribE1PpiExcSlipTrap.setStatus(
        ""
    )

smtGenDvStLinkStatusDigitalItfExcSlipTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 13204)
)
smtGenDvStLinkStatusDigitalItfExcSlipTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfObjectOid"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    smtGenDvStLinkStatusDigitalItfExcSlipTrap.setStatus(
        ""
    )

smtGenDvStLinkStatusDslExcSlipTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 13304)
)
smtGenDvStLinkStatusDslExcSlipTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfObjectOid"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    smtGenDvStLinkStatusDslExcSlipTrap.setStatus(
        ""
    )

smtGenDvStPhSlotStFailFanFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 16002)
)
smtGenDvStPhSlotStFailFanFailTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    smtGenDvStPhSlotStFailFanFailTrap.setStatus(
        ""
    )

smtGenDvStPhSlotStFailFanMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 16007)
)
smtGenDvStPhSlotStFailFanMismatchTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    smtGenDvStPhSlotStFailFanMismatchTrap.setStatus(
        ""
    )

smtGenDvStPhSlotStFailPwrSuppFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 16102)
)
smtGenDvStPhSlotStFailPwrSuppFailTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    smtGenDvStPhSlotStFailPwrSuppFailTrap.setStatus(
        ""
    )

smtGenDvStPhSlotStFailPwrRedundancyFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 16103)
)
smtGenDvStPhSlotStFailPwrRedundancyFailTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    smtGenDvStPhSlotStFailPwrRedundancyFailTrap.setStatus(
        ""
    )

smtGenDvStPhSlotStFailPwrOverloadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 16104)
)
smtGenDvStPhSlotStFailPwrOverloadTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    smtGenDvStPhSlotStFailPwrOverloadTrap.setStatus(
        ""
    )

smtGenDvStPhSlotStFailFuseFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 16105)
)
smtGenDvStPhSlotStFailFuseFailTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    smtGenDvStPhSlotStFailFuseFailTrap.setStatus(
        ""
    )

smtGenDvEthernetOverloadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 16111)
)
smtGenDvEthernetOverloadTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    smtGenDvEthernetOverloadTrap.setStatus(
        ""
    )

smtGenDvStPhSlotStFailAggFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 16122)
)
smtGenDvStPhSlotStFailAggFailTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    smtGenDvStPhSlotStFailAggFailTrap.setStatus(
        ""
    )

smtGenDvStPhSlotOperStAggPrevMaintReqTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 16126)
)
smtGenDvStPhSlotOperStAggPrevMaintReqTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    smtGenDvStPhSlotOperStAggPrevMaintReqTrap.setStatus(
        ""
    )

smtGenDvStPhSlotStFailTribFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 16132)
)
smtGenDvStPhSlotStFailTribFailTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    smtGenDvStPhSlotStFailTribFailTrap.setStatus(
        ""
    )

smtGenDvStPhSlotPresenceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 17001)
)
smtGenDvStPhSlotPresenceTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfObjectOid"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfObjIntegerVal"))
)
if mibBuilder.loadTexts:
    smtGenDvStPhSlotPresenceTrap.setStatus(
        ""
    )

smtGenDvStCurrentDevCpuFWUpdateFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 17007)
)
smtGenDvStCurrentDevCpuFWUpdateFailure.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"))
)
if mibBuilder.loadTexts:
    smtGenDvStCurrentDevCpuFWUpdateFailure.setStatus(
        ""
    )

smtGenDvStCurrentDevCpuFWInvalidInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 17009)
)
smtGenDvStCurrentDevCpuFWInvalidInactive.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrValue"))
)
if mibBuilder.loadTexts:
    smtGenDvStCurrentDevCpuFWInvalidInactive.setStatus(
        ""
    )

smtGenDvStCurrentDevCpuFWImageTemporary = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 17010)
)
smtGenDvStCurrentDevCpuFWImageTemporary.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"))
)
if mibBuilder.loadTexts:
    smtGenDvStCurrentDevCpuFWImageTemporary.setStatus(
        ""
    )

smtGenDvStCurrentDevCpuFWUpdateBeginning = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 17011)
)
smtGenDvStCurrentDevCpuFWUpdateBeginning.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"))
)
if mibBuilder.loadTexts:
    smtGenDvStCurrentDevCpuFWUpdateBeginning.setStatus(
        ""
    )

smtGenDvStPhSlotStFailCpuFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 17012)
)
smtGenDvStPhSlotStFailCpuFailTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    smtGenDvStPhSlotStFailCpuFailTrap.setStatus(
        ""
    )

smtGenDvStPhSlotStFailCriticalTempTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 17013)
)
smtGenDvStPhSlotStFailCriticalTempTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    smtGenDvStPhSlotStFailCriticalTempTrap.setStatus(
        ""
    )

smtsdhStCurrentDevCpuFWUpdateReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 17015)
)
smtsdhStCurrentDevCpuFWUpdateReady.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"))
)
if mibBuilder.loadTexts:
    smtsdhStCurrentDevCpuFWUpdateReady.setStatus(
        ""
    )

smtsdhStCurrentDevFWVersionChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 17020)
)
smtsdhStCurrentDevFWVersionChanged.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfObjIntegerVal"))
)
if mibBuilder.loadTexts:
    smtsdhStCurrentDevFWVersionChanged.setStatus(
        ""
    )

smtGenDvStPhSlotStCardRemovedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 17022)
)
smtGenDvStPhSlotStCardRemovedTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    smtGenDvStPhSlotStCardRemovedTrap.setStatus(
        ""
    )

smtGenDvStPhSlotStCardMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 17023)
)
smtGenDvStPhSlotStCardMismatchTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    smtGenDvStPhSlotStCardMismatchTrap.setStatus(
        ""
    )

smtGenDvStPhSlotStCardDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 17024)
)
smtGenDvStPhSlotStCardDisabledTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    smtGenDvStPhSlotStCardDisabledTrap.setStatus(
        ""
    )

smtGenDvStPhSlotStUnsupportedCardTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 17025)
)
smtGenDvStPhSlotStUnsupportedCardTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    smtGenDvStPhSlotStUnsupportedCardTrap.setStatus(
        ""
    )

smtGenDvStPhSlotStCardConfigMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 17026)
)
smtGenDvStPhSlotStCardConfigMismatch.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    smtGenDvStPhSlotStCardConfigMismatch.setStatus(
        ""
    )

smtGenDvStPhSlotStCardFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 17027)
)
smtGenDvStPhSlotStCardFail.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    smtGenDvStPhSlotStCardFail.setStatus(
        ""
    )

smtGenDvStPhSlotStCardFwMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 17028)
)
smtGenDvStPhSlotStCardFwMismatch.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    smtGenDvStPhSlotStCardFwMismatch.setStatus(
        ""
    )

smtGenDvStPhSlotStCardCriticalTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 17029)
)
smtGenDvStPhSlotStCardCriticalTemp.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    smtGenDvStPhSlotStCardCriticalTemp.setStatus(
        ""
    )

smtGenDvStPhSlotStCardHwConfigFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 17030)
)
smtGenDvStPhSlotStCardHwConfigFail.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    smtGenDvStPhSlotStCardHwConfigFail.setStatus(
        ""
    )

smtGenDvStPhSlotStCardHwProtected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 17031)
)
smtGenDvStPhSlotStCardHwProtected.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    smtGenDvStPhSlotStCardHwProtected.setStatus(
        ""
    )

smtGenDvStPhSlotStCardVendorMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 17032)
)
smtGenDvStPhSlotStCardVendorMismatch.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    smtGenDvStPhSlotStCardVendorMismatch.setStatus(
        ""
    )

smtGenDvStLastChangeTmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 17151)
)
smtGenDvStLastChangeTmTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfObjectOid"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfObjGaugeVal"))
)
if mibBuilder.loadTexts:
    smtGenDvStLastChangeTmTrap.setStatus(
        ""
    )

smtGenDvStLastActivationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 17171)
)
smtGenDvStLastActivationTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrUserName"))
)
if mibBuilder.loadTexts:
    smtGenDvStLastActivationTrap.setStatus(
        ""
    )

smtGenDvStUserListChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 17172)
)
smtGenDvStUserListChangedTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfObjectOid"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfObjIntegerVal"))
)
if mibBuilder.loadTexts:
    smtGenDvStUserListChangedTrap.setStatus(
        ""
    )

smtGenDvStCpuActiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 17191)
)
smtGenDvStCpuActiveTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"))
)
if mibBuilder.loadTexts:
    smtGenDvStCpuActiveTrap.setStatus(
        ""
    )

smtGenDvStCpuColdStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 17192)
)
smtGenDvStCpuColdStartTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"))
)
if mibBuilder.loadTexts:
    smtGenDvStCpuColdStartTrap.setStatus(
        ""
    )

smtGenDvStCpuWarmStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 17193)
)
smtGenDvStCpuWarmStartTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"))
)
if mibBuilder.loadTexts:
    smtGenDvStCpuWarmStartTrap.setStatus(
        ""
    )

smtGenDvInfInsertedDevTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 20001)
)
smtGenDvInfInsertedDevTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfObjectOid"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfObjStringVal"))
)
if mibBuilder.loadTexts:
    smtGenDvInfInsertedDevTrap.setStatus(
        ""
    )

smtGenDvInfRemovedDevTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 20002)
)
smtGenDvInfRemovedDevTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfObjectOid"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfObjStringVal"))
)
if mibBuilder.loadTexts:
    smtGenDvInfRemovedDevTrap.setStatus(
        ""
    )

sFPmismatchAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 21003)
)
sFPmismatchAlarmTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    sFPmismatchAlarmTrap.setStatus(
        ""
    )

sFPvendorMismatchAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 21007)
)
sFPvendorMismatchAlarmTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    sFPvendorMismatchAlarmTrap.setStatus(
        ""
    )

configTemporaryAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 21101)
)
configTemporaryAlarmTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    configTemporaryAlarmTrap.setStatus(
        ""
    )

edfaFailureAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 22014)
)
edfaFailureAlarmTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    edfaFailureAlarmTrap.setStatus(
        ""
    )

edfaLowInputPowerFailureAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 22015)
)
edfaLowInputPowerFailureAlarmTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    edfaLowInputPowerFailureAlarmTrap.setStatus(
        ""
    )

icad2Subdev1MismatchAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 22101)
)
icad2Subdev1MismatchAlarmTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    icad2Subdev1MismatchAlarmTrap.setStatus(
        ""
    )

icad2Subdev2MismatchAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 22102)
)
icad2Subdev2MismatchAlarmTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    icad2Subdev2MismatchAlarmTrap.setStatus(
        ""
    )

icad2Subdev1NotPresentAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 22103)
)
icad2Subdev1NotPresentAlarmTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    icad2Subdev1NotPresentAlarmTrap.setStatus(
        ""
    )

icad2Subdev2NotPresentAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 22104)
)
icad2Subdev2NotPresentAlarmTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    icad2Subdev2NotPresentAlarmTrap.setStatus(
        ""
    )

icad2Subdev1FailureAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 22105)
)
icad2Subdev1FailureAlarmTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    icad2Subdev1FailureAlarmTrap.setStatus(
        ""
    )

icad2Subdev2FailureAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 22106)
)
icad2Subdev2FailureAlarmTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    icad2Subdev2FailureAlarmTrap.setStatus(
        ""
    )

smtGenDvStLostComWithItfTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 30000)
)
smtGenDvStLostComWithItfTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrTimeStamp"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    smtGenDvStLostComWithItfTrap.setStatus(
        ""
    )

smtGenDvStLoSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 30001)
)
smtGenDvStLoSTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrTimeStamp"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    smtGenDvStLoSTrap.setStatus(
        ""
    )

smtGenDvStAiSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 30002)
)
smtGenDvStAiSTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrTimeStamp"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    smtGenDvStAiSTrap.setStatus(
        ""
    )

smtGenDvStLofTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 30003)
)
smtGenDvStLofTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrTimeStamp"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    smtGenDvStLofTrap.setStatus(
        ""
    )

smtGenDvStRalmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 30004)
)
smtGenDvStRalmTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrTimeStamp"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    smtGenDvStRalmTrap.setStatus(
        ""
    )

smtGenDvStMfaTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 30005)
)
smtGenDvStMfaTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrTimeStamp"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    smtGenDvStMfaTrap.setStatus(
        ""
    )

smtGenDvStLomTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 30006)
)
smtGenDvStLomTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrTimeStamp"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    smtGenDvStLomTrap.setStatus(
        ""
    )

smtGenDvStCpuLoadThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 30007)
)
smtGenDvStCpuLoadThresholdTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrTimeStamp"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmSeverityVal"))
)
if mibBuilder.loadTexts:
    smtGenDvStCpuLoadThresholdTrap.setStatus(
        ""
    )

smtGenDvStDiskUseThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 30008)
)
smtGenDvStDiskUseThresholdTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrTimeStamp"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmSeverityVal"))
)
if mibBuilder.loadTexts:
    smtGenDvStDiskUseThresholdTrap.setStatus(
        ""
    )

smtGenDvStMemoryUseThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 30009)
)
smtGenDvStMemoryUseThresholdTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrTimeStamp"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmSeverityVal"))
)
if mibBuilder.loadTexts:
    smtGenDvStMemoryUseThresholdTrap.setStatus(
        ""
    )

stMacSpoofingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 30010)
)
stMacSpoofingTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrValueVlan"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrStringMac"))
)
if mibBuilder.loadTexts:
    stMacSpoofingTrap.setStatus(
        ""
    )

tLoginFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 40001)
)
tLoginFailTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrUserName"))
)
if mibBuilder.loadTexts:
    tLoginFailTrap.setStatus(
        ""
    )

tLoginSucessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 40002)
)
tLoginSucessTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrUserName"))
)
if mibBuilder.loadTexts:
    tLoginSucessTrap.setStatus(
        ""
    )

tTxFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 40003)
)
tTxFaultTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    tTxFaultTrap.setStatus(
        ""
    )

cpuFWMismatchAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 40004)
)
cpuFWMismatchAlarmTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    cpuFWMismatchAlarmTrap.setStatus(
        ""
    )

cardFWMismatchAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 40005)
)
cardFWMismatchAlarmTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    cardFWMismatchAlarmTrap.setStatus(
        ""
    )

fwLoadByTftpAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 40006)
)
fwLoadByTftpAlarmTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    fwLoadByTftpAlarmTrap.setStatus(
        ""
    )

trapLicenseWillExpire = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 40007)
)
trapLicenseWillExpire.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapLicenseSN"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapLicenseExpire"))
)
if mibBuilder.loadTexts:
    trapLicenseWillExpire.setStatus(
        ""
    )

trapLicenseExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 40008)
)
trapLicenseExpired.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapLicenseSN"))
)
if mibBuilder.loadTexts:
    trapLicenseExpired.setStatus(
        ""
    )

uBootUpdateAvailAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 40009)
)
uBootUpdateAvailAlarmTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrAlarmVal"))
)
if mibBuilder.loadTexts:
    uBootUpdateAvailAlarmTrap.setStatus(
        ""
    )

swNonHomologSfpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 2, 4, 0, 40010)
)
swNonHomologSfpTrap.setObjects(
      *(("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrDevLocalId"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrSlotNo"),
        ("DATACOM-GENERIC-DEVICE-TRAPS-MIB", "genDvTrapsInfLastTrPortNo"))
)
if mibBuilder.loadTexts:
    swNonHomologSfpTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DATACOM-GENERIC-DEVICE-TRAPS-MIB",
    **{"DisplayString": DisplayString,
       "DmDevIndex": DmDevIndex,
       "DmDevLocalIndex": DmDevLocalIndex,
       "DmSlotIndex": DmSlotIndex,
       "DmPortIndex": DmPortIndex,
       "DmTrapIndex": DmTrapIndex,
       "datacomGenDvTrapsMIBModule": datacomGenDvTrapsMIBModule,
       "dmGenDvTrapsMIB": dmGenDvTrapsMIB,
       "mtGenDvInfInsertedDevTrap": mtGenDvInfInsertedDevTrap,
       "mtGenDvInfRemovedDevTrap": mtGenDvInfRemovedDevTrap,
       "mtGenDvStSnmpManagementStatusTrap": mtGenDvStSnmpManagementStatusTrap,
       "mtGenDvStLatchedPossibleNewCfgTrap": mtGenDvStLatchedPossibleNewCfgTrap,
       "agFwRemDownTempMemTrap": agFwRemDownTempMemTrap,
       "agFwRemDownActionStTrap": agFwRemDownActionStTrap,
       "mtGenDvInfNumPortsTrap": mtGenDvInfNumPortsTrap,
       "mtGenDvInfTempRangeTrap": mtGenDvInfTempRangeTrap,
       "mtGenDvInfFanFailTrap": mtGenDvInfFanFailTrap,
       "mtGenDvInfInsertedPortTrap": mtGenDvInfInsertedPortTrap,
       "mtGenDvInfRemovedPortTrap": mtGenDvInfRemovedPortTrap,
       "mtGenDvInfPortConfigModeTrap": mtGenDvInfPortConfigModeTrap,
       "mtGenDvInfPowerStatusTrap": mtGenDvInfPowerStatusTrap,
       "smtGenDvStLinkStatusTribE1PpiExcSlipTrap": smtGenDvStLinkStatusTribE1PpiExcSlipTrap,
       "smtGenDvStLinkStatusDigitalItfExcSlipTrap": smtGenDvStLinkStatusDigitalItfExcSlipTrap,
       "smtGenDvStLinkStatusDslExcSlipTrap": smtGenDvStLinkStatusDslExcSlipTrap,
       "smtGenDvStPhSlotStFailFanFailTrap": smtGenDvStPhSlotStFailFanFailTrap,
       "smtGenDvStPhSlotStFailFanMismatchTrap": smtGenDvStPhSlotStFailFanMismatchTrap,
       "smtGenDvStPhSlotStFailPwrSuppFailTrap": smtGenDvStPhSlotStFailPwrSuppFailTrap,
       "smtGenDvStPhSlotStFailPwrRedundancyFailTrap": smtGenDvStPhSlotStFailPwrRedundancyFailTrap,
       "smtGenDvStPhSlotStFailPwrOverloadTrap": smtGenDvStPhSlotStFailPwrOverloadTrap,
       "smtGenDvStPhSlotStFailFuseFailTrap": smtGenDvStPhSlotStFailFuseFailTrap,
       "smtGenDvEthernetOverloadTrap": smtGenDvEthernetOverloadTrap,
       "smtGenDvStPhSlotStFailAggFailTrap": smtGenDvStPhSlotStFailAggFailTrap,
       "smtGenDvStPhSlotOperStAggPrevMaintReqTrap": smtGenDvStPhSlotOperStAggPrevMaintReqTrap,
       "smtGenDvStPhSlotStFailTribFailTrap": smtGenDvStPhSlotStFailTribFailTrap,
       "smtGenDvStPhSlotPresenceTrap": smtGenDvStPhSlotPresenceTrap,
       "smtGenDvStCurrentDevCpuFWUpdateFailure": smtGenDvStCurrentDevCpuFWUpdateFailure,
       "smtGenDvStCurrentDevCpuFWInvalidInactive": smtGenDvStCurrentDevCpuFWInvalidInactive,
       "smtGenDvStCurrentDevCpuFWImageTemporary": smtGenDvStCurrentDevCpuFWImageTemporary,
       "smtGenDvStCurrentDevCpuFWUpdateBeginning": smtGenDvStCurrentDevCpuFWUpdateBeginning,
       "smtGenDvStPhSlotStFailCpuFailTrap": smtGenDvStPhSlotStFailCpuFailTrap,
       "smtGenDvStPhSlotStFailCriticalTempTrap": smtGenDvStPhSlotStFailCriticalTempTrap,
       "smtsdhStCurrentDevCpuFWUpdateReady": smtsdhStCurrentDevCpuFWUpdateReady,
       "smtsdhStCurrentDevFWVersionChanged": smtsdhStCurrentDevFWVersionChanged,
       "smtGenDvStPhSlotStCardRemovedTrap": smtGenDvStPhSlotStCardRemovedTrap,
       "smtGenDvStPhSlotStCardMismatchTrap": smtGenDvStPhSlotStCardMismatchTrap,
       "smtGenDvStPhSlotStCardDisabledTrap": smtGenDvStPhSlotStCardDisabledTrap,
       "smtGenDvStPhSlotStUnsupportedCardTrap": smtGenDvStPhSlotStUnsupportedCardTrap,
       "smtGenDvStPhSlotStCardConfigMismatch": smtGenDvStPhSlotStCardConfigMismatch,
       "smtGenDvStPhSlotStCardFail": smtGenDvStPhSlotStCardFail,
       "smtGenDvStPhSlotStCardFwMismatch": smtGenDvStPhSlotStCardFwMismatch,
       "smtGenDvStPhSlotStCardCriticalTemp": smtGenDvStPhSlotStCardCriticalTemp,
       "smtGenDvStPhSlotStCardHwConfigFail": smtGenDvStPhSlotStCardHwConfigFail,
       "smtGenDvStPhSlotStCardHwProtected": smtGenDvStPhSlotStCardHwProtected,
       "smtGenDvStPhSlotStCardVendorMismatch": smtGenDvStPhSlotStCardVendorMismatch,
       "smtGenDvStLastChangeTmTrap": smtGenDvStLastChangeTmTrap,
       "smtGenDvStLastActivationTrap": smtGenDvStLastActivationTrap,
       "smtGenDvStUserListChangedTrap": smtGenDvStUserListChangedTrap,
       "smtGenDvStCpuActiveTrap": smtGenDvStCpuActiveTrap,
       "smtGenDvStCpuColdStartTrap": smtGenDvStCpuColdStartTrap,
       "smtGenDvStCpuWarmStartTrap": smtGenDvStCpuWarmStartTrap,
       "smtGenDvInfInsertedDevTrap": smtGenDvInfInsertedDevTrap,
       "smtGenDvInfRemovedDevTrap": smtGenDvInfRemovedDevTrap,
       "sFPmismatchAlarmTrap": sFPmismatchAlarmTrap,
       "sFPvendorMismatchAlarmTrap": sFPvendorMismatchAlarmTrap,
       "configTemporaryAlarmTrap": configTemporaryAlarmTrap,
       "edfaFailureAlarmTrap": edfaFailureAlarmTrap,
       "edfaLowInputPowerFailureAlarmTrap": edfaLowInputPowerFailureAlarmTrap,
       "icad2Subdev1MismatchAlarmTrap": icad2Subdev1MismatchAlarmTrap,
       "icad2Subdev2MismatchAlarmTrap": icad2Subdev2MismatchAlarmTrap,
       "icad2Subdev1NotPresentAlarmTrap": icad2Subdev1NotPresentAlarmTrap,
       "icad2Subdev2NotPresentAlarmTrap": icad2Subdev2NotPresentAlarmTrap,
       "icad2Subdev1FailureAlarmTrap": icad2Subdev1FailureAlarmTrap,
       "icad2Subdev2FailureAlarmTrap": icad2Subdev2FailureAlarmTrap,
       "smtGenDvStLostComWithItfTrap": smtGenDvStLostComWithItfTrap,
       "smtGenDvStLoSTrap": smtGenDvStLoSTrap,
       "smtGenDvStAiSTrap": smtGenDvStAiSTrap,
       "smtGenDvStLofTrap": smtGenDvStLofTrap,
       "smtGenDvStRalmTrap": smtGenDvStRalmTrap,
       "smtGenDvStMfaTrap": smtGenDvStMfaTrap,
       "smtGenDvStLomTrap": smtGenDvStLomTrap,
       "smtGenDvStCpuLoadThresholdTrap": smtGenDvStCpuLoadThresholdTrap,
       "smtGenDvStDiskUseThresholdTrap": smtGenDvStDiskUseThresholdTrap,
       "smtGenDvStMemoryUseThresholdTrap": smtGenDvStMemoryUseThresholdTrap,
       "stMacSpoofingTrap": stMacSpoofingTrap,
       "tLoginFailTrap": tLoginFailTrap,
       "tLoginSucessTrap": tLoginSucessTrap,
       "tTxFaultTrap": tTxFaultTrap,
       "cpuFWMismatchAlarmTrap": cpuFWMismatchAlarmTrap,
       "cardFWMismatchAlarmTrap": cardFWMismatchAlarmTrap,
       "fwLoadByTftpAlarmTrap": fwLoadByTftpAlarmTrap,
       "trapLicenseWillExpire": trapLicenseWillExpire,
       "trapLicenseExpired": trapLicenseExpired,
       "uBootUpdateAvailAlarmTrap": uBootUpdateAvailAlarmTrap,
       "swNonHomologSfpTrap": swNonHomologSfpTrap,
       "dmGenDvTrapsInf": dmGenDvTrapsInf,
       "genDvTrapsInfMibVersion": genDvTrapsInfMibVersion,
       "genDvTrapsInfLastTrDevNo": genDvTrapsInfLastTrDevNo,
       "genDvTrapsInfLastTrDevLocalId": genDvTrapsInfLastTrDevLocalId,
       "genDvTrapsInfLastTrSlotNo": genDvTrapsInfLastTrSlotNo,
       "genDvTrapsInfLastTrPortNo": genDvTrapsInfLastTrPortNo,
       "genDvTrapsInfLastTrValue": genDvTrapsInfLastTrValue,
       "genDvTrapsInfLastTrType": genDvTrapsInfLastTrType,
       "genDvTrapsInfLastTrTimeStamp": genDvTrapsInfLastTrTimeStamp,
       "genDvTrapsInfLastTrDeviceProduct": genDvTrapsInfLastTrDeviceProduct,
       "genDvTrapsInfLastTrAlarmId": genDvTrapsInfLastTrAlarmId,
       "genDvTrapsInfLastTrAlarmVal": genDvTrapsInfLastTrAlarmVal,
       "genDvTrapsInfLastTrUserName": genDvTrapsInfLastTrUserName,
       "genDvTrapsInfLastTrAlarmSeverityVal": genDvTrapsInfLastTrAlarmSeverityVal,
       "genDvTrapsInfLastTrChannel": genDvTrapsInfLastTrChannel,
       "genDvTrapLicenseSN": genDvTrapLicenseSN,
       "genDvTrapLicenseExpire": genDvTrapLicenseExpire,
       "genDvTrapsInfLastTrValueVlan": genDvTrapsInfLastTrValueVlan,
       "genDvTrapsInfLastTrStringMac": genDvTrapsInfLastTrStringMac,
       "genDvTrapsInfTable": genDvTrapsInfTable,
       "genDvTrapsInfEntry": genDvTrapsInfEntry,
       "genDvTrapsInfIdxNo": genDvTrapsInfIdxNo,
       "genDvTrapsInfObjectOid": genDvTrapsInfObjectOid,
       "genDvTrapsInfObjIntegerVal": genDvTrapsInfObjIntegerVal,
       "genDvTrapsInfObjTmTicksVal": genDvTrapsInfObjTmTicksVal,
       "genDvTrapsInfObjStringVal": genDvTrapsInfObjStringVal,
       "genDvTrapsInfObjCounterVal": genDvTrapsInfObjCounterVal,
       "genDvTrapsInfObjGaugeVal": genDvTrapsInfObjGaugeVal}
)
