_G='astChanTypeIndex'
_F='astChanIndex'
_E='astIndIndex'
_D='ASTERISK-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
digium,=mibBuilder.importSymbols('DIGIUM-MIB','digium')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
asterisk=ModuleIdentity((1,3,6,1,4,1,22736,1))
if mibBuilder.loadTexts:asterisk.setRevisions(('2008-06-20 20:25','2007-08-21 14:50','2006-03-06 18:40','2006-02-04 19:00'))
_AsteriskVersion_ObjectIdentity=ObjectIdentity
asteriskVersion=_AsteriskVersion_ObjectIdentity((1,3,6,1,4,1,22736,1,1))
_AstVersionString_Type=DisplayString
_AstVersionString_Object=MibScalar
astVersionString=_AstVersionString_Object((1,3,6,1,4,1,22736,1,1,1),_AstVersionString_Type())
astVersionString.setMaxAccess(_B)
if mibBuilder.loadTexts:astVersionString.setStatus(_A)
_AstVersionTag_Type=Unsigned32
_AstVersionTag_Object=MibScalar
astVersionTag=_AstVersionTag_Object((1,3,6,1,4,1,22736,1,1,2),_AstVersionTag_Type())
astVersionTag.setMaxAccess(_B)
if mibBuilder.loadTexts:astVersionTag.setStatus(_A)
_AsteriskConfiguration_ObjectIdentity=ObjectIdentity
asteriskConfiguration=_AsteriskConfiguration_ObjectIdentity((1,3,6,1,4,1,22736,1,2))
_AstConfigUpTime_Type=TimeTicks
_AstConfigUpTime_Object=MibScalar
astConfigUpTime=_AstConfigUpTime_Object((1,3,6,1,4,1,22736,1,2,1),_AstConfigUpTime_Type())
astConfigUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:astConfigUpTime.setStatus(_A)
_AstConfigReloadTime_Type=TimeTicks
_AstConfigReloadTime_Object=MibScalar
astConfigReloadTime=_AstConfigReloadTime_Object((1,3,6,1,4,1,22736,1,2,2),_AstConfigReloadTime_Type())
astConfigReloadTime.setMaxAccess(_B)
if mibBuilder.loadTexts:astConfigReloadTime.setStatus(_A)
_AstConfigPid_Type=Integer32
_AstConfigPid_Object=MibScalar
astConfigPid=_AstConfigPid_Object((1,3,6,1,4,1,22736,1,2,3),_AstConfigPid_Type())
astConfigPid.setMaxAccess(_B)
if mibBuilder.loadTexts:astConfigPid.setStatus(_A)
_AstConfigSocket_Type=DisplayString
_AstConfigSocket_Object=MibScalar
astConfigSocket=_AstConfigSocket_Object((1,3,6,1,4,1,22736,1,2,4),_AstConfigSocket_Type())
astConfigSocket.setMaxAccess(_B)
if mibBuilder.loadTexts:astConfigSocket.setStatus(_A)
_AstConfigCallsActive_Type=Gauge32
_AstConfigCallsActive_Object=MibScalar
astConfigCallsActive=_AstConfigCallsActive_Object((1,3,6,1,4,1,22736,1,2,5),_AstConfigCallsActive_Type())
astConfigCallsActive.setMaxAccess(_B)
if mibBuilder.loadTexts:astConfigCallsActive.setStatus(_A)
_AstConfigCallsProcessed_Type=Counter32
_AstConfigCallsProcessed_Object=MibScalar
astConfigCallsProcessed=_AstConfigCallsProcessed_Object((1,3,6,1,4,1,22736,1,2,6),_AstConfigCallsProcessed_Type())
astConfigCallsProcessed.setMaxAccess(_B)
if mibBuilder.loadTexts:astConfigCallsProcessed.setStatus(_A)
_AsteriskModules_ObjectIdentity=ObjectIdentity
asteriskModules=_AsteriskModules_ObjectIdentity((1,3,6,1,4,1,22736,1,3))
_AstNumModules_Type=Integer32
_AstNumModules_Object=MibScalar
astNumModules=_AstNumModules_Object((1,3,6,1,4,1,22736,1,3,1),_AstNumModules_Type())
astNumModules.setMaxAccess(_B)
if mibBuilder.loadTexts:astNumModules.setStatus(_A)
_AsteriskIndications_ObjectIdentity=ObjectIdentity
asteriskIndications=_AsteriskIndications_ObjectIdentity((1,3,6,1,4,1,22736,1,4))
_AstNumIndications_Type=Integer32
_AstNumIndications_Object=MibScalar
astNumIndications=_AstNumIndications_Object((1,3,6,1,4,1,22736,1,4,1),_AstNumIndications_Type())
astNumIndications.setMaxAccess(_B)
if mibBuilder.loadTexts:astNumIndications.setStatus(_A)
_AstCurrentIndication_Type=DisplayString
_AstCurrentIndication_Object=MibScalar
astCurrentIndication=_AstCurrentIndication_Object((1,3,6,1,4,1,22736,1,4,2),_AstCurrentIndication_Type())
astCurrentIndication.setMaxAccess(_B)
if mibBuilder.loadTexts:astCurrentIndication.setStatus(_A)
_AstIndicationsTable_Object=MibTable
astIndicationsTable=_AstIndicationsTable_Object((1,3,6,1,4,1,22736,1,4,3))
if mibBuilder.loadTexts:astIndicationsTable.setStatus(_A)
_AstIndicationsEntry_Object=MibTableRow
astIndicationsEntry=_AstIndicationsEntry_Object((1,3,6,1,4,1,22736,1,4,3,1))
astIndicationsEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:astIndicationsEntry.setStatus(_A)
class _AstIndIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AstIndIndex_Type.__name__=_C
_AstIndIndex_Object=MibTableColumn
astIndIndex=_AstIndIndex_Object((1,3,6,1,4,1,22736,1,4,3,1,1),_AstIndIndex_Type())
astIndIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:astIndIndex.setStatus(_A)
_AstIndCountry_Type=DisplayString
_AstIndCountry_Object=MibTableColumn
astIndCountry=_AstIndCountry_Object((1,3,6,1,4,1,22736,1,4,3,1,2),_AstIndCountry_Type())
astIndCountry.setMaxAccess(_B)
if mibBuilder.loadTexts:astIndCountry.setStatus(_A)
_AstIndAlias_Type=DisplayString
_AstIndAlias_Object=MibTableColumn
astIndAlias=_AstIndAlias_Object((1,3,6,1,4,1,22736,1,4,3,1,3),_AstIndAlias_Type())
astIndAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:astIndAlias.setStatus(_A)
_AstIndDescription_Type=DisplayString
_AstIndDescription_Object=MibTableColumn
astIndDescription=_AstIndDescription_Object((1,3,6,1,4,1,22736,1,4,3,1,4),_AstIndDescription_Type())
astIndDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:astIndDescription.setStatus(_A)
_AsteriskChannels_ObjectIdentity=ObjectIdentity
asteriskChannels=_AsteriskChannels_ObjectIdentity((1,3,6,1,4,1,22736,1,5))
_AstNumChannels_Type=Gauge32
_AstNumChannels_Object=MibScalar
astNumChannels=_AstNumChannels_Object((1,3,6,1,4,1,22736,1,5,1),_AstNumChannels_Type())
astNumChannels.setMaxAccess(_B)
if mibBuilder.loadTexts:astNumChannels.setStatus(_A)
_AstChanTable_Object=MibTable
astChanTable=_AstChanTable_Object((1,3,6,1,4,1,22736,1,5,2))
if mibBuilder.loadTexts:astChanTable.setStatus(_A)
_AstChanEntry_Object=MibTableRow
astChanEntry=_AstChanEntry_Object((1,3,6,1,4,1,22736,1,5,2,1))
astChanEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:astChanEntry.setStatus(_A)
class _AstChanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AstChanIndex_Type.__name__=_C
_AstChanIndex_Object=MibTableColumn
astChanIndex=_AstChanIndex_Object((1,3,6,1,4,1,22736,1,5,2,1,1),_AstChanIndex_Type())
astChanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanIndex.setStatus(_A)
_AstChanName_Type=DisplayString
_AstChanName_Object=MibTableColumn
astChanName=_AstChanName_Object((1,3,6,1,4,1,22736,1,5,2,1,2),_AstChanName_Type())
astChanName.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanName.setStatus(_A)
_AstChanLanguage_Type=DisplayString
_AstChanLanguage_Object=MibTableColumn
astChanLanguage=_AstChanLanguage_Object((1,3,6,1,4,1,22736,1,5,2,1,3),_AstChanLanguage_Type())
astChanLanguage.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanLanguage.setStatus(_A)
_AstChanType_Type=DisplayString
_AstChanType_Object=MibTableColumn
astChanType=_AstChanType_Object((1,3,6,1,4,1,22736,1,5,2,1,4),_AstChanType_Type())
astChanType.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanType.setStatus(_A)
_AstChanMusicClass_Type=DisplayString
_AstChanMusicClass_Object=MibTableColumn
astChanMusicClass=_AstChanMusicClass_Object((1,3,6,1,4,1,22736,1,5,2,1,5),_AstChanMusicClass_Type())
astChanMusicClass.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanMusicClass.setStatus(_A)
_AstChanBridge_Type=DisplayString
_AstChanBridge_Object=MibTableColumn
astChanBridge=_AstChanBridge_Object((1,3,6,1,4,1,22736,1,5,2,1,6),_AstChanBridge_Type())
astChanBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanBridge.setStatus(_A)
_AstChanMasq_Type=DisplayString
_AstChanMasq_Object=MibTableColumn
astChanMasq=_AstChanMasq_Object((1,3,6,1,4,1,22736,1,5,2,1,7),_AstChanMasq_Type())
astChanMasq.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanMasq.setStatus(_A)
_AstChanMasqr_Type=DisplayString
_AstChanMasqr_Object=MibTableColumn
astChanMasqr=_AstChanMasqr_Object((1,3,6,1,4,1,22736,1,5,2,1,8),_AstChanMasqr_Type())
astChanMasqr.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanMasqr.setStatus(_A)
_AstChanWhenHangup_Type=TimeTicks
_AstChanWhenHangup_Object=MibTableColumn
astChanWhenHangup=_AstChanWhenHangup_Object((1,3,6,1,4,1,22736,1,5,2,1,9),_AstChanWhenHangup_Type())
astChanWhenHangup.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanWhenHangup.setStatus(_A)
_AstChanApp_Type=DisplayString
_AstChanApp_Object=MibTableColumn
astChanApp=_AstChanApp_Object((1,3,6,1,4,1,22736,1,5,2,1,10),_AstChanApp_Type())
astChanApp.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanApp.setStatus(_A)
_AstChanData_Type=DisplayString
_AstChanData_Object=MibTableColumn
astChanData=_AstChanData_Object((1,3,6,1,4,1,22736,1,5,2,1,11),_AstChanData_Type())
astChanData.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanData.setStatus(_A)
_AstChanContext_Type=DisplayString
_AstChanContext_Object=MibTableColumn
astChanContext=_AstChanContext_Object((1,3,6,1,4,1,22736,1,5,2,1,12),_AstChanContext_Type())
astChanContext.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanContext.setStatus(_A)
_AstChanMacroContext_Type=DisplayString
_AstChanMacroContext_Object=MibTableColumn
astChanMacroContext=_AstChanMacroContext_Object((1,3,6,1,4,1,22736,1,5,2,1,13),_AstChanMacroContext_Type())
astChanMacroContext.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanMacroContext.setStatus(_A)
_AstChanMacroExten_Type=DisplayString
_AstChanMacroExten_Object=MibTableColumn
astChanMacroExten=_AstChanMacroExten_Object((1,3,6,1,4,1,22736,1,5,2,1,14),_AstChanMacroExten_Type())
astChanMacroExten.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanMacroExten.setStatus(_A)
_AstChanMacroPri_Type=Integer32
_AstChanMacroPri_Object=MibTableColumn
astChanMacroPri=_AstChanMacroPri_Object((1,3,6,1,4,1,22736,1,5,2,1,15),_AstChanMacroPri_Type())
astChanMacroPri.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanMacroPri.setStatus(_A)
_AstChanExten_Type=DisplayString
_AstChanExten_Object=MibTableColumn
astChanExten=_AstChanExten_Object((1,3,6,1,4,1,22736,1,5,2,1,16),_AstChanExten_Type())
astChanExten.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanExten.setStatus(_A)
_AstChanPri_Type=Integer32
_AstChanPri_Object=MibTableColumn
astChanPri=_AstChanPri_Object((1,3,6,1,4,1,22736,1,5,2,1,17),_AstChanPri_Type())
astChanPri.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanPri.setStatus(_A)
_AstChanAccountCode_Type=DisplayString
_AstChanAccountCode_Object=MibTableColumn
astChanAccountCode=_AstChanAccountCode_Object((1,3,6,1,4,1,22736,1,5,2,1,18),_AstChanAccountCode_Type())
astChanAccountCode.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanAccountCode.setStatus(_A)
_AstChanForwardTo_Type=DisplayString
_AstChanForwardTo_Object=MibTableColumn
astChanForwardTo=_AstChanForwardTo_Object((1,3,6,1,4,1,22736,1,5,2,1,19),_AstChanForwardTo_Type())
astChanForwardTo.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanForwardTo.setStatus(_A)
_AstChanUniqueId_Type=DisplayString
_AstChanUniqueId_Object=MibTableColumn
astChanUniqueId=_AstChanUniqueId_Object((1,3,6,1,4,1,22736,1,5,2,1,20),_AstChanUniqueId_Type())
astChanUniqueId.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanUniqueId.setStatus(_A)
_AstChanCallGroup_Type=Unsigned32
_AstChanCallGroup_Object=MibTableColumn
astChanCallGroup=_AstChanCallGroup_Object((1,3,6,1,4,1,22736,1,5,2,1,21),_AstChanCallGroup_Type())
astChanCallGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanCallGroup.setStatus(_A)
_AstChanPickupGroup_Type=Unsigned32
_AstChanPickupGroup_Object=MibTableColumn
astChanPickupGroup=_AstChanPickupGroup_Object((1,3,6,1,4,1,22736,1,5,2,1,22),_AstChanPickupGroup_Type())
astChanPickupGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanPickupGroup.setStatus(_A)
class _AstChanState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('stateDown',0),('stateReserved',1),('stateOffHook',2),('stateDialing',3),('stateRing',4),('stateRinging',5),('stateUp',6),('stateBusy',7),('stateDialingOffHook',8),('statePreRing',9)))
_AstChanState_Type.__name__=_C
_AstChanState_Object=MibTableColumn
astChanState=_AstChanState_Object((1,3,6,1,4,1,22736,1,5,2,1,23),_AstChanState_Type())
astChanState.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanState.setStatus(_A)
_AstChanMuted_Type=TruthValue
_AstChanMuted_Object=MibTableColumn
astChanMuted=_AstChanMuted_Object((1,3,6,1,4,1,22736,1,5,2,1,24),_AstChanMuted_Type())
astChanMuted.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanMuted.setStatus(_A)
_AstChanRings_Type=Integer32
_AstChanRings_Object=MibTableColumn
astChanRings=_AstChanRings_Object((1,3,6,1,4,1,22736,1,5,2,1,25),_AstChanRings_Type())
astChanRings.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanRings.setStatus(_A)
_AstChanCidDNID_Type=DisplayString
_AstChanCidDNID_Object=MibTableColumn
astChanCidDNID=_AstChanCidDNID_Object((1,3,6,1,4,1,22736,1,5,2,1,26),_AstChanCidDNID_Type())
astChanCidDNID.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanCidDNID.setStatus(_A)
_AstChanCidNum_Type=DisplayString
_AstChanCidNum_Object=MibTableColumn
astChanCidNum=_AstChanCidNum_Object((1,3,6,1,4,1,22736,1,5,2,1,27),_AstChanCidNum_Type())
astChanCidNum.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanCidNum.setStatus(_A)
_AstChanCidName_Type=DisplayString
_AstChanCidName_Object=MibTableColumn
astChanCidName=_AstChanCidName_Object((1,3,6,1,4,1,22736,1,5,2,1,28),_AstChanCidName_Type())
astChanCidName.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanCidName.setStatus(_A)
_AstChanCidANI_Type=DisplayString
_AstChanCidANI_Object=MibTableColumn
astChanCidANI=_AstChanCidANI_Object((1,3,6,1,4,1,22736,1,5,2,1,29),_AstChanCidANI_Type())
astChanCidANI.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanCidANI.setStatus(_A)
_AstChanCidRDNIS_Type=DisplayString
_AstChanCidRDNIS_Object=MibTableColumn
astChanCidRDNIS=_AstChanCidRDNIS_Object((1,3,6,1,4,1,22736,1,5,2,1,30),_AstChanCidRDNIS_Type())
astChanCidRDNIS.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanCidRDNIS.setStatus(_A)
_AstChanCidPresentation_Type=DisplayString
_AstChanCidPresentation_Object=MibTableColumn
astChanCidPresentation=_AstChanCidPresentation_Object((1,3,6,1,4,1,22736,1,5,2,1,31),_AstChanCidPresentation_Type())
astChanCidPresentation.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanCidPresentation.setStatus(_A)
_AstChanCidANI2_Type=Integer32
_AstChanCidANI2_Object=MibTableColumn
astChanCidANI2=_AstChanCidANI2_Object((1,3,6,1,4,1,22736,1,5,2,1,32),_AstChanCidANI2_Type())
astChanCidANI2.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanCidANI2.setStatus(_A)
_AstChanCidTON_Type=Integer32
_AstChanCidTON_Object=MibTableColumn
astChanCidTON=_AstChanCidTON_Object((1,3,6,1,4,1,22736,1,5,2,1,33),_AstChanCidTON_Type())
astChanCidTON.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanCidTON.setStatus(_A)
_AstChanCidTNS_Type=Integer32
_AstChanCidTNS_Object=MibTableColumn
astChanCidTNS=_AstChanCidTNS_Object((1,3,6,1,4,1,22736,1,5,2,1,34),_AstChanCidTNS_Type())
astChanCidTNS.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanCidTNS.setStatus(_A)
class _AstChanAMAFlags_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('default',0),('omit',1),('billing',2),('documentation',3)))
_AstChanAMAFlags_Type.__name__=_C
_AstChanAMAFlags_Object=MibTableColumn
astChanAMAFlags=_AstChanAMAFlags_Object((1,3,6,1,4,1,22736,1,5,2,1,35),_AstChanAMAFlags_Type())
astChanAMAFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanAMAFlags.setStatus(_A)
class _AstChanADSI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('unknown',0),('available',1),('unavailable',2),('offHookOnly',3)))
_AstChanADSI_Type.__name__=_C
_AstChanADSI_Object=MibTableColumn
astChanADSI=_AstChanADSI_Object((1,3,6,1,4,1,22736,1,5,2,1,36),_AstChanADSI_Type())
astChanADSI.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanADSI.setStatus(_A)
_AstChanToneZone_Type=DisplayString
_AstChanToneZone_Object=MibTableColumn
astChanToneZone=_AstChanToneZone_Object((1,3,6,1,4,1,22736,1,5,2,1,37),_AstChanToneZone_Type())
astChanToneZone.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanToneZone.setStatus(_A)
class _AstChanHangupCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,3,16,17,19,34,38,66)));namedValues=NamedValues(*(('notDefined',0),('unregistered',3),('normal',16),('busy',17),('noAnswer',19),('congestion',34),('failure',38),('noSuchDriver',66)))
_AstChanHangupCause_Type.__name__=_C
_AstChanHangupCause_Object=MibTableColumn
astChanHangupCause=_AstChanHangupCause_Object((1,3,6,1,4,1,22736,1,5,2,1,38),_AstChanHangupCause_Type())
astChanHangupCause.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanHangupCause.setStatus(_A)
_AstChanVariables_Type=DisplayString
_AstChanVariables_Object=MibTableColumn
astChanVariables=_AstChanVariables_Object((1,3,6,1,4,1,22736,1,5,2,1,39),_AstChanVariables_Type())
astChanVariables.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanVariables.setStatus(_A)
class _AstChanFlags_Type(Bits):namedValues=NamedValues(*(('wantsJitter',0),('deferDTMF',1),('writeInterrupt',2),('blocking',3),('zombie',4),('exception',5),('musicOnHold',6),('spying',7),('nativeBridge',8),('autoIncrementingLoop',9)))
_AstChanFlags_Type.__name__='Bits'
_AstChanFlags_Object=MibTableColumn
astChanFlags=_AstChanFlags_Object((1,3,6,1,4,1,22736,1,5,2,1,40),_AstChanFlags_Type())
astChanFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanFlags.setStatus(_A)
class _AstChanTransferCap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,8,9,16,17,24)));namedValues=NamedValues(*(('speech',0),('digital',8),('restrictedDigital',9),('audio3k',16),('digitalWithTones',17),('video',24)))
_AstChanTransferCap_Type.__name__=_C
_AstChanTransferCap_Object=MibTableColumn
astChanTransferCap=_AstChanTransferCap_Object((1,3,6,1,4,1,22736,1,5,2,1,41),_AstChanTransferCap_Type())
astChanTransferCap.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanTransferCap.setStatus(_A)
_AstNumChanTypes_Type=Integer32
_AstNumChanTypes_Object=MibScalar
astNumChanTypes=_AstNumChanTypes_Object((1,3,6,1,4,1,22736,1,5,3),_AstNumChanTypes_Type())
astNumChanTypes.setMaxAccess(_B)
if mibBuilder.loadTexts:astNumChanTypes.setStatus(_A)
_AstChanTypeTable_Object=MibTable
astChanTypeTable=_AstChanTypeTable_Object((1,3,6,1,4,1,22736,1,5,4))
if mibBuilder.loadTexts:astChanTypeTable.setStatus(_A)
_AstChanTypeEntry_Object=MibTableRow
astChanTypeEntry=_AstChanTypeEntry_Object((1,3,6,1,4,1,22736,1,5,4,1))
astChanTypeEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:astChanTypeEntry.setStatus(_A)
class _AstChanTypeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AstChanTypeIndex_Type.__name__=_C
_AstChanTypeIndex_Object=MibTableColumn
astChanTypeIndex=_AstChanTypeIndex_Object((1,3,6,1,4,1,22736,1,5,4,1,1),_AstChanTypeIndex_Type())
astChanTypeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanTypeIndex.setStatus(_A)
_AstChanTypeName_Type=DisplayString
_AstChanTypeName_Object=MibTableColumn
astChanTypeName=_AstChanTypeName_Object((1,3,6,1,4,1,22736,1,5,4,1,2),_AstChanTypeName_Type())
astChanTypeName.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanTypeName.setStatus(_A)
_AstChanTypeDesc_Type=DisplayString
_AstChanTypeDesc_Object=MibTableColumn
astChanTypeDesc=_AstChanTypeDesc_Object((1,3,6,1,4,1,22736,1,5,4,1,3),_AstChanTypeDesc_Type())
astChanTypeDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanTypeDesc.setStatus(_A)
_AstChanTypeDeviceState_Type=TruthValue
_AstChanTypeDeviceState_Object=MibTableColumn
astChanTypeDeviceState=_AstChanTypeDeviceState_Object((1,3,6,1,4,1,22736,1,5,4,1,4),_AstChanTypeDeviceState_Type())
astChanTypeDeviceState.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanTypeDeviceState.setStatus(_A)
_AstChanTypeIndications_Type=TruthValue
_AstChanTypeIndications_Object=MibTableColumn
astChanTypeIndications=_AstChanTypeIndications_Object((1,3,6,1,4,1,22736,1,5,4,1,5),_AstChanTypeIndications_Type())
astChanTypeIndications.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanTypeIndications.setStatus(_A)
_AstChanTypeTransfer_Type=TruthValue
_AstChanTypeTransfer_Object=MibTableColumn
astChanTypeTransfer=_AstChanTypeTransfer_Object((1,3,6,1,4,1,22736,1,5,4,1,6),_AstChanTypeTransfer_Type())
astChanTypeTransfer.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanTypeTransfer.setStatus(_A)
_AstChanTypeChannels_Type=Gauge32
_AstChanTypeChannels_Object=MibTableColumn
astChanTypeChannels=_AstChanTypeChannels_Object((1,3,6,1,4,1,22736,1,5,4,1,7),_AstChanTypeChannels_Type())
astChanTypeChannels.setMaxAccess(_B)
if mibBuilder.loadTexts:astChanTypeChannels.setStatus(_A)
_AstChanScalars_ObjectIdentity=ObjectIdentity
astChanScalars=_AstChanScalars_ObjectIdentity((1,3,6,1,4,1,22736,1,5,5))
_AstNumChanBridge_Type=Gauge32
_AstNumChanBridge_Object=MibScalar
astNumChanBridge=_AstNumChanBridge_Object((1,3,6,1,4,1,22736,1,5,5,1),_AstNumChanBridge_Type())
astNumChanBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:astNumChanBridge.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'asterisk':asterisk,'asteriskVersion':asteriskVersion,'astVersionString':astVersionString,'astVersionTag':astVersionTag,'asteriskConfiguration':asteriskConfiguration,'astConfigUpTime':astConfigUpTime,'astConfigReloadTime':astConfigReloadTime,'astConfigPid':astConfigPid,'astConfigSocket':astConfigSocket,'astConfigCallsActive':astConfigCallsActive,'astConfigCallsProcessed':astConfigCallsProcessed,'asteriskModules':asteriskModules,'astNumModules':astNumModules,'asteriskIndications':asteriskIndications,'astNumIndications':astNumIndications,'astCurrentIndication':astCurrentIndication,'astIndicationsTable':astIndicationsTable,'astIndicationsEntry':astIndicationsEntry,_E:astIndIndex,'astIndCountry':astIndCountry,'astIndAlias':astIndAlias,'astIndDescription':astIndDescription,'asteriskChannels':asteriskChannels,'astNumChannels':astNumChannels,'astChanTable':astChanTable,'astChanEntry':astChanEntry,_F:astChanIndex,'astChanName':astChanName,'astChanLanguage':astChanLanguage,'astChanType':astChanType,'astChanMusicClass':astChanMusicClass,'astChanBridge':astChanBridge,'astChanMasq':astChanMasq,'astChanMasqr':astChanMasqr,'astChanWhenHangup':astChanWhenHangup,'astChanApp':astChanApp,'astChanData':astChanData,'astChanContext':astChanContext,'astChanMacroContext':astChanMacroContext,'astChanMacroExten':astChanMacroExten,'astChanMacroPri':astChanMacroPri,'astChanExten':astChanExten,'astChanPri':astChanPri,'astChanAccountCode':astChanAccountCode,'astChanForwardTo':astChanForwardTo,'astChanUniqueId':astChanUniqueId,'astChanCallGroup':astChanCallGroup,'astChanPickupGroup':astChanPickupGroup,'astChanState':astChanState,'astChanMuted':astChanMuted,'astChanRings':astChanRings,'astChanCidDNID':astChanCidDNID,'astChanCidNum':astChanCidNum,'astChanCidName':astChanCidName,'astChanCidANI':astChanCidANI,'astChanCidRDNIS':astChanCidRDNIS,'astChanCidPresentation':astChanCidPresentation,'astChanCidANI2':astChanCidANI2,'astChanCidTON':astChanCidTON,'astChanCidTNS':astChanCidTNS,'astChanAMAFlags':astChanAMAFlags,'astChanADSI':astChanADSI,'astChanToneZone':astChanToneZone,'astChanHangupCause':astChanHangupCause,'astChanVariables':astChanVariables,'astChanFlags':astChanFlags,'astChanTransferCap':astChanTransferCap,'astNumChanTypes':astNumChanTypes,'astChanTypeTable':astChanTypeTable,'astChanTypeEntry':astChanTypeEntry,_G:astChanTypeIndex,'astChanTypeName':astChanTypeName,'astChanTypeDesc':astChanTypeDesc,'astChanTypeDeviceState':astChanTypeDeviceState,'astChanTypeIndications':astChanTypeIndications,'astChanTypeTransfer':astChanTypeTransfer,'astChanTypeChannels':astChanTypeChannels,'astChanScalars':astChanScalars,'astNumChanBridge':astNumChanBridge})