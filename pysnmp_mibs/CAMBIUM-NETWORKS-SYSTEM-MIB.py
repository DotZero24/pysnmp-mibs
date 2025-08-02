_I='InetAddressType'
_H='InetAddress'
_G='OctetString'
_F='read-only'
_E='TruthValue'
_D='DisplayString'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_H,_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_D,'PhysAddress','TextualConvention',_E)
cnSystem=ModuleIdentity((1,3,6,1,4,1,17713,24,4))
if mibBuilder.loadTexts:cnSystem.setRevisions(('2022-09-01 12:00','2022-05-27 19:00','2022-04-08 18:00','2021-12-18 18:00','2021-08-18 18:00','2021-05-06 18:00','2021-03-02 18:00','2021-02-15 18:00','2020-10-23 18:00','2020-06-25 18:00','2019-03-14 18:00'))
class _CambiumScheduledReload_Type(TruthValue):defaultValue=2
_CambiumScheduledReload_Type.__name__=_E
_CambiumScheduledReload_Object=MibScalar
cambiumScheduledReload=_CambiumScheduledReload_Object((1,3,6,1,4,1,17713,24,4,1),_CambiumScheduledReload_Type())
cambiumScheduledReload.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumScheduledReload.setStatus(_A)
class _CambiumReloadRelativeTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,86400))
_CambiumReloadRelativeTime_Type.__name__=_C
_CambiumReloadRelativeTime_Object=MibScalar
cambiumReloadRelativeTime=_CambiumReloadRelativeTime_Object((1,3,6,1,4,1,17713,24,4,2),_CambiumReloadRelativeTime_Type())
cambiumReloadRelativeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumReloadRelativeTime.setStatus(_A)
_CambiumReloadAbsoluteTime_Type=DateAndTime
_CambiumReloadAbsoluteTime_Object=MibScalar
cambiumReloadAbsoluteTime=_CambiumReloadAbsoluteTime_Object((1,3,6,1,4,1,17713,24,4,3),_CambiumReloadAbsoluteTime_Type())
cambiumReloadAbsoluteTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumReloadAbsoluteTime.setStatus(_A)
class _CambiumReloadReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_CambiumReloadReason_Type.__name__=_D
_CambiumReloadReason_Object=MibScalar
cambiumReloadReason=_CambiumReloadReason_Object((1,3,6,1,4,1,17713,24,4,4),_CambiumReloadReason_Type())
cambiumReloadReason.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumReloadReason.setStatus(_A)
class _CambiumLastReloadReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_CambiumLastReloadReason_Type.__name__=_D
_CambiumLastReloadReason_Object=MibScalar
cambiumLastReloadReason=_CambiumLastReloadReason_Object((1,3,6,1,4,1,17713,24,4,5),_CambiumLastReloadReason_Type())
cambiumLastReloadReason.setMaxAccess(_F)
if mibBuilder.loadTexts:cambiumLastReloadReason.setStatus(_A)
class _CambiumStpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_CambiumStpMode_Type.__name__=_C
_CambiumStpMode_Object=MibScalar
cambiumStpMode=_CambiumStpMode_Object((1,3,6,1,4,1,17713,24,4,6),_CambiumStpMode_Type())
cambiumStpMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumStpMode.setStatus(_A)
_CambiumXMSInterfaceIP_Type=IpAddress
_CambiumXMSInterfaceIP_Object=MibScalar
cambiumXMSInterfaceIP=_CambiumXMSInterfaceIP_Object((1,3,6,1,4,1,17713,24,4,7),_CambiumXMSInterfaceIP_Type())
cambiumXMSInterfaceIP.setMaxAccess(_F)
if mibBuilder.loadTexts:cambiumXMSInterfaceIP.setStatus(_A)
_CambiumXMSInterfaceMask_Type=IpAddress
_CambiumXMSInterfaceMask_Object=MibScalar
cambiumXMSInterfaceMask=_CambiumXMSInterfaceMask_Object((1,3,6,1,4,1,17713,24,4,8),_CambiumXMSInterfaceMask_Type())
cambiumXMSInterfaceMask.setMaxAccess(_F)
if mibBuilder.loadTexts:cambiumXMSInterfaceMask.setStatus(_A)
class _CambiumXMSInterfaceVLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_CambiumXMSInterfaceVLANId_Type.__name__=_C
_CambiumXMSInterfaceVLANId_Object=MibScalar
cambiumXMSInterfaceVLANId=_CambiumXMSInterfaceVLANId_Object((1,3,6,1,4,1,17713,24,4,9),_CambiumXMSInterfaceVLANId_Type())
cambiumXMSInterfaceVLANId.setMaxAccess(_F)
if mibBuilder.loadTexts:cambiumXMSInterfaceVLANId.setStatus(_A)
_CambiumSystemClock_Type=DateAndTime
_CambiumSystemClock_Object=MibScalar
cambiumSystemClock=_CambiumSystemClock_Object((1,3,6,1,4,1,17713,24,4,10),_CambiumSystemClock_Type())
cambiumSystemClock.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumSystemClock.setStatus(_A)
class _CambiumSystemTimezoneName_Type(DisplayString):defaultValue=OctetString('UTC');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,6))
_CambiumSystemTimezoneName_Type.__name__=_D
_CambiumSystemTimezoneName_Object=MibScalar
cambiumSystemTimezoneName=_CambiumSystemTimezoneName_Object((1,3,6,1,4,1,17713,24,4,11),_CambiumSystemTimezoneName_Type())
cambiumSystemTimezoneName.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumSystemTimezoneName.setStatus(_A)
class _CambiumSystemTimezoneOffset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1439,1439))
_CambiumSystemTimezoneOffset_Type.__name__=_C
_CambiumSystemTimezoneOffset_Object=MibScalar
cambiumSystemTimezoneOffset=_CambiumSystemTimezoneOffset_Object((1,3,6,1,4,1,17713,24,4,12),_CambiumSystemTimezoneOffset_Type())
cambiumSystemTimezoneOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumSystemTimezoneOffset.setStatus(_A)
class _CambiumSystemSummerTimeName_Type(DisplayString):defaultValue=OctetString('UTC');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,6))
_CambiumSystemSummerTimeName_Type.__name__=_D
_CambiumSystemSummerTimeName_Object=MibScalar
cambiumSystemSummerTimeName=_CambiumSystemSummerTimeName_Object((1,3,6,1,4,1,17713,24,4,13),_CambiumSystemSummerTimeName_Type())
cambiumSystemSummerTimeName.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumSystemSummerTimeName.setStatus(_A)
class _CambiumSystemSummerTimeOffset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_CambiumSystemSummerTimeOffset_Type.__name__=_C
_CambiumSystemSummerTimeOffset_Object=MibScalar
cambiumSystemSummerTimeOffset=_CambiumSystemSummerTimeOffset_Object((1,3,6,1,4,1,17713,24,4,14),_CambiumSystemSummerTimeOffset_Type())
cambiumSystemSummerTimeOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumSystemSummerTimeOffset.setStatus(_A)
_CambiumSystemSummerTimeStart_Type=DateAndTime
_CambiumSystemSummerTimeStart_Object=MibScalar
cambiumSystemSummerTimeStart=_CambiumSystemSummerTimeStart_Object((1,3,6,1,4,1,17713,24,4,15),_CambiumSystemSummerTimeStart_Type())
cambiumSystemSummerTimeStart.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumSystemSummerTimeStart.setStatus(_A)
_CambiumSystemSummerTimeEnd_Type=DateAndTime
_CambiumSystemSummerTimeEnd_Object=MibScalar
cambiumSystemSummerTimeEnd=_CambiumSystemSummerTimeEnd_Object((1,3,6,1,4,1,17713,24,4,16),_CambiumSystemSummerTimeEnd_Type())
cambiumSystemSummerTimeEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumSystemSummerTimeEnd.setStatus(_A)
class _CambiumSystemRecurringSummerTimeStart_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
_CambiumSystemRecurringSummerTimeStart_Type.__name__=_D
_CambiumSystemRecurringSummerTimeStart_Object=MibScalar
cambiumSystemRecurringSummerTimeStart=_CambiumSystemRecurringSummerTimeStart_Object((1,3,6,1,4,1,17713,24,4,17),_CambiumSystemRecurringSummerTimeStart_Type())
cambiumSystemRecurringSummerTimeStart.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumSystemRecurringSummerTimeStart.setStatus(_A)
class _CambiumSystemRecurringSummerTimeEnd_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
_CambiumSystemRecurringSummerTimeEnd_Type.__name__=_D
_CambiumSystemRecurringSummerTimeEnd_Object=MibScalar
cambiumSystemRecurringSummerTimeEnd=_CambiumSystemRecurringSummerTimeEnd_Object((1,3,6,1,4,1,17713,24,4,18),_CambiumSystemRecurringSummerTimeEnd_Type())
cambiumSystemRecurringSummerTimeEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumSystemRecurringSummerTimeEnd.setStatus(_A)
class _CambiumSystemSummerTimeMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('one-shot',2),('recurring',3)))
_CambiumSystemSummerTimeMode_Type.__name__=_C
_CambiumSystemSummerTimeMode_Object=MibScalar
cambiumSystemSummerTimeMode=_CambiumSystemSummerTimeMode_Object((1,3,6,1,4,1,17713,24,4,19),_CambiumSystemSummerTimeMode_Type())
cambiumSystemSummerTimeMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumSystemSummerTimeMode.setStatus(_A)
class _CambiumReloadDefault_Type(TruthValue):defaultValue=2
_CambiumReloadDefault_Type.__name__=_E
_CambiumReloadDefault_Object=MibScalar
cambiumReloadDefault=_CambiumReloadDefault_Object((1,3,6,1,4,1,17713,24,4,20),_CambiumReloadDefault_Type())
cambiumReloadDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumReloadDefault.setStatus(_A)
class _CambiumReloadPartialDefault_Type(TruthValue):defaultValue=2
_CambiumReloadPartialDefault_Type.__name__=_E
_CambiumReloadPartialDefault_Object=MibScalar
cambiumReloadPartialDefault=_CambiumReloadPartialDefault_Object((1,3,6,1,4,1,17713,24,4,21),_CambiumReloadPartialDefault_Type())
cambiumReloadPartialDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumReloadPartialDefault.setStatus(_A)
class _CambiumSystemResetButton_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_CambiumSystemResetButton_Type.__name__=_C
_CambiumSystemResetButton_Object=MibScalar
cambiumSystemResetButton=_CambiumSystemResetButton_Object((1,3,6,1,4,1,17713,24,4,22),_CambiumSystemResetButton_Type())
cambiumSystemResetButton.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumSystemResetButton.setStatus(_A)
class _CambiumMstpReset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_CambiumMstpReset_Type.__name__=_C
_CambiumMstpReset_Object=MibScalar
cambiumMstpReset=_CambiumMstpReset_Object((1,3,6,1,4,1,17713,24,4,23),_CambiumMstpReset_Type())
cambiumMstpReset.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumMstpReset.setStatus(_A)
_CnHttpClient_ObjectIdentity=ObjectIdentity
cnHttpClient=_CnHttpClient_ObjectIdentity((1,3,6,1,4,1,17713,24,4,24))
class _CnHttpClientProxyAddress_Type(InetAddress):defaultValue=OctetString('')
_CnHttpClientProxyAddress_Type.__name__=_H
_CnHttpClientProxyAddress_Object=MibScalar
cnHttpClientProxyAddress=_CnHttpClientProxyAddress_Object((1,3,6,1,4,1,17713,24,4,24,1),_CnHttpClientProxyAddress_Type())
cnHttpClientProxyAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cnHttpClientProxyAddress.setStatus(_A)
class _CnHttpClientProxyAddressType_Type(InetAddressType):defaultValue=0
_CnHttpClientProxyAddressType_Type.__name__=_I
_CnHttpClientProxyAddressType_Object=MibScalar
cnHttpClientProxyAddressType=_CnHttpClientProxyAddressType_Object((1,3,6,1,4,1,17713,24,4,24,2),_CnHttpClientProxyAddressType_Type())
cnHttpClientProxyAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:cnHttpClientProxyAddressType.setStatus(_A)
class _CnHttpClientProxyPort_Type(Integer32):defaultValue=8080;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CnHttpClientProxyPort_Type.__name__=_C
_CnHttpClientProxyPort_Object=MibScalar
cnHttpClientProxyPort=_CnHttpClientProxyPort_Object((1,3,6,1,4,1,17713,24,4,24,3),_CnHttpClientProxyPort_Type())
cnHttpClientProxyPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cnHttpClientProxyPort.setStatus(_A)
class _CnHttpClientUsername_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_CnHttpClientUsername_Type.__name__=_D
_CnHttpClientUsername_Object=MibScalar
cnHttpClientUsername=_CnHttpClientUsername_Object((1,3,6,1,4,1,17713,24,4,24,4),_CnHttpClientUsername_Type())
cnHttpClientUsername.setMaxAccess(_B)
if mibBuilder.loadTexts:cnHttpClientUsername.setStatus(_A)
class _CnHttpClientPassword_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_CnHttpClientPassword_Type.__name__=_D
_CnHttpClientPassword_Object=MibScalar
cnHttpClientPassword=_CnHttpClientPassword_Object((1,3,6,1,4,1,17713,24,4,24,5),_CnHttpClientPassword_Type())
cnHttpClientPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:cnHttpClientPassword.setStatus(_A)
class _CnHttpClientPasswordType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,7)));namedValues=NamedValues(*(('unencrypted-password',0),('type-7',7)))
_CnHttpClientPasswordType_Type.__name__=_C
_CnHttpClientPasswordType_Object=MibScalar
cnHttpClientPasswordType=_CnHttpClientPasswordType_Object((1,3,6,1,4,1,17713,24,4,24,6),_CnHttpClientPasswordType_Type())
cnHttpClientPasswordType.setMaxAccess(_B)
if mibBuilder.loadTexts:cnHttpClientPasswordType.setStatus(_A)
class _CambiumSystemLoginBanner_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,900))
_CambiumSystemLoginBanner_Type.__name__=_G
_CambiumSystemLoginBanner_Object=MibScalar
cambiumSystemLoginBanner=_CambiumSystemLoginBanner_Object((1,3,6,1,4,1,17713,24,4,25),_CambiumSystemLoginBanner_Type())
cambiumSystemLoginBanner.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumSystemLoginBanner.setStatus(_A)
class _CambiumSystemMotdBanner_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,900))
_CambiumSystemMotdBanner_Type.__name__=_G
_CambiumSystemMotdBanner_Object=MibScalar
cambiumSystemMotdBanner=_CambiumSystemMotdBanner_Object((1,3,6,1,4,1,17713,24,4,26),_CambiumSystemMotdBanner_Type())
cambiumSystemMotdBanner.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumSystemMotdBanner.setStatus(_A)
_CnCpuRateLimits_ObjectIdentity=ObjectIdentity
cnCpuRateLimits=_CnCpuRateLimits_ObjectIdentity((1,3,6,1,4,1,17713,24,4,27))
class _CnArpBroadCastRateLimit_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(100,65500))
_CnArpBroadCastRateLimit_Type.__name__=_C
_CnArpBroadCastRateLimit_Object=MibScalar
cnArpBroadCastRateLimit=_CnArpBroadCastRateLimit_Object((1,3,6,1,4,1,17713,24,4,27,1),_CnArpBroadCastRateLimit_Type())
cnArpBroadCastRateLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:cnArpBroadCastRateLimit.setStatus(_A)
class _CambiumPasswordEncryption_Type(TruthValue):defaultValue=2
_CambiumPasswordEncryption_Type.__name__=_E
_CambiumPasswordEncryption_Object=MibScalar
cambiumPasswordEncryption=_CambiumPasswordEncryption_Object((1,3,6,1,4,1,17713,24,4,28),_CambiumPasswordEncryption_Type())
cambiumPasswordEncryption.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumPasswordEncryption.setStatus(_A)
mibBuilder.exportSymbols('CAMBIUM-NETWORKS-SYSTEM-MIB',**{'cnSystem':cnSystem,'cambiumScheduledReload':cambiumScheduledReload,'cambiumReloadRelativeTime':cambiumReloadRelativeTime,'cambiumReloadAbsoluteTime':cambiumReloadAbsoluteTime,'cambiumReloadReason':cambiumReloadReason,'cambiumLastReloadReason':cambiumLastReloadReason,'cambiumStpMode':cambiumStpMode,'cambiumXMSInterfaceIP':cambiumXMSInterfaceIP,'cambiumXMSInterfaceMask':cambiumXMSInterfaceMask,'cambiumXMSInterfaceVLANId':cambiumXMSInterfaceVLANId,'cambiumSystemClock':cambiumSystemClock,'cambiumSystemTimezoneName':cambiumSystemTimezoneName,'cambiumSystemTimezoneOffset':cambiumSystemTimezoneOffset,'cambiumSystemSummerTimeName':cambiumSystemSummerTimeName,'cambiumSystemSummerTimeOffset':cambiumSystemSummerTimeOffset,'cambiumSystemSummerTimeStart':cambiumSystemSummerTimeStart,'cambiumSystemSummerTimeEnd':cambiumSystemSummerTimeEnd,'cambiumSystemRecurringSummerTimeStart':cambiumSystemRecurringSummerTimeStart,'cambiumSystemRecurringSummerTimeEnd':cambiumSystemRecurringSummerTimeEnd,'cambiumSystemSummerTimeMode':cambiumSystemSummerTimeMode,'cambiumReloadDefault':cambiumReloadDefault,'cambiumReloadPartialDefault':cambiumReloadPartialDefault,'cambiumSystemResetButton':cambiumSystemResetButton,'cambiumMstpReset':cambiumMstpReset,'cnHttpClient':cnHttpClient,'cnHttpClientProxyAddress':cnHttpClientProxyAddress,'cnHttpClientProxyAddressType':cnHttpClientProxyAddressType,'cnHttpClientProxyPort':cnHttpClientProxyPort,'cnHttpClientUsername':cnHttpClientUsername,'cnHttpClientPassword':cnHttpClientPassword,'cnHttpClientPasswordType':cnHttpClientPasswordType,'cambiumSystemLoginBanner':cambiumSystemLoginBanner,'cambiumSystemMotdBanner':cambiumSystemMotdBanner,'cnCpuRateLimits':cnCpuRateLimits,'cnArpBroadCastRateLimit':cnArpBroadCastRateLimit,'cambiumPasswordEncryption':cambiumPasswordEncryption})