_B6='atextportZoneIndex'
_B5='atextportZonePort'
_B4='atextportIndex'
_B3='nbCacheIfIndex'
_B2='straceProbe'
_B1='straceHop'
_B0='straceDestAddr'
_A_='straceNMSAddr'
_Az='completed'
_Ay='not-started'
_Ax='spingDestAddr'
_Aw='spingNMSAddr'
_Av='sWorkGroupNumber'
_Au='strapEntryIndex'
_At='strapSeveritySeverity'
_As='strapIndex'
_Ar='slogIndex'
_Aq='igmpCacheIfIndex'
_Ap='igmpCacheAddress'
_Ao='igmpInterfaceIfIndex'
_An='ipMRouteInterfaceIfIndex'
_Am='ipMRouteSourceMask'
_Al='ipMRouteSource'
_Ak='ipMRouteGroup'
_Aj='strunkIfIndex'
_Ai='spvcIfIndex'
_Ah='ruleDestIpMask'
_Ag='ruleSourceIpMask'
_Af='ruleDestIp'
_Ae='ruleSourceIp'
_Ad='ruleIndex'
_Ac='profileDestEnd'
_Ab='profileDestStart'
_Aa='profileSourceEnd'
_AZ='profileSourceStart'
_AY='profileIndex'
_AX='sipNetToMediaNetAddress'
_AW='sipNetToMediaIfIndex'
_AV='sipcktIpAddress'
_AU='sipcktIndex'
_AT='sipmStatIfIndex'
_AS='sipmNeighbors'
_AR='sipmNeighborIfIndex'
_AQ='sipmRouteOriginMask'
_AP='sipmRouteOrigin'
_AO='srtrdiscIfIndex'
_AN='sipxsrPort'
_AM='sipxsfIndex'
_AL='sipxSapIndex'
_AK='sipxRouteDest'
_AJ='sipxIfIndex'
_AI='ethernet2'
_AH='ethernet8023'
_AG='sprotoIfIndex'
_AF='srepeaterPortPortID'
_AE='srepeaterPortGroupID'
_AD='srepeaterGroupID'
_AC='swanIndex'
_AB='lpbkIndex'
_AA='debugIndex'
_A9='rebootIndex'
_A8='filterIndex'
_A7='b45-megabits'
_A6='b2048-kilobits'
_A5='b1544-kilobits'
_A4='b56-kilobits'
_A3='b38400-baud'
_A2='b19200-baud'
_A1='b9600-baud'
_A0='b4800-baud'
_z='b2400-baud'
_y='b1200-baud'
_x='suartIndex'
_w='sfddiIndex'
_v='sifUtilSysPeakOrdinal'
_u='sifUtilSysPeakIndex'
_t='sifUtilPortPeakOrdinal'
_s='sifUtilPortPeakIndex'
_r='sifIndex'
_q='fddismtIndex'
_p='obsolete'
_o='supply-absent'
_n='supply-present'
_m='dc-bad'
_l='dc-good'
_k='ac-bad'
_j='ac-good'
_i='swIndex'
_h='hwIndex'
_g='critical'
_f='major'
_e='minor'
_d='warning'
_c='informational'
_b='feiom-iom'
_a='eiom8-iom'
_Z='ttpr-iom'
_Y='ifddi-iom'
_X='fddi-iom'
_W='tpr-iom'
_V='hssi-iom'
_U='csma-iom'
_T='turbo'
_S='packet-processing-engine'
_R='unknown'
_Q='vacant'
_P='valid'
_O='passBoth'
_N='stripRif'
_M='passRif'
_L='off'
_K='invalid'
_J='none'
_I='disabled'
_H='enabled'
_G='false'
_F='true'
_E='CTATX-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class Boolean(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_Sigma_ObjectIdentity=ObjectIdentity
sigma=_Sigma_ObjectIdentity((1,3,6,1,4,1,97))
_Sys_ObjectIdentity=ObjectIdentity
sys=_Sys_ObjectIdentity((1,3,6,1,4,1,97,1))
class _SysID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3)));namedValues=NamedValues(*(('es-1-bridge-router',1),('es-1-atx-br-router',3)))
_SysID_Type.__name__=_D
_SysID_Object=MibScalar
sysID=_SysID_Object((1,3,6,1,4,1,97,1,1),_SysID_Type())
sysID.setMaxAccess(_B)
if mibBuilder.loadTexts:sysID.setStatus(_A)
_SysReset_Type=TimeTicks
_SysReset_Object=MibScalar
sysReset=_SysReset_Object((1,3,6,1,4,1,97,1,2),_SysReset_Type())
sysReset.setMaxAccess(_C)
if mibBuilder.loadTexts:sysReset.setStatus(_A)
class _SysTrapAck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('traps-need-acks',1),('traps-not-acked',2)))
_SysTrapAck_Type.__name__=_D
_SysTrapAck_Object=MibScalar
sysTrapAck=_SysTrapAck_Object((1,3,6,1,4,1,97,1,3),_SysTrapAck_Type())
sysTrapAck.setMaxAccess(_C)
if mibBuilder.loadTexts:sysTrapAck.setStatus(_A)
_SysTrapTime_Type=TimeTicks
_SysTrapTime_Object=MibScalar
sysTrapTime=_SysTrapTime_Object((1,3,6,1,4,1,97,1,4),_SysTrapTime_Type())
sysTrapTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sysTrapTime.setStatus(_A)
_SysTrapRetry_Type=TimeTicks
_SysTrapRetry_Object=MibScalar
sysTrapRetry=_SysTrapRetry_Object((1,3,6,1,4,1,97,1,5),_SysTrapRetry_Type())
sysTrapRetry.setMaxAccess(_C)
if mibBuilder.loadTexts:sysTrapRetry.setStatus(_A)
_SysTrapPort_Type=Integer32
_SysTrapPort_Object=MibScalar
sysTrapPort=_SysTrapPort_Object((1,3,6,1,4,1,97,1,6),_SysTrapPort_Type())
sysTrapPort.setMaxAccess(_C)
if mibBuilder.loadTexts:sysTrapPort.setStatus(_A)
_Ecs_1_ObjectIdentity=ObjectIdentity
ecs_1=_Ecs_1_ObjectIdentity((1,3,6,1,4,1,97,3))
_Hw_ObjectIdentity=ObjectIdentity
hw=_Hw_ObjectIdentity((1,3,6,1,4,1,97,3,1))
_HwNumber_Type=Integer32
_HwNumber_Object=MibScalar
hwNumber=_HwNumber_Object((1,3,6,1,4,1,97,3,1,1),_HwNumber_Type())
hwNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNumber.setStatus(_A)
_HwSlotTable_Object=MibTable
hwSlotTable=_HwSlotTable_Object((1,3,6,1,4,1,97,3,1,2))
if mibBuilder.loadTexts:hwSlotTable.setStatus(_A)
_HwEntry_Object=MibTableRow
hwEntry=_HwEntry_Object((1,3,6,1,4,1,97,3,1,2,1))
hwEntry.setIndexNames((0,_E,_h))
if mibBuilder.loadTexts:hwEntry.setStatus(_A)
_HwIndex_Type=Integer32
_HwIndex_Object=MibTableColumn
hwIndex=_HwIndex_Object((1,3,6,1,4,1,97,3,1,2,1,1),_HwIndex_Type())
hwIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hwIndex.setStatus(_A)
class _HwType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_Q,1),(_R,2),(_S,3),(_T,4),(_U,5),(_V,6),(_W,7),(_X,8),(_Y,9),(_Z,10),(_a,11),(_b,12)))
_HwType_Type.__name__=_D
_HwType_Object=MibTableColumn
hwType=_HwType_Object((1,3,6,1,4,1,97,3,1,2,1,2),_HwType_Type())
hwType.setMaxAccess(_B)
if mibBuilder.loadTexts:hwType.setStatus(_A)
class _HwUseMod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('reset',1),('run-diagnostics',2),('run',3)))
_HwUseMod_Type.__name__=_D
_HwUseMod_Object=MibTableColumn
hwUseMod=_HwUseMod_Object((1,3,6,1,4,1,97,3,1,2,1,3),_HwUseMod_Type())
hwUseMod.setMaxAccess(_C)
if mibBuilder.loadTexts:hwUseMod.setStatus(_A)
class _HwDefType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_Q,1),(_R,2),(_S,3),(_T,4),(_U,5),(_V,6),(_W,7),(_X,8),(_Y,9),(_Z,10),(_a,11),(_b,12)))
_HwDefType_Type.__name__=_D
_HwDefType_Object=MibTableColumn
hwDefType=_HwDefType_Object((1,3,6,1,4,1,97,3,1,2,1,4),_HwDefType_Type())
hwDefType.setMaxAccess(_B)
if mibBuilder.loadTexts:hwDefType.setStatus(_A)
class _HwDiagStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('diag-failed',1),('diag-not-present',2),('diag-passed',3)))
_HwDiagStatus_Type.__name__=_D
_HwDiagStatus_Object=MibTableColumn
hwDiagStatus=_HwDiagStatus_Object((1,3,6,1,4,1,97,3,1,2,1,5),_HwDiagStatus_Type())
hwDiagStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwDiagStatus.setStatus(_A)
class _HwInuse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HwInuse_Type.__name__=_D
_HwInuse_Object=MibTableColumn
hwInuse=_HwInuse_Object((1,3,6,1,4,1,97,3,1,2,1,6),_HwInuse_Type())
hwInuse.setMaxAccess(_B)
if mibBuilder.loadTexts:hwInuse.setStatus(_A)
_HwDiagCode_Type=Integer32
_HwDiagCode_Object=MibTableColumn
hwDiagCode=_HwDiagCode_Object((1,3,6,1,4,1,97,3,1,2,1,7),_HwDiagCode_Type())
hwDiagCode.setMaxAccess(_B)
if mibBuilder.loadTexts:hwDiagCode.setStatus(_A)
_HwManufData_Type=OctetString
_HwManufData_Object=MibTableColumn
hwManufData=_HwManufData_Object((1,3,6,1,4,1,97,3,1,2,1,8),_HwManufData_Type())
hwManufData.setMaxAccess(_B)
if mibBuilder.loadTexts:hwManufData.setStatus(_A)
_HwPortType_Type=OctetString
_HwPortType_Object=MibTableColumn
hwPortType=_HwPortType_Object((1,3,6,1,4,1,97,3,1,2,1,9),_HwPortType_Type())
hwPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:hwPortType.setStatus(_A)
_HwPortStatus_Type=OctetString
_HwPortStatus_Object=MibTableColumn
hwPortStatus=_HwPortStatus_Object((1,3,6,1,4,1,97,3,1,2,1,10),_HwPortStatus_Type())
hwPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwPortStatus.setStatus(_A)
_HwUsePort_Type=OctetString
_HwUsePort_Object=MibTableColumn
hwUsePort=_HwUsePort_Object((1,3,6,1,4,1,97,3,1,2,1,11),_HwUsePort_Type())
hwUsePort.setMaxAccess(_C)
if mibBuilder.loadTexts:hwUsePort.setStatus(_A)
_HwDefPortType_Type=OctetString
_HwDefPortType_Object=MibTableColumn
hwDefPortType=_HwDefPortType_Object((1,3,6,1,4,1,97,3,1,2,1,12),_HwDefPortType_Type())
hwDefPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:hwDefPortType.setStatus(_A)
_HwAddr1_Type=OctetString
_HwAddr1_Object=MibTableColumn
hwAddr1=_HwAddr1_Object((1,3,6,1,4,1,97,3,1,2,1,13),_HwAddr1_Type())
hwAddr1.setMaxAccess(_B)
if mibBuilder.loadTexts:hwAddr1.setStatus(_A)
_HwAddr2_Type=OctetString
_HwAddr2_Object=MibTableColumn
hwAddr2=_HwAddr2_Object((1,3,6,1,4,1,97,3,1,2,1,14),_HwAddr2_Type())
hwAddr2.setMaxAccess(_B)
if mibBuilder.loadTexts:hwAddr2.setStatus(_A)
_HwAddr3_Type=OctetString
_HwAddr3_Object=MibTableColumn
hwAddr3=_HwAddr3_Object((1,3,6,1,4,1,97,3,1,2,1,15),_HwAddr3_Type())
hwAddr3.setMaxAccess(_B)
if mibBuilder.loadTexts:hwAddr3.setStatus(_A)
_HwAddr4_Type=OctetString
_HwAddr4_Object=MibTableColumn
hwAddr4=_HwAddr4_Object((1,3,6,1,4,1,97,3,1,2,1,16),_HwAddr4_Type())
hwAddr4.setMaxAccess(_B)
if mibBuilder.loadTexts:hwAddr4.setStatus(_A)
class _HwTempOK_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('temperature-normal',1),('temperature-too-hot',2)))
_HwTempOK_Type.__name__=_D
_HwTempOK_Object=MibTableColumn
hwTempOK=_HwTempOK_Object((1,3,6,1,4,1,97,3,1,2,1,17),_HwTempOK_Type())
hwTempOK.setMaxAccess(_B)
if mibBuilder.loadTexts:hwTempOK.setStatus(_A)
_HwFirstPort_Type=Integer32
_HwFirstPort_Object=MibTableColumn
hwFirstPort=_HwFirstPort_Object((1,3,6,1,4,1,97,3,1,2,1,18),_HwFirstPort_Type())
hwFirstPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hwFirstPort.setStatus(_A)
_HwFatalErr_Type=OctetString
_HwFatalErr_Object=MibTableColumn
hwFatalErr=_HwFatalErr_Object((1,3,6,1,4,1,97,3,1,2,1,19),_HwFatalErr_Type())
hwFatalErr.setMaxAccess(_B)
if mibBuilder.loadTexts:hwFatalErr.setStatus(_A)
_HwRptrPorts_Type=OctetString
_HwRptrPorts_Object=MibTableColumn
hwRptrPorts=_HwRptrPorts_Object((1,3,6,1,4,1,97,3,1,2,1,20),_HwRptrPorts_Type())
hwRptrPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:hwRptrPorts.setStatus(_A)
_HwPortSubType_Type=OctetString
_HwPortSubType_Object=MibTableColumn
hwPortSubType=_HwPortSubType_Object((1,3,6,1,4,1,97,3,1,2,1,21),_HwPortSubType_Type())
hwPortSubType.setMaxAccess(_B)
if mibBuilder.loadTexts:hwPortSubType.setStatus(_A)
_HwAddr5_Type=OctetString
_HwAddr5_Object=MibTableColumn
hwAddr5=_HwAddr5_Object((1,3,6,1,4,1,97,3,1,2,1,22),_HwAddr5_Type())
hwAddr5.setMaxAccess(_B)
if mibBuilder.loadTexts:hwAddr5.setStatus(_A)
_HwAddr6_Type=OctetString
_HwAddr6_Object=MibTableColumn
hwAddr6=_HwAddr6_Object((1,3,6,1,4,1,97,3,1,2,1,23),_HwAddr6_Type())
hwAddr6.setMaxAccess(_B)
if mibBuilder.loadTexts:hwAddr6.setStatus(_A)
_HwAddr7_Type=OctetString
_HwAddr7_Object=MibTableColumn
hwAddr7=_HwAddr7_Object((1,3,6,1,4,1,97,3,1,2,1,24),_HwAddr7_Type())
hwAddr7.setMaxAccess(_B)
if mibBuilder.loadTexts:hwAddr7.setStatus(_A)
_HwAddr8_Type=OctetString
_HwAddr8_Object=MibTableColumn
hwAddr8=_HwAddr8_Object((1,3,6,1,4,1,97,3,1,2,1,25),_HwAddr8_Type())
hwAddr8.setMaxAccess(_B)
if mibBuilder.loadTexts:hwAddr8.setStatus(_A)
class _HwSysBus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bus-800-mbit',1),('bus-1p6-gbit',2)))
_HwSysBus_Type.__name__=_D
_HwSysBus_Object=MibScalar
hwSysBus=_HwSysBus_Object((1,3,6,1,4,1,97,3,1,3),_HwSysBus_Type())
hwSysBus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwSysBus.setStatus(_A)
class _HwPpeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ppe2',1),('ppe3',2)))
_HwPpeType_Type.__name__=_D
_HwPpeType_Object=MibScalar
hwPpeType=_HwPpeType_Object((1,3,6,1,4,1,97,3,1,4),_HwPpeType_Type())
hwPpeType.setMaxAccess(_B)
if mibBuilder.loadTexts:hwPpeType.setStatus(_A)
class _HwSysProcessor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dual-29000',1),('dual-29030',2)))
_HwSysProcessor_Type.__name__=_D
_HwSysProcessor_Object=MibScalar
hwSysProcessor=_HwSysProcessor_Object((1,3,6,1,4,1,97,3,1,5),_HwSysProcessor_Type())
hwSysProcessor.setMaxAccess(_B)
if mibBuilder.loadTexts:hwSysProcessor.setStatus(_A)
_Sw_ObjectIdentity=ObjectIdentity
sw=_Sw_ObjectIdentity((1,3,6,1,4,1,97,3,2))
_SwNumber_Type=Integer32
_SwNumber_Object=MibScalar
swNumber=_SwNumber_Object((1,3,6,1,4,1,97,3,2,1),_SwNumber_Type())
swNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:swNumber.setStatus(_A)
_SwFilesetTable_Object=MibTable
swFilesetTable=_SwFilesetTable_Object((1,3,6,1,4,1,97,3,2,2))
if mibBuilder.loadTexts:swFilesetTable.setStatus(_A)
_SwFileset_Object=MibTableRow
swFileset=_SwFileset_Object((1,3,6,1,4,1,97,3,2,2,1))
swFileset.setIndexNames((0,_E,_i))
if mibBuilder.loadTexts:swFileset.setStatus(_A)
class _SwIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('currently-executing',1),('next-boot',2)))
_SwIndex_Type.__name__=_D
_SwIndex_Object=MibTableColumn
swIndex=_SwIndex_Object((1,3,6,1,4,1,97,3,2,2,1,1),_SwIndex_Type())
swIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:swIndex.setStatus(_A)
_SwDesc_Type=DisplayString
_SwDesc_Object=MibTableColumn
swDesc=_SwDesc_Object((1,3,6,1,4,1,97,3,2,2,1,3),_SwDesc_Type())
swDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:swDesc.setStatus(_A)
_SwCount_Type=Integer32
_SwCount_Object=MibTableColumn
swCount=_SwCount_Object((1,3,6,1,4,1,97,3,2,2,1,4),_SwCount_Type())
swCount.setMaxAccess(_B)
if mibBuilder.loadTexts:swCount.setStatus(_A)
_SwTypes_Type=OctetString
_SwTypes_Object=MibTableColumn
swTypes=_SwTypes_Object((1,3,6,1,4,1,97,3,2,2,1,5),_SwTypes_Type())
swTypes.setMaxAccess(_B)
if mibBuilder.loadTexts:swTypes.setStatus(_A)
_SwSizes_Type=OctetString
_SwSizes_Object=MibTableColumn
swSizes=_SwSizes_Object((1,3,6,1,4,1,97,3,2,2,1,6),_SwSizes_Type())
swSizes.setMaxAccess(_B)
if mibBuilder.loadTexts:swSizes.setStatus(_A)
_SwStarts_Type=OctetString
_SwStarts_Object=MibTableColumn
swStarts=_SwStarts_Object((1,3,6,1,4,1,97,3,2,2,1,7),_SwStarts_Type())
swStarts.setMaxAccess(_B)
if mibBuilder.loadTexts:swStarts.setStatus(_A)
_SwBases_Type=OctetString
_SwBases_Object=MibTableColumn
swBases=_SwBases_Object((1,3,6,1,4,1,97,3,2,2,1,8),_SwBases_Type())
swBases.setMaxAccess(_B)
if mibBuilder.loadTexts:swBases.setStatus(_A)
class _SwFlashBank_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('first-bank',1),('second-bank',2)))
_SwFlashBank_Type.__name__=_D
_SwFlashBank_Object=MibTableColumn
swFlashBank=_SwFlashBank_Object((1,3,6,1,4,1,97,3,2,2,1,9),_SwFlashBank_Type())
swFlashBank.setMaxAccess(_B)
if mibBuilder.loadTexts:swFlashBank.setStatus(_A)
_Admin_ObjectIdentity=ObjectIdentity
admin=_Admin_ObjectIdentity((1,3,6,1,4,1,97,3,3))
_Config_ObjectIdentity=ObjectIdentity
config=_Config_ObjectIdentity((1,3,6,1,4,1,97,3,3,1))
_ConfigFatalErr_Type=OctetString
_ConfigFatalErr_Object=MibScalar
configFatalErr=_ConfigFatalErr_Object((1,3,6,1,4,1,97,3,3,1,1),_ConfigFatalErr_Type())
configFatalErr.setMaxAccess(_B)
if mibBuilder.loadTexts:configFatalErr.setStatus(_A)
_ConfigAnyPass_Type=OctetString
_ConfigAnyPass_Object=MibScalar
configAnyPass=_ConfigAnyPass_Object((1,3,6,1,4,1,97,3,3,1,2),_ConfigAnyPass_Type())
configAnyPass.setMaxAccess(_C)
if mibBuilder.loadTexts:configAnyPass.setStatus(_A)
_ConfigGetPass_Type=OctetString
_ConfigGetPass_Object=MibScalar
configGetPass=_ConfigGetPass_Object((1,3,6,1,4,1,97,3,3,1,3),_ConfigGetPass_Type())
configGetPass.setMaxAccess(_C)
if mibBuilder.loadTexts:configGetPass.setStatus(_A)
_ConfigNMSAddress_Type=IpAddress
_ConfigNMSAddress_Object=MibScalar
configNMSAddress=_ConfigNMSAddress_Object((1,3,6,1,4,1,97,3,3,1,4),_ConfigNMSAddress_Type())
configNMSAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:configNMSAddress.setStatus(_A)
_ConfigFunctions_Type=Integer32
_ConfigFunctions_Object=MibScalar
configFunctions=_ConfigFunctions_Object((1,3,6,1,4,1,97,3,3,1,5),_ConfigFunctions_Type())
configFunctions.setMaxAccess(_B)
if mibBuilder.loadTexts:configFunctions.setStatus(_A)
class _ConfigPowerAc1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_j,1),(_k,2)))
_ConfigPowerAc1_Type.__name__=_D
_ConfigPowerAc1_Object=MibScalar
configPowerAc1=_ConfigPowerAc1_Object((1,3,6,1,4,1,97,3,3,1,6),_ConfigPowerAc1_Type())
configPowerAc1.setMaxAccess(_B)
if mibBuilder.loadTexts:configPowerAc1.setStatus(_A)
class _ConfigPowerAc2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_j,1),(_k,2)))
_ConfigPowerAc2_Type.__name__=_D
_ConfigPowerAc2_Object=MibScalar
configPowerAc2=_ConfigPowerAc2_Object((1,3,6,1,4,1,97,3,3,1,7),_ConfigPowerAc2_Type())
configPowerAc2.setMaxAccess(_B)
if mibBuilder.loadTexts:configPowerAc2.setStatus(_A)
class _ConfigPowerDc1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_l,1),(_m,2)))
_ConfigPowerDc1_Type.__name__=_D
_ConfigPowerDc1_Object=MibScalar
configPowerDc1=_ConfigPowerDc1_Object((1,3,6,1,4,1,97,3,3,1,8),_ConfigPowerDc1_Type())
configPowerDc1.setMaxAccess(_B)
if mibBuilder.loadTexts:configPowerDc1.setStatus(_A)
class _ConfigPowerDc2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_l,1),(_m,2)))
_ConfigPowerDc2_Type.__name__=_D
_ConfigPowerDc2_Object=MibScalar
configPowerDc2=_ConfigPowerDc2_Object((1,3,6,1,4,1,97,3,3,1,9),_ConfigPowerDc2_Type())
configPowerDc2.setMaxAccess(_B)
if mibBuilder.loadTexts:configPowerDc2.setStatus(_A)
class _ConfigPowerPresent1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_n,1),(_o,2)))
_ConfigPowerPresent1_Type.__name__=_D
_ConfigPowerPresent1_Object=MibScalar
configPowerPresent1=_ConfigPowerPresent1_Object((1,3,6,1,4,1,97,3,3,1,10),_ConfigPowerPresent1_Type())
configPowerPresent1.setMaxAccess(_B)
if mibBuilder.loadTexts:configPowerPresent1.setStatus(_A)
class _ConfigPowerPresent2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_n,1),(_o,2)))
_ConfigPowerPresent2_Type.__name__=_D
_ConfigPowerPresent2_Object=MibScalar
configPowerPresent2=_ConfigPowerPresent2_Object((1,3,6,1,4,1,97,3,3,1,11),_ConfigPowerPresent2_Type())
configPowerPresent2.setMaxAccess(_B)
if mibBuilder.loadTexts:configPowerPresent2.setStatus(_A)
class _ConfigAlarmDynamic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_ConfigAlarmDynamic_Type.__name__=_D
_ConfigAlarmDynamic_Object=MibScalar
configAlarmDynamic=_ConfigAlarmDynamic_Object((1,3,6,1,4,1,97,3,3,1,12),_ConfigAlarmDynamic_Type())
configAlarmDynamic.setMaxAccess(_C)
if mibBuilder.loadTexts:configAlarmDynamic.setStatus(_A)
class _ConfigAlarmAddresses_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_ConfigAlarmAddresses_Type.__name__=_D
_ConfigAlarmAddresses_Object=MibScalar
configAlarmAddresses=_ConfigAlarmAddresses_Object((1,3,6,1,4,1,97,3,3,1,13),_ConfigAlarmAddresses_Type())
configAlarmAddresses.setMaxAccess(_C)
if mibBuilder.loadTexts:configAlarmAddresses.setStatus(_A)
class _ConfigStorageFailure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_ConfigStorageFailure_Type.__name__=_D
_ConfigStorageFailure_Object=MibScalar
configStorageFailure=_ConfigStorageFailure_Object((1,3,6,1,4,1,97,3,3,1,14),_ConfigStorageFailure_Type())
configStorageFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:configStorageFailure.setStatus(_A)
_ConfigAuthenticationFailure_Type=IpAddress
_ConfigAuthenticationFailure_Object=MibScalar
configAuthenticationFailure=_ConfigAuthenticationFailure_Object((1,3,6,1,4,1,97,3,3,1,15),_ConfigAuthenticationFailure_Type())
configAuthenticationFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:configAuthenticationFailure.setStatus(_A)
_ConfigFddiPriority_Type=Integer32
_ConfigFddiPriority_Object=MibScalar
configFddiPriority=_ConfigFddiPriority_Object((1,3,6,1,4,1,97,3,3,1,16),_ConfigFddiPriority_Type())
configFddiPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:configFddiPriority.setStatus(_A)
_ConfigTprPriority_Type=Integer32
_ConfigTprPriority_Object=MibScalar
configTprPriority=_ConfigTprPriority_Object((1,3,6,1,4,1,97,3,3,1,17),_ConfigTprPriority_Type())
configTprPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:configTprPriority.setStatus(_A)
_ConfigDumpModule_Type=Integer32
_ConfigDumpModule_Object=MibScalar
configDumpModule=_ConfigDumpModule_Object((1,3,6,1,4,1,97,3,3,1,19),_ConfigDumpModule_Type())
configDumpModule.setMaxAccess(_C)
if mibBuilder.loadTexts:configDumpModule.setStatus(_A)
_ConfigDumpStart_Type=Integer32
_ConfigDumpStart_Object=MibScalar
configDumpStart=_ConfigDumpStart_Object((1,3,6,1,4,1,97,3,3,1,20),_ConfigDumpStart_Type())
configDumpStart.setMaxAccess(_C)
if mibBuilder.loadTexts:configDumpStart.setStatus(_A)
_ConfigDumpEnd_Type=Integer32
_ConfigDumpEnd_Object=MibScalar
configDumpEnd=_ConfigDumpEnd_Object((1,3,6,1,4,1,97,3,3,1,21),_ConfigDumpEnd_Type())
configDumpEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:configDumpEnd.setStatus(_A)
_Lma_ObjectIdentity=ObjectIdentity
lma=_Lma_ObjectIdentity((1,3,6,1,4,1,97,3,3,2))
_LmaAllAddr_Type=OctetString
_LmaAllAddr_Object=MibScalar
lmaAllAddr=_LmaAllAddr_Object((1,3,6,1,4,1,97,3,3,2,1),_LmaAllAddr_Type())
lmaAllAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:lmaAllAddr.setStatus(_A)
_LmaAnyAddr_Type=OctetString
_LmaAnyAddr_Object=MibScalar
lmaAnyAddr=_LmaAnyAddr_Object((1,3,6,1,4,1,97,3,3,2,2),_LmaAnyAddr_Type())
lmaAnyAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:lmaAnyAddr.setStatus(_A)
_Ppe_ObjectIdentity=ObjectIdentity
ppe=_Ppe_ObjectIdentity((1,3,6,1,4,1,97,3,3,3))
_PpeLrgUxRxCnt_Type=Integer32
_PpeLrgUxRxCnt_Object=MibScalar
ppeLrgUxRxCnt=_PpeLrgUxRxCnt_Object((1,3,6,1,4,1,97,3,3,3,1),_PpeLrgUxRxCnt_Type())
ppeLrgUxRxCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:ppeLrgUxRxCnt.setStatus(_A)
_PpeSmlUxRxCnt_Type=Integer32
_PpeSmlUxRxCnt_Object=MibScalar
ppeSmlUxRxCnt=_PpeSmlUxRxCnt_Object((1,3,6,1,4,1,97,3,3,3,2),_PpeSmlUxRxCnt_Type())
ppeSmlUxRxCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:ppeSmlUxRxCnt.setStatus(_A)
_PpeUxTxCnt_Type=Integer32
_PpeUxTxCnt_Object=MibScalar
ppeUxTxCnt=_PpeUxTxCnt_Object((1,3,6,1,4,1,97,3,3,3,3),_PpeUxTxCnt_Type())
ppeUxTxCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:ppeUxTxCnt.setStatus(_A)
_PpeSmlBuffSize_Type=Integer32
_PpeSmlBuffSize_Object=MibScalar
ppeSmlBuffSize=_PpeSmlBuffSize_Object((1,3,6,1,4,1,97,3,3,3,4),_PpeSmlBuffSize_Type())
ppeSmlBuffSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ppeSmlBuffSize.setStatus(_A)
_PpeBridgingMemory_Type=Integer32
_PpeBridgingMemory_Object=MibScalar
ppeBridgingMemory=_PpeBridgingMemory_Object((1,3,6,1,4,1,97,3,3,3,5),_PpeBridgingMemory_Type())
ppeBridgingMemory.setMaxAccess(_B)
if mibBuilder.loadTexts:ppeBridgingMemory.setStatus(_A)
class _PpeExtendStats_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PpeExtendStats_Type.__name__=_D
_PpeExtendStats_Object=MibScalar
ppeExtendStats=_PpeExtendStats_Object((1,3,6,1,4,1,97,3,3,3,6),_PpeExtendStats_Type())
ppeExtendStats.setMaxAccess(_C)
if mibBuilder.loadTexts:ppeExtendStats.setStatus(_A)
_PpeBAddrLimit_Type=Integer32
_PpeBAddrLimit_Object=MibScalar
ppeBAddrLimit=_PpeBAddrLimit_Object((1,3,6,1,4,1,97,3,3,3,7),_PpeBAddrLimit_Type())
ppeBAddrLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:ppeBAddrLimit.setStatus(_A)
_PpeTxCongests_Type=Counter32
_PpeTxCongests_Object=MibScalar
ppeTxCongests=_PpeTxCongests_Object((1,3,6,1,4,1,97,3,3,3,8),_PpeTxCongests_Type())
ppeTxCongests.setMaxAccess(_B)
if mibBuilder.loadTexts:ppeTxCongests.setStatus(_A)
_PpeArpEntries_Type=Counter32
_PpeArpEntries_Object=MibScalar
ppeArpEntries=_PpeArpEntries_Object((1,3,6,1,4,1,97,3,3,3,9),_PpeArpEntries_Type())
ppeArpEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:ppeArpEntries.setStatus(_A)
_PpeArpStatics_Type=Counter32
_PpeArpStatics_Object=MibScalar
ppeArpStatics=_PpeArpStatics_Object((1,3,6,1,4,1,97,3,3,3,10),_PpeArpStatics_Type())
ppeArpStatics.setMaxAccess(_B)
if mibBuilder.loadTexts:ppeArpStatics.setStatus(_A)
_PpeArpOverflows_Type=Counter32
_PpeArpOverflows_Object=MibScalar
ppeArpOverflows=_PpeArpOverflows_Object((1,3,6,1,4,1,97,3,3,3,11),_PpeArpOverflows_Type())
ppeArpOverflows.setMaxAccess(_B)
if mibBuilder.loadTexts:ppeArpOverflows.setStatus(_A)
_PpeIpEntries_Type=Counter32
_PpeIpEntries_Object=MibScalar
ppeIpEntries=_PpeIpEntries_Object((1,3,6,1,4,1,97,3,3,3,12),_PpeIpEntries_Type())
ppeIpEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:ppeIpEntries.setStatus(_A)
_PpeIpStatics_Type=Counter32
_PpeIpStatics_Object=MibScalar
ppeIpStatics=_PpeIpStatics_Object((1,3,6,1,4,1,97,3,3,3,13),_PpeIpStatics_Type())
ppeIpStatics.setMaxAccess(_B)
if mibBuilder.loadTexts:ppeIpStatics.setStatus(_A)
_PpeStaticPreference_Type=Integer32
_PpeStaticPreference_Object=MibScalar
ppeStaticPreference=_PpeStaticPreference_Object((1,3,6,1,4,1,97,3,3,3,14),_PpeStaticPreference_Type())
ppeStaticPreference.setMaxAccess(_C)
if mibBuilder.loadTexts:ppeStaticPreference.setStatus(_A)
_PpeOspfPreference_Type=Integer32
_PpeOspfPreference_Object=MibScalar
ppeOspfPreference=_PpeOspfPreference_Object((1,3,6,1,4,1,97,3,3,3,15),_PpeOspfPreference_Type())
ppeOspfPreference.setMaxAccess(_C)
if mibBuilder.loadTexts:ppeOspfPreference.setStatus(_A)
_PpeRipPreference_Type=Integer32
_PpeRipPreference_Object=MibScalar
ppeRipPreference=_PpeRipPreference_Object((1,3,6,1,4,1,97,3,3,3,16),_PpeRipPreference_Type())
ppeRipPreference.setMaxAccess(_C)
if mibBuilder.loadTexts:ppeRipPreference.setStatus(_A)
_PpeEgpPreference_Type=Integer32
_PpeEgpPreference_Object=MibScalar
ppeEgpPreference=_PpeEgpPreference_Object((1,3,6,1,4,1,97,3,3,3,17),_PpeEgpPreference_Type())
ppeEgpPreference.setMaxAccess(_C)
if mibBuilder.loadTexts:ppeEgpPreference.setStatus(_A)
class _PpeCpuUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('low-cpu',1),('medium-cpu',2),('high-cpu',3)))
_PpeCpuUtilization_Type.__name__=_D
_PpeCpuUtilization_Object=MibScalar
ppeCpuUtilization=_PpeCpuUtilization_Object((1,3,6,1,4,1,97,3,3,3,18),_PpeCpuUtilization_Type())
ppeCpuUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:ppeCpuUtilization.setStatus(_A)
_PpeRipRouteDiscards_Type=Counter32
_PpeRipRouteDiscards_Object=MibScalar
ppeRipRouteDiscards=_PpeRipRouteDiscards_Object((1,3,6,1,4,1,97,3,3,3,19),_PpeRipRouteDiscards_Type())
ppeRipRouteDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:ppeRipRouteDiscards.setStatus(_A)
_PpeOspfRouteDiscards_Type=Counter32
_PpeOspfRouteDiscards_Object=MibScalar
ppeOspfRouteDiscards=_PpeOspfRouteDiscards_Object((1,3,6,1,4,1,97,3,3,3,20),_PpeOspfRouteDiscards_Type())
ppeOspfRouteDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:ppeOspfRouteDiscards.setStatus(_A)
_PpeRouteMemorySize_Type=Counter32
_PpeRouteMemorySize_Object=MibScalar
ppeRouteMemorySize=_PpeRouteMemorySize_Object((1,3,6,1,4,1,97,3,3,3,21),_PpeRouteMemorySize_Type())
ppeRouteMemorySize.setMaxAccess(_B)
if mibBuilder.loadTexts:ppeRouteMemorySize.setStatus(_A)
_PpeRouteMemoryAvail_Type=Counter32
_PpeRouteMemoryAvail_Object=MibScalar
ppeRouteMemoryAvail=_PpeRouteMemoryAvail_Object((1,3,6,1,4,1,97,3,3,3,22),_PpeRouteMemoryAvail_Type())
ppeRouteMemoryAvail.setMaxAccess(_B)
if mibBuilder.loadTexts:ppeRouteMemoryAvail.setStatus(_A)
_PpeRouteMemoryFailures_Type=Counter32
_PpeRouteMemoryFailures_Object=MibScalar
ppeRouteMemoryFailures=_PpeRouteMemoryFailures_Object((1,3,6,1,4,1,97,3,3,3,23),_PpeRouteMemoryFailures_Type())
ppeRouteMemoryFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:ppeRouteMemoryFailures.setStatus(_A)
_PpePacketMemorySize_Type=Counter32
_PpePacketMemorySize_Object=MibScalar
ppePacketMemorySize=_PpePacketMemorySize_Object((1,3,6,1,4,1,97,3,3,3,24),_PpePacketMemorySize_Type())
ppePacketMemorySize.setMaxAccess(_B)
if mibBuilder.loadTexts:ppePacketMemorySize.setStatus(_A)
_PpePacketMemoryAvail_Type=Counter32
_PpePacketMemoryAvail_Object=MibScalar
ppePacketMemoryAvail=_PpePacketMemoryAvail_Object((1,3,6,1,4,1,97,3,3,3,25),_PpePacketMemoryAvail_Type())
ppePacketMemoryAvail.setMaxAccess(_B)
if mibBuilder.loadTexts:ppePacketMemoryAvail.setStatus(_A)
_PpePacketMemoryFailures_Type=Counter32
_PpePacketMemoryFailures_Object=MibScalar
ppePacketMemoryFailures=_PpePacketMemoryFailures_Object((1,3,6,1,4,1,97,3,3,3,26),_PpePacketMemoryFailures_Type())
ppePacketMemoryFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:ppePacketMemoryFailures.setStatus(_A)
_PpeOspfPduMemoryFailures_Type=Counter32
_PpeOspfPduMemoryFailures_Object=MibScalar
ppeOspfPduMemoryFailures=_PpeOspfPduMemoryFailures_Object((1,3,6,1,4,1,97,3,3,3,27),_PpeOspfPduMemoryFailures_Type())
ppeOspfPduMemoryFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:ppeOspfPduMemoryFailures.setStatus(_A)
_PpeOspfPduMemoryAllocs_Type=Counter32
_PpeOspfPduMemoryAllocs_Object=MibScalar
ppeOspfPduMemoryAllocs=_PpeOspfPduMemoryAllocs_Object((1,3,6,1,4,1,97,3,3,3,28),_PpeOspfPduMemoryAllocs_Type())
ppeOspfPduMemoryAllocs.setMaxAccess(_B)
if mibBuilder.loadTexts:ppeOspfPduMemoryAllocs.setStatus(_A)
_PpeIcmpPduMemoryFailures_Type=Counter32
_PpeIcmpPduMemoryFailures_Object=MibScalar
ppeIcmpPduMemoryFailures=_PpeIcmpPduMemoryFailures_Object((1,3,6,1,4,1,97,3,3,3,29),_PpeIcmpPduMemoryFailures_Type())
ppeIcmpPduMemoryFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:ppeIcmpPduMemoryFailures.setStatus(_A)
_PpeIcmpPduMemoryAllocs_Type=Counter32
_PpeIcmpPduMemoryAllocs_Object=MibScalar
ppeIcmpPduMemoryAllocs=_PpeIcmpPduMemoryAllocs_Object((1,3,6,1,4,1,97,3,3,3,30),_PpeIcmpPduMemoryAllocs_Type())
ppeIcmpPduMemoryAllocs.setMaxAccess(_B)
if mibBuilder.loadTexts:ppeIcmpPduMemoryAllocs.setStatus(_A)
_PpeRipPduMemoryFailures_Type=Counter32
_PpeRipPduMemoryFailures_Object=MibScalar
ppeRipPduMemoryFailures=_PpeRipPduMemoryFailures_Object((1,3,6,1,4,1,97,3,3,3,31),_PpeRipPduMemoryFailures_Type())
ppeRipPduMemoryFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:ppeRipPduMemoryFailures.setStatus(_A)
_PpeRipPduMemoryAllocs_Type=Counter32
_PpeRipPduMemoryAllocs_Object=MibScalar
ppeRipPduMemoryAllocs=_PpeRipPduMemoryAllocs_Object((1,3,6,1,4,1,97,3,3,3,32),_PpeRipPduMemoryAllocs_Type())
ppeRipPduMemoryAllocs.setMaxAccess(_B)
if mibBuilder.loadTexts:ppeRipPduMemoryAllocs.setStatus(_A)
_PpeBootpPduMemoryFailures_Type=Counter32
_PpeBootpPduMemoryFailures_Object=MibScalar
ppeBootpPduMemoryFailures=_PpeBootpPduMemoryFailures_Object((1,3,6,1,4,1,97,3,3,3,33),_PpeBootpPduMemoryFailures_Type())
ppeBootpPduMemoryFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:ppeBootpPduMemoryFailures.setStatus(_A)
_PpeBootpPduMemoryAllocs_Type=Counter32
_PpeBootpPduMemoryAllocs_Object=MibScalar
ppeBootpPduMemoryAllocs=_PpeBootpPduMemoryAllocs_Object((1,3,6,1,4,1,97,3,3,3,34),_PpeBootpPduMemoryAllocs_Type())
ppeBootpPduMemoryAllocs.setMaxAccess(_B)
if mibBuilder.loadTexts:ppeBootpPduMemoryAllocs.setStatus(_A)
_PpeSnmpPduMemoryFailures_Type=Counter32
_PpeSnmpPduMemoryFailures_Object=MibScalar
ppeSnmpPduMemoryFailures=_PpeSnmpPduMemoryFailures_Object((1,3,6,1,4,1,97,3,3,3,35),_PpeSnmpPduMemoryFailures_Type())
ppeSnmpPduMemoryFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:ppeSnmpPduMemoryFailures.setStatus(_A)
_PpeSnmpPduMemoryAllocs_Type=Counter32
_PpeSnmpPduMemoryAllocs_Object=MibScalar
ppeSnmpPduMemoryAllocs=_PpeSnmpPduMemoryAllocs_Object((1,3,6,1,4,1,97,3,3,3,36),_PpeSnmpPduMemoryAllocs_Type())
ppeSnmpPduMemoryAllocs.setMaxAccess(_B)
if mibBuilder.loadTexts:ppeSnmpPduMemoryAllocs.setStatus(_A)
_PpeTftpPduMemoryFailures_Type=Counter32
_PpeTftpPduMemoryFailures_Object=MibScalar
ppeTftpPduMemoryFailures=_PpeTftpPduMemoryFailures_Object((1,3,6,1,4,1,97,3,3,3,37),_PpeTftpPduMemoryFailures_Type())
ppeTftpPduMemoryFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:ppeTftpPduMemoryFailures.setStatus(_A)
_PpeTftpPduMemoryAllocs_Type=Counter32
_PpeTftpPduMemoryAllocs_Object=MibScalar
ppeTftpPduMemoryAllocs=_PpeTftpPduMemoryAllocs_Object((1,3,6,1,4,1,97,3,3,3,38),_PpeTftpPduMemoryAllocs_Type())
ppeTftpPduMemoryAllocs.setMaxAccess(_B)
if mibBuilder.loadTexts:ppeTftpPduMemoryAllocs.setStatus(_A)
_PpeTraceroutePduMemoryFailures_Type=Counter32
_PpeTraceroutePduMemoryFailures_Object=MibScalar
ppeTraceroutePduMemoryFailures=_PpeTraceroutePduMemoryFailures_Object((1,3,6,1,4,1,97,3,3,3,39),_PpeTraceroutePduMemoryFailures_Type())
ppeTraceroutePduMemoryFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:ppeTraceroutePduMemoryFailures.setStatus(_A)
_PpeTraceroutePduMemoryAllocs_Type=Counter32
_PpeTraceroutePduMemoryAllocs_Object=MibScalar
ppeTraceroutePduMemoryAllocs=_PpeTraceroutePduMemoryAllocs_Object((1,3,6,1,4,1,97,3,3,3,40),_PpeTraceroutePduMemoryAllocs_Type())
ppeTraceroutePduMemoryAllocs.setMaxAccess(_B)
if mibBuilder.loadTexts:ppeTraceroutePduMemoryAllocs.setStatus(_A)
_PpeArpPduMemoryFailures_Type=Counter32
_PpeArpPduMemoryFailures_Object=MibScalar
ppeArpPduMemoryFailures=_PpeArpPduMemoryFailures_Object((1,3,6,1,4,1,97,3,3,3,41),_PpeArpPduMemoryFailures_Type())
ppeArpPduMemoryFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:ppeArpPduMemoryFailures.setStatus(_A)
_PpeArpPduMemoryAllocs_Type=Counter32
_PpeArpPduMemoryAllocs_Object=MibScalar
ppeArpPduMemoryAllocs=_PpeArpPduMemoryAllocs_Object((1,3,6,1,4,1,97,3,3,3,42),_PpeArpPduMemoryAllocs_Type())
ppeArpPduMemoryAllocs.setMaxAccess(_B)
if mibBuilder.loadTexts:ppeArpPduMemoryAllocs.setStatus(_A)
_PpeIgmpPduMemoryFailures_Type=Counter32
_PpeIgmpPduMemoryFailures_Object=MibScalar
ppeIgmpPduMemoryFailures=_PpeIgmpPduMemoryFailures_Object((1,3,6,1,4,1,97,3,3,3,43),_PpeIgmpPduMemoryFailures_Type())
ppeIgmpPduMemoryFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:ppeIgmpPduMemoryFailures.setStatus(_A)
_PpeIgmpPduMemoryAllocs_Type=Counter32
_PpeIgmpPduMemoryAllocs_Object=MibScalar
ppeIgmpPduMemoryAllocs=_PpeIgmpPduMemoryAllocs_Object((1,3,6,1,4,1,97,3,3,3,44),_PpeIgmpPduMemoryAllocs_Type())
ppeIgmpPduMemoryAllocs.setMaxAccess(_B)
if mibBuilder.loadTexts:ppeIgmpPduMemoryAllocs.setStatus(_A)
class _PpeAresAsStes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PpeAresAsStes_Type.__name__=_D
_PpeAresAsStes_Object=MibScalar
ppeAresAsStes=_PpeAresAsStes_Object((1,3,6,1,4,1,97,3,3,3,45),_PpeAresAsStes_Type())
ppeAresAsStes.setMaxAccess(_C)
if mibBuilder.loadTexts:ppeAresAsStes.setStatus(_A)
_PpeRoutePercent_Type=Integer32
_PpeRoutePercent_Object=MibScalar
ppeRoutePercent=_PpeRoutePercent_Object((1,3,6,1,4,1,97,3,3,3,46),_PpeRoutePercent_Type())
ppeRoutePercent.setMaxAccess(_B)
if mibBuilder.loadTexts:ppeRoutePercent.setStatus(_A)
_PpeMgtMemorySize_Type=Counter32
_PpeMgtMemorySize_Object=MibScalar
ppeMgtMemorySize=_PpeMgtMemorySize_Object((1,3,6,1,4,1,97,3,3,3,48),_PpeMgtMemorySize_Type())
ppeMgtMemorySize.setMaxAccess(_B)
if mibBuilder.loadTexts:ppeMgtMemorySize.setStatus(_A)
_PpeMgtMemoryAvail_Type=Counter32
_PpeMgtMemoryAvail_Object=MibScalar
ppeMgtMemoryAvail=_PpeMgtMemoryAvail_Object((1,3,6,1,4,1,97,3,3,3,49),_PpeMgtMemoryAvail_Type())
ppeMgtMemoryAvail.setMaxAccess(_B)
if mibBuilder.loadTexts:ppeMgtMemoryAvail.setStatus(_A)
_PpeMgtMemoryFailures_Type=Counter32
_PpeMgtMemoryFailures_Object=MibScalar
ppeMgtMemoryFailures=_PpeMgtMemoryFailures_Object((1,3,6,1,4,1,97,3,3,3,50),_PpeMgtMemoryFailures_Type())
ppeMgtMemoryFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:ppeMgtMemoryFailures.setStatus(_A)
_St_ObjectIdentity=ObjectIdentity
st=_St_ObjectIdentity((1,3,6,1,4,1,97,3,3,4))
_StGroupAddr_Type=OctetString
_StGroupAddr_Object=MibScalar
stGroupAddr=_StGroupAddr_Object((1,3,6,1,4,1,97,3,3,4,1),_StGroupAddr_Type())
stGroupAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:stGroupAddr.setStatus(_A)
_StResAddr_Type=OctetString
_StResAddr_Object=MibScalar
stResAddr=_StResAddr_Object((1,3,6,1,4,1,97,3,3,4,2),_StResAddr_Type())
stResAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:stResAddr.setStatus(_A)
_StBridgeId_Type=OctetString
_StBridgeId_Object=MibScalar
stBridgeId=_StBridgeId_Object((1,3,6,1,4,1,97,3,3,4,3),_StBridgeId_Type())
stBridgeId.setMaxAccess(_C)
if mibBuilder.loadTexts:stBridgeId.setStatus(_A)
_StRootMaxAge_Type=TimeTicks
_StRootMaxAge_Object=MibScalar
stRootMaxAge=_StRootMaxAge_Object((1,3,6,1,4,1,97,3,3,4,4),_StRootMaxAge_Type())
stRootMaxAge.setMaxAccess(_C)
if mibBuilder.loadTexts:stRootMaxAge.setStatus(_A)
_StRootHello_Type=TimeTicks
_StRootHello_Object=MibScalar
stRootHello=_StRootHello_Object((1,3,6,1,4,1,97,3,3,4,5),_StRootHello_Type())
stRootHello.setMaxAccess(_C)
if mibBuilder.loadTexts:stRootHello.setStatus(_A)
_StRootDelay_Type=TimeTicks
_StRootDelay_Object=MibScalar
stRootDelay=_StRootDelay_Object((1,3,6,1,4,1,97,3,3,4,6),_StRootDelay_Type())
stRootDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:stRootDelay.setStatus(_A)
_StRootID_Type=OctetString
_StRootID_Object=MibScalar
stRootID=_StRootID_Object((1,3,6,1,4,1,97,3,3,4,7),_StRootID_Type())
stRootID.setMaxAccess(_B)
if mibBuilder.loadTexts:stRootID.setStatus(_A)
_StRootCost_Type=Integer32
_StRootCost_Object=MibScalar
stRootCost=_StRootCost_Object((1,3,6,1,4,1,97,3,3,4,8),_StRootCost_Type())
stRootCost.setMaxAccess(_B)
if mibBuilder.loadTexts:stRootCost.setStatus(_A)
_StRootPort_Type=Integer32
_StRootPort_Object=MibScalar
stRootPort=_StRootPort_Object((1,3,6,1,4,1,97,3,3,4,9),_StRootPort_Type())
stRootPort.setMaxAccess(_B)
if mibBuilder.loadTexts:stRootPort.setStatus(_A)
class _StTopChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_StTopChange_Type.__name__=_D
_StTopChange_Object=MibScalar
stTopChange=_StTopChange_Object((1,3,6,1,4,1,97,3,3,4,10),_StTopChange_Type())
stTopChange.setMaxAccess(_B)
if mibBuilder.loadTexts:stTopChange.setStatus(_A)
_StActMaxAge_Type=TimeTicks
_StActMaxAge_Object=MibScalar
stActMaxAge=_StActMaxAge_Object((1,3,6,1,4,1,97,3,3,4,11),_StActMaxAge_Type())
stActMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:stActMaxAge.setStatus(_A)
_StActHello_Type=TimeTicks
_StActHello_Object=MibScalar
stActHello=_StActHello_Object((1,3,6,1,4,1,97,3,3,4,12),_StActHello_Type())
stActHello.setMaxAccess(_B)
if mibBuilder.loadTexts:stActHello.setStatus(_A)
_StActDelay_Type=TimeTicks
_StActDelay_Object=MibScalar
stActDelay=_StActDelay_Object((1,3,6,1,4,1,97,3,3,4,13),_StActDelay_Type())
stActDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:stActDelay.setStatus(_A)
_StTopChangeCount_Type=Integer32
_StTopChangeCount_Object=MibScalar
stTopChangeCount=_StTopChangeCount_Object((1,3,6,1,4,1,97,3,3,4,14),_StTopChangeCount_Type())
stTopChangeCount.setMaxAccess(_C)
if mibBuilder.loadTexts:stTopChangeCount.setStatus(_A)
_StTopChangeTime_Type=TimeTicks
_StTopChangeTime_Object=MibScalar
stTopChangeTime=_StTopChangeTime_Object((1,3,6,1,4,1,97,3,3,4,15),_StTopChangeTime_Type())
stTopChangeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:stTopChangeTime.setStatus(_A)
_StAgeTime_Type=Integer32
_StAgeTime_Object=MibScalar
stAgeTime=_StAgeTime_Object((1,3,6,1,4,1,97,3,3,4,16),_StAgeTime_Type())
stAgeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:stAgeTime.setStatus(_A)
_Mesh_ObjectIdentity=ObjectIdentity
mesh=_Mesh_ObjectIdentity((1,3,6,1,4,1,97,3,3,5))
_MeshCostPercent_Type=Integer32
_MeshCostPercent_Object=MibScalar
meshCostPercent=_MeshCostPercent_Object((1,3,6,1,4,1,97,3,3,5,1),_MeshCostPercent_Type())
meshCostPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:meshCostPercent.setStatus(_A)
_MeshCost_Type=Integer32
_MeshCost_Object=MibScalar
meshCost=_MeshCost_Object((1,3,6,1,4,1,97,3,3,5,2),_MeshCost_Type())
meshCost.setMaxAccess(_C)
if mibBuilder.loadTexts:meshCost.setStatus(_A)
class _MeshCostChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_MeshCostChange_Type.__name__=_D
_MeshCostChange_Object=MibScalar
meshCostChange=_MeshCostChange_Object((1,3,6,1,4,1,97,3,3,5,3),_MeshCostChange_Type())
meshCostChange.setMaxAccess(_B)
if mibBuilder.loadTexts:meshCostChange.setStatus(_A)
_MeshCostChangeCount_Type=Integer32
_MeshCostChangeCount_Object=MibScalar
meshCostChangeCount=_MeshCostChangeCount_Object((1,3,6,1,4,1,97,3,3,5,4),_MeshCostChangeCount_Type())
meshCostChangeCount.setMaxAccess(_C)
if mibBuilder.loadTexts:meshCostChangeCount.setStatus(_A)
_MeshCostChangeTime_Type=TimeTicks
_MeshCostChangeTime_Object=MibScalar
meshCostChangeTime=_MeshCostChangeTime_Object((1,3,6,1,4,1,97,3,3,5,5),_MeshCostChangeTime_Type())
meshCostChangeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:meshCostChangeTime.setStatus(_A)
_MeshSubnet_Type=OctetString
_MeshSubnet_Object=MibScalar
meshSubnet=_MeshSubnet_Object((1,3,6,1,4,1,97,3,3,5,6),_MeshSubnet_Type())
meshSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:meshSubnet.setStatus(_A)
_Swdis_ObjectIdentity=ObjectIdentity
swdis=_Swdis_ObjectIdentity((1,3,6,1,4,1,97,3,4))
_SwdisDesc_Type=OctetString
_SwdisDesc_Object=MibScalar
swdisDesc=_SwdisDesc_Object((1,3,6,1,4,1,97,3,4,1),_SwdisDesc_Type())
swdisDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:swdisDesc.setStatus(_A)
class _SwdisAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('protected',1),('any-software',2)))
_SwdisAccess_Type.__name__=_D
_SwdisAccess_Object=MibScalar
swdisAccess=_SwdisAccess_Object((1,3,6,1,4,1,97,3,4,2),_SwdisAccess_Type())
swdisAccess.setMaxAccess(_C)
if mibBuilder.loadTexts:swdisAccess.setStatus(_A)
class _SwdisWriteStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('in-progress',1),('success',2),('config-error',3),('flash-error',4),('config-and-flash-errors',5)))
_SwdisWriteStatus_Type.__name__=_D
_SwdisWriteStatus_Object=MibScalar
swdisWriteStatus=_SwdisWriteStatus_Object((1,3,6,1,4,1,97,3,4,3),_SwdisWriteStatus_Type())
swdisWriteStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swdisWriteStatus.setStatus(_A)
_SwdisConfigIp_Type=IpAddress
_SwdisConfigIp_Object=MibScalar
swdisConfigIp=_SwdisConfigIp_Object((1,3,6,1,4,1,97,3,4,4),_SwdisConfigIp_Type())
swdisConfigIp.setMaxAccess(_C)
if mibBuilder.loadTexts:swdisConfigIp.setStatus(_A)
_SwdisConfigRetryTime_Type=Integer32
_SwdisConfigRetryTime_Object=MibScalar
swdisConfigRetryTime=_SwdisConfigRetryTime_Object((1,3,6,1,4,1,97,3,4,5),_SwdisConfigRetryTime_Type())
swdisConfigRetryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swdisConfigRetryTime.setStatus(_A)
_SwdisConfigTotalTimeout_Type=Integer32
_SwdisConfigTotalTimeout_Object=MibScalar
swdisConfigTotalTimeout=_SwdisConfigTotalTimeout_Object((1,3,6,1,4,1,97,3,4,6),_SwdisConfigTotalTimeout_Type())
swdisConfigTotalTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:swdisConfigTotalTimeout.setStatus(_A)
_Addr_ObjectIdentity=ObjectIdentity
addr=_Addr_ObjectIdentity((1,3,6,1,4,1,97,3,5))
_AddrStatics_Type=Counter32
_AddrStatics_Object=MibScalar
addrStatics=_AddrStatics_Object((1,3,6,1,4,1,97,3,5,1),_AddrStatics_Type())
addrStatics.setMaxAccess(_B)
if mibBuilder.loadTexts:addrStatics.setStatus(_A)
_AddrDynamics_Type=Counter32
_AddrDynamics_Object=MibScalar
addrDynamics=_AddrDynamics_Object((1,3,6,1,4,1,97,3,5,2),_AddrDynamics_Type())
addrDynamics.setMaxAccess(_B)
if mibBuilder.loadTexts:addrDynamics.setStatus(_A)
_AddrDynamicMax_Type=Gauge32
_AddrDynamicMax_Object=MibScalar
addrDynamicMax=_AddrDynamicMax_Object((1,3,6,1,4,1,97,3,5,3),_AddrDynamicMax_Type())
addrDynamicMax.setMaxAccess(_C)
if mibBuilder.loadTexts:addrDynamicMax.setStatus(_A)
_AddrMeshs_Type=Counter32
_AddrMeshs_Object=MibScalar
addrMeshs=_AddrMeshs_Object((1,3,6,1,4,1,97,3,5,4),_AddrMeshs_Type())
addrMeshs.setMaxAccess(_B)
if mibBuilder.loadTexts:addrMeshs.setStatus(_A)
_AddrDynamicOverflows_Type=Counter32
_AddrDynamicOverflows_Object=MibScalar
addrDynamicOverflows=_AddrDynamicOverflows_Object((1,3,6,1,4,1,97,3,5,5),_AddrDynamicOverflows_Type())
addrDynamicOverflows.setMaxAccess(_B)
if mibBuilder.loadTexts:addrDynamicOverflows.setStatus(_A)
_AddrMeshOverflows_Type=Counter32
_AddrMeshOverflows_Object=MibScalar
addrMeshOverflows=_AddrMeshOverflows_Object((1,3,6,1,4,1,97,3,5,6),_AddrMeshOverflows_Type())
addrMeshOverflows.setMaxAccess(_B)
if mibBuilder.loadTexts:addrMeshOverflows.setStatus(_A)
_AddrFlags_Type=Integer32
_AddrFlags_Object=MibScalar
addrFlags=_AddrFlags_Object((1,3,6,1,4,1,97,3,5,7),_AddrFlags_Type())
addrFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:addrFlags.setStatus(_A)
_AddrMAC_Type=OctetString
_AddrMAC_Object=MibScalar
addrMAC=_AddrMAC_Object((1,3,6,1,4,1,97,3,5,8),_AddrMAC_Type())
addrMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:addrMAC.setStatus(_A)
_AddrPort_Type=Integer32
_AddrPort_Object=MibScalar
addrPort=_AddrPort_Object((1,3,6,1,4,1,97,3,5,9),_AddrPort_Type())
addrPort.setMaxAccess(_C)
if mibBuilder.loadTexts:addrPort.setStatus(_A)
_AddrPortMap_Type=OctetString
_AddrPortMap_Object=MibScalar
addrPortMap=_AddrPortMap_Object((1,3,6,1,4,1,97,3,5,10),_AddrPortMap_Type())
addrPortMap.setMaxAccess(_C)
if mibBuilder.loadTexts:addrPortMap.setStatus(_p)
class _AddrOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('read-random',1),('read-next',2),('zero-stats',3),('update',4),('delete',5),('read-block',6)))
_AddrOperation_Type.__name__=_D
_AddrOperation_Object=MibScalar
addrOperation=_AddrOperation_Object((1,3,6,1,4,1,97,3,5,41),_AddrOperation_Type())
addrOperation.setMaxAccess(_C)
if mibBuilder.loadTexts:addrOperation.setStatus(_A)
_AddrIndex_Type=Integer32
_AddrIndex_Object=MibScalar
addrIndex=_AddrIndex_Object((1,3,6,1,4,1,97,3,5,42),_AddrIndex_Type())
addrIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:addrIndex.setStatus(_A)
_AddrNext_Type=Integer32
_AddrNext_Object=MibScalar
addrNext=_AddrNext_Object((1,3,6,1,4,1,97,3,5,44),_AddrNext_Type())
addrNext.setMaxAccess(_C)
if mibBuilder.loadTexts:addrNext.setStatus(_A)
_AddrAge_Type=TimeTicks
_AddrAge_Object=MibScalar
addrAge=_AddrAge_Object((1,3,6,1,4,1,97,3,5,45),_AddrAge_Type())
addrAge.setMaxAccess(_C)
if mibBuilder.loadTexts:addrAge.setStatus(_A)
_AddrRxPkts_Type=Counter32
_AddrRxPkts_Object=MibScalar
addrRxPkts=_AddrRxPkts_Object((1,3,6,1,4,1,97,3,5,46),_AddrRxPkts_Type())
addrRxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:addrRxPkts.setStatus(_A)
_AddrRxChars_Type=Counter32
_AddrRxChars_Object=MibScalar
addrRxChars=_AddrRxChars_Object((1,3,6,1,4,1,97,3,5,47),_AddrRxChars_Type())
addrRxChars.setMaxAccess(_C)
if mibBuilder.loadTexts:addrRxChars.setStatus(_A)
_AddrRxMultiPkts_Type=Counter32
_AddrRxMultiPkts_Object=MibScalar
addrRxMultiPkts=_AddrRxMultiPkts_Object((1,3,6,1,4,1,97,3,5,48),_AddrRxMultiPkts_Type())
addrRxMultiPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:addrRxMultiPkts.setStatus(_A)
_AddrRxFwdPkts_Type=Counter32
_AddrRxFwdPkts_Object=MibScalar
addrRxFwdPkts=_AddrRxFwdPkts_Object((1,3,6,1,4,1,97,3,5,49),_AddrRxFwdPkts_Type())
addrRxFwdPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:addrRxFwdPkts.setStatus(_A)
_AddrTxPkts_Type=Counter32
_AddrTxPkts_Object=MibScalar
addrTxPkts=_AddrTxPkts_Object((1,3,6,1,4,1,97,3,5,50),_AddrTxPkts_Type())
addrTxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:addrTxPkts.setStatus(_A)
_AddrTxChars_Type=Counter32
_AddrTxChars_Object=MibScalar
addrTxChars=_AddrTxChars_Object((1,3,6,1,4,1,97,3,5,51),_AddrTxChars_Type())
addrTxChars.setMaxAccess(_C)
if mibBuilder.loadTexts:addrTxChars.setStatus(_A)
_AddrBlockSize_Type=Integer32
_AddrBlockSize_Object=MibScalar
addrBlockSize=_AddrBlockSize_Object((1,3,6,1,4,1,97,3,5,52),_AddrBlockSize_Type())
addrBlockSize.setMaxAccess(_C)
if mibBuilder.loadTexts:addrBlockSize.setStatus(_A)
_AddrBlock_Type=OctetString
_AddrBlock_Object=MibScalar
addrBlock=_AddrBlock_Object((1,3,6,1,4,1,97,3,5,53),_AddrBlock_Type())
addrBlock.setMaxAccess(_C)
if mibBuilder.loadTexts:addrBlock.setStatus(_A)
_AddrAlarmMAC_Type=OctetString
_AddrAlarmMAC_Object=MibScalar
addrAlarmMAC=_AddrAlarmMAC_Object((1,3,6,1,4,1,97,3,5,54),_AddrAlarmMAC_Type())
addrAlarmMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:addrAlarmMAC.setStatus(_A)
_AddrRptrPort_Type=Integer32
_AddrRptrPort_Object=MibScalar
addrRptrPort=_AddrRptrPort_Object((1,3,6,1,4,1,97,3,5,55),_AddrRptrPort_Type())
addrRptrPort.setMaxAccess(_C)
if mibBuilder.loadTexts:addrRptrPort.setStatus(_A)
_Snmpsmt_ObjectIdentity=ObjectIdentity
snmpsmt=_Snmpsmt_ObjectIdentity((1,3,6,1,4,1,97,3,6))
_SnmpsmtUpstreamReq_Type=OctetString
_SnmpsmtUpstreamReq_Object=MibScalar
snmpsmtUpstreamReq=_SnmpsmtUpstreamReq_Object((1,3,6,1,4,1,97,3,6,1),_SnmpsmtUpstreamReq_Type())
snmpsmtUpstreamReq.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpsmtUpstreamReq.setStatus(_A)
_SnmpsmtUpstreamRsp_Type=OctetString
_SnmpsmtUpstreamRsp_Object=MibScalar
snmpsmtUpstreamRsp=_SnmpsmtUpstreamRsp_Object((1,3,6,1,4,1,97,3,6,2),_SnmpsmtUpstreamRsp_Type())
snmpsmtUpstreamRsp.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpsmtUpstreamRsp.setStatus(_A)
_SnmpsmtUpstreamDescriptor_Type=OctetString
_SnmpsmtUpstreamDescriptor_Object=MibScalar
snmpsmtUpstreamDescriptor=_SnmpsmtUpstreamDescriptor_Object((1,3,6,1,4,1,97,3,6,3),_SnmpsmtUpstreamDescriptor_Type())
snmpsmtUpstreamDescriptor.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpsmtUpstreamDescriptor.setStatus(_A)
_SnmpsmtUpstreamState_Type=OctetString
_SnmpsmtUpstreamState_Object=MibScalar
snmpsmtUpstreamState=_SnmpsmtUpstreamState_Object((1,3,6,1,4,1,97,3,6,4),_SnmpsmtUpstreamState_Type())
snmpsmtUpstreamState.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpsmtUpstreamState.setStatus(_A)
_FddismtTable_Object=MibTable
fddismtTable=_FddismtTable_Object((1,3,6,1,4,1,97,3,6,5))
if mibBuilder.loadTexts:fddismtTable.setStatus(_A)
_FddismtEntry_Object=MibTableRow
fddismtEntry=_FddismtEntry_Object((1,3,6,1,4,1,97,3,6,5,1))
fddismtEntry.setIndexNames((0,_E,_q))
if mibBuilder.loadTexts:fddismtEntry.setStatus(_A)
_FddismtIndex_Type=Integer32
_FddismtIndex_Object=MibTableColumn
fddismtIndex=_FddismtIndex_Object((1,3,6,1,4,1,97,3,6,5,1,1),_FddismtIndex_Type())
fddismtIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fddismtIndex.setStatus(_A)
_FddismtUpstreamReq_Type=OctetString
_FddismtUpstreamReq_Object=MibTableColumn
fddismtUpstreamReq=_FddismtUpstreamReq_Object((1,3,6,1,4,1,97,3,6,5,1,2),_FddismtUpstreamReq_Type())
fddismtUpstreamReq.setMaxAccess(_C)
if mibBuilder.loadTexts:fddismtUpstreamReq.setStatus(_A)
_FddismtUpstreamRsp_Type=OctetString
_FddismtUpstreamRsp_Object=MibTableColumn
fddismtUpstreamRsp=_FddismtUpstreamRsp_Object((1,3,6,1,4,1,97,3,6,5,1,3),_FddismtUpstreamRsp_Type())
fddismtUpstreamRsp.setMaxAccess(_B)
if mibBuilder.loadTexts:fddismtUpstreamRsp.setStatus(_A)
_FddismtUpstreamDescriptor_Type=OctetString
_FddismtUpstreamDescriptor_Object=MibTableColumn
fddismtUpstreamDescriptor=_FddismtUpstreamDescriptor_Object((1,3,6,1,4,1,97,3,6,5,1,4),_FddismtUpstreamDescriptor_Type())
fddismtUpstreamDescriptor.setMaxAccess(_B)
if mibBuilder.loadTexts:fddismtUpstreamDescriptor.setStatus(_A)
_FddismtUpstreamState_Type=OctetString
_FddismtUpstreamState_Object=MibTableColumn
fddismtUpstreamState=_FddismtUpstreamState_Object((1,3,6,1,4,1,97,3,6,5,1,5),_FddismtUpstreamState_Type())
fddismtUpstreamState.setMaxAccess(_B)
if mibBuilder.loadTexts:fddismtUpstreamState.setStatus(_A)
_Sinterfaces_ObjectIdentity=ObjectIdentity
sinterfaces=_Sinterfaces_ObjectIdentity((1,3,6,1,4,1,97,3,7))
_SifUX_Type=Integer32
_SifUX_Object=MibScalar
sifUX=_SifUX_Object((1,3,6,1,4,1,97,3,7,1),_SifUX_Type())
sifUX.setMaxAccess(_B)
if mibBuilder.loadTexts:sifUX.setStatus(_A)
_SifTable_Object=MibTable
sifTable=_SifTable_Object((1,3,6,1,4,1,97,3,7,2))
if mibBuilder.loadTexts:sifTable.setStatus(_A)
_SifEntry_Object=MibTableRow
sifEntry=_SifEntry_Object((1,3,6,1,4,1,97,3,7,2,1))
sifEntry.setIndexNames((0,_E,_r))
if mibBuilder.loadTexts:sifEntry.setStatus(_A)
_SifIndex_Type=Integer32
_SifIndex_Object=MibTableColumn
sifIndex=_SifIndex_Object((1,3,6,1,4,1,97,3,7,2,1,1),_SifIndex_Type())
sifIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sifIndex.setStatus(_A)
_SifSmlRxCnt_Type=Integer32
_SifSmlRxCnt_Object=MibTableColumn
sifSmlRxCnt=_SifSmlRxCnt_Object((1,3,6,1,4,1,97,3,7,2,1,2),_SifSmlRxCnt_Type())
sifSmlRxCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:sifSmlRxCnt.setStatus(_A)
_SifLrgRxCnt_Type=Integer32
_SifLrgRxCnt_Object=MibTableColumn
sifLrgRxCnt=_SifLrgRxCnt_Object((1,3,6,1,4,1,97,3,7,2,1,3),_SifLrgRxCnt_Type())
sifLrgRxCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:sifLrgRxCnt.setStatus(_A)
_SifUxTxCnt_Type=Integer32
_SifUxTxCnt_Object=MibTableColumn
sifUxTxCnt=_SifUxTxCnt_Object((1,3,6,1,4,1,97,3,7,2,1,4),_SifUxTxCnt_Type())
sifUxTxCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:sifUxTxCnt.setStatus(_A)
_SifThreshold_Type=Integer32
_SifThreshold_Object=MibTableColumn
sifThreshold=_SifThreshold_Object((1,3,6,1,4,1,97,3,7,2,1,5),_SifThreshold_Type())
sifThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sifThreshold.setStatus(_A)
_SifThresholdTime_Type=Integer32
_SifThresholdTime_Object=MibTableColumn
sifThresholdTime=_SifThresholdTime_Object((1,3,6,1,4,1,97,3,7,2,1,6),_SifThresholdTime_Type())
sifThresholdTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sifThresholdTime.setStatus(_A)
_SifRxQueueThresh_Type=Integer32
_SifRxQueueThresh_Object=MibTableColumn
sifRxQueueThresh=_SifRxQueueThresh_Object((1,3,6,1,4,1,97,3,7,2,1,7),_SifRxQueueThresh_Type())
sifRxQueueThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:sifRxQueueThresh.setStatus(_A)
_SifRxQueueThreshTime_Type=Integer32
_SifRxQueueThreshTime_Object=MibTableColumn
sifRxQueueThreshTime=_SifRxQueueThreshTime_Object((1,3,6,1,4,1,97,3,7,2,1,8),_SifRxQueueThreshTime_Type())
sifRxQueueThreshTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sifRxQueueThreshTime.setStatus(_A)
_SifTxStormCnt_Type=Integer32
_SifTxStormCnt_Object=MibTableColumn
sifTxStormCnt=_SifTxStormCnt_Object((1,3,6,1,4,1,97,3,7,2,1,9),_SifTxStormCnt_Type())
sifTxStormCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:sifTxStormCnt.setStatus(_A)
_SifTxStormTime_Type=TimeTicks
_SifTxStormTime_Object=MibTableColumn
sifTxStormTime=_SifTxStormTime_Object((1,3,6,1,4,1,97,3,7,2,1,10),_SifTxStormTime_Type())
sifTxStormTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sifTxStormTime.setStatus(_A)
_SifFilterFlags_Type=Integer32
_SifFilterFlags_Object=MibTableColumn
sifFilterFlags=_SifFilterFlags_Object((1,3,6,1,4,1,97,3,7,2,1,11),_SifFilterFlags_Type())
sifFilterFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:sifFilterFlags.setStatus(_A)
_SifCongestTime_Type=TimeTicks
_SifCongestTime_Object=MibTableColumn
sifCongestTime=_SifCongestTime_Object((1,3,6,1,4,1,97,3,7,2,1,12),_SifCongestTime_Type())
sifCongestTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sifCongestTime.setStatus(_A)
_SifQueueTime_Type=TimeTicks
_SifQueueTime_Object=MibTableColumn
sifQueueTime=_SifQueueTime_Object((1,3,6,1,4,1,97,3,7,2,1,13),_SifQueueTime_Type())
sifQueueTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sifQueueTime.setStatus(_A)
_SifPortCost_Type=Integer32
_SifPortCost_Object=MibTableColumn
sifPortCost=_SifPortCost_Object((1,3,6,1,4,1,97,3,7,2,1,14),_SifPortCost_Type())
sifPortCost.setMaxAccess(_C)
if mibBuilder.loadTexts:sifPortCost.setStatus(_A)
_SifStPriority_Type=Integer32
_SifStPriority_Object=MibTableColumn
sifStPriority=_SifStPriority_Object((1,3,6,1,4,1,97,3,7,2,1,15),_SifStPriority_Type())
sifStPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:sifStPriority.setStatus(_A)
_SifFunctions_Type=Integer32
_SifFunctions_Object=MibTableColumn
sifFunctions=_SifFunctions_Object((1,3,6,1,4,1,97,3,7,2,1,16),_SifFunctions_Type())
sifFunctions.setMaxAccess(_B)
if mibBuilder.loadTexts:sifFunctions.setStatus(_A)
class _SifCongested_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SifCongested_Type.__name__=_D
_SifCongested_Object=MibTableColumn
sifCongested=_SifCongested_Object((1,3,6,1,4,1,97,3,7,2,1,17),_SifCongested_Type())
sifCongested.setMaxAccess(_B)
if mibBuilder.loadTexts:sifCongested.setStatus(_A)
class _SifState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('spanning-tree-disabled',1),('spanning-tree-listening',2),('spanning-tree-learning',3),('spanning-tree-forwarding',4),('spanning-tree-blocking',5)))
_SifState_Type.__name__=_D
_SifState_Object=MibTableColumn
sifState=_SifState_Object((1,3,6,1,4,1,97,3,7,2,1,18),_SifState_Type())
sifState.setMaxAccess(_B)
if mibBuilder.loadTexts:sifState.setStatus(_A)
_SifDesigCost_Type=Integer32
_SifDesigCost_Object=MibTableColumn
sifDesigCost=_SifDesigCost_Object((1,3,6,1,4,1,97,3,7,2,1,19),_SifDesigCost_Type())
sifDesigCost.setMaxAccess(_B)
if mibBuilder.loadTexts:sifDesigCost.setStatus(_A)
_SifDesigRoot_Type=OctetString
_SifDesigRoot_Object=MibTableColumn
sifDesigRoot=_SifDesigRoot_Object((1,3,6,1,4,1,97,3,7,2,1,20),_SifDesigRoot_Type())
sifDesigRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:sifDesigRoot.setStatus(_A)
_SifDesigBridge_Type=OctetString
_SifDesigBridge_Object=MibTableColumn
sifDesigBridge=_SifDesigBridge_Object((1,3,6,1,4,1,97,3,7,2,1,21),_SifDesigBridge_Type())
sifDesigBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:sifDesigBridge.setStatus(_A)
_SifDesigPort_Type=OctetString
_SifDesigPort_Object=MibTableColumn
sifDesigPort=_SifDesigPort_Object((1,3,6,1,4,1,97,3,7,2,1,22),_SifDesigPort_Type())
sifDesigPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sifDesigPort.setStatus(_A)
_SifRxPackets_Type=OctetString
_SifRxPackets_Object=MibTableColumn
sifRxPackets=_SifRxPackets_Object((1,3,6,1,4,1,97,3,7,2,1,23),_SifRxPackets_Type())
sifRxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:sifRxPackets.setStatus(_A)
_SifRxChar0s_Type=Counter32
_SifRxChar0s_Object=MibTableColumn
sifRxChar0s=_SifRxChar0s_Object((1,3,6,1,4,1,97,3,7,2,1,24),_SifRxChar0s_Type())
sifRxChar0s.setMaxAccess(_B)
if mibBuilder.loadTexts:sifRxChar0s.setStatus(_A)
_SifRxChar1s_Type=Counter32
_SifRxChar1s_Object=MibTableColumn
sifRxChar1s=_SifRxChar1s_Object((1,3,6,1,4,1,97,3,7,2,1,25),_SifRxChar1s_Type())
sifRxChar1s.setMaxAccess(_B)
if mibBuilder.loadTexts:sifRxChar1s.setStatus(_A)
_SifRxSizeErrors_Type=Counter32
_SifRxSizeErrors_Object=MibTableColumn
sifRxSizeErrors=_SifRxSizeErrors_Object((1,3,6,1,4,1,97,3,7,2,1,26),_SifRxSizeErrors_Type())
sifRxSizeErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:sifRxSizeErrors.setStatus(_A)
_SifRxHwFCSs_Type=Counter32
_SifRxHwFCSs_Object=MibTableColumn
sifRxHwFCSs=_SifRxHwFCSs_Object((1,3,6,1,4,1,97,3,7,2,1,27),_SifRxHwFCSs_Type())
sifRxHwFCSs.setMaxAccess(_B)
if mibBuilder.loadTexts:sifRxHwFCSs.setStatus(_A)
_SifRxQueues_Type=Counter32
_SifRxQueues_Object=MibTableColumn
sifRxQueues=_SifRxQueues_Object((1,3,6,1,4,1,97,3,7,2,1,28),_SifRxQueues_Type())
sifRxQueues.setMaxAccess(_B)
if mibBuilder.loadTexts:sifRxQueues.setStatus(_A)
_SifTxPackets_Type=OctetString
_SifTxPackets_Object=MibTableColumn
sifTxPackets=_SifTxPackets_Object((1,3,6,1,4,1,97,3,7,2,1,30),_SifTxPackets_Type())
sifTxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:sifTxPackets.setStatus(_A)
_SifTxCongests_Type=Counter32
_SifTxCongests_Object=MibTableColumn
sifTxCongests=_SifTxCongests_Object((1,3,6,1,4,1,97,3,7,2,1,31),_SifTxCongests_Type())
sifTxCongests.setMaxAccess(_B)
if mibBuilder.loadTexts:sifTxCongests.setStatus(_p)
_SifTxStorms_Type=Counter32
_SifTxStorms_Object=MibTableColumn
sifTxStorms=_SifTxStorms_Object((1,3,6,1,4,1,97,3,7,2,1,32),_SifTxStorms_Type())
sifTxStorms.setMaxAccess(_B)
if mibBuilder.loadTexts:sifTxStorms.setStatus(_A)
_SifTxDests_Type=Counter32
_SifTxDests_Object=MibTableColumn
sifTxDests=_SifTxDests_Object((1,3,6,1,4,1,97,3,7,2,1,33),_SifTxDests_Type())
sifTxDests.setMaxAccess(_B)
if mibBuilder.loadTexts:sifTxDests.setStatus(_A)
class _SifErrorsFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SifErrorsFlag_Type.__name__=_D
_SifErrorsFlag_Object=MibTableColumn
sifErrorsFlag=_SifErrorsFlag_Object((1,3,6,1,4,1,97,3,7,2,1,34),_SifErrorsFlag_Type())
sifErrorsFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:sifErrorsFlag.setStatus(_A)
class _SifTxStormFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SifTxStormFlag_Type.__name__=_D
_SifTxStormFlag_Object=MibTableColumn
sifTxStormFlag=_SifTxStormFlag_Object((1,3,6,1,4,1,97,3,7,2,1,35),_SifTxStormFlag_Type())
sifTxStormFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:sifTxStormFlag.setStatus(_A)
_SifTxSizes_Type=Counter32
_SifTxSizes_Object=MibTableColumn
sifTxSizes=_SifTxSizes_Object((1,3,6,1,4,1,97,3,7,2,1,36),_SifTxSizes_Type())
sifTxSizes.setMaxAccess(_B)
if mibBuilder.loadTexts:sifTxSizes.setStatus(_A)
_SifTxAddr_Type=OctetString
_SifTxAddr_Object=MibTableColumn
sifTxAddr=_SifTxAddr_Object((1,3,6,1,4,1,97,3,7,2,1,37),_SifTxAddr_Type())
sifTxAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:sifTxAddr.setStatus(_A)
_SifLan_Type=Integer32
_SifLan_Object=MibTableColumn
sifLan=_SifLan_Object((1,3,6,1,4,1,97,3,7,2,1,38),_SifLan_Type())
sifLan.setMaxAccess(_C)
if mibBuilder.loadTexts:sifLan.setStatus(_A)
_SifStatisticsTime_Type=TimeTicks
_SifStatisticsTime_Object=MibTableColumn
sifStatisticsTime=_SifStatisticsTime_Object((1,3,6,1,4,1,97,3,7,2,1,39),_SifStatisticsTime_Type())
sifStatisticsTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sifStatisticsTime.setStatus(_A)
_SifIpAddress_Type=IpAddress
_SifIpAddress_Object=MibTableColumn
sifIpAddress=_SifIpAddress_Object((1,3,6,1,4,1,97,3,7,2,1,40),_SifIpAddress_Type())
sifIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:sifIpAddress.setStatus(_A)
_SifIpGroupAddress_Type=IpAddress
_SifIpGroupAddress_Object=MibTableColumn
sifIpGroupAddress=_SifIpGroupAddress_Object((1,3,6,1,4,1,97,3,7,2,1,41),_SifIpGroupAddress_Type())
sifIpGroupAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:sifIpGroupAddress.setStatus(_A)
_SifMaxPacketSize_Type=Integer32
_SifMaxPacketSize_Object=MibTableColumn
sifMaxPacketSize=_SifMaxPacketSize_Object((1,3,6,1,4,1,97,3,7,2,1,42),_SifMaxPacketSize_Type())
sifMaxPacketSize.setMaxAccess(_C)
if mibBuilder.loadTexts:sifMaxPacketSize.setStatus(_A)
class _SifExpectSqe_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SifExpectSqe_Type.__name__=_D
_SifExpectSqe_Object=MibTableColumn
sifExpectSqe=_SifExpectSqe_Object((1,3,6,1,4,1,97,3,7,2,1,43),_SifExpectSqe_Type())
sifExpectSqe.setMaxAccess(_C)
if mibBuilder.loadTexts:sifExpectSqe.setStatus(_A)
class _SifFilterLocal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SifFilterLocal_Type.__name__=_D
_SifFilterLocal_Object=MibTableColumn
sifFilterLocal=_SifFilterLocal_Object((1,3,6,1,4,1,97,3,7,2,1,44),_SifFilterLocal_Type())
sifFilterLocal.setMaxAccess(_C)
if mibBuilder.loadTexts:sifFilterLocal.setStatus(_A)
_SifInQLen_Type=Gauge32
_SifInQLen_Object=MibTableColumn
sifInQLen=_SifInQLen_Object((1,3,6,1,4,1,97,3,7,2,1,45),_SifInQLen_Type())
sifInQLen.setMaxAccess(_C)
if mibBuilder.loadTexts:sifInQLen.setStatus(_A)
class _SifFrameSwitching_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_SifFrameSwitching_Type.__name__=_D
_SifFrameSwitching_Object=MibTableColumn
sifFrameSwitching=_SifFrameSwitching_Object((1,3,6,1,4,1,97,3,7,2,1,46),_SifFrameSwitching_Type())
sifFrameSwitching.setMaxAccess(_C)
if mibBuilder.loadTexts:sifFrameSwitching.setStatus(_A)
_SifRingDrops_Type=Counter32
_SifRingDrops_Object=MibTableColumn
sifRingDrops=_SifRingDrops_Object((1,3,6,1,4,1,97,3,7,2,1,47),_SifRingDrops_Type())
sifRingDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:sifRingDrops.setStatus(_A)
_SifAdapterChecks_Type=Counter32
_SifAdapterChecks_Object=MibTableColumn
sifAdapterChecks=_SifAdapterChecks_Object((1,3,6,1,4,1,97,3,7,2,1,48),_SifAdapterChecks_Type())
sifAdapterChecks.setMaxAccess(_B)
if mibBuilder.loadTexts:sifAdapterChecks.setStatus(_A)
_SifIpRipPortMetric_Type=Integer32
_SifIpRipPortMetric_Object=MibTableColumn
sifIpRipPortMetric=_SifIpRipPortMetric_Object((1,3,6,1,4,1,97,3,7,2,1,49),_SifIpRipPortMetric_Type())
sifIpRipPortMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:sifIpRipPortMetric.setStatus(_A)
_SifDescr_Type=OctetString
_SifDescr_Object=MibTableColumn
sifDescr=_SifDescr_Object((1,3,6,1,4,1,97,3,7,2,1,50),_SifDescr_Type())
sifDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:sifDescr.setStatus(_A)
_SifUtilInterval_Type=Integer32
_SifUtilInterval_Object=MibScalar
sifUtilInterval=_SifUtilInterval_Object((1,3,6,1,4,1,97,3,7,3),_SifUtilInterval_Type())
sifUtilInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:sifUtilInterval.setStatus(_A)
_SifUtilCount_Type=Integer32
_SifUtilCount_Object=MibScalar
sifUtilCount=_SifUtilCount_Object((1,3,6,1,4,1,97,3,7,4),_SifUtilCount_Type())
sifUtilCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sifUtilCount.setStatus(_A)
class _SifUtilPortPeakReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_F,1))
_SifUtilPortPeakReset_Type.__name__=_D
_SifUtilPortPeakReset_Object=MibScalar
sifUtilPortPeakReset=_SifUtilPortPeakReset_Object((1,3,6,1,4,1,97,3,7,5),_SifUtilPortPeakReset_Type())
sifUtilPortPeakReset.setMaxAccess(_C)
if mibBuilder.loadTexts:sifUtilPortPeakReset.setStatus(_A)
_SifUtilPortPeakTable_Object=MibTable
sifUtilPortPeakTable=_SifUtilPortPeakTable_Object((1,3,6,1,4,1,97,3,7,6))
if mibBuilder.loadTexts:sifUtilPortPeakTable.setStatus(_A)
_SifUtilPortPeakEntry_Object=MibTableRow
sifUtilPortPeakEntry=_SifUtilPortPeakEntry_Object((1,3,6,1,4,1,97,3,7,6,1))
sifUtilPortPeakEntry.setIndexNames((0,_E,_s),(0,_E,_t))
if mibBuilder.loadTexts:sifUtilPortPeakEntry.setStatus(_A)
_SifUtilPortPeakIndex_Type=Integer32
_SifUtilPortPeakIndex_Object=MibTableColumn
sifUtilPortPeakIndex=_SifUtilPortPeakIndex_Object((1,3,6,1,4,1,97,3,7,6,1,1),_SifUtilPortPeakIndex_Type())
sifUtilPortPeakIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sifUtilPortPeakIndex.setStatus(_A)
_SifUtilPortPeakOrdinal_Type=Integer32
_SifUtilPortPeakOrdinal_Object=MibTableColumn
sifUtilPortPeakOrdinal=_SifUtilPortPeakOrdinal_Object((1,3,6,1,4,1,97,3,7,6,1,2),_SifUtilPortPeakOrdinal_Type())
sifUtilPortPeakOrdinal.setMaxAccess(_B)
if mibBuilder.loadTexts:sifUtilPortPeakOrdinal.setStatus(_A)
_SifUtilPortPeakBRTimestamp_Type=TimeTicks
_SifUtilPortPeakBRTimestamp_Object=MibTableColumn
sifUtilPortPeakBRTimestamp=_SifUtilPortPeakBRTimestamp_Object((1,3,6,1,4,1,97,3,7,6,1,3),_SifUtilPortPeakBRTimestamp_Type())
sifUtilPortPeakBRTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:sifUtilPortPeakBRTimestamp.setStatus(_A)
class _SifUtilPortPeakTBitRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_SifUtilPortPeakTBitRate_Type.__name__=_D
_SifUtilPortPeakTBitRate_Object=MibTableColumn
sifUtilPortPeakTBitRate=_SifUtilPortPeakTBitRate_Object((1,3,6,1,4,1,97,3,7,6,1,4),_SifUtilPortPeakTBitRate_Type())
sifUtilPortPeakTBitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:sifUtilPortPeakTBitRate.setStatus(_A)
class _SifUtilPortPeakRBitRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_SifUtilPortPeakRBitRate_Type.__name__=_D
_SifUtilPortPeakRBitRate_Object=MibTableColumn
sifUtilPortPeakRBitRate=_SifUtilPortPeakRBitRate_Object((1,3,6,1,4,1,97,3,7,6,1,5),_SifUtilPortPeakRBitRate_Type())
sifUtilPortPeakRBitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:sifUtilPortPeakRBitRate.setStatus(_A)
class _SifUtilSysPeakReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_F,1))
_SifUtilSysPeakReset_Type.__name__=_D
_SifUtilSysPeakReset_Object=MibScalar
sifUtilSysPeakReset=_SifUtilSysPeakReset_Object((1,3,6,1,4,1,97,3,7,7),_SifUtilSysPeakReset_Type())
sifUtilSysPeakReset.setMaxAccess(_C)
if mibBuilder.loadTexts:sifUtilSysPeakReset.setStatus(_A)
_SifUtilSysPeakTable_Object=MibTable
sifUtilSysPeakTable=_SifUtilSysPeakTable_Object((1,3,6,1,4,1,97,3,7,8))
if mibBuilder.loadTexts:sifUtilSysPeakTable.setStatus(_A)
_SifUtilSysPeakEntry_Object=MibTableRow
sifUtilSysPeakEntry=_SifUtilSysPeakEntry_Object((1,3,6,1,4,1,97,3,7,8,1))
sifUtilSysPeakEntry.setIndexNames((0,_E,_u),(0,_E,_v))
if mibBuilder.loadTexts:sifUtilSysPeakEntry.setStatus(_A)
_SifUtilSysPeakIndex_Type=Integer32
_SifUtilSysPeakIndex_Object=MibTableColumn
sifUtilSysPeakIndex=_SifUtilSysPeakIndex_Object((1,3,6,1,4,1,97,3,7,8,1,1),_SifUtilSysPeakIndex_Type())
sifUtilSysPeakIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sifUtilSysPeakIndex.setStatus(_A)
_SifUtilSysPeakOrdinal_Type=Integer32
_SifUtilSysPeakOrdinal_Object=MibTableColumn
sifUtilSysPeakOrdinal=_SifUtilSysPeakOrdinal_Object((1,3,6,1,4,1,97,3,7,8,1,2),_SifUtilSysPeakOrdinal_Type())
sifUtilSysPeakOrdinal.setMaxAccess(_B)
if mibBuilder.loadTexts:sifUtilSysPeakOrdinal.setStatus(_A)
_SifUtilSysPeakTimestamp_Type=TimeTicks
_SifUtilSysPeakTimestamp_Object=MibTableColumn
sifUtilSysPeakTimestamp=_SifUtilSysPeakTimestamp_Object((1,3,6,1,4,1,97,3,7,8,1,3),_SifUtilSysPeakTimestamp_Type())
sifUtilSysPeakTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:sifUtilSysPeakTimestamp.setStatus(_A)
class _SifUtilSysPeakTBitRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_SifUtilSysPeakTBitRate_Type.__name__=_D
_SifUtilSysPeakTBitRate_Object=MibTableColumn
sifUtilSysPeakTBitRate=_SifUtilSysPeakTBitRate_Object((1,3,6,1,4,1,97,3,7,8,1,4),_SifUtilSysPeakTBitRate_Type())
sifUtilSysPeakTBitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:sifUtilSysPeakTBitRate.setStatus(_A)
class _SifUtilSysPeakRBitRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_SifUtilSysPeakRBitRate_Type.__name__=_D
_SifUtilSysPeakRBitRate_Object=MibTableColumn
sifUtilSysPeakRBitRate=_SifUtilSysPeakRBitRate_Object((1,3,6,1,4,1,97,3,7,8,1,5),_SifUtilSysPeakRBitRate_Type())
sifUtilSysPeakRBitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:sifUtilSysPeakRBitRate.setStatus(_A)
_Sfddi_ObjectIdentity=ObjectIdentity
sfddi=_Sfddi_ObjectIdentity((1,3,6,1,4,1,97,3,8))
_SfddiTable_Object=MibTable
sfddiTable=_SfddiTable_Object((1,3,6,1,4,1,97,3,8,1))
if mibBuilder.loadTexts:sfddiTable.setStatus(_A)
_SfddiEntry_Object=MibTableRow
sfddiEntry=_SfddiEntry_Object((1,3,6,1,4,1,97,3,8,1,1))
sfddiEntry.setIndexNames((0,_E,_w))
if mibBuilder.loadTexts:sfddiEntry.setStatus(_A)
_SfddiIndex_Type=Integer32
_SfddiIndex_Object=MibTableColumn
sfddiIndex=_SfddiIndex_Object((1,3,6,1,4,1,97,3,8,1,1,1),_SfddiIndex_Type())
sfddiIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfddiIndex.setStatus(_A)
_SfddiRxHwAborts_Type=Counter32
_SfddiRxHwAborts_Object=MibTableColumn
sfddiRxHwAborts=_SfddiRxHwAborts_Object((1,3,6,1,4,1,97,3,8,1,1,2),_SfddiRxHwAborts_Type())
sfddiRxHwAborts.setMaxAccess(_C)
if mibBuilder.loadTexts:sfddiRxHwAborts.setStatus(_A)
_SfddiRxParitys_Type=Counter32
_SfddiRxParitys_Object=MibTableColumn
sfddiRxParitys=_SfddiRxParitys_Object((1,3,6,1,4,1,97,3,8,1,1,3),_SfddiRxParitys_Type())
sfddiRxParitys.setMaxAccess(_C)
if mibBuilder.loadTexts:sfddiRxParitys.setStatus(_A)
_SfddiRxShorts_Type=Counter32
_SfddiRxShorts_Object=MibTableColumn
sfddiRxShorts=_SfddiRxShorts_Object((1,3,6,1,4,1,97,3,8,1,1,4),_SfddiRxShorts_Type())
sfddiRxShorts.setMaxAccess(_C)
if mibBuilder.loadTexts:sfddiRxShorts.setStatus(_A)
_SfddiDpcErrCnts_Type=Counter32
_SfddiDpcErrCnts_Object=MibTableColumn
sfddiDpcErrCnts=_SfddiDpcErrCnts_Object((1,3,6,1,4,1,97,3,8,1,1,5),_SfddiDpcErrCnts_Type())
sfddiDpcErrCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:sfddiDpcErrCnts.setStatus(_A)
_SfddiDpcErrValue_Type=Integer32
_SfddiDpcErrValue_Object=MibTableColumn
sfddiDpcErrValue=_SfddiDpcErrValue_Object((1,3,6,1,4,1,97,3,8,1,1,6),_SfddiDpcErrValue_Type())
sfddiDpcErrValue.setMaxAccess(_C)
if mibBuilder.loadTexts:sfddiDpcErrValue.setStatus(_A)
_SfddiRbcErrCnts_Type=Counter32
_SfddiRbcErrCnts_Object=MibTableColumn
sfddiRbcErrCnts=_SfddiRbcErrCnts_Object((1,3,6,1,4,1,97,3,8,1,1,7),_SfddiRbcErrCnts_Type())
sfddiRbcErrCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:sfddiRbcErrCnts.setStatus(_A)
_SfddiRbcErrValue_Type=Integer32
_SfddiRbcErrValue_Object=MibTableColumn
sfddiRbcErrValue=_SfddiRbcErrValue_Object((1,3,6,1,4,1,97,3,8,1,1,8),_SfddiRbcErrValue_Type())
sfddiRbcErrValue.setMaxAccess(_C)
if mibBuilder.loadTexts:sfddiRbcErrValue.setStatus(_A)
_SfddiTxAsync_Type=Integer32
_SfddiTxAsync_Object=MibTableColumn
sfddiTxAsync=_SfddiTxAsync_Object((1,3,6,1,4,1,97,3,8,1,1,9),_SfddiTxAsync_Type())
sfddiTxAsync.setMaxAccess(_C)
if mibBuilder.loadTexts:sfddiTxAsync.setStatus(_A)
class _SfddiShortAddressing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SfddiShortAddressing_Type.__name__=_D
_SfddiShortAddressing_Object=MibTableColumn
sfddiShortAddressing=_SfddiShortAddressing_Object((1,3,6,1,4,1,97,3,8,1,1,10),_SfddiShortAddressing_Type())
sfddiShortAddressing.setMaxAccess(_B)
if mibBuilder.loadTexts:sfddiShortAddressing.setStatus(_A)
_SfddiSmtConditions_Type=Integer32
_SfddiSmtConditions_Object=MibTableColumn
sfddiSmtConditions=_SfddiSmtConditions_Object((1,3,6,1,4,1,97,3,8,1,1,11),_SfddiSmtConditions_Type())
sfddiSmtConditions.setMaxAccess(_C)
if mibBuilder.loadTexts:sfddiSmtConditions.setStatus(_A)
_SfddiSrfConditions_Type=Integer32
_SfddiSrfConditions_Object=MibTableColumn
sfddiSrfConditions=_SfddiSrfConditions_Object((1,3,6,1,4,1,97,3,8,1,1,12),_SfddiSrfConditions_Type())
sfddiSrfConditions.setMaxAccess(_C)
if mibBuilder.loadTexts:sfddiSrfConditions.setStatus(_A)
_SfddiSmtConditionsStatus_Type=Integer32
_SfddiSmtConditionsStatus_Object=MibTableColumn
sfddiSmtConditionsStatus=_SfddiSmtConditionsStatus_Object((1,3,6,1,4,1,97,3,8,1,1,13),_SfddiSmtConditionsStatus_Type())
sfddiSmtConditionsStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sfddiSmtConditionsStatus.setStatus(_A)
_SfddiSrfConditionsStatus_Type=Integer32
_SfddiSrfConditionsStatus_Object=MibTableColumn
sfddiSrfConditionsStatus=_SfddiSrfConditionsStatus_Object((1,3,6,1,4,1,97,3,8,1,1,14),_SfddiSrfConditionsStatus_Type())
sfddiSrfConditionsStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sfddiSrfConditionsStatus.setStatus(_A)
_SfddiSrfReportLimit_Type=Integer32
_SfddiSrfReportLimit_Object=MibTableColumn
sfddiSrfReportLimit=_SfddiSrfReportLimit_Object((1,3,6,1,4,1,97,3,8,1,1,15),_SfddiSrfReportLimit_Type())
sfddiSrfReportLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:sfddiSrfReportLimit.setStatus(_A)
_SfddiFrameErrorThreshold_Type=Integer32
_SfddiFrameErrorThreshold_Object=MibTableColumn
sfddiFrameErrorThreshold=_SfddiFrameErrorThreshold_Object((1,3,6,1,4,1,97,3,8,1,1,16),_SfddiFrameErrorThreshold_Type())
sfddiFrameErrorThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfddiFrameErrorThreshold.setStatus(_A)
_SfddiNotCopiedThreshold_Type=Integer32
_SfddiNotCopiedThreshold_Object=MibTableColumn
sfddiNotCopiedThreshold=_SfddiNotCopiedThreshold_Object((1,3,6,1,4,1,97,3,8,1,1,17),_SfddiNotCopiedThreshold_Type())
sfddiNotCopiedThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfddiNotCopiedThreshold.setStatus(_A)
class _SfddiSBFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SfddiSBFlag_Type.__name__=_D
_SfddiSBFlag_Object=MibTableColumn
sfddiSBFlag=_SfddiSBFlag_Object((1,3,6,1,4,1,97,3,8,1,1,18),_SfddiSBFlag_Type())
sfddiSBFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:sfddiSBFlag.setStatus(_A)
_SfddiRxEbits_Type=Counter32
_SfddiRxEbits_Object=MibTableColumn
sfddiRxEbits=_SfddiRxEbits_Object((1,3,6,1,4,1,97,3,8,1,1,19),_SfddiRxEbits_Type())
sfddiRxEbits.setMaxAccess(_B)
if mibBuilder.loadTexts:sfddiRxEbits.setStatus(_A)
class _SfddiOBSFuseBad_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SfddiOBSFuseBad_Type.__name__=_D
_SfddiOBSFuseBad_Object=MibTableColumn
sfddiOBSFuseBad=_SfddiOBSFuseBad_Object((1,3,6,1,4,1,97,3,8,1,1,20),_SfddiOBSFuseBad_Type())
sfddiOBSFuseBad.setMaxAccess(_B)
if mibBuilder.loadTexts:sfddiOBSFuseBad.setStatus(_A)
class _SfddiThruB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SfddiThruB_Type.__name__=_D
_SfddiThruB_Object=MibTableColumn
sfddiThruB=_SfddiThruB_Object((1,3,6,1,4,1,97,3,8,1,1,21),_SfddiThruB_Type())
sfddiThruB.setMaxAccess(_C)
if mibBuilder.loadTexts:sfddiThruB.setStatus(_A)
_SfddiStationDescriptor_Type=OctetString
_SfddiStationDescriptor_Object=MibTableColumn
sfddiStationDescriptor=_SfddiStationDescriptor_Object((1,3,6,1,4,1,97,3,8,1,1,22),_SfddiStationDescriptor_Type())
sfddiStationDescriptor.setMaxAccess(_B)
if mibBuilder.loadTexts:sfddiStationDescriptor.setStatus(_A)
_SfddiStationState_Type=OctetString
_SfddiStationState_Object=MibTableColumn
sfddiStationState=_SfddiStationState_Object((1,3,6,1,4,1,97,3,8,1,1,23),_SfddiStationState_Type())
sfddiStationState.setMaxAccess(_B)
if mibBuilder.loadTexts:sfddiStationState.setStatus(_A)
_SfddiDownstreamNbr_Type=OctetString
_SfddiDownstreamNbr_Object=MibTableColumn
sfddiDownstreamNbr=_SfddiDownstreamNbr_Object((1,3,6,1,4,1,97,3,8,1,1,24),_SfddiDownstreamNbr_Type())
sfddiDownstreamNbr.setMaxAccess(_B)
if mibBuilder.loadTexts:sfddiDownstreamNbr.setStatus(_A)
_SfddiSMTBufferSize_Type=Integer32
_SfddiSMTBufferSize_Object=MibTableColumn
sfddiSMTBufferSize=_SfddiSMTBufferSize_Object((1,3,6,1,4,1,97,3,8,1,1,25),_SfddiSMTBufferSize_Type())
sfddiSMTBufferSize.setMaxAccess(_C)
if mibBuilder.loadTexts:sfddiSMTBufferSize.setStatus(_A)
_Suart_ObjectIdentity=ObjectIdentity
suart=_Suart_ObjectIdentity((1,3,6,1,4,1,97,3,9))
_SuartTable_Object=MibTable
suartTable=_SuartTable_Object((1,3,6,1,4,1,97,3,9,1))
if mibBuilder.loadTexts:suartTable.setStatus(_A)
_SuartEntry_Object=MibTableRow
suartEntry=_SuartEntry_Object((1,3,6,1,4,1,97,3,9,1,1))
suartEntry.setIndexNames((0,_E,_x))
if mibBuilder.loadTexts:suartEntry.setStatus(_A)
_SuartIndex_Type=Integer32
_SuartIndex_Object=MibTableColumn
suartIndex=_SuartIndex_Object((1,3,6,1,4,1,97,3,9,1,1,1),_SuartIndex_Type())
suartIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:suartIndex.setStatus(_A)
class _SuartBaud_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('external-clock',1),(_y,2),(_z,3),(_A0,4),(_A1,5),(_A2,6),(_A3,7),(_A4,8),(_A5,9),(_A6,10),(_A7,11)))
_SuartBaud_Type.__name__=_D
_SuartBaud_Object=MibTableColumn
suartBaud=_SuartBaud_Object((1,3,6,1,4,1,97,3,9,1,1,2),_SuartBaud_Type())
suartBaud.setMaxAccess(_C)
if mibBuilder.loadTexts:suartBaud.setStatus(_A)
_SuartModem_Type=Integer32
_SuartModem_Object=MibTableColumn
suartModem=_SuartModem_Object((1,3,6,1,4,1,97,3,9,1,1,3),_SuartModem_Type())
suartModem.setMaxAccess(_C)
if mibBuilder.loadTexts:suartModem.setStatus(_A)
_SuartIpNeighborAddress_Type=IpAddress
_SuartIpNeighborAddress_Object=MibTableColumn
suartIpNeighborAddress=_SuartIpNeighborAddress_Object((1,3,6,1,4,1,97,3,9,1,1,4),_SuartIpNeighborAddress_Type())
suartIpNeighborAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:suartIpNeighborAddress.setStatus(_A)
class _SuartPPPActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SuartPPPActive_Type.__name__=_D
_SuartPPPActive_Object=MibTableColumn
suartPPPActive=_SuartPPPActive_Object((1,3,6,1,4,1,97,3,9,1,1,5),_SuartPPPActive_Type())
suartPPPActive.setMaxAccess(_C)
if mibBuilder.loadTexts:suartPPPActive.setStatus(_A)
_SuartAlignmentErrors_Type=Counter32
_SuartAlignmentErrors_Object=MibTableColumn
suartAlignmentErrors=_SuartAlignmentErrors_Object((1,3,6,1,4,1,97,3,9,1,1,6),_SuartAlignmentErrors_Type())
suartAlignmentErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:suartAlignmentErrors.setStatus(_A)
_SuartOverrunErrors_Type=Counter32
_SuartOverrunErrors_Object=MibTableColumn
suartOverrunErrors=_SuartOverrunErrors_Object((1,3,6,1,4,1,97,3,9,1,1,7),_SuartOverrunErrors_Type())
suartOverrunErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:suartOverrunErrors.setStatus(_A)
_Filter_ObjectIdentity=ObjectIdentity
filter=_Filter_ObjectIdentity((1,3,6,1,4,1,97,3,10))
_FilterMaxCount_Type=Integer32
_FilterMaxCount_Object=MibScalar
filterMaxCount=_FilterMaxCount_Object((1,3,6,1,4,1,97,3,10,1),_FilterMaxCount_Type())
filterMaxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:filterMaxCount.setStatus(_A)
_FilterCurrentCount_Type=Integer32
_FilterCurrentCount_Object=MibScalar
filterCurrentCount=_FilterCurrentCount_Object((1,3,6,1,4,1,97,3,10,2),_FilterCurrentCount_Type())
filterCurrentCount.setMaxAccess(_B)
if mibBuilder.loadTexts:filterCurrentCount.setStatus(_A)
_FilterDeleteID_Type=Integer32
_FilterDeleteID_Object=MibScalar
filterDeleteID=_FilterDeleteID_Object((1,3,6,1,4,1,97,3,10,3),_FilterDeleteID_Type())
filterDeleteID.setMaxAccess(_C)
if mibBuilder.loadTexts:filterDeleteID.setStatus(_A)
_FilterNextID_Type=Integer32
_FilterNextID_Object=MibScalar
filterNextID=_FilterNextID_Object((1,3,6,1,4,1,97,3,10,4),_FilterNextID_Type())
filterNextID.setMaxAccess(_B)
if mibBuilder.loadTexts:filterNextID.setStatus(_A)
_FilterAddID_Type=Integer32
_FilterAddID_Object=MibScalar
filterAddID=_FilterAddID_Object((1,3,6,1,4,1,97,3,10,5),_FilterAddID_Type())
filterAddID.setMaxAccess(_C)
if mibBuilder.loadTexts:filterAddID.setStatus(_A)
_FilterAddIndex_Type=Integer32
_FilterAddIndex_Object=MibScalar
filterAddIndex=_FilterAddIndex_Object((1,3,6,1,4,1,97,3,10,6),_FilterAddIndex_Type())
filterAddIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:filterAddIndex.setStatus(_A)
_FilterTable_Object=MibTable
filterTable=_FilterTable_Object((1,3,6,1,4,1,97,3,10,7))
if mibBuilder.loadTexts:filterTable.setStatus(_A)
_FilterEntry_Object=MibTableRow
filterEntry=_FilterEntry_Object((1,3,6,1,4,1,97,3,10,7,1))
filterEntry.setIndexNames((0,_E,_A8))
if mibBuilder.loadTexts:filterEntry.setStatus(_A)
_FilterIndex_Type=Integer32
_FilterIndex_Object=MibTableColumn
filterIndex=_FilterIndex_Object((1,3,6,1,4,1,97,3,10,7,1,1),_FilterIndex_Type())
filterIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:filterIndex.setStatus(_A)
_FilterID_Type=Integer32
_FilterID_Object=MibTableColumn
filterID=_FilterID_Object((1,3,6,1,4,1,97,3,10,7,1,2),_FilterID_Type())
filterID.setMaxAccess(_B)
if mibBuilder.loadTexts:filterID.setStatus(_A)
_FilterPortNo_Type=Integer32
_FilterPortNo_Object=MibTableColumn
filterPortNo=_FilterPortNo_Object((1,3,6,1,4,1,97,3,10,7,1,3),_FilterPortNo_Type())
filterPortNo.setMaxAccess(_C)
if mibBuilder.loadTexts:filterPortNo.setStatus(_A)
_FilterComboType_Type=Integer32
_FilterComboType_Object=MibTableColumn
filterComboType=_FilterComboType_Object((1,3,6,1,4,1,97,3,10,7,1,4),_FilterComboType_Type())
filterComboType.setMaxAccess(_C)
if mibBuilder.loadTexts:filterComboType.setStatus(_A)
_FilterFlags_Type=Integer32
_FilterFlags_Object=MibTableColumn
filterFlags=_FilterFlags_Object((1,3,6,1,4,1,97,3,10,7,1,5),_FilterFlags_Type())
filterFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:filterFlags.setStatus(_A)
_FilterFrame_Type=Integer32
_FilterFrame_Object=MibTableColumn
filterFrame=_FilterFrame_Object((1,3,6,1,4,1,97,3,10,7,1,6),_FilterFrame_Type())
filterFrame.setMaxAccess(_C)
if mibBuilder.loadTexts:filterFrame.setStatus(_A)
_FilterSource_Type=OctetString
_FilterSource_Object=MibTableColumn
filterSource=_FilterSource_Object((1,3,6,1,4,1,97,3,10,7,1,7),_FilterSource_Type())
filterSource.setMaxAccess(_C)
if mibBuilder.loadTexts:filterSource.setStatus(_A)
_FilterSourceEnd_Type=OctetString
_FilterSourceEnd_Object=MibTableColumn
filterSourceEnd=_FilterSourceEnd_Object((1,3,6,1,4,1,97,3,10,7,1,8),_FilterSourceEnd_Type())
filterSourceEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:filterSourceEnd.setStatus(_A)
_FilterDest_Type=OctetString
_FilterDest_Object=MibTableColumn
filterDest=_FilterDest_Object((1,3,6,1,4,1,97,3,10,7,1,9),_FilterDest_Type())
filterDest.setMaxAccess(_C)
if mibBuilder.loadTexts:filterDest.setStatus(_A)
_FilterDestEnd_Type=OctetString
_FilterDestEnd_Object=MibTableColumn
filterDestEnd=_FilterDestEnd_Object((1,3,6,1,4,1,97,3,10,7,1,10),_FilterDestEnd_Type())
filterDestEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:filterDestEnd.setStatus(_A)
_FilterSourceMask_Type=OctetString
_FilterSourceMask_Object=MibTableColumn
filterSourceMask=_FilterSourceMask_Object((1,3,6,1,4,1,97,3,10,7,1,11),_FilterSourceMask_Type())
filterSourceMask.setMaxAccess(_C)
if mibBuilder.loadTexts:filterSourceMask.setStatus(_A)
_FilterDestMask_Type=OctetString
_FilterDestMask_Object=MibTableColumn
filterDestMask=_FilterDestMask_Object((1,3,6,1,4,1,97,3,10,7,1,12),_FilterDestMask_Type())
filterDestMask.setMaxAccess(_C)
if mibBuilder.loadTexts:filterDestMask.setStatus(_A)
_FilterSrcLan_Type=Integer32
_FilterSrcLan_Object=MibTableColumn
filterSrcLan=_FilterSrcLan_Object((1,3,6,1,4,1,97,3,10,7,1,13),_FilterSrcLan_Type())
filterSrcLan.setMaxAccess(_C)
if mibBuilder.loadTexts:filterSrcLan.setStatus(_A)
_FilterOffset_Type=Integer32
_FilterOffset_Object=MibTableColumn
filterOffset=_FilterOffset_Object((1,3,6,1,4,1,97,3,10,7,1,14),_FilterOffset_Type())
filterOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:filterOffset.setStatus(_A)
_FilterField_Type=OctetString
_FilterField_Object=MibTableColumn
filterField=_FilterField_Object((1,3,6,1,4,1,97,3,10,7,1,15),_FilterField_Type())
filterField.setMaxAccess(_C)
if mibBuilder.loadTexts:filterField.setStatus(_A)
_FilterMask_Type=OctetString
_FilterMask_Object=MibTableColumn
filterMask=_FilterMask_Object((1,3,6,1,4,1,97,3,10,7,1,16),_FilterMask_Type())
filterMask.setMaxAccess(_C)
if mibBuilder.loadTexts:filterMask.setStatus(_A)
_FilterThreshold_Type=Integer32
_FilterThreshold_Object=MibTableColumn
filterThreshold=_FilterThreshold_Object((1,3,6,1,4,1,97,3,10,7,1,17),_FilterThreshold_Type())
filterThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:filterThreshold.setStatus(_A)
_FilterThreshTime_Type=Integer32
_FilterThreshTime_Object=MibTableColumn
filterThreshTime=_FilterThreshTime_Object((1,3,6,1,4,1,97,3,10,7,1,18),_FilterThreshTime_Type())
filterThreshTime.setMaxAccess(_C)
if mibBuilder.loadTexts:filterThreshTime.setStatus(_A)
class _FilterThreshFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_FilterThreshFlag_Type.__name__=_D
_FilterThreshFlag_Object=MibTableColumn
filterThreshFlag=_FilterThreshFlag_Object((1,3,6,1,4,1,97,3,10,7,1,19),_FilterThreshFlag_Type())
filterThreshFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:filterThreshFlag.setStatus(_A)
_FilterPktCnts_Type=Counter32
_FilterPktCnts_Object=MibTableColumn
filterPktCnts=_FilterPktCnts_Object((1,3,6,1,4,1,97,3,10,7,1,20),_FilterPktCnts_Type())
filterPktCnts.setMaxAccess(_B)
if mibBuilder.loadTexts:filterPktCnts.setStatus(_A)
_FilterLastSrc_Type=OctetString
_FilterLastSrc_Object=MibTableColumn
filterLastSrc=_FilterLastSrc_Object((1,3,6,1,4,1,97,3,10,7,1,21),_FilterLastSrc_Type())
filterLastSrc.setMaxAccess(_B)
if mibBuilder.loadTexts:filterLastSrc.setStatus(_A)
_Reboot_ObjectIdentity=ObjectIdentity
reboot=_Reboot_ObjectIdentity((1,3,6,1,4,1,97,3,11))
_RebootBridgingMemory_Type=Integer32
_RebootBridgingMemory_Object=MibScalar
rebootBridgingMemory=_RebootBridgingMemory_Object((1,3,6,1,4,1,97,3,11,1),_RebootBridgingMemory_Type())
rebootBridgingMemory.setMaxAccess(_C)
if mibBuilder.loadTexts:rebootBridgingMemory.setStatus(_A)
_RebootSlotTable_Object=MibTable
rebootSlotTable=_RebootSlotTable_Object((1,3,6,1,4,1,97,3,11,2))
if mibBuilder.loadTexts:rebootSlotTable.setStatus(_A)
_RebootEntry_Object=MibTableRow
rebootEntry=_RebootEntry_Object((1,3,6,1,4,1,97,3,11,2,1))
rebootEntry.setIndexNames((0,_E,_A9))
if mibBuilder.loadTexts:rebootEntry.setStatus(_A)
_RebootIndex_Type=Integer32
_RebootIndex_Object=MibTableColumn
rebootIndex=_RebootIndex_Object((1,3,6,1,4,1,97,3,11,2,1,1),_RebootIndex_Type())
rebootIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rebootIndex.setStatus(_A)
class _RebootType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_Q,1),(_R,2),(_S,3),(_T,4),(_U,5),(_V,6),(_W,7),(_X,8),(_Y,9),(_Z,10),(_a,11),(_b,12)))
_RebootType_Type.__name__=_D
_RebootType_Object=MibTableColumn
rebootType=_RebootType_Object((1,3,6,1,4,1,97,3,11,2,1,2),_RebootType_Type())
rebootType.setMaxAccess(_C)
if mibBuilder.loadTexts:rebootType.setStatus(_A)
class _RebootUseMod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3)));namedValues=NamedValues(*(('reset',1),('run',3)))
_RebootUseMod_Type.__name__=_D
_RebootUseMod_Object=MibTableColumn
rebootUseMod=_RebootUseMod_Object((1,3,6,1,4,1,97,3,11,2,1,3),_RebootUseMod_Type())
rebootUseMod.setMaxAccess(_C)
if mibBuilder.loadTexts:rebootUseMod.setStatus(_A)
_RebootPortType_Type=OctetString
_RebootPortType_Object=MibTableColumn
rebootPortType=_RebootPortType_Object((1,3,6,1,4,1,97,3,11,2,1,4),_RebootPortType_Type())
rebootPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:rebootPortType.setStatus(_A)
class _RebootConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('no-change',1),('tftp-config',2),('revert-to-defaults',3)))
_RebootConfig_Type.__name__=_D
_RebootConfig_Object=MibScalar
rebootConfig=_RebootConfig_Object((1,3,6,1,4,1,97,3,11,3),_RebootConfig_Type())
rebootConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:rebootConfig.setStatus(_A)
_RebootRouteMemory_Type=Integer32
_RebootRouteMemory_Object=MibScalar
rebootRouteMemory=_RebootRouteMemory_Object((1,3,6,1,4,1,97,3,11,4),_RebootRouteMemory_Type())
rebootRouteMemory.setMaxAccess(_C)
if mibBuilder.loadTexts:rebootRouteMemory.setStatus(_A)
_Debug_ObjectIdentity=ObjectIdentity
debug=_Debug_ObjectIdentity((1,3,6,1,4,1,97,3,12))
_DebugStringID_Type=Integer32
_DebugStringID_Object=MibScalar
debugStringID=_DebugStringID_Object((1,3,6,1,4,1,97,3,12,1),_DebugStringID_Type())
debugStringID.setMaxAccess(_B)
if mibBuilder.loadTexts:debugStringID.setStatus(_A)
_DebugString_Type=OctetString
_DebugString_Object=MibScalar
debugString=_DebugString_Object((1,3,6,1,4,1,97,3,12,2),_DebugString_Type())
debugString.setMaxAccess(_B)
if mibBuilder.loadTexts:debugString.setStatus(_A)
_DebugTable_Object=MibTable
debugTable=_DebugTable_Object((1,3,6,1,4,1,97,3,12,3))
if mibBuilder.loadTexts:debugTable.setStatus(_A)
_DebugEntry_Object=MibTableRow
debugEntry=_DebugEntry_Object((1,3,6,1,4,1,97,3,12,3,1))
debugEntry.setIndexNames((0,_E,_AA))
if mibBuilder.loadTexts:debugEntry.setStatus(_A)
_DebugIndex_Type=Integer32
_DebugIndex_Object=MibTableColumn
debugIndex=_DebugIndex_Object((1,3,6,1,4,1,97,3,12,3,1,1),_DebugIndex_Type())
debugIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:debugIndex.setStatus(_A)
class _DebugOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('examine',1),('modify',2)))
_DebugOperation_Type.__name__=_D
_DebugOperation_Object=MibTableColumn
debugOperation=_DebugOperation_Object((1,3,6,1,4,1,97,3,12,3,1,2),_DebugOperation_Type())
debugOperation.setMaxAccess(_C)
if mibBuilder.loadTexts:debugOperation.setStatus(_A)
_DebugBase_Type=Integer32
_DebugBase_Object=MibTableColumn
debugBase=_DebugBase_Object((1,3,6,1,4,1,97,3,12,3,1,3),_DebugBase_Type())
debugBase.setMaxAccess(_C)
if mibBuilder.loadTexts:debugBase.setStatus(_A)
_DebugLength_Type=Integer32
_DebugLength_Object=MibTableColumn
debugLength=_DebugLength_Object((1,3,6,1,4,1,97,3,12,3,1,4),_DebugLength_Type())
debugLength.setMaxAccess(_C)
if mibBuilder.loadTexts:debugLength.setStatus(_A)
_DebugData_Type=OctetString
_DebugData_Object=MibTableColumn
debugData=_DebugData_Object((1,3,6,1,4,1,97,3,12,3,1,5),_DebugData_Type())
debugData.setMaxAccess(_C)
if mibBuilder.loadTexts:debugData.setStatus(_A)
_Lpbk_ObjectIdentity=ObjectIdentity
lpbk=_Lpbk_ObjectIdentity((1,3,6,1,4,1,97,3,13))
_LpbkTable_Object=MibTable
lpbkTable=_LpbkTable_Object((1,3,6,1,4,1,97,3,13,1))
if mibBuilder.loadTexts:lpbkTable.setStatus(_A)
_LpbkEntry_Object=MibTableRow
lpbkEntry=_LpbkEntry_Object((1,3,6,1,4,1,97,3,13,1,1))
lpbkEntry.setIndexNames((0,_E,_AB))
if mibBuilder.loadTexts:lpbkEntry.setStatus(_A)
_LpbkIndex_Type=Integer32
_LpbkIndex_Object=MibTableColumn
lpbkIndex=_LpbkIndex_Object((1,3,6,1,4,1,97,3,13,1,1,1),_LpbkIndex_Type())
lpbkIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lpbkIndex.setStatus(_A)
class _LpbkOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('loopback-off',1),('loopback-local',2),('loopback-remote',3)))
_LpbkOperation_Type.__name__=_D
_LpbkOperation_Object=MibTableColumn
lpbkOperation=_LpbkOperation_Object((1,3,6,1,4,1,97,3,13,1,1,2),_LpbkOperation_Type())
lpbkOperation.setMaxAccess(_C)
if mibBuilder.loadTexts:lpbkOperation.setStatus(_A)
_LpbkDestAddr_Type=OctetString
_LpbkDestAddr_Object=MibTableColumn
lpbkDestAddr=_LpbkDestAddr_Object((1,3,6,1,4,1,97,3,13,1,1,3),_LpbkDestAddr_Type())
lpbkDestAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:lpbkDestAddr.setStatus(_A)
_LpbkPktNum_Type=Integer32
_LpbkPktNum_Object=MibTableColumn
lpbkPktNum=_LpbkPktNum_Object((1,3,6,1,4,1,97,3,13,1,1,4),_LpbkPktNum_Type())
lpbkPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:lpbkPktNum.setStatus(_A)
_LpbkInterval_Type=TimeTicks
_LpbkInterval_Object=MibTableColumn
lpbkInterval=_LpbkInterval_Object((1,3,6,1,4,1,97,3,13,1,1,5),_LpbkInterval_Type())
lpbkInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:lpbkInterval.setStatus(_A)
_LpbkPktLength_Type=Integer32
_LpbkPktLength_Object=MibTableColumn
lpbkPktLength=_LpbkPktLength_Object((1,3,6,1,4,1,97,3,13,1,1,6),_LpbkPktLength_Type())
lpbkPktLength.setMaxAccess(_C)
if mibBuilder.loadTexts:lpbkPktLength.setStatus(_A)
_LpbkIncrements_Type=Integer32
_LpbkIncrements_Object=MibTableColumn
lpbkIncrements=_LpbkIncrements_Object((1,3,6,1,4,1,97,3,13,1,1,7),_LpbkIncrements_Type())
lpbkIncrements.setMaxAccess(_C)
if mibBuilder.loadTexts:lpbkIncrements.setStatus(_A)
_LpbkGoods_Type=Counter32
_LpbkGoods_Object=MibTableColumn
lpbkGoods=_LpbkGoods_Object((1,3,6,1,4,1,97,3,13,1,1,8),_LpbkGoods_Type())
lpbkGoods.setMaxAccess(_B)
if mibBuilder.loadTexts:lpbkGoods.setStatus(_A)
_LpbkErrorNoReceives_Type=Counter32
_LpbkErrorNoReceives_Object=MibTableColumn
lpbkErrorNoReceives=_LpbkErrorNoReceives_Object((1,3,6,1,4,1,97,3,13,1,1,9),_LpbkErrorNoReceives_Type())
lpbkErrorNoReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:lpbkErrorNoReceives.setStatus(_A)
_LpbkErrorBadReceives_Type=Counter32
_LpbkErrorBadReceives_Object=MibTableColumn
lpbkErrorBadReceives=_LpbkErrorBadReceives_Object((1,3,6,1,4,1,97,3,13,1,1,10),_LpbkErrorBadReceives_Type())
lpbkErrorBadReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:lpbkErrorBadReceives.setStatus(_A)
_LpbkErrorSize_Type=Integer32
_LpbkErrorSize_Object=MibTableColumn
lpbkErrorSize=_LpbkErrorSize_Object((1,3,6,1,4,1,97,3,13,1,1,11),_LpbkErrorSize_Type())
lpbkErrorSize.setMaxAccess(_B)
if mibBuilder.loadTexts:lpbkErrorSize.setStatus(_A)
_LpbkErrorSent_Type=OctetString
_LpbkErrorSent_Object=MibTableColumn
lpbkErrorSent=_LpbkErrorSent_Object((1,3,6,1,4,1,97,3,13,1,1,12),_LpbkErrorSent_Type())
lpbkErrorSent.setMaxAccess(_B)
if mibBuilder.loadTexts:lpbkErrorSent.setStatus(_A)
_LpbkErrorReceived_Type=OctetString
_LpbkErrorReceived_Object=MibTableColumn
lpbkErrorReceived=_LpbkErrorReceived_Object((1,3,6,1,4,1,97,3,13,1,1,13),_LpbkErrorReceived_Type())
lpbkErrorReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:lpbkErrorReceived.setStatus(_A)
_LpbkErrorOffset_Type=Integer32
_LpbkErrorOffset_Object=MibTableColumn
lpbkErrorOffset=_LpbkErrorOffset_Object((1,3,6,1,4,1,97,3,13,1,1,14),_LpbkErrorOffset_Type())
lpbkErrorOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:lpbkErrorOffset.setStatus(_A)
_Swan_ObjectIdentity=ObjectIdentity
swan=_Swan_ObjectIdentity((1,3,6,1,4,1,97,3,14))
_SwanTable_Object=MibTable
swanTable=_SwanTable_Object((1,3,6,1,4,1,97,3,14,1))
if mibBuilder.loadTexts:swanTable.setStatus(_A)
_SwanEntry_Object=MibTableRow
swanEntry=_SwanEntry_Object((1,3,6,1,4,1,97,3,14,1,1))
swanEntry.setIndexNames((0,_E,_AC))
if mibBuilder.loadTexts:swanEntry.setStatus(_A)
_SwanIndex_Type=Integer32
_SwanIndex_Object=MibTableColumn
swanIndex=_SwanIndex_Object((1,3,6,1,4,1,97,3,14,1,1,1),_SwanIndex_Type())
swanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:swanIndex.setStatus(_A)
_SwanDesiredSpeed_Type=Integer32
_SwanDesiredSpeed_Object=MibTableColumn
swanDesiredSpeed=_SwanDesiredSpeed_Object((1,3,6,1,4,1,97,3,14,1,1,2),_SwanDesiredSpeed_Type())
swanDesiredSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:swanDesiredSpeed.setStatus(_A)
class _SwanActualSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_y,2),(_z,3),(_A0,4),(_A1,5),(_A2,6),(_A3,7),(_A4,8),(_A5,9),(_A6,10),(_A7,11)))
_SwanActualSpeed_Type.__name__=_D
_SwanActualSpeed_Object=MibTableColumn
swanActualSpeed=_SwanActualSpeed_Object((1,3,6,1,4,1,97,3,14,1,1,3),_SwanActualSpeed_Type())
swanActualSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:swanActualSpeed.setStatus(_A)
_SwanIpNeighborAddress_Type=IpAddress
_SwanIpNeighborAddress_Object=MibTableColumn
swanIpNeighborAddress=_SwanIpNeighborAddress_Object((1,3,6,1,4,1,97,3,14,1,1,4),_SwanIpNeighborAddress_Type())
swanIpNeighborAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:swanIpNeighborAddress.setStatus(_A)
class _SwanPPPActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwanPPPActive_Type.__name__=_D
_SwanPPPActive_Object=MibTableColumn
swanPPPActive=_SwanPPPActive_Object((1,3,6,1,4,1,97,3,14,1,1,5),_SwanPPPActive_Type())
swanPPPActive.setMaxAccess(_C)
if mibBuilder.loadTexts:swanPPPActive.setStatus(_A)
_SwanAlignmentErrors_Type=Counter32
_SwanAlignmentErrors_Object=MibTableColumn
swanAlignmentErrors=_SwanAlignmentErrors_Object((1,3,6,1,4,1,97,3,14,1,1,6),_SwanAlignmentErrors_Type())
swanAlignmentErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:swanAlignmentErrors.setStatus(_A)
_SwanOverrunErrors_Type=Counter32
_SwanOverrunErrors_Object=MibTableColumn
swanOverrunErrors=_SwanOverrunErrors_Object((1,3,6,1,4,1,97,3,14,1,1,7),_SwanOverrunErrors_Type())
swanOverrunErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:swanOverrunErrors.setStatus(_A)
class _SwanPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('wan-unknown',1),('wan-v11',2),('wan-v24',3),('wan-v35',4),('wan-e1',5),('wan-t1',6),('wan-rs530',7),('wan-t3',8)))
_SwanPortType_Type.__name__=_D
_SwanPortType_Object=MibTableColumn
swanPortType=_SwanPortType_Object((1,3,6,1,4,1,97,3,14,1,1,8),_SwanPortType_Type())
swanPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:swanPortType.setStatus(_A)
_SwanLinkCost_Type=Integer32
_SwanLinkCost_Object=MibTableColumn
swanLinkCost=_SwanLinkCost_Object((1,3,6,1,4,1,97,3,14,1,1,9),_SwanLinkCost_Type())
swanLinkCost.setMaxAccess(_B)
if mibBuilder.loadTexts:swanLinkCost.setStatus(_A)
class _SwanMeshState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwanMeshState_Type.__name__=_D
_SwanMeshState_Object=MibTableColumn
swanMeshState=_SwanMeshState_Object((1,3,6,1,4,1,97,3,14,1,1,10),_SwanMeshState_Type())
swanMeshState.setMaxAccess(_B)
if mibBuilder.loadTexts:swanMeshState.setStatus(_A)
_SwanLinkSubnet_Type=OctetString
_SwanLinkSubnet_Object=MibTableColumn
swanLinkSubnet=_SwanLinkSubnet_Object((1,3,6,1,4,1,97,3,14,1,1,11),_SwanLinkSubnet_Type())
swanLinkSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:swanLinkSubnet.setStatus(_A)
_SwanLinkBridge_Type=OctetString
_SwanLinkBridge_Object=MibTableColumn
swanLinkBridge=_SwanLinkBridge_Object((1,3,6,1,4,1,97,3,14,1,1,12),_SwanLinkBridge_Type())
swanLinkBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:swanLinkBridge.setStatus(_A)
_SwanLinkPort_Type=Integer32
_SwanLinkPort_Object=MibTableColumn
swanLinkPort=_SwanLinkPort_Object((1,3,6,1,4,1,97,3,14,1,1,13),_SwanLinkPort_Type())
swanLinkPort.setMaxAccess(_B)
if mibBuilder.loadTexts:swanLinkPort.setStatus(_A)
class _SwanNegotiate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwanNegotiate_Type.__name__=_D
_SwanNegotiate_Object=MibTableColumn
swanNegotiate=_SwanNegotiate_Object((1,3,6,1,4,1,97,3,14,1,1,14),_SwanNegotiate_Type())
swanNegotiate.setMaxAccess(_C)
if mibBuilder.loadTexts:swanNegotiate.setStatus(_A)
class _SwanSwitches_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('wan-hssi',1),('wan-t1',2),('wan-hssi-switching-disabled',3),('wan-t1-switching-disabled',4)))
_SwanSwitches_Type.__name__=_D
_SwanSwitches_Object=MibTableColumn
swanSwitches=_SwanSwitches_Object((1,3,6,1,4,1,97,3,14,1,1,15),_SwanSwitches_Type())
swanSwitches.setMaxAccess(_C)
if mibBuilder.loadTexts:swanSwitches.setStatus(_A)
_SwanDCEDrops_Type=Counter32
_SwanDCEDrops_Object=MibTableColumn
swanDCEDrops=_SwanDCEDrops_Object((1,3,6,1,4,1,97,3,14,1,1,16),_SwanDCEDrops_Type())
swanDCEDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:swanDCEDrops.setStatus(_A)
class _SwanOutPacketType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('token-ring-without-FCS',1),('token-ring-with-FCS',2),('ethernet-without-FCS',3),('ethernet-with-FCS',4)))
_SwanOutPacketType_Type.__name__=_D
_SwanOutPacketType_Object=MibTableColumn
swanOutPacketType=_SwanOutPacketType_Object((1,3,6,1,4,1,97,3,14,1,1,17),_SwanOutPacketType_Type())
swanOutPacketType.setMaxAccess(_C)
if mibBuilder.loadTexts:swanOutPacketType.setStatus(_A)
class _SwanLinkErrorPercentage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_SwanLinkErrorPercentage_Type.__name__=_D
_SwanLinkErrorPercentage_Object=MibTableColumn
swanLinkErrorPercentage=_SwanLinkErrorPercentage_Object((1,3,6,1,4,1,97,3,14,1,1,18),_SwanLinkErrorPercentage_Type())
swanLinkErrorPercentage.setMaxAccess(_C)
if mibBuilder.loadTexts:swanLinkErrorPercentage.setStatus(_A)
class _SwanLinkErrorDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_SwanLinkErrorDuration_Type.__name__=_D
_SwanLinkErrorDuration_Object=MibTableColumn
swanLinkErrorDuration=_SwanLinkErrorDuration_Object((1,3,6,1,4,1,97,3,14,1,1,19),_SwanLinkErrorDuration_Type())
swanLinkErrorDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:swanLinkErrorDuration.setStatus(_A)
class _SwanLinkErrorFailPeriods_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_SwanLinkErrorFailPeriods_Type.__name__=_D
_SwanLinkErrorFailPeriods_Object=MibTableColumn
swanLinkErrorFailPeriods=_SwanLinkErrorFailPeriods_Object((1,3,6,1,4,1,97,3,14,1,1,20),_SwanLinkErrorFailPeriods_Type())
swanLinkErrorFailPeriods.setMaxAccess(_C)
if mibBuilder.loadTexts:swanLinkErrorFailPeriods.setStatus(_A)
class _SwanLinkErrorMaxPeriods_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_SwanLinkErrorMaxPeriods_Type.__name__=_D
_SwanLinkErrorMaxPeriods_Object=MibTableColumn
swanLinkErrorMaxPeriods=_SwanLinkErrorMaxPeriods_Object((1,3,6,1,4,1,97,3,14,1,1,21),_SwanLinkErrorMaxPeriods_Type())
swanLinkErrorMaxPeriods.setMaxAccess(_C)
if mibBuilder.loadTexts:swanLinkErrorMaxPeriods.setStatus(_A)
class _SwanLinkRestartTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_SwanLinkRestartTime_Type.__name__=_D
_SwanLinkRestartTime_Object=MibTableColumn
swanLinkRestartTime=_SwanLinkRestartTime_Object((1,3,6,1,4,1,97,3,14,1,1,22),_SwanLinkRestartTime_Type())
swanLinkRestartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swanLinkRestartTime.setStatus(_A)
class _SwanPreserveFCS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwanPreserveFCS_Type.__name__=_D
_SwanPreserveFCS_Object=MibTableColumn
swanPreserveFCS=_SwanPreserveFCS_Object((1,3,6,1,4,1,97,3,14,1,1,23),_SwanPreserveFCS_Type())
swanPreserveFCS.setMaxAccess(_C)
if mibBuilder.loadTexts:swanPreserveFCS.setStatus(_A)
_Srepeater_ObjectIdentity=ObjectIdentity
srepeater=_Srepeater_ObjectIdentity((1,3,6,1,4,1,97,3,16))
_SrepeaterTable_Object=MibTable
srepeaterTable=_SrepeaterTable_Object((1,3,6,1,4,1,97,3,16,1))
if mibBuilder.loadTexts:srepeaterTable.setStatus(_A)
_SrepeaterEntry_Object=MibTableRow
srepeaterEntry=_SrepeaterEntry_Object((1,3,6,1,4,1,97,3,16,1,1))
srepeaterEntry.setIndexNames((0,_E,_AD))
if mibBuilder.loadTexts:srepeaterEntry.setStatus(_A)
class _SrepeaterGroupID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_SrepeaterGroupID_Type.__name__=_D
_SrepeaterGroupID_Object=MibTableColumn
srepeaterGroupID=_SrepeaterGroupID_Object((1,3,6,1,4,1,97,3,16,1,1,1),_SrepeaterGroupID_Type())
srepeaterGroupID.setMaxAccess(_B)
if mibBuilder.loadTexts:srepeaterGroupID.setStatus(_A)
_SrepeaterLinkStatusMask_Type=Integer32
_SrepeaterLinkStatusMask_Object=MibTableColumn
srepeaterLinkStatusMask=_SrepeaterLinkStatusMask_Object((1,3,6,1,4,1,97,3,16,1,1,2),_SrepeaterLinkStatusMask_Type())
srepeaterLinkStatusMask.setMaxAccess(_B)
if mibBuilder.loadTexts:srepeaterLinkStatusMask.setStatus(_A)
class _SrepeaterExtendedStats_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_SrepeaterExtendedStats_Type.__name__=_D
_SrepeaterExtendedStats_Object=MibTableColumn
srepeaterExtendedStats=_SrepeaterExtendedStats_Object((1,3,6,1,4,1,97,3,16,1,1,3),_SrepeaterExtendedStats_Type())
srepeaterExtendedStats.setMaxAccess(_C)
if mibBuilder.loadTexts:srepeaterExtendedStats.setStatus(_A)
_SrepeaterPortTable_Object=MibTable
srepeaterPortTable=_SrepeaterPortTable_Object((1,3,6,1,4,1,97,3,16,2))
if mibBuilder.loadTexts:srepeaterPortTable.setStatus(_A)
_SrepeaterPortEntry_Object=MibTableRow
srepeaterPortEntry=_SrepeaterPortEntry_Object((1,3,6,1,4,1,97,3,16,2,1))
srepeaterPortEntry.setIndexNames((0,_E,_AE),(0,_E,_AF))
if mibBuilder.loadTexts:srepeaterPortEntry.setStatus(_A)
class _SrepeaterPortGroupID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_SrepeaterPortGroupID_Type.__name__=_D
_SrepeaterPortGroupID_Object=MibTableColumn
srepeaterPortGroupID=_SrepeaterPortGroupID_Object((1,3,6,1,4,1,97,3,16,2,1,1),_SrepeaterPortGroupID_Type())
srepeaterPortGroupID.setMaxAccess(_B)
if mibBuilder.loadTexts:srepeaterPortGroupID.setStatus(_A)
_SrepeaterPortPortID_Type=Integer32
_SrepeaterPortPortID_Object=MibTableColumn
srepeaterPortPortID=_SrepeaterPortPortID_Object((1,3,6,1,4,1,97,3,16,2,1,2),_SrepeaterPortPortID_Type())
srepeaterPortPortID.setMaxAccess(_B)
if mibBuilder.loadTexts:srepeaterPortPortID.setStatus(_A)
class _SrepeaterPortLinkPulse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_SrepeaterPortLinkPulse_Type.__name__=_D
_SrepeaterPortLinkPulse_Object=MibTableColumn
srepeaterPortLinkPulse=_SrepeaterPortLinkPulse_Object((1,3,6,1,4,1,97,3,16,2,1,3),_SrepeaterPortLinkPulse_Type())
srepeaterPortLinkPulse.setMaxAccess(_C)
if mibBuilder.loadTexts:srepeaterPortLinkPulse.setStatus(_A)
_Sproto_ObjectIdentity=ObjectIdentity
sproto=_Sproto_ObjectIdentity((1,3,6,1,4,1,97,3,17))
_SprotoTable_Object=MibTable
sprotoTable=_SprotoTable_Object((1,3,6,1,4,1,97,3,17,1))
if mibBuilder.loadTexts:sprotoTable.setStatus(_A)
_SprotoEntry_Object=MibTableRow
sprotoEntry=_SprotoEntry_Object((1,3,6,1,4,1,97,3,17,1,1))
sprotoEntry.setIndexNames((0,_E,_AG))
if mibBuilder.loadTexts:sprotoEntry.setStatus(_A)
_SprotoIfIndex_Type=Integer32
_SprotoIfIndex_Object=MibTableColumn
sprotoIfIndex=_SprotoIfIndex_Object((1,3,6,1,4,1,97,3,17,1,1,1),_SprotoIfIndex_Type())
sprotoIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sprotoIfIndex.setStatus(_A)
class _SprotoBridge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('transparent',1),('sr',2),('srt',3),(_J,4)))
_SprotoBridge_Type.__name__=_D
_SprotoBridge_Object=MibTableColumn
sprotoBridge=_SprotoBridge_Object((1,3,6,1,4,1,97,3,17,1,1,2),_SprotoBridge_Type())
sprotoBridge.setMaxAccess(_C)
if mibBuilder.loadTexts:sprotoBridge.setStatus(_A)
class _SprotoSuppressBpdus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('suppressed',2)))
_SprotoSuppressBpdus_Type.__name__=_D
_SprotoSuppressBpdus_Object=MibTableColumn
sprotoSuppressBpdus=_SprotoSuppressBpdus_Object((1,3,6,1,4,1,97,3,17,1,1,3),_SprotoSuppressBpdus_Type())
sprotoSuppressBpdus.setMaxAccess(_C)
if mibBuilder.loadTexts:sprotoSuppressBpdus.setStatus(_A)
class _SprotoIpRoute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_SprotoIpRoute_Type.__name__=_D
_SprotoIpRoute_Object=MibTableColumn
sprotoIpRoute=_SprotoIpRoute_Object((1,3,6,1,4,1,97,3,17,1,1,4),_SprotoIpRoute_Type())
sprotoIpRoute.setMaxAccess(_C)
if mibBuilder.loadTexts:sprotoIpRoute.setStatus(_A)
class _SprotoIpxRoute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),('ipxsr',3)))
_SprotoIpxRoute_Type.__name__=_D
_SprotoIpxRoute_Object=MibTableColumn
sprotoIpxRoute=_SprotoIpxRoute_Object((1,3,6,1,4,1,97,3,17,1,1,5),_SprotoIpxRoute_Type())
sprotoIpxRoute.setMaxAccess(_C)
if mibBuilder.loadTexts:sprotoIpxRoute.setStatus(_A)
class _SprotoAppleRoute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_SprotoAppleRoute_Type.__name__=_D
_SprotoAppleRoute_Object=MibTableColumn
sprotoAppleRoute=_SprotoAppleRoute_Object((1,3,6,1,4,1,97,3,17,1,1,6),_SprotoAppleRoute_Type())
sprotoAppleRoute.setMaxAccess(_C)
if mibBuilder.loadTexts:sprotoAppleRoute.setStatus(_A)
class _SprotoArpTranslate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_J,1),('bitswap1',2),('bitswap6',3),('bitswap61',4),('oneto6',5),('oneto6swap',6)))
_SprotoArpTranslate_Type.__name__=_D
_SprotoArpTranslate_Object=MibTableColumn
sprotoArpTranslate=_SprotoArpTranslate_Object((1,3,6,1,4,1,97,3,17,1,1,7),_SprotoArpTranslate_Type())
sprotoArpTranslate.setMaxAccess(_C)
if mibBuilder.loadTexts:sprotoArpTranslate.setStatus(_A)
class _SprotoArpSourceRoute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3),(_J,4)))
_SprotoArpSourceRoute_Type.__name__=_D
_SprotoArpSourceRoute_Object=MibTableColumn
sprotoArpSourceRoute=_SprotoArpSourceRoute_Object((1,3,6,1,4,1,97,3,17,1,1,8),_SprotoArpSourceRoute_Type())
sprotoArpSourceRoute.setMaxAccess(_C)
if mibBuilder.loadTexts:sprotoArpSourceRoute.setStatus(_A)
class _SprotoIpxTranslate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_SprotoIpxTranslate_Type.__name__=_D
_SprotoIpxTranslate_Object=MibTableColumn
sprotoIpxTranslate=_SprotoIpxTranslate_Object((1,3,6,1,4,1,97,3,17,1,1,9),_SprotoIpxTranslate_Type())
sprotoIpxTranslate.setMaxAccess(_C)
if mibBuilder.loadTexts:sprotoIpxTranslate.setStatus(_A)
class _SprotoAppleTranslate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_SprotoAppleTranslate_Type.__name__=_D
_SprotoAppleTranslate_Object=MibTableColumn
sprotoAppleTranslate=_SprotoAppleTranslate_Object((1,3,6,1,4,1,97,3,17,1,1,10),_SprotoAppleTranslate_Type())
sprotoAppleTranslate.setMaxAccess(_C)
if mibBuilder.loadTexts:sprotoAppleTranslate.setStatus(_A)
class _SprotoIbmLlcTranslate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_SprotoIbmLlcTranslate_Type.__name__=_D
_SprotoIbmLlcTranslate_Object=MibTableColumn
sprotoIbmLlcTranslate=_SprotoIbmLlcTranslate_Object((1,3,6,1,4,1,97,3,17,1,1,11),_SprotoIbmLlcTranslate_Type())
sprotoIbmLlcTranslate.setMaxAccess(_C)
if mibBuilder.loadTexts:sprotoIbmLlcTranslate.setStatus(_A)
class _SprotoRip_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_SprotoRip_Type.__name__=_D
_SprotoRip_Object=MibTableColumn
sprotoRip=_SprotoRip_Object((1,3,6,1,4,1,97,3,17,1,1,12),_SprotoRip_Type())
sprotoRip.setMaxAccess(_C)
if mibBuilder.loadTexts:sprotoRip.setStatus(_A)
class _SprotoEgp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_SprotoEgp_Type.__name__=_D
_SprotoEgp_Object=MibTableColumn
sprotoEgp=_SprotoEgp_Object((1,3,6,1,4,1,97,3,17,1,1,13),_SprotoEgp_Type())
sprotoEgp.setMaxAccess(_C)
if mibBuilder.loadTexts:sprotoEgp.setStatus(_A)
class _SprotoOspf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_SprotoOspf_Type.__name__=_D
_SprotoOspf_Object=MibTableColumn
sprotoOspf=_SprotoOspf_Object((1,3,6,1,4,1,97,3,17,1,1,14),_SprotoOspf_Type())
sprotoOspf.setMaxAccess(_C)
if mibBuilder.loadTexts:sprotoOspf.setStatus(_A)
class _SprotoArpProxy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_SprotoArpProxy_Type.__name__=_D
_SprotoArpProxy_Object=MibTableColumn
sprotoArpProxy=_SprotoArpProxy_Object((1,3,6,1,4,1,97,3,17,1,1,15),_SprotoArpProxy_Type())
sprotoArpProxy.setMaxAccess(_C)
if mibBuilder.loadTexts:sprotoArpProxy.setStatus(_A)
_SprotoIbm8209Lsaps_Type=OctetString
_SprotoIbm8209Lsaps_Object=MibTableColumn
sprotoIbm8209Lsaps=_SprotoIbm8209Lsaps_Object((1,3,6,1,4,1,97,3,17,1,1,16),_SprotoIbm8209Lsaps_Type())
sprotoIbm8209Lsaps.setMaxAccess(_C)
if mibBuilder.loadTexts:sprotoIbm8209Lsaps.setStatus(_A)
class _SprotoBootpRelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_SprotoBootpRelay_Type.__name__=_D
_SprotoBootpRelay_Object=MibTableColumn
sprotoBootpRelay=_SprotoBootpRelay_Object((1,3,6,1,4,1,97,3,17,1,1,17),_SprotoBootpRelay_Type())
sprotoBootpRelay.setMaxAccess(_C)
if mibBuilder.loadTexts:sprotoBootpRelay.setStatus(_A)
class _SprotoNetbiosTranslate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3),(_J,4)))
_SprotoNetbiosTranslate_Type.__name__=_D
_SprotoNetbiosTranslate_Object=MibTableColumn
sprotoNetbiosTranslate=_SprotoNetbiosTranslate_Object((1,3,6,1,4,1,97,3,17,1,1,18),_SprotoNetbiosTranslate_Type())
sprotoNetbiosTranslate.setMaxAccess(_C)
if mibBuilder.loadTexts:sprotoNetbiosTranslate.setStatus(_A)
class _SprotoIpMulticast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_SprotoIpMulticast_Type.__name__=_D
_SprotoIpMulticast_Object=MibTableColumn
sprotoIpMulticast=_SprotoIpMulticast_Object((1,3,6,1,4,1,97,3,17,1,1,19),_SprotoIpMulticast_Type())
sprotoIpMulticast.setMaxAccess(_C)
if mibBuilder.loadTexts:sprotoIpMulticast.setStatus(_A)
class _SprotoTrunking_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_SprotoTrunking_Type.__name__=_D
_SprotoTrunking_Object=MibTableColumn
sprotoTrunking=_SprotoTrunking_Object((1,3,6,1,4,1,97,3,17,1,1,20),_SprotoTrunking_Type())
sprotoTrunking.setMaxAccess(_C)
if mibBuilder.loadTexts:sprotoTrunking.setStatus(_A)
class _SprotoIpxSrTranslate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3),(_J,4)))
_SprotoIpxSrTranslate_Type.__name__=_D
_SprotoIpxSrTranslate_Object=MibTableColumn
sprotoIpxSrTranslate=_SprotoIpxSrTranslate_Object((1,3,6,1,4,1,97,3,17,1,1,22),_SprotoIpxSrTranslate_Type())
sprotoIpxSrTranslate.setMaxAccess(_C)
if mibBuilder.loadTexts:sprotoIpxSrTranslate.setStatus(_A)
class _SprotoAllTranslate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3),(_J,4)))
_SprotoAllTranslate_Type.__name__=_D
_SprotoAllTranslate_Object=MibTableColumn
sprotoAllTranslate=_SprotoAllTranslate_Object((1,3,6,1,4,1,97,3,17,1,1,23),_SprotoAllTranslate_Type())
sprotoAllTranslate.setMaxAccess(_C)
if mibBuilder.loadTexts:sprotoAllTranslate.setStatus(_A)
class _SprotoSteHopCountAppliedRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('hopcountnotapplied',1),('hopcountapplied',2)))
_SprotoSteHopCountAppliedRule_Type.__name__=_D
_SprotoSteHopCountAppliedRule_Object=MibTableColumn
sprotoSteHopCountAppliedRule=_SprotoSteHopCountAppliedRule_Object((1,3,6,1,4,1,97,3,17,1,1,24),_SprotoSteHopCountAppliedRule_Type())
sprotoSteHopCountAppliedRule.setMaxAccess(_C)
if mibBuilder.loadTexts:sprotoSteHopCountAppliedRule.setStatus(_A)
class _SprotoIpxDot3Framing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_AH,1),(_AI,2),('ethernet8022',3)))
_SprotoIpxDot3Framing_Type.__name__=_D
_SprotoIpxDot3Framing_Object=MibScalar
sprotoIpxDot3Framing=_SprotoIpxDot3Framing_Object((1,3,6,1,4,1,97,3,17,2),_SprotoIpxDot3Framing_Type())
sprotoIpxDot3Framing.setMaxAccess(_C)
if mibBuilder.loadTexts:sprotoIpxDot3Framing.setStatus(_A)
_Sipx_ObjectIdentity=ObjectIdentity
sipx=_Sipx_ObjectIdentity((1,3,6,1,4,1,97,3,18))
_SipxIfTable_Object=MibTable
sipxIfTable=_SipxIfTable_Object((1,3,6,1,4,1,97,3,18,1))
if mibBuilder.loadTexts:sipxIfTable.setStatus(_A)
_SipxIfEntry_Object=MibTableRow
sipxIfEntry=_SipxIfEntry_Object((1,3,6,1,4,1,97,3,18,1,1))
sipxIfEntry.setIndexNames((0,_E,_AJ))
if mibBuilder.loadTexts:sipxIfEntry.setStatus(_A)
_SipxIfIndex_Type=Integer32
_SipxIfIndex_Object=MibTableColumn
sipxIfIndex=_SipxIfIndex_Object((1,3,6,1,4,1,97,3,18,1,1,1),_SipxIfIndex_Type())
sipxIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sipxIfIndex.setStatus(_A)
_SipxIfNetwork_Type=OctetString
_SipxIfNetwork_Object=MibTableColumn
sipxIfNetwork=_SipxIfNetwork_Object((1,3,6,1,4,1,97,3,18,1,1,2),_SipxIfNetwork_Type())
sipxIfNetwork.setMaxAccess(_C)
if mibBuilder.loadTexts:sipxIfNetwork.setStatus(_A)
class _SipxIfFraming_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_AH,1),(_AI,2),('ieee8022',3),('snap',4),('rawfddi',5),('ppp',6)))
_SipxIfFraming_Type.__name__=_D
_SipxIfFraming_Object=MibTableColumn
sipxIfFraming=_SipxIfFraming_Object((1,3,6,1,4,1,97,3,18,1,1,3),_SipxIfFraming_Type())
sipxIfFraming.setMaxAccess(_C)
if mibBuilder.loadTexts:sipxIfFraming.setStatus(_A)
_SipxIfInRipPkts_Type=Counter32
_SipxIfInRipPkts_Object=MibTableColumn
sipxIfInRipPkts=_SipxIfInRipPkts_Object((1,3,6,1,4,1,97,3,18,1,1,4),_SipxIfInRipPkts_Type())
sipxIfInRipPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sipxIfInRipPkts.setStatus(_A)
_SipxIfOutRipPkts_Type=Counter32
_SipxIfOutRipPkts_Object=MibTableColumn
sipxIfOutRipPkts=_SipxIfOutRipPkts_Object((1,3,6,1,4,1,97,3,18,1,1,5),_SipxIfOutRipPkts_Type())
sipxIfOutRipPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sipxIfOutRipPkts.setStatus(_A)
_SipxIfInSapPkts_Type=Counter32
_SipxIfInSapPkts_Object=MibTableColumn
sipxIfInSapPkts=_SipxIfInSapPkts_Object((1,3,6,1,4,1,97,3,18,1,1,6),_SipxIfInSapPkts_Type())
sipxIfInSapPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sipxIfInSapPkts.setStatus(_A)
_SipxIfOutSapPkts_Type=Counter32
_SipxIfOutSapPkts_Object=MibTableColumn
sipxIfOutSapPkts=_SipxIfOutSapPkts_Object((1,3,6,1,4,1,97,3,18,1,1,7),_SipxIfOutSapPkts_Type())
sipxIfOutSapPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sipxIfOutSapPkts.setStatus(_A)
_SipxRouteTable_Object=MibTable
sipxRouteTable=_SipxRouteTable_Object((1,3,6,1,4,1,97,3,18,2))
if mibBuilder.loadTexts:sipxRouteTable.setStatus(_A)
_SipxRouteEntry_Object=MibTableRow
sipxRouteEntry=_SipxRouteEntry_Object((1,3,6,1,4,1,97,3,18,2,1))
sipxRouteEntry.setIndexNames((0,_E,_AK))
if mibBuilder.loadTexts:sipxRouteEntry.setStatus(_A)
_SipxRouteDest_Type=OctetString
_SipxRouteDest_Object=MibTableColumn
sipxRouteDest=_SipxRouteDest_Object((1,3,6,1,4,1,97,3,18,2,1,1),_SipxRouteDest_Type())
sipxRouteDest.setMaxAccess(_B)
if mibBuilder.loadTexts:sipxRouteDest.setStatus(_A)
_SipxRouteIfIndex_Type=Integer32
_SipxRouteIfIndex_Object=MibTableColumn
sipxRouteIfIndex=_SipxRouteIfIndex_Object((1,3,6,1,4,1,97,3,18,2,1,2),_SipxRouteIfIndex_Type())
sipxRouteIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sipxRouteIfIndex.setStatus(_A)
_SipxRouteTickCount_Type=Integer32
_SipxRouteTickCount_Object=MibTableColumn
sipxRouteTickCount=_SipxRouteTickCount_Object((1,3,6,1,4,1,97,3,18,2,1,3),_SipxRouteTickCount_Type())
sipxRouteTickCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sipxRouteTickCount.setStatus(_A)
_SipxRouteHopCount_Type=Integer32
_SipxRouteHopCount_Object=MibTableColumn
sipxRouteHopCount=_SipxRouteHopCount_Object((1,3,6,1,4,1,97,3,18,2,1,4),_SipxRouteHopCount_Type())
sipxRouteHopCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sipxRouteHopCount.setStatus(_A)
_SipxRouteNextHop_Type=OctetString
_SipxRouteNextHop_Object=MibTableColumn
sipxRouteNextHop=_SipxRouteNextHop_Object((1,3,6,1,4,1,97,3,18,2,1,5),_SipxRouteNextHop_Type())
sipxRouteNextHop.setMaxAccess(_B)
if mibBuilder.loadTexts:sipxRouteNextHop.setStatus(_A)
_SipxRouteAge_Type=Integer32
_SipxRouteAge_Object=MibTableColumn
sipxRouteAge=_SipxRouteAge_Object((1,3,6,1,4,1,97,3,18,2,1,6),_SipxRouteAge_Type())
sipxRouteAge.setMaxAccess(_B)
if mibBuilder.loadTexts:sipxRouteAge.setStatus(_A)
_SipxSapTable_Object=MibTable
sipxSapTable=_SipxSapTable_Object((1,3,6,1,4,1,97,3,18,3))
if mibBuilder.loadTexts:sipxSapTable.setStatus(_A)
_SipxSapEntry_Object=MibTableRow
sipxSapEntry=_SipxSapEntry_Object((1,3,6,1,4,1,97,3,18,3,1))
sipxSapEntry.setIndexNames((0,_E,_AL))
if mibBuilder.loadTexts:sipxSapEntry.setStatus(_A)
_SipxSapIndex_Type=Integer32
_SipxSapIndex_Object=MibTableColumn
sipxSapIndex=_SipxSapIndex_Object((1,3,6,1,4,1,97,3,18,3,1,1),_SipxSapIndex_Type())
sipxSapIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sipxSapIndex.setStatus(_A)
_SipxSapType_Type=Integer32
_SipxSapType_Object=MibTableColumn
sipxSapType=_SipxSapType_Object((1,3,6,1,4,1,97,3,18,3,1,2),_SipxSapType_Type())
sipxSapType.setMaxAccess(_B)
if mibBuilder.loadTexts:sipxSapType.setStatus(_A)
_SipxSapName_Type=OctetString
_SipxSapName_Object=MibTableColumn
sipxSapName=_SipxSapName_Object((1,3,6,1,4,1,97,3,18,3,1,3),_SipxSapName_Type())
sipxSapName.setMaxAccess(_B)
if mibBuilder.loadTexts:sipxSapName.setStatus(_A)
_SipxSapNetwork_Type=OctetString
_SipxSapNetwork_Object=MibTableColumn
sipxSapNetwork=_SipxSapNetwork_Object((1,3,6,1,4,1,97,3,18,3,1,4),_SipxSapNetwork_Type())
sipxSapNetwork.setMaxAccess(_B)
if mibBuilder.loadTexts:sipxSapNetwork.setStatus(_A)
_SipxSapNodeId_Type=OctetString
_SipxSapNodeId_Object=MibTableColumn
sipxSapNodeId=_SipxSapNodeId_Object((1,3,6,1,4,1,97,3,18,3,1,5),_SipxSapNodeId_Type())
sipxSapNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:sipxSapNodeId.setStatus(_A)
_SipxSapSocket_Type=Integer32
_SipxSapSocket_Object=MibTableColumn
sipxSapSocket=_SipxSapSocket_Object((1,3,6,1,4,1,97,3,18,3,1,6),_SipxSapSocket_Type())
sipxSapSocket.setMaxAccess(_B)
if mibBuilder.loadTexts:sipxSapSocket.setStatus(_A)
_SipxSapHopCount_Type=Integer32
_SipxSapHopCount_Object=MibTableColumn
sipxSapHopCount=_SipxSapHopCount_Object((1,3,6,1,4,1,97,3,18,3,1,7),_SipxSapHopCount_Type())
sipxSapHopCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sipxSapHopCount.setStatus(_A)
_SipxDiscardedRoutes_Type=Counter32
_SipxDiscardedRoutes_Object=MibScalar
sipxDiscardedRoutes=_SipxDiscardedRoutes_Object((1,3,6,1,4,1,97,3,18,4),_SipxDiscardedRoutes_Type())
sipxDiscardedRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:sipxDiscardedRoutes.setStatus(_A)
_SipxDiscardedServices_Type=Counter32
_SipxDiscardedServices_Object=MibScalar
sipxDiscardedServices=_SipxDiscardedServices_Object((1,3,6,1,4,1,97,3,18,5),_SipxDiscardedServices_Type())
sipxDiscardedServices.setMaxAccess(_B)
if mibBuilder.loadTexts:sipxDiscardedServices.setStatus(_A)
_SipxsfGrp_ObjectIdentity=ObjectIdentity
sipxsfGrp=_SipxsfGrp_ObjectIdentity((1,3,6,1,4,1,97,3,18,6))
_SipxsfNextIndex_Type=Integer32
_SipxsfNextIndex_Object=MibScalar
sipxsfNextIndex=_SipxsfNextIndex_Object((1,3,6,1,4,1,97,3,18,6,1),_SipxsfNextIndex_Type())
sipxsfNextIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sipxsfNextIndex.setStatus(_A)
_SipxsfTable_Object=MibTable
sipxsfTable=_SipxsfTable_Object((1,3,6,1,4,1,97,3,18,6,2))
if mibBuilder.loadTexts:sipxsfTable.setStatus(_A)
_SipxsfEntry_Object=MibTableRow
sipxsfEntry=_SipxsfEntry_Object((1,3,6,1,4,1,97,3,18,6,2,1))
sipxsfEntry.setIndexNames((0,_E,_AM))
if mibBuilder.loadTexts:sipxsfEntry.setStatus(_A)
_SipxsfIndex_Type=Integer32
_SipxsfIndex_Object=MibTableColumn
sipxsfIndex=_SipxsfIndex_Object((1,3,6,1,4,1,97,3,18,6,2,1,1),_SipxsfIndex_Type())
sipxsfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:sipxsfIndex.setStatus(_A)
_SipxsfSAPName_Type=OctetString
_SipxsfSAPName_Object=MibTableColumn
sipxsfSAPName=_SipxsfSAPName_Object((1,3,6,1,4,1,97,3,18,6,2,1,2),_SipxsfSAPName_Type())
sipxsfSAPName.setMaxAccess(_C)
if mibBuilder.loadTexts:sipxsfSAPName.setStatus(_A)
_SipxsfSAPType_Type=Integer32
_SipxsfSAPType_Object=MibTableColumn
sipxsfSAPType=_SipxsfSAPType_Object((1,3,6,1,4,1,97,3,18,6,2,1,3),_SipxsfSAPType_Type())
sipxsfSAPType.setMaxAccess(_C)
if mibBuilder.loadTexts:sipxsfSAPType.setStatus(_A)
class _SipxsfAccessMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('permitted',1),('denied',2),(_K,3)))
_SipxsfAccessMode_Type.__name__=_D
_SipxsfAccessMode_Object=MibTableColumn
sipxsfAccessMode=_SipxsfAccessMode_Object((1,3,6,1,4,1,97,3,18,6,2,1,4),_SipxsfAccessMode_Type())
sipxsfAccessMode.setMaxAccess(_C)
if mibBuilder.loadTexts:sipxsfAccessMode.setStatus(_A)
class _SipxsfFilterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('entry',1),('exit',2)))
_SipxsfFilterType_Type.__name__=_D
_SipxsfFilterType_Object=MibTableColumn
sipxsfFilterType=_SipxsfFilterType_Object((1,3,6,1,4,1,97,3,18,6,2,1,5),_SipxsfFilterType_Type())
sipxsfFilterType.setMaxAccess(_C)
if mibBuilder.loadTexts:sipxsfFilterType.setStatus(_A)
_SipxsfPortMap_Type=OctetString
_SipxsfPortMap_Object=MibTableColumn
sipxsfPortMap=_SipxsfPortMap_Object((1,3,6,1,4,1,97,3,18,6,2,1,6),_SipxsfPortMap_Type())
sipxsfPortMap.setMaxAccess(_C)
if mibBuilder.loadTexts:sipxsfPortMap.setStatus(_A)
_SipxsfNetworks_Type=OctetString
_SipxsfNetworks_Object=MibTableColumn
sipxsfNetworks=_SipxsfNetworks_Object((1,3,6,1,4,1,97,3,18,6,2,1,7),_SipxsfNetworks_Type())
sipxsfNetworks.setMaxAccess(_C)
if mibBuilder.loadTexts:sipxsfNetworks.setStatus(_A)
_SipxsfFiltered_Type=Counter32
_SipxsfFiltered_Object=MibTableColumn
sipxsfFiltered=_SipxsfFiltered_Object((1,3,6,1,4,1,97,3,18,6,2,1,8),_SipxsfFiltered_Type())
sipxsfFiltered.setMaxAccess(_B)
if mibBuilder.loadTexts:sipxsfFiltered.setStatus(_A)
_SipxsrGrp_ObjectIdentity=ObjectIdentity
sipxsrGrp=_SipxsrGrp_ObjectIdentity((1,3,6,1,4,1,97,3,18,7))
_SipxsrAgingTime_Type=Integer32
_SipxsrAgingTime_Object=MibScalar
sipxsrAgingTime=_SipxsrAgingTime_Object((1,3,6,1,4,1,97,3,18,7,1),_SipxsrAgingTime_Type())
sipxsrAgingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sipxsrAgingTime.setStatus(_A)
_SipxsrExplorerTable_Object=MibTable
sipxsrExplorerTable=_SipxsrExplorerTable_Object((1,3,6,1,4,1,97,3,18,7,2))
if mibBuilder.loadTexts:sipxsrExplorerTable.setStatus(_A)
_SipxsrExplorerEntry_Object=MibTableRow
sipxsrExplorerEntry=_SipxsrExplorerEntry_Object((1,3,6,1,4,1,97,3,18,7,2,1))
sipxsrExplorerEntry.setIndexNames((0,_E,_AN))
if mibBuilder.loadTexts:sipxsrExplorerEntry.setStatus(_A)
_SipxsrPort_Type=Integer32
_SipxsrPort_Object=MibTableColumn
sipxsrPort=_SipxsrPort_Object((1,3,6,1,4,1,97,3,18,7,2,1,1),_SipxsrPort_Type())
sipxsrPort.setMaxAccess(_C)
if mibBuilder.loadTexts:sipxsrPort.setStatus(_A)
class _SipxsrStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_K,2)))
_SipxsrStatus_Type.__name__=_D
_SipxsrStatus_Object=MibTableColumn
sipxsrStatus=_SipxsrStatus_Object((1,3,6,1,4,1,97,3,18,7,2,1,2),_SipxsrStatus_Type())
sipxsrStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sipxsrStatus.setStatus(_A)
class _SipxsrExplorerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('are',1),('ste',2)))
_SipxsrExplorerType_Type.__name__=_D
_SipxsrExplorerType_Object=MibTableColumn
sipxsrExplorerType=_SipxsrExplorerType_Object((1,3,6,1,4,1,97,3,18,7,2,1,3),_SipxsrExplorerType_Type())
sipxsrExplorerType.setMaxAccess(_C)
if mibBuilder.loadTexts:sipxsrExplorerType.setStatus(_A)
_Srtrdisc_ObjectIdentity=ObjectIdentity
srtrdisc=_Srtrdisc_ObjectIdentity((1,3,6,1,4,1,97,3,19))
_SrtrdiscTable_Object=MibTable
srtrdiscTable=_SrtrdiscTable_Object((1,3,6,1,4,1,97,3,19,1))
if mibBuilder.loadTexts:srtrdiscTable.setStatus(_A)
_SrtrdiscEntry_Object=MibTableRow
srtrdiscEntry=_SrtrdiscEntry_Object((1,3,6,1,4,1,97,3,19,1,1))
srtrdiscEntry.setIndexNames((0,_E,_AO))
if mibBuilder.loadTexts:srtrdiscEntry.setStatus(_A)
_SrtrdiscIfIndex_Type=Integer32
_SrtrdiscIfIndex_Object=MibTableColumn
srtrdiscIfIndex=_SrtrdiscIfIndex_Object((1,3,6,1,4,1,97,3,19,1,1,1),_SrtrdiscIfIndex_Type())
srtrdiscIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:srtrdiscIfIndex.setStatus(_A)
class _SrtrdiscState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_SrtrdiscState_Type.__name__=_D
_SrtrdiscState_Object=MibTableColumn
srtrdiscState=_SrtrdiscState_Object((1,3,6,1,4,1,97,3,19,1,1,2),_SrtrdiscState_Type())
srtrdiscState.setMaxAccess(_C)
if mibBuilder.loadTexts:srtrdiscState.setStatus(_A)
class _SrtrdiscAdvertisementAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('multicast',1),('broadcast',2)))
_SrtrdiscAdvertisementAddress_Type.__name__=_D
_SrtrdiscAdvertisementAddress_Object=MibTableColumn
srtrdiscAdvertisementAddress=_SrtrdiscAdvertisementAddress_Object((1,3,6,1,4,1,97,3,19,1,1,3),_SrtrdiscAdvertisementAddress_Type())
srtrdiscAdvertisementAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:srtrdiscAdvertisementAddress.setStatus(_A)
_SrtrdiscAdvertisementInterval_Type=Integer32
_SrtrdiscAdvertisementInterval_Object=MibTableColumn
srtrdiscAdvertisementInterval=_SrtrdiscAdvertisementInterval_Object((1,3,6,1,4,1,97,3,19,1,1,4),_SrtrdiscAdvertisementInterval_Type())
srtrdiscAdvertisementInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:srtrdiscAdvertisementInterval.setStatus(_A)
_SrtrdiscLifetime_Type=Integer32
_SrtrdiscLifetime_Object=MibTableColumn
srtrdiscLifetime=_SrtrdiscLifetime_Object((1,3,6,1,4,1,97,3,19,1,1,5),_SrtrdiscLifetime_Type())
srtrdiscLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:srtrdiscLifetime.setStatus(_A)
_SrtrdiscPreference_Type=Integer32
_SrtrdiscPreference_Object=MibTableColumn
srtrdiscPreference=_SrtrdiscPreference_Object((1,3,6,1,4,1,97,3,19,1,1,6),_SrtrdiscPreference_Type())
srtrdiscPreference.setMaxAccess(_C)
if mibBuilder.loadTexts:srtrdiscPreference.setStatus(_A)
_Sipm_ObjectIdentity=ObjectIdentity
sipm=_Sipm_ObjectIdentity((1,3,6,1,4,1,97,3,20))
_Sipmroute_ObjectIdentity=ObjectIdentity
sipmroute=_Sipmroute_ObjectIdentity((1,3,6,1,4,1,97,3,20,1))
_SipmRouteTable_Object=MibTable
sipmRouteTable=_SipmRouteTable_Object((1,3,6,1,4,1,97,3,20,1,1))
if mibBuilder.loadTexts:sipmRouteTable.setStatus(_A)
_SipmRouteEntry_Object=MibTableRow
sipmRouteEntry=_SipmRouteEntry_Object((1,3,6,1,4,1,97,3,20,1,1,1))
sipmRouteEntry.setIndexNames((0,_E,_AP),(0,_E,_AQ))
if mibBuilder.loadTexts:sipmRouteEntry.setStatus(_A)
_SipmRouteOrigin_Type=IpAddress
_SipmRouteOrigin_Object=MibTableColumn
sipmRouteOrigin=_SipmRouteOrigin_Object((1,3,6,1,4,1,97,3,20,1,1,1,1),_SipmRouteOrigin_Type())
sipmRouteOrigin.setMaxAccess(_B)
if mibBuilder.loadTexts:sipmRouteOrigin.setStatus(_A)
_SipmRouteOriginMask_Type=IpAddress
_SipmRouteOriginMask_Object=MibTableColumn
sipmRouteOriginMask=_SipmRouteOriginMask_Object((1,3,6,1,4,1,97,3,20,1,1,1,2),_SipmRouteOriginMask_Type())
sipmRouteOriginMask.setMaxAccess(_B)
if mibBuilder.loadTexts:sipmRouteOriginMask.setStatus(_A)
_SipmRouteGateway_Type=IpAddress
_SipmRouteGateway_Object=MibTableColumn
sipmRouteGateway=_SipmRouteGateway_Object((1,3,6,1,4,1,97,3,20,1,1,1,3),_SipmRouteGateway_Type())
sipmRouteGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:sipmRouteGateway.setStatus(_A)
_SipmRouteMetric_Type=Integer32
_SipmRouteMetric_Object=MibTableColumn
sipmRouteMetric=_SipmRouteMetric_Object((1,3,6,1,4,1,97,3,20,1,1,1,4),_SipmRouteMetric_Type())
sipmRouteMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:sipmRouteMetric.setStatus(_A)
_SipmRouteAge_Type=TimeTicks
_SipmRouteAge_Object=MibTableColumn
sipmRouteAge=_SipmRouteAge_Object((1,3,6,1,4,1,97,3,20,1,1,1,5),_SipmRouteAge_Type())
sipmRouteAge.setMaxAccess(_C)
if mibBuilder.loadTexts:sipmRouteAge.setStatus(_A)
_SipmRouteParents_Type=OctetString
_SipmRouteParents_Object=MibTableColumn
sipmRouteParents=_SipmRouteParents_Object((1,3,6,1,4,1,97,3,20,1,1,1,6),_SipmRouteParents_Type())
sipmRouteParents.setMaxAccess(_B)
if mibBuilder.loadTexts:sipmRouteParents.setStatus(_A)
_Sipmgroup_ObjectIdentity=ObjectIdentity
sipmgroup=_Sipmgroup_ObjectIdentity((1,3,6,1,4,1,97,3,20,2))
_Sipmneighbor_ObjectIdentity=ObjectIdentity
sipmneighbor=_Sipmneighbor_ObjectIdentity((1,3,6,1,4,1,97,3,20,3))
_SipmNeighborTable_Object=MibTable
sipmNeighborTable=_SipmNeighborTable_Object((1,3,6,1,4,1,97,3,20,3,1))
if mibBuilder.loadTexts:sipmNeighborTable.setStatus(_A)
_SipmNeighborEntry_Object=MibTableRow
sipmNeighborEntry=_SipmNeighborEntry_Object((1,3,6,1,4,1,97,3,20,3,1,1))
sipmNeighborEntry.setIndexNames((0,_E,_AR),(0,_E,_AS))
if mibBuilder.loadTexts:sipmNeighborEntry.setStatus(_A)
_SipmNeighborIfIndex_Type=Integer32
_SipmNeighborIfIndex_Object=MibTableColumn
sipmNeighborIfIndex=_SipmNeighborIfIndex_Object((1,3,6,1,4,1,97,3,20,3,1,1,1),_SipmNeighborIfIndex_Type())
sipmNeighborIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sipmNeighborIfIndex.setStatus(_A)
_SipmNeighbors_Type=IpAddress
_SipmNeighbors_Object=MibTableColumn
sipmNeighbors=_SipmNeighbors_Object((1,3,6,1,4,1,97,3,20,3,1,1,2),_SipmNeighbors_Type())
sipmNeighbors.setMaxAccess(_B)
if mibBuilder.loadTexts:sipmNeighbors.setStatus(_A)
_SipmNeighborLastHeard_Type=TimeTicks
_SipmNeighborLastHeard_Object=MibTableColumn
sipmNeighborLastHeard=_SipmNeighborLastHeard_Object((1,3,6,1,4,1,97,3,20,3,1,1,3),_SipmNeighborLastHeard_Type())
sipmNeighborLastHeard.setMaxAccess(_B)
if mibBuilder.loadTexts:sipmNeighborLastHeard.setStatus(_A)
_Sipmstat_ObjectIdentity=ObjectIdentity
sipmstat=_Sipmstat_ObjectIdentity((1,3,6,1,4,1,97,3,20,4))
_SipmOutOfMemory_Type=Counter32
_SipmOutOfMemory_Object=MibScalar
sipmOutOfMemory=_SipmOutOfMemory_Object((1,3,6,1,4,1,97,3,20,4,1),_SipmOutOfMemory_Type())
sipmOutOfMemory.setMaxAccess(_C)
if mibBuilder.loadTexts:sipmOutOfMemory.setStatus(_A)
_SipmStatTable_Object=MibTable
sipmStatTable=_SipmStatTable_Object((1,3,6,1,4,1,97,3,20,4,2))
if mibBuilder.loadTexts:sipmStatTable.setStatus(_A)
_SipmStatEntry_Object=MibTableRow
sipmStatEntry=_SipmStatEntry_Object((1,3,6,1,4,1,97,3,20,4,2,1))
sipmStatEntry.setIndexNames((0,_E,_AT))
if mibBuilder.loadTexts:sipmStatEntry.setStatus(_A)
_SipmStatIfIndex_Type=Integer32
_SipmStatIfIndex_Object=MibTableColumn
sipmStatIfIndex=_SipmStatIfIndex_Object((1,3,6,1,4,1,97,3,20,4,2,1,1),_SipmStatIfIndex_Type())
sipmStatIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sipmStatIfIndex.setStatus(_A)
_SipmInBadPackets_Type=Counter32
_SipmInBadPackets_Object=MibTableColumn
sipmInBadPackets=_SipmInBadPackets_Object((1,3,6,1,4,1,97,3,20,4,2,1,2),_SipmInBadPackets_Type())
sipmInBadPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:sipmInBadPackets.setStatus(_A)
_SipmCacheMiss_Type=Counter32
_SipmCacheMiss_Object=MibTableColumn
sipmCacheMiss=_SipmCacheMiss_Object((1,3,6,1,4,1,97,3,20,4,2,1,3),_SipmCacheMiss_Type())
sipmCacheMiss.setMaxAccess(_C)
if mibBuilder.loadTexts:sipmCacheMiss.setStatus(_A)
_Sipckt_ObjectIdentity=ObjectIdentity
sipckt=_Sipckt_ObjectIdentity((1,3,6,1,4,1,97,3,21))
_SipcktTable_Object=MibTable
sipcktTable=_SipcktTable_Object((1,3,6,1,4,1,97,3,21,1))
if mibBuilder.loadTexts:sipcktTable.setStatus(_A)
_SipcktEntry_Object=MibTableRow
sipcktEntry=_SipcktEntry_Object((1,3,6,1,4,1,97,3,21,1,1))
sipcktEntry.setIndexNames((0,_E,_AU),(0,_E,_AV))
if mibBuilder.loadTexts:sipcktEntry.setStatus(_A)
_SipcktIndex_Type=Integer32
_SipcktIndex_Object=MibTableColumn
sipcktIndex=_SipcktIndex_Object((1,3,6,1,4,1,97,3,21,1,1,1),_SipcktIndex_Type())
sipcktIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:sipcktIndex.setStatus(_A)
_SipcktIpAddress_Type=IpAddress
_SipcktIpAddress_Object=MibTableColumn
sipcktIpAddress=_SipcktIpAddress_Object((1,3,6,1,4,1,97,3,21,1,1,2),_SipcktIpAddress_Type())
sipcktIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:sipcktIpAddress.setStatus(_A)
class _SipcktState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_P,1),(_K,2),('invalid-all',3),('netmask-conflict',4)))
_SipcktState_Type.__name__=_D
_SipcktState_Object=MibTableColumn
sipcktState=_SipcktState_Object((1,3,6,1,4,1,97,3,21,1,1,3),_SipcktState_Type())
sipcktState.setMaxAccess(_C)
if mibBuilder.loadTexts:sipcktState.setStatus(_A)
_SipcktNetMask_Type=IpAddress
_SipcktNetMask_Object=MibTableColumn
sipcktNetMask=_SipcktNetMask_Object((1,3,6,1,4,1,97,3,21,1,1,4),_SipcktNetMask_Type())
sipcktNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:sipcktNetMask.setStatus(_A)
class _SipcktSourceRoute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('default',1),('sr',2),('no-sr',3),('both',4)))
_SipcktSourceRoute_Type.__name__=_D
_SipcktSourceRoute_Object=MibTableColumn
sipcktSourceRoute=_SipcktSourceRoute_Object((1,3,6,1,4,1,97,3,21,1,1,5),_SipcktSourceRoute_Type())
sipcktSourceRoute.setMaxAccess(_C)
if mibBuilder.loadTexts:sipcktSourceRoute.setStatus(_A)
_SipNetToMediaTable_Object=MibTable
sipNetToMediaTable=_SipNetToMediaTable_Object((1,3,6,1,4,1,97,3,22))
if mibBuilder.loadTexts:sipNetToMediaTable.setStatus(_A)
_SipNetToMediaEntry_Object=MibTableRow
sipNetToMediaEntry=_SipNetToMediaEntry_Object((1,3,6,1,4,1,97,3,22,1))
sipNetToMediaEntry.setIndexNames((0,_E,_AW),(0,_E,_AX))
if mibBuilder.loadTexts:sipNetToMediaEntry.setStatus(_A)
_SipNetToMediaIfIndex_Type=Integer32
_SipNetToMediaIfIndex_Object=MibTableColumn
sipNetToMediaIfIndex=_SipNetToMediaIfIndex_Object((1,3,6,1,4,1,97,3,22,1,1),_SipNetToMediaIfIndex_Type())
sipNetToMediaIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sipNetToMediaIfIndex.setStatus(_A)
_SipNetToMediaNetAddress_Type=IpAddress
_SipNetToMediaNetAddress_Object=MibTableColumn
sipNetToMediaNetAddress=_SipNetToMediaNetAddress_Object((1,3,6,1,4,1,97,3,22,1,2),_SipNetToMediaNetAddress_Type())
sipNetToMediaNetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:sipNetToMediaNetAddress.setStatus(_A)
_SipNetToMediaSourceRoute_Type=OctetString
_SipNetToMediaSourceRoute_Object=MibTableColumn
sipNetToMediaSourceRoute=_SipNetToMediaSourceRoute_Object((1,3,6,1,4,1,97,3,22,1,3),_SipNetToMediaSourceRoute_Type())
sipNetToMediaSourceRoute.setMaxAccess(_B)
if mibBuilder.loadTexts:sipNetToMediaSourceRoute.setStatus(_A)
_SipNetToMediaAge_Type=Integer32
_SipNetToMediaAge_Object=MibTableColumn
sipNetToMediaAge=_SipNetToMediaAge_Object((1,3,6,1,4,1,97,3,22,1,4),_SipNetToMediaAge_Type())
sipNetToMediaAge.setMaxAccess(_B)
if mibBuilder.loadTexts:sipNetToMediaAge.setStatus(_A)
_Ssecure_ObjectIdentity=ObjectIdentity
ssecure=_Ssecure_ObjectIdentity((1,3,6,1,4,1,97,3,23))
_ProfileTable_Object=MibTable
profileTable=_ProfileTable_Object((1,3,6,1,4,1,97,3,23,1))
if mibBuilder.loadTexts:profileTable.setStatus(_A)
_ProfileEntry_Object=MibTableRow
profileEntry=_ProfileEntry_Object((1,3,6,1,4,1,97,3,23,1,1))
profileEntry.setIndexNames((0,_E,_AY),(0,_E,_AZ),(0,_E,_Aa),(0,_E,_Ab),(0,_E,_Ac))
if mibBuilder.loadTexts:profileEntry.setStatus(_A)
_ProfileIndex_Type=Integer32
_ProfileIndex_Object=MibTableColumn
profileIndex=_ProfileIndex_Object((1,3,6,1,4,1,97,3,23,1,1,1),_ProfileIndex_Type())
profileIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:profileIndex.setStatus(_A)
class _ProfileSourceStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ProfileSourceStart_Type.__name__=_D
_ProfileSourceStart_Object=MibTableColumn
profileSourceStart=_ProfileSourceStart_Object((1,3,6,1,4,1,97,3,23,1,1,2),_ProfileSourceStart_Type())
profileSourceStart.setMaxAccess(_B)
if mibBuilder.loadTexts:profileSourceStart.setStatus(_A)
class _ProfileSourceEnd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ProfileSourceEnd_Type.__name__=_D
_ProfileSourceEnd_Object=MibTableColumn
profileSourceEnd=_ProfileSourceEnd_Object((1,3,6,1,4,1,97,3,23,1,1,3),_ProfileSourceEnd_Type())
profileSourceEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:profileSourceEnd.setStatus(_A)
class _ProfileDestStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ProfileDestStart_Type.__name__=_D
_ProfileDestStart_Object=MibTableColumn
profileDestStart=_ProfileDestStart_Object((1,3,6,1,4,1,97,3,23,1,1,4),_ProfileDestStart_Type())
profileDestStart.setMaxAccess(_B)
if mibBuilder.loadTexts:profileDestStart.setStatus(_A)
class _ProfileDestEnd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ProfileDestEnd_Type.__name__=_D
_ProfileDestEnd_Object=MibTableColumn
profileDestEnd=_ProfileDestEnd_Object((1,3,6,1,4,1,97,3,23,1,1,5),_ProfileDestEnd_Type())
profileDestEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:profileDestEnd.setStatus(_A)
class _ProfileType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_K,2)))
_ProfileType_Type.__name__=_D
_ProfileType_Object=MibTableColumn
profileType=_ProfileType_Object((1,3,6,1,4,1,97,3,23,1,1,6),_ProfileType_Type())
profileType.setMaxAccess(_C)
if mibBuilder.loadTexts:profileType.setStatus(_A)
_RuleTable_Object=MibTable
ruleTable=_RuleTable_Object((1,3,6,1,4,1,97,3,23,2))
if mibBuilder.loadTexts:ruleTable.setStatus(_A)
_RuleEntry_Object=MibTableRow
ruleEntry=_RuleEntry_Object((1,3,6,1,4,1,97,3,23,2,1))
ruleEntry.setIndexNames((0,_E,_Ad),(0,_E,_Ae),(0,_E,_Af),(0,_E,_Ag),(0,_E,_Ah))
if mibBuilder.loadTexts:ruleEntry.setStatus(_A)
_RuleIndex_Type=Integer32
_RuleIndex_Object=MibTableColumn
ruleIndex=_RuleIndex_Object((1,3,6,1,4,1,97,3,23,2,1,1),_RuleIndex_Type())
ruleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ruleIndex.setStatus(_A)
_RuleSourceIp_Type=IpAddress
_RuleSourceIp_Object=MibTableColumn
ruleSourceIp=_RuleSourceIp_Object((1,3,6,1,4,1,97,3,23,2,1,2),_RuleSourceIp_Type())
ruleSourceIp.setMaxAccess(_B)
if mibBuilder.loadTexts:ruleSourceIp.setStatus(_A)
_RuleDestIp_Type=IpAddress
_RuleDestIp_Object=MibTableColumn
ruleDestIp=_RuleDestIp_Object((1,3,6,1,4,1,97,3,23,2,1,3),_RuleDestIp_Type())
ruleDestIp.setMaxAccess(_B)
if mibBuilder.loadTexts:ruleDestIp.setStatus(_A)
_RuleSourceIpMask_Type=IpAddress
_RuleSourceIpMask_Object=MibTableColumn
ruleSourceIpMask=_RuleSourceIpMask_Object((1,3,6,1,4,1,97,3,23,2,1,4),_RuleSourceIpMask_Type())
ruleSourceIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ruleSourceIpMask.setStatus(_A)
_RuleDestIpMask_Type=IpAddress
_RuleDestIpMask_Object=MibTableColumn
ruleDestIpMask=_RuleDestIpMask_Object((1,3,6,1,4,1,97,3,23,2,1,5),_RuleDestIpMask_Type())
ruleDestIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ruleDestIpMask.setStatus(_A)
class _RuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_K,2)))
_RuleType_Type.__name__=_D
_RuleType_Object=MibTableColumn
ruleType=_RuleType_Object((1,3,6,1,4,1,97,3,23,2,1,6),_RuleType_Type())
ruleType.setMaxAccess(_C)
if mibBuilder.loadTexts:ruleType.setStatus(_A)
class _RuleUdpProfile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_RuleUdpProfile_Type.__name__=_D
_RuleUdpProfile_Object=MibTableColumn
ruleUdpProfile=_RuleUdpProfile_Object((1,3,6,1,4,1,97,3,23,2,1,7),_RuleUdpProfile_Type())
ruleUdpProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:ruleUdpProfile.setStatus(_A)
class _RuleTcpProfile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_RuleTcpProfile_Type.__name__=_D
_RuleTcpProfile_Object=MibTableColumn
ruleTcpProfile=_RuleTcpProfile_Object((1,3,6,1,4,1,97,3,23,2,1,8),_RuleTcpProfile_Type())
ruleTcpProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:ruleTcpProfile.setStatus(_A)
class _RuleTcpEstProfile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_RuleTcpEstProfile_Type.__name__=_D
_RuleTcpEstProfile_Object=MibTableColumn
ruleTcpEstProfile=_RuleTcpEstProfile_Object((1,3,6,1,4,1,97,3,23,2,1,9),_RuleTcpEstProfile_Type())
ruleTcpEstProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:ruleTcpEstProfile.setStatus(_A)
_RuleFilterUdpFragment_Type=Boolean
_RuleFilterUdpFragment_Object=MibTableColumn
ruleFilterUdpFragment=_RuleFilterUdpFragment_Object((1,3,6,1,4,1,97,3,23,2,1,10),_RuleFilterUdpFragment_Type())
ruleFilterUdpFragment.setMaxAccess(_C)
if mibBuilder.loadTexts:ruleFilterUdpFragment.setStatus(_A)
_RuleFilterTcpFragment_Type=Boolean
_RuleFilterTcpFragment_Object=MibTableColumn
ruleFilterTcpFragment=_RuleFilterTcpFragment_Object((1,3,6,1,4,1,97,3,23,2,1,11),_RuleFilterTcpFragment_Type())
ruleFilterTcpFragment.setMaxAccess(_C)
if mibBuilder.loadTexts:ruleFilterTcpFragment.setStatus(_A)
_RuleFilterIpOption_Type=Boolean
_RuleFilterIpOption_Object=MibTableColumn
ruleFilterIpOption=_RuleFilterIpOption_Object((1,3,6,1,4,1,97,3,23,2,1,12),_RuleFilterIpOption_Type())
ruleFilterIpOption.setMaxAccess(_C)
if mibBuilder.loadTexts:ruleFilterIpOption.setStatus(_A)
_RuleAllowIcmp_Type=Boolean
_RuleAllowIcmp_Object=MibTableColumn
ruleAllowIcmp=_RuleAllowIcmp_Object((1,3,6,1,4,1,97,3,23,2,1,13),_RuleAllowIcmp_Type())
ruleAllowIcmp.setMaxAccess(_C)
if mibBuilder.loadTexts:ruleAllowIcmp.setStatus(_A)
_RuleAllowIpWithinIp_Type=Boolean
_RuleAllowIpWithinIp_Object=MibTableColumn
ruleAllowIpWithinIp=_RuleAllowIpWithinIp_Object((1,3,6,1,4,1,97,3,23,2,1,14),_RuleAllowIpWithinIp_Type())
ruleAllowIpWithinIp.setMaxAccess(_C)
if mibBuilder.loadTexts:ruleAllowIpWithinIp.setStatus(_A)
_RuleAllowEgp_Type=Boolean
_RuleAllowEgp_Object=MibTableColumn
ruleAllowEgp=_RuleAllowEgp_Object((1,3,6,1,4,1,97,3,23,2,1,15),_RuleAllowEgp_Type())
ruleAllowEgp.setMaxAccess(_C)
if mibBuilder.loadTexts:ruleAllowEgp.setStatus(_A)
_RuleAllowIgp_Type=Boolean
_RuleAllowIgp_Object=MibTableColumn
ruleAllowIgp=_RuleAllowIgp_Object((1,3,6,1,4,1,97,3,23,2,1,16),_RuleAllowIgp_Type())
ruleAllowIgp.setMaxAccess(_C)
if mibBuilder.loadTexts:ruleAllowIgp.setStatus(_A)
_RuleAllowIgrp_Type=Boolean
_RuleAllowIgrp_Object=MibTableColumn
ruleAllowIgrp=_RuleAllowIgrp_Object((1,3,6,1,4,1,97,3,23,2,1,17),_RuleAllowIgrp_Type())
ruleAllowIgrp.setMaxAccess(_C)
if mibBuilder.loadTexts:ruleAllowIgrp.setStatus(_A)
_RuleAllowOspf_Type=Boolean
_RuleAllowOspf_Object=MibTableColumn
ruleAllowOspf=_RuleAllowOspf_Object((1,3,6,1,4,1,97,3,23,2,1,18),_RuleAllowOspf_Type())
ruleAllowOspf.setMaxAccess(_C)
if mibBuilder.loadTexts:ruleAllowOspf.setStatus(_A)
_RuleAllowAnyOther_Type=Boolean
_RuleAllowAnyOther_Object=MibTableColumn
ruleAllowAnyOther=_RuleAllowAnyOther_Object((1,3,6,1,4,1,97,3,23,2,1,19),_RuleAllowAnyOther_Type())
ruleAllowAnyOther.setMaxAccess(_C)
if mibBuilder.loadTexts:ruleAllowAnyOther.setStatus(_A)
_Spvc_ObjectIdentity=ObjectIdentity
spvc=_Spvc_ObjectIdentity((1,3,6,1,4,1,97,3,24))
_SpvcTable_Object=MibTable
spvcTable=_SpvcTable_Object((1,3,6,1,4,1,97,3,24,1))
if mibBuilder.loadTexts:spvcTable.setStatus(_A)
_SpvcEntry_Object=MibTableRow
spvcEntry=_SpvcEntry_Object((1,3,6,1,4,1,97,3,24,1,1))
spvcEntry.setIndexNames((0,_E,_Ai))
if mibBuilder.loadTexts:spvcEntry.setStatus(_A)
_SpvcIfIndex_Type=Integer32
_SpvcIfIndex_Object=MibTableColumn
spvcIfIndex=_SpvcIfIndex_Object((1,3,6,1,4,1,97,3,24,1,1,1),_SpvcIfIndex_Type())
spvcIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:spvcIfIndex.setStatus(_A)
_SpvcPathRX_Type=Integer32
_SpvcPathRX_Object=MibTableColumn
spvcPathRX=_SpvcPathRX_Object((1,3,6,1,4,1,97,3,24,1,1,2),_SpvcPathRX_Type())
spvcPathRX.setMaxAccess(_C)
if mibBuilder.loadTexts:spvcPathRX.setStatus(_A)
_SpvcCircuitRX_Type=Integer32
_SpvcCircuitRX_Object=MibTableColumn
spvcCircuitRX=_SpvcCircuitRX_Object((1,3,6,1,4,1,97,3,24,1,1,3),_SpvcCircuitRX_Type())
spvcCircuitRX.setMaxAccess(_C)
if mibBuilder.loadTexts:spvcCircuitRX.setStatus(_A)
_SpvcPathTX_Type=Integer32
_SpvcPathTX_Object=MibTableColumn
spvcPathTX=_SpvcPathTX_Object((1,3,6,1,4,1,97,3,24,1,1,4),_SpvcPathTX_Type())
spvcPathTX.setMaxAccess(_C)
if mibBuilder.loadTexts:spvcPathTX.setStatus(_A)
_SpvcCircuitTX_Type=Integer32
_SpvcCircuitTX_Object=MibTableColumn
spvcCircuitTX=_SpvcCircuitTX_Object((1,3,6,1,4,1,97,3,24,1,1,5),_SpvcCircuitTX_Type())
spvcCircuitTX.setMaxAccess(_C)
if mibBuilder.loadTexts:spvcCircuitTX.setStatus(_A)
class _SpvcState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('exists',1),('removed',2)))
_SpvcState_Type.__name__=_D
_SpvcState_Object=MibTableColumn
spvcState=_SpvcState_Object((1,3,6,1,4,1,97,3,24,1,1,6),_SpvcState_Type())
spvcState.setMaxAccess(_C)
if mibBuilder.loadTexts:spvcState.setStatus(_A)
_SpvcPhysPort_Type=Integer32
_SpvcPhysPort_Object=MibTableColumn
spvcPhysPort=_SpvcPhysPort_Object((1,3,6,1,4,1,97,3,24,1,1,7),_SpvcPhysPort_Type())
spvcPhysPort.setMaxAccess(_B)
if mibBuilder.loadTexts:spvcPhysPort.setStatus(_A)
_SpvcMinPort_Type=Integer32
_SpvcMinPort_Object=MibScalar
spvcMinPort=_SpvcMinPort_Object((1,3,6,1,4,1,97,3,24,2),_SpvcMinPort_Type())
spvcMinPort.setMaxAccess(_B)
if mibBuilder.loadTexts:spvcMinPort.setStatus(_A)
_SpvcMaxPort_Type=Integer32
_SpvcMaxPort_Object=MibScalar
spvcMaxPort=_SpvcMaxPort_Object((1,3,6,1,4,1,97,3,24,3),_SpvcMaxPort_Type())
spvcMaxPort.setMaxAccess(_B)
if mibBuilder.loadTexts:spvcMaxPort.setStatus(_A)
_Strunk_ObjectIdentity=ObjectIdentity
strunk=_Strunk_ObjectIdentity((1,3,6,1,4,1,97,3,25))
_StrunkTable_Object=MibTable
strunkTable=_StrunkTable_Object((1,3,6,1,4,1,97,3,25,1))
if mibBuilder.loadTexts:strunkTable.setStatus(_A)
_StrunkEntry_Object=MibTableRow
strunkEntry=_StrunkEntry_Object((1,3,6,1,4,1,97,3,25,1,1))
strunkEntry.setIndexNames((0,_E,_Aj))
if mibBuilder.loadTexts:strunkEntry.setStatus(_A)
_StrunkIfIndex_Type=Integer32
_StrunkIfIndex_Object=MibTableColumn
strunkIfIndex=_StrunkIfIndex_Object((1,3,6,1,4,1,97,3,25,1,1,1),_StrunkIfIndex_Type())
strunkIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:strunkIfIndex.setStatus(_A)
class _StrunkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_L,1),('closed',2),('oneway',3),('joined',4),('perturbed',5),('helddown',6),('broken',7)))
_StrunkState_Type.__name__=_D
_StrunkState_Object=MibTableColumn
strunkState=_StrunkState_Object((1,3,6,1,4,1,97,3,25,1,1,2),_StrunkState_Type())
strunkState.setMaxAccess(_B)
if mibBuilder.loadTexts:strunkState.setStatus(_A)
_StrunkRemoteBridgeAddr_Type=OctetString
_StrunkRemoteBridgeAddr_Object=MibTableColumn
strunkRemoteBridgeAddr=_StrunkRemoteBridgeAddr_Object((1,3,6,1,4,1,97,3,25,1,1,3),_StrunkRemoteBridgeAddr_Type())
strunkRemoteBridgeAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:strunkRemoteBridgeAddr.setStatus(_A)
_StrunkRemoteIp_Type=IpAddress
_StrunkRemoteIp_Object=MibTableColumn
strunkRemoteIp=_StrunkRemoteIp_Object((1,3,6,1,4,1,97,3,25,1,1,4),_StrunkRemoteIp_Type())
strunkRemoteIp.setMaxAccess(_B)
if mibBuilder.loadTexts:strunkRemoteIp.setStatus(_A)
class _StrunkLastError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_J,1),('in-bpdu',2),('multiple-bridges',3),('ack-lost',4),('standby',5),('too-many-groups',6),('no-ack',7),('perturbed-threshold',8),('self-connect',9),('port-moved',10),('multiple-lan-types',11)))
_StrunkLastError_Type.__name__=_D
_StrunkLastError_Object=MibTableColumn
strunkLastError=_StrunkLastError_Object((1,3,6,1,4,1,97,3,25,1,1,5),_StrunkLastError_Type())
strunkLastError.setMaxAccess(_B)
if mibBuilder.loadTexts:strunkLastError.setStatus(_A)
_StrunkLinkOrdinal_Type=Integer32
_StrunkLinkOrdinal_Object=MibTableColumn
strunkLinkOrdinal=_StrunkLinkOrdinal_Object((1,3,6,1,4,1,97,3,25,1,1,6),_StrunkLinkOrdinal_Type())
strunkLinkOrdinal.setMaxAccess(_B)
if mibBuilder.loadTexts:strunkLinkOrdinal.setStatus(_A)
_StrunkLinkCount_Type=Integer32
_StrunkLinkCount_Object=MibTableColumn
strunkLinkCount=_StrunkLinkCount_Object((1,3,6,1,4,1,97,3,25,1,1,7),_StrunkLinkCount_Type())
strunkLinkCount.setMaxAccess(_B)
if mibBuilder.loadTexts:strunkLinkCount.setStatus(_A)
_StrunkLastChange_Type=Integer32
_StrunkLastChange_Object=MibTableColumn
strunkLastChange=_StrunkLastChange_Object((1,3,6,1,4,1,97,3,25,1,1,8),_StrunkLastChange_Type())
strunkLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:strunkLastChange.setStatus(_A)
_IpMRouteMIB_ObjectIdentity=ObjectIdentity
ipMRouteMIB=_IpMRouteMIB_ObjectIdentity((1,3,6,1,4,1,97,3,26))
_IpMRouteMIBObjects_ObjectIdentity=ObjectIdentity
ipMRouteMIBObjects=_IpMRouteMIBObjects_ObjectIdentity((1,3,6,1,4,1,97,3,26,1))
_IpMRoute_ObjectIdentity=ObjectIdentity
ipMRoute=_IpMRoute_ObjectIdentity((1,3,6,1,4,1,97,3,26,1,1))
class _IpMRouteEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_IpMRouteEnable_Type.__name__=_D
_IpMRouteEnable_Object=MibScalar
ipMRouteEnable=_IpMRouteEnable_Object((1,3,6,1,4,1,97,3,26,1,1,1),_IpMRouteEnable_Type())
ipMRouteEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteEnable.setStatus(_A)
_IpMRouteTable_Object=MibTable
ipMRouteTable=_IpMRouteTable_Object((1,3,6,1,4,1,97,3,26,1,1,2))
if mibBuilder.loadTexts:ipMRouteTable.setStatus(_A)
_IpMRouteEntry_Object=MibTableRow
ipMRouteEntry=_IpMRouteEntry_Object((1,3,6,1,4,1,97,3,26,1,1,2,1))
ipMRouteEntry.setIndexNames((0,_E,_Ak),(0,_E,_Al),(0,_E,_Am))
if mibBuilder.loadTexts:ipMRouteEntry.setStatus(_A)
_IpMRouteGroup_Type=IpAddress
_IpMRouteGroup_Object=MibTableColumn
ipMRouteGroup=_IpMRouteGroup_Object((1,3,6,1,4,1,97,3,26,1,1,2,1,1),_IpMRouteGroup_Type())
ipMRouteGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:ipMRouteGroup.setStatus(_A)
_IpMRouteSource_Type=IpAddress
_IpMRouteSource_Object=MibTableColumn
ipMRouteSource=_IpMRouteSource_Object((1,3,6,1,4,1,97,3,26,1,1,2,1,2),_IpMRouteSource_Type())
ipMRouteSource.setMaxAccess(_B)
if mibBuilder.loadTexts:ipMRouteSource.setStatus(_A)
_IpMRouteSourceMask_Type=IpAddress
_IpMRouteSourceMask_Object=MibTableColumn
ipMRouteSourceMask=_IpMRouteSourceMask_Object((1,3,6,1,4,1,97,3,26,1,1,2,1,3),_IpMRouteSourceMask_Type())
ipMRouteSourceMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ipMRouteSourceMask.setStatus(_A)
_IpMRouteRpfNeighbor_Type=IpAddress
_IpMRouteRpfNeighbor_Object=MibTableColumn
ipMRouteRpfNeighbor=_IpMRouteRpfNeighbor_Object((1,3,6,1,4,1,97,3,26,1,1,2,1,4),_IpMRouteRpfNeighbor_Type())
ipMRouteRpfNeighbor.setMaxAccess(_B)
if mibBuilder.loadTexts:ipMRouteRpfNeighbor.setStatus(_A)
_IpMRouteInIfIndex_Type=Integer32
_IpMRouteInIfIndex_Object=MibTableColumn
ipMRouteInIfIndex=_IpMRouteInIfIndex_Object((1,3,6,1,4,1,97,3,26,1,1,2,1,5),_IpMRouteInIfIndex_Type())
ipMRouteInIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipMRouteInIfIndex.setStatus(_A)
_IpMRouteOutList_Type=OctetString
_IpMRouteOutList_Object=MibTableColumn
ipMRouteOutList=_IpMRouteOutList_Object((1,3,6,1,4,1,97,3,26,1,1,2,1,6),_IpMRouteOutList_Type())
ipMRouteOutList.setMaxAccess(_B)
if mibBuilder.loadTexts:ipMRouteOutList.setStatus(_A)
_IpMRouteUpTime_Type=TimeTicks
_IpMRouteUpTime_Object=MibTableColumn
ipMRouteUpTime=_IpMRouteUpTime_Object((1,3,6,1,4,1,97,3,26,1,1,2,1,7),_IpMRouteUpTime_Type())
ipMRouteUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ipMRouteUpTime.setStatus(_A)
_IpMRouteExpiryTime_Type=TimeTicks
_IpMRouteExpiryTime_Object=MibTableColumn
ipMRouteExpiryTime=_IpMRouteExpiryTime_Object((1,3,6,1,4,1,97,3,26,1,1,2,1,8),_IpMRouteExpiryTime_Type())
ipMRouteExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteExpiryTime.setStatus(_A)
_IpMRoutePkts_Type=Counter32
_IpMRoutePkts_Object=MibTableColumn
ipMRoutePkts=_IpMRoutePkts_Object((1,3,6,1,4,1,97,3,26,1,1,2,1,9),_IpMRoutePkts_Type())
ipMRoutePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ipMRoutePkts.setStatus(_A)
_IpMRouteRpfFails_Type=Counter32
_IpMRouteRpfFails_Object=MibTableColumn
ipMRouteRpfFails=_IpMRouteRpfFails_Object((1,3,6,1,4,1,97,3,26,1,1,2,1,10),_IpMRouteRpfFails_Type())
ipMRouteRpfFails.setMaxAccess(_B)
if mibBuilder.loadTexts:ipMRouteRpfFails.setStatus(_A)
_IpMRouteOctets_Type=Counter32
_IpMRouteOctets_Object=MibTableColumn
ipMRouteOctets=_IpMRouteOctets_Object((1,3,6,1,4,1,97,3,26,1,1,2,1,11),_IpMRouteOctets_Type())
ipMRouteOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ipMRouteOctets.setStatus(_A)
class _IpMRouteNextHopState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pruned',1),('forwarding',2)))
_IpMRouteNextHopState_Type.__name__=_D
_IpMRouteNextHopState_Object=MibTableColumn
ipMRouteNextHopState=_IpMRouteNextHopState_Object((1,3,6,1,4,1,97,3,26,1,1,2,1,12),_IpMRouteNextHopState_Type())
ipMRouteNextHopState.setMaxAccess(_B)
if mibBuilder.loadTexts:ipMRouteNextHopState.setStatus(_A)
_IpMRouteInterfaceTable_Object=MibTable
ipMRouteInterfaceTable=_IpMRouteInterfaceTable_Object((1,3,6,1,4,1,97,3,26,1,1,3))
if mibBuilder.loadTexts:ipMRouteInterfaceTable.setStatus(_A)
_IpMRouteInterfaceEntry_Object=MibTableRow
ipMRouteInterfaceEntry=_IpMRouteInterfaceEntry_Object((1,3,6,1,4,1,97,3,26,1,1,3,1))
ipMRouteInterfaceEntry.setIndexNames((0,_E,_An))
if mibBuilder.loadTexts:ipMRouteInterfaceEntry.setStatus(_A)
_IpMRouteInterfaceIfIndex_Type=Integer32
_IpMRouteInterfaceIfIndex_Object=MibTableColumn
ipMRouteInterfaceIfIndex=_IpMRouteInterfaceIfIndex_Object((1,3,6,1,4,1,97,3,26,1,1,3,1,1),_IpMRouteInterfaceIfIndex_Type())
ipMRouteInterfaceIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipMRouteInterfaceIfIndex.setStatus(_A)
_IpMRouteInterfaceTtl_Type=Integer32
_IpMRouteInterfaceTtl_Object=MibTableColumn
ipMRouteInterfaceTtl=_IpMRouteInterfaceTtl_Object((1,3,6,1,4,1,97,3,26,1,1,3,1,2),_IpMRouteInterfaceTtl_Type())
ipMRouteInterfaceTtl.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteInterfaceTtl.setStatus(_A)
_IgmpMIB_ObjectIdentity=ObjectIdentity
igmpMIB=_IgmpMIB_ObjectIdentity((1,3,6,1,4,1,97,3,27))
_IgmpMIBObjects_ObjectIdentity=ObjectIdentity
igmpMIBObjects=_IgmpMIBObjects_ObjectIdentity((1,3,6,1,4,1,97,3,27,1))
_Igmp_ObjectIdentity=ObjectIdentity
igmp=_Igmp_ObjectIdentity((1,3,6,1,4,1,97,3,27,1,1))
_IgmpInterfaceTable_Object=MibTable
igmpInterfaceTable=_IgmpInterfaceTable_Object((1,3,6,1,4,1,97,3,27,1,1,1))
if mibBuilder.loadTexts:igmpInterfaceTable.setStatus(_A)
_IgmpInterfaceEntry_Object=MibTableRow
igmpInterfaceEntry=_IgmpInterfaceEntry_Object((1,3,6,1,4,1,97,3,27,1,1,1,1))
igmpInterfaceEntry.setIndexNames((0,_E,_Ao))
if mibBuilder.loadTexts:igmpInterfaceEntry.setStatus(_A)
_IgmpInterfaceIfIndex_Type=Integer32
_IgmpInterfaceIfIndex_Object=MibTableColumn
igmpInterfaceIfIndex=_IgmpInterfaceIfIndex_Object((1,3,6,1,4,1,97,3,27,1,1,1,1,1),_IgmpInterfaceIfIndex_Type())
igmpInterfaceIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpInterfaceIfIndex.setStatus(_A)
_IgmpInterfaceQueryInterval_Type=Integer32
_IgmpInterfaceQueryInterval_Object=MibTableColumn
igmpInterfaceQueryInterval=_IgmpInterfaceQueryInterval_Object((1,3,6,1,4,1,97,3,27,1,1,1,1,2),_IgmpInterfaceQueryInterval_Type())
igmpInterfaceQueryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpInterfaceQueryInterval.setStatus(_A)
_IgmpInterfaceStatus_Type=Integer32
_IgmpInterfaceStatus_Object=MibTableColumn
igmpInterfaceStatus=_IgmpInterfaceStatus_Object((1,3,6,1,4,1,97,3,27,1,1,1,1,3),_IgmpInterfaceStatus_Type())
igmpInterfaceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpInterfaceStatus.setStatus(_A)
_IgmpCacheTable_Object=MibTable
igmpCacheTable=_IgmpCacheTable_Object((1,3,6,1,4,1,97,3,27,1,1,2))
if mibBuilder.loadTexts:igmpCacheTable.setStatus(_A)
_IgmpCacheEntry_Object=MibTableRow
igmpCacheEntry=_IgmpCacheEntry_Object((1,3,6,1,4,1,97,3,27,1,1,2,1))
igmpCacheEntry.setIndexNames((0,_E,_Ap),(0,_E,_Aq))
if mibBuilder.loadTexts:igmpCacheEntry.setStatus(_A)
_IgmpCacheAddress_Type=IpAddress
_IgmpCacheAddress_Object=MibTableColumn
igmpCacheAddress=_IgmpCacheAddress_Object((1,3,6,1,4,1,97,3,27,1,1,2,1,1),_IgmpCacheAddress_Type())
igmpCacheAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpCacheAddress.setStatus(_A)
_IgmpCacheIfIndex_Type=Integer32
_IgmpCacheIfIndex_Object=MibTableColumn
igmpCacheIfIndex=_IgmpCacheIfIndex_Object((1,3,6,1,4,1,97,3,27,1,1,2,1,2),_IgmpCacheIfIndex_Type())
igmpCacheIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpCacheIfIndex.setStatus(_A)
_IgmpCacheSelf_Type=Integer32
_IgmpCacheSelf_Object=MibTableColumn
igmpCacheSelf=_IgmpCacheSelf_Object((1,3,6,1,4,1,97,3,27,1,1,2,1,3),_IgmpCacheSelf_Type())
igmpCacheSelf.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpCacheSelf.setStatus(_A)
_IgmpCacheLastReporter_Type=IpAddress
_IgmpCacheLastReporter_Object=MibTableColumn
igmpCacheLastReporter=_IgmpCacheLastReporter_Object((1,3,6,1,4,1,97,3,27,1,1,2,1,4),_IgmpCacheLastReporter_Type())
igmpCacheLastReporter.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpCacheLastReporter.setStatus(_A)
_IgmpCacheUpTime_Type=TimeTicks
_IgmpCacheUpTime_Object=MibTableColumn
igmpCacheUpTime=_IgmpCacheUpTime_Object((1,3,6,1,4,1,97,3,27,1,1,2,1,5),_IgmpCacheUpTime_Type())
igmpCacheUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpCacheUpTime.setStatus(_A)
_IgmpCacheExpiryTime_Type=TimeTicks
_IgmpCacheExpiryTime_Object=MibTableColumn
igmpCacheExpiryTime=_IgmpCacheExpiryTime_Object((1,3,6,1,4,1,97,3,27,1,1,2,1,6),_IgmpCacheExpiryTime_Type())
igmpCacheExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpCacheExpiryTime.setStatus(_A)
_IgmpCacheStatus_Type=Integer32
_IgmpCacheStatus_Object=MibTableColumn
igmpCacheStatus=_IgmpCacheStatus_Object((1,3,6,1,4,1,97,3,27,1,1,2,1,7),_IgmpCacheStatus_Type())
igmpCacheStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpCacheStatus.setStatus(_A)
_Slog_ObjectIdentity=ObjectIdentity
slog=_Slog_ObjectIdentity((1,3,6,1,4,1,97,3,28))
_SlogFilter_Type=OctetString
_SlogFilter_Object=MibScalar
slogFilter=_SlogFilter_Object((1,3,6,1,4,1,97,3,28,1),_SlogFilter_Type())
slogFilter.setMaxAccess(_C)
if mibBuilder.loadTexts:slogFilter.setStatus(_A)
class _SlogTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_SlogTrap_Type.__name__=_D
_SlogTrap_Object=MibScalar
slogTrap=_SlogTrap_Object((1,3,6,1,4,1,97,3,28,2),_SlogTrap_Type())
slogTrap.setMaxAccess(_C)
if mibBuilder.loadTexts:slogTrap.setStatus(_A)
class _SlogOverwrite_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_SlogOverwrite_Type.__name__=_D
_SlogOverwrite_Object=MibScalar
slogOverwrite=_SlogOverwrite_Object((1,3,6,1,4,1,97,3,28,3),_SlogOverwrite_Type())
slogOverwrite.setMaxAccess(_C)
if mibBuilder.loadTexts:slogOverwrite.setStatus(_A)
_SlogEntryNumber_Type=Integer32
_SlogEntryNumber_Object=MibScalar
slogEntryNumber=_SlogEntryNumber_Object((1,3,6,1,4,1,97,3,28,4),_SlogEntryNumber_Type())
slogEntryNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:slogEntryNumber.setStatus(_A)
_SlogEntryTable_Object=MibTable
slogEntryTable=_SlogEntryTable_Object((1,3,6,1,4,1,97,3,28,5))
if mibBuilder.loadTexts:slogEntryTable.setStatus(_A)
_SlogEntry_Object=MibTableRow
slogEntry=_SlogEntry_Object((1,3,6,1,4,1,97,3,28,5,1))
slogEntry.setIndexNames((0,_E,_Ar))
if mibBuilder.loadTexts:slogEntry.setStatus(_A)
_SlogIndex_Type=Integer32
_SlogIndex_Object=MibTableColumn
slogIndex=_SlogIndex_Object((1,3,6,1,4,1,97,3,28,5,1,1),_SlogIndex_Type())
slogIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:slogIndex.setStatus(_A)
_SlogEntryTimeStamp_Type=TimeTicks
_SlogEntryTimeStamp_Object=MibTableColumn
slogEntryTimeStamp=_SlogEntryTimeStamp_Object((1,3,6,1,4,1,97,3,28,5,1,2),_SlogEntryTimeStamp_Type())
slogEntryTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:slogEntryTimeStamp.setStatus(_A)
_SlogEntryMessageText_Type=DisplayString
_SlogEntryMessageText_Object=MibTableColumn
slogEntryMessageText=_SlogEntryMessageText_Object((1,3,6,1,4,1,97,3,28,5,1,3),_SlogEntryMessageText_Type())
slogEntryMessageText.setMaxAccess(_B)
if mibBuilder.loadTexts:slogEntryMessageText.setStatus(_A)
_SlogEntryName_Type=DisplayString
_SlogEntryName_Object=MibTableColumn
slogEntryName=_SlogEntryName_Object((1,3,6,1,4,1,97,3,28,5,1,4),_SlogEntryName_Type())
slogEntryName.setMaxAccess(_B)
if mibBuilder.loadTexts:slogEntryName.setStatus(_A)
_Strap_ObjectIdentity=ObjectIdentity
strap=_Strap_ObjectIdentity((1,3,6,1,4,1,97,3,29))
_StrapControlTable_Object=MibTable
strapControlTable=_StrapControlTable_Object((1,3,6,1,4,1,97,3,29,1))
if mibBuilder.loadTexts:strapControlTable.setStatus(_A)
_StrapControl_Object=MibTableRow
strapControl=_StrapControl_Object((1,3,6,1,4,1,97,3,29,1,1))
strapControl.setIndexNames((0,_E,_As))
if mibBuilder.loadTexts:strapControl.setStatus(_A)
_StrapIndex_Type=Integer32
_StrapIndex_Object=MibTableColumn
strapIndex=_StrapIndex_Object((1,3,6,1,4,1,97,3,29,1,1,1),_StrapIndex_Type())
strapIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:strapIndex.setStatus(_A)
class _StrapEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_StrapEnabled_Type.__name__=_D
_StrapEnabled_Object=MibTableColumn
strapEnabled=_StrapEnabled_Object((1,3,6,1,4,1,97,3,29,1,1,2),_StrapEnabled_Type())
strapEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:strapEnabled.setStatus(_A)
class _StrapSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_c,1),(_d,2),(_e,3),(_f,4),(_g,5)))
_StrapSeverity_Type.__name__=_D
_StrapSeverity_Object=MibTableColumn
strapSeverity=_StrapSeverity_Object((1,3,6,1,4,1,97,3,29,1,1,3),_StrapSeverity_Type())
strapSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:strapSeverity.setStatus(_A)
_StrapText_Type=DisplayString
_StrapText_Object=MibTableColumn
strapText=_StrapText_Object((1,3,6,1,4,1,97,3,29,1,1,4),_StrapText_Type())
strapText.setMaxAccess(_B)
if mibBuilder.loadTexts:strapText.setStatus(_A)
_StrapSeverityControlTable_Object=MibTable
strapSeverityControlTable=_StrapSeverityControlTable_Object((1,3,6,1,4,1,97,3,29,2))
if mibBuilder.loadTexts:strapSeverityControlTable.setStatus(_A)
_StrapSeverityControl_Object=MibTableRow
strapSeverityControl=_StrapSeverityControl_Object((1,3,6,1,4,1,97,3,29,2,1))
strapSeverityControl.setIndexNames((0,_E,_At))
if mibBuilder.loadTexts:strapSeverityControl.setStatus(_A)
class _StrapSeveritySeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_c,1),(_d,2),(_e,3),(_f,4),(_g,5)))
_StrapSeveritySeverity_Type.__name__=_D
_StrapSeveritySeverity_Object=MibTableColumn
strapSeveritySeverity=_StrapSeveritySeverity_Object((1,3,6,1,4,1,97,3,29,2,1,1),_StrapSeveritySeverity_Type())
strapSeveritySeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:strapSeveritySeverity.setStatus(_A)
class _StrapSeverityEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_StrapSeverityEnable_Type.__name__=_D
_StrapSeverityEnable_Object=MibTableColumn
strapSeverityEnable=_StrapSeverityEnable_Object((1,3,6,1,4,1,97,3,29,2,1,2),_StrapSeverityEnable_Type())
strapSeverityEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:strapSeverityEnable.setStatus(_A)
class _StrapIncludeText_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_StrapIncludeText_Type.__name__=_D
_StrapIncludeText_Object=MibScalar
strapIncludeText=_StrapIncludeText_Object((1,3,6,1,4,1,97,3,29,3),_StrapIncludeText_Type())
strapIncludeText.setMaxAccess(_C)
if mibBuilder.loadTexts:strapIncludeText.setStatus(_A)
_StrapTime_Type=TimeTicks
_StrapTime_Object=MibScalar
strapTime=_StrapTime_Object((1,3,6,1,4,1,97,3,29,4),_StrapTime_Type())
strapTime.setMaxAccess(_C)
if mibBuilder.loadTexts:strapTime.setStatus(_A)
_StrapRetry_Type=Integer32
_StrapRetry_Object=MibScalar
strapRetry=_StrapRetry_Object((1,3,6,1,4,1,97,3,29,5),_StrapRetry_Type())
strapRetry.setMaxAccess(_C)
if mibBuilder.loadTexts:strapRetry.setStatus(_A)
_StrapEntryNumber_Type=Integer32
_StrapEntryNumber_Object=MibScalar
strapEntryNumber=_StrapEntryNumber_Object((1,3,6,1,4,1,97,3,29,6),_StrapEntryNumber_Type())
strapEntryNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:strapEntryNumber.setStatus(_A)
_StrapTable_Object=MibTable
strapTable=_StrapTable_Object((1,3,6,1,4,1,97,3,29,7))
if mibBuilder.loadTexts:strapTable.setStatus(_A)
_StrapEntry_Object=MibTableRow
strapEntry=_StrapEntry_Object((1,3,6,1,4,1,97,3,29,7,1))
strapEntry.setIndexNames((0,_E,_Au))
if mibBuilder.loadTexts:strapEntry.setStatus(_A)
_StrapEntryIndex_Type=Integer32
_StrapEntryIndex_Object=MibTableColumn
strapEntryIndex=_StrapEntryIndex_Object((1,3,6,1,4,1,97,3,29,7,1,1),_StrapEntryIndex_Type())
strapEntryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:strapEntryIndex.setStatus(_A)
_StrapEntryTimeStamp_Type=TimeTicks
_StrapEntryTimeStamp_Object=MibTableColumn
strapEntryTimeStamp=_StrapEntryTimeStamp_Object((1,3,6,1,4,1,97,3,29,7,1,2),_StrapEntryTimeStamp_Type())
strapEntryTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:strapEntryTimeStamp.setStatus(_A)
_StrapEntryText_Type=DisplayString
_StrapEntryText_Object=MibTableColumn
strapEntryText=_StrapEntryText_Object((1,3,6,1,4,1,97,3,29,7,1,3),_StrapEntryText_Type())
strapEntryText.setMaxAccess(_B)
if mibBuilder.loadTexts:strapEntryText.setStatus(_A)
_StrapNumber_Type=Integer32
_StrapNumber_Object=MibTableColumn
strapNumber=_StrapNumber_Object((1,3,6,1,4,1,97,3,29,7,1,4),_StrapNumber_Type())
strapNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:strapNumber.setStatus(_A)
class _StrapEntrySeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_c,1),(_d,2),(_e,3),(_f,4),(_g,5)))
_StrapEntrySeverity_Type.__name__=_D
_StrapEntrySeverity_Object=MibTableColumn
strapEntrySeverity=_StrapEntrySeverity_Object((1,3,6,1,4,1,97,3,29,7,1,5),_StrapEntrySeverity_Type())
strapEntrySeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:strapEntrySeverity.setStatus(_A)
_Smirror_ObjectIdentity=ObjectIdentity
smirror=_Smirror_ObjectIdentity((1,3,6,1,4,1,97,3,30))
class _SmirrorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),('local',2),('remote',3)))
_SmirrorStatus_Type.__name__=_D
_SmirrorStatus_Object=MibScalar
smirrorStatus=_SmirrorStatus_Object((1,3,6,1,4,1,97,3,30,1),_SmirrorStatus_Type())
smirrorStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:smirrorStatus.setStatus(_A)
_SmirrorDiagPort_Type=Integer32
_SmirrorDiagPort_Object=MibScalar
smirrorDiagPort=_SmirrorDiagPort_Object((1,3,6,1,4,1,97,3,30,2),_SmirrorDiagPort_Type())
smirrorDiagPort.setMaxAccess(_C)
if mibBuilder.loadTexts:smirrorDiagPort.setStatus(_A)
_SmirrorIPaddr_Type=IpAddress
_SmirrorIPaddr_Object=MibScalar
smirrorIPaddr=_SmirrorIPaddr_Object((1,3,6,1,4,1,97,3,30,3),_SmirrorIPaddr_Type())
smirrorIPaddr.setMaxAccess(_C)
if mibBuilder.loadTexts:smirrorIPaddr.setStatus(_A)
_SmirrorTargetPortLists_Type=OctetString
_SmirrorTargetPortLists_Object=MibScalar
smirrorTargetPortLists=_SmirrorTargetPortLists_Object((1,3,6,1,4,1,97,3,30,4),_SmirrorTargetPortLists_Type())
smirrorTargetPortLists.setMaxAccess(_C)
if mibBuilder.loadTexts:smirrorTargetPortLists.setStatus(_A)
class _SmirrorOversizePkt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('discard',1),('truncate',2)))
_SmirrorOversizePkt_Type.__name__=_D
_SmirrorOversizePkt_Object=MibScalar
smirrorOversizePkt=_SmirrorOversizePkt_Object((1,3,6,1,4,1,97,3,30,5),_SmirrorOversizePkt_Type())
smirrorOversizePkt.setMaxAccess(_C)
if mibBuilder.loadTexts:smirrorOversizePkt.setStatus(_A)
_SmirrorEntryMirroredPkts_Type=Counter32
_SmirrorEntryMirroredPkts_Object=MibScalar
smirrorEntryMirroredPkts=_SmirrorEntryMirroredPkts_Object((1,3,6,1,4,1,97,3,30,6),_SmirrorEntryMirroredPkts_Type())
smirrorEntryMirroredPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:smirrorEntryMirroredPkts.setStatus(_A)
_SmirrorExitMirroredPkts_Type=Counter32
_SmirrorExitMirroredPkts_Object=MibScalar
smirrorExitMirroredPkts=_SmirrorExitMirroredPkts_Object((1,3,6,1,4,1,97,3,30,7),_SmirrorExitMirroredPkts_Type())
smirrorExitMirroredPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:smirrorExitMirroredPkts.setStatus(_A)
_SmirrorNotreadyDroppedPkts_Type=Counter32
_SmirrorNotreadyDroppedPkts_Object=MibScalar
smirrorNotreadyDroppedPkts=_SmirrorNotreadyDroppedPkts_Object((1,3,6,1,4,1,97,3,30,8),_SmirrorNotreadyDroppedPkts_Type())
smirrorNotreadyDroppedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:smirrorNotreadyDroppedPkts.setStatus(_A)
_SmirrorOversizeDroppedPkts_Type=Counter32
_SmirrorOversizeDroppedPkts_Object=MibScalar
smirrorOversizeDroppedPkts=_SmirrorOversizeDroppedPkts_Object((1,3,6,1,4,1,97,3,30,9),_SmirrorOversizeDroppedPkts_Type())
smirrorOversizeDroppedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:smirrorOversizeDroppedPkts.setStatus(_A)
_SmirrorEntryFilteredPkts_Type=Counter32
_SmirrorEntryFilteredPkts_Object=MibScalar
smirrorEntryFilteredPkts=_SmirrorEntryFilteredPkts_Object((1,3,6,1,4,1,97,3,30,10),_SmirrorEntryFilteredPkts_Type())
smirrorEntryFilteredPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:smirrorEntryFilteredPkts.setStatus(_A)
_SmirrorExitFilteredPkts_Type=Counter32
_SmirrorExitFilteredPkts_Object=MibScalar
smirrorExitFilteredPkts=_SmirrorExitFilteredPkts_Object((1,3,6,1,4,1,97,3,30,11),_SmirrorExitFilteredPkts_Type())
smirrorExitFilteredPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:smirrorExitFilteredPkts.setStatus(_A)
_SmirrorCongestionDroppedPkts_Type=Counter32
_SmirrorCongestionDroppedPkts_Object=MibScalar
smirrorCongestionDroppedPkts=_SmirrorCongestionDroppedPkts_Object((1,3,6,1,4,1,97,3,30,12),_SmirrorCongestionDroppedPkts_Type())
smirrorCongestionDroppedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:smirrorCongestionDroppedPkts.setStatus(_A)
_SmirrorNowrapperDroppedPkts_Type=Counter32
_SmirrorNowrapperDroppedPkts_Object=MibScalar
smirrorNowrapperDroppedPkts=_SmirrorNowrapperDroppedPkts_Object((1,3,6,1,4,1,97,3,30,13),_SmirrorNowrapperDroppedPkts_Type())
smirrorNowrapperDroppedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:smirrorNowrapperDroppedPkts.setStatus(_A)
class _SmirrorRemoteStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,6,7,8,9)));namedValues=NamedValues(*(('mirrorOff',0),('handshakeInProgress',1),('arpRefreshInProgress',2),('remoteHostUnreachable',3),('mirroring',6),('versionIncompatible',7),('remoteDiagnosticPortBroken',8),('remoteMirrorNotOn',9)))
_SmirrorRemoteStatus_Type.__name__=_D
_SmirrorRemoteStatus_Object=MibScalar
smirrorRemoteStatus=_SmirrorRemoteStatus_Object((1,3,6,1,4,1,97,3,30,14),_SmirrorRemoteStatus_Type())
smirrorRemoteStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:smirrorRemoteStatus.setStatus(_A)
_SmirrorRemoteExitPort_Type=Integer32
_SmirrorRemoteExitPort_Object=MibScalar
smirrorRemoteExitPort=_SmirrorRemoteExitPort_Object((1,3,6,1,4,1,97,3,30,15),_SmirrorRemoteExitPort_Type())
smirrorRemoteExitPort.setMaxAccess(_B)
if mibBuilder.loadTexts:smirrorRemoteExitPort.setStatus(_A)
_Sworkgroup_ObjectIdentity=ObjectIdentity
sworkgroup=_Sworkgroup_ObjectIdentity((1,3,6,1,4,1,97,3,31))
_SWorkGroupNextNumber_Type=Integer32
_SWorkGroupNextNumber_Object=MibScalar
sWorkGroupNextNumber=_SWorkGroupNextNumber_Object((1,3,6,1,4,1,97,3,31,1),_SWorkGroupNextNumber_Type())
sWorkGroupNextNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:sWorkGroupNextNumber.setStatus(_A)
_SWorkGroupCurrentCount_Type=Integer32
_SWorkGroupCurrentCount_Object=MibScalar
sWorkGroupCurrentCount=_SWorkGroupCurrentCount_Object((1,3,6,1,4,1,97,3,31,2),_SWorkGroupCurrentCount_Type())
sWorkGroupCurrentCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sWorkGroupCurrentCount.setStatus(_A)
_SWorkGroupMaxCount_Type=Integer32
_SWorkGroupMaxCount_Object=MibScalar
sWorkGroupMaxCount=_SWorkGroupMaxCount_Object((1,3,6,1,4,1,97,3,31,3),_SWorkGroupMaxCount_Type())
sWorkGroupMaxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sWorkGroupMaxCount.setStatus(_A)
_SWorkGroupTable_Object=MibTable
sWorkGroupTable=_SWorkGroupTable_Object((1,3,6,1,4,1,97,3,31,4))
if mibBuilder.loadTexts:sWorkGroupTable.setStatus(_A)
_SWorkGroupEntry_Object=MibTableRow
sWorkGroupEntry=_SWorkGroupEntry_Object((1,3,6,1,4,1,97,3,31,4,1))
sWorkGroupEntry.setIndexNames((0,_E,_Av))
if mibBuilder.loadTexts:sWorkGroupEntry.setStatus(_A)
_SWorkGroupNumber_Type=Integer32
_SWorkGroupNumber_Object=MibTableColumn
sWorkGroupNumber=_SWorkGroupNumber_Object((1,3,6,1,4,1,97,3,31,4,1,1),_SWorkGroupNumber_Type())
sWorkGroupNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:sWorkGroupNumber.setStatus(_A)
_SWorkGroupName_Type=DisplayString
_SWorkGroupName_Object=MibTableColumn
sWorkGroupName=_SWorkGroupName_Object((1,3,6,1,4,1,97,3,31,4,1,2),_SWorkGroupName_Type())
sWorkGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:sWorkGroupName.setStatus(_A)
_SWorkGroupPorts_Type=OctetString
_SWorkGroupPorts_Object=MibTableColumn
sWorkGroupPorts=_SWorkGroupPorts_Object((1,3,6,1,4,1,97,3,31,4,1,3),_SWorkGroupPorts_Type())
sWorkGroupPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:sWorkGroupPorts.setStatus(_A)
class _SWorkGroupType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ip',1),('ipx',2),('all',3),(_K,4)))
_SWorkGroupType_Type.__name__=_D
_SWorkGroupType_Object=MibTableColumn
sWorkGroupType=_SWorkGroupType_Object((1,3,6,1,4,1,97,3,31,4,1,4),_SWorkGroupType_Type())
sWorkGroupType.setMaxAccess(_C)
if mibBuilder.loadTexts:sWorkGroupType.setStatus(_A)
_SWorkGroupIpAddress_Type=IpAddress
_SWorkGroupIpAddress_Object=MibTableColumn
sWorkGroupIpAddress=_SWorkGroupIpAddress_Object((1,3,6,1,4,1,97,3,31,4,1,5),_SWorkGroupIpAddress_Type())
sWorkGroupIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:sWorkGroupIpAddress.setStatus(_A)
_SWorkGroupIpMask_Type=IpAddress
_SWorkGroupIpMask_Object=MibTableColumn
sWorkGroupIpMask=_SWorkGroupIpMask_Object((1,3,6,1,4,1,97,3,31,4,1,6),_SWorkGroupIpMask_Type())
sWorkGroupIpMask.setMaxAccess(_C)
if mibBuilder.loadTexts:sWorkGroupIpMask.setStatus(_A)
_SWorkGroupIpxNetwork_Type=OctetString
_SWorkGroupIpxNetwork_Object=MibTableColumn
sWorkGroupIpxNetwork=_SWorkGroupIpxNetwork_Object((1,3,6,1,4,1,97,3,31,4,1,7),_SWorkGroupIpxNetwork_Type())
sWorkGroupIpxNetwork.setMaxAccess(_C)
if mibBuilder.loadTexts:sWorkGroupIpxNetwork.setStatus(_A)
_Sping_ObjectIdentity=ObjectIdentity
sping=_Sping_ObjectIdentity((1,3,6,1,4,1,97,3,32))
_SpingDataTimeout_Type=TimeTicks
_SpingDataTimeout_Object=MibScalar
spingDataTimeout=_SpingDataTimeout_Object((1,3,6,1,4,1,97,3,32,1),_SpingDataTimeout_Type())
spingDataTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:spingDataTimeout.setStatus(_A)
_SpingTable_Object=MibTable
spingTable=_SpingTable_Object((1,3,6,1,4,1,97,3,32,2))
if mibBuilder.loadTexts:spingTable.setStatus(_A)
_SpingEntry_Object=MibTableRow
spingEntry=_SpingEntry_Object((1,3,6,1,4,1,97,3,32,2,1))
spingEntry.setIndexNames((0,_E,_Aw),(0,_E,_Ax))
if mibBuilder.loadTexts:spingEntry.setStatus(_A)
_SpingNMSAddr_Type=IpAddress
_SpingNMSAddr_Object=MibTableColumn
spingNMSAddr=_SpingNMSAddr_Object((1,3,6,1,4,1,97,3,32,2,1,1),_SpingNMSAddr_Type())
spingNMSAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:spingNMSAddr.setStatus(_A)
_SpingDestAddr_Type=IpAddress
_SpingDestAddr_Object=MibTableColumn
spingDestAddr=_SpingDestAddr_Object((1,3,6,1,4,1,97,3,32,2,1,2),_SpingDestAddr_Type())
spingDestAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:spingDestAddr.setStatus(_A)
class _SpingState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_Ay,0),('active',1),('timed-out',2),(_Az,3)))
_SpingState_Type.__name__=_D
_SpingState_Object=MibTableColumn
spingState=_SpingState_Object((1,3,6,1,4,1,97,3,32,2,1,3),_SpingState_Type())
spingState.setMaxAccess(_B)
if mibBuilder.loadTexts:spingState.setStatus(_A)
_SpingCount_Type=Integer32
_SpingCount_Object=MibTableColumn
spingCount=_SpingCount_Object((1,3,6,1,4,1,97,3,32,2,1,4),_SpingCount_Type())
spingCount.setMaxAccess(_C)
if mibBuilder.loadTexts:spingCount.setStatus(_A)
_SpingDataSize_Type=Integer32
_SpingDataSize_Object=MibTableColumn
spingDataSize=_SpingDataSize_Object((1,3,6,1,4,1,97,3,32,2,1,5),_SpingDataSize_Type())
spingDataSize.setMaxAccess(_C)
if mibBuilder.loadTexts:spingDataSize.setStatus(_A)
_SpingWait_Type=TimeTicks
_SpingWait_Object=MibTableColumn
spingWait=_SpingWait_Object((1,3,6,1,4,1,97,3,32,2,1,6),_SpingWait_Type())
spingWait.setMaxAccess(_C)
if mibBuilder.loadTexts:spingWait.setStatus(_A)
_SpingTimeout_Type=TimeTicks
_SpingTimeout_Object=MibTableColumn
spingTimeout=_SpingTimeout_Object((1,3,6,1,4,1,97,3,32,2,1,7),_SpingTimeout_Type())
spingTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:spingTimeout.setStatus(_A)
class _SpingOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),(_L,2)))
_SpingOperation_Type.__name__=_D
_SpingOperation_Object=MibTableColumn
spingOperation=_SpingOperation_Object((1,3,6,1,4,1,97,3,32,2,1,8),_SpingOperation_Type())
spingOperation.setMaxAccess(_C)
if mibBuilder.loadTexts:spingOperation.setStatus(_A)
_SpingMin_Type=TimeTicks
_SpingMin_Object=MibTableColumn
spingMin=_SpingMin_Object((1,3,6,1,4,1,97,3,32,2,1,9),_SpingMin_Type())
spingMin.setMaxAccess(_B)
if mibBuilder.loadTexts:spingMin.setStatus(_A)
_SpingMax_Type=TimeTicks
_SpingMax_Object=MibTableColumn
spingMax=_SpingMax_Object((1,3,6,1,4,1,97,3,32,2,1,10),_SpingMax_Type())
spingMax.setMaxAccess(_B)
if mibBuilder.loadTexts:spingMax.setStatus(_A)
_SpingAvg_Type=TimeTicks
_SpingAvg_Object=MibTableColumn
spingAvg=_SpingAvg_Object((1,3,6,1,4,1,97,3,32,2,1,11),_SpingAvg_Type())
spingAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:spingAvg.setStatus(_A)
_SpingNumTransmitted_Type=Integer32
_SpingNumTransmitted_Object=MibTableColumn
spingNumTransmitted=_SpingNumTransmitted_Object((1,3,6,1,4,1,97,3,32,2,1,12),_SpingNumTransmitted_Type())
spingNumTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:spingNumTransmitted.setStatus(_A)
_SpingNumReceived_Type=Integer32
_SpingNumReceived_Object=MibTableColumn
spingNumReceived=_SpingNumReceived_Object((1,3,6,1,4,1,97,3,32,2,1,13),_SpingNumReceived_Type())
spingNumReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:spingNumReceived.setStatus(_A)
_Strace_ObjectIdentity=ObjectIdentity
strace=_Strace_ObjectIdentity((1,3,6,1,4,1,97,3,33))
_StraceDataTimeout_Type=TimeTicks
_StraceDataTimeout_Object=MibScalar
straceDataTimeout=_StraceDataTimeout_Object((1,3,6,1,4,1,97,3,33,1),_StraceDataTimeout_Type())
straceDataTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:straceDataTimeout.setStatus(_A)
_StraceTable_Object=MibTable
straceTable=_StraceTable_Object((1,3,6,1,4,1,97,3,33,2))
if mibBuilder.loadTexts:straceTable.setStatus(_A)
_StraceEntry_Object=MibTableRow
straceEntry=_StraceEntry_Object((1,3,6,1,4,1,97,3,33,2,1))
straceEntry.setIndexNames((0,_E,_A_),(0,_E,_B0),(0,_E,_B1),(0,_E,_B2))
if mibBuilder.loadTexts:straceEntry.setStatus(_A)
_StraceNMSAddr_Type=IpAddress
_StraceNMSAddr_Object=MibTableColumn
straceNMSAddr=_StraceNMSAddr_Object((1,3,6,1,4,1,97,3,33,2,1,1),_StraceNMSAddr_Type())
straceNMSAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:straceNMSAddr.setStatus(_A)
_StraceDestAddr_Type=IpAddress
_StraceDestAddr_Object=MibTableColumn
straceDestAddr=_StraceDestAddr_Object((1,3,6,1,4,1,97,3,33,2,1,2),_StraceDestAddr_Type())
straceDestAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:straceDestAddr.setStatus(_A)
_StraceMaxTTL_Type=Integer32
_StraceMaxTTL_Object=MibTableColumn
straceMaxTTL=_StraceMaxTTL_Object((1,3,6,1,4,1,97,3,33,2,1,3),_StraceMaxTTL_Type())
straceMaxTTL.setMaxAccess(_C)
if mibBuilder.loadTexts:straceMaxTTL.setStatus(_A)
_StraceDataSize_Type=Integer32
_StraceDataSize_Object=MibTableColumn
straceDataSize=_StraceDataSize_Object((1,3,6,1,4,1,97,3,33,2,1,4),_StraceDataSize_Type())
straceDataSize.setMaxAccess(_C)
if mibBuilder.loadTexts:straceDataSize.setStatus(_A)
_StraceNumProbes_Type=Integer32
_StraceNumProbes_Object=MibTableColumn
straceNumProbes=_StraceNumProbes_Object((1,3,6,1,4,1,97,3,33,2,1,5),_StraceNumProbes_Type())
straceNumProbes.setMaxAccess(_C)
if mibBuilder.loadTexts:straceNumProbes.setStatus(_A)
_StraceWait_Type=TimeTicks
_StraceWait_Object=MibTableColumn
straceWait=_StraceWait_Object((1,3,6,1,4,1,97,3,33,2,1,6),_StraceWait_Type())
straceWait.setMaxAccess(_C)
if mibBuilder.loadTexts:straceWait.setStatus(_A)
class _StraceOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),(_L,2)))
_StraceOperation_Type.__name__=_D
_StraceOperation_Object=MibTableColumn
straceOperation=_StraceOperation_Object((1,3,6,1,4,1,97,3,33,2,1,7),_StraceOperation_Type())
straceOperation.setMaxAccess(_C)
if mibBuilder.loadTexts:straceOperation.setStatus(_A)
_StraceHop_Type=Integer32
_StraceHop_Object=MibTableColumn
straceHop=_StraceHop_Object((1,3,6,1,4,1,97,3,33,2,1,8),_StraceHop_Type())
straceHop.setMaxAccess(_B)
if mibBuilder.loadTexts:straceHop.setStatus(_A)
_StraceHopAddress_Type=IpAddress
_StraceHopAddress_Object=MibTableColumn
straceHopAddress=_StraceHopAddress_Object((1,3,6,1,4,1,97,3,33,2,1,9),_StraceHopAddress_Type())
straceHopAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:straceHopAddress.setStatus(_A)
_StraceProbe_Type=Integer32
_StraceProbe_Object=MibTableColumn
straceProbe=_StraceProbe_Object((1,3,6,1,4,1,97,3,33,2,1,10),_StraceProbe_Type())
straceProbe.setMaxAccess(_B)
if mibBuilder.loadTexts:straceProbe.setStatus(_A)
class _StraceState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_Ay,0),('active',1),('time-exceeded',2),('host-unreachable',3),('net-unreachable',4),(_Az,5)))
_StraceState_Type.__name__=_D
_StraceState_Object=MibTableColumn
straceState=_StraceState_Object((1,3,6,1,4,1,97,3,33,2,1,11),_StraceState_Type())
straceState.setMaxAccess(_B)
if mibBuilder.loadTexts:straceState.setStatus(_A)
_StraceTime_Type=TimeTicks
_StraceTime_Object=MibTableColumn
straceTime=_StraceTime_Object((1,3,6,1,4,1,97,3,33,2,1,12),_StraceTime_Type())
straceTime.setMaxAccess(_B)
if mibBuilder.loadTexts:straceTime.setStatus(_A)
_Srtb_ObjectIdentity=ObjectIdentity
srtb=_Srtb_ObjectIdentity((1,3,6,1,4,1,97,3,34))
class _SrtbProto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,7)));namedValues=NamedValues(*((_L,0),('ip',1),('ipx',2),('others',3),('all',7)))
_SrtbProto_Type.__name__=_D
_SrtbProto_Object=MibScalar
srtbProto=_SrtbProto_Object((1,3,6,1,4,1,97,3,34,1),_SrtbProto_Type())
srtbProto.setMaxAccess(_C)
if mibBuilder.loadTexts:srtbProto.setStatus(_A)
class _SrtbExplorer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('are',1),('ste',2)))
_SrtbExplorer_Type.__name__=_D
_SrtbExplorer_Object=MibScalar
srtbExplorer=_SrtbExplorer_Object((1,3,6,1,4,1,97,3,34,2),_SrtbExplorer_Type())
srtbExplorer.setMaxAccess(_C)
if mibBuilder.loadTexts:srtbExplorer.setStatus(_A)
_SrtbAgingTime_Type=Integer32
_SrtbAgingTime_Object=MibScalar
srtbAgingTime=_SrtbAgingTime_Object((1,3,6,1,4,1,97,3,34,3),_SrtbAgingTime_Type())
srtbAgingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:srtbAgingTime.setStatus(_A)
_Nbcache_ObjectIdentity=ObjectIdentity
nbcache=_Nbcache_ObjectIdentity((1,3,6,1,4,1,97,3,35))
_NbCacheifTable_Object=MibTable
nbCacheifTable=_NbCacheifTable_Object((1,3,6,1,4,1,97,3,35,3))
if mibBuilder.loadTexts:nbCacheifTable.setStatus(_A)
_NbCacheifEntry_Object=MibTableRow
nbCacheifEntry=_NbCacheifEntry_Object((1,3,6,1,4,1,97,3,35,3,1))
nbCacheifEntry.setIndexNames((0,_E,_B3))
if mibBuilder.loadTexts:nbCacheifEntry.setStatus(_A)
_NbCacheIfIndex_Type=Integer32
_NbCacheIfIndex_Object=MibTableColumn
nbCacheIfIndex=_NbCacheIfIndex_Object((1,3,6,1,4,1,97,3,35,3,1,1),_NbCacheIfIndex_Type())
nbCacheIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbCacheIfIndex.setStatus(_A)
class _NbCacheIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_NbCacheIfOperStatus_Type.__name__=_D
_NbCacheIfOperStatus_Object=MibTableColumn
nbCacheIfOperStatus=_NbCacheIfOperStatus_Object((1,3,6,1,4,1,97,3,35,3,1,2),_NbCacheIfOperStatus_Type())
nbCacheIfOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbCacheIfOperStatus.setStatus(_A)
_Atext_ObjectIdentity=ObjectIdentity
atext=_Atext_ObjectIdentity((1,3,6,1,4,1,97,6))
_Atextsystem_ObjectIdentity=ObjectIdentity
atextsystem=_Atextsystem_ObjectIdentity((1,3,6,1,4,1,97,6,1))
class _AtextsysOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),('on',2)))
_AtextsysOperState_Type.__name__=_D
_AtextsysOperState_Object=MibScalar
atextsysOperState=_AtextsysOperState_Object((1,3,6,1,4,1,97,6,1,1),_AtextsysOperState_Type())
atextsysOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:atextsysOperState.setStatus(_A)
_Atextport_ObjectIdentity=ObjectIdentity
atextport=_Atextport_ObjectIdentity((1,3,6,1,4,1,97,6,2))
_AtextportTable_Object=MibTable
atextportTable=_AtextportTable_Object((1,3,6,1,4,1,97,6,2,1))
if mibBuilder.loadTexts:atextportTable.setStatus(_A)
_AtextportEntry_Object=MibTableRow
atextportEntry=_AtextportEntry_Object((1,3,6,1,4,1,97,6,2,1,1))
atextportEntry.setIndexNames((0,_E,_B4))
if mibBuilder.loadTexts:atextportEntry.setStatus(_A)
_AtextportIndex_Type=Integer32
_AtextportIndex_Object=MibTableColumn
atextportIndex=_AtextportIndex_Object((1,3,6,1,4,1,97,6,2,1,1,1),_AtextportIndex_Type())
atextportIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atextportIndex.setStatus(_A)
_AtextportNetStart_Type=OctetString
_AtextportNetStart_Object=MibTableColumn
atextportNetStart=_AtextportNetStart_Object((1,3,6,1,4,1,97,6,2,1,1,2),_AtextportNetStart_Type())
atextportNetStart.setMaxAccess(_B)
if mibBuilder.loadTexts:atextportNetStart.setStatus(_A)
_AtextportNetEnd_Type=OctetString
_AtextportNetEnd_Object=MibTableColumn
atextportNetEnd=_AtextportNetEnd_Object((1,3,6,1,4,1,97,6,2,1,1,3),_AtextportNetEnd_Type())
atextportNetEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:atextportNetEnd.setStatus(_A)
_AtextportNetAddress_Type=OctetString
_AtextportNetAddress_Object=MibTableColumn
atextportNetAddress=_AtextportNetAddress_Object((1,3,6,1,4,1,97,6,2,1,1,4),_AtextportNetAddress_Type())
atextportNetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:atextportNetAddress.setStatus(_A)
_AtextportZone_Type=OctetString
_AtextportZone_Object=MibTableColumn
atextportZone=_AtextportZone_Object((1,3,6,1,4,1,97,6,2,1,1,5),_AtextportZone_Type())
atextportZone.setMaxAccess(_B)
if mibBuilder.loadTexts:atextportZone.setStatus(_A)
_AtextportzipTable_Object=MibTable
atextportzipTable=_AtextportzipTable_Object((1,3,6,1,4,1,97,6,2,2))
if mibBuilder.loadTexts:atextportzipTable.setStatus(_A)
_AtextportzipEntry_Object=MibTableRow
atextportzipEntry=_AtextportzipEntry_Object((1,3,6,1,4,1,97,6,2,2,1))
atextportzipEntry.setIndexNames((0,_E,_B5),(0,_E,_B6))
if mibBuilder.loadTexts:atextportzipEntry.setStatus(_A)
_AtextportZonePort_Type=Integer32
_AtextportZonePort_Object=MibTableColumn
atextportZonePort=_AtextportZonePort_Object((1,3,6,1,4,1,97,6,2,2,1,1),_AtextportZonePort_Type())
atextportZonePort.setMaxAccess(_B)
if mibBuilder.loadTexts:atextportZonePort.setStatus(_A)
_AtextportZoneIndex_Type=Integer32
_AtextportZoneIndex_Object=MibTableColumn
atextportZoneIndex=_AtextportZoneIndex_Object((1,3,6,1,4,1,97,6,2,2,1,2),_AtextportZoneIndex_Type())
atextportZoneIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atextportZoneIndex.setStatus(_A)
_AtextportZoneName_Type=OctetString
_AtextportZoneName_Object=MibTableColumn
atextportZoneName=_AtextportZoneName_Object((1,3,6,1,4,1,97,6,2,2,1,3),_AtextportZoneName_Type())
atextportZoneName.setMaxAccess(_B)
if mibBuilder.loadTexts:atextportZoneName.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'Boolean':Boolean,'sigma':sigma,'sys':sys,'sysID':sysID,'sysReset':sysReset,'sysTrapAck':sysTrapAck,'sysTrapTime':sysTrapTime,'sysTrapRetry':sysTrapRetry,'sysTrapPort':sysTrapPort,'ecs-1':ecs_1,'hw':hw,'hwNumber':hwNumber,'hwSlotTable':hwSlotTable,'hwEntry':hwEntry,_h:hwIndex,'hwType':hwType,'hwUseMod':hwUseMod,'hwDefType':hwDefType,'hwDiagStatus':hwDiagStatus,'hwInuse':hwInuse,'hwDiagCode':hwDiagCode,'hwManufData':hwManufData,'hwPortType':hwPortType,'hwPortStatus':hwPortStatus,'hwUsePort':hwUsePort,'hwDefPortType':hwDefPortType,'hwAddr1':hwAddr1,'hwAddr2':hwAddr2,'hwAddr3':hwAddr3,'hwAddr4':hwAddr4,'hwTempOK':hwTempOK,'hwFirstPort':hwFirstPort,'hwFatalErr':hwFatalErr,'hwRptrPorts':hwRptrPorts,'hwPortSubType':hwPortSubType,'hwAddr5':hwAddr5,'hwAddr6':hwAddr6,'hwAddr7':hwAddr7,'hwAddr8':hwAddr8,'hwSysBus':hwSysBus,'hwPpeType':hwPpeType,'hwSysProcessor':hwSysProcessor,'sw':sw,'swNumber':swNumber,'swFilesetTable':swFilesetTable,'swFileset':swFileset,_i:swIndex,'swDesc':swDesc,'swCount':swCount,'swTypes':swTypes,'swSizes':swSizes,'swStarts':swStarts,'swBases':swBases,'swFlashBank':swFlashBank,'admin':admin,'config':config,'configFatalErr':configFatalErr,'configAnyPass':configAnyPass,'configGetPass':configGetPass,'configNMSAddress':configNMSAddress,'configFunctions':configFunctions,'configPowerAc1':configPowerAc1,'configPowerAc2':configPowerAc2,'configPowerDc1':configPowerDc1,'configPowerDc2':configPowerDc2,'configPowerPresent1':configPowerPresent1,'configPowerPresent2':configPowerPresent2,'configAlarmDynamic':configAlarmDynamic,'configAlarmAddresses':configAlarmAddresses,'configStorageFailure':configStorageFailure,'configAuthenticationFailure':configAuthenticationFailure,'configFddiPriority':configFddiPriority,'configTprPriority':configTprPriority,'configDumpModule':configDumpModule,'configDumpStart':configDumpStart,'configDumpEnd':configDumpEnd,'lma':lma,'lmaAllAddr':lmaAllAddr,'lmaAnyAddr':lmaAnyAddr,'ppe':ppe,'ppeLrgUxRxCnt':ppeLrgUxRxCnt,'ppeSmlUxRxCnt':ppeSmlUxRxCnt,'ppeUxTxCnt':ppeUxTxCnt,'ppeSmlBuffSize':ppeSmlBuffSize,'ppeBridgingMemory':ppeBridgingMemory,'ppeExtendStats':ppeExtendStats,'ppeBAddrLimit':ppeBAddrLimit,'ppeTxCongests':ppeTxCongests,'ppeArpEntries':ppeArpEntries,'ppeArpStatics':ppeArpStatics,'ppeArpOverflows':ppeArpOverflows,'ppeIpEntries':ppeIpEntries,'ppeIpStatics':ppeIpStatics,'ppeStaticPreference':ppeStaticPreference,'ppeOspfPreference':ppeOspfPreference,'ppeRipPreference':ppeRipPreference,'ppeEgpPreference':ppeEgpPreference,'ppeCpuUtilization':ppeCpuUtilization,'ppeRipRouteDiscards':ppeRipRouteDiscards,'ppeOspfRouteDiscards':ppeOspfRouteDiscards,'ppeRouteMemorySize':ppeRouteMemorySize,'ppeRouteMemoryAvail':ppeRouteMemoryAvail,'ppeRouteMemoryFailures':ppeRouteMemoryFailures,'ppePacketMemorySize':ppePacketMemorySize,'ppePacketMemoryAvail':ppePacketMemoryAvail,'ppePacketMemoryFailures':ppePacketMemoryFailures,'ppeOspfPduMemoryFailures':ppeOspfPduMemoryFailures,'ppeOspfPduMemoryAllocs':ppeOspfPduMemoryAllocs,'ppeIcmpPduMemoryFailures':ppeIcmpPduMemoryFailures,'ppeIcmpPduMemoryAllocs':ppeIcmpPduMemoryAllocs,'ppeRipPduMemoryFailures':ppeRipPduMemoryFailures,'ppeRipPduMemoryAllocs':ppeRipPduMemoryAllocs,'ppeBootpPduMemoryFailures':ppeBootpPduMemoryFailures,'ppeBootpPduMemoryAllocs':ppeBootpPduMemoryAllocs,'ppeSnmpPduMemoryFailures':ppeSnmpPduMemoryFailures,'ppeSnmpPduMemoryAllocs':ppeSnmpPduMemoryAllocs,'ppeTftpPduMemoryFailures':ppeTftpPduMemoryFailures,'ppeTftpPduMemoryAllocs':ppeTftpPduMemoryAllocs,'ppeTraceroutePduMemoryFailures':ppeTraceroutePduMemoryFailures,'ppeTraceroutePduMemoryAllocs':ppeTraceroutePduMemoryAllocs,'ppeArpPduMemoryFailures':ppeArpPduMemoryFailures,'ppeArpPduMemoryAllocs':ppeArpPduMemoryAllocs,'ppeIgmpPduMemoryFailures':ppeIgmpPduMemoryFailures,'ppeIgmpPduMemoryAllocs':ppeIgmpPduMemoryAllocs,'ppeAresAsStes':ppeAresAsStes,'ppeRoutePercent':ppeRoutePercent,'ppeMgtMemorySize':ppeMgtMemorySize,'ppeMgtMemoryAvail':ppeMgtMemoryAvail,'ppeMgtMemoryFailures':ppeMgtMemoryFailures,'st':st,'stGroupAddr':stGroupAddr,'stResAddr':stResAddr,'stBridgeId':stBridgeId,'stRootMaxAge':stRootMaxAge,'stRootHello':stRootHello,'stRootDelay':stRootDelay,'stRootID':stRootID,'stRootCost':stRootCost,'stRootPort':stRootPort,'stTopChange':stTopChange,'stActMaxAge':stActMaxAge,'stActHello':stActHello,'stActDelay':stActDelay,'stTopChangeCount':stTopChangeCount,'stTopChangeTime':stTopChangeTime,'stAgeTime':stAgeTime,'mesh':mesh,'meshCostPercent':meshCostPercent,'meshCost':meshCost,'meshCostChange':meshCostChange,'meshCostChangeCount':meshCostChangeCount,'meshCostChangeTime':meshCostChangeTime,'meshSubnet':meshSubnet,'swdis':swdis,'swdisDesc':swdisDesc,'swdisAccess':swdisAccess,'swdisWriteStatus':swdisWriteStatus,'swdisConfigIp':swdisConfigIp,'swdisConfigRetryTime':swdisConfigRetryTime,'swdisConfigTotalTimeout':swdisConfigTotalTimeout,'addr':addr,'addrStatics':addrStatics,'addrDynamics':addrDynamics,'addrDynamicMax':addrDynamicMax,'addrMeshs':addrMeshs,'addrDynamicOverflows':addrDynamicOverflows,'addrMeshOverflows':addrMeshOverflows,'addrFlags':addrFlags,'addrMAC':addrMAC,'addrPort':addrPort,'addrPortMap':addrPortMap,'addrOperation':addrOperation,'addrIndex':addrIndex,'addrNext':addrNext,'addrAge':addrAge,'addrRxPkts':addrRxPkts,'addrRxChars':addrRxChars,'addrRxMultiPkts':addrRxMultiPkts,'addrRxFwdPkts':addrRxFwdPkts,'addrTxPkts':addrTxPkts,'addrTxChars':addrTxChars,'addrBlockSize':addrBlockSize,'addrBlock':addrBlock,'addrAlarmMAC':addrAlarmMAC,'addrRptrPort':addrRptrPort,'snmpsmt':snmpsmt,'snmpsmtUpstreamReq':snmpsmtUpstreamReq,'snmpsmtUpstreamRsp':snmpsmtUpstreamRsp,'snmpsmtUpstreamDescriptor':snmpsmtUpstreamDescriptor,'snmpsmtUpstreamState':snmpsmtUpstreamState,'fddismtTable':fddismtTable,'fddismtEntry':fddismtEntry,_q:fddismtIndex,'fddismtUpstreamReq':fddismtUpstreamReq,'fddismtUpstreamRsp':fddismtUpstreamRsp,'fddismtUpstreamDescriptor':fddismtUpstreamDescriptor,'fddismtUpstreamState':fddismtUpstreamState,'sinterfaces':sinterfaces,'sifUX':sifUX,'sifTable':sifTable,'sifEntry':sifEntry,_r:sifIndex,'sifSmlRxCnt':sifSmlRxCnt,'sifLrgRxCnt':sifLrgRxCnt,'sifUxTxCnt':sifUxTxCnt,'sifThreshold':sifThreshold,'sifThresholdTime':sifThresholdTime,'sifRxQueueThresh':sifRxQueueThresh,'sifRxQueueThreshTime':sifRxQueueThreshTime,'sifTxStormCnt':sifTxStormCnt,'sifTxStormTime':sifTxStormTime,'sifFilterFlags':sifFilterFlags,'sifCongestTime':sifCongestTime,'sifQueueTime':sifQueueTime,'sifPortCost':sifPortCost,'sifStPriority':sifStPriority,'sifFunctions':sifFunctions,'sifCongested':sifCongested,'sifState':sifState,'sifDesigCost':sifDesigCost,'sifDesigRoot':sifDesigRoot,'sifDesigBridge':sifDesigBridge,'sifDesigPort':sifDesigPort,'sifRxPackets':sifRxPackets,'sifRxChar0s':sifRxChar0s,'sifRxChar1s':sifRxChar1s,'sifRxSizeErrors':sifRxSizeErrors,'sifRxHwFCSs':sifRxHwFCSs,'sifRxQueues':sifRxQueues,'sifTxPackets':sifTxPackets,'sifTxCongests':sifTxCongests,'sifTxStorms':sifTxStorms,'sifTxDests':sifTxDests,'sifErrorsFlag':sifErrorsFlag,'sifTxStormFlag':sifTxStormFlag,'sifTxSizes':sifTxSizes,'sifTxAddr':sifTxAddr,'sifLan':sifLan,'sifStatisticsTime':sifStatisticsTime,'sifIpAddress':sifIpAddress,'sifIpGroupAddress':sifIpGroupAddress,'sifMaxPacketSize':sifMaxPacketSize,'sifExpectSqe':sifExpectSqe,'sifFilterLocal':sifFilterLocal,'sifInQLen':sifInQLen,'sifFrameSwitching':sifFrameSwitching,'sifRingDrops':sifRingDrops,'sifAdapterChecks':sifAdapterChecks,'sifIpRipPortMetric':sifIpRipPortMetric,'sifDescr':sifDescr,'sifUtilInterval':sifUtilInterval,'sifUtilCount':sifUtilCount,'sifUtilPortPeakReset':sifUtilPortPeakReset,'sifUtilPortPeakTable':sifUtilPortPeakTable,'sifUtilPortPeakEntry':sifUtilPortPeakEntry,_s:sifUtilPortPeakIndex,_t:sifUtilPortPeakOrdinal,'sifUtilPortPeakBRTimestamp':sifUtilPortPeakBRTimestamp,'sifUtilPortPeakTBitRate':sifUtilPortPeakTBitRate,'sifUtilPortPeakRBitRate':sifUtilPortPeakRBitRate,'sifUtilSysPeakReset':sifUtilSysPeakReset,'sifUtilSysPeakTable':sifUtilSysPeakTable,'sifUtilSysPeakEntry':sifUtilSysPeakEntry,_u:sifUtilSysPeakIndex,_v:sifUtilSysPeakOrdinal,'sifUtilSysPeakTimestamp':sifUtilSysPeakTimestamp,'sifUtilSysPeakTBitRate':sifUtilSysPeakTBitRate,'sifUtilSysPeakRBitRate':sifUtilSysPeakRBitRate,'sfddi':sfddi,'sfddiTable':sfddiTable,'sfddiEntry':sfddiEntry,_w:sfddiIndex,'sfddiRxHwAborts':sfddiRxHwAborts,'sfddiRxParitys':sfddiRxParitys,'sfddiRxShorts':sfddiRxShorts,'sfddiDpcErrCnts':sfddiDpcErrCnts,'sfddiDpcErrValue':sfddiDpcErrValue,'sfddiRbcErrCnts':sfddiRbcErrCnts,'sfddiRbcErrValue':sfddiRbcErrValue,'sfddiTxAsync':sfddiTxAsync,'sfddiShortAddressing':sfddiShortAddressing,'sfddiSmtConditions':sfddiSmtConditions,'sfddiSrfConditions':sfddiSrfConditions,'sfddiSmtConditionsStatus':sfddiSmtConditionsStatus,'sfddiSrfConditionsStatus':sfddiSrfConditionsStatus,'sfddiSrfReportLimit':sfddiSrfReportLimit,'sfddiFrameErrorThreshold':sfddiFrameErrorThreshold,'sfddiNotCopiedThreshold':sfddiNotCopiedThreshold,'sfddiSBFlag':sfddiSBFlag,'sfddiRxEbits':sfddiRxEbits,'sfddiOBSFuseBad':sfddiOBSFuseBad,'sfddiThruB':sfddiThruB,'sfddiStationDescriptor':sfddiStationDescriptor,'sfddiStationState':sfddiStationState,'sfddiDownstreamNbr':sfddiDownstreamNbr,'sfddiSMTBufferSize':sfddiSMTBufferSize,'suart':suart,'suartTable':suartTable,'suartEntry':suartEntry,_x:suartIndex,'suartBaud':suartBaud,'suartModem':suartModem,'suartIpNeighborAddress':suartIpNeighborAddress,'suartPPPActive':suartPPPActive,'suartAlignmentErrors':suartAlignmentErrors,'suartOverrunErrors':suartOverrunErrors,'filter':filter,'filterMaxCount':filterMaxCount,'filterCurrentCount':filterCurrentCount,'filterDeleteID':filterDeleteID,'filterNextID':filterNextID,'filterAddID':filterAddID,'filterAddIndex':filterAddIndex,'filterTable':filterTable,'filterEntry':filterEntry,_A8:filterIndex,'filterID':filterID,'filterPortNo':filterPortNo,'filterComboType':filterComboType,'filterFlags':filterFlags,'filterFrame':filterFrame,'filterSource':filterSource,'filterSourceEnd':filterSourceEnd,'filterDest':filterDest,'filterDestEnd':filterDestEnd,'filterSourceMask':filterSourceMask,'filterDestMask':filterDestMask,'filterSrcLan':filterSrcLan,'filterOffset':filterOffset,'filterField':filterField,'filterMask':filterMask,'filterThreshold':filterThreshold,'filterThreshTime':filterThreshTime,'filterThreshFlag':filterThreshFlag,'filterPktCnts':filterPktCnts,'filterLastSrc':filterLastSrc,'reboot':reboot,'rebootBridgingMemory':rebootBridgingMemory,'rebootSlotTable':rebootSlotTable,'rebootEntry':rebootEntry,_A9:rebootIndex,'rebootType':rebootType,'rebootUseMod':rebootUseMod,'rebootPortType':rebootPortType,'rebootConfig':rebootConfig,'rebootRouteMemory':rebootRouteMemory,'debug':debug,'debugStringID':debugStringID,'debugString':debugString,'debugTable':debugTable,'debugEntry':debugEntry,_AA:debugIndex,'debugOperation':debugOperation,'debugBase':debugBase,'debugLength':debugLength,'debugData':debugData,'lpbk':lpbk,'lpbkTable':lpbkTable,'lpbkEntry':lpbkEntry,_AB:lpbkIndex,'lpbkOperation':lpbkOperation,'lpbkDestAddr':lpbkDestAddr,'lpbkPktNum':lpbkPktNum,'lpbkInterval':lpbkInterval,'lpbkPktLength':lpbkPktLength,'lpbkIncrements':lpbkIncrements,'lpbkGoods':lpbkGoods,'lpbkErrorNoReceives':lpbkErrorNoReceives,'lpbkErrorBadReceives':lpbkErrorBadReceives,'lpbkErrorSize':lpbkErrorSize,'lpbkErrorSent':lpbkErrorSent,'lpbkErrorReceived':lpbkErrorReceived,'lpbkErrorOffset':lpbkErrorOffset,'swan':swan,'swanTable':swanTable,'swanEntry':swanEntry,_AC:swanIndex,'swanDesiredSpeed':swanDesiredSpeed,'swanActualSpeed':swanActualSpeed,'swanIpNeighborAddress':swanIpNeighborAddress,'swanPPPActive':swanPPPActive,'swanAlignmentErrors':swanAlignmentErrors,'swanOverrunErrors':swanOverrunErrors,'swanPortType':swanPortType,'swanLinkCost':swanLinkCost,'swanMeshState':swanMeshState,'swanLinkSubnet':swanLinkSubnet,'swanLinkBridge':swanLinkBridge,'swanLinkPort':swanLinkPort,'swanNegotiate':swanNegotiate,'swanSwitches':swanSwitches,'swanDCEDrops':swanDCEDrops,'swanOutPacketType':swanOutPacketType,'swanLinkErrorPercentage':swanLinkErrorPercentage,'swanLinkErrorDuration':swanLinkErrorDuration,'swanLinkErrorFailPeriods':swanLinkErrorFailPeriods,'swanLinkErrorMaxPeriods':swanLinkErrorMaxPeriods,'swanLinkRestartTime':swanLinkRestartTime,'swanPreserveFCS':swanPreserveFCS,'srepeater':srepeater,'srepeaterTable':srepeaterTable,'srepeaterEntry':srepeaterEntry,_AD:srepeaterGroupID,'srepeaterLinkStatusMask':srepeaterLinkStatusMask,'srepeaterExtendedStats':srepeaterExtendedStats,'srepeaterPortTable':srepeaterPortTable,'srepeaterPortEntry':srepeaterPortEntry,_AE:srepeaterPortGroupID,_AF:srepeaterPortPortID,'srepeaterPortLinkPulse':srepeaterPortLinkPulse,'sproto':sproto,'sprotoTable':sprotoTable,'sprotoEntry':sprotoEntry,_AG:sprotoIfIndex,'sprotoBridge':sprotoBridge,'sprotoSuppressBpdus':sprotoSuppressBpdus,'sprotoIpRoute':sprotoIpRoute,'sprotoIpxRoute':sprotoIpxRoute,'sprotoAppleRoute':sprotoAppleRoute,'sprotoArpTranslate':sprotoArpTranslate,'sprotoArpSourceRoute':sprotoArpSourceRoute,'sprotoIpxTranslate':sprotoIpxTranslate,'sprotoAppleTranslate':sprotoAppleTranslate,'sprotoIbmLlcTranslate':sprotoIbmLlcTranslate,'sprotoRip':sprotoRip,'sprotoEgp':sprotoEgp,'sprotoOspf':sprotoOspf,'sprotoArpProxy':sprotoArpProxy,'sprotoIbm8209Lsaps':sprotoIbm8209Lsaps,'sprotoBootpRelay':sprotoBootpRelay,'sprotoNetbiosTranslate':sprotoNetbiosTranslate,'sprotoIpMulticast':sprotoIpMulticast,'sprotoTrunking':sprotoTrunking,'sprotoIpxSrTranslate':sprotoIpxSrTranslate,'sprotoAllTranslate':sprotoAllTranslate,'sprotoSteHopCountAppliedRule':sprotoSteHopCountAppliedRule,'sprotoIpxDot3Framing':sprotoIpxDot3Framing,'sipx':sipx,'sipxIfTable':sipxIfTable,'sipxIfEntry':sipxIfEntry,_AJ:sipxIfIndex,'sipxIfNetwork':sipxIfNetwork,'sipxIfFraming':sipxIfFraming,'sipxIfInRipPkts':sipxIfInRipPkts,'sipxIfOutRipPkts':sipxIfOutRipPkts,'sipxIfInSapPkts':sipxIfInSapPkts,'sipxIfOutSapPkts':sipxIfOutSapPkts,'sipxRouteTable':sipxRouteTable,'sipxRouteEntry':sipxRouteEntry,_AK:sipxRouteDest,'sipxRouteIfIndex':sipxRouteIfIndex,'sipxRouteTickCount':sipxRouteTickCount,'sipxRouteHopCount':sipxRouteHopCount,'sipxRouteNextHop':sipxRouteNextHop,'sipxRouteAge':sipxRouteAge,'sipxSapTable':sipxSapTable,'sipxSapEntry':sipxSapEntry,_AL:sipxSapIndex,'sipxSapType':sipxSapType,'sipxSapName':sipxSapName,'sipxSapNetwork':sipxSapNetwork,'sipxSapNodeId':sipxSapNodeId,'sipxSapSocket':sipxSapSocket,'sipxSapHopCount':sipxSapHopCount,'sipxDiscardedRoutes':sipxDiscardedRoutes,'sipxDiscardedServices':sipxDiscardedServices,'sipxsfGrp':sipxsfGrp,'sipxsfNextIndex':sipxsfNextIndex,'sipxsfTable':sipxsfTable,'sipxsfEntry':sipxsfEntry,_AM:sipxsfIndex,'sipxsfSAPName':sipxsfSAPName,'sipxsfSAPType':sipxsfSAPType,'sipxsfAccessMode':sipxsfAccessMode,'sipxsfFilterType':sipxsfFilterType,'sipxsfPortMap':sipxsfPortMap,'sipxsfNetworks':sipxsfNetworks,'sipxsfFiltered':sipxsfFiltered,'sipxsrGrp':sipxsrGrp,'sipxsrAgingTime':sipxsrAgingTime,'sipxsrExplorerTable':sipxsrExplorerTable,'sipxsrExplorerEntry':sipxsrExplorerEntry,_AN:sipxsrPort,'sipxsrStatus':sipxsrStatus,'sipxsrExplorerType':sipxsrExplorerType,'srtrdisc':srtrdisc,'srtrdiscTable':srtrdiscTable,'srtrdiscEntry':srtrdiscEntry,_AO:srtrdiscIfIndex,'srtrdiscState':srtrdiscState,'srtrdiscAdvertisementAddress':srtrdiscAdvertisementAddress,'srtrdiscAdvertisementInterval':srtrdiscAdvertisementInterval,'srtrdiscLifetime':srtrdiscLifetime,'srtrdiscPreference':srtrdiscPreference,'sipm':sipm,'sipmroute':sipmroute,'sipmRouteTable':sipmRouteTable,'sipmRouteEntry':sipmRouteEntry,_AP:sipmRouteOrigin,_AQ:sipmRouteOriginMask,'sipmRouteGateway':sipmRouteGateway,'sipmRouteMetric':sipmRouteMetric,'sipmRouteAge':sipmRouteAge,'sipmRouteParents':sipmRouteParents,'sipmgroup':sipmgroup,'sipmneighbor':sipmneighbor,'sipmNeighborTable':sipmNeighborTable,'sipmNeighborEntry':sipmNeighborEntry,_AR:sipmNeighborIfIndex,_AS:sipmNeighbors,'sipmNeighborLastHeard':sipmNeighborLastHeard,'sipmstat':sipmstat,'sipmOutOfMemory':sipmOutOfMemory,'sipmStatTable':sipmStatTable,'sipmStatEntry':sipmStatEntry,_AT:sipmStatIfIndex,'sipmInBadPackets':sipmInBadPackets,'sipmCacheMiss':sipmCacheMiss,'sipckt':sipckt,'sipcktTable':sipcktTable,'sipcktEntry':sipcktEntry,_AU:sipcktIndex,_AV:sipcktIpAddress,'sipcktState':sipcktState,'sipcktNetMask':sipcktNetMask,'sipcktSourceRoute':sipcktSourceRoute,'sipNetToMediaTable':sipNetToMediaTable,'sipNetToMediaEntry':sipNetToMediaEntry,_AW:sipNetToMediaIfIndex,_AX:sipNetToMediaNetAddress,'sipNetToMediaSourceRoute':sipNetToMediaSourceRoute,'sipNetToMediaAge':sipNetToMediaAge,'ssecure':ssecure,'profileTable':profileTable,'profileEntry':profileEntry,_AY:profileIndex,_AZ:profileSourceStart,_Aa:profileSourceEnd,_Ab:profileDestStart,_Ac:profileDestEnd,'profileType':profileType,'ruleTable':ruleTable,'ruleEntry':ruleEntry,_Ad:ruleIndex,_Ae:ruleSourceIp,_Af:ruleDestIp,_Ag:ruleSourceIpMask,_Ah:ruleDestIpMask,'ruleType':ruleType,'ruleUdpProfile':ruleUdpProfile,'ruleTcpProfile':ruleTcpProfile,'ruleTcpEstProfile':ruleTcpEstProfile,'ruleFilterUdpFragment':ruleFilterUdpFragment,'ruleFilterTcpFragment':ruleFilterTcpFragment,'ruleFilterIpOption':ruleFilterIpOption,'ruleAllowIcmp':ruleAllowIcmp,'ruleAllowIpWithinIp':ruleAllowIpWithinIp,'ruleAllowEgp':ruleAllowEgp,'ruleAllowIgp':ruleAllowIgp,'ruleAllowIgrp':ruleAllowIgrp,'ruleAllowOspf':ruleAllowOspf,'ruleAllowAnyOther':ruleAllowAnyOther,'spvc':spvc,'spvcTable':spvcTable,'spvcEntry':spvcEntry,_Ai:spvcIfIndex,'spvcPathRX':spvcPathRX,'spvcCircuitRX':spvcCircuitRX,'spvcPathTX':spvcPathTX,'spvcCircuitTX':spvcCircuitTX,'spvcState':spvcState,'spvcPhysPort':spvcPhysPort,'spvcMinPort':spvcMinPort,'spvcMaxPort':spvcMaxPort,'strunk':strunk,'strunkTable':strunkTable,'strunkEntry':strunkEntry,_Aj:strunkIfIndex,'strunkState':strunkState,'strunkRemoteBridgeAddr':strunkRemoteBridgeAddr,'strunkRemoteIp':strunkRemoteIp,'strunkLastError':strunkLastError,'strunkLinkOrdinal':strunkLinkOrdinal,'strunkLinkCount':strunkLinkCount,'strunkLastChange':strunkLastChange,'ipMRouteMIB':ipMRouteMIB,'ipMRouteMIBObjects':ipMRouteMIBObjects,'ipMRoute':ipMRoute,'ipMRouteEnable':ipMRouteEnable,'ipMRouteTable':ipMRouteTable,'ipMRouteEntry':ipMRouteEntry,_Ak:ipMRouteGroup,_Al:ipMRouteSource,_Am:ipMRouteSourceMask,'ipMRouteRpfNeighbor':ipMRouteRpfNeighbor,'ipMRouteInIfIndex':ipMRouteInIfIndex,'ipMRouteOutList':ipMRouteOutList,'ipMRouteUpTime':ipMRouteUpTime,'ipMRouteExpiryTime':ipMRouteExpiryTime,'ipMRoutePkts':ipMRoutePkts,'ipMRouteRpfFails':ipMRouteRpfFails,'ipMRouteOctets':ipMRouteOctets,'ipMRouteNextHopState':ipMRouteNextHopState,'ipMRouteInterfaceTable':ipMRouteInterfaceTable,'ipMRouteInterfaceEntry':ipMRouteInterfaceEntry,_An:ipMRouteInterfaceIfIndex,'ipMRouteInterfaceTtl':ipMRouteInterfaceTtl,'igmpMIB':igmpMIB,'igmpMIBObjects':igmpMIBObjects,'igmp':igmp,'igmpInterfaceTable':igmpInterfaceTable,'igmpInterfaceEntry':igmpInterfaceEntry,_Ao:igmpInterfaceIfIndex,'igmpInterfaceQueryInterval':igmpInterfaceQueryInterval,'igmpInterfaceStatus':igmpInterfaceStatus,'igmpCacheTable':igmpCacheTable,'igmpCacheEntry':igmpCacheEntry,_Ap:igmpCacheAddress,_Aq:igmpCacheIfIndex,'igmpCacheSelf':igmpCacheSelf,'igmpCacheLastReporter':igmpCacheLastReporter,'igmpCacheUpTime':igmpCacheUpTime,'igmpCacheExpiryTime':igmpCacheExpiryTime,'igmpCacheStatus':igmpCacheStatus,'slog':slog,'slogFilter':slogFilter,'slogTrap':slogTrap,'slogOverwrite':slogOverwrite,'slogEntryNumber':slogEntryNumber,'slogEntryTable':slogEntryTable,'slogEntry':slogEntry,_Ar:slogIndex,'slogEntryTimeStamp':slogEntryTimeStamp,'slogEntryMessageText':slogEntryMessageText,'slogEntryName':slogEntryName,'strap':strap,'strapControlTable':strapControlTable,'strapControl':strapControl,_As:strapIndex,'strapEnabled':strapEnabled,'strapSeverity':strapSeverity,'strapText':strapText,'strapSeverityControlTable':strapSeverityControlTable,'strapSeverityControl':strapSeverityControl,_At:strapSeveritySeverity,'strapSeverityEnable':strapSeverityEnable,'strapIncludeText':strapIncludeText,'strapTime':strapTime,'strapRetry':strapRetry,'strapEntryNumber':strapEntryNumber,'strapTable':strapTable,'strapEntry':strapEntry,_Au:strapEntryIndex,'strapEntryTimeStamp':strapEntryTimeStamp,'strapEntryText':strapEntryText,'strapNumber':strapNumber,'strapEntrySeverity':strapEntrySeverity,'smirror':smirror,'smirrorStatus':smirrorStatus,'smirrorDiagPort':smirrorDiagPort,'smirrorIPaddr':smirrorIPaddr,'smirrorTargetPortLists':smirrorTargetPortLists,'smirrorOversizePkt':smirrorOversizePkt,'smirrorEntryMirroredPkts':smirrorEntryMirroredPkts,'smirrorExitMirroredPkts':smirrorExitMirroredPkts,'smirrorNotreadyDroppedPkts':smirrorNotreadyDroppedPkts,'smirrorOversizeDroppedPkts':smirrorOversizeDroppedPkts,'smirrorEntryFilteredPkts':smirrorEntryFilteredPkts,'smirrorExitFilteredPkts':smirrorExitFilteredPkts,'smirrorCongestionDroppedPkts':smirrorCongestionDroppedPkts,'smirrorNowrapperDroppedPkts':smirrorNowrapperDroppedPkts,'smirrorRemoteStatus':smirrorRemoteStatus,'smirrorRemoteExitPort':smirrorRemoteExitPort,'sworkgroup':sworkgroup,'sWorkGroupNextNumber':sWorkGroupNextNumber,'sWorkGroupCurrentCount':sWorkGroupCurrentCount,'sWorkGroupMaxCount':sWorkGroupMaxCount,'sWorkGroupTable':sWorkGroupTable,'sWorkGroupEntry':sWorkGroupEntry,_Av:sWorkGroupNumber,'sWorkGroupName':sWorkGroupName,'sWorkGroupPorts':sWorkGroupPorts,'sWorkGroupType':sWorkGroupType,'sWorkGroupIpAddress':sWorkGroupIpAddress,'sWorkGroupIpMask':sWorkGroupIpMask,'sWorkGroupIpxNetwork':sWorkGroupIpxNetwork,'sping':sping,'spingDataTimeout':spingDataTimeout,'spingTable':spingTable,'spingEntry':spingEntry,_Aw:spingNMSAddr,_Ax:spingDestAddr,'spingState':spingState,'spingCount':spingCount,'spingDataSize':spingDataSize,'spingWait':spingWait,'spingTimeout':spingTimeout,'spingOperation':spingOperation,'spingMin':spingMin,'spingMax':spingMax,'spingAvg':spingAvg,'spingNumTransmitted':spingNumTransmitted,'spingNumReceived':spingNumReceived,'strace':strace,'straceDataTimeout':straceDataTimeout,'straceTable':straceTable,'straceEntry':straceEntry,_A_:straceNMSAddr,_B0:straceDestAddr,'straceMaxTTL':straceMaxTTL,'straceDataSize':straceDataSize,'straceNumProbes':straceNumProbes,'straceWait':straceWait,'straceOperation':straceOperation,_B1:straceHop,'straceHopAddress':straceHopAddress,_B2:straceProbe,'straceState':straceState,'straceTime':straceTime,'srtb':srtb,'srtbProto':srtbProto,'srtbExplorer':srtbExplorer,'srtbAgingTime':srtbAgingTime,'nbcache':nbcache,'nbCacheifTable':nbCacheifTable,'nbCacheifEntry':nbCacheifEntry,_B3:nbCacheIfIndex,'nbCacheIfOperStatus':nbCacheIfOperStatus,'atext':atext,'atextsystem':atextsystem,'atextsysOperState':atextsysOperState,'atextport':atextport,'atextportTable':atextportTable,'atextportEntry':atextportEntry,_B4:atextportIndex,'atextportNetStart':atextportNetStart,'atextportNetEnd':atextportNetEnd,'atextportNetAddress':atextportNetAddress,'atextportZone':atextportZone,'atextportzipTable':atextportzipTable,'atextportzipEntry':atextportzipEntry,_B5:atextportZonePort,_B6:atextportZoneIndex,'atextportZoneName':atextportZoneName})