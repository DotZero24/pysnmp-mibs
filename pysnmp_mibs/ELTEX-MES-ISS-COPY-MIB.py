_I='eltMesBackupHistoryIndex'
_H='ELTEX-MES-ISS-COPY-MIB'
_G='EltMesBackupUserStatus'
_F='Unsigned32'
_E='Integer32'
_D='TruthValue'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMesIss,=mibBuilder.importSymbols('ELTEX-MES-ISS-MIB','eltMesIss')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_D)
eltMesIssCopyMIB=ModuleIdentity((1,3,6,1,4,1,35265,1,139,15))
if mibBuilder.loadTexts:eltMesIssCopyMIB.setRevisions(('2019-05-02 00:00',))
class EltMesCopyLocationType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tftp',1),('sftp',2)))
class EltMesBackupUserStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('starting',1),('stopped',2)))
class EltMesCopyError(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('no-error',1),('send-failed',2),('save-failed',3)))
_EltMesIssCopyObjects_ObjectIdentity=ObjectIdentity
eltMesIssCopyObjects=_EltMesIssCopyObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,139,15,1))
_EltMesIssCopyBackup_ObjectIdentity=ObjectIdentity
eltMesIssCopyBackup=_EltMesIssCopyBackup_ObjectIdentity((1,3,6,1,4,1,35265,1,139,15,1,1))
_EltMesIssBackupConfigs_ObjectIdentity=ObjectIdentity
eltMesIssBackupConfigs=_EltMesIssBackupConfigs_ObjectIdentity((1,3,6,1,4,1,35265,1,139,15,1,1,1))
class _EltMesBackupAutoEnable_Type(TruthValue):defaultValue=2
_EltMesBackupAutoEnable_Type.__name__=_D
_EltMesBackupAutoEnable_Object=MibScalar
eltMesBackupAutoEnable=_EltMesBackupAutoEnable_Object((1,3,6,1,4,1,35265,1,139,15,1,1,1,1),_EltMesBackupAutoEnable_Type())
eltMesBackupAutoEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesBackupAutoEnable.setStatus(_A)
class _EltMesBackupAutoTimeout_Type(Unsigned32):defaultValue=720
_EltMesBackupAutoTimeout_Type.__name__=_F
_EltMesBackupAutoTimeout_Object=MibScalar
eltMesBackupAutoTimeout=_EltMesBackupAutoTimeout_Object((1,3,6,1,4,1,35265,1,139,15,1,1,1,2),_EltMesBackupAutoTimeout_Type())
eltMesBackupAutoTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesBackupAutoTimeout.setStatus(_A)
_EltMesBackupAutoFilePath_Type=DisplayString
_EltMesBackupAutoFilePath_Object=MibScalar
eltMesBackupAutoFilePath=_EltMesBackupAutoFilePath_Object((1,3,6,1,4,1,35265,1,139,15,1,1,1,3),_EltMesBackupAutoFilePath_Type())
eltMesBackupAutoFilePath.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesBackupAutoFilePath.setStatus(_A)
_EltMesBackupAutoServerAddress_Type=DisplayString
_EltMesBackupAutoServerAddress_Object=MibScalar
eltMesBackupAutoServerAddress=_EltMesBackupAutoServerAddress_Object((1,3,6,1,4,1,35265,1,139,15,1,1,1,4),_EltMesBackupAutoServerAddress_Type())
eltMesBackupAutoServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesBackupAutoServerAddress.setStatus(_A)
class _EltMesBackupAutoOnWrite_Type(TruthValue):defaultValue=2
_EltMesBackupAutoOnWrite_Type.__name__=_D
_EltMesBackupAutoOnWrite_Object=MibScalar
eltMesBackupAutoOnWrite=_EltMesBackupAutoOnWrite_Object((1,3,6,1,4,1,35265,1,139,15,1,1,1,5),_EltMesBackupAutoOnWrite_Type())
eltMesBackupAutoOnWrite.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesBackupAutoOnWrite.setStatus(_A)
class _EltMesBackupUserStartAction_Type(EltMesBackupUserStatus):defaultValue=2
_EltMesBackupUserStartAction_Type.__name__=_G
_EltMesBackupUserStartAction_Object=MibScalar
eltMesBackupUserStartAction=_EltMesBackupUserStartAction_Object((1,3,6,1,4,1,35265,1,139,15,1,1,1,6),_EltMesBackupUserStartAction_Type())
eltMesBackupUserStartAction.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesBackupUserStartAction.setStatus(_A)
class _EltMesBackupHistoryEnable_Type(TruthValue):defaultValue=2
_EltMesBackupHistoryEnable_Type.__name__=_D
_EltMesBackupHistoryEnable_Object=MibScalar
eltMesBackupHistoryEnable=_EltMesBackupHistoryEnable_Object((1,3,6,1,4,1,35265,1,139,15,1,1,1,7),_EltMesBackupHistoryEnable_Type())
eltMesBackupHistoryEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesBackupHistoryEnable.setStatus(_A)
class _EltMesBackupClearAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noAction',1),('clearNow',2)))
_EltMesBackupClearAction_Type.__name__=_E
_EltMesBackupClearAction_Object=MibScalar
eltMesBackupClearAction=_EltMesBackupClearAction_Object((1,3,6,1,4,1,35265,1,139,15,1,1,1,8),_EltMesBackupClearAction_Type())
eltMesBackupClearAction.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesBackupClearAction.setStatus(_A)
_EltMesIssBackupStatistics_ObjectIdentity=ObjectIdentity
eltMesIssBackupStatistics=_EltMesIssBackupStatistics_ObjectIdentity((1,3,6,1,4,1,35265,1,139,15,1,1,2))
_EltMesBackupHistoryTable_Object=MibTable
eltMesBackupHistoryTable=_EltMesBackupHistoryTable_Object((1,3,6,1,4,1,35265,1,139,15,1,1,2,1))
if mibBuilder.loadTexts:eltMesBackupHistoryTable.setStatus(_A)
_EltMesBackupHistoryEntry_Object=MibTableRow
eltMesBackupHistoryEntry=_EltMesBackupHistoryEntry_Object((1,3,6,1,4,1,35265,1,139,15,1,1,2,1,1))
eltMesBackupHistoryEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:eltMesBackupHistoryEntry.setStatus(_A)
_EltMesBackupHistoryIndex_Type=Integer32
_EltMesBackupHistoryIndex_Object=MibTableColumn
eltMesBackupHistoryIndex=_EltMesBackupHistoryIndex_Object((1,3,6,1,4,1,35265,1,139,15,1,1,2,1,1,1),_EltMesBackupHistoryIndex_Type())
eltMesBackupHistoryIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:eltMesBackupHistoryIndex.setStatus(_A)
_EltMesBackupHistoryDateTime_Type=DisplayString
_EltMesBackupHistoryDateTime_Object=MibTableColumn
eltMesBackupHistoryDateTime=_EltMesBackupHistoryDateTime_Object((1,3,6,1,4,1,35265,1,139,15,1,1,2,1,1,2),_EltMesBackupHistoryDateTime_Type())
eltMesBackupHistoryDateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMesBackupHistoryDateTime.setStatus(_A)
_EltMesBackupHistoryDstLocationType_Type=EltMesCopyLocationType
_EltMesBackupHistoryDstLocationType_Object=MibTableColumn
eltMesBackupHistoryDstLocationType=_EltMesBackupHistoryDstLocationType_Object((1,3,6,1,4,1,35265,1,139,15,1,1,2,1,1,3),_EltMesBackupHistoryDstLocationType_Type())
eltMesBackupHistoryDstLocationType.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMesBackupHistoryDstLocationType.setStatus(_A)
_EltMesBackupHistoryServerAddr_Type=DisplayString
_EltMesBackupHistoryServerAddr_Object=MibTableColumn
eltMesBackupHistoryServerAddr=_EltMesBackupHistoryServerAddr_Object((1,3,6,1,4,1,35265,1,139,15,1,1,2,1,1,4),_EltMesBackupHistoryServerAddr_Type())
eltMesBackupHistoryServerAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMesBackupHistoryServerAddr.setStatus(_A)
_EltMesBackupHistoryFilePath_Type=DisplayString
_EltMesBackupHistoryFilePath_Object=MibTableColumn
eltMesBackupHistoryFilePath=_EltMesBackupHistoryFilePath_Object((1,3,6,1,4,1,35265,1,139,15,1,1,2,1,1,5),_EltMesBackupHistoryFilePath_Type())
eltMesBackupHistoryFilePath.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMesBackupHistoryFilePath.setStatus(_A)
_EltMesIssCopyGlobal_ObjectIdentity=ObjectIdentity
eltMesIssCopyGlobal=_EltMesIssCopyGlobal_ObjectIdentity((1,3,6,1,4,1,35265,1,139,15,1,2))
_EltMesLastCopyError_Type=EltMesCopyError
_EltMesLastCopyError_Object=MibScalar
eltMesLastCopyError=_EltMesLastCopyError_Object((1,3,6,1,4,1,35265,1,139,15,1,2,1),_EltMesLastCopyError_Type())
eltMesLastCopyError.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMesLastCopyError.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'EltMesCopyLocationType':EltMesCopyLocationType,_G:EltMesBackupUserStatus,'EltMesCopyError':EltMesCopyError,'eltMesIssCopyMIB':eltMesIssCopyMIB,'eltMesIssCopyObjects':eltMesIssCopyObjects,'eltMesIssCopyBackup':eltMesIssCopyBackup,'eltMesIssBackupConfigs':eltMesIssBackupConfigs,'eltMesBackupAutoEnable':eltMesBackupAutoEnable,'eltMesBackupAutoTimeout':eltMesBackupAutoTimeout,'eltMesBackupAutoFilePath':eltMesBackupAutoFilePath,'eltMesBackupAutoServerAddress':eltMesBackupAutoServerAddress,'eltMesBackupAutoOnWrite':eltMesBackupAutoOnWrite,'eltMesBackupUserStartAction':eltMesBackupUserStartAction,'eltMesBackupHistoryEnable':eltMesBackupHistoryEnable,'eltMesBackupClearAction':eltMesBackupClearAction,'eltMesIssBackupStatistics':eltMesIssBackupStatistics,'eltMesBackupHistoryTable':eltMesBackupHistoryTable,'eltMesBackupHistoryEntry':eltMesBackupHistoryEntry,_I:eltMesBackupHistoryIndex,'eltMesBackupHistoryDateTime':eltMesBackupHistoryDateTime,'eltMesBackupHistoryDstLocationType':eltMesBackupHistoryDstLocationType,'eltMesBackupHistoryServerAddr':eltMesBackupHistoryServerAddr,'eltMesBackupHistoryFilePath':eltMesBackupHistoryFilePath,'eltMesIssCopyGlobal':eltMesIssCopyGlobal,'eltMesLastCopyError':eltMesLastCopyError})