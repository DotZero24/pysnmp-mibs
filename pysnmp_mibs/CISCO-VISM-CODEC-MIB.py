_U='ciscoAltVismCodecCnfGroup'
_T='vismAltCodecString3'
_S='vismAltCodecString2'
_R='vismAltCodecString1'
_Q='vismCodecTemplateMaxChanCount'
_P='vismCodecSupported'
_O='vismCodecIanaType'
_N='vismCodecString'
_M='vismCodecPreference'
_L='vismCodecPktPeriod'
_K='vismCodecName'
_J='ciscoVismCodecTemplateGrp'
_I='ciscoVismCodecCnfGroup'
_H='vismCodecCnfIndex'
_G='vismCodecTemplateNum'
_F='read-only'
_E='SnmpAdminString'
_D='read-write'
_C='Integer32'
_B='CISCO-VISM-CODEC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
voice,=mibBuilder.importSymbols('BASIS-MIB','voice')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoVismCodecMIB=ModuleIdentity((1,3,6,1,4,1,351,150,97))
if mibBuilder.loadTexts:ciscoVismCodecMIB.setRevisions(('2005-05-24 00:00','2004-01-07 00:00'))
_VismCodecTemplateCnfGrp_ObjectIdentity=ObjectIdentity
vismCodecTemplateCnfGrp=_VismCodecTemplateCnfGrp_ObjectIdentity((1,3,6,1,4,1,351,110,5,5,7))
_VismCodecTemplateCnfGrpTable_Object=MibTable
vismCodecTemplateCnfGrpTable=_VismCodecTemplateCnfGrpTable_Object((1,3,6,1,4,1,351,110,5,5,7,1))
if mibBuilder.loadTexts:vismCodecTemplateCnfGrpTable.setStatus(_A)
_VismCodecTemplateCnfGrpEntry_Object=MibTableRow
vismCodecTemplateCnfGrpEntry=_VismCodecTemplateCnfGrpEntry_Object((1,3,6,1,4,1,351,110,5,5,7,1,1))
vismCodecTemplateCnfGrpEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:vismCodecTemplateCnfGrpEntry.setStatus(_A)
class _VismCodecTemplateNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_VismCodecTemplateNum_Type.__name__=_C
_VismCodecTemplateNum_Object=MibTableColumn
vismCodecTemplateNum=_VismCodecTemplateNum_Object((1,3,6,1,4,1,351,110,5,5,7,1,1,1),_VismCodecTemplateNum_Type())
vismCodecTemplateNum.setMaxAccess(_F)
if mibBuilder.loadTexts:vismCodecTemplateNum.setStatus(_A)
class _VismCodecSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VismCodecSupported_Type.__name__=_C
_VismCodecSupported_Object=MibTableColumn
vismCodecSupported=_VismCodecSupported_Object((1,3,6,1,4,1,351,110,5,5,7,1,1,2),_VismCodecSupported_Type())
vismCodecSupported.setMaxAccess(_F)
if mibBuilder.loadTexts:vismCodecSupported.setStatus(_A)
class _VismCodecTemplateMaxChanCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VismCodecTemplateMaxChanCount_Type.__name__=_C
_VismCodecTemplateMaxChanCount_Object=MibTableColumn
vismCodecTemplateMaxChanCount=_VismCodecTemplateMaxChanCount_Object((1,3,6,1,4,1,351,110,5,5,7,1,1,3),_VismCodecTemplateMaxChanCount_Type())
vismCodecTemplateMaxChanCount.setMaxAccess(_F)
if mibBuilder.loadTexts:vismCodecTemplateMaxChanCount.setStatus(_A)
_VismCodecCnfGrp_ObjectIdentity=ObjectIdentity
vismCodecCnfGrp=_VismCodecCnfGrp_ObjectIdentity((1,3,6,1,4,1,351,110,5,5,18))
_VismCodecCnfTable_Object=MibTable
vismCodecCnfTable=_VismCodecCnfTable_Object((1,3,6,1,4,1,351,110,5,5,18,1))
if mibBuilder.loadTexts:vismCodecCnfTable.setStatus(_A)
_VismCodecCnfEntry_Object=MibTableRow
vismCodecCnfEntry=_VismCodecCnfEntry_Object((1,3,6,1,4,1,351,110,5,5,18,1,1))
vismCodecCnfEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:vismCodecCnfEntry.setStatus(_A)
class _VismCodecCnfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,11,12,13,14,15)));namedValues=NamedValues(*(('g711u',1),('g711a',2),('g726r32000',3),('g729a',4),('g729ab',5),('clearChannel',6),('g726r16000',7),('g726r24000',8),('g726r40000',9),('g723h',11),('g723ah',12),('g723l',13),('g723al',14),('lossless',15)))
_VismCodecCnfIndex_Type.__name__=_C
_VismCodecCnfIndex_Object=MibTableColumn
vismCodecCnfIndex=_VismCodecCnfIndex_Object((1,3,6,1,4,1,351,110,5,5,18,1,1,1),_VismCodecCnfIndex_Type())
vismCodecCnfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:vismCodecCnfIndex.setStatus(_A)
class _VismCodecName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_VismCodecName_Type.__name__=_E
_VismCodecName_Object=MibTableColumn
vismCodecName=_VismCodecName_Object((1,3,6,1,4,1,351,110,5,5,18,1,1,2),_VismCodecName_Type())
vismCodecName.setMaxAccess(_F)
if mibBuilder.loadTexts:vismCodecName.setStatus(_A)
class _VismCodecPktPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(10,20,30,40,60)));namedValues=NamedValues(*(('ten',10),('twenty',20),('thirty',30),('fourty',40),('sixty',60)))
_VismCodecPktPeriod_Type.__name__=_C
_VismCodecPktPeriod_Object=MibTableColumn
vismCodecPktPeriod=_VismCodecPktPeriod_Object((1,3,6,1,4,1,351,110,5,5,18,1,1,3),_VismCodecPktPeriod_Type())
vismCodecPktPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:vismCodecPktPeriod.setStatus(_A)
if mibBuilder.loadTexts:vismCodecPktPeriod.setUnits('milliseconds')
class _VismCodecPreference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VismCodecPreference_Type.__name__=_C
_VismCodecPreference_Object=MibTableColumn
vismCodecPreference=_VismCodecPreference_Object((1,3,6,1,4,1,351,110,5,5,18,1,1,4),_VismCodecPreference_Type())
vismCodecPreference.setMaxAccess(_D)
if mibBuilder.loadTexts:vismCodecPreference.setStatus(_A)
class _VismCodecString_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_VismCodecString_Type.__name__=_E
_VismCodecString_Object=MibTableColumn
vismCodecString=_VismCodecString_Object((1,3,6,1,4,1,351,110,5,5,18,1,1,5),_VismCodecString_Type())
vismCodecString.setMaxAccess(_D)
if mibBuilder.loadTexts:vismCodecString.setStatus(_A)
class _VismCodecIanaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_VismCodecIanaType_Type.__name__=_C
_VismCodecIanaType_Object=MibTableColumn
vismCodecIanaType=_VismCodecIanaType_Object((1,3,6,1,4,1,351,110,5,5,18,1,1,6),_VismCodecIanaType_Type())
vismCodecIanaType.setMaxAccess(_D)
if mibBuilder.loadTexts:vismCodecIanaType.setStatus(_A)
class _VismAltCodecString1_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_VismAltCodecString1_Type.__name__=_E
_VismAltCodecString1_Object=MibTableColumn
vismAltCodecString1=_VismAltCodecString1_Object((1,3,6,1,4,1,351,110,5,5,18,1,1,7),_VismAltCodecString1_Type())
vismAltCodecString1.setMaxAccess(_D)
if mibBuilder.loadTexts:vismAltCodecString1.setStatus(_A)
class _VismAltCodecString2_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_VismAltCodecString2_Type.__name__=_E
_VismAltCodecString2_Object=MibTableColumn
vismAltCodecString2=_VismAltCodecString2_Object((1,3,6,1,4,1,351,110,5,5,18,1,1,8),_VismAltCodecString2_Type())
vismAltCodecString2.setMaxAccess(_D)
if mibBuilder.loadTexts:vismAltCodecString2.setStatus(_A)
class _VismAltCodecString3_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_VismAltCodecString3_Type.__name__=_E
_VismAltCodecString3_Object=MibTableColumn
vismAltCodecString3=_VismAltCodecString3_Object((1,3,6,1,4,1,351,110,5,5,18,1,1,9),_VismAltCodecString3_Type())
vismAltCodecString3.setMaxAccess(_D)
if mibBuilder.loadTexts:vismAltCodecString3.setStatus(_A)
_CiscoVismCodecMIBConformance_ObjectIdentity=ObjectIdentity
ciscoVismCodecMIBConformance=_CiscoVismCodecMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,97,2))
_CiscoVismCodecMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoVismCodecMIBCompliances=_CiscoVismCodecMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,97,2,1))
_CiscoVismCodecMIBGroups_ObjectIdentity=ObjectIdentity
ciscoVismCodecMIBGroups=_CiscoVismCodecMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,97,2,2))
ciscoVismCodecCnfGroup=ObjectGroup((1,3,6,1,4,1,351,150,97,2,2,1))
ciscoVismCodecCnfGroup.setObjects(*((_B,_H),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:ciscoVismCodecCnfGroup.setStatus(_A)
ciscoVismCodecTemplateGrp=ObjectGroup((1,3,6,1,4,1,351,150,97,2,2,2))
ciscoVismCodecTemplateGrp.setObjects(*((_B,_G),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:ciscoVismCodecTemplateGrp.setStatus(_A)
ciscoAltVismCodecCnfGroup=ObjectGroup((1,3,6,1,4,1,351,150,97,2,2,3))
ciscoAltVismCodecCnfGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:ciscoAltVismCodecCnfGroup.setStatus(_A)
ciscoVismCodecCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,97,2,1,1))
ciscoVismCodecCompliance.setObjects(*((_B,_I),(_B,_J)))
if mibBuilder.loadTexts:ciscoVismCodecCompliance.setStatus('deprecated')
ciscoVismCodecComplianceRev1=ModuleCompliance((1,3,6,1,4,1,351,150,97,2,1,2))
ciscoVismCodecComplianceRev1.setObjects(*((_B,_I),(_B,_J),(_B,_U)))
if mibBuilder.loadTexts:ciscoVismCodecComplianceRev1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'vismCodecTemplateCnfGrp':vismCodecTemplateCnfGrp,'vismCodecTemplateCnfGrpTable':vismCodecTemplateCnfGrpTable,'vismCodecTemplateCnfGrpEntry':vismCodecTemplateCnfGrpEntry,_G:vismCodecTemplateNum,_P:vismCodecSupported,_Q:vismCodecTemplateMaxChanCount,'vismCodecCnfGrp':vismCodecCnfGrp,'vismCodecCnfTable':vismCodecCnfTable,'vismCodecCnfEntry':vismCodecCnfEntry,_H:vismCodecCnfIndex,_K:vismCodecName,_L:vismCodecPktPeriod,_M:vismCodecPreference,_N:vismCodecString,_O:vismCodecIanaType,_R:vismAltCodecString1,_S:vismAltCodecString2,_T:vismAltCodecString3,'ciscoVismCodecMIB':ciscoVismCodecMIB,'ciscoVismCodecMIBConformance':ciscoVismCodecMIBConformance,'ciscoVismCodecMIBCompliances':ciscoVismCodecMIBCompliances,'ciscoVismCodecCompliance':ciscoVismCodecCompliance,'ciscoVismCodecComplianceRev1':ciscoVismCodecComplianceRev1,'ciscoVismCodecMIBGroups':ciscoVismCodecMIBGroups,_I:ciscoVismCodecCnfGroup,_J:ciscoVismCodecTemplateGrp,_U:ciscoAltVismCodecCnfGroup})