_s='voipProfileName'
_r='mdmIndex'
_q='k56flex'
_p='v32bis'
_o='v22bis'
_n='bell212'
_m='bell103'
_l='mdmProfileName'
_k='auto'
_j='b56000'
_i='b54000'
_h='b52000'
_g='b50000'
_f='b48000'
_e='b46000'
_d='b44000'
_c='b42000'
_b='b40000'
_a='b38000'
_Z='b36000'
_Y='b34000'
_X='b33600'
_W='b32000'
_V='b31200'
_U='b28800'
_T='b26400'
_S='b24000'
_R='b21600'
_Q='b19200'
_P='b16800'
_O='b14400'
_N='b12000'
_M='b9600'
_L='b7200'
_K='b4800'
_J='b2400'
_I='b1200'
_H='b300'
_G='BIANCA-BRICK-MIBMODEM-MIB'
_F='none'
_E='off'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Bintec_ObjectIdentity=ObjectIdentity
bintec=_Bintec_ObjectIdentity((1,3,6,1,4,1,272))
_Bibo_ObjectIdentity=ObjectIdentity
bibo=_Bibo_ObjectIdentity((1,3,6,1,4,1,272,4))
_Mdm_ObjectIdentity=ObjectIdentity
mdm=_Mdm_ObjectIdentity((1,3,6,1,4,1,272,4,18))
_MdmProfileTable_Object=MibTable
mdmProfileTable=_MdmProfileTable_Object((1,3,6,1,4,1,272,4,18,1))
if mibBuilder.loadTexts:mdmProfileTable.setStatus(_A)
_MdmProfileEntry_Object=MibTableRow
mdmProfileEntry=_MdmProfileEntry_Object((1,3,6,1,4,1,272,4,18,1,1))
mdmProfileEntry.setIndexNames((0,_G,_l))
if mibBuilder.loadTexts:mdmProfileEntry.setStatus(_A)
class _MdmProfileName_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('profile-1',1),('profile-2',2),('profile-3',3),('profile-4',4),('profile-5',5),('profile-6',6),('profile-7',7),('profile-8',8)))
_MdmProfileName_Type.__name__=_B
_MdmProfileName_Object=MibTableColumn
mdmProfileName=_MdmProfileName_Object((1,3,6,1,4,1,272,4,18,1,1,1),_MdmProfileName_Type())
mdmProfileName.setMaxAccess(_D)
if mibBuilder.loadTexts:mdmProfileName.setStatus(_A)
_MdmProfileDescr_Type=DisplayString
_MdmProfileDescr_Object=MibTableColumn
mdmProfileDescr=_MdmProfileDescr_Object((1,3,6,1,4,1,272,4,18,1,1,2),_MdmProfileDescr_Type())
mdmProfileDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmProfileDescr.setStatus(_A)
class _MdmProfileModulation_Type(Integer32):defaultValue=9;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_m,1),(_n,2),('v21',3),('v22',4),(_o,5),('v23',6),('v32',7),(_p,8),('v34',9),(_q,10),('vfc',11),('v90',12)))
_MdmProfileModulation_Type.__name__=_B
_MdmProfileModulation_Object=MibTableColumn
mdmProfileModulation=_MdmProfileModulation_Object((1,3,6,1,4,1,272,4,18,1,1,3),_MdmProfileModulation_Type())
mdmProfileModulation.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmProfileModulation.setStatus(_A)
class _MdmProfileMinBps_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(75,300,1200,2400,4800,7200,9600,12000,14400,16800,19200,21600,24000,26400,28800,31200,32000,33600,34000,36000,38000,40000,42000,44000,46000,48000,50000,52000,54000,56000)));namedValues=NamedValues(*(('b75',75),(_H,300),(_I,1200),(_J,2400),(_K,4800),(_L,7200),(_M,9600),(_N,12000),(_O,14400),(_P,16800),(_Q,19200),(_R,21600),(_S,24000),(_T,26400),(_U,28800),(_V,31200),(_W,32000),(_X,33600),(_Y,34000),(_Z,36000),(_a,38000),(_b,40000),(_c,42000),(_d,44000),(_e,46000),(_f,48000),(_g,50000),(_h,52000),(_i,54000),(_j,56000)))
_MdmProfileMinBps_Type.__name__=_B
_MdmProfileMinBps_Object=MibTableColumn
mdmProfileMinBps=_MdmProfileMinBps_Object((1,3,6,1,4,1,272,4,18,1,1,4),_MdmProfileMinBps_Type())
mdmProfileMinBps.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmProfileMinBps.setStatus(_A)
class _MdmProfileMaxRecvBps_Type(Integer32):defaultValue=33600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(300,1200,2400,4800,7200,9600,12000,14400,16800,19200,21600,24000,26400,28800,31200,32000,33600,34000,36000,38000,40000,42000,44000,46000,48000,50000,52000,54000,56000)));namedValues=NamedValues(*((_H,300),(_I,1200),(_J,2400),(_K,4800),(_L,7200),(_M,9600),(_N,12000),(_O,14400),(_P,16800),(_Q,19200),(_R,21600),(_S,24000),(_T,26400),(_U,28800),(_V,31200),(_W,32000),(_X,33600),(_Y,34000),(_Z,36000),(_a,38000),(_b,40000),(_c,42000),(_d,44000),(_e,46000),(_f,48000),(_g,50000),(_h,52000),(_i,54000),(_j,56000)))
_MdmProfileMaxRecvBps_Type.__name__=_B
_MdmProfileMaxRecvBps_Object=MibTableColumn
mdmProfileMaxRecvBps=_MdmProfileMaxRecvBps_Object((1,3,6,1,4,1,272,4,18,1,1,5),_MdmProfileMaxRecvBps_Type())
mdmProfileMaxRecvBps.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmProfileMaxRecvBps.setStatus(_A)
class _MdmProfileMaxXmitBps_Type(Integer32):defaultValue=33600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(300,1200,2400,4800,7200,9600,12000,14400,16800,19200,21600,24000,26400,28800,31200,32000,33600,34000,36000,38000,40000,42000,44000,46000,48000,50000,52000,54000,56000)));namedValues=NamedValues(*((_H,300),(_I,1200),(_J,2400),(_K,4800),(_L,7200),(_M,9600),(_N,12000),(_O,14400),(_P,16800),(_Q,19200),(_R,21600),(_S,24000),(_T,26400),(_U,28800),(_V,31200),(_W,32000),(_X,33600),(_Y,34000),(_Z,36000),(_a,38000),(_b,40000),(_c,42000),(_d,44000),(_e,46000),(_f,48000),(_g,50000),(_h,52000),(_i,54000),(_j,56000)))
_MdmProfileMaxXmitBps_Type.__name__=_B
_MdmProfileMaxXmitBps_Object=MibTableColumn
mdmProfileMaxXmitBps=_MdmProfileMaxXmitBps_Object((1,3,6,1,4,1,272,4,18,1,1,6),_MdmProfileMaxXmitBps_Type())
mdmProfileMaxXmitBps.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmProfileMaxXmitBps.setStatus(_A)
class _MdmProfileAutoMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),('on',2)))
_MdmProfileAutoMode_Type.__name__=_B
_MdmProfileAutoMode_Object=MibTableColumn
mdmProfileAutoMode=_MdmProfileAutoMode_Object((1,3,6,1,4,1,272,4,18,1,1,7),_MdmProfileAutoMode_Type())
mdmProfileAutoMode.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmProfileAutoMode.setStatus(_A)
class _MdmProfileComprV42bis_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_k,2)))
_MdmProfileComprV42bis_Type.__name__=_B
_MdmProfileComprV42bis_Object=MibTableColumn
mdmProfileComprV42bis=_MdmProfileComprV42bis_Object((1,3,6,1,4,1,272,4,18,1,1,8),_MdmProfileComprV42bis_Type())
mdmProfileComprV42bis.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmProfileComprV42bis.setStatus(_A)
class _MdmProfileComprMNP5_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_k,2)))
_MdmProfileComprMNP5_Type.__name__=_B
_MdmProfileComprMNP5_Object=MibTableColumn
mdmProfileComprMNP5=_MdmProfileComprMNP5_Object((1,3,6,1,4,1,272,4,18,1,1,9),_MdmProfileComprMNP5_Type())
mdmProfileComprMNP5.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmProfileComprMNP5.setStatus(_A)
class _MdmProfileErrorCorr_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),('required',2),(_k,3),('lapm',4),('mnp',5)))
_MdmProfileErrorCorr_Type.__name__=_B
_MdmProfileErrorCorr_Object=MibTableColumn
mdmProfileErrorCorr=_MdmProfileErrorCorr_Object((1,3,6,1,4,1,272,4,18,1,1,10),_MdmProfileErrorCorr_Type())
mdmProfileErrorCorr.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmProfileErrorCorr.setStatus(_A)
class _MdmProfileXmitLevel_Type(Integer32):defaultValue=-10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-15,0))
_MdmProfileXmitLevel_Type.__name__=_B
_MdmProfileXmitLevel_Object=MibTableColumn
mdmProfileXmitLevel=_MdmProfileXmitLevel_Object((1,3,6,1,4,1,272,4,18,1,1,11),_MdmProfileXmitLevel_Type())
mdmProfileXmitLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmProfileXmitLevel.setStatus(_A)
class _MdmProfileCDWaitTime_Type(Integer32):defaultValue=50000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,255000))
_MdmProfileCDWaitTime_Type.__name__=_B
_MdmProfileCDWaitTime_Object=MibTableColumn
mdmProfileCDWaitTime=_MdmProfileCDWaitTime_Object((1,3,6,1,4,1,272,4,18,1,1,12),_MdmProfileCDWaitTime_Type())
mdmProfileCDWaitTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmProfileCDWaitTime.setStatus(_A)
class _MdmProfileCDRespTime_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,25500))
_MdmProfileCDRespTime_Type.__name__=_B
_MdmProfileCDRespTime_Object=MibTableColumn
mdmProfileCDRespTime=_MdmProfileCDRespTime_Object((1,3,6,1,4,1,272,4,18,1,1,13),_MdmProfileCDRespTime_Type())
mdmProfileCDRespTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmProfileCDRespTime.setStatus(_A)
class _MdmProfileCDDiscTime_Type(Integer32):defaultValue=1400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,25500))
_MdmProfileCDDiscTime_Type.__name__=_B
_MdmProfileCDDiscTime_Object=MibTableColumn
mdmProfileCDDiscTime=_MdmProfileCDDiscTime_Object((1,3,6,1,4,1,272,4,18,1,1,14),_MdmProfileCDDiscTime_Type())
mdmProfileCDDiscTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmProfileCDDiscTime.setStatus(_A)
class _MdmProfileRetrain_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('retrain',2),('fallbf',3)))
_MdmProfileRetrain_Type.__name__=_B
_MdmProfileRetrain_Object=MibTableColumn
mdmProfileRetrain=_MdmProfileRetrain_Object((1,3,6,1,4,1,272,4,18,1,1,15),_MdmProfileRetrain_Type())
mdmProfileRetrain.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmProfileRetrain.setStatus(_A)
class _MdmProfileIdleTimerMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('dynamic',2)))
_MdmProfileIdleTimerMode_Type.__name__=_B
_MdmProfileIdleTimerMode_Object=MibTableColumn
mdmProfileIdleTimerMode=_MdmProfileIdleTimerMode_Object((1,3,6,1,4,1,272,4,18,1,1,16),_MdmProfileIdleTimerMode_Type())
mdmProfileIdleTimerMode.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmProfileIdleTimerMode.setStatus(_A)
class _MdmProfileIdleTimerFixedDelay_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000))
_MdmProfileIdleTimerFixedDelay_Type.__name__=_B
_MdmProfileIdleTimerFixedDelay_Object=MibTableColumn
mdmProfileIdleTimerFixedDelay=_MdmProfileIdleTimerFixedDelay_Object((1,3,6,1,4,1,272,4,18,1,1,17),_MdmProfileIdleTimerFixedDelay_Type())
mdmProfileIdleTimerFixedDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmProfileIdleTimerFixedDelay.setStatus(_A)
class _MdmProfileIdleTimerCharDelay_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_MdmProfileIdleTimerCharDelay_Type.__name__=_B
_MdmProfileIdleTimerCharDelay_Object=MibTableColumn
mdmProfileIdleTimerCharDelay=_MdmProfileIdleTimerCharDelay_Object((1,3,6,1,4,1,272,4,18,1,1,18),_MdmProfileIdleTimerCharDelay_Type())
mdmProfileIdleTimerCharDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmProfileIdleTimerCharDelay.setStatus(_A)
_MdmTable_Object=MibTable
mdmTable=_MdmTable_Object((1,3,6,1,4,1,272,4,18,2))
if mibBuilder.loadTexts:mdmTable.setStatus(_A)
_MdmEntry_Object=MibTableRow
mdmEntry=_MdmEntry_Object((1,3,6,1,4,1,272,4,18,2,1))
mdmEntry.setIndexNames((0,_G,_r))
if mibBuilder.loadTexts:mdmEntry.setStatus(_A)
_MdmIndex_Type=Integer32
_MdmIndex_Object=MibTableColumn
mdmIndex=_MdmIndex_Object((1,3,6,1,4,1,272,4,18,2,1,1),_MdmIndex_Type())
mdmIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mdmIndex.setStatus(_A)
class _MdmAction_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('reboot',1),('disabled',2),('enabled',3)))
_MdmAction_Type.__name__=_B
_MdmAction_Object=MibTableColumn
mdmAction=_MdmAction_Object((1,3,6,1,4,1,272,4,18,2,1,2),_MdmAction_Type())
mdmAction.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmAction.setStatus(_A)
class _MdmType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('csm56K',1),('csm336',2),('mdm144',3),('mdm336',4),('telindus',5)))
_MdmType_Type.__name__=_B
_MdmType_Object=MibTableColumn
mdmType=_MdmType_Object((1,3,6,1,4,1,272,4,18,2,1,3),_MdmType_Type())
mdmType.setMaxAccess(_D)
if mibBuilder.loadTexts:mdmType.setStatus(_A)
class _MdmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('booting',1),('idle',2),('calling',3),('called',4),('connected',5),('hangup',6),('stopped',7)))
_MdmState_Type.__name__=_B
_MdmState_Object=MibTableColumn
mdmState=_MdmState_Object((1,3,6,1,4,1,272,4,18,2,1,4),_MdmState_Type())
mdmState.setMaxAccess(_D)
if mibBuilder.loadTexts:mdmState.setStatus(_A)
class _MdmMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,7)));namedValues=NamedValues(*(('modem',1),('ppp',2),('fax',3),('dtmf',4),('voice',5),(_F,7)))
_MdmMode_Type.__name__=_B
_MdmMode_Object=MibTableColumn
mdmMode=_MdmMode_Object((1,3,6,1,4,1,272,4,18,2,1,5),_MdmMode_Type())
mdmMode.setMaxAccess(_D)
if mibBuilder.loadTexts:mdmMode.setStatus(_A)
class _MdmModulation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,31)));namedValues=NamedValues(*((_m,1),(_n,2),('v21',3),('v22',4),(_o,5),('v23',6),('v32',7),(_p,8),('v34',9),(_q,10),('vfc',11),('v90',12),('unknown',31)))
_MdmModulation_Type.__name__=_B
_MdmModulation_Object=MibTableColumn
mdmModulation=_MdmModulation_Object((1,3,6,1,4,1,272,4,18,2,1,6),_MdmModulation_Type())
mdmModulation.setMaxAccess(_D)
if mibBuilder.loadTexts:mdmModulation.setStatus(_A)
class _MdmErrorCorr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('alt',2),('lapm',3)))
_MdmErrorCorr_Type.__name__=_B
_MdmErrorCorr_Object=MibTableColumn
mdmErrorCorr=_MdmErrorCorr_Object((1,3,6,1,4,1,272,4,18,2,1,7),_MdmErrorCorr_Type())
mdmErrorCorr.setMaxAccess(_D)
if mibBuilder.loadTexts:mdmErrorCorr.setStatus(_A)
class _MdmCompression_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('class5',2),('v42bis',3)))
_MdmCompression_Type.__name__=_B
_MdmCompression_Object=MibTableColumn
mdmCompression=_MdmCompression_Object((1,3,6,1,4,1,272,4,18,2,1,8),_MdmCompression_Type())
mdmCompression.setMaxAccess(_D)
if mibBuilder.loadTexts:mdmCompression.setStatus(_A)
_MdmXmitSpeed_Type=Integer32
_MdmXmitSpeed_Object=MibTableColumn
mdmXmitSpeed=_MdmXmitSpeed_Object((1,3,6,1,4,1,272,4,18,2,1,9),_MdmXmitSpeed_Type())
mdmXmitSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:mdmXmitSpeed.setStatus(_A)
_MdmRcvSpeed_Type=Integer32
_MdmRcvSpeed_Object=MibTableColumn
mdmRcvSpeed=_MdmRcvSpeed_Object((1,3,6,1,4,1,272,4,18,2,1,10),_MdmRcvSpeed_Type())
mdmRcvSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:mdmRcvSpeed.setStatus(_A)
_MdmIfIndex_Type=Integer32
_MdmIfIndex_Object=MibTableColumn
mdmIfIndex=_MdmIfIndex_Object((1,3,6,1,4,1,272,4,18,2,1,11),_MdmIfIndex_Type())
mdmIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mdmIfIndex.setStatus(_A)
class _MdmIfBchannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_MdmIfBchannel_Type.__name__=_B
_MdmIfBchannel_Object=MibTableColumn
mdmIfBchannel=_MdmIfBchannel_Object((1,3,6,1,4,1,272,4,18,2,1,12),_MdmIfBchannel_Type())
mdmIfBchannel.setMaxAccess(_D)
if mibBuilder.loadTexts:mdmIfBchannel.setStatus(_A)
_VoipProfileTable_Object=MibTable
voipProfileTable=_VoipProfileTable_Object((1,3,6,1,4,1,272,4,18,3))
if mibBuilder.loadTexts:voipProfileTable.setStatus(_A)
_VoipProfileEntry_Object=MibTableRow
voipProfileEntry=_VoipProfileEntry_Object((1,3,6,1,4,1,272,4,18,3,1))
voipProfileEntry.setIndexNames((0,_G,_s))
if mibBuilder.loadTexts:voipProfileEntry.setStatus(_A)
class _VoipProfileName_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('voip-profile-1',1),('voip-profile-2',2),('voip-profile-3',3),('voip-profile-4',4),('voip-profile-5',5),('voip-profile-6',6),('voip-profile-7',7),('voip-profile-8',8),('voip-profile-9',9),('voip-profile-10',10)))
_VoipProfileName_Type.__name__=_B
_VoipProfileName_Object=MibTableColumn
voipProfileName=_VoipProfileName_Object((1,3,6,1,4,1,272,4,18,3,1,1),_VoipProfileName_Type())
voipProfileName.setMaxAccess(_D)
if mibBuilder.loadTexts:voipProfileName.setStatus(_A)
_VoipProfileDescr_Type=DisplayString
_VoipProfileDescr_Object=MibTableColumn
voipProfileDescr=_VoipProfileDescr_Object((1,3,6,1,4,1,272,4,18,3,1,2),_VoipProfileDescr_Type())
voipProfileDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:voipProfileDescr.setStatus(_A)
class _VoipProfileEncoding_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('g711uLaw',1),('g711aLaw',2),('g729a',3),('g729b',4),('g723-63',5),('g723-53',6)))
_VoipProfileEncoding_Type.__name__=_B
_VoipProfileEncoding_Object=MibTableColumn
voipProfileEncoding=_VoipProfileEncoding_Object((1,3,6,1,4,1,272,4,18,3,1,3),_VoipProfileEncoding_Type())
voipProfileEncoding.setMaxAccess(_C)
if mibBuilder.loadTexts:voipProfileEncoding.setStatus(_A)
class _VoipProfileEncapsulation_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('raw',1),('rtp',2),('aal2',3)))
_VoipProfileEncapsulation_Type.__name__=_B
_VoipProfileEncapsulation_Object=MibTableColumn
voipProfileEncapsulation=_VoipProfileEncapsulation_Object((1,3,6,1,4,1,272,4,18,3,1,4),_VoipProfileEncapsulation_Type())
voipProfileEncapsulation.setMaxAccess(_C)
if mibBuilder.loadTexts:voipProfileEncapsulation.setStatus(_A)
class _VoipProfileEchoCancellation_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),('on',2)))
_VoipProfileEchoCancellation_Type.__name__=_B
_VoipProfileEchoCancellation_Object=MibTableColumn
voipProfileEchoCancellation=_VoipProfileEchoCancellation_Object((1,3,6,1,4,1,272,4,18,3,1,5),_VoipProfileEchoCancellation_Type())
voipProfileEchoCancellation.setMaxAccess(_C)
if mibBuilder.loadTexts:voipProfileEchoCancellation.setStatus(_A)
class _VoipProfileComfortNoise_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('vad',2),('cng',3),('vad-cng',4)))
_VoipProfileComfortNoise_Type.__name__=_B
_VoipProfileComfortNoise_Object=MibTableColumn
voipProfileComfortNoise=_VoipProfileComfortNoise_Object((1,3,6,1,4,1,272,4,18,3,1,6),_VoipProfileComfortNoise_Type())
voipProfileComfortNoise.setMaxAccess(_C)
if mibBuilder.loadTexts:voipProfileComfortNoise.setStatus(_A)
class _VoipProfilePacketLength_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,255))
_VoipProfilePacketLength_Type.__name__=_B
_VoipProfilePacketLength_Object=MibTableColumn
voipProfilePacketLength=_VoipProfilePacketLength_Object((1,3,6,1,4,1,272,4,18,3,1,7),_VoipProfilePacketLength_Type())
voipProfilePacketLength.setMaxAccess(_C)
if mibBuilder.loadTexts:voipProfilePacketLength.setStatus(_A)
class _VoipProfilePacketInterval_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,210))
_VoipProfilePacketInterval_Type.__name__=_B
_VoipProfilePacketInterval_Object=MibTableColumn
voipProfilePacketInterval=_VoipProfilePacketInterval_Object((1,3,6,1,4,1,272,4,18,3,1,8),_VoipProfilePacketInterval_Type())
voipProfilePacketInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:voipProfilePacketInterval.setStatus(_A)
class _VoipProfileJitterBufferDelay_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,250))
_VoipProfileJitterBufferDelay_Type.__name__=_B
_VoipProfileJitterBufferDelay_Object=MibTableColumn
voipProfileJitterBufferDelay=_VoipProfileJitterBufferDelay_Object((1,3,6,1,4,1,272,4,18,3,1,9),_VoipProfileJitterBufferDelay_Type())
voipProfileJitterBufferDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:voipProfileJitterBufferDelay.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'bintec':bintec,'bibo':bibo,'mdm':mdm,'mdmProfileTable':mdmProfileTable,'mdmProfileEntry':mdmProfileEntry,_l:mdmProfileName,'mdmProfileDescr':mdmProfileDescr,'mdmProfileModulation':mdmProfileModulation,'mdmProfileMinBps':mdmProfileMinBps,'mdmProfileMaxRecvBps':mdmProfileMaxRecvBps,'mdmProfileMaxXmitBps':mdmProfileMaxXmitBps,'mdmProfileAutoMode':mdmProfileAutoMode,'mdmProfileComprV42bis':mdmProfileComprV42bis,'mdmProfileComprMNP5':mdmProfileComprMNP5,'mdmProfileErrorCorr':mdmProfileErrorCorr,'mdmProfileXmitLevel':mdmProfileXmitLevel,'mdmProfileCDWaitTime':mdmProfileCDWaitTime,'mdmProfileCDRespTime':mdmProfileCDRespTime,'mdmProfileCDDiscTime':mdmProfileCDDiscTime,'mdmProfileRetrain':mdmProfileRetrain,'mdmProfileIdleTimerMode':mdmProfileIdleTimerMode,'mdmProfileIdleTimerFixedDelay':mdmProfileIdleTimerFixedDelay,'mdmProfileIdleTimerCharDelay':mdmProfileIdleTimerCharDelay,'mdmTable':mdmTable,'mdmEntry':mdmEntry,_r:mdmIndex,'mdmAction':mdmAction,'mdmType':mdmType,'mdmState':mdmState,'mdmMode':mdmMode,'mdmModulation':mdmModulation,'mdmErrorCorr':mdmErrorCorr,'mdmCompression':mdmCompression,'mdmXmitSpeed':mdmXmitSpeed,'mdmRcvSpeed':mdmRcvSpeed,'mdmIfIndex':mdmIfIndex,'mdmIfBchannel':mdmIfBchannel,'voipProfileTable':voipProfileTable,'voipProfileEntry':voipProfileEntry,_s:voipProfileName,'voipProfileDescr':voipProfileDescr,'voipProfileEncoding':voipProfileEncoding,'voipProfileEncapsulation':voipProfileEncapsulation,'voipProfileEchoCancellation':voipProfileEchoCancellation,'voipProfileComfortNoise':voipProfileComfortNoise,'voipProfilePacketLength':voipProfilePacketLength,'voipProfilePacketInterval':voipProfilePacketInterval,'voipProfileJitterBufferDelay':voipProfileJitterBufferDelay})