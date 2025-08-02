_AU='els10-27hwDiagCode'
_AT='els10-27adminFatalErr'
_AS='els10-27trunkLinkCount'
_AR='els10-27trunkLinkOrdinal'
_AQ='els10-27trunkLastError'
_AP='els10-27trunkRemoteIp'
_AO='els10-27trunkRemoteBridgeAddr'
_AN='els10-27trunkState'
_AM='els10-27lpbkErrorBadReceives'
_AL='els10-27lpbkErrorNoReceives'
_AK='els10-27lpbkOperation'
_AJ='els10-27debugString'
_AI='els10-27debugStringID'
_AH='els10-27adminNAMReceiveCongests'
_AG='els10-27ifRxQueues'
_AF='els10-27ifFunction'
_AE='els10-27swdisDesc'
_AD='els10-27swdisWriteStatus'
_AC='els10-27FlowControlInterface'
_AB='els10-27igmpCacheIfIndex'
_AA='els10-27igmpCacheAddress'
_A9='els10-27VlanStaticVID'
_A8='els10-27VlanFilterGVRPVID'
_A7='els10-27VlanEgressVID'
_A6='els10-27VlanConfigVID'
_A5='els10-27volmirrorIndex'
_A4='els10-27traceProbe'
_A3='els10-27traceHop'
_A2='els10-27traceDestAddr'
_A1='els10-27traceNMSAddr'
_A0='completed'
_z='not-started'
_y='els10-27pingDestAddr'
_x='els10-27pingNMSAddr'
_w='els10-27trapEntryIndex'
_v='els10-27trapIndex'
_u='els10-27WorkGroupNumber'
_t='els10-27trunkIfIndex'
_s='els10-27protoIfIndex'
_r='els10-27lpbkIndex'
_q='els10-27debugIndex'
_p='els10-27uartIndex'
_o='els10-27dot3Index'
_n='els10-27ifIndex'
_m='els10-27swIndex'
_l='els10-27hwPortIndex'
_k='DisplayString'
_j='NotificationType'
_i='ifOutErrors'
_h='ifOutDiscards'
_g='ifInErrors'
_f='dot1dStpRootPort'
_e='dot1dStpRootCost'
_d='dot1dStpPortDesignatedRoot'
_c='dot1dStpPortDesignatedCost'
_b='dot1dStpPortDesignatedBridge'
_a='dot1dStpMaxAge'
_Z='dot1dStpHelloTime'
_Y='dot1dStpForwardDelay'
_X='dot1dStpDesignatedRoot'
_W='create'
_V='critical'
_U='major'
_T='minor'
_S='warning'
_R='informational'
_Q='dot1dStpPortState'
_P='dot1dStpPortDesignatedPort'
_O='off'
_N='delete'
_M='IF-MIB'
_L='false'
_K='true'
_J='disabled'
_I='enabled'
_H='OctetString'
_G='BRIDGE-MIB'
_F='els10-27trapSeverity'
_E='Integer32'
_D='CT-ELS10-27-MIB'
_C='read-only'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dStpDesignatedRoot,dot1dStpForwardDelay,dot1dStpHelloTime,dot1dStpMaxAge,dot1dStpPortDesignatedBridge,dot1dStpPortDesignatedCost,dot1dStpPortDesignatedPort,dot1dStpPortDesignatedRoot,dot1dStpPortState,dot1dStpRootCost,dot1dStpRootPort=mibBuilder.importSymbols(_G,_X,_Y,_Z,_a,_b,_c,_P,_d,_Q,_e,_f)
ifInErrors,ifOutDiscards,ifOutErrors=mibBuilder.importSymbols(_M,_g,_h,_i)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysObjectID,=mibBuilder.importSymbols('SNMPv2-MIB','sysObjectID')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier',_j,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_j,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_k,'PhysAddress','TextualConvention')
_Sigma_ObjectIdentity=ObjectIdentity
sigma=_Sigma_ObjectIdentity((1,3,6,1,4,1,97))
_Sys_ObjectIdentity=ObjectIdentity
sys=_Sys_ObjectIdentity((1,3,6,1,4,1,97,1))
class _SysID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(7));namedValues=NamedValues(('els10-27-bridge',7))
_SysID_Type.__name__=_E
_SysID_Object=MibScalar
sysID=_SysID_Object((1,3,6,1,4,1,97,1,1),_SysID_Type())
sysID.setMaxAccess(_C)
if mibBuilder.loadTexts:sysID.setStatus(_A)
_SysReset_Type=TimeTicks
_SysReset_Object=MibScalar
sysReset=_SysReset_Object((1,3,6,1,4,1,97,1,2),_SysReset_Type())
sysReset.setMaxAccess(_B)
if mibBuilder.loadTexts:sysReset.setStatus(_A)
_SysTrapPort_Type=Integer32
_SysTrapPort_Object=MibScalar
sysTrapPort=_SysTrapPort_Object((1,3,6,1,4,1,97,1,6),_SysTrapPort_Type())
sysTrapPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sysTrapPort.setStatus(_A)
_Els10_27_ObjectIdentity=ObjectIdentity
els10_27=_Els10_27_ObjectIdentity((1,3,6,1,4,1,97,9))
_Els10_27hw_ObjectIdentity=ObjectIdentity
els10_27hw=_Els10_27hw_ObjectIdentity((1,3,6,1,4,1,97,9,1))
_Els10_27hwDiagCode_Type=OctetString
_Els10_27hwDiagCode_Object=MibScalar
els10_27hwDiagCode=_Els10_27hwDiagCode_Object((1,3,6,1,4,1,97,9,1,1),_Els10_27hwDiagCode_Type())
els10_27hwDiagCode.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27hwDiagCode.setStatus(_A)
_Els10_27hwManufData_Type=OctetString
_Els10_27hwManufData_Object=MibScalar
els10_27hwManufData=_Els10_27hwManufData_Object((1,3,6,1,4,1,97,9,1,2),_Els10_27hwManufData_Type())
els10_27hwManufData.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27hwManufData.setStatus(_A)
_Els10_27hwPortCount_Type=Integer32
_Els10_27hwPortCount_Object=MibScalar
els10_27hwPortCount=_Els10_27hwPortCount_Object((1,3,6,1,4,1,97,9,1,3),_Els10_27hwPortCount_Type())
els10_27hwPortCount.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27hwPortCount.setStatus(_A)
_Els10_27hwPortTable_Object=MibTable
els10_27hwPortTable=_Els10_27hwPortTable_Object((1,3,6,1,4,1,97,9,1,4))
if mibBuilder.loadTexts:els10_27hwPortTable.setStatus(_A)
_Els10_27hwPortEntry_Object=MibTableRow
els10_27hwPortEntry=_Els10_27hwPortEntry_Object((1,3,6,1,4,1,97,9,1,4,1))
els10_27hwPortEntry.setIndexNames((0,_D,_l))
if mibBuilder.loadTexts:els10_27hwPortEntry.setStatus(_A)
_Els10_27hwPortIndex_Type=Integer32
_Els10_27hwPortIndex_Object=MibTableColumn
els10_27hwPortIndex=_Els10_27hwPortIndex_Object((1,3,6,1,4,1,97,9,1,4,1,1),_Els10_27hwPortIndex_Type())
els10_27hwPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27hwPortIndex.setStatus(_A)
class _Els10_27hwPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,6,255)));namedValues=NamedValues(*(('port-csma',1),('port-uart',6),('port-none',255)))
_Els10_27hwPortType_Type.__name__=_E
_Els10_27hwPortType_Object=MibTableColumn
els10_27hwPortType=_Els10_27hwPortType_Object((1,3,6,1,4,1,97,9,1,4,1,2),_Els10_27hwPortType_Type())
els10_27hwPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27hwPortType.setStatus(_A)
class _Els10_27hwPortSubType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(13,16,17,80,255)));namedValues=NamedValues(*(('csmacd-tpx',13),('csmacd-100-tpx',16),('csmacd-100-fx',17),('uart-female-9pin',80),('no-information',255)))
_Els10_27hwPortSubType_Type.__name__=_E
_Els10_27hwPortSubType_Object=MibTableColumn
els10_27hwPortSubType=_Els10_27hwPortSubType_Object((1,3,6,1,4,1,97,9,1,4,1,3),_Els10_27hwPortSubType_Type())
els10_27hwPortSubType.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27hwPortSubType.setStatus(_A)
class _Els10_27hwPortDiagPassed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('diag-passed',1),('diag-failed',2)))
_Els10_27hwPortDiagPassed_Type.__name__=_E
_Els10_27hwPortDiagPassed_Object=MibTableColumn
els10_27hwPortDiagPassed=_Els10_27hwPortDiagPassed_Object((1,3,6,1,4,1,97,9,1,4,1,4),_Els10_27hwPortDiagPassed_Type())
els10_27hwPortDiagPassed.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27hwPortDiagPassed.setStatus(_A)
_Els10_27hwAddr_Type=OctetString
_Els10_27hwAddr_Object=MibTableColumn
els10_27hwAddr=_Els10_27hwAddr_Object((1,3,6,1,4,1,97,9,1,4,1,5),_Els10_27hwAddr_Type())
els10_27hwAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27hwAddr.setStatus(_A)
class _Els10_27hwUpLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_Els10_27hwUpLink_Type.__name__=_E
_Els10_27hwUpLink_Object=MibScalar
els10_27hwUpLink=_Els10_27hwUpLink_Object((1,3,6,1,4,1,97,9,1,5),_Els10_27hwUpLink_Type())
els10_27hwUpLink.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27hwUpLink.setStatus(_A)
_Els10_27hwUpLinkManufData_Type=OctetString
_Els10_27hwUpLinkManufData_Object=MibScalar
els10_27hwUpLinkManufData=_Els10_27hwUpLinkManufData_Object((1,3,6,1,4,1,97,9,1,6),_Els10_27hwUpLinkManufData_Type())
els10_27hwUpLinkManufData.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27hwUpLinkManufData.setStatus(_A)
_Els10_27sw_ObjectIdentity=ObjectIdentity
els10_27sw=_Els10_27sw_ObjectIdentity((1,3,6,1,4,1,97,9,2))
_Els10_27swNumber_Type=Integer32
_Els10_27swNumber_Object=MibScalar
els10_27swNumber=_Els10_27swNumber_Object((1,3,6,1,4,1,97,9,2,1),_Els10_27swNumber_Type())
els10_27swNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27swNumber.setStatus(_A)
_Els10_27swFilesetTable_Object=MibTable
els10_27swFilesetTable=_Els10_27swFilesetTable_Object((1,3,6,1,4,1,97,9,2,2))
if mibBuilder.loadTexts:els10_27swFilesetTable.setStatus(_A)
_Els10_27swFilesetEntry_Object=MibTableRow
els10_27swFilesetEntry=_Els10_27swFilesetEntry_Object((1,3,6,1,4,1,97,9,2,2,1))
els10_27swFilesetEntry.setIndexNames((0,_D,_m))
if mibBuilder.loadTexts:els10_27swFilesetEntry.setStatus(_A)
class _Els10_27swIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('currently-executing',1),('next-boot',2)))
_Els10_27swIndex_Type.__name__=_E
_Els10_27swIndex_Object=MibTableColumn
els10_27swIndex=_Els10_27swIndex_Object((1,3,6,1,4,1,97,9,2,2,1,1),_Els10_27swIndex_Type())
els10_27swIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27swIndex.setStatus(_A)
_Els10_27swDesc_Type=DisplayString
_Els10_27swDesc_Object=MibTableColumn
els10_27swDesc=_Els10_27swDesc_Object((1,3,6,1,4,1,97,9,2,2,1,2),_Els10_27swDesc_Type())
els10_27swDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27swDesc.setStatus(_A)
_Els10_27swCount_Type=Integer32
_Els10_27swCount_Object=MibTableColumn
els10_27swCount=_Els10_27swCount_Object((1,3,6,1,4,1,97,9,2,2,1,3),_Els10_27swCount_Type())
els10_27swCount.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27swCount.setStatus(_A)
_Els10_27swType_Type=OctetString
_Els10_27swType_Object=MibTableColumn
els10_27swType=_Els10_27swType_Object((1,3,6,1,4,1,97,9,2,2,1,4),_Els10_27swType_Type())
els10_27swType.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27swType.setStatus(_A)
_Els10_27swSizes_Type=OctetString
_Els10_27swSizes_Object=MibTableColumn
els10_27swSizes=_Els10_27swSizes_Object((1,3,6,1,4,1,97,9,2,2,1,5),_Els10_27swSizes_Type())
els10_27swSizes.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27swSizes.setStatus(_A)
_Els10_27swStarts_Type=OctetString
_Els10_27swStarts_Object=MibTableColumn
els10_27swStarts=_Els10_27swStarts_Object((1,3,6,1,4,1,97,9,2,2,1,6),_Els10_27swStarts_Type())
els10_27swStarts.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27swStarts.setStatus(_A)
_Els10_27swBases_Type=OctetString
_Els10_27swBases_Object=MibTableColumn
els10_27swBases=_Els10_27swBases_Object((1,3,6,1,4,1,97,9,2,2,1,7),_Els10_27swBases_Type())
els10_27swBases.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27swBases.setStatus(_A)
class _Els10_27swFlashBank_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('first-bank',1),('second-bank',2)))
_Els10_27swFlashBank_Type.__name__=_E
_Els10_27swFlashBank_Object=MibTableColumn
els10_27swFlashBank=_Els10_27swFlashBank_Object((1,3,6,1,4,1,97,9,2,2,1,8),_Els10_27swFlashBank_Type())
els10_27swFlashBank.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27swFlashBank.setStatus(_A)
_Els10_27admin_ObjectIdentity=ObjectIdentity
els10_27admin=_Els10_27admin_ObjectIdentity((1,3,6,1,4,1,97,9,3))
_Els10_27adminFatalErr_Type=OctetString
_Els10_27adminFatalErr_Object=MibScalar
els10_27adminFatalErr=_Els10_27adminFatalErr_Object((1,3,6,1,4,1,97,9,3,1),_Els10_27adminFatalErr_Type())
els10_27adminFatalErr.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27adminFatalErr.setStatus(_A)
_Els10_27adminAnyPass_Type=OctetString
_Els10_27adminAnyPass_Object=MibScalar
els10_27adminAnyPass=_Els10_27adminAnyPass_Object((1,3,6,1,4,1,97,9,3,2),_Els10_27adminAnyPass_Type())
els10_27adminAnyPass.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27adminAnyPass.setStatus(_A)
_Els10_27adminGetPass_Type=OctetString
_Els10_27adminGetPass_Object=MibScalar
els10_27adminGetPass=_Els10_27adminGetPass_Object((1,3,6,1,4,1,97,9,3,3),_Els10_27adminGetPass_Type())
els10_27adminGetPass.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27adminGetPass.setStatus(_A)
_Els10_27adminNMSIPAddr_Type=IpAddress
_Els10_27adminNMSIPAddr_Object=MibScalar
els10_27adminNMSIPAddr=_Els10_27adminNMSIPAddr_Object((1,3,6,1,4,1,97,9,3,4),_Els10_27adminNMSIPAddr_Type())
els10_27adminNMSIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27adminNMSIPAddr.setStatus(_A)
class _Els10_27adminStorageFailure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_Els10_27adminStorageFailure_Type.__name__=_E
_Els10_27adminStorageFailure_Object=MibScalar
els10_27adminStorageFailure=_Els10_27adminStorageFailure_Object((1,3,6,1,4,1,97,9,3,7),_Els10_27adminStorageFailure_Type())
els10_27adminStorageFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27adminStorageFailure.setStatus(_A)
_Els10_27adminAuthenticationFailure_Type=IpAddress
_Els10_27adminAuthenticationFailure_Object=MibScalar
els10_27adminAuthenticationFailure=_Els10_27adminAuthenticationFailure_Object((1,3,6,1,4,1,97,9,3,8),_Els10_27adminAuthenticationFailure_Type())
els10_27adminAuthenticationFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27adminAuthenticationFailure.setStatus(_A)
_Els10_27adminNAMReceiveCongests_Type=Counter32
_Els10_27adminNAMReceiveCongests_Object=MibScalar
els10_27adminNAMReceiveCongests=_Els10_27adminNAMReceiveCongests_Object((1,3,6,1,4,1,97,9,3,10),_Els10_27adminNAMReceiveCongests_Type())
els10_27adminNAMReceiveCongests.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27adminNAMReceiveCongests.setStatus(_A)
_Els10_27adminArpEntries_Type=Counter32
_Els10_27adminArpEntries_Object=MibScalar
els10_27adminArpEntries=_Els10_27adminArpEntries_Object((1,3,6,1,4,1,97,9,3,11),_Els10_27adminArpEntries_Type())
els10_27adminArpEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27adminArpEntries.setStatus(_A)
_Els10_27adminArpStatics_Type=Counter32
_Els10_27adminArpStatics_Object=MibScalar
els10_27adminArpStatics=_Els10_27adminArpStatics_Object((1,3,6,1,4,1,97,9,3,12),_Els10_27adminArpStatics_Type())
els10_27adminArpStatics.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27adminArpStatics.setStatus(_A)
_Els10_27adminArpOverflows_Type=Counter32
_Els10_27adminArpOverflows_Object=MibScalar
els10_27adminArpOverflows=_Els10_27adminArpOverflows_Object((1,3,6,1,4,1,97,9,3,13),_Els10_27adminArpOverflows_Type())
els10_27adminArpOverflows.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27adminArpOverflows.setStatus(_A)
_Els10_27adminIpEntries_Type=Counter32
_Els10_27adminIpEntries_Object=MibScalar
els10_27adminIpEntries=_Els10_27adminIpEntries_Object((1,3,6,1,4,1,97,9,3,14),_Els10_27adminIpEntries_Type())
els10_27adminIpEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27adminIpEntries.setStatus(_A)
_Els10_27adminIpStatics_Type=Counter32
_Els10_27adminIpStatics_Object=MibScalar
els10_27adminIpStatics=_Els10_27adminIpStatics_Object((1,3,6,1,4,1,97,9,3,15),_Els10_27adminIpStatics_Type())
els10_27adminIpStatics.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27adminIpStatics.setStatus(_A)
_Els10_27adminStaticPreference_Type=Integer32
_Els10_27adminStaticPreference_Object=MibScalar
els10_27adminStaticPreference=_Els10_27adminStaticPreference_Object((1,3,6,1,4,1,97,9,3,16),_Els10_27adminStaticPreference_Type())
els10_27adminStaticPreference.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27adminStaticPreference.setStatus(_A)
_Els10_27adminRipPreference_Type=Integer32
_Els10_27adminRipPreference_Object=MibScalar
els10_27adminRipPreference=_Els10_27adminRipPreference_Object((1,3,6,1,4,1,97,9,3,17),_Els10_27adminRipPreference_Type())
els10_27adminRipPreference.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27adminRipPreference.setStatus(_A)
_Els10_27adminRipRouteDiscards_Type=Counter32
_Els10_27adminRipRouteDiscards_Object=MibScalar
els10_27adminRipRouteDiscards=_Els10_27adminRipRouteDiscards_Object((1,3,6,1,4,1,97,9,3,18),_Els10_27adminRipRouteDiscards_Type())
els10_27adminRipRouteDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27adminRipRouteDiscards.setStatus(_A)
class _Els10_27adminRebootConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('no-change',1),('tftp-config',2),('revert-to-defaults',3)))
_Els10_27adminRebootConfig_Type.__name__=_E
_Els10_27adminRebootConfig_Object=MibScalar
els10_27adminRebootConfig=_Els10_27adminRebootConfig_Object((1,3,6,1,4,1,97,9,3,19),_Els10_27adminRebootConfig_Type())
els10_27adminRebootConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27adminRebootConfig.setStatus(_A)
class _Els10_27adminDisableButton_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_Els10_27adminDisableButton_Type.__name__=_E
_Els10_27adminDisableButton_Object=MibScalar
els10_27adminDisableButton=_Els10_27adminDisableButton_Object((1,3,6,1,4,1,97,9,3,21),_Els10_27adminDisableButton_Type())
els10_27adminDisableButton.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27adminDisableButton.setStatus(_A)
class _Els10_27adminButtonSelection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('led-any-activity',1),('led-rx-activity',2),('led-tx-activity',3),('led-any-collision',4),('led-programmed',5),('led-duplex',6),('led-speed',7),('led-mirror',8)))
_Els10_27adminButtonSelection_Type.__name__=_E
_Els10_27adminButtonSelection_Object=MibScalar
els10_27adminButtonSelection=_Els10_27adminButtonSelection_Object((1,3,6,1,4,1,97,9,3,22),_Els10_27adminButtonSelection_Type())
els10_27adminButtonSelection.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27adminButtonSelection.setStatus(_A)
class _Els10_27adminLEDProgramOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('program-led-any-error',1))
_Els10_27adminLEDProgramOption_Type.__name__=_E
_Els10_27adminLEDProgramOption_Object=MibScalar
els10_27adminLEDProgramOption=_Els10_27adminLEDProgramOption_Object((1,3,6,1,4,1,97,9,3,23),_Els10_27adminLEDProgramOption_Type())
els10_27adminLEDProgramOption.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27adminLEDProgramOption.setStatus(_A)
_Els10_27swdis_ObjectIdentity=ObjectIdentity
els10_27swdis=_Els10_27swdis_ObjectIdentity((1,3,6,1,4,1,97,9,4))
_Els10_27swdisDesc_Type=OctetString
_Els10_27swdisDesc_Object=MibScalar
els10_27swdisDesc=_Els10_27swdisDesc_Object((1,3,6,1,4,1,97,9,4,1),_Els10_27swdisDesc_Type())
els10_27swdisDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27swdisDesc.setStatus(_A)
class _Els10_27swdisAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('protected',1),('any-software',2)))
_Els10_27swdisAccess_Type.__name__=_E
_Els10_27swdisAccess_Object=MibScalar
els10_27swdisAccess=_Els10_27swdisAccess_Object((1,3,6,1,4,1,97,9,4,2),_Els10_27swdisAccess_Type())
els10_27swdisAccess.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27swdisAccess.setStatus(_A)
class _Els10_27swdisWriteStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('in-progress',1),('success',2),('config-error',3),('flash-error',4),('config-and-flash-errors',5)))
_Els10_27swdisWriteStatus_Type.__name__=_E
_Els10_27swdisWriteStatus_Object=MibScalar
els10_27swdisWriteStatus=_Els10_27swdisWriteStatus_Object((1,3,6,1,4,1,97,9,4,3),_Els10_27swdisWriteStatus_Type())
els10_27swdisWriteStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27swdisWriteStatus.setStatus(_A)
_Els10_27swdisConfigIp_Type=IpAddress
_Els10_27swdisConfigIp_Object=MibScalar
els10_27swdisConfigIp=_Els10_27swdisConfigIp_Object((1,3,6,1,4,1,97,9,4,4),_Els10_27swdisConfigIp_Type())
els10_27swdisConfigIp.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27swdisConfigIp.setStatus(_A)
_Els10_27swdisConfigRetryTime_Type=Integer32
_Els10_27swdisConfigRetryTime_Object=MibScalar
els10_27swdisConfigRetryTime=_Els10_27swdisConfigRetryTime_Object((1,3,6,1,4,1,97,9,4,5),_Els10_27swdisConfigRetryTime_Type())
els10_27swdisConfigRetryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27swdisConfigRetryTime.setStatus(_A)
_Els10_27swdisConfigTotalTimeout_Type=Integer32
_Els10_27swdisConfigTotalTimeout_Object=MibScalar
els10_27swdisConfigTotalTimeout=_Els10_27swdisConfigTotalTimeout_Object((1,3,6,1,4,1,97,9,4,6),_Els10_27swdisConfigTotalTimeout_Type())
els10_27swdisConfigTotalTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27swdisConfigTotalTimeout.setStatus(_A)
_Els10_27addr_ObjectIdentity=ObjectIdentity
els10_27addr=_Els10_27addr_ObjectIdentity((1,3,6,1,4,1,97,9,5))
_Els10_27addrStatics_Type=Counter32
_Els10_27addrStatics_Object=MibScalar
els10_27addrStatics=_Els10_27addrStatics_Object((1,3,6,1,4,1,97,9,5,1),_Els10_27addrStatics_Type())
els10_27addrStatics.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27addrStatics.setStatus(_A)
_Els10_27addrDynamics_Type=Counter32
_Els10_27addrDynamics_Object=MibScalar
els10_27addrDynamics=_Els10_27addrDynamics_Object((1,3,6,1,4,1,97,9,5,2),_Els10_27addrDynamics_Type())
els10_27addrDynamics.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27addrDynamics.setStatus(_A)
_Els10_27addrDynamicMax_Type=Gauge32
_Els10_27addrDynamicMax_Object=MibScalar
els10_27addrDynamicMax=_Els10_27addrDynamicMax_Object((1,3,6,1,4,1,97,9,5,3),_Els10_27addrDynamicMax_Type())
els10_27addrDynamicMax.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27addrDynamicMax.setStatus(_A)
_Els10_27addrDynamicOverflows_Type=Counter32
_Els10_27addrDynamicOverflows_Object=MibScalar
els10_27addrDynamicOverflows=_Els10_27addrDynamicOverflows_Object((1,3,6,1,4,1,97,9,5,4),_Els10_27addrDynamicOverflows_Type())
els10_27addrDynamicOverflows.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27addrDynamicOverflows.setStatus(_A)
_Els10_27addrFlags_Type=Integer32
_Els10_27addrFlags_Object=MibScalar
els10_27addrFlags=_Els10_27addrFlags_Object((1,3,6,1,4,1,97,9,5,5),_Els10_27addrFlags_Type())
els10_27addrFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27addrFlags.setStatus(_A)
_Els10_27addrMAC_Type=OctetString
_Els10_27addrMAC_Object=MibScalar
els10_27addrMAC=_Els10_27addrMAC_Object((1,3,6,1,4,1,97,9,5,6),_Els10_27addrMAC_Type())
els10_27addrMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27addrMAC.setStatus(_A)
_Els10_27addrPort_Type=Integer32
_Els10_27addrPort_Object=MibScalar
els10_27addrPort=_Els10_27addrPort_Object((1,3,6,1,4,1,97,9,5,7),_Els10_27addrPort_Type())
els10_27addrPort.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27addrPort.setStatus(_A)
class _Els10_27addrOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5,6)));namedValues=NamedValues(*(('read-random',1),('read-next',2),('update',4),(_N,5),('read-block',6)))
_Els10_27addrOperation_Type.__name__=_E
_Els10_27addrOperation_Object=MibScalar
els10_27addrOperation=_Els10_27addrOperation_Object((1,3,6,1,4,1,97,9,5,8),_Els10_27addrOperation_Type())
els10_27addrOperation.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27addrOperation.setStatus(_A)
_Els10_27addrIndex_Type=Integer32
_Els10_27addrIndex_Object=MibScalar
els10_27addrIndex=_Els10_27addrIndex_Object((1,3,6,1,4,1,97,9,5,9),_Els10_27addrIndex_Type())
els10_27addrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27addrIndex.setStatus(_A)
_Els10_27addrNext_Type=Integer32
_Els10_27addrNext_Object=MibScalar
els10_27addrNext=_Els10_27addrNext_Object((1,3,6,1,4,1,97,9,5,10),_Els10_27addrNext_Type())
els10_27addrNext.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27addrNext.setStatus(_A)
_Els10_27addrBlockSize_Type=Integer32
_Els10_27addrBlockSize_Object=MibScalar
els10_27addrBlockSize=_Els10_27addrBlockSize_Object((1,3,6,1,4,1,97,9,5,19),_Els10_27addrBlockSize_Type())
els10_27addrBlockSize.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27addrBlockSize.setStatus(_A)
_Els10_27addrBlock_Type=OctetString
_Els10_27addrBlock_Object=MibScalar
els10_27addrBlock=_Els10_27addrBlock_Object((1,3,6,1,4,1,97,9,5,20),_Els10_27addrBlock_Type())
els10_27addrBlock.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27addrBlock.setStatus(_A)
_Els10_27if_ObjectIdentity=ObjectIdentity
els10_27if=_Els10_27if_ObjectIdentity((1,3,6,1,4,1,97,9,6))
_Els10_27ifTable_Object=MibTable
els10_27ifTable=_Els10_27ifTable_Object((1,3,6,1,4,1,97,9,6,1))
if mibBuilder.loadTexts:els10_27ifTable.setStatus(_A)
_Els10_27ifEntry_Object=MibTableRow
els10_27ifEntry=_Els10_27ifEntry_Object((1,3,6,1,4,1,97,9,6,1,1))
els10_27ifEntry.setIndexNames((0,_D,_n))
if mibBuilder.loadTexts:els10_27ifEntry.setStatus(_A)
_Els10_27ifIndex_Type=Integer32
_Els10_27ifIndex_Object=MibTableColumn
els10_27ifIndex=_Els10_27ifIndex_Object((1,3,6,1,4,1,97,9,6,1,1,1),_Els10_27ifIndex_Type())
els10_27ifIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27ifIndex.setStatus(_A)
_Els10_27ifThreshold_Type=Integer32
_Els10_27ifThreshold_Object=MibTableColumn
els10_27ifThreshold=_Els10_27ifThreshold_Object((1,3,6,1,4,1,97,9,6,1,1,4),_Els10_27ifThreshold_Type())
els10_27ifThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27ifThreshold.setStatus(_A)
_Els10_27ifThresholdTime_Type=Integer32
_Els10_27ifThresholdTime_Object=MibTableColumn
els10_27ifThresholdTime=_Els10_27ifThresholdTime_Object((1,3,6,1,4,1,97,9,6,1,1,5),_Els10_27ifThresholdTime_Type())
els10_27ifThresholdTime.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27ifThresholdTime.setStatus(_A)
_Els10_27ifRxQueueThresh_Type=Integer32
_Els10_27ifRxQueueThresh_Object=MibTableColumn
els10_27ifRxQueueThresh=_Els10_27ifRxQueueThresh_Object((1,3,6,1,4,1,97,9,6,1,1,6),_Els10_27ifRxQueueThresh_Type())
els10_27ifRxQueueThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27ifRxQueueThresh.setStatus(_A)
_Els10_27ifRxQueueThreshTime_Type=Integer32
_Els10_27ifRxQueueThreshTime_Object=MibTableColumn
els10_27ifRxQueueThreshTime=_Els10_27ifRxQueueThreshTime_Object((1,3,6,1,4,1,97,9,6,1,1,7),_Els10_27ifRxQueueThreshTime_Type())
els10_27ifRxQueueThreshTime.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27ifRxQueueThreshTime.setStatus(_A)
_Els10_27ifTxStormCnt_Type=Integer32
_Els10_27ifTxStormCnt_Object=MibTableColumn
els10_27ifTxStormCnt=_Els10_27ifTxStormCnt_Object((1,3,6,1,4,1,97,9,6,1,1,8),_Els10_27ifTxStormCnt_Type())
els10_27ifTxStormCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27ifTxStormCnt.setStatus(_A)
_Els10_27ifTxStormTime_Type=TimeTicks
_Els10_27ifTxStormTime_Object=MibTableColumn
els10_27ifTxStormTime=_Els10_27ifTxStormTime_Object((1,3,6,1,4,1,97,9,6,1,1,9),_Els10_27ifTxStormTime_Type())
els10_27ifTxStormTime.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27ifTxStormTime.setStatus(_A)
_Els10_27ifFunction_Type=Integer32
_Els10_27ifFunction_Object=MibTableColumn
els10_27ifFunction=_Els10_27ifFunction_Object((1,3,6,1,4,1,97,9,6,1,1,16),_Els10_27ifFunction_Type())
els10_27ifFunction.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27ifFunction.setStatus(_A)
_Els10_27ifRxHwFCSs_Type=Counter32
_Els10_27ifRxHwFCSs_Object=MibTableColumn
els10_27ifRxHwFCSs=_Els10_27ifRxHwFCSs_Object((1,3,6,1,4,1,97,9,6,1,1,18),_Els10_27ifRxHwFCSs_Type())
els10_27ifRxHwFCSs.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27ifRxHwFCSs.setStatus(_A)
_Els10_27ifRxQueues_Type=Counter32
_Els10_27ifRxQueues_Object=MibTableColumn
els10_27ifRxQueues=_Els10_27ifRxQueues_Object((1,3,6,1,4,1,97,9,6,1,1,19),_Els10_27ifRxQueues_Type())
els10_27ifRxQueues.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27ifRxQueues.setStatus(_A)
_Els10_27ifStatisticsTime_Type=TimeTicks
_Els10_27ifStatisticsTime_Object=MibTableColumn
els10_27ifStatisticsTime=_Els10_27ifStatisticsTime_Object((1,3,6,1,4,1,97,9,6,1,1,27),_Els10_27ifStatisticsTime_Type())
els10_27ifStatisticsTime.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27ifStatisticsTime.setStatus(_A)
_Els10_27ifForwardedChars_Type=Counter32
_Els10_27ifForwardedChars_Object=MibTableColumn
els10_27ifForwardedChars=_Els10_27ifForwardedChars_Object((1,3,6,1,4,1,97,9,6,1,1,28),_Els10_27ifForwardedChars_Type())
els10_27ifForwardedChars.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27ifForwardedChars.setStatus(_A)
_Els10_27ifDescr_Type=DisplayString
_Els10_27ifDescr_Object=MibTableColumn
els10_27ifDescr=_Els10_27ifDescr_Object((1,3,6,1,4,1,97,9,6,1,1,29),_Els10_27ifDescr_Type())
els10_27ifDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27ifDescr.setStatus(_A)
_Els10_27ifGoodRxFrames_Type=Counter32
_Els10_27ifGoodRxFrames_Object=MibTableColumn
els10_27ifGoodRxFrames=_Els10_27ifGoodRxFrames_Object((1,3,6,1,4,1,97,9,6,1,1,30),_Els10_27ifGoodRxFrames_Type())
els10_27ifGoodRxFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27ifGoodRxFrames.setStatus(_A)
_Els10_27ifGoodTxFrames_Type=Counter32
_Els10_27ifGoodTxFrames_Object=MibTableColumn
els10_27ifGoodTxFrames=_Els10_27ifGoodTxFrames_Object((1,3,6,1,4,1,97,9,6,1,1,31),_Els10_27ifGoodTxFrames_Type())
els10_27ifGoodTxFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27ifGoodTxFrames.setStatus(_A)
_Els10_27dot3_ObjectIdentity=ObjectIdentity
els10_27dot3=_Els10_27dot3_ObjectIdentity((1,3,6,1,4,1,97,9,7))
_Els10_27dot3Table_Object=MibTable
els10_27dot3Table=_Els10_27dot3Table_Object((1,3,6,1,4,1,97,9,7,1))
if mibBuilder.loadTexts:els10_27dot3Table.setStatus(_A)
_Els10_27dot3Entry_Object=MibTableRow
els10_27dot3Entry=_Els10_27dot3Entry_Object((1,3,6,1,4,1,97,9,7,1,1))
els10_27dot3Entry.setIndexNames((0,_D,_o))
if mibBuilder.loadTexts:els10_27dot3Entry.setStatus(_A)
_Els10_27dot3Index_Type=Integer32
_Els10_27dot3Index_Object=MibTableColumn
els10_27dot3Index=_Els10_27dot3Index_Object((1,3,6,1,4,1,97,9,7,1,1,1),_Els10_27dot3Index_Type())
els10_27dot3Index.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27dot3Index.setStatus(_A)
class _Els10_27dot3TPLinkOK_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_Els10_27dot3TPLinkOK_Type.__name__=_E
_Els10_27dot3TPLinkOK_Object=MibTableColumn
els10_27dot3TPLinkOK=_Els10_27dot3TPLinkOK_Object((1,3,6,1,4,1,97,9,7,1,1,2),_Els10_27dot3TPLinkOK_Type())
els10_27dot3TPLinkOK.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27dot3TPLinkOK.setStatus(_A)
class _Els10_27dot3LedOn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('led-on',1),('led-off',2)))
_Els10_27dot3LedOn_Type.__name__=_E
_Els10_27dot3LedOn_Object=MibTableColumn
els10_27dot3LedOn=_Els10_27dot3LedOn_Object((1,3,6,1,4,1,97,9,7,1,1,3),_Els10_27dot3LedOn_Type())
els10_27dot3LedOn.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27dot3LedOn.setStatus(_A)
_Els10_27dot3RxCollisions_Type=Counter32
_Els10_27dot3RxCollisions_Object=MibTableColumn
els10_27dot3RxCollisions=_Els10_27dot3RxCollisions_Object((1,3,6,1,4,1,97,9,7,1,1,4),_Els10_27dot3RxCollisions_Type())
els10_27dot3RxCollisions.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27dot3RxCollisions.setStatus(_A)
_Els10_27dot3RxRunts_Type=Counter32
_Els10_27dot3RxRunts_Object=MibTableColumn
els10_27dot3RxRunts=_Els10_27dot3RxRunts_Object((1,3,6,1,4,1,97,9,7,1,1,5),_Els10_27dot3RxRunts_Type())
els10_27dot3RxRunts.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27dot3RxRunts.setStatus(_A)
_Els10_27dot3RxLateColls_Type=Counter32
_Els10_27dot3RxLateColls_Object=MibTableColumn
els10_27dot3RxLateColls=_Els10_27dot3RxLateColls_Object((1,3,6,1,4,1,97,9,7,1,1,6),_Els10_27dot3RxLateColls_Type())
els10_27dot3RxLateColls.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27dot3RxLateColls.setStatus(_A)
_Els10_27dot3TxJabbers_Type=Counter32
_Els10_27dot3TxJabbers_Object=MibTableColumn
els10_27dot3TxJabbers=_Els10_27dot3TxJabbers_Object((1,3,6,1,4,1,97,9,7,1,1,7),_Els10_27dot3TxJabbers_Type())
els10_27dot3TxJabbers.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27dot3TxJabbers.setStatus(_A)
_Els10_27dot3TxBabbles_Type=Counter32
_Els10_27dot3TxBabbles_Object=MibTableColumn
els10_27dot3TxBabbles=_Els10_27dot3TxBabbles_Object((1,3,6,1,4,1,97,9,7,1,1,8),_Els10_27dot3TxBabbles_Type())
els10_27dot3TxBabbles.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27dot3TxBabbles.setStatus(_A)
_Els10_27dot3TxCollisions_Type=Counter32
_Els10_27dot3TxCollisions_Object=MibTableColumn
els10_27dot3TxCollisions=_Els10_27dot3TxCollisions_Object((1,3,6,1,4,1,97,9,7,1,1,9),_Els10_27dot3TxCollisions_Type())
els10_27dot3TxCollisions.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27dot3TxCollisions.setStatus(_A)
class _Els10_27dot3SpeedSelection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('speed-10mbit',1),('speed-100mbit',2),('speed-auto',3)))
_Els10_27dot3SpeedSelection_Type.__name__=_E
_Els10_27dot3SpeedSelection_Object=MibTableColumn
els10_27dot3SpeedSelection=_Els10_27dot3SpeedSelection_Object((1,3,6,1,4,1,97,9,7,1,1,13),_Els10_27dot3SpeedSelection_Type())
els10_27dot3SpeedSelection.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27dot3SpeedSelection.setStatus(_A)
class _Els10_27dot3DuplexSelection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('duplex-auto',1),('duplex-half',2),('duplex-full',3)))
_Els10_27dot3DuplexSelection_Type.__name__=_E
_Els10_27dot3DuplexSelection_Object=MibTableColumn
els10_27dot3DuplexSelection=_Els10_27dot3DuplexSelection_Object((1,3,6,1,4,1,97,9,7,1,1,14),_Els10_27dot3DuplexSelection_Type())
els10_27dot3DuplexSelection.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27dot3DuplexSelection.setStatus(_A)
_Els10_27uart_ObjectIdentity=ObjectIdentity
els10_27uart=_Els10_27uart_ObjectIdentity((1,3,6,1,4,1,97,9,8))
_Els10_27uartTable_Object=MibTable
els10_27uartTable=_Els10_27uartTable_Object((1,3,6,1,4,1,97,9,8,1))
if mibBuilder.loadTexts:els10_27uartTable.setStatus(_A)
_Els10_27uartEntry_Object=MibTableRow
els10_27uartEntry=_Els10_27uartEntry_Object((1,3,6,1,4,1,97,9,8,1,1))
els10_27uartEntry.setIndexNames((0,_D,_p))
if mibBuilder.loadTexts:els10_27uartEntry.setStatus(_A)
_Els10_27uartIndex_Type=Integer32
_Els10_27uartIndex_Object=MibTableColumn
els10_27uartIndex=_Els10_27uartIndex_Object((1,3,6,1,4,1,97,9,8,1,1,1),_Els10_27uartIndex_Type())
els10_27uartIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27uartIndex.setStatus(_A)
class _Els10_27uartBaud_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,5,6)));namedValues=NamedValues(*(('b2400-baud',3),('b4800-baud',4),('b9600-baud',5),('b19200-baud',6)))
_Els10_27uartBaud_Type.__name__=_E
_Els10_27uartBaud_Object=MibTableColumn
els10_27uartBaud=_Els10_27uartBaud_Object((1,3,6,1,4,1,97,9,8,1,1,2),_Els10_27uartBaud_Type())
els10_27uartBaud.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27uartBaud.setStatus(_A)
_Els10_27uartAlignmentErrors_Type=Counter32
_Els10_27uartAlignmentErrors_Object=MibTableColumn
els10_27uartAlignmentErrors=_Els10_27uartAlignmentErrors_Object((1,3,6,1,4,1,97,9,8,1,1,3),_Els10_27uartAlignmentErrors_Type())
els10_27uartAlignmentErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27uartAlignmentErrors.setStatus(_A)
_Els10_27uartOverrunErrors_Type=Counter32
_Els10_27uartOverrunErrors_Object=MibTableColumn
els10_27uartOverrunErrors=_Els10_27uartOverrunErrors_Object((1,3,6,1,4,1,97,9,8,1,1,4),_Els10_27uartOverrunErrors_Type())
els10_27uartOverrunErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27uartOverrunErrors.setStatus(_A)
_Els10_27debug_ObjectIdentity=ObjectIdentity
els10_27debug=_Els10_27debug_ObjectIdentity((1,3,6,1,4,1,97,9,10))
_Els10_27debugStringID_Type=Integer32
_Els10_27debugStringID_Object=MibScalar
els10_27debugStringID=_Els10_27debugStringID_Object((1,3,6,1,4,1,97,9,10,1),_Els10_27debugStringID_Type())
els10_27debugStringID.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27debugStringID.setStatus(_A)
_Els10_27debugString_Type=OctetString
_Els10_27debugString_Object=MibScalar
els10_27debugString=_Els10_27debugString_Object((1,3,6,1,4,1,97,9,10,2),_Els10_27debugString_Type())
els10_27debugString.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27debugString.setStatus(_A)
_Els10_27debugTable_Object=MibTable
els10_27debugTable=_Els10_27debugTable_Object((1,3,6,1,4,1,97,9,10,3))
if mibBuilder.loadTexts:els10_27debugTable.setStatus(_A)
_Els10_27debugEntry_Object=MibTableRow
els10_27debugEntry=_Els10_27debugEntry_Object((1,3,6,1,4,1,97,9,10,3,1))
els10_27debugEntry.setIndexNames((0,_D,_q))
if mibBuilder.loadTexts:els10_27debugEntry.setStatus(_A)
class _Els10_27debugIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('debug-nam',1))
_Els10_27debugIndex_Type.__name__=_E
_Els10_27debugIndex_Object=MibTableColumn
els10_27debugIndex=_Els10_27debugIndex_Object((1,3,6,1,4,1,97,9,10,3,1,1),_Els10_27debugIndex_Type())
els10_27debugIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27debugIndex.setStatus(_A)
class _Els10_27debugOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('examine',1),('modify',2)))
_Els10_27debugOperation_Type.__name__=_E
_Els10_27debugOperation_Object=MibTableColumn
els10_27debugOperation=_Els10_27debugOperation_Object((1,3,6,1,4,1,97,9,10,3,1,2),_Els10_27debugOperation_Type())
els10_27debugOperation.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27debugOperation.setStatus(_A)
_Els10_27debugBase_Type=Integer32
_Els10_27debugBase_Object=MibTableColumn
els10_27debugBase=_Els10_27debugBase_Object((1,3,6,1,4,1,97,9,10,3,1,3),_Els10_27debugBase_Type())
els10_27debugBase.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27debugBase.setStatus(_A)
_Els10_27debugLength_Type=Integer32
_Els10_27debugLength_Object=MibTableColumn
els10_27debugLength=_Els10_27debugLength_Object((1,3,6,1,4,1,97,9,10,3,1,4),_Els10_27debugLength_Type())
els10_27debugLength.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27debugLength.setStatus(_A)
_Els10_27debugData_Type=OctetString
_Els10_27debugData_Object=MibTableColumn
els10_27debugData=_Els10_27debugData_Object((1,3,6,1,4,1,97,9,10,3,1,5),_Els10_27debugData_Type())
els10_27debugData.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27debugData.setStatus(_A)
_Els10_27lpbk_ObjectIdentity=ObjectIdentity
els10_27lpbk=_Els10_27lpbk_ObjectIdentity((1,3,6,1,4,1,97,9,11))
_Els10_27lpbkTable_Object=MibTable
els10_27lpbkTable=_Els10_27lpbkTable_Object((1,3,6,1,4,1,97,9,11,1))
if mibBuilder.loadTexts:els10_27lpbkTable.setStatus(_A)
_Els10_27lpbkEntry_Object=MibTableRow
els10_27lpbkEntry=_Els10_27lpbkEntry_Object((1,3,6,1,4,1,97,9,11,1,1))
els10_27lpbkEntry.setIndexNames((0,_D,_r))
if mibBuilder.loadTexts:els10_27lpbkEntry.setStatus(_A)
_Els10_27lpbkIndex_Type=Integer32
_Els10_27lpbkIndex_Object=MibTableColumn
els10_27lpbkIndex=_Els10_27lpbkIndex_Object((1,3,6,1,4,1,97,9,11,1,1,1),_Els10_27lpbkIndex_Type())
els10_27lpbkIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27lpbkIndex.setStatus(_A)
class _Els10_27lpbkOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('loopback-off',1),('loopback-local',2),('loopback-remote',3)))
_Els10_27lpbkOperation_Type.__name__=_E
_Els10_27lpbkOperation_Object=MibTableColumn
els10_27lpbkOperation=_Els10_27lpbkOperation_Object((1,3,6,1,4,1,97,9,11,1,1,2),_Els10_27lpbkOperation_Type())
els10_27lpbkOperation.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27lpbkOperation.setStatus(_A)
_Els10_27lpbkDestAddr_Type=OctetString
_Els10_27lpbkDestAddr_Object=MibTableColumn
els10_27lpbkDestAddr=_Els10_27lpbkDestAddr_Object((1,3,6,1,4,1,97,9,11,1,1,3),_Els10_27lpbkDestAddr_Type())
els10_27lpbkDestAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27lpbkDestAddr.setStatus(_A)
_Els10_27lpbkPktNum_Type=Integer32
_Els10_27lpbkPktNum_Object=MibTableColumn
els10_27lpbkPktNum=_Els10_27lpbkPktNum_Object((1,3,6,1,4,1,97,9,11,1,1,4),_Els10_27lpbkPktNum_Type())
els10_27lpbkPktNum.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27lpbkPktNum.setStatus(_A)
_Els10_27lpbkInterval_Type=TimeTicks
_Els10_27lpbkInterval_Object=MibTableColumn
els10_27lpbkInterval=_Els10_27lpbkInterval_Object((1,3,6,1,4,1,97,9,11,1,1,5),_Els10_27lpbkInterval_Type())
els10_27lpbkInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27lpbkInterval.setStatus(_A)
_Els10_27lpbkPktLength_Type=Integer32
_Els10_27lpbkPktLength_Object=MibTableColumn
els10_27lpbkPktLength=_Els10_27lpbkPktLength_Object((1,3,6,1,4,1,97,9,11,1,1,6),_Els10_27lpbkPktLength_Type())
els10_27lpbkPktLength.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27lpbkPktLength.setStatus(_A)
_Els10_27lpbkIncrements_Type=Integer32
_Els10_27lpbkIncrements_Object=MibTableColumn
els10_27lpbkIncrements=_Els10_27lpbkIncrements_Object((1,3,6,1,4,1,97,9,11,1,1,7),_Els10_27lpbkIncrements_Type())
els10_27lpbkIncrements.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27lpbkIncrements.setStatus(_A)
_Els10_27lpbkGoods_Type=Counter32
_Els10_27lpbkGoods_Object=MibTableColumn
els10_27lpbkGoods=_Els10_27lpbkGoods_Object((1,3,6,1,4,1,97,9,11,1,1,8),_Els10_27lpbkGoods_Type())
els10_27lpbkGoods.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27lpbkGoods.setStatus(_A)
_Els10_27lpbkErrorNoReceives_Type=Counter32
_Els10_27lpbkErrorNoReceives_Object=MibTableColumn
els10_27lpbkErrorNoReceives=_Els10_27lpbkErrorNoReceives_Object((1,3,6,1,4,1,97,9,11,1,1,9),_Els10_27lpbkErrorNoReceives_Type())
els10_27lpbkErrorNoReceives.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27lpbkErrorNoReceives.setStatus(_A)
_Els10_27lpbkErrorBadReceives_Type=Counter32
_Els10_27lpbkErrorBadReceives_Object=MibTableColumn
els10_27lpbkErrorBadReceives=_Els10_27lpbkErrorBadReceives_Object((1,3,6,1,4,1,97,9,11,1,1,10),_Els10_27lpbkErrorBadReceives_Type())
els10_27lpbkErrorBadReceives.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27lpbkErrorBadReceives.setStatus(_A)
_Els10_27lpbkErrorSize_Type=Integer32
_Els10_27lpbkErrorSize_Object=MibTableColumn
els10_27lpbkErrorSize=_Els10_27lpbkErrorSize_Object((1,3,6,1,4,1,97,9,11,1,1,11),_Els10_27lpbkErrorSize_Type())
els10_27lpbkErrorSize.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27lpbkErrorSize.setStatus(_A)
_Els10_27lpbkErrorSent_Type=OctetString
_Els10_27lpbkErrorSent_Object=MibTableColumn
els10_27lpbkErrorSent=_Els10_27lpbkErrorSent_Object((1,3,6,1,4,1,97,9,11,1,1,12),_Els10_27lpbkErrorSent_Type())
els10_27lpbkErrorSent.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27lpbkErrorSent.setStatus(_A)
_Els10_27lpbkErrorReceived_Type=OctetString
_Els10_27lpbkErrorReceived_Object=MibTableColumn
els10_27lpbkErrorReceived=_Els10_27lpbkErrorReceived_Object((1,3,6,1,4,1,97,9,11,1,1,13),_Els10_27lpbkErrorReceived_Type())
els10_27lpbkErrorReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27lpbkErrorReceived.setStatus(_A)
_Els10_27lpbkErrorOffset_Type=Integer32
_Els10_27lpbkErrorOffset_Object=MibTableColumn
els10_27lpbkErrorOffset=_Els10_27lpbkErrorOffset_Object((1,3,6,1,4,1,97,9,11,1,1,14),_Els10_27lpbkErrorOffset_Type())
els10_27lpbkErrorOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27lpbkErrorOffset.setStatus(_A)
_Els10_27proto_ObjectIdentity=ObjectIdentity
els10_27proto=_Els10_27proto_ObjectIdentity((1,3,6,1,4,1,97,9,12))
_Els10_27protoTable_Object=MibTable
els10_27protoTable=_Els10_27protoTable_Object((1,3,6,1,4,1,97,9,12,1))
if mibBuilder.loadTexts:els10_27protoTable.setStatus(_A)
_Els10_27protoEntry_Object=MibTableRow
els10_27protoEntry=_Els10_27protoEntry_Object((1,3,6,1,4,1,97,9,12,1,1))
els10_27protoEntry.setIndexNames((0,_D,_s))
if mibBuilder.loadTexts:els10_27protoEntry.setStatus(_A)
_Els10_27protoIfIndex_Type=Integer32
_Els10_27protoIfIndex_Object=MibTableColumn
els10_27protoIfIndex=_Els10_27protoIfIndex_Object((1,3,6,1,4,1,97,9,12,1,1,1),_Els10_27protoIfIndex_Type())
els10_27protoIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27protoIfIndex.setStatus(_A)
class _Els10_27protoBridge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4)));namedValues=NamedValues(*(('transparent',1),('none',4)))
_Els10_27protoBridge_Type.__name__=_E
_Els10_27protoBridge_Object=MibTableColumn
els10_27protoBridge=_Els10_27protoBridge_Object((1,3,6,1,4,1,97,9,12,1,1,2),_Els10_27protoBridge_Type())
els10_27protoBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27protoBridge.setStatus(_A)
class _Els10_27protoSuppressBpdu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('suppressed',2)))
_Els10_27protoSuppressBpdu_Type.__name__=_E
_Els10_27protoSuppressBpdu_Object=MibTableColumn
els10_27protoSuppressBpdu=_Els10_27protoSuppressBpdu_Object((1,3,6,1,4,1,97,9,12,1,1,3),_Els10_27protoSuppressBpdu_Type())
els10_27protoSuppressBpdu.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27protoSuppressBpdu.setStatus(_A)
class _Els10_27protoRipListen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_Els10_27protoRipListen_Type.__name__=_E
_Els10_27protoRipListen_Object=MibTableColumn
els10_27protoRipListen=_Els10_27protoRipListen_Object((1,3,6,1,4,1,97,9,12,1,1,4),_Els10_27protoRipListen_Type())
els10_27protoRipListen.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27protoRipListen.setStatus(_A)
class _Els10_27protoTrunking_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_Els10_27protoTrunking_Type.__name__=_E
_Els10_27protoTrunking_Object=MibTableColumn
els10_27protoTrunking=_Els10_27protoTrunking_Object((1,3,6,1,4,1,97,9,12,1,1,5),_Els10_27protoTrunking_Type())
els10_27protoTrunking.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27protoTrunking.setStatus(_A)
class _Els10_27sprotoTransmitPacing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_Els10_27sprotoTransmitPacing_Type.__name__=_E
_Els10_27sprotoTransmitPacing_Object=MibTableColumn
els10_27sprotoTransmitPacing=_Els10_27sprotoTransmitPacing_Object((1,3,6,1,4,1,97,9,12,1,1,6),_Els10_27sprotoTransmitPacing_Type())
els10_27sprotoTransmitPacing.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27sprotoTransmitPacing.setStatus(_A)
_Els10_27trunk_ObjectIdentity=ObjectIdentity
els10_27trunk=_Els10_27trunk_ObjectIdentity((1,3,6,1,4,1,97,9,13))
_Els10_27trunkTable_Object=MibTable
els10_27trunkTable=_Els10_27trunkTable_Object((1,3,6,1,4,1,97,9,13,1))
if mibBuilder.loadTexts:els10_27trunkTable.setStatus(_A)
_Els10_27trunkEntry_Object=MibTableRow
els10_27trunkEntry=_Els10_27trunkEntry_Object((1,3,6,1,4,1,97,9,13,1,1))
els10_27trunkEntry.setIndexNames((0,_D,_t))
if mibBuilder.loadTexts:els10_27trunkEntry.setStatus(_A)
_Els10_27trunkIfIndex_Type=Integer32
_Els10_27trunkIfIndex_Object=MibTableColumn
els10_27trunkIfIndex=_Els10_27trunkIfIndex_Object((1,3,6,1,4,1,97,9,13,1,1,1),_Els10_27trunkIfIndex_Type())
els10_27trunkIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27trunkIfIndex.setStatus(_A)
class _Els10_27trunkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_O,1),('closed',2),('oneway',3),('joined',4),('perturbed',5),('helddown',6),('broken',7)))
_Els10_27trunkState_Type.__name__=_E
_Els10_27trunkState_Object=MibTableColumn
els10_27trunkState=_Els10_27trunkState_Object((1,3,6,1,4,1,97,9,13,1,1,2),_Els10_27trunkState_Type())
els10_27trunkState.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27trunkState.setStatus(_A)
_Els10_27trunkRemoteBridgeAddr_Type=OctetString
_Els10_27trunkRemoteBridgeAddr_Object=MibTableColumn
els10_27trunkRemoteBridgeAddr=_Els10_27trunkRemoteBridgeAddr_Object((1,3,6,1,4,1,97,9,13,1,1,3),_Els10_27trunkRemoteBridgeAddr_Type())
els10_27trunkRemoteBridgeAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27trunkRemoteBridgeAddr.setStatus(_A)
_Els10_27trunkRemoteIp_Type=IpAddress
_Els10_27trunkRemoteIp_Object=MibTableColumn
els10_27trunkRemoteIp=_Els10_27trunkRemoteIp_Object((1,3,6,1,4,1,97,9,13,1,1,4),_Els10_27trunkRemoteIp_Type())
els10_27trunkRemoteIp.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27trunkRemoteIp.setStatus(_A)
class _Els10_27trunkLastError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('none',1),('in-bpdu',2),('multiple-bridges',3),('ack-lost',4),('standby',5),('too-many-groups',6),('no-ack',7),('perturbed-threshold',8),('self-connect',9),('port-moved',10),('multiple-lan-types',11)))
_Els10_27trunkLastError_Type.__name__=_E
_Els10_27trunkLastError_Object=MibTableColumn
els10_27trunkLastError=_Els10_27trunkLastError_Object((1,3,6,1,4,1,97,9,13,1,1,5),_Els10_27trunkLastError_Type())
els10_27trunkLastError.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27trunkLastError.setStatus(_A)
_Els10_27trunkLinkOrdinal_Type=Integer32
_Els10_27trunkLinkOrdinal_Object=MibTableColumn
els10_27trunkLinkOrdinal=_Els10_27trunkLinkOrdinal_Object((1,3,6,1,4,1,97,9,13,1,1,6),_Els10_27trunkLinkOrdinal_Type())
els10_27trunkLinkOrdinal.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27trunkLinkOrdinal.setStatus(_A)
_Els10_27trunkLinkCount_Type=Integer32
_Els10_27trunkLinkCount_Object=MibTableColumn
els10_27trunkLinkCount=_Els10_27trunkLinkCount_Object((1,3,6,1,4,1,97,9,13,1,1,7),_Els10_27trunkLinkCount_Type())
els10_27trunkLinkCount.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27trunkLinkCount.setStatus(_A)
_Els10_27trunkLastChange_Type=Integer32
_Els10_27trunkLastChange_Object=MibTableColumn
els10_27trunkLastChange=_Els10_27trunkLastChange_Object((1,3,6,1,4,1,97,9,13,1,1,8),_Els10_27trunkLastChange_Type())
els10_27trunkLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27trunkLastChange.setStatus(_A)
_Els10_27workgroup_ObjectIdentity=ObjectIdentity
els10_27workgroup=_Els10_27workgroup_ObjectIdentity((1,3,6,1,4,1,97,9,14))
_Els10_27WorkGroupNextNumber_Type=Integer32
_Els10_27WorkGroupNextNumber_Object=MibScalar
els10_27WorkGroupNextNumber=_Els10_27WorkGroupNextNumber_Object((1,3,6,1,4,1,97,9,14,1),_Els10_27WorkGroupNextNumber_Type())
els10_27WorkGroupNextNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27WorkGroupNextNumber.setStatus(_A)
_Els10_27WorkGroupCurrentCount_Type=Integer32
_Els10_27WorkGroupCurrentCount_Object=MibScalar
els10_27WorkGroupCurrentCount=_Els10_27WorkGroupCurrentCount_Object((1,3,6,1,4,1,97,9,14,2),_Els10_27WorkGroupCurrentCount_Type())
els10_27WorkGroupCurrentCount.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27WorkGroupCurrentCount.setStatus(_A)
_Els10_27WorkGroupMaxCount_Type=Integer32
_Els10_27WorkGroupMaxCount_Object=MibScalar
els10_27WorkGroupMaxCount=_Els10_27WorkGroupMaxCount_Object((1,3,6,1,4,1,97,9,14,3),_Els10_27WorkGroupMaxCount_Type())
els10_27WorkGroupMaxCount.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27WorkGroupMaxCount.setStatus(_A)
_Els10_27WorkGroupTable_Object=MibTable
els10_27WorkGroupTable=_Els10_27WorkGroupTable_Object((1,3,6,1,4,1,97,9,14,4))
if mibBuilder.loadTexts:els10_27WorkGroupTable.setStatus(_A)
_Els10_27WorkGroupEntry_Object=MibTableRow
els10_27WorkGroupEntry=_Els10_27WorkGroupEntry_Object((1,3,6,1,4,1,97,9,14,4,1))
els10_27WorkGroupEntry.setIndexNames((0,_D,_u))
if mibBuilder.loadTexts:els10_27WorkGroupEntry.setStatus(_A)
_Els10_27WorkGroupNumber_Type=Integer32
_Els10_27WorkGroupNumber_Object=MibTableColumn
els10_27WorkGroupNumber=_Els10_27WorkGroupNumber_Object((1,3,6,1,4,1,97,9,14,4,1,1),_Els10_27WorkGroupNumber_Type())
els10_27WorkGroupNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27WorkGroupNumber.setStatus(_A)
_Els10_27WorkGroupName_Type=DisplayString
_Els10_27WorkGroupName_Object=MibTableColumn
els10_27WorkGroupName=_Els10_27WorkGroupName_Object((1,3,6,1,4,1,97,9,14,4,1,2),_Els10_27WorkGroupName_Type())
els10_27WorkGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27WorkGroupName.setStatus(_A)
_Els10_27WorkGroupPorts_Type=OctetString
_Els10_27WorkGroupPorts_Object=MibTableColumn
els10_27WorkGroupPorts=_Els10_27WorkGroupPorts_Object((1,3,6,1,4,1,97,9,14,4,1,3),_Els10_27WorkGroupPorts_Type())
els10_27WorkGroupPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27WorkGroupPorts.setStatus(_A)
class _Els10_27WorkGroupType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4)));namedValues=NamedValues(*(('all',3),('invalid',4)))
_Els10_27WorkGroupType_Type.__name__=_E
_Els10_27WorkGroupType_Object=MibTableColumn
els10_27WorkGroupType=_Els10_27WorkGroupType_Object((1,3,6,1,4,1,97,9,14,4,1,4),_Els10_27WorkGroupType_Type())
els10_27WorkGroupType.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27WorkGroupType.setStatus(_A)
_Els10_27trapMgt_ObjectIdentity=ObjectIdentity
els10_27trapMgt=_Els10_27trapMgt_ObjectIdentity((1,3,6,1,4,1,97,9,15))
_Els10_27trapControlTable_Object=MibTable
els10_27trapControlTable=_Els10_27trapControlTable_Object((1,3,6,1,4,1,97,9,15,1))
if mibBuilder.loadTexts:els10_27trapControlTable.setStatus(_A)
_Els10_27trapControlEntry_Object=MibTableRow
els10_27trapControlEntry=_Els10_27trapControlEntry_Object((1,3,6,1,4,1,97,9,15,1,1))
els10_27trapControlEntry.setIndexNames((0,_D,_v))
if mibBuilder.loadTexts:els10_27trapControlEntry.setStatus(_A)
_Els10_27trapIndex_Type=Integer32
_Els10_27trapIndex_Object=MibTableColumn
els10_27trapIndex=_Els10_27trapIndex_Object((1,3,6,1,4,1,97,9,15,1,1,1),_Els10_27trapIndex_Type())
els10_27trapIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27trapIndex.setStatus(_A)
class _Els10_27trapEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_Els10_27trapEnabled_Type.__name__=_E
_Els10_27trapEnabled_Object=MibTableColumn
els10_27trapEnabled=_Els10_27trapEnabled_Object((1,3,6,1,4,1,97,9,15,1,1,2),_Els10_27trapEnabled_Type())
els10_27trapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27trapEnabled.setStatus(_A)
class _Els10_27trapSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_R,1),(_S,2),(_T,3),(_U,4),(_V,5)))
_Els10_27trapSeverity_Type.__name__=_E
_Els10_27trapSeverity_Object=MibTableColumn
els10_27trapSeverity=_Els10_27trapSeverity_Object((1,3,6,1,4,1,97,9,15,1,1,3),_Els10_27trapSeverity_Type())
els10_27trapSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27trapSeverity.setStatus(_A)
_Els10_27trapText_Type=DisplayString
_Els10_27trapText_Object=MibTableColumn
els10_27trapText=_Els10_27trapText_Object((1,3,6,1,4,1,97,9,15,1,1,4),_Els10_27trapText_Type())
els10_27trapText.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27trapText.setStatus(_A)
_Els10_27trapSeverityControlTable_Object=MibTable
els10_27trapSeverityControlTable=_Els10_27trapSeverityControlTable_Object((1,3,6,1,4,1,97,9,15,2))
if mibBuilder.loadTexts:els10_27trapSeverityControlTable.setStatus(_A)
_Els10_27trapSeverityControlEntry_Object=MibTableRow
els10_27trapSeverityControlEntry=_Els10_27trapSeverityControlEntry_Object((1,3,6,1,4,1,97,9,15,2,1))
els10_27trapSeverityControlEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:els10_27trapSeverityControlEntry.setStatus(_A)
class _Els10_27trapSeverityControlSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_R,1),(_S,2),(_T,3),(_U,4),(_V,5)))
_Els10_27trapSeverityControlSeverity_Type.__name__=_E
_Els10_27trapSeverityControlSeverity_Object=MibTableColumn
els10_27trapSeverityControlSeverity=_Els10_27trapSeverityControlSeverity_Object((1,3,6,1,4,1,97,9,15,2,1,1),_Els10_27trapSeverityControlSeverity_Type())
els10_27trapSeverityControlSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27trapSeverityControlSeverity.setStatus(_A)
class _Els10_27trapSeverityEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_Els10_27trapSeverityEnable_Type.__name__=_E
_Els10_27trapSeverityEnable_Object=MibTableColumn
els10_27trapSeverityEnable=_Els10_27trapSeverityEnable_Object((1,3,6,1,4,1,97,9,15,2,1,2),_Els10_27trapSeverityEnable_Type())
els10_27trapSeverityEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27trapSeverityEnable.setStatus(_A)
class _Els10_27trapIncludeText_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_Els10_27trapIncludeText_Type.__name__=_E
_Els10_27trapIncludeText_Object=MibScalar
els10_27trapIncludeText=_Els10_27trapIncludeText_Object((1,3,6,1,4,1,97,9,15,3),_Els10_27trapIncludeText_Type())
els10_27trapIncludeText.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27trapIncludeText.setStatus(_A)
_Els10_27trapTime_Type=TimeTicks
_Els10_27trapTime_Object=MibScalar
els10_27trapTime=_Els10_27trapTime_Object((1,3,6,1,4,1,97,9,15,4),_Els10_27trapTime_Type())
els10_27trapTime.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27trapTime.setStatus(_A)
_Els10_27trapRetry_Type=Integer32
_Els10_27trapRetry_Object=MibScalar
els10_27trapRetry=_Els10_27trapRetry_Object((1,3,6,1,4,1,97,9,15,5),_Els10_27trapRetry_Type())
els10_27trapRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27trapRetry.setStatus(_A)
_Els10_27trapNumber_Type=Integer32
_Els10_27trapNumber_Object=MibScalar
els10_27trapNumber=_Els10_27trapNumber_Object((1,3,6,1,4,1,97,9,15,6),_Els10_27trapNumber_Type())
els10_27trapNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27trapNumber.setStatus(_A)
_Els10_27trapTable_Object=MibTable
els10_27trapTable=_Els10_27trapTable_Object((1,3,6,1,4,1,97,9,15,7))
if mibBuilder.loadTexts:els10_27trapTable.setStatus(_A)
_Els10_27trapEntry_Object=MibTableRow
els10_27trapEntry=_Els10_27trapEntry_Object((1,3,6,1,4,1,97,9,15,7,1))
els10_27trapEntry.setIndexNames((0,_D,_w))
if mibBuilder.loadTexts:els10_27trapEntry.setStatus(_A)
_Els10_27trapEntryIndex_Type=Integer32
_Els10_27trapEntryIndex_Object=MibTableColumn
els10_27trapEntryIndex=_Els10_27trapEntryIndex_Object((1,3,6,1,4,1,97,9,15,7,1,1),_Els10_27trapEntryIndex_Type())
els10_27trapEntryIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27trapEntryIndex.setStatus(_A)
_Els10_27trapEntryTimeStamp_Type=TimeTicks
_Els10_27trapEntryTimeStamp_Object=MibTableColumn
els10_27trapEntryTimeStamp=_Els10_27trapEntryTimeStamp_Object((1,3,6,1,4,1,97,9,15,7,1,2),_Els10_27trapEntryTimeStamp_Type())
els10_27trapEntryTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27trapEntryTimeStamp.setStatus(_A)
_Els10_27trapEntryText_Type=DisplayString
_Els10_27trapEntryText_Object=MibTableColumn
els10_27trapEntryText=_Els10_27trapEntryText_Object((1,3,6,1,4,1,97,9,15,7,1,3),_Els10_27trapEntryText_Type())
els10_27trapEntryText.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27trapEntryText.setStatus(_A)
_Els10_27trapEntryNumber_Type=Integer32
_Els10_27trapEntryNumber_Object=MibTableColumn
els10_27trapEntryNumber=_Els10_27trapEntryNumber_Object((1,3,6,1,4,1,97,9,15,7,1,4),_Els10_27trapEntryNumber_Type())
els10_27trapEntryNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27trapEntryNumber.setStatus(_A)
class _Els10_27trapEntrySeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_R,1),(_S,2),(_T,3),(_U,4),(_V,5)))
_Els10_27trapEntrySeverity_Type.__name__=_E
_Els10_27trapEntrySeverity_Object=MibTableColumn
els10_27trapEntrySeverity=_Els10_27trapEntrySeverity_Object((1,3,6,1,4,1,97,9,15,7,1,5),_Els10_27trapEntrySeverity_Type())
els10_27trapEntrySeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27trapEntrySeverity.setStatus(_A)
_Els10_27pingMgt_ObjectIdentity=ObjectIdentity
els10_27pingMgt=_Els10_27pingMgt_ObjectIdentity((1,3,6,1,4,1,97,9,16))
_Els10_27pingDataTimeout_Type=TimeTicks
_Els10_27pingDataTimeout_Object=MibScalar
els10_27pingDataTimeout=_Els10_27pingDataTimeout_Object((1,3,6,1,4,1,97,9,16,1),_Els10_27pingDataTimeout_Type())
els10_27pingDataTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27pingDataTimeout.setStatus(_A)
_Els10_27pingTable_Object=MibTable
els10_27pingTable=_Els10_27pingTable_Object((1,3,6,1,4,1,97,9,16,2))
if mibBuilder.loadTexts:els10_27pingTable.setStatus(_A)
_Els10_27pingEntry_Object=MibTableRow
els10_27pingEntry=_Els10_27pingEntry_Object((1,3,6,1,4,1,97,9,16,2,1))
els10_27pingEntry.setIndexNames((0,_D,_x),(0,_D,_y))
if mibBuilder.loadTexts:els10_27pingEntry.setStatus(_A)
_Els10_27pingNMSAddr_Type=IpAddress
_Els10_27pingNMSAddr_Object=MibTableColumn
els10_27pingNMSAddr=_Els10_27pingNMSAddr_Object((1,3,6,1,4,1,97,9,16,2,1,1),_Els10_27pingNMSAddr_Type())
els10_27pingNMSAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27pingNMSAddr.setStatus(_A)
_Els10_27pingDestAddr_Type=IpAddress
_Els10_27pingDestAddr_Object=MibTableColumn
els10_27pingDestAddr=_Els10_27pingDestAddr_Object((1,3,6,1,4,1,97,9,16,2,1,2),_Els10_27pingDestAddr_Type())
els10_27pingDestAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27pingDestAddr.setStatus(_A)
class _Els10_27pingState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_z,0),('active',1),('timed-out',2),(_A0,3)))
_Els10_27pingState_Type.__name__=_E
_Els10_27pingState_Object=MibTableColumn
els10_27pingState=_Els10_27pingState_Object((1,3,6,1,4,1,97,9,16,2,1,3),_Els10_27pingState_Type())
els10_27pingState.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27pingState.setStatus(_A)
_Els10_27pingCount_Type=Integer32
_Els10_27pingCount_Object=MibTableColumn
els10_27pingCount=_Els10_27pingCount_Object((1,3,6,1,4,1,97,9,16,2,1,4),_Els10_27pingCount_Type())
els10_27pingCount.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27pingCount.setStatus(_A)
_Els10_27pingDataSize_Type=Integer32
_Els10_27pingDataSize_Object=MibTableColumn
els10_27pingDataSize=_Els10_27pingDataSize_Object((1,3,6,1,4,1,97,9,16,2,1,5),_Els10_27pingDataSize_Type())
els10_27pingDataSize.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27pingDataSize.setStatus(_A)
_Els10_27pingWait_Type=TimeTicks
_Els10_27pingWait_Object=MibTableColumn
els10_27pingWait=_Els10_27pingWait_Object((1,3,6,1,4,1,97,9,16,2,1,6),_Els10_27pingWait_Type())
els10_27pingWait.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27pingWait.setStatus(_A)
_Els10_27pingTimeOut_Type=TimeTicks
_Els10_27pingTimeOut_Object=MibTableColumn
els10_27pingTimeOut=_Els10_27pingTimeOut_Object((1,3,6,1,4,1,97,9,16,2,1,7),_Els10_27pingTimeOut_Type())
els10_27pingTimeOut.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27pingTimeOut.setStatus(_A)
class _Els10_27pingOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),(_O,2)))
_Els10_27pingOperation_Type.__name__=_E
_Els10_27pingOperation_Object=MibTableColumn
els10_27pingOperation=_Els10_27pingOperation_Object((1,3,6,1,4,1,97,9,16,2,1,8),_Els10_27pingOperation_Type())
els10_27pingOperation.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27pingOperation.setStatus(_A)
_Els10_27pingMin_Type=TimeTicks
_Els10_27pingMin_Object=MibTableColumn
els10_27pingMin=_Els10_27pingMin_Object((1,3,6,1,4,1,97,9,16,2,1,9),_Els10_27pingMin_Type())
els10_27pingMin.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27pingMin.setStatus(_A)
_Els10_27pingMax_Type=TimeTicks
_Els10_27pingMax_Object=MibTableColumn
els10_27pingMax=_Els10_27pingMax_Object((1,3,6,1,4,1,97,9,16,2,1,10),_Els10_27pingMax_Type())
els10_27pingMax.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27pingMax.setStatus(_A)
_Els10_27pingAvg_Type=TimeTicks
_Els10_27pingAvg_Object=MibTableColumn
els10_27pingAvg=_Els10_27pingAvg_Object((1,3,6,1,4,1,97,9,16,2,1,11),_Els10_27pingAvg_Type())
els10_27pingAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27pingAvg.setStatus(_A)
_Els10_27pingNumTransmitted_Type=Integer32
_Els10_27pingNumTransmitted_Object=MibTableColumn
els10_27pingNumTransmitted=_Els10_27pingNumTransmitted_Object((1,3,6,1,4,1,97,9,16,2,1,12),_Els10_27pingNumTransmitted_Type())
els10_27pingNumTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27pingNumTransmitted.setStatus(_A)
_Els10_27pingNumReceived_Type=Integer32
_Els10_27pingNumReceived_Object=MibTableColumn
els10_27pingNumReceived=_Els10_27pingNumReceived_Object((1,3,6,1,4,1,97,9,16,2,1,13),_Els10_27pingNumReceived_Type())
els10_27pingNumReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27pingNumReceived.setStatus(_A)
_Els10_27traceMgt_ObjectIdentity=ObjectIdentity
els10_27traceMgt=_Els10_27traceMgt_ObjectIdentity((1,3,6,1,4,1,97,9,17))
_Els10_27traceDataTimeout_Type=TimeTicks
_Els10_27traceDataTimeout_Object=MibScalar
els10_27traceDataTimeout=_Els10_27traceDataTimeout_Object((1,3,6,1,4,1,97,9,17,1),_Els10_27traceDataTimeout_Type())
els10_27traceDataTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27traceDataTimeout.setStatus(_A)
_Els10_27traceTable_Object=MibTable
els10_27traceTable=_Els10_27traceTable_Object((1,3,6,1,4,1,97,9,17,2))
if mibBuilder.loadTexts:els10_27traceTable.setStatus(_A)
_Els10_27traceEntry_Object=MibTableRow
els10_27traceEntry=_Els10_27traceEntry_Object((1,3,6,1,4,1,97,9,17,2,1))
els10_27traceEntry.setIndexNames((0,_D,_A1),(0,_D,_A2),(0,_D,_A3),(0,_D,_A4))
if mibBuilder.loadTexts:els10_27traceEntry.setStatus(_A)
_Els10_27traceNMSAddr_Type=IpAddress
_Els10_27traceNMSAddr_Object=MibTableColumn
els10_27traceNMSAddr=_Els10_27traceNMSAddr_Object((1,3,6,1,4,1,97,9,17,2,1,1),_Els10_27traceNMSAddr_Type())
els10_27traceNMSAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27traceNMSAddr.setStatus(_A)
_Els10_27traceDestAddr_Type=IpAddress
_Els10_27traceDestAddr_Object=MibTableColumn
els10_27traceDestAddr=_Els10_27traceDestAddr_Object((1,3,6,1,4,1,97,9,17,2,1,2),_Els10_27traceDestAddr_Type())
els10_27traceDestAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27traceDestAddr.setStatus(_A)
_Els10_27traceMaxTTL_Type=Integer32
_Els10_27traceMaxTTL_Object=MibTableColumn
els10_27traceMaxTTL=_Els10_27traceMaxTTL_Object((1,3,6,1,4,1,97,9,17,2,1,3),_Els10_27traceMaxTTL_Type())
els10_27traceMaxTTL.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27traceMaxTTL.setStatus(_A)
_Els10_27traceDataSize_Type=Integer32
_Els10_27traceDataSize_Object=MibTableColumn
els10_27traceDataSize=_Els10_27traceDataSize_Object((1,3,6,1,4,1,97,9,17,2,1,4),_Els10_27traceDataSize_Type())
els10_27traceDataSize.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27traceDataSize.setStatus(_A)
_Els10_27traceNumProbes_Type=Integer32
_Els10_27traceNumProbes_Object=MibTableColumn
els10_27traceNumProbes=_Els10_27traceNumProbes_Object((1,3,6,1,4,1,97,9,17,2,1,5),_Els10_27traceNumProbes_Type())
els10_27traceNumProbes.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27traceNumProbes.setStatus(_A)
_Els10_27traceWait_Type=TimeTicks
_Els10_27traceWait_Object=MibTableColumn
els10_27traceWait=_Els10_27traceWait_Object((1,3,6,1,4,1,97,9,17,2,1,6),_Els10_27traceWait_Type())
els10_27traceWait.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27traceWait.setStatus(_A)
class _Els10_27traceOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),(_O,2)))
_Els10_27traceOperation_Type.__name__=_E
_Els10_27traceOperation_Object=MibTableColumn
els10_27traceOperation=_Els10_27traceOperation_Object((1,3,6,1,4,1,97,9,17,2,1,7),_Els10_27traceOperation_Type())
els10_27traceOperation.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27traceOperation.setStatus(_A)
_Els10_27traceHop_Type=Integer32
_Els10_27traceHop_Object=MibTableColumn
els10_27traceHop=_Els10_27traceHop_Object((1,3,6,1,4,1,97,9,17,2,1,8),_Els10_27traceHop_Type())
els10_27traceHop.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27traceHop.setStatus(_A)
_Els10_27traceHopAddr_Type=IpAddress
_Els10_27traceHopAddr_Object=MibTableColumn
els10_27traceHopAddr=_Els10_27traceHopAddr_Object((1,3,6,1,4,1,97,9,17,2,1,9),_Els10_27traceHopAddr_Type())
els10_27traceHopAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27traceHopAddr.setStatus(_A)
_Els10_27traceProbe_Type=Integer32
_Els10_27traceProbe_Object=MibTableColumn
els10_27traceProbe=_Els10_27traceProbe_Object((1,3,6,1,4,1,97,9,17,2,1,10),_Els10_27traceProbe_Type())
els10_27traceProbe.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27traceProbe.setStatus(_A)
class _Els10_27traceState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_z,0),('active',1),('time-exceeded',2),('host-unreachable',3),('net-unreachable',4),(_A0,5)))
_Els10_27traceState_Type.__name__=_E
_Els10_27traceState_Object=MibTableColumn
els10_27traceState=_Els10_27traceState_Object((1,3,6,1,4,1,97,9,17,2,1,11),_Els10_27traceState_Type())
els10_27traceState.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27traceState.setStatus(_A)
_Els10_27traceTime_Type=TimeTicks
_Els10_27traceTime_Object=MibTableColumn
els10_27traceTime=_Els10_27traceTime_Object((1,3,6,1,4,1,97,9,17,2,1,12),_Els10_27traceTime_Type())
els10_27traceTime.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27traceTime.setStatus(_A)
_Els10_27volmirrorgroup_ObjectIdentity=ObjectIdentity
els10_27volmirrorgroup=_Els10_27volmirrorgroup_ObjectIdentity((1,3,6,1,4,1,97,9,19))
class _Els10_27volmirrorMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),('on',1)))
_Els10_27volmirrorMode_Type.__name__=_E
_Els10_27volmirrorMode_Object=MibScalar
els10_27volmirrorMode=_Els10_27volmirrorMode_Object((1,3,6,1,4,1,97,9,19,1),_Els10_27volmirrorMode_Type())
els10_27volmirrorMode.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27volmirrorMode.setStatus(_A)
_Els10_27volmirrorPort_Type=Integer32
_Els10_27volmirrorPort_Object=MibScalar
els10_27volmirrorPort=_Els10_27volmirrorPort_Object((1,3,6,1,4,1,97,9,19,2),_Els10_27volmirrorPort_Type())
els10_27volmirrorPort.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27volmirrorPort.setStatus(_A)
_Els10_27volmonitorPort_Type=Integer32
_Els10_27volmonitorPort_Object=MibScalar
els10_27volmonitorPort=_Els10_27volmonitorPort_Object((1,3,6,1,4,1,97,9,19,3),_Els10_27volmonitorPort_Type())
els10_27volmonitorPort.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27volmonitorPort.setStatus(_A)
_Els10_27volMirrorMacTable_Object=MibTable
els10_27volMirrorMacTable=_Els10_27volMirrorMacTable_Object((1,3,6,1,4,1,97,9,19,4))
if mibBuilder.loadTexts:els10_27volMirrorMacTable.setStatus(_A)
_Els10_27volmirrorMacEntry_Object=MibTableRow
els10_27volmirrorMacEntry=_Els10_27volmirrorMacEntry_Object((1,3,6,1,4,1,97,9,19,4,1))
els10_27volmirrorMacEntry.setIndexNames((0,_D,_A5))
if mibBuilder.loadTexts:els10_27volmirrorMacEntry.setStatus(_A)
_Els10_27volmirrorIndex_Type=Integer32
_Els10_27volmirrorIndex_Object=MibTableColumn
els10_27volmirrorIndex=_Els10_27volmirrorIndex_Object((1,3,6,1,4,1,97,9,19,4,1,1),_Els10_27volmirrorIndex_Type())
els10_27volmirrorIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27volmirrorIndex.setStatus(_A)
_Els10_27volmirrorMac1_Type=OctetString
_Els10_27volmirrorMac1_Object=MibTableColumn
els10_27volmirrorMac1=_Els10_27volmirrorMac1_Object((1,3,6,1,4,1,97,9,19,4,1,2),_Els10_27volmirrorMac1_Type())
els10_27volmirrorMac1.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27volmirrorMac1.setStatus(_A)
_Els10_27VlanBridgeConfig_ObjectIdentity=ObjectIdentity
els10_27VlanBridgeConfig=_Els10_27VlanBridgeConfig_ObjectIdentity((1,3,6,1,4,1,97,9,20))
_Els10_27VlanVersionNumber_Type=Integer32
_Els10_27VlanVersionNumber_Object=MibScalar
els10_27VlanVersionNumber=_Els10_27VlanVersionNumber_Object((1,3,6,1,4,1,97,9,20,1),_Els10_27VlanVersionNumber_Type())
els10_27VlanVersionNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27VlanVersionNumber.setStatus(_A)
class _Els10_27VlanOperatingMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ieee8021d',1),('ieee8021Q',2)))
_Els10_27VlanOperatingMode_Type.__name__=_E
_Els10_27VlanOperatingMode_Object=MibScalar
els10_27VlanOperatingMode=_Els10_27VlanOperatingMode_Object((1,3,6,1,4,1,97,9,20,2),_Els10_27VlanOperatingMode_Type())
els10_27VlanOperatingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27VlanOperatingMode.setStatus(_A)
class _Els10_27VlanResetDefaults_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('operating',1),('reset',2)))
_Els10_27VlanResetDefaults_Type.__name__=_E
_Els10_27VlanResetDefaults_Object=MibScalar
els10_27VlanResetDefaults=_Els10_27VlanResetDefaults_Object((1,3,6,1,4,1,97,9,20,3),_Els10_27VlanResetDefaults_Type())
els10_27VlanResetDefaults.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27VlanResetDefaults.setStatus(_A)
class _Els10_27VlanGVRPEnable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_Els10_27VlanGVRPEnable_Type.__name__=_H
_Els10_27VlanGVRPEnable_Object=MibScalar
els10_27VlanGVRPEnable=_Els10_27VlanGVRPEnable_Object((1,3,6,1,4,1,97,9,20,4),_Els10_27VlanGVRPEnable_Type())
els10_27VlanGVRPEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27VlanGVRPEnable.setStatus(_A)
class _Els10_27VlanAccessList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_Els10_27VlanAccessList_Type.__name__=_H
_Els10_27VlanAccessList_Object=MibScalar
els10_27VlanAccessList=_Els10_27VlanAccessList_Object((1,3,6,1,4,1,97,9,20,5),_Els10_27VlanAccessList_Type())
els10_27VlanAccessList.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27VlanAccessList.setStatus(_A)
_Els10_27VlanConfigVlan_ObjectIdentity=ObjectIdentity
els10_27VlanConfigVlan=_Els10_27VlanConfigVlan_ObjectIdentity((1,3,6,1,4,1,97,9,20,6))
_Els10_27VlanNumActiveEntries_Type=Integer32
_Els10_27VlanNumActiveEntries_Object=MibScalar
els10_27VlanNumActiveEntries=_Els10_27VlanNumActiveEntries_Object((1,3,6,1,4,1,97,9,20,6,1),_Els10_27VlanNumActiveEntries_Type())
els10_27VlanNumActiveEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27VlanNumActiveEntries.setStatus(_A)
_Els10_27VlanNumConfiguredEntries_Type=Integer32
_Els10_27VlanNumConfiguredEntries_Object=MibScalar
els10_27VlanNumConfiguredEntries=_Els10_27VlanNumConfiguredEntries_Object((1,3,6,1,4,1,97,9,20,6,2),_Els10_27VlanNumConfiguredEntries_Type())
els10_27VlanNumConfiguredEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27VlanNumConfiguredEntries.setStatus(_A)
_Els10_27VlanMaxNumEntries_Type=Integer32
_Els10_27VlanMaxNumEntries_Object=MibScalar
els10_27VlanMaxNumEntries=_Els10_27VlanMaxNumEntries_Object((1,3,6,1,4,1,97,9,20,6,3),_Els10_27VlanMaxNumEntries_Type())
els10_27VlanMaxNumEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27VlanMaxNumEntries.setStatus(_A)
_Els10_27VlanConfigTable_Object=MibTable
els10_27VlanConfigTable=_Els10_27VlanConfigTable_Object((1,3,6,1,4,1,97,9,20,6,4))
if mibBuilder.loadTexts:els10_27VlanConfigTable.setStatus(_A)
_Els10_27VlanConfigEntry_Object=MibTableRow
els10_27VlanConfigEntry=_Els10_27VlanConfigEntry_Object((1,3,6,1,4,1,97,9,20,6,4,1))
els10_27VlanConfigEntry.setIndexNames((0,_D,_A6))
if mibBuilder.loadTexts:els10_27VlanConfigEntry.setStatus(_A)
_Els10_27VlanConfigIndex_Type=Integer32
_Els10_27VlanConfigIndex_Object=MibTableColumn
els10_27VlanConfigIndex=_Els10_27VlanConfigIndex_Object((1,3,6,1,4,1,97,9,20,6,4,1,1),_Els10_27VlanConfigIndex_Type())
els10_27VlanConfigIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27VlanConfigIndex.setStatus(_A)
class _Els10_27VlanConfigVID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_Els10_27VlanConfigVID_Type.__name__=_H
_Els10_27VlanConfigVID_Object=MibTableColumn
els10_27VlanConfigVID=_Els10_27VlanConfigVID_Object((1,3,6,1,4,1,97,9,20,6,4,1,2),_Els10_27VlanConfigVID_Type())
els10_27VlanConfigVID.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27VlanConfigVID.setStatus(_A)
class _Els10_27VlanConfigPorts_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_Els10_27VlanConfigPorts_Type.__name__=_H
_Els10_27VlanConfigPorts_Object=MibTableColumn
els10_27VlanConfigPorts=_Els10_27VlanConfigPorts_Object((1,3,6,1,4,1,97,9,20,6,4,1,3),_Els10_27VlanConfigPorts_Type())
els10_27VlanConfigPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27VlanConfigPorts.setStatus(_A)
_Els10_27VlanConfigIP_Type=IpAddress
_Els10_27VlanConfigIP_Object=MibTableColumn
els10_27VlanConfigIP=_Els10_27VlanConfigIP_Object((1,3,6,1,4,1,97,9,20,6,4,1,4),_Els10_27VlanConfigIP_Type())
els10_27VlanConfigIP.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27VlanConfigIP.setStatus(_A)
_Els10_27VlanConfigIPMask_Type=IpAddress
_Els10_27VlanConfigIPMask_Object=MibTableColumn
els10_27VlanConfigIPMask=_Els10_27VlanConfigIPMask_Object((1,3,6,1,4,1,97,9,20,6,4,1,5),_Els10_27VlanConfigIPMask_Type())
els10_27VlanConfigIPMask.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27VlanConfigIPMask.setStatus(_A)
class _Els10_27VlanConfigName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Els10_27VlanConfigName_Type.__name__=_k
_Els10_27VlanConfigName_Object=MibTableColumn
els10_27VlanConfigName=_Els10_27VlanConfigName_Object((1,3,6,1,4,1,97,9,20,6,4,1,6),_Els10_27VlanConfigName_Type())
els10_27VlanConfigName.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27VlanConfigName.setStatus(_A)
_Els10_27VlanConfigStatus_Type=Integer32
_Els10_27VlanConfigStatus_Object=MibTableColumn
els10_27VlanConfigStatus=_Els10_27VlanConfigStatus_Object((1,3,6,1,4,1,97,9,20,6,4,1,7),_Els10_27VlanConfigStatus_Type())
els10_27VlanConfigStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27VlanConfigStatus.setStatus(_A)
class _Els10_27VlanConfigEstablish_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_N,2)))
_Els10_27VlanConfigEstablish_Type.__name__=_E
_Els10_27VlanConfigEstablish_Object=MibTableColumn
els10_27VlanConfigEstablish=_Els10_27VlanConfigEstablish_Object((1,3,6,1,4,1,97,9,20,6,4,1,8),_Els10_27VlanConfigEstablish_Type())
els10_27VlanConfigEstablish.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27VlanConfigEstablish.setStatus(_A)
_Els10_27VlanConfigEgressTable_Object=MibTable
els10_27VlanConfigEgressTable=_Els10_27VlanConfigEgressTable_Object((1,3,6,1,4,1,97,9,20,6,5))
if mibBuilder.loadTexts:els10_27VlanConfigEgressTable.setStatus(_A)
_Els10_27VlanConfigEgressEntry_Object=MibTableRow
els10_27VlanConfigEgressEntry=_Els10_27VlanConfigEgressEntry_Object((1,3,6,1,4,1,97,9,20,6,5,1))
els10_27VlanConfigEgressEntry.setIndexNames((0,_D,_A7))
if mibBuilder.loadTexts:els10_27VlanConfigEgressEntry.setStatus(_A)
_Els10_27VlanEgressIndex_Type=Integer32
_Els10_27VlanEgressIndex_Object=MibTableColumn
els10_27VlanEgressIndex=_Els10_27VlanEgressIndex_Object((1,3,6,1,4,1,97,9,20,6,5,1,1),_Els10_27VlanEgressIndex_Type())
els10_27VlanEgressIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27VlanEgressIndex.setStatus(_A)
class _Els10_27VlanEgressVID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_Els10_27VlanEgressVID_Type.__name__=_H
_Els10_27VlanEgressVID_Object=MibTableColumn
els10_27VlanEgressVID=_Els10_27VlanEgressVID_Object((1,3,6,1,4,1,97,9,20,6,5,1,2),_Els10_27VlanEgressVID_Type())
els10_27VlanEgressVID.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27VlanEgressVID.setStatus(_A)
class _Els10_27VlanEgressList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_Els10_27VlanEgressList_Type.__name__=_H
_Els10_27VlanEgressList_Object=MibTableColumn
els10_27VlanEgressList=_Els10_27VlanEgressList_Object((1,3,6,1,4,1,97,9,20,6,5,1,3),_Els10_27VlanEgressList_Type())
els10_27VlanEgressList.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27VlanEgressList.setStatus(_A)
_Els10_27VlanEgressStatus_Type=Integer32
_Els10_27VlanEgressStatus_Object=MibTableColumn
els10_27VlanEgressStatus=_Els10_27VlanEgressStatus_Object((1,3,6,1,4,1,97,9,20,6,5,1,4),_Els10_27VlanEgressStatus_Type())
els10_27VlanEgressStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27VlanEgressStatus.setStatus(_A)
_Els10_27VlanFilterGVRPTable_Object=MibTable
els10_27VlanFilterGVRPTable=_Els10_27VlanFilterGVRPTable_Object((1,3,6,1,4,1,97,9,20,6,6))
if mibBuilder.loadTexts:els10_27VlanFilterGVRPTable.setStatus(_A)
_Els10_27VlanFilterGVRPEntry_Object=MibTableRow
els10_27VlanFilterGVRPEntry=_Els10_27VlanFilterGVRPEntry_Object((1,3,6,1,4,1,97,9,20,6,6,1))
els10_27VlanFilterGVRPEntry.setIndexNames((0,_D,_A8))
if mibBuilder.loadTexts:els10_27VlanFilterGVRPEntry.setStatus(_A)
_Els10_27VlanFilterGVRPIndex_Type=Integer32
_Els10_27VlanFilterGVRPIndex_Object=MibTableColumn
els10_27VlanFilterGVRPIndex=_Els10_27VlanFilterGVRPIndex_Object((1,3,6,1,4,1,97,9,20,6,6,1,1),_Els10_27VlanFilterGVRPIndex_Type())
els10_27VlanFilterGVRPIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27VlanFilterGVRPIndex.setStatus(_A)
class _Els10_27VlanFilterGVRPVID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_Els10_27VlanFilterGVRPVID_Type.__name__=_H
_Els10_27VlanFilterGVRPVID_Object=MibTableColumn
els10_27VlanFilterGVRPVID=_Els10_27VlanFilterGVRPVID_Object((1,3,6,1,4,1,97,9,20,6,6,1,2),_Els10_27VlanFilterGVRPVID_Type())
els10_27VlanFilterGVRPVID.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27VlanFilterGVRPVID.setStatus(_A)
class _Els10_27VlanFilterGVRPList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_Els10_27VlanFilterGVRPList_Type.__name__=_H
_Els10_27VlanFilterGVRPList_Object=MibTableColumn
els10_27VlanFilterGVRPList=_Els10_27VlanFilterGVRPList_Object((1,3,6,1,4,1,97,9,20,6,6,1,3),_Els10_27VlanFilterGVRPList_Type())
els10_27VlanFilterGVRPList.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27VlanFilterGVRPList.setStatus(_A)
_Els10_27VlanFilterGVRPStatus_Type=Integer32
_Els10_27VlanFilterGVRPStatus_Object=MibTableColumn
els10_27VlanFilterGVRPStatus=_Els10_27VlanFilterGVRPStatus_Object((1,3,6,1,4,1,97,9,20,6,6,1,4),_Els10_27VlanFilterGVRPStatus_Type())
els10_27VlanFilterGVRPStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27VlanFilterGVRPStatus.setStatus(_A)
class _Els10_27VlanFilterGVRPEstablishVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_N,2)))
_Els10_27VlanFilterGVRPEstablishVID_Type.__name__=_E
_Els10_27VlanFilterGVRPEstablishVID_Object=MibTableColumn
els10_27VlanFilterGVRPEstablishVID=_Els10_27VlanFilterGVRPEstablishVID_Object((1,3,6,1,4,1,97,9,20,6,6,1,5),_Els10_27VlanFilterGVRPEstablishVID_Type())
els10_27VlanFilterGVRPEstablishVID.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27VlanFilterGVRPEstablishVID.setStatus(_A)
_Els10_27VlanStaticTable_Object=MibTable
els10_27VlanStaticTable=_Els10_27VlanStaticTable_Object((1,3,6,1,4,1,97,9,20,6,7))
if mibBuilder.loadTexts:els10_27VlanStaticTable.setStatus(_A)
_Els10_27VlanStaticEntry_Object=MibTableRow
els10_27VlanStaticEntry=_Els10_27VlanStaticEntry_Object((1,3,6,1,4,1,97,9,20,6,7,1))
els10_27VlanStaticEntry.setIndexNames((0,_D,_A9))
if mibBuilder.loadTexts:els10_27VlanStaticEntry.setStatus(_A)
class _Els10_27VlanStaticVID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_Els10_27VlanStaticVID_Type.__name__=_H
_Els10_27VlanStaticVID_Object=MibTableColumn
els10_27VlanStaticVID=_Els10_27VlanStaticVID_Object((1,3,6,1,4,1,97,9,20,6,7,1,1),_Els10_27VlanStaticVID_Type())
els10_27VlanStaticVID.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27VlanStaticVID.setStatus(_A)
_Els10_27VlanStaticMAC_Type=PhysAddress
_Els10_27VlanStaticMAC_Object=MibTableColumn
els10_27VlanStaticMAC=_Els10_27VlanStaticMAC_Object((1,3,6,1,4,1,97,9,20,6,7,1,2),_Els10_27VlanStaticMAC_Type())
els10_27VlanStaticMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27VlanStaticMAC.setStatus(_A)
_Els10_27VlanStaticPort_Type=Integer32
_Els10_27VlanStaticPort_Object=MibTableColumn
els10_27VlanStaticPort=_Els10_27VlanStaticPort_Object((1,3,6,1,4,1,97,9,20,6,7,1,3),_Els10_27VlanStaticPort_Type())
els10_27VlanStaticPort.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27VlanStaticPort.setStatus(_A)
class _Els10_27VlanStaticEstablish_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_N,2)))
_Els10_27VlanStaticEstablish_Type.__name__=_E
_Els10_27VlanStaticEstablish_Object=MibTableColumn
els10_27VlanStaticEstablish=_Els10_27VlanStaticEstablish_Object((1,3,6,1,4,1,97,9,20,6,7,1,4),_Els10_27VlanStaticEstablish_Type())
els10_27VlanStaticEstablish.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27VlanStaticEstablish.setStatus(_A)
_Els10_27volipmgroup_ObjectIdentity=ObjectIdentity
els10_27volipmgroup=_Els10_27volipmgroup_ObjectIdentity((1,3,6,1,4,1,97,9,21))
class _Els10_27IPMulticastStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_I,1)))
_Els10_27IPMulticastStatus_Type.__name__=_E
_Els10_27IPMulticastStatus_Object=MibScalar
els10_27IPMulticastStatus=_Els10_27IPMulticastStatus_Object((1,3,6,1,4,1,97,9,21,1),_Els10_27IPMulticastStatus_Type())
els10_27IPMulticastStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27IPMulticastStatus.setStatus(_A)
_Els10_27ipmInterfaceRtr_Type=Integer32
_Els10_27ipmInterfaceRtr_Object=MibScalar
els10_27ipmInterfaceRtr=_Els10_27ipmInterfaceRtr_Object((1,3,6,1,4,1,97,9,21,2),_Els10_27ipmInterfaceRtr_Type())
els10_27ipmInterfaceRtr.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27ipmInterfaceRtr.setStatus(_A)
_Els10_27voligmpgroup_ObjectIdentity=ObjectIdentity
els10_27voligmpgroup=_Els10_27voligmpgroup_ObjectIdentity((1,3,6,1,4,1,97,9,22))
class _Els10_27igmpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_Els10_27igmpStatus_Type.__name__=_E
_Els10_27igmpStatus_Object=MibScalar
els10_27igmpStatus=_Els10_27igmpStatus_Object((1,3,6,1,4,1,97,9,22,1),_Els10_27igmpStatus_Type())
els10_27igmpStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27igmpStatus.setStatus(_A)
class _Els10_27igmpQueryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_I,1)))
_Els10_27igmpQueryStatus_Type.__name__=_E
_Els10_27igmpQueryStatus_Object=MibScalar
els10_27igmpQueryStatus=_Els10_27igmpQueryStatus_Object((1,3,6,1,4,1,97,9,22,2),_Els10_27igmpQueryStatus_Type())
els10_27igmpQueryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27igmpQueryStatus.setStatus(_A)
_Els10_27igmpQueryCount_Type=Integer32
_Els10_27igmpQueryCount_Object=MibScalar
els10_27igmpQueryCount=_Els10_27igmpQueryCount_Object((1,3,6,1,4,1,97,9,22,3),_Els10_27igmpQueryCount_Type())
els10_27igmpQueryCount.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27igmpQueryCount.setStatus(_A)
_Els10_27igmpPortDelay_Type=Integer32
_Els10_27igmpPortDelay_Object=MibScalar
els10_27igmpPortDelay=_Els10_27igmpPortDelay_Object((1,3,6,1,4,1,97,9,22,4),_Els10_27igmpPortDelay_Type())
els10_27igmpPortDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27igmpPortDelay.setStatus(_A)
_Els10_27igmpCacheTable_Object=MibTable
els10_27igmpCacheTable=_Els10_27igmpCacheTable_Object((1,3,6,1,4,1,97,9,22,5))
if mibBuilder.loadTexts:els10_27igmpCacheTable.setStatus(_A)
_Els10_27igmpCacheEntry_Object=MibTableRow
els10_27igmpCacheEntry=_Els10_27igmpCacheEntry_Object((1,3,6,1,4,1,97,9,22,5,1))
els10_27igmpCacheEntry.setIndexNames((0,_D,_AA),(0,_D,_AB))
if mibBuilder.loadTexts:els10_27igmpCacheEntry.setStatus(_A)
_Els10_27igmpCacheAddress_Type=IpAddress
_Els10_27igmpCacheAddress_Object=MibTableColumn
els10_27igmpCacheAddress=_Els10_27igmpCacheAddress_Object((1,3,6,1,4,1,97,9,22,5,1,1),_Els10_27igmpCacheAddress_Type())
els10_27igmpCacheAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27igmpCacheAddress.setStatus(_A)
_Els10_27igmpCacheIfIndex_Type=Integer32
_Els10_27igmpCacheIfIndex_Object=MibTableColumn
els10_27igmpCacheIfIndex=_Els10_27igmpCacheIfIndex_Object((1,3,6,1,4,1,97,9,22,5,1,2),_Els10_27igmpCacheIfIndex_Type())
els10_27igmpCacheIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27igmpCacheIfIndex.setStatus(_A)
_Els10_27igmpCacheExpiryTime_Type=TimeTicks
_Els10_27igmpCacheExpiryTime_Object=MibTableColumn
els10_27igmpCacheExpiryTime=_Els10_27igmpCacheExpiryTime_Object((1,3,6,1,4,1,97,9,22,5,1,3),_Els10_27igmpCacheExpiryTime_Type())
els10_27igmpCacheExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27igmpCacheExpiryTime.setStatus(_A)
_Els10_27FlowControlCtl_ObjectIdentity=ObjectIdentity
els10_27FlowControlCtl=_Els10_27FlowControlCtl_ObjectIdentity((1,3,6,1,4,1,97,9,23))
_Els10_27FlowControlBackPressure_Type=Integer32
_Els10_27FlowControlBackPressure_Object=MibScalar
els10_27FlowControlBackPressure=_Els10_27FlowControlBackPressure_Object((1,3,6,1,4,1,97,9,23,1),_Els10_27FlowControlBackPressure_Type())
els10_27FlowControlBackPressure.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27FlowControlBackPressure.setStatus(_A)
_Els10_27FlowControlThresholdValue_Type=Integer32
_Els10_27FlowControlThresholdValue_Object=MibScalar
els10_27FlowControlThresholdValue=_Els10_27FlowControlThresholdValue_Object((1,3,6,1,4,1,97,9,23,2),_Els10_27FlowControlThresholdValue_Type())
els10_27FlowControlThresholdValue.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27FlowControlThresholdValue.setStatus(_A)
_Els10_27FlowControlPauseInteval_Type=Integer32
_Els10_27FlowControlPauseInteval_Object=MibScalar
els10_27FlowControlPauseInteval=_Els10_27FlowControlPauseInteval_Object((1,3,6,1,4,1,97,9,23,3),_Els10_27FlowControlPauseInteval_Type())
els10_27FlowControlPauseInteval.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27FlowControlPauseInteval.setStatus(_A)
_Els10_27FlowControlTable_Object=MibTable
els10_27FlowControlTable=_Els10_27FlowControlTable_Object((1,3,6,1,4,1,97,9,23,4))
if mibBuilder.loadTexts:els10_27FlowControlTable.setStatus(_A)
_Els10_27FlowControlEntry_Object=MibTableRow
els10_27FlowControlEntry=_Els10_27FlowControlEntry_Object((1,3,6,1,4,1,97,9,23,4,1))
els10_27FlowControlEntry.setIndexNames((0,_D,_AC))
if mibBuilder.loadTexts:els10_27FlowControlEntry.setStatus(_A)
_Els10_27FlowControlInterface_Type=Integer32
_Els10_27FlowControlInterface_Object=MibTableColumn
els10_27FlowControlInterface=_Els10_27FlowControlInterface_Object((1,3,6,1,4,1,97,9,23,4,1,1),_Els10_27FlowControlInterface_Type())
els10_27FlowControlInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27FlowControlInterface.setStatus(_A)
_Els10_27FlowControlEnable_Type=Integer32
_Els10_27FlowControlEnable_Object=MibTableColumn
els10_27FlowControlEnable=_Els10_27FlowControlEnable_Object((1,3,6,1,4,1,97,9,23,4,1,2),_Els10_27FlowControlEnable_Type())
els10_27FlowControlEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:els10_27FlowControlEnable.setStatus(_A)
_Els10_27FlowControlRxPauseFrames_Type=Integer32
_Els10_27FlowControlRxPauseFrames_Object=MibTableColumn
els10_27FlowControlRxPauseFrames=_Els10_27FlowControlRxPauseFrames_Object((1,3,6,1,4,1,97,9,23,4,1,3),_Els10_27FlowControlRxPauseFrames_Type())
els10_27FlowControlRxPauseFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27FlowControlRxPauseFrames.setStatus(_A)
_Els10_27FlowControlTxPauseFrames_Type=Integer32
_Els10_27FlowControlTxPauseFrames_Object=MibTableColumn
els10_27FlowControlTxPauseFrames=_Els10_27FlowControlTxPauseFrames_Object((1,3,6,1,4,1,97,9,23,4,1,4),_Els10_27FlowControlTxPauseFrames_Type())
els10_27FlowControlTxPauseFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:els10_27FlowControlTxPauseFrames.setStatus(_A)
els10_27WriteStatusTrap=NotificationType((1,3,6,1,2,1,1,2,0,2))
els10_27WriteStatusTrap.setObjects(*((_D,_F),(_D,_AD),(_D,_AE)))
if mibBuilder.loadTexts:els10_27WriteStatusTrap.setStatus('')
els10_27PortFunctionsTrap=NotificationType((1,3,6,1,2,1,1,2,0,3))
els10_27PortFunctionsTrap.setObjects(*((_D,_F),(_D,_AF)))
if mibBuilder.loadTexts:els10_27PortFunctionsTrap.setStatus('')
els10_27RxQueuesTrap=NotificationType((1,3,6,1,2,1,1,2,0,4))
els10_27RxQueuesTrap.setObjects(*((_D,_F),(_D,_AG)))
if mibBuilder.loadTexts:els10_27RxQueuesTrap.setStatus('')
els10_27RxStormFlagTrap=NotificationType((1,3,6,1,2,1,1,2,0,5))
els10_27RxStormFlagTrap.setObjects((_D,_F))
if mibBuilder.loadTexts:els10_27RxStormFlagTrap.setStatus('')
els10_27TxCongestsTrap=NotificationType((1,3,6,1,2,1,1,2,0,6))
els10_27TxCongestsTrap.setObjects(*((_D,_F),(_D,_AH)))
if mibBuilder.loadTexts:els10_27TxCongestsTrap.setStatus('')
els10_27DebugStringIdTrap=NotificationType((1,3,6,1,2,1,1,2,0,8))
els10_27DebugStringIdTrap.setObjects(*((_D,_F),(_D,_AI),(_D,_AJ)))
if mibBuilder.loadTexts:els10_27DebugStringIdTrap.setStatus('')
els10_27LpbkOperationTrap=NotificationType((1,3,6,1,2,1,1,2,0,9))
els10_27LpbkOperationTrap.setObjects(*((_D,_F),(_D,_AK),(_D,_AL),(_D,_AM)))
if mibBuilder.loadTexts:els10_27LpbkOperationTrap.setStatus('')
els10_27TrunkStateTrap=NotificationType((1,3,6,1,2,1,1,2,0,10))
els10_27TrunkStateTrap.setObjects(*((_D,_F),(_D,_AN)))
if mibBuilder.loadTexts:els10_27TrunkStateTrap.setStatus('')
els10_27TrunkBridgeAddrTrap=NotificationType((1,3,6,1,2,1,1,2,0,11))
els10_27TrunkBridgeAddrTrap.setObjects(*((_D,_F),(_D,_AO)))
if mibBuilder.loadTexts:els10_27TrunkBridgeAddrTrap.setStatus('')
els10_27TrunkIPAddrTrap=NotificationType((1,3,6,1,2,1,1,2,0,12))
els10_27TrunkIPAddrTrap.setObjects(*((_D,_F),(_D,_AP)))
if mibBuilder.loadTexts:els10_27TrunkIPAddrTrap.setStatus('')
els10_27TrunkErrorTrap=NotificationType((1,3,6,1,2,1,1,2,0,13))
els10_27TrunkErrorTrap.setObjects(*((_D,_F),(_D,_AQ)))
if mibBuilder.loadTexts:els10_27TrunkErrorTrap.setStatus('')
els10_27TrunkLinkOrdinalTrap=NotificationType((1,3,6,1,2,1,1,2,0,14))
els10_27TrunkLinkOrdinalTrap.setObjects(*((_D,_F),(_D,_AR)))
if mibBuilder.loadTexts:els10_27TrunkLinkOrdinalTrap.setStatus('')
els10_27TrunkLinkCountTrap=NotificationType((1,3,6,1,2,1,1,2,0,15))
els10_27TrunkLinkCountTrap.setObjects(*((_D,_F),(_D,_AS)))
if mibBuilder.loadTexts:els10_27TrunkLinkCountTrap.setStatus('')
els10_27DiagUnitBootedTrap=NotificationType((1,3,6,1,2,1,1,2,0,16))
els10_27DiagUnitBootedTrap.setObjects(*((_D,_F),(_D,_AT)))
if mibBuilder.loadTexts:els10_27DiagUnitBootedTrap.setStatus('')
els10_27StorageFailureTrap=NotificationType((1,3,6,1,2,1,1,2,0,17))
els10_27StorageFailureTrap.setObjects((_D,_F))
if mibBuilder.loadTexts:els10_27StorageFailureTrap.setStatus('')
els10_27PortCongestedTrap=NotificationType((1,3,6,1,2,1,1,2,0,18))
els10_27PortCongestedTrap.setObjects(*((_D,_F),(_M,_h)))
if mibBuilder.loadTexts:els10_27PortCongestedTrap.setStatus('')
els10_27TopChangeBegunTrap=NotificationType((1,3,6,1,2,1,1,2,0,19))
els10_27TopChangeBegunTrap.setObjects((_D,_F))
if mibBuilder.loadTexts:els10_27TopChangeBegunTrap.setStatus('')
els10_27TopChangeEndTrap=NotificationType((1,3,6,1,2,1,1,2,0,20))
els10_27TopChangeEndTrap.setObjects((_D,_F))
if mibBuilder.loadTexts:els10_27TopChangeEndTrap.setStatus('')
els10_27IfErrorsTrap=NotificationType((1,3,6,1,2,1,1,2,0,21))
els10_27IfErrorsTrap.setObjects(*((_D,_F),(_M,_g),(_M,_i)))
if mibBuilder.loadTexts:els10_27IfErrorsTrap.setStatus('')
els10_27StRootIDTrap=NotificationType((1,3,6,1,2,1,1,2,0,22))
els10_27StRootIDTrap.setObjects(*((_D,_F),(_G,_X)))
if mibBuilder.loadTexts:els10_27StRootIDTrap.setStatus('')
els10_27StRootCostTrap=NotificationType((1,3,6,1,2,1,1,2,0,23))
els10_27StRootCostTrap.setObjects(*((_D,_F),(_G,_e)))
if mibBuilder.loadTexts:els10_27StRootCostTrap.setStatus('')
els10_27StRootPortTrap=NotificationType((1,3,6,1,2,1,1,2,0,24))
els10_27StRootPortTrap.setObjects(*((_D,_F),(_G,_f)))
if mibBuilder.loadTexts:els10_27StRootPortTrap.setStatus('')
els10_27StMaxAgeTrap=NotificationType((1,3,6,1,2,1,1,2,0,25))
els10_27StMaxAgeTrap.setObjects(*((_D,_F),(_G,_a)))
if mibBuilder.loadTexts:els10_27StMaxAgeTrap.setStatus('')
els10_27StHelloTimeTrap=NotificationType((1,3,6,1,2,1,1,2,0,26))
els10_27StHelloTimeTrap.setObjects(*((_D,_F),(_G,_Z)))
if mibBuilder.loadTexts:els10_27StHelloTimeTrap.setStatus('')
els10_27StForwardDelayTrap=NotificationType((1,3,6,1,2,1,1,2,0,27))
els10_27StForwardDelayTrap.setObjects(*((_D,_F),(_G,_Y)))
if mibBuilder.loadTexts:els10_27StForwardDelayTrap.setStatus('')
els10_27StDesigRootTrap=NotificationType((1,3,6,1,2,1,1,2,0,28))
els10_27StDesigRootTrap.setObjects(*((_D,_F),(_G,_d)))
if mibBuilder.loadTexts:els10_27StDesigRootTrap.setStatus('')
els10_27StPortDesigBridgeTrap=NotificationType((1,3,6,1,2,1,1,2,0,29))
els10_27StPortDesigBridgeTrap.setObjects(*((_D,_F),(_G,_b)))
if mibBuilder.loadTexts:els10_27StPortDesigBridgeTrap.setStatus('')
els10_27StPortDesigCostTrap=NotificationType((1,3,6,1,2,1,1,2,0,30))
els10_27StPortDesigCostTrap.setObjects(*((_D,_F),(_G,_c)))
if mibBuilder.loadTexts:els10_27StPortDesigCostTrap.setStatus('')
els10_27StPortDesigPortTrap=NotificationType((1,3,6,1,2,1,1,2,0,31))
els10_27StPortDesigPortTrap.setObjects(*((_D,_F),(_G,_P)))
if mibBuilder.loadTexts:els10_27StPortDesigPortTrap.setStatus('')
els10_27StPortStateTrap=NotificationType((1,3,6,1,2,1,1,2,0,32))
els10_27StPortStateTrap.setObjects(*((_D,_F),(_G,_Q)))
if mibBuilder.loadTexts:els10_27StPortStateTrap.setStatus('')
els10_27InvalidConfigurationFileTrap=NotificationType((1,3,6,1,2,1,1,2,0,34))
els10_27InvalidConfigurationFileTrap.setObjects(*((_D,_F),(_G,_P)))
if mibBuilder.loadTexts:els10_27InvalidConfigurationFileTrap.setStatus('')
els10_27StInvalidFlashCodeImageTrap=NotificationType((1,3,6,1,2,1,1,2,0,35))
els10_27StInvalidFlashCodeImageTrap.setObjects(*((_D,_F),(_G,_Q)))
if mibBuilder.loadTexts:els10_27StInvalidFlashCodeImageTrap.setStatus('')
els10_27hwDiagTrap=NotificationType((1,3,6,1,2,1,1,2,0,100))
els10_27hwDiagTrap.setObjects(*((_D,_F),(_D,_AU)))
if mibBuilder.loadTexts:els10_27hwDiagTrap.setStatus('')
mibBuilder.exportSymbols(_D,**{'els10-27WriteStatusTrap':els10_27WriteStatusTrap,'els10-27PortFunctionsTrap':els10_27PortFunctionsTrap,'els10-27RxQueuesTrap':els10_27RxQueuesTrap,'els10-27RxStormFlagTrap':els10_27RxStormFlagTrap,'els10-27TxCongestsTrap':els10_27TxCongestsTrap,'els10-27DebugStringIdTrap':els10_27DebugStringIdTrap,'els10-27LpbkOperationTrap':els10_27LpbkOperationTrap,'els10-27TrunkStateTrap':els10_27TrunkStateTrap,'els10-27TrunkBridgeAddrTrap':els10_27TrunkBridgeAddrTrap,'els10-27TrunkIPAddrTrap':els10_27TrunkIPAddrTrap,'els10-27TrunkErrorTrap':els10_27TrunkErrorTrap,'els10-27TrunkLinkOrdinalTrap':els10_27TrunkLinkOrdinalTrap,'els10-27TrunkLinkCountTrap':els10_27TrunkLinkCountTrap,'els10-27DiagUnitBootedTrap':els10_27DiagUnitBootedTrap,'els10-27StorageFailureTrap':els10_27StorageFailureTrap,'els10-27PortCongestedTrap':els10_27PortCongestedTrap,'els10-27TopChangeBegunTrap':els10_27TopChangeBegunTrap,'els10-27TopChangeEndTrap':els10_27TopChangeEndTrap,'els10-27IfErrorsTrap':els10_27IfErrorsTrap,'els10-27StRootIDTrap':els10_27StRootIDTrap,'els10-27StRootCostTrap':els10_27StRootCostTrap,'els10-27StRootPortTrap':els10_27StRootPortTrap,'els10-27StMaxAgeTrap':els10_27StMaxAgeTrap,'els10-27StHelloTimeTrap':els10_27StHelloTimeTrap,'els10-27StForwardDelayTrap':els10_27StForwardDelayTrap,'els10-27StDesigRootTrap':els10_27StDesigRootTrap,'els10-27StPortDesigBridgeTrap':els10_27StPortDesigBridgeTrap,'els10-27StPortDesigCostTrap':els10_27StPortDesigCostTrap,'els10-27StPortDesigPortTrap':els10_27StPortDesigPortTrap,'els10-27StPortStateTrap':els10_27StPortStateTrap,'els10-27InvalidConfigurationFileTrap':els10_27InvalidConfigurationFileTrap,'els10-27StInvalidFlashCodeImageTrap':els10_27StInvalidFlashCodeImageTrap,'els10-27hwDiagTrap':els10_27hwDiagTrap,'sigma':sigma,'sys':sys,'sysID':sysID,'sysReset':sysReset,'sysTrapPort':sysTrapPort,'els10-27':els10_27,'els10-27hw':els10_27hw,_AU:els10_27hwDiagCode,'els10-27hwManufData':els10_27hwManufData,'els10-27hwPortCount':els10_27hwPortCount,'els10-27hwPortTable':els10_27hwPortTable,'els10-27hwPortEntry':els10_27hwPortEntry,_l:els10_27hwPortIndex,'els10-27hwPortType':els10_27hwPortType,'els10-27hwPortSubType':els10_27hwPortSubType,'els10-27hwPortDiagPassed':els10_27hwPortDiagPassed,'els10-27hwAddr':els10_27hwAddr,'els10-27hwUpLink':els10_27hwUpLink,'els10-27hwUpLinkManufData':els10_27hwUpLinkManufData,'els10-27sw':els10_27sw,'els10-27swNumber':els10_27swNumber,'els10-27swFilesetTable':els10_27swFilesetTable,'els10-27swFilesetEntry':els10_27swFilesetEntry,_m:els10_27swIndex,'els10-27swDesc':els10_27swDesc,'els10-27swCount':els10_27swCount,'els10-27swType':els10_27swType,'els10-27swSizes':els10_27swSizes,'els10-27swStarts':els10_27swStarts,'els10-27swBases':els10_27swBases,'els10-27swFlashBank':els10_27swFlashBank,'els10-27admin':els10_27admin,_AT:els10_27adminFatalErr,'els10-27adminAnyPass':els10_27adminAnyPass,'els10-27adminGetPass':els10_27adminGetPass,'els10-27adminNMSIPAddr':els10_27adminNMSIPAddr,'els10-27adminStorageFailure':els10_27adminStorageFailure,'els10-27adminAuthenticationFailure':els10_27adminAuthenticationFailure,_AH:els10_27adminNAMReceiveCongests,'els10-27adminArpEntries':els10_27adminArpEntries,'els10-27adminArpStatics':els10_27adminArpStatics,'els10-27adminArpOverflows':els10_27adminArpOverflows,'els10-27adminIpEntries':els10_27adminIpEntries,'els10-27adminIpStatics':els10_27adminIpStatics,'els10-27adminStaticPreference':els10_27adminStaticPreference,'els10-27adminRipPreference':els10_27adminRipPreference,'els10-27adminRipRouteDiscards':els10_27adminRipRouteDiscards,'els10-27adminRebootConfig':els10_27adminRebootConfig,'els10-27adminDisableButton':els10_27adminDisableButton,'els10-27adminButtonSelection':els10_27adminButtonSelection,'els10-27adminLEDProgramOption':els10_27adminLEDProgramOption,'els10-27swdis':els10_27swdis,_AE:els10_27swdisDesc,'els10-27swdisAccess':els10_27swdisAccess,_AD:els10_27swdisWriteStatus,'els10-27swdisConfigIp':els10_27swdisConfigIp,'els10-27swdisConfigRetryTime':els10_27swdisConfigRetryTime,'els10-27swdisConfigTotalTimeout':els10_27swdisConfigTotalTimeout,'els10-27addr':els10_27addr,'els10-27addrStatics':els10_27addrStatics,'els10-27addrDynamics':els10_27addrDynamics,'els10-27addrDynamicMax':els10_27addrDynamicMax,'els10-27addrDynamicOverflows':els10_27addrDynamicOverflows,'els10-27addrFlags':els10_27addrFlags,'els10-27addrMAC':els10_27addrMAC,'els10-27addrPort':els10_27addrPort,'els10-27addrOperation':els10_27addrOperation,'els10-27addrIndex':els10_27addrIndex,'els10-27addrNext':els10_27addrNext,'els10-27addrBlockSize':els10_27addrBlockSize,'els10-27addrBlock':els10_27addrBlock,'els10-27if':els10_27if,'els10-27ifTable':els10_27ifTable,'els10-27ifEntry':els10_27ifEntry,_n:els10_27ifIndex,'els10-27ifThreshold':els10_27ifThreshold,'els10-27ifThresholdTime':els10_27ifThresholdTime,'els10-27ifRxQueueThresh':els10_27ifRxQueueThresh,'els10-27ifRxQueueThreshTime':els10_27ifRxQueueThreshTime,'els10-27ifTxStormCnt':els10_27ifTxStormCnt,'els10-27ifTxStormTime':els10_27ifTxStormTime,_AF:els10_27ifFunction,'els10-27ifRxHwFCSs':els10_27ifRxHwFCSs,_AG:els10_27ifRxQueues,'els10-27ifStatisticsTime':els10_27ifStatisticsTime,'els10-27ifForwardedChars':els10_27ifForwardedChars,'els10-27ifDescr':els10_27ifDescr,'els10-27ifGoodRxFrames':els10_27ifGoodRxFrames,'els10-27ifGoodTxFrames':els10_27ifGoodTxFrames,'els10-27dot3':els10_27dot3,'els10-27dot3Table':els10_27dot3Table,'els10-27dot3Entry':els10_27dot3Entry,_o:els10_27dot3Index,'els10-27dot3TPLinkOK':els10_27dot3TPLinkOK,'els10-27dot3LedOn':els10_27dot3LedOn,'els10-27dot3RxCollisions':els10_27dot3RxCollisions,'els10-27dot3RxRunts':els10_27dot3RxRunts,'els10-27dot3RxLateColls':els10_27dot3RxLateColls,'els10-27dot3TxJabbers':els10_27dot3TxJabbers,'els10-27dot3TxBabbles':els10_27dot3TxBabbles,'els10-27dot3TxCollisions':els10_27dot3TxCollisions,'els10-27dot3SpeedSelection':els10_27dot3SpeedSelection,'els10-27dot3DuplexSelection':els10_27dot3DuplexSelection,'els10-27uart':els10_27uart,'els10-27uartTable':els10_27uartTable,'els10-27uartEntry':els10_27uartEntry,_p:els10_27uartIndex,'els10-27uartBaud':els10_27uartBaud,'els10-27uartAlignmentErrors':els10_27uartAlignmentErrors,'els10-27uartOverrunErrors':els10_27uartOverrunErrors,'els10-27debug':els10_27debug,_AI:els10_27debugStringID,_AJ:els10_27debugString,'els10-27debugTable':els10_27debugTable,'els10-27debugEntry':els10_27debugEntry,_q:els10_27debugIndex,'els10-27debugOperation':els10_27debugOperation,'els10-27debugBase':els10_27debugBase,'els10-27debugLength':els10_27debugLength,'els10-27debugData':els10_27debugData,'els10-27lpbk':els10_27lpbk,'els10-27lpbkTable':els10_27lpbkTable,'els10-27lpbkEntry':els10_27lpbkEntry,_r:els10_27lpbkIndex,_AK:els10_27lpbkOperation,'els10-27lpbkDestAddr':els10_27lpbkDestAddr,'els10-27lpbkPktNum':els10_27lpbkPktNum,'els10-27lpbkInterval':els10_27lpbkInterval,'els10-27lpbkPktLength':els10_27lpbkPktLength,'els10-27lpbkIncrements':els10_27lpbkIncrements,'els10-27lpbkGoods':els10_27lpbkGoods,_AL:els10_27lpbkErrorNoReceives,_AM:els10_27lpbkErrorBadReceives,'els10-27lpbkErrorSize':els10_27lpbkErrorSize,'els10-27lpbkErrorSent':els10_27lpbkErrorSent,'els10-27lpbkErrorReceived':els10_27lpbkErrorReceived,'els10-27lpbkErrorOffset':els10_27lpbkErrorOffset,'els10-27proto':els10_27proto,'els10-27protoTable':els10_27protoTable,'els10-27protoEntry':els10_27protoEntry,_s:els10_27protoIfIndex,'els10-27protoBridge':els10_27protoBridge,'els10-27protoSuppressBpdu':els10_27protoSuppressBpdu,'els10-27protoRipListen':els10_27protoRipListen,'els10-27protoTrunking':els10_27protoTrunking,'els10-27sprotoTransmitPacing':els10_27sprotoTransmitPacing,'els10-27trunk':els10_27trunk,'els10-27trunkTable':els10_27trunkTable,'els10-27trunkEntry':els10_27trunkEntry,_t:els10_27trunkIfIndex,_AN:els10_27trunkState,_AO:els10_27trunkRemoteBridgeAddr,_AP:els10_27trunkRemoteIp,_AQ:els10_27trunkLastError,_AR:els10_27trunkLinkOrdinal,_AS:els10_27trunkLinkCount,'els10-27trunkLastChange':els10_27trunkLastChange,'els10-27workgroup':els10_27workgroup,'els10-27WorkGroupNextNumber':els10_27WorkGroupNextNumber,'els10-27WorkGroupCurrentCount':els10_27WorkGroupCurrentCount,'els10-27WorkGroupMaxCount':els10_27WorkGroupMaxCount,'els10-27WorkGroupTable':els10_27WorkGroupTable,'els10-27WorkGroupEntry':els10_27WorkGroupEntry,_u:els10_27WorkGroupNumber,'els10-27WorkGroupName':els10_27WorkGroupName,'els10-27WorkGroupPorts':els10_27WorkGroupPorts,'els10-27WorkGroupType':els10_27WorkGroupType,'els10-27trapMgt':els10_27trapMgt,'els10-27trapControlTable':els10_27trapControlTable,'els10-27trapControlEntry':els10_27trapControlEntry,_v:els10_27trapIndex,'els10-27trapEnabled':els10_27trapEnabled,_F:els10_27trapSeverity,'els10-27trapText':els10_27trapText,'els10-27trapSeverityControlTable':els10_27trapSeverityControlTable,'els10-27trapSeverityControlEntry':els10_27trapSeverityControlEntry,'els10-27trapSeverityControlSeverity':els10_27trapSeverityControlSeverity,'els10-27trapSeverityEnable':els10_27trapSeverityEnable,'els10-27trapIncludeText':els10_27trapIncludeText,'els10-27trapTime':els10_27trapTime,'els10-27trapRetry':els10_27trapRetry,'els10-27trapNumber':els10_27trapNumber,'els10-27trapTable':els10_27trapTable,'els10-27trapEntry':els10_27trapEntry,_w:els10_27trapEntryIndex,'els10-27trapEntryTimeStamp':els10_27trapEntryTimeStamp,'els10-27trapEntryText':els10_27trapEntryText,'els10-27trapEntryNumber':els10_27trapEntryNumber,'els10-27trapEntrySeverity':els10_27trapEntrySeverity,'els10-27pingMgt':els10_27pingMgt,'els10-27pingDataTimeout':els10_27pingDataTimeout,'els10-27pingTable':els10_27pingTable,'els10-27pingEntry':els10_27pingEntry,_x:els10_27pingNMSAddr,_y:els10_27pingDestAddr,'els10-27pingState':els10_27pingState,'els10-27pingCount':els10_27pingCount,'els10-27pingDataSize':els10_27pingDataSize,'els10-27pingWait':els10_27pingWait,'els10-27pingTimeOut':els10_27pingTimeOut,'els10-27pingOperation':els10_27pingOperation,'els10-27pingMin':els10_27pingMin,'els10-27pingMax':els10_27pingMax,'els10-27pingAvg':els10_27pingAvg,'els10-27pingNumTransmitted':els10_27pingNumTransmitted,'els10-27pingNumReceived':els10_27pingNumReceived,'els10-27traceMgt':els10_27traceMgt,'els10-27traceDataTimeout':els10_27traceDataTimeout,'els10-27traceTable':els10_27traceTable,'els10-27traceEntry':els10_27traceEntry,_A1:els10_27traceNMSAddr,_A2:els10_27traceDestAddr,'els10-27traceMaxTTL':els10_27traceMaxTTL,'els10-27traceDataSize':els10_27traceDataSize,'els10-27traceNumProbes':els10_27traceNumProbes,'els10-27traceWait':els10_27traceWait,'els10-27traceOperation':els10_27traceOperation,_A3:els10_27traceHop,'els10-27traceHopAddr':els10_27traceHopAddr,_A4:els10_27traceProbe,'els10-27traceState':els10_27traceState,'els10-27traceTime':els10_27traceTime,'els10-27volmirrorgroup':els10_27volmirrorgroup,'els10-27volmirrorMode':els10_27volmirrorMode,'els10-27volmirrorPort':els10_27volmirrorPort,'els10-27volmonitorPort':els10_27volmonitorPort,'els10-27volMirrorMacTable':els10_27volMirrorMacTable,'els10-27volmirrorMacEntry':els10_27volmirrorMacEntry,_A5:els10_27volmirrorIndex,'els10-27volmirrorMac1':els10_27volmirrorMac1,'els10-27VlanBridgeConfig':els10_27VlanBridgeConfig,'els10-27VlanVersionNumber':els10_27VlanVersionNumber,'els10-27VlanOperatingMode':els10_27VlanOperatingMode,'els10-27VlanResetDefaults':els10_27VlanResetDefaults,'els10-27VlanGVRPEnable':els10_27VlanGVRPEnable,'els10-27VlanAccessList':els10_27VlanAccessList,'els10-27VlanConfigVlan':els10_27VlanConfigVlan,'els10-27VlanNumActiveEntries':els10_27VlanNumActiveEntries,'els10-27VlanNumConfiguredEntries':els10_27VlanNumConfiguredEntries,'els10-27VlanMaxNumEntries':els10_27VlanMaxNumEntries,'els10-27VlanConfigTable':els10_27VlanConfigTable,'els10-27VlanConfigEntry':els10_27VlanConfigEntry,'els10-27VlanConfigIndex':els10_27VlanConfigIndex,_A6:els10_27VlanConfigVID,'els10-27VlanConfigPorts':els10_27VlanConfigPorts,'els10-27VlanConfigIP':els10_27VlanConfigIP,'els10-27VlanConfigIPMask':els10_27VlanConfigIPMask,'els10-27VlanConfigName':els10_27VlanConfigName,'els10-27VlanConfigStatus':els10_27VlanConfigStatus,'els10-27VlanConfigEstablish':els10_27VlanConfigEstablish,'els10-27VlanConfigEgressTable':els10_27VlanConfigEgressTable,'els10-27VlanConfigEgressEntry':els10_27VlanConfigEgressEntry,'els10-27VlanEgressIndex':els10_27VlanEgressIndex,_A7:els10_27VlanEgressVID,'els10-27VlanEgressList':els10_27VlanEgressList,'els10-27VlanEgressStatus':els10_27VlanEgressStatus,'els10-27VlanFilterGVRPTable':els10_27VlanFilterGVRPTable,'els10-27VlanFilterGVRPEntry':els10_27VlanFilterGVRPEntry,'els10-27VlanFilterGVRPIndex':els10_27VlanFilterGVRPIndex,_A8:els10_27VlanFilterGVRPVID,'els10-27VlanFilterGVRPList':els10_27VlanFilterGVRPList,'els10-27VlanFilterGVRPStatus':els10_27VlanFilterGVRPStatus,'els10-27VlanFilterGVRPEstablishVID':els10_27VlanFilterGVRPEstablishVID,'els10-27VlanStaticTable':els10_27VlanStaticTable,'els10-27VlanStaticEntry':els10_27VlanStaticEntry,_A9:els10_27VlanStaticVID,'els10-27VlanStaticMAC':els10_27VlanStaticMAC,'els10-27VlanStaticPort':els10_27VlanStaticPort,'els10-27VlanStaticEstablish':els10_27VlanStaticEstablish,'els10-27volipmgroup':els10_27volipmgroup,'els10-27IPMulticastStatus':els10_27IPMulticastStatus,'els10-27ipmInterfaceRtr':els10_27ipmInterfaceRtr,'els10-27voligmpgroup':els10_27voligmpgroup,'els10-27igmpStatus':els10_27igmpStatus,'els10-27igmpQueryStatus':els10_27igmpQueryStatus,'els10-27igmpQueryCount':els10_27igmpQueryCount,'els10-27igmpPortDelay':els10_27igmpPortDelay,'els10-27igmpCacheTable':els10_27igmpCacheTable,'els10-27igmpCacheEntry':els10_27igmpCacheEntry,_AA:els10_27igmpCacheAddress,_AB:els10_27igmpCacheIfIndex,'els10-27igmpCacheExpiryTime':els10_27igmpCacheExpiryTime,'els10-27FlowControlCtl':els10_27FlowControlCtl,'els10-27FlowControlBackPressure':els10_27FlowControlBackPressure,'els10-27FlowControlThresholdValue':els10_27FlowControlThresholdValue,'els10-27FlowControlPauseInteval':els10_27FlowControlPauseInteval,'els10-27FlowControlTable':els10_27FlowControlTable,'els10-27FlowControlEntry':els10_27FlowControlEntry,_AC:els10_27FlowControlInterface,'els10-27FlowControlEnable':els10_27FlowControlEnable,'els10-27FlowControlRxPauseFrames':els10_27FlowControlRxPauseFrames,'els10-27FlowControlTxPauseFrames':els10_27FlowControlTxPauseFrames})