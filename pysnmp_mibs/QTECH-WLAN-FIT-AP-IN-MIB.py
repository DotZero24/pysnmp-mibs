# SNMP MIB module (QTECH-WLAN-FIT-AP-IN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-WLAN-FIT-AP-IN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:57:06 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(qtechApApName,
 qtechApCfgRadioId,
 qtechApMacAddr,
 qtechApgWlanId,
 qtechStaMacAddr) = mibBuilder.importSymbols(
    "QTECH-AC-MGMT-MIB",
    "qtechApApName",
    "qtechApCfgRadioId",
    "qtechApMacAddr",
    "qtechApgWlanId",
    "qtechStaMacAddr")

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

qtechFitApMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83)
)
if mibBuilder.loadTexts:
    qtechFitApMibModule.setRevisions(
        ("2010-02-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechAlarmTraps_ObjectIdentity = ObjectIdentity
qtechAlarmTraps = _QtechAlarmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 0)
)
_QtechSystemInfoConfigObjects_ObjectIdentity = ObjectIdentity
qtechSystemInfoConfigObjects = _QtechSystemInfoConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 1)
)
_QtechDomain_Type = DisplayString
_QtechDomain_Object = MibScalar
qtechDomain = _QtechDomain_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 1, 1),
    _QtechDomain_Type()
)
qtechDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDomain.setStatus("current")


class _QtechPhySeparatedEnable_Type(Integer32):
    """Custom type qtechPhySeparatedEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_QtechPhySeparatedEnable_Type.__name__ = "Integer32"
_QtechPhySeparatedEnable_Object = MibScalar
qtechPhySeparatedEnable = _QtechPhySeparatedEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 1, 2),
    _QtechPhySeparatedEnable_Type()
)
qtechPhySeparatedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPhySeparatedEnable.setStatus("current")


class _QtechForfendDosAttackEnable_Type(Integer32):
    """Custom type qtechForfendDosAttackEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_QtechForfendDosAttackEnable_Type.__name__ = "Integer32"
_QtechForfendDosAttackEnable_Object = MibScalar
qtechForfendDosAttackEnable = _QtechForfendDosAttackEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 1, 3),
    _QtechForfendDosAttackEnable_Type()
)
qtechForfendDosAttackEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechForfendDosAttackEnable.setStatus("current")
_QtechAcTrafficLoadBalancing_Type = TruthValue
_QtechAcTrafficLoadBalancing_Object = MibScalar
qtechAcTrafficLoadBalancing = _QtechAcTrafficLoadBalancing_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 1, 4),
    _QtechAcTrafficLoadBalancing_Type()
)
qtechAcTrafficLoadBalancing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcTrafficLoadBalancing.setStatus("current")
_QtechAcTrafficLoadBalanceThreshold_Type = Integer32
_QtechAcTrafficLoadBalanceThreshold_Object = MibScalar
qtechAcTrafficLoadBalanceThreshold = _QtechAcTrafficLoadBalanceThreshold_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 1, 5),
    _QtechAcTrafficLoadBalanceThreshold_Type()
)
qtechAcTrafficLoadBalanceThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcTrafficLoadBalanceThreshold.setStatus("current")
_QtechAcTrafficOtherAPThresholdValue_Type = Integer32
_QtechAcTrafficOtherAPThresholdValue_Object = MibScalar
qtechAcTrafficOtherAPThresholdValue = _QtechAcTrafficOtherAPThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 1, 6),
    _QtechAcTrafficOtherAPThresholdValue_Type()
)
qtechAcTrafficOtherAPThresholdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcTrafficOtherAPThresholdValue.setStatus("current")
_QtechAcAPWIDSScanningMode_Type = Integer32
_QtechAcAPWIDSScanningMode_Object = MibScalar
qtechAcAPWIDSScanningMode = _QtechAcAPWIDSScanningMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 1, 7),
    _QtechAcAPWIDSScanningMode_Type()
)
qtechAcAPWIDSScanningMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcAPWIDSScanningMode.setStatus("current")
_QtechAcAPLegitimateMode_Type = Integer32
_QtechAcAPLegitimateMode_Object = MibScalar
qtechAcAPLegitimateMode = _QtechAcAPLegitimateMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 1, 8),
    _QtechAcAPLegitimateMode_Type()
)
qtechAcAPLegitimateMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcAPLegitimateMode.setStatus("current")
_QtechAcAPTreatMode_Type = Integer32
_QtechAcAPTreatMode_Object = MibScalar
qtechAcAPTreatMode = _QtechAcAPTreatMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 1, 9),
    _QtechAcAPTreatMode_Type()
)
qtechAcAPTreatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcAPTreatMode.setStatus("current")
_QtechAcAssociationFailureTotalTimes_Type = Counter32
_QtechAcAssociationFailureTotalTimes_Object = MibScalar
qtechAcAssociationFailureTotalTimes = _QtechAcAssociationFailureTotalTimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 1, 10),
    _QtechAcAssociationFailureTotalTimes_Type()
)
qtechAcAssociationFailureTotalTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcAssociationFailureTotalTimes.setStatus("current")
_QtechAcAirIfRxTotalDataFrams_Type = Counter32
_QtechAcAirIfRxTotalDataFrams_Object = MibScalar
qtechAcAirIfRxTotalDataFrams = _QtechAcAirIfRxTotalDataFrams_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 1, 11),
    _QtechAcAirIfRxTotalDataFrams_Type()
)
qtechAcAirIfRxTotalDataFrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcAirIfRxTotalDataFrams.setStatus("current")
_QtechAcAirIfTxTotalDataFrams_Type = Counter32
_QtechAcAirIfTxTotalDataFrams_Object = MibScalar
qtechAcAirIfTxTotalDataFrams = _QtechAcAirIfTxTotalDataFrams_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 1, 12),
    _QtechAcAirIfTxTotalDataFrams_Type()
)
qtechAcAirIfTxTotalDataFrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcAirIfTxTotalDataFrams.setStatus("current")
_QtechAcAirIfTxTotalLostFrams_Type = Counter32
_QtechAcAirIfTxTotalLostFrams_Object = MibScalar
qtechAcAirIfTxTotalLostFrams = _QtechAcAirIfTxTotalLostFrams_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 1, 13),
    _QtechAcAirIfTxTotalLostFrams_Type()
)
qtechAcAirIfTxTotalLostFrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcAirIfTxTotalLostFrams.setStatus("current")
_QtechAcAirIfTxAssociateFrams_Type = Counter32
_QtechAcAirIfTxAssociateFrams_Object = MibScalar
qtechAcAirIfTxAssociateFrams = _QtechAcAirIfTxAssociateFrams_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 1, 14),
    _QtechAcAirIfTxAssociateFrams_Type()
)
qtechAcAirIfTxAssociateFrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcAirIfTxAssociateFrams.setStatus("current")
_QtechAcAirIfRxAssociateFrams_Type = Counter32
_QtechAcAirIfRxAssociateFrams_Object = MibScalar
qtechAcAirIfRxAssociateFrams = _QtechAcAirIfRxAssociateFrams_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 1, 15),
    _QtechAcAirIfRxAssociateFrams_Type()
)
qtechAcAirIfRxAssociateFrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcAirIfRxAssociateFrams.setStatus("current")
_QtechAcAirIfBeaconTotalFrams_Type = Counter32
_QtechAcAirIfBeaconTotalFrams_Object = MibScalar
qtechAcAirIfBeaconTotalFrams = _QtechAcAirIfBeaconTotalFrams_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 1, 16),
    _QtechAcAirIfBeaconTotalFrams_Type()
)
qtechAcAirIfBeaconTotalFrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcAirIfBeaconTotalFrams.setStatus("current")
_QtechAcAirIfRxTotalDataBytes_Type = Counter32
_QtechAcAirIfRxTotalDataBytes_Object = MibScalar
qtechAcAirIfRxTotalDataBytes = _QtechAcAirIfRxTotalDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 1, 17),
    _QtechAcAirIfRxTotalDataBytes_Type()
)
qtechAcAirIfRxTotalDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcAirIfRxTotalDataBytes.setStatus("current")
_QtechAcAirIfTxTotalDataBytes_Type = Counter32
_QtechAcAirIfTxTotalDataBytes_Object = MibScalar
qtechAcAirIfTxTotalDataBytes = _QtechAcAirIfTxTotalDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 1, 18),
    _QtechAcAirIfTxTotalDataBytes_Type()
)
qtechAcAirIfTxTotalDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcAirIfTxTotalDataBytes.setStatus("current")
_QtechAcAirRxFlux_Type = Integer32
_QtechAcAirRxFlux_Object = MibScalar
qtechAcAirRxFlux = _QtechAcAirRxFlux_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 1, 19),
    _QtechAcAirRxFlux_Type()
)
qtechAcAirRxFlux.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcAirRxFlux.setStatus("current")
_QtechAcAirTxFlux_Type = Integer32
_QtechAcAirTxFlux_Object = MibScalar
qtechAcAirTxFlux = _QtechAcAirTxFlux_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 1, 20),
    _QtechAcAirTxFlux_Type()
)
qtechAcAirTxFlux.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcAirTxFlux.setStatus("current")
_QtechInfoConfigObjects_ObjectIdentity = ObjectIdentity
qtechInfoConfigObjects = _QtechInfoConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 2)
)
_QtechInfoConfigTable_Object = MibTable
qtechInfoConfigTable = _QtechInfoConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 2, 1)
)
if mibBuilder.loadTexts:
    qtechInfoConfigTable.setStatus("current")
_QtechInfoConfigTableEntry_Object = MibTableRow
qtechInfoConfigTableEntry = _QtechInfoConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 2, 1, 1)
)
qtechInfoConfigTableEntry.setIndexNames(
    (0, "QTECH-AC-MGMT-MIB", "qtechApMacAddr"),
)
if mibBuilder.loadTexts:
    qtechInfoConfigTableEntry.setStatus("current")
_QtechAcAPWIDSWorkMode_Type = Integer32
_QtechAcAPWIDSWorkMode_Object = MibTableColumn
qtechAcAPWIDSWorkMode = _QtechAcAPWIDSWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 2, 1, 1, 1),
    _QtechAcAPWIDSWorkMode_Type()
)
qtechAcAPWIDSWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcAPWIDSWorkMode.setStatus("current")
_QtechStationConfigObjects_ObjectIdentity = ObjectIdentity
qtechStationConfigObjects = _QtechStationConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 4)
)
_QtechConfigStaInfoTable_Object = MibTable
qtechConfigStaInfoTable = _QtechConfigStaInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 4, 1)
)
if mibBuilder.loadTexts:
    qtechConfigStaInfoTable.setStatus("current")
_QtechConfigStaInfoTableEntry_Object = MibTableRow
qtechConfigStaInfoTableEntry = _QtechConfigStaInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 4, 1, 1)
)
qtechConfigStaInfoTableEntry.setIndexNames(
    (0, "QTECH-AC-MGMT-MIB", "qtechStaMacAddr"),
)
if mibBuilder.loadTexts:
    qtechConfigStaInfoTableEntry.setStatus("current")
_QtechACconfigAPBandwith_Type = Integer32
_QtechACconfigAPBandwith_Object = MibTableColumn
qtechACconfigAPBandwith = _QtechACconfigAPBandwith_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 4, 1, 1, 1),
    _QtechACconfigAPBandwith_Type()
)
qtechACconfigAPBandwith.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechACconfigAPBandwith.setStatus("current")
_QtechAirIfStatisticsObjects_ObjectIdentity = ObjectIdentity
qtechAirIfStatisticsObjects = _QtechAirIfStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 6)
)
_QtechAirIfInfoStatisticsTable_Object = MibTable
qtechAirIfInfoStatisticsTable = _QtechAirIfInfoStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 6, 1)
)
if mibBuilder.loadTexts:
    qtechAirIfInfoStatisticsTable.setStatus("current")
_QtechAirIfInfoStatisticsTableEntry_Object = MibTableRow
qtechAirIfInfoStatisticsTableEntry = _QtechAirIfInfoStatisticsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 6, 1, 1)
)
qtechAirIfInfoStatisticsTableEntry.setIndexNames(
    (0, "QTECH-AC-MGMT-MIB", "qtechApgWlanId"),
    (0, "QTECH-AC-MGMT-MIB", "qtechApMacAddr"),
)
if mibBuilder.loadTexts:
    qtechAirIfInfoStatisticsTableEntry.setStatus("current")
_QtechRxTotalDataFrams_Type = Counter32
_QtechRxTotalDataFrams_Object = MibTableColumn
qtechRxTotalDataFrams = _QtechRxTotalDataFrams_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 6, 1, 1, 1),
    _QtechRxTotalDataFrams_Type()
)
qtechRxTotalDataFrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRxTotalDataFrams.setStatus("current")
_QtechTxTotalDataFrams_Type = Counter32
_QtechTxTotalDataFrams_Object = MibTableColumn
qtechTxTotalDataFrams = _QtechTxTotalDataFrams_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 6, 1, 1, 2),
    _QtechTxTotalDataFrams_Type()
)
qtechTxTotalDataFrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechTxTotalDataFrams.setStatus("current")
_QtechTxLostDataFrams_Type = Counter32
_QtechTxLostDataFrams_Object = MibTableColumn
qtechTxLostDataFrams = _QtechTxLostDataFrams_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 6, 1, 1, 3),
    _QtechTxLostDataFrams_Type()
)
qtechTxLostDataFrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechTxLostDataFrams.setStatus("current")
_QtechTxAssociateFrams_Type = Counter32
_QtechTxAssociateFrams_Object = MibTableColumn
qtechTxAssociateFrams = _QtechTxAssociateFrams_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 6, 1, 1, 4),
    _QtechTxAssociateFrams_Type()
)
qtechTxAssociateFrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechTxAssociateFrams.setStatus("current")
_QtechRxAssociateFrams_Type = Counter32
_QtechRxAssociateFrams_Object = MibTableColumn
qtechRxAssociateFrams = _QtechRxAssociateFrams_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 6, 1, 1, 5),
    _QtechRxAssociateFrams_Type()
)
qtechRxAssociateFrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRxAssociateFrams.setStatus("current")
_QtechBeaconFrams_Type = Counter32
_QtechBeaconFrams_Object = MibTableColumn
qtechBeaconFrams = _QtechBeaconFrams_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 6, 1, 1, 6),
    _QtechBeaconFrams_Type()
)
qtechBeaconFrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBeaconFrams.setStatus("current")
_QtechRxTotalDataBytes_Type = Counter32
_QtechRxTotalDataBytes_Object = MibTableColumn
qtechRxTotalDataBytes = _QtechRxTotalDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 6, 1, 1, 7),
    _QtechRxTotalDataBytes_Type()
)
qtechRxTotalDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRxTotalDataBytes.setStatus("current")
_QtechTxTotalDataBytes_Type = Counter32
_QtechTxTotalDataBytes_Object = MibTableColumn
qtechTxTotalDataBytes = _QtechTxTotalDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 6, 1, 1, 8),
    _QtechTxTotalDataBytes_Type()
)
qtechTxTotalDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechTxTotalDataBytes.setStatus("current")
_QtechRESUtilization_Type = Integer32
_QtechRESUtilization_Object = MibTableColumn
qtechRESUtilization = _QtechRESUtilization_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 6, 1, 1, 9),
    _QtechRESUtilization_Type()
)
qtechRESUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRESUtilization.setStatus("current")
_QtechAirIfTxResendDataTable_Object = MibTable
qtechAirIfTxResendDataTable = _QtechAirIfTxResendDataTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 6, 2)
)
if mibBuilder.loadTexts:
    qtechAirIfTxResendDataTable.setStatus("current")
_QtechAirIfTxResendDataTableEntry_Object = MibTableRow
qtechAirIfTxResendDataTableEntry = _QtechAirIfTxResendDataTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 6, 2, 1)
)
qtechAirIfTxResendDataTableEntry.setIndexNames(
    (0, "QTECH-AC-MGMT-MIB", "qtechStaMacAddr"),
)
if mibBuilder.loadTexts:
    qtechAirIfTxResendDataTableEntry.setStatus("current")
_QtechStaResendDataFrams_Type = Counter32
_QtechStaResendDataFrams_Object = MibTableColumn
qtechStaResendDataFrams = _QtechStaResendDataFrams_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 6, 2, 1, 1),
    _QtechStaResendDataFrams_Type()
)
qtechStaResendDataFrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaResendDataFrams.setStatus("current")
_QtechTermServiceStatistics_ObjectIdentity = ObjectIdentity
qtechTermServiceStatistics = _QtechTermServiceStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7)
)
_QtechTermServiceStatisticsWithSSID_ObjectIdentity = ObjectIdentity
qtechTermServiceStatisticsWithSSID = _QtechTermServiceStatisticsWithSSID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 1)
)
_QtechTermServiceStaticWithSSIDTable_Object = MibTable
qtechTermServiceStaticWithSSIDTable = _QtechTermServiceStaticWithSSIDTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 1, 1)
)
if mibBuilder.loadTexts:
    qtechTermServiceStaticWithSSIDTable.setStatus("current")
_QtechTermServiceStaticWithSSIDTableEntry_Object = MibTableRow
qtechTermServiceStaticWithSSIDTableEntry = _QtechTermServiceStaticWithSSIDTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 1, 1, 1)
)
qtechTermServiceStaticWithSSIDTableEntry.setIndexNames(
    (0, "QTECH-AC-MGMT-MIB", "qtechApgWlanId"),
)
if mibBuilder.loadTexts:
    qtechTermServiceStaticWithSSIDTableEntry.setStatus("current")
_QtechTotalUserNum_Type = Integer32
_QtechTotalUserNum_Object = MibTableColumn
qtechTotalUserNum = _QtechTotalUserNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 1, 1, 1, 1),
    _QtechTotalUserNum_Type()
)
qtechTotalUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechTotalUserNum.setStatus("current")
_QtechCurrentUserNum_Type = Integer32
_QtechCurrentUserNum_Object = MibTableColumn
qtechCurrentUserNum = _QtechCurrentUserNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 1, 1, 1, 2),
    _QtechCurrentUserNum_Type()
)
qtechCurrentUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCurrentUserNum.setStatus("current")
_QtechStaReqAccessTimes_Type = Integer32
_QtechStaReqAccessTimes_Object = MibTableColumn
qtechStaReqAccessTimes = _QtechStaReqAccessTimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 1, 1, 1, 3),
    _QtechStaReqAccessTimes_Type()
)
qtechStaReqAccessTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaReqAccessTimes.setStatus("current")
_QtechRspStaAccessReqTimes_Type = Integer32
_QtechRspStaAccessReqTimes_Object = MibTableColumn
qtechRspStaAccessReqTimes = _QtechRspStaAccessReqTimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 1, 1, 1, 4),
    _QtechRspStaAccessReqTimes_Type()
)
qtechRspStaAccessReqTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRspStaAccessReqTimes.setStatus("current")
_QtechStaAccessSucessTimes_Type = Integer32
_QtechStaAccessSucessTimes_Object = MibTableColumn
qtechStaAccessSucessTimes = _QtechStaAccessSucessTimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 1, 1, 1, 5),
    _QtechStaAccessSucessTimes_Type()
)
qtechStaAccessSucessTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaAccessSucessTimes.setStatus("current")
_QtechIneffiLinkVerifyFailTime_Type = Integer32
_QtechIneffiLinkVerifyFailTime_Object = MibTableColumn
qtechIneffiLinkVerifyFailTime = _QtechIneffiLinkVerifyFailTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 1, 1, 1, 6),
    _QtechIneffiLinkVerifyFailTime_Type()
)
qtechIneffiLinkVerifyFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIneffiLinkVerifyFailTime.setStatus("current")
_QtechTimeoutLinkVerifyFailTime_Type = Integer32
_QtechTimeoutLinkVerifyFailTime_Object = MibTableColumn
qtechTimeoutLinkVerifyFailTime = _QtechTimeoutLinkVerifyFailTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 1, 1, 1, 7),
    _QtechTimeoutLinkVerifyFailTime_Type()
)
qtechTimeoutLinkVerifyFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechTimeoutLinkVerifyFailTime.setStatus("current")
_QtechInefficiencyLinkVerifyFailTime_Type = Integer32
_QtechInefficiencyLinkVerifyFailTime_Object = MibTableColumn
qtechInefficiencyLinkVerifyFailTime = _QtechInefficiencyLinkVerifyFailTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 1, 1, 1, 8),
    _QtechInefficiencyLinkVerifyFailTime_Type()
)
qtechInefficiencyLinkVerifyFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechInefficiencyLinkVerifyFailTime.setStatus("current")
_QtechOtherReasonLinkVerifyFailTime_Type = Integer32
_QtechOtherReasonLinkVerifyFailTime_Object = MibTableColumn
qtechOtherReasonLinkVerifyFailTime = _QtechOtherReasonLinkVerifyFailTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 1, 1, 1, 9),
    _QtechOtherReasonLinkVerifyFailTime_Type()
)
qtechOtherReasonLinkVerifyFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOtherReasonLinkVerifyFailTime.setStatus("current")
_QtechIneffiAssociationFailTime_Type = Integer32
_QtechIneffiAssociationFailTime_Object = MibTableColumn
qtechIneffiAssociationFailTime = _QtechIneffiAssociationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 1, 1, 1, 10),
    _QtechIneffiAssociationFailTime_Type()
)
qtechIneffiAssociationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIneffiAssociationFailTime.setStatus("current")
_QtechTimeoutAssociationFailTime_Type = Integer32
_QtechTimeoutAssociationFailTime_Object = MibTableColumn
qtechTimeoutAssociationFailTime = _QtechTimeoutAssociationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 1, 1, 1, 11),
    _QtechTimeoutAssociationFailTime_Type()
)
qtechTimeoutAssociationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechTimeoutAssociationFailTime.setStatus("current")
_QtechInefficiencyAssociationFailTime_Type = Integer32
_QtechInefficiencyAssociationFailTime_Object = MibTableColumn
qtechInefficiencyAssociationFailTime = _QtechInefficiencyAssociationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 1, 1, 1, 12),
    _QtechInefficiencyAssociationFailTime_Type()
)
qtechInefficiencyAssociationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechInefficiencyAssociationFailTime.setStatus("current")
_QtechOtherReasonAssociationFailTime_Type = Integer32
_QtechOtherReasonAssociationFailTime_Object = MibTableColumn
qtechOtherReasonAssociationFailTime = _QtechOtherReasonAssociationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 1, 1, 1, 13),
    _QtechOtherReasonAssociationFailTime_Type()
)
qtechOtherReasonAssociationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOtherReasonAssociationFailTime.setStatus("current")
_QtechTotalReassociationAtmptTimes_Type = Integer32
_QtechTotalReassociationAtmptTimes_Object = MibTableColumn
qtechTotalReassociationAtmptTimes = _QtechTotalReassociationAtmptTimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 1, 1, 1, 14),
    _QtechTotalReassociationAtmptTimes_Type()
)
qtechTotalReassociationAtmptTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechTotalReassociationAtmptTimes.setStatus("current")
_QtechTotalReassociationSuccessTimes_Type = Integer32
_QtechTotalReassociationSuccessTimes_Object = MibTableColumn
qtechTotalReassociationSuccessTimes = _QtechTotalReassociationSuccessTimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 1, 1, 1, 15),
    _QtechTotalReassociationSuccessTimes_Type()
)
qtechTotalReassociationSuccessTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechTotalReassociationSuccessTimes.setStatus("current")
_QtechIneffiReassociationFailTime_Type = Integer32
_QtechIneffiReassociationFailTime_Object = MibTableColumn
qtechIneffiReassociationFailTime = _QtechIneffiReassociationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 1, 1, 1, 16),
    _QtechIneffiReassociationFailTime_Type()
)
qtechIneffiReassociationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIneffiReassociationFailTime.setStatus("current")
_QtechTimeoutReassociationFailTime_Type = Integer32
_QtechTimeoutReassociationFailTime_Object = MibTableColumn
qtechTimeoutReassociationFailTime = _QtechTimeoutReassociationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 1, 1, 1, 17),
    _QtechTimeoutReassociationFailTime_Type()
)
qtechTimeoutReassociationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechTimeoutReassociationFailTime.setStatus("current")
_QtechInefficiencyReassociationFailTime_Type = Integer32
_QtechInefficiencyReassociationFailTime_Object = MibTableColumn
qtechInefficiencyReassociationFailTime = _QtechInefficiencyReassociationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 1, 1, 1, 18),
    _QtechInefficiencyReassociationFailTime_Type()
)
qtechInefficiencyReassociationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechInefficiencyReassociationFailTime.setStatus("current")
_QtechOtherReasonReassociationFailTime_Type = Integer32
_QtechOtherReasonReassociationFailTime_Object = MibTableColumn
qtechOtherReasonReassociationFailTime = _QtechOtherReasonReassociationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 1, 1, 1, 19),
    _QtechOtherReasonReassociationFailTime_Type()
)
qtechOtherReasonReassociationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOtherReasonReassociationFailTime.setStatus("current")
_QtechTotalIdentificationAtmptTimes_Type = Integer32
_QtechTotalIdentificationAtmptTimes_Object = MibTableColumn
qtechTotalIdentificationAtmptTimes = _QtechTotalIdentificationAtmptTimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 1, 1, 1, 20),
    _QtechTotalIdentificationAtmptTimes_Type()
)
qtechTotalIdentificationAtmptTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechTotalIdentificationAtmptTimes.setStatus("current")
_QtechTotalIdentificationSuccessTimes_Type = Integer32
_QtechTotalIdentificationSuccessTimes_Object = MibTableColumn
qtechTotalIdentificationSuccessTimes = _QtechTotalIdentificationSuccessTimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 1, 1, 1, 21),
    _QtechTotalIdentificationSuccessTimes_Type()
)
qtechTotalIdentificationSuccessTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechTotalIdentificationSuccessTimes.setStatus("current")
_QtechPwdErrorIdentifyFailTime_Type = Integer32
_QtechPwdErrorIdentifyFailTime_Object = MibTableColumn
qtechPwdErrorIdentifyFailTime = _QtechPwdErrorIdentifyFailTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 1, 1, 1, 22),
    _QtechPwdErrorIdentifyFailTime_Type()
)
qtechPwdErrorIdentifyFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPwdErrorIdentifyFailTime.setStatus("current")
_QtechIneffiIdentificationFailTime_Type = Integer32
_QtechIneffiIdentificationFailTime_Object = MibTableColumn
qtechIneffiIdentificationFailTime = _QtechIneffiIdentificationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 1, 1, 1, 23),
    _QtechIneffiIdentificationFailTime_Type()
)
qtechIneffiIdentificationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIneffiIdentificationFailTime.setStatus("current")
_QtechTimeoutIdentificationFailTime_Type = Integer32
_QtechTimeoutIdentificationFailTime_Object = MibTableColumn
qtechTimeoutIdentificationFailTime = _QtechTimeoutIdentificationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 1, 1, 1, 24),
    _QtechTimeoutIdentificationFailTime_Type()
)
qtechTimeoutIdentificationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechTimeoutIdentificationFailTime.setStatus("current")
_QtechInefficiencyIdentificationFailTime_Type = Integer32
_QtechInefficiencyIdentificationFailTime_Object = MibTableColumn
qtechInefficiencyIdentificationFailTime = _QtechInefficiencyIdentificationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 1, 1, 1, 25),
    _QtechInefficiencyIdentificationFailTime_Type()
)
qtechInefficiencyIdentificationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechInefficiencyIdentificationFailTime.setStatus("current")
_QtechOtherReasonIdentificationFailTime_Type = Integer32
_QtechOtherReasonIdentificationFailTime_Object = MibTableColumn
qtechOtherReasonIdentificationFailTime = _QtechOtherReasonIdentificationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 1, 1, 1, 26),
    _QtechOtherReasonIdentificationFailTime_Type()
)
qtechOtherReasonIdentificationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOtherReasonIdentificationFailTime.setStatus("current")
_QtechTotalRemoveLinkVerifyFailTimes_Type = Integer32
_QtechTotalRemoveLinkVerifyFailTimes_Object = MibTableColumn
qtechTotalRemoveLinkVerifyFailTimes = _QtechTotalRemoveLinkVerifyFailTimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 1, 1, 1, 27),
    _QtechTotalRemoveLinkVerifyFailTimes_Type()
)
qtechTotalRemoveLinkVerifyFailTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechTotalRemoveLinkVerifyFailTimes.setStatus("current")
_QtechLeaveAPCoverageRemoveLinkVerifyFailTimes_Type = Integer32
_QtechLeaveAPCoverageRemoveLinkVerifyFailTimes_Object = MibTableColumn
qtechLeaveAPCoverageRemoveLinkVerifyFailTimes = _QtechLeaveAPCoverageRemoveLinkVerifyFailTimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 1, 1, 1, 28),
    _QtechLeaveAPCoverageRemoveLinkVerifyFailTimes_Type()
)
qtechLeaveAPCoverageRemoveLinkVerifyFailTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLeaveAPCoverageRemoveLinkVerifyFailTimes.setStatus("current")
_QtechInefficiencyRemoveLinkVerifyFailTime_Type = Integer32
_QtechInefficiencyRemoveLinkVerifyFailTime_Object = MibTableColumn
qtechInefficiencyRemoveLinkVerifyFailTime = _QtechInefficiencyRemoveLinkVerifyFailTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 1, 1, 1, 29),
    _QtechInefficiencyRemoveLinkVerifyFailTime_Type()
)
qtechInefficiencyRemoveLinkVerifyFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechInefficiencyRemoveLinkVerifyFailTime.setStatus("current")
_QtechLinkVerifyFailRemoveLinkVerifyFailTime_Type = Integer32
_QtechLinkVerifyFailRemoveLinkVerifyFailTime_Object = MibTableColumn
qtechLinkVerifyFailRemoveLinkVerifyFailTime = _QtechLinkVerifyFailRemoveLinkVerifyFailTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 1, 1, 1, 30),
    _QtechLinkVerifyFailRemoveLinkVerifyFailTime_Type()
)
qtechLinkVerifyFailRemoveLinkVerifyFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLinkVerifyFailRemoveLinkVerifyFailTime.setStatus("current")
_QtechOtherReasonRemoveLinkVerifyFailTime_Type = Integer32
_QtechOtherReasonRemoveLinkVerifyFailTime_Object = MibTableColumn
qtechOtherReasonRemoveLinkVerifyFailTime = _QtechOtherReasonRemoveLinkVerifyFailTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 1, 1, 1, 31),
    _QtechOtherReasonRemoveLinkVerifyFailTime_Type()
)
qtechOtherReasonRemoveLinkVerifyFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOtherReasonRemoveLinkVerifyFailTime.setStatus("current")
_QtechTotalRemoveLinkAssociationTimes_Type = Integer32
_QtechTotalRemoveLinkAssociationTimes_Object = MibTableColumn
qtechTotalRemoveLinkAssociationTimes = _QtechTotalRemoveLinkAssociationTimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 1, 1, 1, 32),
    _QtechTotalRemoveLinkAssociationTimes_Type()
)
qtechTotalRemoveLinkAssociationTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechTotalRemoveLinkAssociationTimes.setStatus("current")
_QtechLeaveAPCoverageRemoveAssociationFailTimes_Type = Integer32
_QtechLeaveAPCoverageRemoveAssociationFailTimes_Object = MibTableColumn
qtechLeaveAPCoverageRemoveAssociationFailTimes = _QtechLeaveAPCoverageRemoveAssociationFailTimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 1, 1, 1, 33),
    _QtechLeaveAPCoverageRemoveAssociationFailTimes_Type()
)
qtechLeaveAPCoverageRemoveAssociationFailTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLeaveAPCoverageRemoveAssociationFailTimes.setStatus("current")
_QtechInefficiencyRemoveAssociationFailTime_Type = Integer32
_QtechInefficiencyRemoveAssociationFailTime_Object = MibTableColumn
qtechInefficiencyRemoveAssociationFailTime = _QtechInefficiencyRemoveAssociationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 1, 1, 1, 34),
    _QtechInefficiencyRemoveAssociationFailTime_Type()
)
qtechInefficiencyRemoveAssociationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechInefficiencyRemoveAssociationFailTime.setStatus("current")
_QtechAssociationFailRemoveAssociationFailTime_Type = Integer32
_QtechAssociationFailRemoveAssociationFailTime_Object = MibTableColumn
qtechAssociationFailRemoveAssociationFailTime = _QtechAssociationFailRemoveAssociationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 1, 1, 1, 35),
    _QtechAssociationFailRemoveAssociationFailTime_Type()
)
qtechAssociationFailRemoveAssociationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAssociationFailRemoveAssociationFailTime.setStatus("current")
_QtechOtherReasonRemoveAssociationFailTime_Type = Integer32
_QtechOtherReasonRemoveAssociationFailTime_Object = MibTableColumn
qtechOtherReasonRemoveAssociationFailTime = _QtechOtherReasonRemoveAssociationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 1, 1, 1, 36),
    _QtechOtherReasonRemoveAssociationFailTime_Type()
)
qtechOtherReasonRemoveAssociationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechOtherReasonRemoveAssociationFailTime.setStatus("current")
_QtechTermServiceStatisticsWithAP_ObjectIdentity = ObjectIdentity
qtechTermServiceStatisticsWithAP = _QtechTermServiceStatisticsWithAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 2)
)
_QtechTermServiceStaticWithAPTable_Object = MibTable
qtechTermServiceStaticWithAPTable = _QtechTermServiceStaticWithAPTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 2, 1)
)
if mibBuilder.loadTexts:
    qtechTermServiceStaticWithAPTable.setStatus("current")
_QtechTermServiceStaticWithAPTableEntry_Object = MibTableRow
qtechTermServiceStaticWithAPTableEntry = _QtechTermServiceStaticWithAPTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 2, 1, 1)
)
qtechTermServiceStaticWithAPTableEntry.setIndexNames(
    (0, "QTECH-AC-MGMT-MIB", "qtechApMacAddr"),
)
if mibBuilder.loadTexts:
    qtechTermServiceStaticWithAPTableEntry.setStatus("current")
_QtechUserAccumulateTime_Type = Counter32
_QtechUserAccumulateTime_Object = MibTableColumn
qtechUserAccumulateTime = _QtechUserAccumulateTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 2, 1, 1, 1),
    _QtechUserAccumulateTime_Type()
)
qtechUserAccumulateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechUserAccumulateTime.setStatus("current")
_QtechAssociaFailTimes_Type = Counter32
_QtechAssociaFailTimes_Object = MibTableColumn
qtechAssociaFailTimes = _QtechAssociaFailTimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 2, 1, 1, 2),
    _QtechAssociaFailTimes_Type()
)
qtechAssociaFailTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAssociaFailTimes.setStatus("current")
_QtechTermServiceSTatisticsWithStation_ObjectIdentity = ObjectIdentity
qtechTermServiceSTatisticsWithStation = _QtechTermServiceSTatisticsWithStation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 3)
)
_QtechTermServiceStationWithStationTable_Object = MibTable
qtechTermServiceStationWithStationTable = _QtechTermServiceStationWithStationTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 3, 1)
)
if mibBuilder.loadTexts:
    qtechTermServiceStationWithStationTable.setStatus("current")
_QtechTermServiceStationWithStationTableEntry_Object = MibTableRow
qtechTermServiceStationWithStationTableEntry = _QtechTermServiceStationWithStationTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 3, 1, 1)
)
qtechTermServiceStationWithStationTableEntry.setIndexNames(
    (0, "QTECH-AC-MGMT-MIB", "qtechApgWlanId"),
    (0, "QTECH-AC-MGMT-MIB", "qtechStaMacAddr"),
)
if mibBuilder.loadTexts:
    qtechTermServiceStationWithStationTableEntry.setStatus("current")
_QtechStaAssociateTime_Type = Counter32
_QtechStaAssociateTime_Object = MibTableColumn
qtechStaAssociateTime = _QtechStaAssociateTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 3, 1, 1, 2),
    _QtechStaAssociateTime_Type()
)
qtechStaAssociateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaAssociateTime.setStatus("current")
_QtechRxStaDataFrams_Type = Counter32
_QtechRxStaDataFrams_Object = MibTableColumn
qtechRxStaDataFrams = _QtechRxStaDataFrams_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 3, 1, 1, 3),
    _QtechRxStaDataFrams_Type()
)
qtechRxStaDataFrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRxStaDataFrams.setStatus("current")
_QtechRXStaErrorFrams_Type = Counter32
_QtechRXStaErrorFrams_Object = MibTableColumn
qtechRXStaErrorFrams = _QtechRXStaErrorFrams_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 3, 1, 1, 4),
    _QtechRXStaErrorFrams_Type()
)
qtechRXStaErrorFrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRXStaErrorFrams.setStatus("current")
_QtechTxStaDataFrams_Type = Counter32
_QtechTxStaDataFrams_Object = MibTableColumn
qtechTxStaDataFrams = _QtechTxStaDataFrams_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 3, 1, 1, 5),
    _QtechTxStaDataFrams_Type()
)
qtechTxStaDataFrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechTxStaDataFrams.setStatus("current")
_QtechReSendDataFrams_Type = Counter32
_QtechReSendDataFrams_Object = MibTableColumn
qtechReSendDataFrams = _QtechReSendDataFrams_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 3, 1, 1, 6),
    _QtechReSendDataFrams_Type()
)
qtechReSendDataFrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechReSendDataFrams.setStatus("current")
_QtechStaRxAvgSpeed_Type = Integer32
_QtechStaRxAvgSpeed_Object = MibTableColumn
qtechStaRxAvgSpeed = _QtechStaRxAvgSpeed_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 3, 1, 1, 7),
    _QtechStaRxAvgSpeed_Type()
)
qtechStaRxAvgSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaRxAvgSpeed.setStatus("current")
_QtechStaTxAvgSpeed_Type = Integer32
_QtechStaTxAvgSpeed_Object = MibTableColumn
qtechStaTxAvgSpeed = _QtechStaTxAvgSpeed_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 3, 1, 1, 8),
    _QtechStaTxAvgSpeed_Type()
)
qtechStaTxAvgSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaTxAvgSpeed.setStatus("current")
_QtechStaThroughput_Type = Integer32
_QtechStaThroughput_Object = MibTableColumn
qtechStaThroughput = _QtechStaThroughput_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 3, 1, 1, 9),
    _QtechStaThroughput_Type()
)
qtechStaThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaThroughput.setStatus("current")
_QtechStaSignalStrength_Type = Integer32
_QtechStaSignalStrength_Object = MibTableColumn
qtechStaSignalStrength = _QtechStaSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 3, 1, 1, 10),
    _QtechStaSignalStrength_Type()
)
qtechStaSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaSignalStrength.setStatus("current")
_QtechStaSignalNoise_Type = Integer32
_QtechStaSignalNoise_Object = MibTableColumn
qtechStaSignalNoise = _QtechStaSignalNoise_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 7, 3, 1, 1, 11),
    _QtechStaSignalNoise_Type()
)
qtechStaSignalNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaSignalNoise.setStatus("current")
_QtechDOT11WIDSParamObjects_ObjectIdentity = ObjectIdentity
qtechDOT11WIDSParamObjects = _QtechDOT11WIDSParamObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8)
)
_QtechDot11WIDSInfoTable_Object = MibTable
qtechDot11WIDSInfoTable = _QtechDot11WIDSInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 1)
)
if mibBuilder.loadTexts:
    qtechDot11WIDSInfoTable.setStatus("current")
_QtechDot11WIDSInfoEntry_Object = MibTableRow
qtechDot11WIDSInfoEntry = _QtechDot11WIDSInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 1, 1)
)
qtechDot11WIDSInfoEntry.setIndexNames(
    (0, "QTECH-WLAN-FIT-AP-IN-MIB", "qtechDot11WIDSLocalIndex"),
)
if mibBuilder.loadTexts:
    qtechDot11WIDSInfoEntry.setStatus("current")
_QtechDot11WIDSLocalIndex_Type = Integer32
_QtechDot11WIDSLocalIndex_Object = MibTableColumn
qtechDot11WIDSLocalIndex = _QtechDot11WIDSLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 1, 1, 1),
    _QtechDot11WIDSLocalIndex_Type()
)
qtechDot11WIDSLocalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechDot11WIDSLocalIndex.setStatus("current")
_QtechDot11WIDSpermittedSSID_Type = DisplayString
_QtechDot11WIDSpermittedSSID_Object = MibTableColumn
qtechDot11WIDSpermittedSSID = _QtechDot11WIDSpermittedSSID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 1, 1, 2),
    _QtechDot11WIDSpermittedSSID_Type()
)
qtechDot11WIDSpermittedSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSpermittedSSID.setStatus("current")
_QtechDot11WIDSpermitBSSID_Type = MacAddress
_QtechDot11WIDSpermitBSSID_Object = MibTableColumn
qtechDot11WIDSpermitBSSID = _QtechDot11WIDSpermitBSSID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 1, 1, 3),
    _QtechDot11WIDSpermitBSSID_Type()
)
qtechDot11WIDSpermitBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSpermitBSSID.setStatus("current")
_QtechDot11WIDSDeviceOUI_Type = DisplayString
_QtechDot11WIDSDeviceOUI_Object = MibTableColumn
qtechDot11WIDSDeviceOUI = _QtechDot11WIDSDeviceOUI_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 1, 1, 4),
    _QtechDot11WIDSDeviceOUI_Type()
)
qtechDot11WIDSDeviceOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSDeviceOUI.setStatus("current")
_QtechDot11WIDSSuspiciousAPBSS_Type = MacAddress
_QtechDot11WIDSSuspiciousAPBSS_Object = MibTableColumn
qtechDot11WIDSSuspiciousAPBSS = _QtechDot11WIDSSuspiciousAPBSS_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 1, 1, 5),
    _QtechDot11WIDSSuspiciousAPBSS_Type()
)
qtechDot11WIDSSuspiciousAPBSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSSuspiciousAPBSS.setStatus("current")
_QtechDot11WIDSSuspiciousAPCount_Type = Integer32
_QtechDot11WIDSSuspiciousAPCount_Object = MibTableColumn
qtechDot11WIDSSuspiciousAPCount = _QtechDot11WIDSSuspiciousAPCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 1, 1, 6),
    _QtechDot11WIDSSuspiciousAPCount_Type()
)
qtechDot11WIDSSuspiciousAPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSSuspiciousAPCount.setStatus("current")
_QtechDot11WIDSMomentFirstTimeDetectedSusAP_Type = TimeTicks
_QtechDot11WIDSMomentFirstTimeDetectedSusAP_Object = MibTableColumn
qtechDot11WIDSMomentFirstTimeDetectedSusAP = _QtechDot11WIDSMomentFirstTimeDetectedSusAP_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 1, 1, 7),
    _QtechDot11WIDSMomentFirstTimeDetectedSusAP_Type()
)
qtechDot11WIDSMomentFirstTimeDetectedSusAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSMomentFirstTimeDetectedSusAP.setStatus("current")
_QtechDot11WIDSMomentLastTimeDetectedSusAP_Type = TimeTicks
_QtechDot11WIDSMomentLastTimeDetectedSusAP_Object = MibTableColumn
qtechDot11WIDSMomentLastTimeDetectedSusAP = _QtechDot11WIDSMomentLastTimeDetectedSusAP_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 1, 1, 8),
    _QtechDot11WIDSMomentLastTimeDetectedSusAP_Type()
)
qtechDot11WIDSMomentLastTimeDetectedSusAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSMomentLastTimeDetectedSusAP.setStatus("current")
_QtechDot11WIDSSuspiciousAPSSID_Type = DisplayString
_QtechDot11WIDSSuspiciousAPSSID_Object = MibTableColumn
qtechDot11WIDSSuspiciousAPSSID = _QtechDot11WIDSSuspiciousAPSSID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 1, 1, 9),
    _QtechDot11WIDSSuspiciousAPSSID_Type()
)
qtechDot11WIDSSuspiciousAPSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSSuspiciousAPSSID.setStatus("current")
_QtechDot11WIDSSuspiciousAPMaxSignalStrength_Type = Integer32
_QtechDot11WIDSSuspiciousAPMaxSignalStrength_Object = MibTableColumn
qtechDot11WIDSSuspiciousAPMaxSignalStrength = _QtechDot11WIDSSuspiciousAPMaxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 1, 1, 10),
    _QtechDot11WIDSSuspiciousAPMaxSignalStrength_Type()
)
qtechDot11WIDSSuspiciousAPMaxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSSuspiciousAPMaxSignalStrength.setStatus("current")
_QtechDot11WIDSSuspiciousAPUsingChannel_Type = Integer32
_QtechDot11WIDSSuspiciousAPUsingChannel_Object = MibTableColumn
qtechDot11WIDSSuspiciousAPUsingChannel = _QtechDot11WIDSSuspiciousAPUsingChannel_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 1, 1, 11),
    _QtechDot11WIDSSuspiciousAPUsingChannel_Type()
)
qtechDot11WIDSSuspiciousAPUsingChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSSuspiciousAPUsingChannel.setStatus("current")
_QtechDot11WIDSSuspiciousAPFrameEncrption_Type = Integer32
_QtechDot11WIDSSuspiciousAPFrameEncrption_Object = MibTableColumn
qtechDot11WIDSSuspiciousAPFrameEncrption = _QtechDot11WIDSSuspiciousAPFrameEncrption_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 1, 1, 12),
    _QtechDot11WIDSSuspiciousAPFrameEncrption_Type()
)
qtechDot11WIDSSuspiciousAPFrameEncrption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSSuspiciousAPFrameEncrption.setStatus("current")
_QtechDot11WIDSSuspiciousAPNeedsDealingTag_Type = TruthValue
_QtechDot11WIDSSuspiciousAPNeedsDealingTag_Object = MibTableColumn
qtechDot11WIDSSuspiciousAPNeedsDealingTag = _QtechDot11WIDSSuspiciousAPNeedsDealingTag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 1, 1, 13),
    _QtechDot11WIDSSuspiciousAPNeedsDealingTag_Type()
)
qtechDot11WIDSSuspiciousAPNeedsDealingTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSSuspiciousAPNeedsDealingTag.setStatus("current")
_QtechDot11WIDSSuspiciousAPIgnoredTag_Type = TruthValue
_QtechDot11WIDSSuspiciousAPIgnoredTag_Object = MibTableColumn
qtechDot11WIDSSuspiciousAPIgnoredTag = _QtechDot11WIDSSuspiciousAPIgnoredTag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 1, 1, 14),
    _QtechDot11WIDSSuspiciousAPIgnoredTag_Type()
)
qtechDot11WIDSSuspiciousAPIgnoredTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSSuspiciousAPIgnoredTag.setStatus("current")
_QtechDot11WIDSSuspiciousSTAMAC_Type = MacAddress
_QtechDot11WIDSSuspiciousSTAMAC_Object = MibTableColumn
qtechDot11WIDSSuspiciousSTAMAC = _QtechDot11WIDSSuspiciousSTAMAC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 1, 1, 15),
    _QtechDot11WIDSSuspiciousSTAMAC_Type()
)
qtechDot11WIDSSuspiciousSTAMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSSuspiciousSTAMAC.setStatus("current")
_QtechDot11WIDSAPCountDetectingSuspiciousSTA_Type = Integer32
_QtechDot11WIDSAPCountDetectingSuspiciousSTA_Object = MibTableColumn
qtechDot11WIDSAPCountDetectingSuspiciousSTA = _QtechDot11WIDSAPCountDetectingSuspiciousSTA_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 1, 1, 16),
    _QtechDot11WIDSAPCountDetectingSuspiciousSTA_Type()
)
qtechDot11WIDSAPCountDetectingSuspiciousSTA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSAPCountDetectingSuspiciousSTA.setStatus("current")
_QtechDot11WIDSMomentFirstTimeDetectedSusSTA_Type = TimeTicks
_QtechDot11WIDSMomentFirstTimeDetectedSusSTA_Object = MibTableColumn
qtechDot11WIDSMomentFirstTimeDetectedSusSTA = _QtechDot11WIDSMomentFirstTimeDetectedSusSTA_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 1, 1, 17),
    _QtechDot11WIDSMomentFirstTimeDetectedSusSTA_Type()
)
qtechDot11WIDSMomentFirstTimeDetectedSusSTA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSMomentFirstTimeDetectedSusSTA.setStatus("current")
_QtechDot11WIDSMomentLastTimeDetectedSusSTA_Type = TimeTicks
_QtechDot11WIDSMomentLastTimeDetectedSusSTA_Object = MibTableColumn
qtechDot11WIDSMomentLastTimeDetectedSusSTA = _QtechDot11WIDSMomentLastTimeDetectedSusSTA_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 1, 1, 18),
    _QtechDot11WIDSMomentLastTimeDetectedSusSTA_Type()
)
qtechDot11WIDSMomentLastTimeDetectedSusSTA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSMomentLastTimeDetectedSusSTA.setStatus("current")
_QtechDot11WIDSBSSIDSuspiciousSTAAccessing_Type = MacAddress
_QtechDot11WIDSBSSIDSuspiciousSTAAccessing_Object = MibTableColumn
qtechDot11WIDSBSSIDSuspiciousSTAAccessing = _QtechDot11WIDSBSSIDSuspiciousSTAAccessing_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 1, 1, 19),
    _QtechDot11WIDSBSSIDSuspiciousSTAAccessing_Type()
)
qtechDot11WIDSBSSIDSuspiciousSTAAccessing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSBSSIDSuspiciousSTAAccessing.setStatus("current")
_QtechDot11WIDSSuspiciousSTAMaxSignalStrength_Type = Integer32
_QtechDot11WIDSSuspiciousSTAMaxSignalStrength_Object = MibTableColumn
qtechDot11WIDSSuspiciousSTAMaxSignalStrength = _QtechDot11WIDSSuspiciousSTAMaxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 1, 1, 20),
    _QtechDot11WIDSSuspiciousSTAMaxSignalStrength_Type()
)
qtechDot11WIDSSuspiciousSTAMaxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSSuspiciousSTAMaxSignalStrength.setStatus("current")
_QtechDot11WIDSSuspiciousSTAUsingChannel_Type = Integer32
_QtechDot11WIDSSuspiciousSTAUsingChannel_Object = MibTableColumn
qtechDot11WIDSSuspiciousSTAUsingChannel = _QtechDot11WIDSSuspiciousSTAUsingChannel_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 1, 1, 21),
    _QtechDot11WIDSSuspiciousSTAUsingChannel_Type()
)
qtechDot11WIDSSuspiciousSTAUsingChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSSuspiciousSTAUsingChannel.setStatus("current")
_QtechDot11WIDSSuspiciousSTAWorksInAdhocMode_Type = TruthValue
_QtechDot11WIDSSuspiciousSTAWorksInAdhocMode_Object = MibTableColumn
qtechDot11WIDSSuspiciousSTAWorksInAdhocMode = _QtechDot11WIDSSuspiciousSTAWorksInAdhocMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 1, 1, 22),
    _QtechDot11WIDSSuspiciousSTAWorksInAdhocMode_Type()
)
qtechDot11WIDSSuspiciousSTAWorksInAdhocMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSSuspiciousSTAWorksInAdhocMode.setStatus("current")
_QtechDot11WIDSSuspiciousSTANeedsDealingTag_Type = TruthValue
_QtechDot11WIDSSuspiciousSTANeedsDealingTag_Object = MibTableColumn
qtechDot11WIDSSuspiciousSTANeedsDealingTag = _QtechDot11WIDSSuspiciousSTANeedsDealingTag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 1, 1, 23),
    _QtechDot11WIDSSuspiciousSTANeedsDealingTag_Type()
)
qtechDot11WIDSSuspiciousSTANeedsDealingTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSSuspiciousSTANeedsDealingTag.setStatus("current")
_QtechDot11WIDSSuspiciousSTAIgnoredTag_Type = TruthValue
_QtechDot11WIDSSuspiciousSTAIgnoredTag_Object = MibTableColumn
qtechDot11WIDSSuspiciousSTAIgnoredTag = _QtechDot11WIDSSuspiciousSTAIgnoredTag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 1, 1, 24),
    _QtechDot11WIDSSuspiciousSTAIgnoredTag_Type()
)
qtechDot11WIDSSuspiciousSTAIgnoredTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSSuspiciousSTAIgnoredTag.setStatus("current")
_QtechDot11WIDSFloodAttackDetectSwitch_Type = TruthValue
_QtechDot11WIDSFloodAttackDetectSwitch_Object = MibTableColumn
qtechDot11WIDSFloodAttackDetectSwitch = _QtechDot11WIDSFloodAttackDetectSwitch_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 1, 1, 25),
    _QtechDot11WIDSFloodAttackDetectSwitch_Type()
)
qtechDot11WIDSFloodAttackDetectSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSFloodAttackDetectSwitch.setStatus("current")
_QtechDot11WIDSSpoofAttackDetectSwitch_Type = TruthValue
_QtechDot11WIDSSpoofAttackDetectSwitch_Object = MibTableColumn
qtechDot11WIDSSpoofAttackDetectSwitch = _QtechDot11WIDSSpoofAttackDetectSwitch_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 1, 1, 26),
    _QtechDot11WIDSSpoofAttackDetectSwitch_Type()
)
qtechDot11WIDSSpoofAttackDetectSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSSpoofAttackDetectSwitch.setStatus("current")
_QtechDot11WIDSWeakIVDetectSwitch_Type = TruthValue
_QtechDot11WIDSWeakIVDetectSwitch_Object = MibTableColumn
qtechDot11WIDSWeakIVDetectSwitch = _QtechDot11WIDSWeakIVDetectSwitch_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 1, 1, 27),
    _QtechDot11WIDSWeakIVDetectSwitch_Type()
)
qtechDot11WIDSWeakIVDetectSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSWeakIVDetectSwitch.setStatus("current")
_QtechDot11WIDSClearIllegalEquipmentHistroyTag_Type = TruthValue
_QtechDot11WIDSClearIllegalEquipmentHistroyTag_Object = MibTableColumn
qtechDot11WIDSClearIllegalEquipmentHistroyTag = _QtechDot11WIDSClearIllegalEquipmentHistroyTag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 1, 1, 28),
    _QtechDot11WIDSClearIllegalEquipmentHistroyTag_Type()
)
qtechDot11WIDSClearIllegalEquipmentHistroyTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSClearIllegalEquipmentHistroyTag.setStatus("current")
_QtechDot11WIDSClearAttackDetectionHistroyTag_Type = TruthValue
_QtechDot11WIDSClearAttackDetectionHistroyTag_Object = MibTableColumn
qtechDot11WIDSClearAttackDetectionHistroyTag = _QtechDot11WIDSClearAttackDetectionHistroyTag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 1, 1, 29),
    _QtechDot11WIDSClearAttackDetectionHistroyTag_Type()
)
qtechDot11WIDSClearAttackDetectionHistroyTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSClearAttackDetectionHistroyTag.setStatus("current")
_QtechDot11WIDSClearAttackDetectionStaticsTag_Type = TruthValue
_QtechDot11WIDSClearAttackDetectionStaticsTag_Object = MibTableColumn
qtechDot11WIDSClearAttackDetectionStaticsTag = _QtechDot11WIDSClearAttackDetectionStaticsTag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 1, 1, 30),
    _QtechDot11WIDSClearAttackDetectionStaticsTag_Type()
)
qtechDot11WIDSClearAttackDetectionStaticsTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSClearAttackDetectionStaticsTag.setStatus("current")
_QtechDot11LawlessApInfoTable_Object = MibTable
qtechDot11LawlessApInfoTable = _QtechDot11LawlessApInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 2)
)
if mibBuilder.loadTexts:
    qtechDot11LawlessApInfoTable.setStatus("current")
_QtechDot11LawlessApInfoTableEntry_Object = MibTableRow
qtechDot11LawlessApInfoTableEntry = _QtechDot11LawlessApInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 2, 1)
)
qtechDot11LawlessApInfoTableEntry.setIndexNames(
    (0, "QTECH-WLAN-FIT-AP-IN-MIB", "qtechLawlessAPIndex"),
)
if mibBuilder.loadTexts:
    qtechDot11LawlessApInfoTableEntry.setStatus("current")
_QtechLawlessAPIndex_Type = Integer32
_QtechLawlessAPIndex_Object = MibTableColumn
qtechLawlessAPIndex = _QtechLawlessAPIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 2, 1, 1),
    _QtechLawlessAPIndex_Type()
)
qtechLawlessAPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechLawlessAPIndex.setStatus("current")
_QtechLawlessAPSignalStrength_Type = Integer32
_QtechLawlessAPSignalStrength_Object = MibTableColumn
qtechLawlessAPSignalStrength = _QtechLawlessAPSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 2, 1, 2),
    _QtechLawlessAPSignalStrength_Type()
)
qtechLawlessAPSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLawlessAPSignalStrength.setStatus("current")
_QtechLawlessAPSignalSNR_Type = Integer32
_QtechLawlessAPSignalSNR_Object = MibTableColumn
qtechLawlessAPSignalSNR = _QtechLawlessAPSignalSNR_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 2, 1, 3),
    _QtechLawlessAPSignalSNR_Type()
)
qtechLawlessAPSignalSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLawlessAPSignalSNR.setStatus("current")
_QtechLawlessAPChannelNum_Type = Integer32
_QtechLawlessAPChannelNum_Object = MibTableColumn
qtechLawlessAPChannelNum = _QtechLawlessAPChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 2, 1, 4),
    _QtechLawlessAPChannelNum_Type()
)
qtechLawlessAPChannelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLawlessAPChannelNum.setStatus("current")
_QtechLawlessAPSSIDName_Type = DisplayString
_QtechLawlessAPSSIDName_Object = MibTableColumn
qtechLawlessAPSSIDName = _QtechLawlessAPSSIDName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 2, 1, 5),
    _QtechLawlessAPSSIDName_Type()
)
qtechLawlessAPSSIDName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLawlessAPSSIDName.setStatus("current")
_QtechLawlessAPMacaddr_Type = MacAddress
_QtechLawlessAPMacaddr_Object = MibTableColumn
qtechLawlessAPMacaddr = _QtechLawlessAPMacaddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 2, 1, 6),
    _QtechLawlessAPMacaddr_Type()
)
qtechLawlessAPMacaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLawlessAPMacaddr.setStatus("current")
_QtechLawlessAPTreatMode_Type = Integer32
_QtechLawlessAPTreatMode_Object = MibTableColumn
qtechLawlessAPTreatMode = _QtechLawlessAPTreatMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 2, 1, 7),
    _QtechLawlessAPTreatMode_Type()
)
qtechLawlessAPTreatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLawlessAPTreatMode.setStatus("current")
_QtechDot11UndefinedApInfoTable_Object = MibTable
qtechDot11UndefinedApInfoTable = _QtechDot11UndefinedApInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 3)
)
if mibBuilder.loadTexts:
    qtechDot11UndefinedApInfoTable.setStatus("current")
_QtechDot11UndefinedApInfoTableEntry_Object = MibTableRow
qtechDot11UndefinedApInfoTableEntry = _QtechDot11UndefinedApInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 3, 1)
)
qtechDot11UndefinedApInfoTableEntry.setIndexNames(
    (0, "QTECH-WLAN-FIT-AP-IN-MIB", "qtechUndefinedAPIndex"),
)
if mibBuilder.loadTexts:
    qtechDot11UndefinedApInfoTableEntry.setStatus("current")
_QtechUndefinedAPIndex_Type = Integer32
_QtechUndefinedAPIndex_Object = MibTableColumn
qtechUndefinedAPIndex = _QtechUndefinedAPIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 3, 1, 1),
    _QtechUndefinedAPIndex_Type()
)
qtechUndefinedAPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechUndefinedAPIndex.setStatus("current")
_QtechUndefinedAPSignalStrength_Type = Integer32
_QtechUndefinedAPSignalStrength_Object = MibTableColumn
qtechUndefinedAPSignalStrength = _QtechUndefinedAPSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 3, 1, 2),
    _QtechUndefinedAPSignalStrength_Type()
)
qtechUndefinedAPSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechUndefinedAPSignalStrength.setStatus("current")
_QtechUndefinedAPSignalSNR_Type = Integer32
_QtechUndefinedAPSignalSNR_Object = MibTableColumn
qtechUndefinedAPSignalSNR = _QtechUndefinedAPSignalSNR_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 3, 1, 3),
    _QtechUndefinedAPSignalSNR_Type()
)
qtechUndefinedAPSignalSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechUndefinedAPSignalSNR.setStatus("current")
_QtechUndefinedAPChannelNum_Type = Integer32
_QtechUndefinedAPChannelNum_Object = MibTableColumn
qtechUndefinedAPChannelNum = _QtechUndefinedAPChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 3, 1, 4),
    _QtechUndefinedAPChannelNum_Type()
)
qtechUndefinedAPChannelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechUndefinedAPChannelNum.setStatus("current")
_QtechUndefinedAPSSIDName_Type = DisplayString
_QtechUndefinedAPSSIDName_Object = MibTableColumn
qtechUndefinedAPSSIDName = _QtechUndefinedAPSSIDName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 3, 1, 5),
    _QtechUndefinedAPSSIDName_Type()
)
qtechUndefinedAPSSIDName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechUndefinedAPSSIDName.setStatus("current")
_QtechUndefinedAPMacaddr_Type = MacAddress
_QtechUndefinedAPMacaddr_Object = MibTableColumn
qtechUndefinedAPMacaddr = _QtechUndefinedAPMacaddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 3, 1, 6),
    _QtechUndefinedAPMacaddr_Type()
)
qtechUndefinedAPMacaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechUndefinedAPMacaddr.setStatus("current")
_QtechUndefinedAPTreatMode_Type = Integer32
_QtechUndefinedAPTreatMode_Object = MibTableColumn
qtechUndefinedAPTreatMode = _QtechUndefinedAPTreatMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 3, 1, 7),
    _QtechUndefinedAPTreatMode_Type()
)
qtechUndefinedAPTreatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechUndefinedAPTreatMode.setStatus("current")
_QtechDot11LegalityApInfoTable_Object = MibTable
qtechDot11LegalityApInfoTable = _QtechDot11LegalityApInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 4)
)
if mibBuilder.loadTexts:
    qtechDot11LegalityApInfoTable.setStatus("current")
_QtechDot11LegalityApInfoTableEntry_Object = MibTableRow
qtechDot11LegalityApInfoTableEntry = _QtechDot11LegalityApInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 4, 1)
)
qtechDot11LegalityApInfoTableEntry.setIndexNames(
    (0, "QTECH-WLAN-FIT-AP-IN-MIB", "qtechLegalityAPIndex"),
)
if mibBuilder.loadTexts:
    qtechDot11LegalityApInfoTableEntry.setStatus("current")
_QtechLegalityAPIndex_Type = Integer32
_QtechLegalityAPIndex_Object = MibTableColumn
qtechLegalityAPIndex = _QtechLegalityAPIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 4, 1, 1),
    _QtechLegalityAPIndex_Type()
)
qtechLegalityAPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechLegalityAPIndex.setStatus("current")
_QtechLegalityAPSignalStrength_Type = Integer32
_QtechLegalityAPSignalStrength_Object = MibTableColumn
qtechLegalityAPSignalStrength = _QtechLegalityAPSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 4, 1, 2),
    _QtechLegalityAPSignalStrength_Type()
)
qtechLegalityAPSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLegalityAPSignalStrength.setStatus("current")
_QtechLegalityAPSignalSNR_Type = Integer32
_QtechLegalityAPSignalSNR_Object = MibTableColumn
qtechLegalityAPSignalSNR = _QtechLegalityAPSignalSNR_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 4, 1, 3),
    _QtechLegalityAPSignalSNR_Type()
)
qtechLegalityAPSignalSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLegalityAPSignalSNR.setStatus("current")
_QtechLegalityAPChannelNum_Type = Integer32
_QtechLegalityAPChannelNum_Object = MibTableColumn
qtechLegalityAPChannelNum = _QtechLegalityAPChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 4, 1, 4),
    _QtechLegalityAPChannelNum_Type()
)
qtechLegalityAPChannelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLegalityAPChannelNum.setStatus("current")
_QtechLegalityAPSSIDName_Type = DisplayString
_QtechLegalityAPSSIDName_Object = MibTableColumn
qtechLegalityAPSSIDName = _QtechLegalityAPSSIDName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 4, 1, 5),
    _QtechLegalityAPSSIDName_Type()
)
qtechLegalityAPSSIDName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLegalityAPSSIDName.setStatus("current")
_QtechLegalityAPMacaddr_Type = MacAddress
_QtechLegalityAPMacaddr_Object = MibTableColumn
qtechLegalityAPMacaddr = _QtechLegalityAPMacaddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 4, 1, 6),
    _QtechLegalityAPMacaddr_Type()
)
qtechLegalityAPMacaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLegalityAPMacaddr.setStatus("current")
_QtechLegalityAPTreatMode_Type = Integer32
_QtechLegalityAPTreatMode_Object = MibTableColumn
qtechLegalityAPTreatMode = _QtechLegalityAPTreatMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 8, 4, 1, 7),
    _QtechLegalityAPTreatMode_Type()
)
qtechLegalityAPTreatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLegalityAPTreatMode.setStatus("current")
_QtechAlarmTrapsObjects_ObjectIdentity = ObjectIdentity
qtechAlarmTrapsObjects = _QtechAlarmTrapsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 10)
)


class _QtechWIDSSuspiciousType_Type(DisplayString):
    """Custom type qtechWIDSSuspiciousType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_QtechWIDSSuspiciousType_Type.__name__ = "DisplayString"
_QtechWIDSSuspiciousType_Object = MibScalar
qtechWIDSSuspiciousType = _QtechWIDSSuspiciousType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 10, 1),
    _QtechWIDSSuspiciousType_Type()
)
qtechWIDSSuspiciousType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWIDSSuspiciousType.setStatus("current")
_QtechWIDSSuspiciousDeviceMac_Type = MacAddress
_QtechWIDSSuspiciousDeviceMac_Object = MibScalar
qtechWIDSSuspiciousDeviceMac = _QtechWIDSSuspiciousDeviceMac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 10, 2),
    _QtechWIDSSuspiciousDeviceMac_Type()
)
qtechWIDSSuspiciousDeviceMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWIDSSuspiciousDeviceMac.setStatus("current")


class _QtechWIDSSuspiciousDeviceExtensionInfo_Type(DisplayString):
    """Custom type qtechWIDSSuspiciousDeviceExtensionInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_QtechWIDSSuspiciousDeviceExtensionInfo_Type.__name__ = "DisplayString"
_QtechWIDSSuspiciousDeviceExtensionInfo_Object = MibScalar
qtechWIDSSuspiciousDeviceExtensionInfo = _QtechWIDSSuspiciousDeviceExtensionInfo_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 10, 3),
    _QtechWIDSSuspiciousDeviceExtensionInfo_Type()
)
qtechWIDSSuspiciousDeviceExtensionInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWIDSSuspiciousDeviceExtensionInfo.setStatus("current")


class _QtechAPCurrentPMMode_Type(DisplayString):
    """Custom type qtechAPCurrentPMMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_QtechAPCurrentPMMode_Type.__name__ = "DisplayString"
_QtechAPCurrentPMMode_Object = MibScalar
qtechAPCurrentPMMode = _QtechAPCurrentPMMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 10, 4),
    _QtechAPCurrentPMMode_Type()
)
qtechAPCurrentPMMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAPCurrentPMMode.setStatus("current")
_QtechChgWorkModeAPMac_Type = MacAddress
_QtechChgWorkModeAPMac_Object = MibScalar
qtechChgWorkModeAPMac = _QtechChgWorkModeAPMac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 10, 7),
    _QtechChgWorkModeAPMac_Type()
)
qtechChgWorkModeAPMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechChgWorkModeAPMac.setStatus("current")


class _QtechAttackType_Type(DisplayString):
    """Custom type qtechAttackType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_QtechAttackType_Type.__name__ = "DisplayString"
_QtechAttackType_Object = MibScalar
qtechAttackType = _QtechAttackType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 10, 8),
    _QtechAttackType_Type()
)
qtechAttackType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAttackType.setStatus("current")
_QtechAttackCilentIP_Type = IpAddress
_QtechAttackCilentIP_Object = MibScalar
qtechAttackCilentIP = _QtechAttackCilentIP_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 10, 9),
    _QtechAttackCilentIP_Type()
)
qtechAttackCilentIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAttackCilentIP.setStatus("current")


class _QtechAttackCilentExternInfo_Type(DisplayString):
    """Custom type qtechAttackCilentExternInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_QtechAttackCilentExternInfo_Type.__name__ = "DisplayString"
_QtechAttackCilentExternInfo_Object = MibScalar
qtechAttackCilentExternInfo = _QtechAttackCilentExternInfo_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 10, 10),
    _QtechAttackCilentExternInfo_Type()
)
qtechAttackCilentExternInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAttackCilentExternInfo.setStatus("current")

# Managed Objects groups


# Notification objects

qtechWIDSIllegalAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 0, 1)
)
qtechWIDSIllegalAlarmTrap.setObjects(
      *(("QTECH-WLAN-FIT-AP-IN-MIB", "qtechWIDSSuspiciousType"),
        ("QTECH-WLAN-FIT-AP-IN-MIB", "qtechWIDSSuspiciousDeviceMac"),
        ("QTECH-WLAN-FIT-AP-IN-MIB", "qtechWIDSSuspiciousDeviceExtensionInfo"))
)
if mibBuilder.loadTexts:
    qtechWIDSIllegalAlarmTrap.setStatus(
        "current"
    )

qtechTelMtWorkModeChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 0, 2)
)
qtechTelMtWorkModeChgTrap.setObjects(
      *(("QTECH-WLAN-FIT-AP-IN-MIB", "qtechAPCurrentPMMode"),
        ("QTECH-WLAN-FIT-AP-IN-MIB", "qtechChgWorkModeAPMac"))
)
if mibBuilder.loadTexts:
    qtechTelMtWorkModeChgTrap.setStatus(
        "current"
    )

qtechAttackAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 83, 0, 4)
)
qtechAttackAlarm.setObjects(
      *(("QTECH-WLAN-FIT-AP-IN-MIB", "qtechAttackType"),
        ("QTECH-WLAN-FIT-AP-IN-MIB", "qtechAttackCilentIP"),
        ("QTECH-WLAN-FIT-AP-IN-MIB", "qtechAttackCilentExternInfo"))
)
if mibBuilder.loadTexts:
    qtechAttackAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-WLAN-FIT-AP-IN-MIB",
    **{"qtechFitApMibModule": qtechFitApMibModule,
       "qtechAlarmTraps": qtechAlarmTraps,
       "qtechWIDSIllegalAlarmTrap": qtechWIDSIllegalAlarmTrap,
       "qtechTelMtWorkModeChgTrap": qtechTelMtWorkModeChgTrap,
       "qtechAttackAlarm": qtechAttackAlarm,
       "qtechSystemInfoConfigObjects": qtechSystemInfoConfigObjects,
       "qtechDomain": qtechDomain,
       "qtechPhySeparatedEnable": qtechPhySeparatedEnable,
       "qtechForfendDosAttackEnable": qtechForfendDosAttackEnable,
       "qtechAcTrafficLoadBalancing": qtechAcTrafficLoadBalancing,
       "qtechAcTrafficLoadBalanceThreshold": qtechAcTrafficLoadBalanceThreshold,
       "qtechAcTrafficOtherAPThresholdValue": qtechAcTrafficOtherAPThresholdValue,
       "qtechAcAPWIDSScanningMode": qtechAcAPWIDSScanningMode,
       "qtechAcAPLegitimateMode": qtechAcAPLegitimateMode,
       "qtechAcAPTreatMode": qtechAcAPTreatMode,
       "qtechAcAssociationFailureTotalTimes": qtechAcAssociationFailureTotalTimes,
       "qtechAcAirIfRxTotalDataFrams": qtechAcAirIfRxTotalDataFrams,
       "qtechAcAirIfTxTotalDataFrams": qtechAcAirIfTxTotalDataFrams,
       "qtechAcAirIfTxTotalLostFrams": qtechAcAirIfTxTotalLostFrams,
       "qtechAcAirIfTxAssociateFrams": qtechAcAirIfTxAssociateFrams,
       "qtechAcAirIfRxAssociateFrams": qtechAcAirIfRxAssociateFrams,
       "qtechAcAirIfBeaconTotalFrams": qtechAcAirIfBeaconTotalFrams,
       "qtechAcAirIfRxTotalDataBytes": qtechAcAirIfRxTotalDataBytes,
       "qtechAcAirIfTxTotalDataBytes": qtechAcAirIfTxTotalDataBytes,
       "qtechAcAirRxFlux": qtechAcAirRxFlux,
       "qtechAcAirTxFlux": qtechAcAirTxFlux,
       "qtechInfoConfigObjects": qtechInfoConfigObjects,
       "qtechInfoConfigTable": qtechInfoConfigTable,
       "qtechInfoConfigTableEntry": qtechInfoConfigTableEntry,
       "qtechAcAPWIDSWorkMode": qtechAcAPWIDSWorkMode,
       "qtechStationConfigObjects": qtechStationConfigObjects,
       "qtechConfigStaInfoTable": qtechConfigStaInfoTable,
       "qtechConfigStaInfoTableEntry": qtechConfigStaInfoTableEntry,
       "qtechACconfigAPBandwith": qtechACconfigAPBandwith,
       "qtechAirIfStatisticsObjects": qtechAirIfStatisticsObjects,
       "qtechAirIfInfoStatisticsTable": qtechAirIfInfoStatisticsTable,
       "qtechAirIfInfoStatisticsTableEntry": qtechAirIfInfoStatisticsTableEntry,
       "qtechRxTotalDataFrams": qtechRxTotalDataFrams,
       "qtechTxTotalDataFrams": qtechTxTotalDataFrams,
       "qtechTxLostDataFrams": qtechTxLostDataFrams,
       "qtechTxAssociateFrams": qtechTxAssociateFrams,
       "qtechRxAssociateFrams": qtechRxAssociateFrams,
       "qtechBeaconFrams": qtechBeaconFrams,
       "qtechRxTotalDataBytes": qtechRxTotalDataBytes,
       "qtechTxTotalDataBytes": qtechTxTotalDataBytes,
       "qtechRESUtilization": qtechRESUtilization,
       "qtechAirIfTxResendDataTable": qtechAirIfTxResendDataTable,
       "qtechAirIfTxResendDataTableEntry": qtechAirIfTxResendDataTableEntry,
       "qtechStaResendDataFrams": qtechStaResendDataFrams,
       "qtechTermServiceStatistics": qtechTermServiceStatistics,
       "qtechTermServiceStatisticsWithSSID": qtechTermServiceStatisticsWithSSID,
       "qtechTermServiceStaticWithSSIDTable": qtechTermServiceStaticWithSSIDTable,
       "qtechTermServiceStaticWithSSIDTableEntry": qtechTermServiceStaticWithSSIDTableEntry,
       "qtechTotalUserNum": qtechTotalUserNum,
       "qtechCurrentUserNum": qtechCurrentUserNum,
       "qtechStaReqAccessTimes": qtechStaReqAccessTimes,
       "qtechRspStaAccessReqTimes": qtechRspStaAccessReqTimes,
       "qtechStaAccessSucessTimes": qtechStaAccessSucessTimes,
       "qtechIneffiLinkVerifyFailTime": qtechIneffiLinkVerifyFailTime,
       "qtechTimeoutLinkVerifyFailTime": qtechTimeoutLinkVerifyFailTime,
       "qtechInefficiencyLinkVerifyFailTime": qtechInefficiencyLinkVerifyFailTime,
       "qtechOtherReasonLinkVerifyFailTime": qtechOtherReasonLinkVerifyFailTime,
       "qtechIneffiAssociationFailTime": qtechIneffiAssociationFailTime,
       "qtechTimeoutAssociationFailTime": qtechTimeoutAssociationFailTime,
       "qtechInefficiencyAssociationFailTime": qtechInefficiencyAssociationFailTime,
       "qtechOtherReasonAssociationFailTime": qtechOtherReasonAssociationFailTime,
       "qtechTotalReassociationAtmptTimes": qtechTotalReassociationAtmptTimes,
       "qtechTotalReassociationSuccessTimes": qtechTotalReassociationSuccessTimes,
       "qtechIneffiReassociationFailTime": qtechIneffiReassociationFailTime,
       "qtechTimeoutReassociationFailTime": qtechTimeoutReassociationFailTime,
       "qtechInefficiencyReassociationFailTime": qtechInefficiencyReassociationFailTime,
       "qtechOtherReasonReassociationFailTime": qtechOtherReasonReassociationFailTime,
       "qtechTotalIdentificationAtmptTimes": qtechTotalIdentificationAtmptTimes,
       "qtechTotalIdentificationSuccessTimes": qtechTotalIdentificationSuccessTimes,
       "qtechPwdErrorIdentifyFailTime": qtechPwdErrorIdentifyFailTime,
       "qtechIneffiIdentificationFailTime": qtechIneffiIdentificationFailTime,
       "qtechTimeoutIdentificationFailTime": qtechTimeoutIdentificationFailTime,
       "qtechInefficiencyIdentificationFailTime": qtechInefficiencyIdentificationFailTime,
       "qtechOtherReasonIdentificationFailTime": qtechOtherReasonIdentificationFailTime,
       "qtechTotalRemoveLinkVerifyFailTimes": qtechTotalRemoveLinkVerifyFailTimes,
       "qtechLeaveAPCoverageRemoveLinkVerifyFailTimes": qtechLeaveAPCoverageRemoveLinkVerifyFailTimes,
       "qtechInefficiencyRemoveLinkVerifyFailTime": qtechInefficiencyRemoveLinkVerifyFailTime,
       "qtechLinkVerifyFailRemoveLinkVerifyFailTime": qtechLinkVerifyFailRemoveLinkVerifyFailTime,
       "qtechOtherReasonRemoveLinkVerifyFailTime": qtechOtherReasonRemoveLinkVerifyFailTime,
       "qtechTotalRemoveLinkAssociationTimes": qtechTotalRemoveLinkAssociationTimes,
       "qtechLeaveAPCoverageRemoveAssociationFailTimes": qtechLeaveAPCoverageRemoveAssociationFailTimes,
       "qtechInefficiencyRemoveAssociationFailTime": qtechInefficiencyRemoveAssociationFailTime,
       "qtechAssociationFailRemoveAssociationFailTime": qtechAssociationFailRemoveAssociationFailTime,
       "qtechOtherReasonRemoveAssociationFailTime": qtechOtherReasonRemoveAssociationFailTime,
       "qtechTermServiceStatisticsWithAP": qtechTermServiceStatisticsWithAP,
       "qtechTermServiceStaticWithAPTable": qtechTermServiceStaticWithAPTable,
       "qtechTermServiceStaticWithAPTableEntry": qtechTermServiceStaticWithAPTableEntry,
       "qtechUserAccumulateTime": qtechUserAccumulateTime,
       "qtechAssociaFailTimes": qtechAssociaFailTimes,
       "qtechTermServiceSTatisticsWithStation": qtechTermServiceSTatisticsWithStation,
       "qtechTermServiceStationWithStationTable": qtechTermServiceStationWithStationTable,
       "qtechTermServiceStationWithStationTableEntry": qtechTermServiceStationWithStationTableEntry,
       "qtechStaAssociateTime": qtechStaAssociateTime,
       "qtechRxStaDataFrams": qtechRxStaDataFrams,
       "qtechRXStaErrorFrams": qtechRXStaErrorFrams,
       "qtechTxStaDataFrams": qtechTxStaDataFrams,
       "qtechReSendDataFrams": qtechReSendDataFrams,
       "qtechStaRxAvgSpeed": qtechStaRxAvgSpeed,
       "qtechStaTxAvgSpeed": qtechStaTxAvgSpeed,
       "qtechStaThroughput": qtechStaThroughput,
       "qtechStaSignalStrength": qtechStaSignalStrength,
       "qtechStaSignalNoise": qtechStaSignalNoise,
       "qtechDOT11WIDSParamObjects": qtechDOT11WIDSParamObjects,
       "qtechDot11WIDSInfoTable": qtechDot11WIDSInfoTable,
       "qtechDot11WIDSInfoEntry": qtechDot11WIDSInfoEntry,
       "qtechDot11WIDSLocalIndex": qtechDot11WIDSLocalIndex,
       "qtechDot11WIDSpermittedSSID": qtechDot11WIDSpermittedSSID,
       "qtechDot11WIDSpermitBSSID": qtechDot11WIDSpermitBSSID,
       "qtechDot11WIDSDeviceOUI": qtechDot11WIDSDeviceOUI,
       "qtechDot11WIDSSuspiciousAPBSS": qtechDot11WIDSSuspiciousAPBSS,
       "qtechDot11WIDSSuspiciousAPCount": qtechDot11WIDSSuspiciousAPCount,
       "qtechDot11WIDSMomentFirstTimeDetectedSusAP": qtechDot11WIDSMomentFirstTimeDetectedSusAP,
       "qtechDot11WIDSMomentLastTimeDetectedSusAP": qtechDot11WIDSMomentLastTimeDetectedSusAP,
       "qtechDot11WIDSSuspiciousAPSSID": qtechDot11WIDSSuspiciousAPSSID,
       "qtechDot11WIDSSuspiciousAPMaxSignalStrength": qtechDot11WIDSSuspiciousAPMaxSignalStrength,
       "qtechDot11WIDSSuspiciousAPUsingChannel": qtechDot11WIDSSuspiciousAPUsingChannel,
       "qtechDot11WIDSSuspiciousAPFrameEncrption": qtechDot11WIDSSuspiciousAPFrameEncrption,
       "qtechDot11WIDSSuspiciousAPNeedsDealingTag": qtechDot11WIDSSuspiciousAPNeedsDealingTag,
       "qtechDot11WIDSSuspiciousAPIgnoredTag": qtechDot11WIDSSuspiciousAPIgnoredTag,
       "qtechDot11WIDSSuspiciousSTAMAC": qtechDot11WIDSSuspiciousSTAMAC,
       "qtechDot11WIDSAPCountDetectingSuspiciousSTA": qtechDot11WIDSAPCountDetectingSuspiciousSTA,
       "qtechDot11WIDSMomentFirstTimeDetectedSusSTA": qtechDot11WIDSMomentFirstTimeDetectedSusSTA,
       "qtechDot11WIDSMomentLastTimeDetectedSusSTA": qtechDot11WIDSMomentLastTimeDetectedSusSTA,
       "qtechDot11WIDSBSSIDSuspiciousSTAAccessing": qtechDot11WIDSBSSIDSuspiciousSTAAccessing,
       "qtechDot11WIDSSuspiciousSTAMaxSignalStrength": qtechDot11WIDSSuspiciousSTAMaxSignalStrength,
       "qtechDot11WIDSSuspiciousSTAUsingChannel": qtechDot11WIDSSuspiciousSTAUsingChannel,
       "qtechDot11WIDSSuspiciousSTAWorksInAdhocMode": qtechDot11WIDSSuspiciousSTAWorksInAdhocMode,
       "qtechDot11WIDSSuspiciousSTANeedsDealingTag": qtechDot11WIDSSuspiciousSTANeedsDealingTag,
       "qtechDot11WIDSSuspiciousSTAIgnoredTag": qtechDot11WIDSSuspiciousSTAIgnoredTag,
       "qtechDot11WIDSFloodAttackDetectSwitch": qtechDot11WIDSFloodAttackDetectSwitch,
       "qtechDot11WIDSSpoofAttackDetectSwitch": qtechDot11WIDSSpoofAttackDetectSwitch,
       "qtechDot11WIDSWeakIVDetectSwitch": qtechDot11WIDSWeakIVDetectSwitch,
       "qtechDot11WIDSClearIllegalEquipmentHistroyTag": qtechDot11WIDSClearIllegalEquipmentHistroyTag,
       "qtechDot11WIDSClearAttackDetectionHistroyTag": qtechDot11WIDSClearAttackDetectionHistroyTag,
       "qtechDot11WIDSClearAttackDetectionStaticsTag": qtechDot11WIDSClearAttackDetectionStaticsTag,
       "qtechDot11LawlessApInfoTable": qtechDot11LawlessApInfoTable,
       "qtechDot11LawlessApInfoTableEntry": qtechDot11LawlessApInfoTableEntry,
       "qtechLawlessAPIndex": qtechLawlessAPIndex,
       "qtechLawlessAPSignalStrength": qtechLawlessAPSignalStrength,
       "qtechLawlessAPSignalSNR": qtechLawlessAPSignalSNR,
       "qtechLawlessAPChannelNum": qtechLawlessAPChannelNum,
       "qtechLawlessAPSSIDName": qtechLawlessAPSSIDName,
       "qtechLawlessAPMacaddr": qtechLawlessAPMacaddr,
       "qtechLawlessAPTreatMode": qtechLawlessAPTreatMode,
       "qtechDot11UndefinedApInfoTable": qtechDot11UndefinedApInfoTable,
       "qtechDot11UndefinedApInfoTableEntry": qtechDot11UndefinedApInfoTableEntry,
       "qtechUndefinedAPIndex": qtechUndefinedAPIndex,
       "qtechUndefinedAPSignalStrength": qtechUndefinedAPSignalStrength,
       "qtechUndefinedAPSignalSNR": qtechUndefinedAPSignalSNR,
       "qtechUndefinedAPChannelNum": qtechUndefinedAPChannelNum,
       "qtechUndefinedAPSSIDName": qtechUndefinedAPSSIDName,
       "qtechUndefinedAPMacaddr": qtechUndefinedAPMacaddr,
       "qtechUndefinedAPTreatMode": qtechUndefinedAPTreatMode,
       "qtechDot11LegalityApInfoTable": qtechDot11LegalityApInfoTable,
       "qtechDot11LegalityApInfoTableEntry": qtechDot11LegalityApInfoTableEntry,
       "qtechLegalityAPIndex": qtechLegalityAPIndex,
       "qtechLegalityAPSignalStrength": qtechLegalityAPSignalStrength,
       "qtechLegalityAPSignalSNR": qtechLegalityAPSignalSNR,
       "qtechLegalityAPChannelNum": qtechLegalityAPChannelNum,
       "qtechLegalityAPSSIDName": qtechLegalityAPSSIDName,
       "qtechLegalityAPMacaddr": qtechLegalityAPMacaddr,
       "qtechLegalityAPTreatMode": qtechLegalityAPTreatMode,
       "qtechAlarmTrapsObjects": qtechAlarmTrapsObjects,
       "qtechWIDSSuspiciousType": qtechWIDSSuspiciousType,
       "qtechWIDSSuspiciousDeviceMac": qtechWIDSSuspiciousDeviceMac,
       "qtechWIDSSuspiciousDeviceExtensionInfo": qtechWIDSSuspiciousDeviceExtensionInfo,
       "qtechAPCurrentPMMode": qtechAPCurrentPMMode,
       "qtechChgWorkModeAPMac": qtechChgWorkModeAPMac,
       "qtechAttackType": qtechAttackType,
       "qtechAttackCilentIP": qtechAttackCilentIP,
       "qtechAttackCilentExternInfo": qtechAttackCilentExternInfo}
)
