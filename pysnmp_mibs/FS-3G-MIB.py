_AY='fs3GNetworkISPName'
_AX='fs3GISPtimeout'
_AW='fs3GTrapFilterMode'
_AV='fs3GRssiThreshold'
_AU='fs3GTrafficTrapInterval'
_AT='fs3G2ifIndex'
_AS='fs3GOutSpeed'
_AR='fs3GInSpeed'
_AQ='fs3GAcessBSLAT'
_AP='fs3GAcessBSLONG'
_AO='fs3GAcessBSLAC'
_AN='fs3GAcessBSCellID'
_AM='fs3GUserActiveTime'
_AL='fs3GSIMCardStatus'
_AK='fs3GNetworkSysMode'
_AJ='fs3GNetworkISPMode'
_AI='fs3GModemIMEI'
_AH='fs3GLineCardType'
_AG='fs3GDeviceBackupIMSI'
_AF='fs3GLineDetectedSubCause'
_AE='fs3GLineDetectedMainCause'
_AD='fs3GLineDetectedResult'
_AC='fs3GLineDetected'
_AB='fs3GPhoneNumber'
_AA='fs3GCellID'
_A9='fs3GBackupIMSI'
_A8='fs3GLineDownCause'
_A7='fs3GGatewayIPAddr'
_A6='fs3GBackupInfo'
_A5='fs3GSignalStrengthPercent'
_A4='fs3GSignalStrength'
_A3='ipsecSetupFailed'
_A2='noGivenReason'
_A1='modem-type-4G'
_A0='modem-type-3G'
_z='master'
_y='myself'
_x='no-backup'
_w='noUsimCard'
_v='invalidForCSPS'
_u='invalidForPS'
_t='invalidForCS'
_s='validUsimCard'
_r='invalidUsimCard'
_q='roaming'
_p='noRoaming'
_o='powerSavingAndDeepSleepState'
_n='restrictedRegional'
_m='restricted'
_l='fdd-lte'
_k='td-1te'
_j='cdmaHdrHybrid'
_i='gsmCdma'
_h='gsmGprs'
_g='ipv6Addr'
_f='ipv4Addr'
_e='fs3GRssiStrengthPercent'
_d='fs3GDeviceBackupInfo'
_c='fs3GOutOctets'
_b='fs3GInOctets'
_a='chinaMobile'
_Z='chinaTelecom'
_Y='chinaUnicom'
_X='fs3GRssiStrength'
_W='fs3GSerialNumber'
_V='fs3GDialOnDemandIfIndex'
_U='fs3GTrafficPreventMode'
_T='fs3GTrafficPreventIfIndex'
_S='fs3GTrafficPreventListID'
_R='fs3GTrafficPreventListName'
_Q='fs3gUsername'
_P='noService'
_O='fs3GDailMode'
_N='fs3GCardPhoneNumber'
_M='fs3GPppUsername'
_L='fs3GDeviceModemType'
_K='fs3GIntfIPAddr'
_J='fs3GCardIMSI'
_I='fs3GRouterSN'
_H='fs3GIMSI'
_G='fs3GRouterSlotNumber'
_F='fs3GIPAddr'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='current'
_A='FS-3G-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
fs3GMonitor=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,95))
if mibBuilder.loadTexts:fs3GMonitor.setRevisions(('2011-02-22 00:00',))
_Fs3GObjects_ObjectIdentity=ObjectIdentity
fs3GObjects=_Fs3GObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,95,1))
_Fs3GTable_Object=MibTable
fs3GTable=_Fs3GTable_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,1))
if mibBuilder.loadTexts:fs3GTable.setStatus(_B)
_Fs3GEntry_Object=MibTableRow
fs3GEntry=_Fs3GEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,1,1))
fs3GEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:fs3GEntry.setStatus(_B)
_Fs3gUsername_Type=DisplayString
_Fs3gUsername_Object=MibTableColumn
fs3gUsername=_Fs3gUsername_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,1,1,1),_Fs3gUsername_Type())
fs3gUsername.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3gUsername.setStatus(_B)
class _Fs3GOnlineStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,4,5,6,7)));namedValues=NamedValues(*(('lpm',0),('online',1),('offline',4),('ftm',5),('reset',6),('rfOff',7)))
_Fs3GOnlineStatus_Type.__name__=_D
_Fs3GOnlineStatus_Object=MibTableColumn
fs3GOnlineStatus=_Fs3GOnlineStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,1,1,2),_Fs3GOnlineStatus_Type())
fs3GOnlineStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GOnlineStatus.setStatus(_B)
_Fs3GIMEI_Type=DisplayString
_Fs3GIMEI_Object=MibTableColumn
fs3GIMEI=_Fs3GIMEI_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,1,1,3),_Fs3GIMEI_Type())
fs3GIMEI.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GIMEI.setStatus(_B)
class _Fs3GIPAddrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_f,1),(_g,2)))
_Fs3GIPAddrType_Type.__name__=_D
_Fs3GIPAddrType_Object=MibTableColumn
fs3GIPAddrType=_Fs3GIPAddrType_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,1,1,4),_Fs3GIPAddrType_Type())
fs3GIPAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GIPAddrType.setStatus(_B)
_Fs3GIPAddr_Type=IpAddress
_Fs3GIPAddr_Object=MibTableColumn
fs3GIPAddr=_Fs3GIPAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,1,1,5),_Fs3GIPAddr_Type())
fs3GIPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GIPAddr.setStatus(_B)
_Fs3GUplineTime_Type=TimeStamp
_Fs3GUplineTime_Object=MibTableColumn
fs3GUplineTime=_Fs3GUplineTime_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,1,1,6),_Fs3GUplineTime_Type())
fs3GUplineTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GUplineTime.setStatus(_B)
class _Fs3GActiveTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Fs3GActiveTime_Type.__name__=_D
_Fs3GActiveTime_Object=MibTableColumn
fs3GActiveTime=_Fs3GActiveTime_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,1,1,7),_Fs3GActiveTime_Type())
fs3GActiveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GActiveTime.setStatus(_B)
class _Fs3GSignalStrength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-150,0))
_Fs3GSignalStrength_Type.__name__=_D
_Fs3GSignalStrength_Object=MibTableColumn
fs3GSignalStrength=_Fs3GSignalStrength_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,1,1,8),_Fs3GSignalStrength_Type())
fs3GSignalStrength.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GSignalStrength.setStatus(_B)
class _Fs3GISP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Y,1),(_Z,2),(_a,3)))
_Fs3GISP_Type.__name__=_D
_Fs3GISP_Object=MibTableColumn
fs3GISP=_Fs3GISP_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,1,1,9),_Fs3GISP_Type())
fs3GISP.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GISP.setStatus(_B)
class _Fs3GSysMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,15,100,101)));namedValues=NamedValues(*((_P,0),('amps',1),('cdma',2),(_h,3),('hdr',4),('wcdma',5),('gps',6),(_i,7),(_j,8),('tdscdma',15),(_k,100),(_l,101)))
_Fs3GSysMode_Type.__name__=_D
_Fs3GSysMode_Object=MibTableColumn
fs3GSysMode=_Fs3GSysMode_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,1,1,10),_Fs3GSysMode_Type())
fs3GSysMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GSysMode.setStatus(_B)
class _Fs3GServiceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_P,0),(_m,1),('valid',2),(_n,3),(_o,4)))
_Fs3GServiceStatus_Type.__name__=_D
_Fs3GServiceStatus_Object=MibTableColumn
fs3GServiceStatus=_Fs3GServiceStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,1,1,11),_Fs3GServiceStatus_Type())
fs3GServiceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GServiceStatus.setStatus(_B)
class _Fs3GRoamingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_p,0),(_q,1)))
_Fs3GRoamingStatus_Type.__name__=_D
_Fs3GRoamingStatus_Object=MibTableColumn
fs3GRoamingStatus=_Fs3GRoamingStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,1,1,12),_Fs3GRoamingStatus_Type())
fs3GRoamingStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GRoamingStatus.setStatus(_B)
class _Fs3GDomain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,100,255)));namedValues=NamedValues(*((_P,0),('onlyCS',1),('onlyPS',2),('pSCS',3),('pSCSnotRegistered',4),('ePSService',100),('cdmaNotSupport',255)))
_Fs3GDomain_Type.__name__=_D
_Fs3GDomain_Object=MibTableColumn
fs3GDomain=_Fs3GDomain_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,1,1,13),_Fs3GDomain_Type())
fs3GDomain.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GDomain.setStatus(_B)
class _Fs3GSIMStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,255)));namedValues=NamedValues(*((_r,0),(_s,1),(_t,2),(_u,3),(_v,4),(_w,255)))
_Fs3GSIMStatus_Type.__name__=_D
_Fs3GSIMStatus_Object=MibTableColumn
fs3GSIMStatus=_Fs3GSIMStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,1,1,14),_Fs3GSIMStatus_Type())
fs3GSIMStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GSIMStatus.setStatus(_B)
class _Fs3GSignalStrengthPercent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Fs3GSignalStrengthPercent_Type.__name__=_D
_Fs3GSignalStrengthPercent_Object=MibTableColumn
fs3GSignalStrengthPercent=_Fs3GSignalStrengthPercent_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,1,1,15),_Fs3GSignalStrengthPercent_Type())
fs3GSignalStrengthPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GSignalStrengthPercent.setStatus(_B)
_Fs3GApn_Type=DisplayString
_Fs3GApn_Object=MibTableColumn
fs3GApn=_Fs3GApn_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,1,1,16),_Fs3GApn_Type())
fs3GApn.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GApn.setStatus(_B)
class _Fs3GCellID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Fs3GCellID_Type.__name__=_D
_Fs3GCellID_Object=MibTableColumn
fs3GCellID=_Fs3GCellID_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,1,1,17),_Fs3GCellID_Type())
fs3GCellID.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GCellID.setStatus(_B)
class _Fs3GLAC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Fs3GLAC_Type.__name__=_D
_Fs3GLAC_Object=MibTableColumn
fs3GLAC=_Fs3GLAC_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,1,1,18),_Fs3GLAC_Type())
fs3GLAC.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GLAC.setStatus(_B)
class _Fs3GBSID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Fs3GBSID_Type.__name__=_D
_Fs3GBSID_Object=MibTableColumn
fs3GBSID=_Fs3GBSID_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,1,1,19),_Fs3GBSID_Type())
fs3GBSID.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GBSID.setStatus(_B)
class _Fs3GNID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Fs3GNID_Type.__name__=_D
_Fs3GNID_Object=MibTableColumn
fs3GNID=_Fs3GNID_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,1,1,20),_Fs3GNID_Type())
fs3GNID.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GNID.setStatus(_B)
class _Fs3GSID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Fs3GSID_Type.__name__=_D
_Fs3GSID_Object=MibTableColumn
fs3GSID=_Fs3GSID_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,1,1,21),_Fs3GSID_Type())
fs3GSID.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GSID.setStatus(_B)
_Fs3GIMSI_Type=DisplayString
_Fs3GIMSI_Object=MibTableColumn
fs3GIMSI=_Fs3GIMSI_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,1,1,22),_Fs3GIMSI_Type())
fs3GIMSI.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GIMSI.setStatus(_B)
_Fs3GESN_Type=DisplayString
_Fs3GESN_Object=MibTableColumn
fs3GESN=_Fs3GESN_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,1,1,23),_Fs3GESN_Type())
fs3GESN.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GESN.setStatus(_B)
_Fs3GPhoneNumber_Type=DisplayString
_Fs3GPhoneNumber_Object=MibTableColumn
fs3GPhoneNumber=_Fs3GPhoneNumber_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,1,1,24),_Fs3GPhoneNumber_Type())
fs3GPhoneNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GPhoneNumber.setStatus(_B)
_Fs3GifIndex_Type=Integer32
_Fs3GifIndex_Object=MibTableColumn
fs3GifIndex=_Fs3GifIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,1,1,25),_Fs3GifIndex_Type())
fs3GifIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GifIndex.setStatus(_B)
_Fs3GBSLONG_Type=Integer32
_Fs3GBSLONG_Object=MibTableColumn
fs3GBSLONG=_Fs3GBSLONG_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,1,1,26),_Fs3GBSLONG_Type())
fs3GBSLONG.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GBSLONG.setStatus(_B)
_Fs3GBSLAT_Type=Integer32
_Fs3GBSLAT_Object=MibTableColumn
fs3GBSLAT=_Fs3GBSLAT_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,1,1,27),_Fs3GBSLAT_Type())
fs3GBSLAT.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GBSLAT.setStatus(_B)
class _Fs3GBackupInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_x,0),(_y,1),(_z,2),('slave',3)))
_Fs3GBackupInfo_Type.__name__=_D
_Fs3GBackupInfo_Object=MibTableColumn
fs3GBackupInfo=_Fs3GBackupInfo_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,1,1,28),_Fs3GBackupInfo_Type())
fs3GBackupInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GBackupInfo.setStatus(_B)
_Fs3GSerialNumber_Type=DisplayString
_Fs3GSerialNumber_Object=MibTableColumn
fs3GSerialNumber=_Fs3GSerialNumber_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,1,1,29),_Fs3GSerialNumber_Type())
fs3GSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GSerialNumber.setStatus(_B)
_Fs3GBackupIMSI_Type=DisplayString
_Fs3GBackupIMSI_Object=MibTableColumn
fs3GBackupIMSI=_Fs3GBackupIMSI_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,1,1,30),_Fs3GBackupIMSI_Type())
fs3GBackupIMSI.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GBackupIMSI.setStatus(_B)
_Fs3GGatewayIPAddr_Type=IpAddress
_Fs3GGatewayIPAddr_Object=MibTableColumn
fs3GGatewayIPAddr=_Fs3GGatewayIPAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,1,1,31),_Fs3GGatewayIPAddr_Type())
fs3GGatewayIPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GGatewayIPAddr.setStatus(_B)
_Fs3GLineDownCause_Type=Integer32
_Fs3GLineDownCause_Object=MibTableColumn
fs3GLineDownCause=_Fs3GLineDownCause_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,1,1,32),_Fs3GLineDownCause_Type())
fs3GLineDownCause.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GLineDownCause.setStatus(_B)
class _Fs3GModemType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_A0,1),(_A1,2)))
_Fs3GModemType_Type.__name__=_D
_Fs3GModemType_Object=MibTableColumn
fs3GModemType=_Fs3GModemType_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,1,1,33),_Fs3GModemType_Type())
fs3GModemType.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GModemType.setStatus(_B)
_Fs3GStatTable_Object=MibTable
fs3GStatTable=_Fs3GStatTable_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,2))
if mibBuilder.loadTexts:fs3GStatTable.setStatus(_B)
_Fs3GStatEntry_Object=MibTableRow
fs3GStatEntry=_Fs3GStatEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,2,1))
fs3GStatEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:fs3GStatEntry.setStatus(_B)
_Fs3GInOctets_Type=Counter64
_Fs3GInOctets_Object=MibTableColumn
fs3GInOctets=_Fs3GInOctets_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,2,1,1),_Fs3GInOctets_Type())
fs3GInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GInOctets.setStatus(_B)
_Fs3GOutOctets_Type=Counter64
_Fs3GOutOctets_Object=MibTableColumn
fs3GOutOctets=_Fs3GOutOctets_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,2,1,2),_Fs3GOutOctets_Type())
fs3GOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GOutOctets.setStatus(_B)
_Fs3GInSpeed_Type=Counter64
_Fs3GInSpeed_Object=MibTableColumn
fs3GInSpeed=_Fs3GInSpeed_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,2,1,3),_Fs3GInSpeed_Type())
fs3GInSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GInSpeed.setStatus(_B)
_Fs3GOutSpeed_Type=Counter64
_Fs3GOutSpeed_Object=MibTableColumn
fs3GOutSpeed=_Fs3GOutSpeed_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,2,1,4),_Fs3GOutSpeed_Type())
fs3GOutSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GOutSpeed.setStatus(_B)
_Fs3G2IMSI_Type=DisplayString
_Fs3G2IMSI_Object=MibTableColumn
fs3G2IMSI=_Fs3G2IMSI_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,2,1,5),_Fs3G2IMSI_Type())
fs3G2IMSI.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3G2IMSI.setStatus(_B)
_Fs3G2ifIndex_Type=Integer32
_Fs3G2ifIndex_Object=MibTableColumn
fs3G2ifIndex=_Fs3G2ifIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,2,1,6),_Fs3G2ifIndex_Type())
fs3G2ifIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3G2ifIndex.setStatus(_B)
_Fs3GTrap_ObjectIdentity=ObjectIdentity
fs3GTrap=_Fs3GTrap_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,95,1,3))
_Fs3GNotifications_ObjectIdentity=ObjectIdentity
fs3GNotifications=_Fs3GNotifications_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,95,1,3,1))
_Fs3GBsNumber_Type=Integer32
_Fs3GBsNumber_Object=MibScalar
fs3GBsNumber=_Fs3GBsNumber_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,4),_Fs3GBsNumber_Type())
fs3GBsNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GBsNumber.setStatus(_B)
_Fs3GBsTable_Object=MibTable
fs3GBsTable=_Fs3GBsTable_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,5))
if mibBuilder.loadTexts:fs3GBsTable.setStatus(_B)
_Fs3GBsEntry_Object=MibTableRow
fs3GBsEntry=_Fs3GBsEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,5,1))
fs3GBsEntry.setIndexNames((0,_A,'fs3GBsSN'))
if mibBuilder.loadTexts:fs3GBsEntry.setStatus(_B)
_Fs3GBsSN_Type=Integer32
_Fs3GBsSN_Object=MibTableColumn
fs3GBsSN=_Fs3GBsSN_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,5,1,1),_Fs3GBsSN_Type())
fs3GBsSN.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GBsSN.setStatus(_B)
class _Fs3GBsISP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Y,1),(_Z,2),(_a,3)))
_Fs3GBsISP_Type.__name__=_D
_Fs3GBsISP_Object=MibTableColumn
fs3GBsISP=_Fs3GBsISP_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,5,1,2),_Fs3GBsISP_Type())
fs3GBsISP.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GBsISP.setStatus(_B)
class _Fs3GBsMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sys2GMode',1),('sys3GMode',2)))
_Fs3GBsMode_Type.__name__=_D
_Fs3GBsMode_Object=MibTableColumn
fs3GBsMode=_Fs3GBsMode_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,5,1,3),_Fs3GBsMode_Type())
fs3GBsMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GBsMode.setStatus(_B)
_Fs3GBsIMSI_Type=DisplayString
_Fs3GBsIMSI_Object=MibTableColumn
fs3GBsIMSI=_Fs3GBsIMSI_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,5,1,4),_Fs3GBsIMSI_Type())
fs3GBsIMSI.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GBsIMSI.setStatus(_B)
_Fs3GBsLAC_Type=Integer32
_Fs3GBsLAC_Object=MibTableColumn
fs3GBsLAC=_Fs3GBsLAC_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,5,1,5),_Fs3GBsLAC_Type())
fs3GBsLAC.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GBsLAC.setStatus(_B)
_Fs3GBsCellID_Type=Integer32
_Fs3GBsCellID_Object=MibTableColumn
fs3GBsCellID=_Fs3GBsCellID_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,5,1,6),_Fs3GBsCellID_Type())
fs3GBsCellID.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GBsCellID.setStatus(_B)
_Fs3GBsBSID_Type=Integer32
_Fs3GBsBSID_Object=MibTableColumn
fs3GBsBSID=_Fs3GBsBSID_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,5,1,7),_Fs3GBsBSID_Type())
fs3GBsBSID.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GBsBSID.setStatus(_B)
_Fs3GBsSID_Type=Integer32
_Fs3GBsSID_Object=MibTableColumn
fs3GBsSID=_Fs3GBsSID_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,5,1,8),_Fs3GBsSID_Type())
fs3GBsSID.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GBsSID.setStatus(_B)
_Fs3GBsNID_Type=Integer32
_Fs3GBsNID_Object=MibTableColumn
fs3GBsNID=_Fs3GBsNID_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,5,1,9),_Fs3GBsNID_Type())
fs3GBsNID.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GBsNID.setStatus(_B)
_Fs3GBsRssi_Type=Integer32
_Fs3GBsRssi_Object=MibTableColumn
fs3GBsRssi=_Fs3GBsRssi_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,5,1,10),_Fs3GBsRssi_Type())
fs3GBsRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GBsRssi.setStatus(_B)
_Fs3GBsBSLONG_Type=Integer32
_Fs3GBsBSLONG_Object=MibTableColumn
fs3GBsBSLONG=_Fs3GBsBSLONG_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,5,1,11),_Fs3GBsBSLONG_Type())
fs3GBsBSLONG.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GBsBSLONG.setStatus(_B)
_Fs3GBsBSLAT_Type=Integer32
_Fs3GBsBSLAT_Object=MibTableColumn
fs3GBsBSLAT=_Fs3GBsBSLAT_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,5,1,12),_Fs3GBsBSLAT_Type())
fs3GBsBSLAT.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GBsBSLAT.setStatus(_B)
_Fs3GDeviceManagementTable_Object=MibTable
fs3GDeviceManagementTable=_Fs3GDeviceManagementTable_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6))
if mibBuilder.loadTexts:fs3GDeviceManagementTable.setStatus(_B)
_Fs3GDeviceManagementEntry_Object=MibTableRow
fs3GDeviceManagementEntry=_Fs3GDeviceManagementEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1))
fs3GDeviceManagementEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:fs3GDeviceManagementEntry.setStatus(_B)
_Fs3GRouterType_Type=DisplayString
_Fs3GRouterType_Object=MibTableColumn
fs3GRouterType=_Fs3GRouterType_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,1),_Fs3GRouterType_Type())
fs3GRouterType.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GRouterType.setStatus(_B)
_Fs3GRouterSN_Type=DisplayString
_Fs3GRouterSN_Object=MibTableColumn
fs3GRouterSN=_Fs3GRouterSN_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,2),_Fs3GRouterSN_Type())
fs3GRouterSN.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GRouterSN.setStatus(_B)
_Fs3GRouterSlotNumber_Type=DisplayString
_Fs3GRouterSlotNumber_Object=MibTableColumn
fs3GRouterSlotNumber=_Fs3GRouterSlotNumber_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,3),_Fs3GRouterSlotNumber_Type())
fs3GRouterSlotNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GRouterSlotNumber.setStatus(_B)
_Fs3GLineCardType_Type=DisplayString
_Fs3GLineCardType_Object=MibTableColumn
fs3GLineCardType=_Fs3GLineCardType_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,4),_Fs3GLineCardType_Type())
fs3GLineCardType.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GLineCardType.setStatus(_B)
_Fs3GCardIMSI_Type=DisplayString
_Fs3GCardIMSI_Object=MibTableColumn
fs3GCardIMSI=_Fs3GCardIMSI_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,5),_Fs3GCardIMSI_Type())
fs3GCardIMSI.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GCardIMSI.setStatus(_B)
_Fs3GModemIMEI_Type=DisplayString
_Fs3GModemIMEI_Object=MibTableColumn
fs3GModemIMEI=_Fs3GModemIMEI_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,6),_Fs3GModemIMEI_Type())
fs3GModemIMEI.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GModemIMEI.setStatus(_B)
_Fs3GIntfIPAddr_Type=IpAddress
_Fs3GIntfIPAddr_Object=MibTableColumn
fs3GIntfIPAddr=_Fs3GIntfIPAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,7),_Fs3GIntfIPAddr_Type())
fs3GIntfIPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GIntfIPAddr.setStatus(_B)
_Fs3GCardPhoneNumber_Type=DisplayString
_Fs3GCardPhoneNumber_Object=MibTableColumn
fs3GCardPhoneNumber=_Fs3GCardPhoneNumber_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,8),_Fs3GCardPhoneNumber_Type())
fs3GCardPhoneNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GCardPhoneNumber.setStatus(_B)
_Fs3GLineDetected_Type=Unsigned32
_Fs3GLineDetected_Object=MibTableColumn
fs3GLineDetected=_Fs3GLineDetected_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,9),_Fs3GLineDetected_Type())
fs3GLineDetected.setMaxAccess(_E)
if mibBuilder.loadTexts:fs3GLineDetected.setStatus(_B)
class _Fs3GLineDetectedResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('noRsponse',0),('pass',1),('failed',2),('using',3),('detecting',4)))
_Fs3GLineDetectedResult_Type.__name__=_D
_Fs3GLineDetectedResult_Object=MibTableColumn
fs3GLineDetectedResult=_Fs3GLineDetectedResult_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,10),_Fs3GLineDetectedResult_Type())
fs3GLineDetectedResult.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GLineDetectedResult.setStatus(_B)
class _Fs3GLineDetectedMainCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_A2,0),('dialFailed',1),('pppFailed',2),(_A3,3)))
_Fs3GLineDetectedMainCause_Type.__name__=_D
_Fs3GLineDetectedMainCause_Object=MibTableColumn
fs3GLineDetectedMainCause=_Fs3GLineDetectedMainCause_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,11),_Fs3GLineDetectedMainCause_Type())
fs3GLineDetectedMainCause.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GLineDetectedMainCause.setStatus(_B)
class _Fs3GLineDetectedSubCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_A2,0),('simCardInvalid',1),('aPNInvalid',2),('powerlower',3),('userInfoError',4),(_A3,5)))
_Fs3GLineDetectedSubCause_Type.__name__=_D
_Fs3GLineDetectedSubCause_Object=MibTableColumn
fs3GLineDetectedSubCause=_Fs3GLineDetectedSubCause_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,12),_Fs3GLineDetectedSubCause_Type())
fs3GLineDetectedSubCause.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GLineDetectedSubCause.setStatus(_B)
class _Fs3GDeviceBackupInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_x,0),(_y,1),(_z,2),('slave',3)))
_Fs3GDeviceBackupInfo_Type.__name__=_D
_Fs3GDeviceBackupInfo_Object=MibTableColumn
fs3GDeviceBackupInfo=_Fs3GDeviceBackupInfo_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,13),_Fs3GDeviceBackupInfo_Type())
fs3GDeviceBackupInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GDeviceBackupInfo.setStatus(_B)
class _Fs3GRssiStrength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-150,0))
_Fs3GRssiStrength_Type.__name__=_D
_Fs3GRssiStrength_Object=MibTableColumn
fs3GRssiStrength=_Fs3GRssiStrength_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,14),_Fs3GRssiStrength_Type())
fs3GRssiStrength.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GRssiStrength.setStatus(_B)
class _Fs3GRssiStrengthPercent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Fs3GRssiStrengthPercent_Type.__name__=_D
_Fs3GRssiStrengthPercent_Object=MibTableColumn
fs3GRssiStrengthPercent=_Fs3GRssiStrengthPercent_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,15),_Fs3GRssiStrengthPercent_Type())
fs3GRssiStrengthPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GRssiStrengthPercent.setStatus(_B)
class _Fs3GNetworkISPMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Y,1),(_Z,2),(_a,3)))
_Fs3GNetworkISPMode_Type.__name__=_D
_Fs3GNetworkISPMode_Object=MibTableColumn
fs3GNetworkISPMode=_Fs3GNetworkISPMode_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,16),_Fs3GNetworkISPMode_Type())
fs3GNetworkISPMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GNetworkISPMode.setStatus(_B)
class _Fs3GNetworkSysMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,15,100,101)));namedValues=NamedValues(*((_P,0),('amps',1),('cdma',2),(_h,3),('hdr',4),('wcdma',5),('gps',6),(_i,7),(_j,8),('td-scdma',15),(_k,100),(_l,101)))
_Fs3GNetworkSysMode_Type.__name__=_D
_Fs3GNetworkSysMode_Object=MibTableColumn
fs3GNetworkSysMode=_Fs3GNetworkSysMode_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,17),_Fs3GNetworkSysMode_Type())
fs3GNetworkSysMode.setMaxAccess(_E)
if mibBuilder.loadTexts:fs3GNetworkSysMode.setStatus(_B)
class _Fs3GNetworkServiceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_P,0),(_m,1),('valid',2),(_n,3),(_o,4)))
_Fs3GNetworkServiceStatus_Type.__name__=_D
_Fs3GNetworkServiceStatus_Object=MibTableColumn
fs3GNetworkServiceStatus=_Fs3GNetworkServiceStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,18),_Fs3GNetworkServiceStatus_Type())
fs3GNetworkServiceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GNetworkServiceStatus.setStatus(_B)
class _Fs3GSIMCardStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,255)));namedValues=NamedValues(*((_r,0),(_s,1),(_t,2),(_u,3),(_v,4),(_w,255)))
_Fs3GSIMCardStatus_Type.__name__=_D
_Fs3GSIMCardStatus_Object=MibTableColumn
fs3GSIMCardStatus=_Fs3GSIMCardStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,19),_Fs3GSIMCardStatus_Type())
fs3GSIMCardStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GSIMCardStatus.setStatus(_B)
class _Fs3GDailMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('dialOnDemand',0),('autoDail',1)))
_Fs3GDailMode_Type.__name__=_D
_Fs3GDailMode_Object=MibTableColumn
fs3GDailMode=_Fs3GDailMode_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,20),_Fs3GDailMode_Type())
fs3GDailMode.setMaxAccess(_E)
if mibBuilder.loadTexts:fs3GDailMode.setStatus(_B)
_Fs3GDeviceBackupIMSI_Type=DisplayString
_Fs3GDeviceBackupIMSI_Object=MibTableColumn
fs3GDeviceBackupIMSI=_Fs3GDeviceBackupIMSI_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,21),_Fs3GDeviceBackupIMSI_Type())
fs3GDeviceBackupIMSI.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GDeviceBackupIMSI.setStatus(_B)
class _Fs3GLineDetectedMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('vpdnMode',0),('ipsecMode',1)))
_Fs3GLineDetectedMode_Type.__name__=_D
_Fs3GLineDetectedMode_Object=MibTableColumn
fs3GLineDetectedMode=_Fs3GLineDetectedMode_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,22),_Fs3GLineDetectedMode_Type())
fs3GLineDetectedMode.setMaxAccess(_E)
if mibBuilder.loadTexts:fs3GLineDetectedMode.setStatus(_B)
_Fs3GPppUsername_Type=DisplayString
_Fs3GPppUsername_Object=MibTableColumn
fs3GPppUsername=_Fs3GPppUsername_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,23),_Fs3GPppUsername_Type())
fs3GPppUsername.setMaxAccess(_E)
if mibBuilder.loadTexts:fs3GPppUsername.setStatus(_B)
_Fs3GUserApn_Type=DisplayString
_Fs3GUserApn_Object=MibTableColumn
fs3GUserApn=_Fs3GUserApn_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,24),_Fs3GUserApn_Type())
fs3GUserApn.setMaxAccess(_E)
if mibBuilder.loadTexts:fs3GUserApn.setStatus(_B)
class _Fs3GModemOnlineStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('minimum-function',0),('fully-function',1),('offline-mode',2),('sim-activate',3),('sim-deactivate',4)))
_Fs3GModemOnlineStatus_Type.__name__=_D
_Fs3GModemOnlineStatus_Object=MibTableColumn
fs3GModemOnlineStatus=_Fs3GModemOnlineStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,25),_Fs3GModemOnlineStatus_Type())
fs3GModemOnlineStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GModemOnlineStatus.setStatus(_B)
class _Fs3GIntfIPAddrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_f,1),(_g,2)))
_Fs3GIntfIPAddrType_Type.__name__=_D
_Fs3GIntfIPAddrType_Object=MibTableColumn
fs3GIntfIPAddrType=_Fs3GIntfIPAddrType_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,26),_Fs3GIntfIPAddrType_Type())
fs3GIntfIPAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GIntfIPAddrType.setStatus(_B)
_Fs3GUserUplineTime_Type=TimeStamp
_Fs3GUserUplineTime_Object=MibTableColumn
fs3GUserUplineTime=_Fs3GUserUplineTime_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,27),_Fs3GUserUplineTime_Type())
fs3GUserUplineTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GUserUplineTime.setStatus(_B)
class _Fs3GUserActiveTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Fs3GUserActiveTime_Type.__name__=_D
_Fs3GUserActiveTime_Object=MibTableColumn
fs3GUserActiveTime=_Fs3GUserActiveTime_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,28),_Fs3GUserActiveTime_Type())
fs3GUserActiveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GUserActiveTime.setStatus(_B)
class _Fs3GSIMRoamingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_p,0),(_q,1)))
_Fs3GSIMRoamingStatus_Type.__name__=_D
_Fs3GSIMRoamingStatus_Object=MibTableColumn
fs3GSIMRoamingStatus=_Fs3GSIMRoamingStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,29),_Fs3GSIMRoamingStatus_Type())
fs3GSIMRoamingStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GSIMRoamingStatus.setStatus(_B)
class _Fs3GAcessBSCellID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Fs3GAcessBSCellID_Type.__name__=_D
_Fs3GAcessBSCellID_Object=MibTableColumn
fs3GAcessBSCellID=_Fs3GAcessBSCellID_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,30),_Fs3GAcessBSCellID_Type())
fs3GAcessBSCellID.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GAcessBSCellID.setStatus(_B)
class _Fs3GAcessBSLAC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Fs3GAcessBSLAC_Type.__name__=_D
_Fs3GAcessBSLAC_Object=MibTableColumn
fs3GAcessBSLAC=_Fs3GAcessBSLAC_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,31),_Fs3GAcessBSLAC_Type())
fs3GAcessBSLAC.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GAcessBSLAC.setStatus(_B)
_Fs3GAcessBSLONG_Type=Integer32
_Fs3GAcessBSLONG_Object=MibTableColumn
fs3GAcessBSLONG=_Fs3GAcessBSLONG_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,32),_Fs3GAcessBSLONG_Type())
fs3GAcessBSLONG.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GAcessBSLONG.setStatus(_B)
_Fs3GAcessBSLAT_Type=Integer32
_Fs3GAcessBSLAT_Object=MibTableColumn
fs3GAcessBSLAT=_Fs3GAcessBSLAT_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,33),_Fs3GAcessBSLAT_Type())
fs3GAcessBSLAT.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GAcessBSLAT.setStatus(_B)
_Fs3GDialOnDemandIfIndex_Type=Integer32
_Fs3GDialOnDemandIfIndex_Object=MibTableColumn
fs3GDialOnDemandIfIndex=_Fs3GDialOnDemandIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,34),_Fs3GDialOnDemandIfIndex_Type())
fs3GDialOnDemandIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GDialOnDemandIfIndex.setStatus(_B)
class _Fs3GTrafficPreventMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_Fs3GTrafficPreventMode_Type.__name__=_D
_Fs3GTrafficPreventMode_Object=MibTableColumn
fs3GTrafficPreventMode=_Fs3GTrafficPreventMode_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,35),_Fs3GTrafficPreventMode_Type())
fs3GTrafficPreventMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GTrafficPreventMode.setStatus(_B)
_Fs3GTrafficPreventIfIndex_Type=Integer32
_Fs3GTrafficPreventIfIndex_Object=MibTableColumn
fs3GTrafficPreventIfIndex=_Fs3GTrafficPreventIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,36),_Fs3GTrafficPreventIfIndex_Type())
fs3GTrafficPreventIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GTrafficPreventIfIndex.setStatus(_B)
_Fs3GTrafficPreventListID_Type=Integer32
_Fs3GTrafficPreventListID_Object=MibTableColumn
fs3GTrafficPreventListID=_Fs3GTrafficPreventListID_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,37),_Fs3GTrafficPreventListID_Type())
fs3GTrafficPreventListID.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GTrafficPreventListID.setStatus(_B)
_Fs3GTrafficPreventListName_Type=DisplayString
_Fs3GTrafficPreventListName_Object=MibTableColumn
fs3GTrafficPreventListName=_Fs3GTrafficPreventListName_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,38),_Fs3GTrafficPreventListName_Type())
fs3GTrafficPreventListName.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GTrafficPreventListName.setStatus(_B)
class _Fs3GDeviceModemType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_A0,1),(_A1,2)))
_Fs3GDeviceModemType_Type.__name__=_D
_Fs3GDeviceModemType_Object=MibTableColumn
fs3GDeviceModemType=_Fs3GDeviceModemType_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,39),_Fs3GDeviceModemType_Type())
fs3GDeviceModemType.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GDeviceModemType.setStatus(_B)
class _Fs3GTrafficTrapInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1440))
_Fs3GTrafficTrapInterval_Type.__name__=_D
_Fs3GTrafficTrapInterval_Object=MibTableColumn
fs3GTrafficTrapInterval=_Fs3GTrafficTrapInterval_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,40),_Fs3GTrafficTrapInterval_Type())
fs3GTrafficTrapInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:fs3GTrafficTrapInterval.setStatus(_B)
class _Fs3GRssiThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-150,0))
_Fs3GRssiThreshold_Type.__name__=_D
_Fs3GRssiThreshold_Object=MibTableColumn
fs3GRssiThreshold=_Fs3GRssiThreshold_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,41),_Fs3GRssiThreshold_Type())
fs3GRssiThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:fs3GRssiThreshold.setStatus(_B)
class _Fs3GTrapFilterMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_Fs3GTrapFilterMode_Type.__name__=_D
_Fs3GTrapFilterMode_Object=MibTableColumn
fs3GTrapFilterMode=_Fs3GTrapFilterMode_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,42),_Fs3GTrapFilterMode_Type())
fs3GTrapFilterMode.setMaxAccess(_E)
if mibBuilder.loadTexts:fs3GTrapFilterMode.setStatus(_B)
class _Fs3GISPtimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,36000))
_Fs3GISPtimeout_Type.__name__=_D
_Fs3GISPtimeout_Object=MibTableColumn
fs3GISPtimeout=_Fs3GISPtimeout_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,43),_Fs3GISPtimeout_Type())
fs3GISPtimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:fs3GISPtimeout.setStatus(_B)
class _Fs3GEncrypt_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,7)));namedValues=NamedValues(*(('encrypt_none',0),('encrypt_temp',7)))
_Fs3GEncrypt_type_Type.__name__=_D
_Fs3GEncrypt_type_Object=MibTableColumn
fs3GEncrypt_type=_Fs3GEncrypt_type_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,44),_Fs3GEncrypt_type_Type())
fs3GEncrypt_type.setMaxAccess(_E)
if mibBuilder.loadTexts:fs3GEncrypt_type.setStatus(_B)
_Fs3GPassword_Type=DisplayString
_Fs3GPassword_Object=MibTableColumn
fs3GPassword=_Fs3GPassword_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,45),_Fs3GPassword_Type())
fs3GPassword.setMaxAccess(_E)
if mibBuilder.loadTexts:fs3GPassword.setStatus(_B)
_Fs3GNetworkISPName_Type=DisplayString
_Fs3GNetworkISPName_Object=MibTableColumn
fs3GNetworkISPName=_Fs3GNetworkISPName_Object((1,3,6,1,4,1,52642,1,1,10,2,95,1,6,1,46),_Fs3GNetworkISPName_Type())
fs3GNetworkISPName.setMaxAccess(_C)
if mibBuilder.loadTexts:fs3GNetworkISPName.setStatus(_B)
_Fs3GTrapNew_ObjectIdentity=ObjectIdentity
fs3GTrapNew=_Fs3GTrapNew_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,95,2))
_Fs3GNotificationsNew_ObjectIdentity=ObjectIdentity
fs3GNotificationsNew=_Fs3GNotificationsNew_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,95,2,1))
fs3GSignalThreshold=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,95,1,3,1,1))
fs3GSignalThreshold.setObjects(*((_A,_F),(_A,_A4),(_A,_A5),(_A,_H)))
if mibBuilder.loadTexts:fs3GSignalThreshold.setStatus(_B)
fs3GUpLine=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,95,1,3,1,2))
fs3GUpLine.setObjects(*((_A,_F),(_A,_Q),(_A,_H),(_A,_A6),(_A,_W),(_A,_A7)))
if mibBuilder.loadTexts:fs3GUpLine.setStatus(_B)
fs3GDownLine=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,95,1,3,1,3))
fs3GDownLine.setObjects(*((_A,_A8),(_A,_F),(_A,_Q),(_A,_H)))
if mibBuilder.loadTexts:fs3GDownLine.setStatus(_B)
fs3GChangeAccessPoint=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,95,1,3,1,4))
fs3GChangeAccessPoint.setObjects(*((_A,_F),(_A,'fs3GApn'),(_A,_Q),(_A,_H)))
if mibBuilder.loadTexts:fs3GChangeAccessPoint.setStatus(_B)
fs3GBackupIntfSwitch=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,95,1,3,1,5))
fs3GBackupIntfSwitch.setObjects(*((_A,_F),(_A,_Q),(_A,_H),(_A,_W),(_A,_A9)))
if mibBuilder.loadTexts:fs3GBackupIntfSwitch.setStatus(_B)
fs3GBaseSationSwitch=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,95,1,3,1,6))
fs3GBaseSationSwitch.setObjects(*((_A,'fs3GISP'),(_A,_AA),(_A,'fs3GLAC'),(_A,'fs3GBSID'),(_A,'fs3GSID'),(_A,'fs3GNID'),(_A,_H),(_A,_AB)))
if mibBuilder.loadTexts:fs3GBaseSationSwitch.setStatus(_B)
fs3GTrafficInformation=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,95,1,3,1,7))
fs3GTrafficInformation.setObjects(*((_A,_F),(_A,_H),(_A,_W),(_A,_b),(_A,_c)))
if mibBuilder.loadTexts:fs3GTrafficInformation.setStatus(_B)
fs3GLineDetectedNotification=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,95,2,1,1))
fs3GLineDetectedNotification.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_d),(_A,_X),(_A,_AG)))
if mibBuilder.loadTexts:fs3GLineDetectedNotification.setStatus(_B)
fs3GUserUpLine=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,95,2,1,2))
fs3GUserUpLine.setObjects(*((_A,_G),(_A,_J),(_A,_K),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_M),(_A,_I),(_A,_N),(_A,_O),(_A,_V),(_A,_L)))
if mibBuilder.loadTexts:fs3GUserUpLine.setStatus(_B)
fs3GUserDownLine=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,95,2,1,3))
fs3GUserDownLine.setObjects(*((_A,_G),(_A,_J),(_A,_K),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_M),(_A,_I),(_A,_N),(_A,_O),(_A,_V),(_A,_L)))
if mibBuilder.loadTexts:fs3GUserDownLine.setStatus(_B)
fs3GRssiNotification=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,95,2,1,4))
fs3GRssiNotification.setObjects(*((_A,_G),(_A,_J),(_A,_I),(_A,_K),(_A,_e),(_A,_X),(_A,_L)))
if mibBuilder.loadTexts:fs3GRssiNotification.setStatus(_B)
fs3GTrafficInfoNotification=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,95,2,1,5))
fs3GTrafficInfoNotification.setObjects(*((_A,_G),(_A,_J),(_A,_I),(_A,_K),(_A,_c),(_A,_b),(_A,_L),(_A,_AH),(_A,_AI),(_A,_N),(_A,_d),(_A,_X),(_A,_e),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_O),(_A,_M),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY)))
if mibBuilder.loadTexts:fs3GTrafficInfoNotification.setStatus(_B)
fs3GBackupMaster=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,95,2,1,6))
fs3GBackupMaster.setObjects(*((_A,_G),(_A,_J),(_A,_K),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_M),(_A,_I),(_A,_N),(_A,_O),(_A,_V),(_A,_L)))
if mibBuilder.loadTexts:fs3GBackupMaster.setStatus(_B)
fs3GBackupSlave=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,95,2,1,7))
fs3GBackupSlave.setObjects(*((_A,_G),(_A,_J),(_A,_K),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_M),(_A,_I),(_A,_N),(_A,_O),(_A,_V),(_A,_L)))
if mibBuilder.loadTexts:fs3GBackupSlave.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'fs3GMonitor':fs3GMonitor,'fs3GObjects':fs3GObjects,'fs3GTable':fs3GTable,'fs3GEntry':fs3GEntry,_Q:fs3gUsername,'fs3GOnlineStatus':fs3GOnlineStatus,'fs3GIMEI':fs3GIMEI,'fs3GIPAddrType':fs3GIPAddrType,_F:fs3GIPAddr,'fs3GUplineTime':fs3GUplineTime,'fs3GActiveTime':fs3GActiveTime,_A4:fs3GSignalStrength,'fs3GISP':fs3GISP,'fs3GSysMode':fs3GSysMode,'fs3GServiceStatus':fs3GServiceStatus,'fs3GRoamingStatus':fs3GRoamingStatus,'fs3GDomain':fs3GDomain,'fs3GSIMStatus':fs3GSIMStatus,_A5:fs3GSignalStrengthPercent,'fs3GApn':fs3GApn,_AA:fs3GCellID,'fs3GLAC':fs3GLAC,'fs3GBSID':fs3GBSID,'fs3GNID':fs3GNID,'fs3GSID':fs3GSID,_H:fs3GIMSI,'fs3GESN':fs3GESN,_AB:fs3GPhoneNumber,'fs3GifIndex':fs3GifIndex,'fs3GBSLONG':fs3GBSLONG,'fs3GBSLAT':fs3GBSLAT,_A6:fs3GBackupInfo,_W:fs3GSerialNumber,_A9:fs3GBackupIMSI,_A7:fs3GGatewayIPAddr,_A8:fs3GLineDownCause,'fs3GModemType':fs3GModemType,'fs3GStatTable':fs3GStatTable,'fs3GStatEntry':fs3GStatEntry,_b:fs3GInOctets,_c:fs3GOutOctets,_AR:fs3GInSpeed,_AS:fs3GOutSpeed,'fs3G2IMSI':fs3G2IMSI,_AT:fs3G2ifIndex,'fs3GTrap':fs3GTrap,'fs3GNotifications':fs3GNotifications,'fs3GSignalThreshold':fs3GSignalThreshold,'fs3GUpLine':fs3GUpLine,'fs3GDownLine':fs3GDownLine,'fs3GChangeAccessPoint':fs3GChangeAccessPoint,'fs3GBackupIntfSwitch':fs3GBackupIntfSwitch,'fs3GBaseSationSwitch':fs3GBaseSationSwitch,'fs3GTrafficInformation':fs3GTrafficInformation,'fs3GBsNumber':fs3GBsNumber,'fs3GBsTable':fs3GBsTable,'fs3GBsEntry':fs3GBsEntry,'fs3GBsSN':fs3GBsSN,'fs3GBsISP':fs3GBsISP,'fs3GBsMode':fs3GBsMode,'fs3GBsIMSI':fs3GBsIMSI,'fs3GBsLAC':fs3GBsLAC,'fs3GBsCellID':fs3GBsCellID,'fs3GBsBSID':fs3GBsBSID,'fs3GBsSID':fs3GBsSID,'fs3GBsNID':fs3GBsNID,'fs3GBsRssi':fs3GBsRssi,'fs3GBsBSLONG':fs3GBsBSLONG,'fs3GBsBSLAT':fs3GBsBSLAT,'fs3GDeviceManagementTable':fs3GDeviceManagementTable,'fs3GDeviceManagementEntry':fs3GDeviceManagementEntry,'fs3GRouterType':fs3GRouterType,_I:fs3GRouterSN,_G:fs3GRouterSlotNumber,_AH:fs3GLineCardType,_J:fs3GCardIMSI,_AI:fs3GModemIMEI,_K:fs3GIntfIPAddr,_N:fs3GCardPhoneNumber,_AC:fs3GLineDetected,_AD:fs3GLineDetectedResult,_AE:fs3GLineDetectedMainCause,_AF:fs3GLineDetectedSubCause,_d:fs3GDeviceBackupInfo,_X:fs3GRssiStrength,_e:fs3GRssiStrengthPercent,_AJ:fs3GNetworkISPMode,_AK:fs3GNetworkSysMode,'fs3GNetworkServiceStatus':fs3GNetworkServiceStatus,_AL:fs3GSIMCardStatus,_O:fs3GDailMode,_AG:fs3GDeviceBackupIMSI,'fs3GLineDetectedMode':fs3GLineDetectedMode,_M:fs3GPppUsername,'fs3GUserApn':fs3GUserApn,'fs3GModemOnlineStatus':fs3GModemOnlineStatus,'fs3GIntfIPAddrType':fs3GIntfIPAddrType,'fs3GUserUplineTime':fs3GUserUplineTime,_AM:fs3GUserActiveTime,'fs3GSIMRoamingStatus':fs3GSIMRoamingStatus,_AN:fs3GAcessBSCellID,_AO:fs3GAcessBSLAC,_AP:fs3GAcessBSLONG,_AQ:fs3GAcessBSLAT,_V:fs3GDialOnDemandIfIndex,_U:fs3GTrafficPreventMode,_T:fs3GTrafficPreventIfIndex,_S:fs3GTrafficPreventListID,_R:fs3GTrafficPreventListName,_L:fs3GDeviceModemType,_AU:fs3GTrafficTrapInterval,_AV:fs3GRssiThreshold,_AW:fs3GTrapFilterMode,_AX:fs3GISPtimeout,'fs3GEncrypt_type':fs3GEncrypt_type,'fs3GPassword':fs3GPassword,_AY:fs3GNetworkISPName,'fs3GTrapNew':fs3GTrapNew,'fs3GNotificationsNew':fs3GNotificationsNew,'fs3GLineDetectedNotification':fs3GLineDetectedNotification,'fs3GUserUpLine':fs3GUserUpLine,'fs3GUserDownLine':fs3GUserDownLine,'fs3GRssiNotification':fs3GRssiNotification,'fs3GTrafficInfoNotification':fs3GTrafficInfoNotification,'fs3GBackupMaster':fs3GBackupMaster,'fs3GBackupSlave':fs3GBackupSlave})