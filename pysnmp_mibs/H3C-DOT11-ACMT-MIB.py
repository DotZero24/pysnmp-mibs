_h='h3cDot11SourceACNmsIP'
_g='h3cDot11ACStatusSwitchInfo'
_f='h3cDot11ACMaxStaNum'
_e='h3cDot11LoadBalanceThreshold'
_d='h3cDot11LoadBalanceType'
_c='h3cDot11ACMtTrapBackupSwitchInfo'
_b='h3cDot11ACMtTrapTnlAPSysName'
_a='h3cDot11ACMtTrapTunlDwnCount'
_Z='h3cDot11ACMtTrapTunlDwnInfo'
_Y='h3cDot11ACMtTrapTunlUpInfo'
_X='second'
_W='kbytes'
_V='h3cDot11LocalACModelAlias'
_U='h3cDot11ACPortalStatisticSSIDCM'
_T='h3cDot11ACBASIfIndex'
_S='h3cDot11ACIfIndex'
_R='H3cDot11MACModeType'
_Q='h3cDot11APConnectCount'
_P='h3cDot11MaxAPNumPermitted'
_O='h3cDot11ACMtTrapAPMacAddress'
_N='h3cDot11ACMtTrapAPIPv6Addr'
_M='h3cDot11ACMtTrapTnlAPIPAddr'
_L='h3cDot11ACMtTrapTnlAPName'
_K='not-accessible'
_J='read-write'
_I='H3cDot11TunnelSecSchemType'
_H='h3cDot11ACMtFirstTrapTime'
_G='h3cDot11CurrTunnelAPID'
_F='OctetString'
_E='Integer32'
_D='accessible-for-notify'
_C='H3C-DOT11-ACMT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
H3cDot11MACModeType,H3cDot11ObjectIDType,H3cDot11TunnelSecSchemType,h3cDot11=mibBuilder.importSymbols('H3C-DOT11-REF-MIB',_R,'H3cDot11ObjectIDType',_I,'h3cDot11')
IANAifType,=mibBuilder.importSymbols('IANAifType-MIB','IANAifType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
h3cDot11ACMT=ModuleIdentity((1,3,6,1,4,1,2011,10,2,75,1))
if mibBuilder.loadTexts:h3cDot11ACMT.setRevisions(('2016-03-11 18:00','2010-08-04 18:00','2009-08-07 18:00','2009-07-29 18:00','2009-05-07 20:00','2008-07-09 18:00','2007-12-21 18:00','2007-06-19 18:00','2007-04-27 20:00','2006-05-10 19:00'))
_H3cDot11ACObjectGroup_ObjectIdentity=ObjectIdentity
h3cDot11ACObjectGroup=_H3cDot11ACObjectGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,1,1))
_H3cDot11ACObject_ObjectIdentity=ObjectIdentity
h3cDot11ACObject=_H3cDot11ACObject_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,1,1,1))
class _H3cDot11CurrentACMACMode_Type(H3cDot11MACModeType):defaultValue=1
_H3cDot11CurrentACMACMode_Type.__name__=_R
_H3cDot11CurrentACMACMode_Object=MibScalar
h3cDot11CurrentACMACMode=_H3cDot11CurrentACMACMode_Object((1,3,6,1,4,1,2011,10,2,75,1,1,1,1),_H3cDot11CurrentACMACMode_Type())
h3cDot11CurrentACMACMode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CurrentACMACMode.setStatus(_A)
_H3cDot11MaxAPNumPermitted_Type=Integer32
_H3cDot11MaxAPNumPermitted_Object=MibScalar
h3cDot11MaxAPNumPermitted=_H3cDot11MaxAPNumPermitted_Object((1,3,6,1,4,1,2011,10,2,75,1,1,1,2),_H3cDot11MaxAPNumPermitted_Type())
h3cDot11MaxAPNumPermitted.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11MaxAPNumPermitted.setStatus(_A)
_H3cDot11MaxStationNumPermitted_Type=Integer32
_H3cDot11MaxStationNumPermitted_Object=MibScalar
h3cDot11MaxStationNumPermitted=_H3cDot11MaxStationNumPermitted_Object((1,3,6,1,4,1,2011,10,2,75,1,1,1,3),_H3cDot11MaxStationNumPermitted_Type())
h3cDot11MaxStationNumPermitted.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11MaxStationNumPermitted.setStatus(_A)
class _H3cDot11RunAPNumThreshold_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,100))
_H3cDot11RunAPNumThreshold_Type.__name__=_E
_H3cDot11RunAPNumThreshold_Object=MibScalar
h3cDot11RunAPNumThreshold=_H3cDot11RunAPNumThreshold_Object((1,3,6,1,4,1,2011,10,2,75,1,1,1,4),_H3cDot11RunAPNumThreshold_Type())
h3cDot11RunAPNumThreshold.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cDot11RunAPNumThreshold.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RunAPNumThreshold.setUnits('percent')
class _H3cDot11MaxNewConnCntPerSecCM_Type(Integer32):defaultValue=300
_H3cDot11MaxNewConnCntPerSecCM_Type.__name__=_E
_H3cDot11MaxNewConnCntPerSecCM_Object=MibScalar
h3cDot11MaxNewConnCntPerSecCM=_H3cDot11MaxNewConnCntPerSecCM_Object((1,3,6,1,4,1,2011,10,2,75,1,1,1,5),_H3cDot11MaxNewConnCntPerSecCM_Type())
h3cDot11MaxNewConnCntPerSecCM.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cDot11MaxNewConnCntPerSecCM.setStatus(_A)
class _H3cDot11IFNumberCM_Type(Integer32):defaultValue=24
_H3cDot11IFNumberCM_Type.__name__=_E
_H3cDot11IFNumberCM_Object=MibScalar
h3cDot11IFNumberCM=_H3cDot11IFNumberCM_Object((1,3,6,1,4,1,2011,10,2,75,1,1,1,6),_H3cDot11IFNumberCM_Type())
h3cDot11IFNumberCM.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cDot11IFNumberCM.setStatus(_A)
_H3cDot11APLicenseWeight_Type=OctetString
_H3cDot11APLicenseWeight_Object=MibScalar
h3cDot11APLicenseWeight=_H3cDot11APLicenseWeight_Object((1,3,6,1,4,1,2011,10,2,75,1,1,1,7),_H3cDot11APLicenseWeight_Type())
h3cDot11APLicenseWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APLicenseWeight.setStatus(_A)
_H3cDot11ACLoadInfo_ObjectIdentity=ObjectIdentity
h3cDot11ACLoadInfo=_H3cDot11ACLoadInfo_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,1,1,2))
_H3cDot11APConnectCount_Type=Integer32
_H3cDot11APConnectCount_Object=MibScalar
h3cDot11APConnectCount=_H3cDot11APConnectCount_Object((1,3,6,1,4,1,2011,10,2,75,1,1,2,1),_H3cDot11APConnectCount_Type())
h3cDot11APConnectCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APConnectCount.setStatus(_A)
_H3cDot11StationConnectCount_Type=Integer32
_H3cDot11StationConnectCount_Object=MibScalar
h3cDot11StationConnectCount=_H3cDot11StationConnectCount_Object((1,3,6,1,4,1,2011,10,2,75,1,1,2,2),_H3cDot11StationConnectCount_Type())
h3cDot11StationConnectCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11StationConnectCount.setStatus(_A)
_H3cDot11ACIFLoadInfoTable_Object=MibTable
h3cDot11ACIFLoadInfoTable=_H3cDot11ACIFLoadInfoTable_Object((1,3,6,1,4,1,2011,10,2,75,1,1,2,3))
if mibBuilder.loadTexts:h3cDot11ACIFLoadInfoTable.setStatus(_A)
_H3cDot11ACIFLoadInfoEntry_Object=MibTableRow
h3cDot11ACIFLoadInfoEntry=_H3cDot11ACIFLoadInfoEntry_Object((1,3,6,1,4,1,2011,10,2,75,1,1,2,3,1))
h3cDot11ACIFLoadInfoEntry.setIndexNames((0,_C,_S))
if mibBuilder.loadTexts:h3cDot11ACIFLoadInfoEntry.setStatus(_A)
_H3cDot11ACIfIndex_Type=Integer32
_H3cDot11ACIfIndex_Object=MibTableColumn
h3cDot11ACIfIndex=_H3cDot11ACIfIndex_Object((1,3,6,1,4,1,2011,10,2,75,1,1,2,3,1,1),_H3cDot11ACIfIndex_Type())
h3cDot11ACIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11ACIfIndex.setStatus(_A)
_H3cDot11ACIfApNum_Type=Integer32
_H3cDot11ACIfApNum_Object=MibTableColumn
h3cDot11ACIfApNum=_H3cDot11ACIfApNum_Object((1,3,6,1,4,1,2011,10,2,75,1,1,2,3,1,2),_H3cDot11ACIfApNum_Type())
h3cDot11ACIfApNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACIfApNum.setStatus(_A)
_H3cDot11ACIfStaNum_Type=Integer32
_H3cDot11ACIfStaNum_Object=MibTableColumn
h3cDot11ACIfStaNum=_H3cDot11ACIfStaNum_Object((1,3,6,1,4,1,2011,10,2,75,1,1,2,3,1,3),_H3cDot11ACIfStaNum_Type())
h3cDot11ACIfStaNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACIfStaNum.setStatus(_A)
_H3cDot11ACIfName_Type=OctetString
_H3cDot11ACIfName_Object=MibTableColumn
h3cDot11ACIfName=_H3cDot11ACIfName_Object((1,3,6,1,4,1,2011,10,2,75,1,1,2,3,1,4),_H3cDot11ACIfName_Type())
h3cDot11ACIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACIfName.setStatus(_A)
_H3cDot11MasterAPCount_Type=Integer32
_H3cDot11MasterAPCount_Object=MibScalar
h3cDot11MasterAPCount=_H3cDot11MasterAPCount_Object((1,3,6,1,4,1,2011,10,2,75,1,1,2,4),_H3cDot11MasterAPCount_Type())
h3cDot11MasterAPCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11MasterAPCount.setStatus(_A)
_H3cDot11SlaveAPCount_Type=Integer32
_H3cDot11SlaveAPCount_Object=MibScalar
h3cDot11SlaveAPCount=_H3cDot11SlaveAPCount_Object((1,3,6,1,4,1,2011,10,2,75,1,1,2,5),_H3cDot11SlaveAPCount_Type())
h3cDot11SlaveAPCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11SlaveAPCount.setStatus(_A)
_H3cDot11ConnectAutoAPCount_Type=Integer32
_H3cDot11ConnectAutoAPCount_Object=MibScalar
h3cDot11ConnectAutoAPCount=_H3cDot11ConnectAutoAPCount_Object((1,3,6,1,4,1,2011,10,2,75,1,1,2,6),_H3cDot11ConnectAutoAPCount_Type())
h3cDot11ConnectAutoAPCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ConnectAutoAPCount.setStatus(_A)
_H3cDot11PersistentAPCount_Type=Integer32
_H3cDot11PersistentAPCount_Object=MibScalar
h3cDot11PersistentAPCount=_H3cDot11PersistentAPCount_Object((1,3,6,1,4,1,2011,10,2,75,1,1,2,7),_H3cDot11PersistentAPCount_Type())
h3cDot11PersistentAPCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11PersistentAPCount.setStatus(_A)
_H3cDot11AcUploadFrameCnt_Type=Counter64
_H3cDot11AcUploadFrameCnt_Object=MibScalar
h3cDot11AcUploadFrameCnt=_H3cDot11AcUploadFrameCnt_Object((1,3,6,1,4,1,2011,10,2,75,1,1,2,8),_H3cDot11AcUploadFrameCnt_Type())
h3cDot11AcUploadFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11AcUploadFrameCnt.setStatus(_A)
_H3cDot11AcDownloadFrameCnt_Type=Counter64
_H3cDot11AcDownloadFrameCnt_Object=MibScalar
h3cDot11AcDownloadFrameCnt=_H3cDot11AcDownloadFrameCnt_Object((1,3,6,1,4,1,2011,10,2,75,1,1,2,9),_H3cDot11AcDownloadFrameCnt_Type())
h3cDot11AcDownloadFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11AcDownloadFrameCnt.setStatus(_A)
_H3cDot11AcUploadFrameBytes_Type=Counter64
_H3cDot11AcUploadFrameBytes_Object=MibScalar
h3cDot11AcUploadFrameBytes=_H3cDot11AcUploadFrameBytes_Object((1,3,6,1,4,1,2011,10,2,75,1,1,2,10),_H3cDot11AcUploadFrameBytes_Type())
h3cDot11AcUploadFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11AcUploadFrameBytes.setStatus(_A)
_H3cDot11AcDownloadFrameBytes_Type=Counter64
_H3cDot11AcDownloadFrameBytes_Object=MibScalar
h3cDot11AcDownloadFrameBytes=_H3cDot11AcDownloadFrameBytes_Object((1,3,6,1,4,1,2011,10,2,75,1,1,2,11),_H3cDot11AcDownloadFrameBytes_Type())
h3cDot11AcDownloadFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11AcDownloadFrameBytes.setStatus(_A)
class _H3cDot11BackupACRole_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('null',1),('master',2),('slave',3)))
_H3cDot11BackupACRole_Type.__name__=_E
_H3cDot11BackupACRole_Object=MibScalar
h3cDot11BackupACRole=_H3cDot11BackupACRole_Object((1,3,6,1,4,1,2011,10,2,75,1,1,2,12),_H3cDot11BackupACRole_Type())
h3cDot11BackupACRole.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11BackupACRole.setStatus(_A)
_H3cDot11BackupACNMSIP_Type=IpAddress
_H3cDot11BackupACNMSIP_Object=MibScalar
h3cDot11BackupACNMSIP=_H3cDot11BackupACNMSIP_Object((1,3,6,1,4,1,2011,10,2,75,1,1,2,13),_H3cDot11BackupACNMSIP_Type())
h3cDot11BackupACNMSIP.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11BackupACNMSIP.setStatus(_A)
class _H3cDot11ACBackupMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('null',1),('hotBackup',2),('coldBackup',3)))
_H3cDot11ACBackupMode_Type.__name__=_E
_H3cDot11ACBackupMode_Object=MibScalar
h3cDot11ACBackupMode=_H3cDot11ACBackupMode_Object((1,3,6,1,4,1,2011,10,2,75,1,1,2,14),_H3cDot11ACBackupMode_Type())
h3cDot11ACBackupMode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACBackupMode.setStatus(_A)
class _H3cDot11ACBackupStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('standby',2)))
_H3cDot11ACBackupStatus_Type.__name__=_E
_H3cDot11ACBackupStatus_Object=MibScalar
h3cDot11ACBackupStatus=_H3cDot11ACBackupStatus_Object((1,3,6,1,4,1,2011,10,2,75,1,1,2,15),_H3cDot11ACBackupStatus_Type())
h3cDot11ACBackupStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACBackupStatus.setStatus(_A)
_H3cDot11ACSwitchCnt_Type=Integer32
_H3cDot11ACSwitchCnt_Object=MibScalar
h3cDot11ACSwitchCnt=_H3cDot11ACSwitchCnt_Object((1,3,6,1,4,1,2011,10,2,75,1,1,2,16),_H3cDot11ACSwitchCnt_Type())
h3cDot11ACSwitchCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACSwitchCnt.setStatus(_A)
_H3cDot11ACSouthifPacketOutputCount_Type=Counter64
_H3cDot11ACSouthifPacketOutputCount_Object=MibScalar
h3cDot11ACSouthifPacketOutputCount=_H3cDot11ACSouthifPacketOutputCount_Object((1,3,6,1,4,1,2011,10,2,75,1,1,2,17),_H3cDot11ACSouthifPacketOutputCount_Type())
h3cDot11ACSouthifPacketOutputCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACSouthifPacketOutputCount.setStatus(_A)
_H3cDot11ACSouthifPacketOutputBytes_Type=Counter64
_H3cDot11ACSouthifPacketOutputBytes_Object=MibScalar
h3cDot11ACSouthifPacketOutputBytes=_H3cDot11ACSouthifPacketOutputBytes_Object((1,3,6,1,4,1,2011,10,2,75,1,1,2,18),_H3cDot11ACSouthifPacketOutputBytes_Type())
h3cDot11ACSouthifPacketOutputBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACSouthifPacketOutputBytes.setStatus(_A)
_H3cDot11ACSouthifPacketInputCount_Type=Counter64
_H3cDot11ACSouthifPacketInputCount_Object=MibScalar
h3cDot11ACSouthifPacketInputCount=_H3cDot11ACSouthifPacketInputCount_Object((1,3,6,1,4,1,2011,10,2,75,1,1,2,19),_H3cDot11ACSouthifPacketInputCount_Type())
h3cDot11ACSouthifPacketInputCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACSouthifPacketInputCount.setStatus(_A)
_H3cDot11ACSouthifPacketInputBytes_Type=Counter64
_H3cDot11ACSouthifPacketInputBytes_Object=MibScalar
h3cDot11ACSouthifPacketInputBytes=_H3cDot11ACSouthifPacketInputBytes_Object((1,3,6,1,4,1,2011,10,2,75,1,1,2,20),_H3cDot11ACSouthifPacketInputBytes_Type())
h3cDot11ACSouthifPacketInputBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACSouthifPacketInputBytes.setStatus(_A)
_H3cDot11TotalAPconnected_Type=Integer32
_H3cDot11TotalAPconnected_Object=MibScalar
h3cDot11TotalAPconnected=_H3cDot11TotalAPconnected_Object((1,3,6,1,4,1,2011,10,2,75,1,1,2,21),_H3cDot11TotalAPconnected_Type())
h3cDot11TotalAPconnected.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11TotalAPconnected.setStatus(_A)
_H3cDot11RemainingAPcapacity_Type=Integer32
_H3cDot11RemainingAPcapacity_Object=MibScalar
h3cDot11RemainingAPcapacity=_H3cDot11RemainingAPcapacity_Object((1,3,6,1,4,1,2011,10,2,75,1,1,2,22),_H3cDot11RemainingAPcapacity_Type())
h3cDot11RemainingAPcapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RemainingAPcapacity.setStatus(_A)
_H3cDot11WLANAssocStatisInfo_ObjectIdentity=ObjectIdentity
h3cDot11WLANAssocStatisInfo=_H3cDot11WLANAssocStatisInfo_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,1,1,3))
_H3cDot11StationAssocSum_Type=Counter32
_H3cDot11StationAssocSum_Object=MibScalar
h3cDot11StationAssocSum=_H3cDot11StationAssocSum_Object((1,3,6,1,4,1,2011,10,2,75,1,1,3,1),_H3cDot11StationAssocSum_Type())
h3cDot11StationAssocSum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11StationAssocSum.setStatus(_A)
_H3cDot11StationAssocFailSum_Type=Counter32
_H3cDot11StationAssocFailSum_Object=MibScalar
h3cDot11StationAssocFailSum=_H3cDot11StationAssocFailSum_Object((1,3,6,1,4,1,2011,10,2,75,1,1,3,2),_H3cDot11StationAssocFailSum_Type())
h3cDot11StationAssocFailSum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11StationAssocFailSum.setStatus(_A)
_H3cDot11StationReassocSum_Type=Counter32
_H3cDot11StationReassocSum_Object=MibScalar
h3cDot11StationReassocSum=_H3cDot11StationReassocSum_Object((1,3,6,1,4,1,2011,10,2,75,1,1,3,3),_H3cDot11StationReassocSum_Type())
h3cDot11StationReassocSum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11StationReassocSum.setStatus(_A)
_H3cDot11StationAssocRejectedSum_Type=Counter32
_H3cDot11StationAssocRejectedSum_Object=MibScalar
h3cDot11StationAssocRejectedSum=_H3cDot11StationAssocRejectedSum_Object((1,3,6,1,4,1,2011,10,2,75,1,1,3,4),_H3cDot11StationAssocRejectedSum_Type())
h3cDot11StationAssocRejectedSum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11StationAssocRejectedSum.setStatus(_A)
_H3cDot11StationExDeAuthenSum_Type=Counter32
_H3cDot11StationExDeAuthenSum_Object=MibScalar
h3cDot11StationExDeAuthenSum=_H3cDot11StationExDeAuthenSum_Object((1,3,6,1,4,1,2011,10,2,75,1,1,3,5),_H3cDot11StationExDeAuthenSum_Type())
h3cDot11StationExDeAuthenSum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11StationExDeAuthenSum.setStatus(_A)
_H3cDot11StationCurAssocSum_Type=Integer32
_H3cDot11StationCurAssocSum_Object=MibScalar
h3cDot11StationCurAssocSum=_H3cDot11StationCurAssocSum_Object((1,3,6,1,4,1,2011,10,2,75,1,1,3,6),_H3cDot11StationCurAssocSum_Type())
h3cDot11StationCurAssocSum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11StationCurAssocSum.setStatus(_A)
_H3cDot11StationAssocReqSum_Type=Counter32
_H3cDot11StationAssocReqSum_Object=MibScalar
h3cDot11StationAssocReqSum=_H3cDot11StationAssocReqSum_Object((1,3,6,1,4,1,2011,10,2,75,1,1,3,7),_H3cDot11StationAssocReqSum_Type())
h3cDot11StationAssocReqSum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11StationAssocReqSum.setStatus(_A)
_H3cDot11StationReassocReqSum_Type=Counter32
_H3cDot11StationReassocReqSum_Object=MibScalar
h3cDot11StationReassocReqSum=_H3cDot11StationReassocReqSum_Object((1,3,6,1,4,1,2011,10,2,75,1,1,3,8),_H3cDot11StationReassocReqSum_Type())
h3cDot11StationReassocReqSum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11StationReassocReqSum.setStatus(_A)
_H3cDot11StationReassocFailSum_Type=Counter32
_H3cDot11StationReassocFailSum_Object=MibScalar
h3cDot11StationReassocFailSum=_H3cDot11StationReassocFailSum_Object((1,3,6,1,4,1,2011,10,2,75,1,1,3,9),_H3cDot11StationReassocFailSum_Type())
h3cDot11StationReassocFailSum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11StationReassocFailSum.setStatus(_A)
_H3cDot11ACBASInfo_ObjectIdentity=ObjectIdentity
h3cDot11ACBASInfo=_H3cDot11ACBASInfo_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,1,1,4))
_H3cDot11ACBASSysObjects_ObjectIdentity=ObjectIdentity
h3cDot11ACBASSysObjects=_H3cDot11ACBASSysObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,1,1,4,1))
_H3cDot11ACBASTableObjects_ObjectIdentity=ObjectIdentity
h3cDot11ACBASTableObjects=_H3cDot11ACBASTableObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,1,1,4,2))
_H3cDot11ACBASIfTable_Object=MibTable
h3cDot11ACBASIfTable=_H3cDot11ACBASIfTable_Object((1,3,6,1,4,1,2011,10,2,75,1,1,4,2,3))
if mibBuilder.loadTexts:h3cDot11ACBASIfTable.setStatus(_A)
_H3cDot11ACBASIfEntry_Object=MibTableRow
h3cDot11ACBASIfEntry=_H3cDot11ACBASIfEntry_Object((1,3,6,1,4,1,2011,10,2,75,1,1,4,2,3,1))
h3cDot11ACBASIfEntry.setIndexNames((0,_C,_T))
if mibBuilder.loadTexts:h3cDot11ACBASIfEntry.setStatus(_A)
_H3cDot11ACBASIfIndex_Type=Integer32
_H3cDot11ACBASIfIndex_Object=MibTableColumn
h3cDot11ACBASIfIndex=_H3cDot11ACBASIfIndex_Object((1,3,6,1,4,1,2011,10,2,75,1,1,4,2,3,1,1),_H3cDot11ACBASIfIndex_Type())
h3cDot11ACBASIfIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cDot11ACBASIfIndex.setStatus(_A)
class _H3cDot11ACBASIfDescr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cDot11ACBASIfDescr_Type.__name__=_F
_H3cDot11ACBASIfDescr_Object=MibTableColumn
h3cDot11ACBASIfDescr=_H3cDot11ACBASIfDescr_Object((1,3,6,1,4,1,2011,10,2,75,1,1,4,2,3,1,2),_H3cDot11ACBASIfDescr_Type())
h3cDot11ACBASIfDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACBASIfDescr.setStatus(_A)
_H3cDot11ACBASIfType_Type=IANAifType
_H3cDot11ACBASIfType_Object=MibTableColumn
h3cDot11ACBASIfType=_H3cDot11ACBASIfType_Object((1,3,6,1,4,1,2011,10,2,75,1,1,4,2,3,1,3),_H3cDot11ACBASIfType_Type())
h3cDot11ACBASIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACBASIfType.setStatus(_A)
_H3cDot11ACStaUserSecAuthStatis_ObjectIdentity=ObjectIdentity
h3cDot11ACStaUserSecAuthStatis=_H3cDot11ACStaUserSecAuthStatis_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,1,1,5))
_H3cDot11ACStaUserAuthCurNumber_Type=Integer32
_H3cDot11ACStaUserAuthCurNumber_Object=MibScalar
h3cDot11ACStaUserAuthCurNumber=_H3cDot11ACStaUserAuthCurNumber_Object((1,3,6,1,4,1,2011,10,2,75,1,1,5,1),_H3cDot11ACStaUserAuthCurNumber_Type())
h3cDot11ACStaUserAuthCurNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACStaUserAuthCurNumber.setStatus(_A)
_H3cDot11ACStaUserConnFailCnt_Type=Counter32
_H3cDot11ACStaUserConnFailCnt_Object=MibScalar
h3cDot11ACStaUserConnFailCnt=_H3cDot11ACStaUserConnFailCnt_Object((1,3,6,1,4,1,2011,10,2,75,1,1,5,2),_H3cDot11ACStaUserConnFailCnt_Type())
h3cDot11ACStaUserConnFailCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACStaUserConnFailCnt.setStatus(_A)
_H3cDot11ACStaUserAuthReqCnt_Type=Counter32
_H3cDot11ACStaUserAuthReqCnt_Object=MibScalar
h3cDot11ACStaUserAuthReqCnt=_H3cDot11ACStaUserAuthReqCnt_Object((1,3,6,1,4,1,2011,10,2,75,1,1,5,3),_H3cDot11ACStaUserAuthReqCnt_Type())
h3cDot11ACStaUserAuthReqCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACStaUserAuthReqCnt.setStatus(_A)
_H3cDot11ACStaUserAuthSuccCnt_Type=Counter32
_H3cDot11ACStaUserAuthSuccCnt_Object=MibScalar
h3cDot11ACStaUserAuthSuccCnt=_H3cDot11ACStaUserAuthSuccCnt_Object((1,3,6,1,4,1,2011,10,2,75,1,1,5,4),_H3cDot11ACStaUserAuthSuccCnt_Type())
h3cDot11ACStaUserAuthSuccCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACStaUserAuthSuccCnt.setStatus(_A)
_H3cDot11ACStaUserAuthFailCnt_Type=Counter32
_H3cDot11ACStaUserAuthFailCnt_Object=MibScalar
h3cDot11ACStaUserAuthFailCnt=_H3cDot11ACStaUserAuthFailCnt_Object((1,3,6,1,4,1,2011,10,2,75,1,1,5,5),_H3cDot11ACStaUserAuthFailCnt_Type())
h3cDot11ACStaUserAuthFailCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACStaUserAuthFailCnt.setStatus(_A)
_H3cDot11ACStaUserAllAuthCntCM_Type=Counter32
_H3cDot11ACStaUserAllAuthCntCM_Object=MibScalar
h3cDot11ACStaUserAllAuthCntCM=_H3cDot11ACStaUserAllAuthCntCM_Object((1,3,6,1,4,1,2011,10,2,75,1,1,5,6),_H3cDot11ACStaUserAllAuthCntCM_Type())
h3cDot11ACStaUserAllAuthCntCM.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACStaUserAllAuthCntCM.setStatus(_A)
_H3cDot11ACStaUserAuthRespCntCM_Type=Counter32
_H3cDot11ACStaUserAuthRespCntCM_Object=MibScalar
h3cDot11ACStaUserAuthRespCntCM=_H3cDot11ACStaUserAuthRespCntCM_Object((1,3,6,1,4,1,2011,10,2,75,1,1,5,7),_H3cDot11ACStaUserAuthRespCntCM_Type())
h3cDot11ACStaUserAuthRespCntCM.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACStaUserAuthRespCntCM.setStatus(_A)
_H3cDot11ACStaSecAuthTypeStatis_ObjectIdentity=ObjectIdentity
h3cDot11ACStaSecAuthTypeStatis=_H3cDot11ACStaSecAuthTypeStatis_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,1,1,6))
_H3cDot11ACStaUserPortalOnlineNum_Type=Integer32
_H3cDot11ACStaUserPortalOnlineNum_Object=MibScalar
h3cDot11ACStaUserPortalOnlineNum=_H3cDot11ACStaUserPortalOnlineNum_Object((1,3,6,1,4,1,2011,10,2,75,1,1,6,1),_H3cDot11ACStaUserPortalOnlineNum_Type())
h3cDot11ACStaUserPortalOnlineNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACStaUserPortalOnlineNum.setStatus(_A)
_H3cDot11ACStaUserFreeAuthOnlineNum_Type=Integer32
_H3cDot11ACStaUserFreeAuthOnlineNum_Object=MibScalar
h3cDot11ACStaUserFreeAuthOnlineNum=_H3cDot11ACStaUserFreeAuthOnlineNum_Object((1,3,6,1,4,1,2011,10,2,75,1,1,6,2),_H3cDot11ACStaUserFreeAuthOnlineNum_Type())
h3cDot11ACStaUserFreeAuthOnlineNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACStaUserFreeAuthOnlineNum.setStatus(_A)
_H3cDot11ACStaUserAssociateAuthOnlineNum_Type=Integer32
_H3cDot11ACStaUserAssociateAuthOnlineNum_Object=MibScalar
h3cDot11ACStaUserAssociateAuthOnlineNum=_H3cDot11ACStaUserAssociateAuthOnlineNum_Object((1,3,6,1,4,1,2011,10,2,75,1,1,6,3),_H3cDot11ACStaUserAssociateAuthOnlineNum_Type())
h3cDot11ACStaUserAssociateAuthOnlineNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACStaUserAssociateAuthOnlineNum.setStatus(_A)
_H3cDot11ACStaUserMacAuthOnlineNum_Type=Integer32
_H3cDot11ACStaUserMacAuthOnlineNum_Object=MibScalar
h3cDot11ACStaUserMacAuthOnlineNum=_H3cDot11ACStaUserMacAuthOnlineNum_Object((1,3,6,1,4,1,2011,10,2,75,1,1,6,4),_H3cDot11ACStaUserMacAuthOnlineNum_Type())
h3cDot11ACStaUserMacAuthOnlineNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACStaUserMacAuthOnlineNum.setStatus(_A)
_H3cDot11ACStaUserPortalLostConnectionCnt_Type=Counter32
_H3cDot11ACStaUserPortalLostConnectionCnt_Object=MibScalar
h3cDot11ACStaUserPortalLostConnectionCnt=_H3cDot11ACStaUserPortalLostConnectionCnt_Object((1,3,6,1,4,1,2011,10,2,75,1,1,6,5),_H3cDot11ACStaUserPortalLostConnectionCnt_Type())
h3cDot11ACStaUserPortalLostConnectionCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACStaUserPortalLostConnectionCnt.setStatus(_A)
_H3cDot11ACStaUserFreeAuthLostConnectionCnt_Type=Counter32
_H3cDot11ACStaUserFreeAuthLostConnectionCnt_Object=MibScalar
h3cDot11ACStaUserFreeAuthLostConnectionCnt=_H3cDot11ACStaUserFreeAuthLostConnectionCnt_Object((1,3,6,1,4,1,2011,10,2,75,1,1,6,6),_H3cDot11ACStaUserFreeAuthLostConnectionCnt_Type())
h3cDot11ACStaUserFreeAuthLostConnectionCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACStaUserFreeAuthLostConnectionCnt.setStatus(_A)
_H3cDot11ACStaUserAssociateAuthLostConnectionCnt_Type=Counter32
_H3cDot11ACStaUserAssociateAuthLostConnectionCnt_Object=MibScalar
h3cDot11ACStaUserAssociateAuthLostConnectionCnt=_H3cDot11ACStaUserAssociateAuthLostConnectionCnt_Object((1,3,6,1,4,1,2011,10,2,75,1,1,6,7),_H3cDot11ACStaUserAssociateAuthLostConnectionCnt_Type())
h3cDot11ACStaUserAssociateAuthLostConnectionCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACStaUserAssociateAuthLostConnectionCnt.setStatus(_A)
_H3cDot11ACStaUserMacAuthLostConnectionCnt_Type=Counter32
_H3cDot11ACStaUserMacAuthLostConnectionCnt_Object=MibScalar
h3cDot11ACStaUserMacAuthLostConnectionCnt=_H3cDot11ACStaUserMacAuthLostConnectionCnt_Object((1,3,6,1,4,1,2011,10,2,75,1,1,6,8),_H3cDot11ACStaUserMacAuthLostConnectionCnt_Type())
h3cDot11ACStaUserMacAuthLostConnectionCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACStaUserMacAuthLostConnectionCnt.setStatus(_A)
_H3cDot11ACStaPortalAuthReqCnt_Type=Counter32
_H3cDot11ACStaPortalAuthReqCnt_Object=MibScalar
h3cDot11ACStaPortalAuthReqCnt=_H3cDot11ACStaPortalAuthReqCnt_Object((1,3,6,1,4,1,2011,10,2,75,1,1,6,9),_H3cDot11ACStaPortalAuthReqCnt_Type())
h3cDot11ACStaPortalAuthReqCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACStaPortalAuthReqCnt.setStatus(_A)
_H3cDot11ACStaAssociateAuthReqCnt_Type=Counter32
_H3cDot11ACStaAssociateAuthReqCnt_Object=MibScalar
h3cDot11ACStaAssociateAuthReqCnt=_H3cDot11ACStaAssociateAuthReqCnt_Object((1,3,6,1,4,1,2011,10,2,75,1,1,6,10),_H3cDot11ACStaAssociateAuthReqCnt_Type())
h3cDot11ACStaAssociateAuthReqCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACStaAssociateAuthReqCnt.setStatus(_A)
_H3cDot11ACStaMacAuthReqCnt_Type=Counter32
_H3cDot11ACStaMacAuthReqCnt_Object=MibScalar
h3cDot11ACStaMacAuthReqCnt=_H3cDot11ACStaMacAuthReqCnt_Object((1,3,6,1,4,1,2011,10,2,75,1,1,6,11),_H3cDot11ACStaMacAuthReqCnt_Type())
h3cDot11ACStaMacAuthReqCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACStaMacAuthReqCnt.setStatus(_A)
_H3cDot11ACStaPortalAuthSuccCnt_Type=Counter32
_H3cDot11ACStaPortalAuthSuccCnt_Object=MibScalar
h3cDot11ACStaPortalAuthSuccCnt=_H3cDot11ACStaPortalAuthSuccCnt_Object((1,3,6,1,4,1,2011,10,2,75,1,1,6,12),_H3cDot11ACStaPortalAuthSuccCnt_Type())
h3cDot11ACStaPortalAuthSuccCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACStaPortalAuthSuccCnt.setStatus(_A)
_H3cDot11ACStaAssociateAuthSuccCnt_Type=Counter32
_H3cDot11ACStaAssociateAuthSuccCnt_Object=MibScalar
h3cDot11ACStaAssociateAuthSuccCnt=_H3cDot11ACStaAssociateAuthSuccCnt_Object((1,3,6,1,4,1,2011,10,2,75,1,1,6,13),_H3cDot11ACStaAssociateAuthSuccCnt_Type())
h3cDot11ACStaAssociateAuthSuccCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACStaAssociateAuthSuccCnt.setStatus(_A)
_H3cDot11ACStaMacAuthSuccCnt_Type=Counter32
_H3cDot11ACStaMacAuthSuccCnt_Object=MibScalar
h3cDot11ACStaMacAuthSuccCnt=_H3cDot11ACStaMacAuthSuccCnt_Object((1,3,6,1,4,1,2011,10,2,75,1,1,6,14),_H3cDot11ACStaMacAuthSuccCnt_Type())
h3cDot11ACStaMacAuthSuccCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACStaMacAuthSuccCnt.setStatus(_A)
_H3cDot11ACStaPortalAuthReqFailCnt_Type=Counter32
_H3cDot11ACStaPortalAuthReqFailCnt_Object=MibScalar
h3cDot11ACStaPortalAuthReqFailCnt=_H3cDot11ACStaPortalAuthReqFailCnt_Object((1,3,6,1,4,1,2011,10,2,75,1,1,6,15),_H3cDot11ACStaPortalAuthReqFailCnt_Type())
h3cDot11ACStaPortalAuthReqFailCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACStaPortalAuthReqFailCnt.setStatus(_A)
_H3cDot11ACStaAssociateAuthReqFailCnt_Type=Counter32
_H3cDot11ACStaAssociateAuthReqFailCnt_Object=MibScalar
h3cDot11ACStaAssociateAuthReqFailCnt=_H3cDot11ACStaAssociateAuthReqFailCnt_Object((1,3,6,1,4,1,2011,10,2,75,1,1,6,16),_H3cDot11ACStaAssociateAuthReqFailCnt_Type())
h3cDot11ACStaAssociateAuthReqFailCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACStaAssociateAuthReqFailCnt.setStatus(_A)
_H3cDot11ACStaMacAuthReqFailCnt_Type=Counter32
_H3cDot11ACStaMacAuthReqFailCnt_Object=MibScalar
h3cDot11ACStaMacAuthReqFailCnt=_H3cDot11ACStaMacAuthReqFailCnt_Object((1,3,6,1,4,1,2011,10,2,75,1,1,6,17),_H3cDot11ACStaMacAuthReqFailCnt_Type())
h3cDot11ACStaMacAuthReqFailCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACStaMacAuthReqFailCnt.setStatus(_A)
_H3cDot11ACStaUserAutoAuthOnlineNumCM_Type=Integer32
_H3cDot11ACStaUserAutoAuthOnlineNumCM_Object=MibScalar
h3cDot11ACStaUserAutoAuthOnlineNumCM=_H3cDot11ACStaUserAutoAuthOnlineNumCM_Object((1,3,6,1,4,1,2011,10,2,75,1,1,6,18),_H3cDot11ACStaUserAutoAuthOnlineNumCM_Type())
h3cDot11ACStaUserAutoAuthOnlineNumCM.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACStaUserAutoAuthOnlineNumCM.setStatus(_A)
_H3cDot11ACStaUserAutoAuthLostConnectionCntCM_Type=Counter32
_H3cDot11ACStaUserAutoAuthLostConnectionCntCM_Object=MibScalar
h3cDot11ACStaUserAutoAuthLostConnectionCntCM=_H3cDot11ACStaUserAutoAuthLostConnectionCntCM_Object((1,3,6,1,4,1,2011,10,2,75,1,1,6,19),_H3cDot11ACStaUserAutoAuthLostConnectionCntCM_Type())
h3cDot11ACStaUserAutoAuthLostConnectionCntCM.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACStaUserAutoAuthLostConnectionCntCM.setStatus(_A)
_H3cDot11ACStaAutoAuthReqCntCM_Type=Counter32
_H3cDot11ACStaAutoAuthReqCntCM_Object=MibScalar
h3cDot11ACStaAutoAuthReqCntCM=_H3cDot11ACStaAutoAuthReqCntCM_Object((1,3,6,1,4,1,2011,10,2,75,1,1,6,20),_H3cDot11ACStaAutoAuthReqCntCM_Type())
h3cDot11ACStaAutoAuthReqCntCM.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACStaAutoAuthReqCntCM.setStatus(_A)
_H3cDot11ACStaAutoAuthSuccCntCM_Type=Counter32
_H3cDot11ACStaAutoAuthSuccCntCM_Object=MibScalar
h3cDot11ACStaAutoAuthSuccCntCM=_H3cDot11ACStaAutoAuthSuccCntCM_Object((1,3,6,1,4,1,2011,10,2,75,1,1,6,21),_H3cDot11ACStaAutoAuthSuccCntCM_Type())
h3cDot11ACStaAutoAuthSuccCntCM.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACStaAutoAuthSuccCntCM.setStatus(_A)
_H3cDot11ACStaAutoAuthReqFailCntCM_Type=Counter32
_H3cDot11ACStaAutoAuthReqFailCntCM_Object=MibScalar
h3cDot11ACStaAutoAuthReqFailCntCM=_H3cDot11ACStaAutoAuthReqFailCntCM_Object((1,3,6,1,4,1,2011,10,2,75,1,1,6,22),_H3cDot11ACStaAutoAuthReqFailCntCM_Type())
h3cDot11ACStaAutoAuthReqFailCntCM.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACStaAutoAuthReqFailCntCM.setStatus(_A)
_H3cDot11ACPortalStatisticCMTable_Object=MibTable
h3cDot11ACPortalStatisticCMTable=_H3cDot11ACPortalStatisticCMTable_Object((1,3,6,1,4,1,2011,10,2,75,1,1,7))
if mibBuilder.loadTexts:h3cDot11ACPortalStatisticCMTable.setStatus(_A)
_H3cDot11ACPortalStatisticCMEntry_Object=MibTableRow
h3cDot11ACPortalStatisticCMEntry=_H3cDot11ACPortalStatisticCMEntry_Object((1,3,6,1,4,1,2011,10,2,75,1,1,7,1))
h3cDot11ACPortalStatisticCMEntry.setIndexNames((0,_C,_U))
if mibBuilder.loadTexts:h3cDot11ACPortalStatisticCMEntry.setStatus(_A)
class _H3cDot11ACPortalStatisticSSIDCM_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cDot11ACPortalStatisticSSIDCM_Type.__name__=_F
_H3cDot11ACPortalStatisticSSIDCM_Object=MibTableColumn
h3cDot11ACPortalStatisticSSIDCM=_H3cDot11ACPortalStatisticSSIDCM_Object((1,3,6,1,4,1,2011,10,2,75,1,1,7,1,1),_H3cDot11ACPortalStatisticSSIDCM_Type())
h3cDot11ACPortalStatisticSSIDCM.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cDot11ACPortalStatisticSSIDCM.setStatus(_A)
_H3cDot11ACPortalStatAuthReqCM_Type=Counter32
_H3cDot11ACPortalStatAuthReqCM_Object=MibTableColumn
h3cDot11ACPortalStatAuthReqCM=_H3cDot11ACPortalStatAuthReqCM_Object((1,3,6,1,4,1,2011,10,2,75,1,1,7,1,2),_H3cDot11ACPortalStatAuthReqCM_Type())
h3cDot11ACPortalStatAuthReqCM.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACPortalStatAuthReqCM.setStatus(_A)
_H3cDot11ACPortalStatAuthRespCM_Type=Counter32
_H3cDot11ACPortalStatAuthRespCM_Object=MibTableColumn
h3cDot11ACPortalStatAuthRespCM=_H3cDot11ACPortalStatAuthRespCM_Object((1,3,6,1,4,1,2011,10,2,75,1,1,7,1,3),_H3cDot11ACPortalStatAuthRespCM_Type())
h3cDot11ACPortalStatAuthRespCM.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACPortalStatAuthRespCM.setStatus(_A)
_H3cDot11LocalACModelTable_Object=MibTable
h3cDot11LocalACModelTable=_H3cDot11LocalACModelTable_Object((1,3,6,1,4,1,2011,10,2,75,1,1,8))
if mibBuilder.loadTexts:h3cDot11LocalACModelTable.setStatus(_A)
_H3cDot11LocalACModelEntry_Object=MibTableRow
h3cDot11LocalACModelEntry=_H3cDot11LocalACModelEntry_Object((1,3,6,1,4,1,2011,10,2,75,1,1,8,1))
h3cDot11LocalACModelEntry.setIndexNames((0,_C,_V))
if mibBuilder.loadTexts:h3cDot11LocalACModelEntry.setStatus(_A)
class _H3cDot11LocalACModelAlias_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_H3cDot11LocalACModelAlias_Type.__name__=_F
_H3cDot11LocalACModelAlias_Object=MibTableColumn
h3cDot11LocalACModelAlias=_H3cDot11LocalACModelAlias_Object((1,3,6,1,4,1,2011,10,2,75,1,1,8,1,1),_H3cDot11LocalACModelAlias_Type())
h3cDot11LocalACModelAlias.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cDot11LocalACModelAlias.setStatus(_A)
_H3cDot11LocalACModelName_Type=OctetString
_H3cDot11LocalACModelName_Object=MibTableColumn
h3cDot11LocalACModelName=_H3cDot11LocalACModelName_Object((1,3,6,1,4,1,2011,10,2,75,1,1,8,1,2),_H3cDot11LocalACModelName_Type())
h3cDot11LocalACModelName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11LocalACModelName.setStatus(_A)
_H3cDot11LocalACManufacturer_Type=OctetString
_H3cDot11LocalACManufacturer_Object=MibTableColumn
h3cDot11LocalACManufacturer=_H3cDot11LocalACManufacturer_Object((1,3,6,1,4,1,2011,10,2,75,1,1,8,1,3),_H3cDot11LocalACManufacturer_Type())
h3cDot11LocalACManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11LocalACManufacturer.setStatus(_A)
_H3cDot11LocalACCPUType_Type=OctetString
_H3cDot11LocalACCPUType_Object=MibTableColumn
h3cDot11LocalACCPUType=_H3cDot11LocalACCPUType_Object((1,3,6,1,4,1,2011,10,2,75,1,1,8,1,4),_H3cDot11LocalACCPUType_Type())
h3cDot11LocalACCPUType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11LocalACCPUType.setStatus(_A)
_H3cDot11LocalACCPUClockSpeed_Type=Unsigned32
_H3cDot11LocalACCPUClockSpeed_Object=MibTableColumn
h3cDot11LocalACCPUClockSpeed=_H3cDot11LocalACCPUClockSpeed_Object((1,3,6,1,4,1,2011,10,2,75,1,1,8,1,5),_H3cDot11LocalACCPUClockSpeed_Type())
h3cDot11LocalACCPUClockSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11LocalACCPUClockSpeed.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11LocalACCPUClockSpeed.setUnits('Hz')
_H3cDot11LocalACMemoryType_Type=OctetString
_H3cDot11LocalACMemoryType_Object=MibTableColumn
h3cDot11LocalACMemoryType=_H3cDot11LocalACMemoryType_Object((1,3,6,1,4,1,2011,10,2,75,1,1,8,1,6),_H3cDot11LocalACMemoryType_Type())
h3cDot11LocalACMemoryType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11LocalACMemoryType.setStatus(_A)
_H3cDot11LocalACMemorySize_Type=Unsigned32
_H3cDot11LocalACMemorySize_Object=MibTableColumn
h3cDot11LocalACMemorySize=_H3cDot11LocalACMemorySize_Object((1,3,6,1,4,1,2011,10,2,75,1,1,8,1,7),_H3cDot11LocalACMemorySize_Type())
h3cDot11LocalACMemorySize.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11LocalACMemorySize.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11LocalACMemorySize.setUnits(_W)
_H3cDot11LocalACFlashType_Type=OctetString
_H3cDot11LocalACFlashType_Object=MibTableColumn
h3cDot11LocalACFlashType=_H3cDot11LocalACFlashType_Object((1,3,6,1,4,1,2011,10,2,75,1,1,8,1,8),_H3cDot11LocalACFlashType_Type())
h3cDot11LocalACFlashType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11LocalACFlashType.setStatus(_A)
_H3cDot11LocalACFlashSize_Type=Unsigned32
_H3cDot11LocalACFlashSize_Object=MibTableColumn
h3cDot11LocalACFlashSize=_H3cDot11LocalACFlashSize_Object((1,3,6,1,4,1,2011,10,2,75,1,1,8,1,9),_H3cDot11LocalACFlashSize_Type())
h3cDot11LocalACFlashSize.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11LocalACFlashSize.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11LocalACFlashSize.setUnits(_W)
_H3cDot11LocalACMemSize_Type=Counter64
_H3cDot11LocalACMemSize_Object=MibTableColumn
h3cDot11LocalACMemSize=_H3cDot11LocalACMemSize_Object((1,3,6,1,4,1,2011,10,2,75,1,1,8,1,10),_H3cDot11LocalACMemSize_Type())
h3cDot11LocalACMemSize.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11LocalACMemSize.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11LocalACMemSize.setUnits('bytes')
_H3cDot11LocalACFlashSizeInBytes_Type=Counter64
_H3cDot11LocalACFlashSizeInBytes_Object=MibTableColumn
h3cDot11LocalACFlashSizeInBytes=_H3cDot11LocalACFlashSizeInBytes_Object((1,3,6,1,4,1,2011,10,2,75,1,1,8,1,11),_H3cDot11LocalACFlashSizeInBytes_Type())
h3cDot11LocalACFlashSizeInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11LocalACFlashSizeInBytes.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11LocalACFlashSizeInBytes.setUnits('bytes')
_H3cDot11CAPWAPTunnelGroup_ObjectIdentity=ObjectIdentity
h3cDot11CAPWAPTunnelGroup=_H3cDot11CAPWAPTunnelGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,1,2))
_H3cDot11CAPWAPTunnelTable_Object=MibTable
h3cDot11CAPWAPTunnelTable=_H3cDot11CAPWAPTunnelTable_Object((1,3,6,1,4,1,2011,10,2,75,1,2,1))
if mibBuilder.loadTexts:h3cDot11CAPWAPTunnelTable.setStatus(_A)
_H3cDot11CAPWAPTunnelEntry_Object=MibTableRow
h3cDot11CAPWAPTunnelEntry=_H3cDot11CAPWAPTunnelEntry_Object((1,3,6,1,4,1,2011,10,2,75,1,2,1,1))
h3cDot11CAPWAPTunnelEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:h3cDot11CAPWAPTunnelEntry.setStatus(_A)
_H3cDot11CurrTunnelAPID_Type=H3cDot11ObjectIDType
_H3cDot11CurrTunnelAPID_Object=MibTableColumn
h3cDot11CurrTunnelAPID=_H3cDot11CurrTunnelAPID_Object((1,3,6,1,4,1,2011,10,2,75,1,2,1,1,1),_H3cDot11CurrTunnelAPID_Type())
h3cDot11CurrTunnelAPID.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11CurrTunnelAPID.setStatus(_A)
class _H3cDot11CtrlTunnelCurrSec_Type(H3cDot11TunnelSecSchemType):defaultValue=1
_H3cDot11CtrlTunnelCurrSec_Type.__name__=_I
_H3cDot11CtrlTunnelCurrSec_Object=MibTableColumn
h3cDot11CtrlTunnelCurrSec=_H3cDot11CtrlTunnelCurrSec_Object((1,3,6,1,4,1,2011,10,2,75,1,2,1,1,2),_H3cDot11CtrlTunnelCurrSec_Type())
h3cDot11CtrlTunnelCurrSec.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CtrlTunnelCurrSec.setStatus(_A)
_H3cDot11CtrlTunnelUpTime_Type=Integer32
_H3cDot11CtrlTunnelUpTime_Object=MibTableColumn
h3cDot11CtrlTunnelUpTime=_H3cDot11CtrlTunnelUpTime_Object((1,3,6,1,4,1,2011,10,2,75,1,2,1,1,3),_H3cDot11CtrlTunnelUpTime_Type())
h3cDot11CtrlTunnelUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CtrlTunnelUpTime.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11CtrlTunnelUpTime.setUnits(_X)
class _H3cDot11DataTunnelCurrSec_Type(H3cDot11TunnelSecSchemType):defaultValue=1
_H3cDot11DataTunnelCurrSec_Type.__name__=_I
_H3cDot11DataTunnelCurrSec_Object=MibTableColumn
h3cDot11DataTunnelCurrSec=_H3cDot11DataTunnelCurrSec_Object((1,3,6,1,4,1,2011,10,2,75,1,2,1,1,4),_H3cDot11DataTunnelCurrSec_Type())
h3cDot11DataTunnelCurrSec.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11DataTunnelCurrSec.setStatus(_A)
_H3cDot11DataTunnelUpTime_Type=Integer32
_H3cDot11DataTunnelUpTime_Object=MibTableColumn
h3cDot11DataTunnelUpTime=_H3cDot11DataTunnelUpTime_Object((1,3,6,1,4,1,2011,10,2,75,1,2,1,1,5),_H3cDot11DataTunnelUpTime_Type())
h3cDot11DataTunnelUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11DataTunnelUpTime.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11DataTunnelUpTime.setUnits(_X)
_H3cDot11CtrlTunnelUpTimeTicks_Type=TimeTicks
_H3cDot11CtrlTunnelUpTimeTicks_Object=MibTableColumn
h3cDot11CtrlTunnelUpTimeTicks=_H3cDot11CtrlTunnelUpTimeTicks_Object((1,3,6,1,4,1,2011,10,2,75,1,2,1,1,6),_H3cDot11CtrlTunnelUpTimeTicks_Type())
h3cDot11CtrlTunnelUpTimeTicks.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CtrlTunnelUpTimeTicks.setStatus(_A)
_H3cDot11ACMtNotifyGroup_ObjectIdentity=ObjectIdentity
h3cDot11ACMtNotifyGroup=_H3cDot11ACMtNotifyGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,1,3))
_H3cDot11ACMtTraps_ObjectIdentity=ObjectIdentity
h3cDot11ACMtTraps=_H3cDot11ACMtTraps_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,1,3,0))
_H3cDot11ACMtTrapVarObjects_ObjectIdentity=ObjectIdentity
h3cDot11ACMtTrapVarObjects=_H3cDot11ACMtTrapVarObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,1,3,1))
class _H3cDot11ACMtTrapTunlDwnInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('tunnelTimeout',1),('keyUpdateFailure',2),('apReset',3),('apCrash',4),('apDeleted',5),('apCfgChange',6)))
_H3cDot11ACMtTrapTunlDwnInfo_Type.__name__=_E
_H3cDot11ACMtTrapTunlDwnInfo_Object=MibScalar
h3cDot11ACMtTrapTunlDwnInfo=_H3cDot11ACMtTrapTunlDwnInfo_Object((1,3,6,1,4,1,2011,10,2,75,1,3,1,1),_H3cDot11ACMtTrapTunlDwnInfo_Type())
h3cDot11ACMtTrapTunlDwnInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11ACMtTrapTunlDwnInfo.setStatus(_A)
class _H3cDot11ACMtTrapTunlUpInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('up',1))
_H3cDot11ACMtTrapTunlUpInfo_Type.__name__=_E
_H3cDot11ACMtTrapTunlUpInfo_Object=MibScalar
h3cDot11ACMtTrapTunlUpInfo=_H3cDot11ACMtTrapTunlUpInfo_Object((1,3,6,1,4,1,2011,10,2,75,1,3,1,2),_H3cDot11ACMtTrapTunlUpInfo_Type())
h3cDot11ACMtTrapTunlUpInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11ACMtTrapTunlUpInfo.setStatus(_A)
class _H3cDot11ACMtTrapBackupSwitchInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('masterToSlave',1),('slaveToMaster',2)))
_H3cDot11ACMtTrapBackupSwitchInfo_Type.__name__=_E
_H3cDot11ACMtTrapBackupSwitchInfo_Object=MibScalar
h3cDot11ACMtTrapBackupSwitchInfo=_H3cDot11ACMtTrapBackupSwitchInfo_Object((1,3,6,1,4,1,2011,10,2,75,1,3,1,3),_H3cDot11ACMtTrapBackupSwitchInfo_Type())
h3cDot11ACMtTrapBackupSwitchInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11ACMtTrapBackupSwitchInfo.setStatus(_A)
_H3cDot11ACMtTrapTnlAPName_Type=OctetString
_H3cDot11ACMtTrapTnlAPName_Object=MibScalar
h3cDot11ACMtTrapTnlAPName=_H3cDot11ACMtTrapTnlAPName_Object((1,3,6,1,4,1,2011,10,2,75,1,3,1,4),_H3cDot11ACMtTrapTnlAPName_Type())
h3cDot11ACMtTrapTnlAPName.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11ACMtTrapTnlAPName.setStatus(_A)
_H3cDot11ACMtTrapTnlAPIPAddr_Type=IpAddress
_H3cDot11ACMtTrapTnlAPIPAddr_Object=MibScalar
h3cDot11ACMtTrapTnlAPIPAddr=_H3cDot11ACMtTrapTnlAPIPAddr_Object((1,3,6,1,4,1,2011,10,2,75,1,3,1,5),_H3cDot11ACMtTrapTnlAPIPAddr_Type())
h3cDot11ACMtTrapTnlAPIPAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11ACMtTrapTnlAPIPAddr.setStatus(_A)
class _H3cDot11LoadBalanceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('traffic',1),('session',2)))
_H3cDot11LoadBalanceType_Type.__name__=_E
_H3cDot11LoadBalanceType_Object=MibScalar
h3cDot11LoadBalanceType=_H3cDot11LoadBalanceType_Object((1,3,6,1,4,1,2011,10,2,75,1,3,1,6),_H3cDot11LoadBalanceType_Type())
h3cDot11LoadBalanceType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11LoadBalanceType.setStatus(_A)
_H3cDot11LoadBalanceThreshold_Type=Integer32
_H3cDot11LoadBalanceThreshold_Object=MibScalar
h3cDot11LoadBalanceThreshold=_H3cDot11LoadBalanceThreshold_Object((1,3,6,1,4,1,2011,10,2,75,1,3,1,7),_H3cDot11LoadBalanceThreshold_Type())
h3cDot11LoadBalanceThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11LoadBalanceThreshold.setStatus(_A)
_H3cDot11ACMtTrapAPIPv6Addr_Type=OctetString
_H3cDot11ACMtTrapAPIPv6Addr_Object=MibScalar
h3cDot11ACMtTrapAPIPv6Addr=_H3cDot11ACMtTrapAPIPv6Addr_Object((1,3,6,1,4,1,2011,10,2,75,1,3,1,8),_H3cDot11ACMtTrapAPIPv6Addr_Type())
h3cDot11ACMtTrapAPIPv6Addr.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11ACMtTrapAPIPv6Addr.setStatus(_A)
_H3cDot11ACMtTrapTunlDwnCount_Type=Integer32
_H3cDot11ACMtTrapTunlDwnCount_Object=MibScalar
h3cDot11ACMtTrapTunlDwnCount=_H3cDot11ACMtTrapTunlDwnCount_Object((1,3,6,1,4,1,2011,10,2,75,1,3,1,9),_H3cDot11ACMtTrapTunlDwnCount_Type())
h3cDot11ACMtTrapTunlDwnCount.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11ACMtTrapTunlDwnCount.setStatus(_A)
_H3cDot11ACMaxStaNum_Type=Integer32
_H3cDot11ACMaxStaNum_Object=MibScalar
h3cDot11ACMaxStaNum=_H3cDot11ACMaxStaNum_Object((1,3,6,1,4,1,2011,10,2,75,1,3,1,10),_H3cDot11ACMaxStaNum_Type())
h3cDot11ACMaxStaNum.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11ACMaxStaNum.setStatus(_A)
_H3cDot11ACMtTrapTnlAPSysName_Type=OctetString
_H3cDot11ACMtTrapTnlAPSysName_Object=MibScalar
h3cDot11ACMtTrapTnlAPSysName=_H3cDot11ACMtTrapTnlAPSysName_Object((1,3,6,1,4,1,2011,10,2,75,1,3,1,11),_H3cDot11ACMtTrapTnlAPSysName_Type())
h3cDot11ACMtTrapTnlAPSysName.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11ACMtTrapTnlAPSysName.setStatus(_A)
_H3cDot11ACMtFirstTrapTime_Type=TimeTicks
_H3cDot11ACMtFirstTrapTime_Object=MibScalar
h3cDot11ACMtFirstTrapTime=_H3cDot11ACMtFirstTrapTime_Object((1,3,6,1,4,1,2011,10,2,75,1,3,1,12),_H3cDot11ACMtFirstTrapTime_Type())
h3cDot11ACMtFirstTrapTime.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11ACMtFirstTrapTime.setStatus(_A)
class _H3cDot11ACStatusSwitchInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('activeToStandby',1),('standbyToActive',2)))
_H3cDot11ACStatusSwitchInfo_Type.__name__=_E
_H3cDot11ACStatusSwitchInfo_Object=MibScalar
h3cDot11ACStatusSwitchInfo=_H3cDot11ACStatusSwitchInfo_Object((1,3,6,1,4,1,2011,10,2,75,1,3,1,13),_H3cDot11ACStatusSwitchInfo_Type())
h3cDot11ACStatusSwitchInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11ACStatusSwitchInfo.setStatus(_A)
_H3cDot11SourceACNmsIP_Type=IpAddress
_H3cDot11SourceACNmsIP_Object=MibScalar
h3cDot11SourceACNmsIP=_H3cDot11SourceACNmsIP_Object((1,3,6,1,4,1,2011,10,2,75,1,3,1,14),_H3cDot11SourceACNmsIP_Type())
h3cDot11SourceACNmsIP.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SourceACNmsIP.setStatus(_A)
_H3cDot11ACMtTrapAPMacAddress_Type=MacAddress
_H3cDot11ACMtTrapAPMacAddress_Object=MibScalar
h3cDot11ACMtTrapAPMacAddress=_H3cDot11ACMtTrapAPMacAddress_Object((1,3,6,1,4,1,2011,10,2,75,1,3,1,15),_H3cDot11ACMtTrapAPMacAddress_Type())
h3cDot11ACMtTrapAPMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11ACMtTrapAPMacAddress.setStatus(_A)
h3cDot11ACMtTunnelSetupTrap=NotificationType((1,3,6,1,4,1,2011,10,2,75,1,3,0,1))
h3cDot11ACMtTunnelSetupTrap.setObjects(*((_C,_G),(_C,_Y),(_C,_L),(_C,_M),(_C,_N),(_C,_H),(_C,_O)))
if mibBuilder.loadTexts:h3cDot11ACMtTunnelSetupTrap.setStatus(_A)
h3cDot11ACMtTunnelDownTrap=NotificationType((1,3,6,1,4,1,2011,10,2,75,1,3,0,2))
h3cDot11ACMtTunnelDownTrap.setObjects(*((_C,_G),(_C,_Z),(_C,_L),(_C,_M),(_C,_N),(_C,_a),(_C,_b),(_C,_H),(_C,_O)))
if mibBuilder.loadTexts:h3cDot11ACMtTunnelDownTrap.setStatus(_A)
h3cDot11ACMtBackupSwtTrap=NotificationType((1,3,6,1,4,1,2011,10,2,75,1,3,0,3))
h3cDot11ACMtBackupSwtTrap.setObjects(*((_C,_c),(_C,_H)))
if mibBuilder.loadTexts:h3cDot11ACMtBackupSwtTrap.setStatus(_A)
h3cDot11ACLoadBalanceTrap=NotificationType((1,3,6,1,4,1,2011,10,2,75,1,3,0,4))
h3cDot11ACLoadBalanceTrap.setObjects(*((_C,_d),(_C,_e)))
if mibBuilder.loadTexts:h3cDot11ACLoadBalanceTrap.setStatus(_A)
h3cDot11ACStaFullTrap=NotificationType((1,3,6,1,4,1,2011,10,2,75,1,3,0,5))
h3cDot11ACStaFullTrap.setObjects((_C,_f))
if mibBuilder.loadTexts:h3cDot11ACStaFullTrap.setStatus(_A)
h3cDot11ACStatusSwitchTrap=NotificationType((1,3,6,1,4,1,2011,10,2,75,1,3,0,6))
h3cDot11ACStatusSwitchTrap.setObjects(*((_C,_g),(_C,_h)))
if mibBuilder.loadTexts:h3cDot11ACStatusSwitchTrap.setStatus(_A)
h3cDot11RunAPNumOverload=NotificationType((1,3,6,1,4,1,2011,10,2,75,1,3,0,7))
h3cDot11RunAPNumOverload.setObjects(*((_C,_P),(_C,_Q)))
if mibBuilder.loadTexts:h3cDot11RunAPNumOverload.setStatus(_A)
h3cDot11RunAPNumOverloadRecover=NotificationType((1,3,6,1,4,1,2011,10,2,75,1,3,0,8))
h3cDot11RunAPNumOverloadRecover.setObjects(*((_C,_P),(_C,_Q)))
if mibBuilder.loadTexts:h3cDot11RunAPNumOverloadRecover.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'h3cDot11ACMT':h3cDot11ACMT,'h3cDot11ACObjectGroup':h3cDot11ACObjectGroup,'h3cDot11ACObject':h3cDot11ACObject,'h3cDot11CurrentACMACMode':h3cDot11CurrentACMACMode,_P:h3cDot11MaxAPNumPermitted,'h3cDot11MaxStationNumPermitted':h3cDot11MaxStationNumPermitted,'h3cDot11RunAPNumThreshold':h3cDot11RunAPNumThreshold,'h3cDot11MaxNewConnCntPerSecCM':h3cDot11MaxNewConnCntPerSecCM,'h3cDot11IFNumberCM':h3cDot11IFNumberCM,'h3cDot11APLicenseWeight':h3cDot11APLicenseWeight,'h3cDot11ACLoadInfo':h3cDot11ACLoadInfo,_Q:h3cDot11APConnectCount,'h3cDot11StationConnectCount':h3cDot11StationConnectCount,'h3cDot11ACIFLoadInfoTable':h3cDot11ACIFLoadInfoTable,'h3cDot11ACIFLoadInfoEntry':h3cDot11ACIFLoadInfoEntry,_S:h3cDot11ACIfIndex,'h3cDot11ACIfApNum':h3cDot11ACIfApNum,'h3cDot11ACIfStaNum':h3cDot11ACIfStaNum,'h3cDot11ACIfName':h3cDot11ACIfName,'h3cDot11MasterAPCount':h3cDot11MasterAPCount,'h3cDot11SlaveAPCount':h3cDot11SlaveAPCount,'h3cDot11ConnectAutoAPCount':h3cDot11ConnectAutoAPCount,'h3cDot11PersistentAPCount':h3cDot11PersistentAPCount,'h3cDot11AcUploadFrameCnt':h3cDot11AcUploadFrameCnt,'h3cDot11AcDownloadFrameCnt':h3cDot11AcDownloadFrameCnt,'h3cDot11AcUploadFrameBytes':h3cDot11AcUploadFrameBytes,'h3cDot11AcDownloadFrameBytes':h3cDot11AcDownloadFrameBytes,'h3cDot11BackupACRole':h3cDot11BackupACRole,'h3cDot11BackupACNMSIP':h3cDot11BackupACNMSIP,'h3cDot11ACBackupMode':h3cDot11ACBackupMode,'h3cDot11ACBackupStatus':h3cDot11ACBackupStatus,'h3cDot11ACSwitchCnt':h3cDot11ACSwitchCnt,'h3cDot11ACSouthifPacketOutputCount':h3cDot11ACSouthifPacketOutputCount,'h3cDot11ACSouthifPacketOutputBytes':h3cDot11ACSouthifPacketOutputBytes,'h3cDot11ACSouthifPacketInputCount':h3cDot11ACSouthifPacketInputCount,'h3cDot11ACSouthifPacketInputBytes':h3cDot11ACSouthifPacketInputBytes,'h3cDot11TotalAPconnected':h3cDot11TotalAPconnected,'h3cDot11RemainingAPcapacity':h3cDot11RemainingAPcapacity,'h3cDot11WLANAssocStatisInfo':h3cDot11WLANAssocStatisInfo,'h3cDot11StationAssocSum':h3cDot11StationAssocSum,'h3cDot11StationAssocFailSum':h3cDot11StationAssocFailSum,'h3cDot11StationReassocSum':h3cDot11StationReassocSum,'h3cDot11StationAssocRejectedSum':h3cDot11StationAssocRejectedSum,'h3cDot11StationExDeAuthenSum':h3cDot11StationExDeAuthenSum,'h3cDot11StationCurAssocSum':h3cDot11StationCurAssocSum,'h3cDot11StationAssocReqSum':h3cDot11StationAssocReqSum,'h3cDot11StationReassocReqSum':h3cDot11StationReassocReqSum,'h3cDot11StationReassocFailSum':h3cDot11StationReassocFailSum,'h3cDot11ACBASInfo':h3cDot11ACBASInfo,'h3cDot11ACBASSysObjects':h3cDot11ACBASSysObjects,'h3cDot11ACBASTableObjects':h3cDot11ACBASTableObjects,'h3cDot11ACBASIfTable':h3cDot11ACBASIfTable,'h3cDot11ACBASIfEntry':h3cDot11ACBASIfEntry,_T:h3cDot11ACBASIfIndex,'h3cDot11ACBASIfDescr':h3cDot11ACBASIfDescr,'h3cDot11ACBASIfType':h3cDot11ACBASIfType,'h3cDot11ACStaUserSecAuthStatis':h3cDot11ACStaUserSecAuthStatis,'h3cDot11ACStaUserAuthCurNumber':h3cDot11ACStaUserAuthCurNumber,'h3cDot11ACStaUserConnFailCnt':h3cDot11ACStaUserConnFailCnt,'h3cDot11ACStaUserAuthReqCnt':h3cDot11ACStaUserAuthReqCnt,'h3cDot11ACStaUserAuthSuccCnt':h3cDot11ACStaUserAuthSuccCnt,'h3cDot11ACStaUserAuthFailCnt':h3cDot11ACStaUserAuthFailCnt,'h3cDot11ACStaUserAllAuthCntCM':h3cDot11ACStaUserAllAuthCntCM,'h3cDot11ACStaUserAuthRespCntCM':h3cDot11ACStaUserAuthRespCntCM,'h3cDot11ACStaSecAuthTypeStatis':h3cDot11ACStaSecAuthTypeStatis,'h3cDot11ACStaUserPortalOnlineNum':h3cDot11ACStaUserPortalOnlineNum,'h3cDot11ACStaUserFreeAuthOnlineNum':h3cDot11ACStaUserFreeAuthOnlineNum,'h3cDot11ACStaUserAssociateAuthOnlineNum':h3cDot11ACStaUserAssociateAuthOnlineNum,'h3cDot11ACStaUserMacAuthOnlineNum':h3cDot11ACStaUserMacAuthOnlineNum,'h3cDot11ACStaUserPortalLostConnectionCnt':h3cDot11ACStaUserPortalLostConnectionCnt,'h3cDot11ACStaUserFreeAuthLostConnectionCnt':h3cDot11ACStaUserFreeAuthLostConnectionCnt,'h3cDot11ACStaUserAssociateAuthLostConnectionCnt':h3cDot11ACStaUserAssociateAuthLostConnectionCnt,'h3cDot11ACStaUserMacAuthLostConnectionCnt':h3cDot11ACStaUserMacAuthLostConnectionCnt,'h3cDot11ACStaPortalAuthReqCnt':h3cDot11ACStaPortalAuthReqCnt,'h3cDot11ACStaAssociateAuthReqCnt':h3cDot11ACStaAssociateAuthReqCnt,'h3cDot11ACStaMacAuthReqCnt':h3cDot11ACStaMacAuthReqCnt,'h3cDot11ACStaPortalAuthSuccCnt':h3cDot11ACStaPortalAuthSuccCnt,'h3cDot11ACStaAssociateAuthSuccCnt':h3cDot11ACStaAssociateAuthSuccCnt,'h3cDot11ACStaMacAuthSuccCnt':h3cDot11ACStaMacAuthSuccCnt,'h3cDot11ACStaPortalAuthReqFailCnt':h3cDot11ACStaPortalAuthReqFailCnt,'h3cDot11ACStaAssociateAuthReqFailCnt':h3cDot11ACStaAssociateAuthReqFailCnt,'h3cDot11ACStaMacAuthReqFailCnt':h3cDot11ACStaMacAuthReqFailCnt,'h3cDot11ACStaUserAutoAuthOnlineNumCM':h3cDot11ACStaUserAutoAuthOnlineNumCM,'h3cDot11ACStaUserAutoAuthLostConnectionCntCM':h3cDot11ACStaUserAutoAuthLostConnectionCntCM,'h3cDot11ACStaAutoAuthReqCntCM':h3cDot11ACStaAutoAuthReqCntCM,'h3cDot11ACStaAutoAuthSuccCntCM':h3cDot11ACStaAutoAuthSuccCntCM,'h3cDot11ACStaAutoAuthReqFailCntCM':h3cDot11ACStaAutoAuthReqFailCntCM,'h3cDot11ACPortalStatisticCMTable':h3cDot11ACPortalStatisticCMTable,'h3cDot11ACPortalStatisticCMEntry':h3cDot11ACPortalStatisticCMEntry,_U:h3cDot11ACPortalStatisticSSIDCM,'h3cDot11ACPortalStatAuthReqCM':h3cDot11ACPortalStatAuthReqCM,'h3cDot11ACPortalStatAuthRespCM':h3cDot11ACPortalStatAuthRespCM,'h3cDot11LocalACModelTable':h3cDot11LocalACModelTable,'h3cDot11LocalACModelEntry':h3cDot11LocalACModelEntry,_V:h3cDot11LocalACModelAlias,'h3cDot11LocalACModelName':h3cDot11LocalACModelName,'h3cDot11LocalACManufacturer':h3cDot11LocalACManufacturer,'h3cDot11LocalACCPUType':h3cDot11LocalACCPUType,'h3cDot11LocalACCPUClockSpeed':h3cDot11LocalACCPUClockSpeed,'h3cDot11LocalACMemoryType':h3cDot11LocalACMemoryType,'h3cDot11LocalACMemorySize':h3cDot11LocalACMemorySize,'h3cDot11LocalACFlashType':h3cDot11LocalACFlashType,'h3cDot11LocalACFlashSize':h3cDot11LocalACFlashSize,'h3cDot11LocalACMemSize':h3cDot11LocalACMemSize,'h3cDot11LocalACFlashSizeInBytes':h3cDot11LocalACFlashSizeInBytes,'h3cDot11CAPWAPTunnelGroup':h3cDot11CAPWAPTunnelGroup,'h3cDot11CAPWAPTunnelTable':h3cDot11CAPWAPTunnelTable,'h3cDot11CAPWAPTunnelEntry':h3cDot11CAPWAPTunnelEntry,_G:h3cDot11CurrTunnelAPID,'h3cDot11CtrlTunnelCurrSec':h3cDot11CtrlTunnelCurrSec,'h3cDot11CtrlTunnelUpTime':h3cDot11CtrlTunnelUpTime,'h3cDot11DataTunnelCurrSec':h3cDot11DataTunnelCurrSec,'h3cDot11DataTunnelUpTime':h3cDot11DataTunnelUpTime,'h3cDot11CtrlTunnelUpTimeTicks':h3cDot11CtrlTunnelUpTimeTicks,'h3cDot11ACMtNotifyGroup':h3cDot11ACMtNotifyGroup,'h3cDot11ACMtTraps':h3cDot11ACMtTraps,'h3cDot11ACMtTunnelSetupTrap':h3cDot11ACMtTunnelSetupTrap,'h3cDot11ACMtTunnelDownTrap':h3cDot11ACMtTunnelDownTrap,'h3cDot11ACMtBackupSwtTrap':h3cDot11ACMtBackupSwtTrap,'h3cDot11ACLoadBalanceTrap':h3cDot11ACLoadBalanceTrap,'h3cDot11ACStaFullTrap':h3cDot11ACStaFullTrap,'h3cDot11ACStatusSwitchTrap':h3cDot11ACStatusSwitchTrap,'h3cDot11RunAPNumOverload':h3cDot11RunAPNumOverload,'h3cDot11RunAPNumOverloadRecover':h3cDot11RunAPNumOverloadRecover,'h3cDot11ACMtTrapVarObjects':h3cDot11ACMtTrapVarObjects,_Z:h3cDot11ACMtTrapTunlDwnInfo,_Y:h3cDot11ACMtTrapTunlUpInfo,_c:h3cDot11ACMtTrapBackupSwitchInfo,_L:h3cDot11ACMtTrapTnlAPName,_M:h3cDot11ACMtTrapTnlAPIPAddr,_d:h3cDot11LoadBalanceType,_e:h3cDot11LoadBalanceThreshold,_N:h3cDot11ACMtTrapAPIPv6Addr,_a:h3cDot11ACMtTrapTunlDwnCount,_f:h3cDot11ACMaxStaNum,_b:h3cDot11ACMtTrapTnlAPSysName,_H:h3cDot11ACMtFirstTrapTime,_g:h3cDot11ACStatusSwitchInfo,_h:h3cDot11SourceACNmsIP,_O:h3cDot11ACMtTrapAPMacAddress})