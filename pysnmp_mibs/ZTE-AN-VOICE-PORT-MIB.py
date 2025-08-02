_h='gainNeg7dB'
_g='gainNeg6dB'
_f='gainNeg5dB'
_e='gainNeg4dB'
_d='gain0dB'
_c='zxAnPstnPortECharPort'
_b='zxAnPstnPortECharSlot'
_a='zxAnPstnPortECharShelf'
_Z='zxAnPstnPortECharRack'
_Y='00000000'
_X='curr45mA'
_W='curr35mA'
_V='curr30mA'
_U='curr20mA'
_T='curr16mA'
_S='curr40mA'
_R='curr32mA'
_Q='curr25mA'
_P='disable'
_O='enable'
_N='a200slcindex'
_M='a200slcslotno'
_L='a200slcshelfno'
_K='a200slcrackno'
_J='normal'
_I='DisplayString'
_H='IpAddress'
_G='read-only'
_F='not-accessible'
_E='ZTE-AN-VOICE-PORT-MIB'
_D='milli-seconds'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,_H,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_I,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
zxAnVoicePortMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,5200))
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_ZxAn_ObjectIdentity=ObjectIdentity
zxAn=_ZxAn_ObjectIdentity((1,3,6,1,4,1,3902,1015))
_ZxAnVoiceMgmt_ObjectIdentity=ObjectIdentity
zxAnVoiceMgmt=_ZxAnVoiceMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3))
_ZxAnVoicePortConfig_ObjectIdentity=ObjectIdentity
zxAnVoicePortConfig=_ZxAnVoicePortConfig_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,3))
_A200SlcTable_Object=MibTable
a200SlcTable=_A200SlcTable_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1))
if mibBuilder.loadTexts:a200SlcTable.setStatus(_A)
_A200SlcEntry_Object=MibTableRow
a200SlcEntry=_A200SlcEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1,1))
a200SlcEntry.setIndexNames((0,_E,_K),(0,_E,_L),(0,_E,_M),(0,_E,_N))
if mibBuilder.loadTexts:a200SlcEntry.setStatus(_A)
_A200slcrackno_Type=Integer32
_A200slcrackno_Object=MibTableColumn
a200slcrackno=_A200slcrackno_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1,1,1),_A200slcrackno_Type())
a200slcrackno.setMaxAccess(_F)
if mibBuilder.loadTexts:a200slcrackno.setStatus(_A)
_A200slcshelfno_Type=Integer32
_A200slcshelfno_Object=MibTableColumn
a200slcshelfno=_A200slcshelfno_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1,1,2),_A200slcshelfno_Type())
a200slcshelfno.setMaxAccess(_F)
if mibBuilder.loadTexts:a200slcshelfno.setStatus(_A)
_A200slcslotno_Type=Integer32
_A200slcslotno_Object=MibTableColumn
a200slcslotno=_A200slcslotno_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1,1,3),_A200slcslotno_Type())
a200slcslotno.setMaxAccess(_F)
if mibBuilder.loadTexts:a200slcslotno.setStatus(_A)
_A200slcindex_Type=Integer32
_A200slcindex_Object=MibTableColumn
a200slcindex=_A200slcindex_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1,1,4),_A200slcindex_Type())
a200slcindex.setMaxAccess(_F)
if mibBuilder.loadTexts:a200slcindex.setStatus(_A)
_A200slcpkg_Type=Integer32
_A200slcpkg_Object=MibTableColumn
a200slcpkg=_A200slcpkg_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1,1,5),_A200slcpkg_Type())
a200slcpkg.setMaxAccess(_B)
if mibBuilder.loadTexts:a200slcpkg.setStatus(_A)
_A200slcstatus_Type=Integer32
_A200slcstatus_Object=MibTableColumn
a200slcstatus=_A200slcstatus_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1,1,6),_A200slcstatus_Type())
a200slcstatus.setMaxAccess(_G)
if mibBuilder.loadTexts:a200slcstatus.setStatus(_A)
class _A200slcdftevent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_A200slcdftevent_Type.__name__=_C
_A200slcdftevent_Object=MibTableColumn
a200slcdftevent=_A200slcdftevent_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1,1,7),_A200slcdftevent_Type())
a200slcdftevent.setMaxAccess(_B)
if mibBuilder.loadTexts:a200slcdftevent.setStatus(_A)
class _A200slcusermode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('usermodeIdle',0),('usermodeH248',1),('usermodeZteUni',2),('usermodeV5',3),('usermodeZ',4),('usermodeMgcp',5),('usermodeZteSni',6),('usermodeV5Isdn',7),('usermodeV5Ddn',8),('usermodeSip',9)))
_A200slcusermode_Type.__name__=_C
_A200slcusermode_Object=MibTableColumn
a200slcusermode=_A200slcusermode_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1,1,8),_A200slcusermode_Type())
a200slcusermode.setMaxAccess(_G)
if mibBuilder.loadTexts:a200slcusermode.setStatus(_A)
class _A200slcFaxMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,13)));namedValues=NamedValues(*(('faxT30',0),('faxT38',1),('faxRTP',2),('faxFastModem',3),('faxFastFax',4),('noSwitch',5),('selfSwitch',6),('faxV34',13)))
_A200slcFaxMode_Type.__name__=_C
_A200slcFaxMode_Object=MibTableColumn
a200slcFaxMode=_A200slcFaxMode_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1,1,9),_A200slcFaxMode_Type())
a200slcFaxMode.setMaxAccess(_B)
if mibBuilder.loadTexts:a200slcFaxMode.setStatus(_A)
class _A200slcQovsId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_A200slcQovsId_Type.__name__=_C
_A200slcQovsId_Object=MibTableColumn
a200slcQovsId=_A200slcQovsId_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1,1,10),_A200slcQovsId_Type())
a200slcQovsId.setMaxAccess(_B)
if mibBuilder.loadTexts:a200slcQovsId.setStatus(_A)
class _A200slcCIDType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('dtmf',1),('fskBell202',2),('mf',3),('fskV23',4)))
_A200slcCIDType_Type.__name__=_C
_A200slcCIDType_Object=MibTableColumn
a200slcCIDType=_A200slcCIDType_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1,1,11),_A200slcCIDType_Type())
a200slcCIDType.setMaxAccess(_B)
if mibBuilder.loadTexts:a200slcCIDType.setStatus(_A)
class _A200slcImType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,3,4,5,6)));namedValues=NamedValues(*((_J,0),('bt3',3),('etsi',4),('bt5',5),('ohm600',6)))
_A200slcImType_Type.__name__=_C
_A200slcImType_Object=MibTableColumn
a200slcImType=_A200slcImType_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1,1,12),_A200slcImType_Type())
a200slcImType.setMaxAccess(_B)
if mibBuilder.loadTexts:a200slcImType.setStatus(_A)
class _A200slcecenable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('default',0),(_O,1),(_P,2)))
_A200slcecenable_Type.__name__=_C
_A200slcecenable_Object=MibTableColumn
a200slcecenable=_A200slcecenable_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1,1,14),_A200slcecenable_Type())
a200slcecenable.setMaxAccess(_B)
if mibBuilder.loadTexts:a200slcecenable.setStatus(_A)
class _A200slcuserclass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),('vip',1)))
_A200slcuserclass_Type.__name__=_C
_A200slcuserclass_Object=MibTableColumn
a200slcuserclass=_A200slcuserclass_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1,1,15),_A200slcuserclass_Type())
a200slcuserclass.setMaxAccess(_B)
if mibBuilder.loadTexts:a200slcuserclass.setStatus(_A)
class _A200slcPktToPcmGain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-20,20))
_A200slcPktToPcmGain_Type.__name__=_C
_A200slcPktToPcmGain_Object=MibTableColumn
a200slcPktToPcmGain=_A200slcPktToPcmGain_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1,1,16),_A200slcPktToPcmGain_Type())
a200slcPktToPcmGain.setMaxAccess(_B)
if mibBuilder.loadTexts:a200slcPktToPcmGain.setStatus(_A)
class _A200slcPcmToPktGain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-20,20))
_A200slcPcmToPktGain_Type.__name__=_C
_A200slcPcmToPktGain_Object=MibTableColumn
a200slcPcmToPktGain=_A200slcPcmToPktGain_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1,1,17),_A200slcPcmToPktGain_Type())
a200slcPcmToPktGain.setMaxAccess(_B)
if mibBuilder.loadTexts:a200slcPcmToPktGain.setStatus(_A)
class _A200slcphonenum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_A200slcphonenum_Type.__name__=_I
_A200slcphonenum_Object=MibTableColumn
a200slcphonenum=_A200slcphonenum_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1,1,18),_A200slcphonenum_Type())
a200slcphonenum.setMaxAccess(_B)
if mibBuilder.loadTexts:a200slcphonenum.setStatus(_A)
class _A200slcoperNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,192))
_A200slcoperNum_Type.__name__=_C
_A200slcoperNum_Object=MibTableColumn
a200slcoperNum=_A200slcoperNum_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1,1,19),_A200slcoperNum_Type())
a200slcoperNum.setMaxAccess(_B)
if mibBuilder.loadTexts:a200slcoperNum.setStatus(_A)
class _A200slcblockoper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_A200slcblockoper_Type.__name__=_C
_A200slcblockoper_Object=MibTableColumn
a200slcblockoper=_A200slcblockoper_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1,1,20),_A200slcblockoper_Type())
a200slcblockoper.setMaxAccess(_B)
if mibBuilder.loadTexts:a200slcblockoper.setStatus(_A)
class _A200slcunblockoper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_A200slcunblockoper_Type.__name__=_C
_A200slcunblockoper_Object=MibTableColumn
a200slcunblockoper=_A200slcunblockoper_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1,1,21),_A200slcunblockoper_Type())
a200slcunblockoper.setMaxAccess(_B)
if mibBuilder.loadTexts:a200slcunblockoper.setStatus(_A)
class _A200slcmonitorflag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_A200slcmonitorflag_Type.__name__=_C
_A200slcmonitorflag_Object=MibTableColumn
a200slcmonitorflag=_A200slcmonitorflag_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1,1,22),_A200slcmonitorflag_Type())
a200slcmonitorflag.setMaxAccess(_B)
if mibBuilder.loadTexts:a200slcmonitorflag.setStatus(_A)
class _A200slcmonitoreerack_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_A200slcmonitoreerack_Type.__name__=_C
_A200slcmonitoreerack_Object=MibTableColumn
a200slcmonitoreerack=_A200slcmonitoreerack_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1,1,23),_A200slcmonitoreerack_Type())
a200slcmonitoreerack.setMaxAccess(_B)
if mibBuilder.loadTexts:a200slcmonitoreerack.setStatus(_A)
class _A200slcmonitoreeshelf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_A200slcmonitoreeshelf_Type.__name__=_C
_A200slcmonitoreeshelf_Object=MibTableColumn
a200slcmonitoreeshelf=_A200slcmonitoreeshelf_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1,1,24),_A200slcmonitoreeshelf_Type())
a200slcmonitoreeshelf.setMaxAccess(_B)
if mibBuilder.loadTexts:a200slcmonitoreeshelf.setStatus(_A)
class _A200slcmonitoreeslot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,17))
_A200slcmonitoreeslot_Type.__name__=_C
_A200slcmonitoreeslot_Object=MibTableColumn
a200slcmonitoreeslot=_A200slcmonitoreeslot_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1,1,25),_A200slcmonitoreeslot_Type())
a200slcmonitoreeslot.setMaxAccess(_B)
if mibBuilder.loadTexts:a200slcmonitoreeslot.setStatus(_A)
class _A200slcmonitoreeindex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_A200slcmonitoreeindex_Type.__name__=_C
_A200slcmonitoreeindex_Object=MibTableColumn
a200slcmonitoreeindex=_A200slcmonitoreeindex_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1,1,26),_A200slcmonitoreeindex_Type())
a200slcmonitoreeindex.setMaxAccess(_B)
if mibBuilder.loadTexts:a200slcmonitoreeindex.setStatus(_A)
class _A200slcDialMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('dtmf',0),('pulse',1)))
_A200slcDialMode_Type.__name__=_C
_A200slcDialMode_Object=MibTableColumn
a200slcDialMode=_A200slcDialMode_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1,1,27),_A200slcDialMode_Type())
a200slcDialMode.setMaxAccess(_B)
if mibBuilder.loadTexts:a200slcDialMode.setStatus(_A)
class _A200slcFeedCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_Q,1),(_R,2),(_S,3),(_T,4),(_U,5),(_V,6),(_W,7),(_X,8),('curr50mA',9),('curr55mA',10)))
_A200slcFeedCurrent_Type.__name__=_C
_A200slcFeedCurrent_Object=MibTableColumn
a200slcFeedCurrent=_A200slcFeedCurrent_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1,1,28),_A200slcFeedCurrent_Type())
a200slcFeedCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:a200slcFeedCurrent.setStatus(_A)
if mibBuilder.loadTexts:a200slcFeedCurrent.setUnits('mA')
class _A200slcHighImpedanceOper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_A200slcHighImpedanceOper_Type.__name__=_C
_A200slcHighImpedanceOper_Object=MibTableColumn
a200slcHighImpedanceOper=_A200slcHighImpedanceOper_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1,1,29),_A200slcHighImpedanceOper_Type())
a200slcHighImpedanceOper.setMaxAccess(_B)
if mibBuilder.loadTexts:a200slcHighImpedanceOper.setStatus(_A)
class _A200slcNoneHighImpedanceOper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_A200slcNoneHighImpedanceOper_Type.__name__=_C
_A200slcNoneHighImpedanceOper_Object=MibTableColumn
a200slcNoneHighImpedanceOper=_A200slcNoneHighImpedanceOper_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1,1,30),_A200slcNoneHighImpedanceOper_Type())
a200slcNoneHighImpedanceOper.setMaxAccess(_B)
if mibBuilder.loadTexts:a200slcNoneHighImpedanceOper.setStatus(_A)
class _ZxAnSlcDelayDialMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noDelay',1),('delay',2)))
_ZxAnSlcDelayDialMode_Type.__name__=_C
_ZxAnSlcDelayDialMode_Object=MibTableColumn
zxAnSlcDelayDialMode=_ZxAnSlcDelayDialMode_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1,1,31),_ZxAnSlcDelayDialMode_Type())
zxAnSlcDelayDialMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSlcDelayDialMode.setStatus(_A)
class _ZxAnSlcDdiTrapEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_ZxAnSlcDdiTrapEnable_Type.__name__=_C
_ZxAnSlcDdiTrapEnable_Object=MibTableColumn
zxAnSlcDdiTrapEnable=_ZxAnSlcDdiTrapEnable_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1,1,32),_ZxAnSlcDdiTrapEnable_Type())
zxAnSlcDdiTrapEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSlcDdiTrapEnable.setStatus(_A)
class _ZxAnSlcSemiPerConnSrcIpAddr_Type(IpAddress):defaultHexValue=_Y
_ZxAnSlcSemiPerConnSrcIpAddr_Type.__name__=_H
_ZxAnSlcSemiPerConnSrcIpAddr_Object=MibTableColumn
zxAnSlcSemiPerConnSrcIpAddr=_ZxAnSlcSemiPerConnSrcIpAddr_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1,1,33),_ZxAnSlcSemiPerConnSrcIpAddr_Type())
zxAnSlcSemiPerConnSrcIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSlcSemiPerConnSrcIpAddr.setStatus(_A)
class _ZxAnSlcSemiPerConnSrcPort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(20480,21503))
_ZxAnSlcSemiPerConnSrcPort_Type.__name__=_C
_ZxAnSlcSemiPerConnSrcPort_Object=MibTableColumn
zxAnSlcSemiPerConnSrcPort=_ZxAnSlcSemiPerConnSrcPort_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1,1,34),_ZxAnSlcSemiPerConnSrcPort_Type())
zxAnSlcSemiPerConnSrcPort.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSlcSemiPerConnSrcPort.setStatus(_A)
class _ZxAnSlcSemiPerConnDstIpAddr_Type(IpAddress):defaultHexValue=_Y
_ZxAnSlcSemiPerConnDstIpAddr_Type.__name__=_H
_ZxAnSlcSemiPerConnDstIpAddr_Object=MibTableColumn
zxAnSlcSemiPerConnDstIpAddr=_ZxAnSlcSemiPerConnDstIpAddr_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1,1,35),_ZxAnSlcSemiPerConnDstIpAddr_Type())
zxAnSlcSemiPerConnDstIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSlcSemiPerConnDstIpAddr.setStatus(_A)
class _ZxAnSlcSemiPerConnDstPort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnSlcSemiPerConnDstPort_Type.__name__=_C
_ZxAnSlcSemiPerConnDstPort_Object=MibTableColumn
zxAnSlcSemiPerConnDstPort=_ZxAnSlcSemiPerConnDstPort_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1,1,36),_ZxAnSlcSemiPerConnDstPort_Type())
zxAnSlcSemiPerConnDstPort.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSlcSemiPerConnDstPort.setStatus(_A)
class _ZxAnSlcSemiPerConnSdpProfileId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_ZxAnSlcSemiPerConnSdpProfileId_Type.__name__=_C
_ZxAnSlcSemiPerConnSdpProfileId_Object=MibTableColumn
zxAnSlcSemiPerConnSdpProfileId=_ZxAnSlcSemiPerConnSdpProfileId_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1,1,37),_ZxAnSlcSemiPerConnSdpProfileId_Type())
zxAnSlcSemiPerConnSdpProfileId.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSlcSemiPerConnSdpProfileId.setStatus(_A)
class _ZxAnSlcSemiPerConnSdpInformation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ZxAnSlcSemiPerConnSdpInformation_Type.__name__=_I
_ZxAnSlcSemiPerConnSdpInformation_Object=MibTableColumn
zxAnSlcSemiPerConnSdpInformation=_ZxAnSlcSemiPerConnSdpInformation_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1,1,38),_ZxAnSlcSemiPerConnSdpInformation_Type())
zxAnSlcSemiPerConnSdpInformation.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnSlcSemiPerConnSdpInformation.setStatus(_A)
_ZxAnVoicePortGlobalObjects_ObjectIdentity=ObjectIdentity
zxAnVoicePortGlobalObjects=_ZxAnVoicePortGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,3,1400))
class _ZxAnVoicePortMgmtCapabilities_Type(Bits):namedValues=NamedValues(*(('nbPlatform',0),('delayDialMode',1)))
_ZxAnVoicePortMgmtCapabilities_Type.__name__='Bits'
_ZxAnVoicePortMgmtCapabilities_Object=MibScalar
zxAnVoicePortMgmtCapabilities=_ZxAnVoicePortMgmtCapabilities_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1400,1),_ZxAnVoicePortMgmtCapabilities_Type())
zxAnVoicePortMgmtCapabilities.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVoicePortMgmtCapabilities.setStatus(_A)
_ZxAnPstnPortECharGlobalObjects_ObjectIdentity=ObjectIdentity
zxAnPstnPortECharGlobalObjects=_ZxAnPstnPortECharGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,3,1400,51))
class _ZxAnPstnPortGlbPcmLaw_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('aLaw',1),('muLaw',2)))
_ZxAnPstnPortGlbPcmLaw_Type.__name__=_C
_ZxAnPstnPortGlbPcmLaw_Object=MibScalar
zxAnPstnPortGlbPcmLaw=_ZxAnPstnPortGlbPcmLaw_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1400,51,1),_ZxAnPstnPortGlbPcmLaw_Type())
zxAnPstnPortGlbPcmLaw.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPstnPortGlbPcmLaw.setStatus(_A)
class _ZxAnPstnPortGlbRingVoltage_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('volt50V',1),('volt75V',2),('volt90V',3)))
_ZxAnPstnPortGlbRingVoltage_Type.__name__=_C
_ZxAnPstnPortGlbRingVoltage_Object=MibScalar
zxAnPstnPortGlbRingVoltage=_ZxAnPstnPortGlbRingVoltage_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1400,51,2),_ZxAnPstnPortGlbRingVoltage_Type())
zxAnPstnPortGlbRingVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPstnPortGlbRingVoltage.setStatus(_A)
class _ZxAnPstnPortGlbRingFrequency_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('freq16Hz',1),('freq25Hz',2),('freq50Hz',3)))
_ZxAnPstnPortGlbRingFrequency_Type.__name__=_C
_ZxAnPstnPortGlbRingFrequency_Object=MibScalar
zxAnPstnPortGlbRingFrequency=_ZxAnPstnPortGlbRingFrequency_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1400,51,3),_ZxAnPstnPortGlbRingFrequency_Type())
zxAnPstnPortGlbRingFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPstnPortGlbRingFrequency.setStatus(_A)
class _ZxAnPstnPolarityRevPulseEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_ZxAnPstnPolarityRevPulseEnable_Type.__name__=_C
_ZxAnPstnPolarityRevPulseEnable_Object=MibScalar
zxAnPstnPolarityRevPulseEnable=_ZxAnPstnPolarityRevPulseEnable_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1400,51,4),_ZxAnPstnPolarityRevPulseEnable_Type())
zxAnPstnPolarityRevPulseEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPstnPolarityRevPulseEnable.setStatus(_A)
class _ZxAnPstnPolarityRevPulseWidth_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,1270))
_ZxAnPstnPolarityRevPulseWidth_Type.__name__=_C
_ZxAnPstnPolarityRevPulseWidth_Object=MibScalar
zxAnPstnPolarityRevPulseWidth=_ZxAnPstnPolarityRevPulseWidth_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1400,51,5),_ZxAnPstnPolarityRevPulseWidth_Type())
zxAnPstnPolarityRevPulseWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPstnPolarityRevPulseWidth.setStatus(_A)
if mibBuilder.loadTexts:zxAnPstnPolarityRevPulseWidth.setUnits(_D)
class _ZxAnPstnPolarityRevMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('hard',1),('soft',2)))
_ZxAnPstnPolarityRevMode_Type.__name__=_C
_ZxAnPstnPolarityRevMode_Object=MibScalar
zxAnPstnPolarityRevMode=_ZxAnPstnPolarityRevMode_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1400,51,6),_ZxAnPstnPolarityRevMode_Type())
zxAnPstnPolarityRevMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPstnPolarityRevMode.setStatus(_A)
class _ZxAnPstnMinDialPulseBreakTime_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,200))
_ZxAnPstnMinDialPulseBreakTime_Type.__name__=_C
_ZxAnPstnMinDialPulseBreakTime_Object=MibScalar
zxAnPstnMinDialPulseBreakTime=_ZxAnPstnMinDialPulseBreakTime_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1400,51,7),_ZxAnPstnMinDialPulseBreakTime_Type())
zxAnPstnMinDialPulseBreakTime.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPstnMinDialPulseBreakTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnPstnMinDialPulseBreakTime.setUnits(_D)
class _ZxAnPstnMaxDialPulseBreakTime_Type(Integer32):defaultValue=80;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,200))
_ZxAnPstnMaxDialPulseBreakTime_Type.__name__=_C
_ZxAnPstnMaxDialPulseBreakTime_Object=MibScalar
zxAnPstnMaxDialPulseBreakTime=_ZxAnPstnMaxDialPulseBreakTime_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1400,51,8),_ZxAnPstnMaxDialPulseBreakTime_Type())
zxAnPstnMaxDialPulseBreakTime.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPstnMaxDialPulseBreakTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnPstnMaxDialPulseBreakTime.setUnits(_D)
class _ZxAnPstnMinDialPulseMakeTime_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,200))
_ZxAnPstnMinDialPulseMakeTime_Type.__name__=_C
_ZxAnPstnMinDialPulseMakeTime_Object=MibScalar
zxAnPstnMinDialPulseMakeTime=_ZxAnPstnMinDialPulseMakeTime_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1400,51,9),_ZxAnPstnMinDialPulseMakeTime_Type())
zxAnPstnMinDialPulseMakeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPstnMinDialPulseMakeTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnPstnMinDialPulseMakeTime.setUnits(_D)
class _ZxAnPstnMaxDialPulseMakeTime_Type(Integer32):defaultValue=90;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,200))
_ZxAnPstnMaxDialPulseMakeTime_Type.__name__=_C
_ZxAnPstnMaxDialPulseMakeTime_Object=MibScalar
zxAnPstnMaxDialPulseMakeTime=_ZxAnPstnMaxDialPulseMakeTime_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1400,51,10),_ZxAnPstnMaxDialPulseMakeTime_Type())
zxAnPstnMaxDialPulseMakeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPstnMaxDialPulseMakeTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnPstnMaxDialPulseMakeTime.setUnits(_D)
class _ZxAnPstnMinDialPulseInterdigit_Type(Integer32):defaultValue=250;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,500))
_ZxAnPstnMinDialPulseInterdigit_Type.__name__=_C
_ZxAnPstnMinDialPulseInterdigit_Object=MibScalar
zxAnPstnMinDialPulseInterdigit=_ZxAnPstnMinDialPulseInterdigit_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1400,51,11),_ZxAnPstnMinDialPulseInterdigit_Type())
zxAnPstnMinDialPulseInterdigit.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPstnMinDialPulseInterdigit.setStatus(_A)
if mibBuilder.loadTexts:zxAnPstnMinDialPulseInterdigit.setUnits(_D)
class _ZxAnPstnPortGlbKcType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('type16kc',1),('type12kc',2)))
_ZxAnPstnPortGlbKcType_Type.__name__=_C
_ZxAnPstnPortGlbKcType_Object=MibScalar
zxAnPstnPortGlbKcType=_ZxAnPstnPortGlbKcType_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1400,51,12),_ZxAnPstnPortGlbKcType_Type())
zxAnPstnPortGlbKcType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPstnPortGlbKcType.setStatus(_A)
class _ZxAnPstnPortGlbKcVoltage_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('volt1V',1),('volt1point5V',2),('volt2V',3),('volt2point5V',4)))
_ZxAnPstnPortGlbKcVoltage_Type.__name__=_C
_ZxAnPstnPortGlbKcVoltage_Object=MibScalar
zxAnPstnPortGlbKcVoltage=_ZxAnPstnPortGlbKcVoltage_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1400,51,13),_ZxAnPstnPortGlbKcVoltage_Type())
zxAnPstnPortGlbKcVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPstnPortGlbKcVoltage.setStatus(_A)
class _ZxAnPstnPortGlbKcPulseWidth_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnPstnPortGlbKcPulseWidth_Type.__name__=_C
_ZxAnPstnPortGlbKcPulseWidth_Object=MibScalar
zxAnPstnPortGlbKcPulseWidth=_ZxAnPstnPortGlbKcPulseWidth_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1400,51,14),_ZxAnPstnPortGlbKcPulseWidth_Type())
zxAnPstnPortGlbKcPulseWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPstnPortGlbKcPulseWidth.setStatus(_A)
if mibBuilder.loadTexts:zxAnPstnPortGlbKcPulseWidth.setUnits(_D)
class _ZxAnPstnPortGlbKcPulseInterval_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnPstnPortGlbKcPulseInterval_Type.__name__=_C
_ZxAnPstnPortGlbKcPulseInterval_Object=MibScalar
zxAnPstnPortGlbKcPulseInterval=_ZxAnPstnPortGlbKcPulseInterval_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1400,51,15),_ZxAnPstnPortGlbKcPulseInterval_Type())
zxAnPstnPortGlbKcPulseInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPstnPortGlbKcPulseInterval.setStatus(_A)
if mibBuilder.loadTexts:zxAnPstnPortGlbKcPulseInterval.setUnits(_D)
class _ZxAnPstnHookFlashMinTime_Type(Integer32):defaultValue=90;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,1500))
_ZxAnPstnHookFlashMinTime_Type.__name__=_C
_ZxAnPstnHookFlashMinTime_Object=MibScalar
zxAnPstnHookFlashMinTime=_ZxAnPstnHookFlashMinTime_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1400,51,16),_ZxAnPstnHookFlashMinTime_Type())
zxAnPstnHookFlashMinTime.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPstnHookFlashMinTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnPstnHookFlashMinTime.setUnits(_D)
class _ZxAnPstnHookFlashMaxTime_Type(Integer32):defaultValue=470;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,1500))
_ZxAnPstnHookFlashMaxTime_Type.__name__=_C
_ZxAnPstnHookFlashMaxTime_Object=MibScalar
zxAnPstnHookFlashMaxTime=_ZxAnPstnHookFlashMaxTime_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1400,51,17),_ZxAnPstnHookFlashMaxTime_Type())
zxAnPstnHookFlashMaxTime.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPstnHookFlashMaxTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnPstnHookFlashMaxTime.setUnits(_D)
_ZxAnPstnPortECharTable_Object=MibTable
zxAnPstnPortECharTable=_ZxAnPstnPortECharTable_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1401))
if mibBuilder.loadTexts:zxAnPstnPortECharTable.setStatus(_A)
_ZxAnPstnPortECharEntry_Object=MibTableRow
zxAnPstnPortECharEntry=_ZxAnPstnPortECharEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1401,1))
zxAnPstnPortECharEntry.setIndexNames((0,_E,_Z),(0,_E,_a),(0,_E,_b),(0,_E,_c))
if mibBuilder.loadTexts:zxAnPstnPortECharEntry.setStatus(_A)
_ZxAnPstnPortECharRack_Type=Integer32
_ZxAnPstnPortECharRack_Object=MibTableColumn
zxAnPstnPortECharRack=_ZxAnPstnPortECharRack_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1401,1,1),_ZxAnPstnPortECharRack_Type())
zxAnPstnPortECharRack.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnPstnPortECharRack.setStatus(_A)
_ZxAnPstnPortECharShelf_Type=Integer32
_ZxAnPstnPortECharShelf_Object=MibTableColumn
zxAnPstnPortECharShelf=_ZxAnPstnPortECharShelf_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1401,1,2),_ZxAnPstnPortECharShelf_Type())
zxAnPstnPortECharShelf.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnPstnPortECharShelf.setStatus(_A)
_ZxAnPstnPortECharSlot_Type=Integer32
_ZxAnPstnPortECharSlot_Object=MibTableColumn
zxAnPstnPortECharSlot=_ZxAnPstnPortECharSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1401,1,3),_ZxAnPstnPortECharSlot_Type())
zxAnPstnPortECharSlot.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnPstnPortECharSlot.setStatus(_A)
_ZxAnPstnPortECharPort_Type=Integer32
_ZxAnPstnPortECharPort_Object=MibTableColumn
zxAnPstnPortECharPort=_ZxAnPstnPortECharPort_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1401,1,4),_ZxAnPstnPortECharPort_Type())
zxAnPstnPortECharPort.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnPstnPortECharPort.setStatus(_A)
_ZxAnPstnPortECharOperNum_Type=Integer32
_ZxAnPstnPortECharOperNum_Object=MibTableColumn
zxAnPstnPortECharOperNum=_ZxAnPstnPortECharOperNum_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1401,1,5),_ZxAnPstnPortECharOperNum_Type())
zxAnPstnPortECharOperNum.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPstnPortECharOperNum.setStatus(_A)
class _ZxAnPstnPortFeedVoltage_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('volt48v',1),('volt75v',2)))
_ZxAnPstnPortFeedVoltage_Type.__name__=_C
_ZxAnPstnPortFeedVoltage_Object=MibTableColumn
zxAnPstnPortFeedVoltage=_ZxAnPstnPortFeedVoltage_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1401,1,6),_ZxAnPstnPortFeedVoltage_Type())
zxAnPstnPortFeedVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPstnPortFeedVoltage.setStatus(_A)
class _ZxAnPstnPortFeedCurrent_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_Q,1),(_R,2),(_S,3),(_T,4),(_U,5),(_V,6),(_W,7),(_X,8)))
_ZxAnPstnPortFeedCurrent_Type.__name__=_C
_ZxAnPstnPortFeedCurrent_Object=MibTableColumn
zxAnPstnPortFeedCurrent=_ZxAnPstnPortFeedCurrent_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1401,1,7),_ZxAnPstnPortFeedCurrent_Type())
zxAnPstnPortFeedCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPstnPortFeedCurrent.setStatus(_A)
class _ZxAnPstnPortImpedanceType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_J,1),('im600ohm',2),('hkBt3',3),('hkBt5',4),('etsi',5),('russia',6)))
_ZxAnPstnPortImpedanceType_Type.__name__=_C
_ZxAnPstnPortImpedanceType_Object=MibTableColumn
zxAnPstnPortImpedanceType=_ZxAnPstnPortImpedanceType_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1401,1,8),_ZxAnPstnPortImpedanceType_Type())
zxAnPstnPortImpedanceType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPstnPortImpedanceType.setStatus(_A)
class _ZxAnPstnPortAdGain_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_d,1),('gainNeg1dB',2),('gainNeg2dB',3),('gainNeg3dB',4),(_e,5),(_f,6),(_g,7),(_h,8),('gain1dB',9),('gain2dB',10),('gain3dB',11)))
_ZxAnPstnPortAdGain_Type.__name__=_C
_ZxAnPstnPortAdGain_Object=MibTableColumn
zxAnPstnPortAdGain=_ZxAnPstnPortAdGain_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1401,1,9),_ZxAnPstnPortAdGain_Type())
zxAnPstnPortAdGain.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPstnPortAdGain.setStatus(_A)
class _ZxAnPstnPortDaGain_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_d,1),('gainNeg3point5dB',2),(_e,3),(_f,4),(_g,5),(_h,6),('gainNeg8dB',7),('gainNeg9dB',8),('gainNeg10dB',9)))
_ZxAnPstnPortDaGain_Type.__name__=_C
_ZxAnPstnPortDaGain_Object=MibTableColumn
zxAnPstnPortDaGain=_ZxAnPstnPortDaGain_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1401,1,10),_ZxAnPstnPortDaGain_Type())
zxAnPstnPortDaGain.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPstnPortDaGain.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'zte':zte,'zxAn':zxAn,'zxAnVoicePortMib':zxAnVoicePortMib,'zxAnVoiceMgmt':zxAnVoiceMgmt,'zxAnVoicePortConfig':zxAnVoicePortConfig,'a200SlcTable':a200SlcTable,'a200SlcEntry':a200SlcEntry,_K:a200slcrackno,_L:a200slcshelfno,_M:a200slcslotno,_N:a200slcindex,'a200slcpkg':a200slcpkg,'a200slcstatus':a200slcstatus,'a200slcdftevent':a200slcdftevent,'a200slcusermode':a200slcusermode,'a200slcFaxMode':a200slcFaxMode,'a200slcQovsId':a200slcQovsId,'a200slcCIDType':a200slcCIDType,'a200slcImType':a200slcImType,'a200slcecenable':a200slcecenable,'a200slcuserclass':a200slcuserclass,'a200slcPktToPcmGain':a200slcPktToPcmGain,'a200slcPcmToPktGain':a200slcPcmToPktGain,'a200slcphonenum':a200slcphonenum,'a200slcoperNum':a200slcoperNum,'a200slcblockoper':a200slcblockoper,'a200slcunblockoper':a200slcunblockoper,'a200slcmonitorflag':a200slcmonitorflag,'a200slcmonitoreerack':a200slcmonitoreerack,'a200slcmonitoreeshelf':a200slcmonitoreeshelf,'a200slcmonitoreeslot':a200slcmonitoreeslot,'a200slcmonitoreeindex':a200slcmonitoreeindex,'a200slcDialMode':a200slcDialMode,'a200slcFeedCurrent':a200slcFeedCurrent,'a200slcHighImpedanceOper':a200slcHighImpedanceOper,'a200slcNoneHighImpedanceOper':a200slcNoneHighImpedanceOper,'zxAnSlcDelayDialMode':zxAnSlcDelayDialMode,'zxAnSlcDdiTrapEnable':zxAnSlcDdiTrapEnable,'zxAnSlcSemiPerConnSrcIpAddr':zxAnSlcSemiPerConnSrcIpAddr,'zxAnSlcSemiPerConnSrcPort':zxAnSlcSemiPerConnSrcPort,'zxAnSlcSemiPerConnDstIpAddr':zxAnSlcSemiPerConnDstIpAddr,'zxAnSlcSemiPerConnDstPort':zxAnSlcSemiPerConnDstPort,'zxAnSlcSemiPerConnSdpProfileId':zxAnSlcSemiPerConnSdpProfileId,'zxAnSlcSemiPerConnSdpInformation':zxAnSlcSemiPerConnSdpInformation,'zxAnVoicePortGlobalObjects':zxAnVoicePortGlobalObjects,'zxAnVoicePortMgmtCapabilities':zxAnVoicePortMgmtCapabilities,'zxAnPstnPortECharGlobalObjects':zxAnPstnPortECharGlobalObjects,'zxAnPstnPortGlbPcmLaw':zxAnPstnPortGlbPcmLaw,'zxAnPstnPortGlbRingVoltage':zxAnPstnPortGlbRingVoltage,'zxAnPstnPortGlbRingFrequency':zxAnPstnPortGlbRingFrequency,'zxAnPstnPolarityRevPulseEnable':zxAnPstnPolarityRevPulseEnable,'zxAnPstnPolarityRevPulseWidth':zxAnPstnPolarityRevPulseWidth,'zxAnPstnPolarityRevMode':zxAnPstnPolarityRevMode,'zxAnPstnMinDialPulseBreakTime':zxAnPstnMinDialPulseBreakTime,'zxAnPstnMaxDialPulseBreakTime':zxAnPstnMaxDialPulseBreakTime,'zxAnPstnMinDialPulseMakeTime':zxAnPstnMinDialPulseMakeTime,'zxAnPstnMaxDialPulseMakeTime':zxAnPstnMaxDialPulseMakeTime,'zxAnPstnMinDialPulseInterdigit':zxAnPstnMinDialPulseInterdigit,'zxAnPstnPortGlbKcType':zxAnPstnPortGlbKcType,'zxAnPstnPortGlbKcVoltage':zxAnPstnPortGlbKcVoltage,'zxAnPstnPortGlbKcPulseWidth':zxAnPstnPortGlbKcPulseWidth,'zxAnPstnPortGlbKcPulseInterval':zxAnPstnPortGlbKcPulseInterval,'zxAnPstnHookFlashMinTime':zxAnPstnHookFlashMinTime,'zxAnPstnHookFlashMaxTime':zxAnPstnHookFlashMaxTime,'zxAnPstnPortECharTable':zxAnPstnPortECharTable,'zxAnPstnPortECharEntry':zxAnPstnPortECharEntry,_Z:zxAnPstnPortECharRack,_a:zxAnPstnPortECharShelf,_b:zxAnPstnPortECharSlot,_c:zxAnPstnPortECharPort,'zxAnPstnPortECharOperNum':zxAnPstnPortECharOperNum,'zxAnPstnPortFeedVoltage':zxAnPstnPortFeedVoltage,'zxAnPstnPortFeedCurrent':zxAnPstnPortFeedCurrent,'zxAnPstnPortImpedanceType':zxAnPstnPortImpedanceType,'zxAnPstnPortAdGain':zxAnPstnPortAdGain,'zxAnPstnPortDaGain':zxAnPstnPortDaGain})