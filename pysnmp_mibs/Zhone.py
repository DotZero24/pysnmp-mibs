_G='zhoneShelfSlotGroup'
_F='read-only'
_E='zhoneSlotIndex'
_D='zhoneShelfIndex'
_C='Integer32'
_B='Zhone'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
zhone=ModuleIdentity((1,3,6,1,4,1,5504))
if mibBuilder.loadTexts:zhone.setRevisions(('2011-12-05 16:58','2011-05-06 00:20','2010-02-19 10:51','2009-05-27 02:08','2008-01-23 11:46','2007-11-09 13:05','2007-10-16 10:26','2007-02-17 13:43','2006-06-09 12:48','2005-12-01 14:20','2004-10-13 14:40','2004-10-08 11:15','2004-08-11 15:42','2004-01-30 13:34','2003-10-28 11:03','2003-07-17 14:29','2002-03-04 15:34','2001-10-09 12:07','2000-09-28 16:32','2000-12-18 16:32','2000-12-20 17:20','2001-02-07 17:11','2001-02-22 11:35','2001-04-10 14:35','2001-05-15 10:32','2001-06-26 17:06','2001-06-28 13:33','2001-07-31 08:51','2001-08-29 16:56','2001-08-31 15:33'))
_ZhoneRegistrations_ObjectIdentity=ObjectIdentity
zhoneRegistrations=_ZhoneRegistrations_ObjectIdentity((1,3,6,1,4,1,5504,1))
if mibBuilder.loadTexts:zhoneRegistrations.setStatus(_A)
_ZhoneRegPls_ObjectIdentity=ObjectIdentity
zhoneRegPls=_ZhoneRegPls_ObjectIdentity((1,3,6,1,4,1,5504,1,1))
if mibBuilder.loadTexts:zhoneRegPls.setStatus(_A)
_ZhoneRegCpe_ObjectIdentity=ObjectIdentity
zhoneRegCpe=_ZhoneRegCpe_ObjectIdentity((1,3,6,1,4,1,5504,1,2))
if mibBuilder.loadTexts:zhoneRegCpe.setStatus(_A)
_ZhoneRegMux_ObjectIdentity=ObjectIdentity
zhoneRegMux=_ZhoneRegMux_ObjectIdentity((1,3,6,1,4,1,5504,1,3))
if mibBuilder.loadTexts:zhoneRegMux.setStatus(_A)
_ZhoneRegSechtor_ObjectIdentity=ObjectIdentity
zhoneRegSechtor=_ZhoneRegSechtor_ObjectIdentity((1,3,6,1,4,1,5504,1,4))
if mibBuilder.loadTexts:zhoneRegSechtor.setStatus(_A)
_ZhoneRegWtn_ObjectIdentity=ObjectIdentity
zhoneRegWtn=_ZhoneRegWtn_ObjectIdentity((1,3,6,1,4,1,5504,1,5))
if mibBuilder.loadTexts:zhoneRegWtn.setStatus(_A)
_ZhoneRegMalc_ObjectIdentity=ObjectIdentity
zhoneRegMalc=_ZhoneRegMalc_ObjectIdentity((1,3,6,1,4,1,5504,1,6))
if mibBuilder.loadTexts:zhoneRegMalc.setStatus(_A)
_ZhoneProduct_ObjectIdentity=ObjectIdentity
zhoneProduct=_ZhoneProduct_ObjectIdentity((1,3,6,1,4,1,5504,2))
if mibBuilder.loadTexts:zhoneProduct.setStatus(_A)
_ZhonePls_ObjectIdentity=ObjectIdentity
zhonePls=_ZhonePls_ObjectIdentity((1,3,6,1,4,1,5504,2,1))
if mibBuilder.loadTexts:zhonePls.setStatus(_A)
_ZhoneZedge_ObjectIdentity=ObjectIdentity
zhoneZedge=_ZhoneZedge_ObjectIdentity((1,3,6,1,4,1,5504,2,2))
if mibBuilder.loadTexts:zhoneZedge.setStatus(_A)
_ZhoneZplex_ObjectIdentity=ObjectIdentity
zhoneZplex=_ZhoneZplex_ObjectIdentity((1,3,6,1,4,1,5504,2,3))
if mibBuilder.loadTexts:zhoneZplex.setStatus(_A)
_ZhoneSechtor_ObjectIdentity=ObjectIdentity
zhoneSechtor=_ZhoneSechtor_ObjectIdentity((1,3,6,1,4,1,5504,2,4))
if mibBuilder.loadTexts:zhoneSechtor.setStatus(_A)
_Sechtor100_ObjectIdentity=ObjectIdentity
sechtor100=_Sechtor100_ObjectIdentity((1,3,6,1,4,1,5504,2,4,1))
if mibBuilder.loadTexts:sechtor100.setStatus(_A)
_Sechtor300_ObjectIdentity=ObjectIdentity
sechtor300=_Sechtor300_ObjectIdentity((1,3,6,1,4,1,5504,2,4,2))
if mibBuilder.loadTexts:sechtor300.setStatus(_A)
_ZhoneWtn_ObjectIdentity=ObjectIdentity
zhoneWtn=_ZhoneWtn_ObjectIdentity((1,3,6,1,4,1,5504,2,5))
if mibBuilder.loadTexts:zhoneWtn.setStatus(_A)
_ZhoneMalc_ObjectIdentity=ObjectIdentity
zhoneMalc=_ZhoneMalc_ObjectIdentity((1,3,6,1,4,1,5504,2,6))
if mibBuilder.loadTexts:zhoneMalc.setStatus(_A)
_ZhoneZmsProduct_ObjectIdentity=ObjectIdentity
zhoneZmsProduct=_ZhoneZmsProduct_ObjectIdentity((1,3,6,1,4,1,5504,2,7))
if mibBuilder.loadTexts:zhoneZmsProduct.setStatus(_A)
_ZhoneGeneric_ObjectIdentity=ObjectIdentity
zhoneGeneric=_ZhoneGeneric_ObjectIdentity((1,3,6,1,4,1,5504,3))
if mibBuilder.loadTexts:zhoneGeneric.setStatus(_A)
_ZhoneSystem_ObjectIdentity=ObjectIdentity
zhoneSystem=_ZhoneSystem_ObjectIdentity((1,3,6,1,4,1,5504,3,1))
if mibBuilder.loadTexts:zhoneSystem.setStatus(_A)
_ZhoneShelf_ObjectIdentity=ObjectIdentity
zhoneShelf=_ZhoneShelf_ObjectIdentity((1,3,6,1,4,1,5504,3,2))
if mibBuilder.loadTexts:zhoneShelf.setStatus(_A)
_ZhoneCard_ObjectIdentity=ObjectIdentity
zhoneCard=_ZhoneCard_ObjectIdentity((1,3,6,1,4,1,5504,3,3))
if mibBuilder.loadTexts:zhoneCard.setStatus(_A)
_ZhoneSubscriber_ObjectIdentity=ObjectIdentity
zhoneSubscriber=_ZhoneSubscriber_ObjectIdentity((1,3,6,1,4,1,5504,3,4))
if mibBuilder.loadTexts:zhoneSubscriber.setStatus(_A)
_ZhoneInterfaceTranslation_ObjectIdentity=ObjectIdentity
zhoneInterfaceTranslation=_ZhoneInterfaceTranslation_ObjectIdentity((1,3,6,1,4,1,5504,3,5))
if mibBuilder.loadTexts:zhoneInterfaceTranslation.setStatus(_A)
_ZhoneInterfaceGroup_ObjectIdentity=ObjectIdentity
zhoneInterfaceGroup=_ZhoneInterfaceGroup_ObjectIdentity((1,3,6,1,4,1,5504,3,6))
if mibBuilder.loadTexts:zhoneInterfaceGroup.setStatus(_A)
_ZhoneMasterAgent_ObjectIdentity=ObjectIdentity
zhoneMasterAgent=_ZhoneMasterAgent_ObjectIdentity((1,3,6,1,4,1,5504,3,7))
if mibBuilder.loadTexts:zhoneMasterAgent.setStatus(_A)
_ZhoneTrapModules_ObjectIdentity=ObjectIdentity
zhoneTrapModules=_ZhoneTrapModules_ObjectIdentity((1,3,6,1,4,1,5504,3,8))
if mibBuilder.loadTexts:zhoneTrapModules.setStatus(_A)
_ZhoneGenWtn_ObjectIdentity=ObjectIdentity
zhoneGenWtn=_ZhoneGenWtn_ObjectIdentity((1,3,6,1,4,1,5504,3,9))
if mibBuilder.loadTexts:zhoneGenWtn.setStatus(_A)
_ZhoneZAP_ObjectIdentity=ObjectIdentity
zhoneZAP=_ZhoneZAP_ObjectIdentity((1,3,6,1,4,1,5504,3,10))
if mibBuilder.loadTexts:zhoneZAP.setStatus(_A)
_ZhoneVoiceStats_ObjectIdentity=ObjectIdentity
zhoneVoiceStats=_ZhoneVoiceStats_ObjectIdentity((1,3,6,1,4,1,5504,3,11))
if mibBuilder.loadTexts:zhoneVoiceStats.setStatus(_A)
_ZhoneSFF_ObjectIdentity=ObjectIdentity
zhoneSFF=_ZhoneSFF_ObjectIdentity((1,3,6,1,4,1,5504,3,12))
if mibBuilder.loadTexts:zhoneSFF.setStatus(_A)
_ZhoneInterfaceConfig_ObjectIdentity=ObjectIdentity
zhoneInterfaceConfig=_ZhoneInterfaceConfig_ObjectIdentity((1,3,6,1,4,1,5504,3,13))
if mibBuilder.loadTexts:zhoneInterfaceConfig.setStatus(_A)
_ZhoneCommunicationProtocols_ObjectIdentity=ObjectIdentity
zhoneCommunicationProtocols=_ZhoneCommunicationProtocols_ObjectIdentity((1,3,6,1,4,1,5504,4))
if mibBuilder.loadTexts:zhoneCommunicationProtocols.setStatus(_A)
_ZhoneIp_ObjectIdentity=ObjectIdentity
zhoneIp=_ZhoneIp_ObjectIdentity((1,3,6,1,4,1,5504,4,1))
if mibBuilder.loadTexts:zhoneIp.setStatus(_A)
_ZhoneAtm_ObjectIdentity=ObjectIdentity
zhoneAtm=_ZhoneAtm_ObjectIdentity((1,3,6,1,4,1,5504,4,2))
if mibBuilder.loadTexts:zhoneAtm.setStatus(_A)
_ZhoneVoice_ObjectIdentity=ObjectIdentity
zhoneVoice=_ZhoneVoice_ObjectIdentity((1,3,6,1,4,1,5504,4,3))
if mibBuilder.loadTexts:zhoneVoice.setStatus(_A)
_ZhoneVoip_ObjectIdentity=ObjectIdentity
zhoneVoip=_ZhoneVoip_ObjectIdentity((1,3,6,1,4,1,5504,4,4))
if mibBuilder.loadTexts:zhoneVoip.setStatus(_A)
_ZhonePpp_ObjectIdentity=ObjectIdentity
zhonePpp=_ZhonePpp_ObjectIdentity((1,3,6,1,4,1,5504,4,5))
if mibBuilder.loadTexts:zhonePpp.setStatus(_A)
_ZhoneIma_ObjectIdentity=ObjectIdentity
zhoneIma=_ZhoneIma_ObjectIdentity((1,3,6,1,4,1,5504,4,6))
if mibBuilder.loadTexts:zhoneIma.setStatus(_A)
_ZhoneBridge_ObjectIdentity=ObjectIdentity
zhoneBridge=_ZhoneBridge_ObjectIdentity((1,3,6,1,4,1,5504,4,7))
if mibBuilder.loadTexts:zhoneBridge.setStatus(_A)
_ZhoneVideo_ObjectIdentity=ObjectIdentity
zhoneVideo=_ZhoneVideo_ObjectIdentity((1,3,6,1,4,1,5504,4,8))
if mibBuilder.loadTexts:zhoneVideo.setStatus(_A)
_ZhoneIsdn_ObjectIdentity=ObjectIdentity
zhoneIsdn=_ZhoneIsdn_ObjectIdentity((1,3,6,1,4,1,5504,4,9))
if mibBuilder.loadTexts:zhoneIsdn.setStatus(_A)
_ZhoneCes_ObjectIdentity=ObjectIdentity
zhoneCes=_ZhoneCes_ObjectIdentity((1,3,6,1,4,1,5504,4,10))
if mibBuilder.loadTexts:zhoneCes.setStatus(_A)
_ZhoneSs7_ObjectIdentity=ObjectIdentity
zhoneSs7=_ZhoneSs7_ObjectIdentity((1,3,6,1,4,1,5504,4,11))
if mibBuilder.loadTexts:zhoneSs7.setStatus(_A)
_ZhoneClass5_ObjectIdentity=ObjectIdentity
zhoneClass5=_ZhoneClass5_ObjectIdentity((1,3,6,1,4,1,5504,4,12))
if mibBuilder.loadTexts:zhoneClass5.setStatus(_A)
_ZhoneBonding_ObjectIdentity=ObjectIdentity
zhoneBonding=_ZhoneBonding_ObjectIdentity((1,3,6,1,4,1,5504,4,13))
if mibBuilder.loadTexts:zhoneBonding.setStatus(_A)
_ZhoneRadius_ObjectIdentity=ObjectIdentity
zhoneRadius=_ZhoneRadius_ObjectIdentity((1,3,6,1,4,1,5504,4,14))
if mibBuilder.loadTexts:zhoneRadius.setStatus(_A)
_ZhoneIua_ObjectIdentity=ObjectIdentity
zhoneIua=_ZhoneIua_ObjectIdentity((1,3,6,1,4,1,5504,4,15))
if mibBuilder.loadTexts:zhoneIua.setStatus(_A)
_Zhone802Dot1Mibs_ObjectIdentity=ObjectIdentity
zhone802Dot1Mibs=_Zhone802Dot1Mibs_ObjectIdentity((1,3,6,1,4,1,5504,4,16))
if mibBuilder.loadTexts:zhone802Dot1Mibs.setStatus(_A)
_ZhonePtp_ObjectIdentity=ObjectIdentity
zhonePtp=_ZhonePtp_ObjectIdentity((1,3,6,1,4,1,5504,4,17))
if mibBuilder.loadTexts:zhonePtp.setStatus(_A)
_ZhonePhysical_ObjectIdentity=ObjectIdentity
zhonePhysical=_ZhonePhysical_ObjectIdentity((1,3,6,1,4,1,5504,5))
if mibBuilder.loadTexts:zhonePhysical.setStatus(_A)
_ZhoneEnet_ObjectIdentity=ObjectIdentity
zhoneEnet=_ZhoneEnet_ObjectIdentity((1,3,6,1,4,1,5504,5,1))
if mibBuilder.loadTexts:zhoneEnet.setStatus(_A)
_ZhoneDsx_ObjectIdentity=ObjectIdentity
zhoneDsx=_ZhoneDsx_ObjectIdentity((1,3,6,1,4,1,5504,5,2))
if mibBuilder.loadTexts:zhoneDsx.setStatus(_A)
_ZhoneOcx_ObjectIdentity=ObjectIdentity
zhoneOcx=_ZhoneOcx_ObjectIdentity((1,3,6,1,4,1,5504,5,3))
if mibBuilder.loadTexts:zhoneOcx.setStatus(_A)
_ZhoneDsl_ObjectIdentity=ObjectIdentity
zhoneDsl=_ZhoneDsl_ObjectIdentity((1,3,6,1,4,1,5504,5,4))
if mibBuilder.loadTexts:zhoneDsl.setStatus(_A)
_ZhoneConsole_ObjectIdentity=ObjectIdentity
zhoneConsole=_ZhoneConsole_ObjectIdentity((1,3,6,1,4,1,5504,5,5))
if mibBuilder.loadTexts:zhoneConsole.setStatus(_A)
_ZhoneRadio_ObjectIdentity=ObjectIdentity
zhoneRadio=_ZhoneRadio_ObjectIdentity((1,3,6,1,4,1,5504,5,8))
if mibBuilder.loadTexts:zhoneRadio.setStatus(_A)
_ZhoneSonet_ObjectIdentity=ObjectIdentity
zhoneSonet=_ZhoneSonet_ObjectIdentity((1,3,6,1,4,1,5504,5,9))
if mibBuilder.loadTexts:zhoneSonet.setStatus(_A)
_ZhoneDs3Ext_ObjectIdentity=ObjectIdentity
zhoneDs3Ext=_ZhoneDs3Ext_ObjectIdentity((1,3,6,1,4,1,5504,5,10))
if mibBuilder.loadTexts:zhoneDs3Ext.setStatus(_A)
_ZhoneLineTypes_ObjectIdentity=ObjectIdentity
zhoneLineTypes=_ZhoneLineTypes_ObjectIdentity((1,3,6,1,4,1,5504,5,11))
if mibBuilder.loadTexts:zhoneLineTypes.setStatus(_A)
_ZhoneApon_ObjectIdentity=ObjectIdentity
zhoneApon=_ZhoneApon_ObjectIdentity((1,3,6,1,4,1,5504,5,12))
if mibBuilder.loadTexts:zhoneApon.setStatus(_A)
_ZhoneVdsl_ObjectIdentity=ObjectIdentity
zhoneVdsl=_ZhoneVdsl_ObjectIdentity((1,3,6,1,4,1,5504,5,13))
if mibBuilder.loadTexts:zhoneVdsl.setStatus(_A)
_ZhoneGpon_ObjectIdentity=ObjectIdentity
zhoneGpon=_ZhoneGpon_ObjectIdentity((1,3,6,1,4,1,5504,5,14))
if mibBuilder.loadTexts:zhoneGpon.setStatus(_A)
_ZhoneWdm_ObjectIdentity=ObjectIdentity
zhoneWdm=_ZhoneWdm_ObjectIdentity((1,3,6,1,4,1,5504,5,15))
if mibBuilder.loadTexts:zhoneWdm.setStatus(_A)
_ZhoneCpe_ObjectIdentity=ObjectIdentity
zhoneCpe=_ZhoneCpe_ObjectIdentity((1,3,6,1,4,1,5504,5,16))
if mibBuilder.loadTexts:zhoneCpe.setStatus(_A)
_ZhoneModules_ObjectIdentity=ObjectIdentity
zhoneModules=_ZhoneModules_ObjectIdentity((1,3,6,1,4,1,5504,6))
if mibBuilder.loadTexts:zhoneModules.setStatus(_A)
_ZhoneShelfSlotTable_Object=MibTable
zhoneShelfSlotTable=_ZhoneShelfSlotTable_Object((1,3,6,1,4,1,5504,7))
if mibBuilder.loadTexts:zhoneShelfSlotTable.setStatus(_A)
_ZhoneShelfSlotEntry_Object=MibTableRow
zhoneShelfSlotEntry=_ZhoneShelfSlotEntry_Object((1,3,6,1,4,1,5504,7,1))
zhoneShelfSlotEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:zhoneShelfSlotEntry.setStatus(_A)
class _ZhoneShelfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ZhoneShelfIndex_Type.__name__=_C
_ZhoneShelfIndex_Object=MibTableColumn
zhoneShelfIndex=_ZhoneShelfIndex_Object((1,3,6,1,4,1,5504,7,1,1),_ZhoneShelfIndex_Type())
zhoneShelfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneShelfIndex.setStatus(_A)
class _ZhoneSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_ZhoneSlotIndex_Type.__name__=_C
_ZhoneSlotIndex_Object=MibTableColumn
zhoneSlotIndex=_ZhoneSlotIndex_Object((1,3,6,1,4,1,5504,7,1,2),_ZhoneSlotIndex_Type())
zhoneSlotIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneSlotIndex.setStatus(_A)
_ZhoneCompliances_ObjectIdentity=ObjectIdentity
zhoneCompliances=_ZhoneCompliances_ObjectIdentity((1,3,6,1,4,1,5504,9))
_ZhoneGroups_ObjectIdentity=ObjectIdentity
zhoneGroups=_ZhoneGroups_ObjectIdentity((1,3,6,1,4,1,5504,9,1))
_ZhoneCompliance_ObjectIdentity=ObjectIdentity
zhoneCompliance=_ZhoneCompliance_ObjectIdentity((1,3,6,1,4,1,5504,9,2))
_ZhoneExperimental_ObjectIdentity=ObjectIdentity
zhoneExperimental=_ZhoneExperimental_ObjectIdentity((1,3,6,1,4,1,5504,10))
if mibBuilder.loadTexts:zhoneExperimental.setStatus(_A)
_IetfDrafts_ObjectIdentity=ObjectIdentity
ietfDrafts=_IetfDrafts_ObjectIdentity((1,3,6,1,4,1,5504,10,1))
if mibBuilder.loadTexts:ietfDrafts.setStatus(_A)
_ApsMIB_ObjectIdentity=ObjectIdentity
apsMIB=_ApsMIB_ObjectIdentity((1,3,6,1,4,1,5504,10,1,1))
if mibBuilder.loadTexts:apsMIB.setStatus(_A)
_SipTC_ObjectIdentity=ObjectIdentity
sipTC=_SipTC_ObjectIdentity((1,3,6,1,4,1,5504,10,1,2))
if mibBuilder.loadTexts:sipTC.setStatus(_A)
_SipCommonMIB_ObjectIdentity=ObjectIdentity
sipCommonMIB=_SipCommonMIB_ObjectIdentity((1,3,6,1,4,1,5504,10,1,3))
if mibBuilder.loadTexts:sipCommonMIB.setStatus(_A)
_SipUAMIB_ObjectIdentity=ObjectIdentity
sipUAMIB=_SipUAMIB_ObjectIdentity((1,3,6,1,4,1,5504,10,1,4))
if mibBuilder.loadTexts:sipUAMIB.setStatus(_A)
_PktcIetfSigMib_ObjectIdentity=ObjectIdentity
pktcIetfSigMib=_PktcIetfSigMib_ObjectIdentity((1,3,6,1,4,1,5504,10,1,5))
if mibBuilder.loadTexts:pktcIetfSigMib.setStatus(_A)
_EfmOamMIB_ObjectIdentity=ObjectIdentity
efmOamMIB=_EfmOamMIB_ObjectIdentity((1,3,6,1,4,1,5504,10,1,6))
if mibBuilder.loadTexts:efmOamMIB.setStatus(_A)
_EfmCuMIB_ObjectIdentity=ObjectIdentity
efmCuMIB=_EfmCuMIB_ObjectIdentity((1,3,6,1,4,1,5504,10,1,7))
if mibBuilder.loadTexts:efmCuMIB.setStatus(_A)
_PwTcStdMIB_ObjectIdentity=ObjectIdentity
pwTcStdMIB=_PwTcStdMIB_ObjectIdentity((1,3,6,1,4,1,5504,10,1,8))
if mibBuilder.loadTexts:pwTcStdMIB.setStatus(_A)
_IanaPwe3MIB_ObjectIdentity=ObjectIdentity
ianaPwe3MIB=_IanaPwe3MIB_ObjectIdentity((1,3,6,1,4,1,5504,10,1,9))
if mibBuilder.loadTexts:ianaPwe3MIB.setStatus(_A)
_PwStdMIB_ObjectIdentity=ObjectIdentity
pwStdMIB=_PwStdMIB_ObjectIdentity((1,3,6,1,4,1,5504,10,1,10))
if mibBuilder.loadTexts:pwStdMIB.setStatus(_A)
_PwTDMMIB_ObjectIdentity=ObjectIdentity
pwTDMMIB=_PwTDMMIB_ObjectIdentity((1,3,6,1,4,1,5504,10,1,11))
if mibBuilder.loadTexts:pwTDMMIB.setStatus(_A)
_ZhoneRmonMibModule_ObjectIdentity=ObjectIdentity
zhoneRmonMibModule=_ZhoneRmonMibModule_ObjectIdentity((1,3,6,1,4,1,5504,10,1,12))
if mibBuilder.loadTexts:zhoneRmonMibModule.setStatus(_A)
_ZhoneDrafts_ObjectIdentity=ObjectIdentity
zhoneDrafts=_ZhoneDrafts_ObjectIdentity((1,3,6,1,4,1,5504,10,2))
if mibBuilder.loadTexts:zhoneDrafts.setStatus(_A)
zhoneShelfSlotGroup=ObjectGroup((1,3,6,1,4,1,5504,9,1,1))
zhoneShelfSlotGroup.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:zhoneShelfSlotGroup.setStatus(_A)
zhoneShelfSlotCompliance=ModuleCompliance((1,3,6,1,4,1,5504,9,2,1))
zhoneShelfSlotCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:zhoneShelfSlotCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'zhone':zhone,'zhoneRegistrations':zhoneRegistrations,'zhoneRegPls':zhoneRegPls,'zhoneRegCpe':zhoneRegCpe,'zhoneRegMux':zhoneRegMux,'zhoneRegSechtor':zhoneRegSechtor,'zhoneRegWtn':zhoneRegWtn,'zhoneRegMalc':zhoneRegMalc,'zhoneProduct':zhoneProduct,'zhonePls':zhonePls,'zhoneZedge':zhoneZedge,'zhoneZplex':zhoneZplex,'zhoneSechtor':zhoneSechtor,'sechtor100':sechtor100,'sechtor300':sechtor300,'zhoneWtn':zhoneWtn,'zhoneMalc':zhoneMalc,'zhoneZmsProduct':zhoneZmsProduct,'zhoneGeneric':zhoneGeneric,'zhoneSystem':zhoneSystem,'zhoneShelf':zhoneShelf,'zhoneCard':zhoneCard,'zhoneSubscriber':zhoneSubscriber,'zhoneInterfaceTranslation':zhoneInterfaceTranslation,'zhoneInterfaceGroup':zhoneInterfaceGroup,'zhoneMasterAgent':zhoneMasterAgent,'zhoneTrapModules':zhoneTrapModules,'zhoneGenWtn':zhoneGenWtn,'zhoneZAP':zhoneZAP,'zhoneVoiceStats':zhoneVoiceStats,'zhoneSFF':zhoneSFF,'zhoneInterfaceConfig':zhoneInterfaceConfig,'zhoneCommunicationProtocols':zhoneCommunicationProtocols,'zhoneIp':zhoneIp,'zhoneAtm':zhoneAtm,'zhoneVoice':zhoneVoice,'zhoneVoip':zhoneVoip,'zhonePpp':zhonePpp,'zhoneIma':zhoneIma,'zhoneBridge':zhoneBridge,'zhoneVideo':zhoneVideo,'zhoneIsdn':zhoneIsdn,'zhoneCes':zhoneCes,'zhoneSs7':zhoneSs7,'zhoneClass5':zhoneClass5,'zhoneBonding':zhoneBonding,'zhoneRadius':zhoneRadius,'zhoneIua':zhoneIua,'zhone802Dot1Mibs':zhone802Dot1Mibs,'zhonePtp':zhonePtp,'zhonePhysical':zhonePhysical,'zhoneEnet':zhoneEnet,'zhoneDsx':zhoneDsx,'zhoneOcx':zhoneOcx,'zhoneDsl':zhoneDsl,'zhoneConsole':zhoneConsole,'zhoneRadio':zhoneRadio,'zhoneSonet':zhoneSonet,'zhoneDs3Ext':zhoneDs3Ext,'zhoneLineTypes':zhoneLineTypes,'zhoneApon':zhoneApon,'zhoneVdsl':zhoneVdsl,'zhoneGpon':zhoneGpon,'zhoneWdm':zhoneWdm,'zhoneCpe':zhoneCpe,'zhoneModules':zhoneModules,'zhoneShelfSlotTable':zhoneShelfSlotTable,'zhoneShelfSlotEntry':zhoneShelfSlotEntry,_D:zhoneShelfIndex,_E:zhoneSlotIndex,'zhoneCompliances':zhoneCompliances,'zhoneGroups':zhoneGroups,_G:zhoneShelfSlotGroup,'zhoneCompliance':zhoneCompliance,'zhoneShelfSlotCompliance':zhoneShelfSlotCompliance,'zhoneExperimental':zhoneExperimental,'ietfDrafts':ietfDrafts,'apsMIB':apsMIB,'sipTC':sipTC,'sipCommonMIB':sipCommonMIB,'sipUAMIB':sipUAMIB,'pktcIetfSigMib':pktcIetfSigMib,'efmOamMIB':efmOamMIB,'efmCuMIB':efmCuMIB,'pwTcStdMIB':pwTcStdMIB,'ianaPwe3MIB':ianaPwe3MIB,'pwStdMIB':pwStdMIB,'pwTDMMIB':pwTDMMIB,'zhoneRmonMibModule':zhoneRmonMibModule,'zhoneDrafts':zhoneDrafts})