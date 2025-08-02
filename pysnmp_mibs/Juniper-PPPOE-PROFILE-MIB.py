_a='juniPppoeProfileGroup7'
_Z='juniPppoeProfileGroup6'
_Y='juniPppoeProfileGroup5'
_X='juniPppoeProfileGroup4'
_W='juniPppoeProfileGroup3'
_V='juniPppoeProfileGroup2'
_U='juniPppoeProfileGroup'
_T='juniPppoeProfileMaxSessionOverride'
_S='juniPppoeProfileId'
_R='juniPppoeProfileMtu'
_Q='juniPppoeProfilePadrRemoteCircuitIdCapture'
_P='Integer32'
_O='juniPppoeProfileServiceNameTableName'
_N='DisplayString'
_M='JuniEnable'
_L='juniPppoeProfilePacketTrace'
_K='juniPppoeProfilePadiFlag'
_J='juniPppoeProfileAcName'
_I='juniPppoeProfileDupProtect'
_H='juniPppoeProfileSubUrl'
_G='juniPppoeProfileSubMotm'
_F='juniPppoeProfileMaxNumSessions'
_E='juniPppoeProfileSetMap'
_D='obsolete'
_C='read-write'
_B='current'
_A='Juniper-PPPOE-PROFILE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
JuniEnable,JuniSetMap=mibBuilder.importSymbols('Juniper-TC',_M,'JuniSetMap')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_P,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_N,'PhysAddress','TextualConvention')
juniPppoeProfileMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,46))
if mibBuilder.loadTexts:juniPppoeProfileMIB.setRevisions(('2008-06-18 10:29','2005-07-13 11:40','2004-06-10 19:25','2003-03-11 21:58','2002-09-16 21:44','2002-08-15 20:34','2002-08-15 19:07','2001-03-21 18:32'))
_JuniPppoeProfileObjects_ObjectIdentity=ObjectIdentity
juniPppoeProfileObjects=_JuniPppoeProfileObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,46,1))
_JuniPppoeProfile_ObjectIdentity=ObjectIdentity
juniPppoeProfile=_JuniPppoeProfile_ObjectIdentity((1,3,6,1,4,1,4874,2,2,46,1,1))
_JuniPppoeProfileTable_Object=MibTable
juniPppoeProfileTable=_JuniPppoeProfileTable_Object((1,3,6,1,4,1,4874,2,2,46,1,1,1))
if mibBuilder.loadTexts:juniPppoeProfileTable.setStatus(_B)
_JuniPppoeProfileEntry_Object=MibTableRow
juniPppoeProfileEntry=_JuniPppoeProfileEntry_Object((1,3,6,1,4,1,4874,2,2,46,1,1,1,1))
juniPppoeProfileEntry.setIndexNames((0,_A,_S))
if mibBuilder.loadTexts:juniPppoeProfileEntry.setStatus(_B)
_JuniPppoeProfileId_Type=Unsigned32
_JuniPppoeProfileId_Object=MibTableColumn
juniPppoeProfileId=_JuniPppoeProfileId_Object((1,3,6,1,4,1,4874,2,2,46,1,1,1,1,1),_JuniPppoeProfileId_Type())
juniPppoeProfileId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:juniPppoeProfileId.setStatus(_B)
_JuniPppoeProfileSetMap_Type=JuniSetMap
_JuniPppoeProfileSetMap_Object=MibTableColumn
juniPppoeProfileSetMap=_JuniPppoeProfileSetMap_Object((1,3,6,1,4,1,4874,2,2,46,1,1,1,1,2),_JuniPppoeProfileSetMap_Type())
juniPppoeProfileSetMap.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppoeProfileSetMap.setStatus(_B)
class _JuniPppoeProfileMaxNumSessions_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_JuniPppoeProfileMaxNumSessions_Type.__name__=_P
_JuniPppoeProfileMaxNumSessions_Object=MibTableColumn
juniPppoeProfileMaxNumSessions=_JuniPppoeProfileMaxNumSessions_Object((1,3,6,1,4,1,4874,2,2,46,1,1,1,1,3),_JuniPppoeProfileMaxNumSessions_Type())
juniPppoeProfileMaxNumSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppoeProfileMaxNumSessions.setStatus(_B)
class _JuniPppoeProfileSubMotm_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_JuniPppoeProfileSubMotm_Type.__name__=_N
_JuniPppoeProfileSubMotm_Object=MibTableColumn
juniPppoeProfileSubMotm=_JuniPppoeProfileSubMotm_Object((1,3,6,1,4,1,4874,2,2,46,1,1,1,1,4),_JuniPppoeProfileSubMotm_Type())
juniPppoeProfileSubMotm.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppoeProfileSubMotm.setStatus(_B)
class _JuniPppoeProfileSubUrl_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_JuniPppoeProfileSubUrl_Type.__name__=_N
_JuniPppoeProfileSubUrl_Object=MibTableColumn
juniPppoeProfileSubUrl=_JuniPppoeProfileSubUrl_Object((1,3,6,1,4,1,4874,2,2,46,1,1,1,1,5),_JuniPppoeProfileSubUrl_Type())
juniPppoeProfileSubUrl.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppoeProfileSubUrl.setStatus(_B)
class _JuniPppoeProfileDupProtect_Type(JuniEnable):defaultValue=0
_JuniPppoeProfileDupProtect_Type.__name__=_M
_JuniPppoeProfileDupProtect_Object=MibTableColumn
juniPppoeProfileDupProtect=_JuniPppoeProfileDupProtect_Object((1,3,6,1,4,1,4874,2,2,46,1,1,1,1,6),_JuniPppoeProfileDupProtect_Type())
juniPppoeProfileDupProtect.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppoeProfileDupProtect.setStatus(_B)
class _JuniPppoeProfileAcName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_JuniPppoeProfileAcName_Type.__name__=_N
_JuniPppoeProfileAcName_Object=MibTableColumn
juniPppoeProfileAcName=_JuniPppoeProfileAcName_Object((1,3,6,1,4,1,4874,2,2,46,1,1,1,1,7),_JuniPppoeProfileAcName_Type())
juniPppoeProfileAcName.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppoeProfileAcName.setStatus(_B)
class _JuniPppoeProfilePadiFlag_Type(JuniEnable):defaultValue=0
_JuniPppoeProfilePadiFlag_Type.__name__=_M
_JuniPppoeProfilePadiFlag_Object=MibTableColumn
juniPppoeProfilePadiFlag=_JuniPppoeProfilePadiFlag_Object((1,3,6,1,4,1,4874,2,2,46,1,1,1,1,8),_JuniPppoeProfilePadiFlag_Type())
juniPppoeProfilePadiFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppoeProfilePadiFlag.setStatus(_B)
class _JuniPppoeProfilePacketTrace_Type(JuniEnable):defaultValue=0
_JuniPppoeProfilePacketTrace_Type.__name__=_M
_JuniPppoeProfilePacketTrace_Object=MibTableColumn
juniPppoeProfilePacketTrace=_JuniPppoeProfilePacketTrace_Object((1,3,6,1,4,1,4874,2,2,46,1,1,1,1,9),_JuniPppoeProfilePacketTrace_Type())
juniPppoeProfilePacketTrace.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppoeProfilePacketTrace.setStatus(_B)
class _JuniPppoeProfileServiceNameTableName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_JuniPppoeProfileServiceNameTableName_Type.__name__=_N
_JuniPppoeProfileServiceNameTableName_Object=MibTableColumn
juniPppoeProfileServiceNameTableName=_JuniPppoeProfileServiceNameTableName_Object((1,3,6,1,4,1,4874,2,2,46,1,1,1,1,10),_JuniPppoeProfileServiceNameTableName_Type())
juniPppoeProfileServiceNameTableName.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppoeProfileServiceNameTableName.setStatus(_B)
class _JuniPppoeProfilePadrRemoteCircuitIdCapture_Type(JuniEnable):defaultValue=0
_JuniPppoeProfilePadrRemoteCircuitIdCapture_Type.__name__=_M
_JuniPppoeProfilePadrRemoteCircuitIdCapture_Object=MibTableColumn
juniPppoeProfilePadrRemoteCircuitIdCapture=_JuniPppoeProfilePadrRemoteCircuitIdCapture_Object((1,3,6,1,4,1,4874,2,2,46,1,1,1,1,11),_JuniPppoeProfilePadrRemoteCircuitIdCapture_Type())
juniPppoeProfilePadrRemoteCircuitIdCapture.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppoeProfilePadrRemoteCircuitIdCapture.setStatus(_B)
class _JuniPppoeProfileMtu_Type(Integer32):defaultValue=1494;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(2,2),ValueRangeConstraint(66,65535))
_JuniPppoeProfileMtu_Type.__name__=_P
_JuniPppoeProfileMtu_Object=MibTableColumn
juniPppoeProfileMtu=_JuniPppoeProfileMtu_Object((1,3,6,1,4,1,4874,2,2,46,1,1,1,1,12),_JuniPppoeProfileMtu_Type())
juniPppoeProfileMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppoeProfileMtu.setStatus(_B)
class _JuniPppoeProfileMaxSessionOverride_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('override',1),('ignore',2)))
_JuniPppoeProfileMaxSessionOverride_Type.__name__=_P
_JuniPppoeProfileMaxSessionOverride_Object=MibTableColumn
juniPppoeProfileMaxSessionOverride=_JuniPppoeProfileMaxSessionOverride_Object((1,3,6,1,4,1,4874,2,2,46,1,1,1,1,13),_JuniPppoeProfileMaxSessionOverride_Type())
juniPppoeProfileMaxSessionOverride.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppoeProfileMaxSessionOverride.setStatus(_B)
_JuniPppoeProfileConformance_ObjectIdentity=ObjectIdentity
juniPppoeProfileConformance=_JuniPppoeProfileConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,46,4))
_JuniPppoeProfileCompliances_ObjectIdentity=ObjectIdentity
juniPppoeProfileCompliances=_JuniPppoeProfileCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,46,4,1))
_JuniPppoeProfileGroups_ObjectIdentity=ObjectIdentity
juniPppoeProfileGroups=_JuniPppoeProfileGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,46,4,2))
juniPppoeProfileGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,46,4,2,1))
juniPppoeProfileGroup.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:juniPppoeProfileGroup.setStatus(_D)
juniPppoeProfileGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,46,4,2,2))
juniPppoeProfileGroup2.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:juniPppoeProfileGroup2.setStatus(_D)
juniPppoeProfileGroup3=ObjectGroup((1,3,6,1,4,1,4874,2,2,46,4,2,3))
juniPppoeProfileGroup3.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:juniPppoeProfileGroup3.setStatus(_D)
juniPppoeProfileGroup4=ObjectGroup((1,3,6,1,4,1,4874,2,2,46,4,2,4))
juniPppoeProfileGroup4.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_O)))
if mibBuilder.loadTexts:juniPppoeProfileGroup4.setStatus(_D)
juniPppoeProfileGroup5=ObjectGroup((1,3,6,1,4,1,4874,2,2,46,4,2,5))
juniPppoeProfileGroup5.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_O),(_A,_Q)))
if mibBuilder.loadTexts:juniPppoeProfileGroup5.setStatus(_D)
juniPppoeProfileGroup6=ObjectGroup((1,3,6,1,4,1,4874,2,2,46,4,2,6))
juniPppoeProfileGroup6.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_O),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:juniPppoeProfileGroup6.setStatus(_D)
juniPppoeProfileGroup7=ObjectGroup((1,3,6,1,4,1,4874,2,2,46,4,2,7))
juniPppoeProfileGroup7.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_O),(_A,_Q),(_A,_R),(_A,_T)))
if mibBuilder.loadTexts:juniPppoeProfileGroup7.setStatus(_B)
juniPppoeProfileCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,46,4,1,1))
juniPppoeProfileCompliance.setObjects((_A,_U))
if mibBuilder.loadTexts:juniPppoeProfileCompliance.setStatus(_D)
juniPppoeCompliance2=ModuleCompliance((1,3,6,1,4,1,4874,2,2,46,4,1,2))
juniPppoeCompliance2.setObjects((_A,_V))
if mibBuilder.loadTexts:juniPppoeCompliance2.setStatus(_D)
juniPppoeCompliance3=ModuleCompliance((1,3,6,1,4,1,4874,2,2,46,4,1,3))
juniPppoeCompliance3.setObjects((_A,_W))
if mibBuilder.loadTexts:juniPppoeCompliance3.setStatus(_D)
juniPppoeCompliance4=ModuleCompliance((1,3,6,1,4,1,4874,2,2,46,4,1,4))
juniPppoeCompliance4.setObjects((_A,_X))
if mibBuilder.loadTexts:juniPppoeCompliance4.setStatus(_D)
juniPppoeCompliance5=ModuleCompliance((1,3,6,1,4,1,4874,2,2,46,4,1,5))
juniPppoeCompliance5.setObjects((_A,_Y))
if mibBuilder.loadTexts:juniPppoeCompliance5.setStatus(_D)
juniPppoeCompliance6=ModuleCompliance((1,3,6,1,4,1,4874,2,2,46,4,1,6))
juniPppoeCompliance6.setObjects((_A,_Z))
if mibBuilder.loadTexts:juniPppoeCompliance6.setStatus(_D)
juniPppoeCompliance7=ModuleCompliance((1,3,6,1,4,1,4874,2,2,46,4,1,7))
juniPppoeCompliance7.setObjects((_A,_a))
if mibBuilder.loadTexts:juniPppoeCompliance7.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'juniPppoeProfileMIB':juniPppoeProfileMIB,'juniPppoeProfileObjects':juniPppoeProfileObjects,'juniPppoeProfile':juniPppoeProfile,'juniPppoeProfileTable':juniPppoeProfileTable,'juniPppoeProfileEntry':juniPppoeProfileEntry,_S:juniPppoeProfileId,_E:juniPppoeProfileSetMap,_F:juniPppoeProfileMaxNumSessions,_G:juniPppoeProfileSubMotm,_H:juniPppoeProfileSubUrl,_I:juniPppoeProfileDupProtect,_J:juniPppoeProfileAcName,_K:juniPppoeProfilePadiFlag,_L:juniPppoeProfilePacketTrace,_O:juniPppoeProfileServiceNameTableName,_Q:juniPppoeProfilePadrRemoteCircuitIdCapture,_R:juniPppoeProfileMtu,_T:juniPppoeProfileMaxSessionOverride,'juniPppoeProfileConformance':juniPppoeProfileConformance,'juniPppoeProfileCompliances':juniPppoeProfileCompliances,'juniPppoeProfileCompliance':juniPppoeProfileCompliance,'juniPppoeCompliance2':juniPppoeCompliance2,'juniPppoeCompliance3':juniPppoeCompliance3,'juniPppoeCompliance4':juniPppoeCompliance4,'juniPppoeCompliance5':juniPppoeCompliance5,'juniPppoeCompliance6':juniPppoeCompliance6,'juniPppoeCompliance7':juniPppoeCompliance7,'juniPppoeProfileGroups':juniPppoeProfileGroups,_U:juniPppoeProfileGroup,_V:juniPppoeProfileGroup2,_W:juniPppoeProfileGroup3,_X:juniPppoeProfileGroup4,_Y:juniPppoeProfileGroup5,_Z:juniPppoeProfileGroup6,_a:juniPppoeProfileGroup7})