_AT='zxAnIsdnSIfAbnormalReason'
_AS='zxAnIsdnUIfAbnormalReason'
_AR='zxAnIsdnRemotePowerSupplySlot'
_AQ='zxAnIsdnRemotePowerSupplyShelf'
_AP='zxAnIsdnRemotePowerSupplyRack'
_AO='zxAnIsdnCallStatsPort'
_AN='zxAnIsdnCallStatsSlot'
_AM='zxAnIsdnCallStatsShelf'
_AL='zxAnIsdnCallStatsRack'
_AK='zxAnIsdnTrunkDsx1TsNo'
_AJ='zxAnIsdnTrunkDsx1LinkNo'
_AI='zxAnIsdnTrunkSlot'
_AH='zxAnIsdnTrunkShelf'
_AG='zxAnIsdnTrunkRack'
_AF='zxAnIsdnTrunkTidDsx1TsNo'
_AE='zxAnIsdnTrunkTidDsx1LinkNo'
_AD='zxAnIsdnTrunkTidSlot'
_AC='zxAnIsdnTrunkTidShelf'
_AB='zxAnIsdnTrunkTidRack'
_AA='zxAnIsdnBertStatsCircuit'
_A9='zxAnIsdnBertStatsSlot'
_A8='zxAnIsdnBertStatsShelf'
_A7='zxAnIsdnBertStatsRack'
_A6='zxAnIsdnBertConfCircuit'
_A5='zxAnIsdnBertConfSlot'
_A4='zxAnIsdnBertConfShelf'
_A3='zxAnIsdnBertConfRack'
_A2='zxAnIsdnSIfNo'
_A1='zxAnIsdnSIfSlot'
_A0='zxAnIsdnSIfShelf'
_z='zxAnIsdnSIfRack'
_y='uIfdeactivationIndication'
_x='uIfActivationIndication'
_w='frameJump'
_v='reSyncIndication'
_u='lossOfSignalLevel'
_t='errorIndication3'
_s='errorIndication2'
_r='zxAnIsdnUIfNo'
_q='zxAnIsdnUIfSlot'
_p='zxAnIsdnUIfShelf'
_o='zxAnIsdnUIfRack'
_n='notKeepActive'
_m='keepActive'
_l='zxAnIsdnPortNo'
_k='zxAnIsdnPortSlot'
_j='zxAnIsdnPortShelf'
_i='zxAnIsdnPortRack'
_h='isdnportno'
_g='isdnslot'
_f='isdnshelf'
_e='isdnkrack'
_d='loopbackportno'
_c='loopbackslot'
_b='loopbackshelf'
_a='loopbackrack'
_Z='isdnDLinkLinkIdx'
_Y='isdnDLinkPCMNo'
_X='isdnDLinkSlot'
_W='isdnDLinkShelf'
_V='isdnDLinkRack'
_U='isdnAARASID'
_T='isdnAARASPID'
_S='aspActive'
_R='aspDown'
_Q='isdnASPID'
_P='active'
_O='inactive'
_N='isdnAppServerID'
_M='TruthValue'
_L='zxAnIsdnSIfSyncStatus'
_K='disable'
_J='enable'
_I='DisplayString'
_H='Unsigned32'
_G='read-write'
_F='read-only'
_E='read-create'
_D='not-accessible'
_C='Integer32'
_B='ZTE-AN-ISDN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','RowStatus','TextualConvention',_M)
zxAnISDNMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,5200))
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_ZxAn_ObjectIdentity=ObjectIdentity
zxAn=_ZxAn_ObjectIdentity((1,3,6,1,4,1,3902,1015))
_MsagmajorVersion_ObjectIdentity=ObjectIdentity
msagmajorVersion=_MsagmajorVersion_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3))
_MsagISDNService_ObjectIdentity=ObjectIdentity
msagISDNService=_MsagISDNService_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,4))
_IsdnAppServerTable_Object=MibTable
isdnAppServerTable=_IsdnAppServerTable_Object((1,3,6,1,4,1,3902,1015,5200,3,4,1))
if mibBuilder.loadTexts:isdnAppServerTable.setStatus(_A)
_IsdnAppServerEntry_Object=MibTableRow
isdnAppServerEntry=_IsdnAppServerEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,4,1,1))
isdnAppServerEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:isdnAppServerEntry.setStatus(_A)
class _IsdnAppServerID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_IsdnAppServerID_Type.__name__=_C
_IsdnAppServerID_Object=MibTableColumn
isdnAppServerID=_IsdnAppServerID_Object((1,3,6,1,4,1,3902,1015,5200,3,4,1,1,1),_IsdnAppServerID_Type())
isdnAppServerID.setMaxAccess(_D)
if mibBuilder.loadTexts:isdnAppServerID.setStatus(_A)
class _IsdnAppServerProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('tpM3UA',1),('tpM2UA',2),('tpM2PA',3),('tpSUA',4),('tpIUA',5),('tpV5UA',6)))
_IsdnAppServerProtocol_Type.__name__=_C
_IsdnAppServerProtocol_Object=MibTableColumn
isdnAppServerProtocol=_IsdnAppServerProtocol_Object((1,3,6,1,4,1,3902,1015,5200,3,4,1,1,2),_IsdnAppServerProtocol_Type())
isdnAppServerProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:isdnAppServerProtocol.setStatus(_A)
class _IsdnAppServerMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('masterSlave',1),('share',2),('broadcast',3)))
_IsdnAppServerMode_Type.__name__=_C
_IsdnAppServerMode_Object=MibTableColumn
isdnAppServerMode=_IsdnAppServerMode_Object((1,3,6,1,4,1,3902,1015,5200,3,4,1,1,3),_IsdnAppServerMode_Type())
isdnAppServerMode.setMaxAccess(_E)
if mibBuilder.loadTexts:isdnAppServerMode.setStatus(_A)
class _IsdnAppServerModeEval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IsdnAppServerModeEval_Type.__name__=_C
_IsdnAppServerModeEval_Object=MibTableColumn
isdnAppServerModeEval=_IsdnAppServerModeEval_Object((1,3,6,1,4,1,3902,1015,5200,3,4,1,1,4),_IsdnAppServerModeEval_Type())
isdnAppServerModeEval.setMaxAccess(_E)
if mibBuilder.loadTexts:isdnAppServerModeEval.setStatus(_A)
class _IsdnAppServerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4)));namedValues=NamedValues(*(('down',0),(_O,1),(_P,2),('pending',4)))
_IsdnAppServerStatus_Type.__name__=_C
_IsdnAppServerStatus_Object=MibTableColumn
isdnAppServerStatus=_IsdnAppServerStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,4,1,1,5),_IsdnAppServerStatus_Type())
isdnAppServerStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:isdnAppServerStatus.setStatus(_A)
_IsdnAppServerRowStatus_Type=RowStatus
_IsdnAppServerRowStatus_Object=MibTableColumn
isdnAppServerRowStatus=_IsdnAppServerRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,4,1,1,6),_IsdnAppServerRowStatus_Type())
isdnAppServerRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:isdnAppServerRowStatus.setStatus(_A)
_IsdnAppServerProcTable_Object=MibTable
isdnAppServerProcTable=_IsdnAppServerProcTable_Object((1,3,6,1,4,1,3902,1015,5200,3,4,2))
if mibBuilder.loadTexts:isdnAppServerProcTable.setStatus(_A)
_IsdnAppServerProcEntry_Object=MibTableRow
isdnAppServerProcEntry=_IsdnAppServerProcEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,4,2,1))
isdnAppServerProcEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:isdnAppServerProcEntry.setStatus(_A)
class _IsdnASPID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_IsdnASPID_Type.__name__=_C
_IsdnASPID_Object=MibTableColumn
isdnASPID=_IsdnASPID_Object((1,3,6,1,4,1,3902,1015,5200,3,4,2,1,1),_IsdnASPID_Type())
isdnASPID.setMaxAccess(_D)
if mibBuilder.loadTexts:isdnASPID.setStatus(_A)
class _IsdnASPDestPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IsdnASPDestPort_Type.__name__=_C
_IsdnASPDestPort_Object=MibTableColumn
isdnASPDestPort=_IsdnASPDestPort_Object((1,3,6,1,4,1,3902,1015,5200,3,4,2,1,2),_IsdnASPDestPort_Type())
isdnASPDestPort.setMaxAccess(_E)
if mibBuilder.loadTexts:isdnASPDestPort.setStatus(_A)
class _IsdnASPLoclPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IsdnASPLoclPort_Type.__name__=_C
_IsdnASPLoclPort_Object=MibTableColumn
isdnASPLoclPort=_IsdnASPLoclPort_Object((1,3,6,1,4,1,3902,1015,5200,3,4,2,1,3),_IsdnASPLoclPort_Type())
isdnASPLoclPort.setMaxAccess(_E)
if mibBuilder.loadTexts:isdnASPLoclPort.setStatus(_A)
_IsdnASPSctpID_Type=Integer32
_IsdnASPSctpID_Object=MibTableColumn
isdnASPSctpID=_IsdnASPSctpID_Object((1,3,6,1,4,1,3902,1015,5200,3,4,2,1,4),_IsdnASPSctpID_Type())
isdnASPSctpID.setMaxAccess(_F)
if mibBuilder.loadTexts:isdnASPSctpID.setStatus(_A)
class _IsdnASPUpProto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(5));namedValues=NamedValues(('iua',5))
_IsdnASPUpProto_Type.__name__=_C
_IsdnASPUpProto_Object=MibTableColumn
isdnASPUpProto=_IsdnASPUpProto_Object((1,3,6,1,4,1,3902,1015,5200,3,4,2,1,5),_IsdnASPUpProto_Type())
isdnASPUpProto.setMaxAccess(_F)
if mibBuilder.loadTexts:isdnASPUpProto.setStatus(_A)
class _IsdnASPDownProto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('udp',1),('ip',2)))
_IsdnASPDownProto_Type.__name__=_C
_IsdnASPDownProto_Object=MibTableColumn
isdnASPDownProto=_IsdnASPDownProto_Object((1,3,6,1,4,1,3902,1015,5200,3,4,2,1,6),_IsdnASPDownProto_Type())
isdnASPDownProto.setMaxAccess(_E)
if mibBuilder.loadTexts:isdnASPDownProto.setStatus(_A)
_IsdnASPDestIP_Type=IpAddress
_IsdnASPDestIP_Object=MibTableColumn
isdnASPDestIP=_IsdnASPDestIP_Object((1,3,6,1,4,1,3902,1015,5200,3,4,2,1,7),_IsdnASPDestIP_Type())
isdnASPDestIP.setMaxAccess(_E)
if mibBuilder.loadTexts:isdnASPDestIP.setStatus(_A)
class _IsdnASPInStream_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_IsdnASPInStream_Type.__name__=_C
_IsdnASPInStream_Object=MibTableColumn
isdnASPInStream=_IsdnASPInStream_Object((1,3,6,1,4,1,3902,1015,5200,3,4,2,1,8),_IsdnASPInStream_Type())
isdnASPInStream.setMaxAccess(_E)
if mibBuilder.loadTexts:isdnASPInStream.setStatus(_A)
class _IsdnASPOutStream_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_IsdnASPOutStream_Type.__name__=_C
_IsdnASPOutStream_Object=MibTableColumn
isdnASPOutStream=_IsdnASPOutStream_Object((1,3,6,1,4,1,3902,1015,5200,3,4,2,1,9),_IsdnASPOutStream_Type())
isdnASPOutStream.setMaxAccess(_E)
if mibBuilder.loadTexts:isdnASPOutStream.setStatus(_A)
class _IsdnASPStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,8,64,128)));namedValues=NamedValues(*(('aspLost',0),(_R,1),('aspInactive',2),(_S,4),('aspStandby',8),('aspManual',64),('aspCongest',128)))
_IsdnASPStat_Type.__name__=_C
_IsdnASPStat_Object=MibTableColumn
isdnASPStat=_IsdnASPStat_Object((1,3,6,1,4,1,3902,1015,5200,3,4,2,1,10),_IsdnASPStat_Type())
isdnASPStat.setMaxAccess(_F)
if mibBuilder.loadTexts:isdnASPStat.setStatus(_A)
_IsdnASPModule_Type=Integer32
_IsdnASPModule_Object=MibTableColumn
isdnASPModule=_IsdnASPModule_Object((1,3,6,1,4,1,3902,1015,5200,3,4,2,1,11),_IsdnASPModule_Type())
isdnASPModule.setMaxAccess(_F)
if mibBuilder.loadTexts:isdnASPModule.setStatus(_A)
class _IsdnASPClieOrServ_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('client',1),('server',2)))
_IsdnASPClieOrServ_Type.__name__=_C
_IsdnASPClieOrServ_Object=MibTableColumn
isdnASPClieOrServ=_IsdnASPClieOrServ_Object((1,3,6,1,4,1,3902,1015,5200,3,4,2,1,12),_IsdnASPClieOrServ_Type())
isdnASPClieOrServ.setMaxAccess(_F)
if mibBuilder.loadTexts:isdnASPClieOrServ.setStatus(_A)
_IsdnASPRowStatus_Type=RowStatus
_IsdnASPRowStatus_Object=MibTableColumn
isdnASPRowStatus=_IsdnASPRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,4,2,1,14),_IsdnASPRowStatus_Type())
isdnASPRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:isdnASPRowStatus.setStatus(_A)
_IsdnASASPRelationTable_Object=MibTable
isdnASASPRelationTable=_IsdnASASPRelationTable_Object((1,3,6,1,4,1,3902,1015,5200,3,4,3))
if mibBuilder.loadTexts:isdnASASPRelationTable.setStatus(_A)
_IsdnASASPRelationEntry_Object=MibTableRow
isdnASASPRelationEntry=_IsdnASASPRelationEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,4,3,1))
isdnASASPRelationEntry.setIndexNames((0,_B,_T),(0,_B,_U))
if mibBuilder.loadTexts:isdnASASPRelationEntry.setStatus(_A)
class _IsdnAARASPID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_IsdnAARASPID_Type.__name__=_C
_IsdnAARASPID_Object=MibTableColumn
isdnAARASPID=_IsdnAARASPID_Object((1,3,6,1,4,1,3902,1015,5200,3,4,3,1,1),_IsdnAARASPID_Type())
isdnAARASPID.setMaxAccess(_D)
if mibBuilder.loadTexts:isdnAARASPID.setStatus(_A)
class _IsdnAARASID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_IsdnAARASID_Type.__name__=_C
_IsdnAARASID_Object=MibTableColumn
isdnAARASID=_IsdnAARASID_Object((1,3,6,1,4,1,3902,1015,5200,3,4,3,1,2),_IsdnAARASID_Type())
isdnAARASID.setMaxAccess(_D)
if mibBuilder.loadTexts:isdnAARASID.setStatus(_A)
class _IsdnAARQueue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4)));namedValues=NamedValues(*(('aspInit',0),(_R,1),('aspUp',2),(_S,4)))
_IsdnAARQueue_Type.__name__=_C
_IsdnAARQueue_Object=MibTableColumn
isdnAARQueue=_IsdnAARQueue_Object((1,3,6,1,4,1,3902,1015,5200,3,4,3,1,3),_IsdnAARQueue_Type())
isdnAARQueue.setMaxAccess(_F)
if mibBuilder.loadTexts:isdnAARQueue.setStatus(_A)
_IsdnAARRowStatus_Type=RowStatus
_IsdnAARRowStatus_Object=MibTableColumn
isdnAARRowStatus=_IsdnAARRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,4,3,1,4),_IsdnAARRowStatus_Type())
isdnAARRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:isdnAARRowStatus.setStatus(_A)
_IsdnDLinkTable_Object=MibTable
isdnDLinkTable=_IsdnDLinkTable_Object((1,3,6,1,4,1,3902,1015,5200,3,4,4))
if mibBuilder.loadTexts:isdnDLinkTable.setStatus(_A)
_IsdnDLinkEntry_Object=MibTableRow
isdnDLinkEntry=_IsdnDLinkEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,4,4,1))
isdnDLinkEntry.setIndexNames((0,_B,_V),(0,_B,_W),(0,_B,_X),(0,_B,_Y),(0,_B,_Z))
if mibBuilder.loadTexts:isdnDLinkEntry.setStatus(_A)
_IsdnDLinkRack_Type=Integer32
_IsdnDLinkRack_Object=MibTableColumn
isdnDLinkRack=_IsdnDLinkRack_Object((1,3,6,1,4,1,3902,1015,5200,3,4,4,1,1),_IsdnDLinkRack_Type())
isdnDLinkRack.setMaxAccess(_D)
if mibBuilder.loadTexts:isdnDLinkRack.setStatus(_A)
_IsdnDLinkShelf_Type=Integer32
_IsdnDLinkShelf_Object=MibTableColumn
isdnDLinkShelf=_IsdnDLinkShelf_Object((1,3,6,1,4,1,3902,1015,5200,3,4,4,1,2),_IsdnDLinkShelf_Type())
isdnDLinkShelf.setMaxAccess(_D)
if mibBuilder.loadTexts:isdnDLinkShelf.setStatus(_A)
_IsdnDLinkSlot_Type=Integer32
_IsdnDLinkSlot_Object=MibTableColumn
isdnDLinkSlot=_IsdnDLinkSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,4,4,1,3),_IsdnDLinkSlot_Type())
isdnDLinkSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:isdnDLinkSlot.setStatus(_A)
class _IsdnDLinkPCMNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_IsdnDLinkPCMNo_Type.__name__=_C
_IsdnDLinkPCMNo_Object=MibTableColumn
isdnDLinkPCMNo=_IsdnDLinkPCMNo_Object((1,3,6,1,4,1,3902,1015,5200,3,4,4,1,4),_IsdnDLinkPCMNo_Type())
isdnDLinkPCMNo.setMaxAccess(_D)
if mibBuilder.loadTexts:isdnDLinkPCMNo.setStatus(_A)
class _IsdnDLinkLinkIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_IsdnDLinkLinkIdx_Type.__name__=_C
_IsdnDLinkLinkIdx_Object=MibTableColumn
isdnDLinkLinkIdx=_IsdnDLinkLinkIdx_Object((1,3,6,1,4,1,3902,1015,5200,3,4,4,1,5),_IsdnDLinkLinkIdx_Type())
isdnDLinkLinkIdx.setMaxAccess(_D)
if mibBuilder.loadTexts:isdnDLinkLinkIdx.setStatus(_A)
class _IsdnDLinkIfID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IsdnDLinkIfID_Type.__name__=_C
_IsdnDLinkIfID_Object=MibTableColumn
isdnDLinkIfID=_IsdnDLinkIfID_Object((1,3,6,1,4,1,3902,1015,5200,3,4,4,1,6),_IsdnDLinkIfID_Type())
isdnDLinkIfID.setMaxAccess(_E)
if mibBuilder.loadTexts:isdnDLinkIfID.setStatus(_A)
class _IsdnDLinkLinkID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_IsdnDLinkLinkID_Type.__name__=_C
_IsdnDLinkLinkID_Object=MibTableColumn
isdnDLinkLinkID=_IsdnDLinkLinkID_Object((1,3,6,1,4,1,3902,1015,5200,3,4,4,1,7),_IsdnDLinkLinkID_Type())
isdnDLinkLinkID.setMaxAccess(_E)
if mibBuilder.loadTexts:isdnDLinkLinkID.setStatus(_A)
class _IsdnDLinkLinkInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('networkSide',0),('subscriberSide',1)))
_IsdnDLinkLinkInfo_Type.__name__=_C
_IsdnDLinkLinkInfo_Object=MibTableColumn
isdnDLinkLinkInfo=_IsdnDLinkLinkInfo_Object((1,3,6,1,4,1,3902,1015,5200,3,4,4,1,8),_IsdnDLinkLinkInfo_Type())
isdnDLinkLinkInfo.setMaxAccess(_E)
if mibBuilder.loadTexts:isdnDLinkLinkInfo.setStatus(_A)
class _IsdnDLinkASID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_IsdnDLinkASID_Type.__name__=_C
_IsdnDLinkASID_Object=MibTableColumn
isdnDLinkASID=_IsdnDLinkASID_Object((1,3,6,1,4,1,3902,1015,5200,3,4,4,1,9),_IsdnDLinkASID_Type())
isdnDLinkASID.setMaxAccess(_E)
if mibBuilder.loadTexts:isdnDLinkASID.setStatus(_A)
class _IsdnDLinkNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_IsdnDLinkNumber_Type.__name__=_C
_IsdnDLinkNumber_Object=MibTableColumn
isdnDLinkNumber=_IsdnDLinkNumber_Object((1,3,6,1,4,1,3902,1015,5200,3,4,4,1,10),_IsdnDLinkNumber_Type())
isdnDLinkNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:isdnDLinkNumber.setStatus(_A)
class _IsdnDLinkProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ptl2BplusD',1),('ptl30BplusD',2),('ptl23BplusD',3)))
_IsdnDLinkProtocol_Type.__name__=_C
_IsdnDLinkProtocol_Object=MibTableColumn
isdnDLinkProtocol=_IsdnDLinkProtocol_Object((1,3,6,1,4,1,3902,1015,5200,3,4,4,1,11),_IsdnDLinkProtocol_Type())
isdnDLinkProtocol.setMaxAccess(_F)
if mibBuilder.loadTexts:isdnDLinkProtocol.setStatus(_A)
_IsdnDLinkStatus_Type=Integer32
_IsdnDLinkStatus_Object=MibTableColumn
isdnDLinkStatus=_IsdnDLinkStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,4,4,1,12),_IsdnDLinkStatus_Type())
isdnDLinkStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:isdnDLinkStatus.setStatus(_A)
_IsdnDLinkRowStatus_Type=RowStatus
_IsdnDLinkRowStatus_Object=MibTableColumn
isdnDLinkRowStatus=_IsdnDLinkRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,4,4,1,13),_IsdnDLinkRowStatus_Type())
isdnDLinkRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:isdnDLinkRowStatus.setStatus(_A)
_LoopbackTable_Object=MibTable
loopbackTable=_LoopbackTable_Object((1,3,6,1,4,1,3902,1015,5200,3,4,6))
if mibBuilder.loadTexts:loopbackTable.setStatus(_A)
_LoopbackEntry_Object=MibTableRow
loopbackEntry=_LoopbackEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,4,6,1))
loopbackEntry.setIndexNames((0,_B,_a),(0,_B,_b),(0,_B,_c),(0,_B,_d))
if mibBuilder.loadTexts:loopbackEntry.setStatus(_A)
_Loopbackrack_Type=Integer32
_Loopbackrack_Object=MibTableColumn
loopbackrack=_Loopbackrack_Object((1,3,6,1,4,1,3902,1015,5200,3,4,6,1,1),_Loopbackrack_Type())
loopbackrack.setMaxAccess(_D)
if mibBuilder.loadTexts:loopbackrack.setStatus(_A)
_Loopbackshelf_Type=Integer32
_Loopbackshelf_Object=MibTableColumn
loopbackshelf=_Loopbackshelf_Object((1,3,6,1,4,1,3902,1015,5200,3,4,6,1,2),_Loopbackshelf_Type())
loopbackshelf.setMaxAccess(_D)
if mibBuilder.loadTexts:loopbackshelf.setStatus(_A)
_Loopbackslot_Type=Integer32
_Loopbackslot_Object=MibTableColumn
loopbackslot=_Loopbackslot_Object((1,3,6,1,4,1,3902,1015,5200,3,4,6,1,3),_Loopbackslot_Type())
loopbackslot.setMaxAccess(_D)
if mibBuilder.loadTexts:loopbackslot.setStatus(_A)
_Loopbackportno_Type=Integer32
_Loopbackportno_Object=MibTableColumn
loopbackportno=_Loopbackportno_Object((1,3,6,1,4,1,3902,1015,5200,3,4,6,1,4),_Loopbackportno_Type())
loopbackportno.setMaxAccess(_D)
if mibBuilder.loadTexts:loopbackportno.setStatus(_A)
class _Loopbacklooptype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('localLoopback',1),('remoteLineLoopback',2),('noLoopback',3)))
_Loopbacklooptype_Type.__name__=_C
_Loopbacklooptype_Object=MibTableColumn
loopbacklooptype=_Loopbacklooptype_Object((1,3,6,1,4,1,3902,1015,5200,3,4,6,1,5),_Loopbacklooptype_Type())
loopbacklooptype.setMaxAccess(_G)
if mibBuilder.loadTexts:loopbacklooptype.setStatus(_A)
_MsagIsdnCapabilityTable_Object=MibTable
msagIsdnCapabilityTable=_MsagIsdnCapabilityTable_Object((1,3,6,1,4,1,3902,1015,5200,3,4,7))
if mibBuilder.loadTexts:msagIsdnCapabilityTable.setStatus(_A)
_MsagIsdnCapabilityEntry_Object=MibTableRow
msagIsdnCapabilityEntry=_MsagIsdnCapabilityEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,4,7,1))
msagIsdnCapabilityEntry.setIndexNames((0,_B,_e),(0,_B,_f),(0,_B,_g),(0,_B,_h))
if mibBuilder.loadTexts:msagIsdnCapabilityEntry.setStatus(_A)
class _Isdnkrack_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_Isdnkrack_Type.__name__=_C
_Isdnkrack_Object=MibTableColumn
isdnkrack=_Isdnkrack_Object((1,3,6,1,4,1,3902,1015,5200,3,4,7,1,1),_Isdnkrack_Type())
isdnkrack.setMaxAccess(_D)
if mibBuilder.loadTexts:isdnkrack.setStatus(_A)
class _Isdnshelf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Isdnshelf_Type.__name__=_C
_Isdnshelf_Object=MibTableColumn
isdnshelf=_Isdnshelf_Object((1,3,6,1,4,1,3902,1015,5200,3,4,7,1,2),_Isdnshelf_Type())
isdnshelf.setMaxAccess(_D)
if mibBuilder.loadTexts:isdnshelf.setStatus(_A)
class _Isdnslot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,23))
_Isdnslot_Type.__name__=_C
_Isdnslot_Object=MibTableColumn
isdnslot=_Isdnslot_Object((1,3,6,1,4,1,3902,1015,5200,3,4,7,1,3),_Isdnslot_Type())
isdnslot.setMaxAccess(_D)
if mibBuilder.loadTexts:isdnslot.setStatus(_A)
class _Isdnportno_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Isdnportno_Type.__name__=_C
_Isdnportno_Object=MibTableColumn
isdnportno=_Isdnportno_Object((1,3,6,1,4,1,3902,1015,5200,3,4,7,1,4),_Isdnportno_Type())
isdnportno.setMaxAccess(_D)
if mibBuilder.loadTexts:isdnportno.setStatus(_A)
class _IsdnLossOfSignal_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_IsdnLossOfSignal_Type.__name__=_H
_IsdnLossOfSignal_Object=MibTableColumn
isdnLossOfSignal=_IsdnLossOfSignal_Object((1,3,6,1,4,1,3902,1015,5200,3,4,7,1,20),_IsdnLossOfSignal_Type())
isdnLossOfSignal.setMaxAccess(_F)
if mibBuilder.loadTexts:isdnLossOfSignal.setStatus(_A)
class _IsdnLossOfPower_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_IsdnLossOfPower_Type.__name__=_H
_IsdnLossOfPower_Object=MibTableColumn
isdnLossOfPower=_IsdnLossOfPower_Object((1,3,6,1,4,1,3902,1015,5200,3,4,7,1,21),_IsdnLossOfPower_Type())
isdnLossOfPower.setMaxAccess(_F)
if mibBuilder.loadTexts:isdnLossOfPower.setStatus(_A)
class _IsdnLossOfFrame_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_IsdnLossOfFrame_Type.__name__=_H
_IsdnLossOfFrame_Object=MibTableColumn
isdnLossOfFrame=_IsdnLossOfFrame_Object((1,3,6,1,4,1,3902,1015,5200,3,4,7,1,22),_IsdnLossOfFrame_Type())
isdnLossOfFrame.setMaxAccess(_F)
if mibBuilder.loadTexts:isdnLossOfFrame.setStatus(_A)
class _IsdnClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_IsdnClear_Type.__name__=_C
_IsdnClear_Object=MibTableColumn
isdnClear=_IsdnClear_Object((1,3,6,1,4,1,3902,1015,5200,3,4,7,1,23),_IsdnClear_Type())
isdnClear.setMaxAccess(_G)
if mibBuilder.loadTexts:isdnClear.setStatus(_A)
_ZxAnIsdnPortActiveStatusTable_Object=MibTable
zxAnIsdnPortActiveStatusTable=_ZxAnIsdnPortActiveStatusTable_Object((1,3,6,1,4,1,3902,1015,5200,3,4,8))
if mibBuilder.loadTexts:zxAnIsdnPortActiveStatusTable.setStatus(_A)
_ZxAnIsdnPortActiveStatusEntry_Object=MibTableRow
zxAnIsdnPortActiveStatusEntry=_ZxAnIsdnPortActiveStatusEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,4,8,1))
zxAnIsdnPortActiveStatusEntry.setIndexNames((0,_B,_i),(0,_B,_j),(0,_B,_k),(0,_B,_l))
if mibBuilder.loadTexts:zxAnIsdnPortActiveStatusEntry.setStatus(_A)
_ZxAnIsdnPortRack_Type=Integer32
_ZxAnIsdnPortRack_Object=MibTableColumn
zxAnIsdnPortRack=_ZxAnIsdnPortRack_Object((1,3,6,1,4,1,3902,1015,5200,3,4,8,1,1),_ZxAnIsdnPortRack_Type())
zxAnIsdnPortRack.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnIsdnPortRack.setStatus(_A)
_ZxAnIsdnPortShelf_Type=Integer32
_ZxAnIsdnPortShelf_Object=MibTableColumn
zxAnIsdnPortShelf=_ZxAnIsdnPortShelf_Object((1,3,6,1,4,1,3902,1015,5200,3,4,8,1,2),_ZxAnIsdnPortShelf_Type())
zxAnIsdnPortShelf.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnIsdnPortShelf.setStatus(_A)
_ZxAnIsdnPortSlot_Type=Integer32
_ZxAnIsdnPortSlot_Object=MibTableColumn
zxAnIsdnPortSlot=_ZxAnIsdnPortSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,4,8,1,3),_ZxAnIsdnPortSlot_Type())
zxAnIsdnPortSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnIsdnPortSlot.setStatus(_A)
_ZxAnIsdnPortNo_Type=Integer32
_ZxAnIsdnPortNo_Object=MibTableColumn
zxAnIsdnPortNo=_ZxAnIsdnPortNo_Object((1,3,6,1,4,1,3902,1015,5200,3,4,8,1,4),_ZxAnIsdnPortNo_Type())
zxAnIsdnPortNo.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnIsdnPortNo.setStatus(_A)
class _ZxAnIsdnPortL1ActiveStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_m,0),(_n,1)))
_ZxAnIsdnPortL1ActiveStatus_Type.__name__=_C
_ZxAnIsdnPortL1ActiveStatus_Object=MibTableColumn
zxAnIsdnPortL1ActiveStatus=_ZxAnIsdnPortL1ActiveStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,4,8,1,5),_ZxAnIsdnPortL1ActiveStatus_Type())
zxAnIsdnPortL1ActiveStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnIsdnPortL1ActiveStatus.setStatus(_A)
class _ZxAnIsdnPortL2ActiveStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_m,1),(_n,2)))
_ZxAnIsdnPortL2ActiveStatus_Type.__name__=_C
_ZxAnIsdnPortL2ActiveStatus_Object=MibTableColumn
zxAnIsdnPortL2ActiveStatus=_ZxAnIsdnPortL2ActiveStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,4,8,1,6),_ZxAnIsdnPortL2ActiveStatus_Type())
zxAnIsdnPortL2ActiveStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnIsdnPortL2ActiveStatus.setStatus(_A)
_ZxAnIsdnUIfCfgTable_Object=MibTable
zxAnIsdnUIfCfgTable=_ZxAnIsdnUIfCfgTable_Object((1,3,6,1,4,1,3902,1015,5200,3,4,9))
if mibBuilder.loadTexts:zxAnIsdnUIfCfgTable.setStatus(_A)
_ZxAnIsdnUIfCfgEntry_Object=MibTableRow
zxAnIsdnUIfCfgEntry=_ZxAnIsdnUIfCfgEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,4,9,1))
zxAnIsdnUIfCfgEntry.setIndexNames((0,_B,_o),(0,_B,_p),(0,_B,_q),(0,_B,_r))
if mibBuilder.loadTexts:zxAnIsdnUIfCfgEntry.setStatus(_A)
_ZxAnIsdnUIfRack_Type=Integer32
_ZxAnIsdnUIfRack_Object=MibTableColumn
zxAnIsdnUIfRack=_ZxAnIsdnUIfRack_Object((1,3,6,1,4,1,3902,1015,5200,3,4,9,1,1),_ZxAnIsdnUIfRack_Type())
zxAnIsdnUIfRack.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnIsdnUIfRack.setStatus(_A)
_ZxAnIsdnUIfShelf_Type=Integer32
_ZxAnIsdnUIfShelf_Object=MibTableColumn
zxAnIsdnUIfShelf=_ZxAnIsdnUIfShelf_Object((1,3,6,1,4,1,3902,1015,5200,3,4,9,1,2),_ZxAnIsdnUIfShelf_Type())
zxAnIsdnUIfShelf.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnIsdnUIfShelf.setStatus(_A)
_ZxAnIsdnUIfSlot_Type=Integer32
_ZxAnIsdnUIfSlot_Object=MibTableColumn
zxAnIsdnUIfSlot=_ZxAnIsdnUIfSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,4,9,1,3),_ZxAnIsdnUIfSlot_Type())
zxAnIsdnUIfSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnIsdnUIfSlot.setStatus(_A)
_ZxAnIsdnUIfNo_Type=Integer32
_ZxAnIsdnUIfNo_Object=MibTableColumn
zxAnIsdnUIfNo=_ZxAnIsdnUIfNo_Object((1,3,6,1,4,1,3902,1015,5200,3,4,9,1,4),_ZxAnIsdnUIfNo_Type())
zxAnIsdnUIfNo.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnIsdnUIfNo.setStatus(_A)
class _ZxAnIsdnUIfRemotePowerFeedEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_ZxAnIsdnUIfRemotePowerFeedEnable_Type.__name__=_C
_ZxAnIsdnUIfRemotePowerFeedEnable_Object=MibTableColumn
zxAnIsdnUIfRemotePowerFeedEnable=_ZxAnIsdnUIfRemotePowerFeedEnable_Object((1,3,6,1,4,1,3902,1015,5200,3,4,9,1,5),_ZxAnIsdnUIfRemotePowerFeedEnable_Type())
zxAnIsdnUIfRemotePowerFeedEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnIsdnUIfRemotePowerFeedEnable.setStatus(_A)
class _ZxAnIsdnUIfTrapEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_ZxAnIsdnUIfTrapEnable_Type.__name__=_C
_ZxAnIsdnUIfTrapEnable_Object=MibTableColumn
zxAnIsdnUIfTrapEnable=_ZxAnIsdnUIfTrapEnable_Object((1,3,6,1,4,1,3902,1015,5200,3,4,9,1,6),_ZxAnIsdnUIfTrapEnable_Type())
zxAnIsdnUIfTrapEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnIsdnUIfTrapEnable.setStatus(_A)
class _ZxAnIsdnUIfActiveStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_O,2)))
_ZxAnIsdnUIfActiveStatus_Type.__name__=_C
_ZxAnIsdnUIfActiveStatus_Object=MibTableColumn
zxAnIsdnUIfActiveStatus=_ZxAnIsdnUIfActiveStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,4,9,1,7),_ZxAnIsdnUIfActiveStatus_Type())
zxAnIsdnUIfActiveStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnIsdnUIfActiveStatus.setStatus(_A)
class _ZxAnIsdnUIfSoftReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_ZxAnIsdnUIfSoftReset_Type.__name__=_C
_ZxAnIsdnUIfSoftReset_Object=MibTableColumn
zxAnIsdnUIfSoftReset=_ZxAnIsdnUIfSoftReset_Object((1,3,6,1,4,1,3902,1015,5200,3,4,9,1,8),_ZxAnIsdnUIfSoftReset_Type())
zxAnIsdnUIfSoftReset.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnIsdnUIfSoftReset.setStatus(_A)
class _ZxAnIsdnUIfAbnormalReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,255)));namedValues=NamedValues(*((_s,1),(_t,2),(_u,3),(_v,4),(_w,5),(_x,6),(_y,7),('other',255)))
_ZxAnIsdnUIfAbnormalReason_Type.__name__=_C
_ZxAnIsdnUIfAbnormalReason_Object=MibTableColumn
zxAnIsdnUIfAbnormalReason=_ZxAnIsdnUIfAbnormalReason_Object((1,3,6,1,4,1,3902,1015,5200,3,4,9,1,9),_ZxAnIsdnUIfAbnormalReason_Type())
zxAnIsdnUIfAbnormalReason.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnIsdnUIfAbnormalReason.setStatus(_A)
_ZxAnIsdnSIfCfgTable_Object=MibTable
zxAnIsdnSIfCfgTable=_ZxAnIsdnSIfCfgTable_Object((1,3,6,1,4,1,3902,1015,5200,3,4,10))
if mibBuilder.loadTexts:zxAnIsdnSIfCfgTable.setStatus(_A)
_ZxAnIsdnSIfCfgEntry_Object=MibTableRow
zxAnIsdnSIfCfgEntry=_ZxAnIsdnSIfCfgEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,4,10,1))
zxAnIsdnSIfCfgEntry.setIndexNames((0,_B,_z),(0,_B,_A0),(0,_B,_A1),(0,_B,_A2))
if mibBuilder.loadTexts:zxAnIsdnSIfCfgEntry.setStatus(_A)
_ZxAnIsdnSIfRack_Type=Integer32
_ZxAnIsdnSIfRack_Object=MibTableColumn
zxAnIsdnSIfRack=_ZxAnIsdnSIfRack_Object((1,3,6,1,4,1,3902,1015,5200,3,4,10,1,1),_ZxAnIsdnSIfRack_Type())
zxAnIsdnSIfRack.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnIsdnSIfRack.setStatus(_A)
_ZxAnIsdnSIfShelf_Type=Integer32
_ZxAnIsdnSIfShelf_Object=MibTableColumn
zxAnIsdnSIfShelf=_ZxAnIsdnSIfShelf_Object((1,3,6,1,4,1,3902,1015,5200,3,4,10,1,2),_ZxAnIsdnSIfShelf_Type())
zxAnIsdnSIfShelf.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnIsdnSIfShelf.setStatus(_A)
_ZxAnIsdnSIfSlot_Type=Integer32
_ZxAnIsdnSIfSlot_Object=MibTableColumn
zxAnIsdnSIfSlot=_ZxAnIsdnSIfSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,4,10,1,3),_ZxAnIsdnSIfSlot_Type())
zxAnIsdnSIfSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnIsdnSIfSlot.setStatus(_A)
_ZxAnIsdnSIfNo_Type=Integer32
_ZxAnIsdnSIfNo_Object=MibTableColumn
zxAnIsdnSIfNo=_ZxAnIsdnSIfNo_Object((1,3,6,1,4,1,3902,1015,5200,3,4,10,1,4),_ZxAnIsdnSIfNo_Type())
zxAnIsdnSIfNo.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnIsdnSIfNo.setStatus(_A)
class _ZxAnIsdnSIfTrapEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_ZxAnIsdnSIfTrapEnable_Type.__name__=_C
_ZxAnIsdnSIfTrapEnable_Object=MibTableColumn
zxAnIsdnSIfTrapEnable=_ZxAnIsdnSIfTrapEnable_Object((1,3,6,1,4,1,3902,1015,5200,3,4,10,1,5),_ZxAnIsdnSIfTrapEnable_Type())
zxAnIsdnSIfTrapEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnIsdnSIfTrapEnable.setStatus(_A)
class _ZxAnIsdnSIfSyncStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('synchronized',1),('unsynchronized',2)))
_ZxAnIsdnSIfSyncStatus_Type.__name__=_C
_ZxAnIsdnSIfSyncStatus_Object=MibTableColumn
zxAnIsdnSIfSyncStatus=_ZxAnIsdnSIfSyncStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,4,10,1,6),_ZxAnIsdnSIfSyncStatus_Type())
zxAnIsdnSIfSyncStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnIsdnSIfSyncStatus.setStatus(_A)
class _ZxAnIsdnSIfAbnormalReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,255)));namedValues=NamedValues(*((_s,1),(_t,2),(_u,3),(_v,4),(_w,5),(_x,6),(_y,7),('other',255)))
_ZxAnIsdnSIfAbnormalReason_Type.__name__=_C
_ZxAnIsdnSIfAbnormalReason_Object=MibTableColumn
zxAnIsdnSIfAbnormalReason=_ZxAnIsdnSIfAbnormalReason_Object((1,3,6,1,4,1,3902,1015,5200,3,4,10,1,7),_ZxAnIsdnSIfAbnormalReason_Type())
zxAnIsdnSIfAbnormalReason.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnIsdnSIfAbnormalReason.setStatus(_A)
_ZxAnIsdnBertMgmtGroup_ObjectIdentity=ObjectIdentity
zxAnIsdnBertMgmtGroup=_ZxAnIsdnBertMgmtGroup_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,4,11))
_ZxAnIsdnBertConfTable_Object=MibTable
zxAnIsdnBertConfTable=_ZxAnIsdnBertConfTable_Object((1,3,6,1,4,1,3902,1015,5200,3,4,11,1))
if mibBuilder.loadTexts:zxAnIsdnBertConfTable.setStatus(_A)
_ZxAnIsdnBertConfEntry_Object=MibTableRow
zxAnIsdnBertConfEntry=_ZxAnIsdnBertConfEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,4,11,1,1))
zxAnIsdnBertConfEntry.setIndexNames((0,_B,_A3),(0,_B,_A4),(0,_B,_A5),(0,_B,_A6))
if mibBuilder.loadTexts:zxAnIsdnBertConfEntry.setStatus(_A)
_ZxAnIsdnBertConfRack_Type=Integer32
_ZxAnIsdnBertConfRack_Object=MibTableColumn
zxAnIsdnBertConfRack=_ZxAnIsdnBertConfRack_Object((1,3,6,1,4,1,3902,1015,5200,3,4,11,1,1,1),_ZxAnIsdnBertConfRack_Type())
zxAnIsdnBertConfRack.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnIsdnBertConfRack.setStatus(_A)
_ZxAnIsdnBertConfShelf_Type=Integer32
_ZxAnIsdnBertConfShelf_Object=MibTableColumn
zxAnIsdnBertConfShelf=_ZxAnIsdnBertConfShelf_Object((1,3,6,1,4,1,3902,1015,5200,3,4,11,1,1,2),_ZxAnIsdnBertConfShelf_Type())
zxAnIsdnBertConfShelf.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnIsdnBertConfShelf.setStatus(_A)
_ZxAnIsdnBertConfSlot_Type=Integer32
_ZxAnIsdnBertConfSlot_Object=MibTableColumn
zxAnIsdnBertConfSlot=_ZxAnIsdnBertConfSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,4,11,1,1,3),_ZxAnIsdnBertConfSlot_Type())
zxAnIsdnBertConfSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnIsdnBertConfSlot.setStatus(_A)
_ZxAnIsdnBertConfCircuit_Type=Integer32
_ZxAnIsdnBertConfCircuit_Object=MibTableColumn
zxAnIsdnBertConfCircuit=_ZxAnIsdnBertConfCircuit_Object((1,3,6,1,4,1,3902,1015,5200,3,4,11,1,1,4),_ZxAnIsdnBertConfCircuit_Type())
zxAnIsdnBertConfCircuit.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnIsdnBertConfCircuit.setStatus(_A)
class _ZxAnIsdnBertAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('stop',2)))
_ZxAnIsdnBertAction_Type.__name__=_C
_ZxAnIsdnBertAction_Object=MibTableColumn
zxAnIsdnBertAction=_ZxAnIsdnBertAction_Object((1,3,6,1,4,1,3902,1015,5200,3,4,11,1,1,5),_ZxAnIsdnBertAction_Type())
zxAnIsdnBertAction.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnIsdnBertAction.setStatus(_A)
class _ZxAnIsdnBertLoopbackPosition_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('local',1),('nt',2),('teTa',3)))
_ZxAnIsdnBertLoopbackPosition_Type.__name__=_C
_ZxAnIsdnBertLoopbackPosition_Object=MibTableColumn
zxAnIsdnBertLoopbackPosition=_ZxAnIsdnBertLoopbackPosition_Object((1,3,6,1,4,1,3902,1015,5200,3,4,11,1,1,6),_ZxAnIsdnBertLoopbackPosition_Type())
zxAnIsdnBertLoopbackPosition.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnIsdnBertLoopbackPosition.setStatus(_A)
class _ZxAnIsdnBertThresholdLevel_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,5,6)));namedValues=NamedValues(*(('tenENegtive3',3),('tenENegtive4',4),('tenENegtive5',5),('tenENegtive6',6)))
_ZxAnIsdnBertThresholdLevel_Type.__name__=_C
_ZxAnIsdnBertThresholdLevel_Object=MibTableColumn
zxAnIsdnBertThresholdLevel=_ZxAnIsdnBertThresholdLevel_Object((1,3,6,1,4,1,3902,1015,5200,3,4,11,1,1,7),_ZxAnIsdnBertThresholdLevel_Type())
zxAnIsdnBertThresholdLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnIsdnBertThresholdLevel.setStatus(_A)
class _ZxAnIsdnBertMeasurePrecision_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('neg30To45',1),('neg22To30',2),('neg17To20',3),('neg12To14',4)))
_ZxAnIsdnBertMeasurePrecision_Type.__name__=_C
_ZxAnIsdnBertMeasurePrecision_Object=MibTableColumn
zxAnIsdnBertMeasurePrecision=_ZxAnIsdnBertMeasurePrecision_Object((1,3,6,1,4,1,3902,1015,5200,3,4,11,1,1,8),_ZxAnIsdnBertMeasurePrecision_Type())
zxAnIsdnBertMeasurePrecision.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnIsdnBertMeasurePrecision.setStatus(_A)
class _ZxAnIsdnBertForceTest_Type(TruthValue):defaultValue=2
_ZxAnIsdnBertForceTest_Type.__name__=_M
_ZxAnIsdnBertForceTest_Object=MibTableColumn
zxAnIsdnBertForceTest=_ZxAnIsdnBertForceTest_Object((1,3,6,1,4,1,3902,1015,5200,3,4,11,1,1,9),_ZxAnIsdnBertForceTest_Type())
zxAnIsdnBertForceTest.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnIsdnBertForceTest.setStatus(_A)
class _ZxAnIsdnBertStartDateAndTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnIsdnBertStartDateAndTime_Type.__name__=_I
_ZxAnIsdnBertStartDateAndTime_Object=MibTableColumn
zxAnIsdnBertStartDateAndTime=_ZxAnIsdnBertStartDateAndTime_Object((1,3,6,1,4,1,3902,1015,5200,3,4,11,1,1,10),_ZxAnIsdnBertStartDateAndTime_Type())
zxAnIsdnBertStartDateAndTime.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnIsdnBertStartDateAndTime.setStatus(_A)
class _ZxAnIsdnBertOperStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notStarted',1),('inProgress',2),('success',3),('failed',4)))
_ZxAnIsdnBertOperStatus_Type.__name__=_C
_ZxAnIsdnBertOperStatus_Object=MibTableColumn
zxAnIsdnBertOperStatus=_ZxAnIsdnBertOperStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,4,11,1,1,11),_ZxAnIsdnBertOperStatus_Type())
zxAnIsdnBertOperStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnIsdnBertOperStatus.setStatus(_A)
class _ZxAnIsdnBertResult_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noResult',1),('pass',2),('notPass',3),('failed',4)))
_ZxAnIsdnBertResult_Type.__name__=_C
_ZxAnIsdnBertResult_Object=MibTableColumn
zxAnIsdnBertResult=_ZxAnIsdnBertResult_Object((1,3,6,1,4,1,3902,1015,5200,3,4,11,1,1,12),_ZxAnIsdnBertResult_Type())
zxAnIsdnBertResult.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnIsdnBertResult.setStatus(_A)
_ZxAnIsdnBertRowStatus_Type=RowStatus
_ZxAnIsdnBertRowStatus_Object=MibTableColumn
zxAnIsdnBertRowStatus=_ZxAnIsdnBertRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,4,11,1,1,20),_ZxAnIsdnBertRowStatus_Type())
zxAnIsdnBertRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnIsdnBertRowStatus.setStatus(_A)
_ZxAnIsdnBertStatsTable_Object=MibTable
zxAnIsdnBertStatsTable=_ZxAnIsdnBertStatsTable_Object((1,3,6,1,4,1,3902,1015,5200,3,4,11,2))
if mibBuilder.loadTexts:zxAnIsdnBertStatsTable.setStatus(_A)
_ZxAnIsdnBertStatsEntry_Object=MibTableRow
zxAnIsdnBertStatsEntry=_ZxAnIsdnBertStatsEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,4,11,2,1))
zxAnIsdnBertStatsEntry.setIndexNames((0,_B,_A7),(0,_B,_A8),(0,_B,_A9),(0,_B,_AA))
if mibBuilder.loadTexts:zxAnIsdnBertStatsEntry.setStatus(_A)
_ZxAnIsdnBertStatsRack_Type=Integer32
_ZxAnIsdnBertStatsRack_Object=MibTableColumn
zxAnIsdnBertStatsRack=_ZxAnIsdnBertStatsRack_Object((1,3,6,1,4,1,3902,1015,5200,3,4,11,2,1,1),_ZxAnIsdnBertStatsRack_Type())
zxAnIsdnBertStatsRack.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnIsdnBertStatsRack.setStatus(_A)
_ZxAnIsdnBertStatsShelf_Type=Integer32
_ZxAnIsdnBertStatsShelf_Object=MibTableColumn
zxAnIsdnBertStatsShelf=_ZxAnIsdnBertStatsShelf_Object((1,3,6,1,4,1,3902,1015,5200,3,4,11,2,1,2),_ZxAnIsdnBertStatsShelf_Type())
zxAnIsdnBertStatsShelf.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnIsdnBertStatsShelf.setStatus(_A)
_ZxAnIsdnBertStatsSlot_Type=Integer32
_ZxAnIsdnBertStatsSlot_Object=MibTableColumn
zxAnIsdnBertStatsSlot=_ZxAnIsdnBertStatsSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,4,11,2,1,3),_ZxAnIsdnBertStatsSlot_Type())
zxAnIsdnBertStatsSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnIsdnBertStatsSlot.setStatus(_A)
_ZxAnIsdnBertStatsCircuit_Type=Integer32
_ZxAnIsdnBertStatsCircuit_Object=MibTableColumn
zxAnIsdnBertStatsCircuit=_ZxAnIsdnBertStatsCircuit_Object((1,3,6,1,4,1,3902,1015,5200,3,4,11,2,1,4),_ZxAnIsdnBertStatsCircuit_Type())
zxAnIsdnBertStatsCircuit.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnIsdnBertStatsCircuit.setStatus(_A)
_ZxAnIsdnBertTimeElapsed_Type=Integer32
_ZxAnIsdnBertTimeElapsed_Object=MibTableColumn
zxAnIsdnBertTimeElapsed=_ZxAnIsdnBertTimeElapsed_Object((1,3,6,1,4,1,3902,1015,5200,3,4,11,2,1,5),_ZxAnIsdnBertTimeElapsed_Type())
zxAnIsdnBertTimeElapsed.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnIsdnBertTimeElapsed.setStatus(_A)
if mibBuilder.loadTexts:zxAnIsdnBertTimeElapsed.setUnits('10ms')
_ZxAnIsdnBertTxTotalBits_Type=Counter64
_ZxAnIsdnBertTxTotalBits_Object=MibTableColumn
zxAnIsdnBertTxTotalBits=_ZxAnIsdnBertTxTotalBits_Object((1,3,6,1,4,1,3902,1015,5200,3,4,11,2,1,6),_ZxAnIsdnBertTxTotalBits_Type())
zxAnIsdnBertTxTotalBits.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnIsdnBertTxTotalBits.setStatus(_A)
_ZxAnIsdnBertRxTotalBits_Type=Counter64
_ZxAnIsdnBertRxTotalBits_Object=MibTableColumn
zxAnIsdnBertRxTotalBits=_ZxAnIsdnBertRxTotalBits_Object((1,3,6,1,4,1,3902,1015,5200,3,4,11,2,1,7),_ZxAnIsdnBertRxTotalBits_Type())
zxAnIsdnBertRxTotalBits.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnIsdnBertRxTotalBits.setStatus(_A)
_ZxAnIsdnBertRxErrorBits_Type=Counter32
_ZxAnIsdnBertRxErrorBits_Object=MibTableColumn
zxAnIsdnBertRxErrorBits=_ZxAnIsdnBertRxErrorBits_Object((1,3,6,1,4,1,3902,1015,5200,3,4,11,2,1,8),_ZxAnIsdnBertRxErrorBits_Type())
zxAnIsdnBertRxErrorBits.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnIsdnBertRxErrorBits.setStatus(_A)
class _ZxAnIsdnBertRxBitErrorRatio_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAnIsdnBertRxBitErrorRatio_Type.__name__=_H
_ZxAnIsdnBertRxBitErrorRatio_Object=MibTableColumn
zxAnIsdnBertRxBitErrorRatio=_ZxAnIsdnBertRxBitErrorRatio_Object((1,3,6,1,4,1,3902,1015,5200,3,4,11,2,1,9),_ZxAnIsdnBertRxBitErrorRatio_Type())
zxAnIsdnBertRxBitErrorRatio.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnIsdnBertRxBitErrorRatio.setStatus(_A)
if mibBuilder.loadTexts:zxAnIsdnBertRxBitErrorRatio.setUnits('percents')
_ZxAnIsdnTrunkTerminationIdTable_Object=MibTable
zxAnIsdnTrunkTerminationIdTable=_ZxAnIsdnTrunkTerminationIdTable_Object((1,3,6,1,4,1,3902,1015,5200,3,4,12))
if mibBuilder.loadTexts:zxAnIsdnTrunkTerminationIdTable.setStatus(_A)
_ZxAnIsdnTrunkTerminationIdEntry_Object=MibTableRow
zxAnIsdnTrunkTerminationIdEntry=_ZxAnIsdnTrunkTerminationIdEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,4,12,1))
zxAnIsdnTrunkTerminationIdEntry.setIndexNames((0,_B,_AB),(0,_B,_AC),(0,_B,_AD),(0,_B,_AE),(0,_B,_AF))
if mibBuilder.loadTexts:zxAnIsdnTrunkTerminationIdEntry.setStatus(_A)
_ZxAnIsdnTrunkTidRack_Type=Integer32
_ZxAnIsdnTrunkTidRack_Object=MibTableColumn
zxAnIsdnTrunkTidRack=_ZxAnIsdnTrunkTidRack_Object((1,3,6,1,4,1,3902,1015,5200,3,4,12,1,1),_ZxAnIsdnTrunkTidRack_Type())
zxAnIsdnTrunkTidRack.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnIsdnTrunkTidRack.setStatus(_A)
_ZxAnIsdnTrunkTidShelf_Type=Integer32
_ZxAnIsdnTrunkTidShelf_Object=MibTableColumn
zxAnIsdnTrunkTidShelf=_ZxAnIsdnTrunkTidShelf_Object((1,3,6,1,4,1,3902,1015,5200,3,4,12,1,2),_ZxAnIsdnTrunkTidShelf_Type())
zxAnIsdnTrunkTidShelf.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnIsdnTrunkTidShelf.setStatus(_A)
_ZxAnIsdnTrunkTidSlot_Type=Integer32
_ZxAnIsdnTrunkTidSlot_Object=MibTableColumn
zxAnIsdnTrunkTidSlot=_ZxAnIsdnTrunkTidSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,4,12,1,3),_ZxAnIsdnTrunkTidSlot_Type())
zxAnIsdnTrunkTidSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnIsdnTrunkTidSlot.setStatus(_A)
class _ZxAnIsdnTrunkTidDsx1LinkNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_ZxAnIsdnTrunkTidDsx1LinkNo_Type.__name__=_C
_ZxAnIsdnTrunkTidDsx1LinkNo_Object=MibTableColumn
zxAnIsdnTrunkTidDsx1LinkNo=_ZxAnIsdnTrunkTidDsx1LinkNo_Object((1,3,6,1,4,1,3902,1015,5200,3,4,12,1,4),_ZxAnIsdnTrunkTidDsx1LinkNo_Type())
zxAnIsdnTrunkTidDsx1LinkNo.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnIsdnTrunkTidDsx1LinkNo.setStatus(_A)
class _ZxAnIsdnTrunkTidDsx1TsNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_ZxAnIsdnTrunkTidDsx1TsNo_Type.__name__=_C
_ZxAnIsdnTrunkTidDsx1TsNo_Object=MibTableColumn
zxAnIsdnTrunkTidDsx1TsNo=_ZxAnIsdnTrunkTidDsx1TsNo_Object((1,3,6,1,4,1,3902,1015,5200,3,4,12,1,5),_ZxAnIsdnTrunkTidDsx1TsNo_Type())
zxAnIsdnTrunkTidDsx1TsNo.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnIsdnTrunkTidDsx1TsNo.setStatus(_A)
class _ZxAnIsdnTrunkTidPrefix_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_ZxAnIsdnTrunkTidPrefix_Type.__name__=_I
_ZxAnIsdnTrunkTidPrefix_Object=MibTableColumn
zxAnIsdnTrunkTidPrefix=_ZxAnIsdnTrunkTidPrefix_Object((1,3,6,1,4,1,3902,1015,5200,3,4,12,1,6),_ZxAnIsdnTrunkTidPrefix_Type())
zxAnIsdnTrunkTidPrefix.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnIsdnTrunkTidPrefix.setStatus(_A)
class _ZxAnIsdnTrunkTidType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('type1',1),('type2',2),('type3',3)))
_ZxAnIsdnTrunkTidType_Type.__name__=_C
_ZxAnIsdnTrunkTidType_Object=MibTableColumn
zxAnIsdnTrunkTidType=_ZxAnIsdnTrunkTidType_Object((1,3,6,1,4,1,3902,1015,5200,3,4,12,1,7),_ZxAnIsdnTrunkTidType_Type())
zxAnIsdnTrunkTidType.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnIsdnTrunkTidType.setStatus(_A)
class _ZxAnIsdnTrunkTidOperNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_ZxAnIsdnTrunkTidOperNum_Type.__name__=_C
_ZxAnIsdnTrunkTidOperNum_Object=MibTableColumn
zxAnIsdnTrunkTidOperNum=_ZxAnIsdnTrunkTidOperNum_Object((1,3,6,1,4,1,3902,1015,5200,3,4,12,1,8),_ZxAnIsdnTrunkTidOperNum_Type())
zxAnIsdnTrunkTidOperNum.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnIsdnTrunkTidOperNum.setStatus(_A)
class _ZxAnIsdnTrunkTidDigitBeginNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnIsdnTrunkTidDigitBeginNo_Type.__name__=_C
_ZxAnIsdnTrunkTidDigitBeginNo_Object=MibTableColumn
zxAnIsdnTrunkTidDigitBeginNo=_ZxAnIsdnTrunkTidDigitBeginNo_Object((1,3,6,1,4,1,3902,1015,5200,3,4,12,1,9),_ZxAnIsdnTrunkTidDigitBeginNo_Type())
zxAnIsdnTrunkTidDigitBeginNo.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnIsdnTrunkTidDigitBeginNo.setStatus(_A)
class _ZxAnIsdnTrunkTidDigitLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,64))
_ZxAnIsdnTrunkTidDigitLength_Type.__name__=_C
_ZxAnIsdnTrunkTidDigitLength_Object=MibTableColumn
zxAnIsdnTrunkTidDigitLength=_ZxAnIsdnTrunkTidDigitLength_Object((1,3,6,1,4,1,3902,1015,5200,3,4,12,1,10),_ZxAnIsdnTrunkTidDigitLength_Type())
zxAnIsdnTrunkTidDigitLength.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnIsdnTrunkTidDigitLength.setStatus(_A)
class _ZxAnIsdnTrunkTidMgId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ZxAnIsdnTrunkTidMgId_Type.__name__=_C
_ZxAnIsdnTrunkTidMgId_Object=MibTableColumn
zxAnIsdnTrunkTidMgId=_ZxAnIsdnTrunkTidMgId_Object((1,3,6,1,4,1,3902,1015,5200,3,4,12,1,11),_ZxAnIsdnTrunkTidMgId_Type())
zxAnIsdnTrunkTidMgId.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnIsdnTrunkTidMgId.setStatus(_A)
class _ZxAnIsdnTrunkTerminationId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ZxAnIsdnTrunkTerminationId_Type.__name__=_I
_ZxAnIsdnTrunkTerminationId_Object=MibTableColumn
zxAnIsdnTrunkTerminationId=_ZxAnIsdnTrunkTerminationId_Object((1,3,6,1,4,1,3902,1015,5200,3,4,12,1,12),_ZxAnIsdnTrunkTerminationId_Type())
zxAnIsdnTrunkTerminationId.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnIsdnTrunkTerminationId.setStatus(_A)
_ZxAnIsdnTrunkTidRowStatus_Type=RowStatus
_ZxAnIsdnTrunkTidRowStatus_Object=MibTableColumn
zxAnIsdnTrunkTidRowStatus=_ZxAnIsdnTrunkTidRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,4,12,1,50),_ZxAnIsdnTrunkTidRowStatus_Type())
zxAnIsdnTrunkTidRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnIsdnTrunkTidRowStatus.setStatus(_A)
_ZxAnIsdnTrunkTable_Object=MibTable
zxAnIsdnTrunkTable=_ZxAnIsdnTrunkTable_Object((1,3,6,1,4,1,3902,1015,5200,3,4,13))
if mibBuilder.loadTexts:zxAnIsdnTrunkTable.setStatus(_A)
_ZxAnIsdnTrunkEntry_Object=MibTableRow
zxAnIsdnTrunkEntry=_ZxAnIsdnTrunkEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,4,13,1))
zxAnIsdnTrunkEntry.setIndexNames((0,_B,_AG),(0,_B,_AH),(0,_B,_AI),(0,_B,_AJ),(0,_B,_AK))
if mibBuilder.loadTexts:zxAnIsdnTrunkEntry.setStatus(_A)
_ZxAnIsdnTrunkRack_Type=Integer32
_ZxAnIsdnTrunkRack_Object=MibTableColumn
zxAnIsdnTrunkRack=_ZxAnIsdnTrunkRack_Object((1,3,6,1,4,1,3902,1015,5200,3,4,13,1,1),_ZxAnIsdnTrunkRack_Type())
zxAnIsdnTrunkRack.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnIsdnTrunkRack.setStatus(_A)
_ZxAnIsdnTrunkShelf_Type=Integer32
_ZxAnIsdnTrunkShelf_Object=MibTableColumn
zxAnIsdnTrunkShelf=_ZxAnIsdnTrunkShelf_Object((1,3,6,1,4,1,3902,1015,5200,3,4,13,1,2),_ZxAnIsdnTrunkShelf_Type())
zxAnIsdnTrunkShelf.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnIsdnTrunkShelf.setStatus(_A)
_ZxAnIsdnTrunkSlot_Type=Integer32
_ZxAnIsdnTrunkSlot_Object=MibTableColumn
zxAnIsdnTrunkSlot=_ZxAnIsdnTrunkSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,4,13,1,3),_ZxAnIsdnTrunkSlot_Type())
zxAnIsdnTrunkSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnIsdnTrunkSlot.setStatus(_A)
_ZxAnIsdnTrunkDsx1LinkNo_Type=Integer32
_ZxAnIsdnTrunkDsx1LinkNo_Object=MibTableColumn
zxAnIsdnTrunkDsx1LinkNo=_ZxAnIsdnTrunkDsx1LinkNo_Object((1,3,6,1,4,1,3902,1015,5200,3,4,13,1,4),_ZxAnIsdnTrunkDsx1LinkNo_Type())
zxAnIsdnTrunkDsx1LinkNo.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnIsdnTrunkDsx1LinkNo.setStatus(_A)
_ZxAnIsdnTrunkDsx1TsNo_Type=Integer32
_ZxAnIsdnTrunkDsx1TsNo_Object=MibTableColumn
zxAnIsdnTrunkDsx1TsNo=_ZxAnIsdnTrunkDsx1TsNo_Object((1,3,6,1,4,1,3902,1015,5200,3,4,13,1,5),_ZxAnIsdnTrunkDsx1TsNo_Type())
zxAnIsdnTrunkDsx1TsNo.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnIsdnTrunkDsx1TsNo.setStatus(_A)
class _ZxAnIsdnTrunkStatus_Type(Bits):namedValues=NamedValues(*(('idle',0),('commOff',1),('powerOff',2),('fault',3),('manualBlock',4),('seizure',5),('spc',6)))
_ZxAnIsdnTrunkStatus_Type.__name__='Bits'
_ZxAnIsdnTrunkStatus_Object=MibTableColumn
zxAnIsdnTrunkStatus=_ZxAnIsdnTrunkStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,4,13,1,6),_ZxAnIsdnTrunkStatus_Type())
zxAnIsdnTrunkStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnIsdnTrunkStatus.setStatus(_A)
_ZxAnIsdnCallStatsTable_Object=MibTable
zxAnIsdnCallStatsTable=_ZxAnIsdnCallStatsTable_Object((1,3,6,1,4,1,3902,1015,5200,3,4,14))
if mibBuilder.loadTexts:zxAnIsdnCallStatsTable.setStatus(_A)
_ZxAnIsdnCallStatsEntry_Object=MibTableRow
zxAnIsdnCallStatsEntry=_ZxAnIsdnCallStatsEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,4,14,1))
zxAnIsdnCallStatsEntry.setIndexNames((0,_B,_AL),(0,_B,_AM),(0,_B,_AN),(0,_B,_AO))
if mibBuilder.loadTexts:zxAnIsdnCallStatsEntry.setStatus(_A)
_ZxAnIsdnCallStatsRack_Type=Integer32
_ZxAnIsdnCallStatsRack_Object=MibTableColumn
zxAnIsdnCallStatsRack=_ZxAnIsdnCallStatsRack_Object((1,3,6,1,4,1,3902,1015,5200,3,4,14,1,1),_ZxAnIsdnCallStatsRack_Type())
zxAnIsdnCallStatsRack.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnIsdnCallStatsRack.setStatus(_A)
_ZxAnIsdnCallStatsShelf_Type=Integer32
_ZxAnIsdnCallStatsShelf_Object=MibTableColumn
zxAnIsdnCallStatsShelf=_ZxAnIsdnCallStatsShelf_Object((1,3,6,1,4,1,3902,1015,5200,3,4,14,1,2),_ZxAnIsdnCallStatsShelf_Type())
zxAnIsdnCallStatsShelf.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnIsdnCallStatsShelf.setStatus(_A)
_ZxAnIsdnCallStatsSlot_Type=Integer32
_ZxAnIsdnCallStatsSlot_Object=MibTableColumn
zxAnIsdnCallStatsSlot=_ZxAnIsdnCallStatsSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,4,14,1,3),_ZxAnIsdnCallStatsSlot_Type())
zxAnIsdnCallStatsSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnIsdnCallStatsSlot.setStatus(_A)
_ZxAnIsdnCallStatsPort_Type=Integer32
_ZxAnIsdnCallStatsPort_Object=MibTableColumn
zxAnIsdnCallStatsPort=_ZxAnIsdnCallStatsPort_Object((1,3,6,1,4,1,3902,1015,5200,3,4,14,1,4),_ZxAnIsdnCallStatsPort_Type())
zxAnIsdnCallStatsPort.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnIsdnCallStatsPort.setStatus(_A)
_ZxAnIsdnSuccessIncomingCalls_Type=Counter32
_ZxAnIsdnSuccessIncomingCalls_Object=MibTableColumn
zxAnIsdnSuccessIncomingCalls=_ZxAnIsdnSuccessIncomingCalls_Object((1,3,6,1,4,1,3902,1015,5200,3,4,14,1,5),_ZxAnIsdnSuccessIncomingCalls_Type())
zxAnIsdnSuccessIncomingCalls.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnIsdnSuccessIncomingCalls.setStatus(_A)
_ZxAnIsdnFailedIncomingCalls_Type=Counter32
_ZxAnIsdnFailedIncomingCalls_Object=MibTableColumn
zxAnIsdnFailedIncomingCalls=_ZxAnIsdnFailedIncomingCalls_Object((1,3,6,1,4,1,3902,1015,5200,3,4,14,1,6),_ZxAnIsdnFailedIncomingCalls_Type())
zxAnIsdnFailedIncomingCalls.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnIsdnFailedIncomingCalls.setStatus(_A)
_ZxAnIsdnSuccessOutgoingCalls_Type=Counter32
_ZxAnIsdnSuccessOutgoingCalls_Object=MibTableColumn
zxAnIsdnSuccessOutgoingCalls=_ZxAnIsdnSuccessOutgoingCalls_Object((1,3,6,1,4,1,3902,1015,5200,3,4,14,1,7),_ZxAnIsdnSuccessOutgoingCalls_Type())
zxAnIsdnSuccessOutgoingCalls.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnIsdnSuccessOutgoingCalls.setStatus(_A)
_ZxAnIsdnFailedOutgoingCalls_Type=Counter32
_ZxAnIsdnFailedOutgoingCalls_Object=MibTableColumn
zxAnIsdnFailedOutgoingCalls=_ZxAnIsdnFailedOutgoingCalls_Object((1,3,6,1,4,1,3902,1015,5200,3,4,14,1,8),_ZxAnIsdnFailedOutgoingCalls_Type())
zxAnIsdnFailedOutgoingCalls.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnIsdnFailedOutgoingCalls.setStatus(_A)
_ZxAnIsdnActiveIncomingCalls_Type=Counter32
_ZxAnIsdnActiveIncomingCalls_Object=MibTableColumn
zxAnIsdnActiveIncomingCalls=_ZxAnIsdnActiveIncomingCalls_Object((1,3,6,1,4,1,3902,1015,5200,3,4,14,1,9),_ZxAnIsdnActiveIncomingCalls_Type())
zxAnIsdnActiveIncomingCalls.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnIsdnActiveIncomingCalls.setStatus(_A)
_ZxAnIsdnActiveOutgoingCalls_Type=Counter32
_ZxAnIsdnActiveOutgoingCalls_Object=MibTableColumn
zxAnIsdnActiveOutgoingCalls=_ZxAnIsdnActiveOutgoingCalls_Object((1,3,6,1,4,1,3902,1015,5200,3,4,14,1,10),_ZxAnIsdnActiveOutgoingCalls_Type())
zxAnIsdnActiveOutgoingCalls.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnIsdnActiveOutgoingCalls.setStatus(_A)
_ZxAnIsdnRemotePowerSupplyTable_Object=MibTable
zxAnIsdnRemotePowerSupplyTable=_ZxAnIsdnRemotePowerSupplyTable_Object((1,3,6,1,4,1,3902,1015,5200,3,4,15))
if mibBuilder.loadTexts:zxAnIsdnRemotePowerSupplyTable.setStatus(_A)
_ZxAnIsdnRemotePowerSupplyEntry_Object=MibTableRow
zxAnIsdnRemotePowerSupplyEntry=_ZxAnIsdnRemotePowerSupplyEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,4,15,1))
zxAnIsdnRemotePowerSupplyEntry.setIndexNames((0,_B,_AP),(0,_B,_AQ),(0,_B,_AR))
if mibBuilder.loadTexts:zxAnIsdnRemotePowerSupplyEntry.setStatus(_A)
_ZxAnIsdnRemotePowerSupplyRack_Type=Integer32
_ZxAnIsdnRemotePowerSupplyRack_Object=MibTableColumn
zxAnIsdnRemotePowerSupplyRack=_ZxAnIsdnRemotePowerSupplyRack_Object((1,3,6,1,4,1,3902,1015,5200,3,4,15,1,1),_ZxAnIsdnRemotePowerSupplyRack_Type())
zxAnIsdnRemotePowerSupplyRack.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnIsdnRemotePowerSupplyRack.setStatus(_A)
_ZxAnIsdnRemotePowerSupplyShelf_Type=Integer32
_ZxAnIsdnRemotePowerSupplyShelf_Object=MibTableColumn
zxAnIsdnRemotePowerSupplyShelf=_ZxAnIsdnRemotePowerSupplyShelf_Object((1,3,6,1,4,1,3902,1015,5200,3,4,15,1,2),_ZxAnIsdnRemotePowerSupplyShelf_Type())
zxAnIsdnRemotePowerSupplyShelf.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnIsdnRemotePowerSupplyShelf.setStatus(_A)
_ZxAnIsdnRemotePowerSupplySlot_Type=Integer32
_ZxAnIsdnRemotePowerSupplySlot_Object=MibTableColumn
zxAnIsdnRemotePowerSupplySlot=_ZxAnIsdnRemotePowerSupplySlot_Object((1,3,6,1,4,1,3902,1015,5200,3,4,15,1,3),_ZxAnIsdnRemotePowerSupplySlot_Type())
zxAnIsdnRemotePowerSupplySlot.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnIsdnRemotePowerSupplySlot.setStatus(_A)
class _ZxAnIsdnRemotePowerSupplyEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_ZxAnIsdnRemotePowerSupplyEnable_Type.__name__=_C
_ZxAnIsdnRemotePowerSupplyEnable_Object=MibTableColumn
zxAnIsdnRemotePowerSupplyEnable=_ZxAnIsdnRemotePowerSupplyEnable_Object((1,3,6,1,4,1,3902,1015,5200,3,4,15,1,4),_ZxAnIsdnRemotePowerSupplyEnable_Type())
zxAnIsdnRemotePowerSupplyEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnIsdnRemotePowerSupplyEnable.setStatus(_A)
_ZxAnIsdnTrapObjects_ObjectIdentity=ObjectIdentity
zxAnIsdnTrapObjects=_ZxAnIsdnTrapObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,4,100))
zxAnIsdnSInterfaceUnsyncAlm=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,4,100,1))
zxAnIsdnSInterfaceUnsyncAlm.setObjects((_B,_L))
if mibBuilder.loadTexts:zxAnIsdnSInterfaceUnsyncAlm.setStatus(_A)
zxAnIsdnSInterfaceUnsyncClr=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,4,100,2))
zxAnIsdnSInterfaceUnsyncClr.setObjects((_B,_L))
if mibBuilder.loadTexts:zxAnIsdnSInterfaceUnsyncClr.setStatus(_A)
zxAnIsdnUInterfaceAbnormal=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,4,100,3))
zxAnIsdnUInterfaceAbnormal.setObjects((_B,_AS))
if mibBuilder.loadTexts:zxAnIsdnUInterfaceAbnormal.setStatus(_A)
zxAnIsdnSInterfaceAbnormal=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,4,100,4))
zxAnIsdnSInterfaceAbnormal.setObjects((_B,_AT))
if mibBuilder.loadTexts:zxAnIsdnSInterfaceAbnormal.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'zte':zte,'zxAn':zxAn,'zxAnISDNMib':zxAnISDNMib,'msagmajorVersion':msagmajorVersion,'msagISDNService':msagISDNService,'isdnAppServerTable':isdnAppServerTable,'isdnAppServerEntry':isdnAppServerEntry,_N:isdnAppServerID,'isdnAppServerProtocol':isdnAppServerProtocol,'isdnAppServerMode':isdnAppServerMode,'isdnAppServerModeEval':isdnAppServerModeEval,'isdnAppServerStatus':isdnAppServerStatus,'isdnAppServerRowStatus':isdnAppServerRowStatus,'isdnAppServerProcTable':isdnAppServerProcTable,'isdnAppServerProcEntry':isdnAppServerProcEntry,_Q:isdnASPID,'isdnASPDestPort':isdnASPDestPort,'isdnASPLoclPort':isdnASPLoclPort,'isdnASPSctpID':isdnASPSctpID,'isdnASPUpProto':isdnASPUpProto,'isdnASPDownProto':isdnASPDownProto,'isdnASPDestIP':isdnASPDestIP,'isdnASPInStream':isdnASPInStream,'isdnASPOutStream':isdnASPOutStream,'isdnASPStat':isdnASPStat,'isdnASPModule':isdnASPModule,'isdnASPClieOrServ':isdnASPClieOrServ,'isdnASPRowStatus':isdnASPRowStatus,'isdnASASPRelationTable':isdnASASPRelationTable,'isdnASASPRelationEntry':isdnASASPRelationEntry,_T:isdnAARASPID,_U:isdnAARASID,'isdnAARQueue':isdnAARQueue,'isdnAARRowStatus':isdnAARRowStatus,'isdnDLinkTable':isdnDLinkTable,'isdnDLinkEntry':isdnDLinkEntry,_V:isdnDLinkRack,_W:isdnDLinkShelf,_X:isdnDLinkSlot,_Y:isdnDLinkPCMNo,_Z:isdnDLinkLinkIdx,'isdnDLinkIfID':isdnDLinkIfID,'isdnDLinkLinkID':isdnDLinkLinkID,'isdnDLinkLinkInfo':isdnDLinkLinkInfo,'isdnDLinkASID':isdnDLinkASID,'isdnDLinkNumber':isdnDLinkNumber,'isdnDLinkProtocol':isdnDLinkProtocol,'isdnDLinkStatus':isdnDLinkStatus,'isdnDLinkRowStatus':isdnDLinkRowStatus,'loopbackTable':loopbackTable,'loopbackEntry':loopbackEntry,_a:loopbackrack,_b:loopbackshelf,_c:loopbackslot,_d:loopbackportno,'loopbacklooptype':loopbacklooptype,'msagIsdnCapabilityTable':msagIsdnCapabilityTable,'msagIsdnCapabilityEntry':msagIsdnCapabilityEntry,_e:isdnkrack,_f:isdnshelf,_g:isdnslot,_h:isdnportno,'isdnLossOfSignal':isdnLossOfSignal,'isdnLossOfPower':isdnLossOfPower,'isdnLossOfFrame':isdnLossOfFrame,'isdnClear':isdnClear,'zxAnIsdnPortActiveStatusTable':zxAnIsdnPortActiveStatusTable,'zxAnIsdnPortActiveStatusEntry':zxAnIsdnPortActiveStatusEntry,_i:zxAnIsdnPortRack,_j:zxAnIsdnPortShelf,_k:zxAnIsdnPortSlot,_l:zxAnIsdnPortNo,'zxAnIsdnPortL1ActiveStatus':zxAnIsdnPortL1ActiveStatus,'zxAnIsdnPortL2ActiveStatus':zxAnIsdnPortL2ActiveStatus,'zxAnIsdnUIfCfgTable':zxAnIsdnUIfCfgTable,'zxAnIsdnUIfCfgEntry':zxAnIsdnUIfCfgEntry,_o:zxAnIsdnUIfRack,_p:zxAnIsdnUIfShelf,_q:zxAnIsdnUIfSlot,_r:zxAnIsdnUIfNo,'zxAnIsdnUIfRemotePowerFeedEnable':zxAnIsdnUIfRemotePowerFeedEnable,'zxAnIsdnUIfTrapEnable':zxAnIsdnUIfTrapEnable,'zxAnIsdnUIfActiveStatus':zxAnIsdnUIfActiveStatus,'zxAnIsdnUIfSoftReset':zxAnIsdnUIfSoftReset,_AS:zxAnIsdnUIfAbnormalReason,'zxAnIsdnSIfCfgTable':zxAnIsdnSIfCfgTable,'zxAnIsdnSIfCfgEntry':zxAnIsdnSIfCfgEntry,_z:zxAnIsdnSIfRack,_A0:zxAnIsdnSIfShelf,_A1:zxAnIsdnSIfSlot,_A2:zxAnIsdnSIfNo,'zxAnIsdnSIfTrapEnable':zxAnIsdnSIfTrapEnable,_L:zxAnIsdnSIfSyncStatus,_AT:zxAnIsdnSIfAbnormalReason,'zxAnIsdnBertMgmtGroup':zxAnIsdnBertMgmtGroup,'zxAnIsdnBertConfTable':zxAnIsdnBertConfTable,'zxAnIsdnBertConfEntry':zxAnIsdnBertConfEntry,_A3:zxAnIsdnBertConfRack,_A4:zxAnIsdnBertConfShelf,_A5:zxAnIsdnBertConfSlot,_A6:zxAnIsdnBertConfCircuit,'zxAnIsdnBertAction':zxAnIsdnBertAction,'zxAnIsdnBertLoopbackPosition':zxAnIsdnBertLoopbackPosition,'zxAnIsdnBertThresholdLevel':zxAnIsdnBertThresholdLevel,'zxAnIsdnBertMeasurePrecision':zxAnIsdnBertMeasurePrecision,'zxAnIsdnBertForceTest':zxAnIsdnBertForceTest,'zxAnIsdnBertStartDateAndTime':zxAnIsdnBertStartDateAndTime,'zxAnIsdnBertOperStatus':zxAnIsdnBertOperStatus,'zxAnIsdnBertResult':zxAnIsdnBertResult,'zxAnIsdnBertRowStatus':zxAnIsdnBertRowStatus,'zxAnIsdnBertStatsTable':zxAnIsdnBertStatsTable,'zxAnIsdnBertStatsEntry':zxAnIsdnBertStatsEntry,_A7:zxAnIsdnBertStatsRack,_A8:zxAnIsdnBertStatsShelf,_A9:zxAnIsdnBertStatsSlot,_AA:zxAnIsdnBertStatsCircuit,'zxAnIsdnBertTimeElapsed':zxAnIsdnBertTimeElapsed,'zxAnIsdnBertTxTotalBits':zxAnIsdnBertTxTotalBits,'zxAnIsdnBertRxTotalBits':zxAnIsdnBertRxTotalBits,'zxAnIsdnBertRxErrorBits':zxAnIsdnBertRxErrorBits,'zxAnIsdnBertRxBitErrorRatio':zxAnIsdnBertRxBitErrorRatio,'zxAnIsdnTrunkTerminationIdTable':zxAnIsdnTrunkTerminationIdTable,'zxAnIsdnTrunkTerminationIdEntry':zxAnIsdnTrunkTerminationIdEntry,_AB:zxAnIsdnTrunkTidRack,_AC:zxAnIsdnTrunkTidShelf,_AD:zxAnIsdnTrunkTidSlot,_AE:zxAnIsdnTrunkTidDsx1LinkNo,_AF:zxAnIsdnTrunkTidDsx1TsNo,'zxAnIsdnTrunkTidPrefix':zxAnIsdnTrunkTidPrefix,'zxAnIsdnTrunkTidType':zxAnIsdnTrunkTidType,'zxAnIsdnTrunkTidOperNum':zxAnIsdnTrunkTidOperNum,'zxAnIsdnTrunkTidDigitBeginNo':zxAnIsdnTrunkTidDigitBeginNo,'zxAnIsdnTrunkTidDigitLength':zxAnIsdnTrunkTidDigitLength,'zxAnIsdnTrunkTidMgId':zxAnIsdnTrunkTidMgId,'zxAnIsdnTrunkTerminationId':zxAnIsdnTrunkTerminationId,'zxAnIsdnTrunkTidRowStatus':zxAnIsdnTrunkTidRowStatus,'zxAnIsdnTrunkTable':zxAnIsdnTrunkTable,'zxAnIsdnTrunkEntry':zxAnIsdnTrunkEntry,_AG:zxAnIsdnTrunkRack,_AH:zxAnIsdnTrunkShelf,_AI:zxAnIsdnTrunkSlot,_AJ:zxAnIsdnTrunkDsx1LinkNo,_AK:zxAnIsdnTrunkDsx1TsNo,'zxAnIsdnTrunkStatus':zxAnIsdnTrunkStatus,'zxAnIsdnCallStatsTable':zxAnIsdnCallStatsTable,'zxAnIsdnCallStatsEntry':zxAnIsdnCallStatsEntry,_AL:zxAnIsdnCallStatsRack,_AM:zxAnIsdnCallStatsShelf,_AN:zxAnIsdnCallStatsSlot,_AO:zxAnIsdnCallStatsPort,'zxAnIsdnSuccessIncomingCalls':zxAnIsdnSuccessIncomingCalls,'zxAnIsdnFailedIncomingCalls':zxAnIsdnFailedIncomingCalls,'zxAnIsdnSuccessOutgoingCalls':zxAnIsdnSuccessOutgoingCalls,'zxAnIsdnFailedOutgoingCalls':zxAnIsdnFailedOutgoingCalls,'zxAnIsdnActiveIncomingCalls':zxAnIsdnActiveIncomingCalls,'zxAnIsdnActiveOutgoingCalls':zxAnIsdnActiveOutgoingCalls,'zxAnIsdnRemotePowerSupplyTable':zxAnIsdnRemotePowerSupplyTable,'zxAnIsdnRemotePowerSupplyEntry':zxAnIsdnRemotePowerSupplyEntry,_AP:zxAnIsdnRemotePowerSupplyRack,_AQ:zxAnIsdnRemotePowerSupplyShelf,_AR:zxAnIsdnRemotePowerSupplySlot,'zxAnIsdnRemotePowerSupplyEnable':zxAnIsdnRemotePowerSupplyEnable,'zxAnIsdnTrapObjects':zxAnIsdnTrapObjects,'zxAnIsdnSInterfaceUnsyncAlm':zxAnIsdnSInterfaceUnsyncAlm,'zxAnIsdnSInterfaceUnsyncClr':zxAnIsdnSInterfaceUnsyncClr,'zxAnIsdnUInterfaceAbnormal':zxAnIsdnUInterfaceAbnormal,'zxAnIsdnSInterfaceAbnormal':zxAnIsdnSInterfaceAbnormal})