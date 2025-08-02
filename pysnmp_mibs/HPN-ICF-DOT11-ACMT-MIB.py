_e='hpnicfDot11SourceACNmsIP'
_d='hpnicfDot11ACStatusSwitchInfo'
_c='hpnicfDot11ACMaxStaNum'
_b='hpnicfDot11LoadBalanceThreshold'
_a='hpnicfDot11LoadBalanceType'
_Z='hpnicfDot11ACMtTrapBackupSwitchInfo'
_Y='hpnicfDot11ACMtTrapTnlAPSysName'
_X='hpnicfDot11ACMtTrapTunlDwnCount'
_W='hpnicfDot11ACMtTrapTunlDwnInfo'
_V='hpnicfDot11ACMtTrapTunlUpInfo'
_U='second'
_T='hpnicfDot11ACPortalStatisticSSIDCM'
_S='not-accessible'
_R='hpnicfDot11ACBASIfIndex'
_Q='hpnicfDot11ACIfIndex'
_P='HpnicfDot11MACModeType'
_O='hpnicfDot11APConnectCount'
_N='hpnicfDot11MaxAPNumPermitted'
_M='hpnicfDot11ACMtTrapAPMacAddress'
_L='hpnicfDot11ACMtTrapAPIPv6Addr'
_K='hpnicfDot11ACMtTrapTnlAPIPAddr'
_J='hpnicfDot11ACMtTrapTnlAPName'
_I='HpnicfDot11TunnelSecSchemType'
_H='OctetString'
_G='hpnicfDot11ACMtFirstTrapTime'
_F='hpnicfDot11CurrTunnelAPID'
_E='Integer32'
_D='accessible-for-notify'
_C='HPN-ICF-DOT11-ACMT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HpnicfDot11MACModeType,HpnicfDot11ObjectIDType,HpnicfDot11TunnelSecSchemType,hpnicfDot11=mibBuilder.importSymbols('HPN-ICF-DOT11-REF-MIB',_P,'HpnicfDot11ObjectIDType',_I,'hpnicfDot11')
IANAifType,=mibBuilder.importSymbols('IANAifType-MIB','IANAifType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
hpnicfDot11ACMT=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,1))
if mibBuilder.loadTexts:hpnicfDot11ACMT.setRevisions(('2010-08-04 18:00','2009-08-07 18:00','2009-07-29 18:00','2009-05-07 20:00','2008-07-09 18:00','2007-12-21 18:00','2007-06-19 18:00','2007-04-27 20:00','2006-05-10 19:00'))
_HpnicfDot11ACObjectGroup_ObjectIdentity=ObjectIdentity
hpnicfDot11ACObjectGroup=_HpnicfDot11ACObjectGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1))
_HpnicfDot11ACObject_ObjectIdentity=ObjectIdentity
hpnicfDot11ACObject=_HpnicfDot11ACObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,1))
class _HpnicfDot11CurrentACMACMode_Type(HpnicfDot11MACModeType):defaultValue=1
_HpnicfDot11CurrentACMACMode_Type.__name__=_P
_HpnicfDot11CurrentACMACMode_Object=MibScalar
hpnicfDot11CurrentACMACMode=_HpnicfDot11CurrentACMACMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,1,1),_HpnicfDot11CurrentACMACMode_Type())
hpnicfDot11CurrentACMACMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CurrentACMACMode.setStatus(_A)
_HpnicfDot11MaxAPNumPermitted_Type=Integer32
_HpnicfDot11MaxAPNumPermitted_Object=MibScalar
hpnicfDot11MaxAPNumPermitted=_HpnicfDot11MaxAPNumPermitted_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,1,2),_HpnicfDot11MaxAPNumPermitted_Type())
hpnicfDot11MaxAPNumPermitted.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11MaxAPNumPermitted.setStatus(_A)
_HpnicfDot11MaxStationNumPermitted_Type=Integer32
_HpnicfDot11MaxStationNumPermitted_Object=MibScalar
hpnicfDot11MaxStationNumPermitted=_HpnicfDot11MaxStationNumPermitted_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,1,3),_HpnicfDot11MaxStationNumPermitted_Type())
hpnicfDot11MaxStationNumPermitted.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11MaxStationNumPermitted.setStatus(_A)
class _HpnicfDot11RunAPNumThreshold_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,100))
_HpnicfDot11RunAPNumThreshold_Type.__name__=_E
_HpnicfDot11RunAPNumThreshold_Object=MibScalar
hpnicfDot11RunAPNumThreshold=_HpnicfDot11RunAPNumThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,1,4),_HpnicfDot11RunAPNumThreshold_Type())
hpnicfDot11RunAPNumThreshold.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpnicfDot11RunAPNumThreshold.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RunAPNumThreshold.setUnits('percent')
_HpnicfDot11ACLoadInfo_ObjectIdentity=ObjectIdentity
hpnicfDot11ACLoadInfo=_HpnicfDot11ACLoadInfo_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,2))
_HpnicfDot11APConnectCount_Type=Integer32
_HpnicfDot11APConnectCount_Object=MibScalar
hpnicfDot11APConnectCount=_HpnicfDot11APConnectCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,2,1),_HpnicfDot11APConnectCount_Type())
hpnicfDot11APConnectCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APConnectCount.setStatus(_A)
_HpnicfDot11StationConnectCount_Type=Integer32
_HpnicfDot11StationConnectCount_Object=MibScalar
hpnicfDot11StationConnectCount=_HpnicfDot11StationConnectCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,2,2),_HpnicfDot11StationConnectCount_Type())
hpnicfDot11StationConnectCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11StationConnectCount.setStatus(_A)
_HpnicfDot11ACIFLoadInfoTable_Object=MibTable
hpnicfDot11ACIFLoadInfoTable=_HpnicfDot11ACIFLoadInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,2,3))
if mibBuilder.loadTexts:hpnicfDot11ACIFLoadInfoTable.setStatus(_A)
_HpnicfDot11ACIFLoadInfoEntry_Object=MibTableRow
hpnicfDot11ACIFLoadInfoEntry=_HpnicfDot11ACIFLoadInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,2,3,1))
hpnicfDot11ACIFLoadInfoEntry.setIndexNames((0,_C,_Q))
if mibBuilder.loadTexts:hpnicfDot11ACIFLoadInfoEntry.setStatus(_A)
_HpnicfDot11ACIfIndex_Type=Integer32
_HpnicfDot11ACIfIndex_Object=MibTableColumn
hpnicfDot11ACIfIndex=_HpnicfDot11ACIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,2,3,1,1),_HpnicfDot11ACIfIndex_Type())
hpnicfDot11ACIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11ACIfIndex.setStatus(_A)
_HpnicfDot11ACIfApNum_Type=Integer32
_HpnicfDot11ACIfApNum_Object=MibTableColumn
hpnicfDot11ACIfApNum=_HpnicfDot11ACIfApNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,2,3,1,2),_HpnicfDot11ACIfApNum_Type())
hpnicfDot11ACIfApNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACIfApNum.setStatus(_A)
_HpnicfDot11ACIfStaNum_Type=Integer32
_HpnicfDot11ACIfStaNum_Object=MibTableColumn
hpnicfDot11ACIfStaNum=_HpnicfDot11ACIfStaNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,2,3,1,3),_HpnicfDot11ACIfStaNum_Type())
hpnicfDot11ACIfStaNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACIfStaNum.setStatus(_A)
_HpnicfDot11ACIfName_Type=OctetString
_HpnicfDot11ACIfName_Object=MibTableColumn
hpnicfDot11ACIfName=_HpnicfDot11ACIfName_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,2,3,1,4),_HpnicfDot11ACIfName_Type())
hpnicfDot11ACIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACIfName.setStatus(_A)
_HpnicfDot11MasterAPCount_Type=Integer32
_HpnicfDot11MasterAPCount_Object=MibScalar
hpnicfDot11MasterAPCount=_HpnicfDot11MasterAPCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,2,4),_HpnicfDot11MasterAPCount_Type())
hpnicfDot11MasterAPCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11MasterAPCount.setStatus(_A)
_HpnicfDot11SlaveAPCount_Type=Integer32
_HpnicfDot11SlaveAPCount_Object=MibScalar
hpnicfDot11SlaveAPCount=_HpnicfDot11SlaveAPCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,2,5),_HpnicfDot11SlaveAPCount_Type())
hpnicfDot11SlaveAPCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11SlaveAPCount.setStatus(_A)
_HpnicfDot11ConnectAutoAPCount_Type=Integer32
_HpnicfDot11ConnectAutoAPCount_Object=MibScalar
hpnicfDot11ConnectAutoAPCount=_HpnicfDot11ConnectAutoAPCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,2,6),_HpnicfDot11ConnectAutoAPCount_Type())
hpnicfDot11ConnectAutoAPCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ConnectAutoAPCount.setStatus(_A)
_HpnicfDot11PersistentAPCount_Type=Integer32
_HpnicfDot11PersistentAPCount_Object=MibScalar
hpnicfDot11PersistentAPCount=_HpnicfDot11PersistentAPCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,2,7),_HpnicfDot11PersistentAPCount_Type())
hpnicfDot11PersistentAPCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11PersistentAPCount.setStatus(_A)
_HpnicfDot11AcUploadFrameCnt_Type=Counter64
_HpnicfDot11AcUploadFrameCnt_Object=MibScalar
hpnicfDot11AcUploadFrameCnt=_HpnicfDot11AcUploadFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,2,8),_HpnicfDot11AcUploadFrameCnt_Type())
hpnicfDot11AcUploadFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11AcUploadFrameCnt.setStatus(_A)
_HpnicfDot11AcDownloadFrameCnt_Type=Counter64
_HpnicfDot11AcDownloadFrameCnt_Object=MibScalar
hpnicfDot11AcDownloadFrameCnt=_HpnicfDot11AcDownloadFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,2,9),_HpnicfDot11AcDownloadFrameCnt_Type())
hpnicfDot11AcDownloadFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11AcDownloadFrameCnt.setStatus(_A)
_HpnicfDot11AcUploadFrameBytes_Type=Counter64
_HpnicfDot11AcUploadFrameBytes_Object=MibScalar
hpnicfDot11AcUploadFrameBytes=_HpnicfDot11AcUploadFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,2,10),_HpnicfDot11AcUploadFrameBytes_Type())
hpnicfDot11AcUploadFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11AcUploadFrameBytes.setStatus(_A)
_HpnicfDot11AcDownloadFrameBytes_Type=Counter64
_HpnicfDot11AcDownloadFrameBytes_Object=MibScalar
hpnicfDot11AcDownloadFrameBytes=_HpnicfDot11AcDownloadFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,2,11),_HpnicfDot11AcDownloadFrameBytes_Type())
hpnicfDot11AcDownloadFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11AcDownloadFrameBytes.setStatus(_A)
class _HpnicfDot11BackupACRole_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('null',1),('master',2),('slave',3)))
_HpnicfDot11BackupACRole_Type.__name__=_E
_HpnicfDot11BackupACRole_Object=MibScalar
hpnicfDot11BackupACRole=_HpnicfDot11BackupACRole_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,2,12),_HpnicfDot11BackupACRole_Type())
hpnicfDot11BackupACRole.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BackupACRole.setStatus(_A)
_HpnicfDot11BackupACNMSIP_Type=IpAddress
_HpnicfDot11BackupACNMSIP_Object=MibScalar
hpnicfDot11BackupACNMSIP=_HpnicfDot11BackupACNMSIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,2,13),_HpnicfDot11BackupACNMSIP_Type())
hpnicfDot11BackupACNMSIP.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BackupACNMSIP.setStatus(_A)
class _HpnicfDot11ACBackupMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('null',1),('hotBackup',2),('coldBackup',3)))
_HpnicfDot11ACBackupMode_Type.__name__=_E
_HpnicfDot11ACBackupMode_Object=MibScalar
hpnicfDot11ACBackupMode=_HpnicfDot11ACBackupMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,2,14),_HpnicfDot11ACBackupMode_Type())
hpnicfDot11ACBackupMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACBackupMode.setStatus(_A)
class _HpnicfDot11ACBackupStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('standby',2)))
_HpnicfDot11ACBackupStatus_Type.__name__=_E
_HpnicfDot11ACBackupStatus_Object=MibScalar
hpnicfDot11ACBackupStatus=_HpnicfDot11ACBackupStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,2,15),_HpnicfDot11ACBackupStatus_Type())
hpnicfDot11ACBackupStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACBackupStatus.setStatus(_A)
_HpnicfDot11ACSwitchCnt_Type=Integer32
_HpnicfDot11ACSwitchCnt_Object=MibScalar
hpnicfDot11ACSwitchCnt=_HpnicfDot11ACSwitchCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,2,16),_HpnicfDot11ACSwitchCnt_Type())
hpnicfDot11ACSwitchCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACSwitchCnt.setStatus(_A)
_HpnicfDot11ACSouthifPacketOutputCount_Type=Counter64
_HpnicfDot11ACSouthifPacketOutputCount_Object=MibScalar
hpnicfDot11ACSouthifPacketOutputCount=_HpnicfDot11ACSouthifPacketOutputCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,2,17),_HpnicfDot11ACSouthifPacketOutputCount_Type())
hpnicfDot11ACSouthifPacketOutputCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACSouthifPacketOutputCount.setStatus(_A)
_HpnicfDot11ACSouthifPacketOutputBytes_Type=Counter64
_HpnicfDot11ACSouthifPacketOutputBytes_Object=MibScalar
hpnicfDot11ACSouthifPacketOutputBytes=_HpnicfDot11ACSouthifPacketOutputBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,2,18),_HpnicfDot11ACSouthifPacketOutputBytes_Type())
hpnicfDot11ACSouthifPacketOutputBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACSouthifPacketOutputBytes.setStatus(_A)
_HpnicfDot11ACSouthifPacketInputCount_Type=Counter64
_HpnicfDot11ACSouthifPacketInputCount_Object=MibScalar
hpnicfDot11ACSouthifPacketInputCount=_HpnicfDot11ACSouthifPacketInputCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,2,19),_HpnicfDot11ACSouthifPacketInputCount_Type())
hpnicfDot11ACSouthifPacketInputCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACSouthifPacketInputCount.setStatus(_A)
_HpnicfDot11ACSouthifPacketInputBytes_Type=Counter64
_HpnicfDot11ACSouthifPacketInputBytes_Object=MibScalar
hpnicfDot11ACSouthifPacketInputBytes=_HpnicfDot11ACSouthifPacketInputBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,2,20),_HpnicfDot11ACSouthifPacketInputBytes_Type())
hpnicfDot11ACSouthifPacketInputBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACSouthifPacketInputBytes.setStatus(_A)
_HpnicfDot11TotalAPconnected_Type=Integer32
_HpnicfDot11TotalAPconnected_Object=MibScalar
hpnicfDot11TotalAPconnected=_HpnicfDot11TotalAPconnected_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,2,21),_HpnicfDot11TotalAPconnected_Type())
hpnicfDot11TotalAPconnected.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11TotalAPconnected.setStatus(_A)
_HpnicfDot11RemainingAPcapacity_Type=Integer32
_HpnicfDot11RemainingAPcapacity_Object=MibScalar
hpnicfDot11RemainingAPcapacity=_HpnicfDot11RemainingAPcapacity_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,2,22),_HpnicfDot11RemainingAPcapacity_Type())
hpnicfDot11RemainingAPcapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RemainingAPcapacity.setStatus(_A)
_HpnicfDot11WLANAssocStatisInfo_ObjectIdentity=ObjectIdentity
hpnicfDot11WLANAssocStatisInfo=_HpnicfDot11WLANAssocStatisInfo_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,3))
_HpnicfDot11StationAssocSum_Type=Counter32
_HpnicfDot11StationAssocSum_Object=MibScalar
hpnicfDot11StationAssocSum=_HpnicfDot11StationAssocSum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,3,1),_HpnicfDot11StationAssocSum_Type())
hpnicfDot11StationAssocSum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11StationAssocSum.setStatus(_A)
_HpnicfDot11StationAssocFailSum_Type=Counter32
_HpnicfDot11StationAssocFailSum_Object=MibScalar
hpnicfDot11StationAssocFailSum=_HpnicfDot11StationAssocFailSum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,3,2),_HpnicfDot11StationAssocFailSum_Type())
hpnicfDot11StationAssocFailSum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11StationAssocFailSum.setStatus(_A)
_HpnicfDot11StationReassocSum_Type=Counter32
_HpnicfDot11StationReassocSum_Object=MibScalar
hpnicfDot11StationReassocSum=_HpnicfDot11StationReassocSum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,3,3),_HpnicfDot11StationReassocSum_Type())
hpnicfDot11StationReassocSum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11StationReassocSum.setStatus(_A)
_HpnicfDot11StationAssocRejectedSum_Type=Counter32
_HpnicfDot11StationAssocRejectedSum_Object=MibScalar
hpnicfDot11StationAssocRejectedSum=_HpnicfDot11StationAssocRejectedSum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,3,4),_HpnicfDot11StationAssocRejectedSum_Type())
hpnicfDot11StationAssocRejectedSum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11StationAssocRejectedSum.setStatus(_A)
_HpnicfDot11StationExDeAuthenSum_Type=Counter32
_HpnicfDot11StationExDeAuthenSum_Object=MibScalar
hpnicfDot11StationExDeAuthenSum=_HpnicfDot11StationExDeAuthenSum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,3,5),_HpnicfDot11StationExDeAuthenSum_Type())
hpnicfDot11StationExDeAuthenSum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11StationExDeAuthenSum.setStatus(_A)
_HpnicfDot11StationCurAssocSum_Type=Integer32
_HpnicfDot11StationCurAssocSum_Object=MibScalar
hpnicfDot11StationCurAssocSum=_HpnicfDot11StationCurAssocSum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,3,6),_HpnicfDot11StationCurAssocSum_Type())
hpnicfDot11StationCurAssocSum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11StationCurAssocSum.setStatus(_A)
_HpnicfDot11StationAssocReqSum_Type=Counter32
_HpnicfDot11StationAssocReqSum_Object=MibScalar
hpnicfDot11StationAssocReqSum=_HpnicfDot11StationAssocReqSum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,3,7),_HpnicfDot11StationAssocReqSum_Type())
hpnicfDot11StationAssocReqSum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11StationAssocReqSum.setStatus(_A)
_HpnicfDot11StationReassocReqSum_Type=Counter32
_HpnicfDot11StationReassocReqSum_Object=MibScalar
hpnicfDot11StationReassocReqSum=_HpnicfDot11StationReassocReqSum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,3,8),_HpnicfDot11StationReassocReqSum_Type())
hpnicfDot11StationReassocReqSum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11StationReassocReqSum.setStatus(_A)
_HpnicfDot11StationReassocFailSum_Type=Counter32
_HpnicfDot11StationReassocFailSum_Object=MibScalar
hpnicfDot11StationReassocFailSum=_HpnicfDot11StationReassocFailSum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,3,9),_HpnicfDot11StationReassocFailSum_Type())
hpnicfDot11StationReassocFailSum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11StationReassocFailSum.setStatus(_A)
_HpnicfDot11ACBASInfo_ObjectIdentity=ObjectIdentity
hpnicfDot11ACBASInfo=_HpnicfDot11ACBASInfo_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,4))
_HpnicfDot11ACBASSysObjects_ObjectIdentity=ObjectIdentity
hpnicfDot11ACBASSysObjects=_HpnicfDot11ACBASSysObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,4,1))
_HpnicfDot11ACBASTableObjects_ObjectIdentity=ObjectIdentity
hpnicfDot11ACBASTableObjects=_HpnicfDot11ACBASTableObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,4,2))
_HpnicfDot11ACBASIfTable_Object=MibTable
hpnicfDot11ACBASIfTable=_HpnicfDot11ACBASIfTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,4,2,3))
if mibBuilder.loadTexts:hpnicfDot11ACBASIfTable.setStatus(_A)
_HpnicfDot11ACBASIfEntry_Object=MibTableRow
hpnicfDot11ACBASIfEntry=_HpnicfDot11ACBASIfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,4,2,3,1))
hpnicfDot11ACBASIfEntry.setIndexNames((0,_C,_R))
if mibBuilder.loadTexts:hpnicfDot11ACBASIfEntry.setStatus(_A)
_HpnicfDot11ACBASIfIndex_Type=Integer32
_HpnicfDot11ACBASIfIndex_Object=MibTableColumn
hpnicfDot11ACBASIfIndex=_HpnicfDot11ACBASIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,4,2,3,1,1),_HpnicfDot11ACBASIfIndex_Type())
hpnicfDot11ACBASIfIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:hpnicfDot11ACBASIfIndex.setStatus(_A)
class _HpnicfDot11ACBASIfDescr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfDot11ACBASIfDescr_Type.__name__=_H
_HpnicfDot11ACBASIfDescr_Object=MibTableColumn
hpnicfDot11ACBASIfDescr=_HpnicfDot11ACBASIfDescr_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,4,2,3,1,2),_HpnicfDot11ACBASIfDescr_Type())
hpnicfDot11ACBASIfDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACBASIfDescr.setStatus(_A)
_HpnicfDot11ACBASIfType_Type=IANAifType
_HpnicfDot11ACBASIfType_Object=MibTableColumn
hpnicfDot11ACBASIfType=_HpnicfDot11ACBASIfType_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,4,2,3,1,3),_HpnicfDot11ACBASIfType_Type())
hpnicfDot11ACBASIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACBASIfType.setStatus(_A)
_HpnicfDot11ACStaUserSecAuthStatis_ObjectIdentity=ObjectIdentity
hpnicfDot11ACStaUserSecAuthStatis=_HpnicfDot11ACStaUserSecAuthStatis_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,5))
_HpnicfDot11ACStaUserAuthCurNumber_Type=Integer32
_HpnicfDot11ACStaUserAuthCurNumber_Object=MibScalar
hpnicfDot11ACStaUserAuthCurNumber=_HpnicfDot11ACStaUserAuthCurNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,5,1),_HpnicfDot11ACStaUserAuthCurNumber_Type())
hpnicfDot11ACStaUserAuthCurNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACStaUserAuthCurNumber.setStatus(_A)
_HpnicfDot11ACStaUserConnFailCnt_Type=Counter32
_HpnicfDot11ACStaUserConnFailCnt_Object=MibScalar
hpnicfDot11ACStaUserConnFailCnt=_HpnicfDot11ACStaUserConnFailCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,5,2),_HpnicfDot11ACStaUserConnFailCnt_Type())
hpnicfDot11ACStaUserConnFailCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACStaUserConnFailCnt.setStatus(_A)
_HpnicfDot11ACStaUserAuthReqCnt_Type=Counter32
_HpnicfDot11ACStaUserAuthReqCnt_Object=MibScalar
hpnicfDot11ACStaUserAuthReqCnt=_HpnicfDot11ACStaUserAuthReqCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,5,3),_HpnicfDot11ACStaUserAuthReqCnt_Type())
hpnicfDot11ACStaUserAuthReqCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACStaUserAuthReqCnt.setStatus(_A)
_HpnicfDot11ACStaUserAuthSuccCnt_Type=Counter32
_HpnicfDot11ACStaUserAuthSuccCnt_Object=MibScalar
hpnicfDot11ACStaUserAuthSuccCnt=_HpnicfDot11ACStaUserAuthSuccCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,5,4),_HpnicfDot11ACStaUserAuthSuccCnt_Type())
hpnicfDot11ACStaUserAuthSuccCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACStaUserAuthSuccCnt.setStatus(_A)
_HpnicfDot11ACStaUserAuthFailCnt_Type=Counter32
_HpnicfDot11ACStaUserAuthFailCnt_Object=MibScalar
hpnicfDot11ACStaUserAuthFailCnt=_HpnicfDot11ACStaUserAuthFailCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,5,5),_HpnicfDot11ACStaUserAuthFailCnt_Type())
hpnicfDot11ACStaUserAuthFailCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACStaUserAuthFailCnt.setStatus(_A)
_HpnicfDot11ACStaUserAllAuthCntCM_Type=Counter32
_HpnicfDot11ACStaUserAllAuthCntCM_Object=MibScalar
hpnicfDot11ACStaUserAllAuthCntCM=_HpnicfDot11ACStaUserAllAuthCntCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,5,6),_HpnicfDot11ACStaUserAllAuthCntCM_Type())
hpnicfDot11ACStaUserAllAuthCntCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACStaUserAllAuthCntCM.setStatus(_A)
_HpnicfDot11ACStaSecAuthTypeStatis_ObjectIdentity=ObjectIdentity
hpnicfDot11ACStaSecAuthTypeStatis=_HpnicfDot11ACStaSecAuthTypeStatis_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,6))
_HpnicfDot11ACStaUserPortalOnlineNum_Type=Integer32
_HpnicfDot11ACStaUserPortalOnlineNum_Object=MibScalar
hpnicfDot11ACStaUserPortalOnlineNum=_HpnicfDot11ACStaUserPortalOnlineNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,6,1),_HpnicfDot11ACStaUserPortalOnlineNum_Type())
hpnicfDot11ACStaUserPortalOnlineNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACStaUserPortalOnlineNum.setStatus(_A)
_HpnicfDot11ACStaUserFreeAuthOnlineNum_Type=Integer32
_HpnicfDot11ACStaUserFreeAuthOnlineNum_Object=MibScalar
hpnicfDot11ACStaUserFreeAuthOnlineNum=_HpnicfDot11ACStaUserFreeAuthOnlineNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,6,2),_HpnicfDot11ACStaUserFreeAuthOnlineNum_Type())
hpnicfDot11ACStaUserFreeAuthOnlineNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACStaUserFreeAuthOnlineNum.setStatus(_A)
_HpnicfDot11ACStaUserAssociateAuthOnlineNum_Type=Integer32
_HpnicfDot11ACStaUserAssociateAuthOnlineNum_Object=MibScalar
hpnicfDot11ACStaUserAssociateAuthOnlineNum=_HpnicfDot11ACStaUserAssociateAuthOnlineNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,6,3),_HpnicfDot11ACStaUserAssociateAuthOnlineNum_Type())
hpnicfDot11ACStaUserAssociateAuthOnlineNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACStaUserAssociateAuthOnlineNum.setStatus(_A)
_HpnicfDot11ACStaUserMacAuthOnlineNum_Type=Integer32
_HpnicfDot11ACStaUserMacAuthOnlineNum_Object=MibScalar
hpnicfDot11ACStaUserMacAuthOnlineNum=_HpnicfDot11ACStaUserMacAuthOnlineNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,6,4),_HpnicfDot11ACStaUserMacAuthOnlineNum_Type())
hpnicfDot11ACStaUserMacAuthOnlineNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACStaUserMacAuthOnlineNum.setStatus(_A)
_HpnicfDot11ACStaUserPortalLostConnectionCnt_Type=Counter32
_HpnicfDot11ACStaUserPortalLostConnectionCnt_Object=MibScalar
hpnicfDot11ACStaUserPortalLostConnectionCnt=_HpnicfDot11ACStaUserPortalLostConnectionCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,6,5),_HpnicfDot11ACStaUserPortalLostConnectionCnt_Type())
hpnicfDot11ACStaUserPortalLostConnectionCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACStaUserPortalLostConnectionCnt.setStatus(_A)
_HpnicfDot11ACStaUserFreeAuthLostConnectionCnt_Type=Counter32
_HpnicfDot11ACStaUserFreeAuthLostConnectionCnt_Object=MibScalar
hpnicfDot11ACStaUserFreeAuthLostConnectionCnt=_HpnicfDot11ACStaUserFreeAuthLostConnectionCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,6,6),_HpnicfDot11ACStaUserFreeAuthLostConnectionCnt_Type())
hpnicfDot11ACStaUserFreeAuthLostConnectionCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACStaUserFreeAuthLostConnectionCnt.setStatus(_A)
_HpnicfDot11ACStaUserAssociateAuthLostConnectionCnt_Type=Counter32
_HpnicfDot11ACStaUserAssociateAuthLostConnectionCnt_Object=MibScalar
hpnicfDot11ACStaUserAssociateAuthLostConnectionCnt=_HpnicfDot11ACStaUserAssociateAuthLostConnectionCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,6,7),_HpnicfDot11ACStaUserAssociateAuthLostConnectionCnt_Type())
hpnicfDot11ACStaUserAssociateAuthLostConnectionCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACStaUserAssociateAuthLostConnectionCnt.setStatus(_A)
_HpnicfDot11ACStaUserMacAuthLostConnectionCnt_Type=Counter32
_HpnicfDot11ACStaUserMacAuthLostConnectionCnt_Object=MibScalar
hpnicfDot11ACStaUserMacAuthLostConnectionCnt=_HpnicfDot11ACStaUserMacAuthLostConnectionCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,6,8),_HpnicfDot11ACStaUserMacAuthLostConnectionCnt_Type())
hpnicfDot11ACStaUserMacAuthLostConnectionCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACStaUserMacAuthLostConnectionCnt.setStatus(_A)
_HpnicfDot11ACStaPortalAuthReqCnt_Type=Counter32
_HpnicfDot11ACStaPortalAuthReqCnt_Object=MibScalar
hpnicfDot11ACStaPortalAuthReqCnt=_HpnicfDot11ACStaPortalAuthReqCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,6,9),_HpnicfDot11ACStaPortalAuthReqCnt_Type())
hpnicfDot11ACStaPortalAuthReqCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACStaPortalAuthReqCnt.setStatus(_A)
_HpnicfDot11ACStaAssociateAuthReqCnt_Type=Counter32
_HpnicfDot11ACStaAssociateAuthReqCnt_Object=MibScalar
hpnicfDot11ACStaAssociateAuthReqCnt=_HpnicfDot11ACStaAssociateAuthReqCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,6,10),_HpnicfDot11ACStaAssociateAuthReqCnt_Type())
hpnicfDot11ACStaAssociateAuthReqCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACStaAssociateAuthReqCnt.setStatus(_A)
_HpnicfDot11ACStaMacAuthReqCnt_Type=Counter32
_HpnicfDot11ACStaMacAuthReqCnt_Object=MibScalar
hpnicfDot11ACStaMacAuthReqCnt=_HpnicfDot11ACStaMacAuthReqCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,6,11),_HpnicfDot11ACStaMacAuthReqCnt_Type())
hpnicfDot11ACStaMacAuthReqCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACStaMacAuthReqCnt.setStatus(_A)
_HpnicfDot11ACStaPortalAuthSuccCnt_Type=Counter32
_HpnicfDot11ACStaPortalAuthSuccCnt_Object=MibScalar
hpnicfDot11ACStaPortalAuthSuccCnt=_HpnicfDot11ACStaPortalAuthSuccCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,6,12),_HpnicfDot11ACStaPortalAuthSuccCnt_Type())
hpnicfDot11ACStaPortalAuthSuccCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACStaPortalAuthSuccCnt.setStatus(_A)
_HpnicfDot11ACStaAssociateAuthSuccCnt_Type=Counter32
_HpnicfDot11ACStaAssociateAuthSuccCnt_Object=MibScalar
hpnicfDot11ACStaAssociateAuthSuccCnt=_HpnicfDot11ACStaAssociateAuthSuccCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,6,13),_HpnicfDot11ACStaAssociateAuthSuccCnt_Type())
hpnicfDot11ACStaAssociateAuthSuccCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACStaAssociateAuthSuccCnt.setStatus(_A)
_HpnicfDot11ACStaMacAuthSuccCnt_Type=Counter32
_HpnicfDot11ACStaMacAuthSuccCnt_Object=MibScalar
hpnicfDot11ACStaMacAuthSuccCnt=_HpnicfDot11ACStaMacAuthSuccCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,6,14),_HpnicfDot11ACStaMacAuthSuccCnt_Type())
hpnicfDot11ACStaMacAuthSuccCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACStaMacAuthSuccCnt.setStatus(_A)
_HpnicfDot11ACStaPortalAuthReqFailCnt_Type=Counter32
_HpnicfDot11ACStaPortalAuthReqFailCnt_Object=MibScalar
hpnicfDot11ACStaPortalAuthReqFailCnt=_HpnicfDot11ACStaPortalAuthReqFailCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,6,15),_HpnicfDot11ACStaPortalAuthReqFailCnt_Type())
hpnicfDot11ACStaPortalAuthReqFailCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACStaPortalAuthReqFailCnt.setStatus(_A)
_HpnicfDot11ACStaAssociateAuthReqFailCnt_Type=Counter32
_HpnicfDot11ACStaAssociateAuthReqFailCnt_Object=MibScalar
hpnicfDot11ACStaAssociateAuthReqFailCnt=_HpnicfDot11ACStaAssociateAuthReqFailCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,6,16),_HpnicfDot11ACStaAssociateAuthReqFailCnt_Type())
hpnicfDot11ACStaAssociateAuthReqFailCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACStaAssociateAuthReqFailCnt.setStatus(_A)
_HpnicfDot11ACStaMacAuthReqFailCnt_Type=Counter32
_HpnicfDot11ACStaMacAuthReqFailCnt_Object=MibScalar
hpnicfDot11ACStaMacAuthReqFailCnt=_HpnicfDot11ACStaMacAuthReqFailCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,6,17),_HpnicfDot11ACStaMacAuthReqFailCnt_Type())
hpnicfDot11ACStaMacAuthReqFailCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACStaMacAuthReqFailCnt.setStatus(_A)
_HpnicfDot11ACStaUserAutoAuthOnlineNumCM_Type=Integer32
_HpnicfDot11ACStaUserAutoAuthOnlineNumCM_Object=MibScalar
hpnicfDot11ACStaUserAutoAuthOnlineNumCM=_HpnicfDot11ACStaUserAutoAuthOnlineNumCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,6,18),_HpnicfDot11ACStaUserAutoAuthOnlineNumCM_Type())
hpnicfDot11ACStaUserAutoAuthOnlineNumCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACStaUserAutoAuthOnlineNumCM.setStatus(_A)
_HpnicfDot11ACStaUserAutoAuthLostConnectionCntCM_Type=Counter32
_HpnicfDot11ACStaUserAutoAuthLostConnectionCntCM_Object=MibScalar
hpnicfDot11ACStaUserAutoAuthLostConnectionCntCM=_HpnicfDot11ACStaUserAutoAuthLostConnectionCntCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,6,19),_HpnicfDot11ACStaUserAutoAuthLostConnectionCntCM_Type())
hpnicfDot11ACStaUserAutoAuthLostConnectionCntCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACStaUserAutoAuthLostConnectionCntCM.setStatus(_A)
_HpnicfDot11ACStaAutoAuthReqCntCM_Type=Counter32
_HpnicfDot11ACStaAutoAuthReqCntCM_Object=MibScalar
hpnicfDot11ACStaAutoAuthReqCntCM=_HpnicfDot11ACStaAutoAuthReqCntCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,6,20),_HpnicfDot11ACStaAutoAuthReqCntCM_Type())
hpnicfDot11ACStaAutoAuthReqCntCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACStaAutoAuthReqCntCM.setStatus(_A)
_HpnicfDot11ACStaAutoAuthSuccCntCM_Type=Counter32
_HpnicfDot11ACStaAutoAuthSuccCntCM_Object=MibScalar
hpnicfDot11ACStaAutoAuthSuccCntCM=_HpnicfDot11ACStaAutoAuthSuccCntCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,6,21),_HpnicfDot11ACStaAutoAuthSuccCntCM_Type())
hpnicfDot11ACStaAutoAuthSuccCntCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACStaAutoAuthSuccCntCM.setStatus(_A)
_HpnicfDot11ACStaAutoAuthReqFailCntCM_Type=Counter32
_HpnicfDot11ACStaAutoAuthReqFailCntCM_Object=MibScalar
hpnicfDot11ACStaAutoAuthReqFailCntCM=_HpnicfDot11ACStaAutoAuthReqFailCntCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,6,22),_HpnicfDot11ACStaAutoAuthReqFailCntCM_Type())
hpnicfDot11ACStaAutoAuthReqFailCntCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACStaAutoAuthReqFailCntCM.setStatus(_A)
_HpnicfDot11ACPortalStatisticCMTable_Object=MibTable
hpnicfDot11ACPortalStatisticCMTable=_HpnicfDot11ACPortalStatisticCMTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,7))
if mibBuilder.loadTexts:hpnicfDot11ACPortalStatisticCMTable.setStatus(_A)
_HpnicfDot11ACPortalStatisticCMEntry_Object=MibTableRow
hpnicfDot11ACPortalStatisticCMEntry=_HpnicfDot11ACPortalStatisticCMEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,7,1))
hpnicfDot11ACPortalStatisticCMEntry.setIndexNames((0,_C,_T))
if mibBuilder.loadTexts:hpnicfDot11ACPortalStatisticCMEntry.setStatus(_A)
class _HpnicfDot11ACPortalStatisticSSIDCM_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpnicfDot11ACPortalStatisticSSIDCM_Type.__name__=_H
_HpnicfDot11ACPortalStatisticSSIDCM_Object=MibTableColumn
hpnicfDot11ACPortalStatisticSSIDCM=_HpnicfDot11ACPortalStatisticSSIDCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,7,1,1),_HpnicfDot11ACPortalStatisticSSIDCM_Type())
hpnicfDot11ACPortalStatisticSSIDCM.setMaxAccess(_S)
if mibBuilder.loadTexts:hpnicfDot11ACPortalStatisticSSIDCM.setStatus(_A)
_HpnicfDot11ACPortalStatAuthReqCM_Type=Counter32
_HpnicfDot11ACPortalStatAuthReqCM_Object=MibTableColumn
hpnicfDot11ACPortalStatAuthReqCM=_HpnicfDot11ACPortalStatAuthReqCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,7,1,2),_HpnicfDot11ACPortalStatAuthReqCM_Type())
hpnicfDot11ACPortalStatAuthReqCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACPortalStatAuthReqCM.setStatus(_A)
_HpnicfDot11ACPortalStatAuthRespCM_Type=Counter32
_HpnicfDot11ACPortalStatAuthRespCM_Object=MibTableColumn
hpnicfDot11ACPortalStatAuthRespCM=_HpnicfDot11ACPortalStatAuthRespCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,1,7,1,3),_HpnicfDot11ACPortalStatAuthRespCM_Type())
hpnicfDot11ACPortalStatAuthRespCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACPortalStatAuthRespCM.setStatus(_A)
_HpnicfDot11CAPWAPTunnelGroup_ObjectIdentity=ObjectIdentity
hpnicfDot11CAPWAPTunnelGroup=_HpnicfDot11CAPWAPTunnelGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,1,2))
_HpnicfDot11CAPWAPTunnelTable_Object=MibTable
hpnicfDot11CAPWAPTunnelTable=_HpnicfDot11CAPWAPTunnelTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,2,1))
if mibBuilder.loadTexts:hpnicfDot11CAPWAPTunnelTable.setStatus(_A)
_HpnicfDot11CAPWAPTunnelEntry_Object=MibTableRow
hpnicfDot11CAPWAPTunnelEntry=_HpnicfDot11CAPWAPTunnelEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,2,1,1))
hpnicfDot11CAPWAPTunnelEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:hpnicfDot11CAPWAPTunnelEntry.setStatus(_A)
_HpnicfDot11CurrTunnelAPID_Type=HpnicfDot11ObjectIDType
_HpnicfDot11CurrTunnelAPID_Object=MibTableColumn
hpnicfDot11CurrTunnelAPID=_HpnicfDot11CurrTunnelAPID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,2,1,1,1),_HpnicfDot11CurrTunnelAPID_Type())
hpnicfDot11CurrTunnelAPID.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11CurrTunnelAPID.setStatus(_A)
class _HpnicfDot11CtrlTunnelCurrSec_Type(HpnicfDot11TunnelSecSchemType):defaultValue=1
_HpnicfDot11CtrlTunnelCurrSec_Type.__name__=_I
_HpnicfDot11CtrlTunnelCurrSec_Object=MibTableColumn
hpnicfDot11CtrlTunnelCurrSec=_HpnicfDot11CtrlTunnelCurrSec_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,2,1,1,2),_HpnicfDot11CtrlTunnelCurrSec_Type())
hpnicfDot11CtrlTunnelCurrSec.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CtrlTunnelCurrSec.setStatus(_A)
_HpnicfDot11CtrlTunnelUpTime_Type=Integer32
_HpnicfDot11CtrlTunnelUpTime_Object=MibTableColumn
hpnicfDot11CtrlTunnelUpTime=_HpnicfDot11CtrlTunnelUpTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,2,1,1,3),_HpnicfDot11CtrlTunnelUpTime_Type())
hpnicfDot11CtrlTunnelUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CtrlTunnelUpTime.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11CtrlTunnelUpTime.setUnits(_U)
class _HpnicfDot11DataTunnelCurrSec_Type(HpnicfDot11TunnelSecSchemType):defaultValue=1
_HpnicfDot11DataTunnelCurrSec_Type.__name__=_I
_HpnicfDot11DataTunnelCurrSec_Object=MibTableColumn
hpnicfDot11DataTunnelCurrSec=_HpnicfDot11DataTunnelCurrSec_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,2,1,1,4),_HpnicfDot11DataTunnelCurrSec_Type())
hpnicfDot11DataTunnelCurrSec.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11DataTunnelCurrSec.setStatus(_A)
_HpnicfDot11DataTunnelUpTime_Type=Integer32
_HpnicfDot11DataTunnelUpTime_Object=MibTableColumn
hpnicfDot11DataTunnelUpTime=_HpnicfDot11DataTunnelUpTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,2,1,1,5),_HpnicfDot11DataTunnelUpTime_Type())
hpnicfDot11DataTunnelUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11DataTunnelUpTime.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11DataTunnelUpTime.setUnits(_U)
_HpnicfDot11CtrlTunnelUpTimeTicks_Type=TimeTicks
_HpnicfDot11CtrlTunnelUpTimeTicks_Object=MibTableColumn
hpnicfDot11CtrlTunnelUpTimeTicks=_HpnicfDot11CtrlTunnelUpTimeTicks_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,2,1,1,6),_HpnicfDot11CtrlTunnelUpTimeTicks_Type())
hpnicfDot11CtrlTunnelUpTimeTicks.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CtrlTunnelUpTimeTicks.setStatus(_A)
_HpnicfDot11ACMtNotifyGroup_ObjectIdentity=ObjectIdentity
hpnicfDot11ACMtNotifyGroup=_HpnicfDot11ACMtNotifyGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,1,3))
_HpnicfDot11ACMtTraps_ObjectIdentity=ObjectIdentity
hpnicfDot11ACMtTraps=_HpnicfDot11ACMtTraps_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,1,3,0))
_HpnicfDot11ACMtTrapVarObjects_ObjectIdentity=ObjectIdentity
hpnicfDot11ACMtTrapVarObjects=_HpnicfDot11ACMtTrapVarObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,1,3,1))
class _HpnicfDot11ACMtTrapTunlDwnInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('tunnelTimeout',1),('keyUpdateFailure',2),('apReset',3),('apCrash',4),('apDeleted',5),('apCfgChange',6)))
_HpnicfDot11ACMtTrapTunlDwnInfo_Type.__name__=_E
_HpnicfDot11ACMtTrapTunlDwnInfo_Object=MibScalar
hpnicfDot11ACMtTrapTunlDwnInfo=_HpnicfDot11ACMtTrapTunlDwnInfo_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,3,1,1),_HpnicfDot11ACMtTrapTunlDwnInfo_Type())
hpnicfDot11ACMtTrapTunlDwnInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11ACMtTrapTunlDwnInfo.setStatus(_A)
class _HpnicfDot11ACMtTrapTunlUpInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('up',1))
_HpnicfDot11ACMtTrapTunlUpInfo_Type.__name__=_E
_HpnicfDot11ACMtTrapTunlUpInfo_Object=MibScalar
hpnicfDot11ACMtTrapTunlUpInfo=_HpnicfDot11ACMtTrapTunlUpInfo_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,3,1,2),_HpnicfDot11ACMtTrapTunlUpInfo_Type())
hpnicfDot11ACMtTrapTunlUpInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11ACMtTrapTunlUpInfo.setStatus(_A)
class _HpnicfDot11ACMtTrapBackupSwitchInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('masterToSlave',1),('slaveToMaster',2)))
_HpnicfDot11ACMtTrapBackupSwitchInfo_Type.__name__=_E
_HpnicfDot11ACMtTrapBackupSwitchInfo_Object=MibScalar
hpnicfDot11ACMtTrapBackupSwitchInfo=_HpnicfDot11ACMtTrapBackupSwitchInfo_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,3,1,3),_HpnicfDot11ACMtTrapBackupSwitchInfo_Type())
hpnicfDot11ACMtTrapBackupSwitchInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11ACMtTrapBackupSwitchInfo.setStatus(_A)
_HpnicfDot11ACMtTrapTnlAPName_Type=OctetString
_HpnicfDot11ACMtTrapTnlAPName_Object=MibScalar
hpnicfDot11ACMtTrapTnlAPName=_HpnicfDot11ACMtTrapTnlAPName_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,3,1,4),_HpnicfDot11ACMtTrapTnlAPName_Type())
hpnicfDot11ACMtTrapTnlAPName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11ACMtTrapTnlAPName.setStatus(_A)
_HpnicfDot11ACMtTrapTnlAPIPAddr_Type=IpAddress
_HpnicfDot11ACMtTrapTnlAPIPAddr_Object=MibScalar
hpnicfDot11ACMtTrapTnlAPIPAddr=_HpnicfDot11ACMtTrapTnlAPIPAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,3,1,5),_HpnicfDot11ACMtTrapTnlAPIPAddr_Type())
hpnicfDot11ACMtTrapTnlAPIPAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11ACMtTrapTnlAPIPAddr.setStatus(_A)
class _HpnicfDot11LoadBalanceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('traffic',1),('session',2)))
_HpnicfDot11LoadBalanceType_Type.__name__=_E
_HpnicfDot11LoadBalanceType_Object=MibScalar
hpnicfDot11LoadBalanceType=_HpnicfDot11LoadBalanceType_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,3,1,6),_HpnicfDot11LoadBalanceType_Type())
hpnicfDot11LoadBalanceType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11LoadBalanceType.setStatus(_A)
_HpnicfDot11LoadBalanceThreshold_Type=Integer32
_HpnicfDot11LoadBalanceThreshold_Object=MibScalar
hpnicfDot11LoadBalanceThreshold=_HpnicfDot11LoadBalanceThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,3,1,7),_HpnicfDot11LoadBalanceThreshold_Type())
hpnicfDot11LoadBalanceThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11LoadBalanceThreshold.setStatus(_A)
_HpnicfDot11ACMtTrapAPIPv6Addr_Type=OctetString
_HpnicfDot11ACMtTrapAPIPv6Addr_Object=MibScalar
hpnicfDot11ACMtTrapAPIPv6Addr=_HpnicfDot11ACMtTrapAPIPv6Addr_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,3,1,8),_HpnicfDot11ACMtTrapAPIPv6Addr_Type())
hpnicfDot11ACMtTrapAPIPv6Addr.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11ACMtTrapAPIPv6Addr.setStatus(_A)
_HpnicfDot11ACMtTrapTunlDwnCount_Type=Integer32
_HpnicfDot11ACMtTrapTunlDwnCount_Object=MibScalar
hpnicfDot11ACMtTrapTunlDwnCount=_HpnicfDot11ACMtTrapTunlDwnCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,3,1,9),_HpnicfDot11ACMtTrapTunlDwnCount_Type())
hpnicfDot11ACMtTrapTunlDwnCount.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11ACMtTrapTunlDwnCount.setStatus(_A)
_HpnicfDot11ACMaxStaNum_Type=Integer32
_HpnicfDot11ACMaxStaNum_Object=MibScalar
hpnicfDot11ACMaxStaNum=_HpnicfDot11ACMaxStaNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,3,1,10),_HpnicfDot11ACMaxStaNum_Type())
hpnicfDot11ACMaxStaNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11ACMaxStaNum.setStatus(_A)
_HpnicfDot11ACMtTrapTnlAPSysName_Type=OctetString
_HpnicfDot11ACMtTrapTnlAPSysName_Object=MibScalar
hpnicfDot11ACMtTrapTnlAPSysName=_HpnicfDot11ACMtTrapTnlAPSysName_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,3,1,11),_HpnicfDot11ACMtTrapTnlAPSysName_Type())
hpnicfDot11ACMtTrapTnlAPSysName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11ACMtTrapTnlAPSysName.setStatus(_A)
_HpnicfDot11ACMtFirstTrapTime_Type=TimeTicks
_HpnicfDot11ACMtFirstTrapTime_Object=MibScalar
hpnicfDot11ACMtFirstTrapTime=_HpnicfDot11ACMtFirstTrapTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,3,1,12),_HpnicfDot11ACMtFirstTrapTime_Type())
hpnicfDot11ACMtFirstTrapTime.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11ACMtFirstTrapTime.setStatus(_A)
class _HpnicfDot11ACStatusSwitchInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('activeToStandby',1),('standbyToActive',2)))
_HpnicfDot11ACStatusSwitchInfo_Type.__name__=_E
_HpnicfDot11ACStatusSwitchInfo_Object=MibScalar
hpnicfDot11ACStatusSwitchInfo=_HpnicfDot11ACStatusSwitchInfo_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,3,1,13),_HpnicfDot11ACStatusSwitchInfo_Type())
hpnicfDot11ACStatusSwitchInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11ACStatusSwitchInfo.setStatus(_A)
_HpnicfDot11SourceACNmsIP_Type=IpAddress
_HpnicfDot11SourceACNmsIP_Object=MibScalar
hpnicfDot11SourceACNmsIP=_HpnicfDot11SourceACNmsIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,3,1,14),_HpnicfDot11SourceACNmsIP_Type())
hpnicfDot11SourceACNmsIP.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11SourceACNmsIP.setStatus(_A)
_HpnicfDot11ACMtTrapAPMacAddress_Type=MacAddress
_HpnicfDot11ACMtTrapAPMacAddress_Object=MibScalar
hpnicfDot11ACMtTrapAPMacAddress=_HpnicfDot11ACMtTrapAPMacAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,1,3,1,15),_HpnicfDot11ACMtTrapAPMacAddress_Type())
hpnicfDot11ACMtTrapAPMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11ACMtTrapAPMacAddress.setStatus(_A)
hpnicfDot11ACMtTunnelSetupTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,1,3,0,1))
hpnicfDot11ACMtTunnelSetupTrap.setObjects(*((_C,_F),(_C,_V),(_C,_J),(_C,_K),(_C,_L),(_C,_G),(_C,_M)))
if mibBuilder.loadTexts:hpnicfDot11ACMtTunnelSetupTrap.setStatus(_A)
hpnicfDot11ACMtTunnelDownTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,1,3,0,2))
hpnicfDot11ACMtTunnelDownTrap.setObjects(*((_C,_F),(_C,_W),(_C,_J),(_C,_K),(_C,_L),(_C,_X),(_C,_Y),(_C,_G),(_C,_M)))
if mibBuilder.loadTexts:hpnicfDot11ACMtTunnelDownTrap.setStatus(_A)
hpnicfDot11ACMtBackupSwtTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,1,3,0,3))
hpnicfDot11ACMtBackupSwtTrap.setObjects(*((_C,_Z),(_C,_G)))
if mibBuilder.loadTexts:hpnicfDot11ACMtBackupSwtTrap.setStatus(_A)
hpnicfDot11ACLoadBalanceTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,1,3,0,4))
hpnicfDot11ACLoadBalanceTrap.setObjects(*((_C,_a),(_C,_b)))
if mibBuilder.loadTexts:hpnicfDot11ACLoadBalanceTrap.setStatus(_A)
hpnicfDot11ACStaFullTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,1,3,0,5))
hpnicfDot11ACStaFullTrap.setObjects((_C,_c))
if mibBuilder.loadTexts:hpnicfDot11ACStaFullTrap.setStatus(_A)
hpnicfDot11ACStatusSwitchTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,1,3,0,6))
hpnicfDot11ACStatusSwitchTrap.setObjects(*((_C,_d),(_C,_e)))
if mibBuilder.loadTexts:hpnicfDot11ACStatusSwitchTrap.setStatus(_A)
hpnicfDot11RunAPNumOverload=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,1,3,0,7))
hpnicfDot11RunAPNumOverload.setObjects(*((_C,_N),(_C,_O)))
if mibBuilder.loadTexts:hpnicfDot11RunAPNumOverload.setStatus(_A)
hpnicfDot11RunAPNumOverloadRecover=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,1,3,0,8))
hpnicfDot11RunAPNumOverloadRecover.setObjects(*((_C,_N),(_C,_O)))
if mibBuilder.loadTexts:hpnicfDot11RunAPNumOverloadRecover.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'hpnicfDot11ACMT':hpnicfDot11ACMT,'hpnicfDot11ACObjectGroup':hpnicfDot11ACObjectGroup,'hpnicfDot11ACObject':hpnicfDot11ACObject,'hpnicfDot11CurrentACMACMode':hpnicfDot11CurrentACMACMode,_N:hpnicfDot11MaxAPNumPermitted,'hpnicfDot11MaxStationNumPermitted':hpnicfDot11MaxStationNumPermitted,'hpnicfDot11RunAPNumThreshold':hpnicfDot11RunAPNumThreshold,'hpnicfDot11ACLoadInfo':hpnicfDot11ACLoadInfo,_O:hpnicfDot11APConnectCount,'hpnicfDot11StationConnectCount':hpnicfDot11StationConnectCount,'hpnicfDot11ACIFLoadInfoTable':hpnicfDot11ACIFLoadInfoTable,'hpnicfDot11ACIFLoadInfoEntry':hpnicfDot11ACIFLoadInfoEntry,_Q:hpnicfDot11ACIfIndex,'hpnicfDot11ACIfApNum':hpnicfDot11ACIfApNum,'hpnicfDot11ACIfStaNum':hpnicfDot11ACIfStaNum,'hpnicfDot11ACIfName':hpnicfDot11ACIfName,'hpnicfDot11MasterAPCount':hpnicfDot11MasterAPCount,'hpnicfDot11SlaveAPCount':hpnicfDot11SlaveAPCount,'hpnicfDot11ConnectAutoAPCount':hpnicfDot11ConnectAutoAPCount,'hpnicfDot11PersistentAPCount':hpnicfDot11PersistentAPCount,'hpnicfDot11AcUploadFrameCnt':hpnicfDot11AcUploadFrameCnt,'hpnicfDot11AcDownloadFrameCnt':hpnicfDot11AcDownloadFrameCnt,'hpnicfDot11AcUploadFrameBytes':hpnicfDot11AcUploadFrameBytes,'hpnicfDot11AcDownloadFrameBytes':hpnicfDot11AcDownloadFrameBytes,'hpnicfDot11BackupACRole':hpnicfDot11BackupACRole,'hpnicfDot11BackupACNMSIP':hpnicfDot11BackupACNMSIP,'hpnicfDot11ACBackupMode':hpnicfDot11ACBackupMode,'hpnicfDot11ACBackupStatus':hpnicfDot11ACBackupStatus,'hpnicfDot11ACSwitchCnt':hpnicfDot11ACSwitchCnt,'hpnicfDot11ACSouthifPacketOutputCount':hpnicfDot11ACSouthifPacketOutputCount,'hpnicfDot11ACSouthifPacketOutputBytes':hpnicfDot11ACSouthifPacketOutputBytes,'hpnicfDot11ACSouthifPacketInputCount':hpnicfDot11ACSouthifPacketInputCount,'hpnicfDot11ACSouthifPacketInputBytes':hpnicfDot11ACSouthifPacketInputBytes,'hpnicfDot11TotalAPconnected':hpnicfDot11TotalAPconnected,'hpnicfDot11RemainingAPcapacity':hpnicfDot11RemainingAPcapacity,'hpnicfDot11WLANAssocStatisInfo':hpnicfDot11WLANAssocStatisInfo,'hpnicfDot11StationAssocSum':hpnicfDot11StationAssocSum,'hpnicfDot11StationAssocFailSum':hpnicfDot11StationAssocFailSum,'hpnicfDot11StationReassocSum':hpnicfDot11StationReassocSum,'hpnicfDot11StationAssocRejectedSum':hpnicfDot11StationAssocRejectedSum,'hpnicfDot11StationExDeAuthenSum':hpnicfDot11StationExDeAuthenSum,'hpnicfDot11StationCurAssocSum':hpnicfDot11StationCurAssocSum,'hpnicfDot11StationAssocReqSum':hpnicfDot11StationAssocReqSum,'hpnicfDot11StationReassocReqSum':hpnicfDot11StationReassocReqSum,'hpnicfDot11StationReassocFailSum':hpnicfDot11StationReassocFailSum,'hpnicfDot11ACBASInfo':hpnicfDot11ACBASInfo,'hpnicfDot11ACBASSysObjects':hpnicfDot11ACBASSysObjects,'hpnicfDot11ACBASTableObjects':hpnicfDot11ACBASTableObjects,'hpnicfDot11ACBASIfTable':hpnicfDot11ACBASIfTable,'hpnicfDot11ACBASIfEntry':hpnicfDot11ACBASIfEntry,_R:hpnicfDot11ACBASIfIndex,'hpnicfDot11ACBASIfDescr':hpnicfDot11ACBASIfDescr,'hpnicfDot11ACBASIfType':hpnicfDot11ACBASIfType,'hpnicfDot11ACStaUserSecAuthStatis':hpnicfDot11ACStaUserSecAuthStatis,'hpnicfDot11ACStaUserAuthCurNumber':hpnicfDot11ACStaUserAuthCurNumber,'hpnicfDot11ACStaUserConnFailCnt':hpnicfDot11ACStaUserConnFailCnt,'hpnicfDot11ACStaUserAuthReqCnt':hpnicfDot11ACStaUserAuthReqCnt,'hpnicfDot11ACStaUserAuthSuccCnt':hpnicfDot11ACStaUserAuthSuccCnt,'hpnicfDot11ACStaUserAuthFailCnt':hpnicfDot11ACStaUserAuthFailCnt,'hpnicfDot11ACStaUserAllAuthCntCM':hpnicfDot11ACStaUserAllAuthCntCM,'hpnicfDot11ACStaSecAuthTypeStatis':hpnicfDot11ACStaSecAuthTypeStatis,'hpnicfDot11ACStaUserPortalOnlineNum':hpnicfDot11ACStaUserPortalOnlineNum,'hpnicfDot11ACStaUserFreeAuthOnlineNum':hpnicfDot11ACStaUserFreeAuthOnlineNum,'hpnicfDot11ACStaUserAssociateAuthOnlineNum':hpnicfDot11ACStaUserAssociateAuthOnlineNum,'hpnicfDot11ACStaUserMacAuthOnlineNum':hpnicfDot11ACStaUserMacAuthOnlineNum,'hpnicfDot11ACStaUserPortalLostConnectionCnt':hpnicfDot11ACStaUserPortalLostConnectionCnt,'hpnicfDot11ACStaUserFreeAuthLostConnectionCnt':hpnicfDot11ACStaUserFreeAuthLostConnectionCnt,'hpnicfDot11ACStaUserAssociateAuthLostConnectionCnt':hpnicfDot11ACStaUserAssociateAuthLostConnectionCnt,'hpnicfDot11ACStaUserMacAuthLostConnectionCnt':hpnicfDot11ACStaUserMacAuthLostConnectionCnt,'hpnicfDot11ACStaPortalAuthReqCnt':hpnicfDot11ACStaPortalAuthReqCnt,'hpnicfDot11ACStaAssociateAuthReqCnt':hpnicfDot11ACStaAssociateAuthReqCnt,'hpnicfDot11ACStaMacAuthReqCnt':hpnicfDot11ACStaMacAuthReqCnt,'hpnicfDot11ACStaPortalAuthSuccCnt':hpnicfDot11ACStaPortalAuthSuccCnt,'hpnicfDot11ACStaAssociateAuthSuccCnt':hpnicfDot11ACStaAssociateAuthSuccCnt,'hpnicfDot11ACStaMacAuthSuccCnt':hpnicfDot11ACStaMacAuthSuccCnt,'hpnicfDot11ACStaPortalAuthReqFailCnt':hpnicfDot11ACStaPortalAuthReqFailCnt,'hpnicfDot11ACStaAssociateAuthReqFailCnt':hpnicfDot11ACStaAssociateAuthReqFailCnt,'hpnicfDot11ACStaMacAuthReqFailCnt':hpnicfDot11ACStaMacAuthReqFailCnt,'hpnicfDot11ACStaUserAutoAuthOnlineNumCM':hpnicfDot11ACStaUserAutoAuthOnlineNumCM,'hpnicfDot11ACStaUserAutoAuthLostConnectionCntCM':hpnicfDot11ACStaUserAutoAuthLostConnectionCntCM,'hpnicfDot11ACStaAutoAuthReqCntCM':hpnicfDot11ACStaAutoAuthReqCntCM,'hpnicfDot11ACStaAutoAuthSuccCntCM':hpnicfDot11ACStaAutoAuthSuccCntCM,'hpnicfDot11ACStaAutoAuthReqFailCntCM':hpnicfDot11ACStaAutoAuthReqFailCntCM,'hpnicfDot11ACPortalStatisticCMTable':hpnicfDot11ACPortalStatisticCMTable,'hpnicfDot11ACPortalStatisticCMEntry':hpnicfDot11ACPortalStatisticCMEntry,_T:hpnicfDot11ACPortalStatisticSSIDCM,'hpnicfDot11ACPortalStatAuthReqCM':hpnicfDot11ACPortalStatAuthReqCM,'hpnicfDot11ACPortalStatAuthRespCM':hpnicfDot11ACPortalStatAuthRespCM,'hpnicfDot11CAPWAPTunnelGroup':hpnicfDot11CAPWAPTunnelGroup,'hpnicfDot11CAPWAPTunnelTable':hpnicfDot11CAPWAPTunnelTable,'hpnicfDot11CAPWAPTunnelEntry':hpnicfDot11CAPWAPTunnelEntry,_F:hpnicfDot11CurrTunnelAPID,'hpnicfDot11CtrlTunnelCurrSec':hpnicfDot11CtrlTunnelCurrSec,'hpnicfDot11CtrlTunnelUpTime':hpnicfDot11CtrlTunnelUpTime,'hpnicfDot11DataTunnelCurrSec':hpnicfDot11DataTunnelCurrSec,'hpnicfDot11DataTunnelUpTime':hpnicfDot11DataTunnelUpTime,'hpnicfDot11CtrlTunnelUpTimeTicks':hpnicfDot11CtrlTunnelUpTimeTicks,'hpnicfDot11ACMtNotifyGroup':hpnicfDot11ACMtNotifyGroup,'hpnicfDot11ACMtTraps':hpnicfDot11ACMtTraps,'hpnicfDot11ACMtTunnelSetupTrap':hpnicfDot11ACMtTunnelSetupTrap,'hpnicfDot11ACMtTunnelDownTrap':hpnicfDot11ACMtTunnelDownTrap,'hpnicfDot11ACMtBackupSwtTrap':hpnicfDot11ACMtBackupSwtTrap,'hpnicfDot11ACLoadBalanceTrap':hpnicfDot11ACLoadBalanceTrap,'hpnicfDot11ACStaFullTrap':hpnicfDot11ACStaFullTrap,'hpnicfDot11ACStatusSwitchTrap':hpnicfDot11ACStatusSwitchTrap,'hpnicfDot11RunAPNumOverload':hpnicfDot11RunAPNumOverload,'hpnicfDot11RunAPNumOverloadRecover':hpnicfDot11RunAPNumOverloadRecover,'hpnicfDot11ACMtTrapVarObjects':hpnicfDot11ACMtTrapVarObjects,_W:hpnicfDot11ACMtTrapTunlDwnInfo,_V:hpnicfDot11ACMtTrapTunlUpInfo,_Z:hpnicfDot11ACMtTrapBackupSwitchInfo,_J:hpnicfDot11ACMtTrapTnlAPName,_K:hpnicfDot11ACMtTrapTnlAPIPAddr,_a:hpnicfDot11LoadBalanceType,_b:hpnicfDot11LoadBalanceThreshold,_L:hpnicfDot11ACMtTrapAPIPv6Addr,_X:hpnicfDot11ACMtTrapTunlDwnCount,_c:hpnicfDot11ACMaxStaNum,_Y:hpnicfDot11ACMtTrapTnlAPSysName,_G:hpnicfDot11ACMtFirstTrapTime,_d:hpnicfDot11ACStatusSwitchInfo,_e:hpnicfDot11SourceACNmsIP,_M:hpnicfDot11ACMtTrapAPMacAddress})