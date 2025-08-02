_Y='agfeoBasicNotificationGroup'
_X='agfeoPropGroup'
_W='agfeoAccountGroup'
_V='agfeoGroup'
_U='agfeoEventGeneric'
_T='agfeoCStaSipAccountCause'
_S='agfeoCStaSipAccountStatus'
_R='agfeoCCfgSipAccountActive'
_Q='agfeoCCfgSipAccountName'
_P='agfeoCStaSipTestInteger'
_O='agfeoCStaPbxAppUpTime'
_N='agfeoCStaPbxFirmware'
_M='agfeoCStaPbxProductId'
_L='agfeoCStaPbxProduct'
_K='agfeoCLicenceIndex'
_J='agfeoCStaSipAccountIndex'
_I='agfeoCCfgSipAccountIndex'
_H='agfeoEventPropText'
_G='agfeoEventPropSeverity'
_F='agfeoEventPropType'
_E='not-accessible'
_D='Integer32'
_C='AGFEO-PBX-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
agfeoMib=ModuleIdentity((1,3,6,1,4,1,53023))
if mibBuilder.loadTexts:agfeoMib.setRevisions(('2020-03-27 00:00','2018-10-25 00:00','2018-10-14 00:00'))
_AgfeoMibObjects_ObjectIdentity=ObjectIdentity
agfeoMibObjects=_AgfeoMibObjects_ObjectIdentity((1,3,6,1,4,1,53023,1))
if mibBuilder.loadTexts:agfeoMibObjects.setStatus(_A)
_AgfeoCommon_ObjectIdentity=ObjectIdentity
agfeoCommon=_AgfeoCommon_ObjectIdentity((1,3,6,1,4,1,53023,1,1))
if mibBuilder.loadTexts:agfeoCommon.setStatus(_A)
_AgfeoCommonCfg_ObjectIdentity=ObjectIdentity
agfeoCommonCfg=_AgfeoCommonCfg_ObjectIdentity((1,3,6,1,4,1,53023,1,1,1))
if mibBuilder.loadTexts:agfeoCommonCfg.setStatus(_A)
_AgfeoCCfgSip_ObjectIdentity=ObjectIdentity
agfeoCCfgSip=_AgfeoCCfgSip_ObjectIdentity((1,3,6,1,4,1,53023,1,1,1,1))
if mibBuilder.loadTexts:agfeoCCfgSip.setStatus(_A)
_AgfeoCCfgSipAccountTable_Object=MibTable
agfeoCCfgSipAccountTable=_AgfeoCCfgSipAccountTable_Object((1,3,6,1,4,1,53023,1,1,1,1,1))
if mibBuilder.loadTexts:agfeoCCfgSipAccountTable.setStatus(_A)
_AgfeoCCfgSipAccountEntry_Object=MibTableRow
agfeoCCfgSipAccountEntry=_AgfeoCCfgSipAccountEntry_Object((1,3,6,1,4,1,53023,1,1,1,1,1,1))
agfeoCCfgSipAccountEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:agfeoCCfgSipAccountEntry.setStatus(_A)
class _AgfeoCCfgSipAccountIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_AgfeoCCfgSipAccountIndex_Type.__name__=_D
_AgfeoCCfgSipAccountIndex_Object=MibTableColumn
agfeoCCfgSipAccountIndex=_AgfeoCCfgSipAccountIndex_Object((1,3,6,1,4,1,53023,1,1,1,1,1,1,1),_AgfeoCCfgSipAccountIndex_Type())
agfeoCCfgSipAccountIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:agfeoCCfgSipAccountIndex.setStatus(_A)
_AgfeoCCfgSipAccountName_Type=OctetString
_AgfeoCCfgSipAccountName_Object=MibTableColumn
agfeoCCfgSipAccountName=_AgfeoCCfgSipAccountName_Object((1,3,6,1,4,1,53023,1,1,1,1,1,1,2),_AgfeoCCfgSipAccountName_Type())
agfeoCCfgSipAccountName.setMaxAccess(_B)
if mibBuilder.loadTexts:agfeoCCfgSipAccountName.setStatus(_A)
class _AgfeoCCfgSipAccountActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('inactive',0),('active',1)))
_AgfeoCCfgSipAccountActive_Type.__name__=_D
_AgfeoCCfgSipAccountActive_Object=MibTableColumn
agfeoCCfgSipAccountActive=_AgfeoCCfgSipAccountActive_Object((1,3,6,1,4,1,53023,1,1,1,1,1,1,3),_AgfeoCCfgSipAccountActive_Type())
agfeoCCfgSipAccountActive.setMaxAccess(_B)
if mibBuilder.loadTexts:agfeoCCfgSipAccountActive.setStatus(_A)
_AgfeoCommonStats_ObjectIdentity=ObjectIdentity
agfeoCommonStats=_AgfeoCommonStats_ObjectIdentity((1,3,6,1,4,1,53023,1,1,2))
if mibBuilder.loadTexts:agfeoCommonStats.setStatus(_A)
_AgfeoCStaGeneral_ObjectIdentity=ObjectIdentity
agfeoCStaGeneral=_AgfeoCStaGeneral_ObjectIdentity((1,3,6,1,4,1,53023,1,1,2,1))
if mibBuilder.loadTexts:agfeoCStaGeneral.setStatus(_A)
_AgfeoCStaPbxProduct_Type=OctetString
_AgfeoCStaPbxProduct_Object=MibScalar
agfeoCStaPbxProduct=_AgfeoCStaPbxProduct_Object((1,3,6,1,4,1,53023,1,1,2,1,1),_AgfeoCStaPbxProduct_Type())
agfeoCStaPbxProduct.setMaxAccess(_B)
if mibBuilder.loadTexts:agfeoCStaPbxProduct.setStatus(_A)
_AgfeoCStaPbxProductId_Type=OctetString
_AgfeoCStaPbxProductId_Object=MibScalar
agfeoCStaPbxProductId=_AgfeoCStaPbxProductId_Object((1,3,6,1,4,1,53023,1,1,2,1,2),_AgfeoCStaPbxProductId_Type())
agfeoCStaPbxProductId.setMaxAccess(_B)
if mibBuilder.loadTexts:agfeoCStaPbxProductId.setStatus(_A)
_AgfeoCStaPbxFirmware_Type=OctetString
_AgfeoCStaPbxFirmware_Object=MibScalar
agfeoCStaPbxFirmware=_AgfeoCStaPbxFirmware_Object((1,3,6,1,4,1,53023,1,1,2,1,3),_AgfeoCStaPbxFirmware_Type())
agfeoCStaPbxFirmware.setMaxAccess(_B)
if mibBuilder.loadTexts:agfeoCStaPbxFirmware.setStatus(_A)
_AgfeoCStaPbxAppUpTime_Type=OctetString
_AgfeoCStaPbxAppUpTime_Object=MibScalar
agfeoCStaPbxAppUpTime=_AgfeoCStaPbxAppUpTime_Object((1,3,6,1,4,1,53023,1,1,2,1,4),_AgfeoCStaPbxAppUpTime_Type())
agfeoCStaPbxAppUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:agfeoCStaPbxAppUpTime.setStatus(_A)
_AgfeoCStaSip_ObjectIdentity=ObjectIdentity
agfeoCStaSip=_AgfeoCStaSip_ObjectIdentity((1,3,6,1,4,1,53023,1,1,2,2))
if mibBuilder.loadTexts:agfeoCStaSip.setStatus(_A)
_AgfeoCStaSipTest_ObjectIdentity=ObjectIdentity
agfeoCStaSipTest=_AgfeoCStaSipTest_ObjectIdentity((1,3,6,1,4,1,53023,1,1,2,2,1))
if mibBuilder.loadTexts:agfeoCStaSipTest.setStatus(_A)
_AgfeoCStaSipTestInteger_Type=Integer32
_AgfeoCStaSipTestInteger_Object=MibScalar
agfeoCStaSipTestInteger=_AgfeoCStaSipTestInteger_Object((1,3,6,1,4,1,53023,1,1,2,2,1,1),_AgfeoCStaSipTestInteger_Type())
agfeoCStaSipTestInteger.setMaxAccess(_B)
if mibBuilder.loadTexts:agfeoCStaSipTestInteger.setStatus(_A)
_AgfeoCStaSipAccountTable_Object=MibTable
agfeoCStaSipAccountTable=_AgfeoCStaSipAccountTable_Object((1,3,6,1,4,1,53023,1,1,2,2,2))
if mibBuilder.loadTexts:agfeoCStaSipAccountTable.setStatus(_A)
_AgfeoCStaSipAccountEntry_Object=MibTableRow
agfeoCStaSipAccountEntry=_AgfeoCStaSipAccountEntry_Object((1,3,6,1,4,1,53023,1,1,2,2,2,1))
agfeoCStaSipAccountEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:agfeoCStaSipAccountEntry.setStatus(_A)
class _AgfeoCStaSipAccountIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_AgfeoCStaSipAccountIndex_Type.__name__=_D
_AgfeoCStaSipAccountIndex_Object=MibTableColumn
agfeoCStaSipAccountIndex=_AgfeoCStaSipAccountIndex_Object((1,3,6,1,4,1,53023,1,1,2,2,2,1,1),_AgfeoCStaSipAccountIndex_Type())
agfeoCStaSipAccountIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:agfeoCStaSipAccountIndex.setStatus(_A)
class _AgfeoCStaSipAccountStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('down',0),('up',1)))
_AgfeoCStaSipAccountStatus_Type.__name__=_D
_AgfeoCStaSipAccountStatus_Object=MibTableColumn
agfeoCStaSipAccountStatus=_AgfeoCStaSipAccountStatus_Object((1,3,6,1,4,1,53023,1,1,2,2,2,1,2),_AgfeoCStaSipAccountStatus_Type())
agfeoCStaSipAccountStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agfeoCStaSipAccountStatus.setStatus(_A)
_AgfeoCStaSipAccountCause_Type=OctetString
_AgfeoCStaSipAccountCause_Object=MibTableColumn
agfeoCStaSipAccountCause=_AgfeoCStaSipAccountCause_Object((1,3,6,1,4,1,53023,1,1,2,2,2,1,3),_AgfeoCStaSipAccountCause_Type())
agfeoCStaSipAccountCause.setMaxAccess(_B)
if mibBuilder.loadTexts:agfeoCStaSipAccountCause.setStatus(_A)
_AgfeoCStaIpChannel_ObjectIdentity=ObjectIdentity
agfeoCStaIpChannel=_AgfeoCStaIpChannel_ObjectIdentity((1,3,6,1,4,1,53023,1,1,2,3))
if mibBuilder.loadTexts:agfeoCStaIpChannel.setStatus(_A)
_AgfeoCStaIpChannelAvailActual_Type=Integer32
_AgfeoCStaIpChannelAvailActual_Object=MibScalar
agfeoCStaIpChannelAvailActual=_AgfeoCStaIpChannelAvailActual_Object((1,3,6,1,4,1,53023,1,1,2,3,1),_AgfeoCStaIpChannelAvailActual_Type())
agfeoCStaIpChannelAvailActual.setMaxAccess(_B)
if mibBuilder.loadTexts:agfeoCStaIpChannelAvailActual.setStatus(_A)
_AgfeoCStaIpChannelAvailMax_Type=Integer32
_AgfeoCStaIpChannelAvailMax_Object=MibScalar
agfeoCStaIpChannelAvailMax=_AgfeoCStaIpChannelAvailMax_Object((1,3,6,1,4,1,53023,1,1,2,3,2),_AgfeoCStaIpChannelAvailMax_Type())
agfeoCStaIpChannelAvailMax.setMaxAccess(_B)
if mibBuilder.loadTexts:agfeoCStaIpChannelAvailMax.setStatus(_A)
_AgfeoCStaIpChannelLoadActual_Type=Integer32
_AgfeoCStaIpChannelLoadActual_Object=MibScalar
agfeoCStaIpChannelLoadActual=_AgfeoCStaIpChannelLoadActual_Object((1,3,6,1,4,1,53023,1,1,2,3,3),_AgfeoCStaIpChannelLoadActual_Type())
agfeoCStaIpChannelLoadActual.setMaxAccess(_B)
if mibBuilder.loadTexts:agfeoCStaIpChannelLoadActual.setStatus(_A)
_AgfeoCStaIpChannelLoadMax_Type=Integer32
_AgfeoCStaIpChannelLoadMax_Object=MibScalar
agfeoCStaIpChannelLoadMax=_AgfeoCStaIpChannelLoadMax_Object((1,3,6,1,4,1,53023,1,1,2,3,4),_AgfeoCStaIpChannelLoadMax_Type())
agfeoCStaIpChannelLoadMax.setMaxAccess(_B)
if mibBuilder.loadTexts:agfeoCStaIpChannelLoadMax.setStatus(_A)
_AgfeoCStaCalls_ObjectIdentity=ObjectIdentity
agfeoCStaCalls=_AgfeoCStaCalls_ObjectIdentity((1,3,6,1,4,1,53023,1,1,2,4))
if mibBuilder.loadTexts:agfeoCStaCalls.setStatus(_A)
_AgfeoCStaCallsAvailActual_Type=Integer32
_AgfeoCStaCallsAvailActual_Object=MibScalar
agfeoCStaCallsAvailActual=_AgfeoCStaCallsAvailActual_Object((1,3,6,1,4,1,53023,1,1,2,4,1),_AgfeoCStaCallsAvailActual_Type())
agfeoCStaCallsAvailActual.setMaxAccess(_B)
if mibBuilder.loadTexts:agfeoCStaCallsAvailActual.setStatus(_A)
_AgfeoCStaCallsAvailMax_Type=Integer32
_AgfeoCStaCallsAvailMax_Object=MibScalar
agfeoCStaCallsAvailMax=_AgfeoCStaCallsAvailMax_Object((1,3,6,1,4,1,53023,1,1,2,4,2),_AgfeoCStaCallsAvailMax_Type())
agfeoCStaCallsAvailMax.setMaxAccess(_B)
if mibBuilder.loadTexts:agfeoCStaCallsAvailMax.setStatus(_A)
_AgfeoCStaCallsLoadActual_Type=Integer32
_AgfeoCStaCallsLoadActual_Object=MibScalar
agfeoCStaCallsLoadActual=_AgfeoCStaCallsLoadActual_Object((1,3,6,1,4,1,53023,1,1,2,4,3),_AgfeoCStaCallsLoadActual_Type())
agfeoCStaCallsLoadActual.setMaxAccess(_B)
if mibBuilder.loadTexts:agfeoCStaCallsLoadActual.setStatus(_A)
_AgfeoCStaCallsLoadMax_Type=Integer32
_AgfeoCStaCallsLoadMax_Object=MibScalar
agfeoCStaCallsLoadMax=_AgfeoCStaCallsLoadMax_Object((1,3,6,1,4,1,53023,1,1,2,4,4),_AgfeoCStaCallsLoadMax_Type())
agfeoCStaCallsLoadMax.setMaxAccess(_B)
if mibBuilder.loadTexts:agfeoCStaCallsLoadMax.setStatus(_A)
_AgfeoCommonLicence_ObjectIdentity=ObjectIdentity
agfeoCommonLicence=_AgfeoCommonLicence_ObjectIdentity((1,3,6,1,4,1,53023,1,1,3))
if mibBuilder.loadTexts:agfeoCommonLicence.setStatus(_A)
_AgfeoCLicenceTable_Object=MibTable
agfeoCLicenceTable=_AgfeoCLicenceTable_Object((1,3,6,1,4,1,53023,1,1,3,1))
if mibBuilder.loadTexts:agfeoCLicenceTable.setStatus(_A)
_AgfeoCLicenceEntry_Object=MibTableRow
agfeoCLicenceEntry=_AgfeoCLicenceEntry_Object((1,3,6,1,4,1,53023,1,1,3,1,1))
agfeoCLicenceEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:agfeoCLicenceEntry.setStatus(_A)
class _AgfeoCLicenceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_AgfeoCLicenceIndex_Type.__name__=_D
_AgfeoCLicenceIndex_Object=MibTableColumn
agfeoCLicenceIndex=_AgfeoCLicenceIndex_Object((1,3,6,1,4,1,53023,1,1,3,1,1,1),_AgfeoCLicenceIndex_Type())
agfeoCLicenceIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:agfeoCLicenceIndex.setStatus(_A)
_AgfeoCLicenceVersion_Type=OctetString
_AgfeoCLicenceVersion_Object=MibTableColumn
agfeoCLicenceVersion=_AgfeoCLicenceVersion_Object((1,3,6,1,4,1,53023,1,1,3,1,1,2),_AgfeoCLicenceVersion_Type())
agfeoCLicenceVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:agfeoCLicenceVersion.setStatus(_A)
_AgfeoCLicenceIssue_Type=OctetString
_AgfeoCLicenceIssue_Object=MibTableColumn
agfeoCLicenceIssue=_AgfeoCLicenceIssue_Object((1,3,6,1,4,1,53023,1,1,3,1,1,3),_AgfeoCLicenceIssue_Type())
agfeoCLicenceIssue.setMaxAccess(_B)
if mibBuilder.loadTexts:agfeoCLicenceIssue.setStatus(_A)
_AgfeoCLicenceUUID_Type=OctetString
_AgfeoCLicenceUUID_Object=MibTableColumn
agfeoCLicenceUUID=_AgfeoCLicenceUUID_Object((1,3,6,1,4,1,53023,1,1,3,1,1,4),_AgfeoCLicenceUUID_Type())
agfeoCLicenceUUID.setMaxAccess(_B)
if mibBuilder.loadTexts:agfeoCLicenceUUID.setStatus(_A)
_AgfeoCLicenceSerial_Type=OctetString
_AgfeoCLicenceSerial_Object=MibTableColumn
agfeoCLicenceSerial=_AgfeoCLicenceSerial_Object((1,3,6,1,4,1,53023,1,1,3,1,1,5),_AgfeoCLicenceSerial_Type())
agfeoCLicenceSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:agfeoCLicenceSerial.setStatus(_A)
_AgfeoCLicenceCode_Type=OctetString
_AgfeoCLicenceCode_Object=MibTableColumn
agfeoCLicenceCode=_AgfeoCLicenceCode_Object((1,3,6,1,4,1,53023,1,1,3,1,1,6),_AgfeoCLicenceCode_Type())
agfeoCLicenceCode.setMaxAccess(_B)
if mibBuilder.loadTexts:agfeoCLicenceCode.setStatus(_A)
_AgfeoCLicenceAmount_Type=Integer32
_AgfeoCLicenceAmount_Object=MibTableColumn
agfeoCLicenceAmount=_AgfeoCLicenceAmount_Object((1,3,6,1,4,1,53023,1,1,3,1,1,7),_AgfeoCLicenceAmount_Type())
agfeoCLicenceAmount.setMaxAccess(_B)
if mibBuilder.loadTexts:agfeoCLicenceAmount.setStatus(_A)
_AgfeoCLicenceStart_Type=OctetString
_AgfeoCLicenceStart_Object=MibTableColumn
agfeoCLicenceStart=_AgfeoCLicenceStart_Object((1,3,6,1,4,1,53023,1,1,3,1,1,8),_AgfeoCLicenceStart_Type())
agfeoCLicenceStart.setMaxAccess(_B)
if mibBuilder.loadTexts:agfeoCLicenceStart.setStatus(_A)
_AgfeoCLicenceEnd_Type=OctetString
_AgfeoCLicenceEnd_Object=MibTableColumn
agfeoCLicenceEnd=_AgfeoCLicenceEnd_Object((1,3,6,1,4,1,53023,1,1,3,1,1,9),_AgfeoCLicenceEnd_Type())
agfeoCLicenceEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:agfeoCLicenceEnd.setStatus(_A)
_AgfeoCLicenceStatus_Type=OctetString
_AgfeoCLicenceStatus_Object=MibTableColumn
agfeoCLicenceStatus=_AgfeoCLicenceStatus_Object((1,3,6,1,4,1,53023,1,1,3,1,1,10),_AgfeoCLicenceStatus_Type())
agfeoCLicenceStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agfeoCLicenceStatus.setStatus(_A)
_AgfeoMibNotify_ObjectIdentity=ObjectIdentity
agfeoMibNotify=_AgfeoMibNotify_ObjectIdentity((1,3,6,1,4,1,53023,2))
if mibBuilder.loadTexts:agfeoMibNotify.setStatus(_A)
_AgfeoEventList_ObjectIdentity=ObjectIdentity
agfeoEventList=_AgfeoEventList_ObjectIdentity((1,3,6,1,4,1,53023,2,0))
if mibBuilder.loadTexts:agfeoEventList.setStatus(_A)
_AgfeoEventProperties_ObjectIdentity=ObjectIdentity
agfeoEventProperties=_AgfeoEventProperties_ObjectIdentity((1,3,6,1,4,1,53023,2,1))
if mibBuilder.loadTexts:agfeoEventProperties.setStatus(_A)
class _AgfeoEventPropType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('type0',0),('type1',1),('sipaccount',2),('type3',3)))
_AgfeoEventPropType_Type.__name__=_D
_AgfeoEventPropType_Object=MibScalar
agfeoEventPropType=_AgfeoEventPropType_Object((1,3,6,1,4,1,53023,2,1,1),_AgfeoEventPropType_Type())
agfeoEventPropType.setMaxAccess(_B)
if mibBuilder.loadTexts:agfeoEventPropType.setStatus(_A)
class _AgfeoEventPropSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('emergency',0),('alert',1),('critical',2),('error',3),('warning',4),('notice',5),('informational',6),('debug',7)))
_AgfeoEventPropSeverity_Type.__name__=_D
_AgfeoEventPropSeverity_Object=MibScalar
agfeoEventPropSeverity=_AgfeoEventPropSeverity_Object((1,3,6,1,4,1,53023,2,1,2),_AgfeoEventPropSeverity_Type())
agfeoEventPropSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:agfeoEventPropSeverity.setStatus(_A)
_AgfeoEventPropText_Type=OctetString
_AgfeoEventPropText_Object=MibScalar
agfeoEventPropText=_AgfeoEventPropText_Object((1,3,6,1,4,1,53023,2,1,3),_AgfeoEventPropText_Type())
agfeoEventPropText.setMaxAccess(_B)
if mibBuilder.loadTexts:agfeoEventPropText.setStatus(_A)
_AgfeoMIBConformance_ObjectIdentity=ObjectIdentity
agfeoMIBConformance=_AgfeoMIBConformance_ObjectIdentity((1,3,6,1,4,1,53023,3))
_AgfeoCompliances_ObjectIdentity=ObjectIdentity
agfeoCompliances=_AgfeoCompliances_ObjectIdentity((1,3,6,1,4,1,53023,3,1))
_AgfeoGroups_ObjectIdentity=ObjectIdentity
agfeoGroups=_AgfeoGroups_ObjectIdentity((1,3,6,1,4,1,53023,3,2))
agfeoGroup=ObjectGroup((1,3,6,1,4,1,53023,3,2,1))
agfeoGroup.setObjects(*((_C,_L),(_C,_M),(_C,_N),(_C,_O)))
if mibBuilder.loadTexts:agfeoGroup.setStatus(_A)
agfeoAccountGroup=ObjectGroup((1,3,6,1,4,1,53023,3,2,2))
agfeoAccountGroup.setObjects(*((_C,_P),(_C,_Q),(_C,_R),(_C,_S),(_C,_T)))
if mibBuilder.loadTexts:agfeoAccountGroup.setStatus(_A)
agfeoPropGroup=ObjectGroup((1,3,6,1,4,1,53023,3,2,3))
agfeoPropGroup.setObjects(*((_C,_F),(_C,_G),(_C,_H)))
if mibBuilder.loadTexts:agfeoPropGroup.setStatus(_A)
agfeoEventGeneric=NotificationType((1,3,6,1,4,1,53023,2,0,1))
agfeoEventGeneric.setObjects(*((_C,_F),(_C,_G),(_C,_H)))
if mibBuilder.loadTexts:agfeoEventGeneric.setStatus(_A)
agfeoBasicNotificationGroup=NotificationGroup((1,3,6,1,4,1,53023,3,2,4))
agfeoBasicNotificationGroup.setObjects((_C,_U))
if mibBuilder.loadTexts:agfeoBasicNotificationGroup.setStatus(_A)
agfeoCompliance=ModuleCompliance((1,3,6,1,4,1,53023,3,1,1))
agfeoCompliance.setObjects(*((_C,_V),(_C,_W),(_C,_X),(_C,_Y)))
if mibBuilder.loadTexts:agfeoCompliance.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'agfeoMib':agfeoMib,'agfeoMibObjects':agfeoMibObjects,'agfeoCommon':agfeoCommon,'agfeoCommonCfg':agfeoCommonCfg,'agfeoCCfgSip':agfeoCCfgSip,'agfeoCCfgSipAccountTable':agfeoCCfgSipAccountTable,'agfeoCCfgSipAccountEntry':agfeoCCfgSipAccountEntry,_I:agfeoCCfgSipAccountIndex,_Q:agfeoCCfgSipAccountName,_R:agfeoCCfgSipAccountActive,'agfeoCommonStats':agfeoCommonStats,'agfeoCStaGeneral':agfeoCStaGeneral,_L:agfeoCStaPbxProduct,_M:agfeoCStaPbxProductId,_N:agfeoCStaPbxFirmware,_O:agfeoCStaPbxAppUpTime,'agfeoCStaSip':agfeoCStaSip,'agfeoCStaSipTest':agfeoCStaSipTest,_P:agfeoCStaSipTestInteger,'agfeoCStaSipAccountTable':agfeoCStaSipAccountTable,'agfeoCStaSipAccountEntry':agfeoCStaSipAccountEntry,_J:agfeoCStaSipAccountIndex,_S:agfeoCStaSipAccountStatus,_T:agfeoCStaSipAccountCause,'agfeoCStaIpChannel':agfeoCStaIpChannel,'agfeoCStaIpChannelAvailActual':agfeoCStaIpChannelAvailActual,'agfeoCStaIpChannelAvailMax':agfeoCStaIpChannelAvailMax,'agfeoCStaIpChannelLoadActual':agfeoCStaIpChannelLoadActual,'agfeoCStaIpChannelLoadMax':agfeoCStaIpChannelLoadMax,'agfeoCStaCalls':agfeoCStaCalls,'agfeoCStaCallsAvailActual':agfeoCStaCallsAvailActual,'agfeoCStaCallsAvailMax':agfeoCStaCallsAvailMax,'agfeoCStaCallsLoadActual':agfeoCStaCallsLoadActual,'agfeoCStaCallsLoadMax':agfeoCStaCallsLoadMax,'agfeoCommonLicence':agfeoCommonLicence,'agfeoCLicenceTable':agfeoCLicenceTable,'agfeoCLicenceEntry':agfeoCLicenceEntry,_K:agfeoCLicenceIndex,'agfeoCLicenceVersion':agfeoCLicenceVersion,'agfeoCLicenceIssue':agfeoCLicenceIssue,'agfeoCLicenceUUID':agfeoCLicenceUUID,'agfeoCLicenceSerial':agfeoCLicenceSerial,'agfeoCLicenceCode':agfeoCLicenceCode,'agfeoCLicenceAmount':agfeoCLicenceAmount,'agfeoCLicenceStart':agfeoCLicenceStart,'agfeoCLicenceEnd':agfeoCLicenceEnd,'agfeoCLicenceStatus':agfeoCLicenceStatus,'agfeoMibNotify':agfeoMibNotify,'agfeoEventList':agfeoEventList,_U:agfeoEventGeneric,'agfeoEventProperties':agfeoEventProperties,_F:agfeoEventPropType,_G:agfeoEventPropSeverity,_H:agfeoEventPropText,'agfeoMIBConformance':agfeoMIBConformance,'agfeoCompliances':agfeoCompliances,'agfeoCompliance':agfeoCompliance,'agfeoGroups':agfeoGroups,_V:agfeoGroup,_W:agfeoAccountGroup,_X:agfeoPropGroup,_Y:agfeoBasicNotificationGroup})