_AG='fsAcDot11MIBGroup'
_AF='fsNetDot11BGEnable'
_AE='fsNetDot11AGEnable'
_AD='fsNetDot11BAMPDU'
_AC='fsNetDot11BMCS15'
_AB='fsNetDot11BMCS14'
_AA='fsNetDot11BMCS13'
_A9='fsNetDot11BMCS12'
_A8='fsNetDot11BMCS11'
_A7='fsNetDot11BMCS10'
_A6='fsNetDot11BMCS9'
_A5='fsNetDot11BMCS8'
_A4='fsNetDot11BMCS7'
_A3='fsNetDot11BMCS6'
_A2='fsNetDot11BMCS5'
_A1='fsNetDot11BMCS4'
_A0='fsNetDot11BMCS3'
_z='fsNetDot11BMCS2'
_y='fsNetDot11BMCS1'
_x='fsNetDot11BMCS0'
_w='fsNetDot11BEnable'
_v='fsNetDot11AAMPDU'
_u='fsNetDot11AMCS15'
_t='fsNetDot11AMCS14'
_s='fsNetDot11AMCS13'
_r='fsNetDot11AMCS12'
_q='fsNetDot11AMCS11'
_p='fsNetDot11AMCS10'
_o='fsNetDot11AMCS9'
_n='fsNetDot11AMCS8'
_m='fsNetDot11AMCS7'
_l='fsNetDot11AMCS6'
_k='fsNetDot11AMCS5'
_j='fsNetDot11AMCS4'
_i='fsNetDot11AMCS3'
_h='fsNetDot11AMCS2'
_g='fsNetDot11AMCS1'
_f='fsNetDot11AMCS0'
_e='fsNetDot11AEnable'
_d='fsWlanDot11Flow'
_c='fsWlanDot11Window'
_b='fsWlanDot11Enable'
_a='fsApDot11AntenneTxB'
_Z='fsApDot11AntenneRxB'
_Y='fsApDot11AntenneTxA'
_X='fsApDot11AntenneRxA'
_W='fsApDot11ChannelWidthB'
_V='fsApDot11ChannelWidthA'
_U='fsApDot11PoeEnable'
_T='fsAcDot11CountryEnable'
_S='fsAcDot11Country'
_R='fsAcDot11AuthTimeout'
_Q='fsAcDot11Client'
_P='fsAcDot11Link'
_O='fsWlanDot11WlanId'
_N='fsApDot11AntenneAPID'
_M='fsApDot11ChannelAPID'
_L='fsApDot11PoeAPID'
_K='fsAcDot11CountryNum'
_J='fsAcDot11ClientMac'
_I='read-only'
_H='fsAcDot11LinkMac'
_G='DisplayString'
_F='TruthValue'
_E='not-accessible'
_D='Integer32'
_C='read-write'
_B='FS-AC-DOT11-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'MacAddress','PhysAddress','TextualConvention',_F)
fsAcDot11MIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,65))
if mibBuilder.loadTexts:fsAcDot11MIB.setRevisions(('2009-11-29 00:00',))
_FsAcDot11MIBObjects_ObjectIdentity=ObjectIdentity
fsAcDot11MIBObjects=_FsAcDot11MIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,65,1))
_FsAcDot11LinkTestStaTable_Object=MibTable
fsAcDot11LinkTestStaTable=_FsAcDot11LinkTestStaTable_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,1))
if mibBuilder.loadTexts:fsAcDot11LinkTestStaTable.setStatus(_A)
_FsAcDot11LinkTestStaEntry_Object=MibTableRow
fsAcDot11LinkTestStaEntry=_FsAcDot11LinkTestStaEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,1,1))
fsAcDot11LinkTestStaEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:fsAcDot11LinkTestStaEntry.setStatus(_A)
_FsAcDot11LinkMac_Type=MacAddress
_FsAcDot11LinkMac_Object=MibTableColumn
fsAcDot11LinkMac=_FsAcDot11LinkMac_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,1,1,1),_FsAcDot11LinkMac_Type())
fsAcDot11LinkMac.setMaxAccess(_E)
if mibBuilder.loadTexts:fsAcDot11LinkMac.setStatus(_A)
class _FsAcDot11Link_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FsAcDot11Link_Type.__name__=_G
_FsAcDot11Link_Object=MibTableColumn
fsAcDot11Link=_FsAcDot11Link_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,1,1,2),_FsAcDot11Link_Type())
fsAcDot11Link.setMaxAccess(_I)
if mibBuilder.loadTexts:fsAcDot11Link.setStatus(_A)
_FsAcDot11ShowClientTable_Object=MibTable
fsAcDot11ShowClientTable=_FsAcDot11ShowClientTable_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,2))
if mibBuilder.loadTexts:fsAcDot11ShowClientTable.setStatus(_A)
_FsAcDot11ShowClientEntry_Object=MibTableRow
fsAcDot11ShowClientEntry=_FsAcDot11ShowClientEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,2,1))
fsAcDot11ShowClientEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:fsAcDot11ShowClientEntry.setStatus(_A)
_FsAcDot11ClientMac_Type=MacAddress
_FsAcDot11ClientMac_Object=MibTableColumn
fsAcDot11ClientMac=_FsAcDot11ClientMac_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,2,1,1),_FsAcDot11ClientMac_Type())
fsAcDot11ClientMac.setMaxAccess(_E)
if mibBuilder.loadTexts:fsAcDot11ClientMac.setStatus(_A)
class _FsAcDot11Client_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FsAcDot11Client_Type.__name__=_G
_FsAcDot11Client_Object=MibTableColumn
fsAcDot11Client=_FsAcDot11Client_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,2,1,2),_FsAcDot11Client_Type())
fsAcDot11Client.setMaxAccess(_I)
if mibBuilder.loadTexts:fsAcDot11Client.setStatus(_A)
_FsAcDot11AuthTimeout_Type=Integer32
_FsAcDot11AuthTimeout_Object=MibScalar
fsAcDot11AuthTimeout=_FsAcDot11AuthTimeout_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,3),_FsAcDot11AuthTimeout_Type())
fsAcDot11AuthTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:fsAcDot11AuthTimeout.setStatus(_A)
_FsAcDot11CountryTable_Object=MibTable
fsAcDot11CountryTable=_FsAcDot11CountryTable_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,4))
if mibBuilder.loadTexts:fsAcDot11CountryTable.setStatus(_A)
_FsAcDot11CountryEntry_Object=MibTableRow
fsAcDot11CountryEntry=_FsAcDot11CountryEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,4,1))
fsAcDot11CountryEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:fsAcDot11CountryEntry.setStatus(_A)
_FsAcDot11CountryNum_Type=Integer32
_FsAcDot11CountryNum_Object=MibTableColumn
fsAcDot11CountryNum=_FsAcDot11CountryNum_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,4,1,1),_FsAcDot11CountryNum_Type())
fsAcDot11CountryNum.setMaxAccess(_E)
if mibBuilder.loadTexts:fsAcDot11CountryNum.setStatus(_A)
class _FsAcDot11Country_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_FsAcDot11Country_Type.__name__=_G
_FsAcDot11Country_Object=MibTableColumn
fsAcDot11Country=_FsAcDot11Country_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,4,1,2),_FsAcDot11Country_Type())
fsAcDot11Country.setMaxAccess(_C)
if mibBuilder.loadTexts:fsAcDot11Country.setStatus(_A)
_FsAcDot11CountryEnable_Type=TruthValue
_FsAcDot11CountryEnable_Object=MibTableColumn
fsAcDot11CountryEnable=_FsAcDot11CountryEnable_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,4,1,3),_FsAcDot11CountryEnable_Type())
fsAcDot11CountryEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:fsAcDot11CountryEnable.setStatus(_A)
class _FsNetDot11AEnable_Type(TruthValue):defaultValue=1
_FsNetDot11AEnable_Type.__name__=_F
_FsNetDot11AEnable_Object=MibScalar
fsNetDot11AEnable=_FsNetDot11AEnable_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,5),_FsNetDot11AEnable_Type())
fsNetDot11AEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNetDot11AEnable.setStatus(_A)
_FsNetDot11AMCS0_Type=TruthValue
_FsNetDot11AMCS0_Object=MibScalar
fsNetDot11AMCS0=_FsNetDot11AMCS0_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,6),_FsNetDot11AMCS0_Type())
fsNetDot11AMCS0.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNetDot11AMCS0.setStatus(_A)
_FsNetDot11AMCS1_Type=TruthValue
_FsNetDot11AMCS1_Object=MibScalar
fsNetDot11AMCS1=_FsNetDot11AMCS1_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,7),_FsNetDot11AMCS1_Type())
fsNetDot11AMCS1.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNetDot11AMCS1.setStatus(_A)
_FsNetDot11AMCS2_Type=TruthValue
_FsNetDot11AMCS2_Object=MibScalar
fsNetDot11AMCS2=_FsNetDot11AMCS2_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,8),_FsNetDot11AMCS2_Type())
fsNetDot11AMCS2.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNetDot11AMCS2.setStatus(_A)
_FsNetDot11AMCS3_Type=TruthValue
_FsNetDot11AMCS3_Object=MibScalar
fsNetDot11AMCS3=_FsNetDot11AMCS3_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,9),_FsNetDot11AMCS3_Type())
fsNetDot11AMCS3.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNetDot11AMCS3.setStatus(_A)
_FsNetDot11AMCS4_Type=TruthValue
_FsNetDot11AMCS4_Object=MibScalar
fsNetDot11AMCS4=_FsNetDot11AMCS4_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,10),_FsNetDot11AMCS4_Type())
fsNetDot11AMCS4.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNetDot11AMCS4.setStatus(_A)
_FsNetDot11AMCS5_Type=TruthValue
_FsNetDot11AMCS5_Object=MibScalar
fsNetDot11AMCS5=_FsNetDot11AMCS5_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,11),_FsNetDot11AMCS5_Type())
fsNetDot11AMCS5.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNetDot11AMCS5.setStatus(_A)
_FsNetDot11AMCS6_Type=TruthValue
_FsNetDot11AMCS6_Object=MibScalar
fsNetDot11AMCS6=_FsNetDot11AMCS6_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,12),_FsNetDot11AMCS6_Type())
fsNetDot11AMCS6.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNetDot11AMCS6.setStatus(_A)
_FsNetDot11AMCS7_Type=TruthValue
_FsNetDot11AMCS7_Object=MibScalar
fsNetDot11AMCS7=_FsNetDot11AMCS7_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,13),_FsNetDot11AMCS7_Type())
fsNetDot11AMCS7.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNetDot11AMCS7.setStatus(_A)
_FsNetDot11AMCS8_Type=TruthValue
_FsNetDot11AMCS8_Object=MibScalar
fsNetDot11AMCS8=_FsNetDot11AMCS8_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,14),_FsNetDot11AMCS8_Type())
fsNetDot11AMCS8.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNetDot11AMCS8.setStatus(_A)
_FsNetDot11AMCS9_Type=TruthValue
_FsNetDot11AMCS9_Object=MibScalar
fsNetDot11AMCS9=_FsNetDot11AMCS9_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,15),_FsNetDot11AMCS9_Type())
fsNetDot11AMCS9.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNetDot11AMCS9.setStatus(_A)
_FsNetDot11AMCS10_Type=TruthValue
_FsNetDot11AMCS10_Object=MibScalar
fsNetDot11AMCS10=_FsNetDot11AMCS10_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,16),_FsNetDot11AMCS10_Type())
fsNetDot11AMCS10.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNetDot11AMCS10.setStatus(_A)
_FsNetDot11AMCS11_Type=TruthValue
_FsNetDot11AMCS11_Object=MibScalar
fsNetDot11AMCS11=_FsNetDot11AMCS11_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,17),_FsNetDot11AMCS11_Type())
fsNetDot11AMCS11.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNetDot11AMCS11.setStatus(_A)
_FsNetDot11AMCS12_Type=TruthValue
_FsNetDot11AMCS12_Object=MibScalar
fsNetDot11AMCS12=_FsNetDot11AMCS12_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,18),_FsNetDot11AMCS12_Type())
fsNetDot11AMCS12.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNetDot11AMCS12.setStatus(_A)
_FsNetDot11AMCS13_Type=TruthValue
_FsNetDot11AMCS13_Object=MibScalar
fsNetDot11AMCS13=_FsNetDot11AMCS13_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,19),_FsNetDot11AMCS13_Type())
fsNetDot11AMCS13.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNetDot11AMCS13.setStatus(_A)
_FsNetDot11AMCS14_Type=TruthValue
_FsNetDot11AMCS14_Object=MibScalar
fsNetDot11AMCS14=_FsNetDot11AMCS14_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,20),_FsNetDot11AMCS14_Type())
fsNetDot11AMCS14.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNetDot11AMCS14.setStatus(_A)
_FsNetDot11AMCS15_Type=TruthValue
_FsNetDot11AMCS15_Object=MibScalar
fsNetDot11AMCS15=_FsNetDot11AMCS15_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,21),_FsNetDot11AMCS15_Type())
fsNetDot11AMCS15.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNetDot11AMCS15.setStatus(_A)
class _FsNetDot11AAMPDU_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsNetDot11AAMPDU_Type.__name__=_D
_FsNetDot11AAMPDU_Object=MibScalar
fsNetDot11AAMPDU=_FsNetDot11AAMPDU_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,22),_FsNetDot11AAMPDU_Type())
fsNetDot11AAMPDU.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNetDot11AAMPDU.setStatus(_A)
class _FsNetDot11BEnable_Type(TruthValue):defaultValue=1
_FsNetDot11BEnable_Type.__name__=_F
_FsNetDot11BEnable_Object=MibScalar
fsNetDot11BEnable=_FsNetDot11BEnable_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,23),_FsNetDot11BEnable_Type())
fsNetDot11BEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNetDot11BEnable.setStatus(_A)
class _FsNetDot11BMCS0_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_FsNetDot11BMCS0_Type.__name__=_D
_FsNetDot11BMCS0_Object=MibScalar
fsNetDot11BMCS0=_FsNetDot11BMCS0_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,24),_FsNetDot11BMCS0_Type())
fsNetDot11BMCS0.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNetDot11BMCS0.setStatus(_A)
class _FsNetDot11BMCS1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_FsNetDot11BMCS1_Type.__name__=_D
_FsNetDot11BMCS1_Object=MibScalar
fsNetDot11BMCS1=_FsNetDot11BMCS1_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,25),_FsNetDot11BMCS1_Type())
fsNetDot11BMCS1.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNetDot11BMCS1.setStatus(_A)
class _FsNetDot11BMCS2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_FsNetDot11BMCS2_Type.__name__=_D
_FsNetDot11BMCS2_Object=MibScalar
fsNetDot11BMCS2=_FsNetDot11BMCS2_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,26),_FsNetDot11BMCS2_Type())
fsNetDot11BMCS2.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNetDot11BMCS2.setStatus(_A)
class _FsNetDot11BMCS3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_FsNetDot11BMCS3_Type.__name__=_D
_FsNetDot11BMCS3_Object=MibScalar
fsNetDot11BMCS3=_FsNetDot11BMCS3_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,27),_FsNetDot11BMCS3_Type())
fsNetDot11BMCS3.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNetDot11BMCS3.setStatus(_A)
class _FsNetDot11BMCS4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_FsNetDot11BMCS4_Type.__name__=_D
_FsNetDot11BMCS4_Object=MibScalar
fsNetDot11BMCS4=_FsNetDot11BMCS4_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,28),_FsNetDot11BMCS4_Type())
fsNetDot11BMCS4.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNetDot11BMCS4.setStatus(_A)
class _FsNetDot11BMCS5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_FsNetDot11BMCS5_Type.__name__=_D
_FsNetDot11BMCS5_Object=MibScalar
fsNetDot11BMCS5=_FsNetDot11BMCS5_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,29),_FsNetDot11BMCS5_Type())
fsNetDot11BMCS5.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNetDot11BMCS5.setStatus(_A)
class _FsNetDot11BMCS6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_FsNetDot11BMCS6_Type.__name__=_D
_FsNetDot11BMCS6_Object=MibScalar
fsNetDot11BMCS6=_FsNetDot11BMCS6_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,30),_FsNetDot11BMCS6_Type())
fsNetDot11BMCS6.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNetDot11BMCS6.setStatus(_A)
class _FsNetDot11BMCS7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_FsNetDot11BMCS7_Type.__name__=_D
_FsNetDot11BMCS7_Object=MibScalar
fsNetDot11BMCS7=_FsNetDot11BMCS7_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,31),_FsNetDot11BMCS7_Type())
fsNetDot11BMCS7.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNetDot11BMCS7.setStatus(_A)
class _FsNetDot11BMCS8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_FsNetDot11BMCS8_Type.__name__=_D
_FsNetDot11BMCS8_Object=MibScalar
fsNetDot11BMCS8=_FsNetDot11BMCS8_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,32),_FsNetDot11BMCS8_Type())
fsNetDot11BMCS8.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNetDot11BMCS8.setStatus(_A)
class _FsNetDot11BMCS9_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_FsNetDot11BMCS9_Type.__name__=_D
_FsNetDot11BMCS9_Object=MibScalar
fsNetDot11BMCS9=_FsNetDot11BMCS9_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,33),_FsNetDot11BMCS9_Type())
fsNetDot11BMCS9.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNetDot11BMCS9.setStatus(_A)
class _FsNetDot11BMCS10_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_FsNetDot11BMCS10_Type.__name__=_D
_FsNetDot11BMCS10_Object=MibScalar
fsNetDot11BMCS10=_FsNetDot11BMCS10_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,34),_FsNetDot11BMCS10_Type())
fsNetDot11BMCS10.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNetDot11BMCS10.setStatus(_A)
class _FsNetDot11BMCS11_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_FsNetDot11BMCS11_Type.__name__=_D
_FsNetDot11BMCS11_Object=MibScalar
fsNetDot11BMCS11=_FsNetDot11BMCS11_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,35),_FsNetDot11BMCS11_Type())
fsNetDot11BMCS11.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNetDot11BMCS11.setStatus(_A)
class _FsNetDot11BMCS12_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_FsNetDot11BMCS12_Type.__name__=_D
_FsNetDot11BMCS12_Object=MibScalar
fsNetDot11BMCS12=_FsNetDot11BMCS12_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,36),_FsNetDot11BMCS12_Type())
fsNetDot11BMCS12.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNetDot11BMCS12.setStatus(_A)
class _FsNetDot11BMCS13_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_FsNetDot11BMCS13_Type.__name__=_D
_FsNetDot11BMCS13_Object=MibScalar
fsNetDot11BMCS13=_FsNetDot11BMCS13_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,37),_FsNetDot11BMCS13_Type())
fsNetDot11BMCS13.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNetDot11BMCS13.setStatus(_A)
class _FsNetDot11BMCS14_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_FsNetDot11BMCS14_Type.__name__=_D
_FsNetDot11BMCS14_Object=MibScalar
fsNetDot11BMCS14=_FsNetDot11BMCS14_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,38),_FsNetDot11BMCS14_Type())
fsNetDot11BMCS14.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNetDot11BMCS14.setStatus(_A)
class _FsNetDot11BMCS15_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_FsNetDot11BMCS15_Type.__name__=_D
_FsNetDot11BMCS15_Object=MibScalar
fsNetDot11BMCS15=_FsNetDot11BMCS15_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,39),_FsNetDot11BMCS15_Type())
fsNetDot11BMCS15.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNetDot11BMCS15.setStatus(_A)
class _FsNetDot11BAMPDU_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsNetDot11BAMPDU_Type.__name__=_D
_FsNetDot11BAMPDU_Object=MibScalar
fsNetDot11BAMPDU=_FsNetDot11BAMPDU_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,40),_FsNetDot11BAMPDU_Type())
fsNetDot11BAMPDU.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNetDot11BAMPDU.setStatus(_A)
class _FsNetDot11AGEnable_Type(TruthValue):defaultValue=1
_FsNetDot11AGEnable_Type.__name__=_F
_FsNetDot11AGEnable_Object=MibScalar
fsNetDot11AGEnable=_FsNetDot11AGEnable_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,41),_FsNetDot11AGEnable_Type())
fsNetDot11AGEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNetDot11AGEnable.setStatus(_A)
class _FsNetDot11BGEnable_Type(TruthValue):defaultValue=1
_FsNetDot11BGEnable_Type.__name__=_F
_FsNetDot11BGEnable_Object=MibScalar
fsNetDot11BGEnable=_FsNetDot11BGEnable_Object((1,3,6,1,4,1,52642,1,1,10,2,65,1,42),_FsNetDot11BGEnable_Type())
fsNetDot11BGEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNetDot11BGEnable.setStatus(_A)
_FsApDot11MIBObjects_ObjectIdentity=ObjectIdentity
fsApDot11MIBObjects=_FsApDot11MIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,65,2))
_FsApDot11PoeTable_Object=MibTable
fsApDot11PoeTable=_FsApDot11PoeTable_Object((1,3,6,1,4,1,52642,1,1,10,2,65,2,1))
if mibBuilder.loadTexts:fsApDot11PoeTable.setStatus(_A)
_FsApDot11PoeEntry_Object=MibTableRow
fsApDot11PoeEntry=_FsApDot11PoeEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,65,2,1,1))
fsApDot11PoeEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:fsApDot11PoeEntry.setStatus(_A)
_FsApDot11PoeAPID_Type=TruthValue
_FsApDot11PoeAPID_Object=MibTableColumn
fsApDot11PoeAPID=_FsApDot11PoeAPID_Object((1,3,6,1,4,1,52642,1,1,10,2,65,2,1,1,1),_FsApDot11PoeAPID_Type())
fsApDot11PoeAPID.setMaxAccess(_E)
if mibBuilder.loadTexts:fsApDot11PoeAPID.setStatus(_A)
_FsApDot11PoeEnable_Type=TruthValue
_FsApDot11PoeEnable_Object=MibTableColumn
fsApDot11PoeEnable=_FsApDot11PoeEnable_Object((1,3,6,1,4,1,52642,1,1,10,2,65,2,1,1,2),_FsApDot11PoeEnable_Type())
fsApDot11PoeEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:fsApDot11PoeEnable.setStatus(_A)
_FsApDot11ChannelTable_Object=MibTable
fsApDot11ChannelTable=_FsApDot11ChannelTable_Object((1,3,6,1,4,1,52642,1,1,10,2,65,2,2))
if mibBuilder.loadTexts:fsApDot11ChannelTable.setStatus(_A)
_FsApDot11ChannelEntry_Object=MibTableRow
fsApDot11ChannelEntry=_FsApDot11ChannelEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,65,2,2,1))
fsApDot11ChannelEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:fsApDot11ChannelEntry.setStatus(_A)
_FsApDot11ChannelAPID_Type=Integer32
_FsApDot11ChannelAPID_Object=MibTableColumn
fsApDot11ChannelAPID=_FsApDot11ChannelAPID_Object((1,3,6,1,4,1,52642,1,1,10,2,65,2,2,1,1),_FsApDot11ChannelAPID_Type())
fsApDot11ChannelAPID.setMaxAccess(_E)
if mibBuilder.loadTexts:fsApDot11ChannelAPID.setStatus(_A)
class _FsApDot11ChannelWidthA_Type(Integer32):defaultValue=20
_FsApDot11ChannelWidthA_Type.__name__=_D
_FsApDot11ChannelWidthA_Object=MibTableColumn
fsApDot11ChannelWidthA=_FsApDot11ChannelWidthA_Object((1,3,6,1,4,1,52642,1,1,10,2,65,2,2,1,2),_FsApDot11ChannelWidthA_Type())
fsApDot11ChannelWidthA.setMaxAccess(_C)
if mibBuilder.loadTexts:fsApDot11ChannelWidthA.setStatus(_A)
class _FsApDot11ChannelWidthB_Type(Integer32):defaultValue=20
_FsApDot11ChannelWidthB_Type.__name__=_D
_FsApDot11ChannelWidthB_Object=MibTableColumn
fsApDot11ChannelWidthB=_FsApDot11ChannelWidthB_Object((1,3,6,1,4,1,52642,1,1,10,2,65,2,2,1,3),_FsApDot11ChannelWidthB_Type())
fsApDot11ChannelWidthB.setMaxAccess(_C)
if mibBuilder.loadTexts:fsApDot11ChannelWidthB.setStatus(_A)
_FsApDot11AntenneTable_Object=MibTable
fsApDot11AntenneTable=_FsApDot11AntenneTable_Object((1,3,6,1,4,1,52642,1,1,10,2,65,2,3))
if mibBuilder.loadTexts:fsApDot11AntenneTable.setStatus(_A)
_FsApDot11AntenneEntry_Object=MibTableRow
fsApDot11AntenneEntry=_FsApDot11AntenneEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,65,2,3,1))
fsApDot11AntenneEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:fsApDot11AntenneEntry.setStatus(_A)
_FsApDot11AntenneAPID_Type=Integer32
_FsApDot11AntenneAPID_Object=MibTableColumn
fsApDot11AntenneAPID=_FsApDot11AntenneAPID_Object((1,3,6,1,4,1,52642,1,1,10,2,65,2,3,1,1),_FsApDot11AntenneAPID_Type())
fsApDot11AntenneAPID.setMaxAccess(_E)
if mibBuilder.loadTexts:fsApDot11AntenneAPID.setStatus(_A)
class _FsApDot11AntenneRxA_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsApDot11AntenneRxA_Type.__name__=_D
_FsApDot11AntenneRxA_Object=MibTableColumn
fsApDot11AntenneRxA=_FsApDot11AntenneRxA_Object((1,3,6,1,4,1,52642,1,1,10,2,65,2,3,1,2),_FsApDot11AntenneRxA_Type())
fsApDot11AntenneRxA.setMaxAccess(_C)
if mibBuilder.loadTexts:fsApDot11AntenneRxA.setStatus(_A)
class _FsApDot11AntenneTxA_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsApDot11AntenneTxA_Type.__name__=_D
_FsApDot11AntenneTxA_Object=MibTableColumn
fsApDot11AntenneTxA=_FsApDot11AntenneTxA_Object((1,3,6,1,4,1,52642,1,1,10,2,65,2,3,1,3),_FsApDot11AntenneTxA_Type())
fsApDot11AntenneTxA.setMaxAccess(_C)
if mibBuilder.loadTexts:fsApDot11AntenneTxA.setStatus(_A)
class _FsApDot11AntenneRxB_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsApDot11AntenneRxB_Type.__name__=_D
_FsApDot11AntenneRxB_Object=MibTableColumn
fsApDot11AntenneRxB=_FsApDot11AntenneRxB_Object((1,3,6,1,4,1,52642,1,1,10,2,65,2,3,1,4),_FsApDot11AntenneRxB_Type())
fsApDot11AntenneRxB.setMaxAccess(_C)
if mibBuilder.loadTexts:fsApDot11AntenneRxB.setStatus(_A)
class _FsApDot11AntenneTxB_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsApDot11AntenneTxB_Type.__name__=_D
_FsApDot11AntenneTxB_Object=MibTableColumn
fsApDot11AntenneTxB=_FsApDot11AntenneTxB_Object((1,3,6,1,4,1,52642,1,1,10,2,65,2,3,1,5),_FsApDot11AntenneTxB_Type())
fsApDot11AntenneTxB.setMaxAccess(_C)
if mibBuilder.loadTexts:fsApDot11AntenneTxB.setStatus(_A)
_FsWlanDot11MIBObjects_ObjectIdentity=ObjectIdentity
fsWlanDot11MIBObjects=_FsWlanDot11MIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,65,3))
_FsWlanDot11LoadTable_Object=MibTable
fsWlanDot11LoadTable=_FsWlanDot11LoadTable_Object((1,3,6,1,4,1,52642,1,1,10,2,65,3,1))
if mibBuilder.loadTexts:fsWlanDot11LoadTable.setStatus(_A)
_FsWlanDot11LoadTEntry_Object=MibTableRow
fsWlanDot11LoadTEntry=_FsWlanDot11LoadTEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,65,3,1,1))
fsWlanDot11LoadTEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:fsWlanDot11LoadTEntry.setStatus(_A)
_FsWlanDot11WlanId_Type=Integer32
_FsWlanDot11WlanId_Object=MibTableColumn
fsWlanDot11WlanId=_FsWlanDot11WlanId_Object((1,3,6,1,4,1,52642,1,1,10,2,65,3,1,1,1),_FsWlanDot11WlanId_Type())
fsWlanDot11WlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsWlanDot11WlanId.setStatus(_A)
class _FsWlanDot11Enable_Type(TruthValue):defaultValue=2
_FsWlanDot11Enable_Type.__name__=_F
_FsWlanDot11Enable_Object=MibTableColumn
fsWlanDot11Enable=_FsWlanDot11Enable_Object((1,3,6,1,4,1,52642,1,1,10,2,65,3,1,1,2),_FsWlanDot11Enable_Type())
fsWlanDot11Enable.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWlanDot11Enable.setStatus(_A)
class _FsWlanDot11Window_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_FsWlanDot11Window_Type.__name__=_D
_FsWlanDot11Window_Object=MibTableColumn
fsWlanDot11Window=_FsWlanDot11Window_Object((1,3,6,1,4,1,52642,1,1,10,2,65,3,1,1,3),_FsWlanDot11Window_Type())
fsWlanDot11Window.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWlanDot11Window.setStatus(_A)
class _FsWlanDot11Flow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,130))
_FsWlanDot11Flow_Type.__name__=_D
_FsWlanDot11Flow_Object=MibTableColumn
fsWlanDot11Flow=_FsWlanDot11Flow_Object((1,3,6,1,4,1,52642,1,1,10,2,65,3,1,1,4),_FsWlanDot11Flow_Type())
fsWlanDot11Flow.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWlanDot11Flow.setStatus(_A)
_FsAcDot11MIBConformance_ObjectIdentity=ObjectIdentity
fsAcDot11MIBConformance=_FsAcDot11MIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,65,5))
_FsAcDot11MIBCompliances_ObjectIdentity=ObjectIdentity
fsAcDot11MIBCompliances=_FsAcDot11MIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,65,5,1))
_FsAcDot11MIBGroups_ObjectIdentity=ObjectIdentity
fsAcDot11MIBGroups=_FsAcDot11MIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,65,5,2))
fsAcDot11MIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,65,5,2,1))
fsAcDot11MIBGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF)))
if mibBuilder.loadTexts:fsAcDot11MIBGroup.setStatus(_A)
fsAcDot11MIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,65,5,1,1))
fsAcDot11MIBCompliance.setObjects((_B,_AG))
if mibBuilder.loadTexts:fsAcDot11MIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsAcDot11MIB':fsAcDot11MIB,'fsAcDot11MIBObjects':fsAcDot11MIBObjects,'fsAcDot11LinkTestStaTable':fsAcDot11LinkTestStaTable,'fsAcDot11LinkTestStaEntry':fsAcDot11LinkTestStaEntry,_H:fsAcDot11LinkMac,_P:fsAcDot11Link,'fsAcDot11ShowClientTable':fsAcDot11ShowClientTable,'fsAcDot11ShowClientEntry':fsAcDot11ShowClientEntry,_J:fsAcDot11ClientMac,_Q:fsAcDot11Client,_R:fsAcDot11AuthTimeout,'fsAcDot11CountryTable':fsAcDot11CountryTable,'fsAcDot11CountryEntry':fsAcDot11CountryEntry,_K:fsAcDot11CountryNum,_S:fsAcDot11Country,_T:fsAcDot11CountryEnable,_e:fsNetDot11AEnable,_f:fsNetDot11AMCS0,_g:fsNetDot11AMCS1,_h:fsNetDot11AMCS2,_i:fsNetDot11AMCS3,_j:fsNetDot11AMCS4,_k:fsNetDot11AMCS5,_l:fsNetDot11AMCS6,_m:fsNetDot11AMCS7,_n:fsNetDot11AMCS8,_o:fsNetDot11AMCS9,_p:fsNetDot11AMCS10,_q:fsNetDot11AMCS11,_r:fsNetDot11AMCS12,_s:fsNetDot11AMCS13,_t:fsNetDot11AMCS14,_u:fsNetDot11AMCS15,_v:fsNetDot11AAMPDU,_w:fsNetDot11BEnable,_x:fsNetDot11BMCS0,_y:fsNetDot11BMCS1,_z:fsNetDot11BMCS2,_A0:fsNetDot11BMCS3,_A1:fsNetDot11BMCS4,_A2:fsNetDot11BMCS5,_A3:fsNetDot11BMCS6,_A4:fsNetDot11BMCS7,_A5:fsNetDot11BMCS8,_A6:fsNetDot11BMCS9,_A7:fsNetDot11BMCS10,_A8:fsNetDot11BMCS11,_A9:fsNetDot11BMCS12,_AA:fsNetDot11BMCS13,_AB:fsNetDot11BMCS14,_AC:fsNetDot11BMCS15,_AD:fsNetDot11BAMPDU,_AE:fsNetDot11AGEnable,_AF:fsNetDot11BGEnable,'fsApDot11MIBObjects':fsApDot11MIBObjects,'fsApDot11PoeTable':fsApDot11PoeTable,'fsApDot11PoeEntry':fsApDot11PoeEntry,_L:fsApDot11PoeAPID,_U:fsApDot11PoeEnable,'fsApDot11ChannelTable':fsApDot11ChannelTable,'fsApDot11ChannelEntry':fsApDot11ChannelEntry,_M:fsApDot11ChannelAPID,_V:fsApDot11ChannelWidthA,_W:fsApDot11ChannelWidthB,'fsApDot11AntenneTable':fsApDot11AntenneTable,'fsApDot11AntenneEntry':fsApDot11AntenneEntry,_N:fsApDot11AntenneAPID,_X:fsApDot11AntenneRxA,_Y:fsApDot11AntenneTxA,_Z:fsApDot11AntenneRxB,_a:fsApDot11AntenneTxB,'fsWlanDot11MIBObjects':fsWlanDot11MIBObjects,'fsWlanDot11LoadTable':fsWlanDot11LoadTable,'fsWlanDot11LoadTEntry':fsWlanDot11LoadTEntry,_O:fsWlanDot11WlanId,_b:fsWlanDot11Enable,_c:fsWlanDot11Window,_d:fsWlanDot11Flow,'fsAcDot11MIBConformance':fsAcDot11MIBConformance,'fsAcDot11MIBCompliances':fsAcDot11MIBCompliances,'fsAcDot11MIBCompliance':fsAcDot11MIBCompliance,'fsAcDot11MIBGroups':fsAcDot11MIBGroups,_AG:fsAcDot11MIBGroup})