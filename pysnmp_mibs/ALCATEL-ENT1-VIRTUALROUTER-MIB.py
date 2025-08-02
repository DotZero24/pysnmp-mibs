_p='alaVirtualRouterConfigMIBGroup'
_o='alaVirtualRouterProfileMaxMatchInterfaces'
_n='alaVirtualRouterProfileMaxAddressBlocks'
_m='alaVirtualRouterProfileMaxAccessLists'
_l='alaVirtualRouterProfileMaxTlvs'
_k='alaVirtualRouterProfileMaxSequences'
_j='alaVirtualRouterProfileMaxRouteMaps'
_i='alaVrConfigVrrpStatus'
_h='alaVrConfigMplsLdpStatus'
_g='alaVrConfigOspf3Status'
_f='alaVrConfigRipngStatus'
_e='alaVrConfigDvmrpStatus'
_d='alaVrConfigPimStatus'
_c='alaVrConfigBgpStatus'
_b='alaVrConfigIsisStatus'
_a='alaVrConfigOspfStatus'
_Z='alaVrConfigRipStatus'
_Y='alaVirtualRouterNoAutoLoadVrrp'
_X='alaVirtualRouterMaxMatchInterfaces'
_W='alaVirtualRouterMaxAddressBlocks'
_V='alaVirtualRouterMaxAccessLists'
_U='alaVirtualRouterMaxTlvs'
_T='alaVirtualRouterMaxSequences'
_S='alaVirtualRouterMaxRouteMaps'
_R='alaVirtualRouterProfile'
_Q='alaVirtualRouterNameRowStatus'
_P='alaVirtualRouterNameIndex'
_O='alaVirtualRouterProfileName'
_N='alaVrConfigIndex'
_M='alaVirtualRouterName'
_L='TruthValue'
_K='read-create'
_J='not-accessible'
_I='SnmpAdminString'
_H='read-only'
_G='loading'
_F='notloaded'
_E='loaded'
_D='Integer32'
_C='read-write'
_B='ALCATEL-ENT1-VIRTUALROUTER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
routingIND1Vrf,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','routingIND1Vrf')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_L)
alcatelIND1VirtualRouterMIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,15,1))
if mibBuilder.loadTexts:alcatelIND1VirtualRouterMIB.setRevisions(('2008-03-17 00:00',))
_AlcatelIND1VirtualRouterMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1VirtualRouterMIBObjects=_AlcatelIND1VirtualRouterMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,1))
_AlaVirtualRouterConfig_ObjectIdentity=ObjectIdentity
alaVirtualRouterConfig=_AlaVirtualRouterConfig_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,1,1))
_AlaVirtualRouterNameTable_Object=MibTable
alaVirtualRouterNameTable=_AlaVirtualRouterNameTable_Object((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,1,1,1))
if mibBuilder.loadTexts:alaVirtualRouterNameTable.setStatus(_A)
_AlaVirtualRouterNameEntry_Object=MibTableRow
alaVirtualRouterNameEntry=_AlaVirtualRouterNameEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,1,1,1,1))
alaVirtualRouterNameEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:alaVirtualRouterNameEntry.setStatus(_A)
class _AlaVirtualRouterName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_AlaVirtualRouterName_Type.__name__=_I
_AlaVirtualRouterName_Object=MibTableColumn
alaVirtualRouterName=_AlaVirtualRouterName_Object((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,1,1,1,1,1),_AlaVirtualRouterName_Type())
alaVirtualRouterName.setMaxAccess(_J)
if mibBuilder.loadTexts:alaVirtualRouterName.setStatus(_A)
_AlaVirtualRouterNameIndex_Type=Integer32
_AlaVirtualRouterNameIndex_Object=MibTableColumn
alaVirtualRouterNameIndex=_AlaVirtualRouterNameIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,1,1,1,1,2),_AlaVirtualRouterNameIndex_Type())
alaVirtualRouterNameIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:alaVirtualRouterNameIndex.setStatus(_A)
_AlaVirtualRouterNameRowStatus_Type=RowStatus
_AlaVirtualRouterNameRowStatus_Object=MibTableColumn
alaVirtualRouterNameRowStatus=_AlaVirtualRouterNameRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,1,1,1,1,3),_AlaVirtualRouterNameRowStatus_Type())
alaVirtualRouterNameRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:alaVirtualRouterNameRowStatus.setStatus(_A)
class _AlaVirtualRouterProfile_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_AlaVirtualRouterProfile_Type.__name__=_I
_AlaVirtualRouterProfile_Object=MibTableColumn
alaVirtualRouterProfile=_AlaVirtualRouterProfile_Object((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,1,1,1,1,4),_AlaVirtualRouterProfile_Type())
alaVirtualRouterProfile.setMaxAccess(_K)
if mibBuilder.loadTexts:alaVirtualRouterProfile.setStatus(_A)
_AlaVirtualRouterMaxRouteMaps_Type=Integer32
_AlaVirtualRouterMaxRouteMaps_Object=MibTableColumn
alaVirtualRouterMaxRouteMaps=_AlaVirtualRouterMaxRouteMaps_Object((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,1,1,1,1,5),_AlaVirtualRouterMaxRouteMaps_Type())
alaVirtualRouterMaxRouteMaps.setMaxAccess(_H)
if mibBuilder.loadTexts:alaVirtualRouterMaxRouteMaps.setStatus(_A)
_AlaVirtualRouterMaxSequences_Type=Integer32
_AlaVirtualRouterMaxSequences_Object=MibTableColumn
alaVirtualRouterMaxSequences=_AlaVirtualRouterMaxSequences_Object((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,1,1,1,1,6),_AlaVirtualRouterMaxSequences_Type())
alaVirtualRouterMaxSequences.setMaxAccess(_H)
if mibBuilder.loadTexts:alaVirtualRouterMaxSequences.setStatus(_A)
_AlaVirtualRouterMaxTlvs_Type=Integer32
_AlaVirtualRouterMaxTlvs_Object=MibTableColumn
alaVirtualRouterMaxTlvs=_AlaVirtualRouterMaxTlvs_Object((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,1,1,1,1,7),_AlaVirtualRouterMaxTlvs_Type())
alaVirtualRouterMaxTlvs.setMaxAccess(_H)
if mibBuilder.loadTexts:alaVirtualRouterMaxTlvs.setStatus(_A)
_AlaVirtualRouterMaxAccessLists_Type=Integer32
_AlaVirtualRouterMaxAccessLists_Object=MibTableColumn
alaVirtualRouterMaxAccessLists=_AlaVirtualRouterMaxAccessLists_Object((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,1,1,1,1,8),_AlaVirtualRouterMaxAccessLists_Type())
alaVirtualRouterMaxAccessLists.setMaxAccess(_H)
if mibBuilder.loadTexts:alaVirtualRouterMaxAccessLists.setStatus(_A)
_AlaVirtualRouterMaxAddressBlocks_Type=Integer32
_AlaVirtualRouterMaxAddressBlocks_Object=MibTableColumn
alaVirtualRouterMaxAddressBlocks=_AlaVirtualRouterMaxAddressBlocks_Object((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,1,1,1,1,9),_AlaVirtualRouterMaxAddressBlocks_Type())
alaVirtualRouterMaxAddressBlocks.setMaxAccess(_H)
if mibBuilder.loadTexts:alaVirtualRouterMaxAddressBlocks.setStatus(_A)
_AlaVirtualRouterMaxMatchInterfaces_Type=Integer32
_AlaVirtualRouterMaxMatchInterfaces_Object=MibTableColumn
alaVirtualRouterMaxMatchInterfaces=_AlaVirtualRouterMaxMatchInterfaces_Object((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,1,1,1,1,10),_AlaVirtualRouterMaxMatchInterfaces_Type())
alaVirtualRouterMaxMatchInterfaces.setMaxAccess(_H)
if mibBuilder.loadTexts:alaVirtualRouterMaxMatchInterfaces.setStatus(_A)
class _AlaVirtualRouterNoAutoLoadVrrp_Type(TruthValue):defaultValue=2
_AlaVirtualRouterNoAutoLoadVrrp_Type.__name__=_L
_AlaVirtualRouterNoAutoLoadVrrp_Object=MibTableColumn
alaVirtualRouterNoAutoLoadVrrp=_AlaVirtualRouterNoAutoLoadVrrp_Object((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,1,1,1,1,11),_AlaVirtualRouterNoAutoLoadVrrp_Type())
alaVirtualRouterNoAutoLoadVrrp.setMaxAccess(_K)
if mibBuilder.loadTexts:alaVirtualRouterNoAutoLoadVrrp.setStatus(_A)
_AlaVrConfigTable_Object=MibTable
alaVrConfigTable=_AlaVrConfigTable_Object((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,1,1,2))
if mibBuilder.loadTexts:alaVrConfigTable.setStatus(_A)
_AlaVrConfigEntry_Object=MibTableRow
alaVrConfigEntry=_AlaVrConfigEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,1,1,2,1))
alaVrConfigEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:alaVrConfigEntry.setStatus(_A)
class _AlaVrConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AlaVrConfigIndex_Type.__name__=_D
_AlaVrConfigIndex_Object=MibTableColumn
alaVrConfigIndex=_AlaVrConfigIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,1,1,2,1,1),_AlaVrConfigIndex_Type())
alaVrConfigIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:alaVrConfigIndex.setStatus(_A)
class _AlaVrConfigRipStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_AlaVrConfigRipStatus_Type.__name__=_D
_AlaVrConfigRipStatus_Object=MibTableColumn
alaVrConfigRipStatus=_AlaVrConfigRipStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,1,1,2,1,2),_AlaVrConfigRipStatus_Type())
alaVrConfigRipStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVrConfigRipStatus.setStatus(_A)
class _AlaVrConfigOspfStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_AlaVrConfigOspfStatus_Type.__name__=_D
_AlaVrConfigOspfStatus_Object=MibTableColumn
alaVrConfigOspfStatus=_AlaVrConfigOspfStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,1,1,2,1,3),_AlaVrConfigOspfStatus_Type())
alaVrConfigOspfStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVrConfigOspfStatus.setStatus(_A)
class _AlaVrConfigIsisStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_AlaVrConfigIsisStatus_Type.__name__=_D
_AlaVrConfigIsisStatus_Object=MibTableColumn
alaVrConfigIsisStatus=_AlaVrConfigIsisStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,1,1,2,1,4),_AlaVrConfigIsisStatus_Type())
alaVrConfigIsisStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVrConfigIsisStatus.setStatus(_A)
class _AlaVrConfigBgpStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_AlaVrConfigBgpStatus_Type.__name__=_D
_AlaVrConfigBgpStatus_Object=MibTableColumn
alaVrConfigBgpStatus=_AlaVrConfigBgpStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,1,1,2,1,5),_AlaVrConfigBgpStatus_Type())
alaVrConfigBgpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVrConfigBgpStatus.setStatus(_A)
class _AlaVrConfigPimStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_AlaVrConfigPimStatus_Type.__name__=_D
_AlaVrConfigPimStatus_Object=MibTableColumn
alaVrConfigPimStatus=_AlaVrConfigPimStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,1,1,2,1,6),_AlaVrConfigPimStatus_Type())
alaVrConfigPimStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVrConfigPimStatus.setStatus(_A)
class _AlaVrConfigDvmrpStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_AlaVrConfigDvmrpStatus_Type.__name__=_D
_AlaVrConfigDvmrpStatus_Object=MibTableColumn
alaVrConfigDvmrpStatus=_AlaVrConfigDvmrpStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,1,1,2,1,7),_AlaVrConfigDvmrpStatus_Type())
alaVrConfigDvmrpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVrConfigDvmrpStatus.setStatus(_A)
class _AlaVrConfigRipngStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_AlaVrConfigRipngStatus_Type.__name__=_D
_AlaVrConfigRipngStatus_Object=MibTableColumn
alaVrConfigRipngStatus=_AlaVrConfigRipngStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,1,1,2,1,8),_AlaVrConfigRipngStatus_Type())
alaVrConfigRipngStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVrConfigRipngStatus.setStatus(_A)
class _AlaVrConfigOspf3Status_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_AlaVrConfigOspf3Status_Type.__name__=_D
_AlaVrConfigOspf3Status_Object=MibTableColumn
alaVrConfigOspf3Status=_AlaVrConfigOspf3Status_Object((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,1,1,2,1,9),_AlaVrConfigOspf3Status_Type())
alaVrConfigOspf3Status.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVrConfigOspf3Status.setStatus(_A)
class _AlaVrConfigMplsLdpStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_AlaVrConfigMplsLdpStatus_Type.__name__=_D
_AlaVrConfigMplsLdpStatus_Object=MibTableColumn
alaVrConfigMplsLdpStatus=_AlaVrConfigMplsLdpStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,1,1,2,1,10),_AlaVrConfigMplsLdpStatus_Type())
alaVrConfigMplsLdpStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:alaVrConfigMplsLdpStatus.setStatus(_A)
class _AlaVrConfigVrrpStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_AlaVrConfigVrrpStatus_Type.__name__=_D
_AlaVrConfigVrrpStatus_Object=MibTableColumn
alaVrConfigVrrpStatus=_AlaVrConfigVrrpStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,1,1,2,1,11),_AlaVrConfigVrrpStatus_Type())
alaVrConfigVrrpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVrConfigVrrpStatus.setStatus(_A)
_AlaVirtualRouterProfileTable_Object=MibTable
alaVirtualRouterProfileTable=_AlaVirtualRouterProfileTable_Object((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,1,1,3))
if mibBuilder.loadTexts:alaVirtualRouterProfileTable.setStatus(_A)
_AlaVirtualRouterProfileEntry_Object=MibTableRow
alaVirtualRouterProfileEntry=_AlaVirtualRouterProfileEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,1,1,3,1))
alaVirtualRouterProfileEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:alaVirtualRouterProfileEntry.setStatus(_A)
_AlaVirtualRouterProfileName_Type=SnmpAdminString
_AlaVirtualRouterProfileName_Object=MibTableColumn
alaVirtualRouterProfileName=_AlaVirtualRouterProfileName_Object((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,1,1,3,1,1),_AlaVirtualRouterProfileName_Type())
alaVirtualRouterProfileName.setMaxAccess(_J)
if mibBuilder.loadTexts:alaVirtualRouterProfileName.setStatus(_A)
_AlaVirtualRouterProfileMaxRouteMaps_Type=Integer32
_AlaVirtualRouterProfileMaxRouteMaps_Object=MibTableColumn
alaVirtualRouterProfileMaxRouteMaps=_AlaVirtualRouterProfileMaxRouteMaps_Object((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,1,1,3,1,2),_AlaVirtualRouterProfileMaxRouteMaps_Type())
alaVirtualRouterProfileMaxRouteMaps.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVirtualRouterProfileMaxRouteMaps.setStatus(_A)
_AlaVirtualRouterProfileMaxSequences_Type=Integer32
_AlaVirtualRouterProfileMaxSequences_Object=MibTableColumn
alaVirtualRouterProfileMaxSequences=_AlaVirtualRouterProfileMaxSequences_Object((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,1,1,3,1,3),_AlaVirtualRouterProfileMaxSequences_Type())
alaVirtualRouterProfileMaxSequences.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVirtualRouterProfileMaxSequences.setStatus(_A)
_AlaVirtualRouterProfileMaxTlvs_Type=Integer32
_AlaVirtualRouterProfileMaxTlvs_Object=MibTableColumn
alaVirtualRouterProfileMaxTlvs=_AlaVirtualRouterProfileMaxTlvs_Object((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,1,1,3,1,4),_AlaVirtualRouterProfileMaxTlvs_Type())
alaVirtualRouterProfileMaxTlvs.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVirtualRouterProfileMaxTlvs.setStatus(_A)
_AlaVirtualRouterProfileMaxAccessLists_Type=Integer32
_AlaVirtualRouterProfileMaxAccessLists_Object=MibTableColumn
alaVirtualRouterProfileMaxAccessLists=_AlaVirtualRouterProfileMaxAccessLists_Object((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,1,1,3,1,5),_AlaVirtualRouterProfileMaxAccessLists_Type())
alaVirtualRouterProfileMaxAccessLists.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVirtualRouterProfileMaxAccessLists.setStatus(_A)
_AlaVirtualRouterProfileMaxAddressBlocks_Type=Integer32
_AlaVirtualRouterProfileMaxAddressBlocks_Object=MibTableColumn
alaVirtualRouterProfileMaxAddressBlocks=_AlaVirtualRouterProfileMaxAddressBlocks_Object((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,1,1,3,1,6),_AlaVirtualRouterProfileMaxAddressBlocks_Type())
alaVirtualRouterProfileMaxAddressBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVirtualRouterProfileMaxAddressBlocks.setStatus(_A)
_AlaVirtualRouterProfileMaxMatchInterfaces_Type=Integer32
_AlaVirtualRouterProfileMaxMatchInterfaces_Object=MibTableColumn
alaVirtualRouterProfileMaxMatchInterfaces=_AlaVirtualRouterProfileMaxMatchInterfaces_Object((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,1,1,3,1,7),_AlaVirtualRouterProfileMaxMatchInterfaces_Type())
alaVirtualRouterProfileMaxMatchInterfaces.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVirtualRouterProfileMaxMatchInterfaces.setStatus(_A)
_AlcatelIND1VirtualRouterMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1VirtualRouterMIBConformance=_AlcatelIND1VirtualRouterMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,2))
_AlcatelIND1VirtualRouterMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1VirtualRouterMIBCompliances=_AlcatelIND1VirtualRouterMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,2,1))
_AlcatelIND1VirtualRouterMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1VirtualRouterMIBGroups=_AlcatelIND1VirtualRouterMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,2,2))
alaVirtualRouterConfigMIBGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,2,2,1))
alaVirtualRouterConfigMIBGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:alaVirtualRouterConfigMIBGroup.setStatus(_A)
alaVirtualRouterCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,10,15,1,2,1,1))
alaVirtualRouterCompliance.setObjects((_B,_p))
if mibBuilder.loadTexts:alaVirtualRouterCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alcatelIND1VirtualRouterMIB':alcatelIND1VirtualRouterMIB,'alcatelIND1VirtualRouterMIBObjects':alcatelIND1VirtualRouterMIBObjects,'alaVirtualRouterConfig':alaVirtualRouterConfig,'alaVirtualRouterNameTable':alaVirtualRouterNameTable,'alaVirtualRouterNameEntry':alaVirtualRouterNameEntry,_M:alaVirtualRouterName,_P:alaVirtualRouterNameIndex,_Q:alaVirtualRouterNameRowStatus,_R:alaVirtualRouterProfile,_S:alaVirtualRouterMaxRouteMaps,_T:alaVirtualRouterMaxSequences,_U:alaVirtualRouterMaxTlvs,_V:alaVirtualRouterMaxAccessLists,_W:alaVirtualRouterMaxAddressBlocks,_X:alaVirtualRouterMaxMatchInterfaces,_Y:alaVirtualRouterNoAutoLoadVrrp,'alaVrConfigTable':alaVrConfigTable,'alaVrConfigEntry':alaVrConfigEntry,_N:alaVrConfigIndex,_Z:alaVrConfigRipStatus,_a:alaVrConfigOspfStatus,_b:alaVrConfigIsisStatus,_c:alaVrConfigBgpStatus,_d:alaVrConfigPimStatus,_e:alaVrConfigDvmrpStatus,_f:alaVrConfigRipngStatus,_g:alaVrConfigOspf3Status,_h:alaVrConfigMplsLdpStatus,_i:alaVrConfigVrrpStatus,'alaVirtualRouterProfileTable':alaVirtualRouterProfileTable,'alaVirtualRouterProfileEntry':alaVirtualRouterProfileEntry,_O:alaVirtualRouterProfileName,_j:alaVirtualRouterProfileMaxRouteMaps,_k:alaVirtualRouterProfileMaxSequences,_l:alaVirtualRouterProfileMaxTlvs,_m:alaVirtualRouterProfileMaxAccessLists,_n:alaVirtualRouterProfileMaxAddressBlocks,_o:alaVirtualRouterProfileMaxMatchInterfaces,'alcatelIND1VirtualRouterMIBConformance':alcatelIND1VirtualRouterMIBConformance,'alcatelIND1VirtualRouterMIBCompliances':alcatelIND1VirtualRouterMIBCompliances,'alaVirtualRouterCompliance':alaVirtualRouterCompliance,'alcatelIND1VirtualRouterMIBGroups':alcatelIND1VirtualRouterMIBGroups,_p:alaVirtualRouterConfigMIBGroup})