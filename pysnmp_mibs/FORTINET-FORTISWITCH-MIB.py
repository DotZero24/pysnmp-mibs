_n='fsTrunkObjectGroup'
_m='fsSystemObjectGroup'
_l='fsNotificationGroup'
_k='fsTrapMemberUp'
_j='fsTrapMemberDown'
_i='fsIpAddress'
_h='fsSensorPsuEventType'
_g='fsSensorFanEventType'
_f='fsAlarmThresholdUnits'
_e='fsAlarmThresholdValue'
_d='fsAlarmEventType'
_c='fsLearningTrapType'
_b='fsLearningTrapVid'
_a='fsLlvTrapMsg'
_Z='fsSysDiskCapacity'
_Y='fsSysDiskUsage'
_X='fsSysMemCapacity'
_W='fsSysMemUsage'
_V='fsSysCpuUsage'
_U='fsSysVersion'
_T='Gauge32'
_S='dot1dTpFdbPort'
_R='dot1dTpFdbAddress'
_Q='fsSensorIdx'
_P='fsSensorType'
_O='fsSensorName'
_N='DisplayString'
_M='ifName'
_L='IF-MIB'
_K='BRIDGE-MIB'
_J='fsTrunkMember'
_I='Integer32'
_H='read-only'
_G='sysName'
_F='SNMPv2-MIB'
_E='fnSysSerial'
_D='FORTINET-CORE-MIB'
_C='accessible-for-notify'
_B='FORTINET-FORTISWITCH-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dTpFdbAddress,dot1dTpFdbPort=mibBuilder.importSymbols(_K,_R,_S)
fnSysSerial,fortinet=mibBuilder.importSymbols(_D,_E,'fortinet')
ifName,=mibBuilder.importSymbols(_L,_M)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysName,=mibBuilder.importSymbols(_F,_G)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_T,_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_N,'PhysAddress','TextualConvention')
fnFortiSwitchMib=ModuleIdentity((1,3,6,1,4,1,12356,106))
if mibBuilder.loadTexts:fnFortiSwitchMib.setRevisions(('2022-04-01 00:00',))
_FsCommon_ObjectIdentity=ObjectIdentity
fsCommon=_FsCommon_ObjectIdentity((1,3,6,1,4,1,12356,106,1))
_FsSys_ObjectIdentity=ObjectIdentity
fsSys=_FsSys_ObjectIdentity((1,3,6,1,4,1,12356,106,1,1))
_FsSysSerial_Type=DisplayString
_FsSysSerial_Object=MibScalar
fsSysSerial=_FsSysSerial_Object((1,3,6,1,4,1,12356,106,1,1,1),_FsSysSerial_Type())
fsSysSerial.setMaxAccess(_H)
if mibBuilder.loadTexts:fsSysSerial.setStatus(_A)
_FsTraps_ObjectIdentity=ObjectIdentity
fsTraps=_FsTraps_ObjectIdentity((1,3,6,1,4,1,12356,106,2))
_FsTrapPrefix_ObjectIdentity=ObjectIdentity
fsTrapPrefix=_FsTrapPrefix_ObjectIdentity((1,3,6,1,4,1,12356,106,2,0))
_FsTrapObjects_ObjectIdentity=ObjectIdentity
fsTrapObjects=_FsTrapObjects_ObjectIdentity((1,3,6,1,4,1,12356,106,2,1))
_FsLlvTrapMsg_Type=DisplayString
_FsLlvTrapMsg_Object=MibScalar
fsLlvTrapMsg=_FsLlvTrapMsg_Object((1,3,6,1,4,1,12356,106,2,1,1),_FsLlvTrapMsg_Type())
fsLlvTrapMsg.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLlvTrapMsg.setStatus(_A)
_FsLearningTrapVid_Type=Integer32
_FsLearningTrapVid_Object=MibScalar
fsLearningTrapVid=_FsLearningTrapVid_Object((1,3,6,1,4,1,12356,106,2,1,2),_FsLearningTrapVid_Type())
fsLearningTrapVid.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLearningTrapVid.setStatus(_A)
class _FsLearningTrapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('add',1),('delete',2),('movefrom',3),('moveto',4)))
_FsLearningTrapType_Type.__name__=_I
_FsLearningTrapType_Object=MibScalar
fsLearningTrapType=_FsLearningTrapType_Object((1,3,6,1,4,1,12356,106,2,1,3),_FsLearningTrapType_Type())
fsLearningTrapType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLearningTrapType.setStatus(_A)
_FsSensorName_Type=DisplayString
_FsSensorName_Object=MibScalar
fsSensorName=_FsSensorName_Object((1,3,6,1,4,1,12356,106,2,1,4),_FsSensorName_Type())
fsSensorName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSensorName.setStatus(_A)
class _FsSensorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,6)));namedValues=NamedValues(*(('temperature',1),('poe',2),('cpu',3),('memory',4),('disk',6)))
_FsSensorType_Type.__name__=_I
_FsSensorType_Object=MibScalar
fsSensorType=_FsSensorType_Object((1,3,6,1,4,1,12356,106,2,1,5),_FsSensorType_Type())
fsSensorType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSensorType.setStatus(_A)
_FsSensorIdx_Type=Integer32
_FsSensorIdx_Object=MibScalar
fsSensorIdx=_FsSensorIdx_Object((1,3,6,1,4,1,12356,106,2,1,6),_FsSensorIdx_Type())
fsSensorIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSensorIdx.setStatus(_A)
class _FsSensorFanEventType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('detected',1),('undetected',2),('resumed',3),('failure',4)))
_FsSensorFanEventType_Type.__name__=_I
_FsSensorFanEventType_Object=MibScalar
fsSensorFanEventType=_FsSensorFanEventType_Object((1,3,6,1,4,1,12356,106,2,1,7),_FsSensorFanEventType_Type())
fsSensorFanEventType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSensorFanEventType.setStatus(_A)
class _FsSensorPsuEventType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('up',1),('connected',2),('good',3),('down',4),('disconnected',5),('bad',6)))
_FsSensorPsuEventType_Type.__name__=_I
_FsSensorPsuEventType_Object=MibScalar
fsSensorPsuEventType=_FsSensorPsuEventType_Object((1,3,6,1,4,1,12356,106,2,1,8),_FsSensorPsuEventType_Type())
fsSensorPsuEventType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSensorPsuEventType.setStatus(_A)
class _FsAlarmEventType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('inrange',1),('warning',2),('outofrange',3),('cleared',4)))
_FsAlarmEventType_Type.__name__=_I
_FsAlarmEventType_Object=MibScalar
fsAlarmEventType=_FsAlarmEventType_Object((1,3,6,1,4,1,12356,106,2,1,9),_FsAlarmEventType_Type())
fsAlarmEventType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsAlarmEventType.setStatus(_A)
_FsAlarmThresholdValue_Type=Integer32
_FsAlarmThresholdValue_Object=MibScalar
fsAlarmThresholdValue=_FsAlarmThresholdValue_Object((1,3,6,1,4,1,12356,106,2,1,10),_FsAlarmThresholdValue_Type())
fsAlarmThresholdValue.setMaxAccess(_C)
if mibBuilder.loadTexts:fsAlarmThresholdValue.setStatus(_A)
class _FsAlarmThresholdUnits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('celcius',1),('watts',2),('percentage',3),('unknown',4)))
_FsAlarmThresholdUnits_Type.__name__=_I
_FsAlarmThresholdUnits_Object=MibScalar
fsAlarmThresholdUnits=_FsAlarmThresholdUnits_Object((1,3,6,1,4,1,12356,106,2,1,11),_FsAlarmThresholdUnits_Type())
fsAlarmThresholdUnits.setMaxAccess(_C)
if mibBuilder.loadTexts:fsAlarmThresholdUnits.setStatus(_A)
_FsIpAddress_Type=IpAddress
_FsIpAddress_Object=MibScalar
fsIpAddress=_FsIpAddress_Object((1,3,6,1,4,1,12356,106,2,1,12),_FsIpAddress_Type())
fsIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpAddress.setStatus(_A)
_FsTrunkMemPrefix_ObjectIdentity=ObjectIdentity
fsTrunkMemPrefix=_FsTrunkMemPrefix_ObjectIdentity((1,3,6,1,4,1,12356,106,3))
class _FsTrunkMember_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,82))
_FsTrunkMember_Type.__name__=_N
_FsTrunkMember_Object=MibScalar
fsTrunkMember=_FsTrunkMember_Object((1,3,6,1,4,1,12356,106,3,1),_FsTrunkMember_Type())
fsTrunkMember.setMaxAccess(_H)
if mibBuilder.loadTexts:fsTrunkMember.setStatus(_A)
_FsSystem_ObjectIdentity=ObjectIdentity
fsSystem=_FsSystem_ObjectIdentity((1,3,6,1,4,1,12356,106,4))
_FsSystemInfo_ObjectIdentity=ObjectIdentity
fsSystemInfo=_FsSystemInfo_ObjectIdentity((1,3,6,1,4,1,12356,106,4,1))
class _FsSysVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_FsSysVersion_Type.__name__=_N
_FsSysVersion_Object=MibScalar
fsSysVersion=_FsSysVersion_Object((1,3,6,1,4,1,12356,106,4,1,1),_FsSysVersion_Type())
fsSysVersion.setMaxAccess(_H)
if mibBuilder.loadTexts:fsSysVersion.setStatus(_A)
class _FsSysCpuUsage_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FsSysCpuUsage_Type.__name__=_T
_FsSysCpuUsage_Object=MibScalar
fsSysCpuUsage=_FsSysCpuUsage_Object((1,3,6,1,4,1,12356,106,4,1,2),_FsSysCpuUsage_Type())
fsSysCpuUsage.setMaxAccess(_H)
if mibBuilder.loadTexts:fsSysCpuUsage.setStatus(_A)
_FsSysMemUsage_Type=Gauge32
_FsSysMemUsage_Object=MibScalar
fsSysMemUsage=_FsSysMemUsage_Object((1,3,6,1,4,1,12356,106,4,1,3),_FsSysMemUsage_Type())
fsSysMemUsage.setMaxAccess(_H)
if mibBuilder.loadTexts:fsSysMemUsage.setStatus(_A)
_FsSysMemCapacity_Type=Gauge32
_FsSysMemCapacity_Object=MibScalar
fsSysMemCapacity=_FsSysMemCapacity_Object((1,3,6,1,4,1,12356,106,4,1,4),_FsSysMemCapacity_Type())
fsSysMemCapacity.setMaxAccess(_H)
if mibBuilder.loadTexts:fsSysMemCapacity.setStatus(_A)
_FsSysDiskUsage_Type=Gauge32
_FsSysDiskUsage_Object=MibScalar
fsSysDiskUsage=_FsSysDiskUsage_Object((1,3,6,1,4,1,12356,106,4,1,5),_FsSysDiskUsage_Type())
fsSysDiskUsage.setMaxAccess(_H)
if mibBuilder.loadTexts:fsSysDiskUsage.setStatus(_A)
_FsSysDiskCapacity_Type=Gauge32
_FsSysDiskCapacity_Object=MibScalar
fsSysDiskCapacity=_FsSysDiskCapacity_Object((1,3,6,1,4,1,12356,106,4,1,6),_FsSysDiskCapacity_Type())
fsSysDiskCapacity.setMaxAccess(_H)
if mibBuilder.loadTexts:fsSysDiskCapacity.setStatus(_A)
_FsModel_ObjectIdentity=ObjectIdentity
fsModel=_FsModel_ObjectIdentity((1,3,6,1,4,1,12356,106,5))
_Fs108d_ObjectIdentity=ObjectIdentity
fs108d=_Fs108d_ObjectIdentity((1,3,6,1,4,1,12356,106,5,1081))
_S108en_ObjectIdentity=ObjectIdentity
s108en=_S108en_ObjectIdentity((1,3,6,1,4,1,12356,106,5,1082))
_S108ep_ObjectIdentity=ObjectIdentity
s108ep=_S108ep_ObjectIdentity((1,3,6,1,4,1,12356,106,5,1083))
_S108ef_ObjectIdentity=ObjectIdentity
s108ef=_S108ef_ObjectIdentity((1,3,6,1,4,1,12356,106,5,1084))
_S108dv_ObjectIdentity=ObjectIdentity
s108dv=_S108dv_ObjectIdentity((1,3,6,1,4,1,12356,106,5,1085))
_S108fn_ObjectIdentity=ObjectIdentity
s108fn=_S108fn_ObjectIdentity((1,3,6,1,4,1,12356,106,5,1086))
_S108fp_ObjectIdentity=ObjectIdentity
s108fp=_S108fp_ObjectIdentity((1,3,6,1,4,1,12356,106,5,1087))
_S108ff_ObjectIdentity=ObjectIdentity
s108ff=_S108ff_ObjectIdentity((1,3,6,1,4,1,12356,106,5,1088))
_Sr12dp_ObjectIdentity=ObjectIdentity
sr12dp=_Sr12dp_ObjectIdentity((1,3,6,1,4,1,12356,106,5,1121))
_S124dn_ObjectIdentity=ObjectIdentity
s124dn=_S124dn_ObjectIdentity((1,3,6,1,4,1,12356,106,5,1241))
_S124dp_ObjectIdentity=ObjectIdentity
s124dp=_S124dp_ObjectIdentity((1,3,6,1,4,1,12356,106,5,1242))
_Sr24dn_ObjectIdentity=ObjectIdentity
sr24dn=_Sr24dn_ObjectIdentity((1,3,6,1,4,1,12356,106,5,1243))
_S124en_ObjectIdentity=ObjectIdentity
s124en=_S124en_ObjectIdentity((1,3,6,1,4,1,12356,106,5,1244))
_S124ep_ObjectIdentity=ObjectIdentity
s124ep=_S124ep_ObjectIdentity((1,3,6,1,4,1,12356,106,5,1245))
_S124ef_ObjectIdentity=ObjectIdentity
s124ef=_S124ef_ObjectIdentity((1,3,6,1,4,1,12356,106,5,1246))
_S148en_ObjectIdentity=ObjectIdentity
s148en=_S148en_ObjectIdentity((1,3,6,1,4,1,12356,106,5,1247))
_S148ep_ObjectIdentity=ObjectIdentity
s148ep=_S148ep_ObjectIdentity((1,3,6,1,4,1,12356,106,5,1248))
_S124ff_ObjectIdentity=ObjectIdentity
s124ff=_S124ff_ObjectIdentity((1,3,6,1,4,1,12356,106,5,1249))
_S148fn_ObjectIdentity=ObjectIdentity
s148fn=_S148fn_ObjectIdentity((1,3,6,1,4,1,12356,106,5,1484))
_S148fp_ObjectIdentity=ObjectIdentity
s148fp=_S148fp_ObjectIdentity((1,3,6,1,4,1,12356,106,5,1485))
_S148ff_ObjectIdentity=ObjectIdentity
s148ff=_S148ff_ObjectIdentity((1,3,6,1,4,1,12356,106,5,1486))
_Fs224d_ObjectIdentity=ObjectIdentity
fs224d=_Fs224d_ObjectIdentity((1,3,6,1,4,1,12356,106,5,2241))
_S224df_ObjectIdentity=ObjectIdentity
s224df=_S224df_ObjectIdentity((1,3,6,1,4,1,12356,106,5,2242))
_S224en_ObjectIdentity=ObjectIdentity
s224en=_S224en_ObjectIdentity((1,3,6,1,4,1,12356,106,5,2243))
_S224ep_ObjectIdentity=ObjectIdentity
s224ep=_S224ep_ObjectIdentity((1,3,6,1,4,1,12356,106,5,2244))
_S248dp_ObjectIdentity=ObjectIdentity
s248dp=_S248dp_ObjectIdentity((1,3,6,1,4,1,12356,106,5,2481))
_S248df_ObjectIdentity=ObjectIdentity
s248df=_S248df_ObjectIdentity((1,3,6,1,4,1,12356,106,5,2482))
_S248dn_ObjectIdentity=ObjectIdentity
s248dn=_S248dn_ObjectIdentity((1,3,6,1,4,1,12356,106,5,2483))
_S248ef_ObjectIdentity=ObjectIdentity
s248ef=_S248ef_ObjectIdentity((1,3,6,1,4,1,12356,106,5,2484))
_S248ep_ObjectIdentity=ObjectIdentity
s248ep=_S248ep_ObjectIdentity((1,3,6,1,4,1,12356,106,5,2485))
_S424dn_ObjectIdentity=ObjectIdentity
s424dn=_S424dn_ObjectIdentity((1,3,6,1,4,1,12356,106,5,4241))
_S424dp_ObjectIdentity=ObjectIdentity
s424dp=_S424dp_ObjectIdentity((1,3,6,1,4,1,12356,106,5,4242))
_S424df_ObjectIdentity=ObjectIdentity
s424df=_S424df_ObjectIdentity((1,3,6,1,4,1,12356,106,5,4243))
_S448dn_ObjectIdentity=ObjectIdentity
s448dn=_S448dn_ObjectIdentity((1,3,6,1,4,1,12356,106,5,4482))
_S448df_ObjectIdentity=ObjectIdentity
s448df=_S448df_ObjectIdentity((1,3,6,1,4,1,12356,106,5,4483))
_S448dp_ObjectIdentity=ObjectIdentity
s448dp=_S448dp_ObjectIdentity((1,3,6,1,4,1,12356,106,5,4484))
_S448en_ObjectIdentity=ObjectIdentity
s448en=_S448en_ObjectIdentity((1,3,6,1,4,1,12356,106,5,4485))
_S448ep_ObjectIdentity=ObjectIdentity
s448ep=_S448ep_ObjectIdentity((1,3,6,1,4,1,12356,106,5,4486))
_S448ef_ObjectIdentity=ObjectIdentity
s448ef=_S448ef_ObjectIdentity((1,3,6,1,4,1,12356,106,5,4487))
_S524df_ObjectIdentity=ObjectIdentity
s524df=_S524df_ObjectIdentity((1,3,6,1,4,1,12356,106,5,5241))
_S524dn_ObjectIdentity=ObjectIdentity
s524dn=_S524dn_ObjectIdentity((1,3,6,1,4,1,12356,106,5,5242))
_S548df_ObjectIdentity=ObjectIdentity
s548df=_S548df_ObjectIdentity((1,3,6,1,4,1,12356,106,5,5481))
_S548dn_ObjectIdentity=ObjectIdentity
s548dn=_S548dn_ObjectIdentity((1,3,6,1,4,1,12356,106,5,5482))
_Fs1d24_ObjectIdentity=ObjectIdentity
fs1d24=_Fs1d24_ObjectIdentity((1,3,6,1,4,1,12356,106,5,10241))
_Fs1e24_ObjectIdentity=ObjectIdentity
fs1e24=_Fs1e24_ObjectIdentity((1,3,6,1,4,1,12356,106,5,10242))
_St1e24_ObjectIdentity=ObjectIdentity
st1e24=_St1e24_ObjectIdentity((1,3,6,1,4,1,12356,106,5,10243))
_Fs1d48_ObjectIdentity=ObjectIdentity
fs1d48=_Fs1d48_ObjectIdentity((1,3,6,1,4,1,12356,106,5,10481))
_Fs1e48_ObjectIdentity=ObjectIdentity
fs1e48=_Fs1e48_ObjectIdentity((1,3,6,1,4,1,12356,106,5,10482))
_S124fn_ObjectIdentity=ObjectIdentity
s124fn=_S124fn_ObjectIdentity((1,3,6,1,4,1,12356,106,5,12410))
_S124fp_ObjectIdentity=ObjectIdentity
s124fp=_S124fp_ObjectIdentity((1,3,6,1,4,1,12356,106,5,12411))
_Fs3d32_ObjectIdentity=ObjectIdentity
fs3d32=_Fs3d32_ObjectIdentity((1,3,6,1,4,1,12356,106,5,30321))
_Fs3e32_ObjectIdentity=ObjectIdentity
fs3e32=_Fs3e32_ObjectIdentity((1,3,6,1,4,1,12356,106,5,30322))
_S424en_ObjectIdentity=ObjectIdentity
s424en=_S424en_ObjectIdentity((1,3,6,1,4,1,12356,106,5,42401))
_S424ep_ObjectIdentity=ObjectIdentity
s424ep=_S424ep_ObjectIdentity((1,3,6,1,4,1,12356,106,5,42402))
_S424ef_ObjectIdentity=ObjectIdentity
s424ef=_S424ef_ObjectIdentity((1,3,6,1,4,1,12356,106,5,42403))
_S424ei_ObjectIdentity=ObjectIdentity
s424ei=_S424ei_ObjectIdentity((1,3,6,1,4,1,12356,106,5,42404))
_S426ef_ObjectIdentity=ObjectIdentity
s426ef=_S426ef_ObjectIdentity((1,3,6,1,4,1,12356,106,5,42405))
_FsMibConformance_ObjectIdentity=ObjectIdentity
fsMibConformance=_FsMibConformance_ObjectIdentity((1,3,6,1,4,1,12356,106,100))
fsSystemObjectGroup=ObjectGroup((1,3,6,1,4,1,12356,106,100,2))
fsSystemObjectGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:fsSystemObjectGroup.setStatus(_A)
fsTrunkObjectGroup=ObjectGroup((1,3,6,1,4,1,12356,106,100,3))
fsTrunkObjectGroup.setObjects((_B,_J))
if mibBuilder.loadTexts:fsTrunkObjectGroup.setStatus(_A)
fsTrapMemberDown=NotificationType((1,3,6,1,4,1,12356,106,2,0,703))
fsTrapMemberDown.setObjects(*((_D,_E),(_F,_G),(_B,_J)))
if mibBuilder.loadTexts:fsTrapMemberDown.setStatus(_A)
fsTrapMemberUp=NotificationType((1,3,6,1,4,1,12356,106,2,0,704))
fsTrapMemberUp.setObjects(*((_D,_E),(_F,_G),(_B,_J)))
if mibBuilder.loadTexts:fsTrapMemberUp.setStatus(_A)
fsTrapLlvViolation=NotificationType((1,3,6,1,4,1,12356,106,2,0,705))
fsTrapLlvViolation.setObjects(*((_D,_E),(_F,_G),(_B,_a)))
if mibBuilder.loadTexts:fsTrapLlvViolation.setStatus(_A)
fsTrapLearningEvent=NotificationType((1,3,6,1,4,1,12356,106,2,0,706))
fsTrapLearningEvent.setObjects(*((_D,_E),(_F,_G),(_K,_R),(_B,_b),(_K,_S),(_B,_c)))
if mibBuilder.loadTexts:fsTrapLearningEvent.setStatus(_A)
fsTrapSensorFault=NotificationType((1,3,6,1,4,1,12356,106,2,0,707))
fsTrapSensorFault.setObjects(*((_D,_E),(_F,_G),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:fsTrapSensorFault.setStatus(_A)
fsTrapSensorAlarm=NotificationType((1,3,6,1,4,1,12356,106,2,0,708))
fsTrapSensorAlarm.setObjects(*((_D,_E),(_F,_G),(_B,_O),(_B,_P),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:fsTrapSensorAlarm.setStatus(_A)
fsTrapFanDetect=NotificationType((1,3,6,1,4,1,12356,106,2,0,709))
fsTrapFanDetect.setObjects(*((_D,_E),(_F,_G),(_B,_Q),(_B,_g)))
if mibBuilder.loadTexts:fsTrapFanDetect.setStatus(_A)
fsTrapPsuStatus=NotificationType((1,3,6,1,4,1,12356,106,2,0,710))
fsTrapPsuStatus.setObjects(*((_D,_E),(_F,_G),(_B,_Q),(_B,_h)))
if mibBuilder.loadTexts:fsTrapPsuStatus.setStatus(_A)
fsTrapIpConflict=NotificationType((1,3,6,1,4,1,12356,106,2,0,801))
fsTrapIpConflict.setObjects(*((_D,_E),(_F,_G),(_B,_i),(_B,'ifname')))
if mibBuilder.loadTexts:fsTrapIpConflict.setStatus(_A)
fsTrapTrunkMemberHBOutOfSync=NotificationType((1,3,6,1,4,1,12356,106,2,0,802))
fsTrapTrunkMemberHBOutOfSync.setObjects(*((_D,_E),(_F,_G),(_L,_M),(_L,_M)))
if mibBuilder.loadTexts:fsTrapTrunkMemberHBOutOfSync.setStatus(_A)
fsNotificationGroup=NotificationGroup((1,3,6,1,4,1,12356,106,100,1))
fsNotificationGroup.setObjects(*((_B,_j),(_B,_k)))
if mibBuilder.loadTexts:fsNotificationGroup.setStatus(_A)
fsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,12356,106,100,100))
fsMIBCompliance.setObjects(*((_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:fsMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fnFortiSwitchMib':fnFortiSwitchMib,'fsCommon':fsCommon,'fsSys':fsSys,'fsSysSerial':fsSysSerial,'fsTraps':fsTraps,'fsTrapPrefix':fsTrapPrefix,_j:fsTrapMemberDown,_k:fsTrapMemberUp,'fsTrapLlvViolation':fsTrapLlvViolation,'fsTrapLearningEvent':fsTrapLearningEvent,'fsTrapSensorFault':fsTrapSensorFault,'fsTrapSensorAlarm':fsTrapSensorAlarm,'fsTrapFanDetect':fsTrapFanDetect,'fsTrapPsuStatus':fsTrapPsuStatus,'fsTrapIpConflict':fsTrapIpConflict,'fsTrapTrunkMemberHBOutOfSync':fsTrapTrunkMemberHBOutOfSync,'fsTrapObjects':fsTrapObjects,_a:fsLlvTrapMsg,_b:fsLearningTrapVid,_c:fsLearningTrapType,_O:fsSensorName,_P:fsSensorType,_Q:fsSensorIdx,_g:fsSensorFanEventType,_h:fsSensorPsuEventType,_d:fsAlarmEventType,_e:fsAlarmThresholdValue,_f:fsAlarmThresholdUnits,_i:fsIpAddress,'fsTrunkMemPrefix':fsTrunkMemPrefix,_J:fsTrunkMember,'fsSystem':fsSystem,'fsSystemInfo':fsSystemInfo,_U:fsSysVersion,_V:fsSysCpuUsage,_W:fsSysMemUsage,_X:fsSysMemCapacity,_Y:fsSysDiskUsage,_Z:fsSysDiskCapacity,'fsModel':fsModel,'fs108d':fs108d,'s108en':s108en,'s108ep':s108ep,'s108ef':s108ef,'s108dv':s108dv,'s108fn':s108fn,'s108fp':s108fp,'s108ff':s108ff,'sr12dp':sr12dp,'s124dn':s124dn,'s124dp':s124dp,'sr24dn':sr24dn,'s124en':s124en,'s124ep':s124ep,'s124ef':s124ef,'s148en':s148en,'s148ep':s148ep,'s124ff':s124ff,'s148fn':s148fn,'s148fp':s148fp,'s148ff':s148ff,'fs224d':fs224d,'s224df':s224df,'s224en':s224en,'s224ep':s224ep,'s248dp':s248dp,'s248df':s248df,'s248dn':s248dn,'s248ef':s248ef,'s248ep':s248ep,'s424dn':s424dn,'s424dp':s424dp,'s424df':s424df,'s448dn':s448dn,'s448df':s448df,'s448dp':s448dp,'s448en':s448en,'s448ep':s448ep,'s448ef':s448ef,'s524df':s524df,'s524dn':s524dn,'s548df':s548df,'s548dn':s548dn,'fs1d24':fs1d24,'fs1e24':fs1e24,'st1e24':st1e24,'fs1d48':fs1d48,'fs1e48':fs1e48,'s124fn':s124fn,'s124fp':s124fp,'fs3d32':fs3d32,'fs3e32':fs3e32,'s424en':s424en,'s424ep':s424ep,'s424ef':s424ef,'s424ei':s424ei,'s426ef':s426ef,'fsMibConformance':fsMibConformance,_l:fsNotificationGroup,_m:fsSystemObjectGroup,_n:fsTrunkObjectGroup,'fsMIBCompliance':fsMIBCompliance})