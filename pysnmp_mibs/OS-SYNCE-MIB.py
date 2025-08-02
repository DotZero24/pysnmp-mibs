_l='osSyncEMIBNotificationsGroup'
_k='osSyncEMibMandatoryGroup'
_j='osSyncEPtpAlarmUnLock'
_i='osSyncEPtpAlarmLock'
_h='osSyncEClockAlarmUnLock'
_g='osSyncEClockAlarmLock'
_f='osSyncEClockSourceJ1QL'
_e='osSyncEClockSourceT1QL'
_d='osSyncEClockSourceE1QL'
_c='osSyncEClockSourceEthPriority'
_b='osSyncEClockSourceEthPortNum'
_a='osSyncEFreeRunMode'
_Z='osSyncELineCode'
_Y='osSyncEFrequencyPtp'
_X='osSyncEFrequencyClkOut'
_W='osSyncEFrequencyClkIn'
_V='osSyncEDs1e1Connect'
_U='osSyncEDs1e1Type'
_T='osSyncET1CableType'
_S='osSyncEStatus'
_R='osSyncEMIBSupport'
_Q='osSyncEClockSourceEntryId'
_P='TruthValue'
_O='DisplayString'
_N='notDefined'
_M='dnu'
_L='frequency19440KHz'
_K='frequency6480KHz'
_J='frequency2048KHz'
_I='frequency1544KHz'
_H='osSyncEClockSourceEntryType'
_G='osSyncEEventDescription'
_F='read-only'
_E='notSet'
_D='read-write'
_C='Integer32'
_B='current'
_A='OS-SYNCE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
oaOptiSwitch,=mibBuilder.importSymbols('OS-COMMON-TC-MIB','oaOptiSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_O,'PhysAddress','TextualConvention',_P)
osSyncEMIB=ModuleIdentity((1,3,6,1,4,1,6926,2,23))
if mibBuilder.loadTexts:osSyncEMIB.setRevisions(('2012-08-15 00:00',))
_OsSyncEMIBNotifs_ObjectIdentity=ObjectIdentity
osSyncEMIBNotifs=_OsSyncEMIBNotifs_ObjectIdentity((1,3,6,1,4,1,6926,2,23,0))
_OsSyncEMIBObjects_ObjectIdentity=ObjectIdentity
osSyncEMIBObjects=_OsSyncEMIBObjects_ObjectIdentity((1,3,6,1,4,1,6926,2,23,1))
_OsSyncEMIBInfo_ObjectIdentity=ObjectIdentity
osSyncEMIBInfo=_OsSyncEMIBInfo_ObjectIdentity((1,3,6,1,4,1,6926,2,23,1,1))
_OsSyncEMIBEventParams_ObjectIdentity=ObjectIdentity
osSyncEMIBEventParams=_OsSyncEMIBEventParams_ObjectIdentity((1,3,6,1,4,1,6926,2,23,1,1,1))
class _OsSyncEEventDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,120))
_OsSyncEEventDescription_Type.__name__=_O
_OsSyncEEventDescription_Object=MibScalar
osSyncEEventDescription=_OsSyncEEventDescription_Object((1,3,6,1,4,1,6926,2,23,1,1,1,1),_OsSyncEEventDescription_Type())
osSyncEEventDescription.setMaxAccess(_F)
if mibBuilder.loadTexts:osSyncEEventDescription.setStatus(_B)
_OsSyncEMIBCfg_ObjectIdentity=ObjectIdentity
osSyncEMIBCfg=_OsSyncEMIBCfg_ObjectIdentity((1,3,6,1,4,1,6926,2,23,1,2))
_OsSyncEMIBCapabilities_ObjectIdentity=ObjectIdentity
osSyncEMIBCapabilities=_OsSyncEMIBCapabilities_ObjectIdentity((1,3,6,1,4,1,6926,2,23,1,2,1))
class _OsSyncEMIBSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notSupported',1),('supported',2)))
_OsSyncEMIBSupport_Type.__name__=_C
_OsSyncEMIBSupport_Object=MibScalar
osSyncEMIBSupport=_OsSyncEMIBSupport_Object((1,3,6,1,4,1,6926,2,23,1,2,1,1),_OsSyncEMIBSupport_Type())
osSyncEMIBSupport.setMaxAccess(_F)
if mibBuilder.loadTexts:osSyncEMIBSupport.setStatus(_B)
_OsSyncEMIBCfgGen_ObjectIdentity=ObjectIdentity
osSyncEMIBCfgGen=_OsSyncEMIBCfgGen_ObjectIdentity((1,3,6,1,4,1,6926,2,23,1,2,2))
class _OsSyncEStatus_Type(TruthValue):defaultValue=2
_OsSyncEStatus_Type.__name__=_P
_OsSyncEStatus_Object=MibScalar
osSyncEStatus=_OsSyncEStatus_Object((1,3,6,1,4,1,6926,2,23,1,2,2,1),_OsSyncEStatus_Type())
osSyncEStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:osSyncEStatus.setStatus(_B)
class _OsSyncET1CableType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('lengthNotApplicable',0),('length0To133',1),('length134To266',2),('length267To399',3),('length400To533',4),('length534To655',5),('lboNeg7p5dB',6),('lboNeg15p0dB',7),('lboNeg22p5dB',8)))
_OsSyncET1CableType_Type.__name__=_C
_OsSyncET1CableType_Object=MibScalar
osSyncET1CableType=_OsSyncET1CableType_Object((1,3,6,1,4,1,6926,2,23,1,2,2,2),_OsSyncET1CableType_Type())
osSyncET1CableType.setMaxAccess(_D)
if mibBuilder.loadTexts:osSyncET1CableType.setStatus(_B)
class _OsSyncEDs1e1Type_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_E,0),('square1544',1),('square2048',2),('typeE1',3),('typeJ1',4),('typeT1',5)))
_OsSyncEDs1e1Type_Type.__name__=_C
_OsSyncEDs1e1Type_Object=MibScalar
osSyncEDs1e1Type=_OsSyncEDs1e1Type_Object((1,3,6,1,4,1,6926,2,23,1,2,2,3),_OsSyncEDs1e1Type_Type())
osSyncEDs1e1Type.setMaxAccess(_D)
if mibBuilder.loadTexts:osSyncEDs1e1Type.setStatus(_B)
class _OsSyncEDs1e1Connect_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),('sec',1),('ssu',2)))
_OsSyncEDs1e1Connect_Type.__name__=_C
_OsSyncEDs1e1Connect_Object=MibScalar
osSyncEDs1e1Connect=_OsSyncEDs1e1Connect_Object((1,3,6,1,4,1,6926,2,23,1,2,2,4),_OsSyncEDs1e1Connect_Type())
osSyncEDs1e1Connect.setMaxAccess(_D)
if mibBuilder.loadTexts:osSyncEDs1e1Connect.setStatus(_B)
class _OsSyncEFrequencyClkIn_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,4,5,6,7)));namedValues=NamedValues(*((_E,0),(_I,4),(_J,5),(_K,6),(_L,7)))
_OsSyncEFrequencyClkIn_Type.__name__=_C
_OsSyncEFrequencyClkIn_Object=MibScalar
osSyncEFrequencyClkIn=_OsSyncEFrequencyClkIn_Object((1,3,6,1,4,1,6926,2,23,1,2,2,5),_OsSyncEFrequencyClkIn_Type())
osSyncEFrequencyClkIn.setMaxAccess(_D)
if mibBuilder.loadTexts:osSyncEFrequencyClkIn.setStatus(_B)
class _OsSyncEFrequencyClkOut_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_E,0),('frequency2KHz',1),('frequency4KHz',2),('frequency8KHz',3),(_I,4),(_J,5),(_K,6),(_L,7),('ptp',8)))
_OsSyncEFrequencyClkOut_Type.__name__=_C
_OsSyncEFrequencyClkOut_Object=MibScalar
osSyncEFrequencyClkOut=_OsSyncEFrequencyClkOut_Object((1,3,6,1,4,1,6926,2,23,1,2,2,6),_OsSyncEFrequencyClkOut_Type())
osSyncEFrequencyClkOut.setMaxAccess(_D)
if mibBuilder.loadTexts:osSyncEFrequencyClkOut.setStatus(_B)
class _OsSyncEFrequencyPtp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_E,0),(_I,1),(_J,2),(_K,3),(_L,4)))
_OsSyncEFrequencyPtp_Type.__name__=_C
_OsSyncEFrequencyPtp_Object=MibScalar
osSyncEFrequencyPtp=_OsSyncEFrequencyPtp_Object((1,3,6,1,4,1,6926,2,23,1,2,2,7),_OsSyncEFrequencyPtp_Type())
osSyncEFrequencyPtp.setMaxAccess(_D)
if mibBuilder.loadTexts:osSyncEFrequencyPtp.setStatus(_B)
class _OsSyncELineCode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_E,0),('ami',1),('hdb3',2),('b8zs',3)))
_OsSyncELineCode_Type.__name__=_C
_OsSyncELineCode_Object=MibScalar
osSyncELineCode=_OsSyncELineCode_Object((1,3,6,1,4,1,6926,2,23,1,2,2,8),_OsSyncELineCode_Type())
osSyncELineCode.setMaxAccess(_D)
if mibBuilder.loadTexts:osSyncELineCode.setStatus(_B)
class _OsSyncEFreeRunMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),('eec',2)))
_OsSyncEFreeRunMode_Type.__name__=_C
_OsSyncEFreeRunMode_Object=MibScalar
osSyncEFreeRunMode=_OsSyncEFreeRunMode_Object((1,3,6,1,4,1,6926,2,23,1,2,2,9),_OsSyncEFreeRunMode_Type())
osSyncEFreeRunMode.setMaxAccess(_D)
if mibBuilder.loadTexts:osSyncEFreeRunMode.setStatus(_B)
_OsSyncEClockSourceTable_Object=MibTable
osSyncEClockSourceTable=_OsSyncEClockSourceTable_Object((1,3,6,1,4,1,6926,2,23,1,2,3))
if mibBuilder.loadTexts:osSyncEClockSourceTable.setStatus(_B)
_OsSyncEClockSourceEntry_Object=MibTableRow
osSyncEClockSourceEntry=_OsSyncEClockSourceEntry_Object((1,3,6,1,4,1,6926,2,23,1,2,3,1))
osSyncEClockSourceEntry.setIndexNames((0,_A,_Q))
if mibBuilder.loadTexts:osSyncEClockSourceEntry.setStatus(_B)
class _OsSyncEClockSourceEntryId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_OsSyncEClockSourceEntryId_Type.__name__=_C
_OsSyncEClockSourceEntryId_Object=MibTableColumn
osSyncEClockSourceEntryId=_OsSyncEClockSourceEntryId_Object((1,3,6,1,4,1,6926,2,23,1,2,3,1,1),_OsSyncEClockSourceEntryId_Type())
osSyncEClockSourceEntryId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:osSyncEClockSourceEntryId.setStatus(_B)
class _OsSyncEClockSourceEntryType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('clkIn',1),('ds1e1',2),('ptp',3),('ethPort',4)))
_OsSyncEClockSourceEntryType_Type.__name__=_C
_OsSyncEClockSourceEntryType_Object=MibTableColumn
osSyncEClockSourceEntryType=_OsSyncEClockSourceEntryType_Object((1,3,6,1,4,1,6926,2,23,1,2,3,1,2),_OsSyncEClockSourceEntryType_Type())
osSyncEClockSourceEntryType.setMaxAccess(_F)
if mibBuilder.loadTexts:osSyncEClockSourceEntryType.setStatus(_B)
class _OsSyncEClockSourceEthPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OsSyncEClockSourceEthPortNum_Type.__name__=_C
_OsSyncEClockSourceEthPortNum_Object=MibTableColumn
osSyncEClockSourceEthPortNum=_OsSyncEClockSourceEthPortNum_Object((1,3,6,1,4,1,6926,2,23,1,2,3,1,3),_OsSyncEClockSourceEthPortNum_Type())
osSyncEClockSourceEthPortNum.setMaxAccess(_F)
if mibBuilder.loadTexts:osSyncEClockSourceEthPortNum.setStatus(_B)
class _OsSyncEClockSourceEthPriority_Type(Integer32):defaultValue=127;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_OsSyncEClockSourceEthPriority_Type.__name__=_C
_OsSyncEClockSourceEthPriority_Object=MibTableColumn
osSyncEClockSourceEthPriority=_OsSyncEClockSourceEthPriority_Object((1,3,6,1,4,1,6926,2,23,1,2,3,1,4),_OsSyncEClockSourceEthPriority_Type())
osSyncEClockSourceEthPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:osSyncEClockSourceEthPriority.setStatus(_B)
class _OsSyncEClockSourceE1QL_Type(Integer32):defaultValue=127;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,4,8,11,15,127)));namedValues=NamedValues(*(('prc',2),('ssuA',4),('ssuB',8),('eec1',11),(_M,15),(_N,127)))
_OsSyncEClockSourceE1QL_Type.__name__=_C
_OsSyncEClockSourceE1QL_Object=MibTableColumn
osSyncEClockSourceE1QL=_OsSyncEClockSourceE1QL_Object((1,3,6,1,4,1,6926,2,23,1,2,3,1,5),_OsSyncEClockSourceE1QL_Type())
osSyncEClockSourceE1QL.setMaxAccess(_D)
if mibBuilder.loadTexts:osSyncEClockSourceE1QL.setStatus(_B)
class _OsSyncEClockSourceT1QL_Type(Integer32):defaultValue=127;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,4,7,10,13,14,15,127)));namedValues=NamedValues(*(('stu',0),('prs',1),('tnc',4),('st2',7),('st3',10),('st3e',13),('prov',14),(_M,15),(_N,127)))
_OsSyncEClockSourceT1QL_Type.__name__=_C
_OsSyncEClockSourceT1QL_Object=MibTableColumn
osSyncEClockSourceT1QL=_OsSyncEClockSourceT1QL_Object((1,3,6,1,4,1,6926,2,23,1,2,3,1,6),_OsSyncEClockSourceT1QL_Type())
osSyncEClockSourceT1QL.setMaxAccess(_D)
if mibBuilder.loadTexts:osSyncEClockSourceT1QL.setStatus(_B)
class _OsSyncEClockSourceJ1QL_Type(Integer32):defaultValue=127;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,11,127)));namedValues=NamedValues(*(('unk',0),('eec1',11),(_N,127)))
_OsSyncEClockSourceJ1QL_Type.__name__=_C
_OsSyncEClockSourceJ1QL_Object=MibTableColumn
osSyncEClockSourceJ1QL=_OsSyncEClockSourceJ1QL_Object((1,3,6,1,4,1,6926,2,23,1,2,3,1,7),_OsSyncEClockSourceJ1QL_Type())
osSyncEClockSourceJ1QL.setMaxAccess(_D)
if mibBuilder.loadTexts:osSyncEClockSourceJ1QL.setStatus(_B)
_OsSyncEMIBConformance_ObjectIdentity=ObjectIdentity
osSyncEMIBConformance=_OsSyncEMIBConformance_ObjectIdentity((1,3,6,1,4,1,6926,2,23,101))
_OsSyncEMIBCompliances_ObjectIdentity=ObjectIdentity
osSyncEMIBCompliances=_OsSyncEMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6926,2,23,101,1))
_OsSyncEMIBGroups_ObjectIdentity=ObjectIdentity
osSyncEMIBGroups=_OsSyncEMIBGroups_ObjectIdentity((1,3,6,1,4,1,6926,2,23,101,2))
osSyncEMibMandatoryGroup=ObjectGroup((1,3,6,1,4,1,6926,2,23,101,2,1))
osSyncEMibMandatoryGroup.setObjects(*((_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_G),(_A,_H),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:osSyncEMibMandatoryGroup.setStatus(_B)
osSyncEClockAlarmLock=NotificationType((1,3,6,1,4,1,6926,2,23,0,1))
osSyncEClockAlarmLock.setObjects((_A,_H))
if mibBuilder.loadTexts:osSyncEClockAlarmLock.setStatus(_B)
osSyncEClockAlarmUnLock=NotificationType((1,3,6,1,4,1,6926,2,23,0,2))
osSyncEClockAlarmUnLock.setObjects((_A,_H))
if mibBuilder.loadTexts:osSyncEClockAlarmUnLock.setStatus(_B)
osSyncEPtpAlarmLock=NotificationType((1,3,6,1,4,1,6926,2,23,0,3))
osSyncEPtpAlarmLock.setObjects((_A,_G))
if mibBuilder.loadTexts:osSyncEPtpAlarmLock.setStatus(_B)
osSyncEPtpAlarmUnLock=NotificationType((1,3,6,1,4,1,6926,2,23,0,4))
osSyncEPtpAlarmUnLock.setObjects((_A,_G))
if mibBuilder.loadTexts:osSyncEPtpAlarmUnLock.setStatus(_B)
osSyncEMIBNotificationsGroup=NotificationGroup((1,3,6,1,4,1,6926,2,23,101,2,2))
osSyncEMIBNotificationsGroup.setObjects(*((_A,_g),(_A,_h),(_A,_i),(_A,_j)))
if mibBuilder.loadTexts:osSyncEMIBNotificationsGroup.setStatus(_B)
osSyncEMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6926,2,23,101,1,1))
osSyncEMIBCompliance.setObjects(*((_A,_k),(_A,_l)))
if mibBuilder.loadTexts:osSyncEMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'osSyncEMIB':osSyncEMIB,'osSyncEMIBNotifs':osSyncEMIBNotifs,_g:osSyncEClockAlarmLock,_h:osSyncEClockAlarmUnLock,_i:osSyncEPtpAlarmLock,_j:osSyncEPtpAlarmUnLock,'osSyncEMIBObjects':osSyncEMIBObjects,'osSyncEMIBInfo':osSyncEMIBInfo,'osSyncEMIBEventParams':osSyncEMIBEventParams,_G:osSyncEEventDescription,'osSyncEMIBCfg':osSyncEMIBCfg,'osSyncEMIBCapabilities':osSyncEMIBCapabilities,_R:osSyncEMIBSupport,'osSyncEMIBCfgGen':osSyncEMIBCfgGen,_S:osSyncEStatus,_T:osSyncET1CableType,_U:osSyncEDs1e1Type,_V:osSyncEDs1e1Connect,_W:osSyncEFrequencyClkIn,_X:osSyncEFrequencyClkOut,_Y:osSyncEFrequencyPtp,_Z:osSyncELineCode,_a:osSyncEFreeRunMode,'osSyncEClockSourceTable':osSyncEClockSourceTable,'osSyncEClockSourceEntry':osSyncEClockSourceEntry,_Q:osSyncEClockSourceEntryId,_H:osSyncEClockSourceEntryType,_b:osSyncEClockSourceEthPortNum,_c:osSyncEClockSourceEthPriority,_d:osSyncEClockSourceE1QL,_e:osSyncEClockSourceT1QL,_f:osSyncEClockSourceJ1QL,'osSyncEMIBConformance':osSyncEMIBConformance,'osSyncEMIBCompliances':osSyncEMIBCompliances,'osSyncEMIBCompliance':osSyncEMIBCompliance,'osSyncEMIBGroups':osSyncEMIBGroups,_k:osSyncEMibMandatoryGroup,_l:osSyncEMIBNotificationsGroup})