_AG='qtechAcDot11MIBGroup'
_AF='qtechNetDot11BGEnable'
_AE='qtechNetDot11AGEnable'
_AD='qtechNetDot11BAMPDU'
_AC='qtechNetDot11BMCS15'
_AB='qtechNetDot11BMCS14'
_AA='qtechNetDot11BMCS13'
_A9='qtechNetDot11BMCS12'
_A8='qtechNetDot11BMCS11'
_A7='qtechNetDot11BMCS10'
_A6='qtechNetDot11BMCS9'
_A5='qtechNetDot11BMCS8'
_A4='qtechNetDot11BMCS7'
_A3='qtechNetDot11BMCS6'
_A2='qtechNetDot11BMCS5'
_A1='qtechNetDot11BMCS4'
_A0='qtechNetDot11BMCS3'
_z='qtechNetDot11BMCS2'
_y='qtechNetDot11BMCS1'
_x='qtechNetDot11BMCS0'
_w='qtechNetDot11BEnable'
_v='qtechNetDot11AAMPDU'
_u='qtechNetDot11AMCS15'
_t='qtechNetDot11AMCS14'
_s='qtechNetDot11AMCS13'
_r='qtechNetDot11AMCS12'
_q='qtechNetDot11AMCS11'
_p='qtechNetDot11AMCS10'
_o='qtechNetDot11AMCS9'
_n='qtechNetDot11AMCS8'
_m='qtechNetDot11AMCS7'
_l='qtechNetDot11AMCS6'
_k='qtechNetDot11AMCS5'
_j='qtechNetDot11AMCS4'
_i='qtechNetDot11AMCS3'
_h='qtechNetDot11AMCS2'
_g='qtechNetDot11AMCS1'
_f='qtechNetDot11AMCS0'
_e='qtechNetDot11AEnable'
_d='qtechWlanDot11Flow'
_c='qtechWlanDot11Window'
_b='qtechWlanDot11Enable'
_a='qtechApDot11AntenneTxB'
_Z='qtechApDot11AntenneRxB'
_Y='qtechApDot11AntenneTxA'
_X='qtechApDot11AntenneRxA'
_W='qtechApDot11ChannelWidthB'
_V='qtechApDot11ChannelWidthA'
_U='qtechApDot11PoeEnable'
_T='qtechAcDot11CountryEnable'
_S='qtechAcDot11Country'
_R='qtechAcDot11AuthTimeout'
_Q='qtechAcDot11Client'
_P='qtechAcDot11Link'
_O='qtechWlanDot11WlanId'
_N='qtechApDot11AntenneAPID'
_M='qtechApDot11ChannelAPID'
_L='qtechApDot11PoeAPID'
_K='qtechAcDot11CountryNum'
_J='qtechAcDot11ClientMac'
_I='read-only'
_H='qtechAcDot11LinkMac'
_G='DisplayString'
_F='TruthValue'
_E='not-accessible'
_D='Integer32'
_C='read-write'
_B='QTECH-AC-DOT11-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'MacAddress','PhysAddress','TextualConvention',_F)
qtechAcDot11MIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,65))
if mibBuilder.loadTexts:qtechAcDot11MIB.setRevisions(('2009-11-29 00:00',))
_QtechAcDot11MIBObjects_ObjectIdentity=ObjectIdentity
qtechAcDot11MIBObjects=_QtechAcDot11MIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,65,1))
_QtechAcDot11LinkTestStaTable_Object=MibTable
qtechAcDot11LinkTestStaTable=_QtechAcDot11LinkTestStaTable_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,1))
if mibBuilder.loadTexts:qtechAcDot11LinkTestStaTable.setStatus(_A)
_QtechAcDot11LinkTestStaEntry_Object=MibTableRow
qtechAcDot11LinkTestStaEntry=_QtechAcDot11LinkTestStaEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,1,1))
qtechAcDot11LinkTestStaEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:qtechAcDot11LinkTestStaEntry.setStatus(_A)
_QtechAcDot11LinkMac_Type=MacAddress
_QtechAcDot11LinkMac_Object=MibTableColumn
qtechAcDot11LinkMac=_QtechAcDot11LinkMac_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,1,1,1),_QtechAcDot11LinkMac_Type())
qtechAcDot11LinkMac.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechAcDot11LinkMac.setStatus(_A)
class _QtechAcDot11Link_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_QtechAcDot11Link_Type.__name__=_G
_QtechAcDot11Link_Object=MibTableColumn
qtechAcDot11Link=_QtechAcDot11Link_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,1,1,2),_QtechAcDot11Link_Type())
qtechAcDot11Link.setMaxAccess(_I)
if mibBuilder.loadTexts:qtechAcDot11Link.setStatus(_A)
_QtechAcDot11ShowClientTable_Object=MibTable
qtechAcDot11ShowClientTable=_QtechAcDot11ShowClientTable_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,2))
if mibBuilder.loadTexts:qtechAcDot11ShowClientTable.setStatus(_A)
_QtechAcDot11ShowClientEntry_Object=MibTableRow
qtechAcDot11ShowClientEntry=_QtechAcDot11ShowClientEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,2,1))
qtechAcDot11ShowClientEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:qtechAcDot11ShowClientEntry.setStatus(_A)
_QtechAcDot11ClientMac_Type=MacAddress
_QtechAcDot11ClientMac_Object=MibTableColumn
qtechAcDot11ClientMac=_QtechAcDot11ClientMac_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,2,1,1),_QtechAcDot11ClientMac_Type())
qtechAcDot11ClientMac.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechAcDot11ClientMac.setStatus(_A)
class _QtechAcDot11Client_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_QtechAcDot11Client_Type.__name__=_G
_QtechAcDot11Client_Object=MibTableColumn
qtechAcDot11Client=_QtechAcDot11Client_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,2,1,2),_QtechAcDot11Client_Type())
qtechAcDot11Client.setMaxAccess(_I)
if mibBuilder.loadTexts:qtechAcDot11Client.setStatus(_A)
_QtechAcDot11AuthTimeout_Type=Integer32
_QtechAcDot11AuthTimeout_Object=MibScalar
qtechAcDot11AuthTimeout=_QtechAcDot11AuthTimeout_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,3),_QtechAcDot11AuthTimeout_Type())
qtechAcDot11AuthTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAcDot11AuthTimeout.setStatus(_A)
_QtechAcDot11CountryTable_Object=MibTable
qtechAcDot11CountryTable=_QtechAcDot11CountryTable_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,4))
if mibBuilder.loadTexts:qtechAcDot11CountryTable.setStatus(_A)
_QtechAcDot11CountryEntry_Object=MibTableRow
qtechAcDot11CountryEntry=_QtechAcDot11CountryEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,4,1))
qtechAcDot11CountryEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:qtechAcDot11CountryEntry.setStatus(_A)
_QtechAcDot11CountryNum_Type=Integer32
_QtechAcDot11CountryNum_Object=MibTableColumn
qtechAcDot11CountryNum=_QtechAcDot11CountryNum_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,4,1,1),_QtechAcDot11CountryNum_Type())
qtechAcDot11CountryNum.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechAcDot11CountryNum.setStatus(_A)
class _QtechAcDot11Country_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_QtechAcDot11Country_Type.__name__=_G
_QtechAcDot11Country_Object=MibTableColumn
qtechAcDot11Country=_QtechAcDot11Country_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,4,1,2),_QtechAcDot11Country_Type())
qtechAcDot11Country.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAcDot11Country.setStatus(_A)
_QtechAcDot11CountryEnable_Type=TruthValue
_QtechAcDot11CountryEnable_Object=MibTableColumn
qtechAcDot11CountryEnable=_QtechAcDot11CountryEnable_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,4,1,3),_QtechAcDot11CountryEnable_Type())
qtechAcDot11CountryEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAcDot11CountryEnable.setStatus(_A)
class _QtechNetDot11AEnable_Type(TruthValue):defaultValue=1
_QtechNetDot11AEnable_Type.__name__=_F
_QtechNetDot11AEnable_Object=MibScalar
qtechNetDot11AEnable=_QtechNetDot11AEnable_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,5),_QtechNetDot11AEnable_Type())
qtechNetDot11AEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNetDot11AEnable.setStatus(_A)
_QtechNetDot11AMCS0_Type=TruthValue
_QtechNetDot11AMCS0_Object=MibScalar
qtechNetDot11AMCS0=_QtechNetDot11AMCS0_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,6),_QtechNetDot11AMCS0_Type())
qtechNetDot11AMCS0.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNetDot11AMCS0.setStatus(_A)
_QtechNetDot11AMCS1_Type=TruthValue
_QtechNetDot11AMCS1_Object=MibScalar
qtechNetDot11AMCS1=_QtechNetDot11AMCS1_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,7),_QtechNetDot11AMCS1_Type())
qtechNetDot11AMCS1.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNetDot11AMCS1.setStatus(_A)
_QtechNetDot11AMCS2_Type=TruthValue
_QtechNetDot11AMCS2_Object=MibScalar
qtechNetDot11AMCS2=_QtechNetDot11AMCS2_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,8),_QtechNetDot11AMCS2_Type())
qtechNetDot11AMCS2.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNetDot11AMCS2.setStatus(_A)
_QtechNetDot11AMCS3_Type=TruthValue
_QtechNetDot11AMCS3_Object=MibScalar
qtechNetDot11AMCS3=_QtechNetDot11AMCS3_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,9),_QtechNetDot11AMCS3_Type())
qtechNetDot11AMCS3.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNetDot11AMCS3.setStatus(_A)
_QtechNetDot11AMCS4_Type=TruthValue
_QtechNetDot11AMCS4_Object=MibScalar
qtechNetDot11AMCS4=_QtechNetDot11AMCS4_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,10),_QtechNetDot11AMCS4_Type())
qtechNetDot11AMCS4.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNetDot11AMCS4.setStatus(_A)
_QtechNetDot11AMCS5_Type=TruthValue
_QtechNetDot11AMCS5_Object=MibScalar
qtechNetDot11AMCS5=_QtechNetDot11AMCS5_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,11),_QtechNetDot11AMCS5_Type())
qtechNetDot11AMCS5.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNetDot11AMCS5.setStatus(_A)
_QtechNetDot11AMCS6_Type=TruthValue
_QtechNetDot11AMCS6_Object=MibScalar
qtechNetDot11AMCS6=_QtechNetDot11AMCS6_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,12),_QtechNetDot11AMCS6_Type())
qtechNetDot11AMCS6.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNetDot11AMCS6.setStatus(_A)
_QtechNetDot11AMCS7_Type=TruthValue
_QtechNetDot11AMCS7_Object=MibScalar
qtechNetDot11AMCS7=_QtechNetDot11AMCS7_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,13),_QtechNetDot11AMCS7_Type())
qtechNetDot11AMCS7.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNetDot11AMCS7.setStatus(_A)
_QtechNetDot11AMCS8_Type=TruthValue
_QtechNetDot11AMCS8_Object=MibScalar
qtechNetDot11AMCS8=_QtechNetDot11AMCS8_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,14),_QtechNetDot11AMCS8_Type())
qtechNetDot11AMCS8.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNetDot11AMCS8.setStatus(_A)
_QtechNetDot11AMCS9_Type=TruthValue
_QtechNetDot11AMCS9_Object=MibScalar
qtechNetDot11AMCS9=_QtechNetDot11AMCS9_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,15),_QtechNetDot11AMCS9_Type())
qtechNetDot11AMCS9.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNetDot11AMCS9.setStatus(_A)
_QtechNetDot11AMCS10_Type=TruthValue
_QtechNetDot11AMCS10_Object=MibScalar
qtechNetDot11AMCS10=_QtechNetDot11AMCS10_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,16),_QtechNetDot11AMCS10_Type())
qtechNetDot11AMCS10.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNetDot11AMCS10.setStatus(_A)
_QtechNetDot11AMCS11_Type=TruthValue
_QtechNetDot11AMCS11_Object=MibScalar
qtechNetDot11AMCS11=_QtechNetDot11AMCS11_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,17),_QtechNetDot11AMCS11_Type())
qtechNetDot11AMCS11.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNetDot11AMCS11.setStatus(_A)
_QtechNetDot11AMCS12_Type=TruthValue
_QtechNetDot11AMCS12_Object=MibScalar
qtechNetDot11AMCS12=_QtechNetDot11AMCS12_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,18),_QtechNetDot11AMCS12_Type())
qtechNetDot11AMCS12.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNetDot11AMCS12.setStatus(_A)
_QtechNetDot11AMCS13_Type=TruthValue
_QtechNetDot11AMCS13_Object=MibScalar
qtechNetDot11AMCS13=_QtechNetDot11AMCS13_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,19),_QtechNetDot11AMCS13_Type())
qtechNetDot11AMCS13.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNetDot11AMCS13.setStatus(_A)
_QtechNetDot11AMCS14_Type=TruthValue
_QtechNetDot11AMCS14_Object=MibScalar
qtechNetDot11AMCS14=_QtechNetDot11AMCS14_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,20),_QtechNetDot11AMCS14_Type())
qtechNetDot11AMCS14.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNetDot11AMCS14.setStatus(_A)
_QtechNetDot11AMCS15_Type=TruthValue
_QtechNetDot11AMCS15_Object=MibScalar
qtechNetDot11AMCS15=_QtechNetDot11AMCS15_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,21),_QtechNetDot11AMCS15_Type())
qtechNetDot11AMCS15.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNetDot11AMCS15.setStatus(_A)
class _QtechNetDot11AAMPDU_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QtechNetDot11AAMPDU_Type.__name__=_D
_QtechNetDot11AAMPDU_Object=MibScalar
qtechNetDot11AAMPDU=_QtechNetDot11AAMPDU_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,22),_QtechNetDot11AAMPDU_Type())
qtechNetDot11AAMPDU.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNetDot11AAMPDU.setStatus(_A)
class _QtechNetDot11BEnable_Type(TruthValue):defaultValue=1
_QtechNetDot11BEnable_Type.__name__=_F
_QtechNetDot11BEnable_Object=MibScalar
qtechNetDot11BEnable=_QtechNetDot11BEnable_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,23),_QtechNetDot11BEnable_Type())
qtechNetDot11BEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNetDot11BEnable.setStatus(_A)
class _QtechNetDot11BMCS0_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_QtechNetDot11BMCS0_Type.__name__=_D
_QtechNetDot11BMCS0_Object=MibScalar
qtechNetDot11BMCS0=_QtechNetDot11BMCS0_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,24),_QtechNetDot11BMCS0_Type())
qtechNetDot11BMCS0.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNetDot11BMCS0.setStatus(_A)
class _QtechNetDot11BMCS1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_QtechNetDot11BMCS1_Type.__name__=_D
_QtechNetDot11BMCS1_Object=MibScalar
qtechNetDot11BMCS1=_QtechNetDot11BMCS1_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,25),_QtechNetDot11BMCS1_Type())
qtechNetDot11BMCS1.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNetDot11BMCS1.setStatus(_A)
class _QtechNetDot11BMCS2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_QtechNetDot11BMCS2_Type.__name__=_D
_QtechNetDot11BMCS2_Object=MibScalar
qtechNetDot11BMCS2=_QtechNetDot11BMCS2_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,26),_QtechNetDot11BMCS2_Type())
qtechNetDot11BMCS2.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNetDot11BMCS2.setStatus(_A)
class _QtechNetDot11BMCS3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_QtechNetDot11BMCS3_Type.__name__=_D
_QtechNetDot11BMCS3_Object=MibScalar
qtechNetDot11BMCS3=_QtechNetDot11BMCS3_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,27),_QtechNetDot11BMCS3_Type())
qtechNetDot11BMCS3.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNetDot11BMCS3.setStatus(_A)
class _QtechNetDot11BMCS4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_QtechNetDot11BMCS4_Type.__name__=_D
_QtechNetDot11BMCS4_Object=MibScalar
qtechNetDot11BMCS4=_QtechNetDot11BMCS4_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,28),_QtechNetDot11BMCS4_Type())
qtechNetDot11BMCS4.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNetDot11BMCS4.setStatus(_A)
class _QtechNetDot11BMCS5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_QtechNetDot11BMCS5_Type.__name__=_D
_QtechNetDot11BMCS5_Object=MibScalar
qtechNetDot11BMCS5=_QtechNetDot11BMCS5_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,29),_QtechNetDot11BMCS5_Type())
qtechNetDot11BMCS5.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNetDot11BMCS5.setStatus(_A)
class _QtechNetDot11BMCS6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_QtechNetDot11BMCS6_Type.__name__=_D
_QtechNetDot11BMCS6_Object=MibScalar
qtechNetDot11BMCS6=_QtechNetDot11BMCS6_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,30),_QtechNetDot11BMCS6_Type())
qtechNetDot11BMCS6.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNetDot11BMCS6.setStatus(_A)
class _QtechNetDot11BMCS7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_QtechNetDot11BMCS7_Type.__name__=_D
_QtechNetDot11BMCS7_Object=MibScalar
qtechNetDot11BMCS7=_QtechNetDot11BMCS7_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,31),_QtechNetDot11BMCS7_Type())
qtechNetDot11BMCS7.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNetDot11BMCS7.setStatus(_A)
class _QtechNetDot11BMCS8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_QtechNetDot11BMCS8_Type.__name__=_D
_QtechNetDot11BMCS8_Object=MibScalar
qtechNetDot11BMCS8=_QtechNetDot11BMCS8_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,32),_QtechNetDot11BMCS8_Type())
qtechNetDot11BMCS8.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNetDot11BMCS8.setStatus(_A)
class _QtechNetDot11BMCS9_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_QtechNetDot11BMCS9_Type.__name__=_D
_QtechNetDot11BMCS9_Object=MibScalar
qtechNetDot11BMCS9=_QtechNetDot11BMCS9_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,33),_QtechNetDot11BMCS9_Type())
qtechNetDot11BMCS9.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNetDot11BMCS9.setStatus(_A)
class _QtechNetDot11BMCS10_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_QtechNetDot11BMCS10_Type.__name__=_D
_QtechNetDot11BMCS10_Object=MibScalar
qtechNetDot11BMCS10=_QtechNetDot11BMCS10_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,34),_QtechNetDot11BMCS10_Type())
qtechNetDot11BMCS10.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNetDot11BMCS10.setStatus(_A)
class _QtechNetDot11BMCS11_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_QtechNetDot11BMCS11_Type.__name__=_D
_QtechNetDot11BMCS11_Object=MibScalar
qtechNetDot11BMCS11=_QtechNetDot11BMCS11_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,35),_QtechNetDot11BMCS11_Type())
qtechNetDot11BMCS11.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNetDot11BMCS11.setStatus(_A)
class _QtechNetDot11BMCS12_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_QtechNetDot11BMCS12_Type.__name__=_D
_QtechNetDot11BMCS12_Object=MibScalar
qtechNetDot11BMCS12=_QtechNetDot11BMCS12_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,36),_QtechNetDot11BMCS12_Type())
qtechNetDot11BMCS12.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNetDot11BMCS12.setStatus(_A)
class _QtechNetDot11BMCS13_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_QtechNetDot11BMCS13_Type.__name__=_D
_QtechNetDot11BMCS13_Object=MibScalar
qtechNetDot11BMCS13=_QtechNetDot11BMCS13_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,37),_QtechNetDot11BMCS13_Type())
qtechNetDot11BMCS13.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNetDot11BMCS13.setStatus(_A)
class _QtechNetDot11BMCS14_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_QtechNetDot11BMCS14_Type.__name__=_D
_QtechNetDot11BMCS14_Object=MibScalar
qtechNetDot11BMCS14=_QtechNetDot11BMCS14_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,38),_QtechNetDot11BMCS14_Type())
qtechNetDot11BMCS14.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNetDot11BMCS14.setStatus(_A)
class _QtechNetDot11BMCS15_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_QtechNetDot11BMCS15_Type.__name__=_D
_QtechNetDot11BMCS15_Object=MibScalar
qtechNetDot11BMCS15=_QtechNetDot11BMCS15_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,39),_QtechNetDot11BMCS15_Type())
qtechNetDot11BMCS15.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNetDot11BMCS15.setStatus(_A)
class _QtechNetDot11BAMPDU_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QtechNetDot11BAMPDU_Type.__name__=_D
_QtechNetDot11BAMPDU_Object=MibScalar
qtechNetDot11BAMPDU=_QtechNetDot11BAMPDU_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,40),_QtechNetDot11BAMPDU_Type())
qtechNetDot11BAMPDU.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNetDot11BAMPDU.setStatus(_A)
class _QtechNetDot11AGEnable_Type(TruthValue):defaultValue=1
_QtechNetDot11AGEnable_Type.__name__=_F
_QtechNetDot11AGEnable_Object=MibScalar
qtechNetDot11AGEnable=_QtechNetDot11AGEnable_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,41),_QtechNetDot11AGEnable_Type())
qtechNetDot11AGEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNetDot11AGEnable.setStatus(_A)
class _QtechNetDot11BGEnable_Type(TruthValue):defaultValue=1
_QtechNetDot11BGEnable_Type.__name__=_F
_QtechNetDot11BGEnable_Object=MibScalar
qtechNetDot11BGEnable=_QtechNetDot11BGEnable_Object((1,3,6,1,4,1,27514,1,1,10,2,65,1,42),_QtechNetDot11BGEnable_Type())
qtechNetDot11BGEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNetDot11BGEnable.setStatus(_A)
_QtechApDot11MIBObjects_ObjectIdentity=ObjectIdentity
qtechApDot11MIBObjects=_QtechApDot11MIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,65,2))
_QtechApDot11PoeTable_Object=MibTable
qtechApDot11PoeTable=_QtechApDot11PoeTable_Object((1,3,6,1,4,1,27514,1,1,10,2,65,2,1))
if mibBuilder.loadTexts:qtechApDot11PoeTable.setStatus(_A)
_QtechApDot11PoeEntry_Object=MibTableRow
qtechApDot11PoeEntry=_QtechApDot11PoeEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,65,2,1,1))
qtechApDot11PoeEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:qtechApDot11PoeEntry.setStatus(_A)
_QtechApDot11PoeAPID_Type=TruthValue
_QtechApDot11PoeAPID_Object=MibTableColumn
qtechApDot11PoeAPID=_QtechApDot11PoeAPID_Object((1,3,6,1,4,1,27514,1,1,10,2,65,2,1,1,1),_QtechApDot11PoeAPID_Type())
qtechApDot11PoeAPID.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechApDot11PoeAPID.setStatus(_A)
_QtechApDot11PoeEnable_Type=TruthValue
_QtechApDot11PoeEnable_Object=MibTableColumn
qtechApDot11PoeEnable=_QtechApDot11PoeEnable_Object((1,3,6,1,4,1,27514,1,1,10,2,65,2,1,1,2),_QtechApDot11PoeEnable_Type())
qtechApDot11PoeEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechApDot11PoeEnable.setStatus(_A)
_QtechApDot11ChannelTable_Object=MibTable
qtechApDot11ChannelTable=_QtechApDot11ChannelTable_Object((1,3,6,1,4,1,27514,1,1,10,2,65,2,2))
if mibBuilder.loadTexts:qtechApDot11ChannelTable.setStatus(_A)
_QtechApDot11ChannelEntry_Object=MibTableRow
qtechApDot11ChannelEntry=_QtechApDot11ChannelEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,65,2,2,1))
qtechApDot11ChannelEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:qtechApDot11ChannelEntry.setStatus(_A)
_QtechApDot11ChannelAPID_Type=Integer32
_QtechApDot11ChannelAPID_Object=MibTableColumn
qtechApDot11ChannelAPID=_QtechApDot11ChannelAPID_Object((1,3,6,1,4,1,27514,1,1,10,2,65,2,2,1,1),_QtechApDot11ChannelAPID_Type())
qtechApDot11ChannelAPID.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechApDot11ChannelAPID.setStatus(_A)
class _QtechApDot11ChannelWidthA_Type(Integer32):defaultValue=20
_QtechApDot11ChannelWidthA_Type.__name__=_D
_QtechApDot11ChannelWidthA_Object=MibTableColumn
qtechApDot11ChannelWidthA=_QtechApDot11ChannelWidthA_Object((1,3,6,1,4,1,27514,1,1,10,2,65,2,2,1,2),_QtechApDot11ChannelWidthA_Type())
qtechApDot11ChannelWidthA.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechApDot11ChannelWidthA.setStatus(_A)
class _QtechApDot11ChannelWidthB_Type(Integer32):defaultValue=20
_QtechApDot11ChannelWidthB_Type.__name__=_D
_QtechApDot11ChannelWidthB_Object=MibTableColumn
qtechApDot11ChannelWidthB=_QtechApDot11ChannelWidthB_Object((1,3,6,1,4,1,27514,1,1,10,2,65,2,2,1,3),_QtechApDot11ChannelWidthB_Type())
qtechApDot11ChannelWidthB.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechApDot11ChannelWidthB.setStatus(_A)
_QtechApDot11AntenneTable_Object=MibTable
qtechApDot11AntenneTable=_QtechApDot11AntenneTable_Object((1,3,6,1,4,1,27514,1,1,10,2,65,2,3))
if mibBuilder.loadTexts:qtechApDot11AntenneTable.setStatus(_A)
_QtechApDot11AntenneEntry_Object=MibTableRow
qtechApDot11AntenneEntry=_QtechApDot11AntenneEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,65,2,3,1))
qtechApDot11AntenneEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:qtechApDot11AntenneEntry.setStatus(_A)
_QtechApDot11AntenneAPID_Type=Integer32
_QtechApDot11AntenneAPID_Object=MibTableColumn
qtechApDot11AntenneAPID=_QtechApDot11AntenneAPID_Object((1,3,6,1,4,1,27514,1,1,10,2,65,2,3,1,1),_QtechApDot11AntenneAPID_Type())
qtechApDot11AntenneAPID.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechApDot11AntenneAPID.setStatus(_A)
class _QtechApDot11AntenneRxA_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QtechApDot11AntenneRxA_Type.__name__=_D
_QtechApDot11AntenneRxA_Object=MibTableColumn
qtechApDot11AntenneRxA=_QtechApDot11AntenneRxA_Object((1,3,6,1,4,1,27514,1,1,10,2,65,2,3,1,2),_QtechApDot11AntenneRxA_Type())
qtechApDot11AntenneRxA.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechApDot11AntenneRxA.setStatus(_A)
class _QtechApDot11AntenneTxA_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QtechApDot11AntenneTxA_Type.__name__=_D
_QtechApDot11AntenneTxA_Object=MibTableColumn
qtechApDot11AntenneTxA=_QtechApDot11AntenneTxA_Object((1,3,6,1,4,1,27514,1,1,10,2,65,2,3,1,3),_QtechApDot11AntenneTxA_Type())
qtechApDot11AntenneTxA.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechApDot11AntenneTxA.setStatus(_A)
class _QtechApDot11AntenneRxB_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QtechApDot11AntenneRxB_Type.__name__=_D
_QtechApDot11AntenneRxB_Object=MibTableColumn
qtechApDot11AntenneRxB=_QtechApDot11AntenneRxB_Object((1,3,6,1,4,1,27514,1,1,10,2,65,2,3,1,4),_QtechApDot11AntenneRxB_Type())
qtechApDot11AntenneRxB.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechApDot11AntenneRxB.setStatus(_A)
class _QtechApDot11AntenneTxB_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QtechApDot11AntenneTxB_Type.__name__=_D
_QtechApDot11AntenneTxB_Object=MibTableColumn
qtechApDot11AntenneTxB=_QtechApDot11AntenneTxB_Object((1,3,6,1,4,1,27514,1,1,10,2,65,2,3,1,5),_QtechApDot11AntenneTxB_Type())
qtechApDot11AntenneTxB.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechApDot11AntenneTxB.setStatus(_A)
_QtechWlanDot11MIBObjects_ObjectIdentity=ObjectIdentity
qtechWlanDot11MIBObjects=_QtechWlanDot11MIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,65,3))
_QtechWlanDot11LoadTable_Object=MibTable
qtechWlanDot11LoadTable=_QtechWlanDot11LoadTable_Object((1,3,6,1,4,1,27514,1,1,10,2,65,3,1))
if mibBuilder.loadTexts:qtechWlanDot11LoadTable.setStatus(_A)
_QtechWlanDot11LoadTEntry_Object=MibTableRow
qtechWlanDot11LoadTEntry=_QtechWlanDot11LoadTEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,65,3,1,1))
qtechWlanDot11LoadTEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:qtechWlanDot11LoadTEntry.setStatus(_A)
_QtechWlanDot11WlanId_Type=Integer32
_QtechWlanDot11WlanId_Object=MibTableColumn
qtechWlanDot11WlanId=_QtechWlanDot11WlanId_Object((1,3,6,1,4,1,27514,1,1,10,2,65,3,1,1,1),_QtechWlanDot11WlanId_Type())
qtechWlanDot11WlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechWlanDot11WlanId.setStatus(_A)
class _QtechWlanDot11Enable_Type(TruthValue):defaultValue=2
_QtechWlanDot11Enable_Type.__name__=_F
_QtechWlanDot11Enable_Object=MibTableColumn
qtechWlanDot11Enable=_QtechWlanDot11Enable_Object((1,3,6,1,4,1,27514,1,1,10,2,65,3,1,1,2),_QtechWlanDot11Enable_Type())
qtechWlanDot11Enable.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlanDot11Enable.setStatus(_A)
class _QtechWlanDot11Window_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_QtechWlanDot11Window_Type.__name__=_D
_QtechWlanDot11Window_Object=MibTableColumn
qtechWlanDot11Window=_QtechWlanDot11Window_Object((1,3,6,1,4,1,27514,1,1,10,2,65,3,1,1,3),_QtechWlanDot11Window_Type())
qtechWlanDot11Window.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlanDot11Window.setStatus(_A)
class _QtechWlanDot11Flow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,130))
_QtechWlanDot11Flow_Type.__name__=_D
_QtechWlanDot11Flow_Object=MibTableColumn
qtechWlanDot11Flow=_QtechWlanDot11Flow_Object((1,3,6,1,4,1,27514,1,1,10,2,65,3,1,1,4),_QtechWlanDot11Flow_Type())
qtechWlanDot11Flow.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlanDot11Flow.setStatus(_A)
_QtechAcDot11MIBConformance_ObjectIdentity=ObjectIdentity
qtechAcDot11MIBConformance=_QtechAcDot11MIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,65,5))
_QtechAcDot11MIBCompliances_ObjectIdentity=ObjectIdentity
qtechAcDot11MIBCompliances=_QtechAcDot11MIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,65,5,1))
_QtechAcDot11MIBGroups_ObjectIdentity=ObjectIdentity
qtechAcDot11MIBGroups=_QtechAcDot11MIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,65,5,2))
qtechAcDot11MIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,65,5,2,1))
qtechAcDot11MIBGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF)))
if mibBuilder.loadTexts:qtechAcDot11MIBGroup.setStatus(_A)
qtechAcDot11MIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,65,5,1,1))
qtechAcDot11MIBCompliance.setObjects((_B,_AG))
if mibBuilder.loadTexts:qtechAcDot11MIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechAcDot11MIB':qtechAcDot11MIB,'qtechAcDot11MIBObjects':qtechAcDot11MIBObjects,'qtechAcDot11LinkTestStaTable':qtechAcDot11LinkTestStaTable,'qtechAcDot11LinkTestStaEntry':qtechAcDot11LinkTestStaEntry,_H:qtechAcDot11LinkMac,_P:qtechAcDot11Link,'qtechAcDot11ShowClientTable':qtechAcDot11ShowClientTable,'qtechAcDot11ShowClientEntry':qtechAcDot11ShowClientEntry,_J:qtechAcDot11ClientMac,_Q:qtechAcDot11Client,_R:qtechAcDot11AuthTimeout,'qtechAcDot11CountryTable':qtechAcDot11CountryTable,'qtechAcDot11CountryEntry':qtechAcDot11CountryEntry,_K:qtechAcDot11CountryNum,_S:qtechAcDot11Country,_T:qtechAcDot11CountryEnable,_e:qtechNetDot11AEnable,_f:qtechNetDot11AMCS0,_g:qtechNetDot11AMCS1,_h:qtechNetDot11AMCS2,_i:qtechNetDot11AMCS3,_j:qtechNetDot11AMCS4,_k:qtechNetDot11AMCS5,_l:qtechNetDot11AMCS6,_m:qtechNetDot11AMCS7,_n:qtechNetDot11AMCS8,_o:qtechNetDot11AMCS9,_p:qtechNetDot11AMCS10,_q:qtechNetDot11AMCS11,_r:qtechNetDot11AMCS12,_s:qtechNetDot11AMCS13,_t:qtechNetDot11AMCS14,_u:qtechNetDot11AMCS15,_v:qtechNetDot11AAMPDU,_w:qtechNetDot11BEnable,_x:qtechNetDot11BMCS0,_y:qtechNetDot11BMCS1,_z:qtechNetDot11BMCS2,_A0:qtechNetDot11BMCS3,_A1:qtechNetDot11BMCS4,_A2:qtechNetDot11BMCS5,_A3:qtechNetDot11BMCS6,_A4:qtechNetDot11BMCS7,_A5:qtechNetDot11BMCS8,_A6:qtechNetDot11BMCS9,_A7:qtechNetDot11BMCS10,_A8:qtechNetDot11BMCS11,_A9:qtechNetDot11BMCS12,_AA:qtechNetDot11BMCS13,_AB:qtechNetDot11BMCS14,_AC:qtechNetDot11BMCS15,_AD:qtechNetDot11BAMPDU,_AE:qtechNetDot11AGEnable,_AF:qtechNetDot11BGEnable,'qtechApDot11MIBObjects':qtechApDot11MIBObjects,'qtechApDot11PoeTable':qtechApDot11PoeTable,'qtechApDot11PoeEntry':qtechApDot11PoeEntry,_L:qtechApDot11PoeAPID,_U:qtechApDot11PoeEnable,'qtechApDot11ChannelTable':qtechApDot11ChannelTable,'qtechApDot11ChannelEntry':qtechApDot11ChannelEntry,_M:qtechApDot11ChannelAPID,_V:qtechApDot11ChannelWidthA,_W:qtechApDot11ChannelWidthB,'qtechApDot11AntenneTable':qtechApDot11AntenneTable,'qtechApDot11AntenneEntry':qtechApDot11AntenneEntry,_N:qtechApDot11AntenneAPID,_X:qtechApDot11AntenneRxA,_Y:qtechApDot11AntenneTxA,_Z:qtechApDot11AntenneRxB,_a:qtechApDot11AntenneTxB,'qtechWlanDot11MIBObjects':qtechWlanDot11MIBObjects,'qtechWlanDot11LoadTable':qtechWlanDot11LoadTable,'qtechWlanDot11LoadTEntry':qtechWlanDot11LoadTEntry,_O:qtechWlanDot11WlanId,_b:qtechWlanDot11Enable,_c:qtechWlanDot11Window,_d:qtechWlanDot11Flow,'qtechAcDot11MIBConformance':qtechAcDot11MIBConformance,'qtechAcDot11MIBCompliances':qtechAcDot11MIBCompliances,'qtechAcDot11MIBCompliance':qtechAcDot11MIBCompliance,'qtechAcDot11MIBGroups':qtechAcDot11MIBGroups,_AG:qtechAcDot11MIBGroup})