_K='rcNtpFilterIndex'
_J='not-accessible'
_I='NTPPollInterval'
_H='rcNtpPeersAssocId'
_G='read-create'
_F='RAISECOM-NTP-MIB'
_E='read-write'
_D='seconds'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
rcNtp=ModuleIdentity((1,3,6,1,4,1,8886,6,1,44))
if mibBuilder.loadTexts:rcNtp.setRevisions(('2009-02-09 00:00',))
class NTPTimeStamp(TextualConvention,OctetString):status=_A;displayHint='4d.4d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class NTPLeapIndicator(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('noWarning',0),('addSecond',1),('subtractSecond',2),('alarm',3)))
class NTPSignedTimeValue(TextualConvention,OctetString):status=_A;displayHint='2d.2d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class NTPUnsignedTimeValue(TextualConvention,OctetString):status=_A;displayHint='2d.2d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class NTPStratum(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class NTPRefId(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class NTPPollInterval(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-20,20))
class NTPAssocIdentifier(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RcNtpMIBObjects_ObjectIdentity=ObjectIdentity
rcNtpMIBObjects=_RcNtpMIBObjects_ObjectIdentity((1,3,6,1,4,1,8886,6,1,44,1))
_RcNtpSystem_ObjectIdentity=ObjectIdentity
rcNtpSystem=_RcNtpSystem_ObjectIdentity((1,3,6,1,4,1,8886,6,1,44,1,1))
_RcNtpSysLeap_Type=NTPLeapIndicator
_RcNtpSysLeap_Object=MibScalar
rcNtpSysLeap=_RcNtpSysLeap_Object((1,3,6,1,4,1,8886,6,1,44,1,1,1),_RcNtpSysLeap_Type())
rcNtpSysLeap.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNtpSysLeap.setStatus(_A)
_RcNtpSysStratum_Type=NTPStratum
_RcNtpSysStratum_Object=MibScalar
rcNtpSysStratum=_RcNtpSysStratum_Object((1,3,6,1,4,1,8886,6,1,44,1,1,2),_RcNtpSysStratum_Type())
rcNtpSysStratum.setMaxAccess(_E)
if mibBuilder.loadTexts:rcNtpSysStratum.setStatus(_A)
_RcNtpSysPrecision_Type=Integer32
_RcNtpSysPrecision_Object=MibScalar
rcNtpSysPrecision=_RcNtpSysPrecision_Object((1,3,6,1,4,1,8886,6,1,44,1,1,3),_RcNtpSysPrecision_Type())
rcNtpSysPrecision.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNtpSysPrecision.setStatus(_A)
_RcNtpSysRootDelay_Type=NTPSignedTimeValue
_RcNtpSysRootDelay_Object=MibScalar
rcNtpSysRootDelay=_RcNtpSysRootDelay_Object((1,3,6,1,4,1,8886,6,1,44,1,1,4),_RcNtpSysRootDelay_Type())
rcNtpSysRootDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNtpSysRootDelay.setStatus(_A)
if mibBuilder.loadTexts:rcNtpSysRootDelay.setUnits(_D)
_RcNtpSysRootDispersion_Type=NTPUnsignedTimeValue
_RcNtpSysRootDispersion_Object=MibScalar
rcNtpSysRootDispersion=_RcNtpSysRootDispersion_Object((1,3,6,1,4,1,8886,6,1,44,1,1,5),_RcNtpSysRootDispersion_Type())
rcNtpSysRootDispersion.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNtpSysRootDispersion.setStatus(_A)
if mibBuilder.loadTexts:rcNtpSysRootDispersion.setUnits(_D)
_RcNtpSysRefId_Type=NTPRefId
_RcNtpSysRefId_Object=MibScalar
rcNtpSysRefId=_RcNtpSysRefId_Object((1,3,6,1,4,1,8886,6,1,44,1,1,6),_RcNtpSysRefId_Type())
rcNtpSysRefId.setMaxAccess(_E)
if mibBuilder.loadTexts:rcNtpSysRefId.setStatus(_A)
_RcNtpSysRefTime_Type=NTPTimeStamp
_RcNtpSysRefTime_Object=MibScalar
rcNtpSysRefTime=_RcNtpSysRefTime_Object((1,3,6,1,4,1,8886,6,1,44,1,1,7),_RcNtpSysRefTime_Type())
rcNtpSysRefTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNtpSysRefTime.setStatus(_A)
class _RcNtpSysPoll_Type(NTPPollInterval):subtypeSpec=NTPPollInterval.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,10))
_RcNtpSysPoll_Type.__name__=_I
_RcNtpSysPoll_Object=MibScalar
rcNtpSysPoll=_RcNtpSysPoll_Object((1,3,6,1,4,1,8886,6,1,44,1,1,8),_RcNtpSysPoll_Type())
rcNtpSysPoll.setMaxAccess(_E)
if mibBuilder.loadTexts:rcNtpSysPoll.setStatus(_A)
_RcNtpSysPeer_Type=NTPAssocIdentifier
_RcNtpSysPeer_Object=MibScalar
rcNtpSysPeer=_RcNtpSysPeer_Object((1,3,6,1,4,1,8886,6,1,44,1,1,9),_RcNtpSysPeer_Type())
rcNtpSysPeer.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNtpSysPeer.setStatus(_A)
_RcNtpSysClock_Type=NTPTimeStamp
_RcNtpSysClock_Object=MibScalar
rcNtpSysClock=_RcNtpSysClock_Object((1,3,6,1,4,1,8886,6,1,44,1,1,10),_RcNtpSysClock_Type())
rcNtpSysClock.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNtpSysClock.setStatus(_A)
class _RcNtpSysClockStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('setByNone',1),('setByManual',2),('setByTimeProtocol',3)))
_RcNtpSysClockStatus_Type.__name__=_C
_RcNtpSysClockStatus_Object=MibScalar
rcNtpSysClockStatus=_RcNtpSysClockStatus_Object((1,3,6,1,4,1,8886,6,1,44,1,1,11),_RcNtpSysClockStatus_Type())
rcNtpSysClockStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNtpSysClockStatus.setStatus(_A)
class _RcNtpSysVersion_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('v1',1),('v2',2),('v3',3)))
_RcNtpSysVersion_Type.__name__=_C
_RcNtpSysVersion_Object=MibScalar
rcNtpSysVersion=_RcNtpSysVersion_Object((1,3,6,1,4,1,8886,6,1,44,1,1,12),_RcNtpSysVersion_Type())
rcNtpSysVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:rcNtpSysVersion.setStatus('deprecated')
class _RcNtpSysMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ntpMaster',1),('ntpSlave',2)))
_RcNtpSysMode_Type.__name__=_C
_RcNtpSysMode_Object=MibScalar
rcNtpSysMode=_RcNtpSysMode_Object((1,3,6,1,4,1,8886,6,1,44,1,1,13),_RcNtpSysMode_Type())
rcNtpSysMode.setMaxAccess(_E)
if mibBuilder.loadTexts:rcNtpSysMode.setStatus(_A)
class _RcNtpSysValidServicerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RcNtpSysValidServicerIndex_Type.__name__=_C
_RcNtpSysValidServicerIndex_Object=MibScalar
rcNtpSysValidServicerIndex=_RcNtpSysValidServicerIndex_Object((1,3,6,1,4,1,8886,6,1,44,1,1,14),_RcNtpSysValidServicerIndex_Type())
rcNtpSysValidServicerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNtpSysValidServicerIndex.setStatus(_A)
_RcNtpPeers_ObjectIdentity=ObjectIdentity
rcNtpPeers=_RcNtpPeers_ObjectIdentity((1,3,6,1,4,1,8886,6,1,44,1,2))
_RcNtpPeersVarTable_Object=MibTable
rcNtpPeersVarTable=_RcNtpPeersVarTable_Object((1,3,6,1,4,1,8886,6,1,44,1,2,1))
if mibBuilder.loadTexts:rcNtpPeersVarTable.setStatus(_A)
_RcNtpPeersVarEntry_Object=MibTableRow
rcNtpPeersVarEntry=_RcNtpPeersVarEntry_Object((1,3,6,1,4,1,8886,6,1,44,1,2,1,1))
rcNtpPeersVarEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:rcNtpPeersVarEntry.setStatus(_A)
_RcNtpPeersAssocId_Type=NTPAssocIdentifier
_RcNtpPeersAssocId_Object=MibTableColumn
rcNtpPeersAssocId=_RcNtpPeersAssocId_Object((1,3,6,1,4,1,8886,6,1,44,1,2,1,1,1),_RcNtpPeersAssocId_Type())
rcNtpPeersAssocId.setMaxAccess(_J)
if mibBuilder.loadTexts:rcNtpPeersAssocId.setStatus(_A)
_RcNtpPeersConfigured_Type=TruthValue
_RcNtpPeersConfigured_Object=MibTableColumn
rcNtpPeersConfigured=_RcNtpPeersConfigured_Object((1,3,6,1,4,1,8886,6,1,44,1,2,1,1,2),_RcNtpPeersConfigured_Type())
rcNtpPeersConfigured.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNtpPeersConfigured.setStatus(_A)
_RcNtpPeersPeerAddress_Type=IpAddress
_RcNtpPeersPeerAddress_Object=MibTableColumn
rcNtpPeersPeerAddress=_RcNtpPeersPeerAddress_Object((1,3,6,1,4,1,8886,6,1,44,1,2,1,1,3),_RcNtpPeersPeerAddress_Type())
rcNtpPeersPeerAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:rcNtpPeersPeerAddress.setStatus(_A)
class _RcNtpPeersPeerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RcNtpPeersPeerPort_Type.__name__=_C
_RcNtpPeersPeerPort_Object=MibTableColumn
rcNtpPeersPeerPort=_RcNtpPeersPeerPort_Object((1,3,6,1,4,1,8886,6,1,44,1,2,1,1,4),_RcNtpPeersPeerPort_Type())
rcNtpPeersPeerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNtpPeersPeerPort.setStatus(_A)
_RcNtpPeersHostAddress_Type=IpAddress
_RcNtpPeersHostAddress_Object=MibTableColumn
rcNtpPeersHostAddress=_RcNtpPeersHostAddress_Object((1,3,6,1,4,1,8886,6,1,44,1,2,1,1,5),_RcNtpPeersHostAddress_Type())
rcNtpPeersHostAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:rcNtpPeersHostAddress.setStatus(_A)
class _RcNtpPeersHostPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RcNtpPeersHostPort_Type.__name__=_C
_RcNtpPeersHostPort_Object=MibTableColumn
rcNtpPeersHostPort=_RcNtpPeersHostPort_Object((1,3,6,1,4,1,8886,6,1,44,1,2,1,1,6),_RcNtpPeersHostPort_Type())
rcNtpPeersHostPort.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNtpPeersHostPort.setStatus(_A)
_RcNtpPeersLeap_Type=NTPLeapIndicator
_RcNtpPeersLeap_Object=MibTableColumn
rcNtpPeersLeap=_RcNtpPeersLeap_Object((1,3,6,1,4,1,8886,6,1,44,1,2,1,1,7),_RcNtpPeersLeap_Type())
rcNtpPeersLeap.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNtpPeersLeap.setStatus(_A)
class _RcNtpPeersMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('unspecified',0),('symmetricActive',1),('symmetricPassive',2),('client',3),('server',4),('broadcast',5),('reservedControl',6),('reservedPrivate',7)))
_RcNtpPeersMode_Type.__name__=_C
_RcNtpPeersMode_Object=MibTableColumn
rcNtpPeersMode=_RcNtpPeersMode_Object((1,3,6,1,4,1,8886,6,1,44,1,2,1,1,8),_RcNtpPeersMode_Type())
rcNtpPeersMode.setMaxAccess(_G)
if mibBuilder.loadTexts:rcNtpPeersMode.setStatus(_A)
_RcNtpPeersStratum_Type=NTPStratum
_RcNtpPeersStratum_Object=MibTableColumn
rcNtpPeersStratum=_RcNtpPeersStratum_Object((1,3,6,1,4,1,8886,6,1,44,1,2,1,1,9),_RcNtpPeersStratum_Type())
rcNtpPeersStratum.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNtpPeersStratum.setStatus(_A)
_RcNtpPeersPeerPoll_Type=NTPPollInterval
_RcNtpPeersPeerPoll_Object=MibTableColumn
rcNtpPeersPeerPoll=_RcNtpPeersPeerPoll_Object((1,3,6,1,4,1,8886,6,1,44,1,2,1,1,10),_RcNtpPeersPeerPoll_Type())
rcNtpPeersPeerPoll.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNtpPeersPeerPoll.setStatus(_A)
_RcNtpPeersHostPoll_Type=NTPPollInterval
_RcNtpPeersHostPoll_Object=MibTableColumn
rcNtpPeersHostPoll=_RcNtpPeersHostPoll_Object((1,3,6,1,4,1,8886,6,1,44,1,2,1,1,11),_RcNtpPeersHostPoll_Type())
rcNtpPeersHostPoll.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNtpPeersHostPoll.setStatus(_A)
_RcNtpPeersPrecision_Type=Integer32
_RcNtpPeersPrecision_Object=MibTableColumn
rcNtpPeersPrecision=_RcNtpPeersPrecision_Object((1,3,6,1,4,1,8886,6,1,44,1,2,1,1,12),_RcNtpPeersPrecision_Type())
rcNtpPeersPrecision.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNtpPeersPrecision.setStatus(_A)
_RcNtpPeersRootDelay_Type=NTPSignedTimeValue
_RcNtpPeersRootDelay_Object=MibTableColumn
rcNtpPeersRootDelay=_RcNtpPeersRootDelay_Object((1,3,6,1,4,1,8886,6,1,44,1,2,1,1,13),_RcNtpPeersRootDelay_Type())
rcNtpPeersRootDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNtpPeersRootDelay.setStatus(_A)
if mibBuilder.loadTexts:rcNtpPeersRootDelay.setUnits(_D)
_RcNtpPeersRootDispersion_Type=NTPUnsignedTimeValue
_RcNtpPeersRootDispersion_Object=MibTableColumn
rcNtpPeersRootDispersion=_RcNtpPeersRootDispersion_Object((1,3,6,1,4,1,8886,6,1,44,1,2,1,1,14),_RcNtpPeersRootDispersion_Type())
rcNtpPeersRootDispersion.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNtpPeersRootDispersion.setStatus(_A)
if mibBuilder.loadTexts:rcNtpPeersRootDispersion.setUnits(_D)
_RcNtpPeersRefId_Type=NTPRefId
_RcNtpPeersRefId_Object=MibTableColumn
rcNtpPeersRefId=_RcNtpPeersRefId_Object((1,3,6,1,4,1,8886,6,1,44,1,2,1,1,15),_RcNtpPeersRefId_Type())
rcNtpPeersRefId.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNtpPeersRefId.setStatus(_A)
_RcNtpPeersRefTime_Type=NTPTimeStamp
_RcNtpPeersRefTime_Object=MibTableColumn
rcNtpPeersRefTime=_RcNtpPeersRefTime_Object((1,3,6,1,4,1,8886,6,1,44,1,2,1,1,16),_RcNtpPeersRefTime_Type())
rcNtpPeersRefTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNtpPeersRefTime.setStatus(_A)
_RcNtpPeersOrgTime_Type=NTPTimeStamp
_RcNtpPeersOrgTime_Object=MibTableColumn
rcNtpPeersOrgTime=_RcNtpPeersOrgTime_Object((1,3,6,1,4,1,8886,6,1,44,1,2,1,1,17),_RcNtpPeersOrgTime_Type())
rcNtpPeersOrgTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNtpPeersOrgTime.setStatus(_A)
_RcNtpPeersReceiveTime_Type=NTPTimeStamp
_RcNtpPeersReceiveTime_Object=MibTableColumn
rcNtpPeersReceiveTime=_RcNtpPeersReceiveTime_Object((1,3,6,1,4,1,8886,6,1,44,1,2,1,1,18),_RcNtpPeersReceiveTime_Type())
rcNtpPeersReceiveTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNtpPeersReceiveTime.setStatus(_A)
_RcNtpPeersTransmitTime_Type=NTPTimeStamp
_RcNtpPeersTransmitTime_Object=MibTableColumn
rcNtpPeersTransmitTime=_RcNtpPeersTransmitTime_Object((1,3,6,1,4,1,8886,6,1,44,1,2,1,1,19),_RcNtpPeersTransmitTime_Type())
rcNtpPeersTransmitTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNtpPeersTransmitTime.setStatus(_A)
_RcNtpPeersUpdateTime_Type=Unsigned32
_RcNtpPeersUpdateTime_Object=MibTableColumn
rcNtpPeersUpdateTime=_RcNtpPeersUpdateTime_Object((1,3,6,1,4,1,8886,6,1,44,1,2,1,1,20),_RcNtpPeersUpdateTime_Type())
rcNtpPeersUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNtpPeersUpdateTime.setStatus(_A)
class _RcNtpPeersReach_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RcNtpPeersReach_Type.__name__=_C
_RcNtpPeersReach_Object=MibTableColumn
rcNtpPeersReach=_RcNtpPeersReach_Object((1,3,6,1,4,1,8886,6,1,44,1,2,1,1,21),_RcNtpPeersReach_Type())
rcNtpPeersReach.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNtpPeersReach.setStatus(_A)
class _RcNtpPeersTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RcNtpPeersTimer_Type.__name__=_C
_RcNtpPeersTimer_Object=MibTableColumn
rcNtpPeersTimer=_RcNtpPeersTimer_Object((1,3,6,1,4,1,8886,6,1,44,1,2,1,1,22),_RcNtpPeersTimer_Type())
rcNtpPeersTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNtpPeersTimer.setStatus(_A)
if mibBuilder.loadTexts:rcNtpPeersTimer.setUnits(_D)
_RcNtpPeersOffset_Type=NTPSignedTimeValue
_RcNtpPeersOffset_Object=MibTableColumn
rcNtpPeersOffset=_RcNtpPeersOffset_Object((1,3,6,1,4,1,8886,6,1,44,1,2,1,1,23),_RcNtpPeersOffset_Type())
rcNtpPeersOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNtpPeersOffset.setStatus(_A)
if mibBuilder.loadTexts:rcNtpPeersOffset.setUnits(_D)
_RcNtpPeersDelay_Type=NTPSignedTimeValue
_RcNtpPeersDelay_Object=MibTableColumn
rcNtpPeersDelay=_RcNtpPeersDelay_Object((1,3,6,1,4,1,8886,6,1,44,1,2,1,1,24),_RcNtpPeersDelay_Type())
rcNtpPeersDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNtpPeersDelay.setStatus(_A)
if mibBuilder.loadTexts:rcNtpPeersDelay.setUnits(_D)
_RcNtpPeersDispersion_Type=NTPUnsignedTimeValue
_RcNtpPeersDispersion_Object=MibTableColumn
rcNtpPeersDispersion=_RcNtpPeersDispersion_Object((1,3,6,1,4,1,8886,6,1,44,1,2,1,1,25),_RcNtpPeersDispersion_Type())
rcNtpPeersDispersion.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNtpPeersDispersion.setStatus(_A)
if mibBuilder.loadTexts:rcNtpPeersDispersion.setUnits(_D)
_RcNtpPeersFilterValidEntries_Type=Gauge32
_RcNtpPeersFilterValidEntries_Object=MibTableColumn
rcNtpPeersFilterValidEntries=_RcNtpPeersFilterValidEntries_Object((1,3,6,1,4,1,8886,6,1,44,1,2,1,1,26),_RcNtpPeersFilterValidEntries_Type())
rcNtpPeersFilterValidEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNtpPeersFilterValidEntries.setStatus(_A)
_RcNtpPeersEntryStatus_Type=RowStatus
_RcNtpPeersEntryStatus_Object=MibTableColumn
rcNtpPeersEntryStatus=_RcNtpPeersEntryStatus_Object((1,3,6,1,4,1,8886,6,1,44,1,2,1,1,27),_RcNtpPeersEntryStatus_Type())
rcNtpPeersEntryStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:rcNtpPeersEntryStatus.setStatus(_A)
class _RcNtpPeersVersion_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('v1',1),('v2',2),('v3',3)))
_RcNtpPeersVersion_Type.__name__=_C
_RcNtpPeersVersion_Object=MibTableColumn
rcNtpPeersVersion=_RcNtpPeersVersion_Object((1,3,6,1,4,1,8886,6,1,44,1,2,1,1,28),_RcNtpPeersVersion_Type())
rcNtpPeersVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:rcNtpPeersVersion.setStatus(_A)
_RcNtpFilter_ObjectIdentity=ObjectIdentity
rcNtpFilter=_RcNtpFilter_ObjectIdentity((1,3,6,1,4,1,8886,6,1,44,1,3))
_RcNtpFilterRegisterTable_Object=MibTable
rcNtpFilterRegisterTable=_RcNtpFilterRegisterTable_Object((1,3,6,1,4,1,8886,6,1,44,1,3,1))
if mibBuilder.loadTexts:rcNtpFilterRegisterTable.setStatus(_A)
_RcNtpFilterRegisterEntry_Object=MibTableRow
rcNtpFilterRegisterEntry=_RcNtpFilterRegisterEntry_Object((1,3,6,1,4,1,8886,6,1,44,1,3,1,1))
rcNtpFilterRegisterEntry.setIndexNames((0,_F,_H),(0,_F,_K))
if mibBuilder.loadTexts:rcNtpFilterRegisterEntry.setStatus(_A)
class _RcNtpFilterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_RcNtpFilterIndex_Type.__name__=_C
_RcNtpFilterIndex_Object=MibTableColumn
rcNtpFilterIndex=_RcNtpFilterIndex_Object((1,3,6,1,4,1,8886,6,1,44,1,3,1,1,1),_RcNtpFilterIndex_Type())
rcNtpFilterIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:rcNtpFilterIndex.setStatus(_A)
_RcNtpFilterPeersOffset_Type=NTPSignedTimeValue
_RcNtpFilterPeersOffset_Object=MibTableColumn
rcNtpFilterPeersOffset=_RcNtpFilterPeersOffset_Object((1,3,6,1,4,1,8886,6,1,44,1,3,1,1,2),_RcNtpFilterPeersOffset_Type())
rcNtpFilterPeersOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNtpFilterPeersOffset.setStatus(_A)
if mibBuilder.loadTexts:rcNtpFilterPeersOffset.setUnits(_D)
_RcNtpFilterPeersDelay_Type=NTPSignedTimeValue
_RcNtpFilterPeersDelay_Object=MibTableColumn
rcNtpFilterPeersDelay=_RcNtpFilterPeersDelay_Object((1,3,6,1,4,1,8886,6,1,44,1,3,1,1,3),_RcNtpFilterPeersDelay_Type())
rcNtpFilterPeersDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNtpFilterPeersDelay.setStatus(_A)
if mibBuilder.loadTexts:rcNtpFilterPeersDelay.setUnits(_D)
_RcNtpFilterPeersDispersion_Type=NTPUnsignedTimeValue
_RcNtpFilterPeersDispersion_Object=MibTableColumn
rcNtpFilterPeersDispersion=_RcNtpFilterPeersDispersion_Object((1,3,6,1,4,1,8886,6,1,44,1,3,1,1,4),_RcNtpFilterPeersDispersion_Type())
rcNtpFilterPeersDispersion.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNtpFilterPeersDispersion.setStatus(_A)
if mibBuilder.loadTexts:rcNtpFilterPeersDispersion.setUnits(_D)
mibBuilder.exportSymbols(_F,**{'NTPTimeStamp':NTPTimeStamp,'NTPLeapIndicator':NTPLeapIndicator,'NTPSignedTimeValue':NTPSignedTimeValue,'NTPUnsignedTimeValue':NTPUnsignedTimeValue,'NTPStratum':NTPStratum,'NTPRefId':NTPRefId,_I:NTPPollInterval,'NTPAssocIdentifier':NTPAssocIdentifier,'rcNtp':rcNtp,'rcNtpMIBObjects':rcNtpMIBObjects,'rcNtpSystem':rcNtpSystem,'rcNtpSysLeap':rcNtpSysLeap,'rcNtpSysStratum':rcNtpSysStratum,'rcNtpSysPrecision':rcNtpSysPrecision,'rcNtpSysRootDelay':rcNtpSysRootDelay,'rcNtpSysRootDispersion':rcNtpSysRootDispersion,'rcNtpSysRefId':rcNtpSysRefId,'rcNtpSysRefTime':rcNtpSysRefTime,'rcNtpSysPoll':rcNtpSysPoll,'rcNtpSysPeer':rcNtpSysPeer,'rcNtpSysClock':rcNtpSysClock,'rcNtpSysClockStatus':rcNtpSysClockStatus,'rcNtpSysVersion':rcNtpSysVersion,'rcNtpSysMode':rcNtpSysMode,'rcNtpSysValidServicerIndex':rcNtpSysValidServicerIndex,'rcNtpPeers':rcNtpPeers,'rcNtpPeersVarTable':rcNtpPeersVarTable,'rcNtpPeersVarEntry':rcNtpPeersVarEntry,_H:rcNtpPeersAssocId,'rcNtpPeersConfigured':rcNtpPeersConfigured,'rcNtpPeersPeerAddress':rcNtpPeersPeerAddress,'rcNtpPeersPeerPort':rcNtpPeersPeerPort,'rcNtpPeersHostAddress':rcNtpPeersHostAddress,'rcNtpPeersHostPort':rcNtpPeersHostPort,'rcNtpPeersLeap':rcNtpPeersLeap,'rcNtpPeersMode':rcNtpPeersMode,'rcNtpPeersStratum':rcNtpPeersStratum,'rcNtpPeersPeerPoll':rcNtpPeersPeerPoll,'rcNtpPeersHostPoll':rcNtpPeersHostPoll,'rcNtpPeersPrecision':rcNtpPeersPrecision,'rcNtpPeersRootDelay':rcNtpPeersRootDelay,'rcNtpPeersRootDispersion':rcNtpPeersRootDispersion,'rcNtpPeersRefId':rcNtpPeersRefId,'rcNtpPeersRefTime':rcNtpPeersRefTime,'rcNtpPeersOrgTime':rcNtpPeersOrgTime,'rcNtpPeersReceiveTime':rcNtpPeersReceiveTime,'rcNtpPeersTransmitTime':rcNtpPeersTransmitTime,'rcNtpPeersUpdateTime':rcNtpPeersUpdateTime,'rcNtpPeersReach':rcNtpPeersReach,'rcNtpPeersTimer':rcNtpPeersTimer,'rcNtpPeersOffset':rcNtpPeersOffset,'rcNtpPeersDelay':rcNtpPeersDelay,'rcNtpPeersDispersion':rcNtpPeersDispersion,'rcNtpPeersFilterValidEntries':rcNtpPeersFilterValidEntries,'rcNtpPeersEntryStatus':rcNtpPeersEntryStatus,'rcNtpPeersVersion':rcNtpPeersVersion,'rcNtpFilter':rcNtpFilter,'rcNtpFilterRegisterTable':rcNtpFilterRegisterTable,'rcNtpFilterRegisterEntry':rcNtpFilterRegisterEntry,_K:rcNtpFilterIndex,'rcNtpFilterPeersOffset':rcNtpFilterPeersOffset,'rcNtpFilterPeersDelay':rcNtpFilterPeersDelay,'rcNtpFilterPeersDispersion':rcNtpFilterPeersDispersion})