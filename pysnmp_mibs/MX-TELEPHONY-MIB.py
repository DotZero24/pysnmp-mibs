_A5='telephonyGroupVer1'
_A4='telephonySpecificCountrySelectionTable'
_A3='telephonyCountrySelection'
_A2='telephonyIpSignalingProtocolProprietary'
_A1='telephonyIpSignalingProtocolSelection'
_A0='countryCustomizationTonePerPortTone'
_z='stutter'
_y='ringback'
_x='reorder'
_w='preemption'
_v='messageWaiting'
_u='intercept'
_t='congestion'
_s='confirmation'
_r='countryCustomizationToneTone'
_q='ifIndex'
_p='austria2-etsi-fsk'
_o='austria-etsi-fsk'
_n='france-etsi-dtmf'
_m='france-etsi-fsk'
_l='uk-etsi-fsk'
_k='uk-cca'
_j='uk-bellcore'
_i='southAfrica'
_h='chile2'
_g='chile1'
_f='czechRepublic'
_e='germany3'
_d='austria2'
_c='newZealand'
_b='australia3'
_a='denmark'
_Z='mexico'
_Y='brazil'
_X='netherlands'
_W='russia'
_V='malaysia'
_U='hongKong'
_T='australia2'
_S='indonesia'
_R='thailand'
_Q='israel'
_P='australia1'
_O='sweden'
_N='switzerland'
_M='germany2'
_L='germany1'
_K='france'
_J='austria'
_I='northAmerica2'
_H='northAmerica1'
_G='read-only'
_F='MxEnableState'
_E='OctetString'
_D='Integer32'
_C='read-write'
_B='MX-TELEPHONY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixConfig,=mibBuilder.importSymbols('MX-SMI','mediatrixConfig')
MxEnableState,=mibBuilder.importSymbols('MX-TC',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
telephonyMIB=ModuleIdentity((1,3,6,1,4,1,4935,15,25))
if mibBuilder.loadTexts:telephonyMIB.setRevisions(('2012-07-03 00:00','2012-06-08 00:00','2010-01-18 00:00','2007-11-13 00:00','2007-08-06 00:00','2007-04-18 00:00','2007-03-21 00:00','2007-01-03 00:00','2006-04-28 00:00','2005-09-28 00:00','2004-11-12 00:00','2004-08-03 00:00','2004-08-02 00:00','2004-07-21 00:00','2004-07-14 00:00','2004-06-15 00:00','2003-10-20 00:00','2003-08-15 00:00','2003-07-03 00:00','2003-06-06 00:00','2003-05-01 00:00','2003-01-13 00:00','2003-01-14 00:00','2002-11-25 00:00','2002-10-09 00:00','2002-03-29 00:00','2001-11-05 00:00','2001-08-29 00:00'))
_TelephonyMIBObjects_ObjectIdentity=ObjectIdentity
telephonyMIBObjects=_TelephonyMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,15,25,1))
class _TelephonyIpSignalingProtocolSelection_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,99)));namedValues=NamedValues(*(('mgcp',1),('sip',2),('ncs',3),('h323',4),('proprietary',99)))
_TelephonyIpSignalingProtocolSelection_Type.__name__=_D
_TelephonyIpSignalingProtocolSelection_Object=MibScalar
telephonyIpSignalingProtocolSelection=_TelephonyIpSignalingProtocolSelection_Object((1,3,6,1,4,1,4935,15,25,1,3),_TelephonyIpSignalingProtocolSelection_Type())
telephonyIpSignalingProtocolSelection.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyIpSignalingProtocolSelection.setStatus(_A)
class _TelephonyIpSignalingProtocolProprietary_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_TelephonyIpSignalingProtocolProprietary_Type.__name__=_E
_TelephonyIpSignalingProtocolProprietary_Object=MibScalar
telephonyIpSignalingProtocolProprietary=_TelephonyIpSignalingProtocolProprietary_Object((1,3,6,1,4,1,4935,15,25,1,4),_TelephonyIpSignalingProtocolProprietary_Type())
telephonyIpSignalingProtocolProprietary.setMaxAccess(_G)
if mibBuilder.loadTexts:telephonyIpSignalingProtocolProprietary.setStatus(_A)
class _TelephonyCountrySelection_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,100,101,102,110,111,120,130)));namedValues=NamedValues(*((_H,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6),('uk',7),('italy',8),('spain',9),(_N,10),(_O,11),(_P,12),('japan',13),(_Q,14),(_R,15),(_S,16),(_T,17),('china',18),(_U,19),(_V,20),(_W,21),(_X,22),(_Y,23),('uae',24),(_Z,25),(_a,26),(_b,27),(_c,28),(_d,29),(_e,30),(_f,31),(_g,32),(_h,33),('uae2',34),(_i,35),(_j,100),(_k,101),(_l,102),(_m,110),(_n,111),(_o,120),(_p,130)))
_TelephonyCountrySelection_Type.__name__=_D
_TelephonyCountrySelection_Object=MibScalar
telephonyCountrySelection=_TelephonyCountrySelection_Object((1,3,6,1,4,1,4935,15,25,1,6),_TelephonyCountrySelection_Type())
telephonyCountrySelection.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyCountrySelection.setStatus(_A)
_TelephonySpecificCountrySelectionTable_Object=MibTable
telephonySpecificCountrySelectionTable=_TelephonySpecificCountrySelectionTable_Object((1,3,6,1,4,1,4935,15,25,1,10))
if mibBuilder.loadTexts:telephonySpecificCountrySelectionTable.setStatus(_A)
_TelephonySpecificCountrySelectionEntry_Object=MibTableRow
telephonySpecificCountrySelectionEntry=_TelephonySpecificCountrySelectionEntry_Object((1,3,6,1,4,1,4935,15,25,1,10,1))
telephonySpecificCountrySelectionEntry.setIndexNames((0,_B,_q))
if mibBuilder.loadTexts:telephonySpecificCountrySelectionEntry.setStatus(_A)
class _TelephonySpecificCountrySelectionEnableConfig_Type(MxEnableState):defaultValue=0
_TelephonySpecificCountrySelectionEnableConfig_Type.__name__=_F
_TelephonySpecificCountrySelectionEnableConfig_Object=MibTableColumn
telephonySpecificCountrySelectionEnableConfig=_TelephonySpecificCountrySelectionEnableConfig_Object((1,3,6,1,4,1,4935,15,25,1,10,1,10),_TelephonySpecificCountrySelectionEnableConfig_Type())
telephonySpecificCountrySelectionEnableConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonySpecificCountrySelectionEnableConfig.setStatus(_A)
class _TelephonySpecificCountrySelectionCountry_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,100,101,102,110,111,120,130)));namedValues=NamedValues(*((_H,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6),('uk',7),('italy',8),('spain',9),(_N,10),(_O,11),(_P,12),('japan',13),(_Q,14),(_R,15),(_S,16),(_T,17),('china',18),(_U,19),(_V,20),(_W,21),(_X,22),(_Y,23),('uae',24),(_Z,25),(_a,26),(_b,27),(_c,28),(_d,29),(_e,30),(_f,31),(_g,32),(_h,33),('uae2',34),(_i,35),(_j,100),(_k,101),(_l,102),(_m,110),(_n,111),(_o,120),(_p,130)))
_TelephonySpecificCountrySelectionCountry_Type.__name__=_D
_TelephonySpecificCountrySelectionCountry_Object=MibTableColumn
telephonySpecificCountrySelectionCountry=_TelephonySpecificCountrySelectionCountry_Object((1,3,6,1,4,1,4935,15,25,1,10,1,20),_TelephonySpecificCountrySelectionCountry_Type())
telephonySpecificCountrySelectionCountry.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonySpecificCountrySelectionCountry.setStatus(_A)
_CountryCustomizationToneGroup_ObjectIdentity=ObjectIdentity
countryCustomizationToneGroup=_CountryCustomizationToneGroup_ObjectIdentity((1,3,6,1,4,1,4935,15,25,1,500))
_CountryCustomizationToneTable_Object=MibTable
countryCustomizationToneTable=_CountryCustomizationToneTable_Object((1,3,6,1,4,1,4935,15,25,1,500,200))
if mibBuilder.loadTexts:countryCustomizationToneTable.setStatus(_A)
_CountryCustomizationToneEntry_Object=MibTableRow
countryCustomizationToneEntry=_CountryCustomizationToneEntry_Object((1,3,6,1,4,1,4935,15,25,1,500,200,1))
countryCustomizationToneEntry.setIndexNames((0,_B,_r))
if mibBuilder.loadTexts:countryCustomizationToneEntry.setStatus(_A)
class _CountryCustomizationToneTone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,600,700,800,900,1000,1100,1200,1300)));namedValues=NamedValues(*(('busy',100),(_s,200),(_t,300),('dial',400),(_u,600),(_v,700),(_w,800),(_x,900),(_y,1000),('roh',1100),('sit',1200),(_z,1300)))
_CountryCustomizationToneTone_Type.__name__=_D
_CountryCustomizationToneTone_Object=MibTableColumn
countryCustomizationToneTone=_CountryCustomizationToneTone_Object((1,3,6,1,4,1,4935,15,25,1,500,200,1,100),_CountryCustomizationToneTone_Type())
countryCustomizationToneTone.setMaxAccess(_G)
if mibBuilder.loadTexts:countryCustomizationToneTone.setStatus(_A)
class _CountryCustomizationToneOverride_Type(MxEnableState):defaultValue=0
_CountryCustomizationToneOverride_Type.__name__=_F
_CountryCustomizationToneOverride_Object=MibTableColumn
countryCustomizationToneOverride=_CountryCustomizationToneOverride_Object((1,3,6,1,4,1,4935,15,25,1,500,200,1,200),_CountryCustomizationToneOverride_Type())
countryCustomizationToneOverride.setMaxAccess(_C)
if mibBuilder.loadTexts:countryCustomizationToneOverride.setStatus(_A)
class _CountryCustomizationTonePattern_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_CountryCustomizationTonePattern_Type.__name__=_E
_CountryCustomizationTonePattern_Object=MibTableColumn
countryCustomizationTonePattern=_CountryCustomizationTonePattern_Object((1,3,6,1,4,1,4935,15,25,1,500,200,1,300),_CountryCustomizationTonePattern_Type())
countryCustomizationTonePattern.setMaxAccess(_C)
if mibBuilder.loadTexts:countryCustomizationTonePattern.setStatus(_A)
_CountryCustomizationTonePerPortTable_Object=MibTable
countryCustomizationTonePerPortTable=_CountryCustomizationTonePerPortTable_Object((1,3,6,1,4,1,4935,15,25,1,500,300))
if mibBuilder.loadTexts:countryCustomizationTonePerPortTable.setStatus(_A)
_CountryCustomizationTonePerPortEntry_Object=MibTableRow
countryCustomizationTonePerPortEntry=_CountryCustomizationTonePerPortEntry_Object((1,3,6,1,4,1,4935,15,25,1,500,300,1))
countryCustomizationTonePerPortEntry.setIndexNames((0,_B,_q),(0,_B,_A0))
if mibBuilder.loadTexts:countryCustomizationTonePerPortEntry.setStatus(_A)
class _CountryCustomizationTonePerPortTone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,600,700,800,900,1000,1100,1200,1300)));namedValues=NamedValues(*(('busy',100),(_s,200),(_t,300),('dial',400),(_u,600),(_v,700),(_w,800),(_x,900),(_y,1000),('roh',1100),('sit',1200),(_z,1300)))
_CountryCustomizationTonePerPortTone_Type.__name__=_D
_CountryCustomizationTonePerPortTone_Object=MibTableColumn
countryCustomizationTonePerPortTone=_CountryCustomizationTonePerPortTone_Object((1,3,6,1,4,1,4935,15,25,1,500,300,1,100),_CountryCustomizationTonePerPortTone_Type())
countryCustomizationTonePerPortTone.setMaxAccess(_G)
if mibBuilder.loadTexts:countryCustomizationTonePerPortTone.setStatus(_A)
class _CountryCustomizationTonePerPortOverride_Type(MxEnableState):defaultValue=0
_CountryCustomizationTonePerPortOverride_Type.__name__=_F
_CountryCustomizationTonePerPortOverride_Object=MibTableColumn
countryCustomizationTonePerPortOverride=_CountryCustomizationTonePerPortOverride_Object((1,3,6,1,4,1,4935,15,25,1,500,300,1,200),_CountryCustomizationTonePerPortOverride_Type())
countryCustomizationTonePerPortOverride.setMaxAccess(_C)
if mibBuilder.loadTexts:countryCustomizationTonePerPortOverride.setStatus(_A)
class _CountryCustomizationTonePerPortPattern_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_CountryCustomizationTonePerPortPattern_Type.__name__=_E
_CountryCustomizationTonePerPortPattern_Object=MibTableColumn
countryCustomizationTonePerPortPattern=_CountryCustomizationTonePerPortPattern_Object((1,3,6,1,4,1,4935,15,25,1,500,300,1,300),_CountryCustomizationTonePerPortPattern_Type())
countryCustomizationTonePerPortPattern.setMaxAccess(_C)
if mibBuilder.loadTexts:countryCustomizationTonePerPortPattern.setStatus(_A)
_TelephonyConformance_ObjectIdentity=ObjectIdentity
telephonyConformance=_TelephonyConformance_ObjectIdentity((1,3,6,1,4,1,4935,15,25,2))
_TelephonyCompliances_ObjectIdentity=ObjectIdentity
telephonyCompliances=_TelephonyCompliances_ObjectIdentity((1,3,6,1,4,1,4935,15,25,2,1))
_TelephonyGroups_ObjectIdentity=ObjectIdentity
telephonyGroups=_TelephonyGroups_ObjectIdentity((1,3,6,1,4,1,4935,15,25,2,2))
telephonyGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,25,2,2,1))
telephonyGroupVer1.setObjects(*((_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:telephonyGroupVer1.setStatus(_A)
telephonyComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,15,25,2,1,1))
telephonyComplVer1.setObjects((_B,_A5))
if mibBuilder.loadTexts:telephonyComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'telephonyMIB':telephonyMIB,'telephonyMIBObjects':telephonyMIBObjects,_A1:telephonyIpSignalingProtocolSelection,_A2:telephonyIpSignalingProtocolProprietary,_A3:telephonyCountrySelection,_A4:telephonySpecificCountrySelectionTable,'telephonySpecificCountrySelectionEntry':telephonySpecificCountrySelectionEntry,'telephonySpecificCountrySelectionEnableConfig':telephonySpecificCountrySelectionEnableConfig,'telephonySpecificCountrySelectionCountry':telephonySpecificCountrySelectionCountry,'countryCustomizationToneGroup':countryCustomizationToneGroup,'countryCustomizationToneTable':countryCustomizationToneTable,'countryCustomizationToneEntry':countryCustomizationToneEntry,_r:countryCustomizationToneTone,'countryCustomizationToneOverride':countryCustomizationToneOverride,'countryCustomizationTonePattern':countryCustomizationTonePattern,'countryCustomizationTonePerPortTable':countryCustomizationTonePerPortTable,'countryCustomizationTonePerPortEntry':countryCustomizationTonePerPortEntry,_A0:countryCustomizationTonePerPortTone,'countryCustomizationTonePerPortOverride':countryCustomizationTonePerPortOverride,'countryCustomizationTonePerPortPattern':countryCustomizationTonePerPortPattern,'telephonyConformance':telephonyConformance,'telephonyCompliances':telephonyCompliances,'telephonyComplVer1':telephonyComplVer1,'telephonyGroups':telephonyGroups,_A5:telephonyGroupVer1})