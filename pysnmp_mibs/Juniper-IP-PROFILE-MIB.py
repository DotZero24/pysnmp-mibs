_j='juniIpProfileGroup7'
_i='juniIpProfileGroup6'
_h='juniIpProfileGroup5'
_g='juniIpProfileGroup4'
_f='juniIpProfileGroup3'
_e='juniIpProfileGroup2'
_d='juniIpProfileGroup1'
_c='juniIpProfileGroup'
_b='juniIpProfileBlockMulticastSources'
_a='juniIpProfileLoopbackIfIndex'
_Z='deprecated'
_Y='juniIpProfileId'
_X='DisplayString'
_W='JuniName'
_V='InterfaceIndexOrZero'
_U='juniIpProfileFlowStats'
_T='juniIpProfileLoopback'
_S='juniIpProfileFilterOptionsAll'
_R='juniIpProfileRowStatus'
_Q='Integer32'
_P='juniIpProfileTcpMss'
_O='juniIpProfileInheritNumString'
_N='juniIpProfileSrcAddrValidEnable'
_M='juniIpProfileSetMap'
_L='JuniEnable'
_K='juniIpProfileMtu'
_J='juniIpProfileAccessRoute'
_I='juniIpProfileIcmpRedirectEnable'
_H='juniIpProfileDirectedBcastEnable'
_G='juniIpProfileIpMask'
_F='juniIpProfileIpAddr'
_E='juniIpProfileRouterName'
_D='obsolete'
_C='read-create'
_B='current'
_A='Juniper-IP-PROFILE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB',_V)
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
JuniEnable,JuniName,JuniSetMap=mibBuilder.importSymbols('Juniper-TC',_L,_W,'JuniSetMap')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_Q,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_X,'PhysAddress','RowStatus','TextualConvention')
juniIpProfileMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,26))
if mibBuilder.loadTexts:juniIpProfileMIB.setRevisions(('2006-09-08 10:26','2005-09-13 17:21','2004-10-05 14:04','2003-09-24 15:33','2002-10-11 13:20','2001-01-24 20:06','2000-05-08 00:00','1999-08-25 00:00'))
_JuniIpProfileObjects_ObjectIdentity=ObjectIdentity
juniIpProfileObjects=_JuniIpProfileObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,26,1))
_JuniIpProfile_ObjectIdentity=ObjectIdentity
juniIpProfile=_JuniIpProfile_ObjectIdentity((1,3,6,1,4,1,4874,2,2,26,1,1))
_JuniIpProfileTable_Object=MibTable
juniIpProfileTable=_JuniIpProfileTable_Object((1,3,6,1,4,1,4874,2,2,26,1,1,1))
if mibBuilder.loadTexts:juniIpProfileTable.setStatus(_B)
_JuniIpProfileEntry_Object=MibTableRow
juniIpProfileEntry=_JuniIpProfileEntry_Object((1,3,6,1,4,1,4874,2,2,26,1,1,1,1))
juniIpProfileEntry.setIndexNames((0,_A,_Y))
if mibBuilder.loadTexts:juniIpProfileEntry.setStatus(_B)
_JuniIpProfileId_Type=Unsigned32
_JuniIpProfileId_Object=MibTableColumn
juniIpProfileId=_JuniIpProfileId_Object((1,3,6,1,4,1,4874,2,2,26,1,1,1,1,1),_JuniIpProfileId_Type())
juniIpProfileId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:juniIpProfileId.setStatus(_B)
_JuniIpProfileRowStatus_Type=RowStatus
_JuniIpProfileRowStatus_Object=MibTableColumn
juniIpProfileRowStatus=_JuniIpProfileRowStatus_Object((1,3,6,1,4,1,4874,2,2,26,1,1,1,1,2),_JuniIpProfileRowStatus_Type())
juniIpProfileRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpProfileRowStatus.setStatus(_Z)
class _JuniIpProfileRouterName_Type(JuniName):defaultValue=OctetString('')
_JuniIpProfileRouterName_Type.__name__=_W
_JuniIpProfileRouterName_Object=MibTableColumn
juniIpProfileRouterName=_JuniIpProfileRouterName_Object((1,3,6,1,4,1,4874,2,2,26,1,1,1,1,3),_JuniIpProfileRouterName_Type())
juniIpProfileRouterName.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpProfileRouterName.setStatus(_B)
_JuniIpProfileIpAddr_Type=IpAddress
_JuniIpProfileIpAddr_Object=MibTableColumn
juniIpProfileIpAddr=_JuniIpProfileIpAddr_Object((1,3,6,1,4,1,4874,2,2,26,1,1,1,1,4),_JuniIpProfileIpAddr_Type())
juniIpProfileIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpProfileIpAddr.setStatus(_B)
_JuniIpProfileIpMask_Type=IpAddress
_JuniIpProfileIpMask_Object=MibTableColumn
juniIpProfileIpMask=_JuniIpProfileIpMask_Object((1,3,6,1,4,1,4874,2,2,26,1,1,1,1,5),_JuniIpProfileIpMask_Type())
juniIpProfileIpMask.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpProfileIpMask.setStatus(_B)
class _JuniIpProfileDirectedBcastEnable_Type(JuniEnable):defaultValue=0
_JuniIpProfileDirectedBcastEnable_Type.__name__=_L
_JuniIpProfileDirectedBcastEnable_Object=MibTableColumn
juniIpProfileDirectedBcastEnable=_JuniIpProfileDirectedBcastEnable_Object((1,3,6,1,4,1,4874,2,2,26,1,1,1,1,6),_JuniIpProfileDirectedBcastEnable_Type())
juniIpProfileDirectedBcastEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpProfileDirectedBcastEnable.setStatus(_B)
class _JuniIpProfileIcmpRedirectEnable_Type(JuniEnable):defaultValue=0
_JuniIpProfileIcmpRedirectEnable_Type.__name__=_L
_JuniIpProfileIcmpRedirectEnable_Object=MibTableColumn
juniIpProfileIcmpRedirectEnable=_JuniIpProfileIcmpRedirectEnable_Object((1,3,6,1,4,1,4874,2,2,26,1,1,1,1,7),_JuniIpProfileIcmpRedirectEnable_Type())
juniIpProfileIcmpRedirectEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpProfileIcmpRedirectEnable.setStatus(_B)
class _JuniIpProfileAccessRoute_Type(JuniEnable):defaultValue=1
_JuniIpProfileAccessRoute_Type.__name__=_L
_JuniIpProfileAccessRoute_Object=MibTableColumn
juniIpProfileAccessRoute=_JuniIpProfileAccessRoute_Object((1,3,6,1,4,1,4874,2,2,26,1,1,1,1,8),_JuniIpProfileAccessRoute_Type())
juniIpProfileAccessRoute.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpProfileAccessRoute.setStatus(_B)
class _JuniIpProfileMtu_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(512,10240))
_JuniIpProfileMtu_Type.__name__=_Q
_JuniIpProfileMtu_Object=MibTableColumn
juniIpProfileMtu=_JuniIpProfileMtu_Object((1,3,6,1,4,1,4874,2,2,26,1,1,1,1,9),_JuniIpProfileMtu_Type())
juniIpProfileMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpProfileMtu.setStatus(_B)
class _JuniIpProfileLoopbackIfIndex_Type(InterfaceIndexOrZero):defaultValue=0
_JuniIpProfileLoopbackIfIndex_Type.__name__=_V
_JuniIpProfileLoopbackIfIndex_Object=MibTableColumn
juniIpProfileLoopbackIfIndex=_JuniIpProfileLoopbackIfIndex_Object((1,3,6,1,4,1,4874,2,2,26,1,1,1,1,10),_JuniIpProfileLoopbackIfIndex_Type())
juniIpProfileLoopbackIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpProfileLoopbackIfIndex.setStatus(_D)
class _JuniIpProfileLoopback_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_JuniIpProfileLoopback_Type.__name__=_Q
_JuniIpProfileLoopback_Object=MibTableColumn
juniIpProfileLoopback=_JuniIpProfileLoopback_Object((1,3,6,1,4,1,4874,2,2,26,1,1,1,1,11),_JuniIpProfileLoopback_Type())
juniIpProfileLoopback.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpProfileLoopback.setStatus(_D)
_JuniIpProfileSetMap_Type=JuniSetMap
_JuniIpProfileSetMap_Object=MibTableColumn
juniIpProfileSetMap=_JuniIpProfileSetMap_Object((1,3,6,1,4,1,4874,2,2,26,1,1,1,1,12),_JuniIpProfileSetMap_Type())
juniIpProfileSetMap.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpProfileSetMap.setStatus(_B)
class _JuniIpProfileSrcAddrValidEnable_Type(JuniEnable):defaultValue=0
_JuniIpProfileSrcAddrValidEnable_Type.__name__=_L
_JuniIpProfileSrcAddrValidEnable_Object=MibTableColumn
juniIpProfileSrcAddrValidEnable=_JuniIpProfileSrcAddrValidEnable_Object((1,3,6,1,4,1,4874,2,2,26,1,1,1,1,13),_JuniIpProfileSrcAddrValidEnable_Type())
juniIpProfileSrcAddrValidEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpProfileSrcAddrValidEnable.setStatus(_B)
class _JuniIpProfileInheritNumString_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_JuniIpProfileInheritNumString_Type.__name__=_X
_JuniIpProfileInheritNumString_Object=MibTableColumn
juniIpProfileInheritNumString=_JuniIpProfileInheritNumString_Object((1,3,6,1,4,1,4874,2,2,26,1,1,1,1,14),_JuniIpProfileInheritNumString_Type())
juniIpProfileInheritNumString.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpProfileInheritNumString.setStatus(_B)
class _JuniIpProfileTcpMss_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(160,10240))
_JuniIpProfileTcpMss_Type.__name__=_Q
_JuniIpProfileTcpMss_Object=MibTableColumn
juniIpProfileTcpMss=_JuniIpProfileTcpMss_Object((1,3,6,1,4,1,4874,2,2,26,1,1,1,1,15),_JuniIpProfileTcpMss_Type())
juniIpProfileTcpMss.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpProfileTcpMss.setStatus(_B)
class _JuniIpProfileFilterOptionsAll_Type(JuniEnable):defaultValue=0
_JuniIpProfileFilterOptionsAll_Type.__name__=_L
_JuniIpProfileFilterOptionsAll_Object=MibTableColumn
juniIpProfileFilterOptionsAll=_JuniIpProfileFilterOptionsAll_Object((1,3,6,1,4,1,4874,2,2,26,1,1,1,1,16),_JuniIpProfileFilterOptionsAll_Type())
juniIpProfileFilterOptionsAll.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpProfileFilterOptionsAll.setStatus(_B)
class _JuniIpProfileFlowStats_Type(JuniEnable):defaultValue=0
_JuniIpProfileFlowStats_Type.__name__=_L
_JuniIpProfileFlowStats_Object=MibTableColumn
juniIpProfileFlowStats=_JuniIpProfileFlowStats_Object((1,3,6,1,4,1,4874,2,2,26,1,1,1,1,17),_JuniIpProfileFlowStats_Type())
juniIpProfileFlowStats.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpProfileFlowStats.setStatus(_B)
class _JuniIpProfileBlockMulticastSources_Type(JuniEnable):defaultValue=0
_JuniIpProfileBlockMulticastSources_Type.__name__=_L
_JuniIpProfileBlockMulticastSources_Object=MibTableColumn
juniIpProfileBlockMulticastSources=_JuniIpProfileBlockMulticastSources_Object((1,3,6,1,4,1,4874,2,2,26,1,1,1,1,18),_JuniIpProfileBlockMulticastSources_Type())
juniIpProfileBlockMulticastSources.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpProfileBlockMulticastSources.setStatus(_B)
_JuniIpProfileMIBConformance_ObjectIdentity=ObjectIdentity
juniIpProfileMIBConformance=_JuniIpProfileMIBConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,26,4))
_JuniIpProfileMIBCompliances_ObjectIdentity=ObjectIdentity
juniIpProfileMIBCompliances=_JuniIpProfileMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,26,4,1))
_JuniIpProfileMIBGroups_ObjectIdentity=ObjectIdentity
juniIpProfileMIBGroups=_JuniIpProfileMIBGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,26,4,2))
juniIpProfileGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,26,4,2,1))
juniIpProfileGroup.setObjects(*((_A,_R),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_a)))
if mibBuilder.loadTexts:juniIpProfileGroup.setStatus(_D)
juniIpProfileGroup1=ObjectGroup((1,3,6,1,4,1,4874,2,2,26,4,2,2))
juniIpProfileGroup1.setObjects(*((_A,_R),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_T)))
if mibBuilder.loadTexts:juniIpProfileGroup1.setStatus(_D)
juniIpProfileGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,26,4,2,3))
juniIpProfileGroup2.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_T),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:juniIpProfileGroup2.setStatus(_D)
juniIpProfileDeprecatedGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,26,4,2,4))
juniIpProfileDeprecatedGroup.setObjects((_A,_R))
if mibBuilder.loadTexts:juniIpProfileDeprecatedGroup.setStatus(_Z)
juniIpProfileGroup3=ObjectGroup((1,3,6,1,4,1,4874,2,2,26,4,2,5))
juniIpProfileGroup3.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:juniIpProfileGroup3.setStatus(_D)
juniIpProfileGroup4=ObjectGroup((1,3,6,1,4,1,4874,2,2,26,4,2,6))
juniIpProfileGroup4.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:juniIpProfileGroup4.setStatus(_D)
juniIpProfileGroup5=ObjectGroup((1,3,6,1,4,1,4874,2,2,26,4,2,7))
juniIpProfileGroup5.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_S)))
if mibBuilder.loadTexts:juniIpProfileGroup5.setStatus(_D)
juniIpProfileGroup6=ObjectGroup((1,3,6,1,4,1,4874,2,2,26,4,2,8))
juniIpProfileGroup6.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_S),(_A,_U)))
if mibBuilder.loadTexts:juniIpProfileGroup6.setStatus(_D)
juniIpProfileGroup7=ObjectGroup((1,3,6,1,4,1,4874,2,2,26,4,2,9))
juniIpProfileGroup7.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_S),(_A,_U),(_A,_b)))
if mibBuilder.loadTexts:juniIpProfileGroup7.setStatus(_B)
juniIpProfileCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,26,4,1,1))
juniIpProfileCompliance.setObjects((_A,_c))
if mibBuilder.loadTexts:juniIpProfileCompliance.setStatus(_D)
juniIpProfileCompliance1=ModuleCompliance((1,3,6,1,4,1,4874,2,2,26,4,1,2))
juniIpProfileCompliance1.setObjects((_A,_d))
if mibBuilder.loadTexts:juniIpProfileCompliance1.setStatus(_D)
juniIpProfileCompliance2=ModuleCompliance((1,3,6,1,4,1,4874,2,2,26,4,1,3))
juniIpProfileCompliance2.setObjects((_A,_e))
if mibBuilder.loadTexts:juniIpProfileCompliance2.setStatus(_D)
juniIpProfileCompliance3=ModuleCompliance((1,3,6,1,4,1,4874,2,2,26,4,1,4))
juniIpProfileCompliance3.setObjects((_A,_f))
if mibBuilder.loadTexts:juniIpProfileCompliance3.setStatus(_D)
juniIpProfileCompliance4=ModuleCompliance((1,3,6,1,4,1,4874,2,2,26,4,1,5))
juniIpProfileCompliance4.setObjects((_A,_g))
if mibBuilder.loadTexts:juniIpProfileCompliance4.setStatus(_D)
juniIpProfileCompliance5=ModuleCompliance((1,3,6,1,4,1,4874,2,2,26,4,1,6))
juniIpProfileCompliance5.setObjects((_A,_h))
if mibBuilder.loadTexts:juniIpProfileCompliance5.setStatus(_B)
juniIpProfileCompliance6=ModuleCompliance((1,3,6,1,4,1,4874,2,2,26,4,1,7))
juniIpProfileCompliance6.setObjects((_A,_i))
if mibBuilder.loadTexts:juniIpProfileCompliance6.setStatus(_B)
juniIpProfileCompliance7=ModuleCompliance((1,3,6,1,4,1,4874,2,2,26,4,1,8))
juniIpProfileCompliance7.setObjects((_A,_j))
if mibBuilder.loadTexts:juniIpProfileCompliance7.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'juniIpProfileMIB':juniIpProfileMIB,'juniIpProfileObjects':juniIpProfileObjects,'juniIpProfile':juniIpProfile,'juniIpProfileTable':juniIpProfileTable,'juniIpProfileEntry':juniIpProfileEntry,_Y:juniIpProfileId,_R:juniIpProfileRowStatus,_E:juniIpProfileRouterName,_F:juniIpProfileIpAddr,_G:juniIpProfileIpMask,_H:juniIpProfileDirectedBcastEnable,_I:juniIpProfileIcmpRedirectEnable,_J:juniIpProfileAccessRoute,_K:juniIpProfileMtu,_a:juniIpProfileLoopbackIfIndex,_T:juniIpProfileLoopback,_M:juniIpProfileSetMap,_N:juniIpProfileSrcAddrValidEnable,_O:juniIpProfileInheritNumString,_P:juniIpProfileTcpMss,_S:juniIpProfileFilterOptionsAll,_U:juniIpProfileFlowStats,_b:juniIpProfileBlockMulticastSources,'juniIpProfileMIBConformance':juniIpProfileMIBConformance,'juniIpProfileMIBCompliances':juniIpProfileMIBCompliances,'juniIpProfileCompliance':juniIpProfileCompliance,'juniIpProfileCompliance1':juniIpProfileCompliance1,'juniIpProfileCompliance2':juniIpProfileCompliance2,'juniIpProfileCompliance3':juniIpProfileCompliance3,'juniIpProfileCompliance4':juniIpProfileCompliance4,'juniIpProfileCompliance5':juniIpProfileCompliance5,'juniIpProfileCompliance6':juniIpProfileCompliance6,'juniIpProfileCompliance7':juniIpProfileCompliance7,'juniIpProfileMIBGroups':juniIpProfileMIBGroups,_c:juniIpProfileGroup,_d:juniIpProfileGroup1,_e:juniIpProfileGroup2,'juniIpProfileDeprecatedGroup':juniIpProfileDeprecatedGroup,_f:juniIpProfileGroup3,_g:juniIpProfileGroup4,_h:juniIpProfileGroup5,_i:juniIpProfileGroup6,_j:juniIpProfileGroup7})