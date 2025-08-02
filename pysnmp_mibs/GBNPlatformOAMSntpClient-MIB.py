_J='sntpAuthKeyId'
_I='sntpClientValidServerMask'
_H='sntpClientValidServerNet'
_G='DisplayString'
_F='Unsigned32'
_E='GBNPlatformOAMSntpClient-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
gbnPlatformOAM,=mibBuilder.importSymbols('GBNPlatformOAM-MIB','gbnPlatformOAM')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
gbnPlatformOAMSntpClient=ModuleIdentity((1,3,6,1,4,1,13464,1,2,1,1,8))
if mibBuilder.loadTexts:gbnPlatformOAMSntpClient.setRevisions(('1901-07-15 20:04',))
_SntpClientGeneral_ObjectIdentity=ObjectIdentity
sntpClientGeneral=_SntpClientGeneral_ObjectIdentity((1,3,6,1,4,1,13464,1,2,1,1,8,1))
class _SntpClientMode_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,8)));namedValues=NamedValues(*(('unicast',1),('anycast',2),('broadcast',4),('multicast',8)))
_SntpClientMode_Type.__name__=_C
_SntpClientMode_Object=MibScalar
sntpClientMode=_SntpClientMode_Object((1,3,6,1,4,1,13464,1,2,1,1,8,1,1),_SntpClientMode_Type())
sntpClientMode.setMaxAccess(_B)
if mibBuilder.loadTexts:sntpClientMode.setStatus(_A)
class _SntpClientPollInterval_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,1024))
_SntpClientPollInterval_Type.__name__=_C
_SntpClientPollInterval_Object=MibScalar
sntpClientPollInterval=_SntpClientPollInterval_Object((1,3,6,1,4,1,13464,1,2,1,1,8,1,2),_SntpClientPollInterval_Type())
sntpClientPollInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:sntpClientPollInterval.setStatus(_A)
class _SntpClientRetransInterval_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_SntpClientRetransInterval_Type.__name__=_C
_SntpClientRetransInterval_Object=MibScalar
sntpClientRetransInterval=_SntpClientRetransInterval_Object((1,3,6,1,4,1,13464,1,2,1,1,8,1,3),_SntpClientRetransInterval_Type())
sntpClientRetransInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:sntpClientRetransInterval.setStatus(_A)
class _SntpClientRetransTimes_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_SntpClientRetransTimes_Type.__name__=_C
_SntpClientRetransTimes_Object=MibScalar
sntpClientRetransTimes=_SntpClientRetransTimes_Object((1,3,6,1,4,1,13464,1,2,1,1,8,1,4),_SntpClientRetransTimes_Type())
sntpClientRetransTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:sntpClientRetransTimes.setStatus(_A)
_SntpClientServer_Type=IpAddress
_SntpClientServer_Object=MibScalar
sntpClientServer=_SntpClientServer_Object((1,3,6,1,4,1,13464,1,2,1,1,8,1,5),_SntpClientServer_Type())
sntpClientServer.setMaxAccess(_B)
if mibBuilder.loadTexts:sntpClientServer.setStatus(_A)
_SntpClientSynthFlag_Type=TruthValue
_SntpClientSynthFlag_Object=MibScalar
sntpClientSynthFlag=_SntpClientSynthFlag_Object((1,3,6,1,4,1,13464,1,2,1,1,8,1,6),_SntpClientSynthFlag_Type())
sntpClientSynthFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:sntpClientSynthFlag.setStatus(_A)
_SntpClientState_Type=Integer32
_SntpClientState_Object=MibScalar
sntpClientState=_SntpClientState_Object((1,3,6,1,4,1,13464,1,2,1,1,8,1,7),_SntpClientState_Type())
sntpClientState.setMaxAccess(_D)
if mibBuilder.loadTexts:sntpClientState.setStatus(_A)
_SntpClientLastSynthTime_Type=Integer32
_SntpClientLastSynthTime_Object=MibScalar
sntpClientLastSynthTime=_SntpClientLastSynthTime_Object((1,3,6,1,4,1,13464,1,2,1,1,8,1,8),_SntpClientLastSynthTime_Type())
sntpClientLastSynthTime.setMaxAccess(_D)
if mibBuilder.loadTexts:sntpClientLastSynthTime.setStatus(_A)
_SntpClientLastSynthErrno_Type=Integer32
_SntpClientLastSynthErrno_Object=MibScalar
sntpClientLastSynthErrno=_SntpClientLastSynthErrno_Object((1,3,6,1,4,1,13464,1,2,1,1,8,1,9),_SntpClientLastSynthErrno_Type())
sntpClientLastSynthErrno.setMaxAccess(_D)
if mibBuilder.loadTexts:sntpClientLastSynthErrno.setStatus(_A)
class _SntpClientAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_SntpClientAdminStatus_Type.__name__=_C
_SntpClientAdminStatus_Object=MibScalar
sntpClientAdminStatus=_SntpClientAdminStatus_Object((1,3,6,1,4,1,13464,1,2,1,1,8,1,10),_SntpClientAdminStatus_Type())
sntpClientAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sntpClientAdminStatus.setStatus(_A)
class _SntpClientBcastDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9999))
_SntpClientBcastDelay_Type.__name__=_C
_SntpClientBcastDelay_Object=MibScalar
sntpClientBcastDelay=_SntpClientBcastDelay_Object((1,3,6,1,4,1,13464,1,2,1,1,8,1,11),_SntpClientBcastDelay_Type())
sntpClientBcastDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:sntpClientBcastDelay.setStatus(_A)
class _SntpClientMcastTtl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SntpClientMcastTtl_Type.__name__=_C
_SntpClientMcastTtl_Object=MibScalar
sntpClientMcastTtl=_SntpClientMcastTtl_Object((1,3,6,1,4,1,13464,1,2,1,1,8,1,12),_SntpClientMcastTtl_Type())
sntpClientMcastTtl.setMaxAccess(_B)
if mibBuilder.loadTexts:sntpClientMcastTtl.setStatus(_A)
_SntpClientAuthFlag_Type=TruthValue
_SntpClientAuthFlag_Object=MibScalar
sntpClientAuthFlag=_SntpClientAuthFlag_Object((1,3,6,1,4,1,13464,1,2,1,1,8,1,13),_SntpClientAuthFlag_Type())
sntpClientAuthFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:sntpClientAuthFlag.setStatus(_A)
_SntpClientUniKeyID_Type=Unsigned32
_SntpClientUniKeyID_Object=MibScalar
sntpClientUniKeyID=_SntpClientUniKeyID_Object((1,3,6,1,4,1,13464,1,2,1,1,8,1,14),_SntpClientUniKeyID_Type())
sntpClientUniKeyID.setMaxAccess(_B)
if mibBuilder.loadTexts:sntpClientUniKeyID.setStatus(_A)
_SntpClientAnyKeyID_Type=Unsigned32
_SntpClientAnyKeyID_Object=MibScalar
sntpClientAnyKeyID=_SntpClientAnyKeyID_Object((1,3,6,1,4,1,13464,1,2,1,1,8,1,15),_SntpClientAnyKeyID_Type())
sntpClientAnyKeyID.setMaxAccess(_B)
if mibBuilder.loadTexts:sntpClientAnyKeyID.setStatus(_A)
_SntpClientValidServerTable_Object=MibTable
sntpClientValidServerTable=_SntpClientValidServerTable_Object((1,3,6,1,4,1,13464,1,2,1,1,8,2))
if mibBuilder.loadTexts:sntpClientValidServerTable.setStatus(_A)
_SntpClientValidServerEntry_Object=MibTableRow
sntpClientValidServerEntry=_SntpClientValidServerEntry_Object((1,3,6,1,4,1,13464,1,2,1,1,8,2,1))
sntpClientValidServerEntry.setIndexNames((0,_E,_H),(0,_E,_I))
if mibBuilder.loadTexts:sntpClientValidServerEntry.setStatus(_A)
_SntpClientValidServerNet_Type=IpAddress
_SntpClientValidServerNet_Object=MibTableColumn
sntpClientValidServerNet=_SntpClientValidServerNet_Object((1,3,6,1,4,1,13464,1,2,1,1,8,2,1,1),_SntpClientValidServerNet_Type())
sntpClientValidServerNet.setMaxAccess(_D)
if mibBuilder.loadTexts:sntpClientValidServerNet.setStatus(_A)
_SntpClientValidServerMask_Type=IpAddress
_SntpClientValidServerMask_Object=MibTableColumn
sntpClientValidServerMask=_SntpClientValidServerMask_Object((1,3,6,1,4,1,13464,1,2,1,1,8,2,1,2),_SntpClientValidServerMask_Type())
sntpClientValidServerMask.setMaxAccess(_D)
if mibBuilder.loadTexts:sntpClientValidServerMask.setStatus(_A)
_SntpClientValidServerRowStatus_Type=RowStatus
_SntpClientValidServerRowStatus_Object=MibTableColumn
sntpClientValidServerRowStatus=_SntpClientValidServerRowStatus_Object((1,3,6,1,4,1,13464,1,2,1,1,8,2,1,3),_SntpClientValidServerRowStatus_Type())
sntpClientValidServerRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sntpClientValidServerRowStatus.setStatus(_A)
_SntpAuthKeyTable_Object=MibTable
sntpAuthKeyTable=_SntpAuthKeyTable_Object((1,3,6,1,4,1,13464,1,2,1,1,8,3))
if mibBuilder.loadTexts:sntpAuthKeyTable.setStatus(_A)
_SntpAuthKeyEntry_Object=MibTableRow
sntpAuthKeyEntry=_SntpAuthKeyEntry_Object((1,3,6,1,4,1,13464,1,2,1,1,8,3,1))
sntpAuthKeyEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:sntpAuthKeyEntry.setStatus(_A)
class _SntpAuthKeyId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_SntpAuthKeyId_Type.__name__=_F
_SntpAuthKeyId_Object=MibTableColumn
sntpAuthKeyId=_SntpAuthKeyId_Object((1,3,6,1,4,1,13464,1,2,1,1,8,3,1,1),_SntpAuthKeyId_Type())
sntpAuthKeyId.setMaxAccess(_D)
if mibBuilder.loadTexts:sntpAuthKeyId.setStatus(_A)
class _SntpAuthKeyValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_SntpAuthKeyValue_Type.__name__=_G
_SntpAuthKeyValue_Object=MibTableColumn
sntpAuthKeyValue=_SntpAuthKeyValue_Object((1,3,6,1,4,1,13464,1,2,1,1,8,3,1,2),_SntpAuthKeyValue_Type())
sntpAuthKeyValue.setMaxAccess(_B)
if mibBuilder.loadTexts:sntpAuthKeyValue.setStatus(_A)
_SntpAuthKeyTrustFlag_Type=TruthValue
_SntpAuthKeyTrustFlag_Object=MibTableColumn
sntpAuthKeyTrustFlag=_SntpAuthKeyTrustFlag_Object((1,3,6,1,4,1,13464,1,2,1,1,8,3,1,3),_SntpAuthKeyTrustFlag_Type())
sntpAuthKeyTrustFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:sntpAuthKeyTrustFlag.setStatus(_A)
_SntpAuthKeyRowStatus_Type=RowStatus
_SntpAuthKeyRowStatus_Object=MibTableColumn
sntpAuthKeyRowStatus=_SntpAuthKeyRowStatus_Object((1,3,6,1,4,1,13464,1,2,1,1,8,3,1,4),_SntpAuthKeyRowStatus_Type())
sntpAuthKeyRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sntpAuthKeyRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'gbnPlatformOAMSntpClient':gbnPlatformOAMSntpClient,'sntpClientGeneral':sntpClientGeneral,'sntpClientMode':sntpClientMode,'sntpClientPollInterval':sntpClientPollInterval,'sntpClientRetransInterval':sntpClientRetransInterval,'sntpClientRetransTimes':sntpClientRetransTimes,'sntpClientServer':sntpClientServer,'sntpClientSynthFlag':sntpClientSynthFlag,'sntpClientState':sntpClientState,'sntpClientLastSynthTime':sntpClientLastSynthTime,'sntpClientLastSynthErrno':sntpClientLastSynthErrno,'sntpClientAdminStatus':sntpClientAdminStatus,'sntpClientBcastDelay':sntpClientBcastDelay,'sntpClientMcastTtl':sntpClientMcastTtl,'sntpClientAuthFlag':sntpClientAuthFlag,'sntpClientUniKeyID':sntpClientUniKeyID,'sntpClientAnyKeyID':sntpClientAnyKeyID,'sntpClientValidServerTable':sntpClientValidServerTable,'sntpClientValidServerEntry':sntpClientValidServerEntry,_H:sntpClientValidServerNet,_I:sntpClientValidServerMask,'sntpClientValidServerRowStatus':sntpClientValidServerRowStatus,'sntpAuthKeyTable':sntpAuthKeyTable,'sntpAuthKeyEntry':sntpAuthKeyEntry,_J:sntpAuthKeyId,'sntpAuthKeyValue':sntpAuthKeyValue,'sntpAuthKeyTrustFlag':sntpAuthKeyTrustFlag,'sntpAuthKeyRowStatus':sntpAuthKeyRowStatus})