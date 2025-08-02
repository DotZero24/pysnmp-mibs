_I='oacCMGeneralGroup'
_H='oacCMHistoryStartupLastChanged'
_G='oacCMHistoryRunningLastSaved'
_F='oacCMHistoryRunningLastChanged'
_E='read-write'
_D='oacCMCopyIndex'
_C='read-only'
_B='ONEACCESS-CONFIGMGMT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
oacExpIMManagement,oacMIBModules,oacRequirements=mibBuilder.importSymbols('ONEACCESS-GLOBAL-REG','oacExpIMManagement','oacMIBModules','oacRequirements')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
oacConfigMgmtMIBModule=ModuleIdentity((1,3,6,1,4,1,13191,1,100,2001))
if mibBuilder.loadTexts:oacConfigMgmtMIBModule.setRevisions(('2011-10-27 00:00','2010-07-08 10:00'))
_OacCMConformance_ObjectIdentity=ObjectIdentity
oacCMConformance=_OacCMConformance_ObjectIdentity((1,3,6,1,4,1,13191,5,2001))
_OacCMGroups_ObjectIdentity=ObjectIdentity
oacCMGroups=_OacCMGroups_ObjectIdentity((1,3,6,1,4,1,13191,5,2001,1))
_OacCMCompliances_ObjectIdentity=ObjectIdentity
oacCMCompliances=_OacCMCompliances_ObjectIdentity((1,3,6,1,4,1,13191,5,2001,2))
_OacExpIMConfigMgmt_ObjectIdentity=ObjectIdentity
oacExpIMConfigMgmt=_OacExpIMConfigMgmt_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,6))
_OacConfigMgmtObjects_ObjectIdentity=ObjectIdentity
oacConfigMgmtObjects=_OacConfigMgmtObjects_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,6,1))
_OacCMHistory_ObjectIdentity=ObjectIdentity
oacCMHistory=_OacCMHistory_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,6,1,1))
_OacCMHistoryRunningLastChanged_Type=DateAndTime
_OacCMHistoryRunningLastChanged_Object=MibScalar
oacCMHistoryRunningLastChanged=_OacCMHistoryRunningLastChanged_Object((1,3,6,1,4,1,13191,10,3,4,6,1,1,1),_OacCMHistoryRunningLastChanged_Type())
oacCMHistoryRunningLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:oacCMHistoryRunningLastChanged.setStatus(_A)
_OacCMHistoryRunningLastSaved_Type=DateAndTime
_OacCMHistoryRunningLastSaved_Object=MibScalar
oacCMHistoryRunningLastSaved=_OacCMHistoryRunningLastSaved_Object((1,3,6,1,4,1,13191,10,3,4,6,1,1,2),_OacCMHistoryRunningLastSaved_Type())
oacCMHistoryRunningLastSaved.setMaxAccess(_C)
if mibBuilder.loadTexts:oacCMHistoryRunningLastSaved.setStatus(_A)
_OacCMHistoryStartupLastChanged_Type=DateAndTime
_OacCMHistoryStartupLastChanged_Object=MibScalar
oacCMHistoryStartupLastChanged=_OacCMHistoryStartupLastChanged_Object((1,3,6,1,4,1,13191,10,3,4,6,1,1,3),_OacCMHistoryStartupLastChanged_Type())
oacCMHistoryStartupLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:oacCMHistoryStartupLastChanged.setStatus(_A)
_OacCMCopy_ObjectIdentity=ObjectIdentity
oacCMCopy=_OacCMCopy_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,6,1,2))
_OacCMCopyIndex_Type=IpAddress
_OacCMCopyIndex_Object=MibScalar
oacCMCopyIndex=_OacCMCopyIndex_Object((1,3,6,1,4,1,13191,10,3,4,6,1,2,1),_OacCMCopyIndex_Type())
oacCMCopyIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:oacCMCopyIndex.setStatus(_A)
_OacCMCopyTftpRunTable_Object=MibTable
oacCMCopyTftpRunTable=_OacCMCopyTftpRunTable_Object((1,3,6,1,4,1,13191,10,3,4,6,1,2,2))
if mibBuilder.loadTexts:oacCMCopyTftpRunTable.setStatus(_A)
_OacCMCopyTftpRunEntry_Object=MibTableRow
oacCMCopyTftpRunEntry=_OacCMCopyTftpRunEntry_Object((1,3,6,1,4,1,13191,10,3,4,6,1,2,2,1))
oacCMCopyTftpRunEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:oacCMCopyTftpRunEntry.setStatus(_A)
_OacCMCopyTftpRun_Type=DisplayString
_OacCMCopyTftpRun_Object=MibTableColumn
oacCMCopyTftpRun=_OacCMCopyTftpRun_Object((1,3,6,1,4,1,13191,10,3,4,6,1,2,2,1,1),_OacCMCopyTftpRun_Type())
oacCMCopyTftpRun.setMaxAccess(_E)
if mibBuilder.loadTexts:oacCMCopyTftpRun.setStatus(_A)
_OacCMCopyRunTftpTable_Object=MibTable
oacCMCopyRunTftpTable=_OacCMCopyRunTftpTable_Object((1,3,6,1,4,1,13191,10,3,4,6,1,2,3))
if mibBuilder.loadTexts:oacCMCopyRunTftpTable.setStatus(_A)
_OacCMCopyRunTftpEntry_Object=MibTableRow
oacCMCopyRunTftpEntry=_OacCMCopyRunTftpEntry_Object((1,3,6,1,4,1,13191,10,3,4,6,1,2,3,1))
oacCMCopyRunTftpEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:oacCMCopyRunTftpEntry.setStatus(_A)
_OacCMCopyRunTftp_Type=DisplayString
_OacCMCopyRunTftp_Object=MibTableColumn
oacCMCopyRunTftp=_OacCMCopyRunTftp_Object((1,3,6,1,4,1,13191,10,3,4,6,1,2,3,1,1),_OacCMCopyRunTftp_Type())
oacCMCopyRunTftp.setMaxAccess(_E)
if mibBuilder.loadTexts:oacCMCopyRunTftp.setStatus(_A)
_OacConfigMgmtNotifications_ObjectIdentity=ObjectIdentity
oacConfigMgmtNotifications=_OacConfigMgmtNotifications_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,6,1,3))
oacCMGeneralGroup=ObjectGroup((1,3,6,1,4,1,13191,5,2001,1,1))
oacCMGeneralGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:oacCMGeneralGroup.setStatus(_A)
oacCMRunningConfigSaved=NotificationType((1,3,6,1,4,1,13191,10,3,4,6,1,3,1))
if mibBuilder.loadTexts:oacCMRunningConfigSaved.setStatus(_A)
oacCMCompliance=ModuleCompliance((1,3,6,1,4,1,13191,5,2001,2,1))
oacCMCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:oacCMCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'oacConfigMgmtMIBModule':oacConfigMgmtMIBModule,'oacCMConformance':oacCMConformance,'oacCMGroups':oacCMGroups,_I:oacCMGeneralGroup,'oacCMCompliances':oacCMCompliances,'oacCMCompliance':oacCMCompliance,'oacExpIMConfigMgmt':oacExpIMConfigMgmt,'oacConfigMgmtObjects':oacConfigMgmtObjects,'oacCMHistory':oacCMHistory,_F:oacCMHistoryRunningLastChanged,_G:oacCMHistoryRunningLastSaved,_H:oacCMHistoryStartupLastChanged,'oacCMCopy':oacCMCopy,_D:oacCMCopyIndex,'oacCMCopyTftpRunTable':oacCMCopyTftpRunTable,'oacCMCopyTftpRunEntry':oacCMCopyTftpRunEntry,'oacCMCopyTftpRun':oacCMCopyTftpRun,'oacCMCopyRunTftpTable':oacCMCopyRunTftpTable,'oacCMCopyRunTftpEntry':oacCMCopyRunTftpEntry,'oacCMCopyRunTftp':oacCMCopyRunTftp,'oacConfigMgmtNotifications':oacConfigMgmtNotifications,'oacCMRunningConfigSaved':oacCMRunningConfigSaved})