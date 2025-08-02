_A6='sarChanNum'
_A5='sarSlotNum'
_A4='sarShelfNum'
_A3='ethernet-3Mbit'
_A2='interfaceLineNum'
_A1='notPresent'
_A0='pxm-ui-s3'
_z='mmf-fe'
_y='rj45-fe'
_x='smflr-4-155'
_w='smfir-4-155'
_v='mmf-4-155'
_u='smflr15-1-622'
_t='smfir15-1-622'
_s='smflr-1-622'
_r='smfir-1-622'
_q='pxm-ui'
_p='lm-BNC-2E3'
_o='lm-BNC-2T3'
_n='lm-BSCSM-4'
_m='lm-BSCSM-2'
_l='lm-12In1-8s'
_k='lm-HS1-4V35'
_j='lm-HS1-3HSSI'
_i='lm-HS1-4X21'
_h='lm-3T3-B'
_g='lm-SMB-8E1-R'
_f='lm-RJ48-8E1-R'
_e='lm-RJ48-8T1-R'
_d='lm-155-UTP'
_c='lm-155-SMF'
_b='lm-T3E3-B'
_a='lm-T3E3-D'
_Z='lm-SMB-T3E1'
_Y='lm-RJ48-E3T1'
_X='lm-SMB-E3E1'
_W='lm-RJ48-T3E1'
_V='lm-RJ48-E3E1'
_U='lm-RJ48-T3T1'
_T='lm-SMB-8E1'
_S='lm-RJ48-8E1'
_R='lm-RJ48-8T1'
_Q='lm-BNC-4E1-R'
_P='lm-DB15-4E1-R'
_O='lm-DB15-4T1-R'
_N='lm-BNC-4E1'
_M='lm-DB15-4E1'
_L='lm-DB15-4T1'
_K='lm-ASC'
_J='unknown'
_I='failed'
_H='clear'
_G='read-write'
_F='BASIS-GENERIC-MIB'
_E='other'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cardGeneric,=mibBuilder.importSymbols('BASIS-MIB','cardGeneric')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
_CardInformation_ObjectIdentity=ObjectIdentity
cardInformation=_CardInformation_ObjectIdentity((1,3,6,1,4,1,351,110,2,1))
class _ModuleSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_ModuleSlotNumber_Type.__name__=_C
_ModuleSlotNumber_Object=MibScalar
moduleSlotNumber=_ModuleSlotNumber_Object((1,3,6,1,4,1,351,110,2,1,1),_ModuleSlotNumber_Type())
moduleSlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleSlotNumber.setStatus(_A)
class _FunctionModuleType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,10,11,12,20,21,22,23,24,25,30,31,32,33,34,35,36,37,40,41,50,51,52,53,60,61,70,71,72,73,80,90,91,100,101,110,111,120,121,130,131,132,133,134,135,136,137,140,141,150,151,563,564,787,1000,1001,1002,1003,2000,2001)));namedValues=NamedValues(*((_E,1),('asc',2),('bnm-T3',10),('bnm-E3',11),('bnm-155',12),('srm-4T1E1',20),('srm-3T3',21),('srme-1OC3',22),('srme-1STS3',23),('srme-NOBC',24),('srm-3T3-NOBC',25),('frsm-4T1',30),('frsm-4E1',31),('frsm-4T1-C',32),('frsm-4E1-C',33),('frsm-hs1',34),('frsm-8T1',35),('frsm-8E1',36),('frsm-hs1b',37),('ausm-4T1',40),('ausm-4E1',41),('ausm-8T1',50),('ausm-8E1',51),('ausmB-8T1',52),('ausmB-8E1',53),('cesm-4T1',60),('cesm-4E1',61),('imatm-T3T1',70),('imatm-E3E1',71),('imatmB-8T1',72),('imatmB-8E1',73),('frasm-8T1',80),('cesm-8T1',90),('cesm-8E1',91),('bscsm-2',100),('bscsm-4',101),('atmt-8T1',110),('atmt-8E1',111),('frt-8T1',120),('frt-8E1',121),('frsm-2ct3',130),('frsm-2t3',131),('frsm-2e3',132),('frsm-hs2',133),('frsm-2t3b',134),('frsm-2e3b',135),('frsm-hs2b-hssi',136),('frsm-hs2b-12In1',137),('cesm-T3',140),('cesm-E3',141),('vism-8T1',150),('vism-8E1',151),('vism-pr-8T1',563),('vism-pr-8E1',564),('cesmB-8T1',787),('pxm1',1000),('pxm1-2t3e3',1001),('pxm1-4oc3',1002),('pxm1-oc12',1003),('rpm',2000),('rpm-pr',2001)))
_FunctionModuleType_Type.__name__=_C
_FunctionModuleType_Object=MibScalar
functionModuleType=_FunctionModuleType_Object((1,3,6,1,4,1,351,110,2,1,2),_FunctionModuleType_Type())
functionModuleType.setMaxAccess(_B)
if mibBuilder.loadTexts:functionModuleType.setStatus(_A)
class _FunctionModuleDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_FunctionModuleDescription_Type.__name__=_D
_FunctionModuleDescription_Object=MibScalar
functionModuleDescription=_FunctionModuleDescription_Object((1,3,6,1,4,1,351,110,2,1,3),_FunctionModuleDescription_Type())
functionModuleDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:functionModuleDescription.setStatus(_A)
class _FunctionModuleSerialNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,11))
_FunctionModuleSerialNum_Type.__name__=_D
_FunctionModuleSerialNum_Object=MibScalar
functionModuleSerialNum=_FunctionModuleSerialNum_Object((1,3,6,1,4,1,351,110,2,1,4),_FunctionModuleSerialNum_Type())
functionModuleSerialNum.setMaxAccess(_B)
if mibBuilder.loadTexts:functionModuleSerialNum.setStatus(_A)
class _FunctionModuleHWRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_FunctionModuleHWRev_Type.__name__=_D
_FunctionModuleHWRev_Object=MibScalar
functionModuleHWRev=_FunctionModuleHWRev_Object((1,3,6,1,4,1,351,110,2,1,5),_FunctionModuleHWRev_Type())
functionModuleHWRev.setMaxAccess(_B)
if mibBuilder.loadTexts:functionModuleHWRev.setStatus(_A)
class _FunctionModuleFWRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_FunctionModuleFWRev_Type.__name__=_D
_FunctionModuleFWRev_Object=MibScalar
functionModuleFWRev=_FunctionModuleFWRev_Object((1,3,6,1,4,1,351,110,2,1,6),_FunctionModuleFWRev_Type())
functionModuleFWRev.setMaxAccess(_B)
if mibBuilder.loadTexts:functionModuleFWRev.setStatus(_A)
class _FunctionModuleState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,17)));namedValues=NamedValues(*(('nocard',1),('standby',2),('active',3),(_I,4),('selfTest',5),('heldInReset',6),('boot',7),('mismatch',8),(_J,9),('coreCardMisMatch',10),('blocked',11),('reserved',12),('hold',13),('notResponding',14),('cardinit',17)))
_FunctionModuleState_Type.__name__=_C
_FunctionModuleState_Object=MibScalar
functionModuleState=_FunctionModuleState_Object((1,3,6,1,4,1,351,110,2,1,7),_FunctionModuleState_Type())
functionModuleState.setMaxAccess(_B)
if mibBuilder.loadTexts:functionModuleState.setStatus(_A)
class _FunctionModuleResetReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)));namedValues=NamedValues(*(('powerUp',1),('parityError',2),('watchDog',3),('resourceOverflow',4),('clrAllCnf',5),('missingTask',6),('pxmLowVoltage',7),('resetByEventLogTask',8),('resetFromShell',9),(_J,10),('resetFromPXM',11),('resetSys',12),('switchCC',13),('sCacheError',14),('swError',15),('upgrade',16),('restoreAllCnf',17),('driverError',18)))
_FunctionModuleResetReason_Type.__name__=_C
_FunctionModuleResetReason_Object=MibScalar
functionModuleResetReason=_FunctionModuleResetReason_Object((1,3,6,1,4,1,351,110,2,1,8),_FunctionModuleResetReason_Type())
functionModuleResetReason.setMaxAccess(_B)
if mibBuilder.loadTexts:functionModuleResetReason.setStatus(_A)
class _LineModuleType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,33,34,35,48,49,50,51,60,61,62,63,70,71,80,81,500,501,502,503,504,505,506,507,511,512,513,514,515,1006,1050,1051,1052)));namedValues=NamedValues(*((_E,1),(_K,2),(_L,16),(_M,17),(_N,18),(_O,19),(_P,20),(_Q,21),(_R,22),(_S,23),(_T,24),(_U,25),(_V,26),(_W,27),(_X,28),(_Y,29),(_Z,30),(_a,32),(_b,33),(_c,34),(_d,35),(_e,48),(_f,49),(_g,50),(_h,51),(_i,60),(_j,61),(_k,62),(_l,63),(_m,70),(_n,71),(_o,80),(_p,81),(_q,500),(_r,501),(_s,502),(_t,503),(_u,504),(_v,505),(_w,506),(_x,507),(_y,511),(_z,512),('mmf-fddi',513),('smf-fddi',514),('rj45-4e',515),(_A0,1006),('lm-srme-1OC3-smlr',1050),('lm-srme-1OC3-smir',1051),('lm-srme-1OC3-smb',1052)))
_LineModuleType_Type.__name__=_C
_LineModuleType_Object=MibScalar
lineModuleType=_LineModuleType_Object((1,3,6,1,4,1,351,110,2,1,9),_LineModuleType_Type())
lineModuleType.setMaxAccess(_B)
if mibBuilder.loadTexts:lineModuleType.setStatus(_A)
class _LineModuleDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_LineModuleDescription_Type.__name__=_D
_LineModuleDescription_Object=MibScalar
lineModuleDescription=_LineModuleDescription_Object((1,3,6,1,4,1,351,110,2,1,10),_LineModuleDescription_Type())
lineModuleDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:lineModuleDescription.setStatus(_A)
class _LineModuleSerialNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,11))
_LineModuleSerialNum_Type.__name__=_D
_LineModuleSerialNum_Object=MibScalar
lineModuleSerialNum=_LineModuleSerialNum_Object((1,3,6,1,4,1,351,110,2,1,11),_LineModuleSerialNum_Type())
lineModuleSerialNum.setMaxAccess(_B)
if mibBuilder.loadTexts:lineModuleSerialNum.setStatus(_A)
class _LineModuleHWRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_LineModuleHWRev_Type.__name__=_D
_LineModuleHWRev_Object=MibScalar
lineModuleHWRev=_LineModuleHWRev_Object((1,3,6,1,4,1,351,110,2,1,12),_LineModuleHWRev_Type())
lineModuleHWRev.setMaxAccess(_B)
if mibBuilder.loadTexts:lineModuleHWRev.setStatus(_A)
class _LineModuleFWRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_LineModuleFWRev_Type.__name__=_D
_LineModuleFWRev_Object=MibScalar
lineModuleFWRev=_LineModuleFWRev_Object((1,3,6,1,4,1,351,110,2,1,13),_LineModuleFWRev_Type())
lineModuleFWRev.setMaxAccess(_B)
if mibBuilder.loadTexts:lineModuleFWRev.setStatus(_A)
class _LineModuleState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_A1,1),('present',2),('invalid',3)))
_LineModuleState_Type.__name__=_C
_LineModuleState_Object=MibScalar
lineModuleState=_LineModuleState_Object((1,3,6,1,4,1,351,110,2,1,14),_LineModuleState_Type())
lineModuleState.setMaxAccess(_B)
if mibBuilder.loadTexts:lineModuleState.setStatus(_A)
class _ModuleTrapAlarmSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('minor',1),('major',2),('dontCare',3),('critical',4),('error',5),('warning',6),('notice',7),('info',8)))
_ModuleTrapAlarmSeverity_Type.__name__=_C
_ModuleTrapAlarmSeverity_Object=MibScalar
moduleTrapAlarmSeverity=_ModuleTrapAlarmSeverity_Object((1,3,6,1,4,1,351,110,2,1,15),_ModuleTrapAlarmSeverity_Type())
moduleTrapAlarmSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleTrapAlarmSeverity.setStatus(_A)
class _MibVersionNumber_Type(Integer32):defaultValue=2
_MibVersionNumber_Type.__name__=_C
_MibVersionNumber_Object=MibScalar
mibVersionNumber=_MibVersionNumber_Object((1,3,6,1,4,1,351,110,2,1,16),_MibVersionNumber_Type())
mibVersionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:mibVersionNumber.setStatus(_A)
class _ConfigChangeTypeBitMap_Type(Integer32):defaultValue=0
_ConfigChangeTypeBitMap_Type.__name__=_C
_ConfigChangeTypeBitMap_Object=MibScalar
configChangeTypeBitMap=_ConfigChangeTypeBitMap_Object((1,3,6,1,4,1,351,110,2,1,17),_ConfigChangeTypeBitMap_Type())
configChangeTypeBitMap.setMaxAccess(_B)
if mibBuilder.loadTexts:configChangeTypeBitMap.setStatus(_A)
class _ConfigChangeObjectIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_ConfigChangeObjectIndex_Type.__name__=_C
_ConfigChangeObjectIndex_Object=MibScalar
configChangeObjectIndex=_ConfigChangeObjectIndex_Object((1,3,6,1,4,1,351,110,2,1,18),_ConfigChangeObjectIndex_Type())
configChangeObjectIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:configChangeObjectIndex.setStatus(_A)
class _ConfigChangeStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_ConfigChangeStatus_Type.__name__=_C
_ConfigChangeStatus_Object=MibScalar
configChangeStatus=_ConfigChangeStatus_Object((1,3,6,1,4,1,351,110,2,1,19),_ConfigChangeStatus_Type())
configChangeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:configChangeStatus.setStatus(_A)
class _CardIntegratedAlarmBitMap_Type(Integer32):defaultValue=0
_CardIntegratedAlarmBitMap_Type.__name__=_C
_CardIntegratedAlarmBitMap_Object=MibScalar
cardIntegratedAlarmBitMap=_CardIntegratedAlarmBitMap_Object((1,3,6,1,4,1,351,110,2,1,20),_CardIntegratedAlarmBitMap_Type())
cardIntegratedAlarmBitMap.setMaxAccess(_B)
if mibBuilder.loadTexts:cardIntegratedAlarmBitMap.setStatus(_A)
class _CleiCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_CleiCode_Type.__name__=_D
_CleiCode_Object=MibScalar
cleiCode=_CleiCode_Object((1,3,6,1,4,1,351,110,2,1,21),_CleiCode_Type())
cleiCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cleiCode.setStatus(_A)
_MacAddress_Type=DisplayString
_MacAddress_Object=MibScalar
macAddress=_MacAddress_Object((1,3,6,1,4,1,351,110,2,1,22),_MacAddress_Type())
macAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:macAddress.setStatus(_A)
_MacAddrBlkSize_Type=Integer32
_MacAddrBlkSize_Object=MibScalar
macAddrBlkSize=_MacAddrBlkSize_Object((1,3,6,1,4,1,351,110,2,1,23),_MacAddrBlkSize_Type())
macAddrBlkSize.setMaxAccess(_B)
if mibBuilder.loadTexts:macAddrBlkSize.setStatus(_A)
class _FinalTestTechnician_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_FinalTestTechnician_Type.__name__=_D
_FinalTestTechnician_Object=MibScalar
finalTestTechnician=_FinalTestTechnician_Object((1,3,6,1,4,1,351,110,2,1,24),_FinalTestTechnician_Type())
finalTestTechnician.setMaxAccess(_B)
if mibBuilder.loadTexts:finalTestTechnician.setStatus(_A)
_HwFailures_Type=Integer32
_HwFailures_Object=MibScalar
hwFailures=_HwFailures_Object((1,3,6,1,4,1,351,110,2,1,25),_HwFailures_Type())
hwFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:hwFailures.setStatus(_A)
_HwHistory_Type=Integer32
_HwHistory_Object=MibScalar
hwHistory=_HwHistory_Object((1,3,6,1,4,1,351,110,2,1,26),_HwHistory_Type())
hwHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:hwHistory.setStatus(_A)
class _SecLineModuleType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,33,34,35,48,49,50,51,60,61,62,63,70,71,80,81,500,501,502,503,504,505,506,507,511,512,513,514,515,1006)));namedValues=NamedValues(*((_E,1),(_K,2),(_L,16),(_M,17),(_N,18),(_O,19),(_P,20),(_Q,21),(_R,22),(_S,23),(_T,24),(_U,25),(_V,26),(_W,27),(_X,28),(_Y,29),(_Z,30),(_a,32),(_b,33),(_c,34),(_d,35),(_e,48),(_f,49),(_g,50),(_h,51),(_i,60),(_j,61),(_k,62),(_l,63),(_m,70),(_n,71),(_o,80),(_p,81),(_q,500),(_r,501),(_s,502),(_t,503),(_u,504),(_v,505),(_w,506),(_x,507),(_y,511),(_z,512),('mmf-fddi',513),('smf-fddi',514),('rj45-4e',515),(_A0,1006)))
_SecLineModuleType_Type.__name__=_C
_SecLineModuleType_Object=MibScalar
secLineModuleType=_SecLineModuleType_Object((1,3,6,1,4,1,351,110,2,1,27),_SecLineModuleType_Type())
secLineModuleType.setMaxAccess(_B)
if mibBuilder.loadTexts:secLineModuleType.setStatus(_A)
class _SecLineModuleDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SecLineModuleDescription_Type.__name__=_D
_SecLineModuleDescription_Object=MibScalar
secLineModuleDescription=_SecLineModuleDescription_Object((1,3,6,1,4,1,351,110,2,1,28),_SecLineModuleDescription_Type())
secLineModuleDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:secLineModuleDescription.setStatus(_A)
class _SecLineModuleSerialNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,11))
_SecLineModuleSerialNum_Type.__name__=_D
_SecLineModuleSerialNum_Object=MibScalar
secLineModuleSerialNum=_SecLineModuleSerialNum_Object((1,3,6,1,4,1,351,110,2,1,29),_SecLineModuleSerialNum_Type())
secLineModuleSerialNum.setMaxAccess(_B)
if mibBuilder.loadTexts:secLineModuleSerialNum.setStatus(_A)
class _SecLineModuleHWRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_SecLineModuleHWRev_Type.__name__=_D
_SecLineModuleHWRev_Object=MibScalar
secLineModuleHWRev=_SecLineModuleHWRev_Object((1,3,6,1,4,1,351,110,2,1,30),_SecLineModuleHWRev_Type())
secLineModuleHWRev.setMaxAccess(_B)
if mibBuilder.loadTexts:secLineModuleHWRev.setStatus(_A)
class _SecLineModuleFWRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_SecLineModuleFWRev_Type.__name__=_D
_SecLineModuleFWRev_Object=MibScalar
secLineModuleFWRev=_SecLineModuleFWRev_Object((1,3,6,1,4,1,351,110,2,1,31),_SecLineModuleFWRev_Type())
secLineModuleFWRev.setMaxAccess(_B)
if mibBuilder.loadTexts:secLineModuleFWRev.setStatus(_A)
class _SecLineModuleState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_A1,1),('present',2),('invalid',3)))
_SecLineModuleState_Type.__name__=_C
_SecLineModuleState_Object=MibScalar
secLineModuleState=_SecLineModuleState_Object((1,3,6,1,4,1,351,110,2,1,32),_SecLineModuleState_Type())
secLineModuleState.setMaxAccess(_B)
if mibBuilder.loadTexts:secLineModuleState.setStatus(_A)
class _ConfigChangeParentObjectIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_ConfigChangeParentObjectIndex_Type.__name__=_C
_ConfigChangeParentObjectIndex_Object=MibScalar
configChangeParentObjectIndex=_ConfigChangeParentObjectIndex_Object((1,3,6,1,4,1,351,110,2,1,33),_ConfigChangeParentObjectIndex_Type())
configChangeParentObjectIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:configChangeParentObjectIndex.setStatus(_A)
class _ConfigChangeGrandParentObjectIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_ConfigChangeGrandParentObjectIndex_Type.__name__=_C
_ConfigChangeGrandParentObjectIndex_Object=MibScalar
configChangeGrandParentObjectIndex=_ConfigChangeGrandParentObjectIndex_Object((1,3,6,1,4,1,351,110,2,1,34),_ConfigChangeGrandParentObjectIndex_Type())
configChangeGrandParentObjectIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:configChangeGrandParentObjectIndex.setStatus(_A)
class _ConfigChangeSMSpecificObject_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_ConfigChangeSMSpecificObject_Type.__name__=_C
_ConfigChangeSMSpecificObject_Object=MibScalar
configChangeSMSpecificObject=_ConfigChangeSMSpecificObject_Object((1,3,6,1,4,1,351,110,2,1,35),_ConfigChangeSMSpecificObject_Type())
configChangeSMSpecificObject.setMaxAccess(_B)
if mibBuilder.loadTexts:configChangeSMSpecificObject.setStatus(_A)
class _TransId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_TransId_Type.__name__=_C
_TransId_Object=MibScalar
transId=_TransId_Object((1,3,6,1,4,1,351,110,2,1,36),_TransId_Type())
transId.setMaxAccess(_B)
if mibBuilder.loadTexts:transId.setStatus(_A)
_CardInterface_ObjectIdentity=ObjectIdentity
cardInterface=_CardInterface_ObjectIdentity((1,3,6,1,4,1,351,110,2,2))
_InterfaceLineTable_Object=MibTable
interfaceLineTable=_InterfaceLineTable_Object((1,3,6,1,4,1,351,110,2,2,1))
if mibBuilder.loadTexts:interfaceLineTable.setStatus(_A)
_InterfaceLineEntry_Object=MibTableRow
interfaceLineEntry=_InterfaceLineEntry_Object((1,3,6,1,4,1,351,110,2,2,1,1))
interfaceLineEntry.setIndexNames((0,_F,_A2))
if mibBuilder.loadTexts:interfaceLineEntry.setStatus(_A)
class _InterfaceLineNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_InterfaceLineNum_Type.__name__=_C
_InterfaceLineNum_Object=MibTableColumn
interfaceLineNum=_InterfaceLineNum_Object((1,3,6,1,4,1,351,110,2,2,1,1,1),_InterfaceLineNum_Type())
interfaceLineNum.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceLineNum.setStatus(_A)
class _InterfaceLineType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,18,19,26,30,33,45,46)));namedValues=NamedValues(*((_E,1),('ds1',18),('e1',19),(_A3,26),('ds3',30),('rs232',33),('v35',45),('hssi',46)))
_InterfaceLineType_Type.__name__=_C
_InterfaceLineType_Object=MibTableColumn
interfaceLineType=_InterfaceLineType_Object((1,3,6,1,4,1,351,110,2,2,1,1,2),_InterfaceLineType_Type())
interfaceLineType.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceLineType.setStatus(_A)
class _InterfaceNumOfPortsPerLine_Type(Integer32):defaultValue=672;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_InterfaceNumOfPortsPerLine_Type.__name__=_C
_InterfaceNumOfPortsPerLine_Object=MibTableColumn
interfaceNumOfPortsPerLine=_InterfaceNumOfPortsPerLine_Object((1,3,6,1,4,1,351,110,2,2,1,1,3),_InterfaceNumOfPortsPerLine_Type())
interfaceNumOfPortsPerLine.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceNumOfPortsPerLine.setStatus(_A)
class _InterfaceServiceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,26,28,32,37,42)));namedValues=NamedValues(*((_E,1),(_A3,26),('slip',28),('frameRelay',32),('atm',37),('voice',42)))
_InterfaceServiceType_Type.__name__=_C
_InterfaceServiceType_Object=MibTableColumn
interfaceServiceType=_InterfaceServiceType_Object((1,3,6,1,4,1,351,110,2,2,1,1,4),_InterfaceServiceType_Type())
interfaceServiceType.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceServiceType.setStatus(_A)
_InterfaceNumOfPVC_Type=Integer32
_InterfaceNumOfPVC_Object=MibTableColumn
interfaceNumOfPVC=_InterfaceNumOfPVC_Object((1,3,6,1,4,1,351,110,2,2,1,1,5),_InterfaceNumOfPVC_Type())
interfaceNumOfPVC.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceNumOfPVC.setStatus(_A)
_InterfaceNumOfEgressQueue_Type=Integer32
_InterfaceNumOfEgressQueue_Object=MibTableColumn
interfaceNumOfEgressQueue=_InterfaceNumOfEgressQueue_Object((1,3,6,1,4,1,351,110,2,2,1,1,6),_InterfaceNumOfEgressQueue_Type())
interfaceNumOfEgressQueue.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceNumOfEgressQueue.setStatus(_A)
_InterfaceNumOfValidEntries_Type=Integer32
_InterfaceNumOfValidEntries_Object=MibScalar
interfaceNumOfValidEntries=_InterfaceNumOfValidEntries_Object((1,3,6,1,4,1,351,110,2,2,2),_InterfaceNumOfValidEntries_Type())
interfaceNumOfValidEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceNumOfValidEntries.setStatus(_A)
_CardSelfTest_ObjectIdentity=ObjectIdentity
cardSelfTest=_CardSelfTest_ObjectIdentity((1,3,6,1,4,1,351,110,2,3))
class _SelfTestEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('enable',2)))
_SelfTestEnable_Type.__name__=_C
_SelfTestEnable_Object=MibScalar
selfTestEnable=_SelfTestEnable_Object((1,3,6,1,4,1,351,110,2,3,1),_SelfTestEnable_Type())
selfTestEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:selfTestEnable.setStatus(_A)
class _SelfTestPeriod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_SelfTestPeriod_Type.__name__=_C
_SelfTestPeriod_Object=MibScalar
selfTestPeriod=_SelfTestPeriod_Object((1,3,6,1,4,1,351,110,2,3,2),_SelfTestPeriod_Type())
selfTestPeriod.setMaxAccess(_G)
if mibBuilder.loadTexts:selfTestPeriod.setStatus(_A)
class _SelfTestState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('passed',1),(_I,2)))
_SelfTestState_Type.__name__=_C
_SelfTestState_Object=MibScalar
selfTestState=_SelfTestState_Object((1,3,6,1,4,1,351,110,2,3,3),_SelfTestState_Type())
selfTestState.setMaxAccess(_B)
if mibBuilder.loadTexts:selfTestState.setStatus(_A)
class _SelfTestResultDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_SelfTestResultDescription_Type.__name__=_D
_SelfTestResultDescription_Object=MibScalar
selfTestResultDescription=_SelfTestResultDescription_Object((1,3,6,1,4,1,351,110,2,3,4),_SelfTestResultDescription_Type())
selfTestResultDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:selfTestResultDescription.setStatus(_A)
class _SelfTestClrResultButton_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_H,2)))
_SelfTestClrResultButton_Type.__name__=_C
_SelfTestClrResultButton_Object=MibScalar
selfTestClrResultButton=_SelfTestClrResultButton_Object((1,3,6,1,4,1,351,110,2,3,5),_SelfTestClrResultButton_Type())
selfTestClrResultButton.setMaxAccess(_G)
if mibBuilder.loadTexts:selfTestClrResultButton.setStatus(_A)
_ControlMsgCounter_ObjectIdentity=ObjectIdentity
controlMsgCounter=_ControlMsgCounter_ObjectIdentity((1,3,6,1,4,1,351,110,2,4))
_RiscXmtCtrlMsg_Type=Counter32
_RiscXmtCtrlMsg_Object=MibScalar
riscXmtCtrlMsg=_RiscXmtCtrlMsg_Object((1,3,6,1,4,1,351,110,2,4,1),_RiscXmtCtrlMsg_Type())
riscXmtCtrlMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:riscXmtCtrlMsg.setStatus(_A)
_RiscRcvCtrlMsg_Type=Counter32
_RiscRcvCtrlMsg_Object=MibScalar
riscRcvCtrlMsg=_RiscRcvCtrlMsg_Object((1,3,6,1,4,1,351,110,2,4,2),_RiscRcvCtrlMsg_Type())
riscRcvCtrlMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:riscRcvCtrlMsg.setStatus(_A)
_SarXmtCtrlMsg_Type=Counter32
_SarXmtCtrlMsg_Object=MibScalar
sarXmtCtrlMsg=_SarXmtCtrlMsg_Object((1,3,6,1,4,1,351,110,2,4,3),_SarXmtCtrlMsg_Type())
sarXmtCtrlMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:sarXmtCtrlMsg.setStatus(_A)
_SarRcvCtrlMsg_Type=Counter32
_SarRcvCtrlMsg_Object=MibScalar
sarRcvCtrlMsg=_SarRcvCtrlMsg_Object((1,3,6,1,4,1,351,110,2,4,4),_SarRcvCtrlMsg_Type())
sarRcvCtrlMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:sarRcvCtrlMsg.setStatus(_A)
_SarCtrlMsgDiscLenErr_Type=Counter32
_SarCtrlMsgDiscLenErr_Object=MibScalar
sarCtrlMsgDiscLenErr=_SarCtrlMsgDiscLenErr_Object((1,3,6,1,4,1,351,110,2,4,5),_SarCtrlMsgDiscLenErr_Type())
sarCtrlMsgDiscLenErr.setMaxAccess(_B)
if mibBuilder.loadTexts:sarCtrlMsgDiscLenErr.setStatus(_A)
_SarCtrlMsgDiscCRCErr_Type=Counter32
_SarCtrlMsgDiscCRCErr_Object=MibScalar
sarCtrlMsgDiscCRCErr=_SarCtrlMsgDiscCRCErr_Object((1,3,6,1,4,1,351,110,2,4,6),_SarCtrlMsgDiscCRCErr_Type())
sarCtrlMsgDiscCRCErr.setMaxAccess(_B)
if mibBuilder.loadTexts:sarCtrlMsgDiscCRCErr.setStatus(_A)
_SarCtrlMsgDiscUnknownChan_Type=Counter32
_SarCtrlMsgDiscUnknownChan_Object=MibScalar
sarCtrlMsgDiscUnknownChan=_SarCtrlMsgDiscUnknownChan_Object((1,3,6,1,4,1,351,110,2,4,7),_SarCtrlMsgDiscUnknownChan_Type())
sarCtrlMsgDiscUnknownChan.setMaxAccess(_B)
if mibBuilder.loadTexts:sarCtrlMsgDiscUnknownChan.setStatus(_A)
_SarCtrlMsgLastUnkownChan_Type=Integer32
_SarCtrlMsgLastUnkownChan_Object=MibScalar
sarCtrlMsgLastUnkownChan=_SarCtrlMsgLastUnkownChan_Object((1,3,6,1,4,1,351,110,2,4,8),_SarCtrlMsgLastUnkownChan_Type())
sarCtrlMsgLastUnkownChan.setMaxAccess(_B)
if mibBuilder.loadTexts:sarCtrlMsgLastUnkownChan.setStatus(_A)
class _CtrlMsgClrButton_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_H,2)))
_CtrlMsgClrButton_Type.__name__=_C
_CtrlMsgClrButton_Object=MibScalar
ctrlMsgClrButton=_CtrlMsgClrButton_Object((1,3,6,1,4,1,351,110,2,4,9),_CtrlMsgClrButton_Type())
ctrlMsgClrButton.setMaxAccess(_G)
if mibBuilder.loadTexts:ctrlMsgClrButton.setStatus(_A)
_SarChannelCounter_ObjectIdentity=ObjectIdentity
sarChannelCounter=_SarChannelCounter_ObjectIdentity((1,3,6,1,4,1,351,110,2,5))
_SarChannelCounterTable_Object=MibTable
sarChannelCounterTable=_SarChannelCounterTable_Object((1,3,6,1,4,1,351,110,2,5,1))
if mibBuilder.loadTexts:sarChannelCounterTable.setStatus(_A)
_SarChannelCounterEntry_Object=MibTableRow
sarChannelCounterEntry=_SarChannelCounterEntry_Object((1,3,6,1,4,1,351,110,2,5,1,1))
sarChannelCounterEntry.setIndexNames((0,_F,_A4),(0,_F,_A5),(0,_F,_A6))
if mibBuilder.loadTexts:sarChannelCounterEntry.setStatus(_A)
class _SarShelfNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_SarShelfNum_Type.__name__=_C
_SarShelfNum_Object=MibTableColumn
sarShelfNum=_SarShelfNum_Object((1,3,6,1,4,1,351,110,2,5,1,1,1),_SarShelfNum_Type())
sarShelfNum.setMaxAccess(_B)
if mibBuilder.loadTexts:sarShelfNum.setStatus(_A)
class _SarSlotNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_SarSlotNum_Type.__name__=_C
_SarSlotNum_Object=MibTableColumn
sarSlotNum=_SarSlotNum_Object((1,3,6,1,4,1,351,110,2,5,1,1,2),_SarSlotNum_Type())
sarSlotNum.setMaxAccess(_B)
if mibBuilder.loadTexts:sarSlotNum.setStatus(_A)
class _SarChanNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4015))
_SarChanNum_Type.__name__=_C
_SarChanNum_Object=MibTableColumn
sarChanNum=_SarChanNum_Object((1,3,6,1,4,1,351,110,2,5,1,1,3),_SarChanNum_Type())
sarChanNum.setMaxAccess(_B)
if mibBuilder.loadTexts:sarChanNum.setStatus(_A)
_XmtCells_Type=Counter32
_XmtCells_Object=MibTableColumn
xmtCells=_XmtCells_Object((1,3,6,1,4,1,351,110,2,5,1,1,4),_XmtCells_Type())
xmtCells.setMaxAccess(_B)
if mibBuilder.loadTexts:xmtCells.setStatus(_A)
_XmtCellsCLP_Type=Counter32
_XmtCellsCLP_Object=MibTableColumn
xmtCellsCLP=_XmtCellsCLP_Object((1,3,6,1,4,1,351,110,2,5,1,1,5),_XmtCellsCLP_Type())
xmtCellsCLP.setMaxAccess(_B)
if mibBuilder.loadTexts:xmtCellsCLP.setStatus(_A)
_XmtCellsAIS_Type=Counter32
_XmtCellsAIS_Object=MibTableColumn
xmtCellsAIS=_XmtCellsAIS_Object((1,3,6,1,4,1,351,110,2,5,1,1,6),_XmtCellsAIS_Type())
xmtCellsAIS.setMaxAccess(_B)
if mibBuilder.loadTexts:xmtCellsAIS.setStatus(_A)
_XmtCellsFERF_Type=Counter32
_XmtCellsFERF_Object=MibTableColumn
xmtCellsFERF=_XmtCellsFERF_Object((1,3,6,1,4,1,351,110,2,5,1,1,7),_XmtCellsFERF_Type())
xmtCellsFERF.setMaxAccess(_B)
if mibBuilder.loadTexts:xmtCellsFERF.setStatus(_A)
_XmtCellsBCM_Type=Counter32
_XmtCellsBCM_Object=MibTableColumn
xmtCellsBCM=_XmtCellsBCM_Object((1,3,6,1,4,1,351,110,2,5,1,1,8),_XmtCellsBCM_Type())
xmtCellsBCM.setMaxAccess(_B)
if mibBuilder.loadTexts:xmtCellsBCM.setStatus(_A)
_XmtCellsEnd2EndLpBk_Type=Counter32
_XmtCellsEnd2EndLpBk_Object=MibTableColumn
xmtCellsEnd2EndLpBk=_XmtCellsEnd2EndLpBk_Object((1,3,6,1,4,1,351,110,2,5,1,1,9),_XmtCellsEnd2EndLpBk_Type())
xmtCellsEnd2EndLpBk.setMaxAccess(_B)
if mibBuilder.loadTexts:xmtCellsEnd2EndLpBk.setStatus(_A)
_XmtCellsSegmentLpBk_Type=Counter32
_XmtCellsSegmentLpBk_Object=MibTableColumn
xmtCellsSegmentLpBk=_XmtCellsSegmentLpBk_Object((1,3,6,1,4,1,351,110,2,5,1,1,10),_XmtCellsSegmentLpBk_Type())
xmtCellsSegmentLpBk.setMaxAccess(_B)
if mibBuilder.loadTexts:xmtCellsSegmentLpBk.setStatus(_A)
_XmtCellsDiscShelfAlarm_Type=Counter32
_XmtCellsDiscShelfAlarm_Object=MibTableColumn
xmtCellsDiscShelfAlarm=_XmtCellsDiscShelfAlarm_Object((1,3,6,1,4,1,351,110,2,5,1,1,11),_XmtCellsDiscShelfAlarm_Type())
xmtCellsDiscShelfAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:xmtCellsDiscShelfAlarm.setStatus(_A)
_RcvCells_Type=Counter32
_RcvCells_Object=MibTableColumn
rcvCells=_RcvCells_Object((1,3,6,1,4,1,351,110,2,5,1,1,12),_RcvCells_Type())
rcvCells.setMaxAccess(_B)
if mibBuilder.loadTexts:rcvCells.setStatus(_A)
_RcvCellsCLP_Type=Counter32
_RcvCellsCLP_Object=MibTableColumn
rcvCellsCLP=_RcvCellsCLP_Object((1,3,6,1,4,1,351,110,2,5,1,1,13),_RcvCellsCLP_Type())
rcvCellsCLP.setMaxAccess(_B)
if mibBuilder.loadTexts:rcvCellsCLP.setStatus(_A)
_RcvCellsAIS_Type=Counter32
_RcvCellsAIS_Object=MibTableColumn
rcvCellsAIS=_RcvCellsAIS_Object((1,3,6,1,4,1,351,110,2,5,1,1,14),_RcvCellsAIS_Type())
rcvCellsAIS.setMaxAccess(_B)
if mibBuilder.loadTexts:rcvCellsAIS.setStatus(_A)
_RcvCellsFERF_Type=Counter32
_RcvCellsFERF_Object=MibTableColumn
rcvCellsFERF=_RcvCellsFERF_Object((1,3,6,1,4,1,351,110,2,5,1,1,15),_RcvCellsFERF_Type())
rcvCellsFERF.setMaxAccess(_B)
if mibBuilder.loadTexts:rcvCellsFERF.setStatus(_A)
_RcvCellsBCM_Type=Counter32
_RcvCellsBCM_Object=MibTableColumn
rcvCellsBCM=_RcvCellsBCM_Object((1,3,6,1,4,1,351,110,2,5,1,1,16),_RcvCellsBCM_Type())
rcvCellsBCM.setMaxAccess(_B)
if mibBuilder.loadTexts:rcvCellsBCM.setStatus(_A)
_RcvCellsEnd2EndLpBk_Type=Counter32
_RcvCellsEnd2EndLpBk_Object=MibTableColumn
rcvCellsEnd2EndLpBk=_RcvCellsEnd2EndLpBk_Object((1,3,6,1,4,1,351,110,2,5,1,1,17),_RcvCellsEnd2EndLpBk_Type())
rcvCellsEnd2EndLpBk.setMaxAccess(_B)
if mibBuilder.loadTexts:rcvCellsEnd2EndLpBk.setStatus(_A)
_RcvCellsSegmentLpBk_Type=Counter32
_RcvCellsSegmentLpBk_Object=MibTableColumn
rcvCellsSegmentLpBk=_RcvCellsSegmentLpBk_Object((1,3,6,1,4,1,351,110,2,5,1,1,18),_RcvCellsSegmentLpBk_Type())
rcvCellsSegmentLpBk.setMaxAccess(_B)
if mibBuilder.loadTexts:rcvCellsSegmentLpBk.setStatus(_A)
_RcvCellsDiscOAM_Type=Counter32
_RcvCellsDiscOAM_Object=MibTableColumn
rcvCellsDiscOAM=_RcvCellsDiscOAM_Object((1,3,6,1,4,1,351,110,2,5,1,1,19),_RcvCellsDiscOAM_Type())
rcvCellsDiscOAM.setMaxAccess(_B)
if mibBuilder.loadTexts:rcvCellsDiscOAM.setStatus(_A)
class _SarClrButton_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_H,2)))
_SarClrButton_Type.__name__=_C
_SarClrButton_Object=MibTableColumn
sarClrButton=_SarClrButton_Object((1,3,6,1,4,1,351,110,2,5,1,1,20),_SarClrButton_Type())
sarClrButton.setMaxAccess(_G)
if mibBuilder.loadTexts:sarClrButton.setStatus(_A)
_ChanNumOfValidEntries_Type=Integer32
_ChanNumOfValidEntries_Object=MibScalar
chanNumOfValidEntries=_ChanNumOfValidEntries_Object((1,3,6,1,4,1,351,110,2,5,2),_ChanNumOfValidEntries_Type())
chanNumOfValidEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:chanNumOfValidEntries.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'cardInformation':cardInformation,'moduleSlotNumber':moduleSlotNumber,'functionModuleType':functionModuleType,'functionModuleDescription':functionModuleDescription,'functionModuleSerialNum':functionModuleSerialNum,'functionModuleHWRev':functionModuleHWRev,'functionModuleFWRev':functionModuleFWRev,'functionModuleState':functionModuleState,'functionModuleResetReason':functionModuleResetReason,'lineModuleType':lineModuleType,'lineModuleDescription':lineModuleDescription,'lineModuleSerialNum':lineModuleSerialNum,'lineModuleHWRev':lineModuleHWRev,'lineModuleFWRev':lineModuleFWRev,'lineModuleState':lineModuleState,'moduleTrapAlarmSeverity':moduleTrapAlarmSeverity,'mibVersionNumber':mibVersionNumber,'configChangeTypeBitMap':configChangeTypeBitMap,'configChangeObjectIndex':configChangeObjectIndex,'configChangeStatus':configChangeStatus,'cardIntegratedAlarmBitMap':cardIntegratedAlarmBitMap,'cleiCode':cleiCode,'macAddress':macAddress,'macAddrBlkSize':macAddrBlkSize,'finalTestTechnician':finalTestTechnician,'hwFailures':hwFailures,'hwHistory':hwHistory,'secLineModuleType':secLineModuleType,'secLineModuleDescription':secLineModuleDescription,'secLineModuleSerialNum':secLineModuleSerialNum,'secLineModuleHWRev':secLineModuleHWRev,'secLineModuleFWRev':secLineModuleFWRev,'secLineModuleState':secLineModuleState,'configChangeParentObjectIndex':configChangeParentObjectIndex,'configChangeGrandParentObjectIndex':configChangeGrandParentObjectIndex,'configChangeSMSpecificObject':configChangeSMSpecificObject,'transId':transId,'cardInterface':cardInterface,'interfaceLineTable':interfaceLineTable,'interfaceLineEntry':interfaceLineEntry,_A2:interfaceLineNum,'interfaceLineType':interfaceLineType,'interfaceNumOfPortsPerLine':interfaceNumOfPortsPerLine,'interfaceServiceType':interfaceServiceType,'interfaceNumOfPVC':interfaceNumOfPVC,'interfaceNumOfEgressQueue':interfaceNumOfEgressQueue,'interfaceNumOfValidEntries':interfaceNumOfValidEntries,'cardSelfTest':cardSelfTest,'selfTestEnable':selfTestEnable,'selfTestPeriod':selfTestPeriod,'selfTestState':selfTestState,'selfTestResultDescription':selfTestResultDescription,'selfTestClrResultButton':selfTestClrResultButton,'controlMsgCounter':controlMsgCounter,'riscXmtCtrlMsg':riscXmtCtrlMsg,'riscRcvCtrlMsg':riscRcvCtrlMsg,'sarXmtCtrlMsg':sarXmtCtrlMsg,'sarRcvCtrlMsg':sarRcvCtrlMsg,'sarCtrlMsgDiscLenErr':sarCtrlMsgDiscLenErr,'sarCtrlMsgDiscCRCErr':sarCtrlMsgDiscCRCErr,'sarCtrlMsgDiscUnknownChan':sarCtrlMsgDiscUnknownChan,'sarCtrlMsgLastUnkownChan':sarCtrlMsgLastUnkownChan,'ctrlMsgClrButton':ctrlMsgClrButton,'sarChannelCounter':sarChannelCounter,'sarChannelCounterTable':sarChannelCounterTable,'sarChannelCounterEntry':sarChannelCounterEntry,_A4:sarShelfNum,_A5:sarSlotNum,_A6:sarChanNum,'xmtCells':xmtCells,'xmtCellsCLP':xmtCellsCLP,'xmtCellsAIS':xmtCellsAIS,'xmtCellsFERF':xmtCellsFERF,'xmtCellsBCM':xmtCellsBCM,'xmtCellsEnd2EndLpBk':xmtCellsEnd2EndLpBk,'xmtCellsSegmentLpBk':xmtCellsSegmentLpBk,'xmtCellsDiscShelfAlarm':xmtCellsDiscShelfAlarm,'rcvCells':rcvCells,'rcvCellsCLP':rcvCellsCLP,'rcvCellsAIS':rcvCellsAIS,'rcvCellsFERF':rcvCellsFERF,'rcvCellsBCM':rcvCellsBCM,'rcvCellsEnd2EndLpBk':rcvCellsEnd2EndLpBk,'rcvCellsSegmentLpBk':rcvCellsSegmentLpBk,'rcvCellsDiscOAM':rcvCellsDiscOAM,'sarClrButton':sarClrButton,'chanNumOfValidEntries':chanNumOfValidEntries})