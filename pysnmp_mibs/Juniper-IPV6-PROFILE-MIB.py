_f='juniIpv6ProfileGroup1'
_e='juniIpv6ProfileGroup'
_d='juniIpv6ProfileNdPrefixValidLifetime'
_c='juniIpv6ProfileNdPrefixPreferredLifetime'
_b='juniIpv6ProfileNdPrefixAutonomousFlag'
_a='juniIpv6ProfileNdPrefixOnLinkFlag'
_Z='juniIpv6ProfileNdPrefixLength'
_Y='juniIpv6ProfileNdPrefix'
_X='juniIpv6ProfileNdReachableTime'
_W='juniIpv6ProfileNdRaLifeTime'
_V='juniIpv6ProfileNdRaInterval'
_U='juniIpv6ProfileNdSuppressRa'
_T='juniIpv6ProfileNdOtherConfig'
_S='juniIpv6ProfileNdManagedConfig'
_R='juniIpv6ProfileNdEnabled'
_Q='obsolete'
_P='juniIpv6ProfileId'
_O='DisplayString'
_N='JuniName'
_M='InetAddressIPv6'
_L='juniIpv6ProfileInheritNumString'
_K='juniIpv6ProfileSrcAddrValidEnable'
_J='juniIpv6ProfileMtu'
_I='juniIpv6ProfileIpv6MaskLen'
_H='juniIpv6ProfileIpv6Addr'
_G='juniIpv6ProfileRouterName'
_F='juniIpv6ProfileSetMap'
_E='JuniEnable'
_D='Integer32'
_C='read-write'
_B='current'
_A='Juniper-IPV6-PROFILE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddressIPv6,=mibBuilder.importSymbols('INET-ADDRESS-MIB',_M)
Ipv6AddressPrefix,=mibBuilder.importSymbols('IPV6-TC','Ipv6AddressPrefix')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
JuniEnable,JuniName,JuniSetMap=mibBuilder.importSymbols('Juniper-TC',_E,_N,'JuniSetMap')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_O,'PhysAddress','TextualConvention')
juniIpv6ProfileMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,68))
if mibBuilder.loadTexts:juniIpv6ProfileMIB.setRevisions(('2007-07-19 18:19','2003-09-29 17:58'))
_JuniIpv6ProfileObjects_ObjectIdentity=ObjectIdentity
juniIpv6ProfileObjects=_JuniIpv6ProfileObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,68,1))
_JuniIpv6Profile_ObjectIdentity=ObjectIdentity
juniIpv6Profile=_JuniIpv6Profile_ObjectIdentity((1,3,6,1,4,1,4874,2,2,68,1,1))
_JuniIpv6ProfileTable_Object=MibTable
juniIpv6ProfileTable=_JuniIpv6ProfileTable_Object((1,3,6,1,4,1,4874,2,2,68,1,1,1))
if mibBuilder.loadTexts:juniIpv6ProfileTable.setStatus(_B)
_JuniIpv6ProfileEntry_Object=MibTableRow
juniIpv6ProfileEntry=_JuniIpv6ProfileEntry_Object((1,3,6,1,4,1,4874,2,2,68,1,1,1,1))
juniIpv6ProfileEntry.setIndexNames((0,_A,_P))
if mibBuilder.loadTexts:juniIpv6ProfileEntry.setStatus(_B)
_JuniIpv6ProfileId_Type=Unsigned32
_JuniIpv6ProfileId_Object=MibTableColumn
juniIpv6ProfileId=_JuniIpv6ProfileId_Object((1,3,6,1,4,1,4874,2,2,68,1,1,1,1,1),_JuniIpv6ProfileId_Type())
juniIpv6ProfileId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:juniIpv6ProfileId.setStatus(_B)
_JuniIpv6ProfileSetMap_Type=JuniSetMap
_JuniIpv6ProfileSetMap_Object=MibTableColumn
juniIpv6ProfileSetMap=_JuniIpv6ProfileSetMap_Object((1,3,6,1,4,1,4874,2,2,68,1,1,1,1,2),_JuniIpv6ProfileSetMap_Type())
juniIpv6ProfileSetMap.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpv6ProfileSetMap.setStatus(_B)
class _JuniIpv6ProfileRouterName_Type(JuniName):defaultValue=OctetString('')
_JuniIpv6ProfileRouterName_Type.__name__=_N
_JuniIpv6ProfileRouterName_Object=MibTableColumn
juniIpv6ProfileRouterName=_JuniIpv6ProfileRouterName_Object((1,3,6,1,4,1,4874,2,2,68,1,1,1,1,3),_JuniIpv6ProfileRouterName_Type())
juniIpv6ProfileRouterName.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpv6ProfileRouterName.setStatus(_B)
class _JuniIpv6ProfileIpv6Addr_Type(InetAddressIPv6):defaultHexValue='00000000000000000000000000000000'
_JuniIpv6ProfileIpv6Addr_Type.__name__=_M
_JuniIpv6ProfileIpv6Addr_Object=MibTableColumn
juniIpv6ProfileIpv6Addr=_JuniIpv6ProfileIpv6Addr_Object((1,3,6,1,4,1,4874,2,2,68,1,1,1,1,4),_JuniIpv6ProfileIpv6Addr_Type())
juniIpv6ProfileIpv6Addr.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpv6ProfileIpv6Addr.setStatus(_B)
class _JuniIpv6ProfileIpv6MaskLen_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_JuniIpv6ProfileIpv6MaskLen_Type.__name__=_D
_JuniIpv6ProfileIpv6MaskLen_Object=MibTableColumn
juniIpv6ProfileIpv6MaskLen=_JuniIpv6ProfileIpv6MaskLen_Object((1,3,6,1,4,1,4874,2,2,68,1,1,1,1,5),_JuniIpv6ProfileIpv6MaskLen_Type())
juniIpv6ProfileIpv6MaskLen.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpv6ProfileIpv6MaskLen.setStatus(_B)
class _JuniIpv6ProfileMtu_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1280,10240))
_JuniIpv6ProfileMtu_Type.__name__=_D
_JuniIpv6ProfileMtu_Object=MibTableColumn
juniIpv6ProfileMtu=_JuniIpv6ProfileMtu_Object((1,3,6,1,4,1,4874,2,2,68,1,1,1,1,6),_JuniIpv6ProfileMtu_Type())
juniIpv6ProfileMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpv6ProfileMtu.setStatus(_B)
class _JuniIpv6ProfileSrcAddrValidEnable_Type(JuniEnable):defaultValue=0
_JuniIpv6ProfileSrcAddrValidEnable_Type.__name__=_E
_JuniIpv6ProfileSrcAddrValidEnable_Object=MibTableColumn
juniIpv6ProfileSrcAddrValidEnable=_JuniIpv6ProfileSrcAddrValidEnable_Object((1,3,6,1,4,1,4874,2,2,68,1,1,1,1,7),_JuniIpv6ProfileSrcAddrValidEnable_Type())
juniIpv6ProfileSrcAddrValidEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpv6ProfileSrcAddrValidEnable.setStatus(_B)
class _JuniIpv6ProfileInheritNumString_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_JuniIpv6ProfileInheritNumString_Type.__name__=_O
_JuniIpv6ProfileInheritNumString_Object=MibTableColumn
juniIpv6ProfileInheritNumString=_JuniIpv6ProfileInheritNumString_Object((1,3,6,1,4,1,4874,2,2,68,1,1,1,1,8),_JuniIpv6ProfileInheritNumString_Type())
juniIpv6ProfileInheritNumString.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpv6ProfileInheritNumString.setStatus(_B)
class _JuniIpv6ProfileNdEnabled_Type(JuniEnable):defaultValue=0
_JuniIpv6ProfileNdEnabled_Type.__name__=_E
_JuniIpv6ProfileNdEnabled_Object=MibTableColumn
juniIpv6ProfileNdEnabled=_JuniIpv6ProfileNdEnabled_Object((1,3,6,1,4,1,4874,2,2,68,1,1,1,1,9),_JuniIpv6ProfileNdEnabled_Type())
juniIpv6ProfileNdEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpv6ProfileNdEnabled.setStatus(_B)
class _JuniIpv6ProfileNdManagedConfig_Type(JuniEnable):defaultValue=0
_JuniIpv6ProfileNdManagedConfig_Type.__name__=_E
_JuniIpv6ProfileNdManagedConfig_Object=MibTableColumn
juniIpv6ProfileNdManagedConfig=_JuniIpv6ProfileNdManagedConfig_Object((1,3,6,1,4,1,4874,2,2,68,1,1,1,1,10),_JuniIpv6ProfileNdManagedConfig_Type())
juniIpv6ProfileNdManagedConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpv6ProfileNdManagedConfig.setStatus(_B)
class _JuniIpv6ProfileNdOtherConfig_Type(JuniEnable):defaultValue=0
_JuniIpv6ProfileNdOtherConfig_Type.__name__=_E
_JuniIpv6ProfileNdOtherConfig_Object=MibTableColumn
juniIpv6ProfileNdOtherConfig=_JuniIpv6ProfileNdOtherConfig_Object((1,3,6,1,4,1,4874,2,2,68,1,1,1,1,11),_JuniIpv6ProfileNdOtherConfig_Type())
juniIpv6ProfileNdOtherConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpv6ProfileNdOtherConfig.setStatus(_B)
class _JuniIpv6ProfileNdSuppressRa_Type(JuniEnable):defaultValue=0
_JuniIpv6ProfileNdSuppressRa_Type.__name__=_E
_JuniIpv6ProfileNdSuppressRa_Object=MibTableColumn
juniIpv6ProfileNdSuppressRa=_JuniIpv6ProfileNdSuppressRa_Object((1,3,6,1,4,1,4874,2,2,68,1,1,1,1,12),_JuniIpv6ProfileNdSuppressRa_Type())
juniIpv6ProfileNdSuppressRa.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpv6ProfileNdSuppressRa.setStatus(_B)
class _JuniIpv6ProfileNdRaInterval_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,1800))
_JuniIpv6ProfileNdRaInterval_Type.__name__=_D
_JuniIpv6ProfileNdRaInterval_Object=MibTableColumn
juniIpv6ProfileNdRaInterval=_JuniIpv6ProfileNdRaInterval_Object((1,3,6,1,4,1,4874,2,2,68,1,1,1,1,13),_JuniIpv6ProfileNdRaInterval_Type())
juniIpv6ProfileNdRaInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpv6ProfileNdRaInterval.setStatus(_B)
class _JuniIpv6ProfileNdRaLifeTime_Type(Integer32):defaultValue=1800;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1800))
_JuniIpv6ProfileNdRaLifeTime_Type.__name__=_D
_JuniIpv6ProfileNdRaLifeTime_Object=MibTableColumn
juniIpv6ProfileNdRaLifeTime=_JuniIpv6ProfileNdRaLifeTime_Object((1,3,6,1,4,1,4874,2,2,68,1,1,1,1,14),_JuniIpv6ProfileNdRaLifeTime_Type())
juniIpv6ProfileNdRaLifeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpv6ProfileNdRaLifeTime.setStatus(_B)
class _JuniIpv6ProfileNdReachableTime_Type(Integer32):defaultValue=0
_JuniIpv6ProfileNdReachableTime_Type.__name__=_D
_JuniIpv6ProfileNdReachableTime_Object=MibTableColumn
juniIpv6ProfileNdReachableTime=_JuniIpv6ProfileNdReachableTime_Object((1,3,6,1,4,1,4874,2,2,68,1,1,1,1,15),_JuniIpv6ProfileNdReachableTime_Type())
juniIpv6ProfileNdReachableTime.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpv6ProfileNdReachableTime.setStatus(_B)
_JuniIpv6ProfileNdPrefix_Type=Ipv6AddressPrefix
_JuniIpv6ProfileNdPrefix_Object=MibTableColumn
juniIpv6ProfileNdPrefix=_JuniIpv6ProfileNdPrefix_Object((1,3,6,1,4,1,4874,2,2,68,1,1,1,1,16),_JuniIpv6ProfileNdPrefix_Type())
juniIpv6ProfileNdPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpv6ProfileNdPrefix.setStatus(_B)
class _JuniIpv6ProfileNdPrefixLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_JuniIpv6ProfileNdPrefixLength_Type.__name__=_D
_JuniIpv6ProfileNdPrefixLength_Object=MibTableColumn
juniIpv6ProfileNdPrefixLength=_JuniIpv6ProfileNdPrefixLength_Object((1,3,6,1,4,1,4874,2,2,68,1,1,1,1,17),_JuniIpv6ProfileNdPrefixLength_Type())
juniIpv6ProfileNdPrefixLength.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpv6ProfileNdPrefixLength.setStatus(_B)
class _JuniIpv6ProfileNdPrefixOnLinkFlag_Type(JuniEnable):defaultValue=1
_JuniIpv6ProfileNdPrefixOnLinkFlag_Type.__name__=_E
_JuniIpv6ProfileNdPrefixOnLinkFlag_Object=MibTableColumn
juniIpv6ProfileNdPrefixOnLinkFlag=_JuniIpv6ProfileNdPrefixOnLinkFlag_Object((1,3,6,1,4,1,4874,2,2,68,1,1,1,1,18),_JuniIpv6ProfileNdPrefixOnLinkFlag_Type())
juniIpv6ProfileNdPrefixOnLinkFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpv6ProfileNdPrefixOnLinkFlag.setStatus(_B)
class _JuniIpv6ProfileNdPrefixAutonomousFlag_Type(JuniEnable):defaultValue=1
_JuniIpv6ProfileNdPrefixAutonomousFlag_Type.__name__=_E
_JuniIpv6ProfileNdPrefixAutonomousFlag_Object=MibTableColumn
juniIpv6ProfileNdPrefixAutonomousFlag=_JuniIpv6ProfileNdPrefixAutonomousFlag_Object((1,3,6,1,4,1,4874,2,2,68,1,1,1,1,19),_JuniIpv6ProfileNdPrefixAutonomousFlag_Type())
juniIpv6ProfileNdPrefixAutonomousFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpv6ProfileNdPrefixAutonomousFlag.setStatus(_B)
class _JuniIpv6ProfileNdPrefixPreferredLifetime_Type(Integer32):defaultValue=604800
_JuniIpv6ProfileNdPrefixPreferredLifetime_Type.__name__=_D
_JuniIpv6ProfileNdPrefixPreferredLifetime_Object=MibTableColumn
juniIpv6ProfileNdPrefixPreferredLifetime=_JuniIpv6ProfileNdPrefixPreferredLifetime_Object((1,3,6,1,4,1,4874,2,2,68,1,1,1,1,20),_JuniIpv6ProfileNdPrefixPreferredLifetime_Type())
juniIpv6ProfileNdPrefixPreferredLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpv6ProfileNdPrefixPreferredLifetime.setStatus(_B)
class _JuniIpv6ProfileNdPrefixValidLifetime_Type(Integer32):defaultValue=2592000
_JuniIpv6ProfileNdPrefixValidLifetime_Type.__name__=_D
_JuniIpv6ProfileNdPrefixValidLifetime_Object=MibTableColumn
juniIpv6ProfileNdPrefixValidLifetime=_JuniIpv6ProfileNdPrefixValidLifetime_Object((1,3,6,1,4,1,4874,2,2,68,1,1,1,1,21),_JuniIpv6ProfileNdPrefixValidLifetime_Type())
juniIpv6ProfileNdPrefixValidLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpv6ProfileNdPrefixValidLifetime.setStatus(_B)
_JuniIpv6ProfileMIBConformance_ObjectIdentity=ObjectIdentity
juniIpv6ProfileMIBConformance=_JuniIpv6ProfileMIBConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,68,4))
_JuniIpv6ProfileMIBCompliances_ObjectIdentity=ObjectIdentity
juniIpv6ProfileMIBCompliances=_JuniIpv6ProfileMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,68,4,1))
_JuniIpv6ProfileMIBGroups_ObjectIdentity=ObjectIdentity
juniIpv6ProfileMIBGroups=_JuniIpv6ProfileMIBGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,68,4,2))
juniIpv6ProfileGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,68,4,2,1))
juniIpv6ProfileGroup.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:juniIpv6ProfileGroup.setStatus(_Q)
juniIpv6ProfileGroup1=ObjectGroup((1,3,6,1,4,1,4874,2,2,68,4,2,2))
juniIpv6ProfileGroup1.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d)))
if mibBuilder.loadTexts:juniIpv6ProfileGroup1.setStatus(_B)
juniIpv6ProfileCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,68,4,1,1))
juniIpv6ProfileCompliance.setObjects((_A,_e))
if mibBuilder.loadTexts:juniIpv6ProfileCompliance.setStatus(_Q)
juniIpv6ProfileCompliance1=ModuleCompliance((1,3,6,1,4,1,4874,2,2,68,4,1,2))
juniIpv6ProfileCompliance1.setObjects((_A,_f))
if mibBuilder.loadTexts:juniIpv6ProfileCompliance1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'juniIpv6ProfileMIB':juniIpv6ProfileMIB,'juniIpv6ProfileObjects':juniIpv6ProfileObjects,'juniIpv6Profile':juniIpv6Profile,'juniIpv6ProfileTable':juniIpv6ProfileTable,'juniIpv6ProfileEntry':juniIpv6ProfileEntry,_P:juniIpv6ProfileId,_F:juniIpv6ProfileSetMap,_G:juniIpv6ProfileRouterName,_H:juniIpv6ProfileIpv6Addr,_I:juniIpv6ProfileIpv6MaskLen,_J:juniIpv6ProfileMtu,_K:juniIpv6ProfileSrcAddrValidEnable,_L:juniIpv6ProfileInheritNumString,_R:juniIpv6ProfileNdEnabled,_S:juniIpv6ProfileNdManagedConfig,_T:juniIpv6ProfileNdOtherConfig,_U:juniIpv6ProfileNdSuppressRa,_V:juniIpv6ProfileNdRaInterval,_W:juniIpv6ProfileNdRaLifeTime,_X:juniIpv6ProfileNdReachableTime,_Y:juniIpv6ProfileNdPrefix,_Z:juniIpv6ProfileNdPrefixLength,_a:juniIpv6ProfileNdPrefixOnLinkFlag,_b:juniIpv6ProfileNdPrefixAutonomousFlag,_c:juniIpv6ProfileNdPrefixPreferredLifetime,_d:juniIpv6ProfileNdPrefixValidLifetime,'juniIpv6ProfileMIBConformance':juniIpv6ProfileMIBConformance,'juniIpv6ProfileMIBCompliances':juniIpv6ProfileMIBCompliances,'juniIpv6ProfileCompliance':juniIpv6ProfileCompliance,'juniIpv6ProfileCompliance1':juniIpv6ProfileCompliance1,'juniIpv6ProfileMIBGroups':juniIpv6ProfileMIBGroups,_e:juniIpv6ProfileGroup,_f:juniIpv6ProfileGroup1})