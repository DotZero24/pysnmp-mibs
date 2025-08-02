_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
liebertGlobalProductsRegistrationModule=ModuleIdentity((1,3,6,1,4,1,476,1,42,1,1,1))
if mibBuilder.loadTexts:liebertGlobalProductsRegistrationModule.setRevisions(('2015-02-02 00:00','2014-09-17 00:00','2014-06-24 00:00','2014-03-27 00:00','2013-07-10 00:00','2013-05-14 00:00','2009-04-17 00:00','2008-07-02 00:00','2008-01-10 00:00','2006-02-22 00:00'))
_Vertiv_ObjectIdentity=ObjectIdentity
vertiv=_Vertiv_ObjectIdentity((1,3,6,1,4,1,476))
if mibBuilder.loadTexts:vertiv.setStatus(_A)
_LiebertCorp_ObjectIdentity=ObjectIdentity
liebertCorp=_LiebertCorp_ObjectIdentity((1,3,6,1,4,1,476,1))
if mibBuilder.loadTexts:liebertCorp.setStatus(_A)
_LiebertGlobalProducts_ObjectIdentity=ObjectIdentity
liebertGlobalProducts=_LiebertGlobalProducts_ObjectIdentity((1,3,6,1,4,1,476,1,42))
if mibBuilder.loadTexts:liebertGlobalProducts.setStatus(_A)
_LgpModuleReg_ObjectIdentity=ObjectIdentity
lgpModuleReg=_LgpModuleReg_ObjectIdentity((1,3,6,1,4,1,476,1,42,1))
if mibBuilder.loadTexts:lgpModuleReg.setStatus(_A)
_LiebertModuleReg_ObjectIdentity=ObjectIdentity
liebertModuleReg=_LiebertModuleReg_ObjectIdentity((1,3,6,1,4,1,476,1,42,1,1))
if mibBuilder.loadTexts:liebertModuleReg.setStatus(_A)
_LiebertAgentModuleReg_ObjectIdentity=ObjectIdentity
liebertAgentModuleReg=_LiebertAgentModuleReg_ObjectIdentity((1,3,6,1,4,1,476,1,42,1,2))
if mibBuilder.loadTexts:liebertAgentModuleReg.setStatus(_A)
_LiebertConditionsModuleReg_ObjectIdentity=ObjectIdentity
liebertConditionsModuleReg=_LiebertConditionsModuleReg_ObjectIdentity((1,3,6,1,4,1,476,1,42,1,3))
if mibBuilder.loadTexts:liebertConditionsModuleReg.setStatus(_A)
_LiebertNotificationsModuleReg_ObjectIdentity=ObjectIdentity
liebertNotificationsModuleReg=_LiebertNotificationsModuleReg_ObjectIdentity((1,3,6,1,4,1,476,1,42,1,4))
if mibBuilder.loadTexts:liebertNotificationsModuleReg.setStatus(_A)
_LiebertEnvironmentalModuleReg_ObjectIdentity=ObjectIdentity
liebertEnvironmentalModuleReg=_LiebertEnvironmentalModuleReg_ObjectIdentity((1,3,6,1,4,1,476,1,42,1,5))
if mibBuilder.loadTexts:liebertEnvironmentalModuleReg.setStatus(_A)
_LiebertPowerModuleReg_ObjectIdentity=ObjectIdentity
liebertPowerModuleReg=_LiebertPowerModuleReg_ObjectIdentity((1,3,6,1,4,1,476,1,42,1,6))
if mibBuilder.loadTexts:liebertPowerModuleReg.setStatus(_A)
_LiebertControllerModuleReg_ObjectIdentity=ObjectIdentity
liebertControllerModuleReg=_LiebertControllerModuleReg_ObjectIdentity((1,3,6,1,4,1,476,1,42,1,7))
if mibBuilder.loadTexts:liebertControllerModuleReg.setStatus(_A)
_LiebertSystemModuleReg_ObjectIdentity=ObjectIdentity
liebertSystemModuleReg=_LiebertSystemModuleReg_ObjectIdentity((1,3,6,1,4,1,476,1,42,1,8))
if mibBuilder.loadTexts:liebertSystemModuleReg.setStatus(_A)
_LiebertPduModuleReg_ObjectIdentity=ObjectIdentity
liebertPduModuleReg=_LiebertPduModuleReg_ObjectIdentity((1,3,6,1,4,1,476,1,42,1,9))
if mibBuilder.loadTexts:liebertPduModuleReg.setStatus(_A)
_LiebertFlexibleModuleReg_ObjectIdentity=ObjectIdentity
liebertFlexibleModuleReg=_LiebertFlexibleModuleReg_ObjectIdentity((1,3,6,1,4,1,476,1,42,1,10))
if mibBuilder.loadTexts:liebertFlexibleModuleReg.setStatus(_A)
_LiebertFlexibleConditionsModuleReg_ObjectIdentity=ObjectIdentity
liebertFlexibleConditionsModuleReg=_LiebertFlexibleConditionsModuleReg_ObjectIdentity((1,3,6,1,4,1,476,1,42,1,11))
if mibBuilder.loadTexts:liebertFlexibleConditionsModuleReg.setStatus(_A)
_LiebertSrcModuleReg_ObjectIdentity=ObjectIdentity
liebertSrcModuleReg=_LiebertSrcModuleReg_ObjectIdentity((1,3,6,1,4,1,476,1,42,1,12))
if mibBuilder.loadTexts:liebertSrcModuleReg.setStatus(_A)
_LgpAgent_ObjectIdentity=ObjectIdentity
lgpAgent=_LgpAgent_ObjectIdentity((1,3,6,1,4,1,476,1,42,2))
if mibBuilder.loadTexts:lgpAgent.setStatus(_A)
_LgpAgentIdent_ObjectIdentity=ObjectIdentity
lgpAgentIdent=_LgpAgentIdent_ObjectIdentity((1,3,6,1,4,1,476,1,42,2,1))
if mibBuilder.loadTexts:lgpAgentIdent.setStatus(_A)
_LgpAgentNotifications_ObjectIdentity=ObjectIdentity
lgpAgentNotifications=_LgpAgentNotifications_ObjectIdentity((1,3,6,1,4,1,476,1,42,2,3))
if mibBuilder.loadTexts:lgpAgentNotifications.setStatus(_A)
_LgpAgentDevice_ObjectIdentity=ObjectIdentity
lgpAgentDevice=_LgpAgentDevice_ObjectIdentity((1,3,6,1,4,1,476,1,42,2,4))
if mibBuilder.loadTexts:lgpAgentDevice.setStatus(_A)
_LgpAgentControl_ObjectIdentity=ObjectIdentity
lgpAgentControl=_LgpAgentControl_ObjectIdentity((1,3,6,1,4,1,476,1,42,2,5))
if mibBuilder.loadTexts:lgpAgentControl.setStatus(_A)
_LgpFoundation_ObjectIdentity=ObjectIdentity
lgpFoundation=_LgpFoundation_ObjectIdentity((1,3,6,1,4,1,476,1,42,3))
if mibBuilder.loadTexts:lgpFoundation.setStatus(_A)
_LgpConditions_ObjectIdentity=ObjectIdentity
lgpConditions=_LgpConditions_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,2))
if mibBuilder.loadTexts:lgpConditions.setStatus(_A)
_LgpNotifications_ObjectIdentity=ObjectIdentity
lgpNotifications=_LgpNotifications_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,3))
if mibBuilder.loadTexts:lgpNotifications.setStatus(_A)
_LgpEnvironmental_ObjectIdentity=ObjectIdentity
lgpEnvironmental=_LgpEnvironmental_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4))
if mibBuilder.loadTexts:lgpEnvironmental.setStatus(_A)
_LgpPower_ObjectIdentity=ObjectIdentity
lgpPower=_LgpPower_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,5))
if mibBuilder.loadTexts:lgpPower.setStatus(_A)
_LgpController_ObjectIdentity=ObjectIdentity
lgpController=_LgpController_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,6))
if mibBuilder.loadTexts:lgpController.setStatus(_A)
_LgpSystem_ObjectIdentity=ObjectIdentity
lgpSystem=_LgpSystem_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,7))
if mibBuilder.loadTexts:lgpSystem.setStatus(_A)
_LgpPdu_ObjectIdentity=ObjectIdentity
lgpPdu=_LgpPdu_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,8))
if mibBuilder.loadTexts:lgpPdu.setStatus(_A)
_LgpFlexible_ObjectIdentity=ObjectIdentity
lgpFlexible=_LgpFlexible_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,9))
if mibBuilder.loadTexts:lgpFlexible.setStatus(_A)
_LgpSrc_ObjectIdentity=ObjectIdentity
lgpSrc=_LgpSrc_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,10))
if mibBuilder.loadTexts:lgpSrc.setStatus(_A)
_LgpProductSpecific_ObjectIdentity=ObjectIdentity
lgpProductSpecific=_LgpProductSpecific_ObjectIdentity((1,3,6,1,4,1,476,1,42,4))
if mibBuilder.loadTexts:lgpProductSpecific.setStatus(_A)
_LgpUpsProducts_ObjectIdentity=ObjectIdentity
lgpUpsProducts=_LgpUpsProducts_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2))
if mibBuilder.loadTexts:lgpUpsProducts.setStatus(_A)
_LgpSeries7200_ObjectIdentity=ObjectIdentity
lgpSeries7200=_LgpSeries7200_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,1))
if mibBuilder.loadTexts:lgpSeries7200.setStatus(_A)
_LgpUPStationGXT_ObjectIdentity=ObjectIdentity
lgpUPStationGXT=_LgpUPStationGXT_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,2))
if mibBuilder.loadTexts:lgpUPStationGXT.setStatus(_A)
_LgpPowerSureInteractive_ObjectIdentity=ObjectIdentity
lgpPowerSureInteractive=_LgpPowerSureInteractive_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,3))
if mibBuilder.loadTexts:lgpPowerSureInteractive.setStatus(_A)
_LgpNfinity_ObjectIdentity=ObjectIdentity
lgpNfinity=_LgpNfinity_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,4))
if mibBuilder.loadTexts:lgpNfinity.setStatus(_A)
_LgpNpower_ObjectIdentity=ObjectIdentity
lgpNpower=_LgpNpower_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,5))
if mibBuilder.loadTexts:lgpNpower.setStatus(_A)
_LgpGXT2Dual_ObjectIdentity=ObjectIdentity
lgpGXT2Dual=_LgpGXT2Dual_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,6))
if mibBuilder.loadTexts:lgpGXT2Dual.setStatus(_A)
_LgpPowerSureInteractive2_ObjectIdentity=ObjectIdentity
lgpPowerSureInteractive2=_LgpPowerSureInteractive2_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,7))
if mibBuilder.loadTexts:lgpPowerSureInteractive2.setStatus(_A)
_LgpNX_ObjectIdentity=ObjectIdentity
lgpNX=_LgpNX_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,8))
if mibBuilder.loadTexts:lgpNX.setStatus(_A)
_LgpHiNet_ObjectIdentity=ObjectIdentity
lgpHiNet=_LgpHiNet_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,9))
if mibBuilder.loadTexts:lgpHiNet.setStatus(_A)
_LgpNXL_ObjectIdentity=ObjectIdentity
lgpNXL=_LgpNXL_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,10))
if mibBuilder.loadTexts:lgpNXL.setStatus(_A)
_LgpNXLJD_ObjectIdentity=ObjectIdentity
lgpNXLJD=_LgpNXLJD_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,10,1))
if mibBuilder.loadTexts:lgpNXLJD.setStatus(_A)
_LgpSuper400_ObjectIdentity=ObjectIdentity
lgpSuper400=_LgpSuper400_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,11))
if mibBuilder.loadTexts:lgpSuper400.setStatus(_A)
_LgpSeries600or610_ObjectIdentity=ObjectIdentity
lgpSeries600or610=_LgpSeries600or610_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,12))
if mibBuilder.loadTexts:lgpSeries600or610.setStatus(_A)
_LgpSeries300_ObjectIdentity=ObjectIdentity
lgpSeries300=_LgpSeries300_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,13))
if mibBuilder.loadTexts:lgpSeries300.setStatus(_A)
_LgpSeries610SMS_ObjectIdentity=ObjectIdentity
lgpSeries610SMS=_LgpSeries610SMS_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,14))
if mibBuilder.loadTexts:lgpSeries610SMS.setStatus(_A)
_LgpSeries610MMU_ObjectIdentity=ObjectIdentity
lgpSeries610MMU=_LgpSeries610MMU_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,15))
if mibBuilder.loadTexts:lgpSeries610MMU.setStatus(_A)
_LgpSeries610SCC_ObjectIdentity=ObjectIdentity
lgpSeries610SCC=_LgpSeries610SCC_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,16))
if mibBuilder.loadTexts:lgpSeries610SCC.setStatus(_A)
_LgpGXT3_ObjectIdentity=ObjectIdentity
lgpGXT3=_LgpGXT3_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,17))
if mibBuilder.loadTexts:lgpGXT3.setStatus(_A)
_LgpGXT3Dual_ObjectIdentity=ObjectIdentity
lgpGXT3Dual=_LgpGXT3Dual_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,18))
if mibBuilder.loadTexts:lgpGXT3Dual.setStatus(_A)
_LgpNXr_ObjectIdentity=ObjectIdentity
lgpNXr=_LgpNXr_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,19))
if mibBuilder.loadTexts:lgpNXr.setStatus(_A)
_LgpITA_ObjectIdentity=ObjectIdentity
lgpITA=_LgpITA_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,19,1))
if mibBuilder.loadTexts:lgpITA.setStatus(_A)
_LgpNXRb_ObjectIdentity=ObjectIdentity
lgpNXRb=_LgpNXRb_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,19,2))
if mibBuilder.loadTexts:lgpNXRb.setStatus(_A)
_LgpNXC_ObjectIdentity=ObjectIdentity
lgpNXC=_LgpNXC_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,19,3))
if mibBuilder.loadTexts:lgpNXC.setStatus(_A)
_LgpNXC30to40k_ObjectIdentity=ObjectIdentity
lgpNXC30to40k=_LgpNXC30to40k_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,19,4))
if mibBuilder.loadTexts:lgpNXC30to40k.setStatus(_A)
_LgpITA30to40k_ObjectIdentity=ObjectIdentity
lgpITA30to40k=_LgpITA30to40k_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,19,5))
if mibBuilder.loadTexts:lgpITA30to40k.setStatus(_A)
_LgpAPS_ObjectIdentity=ObjectIdentity
lgpAPS=_LgpAPS_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,20))
if mibBuilder.loadTexts:lgpAPS.setStatus(_A)
_LgpMUNiMx_ObjectIdentity=ObjectIdentity
lgpMUNiMx=_LgpMUNiMx_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,22))
if mibBuilder.loadTexts:lgpMUNiMx.setStatus(_A)
_LgpNX225to600k_ObjectIdentity=ObjectIdentity
lgpNX225to600k=_LgpNX225to600k_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,22,1))
if mibBuilder.loadTexts:lgpNX225to600k.setStatus(_A)
_LgpGXT4_ObjectIdentity=ObjectIdentity
lgpGXT4=_LgpGXT4_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,23))
if mibBuilder.loadTexts:lgpGXT4.setStatus(_A)
_LgpGXT4Dual_ObjectIdentity=ObjectIdentity
lgpGXT4Dual=_LgpGXT4Dual_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,24))
if mibBuilder.loadTexts:lgpGXT4Dual.setStatus(_A)
_LgpEXL_ObjectIdentity=ObjectIdentity
lgpEXL=_LgpEXL_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,25))
if mibBuilder.loadTexts:lgpEXL.setStatus(_A)
_LgpEXM_ObjectIdentity=ObjectIdentity
lgpEXM=_LgpEXM_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,26))
if mibBuilder.loadTexts:lgpEXM.setStatus(_A)
_LgpEXM208v_ObjectIdentity=ObjectIdentity
lgpEXM208v=_LgpEXM208v_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,26,1))
if mibBuilder.loadTexts:lgpEXM208v.setStatus(_A)
_LgpEXM400v_ObjectIdentity=ObjectIdentity
lgpEXM400v=_LgpEXM400v_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,26,2))
if mibBuilder.loadTexts:lgpEXM400v.setStatus(_A)
_LgpEXM480v_ObjectIdentity=ObjectIdentity
lgpEXM480v=_LgpEXM480v_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,26,3))
if mibBuilder.loadTexts:lgpEXM480v.setStatus(_A)
_LgpEPM_ObjectIdentity=ObjectIdentity
lgpEPM=_LgpEPM_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,27))
if mibBuilder.loadTexts:lgpEPM.setStatus(_A)
_LgpEPM300k_ObjectIdentity=ObjectIdentity
lgpEPM300k=_LgpEPM300k_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,27,1))
if mibBuilder.loadTexts:lgpEPM300k.setStatus(_A)
_LgpEPM400k_ObjectIdentity=ObjectIdentity
lgpEPM400k=_LgpEPM400k_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,27,2))
if mibBuilder.loadTexts:lgpEPM400k.setStatus(_A)
_LgpEPM500k_ObjectIdentity=ObjectIdentity
lgpEPM500k=_LgpEPM500k_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,27,3))
if mibBuilder.loadTexts:lgpEPM500k.setStatus(_A)
_LgpEPM600k_ObjectIdentity=ObjectIdentity
lgpEPM600k=_LgpEPM600k_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,27,4))
if mibBuilder.loadTexts:lgpEPM600k.setStatus(_A)
_LgpEPM800k_ObjectIdentity=ObjectIdentity
lgpEPM800k=_LgpEPM800k_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,27,5))
if mibBuilder.loadTexts:lgpEPM800k.setStatus(_A)
_LgpAPM600_ObjectIdentity=ObjectIdentity
lgpAPM600=_LgpAPM600_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,27,9))
if mibBuilder.loadTexts:lgpAPM600.setStatus(_A)
_LgpEXLS1_ObjectIdentity=ObjectIdentity
lgpEXLS1=_LgpEXLS1_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,28))
if mibBuilder.loadTexts:lgpEXLS1.setStatus(_A)
_LgpEXLS1UPS_ObjectIdentity=ObjectIdentity
lgpEXLS1UPS=_LgpEXLS1UPS_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,28,1))
if mibBuilder.loadTexts:lgpEXLS1UPS.setStatus(_A)
_LgpEXMMSR_ObjectIdentity=ObjectIdentity
lgpEXMMSR=_LgpEXMMSR_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,29))
if mibBuilder.loadTexts:lgpEXMMSR.setStatus(_A)
_LgpAPM600GHMI_ObjectIdentity=ObjectIdentity
lgpAPM600GHMI=_LgpAPM600GHMI_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,29,2))
if mibBuilder.loadTexts:lgpAPM600GHMI.setStatus(_A)
_LgpEPMGHMI_ObjectIdentity=ObjectIdentity
lgpEPMGHMI=_LgpEPMGHMI_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,29,3))
if mibBuilder.loadTexts:lgpEPMGHMI.setStatus(_A)
_LgpITA2_ObjectIdentity=ObjectIdentity
lgpITA2=_LgpITA2_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,31))
if mibBuilder.loadTexts:lgpITA2.setStatus(_A)
_LgpITA2cap20k_ObjectIdentity=ObjectIdentity
lgpITA2cap20k=_LgpITA2cap20k_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,31,1))
if mibBuilder.loadTexts:lgpITA2cap20k.setStatus(_A)
_LgpITA2cap40k_ObjectIdentity=ObjectIdentity
lgpITA2cap40k=_LgpITA2cap40k_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,31,2))
if mibBuilder.loadTexts:lgpITA2cap40k.setStatus(_A)
_LgpEXSRackMountAndFrame1_ObjectIdentity=ObjectIdentity
lgpEXSRackMountAndFrame1=_LgpEXSRackMountAndFrame1_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,31,3))
if mibBuilder.loadTexts:lgpEXSRackMountAndFrame1.setStatus(_A)
_LgpGXE_ObjectIdentity=ObjectIdentity
lgpGXE=_LgpGXE_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,31,4))
if mibBuilder.loadTexts:lgpGXE.setStatus(_A)
_LgpITA2cap5k30k_ObjectIdentity=ObjectIdentity
lgpITA2cap5k30k=_LgpITA2cap5k30k_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,31,5))
if mibBuilder.loadTexts:lgpITA2cap5k30k.setStatus(_A)
_LgpEXS_ObjectIdentity=ObjectIdentity
lgpEXS=_LgpEXS_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,32))
if mibBuilder.loadTexts:lgpEXS.setStatus(_A)
_LgpEXSFr45_ObjectIdentity=ObjectIdentity
lgpEXSFr45=_LgpEXSFr45_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,32,2))
if mibBuilder.loadTexts:lgpEXSFr45.setStatus(_A)
_LgpPowerSureInteractive5_ObjectIdentity=ObjectIdentity
lgpPowerSureInteractive5=_LgpPowerSureInteractive5_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,33))
if mibBuilder.loadTexts:lgpPowerSureInteractive5.setStatus(_A)
_LgpGXT5_ObjectIdentity=ObjectIdentity
lgpGXT5=_LgpGXT5_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,34))
if mibBuilder.loadTexts:lgpGXT5.setStatus(_A)
_LgpAPME_ObjectIdentity=ObjectIdentity
lgpAPME=_LgpAPME_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,37))
if mibBuilder.loadTexts:lgpAPME.setStatus(_A)
_LgpEXM2_ObjectIdentity=ObjectIdentity
lgpEXM2=_LgpEXM2_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,38))
if mibBuilder.loadTexts:lgpEXM2.setStatus(_A)
_LgpAPMV2_ObjectIdentity=ObjectIdentity
lgpAPMV2=_LgpAPMV2_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,38,2))
if mibBuilder.loadTexts:lgpAPMV2.setStatus(_A)
_LgpTrinergyCube_ObjectIdentity=ObjectIdentity
lgpTrinergyCube=_LgpTrinergyCube_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,39))
if mibBuilder.loadTexts:lgpTrinergyCube.setStatus(_A)
_LgpEdgeUPS_ObjectIdentity=ObjectIdentity
lgpEdgeUPS=_LgpEdgeUPS_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,2,40))
if mibBuilder.loadTexts:lgpEdgeUPS.setStatus(_A)
_LgpAcProducts_ObjectIdentity=ObjectIdentity
lgpAcProducts=_LgpAcProducts_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3))
if mibBuilder.loadTexts:lgpAcProducts.setStatus(_A)
_LgpAdvancedMicroprocessor_ObjectIdentity=ObjectIdentity
lgpAdvancedMicroprocessor=_LgpAdvancedMicroprocessor_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,1))
if mibBuilder.loadTexts:lgpAdvancedMicroprocessor.setStatus(_A)
_LgpStandardMicroprocessor_ObjectIdentity=ObjectIdentity
lgpStandardMicroprocessor=_LgpStandardMicroprocessor_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,2))
if mibBuilder.loadTexts:lgpStandardMicroprocessor.setStatus(_A)
_LgpMiniMate2_ObjectIdentity=ObjectIdentity
lgpMiniMate2=_LgpMiniMate2_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,3))
if mibBuilder.loadTexts:lgpMiniMate2.setStatus(_A)
_LgpHimod_ObjectIdentity=ObjectIdentity
lgpHimod=_LgpHimod_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,4))
if mibBuilder.loadTexts:lgpHimod.setStatus(_A)
_LgpCEMS100orLECS15_ObjectIdentity=ObjectIdentity
lgpCEMS100orLECS15=_LgpCEMS100orLECS15_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,5))
if mibBuilder.loadTexts:lgpCEMS100orLECS15.setStatus(_A)
_LgpIcom_ObjectIdentity=ObjectIdentity
lgpIcom=_LgpIcom_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,6))
if mibBuilder.loadTexts:lgpIcom.setStatus(_A)
_LgpIcomPA_ObjectIdentity=ObjectIdentity
lgpIcomPA=_LgpIcomPA_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,7))
if mibBuilder.loadTexts:lgpIcomPA.setStatus(_A)
_LgpIcomPAtypeDS_ObjectIdentity=ObjectIdentity
lgpIcomPAtypeDS=_LgpIcomPAtypeDS_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,7,1))
if mibBuilder.loadTexts:lgpIcomPAtypeDS.setStatus(_A)
_LgpIcomPAtypeHPM_ObjectIdentity=ObjectIdentity
lgpIcomPAtypeHPM=_LgpIcomPAtypeHPM_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,7,2))
if mibBuilder.loadTexts:lgpIcomPAtypeHPM.setStatus(_A)
_LgpIcomPAtypeChallenger_ObjectIdentity=ObjectIdentity
lgpIcomPAtypeChallenger=_LgpIcomPAtypeChallenger_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,7,3))
if mibBuilder.loadTexts:lgpIcomPAtypeChallenger.setStatus(_A)
_LgpIcomPAtypePeX_ObjectIdentity=ObjectIdentity
lgpIcomPAtypePeX=_LgpIcomPAtypePeX_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,7,4))
if mibBuilder.loadTexts:lgpIcomPAtypePeX.setStatus(_A)
_LgpIcomPAtypeDeluxeSys3_ObjectIdentity=ObjectIdentity
lgpIcomPAtypeDeluxeSys3=_LgpIcomPAtypeDeluxeSys3_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,7,5))
if mibBuilder.loadTexts:lgpIcomPAtypeDeluxeSys3.setStatus(_A)
_LgpIcomPAtypeDeluxeSystem3_ObjectIdentity=ObjectIdentity
lgpIcomPAtypeDeluxeSystem3=_LgpIcomPAtypeDeluxeSystem3_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,7,5,1))
if mibBuilder.loadTexts:lgpIcomPAtypeDeluxeSystem3.setStatus(_A)
_LgpIcomPAtypeCW_ObjectIdentity=ObjectIdentity
lgpIcomPAtypeCW=_LgpIcomPAtypeCW_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,7,5,2))
if mibBuilder.loadTexts:lgpIcomPAtypeCW.setStatus(_A)
_LgpIcomPAtypeJumboCW_ObjectIdentity=ObjectIdentity
lgpIcomPAtypeJumboCW=_LgpIcomPAtypeJumboCW_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,7,6))
if mibBuilder.loadTexts:lgpIcomPAtypeJumboCW.setStatus(_A)
_LgpIcomPAtypeDSE_ObjectIdentity=ObjectIdentity
lgpIcomPAtypeDSE=_LgpIcomPAtypeDSE_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,7,7))
if mibBuilder.loadTexts:lgpIcomPAtypeDSE.setStatus(_A)
_LgpIcomPAtypeDSE400_ObjectIdentity=ObjectIdentity
lgpIcomPAtypeDSE400=_LgpIcomPAtypeDSE400_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,7,7,1))
if mibBuilder.loadTexts:lgpIcomPAtypeDSE400.setStatus(_A)
_LgpIcomPAtypeDP060_ObjectIdentity=ObjectIdentity
lgpIcomPAtypeDP060=_LgpIcomPAtypeDP060_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,7,7,2))
if mibBuilder.loadTexts:lgpIcomPAtypeDP060.setStatus(_A)
_LgpIcomPAtypePEXS_ObjectIdentity=ObjectIdentity
lgpIcomPAtypePEXS=_LgpIcomPAtypePEXS_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,7,8))
if mibBuilder.loadTexts:lgpIcomPAtypePEXS.setStatus(_A)
_LgpIcomPAtypePDXsmall_ObjectIdentity=ObjectIdentity
lgpIcomPAtypePDXsmall=_LgpIcomPAtypePDXsmall_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,7,8,1))
if mibBuilder.loadTexts:lgpIcomPAtypePDXsmall.setStatus(_A)
_LgpIcomPAtypePCWsmall_ObjectIdentity=ObjectIdentity
lgpIcomPAtypePCWsmall=_LgpIcomPAtypePCWsmall_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,7,8,2))
if mibBuilder.loadTexts:lgpIcomPAtypePCWsmall.setStatus(_A)
_LgpIcomPAtypePDX_ObjectIdentity=ObjectIdentity
lgpIcomPAtypePDX=_LgpIcomPAtypePDX_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,7,9))
if mibBuilder.loadTexts:lgpIcomPAtypePDX.setStatus(_A)
_LgpIcomPAtypePDXlarge_ObjectIdentity=ObjectIdentity
lgpIcomPAtypePDXlarge=_LgpIcomPAtypePDXlarge_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,7,9,1))
if mibBuilder.loadTexts:lgpIcomPAtypePDXlarge.setStatus(_A)
_LgpIcomPAtypePCWlarge_ObjectIdentity=ObjectIdentity
lgpIcomPAtypePCWlarge=_LgpIcomPAtypePCWlarge_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,7,9,2))
if mibBuilder.loadTexts:lgpIcomPAtypePCWlarge.setStatus(_A)
_LgpIcomPAtypeHPS_ObjectIdentity=ObjectIdentity
lgpIcomPAtypeHPS=_LgpIcomPAtypeHPS_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,7,10))
if mibBuilder.loadTexts:lgpIcomPAtypeHPS.setStatus(_A)
_LgpMiniMate3_ObjectIdentity=ObjectIdentity
lgpMiniMate3=_LgpMiniMate3_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,7,11))
if mibBuilder.loadTexts:lgpMiniMate3.setStatus(_A)
_LgpIcomPAtypeXDU_ObjectIdentity=ObjectIdentity
lgpIcomPAtypeXDU=_LgpIcomPAtypeXDU_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,7,12))
if mibBuilder.loadTexts:lgpIcomPAtypeXDU.setStatus(_A)
_LgpIcomPAtypeXDM_ObjectIdentity=ObjectIdentity
lgpIcomPAtypeXDM=_LgpIcomPAtypeXDM_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,7,13))
if mibBuilder.loadTexts:lgpIcomPAtypeXDM.setStatus(_A)
_LgpIcomPAtypeCWA_ObjectIdentity=ObjectIdentity
lgpIcomPAtypeCWA=_LgpIcomPAtypeCWA_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,7,14))
if mibBuilder.loadTexts:lgpIcomPAtypeCWA.setStatus(_A)
_LgpIcomXD_ObjectIdentity=ObjectIdentity
lgpIcomXD=_LgpIcomXD_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,8))
if mibBuilder.loadTexts:lgpIcomXD.setStatus(_A)
_LgpIcomXDtypeXDF_ObjectIdentity=ObjectIdentity
lgpIcomXDtypeXDF=_LgpIcomXDtypeXDF_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,8,1))
if mibBuilder.loadTexts:lgpIcomXDtypeXDF.setStatus(_A)
_LgpIcomXDtypeXDFN_ObjectIdentity=ObjectIdentity
lgpIcomXDtypeXDFN=_LgpIcomXDtypeXDFN_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,8,2))
if mibBuilder.loadTexts:lgpIcomXDtypeXDFN.setStatus(_A)
_LgpIcomXP_ObjectIdentity=ObjectIdentity
lgpIcomXP=_LgpIcomXP_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,9))
if mibBuilder.loadTexts:lgpIcomXP.setStatus(_A)
_LgpIcomXPtypeXDP_ObjectIdentity=ObjectIdentity
lgpIcomXPtypeXDP=_LgpIcomXPtypeXDP_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,9,1))
if mibBuilder.loadTexts:lgpIcomXPtypeXDP.setStatus(_A)
_LgpIcomXPtypeXDPCray_ObjectIdentity=ObjectIdentity
lgpIcomXPtypeXDPCray=_LgpIcomXPtypeXDPCray_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,9,1,1))
if mibBuilder.loadTexts:lgpIcomXPtypeXDPCray.setStatus(_A)
_LgpIcomXPtypeXDC_ObjectIdentity=ObjectIdentity
lgpIcomXPtypeXDC=_LgpIcomXPtypeXDC_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,9,2))
if mibBuilder.loadTexts:lgpIcomXPtypeXDC.setStatus(_A)
_LgpIcomXPtypeXDPW_ObjectIdentity=ObjectIdentity
lgpIcomXPtypeXDPW=_LgpIcomXPtypeXDPW_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,9,3))
if mibBuilder.loadTexts:lgpIcomXPtypeXDPW.setStatus(_A)
_LgpIcomSC_ObjectIdentity=ObjectIdentity
lgpIcomSC=_LgpIcomSC_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,10))
if mibBuilder.loadTexts:lgpIcomSC.setStatus(_A)
_LgpIcomSCtypeHPC_ObjectIdentity=ObjectIdentity
lgpIcomSCtypeHPC=_LgpIcomSCtypeHPC_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,10,1))
if mibBuilder.loadTexts:lgpIcomSCtypeHPC.setStatus(_A)
_LgpIcomSCtypeHPCSSmall_ObjectIdentity=ObjectIdentity
lgpIcomSCtypeHPCSSmall=_LgpIcomSCtypeHPCSSmall_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,10,1,1))
if mibBuilder.loadTexts:lgpIcomSCtypeHPCSSmall.setStatus(_A)
_LgpIcomSCtypeHPCSLarge_ObjectIdentity=ObjectIdentity
lgpIcomSCtypeHPCSLarge=_LgpIcomSCtypeHPCSLarge_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,10,1,2))
if mibBuilder.loadTexts:lgpIcomSCtypeHPCSLarge.setStatus(_A)
_LgpIcomSCtypeHPCR_ObjectIdentity=ObjectIdentity
lgpIcomSCtypeHPCR=_LgpIcomSCtypeHPCR_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,10,1,3))
if mibBuilder.loadTexts:lgpIcomSCtypeHPCR.setStatus(_A)
_LgpIcomSCtypeHPCM_ObjectIdentity=ObjectIdentity
lgpIcomSCtypeHPCM=_LgpIcomSCtypeHPCM_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,10,1,4))
if mibBuilder.loadTexts:lgpIcomSCtypeHPCM.setStatus(_A)
_LgpIcomSCtypeHPCL_ObjectIdentity=ObjectIdentity
lgpIcomSCtypeHPCL=_LgpIcomSCtypeHPCL_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,10,1,5))
if mibBuilder.loadTexts:lgpIcomSCtypeHPCL.setStatus(_A)
_LgpIcomSCtypeHPCW_ObjectIdentity=ObjectIdentity
lgpIcomSCtypeHPCW=_LgpIcomSCtypeHPCW_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,10,1,6))
if mibBuilder.loadTexts:lgpIcomSCtypeHPCW.setStatus(_A)
_LgpIcomCR_ObjectIdentity=ObjectIdentity
lgpIcomCR=_LgpIcomCR_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,11))
if mibBuilder.loadTexts:lgpIcomCR.setStatus(_A)
_LgpIcomCRtypeCRV_ObjectIdentity=ObjectIdentity
lgpIcomCRtypeCRV=_LgpIcomCRtypeCRV_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,11,1))
if mibBuilder.loadTexts:lgpIcomCRtypeCRV.setStatus(_A)
_LgpIcomAH_ObjectIdentity=ObjectIdentity
lgpIcomAH=_LgpIcomAH_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,12))
if mibBuilder.loadTexts:lgpIcomAH.setStatus(_A)
_LgpIcomAHStandard_ObjectIdentity=ObjectIdentity
lgpIcomAHStandard=_LgpIcomAHStandard_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,12,1))
if mibBuilder.loadTexts:lgpIcomAHStandard.setStatus(_A)
_LgpIcomDCL_ObjectIdentity=ObjectIdentity
lgpIcomDCL=_LgpIcomDCL_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,13))
if mibBuilder.loadTexts:lgpIcomDCL.setStatus(_A)
_LgpIcomEEV_ObjectIdentity=ObjectIdentity
lgpIcomEEV=_LgpIcomEEV_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,14))
if mibBuilder.loadTexts:lgpIcomEEV.setStatus(_A)
_LgpIproAFC_ObjectIdentity=ObjectIdentity
lgpIproAFC=_LgpIproAFC_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,30))
if mibBuilder.loadTexts:lgpIproAFC.setStatus(_A)
_LgpIproEFC_ObjectIdentity=ObjectIdentity
lgpIproEFC=_LgpIproEFC_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,31))
if mibBuilder.loadTexts:lgpIproEFC.setStatus(_A)
_LgpCpcoPDX_ObjectIdentity=ObjectIdentity
lgpCpcoPDX=_LgpCpcoPDX_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,3,32))
if mibBuilder.loadTexts:lgpCpcoPDX.setStatus(_A)
_LgpPowerConditioningProducts_ObjectIdentity=ObjectIdentity
lgpPowerConditioningProducts=_LgpPowerConditioningProducts_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,4))
if mibBuilder.loadTexts:lgpPowerConditioningProducts.setStatus(_A)
_LgpPMP_ObjectIdentity=ObjectIdentity
lgpPMP=_LgpPMP_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,4,1))
if mibBuilder.loadTexts:lgpPMP.setStatus(_A)
_LgpEPMP_ObjectIdentity=ObjectIdentity
lgpEPMP=_LgpEPMP_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,4,2))
if mibBuilder.loadTexts:lgpEPMP.setStatus(_A)
_LgpTransferSwitchProducts_ObjectIdentity=ObjectIdentity
lgpTransferSwitchProducts=_LgpTransferSwitchProducts_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,5))
if mibBuilder.loadTexts:lgpTransferSwitchProducts.setStatus(_A)
_LgpStaticTransferSwitchEDS_ObjectIdentity=ObjectIdentity
lgpStaticTransferSwitchEDS=_LgpStaticTransferSwitchEDS_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,5,1))
if mibBuilder.loadTexts:lgpStaticTransferSwitchEDS.setStatus(_A)
_LgpStaticTransferSwitch1_ObjectIdentity=ObjectIdentity
lgpStaticTransferSwitch1=_LgpStaticTransferSwitch1_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,5,2))
if mibBuilder.loadTexts:lgpStaticTransferSwitch1.setStatus(_A)
_LgpStaticTransferSwitch2_ObjectIdentity=ObjectIdentity
lgpStaticTransferSwitch2=_LgpStaticTransferSwitch2_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,5,3))
if mibBuilder.loadTexts:lgpStaticTransferSwitch2.setStatus(_A)
_LgpStaticTransferSwitch2FourPole_ObjectIdentity=ObjectIdentity
lgpStaticTransferSwitch2FourPole=_LgpStaticTransferSwitch2FourPole_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,5,4))
if mibBuilder.loadTexts:lgpStaticTransferSwitch2FourPole.setStatus(_A)
_LgpMultiLinkProducts_ObjectIdentity=ObjectIdentity
lgpMultiLinkProducts=_LgpMultiLinkProducts_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,7))
if mibBuilder.loadTexts:lgpMultiLinkProducts.setStatus(_A)
_LgpMultiLinkBasicNotification_ObjectIdentity=ObjectIdentity
lgpMultiLinkBasicNotification=_LgpMultiLinkBasicNotification_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,7,1))
if mibBuilder.loadTexts:lgpMultiLinkBasicNotification.setStatus(_A)
_LgpPowerDistributionProducts_ObjectIdentity=ObjectIdentity
lgpPowerDistributionProducts=_LgpPowerDistributionProducts_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,8))
if mibBuilder.loadTexts:lgpPowerDistributionProducts.setStatus(_A)
_LgpRackPDU_ObjectIdentity=ObjectIdentity
lgpRackPDU=_LgpRackPDU_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,8,2))
if mibBuilder.loadTexts:lgpRackPDU.setStatus(_A)
_LgpMPX_ObjectIdentity=ObjectIdentity
lgpMPX=_LgpMPX_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,8,2,1))
if mibBuilder.loadTexts:lgpMPX.setStatus(_A)
_LgpMPH_ObjectIdentity=ObjectIdentity
lgpMPH=_LgpMPH_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,8,2,2))
if mibBuilder.loadTexts:lgpMPH.setStatus(_A)
_LgpRackPDU2_ObjectIdentity=ObjectIdentity
lgpRackPDU2=_LgpRackPDU2_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,8,4))
if mibBuilder.loadTexts:lgpRackPDU2.setStatus(_A)
_LgpRPC2kMPX_ObjectIdentity=ObjectIdentity
lgpRPC2kMPX=_LgpRPC2kMPX_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,8,4,1))
if mibBuilder.loadTexts:lgpRPC2kMPX.setStatus(_A)
_LgpRPC2kMPH_ObjectIdentity=ObjectIdentity
lgpRPC2kMPH=_LgpRPC2kMPH_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,8,4,2))
if mibBuilder.loadTexts:lgpRPC2kMPH.setStatus(_A)
_LgpCombinedSystemProducts_ObjectIdentity=ObjectIdentity
lgpCombinedSystemProducts=_LgpCombinedSystemProducts_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,10))
if mibBuilder.loadTexts:lgpCombinedSystemProducts.setStatus(_A)
_LgpPMPandLDMF_ObjectIdentity=ObjectIdentity
lgpPMPandLDMF=_LgpPMPandLDMF_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,10,1))
if mibBuilder.loadTexts:lgpPMPandLDMF.setStatus(_A)
_LgpPMPgeneric_ObjectIdentity=ObjectIdentity
lgpPMPgeneric=_LgpPMPgeneric_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,10,1,1))
if mibBuilder.loadTexts:lgpPMPgeneric.setStatus(_A)
_LgpPMPonFPC_ObjectIdentity=ObjectIdentity
lgpPMPonFPC=_LgpPMPonFPC_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,10,1,2))
if mibBuilder.loadTexts:lgpPMPonFPC.setStatus(_A)
_LgpPMPonPPC_ObjectIdentity=ObjectIdentity
lgpPMPonPPC=_LgpPMPonPPC_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,10,1,3))
if mibBuilder.loadTexts:lgpPMPonPPC.setStatus(_A)
_LgpPMPonFDC_ObjectIdentity=ObjectIdentity
lgpPMPonFDC=_LgpPMPonFDC_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,10,1,4))
if mibBuilder.loadTexts:lgpPMPonFDC.setStatus(_A)
_LgpPMPonRDC_ObjectIdentity=ObjectIdentity
lgpPMPonRDC=_LgpPMPonRDC_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,10,1,5))
if mibBuilder.loadTexts:lgpPMPonRDC.setStatus(_A)
_LgpPMPonEXC_ObjectIdentity=ObjectIdentity
lgpPMPonEXC=_LgpPMPonEXC_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,10,1,6))
if mibBuilder.loadTexts:lgpPMPonEXC.setStatus(_A)
_LgpPMPonSTS2_ObjectIdentity=ObjectIdentity
lgpPMPonSTS2=_LgpPMPonSTS2_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,10,1,7))
if mibBuilder.loadTexts:lgpPMPonSTS2.setStatus(_A)
_LgpPMPonSTS2PDU_ObjectIdentity=ObjectIdentity
lgpPMPonSTS2PDU=_LgpPMPonSTS2PDU_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,10,1,8))
if mibBuilder.loadTexts:lgpPMPonSTS2PDU.setStatus(_A)
_LgpPM5_ObjectIdentity=ObjectIdentity
lgpPM5=_LgpPM5_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,10,3))
if mibBuilder.loadTexts:lgpPM5.setStatus(_A)
_LgpAcPACCProducts_ObjectIdentity=ObjectIdentity
lgpAcPACCProducts=_LgpAcPACCProducts_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,12))
if mibBuilder.loadTexts:lgpAcPACCProducts.setStatus(_A)
_LgpCRD_ObjectIdentity=ObjectIdentity
lgpCRD=_LgpCRD_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,12,1))
if mibBuilder.loadTexts:lgpCRD.setStatus(_A)
_LgpCRD010_ObjectIdentity=ObjectIdentity
lgpCRD010=_LgpCRD010_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,12,1,1))
if mibBuilder.loadTexts:lgpCRD010.setStatus(_A)
_LgpCR_ObjectIdentity=ObjectIdentity
lgpCR=_LgpCR_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,12,2))
if mibBuilder.loadTexts:lgpCR.setStatus(_A)
_LgpCR012_ObjectIdentity=ObjectIdentity
lgpCR012=_LgpCR012_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,12,2,1))
if mibBuilder.loadTexts:lgpCR012.setStatus(_A)
_LgpCR025_ObjectIdentity=ObjectIdentity
lgpCR025=_LgpCR025_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,12,2,2))
if mibBuilder.loadTexts:lgpCR025.setStatus(_A)
_LgpCR030_ObjectIdentity=ObjectIdentity
lgpCR030=_LgpCR030_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,12,2,3))
if mibBuilder.loadTexts:lgpCR030.setStatus(_A)
_LgpPEX4_ObjectIdentity=ObjectIdentity
lgpPEX4=_LgpPEX4_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,12,2,4))
if mibBuilder.loadTexts:lgpPEX4.setStatus(_A)
_LgpCRC300600_ObjectIdentity=ObjectIdentity
lgpCRC300600=_LgpCRC300600_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,12,2,5))
if mibBuilder.loadTexts:lgpCRC300600.setStatus(_A)
_LgpCRV4_ObjectIdentity=ObjectIdentity
lgpCRV4=_LgpCRV4_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,12,2,6))
if mibBuilder.loadTexts:lgpCRV4.setStatus(_A)
_LgpDME2_ObjectIdentity=ObjectIdentity
lgpDME2=_LgpDME2_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,12,2,7))
if mibBuilder.loadTexts:lgpDME2.setStatus(_A)
_LgpCAHU_ObjectIdentity=ObjectIdentity
lgpCAHU=_LgpCAHU_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,12,2,8))
if mibBuilder.loadTexts:lgpCAHU.setStatus(_A)
_LgpPEX4WCFC_ObjectIdentity=ObjectIdentity
lgpPEX4WCFC=_LgpPEX4WCFC_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,12,2,9))
if mibBuilder.loadTexts:lgpPEX4WCFC.setStatus(_A)
_LgpCRVDX2535_ObjectIdentity=ObjectIdentity
lgpCRVDX2535=_LgpCRVDX2535_ObjectIdentity((1,3,6,1,4,1,476,1,42,4,12,2,10))
if mibBuilder.loadTexts:lgpCRVDX2535.setStatus(_A)
mibBuilder.exportSymbols('LIEBERT-GP-REGISTRATION-MIB',**{'vertiv':vertiv,'liebertCorp':liebertCorp,'liebertGlobalProducts':liebertGlobalProducts,'lgpModuleReg':lgpModuleReg,'liebertModuleReg':liebertModuleReg,'liebertGlobalProductsRegistrationModule':liebertGlobalProductsRegistrationModule,'liebertAgentModuleReg':liebertAgentModuleReg,'liebertConditionsModuleReg':liebertConditionsModuleReg,'liebertNotificationsModuleReg':liebertNotificationsModuleReg,'liebertEnvironmentalModuleReg':liebertEnvironmentalModuleReg,'liebertPowerModuleReg':liebertPowerModuleReg,'liebertControllerModuleReg':liebertControllerModuleReg,'liebertSystemModuleReg':liebertSystemModuleReg,'liebertPduModuleReg':liebertPduModuleReg,'liebertFlexibleModuleReg':liebertFlexibleModuleReg,'liebertFlexibleConditionsModuleReg':liebertFlexibleConditionsModuleReg,'liebertSrcModuleReg':liebertSrcModuleReg,'lgpAgent':lgpAgent,'lgpAgentIdent':lgpAgentIdent,'lgpAgentNotifications':lgpAgentNotifications,'lgpAgentDevice':lgpAgentDevice,'lgpAgentControl':lgpAgentControl,'lgpFoundation':lgpFoundation,'lgpConditions':lgpConditions,'lgpNotifications':lgpNotifications,'lgpEnvironmental':lgpEnvironmental,'lgpPower':lgpPower,'lgpController':lgpController,'lgpSystem':lgpSystem,'lgpPdu':lgpPdu,'lgpFlexible':lgpFlexible,'lgpSrc':lgpSrc,'lgpProductSpecific':lgpProductSpecific,'lgpUpsProducts':lgpUpsProducts,'lgpSeries7200':lgpSeries7200,'lgpUPStationGXT':lgpUPStationGXT,'lgpPowerSureInteractive':lgpPowerSureInteractive,'lgpNfinity':lgpNfinity,'lgpNpower':lgpNpower,'lgpGXT2Dual':lgpGXT2Dual,'lgpPowerSureInteractive2':lgpPowerSureInteractive2,'lgpNX':lgpNX,'lgpHiNet':lgpHiNet,'lgpNXL':lgpNXL,'lgpNXLJD':lgpNXLJD,'lgpSuper400':lgpSuper400,'lgpSeries600or610':lgpSeries600or610,'lgpSeries300':lgpSeries300,'lgpSeries610SMS':lgpSeries610SMS,'lgpSeries610MMU':lgpSeries610MMU,'lgpSeries610SCC':lgpSeries610SCC,'lgpGXT3':lgpGXT3,'lgpGXT3Dual':lgpGXT3Dual,'lgpNXr':lgpNXr,'lgpITA':lgpITA,'lgpNXRb':lgpNXRb,'lgpNXC':lgpNXC,'lgpNXC30to40k':lgpNXC30to40k,'lgpITA30to40k':lgpITA30to40k,'lgpAPS':lgpAPS,'lgpMUNiMx':lgpMUNiMx,'lgpNX225to600k':lgpNX225to600k,'lgpGXT4':lgpGXT4,'lgpGXT4Dual':lgpGXT4Dual,'lgpEXL':lgpEXL,'lgpEXM':lgpEXM,'lgpEXM208v':lgpEXM208v,'lgpEXM400v':lgpEXM400v,'lgpEXM480v':lgpEXM480v,'lgpEPM':lgpEPM,'lgpEPM300k':lgpEPM300k,'lgpEPM400k':lgpEPM400k,'lgpEPM500k':lgpEPM500k,'lgpEPM600k':lgpEPM600k,'lgpEPM800k':lgpEPM800k,'lgpAPM600':lgpAPM600,'lgpEXLS1':lgpEXLS1,'lgpEXLS1UPS':lgpEXLS1UPS,'lgpEXMMSR':lgpEXMMSR,'lgpAPM600GHMI':lgpAPM600GHMI,'lgpEPMGHMI':lgpEPMGHMI,'lgpITA2':lgpITA2,'lgpITA2cap20k':lgpITA2cap20k,'lgpITA2cap40k':lgpITA2cap40k,'lgpEXSRackMountAndFrame1':lgpEXSRackMountAndFrame1,'lgpGXE':lgpGXE,'lgpITA2cap5k30k':lgpITA2cap5k30k,'lgpEXS':lgpEXS,'lgpEXSFr45':lgpEXSFr45,'lgpPowerSureInteractive5':lgpPowerSureInteractive5,'lgpGXT5':lgpGXT5,'lgpAPME':lgpAPME,'lgpEXM2':lgpEXM2,'lgpAPMV2':lgpAPMV2,'lgpTrinergyCube':lgpTrinergyCube,'lgpEdgeUPS':lgpEdgeUPS,'lgpAcProducts':lgpAcProducts,'lgpAdvancedMicroprocessor':lgpAdvancedMicroprocessor,'lgpStandardMicroprocessor':lgpStandardMicroprocessor,'lgpMiniMate2':lgpMiniMate2,'lgpHimod':lgpHimod,'lgpCEMS100orLECS15':lgpCEMS100orLECS15,'lgpIcom':lgpIcom,'lgpIcomPA':lgpIcomPA,'lgpIcomPAtypeDS':lgpIcomPAtypeDS,'lgpIcomPAtypeHPM':lgpIcomPAtypeHPM,'lgpIcomPAtypeChallenger':lgpIcomPAtypeChallenger,'lgpIcomPAtypePeX':lgpIcomPAtypePeX,'lgpIcomPAtypeDeluxeSys3':lgpIcomPAtypeDeluxeSys3,'lgpIcomPAtypeDeluxeSystem3':lgpIcomPAtypeDeluxeSystem3,'lgpIcomPAtypeCW':lgpIcomPAtypeCW,'lgpIcomPAtypeJumboCW':lgpIcomPAtypeJumboCW,'lgpIcomPAtypeDSE':lgpIcomPAtypeDSE,'lgpIcomPAtypeDSE400':lgpIcomPAtypeDSE400,'lgpIcomPAtypeDP060':lgpIcomPAtypeDP060,'lgpIcomPAtypePEXS':lgpIcomPAtypePEXS,'lgpIcomPAtypePDXsmall':lgpIcomPAtypePDXsmall,'lgpIcomPAtypePCWsmall':lgpIcomPAtypePCWsmall,'lgpIcomPAtypePDX':lgpIcomPAtypePDX,'lgpIcomPAtypePDXlarge':lgpIcomPAtypePDXlarge,'lgpIcomPAtypePCWlarge':lgpIcomPAtypePCWlarge,'lgpIcomPAtypeHPS':lgpIcomPAtypeHPS,'lgpMiniMate3':lgpMiniMate3,'lgpIcomPAtypeXDU':lgpIcomPAtypeXDU,'lgpIcomPAtypeXDM':lgpIcomPAtypeXDM,'lgpIcomPAtypeCWA':lgpIcomPAtypeCWA,'lgpIcomXD':lgpIcomXD,'lgpIcomXDtypeXDF':lgpIcomXDtypeXDF,'lgpIcomXDtypeXDFN':lgpIcomXDtypeXDFN,'lgpIcomXP':lgpIcomXP,'lgpIcomXPtypeXDP':lgpIcomXPtypeXDP,'lgpIcomXPtypeXDPCray':lgpIcomXPtypeXDPCray,'lgpIcomXPtypeXDC':lgpIcomXPtypeXDC,'lgpIcomXPtypeXDPW':lgpIcomXPtypeXDPW,'lgpIcomSC':lgpIcomSC,'lgpIcomSCtypeHPC':lgpIcomSCtypeHPC,'lgpIcomSCtypeHPCSSmall':lgpIcomSCtypeHPCSSmall,'lgpIcomSCtypeHPCSLarge':lgpIcomSCtypeHPCSLarge,'lgpIcomSCtypeHPCR':lgpIcomSCtypeHPCR,'lgpIcomSCtypeHPCM':lgpIcomSCtypeHPCM,'lgpIcomSCtypeHPCL':lgpIcomSCtypeHPCL,'lgpIcomSCtypeHPCW':lgpIcomSCtypeHPCW,'lgpIcomCR':lgpIcomCR,'lgpIcomCRtypeCRV':lgpIcomCRtypeCRV,'lgpIcomAH':lgpIcomAH,'lgpIcomAHStandard':lgpIcomAHStandard,'lgpIcomDCL':lgpIcomDCL,'lgpIcomEEV':lgpIcomEEV,'lgpIproAFC':lgpIproAFC,'lgpIproEFC':lgpIproEFC,'lgpCpcoPDX':lgpCpcoPDX,'lgpPowerConditioningProducts':lgpPowerConditioningProducts,'lgpPMP':lgpPMP,'lgpEPMP':lgpEPMP,'lgpTransferSwitchProducts':lgpTransferSwitchProducts,'lgpStaticTransferSwitchEDS':lgpStaticTransferSwitchEDS,'lgpStaticTransferSwitch1':lgpStaticTransferSwitch1,'lgpStaticTransferSwitch2':lgpStaticTransferSwitch2,'lgpStaticTransferSwitch2FourPole':lgpStaticTransferSwitch2FourPole,'lgpMultiLinkProducts':lgpMultiLinkProducts,'lgpMultiLinkBasicNotification':lgpMultiLinkBasicNotification,'lgpPowerDistributionProducts':lgpPowerDistributionProducts,'lgpRackPDU':lgpRackPDU,'lgpMPX':lgpMPX,'lgpMPH':lgpMPH,'lgpRackPDU2':lgpRackPDU2,'lgpRPC2kMPX':lgpRPC2kMPX,'lgpRPC2kMPH':lgpRPC2kMPH,'lgpCombinedSystemProducts':lgpCombinedSystemProducts,'lgpPMPandLDMF':lgpPMPandLDMF,'lgpPMPgeneric':lgpPMPgeneric,'lgpPMPonFPC':lgpPMPonFPC,'lgpPMPonPPC':lgpPMPonPPC,'lgpPMPonFDC':lgpPMPonFDC,'lgpPMPonRDC':lgpPMPonRDC,'lgpPMPonEXC':lgpPMPonEXC,'lgpPMPonSTS2':lgpPMPonSTS2,'lgpPMPonSTS2PDU':lgpPMPonSTS2PDU,'lgpPM5':lgpPM5,'lgpAcPACCProducts':lgpAcPACCProducts,'lgpCRD':lgpCRD,'lgpCRD010':lgpCRD010,'lgpCR':lgpCR,'lgpCR012':lgpCR012,'lgpCR025':lgpCR025,'lgpCR030':lgpCR030,'lgpPEX4':lgpPEX4,'lgpCRC300600':lgpCRC300600,'lgpCRV4':lgpCRV4,'lgpDME2':lgpDME2,'lgpCAHU':lgpCAHU,'lgpPEX4WCFC':lgpPEX4WCFC,'lgpCRVDX2535':lgpCRVDX2535})