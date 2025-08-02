_k='kxadminFatalErr'
_j='kxtrunkLinkCount'
_i='kxtrunkLinkOrdinal'
_h='kxtrunkLastError'
_g='kxtrunkRemoteIp'
_f='kxtrunkRemoteBridgeAddr'
_e='kxtrunkState'
_d='kxadminNAMReceiveCongests'
_c='kxifRxQueueThreshTime'
_b='kxifFunction'
_a='kxtrapEntryIndex'
_Z='kxtrapIndex'
_Y='kxWorkGroupNumber'
_X='kxtrunkIfIndex'
_W='kxprotoIfIndex'
_V='kxuartIndex'
_U='kxifIndex'
_T='kxswIndex'
_S='NotificationType'
_R='ifOutErrors'
_Q='ifInErrors'
_P='critical'
_O='major'
_N='minor'
_M='warning'
_L='informational'
_K='enabled'
_J='IF-MIB'
_I='disabled'
_H='false'
_G='true'
_F='kxtrapSeverity'
_E='Integer32'
_D='CT-ELS100-MIB'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifInErrors,ifOutErrors=mibBuilder.importSymbols(_J,_Q,_R)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysObjectID,=mibBuilder.importSymbols('SNMPv2-MIB','sysObjectID')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier',_S,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_S,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Sigma_ObjectIdentity=ObjectIdentity
sigma=_Sigma_ObjectIdentity((1,3,6,1,4,1,97))
_Sys_ObjectIdentity=ObjectIdentity
sys=_Sys_ObjectIdentity((1,3,6,1,4,1,97,1))
class _SysID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(8));namedValues=NamedValues(('els-100-bridge',8))
_SysID_Type.__name__=_E
_SysID_Object=MibScalar
sysID=_SysID_Object((1,3,6,1,4,1,97,1,1),_SysID_Type())
sysID.setMaxAccess(_B)
if mibBuilder.loadTexts:sysID.setStatus(_A)
_SysReset_Type=TimeTicks
_SysReset_Object=MibScalar
sysReset=_SysReset_Object((1,3,6,1,4,1,97,1,2),_SysReset_Type())
sysReset.setMaxAccess(_C)
if mibBuilder.loadTexts:sysReset.setStatus(_A)
_SysTrapPort_Type=Integer32
_SysTrapPort_Object=MibScalar
sysTrapPort=_SysTrapPort_Object((1,3,6,1,4,1,97,1,3),_SysTrapPort_Type())
sysTrapPort.setMaxAccess(_C)
if mibBuilder.loadTexts:sysTrapPort.setStatus(_A)
_Els_100_ObjectIdentity=ObjectIdentity
els_100=_Els_100_ObjectIdentity((1,3,6,1,4,1,97,8))
_Kxhw_ObjectIdentity=ObjectIdentity
kxhw=_Kxhw_ObjectIdentity((1,3,6,1,4,1,97,8,1))
_KxhwDiagCode_Type=OctetString
_KxhwDiagCode_Object=MibScalar
kxhwDiagCode=_KxhwDiagCode_Object((1,3,6,1,4,1,97,8,1,1),_KxhwDiagCode_Type())
kxhwDiagCode.setMaxAccess(_B)
if mibBuilder.loadTexts:kxhwDiagCode.setStatus(_A)
_KxhwManufData_Type=OctetString
_KxhwManufData_Object=MibScalar
kxhwManufData=_KxhwManufData_Object((1,3,6,1,4,1,97,8,1,2),_KxhwManufData_Type())
kxhwManufData.setMaxAccess(_B)
if mibBuilder.loadTexts:kxhwManufData.setStatus(_A)
_KxhwPortCount_Type=Integer32
_KxhwPortCount_Object=MibScalar
kxhwPortCount=_KxhwPortCount_Object((1,3,6,1,4,1,97,8,1,3),_KxhwPortCount_Type())
kxhwPortCount.setMaxAccess(_B)
if mibBuilder.loadTexts:kxhwPortCount.setStatus(_A)
_Kxsw_ObjectIdentity=ObjectIdentity
kxsw=_Kxsw_ObjectIdentity((1,3,6,1,4,1,97,8,2))
_KxswNumber_Type=Integer32
_KxswNumber_Object=MibScalar
kxswNumber=_KxswNumber_Object((1,3,6,1,4,1,97,8,2,1),_KxswNumber_Type())
kxswNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:kxswNumber.setStatus(_A)
_KxswFilesetTable_Object=MibTable
kxswFilesetTable=_KxswFilesetTable_Object((1,3,6,1,4,1,97,8,2,2))
if mibBuilder.loadTexts:kxswFilesetTable.setStatus(_A)
_KxswFilesetEntry_Object=MibTableRow
kxswFilesetEntry=_KxswFilesetEntry_Object((1,3,6,1,4,1,97,8,2,2,1))
kxswFilesetEntry.setIndexNames((0,_D,_T))
if mibBuilder.loadTexts:kxswFilesetEntry.setStatus(_A)
class _KxswIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('currently-executing',1),('next-boot',2)))
_KxswIndex_Type.__name__=_E
_KxswIndex_Object=MibTableColumn
kxswIndex=_KxswIndex_Object((1,3,6,1,4,1,97,8,2,2,1,1),_KxswIndex_Type())
kxswIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:kxswIndex.setStatus(_A)
_KxswDesc_Type=DisplayString
_KxswDesc_Object=MibTableColumn
kxswDesc=_KxswDesc_Object((1,3,6,1,4,1,97,8,2,2,1,2),_KxswDesc_Type())
kxswDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:kxswDesc.setStatus(_A)
_KxswCount_Type=Integer32
_KxswCount_Object=MibTableColumn
kxswCount=_KxswCount_Object((1,3,6,1,4,1,97,8,2,2,1,3),_KxswCount_Type())
kxswCount.setMaxAccess(_B)
if mibBuilder.loadTexts:kxswCount.setStatus(_A)
_KxswType_Type=OctetString
_KxswType_Object=MibTableColumn
kxswType=_KxswType_Object((1,3,6,1,4,1,97,8,2,2,1,4),_KxswType_Type())
kxswType.setMaxAccess(_B)
if mibBuilder.loadTexts:kxswType.setStatus(_A)
_KxswSizes_Type=OctetString
_KxswSizes_Object=MibTableColumn
kxswSizes=_KxswSizes_Object((1,3,6,1,4,1,97,8,2,2,1,5),_KxswSizes_Type())
kxswSizes.setMaxAccess(_B)
if mibBuilder.loadTexts:kxswSizes.setStatus(_A)
_KxswStarts_Type=OctetString
_KxswStarts_Object=MibTableColumn
kxswStarts=_KxswStarts_Object((1,3,6,1,4,1,97,8,2,2,1,6),_KxswStarts_Type())
kxswStarts.setMaxAccess(_B)
if mibBuilder.loadTexts:kxswStarts.setStatus(_A)
_KxswBases_Type=OctetString
_KxswBases_Object=MibTableColumn
kxswBases=_KxswBases_Object((1,3,6,1,4,1,97,8,2,2,1,7),_KxswBases_Type())
kxswBases.setMaxAccess(_B)
if mibBuilder.loadTexts:kxswBases.setStatus(_A)
class _KxswFlashBank_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('first-bank',1),('second-bank',2)))
_KxswFlashBank_Type.__name__=_E
_KxswFlashBank_Object=MibTableColumn
kxswFlashBank=_KxswFlashBank_Object((1,3,6,1,4,1,97,8,2,2,1,8),_KxswFlashBank_Type())
kxswFlashBank.setMaxAccess(_B)
if mibBuilder.loadTexts:kxswFlashBank.setStatus(_A)
_Kxadmin_ObjectIdentity=ObjectIdentity
kxadmin=_Kxadmin_ObjectIdentity((1,3,6,1,4,1,97,8,3))
_KxadminFatalErr_Type=OctetString
_KxadminFatalErr_Object=MibScalar
kxadminFatalErr=_KxadminFatalErr_Object((1,3,6,1,4,1,97,8,3,1),_KxadminFatalErr_Type())
kxadminFatalErr.setMaxAccess(_B)
if mibBuilder.loadTexts:kxadminFatalErr.setStatus(_A)
_KxadminAnyPass_Type=OctetString
_KxadminAnyPass_Object=MibScalar
kxadminAnyPass=_KxadminAnyPass_Object((1,3,6,1,4,1,97,8,3,2),_KxadminAnyPass_Type())
kxadminAnyPass.setMaxAccess(_C)
if mibBuilder.loadTexts:kxadminAnyPass.setStatus(_A)
_KxadminGetPass_Type=OctetString
_KxadminGetPass_Object=MibScalar
kxadminGetPass=_KxadminGetPass_Object((1,3,6,1,4,1,97,8,3,3),_KxadminGetPass_Type())
kxadminGetPass.setMaxAccess(_C)
if mibBuilder.loadTexts:kxadminGetPass.setStatus(_A)
_KxadminNMSIPAddr_Type=IpAddress
_KxadminNMSIPAddr_Object=MibScalar
kxadminNMSIPAddr=_KxadminNMSIPAddr_Object((1,3,6,1,4,1,97,8,3,4),_KxadminNMSIPAddr_Type())
kxadminNMSIPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:kxadminNMSIPAddr.setStatus(_A)
class _KxadminStorageFailure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_KxadminStorageFailure_Type.__name__=_E
_KxadminStorageFailure_Object=MibScalar
kxadminStorageFailure=_KxadminStorageFailure_Object((1,3,6,1,4,1,97,8,3,5),_KxadminStorageFailure_Type())
kxadminStorageFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:kxadminStorageFailure.setStatus(_A)
_KxadminAuthenticationFailure_Type=IpAddress
_KxadminAuthenticationFailure_Object=MibScalar
kxadminAuthenticationFailure=_KxadminAuthenticationFailure_Object((1,3,6,1,4,1,97,8,3,6),_KxadminAuthenticationFailure_Type())
kxadminAuthenticationFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:kxadminAuthenticationFailure.setStatus(_A)
_KxadminNAMReceiveCongests_Type=Counter32
_KxadminNAMReceiveCongests_Object=MibScalar
kxadminNAMReceiveCongests=_KxadminNAMReceiveCongests_Object((1,3,6,1,4,1,97,8,3,7),_KxadminNAMReceiveCongests_Type())
kxadminNAMReceiveCongests.setMaxAccess(_B)
if mibBuilder.loadTexts:kxadminNAMReceiveCongests.setStatus(_A)
_KxadminArpEntries_Type=Counter32
_KxadminArpEntries_Object=MibScalar
kxadminArpEntries=_KxadminArpEntries_Object((1,3,6,1,4,1,97,8,3,8),_KxadminArpEntries_Type())
kxadminArpEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:kxadminArpEntries.setStatus(_A)
_KxadminArpStatics_Type=Counter32
_KxadminArpStatics_Object=MibScalar
kxadminArpStatics=_KxadminArpStatics_Object((1,3,6,1,4,1,97,8,3,9),_KxadminArpStatics_Type())
kxadminArpStatics.setMaxAccess(_B)
if mibBuilder.loadTexts:kxadminArpStatics.setStatus(_A)
_KxadminArpOverflows_Type=Counter32
_KxadminArpOverflows_Object=MibScalar
kxadminArpOverflows=_KxadminArpOverflows_Object((1,3,6,1,4,1,97,8,3,10),_KxadminArpOverflows_Type())
kxadminArpOverflows.setMaxAccess(_B)
if mibBuilder.loadTexts:kxadminArpOverflows.setStatus(_A)
_KxadminRipPreference_Type=Integer32
_KxadminRipPreference_Object=MibScalar
kxadminRipPreference=_KxadminRipPreference_Object((1,3,6,1,4,1,97,8,3,11),_KxadminRipPreference_Type())
kxadminRipPreference.setMaxAccess(_C)
if mibBuilder.loadTexts:kxadminRipPreference.setStatus(_A)
_KxadminRipRouteDiscards_Type=Counter32
_KxadminRipRouteDiscards_Object=MibScalar
kxadminRipRouteDiscards=_KxadminRipRouteDiscards_Object((1,3,6,1,4,1,97,8,3,12),_KxadminRipRouteDiscards_Type())
kxadminRipRouteDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:kxadminRipRouteDiscards.setStatus(_A)
class _KxadminRebootConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('no-change',1),('tftp-config',2),('revert-to-defaults',3)))
_KxadminRebootConfig_Type.__name__=_E
_KxadminRebootConfig_Object=MibScalar
kxadminRebootConfig=_KxadminRebootConfig_Object((1,3,6,1,4,1,97,8,3,13),_KxadminRebootConfig_Type())
kxadminRebootConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:kxadminRebootConfig.setStatus(_A)
class _KxadminDisableButton_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_KxadminDisableButton_Type.__name__=_E
_KxadminDisableButton_Object=MibScalar
kxadminDisableButton=_KxadminDisableButton_Object((1,3,6,1,4,1,97,8,3,14),_KxadminDisableButton_Type())
kxadminDisableButton.setMaxAccess(_C)
if mibBuilder.loadTexts:kxadminDisableButton.setStatus(_A)
class _KxadminButtonSelection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('led-any-activity',1),('led-rx-activity',2),('led-tx-activity',3),('led-any-collision',4),('led-programmed',5),('led-duplex',6),('led-speed',7),('led-mirror',8)))
_KxadminButtonSelection_Type.__name__=_E
_KxadminButtonSelection_Object=MibScalar
kxadminButtonSelection=_KxadminButtonSelection_Object((1,3,6,1,4,1,97,8,3,15),_KxadminButtonSelection_Type())
kxadminButtonSelection.setMaxAccess(_C)
if mibBuilder.loadTexts:kxadminButtonSelection.setStatus(_A)
class _KxadminLEDProgramOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('program-led-any-error',1))
_KxadminLEDProgramOption_Type.__name__=_E
_KxadminLEDProgramOption_Object=MibScalar
kxadminLEDProgramOption=_KxadminLEDProgramOption_Object((1,3,6,1,4,1,97,8,3,16),_KxadminLEDProgramOption_Type())
kxadminLEDProgramOption.setMaxAccess(_C)
if mibBuilder.loadTexts:kxadminLEDProgramOption.setStatus(_A)
_Kxswdis_ObjectIdentity=ObjectIdentity
kxswdis=_Kxswdis_ObjectIdentity((1,3,6,1,4,1,97,8,4))
_KxswdisDesc_Type=OctetString
_KxswdisDesc_Object=MibScalar
kxswdisDesc=_KxswdisDesc_Object((1,3,6,1,4,1,97,8,4,1),_KxswdisDesc_Type())
kxswdisDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:kxswdisDesc.setStatus(_A)
class _KxswdisAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('protected',1),('any-software',2)))
_KxswdisAccess_Type.__name__=_E
_KxswdisAccess_Object=MibScalar
kxswdisAccess=_KxswdisAccess_Object((1,3,6,1,4,1,97,8,4,2),_KxswdisAccess_Type())
kxswdisAccess.setMaxAccess(_C)
if mibBuilder.loadTexts:kxswdisAccess.setStatus(_A)
class _KxswdisWriteStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('in-progress',1),('success',2),('config-error',3),('flash-error',4),('config-and-flash-errors',5)))
_KxswdisWriteStatus_Type.__name__=_E
_KxswdisWriteStatus_Object=MibScalar
kxswdisWriteStatus=_KxswdisWriteStatus_Object((1,3,6,1,4,1,97,8,4,3),_KxswdisWriteStatus_Type())
kxswdisWriteStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:kxswdisWriteStatus.setStatus(_A)
_KxswdisConfigIp_Type=IpAddress
_KxswdisConfigIp_Object=MibScalar
kxswdisConfigIp=_KxswdisConfigIp_Object((1,3,6,1,4,1,97,8,4,4),_KxswdisConfigIp_Type())
kxswdisConfigIp.setMaxAccess(_C)
if mibBuilder.loadTexts:kxswdisConfigIp.setStatus(_A)
_KxswdisConfigRetryTime_Type=Integer32
_KxswdisConfigRetryTime_Object=MibScalar
kxswdisConfigRetryTime=_KxswdisConfigRetryTime_Object((1,3,6,1,4,1,97,8,4,5),_KxswdisConfigRetryTime_Type())
kxswdisConfigRetryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:kxswdisConfigRetryTime.setStatus(_A)
_KxswdisConfigTotalTimeout_Type=Integer32
_KxswdisConfigTotalTimeout_Object=MibScalar
kxswdisConfigTotalTimeout=_KxswdisConfigTotalTimeout_Object((1,3,6,1,4,1,97,8,4,6),_KxswdisConfigTotalTimeout_Type())
kxswdisConfigTotalTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:kxswdisConfigTotalTimeout.setStatus(_A)
_Kxaddr_ObjectIdentity=ObjectIdentity
kxaddr=_Kxaddr_ObjectIdentity((1,3,6,1,4,1,97,8,5))
_KxaddrStatics_Type=Counter32
_KxaddrStatics_Object=MibScalar
kxaddrStatics=_KxaddrStatics_Object((1,3,6,1,4,1,97,8,5,1),_KxaddrStatics_Type())
kxaddrStatics.setMaxAccess(_B)
if mibBuilder.loadTexts:kxaddrStatics.setStatus(_A)
_KxaddrDynamics_Type=Counter32
_KxaddrDynamics_Object=MibScalar
kxaddrDynamics=_KxaddrDynamics_Object((1,3,6,1,4,1,97,8,5,2),_KxaddrDynamics_Type())
kxaddrDynamics.setMaxAccess(_B)
if mibBuilder.loadTexts:kxaddrDynamics.setStatus(_A)
_KxaddrDynamicMax_Type=Gauge32
_KxaddrDynamicMax_Object=MibScalar
kxaddrDynamicMax=_KxaddrDynamicMax_Object((1,3,6,1,4,1,97,8,5,3),_KxaddrDynamicMax_Type())
kxaddrDynamicMax.setMaxAccess(_C)
if mibBuilder.loadTexts:kxaddrDynamicMax.setStatus(_A)
_KxaddrDynamicOverflows_Type=Counter32
_KxaddrDynamicOverflows_Object=MibScalar
kxaddrDynamicOverflows=_KxaddrDynamicOverflows_Object((1,3,6,1,4,1,97,8,5,4),_KxaddrDynamicOverflows_Type())
kxaddrDynamicOverflows.setMaxAccess(_B)
if mibBuilder.loadTexts:kxaddrDynamicOverflows.setStatus(_A)
_KxaddrFlags_Type=Integer32
_KxaddrFlags_Object=MibScalar
kxaddrFlags=_KxaddrFlags_Object((1,3,6,1,4,1,97,8,5,5),_KxaddrFlags_Type())
kxaddrFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:kxaddrFlags.setStatus(_A)
_KxaddrMAC_Type=OctetString
_KxaddrMAC_Object=MibScalar
kxaddrMAC=_KxaddrMAC_Object((1,3,6,1,4,1,97,8,5,6),_KxaddrMAC_Type())
kxaddrMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:kxaddrMAC.setStatus(_A)
_KxaddrPort_Type=Integer32
_KxaddrPort_Object=MibScalar
kxaddrPort=_KxaddrPort_Object((1,3,6,1,4,1,97,8,5,7),_KxaddrPort_Type())
kxaddrPort.setMaxAccess(_C)
if mibBuilder.loadTexts:kxaddrPort.setStatus(_A)
class _KxaddrOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5,6)));namedValues=NamedValues(*(('read-random',1),('read-next',2),('update',4),('delete',5),('read-block',6)))
_KxaddrOperation_Type.__name__=_E
_KxaddrOperation_Object=MibScalar
kxaddrOperation=_KxaddrOperation_Object((1,3,6,1,4,1,97,8,5,8),_KxaddrOperation_Type())
kxaddrOperation.setMaxAccess(_C)
if mibBuilder.loadTexts:kxaddrOperation.setStatus(_A)
_KxaddrIndex_Type=Integer32
_KxaddrIndex_Object=MibScalar
kxaddrIndex=_KxaddrIndex_Object((1,3,6,1,4,1,97,8,5,9),_KxaddrIndex_Type())
kxaddrIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:kxaddrIndex.setStatus(_A)
_KxaddrNext_Type=Integer32
_KxaddrNext_Object=MibScalar
kxaddrNext=_KxaddrNext_Object((1,3,6,1,4,1,97,8,5,10),_KxaddrNext_Type())
kxaddrNext.setMaxAccess(_C)
if mibBuilder.loadTexts:kxaddrNext.setStatus(_A)
_KxaddrBlockSize_Type=Integer32
_KxaddrBlockSize_Object=MibScalar
kxaddrBlockSize=_KxaddrBlockSize_Object((1,3,6,1,4,1,97,8,5,11),_KxaddrBlockSize_Type())
kxaddrBlockSize.setMaxAccess(_C)
if mibBuilder.loadTexts:kxaddrBlockSize.setStatus(_A)
_KxaddrBlock_Type=OctetString
_KxaddrBlock_Object=MibScalar
kxaddrBlock=_KxaddrBlock_Object((1,3,6,1,4,1,97,8,5,12),_KxaddrBlock_Type())
kxaddrBlock.setMaxAccess(_C)
if mibBuilder.loadTexts:kxaddrBlock.setStatus(_A)
_Kxif_ObjectIdentity=ObjectIdentity
kxif=_Kxif_ObjectIdentity((1,3,6,1,4,1,97,8,6))
_KxifTable_Object=MibTable
kxifTable=_KxifTable_Object((1,3,6,1,4,1,97,8,6,1))
if mibBuilder.loadTexts:kxifTable.setStatus(_A)
_KxifEntry_Object=MibTableRow
kxifEntry=_KxifEntry_Object((1,3,6,1,4,1,97,8,6,1,1))
kxifEntry.setIndexNames((0,_D,_U))
if mibBuilder.loadTexts:kxifEntry.setStatus(_A)
_KxifIndex_Type=Integer32
_KxifIndex_Object=MibTableColumn
kxifIndex=_KxifIndex_Object((1,3,6,1,4,1,97,8,6,1,1,1),_KxifIndex_Type())
kxifIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:kxifIndex.setStatus(_A)
_KxifRxCnt_Type=Integer32
_KxifRxCnt_Object=MibTableColumn
kxifRxCnt=_KxifRxCnt_Object((1,3,6,1,4,1,97,8,6,1,1,2),_KxifRxCnt_Type())
kxifRxCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:kxifRxCnt.setStatus(_A)
_KxifTxCnt_Type=Integer32
_KxifTxCnt_Object=MibTableColumn
kxifTxCnt=_KxifTxCnt_Object((1,3,6,1,4,1,97,8,6,1,1,3),_KxifTxCnt_Type())
kxifTxCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:kxifTxCnt.setStatus(_A)
_KxifThreshold_Type=Integer32
_KxifThreshold_Object=MibTableColumn
kxifThreshold=_KxifThreshold_Object((1,3,6,1,4,1,97,8,6,1,1,4),_KxifThreshold_Type())
kxifThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:kxifThreshold.setStatus(_A)
_KxifThresholdTime_Type=Integer32
_KxifThresholdTime_Object=MibTableColumn
kxifThresholdTime=_KxifThresholdTime_Object((1,3,6,1,4,1,97,8,6,1,1,5),_KxifThresholdTime_Type())
kxifThresholdTime.setMaxAccess(_C)
if mibBuilder.loadTexts:kxifThresholdTime.setStatus(_A)
_KxifRxQueueThresh_Type=Integer32
_KxifRxQueueThresh_Object=MibTableColumn
kxifRxQueueThresh=_KxifRxQueueThresh_Object((1,3,6,1,4,1,97,8,6,1,1,6),_KxifRxQueueThresh_Type())
kxifRxQueueThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:kxifRxQueueThresh.setStatus(_A)
_KxifRxQueueThreshTime_Type=Integer32
_KxifRxQueueThreshTime_Object=MibTableColumn
kxifRxQueueThreshTime=_KxifRxQueueThreshTime_Object((1,3,6,1,4,1,97,8,6,1,1,7),_KxifRxQueueThreshTime_Type())
kxifRxQueueThreshTime.setMaxAccess(_C)
if mibBuilder.loadTexts:kxifRxQueueThreshTime.setStatus(_A)
_KxifFunction_Type=Integer32
_KxifFunction_Object=MibTableColumn
kxifFunction=_KxifFunction_Object((1,3,6,1,4,1,97,8,6,1,1,8),_KxifFunction_Type())
kxifFunction.setMaxAccess(_B)
if mibBuilder.loadTexts:kxifFunction.setStatus(_A)
_KxifStatisticsTime_Type=TimeTicks
_KxifStatisticsTime_Object=MibTableColumn
kxifStatisticsTime=_KxifStatisticsTime_Object((1,3,6,1,4,1,97,8,6,1,1,9),_KxifStatisticsTime_Type())
kxifStatisticsTime.setMaxAccess(_B)
if mibBuilder.loadTexts:kxifStatisticsTime.setStatus(_A)
_Kxuart_ObjectIdentity=ObjectIdentity
kxuart=_Kxuart_ObjectIdentity((1,3,6,1,4,1,97,8,7))
_KxuartTable_Object=MibTable
kxuartTable=_KxuartTable_Object((1,3,6,1,4,1,97,8,7,1))
if mibBuilder.loadTexts:kxuartTable.setStatus(_A)
_KxuartEntry_Object=MibTableRow
kxuartEntry=_KxuartEntry_Object((1,3,6,1,4,1,97,8,7,1,1))
kxuartEntry.setIndexNames((0,_D,_V))
if mibBuilder.loadTexts:kxuartEntry.setStatus(_A)
_KxuartIndex_Type=Integer32
_KxuartIndex_Object=MibTableColumn
kxuartIndex=_KxuartIndex_Object((1,3,6,1,4,1,97,8,7,1,1,1),_KxuartIndex_Type())
kxuartIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:kxuartIndex.setStatus(_A)
class _KxuartBaud_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('external-clock',1),('b1200-baud',2),('b2400-baud',3),('b4800-baud',4),('b9600-baud',5),('b19200-baud',6),('b38400-baud',7),('b56-kilobits',8),('b1544-kilobits',9),('b2048-kilobits',10),('b45-megabits',11)))
_KxuartBaud_Type.__name__=_E
_KxuartBaud_Object=MibTableColumn
kxuartBaud=_KxuartBaud_Object((1,3,6,1,4,1,97,8,7,1,1,2),_KxuartBaud_Type())
kxuartBaud.setMaxAccess(_C)
if mibBuilder.loadTexts:kxuartBaud.setStatus(_A)
_KxuartAlignmentErrors_Type=Counter32
_KxuartAlignmentErrors_Object=MibTableColumn
kxuartAlignmentErrors=_KxuartAlignmentErrors_Object((1,3,6,1,4,1,97,8,7,1,1,3),_KxuartAlignmentErrors_Type())
kxuartAlignmentErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:kxuartAlignmentErrors.setStatus(_A)
_KxuartOverrunErrors_Type=Counter32
_KxuartOverrunErrors_Object=MibTableColumn
kxuartOverrunErrors=_KxuartOverrunErrors_Object((1,3,6,1,4,1,97,8,7,1,1,4),_KxuartOverrunErrors_Type())
kxuartOverrunErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:kxuartOverrunErrors.setStatus(_A)
_Kxproto_ObjectIdentity=ObjectIdentity
kxproto=_Kxproto_ObjectIdentity((1,3,6,1,4,1,97,8,8))
_KxprotoTable_Object=MibTable
kxprotoTable=_KxprotoTable_Object((1,3,6,1,4,1,97,8,8,1))
if mibBuilder.loadTexts:kxprotoTable.setStatus(_A)
_KxprotoEntry_Object=MibTableRow
kxprotoEntry=_KxprotoEntry_Object((1,3,6,1,4,1,97,8,8,1,1))
kxprotoEntry.setIndexNames((0,_D,_W))
if mibBuilder.loadTexts:kxprotoEntry.setStatus(_A)
_KxprotoIfIndex_Type=Integer32
_KxprotoIfIndex_Object=MibTableColumn
kxprotoIfIndex=_KxprotoIfIndex_Object((1,3,6,1,4,1,97,8,8,1,1,1),_KxprotoIfIndex_Type())
kxprotoIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:kxprotoIfIndex.setStatus(_A)
class _KxprotoBridge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4)));namedValues=NamedValues(*(('transparent',1),('none',4)))
_KxprotoBridge_Type.__name__=_E
_KxprotoBridge_Object=MibTableColumn
kxprotoBridge=_KxprotoBridge_Object((1,3,6,1,4,1,97,8,8,1,1,2),_KxprotoBridge_Type())
kxprotoBridge.setMaxAccess(_C)
if mibBuilder.loadTexts:kxprotoBridge.setStatus(_A)
class _KxprotoSuppressBpdu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('suppressed',2)))
_KxprotoSuppressBpdu_Type.__name__=_E
_KxprotoSuppressBpdu_Object=MibTableColumn
kxprotoSuppressBpdu=_KxprotoSuppressBpdu_Object((1,3,6,1,4,1,97,8,8,1,1,3),_KxprotoSuppressBpdu_Type())
kxprotoSuppressBpdu.setMaxAccess(_C)
if mibBuilder.loadTexts:kxprotoSuppressBpdu.setStatus(_A)
class _KxprotoRipListen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_I,2)))
_KxprotoRipListen_Type.__name__=_E
_KxprotoRipListen_Object=MibTableColumn
kxprotoRipListen=_KxprotoRipListen_Object((1,3,6,1,4,1,97,8,8,1,1,4),_KxprotoRipListen_Type())
kxprotoRipListen.setMaxAccess(_C)
if mibBuilder.loadTexts:kxprotoRipListen.setStatus(_A)
class _KxprotoTrunking_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_I,2)))
_KxprotoTrunking_Type.__name__=_E
_KxprotoTrunking_Object=MibTableColumn
kxprotoTrunking=_KxprotoTrunking_Object((1,3,6,1,4,1,97,8,8,1,1,5),_KxprotoTrunking_Type())
kxprotoTrunking.setMaxAccess(_C)
if mibBuilder.loadTexts:kxprotoTrunking.setStatus(_A)
_Kxtrunk_ObjectIdentity=ObjectIdentity
kxtrunk=_Kxtrunk_ObjectIdentity((1,3,6,1,4,1,97,8,9))
_KxtrunkTable_Object=MibTable
kxtrunkTable=_KxtrunkTable_Object((1,3,6,1,4,1,97,8,9,1))
if mibBuilder.loadTexts:kxtrunkTable.setStatus(_A)
_KxtrunkEntry_Object=MibTableRow
kxtrunkEntry=_KxtrunkEntry_Object((1,3,6,1,4,1,97,8,9,1,1))
kxtrunkEntry.setIndexNames((0,_D,_X))
if mibBuilder.loadTexts:kxtrunkEntry.setStatus(_A)
_KxtrunkIfIndex_Type=Integer32
_KxtrunkIfIndex_Object=MibTableColumn
kxtrunkIfIndex=_KxtrunkIfIndex_Object((1,3,6,1,4,1,97,8,9,1,1,1),_KxtrunkIfIndex_Type())
kxtrunkIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:kxtrunkIfIndex.setStatus(_A)
class _KxtrunkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('off',1),('closed',2),('oneway',3),('joined',4),('perturbed',5),('helddown',6),(_I,7)))
_KxtrunkState_Type.__name__=_E
_KxtrunkState_Object=MibTableColumn
kxtrunkState=_KxtrunkState_Object((1,3,6,1,4,1,97,8,9,1,1,2),_KxtrunkState_Type())
kxtrunkState.setMaxAccess(_B)
if mibBuilder.loadTexts:kxtrunkState.setStatus(_A)
_KxtrunkRemoteBridgeAddr_Type=OctetString
_KxtrunkRemoteBridgeAddr_Object=MibTableColumn
kxtrunkRemoteBridgeAddr=_KxtrunkRemoteBridgeAddr_Object((1,3,6,1,4,1,97,8,9,1,1,3),_KxtrunkRemoteBridgeAddr_Type())
kxtrunkRemoteBridgeAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:kxtrunkRemoteBridgeAddr.setStatus(_A)
_KxtrunkRemoteIp_Type=IpAddress
_KxtrunkRemoteIp_Object=MibTableColumn
kxtrunkRemoteIp=_KxtrunkRemoteIp_Object((1,3,6,1,4,1,97,8,9,1,1,4),_KxtrunkRemoteIp_Type())
kxtrunkRemoteIp.setMaxAccess(_B)
if mibBuilder.loadTexts:kxtrunkRemoteIp.setStatus(_A)
class _KxtrunkLastError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('none',1),('in-bpdu',2),('multiple-bridges',3),('ack-lost',4),('standby',5),('too-many-groups',6),('no-ack',7),('perturbed-threshold',8),('self-connect',9),('port-moved',10),('multiple-lan-types',11)))
_KxtrunkLastError_Type.__name__=_E
_KxtrunkLastError_Object=MibTableColumn
kxtrunkLastError=_KxtrunkLastError_Object((1,3,6,1,4,1,97,8,9,1,1,5),_KxtrunkLastError_Type())
kxtrunkLastError.setMaxAccess(_B)
if mibBuilder.loadTexts:kxtrunkLastError.setStatus(_A)
_KxtrunkLinkOrdinal_Type=Integer32
_KxtrunkLinkOrdinal_Object=MibTableColumn
kxtrunkLinkOrdinal=_KxtrunkLinkOrdinal_Object((1,3,6,1,4,1,97,8,9,1,1,6),_KxtrunkLinkOrdinal_Type())
kxtrunkLinkOrdinal.setMaxAccess(_B)
if mibBuilder.loadTexts:kxtrunkLinkOrdinal.setStatus(_A)
_KxtrunkLinkCount_Type=Integer32
_KxtrunkLinkCount_Object=MibTableColumn
kxtrunkLinkCount=_KxtrunkLinkCount_Object((1,3,6,1,4,1,97,8,9,1,1,7),_KxtrunkLinkCount_Type())
kxtrunkLinkCount.setMaxAccess(_B)
if mibBuilder.loadTexts:kxtrunkLinkCount.setStatus(_A)
_KxtrunkLastChange_Type=Integer32
_KxtrunkLastChange_Object=MibTableColumn
kxtrunkLastChange=_KxtrunkLastChange_Object((1,3,6,1,4,1,97,8,9,1,1,8),_KxtrunkLastChange_Type())
kxtrunkLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:kxtrunkLastChange.setStatus(_A)
_Kxworkgroup_ObjectIdentity=ObjectIdentity
kxworkgroup=_Kxworkgroup_ObjectIdentity((1,3,6,1,4,1,97,8,10))
_KxWorkGroupNextNumber_Type=Integer32
_KxWorkGroupNextNumber_Object=MibScalar
kxWorkGroupNextNumber=_KxWorkGroupNextNumber_Object((1,3,6,1,4,1,97,8,10,1),_KxWorkGroupNextNumber_Type())
kxWorkGroupNextNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:kxWorkGroupNextNumber.setStatus(_A)
_KxWorkGroupCurrentCount_Type=Integer32
_KxWorkGroupCurrentCount_Object=MibScalar
kxWorkGroupCurrentCount=_KxWorkGroupCurrentCount_Object((1,3,6,1,4,1,97,8,10,2),_KxWorkGroupCurrentCount_Type())
kxWorkGroupCurrentCount.setMaxAccess(_B)
if mibBuilder.loadTexts:kxWorkGroupCurrentCount.setStatus(_A)
_KxWorkGroupMaxCount_Type=Integer32
_KxWorkGroupMaxCount_Object=MibScalar
kxWorkGroupMaxCount=_KxWorkGroupMaxCount_Object((1,3,6,1,4,1,97,8,10,3),_KxWorkGroupMaxCount_Type())
kxWorkGroupMaxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:kxWorkGroupMaxCount.setStatus(_A)
_KxWorkGroupTable_Object=MibTable
kxWorkGroupTable=_KxWorkGroupTable_Object((1,3,6,1,4,1,97,8,10,4))
if mibBuilder.loadTexts:kxWorkGroupTable.setStatus(_A)
_KxWorkGroupEntry_Object=MibTableRow
kxWorkGroupEntry=_KxWorkGroupEntry_Object((1,3,6,1,4,1,97,8,10,4,1))
kxWorkGroupEntry.setIndexNames((0,_D,_Y))
if mibBuilder.loadTexts:kxWorkGroupEntry.setStatus(_A)
_KxWorkGroupNumber_Type=Integer32
_KxWorkGroupNumber_Object=MibTableColumn
kxWorkGroupNumber=_KxWorkGroupNumber_Object((1,3,6,1,4,1,97,8,10,4,1,1),_KxWorkGroupNumber_Type())
kxWorkGroupNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:kxWorkGroupNumber.setStatus(_A)
_KxWorkGroupName_Type=DisplayString
_KxWorkGroupName_Object=MibTableColumn
kxWorkGroupName=_KxWorkGroupName_Object((1,3,6,1,4,1,97,8,10,4,1,2),_KxWorkGroupName_Type())
kxWorkGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:kxWorkGroupName.setStatus(_A)
_KxWorkGroupPorts_Type=OctetString
_KxWorkGroupPorts_Object=MibTableColumn
kxWorkGroupPorts=_KxWorkGroupPorts_Object((1,3,6,1,4,1,97,8,10,4,1,3),_KxWorkGroupPorts_Type())
kxWorkGroupPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:kxWorkGroupPorts.setStatus(_A)
class _KxWorkGroupType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4)));namedValues=NamedValues(*(('all',3),('invalid',4)))
_KxWorkGroupType_Type.__name__=_E
_KxWorkGroupType_Object=MibTableColumn
kxWorkGroupType=_KxWorkGroupType_Object((1,3,6,1,4,1,97,8,10,4,1,4),_KxWorkGroupType_Type())
kxWorkGroupType.setMaxAccess(_C)
if mibBuilder.loadTexts:kxWorkGroupType.setStatus(_A)
_KxtrapMgt_ObjectIdentity=ObjectIdentity
kxtrapMgt=_KxtrapMgt_ObjectIdentity((1,3,6,1,4,1,97,8,11))
_KxtrapControlTable_Object=MibTable
kxtrapControlTable=_KxtrapControlTable_Object((1,3,6,1,4,1,97,8,11,1))
if mibBuilder.loadTexts:kxtrapControlTable.setStatus(_A)
_KxtrapControlEntry_Object=MibTableRow
kxtrapControlEntry=_KxtrapControlEntry_Object((1,3,6,1,4,1,97,8,11,1,1))
kxtrapControlEntry.setIndexNames((0,_D,_Z))
if mibBuilder.loadTexts:kxtrapControlEntry.setStatus(_A)
_KxtrapIndex_Type=Integer32
_KxtrapIndex_Object=MibTableColumn
kxtrapIndex=_KxtrapIndex_Object((1,3,6,1,4,1,97,8,11,1,1,1),_KxtrapIndex_Type())
kxtrapIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:kxtrapIndex.setStatus(_A)
class _KxtrapEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_KxtrapEnabled_Type.__name__=_E
_KxtrapEnabled_Object=MibTableColumn
kxtrapEnabled=_KxtrapEnabled_Object((1,3,6,1,4,1,97,8,11,1,1,2),_KxtrapEnabled_Type())
kxtrapEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:kxtrapEnabled.setStatus(_A)
class _KxtrapSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),(_O,4),(_P,5)))
_KxtrapSeverity_Type.__name__=_E
_KxtrapSeverity_Object=MibTableColumn
kxtrapSeverity=_KxtrapSeverity_Object((1,3,6,1,4,1,97,8,11,1,1,3),_KxtrapSeverity_Type())
kxtrapSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:kxtrapSeverity.setStatus(_A)
_KxtrapText_Type=DisplayString
_KxtrapText_Object=MibTableColumn
kxtrapText=_KxtrapText_Object((1,3,6,1,4,1,97,8,11,1,1,4),_KxtrapText_Type())
kxtrapText.setMaxAccess(_B)
if mibBuilder.loadTexts:kxtrapText.setStatus(_A)
_KxtrapSeverityControlTable_Object=MibTable
kxtrapSeverityControlTable=_KxtrapSeverityControlTable_Object((1,3,6,1,4,1,97,8,11,2))
if mibBuilder.loadTexts:kxtrapSeverityControlTable.setStatus(_A)
_KxtrapSeverityControlEntry_Object=MibTableRow
kxtrapSeverityControlEntry=_KxtrapSeverityControlEntry_Object((1,3,6,1,4,1,97,8,11,2,1))
kxtrapSeverityControlEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:kxtrapSeverityControlEntry.setStatus(_A)
class _KxtrapSeverityControlSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),(_O,4),(_P,5)))
_KxtrapSeverityControlSeverity_Type.__name__=_E
_KxtrapSeverityControlSeverity_Object=MibTableColumn
kxtrapSeverityControlSeverity=_KxtrapSeverityControlSeverity_Object((1,3,6,1,4,1,97,8,11,2,1,1),_KxtrapSeverityControlSeverity_Type())
kxtrapSeverityControlSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:kxtrapSeverityControlSeverity.setStatus(_A)
class _KxtrapSeverityEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_I,2)))
_KxtrapSeverityEnable_Type.__name__=_E
_KxtrapSeverityEnable_Object=MibTableColumn
kxtrapSeverityEnable=_KxtrapSeverityEnable_Object((1,3,6,1,4,1,97,8,11,2,1,2),_KxtrapSeverityEnable_Type())
kxtrapSeverityEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:kxtrapSeverityEnable.setStatus(_A)
class _KxtrapIncludeText_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_KxtrapIncludeText_Type.__name__=_E
_KxtrapIncludeText_Object=MibScalar
kxtrapIncludeText=_KxtrapIncludeText_Object((1,3,6,1,4,1,97,8,11,3),_KxtrapIncludeText_Type())
kxtrapIncludeText.setMaxAccess(_C)
if mibBuilder.loadTexts:kxtrapIncludeText.setStatus(_A)
_KxtrapTime_Type=TimeTicks
_KxtrapTime_Object=MibScalar
kxtrapTime=_KxtrapTime_Object((1,3,6,1,4,1,97,8,11,4),_KxtrapTime_Type())
kxtrapTime.setMaxAccess(_C)
if mibBuilder.loadTexts:kxtrapTime.setStatus(_A)
_KxtrapRetry_Type=Integer32
_KxtrapRetry_Object=MibScalar
kxtrapRetry=_KxtrapRetry_Object((1,3,6,1,4,1,97,8,11,5),_KxtrapRetry_Type())
kxtrapRetry.setMaxAccess(_C)
if mibBuilder.loadTexts:kxtrapRetry.setStatus(_A)
_KxtrapNumber_Type=Integer32
_KxtrapNumber_Object=MibScalar
kxtrapNumber=_KxtrapNumber_Object((1,3,6,1,4,1,97,8,11,6),_KxtrapNumber_Type())
kxtrapNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:kxtrapNumber.setStatus(_A)
_KxtrapTable_Object=MibTable
kxtrapTable=_KxtrapTable_Object((1,3,6,1,4,1,97,8,11,7))
if mibBuilder.loadTexts:kxtrapTable.setStatus(_A)
_KxtrapEntry_Object=MibTableRow
kxtrapEntry=_KxtrapEntry_Object((1,3,6,1,4,1,97,8,11,7,1))
kxtrapEntry.setIndexNames((0,_D,_a))
if mibBuilder.loadTexts:kxtrapEntry.setStatus(_A)
_KxtrapEntryIndex_Type=Integer32
_KxtrapEntryIndex_Object=MibTableColumn
kxtrapEntryIndex=_KxtrapEntryIndex_Object((1,3,6,1,4,1,97,8,11,7,1,1),_KxtrapEntryIndex_Type())
kxtrapEntryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:kxtrapEntryIndex.setStatus(_A)
_KxtrapEntryTimeStamp_Type=TimeTicks
_KxtrapEntryTimeStamp_Object=MibTableColumn
kxtrapEntryTimeStamp=_KxtrapEntryTimeStamp_Object((1,3,6,1,4,1,97,8,11,7,1,2),_KxtrapEntryTimeStamp_Type())
kxtrapEntryTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:kxtrapEntryTimeStamp.setStatus(_A)
_KxtrapEntryText_Type=DisplayString
_KxtrapEntryText_Object=MibTableColumn
kxtrapEntryText=_KxtrapEntryText_Object((1,3,6,1,4,1,97,8,11,7,1,3),_KxtrapEntryText_Type())
kxtrapEntryText.setMaxAccess(_B)
if mibBuilder.loadTexts:kxtrapEntryText.setStatus(_A)
_KxtrapEntryNumber_Type=Integer32
_KxtrapEntryNumber_Object=MibTableColumn
kxtrapEntryNumber=_KxtrapEntryNumber_Object((1,3,6,1,4,1,97,8,11,7,1,4),_KxtrapEntryNumber_Type())
kxtrapEntryNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:kxtrapEntryNumber.setStatus(_A)
class _KxtrapEntrySeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),(_O,4),(_P,5)))
_KxtrapEntrySeverity_Type.__name__=_E
_KxtrapEntrySeverity_Object=MibTableColumn
kxtrapEntrySeverity=_KxtrapEntrySeverity_Object((1,3,6,1,4,1,97,8,11,7,1,5),_KxtrapEntrySeverity_Type())
kxtrapEntrySeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:kxtrapEntrySeverity.setStatus(_A)
_Kxmirrorgroup_ObjectIdentity=ObjectIdentity
kxmirrorgroup=_Kxmirrorgroup_ObjectIdentity((1,3,6,1,4,1,97,8,12))
class _KxmirrorMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('off',1),('tx',2),('rx',3),('rxandtx',4)))
_KxmirrorMode_Type.__name__=_E
_KxmirrorMode_Object=MibScalar
kxmirrorMode=_KxmirrorMode_Object((1,3,6,1,4,1,97,8,12,1),_KxmirrorMode_Type())
kxmirrorMode.setMaxAccess(_C)
if mibBuilder.loadTexts:kxmirrorMode.setStatus(_A)
_KxmirrorDiagPort_Type=Integer32
_KxmirrorDiagPort_Object=MibScalar
kxmirrorDiagPort=_KxmirrorDiagPort_Object((1,3,6,1,4,1,97,8,12,2),_KxmirrorDiagPort_Type())
kxmirrorDiagPort.setMaxAccess(_C)
if mibBuilder.loadTexts:kxmirrorDiagPort.setStatus(_A)
_KxmirrorTargetPortLists_Type=OctetString
_KxmirrorTargetPortLists_Object=MibScalar
kxmirrorTargetPortLists=_KxmirrorTargetPortLists_Object((1,3,6,1,4,1,97,8,12,3),_KxmirrorTargetPortLists_Type())
kxmirrorTargetPortLists.setMaxAccess(_C)
if mibBuilder.loadTexts:kxmirrorTargetPortLists.setStatus(_A)
kxPortFunctionsTrap=NotificationType((1,3,6,1,2,1,1,2,0,1))
kxPortFunctionsTrap.setObjects(*((_D,_F),(_D,_b)))
if mibBuilder.loadTexts:kxPortFunctionsTrap.setStatus('')
kxRxQueuesTrap=NotificationType((1,3,6,1,2,1,1,2,0,2))
kxRxQueuesTrap.setObjects(*((_D,_F),(_D,_c)))
if mibBuilder.loadTexts:kxRxQueuesTrap.setStatus('')
kxTxStormFlagTrap=NotificationType((1,3,6,1,2,1,1,2,0,3))
kxTxStormFlagTrap.setObjects((_D,_F))
if mibBuilder.loadTexts:kxTxStormFlagTrap.setStatus('')
kxTxCongestsTrap=NotificationType((1,3,6,1,2,1,1,2,0,4))
kxTxCongestsTrap.setObjects(*((_D,_F),(_D,_d)))
if mibBuilder.loadTexts:kxTxCongestsTrap.setStatus('')
kxTrunkStateTrap=NotificationType((1,3,6,1,2,1,1,2,0,5))
kxTrunkStateTrap.setObjects(*((_D,_F),(_D,_e)))
if mibBuilder.loadTexts:kxTrunkStateTrap.setStatus('')
kxTrunkBridgeAddrTrap=NotificationType((1,3,6,1,2,1,1,2,0,6))
kxTrunkBridgeAddrTrap.setObjects(*((_D,_F),(_D,_f)))
if mibBuilder.loadTexts:kxTrunkBridgeAddrTrap.setStatus('')
kxTrunkIPAddrTrap=NotificationType((1,3,6,1,2,1,1,2,0,7))
kxTrunkIPAddrTrap.setObjects(*((_D,_F),(_D,_g)))
if mibBuilder.loadTexts:kxTrunkIPAddrTrap.setStatus('')
kxTrunkErrorTrap=NotificationType((1,3,6,1,2,1,1,2,0,8))
kxTrunkErrorTrap.setObjects(*((_D,_F),(_D,_h)))
if mibBuilder.loadTexts:kxTrunkErrorTrap.setStatus('')
kxTrunkLinkOrdinalTrap=NotificationType((1,3,6,1,2,1,1,2,0,9))
kxTrunkLinkOrdinalTrap.setObjects(*((_D,_F),(_D,_i)))
if mibBuilder.loadTexts:kxTrunkLinkOrdinalTrap.setStatus('')
kxTrunkLinkCountTrap=NotificationType((1,3,6,1,2,1,1,2,0,10))
kxTrunkLinkCountTrap.setObjects(*((_D,_F),(_D,_j)))
if mibBuilder.loadTexts:kxTrunkLinkCountTrap.setStatus('')
kxDiagUnitBootedTrap=NotificationType((1,3,6,1,2,1,1,2,0,11))
kxDiagUnitBootedTrap.setObjects(*((_D,_F),(_D,_k)))
if mibBuilder.loadTexts:kxDiagUnitBootedTrap.setStatus('')
kxStorageFailureTrap=NotificationType((1,3,6,1,2,1,1,2,0,12))
kxStorageFailureTrap.setObjects((_D,_F))
if mibBuilder.loadTexts:kxStorageFailureTrap.setStatus('')
kxIfErrorsTrap=NotificationType((1,3,6,1,2,1,1,2,0,13))
kxIfErrorsTrap.setObjects(*((_D,_F),(_J,_Q),(_J,_R)))
if mibBuilder.loadTexts:kxIfErrorsTrap.setStatus('')
mibBuilder.exportSymbols(_D,**{'kxPortFunctionsTrap':kxPortFunctionsTrap,'kxRxQueuesTrap':kxRxQueuesTrap,'kxTxStormFlagTrap':kxTxStormFlagTrap,'kxTxCongestsTrap':kxTxCongestsTrap,'kxTrunkStateTrap':kxTrunkStateTrap,'kxTrunkBridgeAddrTrap':kxTrunkBridgeAddrTrap,'kxTrunkIPAddrTrap':kxTrunkIPAddrTrap,'kxTrunkErrorTrap':kxTrunkErrorTrap,'kxTrunkLinkOrdinalTrap':kxTrunkLinkOrdinalTrap,'kxTrunkLinkCountTrap':kxTrunkLinkCountTrap,'kxDiagUnitBootedTrap':kxDiagUnitBootedTrap,'kxStorageFailureTrap':kxStorageFailureTrap,'kxIfErrorsTrap':kxIfErrorsTrap,'sigma':sigma,'sys':sys,'sysID':sysID,'sysReset':sysReset,'sysTrapPort':sysTrapPort,'els-100':els_100,'kxhw':kxhw,'kxhwDiagCode':kxhwDiagCode,'kxhwManufData':kxhwManufData,'kxhwPortCount':kxhwPortCount,'kxsw':kxsw,'kxswNumber':kxswNumber,'kxswFilesetTable':kxswFilesetTable,'kxswFilesetEntry':kxswFilesetEntry,_T:kxswIndex,'kxswDesc':kxswDesc,'kxswCount':kxswCount,'kxswType':kxswType,'kxswSizes':kxswSizes,'kxswStarts':kxswStarts,'kxswBases':kxswBases,'kxswFlashBank':kxswFlashBank,'kxadmin':kxadmin,_k:kxadminFatalErr,'kxadminAnyPass':kxadminAnyPass,'kxadminGetPass':kxadminGetPass,'kxadminNMSIPAddr':kxadminNMSIPAddr,'kxadminStorageFailure':kxadminStorageFailure,'kxadminAuthenticationFailure':kxadminAuthenticationFailure,_d:kxadminNAMReceiveCongests,'kxadminArpEntries':kxadminArpEntries,'kxadminArpStatics':kxadminArpStatics,'kxadminArpOverflows':kxadminArpOverflows,'kxadminRipPreference':kxadminRipPreference,'kxadminRipRouteDiscards':kxadminRipRouteDiscards,'kxadminRebootConfig':kxadminRebootConfig,'kxadminDisableButton':kxadminDisableButton,'kxadminButtonSelection':kxadminButtonSelection,'kxadminLEDProgramOption':kxadminLEDProgramOption,'kxswdis':kxswdis,'kxswdisDesc':kxswdisDesc,'kxswdisAccess':kxswdisAccess,'kxswdisWriteStatus':kxswdisWriteStatus,'kxswdisConfigIp':kxswdisConfigIp,'kxswdisConfigRetryTime':kxswdisConfigRetryTime,'kxswdisConfigTotalTimeout':kxswdisConfigTotalTimeout,'kxaddr':kxaddr,'kxaddrStatics':kxaddrStatics,'kxaddrDynamics':kxaddrDynamics,'kxaddrDynamicMax':kxaddrDynamicMax,'kxaddrDynamicOverflows':kxaddrDynamicOverflows,'kxaddrFlags':kxaddrFlags,'kxaddrMAC':kxaddrMAC,'kxaddrPort':kxaddrPort,'kxaddrOperation':kxaddrOperation,'kxaddrIndex':kxaddrIndex,'kxaddrNext':kxaddrNext,'kxaddrBlockSize':kxaddrBlockSize,'kxaddrBlock':kxaddrBlock,'kxif':kxif,'kxifTable':kxifTable,'kxifEntry':kxifEntry,_U:kxifIndex,'kxifRxCnt':kxifRxCnt,'kxifTxCnt':kxifTxCnt,'kxifThreshold':kxifThreshold,'kxifThresholdTime':kxifThresholdTime,'kxifRxQueueThresh':kxifRxQueueThresh,_c:kxifRxQueueThreshTime,_b:kxifFunction,'kxifStatisticsTime':kxifStatisticsTime,'kxuart':kxuart,'kxuartTable':kxuartTable,'kxuartEntry':kxuartEntry,_V:kxuartIndex,'kxuartBaud':kxuartBaud,'kxuartAlignmentErrors':kxuartAlignmentErrors,'kxuartOverrunErrors':kxuartOverrunErrors,'kxproto':kxproto,'kxprotoTable':kxprotoTable,'kxprotoEntry':kxprotoEntry,_W:kxprotoIfIndex,'kxprotoBridge':kxprotoBridge,'kxprotoSuppressBpdu':kxprotoSuppressBpdu,'kxprotoRipListen':kxprotoRipListen,'kxprotoTrunking':kxprotoTrunking,'kxtrunk':kxtrunk,'kxtrunkTable':kxtrunkTable,'kxtrunkEntry':kxtrunkEntry,_X:kxtrunkIfIndex,_e:kxtrunkState,_f:kxtrunkRemoteBridgeAddr,_g:kxtrunkRemoteIp,_h:kxtrunkLastError,_i:kxtrunkLinkOrdinal,_j:kxtrunkLinkCount,'kxtrunkLastChange':kxtrunkLastChange,'kxworkgroup':kxworkgroup,'kxWorkGroupNextNumber':kxWorkGroupNextNumber,'kxWorkGroupCurrentCount':kxWorkGroupCurrentCount,'kxWorkGroupMaxCount':kxWorkGroupMaxCount,'kxWorkGroupTable':kxWorkGroupTable,'kxWorkGroupEntry':kxWorkGroupEntry,_Y:kxWorkGroupNumber,'kxWorkGroupName':kxWorkGroupName,'kxWorkGroupPorts':kxWorkGroupPorts,'kxWorkGroupType':kxWorkGroupType,'kxtrapMgt':kxtrapMgt,'kxtrapControlTable':kxtrapControlTable,'kxtrapControlEntry':kxtrapControlEntry,_Z:kxtrapIndex,'kxtrapEnabled':kxtrapEnabled,_F:kxtrapSeverity,'kxtrapText':kxtrapText,'kxtrapSeverityControlTable':kxtrapSeverityControlTable,'kxtrapSeverityControlEntry':kxtrapSeverityControlEntry,'kxtrapSeverityControlSeverity':kxtrapSeverityControlSeverity,'kxtrapSeverityEnable':kxtrapSeverityEnable,'kxtrapIncludeText':kxtrapIncludeText,'kxtrapTime':kxtrapTime,'kxtrapRetry':kxtrapRetry,'kxtrapNumber':kxtrapNumber,'kxtrapTable':kxtrapTable,'kxtrapEntry':kxtrapEntry,_a:kxtrapEntryIndex,'kxtrapEntryTimeStamp':kxtrapEntryTimeStamp,'kxtrapEntryText':kxtrapEntryText,'kxtrapEntryNumber':kxtrapEntryNumber,'kxtrapEntrySeverity':kxtrapEntrySeverity,'kxmirrorgroup':kxmirrorgroup,'kxmirrorMode':kxmirrorMode,'kxmirrorDiagPort':kxmirrorDiagPort,'kxmirrorTargetPortLists':kxmirrorTargetPortLists})