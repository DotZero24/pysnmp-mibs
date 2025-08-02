_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
utCommonMib=ModuleIdentity((1,3,6,1,4,1,1949,1,1,1,1))
if mibBuilder.loadTexts:utCommonMib.setRevisions(('2002-04-28 00:00','2004-08-19 00:00','2004-09-21 00:00','2005-05-08 00:00'))
_Utstarcom_ObjectIdentity=ObjectIdentity
utstarcom=_Utstarcom_ObjectIdentity((1,3,6,1,4,1,1949))
_UtsRoot_ObjectIdentity=ObjectIdentity
utsRoot=_UtsRoot_ObjectIdentity((1,3,6,1,4,1,1949,1))
if mibBuilder.loadTexts:utsRoot.setStatus(_A)
_UtsReg_ObjectIdentity=ObjectIdentity
utsReg=_UtsReg_ObjectIdentity((1,3,6,1,4,1,1949,1,1))
if mibBuilder.loadTexts:utsReg.setStatus(_A)
_UtModules_ObjectIdentity=ObjectIdentity
utModules=_UtModules_ObjectIdentity((1,3,6,1,4,1,1949,1,1,1))
if mibBuilder.loadTexts:utModules.setStatus(_A)
_UtUmtsModules_ObjectIdentity=ObjectIdentity
utUmtsModules=_UtUmtsModules_ObjectIdentity((1,3,6,1,4,1,1949,1,1,1,2))
if mibBuilder.loadTexts:utUmtsModules.setStatus(_A)
_UtEmbeddedPlatformModules_ObjectIdentity=ObjectIdentity
utEmbeddedPlatformModules=_UtEmbeddedPlatformModules_ObjectIdentity((1,3,6,1,4,1,1949,1,1,1,5))
if mibBuilder.loadTexts:utEmbeddedPlatformModules.setStatus(_A)
_UtServerPlatformModules_ObjectIdentity=ObjectIdentity
utServerPlatformModules=_UtServerPlatformModules_ObjectIdentity((1,3,6,1,4,1,1949,1,1,1,6))
if mibBuilder.loadTexts:utServerPlatformModules.setStatus(_A)
_UtCommonPlatformModules_ObjectIdentity=ObjectIdentity
utCommonPlatformModules=_UtCommonPlatformModules_ObjectIdentity((1,3,6,1,4,1,1949,1,1,1,7))
if mibBuilder.loadTexts:utCommonPlatformModules.setStatus(_A)
_UtBroadbandModules_ObjectIdentity=ObjectIdentity
utBroadbandModules=_UtBroadbandModules_ObjectIdentity((1,3,6,1,4,1,1949,1,1,1,8))
if mibBuilder.loadTexts:utBroadbandModules.setStatus(_A)
_UtMediaSwitchModules_ObjectIdentity=ObjectIdentity
utMediaSwitchModules=_UtMediaSwitchModules_ObjectIdentity((1,3,6,1,4,1,1949,1,1,1,9))
if mibBuilder.loadTexts:utMediaSwitchModules.setStatus(_A)
_UtMswitchModules_ObjectIdentity=ObjectIdentity
utMswitchModules=_UtMswitchModules_ObjectIdentity((1,3,6,1,4,1,1949,1,1,1,10))
if mibBuilder.loadTexts:utMswitchModules.setStatus(_A)
_UtAgentCap_ObjectIdentity=ObjectIdentity
utAgentCap=_UtAgentCap_ObjectIdentity((1,3,6,1,4,1,1949,1,1,2))
if mibBuilder.loadTexts:utAgentCap.setStatus(_A)
_UtsGeneric_ObjectIdentity=ObjectIdentity
utsGeneric=_UtsGeneric_ObjectIdentity((1,3,6,1,4,1,1949,1,2))
if mibBuilder.loadTexts:utsGeneric.setStatus(_A)
_UtsProducts_ObjectIdentity=ObjectIdentity
utsProducts=_UtsProducts_ObjectIdentity((1,3,6,1,4,1,1949,1,3))
if mibBuilder.loadTexts:utsProducts.setStatus(_A)
_UtsAn2K_ObjectIdentity=ObjectIdentity
utsAn2K=_UtsAn2K_ObjectIdentity((1,3,6,1,4,1,1949,1,3,1))
if mibBuilder.loadTexts:utsAn2K.setStatus(_A)
_UtsWll_ObjectIdentity=ObjectIdentity
utsWll=_UtsWll_ObjectIdentity((1,3,6,1,4,1,1949,1,3,2))
if mibBuilder.loadTexts:utsWll.setStatus(_A)
_UtsIpDslam_ObjectIdentity=ObjectIdentity
utsIpDslam=_UtsIpDslam_ObjectIdentity((1,3,6,1,4,1,1949,1,3,3))
if mibBuilder.loadTexts:utsIpDslam.setStatus(_A)
_UtsiAN4000_ObjectIdentity=ObjectIdentity
utsiAN4000=_UtsiAN4000_ObjectIdentity((1,3,6,1,4,1,1949,1,3,4))
if mibBuilder.loadTexts:utsiAN4000.setStatus(_A)
_UtsVas_ObjectIdentity=ObjectIdentity
utsVas=_UtsVas_ObjectIdentity((1,3,6,1,4,1,1949,1,3,5))
if mibBuilder.loadTexts:utsVas.setStatus(_A)
_UtsMiniDslam_ObjectIdentity=ObjectIdentity
utsMiniDslam=_UtsMiniDslam_ObjectIdentity((1,3,6,1,4,1,1949,1,3,6))
if mibBuilder.loadTexts:utsMiniDslam.setStatus(_A)
_UtsL2Switch_ObjectIdentity=ObjectIdentity
utsL2Switch=_UtsL2Switch_ObjectIdentity((1,3,6,1,4,1,1949,1,3,7))
if mibBuilder.loadTexts:utsL2Switch.setStatus(_A)
_UtsUmts_ObjectIdentity=ObjectIdentity
utsUmts=_UtsUmts_ObjectIdentity((1,3,6,1,4,1,1949,1,3,8))
if mibBuilder.loadTexts:utsUmts.setStatus(_A)
_UtUmtsFunctions_ObjectIdentity=ObjectIdentity
utUmtsFunctions=_UtUmtsFunctions_ObjectIdentity((1,3,6,1,4,1,1949,1,3,8,1))
if mibBuilder.loadTexts:utUmtsFunctions.setStatus(_A)
_UtUmtsServices_ObjectIdentity=ObjectIdentity
utUmtsServices=_UtUmtsServices_ObjectIdentity((1,3,6,1,4,1,1949,1,3,8,2))
if mibBuilder.loadTexts:utUmtsServices.setStatus(_A)
_UtsSp8000_ObjectIdentity=ObjectIdentity
utsSp8000=_UtsSp8000_ObjectIdentity((1,3,6,1,4,1,1949,1,3,9))
if mibBuilder.loadTexts:utsSp8000.setStatus(_A)
_UtsBroadbandSwitch_ObjectIdentity=ObjectIdentity
utsBroadbandSwitch=_UtsBroadbandSwitch_ObjectIdentity((1,3,6,1,4,1,1949,1,3,10))
if mibBuilder.loadTexts:utsBroadbandSwitch.setStatus(_A)
_UtsMediaSwitch_ObjectIdentity=ObjectIdentity
utsMediaSwitch=_UtsMediaSwitch_ObjectIdentity((1,3,6,1,4,1,1949,1,3,11))
if mibBuilder.loadTexts:utsMediaSwitch.setStatus(_A)
_UtsAirStarEp_ObjectIdentity=ObjectIdentity
utsAirStarEp=_UtsAirStarEp_ObjectIdentity((1,3,6,1,4,1,1949,1,3,12))
if mibBuilder.loadTexts:utsAirStarEp.setStatus(_A)
_UtsMswitch_ObjectIdentity=ObjectIdentity
utsMswitch=_UtsMswitch_ObjectIdentity((1,3,6,1,4,1,1949,1,3,13))
if mibBuilder.loadTexts:utsMswitch.setStatus(_A)
_UtsDslam_ObjectIdentity=ObjectIdentity
utsDslam=_UtsDslam_ObjectIdentity((1,3,6,1,4,1,1949,1,3,14))
if mibBuilder.loadTexts:utsDslam.setStatus(_A)
_UtsAN2000B300_ObjectIdentity=ObjectIdentity
utsAN2000B300=_UtsAN2000B300_ObjectIdentity((1,3,6,1,4,1,1949,1,3,14,1))
if mibBuilder.loadTexts:utsAN2000B300.setStatus(_A)
_UtDslamCommon_ObjectIdentity=ObjectIdentity
utDslamCommon=_UtDslamCommon_ObjectIdentity((1,3,6,1,4,1,1949,1,3,14,2))
if mibBuilder.loadTexts:utDslamCommon.setStatus(_A)
_UtsWlan_ObjectIdentity=ObjectIdentity
utsWlan=_UtsWlan_ObjectIdentity((1,3,6,1,4,1,1949,1,3,15))
if mibBuilder.loadTexts:utsWlan.setStatus(_A)
_UtsCpe_ObjectIdentity=ObjectIdentity
utsCpe=_UtsCpe_ObjectIdentity((1,3,6,1,4,1,1949,1,3,16))
if mibBuilder.loadTexts:utsCpe.setStatus(_A)
_UtsCdma2000_ObjectIdentity=ObjectIdentity
utsCdma2000=_UtsCdma2000_ObjectIdentity((1,3,6,1,4,1,1949,1,3,17))
if mibBuilder.loadTexts:utsCdma2000.setStatus(_A)
_UtCdma2000Functions_ObjectIdentity=ObjectIdentity
utCdma2000Functions=_UtCdma2000Functions_ObjectIdentity((1,3,6,1,4,1,1949,1,3,17,1))
if mibBuilder.loadTexts:utCdma2000Functions.setStatus(_A)
_UtBtsFunctions_ObjectIdentity=ObjectIdentity
utBtsFunctions=_UtBtsFunctions_ObjectIdentity((1,3,6,1,4,1,1949,1,3,17,1,1))
if mibBuilder.loadTexts:utBtsFunctions.setStatus(_A)
_UtiCellBtsFunctions_ObjectIdentity=ObjectIdentity
utiCellBtsFunctions=_UtiCellBtsFunctions_ObjectIdentity((1,3,6,1,4,1,1949,1,3,17,1,1,1))
if mibBuilder.loadTexts:utiCellBtsFunctions.setStatus(_A)
_UtHsiBtsFunctions_ObjectIdentity=ObjectIdentity
utHsiBtsFunctions=_UtHsiBtsFunctions_ObjectIdentity((1,3,6,1,4,1,1949,1,3,17,1,1,2))
if mibBuilder.loadTexts:utHsiBtsFunctions.setStatus(_A)
_UtBscFunctions_ObjectIdentity=ObjectIdentity
utBscFunctions=_UtBscFunctions_ObjectIdentity((1,3,6,1,4,1,1949,1,3,17,1,2))
if mibBuilder.loadTexts:utBscFunctions.setStatus(_A)
_UtiCellBscFunctions_ObjectIdentity=ObjectIdentity
utiCellBscFunctions=_UtiCellBscFunctions_ObjectIdentity((1,3,6,1,4,1,1949,1,3,17,1,2,1))
if mibBuilder.loadTexts:utiCellBscFunctions.setStatus(_A)
_UtHsiBscFunctions_ObjectIdentity=ObjectIdentity
utHsiBscFunctions=_UtHsiBscFunctions_ObjectIdentity((1,3,6,1,4,1,1949,1,3,17,1,2,2))
if mibBuilder.loadTexts:utHsiBscFunctions.setStatus(_A)
_UtMscFunctions_ObjectIdentity=ObjectIdentity
utMscFunctions=_UtMscFunctions_ObjectIdentity((1,3,6,1,4,1,1949,1,3,17,1,3))
if mibBuilder.loadTexts:utMscFunctions.setStatus(_A)
_UtSonataMscFunctions_ObjectIdentity=ObjectIdentity
utSonataMscFunctions=_UtSonataMscFunctions_ObjectIdentity((1,3,6,1,4,1,1949,1,3,17,1,3,1))
if mibBuilder.loadTexts:utSonataMscFunctions.setStatus(_A)
_UtCdma2000Services_ObjectIdentity=ObjectIdentity
utCdma2000Services=_UtCdma2000Services_ObjectIdentity((1,3,6,1,4,1,1949,1,3,17,2))
if mibBuilder.loadTexts:utCdma2000Services.setStatus(_A)
_UtsMsan_ObjectIdentity=ObjectIdentity
utsMsan=_UtsMsan_ObjectIdentity((1,3,6,1,4,1,1949,1,3,18))
if mibBuilder.loadTexts:utsMsan.setStatus(_A)
_UtiAN8000_ObjectIdentity=ObjectIdentity
utiAN8000=_UtiAN8000_ObjectIdentity((1,3,6,1,4,1,1949,1,3,18,1))
if mibBuilder.loadTexts:utiAN8000.setStatus(_A)
_UtsPwlan_ObjectIdentity=ObjectIdentity
utsPwlan=_UtsPwlan_ObjectIdentity((1,3,6,1,4,1,1949,1,3,19))
if mibBuilder.loadTexts:utsPwlan.setStatus(_A)
_UtsRfOverlay_ObjectIdentity=ObjectIdentity
utsRfOverlay=_UtsRfOverlay_ObjectIdentity((1,3,6,1,4,1,1949,1,3,20))
if mibBuilder.loadTexts:utsRfOverlay.setStatus(_A)
_UtsPlatform_ObjectIdentity=ObjectIdentity
utsPlatform=_UtsPlatform_ObjectIdentity((1,3,6,1,4,1,1949,2))
if mibBuilder.loadTexts:utsPlatform.setStatus(_A)
_UtEmbeddedPlatform_ObjectIdentity=ObjectIdentity
utEmbeddedPlatform=_UtEmbeddedPlatform_ObjectIdentity((1,3,6,1,4,1,1949,2,1))
if mibBuilder.loadTexts:utEmbeddedPlatform.setStatus(_A)
_UtChassis_ObjectIdentity=ObjectIdentity
utChassis=_UtChassis_ObjectIdentity((1,3,6,1,4,1,1949,2,1,1))
if mibBuilder.loadTexts:utChassis.setStatus(_A)
_UtRem_ObjectIdentity=ObjectIdentity
utRem=_UtRem_ObjectIdentity((1,3,6,1,4,1,1949,2,1,100))
if mibBuilder.loadTexts:utRem.setStatus(_A)
_UtServerPlatform_ObjectIdentity=ObjectIdentity
utServerPlatform=_UtServerPlatform_ObjectIdentity((1,3,6,1,4,1,1949,2,2))
if mibBuilder.loadTexts:utServerPlatform.setStatus(_A)
_UtCommonPlatform_ObjectIdentity=ObjectIdentity
utCommonPlatform=_UtCommonPlatform_ObjectIdentity((1,3,6,1,4,1,1949,2,3))
if mibBuilder.loadTexts:utCommonPlatform.setStatus(_A)
_UtCommonProtocol_ObjectIdentity=ObjectIdentity
utCommonProtocol=_UtCommonProtocol_ObjectIdentity((1,3,6,1,4,1,1949,2,3,1))
if mibBuilder.loadTexts:utCommonProtocol.setStatus(_A)
_UtCommonOam_ObjectIdentity=ObjectIdentity
utCommonOam=_UtCommonOam_ObjectIdentity((1,3,6,1,4,1,1949,2,3,2))
if mibBuilder.loadTexts:utCommonOam.setStatus(_A)
_UtCommonSyslog_ObjectIdentity=ObjectIdentity
utCommonSyslog=_UtCommonSyslog_ObjectIdentity((1,3,6,1,4,1,1949,2,3,3))
_UtsExperiment_ObjectIdentity=ObjectIdentity
utsExperiment=_UtsExperiment_ObjectIdentity((1,3,6,1,4,1,1949,100))
if mibBuilder.loadTexts:utsExperiment.setStatus(_A)
mibBuilder.exportSymbols('UTS-COMMON-MIB',**{'utstarcom':utstarcom,'utsRoot':utsRoot,'utsReg':utsReg,'utModules':utModules,'utCommonMib':utCommonMib,'utUmtsModules':utUmtsModules,'utEmbeddedPlatformModules':utEmbeddedPlatformModules,'utServerPlatformModules':utServerPlatformModules,'utCommonPlatformModules':utCommonPlatformModules,'utBroadbandModules':utBroadbandModules,'utMediaSwitchModules':utMediaSwitchModules,'utMswitchModules':utMswitchModules,'utAgentCap':utAgentCap,'utsGeneric':utsGeneric,'utsProducts':utsProducts,'utsAn2K':utsAn2K,'utsWll':utsWll,'utsIpDslam':utsIpDslam,'utsiAN4000':utsiAN4000,'utsVas':utsVas,'utsMiniDslam':utsMiniDslam,'utsL2Switch':utsL2Switch,'utsUmts':utsUmts,'utUmtsFunctions':utUmtsFunctions,'utUmtsServices':utUmtsServices,'utsSp8000':utsSp8000,'utsBroadbandSwitch':utsBroadbandSwitch,'utsMediaSwitch':utsMediaSwitch,'utsAirStarEp':utsAirStarEp,'utsMswitch':utsMswitch,'utsDslam':utsDslam,'utsAN2000B300':utsAN2000B300,'utDslamCommon':utDslamCommon,'utsWlan':utsWlan,'utsCpe':utsCpe,'utsCdma2000':utsCdma2000,'utCdma2000Functions':utCdma2000Functions,'utBtsFunctions':utBtsFunctions,'utiCellBtsFunctions':utiCellBtsFunctions,'utHsiBtsFunctions':utHsiBtsFunctions,'utBscFunctions':utBscFunctions,'utiCellBscFunctions':utiCellBscFunctions,'utHsiBscFunctions':utHsiBscFunctions,'utMscFunctions':utMscFunctions,'utSonataMscFunctions':utSonataMscFunctions,'utCdma2000Services':utCdma2000Services,'utsMsan':utsMsan,'utiAN8000':utiAN8000,'utsPwlan':utsPwlan,'utsRfOverlay':utsRfOverlay,'utsPlatform':utsPlatform,'utEmbeddedPlatform':utEmbeddedPlatform,'utChassis':utChassis,'utRem':utRem,'utServerPlatform':utServerPlatform,'utCommonPlatform':utCommonPlatform,'utCommonProtocol':utCommonProtocol,'utCommonOam':utCommonOam,'utCommonSyslog':utCommonSyslog,'utsExperiment':utsExperiment})