_r='nbsMegaSwPermVbcIndex'
_q='nbsMegaSwPermIsvlanIndex'
_p='nbsMegaSwPermSvlanIndex'
_o='nbsMegaSwRunVbcIndex'
_n='nbsMegaSwRunIsvlanIndex'
_m='nbsMegaSwRunSvlanIndex'
_l='nbsMegaSwSvlanConnectSport'
_k='nbsMegaSwRunFilterSport'
_j='nbsMegaSwRunFilterAddr'
_i='customFilter'
_h='virtualFilter'
_g='deleteOnTimeout'
_f='deleteOnReset'
_e='permanent'
_d='system'
_c='nbsMegaSwRunDbIndex'
_b='nbsMgmtXmtPerfOutPort'
_a='nbsMgmtRcvPerfInPort'
_Z='nbsPortFwdPerfOutPort'
_Y='nbsPortFwdPerfInPort'
_X='nbsSwitchPerfIndex'
_W='nbsEthInfoIndex'
_V='nbsPortGrpCfgIndex'
_U='nbsPortCfgIndex'
_T='nbsSysTrapTblEntIndex'
_S='000000000000'
_R='stpEnable'
_Q='stpDisable'
_P='IpAddress'
_O='inactive'
_N='enable'
_M='disable'
_L='MacAddress'
_K='active'
_J='DisplayString'
_I='valid'
_H='ffff'
_G='OctetString'
_F='invalid'
_E='NBASE-G1-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,_P,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','TextualConvention')
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_Nbase_ObjectIdentity=ObjectIdentity
nbase=_Nbase_ObjectIdentity((1,3,6,1,4,1,629))
_NbSwitchG1_ObjectIdentity=ObjectIdentity
nbSwitchG1=_NbSwitchG1_ObjectIdentity((1,3,6,1,4,1,629,1))
_NbsProducts_ObjectIdentity=ObjectIdentity
nbsProducts=_NbsProducts_ObjectIdentity((1,3,6,1,4,1,629,1,1))
_MiniSwitch_ObjectIdentity=ObjectIdentity
miniSwitch=_MiniSwitch_ObjectIdentity((1,3,6,1,4,1,629,1,1,1))
_MegaSwitch208_ObjectIdentity=ObjectIdentity
megaSwitch208=_MegaSwitch208_ObjectIdentity((1,3,6,1,4,1,629,1,1,2))
_MegaSwitch215_ObjectIdentity=ObjectIdentity
megaSwitch215=_MegaSwitch215_ObjectIdentity((1,3,6,1,4,1,629,1,1,3))
_MegaFastSwitch_ObjectIdentity=ObjectIdentity
megaFastSwitch=_MegaFastSwitch_ObjectIdentity((1,3,6,1,4,1,629,1,1,4))
_MegaSwitchII_ObjectIdentity=ObjectIdentity
megaSwitchII=_MegaSwitchII_ObjectIdentity((1,3,6,1,4,1,629,1,1,5))
_MegaSwitch2015_ObjectIdentity=ObjectIdentity
megaSwitch2015=_MegaSwitch2015_ObjectIdentity((1,3,6,1,4,1,629,1,1,6))
_MegaSwitch2048_ObjectIdentity=ObjectIdentity
megaSwitch2048=_MegaSwitch2048_ObjectIdentity((1,3,6,1,4,1,629,1,1,7))
_NbsSys_ObjectIdentity=ObjectIdentity
nbsSys=_NbsSys_ObjectIdentity((1,3,6,1,4,1,629,1,2))
_NbsSysFwVers_Type=DisplayString
_NbsSysFwVers_Object=MibScalar
nbsSysFwVers=_NbsSysFwVers_Object((1,3,6,1,4,1,629,1,2,1),_NbsSysFwVers_Type())
nbsSysFwVers.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSysFwVers.setStatus(_A)
_NbsSysPortsNumber_Type=Integer32
_NbsSysPortsNumber_Object=MibScalar
nbsSysPortsNumber=_NbsSysPortsNumber_Object((1,3,6,1,4,1,629,1,2,2),_NbsSysPortsNumber_Type())
nbsSysPortsNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSysPortsNumber.setStatus(_A)
class _NbsSysRestart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('running',1),('coldRestart',2),('warmRestart',3),('backupRestart',4)))
_NbsSysRestart_Type.__name__=_D
_NbsSysRestart_Object=MibScalar
nbsSysRestart=_NbsSysRestart_Object((1,3,6,1,4,1,629,1,2,3),_NbsSysRestart_Type())
nbsSysRestart.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSysRestart.setStatus(_A)
_NbsSysNumRestarts_Type=Counter32
_NbsSysNumRestarts_Object=MibScalar
nbsSysNumRestarts=_NbsSysNumRestarts_Object((1,3,6,1,4,1,629,1,2,4),_NbsSysNumRestarts_Type())
nbsSysNumRestarts.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSysNumRestarts.setStatus(_A)
class _NbsSysLastError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('noError',1))
_NbsSysLastError_Type.__name__=_D
_NbsSysLastError_Object=MibScalar
nbsSysLastError=_NbsSysLastError_Object((1,3,6,1,4,1,629,1,2,5),_NbsSysLastError_Type())
nbsSysLastError.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSysLastError.setStatus(_A)
_NbsSysErrUptime_Type=TimeTicks
_NbsSysErrUptime_Object=MibScalar
nbsSysErrUptime=_NbsSysErrUptime_Object((1,3,6,1,4,1,629,1,2,6),_NbsSysErrUptime_Type())
nbsSysErrUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSysErrUptime.setStatus(_A)
_NbsSysSwitchDBSize_Type=Integer32
_NbsSysSwitchDBSize_Object=MibScalar
nbsSysSwitchDBSize=_NbsSysSwitchDBSize_Object((1,3,6,1,4,1,629,1,2,7),_NbsSysSwitchDBSize_Type())
nbsSysSwitchDBSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSysSwitchDBSize.setStatus(_A)
class _NbsSysSetNvramDefaults_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('setDefaults',1))
_NbsSysSetNvramDefaults_Type.__name__=_D
_NbsSysSetNvramDefaults_Object=MibScalar
nbsSysSetNvramDefaults=_NbsSysSetNvramDefaults_Object((1,3,6,1,4,1,629,1,2,8),_NbsSysSetNvramDefaults_Type())
nbsSysSetNvramDefaults.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSysSetNvramDefaults.setStatus(_A)
class _NbsSysResetSwitchStats_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('resetStats',1))
_NbsSysResetSwitchStats_Type.__name__=_D
_NbsSysResetSwitchStats_Object=MibScalar
nbsSysResetSwitchStats=_NbsSysResetSwitchStats_Object((1,3,6,1,4,1,629,1,2,9),_NbsSysResetSwitchStats_Type())
nbsSysResetSwitchStats.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSysResetSwitchStats.setStatus(_A)
class _NbsSysStpEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_NbsSysStpEnable_Type.__name__=_D
_NbsSysStpEnable_Object=MibScalar
nbsSysStpEnable=_NbsSysStpEnable_Object((1,3,6,1,4,1,629,1,2,10),_NbsSysStpEnable_Type())
nbsSysStpEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSysStpEnable.setStatus(_A)
class _NbsSysRunStpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_NbsSysRunStpState_Type.__name__=_D
_NbsSysRunStpState_Object=MibScalar
nbsSysRunStpState=_NbsSysRunStpState_Object((1,3,6,1,4,1,629,1,2,11),_NbsSysRunStpState_Type())
nbsSysRunStpState.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSysRunStpState.setStatus(_A)
_NbsSysFrmGen_ObjectIdentity=ObjectIdentity
nbsSysFrmGen=_NbsSysFrmGen_ObjectIdentity((1,3,6,1,4,1,629,1,2,12))
class _NbsSysFrmGenSession_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('idleFG',1),('runFG',2)))
_NbsSysFrmGenSession_Type.__name__=_D
_NbsSysFrmGenSession_Object=MibScalar
nbsSysFrmGenSession=_NbsSysFrmGenSession_Object((1,3,6,1,4,1,629,1,2,12,1),_NbsSysFrmGenSession_Type())
nbsSysFrmGenSession.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSysFrmGenSession.setStatus(_A)
class _NbsSysFrmGenDa_Type(MacAddress):defaultHexValue=_S
_NbsSysFrmGenDa_Type.__name__=_L
_NbsSysFrmGenDa_Object=MibScalar
nbsSysFrmGenDa=_NbsSysFrmGenDa_Object((1,3,6,1,4,1,629,1,2,12,2),_NbsSysFrmGenDa_Type())
nbsSysFrmGenDa.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSysFrmGenDa.setStatus(_A)
class _NbsSysFrmGenSa_Type(MacAddress):defaultHexValue=_S
_NbsSysFrmGenSa_Type.__name__=_L
_NbsSysFrmGenSa_Object=MibScalar
nbsSysFrmGenSa=_NbsSysFrmGenSa_Object((1,3,6,1,4,1,629,1,2,12,3),_NbsSysFrmGenSa_Type())
nbsSysFrmGenSa.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSysFrmGenSa.setStatus(_A)
_NbsSysFrmGenPktFill_Type=Integer32
_NbsSysFrmGenPktFill_Object=MibScalar
nbsSysFrmGenPktFill=_NbsSysFrmGenPktFill_Object((1,3,6,1,4,1,629,1,2,12,4),_NbsSysFrmGenPktFill_Type())
nbsSysFrmGenPktFill.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSysFrmGenPktFill.setStatus(_A)
_NbsSysFrmGenPktRate_Type=Integer32
_NbsSysFrmGenPktRate_Object=MibScalar
nbsSysFrmGenPktRate=_NbsSysFrmGenPktRate_Object((1,3,6,1,4,1,629,1,2,12,5),_NbsSysFrmGenPktRate_Type())
nbsSysFrmGenPktRate.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSysFrmGenPktRate.setStatus(_A)
_NbsSysFrmGenDestMap_Type=OctetString
_NbsSysFrmGenDestMap_Object=MibScalar
nbsSysFrmGenDestMap=_NbsSysFrmGenDestMap_Object((1,3,6,1,4,1,629,1,2,12,6),_NbsSysFrmGenDestMap_Type())
nbsSysFrmGenDestMap.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSysFrmGenDestMap.setStatus(_A)
_NbsSysFrmGenPktNum_Type=Counter32
_NbsSysFrmGenPktNum_Object=MibScalar
nbsSysFrmGenPktNum=_NbsSysFrmGenPktNum_Object((1,3,6,1,4,1,629,1,2,12,7),_NbsSysFrmGenPktNum_Type())
nbsSysFrmGenPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSysFrmGenPktNum.setStatus(_A)
_NbsSysFrmGenPktLen_Type=Integer32
_NbsSysFrmGenPktLen_Object=MibScalar
nbsSysFrmGenPktLen=_NbsSysFrmGenPktLen_Object((1,3,6,1,4,1,629,1,2,12,8),_NbsSysFrmGenPktLen_Type())
nbsSysFrmGenPktLen.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSysFrmGenPktLen.setStatus(_A)
_NbsSysFrmGenXmtPktNum_Type=Counter32
_NbsSysFrmGenXmtPktNum_Object=MibScalar
nbsSysFrmGenXmtPktNum=_NbsSysFrmGenXmtPktNum_Object((1,3,6,1,4,1,629,1,2,12,9),_NbsSysFrmGenXmtPktNum_Type())
nbsSysFrmGenXmtPktNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSysFrmGenXmtPktNum.setStatus(_A)
class _NbsSysSelftestLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ststNone',1),('ststShort',2),('ststLong',3),('ststDiagnostics',4)))
_NbsSysSelftestLevel_Type.__name__=_D
_NbsSysSelftestLevel_Object=MibScalar
nbsSysSelftestLevel=_NbsSysSelftestLevel_Object((1,3,6,1,4,1,629,1,2,13),_NbsSysSelftestLevel_Type())
nbsSysSelftestLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSysSelftestLevel.setStatus(_A)
_NbsSysRomVers_Type=DisplayString
_NbsSysRomVers_Object=MibScalar
nbsSysRomVers=_NbsSysRomVers_Object((1,3,6,1,4,1,629,1,2,14),_NbsSysRomVers_Type())
nbsSysRomVers.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSysRomVers.setStatus(_A)
_NbsSysSnmpCfg_ObjectIdentity=ObjectIdentity
nbsSysSnmpCfg=_NbsSysSnmpCfg_ObjectIdentity((1,3,6,1,4,1,629,1,3))
_NbsSysIpAddr_Type=IpAddress
_NbsSysIpAddr_Object=MibScalar
nbsSysIpAddr=_NbsSysIpAddr_Object((1,3,6,1,4,1,629,1,3,1),_NbsSysIpAddr_Type())
nbsSysIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSysIpAddr.setStatus(_A)
_NbsSysNetMask_Type=IpAddress
_NbsSysNetMask_Object=MibScalar
nbsSysNetMask=_NbsSysNetMask_Object((1,3,6,1,4,1,629,1,3,2),_NbsSysNetMask_Type())
nbsSysNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSysNetMask.setStatus(_A)
_NbsSysBcastAddr_Type=IpAddress
_NbsSysBcastAddr_Object=MibScalar
nbsSysBcastAddr=_NbsSysBcastAddr_Object((1,3,6,1,4,1,629,1,3,3),_NbsSysBcastAddr_Type())
nbsSysBcastAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSysBcastAddr.setStatus(_A)
_NbsSysObIpAddr_Type=IpAddress
_NbsSysObIpAddr_Object=MibScalar
nbsSysObIpAddr=_NbsSysObIpAddr_Object((1,3,6,1,4,1,629,1,3,4),_NbsSysObIpAddr_Type())
nbsSysObIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSysObIpAddr.setStatus(_A)
_NbsSysObNetMask_Type=IpAddress
_NbsSysObNetMask_Object=MibScalar
nbsSysObNetMask=_NbsSysObNetMask_Object((1,3,6,1,4,1,629,1,3,5),_NbsSysObNetMask_Type())
nbsSysObNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSysObNetMask.setStatus(_A)
_NbsSysObBcastAddr_Type=IpAddress
_NbsSysObBcastAddr_Object=MibScalar
nbsSysObBcastAddr=_NbsSysObBcastAddr_Object((1,3,6,1,4,1,629,1,3,6),_NbsSysObBcastAddr_Type())
nbsSysObBcastAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSysObBcastAddr.setStatus(_A)
_NbsSysDefaultGateway_Type=IpAddress
_NbsSysDefaultGateway_Object=MibScalar
nbsSysDefaultGateway=_NbsSysDefaultGateway_Object((1,3,6,1,4,1,629,1,3,7),_NbsSysDefaultGateway_Type())
nbsSysDefaultGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSysDefaultGateway.setStatus(_A)
class _NbsSysReadComunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_NbsSysReadComunity_Type.__name__=_J
_NbsSysReadComunity_Object=MibScalar
nbsSysReadComunity=_NbsSysReadComunity_Object((1,3,6,1,4,1,629,1,3,8),_NbsSysReadComunity_Type())
nbsSysReadComunity.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSysReadComunity.setStatus(_A)
class _NbsSysWriteComunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_NbsSysWriteComunity_Type.__name__=_J
_NbsSysWriteComunity_Object=MibScalar
nbsSysWriteComunity=_NbsSysWriteComunity_Object((1,3,6,1,4,1,629,1,3,9),_NbsSysWriteComunity_Type())
nbsSysWriteComunity.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSysWriteComunity.setStatus(_A)
class _NbsSysBootpEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_NbsSysBootpEnable_Type.__name__=_D
_NbsSysBootpEnable_Object=MibScalar
nbsSysBootpEnable=_NbsSysBootpEnable_Object((1,3,6,1,4,1,629,1,3,10),_NbsSysBootpEnable_Type())
nbsSysBootpEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSysBootpEnable.setStatus(_A)
_NbsSysTrapTblMaxSize_Type=Integer32
_NbsSysTrapTblMaxSize_Object=MibScalar
nbsSysTrapTblMaxSize=_NbsSysTrapTblMaxSize_Object((1,3,6,1,4,1,629,1,3,11),_NbsSysTrapTblMaxSize_Type())
nbsSysTrapTblMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSysTrapTblMaxSize.setStatus(_A)
_NbsSysTrapTable_Object=MibTable
nbsSysTrapTable=_NbsSysTrapTable_Object((1,3,6,1,4,1,629,1,3,12))
if mibBuilder.loadTexts:nbsSysTrapTable.setStatus(_A)
_NbsSysTrapEntry_Object=MibTableRow
nbsSysTrapEntry=_NbsSysTrapEntry_Object((1,3,6,1,4,1,629,1,3,12,1))
nbsSysTrapEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:nbsSysTrapEntry.setStatus(_A)
_NbsSysTrapTblEntIndex_Type=Integer32
_NbsSysTrapTblEntIndex_Object=MibTableColumn
nbsSysTrapTblEntIndex=_NbsSysTrapTblEntIndex_Object((1,3,6,1,4,1,629,1,3,12,1,1),_NbsSysTrapTblEntIndex_Type())
nbsSysTrapTblEntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSysTrapTblEntIndex.setStatus(_A)
class _NbsSysTrapTblEntStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_K,2)))
_NbsSysTrapTblEntStatus_Type.__name__=_D
_NbsSysTrapTblEntStatus_Object=MibTableColumn
nbsSysTrapTblEntStatus=_NbsSysTrapTblEntStatus_Object((1,3,6,1,4,1,629,1,3,12,1,2),_NbsSysTrapTblEntStatus_Type())
nbsSysTrapTblEntStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSysTrapTblEntStatus.setStatus(_A)
_NbsSysTrapTblEntIpAddr_Type=IpAddress
_NbsSysTrapTblEntIpAddr_Object=MibTableColumn
nbsSysTrapTblEntIpAddr=_NbsSysTrapTblEntIpAddr_Object((1,3,6,1,4,1,629,1,3,12,1,3),_NbsSysTrapTblEntIpAddr_Type())
nbsSysTrapTblEntIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSysTrapTblEntIpAddr.setStatus(_A)
_NbsSysTrapTblEntComm_Type=DisplayString
_NbsSysTrapTblEntComm_Object=MibTableColumn
nbsSysTrapTblEntComm=_NbsSysTrapTblEntComm_Object((1,3,6,1,4,1,629,1,3,12,1,4),_NbsSysTrapTblEntComm_Type())
nbsSysTrapTblEntComm.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSysTrapTblEntComm.setStatus(_A)
_NbsSysTftpSwFileName_Type=DisplayString
_NbsSysTftpSwFileName_Object=MibScalar
nbsSysTftpSwFileName=_NbsSysTftpSwFileName_Object((1,3,6,1,4,1,629,1,3,13),_NbsSysTftpSwFileName_Type())
nbsSysTftpSwFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSysTftpSwFileName.setStatus(_A)
_NbsSysTftpParFileName_Type=DisplayString
_NbsSysTftpParFileName_Object=MibScalar
nbsSysTftpParFileName=_NbsSysTftpParFileName_Object((1,3,6,1,4,1,629,1,3,14),_NbsSysTftpParFileName_Type())
nbsSysTftpParFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSysTftpParFileName.setStatus(_A)
class _NbsSysSerialLineMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('adminIf',1),('slipIf',2)))
_NbsSysSerialLineMode_Type.__name__=_D
_NbsSysSerialLineMode_Object=MibScalar
nbsSysSerialLineMode=_NbsSysSerialLineMode_Object((1,3,6,1,4,1,629,1,3,15),_NbsSysSerialLineMode_Type())
nbsSysSerialLineMode.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSysSerialLineMode.setStatus(_A)
class _NbsSysSerialSlipBaudRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('b9600',1),('b19200',2),('b38400',3)))
_NbsSysSerialSlipBaudRate_Type.__name__=_D
_NbsSysSerialSlipBaudRate_Object=MibScalar
nbsSysSerialSlipBaudRate=_NbsSysSerialSlipBaudRate_Object((1,3,6,1,4,1,629,1,3,16),_NbsSysSerialSlipBaudRate_Type())
nbsSysSerialSlipBaudRate.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSysSerialSlipBaudRate.setStatus(_A)
class _NbsSysTelnetSession_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('connected',1),('disconnect',2)))
_NbsSysTelnetSession_Type.__name__=_D
_NbsSysTelnetSession_Object=MibScalar
nbsSysTelnetSession=_NbsSysTelnetSession_Object((1,3,6,1,4,1,629,1,3,17),_NbsSysTelnetSession_Type())
nbsSysTelnetSession.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSysTelnetSession.setStatus(_A)
_NbsSysPing_ObjectIdentity=ObjectIdentity
nbsSysPing=_NbsSysPing_ObjectIdentity((1,3,6,1,4,1,629,1,3,18))
class _NbsSysPingSession_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('idlePing',1),('runPing',2)))
_NbsSysPingSession_Type.__name__=_D
_NbsSysPingSession_Object=MibScalar
nbsSysPingSession=_NbsSysPingSession_Object((1,3,6,1,4,1,629,1,3,18,1),_NbsSysPingSession_Type())
nbsSysPingSession.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSysPingSession.setStatus(_A)
class _NbsSysPingAddr_Type(IpAddress):defaultHexValue='7F000001'
_NbsSysPingAddr_Type.__name__=_P
_NbsSysPingAddr_Object=MibScalar
nbsSysPingAddr=_NbsSysPingAddr_Object((1,3,6,1,4,1,629,1,3,18,2),_NbsSysPingAddr_Type())
nbsSysPingAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSysPingAddr.setStatus(_A)
_NbsSysPingNumber_Type=Counter32
_NbsSysPingNumber_Object=MibScalar
nbsSysPingNumber=_NbsSysPingNumber_Object((1,3,6,1,4,1,629,1,3,18,3),_NbsSysPingNumber_Type())
nbsSysPingNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSysPingNumber.setStatus(_A)
_NbsSysPingRequests_Type=Counter32
_NbsSysPingRequests_Object=MibScalar
nbsSysPingRequests=_NbsSysPingRequests_Object((1,3,6,1,4,1,629,1,3,18,4),_NbsSysPingRequests_Type())
nbsSysPingRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSysPingRequests.setStatus(_A)
_NbsSysPingResps_Type=Integer32
_NbsSysPingResps_Object=MibScalar
nbsSysPingResps=_NbsSysPingResps_Object((1,3,6,1,4,1,629,1,3,18,5),_NbsSysPingResps_Type())
nbsSysPingResps.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSysPingResps.setStatus(_A)
class _NbsSysPingOwner_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('adminInterface',1),('snmpAgent',2)))
_NbsSysPingOwner_Type.__name__=_D
_NbsSysPingOwner_Object=MibScalar
nbsSysPingOwner=_NbsSysPingOwner_Object((1,3,6,1,4,1,629,1,3,18,6),_NbsSysPingOwner_Type())
nbsSysPingOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSysPingOwner.setStatus(_A)
_NbsSysTelnetHost_Type=IpAddress
_NbsSysTelnetHost_Object=MibScalar
nbsSysTelnetHost=_NbsSysTelnetHost_Object((1,3,6,1,4,1,629,1,3,19),_NbsSysTelnetHost_Type())
nbsSysTelnetHost.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSysTelnetHost.setStatus(_A)
_NbsSysTftpRswFileName_Type=DisplayString
_NbsSysTftpRswFileName_Object=MibScalar
nbsSysTftpRswFileName=_NbsSysTftpRswFileName_Object((1,3,6,1,4,1,629,1,3,20),_NbsSysTftpRswFileName_Type())
nbsSysTftpRswFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSysTftpRswFileName.setStatus(_A)
_NbsSysTftpServerIP_Type=IpAddress
_NbsSysTftpServerIP_Object=MibScalar
nbsSysTftpServerIP=_NbsSysTftpServerIP_Object((1,3,6,1,4,1,629,1,3,21),_NbsSysTftpServerIP_Type())
nbsSysTftpServerIP.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSysTftpServerIP.setStatus(_A)
class _NbsSysInitDownload_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_O,2),('activeAppl',3)))
_NbsSysInitDownload_Type.__name__=_D
_NbsSysInitDownload_Object=MibScalar
nbsSysInitDownload=_NbsSysInitDownload_Object((1,3,6,1,4,1,629,1,3,22),_NbsSysInitDownload_Type())
nbsSysInitDownload.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSysInitDownload.setStatus(_A)
class _NbsSysParDownload_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_O,2)))
_NbsSysParDownload_Type.__name__=_D
_NbsSysParDownload_Object=MibScalar
nbsSysParDownload=_NbsSysParDownload_Object((1,3,6,1,4,1,629,1,3,23),_NbsSysParDownload_Type())
nbsSysParDownload.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSysParDownload.setStatus(_A)
class _NbsSysParUpload_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_O,2)))
_NbsSysParUpload_Type.__name__=_D
_NbsSysParUpload_Object=MibScalar
nbsSysParUpload=_NbsSysParUpload_Object((1,3,6,1,4,1,629,1,3,24),_NbsSysParUpload_Type())
nbsSysParUpload.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsSysParUpload.setStatus(_A)
_NbsPortCfg_ObjectIdentity=ObjectIdentity
nbsPortCfg=_NbsPortCfg_ObjectIdentity((1,3,6,1,4,1,629,1,4))
_NbsPortCfgTable_Object=MibTable
nbsPortCfgTable=_NbsPortCfgTable_Object((1,3,6,1,4,1,629,1,4,1))
if mibBuilder.loadTexts:nbsPortCfgTable.setStatus(_A)
_NbsPortCfgEntry_Object=MibTableRow
nbsPortCfgEntry=_NbsPortCfgEntry_Object((1,3,6,1,4,1,629,1,4,1,1))
nbsPortCfgEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:nbsPortCfgEntry.setStatus(_A)
_NbsPortCfgIndex_Type=Integer32
_NbsPortCfgIndex_Object=MibTableColumn
nbsPortCfgIndex=_NbsPortCfgIndex_Object((1,3,6,1,4,1,629,1,4,1,1,1),_NbsPortCfgIndex_Type())
nbsPortCfgIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPortCfgIndex.setStatus(_A)
class _NbsPortCfgLanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,30,40,50,51)));namedValues=NamedValues(*(('none',1),('eth10',2),('eth100',3),('eth10or100',4),('eth100B',5),('eth1000B',6),('atmLane',7),('eth100Grp',8),('eth10or100Grp',9),('fddi',10),('eth100or1000',11),('eth10hpna',12),('eth100or1000amp',13),('eth10or100overVDSL',14),('ethSFP',15),('eth10or100or1000',16),('ethSFP100',30),('ethXFP',40),('ethComboDualMode',50),('ethComboTriMode',51)))
_NbsPortCfgLanType_Type.__name__=_D
_NbsPortCfgLanType_Object=MibTableColumn
nbsPortCfgLanType=_NbsPortCfgLanType_Object((1,3,6,1,4,1,629,1,4,1,1,2),_NbsPortCfgLanType_Type())
nbsPortCfgLanType.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPortCfgLanType.setStatus(_A)
class _NbsPortCfgIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26)));namedValues=NamedValues(*(('aui',1),('tp',2),('auiTp',3),('tpfd',4),('coax',5),('foMm',6),('foSm',7),('none',8),('foSxM',9),('foLxM',10),('foLxS1',11),('foLxS2',12),('foLxS3',13),('foM',14),('foMX',15),('foS1',16),('foS2',17),('foS3',18),('foLxS4',19),('foLxS5',20),('foS4',21),('foS5',22),('foM10',23),('foGMX',24),('foS1A',25),('foPAL',26)))
_NbsPortCfgIfType_Type.__name__=_D
_NbsPortCfgIfType_Object=MibTableColumn
nbsPortCfgIfType=_NbsPortCfgIfType_Object((1,3,6,1,4,1,629,1,4,1,1,3),_NbsPortCfgIfType_Type())
nbsPortCfgIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPortCfgIfType.setStatus(_A)
class _NbsPortCfgPortSelect_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('aui',2),('tp',3),('asel',4)))
_NbsPortCfgPortSelect_Type.__name__=_D
_NbsPortCfgPortSelect_Object=MibTableColumn
nbsPortCfgPortSelect=_NbsPortCfgPortSelect_Object((1,3,6,1,4,1,629,1,4,1,1,4),_NbsPortCfgPortSelect_Type())
nbsPortCfgPortSelect.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsPortCfgPortSelect.setStatus(_A)
class _NbsPortCfgIfLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),(_N,2),(_M,3)))
_NbsPortCfgIfLink_Type.__name__=_D
_NbsPortCfgIfLink_Object=MibTableColumn
nbsPortCfgIfLink=_NbsPortCfgIfLink_Object((1,3,6,1,4,1,629,1,4,1,1,5),_NbsPortCfgIfLink_Type())
nbsPortCfgIfLink.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPortCfgIfLink.setStatus(_A)
class _NbsPortCfgPortFctrl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_NbsPortCfgPortFctrl_Type.__name__=_D
_NbsPortCfgPortFctrl_Object=MibTableColumn
nbsPortCfgPortFctrl=_NbsPortCfgPortFctrl_Object((1,3,6,1,4,1,629,1,4,1,1,6),_NbsPortCfgPortFctrl_Type())
nbsPortCfgPortFctrl.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsPortCfgPortFctrl.setStatus(_A)
class _NbsPortCfgPortDplex_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('halfDuplex',1),('fullDuplex',2)))
_NbsPortCfgPortDplex_Type.__name__=_D
_NbsPortCfgPortDplex_Object=MibTableColumn
nbsPortCfgPortDplex=_NbsPortCfgPortDplex_Object((1,3,6,1,4,1,629,1,4,1,1,7),_NbsPortCfgPortDplex_Type())
nbsPortCfgPortDplex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsPortCfgPortDplex.setStatus(_A)
class _NbsPortCfgPortDelay_Type(Integer32):defaultValue=64
_NbsPortCfgPortDelay_Type.__name__=_D
_NbsPortCfgPortDelay_Object=MibTableColumn
nbsPortCfgPortDelay=_NbsPortCfgPortDelay_Object((1,3,6,1,4,1,629,1,4,1,1,8),_NbsPortCfgPortDelay_Type())
nbsPortCfgPortDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsPortCfgPortDelay.setStatus(_A)
class _NbsPortCfgSpeedSelect_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('autoSense',1),('force10',2),('force100',3),('force1000',4),('force10000',5)))
_NbsPortCfgSpeedSelect_Type.__name__=_D
_NbsPortCfgSpeedSelect_Object=MibTableColumn
nbsPortCfgSpeedSelect=_NbsPortCfgSpeedSelect_Object((1,3,6,1,4,1,629,1,4,1,1,9),_NbsPortCfgSpeedSelect_Type())
nbsPortCfgSpeedSelect.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsPortCfgSpeedSelect.setStatus(_A)
class _NbsPortCfgEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('portDisable',1),('portEnable',2)))
_NbsPortCfgEnable_Type.__name__=_D
_NbsPortCfgEnable_Object=MibTableColumn
nbsPortCfgEnable=_NbsPortCfgEnable_Object((1,3,6,1,4,1,629,1,4,1,1,10),_NbsPortCfgEnable_Type())
nbsPortCfgEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsPortCfgEnable.setStatus(_A)
class _NbsPortCfgIsvpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('access',1),('trunk',2),('nonIsvp',3)))
_NbsPortCfgIsvpMode_Type.__name__=_D
_NbsPortCfgIsvpMode_Object=MibTableColumn
nbsPortCfgIsvpMode=_NbsPortCfgIsvpMode_Object((1,3,6,1,4,1,629,1,4,1,1,11),_NbsPortCfgIsvpMode_Type())
nbsPortCfgIsvpMode.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsPortCfgIsvpMode.setStatus(_A)
_NbsPortGrpCfgNum_Type=Integer32
_NbsPortGrpCfgNum_Object=MibScalar
nbsPortGrpCfgNum=_NbsPortGrpCfgNum_Object((1,3,6,1,4,1,629,1,4,2),_NbsPortGrpCfgNum_Type())
nbsPortGrpCfgNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPortGrpCfgNum.setStatus(_A)
_NbsPortGrpCfgTable_Object=MibTable
nbsPortGrpCfgTable=_NbsPortGrpCfgTable_Object((1,3,6,1,4,1,629,1,4,3))
if mibBuilder.loadTexts:nbsPortGrpCfgTable.setStatus(_A)
_NbsPortGrpCfgEntry_Object=MibTableRow
nbsPortGrpCfgEntry=_NbsPortGrpCfgEntry_Object((1,3,6,1,4,1,629,1,4,3,1))
nbsPortGrpCfgEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:nbsPortGrpCfgEntry.setStatus(_A)
_NbsPortGrpCfgIndex_Type=Integer32
_NbsPortGrpCfgIndex_Object=MibTableColumn
nbsPortGrpCfgIndex=_NbsPortGrpCfgIndex_Object((1,3,6,1,4,1,629,1,4,3,1,1),_NbsPortGrpCfgIndex_Type())
nbsPortGrpCfgIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPortGrpCfgIndex.setStatus(_A)
_NbsPortGrpCfgGrpNumber_Type=Integer32
_NbsPortGrpCfgGrpNumber_Object=MibTableColumn
nbsPortGrpCfgGrpNumber=_NbsPortGrpCfgGrpNumber_Object((1,3,6,1,4,1,629,1,4,3,1,2),_NbsPortGrpCfgGrpNumber_Type())
nbsPortGrpCfgGrpNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPortGrpCfgGrpNumber.setStatus(_A)
_NbsPortGrpCfgPortNumber_Type=Integer32
_NbsPortGrpCfgPortNumber_Object=MibTableColumn
nbsPortGrpCfgPortNumber=_NbsPortGrpCfgPortNumber_Object((1,3,6,1,4,1,629,1,4,3,1,3),_NbsPortGrpCfgPortNumber_Type())
nbsPortGrpCfgPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPortGrpCfgPortNumber.setStatus(_A)
class _NbsPortGrpCfgLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('linkOff',1),('linkOn',2)))
_NbsPortGrpCfgLinkStatus_Type.__name__=_D
_NbsPortGrpCfgLinkStatus_Object=MibTableColumn
nbsPortGrpCfgLinkStatus=_NbsPortGrpCfgLinkStatus_Object((1,3,6,1,4,1,629,1,4,3,1,4),_NbsPortGrpCfgLinkStatus_Type())
nbsPortGrpCfgLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPortGrpCfgLinkStatus.setStatus(_A)
class _NbsPortGrpCfgActivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nonActivity',1),('activity',2)))
_NbsPortGrpCfgActivity_Type.__name__=_D
_NbsPortGrpCfgActivity_Object=MibTableColumn
nbsPortGrpCfgActivity=_NbsPortGrpCfgActivity_Object((1,3,6,1,4,1,629,1,4,3,1,5),_NbsPortGrpCfgActivity_Type())
nbsPortGrpCfgActivity.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPortGrpCfgActivity.setStatus(_A)
_NbsEtherInfo_ObjectIdentity=ObjectIdentity
nbsEtherInfo=_NbsEtherInfo_ObjectIdentity((1,3,6,1,4,1,629,1,5))
_NbsEthInfoTable_Object=MibTable
nbsEthInfoTable=_NbsEthInfoTable_Object((1,3,6,1,4,1,629,1,5,1))
if mibBuilder.loadTexts:nbsEthInfoTable.setStatus(_A)
_NbsEthInfoEntry_Object=MibTableRow
nbsEthInfoEntry=_NbsEthInfoEntry_Object((1,3,6,1,4,1,629,1,5,1,1))
nbsEthInfoEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:nbsEthInfoEntry.setStatus(_A)
_NbsEthInfoIndex_Type=Integer32
_NbsEthInfoIndex_Object=MibTableColumn
nbsEthInfoIndex=_NbsEthInfoIndex_Object((1,3,6,1,4,1,629,1,5,1,1,1),_NbsEthInfoIndex_Type())
nbsEthInfoIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEthInfoIndex.setStatus(_A)
_NbsEthInfoCntFctrls_Type=Counter32
_NbsEthInfoCntFctrls_Object=MibTableColumn
nbsEthInfoCntFctrls=_NbsEthInfoCntFctrls_Object((1,3,6,1,4,1,629,1,5,1,1,2),_NbsEthInfoCntFctrls_Type())
nbsEthInfoCntFctrls.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEthInfoCntFctrls.setStatus(_A)
_NbsEthInfoCntExcessFctrls_Type=Counter32
_NbsEthInfoCntExcessFctrls_Object=MibTableColumn
nbsEthInfoCntExcessFctrls=_NbsEthInfoCntExcessFctrls_Object((1,3,6,1,4,1,629,1,5,1,1,3),_NbsEthInfoCntExcessFctrls_Type())
nbsEthInfoCntExcessFctrls.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEthInfoCntExcessFctrls.setStatus(_A)
_NbsSwitchPerf_ObjectIdentity=ObjectIdentity
nbsSwitchPerf=_NbsSwitchPerf_ObjectIdentity((1,3,6,1,4,1,629,1,6))
_NbsSwitchPerfTable_Object=MibTable
nbsSwitchPerfTable=_NbsSwitchPerfTable_Object((1,3,6,1,4,1,629,1,6,1))
if mibBuilder.loadTexts:nbsSwitchPerfTable.setStatus(_A)
_NbsSwitchPerfEntry_Object=MibTableRow
nbsSwitchPerfEntry=_NbsSwitchPerfEntry_Object((1,3,6,1,4,1,629,1,6,1,1))
nbsSwitchPerfEntry.setIndexNames((0,_E,_X))
if mibBuilder.loadTexts:nbsSwitchPerfEntry.setStatus(_A)
_NbsSwitchPerfIndex_Type=Integer32
_NbsSwitchPerfIndex_Object=MibTableColumn
nbsSwitchPerfIndex=_NbsSwitchPerfIndex_Object((1,3,6,1,4,1,629,1,6,1,1,1),_NbsSwitchPerfIndex_Type())
nbsSwitchPerfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSwitchPerfIndex.setStatus(_A)
_NbsSwitchPerfMcastPkts_Type=Counter32
_NbsSwitchPerfMcastPkts_Object=MibTableColumn
nbsSwitchPerfMcastPkts=_NbsSwitchPerfMcastPkts_Object((1,3,6,1,4,1,629,1,6,1,1,2),_NbsSwitchPerfMcastPkts_Type())
nbsSwitchPerfMcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSwitchPerfMcastPkts.setStatus(_A)
_NbsSwitchPerfUnknPkts_Type=Counter32
_NbsSwitchPerfUnknPkts_Object=MibTableColumn
nbsSwitchPerfUnknPkts=_NbsSwitchPerfUnknPkts_Object((1,3,6,1,4,1,629,1,6,1,1,3),_NbsSwitchPerfUnknPkts_Type())
nbsSwitchPerfUnknPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSwitchPerfUnknPkts.setStatus(_A)
_NbsPortFwdPerfTable_Object=MibTable
nbsPortFwdPerfTable=_NbsPortFwdPerfTable_Object((1,3,6,1,4,1,629,1,6,2))
if mibBuilder.loadTexts:nbsPortFwdPerfTable.setStatus(_A)
_NbsPortFwdPerfEntry_Object=MibTableRow
nbsPortFwdPerfEntry=_NbsPortFwdPerfEntry_Object((1,3,6,1,4,1,629,1,6,2,1))
nbsPortFwdPerfEntry.setIndexNames((0,_E,_Y),(0,_E,_Z))
if mibBuilder.loadTexts:nbsPortFwdPerfEntry.setStatus(_A)
_NbsPortFwdPerfInPort_Type=Integer32
_NbsPortFwdPerfInPort_Object=MibTableColumn
nbsPortFwdPerfInPort=_NbsPortFwdPerfInPort_Object((1,3,6,1,4,1,629,1,6,2,1,1),_NbsPortFwdPerfInPort_Type())
nbsPortFwdPerfInPort.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPortFwdPerfInPort.setStatus(_A)
_NbsPortFwdPerfOutPort_Type=Integer32
_NbsPortFwdPerfOutPort_Object=MibTableColumn
nbsPortFwdPerfOutPort=_NbsPortFwdPerfOutPort_Object((1,3,6,1,4,1,629,1,6,2,1,2),_NbsPortFwdPerfOutPort_Type())
nbsPortFwdPerfOutPort.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPortFwdPerfOutPort.setStatus(_A)
_NbsPortFwdPerfFwdPkts_Type=Counter32
_NbsPortFwdPerfFwdPkts_Object=MibTableColumn
nbsPortFwdPerfFwdPkts=_NbsPortFwdPerfFwdPkts_Object((1,3,6,1,4,1,629,1,6,2,1,3),_NbsPortFwdPerfFwdPkts_Type())
nbsPortFwdPerfFwdPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPortFwdPerfFwdPkts.setStatus(_A)
_NbsPortFwdPerfFwdBytes_Type=Counter32
_NbsPortFwdPerfFwdBytes_Object=MibTableColumn
nbsPortFwdPerfFwdBytes=_NbsPortFwdPerfFwdBytes_Object((1,3,6,1,4,1,629,1,6,2,1,4),_NbsPortFwdPerfFwdBytes_Type())
nbsPortFwdPerfFwdBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPortFwdPerfFwdBytes.setStatus(_A)
_NbsMgmtPerfStats_ObjectIdentity=ObjectIdentity
nbsMgmtPerfStats=_NbsMgmtPerfStats_ObjectIdentity((1,3,6,1,4,1,629,1,6,3))
_NbsMgmtPerfRcvdPkts_Type=Counter32
_NbsMgmtPerfRcvdPkts_Object=MibScalar
nbsMgmtPerfRcvdPkts=_NbsMgmtPerfRcvdPkts_Object((1,3,6,1,4,1,629,1,6,3,1),_NbsMgmtPerfRcvdPkts_Type())
nbsMgmtPerfRcvdPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMgmtPerfRcvdPkts.setStatus(_A)
_NbsMgmtPerfRcvdBytes_Type=Counter32
_NbsMgmtPerfRcvdBytes_Object=MibScalar
nbsMgmtPerfRcvdBytes=_NbsMgmtPerfRcvdBytes_Object((1,3,6,1,4,1,629,1,6,3,2),_NbsMgmtPerfRcvdBytes_Type())
nbsMgmtPerfRcvdBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMgmtPerfRcvdBytes.setStatus(_A)
_NbsMgmtPerfFilterdPkts_Type=Counter32
_NbsMgmtPerfFilterdPkts_Object=MibScalar
nbsMgmtPerfFilterdPkts=_NbsMgmtPerfFilterdPkts_Object((1,3,6,1,4,1,629,1,6,3,3),_NbsMgmtPerfFilterdPkts_Type())
nbsMgmtPerfFilterdPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMgmtPerfFilterdPkts.setStatus(_A)
_NbsMgmtPerfRcvBcastPkts_Type=Counter32
_NbsMgmtPerfRcvBcastPkts_Object=MibScalar
nbsMgmtPerfRcvBcastPkts=_NbsMgmtPerfRcvBcastPkts_Object((1,3,6,1,4,1,629,1,6,3,4),_NbsMgmtPerfRcvBcastPkts_Type())
nbsMgmtPerfRcvBcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMgmtPerfRcvBcastPkts.setStatus(_A)
_NbsMgmtPerfXmtPkts_Type=Counter32
_NbsMgmtPerfXmtPkts_Object=MibScalar
nbsMgmtPerfXmtPkts=_NbsMgmtPerfXmtPkts_Object((1,3,6,1,4,1,629,1,6,3,5),_NbsMgmtPerfXmtPkts_Type())
nbsMgmtPerfXmtPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMgmtPerfXmtPkts.setStatus(_A)
_NbsMgmtPerfXmtUcastPkts_Type=Counter32
_NbsMgmtPerfXmtUcastPkts_Object=MibScalar
nbsMgmtPerfXmtUcastPkts=_NbsMgmtPerfXmtUcastPkts_Object((1,3,6,1,4,1,629,1,6,3,6),_NbsMgmtPerfXmtUcastPkts_Type())
nbsMgmtPerfXmtUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMgmtPerfXmtUcastPkts.setStatus(_A)
_NbsMgmtPerfXmtMcastPkts_Type=Counter32
_NbsMgmtPerfXmtMcastPkts_Object=MibScalar
nbsMgmtPerfXmtMcastPkts=_NbsMgmtPerfXmtMcastPkts_Object((1,3,6,1,4,1,629,1,6,3,7),_NbsMgmtPerfXmtMcastPkts_Type())
nbsMgmtPerfXmtMcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMgmtPerfXmtMcastPkts.setStatus(_A)
_NbsMgmtPerfXmtBcastPkts_Type=Counter32
_NbsMgmtPerfXmtBcastPkts_Object=MibScalar
nbsMgmtPerfXmtBcastPkts=_NbsMgmtPerfXmtBcastPkts_Object((1,3,6,1,4,1,629,1,6,3,8),_NbsMgmtPerfXmtBcastPkts_Type())
nbsMgmtPerfXmtBcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMgmtPerfXmtBcastPkts.setStatus(_A)
_NbsMgmtRcvPerfTable_Object=MibTable
nbsMgmtRcvPerfTable=_NbsMgmtRcvPerfTable_Object((1,3,6,1,4,1,629,1,6,4))
if mibBuilder.loadTexts:nbsMgmtRcvPerfTable.setStatus(_A)
_NbsMgmtRcvPerfEntry_Object=MibTableRow
nbsMgmtRcvPerfEntry=_NbsMgmtRcvPerfEntry_Object((1,3,6,1,4,1,629,1,6,4,1))
nbsMgmtRcvPerfEntry.setIndexNames((0,_E,_a))
if mibBuilder.loadTexts:nbsMgmtRcvPerfEntry.setStatus(_A)
_NbsMgmtRcvPerfInPort_Type=Integer32
_NbsMgmtRcvPerfInPort_Object=MibTableColumn
nbsMgmtRcvPerfInPort=_NbsMgmtRcvPerfInPort_Object((1,3,6,1,4,1,629,1,6,4,1,2),_NbsMgmtRcvPerfInPort_Type())
nbsMgmtRcvPerfInPort.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMgmtRcvPerfInPort.setStatus(_A)
_NbsMgmtRcvPerfFwdPkts_Type=Counter32
_NbsMgmtRcvPerfFwdPkts_Object=MibTableColumn
nbsMgmtRcvPerfFwdPkts=_NbsMgmtRcvPerfFwdPkts_Object((1,3,6,1,4,1,629,1,6,4,1,3),_NbsMgmtRcvPerfFwdPkts_Type())
nbsMgmtRcvPerfFwdPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMgmtRcvPerfFwdPkts.setStatus(_A)
_NbsMgmtRcvPerfFwdBytes_Type=Counter32
_NbsMgmtRcvPerfFwdBytes_Object=MibTableColumn
nbsMgmtRcvPerfFwdBytes=_NbsMgmtRcvPerfFwdBytes_Object((1,3,6,1,4,1,629,1,6,4,1,4),_NbsMgmtRcvPerfFwdBytes_Type())
nbsMgmtRcvPerfFwdBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMgmtRcvPerfFwdBytes.setStatus(_A)
_NbsMgmtXmtPerfTable_Object=MibTable
nbsMgmtXmtPerfTable=_NbsMgmtXmtPerfTable_Object((1,3,6,1,4,1,629,1,6,5))
if mibBuilder.loadTexts:nbsMgmtXmtPerfTable.setStatus(_A)
_NbsMgmtXmtPerfEntry_Object=MibTableRow
nbsMgmtXmtPerfEntry=_NbsMgmtXmtPerfEntry_Object((1,3,6,1,4,1,629,1,6,5,1))
nbsMgmtXmtPerfEntry.setIndexNames((0,_E,_b))
if mibBuilder.loadTexts:nbsMgmtXmtPerfEntry.setStatus(_A)
_NbsMgmtXmtPerfOutPort_Type=Integer32
_NbsMgmtXmtPerfOutPort_Object=MibTableColumn
nbsMgmtXmtPerfOutPort=_NbsMgmtXmtPerfOutPort_Object((1,3,6,1,4,1,629,1,6,5,1,2),_NbsMgmtXmtPerfOutPort_Type())
nbsMgmtXmtPerfOutPort.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMgmtXmtPerfOutPort.setStatus(_A)
_NbsMgmtXmtPerfFwdPkts_Type=Counter32
_NbsMgmtXmtPerfFwdPkts_Object=MibTableColumn
nbsMgmtXmtPerfFwdPkts=_NbsMgmtXmtPerfFwdPkts_Object((1,3,6,1,4,1,629,1,6,5,1,3),_NbsMgmtXmtPerfFwdPkts_Type())
nbsMgmtXmtPerfFwdPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMgmtXmtPerfFwdPkts.setStatus(_A)
_NbsMgmtXmtPerfFwdBytes_Type=Counter32
_NbsMgmtXmtPerfFwdBytes_Object=MibTableColumn
nbsMgmtXmtPerfFwdBytes=_NbsMgmtXmtPerfFwdBytes_Object((1,3,6,1,4,1,629,1,6,5,1,4),_NbsMgmtXmtPerfFwdBytes_Type())
nbsMgmtXmtPerfFwdBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMgmtXmtPerfFwdBytes.setStatus(_A)
_NbsTraps_ObjectIdentity=ObjectIdentity
nbsTraps=_NbsTraps_ObjectIdentity((1,3,6,1,4,1,629,1,7))
_NbsMiniSwDb_ObjectIdentity=ObjectIdentity
nbsMiniSwDb=_NbsMiniSwDb_ObjectIdentity((1,3,6,1,4,1,629,1,8))
_NbsMegaSwDb_ObjectIdentity=ObjectIdentity
nbsMegaSwDb=_NbsMegaSwDb_ObjectIdentity((1,3,6,1,4,1,629,1,9))
_NbsMegaSwRunDb_ObjectIdentity=ObjectIdentity
nbsMegaSwRunDb=_NbsMegaSwRunDb_ObjectIdentity((1,3,6,1,4,1,629,1,9,1))
_NbsMegaSwRunDbTable_Object=MibTable
nbsMegaSwRunDbTable=_NbsMegaSwRunDbTable_Object((1,3,6,1,4,1,629,1,9,1,1))
if mibBuilder.loadTexts:nbsMegaSwRunDbTable.setStatus(_A)
_NbsMegaSwRunDbEntry_Object=MibTableRow
nbsMegaSwRunDbEntry=_NbsMegaSwRunDbEntry_Object((1,3,6,1,4,1,629,1,9,1,1,1))
nbsMegaSwRunDbEntry.setIndexNames((0,_E,_c))
if mibBuilder.loadTexts:nbsMegaSwRunDbEntry.setStatus(_A)
_NbsMegaSwRunDbIndex_Type=Integer32
_NbsMegaSwRunDbIndex_Object=MibTableColumn
nbsMegaSwRunDbIndex=_NbsMegaSwRunDbIndex_Object((1,3,6,1,4,1,629,1,9,1,1,1,1),_NbsMegaSwRunDbIndex_Type())
nbsMegaSwRunDbIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMegaSwRunDbIndex.setStatus(_A)
class _NbsMegaSwRunDbStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_d,2),(_e,3),(_f,4),(_g,5)))
_NbsMegaSwRunDbStatus_Type.__name__=_D
_NbsMegaSwRunDbStatus_Object=MibTableColumn
nbsMegaSwRunDbStatus=_NbsMegaSwRunDbStatus_Object((1,3,6,1,4,1,629,1,9,1,1,1,2),_NbsMegaSwRunDbStatus_Type())
nbsMegaSwRunDbStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMegaSwRunDbStatus.setStatus(_A)
_NbsMegaSwRunDbAddr_Type=MacAddress
_NbsMegaSwRunDbAddr_Object=MibTableColumn
nbsMegaSwRunDbAddr=_NbsMegaSwRunDbAddr_Object((1,3,6,1,4,1,629,1,9,1,1,1,3),_NbsMegaSwRunDbAddr_Type())
nbsMegaSwRunDbAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMegaSwRunDbAddr.setStatus(_A)
class _NbsMegaSwRunDbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_h,1),(_i,2)))
_NbsMegaSwRunDbType_Type.__name__=_D
_NbsMegaSwRunDbType_Object=MibTableColumn
nbsMegaSwRunDbType=_NbsMegaSwRunDbType_Object((1,3,6,1,4,1,629,1,9,1,1,1,4),_NbsMegaSwRunDbType_Type())
nbsMegaSwRunDbType.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMegaSwRunDbType.setStatus(_A)
_NbsMegaSwRunDbDport_Type=Integer32
_NbsMegaSwRunDbDport_Object=MibTableColumn
nbsMegaSwRunDbDport=_NbsMegaSwRunDbDport_Object((1,3,6,1,4,1,629,1,9,1,1,1,5),_NbsMegaSwRunDbDport_Type())
nbsMegaSwRunDbDport.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMegaSwRunDbDport.setStatus(_A)
_NbsMegaSwRunFilterTable_Object=MibTable
nbsMegaSwRunFilterTable=_NbsMegaSwRunFilterTable_Object((1,3,6,1,4,1,629,1,9,1,2))
if mibBuilder.loadTexts:nbsMegaSwRunFilterTable.setStatus(_A)
_NbsMegaSwRunFilterEntry_Object=MibTableRow
nbsMegaSwRunFilterEntry=_NbsMegaSwRunFilterEntry_Object((1,3,6,1,4,1,629,1,9,1,2,1))
nbsMegaSwRunFilterEntry.setIndexNames((0,_E,_j),(0,_E,_k))
if mibBuilder.loadTexts:nbsMegaSwRunFilterEntry.setStatus(_A)
class _NbsMegaSwRunFilterStatus_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_d,2),(_e,3),(_f,4),(_g,5)))
_NbsMegaSwRunFilterStatus_Type.__name__=_D
_NbsMegaSwRunFilterStatus_Object=MibTableColumn
nbsMegaSwRunFilterStatus=_NbsMegaSwRunFilterStatus_Object((1,3,6,1,4,1,629,1,9,1,2,1,1),_NbsMegaSwRunFilterStatus_Type())
nbsMegaSwRunFilterStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsMegaSwRunFilterStatus.setStatus(_A)
_NbsMegaSwRunFilterAddr_Type=MacAddress
_NbsMegaSwRunFilterAddr_Object=MibTableColumn
nbsMegaSwRunFilterAddr=_NbsMegaSwRunFilterAddr_Object((1,3,6,1,4,1,629,1,9,1,2,1,2),_NbsMegaSwRunFilterAddr_Type())
nbsMegaSwRunFilterAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsMegaSwRunFilterAddr.setStatus(_A)
class _NbsMegaSwRunFilterType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_h,1),(_i,2)))
_NbsMegaSwRunFilterType_Type.__name__=_D
_NbsMegaSwRunFilterType_Object=MibTableColumn
nbsMegaSwRunFilterType=_NbsMegaSwRunFilterType_Object((1,3,6,1,4,1,629,1,9,1,2,1,3),_NbsMegaSwRunFilterType_Type())
nbsMegaSwRunFilterType.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsMegaSwRunFilterType.setStatus(_A)
class _NbsMegaSwRunFilterDport_Type(Integer32):defaultValue=0
_NbsMegaSwRunFilterDport_Type.__name__=_D
_NbsMegaSwRunFilterDport_Object=MibTableColumn
nbsMegaSwRunFilterDport=_NbsMegaSwRunFilterDport_Object((1,3,6,1,4,1,629,1,9,1,2,1,4),_NbsMegaSwRunFilterDport_Type())
nbsMegaSwRunFilterDport.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsMegaSwRunFilterDport.setStatus(_A)
_NbsMegaSwRunFilterSport_Type=Integer32
_NbsMegaSwRunFilterSport_Object=MibTableColumn
nbsMegaSwRunFilterSport=_NbsMegaSwRunFilterSport_Object((1,3,6,1,4,1,629,1,9,1,2,1,5),_NbsMegaSwRunFilterSport_Type())
nbsMegaSwRunFilterSport.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsMegaSwRunFilterSport.setStatus(_A)
class _NbsMegaSwRunFilterDmap_Type(OctetString):defaultHexValue=_H
_NbsMegaSwRunFilterDmap_Type.__name__=_G
_NbsMegaSwRunFilterDmap_Object=MibTableColumn
nbsMegaSwRunFilterDmap=_NbsMegaSwRunFilterDmap_Object((1,3,6,1,4,1,629,1,9,1,2,1,6),_NbsMegaSwRunFilterDmap_Type())
nbsMegaSwRunFilterDmap.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsMegaSwRunFilterDmap.setStatus(_A)
_NbsMegaSwSvlanConnectTable_Object=MibTable
nbsMegaSwSvlanConnectTable=_NbsMegaSwSvlanConnectTable_Object((1,3,6,1,4,1,629,1,9,1,3))
if mibBuilder.loadTexts:nbsMegaSwSvlanConnectTable.setStatus(_A)
_NbsMegaSwSvlanConnectEntry_Object=MibTableRow
nbsMegaSwSvlanConnectEntry=_NbsMegaSwSvlanConnectEntry_Object((1,3,6,1,4,1,629,1,9,1,3,1))
nbsMegaSwSvlanConnectEntry.setIndexNames((0,_E,_l))
if mibBuilder.loadTexts:nbsMegaSwSvlanConnectEntry.setStatus(_A)
_NbsMegaSwSvlanConnectSport_Type=Integer32
_NbsMegaSwSvlanConnectSport_Object=MibTableColumn
nbsMegaSwSvlanConnectSport=_NbsMegaSwSvlanConnectSport_Object((1,3,6,1,4,1,629,1,9,1,3,1,1),_NbsMegaSwSvlanConnectSport_Type())
nbsMegaSwSvlanConnectSport.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMegaSwSvlanConnectSport.setStatus(_A)
_NbsMegaSwSvlanConnectDport_Type=OctetString
_NbsMegaSwSvlanConnectDport_Object=MibTableColumn
nbsMegaSwSvlanConnectDport=_NbsMegaSwSvlanConnectDport_Object((1,3,6,1,4,1,629,1,9,1,3,1,2),_NbsMegaSwSvlanConnectDport_Type())
nbsMegaSwSvlanConnectDport.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMegaSwSvlanConnectDport.setStatus(_A)
_NbsMegaSwRunSvlanDb_ObjectIdentity=ObjectIdentity
nbsMegaSwRunSvlanDb=_NbsMegaSwRunSvlanDb_ObjectIdentity((1,3,6,1,4,1,629,1,9,1,4))
_NbsMegaSwRunSvlanMaxNum_Type=Integer32
_NbsMegaSwRunSvlanMaxNum_Object=MibScalar
nbsMegaSwRunSvlanMaxNum=_NbsMegaSwRunSvlanMaxNum_Object((1,3,6,1,4,1,629,1,9,1,4,1),_NbsMegaSwRunSvlanMaxNum_Type())
nbsMegaSwRunSvlanMaxNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMegaSwRunSvlanMaxNum.setStatus(_A)
_NbsMegaSwRunSvlanTable_Object=MibTable
nbsMegaSwRunSvlanTable=_NbsMegaSwRunSvlanTable_Object((1,3,6,1,4,1,629,1,9,1,4,2))
if mibBuilder.loadTexts:nbsMegaSwRunSvlanTable.setStatus(_A)
_NbsMegaSwRunSvlanEntry_Object=MibTableRow
nbsMegaSwRunSvlanEntry=_NbsMegaSwRunSvlanEntry_Object((1,3,6,1,4,1,629,1,9,1,4,2,1))
nbsMegaSwRunSvlanEntry.setIndexNames((0,_E,_m))
if mibBuilder.loadTexts:nbsMegaSwRunSvlanEntry.setStatus(_A)
_NbsMegaSwRunSvlanIndex_Type=Integer32
_NbsMegaSwRunSvlanIndex_Object=MibTableColumn
nbsMegaSwRunSvlanIndex=_NbsMegaSwRunSvlanIndex_Object((1,3,6,1,4,1,629,1,9,1,4,2,1,1),_NbsMegaSwRunSvlanIndex_Type())
nbsMegaSwRunSvlanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMegaSwRunSvlanIndex.setStatus(_A)
class _NbsMegaSwRunSvlanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_F,2)))
_NbsMegaSwRunSvlanStatus_Type.__name__=_D
_NbsMegaSwRunSvlanStatus_Object=MibTableColumn
nbsMegaSwRunSvlanStatus=_NbsMegaSwRunSvlanStatus_Object((1,3,6,1,4,1,629,1,9,1,4,2,1,2),_NbsMegaSwRunSvlanStatus_Type())
nbsMegaSwRunSvlanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsMegaSwRunSvlanStatus.setStatus(_A)
class _NbsMegaSwRunSvlanList_Type(OctetString):defaultHexValue=_H
_NbsMegaSwRunSvlanList_Type.__name__=_G
_NbsMegaSwRunSvlanList_Object=MibTableColumn
nbsMegaSwRunSvlanList=_NbsMegaSwRunSvlanList_Object((1,3,6,1,4,1,629,1,9,1,4,2,1,3),_NbsMegaSwRunSvlanList_Type())
nbsMegaSwRunSvlanList.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsMegaSwRunSvlanList.setStatus(_A)
_NbsMegaSwRunSvlanIsvlanFlag_Type=Integer32
_NbsMegaSwRunSvlanIsvlanFlag_Object=MibTableColumn
nbsMegaSwRunSvlanIsvlanFlag=_NbsMegaSwRunSvlanIsvlanFlag_Object((1,3,6,1,4,1,629,1,9,1,4,2,1,4),_NbsMegaSwRunSvlanIsvlanFlag_Type())
nbsMegaSwRunSvlanIsvlanFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMegaSwRunSvlanIsvlanFlag.setStatus(_A)
_NbsMegaSwRunIsvlanMaxNum_Type=Integer32
_NbsMegaSwRunIsvlanMaxNum_Object=MibScalar
nbsMegaSwRunIsvlanMaxNum=_NbsMegaSwRunIsvlanMaxNum_Object((1,3,6,1,4,1,629,1,9,1,4,3),_NbsMegaSwRunIsvlanMaxNum_Type())
nbsMegaSwRunIsvlanMaxNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMegaSwRunIsvlanMaxNum.setStatus(_A)
_NbsMegaSwRunIsvlanTable_Object=MibTable
nbsMegaSwRunIsvlanTable=_NbsMegaSwRunIsvlanTable_Object((1,3,6,1,4,1,629,1,9,1,4,4))
if mibBuilder.loadTexts:nbsMegaSwRunIsvlanTable.setStatus(_A)
_NbsMegaSwRunIsvlanEntry_Object=MibTableRow
nbsMegaSwRunIsvlanEntry=_NbsMegaSwRunIsvlanEntry_Object((1,3,6,1,4,1,629,1,9,1,4,4,1))
nbsMegaSwRunIsvlanEntry.setIndexNames((0,_E,_n))
if mibBuilder.loadTexts:nbsMegaSwRunIsvlanEntry.setStatus(_A)
_NbsMegaSwRunIsvlanIndex_Type=Integer32
_NbsMegaSwRunIsvlanIndex_Object=MibTableColumn
nbsMegaSwRunIsvlanIndex=_NbsMegaSwRunIsvlanIndex_Object((1,3,6,1,4,1,629,1,9,1,4,4,1,1),_NbsMegaSwRunIsvlanIndex_Type())
nbsMegaSwRunIsvlanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMegaSwRunIsvlanIndex.setStatus(_A)
class _NbsMegaSwRunIsvlanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_F,2),('mcast',3)))
_NbsMegaSwRunIsvlanStatus_Type.__name__=_D
_NbsMegaSwRunIsvlanStatus_Object=MibTableColumn
nbsMegaSwRunIsvlanStatus=_NbsMegaSwRunIsvlanStatus_Object((1,3,6,1,4,1,629,1,9,1,4,4,1,2),_NbsMegaSwRunIsvlanStatus_Type())
nbsMegaSwRunIsvlanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsMegaSwRunIsvlanStatus.setStatus(_A)
class _NbsMegaSwRunIsvlanList_Type(OctetString):defaultHexValue=_H
_NbsMegaSwRunIsvlanList_Type.__name__=_G
_NbsMegaSwRunIsvlanList_Object=MibTableColumn
nbsMegaSwRunIsvlanList=_NbsMegaSwRunIsvlanList_Object((1,3,6,1,4,1,629,1,9,1,4,4,1,3),_NbsMegaSwRunIsvlanList_Type())
nbsMegaSwRunIsvlanList.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsMegaSwRunIsvlanList.setStatus(_A)
class _NbsMegaSwRunIsvlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_NbsMegaSwRunIsvlanName_Type.__name__=_J
_NbsMegaSwRunIsvlanName_Object=MibTableColumn
nbsMegaSwRunIsvlanName=_NbsMegaSwRunIsvlanName_Object((1,3,6,1,4,1,629,1,9,1,4,4,1,4),_NbsMegaSwRunIsvlanName_Type())
nbsMegaSwRunIsvlanName.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsMegaSwRunIsvlanName.setStatus(_A)
class _NbsMegaSwRunIsvlanTag_Type(Integer32):defaultValue=1
_NbsMegaSwRunIsvlanTag_Type.__name__=_D
_NbsMegaSwRunIsvlanTag_Object=MibTableColumn
nbsMegaSwRunIsvlanTag=_NbsMegaSwRunIsvlanTag_Object((1,3,6,1,4,1,629,1,9,1,4,4,1,5),_NbsMegaSwRunIsvlanTag_Type())
nbsMegaSwRunIsvlanTag.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsMegaSwRunIsvlanTag.setStatus(_A)
_NbsMegaSwRunIsvlanVlanIndex_Type=Integer32
_NbsMegaSwRunIsvlanVlanIndex_Object=MibTableColumn
nbsMegaSwRunIsvlanVlanIndex=_NbsMegaSwRunIsvlanVlanIndex_Object((1,3,6,1,4,1,629,1,9,1,4,4,1,6),_NbsMegaSwRunIsvlanVlanIndex_Type())
nbsMegaSwRunIsvlanVlanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMegaSwRunIsvlanVlanIndex.setStatus(_A)
_NbsMegaSwRunVbcDb_ObjectIdentity=ObjectIdentity
nbsMegaSwRunVbcDb=_NbsMegaSwRunVbcDb_ObjectIdentity((1,3,6,1,4,1,629,1,9,1,5))
_NbsMegaSwRunVbcMaxNum_Type=Integer32
_NbsMegaSwRunVbcMaxNum_Object=MibScalar
nbsMegaSwRunVbcMaxNum=_NbsMegaSwRunVbcMaxNum_Object((1,3,6,1,4,1,629,1,9,1,5,1),_NbsMegaSwRunVbcMaxNum_Type())
nbsMegaSwRunVbcMaxNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMegaSwRunVbcMaxNum.setStatus(_A)
_NbsMegaSwRunVbcTable_Object=MibTable
nbsMegaSwRunVbcTable=_NbsMegaSwRunVbcTable_Object((1,3,6,1,4,1,629,1,9,1,5,2))
if mibBuilder.loadTexts:nbsMegaSwRunVbcTable.setStatus(_A)
_NbsMegaSwRunVbcEntry_Object=MibTableRow
nbsMegaSwRunVbcEntry=_NbsMegaSwRunVbcEntry_Object((1,3,6,1,4,1,629,1,9,1,5,2,1))
nbsMegaSwRunVbcEntry.setIndexNames((0,_E,_o))
if mibBuilder.loadTexts:nbsMegaSwRunVbcEntry.setStatus(_A)
_NbsMegaSwRunVbcIndex_Type=Integer32
_NbsMegaSwRunVbcIndex_Object=MibTableColumn
nbsMegaSwRunVbcIndex=_NbsMegaSwRunVbcIndex_Object((1,3,6,1,4,1,629,1,9,1,5,2,1,1),_NbsMegaSwRunVbcIndex_Type())
nbsMegaSwRunVbcIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMegaSwRunVbcIndex.setStatus(_A)
class _NbsMegaSwRunVbcStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_F,2)))
_NbsMegaSwRunVbcStatus_Type.__name__=_D
_NbsMegaSwRunVbcStatus_Object=MibTableColumn
nbsMegaSwRunVbcStatus=_NbsMegaSwRunVbcStatus_Object((1,3,6,1,4,1,629,1,9,1,5,2,1,2),_NbsMegaSwRunVbcStatus_Type())
nbsMegaSwRunVbcStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsMegaSwRunVbcStatus.setStatus(_A)
class _NbsMegaSwRunVbcList_Type(OctetString):defaultHexValue=_H
_NbsMegaSwRunVbcList_Type.__name__=_G
_NbsMegaSwRunVbcList_Object=MibTableColumn
nbsMegaSwRunVbcList=_NbsMegaSwRunVbcList_Object((1,3,6,1,4,1,629,1,9,1,5,2,1,3),_NbsMegaSwRunVbcList_Type())
nbsMegaSwRunVbcList.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsMegaSwRunVbcList.setStatus(_A)
_NbsMegaSwVmon_ObjectIdentity=ObjectIdentity
nbsMegaSwVmon=_NbsMegaSwVmon_ObjectIdentity((1,3,6,1,4,1,629,1,9,1,6))
_NbsMegaSwVmonMonitorPort_Type=Integer32
_NbsMegaSwVmonMonitorPort_Object=MibScalar
nbsMegaSwVmonMonitorPort=_NbsMegaSwVmonMonitorPort_Object((1,3,6,1,4,1,629,1,9,1,6,1),_NbsMegaSwVmonMonitorPort_Type())
nbsMegaSwVmonMonitorPort.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsMegaSwVmonMonitorPort.setStatus(_A)
_NbsMegaSwVmonMonitrdPort_Type=Integer32
_NbsMegaSwVmonMonitrdPort_Object=MibScalar
nbsMegaSwVmonMonitrdPort=_NbsMegaSwVmonMonitrdPort_Object((1,3,6,1,4,1,629,1,9,1,6,2),_NbsMegaSwVmonMonitrdPort_Type())
nbsMegaSwVmonMonitrdPort.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsMegaSwVmonMonitrdPort.setStatus(_A)
class _NbsMegaSwVmonStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('nonInit',1),('startMon',2),('stopMon',3)))
_NbsMegaSwVmonStatus_Type.__name__=_D
_NbsMegaSwVmonStatus_Object=MibScalar
nbsMegaSwVmonStatus=_NbsMegaSwVmonStatus_Object((1,3,6,1,4,1,629,1,9,1,6,3),_NbsMegaSwVmonStatus_Type())
nbsMegaSwVmonStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsMegaSwVmonStatus.setStatus(_A)
_NbsMegaSwPermDb_ObjectIdentity=ObjectIdentity
nbsMegaSwPermDb=_NbsMegaSwPermDb_ObjectIdentity((1,3,6,1,4,1,629,1,9,2))
_NbsMegaSwPermSvlanDb_ObjectIdentity=ObjectIdentity
nbsMegaSwPermSvlanDb=_NbsMegaSwPermSvlanDb_ObjectIdentity((1,3,6,1,4,1,629,1,9,2,1))
_NbsMegaSwPermSvlanMaxNum_Type=Integer32
_NbsMegaSwPermSvlanMaxNum_Object=MibScalar
nbsMegaSwPermSvlanMaxNum=_NbsMegaSwPermSvlanMaxNum_Object((1,3,6,1,4,1,629,1,9,2,1,1),_NbsMegaSwPermSvlanMaxNum_Type())
nbsMegaSwPermSvlanMaxNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMegaSwPermSvlanMaxNum.setStatus(_A)
_NbsMegaSwPermSvlanTable_Object=MibTable
nbsMegaSwPermSvlanTable=_NbsMegaSwPermSvlanTable_Object((1,3,6,1,4,1,629,1,9,2,1,2))
if mibBuilder.loadTexts:nbsMegaSwPermSvlanTable.setStatus(_A)
_NbsMegaSwPermSvlanEntry_Object=MibTableRow
nbsMegaSwPermSvlanEntry=_NbsMegaSwPermSvlanEntry_Object((1,3,6,1,4,1,629,1,9,2,1,2,1))
nbsMegaSwPermSvlanEntry.setIndexNames((0,_E,_p))
if mibBuilder.loadTexts:nbsMegaSwPermSvlanEntry.setStatus(_A)
_NbsMegaSwPermSvlanIndex_Type=Integer32
_NbsMegaSwPermSvlanIndex_Object=MibTableColumn
nbsMegaSwPermSvlanIndex=_NbsMegaSwPermSvlanIndex_Object((1,3,6,1,4,1,629,1,9,2,1,2,1,1),_NbsMegaSwPermSvlanIndex_Type())
nbsMegaSwPermSvlanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMegaSwPermSvlanIndex.setStatus(_A)
class _NbsMegaSwPermSvlanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_F,2)))
_NbsMegaSwPermSvlanStatus_Type.__name__=_D
_NbsMegaSwPermSvlanStatus_Object=MibTableColumn
nbsMegaSwPermSvlanStatus=_NbsMegaSwPermSvlanStatus_Object((1,3,6,1,4,1,629,1,9,2,1,2,1,2),_NbsMegaSwPermSvlanStatus_Type())
nbsMegaSwPermSvlanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsMegaSwPermSvlanStatus.setStatus(_A)
class _NbsMegaSwPermSvlanList_Type(OctetString):defaultHexValue=_H
_NbsMegaSwPermSvlanList_Type.__name__=_G
_NbsMegaSwPermSvlanList_Object=MibTableColumn
nbsMegaSwPermSvlanList=_NbsMegaSwPermSvlanList_Object((1,3,6,1,4,1,629,1,9,2,1,2,1,3),_NbsMegaSwPermSvlanList_Type())
nbsMegaSwPermSvlanList.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsMegaSwPermSvlanList.setStatus(_A)
_NbsMegaSwPermIsvlanMaxNum_Type=Integer32
_NbsMegaSwPermIsvlanMaxNum_Object=MibScalar
nbsMegaSwPermIsvlanMaxNum=_NbsMegaSwPermIsvlanMaxNum_Object((1,3,6,1,4,1,629,1,9,2,1,3),_NbsMegaSwPermIsvlanMaxNum_Type())
nbsMegaSwPermIsvlanMaxNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMegaSwPermIsvlanMaxNum.setStatus(_A)
_NbsMegaSwPermIsvlanTable_Object=MibTable
nbsMegaSwPermIsvlanTable=_NbsMegaSwPermIsvlanTable_Object((1,3,6,1,4,1,629,1,9,2,1,4))
if mibBuilder.loadTexts:nbsMegaSwPermIsvlanTable.setStatus(_A)
_NbsMegaSwPermIsvlanEntry_Object=MibTableRow
nbsMegaSwPermIsvlanEntry=_NbsMegaSwPermIsvlanEntry_Object((1,3,6,1,4,1,629,1,9,2,1,4,1))
nbsMegaSwPermIsvlanEntry.setIndexNames((0,_E,_q))
if mibBuilder.loadTexts:nbsMegaSwPermIsvlanEntry.setStatus(_A)
_NbsMegaSwPermIsvlanIndex_Type=Integer32
_NbsMegaSwPermIsvlanIndex_Object=MibTableColumn
nbsMegaSwPermIsvlanIndex=_NbsMegaSwPermIsvlanIndex_Object((1,3,6,1,4,1,629,1,9,2,1,4,1,1),_NbsMegaSwPermIsvlanIndex_Type())
nbsMegaSwPermIsvlanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMegaSwPermIsvlanIndex.setStatus(_A)
class _NbsMegaSwPermIsvlanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_F,2),('mcast',3)))
_NbsMegaSwPermIsvlanStatus_Type.__name__=_D
_NbsMegaSwPermIsvlanStatus_Object=MibTableColumn
nbsMegaSwPermIsvlanStatus=_NbsMegaSwPermIsvlanStatus_Object((1,3,6,1,4,1,629,1,9,2,1,4,1,2),_NbsMegaSwPermIsvlanStatus_Type())
nbsMegaSwPermIsvlanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsMegaSwPermIsvlanStatus.setStatus(_A)
class _NbsMegaSwPermIsvlanList_Type(OctetString):defaultHexValue=_H
_NbsMegaSwPermIsvlanList_Type.__name__=_G
_NbsMegaSwPermIsvlanList_Object=MibTableColumn
nbsMegaSwPermIsvlanList=_NbsMegaSwPermIsvlanList_Object((1,3,6,1,4,1,629,1,9,2,1,4,1,3),_NbsMegaSwPermIsvlanList_Type())
nbsMegaSwPermIsvlanList.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsMegaSwPermIsvlanList.setStatus(_A)
class _NbsMegaSwPermIsvlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_NbsMegaSwPermIsvlanName_Type.__name__=_J
_NbsMegaSwPermIsvlanName_Object=MibTableColumn
nbsMegaSwPermIsvlanName=_NbsMegaSwPermIsvlanName_Object((1,3,6,1,4,1,629,1,9,2,1,4,1,4),_NbsMegaSwPermIsvlanName_Type())
nbsMegaSwPermIsvlanName.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsMegaSwPermIsvlanName.setStatus(_A)
_NbsMegaSwPermIsvlanTag_Type=Integer32
_NbsMegaSwPermIsvlanTag_Object=MibTableColumn
nbsMegaSwPermIsvlanTag=_NbsMegaSwPermIsvlanTag_Object((1,3,6,1,4,1,629,1,9,2,1,4,1,5),_NbsMegaSwPermIsvlanTag_Type())
nbsMegaSwPermIsvlanTag.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsMegaSwPermIsvlanTag.setStatus(_A)
_NbsMegaSwPermVbcDb_ObjectIdentity=ObjectIdentity
nbsMegaSwPermVbcDb=_NbsMegaSwPermVbcDb_ObjectIdentity((1,3,6,1,4,1,629,1,9,2,2))
_NbsMegaSwPermVbcMaxNum_Type=Integer32
_NbsMegaSwPermVbcMaxNum_Object=MibScalar
nbsMegaSwPermVbcMaxNum=_NbsMegaSwPermVbcMaxNum_Object((1,3,6,1,4,1,629,1,9,2,2,1),_NbsMegaSwPermVbcMaxNum_Type())
nbsMegaSwPermVbcMaxNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMegaSwPermVbcMaxNum.setStatus(_A)
_NbsMegaSwPermVbcTable_Object=MibTable
nbsMegaSwPermVbcTable=_NbsMegaSwPermVbcTable_Object((1,3,6,1,4,1,629,1,9,2,2,2))
if mibBuilder.loadTexts:nbsMegaSwPermVbcTable.setStatus(_A)
_NbsMegaSwPermVbcEntry_Object=MibTableRow
nbsMegaSwPermVbcEntry=_NbsMegaSwPermVbcEntry_Object((1,3,6,1,4,1,629,1,9,2,2,2,1))
nbsMegaSwPermVbcEntry.setIndexNames((0,_E,_r))
if mibBuilder.loadTexts:nbsMegaSwPermVbcEntry.setStatus(_A)
_NbsMegaSwPermVbcIndex_Type=Integer32
_NbsMegaSwPermVbcIndex_Object=MibTableColumn
nbsMegaSwPermVbcIndex=_NbsMegaSwPermVbcIndex_Object((1,3,6,1,4,1,629,1,9,2,2,2,1,1),_NbsMegaSwPermVbcIndex_Type())
nbsMegaSwPermVbcIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMegaSwPermVbcIndex.setStatus(_A)
class _NbsMegaSwPermVbcStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_F,2)))
_NbsMegaSwPermVbcStatus_Type.__name__=_D
_NbsMegaSwPermVbcStatus_Object=MibTableColumn
nbsMegaSwPermVbcStatus=_NbsMegaSwPermVbcStatus_Object((1,3,6,1,4,1,629,1,9,2,2,2,1,2),_NbsMegaSwPermVbcStatus_Type())
nbsMegaSwPermVbcStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsMegaSwPermVbcStatus.setStatus(_A)
class _NbsMegaSwPermVbcList_Type(OctetString):defaultHexValue=_H
_NbsMegaSwPermVbcList_Type.__name__=_G
_NbsMegaSwPermVbcList_Object=MibTableColumn
nbsMegaSwPermVbcList=_NbsMegaSwPermVbcList_Object((1,3,6,1,4,1,629,1,9,2,2,2,1,3),_NbsMegaSwPermVbcList_Type())
nbsMegaSwPermVbcList.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsMegaSwPermVbcList.setStatus(_A)
_NbsTpPermAgingTime_Type=Integer32
_NbsTpPermAgingTime_Object=MibScalar
nbsTpPermAgingTime=_NbsTpPermAgingTime_Object((1,3,6,1,4,1,629,1,9,2,3),_NbsTpPermAgingTime_Type())
nbsTpPermAgingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsTpPermAgingTime.setStatus(_A)
mibBuilder.exportSymbols(_E,**{_L:MacAddress,'nbase':nbase,'nbSwitchG1':nbSwitchG1,'nbsProducts':nbsProducts,'miniSwitch':miniSwitch,'megaSwitch208':megaSwitch208,'megaSwitch215':megaSwitch215,'megaFastSwitch':megaFastSwitch,'megaSwitchII':megaSwitchII,'megaSwitch2015':megaSwitch2015,'megaSwitch2048':megaSwitch2048,'nbsSys':nbsSys,'nbsSysFwVers':nbsSysFwVers,'nbsSysPortsNumber':nbsSysPortsNumber,'nbsSysRestart':nbsSysRestart,'nbsSysNumRestarts':nbsSysNumRestarts,'nbsSysLastError':nbsSysLastError,'nbsSysErrUptime':nbsSysErrUptime,'nbsSysSwitchDBSize':nbsSysSwitchDBSize,'nbsSysSetNvramDefaults':nbsSysSetNvramDefaults,'nbsSysResetSwitchStats':nbsSysResetSwitchStats,'nbsSysStpEnable':nbsSysStpEnable,'nbsSysRunStpState':nbsSysRunStpState,'nbsSysFrmGen':nbsSysFrmGen,'nbsSysFrmGenSession':nbsSysFrmGenSession,'nbsSysFrmGenDa':nbsSysFrmGenDa,'nbsSysFrmGenSa':nbsSysFrmGenSa,'nbsSysFrmGenPktFill':nbsSysFrmGenPktFill,'nbsSysFrmGenPktRate':nbsSysFrmGenPktRate,'nbsSysFrmGenDestMap':nbsSysFrmGenDestMap,'nbsSysFrmGenPktNum':nbsSysFrmGenPktNum,'nbsSysFrmGenPktLen':nbsSysFrmGenPktLen,'nbsSysFrmGenXmtPktNum':nbsSysFrmGenXmtPktNum,'nbsSysSelftestLevel':nbsSysSelftestLevel,'nbsSysRomVers':nbsSysRomVers,'nbsSysSnmpCfg':nbsSysSnmpCfg,'nbsSysIpAddr':nbsSysIpAddr,'nbsSysNetMask':nbsSysNetMask,'nbsSysBcastAddr':nbsSysBcastAddr,'nbsSysObIpAddr':nbsSysObIpAddr,'nbsSysObNetMask':nbsSysObNetMask,'nbsSysObBcastAddr':nbsSysObBcastAddr,'nbsSysDefaultGateway':nbsSysDefaultGateway,'nbsSysReadComunity':nbsSysReadComunity,'nbsSysWriteComunity':nbsSysWriteComunity,'nbsSysBootpEnable':nbsSysBootpEnable,'nbsSysTrapTblMaxSize':nbsSysTrapTblMaxSize,'nbsSysTrapTable':nbsSysTrapTable,'nbsSysTrapEntry':nbsSysTrapEntry,_T:nbsSysTrapTblEntIndex,'nbsSysTrapTblEntStatus':nbsSysTrapTblEntStatus,'nbsSysTrapTblEntIpAddr':nbsSysTrapTblEntIpAddr,'nbsSysTrapTblEntComm':nbsSysTrapTblEntComm,'nbsSysTftpSwFileName':nbsSysTftpSwFileName,'nbsSysTftpParFileName':nbsSysTftpParFileName,'nbsSysSerialLineMode':nbsSysSerialLineMode,'nbsSysSerialSlipBaudRate':nbsSysSerialSlipBaudRate,'nbsSysTelnetSession':nbsSysTelnetSession,'nbsSysPing':nbsSysPing,'nbsSysPingSession':nbsSysPingSession,'nbsSysPingAddr':nbsSysPingAddr,'nbsSysPingNumber':nbsSysPingNumber,'nbsSysPingRequests':nbsSysPingRequests,'nbsSysPingResps':nbsSysPingResps,'nbsSysPingOwner':nbsSysPingOwner,'nbsSysTelnetHost':nbsSysTelnetHost,'nbsSysTftpRswFileName':nbsSysTftpRswFileName,'nbsSysTftpServerIP':nbsSysTftpServerIP,'nbsSysInitDownload':nbsSysInitDownload,'nbsSysParDownload':nbsSysParDownload,'nbsSysParUpload':nbsSysParUpload,'nbsPortCfg':nbsPortCfg,'nbsPortCfgTable':nbsPortCfgTable,'nbsPortCfgEntry':nbsPortCfgEntry,_U:nbsPortCfgIndex,'nbsPortCfgLanType':nbsPortCfgLanType,'nbsPortCfgIfType':nbsPortCfgIfType,'nbsPortCfgPortSelect':nbsPortCfgPortSelect,'nbsPortCfgIfLink':nbsPortCfgIfLink,'nbsPortCfgPortFctrl':nbsPortCfgPortFctrl,'nbsPortCfgPortDplex':nbsPortCfgPortDplex,'nbsPortCfgPortDelay':nbsPortCfgPortDelay,'nbsPortCfgSpeedSelect':nbsPortCfgSpeedSelect,'nbsPortCfgEnable':nbsPortCfgEnable,'nbsPortCfgIsvpMode':nbsPortCfgIsvpMode,'nbsPortGrpCfgNum':nbsPortGrpCfgNum,'nbsPortGrpCfgTable':nbsPortGrpCfgTable,'nbsPortGrpCfgEntry':nbsPortGrpCfgEntry,_V:nbsPortGrpCfgIndex,'nbsPortGrpCfgGrpNumber':nbsPortGrpCfgGrpNumber,'nbsPortGrpCfgPortNumber':nbsPortGrpCfgPortNumber,'nbsPortGrpCfgLinkStatus':nbsPortGrpCfgLinkStatus,'nbsPortGrpCfgActivity':nbsPortGrpCfgActivity,'nbsEtherInfo':nbsEtherInfo,'nbsEthInfoTable':nbsEthInfoTable,'nbsEthInfoEntry':nbsEthInfoEntry,_W:nbsEthInfoIndex,'nbsEthInfoCntFctrls':nbsEthInfoCntFctrls,'nbsEthInfoCntExcessFctrls':nbsEthInfoCntExcessFctrls,'nbsSwitchPerf':nbsSwitchPerf,'nbsSwitchPerfTable':nbsSwitchPerfTable,'nbsSwitchPerfEntry':nbsSwitchPerfEntry,_X:nbsSwitchPerfIndex,'nbsSwitchPerfMcastPkts':nbsSwitchPerfMcastPkts,'nbsSwitchPerfUnknPkts':nbsSwitchPerfUnknPkts,'nbsPortFwdPerfTable':nbsPortFwdPerfTable,'nbsPortFwdPerfEntry':nbsPortFwdPerfEntry,_Y:nbsPortFwdPerfInPort,_Z:nbsPortFwdPerfOutPort,'nbsPortFwdPerfFwdPkts':nbsPortFwdPerfFwdPkts,'nbsPortFwdPerfFwdBytes':nbsPortFwdPerfFwdBytes,'nbsMgmtPerfStats':nbsMgmtPerfStats,'nbsMgmtPerfRcvdPkts':nbsMgmtPerfRcvdPkts,'nbsMgmtPerfRcvdBytes':nbsMgmtPerfRcvdBytes,'nbsMgmtPerfFilterdPkts':nbsMgmtPerfFilterdPkts,'nbsMgmtPerfRcvBcastPkts':nbsMgmtPerfRcvBcastPkts,'nbsMgmtPerfXmtPkts':nbsMgmtPerfXmtPkts,'nbsMgmtPerfXmtUcastPkts':nbsMgmtPerfXmtUcastPkts,'nbsMgmtPerfXmtMcastPkts':nbsMgmtPerfXmtMcastPkts,'nbsMgmtPerfXmtBcastPkts':nbsMgmtPerfXmtBcastPkts,'nbsMgmtRcvPerfTable':nbsMgmtRcvPerfTable,'nbsMgmtRcvPerfEntry':nbsMgmtRcvPerfEntry,_a:nbsMgmtRcvPerfInPort,'nbsMgmtRcvPerfFwdPkts':nbsMgmtRcvPerfFwdPkts,'nbsMgmtRcvPerfFwdBytes':nbsMgmtRcvPerfFwdBytes,'nbsMgmtXmtPerfTable':nbsMgmtXmtPerfTable,'nbsMgmtXmtPerfEntry':nbsMgmtXmtPerfEntry,_b:nbsMgmtXmtPerfOutPort,'nbsMgmtXmtPerfFwdPkts':nbsMgmtXmtPerfFwdPkts,'nbsMgmtXmtPerfFwdBytes':nbsMgmtXmtPerfFwdBytes,'nbsTraps':nbsTraps,'nbsMiniSwDb':nbsMiniSwDb,'nbsMegaSwDb':nbsMegaSwDb,'nbsMegaSwRunDb':nbsMegaSwRunDb,'nbsMegaSwRunDbTable':nbsMegaSwRunDbTable,'nbsMegaSwRunDbEntry':nbsMegaSwRunDbEntry,_c:nbsMegaSwRunDbIndex,'nbsMegaSwRunDbStatus':nbsMegaSwRunDbStatus,'nbsMegaSwRunDbAddr':nbsMegaSwRunDbAddr,'nbsMegaSwRunDbType':nbsMegaSwRunDbType,'nbsMegaSwRunDbDport':nbsMegaSwRunDbDport,'nbsMegaSwRunFilterTable':nbsMegaSwRunFilterTable,'nbsMegaSwRunFilterEntry':nbsMegaSwRunFilterEntry,'nbsMegaSwRunFilterStatus':nbsMegaSwRunFilterStatus,_j:nbsMegaSwRunFilterAddr,'nbsMegaSwRunFilterType':nbsMegaSwRunFilterType,'nbsMegaSwRunFilterDport':nbsMegaSwRunFilterDport,_k:nbsMegaSwRunFilterSport,'nbsMegaSwRunFilterDmap':nbsMegaSwRunFilterDmap,'nbsMegaSwSvlanConnectTable':nbsMegaSwSvlanConnectTable,'nbsMegaSwSvlanConnectEntry':nbsMegaSwSvlanConnectEntry,_l:nbsMegaSwSvlanConnectSport,'nbsMegaSwSvlanConnectDport':nbsMegaSwSvlanConnectDport,'nbsMegaSwRunSvlanDb':nbsMegaSwRunSvlanDb,'nbsMegaSwRunSvlanMaxNum':nbsMegaSwRunSvlanMaxNum,'nbsMegaSwRunSvlanTable':nbsMegaSwRunSvlanTable,'nbsMegaSwRunSvlanEntry':nbsMegaSwRunSvlanEntry,_m:nbsMegaSwRunSvlanIndex,'nbsMegaSwRunSvlanStatus':nbsMegaSwRunSvlanStatus,'nbsMegaSwRunSvlanList':nbsMegaSwRunSvlanList,'nbsMegaSwRunSvlanIsvlanFlag':nbsMegaSwRunSvlanIsvlanFlag,'nbsMegaSwRunIsvlanMaxNum':nbsMegaSwRunIsvlanMaxNum,'nbsMegaSwRunIsvlanTable':nbsMegaSwRunIsvlanTable,'nbsMegaSwRunIsvlanEntry':nbsMegaSwRunIsvlanEntry,_n:nbsMegaSwRunIsvlanIndex,'nbsMegaSwRunIsvlanStatus':nbsMegaSwRunIsvlanStatus,'nbsMegaSwRunIsvlanList':nbsMegaSwRunIsvlanList,'nbsMegaSwRunIsvlanName':nbsMegaSwRunIsvlanName,'nbsMegaSwRunIsvlanTag':nbsMegaSwRunIsvlanTag,'nbsMegaSwRunIsvlanVlanIndex':nbsMegaSwRunIsvlanVlanIndex,'nbsMegaSwRunVbcDb':nbsMegaSwRunVbcDb,'nbsMegaSwRunVbcMaxNum':nbsMegaSwRunVbcMaxNum,'nbsMegaSwRunVbcTable':nbsMegaSwRunVbcTable,'nbsMegaSwRunVbcEntry':nbsMegaSwRunVbcEntry,_o:nbsMegaSwRunVbcIndex,'nbsMegaSwRunVbcStatus':nbsMegaSwRunVbcStatus,'nbsMegaSwRunVbcList':nbsMegaSwRunVbcList,'nbsMegaSwVmon':nbsMegaSwVmon,'nbsMegaSwVmonMonitorPort':nbsMegaSwVmonMonitorPort,'nbsMegaSwVmonMonitrdPort':nbsMegaSwVmonMonitrdPort,'nbsMegaSwVmonStatus':nbsMegaSwVmonStatus,'nbsMegaSwPermDb':nbsMegaSwPermDb,'nbsMegaSwPermSvlanDb':nbsMegaSwPermSvlanDb,'nbsMegaSwPermSvlanMaxNum':nbsMegaSwPermSvlanMaxNum,'nbsMegaSwPermSvlanTable':nbsMegaSwPermSvlanTable,'nbsMegaSwPermSvlanEntry':nbsMegaSwPermSvlanEntry,_p:nbsMegaSwPermSvlanIndex,'nbsMegaSwPermSvlanStatus':nbsMegaSwPermSvlanStatus,'nbsMegaSwPermSvlanList':nbsMegaSwPermSvlanList,'nbsMegaSwPermIsvlanMaxNum':nbsMegaSwPermIsvlanMaxNum,'nbsMegaSwPermIsvlanTable':nbsMegaSwPermIsvlanTable,'nbsMegaSwPermIsvlanEntry':nbsMegaSwPermIsvlanEntry,_q:nbsMegaSwPermIsvlanIndex,'nbsMegaSwPermIsvlanStatus':nbsMegaSwPermIsvlanStatus,'nbsMegaSwPermIsvlanList':nbsMegaSwPermIsvlanList,'nbsMegaSwPermIsvlanName':nbsMegaSwPermIsvlanName,'nbsMegaSwPermIsvlanTag':nbsMegaSwPermIsvlanTag,'nbsMegaSwPermVbcDb':nbsMegaSwPermVbcDb,'nbsMegaSwPermVbcMaxNum':nbsMegaSwPermVbcMaxNum,'nbsMegaSwPermVbcTable':nbsMegaSwPermVbcTable,'nbsMegaSwPermVbcEntry':nbsMegaSwPermVbcEntry,_r:nbsMegaSwPermVbcIndex,'nbsMegaSwPermVbcStatus':nbsMegaSwPermVbcStatus,'nbsMegaSwPermVbcList':nbsMegaSwPermVbcList,'nbsTpPermAgingTime':nbsTpPermAgingTime})