# SNMP MIB module (RED-LION-RAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/redlionram/RED-LION-RAM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:10:56 2025
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Redlionram_ObjectIdentity = ObjectIdentity
redlionram = _Redlionram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1890)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1890, 1)
)
_UnitInfo_ObjectIdentity = ObjectIdentity
unitInfo = _UnitInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1890, 1, 1)
)
_UnitDescription_Type = DisplayString
_UnitDescription_Object = MibScalar
unitDescription = _UnitDescription_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 1, 1),
    _UnitDescription_Type()
)
unitDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitDescription.setStatus("mandatory")
_UnitSerialNumber_Type = DisplayString
_UnitSerialNumber_Object = MibScalar
unitSerialNumber = _UnitSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 1, 2),
    _UnitSerialNumber_Type()
)
unitSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitSerialNumber.setStatus("mandatory")
_UnitFirmwareVersion_Type = DisplayString
_UnitFirmwareVersion_Object = MibScalar
unitFirmwareVersion = _UnitFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 1, 3),
    _UnitFirmwareVersion_Type()
)
unitFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitFirmwareVersion.setStatus("mandatory")
_UnitName_Type = DisplayString
_UnitName_Object = MibScalar
unitName = _UnitName_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 1, 4),
    _UnitName_Type()
)
unitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitName.setStatus("mandatory")
_Cellular_ObjectIdentity = ObjectIdentity
cellular = _Cellular_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2)
)
_Mdn_Type = DisplayString
_Mdn_Object = MibScalar
mdn = _Mdn_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 1),
    _Mdn_Type()
)
mdn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdn.setStatus("mandatory")
_MinIMEI_Type = DisplayString
_MinIMEI_Object = MibScalar
minIMEI = _MinIMEI_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 2),
    _MinIMEI_Type()
)
minIMEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minIMEI.setStatus("mandatory")
_Nai_Type = DisplayString
_Nai_Object = MibScalar
nai = _Nai_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 3),
    _Nai_Type()
)
nai.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nai.setStatus("mandatory")
_SipUser_Type = Integer32
_SipUser_Object = MibScalar
sipUser = _SipUser_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 4),
    _SipUser_Type()
)
sipUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipUser.setStatus("mandatory")
_Sid_Type = Integer32
_Sid_Object = MibScalar
sid = _Sid_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 5),
    _Sid_Type()
)
sid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sid.setStatus("mandatory")
_Nid_Type = Integer32
_Nid_Object = MibScalar
nid = _Nid_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 6),
    _Nid_Type()
)
nid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nid.setStatus("mandatory")
_Prl_Type = Integer32
_Prl_Object = MibScalar
prl = _Prl_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 7),
    _Prl_Type()
)
prl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prl.setStatus("mandatory")
_Activated_Type = Integer32
_Activated_Object = MibScalar
activated = _Activated_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 8),
    _Activated_Type()
)
activated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activated.setStatus("mandatory")
_OmaSupported_Type = Integer32
_OmaSupported_Object = MibScalar
omaSupported = _OmaSupported_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 9),
    _OmaSupported_Type()
)
omaSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omaSupported.setStatus("mandatory")
_CurrentMipProfile_Type = Integer32
_CurrentMipProfile_Object = MibScalar
currentMipProfile = _CurrentMipProfile_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 10),
    _CurrentMipProfile_Type()
)
currentMipProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMipProfile.setStatus("mandatory")
_Esn_Type = DisplayString
_Esn_Object = MibScalar
esn = _Esn_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 11),
    _Esn_Type()
)
esn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esn.setStatus("mandatory")
_Pesn_Type = DisplayString
_Pesn_Object = MibScalar
pesn = _Pesn_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 12),
    _Pesn_Type()
)
pesn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pesn.setStatus("mandatory")
_Meid_Type = DisplayString
_Meid_Object = MibScalar
meid = _Meid_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 13),
    _Meid_Type()
)
meid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meid.setStatus("mandatory")
_Vendor_Type = DisplayString
_Vendor_Object = MibScalar
vendor = _Vendor_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 14),
    _Vendor_Type()
)
vendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vendor.setStatus("mandatory")
_ModelName_Type = DisplayString
_ModelName_Object = MibScalar
modelName = _ModelName_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 15),
    _ModelName_Type()
)
modelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modelName.setStatus("mandatory")
_FwVersion_Type = DisplayString
_FwVersion_Object = MibScalar
fwVersion = _FwVersion_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 16),
    _FwVersion_Type()
)
fwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVersion.setStatus("mandatory")
_HwVersion_Type = DisplayString
_HwVersion_Object = MibScalar
hwVersion = _HwVersion_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 17),
    _HwVersion_Type()
)
hwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVersion.setStatus("mandatory")
_Carrier_Type = DisplayString
_Carrier_Object = MibScalar
carrier = _Carrier_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 18),
    _Carrier_Type()
)
carrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrier.setStatus("mandatory")
_LowRssi_Type = Integer32
_LowRssi_Object = MibScalar
lowRssi = _LowRssi_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 19),
    _LowRssi_Type()
)
lowRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowRssi.setStatus("mandatory")
_LowEcio_Type = Integer32
_LowEcio_Object = MibScalar
lowEcio = _LowEcio_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 20),
    _LowEcio_Type()
)
lowEcio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowEcio.setStatus("mandatory")
_HighRssi_Type = Integer32
_HighRssi_Object = MibScalar
highRssi = _HighRssi_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 21),
    _HighRssi_Type()
)
highRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    highRssi.setStatus("mandatory")
_HighEcio_Type = Integer32
_HighEcio_Object = MibScalar
highEcio = _HighEcio_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 22),
    _HighEcio_Type()
)
highEcio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    highEcio.setStatus("mandatory")
_CurrentRssi_Type = Integer32
_CurrentRssi_Object = MibScalar
currentRssi = _CurrentRssi_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 23),
    _CurrentRssi_Type()
)
currentRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentRssi.setStatus("mandatory")
_CurrentEcio_Type = Integer32
_CurrentEcio_Object = MibScalar
currentEcio = _CurrentEcio_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 24),
    _CurrentEcio_Type()
)
currentEcio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentEcio.setStatus("mandatory")
_SvcType_Type = DisplayString
_SvcType_Object = MibScalar
svcType = _SvcType_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 25),
    _SvcType_Type()
)
svcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcType.setStatus("mandatory")
_CurrentChannel_Type = Integer32
_CurrentChannel_Object = MibScalar
currentChannel = _CurrentChannel_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 29),
    _CurrentChannel_Type()
)
currentChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentChannel.setStatus("mandatory")
_CdmaType_Type = DisplayString
_CdmaType_Object = MibScalar
cdmaType = _CdmaType_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 30),
    _CdmaType_Type()
)
cdmaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaType.setStatus("mandatory")
_HdrType_Type = DisplayString
_HdrType_Object = MibScalar
hdrType = _HdrType_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 31),
    _HdrType_Type()
)
hdrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdrType.setStatus("mandatory")
_CdmaRoaming_Type = DisplayString
_CdmaRoaming_Object = MibScalar
cdmaRoaming = _CdmaRoaming_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 32),
    _CdmaRoaming_Type()
)
cdmaRoaming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaRoaming.setStatus("mandatory")
_HdrRoaming_Type = DisplayString
_HdrRoaming_Object = MibScalar
hdrRoaming = _HdrRoaming_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 33),
    _HdrRoaming_Type()
)
hdrRoaming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdrRoaming.setStatus("mandatory")
_Roaming_Type = Integer32
_Roaming_Object = MibScalar
roaming = _Roaming_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 34),
    _Roaming_Type()
)
roaming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roaming.setStatus("mandatory")
_CurrentState_Type = Integer32
_CurrentState_Object = MibScalar
currentState = _CurrentState_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 35),
    _CurrentState_Type()
)
currentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentState.setStatus("mandatory")
_SpeedPref_Type = DisplayString
_SpeedPref_Object = MibScalar
speedPref = _SpeedPref_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 36),
    _SpeedPref_Type()
)
speedPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedPref.setStatus("mandatory")
_RoamPref_Type = DisplayString
_RoamPref_Object = MibScalar
roamPref = _RoamPref_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 37),
    _RoamPref_Type()
)
roamPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roamPref.setStatus("mandatory")
_DevName_Type = DisplayString
_DevName_Object = MibScalar
devName = _DevName_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 38),
    _DevName_Type()
)
devName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devName.setStatus("mandatory")
_IfName_Type = DisplayString
_IfName_Object = MibScalar
ifName = _IfName_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 39),
    _IfName_Type()
)
ifName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifName.setStatus("mandatory")
_TxCount_Type = Integer32
_TxCount_Object = MibScalar
txCount = _TxCount_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 40),
    _TxCount_Type()
)
txCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txCount.setStatus("mandatory")
_RxCount_Type = Integer32
_RxCount_Object = MibScalar
rxCount = _RxCount_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 41),
    _RxCount_Type()
)
rxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxCount.setStatus("mandatory")
_GprsState_Type = DisplayString
_GprsState_Object = MibScalar
gprsState = _GprsState_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 42),
    _GprsState_Type()
)
gprsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gprsState.setStatus("mandatory")
_RxLevel_Type = DisplayString
_RxLevel_Object = MibScalar
rxLevel = _RxLevel_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 43),
    _RxLevel_Type()
)
rxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxLevel.setStatus("mandatory")
_ServingCell_Type = DisplayString
_ServingCell_Object = MibScalar
servingCell = _ServingCell_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 44),
    _ServingCell_Type()
)
servingCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    servingCell.setStatus("mandatory")
_RccState_Type = DisplayString
_RccState_Object = MibScalar
rccState = _RccState_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 45),
    _RccState_Type()
)
rccState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rccState.setStatus("mandatory")
_GsmChannel_Type = DisplayString
_GsmChannel_Object = MibScalar
gsmChannel = _GsmChannel_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 46),
    _GsmChannel_Type()
)
gsmChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmChannel.setStatus("mandatory")
_PsState_Type = DisplayString
_PsState_Object = MibScalar
psState = _PsState_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 47),
    _PsState_Type()
)
psState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psState.setStatus("mandatory")
_Mode_Type = DisplayString
_Mode_Object = MibScalar
mode = _Mode_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 48),
    _Mode_Type()
)
mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mode.setStatus("mandatory")
_Temperature_Type = DisplayString
_Temperature_Object = MibScalar
temperature = _Temperature_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 49),
    _Temperature_Type()
)
temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature.setStatus("mandatory")
_SimContextApn0_Type = DisplayString
_SimContextApn0_Object = MibScalar
simContextApn0 = _SimContextApn0_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 50),
    _SimContextApn0_Type()
)
simContextApn0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simContextApn0.setStatus("mandatory")
_SimContextApn1_Type = DisplayString
_SimContextApn1_Object = MibScalar
simContextApn1 = _SimContextApn1_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 51),
    _SimContextApn1_Type()
)
simContextApn1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simContextApn1.setStatus("mandatory")
_SimStatus_Type = DisplayString
_SimStatus_Object = MibScalar
simStatus = _SimStatus_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 52),
    _SimStatus_Type()
)
simStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simStatus.setStatus("mandatory")
_ServiceDomain_Type = DisplayString
_ServiceDomain_Object = MibScalar
serviceDomain = _ServiceDomain_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 53),
    _ServiceDomain_Type()
)
serviceDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceDomain.setStatus("mandatory")
_AvailServiceType_Type = DisplayString
_AvailServiceType_Object = MibScalar
availServiceType = _AvailServiceType_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 54),
    _AvailServiceType_Type()
)
availServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    availServiceType.setStatus("mandatory")
_WCdmaL1State_Type = DisplayString
_WCdmaL1State_Object = MibScalar
wCdmaL1State = _WCdmaL1State_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 55),
    _WCdmaL1State_Type()
)
wCdmaL1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wCdmaL1State.setStatus("mandatory")
_MmcsState_Type = DisplayString
_MmcsState_Object = MibScalar
mmcsState = _MmcsState_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 56),
    _MmcsState_Type()
)
mmcsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmcsState.setStatus("mandatory")
_GmmPsState_Type = DisplayString
_GmmPsState_Object = MibScalar
gmmPsState = _GmmPsState_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 57),
    _GmmPsState_Type()
)
gmmPsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmmPsState.setStatus("mandatory")
_WCdmaChannel_Type = DisplayString
_WCdmaChannel_Object = MibScalar
wCdmaChannel = _WCdmaChannel_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 58),
    _WCdmaChannel_Type()
)
wCdmaChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wCdmaChannel.setStatus("mandatory")
_WCdmaBand_Type = DisplayString
_WCdmaBand_Object = MibScalar
wCdmaBand = _WCdmaBand_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 59),
    _WCdmaBand_Type()
)
wCdmaBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wCdmaBand.setStatus("mandatory")
_SystemMode_Type = DisplayString
_SystemMode_Object = MibScalar
systemMode = _SystemMode_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 60),
    _SystemMode_Type()
)
systemMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemMode.setStatus("mandatory")
_PowerOnTime_Type = DisplayString
_PowerOnTime_Object = MibScalar
powerOnTime = _PowerOnTime_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 61),
    _PowerOnTime_Type()
)
powerOnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerOnTime.setStatus("mandatory")
_LowSpeedCsq_Type = DisplayString
_LowSpeedCsq_Object = MibScalar
lowSpeedCsq = _LowSpeedCsq_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 62),
    _LowSpeedCsq_Type()
)
lowSpeedCsq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowSpeedCsq.setStatus("mandatory")
_HighSpeedCsq_Type = DisplayString
_HighSpeedCsq_Object = MibScalar
highSpeedCsq = _HighSpeedCsq_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 63),
    _HighSpeedCsq_Type()
)
highSpeedCsq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    highSpeedCsq.setStatus("mandatory")
_Band_Type = DisplayString
_Band_Object = MibScalar
band = _Band_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 64),
    _Band_Type()
)
band.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    band.setStatus("mandatory")
_Imei_Type = DisplayString
_Imei_Object = MibScalar
imei = _Imei_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 65),
    _Imei_Type()
)
imei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imei.setStatus("mandatory")
_SimId_Type = DisplayString
_SimId_Object = MibScalar
simId = _SimId_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 66),
    _SimId_Type()
)
simId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simId.setStatus("mandatory")
_CarrPLMN_Type = DisplayString
_CarrPLMN_Object = MibScalar
carrPLMN = _CarrPLMN_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 67),
    _CarrPLMN_Type()
)
carrPLMN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrPLMN.setStatus("mandatory")
_RxLevelC0_Type = DisplayString
_RxLevelC0_Object = MibScalar
rxLevelC0 = _RxLevelC0_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 68),
    _RxLevelC0_Type()
)
rxLevelC0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxLevelC0.setStatus("mandatory")
_RxLevelC1_Type = DisplayString
_RxLevelC1_Object = MibScalar
rxLevelC1 = _RxLevelC1_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 69),
    _RxLevelC1_Type()
)
rxLevelC1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxLevelC1.setStatus("mandatory")
_LocAreaCode_Type = DisplayString
_LocAreaCode_Object = MibScalar
locAreaCode = _LocAreaCode_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 70),
    _LocAreaCode_Type()
)
locAreaCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locAreaCode.setStatus("mandatory")
_LteBand_Type = DisplayString
_LteBand_Object = MibScalar
lteBand = _LteBand_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 71),
    _LteBand_Type()
)
lteBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lteBand.setStatus("mandatory")
_LteRxChan_Type = DisplayString
_LteRxChan_Object = MibScalar
lteRxChan = _LteRxChan_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 72),
    _LteRxChan_Type()
)
lteRxChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lteRxChan.setStatus("mandatory")
_LteTxChan_Type = DisplayString
_LteTxChan_Object = MibScalar
lteTxChan = _LteTxChan_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 73),
    _LteTxChan_Type()
)
lteTxChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lteTxChan.setStatus("mandatory")
_LteBW_Type = DisplayString
_LteBW_Object = MibScalar
lteBW = _LteBW_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 74),
    _LteBW_Type()
)
lteBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lteBW.setStatus("mandatory")
_LteRSRP_Type = DisplayString
_LteRSRP_Object = MibScalar
lteRSRP = _LteRSRP_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 75),
    _LteRSRP_Type()
)
lteRSRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lteRSRP.setStatus("mandatory")
_LteRSRQ_Type = DisplayString
_LteRSRQ_Object = MibScalar
lteRSRQ = _LteRSRQ_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 76),
    _LteRSRQ_Type()
)
lteRSRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lteRSRQ.setStatus("mandatory")
_LteTracAreaCode_Type = DisplayString
_LteTracAreaCode_Object = MibScalar
lteTracAreaCode = _LteTracAreaCode_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 77),
    _LteTracAreaCode_Type()
)
lteTracAreaCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lteTracAreaCode.setStatus("mandatory")
_Creg_Type = DisplayString
_Creg_Object = MibScalar
creg = _Creg_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 78),
    _Creg_Type()
)
creg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    creg.setStatus("mandatory")
_CellularUpTime_Type = Integer32
_CellularUpTime_Object = MibScalar
cellularUpTime = _CellularUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 79),
    _CellularUpTime_Type()
)
cellularUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularUpTime.setStatus("mandatory")
_LteRSRPint_Type = Integer32
_LteRSRPint_Object = MibScalar
lteRSRPint = _LteRSRPint_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 80),
    _LteRSRPint_Type()
)
lteRSRPint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lteRSRPint.setStatus("mandatory")
_LteRSRQint_Type = Integer32
_LteRSRQint_Object = MibScalar
lteRSRQint = _LteRSRQint_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 81),
    _LteRSRQint_Type()
)
lteRSRQint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lteRSRQint.setStatus("mandatory")
_LteSINRint_Type = Integer32
_LteSINRint_Object = MibScalar
lteSINRint = _LteSINRint_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 2, 82),
    _LteSINRint_Type()
)
lteSINRint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lteSINRint.setStatus("mandatory")
_Trafficppp0_ObjectIdentity = ObjectIdentity
trafficppp0 = _Trafficppp0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1890, 1, 3)
)
_TodayRxPpp0_Type = DisplayString
_TodayRxPpp0_Object = MibScalar
todayRxPpp0 = _TodayRxPpp0_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 3, 1),
    _TodayRxPpp0_Type()
)
todayRxPpp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    todayRxPpp0.setStatus("mandatory")
_TodayTxPpp0_Type = DisplayString
_TodayTxPpp0_Object = MibScalar
todayTxPpp0 = _TodayTxPpp0_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 3, 2),
    _TodayTxPpp0_Type()
)
todayTxPpp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    todayTxPpp0.setStatus("mandatory")
_TodayTotalPpp0_Type = DisplayString
_TodayTotalPpp0_Object = MibScalar
todayTotalPpp0 = _TodayTotalPpp0_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 3, 3),
    _TodayTotalPpp0_Type()
)
todayTotalPpp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    todayTotalPpp0.setStatus("mandatory")
_YesterdayRxPpp0_Type = DisplayString
_YesterdayRxPpp0_Object = MibScalar
yesterdayRxPpp0 = _YesterdayRxPpp0_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 3, 4),
    _YesterdayRxPpp0_Type()
)
yesterdayRxPpp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    yesterdayRxPpp0.setStatus("mandatory")
_YesterdayTxPpp0_Type = DisplayString
_YesterdayTxPpp0_Object = MibScalar
yesterdayTxPpp0 = _YesterdayTxPpp0_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 3, 5),
    _YesterdayTxPpp0_Type()
)
yesterdayTxPpp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    yesterdayTxPpp0.setStatus("mandatory")
_YesterdayTotalPpp0_Type = DisplayString
_YesterdayTotalPpp0_Object = MibScalar
yesterdayTotalPpp0 = _YesterdayTotalPpp0_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 3, 6),
    _YesterdayTotalPpp0_Type()
)
yesterdayTotalPpp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    yesterdayTotalPpp0.setStatus("mandatory")
_CurrMonthRxPpp0_Type = DisplayString
_CurrMonthRxPpp0_Object = MibScalar
currMonthRxPpp0 = _CurrMonthRxPpp0_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 3, 7),
    _CurrMonthRxPpp0_Type()
)
currMonthRxPpp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currMonthRxPpp0.setStatus("mandatory")
_CurrMonthTxPpp0_Type = DisplayString
_CurrMonthTxPpp0_Object = MibScalar
currMonthTxPpp0 = _CurrMonthTxPpp0_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 3, 8),
    _CurrMonthTxPpp0_Type()
)
currMonthTxPpp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currMonthTxPpp0.setStatus("mandatory")
_CurrMonthTotalPpp0_Type = DisplayString
_CurrMonthTotalPpp0_Object = MibScalar
currMonthTotalPpp0 = _CurrMonthTotalPpp0_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 3, 9),
    _CurrMonthTotalPpp0_Type()
)
currMonthTotalPpp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currMonthTotalPpp0.setStatus("mandatory")
_PreMonthRxPpp0_Type = DisplayString
_PreMonthRxPpp0_Object = MibScalar
preMonthRxPpp0 = _PreMonthRxPpp0_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 3, 10),
    _PreMonthRxPpp0_Type()
)
preMonthRxPpp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    preMonthRxPpp0.setStatus("mandatory")
_PreMonthTxPpp0_Type = DisplayString
_PreMonthTxPpp0_Object = MibScalar
preMonthTxPpp0 = _PreMonthTxPpp0_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 3, 11),
    _PreMonthTxPpp0_Type()
)
preMonthTxPpp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    preMonthTxPpp0.setStatus("mandatory")
_PreMonthTotalPpp0_Type = DisplayString
_PreMonthTotalPpp0_Object = MibScalar
preMonthTotalPpp0 = _PreMonthTotalPpp0_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 3, 12),
    _PreMonthTotalPpp0_Type()
)
preMonthTotalPpp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    preMonthTotalPpp0.setStatus("mandatory")
_TodayRxPpp0Kib_Type = Integer32
_TodayRxPpp0Kib_Object = MibScalar
todayRxPpp0Kib = _TodayRxPpp0Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 3, 13),
    _TodayRxPpp0Kib_Type()
)
todayRxPpp0Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    todayRxPpp0Kib.setStatus("mandatory")
_TodayTxPpp0Kib_Type = Integer32
_TodayTxPpp0Kib_Object = MibScalar
todayTxPpp0Kib = _TodayTxPpp0Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 3, 14),
    _TodayTxPpp0Kib_Type()
)
todayTxPpp0Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    todayTxPpp0Kib.setStatus("mandatory")
_TodayTotalPpp0Kib_Type = Integer32
_TodayTotalPpp0Kib_Object = MibScalar
todayTotalPpp0Kib = _TodayTotalPpp0Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 3, 15),
    _TodayTotalPpp0Kib_Type()
)
todayTotalPpp0Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    todayTotalPpp0Kib.setStatus("mandatory")
_YesterdayRxPpp0Kib_Type = Integer32
_YesterdayRxPpp0Kib_Object = MibScalar
yesterdayRxPpp0Kib = _YesterdayRxPpp0Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 3, 16),
    _YesterdayRxPpp0Kib_Type()
)
yesterdayRxPpp0Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    yesterdayRxPpp0Kib.setStatus("mandatory")
_YesterdayTxPpp0Kib_Type = Integer32
_YesterdayTxPpp0Kib_Object = MibScalar
yesterdayTxPpp0Kib = _YesterdayTxPpp0Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 3, 17),
    _YesterdayTxPpp0Kib_Type()
)
yesterdayTxPpp0Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    yesterdayTxPpp0Kib.setStatus("mandatory")
_YesterdayTotalPpp0Kib_Type = Integer32
_YesterdayTotalPpp0Kib_Object = MibScalar
yesterdayTotalPpp0Kib = _YesterdayTotalPpp0Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 3, 18),
    _YesterdayTotalPpp0Kib_Type()
)
yesterdayTotalPpp0Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    yesterdayTotalPpp0Kib.setStatus("mandatory")
_CurrMonthRxPpp0Kib_Type = Integer32
_CurrMonthRxPpp0Kib_Object = MibScalar
currMonthRxPpp0Kib = _CurrMonthRxPpp0Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 3, 19),
    _CurrMonthRxPpp0Kib_Type()
)
currMonthRxPpp0Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currMonthRxPpp0Kib.setStatus("mandatory")
_CurrMonthTxPpp0Kib_Type = Integer32
_CurrMonthTxPpp0Kib_Object = MibScalar
currMonthTxPpp0Kib = _CurrMonthTxPpp0Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 3, 20),
    _CurrMonthTxPpp0Kib_Type()
)
currMonthTxPpp0Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currMonthTxPpp0Kib.setStatus("mandatory")
_CurrMonthTotalPpp0Kib_Type = Integer32
_CurrMonthTotalPpp0Kib_Object = MibScalar
currMonthTotalPpp0Kib = _CurrMonthTotalPpp0Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 3, 21),
    _CurrMonthTotalPpp0Kib_Type()
)
currMonthTotalPpp0Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currMonthTotalPpp0Kib.setStatus("mandatory")
_PreMonthRxPpp0Kib_Type = Integer32
_PreMonthRxPpp0Kib_Object = MibScalar
preMonthRxPpp0Kib = _PreMonthRxPpp0Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 3, 22),
    _PreMonthRxPpp0Kib_Type()
)
preMonthRxPpp0Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    preMonthRxPpp0Kib.setStatus("mandatory")
_PreMonthTxPpp0Kib_Type = Integer32
_PreMonthTxPpp0Kib_Object = MibScalar
preMonthTxPpp0Kib = _PreMonthTxPpp0Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 3, 23),
    _PreMonthTxPpp0Kib_Type()
)
preMonthTxPpp0Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    preMonthTxPpp0Kib.setStatus("mandatory")
_PreMonthTotalPpp0Kib_Type = Integer32
_PreMonthTotalPpp0Kib_Object = MibScalar
preMonthTotalPpp0Kib = _PreMonthTotalPpp0Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 3, 24),
    _PreMonthTotalPpp0Kib_Type()
)
preMonthTotalPpp0Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    preMonthTotalPpp0Kib.setStatus("mandatory")
_Trafficwwan0_ObjectIdentity = ObjectIdentity
trafficwwan0 = _Trafficwwan0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1890, 1, 4)
)
_TodayRxWwan0_Type = DisplayString
_TodayRxWwan0_Object = MibScalar
todayRxWwan0 = _TodayRxWwan0_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 4, 1),
    _TodayRxWwan0_Type()
)
todayRxWwan0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    todayRxWwan0.setStatus("mandatory")
_TodayTxWwan0_Type = DisplayString
_TodayTxWwan0_Object = MibScalar
todayTxWwan0 = _TodayTxWwan0_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 4, 2),
    _TodayTxWwan0_Type()
)
todayTxWwan0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    todayTxWwan0.setStatus("mandatory")
_TodayTotalWwan0_Type = DisplayString
_TodayTotalWwan0_Object = MibScalar
todayTotalWwan0 = _TodayTotalWwan0_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 4, 3),
    _TodayTotalWwan0_Type()
)
todayTotalWwan0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    todayTotalWwan0.setStatus("mandatory")
_YesterdayRxWwan0_Type = DisplayString
_YesterdayRxWwan0_Object = MibScalar
yesterdayRxWwan0 = _YesterdayRxWwan0_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 4, 4),
    _YesterdayRxWwan0_Type()
)
yesterdayRxWwan0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    yesterdayRxWwan0.setStatus("mandatory")
_YesterdayTxWwan0_Type = DisplayString
_YesterdayTxWwan0_Object = MibScalar
yesterdayTxWwan0 = _YesterdayTxWwan0_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 4, 5),
    _YesterdayTxWwan0_Type()
)
yesterdayTxWwan0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    yesterdayTxWwan0.setStatus("mandatory")
_YesterdayTotalWwan0_Type = DisplayString
_YesterdayTotalWwan0_Object = MibScalar
yesterdayTotalWwan0 = _YesterdayTotalWwan0_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 4, 6),
    _YesterdayTotalWwan0_Type()
)
yesterdayTotalWwan0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    yesterdayTotalWwan0.setStatus("mandatory")
_CurrMonthRxWwan0_Type = DisplayString
_CurrMonthRxWwan0_Object = MibScalar
currMonthRxWwan0 = _CurrMonthRxWwan0_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 4, 7),
    _CurrMonthRxWwan0_Type()
)
currMonthRxWwan0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currMonthRxWwan0.setStatus("mandatory")
_CurrMonthTxWwan0_Type = DisplayString
_CurrMonthTxWwan0_Object = MibScalar
currMonthTxWwan0 = _CurrMonthTxWwan0_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 4, 8),
    _CurrMonthTxWwan0_Type()
)
currMonthTxWwan0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currMonthTxWwan0.setStatus("mandatory")
_CurrMonthTotalWwan0_Type = DisplayString
_CurrMonthTotalWwan0_Object = MibScalar
currMonthTotalWwan0 = _CurrMonthTotalWwan0_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 4, 9),
    _CurrMonthTotalWwan0_Type()
)
currMonthTotalWwan0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currMonthTotalWwan0.setStatus("mandatory")
_PreMonthRxWwan0_Type = DisplayString
_PreMonthRxWwan0_Object = MibScalar
preMonthRxWwan0 = _PreMonthRxWwan0_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 4, 10),
    _PreMonthRxWwan0_Type()
)
preMonthRxWwan0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    preMonthRxWwan0.setStatus("mandatory")
_PreMonthTxWwan0_Type = DisplayString
_PreMonthTxWwan0_Object = MibScalar
preMonthTxWwan0 = _PreMonthTxWwan0_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 4, 11),
    _PreMonthTxWwan0_Type()
)
preMonthTxWwan0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    preMonthTxWwan0.setStatus("mandatory")
_PreMonthTotalWwan0_Type = DisplayString
_PreMonthTotalWwan0_Object = MibScalar
preMonthTotalWwan0 = _PreMonthTotalWwan0_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 4, 12),
    _PreMonthTotalWwan0_Type()
)
preMonthTotalWwan0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    preMonthTotalWwan0.setStatus("mandatory")
_TodayRxWwan0Kib_Type = Integer32
_TodayRxWwan0Kib_Object = MibScalar
todayRxWwan0Kib = _TodayRxWwan0Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 4, 13),
    _TodayRxWwan0Kib_Type()
)
todayRxWwan0Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    todayRxWwan0Kib.setStatus("mandatory")
_TodayTxWwan0Kib_Type = Integer32
_TodayTxWwan0Kib_Object = MibScalar
todayTxWwan0Kib = _TodayTxWwan0Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 4, 14),
    _TodayTxWwan0Kib_Type()
)
todayTxWwan0Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    todayTxWwan0Kib.setStatus("mandatory")
_TodayTotalWwan0Kib_Type = Integer32
_TodayTotalWwan0Kib_Object = MibScalar
todayTotalWwan0Kib = _TodayTotalWwan0Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 4, 15),
    _TodayTotalWwan0Kib_Type()
)
todayTotalWwan0Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    todayTotalWwan0Kib.setStatus("mandatory")
_YesterdayRxWwan0Kib_Type = Integer32
_YesterdayRxWwan0Kib_Object = MibScalar
yesterdayRxWwan0Kib = _YesterdayRxWwan0Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 4, 16),
    _YesterdayRxWwan0Kib_Type()
)
yesterdayRxWwan0Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    yesterdayRxWwan0Kib.setStatus("mandatory")
_YesterdayTxWwan0Kib_Type = Integer32
_YesterdayTxWwan0Kib_Object = MibScalar
yesterdayTxWwan0Kib = _YesterdayTxWwan0Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 4, 17),
    _YesterdayTxWwan0Kib_Type()
)
yesterdayTxWwan0Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    yesterdayTxWwan0Kib.setStatus("mandatory")
_YesterdayTotalWwan0Kib_Type = Integer32
_YesterdayTotalWwan0Kib_Object = MibScalar
yesterdayTotalWwan0Kib = _YesterdayTotalWwan0Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 4, 18),
    _YesterdayTotalWwan0Kib_Type()
)
yesterdayTotalWwan0Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    yesterdayTotalWwan0Kib.setStatus("mandatory")
_CurrMonthRxWwan0Kib_Type = Integer32
_CurrMonthRxWwan0Kib_Object = MibScalar
currMonthRxWwan0Kib = _CurrMonthRxWwan0Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 4, 19),
    _CurrMonthRxWwan0Kib_Type()
)
currMonthRxWwan0Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currMonthRxWwan0Kib.setStatus("mandatory")
_CurrMonthTxWwan0Kib_Type = Integer32
_CurrMonthTxWwan0Kib_Object = MibScalar
currMonthTxWwan0Kib = _CurrMonthTxWwan0Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 4, 20),
    _CurrMonthTxWwan0Kib_Type()
)
currMonthTxWwan0Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currMonthTxWwan0Kib.setStatus("mandatory")
_CurrMonthTotalWwan0Kib_Type = Integer32
_CurrMonthTotalWwan0Kib_Object = MibScalar
currMonthTotalWwan0Kib = _CurrMonthTotalWwan0Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 4, 21),
    _CurrMonthTotalWwan0Kib_Type()
)
currMonthTotalWwan0Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currMonthTotalWwan0Kib.setStatus("mandatory")
_PreMonthRxWwan0Kib_Type = Integer32
_PreMonthRxWwan0Kib_Object = MibScalar
preMonthRxWwan0Kib = _PreMonthRxWwan0Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 4, 22),
    _PreMonthRxWwan0Kib_Type()
)
preMonthRxWwan0Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    preMonthRxWwan0Kib.setStatus("mandatory")
_PreMonthTxWwan0Kib_Type = Integer32
_PreMonthTxWwan0Kib_Object = MibScalar
preMonthTxWwan0Kib = _PreMonthTxWwan0Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 4, 23),
    _PreMonthTxWwan0Kib_Type()
)
preMonthTxWwan0Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    preMonthTxWwan0Kib.setStatus("mandatory")
_PreMonthTotalWwan0Kib_Type = Integer32
_PreMonthTotalWwan0Kib_Object = MibScalar
preMonthTotalWwan0Kib = _PreMonthTotalWwan0Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 4, 24),
    _PreMonthTotalWwan0Kib_Type()
)
preMonthTotalWwan0Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    preMonthTotalWwan0Kib.setStatus("mandatory")
_Trafficeth0_ObjectIdentity = ObjectIdentity
trafficeth0 = _Trafficeth0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1890, 1, 5)
)
_TodayRxEth0_Type = DisplayString
_TodayRxEth0_Object = MibScalar
todayRxEth0 = _TodayRxEth0_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 5, 1),
    _TodayRxEth0_Type()
)
todayRxEth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    todayRxEth0.setStatus("mandatory")
_TodayTxEth0_Type = DisplayString
_TodayTxEth0_Object = MibScalar
todayTxEth0 = _TodayTxEth0_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 5, 2),
    _TodayTxEth0_Type()
)
todayTxEth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    todayTxEth0.setStatus("mandatory")
_TodayTotalEth0_Type = DisplayString
_TodayTotalEth0_Object = MibScalar
todayTotalEth0 = _TodayTotalEth0_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 5, 3),
    _TodayTotalEth0_Type()
)
todayTotalEth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    todayTotalEth0.setStatus("mandatory")
_YesterdayRxEth0_Type = DisplayString
_YesterdayRxEth0_Object = MibScalar
yesterdayRxEth0 = _YesterdayRxEth0_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 5, 4),
    _YesterdayRxEth0_Type()
)
yesterdayRxEth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    yesterdayRxEth0.setStatus("mandatory")
_YesterdayTxEth0_Type = DisplayString
_YesterdayTxEth0_Object = MibScalar
yesterdayTxEth0 = _YesterdayTxEth0_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 5, 5),
    _YesterdayTxEth0_Type()
)
yesterdayTxEth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    yesterdayTxEth0.setStatus("mandatory")
_YesterdayTotalEth0_Type = DisplayString
_YesterdayTotalEth0_Object = MibScalar
yesterdayTotalEth0 = _YesterdayTotalEth0_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 5, 6),
    _YesterdayTotalEth0_Type()
)
yesterdayTotalEth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    yesterdayTotalEth0.setStatus("mandatory")
_CurrMonthRxEth0_Type = DisplayString
_CurrMonthRxEth0_Object = MibScalar
currMonthRxEth0 = _CurrMonthRxEth0_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 5, 7),
    _CurrMonthRxEth0_Type()
)
currMonthRxEth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currMonthRxEth0.setStatus("mandatory")
_CurrMonthTxEth0_Type = DisplayString
_CurrMonthTxEth0_Object = MibScalar
currMonthTxEth0 = _CurrMonthTxEth0_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 5, 8),
    _CurrMonthTxEth0_Type()
)
currMonthTxEth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currMonthTxEth0.setStatus("mandatory")
_CurrMonthTotalEth0_Type = DisplayString
_CurrMonthTotalEth0_Object = MibScalar
currMonthTotalEth0 = _CurrMonthTotalEth0_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 5, 9),
    _CurrMonthTotalEth0_Type()
)
currMonthTotalEth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currMonthTotalEth0.setStatus("mandatory")
_PreMonthRxEth0_Type = DisplayString
_PreMonthRxEth0_Object = MibScalar
preMonthRxEth0 = _PreMonthRxEth0_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 5, 10),
    _PreMonthRxEth0_Type()
)
preMonthRxEth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    preMonthRxEth0.setStatus("mandatory")
_PreMonthTxEth0_Type = DisplayString
_PreMonthTxEth0_Object = MibScalar
preMonthTxEth0 = _PreMonthTxEth0_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 5, 11),
    _PreMonthTxEth0_Type()
)
preMonthTxEth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    preMonthTxEth0.setStatus("mandatory")
_PreMonthTotalEth0_Type = DisplayString
_PreMonthTotalEth0_Object = MibScalar
preMonthTotalEth0 = _PreMonthTotalEth0_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 5, 12),
    _PreMonthTotalEth0_Type()
)
preMonthTotalEth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    preMonthTotalEth0.setStatus("mandatory")
_TodayRxEth0Kib_Type = Integer32
_TodayRxEth0Kib_Object = MibScalar
todayRxEth0Kib = _TodayRxEth0Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 5, 13),
    _TodayRxEth0Kib_Type()
)
todayRxEth0Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    todayRxEth0Kib.setStatus("mandatory")
_TodayTxEth0Kib_Type = Integer32
_TodayTxEth0Kib_Object = MibScalar
todayTxEth0Kib = _TodayTxEth0Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 5, 14),
    _TodayTxEth0Kib_Type()
)
todayTxEth0Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    todayTxEth0Kib.setStatus("mandatory")
_TodayTotalEth0Kib_Type = Integer32
_TodayTotalEth0Kib_Object = MibScalar
todayTotalEth0Kib = _TodayTotalEth0Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 5, 15),
    _TodayTotalEth0Kib_Type()
)
todayTotalEth0Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    todayTotalEth0Kib.setStatus("mandatory")
_YesterdayRxEth0Kib_Type = Integer32
_YesterdayRxEth0Kib_Object = MibScalar
yesterdayRxEth0Kib = _YesterdayRxEth0Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 5, 16),
    _YesterdayRxEth0Kib_Type()
)
yesterdayRxEth0Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    yesterdayRxEth0Kib.setStatus("mandatory")
_YesterdayTxEth0Kib_Type = Integer32
_YesterdayTxEth0Kib_Object = MibScalar
yesterdayTxEth0Kib = _YesterdayTxEth0Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 5, 17),
    _YesterdayTxEth0Kib_Type()
)
yesterdayTxEth0Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    yesterdayTxEth0Kib.setStatus("mandatory")
_YesterdayTotalEth0Kib_Type = Integer32
_YesterdayTotalEth0Kib_Object = MibScalar
yesterdayTotalEth0Kib = _YesterdayTotalEth0Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 5, 18),
    _YesterdayTotalEth0Kib_Type()
)
yesterdayTotalEth0Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    yesterdayTotalEth0Kib.setStatus("mandatory")
_CurrMonthRxEth0Kib_Type = Integer32
_CurrMonthRxEth0Kib_Object = MibScalar
currMonthRxEth0Kib = _CurrMonthRxEth0Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 5, 19),
    _CurrMonthRxEth0Kib_Type()
)
currMonthRxEth0Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currMonthRxEth0Kib.setStatus("mandatory")
_CurrMonthTxEth0Kib_Type = Integer32
_CurrMonthTxEth0Kib_Object = MibScalar
currMonthTxEth0Kib = _CurrMonthTxEth0Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 5, 20),
    _CurrMonthTxEth0Kib_Type()
)
currMonthTxEth0Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currMonthTxEth0Kib.setStatus("mandatory")
_CurrMonthTotalEth0Kib_Type = Integer32
_CurrMonthTotalEth0Kib_Object = MibScalar
currMonthTotalEth0Kib = _CurrMonthTotalEth0Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 5, 21),
    _CurrMonthTotalEth0Kib_Type()
)
currMonthTotalEth0Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currMonthTotalEth0Kib.setStatus("mandatory")
_PreMonthRxEth0Kib_Type = Integer32
_PreMonthRxEth0Kib_Object = MibScalar
preMonthRxEth0Kib = _PreMonthRxEth0Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 5, 22),
    _PreMonthRxEth0Kib_Type()
)
preMonthRxEth0Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    preMonthRxEth0Kib.setStatus("mandatory")
_PreMonthTxEth0Kib_Type = Integer32
_PreMonthTxEth0Kib_Object = MibScalar
preMonthTxEth0Kib = _PreMonthTxEth0Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 5, 23),
    _PreMonthTxEth0Kib_Type()
)
preMonthTxEth0Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    preMonthTxEth0Kib.setStatus("mandatory")
_PreMonthTotalEth0Kib_Type = Integer32
_PreMonthTotalEth0Kib_Object = MibScalar
preMonthTotalEth0Kib = _PreMonthTotalEth0Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 5, 24),
    _PreMonthTotalEth0Kib_Type()
)
preMonthTotalEth0Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    preMonthTotalEth0Kib.setStatus("mandatory")
_Trafficeth1_ObjectIdentity = ObjectIdentity
trafficeth1 = _Trafficeth1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1890, 1, 6)
)
_TodayRxEth1_Type = DisplayString
_TodayRxEth1_Object = MibScalar
todayRxEth1 = _TodayRxEth1_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 6, 1),
    _TodayRxEth1_Type()
)
todayRxEth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    todayRxEth1.setStatus("mandatory")
_TodayTxEth1_Type = DisplayString
_TodayTxEth1_Object = MibScalar
todayTxEth1 = _TodayTxEth1_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 6, 2),
    _TodayTxEth1_Type()
)
todayTxEth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    todayTxEth1.setStatus("mandatory")
_TodayTotalEth1_Type = DisplayString
_TodayTotalEth1_Object = MibScalar
todayTotalEth1 = _TodayTotalEth1_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 6, 3),
    _TodayTotalEth1_Type()
)
todayTotalEth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    todayTotalEth1.setStatus("mandatory")
_YesterdayRxEth1_Type = DisplayString
_YesterdayRxEth1_Object = MibScalar
yesterdayRxEth1 = _YesterdayRxEth1_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 6, 4),
    _YesterdayRxEth1_Type()
)
yesterdayRxEth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    yesterdayRxEth1.setStatus("mandatory")
_YesterdayTxEth1_Type = DisplayString
_YesterdayTxEth1_Object = MibScalar
yesterdayTxEth1 = _YesterdayTxEth1_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 6, 5),
    _YesterdayTxEth1_Type()
)
yesterdayTxEth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    yesterdayTxEth1.setStatus("mandatory")
_YesterdayTotalEth1_Type = DisplayString
_YesterdayTotalEth1_Object = MibScalar
yesterdayTotalEth1 = _YesterdayTotalEth1_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 6, 6),
    _YesterdayTotalEth1_Type()
)
yesterdayTotalEth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    yesterdayTotalEth1.setStatus("mandatory")
_CurrMonthRxEth1_Type = DisplayString
_CurrMonthRxEth1_Object = MibScalar
currMonthRxEth1 = _CurrMonthRxEth1_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 6, 7),
    _CurrMonthRxEth1_Type()
)
currMonthRxEth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currMonthRxEth1.setStatus("mandatory")
_CurrMonthTxEth1_Type = DisplayString
_CurrMonthTxEth1_Object = MibScalar
currMonthTxEth1 = _CurrMonthTxEth1_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 6, 8),
    _CurrMonthTxEth1_Type()
)
currMonthTxEth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currMonthTxEth1.setStatus("mandatory")
_CurrMonthTotalEth1_Type = DisplayString
_CurrMonthTotalEth1_Object = MibScalar
currMonthTotalEth1 = _CurrMonthTotalEth1_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 6, 9),
    _CurrMonthTotalEth1_Type()
)
currMonthTotalEth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currMonthTotalEth1.setStatus("mandatory")
_PreMonthRxEth1_Type = DisplayString
_PreMonthRxEth1_Object = MibScalar
preMonthRxEth1 = _PreMonthRxEth1_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 6, 10),
    _PreMonthRxEth1_Type()
)
preMonthRxEth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    preMonthRxEth1.setStatus("mandatory")
_PreMonthTxEth1_Type = DisplayString
_PreMonthTxEth1_Object = MibScalar
preMonthTxEth1 = _PreMonthTxEth1_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 6, 11),
    _PreMonthTxEth1_Type()
)
preMonthTxEth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    preMonthTxEth1.setStatus("mandatory")
_PreMonthTotalEth1_Type = DisplayString
_PreMonthTotalEth1_Object = MibScalar
preMonthTotalEth1 = _PreMonthTotalEth1_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 6, 12),
    _PreMonthTotalEth1_Type()
)
preMonthTotalEth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    preMonthTotalEth1.setStatus("mandatory")
_TodayRxEth1Kib_Type = Integer32
_TodayRxEth1Kib_Object = MibScalar
todayRxEth1Kib = _TodayRxEth1Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 6, 13),
    _TodayRxEth1Kib_Type()
)
todayRxEth1Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    todayRxEth1Kib.setStatus("mandatory")
_TodayTxEth1Kib_Type = Integer32
_TodayTxEth1Kib_Object = MibScalar
todayTxEth1Kib = _TodayTxEth1Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 6, 14),
    _TodayTxEth1Kib_Type()
)
todayTxEth1Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    todayTxEth1Kib.setStatus("mandatory")
_TodayTotalEth1Kib_Type = Integer32
_TodayTotalEth1Kib_Object = MibScalar
todayTotalEth1Kib = _TodayTotalEth1Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 6, 15),
    _TodayTotalEth1Kib_Type()
)
todayTotalEth1Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    todayTotalEth1Kib.setStatus("mandatory")
_YesterdayRxEth1Kib_Type = Integer32
_YesterdayRxEth1Kib_Object = MibScalar
yesterdayRxEth1Kib = _YesterdayRxEth1Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 6, 16),
    _YesterdayRxEth1Kib_Type()
)
yesterdayRxEth1Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    yesterdayRxEth1Kib.setStatus("mandatory")
_YesterdayTxEth1Kib_Type = Integer32
_YesterdayTxEth1Kib_Object = MibScalar
yesterdayTxEth1Kib = _YesterdayTxEth1Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 6, 17),
    _YesterdayTxEth1Kib_Type()
)
yesterdayTxEth1Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    yesterdayTxEth1Kib.setStatus("mandatory")
_YesterdayTotalEth1Kib_Type = Integer32
_YesterdayTotalEth1Kib_Object = MibScalar
yesterdayTotalEth1Kib = _YesterdayTotalEth1Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 6, 18),
    _YesterdayTotalEth1Kib_Type()
)
yesterdayTotalEth1Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    yesterdayTotalEth1Kib.setStatus("mandatory")
_CurrMonthRxEth1Kib_Type = Integer32
_CurrMonthRxEth1Kib_Object = MibScalar
currMonthRxEth1Kib = _CurrMonthRxEth1Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 6, 19),
    _CurrMonthRxEth1Kib_Type()
)
currMonthRxEth1Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currMonthRxEth1Kib.setStatus("mandatory")
_CurrMonthTxEth1Kib_Type = Integer32
_CurrMonthTxEth1Kib_Object = MibScalar
currMonthTxEth1Kib = _CurrMonthTxEth1Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 6, 20),
    _CurrMonthTxEth1Kib_Type()
)
currMonthTxEth1Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currMonthTxEth1Kib.setStatus("mandatory")
_CurrMonthTotalEth1Kib_Type = Integer32
_CurrMonthTotalEth1Kib_Object = MibScalar
currMonthTotalEth1Kib = _CurrMonthTotalEth1Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 6, 21),
    _CurrMonthTotalEth1Kib_Type()
)
currMonthTotalEth1Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currMonthTotalEth1Kib.setStatus("mandatory")
_PreMonthRxEth1Kib_Type = Integer32
_PreMonthRxEth1Kib_Object = MibScalar
preMonthRxEth1Kib = _PreMonthRxEth1Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 6, 22),
    _PreMonthRxEth1Kib_Type()
)
preMonthRxEth1Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    preMonthRxEth1Kib.setStatus("mandatory")
_PreMonthTxEth1Kib_Type = Integer32
_PreMonthTxEth1Kib_Object = MibScalar
preMonthTxEth1Kib = _PreMonthTxEth1Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 6, 23),
    _PreMonthTxEth1Kib_Type()
)
preMonthTxEth1Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    preMonthTxEth1Kib.setStatus("mandatory")
_PreMonthTotalEth1Kib_Type = Integer32
_PreMonthTotalEth1Kib_Object = MibScalar
preMonthTotalEth1Kib = _PreMonthTotalEth1Kib_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 6, 24),
    _PreMonthTotalEth1Kib_Type()
)
preMonthTotalEth1Kib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    preMonthTotalEth1Kib.setStatus("mandatory")
_Gpscurrent_ObjectIdentity = ObjectIdentity
gpscurrent = _Gpscurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1890, 1, 7)
)
_CurrentGpsValid_Type = DisplayString
_CurrentGpsValid_Object = MibScalar
currentGpsValid = _CurrentGpsValid_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 7, 1),
    _CurrentGpsValid_Type()
)
currentGpsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentGpsValid.setStatus("mandatory")
_CurrentGpsLat_Type = DisplayString
_CurrentGpsLat_Object = MibScalar
currentGpsLat = _CurrentGpsLat_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 7, 2),
    _CurrentGpsLat_Type()
)
currentGpsLat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentGpsLat.setStatus("mandatory")
_CurrentGpsLong_Type = DisplayString
_CurrentGpsLong_Object = MibScalar
currentGpsLong = _CurrentGpsLong_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 7, 3),
    _CurrentGpsLong_Type()
)
currentGpsLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentGpsLong.setStatus("mandatory")
_CurrentGpsAlt_Type = DisplayString
_CurrentGpsAlt_Object = MibScalar
currentGpsAlt = _CurrentGpsAlt_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 7, 4),
    _CurrentGpsAlt_Type()
)
currentGpsAlt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentGpsAlt.setStatus("mandatory")
_CurrentGpsTimeStamp_Type = DisplayString
_CurrentGpsTimeStamp_Object = MibScalar
currentGpsTimeStamp = _CurrentGpsTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 7, 5),
    _CurrentGpsTimeStamp_Type()
)
currentGpsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentGpsTimeStamp.setStatus("mandatory")
_CurrentGpsNumSat_Type = DisplayString
_CurrentGpsNumSat_Object = MibScalar
currentGpsNumSat = _CurrentGpsNumSat_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 7, 6),
    _CurrentGpsNumSat_Type()
)
currentGpsNumSat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentGpsNumSat.setStatus("mandatory")
_CurrentGpsFtfromcp_Type = DisplayString
_CurrentGpsFtfromcp_Object = MibScalar
currentGpsFtfromcp = _CurrentGpsFtfromcp_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 7, 7),
    _CurrentGpsFtfromcp_Type()
)
currentGpsFtfromcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentGpsFtfromcp.setStatus("mandatory")
_CurrentGpsSpeed_Type = DisplayString
_CurrentGpsSpeed_Object = MibScalar
currentGpsSpeed = _CurrentGpsSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 7, 8),
    _CurrentGpsSpeed_Type()
)
currentGpsSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentGpsSpeed.setStatus("mandatory")
_CurrentGpsCourse_Type = DisplayString
_CurrentGpsCourse_Object = MibScalar
currentGpsCourse = _CurrentGpsCourse_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 7, 9),
    _CurrentGpsCourse_Type()
)
currentGpsCourse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentGpsCourse.setStatus("mandatory")
_GpsSource_Type = DisplayString
_GpsSource_Object = MibScalar
gpsSource = _GpsSource_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 7, 10),
    _GpsSource_Type()
)
gpsSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsSource.setStatus("mandatory")
_GpsLockdownState_Type = DisplayString
_GpsLockdownState_Object = MibScalar
gpsLockdownState = _GpsLockdownState_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 7, 11),
    _GpsLockdownState_Type()
)
gpsLockdownState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsLockdownState.setStatus("mandatory")
_GpsLockdownRadius_Type = DisplayString
_GpsLockdownRadius_Object = MibScalar
gpsLockdownRadius = _GpsLockdownRadius_Object(
    (1, 3, 6, 1, 4, 1, 1890, 1, 7, 12),
    _GpsLockdownRadius_Type()
)
gpsLockdownRadius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsLockdownRadius.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RED-LION-RAM-MIB",
    **{"redlionram": redlionram,
       "system": system,
       "unitInfo": unitInfo,
       "unitDescription": unitDescription,
       "unitSerialNumber": unitSerialNumber,
       "unitFirmwareVersion": unitFirmwareVersion,
       "unitName": unitName,
       "cellular": cellular,
       "mdn": mdn,
       "minIMEI": minIMEI,
       "nai": nai,
       "sipUser": sipUser,
       "sid": sid,
       "nid": nid,
       "prl": prl,
       "activated": activated,
       "omaSupported": omaSupported,
       "currentMipProfile": currentMipProfile,
       "esn": esn,
       "pesn": pesn,
       "meid": meid,
       "vendor": vendor,
       "modelName": modelName,
       "fwVersion": fwVersion,
       "hwVersion": hwVersion,
       "carrier": carrier,
       "lowRssi": lowRssi,
       "lowEcio": lowEcio,
       "highRssi": highRssi,
       "highEcio": highEcio,
       "currentRssi": currentRssi,
       "currentEcio": currentEcio,
       "svcType": svcType,
       "currentChannel": currentChannel,
       "cdmaType": cdmaType,
       "hdrType": hdrType,
       "cdmaRoaming": cdmaRoaming,
       "hdrRoaming": hdrRoaming,
       "roaming": roaming,
       "currentState": currentState,
       "speedPref": speedPref,
       "roamPref": roamPref,
       "devName": devName,
       "ifName": ifName,
       "txCount": txCount,
       "rxCount": rxCount,
       "gprsState": gprsState,
       "rxLevel": rxLevel,
       "servingCell": servingCell,
       "rccState": rccState,
       "gsmChannel": gsmChannel,
       "psState": psState,
       "mode": mode,
       "temperature": temperature,
       "simContextApn0": simContextApn0,
       "simContextApn1": simContextApn1,
       "simStatus": simStatus,
       "serviceDomain": serviceDomain,
       "availServiceType": availServiceType,
       "wCdmaL1State": wCdmaL1State,
       "mmcsState": mmcsState,
       "gmmPsState": gmmPsState,
       "wCdmaChannel": wCdmaChannel,
       "wCdmaBand": wCdmaBand,
       "systemMode": systemMode,
       "powerOnTime": powerOnTime,
       "lowSpeedCsq": lowSpeedCsq,
       "highSpeedCsq": highSpeedCsq,
       "band": band,
       "imei": imei,
       "simId": simId,
       "carrPLMN": carrPLMN,
       "rxLevelC0": rxLevelC0,
       "rxLevelC1": rxLevelC1,
       "locAreaCode": locAreaCode,
       "lteBand": lteBand,
       "lteRxChan": lteRxChan,
       "lteTxChan": lteTxChan,
       "lteBW": lteBW,
       "lteRSRP": lteRSRP,
       "lteRSRQ": lteRSRQ,
       "lteTracAreaCode": lteTracAreaCode,
       "creg": creg,
       "cellularUpTime": cellularUpTime,
       "lteRSRPint": lteRSRPint,
       "lteRSRQint": lteRSRQint,
       "lteSINRint": lteSINRint,
       "trafficppp0": trafficppp0,
       "todayRxPpp0": todayRxPpp0,
       "todayTxPpp0": todayTxPpp0,
       "todayTotalPpp0": todayTotalPpp0,
       "yesterdayRxPpp0": yesterdayRxPpp0,
       "yesterdayTxPpp0": yesterdayTxPpp0,
       "yesterdayTotalPpp0": yesterdayTotalPpp0,
       "currMonthRxPpp0": currMonthRxPpp0,
       "currMonthTxPpp0": currMonthTxPpp0,
       "currMonthTotalPpp0": currMonthTotalPpp0,
       "preMonthRxPpp0": preMonthRxPpp0,
       "preMonthTxPpp0": preMonthTxPpp0,
       "preMonthTotalPpp0": preMonthTotalPpp0,
       "todayRxPpp0Kib": todayRxPpp0Kib,
       "todayTxPpp0Kib": todayTxPpp0Kib,
       "todayTotalPpp0Kib": todayTotalPpp0Kib,
       "yesterdayRxPpp0Kib": yesterdayRxPpp0Kib,
       "yesterdayTxPpp0Kib": yesterdayTxPpp0Kib,
       "yesterdayTotalPpp0Kib": yesterdayTotalPpp0Kib,
       "currMonthRxPpp0Kib": currMonthRxPpp0Kib,
       "currMonthTxPpp0Kib": currMonthTxPpp0Kib,
       "currMonthTotalPpp0Kib": currMonthTotalPpp0Kib,
       "preMonthRxPpp0Kib": preMonthRxPpp0Kib,
       "preMonthTxPpp0Kib": preMonthTxPpp0Kib,
       "preMonthTotalPpp0Kib": preMonthTotalPpp0Kib,
       "trafficwwan0": trafficwwan0,
       "todayRxWwan0": todayRxWwan0,
       "todayTxWwan0": todayTxWwan0,
       "todayTotalWwan0": todayTotalWwan0,
       "yesterdayRxWwan0": yesterdayRxWwan0,
       "yesterdayTxWwan0": yesterdayTxWwan0,
       "yesterdayTotalWwan0": yesterdayTotalWwan0,
       "currMonthRxWwan0": currMonthRxWwan0,
       "currMonthTxWwan0": currMonthTxWwan0,
       "currMonthTotalWwan0": currMonthTotalWwan0,
       "preMonthRxWwan0": preMonthRxWwan0,
       "preMonthTxWwan0": preMonthTxWwan0,
       "preMonthTotalWwan0": preMonthTotalWwan0,
       "todayRxWwan0Kib": todayRxWwan0Kib,
       "todayTxWwan0Kib": todayTxWwan0Kib,
       "todayTotalWwan0Kib": todayTotalWwan0Kib,
       "yesterdayRxWwan0Kib": yesterdayRxWwan0Kib,
       "yesterdayTxWwan0Kib": yesterdayTxWwan0Kib,
       "yesterdayTotalWwan0Kib": yesterdayTotalWwan0Kib,
       "currMonthRxWwan0Kib": currMonthRxWwan0Kib,
       "currMonthTxWwan0Kib": currMonthTxWwan0Kib,
       "currMonthTotalWwan0Kib": currMonthTotalWwan0Kib,
       "preMonthRxWwan0Kib": preMonthRxWwan0Kib,
       "preMonthTxWwan0Kib": preMonthTxWwan0Kib,
       "preMonthTotalWwan0Kib": preMonthTotalWwan0Kib,
       "trafficeth0": trafficeth0,
       "todayRxEth0": todayRxEth0,
       "todayTxEth0": todayTxEth0,
       "todayTotalEth0": todayTotalEth0,
       "yesterdayRxEth0": yesterdayRxEth0,
       "yesterdayTxEth0": yesterdayTxEth0,
       "yesterdayTotalEth0": yesterdayTotalEth0,
       "currMonthRxEth0": currMonthRxEth0,
       "currMonthTxEth0": currMonthTxEth0,
       "currMonthTotalEth0": currMonthTotalEth0,
       "preMonthRxEth0": preMonthRxEth0,
       "preMonthTxEth0": preMonthTxEth0,
       "preMonthTotalEth0": preMonthTotalEth0,
       "todayRxEth0Kib": todayRxEth0Kib,
       "todayTxEth0Kib": todayTxEth0Kib,
       "todayTotalEth0Kib": todayTotalEth0Kib,
       "yesterdayRxEth0Kib": yesterdayRxEth0Kib,
       "yesterdayTxEth0Kib": yesterdayTxEth0Kib,
       "yesterdayTotalEth0Kib": yesterdayTotalEth0Kib,
       "currMonthRxEth0Kib": currMonthRxEth0Kib,
       "currMonthTxEth0Kib": currMonthTxEth0Kib,
       "currMonthTotalEth0Kib": currMonthTotalEth0Kib,
       "preMonthRxEth0Kib": preMonthRxEth0Kib,
       "preMonthTxEth0Kib": preMonthTxEth0Kib,
       "preMonthTotalEth0Kib": preMonthTotalEth0Kib,
       "trafficeth1": trafficeth1,
       "todayRxEth1": todayRxEth1,
       "todayTxEth1": todayTxEth1,
       "todayTotalEth1": todayTotalEth1,
       "yesterdayRxEth1": yesterdayRxEth1,
       "yesterdayTxEth1": yesterdayTxEth1,
       "yesterdayTotalEth1": yesterdayTotalEth1,
       "currMonthRxEth1": currMonthRxEth1,
       "currMonthTxEth1": currMonthTxEth1,
       "currMonthTotalEth1": currMonthTotalEth1,
       "preMonthRxEth1": preMonthRxEth1,
       "preMonthTxEth1": preMonthTxEth1,
       "preMonthTotalEth1": preMonthTotalEth1,
       "todayRxEth1Kib": todayRxEth1Kib,
       "todayTxEth1Kib": todayTxEth1Kib,
       "todayTotalEth1Kib": todayTotalEth1Kib,
       "yesterdayRxEth1Kib": yesterdayRxEth1Kib,
       "yesterdayTxEth1Kib": yesterdayTxEth1Kib,
       "yesterdayTotalEth1Kib": yesterdayTotalEth1Kib,
       "currMonthRxEth1Kib": currMonthRxEth1Kib,
       "currMonthTxEth1Kib": currMonthTxEth1Kib,
       "currMonthTotalEth1Kib": currMonthTotalEth1Kib,
       "preMonthRxEth1Kib": preMonthRxEth1Kib,
       "preMonthTxEth1Kib": preMonthTxEth1Kib,
       "preMonthTotalEth1Kib": preMonthTotalEth1Kib,
       "gpscurrent": gpscurrent,
       "currentGpsValid": currentGpsValid,
       "currentGpsLat": currentGpsLat,
       "currentGpsLong": currentGpsLong,
       "currentGpsAlt": currentGpsAlt,
       "currentGpsTimeStamp": currentGpsTimeStamp,
       "currentGpsNumSat": currentGpsNumSat,
       "currentGpsFtfromcp": currentGpsFtfromcp,
       "currentGpsSpeed": currentGpsSpeed,
       "currentGpsCourse": currentGpsCourse,
       "gpsSource": gpsSource,
       "gpsLockdownState": gpsLockdownState,
       "gpsLockdownRadius": gpsLockdownRadius}
)
