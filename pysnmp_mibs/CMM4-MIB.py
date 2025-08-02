_Ac='accessLevel'
_Ab='userLoginName'
_Aa='cmm4SnmpAccessSubnet10'
_AZ='cmm4SnmpAccessSubnet9'
_AY='cmm4SnmpAccessSubnet8'
_AX='cmm4SnmpAccessSubnet7'
_AW='cmm4SnmpAccessSubnet6'
_AV='cmm4SnmpAccessSubnet5'
_AU='cmm4SnmpAccessSubnet4'
_AT='cmm4SnmpAccessSubnet3'
_AS='cmm4SnmpAccessSubnet2'
_AR='cmm4SnmpGPSSyncTrapEnable'
_AQ='cmm4SnmpReadOnly'
_AP='cmm4SnmpTrapIp10'
_AO='cmm4SnmpTrapIp9'
_AN='cmm4SnmpTrapIp8'
_AM='cmm4SnmpTrapIp7'
_AL='cmm4SnmpTrapIp6'
_AK='cmm4SnmpTrapIp5'
_AJ='cmm4SnmpTrapIp4'
_AI='cmm4SnmpTrapIp3'
_AH='cmm4SnmpTrapIp2'
_AG='cmm4SnmpTrapIp1'
_AF='cmm4SnmpAccessSubnet'
_AE='cmm4SnmpComString'
_AD='cmm4RebootIfRequired'
_AC='cmm4ClearEventLog'
_AB='cmm4Reboot'
_AA='gpsReInitCount'
_A9='gpsSyncMasterSlave'
_A8='gpsReceiverInfo'
_A7='gpsRestartCount'
_A6='gpsInvalidMsg'
_A5='gpsLongitude'
_A4='gpsLatitude'
_A3='gpsAntennaConnection'
_A2='gpsHeight'
_A1='gpsSatellitesTracked'
_A0='gpsSatellitesVisible'
_z='gpsTrackingMode'
_y='defaultStatus'
_x='cmm4FPGAPlatform'
_w='cmm4FPGAVersion'
_v='cmm4ExtEthPwrStat'
_u='syncStatus'
_t='trackingMode'
_s='height'
_r='longitude'
_q='latitude'
_p='satellitesTracked'
_o='satellitesVisible'
_n='cmm4UpTime'
_m='cmm4SystemTime'
_l='cmm4SoftwareVersion'
_k='cmm4pldVersion'
_j='deviceType'
_i='cmm4PortPowerStatus'
_h='siteInfoViewable'
_g='managementVID'
_f='vlanEnable'
_e='sessionTimeout'
_d='cmm4NTPServerIp'
_c='cmm4MgmtPortSpeed'
_b='cmm4IpAccess3'
_a='cmm4IpAccess2'
_Z='cmm4IpAccess1'
_Y='cmm4IpAccessFilter'
_X='cmm4ExtEthPowerReset'
_W='cmm4WebAutoUpdate'
_V='defaultGateway'
_U='lan1SubnetMask'
_T='lan1Ip'
_S='gpsTimingPulse'
_R='cmm4PortResetCfg'
_Q='cmm4PortPowerCfg'
_P='cmm4PortDevType'
_O='cmm4PortText'
_N='enable'
_M='disable'
_L='entryIndex'
_K='portStatusIndex'
_J='portCfgIndex'
_I='gpsSyncStatus'
_H='cmm4MacAddress'
_G='on'
_F='off'
_E='Integer32'
_D='read-only'
_C='read-write'
_B='CMM4-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
whispBox,whispCMM4,whispModules=mibBuilder.importSymbols('WHISP-GLOBAL-REG-MIB','whispBox','whispCMM4','whispModules')
EventString,WhispLUID,WhispMACAddress=mibBuilder.importSymbols('WHISP-TCV2-MIB','EventString','WhispLUID','WhispMACAddress')
cmm4MibModule=ModuleIdentity((1,3,6,1,4,1,161,19,1,1,15))
_Cmm4Groups_ObjectIdentity=ObjectIdentity
cmm4Groups=_Cmm4Groups_ObjectIdentity((1,3,6,1,4,1,161,19,3,6,1))
_Cmm4Config_ObjectIdentity=ObjectIdentity
cmm4Config=_Cmm4Config_ObjectIdentity((1,3,6,1,4,1,161,19,3,6,2))
class _GpsTimingPulse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('slave',0),('master',1)))
_GpsTimingPulse_Type.__name__=_E
_GpsTimingPulse_Object=MibScalar
gpsTimingPulse=_GpsTimingPulse_Object((1,3,6,1,4,1,161,19,3,6,2,1),_GpsTimingPulse_Type())
gpsTimingPulse.setMaxAccess(_C)
if mibBuilder.loadTexts:gpsTimingPulse.setStatus(_A)
_Lan1Ip_Type=IpAddress
_Lan1Ip_Object=MibScalar
lan1Ip=_Lan1Ip_Object((1,3,6,1,4,1,161,19,3,6,2,2),_Lan1Ip_Type())
lan1Ip.setMaxAccess(_C)
if mibBuilder.loadTexts:lan1Ip.setStatus(_A)
_Lan1SubnetMask_Type=IpAddress
_Lan1SubnetMask_Object=MibScalar
lan1SubnetMask=_Lan1SubnetMask_Object((1,3,6,1,4,1,161,19,3,6,2,3),_Lan1SubnetMask_Type())
lan1SubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:lan1SubnetMask.setStatus(_A)
_DefaultGateway_Type=IpAddress
_DefaultGateway_Object=MibScalar
defaultGateway=_DefaultGateway_Object((1,3,6,1,4,1,161,19,3,6,2,4),_DefaultGateway_Type())
defaultGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:defaultGateway.setStatus(_A)
_Cmm4WebAutoUpdate_Type=Integer32
_Cmm4WebAutoUpdate_Object=MibScalar
cmm4WebAutoUpdate=_Cmm4WebAutoUpdate_Object((1,3,6,1,4,1,161,19,3,6,2,5),_Cmm4WebAutoUpdate_Type())
cmm4WebAutoUpdate.setMaxAccess(_C)
if mibBuilder.loadTexts:cmm4WebAutoUpdate.setStatus(_A)
if mibBuilder.loadTexts:cmm4WebAutoUpdate.setUnits('Seconds')
class _Cmm4ExtEthPowerReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_Cmm4ExtEthPowerReset_Type.__name__=_E
_Cmm4ExtEthPowerReset_Object=MibScalar
cmm4ExtEthPowerReset=_Cmm4ExtEthPowerReset_Object((1,3,6,1,4,1,161,19,3,6,2,6),_Cmm4ExtEthPowerReset_Type())
cmm4ExtEthPowerReset.setMaxAccess(_C)
if mibBuilder.loadTexts:cmm4ExtEthPowerReset.setStatus(_A)
_Cmm4PortCfgTable_Object=MibTable
cmm4PortCfgTable=_Cmm4PortCfgTable_Object((1,3,6,1,4,1,161,19,3,6,2,7))
if mibBuilder.loadTexts:cmm4PortCfgTable.setStatus(_A)
_Cmm4PortCfgEntry_Object=MibTableRow
cmm4PortCfgEntry=_Cmm4PortCfgEntry_Object((1,3,6,1,4,1,161,19,3,6,2,7,1))
cmm4PortCfgEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:cmm4PortCfgEntry.setStatus(_A)
class _PortCfgIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_PortCfgIndex_Type.__name__=_E
_PortCfgIndex_Object=MibTableColumn
portCfgIndex=_PortCfgIndex_Object((1,3,6,1,4,1,161,19,3,6,2,7,1,1),_PortCfgIndex_Type())
portCfgIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:portCfgIndex.setStatus(_A)
_Cmm4PortText_Type=DisplayString
_Cmm4PortText_Object=MibTableColumn
cmm4PortText=_Cmm4PortText_Object((1,3,6,1,4,1,161,19,3,6,2,7,1,2),_Cmm4PortText_Type())
cmm4PortText.setMaxAccess(_C)
if mibBuilder.loadTexts:cmm4PortText.setStatus(_A)
class _Cmm4PortDevType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('canopy',1),('canopy56V',2)))
_Cmm4PortDevType_Type.__name__=_E
_Cmm4PortDevType_Object=MibTableColumn
cmm4PortDevType=_Cmm4PortDevType_Object((1,3,6,1,4,1,161,19,3,6,2,7,1,3),_Cmm4PortDevType_Type())
cmm4PortDevType.setMaxAccess(_C)
if mibBuilder.loadTexts:cmm4PortDevType.setStatus(_A)
class _Cmm4PortPowerCfg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_Cmm4PortPowerCfg_Type.__name__=_E
_Cmm4PortPowerCfg_Object=MibTableColumn
cmm4PortPowerCfg=_Cmm4PortPowerCfg_Object((1,3,6,1,4,1,161,19,3,6,2,7,1,4),_Cmm4PortPowerCfg_Type())
cmm4PortPowerCfg.setMaxAccess(_C)
if mibBuilder.loadTexts:cmm4PortPowerCfg.setStatus(_A)
class _Cmm4PortResetCfg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('resetComplete',0),('resetPort',1)))
_Cmm4PortResetCfg_Type.__name__=_E
_Cmm4PortResetCfg_Object=MibTableColumn
cmm4PortResetCfg=_Cmm4PortResetCfg_Object((1,3,6,1,4,1,161,19,3,6,2,7,1,5),_Cmm4PortResetCfg_Type())
cmm4PortResetCfg.setMaxAccess(_C)
if mibBuilder.loadTexts:cmm4PortResetCfg.setStatus(_A)
class _Cmm4IpAccessFilter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_Cmm4IpAccessFilter_Type.__name__=_E
_Cmm4IpAccessFilter_Object=MibScalar
cmm4IpAccessFilter=_Cmm4IpAccessFilter_Object((1,3,6,1,4,1,161,19,3,6,2,8),_Cmm4IpAccessFilter_Type())
cmm4IpAccessFilter.setMaxAccess(_C)
if mibBuilder.loadTexts:cmm4IpAccessFilter.setStatus(_A)
_Cmm4IpAccess1_Type=IpAddress
_Cmm4IpAccess1_Object=MibScalar
cmm4IpAccess1=_Cmm4IpAccess1_Object((1,3,6,1,4,1,161,19,3,6,2,9),_Cmm4IpAccess1_Type())
cmm4IpAccess1.setMaxAccess(_C)
if mibBuilder.loadTexts:cmm4IpAccess1.setStatus(_A)
_Cmm4IpAccess2_Type=IpAddress
_Cmm4IpAccess2_Object=MibScalar
cmm4IpAccess2=_Cmm4IpAccess2_Object((1,3,6,1,4,1,161,19,3,6,2,10),_Cmm4IpAccess2_Type())
cmm4IpAccess2.setMaxAccess(_C)
if mibBuilder.loadTexts:cmm4IpAccess2.setStatus(_A)
_Cmm4IpAccess3_Type=IpAddress
_Cmm4IpAccess3_Object=MibScalar
cmm4IpAccess3=_Cmm4IpAccess3_Object((1,3,6,1,4,1,161,19,3,6,2,11),_Cmm4IpAccess3_Type())
cmm4IpAccess3.setMaxAccess(_C)
if mibBuilder.loadTexts:cmm4IpAccess3.setStatus(_A)
class _Cmm4MgmtPortSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('autoNegotiate',1),('force10Half',2),('force10Full',3),('force100Half',4),('force100Full',5)))
_Cmm4MgmtPortSpeed_Type.__name__=_E
_Cmm4MgmtPortSpeed_Object=MibScalar
cmm4MgmtPortSpeed=_Cmm4MgmtPortSpeed_Object((1,3,6,1,4,1,161,19,3,6,2,12),_Cmm4MgmtPortSpeed_Type())
cmm4MgmtPortSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:cmm4MgmtPortSpeed.setStatus(_A)
_Cmm4NTPServerIp_Type=IpAddress
_Cmm4NTPServerIp_Object=MibScalar
cmm4NTPServerIp=_Cmm4NTPServerIp_Object((1,3,6,1,4,1,161,19,3,6,2,13),_Cmm4NTPServerIp_Type())
cmm4NTPServerIp.setMaxAccess(_C)
if mibBuilder.loadTexts:cmm4NTPServerIp.setStatus(_A)
_SessionTimeout_Type=Integer32
_SessionTimeout_Object=MibScalar
sessionTimeout=_SessionTimeout_Object((1,3,6,1,4,1,161,19,3,6,2,14),_SessionTimeout_Type())
sessionTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:sessionTimeout.setStatus(_A)
class _VlanEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),(_N,1)))
_VlanEnable_Type.__name__=_E
_VlanEnable_Object=MibScalar
vlanEnable=_VlanEnable_Object((1,3,6,1,4,1,161,19,3,6,2,15),_VlanEnable_Type())
vlanEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanEnable.setStatus(_A)
class _ManagementVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ManagementVID_Type.__name__=_E
_ManagementVID_Object=MibScalar
managementVID=_ManagementVID_Object((1,3,6,1,4,1,161,19,3,6,2,16),_ManagementVID_Type())
managementVID.setMaxAccess(_C)
if mibBuilder.loadTexts:managementVID.setStatus(_A)
class _SiteInfoViewable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),(_N,1)))
_SiteInfoViewable_Type.__name__=_E
_SiteInfoViewable_Object=MibScalar
siteInfoViewable=_SiteInfoViewable_Object((1,3,6,1,4,1,161,19,3,6,2,17),_SiteInfoViewable_Type())
siteInfoViewable.setMaxAccess(_C)
if mibBuilder.loadTexts:siteInfoViewable.setStatus(_A)
_Cmm4Status_ObjectIdentity=ObjectIdentity
cmm4Status=_Cmm4Status_ObjectIdentity((1,3,6,1,4,1,161,19,3,6,3))
_Cmm4PortStatusTable_Object=MibTable
cmm4PortStatusTable=_Cmm4PortStatusTable_Object((1,3,6,1,4,1,161,19,3,6,3,1))
if mibBuilder.loadTexts:cmm4PortStatusTable.setStatus(_A)
_Cmm4PortStatusEntry_Object=MibTableRow
cmm4PortStatusEntry=_Cmm4PortStatusEntry_Object((1,3,6,1,4,1,161,19,3,6,3,1,1))
cmm4PortStatusEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:cmm4PortStatusEntry.setStatus(_A)
class _PortStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_PortStatusIndex_Type.__name__=_E
_PortStatusIndex_Object=MibTableColumn
portStatusIndex=_PortStatusIndex_Object((1,3,6,1,4,1,161,19,3,6,3,1,1,1),_PortStatusIndex_Type())
portStatusIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:portStatusIndex.setStatus(_A)
class _Cmm4PortPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1)));namedValues=NamedValues(*(('powerOverEthernetFault',-1),(_F,0),(_G,1)))
_Cmm4PortPowerStatus_Type.__name__=_E
_Cmm4PortPowerStatus_Object=MibTableColumn
cmm4PortPowerStatus=_Cmm4PortPowerStatus_Object((1,3,6,1,4,1,161,19,3,6,3,1,1,4),_Cmm4PortPowerStatus_Type())
cmm4PortPowerStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cmm4PortPowerStatus.setStatus(_A)
_DeviceType_Type=DisplayString
_DeviceType_Object=MibScalar
deviceType=_DeviceType_Object((1,3,6,1,4,1,161,19,3,6,3,2),_DeviceType_Type())
deviceType.setMaxAccess(_D)
if mibBuilder.loadTexts:deviceType.setStatus(_A)
_Cmm4pldVersion_Type=DisplayString
_Cmm4pldVersion_Object=MibScalar
cmm4pldVersion=_Cmm4pldVersion_Object((1,3,6,1,4,1,161,19,3,6,3,3),_Cmm4pldVersion_Type())
cmm4pldVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:cmm4pldVersion.setStatus(_A)
_Cmm4SoftwareVersion_Type=DisplayString
_Cmm4SoftwareVersion_Object=MibScalar
cmm4SoftwareVersion=_Cmm4SoftwareVersion_Object((1,3,6,1,4,1,161,19,3,6,3,4),_Cmm4SoftwareVersion_Type())
cmm4SoftwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:cmm4SoftwareVersion.setStatus(_A)
_Cmm4SystemTime_Type=DisplayString
_Cmm4SystemTime_Object=MibScalar
cmm4SystemTime=_Cmm4SystemTime_Object((1,3,6,1,4,1,161,19,3,6,3,5),_Cmm4SystemTime_Type())
cmm4SystemTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cmm4SystemTime.setStatus(_A)
_Cmm4UpTime_Type=DisplayString
_Cmm4UpTime_Object=MibScalar
cmm4UpTime=_Cmm4UpTime_Object((1,3,6,1,4,1,161,19,3,6,3,6),_Cmm4UpTime_Type())
cmm4UpTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cmm4UpTime.setStatus(_A)
_SatellitesVisible_Type=DisplayString
_SatellitesVisible_Object=MibScalar
satellitesVisible=_SatellitesVisible_Object((1,3,6,1,4,1,161,19,3,6,3,7),_SatellitesVisible_Type())
satellitesVisible.setMaxAccess(_D)
if mibBuilder.loadTexts:satellitesVisible.setStatus(_A)
_SatellitesTracked_Type=DisplayString
_SatellitesTracked_Object=MibScalar
satellitesTracked=_SatellitesTracked_Object((1,3,6,1,4,1,161,19,3,6,3,8),_SatellitesTracked_Type())
satellitesTracked.setMaxAccess(_D)
if mibBuilder.loadTexts:satellitesTracked.setStatus(_A)
_Latitude_Type=DisplayString
_Latitude_Object=MibScalar
latitude=_Latitude_Object((1,3,6,1,4,1,161,19,3,6,3,9),_Latitude_Type())
latitude.setMaxAccess(_D)
if mibBuilder.loadTexts:latitude.setStatus(_A)
_Longitude_Type=DisplayString
_Longitude_Object=MibScalar
longitude=_Longitude_Object((1,3,6,1,4,1,161,19,3,6,3,10),_Longitude_Type())
longitude.setMaxAccess(_D)
if mibBuilder.loadTexts:longitude.setStatus(_A)
_Height_Type=DisplayString
_Height_Object=MibScalar
height=_Height_Object((1,3,6,1,4,1,161,19,3,6,3,11),_Height_Type())
height.setMaxAccess(_D)
if mibBuilder.loadTexts:height.setStatus(_A)
_TrackingMode_Type=DisplayString
_TrackingMode_Object=MibScalar
trackingMode=_TrackingMode_Object((1,3,6,1,4,1,161,19,3,6,3,12),_TrackingMode_Type())
trackingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:trackingMode.setStatus(_A)
_SyncStatus_Type=DisplayString
_SyncStatus_Object=MibScalar
syncStatus=_SyncStatus_Object((1,3,6,1,4,1,161,19,3,6,3,13),_SyncStatus_Type())
syncStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:syncStatus.setStatus(_A)
_Cmm4MacAddress_Type=WhispMACAddress
_Cmm4MacAddress_Object=MibScalar
cmm4MacAddress=_Cmm4MacAddress_Object((1,3,6,1,4,1,161,19,3,6,3,14),_Cmm4MacAddress_Type())
cmm4MacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cmm4MacAddress.setStatus(_A)
class _Cmm4ExtEthPwrStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_Cmm4ExtEthPwrStat_Type.__name__=_E
_Cmm4ExtEthPwrStat_Object=MibScalar
cmm4ExtEthPwrStat=_Cmm4ExtEthPwrStat_Object((1,3,6,1,4,1,161,19,3,6,3,15),_Cmm4ExtEthPwrStat_Type())
cmm4ExtEthPwrStat.setMaxAccess(_D)
if mibBuilder.loadTexts:cmm4ExtEthPwrStat.setStatus(_A)
_Cmm4FPGAVersion_Type=DisplayString
_Cmm4FPGAVersion_Object=MibScalar
cmm4FPGAVersion=_Cmm4FPGAVersion_Object((1,3,6,1,4,1,161,19,3,6,3,16),_Cmm4FPGAVersion_Type())
cmm4FPGAVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:cmm4FPGAVersion.setStatus(_A)
_Cmm4FPGAPlatform_Type=DisplayString
_Cmm4FPGAPlatform_Object=MibScalar
cmm4FPGAPlatform=_Cmm4FPGAPlatform_Object((1,3,6,1,4,1,161,19,3,6,3,17),_Cmm4FPGAPlatform_Type())
cmm4FPGAPlatform.setMaxAccess(_D)
if mibBuilder.loadTexts:cmm4FPGAPlatform.setStatus(_A)
class _DefaultStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('defaultPlugInserted',1),('defaultSwitchActive',2),('defaultPlugInsertedAndDefaultSwitchActive',3)))
_DefaultStatus_Type.__name__=_E
_DefaultStatus_Object=MibScalar
defaultStatus=_DefaultStatus_Object((1,3,6,1,4,1,161,19,3,6,3,18),_DefaultStatus_Type())
defaultStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultStatus.setStatus(_A)
_Cmm4Gps_ObjectIdentity=ObjectIdentity
cmm4Gps=_Cmm4Gps_ObjectIdentity((1,3,6,1,4,1,161,19,3,6,4))
_GpsTrackingMode_Type=DisplayString
_GpsTrackingMode_Object=MibScalar
gpsTrackingMode=_GpsTrackingMode_Object((1,3,6,1,4,1,161,19,3,6,4,1),_GpsTrackingMode_Type())
gpsTrackingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:gpsTrackingMode.setStatus(_A)
_GpsTime_Type=DisplayString
_GpsTime_Object=MibScalar
gpsTime=_GpsTime_Object((1,3,6,1,4,1,161,19,3,6,4,2),_GpsTime_Type())
gpsTime.setMaxAccess(_D)
if mibBuilder.loadTexts:gpsTime.setStatus(_A)
_GpsDate_Type=DisplayString
_GpsDate_Object=MibScalar
gpsDate=_GpsDate_Object((1,3,6,1,4,1,161,19,3,6,4,3),_GpsDate_Type())
gpsDate.setMaxAccess(_D)
if mibBuilder.loadTexts:gpsDate.setStatus(_A)
_GpsSatellitesVisible_Type=DisplayString
_GpsSatellitesVisible_Object=MibScalar
gpsSatellitesVisible=_GpsSatellitesVisible_Object((1,3,6,1,4,1,161,19,3,6,4,4),_GpsSatellitesVisible_Type())
gpsSatellitesVisible.setMaxAccess(_D)
if mibBuilder.loadTexts:gpsSatellitesVisible.setStatus(_A)
_GpsSatellitesTracked_Type=DisplayString
_GpsSatellitesTracked_Object=MibScalar
gpsSatellitesTracked=_GpsSatellitesTracked_Object((1,3,6,1,4,1,161,19,3,6,4,5),_GpsSatellitesTracked_Type())
gpsSatellitesTracked.setMaxAccess(_D)
if mibBuilder.loadTexts:gpsSatellitesTracked.setStatus(_A)
_GpsHeight_Type=DisplayString
_GpsHeight_Object=MibScalar
gpsHeight=_GpsHeight_Object((1,3,6,1,4,1,161,19,3,6,4,6),_GpsHeight_Type())
gpsHeight.setMaxAccess(_D)
if mibBuilder.loadTexts:gpsHeight.setStatus(_A)
_GpsAntennaConnection_Type=DisplayString
_GpsAntennaConnection_Object=MibScalar
gpsAntennaConnection=_GpsAntennaConnection_Object((1,3,6,1,4,1,161,19,3,6,4,7),_GpsAntennaConnection_Type())
gpsAntennaConnection.setMaxAccess(_D)
if mibBuilder.loadTexts:gpsAntennaConnection.setStatus(_A)
_GpsLatitude_Type=DisplayString
_GpsLatitude_Object=MibScalar
gpsLatitude=_GpsLatitude_Object((1,3,6,1,4,1,161,19,3,6,4,8),_GpsLatitude_Type())
gpsLatitude.setMaxAccess(_D)
if mibBuilder.loadTexts:gpsLatitude.setStatus(_A)
_GpsLongitude_Type=DisplayString
_GpsLongitude_Object=MibScalar
gpsLongitude=_GpsLongitude_Object((1,3,6,1,4,1,161,19,3,6,4,9),_GpsLongitude_Type())
gpsLongitude.setMaxAccess(_D)
if mibBuilder.loadTexts:gpsLongitude.setStatus(_A)
_GpsInvalidMsg_Type=DisplayString
_GpsInvalidMsg_Object=MibScalar
gpsInvalidMsg=_GpsInvalidMsg_Object((1,3,6,1,4,1,161,19,3,6,4,10),_GpsInvalidMsg_Type())
gpsInvalidMsg.setMaxAccess(_D)
if mibBuilder.loadTexts:gpsInvalidMsg.setStatus(_A)
_GpsRestartCount_Type=Integer32
_GpsRestartCount_Object=MibScalar
gpsRestartCount=_GpsRestartCount_Object((1,3,6,1,4,1,161,19,3,6,4,11),_GpsRestartCount_Type())
gpsRestartCount.setMaxAccess(_D)
if mibBuilder.loadTexts:gpsRestartCount.setStatus(_A)
_GpsReceiverInfo_Type=DisplayString
_GpsReceiverInfo_Object=MibScalar
gpsReceiverInfo=_GpsReceiverInfo_Object((1,3,6,1,4,1,161,19,3,6,4,12),_GpsReceiverInfo_Type())
gpsReceiverInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:gpsReceiverInfo.setStatus(_A)
class _GpsSyncStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('syncOK',1),('noSync',2)))
_GpsSyncStatus_Type.__name__=_E
_GpsSyncStatus_Object=MibScalar
gpsSyncStatus=_GpsSyncStatus_Object((1,3,6,1,4,1,161,19,3,6,4,13),_GpsSyncStatus_Type())
gpsSyncStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:gpsSyncStatus.setStatus(_A)
class _GpsSyncMasterSlave_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('cmmIsGPSSlave',0),('cmmIsGPSMaster',1)))
_GpsSyncMasterSlave_Type.__name__=_E
_GpsSyncMasterSlave_Object=MibScalar
gpsSyncMasterSlave=_GpsSyncMasterSlave_Object((1,3,6,1,4,1,161,19,3,6,4,14),_GpsSyncMasterSlave_Type())
gpsSyncMasterSlave.setMaxAccess(_D)
if mibBuilder.loadTexts:gpsSyncMasterSlave.setStatus(_A)
_GpsLog_Type=EventString
_GpsLog_Object=MibScalar
gpsLog=_GpsLog_Object((1,3,6,1,4,1,161,19,3,6,4,15),_GpsLog_Type())
gpsLog.setMaxAccess(_D)
if mibBuilder.loadTexts:gpsLog.setStatus(_A)
_GpsReInitCount_Type=Integer32
_GpsReInitCount_Object=MibScalar
gpsReInitCount=_GpsReInitCount_Object((1,3,6,1,4,1,161,19,3,6,4,16),_GpsReInitCount_Type())
gpsReInitCount.setMaxAccess(_D)
if mibBuilder.loadTexts:gpsReInitCount.setStatus(_A)
_Cmm4EventLog_ObjectIdentity=ObjectIdentity
cmm4EventLog=_Cmm4EventLog_ObjectIdentity((1,3,6,1,4,1,161,19,3,6,5))
_EventLog_Type=EventString
_EventLog_Object=MibScalar
eventLog=_EventLog_Object((1,3,6,1,4,1,161,19,3,6,5,1),_EventLog_Type())
eventLog.setMaxAccess(_D)
if mibBuilder.loadTexts:eventLog.setStatus(_A)
_NtpLog_Type=EventString
_NtpLog_Object=MibScalar
ntpLog=_NtpLog_Object((1,3,6,1,4,1,161,19,3,6,5,2),_NtpLog_Type())
ntpLog.setMaxAccess(_D)
if mibBuilder.loadTexts:ntpLog.setStatus(_A)
_Cmm4Controls_ObjectIdentity=ObjectIdentity
cmm4Controls=_Cmm4Controls_ObjectIdentity((1,3,6,1,4,1,161,19,3,6,6))
class _Cmm4Reboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('finishedReboot',0),('reboot',1)))
_Cmm4Reboot_Type.__name__=_E
_Cmm4Reboot_Object=MibScalar
cmm4Reboot=_Cmm4Reboot_Object((1,3,6,1,4,1,161,19,3,6,6,1),_Cmm4Reboot_Type())
cmm4Reboot.setMaxAccess(_C)
if mibBuilder.loadTexts:cmm4Reboot.setStatus(_A)
class _Cmm4ClearEventLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('notClear',0),('clear',1)))
_Cmm4ClearEventLog_Type.__name__=_E
_Cmm4ClearEventLog_Object=MibScalar
cmm4ClearEventLog=_Cmm4ClearEventLog_Object((1,3,6,1,4,1,161,19,3,6,6,2),_Cmm4ClearEventLog_Type())
cmm4ClearEventLog.setMaxAccess(_C)
if mibBuilder.loadTexts:cmm4ClearEventLog.setStatus(_A)
class _Cmm4RebootIfRequired_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('rebootcomplete',0),('rebootifrquired',1)))
_Cmm4RebootIfRequired_Type.__name__=_E
_Cmm4RebootIfRequired_Object=MibScalar
cmm4RebootIfRequired=_Cmm4RebootIfRequired_Object((1,3,6,1,4,1,161,19,3,6,6,3),_Cmm4RebootIfRequired_Type())
cmm4RebootIfRequired.setMaxAccess(_C)
if mibBuilder.loadTexts:cmm4RebootIfRequired.setStatus(_A)
_Cmm4Snmp_ObjectIdentity=ObjectIdentity
cmm4Snmp=_Cmm4Snmp_ObjectIdentity((1,3,6,1,4,1,161,19,3,6,7))
_Cmm4SnmpComString_Type=DisplayString
_Cmm4SnmpComString_Object=MibScalar
cmm4SnmpComString=_Cmm4SnmpComString_Object((1,3,6,1,4,1,161,19,3,6,7,1),_Cmm4SnmpComString_Type())
cmm4SnmpComString.setMaxAccess(_C)
if mibBuilder.loadTexts:cmm4SnmpComString.setStatus(_A)
_Cmm4SnmpAccessSubnet_Type=DisplayString
_Cmm4SnmpAccessSubnet_Object=MibScalar
cmm4SnmpAccessSubnet=_Cmm4SnmpAccessSubnet_Object((1,3,6,1,4,1,161,19,3,6,7,2),_Cmm4SnmpAccessSubnet_Type())
cmm4SnmpAccessSubnet.setMaxAccess(_C)
if mibBuilder.loadTexts:cmm4SnmpAccessSubnet.setStatus(_A)
_Cmm4SnmpTrapIp1_Type=IpAddress
_Cmm4SnmpTrapIp1_Object=MibScalar
cmm4SnmpTrapIp1=_Cmm4SnmpTrapIp1_Object((1,3,6,1,4,1,161,19,3,6,7,3),_Cmm4SnmpTrapIp1_Type())
cmm4SnmpTrapIp1.setMaxAccess(_C)
if mibBuilder.loadTexts:cmm4SnmpTrapIp1.setStatus(_A)
_Cmm4SnmpTrapIp2_Type=IpAddress
_Cmm4SnmpTrapIp2_Object=MibScalar
cmm4SnmpTrapIp2=_Cmm4SnmpTrapIp2_Object((1,3,6,1,4,1,161,19,3,6,7,4),_Cmm4SnmpTrapIp2_Type())
cmm4SnmpTrapIp2.setMaxAccess(_C)
if mibBuilder.loadTexts:cmm4SnmpTrapIp2.setStatus(_A)
_Cmm4SnmpTrapIp3_Type=IpAddress
_Cmm4SnmpTrapIp3_Object=MibScalar
cmm4SnmpTrapIp3=_Cmm4SnmpTrapIp3_Object((1,3,6,1,4,1,161,19,3,6,7,5),_Cmm4SnmpTrapIp3_Type())
cmm4SnmpTrapIp3.setMaxAccess(_C)
if mibBuilder.loadTexts:cmm4SnmpTrapIp3.setStatus(_A)
_Cmm4SnmpTrapIp4_Type=IpAddress
_Cmm4SnmpTrapIp4_Object=MibScalar
cmm4SnmpTrapIp4=_Cmm4SnmpTrapIp4_Object((1,3,6,1,4,1,161,19,3,6,7,6),_Cmm4SnmpTrapIp4_Type())
cmm4SnmpTrapIp4.setMaxAccess(_C)
if mibBuilder.loadTexts:cmm4SnmpTrapIp4.setStatus(_A)
_Cmm4SnmpTrapIp5_Type=IpAddress
_Cmm4SnmpTrapIp5_Object=MibScalar
cmm4SnmpTrapIp5=_Cmm4SnmpTrapIp5_Object((1,3,6,1,4,1,161,19,3,6,7,7),_Cmm4SnmpTrapIp5_Type())
cmm4SnmpTrapIp5.setMaxAccess(_C)
if mibBuilder.loadTexts:cmm4SnmpTrapIp5.setStatus(_A)
_Cmm4SnmpTrapIp6_Type=IpAddress
_Cmm4SnmpTrapIp6_Object=MibScalar
cmm4SnmpTrapIp6=_Cmm4SnmpTrapIp6_Object((1,3,6,1,4,1,161,19,3,6,7,8),_Cmm4SnmpTrapIp6_Type())
cmm4SnmpTrapIp6.setMaxAccess(_C)
if mibBuilder.loadTexts:cmm4SnmpTrapIp6.setStatus(_A)
_Cmm4SnmpTrapIp7_Type=IpAddress
_Cmm4SnmpTrapIp7_Object=MibScalar
cmm4SnmpTrapIp7=_Cmm4SnmpTrapIp7_Object((1,3,6,1,4,1,161,19,3,6,7,9),_Cmm4SnmpTrapIp7_Type())
cmm4SnmpTrapIp7.setMaxAccess(_C)
if mibBuilder.loadTexts:cmm4SnmpTrapIp7.setStatus(_A)
_Cmm4SnmpTrapIp8_Type=IpAddress
_Cmm4SnmpTrapIp8_Object=MibScalar
cmm4SnmpTrapIp8=_Cmm4SnmpTrapIp8_Object((1,3,6,1,4,1,161,19,3,6,7,10),_Cmm4SnmpTrapIp8_Type())
cmm4SnmpTrapIp8.setMaxAccess(_C)
if mibBuilder.loadTexts:cmm4SnmpTrapIp8.setStatus(_A)
_Cmm4SnmpTrapIp9_Type=IpAddress
_Cmm4SnmpTrapIp9_Object=MibScalar
cmm4SnmpTrapIp9=_Cmm4SnmpTrapIp9_Object((1,3,6,1,4,1,161,19,3,6,7,11),_Cmm4SnmpTrapIp9_Type())
cmm4SnmpTrapIp9.setMaxAccess(_C)
if mibBuilder.loadTexts:cmm4SnmpTrapIp9.setStatus(_A)
_Cmm4SnmpTrapIp10_Type=IpAddress
_Cmm4SnmpTrapIp10_Object=MibScalar
cmm4SnmpTrapIp10=_Cmm4SnmpTrapIp10_Object((1,3,6,1,4,1,161,19,3,6,7,12),_Cmm4SnmpTrapIp10_Type())
cmm4SnmpTrapIp10.setMaxAccess(_C)
if mibBuilder.loadTexts:cmm4SnmpTrapIp10.setStatus(_A)
class _Cmm4SnmpReadOnly_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('readWritePermissions',0),('readOnlyPermissions',1)))
_Cmm4SnmpReadOnly_Type.__name__=_E
_Cmm4SnmpReadOnly_Object=MibScalar
cmm4SnmpReadOnly=_Cmm4SnmpReadOnly_Object((1,3,6,1,4,1,161,19,3,6,7,13),_Cmm4SnmpReadOnly_Type())
cmm4SnmpReadOnly.setMaxAccess(_C)
if mibBuilder.loadTexts:cmm4SnmpReadOnly.setStatus(_A)
class _Cmm4SnmpGPSSyncTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('gpsSyncTrapDisabled',0),('gpsSyncTrapEnabled',1)))
_Cmm4SnmpGPSSyncTrapEnable_Type.__name__=_E
_Cmm4SnmpGPSSyncTrapEnable_Object=MibScalar
cmm4SnmpGPSSyncTrapEnable=_Cmm4SnmpGPSSyncTrapEnable_Object((1,3,6,1,4,1,161,19,3,6,7,14),_Cmm4SnmpGPSSyncTrapEnable_Type())
cmm4SnmpGPSSyncTrapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cmm4SnmpGPSSyncTrapEnable.setStatus(_A)
_Cmm4SnmpAccessSubnet2_Type=DisplayString
_Cmm4SnmpAccessSubnet2_Object=MibScalar
cmm4SnmpAccessSubnet2=_Cmm4SnmpAccessSubnet2_Object((1,3,6,1,4,1,161,19,3,6,7,15),_Cmm4SnmpAccessSubnet2_Type())
cmm4SnmpAccessSubnet2.setMaxAccess(_C)
if mibBuilder.loadTexts:cmm4SnmpAccessSubnet2.setStatus(_A)
_Cmm4SnmpAccessSubnet3_Type=DisplayString
_Cmm4SnmpAccessSubnet3_Object=MibScalar
cmm4SnmpAccessSubnet3=_Cmm4SnmpAccessSubnet3_Object((1,3,6,1,4,1,161,19,3,6,7,16),_Cmm4SnmpAccessSubnet3_Type())
cmm4SnmpAccessSubnet3.setMaxAccess(_C)
if mibBuilder.loadTexts:cmm4SnmpAccessSubnet3.setStatus(_A)
_Cmm4SnmpAccessSubnet4_Type=DisplayString
_Cmm4SnmpAccessSubnet4_Object=MibScalar
cmm4SnmpAccessSubnet4=_Cmm4SnmpAccessSubnet4_Object((1,3,6,1,4,1,161,19,3,6,7,17),_Cmm4SnmpAccessSubnet4_Type())
cmm4SnmpAccessSubnet4.setMaxAccess(_C)
if mibBuilder.loadTexts:cmm4SnmpAccessSubnet4.setStatus(_A)
_Cmm4SnmpAccessSubnet5_Type=DisplayString
_Cmm4SnmpAccessSubnet5_Object=MibScalar
cmm4SnmpAccessSubnet5=_Cmm4SnmpAccessSubnet5_Object((1,3,6,1,4,1,161,19,3,6,7,18),_Cmm4SnmpAccessSubnet5_Type())
cmm4SnmpAccessSubnet5.setMaxAccess(_C)
if mibBuilder.loadTexts:cmm4SnmpAccessSubnet5.setStatus(_A)
_Cmm4SnmpAccessSubnet6_Type=DisplayString
_Cmm4SnmpAccessSubnet6_Object=MibScalar
cmm4SnmpAccessSubnet6=_Cmm4SnmpAccessSubnet6_Object((1,3,6,1,4,1,161,19,3,6,7,19),_Cmm4SnmpAccessSubnet6_Type())
cmm4SnmpAccessSubnet6.setMaxAccess(_C)
if mibBuilder.loadTexts:cmm4SnmpAccessSubnet6.setStatus(_A)
_Cmm4SnmpAccessSubnet7_Type=DisplayString
_Cmm4SnmpAccessSubnet7_Object=MibScalar
cmm4SnmpAccessSubnet7=_Cmm4SnmpAccessSubnet7_Object((1,3,6,1,4,1,161,19,3,6,7,20),_Cmm4SnmpAccessSubnet7_Type())
cmm4SnmpAccessSubnet7.setMaxAccess(_C)
if mibBuilder.loadTexts:cmm4SnmpAccessSubnet7.setStatus(_A)
_Cmm4SnmpAccessSubnet8_Type=DisplayString
_Cmm4SnmpAccessSubnet8_Object=MibScalar
cmm4SnmpAccessSubnet8=_Cmm4SnmpAccessSubnet8_Object((1,3,6,1,4,1,161,19,3,6,7,21),_Cmm4SnmpAccessSubnet8_Type())
cmm4SnmpAccessSubnet8.setMaxAccess(_C)
if mibBuilder.loadTexts:cmm4SnmpAccessSubnet8.setStatus(_A)
_Cmm4SnmpAccessSubnet9_Type=DisplayString
_Cmm4SnmpAccessSubnet9_Object=MibScalar
cmm4SnmpAccessSubnet9=_Cmm4SnmpAccessSubnet9_Object((1,3,6,1,4,1,161,19,3,6,7,22),_Cmm4SnmpAccessSubnet9_Type())
cmm4SnmpAccessSubnet9.setMaxAccess(_C)
if mibBuilder.loadTexts:cmm4SnmpAccessSubnet9.setStatus(_A)
_Cmm4SnmpAccessSubnet10_Type=DisplayString
_Cmm4SnmpAccessSubnet10_Object=MibScalar
cmm4SnmpAccessSubnet10=_Cmm4SnmpAccessSubnet10_Object((1,3,6,1,4,1,161,19,3,6,7,23),_Cmm4SnmpAccessSubnet10_Type())
cmm4SnmpAccessSubnet10.setMaxAccess(_C)
if mibBuilder.loadTexts:cmm4SnmpAccessSubnet10.setStatus(_A)
_Cmm4Event_ObjectIdentity=ObjectIdentity
cmm4Event=_Cmm4Event_ObjectIdentity((1,3,6,1,4,1,161,19,3,6,8))
_Cmm4GPSEvent_ObjectIdentity=ObjectIdentity
cmm4GPSEvent=_Cmm4GPSEvent_ObjectIdentity((1,3,6,1,4,1,161,19,3,6,8,1))
_Cmm4UserTable_Object=MibTable
cmm4UserTable=_Cmm4UserTable_Object((1,3,6,1,4,1,161,19,3,6,9))
if mibBuilder.loadTexts:cmm4UserTable.setStatus(_A)
_Cmm4UserEntry_Object=MibTableRow
cmm4UserEntry=_Cmm4UserEntry_Object((1,3,6,1,4,1,161,19,3,6,9,1))
cmm4UserEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:cmm4UserEntry.setStatus(_A)
class _EntryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_EntryIndex_Type.__name__=_E
_EntryIndex_Object=MibTableColumn
entryIndex=_EntryIndex_Object((1,3,6,1,4,1,161,19,3,6,9,1,1),_EntryIndex_Type())
entryIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:entryIndex.setStatus(_A)
_UserLoginName_Type=DisplayString
_UserLoginName_Object=MibTableColumn
userLoginName=_UserLoginName_Object((1,3,6,1,4,1,161,19,3,6,9,1,2),_UserLoginName_Type())
userLoginName.setMaxAccess(_D)
if mibBuilder.loadTexts:userLoginName.setStatus(_A)
_UserPswd_Type=DisplayString
_UserPswd_Object=MibTableColumn
userPswd=_UserPswd_Object((1,3,6,1,4,1,161,19,3,6,9,1,3),_UserPswd_Type())
userPswd.setMaxAccess(_D)
if mibBuilder.loadTexts:userPswd.setStatus(_A)
class _AccessLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('noAdmin',0),('guest',1),('installer',2),('administrator',3),('technician',4),('engineering',5)))
_AccessLevel_Type.__name__=_E
_AccessLevel_Object=MibTableColumn
accessLevel=_AccessLevel_Object((1,3,6,1,4,1,161,19,3,6,9,1,4),_AccessLevel_Type())
accessLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:accessLevel.setStatus(_A)
cmm4PortCfgGroup=ObjectGroup((1,3,6,1,4,1,161,19,3,6,1,1))
cmm4PortCfgGroup.setObjects(*((_B,_J),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:cmm4PortCfgGroup.setStatus(_A)
cmm4ConfigGroup=ObjectGroup((1,3,6,1,4,1,161,19,3,6,1,2))
cmm4ConfigGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:cmm4ConfigGroup.setStatus(_A)
cmm4PortStatusGroup=ObjectGroup((1,3,6,1,4,1,161,19,3,6,1,3))
cmm4PortStatusGroup.setObjects(*((_B,_K),(_B,_i)))
if mibBuilder.loadTexts:cmm4PortStatusGroup.setStatus(_A)
cmm4StatusGroup=ObjectGroup((1,3,6,1,4,1,161,19,3,6,1,4))
cmm4StatusGroup.setObjects(*((_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_H),(_B,_v),(_B,_w),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:cmm4StatusGroup.setStatus(_A)
cmm4GPSGroup=ObjectGroup((1,3,6,1,4,1,161,19,3,6,1,5))
cmm4GPSGroup.setObjects(*((_B,_z),(_B,'gpsTime'),(_B,'gpsDate'),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_I),(_B,_A9),(_B,'gpsLog'),(_B,_AA)))
if mibBuilder.loadTexts:cmm4GPSGroup.setStatus(_A)
cmm4ControlsGroup=ObjectGroup((1,3,6,1,4,1,161,19,3,6,1,6))
cmm4ControlsGroup.setObjects(*((_B,_AB),(_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:cmm4ControlsGroup.setStatus(_A)
cmm4SNMPGroup=ObjectGroup((1,3,6,1,4,1,161,19,3,6,1,7))
cmm4SNMPGroup.setObjects(*((_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa)))
if mibBuilder.loadTexts:cmm4SNMPGroup.setStatus(_A)
cmm4UserTableGroup=ObjectGroup((1,3,6,1,4,1,161,19,3,6,1,8))
cmm4UserTableGroup.setObjects(*((_B,_L),(_B,_Ab),(_B,'userPswd'),(_B,_Ac)))
if mibBuilder.loadTexts:cmm4UserTableGroup.setStatus(_A)
cmm4GPSInSync=NotificationType((1,3,6,1,4,1,161,19,3,6,8,1,1))
cmm4GPSInSync.setObjects(*((_B,_I),(_B,_H)))
if mibBuilder.loadTexts:cmm4GPSInSync.setStatus(_A)
cmm4GPSNoSync=NotificationType((1,3,6,1,4,1,161,19,3,6,8,1,2))
cmm4GPSNoSync.setObjects(*((_B,_I),(_B,_H)))
if mibBuilder.loadTexts:cmm4GPSNoSync.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cmm4MibModule':cmm4MibModule,'cmm4Groups':cmm4Groups,'cmm4PortCfgGroup':cmm4PortCfgGroup,'cmm4ConfigGroup':cmm4ConfigGroup,'cmm4PortStatusGroup':cmm4PortStatusGroup,'cmm4StatusGroup':cmm4StatusGroup,'cmm4GPSGroup':cmm4GPSGroup,'cmm4ControlsGroup':cmm4ControlsGroup,'cmm4SNMPGroup':cmm4SNMPGroup,'cmm4UserTableGroup':cmm4UserTableGroup,'cmm4Config':cmm4Config,_S:gpsTimingPulse,_T:lan1Ip,_U:lan1SubnetMask,_V:defaultGateway,_W:cmm4WebAutoUpdate,_X:cmm4ExtEthPowerReset,'cmm4PortCfgTable':cmm4PortCfgTable,'cmm4PortCfgEntry':cmm4PortCfgEntry,_J:portCfgIndex,_O:cmm4PortText,_P:cmm4PortDevType,_Q:cmm4PortPowerCfg,_R:cmm4PortResetCfg,_Y:cmm4IpAccessFilter,_Z:cmm4IpAccess1,_a:cmm4IpAccess2,_b:cmm4IpAccess3,_c:cmm4MgmtPortSpeed,_d:cmm4NTPServerIp,_e:sessionTimeout,_f:vlanEnable,_g:managementVID,_h:siteInfoViewable,'cmm4Status':cmm4Status,'cmm4PortStatusTable':cmm4PortStatusTable,'cmm4PortStatusEntry':cmm4PortStatusEntry,_K:portStatusIndex,_i:cmm4PortPowerStatus,_j:deviceType,_k:cmm4pldVersion,_l:cmm4SoftwareVersion,_m:cmm4SystemTime,_n:cmm4UpTime,_o:satellitesVisible,_p:satellitesTracked,_q:latitude,_r:longitude,_s:height,_t:trackingMode,_u:syncStatus,_H:cmm4MacAddress,_v:cmm4ExtEthPwrStat,_w:cmm4FPGAVersion,_x:cmm4FPGAPlatform,_y:defaultStatus,'cmm4Gps':cmm4Gps,_z:gpsTrackingMode,'gpsTime':gpsTime,'gpsDate':gpsDate,_A0:gpsSatellitesVisible,_A1:gpsSatellitesTracked,_A2:gpsHeight,_A3:gpsAntennaConnection,_A4:gpsLatitude,_A5:gpsLongitude,_A6:gpsInvalidMsg,_A7:gpsRestartCount,_A8:gpsReceiverInfo,_I:gpsSyncStatus,_A9:gpsSyncMasterSlave,'gpsLog':gpsLog,_AA:gpsReInitCount,'cmm4EventLog':cmm4EventLog,'eventLog':eventLog,'ntpLog':ntpLog,'cmm4Controls':cmm4Controls,_AB:cmm4Reboot,_AC:cmm4ClearEventLog,_AD:cmm4RebootIfRequired,'cmm4Snmp':cmm4Snmp,_AE:cmm4SnmpComString,_AF:cmm4SnmpAccessSubnet,_AG:cmm4SnmpTrapIp1,_AH:cmm4SnmpTrapIp2,_AI:cmm4SnmpTrapIp3,_AJ:cmm4SnmpTrapIp4,_AK:cmm4SnmpTrapIp5,_AL:cmm4SnmpTrapIp6,_AM:cmm4SnmpTrapIp7,_AN:cmm4SnmpTrapIp8,_AO:cmm4SnmpTrapIp9,_AP:cmm4SnmpTrapIp10,_AQ:cmm4SnmpReadOnly,_AR:cmm4SnmpGPSSyncTrapEnable,_AS:cmm4SnmpAccessSubnet2,_AT:cmm4SnmpAccessSubnet3,_AU:cmm4SnmpAccessSubnet4,_AV:cmm4SnmpAccessSubnet5,_AW:cmm4SnmpAccessSubnet6,_AX:cmm4SnmpAccessSubnet7,_AY:cmm4SnmpAccessSubnet8,_AZ:cmm4SnmpAccessSubnet9,_Aa:cmm4SnmpAccessSubnet10,'cmm4Event':cmm4Event,'cmm4GPSEvent':cmm4GPSEvent,'cmm4GPSInSync':cmm4GPSInSync,'cmm4GPSNoSync':cmm4GPSNoSync,'cmm4UserTable':cmm4UserTable,'cmm4UserEntry':cmm4UserEntry,_L:entryIndex,_Ab:userLoginName,'userPswd':userPswd,_Ac:accessLevel})