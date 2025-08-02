_k='oaApsMibMandatoryConfigGroupMode'
_j='oaApsMibMandatoryConfigMode'
_i='oaApsConfigGroupProtectLineDefect'
_h='oaApsConfigGroupWorkingLineDefect'
_g='oaApsConfigGroupCmdSwitchStatus'
_f='oaApsConfigGroupCmdSwitchRec'
_e='oaApsConfigGroupCmdSwitchTrans'
_d='oaApsConfigGroupProtectStatus'
_c='oaApsConfigGroupWorkingStatus'
_b='oaApsConfigGroupProtectLinePort'
_a='oaApsConfigGroupWorkingLinePort'
_Z='oaApsConfigGroupPortMembers'
_Y='oaApsConfigGroupName'
_X='oaApsModeVersion'
_W='oaApsModeConfigGroups'
_V='oaApsModeConfigWaitToRestore'
_U='oaApsModeConfigRevert'
_T='oaApsModeConfigMode'
_S='otu2BDI'
_R='otu2LOS'
_Q='odu1AIS'
_P='noDefect'
_O='standBy'
_N='active'
_M='inActive'
_L='oaApsConfigGroupId'
_K='oaApsConfigGroupSlotIndex'
_J='oaApsModeConfigSlotIndex'
_I='DisplayString'
_H='OctetString'
_G='not-accessible'
_F='Bits'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='OA-APS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI',_F,'Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention')
oaApsMIB=ModuleIdentity((1,3,6,1,4,1,6926,1,41,20))
if mibBuilder.loadTexts:oaApsMIB.setRevisions(('2012-07-30 00:00','2012-02-07 00:00','2011-09-15 00:00'))
class ApsSwitchCommand(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('noCmd',1),('clear',2),('lockoutOfProtection',3),('forcedSwitchWorkToProtect',4),('forcedSwitchProtectToWork',5),('manualSwitchWorkToProtect',6),('manualSwitchProtectToWork',7)))
_Oaccess_ObjectIdentity=ObjectIdentity
oaccess=_Oaccess_ObjectIdentity((1,3,6,1,4,1,6926))
_OaManagement_ObjectIdentity=ObjectIdentity
oaManagement=_OaManagement_ObjectIdentity((1,3,6,1,4,1,6926,1))
_OaLambdaDriver_ObjectIdentity=ObjectIdentity
oaLambdaDriver=_OaLambdaDriver_ObjectIdentity((1,3,6,1,4,1,6926,1,41))
_OaApsConfig_ObjectIdentity=ObjectIdentity
oaApsConfig=_OaApsConfig_ObjectIdentity((1,3,6,1,4,1,6926,1,41,20,1))
_OaApsModeConfigTable_Object=MibTable
oaApsModeConfigTable=_OaApsModeConfigTable_Object((1,3,6,1,4,1,6926,1,41,20,1,1))
if mibBuilder.loadTexts:oaApsModeConfigTable.setStatus(_A)
_OaApsModeConfigEntry_Object=MibTableRow
oaApsModeConfigEntry=_OaApsModeConfigEntry_Object((1,3,6,1,4,1,6926,1,41,20,1,1,1))
oaApsModeConfigEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:oaApsModeConfigEntry.setStatus(_A)
class _OaApsModeConfigSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_OaApsModeConfigSlotIndex_Type.__name__=_D
_OaApsModeConfigSlotIndex_Object=MibTableColumn
oaApsModeConfigSlotIndex=_OaApsModeConfigSlotIndex_Object((1,3,6,1,4,1,6926,1,41,20,1,1,1,1),_OaApsModeConfigSlotIndex_Type())
oaApsModeConfigSlotIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:oaApsModeConfigSlotIndex.setStatus(_A)
class _OaApsModeConfigMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noAps',1),('apsProtect',2)))
_OaApsModeConfigMode_Type.__name__=_D
_OaApsModeConfigMode_Object=MibTableColumn
oaApsModeConfigMode=_OaApsModeConfigMode_Object((1,3,6,1,4,1,6926,1,41,20,1,1,1,2),_OaApsModeConfigMode_Type())
oaApsModeConfigMode.setMaxAccess(_E)
if mibBuilder.loadTexts:oaApsModeConfigMode.setStatus(_A)
class _OaApsModeConfigRevert_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nonRevertive',1),('revertive',2)))
_OaApsModeConfigRevert_Type.__name__=_D
_OaApsModeConfigRevert_Object=MibTableColumn
oaApsModeConfigRevert=_OaApsModeConfigRevert_Object((1,3,6,1,4,1,6926,1,41,20,1,1,1,3),_OaApsModeConfigRevert_Type())
oaApsModeConfigRevert.setMaxAccess(_E)
if mibBuilder.loadTexts:oaApsModeConfigRevert.setStatus(_A)
class _OaApsModeConfigWaitToRestore_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,720))
_OaApsModeConfigWaitToRestore_Type.__name__=_D
_OaApsModeConfigWaitToRestore_Object=MibTableColumn
oaApsModeConfigWaitToRestore=_OaApsModeConfigWaitToRestore_Object((1,3,6,1,4,1,6926,1,41,20,1,1,1,4),_OaApsModeConfigWaitToRestore_Type())
oaApsModeConfigWaitToRestore.setMaxAccess(_E)
if mibBuilder.loadTexts:oaApsModeConfigWaitToRestore.setStatus(_A)
if mibBuilder.loadTexts:oaApsModeConfigWaitToRestore.setUnits('seconds')
_OaApsModeConfigGroups_Type=Gauge32
_OaApsModeConfigGroups_Object=MibTableColumn
oaApsModeConfigGroups=_OaApsModeConfigGroups_Object((1,3,6,1,4,1,6926,1,41,20,1,1,1,5),_OaApsModeConfigGroups_Type())
oaApsModeConfigGroups.setMaxAccess(_C)
if mibBuilder.loadTexts:oaApsModeConfigGroups.setStatus(_A)
_OaApsModeVersion_Type=Integer32
_OaApsModeVersion_Object=MibTableColumn
oaApsModeVersion=_OaApsModeVersion_Object((1,3,6,1,4,1,6926,1,41,20,1,1,1,6),_OaApsModeVersion_Type())
oaApsModeVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:oaApsModeVersion.setStatus(_A)
_OaApsConfigGroupTable_Object=MibTable
oaApsConfigGroupTable=_OaApsConfigGroupTable_Object((1,3,6,1,4,1,6926,1,41,20,1,5))
if mibBuilder.loadTexts:oaApsConfigGroupTable.setStatus(_A)
_OaApsConfigGroupEntry_Object=MibTableRow
oaApsConfigGroupEntry=_OaApsConfigGroupEntry_Object((1,3,6,1,4,1,6926,1,41,20,1,5,1))
oaApsConfigGroupEntry.setIndexNames((0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:oaApsConfigGroupEntry.setStatus(_A)
class _OaApsConfigGroupSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_OaApsConfigGroupSlotIndex_Type.__name__=_D
_OaApsConfigGroupSlotIndex_Object=MibTableColumn
oaApsConfigGroupSlotIndex=_OaApsConfigGroupSlotIndex_Object((1,3,6,1,4,1,6926,1,41,20,1,5,1,1),_OaApsConfigGroupSlotIndex_Type())
oaApsConfigGroupSlotIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:oaApsConfigGroupSlotIndex.setStatus(_A)
class _OaApsConfigGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_OaApsConfigGroupId_Type.__name__=_D
_OaApsConfigGroupId_Object=MibTableColumn
oaApsConfigGroupId=_OaApsConfigGroupId_Object((1,3,6,1,4,1,6926,1,41,20,1,5,1,2),_OaApsConfigGroupId_Type())
oaApsConfigGroupId.setMaxAccess(_G)
if mibBuilder.loadTexts:oaApsConfigGroupId.setStatus(_A)
class _OaApsConfigGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_OaApsConfigGroupName_Type.__name__=_I
_OaApsConfigGroupName_Object=MibTableColumn
oaApsConfigGroupName=_OaApsConfigGroupName_Object((1,3,6,1,4,1,6926,1,41,20,1,5,1,3),_OaApsConfigGroupName_Type())
oaApsConfigGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:oaApsConfigGroupName.setStatus(_A)
class _OaApsConfigGroupPortMembers_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_OaApsConfigGroupPortMembers_Type.__name__=_H
_OaApsConfigGroupPortMembers_Object=MibTableColumn
oaApsConfigGroupPortMembers=_OaApsConfigGroupPortMembers_Object((1,3,6,1,4,1,6926,1,41,20,1,5,1,4),_OaApsConfigGroupPortMembers_Type())
oaApsConfigGroupPortMembers.setMaxAccess(_C)
if mibBuilder.loadTexts:oaApsConfigGroupPortMembers.setStatus(_A)
class _OaApsConfigGroupWorkingLinePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_OaApsConfigGroupWorkingLinePort_Type.__name__=_D
_OaApsConfigGroupWorkingLinePort_Object=MibTableColumn
oaApsConfigGroupWorkingLinePort=_OaApsConfigGroupWorkingLinePort_Object((1,3,6,1,4,1,6926,1,41,20,1,5,1,5),_OaApsConfigGroupWorkingLinePort_Type())
oaApsConfigGroupWorkingLinePort.setMaxAccess(_C)
if mibBuilder.loadTexts:oaApsConfigGroupWorkingLinePort.setStatus(_A)
class _OaApsConfigGroupProtectLinePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_OaApsConfigGroupProtectLinePort_Type.__name__=_D
_OaApsConfigGroupProtectLinePort_Object=MibTableColumn
oaApsConfigGroupProtectLinePort=_OaApsConfigGroupProtectLinePort_Object((1,3,6,1,4,1,6926,1,41,20,1,5,1,6),_OaApsConfigGroupProtectLinePort_Type())
oaApsConfigGroupProtectLinePort.setMaxAccess(_C)
if mibBuilder.loadTexts:oaApsConfigGroupProtectLinePort.setStatus(_A)
class _OaApsConfigGroupWorkingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3)))
_OaApsConfigGroupWorkingStatus_Type.__name__=_D
_OaApsConfigGroupWorkingStatus_Object=MibTableColumn
oaApsConfigGroupWorkingStatus=_OaApsConfigGroupWorkingStatus_Object((1,3,6,1,4,1,6926,1,41,20,1,5,1,7),_OaApsConfigGroupWorkingStatus_Type())
oaApsConfigGroupWorkingStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:oaApsConfigGroupWorkingStatus.setStatus(_A)
class _OaApsConfigGroupProtectStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3)))
_OaApsConfigGroupProtectStatus_Type.__name__=_D
_OaApsConfigGroupProtectStatus_Object=MibTableColumn
oaApsConfigGroupProtectStatus=_OaApsConfigGroupProtectStatus_Object((1,3,6,1,4,1,6926,1,41,20,1,5,1,8),_OaApsConfigGroupProtectStatus_Type())
oaApsConfigGroupProtectStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:oaApsConfigGroupProtectStatus.setStatus(_A)
_OaApsConfigGroupCmdSwitchTrans_Type=ApsSwitchCommand
_OaApsConfigGroupCmdSwitchTrans_Object=MibTableColumn
oaApsConfigGroupCmdSwitchTrans=_OaApsConfigGroupCmdSwitchTrans_Object((1,3,6,1,4,1,6926,1,41,20,1,5,1,9),_OaApsConfigGroupCmdSwitchTrans_Type())
oaApsConfigGroupCmdSwitchTrans.setMaxAccess(_E)
if mibBuilder.loadTexts:oaApsConfigGroupCmdSwitchTrans.setStatus(_A)
_OaApsConfigGroupCmdSwitchRec_Type=ApsSwitchCommand
_OaApsConfigGroupCmdSwitchRec_Object=MibTableColumn
oaApsConfigGroupCmdSwitchRec=_OaApsConfigGroupCmdSwitchRec_Object((1,3,6,1,4,1,6926,1,41,20,1,5,1,10),_OaApsConfigGroupCmdSwitchRec_Type())
oaApsConfigGroupCmdSwitchRec.setMaxAccess(_C)
if mibBuilder.loadTexts:oaApsConfigGroupCmdSwitchRec.setStatus(_A)
_OaApsConfigGroupCmdSwitchStatus_Type=ApsSwitchCommand
_OaApsConfigGroupCmdSwitchStatus_Object=MibTableColumn
oaApsConfigGroupCmdSwitchStatus=_OaApsConfigGroupCmdSwitchStatus_Object((1,3,6,1,4,1,6926,1,41,20,1,5,1,11),_OaApsConfigGroupCmdSwitchStatus_Type())
oaApsConfigGroupCmdSwitchStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:oaApsConfigGroupCmdSwitchStatus.setStatus(_A)
class _OaApsConfigGroupWorkingLineDefect_Type(Bits):namedValues=NamedValues(*((_P,0),(_Q,1),(_R,2),(_S,3)))
_OaApsConfigGroupWorkingLineDefect_Type.__name__=_F
_OaApsConfigGroupWorkingLineDefect_Object=MibTableColumn
oaApsConfigGroupWorkingLineDefect=_OaApsConfigGroupWorkingLineDefect_Object((1,3,6,1,4,1,6926,1,41,20,1,5,1,12),_OaApsConfigGroupWorkingLineDefect_Type())
oaApsConfigGroupWorkingLineDefect.setMaxAccess(_C)
if mibBuilder.loadTexts:oaApsConfigGroupWorkingLineDefect.setStatus(_A)
class _OaApsConfigGroupProtectLineDefect_Type(Bits):namedValues=NamedValues(*((_P,0),(_Q,1),(_R,2),(_S,3)))
_OaApsConfigGroupProtectLineDefect_Type.__name__=_F
_OaApsConfigGroupProtectLineDefect_Object=MibTableColumn
oaApsConfigGroupProtectLineDefect=_OaApsConfigGroupProtectLineDefect_Object((1,3,6,1,4,1,6926,1,41,20,1,5,1,13),_OaApsConfigGroupProtectLineDefect_Type())
oaApsConfigGroupProtectLineDefect.setMaxAccess(_C)
if mibBuilder.loadTexts:oaApsConfigGroupProtectLineDefect.setStatus(_A)
_OaApsMIBNotifications_ObjectIdentity=ObjectIdentity
oaApsMIBNotifications=_OaApsMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6926,1,41,20,2))
_OaApsMIBConformance_ObjectIdentity=ObjectIdentity
oaApsMIBConformance=_OaApsMIBConformance_ObjectIdentity((1,3,6,1,4,1,6926,1,41,20,3))
_OaApsMIBCompliances_ObjectIdentity=ObjectIdentity
oaApsMIBCompliances=_OaApsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6926,1,41,20,3,1))
_OaApsMIBGroups_ObjectIdentity=ObjectIdentity
oaApsMIBGroups=_OaApsMIBGroups_ObjectIdentity((1,3,6,1,4,1,6926,1,41,20,3,2))
oaApsMibMandatoryConfigMode=ObjectGroup((1,3,6,1,4,1,6926,1,41,20,3,2,1))
oaApsMibMandatoryConfigMode.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:oaApsMibMandatoryConfigMode.setStatus(_A)
oaApsMibMandatoryConfigGroupMode=ObjectGroup((1,3,6,1,4,1,6926,1,41,20,3,2,2))
oaApsMibMandatoryConfigGroupMode.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:oaApsMibMandatoryConfigGroupMode.setStatus(_A)
oaApsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6926,1,41,20,3,1,1))
oaApsMIBCompliance.setObjects(*((_B,_j),(_B,_k)))
if mibBuilder.loadTexts:oaApsMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ApsSwitchCommand':ApsSwitchCommand,'oaccess':oaccess,'oaManagement':oaManagement,'oaLambdaDriver':oaLambdaDriver,'oaApsMIB':oaApsMIB,'oaApsConfig':oaApsConfig,'oaApsModeConfigTable':oaApsModeConfigTable,'oaApsModeConfigEntry':oaApsModeConfigEntry,_J:oaApsModeConfigSlotIndex,_T:oaApsModeConfigMode,_U:oaApsModeConfigRevert,_V:oaApsModeConfigWaitToRestore,_W:oaApsModeConfigGroups,_X:oaApsModeVersion,'oaApsConfigGroupTable':oaApsConfigGroupTable,'oaApsConfigGroupEntry':oaApsConfigGroupEntry,_K:oaApsConfigGroupSlotIndex,_L:oaApsConfigGroupId,_Y:oaApsConfigGroupName,_Z:oaApsConfigGroupPortMembers,_a:oaApsConfigGroupWorkingLinePort,_b:oaApsConfigGroupProtectLinePort,_c:oaApsConfigGroupWorkingStatus,_d:oaApsConfigGroupProtectStatus,_e:oaApsConfigGroupCmdSwitchTrans,_f:oaApsConfigGroupCmdSwitchRec,_g:oaApsConfigGroupCmdSwitchStatus,_h:oaApsConfigGroupWorkingLineDefect,_i:oaApsConfigGroupProtectLineDefect,'oaApsMIBNotifications':oaApsMIBNotifications,'oaApsMIBConformance':oaApsMIBConformance,'oaApsMIBCompliances':oaApsMIBCompliances,'oaApsMIBCompliance':oaApsMIBCompliance,'oaApsMIBGroups':oaApsMIBGroups,_j:oaApsMibMandatoryConfigMode,_k:oaApsMibMandatoryConfigGroupMode})