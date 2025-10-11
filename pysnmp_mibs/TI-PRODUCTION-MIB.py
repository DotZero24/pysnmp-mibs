# SNMP MIB module (TI-PRODUCTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/arris/TI-PRODUCTION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:10:12 2025
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

(DocsisUpstreamType,) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "DocsisUpstreamType")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(eqName,) = mibBuilder.importSymbols(
    "TI-MANUFACTURER-MIB",
    "eqName")


# MODULE-IDENTITY

modemProduction = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ModemProdCmSetup_ObjectIdentity = ObjectIdentity
modemProdCmSetup = _ModemProdCmSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1)
)
_ModemProdCmPermanentSetup_ObjectIdentity = ObjectIdentity
modemProdCmPermanentSetup = _ModemProdCmPermanentSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 1)
)
_ModemProdCmCertServerIp_Type = IpAddress
_ModemProdCmCertServerIp_Object = MibScalar
modemProdCmCertServerIp = _ModemProdCmCertServerIp_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 1, 1),
    _ModemProdCmCertServerIp_Type()
)
modemProdCmCertServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProdCmCertServerIp.setStatus("current")


class _ModemProdCmCertFileName_Type(DisplayString):
    """Custom type modemProdCmCertFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ModemProdCmCertFileName_Type.__name__ = "DisplayString"
_ModemProdCmCertFileName_Object = MibScalar
modemProdCmCertFileName = _ModemProdCmCertFileName_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 1, 2),
    _ModemProdCmCertFileName_Type()
)
modemProdCmCertFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProdCmCertFileName.setStatus("current")


class _ModemProdCmCertKeyFileName_Type(DisplayString):
    """Custom type modemProdCmCertKeyFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ModemProdCmCertKeyFileName_Type.__name__ = "DisplayString"
_ModemProdCmCertKeyFileName_Object = MibScalar
modemProdCmCertKeyFileName = _ModemProdCmCertKeyFileName_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 1, 3),
    _ModemProdCmCertKeyFileName_Type()
)
modemProdCmCertKeyFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProdCmCertKeyFileName.setStatus("current")


class _ModemProdCmCertFrequencyPlan_Type(Integer32):
    """Custom type modemProdCmCertFrequencyPlan based on Integer32"""
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
          ("northAmerican", 1),
          ("european", 2),
          ("japanese", 3))
    )


_ModemProdCmCertFrequencyPlan_Type.__name__ = "Integer32"
_ModemProdCmCertFrequencyPlan_Object = MibScalar
modemProdCmCertFrequencyPlan = _ModemProdCmCertFrequencyPlan_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 1, 4),
    _ModemProdCmCertFrequencyPlan_Type()
)
modemProdCmCertFrequencyPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProdCmCertFrequencyPlan.setStatus("current")
_ModemProdCmCertDownload_Type = TruthValue
_ModemProdCmCertDownload_Object = MibScalar
modemProdCmCertDownload = _ModemProdCmCertDownload_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 1, 5),
    _ModemProdCmCertDownload_Type()
)
modemProdCmCertDownload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProdCmCertDownload.setStatus("current")


class _ModemProdCmCertOperStat_Type(Integer32):
    """Custom type modemProdCmCertOperStat based on Integer32"""
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
          ("downloadInProgress", 1),
          ("downloadSuccess", 2),
          ("downloadFailed", 3))
    )


_ModemProdCmCertOperStat_Type.__name__ = "Integer32"
_ModemProdCmCertOperStat_Object = MibScalar
modemProdCmCertOperStat = _ModemProdCmCertOperStat_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 1, 6),
    _ModemProdCmCertOperStat_Type()
)
modemProdCmCertOperStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemProdCmCertOperStat.setStatus("current")
_ModemProdCmManufacturingSetup_ObjectIdentity = ObjectIdentity
modemProdCmManufacturingSetup = _ModemProdCmManufacturingSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 2)
)


class _ModemProdMibAccessControl_Type(Integer32):
    """Custom type modemProdMibAccessControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("maxaccess", 1),
          ("limitedaccess", 2),
          ("nonaccessible", 3))
    )


_ModemProdMibAccessControl_Type.__name__ = "Integer32"
_ModemProdMibAccessControl_Object = MibScalar
modemProdMibAccessControl = _ModemProdMibAccessControl_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 2, 1),
    _ModemProdMibAccessControl_Type()
)
modemProdMibAccessControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProdMibAccessControl.setStatus("current")


class _ModemProdSerialNumber_Type(DisplayString):
    """Custom type modemProdSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ModemProdSerialNumber_Type.__name__ = "DisplayString"
_ModemProdSerialNumber_Object = MibScalar
modemProdSerialNumber = _ModemProdSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 2, 2),
    _ModemProdSerialNumber_Type()
)
modemProdSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemProdSerialNumber.setStatus("current")
_ModemProdMtaEnable_Type = TruthValue
_ModemProdMtaEnable_Object = MibScalar
modemProdMtaEnable = _ModemProdMtaEnable_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 2, 3),
    _ModemProdMtaEnable_Type()
)
modemProdMtaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProdMtaEnable.setStatus("current")
_ModemProdMfgOrganizationName_Type = DisplayString
_ModemProdMfgOrganizationName_Object = MibScalar
modemProdMfgOrganizationName = _ModemProdMfgOrganizationName_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 2, 4),
    _ModemProdMfgOrganizationName_Type()
)
modemProdMfgOrganizationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProdMfgOrganizationName.setStatus("current")
_ModemProdCvcAccessStart_Type = DateAndTime
_ModemProdCvcAccessStart_Object = MibScalar
modemProdCvcAccessStart = _ModemProdCvcAccessStart_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 2, 5),
    _ModemProdCvcAccessStart_Type()
)
modemProdCvcAccessStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProdCvcAccessStart.setStatus("current")
_ModemProdCodeAccessStart_Type = DateAndTime
_ModemProdCodeAccessStart_Object = MibScalar
modemProdCodeAccessStart = _ModemProdCodeAccessStart_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 2, 6),
    _ModemProdCodeAccessStart_Type()
)
modemProdCodeAccessStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProdCodeAccessStart.setStatus("current")
_ModemProdLanIp_Type = IpAddress
_ModemProdLanIp_Object = MibScalar
modemProdLanIp = _ModemProdLanIp_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 2, 7),
    _ModemProdLanIp_Type()
)
modemProdLanIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProdLanIp.setStatus("current")
_ModemProdHostIp_Type = IpAddress
_ModemProdHostIp_Object = MibScalar
modemProdHostIp = _ModemProdHostIp_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 2, 8),
    _ModemProdHostIp_Type()
)
modemProdHostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProdHostIp.setStatus("current")
_ModemProdIpMask_Type = IpAddress
_ModemProdIpMask_Object = MibScalar
modemProdIpMask = _ModemProdIpMask_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 2, 9),
    _ModemProdIpMask_Type()
)
modemProdIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProdIpMask.setStatus("current")
_ModemProdInterfaceName_Type = DisplayString
_ModemProdInterfaceName_Object = MibScalar
modemProdInterfaceName = _ModemProdInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 2, 10),
    _ModemProdInterfaceName_Type()
)
modemProdInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProdInterfaceName.setStatus("current")
_ModemProdCmMacAddress_Type = MacAddress
_ModemProdCmMacAddress_Object = MibScalar
modemProdCmMacAddress = _ModemProdCmMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 2, 11),
    _ModemProdCmMacAddress_Type()
)
modemProdCmMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProdCmMacAddress.setStatus("current")
_ModemProdLanMacAddress_Type = MacAddress
_ModemProdLanMacAddress_Object = MibScalar
modemProdLanMacAddress = _ModemProdLanMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 2, 12),
    _ModemProdLanMacAddress_Type()
)
modemProdLanMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProdLanMacAddress.setStatus("current")
_ModemProdUsbDevMacAddress_Type = MacAddress
_ModemProdUsbDevMacAddress_Object = MibScalar
modemProdUsbDevMacAddress = _ModemProdUsbDevMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 2, 13),
    _ModemProdUsbDevMacAddress_Type()
)
modemProdUsbDevMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProdUsbDevMacAddress.setStatus("current")
_ModemProdUsbHostMacAddress_Type = MacAddress
_ModemProdUsbHostMacAddress_Object = MibScalar
modemProdUsbHostMacAddress = _ModemProdUsbHostMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 2, 14),
    _ModemProdUsbHostMacAddress_Type()
)
modemProdUsbHostMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProdUsbHostMacAddress.setStatus("current")


class _ModemProdBaudRate_Type(Integer32):
    """Custom type modemProdBaudRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("br2400", 1),
          ("br4800", 2),
          ("br9600", 3),
          ("br19200", 4),
          ("br38400", 5),
          ("br115200", 6))
    )


_ModemProdBaudRate_Type.__name__ = "Integer32"
_ModemProdBaudRate_Object = MibScalar
modemProdBaudRate = _ModemProdBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 2, 15),
    _ModemProdBaudRate_Type()
)
modemProdBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProdBaudRate.setStatus("current")


class _ModemProdTunersNumber_Type(Integer32):
    """Custom type modemProdTunersNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_ModemProdTunersNumber_Type.__name__ = "Integer32"
_ModemProdTunersNumber_Object = MibScalar
modemProdTunersNumber = _ModemProdTunersNumber_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 2, 16),
    _ModemProdTunersNumber_Type()
)
modemProdTunersNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProdTunersNumber.setStatus("current")
_ModemProdDocsisPhyMultFact_Type = Integer32
_ModemProdDocsisPhyMultFact_Object = MibScalar
modemProdDocsisPhyMultFact = _ModemProdDocsisPhyMultFact_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 2, 17),
    _ModemProdDocsisPhyMultFact_Type()
)
modemProdDocsisPhyMultFact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProdDocsisPhyMultFact.setStatus("current")


class _ModemProdTunerType_Type(Integer32):
    """Custom type modemProdTunerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("mt2060", 1),
          ("mt2064", 2),
          ("mt2068", 3),
          ("mt2170", 4),
          ("anadAt1061", 5))
    )


_ModemProdTunerType_Type.__name__ = "Integer32"
_ModemProdTunerType_Object = MibScalar
modemProdTunerType = _ModemProdTunerType_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 2, 18),
    _ModemProdTunerType_Type()
)
modemProdTunerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProdTunerType.setStatus("current")


class _ModemProdPgaType_Type(Integer32):
    """Custom type modemProdPgaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("anadAra2017", 1))
    )


_ModemProdPgaType_Type.__name__ = "Integer32"
_ModemProdPgaType_Object = MibScalar
modemProdPgaType = _ModemProdPgaType_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 2, 19),
    _ModemProdPgaType_Type()
)
modemProdPgaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProdPgaType.setStatus("current")
_ModemProdHwRevision_Type = Integer32
_ModemProdHwRevision_Object = MibScalar
modemProdHwRevision = _ModemProdHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 2, 20),
    _ModemProdHwRevision_Type()
)
modemProdHwRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProdHwRevision.setStatus("current")


class _ModemProdFrequencyPlan_Type(Integer32):
    """Custom type modemProdFrequencyPlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("northAmerican", 1),
          ("european", 2),
          ("japanese", 3),
          ("hybrid", 4))
    )


_ModemProdFrequencyPlan_Type.__name__ = "Integer32"
_ModemProdFrequencyPlan_Object = MibScalar
modemProdFrequencyPlan = _ModemProdFrequencyPlan_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 2, 21),
    _ModemProdFrequencyPlan_Type()
)
modemProdFrequencyPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProdFrequencyPlan.setStatus("current")
_ModemProdEnableCli_Type = TruthValue
_ModemProdEnableCli_Object = MibScalar
modemProdEnableCli = _ModemProdEnableCli_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 2, 22),
    _ModemProdEnableCli_Type()
)
modemProdEnableCli.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProdEnableCli.setStatus("current")
_ModemProdCmCalibrationSetup_ObjectIdentity = ObjectIdentity
modemProdCmCalibrationSetup = _ModemProdCmCalibrationSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3)
)
_ModemProdDownstreamCalibration_ObjectIdentity = ObjectIdentity
modemProdDownstreamCalibration = _ModemProdDownstreamCalibration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3, 1)
)


class _ModemProdDsCalibrationOperStatus_Type(Integer32):
    """Custom type modemProdDsCalibrationOperStatus based on Integer32"""
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
        *(("emptyTable", 1),
          ("completeTable", 2),
          ("callibrationInProgress", 3),
          ("callibrationComplete", 4))
    )


_ModemProdDsCalibrationOperStatus_Type.__name__ = "Integer32"
_ModemProdDsCalibrationOperStatus_Object = MibScalar
modemProdDsCalibrationOperStatus = _ModemProdDsCalibrationOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3, 1, 1),
    _ModemProdDsCalibrationOperStatus_Type()
)
modemProdDsCalibrationOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemProdDsCalibrationOperStatus.setStatus("current")


class _ModemProdDsCalibrationAdminStatus_Type(Integer32):
    """Custom type modemProdDsCalibrationAdminStatus based on Integer32"""
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
        *(("validateAndStart", 1),
          ("validateOnly", 2),
          ("startOnly", 3),
          ("erase", 4))
    )


_ModemProdDsCalibrationAdminStatus_Type.__name__ = "Integer32"
_ModemProdDsCalibrationAdminStatus_Object = MibScalar
modemProdDsCalibrationAdminStatus = _ModemProdDsCalibrationAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3, 1, 2),
    _ModemProdDsCalibrationAdminStatus_Type()
)
modemProdDsCalibrationAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProdDsCalibrationAdminStatus.setStatus("current")
_ModemProdPowerCalibrationTable_Object = MibTable
modemProdPowerCalibrationTable = _ModemProdPowerCalibrationTable_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    modemProdPowerCalibrationTable.setStatus("current")
_ModemProdPowerCalibrationEntry_Object = MibTableRow
modemProdPowerCalibrationEntry = _ModemProdPowerCalibrationEntry_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3, 1, 3, 1)
)
modemProdPowerCalibrationEntry.setIndexNames(
    (0, "TI-PRODUCTION-MIB", "modemProdDsCallIndex"),
)
if mibBuilder.loadTexts:
    modemProdPowerCalibrationEntry.setStatus("current")


class _ModemProdDsCallIndex_Type(Integer32):
    """Custom type modemProdDsCallIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ModemProdDsCallIndex_Type.__name__ = "Integer32"
_ModemProdDsCallIndex_Object = MibTableColumn
modemProdDsCallIndex = _ModemProdDsCallIndex_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3, 1, 3, 1, 1),
    _ModemProdDsCallIndex_Type()
)
modemProdDsCallIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    modemProdDsCallIndex.setStatus("current")


class _ModemProdDsFrequency_Type(Integer32):
    """Custom type modemProdDsFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(80000, 1300000),
    )


_ModemProdDsFrequency_Type.__name__ = "Integer32"
_ModemProdDsFrequency_Object = MibTableColumn
modemProdDsFrequency = _ModemProdDsFrequency_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3, 1, 3, 1, 2),
    _ModemProdDsFrequency_Type()
)
modemProdDsFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProdDsFrequency.setStatus("current")
if mibBuilder.loadTexts:
    modemProdDsFrequency.setUnits("herz")


class _ModemProdDsPower_Type(Integer32):
    """Custom type modemProdDsPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-700, 700),
    )


_ModemProdDsPower_Type.__name__ = "Integer32"
_ModemProdDsPower_Object = MibTableColumn
modemProdDsPower = _ModemProdDsPower_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3, 1, 3, 1, 3),
    _ModemProdDsPower_Type()
)
modemProdDsPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProdDsPower.setStatus("current")
if mibBuilder.loadTexts:
    modemProdDsPower.setUnits("0.01 dbmV")
_ModemProdUpstreamTransmit_ObjectIdentity = ObjectIdentity
modemProdUpstreamTransmit = _ModemProdUpstreamTransmit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3, 2)
)
_ModemProdUpTransGain_Type = Integer32
_ModemProdUpTransGain_Object = MibScalar
modemProdUpTransGain = _ModemProdUpTransGain_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3, 2, 1),
    _ModemProdUpTransGain_Type()
)
modemProdUpTransGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProdUpTransGain.setStatus("current")
_ModemProdUpstreamTransmitTable_Object = MibTable
modemProdUpstreamTransmitTable = _ModemProdUpstreamTransmitTable_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    modemProdUpstreamTransmitTable.setStatus("current")
_ModemProdUpstreamTransmitEntry_Object = MibTableRow
modemProdUpstreamTransmitEntry = _ModemProdUpstreamTransmitEntry_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3, 2, 2, 1)
)
modemProdUpstreamTransmitEntry.setIndexNames(
    (0, "TI-PRODUCTION-MIB", "modemProdUsTransmitlIndex"),
)
if mibBuilder.loadTexts:
    modemProdUpstreamTransmitEntry.setStatus("current")


class _ModemProdUsTransmitlIndex_Type(Integer32):
    """Custom type modemProdUsTransmitlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ModemProdUsTransmitlIndex_Type.__name__ = "Integer32"
_ModemProdUsTransmitlIndex_Object = MibTableColumn
modemProdUsTransmitlIndex = _ModemProdUsTransmitlIndex_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3, 2, 2, 1, 1),
    _ModemProdUsTransmitlIndex_Type()
)
modemProdUsTransmitlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    modemProdUsTransmitlIndex.setStatus("current")
_ModemProdUsFrequency_Type = Integer32
_ModemProdUsFrequency_Object = MibTableColumn
modemProdUsFrequency = _ModemProdUsFrequency_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3, 2, 2, 1, 2),
    _ModemProdUsFrequency_Type()
)
modemProdUsFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProdUsFrequency.setStatus("current")
if mibBuilder.loadTexts:
    modemProdUsFrequency.setUnits("herz")


class _ModemProdUsModulation_Type(Integer32):
    """Custom type modemProdUsModulation based on Integer32"""
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
        *(("qpsk", 1),
          ("qam8", 2),
          ("qam16", 3),
          ("qam32", 4),
          ("qam64", 5),
          ("qam128", 6),
          ("qam256", 7))
    )


_ModemProdUsModulation_Type.__name__ = "Integer32"
_ModemProdUsModulation_Object = MibTableColumn
modemProdUsModulation = _ModemProdUsModulation_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3, 2, 2, 1, 3),
    _ModemProdUsModulation_Type()
)
modemProdUsModulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProdUsModulation.setStatus("current")


class _ModemProdUsSymbolRate_Type(Integer32):
    """Custom type modemProdUsSymbolRate based on Integer32"""
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
        *(("sr1", 1),
          ("sr2", 2),
          ("sr4", 3),
          ("sr8", 4),
          ("sr16", 5),
          ("sr32", 6))
    )


_ModemProdUsSymbolRate_Type.__name__ = "Integer32"
_ModemProdUsSymbolRate_Object = MibTableColumn
modemProdUsSymbolRate = _ModemProdUsSymbolRate_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3, 2, 2, 1, 4),
    _ModemProdUsSymbolRate_Type()
)
modemProdUsSymbolRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProdUsSymbolRate.setStatus("current")
_ModemProdUsAttenuation_Type = Integer32
_ModemProdUsAttenuation_Object = MibTableColumn
modemProdUsAttenuation = _ModemProdUsAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3, 2, 2, 1, 5),
    _ModemProdUsAttenuation_Type()
)
modemProdUsAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProdUsAttenuation.setStatus("current")
if mibBuilder.loadTexts:
    modemProdUsAttenuation.setUnits("dB")


class _ModemProdUsTransmitionType_Type(Integer32):
    """Custom type modemProdUsTransmitionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stop", 1),
          ("data", 2),
          ("syn", 3))
    )


_ModemProdUsTransmitionType_Type.__name__ = "Integer32"
_ModemProdUsTransmitionType_Object = MibTableColumn
modemProdUsTransmitionType = _ModemProdUsTransmitionType_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3, 2, 2, 1, 6),
    _ModemProdUsTransmitionType_Type()
)
modemProdUsTransmitionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProdUsTransmitionType.setStatus("current")
_ModemProdUsBurst_Type = Integer32
_ModemProdUsBurst_Object = MibTableColumn
modemProdUsBurst = _ModemProdUsBurst_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3, 2, 2, 1, 7),
    _ModemProdUsBurst_Type()
)
modemProdUsBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProdUsBurst.setStatus("current")
_ModemProdUpstreamCalibration_ObjectIdentity = ObjectIdentity
modemProdUpstreamCalibration = _ModemProdUpstreamCalibration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3, 3)
)


class _ModemProdUsCalibrationTableErase_Type(Integer32):
    """Custom type modemProdUsCalibrationTableErase based on Integer32"""
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
        *(("pgaParams", 1),
          ("cmfParams", 2),
          ("freqParams", 3),
          ("allTables", 4))
    )


_ModemProdUsCalibrationTableErase_Type.__name__ = "Integer32"
_ModemProdUsCalibrationTableErase_Object = MibScalar
modemProdUsCalibrationTableErase = _ModemProdUsCalibrationTableErase_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3, 3, 1),
    _ModemProdUsCalibrationTableErase_Type()
)
modemProdUsCalibrationTableErase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProdUsCalibrationTableErase.setStatus("current")


class _ModemProdUsCalibrationModeFactor_Type(Integer32):
    """Custom type modemProdUsCalibrationModeFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_ModemProdUsCalibrationModeFactor_Type.__name__ = "Integer32"
_ModemProdUsCalibrationModeFactor_Object = MibScalar
modemProdUsCalibrationModeFactor = _ModemProdUsCalibrationModeFactor_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3, 3, 2),
    _ModemProdUsCalibrationModeFactor_Type()
)
modemProdUsCalibrationModeFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProdUsCalibrationModeFactor.setStatus("current")
_ModemProdUsCalibrationPowerDelta_Type = Integer32
_ModemProdUsCalibrationPowerDelta_Object = MibScalar
modemProdUsCalibrationPowerDelta = _ModemProdUsCalibrationPowerDelta_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3, 3, 3),
    _ModemProdUsCalibrationPowerDelta_Type()
)
modemProdUsCalibrationPowerDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProdUsCalibrationPowerDelta.setStatus("current")
if mibBuilder.loadTexts:
    modemProdUsCalibrationPowerDelta.setUnits("dB")
_ModemProdUpstreamCalibrationTable_Object = MibTable
modemProdUpstreamCalibrationTable = _ModemProdUpstreamCalibrationTable_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3, 3, 4)
)
if mibBuilder.loadTexts:
    modemProdUpstreamCalibrationTable.setStatus("current")
_ModemProdUpstreamCalibrationEntry_Object = MibTableRow
modemProdUpstreamCalibrationEntry = _ModemProdUpstreamCalibrationEntry_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3, 3, 4, 1)
)
modemProdUpstreamCalibrationEntry.setIndexNames(
    (0, "TI-PRODUCTION-MIB", "modemProdUsCalibrationIndex"),
)
if mibBuilder.loadTexts:
    modemProdUpstreamCalibrationEntry.setStatus("current")


class _ModemProdUsCalibrationIndex_Type(Integer32):
    """Custom type modemProdUsCalibrationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ModemProdUsCalibrationIndex_Type.__name__ = "Integer32"
_ModemProdUsCalibrationIndex_Object = MibTableColumn
modemProdUsCalibrationIndex = _ModemProdUsCalibrationIndex_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3, 3, 4, 1, 1),
    _ModemProdUsCalibrationIndex_Type()
)
modemProdUsCalibrationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    modemProdUsCalibrationIndex.setStatus("current")
_ModemProdUsCalibrationPower_Type = Integer32
_ModemProdUsCalibrationPower_Object = MibTableColumn
modemProdUsCalibrationPower = _ModemProdUsCalibrationPower_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3, 3, 4, 1, 2),
    _ModemProdUsCalibrationPower_Type()
)
modemProdUsCalibrationPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemProdUsCalibrationPower.setStatus("current")
if mibBuilder.loadTexts:
    modemProdUsCalibrationPower.setUnits("dB")
_ModemProdFrequencyCalibrationTable_Object = MibTable
modemProdFrequencyCalibrationTable = _ModemProdFrequencyCalibrationTable_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3, 3, 5)
)
if mibBuilder.loadTexts:
    modemProdFrequencyCalibrationTable.setStatus("current")
_ModemProdFrequencyCalibrationEntry_Object = MibTableRow
modemProdFrequencyCalibrationEntry = _ModemProdFrequencyCalibrationEntry_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3, 3, 5, 1)
)
modemProdFrequencyCalibrationEntry.setIndexNames(
    (0, "TI-PRODUCTION-MIB", "modemProdUsFreqCalibrationIndex"),
)
if mibBuilder.loadTexts:
    modemProdFrequencyCalibrationEntry.setStatus("current")
_ModemProdUsFreqCalibrationIndex_Type = Integer32
_ModemProdUsFreqCalibrationIndex_Object = MibTableColumn
modemProdUsFreqCalibrationIndex = _ModemProdUsFreqCalibrationIndex_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3, 3, 5, 1, 1),
    _ModemProdUsFreqCalibrationIndex_Type()
)
modemProdUsFreqCalibrationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    modemProdUsFreqCalibrationIndex.setStatus("current")
if mibBuilder.loadTexts:
    modemProdUsFreqCalibrationIndex.setUnits("herz")
_ModemProdUsFreqCalibrationPower_Type = Integer32
_ModemProdUsFreqCalibrationPower_Object = MibTableColumn
modemProdUsFreqCalibrationPower = _ModemProdUsFreqCalibrationPower_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3, 3, 5, 1, 2),
    _ModemProdUsFreqCalibrationPower_Type()
)
modemProdUsFreqCalibrationPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemProdUsFreqCalibrationPower.setStatus("current")
if mibBuilder.loadTexts:
    modemProdUsFreqCalibrationPower.setUnits("dBmV")
_ModemProdPgaAttenuationTable_Object = MibTable
modemProdPgaAttenuationTable = _ModemProdPgaAttenuationTable_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3, 3, 6)
)
if mibBuilder.loadTexts:
    modemProdPgaAttenuationTable.setStatus("current")
_ModemProdPgaAttenuationEntry_Object = MibTableRow
modemProdPgaAttenuationEntry = _ModemProdPgaAttenuationEntry_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3, 3, 6, 1)
)
modemProdPgaAttenuationEntry.setIndexNames(
    (0, "TI-PRODUCTION-MIB", "modemProdUsPgaAttenIndex"),
)
if mibBuilder.loadTexts:
    modemProdPgaAttenuationEntry.setStatus("current")


class _ModemProdUsPgaAttenIndex_Type(Integer32):
    """Custom type modemProdUsPgaAttenIndex based on Integer32"""
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
        *(("pgaAtten0dB", 1),
          ("pgaAtten2dB", 2),
          ("pgaAtten4dB", 3),
          ("pgaAtten8dB", 4),
          ("pgaAtten16dB", 5),
          ("pgaAtten32dBb", 6))
    )


_ModemProdUsPgaAttenIndex_Type.__name__ = "Integer32"
_ModemProdUsPgaAttenIndex_Object = MibTableColumn
modemProdUsPgaAttenIndex = _ModemProdUsPgaAttenIndex_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3, 3, 6, 1, 1),
    _ModemProdUsPgaAttenIndex_Type()
)
modemProdUsPgaAttenIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    modemProdUsPgaAttenIndex.setStatus("current")
_ModemProdUsPgaAttenPower_Type = Integer32
_ModemProdUsPgaAttenPower_Object = MibTableColumn
modemProdUsPgaAttenPower = _ModemProdUsPgaAttenPower_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3, 3, 6, 1, 2),
    _ModemProdUsPgaAttenPower_Type()
)
modemProdUsPgaAttenPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemProdUsPgaAttenPower.setStatus("current")
if mibBuilder.loadTexts:
    modemProdUsPgaAttenPower.setUnits("dBmV")
_ModemProdCurrentModeFactorTable_Object = MibTable
modemProdCurrentModeFactorTable = _ModemProdCurrentModeFactorTable_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3, 3, 7)
)
if mibBuilder.loadTexts:
    modemProdCurrentModeFactorTable.setStatus("current")
_ModemProdCurrentModeFactorEntry_Object = MibTableRow
modemProdCurrentModeFactorEntry = _ModemProdCurrentModeFactorEntry_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3, 3, 7, 1)
)
modemProdCurrentModeFactorEntry.setIndexNames(
    (0, "TI-PRODUCTION-MIB", "modemProdUsCmfIndex"),
)
if mibBuilder.loadTexts:
    modemProdCurrentModeFactorEntry.setStatus("current")


class _ModemProdUsCmfIndex_Type(Integer32):
    """Custom type modemProdUsCmfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_ModemProdUsCmfIndex_Type.__name__ = "Integer32"
_ModemProdUsCmfIndex_Object = MibTableColumn
modemProdUsCmfIndex = _ModemProdUsCmfIndex_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3, 3, 7, 1, 1),
    _ModemProdUsCmfIndex_Type()
)
modemProdUsCmfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    modemProdUsCmfIndex.setStatus("current")
_ModemProdUsCmfPower_Type = Integer32
_ModemProdUsCmfPower_Object = MibTableColumn
modemProdUsCmfPower = _ModemProdUsCmfPower_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3, 3, 7, 1, 2),
    _ModemProdUsCmfPower_Type()
)
modemProdUsCmfPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemProdUsCmfPower.setStatus("current")
if mibBuilder.loadTexts:
    modemProdUsCmfPower.setUnits("dBmV")
_ModemProdUsCalibrationUpdateFlash_Type = TruthValue
_ModemProdUsCalibrationUpdateFlash_Object = MibScalar
modemProdUsCalibrationUpdateFlash = _ModemProdUsCalibrationUpdateFlash_Object(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 1, 3, 3, 8),
    _ModemProdUsCalibrationUpdateFlash_Type()
)
modemProdUsCalibrationUpdateFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProdUsCalibrationUpdateFlash.setStatus("current")
_ModemProdCmTest_ObjectIdentity = ObjectIdentity
modemProdCmTest = _ModemProdCmTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 294, 1, 400, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TI-PRODUCTION-MIB",
    **{"modemProduction": modemProduction,
       "modemProdCmSetup": modemProdCmSetup,
       "modemProdCmPermanentSetup": modemProdCmPermanentSetup,
       "modemProdCmCertServerIp": modemProdCmCertServerIp,
       "modemProdCmCertFileName": modemProdCmCertFileName,
       "modemProdCmCertKeyFileName": modemProdCmCertKeyFileName,
       "modemProdCmCertFrequencyPlan": modemProdCmCertFrequencyPlan,
       "modemProdCmCertDownload": modemProdCmCertDownload,
       "modemProdCmCertOperStat": modemProdCmCertOperStat,
       "modemProdCmManufacturingSetup": modemProdCmManufacturingSetup,
       "modemProdMibAccessControl": modemProdMibAccessControl,
       "modemProdSerialNumber": modemProdSerialNumber,
       "modemProdMtaEnable": modemProdMtaEnable,
       "modemProdMfgOrganizationName": modemProdMfgOrganizationName,
       "modemProdCvcAccessStart": modemProdCvcAccessStart,
       "modemProdCodeAccessStart": modemProdCodeAccessStart,
       "modemProdLanIp": modemProdLanIp,
       "modemProdHostIp": modemProdHostIp,
       "modemProdIpMask": modemProdIpMask,
       "modemProdInterfaceName": modemProdInterfaceName,
       "modemProdCmMacAddress": modemProdCmMacAddress,
       "modemProdLanMacAddress": modemProdLanMacAddress,
       "modemProdUsbDevMacAddress": modemProdUsbDevMacAddress,
       "modemProdUsbHostMacAddress": modemProdUsbHostMacAddress,
       "modemProdBaudRate": modemProdBaudRate,
       "modemProdTunersNumber": modemProdTunersNumber,
       "modemProdDocsisPhyMultFact": modemProdDocsisPhyMultFact,
       "modemProdTunerType": modemProdTunerType,
       "modemProdPgaType": modemProdPgaType,
       "modemProdHwRevision": modemProdHwRevision,
       "modemProdFrequencyPlan": modemProdFrequencyPlan,
       "modemProdEnableCli": modemProdEnableCli,
       "modemProdCmCalibrationSetup": modemProdCmCalibrationSetup,
       "modemProdDownstreamCalibration": modemProdDownstreamCalibration,
       "modemProdDsCalibrationOperStatus": modemProdDsCalibrationOperStatus,
       "modemProdDsCalibrationAdminStatus": modemProdDsCalibrationAdminStatus,
       "modemProdPowerCalibrationTable": modemProdPowerCalibrationTable,
       "modemProdPowerCalibrationEntry": modemProdPowerCalibrationEntry,
       "modemProdDsCallIndex": modemProdDsCallIndex,
       "modemProdDsFrequency": modemProdDsFrequency,
       "modemProdDsPower": modemProdDsPower,
       "modemProdUpstreamTransmit": modemProdUpstreamTransmit,
       "modemProdUpTransGain": modemProdUpTransGain,
       "modemProdUpstreamTransmitTable": modemProdUpstreamTransmitTable,
       "modemProdUpstreamTransmitEntry": modemProdUpstreamTransmitEntry,
       "modemProdUsTransmitlIndex": modemProdUsTransmitlIndex,
       "modemProdUsFrequency": modemProdUsFrequency,
       "modemProdUsModulation": modemProdUsModulation,
       "modemProdUsSymbolRate": modemProdUsSymbolRate,
       "modemProdUsAttenuation": modemProdUsAttenuation,
       "modemProdUsTransmitionType": modemProdUsTransmitionType,
       "modemProdUsBurst": modemProdUsBurst,
       "modemProdUpstreamCalibration": modemProdUpstreamCalibration,
       "modemProdUsCalibrationTableErase": modemProdUsCalibrationTableErase,
       "modemProdUsCalibrationModeFactor": modemProdUsCalibrationModeFactor,
       "modemProdUsCalibrationPowerDelta": modemProdUsCalibrationPowerDelta,
       "modemProdUpstreamCalibrationTable": modemProdUpstreamCalibrationTable,
       "modemProdUpstreamCalibrationEntry": modemProdUpstreamCalibrationEntry,
       "modemProdUsCalibrationIndex": modemProdUsCalibrationIndex,
       "modemProdUsCalibrationPower": modemProdUsCalibrationPower,
       "modemProdFrequencyCalibrationTable": modemProdFrequencyCalibrationTable,
       "modemProdFrequencyCalibrationEntry": modemProdFrequencyCalibrationEntry,
       "modemProdUsFreqCalibrationIndex": modemProdUsFreqCalibrationIndex,
       "modemProdUsFreqCalibrationPower": modemProdUsFreqCalibrationPower,
       "modemProdPgaAttenuationTable": modemProdPgaAttenuationTable,
       "modemProdPgaAttenuationEntry": modemProdPgaAttenuationEntry,
       "modemProdUsPgaAttenIndex": modemProdUsPgaAttenIndex,
       "modemProdUsPgaAttenPower": modemProdUsPgaAttenPower,
       "modemProdCurrentModeFactorTable": modemProdCurrentModeFactorTable,
       "modemProdCurrentModeFactorEntry": modemProdCurrentModeFactorEntry,
       "modemProdUsCmfIndex": modemProdUsCmfIndex,
       "modemProdUsCmfPower": modemProdUsCmfPower,
       "modemProdUsCalibrationUpdateFlash": modemProdUsCalibrationUpdateFlash,
       "modemProdCmTest": modemProdCmTest}
)
