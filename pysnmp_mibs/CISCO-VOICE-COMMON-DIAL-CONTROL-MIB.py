_A5='cvCommonDcCallGroup1'
_A4='cvCommonDcCallGroup'
_A3='cvCommonDcCallHistoryCallerIDBlock'
_A2='cvCommonDcCallHistoryCallingName'
_A1='cvCommonDcCallActiveCallerIDBlock'
_A0='cvCommonDcCallActiveCallingName'
_z='deprecated'
_y='fax12000'
_x='fax14400'
_w='fax9600'
_v='fax7200'
_u='fax4800'
_t='fax2400'
_s='g722r6400'
_r='g722r5600'
_q='g722r4800'
_p='iLBCr13330'
_o='iLBCr15200'
_n='gsmAmrNb'
_m='g726r40000'
_l='clearChannel'
_k='gsmeEr12200'
_j='g723Ar5300'
_i='g723Ar6300'
_h='g729ABr8000'
_g='g729Br8000'
_f='gsmr13200'
_e='g723r5300'
_d='g723r6300'
_c='g728r16000'
_b='g711Alawr64000'
_a='g711ulawr64000'
_Z='g726r32000'
_Y='g726r24000'
_X='g726r16000'
_W='g729Ar8000'
_V='g729r8000'
_U='callActiveSetupTime'
_T='callActiveIndex'
_S='cCallHistoryIndex'
_R='CISCO-DIAL-CONTROL-MIB'
_Q='cvCommonDcCallHistoryInBandSignaling'
_P='cvCommonDcCallHistoryCodecBytes'
_O='cvCommonDcCallHistoryCoderTypeRate'
_N='cvCommonDcCallHistoryVADEnable'
_M='cvCommonDcCallHistoryConnectionId'
_L='cvCommonDcCallActiveInBandSignaling'
_K='cvCommonDcCallActiveCodecBytes'
_J='cvCommonDcCallActiveCoderTypeRate'
_I='cvCommonDcCallActiveVADEnable'
_H='cvCommonDcCallActiveConnectionId'
_G='Integer32'
_F='SnmpAdminString'
_E='DIAL-CONTROL-MIB'
_D='none'
_C='read-only'
_B='CISCO-VOICE-COMMON-DIAL-CONTROL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cCallHistoryIndex,=mibBuilder.importSymbols(_R,_S)
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
callActiveIndex,callActiveSetupTime=mibBuilder.importSymbols(_E,_T,_U)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoVoiceCommonDialControlMIB=ModuleIdentity((1,3,6,1,4,1,9,10,55))
if mibBuilder.loadTexts:ciscoVoiceCommonDialControlMIB.setRevisions(('2010-06-30 00:00','2009-03-18 00:00','2008-07-02 00:00','2007-06-26 00:00','2005-08-16 00:00','2005-03-06 00:00','2003-03-11 00:00','2001-10-06 00:00','2001-09-05 00:00','2000-07-22 00:00'))
class CvcSpeechCoderRate(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30)));namedValues=NamedValues(*((_V,1),(_W,2),(_X,3),(_Y,4),(_Z,5),(_a,6),(_b,7),(_c,8),(_d,9),(_e,10),(_f,11),(_g,12),(_h,13),(_i,14),(_j,15),('g729IETFr8000',16),(_k,17),(_l,18),(_m,19),('llcc',20),(_n,21),('iLBC',22),(_o,23),(_p,24),(_q,25),(_r,26),(_s,27),('iSAC',28),('aaclc',29),('aacld',30)))
class CvcFaxTransmitRate(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_D,1),('voiceRate',2),(_t,3),(_u,4),(_v,5),(_w,6),(_x,7),(_y,8)))
class CvcCoderTypeRate(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40)));namedValues=NamedValues(*(('other',1),(_t,2),(_u,3),(_v,4),(_w,5),(_x,6),(_y,7),(_V,10),(_W,11),(_X,12),(_Y,13),(_Z,14),(_a,15),(_b,16),(_c,17),(_d,18),(_e,19),(_f,20),(_g,21),(_h,22),(_i,23),(_j,24),('ietfg729r8000',25),(_k,26),(_l,27),(_m,28),('llcc',29),(_n,30),('g722',31),('iLBC',32),(_o,33),(_p,34),(_q,35),(_r,36),(_s,37),('iSAC',38),('aaclc',39),('aacld',40)))
class CvcGUid(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
class CvcInBandSignaling(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('cas',1),(_D,2),('cept',3),('transparent',4),('gr303',5)))
class CvcCallReferenceIdOrZero(TextualConvention,Unsigned32):status=_A
class CvcH320CallType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_D,0),('primary',1),('secondary',2)))
class CvcVideoCoderRate(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_D,0),('h261',1),('h263',2),('h263plus',3),('h264',4)))
_CvCommonDcMIBObjects_ObjectIdentity=ObjectIdentity
cvCommonDcMIBObjects=_CvCommonDcMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,55,1))
_CvCommonDcCallActive_ObjectIdentity=ObjectIdentity
cvCommonDcCallActive=_CvCommonDcCallActive_ObjectIdentity((1,3,6,1,4,1,9,10,55,1,1))
_CvCommonDcCallActiveTable_Object=MibTable
cvCommonDcCallActiveTable=_CvCommonDcCallActiveTable_Object((1,3,6,1,4,1,9,10,55,1,1,1))
if mibBuilder.loadTexts:cvCommonDcCallActiveTable.setStatus(_A)
_CvCommonDcCallActiveEntry_Object=MibTableRow
cvCommonDcCallActiveEntry=_CvCommonDcCallActiveEntry_Object((1,3,6,1,4,1,9,10,55,1,1,1,1))
cvCommonDcCallActiveEntry.setIndexNames((0,_E,_U),(0,_E,_T))
if mibBuilder.loadTexts:cvCommonDcCallActiveEntry.setStatus(_A)
_CvCommonDcCallActiveConnectionId_Type=CvcGUid
_CvCommonDcCallActiveConnectionId_Object=MibTableColumn
cvCommonDcCallActiveConnectionId=_CvCommonDcCallActiveConnectionId_Object((1,3,6,1,4,1,9,10,55,1,1,1,1,1),_CvCommonDcCallActiveConnectionId_Type())
cvCommonDcCallActiveConnectionId.setMaxAccess(_C)
if mibBuilder.loadTexts:cvCommonDcCallActiveConnectionId.setStatus(_A)
_CvCommonDcCallActiveVADEnable_Type=TruthValue
_CvCommonDcCallActiveVADEnable_Object=MibTableColumn
cvCommonDcCallActiveVADEnable=_CvCommonDcCallActiveVADEnable_Object((1,3,6,1,4,1,9,10,55,1,1,1,1,2),_CvCommonDcCallActiveVADEnable_Type())
cvCommonDcCallActiveVADEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cvCommonDcCallActiveVADEnable.setStatus(_A)
_CvCommonDcCallActiveCoderTypeRate_Type=CvcCoderTypeRate
_CvCommonDcCallActiveCoderTypeRate_Object=MibTableColumn
cvCommonDcCallActiveCoderTypeRate=_CvCommonDcCallActiveCoderTypeRate_Object((1,3,6,1,4,1,9,10,55,1,1,1,1,3),_CvCommonDcCallActiveCoderTypeRate_Type())
cvCommonDcCallActiveCoderTypeRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cvCommonDcCallActiveCoderTypeRate.setStatus(_A)
class _CvCommonDcCallActiveCodecBytes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,255))
_CvCommonDcCallActiveCodecBytes_Type.__name__=_G
_CvCommonDcCallActiveCodecBytes_Object=MibTableColumn
cvCommonDcCallActiveCodecBytes=_CvCommonDcCallActiveCodecBytes_Object((1,3,6,1,4,1,9,10,55,1,1,1,1,4),_CvCommonDcCallActiveCodecBytes_Type())
cvCommonDcCallActiveCodecBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cvCommonDcCallActiveCodecBytes.setStatus(_A)
_CvCommonDcCallActiveInBandSignaling_Type=CvcInBandSignaling
_CvCommonDcCallActiveInBandSignaling_Object=MibTableColumn
cvCommonDcCallActiveInBandSignaling=_CvCommonDcCallActiveInBandSignaling_Object((1,3,6,1,4,1,9,10,55,1,1,1,1,5),_CvCommonDcCallActiveInBandSignaling_Type())
cvCommonDcCallActiveInBandSignaling.setMaxAccess(_C)
if mibBuilder.loadTexts:cvCommonDcCallActiveInBandSignaling.setStatus(_A)
class _CvCommonDcCallActiveCallingName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CvCommonDcCallActiveCallingName_Type.__name__=_F
_CvCommonDcCallActiveCallingName_Object=MibTableColumn
cvCommonDcCallActiveCallingName=_CvCommonDcCallActiveCallingName_Object((1,3,6,1,4,1,9,10,55,1,1,1,1,6),_CvCommonDcCallActiveCallingName_Type())
cvCommonDcCallActiveCallingName.setMaxAccess(_C)
if mibBuilder.loadTexts:cvCommonDcCallActiveCallingName.setStatus(_A)
_CvCommonDcCallActiveCallerIDBlock_Type=TruthValue
_CvCommonDcCallActiveCallerIDBlock_Object=MibTableColumn
cvCommonDcCallActiveCallerIDBlock=_CvCommonDcCallActiveCallerIDBlock_Object((1,3,6,1,4,1,9,10,55,1,1,1,1,7),_CvCommonDcCallActiveCallerIDBlock_Type())
cvCommonDcCallActiveCallerIDBlock.setMaxAccess(_C)
if mibBuilder.loadTexts:cvCommonDcCallActiveCallerIDBlock.setStatus(_A)
_CvCommonDcCallHistory_ObjectIdentity=ObjectIdentity
cvCommonDcCallHistory=_CvCommonDcCallHistory_ObjectIdentity((1,3,6,1,4,1,9,10,55,1,2))
_CvCommonDcCallHistoryTable_Object=MibTable
cvCommonDcCallHistoryTable=_CvCommonDcCallHistoryTable_Object((1,3,6,1,4,1,9,10,55,1,2,1))
if mibBuilder.loadTexts:cvCommonDcCallHistoryTable.setStatus(_A)
_CvCommonDcCallHistoryEntry_Object=MibTableRow
cvCommonDcCallHistoryEntry=_CvCommonDcCallHistoryEntry_Object((1,3,6,1,4,1,9,10,55,1,2,1,1))
cvCommonDcCallHistoryEntry.setIndexNames((0,_R,_S))
if mibBuilder.loadTexts:cvCommonDcCallHistoryEntry.setStatus(_A)
_CvCommonDcCallHistoryConnectionId_Type=CvcGUid
_CvCommonDcCallHistoryConnectionId_Object=MibTableColumn
cvCommonDcCallHistoryConnectionId=_CvCommonDcCallHistoryConnectionId_Object((1,3,6,1,4,1,9,10,55,1,2,1,1,1),_CvCommonDcCallHistoryConnectionId_Type())
cvCommonDcCallHistoryConnectionId.setMaxAccess(_C)
if mibBuilder.loadTexts:cvCommonDcCallHistoryConnectionId.setStatus(_A)
_CvCommonDcCallHistoryVADEnable_Type=TruthValue
_CvCommonDcCallHistoryVADEnable_Object=MibTableColumn
cvCommonDcCallHistoryVADEnable=_CvCommonDcCallHistoryVADEnable_Object((1,3,6,1,4,1,9,10,55,1,2,1,1,2),_CvCommonDcCallHistoryVADEnable_Type())
cvCommonDcCallHistoryVADEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cvCommonDcCallHistoryVADEnable.setStatus(_A)
_CvCommonDcCallHistoryCoderTypeRate_Type=CvcCoderTypeRate
_CvCommonDcCallHistoryCoderTypeRate_Object=MibTableColumn
cvCommonDcCallHistoryCoderTypeRate=_CvCommonDcCallHistoryCoderTypeRate_Object((1,3,6,1,4,1,9,10,55,1,2,1,1,3),_CvCommonDcCallHistoryCoderTypeRate_Type())
cvCommonDcCallHistoryCoderTypeRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cvCommonDcCallHistoryCoderTypeRate.setStatus(_A)
class _CvCommonDcCallHistoryCodecBytes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,255))
_CvCommonDcCallHistoryCodecBytes_Type.__name__=_G
_CvCommonDcCallHistoryCodecBytes_Object=MibTableColumn
cvCommonDcCallHistoryCodecBytes=_CvCommonDcCallHistoryCodecBytes_Object((1,3,6,1,4,1,9,10,55,1,2,1,1,4),_CvCommonDcCallHistoryCodecBytes_Type())
cvCommonDcCallHistoryCodecBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cvCommonDcCallHistoryCodecBytes.setStatus(_A)
_CvCommonDcCallHistoryInBandSignaling_Type=CvcInBandSignaling
_CvCommonDcCallHistoryInBandSignaling_Object=MibTableColumn
cvCommonDcCallHistoryInBandSignaling=_CvCommonDcCallHistoryInBandSignaling_Object((1,3,6,1,4,1,9,10,55,1,2,1,1,5),_CvCommonDcCallHistoryInBandSignaling_Type())
cvCommonDcCallHistoryInBandSignaling.setMaxAccess(_C)
if mibBuilder.loadTexts:cvCommonDcCallHistoryInBandSignaling.setStatus(_A)
class _CvCommonDcCallHistoryCallingName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CvCommonDcCallHistoryCallingName_Type.__name__=_F
_CvCommonDcCallHistoryCallingName_Object=MibTableColumn
cvCommonDcCallHistoryCallingName=_CvCommonDcCallHistoryCallingName_Object((1,3,6,1,4,1,9,10,55,1,2,1,1,6),_CvCommonDcCallHistoryCallingName_Type())
cvCommonDcCallHistoryCallingName.setMaxAccess(_C)
if mibBuilder.loadTexts:cvCommonDcCallHistoryCallingName.setStatus(_A)
_CvCommonDcCallHistoryCallerIDBlock_Type=TruthValue
_CvCommonDcCallHistoryCallerIDBlock_Object=MibTableColumn
cvCommonDcCallHistoryCallerIDBlock=_CvCommonDcCallHistoryCallerIDBlock_Object((1,3,6,1,4,1,9,10,55,1,2,1,1,7),_CvCommonDcCallHistoryCallerIDBlock_Type())
cvCommonDcCallHistoryCallerIDBlock.setMaxAccess(_C)
if mibBuilder.loadTexts:cvCommonDcCallHistoryCallerIDBlock.setStatus(_A)
_CvCommonDcMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
cvCommonDcMIBNotificationPrefix=_CvCommonDcMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,10,55,2))
_CvCommonDcMIBNotifications_ObjectIdentity=ObjectIdentity
cvCommonDcMIBNotifications=_CvCommonDcMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,55,2,0))
_CvCommonDcMIBConformance_ObjectIdentity=ObjectIdentity
cvCommonDcMIBConformance=_CvCommonDcMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,55,3))
_CvCommonDcMIBCompliances_ObjectIdentity=ObjectIdentity
cvCommonDcMIBCompliances=_CvCommonDcMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,55,3,1))
_CvCommonDcMIBGroups_ObjectIdentity=ObjectIdentity
cvCommonDcMIBGroups=_CvCommonDcMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,55,3,2))
cvCommonDcCallGroup=ObjectGroup((1,3,6,1,4,1,9,10,55,3,2,1))
cvCommonDcCallGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:cvCommonDcCallGroup.setStatus(_z)
cvCommonDcCallGroup1=ObjectGroup((1,3,6,1,4,1,9,10,55,3,2,2))
cvCommonDcCallGroup1.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_A0),(_B,_A1),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_A2),(_B,_A3)))
if mibBuilder.loadTexts:cvCommonDcCallGroup1.setStatus(_A)
cvCommonDcMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,55,3,1,1))
cvCommonDcMIBCompliance.setObjects((_B,_A4))
if mibBuilder.loadTexts:cvCommonDcMIBCompliance.setStatus(_z)
cvCommonDcMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,10,55,3,1,2))
cvCommonDcMIBComplianceRev1.setObjects((_B,_A5))
if mibBuilder.loadTexts:cvCommonDcMIBComplianceRev1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CvcSpeechCoderRate':CvcSpeechCoderRate,'CvcFaxTransmitRate':CvcFaxTransmitRate,'CvcCoderTypeRate':CvcCoderTypeRate,'CvcGUid':CvcGUid,'CvcInBandSignaling':CvcInBandSignaling,'CvcCallReferenceIdOrZero':CvcCallReferenceIdOrZero,'CvcH320CallType':CvcH320CallType,'CvcVideoCoderRate':CvcVideoCoderRate,'ciscoVoiceCommonDialControlMIB':ciscoVoiceCommonDialControlMIB,'cvCommonDcMIBObjects':cvCommonDcMIBObjects,'cvCommonDcCallActive':cvCommonDcCallActive,'cvCommonDcCallActiveTable':cvCommonDcCallActiveTable,'cvCommonDcCallActiveEntry':cvCommonDcCallActiveEntry,_H:cvCommonDcCallActiveConnectionId,_I:cvCommonDcCallActiveVADEnable,_J:cvCommonDcCallActiveCoderTypeRate,_K:cvCommonDcCallActiveCodecBytes,_L:cvCommonDcCallActiveInBandSignaling,_A0:cvCommonDcCallActiveCallingName,_A1:cvCommonDcCallActiveCallerIDBlock,'cvCommonDcCallHistory':cvCommonDcCallHistory,'cvCommonDcCallHistoryTable':cvCommonDcCallHistoryTable,'cvCommonDcCallHistoryEntry':cvCommonDcCallHistoryEntry,_M:cvCommonDcCallHistoryConnectionId,_N:cvCommonDcCallHistoryVADEnable,_O:cvCommonDcCallHistoryCoderTypeRate,_P:cvCommonDcCallHistoryCodecBytes,_Q:cvCommonDcCallHistoryInBandSignaling,_A2:cvCommonDcCallHistoryCallingName,_A3:cvCommonDcCallHistoryCallerIDBlock,'cvCommonDcMIBNotificationPrefix':cvCommonDcMIBNotificationPrefix,'cvCommonDcMIBNotifications':cvCommonDcMIBNotifications,'cvCommonDcMIBConformance':cvCommonDcMIBConformance,'cvCommonDcMIBCompliances':cvCommonDcMIBCompliances,'cvCommonDcMIBCompliance':cvCommonDcMIBCompliance,'cvCommonDcMIBComplianceRev1':cvCommonDcMIBComplianceRev1,'cvCommonDcMIBGroups':cvCommonDcMIBGroups,_A4:cvCommonDcCallGroup,_A5:cvCommonDcCallGroup1})