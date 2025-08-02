_v='frCLLMDlciList'
_u='frCLLMCauseCode'
_t='frCLLMStatsDlci'
_s='frCLLMStatsIfIndex'
_r='ibmdlswQllcLsQaddress'
_q='ibmdlswQllcLsQdomain'
_p='ibmdlswQllcLsIfIndex'
_o='ibmdlswTConnGroupOperIndex'
_n='pppMPPEIfIndex'
_m='pppEAPIfIndex'
_l='pppCBCPIfIndex'
_k='pppMSCHAPIfIndex'
_j='pppEPIfIndex'
_i='pppCPIfIndex'
_h='pppBAPIfIndex'
_g='pppSPAPIfIndex'
_f='pppCHAPIfIndex'
_e='pppPAPIfIndex'
_d='pppLCProtoIfIndex'
_c='pppLinkErrIfIndex'
_b='pppProtocolId'
_a='pppProtocolIfIndex'
_Z='ibmSysDumpIndex'
_Y='NotificationType'
_X='proResMemHeapTotal'
_W='proResMemHeapNeverAlloc'
_V='proElsSubSysEventMsg'
_U='disabled'
_T='enabled'
_S='frCLLMCauseIfIndex'
_R='DisplayString'
_Q='frCircuitIfIndex'
_P='frCircuitDlci'
_O='termSent'
_N='opened'
_M='ackSent'
_L='ackReceived'
_K='requestSent'
_J='listen'
_I='closed'
_H='PROTEON-MIB'
_G='read-write'
_F='RFC1315-MIB'
_E='OctetString'
_D='IBMIROC-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
proElsSubSysEventMsg,proResMemHeapNeverAlloc,proResMemHeapTotal=mibBuilder.importSymbols(_H,_V,_W,_X)
frCircuitDlci,frCircuitIfIndex=mibBuilder.importSymbols(_F,_P,_Q)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_Y,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_Y,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_R,'PhysAddress','TextualConvention')
class MacAddressNCIROC(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_Ibm_ObjectIdentity=ObjectIdentity
ibm=_Ibm_ObjectIdentity((1,3,6,1,4,1,2))
_IbmProd_ObjectIdentity=ObjectIdentity
ibmProd=_IbmProd_ObjectIdentity((1,3,6,1,4,1,2,6))
_IbmIROC_ObjectIdentity=ObjectIdentity
ibmIROC=_IbmIROC_ObjectIdentity((1,3,6,1,4,1,2,6,119))
_IbmIROCadmin_ObjectIdentity=ObjectIdentity
ibmIROCadmin=_IbmIROCadmin_ObjectIdentity((1,3,6,1,4,1,2,6,119,1))
_IbmIROCadminproducts_ObjectIdentity=ObjectIdentity
ibmIROCadminproducts=_IbmIROCadminproducts_ObjectIdentity((1,3,6,1,4,1,2,6,119,1,1))
_IbmIROCadminOID_ObjectIdentity=ObjectIdentity
ibmIROCadminOID=_IbmIROCadminOID_ObjectIdentity((1,3,6,1,4,1,2,6,119,1,2))
_IbmIROCadminDebug_ObjectIdentity=ObjectIdentity
ibmIROCadminDebug=_IbmIROCadminDebug_ObjectIdentity((1,3,6,1,4,1,2,6,119,1,3))
_IbmIROCAgentDebug_ObjectIdentity=ObjectIdentity
ibmIROCAgentDebug=_IbmIROCAgentDebug_ObjectIdentity((1,3,6,1,4,1,2,6,119,1,3,1))
_AgentMemUse_Type=Gauge32
_AgentMemUse_Object=MibScalar
agentMemUse=_AgentMemUse_Object((1,3,6,1,4,1,2,6,119,1,3,1,1),_AgentMemUse_Type())
agentMemUse.setMaxAccess(_B)
if mibBuilder.loadTexts:agentMemUse.setStatus(_A)
_IbmIROCadminSnmp_ObjectIdentity=ObjectIdentity
ibmIROCadminSnmp=_IbmIROCadminSnmp_ObjectIdentity((1,3,6,1,4,1,2,6,119,1,4))
_IbmIROCSnmpAuthFail_ObjectIdentity=ObjectIdentity
ibmIROCSnmpAuthFail=_IbmIROCSnmpAuthFail_ObjectIdentity((1,3,6,1,4,1,2,6,119,1,4,1))
_AuthTrapSourceIPAddr_Type=IpAddress
_AuthTrapSourceIPAddr_Object=MibScalar
authTrapSourceIPAddr=_AuthTrapSourceIPAddr_Object((1,3,6,1,4,1,2,6,119,1,4,1,1),_AuthTrapSourceIPAddr_Type())
authTrapSourceIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:authTrapSourceIPAddr.setStatus(_A)
_IbmIROCsystem_ObjectIdentity=ObjectIdentity
ibmIROCsystem=_IbmIROCsystem_ObjectIdentity((1,3,6,1,4,1,2,6,119,2))
_IbmIROCsystemInfo_ObjectIdentity=ObjectIdentity
ibmIROCsystemInfo=_IbmIROCsystemInfo_ObjectIdentity((1,3,6,1,4,1,2,6,119,2,1))
_IbmIROCcfgInfo_ObjectIdentity=ObjectIdentity
ibmIROCcfgInfo=_IbmIROCcfgInfo_ObjectIdentity((1,3,6,1,4,1,2,6,119,2,2))
_IbmIROCdumpInfo_ObjectIdentity=ObjectIdentity
ibmIROCdumpInfo=_IbmIROCdumpInfo_ObjectIdentity((1,3,6,1,4,1,2,6,119,2,4))
_IbmSysDumpTable_Object=MibTable
ibmSysDumpTable=_IbmSysDumpTable_Object((1,3,6,1,4,1,2,6,119,2,4,1))
if mibBuilder.loadTexts:ibmSysDumpTable.setStatus(_A)
_IbmSysDumpEntry_Object=MibTableRow
ibmSysDumpEntry=_IbmSysDumpEntry_Object((1,3,6,1,4,1,2,6,119,2,4,1,1))
ibmSysDumpEntry.setIndexNames((0,_D,_Z))
if mibBuilder.loadTexts:ibmSysDumpEntry.setStatus(_A)
_IbmSysDumpIndex_Type=Integer32
_IbmSysDumpIndex_Object=MibTableColumn
ibmSysDumpIndex=_IbmSysDumpIndex_Object((1,3,6,1,4,1,2,6,119,2,4,1,1,1),_IbmSysDumpIndex_Type())
ibmSysDumpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmSysDumpIndex.setStatus(_A)
_IbmSysDumpFileName_Type=DisplayString
_IbmSysDumpFileName_Object=MibTableColumn
ibmSysDumpFileName=_IbmSysDumpFileName_Object((1,3,6,1,4,1,2,6,119,2,4,1,1,2),_IbmSysDumpFileName_Type())
ibmSysDumpFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmSysDumpFileName.setStatus(_A)
_IbmSysDumpFileDate_Type=DisplayString
_IbmSysDumpFileDate_Object=MibTableColumn
ibmSysDumpFileDate=_IbmSysDumpFileDate_Object((1,3,6,1,4,1,2,6,119,2,4,1,1,3),_IbmSysDumpFileDate_Type())
ibmSysDumpFileDate.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmSysDumpFileDate.setStatus(_A)
_IbmSysDumpBuild_Type=DisplayString
_IbmSysDumpBuild_Object=MibTableColumn
ibmSysDumpBuild=_IbmSysDumpBuild_Object((1,3,6,1,4,1,2,6,119,2,4,1,1,4),_IbmSysDumpBuild_Type())
ibmSysDumpBuild.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmSysDumpBuild.setStatus(_A)
_IbmSysDumpBuilder_Type=DisplayString
_IbmSysDumpBuilder_Object=MibTableColumn
ibmSysDumpBuilder=_IbmSysDumpBuilder_Object((1,3,6,1,4,1,2,6,119,2,4,1,1,5),_IbmSysDumpBuilder_Type())
ibmSysDumpBuilder.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmSysDumpBuilder.setStatus(_A)
_IbmSysDumpBuildName_Type=DisplayString
_IbmSysDumpBuildName_Object=MibTableColumn
ibmSysDumpBuildName=_IbmSysDumpBuildName_Object((1,3,6,1,4,1,2,6,119,2,4,1,1,6),_IbmSysDumpBuildName_Type())
ibmSysDumpBuildName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmSysDumpBuildName.setStatus(_A)
_IbmSysDumpRetainName_Type=DisplayString
_IbmSysDumpRetainName_Object=MibTableColumn
ibmSysDumpRetainName=_IbmSysDumpRetainName_Object((1,3,6,1,4,1,2,6,119,2,4,1,1,7),_IbmSysDumpRetainName_Type())
ibmSysDumpRetainName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmSysDumpRetainName.setStatus(_A)
_IbmSysDumpProductNumber_Type=DisplayString
_IbmSysDumpProductNumber_Object=MibTableColumn
ibmSysDumpProductNumber=_IbmSysDumpProductNumber_Object((1,3,6,1,4,1,2,6,119,2,4,1,1,8),_IbmSysDumpProductNumber_Type())
ibmSysDumpProductNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmSysDumpProductNumber.setStatus(_A)
_IbmSysDumpBuildDate_Type=DisplayString
_IbmSysDumpBuildDate_Object=MibTableColumn
ibmSysDumpBuildDate=_IbmSysDumpBuildDate_Object((1,3,6,1,4,1,2,6,119,2,4,1,1,9),_IbmSysDumpBuildDate_Type())
ibmSysDumpBuildDate.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmSysDumpBuildDate.setStatus(_A)
_IbmSysDumpFatalMsg1_Type=DisplayString
_IbmSysDumpFatalMsg1_Object=MibTableColumn
ibmSysDumpFatalMsg1=_IbmSysDumpFatalMsg1_Object((1,3,6,1,4,1,2,6,119,2,4,1,1,10),_IbmSysDumpFatalMsg1_Type())
ibmSysDumpFatalMsg1.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmSysDumpFatalMsg1.setStatus(_A)
_IbmSysDumpFatalMsg2_Type=DisplayString
_IbmSysDumpFatalMsg2_Object=MibTableColumn
ibmSysDumpFatalMsg2=_IbmSysDumpFatalMsg2_Object((1,3,6,1,4,1,2,6,119,2,4,1,1,11),_IbmSysDumpFatalMsg2_Type())
ibmSysDumpFatalMsg2.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmSysDumpFatalMsg2.setStatus(_A)
_IbmSysDumpFatalMsg3_Type=DisplayString
_IbmSysDumpFatalMsg3_Object=MibTableColumn
ibmSysDumpFatalMsg3=_IbmSysDumpFatalMsg3_Object((1,3,6,1,4,1,2,6,119,2,4,1,1,12),_IbmSysDumpFatalMsg3_Type())
ibmSysDumpFatalMsg3.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmSysDumpFatalMsg3.setStatus(_A)
_IbmSysDumpFatalMsg4_Type=DisplayString
_IbmSysDumpFatalMsg4_Object=MibTableColumn
ibmSysDumpFatalMsg4=_IbmSysDumpFatalMsg4_Object((1,3,6,1,4,1,2,6,119,2,4,1,1,13),_IbmSysDumpFatalMsg4_Type())
ibmSysDumpFatalMsg4.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmSysDumpFatalMsg4.setStatus(_A)
_IbmSysDumpFatalMsg5_Type=DisplayString
_IbmSysDumpFatalMsg5_Object=MibTableColumn
ibmSysDumpFatalMsg5=_IbmSysDumpFatalMsg5_Object((1,3,6,1,4,1,2,6,119,2,4,1,1,14),_IbmSysDumpFatalMsg5_Type())
ibmSysDumpFatalMsg5.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmSysDumpFatalMsg5.setStatus(_A)
_IbmSysDumpRemoteIPAddr_Type=DisplayString
_IbmSysDumpRemoteIPAddr_Object=MibTableColumn
ibmSysDumpRemoteIPAddr=_IbmSysDumpRemoteIPAddr_Object((1,3,6,1,4,1,2,6,119,2,4,1,1,15),_IbmSysDumpRemoteIPAddr_Type())
ibmSysDumpRemoteIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmSysDumpRemoteIPAddr.setStatus(_A)
_IbmSysDumpRemotePath_Type=DisplayString
_IbmSysDumpRemotePath_Object=MibTableColumn
ibmSysDumpRemotePath=_IbmSysDumpRemotePath_Object((1,3,6,1,4,1,2,6,119,2,4,1,1,16),_IbmSysDumpRemotePath_Type())
ibmSysDumpRemotePath.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmSysDumpRemotePath.setStatus(_A)
_IbmIROChardware_ObjectIdentity=ObjectIdentity
ibmIROChardware=_IbmIROChardware_ObjectIdentity((1,3,6,1,4,1,2,6,119,3))
_IbmIROChardwareInfo_ObjectIdentity=ObjectIdentity
ibmIROChardwareInfo=_IbmIROChardwareInfo_ObjectIdentity((1,3,6,1,4,1,2,6,119,3,1))
class _PlatformType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42)));namedValues=NamedValues(*(('plat-other',1),('plat-mss-8210',2),('plat-mss-blade',3),('plat-mss-client',4),('plat-2216-400',5),('plat-2210-1s4',6),('plat-2210-1s8',7),('plat-2210-1u4',8),('plat-2210-1u8',9),('plat-2210-24e',10),('plat-2210-24m',11),('plat-2210-24t',12),('plat-2210-14t',13),('plat-2210-125',14),('plat-2210-127',15),('plat-2210-121',16),('plat-2210-12t',17),('plat-2210-126',18),('plat-2210-128',19),('plat-2210-122',20),('plat-2210-12e',21),('plat-2220-200',22),('plat-3746-MAE',23),('plat-mss-domain-client',24),('plat-mss-8210V2',25),('plat-mss-bladeV2',26),('plat-netu-xx1',27),('plat-2212-10F',28),('plat-2212-10H',29),('plat-2212-40F',30),('plat-2212-40H',31),('plat-8371',32),('plat-8375',33),('plat-2212-15F',34),('plat-2212-15H',35),('plat-2212-45F',36),('plat-2212-45H',37),('plat-reserved1',38),('plat-reserved2',39),('plat-8275-RR',40),('plat-8371-8260B',41),('plat-reserved',42)))
_PlatformType_Type.__name__=_C
_PlatformType_Object=MibScalar
platformType=_PlatformType_Object((1,3,6,1,4,1,2,6,119,3,1,1),_PlatformType_Type())
platformType.setMaxAccess(_B)
if mibBuilder.loadTexts:platformType.setStatus(_A)
_PlatformDRAMSize_Type=Integer32
_PlatformDRAMSize_Object=MibScalar
platformDRAMSize=_PlatformDRAMSize_Object((1,3,6,1,4,1,2,6,119,3,1,2),_PlatformDRAMSize_Type())
platformDRAMSize.setMaxAccess(_B)
if mibBuilder.loadTexts:platformDRAMSize.setStatus(_A)
_PlatformFLASHSize_Type=Integer32
_PlatformFLASHSize_Object=MibScalar
platformFLASHSize=_PlatformFLASHSize_Object((1,3,6,1,4,1,2,6,119,3,1,3),_PlatformFLASHSize_Type())
platformFLASHSize.setMaxAccess(_B)
if mibBuilder.loadTexts:platformFLASHSize.setStatus(_A)
_PlatformNVRAMSize_Type=Integer32
_PlatformNVRAMSize_Object=MibScalar
platformNVRAMSize=_PlatformNVRAMSize_Object((1,3,6,1,4,1,2,6,119,3,1,4),_PlatformNVRAMSize_Type())
platformNVRAMSize.setMaxAccess(_B)
if mibBuilder.loadTexts:platformNVRAMSize.setStatus(_A)
class _PlatformFeatureSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)));namedValues=NamedValues(*(('none',1),('isdn-BRI-ST',2),('isdn-PRI-E1-120',3),('isdn-PRI-E1-75',4),('isdn-PRI-T1J1',5),('atm-155',6),('atm-25',7),('serial-wan-4port',8),('serial-wan-8port',9),('modem-4port',10),('modem-8port',11),('isdn-BRI-4port-ST',12),('isdn-BRI-4port-U',13),('isdn-voice-ST-FXO',14),('isdn-voice-ST-FXS',15),('isdn-voice-ST-EM',16),('isdn-voice-U-FXO',17),('isdn-voice-U-FXS',18),('isdn-voice-U-EM',19)))
_PlatformFeatureSlot_Type.__name__=_C
_PlatformFeatureSlot_Object=MibScalar
platformFeatureSlot=_PlatformFeatureSlot_Object((1,3,6,1,4,1,2,6,119,3,1,5),_PlatformFeatureSlot_Type())
platformFeatureSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:platformFeatureSlot.setStatus(_A)
_IbmIROCrouting_ObjectIdentity=ObjectIdentity
ibmIROCrouting=_IbmIROCrouting_ObjectIdentity((1,3,6,1,4,1,2,6,119,4))
_IbmIROCroutingppp_ObjectIdentity=ObjectIdentity
ibmIROCroutingppp=_IbmIROCroutingppp_ObjectIdentity((1,3,6,1,4,1,2,6,119,4,2))
_PppProtocolTable_Object=MibTable
pppProtocolTable=_PppProtocolTable_Object((1,3,6,1,4,1,2,6,119,4,2,1))
if mibBuilder.loadTexts:pppProtocolTable.setStatus(_A)
_PppProtocolEntry_Object=MibTableRow
pppProtocolEntry=_PppProtocolEntry_Object((1,3,6,1,4,1,2,6,119,4,2,1,1))
pppProtocolEntry.setIndexNames((0,_D,_a),(0,_D,_b))
if mibBuilder.loadTexts:pppProtocolEntry.setStatus(_A)
class _PppProtocolIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PppProtocolIfIndex_Type.__name__=_C
_PppProtocolIfIndex_Object=MibTableColumn
pppProtocolIfIndex=_PppProtocolIfIndex_Object((1,3,6,1,4,1,2,6,119,4,2,1,1,1),_PppProtocolIfIndex_Type())
pppProtocolIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pppProtocolIfIndex.setStatus(_A)
class _PppProtocolId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('ip',1),('decnet',2),('ipx',3),('bridge',4),('appletalk',5),('osi',6),('appnhpr',7),('appnisr',8),('vines',9),('compression',10),('netbios',11),('netbios-forw',12),('bandwidth-allocation',13),('encryption',14),('ipv6',15)))
_PppProtocolId_Type.__name__=_C
_PppProtocolId_Object=MibTableColumn
pppProtocolId=_PppProtocolId_Object((1,3,6,1,4,1,2,6,119,4,2,1,1,2),_PppProtocolId_Type())
pppProtocolId.setMaxAccess(_B)
if mibBuilder.loadTexts:pppProtocolId.setStatus(_A)
class _PppProtocolRegistered_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_PppProtocolRegistered_Type.__name__=_C
_PppProtocolRegistered_Object=MibTableColumn
pppProtocolRegistered=_PppProtocolRegistered_Object((1,3,6,1,4,1,2,6,119,4,2,1,1,3),_PppProtocolRegistered_Type())
pppProtocolRegistered.setMaxAccess(_B)
if mibBuilder.loadTexts:pppProtocolRegistered.setStatus(_A)
class _PppProtocolState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_L,4),(_M,5),(_N,6),(_O,7)))
_PppProtocolState_Type.__name__=_C
_PppProtocolState_Object=MibTableColumn
pppProtocolState=_PppProtocolState_Object((1,3,6,1,4,1,2,6,119,4,2,1,1,4),_PppProtocolState_Type())
pppProtocolState.setMaxAccess(_B)
if mibBuilder.loadTexts:pppProtocolState.setStatus(_A)
class _PppProtocolPreviousState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_L,4),(_M,5),(_N,6),(_O,7)))
_PppProtocolPreviousState_Type.__name__=_C
_PppProtocolPreviousState_Object=MibTableColumn
pppProtocolPreviousState=_PppProtocolPreviousState_Object((1,3,6,1,4,1,2,6,119,4,2,1,1,5),_PppProtocolPreviousState_Type())
pppProtocolPreviousState.setMaxAccess(_B)
if mibBuilder.loadTexts:pppProtocolPreviousState.setStatus(_A)
_PppProtocolLastTimeChange_Type=TimeTicks
_PppProtocolLastTimeChange_Object=MibTableColumn
pppProtocolLastTimeChange=_PppProtocolLastTimeChange_Object((1,3,6,1,4,1,2,6,119,4,2,1,1,6),_PppProtocolLastTimeChange_Type())
pppProtocolLastTimeChange.setMaxAccess(_B)
if mibBuilder.loadTexts:pppProtocolLastTimeChange.setStatus(_A)
_PppProtocolCtlInRejects_Type=Counter32
_PppProtocolCtlInRejects_Object=MibTableColumn
pppProtocolCtlInRejects=_PppProtocolCtlInRejects_Object((1,3,6,1,4,1,2,6,119,4,2,1,1,7),_PppProtocolCtlInRejects_Type())
pppProtocolCtlInRejects.setMaxAccess(_B)
if mibBuilder.loadTexts:pppProtocolCtlInRejects.setStatus(_A)
_PppProtocolCtlInOctets_Type=Counter32
_PppProtocolCtlInOctets_Object=MibTableColumn
pppProtocolCtlInOctets=_PppProtocolCtlInOctets_Object((1,3,6,1,4,1,2,6,119,4,2,1,1,8),_PppProtocolCtlInOctets_Type())
pppProtocolCtlInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppProtocolCtlInOctets.setStatus(_A)
_PppProtocolCtlInPkts_Type=Counter32
_PppProtocolCtlInPkts_Object=MibTableColumn
pppProtocolCtlInPkts=_PppProtocolCtlInPkts_Object((1,3,6,1,4,1,2,6,119,4,2,1,1,9),_PppProtocolCtlInPkts_Type())
pppProtocolCtlInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:pppProtocolCtlInPkts.setStatus(_A)
_PppProtocolCtlOutOctets_Type=Counter32
_PppProtocolCtlOutOctets_Object=MibTableColumn
pppProtocolCtlOutOctets=_PppProtocolCtlOutOctets_Object((1,3,6,1,4,1,2,6,119,4,2,1,1,10),_PppProtocolCtlOutOctets_Type())
pppProtocolCtlOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppProtocolCtlOutOctets.setStatus(_A)
_PppProtocolCtlOutPkts_Type=Counter32
_PppProtocolCtlOutPkts_Object=MibTableColumn
pppProtocolCtlOutPkts=_PppProtocolCtlOutPkts_Object((1,3,6,1,4,1,2,6,119,4,2,1,1,11),_PppProtocolCtlOutPkts_Type())
pppProtocolCtlOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:pppProtocolCtlOutPkts.setStatus(_A)
_PppProtocolDataInRejects_Type=Counter32
_PppProtocolDataInRejects_Object=MibTableColumn
pppProtocolDataInRejects=_PppProtocolDataInRejects_Object((1,3,6,1,4,1,2,6,119,4,2,1,1,12),_PppProtocolDataInRejects_Type())
pppProtocolDataInRejects.setMaxAccess(_B)
if mibBuilder.loadTexts:pppProtocolDataInRejects.setStatus(_A)
_PppProtocolDataInOctets_Type=Counter32
_PppProtocolDataInOctets_Object=MibTableColumn
pppProtocolDataInOctets=_PppProtocolDataInOctets_Object((1,3,6,1,4,1,2,6,119,4,2,1,1,13),_PppProtocolDataInOctets_Type())
pppProtocolDataInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppProtocolDataInOctets.setStatus(_A)
_PppProtocolDataInPkts_Type=Counter32
_PppProtocolDataInPkts_Object=MibTableColumn
pppProtocolDataInPkts=_PppProtocolDataInPkts_Object((1,3,6,1,4,1,2,6,119,4,2,1,1,14),_PppProtocolDataInPkts_Type())
pppProtocolDataInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:pppProtocolDataInPkts.setStatus(_A)
_PppProtocolDataOutOctets_Type=Counter32
_PppProtocolDataOutOctets_Object=MibTableColumn
pppProtocolDataOutOctets=_PppProtocolDataOutOctets_Object((1,3,6,1,4,1,2,6,119,4,2,1,1,15),_PppProtocolDataOutOctets_Type())
pppProtocolDataOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppProtocolDataOutOctets.setStatus(_A)
_PppProtocolDataOutPkts_Type=Counter32
_PppProtocolDataOutPkts_Object=MibTableColumn
pppProtocolDataOutPkts=_PppProtocolDataOutPkts_Object((1,3,6,1,4,1,2,6,119,4,2,1,1,16),_PppProtocolDataOutPkts_Type())
pppProtocolDataOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:pppProtocolDataOutPkts.setStatus(_A)
_PppLinkErrTable_Object=MibTable
pppLinkErrTable=_PppLinkErrTable_Object((1,3,6,1,4,1,2,6,119,4,2,2))
if mibBuilder.loadTexts:pppLinkErrTable.setStatus(_A)
_PppLinkErrEntry_Object=MibTableRow
pppLinkErrEntry=_PppLinkErrEntry_Object((1,3,6,1,4,1,2,6,119,4,2,2,1))
pppLinkErrEntry.setIndexNames((0,_D,_c))
if mibBuilder.loadTexts:pppLinkErrEntry.setStatus(_A)
class _PppLinkErrIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PppLinkErrIfIndex_Type.__name__=_C
_PppLinkErrIfIndex_Object=MibTableColumn
pppLinkErrIfIndex=_PppLinkErrIfIndex_Object((1,3,6,1,4,1,2,6,119,4,2,2,1,1),_PppLinkErrIfIndex_Type())
pppLinkErrIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkErrIfIndex.setStatus(_A)
_PppLinkErrBadAddrs_Type=Counter32
_PppLinkErrBadAddrs_Object=MibTableColumn
pppLinkErrBadAddrs=_PppLinkErrBadAddrs_Object((1,3,6,1,4,1,2,6,119,4,2,2,1,2),_PppLinkErrBadAddrs_Type())
pppLinkErrBadAddrs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkErrBadAddrs.setStatus(_A)
class _PppLinkErrLastBadAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_PppLinkErrLastBadAddr_Type.__name__=_E
_PppLinkErrLastBadAddr_Object=MibTableColumn
pppLinkErrLastBadAddr=_PppLinkErrLastBadAddr_Object((1,3,6,1,4,1,2,6,119,4,2,2,1,3),_PppLinkErrLastBadAddr_Type())
pppLinkErrLastBadAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkErrLastBadAddr.setStatus(_A)
_PppLinkErrBadCtrls_Type=Counter32
_PppLinkErrBadCtrls_Object=MibTableColumn
pppLinkErrBadCtrls=_PppLinkErrBadCtrls_Object((1,3,6,1,4,1,2,6,119,4,2,2,1,4),_PppLinkErrBadCtrls_Type())
pppLinkErrBadCtrls.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkErrBadCtrls.setStatus(_A)
class _PppLinkErrLastBadCtrl_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_PppLinkErrLastBadCtrl_Type.__name__=_E
_PppLinkErrLastBadCtrl_Object=MibTableColumn
pppLinkErrLastBadCtrl=_PppLinkErrLastBadCtrl_Object((1,3,6,1,4,1,2,6,119,4,2,2,1,5),_PppLinkErrLastBadCtrl_Type())
pppLinkErrLastBadCtrl.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkErrLastBadCtrl.setStatus(_A)
_PppLinkErrUnkProtos_Type=Counter32
_PppLinkErrUnkProtos_Object=MibTableColumn
pppLinkErrUnkProtos=_PppLinkErrUnkProtos_Object((1,3,6,1,4,1,2,6,119,4,2,2,1,6),_PppLinkErrUnkProtos_Type())
pppLinkErrUnkProtos.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkErrUnkProtos.setStatus(_A)
class _PppLinkErrLastUnkProto_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_PppLinkErrLastUnkProto_Type.__name__=_E
_PppLinkErrLastUnkProto_Object=MibTableColumn
pppLinkErrLastUnkProto=_PppLinkErrLastUnkProto_Object((1,3,6,1,4,1,2,6,119,4,2,2,1,7),_PppLinkErrLastUnkProto_Type())
pppLinkErrLastUnkProto.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkErrLastUnkProto.setStatus(_A)
_PppLinkErrInvProtos_Type=Counter32
_PppLinkErrInvProtos_Object=MibTableColumn
pppLinkErrInvProtos=_PppLinkErrInvProtos_Object((1,3,6,1,4,1,2,6,119,4,2,2,1,8),_PppLinkErrInvProtos_Type())
pppLinkErrInvProtos.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkErrInvProtos.setStatus(_A)
class _PppLinkErrLastInvProto_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_PppLinkErrLastInvProto_Type.__name__=_E
_PppLinkErrLastInvProto_Object=MibTableColumn
pppLinkErrLastInvProto=_PppLinkErrLastInvProto_Object((1,3,6,1,4,1,2,6,119,4,2,2,1,9),_PppLinkErrLastInvProto_Type())
pppLinkErrLastInvProto.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkErrLastInvProto.setStatus(_A)
_PppLinkErrConfigTOs_Type=Counter32
_PppLinkErrConfigTOs_Object=MibTableColumn
pppLinkErrConfigTOs=_PppLinkErrConfigTOs_Object((1,3,6,1,4,1,2,6,119,4,2,2,1,10),_PppLinkErrConfigTOs_Type())
pppLinkErrConfigTOs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkErrConfigTOs.setStatus(_A)
_PppLinkErrTermTOs_Type=Counter32
_PppLinkErrTermTOs_Object=MibTableColumn
pppLinkErrTermTOs=_PppLinkErrTermTOs_Object((1,3,6,1,4,1,2,6,119,4,2,2,1,11),_PppLinkErrTermTOs_Type())
pppLinkErrTermTOs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkErrTermTOs.setStatus(_A)
_PppLCProtoTable_Object=MibTable
pppLCProtoTable=_PppLCProtoTable_Object((1,3,6,1,4,1,2,6,119,4,2,3))
if mibBuilder.loadTexts:pppLCProtoTable.setStatus(_A)
_PppLCProtoEntry_Object=MibTableRow
pppLCProtoEntry=_PppLCProtoEntry_Object((1,3,6,1,4,1,2,6,119,4,2,3,1))
pppLCProtoEntry.setIndexNames((0,_D,_d))
if mibBuilder.loadTexts:pppLCProtoEntry.setStatus(_A)
class _PppLCProtoIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PppLCProtoIfIndex_Type.__name__=_C
_PppLCProtoIfIndex_Object=MibTableColumn
pppLCProtoIfIndex=_PppLCProtoIfIndex_Object((1,3,6,1,4,1,2,6,119,4,2,3,1,1),_PppLCProtoIfIndex_Type())
pppLCProtoIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLCProtoIfIndex.setStatus(_A)
class _PppLCProtoState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_L,4),(_M,5),(_N,6),(_O,7)))
_PppLCProtoState_Type.__name__=_C
_PppLCProtoState_Object=MibTableColumn
pppLCProtoState=_PppLCProtoState_Object((1,3,6,1,4,1,2,6,119,4,2,3,1,2),_PppLCProtoState_Type())
pppLCProtoState.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLCProtoState.setStatus(_A)
class _PppLCProtoPreviousState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_L,4),(_M,5),(_N,6),(_O,7)))
_PppLCProtoPreviousState_Type.__name__=_C
_PppLCProtoPreviousState_Object=MibTableColumn
pppLCProtoPreviousState=_PppLCProtoPreviousState_Object((1,3,6,1,4,1,2,6,119,4,2,3,1,3),_PppLCProtoPreviousState_Type())
pppLCProtoPreviousState.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLCProtoPreviousState.setStatus(_A)
_PppLCProtoLastTimeChange_Type=TimeTicks
_PppLCProtoLastTimeChange_Object=MibTableColumn
pppLCProtoLastTimeChange=_PppLCProtoLastTimeChange_Object((1,3,6,1,4,1,2,6,119,4,2,3,1,4),_PppLCProtoLastTimeChange_Type())
pppLCProtoLastTimeChange.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLCProtoLastTimeChange.setStatus(_A)
_PppLCProtoOutPackets_Type=Counter32
_PppLCProtoOutPackets_Object=MibTableColumn
pppLCProtoOutPackets=_PppLCProtoOutPackets_Object((1,3,6,1,4,1,2,6,119,4,2,3,1,5),_PppLCProtoOutPackets_Type())
pppLCProtoOutPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLCProtoOutPackets.setStatus(_A)
_PppLCProtoOutOctets_Type=Counter32
_PppLCProtoOutOctets_Object=MibTableColumn
pppLCProtoOutOctets=_PppLCProtoOutOctets_Object((1,3,6,1,4,1,2,6,119,4,2,3,1,6),_PppLCProtoOutOctets_Type())
pppLCProtoOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLCProtoOutOctets.setStatus(_A)
_PppLCProtoOutCRs_Type=Counter32
_PppLCProtoOutCRs_Object=MibTableColumn
pppLCProtoOutCRs=_PppLCProtoOutCRs_Object((1,3,6,1,4,1,2,6,119,4,2,3,1,7),_PppLCProtoOutCRs_Type())
pppLCProtoOutCRs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLCProtoOutCRs.setStatus(_A)
_PppLCProtoOutCAs_Type=Counter32
_PppLCProtoOutCAs_Object=MibTableColumn
pppLCProtoOutCAs=_PppLCProtoOutCAs_Object((1,3,6,1,4,1,2,6,119,4,2,3,1,8),_PppLCProtoOutCAs_Type())
pppLCProtoOutCAs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLCProtoOutCAs.setStatus(_A)
_PppLCProtoOutCNs_Type=Counter32
_PppLCProtoOutCNs_Object=MibTableColumn
pppLCProtoOutCNs=_PppLCProtoOutCNs_Object((1,3,6,1,4,1,2,6,119,4,2,3,1,9),_PppLCProtoOutCNs_Type())
pppLCProtoOutCNs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLCProtoOutCNs.setStatus(_A)
_PppLCProtoOutCRejs_Type=Counter32
_PppLCProtoOutCRejs_Object=MibTableColumn
pppLCProtoOutCRejs=_PppLCProtoOutCRejs_Object((1,3,6,1,4,1,2,6,119,4,2,3,1,10),_PppLCProtoOutCRejs_Type())
pppLCProtoOutCRejs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLCProtoOutCRejs.setStatus(_A)
_PppLCProtoOutTRs_Type=Counter32
_PppLCProtoOutTRs_Object=MibTableColumn
pppLCProtoOutTRs=_PppLCProtoOutTRs_Object((1,3,6,1,4,1,2,6,119,4,2,3,1,11),_PppLCProtoOutTRs_Type())
pppLCProtoOutTRs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLCProtoOutTRs.setStatus(_A)
_PppLCProtoOutTAs_Type=Counter32
_PppLCProtoOutTAs_Object=MibTableColumn
pppLCProtoOutTAs=_PppLCProtoOutTAs_Object((1,3,6,1,4,1,2,6,119,4,2,3,1,12),_PppLCProtoOutTAs_Type())
pppLCProtoOutTAs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLCProtoOutTAs.setStatus(_A)
_PppLCProtoOutCodeRejs_Type=Counter32
_PppLCProtoOutCodeRejs_Object=MibTableColumn
pppLCProtoOutCodeRejs=_PppLCProtoOutCodeRejs_Object((1,3,6,1,4,1,2,6,119,4,2,3,1,13),_PppLCProtoOutCodeRejs_Type())
pppLCProtoOutCodeRejs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLCProtoOutCodeRejs.setStatus(_A)
_PppLCProtoOutEchoReqs_Type=Counter32
_PppLCProtoOutEchoReqs_Object=MibTableColumn
pppLCProtoOutEchoReqs=_PppLCProtoOutEchoReqs_Object((1,3,6,1,4,1,2,6,119,4,2,3,1,14),_PppLCProtoOutEchoReqs_Type())
pppLCProtoOutEchoReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLCProtoOutEchoReqs.setStatus(_A)
_PppLCProtoOutEchoReps_Type=Counter32
_PppLCProtoOutEchoReps_Object=MibTableColumn
pppLCProtoOutEchoReps=_PppLCProtoOutEchoReps_Object((1,3,6,1,4,1,2,6,119,4,2,3,1,15),_PppLCProtoOutEchoReps_Type())
pppLCProtoOutEchoReps.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLCProtoOutEchoReps.setStatus(_A)
_PppLCProtoOutDiscReqs_Type=Counter32
_PppLCProtoOutDiscReqs_Object=MibTableColumn
pppLCProtoOutDiscReqs=_PppLCProtoOutDiscReqs_Object((1,3,6,1,4,1,2,6,119,4,2,3,1,16),_PppLCProtoOutDiscReqs_Type())
pppLCProtoOutDiscReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLCProtoOutDiscReqs.setStatus(_A)
_PppLCProtoOutResetReqs_Type=Counter32
_PppLCProtoOutResetReqs_Object=MibTableColumn
pppLCProtoOutResetReqs=_PppLCProtoOutResetReqs_Object((1,3,6,1,4,1,2,6,119,4,2,3,1,17),_PppLCProtoOutResetReqs_Type())
pppLCProtoOutResetReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLCProtoOutResetReqs.setStatus(_A)
_PppLCProtoOutResetAcks_Type=Counter32
_PppLCProtoOutResetAcks_Object=MibTableColumn
pppLCProtoOutResetAcks=_PppLCProtoOutResetAcks_Object((1,3,6,1,4,1,2,6,119,4,2,3,1,18),_PppLCProtoOutResetAcks_Type())
pppLCProtoOutResetAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLCProtoOutResetAcks.setStatus(_A)
_PppLCProtoOutIdents_Type=Counter32
_PppLCProtoOutIdents_Object=MibTableColumn
pppLCProtoOutIdents=_PppLCProtoOutIdents_Object((1,3,6,1,4,1,2,6,119,4,2,3,1,19),_PppLCProtoOutIdents_Type())
pppLCProtoOutIdents.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLCProtoOutIdents.setStatus(_A)
_PppLCProtoOutTimeRemains_Type=Counter32
_PppLCProtoOutTimeRemains_Object=MibTableColumn
pppLCProtoOutTimeRemains=_PppLCProtoOutTimeRemains_Object((1,3,6,1,4,1,2,6,119,4,2,3,1,20),_PppLCProtoOutTimeRemains_Type())
pppLCProtoOutTimeRemains.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLCProtoOutTimeRemains.setStatus(_A)
_PppLCProtoInRejects_Type=Counter32
_PppLCProtoInRejects_Object=MibTableColumn
pppLCProtoInRejects=_PppLCProtoInRejects_Object((1,3,6,1,4,1,2,6,119,4,2,3,1,21),_PppLCProtoInRejects_Type())
pppLCProtoInRejects.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLCProtoInRejects.setStatus(_A)
_PppLCProtoInPackets_Type=Counter32
_PppLCProtoInPackets_Object=MibTableColumn
pppLCProtoInPackets=_PppLCProtoInPackets_Object((1,3,6,1,4,1,2,6,119,4,2,3,1,22),_PppLCProtoInPackets_Type())
pppLCProtoInPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLCProtoInPackets.setStatus(_A)
_PppLCProtoInOctets_Type=Counter32
_PppLCProtoInOctets_Object=MibTableColumn
pppLCProtoInOctets=_PppLCProtoInOctets_Object((1,3,6,1,4,1,2,6,119,4,2,3,1,23),_PppLCProtoInOctets_Type())
pppLCProtoInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLCProtoInOctets.setStatus(_A)
_PppLCProtoInCRs_Type=Counter32
_PppLCProtoInCRs_Object=MibTableColumn
pppLCProtoInCRs=_PppLCProtoInCRs_Object((1,3,6,1,4,1,2,6,119,4,2,3,1,24),_PppLCProtoInCRs_Type())
pppLCProtoInCRs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLCProtoInCRs.setStatus(_A)
_PppLCProtoInCAs_Type=Counter32
_PppLCProtoInCAs_Object=MibTableColumn
pppLCProtoInCAs=_PppLCProtoInCAs_Object((1,3,6,1,4,1,2,6,119,4,2,3,1,25),_PppLCProtoInCAs_Type())
pppLCProtoInCAs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLCProtoInCAs.setStatus(_A)
_PppLCProtoInCNs_Type=Counter32
_PppLCProtoInCNs_Object=MibTableColumn
pppLCProtoInCNs=_PppLCProtoInCNs_Object((1,3,6,1,4,1,2,6,119,4,2,3,1,26),_PppLCProtoInCNs_Type())
pppLCProtoInCNs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLCProtoInCNs.setStatus(_A)
_PppLCProtoInCRejs_Type=Counter32
_PppLCProtoInCRejs_Object=MibTableColumn
pppLCProtoInCRejs=_PppLCProtoInCRejs_Object((1,3,6,1,4,1,2,6,119,4,2,3,1,27),_PppLCProtoInCRejs_Type())
pppLCProtoInCRejs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLCProtoInCRejs.setStatus(_A)
_PppLCProtoInTRs_Type=Counter32
_PppLCProtoInTRs_Object=MibTableColumn
pppLCProtoInTRs=_PppLCProtoInTRs_Object((1,3,6,1,4,1,2,6,119,4,2,3,1,28),_PppLCProtoInTRs_Type())
pppLCProtoInTRs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLCProtoInTRs.setStatus(_A)
_PppLCProtoInTAs_Type=Counter32
_PppLCProtoInTAs_Object=MibTableColumn
pppLCProtoInTAs=_PppLCProtoInTAs_Object((1,3,6,1,4,1,2,6,119,4,2,3,1,29),_PppLCProtoInTAs_Type())
pppLCProtoInTAs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLCProtoInTAs.setStatus(_A)
_PppLCProtoInCodeRejs_Type=Counter32
_PppLCProtoInCodeRejs_Object=MibTableColumn
pppLCProtoInCodeRejs=_PppLCProtoInCodeRejs_Object((1,3,6,1,4,1,2,6,119,4,2,3,1,30),_PppLCProtoInCodeRejs_Type())
pppLCProtoInCodeRejs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLCProtoInCodeRejs.setStatus(_A)
_PppLCProtoInEchoReqs_Type=Counter32
_PppLCProtoInEchoReqs_Object=MibTableColumn
pppLCProtoInEchoReqs=_PppLCProtoInEchoReqs_Object((1,3,6,1,4,1,2,6,119,4,2,3,1,31),_PppLCProtoInEchoReqs_Type())
pppLCProtoInEchoReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLCProtoInEchoReqs.setStatus(_A)
_PppLCProtoInEchoReps_Type=Counter32
_PppLCProtoInEchoReps_Object=MibTableColumn
pppLCProtoInEchoReps=_PppLCProtoInEchoReps_Object((1,3,6,1,4,1,2,6,119,4,2,3,1,32),_PppLCProtoInEchoReps_Type())
pppLCProtoInEchoReps.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLCProtoInEchoReps.setStatus(_A)
_PppLCProtoInDiscReqs_Type=Counter32
_PppLCProtoInDiscReqs_Object=MibTableColumn
pppLCProtoInDiscReqs=_PppLCProtoInDiscReqs_Object((1,3,6,1,4,1,2,6,119,4,2,3,1,33),_PppLCProtoInDiscReqs_Type())
pppLCProtoInDiscReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLCProtoInDiscReqs.setStatus(_A)
_PppLCProtoInResetReqs_Type=Counter32
_PppLCProtoInResetReqs_Object=MibTableColumn
pppLCProtoInResetReqs=_PppLCProtoInResetReqs_Object((1,3,6,1,4,1,2,6,119,4,2,3,1,34),_PppLCProtoInResetReqs_Type())
pppLCProtoInResetReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLCProtoInResetReqs.setStatus(_A)
_PppLCProtoInResetAcks_Type=Counter32
_PppLCProtoInResetAcks_Object=MibTableColumn
pppLCProtoInResetAcks=_PppLCProtoInResetAcks_Object((1,3,6,1,4,1,2,6,119,4,2,3,1,35),_PppLCProtoInResetAcks_Type())
pppLCProtoInResetAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLCProtoInResetAcks.setStatus(_A)
_PppLCProtoInIdents_Type=Counter32
_PppLCProtoInIdents_Object=MibTableColumn
pppLCProtoInIdents=_PppLCProtoInIdents_Object((1,3,6,1,4,1,2,6,119,4,2,3,1,36),_PppLCProtoInIdents_Type())
pppLCProtoInIdents.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLCProtoInIdents.setStatus(_A)
_PppLCProtoInTimeRemains_Type=Counter32
_PppLCProtoInTimeRemains_Object=MibTableColumn
pppLCProtoInTimeRemains=_PppLCProtoInTimeRemains_Object((1,3,6,1,4,1,2,6,119,4,2,3,1,37),_PppLCProtoInTimeRemains_Type())
pppLCProtoInTimeRemains.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLCProtoInTimeRemains.setStatus(_A)
_PppPAPTable_Object=MibTable
pppPAPTable=_PppPAPTable_Object((1,3,6,1,4,1,2,6,119,4,2,4))
if mibBuilder.loadTexts:pppPAPTable.setStatus(_A)
_PppPAPEntry_Object=MibTableRow
pppPAPEntry=_PppPAPEntry_Object((1,3,6,1,4,1,2,6,119,4,2,4,1))
pppPAPEntry.setIndexNames((0,_D,_e))
if mibBuilder.loadTexts:pppPAPEntry.setStatus(_A)
class _PppPAPIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PppPAPIfIndex_Type.__name__=_C
_PppPAPIfIndex_Object=MibTableColumn
pppPAPIfIndex=_PppPAPIfIndex_Object((1,3,6,1,4,1,2,6,119,4,2,4,1,1),_PppPAPIfIndex_Type())
pppPAPIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pppPAPIfIndex.setStatus(_A)
_PppPAPInPackets_Type=Counter32
_PppPAPInPackets_Object=MibTableColumn
pppPAPInPackets=_PppPAPInPackets_Object((1,3,6,1,4,1,2,6,119,4,2,4,1,2),_PppPAPInPackets_Type())
pppPAPInPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppPAPInPackets.setStatus(_A)
_PppPAPInOctets_Type=Counter32
_PppPAPInOctets_Object=MibTableColumn
pppPAPInOctets=_PppPAPInOctets_Object((1,3,6,1,4,1,2,6,119,4,2,4,1,3),_PppPAPInOctets_Type())
pppPAPInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppPAPInOctets.setStatus(_A)
_PppPAPInRequests_Type=Counter32
_PppPAPInRequests_Object=MibTableColumn
pppPAPInRequests=_PppPAPInRequests_Object((1,3,6,1,4,1,2,6,119,4,2,4,1,4),_PppPAPInRequests_Type())
pppPAPInRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:pppPAPInRequests.setStatus(_A)
_PppPAPInAcks_Type=Counter32
_PppPAPInAcks_Object=MibTableColumn
pppPAPInAcks=_PppPAPInAcks_Object((1,3,6,1,4,1,2,6,119,4,2,4,1,5),_PppPAPInAcks_Type())
pppPAPInAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:pppPAPInAcks.setStatus(_A)
_PppPAPInNacks_Type=Counter32
_PppPAPInNacks_Object=MibTableColumn
pppPAPInNacks=_PppPAPInNacks_Object((1,3,6,1,4,1,2,6,119,4,2,4,1,6),_PppPAPInNacks_Type())
pppPAPInNacks.setMaxAccess(_B)
if mibBuilder.loadTexts:pppPAPInNacks.setStatus(_A)
_PppPAPOutPackets_Type=Counter32
_PppPAPOutPackets_Object=MibTableColumn
pppPAPOutPackets=_PppPAPOutPackets_Object((1,3,6,1,4,1,2,6,119,4,2,4,1,7),_PppPAPOutPackets_Type())
pppPAPOutPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppPAPOutPackets.setStatus(_A)
_PppPAPOutOctets_Type=Counter32
_PppPAPOutOctets_Object=MibTableColumn
pppPAPOutOctets=_PppPAPOutOctets_Object((1,3,6,1,4,1,2,6,119,4,2,4,1,8),_PppPAPOutOctets_Type())
pppPAPOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppPAPOutOctets.setStatus(_A)
_PppPAPOutRequests_Type=Counter32
_PppPAPOutRequests_Object=MibTableColumn
pppPAPOutRequests=_PppPAPOutRequests_Object((1,3,6,1,4,1,2,6,119,4,2,4,1,9),_PppPAPOutRequests_Type())
pppPAPOutRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:pppPAPOutRequests.setStatus(_A)
_PppPAPOutAcks_Type=Counter32
_PppPAPOutAcks_Object=MibTableColumn
pppPAPOutAcks=_PppPAPOutAcks_Object((1,3,6,1,4,1,2,6,119,4,2,4,1,10),_PppPAPOutAcks_Type())
pppPAPOutAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:pppPAPOutAcks.setStatus(_A)
_PppPAPOutNacks_Type=Counter32
_PppPAPOutNacks_Object=MibTableColumn
pppPAPOutNacks=_PppPAPOutNacks_Object((1,3,6,1,4,1,2,6,119,4,2,4,1,11),_PppPAPOutNacks_Type())
pppPAPOutNacks.setMaxAccess(_B)
if mibBuilder.loadTexts:pppPAPOutNacks.setStatus(_A)
_PppCHAPTable_Object=MibTable
pppCHAPTable=_PppCHAPTable_Object((1,3,6,1,4,1,2,6,119,4,2,5))
if mibBuilder.loadTexts:pppCHAPTable.setStatus(_A)
_PppCHAPEntry_Object=MibTableRow
pppCHAPEntry=_PppCHAPEntry_Object((1,3,6,1,4,1,2,6,119,4,2,5,1))
pppCHAPEntry.setIndexNames((0,_D,_f))
if mibBuilder.loadTexts:pppCHAPEntry.setStatus(_A)
class _PppCHAPIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PppCHAPIfIndex_Type.__name__=_C
_PppCHAPIfIndex_Object=MibTableColumn
pppCHAPIfIndex=_PppCHAPIfIndex_Object((1,3,6,1,4,1,2,6,119,4,2,5,1,1),_PppCHAPIfIndex_Type())
pppCHAPIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCHAPIfIndex.setStatus(_A)
_PppCHAPInPackets_Type=Counter32
_PppCHAPInPackets_Object=MibTableColumn
pppCHAPInPackets=_PppCHAPInPackets_Object((1,3,6,1,4,1,2,6,119,4,2,5,1,2),_PppCHAPInPackets_Type())
pppCHAPInPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCHAPInPackets.setStatus(_A)
_PppCHAPInOctets_Type=Counter32
_PppCHAPInOctets_Object=MibTableColumn
pppCHAPInOctets=_PppCHAPInOctets_Object((1,3,6,1,4,1,2,6,119,4,2,5,1,3),_PppCHAPInOctets_Type())
pppCHAPInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCHAPInOctets.setStatus(_A)
_PppCHAPInChallenges_Type=Counter32
_PppCHAPInChallenges_Object=MibTableColumn
pppCHAPInChallenges=_PppCHAPInChallenges_Object((1,3,6,1,4,1,2,6,119,4,2,5,1,4),_PppCHAPInChallenges_Type())
pppCHAPInChallenges.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCHAPInChallenges.setStatus(_A)
_PppCHAPInResponses_Type=Counter32
_PppCHAPInResponses_Object=MibTableColumn
pppCHAPInResponses=_PppCHAPInResponses_Object((1,3,6,1,4,1,2,6,119,4,2,5,1,5),_PppCHAPInResponses_Type())
pppCHAPInResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCHAPInResponses.setStatus(_A)
_PppCHAPInSuccesses_Type=Counter32
_PppCHAPInSuccesses_Object=MibTableColumn
pppCHAPInSuccesses=_PppCHAPInSuccesses_Object((1,3,6,1,4,1,2,6,119,4,2,5,1,6),_PppCHAPInSuccesses_Type())
pppCHAPInSuccesses.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCHAPInSuccesses.setStatus(_A)
_PppCHAPInFailures_Type=Counter32
_PppCHAPInFailures_Object=MibTableColumn
pppCHAPInFailures=_PppCHAPInFailures_Object((1,3,6,1,4,1,2,6,119,4,2,5,1,7),_PppCHAPInFailures_Type())
pppCHAPInFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCHAPInFailures.setStatus(_A)
_PppCHAPOutPackets_Type=Counter32
_PppCHAPOutPackets_Object=MibTableColumn
pppCHAPOutPackets=_PppCHAPOutPackets_Object((1,3,6,1,4,1,2,6,119,4,2,5,1,8),_PppCHAPOutPackets_Type())
pppCHAPOutPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCHAPOutPackets.setStatus(_A)
_PppCHAPOutOctets_Type=Counter32
_PppCHAPOutOctets_Object=MibTableColumn
pppCHAPOutOctets=_PppCHAPOutOctets_Object((1,3,6,1,4,1,2,6,119,4,2,5,1,9),_PppCHAPOutOctets_Type())
pppCHAPOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCHAPOutOctets.setStatus(_A)
_PppCHAPOutChallenges_Type=Counter32
_PppCHAPOutChallenges_Object=MibTableColumn
pppCHAPOutChallenges=_PppCHAPOutChallenges_Object((1,3,6,1,4,1,2,6,119,4,2,5,1,10),_PppCHAPOutChallenges_Type())
pppCHAPOutChallenges.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCHAPOutChallenges.setStatus(_A)
_PppCHAPOutResponses_Type=Counter32
_PppCHAPOutResponses_Object=MibTableColumn
pppCHAPOutResponses=_PppCHAPOutResponses_Object((1,3,6,1,4,1,2,6,119,4,2,5,1,11),_PppCHAPOutResponses_Type())
pppCHAPOutResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCHAPOutResponses.setStatus(_A)
_PppCHAPOutSuccesses_Type=Counter32
_PppCHAPOutSuccesses_Object=MibTableColumn
pppCHAPOutSuccesses=_PppCHAPOutSuccesses_Object((1,3,6,1,4,1,2,6,119,4,2,5,1,12),_PppCHAPOutSuccesses_Type())
pppCHAPOutSuccesses.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCHAPOutSuccesses.setStatus(_A)
_PppCHAPOutFailures_Type=Counter32
_PppCHAPOutFailures_Object=MibTableColumn
pppCHAPOutFailures=_PppCHAPOutFailures_Object((1,3,6,1,4,1,2,6,119,4,2,5,1,13),_PppCHAPOutFailures_Type())
pppCHAPOutFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCHAPOutFailures.setStatus(_A)
_PppSPAPTable_Object=MibTable
pppSPAPTable=_PppSPAPTable_Object((1,3,6,1,4,1,2,6,119,4,2,6))
if mibBuilder.loadTexts:pppSPAPTable.setStatus(_A)
_PppSPAPEntry_Object=MibTableRow
pppSPAPEntry=_PppSPAPEntry_Object((1,3,6,1,4,1,2,6,119,4,2,6,1))
pppSPAPEntry.setIndexNames((0,_D,_g))
if mibBuilder.loadTexts:pppSPAPEntry.setStatus(_A)
class _PppSPAPIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PppSPAPIfIndex_Type.__name__=_C
_PppSPAPIfIndex_Object=MibTableColumn
pppSPAPIfIndex=_PppSPAPIfIndex_Object((1,3,6,1,4,1,2,6,119,4,2,6,1,1),_PppSPAPIfIndex_Type())
pppSPAPIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pppSPAPIfIndex.setStatus(_A)
_PppSPAPInPackets_Type=Counter32
_PppSPAPInPackets_Object=MibTableColumn
pppSPAPInPackets=_PppSPAPInPackets_Object((1,3,6,1,4,1,2,6,119,4,2,6,1,2),_PppSPAPInPackets_Type())
pppSPAPInPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppSPAPInPackets.setStatus(_A)
_PppSPAPInOctets_Type=Counter32
_PppSPAPInOctets_Object=MibTableColumn
pppSPAPInOctets=_PppSPAPInOctets_Object((1,3,6,1,4,1,2,6,119,4,2,6,1,3),_PppSPAPInOctets_Type())
pppSPAPInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppSPAPInOctets.setStatus(_A)
_PppSPAPInRequests_Type=Counter32
_PppSPAPInRequests_Object=MibTableColumn
pppSPAPInRequests=_PppSPAPInRequests_Object((1,3,6,1,4,1,2,6,119,4,2,6,1,4),_PppSPAPInRequests_Type())
pppSPAPInRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:pppSPAPInRequests.setStatus(_A)
_PppSPAPInAcks_Type=Counter32
_PppSPAPInAcks_Object=MibTableColumn
pppSPAPInAcks=_PppSPAPInAcks_Object((1,3,6,1,4,1,2,6,119,4,2,6,1,5),_PppSPAPInAcks_Type())
pppSPAPInAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:pppSPAPInAcks.setStatus(_A)
_PppSPAPInNacks_Type=Counter32
_PppSPAPInNacks_Object=MibTableColumn
pppSPAPInNacks=_PppSPAPInNacks_Object((1,3,6,1,4,1,2,6,119,4,2,6,1,6),_PppSPAPInNacks_Type())
pppSPAPInNacks.setMaxAccess(_B)
if mibBuilder.loadTexts:pppSPAPInNacks.setStatus(_A)
_PppSPAPInDialbacks_Type=Counter32
_PppSPAPInDialbacks_Object=MibTableColumn
pppSPAPInDialbacks=_PppSPAPInDialbacks_Object((1,3,6,1,4,1,2,6,119,4,2,6,1,7),_PppSPAPInDialbacks_Type())
pppSPAPInDialbacks.setMaxAccess(_B)
if mibBuilder.loadTexts:pppSPAPInDialbacks.setStatus(_A)
_PppSPAPInPleaseAuthenticates_Type=Counter32
_PppSPAPInPleaseAuthenticates_Object=MibTableColumn
pppSPAPInPleaseAuthenticates=_PppSPAPInPleaseAuthenticates_Object((1,3,6,1,4,1,2,6,119,4,2,6,1,8),_PppSPAPInPleaseAuthenticates_Type())
pppSPAPInPleaseAuthenticates.setMaxAccess(_B)
if mibBuilder.loadTexts:pppSPAPInPleaseAuthenticates.setStatus(_A)
_PppSPAPInChangePasswords_Type=Counter32
_PppSPAPInChangePasswords_Object=MibTableColumn
pppSPAPInChangePasswords=_PppSPAPInChangePasswords_Object((1,3,6,1,4,1,2,6,119,4,2,6,1,9),_PppSPAPInChangePasswords_Type())
pppSPAPInChangePasswords.setMaxAccess(_B)
if mibBuilder.loadTexts:pppSPAPInChangePasswords.setStatus(_A)
_PppSPAPInAlerts_Type=Counter32
_PppSPAPInAlerts_Object=MibTableColumn
pppSPAPInAlerts=_PppSPAPInAlerts_Object((1,3,6,1,4,1,2,6,119,4,2,6,1,10),_PppSPAPInAlerts_Type())
pppSPAPInAlerts.setMaxAccess(_B)
if mibBuilder.loadTexts:pppSPAPInAlerts.setStatus(_A)
_PppSPAPInAlertAcks_Type=Counter32
_PppSPAPInAlertAcks_Object=MibTableColumn
pppSPAPInAlertAcks=_PppSPAPInAlertAcks_Object((1,3,6,1,4,1,2,6,119,4,2,6,1,11),_PppSPAPInAlertAcks_Type())
pppSPAPInAlertAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:pppSPAPInAlertAcks.setStatus(_A)
_PppSPAPOutPackets_Type=Counter32
_PppSPAPOutPackets_Object=MibTableColumn
pppSPAPOutPackets=_PppSPAPOutPackets_Object((1,3,6,1,4,1,2,6,119,4,2,6,1,12),_PppSPAPOutPackets_Type())
pppSPAPOutPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppSPAPOutPackets.setStatus(_A)
_PppSPAPOutOctets_Type=Counter32
_PppSPAPOutOctets_Object=MibTableColumn
pppSPAPOutOctets=_PppSPAPOutOctets_Object((1,3,6,1,4,1,2,6,119,4,2,6,1,13),_PppSPAPOutOctets_Type())
pppSPAPOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppSPAPOutOctets.setStatus(_A)
_PppSPAPOutRequests_Type=Counter32
_PppSPAPOutRequests_Object=MibTableColumn
pppSPAPOutRequests=_PppSPAPOutRequests_Object((1,3,6,1,4,1,2,6,119,4,2,6,1,14),_PppSPAPOutRequests_Type())
pppSPAPOutRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:pppSPAPOutRequests.setStatus(_A)
_PppSPAPOutAcks_Type=Counter32
_PppSPAPOutAcks_Object=MibTableColumn
pppSPAPOutAcks=_PppSPAPOutAcks_Object((1,3,6,1,4,1,2,6,119,4,2,6,1,15),_PppSPAPOutAcks_Type())
pppSPAPOutAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:pppSPAPOutAcks.setStatus(_A)
_PppSPAPOutNacks_Type=Counter32
_PppSPAPOutNacks_Object=MibTableColumn
pppSPAPOutNacks=_PppSPAPOutNacks_Object((1,3,6,1,4,1,2,6,119,4,2,6,1,16),_PppSPAPOutNacks_Type())
pppSPAPOutNacks.setMaxAccess(_B)
if mibBuilder.loadTexts:pppSPAPOutNacks.setStatus(_A)
_PppSPAPOutDialbacks_Type=Counter32
_PppSPAPOutDialbacks_Object=MibTableColumn
pppSPAPOutDialbacks=_PppSPAPOutDialbacks_Object((1,3,6,1,4,1,2,6,119,4,2,6,1,17),_PppSPAPOutDialbacks_Type())
pppSPAPOutDialbacks.setMaxAccess(_B)
if mibBuilder.loadTexts:pppSPAPOutDialbacks.setStatus(_A)
_PppSPAPOutPleaseAuthenticates_Type=Counter32
_PppSPAPOutPleaseAuthenticates_Object=MibTableColumn
pppSPAPOutPleaseAuthenticates=_PppSPAPOutPleaseAuthenticates_Object((1,3,6,1,4,1,2,6,119,4,2,6,1,18),_PppSPAPOutPleaseAuthenticates_Type())
pppSPAPOutPleaseAuthenticates.setMaxAccess(_B)
if mibBuilder.loadTexts:pppSPAPOutPleaseAuthenticates.setStatus(_A)
_PppSPAPOutChangePasswords_Type=Counter32
_PppSPAPOutChangePasswords_Object=MibTableColumn
pppSPAPOutChangePasswords=_PppSPAPOutChangePasswords_Object((1,3,6,1,4,1,2,6,119,4,2,6,1,19),_PppSPAPOutChangePasswords_Type())
pppSPAPOutChangePasswords.setMaxAccess(_B)
if mibBuilder.loadTexts:pppSPAPOutChangePasswords.setStatus(_A)
_PppSPAPOutAlerts_Type=Counter32
_PppSPAPOutAlerts_Object=MibTableColumn
pppSPAPOutAlerts=_PppSPAPOutAlerts_Object((1,3,6,1,4,1,2,6,119,4,2,6,1,20),_PppSPAPOutAlerts_Type())
pppSPAPOutAlerts.setMaxAccess(_B)
if mibBuilder.loadTexts:pppSPAPOutAlerts.setStatus(_A)
_PppSPAPOutAlertAcks_Type=Counter32
_PppSPAPOutAlertAcks_Object=MibTableColumn
pppSPAPOutAlertAcks=_PppSPAPOutAlertAcks_Object((1,3,6,1,4,1,2,6,119,4,2,6,1,21),_PppSPAPOutAlertAcks_Type())
pppSPAPOutAlertAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:pppSPAPOutAlertAcks.setStatus(_A)
_PppBAPTable_Object=MibTable
pppBAPTable=_PppBAPTable_Object((1,3,6,1,4,1,2,6,119,4,2,7))
if mibBuilder.loadTexts:pppBAPTable.setStatus(_A)
_PppBAPEntry_Object=MibTableRow
pppBAPEntry=_PppBAPEntry_Object((1,3,6,1,4,1,2,6,119,4,2,7,1))
pppBAPEntry.setIndexNames((0,_D,_h))
if mibBuilder.loadTexts:pppBAPEntry.setStatus(_A)
class _PppBAPIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PppBAPIfIndex_Type.__name__=_C
_PppBAPIfIndex_Object=MibTableColumn
pppBAPIfIndex=_PppBAPIfIndex_Object((1,3,6,1,4,1,2,6,119,4,2,7,1,1),_PppBAPIfIndex_Type())
pppBAPIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pppBAPIfIndex.setStatus(_A)
_PppBAPInCallReqs_Type=Counter32
_PppBAPInCallReqs_Object=MibTableColumn
pppBAPInCallReqs=_PppBAPInCallReqs_Object((1,3,6,1,4,1,2,6,119,4,2,7,1,2),_PppBAPInCallReqs_Type())
pppBAPInCallReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppBAPInCallReqs.setStatus(_A)
_PppBAPInCallAcks_Type=Counter32
_PppBAPInCallAcks_Object=MibTableColumn
pppBAPInCallAcks=_PppBAPInCallAcks_Object((1,3,6,1,4,1,2,6,119,4,2,7,1,3),_PppBAPInCallAcks_Type())
pppBAPInCallAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:pppBAPInCallAcks.setStatus(_A)
_PppBAPInCallNaks_Type=Counter32
_PppBAPInCallNaks_Object=MibTableColumn
pppBAPInCallNaks=_PppBAPInCallNaks_Object((1,3,6,1,4,1,2,6,119,4,2,7,1,4),_PppBAPInCallNaks_Type())
pppBAPInCallNaks.setMaxAccess(_B)
if mibBuilder.loadTexts:pppBAPInCallNaks.setStatus(_A)
_PppBAPInCallRejs_Type=Counter32
_PppBAPInCallRejs_Object=MibTableColumn
pppBAPInCallRejs=_PppBAPInCallRejs_Object((1,3,6,1,4,1,2,6,119,4,2,7,1,5),_PppBAPInCallRejs_Type())
pppBAPInCallRejs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppBAPInCallRejs.setStatus(_A)
_PppBAPInCallBackReqs_Type=Counter32
_PppBAPInCallBackReqs_Object=MibTableColumn
pppBAPInCallBackReqs=_PppBAPInCallBackReqs_Object((1,3,6,1,4,1,2,6,119,4,2,7,1,6),_PppBAPInCallBackReqs_Type())
pppBAPInCallBackReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppBAPInCallBackReqs.setStatus(_A)
_PppBAPInCallBackAcks_Type=Counter32
_PppBAPInCallBackAcks_Object=MibTableColumn
pppBAPInCallBackAcks=_PppBAPInCallBackAcks_Object((1,3,6,1,4,1,2,6,119,4,2,7,1,7),_PppBAPInCallBackAcks_Type())
pppBAPInCallBackAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:pppBAPInCallBackAcks.setStatus(_A)
_PppBAPInCallBackNaks_Type=Counter32
_PppBAPInCallBackNaks_Object=MibTableColumn
pppBAPInCallBackNaks=_PppBAPInCallBackNaks_Object((1,3,6,1,4,1,2,6,119,4,2,7,1,8),_PppBAPInCallBackNaks_Type())
pppBAPInCallBackNaks.setMaxAccess(_B)
if mibBuilder.loadTexts:pppBAPInCallBackNaks.setStatus(_A)
_PppBAPInCallBackRejs_Type=Counter32
_PppBAPInCallBackRejs_Object=MibTableColumn
pppBAPInCallBackRejs=_PppBAPInCallBackRejs_Object((1,3,6,1,4,1,2,6,119,4,2,7,1,9),_PppBAPInCallBackRejs_Type())
pppBAPInCallBackRejs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppBAPInCallBackRejs.setStatus(_A)
_PppBAPInDropReqs_Type=Counter32
_PppBAPInDropReqs_Object=MibTableColumn
pppBAPInDropReqs=_PppBAPInDropReqs_Object((1,3,6,1,4,1,2,6,119,4,2,7,1,10),_PppBAPInDropReqs_Type())
pppBAPInDropReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppBAPInDropReqs.setStatus(_A)
_PppBAPInDropAcks_Type=Counter32
_PppBAPInDropAcks_Object=MibTableColumn
pppBAPInDropAcks=_PppBAPInDropAcks_Object((1,3,6,1,4,1,2,6,119,4,2,7,1,11),_PppBAPInDropAcks_Type())
pppBAPInDropAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:pppBAPInDropAcks.setStatus(_A)
_PppBAPInDropNaks_Type=Counter32
_PppBAPInDropNaks_Object=MibTableColumn
pppBAPInDropNaks=_PppBAPInDropNaks_Object((1,3,6,1,4,1,2,6,119,4,2,7,1,12),_PppBAPInDropNaks_Type())
pppBAPInDropNaks.setMaxAccess(_B)
if mibBuilder.loadTexts:pppBAPInDropNaks.setStatus(_A)
_PppBAPInDropRejs_Type=Counter32
_PppBAPInDropRejs_Object=MibTableColumn
pppBAPInDropRejs=_PppBAPInDropRejs_Object((1,3,6,1,4,1,2,6,119,4,2,7,1,13),_PppBAPInDropRejs_Type())
pppBAPInDropRejs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppBAPInDropRejs.setStatus(_A)
_PppBAPInStatSuccs_Type=Counter32
_PppBAPInStatSuccs_Object=MibTableColumn
pppBAPInStatSuccs=_PppBAPInStatSuccs_Object((1,3,6,1,4,1,2,6,119,4,2,7,1,14),_PppBAPInStatSuccs_Type())
pppBAPInStatSuccs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppBAPInStatSuccs.setStatus(_A)
_PppBAPInStatFails_Type=Counter32
_PppBAPInStatFails_Object=MibTableColumn
pppBAPInStatFails=_PppBAPInStatFails_Object((1,3,6,1,4,1,2,6,119,4,2,7,1,15),_PppBAPInStatFails_Type())
pppBAPInStatFails.setMaxAccess(_B)
if mibBuilder.loadTexts:pppBAPInStatFails.setStatus(_A)
_PppBAPOutCallReqs_Type=Counter32
_PppBAPOutCallReqs_Object=MibTableColumn
pppBAPOutCallReqs=_PppBAPOutCallReqs_Object((1,3,6,1,4,1,2,6,119,4,2,7,1,16),_PppBAPOutCallReqs_Type())
pppBAPOutCallReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppBAPOutCallReqs.setStatus(_A)
_PppBAPOutCallAcks_Type=Counter32
_PppBAPOutCallAcks_Object=MibTableColumn
pppBAPOutCallAcks=_PppBAPOutCallAcks_Object((1,3,6,1,4,1,2,6,119,4,2,7,1,17),_PppBAPOutCallAcks_Type())
pppBAPOutCallAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:pppBAPOutCallAcks.setStatus(_A)
_PppBAPOutCallNaks_Type=Counter32
_PppBAPOutCallNaks_Object=MibTableColumn
pppBAPOutCallNaks=_PppBAPOutCallNaks_Object((1,3,6,1,4,1,2,6,119,4,2,7,1,18),_PppBAPOutCallNaks_Type())
pppBAPOutCallNaks.setMaxAccess(_B)
if mibBuilder.loadTexts:pppBAPOutCallNaks.setStatus(_A)
_PppBAPOutCallRejs_Type=Counter32
_PppBAPOutCallRejs_Object=MibTableColumn
pppBAPOutCallRejs=_PppBAPOutCallRejs_Object((1,3,6,1,4,1,2,6,119,4,2,7,1,19),_PppBAPOutCallRejs_Type())
pppBAPOutCallRejs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppBAPOutCallRejs.setStatus(_A)
_PppBAPOutCallBackReqs_Type=Counter32
_PppBAPOutCallBackReqs_Object=MibTableColumn
pppBAPOutCallBackReqs=_PppBAPOutCallBackReqs_Object((1,3,6,1,4,1,2,6,119,4,2,7,1,20),_PppBAPOutCallBackReqs_Type())
pppBAPOutCallBackReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppBAPOutCallBackReqs.setStatus(_A)
_PppBAPOutCallBackAcks_Type=Counter32
_PppBAPOutCallBackAcks_Object=MibTableColumn
pppBAPOutCallBackAcks=_PppBAPOutCallBackAcks_Object((1,3,6,1,4,1,2,6,119,4,2,7,1,21),_PppBAPOutCallBackAcks_Type())
pppBAPOutCallBackAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:pppBAPOutCallBackAcks.setStatus(_A)
_PppBAPOutCallBackNaks_Type=Counter32
_PppBAPOutCallBackNaks_Object=MibTableColumn
pppBAPOutCallBackNaks=_PppBAPOutCallBackNaks_Object((1,3,6,1,4,1,2,6,119,4,2,7,1,22),_PppBAPOutCallBackNaks_Type())
pppBAPOutCallBackNaks.setMaxAccess(_B)
if mibBuilder.loadTexts:pppBAPOutCallBackNaks.setStatus(_A)
_PppBAPOutCallBackRejs_Type=Counter32
_PppBAPOutCallBackRejs_Object=MibTableColumn
pppBAPOutCallBackRejs=_PppBAPOutCallBackRejs_Object((1,3,6,1,4,1,2,6,119,4,2,7,1,23),_PppBAPOutCallBackRejs_Type())
pppBAPOutCallBackRejs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppBAPOutCallBackRejs.setStatus(_A)
_PppBAPOutDropReqs_Type=Counter32
_PppBAPOutDropReqs_Object=MibTableColumn
pppBAPOutDropReqs=_PppBAPOutDropReqs_Object((1,3,6,1,4,1,2,6,119,4,2,7,1,24),_PppBAPOutDropReqs_Type())
pppBAPOutDropReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppBAPOutDropReqs.setStatus(_A)
_PppBAPOutDropAcks_Type=Counter32
_PppBAPOutDropAcks_Object=MibTableColumn
pppBAPOutDropAcks=_PppBAPOutDropAcks_Object((1,3,6,1,4,1,2,6,119,4,2,7,1,25),_PppBAPOutDropAcks_Type())
pppBAPOutDropAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:pppBAPOutDropAcks.setStatus(_A)
_PppBAPOutDropNaks_Type=Counter32
_PppBAPOutDropNaks_Object=MibTableColumn
pppBAPOutDropNaks=_PppBAPOutDropNaks_Object((1,3,6,1,4,1,2,6,119,4,2,7,1,26),_PppBAPOutDropNaks_Type())
pppBAPOutDropNaks.setMaxAccess(_B)
if mibBuilder.loadTexts:pppBAPOutDropNaks.setStatus(_A)
_PppBAPOutDropRejs_Type=Counter32
_PppBAPOutDropRejs_Object=MibTableColumn
pppBAPOutDropRejs=_PppBAPOutDropRejs_Object((1,3,6,1,4,1,2,6,119,4,2,7,1,27),_PppBAPOutDropRejs_Type())
pppBAPOutDropRejs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppBAPOutDropRejs.setStatus(_A)
_PppBAPOutStatSuccs_Type=Counter32
_PppBAPOutStatSuccs_Object=MibTableColumn
pppBAPOutStatSuccs=_PppBAPOutStatSuccs_Object((1,3,6,1,4,1,2,6,119,4,2,7,1,28),_PppBAPOutStatSuccs_Type())
pppBAPOutStatSuccs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppBAPOutStatSuccs.setStatus(_A)
_PppBAPOutStatFails_Type=Counter32
_PppBAPOutStatFails_Object=MibTableColumn
pppBAPOutStatFails=_PppBAPOutStatFails_Object((1,3,6,1,4,1,2,6,119,4,2,7,1,29),_PppBAPOutStatFails_Type())
pppBAPOutStatFails.setMaxAccess(_B)
if mibBuilder.loadTexts:pppBAPOutStatFails.setStatus(_A)
_PppCPTable_Object=MibTable
pppCPTable=_PppCPTable_Object((1,3,6,1,4,1,2,6,119,4,2,8))
if mibBuilder.loadTexts:pppCPTable.setStatus(_A)
_PppCPEntry_Object=MibTableRow
pppCPEntry=_PppCPEntry_Object((1,3,6,1,4,1,2,6,119,4,2,8,1))
pppCPEntry.setIndexNames((0,_D,_i))
if mibBuilder.loadTexts:pppCPEntry.setStatus(_A)
class _PppCPIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PppCPIfIndex_Type.__name__=_C
_PppCPIfIndex_Object=MibTableColumn
pppCPIfIndex=_PppCPIfIndex_Object((1,3,6,1,4,1,2,6,119,4,2,8,1,1),_PppCPIfIndex_Type())
pppCPIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCPIfIndex.setStatus(_A)
_PppCPInCompressedOctets_Type=Counter32
_PppCPInCompressedOctets_Object=MibTableColumn
pppCPInCompressedOctets=_PppCPInCompressedOctets_Object((1,3,6,1,4,1,2,6,119,4,2,8,1,2),_PppCPInCompressedOctets_Type())
pppCPInCompressedOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCPInCompressedOctets.setStatus(_A)
_PppCPInInCompressablePkts_Type=Counter32
_PppCPInInCompressablePkts_Object=MibTableColumn
pppCPInInCompressablePkts=_PppCPInInCompressablePkts_Object((1,3,6,1,4,1,2,6,119,4,2,8,1,3),_PppCPInInCompressablePkts_Type())
pppCPInInCompressablePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCPInInCompressablePkts.setStatus(_A)
_PppCPInDestroyeds_Type=Counter32
_PppCPInDestroyeds_Object=MibTableColumn
pppCPInDestroyeds=_PppCPInDestroyeds_Object((1,3,6,1,4,1,2,6,119,4,2,8,1,4),_PppCPInDestroyeds_Type())
pppCPInDestroyeds.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCPInDestroyeds.setStatus(_A)
_PppCPInCopies_Type=Counter32
_PppCPInCopies_Object=MibTableColumn
pppCPInCopies=_PppCPInCopies_Object((1,3,6,1,4,1,2,6,119,4,2,8,1,5),_PppCPInCopies_Type())
pppCPInCopies.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCPInCopies.setStatus(_A)
_PppCPOutCompressedOctets_Type=Counter32
_PppCPOutCompressedOctets_Object=MibTableColumn
pppCPOutCompressedOctets=_PppCPOutCompressedOctets_Object((1,3,6,1,4,1,2,6,119,4,2,8,1,6),_PppCPOutCompressedOctets_Type())
pppCPOutCompressedOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCPOutCompressedOctets.setStatus(_A)
_PppCPOutInCompressablePkts_Type=Counter32
_PppCPOutInCompressablePkts_Object=MibTableColumn
pppCPOutInCompressablePkts=_PppCPOutInCompressablePkts_Object((1,3,6,1,4,1,2,6,119,4,2,8,1,7),_PppCPOutInCompressablePkts_Type())
pppCPOutInCompressablePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCPOutInCompressablePkts.setStatus(_A)
_PppCPOutDestroyeds_Type=Counter32
_PppCPOutDestroyeds_Object=MibTableColumn
pppCPOutDestroyeds=_PppCPOutDestroyeds_Object((1,3,6,1,4,1,2,6,119,4,2,8,1,8),_PppCPOutDestroyeds_Type())
pppCPOutDestroyeds.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCPOutDestroyeds.setStatus(_A)
_PppCPOutCopies_Type=Counter32
_PppCPOutCopies_Object=MibTableColumn
pppCPOutCopies=_PppCPOutCopies_Object((1,3,6,1,4,1,2,6,119,4,2,8,1,9),_PppCPOutCopies_Type())
pppCPOutCopies.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCPOutCopies.setStatus(_A)
_PppCCPInResetReqs_Type=Counter32
_PppCCPInResetReqs_Object=MibTableColumn
pppCCPInResetReqs=_PppCCPInResetReqs_Object((1,3,6,1,4,1,2,6,119,4,2,8,1,10),_PppCCPInResetReqs_Type())
pppCCPInResetReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCCPInResetReqs.setStatus(_A)
_PppCCPInResetAcks_Type=Counter32
_PppCCPInResetAcks_Object=MibTableColumn
pppCCPInResetAcks=_PppCCPInResetAcks_Object((1,3,6,1,4,1,2,6,119,4,2,8,1,11),_PppCCPInResetAcks_Type())
pppCCPInResetAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCCPInResetAcks.setStatus(_A)
_PppCCPInDictResets_Type=Counter32
_PppCCPInDictResets_Object=MibTableColumn
pppCCPInDictResets=_PppCCPInDictResets_Object((1,3,6,1,4,1,2,6,119,4,2,8,1,12),_PppCCPInDictResets_Type())
pppCCPInDictResets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCCPInDictResets.setStatus(_A)
_PppCCPOutResetReqs_Type=Counter32
_PppCCPOutResetReqs_Object=MibTableColumn
pppCCPOutResetReqs=_PppCCPOutResetReqs_Object((1,3,6,1,4,1,2,6,119,4,2,8,1,13),_PppCCPOutResetReqs_Type())
pppCCPOutResetReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCCPOutResetReqs.setStatus(_A)
_PppCCPOutResetAcks_Type=Counter32
_PppCCPOutResetAcks_Object=MibTableColumn
pppCCPOutResetAcks=_PppCCPOutResetAcks_Object((1,3,6,1,4,1,2,6,119,4,2,8,1,14),_PppCCPOutResetAcks_Type())
pppCCPOutResetAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCCPOutResetAcks.setStatus(_A)
_PppCCPOutDictResets_Type=Counter32
_PppCCPOutDictResets_Object=MibTableColumn
pppCCPOutDictResets=_PppCCPOutDictResets_Object((1,3,6,1,4,1,2,6,119,4,2,8,1,15),_PppCCPOutDictResets_Type())
pppCCPOutDictResets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCCPOutDictResets.setStatus(_A)
_PppCCPPacketDiscards_Type=Counter32
_PppCCPPacketDiscards_Object=MibTableColumn
pppCCPPacketDiscards=_PppCCPPacketDiscards_Object((1,3,6,1,4,1,2,6,119,4,2,8,1,16),_PppCCPPacketDiscards_Type())
pppCCPPacketDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCCPPacketDiscards.setStatus(_A)
_PppCCPOctetDiscards_Type=Counter32
_PppCCPOctetDiscards_Object=MibTableColumn
pppCCPOctetDiscards=_PppCCPOctetDiscards_Object((1,3,6,1,4,1,2,6,119,4,2,8,1,17),_PppCCPOctetDiscards_Type())
pppCCPOctetDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCCPOctetDiscards.setStatus(_A)
_PppEPTable_Object=MibTable
pppEPTable=_PppEPTable_Object((1,3,6,1,4,1,2,6,119,4,2,9))
if mibBuilder.loadTexts:pppEPTable.setStatus(_A)
_PppEPEntry_Object=MibTableRow
pppEPEntry=_PppEPEntry_Object((1,3,6,1,4,1,2,6,119,4,2,9,1))
pppEPEntry.setIndexNames((0,_D,_j))
if mibBuilder.loadTexts:pppEPEntry.setStatus(_A)
class _PppEPIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PppEPIfIndex_Type.__name__=_C
_PppEPIfIndex_Object=MibTableColumn
pppEPIfIndex=_PppEPIfIndex_Object((1,3,6,1,4,1,2,6,119,4,2,9,1,1),_PppEPIfIndex_Type())
pppEPIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pppEPIfIndex.setStatus(_A)
_PppEPInEncryptedOctets_Type=Counter32
_PppEPInEncryptedOctets_Object=MibTableColumn
pppEPInEncryptedOctets=_PppEPInEncryptedOctets_Object((1,3,6,1,4,1,2,6,119,4,2,9,1,2),_PppEPInEncryptedOctets_Type())
pppEPInEncryptedOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppEPInEncryptedOctets.setStatus(_A)
_PppEPInDestroyeds_Type=Counter32
_PppEPInDestroyeds_Object=MibTableColumn
pppEPInDestroyeds=_PppEPInDestroyeds_Object((1,3,6,1,4,1,2,6,119,4,2,9,1,3),_PppEPInDestroyeds_Type())
pppEPInDestroyeds.setMaxAccess(_B)
if mibBuilder.loadTexts:pppEPInDestroyeds.setStatus(_A)
_PppEPInCopies_Type=Counter32
_PppEPInCopies_Object=MibTableColumn
pppEPInCopies=_PppEPInCopies_Object((1,3,6,1,4,1,2,6,119,4,2,9,1,4),_PppEPInCopies_Type())
pppEPInCopies.setMaxAccess(_B)
if mibBuilder.loadTexts:pppEPInCopies.setStatus(_A)
_PppEPOutEncryptedOctets_Type=Counter32
_PppEPOutEncryptedOctets_Object=MibTableColumn
pppEPOutEncryptedOctets=_PppEPOutEncryptedOctets_Object((1,3,6,1,4,1,2,6,119,4,2,9,1,5),_PppEPOutEncryptedOctets_Type())
pppEPOutEncryptedOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppEPOutEncryptedOctets.setStatus(_A)
_PppEPOutDestroyeds_Type=Counter32
_PppEPOutDestroyeds_Object=MibTableColumn
pppEPOutDestroyeds=_PppEPOutDestroyeds_Object((1,3,6,1,4,1,2,6,119,4,2,9,1,6),_PppEPOutDestroyeds_Type())
pppEPOutDestroyeds.setMaxAccess(_B)
if mibBuilder.loadTexts:pppEPOutDestroyeds.setStatus(_A)
_PppEPOutCopies_Type=Counter32
_PppEPOutCopies_Object=MibTableColumn
pppEPOutCopies=_PppEPOutCopies_Object((1,3,6,1,4,1,2,6,119,4,2,9,1,7),_PppEPOutCopies_Type())
pppEPOutCopies.setMaxAccess(_B)
if mibBuilder.loadTexts:pppEPOutCopies.setStatus(_A)
_PppECPInResetReqs_Type=Counter32
_PppECPInResetReqs_Object=MibTableColumn
pppECPInResetReqs=_PppECPInResetReqs_Object((1,3,6,1,4,1,2,6,119,4,2,9,1,8),_PppECPInResetReqs_Type())
pppECPInResetReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppECPInResetReqs.setStatus(_A)
_PppECPInResetAcks_Type=Counter32
_PppECPInResetAcks_Object=MibTableColumn
pppECPInResetAcks=_PppECPInResetAcks_Object((1,3,6,1,4,1,2,6,119,4,2,9,1,9),_PppECPInResetAcks_Type())
pppECPInResetAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:pppECPInResetAcks.setStatus(_A)
_PppECPInDictResets_Type=Counter32
_PppECPInDictResets_Object=MibTableColumn
pppECPInDictResets=_PppECPInDictResets_Object((1,3,6,1,4,1,2,6,119,4,2,9,1,10),_PppECPInDictResets_Type())
pppECPInDictResets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppECPInDictResets.setStatus(_A)
_PppECPOutResetReqs_Type=Counter32
_PppECPOutResetReqs_Object=MibTableColumn
pppECPOutResetReqs=_PppECPOutResetReqs_Object((1,3,6,1,4,1,2,6,119,4,2,9,1,11),_PppECPOutResetReqs_Type())
pppECPOutResetReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:pppECPOutResetReqs.setStatus(_A)
_PppECPOutResetAcks_Type=Counter32
_PppECPOutResetAcks_Object=MibTableColumn
pppECPOutResetAcks=_PppECPOutResetAcks_Object((1,3,6,1,4,1,2,6,119,4,2,9,1,12),_PppECPOutResetAcks_Type())
pppECPOutResetAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:pppECPOutResetAcks.setStatus(_A)
_PppECPOutDictResets_Type=Counter32
_PppECPOutDictResets_Object=MibTableColumn
pppECPOutDictResets=_PppECPOutDictResets_Object((1,3,6,1,4,1,2,6,119,4,2,9,1,13),_PppECPOutDictResets_Type())
pppECPOutDictResets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppECPOutDictResets.setStatus(_A)
_PppECPPacketDiscards_Type=Counter32
_PppECPPacketDiscards_Object=MibTableColumn
pppECPPacketDiscards=_PppECPPacketDiscards_Object((1,3,6,1,4,1,2,6,119,4,2,9,1,14),_PppECPPacketDiscards_Type())
pppECPPacketDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:pppECPPacketDiscards.setStatus(_A)
_PppECPOctetDiscards_Type=Counter32
_PppECPOctetDiscards_Object=MibTableColumn
pppECPOctetDiscards=_PppECPOctetDiscards_Object((1,3,6,1,4,1,2,6,119,4,2,9,1,15),_PppECPOctetDiscards_Type())
pppECPOctetDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:pppECPOctetDiscards.setStatus(_A)
_PppMSCHAPTable_Object=MibTable
pppMSCHAPTable=_PppMSCHAPTable_Object((1,3,6,1,4,1,2,6,119,4,2,10))
if mibBuilder.loadTexts:pppMSCHAPTable.setStatus(_A)
_PppMSCHAPEntry_Object=MibTableRow
pppMSCHAPEntry=_PppMSCHAPEntry_Object((1,3,6,1,4,1,2,6,119,4,2,10,1))
pppMSCHAPEntry.setIndexNames((0,_D,_k))
if mibBuilder.loadTexts:pppMSCHAPEntry.setStatus(_A)
class _PppMSCHAPIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PppMSCHAPIfIndex_Type.__name__=_C
_PppMSCHAPIfIndex_Object=MibTableColumn
pppMSCHAPIfIndex=_PppMSCHAPIfIndex_Object((1,3,6,1,4,1,2,6,119,4,2,10,1,1),_PppMSCHAPIfIndex_Type())
pppMSCHAPIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pppMSCHAPIfIndex.setStatus(_A)
_PppMSCHAPInPackets_Type=Counter32
_PppMSCHAPInPackets_Object=MibTableColumn
pppMSCHAPInPackets=_PppMSCHAPInPackets_Object((1,3,6,1,4,1,2,6,119,4,2,10,1,2),_PppMSCHAPInPackets_Type())
pppMSCHAPInPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppMSCHAPInPackets.setStatus(_A)
_PppMSCHAPInOctets_Type=Counter32
_PppMSCHAPInOctets_Object=MibTableColumn
pppMSCHAPInOctets=_PppMSCHAPInOctets_Object((1,3,6,1,4,1,2,6,119,4,2,10,1,3),_PppMSCHAPInOctets_Type())
pppMSCHAPInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppMSCHAPInOctets.setStatus(_A)
_PppMSCHAPInChallenges_Type=Counter32
_PppMSCHAPInChallenges_Object=MibTableColumn
pppMSCHAPInChallenges=_PppMSCHAPInChallenges_Object((1,3,6,1,4,1,2,6,119,4,2,10,1,4),_PppMSCHAPInChallenges_Type())
pppMSCHAPInChallenges.setMaxAccess(_B)
if mibBuilder.loadTexts:pppMSCHAPInChallenges.setStatus(_A)
_PppMSCHAPInResponses_Type=Counter32
_PppMSCHAPInResponses_Object=MibTableColumn
pppMSCHAPInResponses=_PppMSCHAPInResponses_Object((1,3,6,1,4,1,2,6,119,4,2,10,1,5),_PppMSCHAPInResponses_Type())
pppMSCHAPInResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:pppMSCHAPInResponses.setStatus(_A)
_PppMSCHAPInSuccesses_Type=Counter32
_PppMSCHAPInSuccesses_Object=MibTableColumn
pppMSCHAPInSuccesses=_PppMSCHAPInSuccesses_Object((1,3,6,1,4,1,2,6,119,4,2,10,1,6),_PppMSCHAPInSuccesses_Type())
pppMSCHAPInSuccesses.setMaxAccess(_B)
if mibBuilder.loadTexts:pppMSCHAPInSuccesses.setStatus(_A)
_PppMSCHAPInFailures_Type=Counter32
_PppMSCHAPInFailures_Object=MibTableColumn
pppMSCHAPInFailures=_PppMSCHAPInFailures_Object((1,3,6,1,4,1,2,6,119,4,2,10,1,7),_PppMSCHAPInFailures_Type())
pppMSCHAPInFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:pppMSCHAPInFailures.setStatus(_A)
_PppMSCHAPInChangePasswords_Type=Counter32
_PppMSCHAPInChangePasswords_Object=MibTableColumn
pppMSCHAPInChangePasswords=_PppMSCHAPInChangePasswords_Object((1,3,6,1,4,1,2,6,119,4,2,10,1,8),_PppMSCHAPInChangePasswords_Type())
pppMSCHAPInChangePasswords.setMaxAccess(_B)
if mibBuilder.loadTexts:pppMSCHAPInChangePasswords.setStatus(_A)
_PppMSCHAPInRestrictedHoursFailures_Type=Counter32
_PppMSCHAPInRestrictedHoursFailures_Object=MibTableColumn
pppMSCHAPInRestrictedHoursFailures=_PppMSCHAPInRestrictedHoursFailures_Object((1,3,6,1,4,1,2,6,119,4,2,10,1,9),_PppMSCHAPInRestrictedHoursFailures_Type())
pppMSCHAPInRestrictedHoursFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:pppMSCHAPInRestrictedHoursFailures.setStatus(_A)
_PppMSCHAPInAccountDisabledFailures_Type=Counter32
_PppMSCHAPInAccountDisabledFailures_Object=MibTableColumn
pppMSCHAPInAccountDisabledFailures=_PppMSCHAPInAccountDisabledFailures_Object((1,3,6,1,4,1,2,6,119,4,2,10,1,10),_PppMSCHAPInAccountDisabledFailures_Type())
pppMSCHAPInAccountDisabledFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:pppMSCHAPInAccountDisabledFailures.setStatus(_A)
_PppMSCHAPInPasswordExpiredFailures_Type=Counter32
_PppMSCHAPInPasswordExpiredFailures_Object=MibTableColumn
pppMSCHAPInPasswordExpiredFailures=_PppMSCHAPInPasswordExpiredFailures_Object((1,3,6,1,4,1,2,6,119,4,2,10,1,11),_PppMSCHAPInPasswordExpiredFailures_Type())
pppMSCHAPInPasswordExpiredFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:pppMSCHAPInPasswordExpiredFailures.setStatus(_A)
_PppMSCHAPInNoPermissionFailures_Type=Counter32
_PppMSCHAPInNoPermissionFailures_Object=MibTableColumn
pppMSCHAPInNoPermissionFailures=_PppMSCHAPInNoPermissionFailures_Object((1,3,6,1,4,1,2,6,119,4,2,10,1,12),_PppMSCHAPInNoPermissionFailures_Type())
pppMSCHAPInNoPermissionFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:pppMSCHAPInNoPermissionFailures.setStatus(_A)
_PppMSCHAPInAuthenticationFailures_Type=Counter32
_PppMSCHAPInAuthenticationFailures_Object=MibTableColumn
pppMSCHAPInAuthenticationFailures=_PppMSCHAPInAuthenticationFailures_Object((1,3,6,1,4,1,2,6,119,4,2,10,1,13),_PppMSCHAPInAuthenticationFailures_Type())
pppMSCHAPInAuthenticationFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:pppMSCHAPInAuthenticationFailures.setStatus(_A)
_PppMSCHAPInChangePasswordFailures_Type=Counter32
_PppMSCHAPInChangePasswordFailures_Object=MibTableColumn
pppMSCHAPInChangePasswordFailures=_PppMSCHAPInChangePasswordFailures_Object((1,3,6,1,4,1,2,6,119,4,2,10,1,14),_PppMSCHAPInChangePasswordFailures_Type())
pppMSCHAPInChangePasswordFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:pppMSCHAPInChangePasswordFailures.setStatus(_A)
_PppMSCHAPOutPackets_Type=Counter32
_PppMSCHAPOutPackets_Object=MibTableColumn
pppMSCHAPOutPackets=_PppMSCHAPOutPackets_Object((1,3,6,1,4,1,2,6,119,4,2,10,1,15),_PppMSCHAPOutPackets_Type())
pppMSCHAPOutPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppMSCHAPOutPackets.setStatus(_A)
_PppMSCHAPOutOctets_Type=Counter32
_PppMSCHAPOutOctets_Object=MibTableColumn
pppMSCHAPOutOctets=_PppMSCHAPOutOctets_Object((1,3,6,1,4,1,2,6,119,4,2,10,1,16),_PppMSCHAPOutOctets_Type())
pppMSCHAPOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppMSCHAPOutOctets.setStatus(_A)
_PppMSCHAPOutChallenges_Type=Counter32
_PppMSCHAPOutChallenges_Object=MibTableColumn
pppMSCHAPOutChallenges=_PppMSCHAPOutChallenges_Object((1,3,6,1,4,1,2,6,119,4,2,10,1,17),_PppMSCHAPOutChallenges_Type())
pppMSCHAPOutChallenges.setMaxAccess(_B)
if mibBuilder.loadTexts:pppMSCHAPOutChallenges.setStatus(_A)
_PppMSCHAPOutResponses_Type=Counter32
_PppMSCHAPOutResponses_Object=MibTableColumn
pppMSCHAPOutResponses=_PppMSCHAPOutResponses_Object((1,3,6,1,4,1,2,6,119,4,2,10,1,18),_PppMSCHAPOutResponses_Type())
pppMSCHAPOutResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:pppMSCHAPOutResponses.setStatus(_A)
_PppMSCHAPOutSuccesses_Type=Counter32
_PppMSCHAPOutSuccesses_Object=MibTableColumn
pppMSCHAPOutSuccesses=_PppMSCHAPOutSuccesses_Object((1,3,6,1,4,1,2,6,119,4,2,10,1,19),_PppMSCHAPOutSuccesses_Type())
pppMSCHAPOutSuccesses.setMaxAccess(_B)
if mibBuilder.loadTexts:pppMSCHAPOutSuccesses.setStatus(_A)
_PppMSCHAPOutFailures_Type=Counter32
_PppMSCHAPOutFailures_Object=MibTableColumn
pppMSCHAPOutFailures=_PppMSCHAPOutFailures_Object((1,3,6,1,4,1,2,6,119,4,2,10,1,20),_PppMSCHAPOutFailures_Type())
pppMSCHAPOutFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:pppMSCHAPOutFailures.setStatus(_A)
_PppMSCHAPOutChangePasswords_Type=Counter32
_PppMSCHAPOutChangePasswords_Object=MibTableColumn
pppMSCHAPOutChangePasswords=_PppMSCHAPOutChangePasswords_Object((1,3,6,1,4,1,2,6,119,4,2,10,1,21),_PppMSCHAPOutChangePasswords_Type())
pppMSCHAPOutChangePasswords.setMaxAccess(_B)
if mibBuilder.loadTexts:pppMSCHAPOutChangePasswords.setStatus(_A)
_PppMSCHAPOutRestrictedHoursFailures_Type=Counter32
_PppMSCHAPOutRestrictedHoursFailures_Object=MibTableColumn
pppMSCHAPOutRestrictedHoursFailures=_PppMSCHAPOutRestrictedHoursFailures_Object((1,3,6,1,4,1,2,6,119,4,2,10,1,22),_PppMSCHAPOutRestrictedHoursFailures_Type())
pppMSCHAPOutRestrictedHoursFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:pppMSCHAPOutRestrictedHoursFailures.setStatus(_A)
_PppMSCHAPOutAccountDisabledFailures_Type=Counter32
_PppMSCHAPOutAccountDisabledFailures_Object=MibTableColumn
pppMSCHAPOutAccountDisabledFailures=_PppMSCHAPOutAccountDisabledFailures_Object((1,3,6,1,4,1,2,6,119,4,2,10,1,23),_PppMSCHAPOutAccountDisabledFailures_Type())
pppMSCHAPOutAccountDisabledFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:pppMSCHAPOutAccountDisabledFailures.setStatus(_A)
_PppMSCHAPOutPasswordExpiredFailures_Type=Counter32
_PppMSCHAPOutPasswordExpiredFailures_Object=MibTableColumn
pppMSCHAPOutPasswordExpiredFailures=_PppMSCHAPOutPasswordExpiredFailures_Object((1,3,6,1,4,1,2,6,119,4,2,10,1,24),_PppMSCHAPOutPasswordExpiredFailures_Type())
pppMSCHAPOutPasswordExpiredFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:pppMSCHAPOutPasswordExpiredFailures.setStatus(_A)
_PppMSCHAPOutNoPermissionFailures_Type=Counter32
_PppMSCHAPOutNoPermissionFailures_Object=MibTableColumn
pppMSCHAPOutNoPermissionFailures=_PppMSCHAPOutNoPermissionFailures_Object((1,3,6,1,4,1,2,6,119,4,2,10,1,25),_PppMSCHAPOutNoPermissionFailures_Type())
pppMSCHAPOutNoPermissionFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:pppMSCHAPOutNoPermissionFailures.setStatus(_A)
_PppMSCHAPOutAuthenticationFailures_Type=Counter32
_PppMSCHAPOutAuthenticationFailures_Object=MibTableColumn
pppMSCHAPOutAuthenticationFailures=_PppMSCHAPOutAuthenticationFailures_Object((1,3,6,1,4,1,2,6,119,4,2,10,1,26),_PppMSCHAPOutAuthenticationFailures_Type())
pppMSCHAPOutAuthenticationFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:pppMSCHAPOutAuthenticationFailures.setStatus(_A)
_PppMSCHAPOutChangePasswordFailures_Type=Counter32
_PppMSCHAPOutChangePasswordFailures_Object=MibTableColumn
pppMSCHAPOutChangePasswordFailures=_PppMSCHAPOutChangePasswordFailures_Object((1,3,6,1,4,1,2,6,119,4,2,10,1,27),_PppMSCHAPOutChangePasswordFailures_Type())
pppMSCHAPOutChangePasswordFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:pppMSCHAPOutChangePasswordFailures.setStatus(_A)
_PppCBCPTable_Object=MibTable
pppCBCPTable=_PppCBCPTable_Object((1,3,6,1,4,1,2,6,119,4,2,11))
if mibBuilder.loadTexts:pppCBCPTable.setStatus(_A)
_PppCBCPEntry_Object=MibTableRow
pppCBCPEntry=_PppCBCPEntry_Object((1,3,6,1,4,1,2,6,119,4,2,11,1))
pppCBCPEntry.setIndexNames((0,_D,_l))
if mibBuilder.loadTexts:pppCBCPEntry.setStatus(_A)
class _PppCBCPIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PppCBCPIfIndex_Type.__name__=_C
_PppCBCPIfIndex_Object=MibTableColumn
pppCBCPIfIndex=_PppCBCPIfIndex_Object((1,3,6,1,4,1,2,6,119,4,2,11,1,1),_PppCBCPIfIndex_Type())
pppCBCPIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCBCPIfIndex.setStatus(_A)
_PppCBCPInPackets_Type=Counter32
_PppCBCPInPackets_Object=MibTableColumn
pppCBCPInPackets=_PppCBCPInPackets_Object((1,3,6,1,4,1,2,6,119,4,2,11,1,2),_PppCBCPInPackets_Type())
pppCBCPInPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCBCPInPackets.setStatus(_A)
_PppCBCPInOctets_Type=Counter32
_PppCBCPInOctets_Object=MibTableColumn
pppCBCPInOctets=_PppCBCPInOctets_Object((1,3,6,1,4,1,2,6,119,4,2,11,1,3),_PppCBCPInOctets_Type())
pppCBCPInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCBCPInOctets.setStatus(_A)
_PppCBCPOutPackets_Type=Counter32
_PppCBCPOutPackets_Object=MibTableColumn
pppCBCPOutPackets=_PppCBCPOutPackets_Object((1,3,6,1,4,1,2,6,119,4,2,11,1,4),_PppCBCPOutPackets_Type())
pppCBCPOutPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCBCPOutPackets.setStatus(_A)
_PppCBCPOutOctets_Type=Counter32
_PppCBCPOutOctets_Object=MibTableColumn
pppCBCPOutOctets=_PppCBCPOutOctets_Object((1,3,6,1,4,1,2,6,119,4,2,11,1,5),_PppCBCPOutOctets_Type())
pppCBCPOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCBCPOutOctets.setStatus(_A)
_PppCBCPAttempts_Type=Counter32
_PppCBCPAttempts_Object=MibTableColumn
pppCBCPAttempts=_PppCBCPAttempts_Object((1,3,6,1,4,1,2,6,119,4,2,11,1,6),_PppCBCPAttempts_Type())
pppCBCPAttempts.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCBCPAttempts.setStatus(_A)
_PppCBCPSuccess_Type=Counter32
_PppCBCPSuccess_Object=MibTableColumn
pppCBCPSuccess=_PppCBCPSuccess_Object((1,3,6,1,4,1,2,6,119,4,2,11,1,7),_PppCBCPSuccess_Type())
pppCBCPSuccess.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCBCPSuccess.setStatus(_A)
_PppEAPTable_Object=MibTable
pppEAPTable=_PppEAPTable_Object((1,3,6,1,4,1,2,6,119,4,2,12))
if mibBuilder.loadTexts:pppEAPTable.setStatus(_A)
_PppEAPEntry_Object=MibTableRow
pppEAPEntry=_PppEAPEntry_Object((1,3,6,1,4,1,2,6,119,4,2,12,1))
pppEAPEntry.setIndexNames((0,_D,_m))
if mibBuilder.loadTexts:pppEAPEntry.setStatus(_A)
class _PppEAPIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PppEAPIfIndex_Type.__name__=_C
_PppEAPIfIndex_Object=MibTableColumn
pppEAPIfIndex=_PppEAPIfIndex_Object((1,3,6,1,4,1,2,6,119,4,2,12,1,1),_PppEAPIfIndex_Type())
pppEAPIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pppEAPIfIndex.setStatus(_A)
_PppEAPInPackets_Type=Counter32
_PppEAPInPackets_Object=MibTableColumn
pppEAPInPackets=_PppEAPInPackets_Object((1,3,6,1,4,1,2,6,119,4,2,12,1,2),_PppEAPInPackets_Type())
pppEAPInPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppEAPInPackets.setStatus(_A)
_PppEAPInOctets_Type=Counter32
_PppEAPInOctets_Object=MibTableColumn
pppEAPInOctets=_PppEAPInOctets_Object((1,3,6,1,4,1,2,6,119,4,2,12,1,3),_PppEAPInOctets_Type())
pppEAPInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppEAPInOctets.setStatus(_A)
_PppEAPInRequests_Type=Counter32
_PppEAPInRequests_Object=MibTableColumn
pppEAPInRequests=_PppEAPInRequests_Object((1,3,6,1,4,1,2,6,119,4,2,12,1,4),_PppEAPInRequests_Type())
pppEAPInRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:pppEAPInRequests.setStatus(_A)
_PppEAPInAcks_Type=Counter32
_PppEAPInAcks_Object=MibTableColumn
pppEAPInAcks=_PppEAPInAcks_Object((1,3,6,1,4,1,2,6,119,4,2,12,1,5),_PppEAPInAcks_Type())
pppEAPInAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:pppEAPInAcks.setStatus(_A)
_PppEAPInNaks_Type=Counter32
_PppEAPInNaks_Object=MibTableColumn
pppEAPInNaks=_PppEAPInNaks_Object((1,3,6,1,4,1,2,6,119,4,2,12,1,6),_PppEAPInNaks_Type())
pppEAPInNaks.setMaxAccess(_B)
if mibBuilder.loadTexts:pppEAPInNaks.setStatus(_A)
_PppEAPOutPackets_Type=Counter32
_PppEAPOutPackets_Object=MibTableColumn
pppEAPOutPackets=_PppEAPOutPackets_Object((1,3,6,1,4,1,2,6,119,4,2,12,1,7),_PppEAPOutPackets_Type())
pppEAPOutPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppEAPOutPackets.setStatus(_A)
_PppEAPOutOctets_Type=Counter32
_PppEAPOutOctets_Object=MibTableColumn
pppEAPOutOctets=_PppEAPOutOctets_Object((1,3,6,1,4,1,2,6,119,4,2,12,1,8),_PppEAPOutOctets_Type())
pppEAPOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppEAPOutOctets.setStatus(_A)
_PppEAPOutRequests_Type=Counter32
_PppEAPOutRequests_Object=MibTableColumn
pppEAPOutRequests=_PppEAPOutRequests_Object((1,3,6,1,4,1,2,6,119,4,2,12,1,9),_PppEAPOutRequests_Type())
pppEAPOutRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:pppEAPOutRequests.setStatus(_A)
_PppEAPOutAcks_Type=Counter32
_PppEAPOutAcks_Object=MibTableColumn
pppEAPOutAcks=_PppEAPOutAcks_Object((1,3,6,1,4,1,2,6,119,4,2,12,1,10),_PppEAPOutAcks_Type())
pppEAPOutAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:pppEAPOutAcks.setStatus(_A)
_PppEAPOutNaks_Type=Counter32
_PppEAPOutNaks_Object=MibTableColumn
pppEAPOutNaks=_PppEAPOutNaks_Object((1,3,6,1,4,1,2,6,119,4,2,12,1,11),_PppEAPOutNaks_Type())
pppEAPOutNaks.setMaxAccess(_B)
if mibBuilder.loadTexts:pppEAPOutNaks.setStatus(_A)
_PppMPPETable_Object=MibTable
pppMPPETable=_PppMPPETable_Object((1,3,6,1,4,1,2,6,119,4,2,13))
if mibBuilder.loadTexts:pppMPPETable.setStatus(_A)
_PppMPPEEntry_Object=MibTableRow
pppMPPEEntry=_PppMPPEEntry_Object((1,3,6,1,4,1,2,6,119,4,2,13,1))
pppMPPEEntry.setIndexNames((0,_D,_n))
if mibBuilder.loadTexts:pppMPPEEntry.setStatus(_A)
class _PppMPPEIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PppMPPEIfIndex_Type.__name__=_C
_PppMPPEIfIndex_Object=MibTableColumn
pppMPPEIfIndex=_PppMPPEIfIndex_Object((1,3,6,1,4,1,2,6,119,4,2,13,1,1),_PppMPPEIfIndex_Type())
pppMPPEIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pppMPPEIfIndex.setStatus(_A)
_PppMPPEInPackets_Type=Counter32
_PppMPPEInPackets_Object=MibTableColumn
pppMPPEInPackets=_PppMPPEInPackets_Object((1,3,6,1,4,1,2,6,119,4,2,13,1,2),_PppMPPEInPackets_Type())
pppMPPEInPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppMPPEInPackets.setStatus(_A)
_PppMPPEInOctets_Type=Counter32
_PppMPPEInOctets_Object=MibTableColumn
pppMPPEInOctets=_PppMPPEInOctets_Object((1,3,6,1,4,1,2,6,119,4,2,13,1,3),_PppMPPEInOctets_Type())
pppMPPEInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppMPPEInOctets.setStatus(_A)
_PppMPPEInDestroyed_Type=Counter32
_PppMPPEInDestroyed_Object=MibTableColumn
pppMPPEInDestroyed=_PppMPPEInDestroyed_Object((1,3,6,1,4,1,2,6,119,4,2,13,1,4),_PppMPPEInDestroyed_Type())
pppMPPEInDestroyed.setMaxAccess(_B)
if mibBuilder.loadTexts:pppMPPEInDestroyed.setStatus(_A)
_PppMPPEOutPackets_Type=Counter32
_PppMPPEOutPackets_Object=MibTableColumn
pppMPPEOutPackets=_PppMPPEOutPackets_Object((1,3,6,1,4,1,2,6,119,4,2,13,1,5),_PppMPPEOutPackets_Type())
pppMPPEOutPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppMPPEOutPackets.setStatus(_A)
_PppMPPEOutOctets_Type=Counter32
_PppMPPEOutOctets_Object=MibTableColumn
pppMPPEOutOctets=_PppMPPEOutOctets_Object((1,3,6,1,4,1,2,6,119,4,2,13,1,6),_PppMPPEOutOctets_Type())
pppMPPEOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppMPPEOutOctets.setStatus(_A)
_PppMPPEOutDestroyed_Type=Counter32
_PppMPPEOutDestroyed_Object=MibTableColumn
pppMPPEOutDestroyed=_PppMPPEOutDestroyed_Object((1,3,6,1,4,1,2,6,119,4,2,13,1,7),_PppMPPEOutDestroyed_Type())
pppMPPEOutDestroyed.setMaxAccess(_B)
if mibBuilder.loadTexts:pppMPPEOutDestroyed.setStatus(_A)
_IbmIROCroutingdlsw_ObjectIdentity=ObjectIdentity
ibmIROCroutingdlsw=_IbmIROCroutingdlsw_ObjectIdentity((1,3,6,1,4,1,2,6,119,4,3))
_IbmdlswTConnGroupOperTable_Object=MibTable
ibmdlswTConnGroupOperTable=_IbmdlswTConnGroupOperTable_Object((1,3,6,1,4,1,2,6,119,4,3,1))
if mibBuilder.loadTexts:ibmdlswTConnGroupOperTable.setStatus(_A)
_IbmdlswTConnGroupOperEntry_Object=MibTableRow
ibmdlswTConnGroupOperEntry=_IbmdlswTConnGroupOperEntry_Object((1,3,6,1,4,1,2,6,119,4,3,1,1))
ibmdlswTConnGroupOperEntry.setIndexNames((0,_D,_o))
if mibBuilder.loadTexts:ibmdlswTConnGroupOperEntry.setStatus(_A)
class _IbmdlswTConnGroupOperIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_IbmdlswTConnGroupOperIndex_Type.__name__=_C
_IbmdlswTConnGroupOperIndex_Object=MibTableColumn
ibmdlswTConnGroupOperIndex=_IbmdlswTConnGroupOperIndex_Object((1,3,6,1,4,1,2,6,119,4,3,1,1,1),_IbmdlswTConnGroupOperIndex_Type())
ibmdlswTConnGroupOperIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlswTConnGroupOperIndex.setStatus(_A)
class _IbmdlswTConnGroupOperRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('peer',1),('client',2),('server',3),('readonly',4),('writeonly',5),('readwrite',6),('other',7)))
_IbmdlswTConnGroupOperRole_Type.__name__=_C
_IbmdlswTConnGroupOperRole_Object=MibTableColumn
ibmdlswTConnGroupOperRole=_IbmdlswTConnGroupOperRole_Object((1,3,6,1,4,1,2,6,119,4,3,1,1,2),_IbmdlswTConnGroupOperRole_Type())
ibmdlswTConnGroupOperRole.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlswTConnGroupOperRole.setStatus(_A)
_IbmdlswTConnGroupOperJoinTime_Type=TimeTicks
_IbmdlswTConnGroupOperJoinTime_Object=MibTableColumn
ibmdlswTConnGroupOperJoinTime=_IbmdlswTConnGroupOperJoinTime_Object((1,3,6,1,4,1,2,6,119,4,3,1,1,3),_IbmdlswTConnGroupOperJoinTime_Type())
ibmdlswTConnGroupOperJoinTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlswTConnGroupOperJoinTime.setStatus(_A)
class _IbmdlswTConnGroupOperConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_IbmdlswTConnGroupOperConfigIndex_Type.__name__=_C
_IbmdlswTConnGroupOperConfigIndex_Object=MibTableColumn
ibmdlswTConnGroupOperConfigIndex=_IbmdlswTConnGroupOperConfigIndex_Object((1,3,6,1,4,1,2,6,119,4,3,1,1,4),_IbmdlswTConnGroupOperConfigIndex_Type())
ibmdlswTConnGroupOperConfigIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlswTConnGroupOperConfigIndex.setStatus(_A)
_IbmdlswTConnGroupOperInDataPkts_Type=Counter32
_IbmdlswTConnGroupOperInDataPkts_Object=MibTableColumn
ibmdlswTConnGroupOperInDataPkts=_IbmdlswTConnGroupOperInDataPkts_Object((1,3,6,1,4,1,2,6,119,4,3,1,1,5),_IbmdlswTConnGroupOperInDataPkts_Type())
ibmdlswTConnGroupOperInDataPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlswTConnGroupOperInDataPkts.setStatus(_A)
_IbmdlswTConnGroupOperOutDataPkts_Type=Counter32
_IbmdlswTConnGroupOperOutDataPkts_Object=MibTableColumn
ibmdlswTConnGroupOperOutDataPkts=_IbmdlswTConnGroupOperOutDataPkts_Object((1,3,6,1,4,1,2,6,119,4,3,1,1,6),_IbmdlswTConnGroupOperOutDataPkts_Type())
ibmdlswTConnGroupOperOutDataPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlswTConnGroupOperOutDataPkts.setStatus(_A)
_IbmdlswTConnGroupOperInDataOctets_Type=Counter32
_IbmdlswTConnGroupOperInDataOctets_Object=MibTableColumn
ibmdlswTConnGroupOperInDataOctets=_IbmdlswTConnGroupOperInDataOctets_Object((1,3,6,1,4,1,2,6,119,4,3,1,1,7),_IbmdlswTConnGroupOperInDataOctets_Type())
ibmdlswTConnGroupOperInDataOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlswTConnGroupOperInDataOctets.setStatus(_A)
_IbmdlswTConnGroupOperOutDataOctets_Type=Counter32
_IbmdlswTConnGroupOperOutDataOctets_Object=MibTableColumn
ibmdlswTConnGroupOperOutDataOctets=_IbmdlswTConnGroupOperOutDataOctets_Object((1,3,6,1,4,1,2,6,119,4,3,1,1,8),_IbmdlswTConnGroupOperOutDataOctets_Type())
ibmdlswTConnGroupOperOutDataOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlswTConnGroupOperOutDataOctets.setStatus(_A)
_IbmdlswTConnGroupOperInCntlPkts_Type=Counter32
_IbmdlswTConnGroupOperInCntlPkts_Object=MibTableColumn
ibmdlswTConnGroupOperInCntlPkts=_IbmdlswTConnGroupOperInCntlPkts_Object((1,3,6,1,4,1,2,6,119,4,3,1,1,9),_IbmdlswTConnGroupOperInCntlPkts_Type())
ibmdlswTConnGroupOperInCntlPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlswTConnGroupOperInCntlPkts.setStatus(_A)
_IbmdlswTConnGroupOperOutCntlPkts_Type=Counter32
_IbmdlswTConnGroupOperOutCntlPkts_Object=MibTableColumn
ibmdlswTConnGroupOperOutCntlPkts=_IbmdlswTConnGroupOperOutCntlPkts_Object((1,3,6,1,4,1,2,6,119,4,3,1,1,10),_IbmdlswTConnGroupOperOutCntlPkts_Type())
ibmdlswTConnGroupOperOutCntlPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlswTConnGroupOperOutCntlPkts.setStatus(_A)
_IbmdlswTConnGroupOperCURexSents_Type=Counter32
_IbmdlswTConnGroupOperCURexSents_Object=MibTableColumn
ibmdlswTConnGroupOperCURexSents=_IbmdlswTConnGroupOperCURexSents_Object((1,3,6,1,4,1,2,6,119,4,3,1,1,11),_IbmdlswTConnGroupOperCURexSents_Type())
ibmdlswTConnGroupOperCURexSents.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlswTConnGroupOperCURexSents.setStatus(_A)
_IbmdlswTConnGroupOperICRexRcvds_Type=Counter32
_IbmdlswTConnGroupOperICRexRcvds_Object=MibTableColumn
ibmdlswTConnGroupOperICRexRcvds=_IbmdlswTConnGroupOperICRexRcvds_Object((1,3,6,1,4,1,2,6,119,4,3,1,1,12),_IbmdlswTConnGroupOperICRexRcvds_Type())
ibmdlswTConnGroupOperICRexRcvds.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlswTConnGroupOperICRexRcvds.setStatus(_A)
_IbmdlswTConnGroupOperCURexRcvds_Type=Counter32
_IbmdlswTConnGroupOperCURexRcvds_Object=MibTableColumn
ibmdlswTConnGroupOperCURexRcvds=_IbmdlswTConnGroupOperCURexRcvds_Object((1,3,6,1,4,1,2,6,119,4,3,1,1,13),_IbmdlswTConnGroupOperCURexRcvds_Type())
ibmdlswTConnGroupOperCURexRcvds.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlswTConnGroupOperCURexRcvds.setStatus(_A)
_IbmdlswTConnGroupOperICRexSents_Type=Counter32
_IbmdlswTConnGroupOperICRexSents_Object=MibTableColumn
ibmdlswTConnGroupOperICRexSents=_IbmdlswTConnGroupOperICRexSents_Object((1,3,6,1,4,1,2,6,119,4,3,1,1,14),_IbmdlswTConnGroupOperICRexSents_Type())
ibmdlswTConnGroupOperICRexSents.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlswTConnGroupOperICRexSents.setStatus(_A)
_IbmdlswTConnGroupOperNQexSents_Type=Counter32
_IbmdlswTConnGroupOperNQexSents_Object=MibTableColumn
ibmdlswTConnGroupOperNQexSents=_IbmdlswTConnGroupOperNQexSents_Object((1,3,6,1,4,1,2,6,119,4,3,1,1,15),_IbmdlswTConnGroupOperNQexSents_Type())
ibmdlswTConnGroupOperNQexSents.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlswTConnGroupOperNQexSents.setStatus(_A)
_IbmdlswTConnGroupOperNRexRcvds_Type=Counter32
_IbmdlswTConnGroupOperNRexRcvds_Object=MibTableColumn
ibmdlswTConnGroupOperNRexRcvds=_IbmdlswTConnGroupOperNRexRcvds_Object((1,3,6,1,4,1,2,6,119,4,3,1,1,16),_IbmdlswTConnGroupOperNRexRcvds_Type())
ibmdlswTConnGroupOperNRexRcvds.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlswTConnGroupOperNRexRcvds.setStatus(_A)
_IbmdlswTConnGroupOperNQexRcvds_Type=Counter32
_IbmdlswTConnGroupOperNQexRcvds_Object=MibTableColumn
ibmdlswTConnGroupOperNQexRcvds=_IbmdlswTConnGroupOperNQexRcvds_Object((1,3,6,1,4,1,2,6,119,4,3,1,1,17),_IbmdlswTConnGroupOperNQexRcvds_Type())
ibmdlswTConnGroupOperNQexRcvds.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlswTConnGroupOperNQexRcvds.setStatus(_A)
_IbmdlswTConnGroupOperNRexSents_Type=Counter32
_IbmdlswTConnGroupOperNRexSents_Object=MibTableColumn
ibmdlswTConnGroupOperNRexSents=_IbmdlswTConnGroupOperNRexSents_Object((1,3,6,1,4,1,2,6,119,4,3,1,1,18),_IbmdlswTConnGroupOperNRexSents_Type())
ibmdlswTConnGroupOperNRexSents.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlswTConnGroupOperNRexSents.setStatus(_A)
_IbmdlswQllcLsTable_Object=MibTable
ibmdlswQllcLsTable=_IbmdlswQllcLsTable_Object((1,3,6,1,4,1,2,6,119,4,3,2))
if mibBuilder.loadTexts:ibmdlswQllcLsTable.setStatus(_A)
_IbmdlswQllcLsEntry_Object=MibTableRow
ibmdlswQllcLsEntry=_IbmdlswQllcLsEntry_Object((1,3,6,1,4,1,2,6,119,4,3,2,1))
ibmdlswQllcLsEntry.setIndexNames((0,_D,_p),(0,_D,_q),(0,_D,_r))
if mibBuilder.loadTexts:ibmdlswQllcLsEntry.setStatus(_A)
_IbmdlswQllcLsIfIndex_Type=Integer32
_IbmdlswQllcLsIfIndex_Object=MibTableColumn
ibmdlswQllcLsIfIndex=_IbmdlswQllcLsIfIndex_Object((1,3,6,1,4,1,2,6,119,4,3,2,1,1),_IbmdlswQllcLsIfIndex_Type())
ibmdlswQllcLsIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlswQllcLsIfIndex.setStatus(_A)
class _IbmdlswQllcLsQdomain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pvc',1),('svc',2)))
_IbmdlswQllcLsQdomain_Type.__name__=_C
_IbmdlswQllcLsQdomain_Object=MibTableColumn
ibmdlswQllcLsQdomain=_IbmdlswQllcLsQdomain_Object((1,3,6,1,4,1,2,6,119,4,3,2,1,2),_IbmdlswQllcLsQdomain_Type())
ibmdlswQllcLsQdomain.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlswQllcLsQdomain.setStatus(_A)
class _IbmdlswQllcLsQaddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_IbmdlswQllcLsQaddress_Type.__name__=_E
_IbmdlswQllcLsQaddress_Object=MibTableColumn
ibmdlswQllcLsQaddress=_IbmdlswQllcLsQaddress_Object((1,3,6,1,4,1,2,6,119,4,3,2,1,3),_IbmdlswQllcLsQaddress_Type())
ibmdlswQllcLsQaddress.setMaxAccess(_G)
if mibBuilder.loadTexts:ibmdlswQllcLsQaddress.setStatus(_A)
class _IbmdlswQllcLsChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_IbmdlswQllcLsChannel_Type.__name__=_C
_IbmdlswQllcLsChannel_Object=MibTableColumn
ibmdlswQllcLsChannel=_IbmdlswQllcLsChannel_Object((1,3,6,1,4,1,2,6,119,4,3,2,1,4),_IbmdlswQllcLsChannel_Type())
ibmdlswQllcLsChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlswQllcLsChannel.setStatus(_A)
_IbmdlswQllcLsLocalMac_Type=MacAddressNCIROC
_IbmdlswQllcLsLocalMac_Object=MibTableColumn
ibmdlswQllcLsLocalMac=_IbmdlswQllcLsLocalMac_Object((1,3,6,1,4,1,2,6,119,4,3,2,1,5),_IbmdlswQllcLsLocalMac_Type())
ibmdlswQllcLsLocalMac.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlswQllcLsLocalMac.setStatus(_A)
_IbmdlswQllcLsLocalSap_Type=OctetString
_IbmdlswQllcLsLocalSap_Object=MibTableColumn
ibmdlswQllcLsLocalSap=_IbmdlswQllcLsLocalSap_Object((1,3,6,1,4,1,2,6,119,4,3,2,1,6),_IbmdlswQllcLsLocalSap_Type())
ibmdlswQllcLsLocalSap.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlswQllcLsLocalSap.setStatus(_A)
_IbmdlswQllcLsRemoteMac_Type=MacAddressNCIROC
_IbmdlswQllcLsRemoteMac_Object=MibTableColumn
ibmdlswQllcLsRemoteMac=_IbmdlswQllcLsRemoteMac_Object((1,3,6,1,4,1,2,6,119,4,3,2,1,7),_IbmdlswQllcLsRemoteMac_Type())
ibmdlswQllcLsRemoteMac.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlswQllcLsRemoteMac.setStatus(_A)
_IbmdlswQllcLsRemoteSap_Type=OctetString
_IbmdlswQllcLsRemoteSap_Object=MibTableColumn
ibmdlswQllcLsRemoteSap=_IbmdlswQllcLsRemoteSap_Object((1,3,6,1,4,1,2,6,119,4,3,2,1,8),_IbmdlswQllcLsRemoteSap_Type())
ibmdlswQllcLsRemoteSap.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlswQllcLsRemoteSap.setStatus(_A)
class _IbmdlswQllcLsPuType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5,6)));namedValues=NamedValues(*(('type1',1),('type2',2),('type4',4),('type5',5),('other',6)))
_IbmdlswQllcLsPuType_Type.__name__=_C
_IbmdlswQllcLsPuType_Object=MibTableColumn
ibmdlswQllcLsPuType=_IbmdlswQllcLsPuType_Object((1,3,6,1,4,1,2,6,119,4,3,2,1,9),_IbmdlswQllcLsPuType_Type())
ibmdlswQllcLsPuType.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlswQllcLsPuType.setStatus(_A)
class _IbmdlswQllcLsBlkNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_IbmdlswQllcLsBlkNum_Type.__name__=_R
_IbmdlswQllcLsBlkNum_Object=MibTableColumn
ibmdlswQllcLsBlkNum=_IbmdlswQllcLsBlkNum_Object((1,3,6,1,4,1,2,6,119,4,3,2,1,10),_IbmdlswQllcLsBlkNum_Type())
ibmdlswQllcLsBlkNum.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlswQllcLsBlkNum.setStatus(_A)
class _IbmdlswQllcLsIdNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_IbmdlswQllcLsIdNum_Type.__name__=_R
_IbmdlswQllcLsIdNum_Object=MibTableColumn
ibmdlswQllcLsIdNum=_IbmdlswQllcLsIdNum_Object((1,3,6,1,4,1,2,6,119,4,3,2,1,11),_IbmdlswQllcLsIdNum_Type())
ibmdlswQllcLsIdNum.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlswQllcLsIdNum.setStatus(_A)
_IbmIROCroutingfr_ObjectIdentity=ObjectIdentity
ibmIROCroutingfr=_IbmIROCroutingfr_ObjectIdentity((1,3,6,1,4,1,2,6,119,4,4))
_FrCLLMStatsTable_Object=MibTable
frCLLMStatsTable=_FrCLLMStatsTable_Object((1,3,6,1,4,1,2,6,119,4,4,1))
if mibBuilder.loadTexts:frCLLMStatsTable.setStatus(_A)
_FrCLLMStatsEntry_Object=MibTableRow
frCLLMStatsEntry=_FrCLLMStatsEntry_Object((1,3,6,1,4,1,2,6,119,4,4,1,1))
frCLLMStatsEntry.setIndexNames((0,_D,_s),(0,_D,_t))
if mibBuilder.loadTexts:frCLLMStatsEntry.setStatus(_A)
_FrCLLMStatsIfIndex_Type=Integer32
_FrCLLMStatsIfIndex_Object=MibTableColumn
frCLLMStatsIfIndex=_FrCLLMStatsIfIndex_Object((1,3,6,1,4,1,2,6,119,4,4,1,1,1),_FrCLLMStatsIfIndex_Type())
frCLLMStatsIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:frCLLMStatsIfIndex.setStatus(_A)
_FrCLLMStatsDlci_Type=Integer32
_FrCLLMStatsDlci_Object=MibTableColumn
frCLLMStatsDlci=_FrCLLMStatsDlci_Object((1,3,6,1,4,1,2,6,119,4,4,1,1,2),_FrCLLMStatsDlci_Type())
frCLLMStatsDlci.setMaxAccess(_B)
if mibBuilder.loadTexts:frCLLMStatsDlci.setStatus(_A)
_FrCLLMStatsRcvds_Type=Counter32
_FrCLLMStatsRcvds_Object=MibTableColumn
frCLLMStatsRcvds=_FrCLLMStatsRcvds_Object((1,3,6,1,4,1,2,6,119,4,4,1,1,3),_FrCLLMStatsRcvds_Type())
frCLLMStatsRcvds.setMaxAccess(_B)
if mibBuilder.loadTexts:frCLLMStatsRcvds.setStatus(_A)
_FrCLLMCauseTable_Object=MibTable
frCLLMCauseTable=_FrCLLMCauseTable_Object((1,3,6,1,4,1,2,6,119,4,4,2))
if mibBuilder.loadTexts:frCLLMCauseTable.setStatus(_A)
_FrCLLMCauseEntry_Object=MibTableRow
frCLLMCauseEntry=_FrCLLMCauseEntry_Object((1,3,6,1,4,1,2,6,119,4,4,2,1))
frCLLMCauseEntry.setIndexNames((0,_D,_S))
if mibBuilder.loadTexts:frCLLMCauseEntry.setStatus(_A)
_FrCLLMCauseIfIndex_Type=Integer32
_FrCLLMCauseIfIndex_Object=MibTableColumn
frCLLMCauseIfIndex=_FrCLLMCauseIfIndex_Object((1,3,6,1,4,1,2,6,119,4,4,2,1,1),_FrCLLMCauseIfIndex_Type())
frCLLMCauseIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:frCLLMCauseIfIndex.setStatus(_A)
_FrCLLMCauseCode_Type=Integer32
_FrCLLMCauseCode_Object=MibTableColumn
frCLLMCauseCode=_FrCLLMCauseCode_Object((1,3,6,1,4,1,2,6,119,4,4,2,1,2),_FrCLLMCauseCode_Type())
frCLLMCauseCode.setMaxAccess(_B)
if mibBuilder.loadTexts:frCLLMCauseCode.setStatus(_A)
_FrSimpleObjs_ObjectIdentity=ObjectIdentity
frSimpleObjs=_FrSimpleObjs_ObjectIdentity((1,3,6,1,4,1,2,6,119,4,4,3))
class _FrCLLMDlciList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1024))
_FrCLLMDlciList_Type.__name__=_E
_FrCLLMDlciList_Object=MibScalar
frCLLMDlciList=_FrCLLMDlciList_Object((1,3,6,1,4,1,2,6,119,4,4,3,1),_FrCLLMDlciList_Type())
frCLLMDlciList.setMaxAccess(_B)
if mibBuilder.loadTexts:frCLLMDlciList.setStatus(_A)
class _FrTrapStateFECN_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_FrTrapStateFECN_Type.__name__=_C
_FrTrapStateFECN_Object=MibScalar
frTrapStateFECN=_FrTrapStateFECN_Object((1,3,6,1,4,1,2,6,119,4,4,3,2),_FrTrapStateFECN_Type())
frTrapStateFECN.setMaxAccess(_G)
if mibBuilder.loadTexts:frTrapStateFECN.setStatus(_A)
class _FrTrapStateBECN_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_FrTrapStateBECN_Type.__name__=_C
_FrTrapStateBECN_Object=MibScalar
frTrapStateBECN=_FrTrapStateBECN_Object((1,3,6,1,4,1,2,6,119,4,4,3,3),_FrTrapStateBECN_Type())
frTrapStateBECN.setMaxAccess(_G)
if mibBuilder.loadTexts:frTrapStateBECN.setStatus(_A)
class _FrTrapStateCLLM_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_FrTrapStateCLLM_Type.__name__=_C
_FrTrapStateCLLM_Object=MibScalar
frTrapStateCLLM=_FrTrapStateCLLM_Object((1,3,6,1,4,1,2,6,119,4,4,3,4),_FrTrapStateCLLM_Type())
frTrapStateCLLM.setMaxAccess(_G)
if mibBuilder.loadTexts:frTrapStateCLLM.setStatus(_A)
_IbmIROCfrBRS_ObjectIdentity=ObjectIdentity
ibmIROCfrBRS=_IbmIROCfrBRS_ObjectIdentity((1,3,6,1,4,1,2,6,119,4,4,4))
_IbmIROCfrcircuit_ObjectIdentity=ObjectIdentity
ibmIROCfrcircuit=_IbmIROCfrcircuit_ObjectIdentity((1,3,6,1,4,1,2,6,119,4,4,5))
_IbmIROCroutingRlan_ObjectIdentity=ObjectIdentity
ibmIROCroutingRlan=_IbmIROCroutingRlan_ObjectIdentity((1,3,6,1,4,1,2,6,119,4,5))
_IbmIROCroutingDialOut_ObjectIdentity=ObjectIdentity
ibmIROCroutingDialOut=_IbmIROCroutingDialOut_ObjectIdentity((1,3,6,1,4,1,2,6,119,4,6))
_IbmIROCroutingl2tp_ObjectIdentity=ObjectIdentity
ibmIROCroutingl2tp=_IbmIROCroutingl2tp_ObjectIdentity((1,3,6,1,4,1,2,6,119,4,7))
_IbmCacheServer_ObjectIdentity=ObjectIdentity
ibmCacheServer=_IbmCacheServer_ObjectIdentity((1,3,6,1,4,1,2,6,119,4,8))
_IbmIROCroutingIpSec_ObjectIdentity=ObjectIdentity
ibmIROCroutingIpSec=_IbmIROCroutingIpSec_ObjectIdentity((1,3,6,1,4,1,2,6,119,4,9))
_IbmIROCswhw_ObjectIdentity=ObjectIdentity
ibmIROCswhw=_IbmIROCswhw_ObjectIdentity((1,3,6,1,4,1,2,6,119,4,10))
_IbmWanRestoralRerouteMIB_ObjectIdentity=ObjectIdentity
ibmWanRestoralRerouteMIB=_IbmWanRestoralRerouteMIB_ObjectIdentity((1,3,6,1,4,1,2,6,119,4,11))
_IbmBANMIB_ObjectIdentity=ObjectIdentity
ibmBANMIB=_IbmBANMIB_ObjectIdentity((1,3,6,1,4,1,2,6,119,4,12))
_IbmIROCrmon_ObjectIdentity=ObjectIdentity
ibmIROCrmon=_IbmIROCrmon_ObjectIdentity((1,3,6,1,4,1,2,6,119,4,13))
_IbmIROCescon_ObjectIdentity=ObjectIdentity
ibmIROCescon=_IbmIROCescon_ObjectIdentity((1,3,6,1,4,1,2,6,119,4,14))
_IbmIROCVPNpolicy_ObjectIdentity=ObjectIdentity
ibmIROCVPNpolicy=_IbmIROCVPNpolicy_ObjectIdentity((1,3,6,1,4,1,2,6,119,4,15))
_IbmIROCroutingvoice_ObjectIdentity=ObjectIdentity
ibmIROCroutingvoice=_IbmIROCroutingvoice_ObjectIdentity((1,3,6,1,4,1,2,6,119,4,16))
_IbmIROCroutinginterface_ObjectIdentity=ObjectIdentity
ibmIROCroutinginterface=_IbmIROCroutinginterface_ObjectIdentity((1,3,6,1,4,1,2,6,119,4,17))
_IbmIROCroutingtn3270e_ObjectIdentity=ObjectIdentity
ibmIROCroutingtn3270e=_IbmIROCroutingtn3270e_ObjectIdentity((1,3,6,1,4,1,2,6,119,4,18))
_IbmIROCroutingtcpip_ObjectIdentity=ObjectIdentity
ibmIROCroutingtcpip=_IbmIROCroutingtcpip_ObjectIdentity((1,3,6,1,4,1,2,6,119,4,20))
_TcpiprouteTabSize_Type=Integer32
_TcpiprouteTabSize_Object=MibScalar
tcpiprouteTabSize=_TcpiprouteTabSize_Object((1,3,6,1,4,1,2,6,119,4,20,1),_TcpiprouteTabSize_Type())
tcpiprouteTabSize.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpiprouteTabSize.setStatus(_A)
_TcpiprouteTabUsed_Type=Gauge32
_TcpiprouteTabUsed_Object=MibScalar
tcpiprouteTabUsed=_TcpiprouteTabUsed_Object((1,3,6,1,4,1,2,6,119,4,20,2),_TcpiprouteTabUsed_Type())
tcpiprouteTabUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpiprouteTabUsed.setStatus(_A)
_TcpiprouteCacheSize_Type=Integer32
_TcpiprouteCacheSize_Object=MibScalar
tcpiprouteCacheSize=_TcpiprouteCacheSize_Object((1,3,6,1,4,1,2,6,119,4,20,3),_TcpiprouteCacheSize_Type())
tcpiprouteCacheSize.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpiprouteCacheSize.setStatus(_A)
_TcpiprouteCacheUsed_Type=Gauge32
_TcpiprouteCacheUsed_Object=MibScalar
tcpiprouteCacheUsed=_TcpiprouteCacheUsed_Object((1,3,6,1,4,1,2,6,119,4,20,4),_TcpiprouteCacheUsed_Type())
tcpiprouteCacheUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpiprouteCacheUsed.setStatus(_A)
_TcpiprouteOverFlow_Type=Counter32
_TcpiprouteOverFlow_Object=MibScalar
tcpiprouteOverFlow=_TcpiprouteOverFlow_Object((1,3,6,1,4,1,2,6,119,4,20,5),_TcpiprouteOverFlow_Type())
tcpiprouteOverFlow.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpiprouteOverFlow.setStatus(_A)
_TcpiprouteNoReach_Type=Counter32
_TcpiprouteNoReach_Object=MibScalar
tcpiprouteNoReach=_TcpiprouteNoReach_Object((1,3,6,1,4,1,2,6,119,4,20,6),_TcpiprouteNoReach_Type())
tcpiprouteNoReach.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpiprouteNoReach.setStatus(_A)
_TcpiprouteBadSubnet_Type=Counter32
_TcpiprouteBadSubnet_Object=MibScalar
tcpiprouteBadSubnet=_TcpiprouteBadSubnet_Object((1,3,6,1,4,1,2,6,119,4,20,7),_TcpiprouteBadSubnet_Type())
tcpiprouteBadSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpiprouteBadSubnet.setStatus(_A)
_TcpiprouteBadNet_Type=Counter32
_TcpiprouteBadNet_Object=MibScalar
tcpiprouteBadNet=_TcpiprouteBadNet_Object((1,3,6,1,4,1,2,6,119,4,20,8),_TcpiprouteBadNet_Type())
tcpiprouteBadNet.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpiprouteBadNet.setStatus(_A)
_TcpiprouteUnhBcast_Type=Counter32
_TcpiprouteUnhBcast_Object=MibScalar
tcpiprouteUnhBcast=_TcpiprouteUnhBcast_Object((1,3,6,1,4,1,2,6,119,4,20,9),_TcpiprouteUnhBcast_Type())
tcpiprouteUnhBcast.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpiprouteUnhBcast.setStatus(_A)
_TcpiprouteUnhMcast_Type=Counter32
_TcpiprouteUnhMcast_Object=MibScalar
tcpiprouteUnhMcast=_TcpiprouteUnhMcast_Object((1,3,6,1,4,1,2,6,119,4,20,10),_TcpiprouteUnhMcast_Type())
tcpiprouteUnhMcast.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpiprouteUnhMcast.setStatus(_A)
_TcpiprouteUnhDirBcast_Type=Counter32
_TcpiprouteUnhDirBcast_Object=MibScalar
tcpiprouteUnhDirBcast=_TcpiprouteUnhDirBcast_Object((1,3,6,1,4,1,2,6,119,4,20,11),_TcpiprouteUnhDirBcast_Type())
tcpiprouteUnhDirBcast.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpiprouteUnhDirBcast.setStatus(_A)
_TcpiprouteUnhLLbcast_Type=Counter32
_TcpiprouteUnhLLbcast_Object=MibScalar
tcpiprouteUnhLLbcast=_TcpiprouteUnhLLbcast_Object((1,3,6,1,4,1,2,6,119,4,20,12),_TcpiprouteUnhLLbcast_Type())
tcpiprouteUnhLLbcast.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpiprouteUnhLLbcast.setStatus(_A)
_TcpiprouteDiscFilt_Type=Counter32
_TcpiprouteDiscFilt_Object=MibScalar
tcpiprouteDiscFilt=_TcpiprouteDiscFilt_Object((1,3,6,1,4,1,2,6,119,4,20,13),_TcpiprouteDiscFilt_Type())
tcpiprouteDiscFilt.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpiprouteDiscFilt.setStatus(_A)
_TcpiprouteMultRcvd_Type=Counter32
_TcpiprouteMultRcvd_Object=MibScalar
tcpiprouteMultRcvd=_TcpiprouteMultRcvd_Object((1,3,6,1,4,1,2,6,119,4,20,14),_TcpiprouteMultRcvd_Type())
tcpiprouteMultRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpiprouteMultRcvd.setStatus(_A)
_TcpCurrConnections_Type=Gauge32
_TcpCurrConnections_Object=MibScalar
tcpCurrConnections=_TcpCurrConnections_Object((1,3,6,1,4,1,2,6,119,4,20,15),_TcpCurrConnections_Type())
tcpCurrConnections.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpCurrConnections.setStatus(_A)
_TcpMaxConnections_Type=Integer32
_TcpMaxConnections_Object=MibScalar
tcpMaxConnections=_TcpMaxConnections_Object((1,3,6,1,4,1,2,6,119,4,20,16),_TcpMaxConnections_Type())
tcpMaxConnections.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpMaxConnections.setStatus(_A)
_ServerCurrConnections_Type=Gauge32
_ServerCurrConnections_Object=MibScalar
serverCurrConnections=_ServerCurrConnections_Object((1,3,6,1,4,1,2,6,119,4,20,17),_ServerCurrConnections_Type())
serverCurrConnections.setMaxAccess(_B)
if mibBuilder.loadTexts:serverCurrConnections.setStatus(_A)
_ServerMaxConnections_Type=Integer32
_ServerMaxConnections_Object=MibScalar
serverMaxConnections=_ServerMaxConnections_Object((1,3,6,1,4,1,2,6,119,4,20,18),_ServerMaxConnections_Type())
serverMaxConnections.setMaxAccess(_B)
if mibBuilder.loadTexts:serverMaxConnections.setStatus(_A)
_IbmIROCswitching_ObjectIdentity=ObjectIdentity
ibmIROCswitching=_IbmIROCswitching_ObjectIdentity((1,3,6,1,4,1,2,6,119,5))
_IbmIROCtraps_ObjectIdentity=ObjectIdentity
ibmIROCtraps=_IbmIROCtraps_ObjectIdentity((1,3,6,1,4,1,2,6,119,6))
_IbmIROCtrapsfr_ObjectIdentity=ObjectIdentity
ibmIROCtrapsfr=_IbmIROCtrapsfr_ObjectIdentity((1,3,6,1,4,1,2,6,119,6,1))
_IbmIROCtrapssys_ObjectIdentity=ObjectIdentity
ibmIROCtrapssys=_IbmIROCtrapssys_ObjectIdentity((1,3,6,1,4,1,2,6,119,6,2))
_IbmIROCtrapsels_ObjectIdentity=ObjectIdentity
ibmIROCtrapsels=_IbmIROCtrapsels_ObjectIdentity((1,3,6,1,4,1,2,6,119,6,3))
_IbmIROCconfig_ObjectIdentity=ObjectIdentity
ibmIROCconfig=_IbmIROCconfig_ObjectIdentity((1,3,6,1,4,1,2,6,119,7))
_IbmIROCconfigAuth_ObjectIdentity=ObjectIdentity
ibmIROCconfigAuth=_IbmIROCconfigAuth_ObjectIdentity((1,3,6,1,4,1,2,6,119,7,2))
class _IbmIROCconfigWrite_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noaction',1),('write',2)))
_IbmIROCconfigWrite_Type.__name__=_C
_IbmIROCconfigWrite_Object=MibScalar
ibmIROCconfigWrite=_IbmIROCconfigWrite_Object((1,3,6,1,4,1,2,6,119,7,4),_IbmIROCconfigWrite_Type())
ibmIROCconfigWrite.setMaxAccess(_G)
if mibBuilder.loadTexts:ibmIROCconfigWrite.setStatus(_A)
frrcvdFECN=NotificationType((1,3,6,1,4,1,2,6,119,6,1,0,1))
frrcvdFECN.setObjects(*((_F,_Q),(_F,_P)))
if mibBuilder.loadTexts:frrcvdFECN.setStatus('')
frrcvdBECN=NotificationType((1,3,6,1,4,1,2,6,119,6,1,0,2))
frrcvdBECN.setObjects(*((_F,_Q),(_F,_P)))
if mibBuilder.loadTexts:frrcvdBECN.setStatus('')
frrcvdCLLM=NotificationType((1,3,6,1,4,1,2,6,119,6,1,0,3))
frrcvdCLLM.setObjects(*((_D,_S),(_D,_u),(_D,_v)))
if mibBuilder.loadTexts:frrcvdCLLM.setStatus('')
mosMemLow=NotificationType((1,3,6,1,4,1,2,6,119,6,2,0,1))
mosMemLow.setObjects(*((_H,_X),(_H,_W)))
if mibBuilder.loadTexts:mosMemLow.setStatus('')
elsTrap=NotificationType((1,3,6,1,4,1,2,6,119,6,3,0,2))
elsTrap.setObjects((_H,_V))
if mibBuilder.loadTexts:elsTrap.setStatus('')
mibBuilder.exportSymbols(_D,**{'MacAddressNCIROC':MacAddressNCIROC,'ibm':ibm,'ibmProd':ibmProd,'ibmIROC':ibmIROC,'ibmIROCadmin':ibmIROCadmin,'ibmIROCadminproducts':ibmIROCadminproducts,'ibmIROCadminOID':ibmIROCadminOID,'ibmIROCadminDebug':ibmIROCadminDebug,'ibmIROCAgentDebug':ibmIROCAgentDebug,'agentMemUse':agentMemUse,'ibmIROCadminSnmp':ibmIROCadminSnmp,'ibmIROCSnmpAuthFail':ibmIROCSnmpAuthFail,'authTrapSourceIPAddr':authTrapSourceIPAddr,'ibmIROCsystem':ibmIROCsystem,'ibmIROCsystemInfo':ibmIROCsystemInfo,'ibmIROCcfgInfo':ibmIROCcfgInfo,'ibmIROCdumpInfo':ibmIROCdumpInfo,'ibmSysDumpTable':ibmSysDumpTable,'ibmSysDumpEntry':ibmSysDumpEntry,_Z:ibmSysDumpIndex,'ibmSysDumpFileName':ibmSysDumpFileName,'ibmSysDumpFileDate':ibmSysDumpFileDate,'ibmSysDumpBuild':ibmSysDumpBuild,'ibmSysDumpBuilder':ibmSysDumpBuilder,'ibmSysDumpBuildName':ibmSysDumpBuildName,'ibmSysDumpRetainName':ibmSysDumpRetainName,'ibmSysDumpProductNumber':ibmSysDumpProductNumber,'ibmSysDumpBuildDate':ibmSysDumpBuildDate,'ibmSysDumpFatalMsg1':ibmSysDumpFatalMsg1,'ibmSysDumpFatalMsg2':ibmSysDumpFatalMsg2,'ibmSysDumpFatalMsg3':ibmSysDumpFatalMsg3,'ibmSysDumpFatalMsg4':ibmSysDumpFatalMsg4,'ibmSysDumpFatalMsg5':ibmSysDumpFatalMsg5,'ibmSysDumpRemoteIPAddr':ibmSysDumpRemoteIPAddr,'ibmSysDumpRemotePath':ibmSysDumpRemotePath,'ibmIROChardware':ibmIROChardware,'ibmIROChardwareInfo':ibmIROChardwareInfo,'platformType':platformType,'platformDRAMSize':platformDRAMSize,'platformFLASHSize':platformFLASHSize,'platformNVRAMSize':platformNVRAMSize,'platformFeatureSlot':platformFeatureSlot,'ibmIROCrouting':ibmIROCrouting,'ibmIROCroutingppp':ibmIROCroutingppp,'pppProtocolTable':pppProtocolTable,'pppProtocolEntry':pppProtocolEntry,_a:pppProtocolIfIndex,_b:pppProtocolId,'pppProtocolRegistered':pppProtocolRegistered,'pppProtocolState':pppProtocolState,'pppProtocolPreviousState':pppProtocolPreviousState,'pppProtocolLastTimeChange':pppProtocolLastTimeChange,'pppProtocolCtlInRejects':pppProtocolCtlInRejects,'pppProtocolCtlInOctets':pppProtocolCtlInOctets,'pppProtocolCtlInPkts':pppProtocolCtlInPkts,'pppProtocolCtlOutOctets':pppProtocolCtlOutOctets,'pppProtocolCtlOutPkts':pppProtocolCtlOutPkts,'pppProtocolDataInRejects':pppProtocolDataInRejects,'pppProtocolDataInOctets':pppProtocolDataInOctets,'pppProtocolDataInPkts':pppProtocolDataInPkts,'pppProtocolDataOutOctets':pppProtocolDataOutOctets,'pppProtocolDataOutPkts':pppProtocolDataOutPkts,'pppLinkErrTable':pppLinkErrTable,'pppLinkErrEntry':pppLinkErrEntry,_c:pppLinkErrIfIndex,'pppLinkErrBadAddrs':pppLinkErrBadAddrs,'pppLinkErrLastBadAddr':pppLinkErrLastBadAddr,'pppLinkErrBadCtrls':pppLinkErrBadCtrls,'pppLinkErrLastBadCtrl':pppLinkErrLastBadCtrl,'pppLinkErrUnkProtos':pppLinkErrUnkProtos,'pppLinkErrLastUnkProto':pppLinkErrLastUnkProto,'pppLinkErrInvProtos':pppLinkErrInvProtos,'pppLinkErrLastInvProto':pppLinkErrLastInvProto,'pppLinkErrConfigTOs':pppLinkErrConfigTOs,'pppLinkErrTermTOs':pppLinkErrTermTOs,'pppLCProtoTable':pppLCProtoTable,'pppLCProtoEntry':pppLCProtoEntry,_d:pppLCProtoIfIndex,'pppLCProtoState':pppLCProtoState,'pppLCProtoPreviousState':pppLCProtoPreviousState,'pppLCProtoLastTimeChange':pppLCProtoLastTimeChange,'pppLCProtoOutPackets':pppLCProtoOutPackets,'pppLCProtoOutOctets':pppLCProtoOutOctets,'pppLCProtoOutCRs':pppLCProtoOutCRs,'pppLCProtoOutCAs':pppLCProtoOutCAs,'pppLCProtoOutCNs':pppLCProtoOutCNs,'pppLCProtoOutCRejs':pppLCProtoOutCRejs,'pppLCProtoOutTRs':pppLCProtoOutTRs,'pppLCProtoOutTAs':pppLCProtoOutTAs,'pppLCProtoOutCodeRejs':pppLCProtoOutCodeRejs,'pppLCProtoOutEchoReqs':pppLCProtoOutEchoReqs,'pppLCProtoOutEchoReps':pppLCProtoOutEchoReps,'pppLCProtoOutDiscReqs':pppLCProtoOutDiscReqs,'pppLCProtoOutResetReqs':pppLCProtoOutResetReqs,'pppLCProtoOutResetAcks':pppLCProtoOutResetAcks,'pppLCProtoOutIdents':pppLCProtoOutIdents,'pppLCProtoOutTimeRemains':pppLCProtoOutTimeRemains,'pppLCProtoInRejects':pppLCProtoInRejects,'pppLCProtoInPackets':pppLCProtoInPackets,'pppLCProtoInOctets':pppLCProtoInOctets,'pppLCProtoInCRs':pppLCProtoInCRs,'pppLCProtoInCAs':pppLCProtoInCAs,'pppLCProtoInCNs':pppLCProtoInCNs,'pppLCProtoInCRejs':pppLCProtoInCRejs,'pppLCProtoInTRs':pppLCProtoInTRs,'pppLCProtoInTAs':pppLCProtoInTAs,'pppLCProtoInCodeRejs':pppLCProtoInCodeRejs,'pppLCProtoInEchoReqs':pppLCProtoInEchoReqs,'pppLCProtoInEchoReps':pppLCProtoInEchoReps,'pppLCProtoInDiscReqs':pppLCProtoInDiscReqs,'pppLCProtoInResetReqs':pppLCProtoInResetReqs,'pppLCProtoInResetAcks':pppLCProtoInResetAcks,'pppLCProtoInIdents':pppLCProtoInIdents,'pppLCProtoInTimeRemains':pppLCProtoInTimeRemains,'pppPAPTable':pppPAPTable,'pppPAPEntry':pppPAPEntry,_e:pppPAPIfIndex,'pppPAPInPackets':pppPAPInPackets,'pppPAPInOctets':pppPAPInOctets,'pppPAPInRequests':pppPAPInRequests,'pppPAPInAcks':pppPAPInAcks,'pppPAPInNacks':pppPAPInNacks,'pppPAPOutPackets':pppPAPOutPackets,'pppPAPOutOctets':pppPAPOutOctets,'pppPAPOutRequests':pppPAPOutRequests,'pppPAPOutAcks':pppPAPOutAcks,'pppPAPOutNacks':pppPAPOutNacks,'pppCHAPTable':pppCHAPTable,'pppCHAPEntry':pppCHAPEntry,_f:pppCHAPIfIndex,'pppCHAPInPackets':pppCHAPInPackets,'pppCHAPInOctets':pppCHAPInOctets,'pppCHAPInChallenges':pppCHAPInChallenges,'pppCHAPInResponses':pppCHAPInResponses,'pppCHAPInSuccesses':pppCHAPInSuccesses,'pppCHAPInFailures':pppCHAPInFailures,'pppCHAPOutPackets':pppCHAPOutPackets,'pppCHAPOutOctets':pppCHAPOutOctets,'pppCHAPOutChallenges':pppCHAPOutChallenges,'pppCHAPOutResponses':pppCHAPOutResponses,'pppCHAPOutSuccesses':pppCHAPOutSuccesses,'pppCHAPOutFailures':pppCHAPOutFailures,'pppSPAPTable':pppSPAPTable,'pppSPAPEntry':pppSPAPEntry,_g:pppSPAPIfIndex,'pppSPAPInPackets':pppSPAPInPackets,'pppSPAPInOctets':pppSPAPInOctets,'pppSPAPInRequests':pppSPAPInRequests,'pppSPAPInAcks':pppSPAPInAcks,'pppSPAPInNacks':pppSPAPInNacks,'pppSPAPInDialbacks':pppSPAPInDialbacks,'pppSPAPInPleaseAuthenticates':pppSPAPInPleaseAuthenticates,'pppSPAPInChangePasswords':pppSPAPInChangePasswords,'pppSPAPInAlerts':pppSPAPInAlerts,'pppSPAPInAlertAcks':pppSPAPInAlertAcks,'pppSPAPOutPackets':pppSPAPOutPackets,'pppSPAPOutOctets':pppSPAPOutOctets,'pppSPAPOutRequests':pppSPAPOutRequests,'pppSPAPOutAcks':pppSPAPOutAcks,'pppSPAPOutNacks':pppSPAPOutNacks,'pppSPAPOutDialbacks':pppSPAPOutDialbacks,'pppSPAPOutPleaseAuthenticates':pppSPAPOutPleaseAuthenticates,'pppSPAPOutChangePasswords':pppSPAPOutChangePasswords,'pppSPAPOutAlerts':pppSPAPOutAlerts,'pppSPAPOutAlertAcks':pppSPAPOutAlertAcks,'pppBAPTable':pppBAPTable,'pppBAPEntry':pppBAPEntry,_h:pppBAPIfIndex,'pppBAPInCallReqs':pppBAPInCallReqs,'pppBAPInCallAcks':pppBAPInCallAcks,'pppBAPInCallNaks':pppBAPInCallNaks,'pppBAPInCallRejs':pppBAPInCallRejs,'pppBAPInCallBackReqs':pppBAPInCallBackReqs,'pppBAPInCallBackAcks':pppBAPInCallBackAcks,'pppBAPInCallBackNaks':pppBAPInCallBackNaks,'pppBAPInCallBackRejs':pppBAPInCallBackRejs,'pppBAPInDropReqs':pppBAPInDropReqs,'pppBAPInDropAcks':pppBAPInDropAcks,'pppBAPInDropNaks':pppBAPInDropNaks,'pppBAPInDropRejs':pppBAPInDropRejs,'pppBAPInStatSuccs':pppBAPInStatSuccs,'pppBAPInStatFails':pppBAPInStatFails,'pppBAPOutCallReqs':pppBAPOutCallReqs,'pppBAPOutCallAcks':pppBAPOutCallAcks,'pppBAPOutCallNaks':pppBAPOutCallNaks,'pppBAPOutCallRejs':pppBAPOutCallRejs,'pppBAPOutCallBackReqs':pppBAPOutCallBackReqs,'pppBAPOutCallBackAcks':pppBAPOutCallBackAcks,'pppBAPOutCallBackNaks':pppBAPOutCallBackNaks,'pppBAPOutCallBackRejs':pppBAPOutCallBackRejs,'pppBAPOutDropReqs':pppBAPOutDropReqs,'pppBAPOutDropAcks':pppBAPOutDropAcks,'pppBAPOutDropNaks':pppBAPOutDropNaks,'pppBAPOutDropRejs':pppBAPOutDropRejs,'pppBAPOutStatSuccs':pppBAPOutStatSuccs,'pppBAPOutStatFails':pppBAPOutStatFails,'pppCPTable':pppCPTable,'pppCPEntry':pppCPEntry,_i:pppCPIfIndex,'pppCPInCompressedOctets':pppCPInCompressedOctets,'pppCPInInCompressablePkts':pppCPInInCompressablePkts,'pppCPInDestroyeds':pppCPInDestroyeds,'pppCPInCopies':pppCPInCopies,'pppCPOutCompressedOctets':pppCPOutCompressedOctets,'pppCPOutInCompressablePkts':pppCPOutInCompressablePkts,'pppCPOutDestroyeds':pppCPOutDestroyeds,'pppCPOutCopies':pppCPOutCopies,'pppCCPInResetReqs':pppCCPInResetReqs,'pppCCPInResetAcks':pppCCPInResetAcks,'pppCCPInDictResets':pppCCPInDictResets,'pppCCPOutResetReqs':pppCCPOutResetReqs,'pppCCPOutResetAcks':pppCCPOutResetAcks,'pppCCPOutDictResets':pppCCPOutDictResets,'pppCCPPacketDiscards':pppCCPPacketDiscards,'pppCCPOctetDiscards':pppCCPOctetDiscards,'pppEPTable':pppEPTable,'pppEPEntry':pppEPEntry,_j:pppEPIfIndex,'pppEPInEncryptedOctets':pppEPInEncryptedOctets,'pppEPInDestroyeds':pppEPInDestroyeds,'pppEPInCopies':pppEPInCopies,'pppEPOutEncryptedOctets':pppEPOutEncryptedOctets,'pppEPOutDestroyeds':pppEPOutDestroyeds,'pppEPOutCopies':pppEPOutCopies,'pppECPInResetReqs':pppECPInResetReqs,'pppECPInResetAcks':pppECPInResetAcks,'pppECPInDictResets':pppECPInDictResets,'pppECPOutResetReqs':pppECPOutResetReqs,'pppECPOutResetAcks':pppECPOutResetAcks,'pppECPOutDictResets':pppECPOutDictResets,'pppECPPacketDiscards':pppECPPacketDiscards,'pppECPOctetDiscards':pppECPOctetDiscards,'pppMSCHAPTable':pppMSCHAPTable,'pppMSCHAPEntry':pppMSCHAPEntry,_k:pppMSCHAPIfIndex,'pppMSCHAPInPackets':pppMSCHAPInPackets,'pppMSCHAPInOctets':pppMSCHAPInOctets,'pppMSCHAPInChallenges':pppMSCHAPInChallenges,'pppMSCHAPInResponses':pppMSCHAPInResponses,'pppMSCHAPInSuccesses':pppMSCHAPInSuccesses,'pppMSCHAPInFailures':pppMSCHAPInFailures,'pppMSCHAPInChangePasswords':pppMSCHAPInChangePasswords,'pppMSCHAPInRestrictedHoursFailures':pppMSCHAPInRestrictedHoursFailures,'pppMSCHAPInAccountDisabledFailures':pppMSCHAPInAccountDisabledFailures,'pppMSCHAPInPasswordExpiredFailures':pppMSCHAPInPasswordExpiredFailures,'pppMSCHAPInNoPermissionFailures':pppMSCHAPInNoPermissionFailures,'pppMSCHAPInAuthenticationFailures':pppMSCHAPInAuthenticationFailures,'pppMSCHAPInChangePasswordFailures':pppMSCHAPInChangePasswordFailures,'pppMSCHAPOutPackets':pppMSCHAPOutPackets,'pppMSCHAPOutOctets':pppMSCHAPOutOctets,'pppMSCHAPOutChallenges':pppMSCHAPOutChallenges,'pppMSCHAPOutResponses':pppMSCHAPOutResponses,'pppMSCHAPOutSuccesses':pppMSCHAPOutSuccesses,'pppMSCHAPOutFailures':pppMSCHAPOutFailures,'pppMSCHAPOutChangePasswords':pppMSCHAPOutChangePasswords,'pppMSCHAPOutRestrictedHoursFailures':pppMSCHAPOutRestrictedHoursFailures,'pppMSCHAPOutAccountDisabledFailures':pppMSCHAPOutAccountDisabledFailures,'pppMSCHAPOutPasswordExpiredFailures':pppMSCHAPOutPasswordExpiredFailures,'pppMSCHAPOutNoPermissionFailures':pppMSCHAPOutNoPermissionFailures,'pppMSCHAPOutAuthenticationFailures':pppMSCHAPOutAuthenticationFailures,'pppMSCHAPOutChangePasswordFailures':pppMSCHAPOutChangePasswordFailures,'pppCBCPTable':pppCBCPTable,'pppCBCPEntry':pppCBCPEntry,_l:pppCBCPIfIndex,'pppCBCPInPackets':pppCBCPInPackets,'pppCBCPInOctets':pppCBCPInOctets,'pppCBCPOutPackets':pppCBCPOutPackets,'pppCBCPOutOctets':pppCBCPOutOctets,'pppCBCPAttempts':pppCBCPAttempts,'pppCBCPSuccess':pppCBCPSuccess,'pppEAPTable':pppEAPTable,'pppEAPEntry':pppEAPEntry,_m:pppEAPIfIndex,'pppEAPInPackets':pppEAPInPackets,'pppEAPInOctets':pppEAPInOctets,'pppEAPInRequests':pppEAPInRequests,'pppEAPInAcks':pppEAPInAcks,'pppEAPInNaks':pppEAPInNaks,'pppEAPOutPackets':pppEAPOutPackets,'pppEAPOutOctets':pppEAPOutOctets,'pppEAPOutRequests':pppEAPOutRequests,'pppEAPOutAcks':pppEAPOutAcks,'pppEAPOutNaks':pppEAPOutNaks,'pppMPPETable':pppMPPETable,'pppMPPEEntry':pppMPPEEntry,_n:pppMPPEIfIndex,'pppMPPEInPackets':pppMPPEInPackets,'pppMPPEInOctets':pppMPPEInOctets,'pppMPPEInDestroyed':pppMPPEInDestroyed,'pppMPPEOutPackets':pppMPPEOutPackets,'pppMPPEOutOctets':pppMPPEOutOctets,'pppMPPEOutDestroyed':pppMPPEOutDestroyed,'ibmIROCroutingdlsw':ibmIROCroutingdlsw,'ibmdlswTConnGroupOperTable':ibmdlswTConnGroupOperTable,'ibmdlswTConnGroupOperEntry':ibmdlswTConnGroupOperEntry,_o:ibmdlswTConnGroupOperIndex,'ibmdlswTConnGroupOperRole':ibmdlswTConnGroupOperRole,'ibmdlswTConnGroupOperJoinTime':ibmdlswTConnGroupOperJoinTime,'ibmdlswTConnGroupOperConfigIndex':ibmdlswTConnGroupOperConfigIndex,'ibmdlswTConnGroupOperInDataPkts':ibmdlswTConnGroupOperInDataPkts,'ibmdlswTConnGroupOperOutDataPkts':ibmdlswTConnGroupOperOutDataPkts,'ibmdlswTConnGroupOperInDataOctets':ibmdlswTConnGroupOperInDataOctets,'ibmdlswTConnGroupOperOutDataOctets':ibmdlswTConnGroupOperOutDataOctets,'ibmdlswTConnGroupOperInCntlPkts':ibmdlswTConnGroupOperInCntlPkts,'ibmdlswTConnGroupOperOutCntlPkts':ibmdlswTConnGroupOperOutCntlPkts,'ibmdlswTConnGroupOperCURexSents':ibmdlswTConnGroupOperCURexSents,'ibmdlswTConnGroupOperICRexRcvds':ibmdlswTConnGroupOperICRexRcvds,'ibmdlswTConnGroupOperCURexRcvds':ibmdlswTConnGroupOperCURexRcvds,'ibmdlswTConnGroupOperICRexSents':ibmdlswTConnGroupOperICRexSents,'ibmdlswTConnGroupOperNQexSents':ibmdlswTConnGroupOperNQexSents,'ibmdlswTConnGroupOperNRexRcvds':ibmdlswTConnGroupOperNRexRcvds,'ibmdlswTConnGroupOperNQexRcvds':ibmdlswTConnGroupOperNQexRcvds,'ibmdlswTConnGroupOperNRexSents':ibmdlswTConnGroupOperNRexSents,'ibmdlswQllcLsTable':ibmdlswQllcLsTable,'ibmdlswQllcLsEntry':ibmdlswQllcLsEntry,_p:ibmdlswQllcLsIfIndex,_q:ibmdlswQllcLsQdomain,_r:ibmdlswQllcLsQaddress,'ibmdlswQllcLsChannel':ibmdlswQllcLsChannel,'ibmdlswQllcLsLocalMac':ibmdlswQllcLsLocalMac,'ibmdlswQllcLsLocalSap':ibmdlswQllcLsLocalSap,'ibmdlswQllcLsRemoteMac':ibmdlswQllcLsRemoteMac,'ibmdlswQllcLsRemoteSap':ibmdlswQllcLsRemoteSap,'ibmdlswQllcLsPuType':ibmdlswQllcLsPuType,'ibmdlswQllcLsBlkNum':ibmdlswQllcLsBlkNum,'ibmdlswQllcLsIdNum':ibmdlswQllcLsIdNum,'ibmIROCroutingfr':ibmIROCroutingfr,'frCLLMStatsTable':frCLLMStatsTable,'frCLLMStatsEntry':frCLLMStatsEntry,_s:frCLLMStatsIfIndex,_t:frCLLMStatsDlci,'frCLLMStatsRcvds':frCLLMStatsRcvds,'frCLLMCauseTable':frCLLMCauseTable,'frCLLMCauseEntry':frCLLMCauseEntry,_S:frCLLMCauseIfIndex,_u:frCLLMCauseCode,'frSimpleObjs':frSimpleObjs,_v:frCLLMDlciList,'frTrapStateFECN':frTrapStateFECN,'frTrapStateBECN':frTrapStateBECN,'frTrapStateCLLM':frTrapStateCLLM,'ibmIROCfrBRS':ibmIROCfrBRS,'ibmIROCfrcircuit':ibmIROCfrcircuit,'ibmIROCroutingRlan':ibmIROCroutingRlan,'ibmIROCroutingDialOut':ibmIROCroutingDialOut,'ibmIROCroutingl2tp':ibmIROCroutingl2tp,'ibmCacheServer':ibmCacheServer,'ibmIROCroutingIpSec':ibmIROCroutingIpSec,'ibmIROCswhw':ibmIROCswhw,'ibmWanRestoralRerouteMIB':ibmWanRestoralRerouteMIB,'ibmBANMIB':ibmBANMIB,'ibmIROCrmon':ibmIROCrmon,'ibmIROCescon':ibmIROCescon,'ibmIROCVPNpolicy':ibmIROCVPNpolicy,'ibmIROCroutingvoice':ibmIROCroutingvoice,'ibmIROCroutinginterface':ibmIROCroutinginterface,'ibmIROCroutingtn3270e':ibmIROCroutingtn3270e,'ibmIROCroutingtcpip':ibmIROCroutingtcpip,'tcpiprouteTabSize':tcpiprouteTabSize,'tcpiprouteTabUsed':tcpiprouteTabUsed,'tcpiprouteCacheSize':tcpiprouteCacheSize,'tcpiprouteCacheUsed':tcpiprouteCacheUsed,'tcpiprouteOverFlow':tcpiprouteOverFlow,'tcpiprouteNoReach':tcpiprouteNoReach,'tcpiprouteBadSubnet':tcpiprouteBadSubnet,'tcpiprouteBadNet':tcpiprouteBadNet,'tcpiprouteUnhBcast':tcpiprouteUnhBcast,'tcpiprouteUnhMcast':tcpiprouteUnhMcast,'tcpiprouteUnhDirBcast':tcpiprouteUnhDirBcast,'tcpiprouteUnhLLbcast':tcpiprouteUnhLLbcast,'tcpiprouteDiscFilt':tcpiprouteDiscFilt,'tcpiprouteMultRcvd':tcpiprouteMultRcvd,'tcpCurrConnections':tcpCurrConnections,'tcpMaxConnections':tcpMaxConnections,'serverCurrConnections':serverCurrConnections,'serverMaxConnections':serverMaxConnections,'ibmIROCswitching':ibmIROCswitching,'ibmIROCtraps':ibmIROCtraps,'ibmIROCtrapsfr':ibmIROCtrapsfr,'frrcvdFECN':frrcvdFECN,'frrcvdBECN':frrcvdBECN,'frrcvdCLLM':frrcvdCLLM,'ibmIROCtrapssys':ibmIROCtrapssys,'mosMemLow':mosMemLow,'ibmIROCtrapsels':ibmIROCtrapsels,'elsTrap':elsTrap,'ibmIROCconfig':ibmIROCconfig,'ibmIROCconfigAuth':ibmIROCconfigAuth,'ibmIROCconfigWrite':ibmIROCconfigWrite})