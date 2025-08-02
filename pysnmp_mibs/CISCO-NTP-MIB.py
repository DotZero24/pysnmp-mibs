_AH='ciscoNtpSrvNotifGroup'
_AG='ciscoNtpSysExtGroup'
_AF='ciscoNtpPeersGroup'
_AE='ciscoNtpGeneralConnRestore'
_AD='ciscoNtpGeneralConnFailure'
_AC='ciscoNtpHighPriorityConnRestore'
_AB='ciscoNtpHighPriorityConnFailure'
_AA='ciscoNtpSrvStatusChange'
_A9='cntpPeersPeerType'
_A8='cntpPeersPeerName'
_A7='cntpPeersPrefPeer'
_A6='cntpFilterPeersDispersion'
_A5='cntpFilterPeersDelay'
_A4='cntpFilterPeersOffset'
_A3='cntpPeersUpdateTime'
_A2='cntpSysClock'
_A1='cntpSysPeer'
_A0='cntpSysPoll'
_z='cntpSysRefTime'
_y='cntpSysRefId'
_x='cntpSysRootDispersion'
_w='cntpSysRootDelay'
_v='cntpSysPrecision'
_u='cntpSysStratum'
_t='cntpSysLeap'
_s='cntpFilterIndex'
_r='not-accessible'
_q='read-write'
_p='TruthValue'
_o='InetAddressType'
_n='ciscoNtpPeersGroupRev2'
_m='ciscoNtpPeersGroupRev1'
_l='cntpSysSrvStatus'
_k='cntpPeersUpdateTimeRev1'
_j='cntpPeersAssocId'
_i='ciscoNtpPeerExtGroup'
_h='cntpPeersEntryStatus'
_g='cntpPeersFilterValidEntries'
_f='cntpPeersDispersion'
_e='cntpPeersDelay'
_d='cntpPeersOffset'
_c='cntpPeersTimer'
_b='cntpPeersReach'
_a='cntpPeersTransmitTime'
_Z='cntpPeersReceiveTime'
_Y='cntpPeersOrgTime'
_X='cntpPeersRefTime'
_W='cntpPeersRefId'
_V='cntpPeersRootDispersion'
_U='cntpPeersRootDelay'
_T='cntpPeersPrecision'
_S='cntpPeersHostPoll'
_R='cntpPeersPeerPoll'
_Q='cntpPeersStratum'
_P='cntpPeersMode'
_O='cntpPeersLeap'
_N='cntpPeersHostPort'
_M='cntpPeersHostAddress'
_L='cntpPeersPeerPort'
_K='cntpPeersConfigured'
_J='ciscoNtpFilterGroup'
_I='ciscoNtpSysGroup'
_H='cntpPeersPeerAddress'
_G='deprecated'
_F='read-create'
_E='seconds'
_D='Integer32'
_C='read-only'
_B='current'
_A='CISCO-NTP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_o)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_p)
ciscoNtpMIB=ModuleIdentity((1,3,6,1,4,1,9,9,168))
if mibBuilder.loadTexts:ciscoNtpMIB.setRevisions(('2006-07-31 00:00','2004-07-23 00:00','2003-07-29 00:00','2003-07-07 00:00','2002-02-20 00:00','2000-06-16 00:00'))
class NTPTimeStamp(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class NTPLeapIndicator(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('noWarning',0),('addSecond',1),('subtractSecond',2),('alarm',3)))
class NTPSignedTimeValue(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class NTPUnsignedTimeValue(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class NTPStratum(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class NTPRefId(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class NTPPollInterval(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-20,20))
class NTPAssocIdentifier(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CiscoNtpMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoNtpMIBNotifs=_CiscoNtpMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,168,0))
_CiscoNtpMIBObjects_ObjectIdentity=ObjectIdentity
ciscoNtpMIBObjects=_CiscoNtpMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,168,1))
_CntpSystem_ObjectIdentity=ObjectIdentity
cntpSystem=_CntpSystem_ObjectIdentity((1,3,6,1,4,1,9,9,168,1,1))
_CntpSysLeap_Type=NTPLeapIndicator
_CntpSysLeap_Object=MibScalar
cntpSysLeap=_CntpSysLeap_Object((1,3,6,1,4,1,9,9,168,1,1,1),_CntpSysLeap_Type())
cntpSysLeap.setMaxAccess(_q)
if mibBuilder.loadTexts:cntpSysLeap.setStatus(_B)
_CntpSysStratum_Type=NTPStratum
_CntpSysStratum_Object=MibScalar
cntpSysStratum=_CntpSysStratum_Object((1,3,6,1,4,1,9,9,168,1,1,2),_CntpSysStratum_Type())
cntpSysStratum.setMaxAccess(_q)
if mibBuilder.loadTexts:cntpSysStratum.setStatus(_B)
class _CntpSysPrecision_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-20,20))
_CntpSysPrecision_Type.__name__=_D
_CntpSysPrecision_Object=MibScalar
cntpSysPrecision=_CntpSysPrecision_Object((1,3,6,1,4,1,9,9,168,1,1,3),_CntpSysPrecision_Type())
cntpSysPrecision.setMaxAccess(_C)
if mibBuilder.loadTexts:cntpSysPrecision.setStatus(_B)
_CntpSysRootDelay_Type=NTPSignedTimeValue
_CntpSysRootDelay_Object=MibScalar
cntpSysRootDelay=_CntpSysRootDelay_Object((1,3,6,1,4,1,9,9,168,1,1,4),_CntpSysRootDelay_Type())
cntpSysRootDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:cntpSysRootDelay.setStatus(_B)
if mibBuilder.loadTexts:cntpSysRootDelay.setUnits(_E)
_CntpSysRootDispersion_Type=NTPUnsignedTimeValue
_CntpSysRootDispersion_Object=MibScalar
cntpSysRootDispersion=_CntpSysRootDispersion_Object((1,3,6,1,4,1,9,9,168,1,1,5),_CntpSysRootDispersion_Type())
cntpSysRootDispersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cntpSysRootDispersion.setStatus(_B)
if mibBuilder.loadTexts:cntpSysRootDispersion.setUnits(_E)
_CntpSysRefId_Type=NTPRefId
_CntpSysRefId_Object=MibScalar
cntpSysRefId=_CntpSysRefId_Object((1,3,6,1,4,1,9,9,168,1,1,6),_CntpSysRefId_Type())
cntpSysRefId.setMaxAccess(_C)
if mibBuilder.loadTexts:cntpSysRefId.setStatus(_B)
_CntpSysRefTime_Type=NTPTimeStamp
_CntpSysRefTime_Object=MibScalar
cntpSysRefTime=_CntpSysRefTime_Object((1,3,6,1,4,1,9,9,168,1,1,7),_CntpSysRefTime_Type())
cntpSysRefTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cntpSysRefTime.setStatus(_B)
_CntpSysPoll_Type=NTPPollInterval
_CntpSysPoll_Object=MibScalar
cntpSysPoll=_CntpSysPoll_Object((1,3,6,1,4,1,9,9,168,1,1,8),_CntpSysPoll_Type())
cntpSysPoll.setMaxAccess(_C)
if mibBuilder.loadTexts:cntpSysPoll.setStatus(_B)
_CntpSysPeer_Type=NTPAssocIdentifier
_CntpSysPeer_Object=MibScalar
cntpSysPeer=_CntpSysPeer_Object((1,3,6,1,4,1,9,9,168,1,1,9),_CntpSysPeer_Type())
cntpSysPeer.setMaxAccess(_C)
if mibBuilder.loadTexts:cntpSysPeer.setStatus(_B)
_CntpSysClock_Type=NTPTimeStamp
_CntpSysClock_Object=MibScalar
cntpSysClock=_CntpSysClock_Object((1,3,6,1,4,1,9,9,168,1,1,10),_CntpSysClock_Type())
cntpSysClock.setMaxAccess(_C)
if mibBuilder.loadTexts:cntpSysClock.setStatus(_B)
class _CntpSysSrvStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('unknown',1),('notRunning',2),('notSynchronized',3),('syncToLocal',4),('syncToRefclock',5),('syncToRemoteServer',6)))
_CntpSysSrvStatus_Type.__name__=_D
_CntpSysSrvStatus_Object=MibScalar
cntpSysSrvStatus=_CntpSysSrvStatus_Object((1,3,6,1,4,1,9,9,168,1,1,11),_CntpSysSrvStatus_Type())
cntpSysSrvStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cntpSysSrvStatus.setStatus(_B)
_CntpPeers_ObjectIdentity=ObjectIdentity
cntpPeers=_CntpPeers_ObjectIdentity((1,3,6,1,4,1,9,9,168,1,2))
_CntpPeersVarTable_Object=MibTable
cntpPeersVarTable=_CntpPeersVarTable_Object((1,3,6,1,4,1,9,9,168,1,2,1))
if mibBuilder.loadTexts:cntpPeersVarTable.setStatus(_B)
_CntpPeersVarEntry_Object=MibTableRow
cntpPeersVarEntry=_CntpPeersVarEntry_Object((1,3,6,1,4,1,9,9,168,1,2,1,1))
cntpPeersVarEntry.setIndexNames((0,_A,_j))
if mibBuilder.loadTexts:cntpPeersVarEntry.setStatus(_B)
_CntpPeersAssocId_Type=NTPAssocIdentifier
_CntpPeersAssocId_Object=MibTableColumn
cntpPeersAssocId=_CntpPeersAssocId_Object((1,3,6,1,4,1,9,9,168,1,2,1,1,1),_CntpPeersAssocId_Type())
cntpPeersAssocId.setMaxAccess(_r)
if mibBuilder.loadTexts:cntpPeersAssocId.setStatus(_B)
_CntpPeersConfigured_Type=TruthValue
_CntpPeersConfigured_Object=MibTableColumn
cntpPeersConfigured=_CntpPeersConfigured_Object((1,3,6,1,4,1,9,9,168,1,2,1,1,2),_CntpPeersConfigured_Type())
cntpPeersConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:cntpPeersConfigured.setStatus(_B)
_CntpPeersPeerAddress_Type=IpAddress
_CntpPeersPeerAddress_Object=MibTableColumn
cntpPeersPeerAddress=_CntpPeersPeerAddress_Object((1,3,6,1,4,1,9,9,168,1,2,1,1,3),_CntpPeersPeerAddress_Type())
cntpPeersPeerAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:cntpPeersPeerAddress.setStatus(_B)
class _CntpPeersPeerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CntpPeersPeerPort_Type.__name__=_D
_CntpPeersPeerPort_Object=MibTableColumn
cntpPeersPeerPort=_CntpPeersPeerPort_Object((1,3,6,1,4,1,9,9,168,1,2,1,1,4),_CntpPeersPeerPort_Type())
cntpPeersPeerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cntpPeersPeerPort.setStatus(_B)
_CntpPeersHostAddress_Type=IpAddress
_CntpPeersHostAddress_Object=MibTableColumn
cntpPeersHostAddress=_CntpPeersHostAddress_Object((1,3,6,1,4,1,9,9,168,1,2,1,1,5),_CntpPeersHostAddress_Type())
cntpPeersHostAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:cntpPeersHostAddress.setStatus(_B)
class _CntpPeersHostPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CntpPeersHostPort_Type.__name__=_D
_CntpPeersHostPort_Object=MibTableColumn
cntpPeersHostPort=_CntpPeersHostPort_Object((1,3,6,1,4,1,9,9,168,1,2,1,1,6),_CntpPeersHostPort_Type())
cntpPeersHostPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cntpPeersHostPort.setStatus(_B)
_CntpPeersLeap_Type=NTPLeapIndicator
_CntpPeersLeap_Object=MibTableColumn
cntpPeersLeap=_CntpPeersLeap_Object((1,3,6,1,4,1,9,9,168,1,2,1,1,7),_CntpPeersLeap_Type())
cntpPeersLeap.setMaxAccess(_C)
if mibBuilder.loadTexts:cntpPeersLeap.setStatus(_B)
class _CntpPeersMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('unspecified',0),('symmetricActive',1),('symmetricPassive',2),('client',3),('server',4),('broadcast',5),('reservedControl',6),('reservedPrivate',7)))
_CntpPeersMode_Type.__name__=_D
_CntpPeersMode_Object=MibTableColumn
cntpPeersMode=_CntpPeersMode_Object((1,3,6,1,4,1,9,9,168,1,2,1,1,8),_CntpPeersMode_Type())
cntpPeersMode.setMaxAccess(_F)
if mibBuilder.loadTexts:cntpPeersMode.setStatus(_B)
_CntpPeersStratum_Type=NTPStratum
_CntpPeersStratum_Object=MibTableColumn
cntpPeersStratum=_CntpPeersStratum_Object((1,3,6,1,4,1,9,9,168,1,2,1,1,9),_CntpPeersStratum_Type())
cntpPeersStratum.setMaxAccess(_C)
if mibBuilder.loadTexts:cntpPeersStratum.setStatus(_B)
_CntpPeersPeerPoll_Type=NTPPollInterval
_CntpPeersPeerPoll_Object=MibTableColumn
cntpPeersPeerPoll=_CntpPeersPeerPoll_Object((1,3,6,1,4,1,9,9,168,1,2,1,1,10),_CntpPeersPeerPoll_Type())
cntpPeersPeerPoll.setMaxAccess(_C)
if mibBuilder.loadTexts:cntpPeersPeerPoll.setStatus(_B)
_CntpPeersHostPoll_Type=NTPPollInterval
_CntpPeersHostPoll_Object=MibTableColumn
cntpPeersHostPoll=_CntpPeersHostPoll_Object((1,3,6,1,4,1,9,9,168,1,2,1,1,11),_CntpPeersHostPoll_Type())
cntpPeersHostPoll.setMaxAccess(_C)
if mibBuilder.loadTexts:cntpPeersHostPoll.setStatus(_B)
class _CntpPeersPrecision_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-20,20))
_CntpPeersPrecision_Type.__name__=_D
_CntpPeersPrecision_Object=MibTableColumn
cntpPeersPrecision=_CntpPeersPrecision_Object((1,3,6,1,4,1,9,9,168,1,2,1,1,12),_CntpPeersPrecision_Type())
cntpPeersPrecision.setMaxAccess(_C)
if mibBuilder.loadTexts:cntpPeersPrecision.setStatus(_B)
_CntpPeersRootDelay_Type=NTPSignedTimeValue
_CntpPeersRootDelay_Object=MibTableColumn
cntpPeersRootDelay=_CntpPeersRootDelay_Object((1,3,6,1,4,1,9,9,168,1,2,1,1,13),_CntpPeersRootDelay_Type())
cntpPeersRootDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:cntpPeersRootDelay.setStatus(_B)
if mibBuilder.loadTexts:cntpPeersRootDelay.setUnits(_E)
_CntpPeersRootDispersion_Type=NTPUnsignedTimeValue
_CntpPeersRootDispersion_Object=MibTableColumn
cntpPeersRootDispersion=_CntpPeersRootDispersion_Object((1,3,6,1,4,1,9,9,168,1,2,1,1,14),_CntpPeersRootDispersion_Type())
cntpPeersRootDispersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cntpPeersRootDispersion.setStatus(_B)
if mibBuilder.loadTexts:cntpPeersRootDispersion.setUnits(_E)
_CntpPeersRefId_Type=NTPRefId
_CntpPeersRefId_Object=MibTableColumn
cntpPeersRefId=_CntpPeersRefId_Object((1,3,6,1,4,1,9,9,168,1,2,1,1,15),_CntpPeersRefId_Type())
cntpPeersRefId.setMaxAccess(_C)
if mibBuilder.loadTexts:cntpPeersRefId.setStatus(_B)
_CntpPeersRefTime_Type=NTPTimeStamp
_CntpPeersRefTime_Object=MibTableColumn
cntpPeersRefTime=_CntpPeersRefTime_Object((1,3,6,1,4,1,9,9,168,1,2,1,1,16),_CntpPeersRefTime_Type())
cntpPeersRefTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cntpPeersRefTime.setStatus(_B)
_CntpPeersOrgTime_Type=NTPTimeStamp
_CntpPeersOrgTime_Object=MibTableColumn
cntpPeersOrgTime=_CntpPeersOrgTime_Object((1,3,6,1,4,1,9,9,168,1,2,1,1,17),_CntpPeersOrgTime_Type())
cntpPeersOrgTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cntpPeersOrgTime.setStatus(_B)
_CntpPeersReceiveTime_Type=NTPTimeStamp
_CntpPeersReceiveTime_Object=MibTableColumn
cntpPeersReceiveTime=_CntpPeersReceiveTime_Object((1,3,6,1,4,1,9,9,168,1,2,1,1,18),_CntpPeersReceiveTime_Type())
cntpPeersReceiveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cntpPeersReceiveTime.setStatus(_B)
_CntpPeersTransmitTime_Type=NTPTimeStamp
_CntpPeersTransmitTime_Object=MibTableColumn
cntpPeersTransmitTime=_CntpPeersTransmitTime_Object((1,3,6,1,4,1,9,9,168,1,2,1,1,19),_CntpPeersTransmitTime_Type())
cntpPeersTransmitTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cntpPeersTransmitTime.setStatus(_B)
class _CntpPeersUpdateTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CntpPeersUpdateTime_Type.__name__=_D
_CntpPeersUpdateTime_Object=MibTableColumn
cntpPeersUpdateTime=_CntpPeersUpdateTime_Object((1,3,6,1,4,1,9,9,168,1,2,1,1,20),_CntpPeersUpdateTime_Type())
cntpPeersUpdateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cntpPeersUpdateTime.setStatus(_G)
class _CntpPeersReach_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CntpPeersReach_Type.__name__=_D
_CntpPeersReach_Object=MibTableColumn
cntpPeersReach=_CntpPeersReach_Object((1,3,6,1,4,1,9,9,168,1,2,1,1,21),_CntpPeersReach_Type())
cntpPeersReach.setMaxAccess(_C)
if mibBuilder.loadTexts:cntpPeersReach.setStatus(_B)
class _CntpPeersTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CntpPeersTimer_Type.__name__=_D
_CntpPeersTimer_Object=MibTableColumn
cntpPeersTimer=_CntpPeersTimer_Object((1,3,6,1,4,1,9,9,168,1,2,1,1,22),_CntpPeersTimer_Type())
cntpPeersTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:cntpPeersTimer.setStatus(_B)
if mibBuilder.loadTexts:cntpPeersTimer.setUnits(_E)
_CntpPeersOffset_Type=NTPSignedTimeValue
_CntpPeersOffset_Object=MibTableColumn
cntpPeersOffset=_CntpPeersOffset_Object((1,3,6,1,4,1,9,9,168,1,2,1,1,23),_CntpPeersOffset_Type())
cntpPeersOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:cntpPeersOffset.setStatus(_B)
if mibBuilder.loadTexts:cntpPeersOffset.setUnits(_E)
_CntpPeersDelay_Type=NTPSignedTimeValue
_CntpPeersDelay_Object=MibTableColumn
cntpPeersDelay=_CntpPeersDelay_Object((1,3,6,1,4,1,9,9,168,1,2,1,1,24),_CntpPeersDelay_Type())
cntpPeersDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:cntpPeersDelay.setStatus(_B)
if mibBuilder.loadTexts:cntpPeersDelay.setUnits(_E)
_CntpPeersDispersion_Type=NTPUnsignedTimeValue
_CntpPeersDispersion_Object=MibTableColumn
cntpPeersDispersion=_CntpPeersDispersion_Object((1,3,6,1,4,1,9,9,168,1,2,1,1,25),_CntpPeersDispersion_Type())
cntpPeersDispersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cntpPeersDispersion.setStatus(_B)
if mibBuilder.loadTexts:cntpPeersDispersion.setUnits(_E)
_CntpPeersFilterValidEntries_Type=Gauge32
_CntpPeersFilterValidEntries_Object=MibTableColumn
cntpPeersFilterValidEntries=_CntpPeersFilterValidEntries_Object((1,3,6,1,4,1,9,9,168,1,2,1,1,26),_CntpPeersFilterValidEntries_Type())
cntpPeersFilterValidEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:cntpPeersFilterValidEntries.setStatus(_B)
_CntpPeersEntryStatus_Type=RowStatus
_CntpPeersEntryStatus_Object=MibTableColumn
cntpPeersEntryStatus=_CntpPeersEntryStatus_Object((1,3,6,1,4,1,9,9,168,1,2,1,1,27),_CntpPeersEntryStatus_Type())
cntpPeersEntryStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:cntpPeersEntryStatus.setStatus(_B)
_CntpPeersUpdateTimeRev1_Type=Unsigned32
_CntpPeersUpdateTimeRev1_Object=MibTableColumn
cntpPeersUpdateTimeRev1=_CntpPeersUpdateTimeRev1_Object((1,3,6,1,4,1,9,9,168,1,2,1,1,28),_CntpPeersUpdateTimeRev1_Type())
cntpPeersUpdateTimeRev1.setMaxAccess(_C)
if mibBuilder.loadTexts:cntpPeersUpdateTimeRev1.setStatus(_B)
class _CntpPeersPrefPeer_Type(TruthValue):defaultValue=2
_CntpPeersPrefPeer_Type.__name__=_p
_CntpPeersPrefPeer_Object=MibTableColumn
cntpPeersPrefPeer=_CntpPeersPrefPeer_Object((1,3,6,1,4,1,9,9,168,1,2,1,1,29),_CntpPeersPrefPeer_Type())
cntpPeersPrefPeer.setMaxAccess(_F)
if mibBuilder.loadTexts:cntpPeersPrefPeer.setStatus(_B)
class _CntpPeersPeerType_Type(InetAddressType):defaultValue=1
_CntpPeersPeerType_Type.__name__=_o
_CntpPeersPeerType_Object=MibTableColumn
cntpPeersPeerType=_CntpPeersPeerType_Object((1,3,6,1,4,1,9,9,168,1,2,1,1,30),_CntpPeersPeerType_Type())
cntpPeersPeerType.setMaxAccess(_F)
if mibBuilder.loadTexts:cntpPeersPeerType.setStatus(_B)
_CntpPeersPeerName_Type=InetAddress
_CntpPeersPeerName_Object=MibTableColumn
cntpPeersPeerName=_CntpPeersPeerName_Object((1,3,6,1,4,1,9,9,168,1,2,1,1,31),_CntpPeersPeerName_Type())
cntpPeersPeerName.setMaxAccess(_F)
if mibBuilder.loadTexts:cntpPeersPeerName.setStatus(_B)
_CntpFilter_ObjectIdentity=ObjectIdentity
cntpFilter=_CntpFilter_ObjectIdentity((1,3,6,1,4,1,9,9,168,1,3))
_CntpFilterRegisterTable_Object=MibTable
cntpFilterRegisterTable=_CntpFilterRegisterTable_Object((1,3,6,1,4,1,9,9,168,1,3,2))
if mibBuilder.loadTexts:cntpFilterRegisterTable.setStatus(_B)
_CntpFilterRegisterEntry_Object=MibTableRow
cntpFilterRegisterEntry=_CntpFilterRegisterEntry_Object((1,3,6,1,4,1,9,9,168,1,3,2,1))
cntpFilterRegisterEntry.setIndexNames((0,_A,_j),(0,_A,_s))
if mibBuilder.loadTexts:cntpFilterRegisterEntry.setStatus(_B)
class _CntpFilterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_CntpFilterIndex_Type.__name__=_D
_CntpFilterIndex_Object=MibTableColumn
cntpFilterIndex=_CntpFilterIndex_Object((1,3,6,1,4,1,9,9,168,1,3,2,1,1),_CntpFilterIndex_Type())
cntpFilterIndex.setMaxAccess(_r)
if mibBuilder.loadTexts:cntpFilterIndex.setStatus(_B)
_CntpFilterPeersOffset_Type=NTPSignedTimeValue
_CntpFilterPeersOffset_Object=MibTableColumn
cntpFilterPeersOffset=_CntpFilterPeersOffset_Object((1,3,6,1,4,1,9,9,168,1,3,2,1,2),_CntpFilterPeersOffset_Type())
cntpFilterPeersOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:cntpFilterPeersOffset.setStatus(_B)
if mibBuilder.loadTexts:cntpFilterPeersOffset.setUnits(_E)
_CntpFilterPeersDelay_Type=NTPSignedTimeValue
_CntpFilterPeersDelay_Object=MibTableColumn
cntpFilterPeersDelay=_CntpFilterPeersDelay_Object((1,3,6,1,4,1,9,9,168,1,3,2,1,3),_CntpFilterPeersDelay_Type())
cntpFilterPeersDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:cntpFilterPeersDelay.setStatus(_B)
if mibBuilder.loadTexts:cntpFilterPeersDelay.setUnits(_E)
_CntpFilterPeersDispersion_Type=NTPUnsignedTimeValue
_CntpFilterPeersDispersion_Object=MibTableColumn
cntpFilterPeersDispersion=_CntpFilterPeersDispersion_Object((1,3,6,1,4,1,9,9,168,1,3,2,1,4),_CntpFilterPeersDispersion_Type())
cntpFilterPeersDispersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cntpFilterPeersDispersion.setStatus(_B)
if mibBuilder.loadTexts:cntpFilterPeersDispersion.setUnits(_E)
_CiscoNtpMIBConformance_ObjectIdentity=ObjectIdentity
ciscoNtpMIBConformance=_CiscoNtpMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,168,2))
_CiscoNtpMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoNtpMIBCompliances=_CiscoNtpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,168,2,1))
_CiscoNtpMIBGroups_ObjectIdentity=ObjectIdentity
ciscoNtpMIBGroups=_CiscoNtpMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,168,2,2))
ciscoNtpSysGroup=ObjectGroup((1,3,6,1,4,1,9,9,168,2,2,1))
ciscoNtpSysGroup.setObjects(*((_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2)))
if mibBuilder.loadTexts:ciscoNtpSysGroup.setStatus(_B)
ciscoNtpPeersGroup=ObjectGroup((1,3,6,1,4,1,9,9,168,2,2,2))
ciscoNtpPeersGroup.setObjects(*((_A,_K),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_A3),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:ciscoNtpPeersGroup.setStatus(_G)
ciscoNtpFilterGroup=ObjectGroup((1,3,6,1,4,1,9,9,168,2,2,3))
ciscoNtpFilterGroup.setObjects(*((_A,_A4),(_A,_A5),(_A,_A6)))
if mibBuilder.loadTexts:ciscoNtpFilterGroup.setStatus(_B)
ciscoNtpPeersGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,168,2,2,4))
ciscoNtpPeersGroupRev1.setObjects(*((_A,_K),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_k),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:ciscoNtpPeersGroupRev1.setStatus(_G)
ciscoNtpPeerExtGroup=ObjectGroup((1,3,6,1,4,1,9,9,168,2,2,5))
ciscoNtpPeerExtGroup.setObjects((_A,_A7))
if mibBuilder.loadTexts:ciscoNtpPeerExtGroup.setStatus(_B)
ciscoNtpPeersGroupRev2=ObjectGroup((1,3,6,1,4,1,9,9,168,2,2,6))
ciscoNtpPeersGroupRev2.setObjects(*((_A,_K),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_k),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_A8),(_A,_A9)))
if mibBuilder.loadTexts:ciscoNtpPeersGroupRev2.setStatus(_B)
ciscoNtpSysExtGroup=ObjectGroup((1,3,6,1,4,1,9,9,168,2,2,7))
ciscoNtpSysExtGroup.setObjects((_A,_l))
if mibBuilder.loadTexts:ciscoNtpSysExtGroup.setStatus(_B)
ciscoNtpSrvStatusChange=NotificationType((1,3,6,1,4,1,9,9,168,0,1))
ciscoNtpSrvStatusChange.setObjects((_A,_l))
if mibBuilder.loadTexts:ciscoNtpSrvStatusChange.setStatus(_B)
ciscoNtpHighPriorityConnFailure=NotificationType((1,3,6,1,4,1,9,9,168,0,2))
ciscoNtpHighPriorityConnFailure.setObjects((_A,_H))
if mibBuilder.loadTexts:ciscoNtpHighPriorityConnFailure.setStatus(_B)
ciscoNtpHighPriorityConnRestore=NotificationType((1,3,6,1,4,1,9,9,168,0,3))
ciscoNtpHighPriorityConnRestore.setObjects((_A,_H))
if mibBuilder.loadTexts:ciscoNtpHighPriorityConnRestore.setStatus(_B)
ciscoNtpGeneralConnFailure=NotificationType((1,3,6,1,4,1,9,9,168,0,4))
if mibBuilder.loadTexts:ciscoNtpGeneralConnFailure.setStatus(_B)
ciscoNtpGeneralConnRestore=NotificationType((1,3,6,1,4,1,9,9,168,0,5))
ciscoNtpGeneralConnRestore.setObjects((_A,_H))
if mibBuilder.loadTexts:ciscoNtpGeneralConnRestore.setStatus(_B)
ciscoNtpSrvNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,168,2,2,8))
ciscoNtpSrvNotifGroup.setObjects(*((_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE)))
if mibBuilder.loadTexts:ciscoNtpSrvNotifGroup.setStatus(_B)
ciscoNtpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,168,2,1,1))
ciscoNtpMIBCompliance.setObjects(*((_A,_I),(_A,_AF),(_A,_J)))
if mibBuilder.loadTexts:ciscoNtpMIBCompliance.setStatus(_G)
ciscoNtpMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,168,2,1,2))
ciscoNtpMIBComplianceRev1.setObjects(*((_A,_I),(_A,_m),(_A,_J)))
if mibBuilder.loadTexts:ciscoNtpMIBComplianceRev1.setStatus(_G)
ciscoNtpMIBComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,168,2,1,3))
ciscoNtpMIBComplianceRev2.setObjects(*((_A,_I),(_A,_m),(_A,_J),(_A,_i)))
if mibBuilder.loadTexts:ciscoNtpMIBComplianceRev2.setStatus(_G)
ciscoNtpMIBComplianceRev3=ModuleCompliance((1,3,6,1,4,1,9,9,168,2,1,4))
ciscoNtpMIBComplianceRev3.setObjects(*((_A,_I),(_A,_n),(_A,_J),(_A,_i)))
if mibBuilder.loadTexts:ciscoNtpMIBComplianceRev3.setStatus(_G)
ciscoNtpMIBComplianceRev4=ModuleCompliance((1,3,6,1,4,1,9,9,168,2,1,5))
ciscoNtpMIBComplianceRev4.setObjects(*((_A,_I),(_A,_n),(_A,_J),(_A,_i),(_A,_AG),(_A,_AH)))
if mibBuilder.loadTexts:ciscoNtpMIBComplianceRev4.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'NTPTimeStamp':NTPTimeStamp,'NTPLeapIndicator':NTPLeapIndicator,'NTPSignedTimeValue':NTPSignedTimeValue,'NTPUnsignedTimeValue':NTPUnsignedTimeValue,'NTPStratum':NTPStratum,'NTPRefId':NTPRefId,'NTPPollInterval':NTPPollInterval,'NTPAssocIdentifier':NTPAssocIdentifier,'ciscoNtpMIB':ciscoNtpMIB,'ciscoNtpMIBNotifs':ciscoNtpMIBNotifs,_AA:ciscoNtpSrvStatusChange,_AB:ciscoNtpHighPriorityConnFailure,_AC:ciscoNtpHighPriorityConnRestore,_AD:ciscoNtpGeneralConnFailure,_AE:ciscoNtpGeneralConnRestore,'ciscoNtpMIBObjects':ciscoNtpMIBObjects,'cntpSystem':cntpSystem,_t:cntpSysLeap,_u:cntpSysStratum,_v:cntpSysPrecision,_w:cntpSysRootDelay,_x:cntpSysRootDispersion,_y:cntpSysRefId,_z:cntpSysRefTime,_A0:cntpSysPoll,_A1:cntpSysPeer,_A2:cntpSysClock,_l:cntpSysSrvStatus,'cntpPeers':cntpPeers,'cntpPeersVarTable':cntpPeersVarTable,'cntpPeersVarEntry':cntpPeersVarEntry,_j:cntpPeersAssocId,_K:cntpPeersConfigured,_H:cntpPeersPeerAddress,_L:cntpPeersPeerPort,_M:cntpPeersHostAddress,_N:cntpPeersHostPort,_O:cntpPeersLeap,_P:cntpPeersMode,_Q:cntpPeersStratum,_R:cntpPeersPeerPoll,_S:cntpPeersHostPoll,_T:cntpPeersPrecision,_U:cntpPeersRootDelay,_V:cntpPeersRootDispersion,_W:cntpPeersRefId,_X:cntpPeersRefTime,_Y:cntpPeersOrgTime,_Z:cntpPeersReceiveTime,_a:cntpPeersTransmitTime,_A3:cntpPeersUpdateTime,_b:cntpPeersReach,_c:cntpPeersTimer,_d:cntpPeersOffset,_e:cntpPeersDelay,_f:cntpPeersDispersion,_g:cntpPeersFilterValidEntries,_h:cntpPeersEntryStatus,_k:cntpPeersUpdateTimeRev1,_A7:cntpPeersPrefPeer,_A9:cntpPeersPeerType,_A8:cntpPeersPeerName,'cntpFilter':cntpFilter,'cntpFilterRegisterTable':cntpFilterRegisterTable,'cntpFilterRegisterEntry':cntpFilterRegisterEntry,_s:cntpFilterIndex,_A4:cntpFilterPeersOffset,_A5:cntpFilterPeersDelay,_A6:cntpFilterPeersDispersion,'ciscoNtpMIBConformance':ciscoNtpMIBConformance,'ciscoNtpMIBCompliances':ciscoNtpMIBCompliances,'ciscoNtpMIBCompliance':ciscoNtpMIBCompliance,'ciscoNtpMIBComplianceRev1':ciscoNtpMIBComplianceRev1,'ciscoNtpMIBComplianceRev2':ciscoNtpMIBComplianceRev2,'ciscoNtpMIBComplianceRev3':ciscoNtpMIBComplianceRev3,'ciscoNtpMIBComplianceRev4':ciscoNtpMIBComplianceRev4,'ciscoNtpMIBGroups':ciscoNtpMIBGroups,_I:ciscoNtpSysGroup,_AF:ciscoNtpPeersGroup,_J:ciscoNtpFilterGroup,_m:ciscoNtpPeersGroupRev1,_i:ciscoNtpPeerExtGroup,_n:ciscoNtpPeersGroupRev2,_AG:ciscoNtpSysExtGroup,_AH:ciscoNtpSrvNotifGroup})