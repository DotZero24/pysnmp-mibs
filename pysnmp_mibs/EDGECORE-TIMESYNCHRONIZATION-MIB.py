_i='rlSntpServerInetAddress'
_h='rlSntpServerInetAddressType'
_g='rlSntpAnycastInetIfIndex'
_f='rlSntpBroadcastInetIfIndex'
_e='rlSntpAuthenticationKeyID'
_d='rlSntpServerAddress'
_c='rlSntpAnycastIfIndex'
_b='receiveSend'
_a='receive'
_Z='rlSntpBroadcastIfIndex'
_Y='rlSntpNtpConfigSrvEntryType'
_X='RlSntpNtpSyncType'
_W='rlTimeZoneIndex'
_V='anycast'
_U='unicast'
_T='Unsigned32'
_S='RlDaylightSavingTimeMode'
_R='RlTimeSyncMethod'
_Q='OctetString'
_P='down'
_O='up'
_N='inProcess'
_M='unknown'
_L='disabled'
_K='enabled'
_J='none'
_I='not-accessible'
_H='TruthValue'
_G='EDGECORE-TIMESYNCHRONIZATION-MIB'
_F='seconds'
_E='DisplayString'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_Q,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rnd,=mibBuilder.importSymbols('EDGECORE-MIB','rnd')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_T,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention',_H)
rlTimeSynchronization=ModuleIdentity((1,3,6,1,4,1,259,10,1,14,89,92))
if mibBuilder.loadTexts:rlTimeSynchronization.setRevisions(('2009-06-18 00:24','2007-09-06 00:24','2003-11-23 00:24'))
class NTPTimeStamp(TextualConvention,OctetString):status=_A;displayHint='4d.4d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class NTPSignedTimeValue(TextualConvention,OctetString):status=_A;displayHint='2d.2d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class NTPStratum(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class RlTimeSyncMethod(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('sntp',2),('ntp',3)))
class RlDaylightSavingTimeMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('recurring',1),('date',2),(_J,3)))
class RlSntpNtpSyncType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_U,2),(_V,3),('broadcast',4)))
class RlSntpNtpSyncEntryType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primaryPollSrv',1),('syncSrv',2)))
_RlTimeSyncMethodMode_ObjectIdentity=ObjectIdentity
rlTimeSyncMethodMode=_RlTimeSyncMethodMode_ObjectIdentity((1,3,6,1,4,1,259,10,1,14,89,92,1))
_RlTimeSyncMibVersion_Type=Integer32
_RlTimeSyncMibVersion_Object=MibScalar
rlTimeSyncMibVersion=_RlTimeSyncMibVersion_Object((1,3,6,1,4,1,259,10,1,14,89,92,1,1),_RlTimeSyncMibVersion_Type())
rlTimeSyncMibVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:rlTimeSyncMibVersion.setStatus(_A)
class _RndTimeSyncManagedTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_RndTimeSyncManagedTime_Type.__name__=_E
_RndTimeSyncManagedTime_Object=MibScalar
rndTimeSyncManagedTime=_RndTimeSyncManagedTime_Object((1,3,6,1,4,1,259,10,1,14,89,92,1,2),_RndTimeSyncManagedTime_Type())
rndTimeSyncManagedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rndTimeSyncManagedTime.setStatus(_A)
class _RndTimeSyncManagedDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_RndTimeSyncManagedDate_Type.__name__=_E
_RndTimeSyncManagedDate_Object=MibScalar
rndTimeSyncManagedDate=_RndTimeSyncManagedDate_Object((1,3,6,1,4,1,259,10,1,14,89,92,1,3),_RndTimeSyncManagedDate_Type())
rndTimeSyncManagedDate.setMaxAccess(_C)
if mibBuilder.loadTexts:rndTimeSyncManagedDate.setStatus(_A)
class _RndTimeSyncManagedDateTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
_RndTimeSyncManagedDateTime_Type.__name__=_E
_RndTimeSyncManagedDateTime_Object=MibScalar
rndTimeSyncManagedDateTime=_RndTimeSyncManagedDateTime_Object((1,3,6,1,4,1,259,10,1,14,89,92,1,4),_RndTimeSyncManagedDateTime_Type())
rndTimeSyncManagedDateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rndTimeSyncManagedDateTime.setStatus(_A)
class _RlTimeSyncMethod_Type(RlTimeSyncMethod):defaultValue=1
_RlTimeSyncMethod_Type.__name__=_R
_RlTimeSyncMethod_Object=MibScalar
rlTimeSyncMethod=_RlTimeSyncMethod_Object((1,3,6,1,4,1,259,10,1,14,89,92,1,5),_RlTimeSyncMethod_Type())
rlTimeSyncMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:rlTimeSyncMethod.setStatus(_A)
class _RlTimeZone_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,6))
_RlTimeZone_Type.__name__=_E
_RlTimeZone_Object=MibScalar
rlTimeZone=_RlTimeZone_Object((1,3,6,1,4,1,259,10,1,14,89,92,1,6),_RlTimeZone_Type())
rlTimeZone.setMaxAccess(_C)
if mibBuilder.loadTexts:rlTimeZone.setStatus(_A)
class _RlTimeZoneCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_RlTimeZoneCode_Type.__name__=_E
_RlTimeZoneCode_Object=MibScalar
rlTimeZoneCode=_RlTimeZoneCode_Object((1,3,6,1,4,1,259,10,1,14,89,92,1,7),_RlTimeZoneCode_Type())
rlTimeZoneCode.setMaxAccess(_C)
if mibBuilder.loadTexts:rlTimeZoneCode.setStatus(_A)
class _RlDaylightSavingTimeMode_Type(RlDaylightSavingTimeMode):defaultValue=3
_RlDaylightSavingTimeMode_Type.__name__=_S
_RlDaylightSavingTimeMode_Object=MibScalar
rlDaylightSavingTimeMode=_RlDaylightSavingTimeMode_Object((1,3,6,1,4,1,259,10,1,14,89,92,1,8),_RlDaylightSavingTimeMode_Type())
rlDaylightSavingTimeMode.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDaylightSavingTimeMode.setStatus(_A)
class _RlDaylightSavingTimeStart_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(14,14));fixedLength=14
_RlDaylightSavingTimeStart_Type.__name__=_Q
_RlDaylightSavingTimeStart_Object=MibScalar
rlDaylightSavingTimeStart=_RlDaylightSavingTimeStart_Object((1,3,6,1,4,1,259,10,1,14,89,92,1,9),_RlDaylightSavingTimeStart_Type())
rlDaylightSavingTimeStart.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDaylightSavingTimeStart.setStatus(_A)
class _RlDaylightSavingTimeEnd_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(14,14));fixedLength=14
_RlDaylightSavingTimeEnd_Type.__name__=_Q
_RlDaylightSavingTimeEnd_Object=MibScalar
rlDaylightSavingTimeEnd=_RlDaylightSavingTimeEnd_Object((1,3,6,1,4,1,259,10,1,14,89,92,1,10),_RlDaylightSavingTimeEnd_Type())
rlDaylightSavingTimeEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDaylightSavingTimeEnd.setStatus(_A)
class _RlDaylightSavingTimeOffset_Type(Integer32):defaultValue=60
_RlDaylightSavingTimeOffset_Type.__name__=_D
_RlDaylightSavingTimeOffset_Object=MibScalar
rlDaylightSavingTimeOffset=_RlDaylightSavingTimeOffset_Object((1,3,6,1,4,1,259,10,1,14,89,92,1,11),_RlDaylightSavingTimeOffset_Type())
rlDaylightSavingTimeOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDaylightSavingTimeOffset.setStatus(_A)
class _RlDaylightSavingTimeCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_RlDaylightSavingTimeCode_Type.__name__=_E
_RlDaylightSavingTimeCode_Object=MibScalar
rlDaylightSavingTimeCode=_RlDaylightSavingTimeCode_Object((1,3,6,1,4,1,259,10,1,14,89,92,1,12),_RlDaylightSavingTimeCode_Type())
rlDaylightSavingTimeCode.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDaylightSavingTimeCode.setStatus(_A)
_RlTZDSTOffset_Type=Integer32
_RlTZDSTOffset_Object=MibScalar
rlTZDSTOffset=_RlTZDSTOffset_Object((1,3,6,1,4,1,259,10,1,14,89,92,1,13),_RlTZDSTOffset_Type())
rlTZDSTOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:rlTZDSTOffset.setStatus(_A)
class _RlTimeZoneName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_RlTimeZoneName_Type.__name__=_E
_RlTimeZoneName_Object=MibScalar
rlTimeZoneName=_RlTimeZoneName_Object((1,3,6,1,4,1,259,10,1,14,89,92,1,14),_RlTimeZoneName_Type())
rlTimeZoneName.setMaxAccess(_C)
if mibBuilder.loadTexts:rlTimeZoneName.setStatus(_A)
_RlTimeZoneTable_Object=MibTable
rlTimeZoneTable=_RlTimeZoneTable_Object((1,3,6,1,4,1,259,10,1,14,89,92,1,15))
if mibBuilder.loadTexts:rlTimeZoneTable.setStatus(_A)
_RlTimeZoneEntry_Object=MibTableRow
rlTimeZoneEntry=_RlTimeZoneEntry_Object((1,3,6,1,4,1,259,10,1,14,89,92,1,15,1))
rlTimeZoneEntry.setIndexNames((0,_G,_W))
if mibBuilder.loadTexts:rlTimeZoneEntry.setStatus(_A)
class _RlTimeZoneIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_RlTimeZoneIndex_Type.__name__=_D
_RlTimeZoneIndex_Object=MibTableColumn
rlTimeZoneIndex=_RlTimeZoneIndex_Object((1,3,6,1,4,1,259,10,1,14,89,92,1,15,1,1),_RlTimeZoneIndex_Type())
rlTimeZoneIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:rlTimeZoneIndex.setStatus(_A)
class _RlTimeZoneTimeSyncMethod_Type(RlTimeSyncMethod):defaultValue=1
_RlTimeZoneTimeSyncMethod_Type.__name__=_R
_RlTimeZoneTimeSyncMethod_Object=MibTableColumn
rlTimeZoneTimeSyncMethod=_RlTimeZoneTimeSyncMethod_Object((1,3,6,1,4,1,259,10,1,14,89,92,1,15,1,2),_RlTimeZoneTimeSyncMethod_Type())
rlTimeZoneTimeSyncMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:rlTimeZoneTimeSyncMethod.setStatus(_A)
class _RlTimeZoneTimeZoneOffset_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,6))
_RlTimeZoneTimeZoneOffset_Type.__name__=_E
_RlTimeZoneTimeZoneOffset_Object=MibTableColumn
rlTimeZoneTimeZoneOffset=_RlTimeZoneTimeZoneOffset_Object((1,3,6,1,4,1,259,10,1,14,89,92,1,15,1,3),_RlTimeZoneTimeZoneOffset_Type())
rlTimeZoneTimeZoneOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:rlTimeZoneTimeZoneOffset.setStatus(_A)
class _RlTimeZoneTimeZoneCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_RlTimeZoneTimeZoneCode_Type.__name__=_E
_RlTimeZoneTimeZoneCode_Object=MibTableColumn
rlTimeZoneTimeZoneCode=_RlTimeZoneTimeZoneCode_Object((1,3,6,1,4,1,259,10,1,14,89,92,1,15,1,4),_RlTimeZoneTimeZoneCode_Type())
rlTimeZoneTimeZoneCode.setMaxAccess(_C)
if mibBuilder.loadTexts:rlTimeZoneTimeZoneCode.setStatus(_A)
class _RlTimeZoneDaylightSavingTimeMode_Type(RlDaylightSavingTimeMode):defaultValue=3
_RlTimeZoneDaylightSavingTimeMode_Type.__name__=_S
_RlTimeZoneDaylightSavingTimeMode_Object=MibTableColumn
rlTimeZoneDaylightSavingTimeMode=_RlTimeZoneDaylightSavingTimeMode_Object((1,3,6,1,4,1,259,10,1,14,89,92,1,15,1,5),_RlTimeZoneDaylightSavingTimeMode_Type())
rlTimeZoneDaylightSavingTimeMode.setMaxAccess(_C)
if mibBuilder.loadTexts:rlTimeZoneDaylightSavingTimeMode.setStatus(_A)
class _RlTimeZoneDaylightSavingTimeStart_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(14,14));fixedLength=14
_RlTimeZoneDaylightSavingTimeStart_Type.__name__=_Q
_RlTimeZoneDaylightSavingTimeStart_Object=MibTableColumn
rlTimeZoneDaylightSavingTimeStart=_RlTimeZoneDaylightSavingTimeStart_Object((1,3,6,1,4,1,259,10,1,14,89,92,1,15,1,6),_RlTimeZoneDaylightSavingTimeStart_Type())
rlTimeZoneDaylightSavingTimeStart.setMaxAccess(_C)
if mibBuilder.loadTexts:rlTimeZoneDaylightSavingTimeStart.setStatus(_A)
class _RlTimeZoneDaylightSavingTimeEnd_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(14,14));fixedLength=14
_RlTimeZoneDaylightSavingTimeEnd_Type.__name__=_Q
_RlTimeZoneDaylightSavingTimeEnd_Object=MibTableColumn
rlTimeZoneDaylightSavingTimeEnd=_RlTimeZoneDaylightSavingTimeEnd_Object((1,3,6,1,4,1,259,10,1,14,89,92,1,15,1,7),_RlTimeZoneDaylightSavingTimeEnd_Type())
rlTimeZoneDaylightSavingTimeEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:rlTimeZoneDaylightSavingTimeEnd.setStatus(_A)
class _RlTimeZoneDaylightSavingTimeOffset_Type(Integer32):defaultValue=60
_RlTimeZoneDaylightSavingTimeOffset_Type.__name__=_D
_RlTimeZoneDaylightSavingTimeOffset_Object=MibTableColumn
rlTimeZoneDaylightSavingTimeOffset=_RlTimeZoneDaylightSavingTimeOffset_Object((1,3,6,1,4,1,259,10,1,14,89,92,1,15,1,8),_RlTimeZoneDaylightSavingTimeOffset_Type())
rlTimeZoneDaylightSavingTimeOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:rlTimeZoneDaylightSavingTimeOffset.setStatus(_A)
class _RlTimeZoneDaylightSavingTimeCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_RlTimeZoneDaylightSavingTimeCode_Type.__name__=_E
_RlTimeZoneDaylightSavingTimeCode_Object=MibTableColumn
rlTimeZoneDaylightSavingTimeCode=_RlTimeZoneDaylightSavingTimeCode_Object((1,3,6,1,4,1,259,10,1,14,89,92,1,15,1,9),_RlTimeZoneDaylightSavingTimeCode_Type())
rlTimeZoneDaylightSavingTimeCode.setMaxAccess(_C)
if mibBuilder.loadTexts:rlTimeZoneDaylightSavingTimeCode.setStatus(_A)
_RlTimeZoneTZDSTOffset_Type=Integer32
_RlTimeZoneTZDSTOffset_Object=MibTableColumn
rlTimeZoneTZDSTOffset=_RlTimeZoneTZDSTOffset_Object((1,3,6,1,4,1,259,10,1,14,89,92,1,15,1,10),_RlTimeZoneTZDSTOffset_Type())
rlTimeZoneTZDSTOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:rlTimeZoneTZDSTOffset.setStatus(_A)
class _RlTimeZoneTimeZoneName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_RlTimeZoneTimeZoneName_Type.__name__=_E
_RlTimeZoneTimeZoneName_Object=MibTableColumn
rlTimeZoneTimeZoneName=_RlTimeZoneTimeZoneName_Object((1,3,6,1,4,1,259,10,1,14,89,92,1,15,1,11),_RlTimeZoneTimeZoneName_Type())
rlTimeZoneTimeZoneName.setMaxAccess(_C)
if mibBuilder.loadTexts:rlTimeZoneTimeZoneName.setStatus(_A)
class _RlTimeZoneDataType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('dynamic',2)))
_RlTimeZoneDataType_Type.__name__=_D
_RlTimeZoneDataType_Object=MibTableColumn
rlTimeZoneDataType=_RlTimeZoneDataType_Object((1,3,6,1,4,1,259,10,1,14,89,92,1,15,1,12),_RlTimeZoneDataType_Type())
rlTimeZoneDataType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlTimeZoneDataType.setStatus(_A)
class _RlTimeZoneDataSourceIfIndex_Type(Integer32):defaultValue=0
_RlTimeZoneDataSourceIfIndex_Type.__name__=_D
_RlTimeZoneDataSourceIfIndex_Object=MibTableColumn
rlTimeZoneDataSourceIfIndex=_RlTimeZoneDataSourceIfIndex_Object((1,3,6,1,4,1,259,10,1,14,89,92,1,15,1,13),_RlTimeZoneDataSourceIfIndex_Type())
rlTimeZoneDataSourceIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rlTimeZoneDataSourceIfIndex.setStatus(_A)
class _RlClockStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('invalid',1),('manuallySet',2),('synchronizedBySntp',3)))
_RlClockStatus_Type.__name__=_D
_RlClockStatus_Object=MibScalar
rlClockStatus=_RlClockStatus_Object((1,3,6,1,4,1,259,10,1,14,89,92,1,16),_RlClockStatus_Type())
rlClockStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlClockStatus.setStatus(_A)
_RlDhcpTimezoneOptionEnabled_Type=TruthValue
_RlDhcpTimezoneOptionEnabled_Object=MibScalar
rlDhcpTimezoneOptionEnabled=_RlDhcpTimezoneOptionEnabled_Object((1,3,6,1,4,1,259,10,1,14,89,92,1,17),_RlDhcpTimezoneOptionEnabled_Type())
rlDhcpTimezoneOptionEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpTimezoneOptionEnabled.setStatus(_A)
class _RlAutomaticClockSetFromPCEnabled_Type(TruthValue):defaultValue=2
_RlAutomaticClockSetFromPCEnabled_Type.__name__=_H
_RlAutomaticClockSetFromPCEnabled_Object=MibScalar
rlAutomaticClockSetFromPCEnabled=_RlAutomaticClockSetFromPCEnabled_Object((1,3,6,1,4,1,259,10,1,14,89,92,1,18),_RlAutomaticClockSetFromPCEnabled_Type())
rlAutomaticClockSetFromPCEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:rlAutomaticClockSetFromPCEnabled.setStatus(_A)
_RlTimeAndDateHaveBeenSet_Type=TruthValue
_RlTimeAndDateHaveBeenSet_Object=MibScalar
rlTimeAndDateHaveBeenSet=_RlTimeAndDateHaveBeenSet_Object((1,3,6,1,4,1,259,10,1,14,89,92,1,19),_RlTimeAndDateHaveBeenSet_Type())
rlTimeAndDateHaveBeenSet.setMaxAccess(_B)
if mibBuilder.loadTexts:rlTimeAndDateHaveBeenSet.setStatus(_A)
_RlSntpNtpClient_ObjectIdentity=ObjectIdentity
rlSntpNtpClient=_RlSntpNtpClient_ObjectIdentity((1,3,6,1,4,1,259,10,1,14,89,92,2))
_RlSntpNtpConfig_ObjectIdentity=ObjectIdentity
rlSntpNtpConfig=_RlSntpNtpConfig_ObjectIdentity((1,3,6,1,4,1,259,10,1,14,89,92,2,1))
_RlSntpNtpMibVersion_Type=Integer32
_RlSntpNtpMibVersion_Object=MibScalar
rlSntpNtpMibVersion=_RlSntpNtpMibVersion_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,1,1),_RlSntpNtpMibVersion_Type())
rlSntpNtpMibVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpNtpMibVersion.setStatus(_A)
class _RlSntpNtpConfigMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_J,1),(_U,2),(_V,3),('multicast',4),('unicastAnycast',5),('unicastMulticast',6),('anycastMulticast',7),('unicastAnycastMulticast',8)))
_RlSntpNtpConfigMode_Type.__name__=_D
_RlSntpNtpConfigMode_Object=MibScalar
rlSntpNtpConfigMode=_RlSntpNtpConfigMode_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,1,2),_RlSntpNtpConfigMode_Type())
rlSntpNtpConfigMode.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpNtpConfigMode.setStatus(_A)
_RlSntpNtpConfigSysStratum_Type=NTPStratum
_RlSntpNtpConfigSysStratum_Object=MibScalar
rlSntpNtpConfigSysStratum=_RlSntpNtpConfigSysStratum_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,1,3),_RlSntpNtpConfigSysStratum_Type())
rlSntpNtpConfigSysStratum.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpNtpConfigSysStratum.setStatus(_A)
class _RlSntpNtpConfigPollInterval_Type(Integer32):defaultValue=1024
_RlSntpNtpConfigPollInterval_Type.__name__=_D
_RlSntpNtpConfigPollInterval_Object=MibScalar
rlSntpNtpConfigPollInterval=_RlSntpNtpConfigPollInterval_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,1,4),_RlSntpNtpConfigPollInterval_Type())
rlSntpNtpConfigPollInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSntpNtpConfigPollInterval.setStatus(_A)
_RlSntpNtpConfigPrimaryPollSrvAddr_Type=IpAddress
_RlSntpNtpConfigPrimaryPollSrvAddr_Object=MibScalar
rlSntpNtpConfigPrimaryPollSrvAddr=_RlSntpNtpConfigPrimaryPollSrvAddr_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,1,5),_RlSntpNtpConfigPrimaryPollSrvAddr_Type())
rlSntpNtpConfigPrimaryPollSrvAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpNtpConfigPrimaryPollSrvAddr.setStatus(_A)
_RlSntpNtpConfigPrimaryPollSrvMrid_Type=Integer32
_RlSntpNtpConfigPrimaryPollSrvMrid_Object=MibScalar
rlSntpNtpConfigPrimaryPollSrvMrid=_RlSntpNtpConfigPrimaryPollSrvMrid_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,1,6),_RlSntpNtpConfigPrimaryPollSrvMrid_Type())
rlSntpNtpConfigPrimaryPollSrvMrid.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpNtpConfigPrimaryPollSrvMrid.setStatus(_A)
_RlSntpNtpConfigPrimaryPollSrvIfIndex_Type=Integer32
_RlSntpNtpConfigPrimaryPollSrvIfIndex_Object=MibScalar
rlSntpNtpConfigPrimaryPollSrvIfIndex=_RlSntpNtpConfigPrimaryPollSrvIfIndex_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,1,7),_RlSntpNtpConfigPrimaryPollSrvIfIndex_Type())
rlSntpNtpConfigPrimaryPollSrvIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpNtpConfigPrimaryPollSrvIfIndex.setStatus(_A)
_RlSntpNtpConfigPrimaryPollSrvStratum_Type=NTPStratum
_RlSntpNtpConfigPrimaryPollSrvStratum_Object=MibScalar
rlSntpNtpConfigPrimaryPollSrvStratum=_RlSntpNtpConfigPrimaryPollSrvStratum_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,1,8),_RlSntpNtpConfigPrimaryPollSrvStratum_Type())
rlSntpNtpConfigPrimaryPollSrvStratum.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpNtpConfigPrimaryPollSrvStratum.setStatus(_A)
_RlSntpNtpConfigSyncSrvAddr_Type=IpAddress
_RlSntpNtpConfigSyncSrvAddr_Object=MibScalar
rlSntpNtpConfigSyncSrvAddr=_RlSntpNtpConfigSyncSrvAddr_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,1,9),_RlSntpNtpConfigSyncSrvAddr_Type())
rlSntpNtpConfigSyncSrvAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpNtpConfigSyncSrvAddr.setStatus(_A)
_RlSntpNtpConfigSyncSrvMrid_Type=Integer32
_RlSntpNtpConfigSyncSrvMrid_Object=MibScalar
rlSntpNtpConfigSyncSrvMrid=_RlSntpNtpConfigSyncSrvMrid_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,1,10),_RlSntpNtpConfigSyncSrvMrid_Type())
rlSntpNtpConfigSyncSrvMrid.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpNtpConfigSyncSrvMrid.setStatus(_A)
_RlSntpNtpConfigSyncSrvIfIndex_Type=Integer32
_RlSntpNtpConfigSyncSrvIfIndex_Object=MibScalar
rlSntpNtpConfigSyncSrvIfIndex=_RlSntpNtpConfigSyncSrvIfIndex_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,1,11),_RlSntpNtpConfigSyncSrvIfIndex_Type())
rlSntpNtpConfigSyncSrvIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpNtpConfigSyncSrvIfIndex.setStatus(_A)
class _RlSntpNtpConfigSyncSrvType_Type(RlSntpNtpSyncType):defaultValue=1
_RlSntpNtpConfigSyncSrvType_Type.__name__=_X
_RlSntpNtpConfigSyncSrvType_Object=MibScalar
rlSntpNtpConfigSyncSrvType=_RlSntpNtpConfigSyncSrvType_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,1,12),_RlSntpNtpConfigSyncSrvType_Type())
rlSntpNtpConfigSyncSrvType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpNtpConfigSyncSrvType.setStatus(_A)
_RlSntpNtpConfigSyncSrvStratum_Type=NTPStratum
_RlSntpNtpConfigSyncSrvStratum_Object=MibScalar
rlSntpNtpConfigSyncSrvStratum=_RlSntpNtpConfigSyncSrvStratum_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,1,13),_RlSntpNtpConfigSyncSrvStratum_Type())
rlSntpNtpConfigSyncSrvStratum.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpNtpConfigSyncSrvStratum.setStatus(_A)
_RlSntpNtpConfigRetryTimeout_Type=Integer32
_RlSntpNtpConfigRetryTimeout_Object=MibScalar
rlSntpNtpConfigRetryTimeout=_RlSntpNtpConfigRetryTimeout_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,1,14),_RlSntpNtpConfigRetryTimeout_Type())
rlSntpNtpConfigRetryTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpNtpConfigRetryTimeout.setStatus(_A)
_RlSntpNtpConfigRetryCnt_Type=Integer32
_RlSntpNtpConfigRetryCnt_Object=MibScalar
rlSntpNtpConfigRetryCnt=_RlSntpNtpConfigRetryCnt_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,1,15),_RlSntpNtpConfigRetryCnt_Type())
rlSntpNtpConfigRetryCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpNtpConfigRetryCnt.setStatus(_A)
_RlSntpNtpConfigSrvTable_Object=MibTable
rlSntpNtpConfigSrvTable=_RlSntpNtpConfigSrvTable_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,1,16))
if mibBuilder.loadTexts:rlSntpNtpConfigSrvTable.setStatus(_A)
_RlSntpNtpConfigSrvEntry_Object=MibTableRow
rlSntpNtpConfigSrvEntry=_RlSntpNtpConfigSrvEntry_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,1,16,1))
rlSntpNtpConfigSrvEntry.setIndexNames((0,_G,_Y))
if mibBuilder.loadTexts:rlSntpNtpConfigSrvEntry.setStatus(_A)
_RlSntpNtpConfigSrvEntryType_Type=RlSntpNtpSyncEntryType
_RlSntpNtpConfigSrvEntryType_Object=MibTableColumn
rlSntpNtpConfigSrvEntryType=_RlSntpNtpConfigSrvEntryType_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,1,16,1,1),_RlSntpNtpConfigSrvEntryType_Type())
rlSntpNtpConfigSrvEntryType.setMaxAccess(_I)
if mibBuilder.loadTexts:rlSntpNtpConfigSrvEntryType.setStatus(_A)
_RlSntpNtpConfigSrvInetAddressType_Type=InetAddressType
_RlSntpNtpConfigSrvInetAddressType_Object=MibTableColumn
rlSntpNtpConfigSrvInetAddressType=_RlSntpNtpConfigSrvInetAddressType_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,1,16,1,2),_RlSntpNtpConfigSrvInetAddressType_Type())
rlSntpNtpConfigSrvInetAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpNtpConfigSrvInetAddressType.setStatus(_A)
_RlSntpNtpConfigSrvInetAddress_Type=InetAddress
_RlSntpNtpConfigSrvInetAddress_Object=MibTableColumn
rlSntpNtpConfigSrvInetAddress=_RlSntpNtpConfigSrvInetAddress_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,1,16,1,3),_RlSntpNtpConfigSrvInetAddress_Type())
rlSntpNtpConfigSrvInetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpNtpConfigSrvInetAddress.setStatus(_A)
_RlSntpNtpConfigSrvMrid_Type=Integer32
_RlSntpNtpConfigSrvMrid_Object=MibTableColumn
rlSntpNtpConfigSrvMrid=_RlSntpNtpConfigSrvMrid_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,1,16,1,4),_RlSntpNtpConfigSrvMrid_Type())
rlSntpNtpConfigSrvMrid.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpNtpConfigSrvMrid.setStatus(_A)
_RlSntpNtpConfigSrvIfIndex_Type=Integer32
_RlSntpNtpConfigSrvIfIndex_Object=MibTableColumn
rlSntpNtpConfigSrvIfIndex=_RlSntpNtpConfigSrvIfIndex_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,1,16,1,5),_RlSntpNtpConfigSrvIfIndex_Type())
rlSntpNtpConfigSrvIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpNtpConfigSrvIfIndex.setStatus(_A)
_RlSntpNtpConfigSrvSyncType_Type=RlSntpNtpSyncType
_RlSntpNtpConfigSrvSyncType_Object=MibTableColumn
rlSntpNtpConfigSrvSyncType=_RlSntpNtpConfigSrvSyncType_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,1,16,1,6),_RlSntpNtpConfigSrvSyncType_Type())
rlSntpNtpConfigSrvSyncType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpNtpConfigSrvSyncType.setStatus(_A)
_RlSntpNtpConfigSrvStratum_Type=NTPStratum
_RlSntpNtpConfigSrvStratum_Object=MibTableColumn
rlSntpNtpConfigSrvStratum=_RlSntpNtpConfigSrvStratum_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,1,16,1,7),_RlSntpNtpConfigSrvStratum_Type())
rlSntpNtpConfigSrvStratum.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpNtpConfigSrvStratum.setStatus(_A)
_RlSntpConfig_ObjectIdentity=ObjectIdentity
rlSntpConfig=_RlSntpConfig_ObjectIdentity((1,3,6,1,4,1,259,10,1,14,89,92,2,2))
class _RlSntpClientMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('active',2),('passive',3)))
_RlSntpClientMode_Type.__name__=_D
_RlSntpClientMode_Object=MibScalar
rlSntpClientMode=_RlSntpClientMode_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,1),_RlSntpClientMode_Type())
rlSntpClientMode.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpClientMode.setStatus(_A)
class _RlSntpUnicastAdminState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_RlSntpUnicastAdminState_Type.__name__=_D
_RlSntpUnicastAdminState_Object=MibScalar
rlSntpUnicastAdminState=_RlSntpUnicastAdminState_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,2),_RlSntpUnicastAdminState_Type())
rlSntpUnicastAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSntpUnicastAdminState.setStatus(_A)
class _RlSntpBroadcastAdminState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_RlSntpBroadcastAdminState_Type.__name__=_D
_RlSntpBroadcastAdminState_Object=MibScalar
rlSntpBroadcastAdminState=_RlSntpBroadcastAdminState_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,3),_RlSntpBroadcastAdminState_Type())
rlSntpBroadcastAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSntpBroadcastAdminState.setStatus(_A)
class _RlSntpAnycastAdminState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_RlSntpAnycastAdminState_Type.__name__=_D
_RlSntpAnycastAdminState_Object=MibScalar
rlSntpAnycastAdminState=_RlSntpAnycastAdminState_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,4),_RlSntpAnycastAdminState_Type())
rlSntpAnycastAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSntpAnycastAdminState.setStatus(_A)
class _RlSntpUnicastPollState_Type(TruthValue):defaultValue=2
_RlSntpUnicastPollState_Type.__name__=_H
_RlSntpUnicastPollState_Object=MibScalar
rlSntpUnicastPollState=_RlSntpUnicastPollState_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,5),_RlSntpUnicastPollState_Type())
rlSntpUnicastPollState.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSntpUnicastPollState.setStatus(_A)
class _RlSntpBroadcastPollState_Type(TruthValue):defaultValue=2
_RlSntpBroadcastPollState_Type.__name__=_H
_RlSntpBroadcastPollState_Object=MibScalar
rlSntpBroadcastPollState=_RlSntpBroadcastPollState_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,6),_RlSntpBroadcastPollState_Type())
rlSntpBroadcastPollState.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSntpBroadcastPollState.setStatus(_A)
class _RlSntpAnycastPollState_Type(TruthValue):defaultValue=2
_RlSntpAnycastPollState_Type.__name__=_H
_RlSntpAnycastPollState_Object=MibScalar
rlSntpAnycastPollState=_RlSntpAnycastPollState_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,7),_RlSntpAnycastPollState_Type())
rlSntpAnycastPollState.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSntpAnycastPollState.setStatus(_A)
class _RlSntpAuthenticationState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_RlSntpAuthenticationState_Type.__name__=_D
_RlSntpAuthenticationState_Object=MibScalar
rlSntpAuthenticationState=_RlSntpAuthenticationState_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,8),_RlSntpAuthenticationState_Type())
rlSntpAuthenticationState.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSntpAuthenticationState.setStatus(_A)
class _RlTimeValidFlag_Type(TruthValue):defaultValue=2
_RlTimeValidFlag_Type.__name__=_H
_RlTimeValidFlag_Object=MibScalar
rlTimeValidFlag=_RlTimeValidFlag_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,9),_RlTimeValidFlag_Type())
rlTimeValidFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:rlTimeValidFlag.setStatus(_A)
_RlSntpConfigBroadcastTable_Object=MibTable
rlSntpConfigBroadcastTable=_RlSntpConfigBroadcastTable_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,10))
if mibBuilder.loadTexts:rlSntpConfigBroadcastTable.setStatus(_A)
_RlSntpBroadcastEntry_Object=MibTableRow
rlSntpBroadcastEntry=_RlSntpBroadcastEntry_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,10,1))
rlSntpBroadcastEntry.setIndexNames((0,_G,_Z))
if mibBuilder.loadTexts:rlSntpBroadcastEntry.setStatus(_A)
_RlSntpBroadcastIfIndex_Type=Integer32
_RlSntpBroadcastIfIndex_Object=MibTableColumn
rlSntpBroadcastIfIndex=_RlSntpBroadcastIfIndex_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,10,1,1),_RlSntpBroadcastIfIndex_Type())
rlSntpBroadcastIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:rlSntpBroadcastIfIndex.setStatus(_A)
class _RlSntpBroadcastIfAdminState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_RlSntpBroadcastIfAdminState_Type.__name__=_D
_RlSntpBroadcastIfAdminState_Object=MibTableColumn
rlSntpBroadcastIfAdminState=_RlSntpBroadcastIfAdminState_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,10,1,2),_RlSntpBroadcastIfAdminState_Type())
rlSntpBroadcastIfAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSntpBroadcastIfAdminState.setStatus(_A)
class _RlSntpBroadcastMode_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_a,2),('send',3),(_b,4)))
_RlSntpBroadcastMode_Type.__name__=_D
_RlSntpBroadcastMode_Object=MibTableColumn
rlSntpBroadcastMode=_RlSntpBroadcastMode_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,10,1,3),_RlSntpBroadcastMode_Type())
rlSntpBroadcastMode.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSntpBroadcastMode.setStatus(_A)
class _RlSntpBroadcastPolled_Type(TruthValue):defaultValue=2
_RlSntpBroadcastPolled_Type.__name__=_H
_RlSntpBroadcastPolled_Object=MibTableColumn
rlSntpBroadcastPolled=_RlSntpBroadcastPolled_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,10,1,4),_RlSntpBroadcastPolled_Type())
rlSntpBroadcastPolled.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSntpBroadcastPolled.setStatus(_A)
_RlSntpBroadcastAddress_Type=IpAddress
_RlSntpBroadcastAddress_Object=MibTableColumn
rlSntpBroadcastAddress=_RlSntpBroadcastAddress_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,10,1,5),_RlSntpBroadcastAddress_Type())
rlSntpBroadcastAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpBroadcastAddress.setStatus(_A)
_RlSntpBroadcastStratum_Type=NTPStratum
_RlSntpBroadcastStratum_Object=MibTableColumn
rlSntpBroadcastStratum=_RlSntpBroadcastStratum_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,10,1,6),_RlSntpBroadcastStratum_Type())
rlSntpBroadcastStratum.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpBroadcastStratum.setStatus(_A)
_RlSntpBroadcastLastResp_Type=NTPTimeStamp
_RlSntpBroadcastLastResp_Object=MibTableColumn
rlSntpBroadcastLastResp=_RlSntpBroadcastLastResp_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,10,1,7),_RlSntpBroadcastLastResp_Type())
rlSntpBroadcastLastResp.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpBroadcastLastResp.setStatus(_A)
class _RlSntpBroadcastStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3),(_P,4)))
_RlSntpBroadcastStatus_Type.__name__=_D
_RlSntpBroadcastStatus_Object=MibTableColumn
rlSntpBroadcastStatus=_RlSntpBroadcastStatus_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,10,1,8),_RlSntpBroadcastStatus_Type())
rlSntpBroadcastStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpBroadcastStatus.setStatus(_A)
_RlSntpBroadcastOffset_Type=NTPTimeStamp
_RlSntpBroadcastOffset_Object=MibTableColumn
rlSntpBroadcastOffset=_RlSntpBroadcastOffset_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,10,1,9),_RlSntpBroadcastOffset_Type())
rlSntpBroadcastOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpBroadcastOffset.setStatus(_A)
if mibBuilder.loadTexts:rlSntpBroadcastOffset.setUnits(_F)
_RlSntpBroadcastDelay_Type=NTPSignedTimeValue
_RlSntpBroadcastDelay_Object=MibTableColumn
rlSntpBroadcastDelay=_RlSntpBroadcastDelay_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,10,1,10),_RlSntpBroadcastDelay_Type())
rlSntpBroadcastDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpBroadcastDelay.setStatus(_A)
if mibBuilder.loadTexts:rlSntpBroadcastDelay.setUnits(_F)
_RlSntpBroadcastRowStatus_Type=RowStatus
_RlSntpBroadcastRowStatus_Object=MibTableColumn
rlSntpBroadcastRowStatus=_RlSntpBroadcastRowStatus_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,10,1,11),_RlSntpBroadcastRowStatus_Type())
rlSntpBroadcastRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSntpBroadcastRowStatus.setStatus(_A)
_RlSntpConfigAnycastTable_Object=MibTable
rlSntpConfigAnycastTable=_RlSntpConfigAnycastTable_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,11))
if mibBuilder.loadTexts:rlSntpConfigAnycastTable.setStatus(_A)
_RlSntpAnycastEntry_Object=MibTableRow
rlSntpAnycastEntry=_RlSntpAnycastEntry_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,11,1))
rlSntpAnycastEntry.setIndexNames((0,_G,_c))
if mibBuilder.loadTexts:rlSntpAnycastEntry.setStatus(_A)
_RlSntpAnycastIfIndex_Type=Integer32
_RlSntpAnycastIfIndex_Object=MibTableColumn
rlSntpAnycastIfIndex=_RlSntpAnycastIfIndex_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,11,1,1),_RlSntpAnycastIfIndex_Type())
rlSntpAnycastIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:rlSntpAnycastIfIndex.setStatus(_A)
_RlSntpAnycastAddress_Type=IpAddress
_RlSntpAnycastAddress_Object=MibTableColumn
rlSntpAnycastAddress=_RlSntpAnycastAddress_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,11,1,2),_RlSntpAnycastAddress_Type())
rlSntpAnycastAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpAnycastAddress.setStatus(_A)
_RlSntpAnycastStratum_Type=NTPStratum
_RlSntpAnycastStratum_Object=MibTableColumn
rlSntpAnycastStratum=_RlSntpAnycastStratum_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,11,1,3),_RlSntpAnycastStratum_Type())
rlSntpAnycastStratum.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpAnycastStratum.setStatus(_A)
_RlSntpAnycastLastResp_Type=NTPTimeStamp
_RlSntpAnycastLastResp_Object=MibTableColumn
rlSntpAnycastLastResp=_RlSntpAnycastLastResp_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,11,1,4),_RlSntpAnycastLastResp_Type())
rlSntpAnycastLastResp.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpAnycastLastResp.setStatus(_A)
class _RlSntpAnycastStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3),(_P,4)))
_RlSntpAnycastStatus_Type.__name__=_D
_RlSntpAnycastStatus_Object=MibTableColumn
rlSntpAnycastStatus=_RlSntpAnycastStatus_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,11,1,5),_RlSntpAnycastStatus_Type())
rlSntpAnycastStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpAnycastStatus.setStatus(_A)
_RlSntpAnycastOffset_Type=NTPTimeStamp
_RlSntpAnycastOffset_Object=MibTableColumn
rlSntpAnycastOffset=_RlSntpAnycastOffset_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,11,1,6),_RlSntpAnycastOffset_Type())
rlSntpAnycastOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpAnycastOffset.setStatus(_A)
if mibBuilder.loadTexts:rlSntpAnycastOffset.setUnits(_F)
_RlSntpAnycastDelay_Type=NTPSignedTimeValue
_RlSntpAnycastDelay_Object=MibTableColumn
rlSntpAnycastDelay=_RlSntpAnycastDelay_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,11,1,7),_RlSntpAnycastDelay_Type())
rlSntpAnycastDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpAnycastDelay.setStatus(_A)
if mibBuilder.loadTexts:rlSntpAnycastDelay.setUnits(_F)
_RlSntpAnycastRowStatus_Type=RowStatus
_RlSntpAnycastRowStatus_Object=MibTableColumn
rlSntpAnycastRowStatus=_RlSntpAnycastRowStatus_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,11,1,8),_RlSntpAnycastRowStatus_Type())
rlSntpAnycastRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSntpAnycastRowStatus.setStatus(_A)
_RlSntpConfigServerTable_Object=MibTable
rlSntpConfigServerTable=_RlSntpConfigServerTable_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,12))
if mibBuilder.loadTexts:rlSntpConfigServerTable.setStatus(_A)
_RlSntpServerEntry_Object=MibTableRow
rlSntpServerEntry=_RlSntpServerEntry_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,12,1))
rlSntpServerEntry.setIndexNames((0,_G,_d))
if mibBuilder.loadTexts:rlSntpServerEntry.setStatus(_A)
_RlSntpServerAddress_Type=IpAddress
_RlSntpServerAddress_Object=MibTableColumn
rlSntpServerAddress=_RlSntpServerAddress_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,12,1,1),_RlSntpServerAddress_Type())
rlSntpServerAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:rlSntpServerAddress.setStatus(_A)
class _RlSntpServerPolled_Type(TruthValue):defaultValue=2
_RlSntpServerPolled_Type.__name__=_H
_RlSntpServerPolled_Object=MibTableColumn
rlSntpServerPolled=_RlSntpServerPolled_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,12,1,2),_RlSntpServerPolled_Type())
rlSntpServerPolled.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSntpServerPolled.setStatus(_A)
_RlSntpServerStratum_Type=NTPStratum
_RlSntpServerStratum_Object=MibTableColumn
rlSntpServerStratum=_RlSntpServerStratum_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,12,1,3),_RlSntpServerStratum_Type())
rlSntpServerStratum.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpServerStratum.setStatus(_A)
_RlSntpServerLastResp_Type=NTPTimeStamp
_RlSntpServerLastResp_Object=MibTableColumn
rlSntpServerLastResp=_RlSntpServerLastResp_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,12,1,4),_RlSntpServerLastResp_Type())
rlSntpServerLastResp.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpServerLastResp.setStatus(_A)
class _RlSntpServerStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3),(_P,4)))
_RlSntpServerStatus_Type.__name__=_D
_RlSntpServerStatus_Object=MibTableColumn
rlSntpServerStatus=_RlSntpServerStatus_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,12,1,5),_RlSntpServerStatus_Type())
rlSntpServerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpServerStatus.setStatus(_A)
_RlSntpServersOffset_Type=NTPTimeStamp
_RlSntpServersOffset_Object=MibTableColumn
rlSntpServersOffset=_RlSntpServersOffset_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,12,1,6),_RlSntpServersOffset_Type())
rlSntpServersOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpServersOffset.setStatus(_A)
if mibBuilder.loadTexts:rlSntpServersOffset.setUnits(_F)
_RlSntpServersDelay_Type=NTPSignedTimeValue
_RlSntpServersDelay_Object=MibTableColumn
rlSntpServersDelay=_RlSntpServersDelay_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,12,1,7),_RlSntpServersDelay_Type())
rlSntpServersDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpServersDelay.setStatus(_A)
if mibBuilder.loadTexts:rlSntpServersDelay.setUnits(_F)
_RlSntpServersKeyIdentifier_Type=Unsigned32
_RlSntpServersKeyIdentifier_Object=MibTableColumn
rlSntpServersKeyIdentifier=_RlSntpServersKeyIdentifier_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,12,1,8),_RlSntpServersKeyIdentifier_Type())
rlSntpServersKeyIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSntpServersKeyIdentifier.setStatus(_A)
_RlSntpServerRowStatus_Type=RowStatus
_RlSntpServerRowStatus_Object=MibTableColumn
rlSntpServerRowStatus=_RlSntpServerRowStatus_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,12,1,9),_RlSntpServerRowStatus_Type())
rlSntpServerRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSntpServerRowStatus.setStatus(_A)
_RlSntpConfigAuthenticationTable_Object=MibTable
rlSntpConfigAuthenticationTable=_RlSntpConfigAuthenticationTable_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,13))
if mibBuilder.loadTexts:rlSntpConfigAuthenticationTable.setStatus(_A)
_RlSntpAuthenticationEntry_Object=MibTableRow
rlSntpAuthenticationEntry=_RlSntpAuthenticationEntry_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,13,1))
rlSntpAuthenticationEntry.setIndexNames((0,_G,_e))
if mibBuilder.loadTexts:rlSntpAuthenticationEntry.setStatus(_A)
class _RlSntpAuthenticationKeyID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_RlSntpAuthenticationKeyID_Type.__name__=_T
_RlSntpAuthenticationKeyID_Object=MibTableColumn
rlSntpAuthenticationKeyID=_RlSntpAuthenticationKeyID_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,13,1,1),_RlSntpAuthenticationKeyID_Type())
rlSntpAuthenticationKeyID.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSntpAuthenticationKeyID.setStatus(_A)
class _RlSntpAuthenticationKeyValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_RlSntpAuthenticationKeyValue_Type.__name__=_E
_RlSntpAuthenticationKeyValue_Object=MibTableColumn
rlSntpAuthenticationKeyValue=_RlSntpAuthenticationKeyValue_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,13,1,2),_RlSntpAuthenticationKeyValue_Type())
rlSntpAuthenticationKeyValue.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSntpAuthenticationKeyValue.setStatus(_A)
class _RlSntpAuthenticationKeyState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_RlSntpAuthenticationKeyState_Type.__name__=_D
_RlSntpAuthenticationKeyState_Object=MibTableColumn
rlSntpAuthenticationKeyState=_RlSntpAuthenticationKeyState_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,13,1,3),_RlSntpAuthenticationKeyState_Type())
rlSntpAuthenticationKeyState.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSntpAuthenticationKeyState.setStatus(_A)
_RlSntpAuthenticationRowStatus_Type=RowStatus
_RlSntpAuthenticationRowStatus_Object=MibTableColumn
rlSntpAuthenticationRowStatus=_RlSntpAuthenticationRowStatus_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,13,1,4),_RlSntpAuthenticationRowStatus_Type())
rlSntpAuthenticationRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSntpAuthenticationRowStatus.setStatus(_A)
class _RlSntpPort_Type(Integer32):defaultValue=123;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RlSntpPort_Type.__name__=_D
_RlSntpPort_Object=MibScalar
rlSntpPort=_RlSntpPort_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,14),_RlSntpPort_Type())
rlSntpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSntpPort.setStatus(_A)
_RlSntpConfigBroadcastInetTable_Object=MibTable
rlSntpConfigBroadcastInetTable=_RlSntpConfigBroadcastInetTable_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,15))
if mibBuilder.loadTexts:rlSntpConfigBroadcastInetTable.setStatus(_A)
_RlSntpBroadcastInetEntry_Object=MibTableRow
rlSntpBroadcastInetEntry=_RlSntpBroadcastInetEntry_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,15,1))
rlSntpBroadcastInetEntry.setIndexNames((0,_G,_f))
if mibBuilder.loadTexts:rlSntpBroadcastInetEntry.setStatus(_A)
_RlSntpBroadcastInetIfIndex_Type=Integer32
_RlSntpBroadcastInetIfIndex_Object=MibTableColumn
rlSntpBroadcastInetIfIndex=_RlSntpBroadcastInetIfIndex_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,15,1,1),_RlSntpBroadcastInetIfIndex_Type())
rlSntpBroadcastInetIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:rlSntpBroadcastInetIfIndex.setStatus(_A)
class _RlSntpBroadcastInetIfAdminState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_RlSntpBroadcastInetIfAdminState_Type.__name__=_D
_RlSntpBroadcastInetIfAdminState_Object=MibTableColumn
rlSntpBroadcastInetIfAdminState=_RlSntpBroadcastInetIfAdminState_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,15,1,2),_RlSntpBroadcastInetIfAdminState_Type())
rlSntpBroadcastInetIfAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSntpBroadcastInetIfAdminState.setStatus(_A)
class _RlSntpBroadcastInetMode_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_a,2),('send',3),(_b,4)))
_RlSntpBroadcastInetMode_Type.__name__=_D
_RlSntpBroadcastInetMode_Object=MibTableColumn
rlSntpBroadcastInetMode=_RlSntpBroadcastInetMode_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,15,1,3),_RlSntpBroadcastInetMode_Type())
rlSntpBroadcastInetMode.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSntpBroadcastInetMode.setStatus(_A)
class _RlSntpBroadcastInetPolled_Type(TruthValue):defaultValue=2
_RlSntpBroadcastInetPolled_Type.__name__=_H
_RlSntpBroadcastInetPolled_Object=MibTableColumn
rlSntpBroadcastInetPolled=_RlSntpBroadcastInetPolled_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,15,1,4),_RlSntpBroadcastInetPolled_Type())
rlSntpBroadcastInetPolled.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSntpBroadcastInetPolled.setStatus(_A)
_RlSntpBroadcastInetAddressType_Type=InetAddressType
_RlSntpBroadcastInetAddressType_Object=MibTableColumn
rlSntpBroadcastInetAddressType=_RlSntpBroadcastInetAddressType_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,15,1,5),_RlSntpBroadcastInetAddressType_Type())
rlSntpBroadcastInetAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpBroadcastInetAddressType.setStatus(_A)
_RlSntpBroadcastInetAddress_Type=InetAddress
_RlSntpBroadcastInetAddress_Object=MibTableColumn
rlSntpBroadcastInetAddress=_RlSntpBroadcastInetAddress_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,15,1,6),_RlSntpBroadcastInetAddress_Type())
rlSntpBroadcastInetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpBroadcastInetAddress.setStatus(_A)
_RlSntpBroadcastInetStratum_Type=NTPStratum
_RlSntpBroadcastInetStratum_Object=MibTableColumn
rlSntpBroadcastInetStratum=_RlSntpBroadcastInetStratum_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,15,1,7),_RlSntpBroadcastInetStratum_Type())
rlSntpBroadcastInetStratum.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpBroadcastInetStratum.setStatus(_A)
_RlSntpBroadcastInetLastResp_Type=NTPTimeStamp
_RlSntpBroadcastInetLastResp_Object=MibTableColumn
rlSntpBroadcastInetLastResp=_RlSntpBroadcastInetLastResp_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,15,1,8),_RlSntpBroadcastInetLastResp_Type())
rlSntpBroadcastInetLastResp.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpBroadcastInetLastResp.setStatus(_A)
class _RlSntpBroadcastInetStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3),(_P,4)))
_RlSntpBroadcastInetStatus_Type.__name__=_D
_RlSntpBroadcastInetStatus_Object=MibTableColumn
rlSntpBroadcastInetStatus=_RlSntpBroadcastInetStatus_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,15,1,9),_RlSntpBroadcastInetStatus_Type())
rlSntpBroadcastInetStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpBroadcastInetStatus.setStatus(_A)
_RlSntpBroadcastInetOffset_Type=NTPTimeStamp
_RlSntpBroadcastInetOffset_Object=MibTableColumn
rlSntpBroadcastInetOffset=_RlSntpBroadcastInetOffset_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,15,1,10),_RlSntpBroadcastInetOffset_Type())
rlSntpBroadcastInetOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpBroadcastInetOffset.setStatus(_A)
if mibBuilder.loadTexts:rlSntpBroadcastInetOffset.setUnits(_F)
_RlSntpBroadcastInetDelay_Type=NTPSignedTimeValue
_RlSntpBroadcastInetDelay_Object=MibTableColumn
rlSntpBroadcastInetDelay=_RlSntpBroadcastInetDelay_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,15,1,11),_RlSntpBroadcastInetDelay_Type())
rlSntpBroadcastInetDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpBroadcastInetDelay.setStatus(_A)
if mibBuilder.loadTexts:rlSntpBroadcastInetDelay.setUnits(_F)
_RlSntpBroadcastInetRowStatus_Type=RowStatus
_RlSntpBroadcastInetRowStatus_Object=MibTableColumn
rlSntpBroadcastInetRowStatus=_RlSntpBroadcastInetRowStatus_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,15,1,12),_RlSntpBroadcastInetRowStatus_Type())
rlSntpBroadcastInetRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSntpBroadcastInetRowStatus.setStatus(_A)
_RlSntpConfigAnycastInetTable_Object=MibTable
rlSntpConfigAnycastInetTable=_RlSntpConfigAnycastInetTable_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,16))
if mibBuilder.loadTexts:rlSntpConfigAnycastInetTable.setStatus(_A)
_RlSntpAnycastInetEntry_Object=MibTableRow
rlSntpAnycastInetEntry=_RlSntpAnycastInetEntry_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,16,1))
rlSntpAnycastInetEntry.setIndexNames((0,_G,_g))
if mibBuilder.loadTexts:rlSntpAnycastInetEntry.setStatus(_A)
_RlSntpAnycastInetIfIndex_Type=Integer32
_RlSntpAnycastInetIfIndex_Object=MibTableColumn
rlSntpAnycastInetIfIndex=_RlSntpAnycastInetIfIndex_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,16,1,1),_RlSntpAnycastInetIfIndex_Type())
rlSntpAnycastInetIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:rlSntpAnycastInetIfIndex.setStatus(_A)
_RlSntpAnycastInetAddressType_Type=InetAddressType
_RlSntpAnycastInetAddressType_Object=MibTableColumn
rlSntpAnycastInetAddressType=_RlSntpAnycastInetAddressType_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,16,1,2),_RlSntpAnycastInetAddressType_Type())
rlSntpAnycastInetAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpAnycastInetAddressType.setStatus(_A)
_RlSntpAnycastInetAddress_Type=InetAddress
_RlSntpAnycastInetAddress_Object=MibTableColumn
rlSntpAnycastInetAddress=_RlSntpAnycastInetAddress_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,16,1,3),_RlSntpAnycastInetAddress_Type())
rlSntpAnycastInetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpAnycastInetAddress.setStatus(_A)
_RlSntpAnycastInetStratum_Type=NTPStratum
_RlSntpAnycastInetStratum_Object=MibTableColumn
rlSntpAnycastInetStratum=_RlSntpAnycastInetStratum_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,16,1,4),_RlSntpAnycastInetStratum_Type())
rlSntpAnycastInetStratum.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpAnycastInetStratum.setStatus(_A)
_RlSntpAnycastInetLastResp_Type=NTPTimeStamp
_RlSntpAnycastInetLastResp_Object=MibTableColumn
rlSntpAnycastInetLastResp=_RlSntpAnycastInetLastResp_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,16,1,5),_RlSntpAnycastInetLastResp_Type())
rlSntpAnycastInetLastResp.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpAnycastInetLastResp.setStatus(_A)
class _RlSntpAnycastInetStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3),(_P,4)))
_RlSntpAnycastInetStatus_Type.__name__=_D
_RlSntpAnycastInetStatus_Object=MibTableColumn
rlSntpAnycastInetStatus=_RlSntpAnycastInetStatus_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,16,1,6),_RlSntpAnycastInetStatus_Type())
rlSntpAnycastInetStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpAnycastInetStatus.setStatus(_A)
_RlSntpAnycastInetOffset_Type=NTPTimeStamp
_RlSntpAnycastInetOffset_Object=MibTableColumn
rlSntpAnycastInetOffset=_RlSntpAnycastInetOffset_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,16,1,7),_RlSntpAnycastInetOffset_Type())
rlSntpAnycastInetOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpAnycastInetOffset.setStatus(_A)
if mibBuilder.loadTexts:rlSntpAnycastInetOffset.setUnits(_F)
_RlSntpAnycastInetDelay_Type=NTPSignedTimeValue
_RlSntpAnycastInetDelay_Object=MibTableColumn
rlSntpAnycastInetDelay=_RlSntpAnycastInetDelay_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,16,1,8),_RlSntpAnycastInetDelay_Type())
rlSntpAnycastInetDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpAnycastInetDelay.setStatus(_A)
if mibBuilder.loadTexts:rlSntpAnycastInetDelay.setUnits(_F)
_RlSntpAnycastInetRowStatus_Type=RowStatus
_RlSntpAnycastInetRowStatus_Object=MibTableColumn
rlSntpAnycastInetRowStatus=_RlSntpAnycastInetRowStatus_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,16,1,9),_RlSntpAnycastInetRowStatus_Type())
rlSntpAnycastInetRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSntpAnycastInetRowStatus.setStatus(_A)
_RlSntpConfigServerInetTable_Object=MibTable
rlSntpConfigServerInetTable=_RlSntpConfigServerInetTable_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,17))
if mibBuilder.loadTexts:rlSntpConfigServerInetTable.setStatus(_A)
_RlSntpServerInetEntry_Object=MibTableRow
rlSntpServerInetEntry=_RlSntpServerInetEntry_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,17,1))
rlSntpServerInetEntry.setIndexNames((0,_G,_h),(0,_G,_i))
if mibBuilder.loadTexts:rlSntpServerInetEntry.setStatus(_A)
_RlSntpServerInetAddressType_Type=InetAddressType
_RlSntpServerInetAddressType_Object=MibTableColumn
rlSntpServerInetAddressType=_RlSntpServerInetAddressType_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,17,1,1),_RlSntpServerInetAddressType_Type())
rlSntpServerInetAddressType.setMaxAccess(_I)
if mibBuilder.loadTexts:rlSntpServerInetAddressType.setStatus(_A)
_RlSntpServerInetAddress_Type=InetAddress
_RlSntpServerInetAddress_Object=MibTableColumn
rlSntpServerInetAddress=_RlSntpServerInetAddress_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,17,1,2),_RlSntpServerInetAddress_Type())
rlSntpServerInetAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:rlSntpServerInetAddress.setStatus(_A)
class _RlSntpServerInetPolled_Type(TruthValue):defaultValue=2
_RlSntpServerInetPolled_Type.__name__=_H
_RlSntpServerInetPolled_Object=MibTableColumn
rlSntpServerInetPolled=_RlSntpServerInetPolled_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,17,1,3),_RlSntpServerInetPolled_Type())
rlSntpServerInetPolled.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSntpServerInetPolled.setStatus(_A)
_RlSntpServerInetStratum_Type=NTPStratum
_RlSntpServerInetStratum_Object=MibTableColumn
rlSntpServerInetStratum=_RlSntpServerInetStratum_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,17,1,4),_RlSntpServerInetStratum_Type())
rlSntpServerInetStratum.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpServerInetStratum.setStatus(_A)
_RlSntpServerInetLastResp_Type=NTPTimeStamp
_RlSntpServerInetLastResp_Object=MibTableColumn
rlSntpServerInetLastResp=_RlSntpServerInetLastResp_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,17,1,5),_RlSntpServerInetLastResp_Type())
rlSntpServerInetLastResp.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpServerInetLastResp.setStatus(_A)
class _RlSntpServerInetStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3),(_P,4)))
_RlSntpServerInetStatus_Type.__name__=_D
_RlSntpServerInetStatus_Object=MibTableColumn
rlSntpServerInetStatus=_RlSntpServerInetStatus_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,17,1,6),_RlSntpServerInetStatus_Type())
rlSntpServerInetStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpServerInetStatus.setStatus(_A)
_RlSntpServerInetOffset_Type=NTPTimeStamp
_RlSntpServerInetOffset_Object=MibTableColumn
rlSntpServerInetOffset=_RlSntpServerInetOffset_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,17,1,7),_RlSntpServerInetOffset_Type())
rlSntpServerInetOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpServerInetOffset.setStatus(_A)
if mibBuilder.loadTexts:rlSntpServerInetOffset.setUnits(_F)
_RlSntpServerInetDelay_Type=NTPSignedTimeValue
_RlSntpServerInetDelay_Object=MibTableColumn
rlSntpServerInetDelay=_RlSntpServerInetDelay_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,17,1,8),_RlSntpServerInetDelay_Type())
rlSntpServerInetDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSntpServerInetDelay.setStatus(_A)
if mibBuilder.loadTexts:rlSntpServerInetDelay.setUnits(_F)
_RlSntpServerInetKeyIdentifier_Type=Unsigned32
_RlSntpServerInetKeyIdentifier_Object=MibTableColumn
rlSntpServerInetKeyIdentifier=_RlSntpServerInetKeyIdentifier_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,17,1,9),_RlSntpServerInetKeyIdentifier_Type())
rlSntpServerInetKeyIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSntpServerInetKeyIdentifier.setStatus(_A)
_RlSntpServerInetRowStatus_Type=RowStatus
_RlSntpServerInetRowStatus_Object=MibTableColumn
rlSntpServerInetRowStatus=_RlSntpServerInetRowStatus_Object((1,3,6,1,4,1,259,10,1,14,89,92,2,2,17,1,10),_RlSntpServerInetRowStatus_Type())
rlSntpServerInetRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSntpServerInetRowStatus.setStatus(_A)
_RlNtpConfig_ObjectIdentity=ObjectIdentity
rlNtpConfig=_RlNtpConfig_ObjectIdentity((1,3,6,1,4,1,259,10,1,14,89,92,2,3))
mibBuilder.exportSymbols(_G,**{'NTPTimeStamp':NTPTimeStamp,'NTPSignedTimeValue':NTPSignedTimeValue,'NTPStratum':NTPStratum,_R:RlTimeSyncMethod,_S:RlDaylightSavingTimeMode,_X:RlSntpNtpSyncType,'RlSntpNtpSyncEntryType':RlSntpNtpSyncEntryType,'rlTimeSynchronization':rlTimeSynchronization,'rlTimeSyncMethodMode':rlTimeSyncMethodMode,'rlTimeSyncMibVersion':rlTimeSyncMibVersion,'rndTimeSyncManagedTime':rndTimeSyncManagedTime,'rndTimeSyncManagedDate':rndTimeSyncManagedDate,'rndTimeSyncManagedDateTime':rndTimeSyncManagedDateTime,'rlTimeSyncMethod':rlTimeSyncMethod,'rlTimeZone':rlTimeZone,'rlTimeZoneCode':rlTimeZoneCode,'rlDaylightSavingTimeMode':rlDaylightSavingTimeMode,'rlDaylightSavingTimeStart':rlDaylightSavingTimeStart,'rlDaylightSavingTimeEnd':rlDaylightSavingTimeEnd,'rlDaylightSavingTimeOffset':rlDaylightSavingTimeOffset,'rlDaylightSavingTimeCode':rlDaylightSavingTimeCode,'rlTZDSTOffset':rlTZDSTOffset,'rlTimeZoneName':rlTimeZoneName,'rlTimeZoneTable':rlTimeZoneTable,'rlTimeZoneEntry':rlTimeZoneEntry,_W:rlTimeZoneIndex,'rlTimeZoneTimeSyncMethod':rlTimeZoneTimeSyncMethod,'rlTimeZoneTimeZoneOffset':rlTimeZoneTimeZoneOffset,'rlTimeZoneTimeZoneCode':rlTimeZoneTimeZoneCode,'rlTimeZoneDaylightSavingTimeMode':rlTimeZoneDaylightSavingTimeMode,'rlTimeZoneDaylightSavingTimeStart':rlTimeZoneDaylightSavingTimeStart,'rlTimeZoneDaylightSavingTimeEnd':rlTimeZoneDaylightSavingTimeEnd,'rlTimeZoneDaylightSavingTimeOffset':rlTimeZoneDaylightSavingTimeOffset,'rlTimeZoneDaylightSavingTimeCode':rlTimeZoneDaylightSavingTimeCode,'rlTimeZoneTZDSTOffset':rlTimeZoneTZDSTOffset,'rlTimeZoneTimeZoneName':rlTimeZoneTimeZoneName,'rlTimeZoneDataType':rlTimeZoneDataType,'rlTimeZoneDataSourceIfIndex':rlTimeZoneDataSourceIfIndex,'rlClockStatus':rlClockStatus,'rlDhcpTimezoneOptionEnabled':rlDhcpTimezoneOptionEnabled,'rlAutomaticClockSetFromPCEnabled':rlAutomaticClockSetFromPCEnabled,'rlTimeAndDateHaveBeenSet':rlTimeAndDateHaveBeenSet,'rlSntpNtpClient':rlSntpNtpClient,'rlSntpNtpConfig':rlSntpNtpConfig,'rlSntpNtpMibVersion':rlSntpNtpMibVersion,'rlSntpNtpConfigMode':rlSntpNtpConfigMode,'rlSntpNtpConfigSysStratum':rlSntpNtpConfigSysStratum,'rlSntpNtpConfigPollInterval':rlSntpNtpConfigPollInterval,'rlSntpNtpConfigPrimaryPollSrvAddr':rlSntpNtpConfigPrimaryPollSrvAddr,'rlSntpNtpConfigPrimaryPollSrvMrid':rlSntpNtpConfigPrimaryPollSrvMrid,'rlSntpNtpConfigPrimaryPollSrvIfIndex':rlSntpNtpConfigPrimaryPollSrvIfIndex,'rlSntpNtpConfigPrimaryPollSrvStratum':rlSntpNtpConfigPrimaryPollSrvStratum,'rlSntpNtpConfigSyncSrvAddr':rlSntpNtpConfigSyncSrvAddr,'rlSntpNtpConfigSyncSrvMrid':rlSntpNtpConfigSyncSrvMrid,'rlSntpNtpConfigSyncSrvIfIndex':rlSntpNtpConfigSyncSrvIfIndex,'rlSntpNtpConfigSyncSrvType':rlSntpNtpConfigSyncSrvType,'rlSntpNtpConfigSyncSrvStratum':rlSntpNtpConfigSyncSrvStratum,'rlSntpNtpConfigRetryTimeout':rlSntpNtpConfigRetryTimeout,'rlSntpNtpConfigRetryCnt':rlSntpNtpConfigRetryCnt,'rlSntpNtpConfigSrvTable':rlSntpNtpConfigSrvTable,'rlSntpNtpConfigSrvEntry':rlSntpNtpConfigSrvEntry,_Y:rlSntpNtpConfigSrvEntryType,'rlSntpNtpConfigSrvInetAddressType':rlSntpNtpConfigSrvInetAddressType,'rlSntpNtpConfigSrvInetAddress':rlSntpNtpConfigSrvInetAddress,'rlSntpNtpConfigSrvMrid':rlSntpNtpConfigSrvMrid,'rlSntpNtpConfigSrvIfIndex':rlSntpNtpConfigSrvIfIndex,'rlSntpNtpConfigSrvSyncType':rlSntpNtpConfigSrvSyncType,'rlSntpNtpConfigSrvStratum':rlSntpNtpConfigSrvStratum,'rlSntpConfig':rlSntpConfig,'rlSntpClientMode':rlSntpClientMode,'rlSntpUnicastAdminState':rlSntpUnicastAdminState,'rlSntpBroadcastAdminState':rlSntpBroadcastAdminState,'rlSntpAnycastAdminState':rlSntpAnycastAdminState,'rlSntpUnicastPollState':rlSntpUnicastPollState,'rlSntpBroadcastPollState':rlSntpBroadcastPollState,'rlSntpAnycastPollState':rlSntpAnycastPollState,'rlSntpAuthenticationState':rlSntpAuthenticationState,'rlTimeValidFlag':rlTimeValidFlag,'rlSntpConfigBroadcastTable':rlSntpConfigBroadcastTable,'rlSntpBroadcastEntry':rlSntpBroadcastEntry,_Z:rlSntpBroadcastIfIndex,'rlSntpBroadcastIfAdminState':rlSntpBroadcastIfAdminState,'rlSntpBroadcastMode':rlSntpBroadcastMode,'rlSntpBroadcastPolled':rlSntpBroadcastPolled,'rlSntpBroadcastAddress':rlSntpBroadcastAddress,'rlSntpBroadcastStratum':rlSntpBroadcastStratum,'rlSntpBroadcastLastResp':rlSntpBroadcastLastResp,'rlSntpBroadcastStatus':rlSntpBroadcastStatus,'rlSntpBroadcastOffset':rlSntpBroadcastOffset,'rlSntpBroadcastDelay':rlSntpBroadcastDelay,'rlSntpBroadcastRowStatus':rlSntpBroadcastRowStatus,'rlSntpConfigAnycastTable':rlSntpConfigAnycastTable,'rlSntpAnycastEntry':rlSntpAnycastEntry,_c:rlSntpAnycastIfIndex,'rlSntpAnycastAddress':rlSntpAnycastAddress,'rlSntpAnycastStratum':rlSntpAnycastStratum,'rlSntpAnycastLastResp':rlSntpAnycastLastResp,'rlSntpAnycastStatus':rlSntpAnycastStatus,'rlSntpAnycastOffset':rlSntpAnycastOffset,'rlSntpAnycastDelay':rlSntpAnycastDelay,'rlSntpAnycastRowStatus':rlSntpAnycastRowStatus,'rlSntpConfigServerTable':rlSntpConfigServerTable,'rlSntpServerEntry':rlSntpServerEntry,_d:rlSntpServerAddress,'rlSntpServerPolled':rlSntpServerPolled,'rlSntpServerStratum':rlSntpServerStratum,'rlSntpServerLastResp':rlSntpServerLastResp,'rlSntpServerStatus':rlSntpServerStatus,'rlSntpServersOffset':rlSntpServersOffset,'rlSntpServersDelay':rlSntpServersDelay,'rlSntpServersKeyIdentifier':rlSntpServersKeyIdentifier,'rlSntpServerRowStatus':rlSntpServerRowStatus,'rlSntpConfigAuthenticationTable':rlSntpConfigAuthenticationTable,'rlSntpAuthenticationEntry':rlSntpAuthenticationEntry,_e:rlSntpAuthenticationKeyID,'rlSntpAuthenticationKeyValue':rlSntpAuthenticationKeyValue,'rlSntpAuthenticationKeyState':rlSntpAuthenticationKeyState,'rlSntpAuthenticationRowStatus':rlSntpAuthenticationRowStatus,'rlSntpPort':rlSntpPort,'rlSntpConfigBroadcastInetTable':rlSntpConfigBroadcastInetTable,'rlSntpBroadcastInetEntry':rlSntpBroadcastInetEntry,_f:rlSntpBroadcastInetIfIndex,'rlSntpBroadcastInetIfAdminState':rlSntpBroadcastInetIfAdminState,'rlSntpBroadcastInetMode':rlSntpBroadcastInetMode,'rlSntpBroadcastInetPolled':rlSntpBroadcastInetPolled,'rlSntpBroadcastInetAddressType':rlSntpBroadcastInetAddressType,'rlSntpBroadcastInetAddress':rlSntpBroadcastInetAddress,'rlSntpBroadcastInetStratum':rlSntpBroadcastInetStratum,'rlSntpBroadcastInetLastResp':rlSntpBroadcastInetLastResp,'rlSntpBroadcastInetStatus':rlSntpBroadcastInetStatus,'rlSntpBroadcastInetOffset':rlSntpBroadcastInetOffset,'rlSntpBroadcastInetDelay':rlSntpBroadcastInetDelay,'rlSntpBroadcastInetRowStatus':rlSntpBroadcastInetRowStatus,'rlSntpConfigAnycastInetTable':rlSntpConfigAnycastInetTable,'rlSntpAnycastInetEntry':rlSntpAnycastInetEntry,_g:rlSntpAnycastInetIfIndex,'rlSntpAnycastInetAddressType':rlSntpAnycastInetAddressType,'rlSntpAnycastInetAddress':rlSntpAnycastInetAddress,'rlSntpAnycastInetStratum':rlSntpAnycastInetStratum,'rlSntpAnycastInetLastResp':rlSntpAnycastInetLastResp,'rlSntpAnycastInetStatus':rlSntpAnycastInetStatus,'rlSntpAnycastInetOffset':rlSntpAnycastInetOffset,'rlSntpAnycastInetDelay':rlSntpAnycastInetDelay,'rlSntpAnycastInetRowStatus':rlSntpAnycastInetRowStatus,'rlSntpConfigServerInetTable':rlSntpConfigServerInetTable,'rlSntpServerInetEntry':rlSntpServerInetEntry,_h:rlSntpServerInetAddressType,_i:rlSntpServerInetAddress,'rlSntpServerInetPolled':rlSntpServerInetPolled,'rlSntpServerInetStratum':rlSntpServerInetStratum,'rlSntpServerInetLastResp':rlSntpServerInetLastResp,'rlSntpServerInetStatus':rlSntpServerInetStatus,'rlSntpServerInetOffset':rlSntpServerInetOffset,'rlSntpServerInetDelay':rlSntpServerInetDelay,'rlSntpServerInetKeyIdentifier':rlSntpServerInetKeyIdentifier,'rlSntpServerInetRowStatus':rlSntpServerInetRowStatus,'rlNtpConfig':rlNtpConfig})