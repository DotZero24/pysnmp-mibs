_N='cadNtpAuthKeyId'
_M='not-accessible'
_L='cadNtpSourceIpAddress'
_K='IpAddress'
_J='CADANT-TIME-MIB'
_I='RowStatus'
_H='DisplayString'
_G='Unsigned32'
_F='read-only'
_E='TruthValue'
_D='read-write'
_C='read-create'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cadSystem,=mibBuilder.importSymbols('CADANT-PRODUCTS-MIB','cadSystem')
CadDouble,=mibBuilder.importSymbols('CADANT-TC','CadDouble')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,_K,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_H,'PhysAddress',_I,'TextualConvention',_E)
cadTimeMib=ModuleIdentity((1,3,6,1,4,1,4998,1,1,5,2))
if mibBuilder.loadTexts:cadTimeMib.setRevisions(('2015-10-19 00:00','2011-02-07 00:00','2006-03-07 00:00','2005-07-26 00:00','2003-09-11 00:00','2003-04-29 00:00','2002-10-28 00:00','2002-10-23 00:00'))
_CadClock_ObjectIdentity=ObjectIdentity
cadClock=_CadClock_ObjectIdentity((1,3,6,1,4,1,4998,1,1,5,2,1))
class _CadTimeZone_Type(DisplayString):defaultValue=OctetString('GMT')
_CadTimeZone_Type.__name__=_H
_CadTimeZone_Object=MibScalar
cadTimeZone=_CadTimeZone_Object((1,3,6,1,4,1,4998,1,1,5,2,1,1),_CadTimeZone_Type())
cadTimeZone.setMaxAccess(_D)
if mibBuilder.loadTexts:cadTimeZone.setStatus(_A)
class _CadIsDST_Type(TruthValue):defaultValue=2
_CadIsDST_Type.__name__=_E
_CadIsDST_Object=MibScalar
cadIsDST=_CadIsDST_Object((1,3,6,1,4,1,4998,1,1,5,2,1,2),_CadIsDST_Type())
cadIsDST.setMaxAccess(_F)
if mibBuilder.loadTexts:cadIsDST.setStatus(_A)
_CadTZAbbrev_Type=DisplayString
_CadTZAbbrev_Object=MibScalar
cadTZAbbrev=_CadTZAbbrev_Object((1,3,6,1,4,1,4998,1,1,5,2,1,3),_CadTZAbbrev_Type())
cadTZAbbrev.setMaxAccess(_F)
if mibBuilder.loadTexts:cadTZAbbrev.setStatus(_A)
_CadLocalDateAndTime_Type=DateAndTime
_CadLocalDateAndTime_Object=MibScalar
cadLocalDateAndTime=_CadLocalDateAndTime_Object((1,3,6,1,4,1,4998,1,1,5,2,1,4),_CadLocalDateAndTime_Type())
cadLocalDateAndTime.setMaxAccess(_F)
if mibBuilder.loadTexts:cadLocalDateAndTime.setStatus(_A)
_CadLocalTime_Type=Unsigned32
_CadLocalTime_Object=MibScalar
cadLocalTime=_CadLocalTime_Object((1,3,6,1,4,1,4998,1,1,5,2,1,5),_CadLocalTime_Type())
cadLocalTime.setMaxAccess(_F)
if mibBuilder.loadTexts:cadLocalTime.setStatus(_A)
_CadUTCtime_Type=Unsigned32
_CadUTCtime_Object=MibScalar
cadUTCtime=_CadUTCtime_Object((1,3,6,1,4,1,4998,1,1,5,2,1,6),_CadUTCtime_Type())
cadUTCtime.setMaxAccess(_D)
if mibBuilder.loadTexts:cadUTCtime.setStatus(_A)
class _CadNetTimeSyncProto_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('tod',1),('ntp',2)))
_CadNetTimeSyncProto_Type.__name__=_B
_CadNetTimeSyncProto_Object=MibScalar
cadNetTimeSyncProto=_CadNetTimeSyncProto_Object((1,3,6,1,4,1,4998,1,1,5,2,1,7),_CadNetTimeSyncProto_Type())
cadNetTimeSyncProto.setMaxAccess(_D)
if mibBuilder.loadTexts:cadNetTimeSyncProto.setStatus(_A)
_CadTod_ObjectIdentity=ObjectIdentity
cadTod=_CadTod_ObjectIdentity((1,3,6,1,4,1,4998,1,1,5,2,2))
class _CadTodServerIpAddress_Type(IpAddress):defaultHexValue='00000000'
_CadTodServerIpAddress_Type.__name__=_K
_CadTodServerIpAddress_Object=MibScalar
cadTodServerIpAddress=_CadTodServerIpAddress_Object((1,3,6,1,4,1,4998,1,1,5,2,2,1),_CadTodServerIpAddress_Type())
cadTodServerIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cadTodServerIpAddress.setStatus(_A)
class _CadTodServerConnType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tcp',1),('udp',2)))
_CadTodServerConnType_Type.__name__=_B
_CadTodServerConnType_Object=MibScalar
cadTodServerConnType=_CadTodServerConnType_Object((1,3,6,1,4,1,4998,1,1,5,2,2,2),_CadTodServerConnType_Type())
cadTodServerConnType.setMaxAccess(_D)
if mibBuilder.loadTexts:cadTodServerConnType.setStatus(_A)
_CadNtp_ObjectIdentity=ObjectIdentity
cadNtp=_CadNtp_ObjectIdentity((1,3,6,1,4,1,4998,1,1,5,2,3))
class _CadNtpVersionDefault_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4))
_CadNtpVersionDefault_Type.__name__=_B
_CadNtpVersionDefault_Object=MibScalar
cadNtpVersionDefault=_CadNtpVersionDefault_Object((1,3,6,1,4,1,4998,1,1,5,2,3,1),_CadNtpVersionDefault_Type())
cadNtpVersionDefault.setMaxAccess(_D)
if mibBuilder.loadTexts:cadNtpVersionDefault.setStatus(_A)
class _CadNtpAuthenticate_Type(TruthValue):defaultValue=2
_CadNtpAuthenticate_Type.__name__=_E
_CadNtpAuthenticate_Object=MibScalar
cadNtpAuthenticate=_CadNtpAuthenticate_Object((1,3,6,1,4,1,4998,1,1,5,2,3,2),_CadNtpAuthenticate_Type())
cadNtpAuthenticate.setMaxAccess(_D)
if mibBuilder.loadTexts:cadNtpAuthenticate.setStatus(_A)
_CadNtpClockDrift_Type=CadDouble
_CadNtpClockDrift_Object=MibScalar
cadNtpClockDrift=_CadNtpClockDrift_Object((1,3,6,1,4,1,4998,1,1,5,2,3,3),_CadNtpClockDrift_Type())
cadNtpClockDrift.setMaxAccess(_F)
if mibBuilder.loadTexts:cadNtpClockDrift.setStatus(_A)
_CadNtpSource_ObjectIdentity=ObjectIdentity
cadNtpSource=_CadNtpSource_ObjectIdentity((1,3,6,1,4,1,4998,1,1,5,2,3,10))
class _CadNtpSourceMinPollDefault_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,11))
_CadNtpSourceMinPollDefault_Type.__name__=_B
_CadNtpSourceMinPollDefault_Object=MibScalar
cadNtpSourceMinPollDefault=_CadNtpSourceMinPollDefault_Object((1,3,6,1,4,1,4998,1,1,5,2,3,10,1),_CadNtpSourceMinPollDefault_Type())
cadNtpSourceMinPollDefault.setMaxAccess(_D)
if mibBuilder.loadTexts:cadNtpSourceMinPollDefault.setStatus(_A)
class _CadNtpSourceMaxPollDefault_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,11))
_CadNtpSourceMaxPollDefault_Type.__name__=_B
_CadNtpSourceMaxPollDefault_Object=MibScalar
cadNtpSourceMaxPollDefault=_CadNtpSourceMaxPollDefault_Object((1,3,6,1,4,1,4998,1,1,5,2,3,10,2),_CadNtpSourceMaxPollDefault_Type())
cadNtpSourceMaxPollDefault.setMaxAccess(_D)
if mibBuilder.loadTexts:cadNtpSourceMaxPollDefault.setStatus(_A)
_CadNtpSourceTable_Object=MibTable
cadNtpSourceTable=_CadNtpSourceTable_Object((1,3,6,1,4,1,4998,1,1,5,2,3,10,10))
if mibBuilder.loadTexts:cadNtpSourceTable.setStatus(_A)
_CadNtpSourceEntry_Object=MibTableRow
cadNtpSourceEntry=_CadNtpSourceEntry_Object((1,3,6,1,4,1,4998,1,1,5,2,3,10,10,1))
cadNtpSourceEntry.setIndexNames((0,_J,_L))
if mibBuilder.loadTexts:cadNtpSourceEntry.setStatus(_A)
_CadNtpSourceIpAddress_Type=IpAddress
_CadNtpSourceIpAddress_Object=MibTableColumn
cadNtpSourceIpAddress=_CadNtpSourceIpAddress_Object((1,3,6,1,4,1,4998,1,1,5,2,3,10,10,1,1),_CadNtpSourceIpAddress_Type())
cadNtpSourceIpAddress.setMaxAccess(_M)
if mibBuilder.loadTexts:cadNtpSourceIpAddress.setStatus(_A)
class _CadNtpSourceType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('unicastServer',1),('broadcastServer',2),('multicastServer',3),('manycastServer',4),('unicastPeer',5),('manycastPeer',6)))
_CadNtpSourceType_Type.__name__=_B
_CadNtpSourceType_Object=MibTableColumn
cadNtpSourceType=_CadNtpSourceType_Object((1,3,6,1,4,1,4998,1,1,5,2,3,10,10,1,2),_CadNtpSourceType_Type())
cadNtpSourceType.setMaxAccess(_C)
if mibBuilder.loadTexts:cadNtpSourceType.setStatus(_A)
class _CadNtpSourceBurstEnabled_Type(TruthValue):defaultValue=2
_CadNtpSourceBurstEnabled_Type.__name__=_E
_CadNtpSourceBurstEnabled_Object=MibTableColumn
cadNtpSourceBurstEnabled=_CadNtpSourceBurstEnabled_Object((1,3,6,1,4,1,4998,1,1,5,2,3,10,10,1,3),_CadNtpSourceBurstEnabled_Type())
cadNtpSourceBurstEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cadNtpSourceBurstEnabled.setStatus(_A)
class _CadNtpSourcePreferred_Type(TruthValue):defaultValue=2
_CadNtpSourcePreferred_Type.__name__=_E
_CadNtpSourcePreferred_Object=MibTableColumn
cadNtpSourcePreferred=_CadNtpSourcePreferred_Object((1,3,6,1,4,1,4998,1,1,5,2,3,10,10,1,4),_CadNtpSourcePreferred_Type())
cadNtpSourcePreferred.setMaxAccess(_C)
if mibBuilder.loadTexts:cadNtpSourcePreferred.setStatus(_A)
class _CadNtpSourceAuthKeyId_Type(Unsigned32):defaultValue=0
_CadNtpSourceAuthKeyId_Type.__name__=_G
_CadNtpSourceAuthKeyId_Object=MibTableColumn
cadNtpSourceAuthKeyId=_CadNtpSourceAuthKeyId_Object((1,3,6,1,4,1,4998,1,1,5,2,3,10,10,1,5),_CadNtpSourceAuthKeyId_Type())
cadNtpSourceAuthKeyId.setMaxAccess(_C)
if mibBuilder.loadTexts:cadNtpSourceAuthKeyId.setStatus(_A)
class _CadNtpSourceMinPoll_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(4,11))
_CadNtpSourceMinPoll_Type.__name__=_B
_CadNtpSourceMinPoll_Object=MibTableColumn
cadNtpSourceMinPoll=_CadNtpSourceMinPoll_Object((1,3,6,1,4,1,4998,1,1,5,2,3,10,10,1,6),_CadNtpSourceMinPoll_Type())
cadNtpSourceMinPoll.setMaxAccess(_C)
if mibBuilder.loadTexts:cadNtpSourceMinPoll.setStatus(_A)
class _CadNtpSourceMaxPoll_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(4,11))
_CadNtpSourceMaxPoll_Type.__name__=_B
_CadNtpSourceMaxPoll_Object=MibTableColumn
cadNtpSourceMaxPoll=_CadNtpSourceMaxPoll_Object((1,3,6,1,4,1,4998,1,1,5,2,3,10,10,1,7),_CadNtpSourceMaxPoll_Type())
cadNtpSourceMaxPoll.setMaxAccess(_C)
if mibBuilder.loadTexts:cadNtpSourceMaxPoll.setStatus(_A)
class _CadNtpSourceVersion_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2,4))
_CadNtpSourceVersion_Type.__name__=_B
_CadNtpSourceVersion_Object=MibTableColumn
cadNtpSourceVersion=_CadNtpSourceVersion_Object((1,3,6,1,4,1,4998,1,1,5,2,3,10,10,1,8),_CadNtpSourceVersion_Type())
cadNtpSourceVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cadNtpSourceVersion.setStatus(_A)
class _CadNtpSourceTtl_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CadNtpSourceTtl_Type.__name__=_B
_CadNtpSourceTtl_Object=MibTableColumn
cadNtpSourceTtl=_CadNtpSourceTtl_Object((1,3,6,1,4,1,4998,1,1,5,2,3,10,10,1,9),_CadNtpSourceTtl_Type())
cadNtpSourceTtl.setMaxAccess(_C)
if mibBuilder.loadTexts:cadNtpSourceTtl.setStatus(_A)
class _CadNtpSourceRowStatus_Type(RowStatus):defaultValue=4
_CadNtpSourceRowStatus_Type.__name__=_I
_CadNtpSourceRowStatus_Object=MibTableColumn
cadNtpSourceRowStatus=_CadNtpSourceRowStatus_Object((1,3,6,1,4,1,4998,1,1,5,2,3,10,10,1,10),_CadNtpSourceRowStatus_Type())
cadNtpSourceRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cadNtpSourceRowStatus.setStatus(_A)
_CadNtpAuthKeyTable_Object=MibTable
cadNtpAuthKeyTable=_CadNtpAuthKeyTable_Object((1,3,6,1,4,1,4998,1,1,5,2,3,30))
if mibBuilder.loadTexts:cadNtpAuthKeyTable.setStatus(_A)
_CadNtpAuthKeyEntry_Object=MibTableRow
cadNtpAuthKeyEntry=_CadNtpAuthKeyEntry_Object((1,3,6,1,4,1,4998,1,1,5,2,3,30,1))
cadNtpAuthKeyEntry.setIndexNames((0,_J,_N))
if mibBuilder.loadTexts:cadNtpAuthKeyEntry.setStatus(_A)
class _CadNtpAuthKeyId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65534))
_CadNtpAuthKeyId_Type.__name__=_G
_CadNtpAuthKeyId_Object=MibTableColumn
cadNtpAuthKeyId=_CadNtpAuthKeyId_Object((1,3,6,1,4,1,4998,1,1,5,2,3,30,1,1),_CadNtpAuthKeyId_Type())
cadNtpAuthKeyId.setMaxAccess(_M)
if mibBuilder.loadTexts:cadNtpAuthKeyId.setStatus(_A)
class _CadNtpAuthKeyType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('md5',1))
_CadNtpAuthKeyType_Type.__name__=_B
_CadNtpAuthKeyType_Object=MibTableColumn
cadNtpAuthKeyType=_CadNtpAuthKeyType_Object((1,3,6,1,4,1,4998,1,1,5,2,3,30,1,2),_CadNtpAuthKeyType_Type())
cadNtpAuthKeyType.setMaxAccess(_C)
if mibBuilder.loadTexts:cadNtpAuthKeyType.setStatus(_A)
class _CadNtpAuthKeyValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_CadNtpAuthKeyValue_Type.__name__=_H
_CadNtpAuthKeyValue_Object=MibTableColumn
cadNtpAuthKeyValue=_CadNtpAuthKeyValue_Object((1,3,6,1,4,1,4998,1,1,5,2,3,30,1,3),_CadNtpAuthKeyValue_Type())
cadNtpAuthKeyValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cadNtpAuthKeyValue.setStatus(_A)
class _CadNtpAuthKeyRowStatus_Type(RowStatus):defaultValue=4
_CadNtpAuthKeyRowStatus_Type.__name__=_I
_CadNtpAuthKeyRowStatus_Object=MibTableColumn
cadNtpAuthKeyRowStatus=_CadNtpAuthKeyRowStatus_Object((1,3,6,1,4,1,4998,1,1,5,2,3,30,1,4),_CadNtpAuthKeyRowStatus_Type())
cadNtpAuthKeyRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cadNtpAuthKeyRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_J,**{'cadTimeMib':cadTimeMib,'cadClock':cadClock,'cadTimeZone':cadTimeZone,'cadIsDST':cadIsDST,'cadTZAbbrev':cadTZAbbrev,'cadLocalDateAndTime':cadLocalDateAndTime,'cadLocalTime':cadLocalTime,'cadUTCtime':cadUTCtime,'cadNetTimeSyncProto':cadNetTimeSyncProto,'cadTod':cadTod,'cadTodServerIpAddress':cadTodServerIpAddress,'cadTodServerConnType':cadTodServerConnType,'cadNtp':cadNtp,'cadNtpVersionDefault':cadNtpVersionDefault,'cadNtpAuthenticate':cadNtpAuthenticate,'cadNtpClockDrift':cadNtpClockDrift,'cadNtpSource':cadNtpSource,'cadNtpSourceMinPollDefault':cadNtpSourceMinPollDefault,'cadNtpSourceMaxPollDefault':cadNtpSourceMaxPollDefault,'cadNtpSourceTable':cadNtpSourceTable,'cadNtpSourceEntry':cadNtpSourceEntry,_L:cadNtpSourceIpAddress,'cadNtpSourceType':cadNtpSourceType,'cadNtpSourceBurstEnabled':cadNtpSourceBurstEnabled,'cadNtpSourcePreferred':cadNtpSourcePreferred,'cadNtpSourceAuthKeyId':cadNtpSourceAuthKeyId,'cadNtpSourceMinPoll':cadNtpSourceMinPoll,'cadNtpSourceMaxPoll':cadNtpSourceMaxPoll,'cadNtpSourceVersion':cadNtpSourceVersion,'cadNtpSourceTtl':cadNtpSourceTtl,'cadNtpSourceRowStatus':cadNtpSourceRowStatus,'cadNtpAuthKeyTable':cadNtpAuthKeyTable,'cadNtpAuthKeyEntry':cadNtpAuthKeyEntry,_N:cadNtpAuthKeyId,'cadNtpAuthKeyType':cadNtpAuthKeyType,'cadNtpAuthKeyValue':cadNtpAuthKeyValue,'cadNtpAuthKeyRowStatus':cadNtpAuthKeyRowStatus})