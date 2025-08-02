_r='zxAnIpsStaticTidSequenceNumber'
_q='zxAnIpsStaticTidSubcard'
_p='zxAnIpsStaticTidSlot'
_o='zxAnIpsStaticTidShelf'
_n='zxAnIpsStaticTidRack'
_m='zxAnToneMgId'
_l='zxAnSlcVoipPort'
_k='zxAnSlcVoipSlot'
_j='zxAnSlcVoipShelf'
_i='zxAnSlcVoipRack'
_h='zxAnCircuitType'
_g='milliseconds'
_f='ssControl'
_e='selfSwitch'
_d='selfNegotiation'
_c='a200mprbparparid'
_b='a200confindex'
_a='a200confsubdevno'
_Z='a200confslotno'
_Y='a200confshelfno'
_X='a200confrackno'
_W='a200asigindex'
_V='a200asigsubdevno'
_U='a200asigslotno'
_T='a200asigshelfno'
_S='a200asigrackno'
_R='a200ipsindex'
_Q='a200ipsubdevno'
_P='a200ipsslotno'
_O='a200ipsshelfno'
_N='a200ipsrackno'
_M='enable'
_L='disable'
_K='seconds'
_J='DisplayString'
_I='read-create'
_H='report'
_G='notReport'
_F='not-accessible'
_E='ZTE-AN-VOICE-RESOURCE-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_J,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
zxAnVoiceResourceMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,5200))
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_ZxAn_ObjectIdentity=ObjectIdentity
zxAn=_ZxAn_ObjectIdentity((1,3,6,1,4,1,3902,1015))
_ZxAnVoiceMgmt_ObjectIdentity=ObjectIdentity
zxAnVoiceMgmt=_ZxAnVoiceMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3))
_ZxAnVoipResource_ObjectIdentity=ObjectIdentity
zxAnVoipResource=_ZxAnVoipResource_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,3))
_A200IpsTable_Object=MibTable
a200IpsTable=_A200IpsTable_Object((1,3,6,1,4,1,3902,1015,5200,3,3,2))
if mibBuilder.loadTexts:a200IpsTable.setStatus(_A)
_A200IpsEntry_Object=MibTableRow
a200IpsEntry=_A200IpsEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,3,2,1))
a200IpsEntry.setIndexNames((0,_E,_N),(0,_E,_O),(0,_E,_P),(0,_E,_Q),(0,_E,_R))
if mibBuilder.loadTexts:a200IpsEntry.setStatus(_A)
_A200ipsrackno_Type=Integer32
_A200ipsrackno_Object=MibTableColumn
a200ipsrackno=_A200ipsrackno_Object((1,3,6,1,4,1,3902,1015,5200,3,3,2,1,1),_A200ipsrackno_Type())
a200ipsrackno.setMaxAccess(_F)
if mibBuilder.loadTexts:a200ipsrackno.setStatus(_A)
_A200ipsshelfno_Type=Integer32
_A200ipsshelfno_Object=MibTableColumn
a200ipsshelfno=_A200ipsshelfno_Object((1,3,6,1,4,1,3902,1015,5200,3,3,2,1,2),_A200ipsshelfno_Type())
a200ipsshelfno.setMaxAccess(_F)
if mibBuilder.loadTexts:a200ipsshelfno.setStatus(_A)
_A200ipsslotno_Type=Integer32
_A200ipsslotno_Object=MibTableColumn
a200ipsslotno=_A200ipsslotno_Object((1,3,6,1,4,1,3902,1015,5200,3,3,2,1,3),_A200ipsslotno_Type())
a200ipsslotno.setMaxAccess(_F)
if mibBuilder.loadTexts:a200ipsslotno.setStatus(_A)
_A200ipsubdevno_Type=Integer32
_A200ipsubdevno_Object=MibTableColumn
a200ipsubdevno=_A200ipsubdevno_Object((1,3,6,1,4,1,3902,1015,5200,3,3,2,1,4),_A200ipsubdevno_Type())
a200ipsubdevno.setMaxAccess(_F)
if mibBuilder.loadTexts:a200ipsubdevno.setStatus(_A)
_A200ipsindex_Type=Integer32
_A200ipsindex_Object=MibTableColumn
a200ipsindex=_A200ipsindex_Object((1,3,6,1,4,1,3902,1015,5200,3,3,2,1,5),_A200ipsindex_Type())
a200ipsindex.setMaxAccess(_F)
if mibBuilder.loadTexts:a200ipsindex.setStatus(_A)
_A200ipsstatus_Type=Integer32
_A200ipsstatus_Object=MibTableColumn
a200ipsstatus=_A200ipsstatus_Object((1,3,6,1,4,1,3902,1015,5200,3,3,2,1,6),_A200ipsstatus_Type())
a200ipsstatus.setMaxAccess(_D)
if mibBuilder.loadTexts:a200ipsstatus.setStatus(_A)
_A200ipspkg_Type=Unsigned32
_A200ipspkg_Object=MibTableColumn
a200ipspkg=_A200ipspkg_Object((1,3,6,1,4,1,3902,1015,5200,3,3,2,1,7),_A200ipspkg_Type())
a200ipspkg.setMaxAccess(_D)
if mibBuilder.loadTexts:a200ipspkg.setStatus(_A)
class _A200ipsmuxtype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_A200ipsmuxtype_Type.__name__=_B
_A200ipsmuxtype_Object=MibTableColumn
a200ipsmuxtype=_A200ipsmuxtype_Object((1,3,6,1,4,1,3902,1015,5200,3,3,2,1,8),_A200ipsmuxtype_Type())
a200ipsmuxtype.setMaxAccess(_C)
if mibBuilder.loadTexts:a200ipsmuxtype.setStatus(_A)
_A200ipsmodmtype_Type=Integer32
_A200ipsmodmtype_Object=MibTableColumn
a200ipsmodmtype=_A200ipsmodmtype_Object((1,3,6,1,4,1,3902,1015,5200,3,3,2,1,9),_A200ipsmodmtype_Type())
a200ipsmodmtype.setMaxAccess(_D)
if mibBuilder.loadTexts:a200ipsmodmtype.setStatus(_A)
_A200ipslpt_Type=Unsigned32
_A200ipslpt_Object=MibTableColumn
a200ipslpt=_A200ipslpt_Object((1,3,6,1,4,1,3902,1015,5200,3,3,2,1,10),_A200ipslpt_Type())
a200ipslpt.setMaxAccess(_D)
if mibBuilder.loadTexts:a200ipslpt.setStatus(_A)
_A200ipsrpt_Type=Unsigned32
_A200ipsrpt_Object=MibTableColumn
a200ipsrpt=_A200ipsrpt_Object((1,3,6,1,4,1,3902,1015,5200,3,3,2,1,11),_A200ipsrpt_Type())
a200ipsrpt.setMaxAccess(_D)
if mibBuilder.loadTexts:a200ipsrpt.setStatus(_A)
_A200ipslptimmin_Type=Integer32
_A200ipslptimmin_Object=MibTableColumn
a200ipslptimmin=_A200ipslptimmin_Object((1,3,6,1,4,1,3902,1015,5200,3,3,2,1,12),_A200ipslptimmin_Type())
a200ipslptimmin.setMaxAccess(_C)
if mibBuilder.loadTexts:a200ipslptimmin.setStatus(_A)
_A200ipslptimmax_Type=Integer32
_A200ipslptimmax_Object=MibTableColumn
a200ipslptimmax=_A200ipslptimmax_Object((1,3,6,1,4,1,3902,1015,5200,3,3,2,1,13),_A200ipslptimmax_Type())
a200ipslptimmax.setMaxAccess(_C)
if mibBuilder.loadTexts:a200ipslptimmax.setStatus(_A)
_A200ipsrptimmin_Type=Integer32
_A200ipsrptimmin_Object=MibTableColumn
a200ipsrptimmin=_A200ipsrptimmin_Object((1,3,6,1,4,1,3902,1015,5200,3,3,2,1,14),_A200ipsrptimmin_Type())
a200ipsrptimmin.setMaxAccess(_C)
if mibBuilder.loadTexts:a200ipsrptimmin.setStatus(_A)
_A200ipsrptimmax_Type=Integer32
_A200ipsrptimmax_Object=MibTableColumn
a200ipsrptimmax=_A200ipsrptimmax_Object((1,3,6,1,4,1,3902,1015,5200,3,3,2,1,15),_A200ipsrptimmax_Type())
a200ipsrptimmax.setMaxAccess(_C)
if mibBuilder.loadTexts:a200ipsrptimmax.setStatus(_A)
_A200ipstmmdtyp_Type=Integer32
_A200ipstmmdtyp_Object=MibTableColumn
a200ipstmmdtyp=_A200ipstmmdtyp_Object((1,3,6,1,4,1,3902,1015,5200,3,3,2,1,16),_A200ipstmmdtyp_Type())
a200ipstmmdtyp.setMaxAccess(_D)
if mibBuilder.loadTexts:a200ipstmmdtyp.setStatus(_A)
_A200ipscallerid_Type=Integer32
_A200ipscallerid_Object=MibTableColumn
a200ipscallerid=_A200ipscallerid_Object((1,3,6,1,4,1,3902,1015,5200,3,3,2,1,17),_A200ipscallerid_Type())
a200ipscallerid.setMaxAccess(_D)
if mibBuilder.loadTexts:a200ipscallerid.setStatus(_A)
class _A200ipsoperNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_A200ipsoperNum_Type.__name__=_B
_A200ipsoperNum_Object=MibTableColumn
a200ipsoperNum=_A200ipsoperNum_Object((1,3,6,1,4,1,3902,1015,5200,3,3,2,1,18),_A200ipsoperNum_Type())
a200ipsoperNum.setMaxAccess(_C)
if mibBuilder.loadTexts:a200ipsoperNum.setStatus(_A)
class _A200ipsblockoper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_A200ipsblockoper_Type.__name__=_B
_A200ipsblockoper_Object=MibTableColumn
a200ipsblockoper=_A200ipsblockoper_Object((1,3,6,1,4,1,3902,1015,5200,3,3,2,1,19),_A200ipsblockoper_Type())
a200ipsblockoper.setMaxAccess(_C)
if mibBuilder.loadTexts:a200ipsblockoper.setStatus(_A)
class _A200ipsunblockoper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_A200ipsunblockoper_Type.__name__=_B
_A200ipsunblockoper_Object=MibTableColumn
a200ipsunblockoper=_A200ipsunblockoper_Object((1,3,6,1,4,1,3902,1015,5200,3,3,2,1,20),_A200ipsunblockoper_Type())
a200ipsunblockoper.setMaxAccess(_C)
if mibBuilder.loadTexts:a200ipsunblockoper.setStatus(_A)
_A200AsigTable_Object=MibTable
a200AsigTable=_A200AsigTable_Object((1,3,6,1,4,1,3902,1015,5200,3,3,3))
if mibBuilder.loadTexts:a200AsigTable.setStatus(_A)
_A200AsigEntry_Object=MibTableRow
a200AsigEntry=_A200AsigEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,3,3,1))
a200AsigEntry.setIndexNames((0,_E,_S),(0,_E,_T),(0,_E,_U),(0,_E,_V),(0,_E,_W))
if mibBuilder.loadTexts:a200AsigEntry.setStatus(_A)
_A200asigrackno_Type=Integer32
_A200asigrackno_Object=MibTableColumn
a200asigrackno=_A200asigrackno_Object((1,3,6,1,4,1,3902,1015,5200,3,3,3,1,1),_A200asigrackno_Type())
a200asigrackno.setMaxAccess(_F)
if mibBuilder.loadTexts:a200asigrackno.setStatus(_A)
_A200asigshelfno_Type=Integer32
_A200asigshelfno_Object=MibTableColumn
a200asigshelfno=_A200asigshelfno_Object((1,3,6,1,4,1,3902,1015,5200,3,3,3,1,2),_A200asigshelfno_Type())
a200asigshelfno.setMaxAccess(_F)
if mibBuilder.loadTexts:a200asigshelfno.setStatus(_A)
_A200asigslotno_Type=Integer32
_A200asigslotno_Object=MibTableColumn
a200asigslotno=_A200asigslotno_Object((1,3,6,1,4,1,3902,1015,5200,3,3,3,1,3),_A200asigslotno_Type())
a200asigslotno.setMaxAccess(_F)
if mibBuilder.loadTexts:a200asigslotno.setStatus(_A)
_A200asigsubdevno_Type=Integer32
_A200asigsubdevno_Object=MibTableColumn
a200asigsubdevno=_A200asigsubdevno_Object((1,3,6,1,4,1,3902,1015,5200,3,3,3,1,4),_A200asigsubdevno_Type())
a200asigsubdevno.setMaxAccess(_F)
if mibBuilder.loadTexts:a200asigsubdevno.setStatus(_A)
_A200asigindex_Type=Integer32
_A200asigindex_Object=MibTableColumn
a200asigindex=_A200asigindex_Object((1,3,6,1,4,1,3902,1015,5200,3,3,3,1,5),_A200asigindex_Type())
a200asigindex.setMaxAccess(_F)
if mibBuilder.loadTexts:a200asigindex.setStatus(_A)
_A200asigstatus_Type=Integer32
_A200asigstatus_Object=MibTableColumn
a200asigstatus=_A200asigstatus_Object((1,3,6,1,4,1,3902,1015,5200,3,3,3,1,6),_A200asigstatus_Type())
a200asigstatus.setMaxAccess(_D)
if mibBuilder.loadTexts:a200asigstatus.setStatus(_A)
class _A200asigkind_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('dtmf',1),('tone',2),('cid',3),('mfc',4),('conf',5),('mf',6)))
_A200asigkind_Type.__name__=_B
_A200asigkind_Object=MibTableColumn
a200asigkind=_A200asigkind_Object((1,3,6,1,4,1,3902,1015,5200,3,3,3,1,7),_A200asigkind_Type())
a200asigkind.setMaxAccess(_C)
if mibBuilder.loadTexts:a200asigkind.setStatus(_A)
class _A200asigoperNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_A200asigoperNum_Type.__name__=_B
_A200asigoperNum_Object=MibTableColumn
a200asigoperNum=_A200asigoperNum_Object((1,3,6,1,4,1,3902,1015,5200,3,3,3,1,8),_A200asigoperNum_Type())
a200asigoperNum.setMaxAccess(_C)
if mibBuilder.loadTexts:a200asigoperNum.setStatus(_A)
class _A200asigBlockOper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_A200asigBlockOper_Type.__name__=_B
_A200asigBlockOper_Object=MibTableColumn
a200asigBlockOper=_A200asigBlockOper_Object((1,3,6,1,4,1,3902,1015,5200,3,3,3,1,9),_A200asigBlockOper_Type())
a200asigBlockOper.setMaxAccess(_C)
if mibBuilder.loadTexts:a200asigBlockOper.setStatus(_A)
class _A200asigUnblockOper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_A200asigUnblockOper_Type.__name__=_B
_A200asigUnblockOper_Object=MibTableColumn
a200asigUnblockOper=_A200asigUnblockOper_Object((1,3,6,1,4,1,3902,1015,5200,3,3,3,1,10),_A200asigUnblockOper_Type())
a200asigUnblockOper.setMaxAccess(_C)
if mibBuilder.loadTexts:a200asigUnblockOper.setStatus(_A)
_A200ConfTable_Object=MibTable
a200ConfTable=_A200ConfTable_Object((1,3,6,1,4,1,3902,1015,5200,3,3,4))
if mibBuilder.loadTexts:a200ConfTable.setStatus(_A)
_A200ConfEntry_Object=MibTableRow
a200ConfEntry=_A200ConfEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,3,4,1))
a200ConfEntry.setIndexNames((0,_E,_X),(0,_E,_Y),(0,_E,_Z),(0,_E,_a),(0,_E,_b))
if mibBuilder.loadTexts:a200ConfEntry.setStatus(_A)
_A200confrackno_Type=Integer32
_A200confrackno_Object=MibTableColumn
a200confrackno=_A200confrackno_Object((1,3,6,1,4,1,3902,1015,5200,3,3,4,1,1),_A200confrackno_Type())
a200confrackno.setMaxAccess(_F)
if mibBuilder.loadTexts:a200confrackno.setStatus(_A)
_A200confshelfno_Type=Integer32
_A200confshelfno_Object=MibTableColumn
a200confshelfno=_A200confshelfno_Object((1,3,6,1,4,1,3902,1015,5200,3,3,4,1,2),_A200confshelfno_Type())
a200confshelfno.setMaxAccess(_F)
if mibBuilder.loadTexts:a200confshelfno.setStatus(_A)
_A200confslotno_Type=Integer32
_A200confslotno_Object=MibTableColumn
a200confslotno=_A200confslotno_Object((1,3,6,1,4,1,3902,1015,5200,3,3,4,1,3),_A200confslotno_Type())
a200confslotno.setMaxAccess(_F)
if mibBuilder.loadTexts:a200confslotno.setStatus(_A)
_A200confsubdevno_Type=Integer32
_A200confsubdevno_Object=MibTableColumn
a200confsubdevno=_A200confsubdevno_Object((1,3,6,1,4,1,3902,1015,5200,3,3,4,1,4),_A200confsubdevno_Type())
a200confsubdevno.setMaxAccess(_F)
if mibBuilder.loadTexts:a200confsubdevno.setStatus(_A)
_A200confindex_Type=Integer32
_A200confindex_Object=MibTableColumn
a200confindex=_A200confindex_Object((1,3,6,1,4,1,3902,1015,5200,3,3,4,1,5),_A200confindex_Type())
a200confindex.setMaxAccess(_F)
if mibBuilder.loadTexts:a200confindex.setStatus(_A)
_A200confstatus_Type=Integer32
_A200confstatus_Object=MibTableColumn
a200confstatus=_A200confstatus_Object((1,3,6,1,4,1,3902,1015,5200,3,3,4,1,6),_A200confstatus_Type())
a200confstatus.setMaxAccess(_D)
if mibBuilder.loadTexts:a200confstatus.setStatus(_A)
_A200confset_Type=Integer32
_A200confset_Object=MibTableColumn
a200confset=_A200confset_Object((1,3,6,1,4,1,3902,1015,5200,3,3,4,1,7),_A200confset_Type())
a200confset.setMaxAccess(_D)
if mibBuilder.loadTexts:a200confset.setStatus(_A)
_A200confgroup_Type=Integer32
_A200confgroup_Object=MibTableColumn
a200confgroup=_A200confgroup_Object((1,3,6,1,4,1,3902,1015,5200,3,3,4,1,8),_A200confgroup_Type())
a200confgroup.setMaxAccess(_D)
if mibBuilder.loadTexts:a200confgroup.setStatus(_A)
_A200confoperNum_Type=Integer32
_A200confoperNum_Object=MibTableColumn
a200confoperNum=_A200confoperNum_Object((1,3,6,1,4,1,3902,1015,5200,3,3,4,1,9),_A200confoperNum_Type())
a200confoperNum.setMaxAccess(_C)
if mibBuilder.loadTexts:a200confoperNum.setStatus(_A)
class _A200confblockoper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_A200confblockoper_Type.__name__=_B
_A200confblockoper_Object=MibTableColumn
a200confblockoper=_A200confblockoper_Object((1,3,6,1,4,1,3902,1015,5200,3,3,4,1,10),_A200confblockoper_Type())
a200confblockoper.setMaxAccess(_C)
if mibBuilder.loadTexts:a200confblockoper.setStatus(_A)
class _A200confunblockoper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_A200confunblockoper_Type.__name__=_B
_A200confunblockoper_Object=MibTableColumn
a200confunblockoper=_A200confunblockoper_Object((1,3,6,1,4,1,3902,1015,5200,3,3,4,1,11),_A200confunblockoper_Type())
a200confunblockoper.setMaxAccess(_C)
if mibBuilder.loadTexts:a200confunblockoper.setStatus(_A)
_A200MprbParTable_Object=MibTable
a200MprbParTable=_A200MprbParTable_Object((1,3,6,1,4,1,3902,1015,5200,3,3,9))
if mibBuilder.loadTexts:a200MprbParTable.setStatus(_A)
_A200MprbParEntry_Object=MibTableRow
a200MprbParEntry=_A200MprbParEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,3,9,1))
a200MprbParEntry.setIndexNames((0,_E,_c))
if mibBuilder.loadTexts:a200MprbParEntry.setStatus(_A)
class _A200mprbparparid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_A200mprbparparid_Type.__name__=_B
_A200mprbparparid_Object=MibTableColumn
a200mprbparparid=_A200mprbparparid_Object((1,3,6,1,4,1,3902,1015,5200,3,3,9,1,1),_A200mprbparparid_Type())
a200mprbparparid.setMaxAccess(_F)
if mibBuilder.loadTexts:a200mprbparparid.setStatus(_A)
class _A200mprbpardtmfrelaymode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,6)));namedValues=NamedValues(*(('notRelay',0),('voiceCoding',1),('redRfc2833',2),('aal2Ietf',4),('nredRfc2833',6)))
_A200mprbpardtmfrelaymode_Type.__name__=_B
_A200mprbpardtmfrelaymode_Object=MibTableColumn
a200mprbpardtmfrelaymode=_A200mprbpardtmfrelaymode_Object((1,3,6,1,4,1,3902,1015,5200,3,3,9,1,2),_A200mprbpardtmfrelaymode_Type())
a200mprbpardtmfrelaymode.setMaxAccess(_C)
if mibBuilder.loadTexts:a200mprbpardtmfrelaymode.setStatus(_A)
class _A200mprbpardtmfpayload_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_A200mprbpardtmfpayload_Type.__name__=_B
_A200mprbpardtmfpayload_Object=MibTableColumn
a200mprbpardtmfpayload=_A200mprbpardtmfpayload_Object((1,3,6,1,4,1,3902,1015,5200,3,3,9,1,3),_A200mprbpardtmfpayload_Type())
a200mprbpardtmfpayload.setMaxAccess(_C)
if mibBuilder.loadTexts:a200mprbpardtmfpayload.setStatus(_A)
class _A200mprbpardtmfredundant_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_A200mprbpardtmfredundant_Type.__name__=_B
_A200mprbpardtmfredundant_Object=MibTableColumn
a200mprbpardtmfredundant=_A200mprbpardtmfredundant_Object((1,3,6,1,4,1,3902,1015,5200,3,3,9,1,4),_A200mprbpardtmfredundant_Type())
a200mprbpardtmfredundant.setMaxAccess(_C)
if mibBuilder.loadTexts:a200mprbpardtmfredundant.setStatus(_A)
class _A200mprbparecenable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_A200mprbparecenable_Type.__name__=_B
_A200mprbparecenable_Object=MibTableColumn
a200mprbparecenable=_A200mprbparecenable_Object((1,3,6,1,4,1,3902,1015,5200,3,3,9,1,5),_A200mprbparecenable_Type())
a200mprbparecenable.setMaxAccess(_C)
if mibBuilder.loadTexts:a200mprbparecenable.setStatus(_A)
class _A200mprbparectaillen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,7,15)));namedValues=NamedValues(*(('is8ms',0),('is16ms',1),('is24ms',2),('is32ms',3),('is64ms',7),('is128ms',15)))
_A200mprbparectaillen_Type.__name__=_B
_A200mprbparectaillen_Object=MibTableColumn
a200mprbparectaillen=_A200mprbparectaillen_Object((1,3,6,1,4,1,3902,1015,5200,3,3,9,1,6),_A200mprbparectaillen_Type())
a200mprbparectaillen.setMaxAccess(_C)
if mibBuilder.loadTexts:a200mprbparectaillen.setStatus(_A)
class _A200mprbparectxf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('notLinear',0),('fixedTransmit',1)))
_A200mprbparectxf_Type.__name__=_B
_A200mprbparectxf_Object=MibTableColumn
a200mprbparectxf=_A200mprbparectxf_Object((1,3,6,1,4,1,3902,1015,5200,3,3,9,1,7),_A200mprbparectxf_Type())
a200mprbparectxf.setMaxAccess(_C)
if mibBuilder.loadTexts:a200mprbparectxf.setStatus(_A)
class _A200mprbparnlpaggress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_A200mprbparnlpaggress_Type.__name__=_B
_A200mprbparnlpaggress_Object=MibTableColumn
a200mprbparnlpaggress=_A200mprbparnlpaggress_Object((1,3,6,1,4,1,3902,1015,5200,3,3,9,1,8),_A200mprbparnlpaggress_Type())
a200mprbparnlpaggress.setMaxAccess(_C)
if mibBuilder.loadTexts:a200mprbparnlpaggress.setStatus(_A)
class _A200mprbparg711redundancy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_A200mprbparg711redundancy_Type.__name__=_B
_A200mprbparg711redundancy_Object=MibTableColumn
a200mprbparg711redundancy=_A200mprbparg711redundancy_Object((1,3,6,1,4,1,3902,1015,5200,3,3,9,1,9),_A200mprbparg711redundancy_Type())
a200mprbparg711redundancy.setMaxAccess(_C)
if mibBuilder.loadTexts:a200mprbparg711redundancy.setStatus(_A)
class _A200mprbparfaxmode_Type(Integer32):defaultValue=11;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,6,11)));namedValues=NamedValues(*((_d,0),(_e,6),(_f,11)))
_A200mprbparfaxmode_Type.__name__=_B
_A200mprbparfaxmode_Object=MibTableColumn
a200mprbparfaxmode=_A200mprbparfaxmode_Object((1,3,6,1,4,1,3902,1015,5200,3,3,9,1,10),_A200mprbparfaxmode_Type())
a200mprbparfaxmode.setMaxAccess(_C)
if mibBuilder.loadTexts:a200mprbparfaxmode.setStatus(_A)
class _A200mprbparmodemmode_Type(Integer32):defaultValue=11;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,6,11)));namedValues=NamedValues(*((_d,0),(_e,6),(_f,11)))
_A200mprbparmodemmode_Type.__name__=_B
_A200mprbparmodemmode_Object=MibTableColumn
a200mprbparmodemmode=_A200mprbparmodemmode_Object((1,3,6,1,4,1,3902,1015,5200,3,3,9,1,11),_A200mprbparmodemmode_Type())
a200mprbparmodemmode.setMaxAccess(_C)
if mibBuilder.loadTexts:a200mprbparmodemmode.setStatus(_A)
class _A200mprbparecmenable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('preventEcm',0),('allowEcm',1)))
_A200mprbparecmenable_Type.__name__=_B
_A200mprbparecmenable_Object=MibTableColumn
a200mprbparecmenable=_A200mprbparecmenable_Object((1,3,6,1,4,1,3902,1015,5200,3,3,9,1,12),_A200mprbparecmenable_Type())
a200mprbparecmenable.setMaxAccess(_C)
if mibBuilder.loadTexts:a200mprbparecmenable.setStatus(_A)
class _A200mprbparfaxpage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_A200mprbparfaxpage_Type.__name__=_B
_A200mprbparfaxpage_Object=MibTableColumn
a200mprbparfaxpage=_A200mprbparfaxpage_Object((1,3,6,1,4,1,3902,1015,5200,3,3,9,1,13),_A200mprbparfaxpage_Type())
a200mprbparfaxpage.setMaxAccess(_C)
if mibBuilder.loadTexts:a200mprbparfaxpage.setStatus(_A)
class _A200mprbpart30message_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_A200mprbpart30message_Type.__name__=_B
_A200mprbpart30message_Object=MibTableColumn
a200mprbpart30message=_A200mprbpart30message_Object((1,3,6,1,4,1,3902,1015,5200,3,3,9,1,14),_A200mprbpart30message_Type())
a200mprbpart30message.setMaxAccess(_C)
if mibBuilder.loadTexts:a200mprbpart30message.setStatus(_A)
class _A200mprbparspeedlimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('noLimit',0),('is2400bps',1),('is4800bps',2),('is7200bps',3),('is9600bps',4),('is12000bps',5),('is14400bps',6)))
_A200mprbparspeedlimit_Type.__name__=_B
_A200mprbparspeedlimit_Object=MibTableColumn
a200mprbparspeedlimit=_A200mprbparspeedlimit_Object((1,3,6,1,4,1,3902,1015,5200,3,3,9,1,15),_A200mprbparspeedlimit_Type())
a200mprbparspeedlimit.setMaxAccess(_C)
if mibBuilder.loadTexts:a200mprbparspeedlimit.setStatus(_A)
class _A200mprbpartcfprocedure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('procedure2',0),('procedure1',1)))
_A200mprbpartcfprocedure_Type.__name__=_B
_A200mprbpartcfprocedure_Object=MibTableColumn
a200mprbpartcfprocedure=_A200mprbpartcfprocedure_Object((1,3,6,1,4,1,3902,1015,5200,3,3,9,1,16),_A200mprbpartcfprocedure_Type())
a200mprbpartcfprocedure.setMaxAccess(_C)
if mibBuilder.loadTexts:a200mprbpartcfprocedure.setStatus(_A)
class _A200mprbparfaxswtime_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_A200mprbparfaxswtime_Type.__name__=_B
_A200mprbparfaxswtime_Object=MibTableColumn
a200mprbparfaxswtime=_A200mprbparfaxswtime_Object((1,3,6,1,4,1,3902,1015,5200,3,3,9,1,17),_A200mprbparfaxswtime_Type())
a200mprbparfaxswtime.setMaxAccess(_C)
if mibBuilder.loadTexts:a200mprbparfaxswtime.setStatus(_A)
if mibBuilder.loadTexts:a200mprbparfaxswtime.setUnits('100ms')
class _A200mprbparmindelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_A200mprbparmindelay_Type.__name__=_B
_A200mprbparmindelay_Object=MibTableColumn
a200mprbparmindelay=_A200mprbparmindelay_Object((1,3,6,1,4,1,3902,1015,5200,3,3,9,1,18),_A200mprbparmindelay_Type())
a200mprbparmindelay.setMaxAccess(_C)
if mibBuilder.loadTexts:a200mprbparmindelay.setStatus(_A)
class _A200mprbparmaxdelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_A200mprbparmaxdelay_Type.__name__=_B
_A200mprbparmaxdelay_Object=MibTableColumn
a200mprbparmaxdelay=_A200mprbparmaxdelay_Object((1,3,6,1,4,1,3902,1015,5200,3,3,9,1,19),_A200mprbparmaxdelay_Type())
a200mprbparmaxdelay.setMaxAccess(_C)
if mibBuilder.loadTexts:a200mprbparmaxdelay.setStatus(_A)
class _A200mprbparnomdelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_A200mprbparnomdelay_Type.__name__=_B
_A200mprbparnomdelay_Object=MibTableColumn
a200mprbparnomdelay=_A200mprbparnomdelay_Object((1,3,6,1,4,1,3902,1015,5200,3,3,9,1,20),_A200mprbparnomdelay_Type())
a200mprbparnomdelay.setMaxAccess(_C)
if mibBuilder.loadTexts:a200mprbparnomdelay.setStatus(_A)
class _A200mprbparvadvalue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('disableVAD',0),('defaultScheme',1),('reserved',2)))
_A200mprbparvadvalue_Type.__name__=_B
_A200mprbparvadvalue_Object=MibTableColumn
a200mprbparvadvalue=_A200mprbparvadvalue_Object((1,3,6,1,4,1,3902,1015,5200,3,3,9,1,21),_A200mprbparvadvalue_Type())
a200mprbparvadvalue.setMaxAccess(_C)
if mibBuilder.loadTexts:a200mprbparvadvalue.setStatus(_A)
class _A200mprbparg723rate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('lowRT5point3kbps',0),('highRT6point3kbps',1)))
_A200mprbparg723rate_Type.__name__=_B
_A200mprbparg723rate_Object=MibTableColumn
a200mprbparg723rate=_A200mprbparg723rate_Object((1,3,6,1,4,1,3902,1015,5200,3,3,9,1,22),_A200mprbparg723rate_Type())
a200mprbparg723rate.setMaxAccess(_C)
if mibBuilder.loadTexts:a200mprbparg723rate.setStatus(_A)
class _A200mprbpardcfilter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('enabledc',0),('disabledc',1)))
_A200mprbpardcfilter_Type.__name__=_B
_A200mprbpardcfilter_Object=MibTableColumn
a200mprbpardcfilter=_A200mprbpardcfilter_Object((1,3,6,1,4,1,3902,1015,5200,3,3,9,1,23),_A200mprbpardcfilter_Type())
a200mprbpardcfilter.setMaxAccess(_C)
if mibBuilder.loadTexts:a200mprbpardcfilter.setStatus(_A)
class _A200mprbparsilencetopcm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('comfortNoise',0),('silence',1)))
_A200mprbparsilencetopcm_Type.__name__=_B
_A200mprbparsilencetopcm_Object=MibTableColumn
a200mprbparsilencetopcm=_A200mprbparsilencetopcm_Object((1,3,6,1,4,1,3902,1015,5200,3,3,9,1,24),_A200mprbparsilencetopcm_Type())
a200mprbparsilencetopcm.setMaxAccess(_C)
if mibBuilder.loadTexts:a200mprbparsilencetopcm.setStatus(_A)
class _A200mprbparpcmlaw_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('aLaw',0),('muLaw',1)))
_A200mprbparpcmlaw_Type.__name__=_B
_A200mprbparpcmlaw_Object=MibTableColumn
a200mprbparpcmlaw=_A200mprbparpcmlaw_Object((1,3,6,1,4,1,3902,1015,5200,3,3,9,1,25),_A200mprbparpcmlaw_Type())
a200mprbparpcmlaw.setMaxAccess(_C)
if mibBuilder.loadTexts:a200mprbparpcmlaw.setStatus(_A)
class _A200mprbparpcmtopkggain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-20,20))
_A200mprbparpcmtopkggain_Type.__name__=_B
_A200mprbparpcmtopkggain_Object=MibTableColumn
a200mprbparpcmtopkggain=_A200mprbparpcmtopkggain_Object((1,3,6,1,4,1,3902,1015,5200,3,3,9,1,26),_A200mprbparpcmtopkggain_Type())
a200mprbparpcmtopkggain.setMaxAccess(_C)
if mibBuilder.loadTexts:a200mprbparpcmtopkggain.setStatus(_A)
class _A200mprbparpkgtopcmgain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-20,20))
_A200mprbparpkgtopcmgain_Type.__name__=_B
_A200mprbparpkgtopcmgain_Object=MibTableColumn
a200mprbparpkgtopcmgain=_A200mprbparpkgtopcmgain_Object((1,3,6,1,4,1,3902,1015,5200,3,3,9,1,27),_A200mprbparpkgtopcmgain_Type())
a200mprbparpkgtopcmgain.setMaxAccess(_C)
if mibBuilder.loadTexts:a200mprbparpkgtopcmgain.setStatus(_A)
class _A200mprbparfsklevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(62,212))
_A200mprbparfsklevel_Type.__name__=_B
_A200mprbparfsklevel_Object=MibTableColumn
a200mprbparfsklevel=_A200mprbparfsklevel_Object((1,3,6,1,4,1,3902,1015,5200,3,3,9,1,28),_A200mprbparfsklevel_Type())
a200mprbparfsklevel.setMaxAccess(_C)
if mibBuilder.loadTexts:a200mprbparfsklevel.setStatus(_A)
class _A200mprbpardtmfcidelec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,630))
_A200mprbpardtmfcidelec_Type.__name__=_B
_A200mprbpardtmfcidelec_Object=MibTableColumn
a200mprbpardtmfcidelec=_A200mprbpardtmfcidelec_Object((1,3,6,1,4,1,3902,1015,5200,3,3,9,1,29),_A200mprbpardtmfcidelec_Type())
a200mprbpardtmfcidelec.setMaxAccess(_C)
if mibBuilder.loadTexts:a200mprbpardtmfcidelec.setStatus(_A)
class _A200mprbparnortppktcheck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_A200mprbparnortppktcheck_Type.__name__=_B
_A200mprbparnortppktcheck_Object=MibTableColumn
a200mprbparnortppktcheck=_A200mprbparnortppktcheck_Object((1,3,6,1,4,1,3902,1015,5200,3,3,9,1,30),_A200mprbparnortppktcheck_Type())
a200mprbparnortppktcheck.setMaxAccess(_C)
if mibBuilder.loadTexts:a200mprbparnortppktcheck.setStatus(_A)
_ZxAnRtpStatsMgmt_ObjectIdentity=ObjectIdentity
zxAnRtpStatsMgmt=_ZxAnRtpStatsMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,3,50))
class _ZxAnRtpPerfEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_L,2)))
_ZxAnRtpPerfEnable_Type.__name__=_B
_ZxAnRtpPerfEnable_Object=MibScalar
zxAnRtpPerfEnable=_ZxAnRtpPerfEnable_Object((1,3,6,1,4,1,3902,1015,5200,3,3,50,1),_ZxAnRtpPerfEnable_Type())
zxAnRtpPerfEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnRtpPerfEnable.setStatus(_A)
_ZxAnRtpSenderPackets_Type=Counter64
_ZxAnRtpSenderPackets_Object=MibScalar
zxAnRtpSenderPackets=_ZxAnRtpSenderPackets_Object((1,3,6,1,4,1,3902,1015,5200,3,3,50,2),_ZxAnRtpSenderPackets_Type())
zxAnRtpSenderPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnRtpSenderPackets.setStatus(_A)
_ZxAnRtpSenderOctets_Type=Counter64
_ZxAnRtpSenderOctets_Object=MibScalar
zxAnRtpSenderOctets=_ZxAnRtpSenderOctets_Object((1,3,6,1,4,1,3902,1015,5200,3,3,50,3),_ZxAnRtpSenderOctets_Type())
zxAnRtpSenderOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnRtpSenderOctets.setStatus(_A)
_ZxAnRtpRcvrPackets_Type=Counter64
_ZxAnRtpRcvrPackets_Object=MibScalar
zxAnRtpRcvrPackets=_ZxAnRtpRcvrPackets_Object((1,3,6,1,4,1,3902,1015,5200,3,3,50,4),_ZxAnRtpRcvrPackets_Type())
zxAnRtpRcvrPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnRtpRcvrPackets.setStatus(_A)
_ZxAnRtpRcvrOctets_Type=Counter64
_ZxAnRtpRcvrOctets_Object=MibScalar
zxAnRtpRcvrOctets=_ZxAnRtpRcvrOctets_Object((1,3,6,1,4,1,3902,1015,5200,3,3,50,5),_ZxAnRtpRcvrOctets_Type())
zxAnRtpRcvrOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnRtpRcvrOctets.setStatus(_A)
class _ZxAnRtpRcvrAvgPacketLossRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAnRtpRcvrAvgPacketLossRate_Type.__name__=_B
_ZxAnRtpRcvrAvgPacketLossRate_Object=MibScalar
zxAnRtpRcvrAvgPacketLossRate=_ZxAnRtpRcvrAvgPacketLossRate_Object((1,3,6,1,4,1,3902,1015,5200,3,3,50,6),_ZxAnRtpRcvrAvgPacketLossRate_Type())
zxAnRtpRcvrAvgPacketLossRate.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnRtpRcvrAvgPacketLossRate.setStatus(_A)
_ZxAnRtpRcvrAvgDelay_Type=Integer32
_ZxAnRtpRcvrAvgDelay_Object=MibScalar
zxAnRtpRcvrAvgDelay=_ZxAnRtpRcvrAvgDelay_Object((1,3,6,1,4,1,3902,1015,5200,3,3,50,7),_ZxAnRtpRcvrAvgDelay_Type())
zxAnRtpRcvrAvgDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnRtpRcvrAvgDelay.setStatus(_A)
if mibBuilder.loadTexts:zxAnRtpRcvrAvgDelay.setUnits(_g)
_ZxAnRtpRcvrAvgJitter_Type=Integer32
_ZxAnRtpRcvrAvgJitter_Object=MibScalar
zxAnRtpRcvrAvgJitter=_ZxAnRtpRcvrAvgJitter_Object((1,3,6,1,4,1,3902,1015,5200,3,3,50,8),_ZxAnRtpRcvrAvgJitter_Type())
zxAnRtpRcvrAvgJitter.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnRtpRcvrAvgJitter.setStatus(_A)
if mibBuilder.loadTexts:zxAnRtpRcvrAvgJitter.setUnits(_g)
_ZxAnNarrowbandCircuitResTable_Object=MibTable
zxAnNarrowbandCircuitResTable=_ZxAnNarrowbandCircuitResTable_Object((1,3,6,1,4,1,3902,1015,5200,3,3,51))
if mibBuilder.loadTexts:zxAnNarrowbandCircuitResTable.setStatus(_A)
_ZxAnNarrowbandCircuitResEntry_Object=MibTableRow
zxAnNarrowbandCircuitResEntry=_ZxAnNarrowbandCircuitResEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,3,51,1))
zxAnNarrowbandCircuitResEntry.setIndexNames((0,_E,_h))
if mibBuilder.loadTexts:zxAnNarrowbandCircuitResEntry.setStatus(_A)
class _ZxAnCircuitType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('typeSLC',1),('typeIPS',2)))
_ZxAnCircuitType_Type.__name__=_B
_ZxAnCircuitType_Object=MibTableColumn
zxAnCircuitType=_ZxAnCircuitType_Object((1,3,6,1,4,1,3902,1015,5200,3,3,51,1,1),_ZxAnCircuitType_Type())
zxAnCircuitType.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnCircuitType.setStatus(_A)
_ZxAnCircuitTotalNum_Type=Integer32
_ZxAnCircuitTotalNum_Object=MibTableColumn
zxAnCircuitTotalNum=_ZxAnCircuitTotalNum_Object((1,3,6,1,4,1,3902,1015,5200,3,3,51,1,2),_ZxAnCircuitTotalNum_Type())
zxAnCircuitTotalNum.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnCircuitTotalNum.setStatus(_A)
_ZxAnCircuitBusyNum_Type=Integer32
_ZxAnCircuitBusyNum_Object=MibTableColumn
zxAnCircuitBusyNum=_ZxAnCircuitBusyNum_Object((1,3,6,1,4,1,3902,1015,5200,3,3,51,1,3),_ZxAnCircuitBusyNum_Type())
zxAnCircuitBusyNum.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnCircuitBusyNum.setStatus(_A)
_ZxAnCircuitIdleNum_Type=Integer32
_ZxAnCircuitIdleNum_Object=MibTableColumn
zxAnCircuitIdleNum=_ZxAnCircuitIdleNum_Object((1,3,6,1,4,1,3902,1015,5200,3,3,51,1,4),_ZxAnCircuitIdleNum_Type())
zxAnCircuitIdleNum.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnCircuitIdleNum.setStatus(_A)
_ZxAnCircuitBlockedNum_Type=Integer32
_ZxAnCircuitBlockedNum_Object=MibTableColumn
zxAnCircuitBlockedNum=_ZxAnCircuitBlockedNum_Object((1,3,6,1,4,1,3902,1015,5200,3,3,51,1,5),_ZxAnCircuitBlockedNum_Type())
zxAnCircuitBlockedNum.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnCircuitBlockedNum.setStatus(_A)
class _ZxAnCircuitOccupancy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAnCircuitOccupancy_Type.__name__=_B
_ZxAnCircuitOccupancy_Object=MibTableColumn
zxAnCircuitOccupancy=_ZxAnCircuitOccupancy_Object((1,3,6,1,4,1,3902,1015,5200,3,3,51,1,6),_ZxAnCircuitOccupancy_Type())
zxAnCircuitOccupancy.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnCircuitOccupancy.setStatus(_A)
_ZxAnSlcVoipStatsMgmt_ObjectIdentity=ObjectIdentity
zxAnSlcVoipStatsMgmt=_ZxAnSlcVoipStatsMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,3,52))
class _ZxAnSlcVoipStatsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_L,2)))
_ZxAnSlcVoipStatsEnable_Type.__name__=_B
_ZxAnSlcVoipStatsEnable_Object=MibScalar
zxAnSlcVoipStatsEnable=_ZxAnSlcVoipStatsEnable_Object((1,3,6,1,4,1,3902,1015,5200,3,3,52,1),_ZxAnSlcVoipStatsEnable_Type())
zxAnSlcVoipStatsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSlcVoipStatsEnable.setStatus(_A)
_ZxAnSlcVoipStatsTable_Object=MibTable
zxAnSlcVoipStatsTable=_ZxAnSlcVoipStatsTable_Object((1,3,6,1,4,1,3902,1015,5200,3,3,52,10))
if mibBuilder.loadTexts:zxAnSlcVoipStatsTable.setStatus(_A)
_ZxAnSlcVoipStatsEntry_Object=MibTableRow
zxAnSlcVoipStatsEntry=_ZxAnSlcVoipStatsEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,3,52,10,1))
zxAnSlcVoipStatsEntry.setIndexNames((0,_E,_i),(0,_E,_j),(0,_E,_k),(0,_E,_l))
if mibBuilder.loadTexts:zxAnSlcVoipStatsEntry.setStatus(_A)
class _ZxAnSlcVoipRack_Type(Integer32):defaultValue=1
_ZxAnSlcVoipRack_Type.__name__=_B
_ZxAnSlcVoipRack_Object=MibTableColumn
zxAnSlcVoipRack=_ZxAnSlcVoipRack_Object((1,3,6,1,4,1,3902,1015,5200,3,3,52,10,1,1),_ZxAnSlcVoipRack_Type())
zxAnSlcVoipRack.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnSlcVoipRack.setStatus(_A)
class _ZxAnSlcVoipShelf_Type(Integer32):defaultValue=1
_ZxAnSlcVoipShelf_Type.__name__=_B
_ZxAnSlcVoipShelf_Object=MibTableColumn
zxAnSlcVoipShelf=_ZxAnSlcVoipShelf_Object((1,3,6,1,4,1,3902,1015,5200,3,3,52,10,1,2),_ZxAnSlcVoipShelf_Type())
zxAnSlcVoipShelf.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnSlcVoipShelf.setStatus(_A)
class _ZxAnSlcVoipSlot_Type(Integer32):defaultValue=3
_ZxAnSlcVoipSlot_Type.__name__=_B
_ZxAnSlcVoipSlot_Object=MibTableColumn
zxAnSlcVoipSlot=_ZxAnSlcVoipSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,3,52,10,1,3),_ZxAnSlcVoipSlot_Type())
zxAnSlcVoipSlot.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnSlcVoipSlot.setStatus(_A)
class _ZxAnSlcVoipPort_Type(Integer32):defaultValue=1
_ZxAnSlcVoipPort_Type.__name__=_B
_ZxAnSlcVoipPort_Object=MibTableColumn
zxAnSlcVoipPort=_ZxAnSlcVoipPort_Object((1,3,6,1,4,1,3902,1015,5200,3,3,52,10,1,4),_ZxAnSlcVoipPort_Type())
zxAnSlcVoipPort.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnSlcVoipPort.setStatus(_A)
_ZxAnSlcVoipRtpSenderPackets_Type=Counter64
_ZxAnSlcVoipRtpSenderPackets_Object=MibTableColumn
zxAnSlcVoipRtpSenderPackets=_ZxAnSlcVoipRtpSenderPackets_Object((1,3,6,1,4,1,3902,1015,5200,3,3,52,10,1,5),_ZxAnSlcVoipRtpSenderPackets_Type())
zxAnSlcVoipRtpSenderPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSlcVoipRtpSenderPackets.setStatus(_A)
_ZxAnSlcVoipRtpRcvrPackets_Type=Counter64
_ZxAnSlcVoipRtpRcvrPackets_Object=MibTableColumn
zxAnSlcVoipRtpRcvrPackets=_ZxAnSlcVoipRtpRcvrPackets_Object((1,3,6,1,4,1,3902,1015,5200,3,3,52,10,1,6),_ZxAnSlcVoipRtpRcvrPackets_Type())
zxAnSlcVoipRtpRcvrPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSlcVoipRtpRcvrPackets.setStatus(_A)
_ZxAnSlcVoipSipIncomingCalls_Type=Counter32
_ZxAnSlcVoipSipIncomingCalls_Object=MibTableColumn
zxAnSlcVoipSipIncomingCalls=_ZxAnSlcVoipSipIncomingCalls_Object((1,3,6,1,4,1,3902,1015,5200,3,3,52,10,1,7),_ZxAnSlcVoipSipIncomingCalls_Type())
zxAnSlcVoipSipIncomingCalls.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSlcVoipSipIncomingCalls.setStatus(_A)
_ZxAnSlcVoipSipOutgoingCalls_Type=Counter32
_ZxAnSlcVoipSipOutgoingCalls_Object=MibTableColumn
zxAnSlcVoipSipOutgoingCalls=_ZxAnSlcVoipSipOutgoingCalls_Object((1,3,6,1,4,1,3902,1015,5200,3,3,52,10,1,8),_ZxAnSlcVoipSipOutgoingCalls_Type())
zxAnSlcVoipSipOutgoingCalls.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSlcVoipSipOutgoingCalls.setStatus(_A)
_ZxAnSlcVoipH248IncomingCalls_Type=Counter32
_ZxAnSlcVoipH248IncomingCalls_Object=MibTableColumn
zxAnSlcVoipH248IncomingCalls=_ZxAnSlcVoipH248IncomingCalls_Object((1,3,6,1,4,1,3902,1015,5200,3,3,52,10,1,9),_ZxAnSlcVoipH248IncomingCalls_Type())
zxAnSlcVoipH248IncomingCalls.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSlcVoipH248IncomingCalls.setStatus(_A)
_ZxAnSlcVoipH248OutgoingCalls_Type=Counter32
_ZxAnSlcVoipH248OutgoingCalls_Object=MibTableColumn
zxAnSlcVoipH248OutgoingCalls=_ZxAnSlcVoipH248OutgoingCalls_Object((1,3,6,1,4,1,3902,1015,5200,3,3,52,10,1,10),_ZxAnSlcVoipH248OutgoingCalls_Type())
zxAnSlcVoipH248OutgoingCalls.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSlcVoipH248OutgoingCalls.setStatus(_A)
class _ZxAnSlcRtpSessionRecordTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_ZxAnSlcRtpSessionRecordTime_Type.__name__=_J
_ZxAnSlcRtpSessionRecordTime_Object=MibTableColumn
zxAnSlcRtpSessionRecordTime=_ZxAnSlcRtpSessionRecordTime_Object((1,3,6,1,4,1,3902,1015,5200,3,3,52,10,1,11),_ZxAnSlcRtpSessionRecordTime_Type())
zxAnSlcRtpSessionRecordTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSlcRtpSessionRecordTime.setStatus(_A)
_ZxAnSlcRtpSessionSenderPkts_Type=Counter32
_ZxAnSlcRtpSessionSenderPkts_Object=MibTableColumn
zxAnSlcRtpSessionSenderPkts=_ZxAnSlcRtpSessionSenderPkts_Object((1,3,6,1,4,1,3902,1015,5200,3,3,52,10,1,12),_ZxAnSlcRtpSessionSenderPkts_Type())
zxAnSlcRtpSessionSenderPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSlcRtpSessionSenderPkts.setStatus(_A)
_ZxAnSlcRtpSessionRcvrPkts_Type=Counter32
_ZxAnSlcRtpSessionRcvrPkts_Object=MibTableColumn
zxAnSlcRtpSessionRcvrPkts=_ZxAnSlcRtpSessionRcvrPkts_Object((1,3,6,1,4,1,3902,1015,5200,3,3,52,10,1,13),_ZxAnSlcRtpSessionRcvrPkts_Type())
zxAnSlcRtpSessionRcvrPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSlcRtpSessionRcvrPkts.setStatus(_A)
_ZxAnSlcRtpSessionSenderOctets_Type=Counter32
_ZxAnSlcRtpSessionSenderOctets_Object=MibTableColumn
zxAnSlcRtpSessionSenderOctets=_ZxAnSlcRtpSessionSenderOctets_Object((1,3,6,1,4,1,3902,1015,5200,3,3,52,10,1,14),_ZxAnSlcRtpSessionSenderOctets_Type())
zxAnSlcRtpSessionSenderOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSlcRtpSessionSenderOctets.setStatus(_A)
_ZxAnSlcRtpSessionRcvrOctets_Type=Counter32
_ZxAnSlcRtpSessionRcvrOctets_Object=MibTableColumn
zxAnSlcRtpSessionRcvrOctets=_ZxAnSlcRtpSessionRcvrOctets_Object((1,3,6,1,4,1,3902,1015,5200,3,3,52,10,1,15),_ZxAnSlcRtpSessionRcvrOctets_Type())
zxAnSlcRtpSessionRcvrOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSlcRtpSessionRcvrOctets.setStatus(_A)
class _ZxAnSlcRtpSessionRcvrPlr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_ZxAnSlcRtpSessionRcvrPlr_Type.__name__=_B
_ZxAnSlcRtpSessionRcvrPlr_Object=MibTableColumn
zxAnSlcRtpSessionRcvrPlr=_ZxAnSlcRtpSessionRcvrPlr_Object((1,3,6,1,4,1,3902,1015,5200,3,3,52,10,1,16),_ZxAnSlcRtpSessionRcvrPlr_Type())
zxAnSlcRtpSessionRcvrPlr.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSlcRtpSessionRcvrPlr.setStatus(_A)
_ZxAnSlcRtpSessionRcvrAvgDelay_Type=Integer32
_ZxAnSlcRtpSessionRcvrAvgDelay_Object=MibTableColumn
zxAnSlcRtpSessionRcvrAvgDelay=_ZxAnSlcRtpSessionRcvrAvgDelay_Object((1,3,6,1,4,1,3902,1015,5200,3,3,52,10,1,17),_ZxAnSlcRtpSessionRcvrAvgDelay_Type())
zxAnSlcRtpSessionRcvrAvgDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSlcRtpSessionRcvrAvgDelay.setStatus(_A)
if mibBuilder.loadTexts:zxAnSlcRtpSessionRcvrAvgDelay.setUnits('milli-seconds')
_ZxAnSlcRtpSessionRcvrAvgJitter_Type=Gauge32
_ZxAnSlcRtpSessionRcvrAvgJitter_Object=MibTableColumn
zxAnSlcRtpSessionRcvrAvgJitter=_ZxAnSlcRtpSessionRcvrAvgJitter_Object((1,3,6,1,4,1,3902,1015,5200,3,3,52,10,1,18),_ZxAnSlcRtpSessionRcvrAvgJitter_Type())
zxAnSlcRtpSessionRcvrAvgJitter.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSlcRtpSessionRcvrAvgJitter.setStatus(_A)
_ZxAnSlcVoipIncomingCalls_Type=Counter32
_ZxAnSlcVoipIncomingCalls_Object=MibTableColumn
zxAnSlcVoipIncomingCalls=_ZxAnSlcVoipIncomingCalls_Object((1,3,6,1,4,1,3902,1015,5200,3,3,52,10,1,31),_ZxAnSlcVoipIncomingCalls_Type())
zxAnSlcVoipIncomingCalls.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSlcVoipIncomingCalls.setStatus(_A)
_ZxAnSlcVoipOutgoingCalls_Type=Counter32
_ZxAnSlcVoipOutgoingCalls_Object=MibTableColumn
zxAnSlcVoipOutgoingCalls=_ZxAnSlcVoipOutgoingCalls_Object((1,3,6,1,4,1,3902,1015,5200,3,3,52,10,1,32),_ZxAnSlcVoipOutgoingCalls_Type())
zxAnSlcVoipOutgoingCalls.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSlcVoipOutgoingCalls.setStatus(_A)
_ZxAnSlcVoipIncomingCallKeepTime_Type=Integer32
_ZxAnSlcVoipIncomingCallKeepTime_Object=MibTableColumn
zxAnSlcVoipIncomingCallKeepTime=_ZxAnSlcVoipIncomingCallKeepTime_Object((1,3,6,1,4,1,3902,1015,5200,3,3,52,10,1,33),_ZxAnSlcVoipIncomingCallKeepTime_Type())
zxAnSlcVoipIncomingCallKeepTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSlcVoipIncomingCallKeepTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnSlcVoipIncomingCallKeepTime.setUnits(_K)
_ZxAnSlcVoipOutgoingCallKeepTime_Type=Integer32
_ZxAnSlcVoipOutgoingCallKeepTime_Object=MibTableColumn
zxAnSlcVoipOutgoingCallKeepTime=_ZxAnSlcVoipOutgoingCallKeepTime_Object((1,3,6,1,4,1,3902,1015,5200,3,3,52,10,1,34),_ZxAnSlcVoipOutgoingCallKeepTime_Type())
zxAnSlcVoipOutgoingCallKeepTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSlcVoipOutgoingCallKeepTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnSlcVoipOutgoingCallKeepTime.setUnits(_K)
_ZxAnSlcVoipCurrInCallKeepTime_Type=Integer32
_ZxAnSlcVoipCurrInCallKeepTime_Object=MibTableColumn
zxAnSlcVoipCurrInCallKeepTime=_ZxAnSlcVoipCurrInCallKeepTime_Object((1,3,6,1,4,1,3902,1015,5200,3,3,52,10,1,35),_ZxAnSlcVoipCurrInCallKeepTime_Type())
zxAnSlcVoipCurrInCallKeepTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSlcVoipCurrInCallKeepTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnSlcVoipCurrInCallKeepTime.setUnits(_K)
_ZxAnSlcVoipCurrOutCallKeepTime_Type=Integer32
_ZxAnSlcVoipCurrOutCallKeepTime_Object=MibTableColumn
zxAnSlcVoipCurrOutCallKeepTime=_ZxAnSlcVoipCurrOutCallKeepTime_Object((1,3,6,1,4,1,3902,1015,5200,3,3,52,10,1,36),_ZxAnSlcVoipCurrOutCallKeepTime_Type())
zxAnSlcVoipCurrOutCallKeepTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSlcVoipCurrOutCallKeepTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnSlcVoipCurrOutCallKeepTime.setUnits(_K)
_ZxAnVoipResourceGlobalObjects_ObjectIdentity=ObjectIdentity
zxAnVoipResourceGlobalObjects=_ZxAnVoipResourceGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,3,1200))
class _ZxAnVoipResourceMgmtCapabilities_Type(Bits):namedValues=NamedValues(('nbPlatform',0))
_ZxAnVoipResourceMgmtCapabilities_Type.__name__='Bits'
_ZxAnVoipResourceMgmtCapabilities_Object=MibScalar
zxAnVoipResourceMgmtCapabilities=_ZxAnVoipResourceMgmtCapabilities_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1200,1),_ZxAnVoipResourceMgmtCapabilities_Type())
zxAnVoipResourceMgmtCapabilities.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnVoipResourceMgmtCapabilities.setStatus(_A)
_ZxAnToneTable_Object=MibTable
zxAnToneTable=_ZxAnToneTable_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1201))
if mibBuilder.loadTexts:zxAnToneTable.setStatus(_A)
_ZxAnToneEntry_Object=MibTableRow
zxAnToneEntry=_ZxAnToneEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1201,1))
zxAnToneEntry.setIndexNames((0,_E,_m))
if mibBuilder.loadTexts:zxAnToneEntry.setStatus(_A)
class _ZxAnToneMgId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ZxAnToneMgId_Type.__name__=_B
_ZxAnToneMgId_Object=MibTableColumn
zxAnToneMgId=_ZxAnToneMgId_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1201,1,1),_ZxAnToneMgId_Type())
zxAnToneMgId.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnToneMgId.setStatus(_A)
class _ZxAnToneFaxcngTone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_ZxAnToneFaxcngTone_Type.__name__=_B
_ZxAnToneFaxcngTone_Object=MibTableColumn
zxAnToneFaxcngTone=_ZxAnToneFaxcngTone_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1201,1,2),_ZxAnToneFaxcngTone_Type())
zxAnToneFaxcngTone.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnToneFaxcngTone.setStatus(_A)
class _ZxAnToneV21FlagsTone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_ZxAnToneV21FlagsTone_Type.__name__=_B
_ZxAnToneV21FlagsTone_Object=MibTableColumn
zxAnToneV21FlagsTone=_ZxAnToneV21FlagsTone_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1201,1,3),_ZxAnToneV21FlagsTone_Type())
zxAnToneV21FlagsTone.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnToneV21FlagsTone.setStatus(_A)
class _ZxAnToneT38FaxEnd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_ZxAnToneT38FaxEnd_Type.__name__=_B
_ZxAnToneT38FaxEnd_Object=MibTableColumn
zxAnToneT38FaxEnd=_ZxAnToneT38FaxEnd_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1201,1,4),_ZxAnToneT38FaxEnd_Type())
zxAnToneT38FaxEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnToneT38FaxEnd.setStatus(_A)
class _ZxAnToneAnsamwiTone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_ZxAnToneAnsamwiTone_Type.__name__=_B
_ZxAnToneAnsamwiTone_Object=MibTableColumn
zxAnToneAnsamwiTone=_ZxAnToneAnsamwiTone_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1201,1,5),_ZxAnToneAnsamwiTone_Type())
zxAnToneAnsamwiTone.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnToneAnsamwiTone.setStatus(_A)
class _ZxAnToneAnsamwoTone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_ZxAnToneAnsamwoTone_Type.__name__=_B
_ZxAnToneAnsamwoTone_Object=MibTableColumn
zxAnToneAnsamwoTone=_ZxAnToneAnsamwoTone_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1201,1,6),_ZxAnToneAnsamwoTone_Type())
zxAnToneAnsamwoTone.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnToneAnsamwoTone.setStatus(_A)
class _ZxAnToneAnswiTone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_ZxAnToneAnswiTone_Type.__name__=_B
_ZxAnToneAnswiTone_Object=MibTableColumn
zxAnToneAnswiTone=_ZxAnToneAnswiTone_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1201,1,7),_ZxAnToneAnswiTone_Type())
zxAnToneAnswiTone.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnToneAnswiTone.setStatus(_A)
class _ZxAnToneAnswoTone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_ZxAnToneAnswoTone_Type.__name__=_B
_ZxAnToneAnswoTone_Object=MibTableColumn
zxAnToneAnswoTone=_ZxAnToneAnswoTone_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1201,1,8),_ZxAnToneAnswoTone_Type())
zxAnToneAnswoTone.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnToneAnswoTone.setStatus(_A)
_ZxAnIpsStaticTerminationIdTable_Object=MibTable
zxAnIpsStaticTerminationIdTable=_ZxAnIpsStaticTerminationIdTable_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1202))
if mibBuilder.loadTexts:zxAnIpsStaticTerminationIdTable.setStatus(_A)
_ZxAnIpsStaticTerminationIdEntry_Object=MibTableRow
zxAnIpsStaticTerminationIdEntry=_ZxAnIpsStaticTerminationIdEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1202,1))
zxAnIpsStaticTerminationIdEntry.setIndexNames((0,_E,_n),(0,_E,_o),(0,_E,_p),(0,_E,_q),(0,_E,_r))
if mibBuilder.loadTexts:zxAnIpsStaticTerminationIdEntry.setStatus(_A)
_ZxAnIpsStaticTidRack_Type=Integer32
_ZxAnIpsStaticTidRack_Object=MibTableColumn
zxAnIpsStaticTidRack=_ZxAnIpsStaticTidRack_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1202,1,1),_ZxAnIpsStaticTidRack_Type())
zxAnIpsStaticTidRack.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnIpsStaticTidRack.setStatus(_A)
_ZxAnIpsStaticTidShelf_Type=Integer32
_ZxAnIpsStaticTidShelf_Object=MibTableColumn
zxAnIpsStaticTidShelf=_ZxAnIpsStaticTidShelf_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1202,1,2),_ZxAnIpsStaticTidShelf_Type())
zxAnIpsStaticTidShelf.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnIpsStaticTidShelf.setStatus(_A)
_ZxAnIpsStaticTidSlot_Type=Integer32
_ZxAnIpsStaticTidSlot_Object=MibTableColumn
zxAnIpsStaticTidSlot=_ZxAnIpsStaticTidSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1202,1,3),_ZxAnIpsStaticTidSlot_Type())
zxAnIpsStaticTidSlot.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnIpsStaticTidSlot.setStatus(_A)
_ZxAnIpsStaticTidSubcard_Type=Integer32
_ZxAnIpsStaticTidSubcard_Object=MibTableColumn
zxAnIpsStaticTidSubcard=_ZxAnIpsStaticTidSubcard_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1202,1,4),_ZxAnIpsStaticTidSubcard_Type())
zxAnIpsStaticTidSubcard.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnIpsStaticTidSubcard.setStatus(_A)
_ZxAnIpsStaticTidSequenceNumber_Type=Integer32
_ZxAnIpsStaticTidSequenceNumber_Object=MibTableColumn
zxAnIpsStaticTidSequenceNumber=_ZxAnIpsStaticTidSequenceNumber_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1202,1,5),_ZxAnIpsStaticTidSequenceNumber_Type())
zxAnIpsStaticTidSequenceNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnIpsStaticTidSequenceNumber.setStatus(_A)
_ZxAnIpsStaticTidOperNum_Type=Integer32
_ZxAnIpsStaticTidOperNum_Object=MibTableColumn
zxAnIpsStaticTidOperNum=_ZxAnIpsStaticTidOperNum_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1202,1,6),_ZxAnIpsStaticTidOperNum_Type())
zxAnIpsStaticTidOperNum.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnIpsStaticTidOperNum.setStatus(_A)
class _ZxAnIpsStaticTidType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('type1',1),('type2',2),('type3',3)))
_ZxAnIpsStaticTidType_Type.__name__=_B
_ZxAnIpsStaticTidType_Object=MibTableColumn
zxAnIpsStaticTidType=_ZxAnIpsStaticTidType_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1202,1,7),_ZxAnIpsStaticTidType_Type())
zxAnIpsStaticTidType.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnIpsStaticTidType.setStatus(_A)
class _ZxAnIpsStaticTidPrefix_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_ZxAnIpsStaticTidPrefix_Type.__name__=_J
_ZxAnIpsStaticTidPrefix_Object=MibTableColumn
zxAnIpsStaticTidPrefix=_ZxAnIpsStaticTidPrefix_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1202,1,8),_ZxAnIpsStaticTidPrefix_Type())
zxAnIpsStaticTidPrefix.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnIpsStaticTidPrefix.setStatus(_A)
class _ZxAnIpsStaticTidDigitLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_ZxAnIpsStaticTidDigitLength_Type.__name__=_B
_ZxAnIpsStaticTidDigitLength_Object=MibTableColumn
zxAnIpsStaticTidDigitLength=_ZxAnIpsStaticTidDigitLength_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1202,1,9),_ZxAnIpsStaticTidDigitLength_Type())
zxAnIpsStaticTidDigitLength.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnIpsStaticTidDigitLength.setStatus(_A)
class _ZxAnIpsStaticTerminationId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_ZxAnIpsStaticTerminationId_Type.__name__=_J
_ZxAnIpsStaticTerminationId_Object=MibTableColumn
zxAnIpsStaticTerminationId=_ZxAnIpsStaticTerminationId_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1202,1,10),_ZxAnIpsStaticTerminationId_Type())
zxAnIpsStaticTerminationId.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnIpsStaticTerminationId.setStatus(_A)
_ZxAnIpsStaticTidRowStatus_Type=RowStatus
_ZxAnIpsStaticTidRowStatus_Object=MibTableColumn
zxAnIpsStaticTidRowStatus=_ZxAnIpsStaticTidRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,3,1202,1,30),_ZxAnIpsStaticTidRowStatus_Type())
zxAnIpsStaticTidRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnIpsStaticTidRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'zte':zte,'zxAn':zxAn,'zxAnVoiceResourceMib':zxAnVoiceResourceMib,'zxAnVoiceMgmt':zxAnVoiceMgmt,'zxAnVoipResource':zxAnVoipResource,'a200IpsTable':a200IpsTable,'a200IpsEntry':a200IpsEntry,_N:a200ipsrackno,_O:a200ipsshelfno,_P:a200ipsslotno,_Q:a200ipsubdevno,_R:a200ipsindex,'a200ipsstatus':a200ipsstatus,'a200ipspkg':a200ipspkg,'a200ipsmuxtype':a200ipsmuxtype,'a200ipsmodmtype':a200ipsmodmtype,'a200ipslpt':a200ipslpt,'a200ipsrpt':a200ipsrpt,'a200ipslptimmin':a200ipslptimmin,'a200ipslptimmax':a200ipslptimmax,'a200ipsrptimmin':a200ipsrptimmin,'a200ipsrptimmax':a200ipsrptimmax,'a200ipstmmdtyp':a200ipstmmdtyp,'a200ipscallerid':a200ipscallerid,'a200ipsoperNum':a200ipsoperNum,'a200ipsblockoper':a200ipsblockoper,'a200ipsunblockoper':a200ipsunblockoper,'a200AsigTable':a200AsigTable,'a200AsigEntry':a200AsigEntry,_S:a200asigrackno,_T:a200asigshelfno,_U:a200asigslotno,_V:a200asigsubdevno,_W:a200asigindex,'a200asigstatus':a200asigstatus,'a200asigkind':a200asigkind,'a200asigoperNum':a200asigoperNum,'a200asigBlockOper':a200asigBlockOper,'a200asigUnblockOper':a200asigUnblockOper,'a200ConfTable':a200ConfTable,'a200ConfEntry':a200ConfEntry,_X:a200confrackno,_Y:a200confshelfno,_Z:a200confslotno,_a:a200confsubdevno,_b:a200confindex,'a200confstatus':a200confstatus,'a200confset':a200confset,'a200confgroup':a200confgroup,'a200confoperNum':a200confoperNum,'a200confblockoper':a200confblockoper,'a200confunblockoper':a200confunblockoper,'a200MprbParTable':a200MprbParTable,'a200MprbParEntry':a200MprbParEntry,_c:a200mprbparparid,'a200mprbpardtmfrelaymode':a200mprbpardtmfrelaymode,'a200mprbpardtmfpayload':a200mprbpardtmfpayload,'a200mprbpardtmfredundant':a200mprbpardtmfredundant,'a200mprbparecenable':a200mprbparecenable,'a200mprbparectaillen':a200mprbparectaillen,'a200mprbparectxf':a200mprbparectxf,'a200mprbparnlpaggress':a200mprbparnlpaggress,'a200mprbparg711redundancy':a200mprbparg711redundancy,'a200mprbparfaxmode':a200mprbparfaxmode,'a200mprbparmodemmode':a200mprbparmodemmode,'a200mprbparecmenable':a200mprbparecmenable,'a200mprbparfaxpage':a200mprbparfaxpage,'a200mprbpart30message':a200mprbpart30message,'a200mprbparspeedlimit':a200mprbparspeedlimit,'a200mprbpartcfprocedure':a200mprbpartcfprocedure,'a200mprbparfaxswtime':a200mprbparfaxswtime,'a200mprbparmindelay':a200mprbparmindelay,'a200mprbparmaxdelay':a200mprbparmaxdelay,'a200mprbparnomdelay':a200mprbparnomdelay,'a200mprbparvadvalue':a200mprbparvadvalue,'a200mprbparg723rate':a200mprbparg723rate,'a200mprbpardcfilter':a200mprbpardcfilter,'a200mprbparsilencetopcm':a200mprbparsilencetopcm,'a200mprbparpcmlaw':a200mprbparpcmlaw,'a200mprbparpcmtopkggain':a200mprbparpcmtopkggain,'a200mprbparpkgtopcmgain':a200mprbparpkgtopcmgain,'a200mprbparfsklevel':a200mprbparfsklevel,'a200mprbpardtmfcidelec':a200mprbpardtmfcidelec,'a200mprbparnortppktcheck':a200mprbparnortppktcheck,'zxAnRtpStatsMgmt':zxAnRtpStatsMgmt,'zxAnRtpPerfEnable':zxAnRtpPerfEnable,'zxAnRtpSenderPackets':zxAnRtpSenderPackets,'zxAnRtpSenderOctets':zxAnRtpSenderOctets,'zxAnRtpRcvrPackets':zxAnRtpRcvrPackets,'zxAnRtpRcvrOctets':zxAnRtpRcvrOctets,'zxAnRtpRcvrAvgPacketLossRate':zxAnRtpRcvrAvgPacketLossRate,'zxAnRtpRcvrAvgDelay':zxAnRtpRcvrAvgDelay,'zxAnRtpRcvrAvgJitter':zxAnRtpRcvrAvgJitter,'zxAnNarrowbandCircuitResTable':zxAnNarrowbandCircuitResTable,'zxAnNarrowbandCircuitResEntry':zxAnNarrowbandCircuitResEntry,_h:zxAnCircuitType,'zxAnCircuitTotalNum':zxAnCircuitTotalNum,'zxAnCircuitBusyNum':zxAnCircuitBusyNum,'zxAnCircuitIdleNum':zxAnCircuitIdleNum,'zxAnCircuitBlockedNum':zxAnCircuitBlockedNum,'zxAnCircuitOccupancy':zxAnCircuitOccupancy,'zxAnSlcVoipStatsMgmt':zxAnSlcVoipStatsMgmt,'zxAnSlcVoipStatsEnable':zxAnSlcVoipStatsEnable,'zxAnSlcVoipStatsTable':zxAnSlcVoipStatsTable,'zxAnSlcVoipStatsEntry':zxAnSlcVoipStatsEntry,_i:zxAnSlcVoipRack,_j:zxAnSlcVoipShelf,_k:zxAnSlcVoipSlot,_l:zxAnSlcVoipPort,'zxAnSlcVoipRtpSenderPackets':zxAnSlcVoipRtpSenderPackets,'zxAnSlcVoipRtpRcvrPackets':zxAnSlcVoipRtpRcvrPackets,'zxAnSlcVoipSipIncomingCalls':zxAnSlcVoipSipIncomingCalls,'zxAnSlcVoipSipOutgoingCalls':zxAnSlcVoipSipOutgoingCalls,'zxAnSlcVoipH248IncomingCalls':zxAnSlcVoipH248IncomingCalls,'zxAnSlcVoipH248OutgoingCalls':zxAnSlcVoipH248OutgoingCalls,'zxAnSlcRtpSessionRecordTime':zxAnSlcRtpSessionRecordTime,'zxAnSlcRtpSessionSenderPkts':zxAnSlcRtpSessionSenderPkts,'zxAnSlcRtpSessionRcvrPkts':zxAnSlcRtpSessionRcvrPkts,'zxAnSlcRtpSessionSenderOctets':zxAnSlcRtpSessionSenderOctets,'zxAnSlcRtpSessionRcvrOctets':zxAnSlcRtpSessionRcvrOctets,'zxAnSlcRtpSessionRcvrPlr':zxAnSlcRtpSessionRcvrPlr,'zxAnSlcRtpSessionRcvrAvgDelay':zxAnSlcRtpSessionRcvrAvgDelay,'zxAnSlcRtpSessionRcvrAvgJitter':zxAnSlcRtpSessionRcvrAvgJitter,'zxAnSlcVoipIncomingCalls':zxAnSlcVoipIncomingCalls,'zxAnSlcVoipOutgoingCalls':zxAnSlcVoipOutgoingCalls,'zxAnSlcVoipIncomingCallKeepTime':zxAnSlcVoipIncomingCallKeepTime,'zxAnSlcVoipOutgoingCallKeepTime':zxAnSlcVoipOutgoingCallKeepTime,'zxAnSlcVoipCurrInCallKeepTime':zxAnSlcVoipCurrInCallKeepTime,'zxAnSlcVoipCurrOutCallKeepTime':zxAnSlcVoipCurrOutCallKeepTime,'zxAnVoipResourceGlobalObjects':zxAnVoipResourceGlobalObjects,'zxAnVoipResourceMgmtCapabilities':zxAnVoipResourceMgmtCapabilities,'zxAnToneTable':zxAnToneTable,'zxAnToneEntry':zxAnToneEntry,_m:zxAnToneMgId,'zxAnToneFaxcngTone':zxAnToneFaxcngTone,'zxAnToneV21FlagsTone':zxAnToneV21FlagsTone,'zxAnToneT38FaxEnd':zxAnToneT38FaxEnd,'zxAnToneAnsamwiTone':zxAnToneAnsamwiTone,'zxAnToneAnsamwoTone':zxAnToneAnsamwoTone,'zxAnToneAnswiTone':zxAnToneAnswiTone,'zxAnToneAnswoTone':zxAnToneAnswoTone,'zxAnIpsStaticTerminationIdTable':zxAnIpsStaticTerminationIdTable,'zxAnIpsStaticTerminationIdEntry':zxAnIpsStaticTerminationIdEntry,_n:zxAnIpsStaticTidRack,_o:zxAnIpsStaticTidShelf,_p:zxAnIpsStaticTidSlot,_q:zxAnIpsStaticTidSubcard,_r:zxAnIpsStaticTidSequenceNumber,'zxAnIpsStaticTidOperNum':zxAnIpsStaticTidOperNum,'zxAnIpsStaticTidType':zxAnIpsStaticTidType,'zxAnIpsStaticTidPrefix':zxAnIpsStaticTidPrefix,'zxAnIpsStaticTidDigitLength':zxAnIpsStaticTidDigitLength,'zxAnIpsStaticTerminationId':zxAnIpsStaticTerminationId,'zxAnIpsStaticTidRowStatus':zxAnIpsStaticTidRowStatus})