_B8='sdlcPrimaryMultipointGroup'
_B7='sdlcPrimaryGroup'
_B6='sdlcCoreLSStatsGroup'
_B5='sdlcCoreLSOperGroup'
_B4='sdlcCoreLSAdminGroup'
_B3='sdlcCorePortStatsGroup'
_B2='sdlcCorePortOperGroup'
_B1='sdlcCorePortAdminGroup'
_B0='sdlcPortOperSlowPollTimer'
_A_='sdlcPortOperSERVLIM'
_Az='sdlcPortOperSlowPollMethod'
_Ay='sdlcPortAdminSlowPollTimer'
_Ax='sdlcPortAdminSERVLIM'
_Aw='sdlcLSOperREPLYTO'
_Av='sdlcLSAdminREPLYTO'
_Au='sdlcPortOperPAUSE'
_At='sdlcPortAdminPAUSE'
_As='sdlcLSStatsRetriesExps'
_Ar='sdlcLSStatsRNRLIMITs'
_Aq='sdlcLSStatsProtocolErrs'
_Ap='sdlcLSStatsRIMsOut'
_Ao='sdlcLSStatsRIMsIn'
_An='sdlcLSStatsSIMsOut'
_Am='sdlcLSStatsSIMsIn'
_Al='sdlcLSStatsFRMRsOut'
_Ak='sdlcLSStatsFRMRsIn'
_Aj='sdlcLSStatsREJsOut'
_Ai='sdlcLSStatsREJsIn'
_Ah='sdlcLSStatsTESTsOut'
_Ag='sdlcLSStatsTESTsIn'
_Af='sdlcLSStatsXIDsOut'
_Ae='sdlcLSStatsXIDsIn'
_Ad='sdlcLSStatsUIFramesOut'
_Ac='sdlcLSStatsUIFramesIn'
_Ab='sdlcLSStatsRetransmitsOut'
_Aa='sdlcLSStatsRetransmitsIn'
_AZ='sdlcLSStatsIFramesOut'
_AY='sdlcLSStatsIFramesIn'
_AX='sdlcLSStatsRemoteBusies'
_AW='sdlcLSStatsLocalBusies'
_AV='sdlcLSStatsPollRspsOut'
_AU='sdlcLSStatsPollRspsIn'
_AT='sdlcLSStatsPollsOut'
_AS='sdlcLSStatsPollsIn'
_AR='sdlcLSStatsOctetsOut'
_AQ='sdlcLSStatsOctetsIn'
_AP='sdlcLSStatsBLUsOut'
_AO='sdlcLSStatsBLUsIn'
_AN='sdlcLSOperGPoll'
_AM='sdlcLSOperEcho'
_AL='sdlcLSOperDATMODE'
_AK='sdlcLSOperRNRLIMIT'
_AJ='sdlcLSOperRETRIESn'
_AI='sdlcLSOperRETRIESt'
_AH='sdlcLSOperRETRIESm'
_AG='sdlcLSOperMODULO'
_AF='sdlcLSOperMAXOUT'
_AE='sdlcLSOperMAXIN'
_AD='sdlcLSOperMAXDATASend'
_AC='sdlcLSOperRole'
_AB='sdlcLSAdminRowStatus'
_AA='sdlcLSAdminSimRim'
_A9='sdlcLSAdminGPoll'
_A8='sdlcLSAdminDATMODE'
_A7='sdlcLSAdminRNRLIMIT'
_A6='sdlcLSAdminRETRIESn'
_A5='sdlcLSAdminRETRIESt'
_A4='sdlcLSAdminRETRIESm'
_A3='sdlcLSAdminMODULO'
_A2='sdlcLSAdminMAXOUT'
_A1='sdlcLSAdminMAXIN'
_A0='sdlcLSAdminMAXDATARcv'
_z='sdlcLSAdminMAXDATASend'
_y='sdlcLSAdminISTATUS'
_x='sdlcLSAdminName'
_w='sdlcPortStatsDwarfFrames'
_v='sdlcPortStatsInvalidAddresses'
_u='sdlcPortStatsPhysicalFailures'
_t='sdlcPortOperACTIVTO'
_s='sdlcPortOperISTATUS'
_r='sdlcPortOperTopology'
_q='sdlcPortOperType'
_p='sdlcPortOperRole'
_o='sdlcPortOperName'
_n='sdlcPortAdminISTATUS'
_m='sdlcPortAdminTopology'
_l='sdlcPortAdminType'
_k='sdlcPortAdminRole'
_j='sdlcPortAdminName'
_i='onetwentyeight'
_h='multipoint'
_g='pointToPoint'
_f='switched'
_e='leased'
_d='ifOperStatus'
_c='ifAdminStatus'
_b='sdlcLSOperLastFailREPLYTOs'
_a='sdlcLSOperLastFailFRMRInfo'
_Z='sdlcLSOperLastFailCtrlOut'
_Y='sdlcLSOperLastFailCtrlIn'
_X='sdlcLSOperLastFailCause'
_W='sdlcLSOperLastFailTime'
_V='sdlcLSOperState'
_U='sdlcLSAdminState'
_T='sdlcPortOperLastFailCause'
_S='sdlcPortOperLastFailTime'
_R='yes'
_Q='secondary'
_P='primary'
_O='undefined'
_N='active'
_M='inactive'
_L='OctetString'
_K='DisplayString'
_J='sdlcLSAddress'
_I='TimeInterval'
_H='read-write'
_G='ifIndex'
_F='IF-MIB'
_E='read-create'
_D='Integer32'
_C='read-only'
_B='SNA-SDLC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifAdminStatus,ifIndex,ifOperStatus=mibBuilder.importSymbols(_F,_c,_G,_d)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeInterval=mibBuilder.importSymbols('SNMPv2-TC',_K,'PhysAddress','RowStatus','TextualConvention',_I)
snaDLC=ModuleIdentity((1,3,6,1,2,1,41))
_Sdlc_ObjectIdentity=ObjectIdentity
sdlc=_Sdlc_ObjectIdentity((1,3,6,1,2,1,41,1))
_SdlcPortGroup_ObjectIdentity=ObjectIdentity
sdlcPortGroup=_SdlcPortGroup_ObjectIdentity((1,3,6,1,2,1,41,1,1))
_SdlcPortAdminTable_Object=MibTable
sdlcPortAdminTable=_SdlcPortAdminTable_Object((1,3,6,1,2,1,41,1,1,1))
if mibBuilder.loadTexts:sdlcPortAdminTable.setStatus(_A)
_SdlcPortAdminEntry_Object=MibTableRow
sdlcPortAdminEntry=_SdlcPortAdminEntry_Object((1,3,6,1,2,1,41,1,1,1,1))
sdlcPortAdminEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:sdlcPortAdminEntry.setStatus(_A)
class _SdlcPortAdminName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_SdlcPortAdminName_Type.__name__=_K
_SdlcPortAdminName_Object=MibTableColumn
sdlcPortAdminName=_SdlcPortAdminName_Object((1,3,6,1,2,1,41,1,1,1,1,1),_SdlcPortAdminName_Type())
sdlcPortAdminName.setMaxAccess(_H)
if mibBuilder.loadTexts:sdlcPortAdminName.setStatus(_A)
class _SdlcPortAdminRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),(_Q,2),('negotiable',3)))
_SdlcPortAdminRole_Type.__name__=_D
_SdlcPortAdminRole_Object=MibTableColumn
sdlcPortAdminRole=_SdlcPortAdminRole_Object((1,3,6,1,2,1,41,1,1,1,1,2),_SdlcPortAdminRole_Type())
sdlcPortAdminRole.setMaxAccess(_H)
if mibBuilder.loadTexts:sdlcPortAdminRole.setStatus(_A)
class _SdlcPortAdminType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_e,1),(_f,2)))
_SdlcPortAdminType_Type.__name__=_D
_SdlcPortAdminType_Object=MibTableColumn
sdlcPortAdminType=_SdlcPortAdminType_Object((1,3,6,1,2,1,41,1,1,1,1,3),_SdlcPortAdminType_Type())
sdlcPortAdminType.setMaxAccess(_H)
if mibBuilder.loadTexts:sdlcPortAdminType.setStatus(_A)
class _SdlcPortAdminTopology_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_g,1),(_h,2)))
_SdlcPortAdminTopology_Type.__name__=_D
_SdlcPortAdminTopology_Object=MibTableColumn
sdlcPortAdminTopology=_SdlcPortAdminTopology_Object((1,3,6,1,2,1,41,1,1,1,1,4),_SdlcPortAdminTopology_Type())
sdlcPortAdminTopology.setMaxAccess(_H)
if mibBuilder.loadTexts:sdlcPortAdminTopology.setStatus(_A)
class _SdlcPortAdminISTATUS_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_SdlcPortAdminISTATUS_Type.__name__=_D
_SdlcPortAdminISTATUS_Object=MibTableColumn
sdlcPortAdminISTATUS=_SdlcPortAdminISTATUS_Object((1,3,6,1,2,1,41,1,1,1,1,5),_SdlcPortAdminISTATUS_Type())
sdlcPortAdminISTATUS.setMaxAccess(_H)
if mibBuilder.loadTexts:sdlcPortAdminISTATUS.setStatus(_A)
class _SdlcPortAdminACTIVTO_Type(TimeInterval):defaultValue=0
_SdlcPortAdminACTIVTO_Type.__name__=_I
_SdlcPortAdminACTIVTO_Object=MibTableColumn
sdlcPortAdminACTIVTO=_SdlcPortAdminACTIVTO_Object((1,3,6,1,2,1,41,1,1,1,1,6),_SdlcPortAdminACTIVTO_Type())
sdlcPortAdminACTIVTO.setMaxAccess(_H)
if mibBuilder.loadTexts:sdlcPortAdminACTIVTO.setStatus(_A)
class _SdlcPortAdminPAUSE_Type(TimeInterval):defaultValue=200
_SdlcPortAdminPAUSE_Type.__name__=_I
_SdlcPortAdminPAUSE_Object=MibTableColumn
sdlcPortAdminPAUSE=_SdlcPortAdminPAUSE_Object((1,3,6,1,2,1,41,1,1,1,1,7),_SdlcPortAdminPAUSE_Type())
sdlcPortAdminPAUSE.setMaxAccess(_H)
if mibBuilder.loadTexts:sdlcPortAdminPAUSE.setStatus(_A)
class _SdlcPortAdminSERVLIM_Type(Integer32):defaultValue=20
_SdlcPortAdminSERVLIM_Type.__name__=_D
_SdlcPortAdminSERVLIM_Object=MibTableColumn
sdlcPortAdminSERVLIM=_SdlcPortAdminSERVLIM_Object((1,3,6,1,2,1,41,1,1,1,1,8),_SdlcPortAdminSERVLIM_Type())
sdlcPortAdminSERVLIM.setMaxAccess(_H)
if mibBuilder.loadTexts:sdlcPortAdminSERVLIM.setStatus(_A)
class _SdlcPortAdminSlowPollTimer_Type(TimeInterval):defaultValue=2000
_SdlcPortAdminSlowPollTimer_Type.__name__=_I
_SdlcPortAdminSlowPollTimer_Object=MibTableColumn
sdlcPortAdminSlowPollTimer=_SdlcPortAdminSlowPollTimer_Object((1,3,6,1,2,1,41,1,1,1,1,9),_SdlcPortAdminSlowPollTimer_Type())
sdlcPortAdminSlowPollTimer.setMaxAccess(_H)
if mibBuilder.loadTexts:sdlcPortAdminSlowPollTimer.setStatus(_A)
_SdlcPortOperTable_Object=MibTable
sdlcPortOperTable=_SdlcPortOperTable_Object((1,3,6,1,2,1,41,1,1,2))
if mibBuilder.loadTexts:sdlcPortOperTable.setStatus(_A)
_SdlcPortOperEntry_Object=MibTableRow
sdlcPortOperEntry=_SdlcPortOperEntry_Object((1,3,6,1,2,1,41,1,1,2,1))
sdlcPortOperEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:sdlcPortOperEntry.setStatus(_A)
class _SdlcPortOperName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_SdlcPortOperName_Type.__name__=_K
_SdlcPortOperName_Object=MibTableColumn
sdlcPortOperName=_SdlcPortOperName_Object((1,3,6,1,2,1,41,1,1,2,1,1),_SdlcPortOperName_Type())
sdlcPortOperName.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcPortOperName.setStatus(_A)
class _SdlcPortOperRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),(_Q,2),(_O,3)))
_SdlcPortOperRole_Type.__name__=_D
_SdlcPortOperRole_Object=MibTableColumn
sdlcPortOperRole=_SdlcPortOperRole_Object((1,3,6,1,2,1,41,1,1,2,1,2),_SdlcPortOperRole_Type())
sdlcPortOperRole.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcPortOperRole.setStatus(_A)
class _SdlcPortOperType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_e,1),(_f,2)))
_SdlcPortOperType_Type.__name__=_D
_SdlcPortOperType_Object=MibTableColumn
sdlcPortOperType=_SdlcPortOperType_Object((1,3,6,1,2,1,41,1,1,2,1,3),_SdlcPortOperType_Type())
sdlcPortOperType.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcPortOperType.setStatus(_A)
class _SdlcPortOperTopology_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_g,1),(_h,2)))
_SdlcPortOperTopology_Type.__name__=_D
_SdlcPortOperTopology_Object=MibTableColumn
sdlcPortOperTopology=_SdlcPortOperTopology_Object((1,3,6,1,2,1,41,1,1,2,1,4),_SdlcPortOperTopology_Type())
sdlcPortOperTopology.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcPortOperTopology.setStatus(_A)
class _SdlcPortOperISTATUS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_SdlcPortOperISTATUS_Type.__name__=_D
_SdlcPortOperISTATUS_Object=MibTableColumn
sdlcPortOperISTATUS=_SdlcPortOperISTATUS_Object((1,3,6,1,2,1,41,1,1,2,1,5),_SdlcPortOperISTATUS_Type())
sdlcPortOperISTATUS.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcPortOperISTATUS.setStatus(_A)
_SdlcPortOperACTIVTO_Type=TimeInterval
_SdlcPortOperACTIVTO_Object=MibTableColumn
sdlcPortOperACTIVTO=_SdlcPortOperACTIVTO_Object((1,3,6,1,2,1,41,1,1,2,1,6),_SdlcPortOperACTIVTO_Type())
sdlcPortOperACTIVTO.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcPortOperACTIVTO.setStatus(_A)
_SdlcPortOperPAUSE_Type=TimeInterval
_SdlcPortOperPAUSE_Object=MibTableColumn
sdlcPortOperPAUSE=_SdlcPortOperPAUSE_Object((1,3,6,1,2,1,41,1,1,2,1,7),_SdlcPortOperPAUSE_Type())
sdlcPortOperPAUSE.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcPortOperPAUSE.setStatus(_A)
class _SdlcPortOperSlowPollMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('servlim',1),('pollpause',2),('other',3)))
_SdlcPortOperSlowPollMethod_Type.__name__=_D
_SdlcPortOperSlowPollMethod_Object=MibTableColumn
sdlcPortOperSlowPollMethod=_SdlcPortOperSlowPollMethod_Object((1,3,6,1,2,1,41,1,1,2,1,8),_SdlcPortOperSlowPollMethod_Type())
sdlcPortOperSlowPollMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcPortOperSlowPollMethod.setStatus(_A)
_SdlcPortOperSERVLIM_Type=Integer32
_SdlcPortOperSERVLIM_Object=MibTableColumn
sdlcPortOperSERVLIM=_SdlcPortOperSERVLIM_Object((1,3,6,1,2,1,41,1,1,2,1,9),_SdlcPortOperSERVLIM_Type())
sdlcPortOperSERVLIM.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcPortOperSERVLIM.setStatus(_A)
_SdlcPortOperSlowPollTimer_Type=TimeInterval
_SdlcPortOperSlowPollTimer_Object=MibTableColumn
sdlcPortOperSlowPollTimer=_SdlcPortOperSlowPollTimer_Object((1,3,6,1,2,1,41,1,1,2,1,10),_SdlcPortOperSlowPollTimer_Type())
sdlcPortOperSlowPollTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcPortOperSlowPollTimer.setStatus(_A)
_SdlcPortOperLastModifyTime_Type=TimeTicks
_SdlcPortOperLastModifyTime_Object=MibTableColumn
sdlcPortOperLastModifyTime=_SdlcPortOperLastModifyTime_Object((1,3,6,1,2,1,41,1,1,2,1,11),_SdlcPortOperLastModifyTime_Type())
sdlcPortOperLastModifyTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcPortOperLastModifyTime.setStatus(_A)
_SdlcPortOperLastFailTime_Type=TimeTicks
_SdlcPortOperLastFailTime_Object=MibTableColumn
sdlcPortOperLastFailTime=_SdlcPortOperLastFailTime_Object((1,3,6,1,2,1,41,1,1,2,1,12),_SdlcPortOperLastFailTime_Type())
sdlcPortOperLastFailTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcPortOperLastFailTime.setStatus(_A)
class _SdlcPortOperLastFailCause_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),('physical',2)))
_SdlcPortOperLastFailCause_Type.__name__=_D
_SdlcPortOperLastFailCause_Object=MibTableColumn
sdlcPortOperLastFailCause=_SdlcPortOperLastFailCause_Object((1,3,6,1,2,1,41,1,1,2,1,13),_SdlcPortOperLastFailCause_Type())
sdlcPortOperLastFailCause.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcPortOperLastFailCause.setStatus(_A)
_SdlcPortStatsTable_Object=MibTable
sdlcPortStatsTable=_SdlcPortStatsTable_Object((1,3,6,1,2,1,41,1,1,3))
if mibBuilder.loadTexts:sdlcPortStatsTable.setStatus(_A)
_SdlcPortStatsEntry_Object=MibTableRow
sdlcPortStatsEntry=_SdlcPortStatsEntry_Object((1,3,6,1,2,1,41,1,1,3,1))
sdlcPortStatsEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:sdlcPortStatsEntry.setStatus(_A)
_SdlcPortStatsPhysicalFailures_Type=Counter32
_SdlcPortStatsPhysicalFailures_Object=MibTableColumn
sdlcPortStatsPhysicalFailures=_SdlcPortStatsPhysicalFailures_Object((1,3,6,1,2,1,41,1,1,3,1,1),_SdlcPortStatsPhysicalFailures_Type())
sdlcPortStatsPhysicalFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcPortStatsPhysicalFailures.setStatus(_A)
_SdlcPortStatsInvalidAddresses_Type=Counter32
_SdlcPortStatsInvalidAddresses_Object=MibTableColumn
sdlcPortStatsInvalidAddresses=_SdlcPortStatsInvalidAddresses_Object((1,3,6,1,2,1,41,1,1,3,1,2),_SdlcPortStatsInvalidAddresses_Type())
sdlcPortStatsInvalidAddresses.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcPortStatsInvalidAddresses.setStatus(_A)
_SdlcPortStatsDwarfFrames_Type=Counter32
_SdlcPortStatsDwarfFrames_Object=MibTableColumn
sdlcPortStatsDwarfFrames=_SdlcPortStatsDwarfFrames_Object((1,3,6,1,2,1,41,1,1,3,1,3),_SdlcPortStatsDwarfFrames_Type())
sdlcPortStatsDwarfFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcPortStatsDwarfFrames.setStatus(_A)
_SdlcPortStatsPollsIn_Type=Counter32
_SdlcPortStatsPollsIn_Object=MibTableColumn
sdlcPortStatsPollsIn=_SdlcPortStatsPollsIn_Object((1,3,6,1,2,1,41,1,1,3,1,4),_SdlcPortStatsPollsIn_Type())
sdlcPortStatsPollsIn.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcPortStatsPollsIn.setStatus(_A)
_SdlcPortStatsPollsOut_Type=Counter32
_SdlcPortStatsPollsOut_Object=MibTableColumn
sdlcPortStatsPollsOut=_SdlcPortStatsPollsOut_Object((1,3,6,1,2,1,41,1,1,3,1,5),_SdlcPortStatsPollsOut_Type())
sdlcPortStatsPollsOut.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcPortStatsPollsOut.setStatus(_A)
_SdlcPortStatsPollRspsIn_Type=Counter32
_SdlcPortStatsPollRspsIn_Object=MibTableColumn
sdlcPortStatsPollRspsIn=_SdlcPortStatsPollRspsIn_Object((1,3,6,1,2,1,41,1,1,3,1,6),_SdlcPortStatsPollRspsIn_Type())
sdlcPortStatsPollRspsIn.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcPortStatsPollRspsIn.setStatus(_A)
_SdlcPortStatsPollRspsOut_Type=Counter32
_SdlcPortStatsPollRspsOut_Object=MibTableColumn
sdlcPortStatsPollRspsOut=_SdlcPortStatsPollRspsOut_Object((1,3,6,1,2,1,41,1,1,3,1,7),_SdlcPortStatsPollRspsOut_Type())
sdlcPortStatsPollRspsOut.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcPortStatsPollRspsOut.setStatus(_A)
_SdlcPortStatsLocalBusies_Type=Counter32
_SdlcPortStatsLocalBusies_Object=MibTableColumn
sdlcPortStatsLocalBusies=_SdlcPortStatsLocalBusies_Object((1,3,6,1,2,1,41,1,1,3,1,8),_SdlcPortStatsLocalBusies_Type())
sdlcPortStatsLocalBusies.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcPortStatsLocalBusies.setStatus(_A)
_SdlcPortStatsRemoteBusies_Type=Counter32
_SdlcPortStatsRemoteBusies_Object=MibTableColumn
sdlcPortStatsRemoteBusies=_SdlcPortStatsRemoteBusies_Object((1,3,6,1,2,1,41,1,1,3,1,9),_SdlcPortStatsRemoteBusies_Type())
sdlcPortStatsRemoteBusies.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcPortStatsRemoteBusies.setStatus(_A)
_SdlcPortStatsIFramesIn_Type=Counter32
_SdlcPortStatsIFramesIn_Object=MibTableColumn
sdlcPortStatsIFramesIn=_SdlcPortStatsIFramesIn_Object((1,3,6,1,2,1,41,1,1,3,1,10),_SdlcPortStatsIFramesIn_Type())
sdlcPortStatsIFramesIn.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcPortStatsIFramesIn.setStatus(_A)
_SdlcPortStatsIFramesOut_Type=Counter32
_SdlcPortStatsIFramesOut_Object=MibTableColumn
sdlcPortStatsIFramesOut=_SdlcPortStatsIFramesOut_Object((1,3,6,1,2,1,41,1,1,3,1,11),_SdlcPortStatsIFramesOut_Type())
sdlcPortStatsIFramesOut.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcPortStatsIFramesOut.setStatus(_A)
_SdlcPortStatsOctetsIn_Type=Counter32
_SdlcPortStatsOctetsIn_Object=MibTableColumn
sdlcPortStatsOctetsIn=_SdlcPortStatsOctetsIn_Object((1,3,6,1,2,1,41,1,1,3,1,12),_SdlcPortStatsOctetsIn_Type())
sdlcPortStatsOctetsIn.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcPortStatsOctetsIn.setStatus(_A)
_SdlcPortStatsOctetsOut_Type=Counter32
_SdlcPortStatsOctetsOut_Object=MibTableColumn
sdlcPortStatsOctetsOut=_SdlcPortStatsOctetsOut_Object((1,3,6,1,2,1,41,1,1,3,1,13),_SdlcPortStatsOctetsOut_Type())
sdlcPortStatsOctetsOut.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcPortStatsOctetsOut.setStatus(_A)
_SdlcPortStatsProtocolErrs_Type=Counter32
_SdlcPortStatsProtocolErrs_Object=MibTableColumn
sdlcPortStatsProtocolErrs=_SdlcPortStatsProtocolErrs_Object((1,3,6,1,2,1,41,1,1,3,1,14),_SdlcPortStatsProtocolErrs_Type())
sdlcPortStatsProtocolErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcPortStatsProtocolErrs.setStatus(_A)
_SdlcPortStatsActivityTOs_Type=Counter32
_SdlcPortStatsActivityTOs_Object=MibTableColumn
sdlcPortStatsActivityTOs=_SdlcPortStatsActivityTOs_Object((1,3,6,1,2,1,41,1,1,3,1,15),_SdlcPortStatsActivityTOs_Type())
sdlcPortStatsActivityTOs.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcPortStatsActivityTOs.setStatus(_A)
_SdlcPortStatsRNRLIMITs_Type=Counter32
_SdlcPortStatsRNRLIMITs_Object=MibTableColumn
sdlcPortStatsRNRLIMITs=_SdlcPortStatsRNRLIMITs_Object((1,3,6,1,2,1,41,1,1,3,1,16),_SdlcPortStatsRNRLIMITs_Type())
sdlcPortStatsRNRLIMITs.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcPortStatsRNRLIMITs.setStatus(_A)
_SdlcPortStatsRetriesExps_Type=Counter32
_SdlcPortStatsRetriesExps_Object=MibTableColumn
sdlcPortStatsRetriesExps=_SdlcPortStatsRetriesExps_Object((1,3,6,1,2,1,41,1,1,3,1,17),_SdlcPortStatsRetriesExps_Type())
sdlcPortStatsRetriesExps.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcPortStatsRetriesExps.setStatus(_A)
_SdlcPortStatsRetransmitsIn_Type=Counter32
_SdlcPortStatsRetransmitsIn_Object=MibTableColumn
sdlcPortStatsRetransmitsIn=_SdlcPortStatsRetransmitsIn_Object((1,3,6,1,2,1,41,1,1,3,1,18),_SdlcPortStatsRetransmitsIn_Type())
sdlcPortStatsRetransmitsIn.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcPortStatsRetransmitsIn.setStatus(_A)
_SdlcPortStatsRetransmitsOut_Type=Counter32
_SdlcPortStatsRetransmitsOut_Object=MibTableColumn
sdlcPortStatsRetransmitsOut=_SdlcPortStatsRetransmitsOut_Object((1,3,6,1,2,1,41,1,1,3,1,19),_SdlcPortStatsRetransmitsOut_Type())
sdlcPortStatsRetransmitsOut.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcPortStatsRetransmitsOut.setStatus(_A)
_SdlcLSGroup_ObjectIdentity=ObjectIdentity
sdlcLSGroup=_SdlcLSGroup_ObjectIdentity((1,3,6,1,2,1,41,1,2))
_SdlcLSAdminTable_Object=MibTable
sdlcLSAdminTable=_SdlcLSAdminTable_Object((1,3,6,1,2,1,41,1,2,1))
if mibBuilder.loadTexts:sdlcLSAdminTable.setStatus(_A)
_SdlcLSAdminEntry_Object=MibTableRow
sdlcLSAdminEntry=_SdlcLSAdminEntry_Object((1,3,6,1,2,1,41,1,2,1,1))
sdlcLSAdminEntry.setIndexNames((0,_F,_G),(0,_B,_J))
if mibBuilder.loadTexts:sdlcLSAdminEntry.setStatus(_A)
class _SdlcLSAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SdlcLSAddress_Type.__name__=_D
_SdlcLSAddress_Object=MibTableColumn
sdlcLSAddress=_SdlcLSAddress_Object((1,3,6,1,2,1,41,1,2,1,1,1),_SdlcLSAddress_Type())
sdlcLSAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:sdlcLSAddress.setStatus(_A)
class _SdlcLSAdminName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_SdlcLSAdminName_Type.__name__=_K
_SdlcLSAdminName_Object=MibTableColumn
sdlcLSAdminName=_SdlcLSAdminName_Object((1,3,6,1,2,1,41,1,2,1,1,2),_SdlcLSAdminName_Type())
sdlcLSAdminName.setMaxAccess(_E)
if mibBuilder.loadTexts:sdlcLSAdminName.setStatus(_A)
class _SdlcLSAdminState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_SdlcLSAdminState_Type.__name__=_D
_SdlcLSAdminState_Object=MibTableColumn
sdlcLSAdminState=_SdlcLSAdminState_Object((1,3,6,1,2,1,41,1,2,1,1,3),_SdlcLSAdminState_Type())
sdlcLSAdminState.setMaxAccess(_E)
if mibBuilder.loadTexts:sdlcLSAdminState.setStatus(_A)
class _SdlcLSAdminISTATUS_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_SdlcLSAdminISTATUS_Type.__name__=_D
_SdlcLSAdminISTATUS_Object=MibTableColumn
sdlcLSAdminISTATUS=_SdlcLSAdminISTATUS_Object((1,3,6,1,2,1,41,1,2,1,1,4),_SdlcLSAdminISTATUS_Type())
sdlcLSAdminISTATUS.setMaxAccess(_E)
if mibBuilder.loadTexts:sdlcLSAdminISTATUS.setStatus(_A)
_SdlcLSAdminMAXDATASend_Type=Integer32
_SdlcLSAdminMAXDATASend_Object=MibTableColumn
sdlcLSAdminMAXDATASend=_SdlcLSAdminMAXDATASend_Object((1,3,6,1,2,1,41,1,2,1,1,5),_SdlcLSAdminMAXDATASend_Type())
sdlcLSAdminMAXDATASend.setMaxAccess(_E)
if mibBuilder.loadTexts:sdlcLSAdminMAXDATASend.setStatus(_A)
_SdlcLSAdminMAXDATARcv_Type=Integer32
_SdlcLSAdminMAXDATARcv_Object=MibTableColumn
sdlcLSAdminMAXDATARcv=_SdlcLSAdminMAXDATARcv_Object((1,3,6,1,2,1,41,1,2,1,1,6),_SdlcLSAdminMAXDATARcv_Type())
sdlcLSAdminMAXDATARcv.setMaxAccess(_E)
if mibBuilder.loadTexts:sdlcLSAdminMAXDATARcv.setStatus(_A)
class _SdlcLSAdminREPLYTO_Type(TimeInterval):defaultValue=100
_SdlcLSAdminREPLYTO_Type.__name__=_I
_SdlcLSAdminREPLYTO_Object=MibTableColumn
sdlcLSAdminREPLYTO=_SdlcLSAdminREPLYTO_Object((1,3,6,1,2,1,41,1,2,1,1,7),_SdlcLSAdminREPLYTO_Type())
sdlcLSAdminREPLYTO.setMaxAccess(_E)
if mibBuilder.loadTexts:sdlcLSAdminREPLYTO.setStatus(_A)
class _SdlcLSAdminMAXIN_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_SdlcLSAdminMAXIN_Type.__name__=_D
_SdlcLSAdminMAXIN_Object=MibTableColumn
sdlcLSAdminMAXIN=_SdlcLSAdminMAXIN_Object((1,3,6,1,2,1,41,1,2,1,1,8),_SdlcLSAdminMAXIN_Type())
sdlcLSAdminMAXIN.setMaxAccess(_E)
if mibBuilder.loadTexts:sdlcLSAdminMAXIN.setStatus(_A)
class _SdlcLSAdminMAXOUT_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_SdlcLSAdminMAXOUT_Type.__name__=_D
_SdlcLSAdminMAXOUT_Object=MibTableColumn
sdlcLSAdminMAXOUT=_SdlcLSAdminMAXOUT_Object((1,3,6,1,2,1,41,1,2,1,1,9),_SdlcLSAdminMAXOUT_Type())
sdlcLSAdminMAXOUT.setMaxAccess(_E)
if mibBuilder.loadTexts:sdlcLSAdminMAXOUT.setStatus(_A)
class _SdlcLSAdminMODULO_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(8,128)));namedValues=NamedValues(*(('eight',8),(_i,128)))
_SdlcLSAdminMODULO_Type.__name__=_D
_SdlcLSAdminMODULO_Object=MibTableColumn
sdlcLSAdminMODULO=_SdlcLSAdminMODULO_Object((1,3,6,1,2,1,41,1,2,1,1,10),_SdlcLSAdminMODULO_Type())
sdlcLSAdminMODULO.setMaxAccess(_E)
if mibBuilder.loadTexts:sdlcLSAdminMODULO.setStatus(_A)
class _SdlcLSAdminRETRIESm_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_SdlcLSAdminRETRIESm_Type.__name__=_D
_SdlcLSAdminRETRIESm_Object=MibTableColumn
sdlcLSAdminRETRIESm=_SdlcLSAdminRETRIESm_Object((1,3,6,1,2,1,41,1,2,1,1,11),_SdlcLSAdminRETRIESm_Type())
sdlcLSAdminRETRIESm.setMaxAccess(_E)
if mibBuilder.loadTexts:sdlcLSAdminRETRIESm.setStatus(_A)
class _SdlcLSAdminRETRIESt_Type(TimeInterval):defaultValue=0
_SdlcLSAdminRETRIESt_Type.__name__=_I
_SdlcLSAdminRETRIESt_Object=MibTableColumn
sdlcLSAdminRETRIESt=_SdlcLSAdminRETRIESt_Object((1,3,6,1,2,1,41,1,2,1,1,12),_SdlcLSAdminRETRIESt_Type())
sdlcLSAdminRETRIESt.setMaxAccess(_E)
if mibBuilder.loadTexts:sdlcLSAdminRETRIESt.setStatus(_A)
class _SdlcLSAdminRETRIESn_Type(Integer32):defaultValue=0
_SdlcLSAdminRETRIESn_Type.__name__=_D
_SdlcLSAdminRETRIESn_Object=MibTableColumn
sdlcLSAdminRETRIESn=_SdlcLSAdminRETRIESn_Object((1,3,6,1,2,1,41,1,2,1,1,13),_SdlcLSAdminRETRIESn_Type())
sdlcLSAdminRETRIESn.setMaxAccess(_E)
if mibBuilder.loadTexts:sdlcLSAdminRETRIESn.setStatus(_A)
class _SdlcLSAdminRNRLIMIT_Type(TimeInterval):defaultValue=18000
_SdlcLSAdminRNRLIMIT_Type.__name__=_I
_SdlcLSAdminRNRLIMIT_Object=MibTableColumn
sdlcLSAdminRNRLIMIT=_SdlcLSAdminRNRLIMIT_Object((1,3,6,1,2,1,41,1,2,1,1,14),_SdlcLSAdminRNRLIMIT_Type())
sdlcLSAdminRNRLIMIT.setMaxAccess(_E)
if mibBuilder.loadTexts:sdlcLSAdminRNRLIMIT.setStatus(_A)
class _SdlcLSAdminDATMODE_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('half',1),('full',2)))
_SdlcLSAdminDATMODE_Type.__name__=_D
_SdlcLSAdminDATMODE_Object=MibTableColumn
sdlcLSAdminDATMODE=_SdlcLSAdminDATMODE_Object((1,3,6,1,2,1,41,1,2,1,1,15),_SdlcLSAdminDATMODE_Type())
sdlcLSAdminDATMODE.setMaxAccess(_E)
if mibBuilder.loadTexts:sdlcLSAdminDATMODE.setStatus(_A)
class _SdlcLSAdminGPoll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_SdlcLSAdminGPoll_Type.__name__=_D
_SdlcLSAdminGPoll_Object=MibTableColumn
sdlcLSAdminGPoll=_SdlcLSAdminGPoll_Object((1,3,6,1,2,1,41,1,2,1,1,16),_SdlcLSAdminGPoll_Type())
sdlcLSAdminGPoll.setMaxAccess(_E)
if mibBuilder.loadTexts:sdlcLSAdminGPoll.setStatus(_A)
class _SdlcLSAdminSimRim_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('no',1),(_R,2)))
_SdlcLSAdminSimRim_Type.__name__=_D
_SdlcLSAdminSimRim_Object=MibTableColumn
sdlcLSAdminSimRim=_SdlcLSAdminSimRim_Object((1,3,6,1,2,1,41,1,2,1,1,17),_SdlcLSAdminSimRim_Type())
sdlcLSAdminSimRim.setMaxAccess(_E)
if mibBuilder.loadTexts:sdlcLSAdminSimRim.setStatus(_A)
class _SdlcLSAdminXmitRcvCap_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('twa',1),('tws',2)))
_SdlcLSAdminXmitRcvCap_Type.__name__=_D
_SdlcLSAdminXmitRcvCap_Object=MibTableColumn
sdlcLSAdminXmitRcvCap=_SdlcLSAdminXmitRcvCap_Object((1,3,6,1,2,1,41,1,2,1,1,18),_SdlcLSAdminXmitRcvCap_Type())
sdlcLSAdminXmitRcvCap.setMaxAccess(_E)
if mibBuilder.loadTexts:sdlcLSAdminXmitRcvCap.setStatus(_A)
_SdlcLSAdminRowStatus_Type=RowStatus
_SdlcLSAdminRowStatus_Object=MibTableColumn
sdlcLSAdminRowStatus=_SdlcLSAdminRowStatus_Object((1,3,6,1,2,1,41,1,2,1,1,19),_SdlcLSAdminRowStatus_Type())
sdlcLSAdminRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sdlcLSAdminRowStatus.setStatus(_A)
_SdlcLSOperTable_Object=MibTable
sdlcLSOperTable=_SdlcLSOperTable_Object((1,3,6,1,2,1,41,1,2,2))
if mibBuilder.loadTexts:sdlcLSOperTable.setStatus(_A)
_SdlcLSOperEntry_Object=MibTableRow
sdlcLSOperEntry=_SdlcLSOperEntry_Object((1,3,6,1,2,1,41,1,2,2,1))
sdlcLSOperEntry.setIndexNames((0,_F,_G),(0,_B,_J))
if mibBuilder.loadTexts:sdlcLSOperEntry.setStatus(_A)
class _SdlcLSOperName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_SdlcLSOperName_Type.__name__=_K
_SdlcLSOperName_Object=MibTableColumn
sdlcLSOperName=_SdlcLSOperName_Object((1,3,6,1,2,1,41,1,2,2,1,1),_SdlcLSOperName_Type())
sdlcLSOperName.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSOperName.setStatus(_A)
class _SdlcLSOperRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),(_Q,2),(_O,3)))
_SdlcLSOperRole_Type.__name__=_D
_SdlcLSOperRole_Object=MibTableColumn
sdlcLSOperRole=_SdlcLSOperRole_Object((1,3,6,1,2,1,41,1,2,2,1,2),_SdlcLSOperRole_Type())
sdlcLSOperRole.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSOperRole.setStatus(_A)
class _SdlcLSOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('discontacted',1),('contactPending',2),('contacted',3),('discontactPending',4)))
_SdlcLSOperState_Type.__name__=_D
_SdlcLSOperState_Object=MibTableColumn
sdlcLSOperState=_SdlcLSOperState_Object((1,3,6,1,2,1,41,1,2,2,1,3),_SdlcLSOperState_Type())
sdlcLSOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSOperState.setStatus(_A)
_SdlcLSOperMAXDATASend_Type=Integer32
_SdlcLSOperMAXDATASend_Object=MibTableColumn
sdlcLSOperMAXDATASend=_SdlcLSOperMAXDATASend_Object((1,3,6,1,2,1,41,1,2,2,1,4),_SdlcLSOperMAXDATASend_Type())
sdlcLSOperMAXDATASend.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSOperMAXDATASend.setStatus(_A)
_SdlcLSOperREPLYTO_Type=TimeInterval
_SdlcLSOperREPLYTO_Object=MibTableColumn
sdlcLSOperREPLYTO=_SdlcLSOperREPLYTO_Object((1,3,6,1,2,1,41,1,2,2,1,5),_SdlcLSOperREPLYTO_Type())
sdlcLSOperREPLYTO.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSOperREPLYTO.setStatus(_A)
class _SdlcLSOperMAXIN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_SdlcLSOperMAXIN_Type.__name__=_D
_SdlcLSOperMAXIN_Object=MibTableColumn
sdlcLSOperMAXIN=_SdlcLSOperMAXIN_Object((1,3,6,1,2,1,41,1,2,2,1,6),_SdlcLSOperMAXIN_Type())
sdlcLSOperMAXIN.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSOperMAXIN.setStatus(_A)
class _SdlcLSOperMAXOUT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_SdlcLSOperMAXOUT_Type.__name__=_D
_SdlcLSOperMAXOUT_Object=MibTableColumn
sdlcLSOperMAXOUT=_SdlcLSOperMAXOUT_Object((1,3,6,1,2,1,41,1,2,2,1,7),_SdlcLSOperMAXOUT_Type())
sdlcLSOperMAXOUT.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSOperMAXOUT.setStatus(_A)
class _SdlcLSOperMODULO_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(8,128)));namedValues=NamedValues(*(('eight',8),(_i,128)))
_SdlcLSOperMODULO_Type.__name__=_D
_SdlcLSOperMODULO_Object=MibTableColumn
sdlcLSOperMODULO=_SdlcLSOperMODULO_Object((1,3,6,1,2,1,41,1,2,2,1,8),_SdlcLSOperMODULO_Type())
sdlcLSOperMODULO.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSOperMODULO.setStatus(_A)
class _SdlcLSOperRETRIESm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_SdlcLSOperRETRIESm_Type.__name__=_D
_SdlcLSOperRETRIESm_Object=MibTableColumn
sdlcLSOperRETRIESm=_SdlcLSOperRETRIESm_Object((1,3,6,1,2,1,41,1,2,2,1,9),_SdlcLSOperRETRIESm_Type())
sdlcLSOperRETRIESm.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSOperRETRIESm.setStatus(_A)
_SdlcLSOperRETRIESt_Type=TimeInterval
_SdlcLSOperRETRIESt_Object=MibTableColumn
sdlcLSOperRETRIESt=_SdlcLSOperRETRIESt_Object((1,3,6,1,2,1,41,1,2,2,1,10),_SdlcLSOperRETRIESt_Type())
sdlcLSOperRETRIESt.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSOperRETRIESt.setStatus(_A)
class _SdlcLSOperRETRIESn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_SdlcLSOperRETRIESn_Type.__name__=_D
_SdlcLSOperRETRIESn_Object=MibTableColumn
sdlcLSOperRETRIESn=_SdlcLSOperRETRIESn_Object((1,3,6,1,2,1,41,1,2,2,1,11),_SdlcLSOperRETRIESn_Type())
sdlcLSOperRETRIESn.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSOperRETRIESn.setStatus(_A)
_SdlcLSOperRNRLIMIT_Type=TimeInterval
_SdlcLSOperRNRLIMIT_Object=MibTableColumn
sdlcLSOperRNRLIMIT=_SdlcLSOperRNRLIMIT_Object((1,3,6,1,2,1,41,1,2,2,1,12),_SdlcLSOperRNRLIMIT_Type())
sdlcLSOperRNRLIMIT.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSOperRNRLIMIT.setStatus(_A)
class _SdlcLSOperDATMODE_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('half',1),('full',2)))
_SdlcLSOperDATMODE_Type.__name__=_D
_SdlcLSOperDATMODE_Object=MibTableColumn
sdlcLSOperDATMODE=_SdlcLSOperDATMODE_Object((1,3,6,1,2,1,41,1,2,2,1,13),_SdlcLSOperDATMODE_Type())
sdlcLSOperDATMODE.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSOperDATMODE.setStatus(_A)
_SdlcLSOperLastModifyTime_Type=TimeTicks
_SdlcLSOperLastModifyTime_Object=MibTableColumn
sdlcLSOperLastModifyTime=_SdlcLSOperLastModifyTime_Object((1,3,6,1,2,1,41,1,2,2,1,14),_SdlcLSOperLastModifyTime_Type())
sdlcLSOperLastModifyTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSOperLastModifyTime.setStatus(_A)
_SdlcLSOperLastFailTime_Type=TimeTicks
_SdlcLSOperLastFailTime_Object=MibTableColumn
sdlcLSOperLastFailTime=_SdlcLSOperLastFailTime_Object((1,3,6,1,2,1,41,1,2,2,1,15),_SdlcLSOperLastFailTime_Type())
sdlcLSOperLastFailTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSOperLastFailTime.setStatus(_A)
class _SdlcLSOperLastFailCause_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_O,1),('rxFRMR',2),('txFRMR',3),('noResponse',4),('protocolErr',5),('noActivity',6),('rnrLimit',7),('retriesExpired',8)))
_SdlcLSOperLastFailCause_Type.__name__=_D
_SdlcLSOperLastFailCause_Object=MibTableColumn
sdlcLSOperLastFailCause=_SdlcLSOperLastFailCause_Object((1,3,6,1,2,1,41,1,2,2,1,16),_SdlcLSOperLastFailCause_Type())
sdlcLSOperLastFailCause.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSOperLastFailCause.setStatus(_A)
class _SdlcLSOperLastFailCtrlIn_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,2))
_SdlcLSOperLastFailCtrlIn_Type.__name__=_L
_SdlcLSOperLastFailCtrlIn_Object=MibTableColumn
sdlcLSOperLastFailCtrlIn=_SdlcLSOperLastFailCtrlIn_Object((1,3,6,1,2,1,41,1,2,2,1,17),_SdlcLSOperLastFailCtrlIn_Type())
sdlcLSOperLastFailCtrlIn.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSOperLastFailCtrlIn.setStatus(_A)
class _SdlcLSOperLastFailCtrlOut_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,2))
_SdlcLSOperLastFailCtrlOut_Type.__name__=_L
_SdlcLSOperLastFailCtrlOut_Object=MibTableColumn
sdlcLSOperLastFailCtrlOut=_SdlcLSOperLastFailCtrlOut_Object((1,3,6,1,2,1,41,1,2,2,1,18),_SdlcLSOperLastFailCtrlOut_Type())
sdlcLSOperLastFailCtrlOut.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSOperLastFailCtrlOut.setStatus(_A)
class _SdlcLSOperLastFailFRMRInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_SdlcLSOperLastFailFRMRInfo_Type.__name__=_L
_SdlcLSOperLastFailFRMRInfo_Object=MibTableColumn
sdlcLSOperLastFailFRMRInfo=_SdlcLSOperLastFailFRMRInfo_Object((1,3,6,1,2,1,41,1,2,2,1,19),_SdlcLSOperLastFailFRMRInfo_Type())
sdlcLSOperLastFailFRMRInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSOperLastFailFRMRInfo.setStatus(_A)
_SdlcLSOperLastFailREPLYTOs_Type=Counter32
_SdlcLSOperLastFailREPLYTOs_Object=MibTableColumn
sdlcLSOperLastFailREPLYTOs=_SdlcLSOperLastFailREPLYTOs_Object((1,3,6,1,2,1,41,1,2,2,1,20),_SdlcLSOperLastFailREPLYTOs_Type())
sdlcLSOperLastFailREPLYTOs.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSOperLastFailREPLYTOs.setStatus(_A)
class _SdlcLSOperEcho_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('no',1),(_R,2)))
_SdlcLSOperEcho_Type.__name__=_D
_SdlcLSOperEcho_Object=MibTableColumn
sdlcLSOperEcho=_SdlcLSOperEcho_Object((1,3,6,1,2,1,41,1,2,2,1,21),_SdlcLSOperEcho_Type())
sdlcLSOperEcho.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSOperEcho.setStatus(_A)
class _SdlcLSOperGPoll_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_SdlcLSOperGPoll_Type.__name__=_D
_SdlcLSOperGPoll_Object=MibTableColumn
sdlcLSOperGPoll=_SdlcLSOperGPoll_Object((1,3,6,1,2,1,41,1,2,2,1,22),_SdlcLSOperGPoll_Type())
sdlcLSOperGPoll.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSOperGPoll.setStatus(_A)
class _SdlcLSOperSimRim_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('no',1),(_R,2)))
_SdlcLSOperSimRim_Type.__name__=_D
_SdlcLSOperSimRim_Object=MibTableColumn
sdlcLSOperSimRim=_SdlcLSOperSimRim_Object((1,3,6,1,2,1,41,1,2,2,1,23),_SdlcLSOperSimRim_Type())
sdlcLSOperSimRim.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSOperSimRim.setStatus(_A)
class _SdlcLSOperXmitRcvCap_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('twa',1),('tws',2)))
_SdlcLSOperXmitRcvCap_Type.__name__=_D
_SdlcLSOperXmitRcvCap_Object=MibTableColumn
sdlcLSOperXmitRcvCap=_SdlcLSOperXmitRcvCap_Object((1,3,6,1,2,1,41,1,2,2,1,24),_SdlcLSOperXmitRcvCap_Type())
sdlcLSOperXmitRcvCap.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSOperXmitRcvCap.setStatus(_A)
_SdlcLSStatsTable_Object=MibTable
sdlcLSStatsTable=_SdlcLSStatsTable_Object((1,3,6,1,2,1,41,1,2,3))
if mibBuilder.loadTexts:sdlcLSStatsTable.setStatus(_A)
_SdlcLSStatsEntry_Object=MibTableRow
sdlcLSStatsEntry=_SdlcLSStatsEntry_Object((1,3,6,1,2,1,41,1,2,3,1))
sdlcLSStatsEntry.setIndexNames((0,_F,_G),(0,_B,_J))
if mibBuilder.loadTexts:sdlcLSStatsEntry.setStatus(_A)
_SdlcLSStatsBLUsIn_Type=Counter32
_SdlcLSStatsBLUsIn_Object=MibTableColumn
sdlcLSStatsBLUsIn=_SdlcLSStatsBLUsIn_Object((1,3,6,1,2,1,41,1,2,3,1,1),_SdlcLSStatsBLUsIn_Type())
sdlcLSStatsBLUsIn.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSStatsBLUsIn.setStatus(_A)
_SdlcLSStatsBLUsOut_Type=Counter32
_SdlcLSStatsBLUsOut_Object=MibTableColumn
sdlcLSStatsBLUsOut=_SdlcLSStatsBLUsOut_Object((1,3,6,1,2,1,41,1,2,3,1,2),_SdlcLSStatsBLUsOut_Type())
sdlcLSStatsBLUsOut.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSStatsBLUsOut.setStatus(_A)
_SdlcLSStatsOctetsIn_Type=Counter32
_SdlcLSStatsOctetsIn_Object=MibTableColumn
sdlcLSStatsOctetsIn=_SdlcLSStatsOctetsIn_Object((1,3,6,1,2,1,41,1,2,3,1,3),_SdlcLSStatsOctetsIn_Type())
sdlcLSStatsOctetsIn.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSStatsOctetsIn.setStatus(_A)
_SdlcLSStatsOctetsOut_Type=Counter32
_SdlcLSStatsOctetsOut_Object=MibTableColumn
sdlcLSStatsOctetsOut=_SdlcLSStatsOctetsOut_Object((1,3,6,1,2,1,41,1,2,3,1,4),_SdlcLSStatsOctetsOut_Type())
sdlcLSStatsOctetsOut.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSStatsOctetsOut.setStatus(_A)
_SdlcLSStatsPollsIn_Type=Counter32
_SdlcLSStatsPollsIn_Object=MibTableColumn
sdlcLSStatsPollsIn=_SdlcLSStatsPollsIn_Object((1,3,6,1,2,1,41,1,2,3,1,5),_SdlcLSStatsPollsIn_Type())
sdlcLSStatsPollsIn.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSStatsPollsIn.setStatus(_A)
_SdlcLSStatsPollsOut_Type=Counter32
_SdlcLSStatsPollsOut_Object=MibTableColumn
sdlcLSStatsPollsOut=_SdlcLSStatsPollsOut_Object((1,3,6,1,2,1,41,1,2,3,1,6),_SdlcLSStatsPollsOut_Type())
sdlcLSStatsPollsOut.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSStatsPollsOut.setStatus(_A)
_SdlcLSStatsPollRspsOut_Type=Counter32
_SdlcLSStatsPollRspsOut_Object=MibTableColumn
sdlcLSStatsPollRspsOut=_SdlcLSStatsPollRspsOut_Object((1,3,6,1,2,1,41,1,2,3,1,7),_SdlcLSStatsPollRspsOut_Type())
sdlcLSStatsPollRspsOut.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSStatsPollRspsOut.setStatus(_A)
_SdlcLSStatsPollRspsIn_Type=Counter32
_SdlcLSStatsPollRspsIn_Object=MibTableColumn
sdlcLSStatsPollRspsIn=_SdlcLSStatsPollRspsIn_Object((1,3,6,1,2,1,41,1,2,3,1,8),_SdlcLSStatsPollRspsIn_Type())
sdlcLSStatsPollRspsIn.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSStatsPollRspsIn.setStatus(_A)
_SdlcLSStatsLocalBusies_Type=Counter32
_SdlcLSStatsLocalBusies_Object=MibTableColumn
sdlcLSStatsLocalBusies=_SdlcLSStatsLocalBusies_Object((1,3,6,1,2,1,41,1,2,3,1,9),_SdlcLSStatsLocalBusies_Type())
sdlcLSStatsLocalBusies.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSStatsLocalBusies.setStatus(_A)
_SdlcLSStatsRemoteBusies_Type=Counter32
_SdlcLSStatsRemoteBusies_Object=MibTableColumn
sdlcLSStatsRemoteBusies=_SdlcLSStatsRemoteBusies_Object((1,3,6,1,2,1,41,1,2,3,1,10),_SdlcLSStatsRemoteBusies_Type())
sdlcLSStatsRemoteBusies.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSStatsRemoteBusies.setStatus(_A)
_SdlcLSStatsIFramesIn_Type=Counter32
_SdlcLSStatsIFramesIn_Object=MibTableColumn
sdlcLSStatsIFramesIn=_SdlcLSStatsIFramesIn_Object((1,3,6,1,2,1,41,1,2,3,1,11),_SdlcLSStatsIFramesIn_Type())
sdlcLSStatsIFramesIn.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSStatsIFramesIn.setStatus(_A)
_SdlcLSStatsIFramesOut_Type=Counter32
_SdlcLSStatsIFramesOut_Object=MibTableColumn
sdlcLSStatsIFramesOut=_SdlcLSStatsIFramesOut_Object((1,3,6,1,2,1,41,1,2,3,1,12),_SdlcLSStatsIFramesOut_Type())
sdlcLSStatsIFramesOut.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSStatsIFramesOut.setStatus(_A)
_SdlcLSStatsUIFramesIn_Type=Counter32
_SdlcLSStatsUIFramesIn_Object=MibTableColumn
sdlcLSStatsUIFramesIn=_SdlcLSStatsUIFramesIn_Object((1,3,6,1,2,1,41,1,2,3,1,13),_SdlcLSStatsUIFramesIn_Type())
sdlcLSStatsUIFramesIn.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSStatsUIFramesIn.setStatus(_A)
_SdlcLSStatsUIFramesOut_Type=Counter32
_SdlcLSStatsUIFramesOut_Object=MibTableColumn
sdlcLSStatsUIFramesOut=_SdlcLSStatsUIFramesOut_Object((1,3,6,1,2,1,41,1,2,3,1,14),_SdlcLSStatsUIFramesOut_Type())
sdlcLSStatsUIFramesOut.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSStatsUIFramesOut.setStatus(_A)
_SdlcLSStatsXIDsIn_Type=Counter32
_SdlcLSStatsXIDsIn_Object=MibTableColumn
sdlcLSStatsXIDsIn=_SdlcLSStatsXIDsIn_Object((1,3,6,1,2,1,41,1,2,3,1,15),_SdlcLSStatsXIDsIn_Type())
sdlcLSStatsXIDsIn.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSStatsXIDsIn.setStatus(_A)
_SdlcLSStatsXIDsOut_Type=Counter32
_SdlcLSStatsXIDsOut_Object=MibTableColumn
sdlcLSStatsXIDsOut=_SdlcLSStatsXIDsOut_Object((1,3,6,1,2,1,41,1,2,3,1,16),_SdlcLSStatsXIDsOut_Type())
sdlcLSStatsXIDsOut.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSStatsXIDsOut.setStatus(_A)
_SdlcLSStatsTESTsIn_Type=Counter32
_SdlcLSStatsTESTsIn_Object=MibTableColumn
sdlcLSStatsTESTsIn=_SdlcLSStatsTESTsIn_Object((1,3,6,1,2,1,41,1,2,3,1,17),_SdlcLSStatsTESTsIn_Type())
sdlcLSStatsTESTsIn.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSStatsTESTsIn.setStatus(_A)
_SdlcLSStatsTESTsOut_Type=Counter32
_SdlcLSStatsTESTsOut_Object=MibTableColumn
sdlcLSStatsTESTsOut=_SdlcLSStatsTESTsOut_Object((1,3,6,1,2,1,41,1,2,3,1,18),_SdlcLSStatsTESTsOut_Type())
sdlcLSStatsTESTsOut.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSStatsTESTsOut.setStatus(_A)
_SdlcLSStatsREJsIn_Type=Counter32
_SdlcLSStatsREJsIn_Object=MibTableColumn
sdlcLSStatsREJsIn=_SdlcLSStatsREJsIn_Object((1,3,6,1,2,1,41,1,2,3,1,19),_SdlcLSStatsREJsIn_Type())
sdlcLSStatsREJsIn.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSStatsREJsIn.setStatus(_A)
_SdlcLSStatsREJsOut_Type=Counter32
_SdlcLSStatsREJsOut_Object=MibTableColumn
sdlcLSStatsREJsOut=_SdlcLSStatsREJsOut_Object((1,3,6,1,2,1,41,1,2,3,1,20),_SdlcLSStatsREJsOut_Type())
sdlcLSStatsREJsOut.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSStatsREJsOut.setStatus(_A)
_SdlcLSStatsFRMRsIn_Type=Counter32
_SdlcLSStatsFRMRsIn_Object=MibTableColumn
sdlcLSStatsFRMRsIn=_SdlcLSStatsFRMRsIn_Object((1,3,6,1,2,1,41,1,2,3,1,21),_SdlcLSStatsFRMRsIn_Type())
sdlcLSStatsFRMRsIn.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSStatsFRMRsIn.setStatus(_A)
_SdlcLSStatsFRMRsOut_Type=Counter32
_SdlcLSStatsFRMRsOut_Object=MibTableColumn
sdlcLSStatsFRMRsOut=_SdlcLSStatsFRMRsOut_Object((1,3,6,1,2,1,41,1,2,3,1,22),_SdlcLSStatsFRMRsOut_Type())
sdlcLSStatsFRMRsOut.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSStatsFRMRsOut.setStatus(_A)
_SdlcLSStatsSIMsIn_Type=Counter32
_SdlcLSStatsSIMsIn_Object=MibTableColumn
sdlcLSStatsSIMsIn=_SdlcLSStatsSIMsIn_Object((1,3,6,1,2,1,41,1,2,3,1,23),_SdlcLSStatsSIMsIn_Type())
sdlcLSStatsSIMsIn.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSStatsSIMsIn.setStatus(_A)
_SdlcLSStatsSIMsOut_Type=Counter32
_SdlcLSStatsSIMsOut_Object=MibTableColumn
sdlcLSStatsSIMsOut=_SdlcLSStatsSIMsOut_Object((1,3,6,1,2,1,41,1,2,3,1,24),_SdlcLSStatsSIMsOut_Type())
sdlcLSStatsSIMsOut.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSStatsSIMsOut.setStatus(_A)
_SdlcLSStatsRIMsIn_Type=Counter32
_SdlcLSStatsRIMsIn_Object=MibTableColumn
sdlcLSStatsRIMsIn=_SdlcLSStatsRIMsIn_Object((1,3,6,1,2,1,41,1,2,3,1,25),_SdlcLSStatsRIMsIn_Type())
sdlcLSStatsRIMsIn.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSStatsRIMsIn.setStatus(_A)
_SdlcLSStatsRIMsOut_Type=Counter32
_SdlcLSStatsRIMsOut_Object=MibTableColumn
sdlcLSStatsRIMsOut=_SdlcLSStatsRIMsOut_Object((1,3,6,1,2,1,41,1,2,3,1,26),_SdlcLSStatsRIMsOut_Type())
sdlcLSStatsRIMsOut.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSStatsRIMsOut.setStatus(_A)
_SdlcLSStatsDISCIn_Type=Counter32
_SdlcLSStatsDISCIn_Object=MibTableColumn
sdlcLSStatsDISCIn=_SdlcLSStatsDISCIn_Object((1,3,6,1,2,1,41,1,2,3,1,27),_SdlcLSStatsDISCIn_Type())
sdlcLSStatsDISCIn.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSStatsDISCIn.setStatus(_A)
_SdlcLSStatsDISCOut_Type=Counter32
_SdlcLSStatsDISCOut_Object=MibTableColumn
sdlcLSStatsDISCOut=_SdlcLSStatsDISCOut_Object((1,3,6,1,2,1,41,1,2,3,1,28),_SdlcLSStatsDISCOut_Type())
sdlcLSStatsDISCOut.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSStatsDISCOut.setStatus(_A)
_SdlcLSStatsUAIn_Type=Counter32
_SdlcLSStatsUAIn_Object=MibTableColumn
sdlcLSStatsUAIn=_SdlcLSStatsUAIn_Object((1,3,6,1,2,1,41,1,2,3,1,29),_SdlcLSStatsUAIn_Type())
sdlcLSStatsUAIn.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSStatsUAIn.setStatus(_A)
_SdlcLSStatsUAOut_Type=Counter32
_SdlcLSStatsUAOut_Object=MibTableColumn
sdlcLSStatsUAOut=_SdlcLSStatsUAOut_Object((1,3,6,1,2,1,41,1,2,3,1,30),_SdlcLSStatsUAOut_Type())
sdlcLSStatsUAOut.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSStatsUAOut.setStatus(_A)
_SdlcLSStatsDMIn_Type=Counter32
_SdlcLSStatsDMIn_Object=MibTableColumn
sdlcLSStatsDMIn=_SdlcLSStatsDMIn_Object((1,3,6,1,2,1,41,1,2,3,1,31),_SdlcLSStatsDMIn_Type())
sdlcLSStatsDMIn.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSStatsDMIn.setStatus(_A)
_SdlcLSStatsDMOut_Type=Counter32
_SdlcLSStatsDMOut_Object=MibTableColumn
sdlcLSStatsDMOut=_SdlcLSStatsDMOut_Object((1,3,6,1,2,1,41,1,2,3,1,32),_SdlcLSStatsDMOut_Type())
sdlcLSStatsDMOut.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSStatsDMOut.setStatus(_A)
_SdlcLSStatsSNRMIn_Type=Counter32
_SdlcLSStatsSNRMIn_Object=MibTableColumn
sdlcLSStatsSNRMIn=_SdlcLSStatsSNRMIn_Object((1,3,6,1,2,1,41,1,2,3,1,33),_SdlcLSStatsSNRMIn_Type())
sdlcLSStatsSNRMIn.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSStatsSNRMIn.setStatus(_A)
_SdlcLSStatsSNRMOut_Type=Counter32
_SdlcLSStatsSNRMOut_Object=MibTableColumn
sdlcLSStatsSNRMOut=_SdlcLSStatsSNRMOut_Object((1,3,6,1,2,1,41,1,2,3,1,34),_SdlcLSStatsSNRMOut_Type())
sdlcLSStatsSNRMOut.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSStatsSNRMOut.setStatus(_A)
_SdlcLSStatsProtocolErrs_Type=Counter32
_SdlcLSStatsProtocolErrs_Object=MibTableColumn
sdlcLSStatsProtocolErrs=_SdlcLSStatsProtocolErrs_Object((1,3,6,1,2,1,41,1,2,3,1,35),_SdlcLSStatsProtocolErrs_Type())
sdlcLSStatsProtocolErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSStatsProtocolErrs.setStatus(_A)
_SdlcLSStatsActivityTOs_Type=Counter32
_SdlcLSStatsActivityTOs_Object=MibTableColumn
sdlcLSStatsActivityTOs=_SdlcLSStatsActivityTOs_Object((1,3,6,1,2,1,41,1,2,3,1,36),_SdlcLSStatsActivityTOs_Type())
sdlcLSStatsActivityTOs.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSStatsActivityTOs.setStatus(_A)
_SdlcLSStatsRNRLIMITs_Type=Counter32
_SdlcLSStatsRNRLIMITs_Object=MibTableColumn
sdlcLSStatsRNRLIMITs=_SdlcLSStatsRNRLIMITs_Object((1,3,6,1,2,1,41,1,2,3,1,37),_SdlcLSStatsRNRLIMITs_Type())
sdlcLSStatsRNRLIMITs.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSStatsRNRLIMITs.setStatus(_A)
_SdlcLSStatsRetriesExps_Type=Counter32
_SdlcLSStatsRetriesExps_Object=MibTableColumn
sdlcLSStatsRetriesExps=_SdlcLSStatsRetriesExps_Object((1,3,6,1,2,1,41,1,2,3,1,38),_SdlcLSStatsRetriesExps_Type())
sdlcLSStatsRetriesExps.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSStatsRetriesExps.setStatus(_A)
_SdlcLSStatsRetransmitsIn_Type=Counter32
_SdlcLSStatsRetransmitsIn_Object=MibTableColumn
sdlcLSStatsRetransmitsIn=_SdlcLSStatsRetransmitsIn_Object((1,3,6,1,2,1,41,1,2,3,1,39),_SdlcLSStatsRetransmitsIn_Type())
sdlcLSStatsRetransmitsIn.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSStatsRetransmitsIn.setStatus(_A)
_SdlcLSStatsRetransmitsOut_Type=Counter32
_SdlcLSStatsRetransmitsOut_Object=MibTableColumn
sdlcLSStatsRetransmitsOut=_SdlcLSStatsRetransmitsOut_Object((1,3,6,1,2,1,41,1,2,3,1,40),_SdlcLSStatsRetransmitsOut_Type())
sdlcLSStatsRetransmitsOut.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSStatsRetransmitsOut.setStatus(_A)
_SdlcTraps_ObjectIdentity=ObjectIdentity
sdlcTraps=_SdlcTraps_ObjectIdentity((1,3,6,1,2,1,41,1,3))
_SdlcConformance_ObjectIdentity=ObjectIdentity
sdlcConformance=_SdlcConformance_ObjectIdentity((1,3,6,1,2,1,41,1,4))
_SdlcCompliances_ObjectIdentity=ObjectIdentity
sdlcCompliances=_SdlcCompliances_ObjectIdentity((1,3,6,1,2,1,41,1,4,1))
_SdlcGroups_ObjectIdentity=ObjectIdentity
sdlcGroups=_SdlcGroups_ObjectIdentity((1,3,6,1,2,1,41,1,4,2))
_SdlcCoreGroups_ObjectIdentity=ObjectIdentity
sdlcCoreGroups=_SdlcCoreGroups_ObjectIdentity((1,3,6,1,2,1,41,1,4,2,1))
_SdlcPrimaryGroups_ObjectIdentity=ObjectIdentity
sdlcPrimaryGroups=_SdlcPrimaryGroups_ObjectIdentity((1,3,6,1,2,1,41,1,4,2,2))
sdlcCorePortAdminGroup=ObjectGroup((1,3,6,1,2,1,41,1,4,2,1,1))
sdlcCorePortAdminGroup.setObjects(*((_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:sdlcCorePortAdminGroup.setStatus(_A)
sdlcCorePortOperGroup=ObjectGroup((1,3,6,1,2,1,41,1,4,2,1,2))
sdlcCorePortOperGroup.setObjects(*((_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:sdlcCorePortOperGroup.setStatus(_A)
sdlcCorePortStatsGroup=ObjectGroup((1,3,6,1,2,1,41,1,4,2,1,3))
sdlcCorePortStatsGroup.setObjects(*((_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:sdlcCorePortStatsGroup.setStatus(_A)
sdlcCoreLSAdminGroup=ObjectGroup((1,3,6,1,2,1,41,1,4,2,1,4))
sdlcCoreLSAdminGroup.setObjects(*((_B,_J),(_B,_x),(_B,_U),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB)))
if mibBuilder.loadTexts:sdlcCoreLSAdminGroup.setStatus(_A)
sdlcCoreLSOperGroup=ObjectGroup((1,3,6,1,2,1,41,1,4,2,1,5))
sdlcCoreLSOperGroup.setObjects(*((_B,_AC),(_B,_V),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_AM),(_B,_AN)))
if mibBuilder.loadTexts:sdlcCoreLSOperGroup.setStatus(_A)
sdlcCoreLSStatsGroup=ObjectGroup((1,3,6,1,2,1,41,1,4,2,1,6))
sdlcCoreLSStatsGroup.setObjects(*((_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As)))
if mibBuilder.loadTexts:sdlcCoreLSStatsGroup.setStatus(_A)
sdlcPrimaryGroup=ObjectGroup((1,3,6,1,2,1,41,1,4,2,2,1))
sdlcPrimaryGroup.setObjects(*((_B,_At),(_B,_Au),(_B,_Av),(_B,_Aw)))
if mibBuilder.loadTexts:sdlcPrimaryGroup.setStatus(_A)
sdlcPrimaryMultipointGroup=ObjectGroup((1,3,6,1,2,1,41,1,4,2,2,2))
sdlcPrimaryMultipointGroup.setObjects(*((_B,_Ax),(_B,_Ay),(_B,_Az),(_B,_A_),(_B,_B0)))
if mibBuilder.loadTexts:sdlcPrimaryMultipointGroup.setStatus(_A)
sdlcPortStatusChange=NotificationType((1,3,6,1,2,1,41,1,3,1))
sdlcPortStatusChange.setObjects(*((_F,_G),(_F,_c),(_F,_d),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:sdlcPortStatusChange.setStatus(_A)
sdlcLSStatusChange=NotificationType((1,3,6,1,2,1,41,1,3,2))
sdlcLSStatusChange.setObjects(*((_F,_G),(_B,_J),(_B,_V),(_B,_U),(_B,_W),(_B,_X),(_B,_a),(_B,_Y),(_B,_Z),(_B,_b)))
if mibBuilder.loadTexts:sdlcLSStatusChange.setStatus(_A)
sdlcCoreCompliance=ModuleCompliance((1,3,6,1,2,1,41,1,4,1,1))
sdlcCoreCompliance.setObjects(*((_B,_B1),(_B,_B2),(_B,_B3),(_B,_B4),(_B,_B5),(_B,_B6)))
if mibBuilder.loadTexts:sdlcCoreCompliance.setStatus(_A)
sdlcPrimaryCompliance=ModuleCompliance((1,3,6,1,2,1,41,1,4,1,2))
sdlcPrimaryCompliance.setObjects((_B,_B7))
if mibBuilder.loadTexts:sdlcPrimaryCompliance.setStatus(_A)
sdlcPrimaryMultipointCompliance=ModuleCompliance((1,3,6,1,2,1,41,1,4,1,3))
sdlcPrimaryMultipointCompliance.setObjects((_B,_B8))
if mibBuilder.loadTexts:sdlcPrimaryMultipointCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'snaDLC':snaDLC,'sdlc':sdlc,'sdlcPortGroup':sdlcPortGroup,'sdlcPortAdminTable':sdlcPortAdminTable,'sdlcPortAdminEntry':sdlcPortAdminEntry,_j:sdlcPortAdminName,_k:sdlcPortAdminRole,_l:sdlcPortAdminType,_m:sdlcPortAdminTopology,_n:sdlcPortAdminISTATUS,'sdlcPortAdminACTIVTO':sdlcPortAdminACTIVTO,_At:sdlcPortAdminPAUSE,_Ax:sdlcPortAdminSERVLIM,_Ay:sdlcPortAdminSlowPollTimer,'sdlcPortOperTable':sdlcPortOperTable,'sdlcPortOperEntry':sdlcPortOperEntry,_o:sdlcPortOperName,_p:sdlcPortOperRole,_q:sdlcPortOperType,_r:sdlcPortOperTopology,_s:sdlcPortOperISTATUS,_t:sdlcPortOperACTIVTO,_Au:sdlcPortOperPAUSE,_Az:sdlcPortOperSlowPollMethod,_A_:sdlcPortOperSERVLIM,_B0:sdlcPortOperSlowPollTimer,'sdlcPortOperLastModifyTime':sdlcPortOperLastModifyTime,_S:sdlcPortOperLastFailTime,_T:sdlcPortOperLastFailCause,'sdlcPortStatsTable':sdlcPortStatsTable,'sdlcPortStatsEntry':sdlcPortStatsEntry,_u:sdlcPortStatsPhysicalFailures,_v:sdlcPortStatsInvalidAddresses,_w:sdlcPortStatsDwarfFrames,'sdlcPortStatsPollsIn':sdlcPortStatsPollsIn,'sdlcPortStatsPollsOut':sdlcPortStatsPollsOut,'sdlcPortStatsPollRspsIn':sdlcPortStatsPollRspsIn,'sdlcPortStatsPollRspsOut':sdlcPortStatsPollRspsOut,'sdlcPortStatsLocalBusies':sdlcPortStatsLocalBusies,'sdlcPortStatsRemoteBusies':sdlcPortStatsRemoteBusies,'sdlcPortStatsIFramesIn':sdlcPortStatsIFramesIn,'sdlcPortStatsIFramesOut':sdlcPortStatsIFramesOut,'sdlcPortStatsOctetsIn':sdlcPortStatsOctetsIn,'sdlcPortStatsOctetsOut':sdlcPortStatsOctetsOut,'sdlcPortStatsProtocolErrs':sdlcPortStatsProtocolErrs,'sdlcPortStatsActivityTOs':sdlcPortStatsActivityTOs,'sdlcPortStatsRNRLIMITs':sdlcPortStatsRNRLIMITs,'sdlcPortStatsRetriesExps':sdlcPortStatsRetriesExps,'sdlcPortStatsRetransmitsIn':sdlcPortStatsRetransmitsIn,'sdlcPortStatsRetransmitsOut':sdlcPortStatsRetransmitsOut,'sdlcLSGroup':sdlcLSGroup,'sdlcLSAdminTable':sdlcLSAdminTable,'sdlcLSAdminEntry':sdlcLSAdminEntry,_J:sdlcLSAddress,_x:sdlcLSAdminName,_U:sdlcLSAdminState,_y:sdlcLSAdminISTATUS,_z:sdlcLSAdminMAXDATASend,_A0:sdlcLSAdminMAXDATARcv,_Av:sdlcLSAdminREPLYTO,_A1:sdlcLSAdminMAXIN,_A2:sdlcLSAdminMAXOUT,_A3:sdlcLSAdminMODULO,_A4:sdlcLSAdminRETRIESm,_A5:sdlcLSAdminRETRIESt,_A6:sdlcLSAdminRETRIESn,_A7:sdlcLSAdminRNRLIMIT,_A8:sdlcLSAdminDATMODE,_A9:sdlcLSAdminGPoll,_AA:sdlcLSAdminSimRim,'sdlcLSAdminXmitRcvCap':sdlcLSAdminXmitRcvCap,_AB:sdlcLSAdminRowStatus,'sdlcLSOperTable':sdlcLSOperTable,'sdlcLSOperEntry':sdlcLSOperEntry,'sdlcLSOperName':sdlcLSOperName,_AC:sdlcLSOperRole,_V:sdlcLSOperState,_AD:sdlcLSOperMAXDATASend,_Aw:sdlcLSOperREPLYTO,_AE:sdlcLSOperMAXIN,_AF:sdlcLSOperMAXOUT,_AG:sdlcLSOperMODULO,_AH:sdlcLSOperRETRIESm,_AI:sdlcLSOperRETRIESt,_AJ:sdlcLSOperRETRIESn,_AK:sdlcLSOperRNRLIMIT,_AL:sdlcLSOperDATMODE,'sdlcLSOperLastModifyTime':sdlcLSOperLastModifyTime,_W:sdlcLSOperLastFailTime,_X:sdlcLSOperLastFailCause,_Y:sdlcLSOperLastFailCtrlIn,_Z:sdlcLSOperLastFailCtrlOut,_a:sdlcLSOperLastFailFRMRInfo,_b:sdlcLSOperLastFailREPLYTOs,_AM:sdlcLSOperEcho,_AN:sdlcLSOperGPoll,'sdlcLSOperSimRim':sdlcLSOperSimRim,'sdlcLSOperXmitRcvCap':sdlcLSOperXmitRcvCap,'sdlcLSStatsTable':sdlcLSStatsTable,'sdlcLSStatsEntry':sdlcLSStatsEntry,_AO:sdlcLSStatsBLUsIn,_AP:sdlcLSStatsBLUsOut,_AQ:sdlcLSStatsOctetsIn,_AR:sdlcLSStatsOctetsOut,_AS:sdlcLSStatsPollsIn,_AT:sdlcLSStatsPollsOut,_AV:sdlcLSStatsPollRspsOut,_AU:sdlcLSStatsPollRspsIn,_AW:sdlcLSStatsLocalBusies,_AX:sdlcLSStatsRemoteBusies,_AY:sdlcLSStatsIFramesIn,_AZ:sdlcLSStatsIFramesOut,_Ac:sdlcLSStatsUIFramesIn,_Ad:sdlcLSStatsUIFramesOut,_Ae:sdlcLSStatsXIDsIn,_Af:sdlcLSStatsXIDsOut,_Ag:sdlcLSStatsTESTsIn,_Ah:sdlcLSStatsTESTsOut,_Ai:sdlcLSStatsREJsIn,_Aj:sdlcLSStatsREJsOut,_Ak:sdlcLSStatsFRMRsIn,_Al:sdlcLSStatsFRMRsOut,_Am:sdlcLSStatsSIMsIn,_An:sdlcLSStatsSIMsOut,_Ao:sdlcLSStatsRIMsIn,_Ap:sdlcLSStatsRIMsOut,'sdlcLSStatsDISCIn':sdlcLSStatsDISCIn,'sdlcLSStatsDISCOut':sdlcLSStatsDISCOut,'sdlcLSStatsUAIn':sdlcLSStatsUAIn,'sdlcLSStatsUAOut':sdlcLSStatsUAOut,'sdlcLSStatsDMIn':sdlcLSStatsDMIn,'sdlcLSStatsDMOut':sdlcLSStatsDMOut,'sdlcLSStatsSNRMIn':sdlcLSStatsSNRMIn,'sdlcLSStatsSNRMOut':sdlcLSStatsSNRMOut,_Aq:sdlcLSStatsProtocolErrs,'sdlcLSStatsActivityTOs':sdlcLSStatsActivityTOs,_Ar:sdlcLSStatsRNRLIMITs,_As:sdlcLSStatsRetriesExps,_Aa:sdlcLSStatsRetransmitsIn,_Ab:sdlcLSStatsRetransmitsOut,'sdlcTraps':sdlcTraps,'sdlcPortStatusChange':sdlcPortStatusChange,'sdlcLSStatusChange':sdlcLSStatusChange,'sdlcConformance':sdlcConformance,'sdlcCompliances':sdlcCompliances,'sdlcCoreCompliance':sdlcCoreCompliance,'sdlcPrimaryCompliance':sdlcPrimaryCompliance,'sdlcPrimaryMultipointCompliance':sdlcPrimaryMultipointCompliance,'sdlcGroups':sdlcGroups,'sdlcCoreGroups':sdlcCoreGroups,_B1:sdlcCorePortAdminGroup,_B2:sdlcCorePortOperGroup,_B3:sdlcCorePortStatsGroup,_B4:sdlcCoreLSAdminGroup,_B5:sdlcCoreLSOperGroup,_B6:sdlcCoreLSStatsGroup,'sdlcPrimaryGroups':sdlcPrimaryGroups,_B7:sdlcPrimaryGroup,_B8:sdlcPrimaryMultipointGroup})