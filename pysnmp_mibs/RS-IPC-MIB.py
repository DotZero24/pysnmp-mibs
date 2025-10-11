# SNMP MIB module (RS-IPC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raysharp/RS-IPC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:17:33 2025
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

rsIpcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 51159)
)
if mibBuilder.loadTexts:
    rsIpcMIB.setRevisions(
        ("2018-07-05 10:10",
         "2018-08-07 13:10")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsiEnterprises_ObjectIdentity = ObjectIdentity
rsiEnterprises = _RsiEnterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51159, 0)
)
_EpiInfoObjects_ObjectIdentity = ObjectIdentity
epiInfoObjects = _EpiInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51159, 0, 1)
)
_InfoEpi_Type = DisplayString
_InfoEpi_Object = MibScalar
infoEpi = _InfoEpi_Object(
    (1, 3, 6, 1, 4, 1, 51159, 0, 1, 1),
    _InfoEpi_Type()
)
infoEpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoEpi.setStatus("current")
_RsiSystemModules_ObjectIdentity = ObjectIdentity
rsiSystemModules = _RsiSystemModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51159, 1)
)
_SysInfoObjects_ObjectIdentity = ObjectIdentity
sysInfoObjects = _SysInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51159, 1, 1)
)
_InfoDevID_Type = DisplayString
_InfoDevID_Object = MibScalar
infoDevID = _InfoDevID_Object(
    (1, 3, 6, 1, 4, 1, 51159, 1, 1, 1),
    _InfoDevID_Type()
)
infoDevID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoDevID.setStatus("current")
_InfoDevName_Type = DisplayString
_InfoDevName_Object = MibScalar
infoDevName = _InfoDevName_Object(
    (1, 3, 6, 1, 4, 1, 51159, 1, 1, 2),
    _InfoDevName_Type()
)
infoDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoDevName.setStatus("current")
_InfoDevType_Type = DisplayString
_InfoDevType_Object = MibScalar
infoDevType = _InfoDevType_Object(
    (1, 3, 6, 1, 4, 1, 51159, 1, 1, 3),
    _InfoDevType_Type()
)
infoDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoDevType.setStatus("current")
_InfoHardwareVer_Type = DisplayString
_InfoHardwareVer_Object = MibScalar
infoHardwareVer = _InfoHardwareVer_Object(
    (1, 3, 6, 1, 4, 1, 51159, 1, 1, 4),
    _InfoHardwareVer_Type()
)
infoHardwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoHardwareVer.setStatus("current")
_InfoSoftwareVer_Type = DisplayString
_InfoSoftwareVer_Object = MibScalar
infoSoftwareVer = _InfoSoftwareVer_Object(
    (1, 3, 6, 1, 4, 1, 51159, 1, 1, 5),
    _InfoSoftwareVer_Type()
)
infoSoftwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoSoftwareVer.setStatus("current")
_InfoIEClientVer_Type = DisplayString
_InfoIEClientVer_Object = MibScalar
infoIEClientVer = _InfoIEClientVer_Object(
    (1, 3, 6, 1, 4, 1, 51159, 1, 1, 6),
    _InfoIEClientVer_Type()
)
infoIEClientVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoIEClientVer.setStatus("current")
_InfoMacAddress_Type = DisplayString
_InfoMacAddress_Object = MibScalar
infoMacAddress = _InfoMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 51159, 1, 1, 7),
    _InfoMacAddress_Type()
)
infoMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoMacAddress.setStatus("current")
_InfoMaxCHN_Type = Integer32
_InfoMaxCHN_Object = MibScalar
infoMaxCHN = _InfoMaxCHN_Object(
    (1, 3, 6, 1, 4, 1, 51159, 1, 1, 8),
    _InfoMaxCHN_Type()
)
infoMaxCHN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoMaxCHN.setStatus("current")
_SysGeneralObjects_ObjectIdentity = ObjectIdentity
sysGeneralObjects = _SysGeneralObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51159, 1, 2)
)
_GenSySTimeObjects_ObjectIdentity = ObjectIdentity
genSySTimeObjects = _GenSySTimeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51159, 1, 2, 1)
)
_SysDateFormat_Type = Integer32
_SysDateFormat_Object = MibScalar
sysDateFormat = _SysDateFormat_Object(
    (1, 3, 6, 1, 4, 1, 51159, 1, 2, 1, 1),
    _SysDateFormat_Type()
)
sysDateFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDateFormat.setStatus("current")
_SysTimeFormat_Type = Integer32
_SysTimeFormat_Object = MibScalar
sysTimeFormat = _SysTimeFormat_Object(
    (1, 3, 6, 1, 4, 1, 51159, 1, 2, 1, 2),
    _SysTimeFormat_Type()
)
sysTimeFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeFormat.setStatus("current")
_SysTimeYear_Type = Integer32
_SysTimeYear_Object = MibScalar
sysTimeYear = _SysTimeYear_Object(
    (1, 3, 6, 1, 4, 1, 51159, 1, 2, 1, 3),
    _SysTimeYear_Type()
)
sysTimeYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeYear.setStatus("current")
_SysTimeMonth_Type = Integer32
_SysTimeMonth_Object = MibScalar
sysTimeMonth = _SysTimeMonth_Object(
    (1, 3, 6, 1, 4, 1, 51159, 1, 2, 1, 4),
    _SysTimeMonth_Type()
)
sysTimeMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeMonth.setStatus("current")
_SysTimeDay_Type = Integer32
_SysTimeDay_Object = MibScalar
sysTimeDay = _SysTimeDay_Object(
    (1, 3, 6, 1, 4, 1, 51159, 1, 2, 1, 5),
    _SysTimeDay_Type()
)
sysTimeDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeDay.setStatus("current")
_SysTimeHour_Type = Integer32
_SysTimeHour_Object = MibScalar
sysTimeHour = _SysTimeHour_Object(
    (1, 3, 6, 1, 4, 1, 51159, 1, 2, 1, 6),
    _SysTimeHour_Type()
)
sysTimeHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeHour.setStatus("current")
_SysTimeMinute_Type = Integer32
_SysTimeMinute_Object = MibScalar
sysTimeMinute = _SysTimeMinute_Object(
    (1, 3, 6, 1, 4, 1, 51159, 1, 2, 1, 7),
    _SysTimeMinute_Type()
)
sysTimeMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeMinute.setStatus("current")
_SysTimeSecond_Type = Integer32
_SysTimeSecond_Object = MibScalar
sysTimeSecond = _SysTimeSecond_Object(
    (1, 3, 6, 1, 4, 1, 51159, 1, 2, 1, 8),
    _SysTimeSecond_Type()
)
sysTimeSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeSecond.setStatus("current")
_GenDstObjects_ObjectIdentity = ObjectIdentity
genDstObjects = _GenDstObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51159, 1, 2, 2)
)
_GenNtpObjects_ObjectIdentity = ObjectIdentity
genNtpObjects = _GenNtpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51159, 1, 2, 3)
)
_GenSyncObjects_ObjectIdentity = ObjectIdentity
genSyncObjects = _GenSyncObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51159, 1, 2, 4)
)
_SysUsersObjects_ObjectIdentity = ObjectIdentity
sysUsersObjects = _SysUsersObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51159, 1, 3)
)
_UserConfigObjects_ObjectIdentity = ObjectIdentity
userConfigObjects = _UserConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51159, 1, 3, 1)
)
_RsiDisplayModules_ObjectIdentity = ObjectIdentity
rsiDisplayModules = _RsiDisplayModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51159, 2)
)
_DisplayLiveObjects_ObjectIdentity = ObjectIdentity
displayLiveObjects = _DisplayLiveObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51159, 2, 1)
)
_LiveConfigObjects_ObjectIdentity = ObjectIdentity
liveConfigObjects = _LiveConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51159, 2, 1, 1)
)
_IpcName_Type = DisplayString
_IpcName_Object = MibScalar
ipcName = _IpcName_Object(
    (1, 3, 6, 1, 4, 1, 51159, 2, 1, 1, 1),
    _IpcName_Type()
)
ipcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipcName.setStatus("current")
_FlickerCtrl_Type = DisplayString
_FlickerCtrl_Object = MibScalar
flickerCtrl = _FlickerCtrl_Object(
    (1, 3, 6, 1, 4, 1, 51159, 2, 1, 1, 2),
    _FlickerCtrl_Type()
)
flickerCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flickerCtrl.setStatus("current")
_OsdTransparency_Type = Integer32
_OsdTransparency_Object = MibScalar
osdTransparency = _OsdTransparency_Object(
    (1, 3, 6, 1, 4, 1, 51159, 2, 1, 1, 3),
    _OsdTransparency_Type()
)
osdTransparency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osdTransparency.setStatus("current")
_OsdShowName_Type = DisplayString
_OsdShowName_Object = MibScalar
osdShowName = _OsdShowName_Object(
    (1, 3, 6, 1, 4, 1, 51159, 2, 1, 1, 4),
    _OsdShowName_Type()
)
osdShowName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osdShowName.setStatus("current")
_OsdShowTime_Type = DisplayString
_OsdShowTime_Object = MibScalar
osdShowTime = _OsdShowTime_Object(
    (1, 3, 6, 1, 4, 1, 51159, 2, 1, 1, 5),
    _OsdShowTime_Type()
)
osdShowTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osdShowTime.setStatus("current")
_DisplayImageCtrlObjects_ObjectIdentity = ObjectIdentity
displayImageCtrlObjects = _DisplayImageCtrlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51159, 2, 2)
)
_DisplayPrivacyzoneObjects_ObjectIdentity = ObjectIdentity
displayPrivacyzoneObjects = _DisplayPrivacyzoneObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51159, 2, 3)
)
_DisplayROIObjects_ObjectIdentity = ObjectIdentity
displayROIObjects = _DisplayROIObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51159, 2, 4)
)
_RsiDeviceModules_ObjectIdentity = ObjectIdentity
rsiDeviceModules = _RsiDeviceModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51159, 3)
)
_DevHDDObjects_ObjectIdentity = ObjectIdentity
devHDDObjects = _DevHDDObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51159, 3, 1)
)
_HddStatus_Type = DisplayString
_HddStatus_Object = MibScalar
hddStatus = _HddStatus_Object(
    (1, 3, 6, 1, 4, 1, 51159, 3, 1, 1),
    _HddStatus_Type()
)
hddStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddStatus.setStatus("current")
_HddTotalSize_Type = DisplayString
_HddTotalSize_Object = MibScalar
hddTotalSize = _HddTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 51159, 3, 1, 2),
    _HddTotalSize_Type()
)
hddTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddTotalSize.setStatus("current")
_HddFreeSize_Type = DisplayString
_HddFreeSize_Object = MibScalar
hddFreeSize = _HddFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 51159, 3, 1, 3),
    _HddFreeSize_Type()
)
hddFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddFreeSize.setStatus("current")
_HddFreeTime_Type = DisplayString
_HddFreeTime_Object = MibScalar
hddFreeTime = _HddFreeTime_Object(
    (1, 3, 6, 1, 4, 1, 51159, 3, 1, 4),
    _HddFreeTime_Type()
)
hddFreeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddFreeTime.setStatus("current")
_HddOverWrite_Type = Integer32
_HddOverWrite_Object = MibScalar
hddOverWrite = _HddOverWrite_Object(
    (1, 3, 6, 1, 4, 1, 51159, 3, 1, 5),
    _HddOverWrite_Type()
)
hddOverWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hddOverWrite.setStatus("current")
_HddOWPeriod_Type = Integer32
_HddOWPeriod_Object = MibScalar
hddOWPeriod = _HddOWPeriod_Object(
    (1, 3, 6, 1, 4, 1, 51159, 3, 1, 6),
    _HddOWPeriod_Type()
)
hddOWPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hddOWPeriod.setStatus("current")
_HddRedundancy_Type = DisplayString
_HddRedundancy_Object = MibScalar
hddRedundancy = _HddRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 51159, 3, 1, 7),
    _HddRedundancy_Type()
)
hddRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hddRedundancy.setStatus("current")
_HddMaxNum_Type = Integer32
_HddMaxNum_Object = MibScalar
hddMaxNum = _HddMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 51159, 3, 1, 8),
    _HddMaxNum_Type()
)
hddMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddMaxNum.setStatus("current")
_DevAudioObjects_ObjectIdentity = ObjectIdentity
devAudioObjects = _DevAudioObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51159, 3, 2)
)
_DevLogObjects_ObjectIdentity = ObjectIdentity
devLogObjects = _DevLogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51159, 3, 3)
)
_DevCloudObjects_ObjectIdentity = ObjectIdentity
devCloudObjects = _DevCloudObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51159, 3, 4)
)
_RsiNetworkModules_ObjectIdentity = ObjectIdentity
rsiNetworkModules = _RsiNetworkModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51159, 4)
)
_NetConfigObjects_ObjectIdentity = ObjectIdentity
netConfigObjects = _NetConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51159, 4, 1)
)
_NetworkMode_Type = DisplayString
_NetworkMode_Object = MibScalar
networkMode = _NetworkMode_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 1, 1),
    _NetworkMode_Type()
)
networkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkMode.setStatus("current")
_NetClientPort_Type = Integer32
_NetClientPort_Object = MibScalar
netClientPort = _NetClientPort_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 1, 2),
    _NetClientPort_Type()
)
netClientPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netClientPort.setStatus("current")
_NetHttpPort_Type = Integer32
_NetHttpPort_Object = MibScalar
netHttpPort = _NetHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 1, 3),
    _NetHttpPort_Type()
)
netHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netHttpPort.setStatus("current")
_NetIPaddr_Type = DisplayString
_NetIPaddr_Object = MibScalar
netIPaddr = _NetIPaddr_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 1, 4),
    _NetIPaddr_Type()
)
netIPaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netIPaddr.setStatus("current")
_NetSubMask_Type = DisplayString
_NetSubMask_Object = MibScalar
netSubMask = _NetSubMask_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 1, 5),
    _NetSubMask_Type()
)
netSubMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netSubMask.setStatus("current")
_NetGateWay_Type = DisplayString
_NetGateWay_Object = MibScalar
netGateWay = _NetGateWay_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 1, 6),
    _NetGateWay_Type()
)
netGateWay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netGateWay.setStatus("current")
_NetDNS1_Type = DisplayString
_NetDNS1_Object = MibScalar
netDNS1 = _NetDNS1_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 1, 7),
    _NetDNS1_Type()
)
netDNS1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netDNS1.setStatus("current")
_NetDNS2_Type = DisplayString
_NetDNS2_Object = MibScalar
netDNS2 = _NetDNS2_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 1, 8),
    _NetDNS2_Type()
)
netDNS2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netDNS2.setStatus("current")
_NetPPPoEUserName_Type = DisplayString
_NetPPPoEUserName_Object = MibScalar
netPPPoEUserName = _NetPPPoEUserName_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 1, 9),
    _NetPPPoEUserName_Type()
)
netPPPoEUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netPPPoEUserName.setStatus("current")
_NetPPPoEPasswd_Type = DisplayString
_NetPPPoEPasswd_Object = MibScalar
netPPPoEPasswd = _NetPPPoEPasswd_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 1, 10),
    _NetPPPoEPasswd_Type()
)
netPPPoEPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netPPPoEPasswd.setStatus("current")
_VideoStreamObjects_ObjectIdentity = ObjectIdentity
videoStreamObjects = _VideoStreamObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51159, 4, 2)
)
_StreamMainObjects_ObjectIdentity = ObjectIdentity
streamMainObjects = _StreamMainObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51159, 4, 2, 1)
)
_MainReslution_Type = DisplayString
_MainReslution_Object = MibScalar
mainReslution = _MainReslution_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 2, 1, 1),
    _MainReslution_Type()
)
mainReslution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainReslution.setStatus("current")
_MainFps_Type = DisplayString
_MainFps_Object = MibScalar
mainFps = _MainFps_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 2, 1, 2),
    _MainFps_Type()
)
mainFps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainFps.setStatus("current")
_MainCodeType_Type = DisplayString
_MainCodeType_Object = MibScalar
mainCodeType = _MainCodeType_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 2, 1, 3),
    _MainCodeType_Type()
)
mainCodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainCodeType.setStatus("current")
_MainCodeLevel_Type = DisplayString
_MainCodeLevel_Object = MibScalar
mainCodeLevel = _MainCodeLevel_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 2, 1, 4),
    _MainCodeLevel_Type()
)
mainCodeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainCodeLevel.setStatus("current")
_MainBitrateCtrl_Type = DisplayString
_MainBitrateCtrl_Object = MibScalar
mainBitrateCtrl = _MainBitrateCtrl_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 2, 1, 5),
    _MainBitrateCtrl_Type()
)
mainBitrateCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainBitrateCtrl.setStatus("current")
_MainBitrateMode_Type = DisplayString
_MainBitrateMode_Object = MibScalar
mainBitrateMode = _MainBitrateMode_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 2, 1, 6),
    _MainBitrateMode_Type()
)
mainBitrateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainBitrateMode.setStatus("current")
_MainBitrate_Type = DisplayString
_MainBitrate_Object = MibScalar
mainBitrate = _MainBitrate_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 2, 1, 7),
    _MainBitrate_Type()
)
mainBitrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainBitrate.setStatus("current")
_MainIFI_Type = DisplayString
_MainIFI_Object = MibScalar
mainIFI = _MainIFI_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 2, 1, 8),
    _MainIFI_Type()
)
mainIFI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainIFI.setStatus("current")
_MainAudio_Type = DisplayString
_MainAudio_Object = MibScalar
mainAudio = _MainAudio_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 2, 1, 9),
    _MainAudio_Type()
)
mainAudio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainAudio.setStatus("current")
_StreamSubObjects_ObjectIdentity = ObjectIdentity
streamSubObjects = _StreamSubObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51159, 4, 2, 2)
)
_SubReslution_Type = DisplayString
_SubReslution_Object = MibScalar
subReslution = _SubReslution_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 2, 2, 1),
    _SubReslution_Type()
)
subReslution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subReslution.setStatus("current")
_SubFps_Type = DisplayString
_SubFps_Object = MibScalar
subFps = _SubFps_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 2, 2, 2),
    _SubFps_Type()
)
subFps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subFps.setStatus("current")
_SubCodeType_Type = DisplayString
_SubCodeType_Object = MibScalar
subCodeType = _SubCodeType_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 2, 2, 3),
    _SubCodeType_Type()
)
subCodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subCodeType.setStatus("current")
_SubCodeLevel_Type = DisplayString
_SubCodeLevel_Object = MibScalar
subCodeLevel = _SubCodeLevel_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 2, 2, 4),
    _SubCodeLevel_Type()
)
subCodeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subCodeLevel.setStatus("current")
_SubBitrateCtrl_Type = DisplayString
_SubBitrateCtrl_Object = MibScalar
subBitrateCtrl = _SubBitrateCtrl_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 2, 2, 5),
    _SubBitrateCtrl_Type()
)
subBitrateCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subBitrateCtrl.setStatus("current")
_SubBitrateMode_Type = DisplayString
_SubBitrateMode_Object = MibScalar
subBitrateMode = _SubBitrateMode_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 2, 2, 6),
    _SubBitrateMode_Type()
)
subBitrateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subBitrateMode.setStatus("current")
_SubBitrate_Type = DisplayString
_SubBitrate_Object = MibScalar
subBitrate = _SubBitrate_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 2, 2, 7),
    _SubBitrate_Type()
)
subBitrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subBitrate.setStatus("current")
_SubIFI_Type = DisplayString
_SubIFI_Object = MibScalar
subIFI = _SubIFI_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 2, 2, 8),
    _SubIFI_Type()
)
subIFI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subIFI.setStatus("current")
_SubAudio_Type = DisplayString
_SubAudio_Object = MibScalar
subAudio = _SubAudio_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 2, 2, 9),
    _SubAudio_Type()
)
subAudio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subAudio.setStatus("current")
_StreamMobileObjects_ObjectIdentity = ObjectIdentity
streamMobileObjects = _StreamMobileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51159, 4, 2, 3)
)
_MobileReslution_Type = DisplayString
_MobileReslution_Object = MibScalar
mobileReslution = _MobileReslution_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 2, 3, 1),
    _MobileReslution_Type()
)
mobileReslution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mobileReslution.setStatus("current")
_MobileFps_Type = DisplayString
_MobileFps_Object = MibScalar
mobileFps = _MobileFps_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 2, 3, 2),
    _MobileFps_Type()
)
mobileFps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mobileFps.setStatus("current")
_MobileCodeType_Type = DisplayString
_MobileCodeType_Object = MibScalar
mobileCodeType = _MobileCodeType_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 2, 3, 3),
    _MobileCodeType_Type()
)
mobileCodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mobileCodeType.setStatus("current")
_MobileCodeLevel_Type = DisplayString
_MobileCodeLevel_Object = MibScalar
mobileCodeLevel = _MobileCodeLevel_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 2, 3, 4),
    _MobileCodeLevel_Type()
)
mobileCodeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mobileCodeLevel.setStatus("current")
_MobileBitrateCtrl_Type = DisplayString
_MobileBitrateCtrl_Object = MibScalar
mobileBitrateCtrl = _MobileBitrateCtrl_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 2, 3, 5),
    _MobileBitrateCtrl_Type()
)
mobileBitrateCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mobileBitrateCtrl.setStatus("current")
_MobileBitrateMode_Type = DisplayString
_MobileBitrateMode_Object = MibScalar
mobileBitrateMode = _MobileBitrateMode_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 2, 3, 6),
    _MobileBitrateMode_Type()
)
mobileBitrateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mobileBitrateMode.setStatus("current")
_MobileBitrate_Type = DisplayString
_MobileBitrate_Object = MibScalar
mobileBitrate = _MobileBitrate_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 2, 3, 7),
    _MobileBitrate_Type()
)
mobileBitrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mobileBitrate.setStatus("current")
_MobileIFI_Type = DisplayString
_MobileIFI_Object = MibScalar
mobileIFI = _MobileIFI_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 2, 3, 8),
    _MobileIFI_Type()
)
mobileIFI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mobileIFI.setStatus("current")
_MobileAudio_Type = DisplayString
_MobileAudio_Object = MibScalar
mobileAudio = _MobileAudio_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 2, 3, 9),
    _MobileAudio_Type()
)
mobileAudio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mobileAudio.setStatus("current")
_MobileEnable_Type = DisplayString
_MobileEnable_Object = MibScalar
mobileEnable = _MobileEnable_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 2, 3, 10),
    _MobileEnable_Type()
)
mobileEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mobileEnable.setStatus("current")
_NetEmailObjects_ObjectIdentity = ObjectIdentity
netEmailObjects = _NetEmailObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51159, 4, 3)
)
_NetDDNSObjects_ObjectIdentity = ObjectIdentity
netDDNSObjects = _NetDDNSObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51159, 4, 4)
)
_NetIPFilterObjects_ObjectIdentity = ObjectIdentity
netIPFilterObjects = _NetIPFilterObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51159, 4, 5)
)
_NetRTSPObjects_ObjectIdentity = ObjectIdentity
netRTSPObjects = _NetRTSPObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51159, 4, 6)
)
_RtspEnable_Type = Integer32
_RtspEnable_Object = MibScalar
rtspEnable = _RtspEnable_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 6, 1),
    _RtspEnable_Type()
)
rtspEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtspEnable.setStatus("current")
_RtspPort_Type = Integer32
_RtspPort_Object = MibScalar
rtspPort = _RtspPort_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 6, 2),
    _RtspPort_Type()
)
rtspPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtspPort.setStatus("current")
_RtspAnonymous_Type = Integer32
_RtspAnonymous_Object = MibScalar
rtspAnonymous = _RtspAnonymous_Object(
    (1, 3, 6, 1, 4, 1, 51159, 4, 6, 3),
    _RtspAnonymous_Type()
)
rtspAnonymous.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtspAnonymous.setStatus("current")
_NetFTPObjects_ObjectIdentity = ObjectIdentity
netFTPObjects = _NetFTPObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51159, 4, 7)
)
_NetHTTPSObjects_ObjectIdentity = ObjectIdentity
netHTTPSObjects = _NetHTTPSObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51159, 4, 8)
)
_RsiAlarmModules_ObjectIdentity = ObjectIdentity
rsiAlarmModules = _RsiAlarmModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51159, 5)
)
_RsiAdvancedModules_ObjectIdentity = ObjectIdentity
rsiAdvancedModules = _RsiAdvancedModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51159, 6)
)
_RsiIntelligentModules_ObjectIdentity = ObjectIdentity
rsiIntelligentModules = _RsiIntelligentModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51159, 7)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RS-IPC-MIB",
    **{"rsIpcMIB": rsIpcMIB,
       "rsiEnterprises": rsiEnterprises,
       "epiInfoObjects": epiInfoObjects,
       "infoEpi": infoEpi,
       "rsiSystemModules": rsiSystemModules,
       "sysInfoObjects": sysInfoObjects,
       "infoDevID": infoDevID,
       "infoDevName": infoDevName,
       "infoDevType": infoDevType,
       "infoHardwareVer": infoHardwareVer,
       "infoSoftwareVer": infoSoftwareVer,
       "infoIEClientVer": infoIEClientVer,
       "infoMacAddress": infoMacAddress,
       "infoMaxCHN": infoMaxCHN,
       "sysGeneralObjects": sysGeneralObjects,
       "genSySTimeObjects": genSySTimeObjects,
       "sysDateFormat": sysDateFormat,
       "sysTimeFormat": sysTimeFormat,
       "sysTimeYear": sysTimeYear,
       "sysTimeMonth": sysTimeMonth,
       "sysTimeDay": sysTimeDay,
       "sysTimeHour": sysTimeHour,
       "sysTimeMinute": sysTimeMinute,
       "sysTimeSecond": sysTimeSecond,
       "genDstObjects": genDstObjects,
       "genNtpObjects": genNtpObjects,
       "genSyncObjects": genSyncObjects,
       "sysUsersObjects": sysUsersObjects,
       "userConfigObjects": userConfigObjects,
       "rsiDisplayModules": rsiDisplayModules,
       "displayLiveObjects": displayLiveObjects,
       "liveConfigObjects": liveConfigObjects,
       "ipcName": ipcName,
       "flickerCtrl": flickerCtrl,
       "osdTransparency": osdTransparency,
       "osdShowName": osdShowName,
       "osdShowTime": osdShowTime,
       "displayImageCtrlObjects": displayImageCtrlObjects,
       "displayPrivacyzoneObjects": displayPrivacyzoneObjects,
       "displayROIObjects": displayROIObjects,
       "rsiDeviceModules": rsiDeviceModules,
       "devHDDObjects": devHDDObjects,
       "hddStatus": hddStatus,
       "hddTotalSize": hddTotalSize,
       "hddFreeSize": hddFreeSize,
       "hddFreeTime": hddFreeTime,
       "hddOverWrite": hddOverWrite,
       "hddOWPeriod": hddOWPeriod,
       "hddRedundancy": hddRedundancy,
       "hddMaxNum": hddMaxNum,
       "devAudioObjects": devAudioObjects,
       "devLogObjects": devLogObjects,
       "devCloudObjects": devCloudObjects,
       "rsiNetworkModules": rsiNetworkModules,
       "netConfigObjects": netConfigObjects,
       "networkMode": networkMode,
       "netClientPort": netClientPort,
       "netHttpPort": netHttpPort,
       "netIPaddr": netIPaddr,
       "netSubMask": netSubMask,
       "netGateWay": netGateWay,
       "netDNS1": netDNS1,
       "netDNS2": netDNS2,
       "netPPPoEUserName": netPPPoEUserName,
       "netPPPoEPasswd": netPPPoEPasswd,
       "videoStreamObjects": videoStreamObjects,
       "streamMainObjects": streamMainObjects,
       "mainReslution": mainReslution,
       "mainFps": mainFps,
       "mainCodeType": mainCodeType,
       "mainCodeLevel": mainCodeLevel,
       "mainBitrateCtrl": mainBitrateCtrl,
       "mainBitrateMode": mainBitrateMode,
       "mainBitrate": mainBitrate,
       "mainIFI": mainIFI,
       "mainAudio": mainAudio,
       "streamSubObjects": streamSubObjects,
       "subReslution": subReslution,
       "subFps": subFps,
       "subCodeType": subCodeType,
       "subCodeLevel": subCodeLevel,
       "subBitrateCtrl": subBitrateCtrl,
       "subBitrateMode": subBitrateMode,
       "subBitrate": subBitrate,
       "subIFI": subIFI,
       "subAudio": subAudio,
       "streamMobileObjects": streamMobileObjects,
       "mobileReslution": mobileReslution,
       "mobileFps": mobileFps,
       "mobileCodeType": mobileCodeType,
       "mobileCodeLevel": mobileCodeLevel,
       "mobileBitrateCtrl": mobileBitrateCtrl,
       "mobileBitrateMode": mobileBitrateMode,
       "mobileBitrate": mobileBitrate,
       "mobileIFI": mobileIFI,
       "mobileAudio": mobileAudio,
       "mobileEnable": mobileEnable,
       "netEmailObjects": netEmailObjects,
       "netDDNSObjects": netDDNSObjects,
       "netIPFilterObjects": netIPFilterObjects,
       "netRTSPObjects": netRTSPObjects,
       "rtspEnable": rtspEnable,
       "rtspPort": rtspPort,
       "rtspAnonymous": rtspAnonymous,
       "netFTPObjects": netFTPObjects,
       "netHTTPSObjects": netHTTPSObjects,
       "rsiAlarmModules": rsiAlarmModules,
       "rsiAdvancedModules": rsiAdvancedModules,
       "rsiIntelligentModules": rsiIntelligentModules}
)
