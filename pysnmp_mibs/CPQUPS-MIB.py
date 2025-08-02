_Q='cpqUpsMemberIndex'
_P='cpqUpsOsCommonModuleIndex'
_O='failed'
_N='NotificationType'
_M='cpqUpsAlarm'
_L='cpqUpsEstimatedBatteryLife'
_K='OctetString'
_J='CPQUPS-MIB'
_I='read-write'
_H='Integer32'
_G='DisplayString'
_F='sysName'
_E='SNMPv2-MIB'
_D='cpqHoTrapFlags'
_C='CPQHOST-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
compaq,cpqHoTrapFlags=mibBuilder.importSymbols(_C,'compaq',_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_E,_F)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier',_N,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_N,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
_CpqUps_ObjectIdentity=ObjectIdentity
cpqUps=_CpqUps_ObjectIdentity((1,3,6,1,4,1,232,12))
_CpqUpsMibRev_ObjectIdentity=ObjectIdentity
cpqUpsMibRev=_CpqUpsMibRev_ObjectIdentity((1,3,6,1,4,1,232,12,1))
class _CpqUpsMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpqUpsMibRevMajor_Type.__name__=_H
_CpqUpsMibRevMajor_Object=MibScalar
cpqUpsMibRevMajor=_CpqUpsMibRevMajor_Object((1,3,6,1,4,1,232,12,1,1),_CpqUpsMibRevMajor_Type())
cpqUpsMibRevMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqUpsMibRevMajor.setStatus(_A)
class _CpqUpsMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqUpsMibRevMinor_Type.__name__=_H
_CpqUpsMibRevMinor_Object=MibScalar
cpqUpsMibRevMinor=_CpqUpsMibRevMinor_Object((1,3,6,1,4,1,232,12,1,2),_CpqUpsMibRevMinor_Type())
cpqUpsMibRevMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqUpsMibRevMinor.setStatus(_A)
class _CpqUpsMibCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('ok',2),('degraded',3),(_O,4)))
_CpqUpsMibCondition_Type.__name__=_H
_CpqUpsMibCondition_Object=MibScalar
cpqUpsMibCondition=_CpqUpsMibCondition_Object((1,3,6,1,4,1,232,12,1,3),_CpqUpsMibCondition_Type())
cpqUpsMibCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqUpsMibCondition.setStatus(_A)
_CpqUpsComponent_ObjectIdentity=ObjectIdentity
cpqUpsComponent=_CpqUpsComponent_ObjectIdentity((1,3,6,1,4,1,232,12,2))
_CpqUpsInterface_ObjectIdentity=ObjectIdentity
cpqUpsInterface=_CpqUpsInterface_ObjectIdentity((1,3,6,1,4,1,232,12,2,1))
_CpqUpsOsCommon_ObjectIdentity=ObjectIdentity
cpqUpsOsCommon=_CpqUpsOsCommon_ObjectIdentity((1,3,6,1,4,1,232,12,2,1,4))
class _CpqUpsOsCommonPollFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqUpsOsCommonPollFreq_Type.__name__=_H
_CpqUpsOsCommonPollFreq_Object=MibScalar
cpqUpsOsCommonPollFreq=_CpqUpsOsCommonPollFreq_Object((1,3,6,1,4,1,232,12,2,1,4,1),_CpqUpsOsCommonPollFreq_Type())
cpqUpsOsCommonPollFreq.setMaxAccess(_I)
if mibBuilder.loadTexts:cpqUpsOsCommonPollFreq.setStatus(_A)
_CpqUpsOsCommonModuleTable_Object=MibTable
cpqUpsOsCommonModuleTable=_CpqUpsOsCommonModuleTable_Object((1,3,6,1,4,1,232,12,2,1,4,2))
if mibBuilder.loadTexts:cpqUpsOsCommonModuleTable.setStatus(_A)
_CpqUpsOsCommonModuleEntry_Object=MibTableRow
cpqUpsOsCommonModuleEntry=_CpqUpsOsCommonModuleEntry_Object((1,3,6,1,4,1,232,12,2,1,4,2,1))
cpqUpsOsCommonModuleEntry.setIndexNames((0,_J,_P))
if mibBuilder.loadTexts:cpqUpsOsCommonModuleEntry.setStatus(_A)
class _CpqUpsOsCommonModuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqUpsOsCommonModuleIndex_Type.__name__=_H
_CpqUpsOsCommonModuleIndex_Object=MibTableColumn
cpqUpsOsCommonModuleIndex=_CpqUpsOsCommonModuleIndex_Object((1,3,6,1,4,1,232,12,2,1,4,2,1,1),_CpqUpsOsCommonModuleIndex_Type())
cpqUpsOsCommonModuleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqUpsOsCommonModuleIndex.setStatus(_A)
class _CpqUpsOsCommonModuleName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqUpsOsCommonModuleName_Type.__name__=_G
_CpqUpsOsCommonModuleName_Object=MibTableColumn
cpqUpsOsCommonModuleName=_CpqUpsOsCommonModuleName_Object((1,3,6,1,4,1,232,12,2,1,4,2,1,2),_CpqUpsOsCommonModuleName_Type())
cpqUpsOsCommonModuleName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqUpsOsCommonModuleName.setStatus(_A)
class _CpqUpsOsCommonModuleVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_CpqUpsOsCommonModuleVersion_Type.__name__=_G
_CpqUpsOsCommonModuleVersion_Object=MibTableColumn
cpqUpsOsCommonModuleVersion=_CpqUpsOsCommonModuleVersion_Object((1,3,6,1,4,1,232,12,2,1,4,2,1,3),_CpqUpsOsCommonModuleVersion_Type())
cpqUpsOsCommonModuleVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqUpsOsCommonModuleVersion.setStatus(_A)
class _CpqUpsOsCommonModuleDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_CpqUpsOsCommonModuleDate_Type.__name__=_K
_CpqUpsOsCommonModuleDate_Object=MibTableColumn
cpqUpsOsCommonModuleDate=_CpqUpsOsCommonModuleDate_Object((1,3,6,1,4,1,232,12,2,1,4,2,1,4),_CpqUpsOsCommonModuleDate_Type())
cpqUpsOsCommonModuleDate.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqUpsOsCommonModuleDate.setStatus(_A)
class _CpqUpsOsCommonModulePurpose_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqUpsOsCommonModulePurpose_Type.__name__=_G
_CpqUpsOsCommonModulePurpose_Object=MibTableColumn
cpqUpsOsCommonModulePurpose=_CpqUpsOsCommonModulePurpose_Object((1,3,6,1,4,1,232,12,2,1,4,2,1,5),_CpqUpsOsCommonModulePurpose_Type())
cpqUpsOsCommonModulePurpose.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqUpsOsCommonModulePurpose.setStatus(_A)
_CpqUpsBasic_ObjectIdentity=ObjectIdentity
cpqUpsBasic=_CpqUpsBasic_ObjectIdentity((1,3,6,1,4,1,232,12,2,2))
class _CpqUpsLineStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4)));namedValues=NamedValues(*(('other',1),('ok',2),(_O,4)))
_CpqUpsLineStatus_Type.__name__=_H
_CpqUpsLineStatus_Object=MibScalar
cpqUpsLineStatus=_CpqUpsLineStatus_Object((1,3,6,1,4,1,232,12,2,2,1),_CpqUpsLineStatus_Type())
cpqUpsLineStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqUpsLineStatus.setStatus(_A)
class _CpqUpsName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_CpqUpsName_Type.__name__=_G
_CpqUpsName_Object=MibScalar
cpqUpsName=_CpqUpsName_Object((1,3,6,1,4,1,232,12,2,2,2),_CpqUpsName_Type())
cpqUpsName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqUpsName.setStatus(_A)
_CpqUpsEstimatedBatteryLife_Type=Integer32
_CpqUpsEstimatedBatteryLife_Object=MibScalar
cpqUpsEstimatedBatteryLife=_CpqUpsEstimatedBatteryLife_Object((1,3,6,1,4,1,232,12,2,2,3),_CpqUpsEstimatedBatteryLife_Type())
cpqUpsEstimatedBatteryLife.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqUpsEstimatedBatteryLife.setStatus(_A)
_CpqUpsAutoShutdownDelay_Type=Integer32
_CpqUpsAutoShutdownDelay_Object=MibScalar
cpqUpsAutoShutdownDelay=_CpqUpsAutoShutdownDelay_Object((1,3,6,1,4,1,232,12,2,2,4),_CpqUpsAutoShutdownDelay_Type())
cpqUpsAutoShutdownDelay.setMaxAccess(_I)
if mibBuilder.loadTexts:cpqUpsAutoShutdownDelay.setStatus(_A)
class _CpqUpsLaunchCommand_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,250))
_CpqUpsLaunchCommand_Type.__name__=_K
_CpqUpsLaunchCommand_Object=MibScalar
cpqUpsLaunchCommand=_CpqUpsLaunchCommand_Object((1,3,6,1,4,1,232,12,2,2,5),_CpqUpsLaunchCommand_Type())
cpqUpsLaunchCommand.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqUpsLaunchCommand.setStatus(_A)
class _CpqUpsAlarm_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,250))
_CpqUpsAlarm_Type.__name__=_G
_CpqUpsAlarm_Object=MibScalar
cpqUpsAlarm=_CpqUpsAlarm_Object((1,3,6,1,4,1,232,12,2,2,6),_CpqUpsAlarm_Type())
cpqUpsAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqUpsAlarm.setStatus(_A)
_CpqUpsFamily_ObjectIdentity=ObjectIdentity
cpqUpsFamily=_CpqUpsFamily_ObjectIdentity((1,3,6,1,4,1,232,12,2,3))
_CpqUpsMemberTable_Object=MibTable
cpqUpsMemberTable=_CpqUpsMemberTable_Object((1,3,6,1,4,1,232,12,2,3,1))
if mibBuilder.loadTexts:cpqUpsMemberTable.setStatus(_A)
_CpqUpsMemberEntry_Object=MibTableRow
cpqUpsMemberEntry=_CpqUpsMemberEntry_Object((1,3,6,1,4,1,232,12,2,3,1,1))
cpqUpsMemberEntry.setIndexNames((0,_J,_Q))
if mibBuilder.loadTexts:cpqUpsMemberEntry.setStatus(_A)
class _CpqUpsMemberIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CpqUpsMemberIndex_Type.__name__=_H
_CpqUpsMemberIndex_Object=MibTableColumn
cpqUpsMemberIndex=_CpqUpsMemberIndex_Object((1,3,6,1,4,1,232,12,2,3,1,1,1),_CpqUpsMemberIndex_Type())
cpqUpsMemberIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:cpqUpsMemberIndex.setStatus(_A)
class _CpqUpsMemberName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqUpsMemberName_Type.__name__=_G
_CpqUpsMemberName_Object=MibTableColumn
cpqUpsMemberName=_CpqUpsMemberName_Object((1,3,6,1,4,1,232,12,2,3,1,1,2),_CpqUpsMemberName_Type())
cpqUpsMemberName.setMaxAccess(_I)
if mibBuilder.loadTexts:cpqUpsMemberName.setStatus(_A)
class _CpqUpsMemberCommunityStr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqUpsMemberCommunityStr_Type.__name__=_G
_CpqUpsMemberCommunityStr_Object=MibTableColumn
cpqUpsMemberCommunityStr=_CpqUpsMemberCommunityStr_Object((1,3,6,1,4,1,232,12,2,3,1,1,3),_CpqUpsMemberCommunityStr_Type())
cpqUpsMemberCommunityStr.setMaxAccess(_I)
if mibBuilder.loadTexts:cpqUpsMemberCommunityStr.setStatus(_A)
class _CpqUpsAddMemberName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqUpsAddMemberName_Type.__name__=_G
_CpqUpsAddMemberName_Object=MibScalar
cpqUpsAddMemberName=_CpqUpsAddMemberName_Object((1,3,6,1,4,1,232,12,2,3,2),_CpqUpsAddMemberName_Type())
cpqUpsAddMemberName.setMaxAccess(_I)
if mibBuilder.loadTexts:cpqUpsAddMemberName.setStatus(_A)
class _CpqUpsAddMemberCommunityStr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqUpsAddMemberCommunityStr_Type.__name__=_G
_CpqUpsAddMemberCommunityStr_Object=MibScalar
cpqUpsAddMemberCommunityStr=_CpqUpsAddMemberCommunityStr_Object((1,3,6,1,4,1,232,12,2,3,3),_CpqUpsAddMemberCommunityStr_Type())
cpqUpsAddMemberCommunityStr.setMaxAccess(_I)
if mibBuilder.loadTexts:cpqUpsAddMemberCommunityStr.setStatus(_A)
cpqUpsLineFailed=NotificationType((1,3,6,1,4,1,232,0,12001))
cpqUpsLineFailed.setObjects((_J,_L))
if mibBuilder.loadTexts:cpqUpsLineFailed.setStatus('')
cpqUpsLineOk=NotificationType((1,3,6,1,4,1,232,0,12002))
if mibBuilder.loadTexts:cpqUpsLineOk.setStatus('')
cpqUpsShutdown=NotificationType((1,3,6,1,4,1,232,0,12003))
if mibBuilder.loadTexts:cpqUpsShutdown.setStatus('')
cpqUpsConfirmation=NotificationType((1,3,6,1,4,1,232,0,12004))
if mibBuilder.loadTexts:cpqUpsConfirmation.setStatus('')
cpqUpsBatteryLow=NotificationType((1,3,6,1,4,1,232,0,12005))
if mibBuilder.loadTexts:cpqUpsBatteryLow.setStatus('')
cpqUps2LineFailed=NotificationType((1,3,6,1,4,1,232,0,12006))
cpqUps2LineFailed.setObjects(*((_E,_F),(_C,_D),(_J,_L)))
if mibBuilder.loadTexts:cpqUps2LineFailed.setStatus('')
cpqUps2LineOk=NotificationType((1,3,6,1,4,1,232,0,12007))
cpqUps2LineOk.setObjects(*((_E,_F),(_C,_D)))
if mibBuilder.loadTexts:cpqUps2LineOk.setStatus('')
cpqUps2Shutdown=NotificationType((1,3,6,1,4,1,232,0,12008))
cpqUps2Shutdown.setObjects(*((_E,_F),(_C,_D)))
if mibBuilder.loadTexts:cpqUps2Shutdown.setStatus('')
cpqUps2Confirmation=NotificationType((1,3,6,1,4,1,232,0,12009))
cpqUps2Confirmation.setObjects(*((_E,_F),(_C,_D)))
if mibBuilder.loadTexts:cpqUps2Confirmation.setStatus('')
cpqUps2BatteryLow=NotificationType((1,3,6,1,4,1,232,0,12010))
cpqUps2BatteryLow.setObjects(*((_E,_F),(_C,_D)))
if mibBuilder.loadTexts:cpqUps2BatteryLow.setStatus('')
cpqUpsOverload=NotificationType((1,3,6,1,4,1,232,0,12011))
cpqUpsOverload.setObjects(*((_E,_F),(_C,_D)))
if mibBuilder.loadTexts:cpqUpsOverload.setStatus('')
cpqUpsPendingBatteryFailure=NotificationType((1,3,6,1,4,1,232,0,12012))
cpqUpsPendingBatteryFailure.setObjects(*((_E,_F),(_C,_D)))
if mibBuilder.loadTexts:cpqUpsPendingBatteryFailure.setStatus('')
cpqUpsGenericCritical=NotificationType((1,3,6,1,4,1,232,0,12013))
cpqUpsGenericCritical.setObjects(*((_E,_F),(_C,_D),(_J,_M)))
if mibBuilder.loadTexts:cpqUpsGenericCritical.setStatus('')
cpqUpsGenericInfo=NotificationType((1,3,6,1,4,1,232,0,12014))
cpqUpsGenericInfo.setObjects(*((_E,_F),(_C,_D),(_J,_M)))
if mibBuilder.loadTexts:cpqUpsGenericInfo.setStatus('')
mibBuilder.exportSymbols(_J,**{'cpqUpsLineFailed':cpqUpsLineFailed,'cpqUpsLineOk':cpqUpsLineOk,'cpqUpsShutdown':cpqUpsShutdown,'cpqUpsConfirmation':cpqUpsConfirmation,'cpqUpsBatteryLow':cpqUpsBatteryLow,'cpqUps2LineFailed':cpqUps2LineFailed,'cpqUps2LineOk':cpqUps2LineOk,'cpqUps2Shutdown':cpqUps2Shutdown,'cpqUps2Confirmation':cpqUps2Confirmation,'cpqUps2BatteryLow':cpqUps2BatteryLow,'cpqUpsOverload':cpqUpsOverload,'cpqUpsPendingBatteryFailure':cpqUpsPendingBatteryFailure,'cpqUpsGenericCritical':cpqUpsGenericCritical,'cpqUpsGenericInfo':cpqUpsGenericInfo,'cpqUps':cpqUps,'cpqUpsMibRev':cpqUpsMibRev,'cpqUpsMibRevMajor':cpqUpsMibRevMajor,'cpqUpsMibRevMinor':cpqUpsMibRevMinor,'cpqUpsMibCondition':cpqUpsMibCondition,'cpqUpsComponent':cpqUpsComponent,'cpqUpsInterface':cpqUpsInterface,'cpqUpsOsCommon':cpqUpsOsCommon,'cpqUpsOsCommonPollFreq':cpqUpsOsCommonPollFreq,'cpqUpsOsCommonModuleTable':cpqUpsOsCommonModuleTable,'cpqUpsOsCommonModuleEntry':cpqUpsOsCommonModuleEntry,_P:cpqUpsOsCommonModuleIndex,'cpqUpsOsCommonModuleName':cpqUpsOsCommonModuleName,'cpqUpsOsCommonModuleVersion':cpqUpsOsCommonModuleVersion,'cpqUpsOsCommonModuleDate':cpqUpsOsCommonModuleDate,'cpqUpsOsCommonModulePurpose':cpqUpsOsCommonModulePurpose,'cpqUpsBasic':cpqUpsBasic,'cpqUpsLineStatus':cpqUpsLineStatus,'cpqUpsName':cpqUpsName,_L:cpqUpsEstimatedBatteryLife,'cpqUpsAutoShutdownDelay':cpqUpsAutoShutdownDelay,'cpqUpsLaunchCommand':cpqUpsLaunchCommand,_M:cpqUpsAlarm,'cpqUpsFamily':cpqUpsFamily,'cpqUpsMemberTable':cpqUpsMemberTable,'cpqUpsMemberEntry':cpqUpsMemberEntry,_Q:cpqUpsMemberIndex,'cpqUpsMemberName':cpqUpsMemberName,'cpqUpsMemberCommunityStr':cpqUpsMemberCommunityStr,'cpqUpsAddMemberName':cpqUpsAddMemberName,'cpqUpsAddMemberCommunityStr':cpqUpsAddMemberCommunityStr})