_Ae='qtech3GISPtimeout'
_Ad='qtech3GTrapFilterMode'
_Ac='qtech3GRssiThreshold'
_Ab='qtech3GTrafficTrapInterval'
_Aa='qtech3G2ifIndex'
_AZ='qtech3GOutSpeed'
_AY='qtech3GInSpeed'
_AX='qtech3GAcessBSLAT'
_AW='qtech3GAcessBSLONG'
_AV='qtech3GAcessBSLAC'
_AU='qtech3GAcessBSCellID'
_AT='qtech3GUserActiveTime'
_AS='qtech3GSIMCardStatus'
_AR='qtech3GNetworkSysMode'
_AQ='qtech3GNetworkISPMode'
_AP='qtech3GModemIMEI'
_AO='qtech3GLineCardType'
_AN='qtech3GDeviceBackupIMSI'
_AM='qtech3GLineDetectedSubCause'
_AL='qtech3GLineDetectedMainCause'
_AK='qtech3GLineDetectedResult'
_AJ='qtech3GLineDetected'
_AI='qtech3GPhoneNumber'
_AH='qtech3GNID'
_AG='qtech3GSID'
_AF='qtech3GBSID'
_AE='qtech3GLAC'
_AD='qtech3GCellID'
_AC='qtech3GISP'
_AB='qtech3GBackupIMSI'
_AA='qtech3GApn'
_A9='qtech3GLineDownCause'
_A8='qtech3GGatewayIPAddr'
_A7='qtech3GBackupInfo'
_A6='qtech3GSignalStrengthPercent'
_A5='qtech3GSignalStrength'
_A4='ipsecSetupFailed'
_A3='noGivenReason'
_A2='qtech3GBsSN'
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
_e='qtech3GRssiStrengthPercent'
_d='qtech3GDeviceBackupInfo'
_c='qtech3GOutOctets'
_b='qtech3GInOctets'
_a='chinaMobile'
_Z='chinaTelecom'
_Y='chinaUnicom'
_X='qtech3GRssiStrength'
_W='qtech3GSerialNumber'
_V='qtech3GDialOnDemandIfIndex'
_U='qtech3GTrafficPreventMode'
_T='qtech3GTrafficPreventIfIndex'
_S='qtech3GTrafficPreventListID'
_R='qtech3GTrafficPreventListName'
_Q='qtech3gUsername'
_P='noService'
_O='qtech3GDailMode'
_N='qtech3GCardPhoneNumber'
_M='qtech3GPppUsername'
_L='qtech3GDeviceModemType'
_K='qtech3GIntfIPAddr'
_J='qtech3GCardIMSI'
_I='qtech3GRouterSN'
_H='qtech3GIMSI'
_G='qtech3GRouterSlotNumber'
_F='qtech3GIPAddr'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='current'
_A='QTECH-3G-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
qtech3GMonitor=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,95))
if mibBuilder.loadTexts:qtech3GMonitor.setRevisions(('2011-02-22 00:00',))
_Qtech3GObjects_ObjectIdentity=ObjectIdentity
qtech3GObjects=_Qtech3GObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,95,1))
_Qtech3GTable_Object=MibTable
qtech3GTable=_Qtech3GTable_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,1))
if mibBuilder.loadTexts:qtech3GTable.setStatus(_B)
_Qtech3GEntry_Object=MibTableRow
qtech3GEntry=_Qtech3GEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,1,1))
qtech3GEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:qtech3GEntry.setStatus(_B)
_Qtech3gUsername_Type=DisplayString
_Qtech3gUsername_Object=MibTableColumn
qtech3gUsername=_Qtech3gUsername_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,1,1,1),_Qtech3gUsername_Type())
qtech3gUsername.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3gUsername.setStatus(_B)
class _Qtech3GOnlineStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,4,5,6,7)));namedValues=NamedValues(*(('lpm',0),('online',1),('offline',4),('ftm',5),('reset',6),('rfOff',7)))
_Qtech3GOnlineStatus_Type.__name__=_D
_Qtech3GOnlineStatus_Object=MibTableColumn
qtech3GOnlineStatus=_Qtech3GOnlineStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,1,1,2),_Qtech3GOnlineStatus_Type())
qtech3GOnlineStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GOnlineStatus.setStatus(_B)
_Qtech3GIMEI_Type=DisplayString
_Qtech3GIMEI_Object=MibTableColumn
qtech3GIMEI=_Qtech3GIMEI_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,1,1,3),_Qtech3GIMEI_Type())
qtech3GIMEI.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GIMEI.setStatus(_B)
class _Qtech3GIPAddrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_f,1),(_g,2)))
_Qtech3GIPAddrType_Type.__name__=_D
_Qtech3GIPAddrType_Object=MibTableColumn
qtech3GIPAddrType=_Qtech3GIPAddrType_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,1,1,4),_Qtech3GIPAddrType_Type())
qtech3GIPAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GIPAddrType.setStatus(_B)
_Qtech3GIPAddr_Type=IpAddress
_Qtech3GIPAddr_Object=MibTableColumn
qtech3GIPAddr=_Qtech3GIPAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,1,1,5),_Qtech3GIPAddr_Type())
qtech3GIPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GIPAddr.setStatus(_B)
_Qtech3GUplineTime_Type=TimeStamp
_Qtech3GUplineTime_Object=MibTableColumn
qtech3GUplineTime=_Qtech3GUplineTime_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,1,1,6),_Qtech3GUplineTime_Type())
qtech3GUplineTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GUplineTime.setStatus(_B)
class _Qtech3GActiveTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Qtech3GActiveTime_Type.__name__=_D
_Qtech3GActiveTime_Object=MibTableColumn
qtech3GActiveTime=_Qtech3GActiveTime_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,1,1,7),_Qtech3GActiveTime_Type())
qtech3GActiveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GActiveTime.setStatus(_B)
class _Qtech3GSignalStrength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-150,0))
_Qtech3GSignalStrength_Type.__name__=_D
_Qtech3GSignalStrength_Object=MibTableColumn
qtech3GSignalStrength=_Qtech3GSignalStrength_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,1,1,8),_Qtech3GSignalStrength_Type())
qtech3GSignalStrength.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GSignalStrength.setStatus(_B)
class _Qtech3GISP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Y,1),(_Z,2),(_a,3)))
_Qtech3GISP_Type.__name__=_D
_Qtech3GISP_Object=MibTableColumn
qtech3GISP=_Qtech3GISP_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,1,1,9),_Qtech3GISP_Type())
qtech3GISP.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GISP.setStatus(_B)
class _Qtech3GSysMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,15,100,101)));namedValues=NamedValues(*((_P,0),('amps',1),('cdma',2),(_h,3),('hdr',4),('wcdma',5),('gps',6),(_i,7),(_j,8),('tdscdma',15),(_k,100),(_l,101)))
_Qtech3GSysMode_Type.__name__=_D
_Qtech3GSysMode_Object=MibTableColumn
qtech3GSysMode=_Qtech3GSysMode_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,1,1,10),_Qtech3GSysMode_Type())
qtech3GSysMode.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GSysMode.setStatus(_B)
class _Qtech3GServiceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_P,0),(_m,1),('valid',2),(_n,3),(_o,4)))
_Qtech3GServiceStatus_Type.__name__=_D
_Qtech3GServiceStatus_Object=MibTableColumn
qtech3GServiceStatus=_Qtech3GServiceStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,1,1,11),_Qtech3GServiceStatus_Type())
qtech3GServiceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GServiceStatus.setStatus(_B)
class _Qtech3GRoamingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_p,0),(_q,1)))
_Qtech3GRoamingStatus_Type.__name__=_D
_Qtech3GRoamingStatus_Object=MibTableColumn
qtech3GRoamingStatus=_Qtech3GRoamingStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,1,1,12),_Qtech3GRoamingStatus_Type())
qtech3GRoamingStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GRoamingStatus.setStatus(_B)
class _Qtech3GDomain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,100,255)));namedValues=NamedValues(*((_P,0),('onlyCS',1),('onlyPS',2),('pSCS',3),('pSCSnotRegistered',4),('ePSService',100),('cdmaNotSupport',255)))
_Qtech3GDomain_Type.__name__=_D
_Qtech3GDomain_Object=MibTableColumn
qtech3GDomain=_Qtech3GDomain_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,1,1,13),_Qtech3GDomain_Type())
qtech3GDomain.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GDomain.setStatus(_B)
class _Qtech3GSIMStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,255)));namedValues=NamedValues(*((_r,0),(_s,1),(_t,2),(_u,3),(_v,4),(_w,255)))
_Qtech3GSIMStatus_Type.__name__=_D
_Qtech3GSIMStatus_Object=MibTableColumn
qtech3GSIMStatus=_Qtech3GSIMStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,1,1,14),_Qtech3GSIMStatus_Type())
qtech3GSIMStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GSIMStatus.setStatus(_B)
class _Qtech3GSignalStrengthPercent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Qtech3GSignalStrengthPercent_Type.__name__=_D
_Qtech3GSignalStrengthPercent_Object=MibTableColumn
qtech3GSignalStrengthPercent=_Qtech3GSignalStrengthPercent_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,1,1,15),_Qtech3GSignalStrengthPercent_Type())
qtech3GSignalStrengthPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GSignalStrengthPercent.setStatus(_B)
_Qtech3GApn_Type=DisplayString
_Qtech3GApn_Object=MibTableColumn
qtech3GApn=_Qtech3GApn_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,1,1,16),_Qtech3GApn_Type())
qtech3GApn.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GApn.setStatus(_B)
class _Qtech3GCellID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Qtech3GCellID_Type.__name__=_D
_Qtech3GCellID_Object=MibTableColumn
qtech3GCellID=_Qtech3GCellID_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,1,1,17),_Qtech3GCellID_Type())
qtech3GCellID.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GCellID.setStatus(_B)
class _Qtech3GLAC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Qtech3GLAC_Type.__name__=_D
_Qtech3GLAC_Object=MibTableColumn
qtech3GLAC=_Qtech3GLAC_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,1,1,18),_Qtech3GLAC_Type())
qtech3GLAC.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GLAC.setStatus(_B)
class _Qtech3GBSID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Qtech3GBSID_Type.__name__=_D
_Qtech3GBSID_Object=MibTableColumn
qtech3GBSID=_Qtech3GBSID_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,1,1,19),_Qtech3GBSID_Type())
qtech3GBSID.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GBSID.setStatus(_B)
class _Qtech3GNID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Qtech3GNID_Type.__name__=_D
_Qtech3GNID_Object=MibTableColumn
qtech3GNID=_Qtech3GNID_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,1,1,20),_Qtech3GNID_Type())
qtech3GNID.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GNID.setStatus(_B)
class _Qtech3GSID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Qtech3GSID_Type.__name__=_D
_Qtech3GSID_Object=MibTableColumn
qtech3GSID=_Qtech3GSID_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,1,1,21),_Qtech3GSID_Type())
qtech3GSID.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GSID.setStatus(_B)
_Qtech3GIMSI_Type=DisplayString
_Qtech3GIMSI_Object=MibTableColumn
qtech3GIMSI=_Qtech3GIMSI_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,1,1,22),_Qtech3GIMSI_Type())
qtech3GIMSI.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GIMSI.setStatus(_B)
_Qtech3GESN_Type=DisplayString
_Qtech3GESN_Object=MibTableColumn
qtech3GESN=_Qtech3GESN_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,1,1,23),_Qtech3GESN_Type())
qtech3GESN.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GESN.setStatus(_B)
_Qtech3GPhoneNumber_Type=DisplayString
_Qtech3GPhoneNumber_Object=MibTableColumn
qtech3GPhoneNumber=_Qtech3GPhoneNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,1,1,24),_Qtech3GPhoneNumber_Type())
qtech3GPhoneNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GPhoneNumber.setStatus(_B)
_Qtech3GifIndex_Type=Integer32
_Qtech3GifIndex_Object=MibTableColumn
qtech3GifIndex=_Qtech3GifIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,1,1,25),_Qtech3GifIndex_Type())
qtech3GifIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GifIndex.setStatus(_B)
_Qtech3GBSLONG_Type=Integer32
_Qtech3GBSLONG_Object=MibTableColumn
qtech3GBSLONG=_Qtech3GBSLONG_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,1,1,26),_Qtech3GBSLONG_Type())
qtech3GBSLONG.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GBSLONG.setStatus(_B)
_Qtech3GBSLAT_Type=Integer32
_Qtech3GBSLAT_Object=MibTableColumn
qtech3GBSLAT=_Qtech3GBSLAT_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,1,1,27),_Qtech3GBSLAT_Type())
qtech3GBSLAT.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GBSLAT.setStatus(_B)
class _Qtech3GBackupInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_x,0),(_y,1),(_z,2),('slave',3)))
_Qtech3GBackupInfo_Type.__name__=_D
_Qtech3GBackupInfo_Object=MibTableColumn
qtech3GBackupInfo=_Qtech3GBackupInfo_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,1,1,28),_Qtech3GBackupInfo_Type())
qtech3GBackupInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GBackupInfo.setStatus(_B)
_Qtech3GSerialNumber_Type=DisplayString
_Qtech3GSerialNumber_Object=MibTableColumn
qtech3GSerialNumber=_Qtech3GSerialNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,1,1,29),_Qtech3GSerialNumber_Type())
qtech3GSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GSerialNumber.setStatus(_B)
_Qtech3GBackupIMSI_Type=DisplayString
_Qtech3GBackupIMSI_Object=MibTableColumn
qtech3GBackupIMSI=_Qtech3GBackupIMSI_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,1,1,30),_Qtech3GBackupIMSI_Type())
qtech3GBackupIMSI.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GBackupIMSI.setStatus(_B)
_Qtech3GGatewayIPAddr_Type=IpAddress
_Qtech3GGatewayIPAddr_Object=MibTableColumn
qtech3GGatewayIPAddr=_Qtech3GGatewayIPAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,1,1,31),_Qtech3GGatewayIPAddr_Type())
qtech3GGatewayIPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GGatewayIPAddr.setStatus(_B)
_Qtech3GLineDownCause_Type=Integer32
_Qtech3GLineDownCause_Object=MibTableColumn
qtech3GLineDownCause=_Qtech3GLineDownCause_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,1,1,32),_Qtech3GLineDownCause_Type())
qtech3GLineDownCause.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GLineDownCause.setStatus(_B)
class _Qtech3GModemType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_A0,1),(_A1,2)))
_Qtech3GModemType_Type.__name__=_D
_Qtech3GModemType_Object=MibTableColumn
qtech3GModemType=_Qtech3GModemType_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,1,1,33),_Qtech3GModemType_Type())
qtech3GModemType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GModemType.setStatus(_B)
_Qtech3GStatTable_Object=MibTable
qtech3GStatTable=_Qtech3GStatTable_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,2))
if mibBuilder.loadTexts:qtech3GStatTable.setStatus(_B)
_Qtech3GStatEntry_Object=MibTableRow
qtech3GStatEntry=_Qtech3GStatEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,2,1))
qtech3GStatEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:qtech3GStatEntry.setStatus(_B)
_Qtech3GInOctets_Type=Counter64
_Qtech3GInOctets_Object=MibTableColumn
qtech3GInOctets=_Qtech3GInOctets_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,2,1,1),_Qtech3GInOctets_Type())
qtech3GInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GInOctets.setStatus(_B)
_Qtech3GOutOctets_Type=Counter64
_Qtech3GOutOctets_Object=MibTableColumn
qtech3GOutOctets=_Qtech3GOutOctets_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,2,1,2),_Qtech3GOutOctets_Type())
qtech3GOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GOutOctets.setStatus(_B)
_Qtech3GInSpeed_Type=Counter64
_Qtech3GInSpeed_Object=MibTableColumn
qtech3GInSpeed=_Qtech3GInSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,2,1,3),_Qtech3GInSpeed_Type())
qtech3GInSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GInSpeed.setStatus(_B)
_Qtech3GOutSpeed_Type=Counter64
_Qtech3GOutSpeed_Object=MibTableColumn
qtech3GOutSpeed=_Qtech3GOutSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,2,1,4),_Qtech3GOutSpeed_Type())
qtech3GOutSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GOutSpeed.setStatus(_B)
_Qtech3G2IMSI_Type=DisplayString
_Qtech3G2IMSI_Object=MibTableColumn
qtech3G2IMSI=_Qtech3G2IMSI_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,2,1,5),_Qtech3G2IMSI_Type())
qtech3G2IMSI.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3G2IMSI.setStatus(_B)
_Qtech3G2ifIndex_Type=Integer32
_Qtech3G2ifIndex_Object=MibTableColumn
qtech3G2ifIndex=_Qtech3G2ifIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,2,1,6),_Qtech3G2ifIndex_Type())
qtech3G2ifIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3G2ifIndex.setStatus(_B)
_Qtech3GTrap_ObjectIdentity=ObjectIdentity
qtech3GTrap=_Qtech3GTrap_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,95,1,3))
_Qtech3GNotifications_ObjectIdentity=ObjectIdentity
qtech3GNotifications=_Qtech3GNotifications_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,95,1,3,1))
_Qtech3GBsNumber_Type=Integer32
_Qtech3GBsNumber_Object=MibScalar
qtech3GBsNumber=_Qtech3GBsNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,4),_Qtech3GBsNumber_Type())
qtech3GBsNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GBsNumber.setStatus(_B)
_Qtech3GBsTable_Object=MibTable
qtech3GBsTable=_Qtech3GBsTable_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,5))
if mibBuilder.loadTexts:qtech3GBsTable.setStatus(_B)
_Qtech3GBsEntry_Object=MibTableRow
qtech3GBsEntry=_Qtech3GBsEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,5,1))
qtech3GBsEntry.setIndexNames((0,_A,_A2))
if mibBuilder.loadTexts:qtech3GBsEntry.setStatus(_B)
_Qtech3GBsSN_Type=Integer32
_Qtech3GBsSN_Object=MibTableColumn
qtech3GBsSN=_Qtech3GBsSN_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,5,1,1),_Qtech3GBsSN_Type())
qtech3GBsSN.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GBsSN.setStatus(_B)
class _Qtech3GBsISP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Y,1),(_Z,2),(_a,3)))
_Qtech3GBsISP_Type.__name__=_D
_Qtech3GBsISP_Object=MibTableColumn
qtech3GBsISP=_Qtech3GBsISP_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,5,1,2),_Qtech3GBsISP_Type())
qtech3GBsISP.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GBsISP.setStatus(_B)
class _Qtech3GBsMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sys2GMode',1),('sys3GMode',2)))
_Qtech3GBsMode_Type.__name__=_D
_Qtech3GBsMode_Object=MibTableColumn
qtech3GBsMode=_Qtech3GBsMode_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,5,1,3),_Qtech3GBsMode_Type())
qtech3GBsMode.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GBsMode.setStatus(_B)
_Qtech3GBsIMSI_Type=DisplayString
_Qtech3GBsIMSI_Object=MibTableColumn
qtech3GBsIMSI=_Qtech3GBsIMSI_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,5,1,4),_Qtech3GBsIMSI_Type())
qtech3GBsIMSI.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GBsIMSI.setStatus(_B)
_Qtech3GBsLAC_Type=Integer32
_Qtech3GBsLAC_Object=MibTableColumn
qtech3GBsLAC=_Qtech3GBsLAC_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,5,1,5),_Qtech3GBsLAC_Type())
qtech3GBsLAC.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GBsLAC.setStatus(_B)
_Qtech3GBsCellID_Type=Integer32
_Qtech3GBsCellID_Object=MibTableColumn
qtech3GBsCellID=_Qtech3GBsCellID_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,5,1,6),_Qtech3GBsCellID_Type())
qtech3GBsCellID.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GBsCellID.setStatus(_B)
_Qtech3GBsBSID_Type=Integer32
_Qtech3GBsBSID_Object=MibTableColumn
qtech3GBsBSID=_Qtech3GBsBSID_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,5,1,7),_Qtech3GBsBSID_Type())
qtech3GBsBSID.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GBsBSID.setStatus(_B)
_Qtech3GBsSID_Type=Integer32
_Qtech3GBsSID_Object=MibTableColumn
qtech3GBsSID=_Qtech3GBsSID_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,5,1,8),_Qtech3GBsSID_Type())
qtech3GBsSID.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GBsSID.setStatus(_B)
_Qtech3GBsNID_Type=Integer32
_Qtech3GBsNID_Object=MibTableColumn
qtech3GBsNID=_Qtech3GBsNID_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,5,1,9),_Qtech3GBsNID_Type())
qtech3GBsNID.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GBsNID.setStatus(_B)
_Qtech3GBsRssi_Type=Integer32
_Qtech3GBsRssi_Object=MibTableColumn
qtech3GBsRssi=_Qtech3GBsRssi_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,5,1,10),_Qtech3GBsRssi_Type())
qtech3GBsRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GBsRssi.setStatus(_B)
_Qtech3GBsBSLONG_Type=Integer32
_Qtech3GBsBSLONG_Object=MibTableColumn
qtech3GBsBSLONG=_Qtech3GBsBSLONG_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,5,1,11),_Qtech3GBsBSLONG_Type())
qtech3GBsBSLONG.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GBsBSLONG.setStatus(_B)
_Qtech3GBsBSLAT_Type=Integer32
_Qtech3GBsBSLAT_Object=MibTableColumn
qtech3GBsBSLAT=_Qtech3GBsBSLAT_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,5,1,12),_Qtech3GBsBSLAT_Type())
qtech3GBsBSLAT.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GBsBSLAT.setStatus(_B)
_Qtech3GDeviceManagementTable_Object=MibTable
qtech3GDeviceManagementTable=_Qtech3GDeviceManagementTable_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6))
if mibBuilder.loadTexts:qtech3GDeviceManagementTable.setStatus(_B)
_Qtech3GDeviceManagementEntry_Object=MibTableRow
qtech3GDeviceManagementEntry=_Qtech3GDeviceManagementEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1))
qtech3GDeviceManagementEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:qtech3GDeviceManagementEntry.setStatus(_B)
_Qtech3GRouterType_Type=DisplayString
_Qtech3GRouterType_Object=MibTableColumn
qtech3GRouterType=_Qtech3GRouterType_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,1),_Qtech3GRouterType_Type())
qtech3GRouterType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GRouterType.setStatus(_B)
_Qtech3GRouterSN_Type=DisplayString
_Qtech3GRouterSN_Object=MibTableColumn
qtech3GRouterSN=_Qtech3GRouterSN_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,2),_Qtech3GRouterSN_Type())
qtech3GRouterSN.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GRouterSN.setStatus(_B)
_Qtech3GRouterSlotNumber_Type=DisplayString
_Qtech3GRouterSlotNumber_Object=MibTableColumn
qtech3GRouterSlotNumber=_Qtech3GRouterSlotNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,3),_Qtech3GRouterSlotNumber_Type())
qtech3GRouterSlotNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GRouterSlotNumber.setStatus(_B)
_Qtech3GLineCardType_Type=DisplayString
_Qtech3GLineCardType_Object=MibTableColumn
qtech3GLineCardType=_Qtech3GLineCardType_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,4),_Qtech3GLineCardType_Type())
qtech3GLineCardType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GLineCardType.setStatus(_B)
_Qtech3GCardIMSI_Type=DisplayString
_Qtech3GCardIMSI_Object=MibTableColumn
qtech3GCardIMSI=_Qtech3GCardIMSI_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,5),_Qtech3GCardIMSI_Type())
qtech3GCardIMSI.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GCardIMSI.setStatus(_B)
_Qtech3GModemIMEI_Type=DisplayString
_Qtech3GModemIMEI_Object=MibTableColumn
qtech3GModemIMEI=_Qtech3GModemIMEI_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,6),_Qtech3GModemIMEI_Type())
qtech3GModemIMEI.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GModemIMEI.setStatus(_B)
_Qtech3GIntfIPAddr_Type=IpAddress
_Qtech3GIntfIPAddr_Object=MibTableColumn
qtech3GIntfIPAddr=_Qtech3GIntfIPAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,7),_Qtech3GIntfIPAddr_Type())
qtech3GIntfIPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GIntfIPAddr.setStatus(_B)
_Qtech3GCardPhoneNumber_Type=DisplayString
_Qtech3GCardPhoneNumber_Object=MibTableColumn
qtech3GCardPhoneNumber=_Qtech3GCardPhoneNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,8),_Qtech3GCardPhoneNumber_Type())
qtech3GCardPhoneNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GCardPhoneNumber.setStatus(_B)
_Qtech3GLineDetected_Type=Unsigned32
_Qtech3GLineDetected_Object=MibTableColumn
qtech3GLineDetected=_Qtech3GLineDetected_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,9),_Qtech3GLineDetected_Type())
qtech3GLineDetected.setMaxAccess(_E)
if mibBuilder.loadTexts:qtech3GLineDetected.setStatus(_B)
class _Qtech3GLineDetectedResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('noRsponse',0),('pass',1),('failed',2),('using',3),('detecting',4)))
_Qtech3GLineDetectedResult_Type.__name__=_D
_Qtech3GLineDetectedResult_Object=MibTableColumn
qtech3GLineDetectedResult=_Qtech3GLineDetectedResult_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,10),_Qtech3GLineDetectedResult_Type())
qtech3GLineDetectedResult.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GLineDetectedResult.setStatus(_B)
class _Qtech3GLineDetectedMainCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_A3,0),('dialFailed',1),('pppFailed',2),(_A4,3)))
_Qtech3GLineDetectedMainCause_Type.__name__=_D
_Qtech3GLineDetectedMainCause_Object=MibTableColumn
qtech3GLineDetectedMainCause=_Qtech3GLineDetectedMainCause_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,11),_Qtech3GLineDetectedMainCause_Type())
qtech3GLineDetectedMainCause.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GLineDetectedMainCause.setStatus(_B)
class _Qtech3GLineDetectedSubCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_A3,0),('simCardInvalid',1),('aPNInvalid',2),('powerlower',3),('userInfoError',4),(_A4,5)))
_Qtech3GLineDetectedSubCause_Type.__name__=_D
_Qtech3GLineDetectedSubCause_Object=MibTableColumn
qtech3GLineDetectedSubCause=_Qtech3GLineDetectedSubCause_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,12),_Qtech3GLineDetectedSubCause_Type())
qtech3GLineDetectedSubCause.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GLineDetectedSubCause.setStatus(_B)
class _Qtech3GDeviceBackupInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_x,0),(_y,1),(_z,2),('slave',3)))
_Qtech3GDeviceBackupInfo_Type.__name__=_D
_Qtech3GDeviceBackupInfo_Object=MibTableColumn
qtech3GDeviceBackupInfo=_Qtech3GDeviceBackupInfo_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,13),_Qtech3GDeviceBackupInfo_Type())
qtech3GDeviceBackupInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GDeviceBackupInfo.setStatus(_B)
class _Qtech3GRssiStrength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-150,0))
_Qtech3GRssiStrength_Type.__name__=_D
_Qtech3GRssiStrength_Object=MibTableColumn
qtech3GRssiStrength=_Qtech3GRssiStrength_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,14),_Qtech3GRssiStrength_Type())
qtech3GRssiStrength.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GRssiStrength.setStatus(_B)
class _Qtech3GRssiStrengthPercent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Qtech3GRssiStrengthPercent_Type.__name__=_D
_Qtech3GRssiStrengthPercent_Object=MibTableColumn
qtech3GRssiStrengthPercent=_Qtech3GRssiStrengthPercent_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,15),_Qtech3GRssiStrengthPercent_Type())
qtech3GRssiStrengthPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GRssiStrengthPercent.setStatus(_B)
class _Qtech3GNetworkISPMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Y,1),(_Z,2),(_a,3)))
_Qtech3GNetworkISPMode_Type.__name__=_D
_Qtech3GNetworkISPMode_Object=MibTableColumn
qtech3GNetworkISPMode=_Qtech3GNetworkISPMode_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,16),_Qtech3GNetworkISPMode_Type())
qtech3GNetworkISPMode.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GNetworkISPMode.setStatus(_B)
class _Qtech3GNetworkSysMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,15,100,101)));namedValues=NamedValues(*((_P,0),('amps',1),('cdma',2),(_h,3),('hdr',4),('wcdma',5),('gps',6),(_i,7),(_j,8),('td-scdma',15),(_k,100),(_l,101)))
_Qtech3GNetworkSysMode_Type.__name__=_D
_Qtech3GNetworkSysMode_Object=MibTableColumn
qtech3GNetworkSysMode=_Qtech3GNetworkSysMode_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,17),_Qtech3GNetworkSysMode_Type())
qtech3GNetworkSysMode.setMaxAccess(_E)
if mibBuilder.loadTexts:qtech3GNetworkSysMode.setStatus(_B)
class _Qtech3GNetworkServiceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_P,0),(_m,1),('valid',2),(_n,3),(_o,4)))
_Qtech3GNetworkServiceStatus_Type.__name__=_D
_Qtech3GNetworkServiceStatus_Object=MibTableColumn
qtech3GNetworkServiceStatus=_Qtech3GNetworkServiceStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,18),_Qtech3GNetworkServiceStatus_Type())
qtech3GNetworkServiceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GNetworkServiceStatus.setStatus(_B)
class _Qtech3GSIMCardStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,255)));namedValues=NamedValues(*((_r,0),(_s,1),(_t,2),(_u,3),(_v,4),(_w,255)))
_Qtech3GSIMCardStatus_Type.__name__=_D
_Qtech3GSIMCardStatus_Object=MibTableColumn
qtech3GSIMCardStatus=_Qtech3GSIMCardStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,19),_Qtech3GSIMCardStatus_Type())
qtech3GSIMCardStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GSIMCardStatus.setStatus(_B)
class _Qtech3GDailMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('dialOnDemand',0),('autoDail',1)))
_Qtech3GDailMode_Type.__name__=_D
_Qtech3GDailMode_Object=MibTableColumn
qtech3GDailMode=_Qtech3GDailMode_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,20),_Qtech3GDailMode_Type())
qtech3GDailMode.setMaxAccess(_E)
if mibBuilder.loadTexts:qtech3GDailMode.setStatus(_B)
_Qtech3GDeviceBackupIMSI_Type=DisplayString
_Qtech3GDeviceBackupIMSI_Object=MibTableColumn
qtech3GDeviceBackupIMSI=_Qtech3GDeviceBackupIMSI_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,21),_Qtech3GDeviceBackupIMSI_Type())
qtech3GDeviceBackupIMSI.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GDeviceBackupIMSI.setStatus(_B)
class _Qtech3GLineDetectedMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('vpdnMode',0),('ipsecMode',1)))
_Qtech3GLineDetectedMode_Type.__name__=_D
_Qtech3GLineDetectedMode_Object=MibTableColumn
qtech3GLineDetectedMode=_Qtech3GLineDetectedMode_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,22),_Qtech3GLineDetectedMode_Type())
qtech3GLineDetectedMode.setMaxAccess(_E)
if mibBuilder.loadTexts:qtech3GLineDetectedMode.setStatus(_B)
_Qtech3GPppUsername_Type=DisplayString
_Qtech3GPppUsername_Object=MibTableColumn
qtech3GPppUsername=_Qtech3GPppUsername_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,23),_Qtech3GPppUsername_Type())
qtech3GPppUsername.setMaxAccess(_E)
if mibBuilder.loadTexts:qtech3GPppUsername.setStatus(_B)
_Qtech3GUserApn_Type=DisplayString
_Qtech3GUserApn_Object=MibTableColumn
qtech3GUserApn=_Qtech3GUserApn_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,24),_Qtech3GUserApn_Type())
qtech3GUserApn.setMaxAccess(_E)
if mibBuilder.loadTexts:qtech3GUserApn.setStatus(_B)
class _Qtech3GModemOnlineStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('minimum-function',0),('fully-function',1),('offline-mode',2),('sim-activate',3),('sim-deactivate',4)))
_Qtech3GModemOnlineStatus_Type.__name__=_D
_Qtech3GModemOnlineStatus_Object=MibTableColumn
qtech3GModemOnlineStatus=_Qtech3GModemOnlineStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,25),_Qtech3GModemOnlineStatus_Type())
qtech3GModemOnlineStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GModemOnlineStatus.setStatus(_B)
class _Qtech3GIntfIPAddrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_f,1),(_g,2)))
_Qtech3GIntfIPAddrType_Type.__name__=_D
_Qtech3GIntfIPAddrType_Object=MibTableColumn
qtech3GIntfIPAddrType=_Qtech3GIntfIPAddrType_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,26),_Qtech3GIntfIPAddrType_Type())
qtech3GIntfIPAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GIntfIPAddrType.setStatus(_B)
_Qtech3GUserUplineTime_Type=TimeStamp
_Qtech3GUserUplineTime_Object=MibTableColumn
qtech3GUserUplineTime=_Qtech3GUserUplineTime_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,27),_Qtech3GUserUplineTime_Type())
qtech3GUserUplineTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GUserUplineTime.setStatus(_B)
class _Qtech3GUserActiveTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Qtech3GUserActiveTime_Type.__name__=_D
_Qtech3GUserActiveTime_Object=MibTableColumn
qtech3GUserActiveTime=_Qtech3GUserActiveTime_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,28),_Qtech3GUserActiveTime_Type())
qtech3GUserActiveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GUserActiveTime.setStatus(_B)
class _Qtech3GSIMRoamingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_p,0),(_q,1)))
_Qtech3GSIMRoamingStatus_Type.__name__=_D
_Qtech3GSIMRoamingStatus_Object=MibTableColumn
qtech3GSIMRoamingStatus=_Qtech3GSIMRoamingStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,29),_Qtech3GSIMRoamingStatus_Type())
qtech3GSIMRoamingStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GSIMRoamingStatus.setStatus(_B)
class _Qtech3GAcessBSCellID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Qtech3GAcessBSCellID_Type.__name__=_D
_Qtech3GAcessBSCellID_Object=MibTableColumn
qtech3GAcessBSCellID=_Qtech3GAcessBSCellID_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,30),_Qtech3GAcessBSCellID_Type())
qtech3GAcessBSCellID.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GAcessBSCellID.setStatus(_B)
class _Qtech3GAcessBSLAC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Qtech3GAcessBSLAC_Type.__name__=_D
_Qtech3GAcessBSLAC_Object=MibTableColumn
qtech3GAcessBSLAC=_Qtech3GAcessBSLAC_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,31),_Qtech3GAcessBSLAC_Type())
qtech3GAcessBSLAC.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GAcessBSLAC.setStatus(_B)
_Qtech3GAcessBSLONG_Type=Integer32
_Qtech3GAcessBSLONG_Object=MibTableColumn
qtech3GAcessBSLONG=_Qtech3GAcessBSLONG_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,32),_Qtech3GAcessBSLONG_Type())
qtech3GAcessBSLONG.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GAcessBSLONG.setStatus(_B)
_Qtech3GAcessBSLAT_Type=Integer32
_Qtech3GAcessBSLAT_Object=MibTableColumn
qtech3GAcessBSLAT=_Qtech3GAcessBSLAT_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,33),_Qtech3GAcessBSLAT_Type())
qtech3GAcessBSLAT.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GAcessBSLAT.setStatus(_B)
_Qtech3GDialOnDemandIfIndex_Type=Integer32
_Qtech3GDialOnDemandIfIndex_Object=MibTableColumn
qtech3GDialOnDemandIfIndex=_Qtech3GDialOnDemandIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,34),_Qtech3GDialOnDemandIfIndex_Type())
qtech3GDialOnDemandIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GDialOnDemandIfIndex.setStatus(_B)
class _Qtech3GTrafficPreventMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_Qtech3GTrafficPreventMode_Type.__name__=_D
_Qtech3GTrafficPreventMode_Object=MibTableColumn
qtech3GTrafficPreventMode=_Qtech3GTrafficPreventMode_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,35),_Qtech3GTrafficPreventMode_Type())
qtech3GTrafficPreventMode.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GTrafficPreventMode.setStatus(_B)
_Qtech3GTrafficPreventIfIndex_Type=Integer32
_Qtech3GTrafficPreventIfIndex_Object=MibTableColumn
qtech3GTrafficPreventIfIndex=_Qtech3GTrafficPreventIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,36),_Qtech3GTrafficPreventIfIndex_Type())
qtech3GTrafficPreventIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GTrafficPreventIfIndex.setStatus(_B)
_Qtech3GTrafficPreventListID_Type=Integer32
_Qtech3GTrafficPreventListID_Object=MibTableColumn
qtech3GTrafficPreventListID=_Qtech3GTrafficPreventListID_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,37),_Qtech3GTrafficPreventListID_Type())
qtech3GTrafficPreventListID.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GTrafficPreventListID.setStatus(_B)
_Qtech3GTrafficPreventListName_Type=DisplayString
_Qtech3GTrafficPreventListName_Object=MibTableColumn
qtech3GTrafficPreventListName=_Qtech3GTrafficPreventListName_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,38),_Qtech3GTrafficPreventListName_Type())
qtech3GTrafficPreventListName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GTrafficPreventListName.setStatus(_B)
class _Qtech3GDeviceModemType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_A0,1),(_A1,2)))
_Qtech3GDeviceModemType_Type.__name__=_D
_Qtech3GDeviceModemType_Object=MibTableColumn
qtech3GDeviceModemType=_Qtech3GDeviceModemType_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,39),_Qtech3GDeviceModemType_Type())
qtech3GDeviceModemType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech3GDeviceModemType.setStatus(_B)
class _Qtech3GTrafficTrapInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1440))
_Qtech3GTrafficTrapInterval_Type.__name__=_D
_Qtech3GTrafficTrapInterval_Object=MibTableColumn
qtech3GTrafficTrapInterval=_Qtech3GTrafficTrapInterval_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,40),_Qtech3GTrafficTrapInterval_Type())
qtech3GTrafficTrapInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:qtech3GTrafficTrapInterval.setStatus(_B)
class _Qtech3GRssiThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-150,0))
_Qtech3GRssiThreshold_Type.__name__=_D
_Qtech3GRssiThreshold_Object=MibTableColumn
qtech3GRssiThreshold=_Qtech3GRssiThreshold_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,41),_Qtech3GRssiThreshold_Type())
qtech3GRssiThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:qtech3GRssiThreshold.setStatus(_B)
class _Qtech3GTrapFilterMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_Qtech3GTrapFilterMode_Type.__name__=_D
_Qtech3GTrapFilterMode_Object=MibTableColumn
qtech3GTrapFilterMode=_Qtech3GTrapFilterMode_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,42),_Qtech3GTrapFilterMode_Type())
qtech3GTrapFilterMode.setMaxAccess(_E)
if mibBuilder.loadTexts:qtech3GTrapFilterMode.setStatus(_B)
class _Qtech3GISPtimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,36000))
_Qtech3GISPtimeout_Type.__name__=_D
_Qtech3GISPtimeout_Object=MibTableColumn
qtech3GISPtimeout=_Qtech3GISPtimeout_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,43),_Qtech3GISPtimeout_Type())
qtech3GISPtimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:qtech3GISPtimeout.setStatus(_B)
class _Qtech3GEncrypt_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,7)));namedValues=NamedValues(*(('ENCRYPT_NONE',0),('ENCRYPT_TEMP',7)))
_Qtech3GEncrypt_type_Type.__name__=_D
_Qtech3GEncrypt_type_Object=MibTableColumn
qtech3GEncrypt_type=_Qtech3GEncrypt_type_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,44),_Qtech3GEncrypt_type_Type())
qtech3GEncrypt_type.setMaxAccess(_E)
if mibBuilder.loadTexts:qtech3GEncrypt_type.setStatus(_B)
_Qtech3GPassword_Type=DisplayString
_Qtech3GPassword_Object=MibTableColumn
qtech3GPassword=_Qtech3GPassword_Object((1,3,6,1,4,1,27514,1,1,10,2,95,1,6,1,45),_Qtech3GPassword_Type())
qtech3GPassword.setMaxAccess(_E)
if mibBuilder.loadTexts:qtech3GPassword.setStatus(_B)
_Qtech3GTrapNew_ObjectIdentity=ObjectIdentity
qtech3GTrapNew=_Qtech3GTrapNew_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,95,2))
_Qtech3GNotificationsNew_ObjectIdentity=ObjectIdentity
qtech3GNotificationsNew=_Qtech3GNotificationsNew_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,95,2,1))
qtech3GSignalThreshold=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,95,1,3,1,1))
qtech3GSignalThreshold.setObjects(*((_A,_F),(_A,_A5),(_A,_A6),(_A,_H)))
if mibBuilder.loadTexts:qtech3GSignalThreshold.setStatus(_B)
qtech3GUpLine=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,95,1,3,1,2))
qtech3GUpLine.setObjects(*((_A,_F),(_A,_Q),(_A,_H),(_A,_A7),(_A,_W),(_A,_A8)))
if mibBuilder.loadTexts:qtech3GUpLine.setStatus(_B)
qtech3GDownLine=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,95,1,3,1,3))
qtech3GDownLine.setObjects(*((_A,_A9),(_A,_F),(_A,_Q),(_A,_H)))
if mibBuilder.loadTexts:qtech3GDownLine.setStatus(_B)
qtech3GChangeAccessPoint=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,95,1,3,1,4))
qtech3GChangeAccessPoint.setObjects(*((_A,_F),(_A,_AA),(_A,_Q),(_A,_H)))
if mibBuilder.loadTexts:qtech3GChangeAccessPoint.setStatus(_B)
qtech3GBackupIntfSwitch=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,95,1,3,1,5))
qtech3GBackupIntfSwitch.setObjects(*((_A,_F),(_A,_Q),(_A,_H),(_A,_W),(_A,_AB)))
if mibBuilder.loadTexts:qtech3GBackupIntfSwitch.setStatus(_B)
qtech3GBaseSationSwitch=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,95,1,3,1,6))
qtech3GBaseSationSwitch.setObjects(*((_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_H),(_A,_AI)))
if mibBuilder.loadTexts:qtech3GBaseSationSwitch.setStatus(_B)
qtech3GTrafficInformation=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,95,1,3,1,7))
qtech3GTrafficInformation.setObjects(*((_A,_F),(_A,_H),(_A,_W),(_A,_b),(_A,_c)))
if mibBuilder.loadTexts:qtech3GTrafficInformation.setStatus(_B)
qtech3GLineDetectedNotification=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,95,2,1,1))
qtech3GLineDetectedNotification.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_d),(_A,_X),(_A,_AN)))
if mibBuilder.loadTexts:qtech3GLineDetectedNotification.setStatus(_B)
qtech3GUserUpLine=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,95,2,1,2))
qtech3GUserUpLine.setObjects(*((_A,_G),(_A,_J),(_A,_K),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_M),(_A,_I),(_A,_N),(_A,_O),(_A,_V),(_A,_L)))
if mibBuilder.loadTexts:qtech3GUserUpLine.setStatus(_B)
qtech3GUserDownLine=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,95,2,1,3))
qtech3GUserDownLine.setObjects(*((_A,_G),(_A,_J),(_A,_K),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_M),(_A,_I),(_A,_N),(_A,_O),(_A,_V),(_A,_L)))
if mibBuilder.loadTexts:qtech3GUserDownLine.setStatus(_B)
qtech3GRssiNotification=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,95,2,1,4))
qtech3GRssiNotification.setObjects(*((_A,_G),(_A,_J),(_A,_I),(_A,_K),(_A,_e),(_A,_X),(_A,_L)))
if mibBuilder.loadTexts:qtech3GRssiNotification.setStatus(_B)
qtech3GTrafficInfoNotification=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,95,2,1,5))
qtech3GTrafficInfoNotification.setObjects(*((_A,_G),(_A,_J),(_A,_I),(_A,_K),(_A,_c),(_A,_b),(_A,_L),(_A,_AO),(_A,_AP),(_A,_N),(_A,_d),(_A,_X),(_A,_e),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_O),(_A,_M),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae)))
if mibBuilder.loadTexts:qtech3GTrafficInfoNotification.setStatus(_B)
qtech3GBackupMaster=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,95,2,1,6))
qtech3GBackupMaster.setObjects(*((_A,_G),(_A,_J),(_A,_K),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_M),(_A,_I),(_A,_N),(_A,_O),(_A,_V),(_A,_L)))
if mibBuilder.loadTexts:qtech3GBackupMaster.setStatus(_B)
qtech3GBackupSlave=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,95,2,1,7))
qtech3GBackupSlave.setObjects(*((_A,_G),(_A,_J),(_A,_K),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_M),(_A,_I),(_A,_N),(_A,_O),(_A,_V),(_A,_L)))
if mibBuilder.loadTexts:qtech3GBackupSlave.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'qtech3GMonitor':qtech3GMonitor,'qtech3GObjects':qtech3GObjects,'qtech3GTable':qtech3GTable,'qtech3GEntry':qtech3GEntry,_Q:qtech3gUsername,'qtech3GOnlineStatus':qtech3GOnlineStatus,'qtech3GIMEI':qtech3GIMEI,'qtech3GIPAddrType':qtech3GIPAddrType,_F:qtech3GIPAddr,'qtech3GUplineTime':qtech3GUplineTime,'qtech3GActiveTime':qtech3GActiveTime,_A5:qtech3GSignalStrength,_AC:qtech3GISP,'qtech3GSysMode':qtech3GSysMode,'qtech3GServiceStatus':qtech3GServiceStatus,'qtech3GRoamingStatus':qtech3GRoamingStatus,'qtech3GDomain':qtech3GDomain,'qtech3GSIMStatus':qtech3GSIMStatus,_A6:qtech3GSignalStrengthPercent,_AA:qtech3GApn,_AD:qtech3GCellID,_AE:qtech3GLAC,_AF:qtech3GBSID,_AH:qtech3GNID,_AG:qtech3GSID,_H:qtech3GIMSI,'qtech3GESN':qtech3GESN,_AI:qtech3GPhoneNumber,'qtech3GifIndex':qtech3GifIndex,'qtech3GBSLONG':qtech3GBSLONG,'qtech3GBSLAT':qtech3GBSLAT,_A7:qtech3GBackupInfo,_W:qtech3GSerialNumber,_AB:qtech3GBackupIMSI,_A8:qtech3GGatewayIPAddr,_A9:qtech3GLineDownCause,'qtech3GModemType':qtech3GModemType,'qtech3GStatTable':qtech3GStatTable,'qtech3GStatEntry':qtech3GStatEntry,_b:qtech3GInOctets,_c:qtech3GOutOctets,_AY:qtech3GInSpeed,_AZ:qtech3GOutSpeed,'qtech3G2IMSI':qtech3G2IMSI,_Aa:qtech3G2ifIndex,'qtech3GTrap':qtech3GTrap,'qtech3GNotifications':qtech3GNotifications,'qtech3GSignalThreshold':qtech3GSignalThreshold,'qtech3GUpLine':qtech3GUpLine,'qtech3GDownLine':qtech3GDownLine,'qtech3GChangeAccessPoint':qtech3GChangeAccessPoint,'qtech3GBackupIntfSwitch':qtech3GBackupIntfSwitch,'qtech3GBaseSationSwitch':qtech3GBaseSationSwitch,'qtech3GTrafficInformation':qtech3GTrafficInformation,'qtech3GBsNumber':qtech3GBsNumber,'qtech3GBsTable':qtech3GBsTable,'qtech3GBsEntry':qtech3GBsEntry,_A2:qtech3GBsSN,'qtech3GBsISP':qtech3GBsISP,'qtech3GBsMode':qtech3GBsMode,'qtech3GBsIMSI':qtech3GBsIMSI,'qtech3GBsLAC':qtech3GBsLAC,'qtech3GBsCellID':qtech3GBsCellID,'qtech3GBsBSID':qtech3GBsBSID,'qtech3GBsSID':qtech3GBsSID,'qtech3GBsNID':qtech3GBsNID,'qtech3GBsRssi':qtech3GBsRssi,'qtech3GBsBSLONG':qtech3GBsBSLONG,'qtech3GBsBSLAT':qtech3GBsBSLAT,'qtech3GDeviceManagementTable':qtech3GDeviceManagementTable,'qtech3GDeviceManagementEntry':qtech3GDeviceManagementEntry,'qtech3GRouterType':qtech3GRouterType,_I:qtech3GRouterSN,_G:qtech3GRouterSlotNumber,_AO:qtech3GLineCardType,_J:qtech3GCardIMSI,_AP:qtech3GModemIMEI,_K:qtech3GIntfIPAddr,_N:qtech3GCardPhoneNumber,_AJ:qtech3GLineDetected,_AK:qtech3GLineDetectedResult,_AL:qtech3GLineDetectedMainCause,_AM:qtech3GLineDetectedSubCause,_d:qtech3GDeviceBackupInfo,_X:qtech3GRssiStrength,_e:qtech3GRssiStrengthPercent,_AQ:qtech3GNetworkISPMode,_AR:qtech3GNetworkSysMode,'qtech3GNetworkServiceStatus':qtech3GNetworkServiceStatus,_AS:qtech3GSIMCardStatus,_O:qtech3GDailMode,_AN:qtech3GDeviceBackupIMSI,'qtech3GLineDetectedMode':qtech3GLineDetectedMode,_M:qtech3GPppUsername,'qtech3GUserApn':qtech3GUserApn,'qtech3GModemOnlineStatus':qtech3GModemOnlineStatus,'qtech3GIntfIPAddrType':qtech3GIntfIPAddrType,'qtech3GUserUplineTime':qtech3GUserUplineTime,_AT:qtech3GUserActiveTime,'qtech3GSIMRoamingStatus':qtech3GSIMRoamingStatus,_AU:qtech3GAcessBSCellID,_AV:qtech3GAcessBSLAC,_AW:qtech3GAcessBSLONG,_AX:qtech3GAcessBSLAT,_V:qtech3GDialOnDemandIfIndex,_U:qtech3GTrafficPreventMode,_T:qtech3GTrafficPreventIfIndex,_S:qtech3GTrafficPreventListID,_R:qtech3GTrafficPreventListName,_L:qtech3GDeviceModemType,_Ab:qtech3GTrafficTrapInterval,_Ac:qtech3GRssiThreshold,_Ad:qtech3GTrapFilterMode,_Ae:qtech3GISPtimeout,'qtech3GEncrypt_type':qtech3GEncrypt_type,'qtech3GPassword':qtech3GPassword,'qtech3GTrapNew':qtech3GTrapNew,'qtech3GNotificationsNew':qtech3GNotificationsNew,'qtech3GLineDetectedNotification':qtech3GLineDetectedNotification,'qtech3GUserUpLine':qtech3GUserUpLine,'qtech3GUserDownLine':qtech3GUserDownLine,'qtech3GRssiNotification':qtech3GRssiNotification,'qtech3GTrafficInfoNotification':qtech3GTrafficInfoNotification,'qtech3GBackupMaster':qtech3GBackupMaster,'qtech3GBackupSlave':qtech3GBackupSlave})