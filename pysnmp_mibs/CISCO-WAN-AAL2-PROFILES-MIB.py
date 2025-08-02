_V='aal2ProfileGroup'
_U='aal2ProfileVBDPktPeriod'
_T='aal2ProfileVBDCodec'
_S='aal2ProfileVoiceVAD'
_R='aal2ProfileVoicePktPeriod'
_Q='aal2ProfileVoiceCodec'
_P='aal2ProfilePreference'
_O='milli seconds'
_N='thirty'
_M='lossless'
_L='g726r40000'
_K='g726r24000'
_J='g726r16000'
_I='clearChannel'
_H='g726r32000'
_G='not-accessible'
_F='aal2ProfileNumber'
_E='aal2ProfileType'
_D='read-write'
_C='Integer32'
_B='CISCO-WAN-AAL2-PROFILES-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoWanAal2ProfilesMIB=ModuleIdentity((1,3,6,1,4,1,351,150,17))
if mibBuilder.loadTexts:ciscoWanAal2ProfilesMIB.setRevisions(('2005-09-01 00:00','2004-04-09 00:00','2003-10-10 00:00','2003-08-14 00:00','2003-05-23 00:00','2001-09-10 00:00','2001-08-24 15:00','2001-01-19 15:00'))
_CiscoWanAal2ProfilesMIBObjects_ObjectIdentity=ObjectIdentity
ciscoWanAal2ProfilesMIBObjects=_CiscoWanAal2ProfilesMIBObjects_ObjectIdentity((1,3,6,1,4,1,351,150,17,1))
_Aal2ProfilesGrp_ObjectIdentity=ObjectIdentity
aal2ProfilesGrp=_Aal2ProfilesGrp_ObjectIdentity((1,3,6,1,4,1,351,150,17,1,1))
_Aal2ProfilesGrpTable_Object=MibTable
aal2ProfilesGrpTable=_Aal2ProfilesGrpTable_Object((1,3,6,1,4,1,351,150,17,1,1,1))
if mibBuilder.loadTexts:aal2ProfilesGrpTable.setStatus(_A)
_Aal2ProfilesGrpEntry_Object=MibTableRow
aal2ProfilesGrpEntry=_Aal2ProfilesGrpEntry_Object((1,3,6,1,4,1,351,150,17,1,1,1,1))
aal2ProfilesGrpEntry.setIndexNames((0,_B,_E),(0,_B,_F))
if mibBuilder.loadTexts:aal2ProfilesGrpEntry.setStatus(_A)
class _Aal2ProfileType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3)));namedValues=NamedValues(*(('itu',1),('custom',3)))
_Aal2ProfileType_Type.__name__=_C
_Aal2ProfileType_Object=MibTableColumn
aal2ProfileType=_Aal2ProfileType_Object((1,3,6,1,4,1,351,150,17,1,1,1,1,1),_Aal2ProfileType_Type())
aal2ProfileType.setMaxAccess(_G)
if mibBuilder.loadTexts:aal2ProfileType.setStatus(_A)
class _Aal2ProfileNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,7,8,12,100,101,110,200,201,210)));namedValues=NamedValues(*(('one',1),('two',2),('three',3),('seven',7),('eight',8),('twelve',12),('oneHundred',100),('oneHundredOne',101),('oneHundredTen',110),('twoHundred',200),('twoHundredOne',201),('twoHundredTen',210)))
_Aal2ProfileNumber_Type.__name__=_C
_Aal2ProfileNumber_Object=MibTableColumn
aal2ProfileNumber=_Aal2ProfileNumber_Object((1,3,6,1,4,1,351,150,17,1,1,1,1,2),_Aal2ProfileNumber_Type())
aal2ProfileNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:aal2ProfileNumber.setStatus(_A)
class _Aal2ProfilePreference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Aal2ProfilePreference_Type.__name__=_C
_Aal2ProfilePreference_Object=MibTableColumn
aal2ProfilePreference=_Aal2ProfilePreference_Object((1,3,6,1,4,1,351,150,17,1,1,1,1,3),_Aal2ProfilePreference_Type())
aal2ProfilePreference.setMaxAccess(_D)
if mibBuilder.loadTexts:aal2ProfilePreference.setStatus(_A)
class _Aal2ProfileVoiceCodec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,11,12,13,14,15)));namedValues=NamedValues(*(('g711u',1),('g711a',2),(_H,3),('g729a',4),('g729ab',5),(_I,6),(_J,7),(_K,8),(_L,9),('g723h',11),('g723ah',12),('g723l',13),('g723al',14),(_M,15)))
_Aal2ProfileVoiceCodec_Type.__name__=_C
_Aal2ProfileVoiceCodec_Object=MibTableColumn
aal2ProfileVoiceCodec=_Aal2ProfileVoiceCodec_Object((1,3,6,1,4,1,351,150,17,1,1,1,1,4),_Aal2ProfileVoiceCodec_Type())
aal2ProfileVoiceCodec.setMaxAccess(_D)
if mibBuilder.loadTexts:aal2ProfileVoiceCodec.setStatus(_A)
class _Aal2ProfileVoicePktPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5,10,20,30,40)));namedValues=NamedValues(*(('five',5),('ten',10),('twenty',20),(_N,30),('fourty',40)))
_Aal2ProfileVoicePktPeriod_Type.__name__=_C
_Aal2ProfileVoicePktPeriod_Object=MibTableColumn
aal2ProfileVoicePktPeriod=_Aal2ProfileVoicePktPeriod_Object((1,3,6,1,4,1,351,150,17,1,1,1,1,5),_Aal2ProfileVoicePktPeriod_Type())
aal2ProfileVoicePktPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:aal2ProfileVoicePktPeriod.setStatus(_A)
if mibBuilder.loadTexts:aal2ProfileVoicePktPeriod.setUnits(_O)
class _Aal2ProfileVoiceVAD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('off',1),('on',2),('sidGenric',3),('sid729',4),('sid723',5)))
_Aal2ProfileVoiceVAD_Type.__name__=_C
_Aal2ProfileVoiceVAD_Object=MibTableColumn
aal2ProfileVoiceVAD=_Aal2ProfileVoiceVAD_Object((1,3,6,1,4,1,351,150,17,1,1,1,1,6),_Aal2ProfileVoiceVAD_Type())
aal2ProfileVoiceVAD.setMaxAccess(_D)
if mibBuilder.loadTexts:aal2ProfileVoiceVAD.setStatus(_A)
class _Aal2ProfileVBDCodec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,6,7,8,9,11,13,15)));namedValues=NamedValues(*(('g711u',1),('g711a',2),(_H,3),(_I,6),(_J,7),(_K,8),(_L,9),('g723h',11),('g723l',13),(_M,15)))
_Aal2ProfileVBDCodec_Type.__name__=_C
_Aal2ProfileVBDCodec_Object=MibTableColumn
aal2ProfileVBDCodec=_Aal2ProfileVBDCodec_Object((1,3,6,1,4,1,351,150,17,1,1,1,1,7),_Aal2ProfileVBDCodec_Type())
aal2ProfileVBDCodec.setMaxAccess(_D)
if mibBuilder.loadTexts:aal2ProfileVBDCodec.setStatus(_A)
class _Aal2ProfileVBDPktPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5,10,30)));namedValues=NamedValues(*(('five',5),('ten',10),(_N,30)))
_Aal2ProfileVBDPktPeriod_Type.__name__=_C
_Aal2ProfileVBDPktPeriod_Object=MibTableColumn
aal2ProfileVBDPktPeriod=_Aal2ProfileVBDPktPeriod_Object((1,3,6,1,4,1,351,150,17,1,1,1,1,8),_Aal2ProfileVBDPktPeriod_Type())
aal2ProfileVBDPktPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:aal2ProfileVBDPktPeriod.setStatus(_A)
if mibBuilder.loadTexts:aal2ProfileVBDPktPeriod.setUnits(_O)
_Aal2ProfileMIBConformance_ObjectIdentity=ObjectIdentity
aal2ProfileMIBConformance=_Aal2ProfileMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,17,2))
_Aal2ProfileMIBCompliances_ObjectIdentity=ObjectIdentity
aal2ProfileMIBCompliances=_Aal2ProfileMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,17,2,1))
_Aal2ProfileMIBGroups_ObjectIdentity=ObjectIdentity
aal2ProfileMIBGroups=_Aal2ProfileMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,17,2,2))
aal2ProfileGroup=ObjectGroup((1,3,6,1,4,1,351,150,17,2,2,1))
aal2ProfileGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:aal2ProfileGroup.setStatus(_A)
aal2ProfileMIBCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,17,2,1,1))
aal2ProfileMIBCompliance.setObjects((_B,_V))
if mibBuilder.loadTexts:aal2ProfileMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoWanAal2ProfilesMIB':ciscoWanAal2ProfilesMIB,'ciscoWanAal2ProfilesMIBObjects':ciscoWanAal2ProfilesMIBObjects,'aal2ProfilesGrp':aal2ProfilesGrp,'aal2ProfilesGrpTable':aal2ProfilesGrpTable,'aal2ProfilesGrpEntry':aal2ProfilesGrpEntry,_E:aal2ProfileType,_F:aal2ProfileNumber,_P:aal2ProfilePreference,_Q:aal2ProfileVoiceCodec,_R:aal2ProfileVoicePktPeriod,_S:aal2ProfileVoiceVAD,_T:aal2ProfileVBDCodec,_U:aal2ProfileVBDPktPeriod,'aal2ProfileMIBConformance':aal2ProfileMIBConformance,'aal2ProfileMIBCompliances':aal2ProfileMIBCompliances,'aal2ProfileMIBCompliance':aal2ProfileMIBCompliance,'aal2ProfileMIBGroups':aal2ProfileMIBGroups,_V:aal2ProfileGroup})