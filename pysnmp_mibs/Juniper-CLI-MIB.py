_T='juniCliConfigurationGroup'
_S='juniCliSecurityAlert'
_R='juniCliConfigurationOpStatus'
_Q='juniCliConfigurationApply'
_P='juniCliConfigurationFileName'
_O='juniCliSecurityTrapEnable'
_N='read-only'
_M='juniCliConfigurationIndex'
_L='read-write'
_K='DisplayString'
_J='juniCliSecurityTrapGroup'
_I='juniCliSecurityAlertGroup'
_H='juniCliGroup'
_G='juniCliSecurityAlertTime'
_F='juniCliSecurityAlertMessage'
_E='juniCliSecurityAlertPriority'
_D='accessible-for-notify'
_C='Integer32'
_B='current'
_A='Juniper-CLI-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
JuniLogSeverity,=mibBuilder.importSymbols('Juniper-TC','JuniLogSeverity')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_K,'PhysAddress','TextualConvention','TruthValue')
juniCliMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,30))
if mibBuilder.loadTexts:juniCliMIB.setRevisions(('2007-12-10 13:25','2002-09-16 21:44','2000-09-26 13:50','1999-12-01 00:00'))
_JuniCliTrap_ObjectIdentity=ObjectIdentity
juniCliTrap=_JuniCliTrap_ObjectIdentity((1,3,6,1,4,1,4874,2,2,30,0))
_JuniCliObjects_ObjectIdentity=ObjectIdentity
juniCliObjects=_JuniCliObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,30,1))
_JuniCliGeneral_ObjectIdentity=ObjectIdentity
juniCliGeneral=_JuniCliGeneral_ObjectIdentity((1,3,6,1,4,1,4874,2,2,30,1,1))
_JuniCliSecurityTrapEnable_Type=TruthValue
_JuniCliSecurityTrapEnable_Object=MibScalar
juniCliSecurityTrapEnable=_JuniCliSecurityTrapEnable_Object((1,3,6,1,4,1,4874,2,2,30,1,1,1),_JuniCliSecurityTrapEnable_Type())
juniCliSecurityTrapEnable.setMaxAccess(_L)
if mibBuilder.loadTexts:juniCliSecurityTrapEnable.setStatus(_B)
_JuniCliSecurity_ObjectIdentity=ObjectIdentity
juniCliSecurity=_JuniCliSecurity_ObjectIdentity((1,3,6,1,4,1,4874,2,2,30,1,2))
_JuniCliSecurityAlertPriority_Type=JuniLogSeverity
_JuniCliSecurityAlertPriority_Object=MibScalar
juniCliSecurityAlertPriority=_JuniCliSecurityAlertPriority_Object((1,3,6,1,4,1,4874,2,2,30,1,2,1),_JuniCliSecurityAlertPriority_Type())
juniCliSecurityAlertPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:juniCliSecurityAlertPriority.setStatus(_B)
_JuniCliSecurityAlertMessage_Type=DisplayString
_JuniCliSecurityAlertMessage_Object=MibScalar
juniCliSecurityAlertMessage=_JuniCliSecurityAlertMessage_Object((1,3,6,1,4,1,4874,2,2,30,1,2,2),_JuniCliSecurityAlertMessage_Type())
juniCliSecurityAlertMessage.setMaxAccess(_D)
if mibBuilder.loadTexts:juniCliSecurityAlertMessage.setStatus(_B)
_JuniCliSecurityAlertTime_Type=DateAndTime
_JuniCliSecurityAlertTime_Object=MibScalar
juniCliSecurityAlertTime=_JuniCliSecurityAlertTime_Object((1,3,6,1,4,1,4874,2,2,30,1,2,3),_JuniCliSecurityAlertTime_Type())
juniCliSecurityAlertTime.setMaxAccess(_D)
if mibBuilder.loadTexts:juniCliSecurityAlertTime.setStatus(_B)
_JuniCliConfigurationTable_Object=MibTable
juniCliConfigurationTable=_JuniCliConfigurationTable_Object((1,3,6,1,4,1,4874,2,2,30,1,3))
if mibBuilder.loadTexts:juniCliConfigurationTable.setStatus(_B)
_JuniCliConfigurationEntry_Object=MibTableRow
juniCliConfigurationEntry=_JuniCliConfigurationEntry_Object((1,3,6,1,4,1,4874,2,2,30,1,3,1))
juniCliConfigurationEntry.setIndexNames((0,_A,_M))
if mibBuilder.loadTexts:juniCliConfigurationEntry.setStatus(_B)
class _JuniCliConfigurationIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_JuniCliConfigurationIndex_Type.__name__=_C
_JuniCliConfigurationIndex_Object=MibTableColumn
juniCliConfigurationIndex=_JuniCliConfigurationIndex_Object((1,3,6,1,4,1,4874,2,2,30,1,3,1,1),_JuniCliConfigurationIndex_Type())
juniCliConfigurationIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:juniCliConfigurationIndex.setStatus(_B)
class _JuniCliConfigurationFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_JuniCliConfigurationFileName_Type.__name__=_K
_JuniCliConfigurationFileName_Object=MibTableColumn
juniCliConfigurationFileName=_JuniCliConfigurationFileName_Object((1,3,6,1,4,1,4874,2,2,30,1,3,1,2),_JuniCliConfigurationFileName_Type())
juniCliConfigurationFileName.setMaxAccess(_N)
if mibBuilder.loadTexts:juniCliConfigurationFileName.setStatus(_B)
class _JuniCliConfigurationApply_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('juniCliConfigurationReadyToApply',0),('juniCliConfigurationApplyNow',1)))
_JuniCliConfigurationApply_Type.__name__=_C
_JuniCliConfigurationApply_Object=MibTableColumn
juniCliConfigurationApply=_JuniCliConfigurationApply_Object((1,3,6,1,4,1,4874,2,2,30,1,3,1,3),_JuniCliConfigurationApply_Type())
juniCliConfigurationApply.setMaxAccess(_L)
if mibBuilder.loadTexts:juniCliConfigurationApply.setStatus(_B)
class _JuniCliConfigurationOpStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('juniCliConfigurationOpNoOp',0),('juniCliConfigurationOpSuccessful',1),('juniCliConfigurationOpInProgress',2),('juniCliConfigurationFileNotFound',3),('juniCliConfigurationFileIncompatible',4),('juniCliConfigurationOperationFailed',5)))
_JuniCliConfigurationOpStatus_Type.__name__=_C
_JuniCliConfigurationOpStatus_Object=MibTableColumn
juniCliConfigurationOpStatus=_JuniCliConfigurationOpStatus_Object((1,3,6,1,4,1,4874,2,2,30,1,3,1,4),_JuniCliConfigurationOpStatus_Type())
juniCliConfigurationOpStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:juniCliConfigurationOpStatus.setStatus(_B)
_JuniCliConformance_ObjectIdentity=ObjectIdentity
juniCliConformance=_JuniCliConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,30,2))
_JuniCliCompliances_ObjectIdentity=ObjectIdentity
juniCliCompliances=_JuniCliCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,30,2,1))
_JuniCliGroups_ObjectIdentity=ObjectIdentity
juniCliGroups=_JuniCliGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,30,2,2))
juniCliGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,30,2,2,1))
juniCliGroup.setObjects((_A,_O))
if mibBuilder.loadTexts:juniCliGroup.setStatus(_B)
juniCliSecurityAlertGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,30,2,2,2))
juniCliSecurityAlertGroup.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:juniCliSecurityAlertGroup.setStatus(_B)
juniCliConfigurationGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,30,2,2,4))
juniCliConfigurationGroup.setObjects(*((_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:juniCliConfigurationGroup.setStatus(_B)
juniCliSecurityAlert=NotificationType((1,3,6,1,4,1,4874,2,2,30,0,1))
juniCliSecurityAlert.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:juniCliSecurityAlert.setStatus(_B)
juniCliSecurityTrapGroup=NotificationGroup((1,3,6,1,4,1,4874,2,2,30,2,2,3))
juniCliSecurityTrapGroup.setObjects((_A,_S))
if mibBuilder.loadTexts:juniCliSecurityTrapGroup.setStatus(_B)
juniCliCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,30,2,1,1))
juniCliCompliance.setObjects(*((_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:juniCliCompliance.setStatus('obsolete')
juniCliCompliance2=ModuleCompliance((1,3,6,1,4,1,4874,2,2,30,2,1,2))
juniCliCompliance2.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_T)))
if mibBuilder.loadTexts:juniCliCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'juniCliMIB':juniCliMIB,'juniCliTrap':juniCliTrap,_S:juniCliSecurityAlert,'juniCliObjects':juniCliObjects,'juniCliGeneral':juniCliGeneral,_O:juniCliSecurityTrapEnable,'juniCliSecurity':juniCliSecurity,_E:juniCliSecurityAlertPriority,_F:juniCliSecurityAlertMessage,_G:juniCliSecurityAlertTime,'juniCliConfigurationTable':juniCliConfigurationTable,'juniCliConfigurationEntry':juniCliConfigurationEntry,_M:juniCliConfigurationIndex,_P:juniCliConfigurationFileName,_Q:juniCliConfigurationApply,_R:juniCliConfigurationOpStatus,'juniCliConformance':juniCliConformance,'juniCliCompliances':juniCliCompliances,'juniCliCompliance':juniCliCompliance,'juniCliCompliance2':juniCliCompliance2,'juniCliGroups':juniCliGroups,_H:juniCliGroup,_I:juniCliSecurityAlertGroup,_J:juniCliSecurityTrapGroup,_T:juniCliConfigurationGroup})