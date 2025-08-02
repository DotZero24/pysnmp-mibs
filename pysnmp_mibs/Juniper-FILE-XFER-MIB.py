_Z='juniFileXferGroup2'
_Y='juniFileXferGroup1'
_X='juniFileXferTrap'
_W='juniFileXferRouterName'
_V='juniFileXferRemoteUserPassword'
_U='juniFileXferRemoteUserName'
_T='anonymous'
_S='OctetString'
_R='juniFileXferTrapGroup'
_Q='juniFileXferTrapEnabled'
_P='juniFileXferRowStatus'
_O='juniFileXferProtocol'
_N='juniFileXferLocalFileName'
_M='juniFileXferRemoteFileName'
_L='juniFileXferFileType'
_K='juniFileXferDirection'
_J='read-only'
_I='juniFileXferTimeStamp'
_H='juniFileXferStatus'
_G='obsolete'
_F='juniFileXferIndex'
_E='DisplayString'
_D='Integer32'
_C='read-write'
_B='current'
_A='Juniper-FILE-XFER-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_S,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
JuniName,=mibBuilder.importSymbols('Juniper-TC','JuniName')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention')
juniFileXferMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,23))
if mibBuilder.loadTexts:juniFileXferMIB.setRevisions(('2002-09-16 21:44','2001-03-28 13:46','2000-05-01 00:00','1999-08-18 00:00'))
_JuniFileXferObjects_ObjectIdentity=ObjectIdentity
juniFileXferObjects=_JuniFileXferObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,23,1))
_JuniFileXferTable_Object=MibTable
juniFileXferTable=_JuniFileXferTable_Object((1,3,6,1,4,1,4874,2,2,23,1,1))
if mibBuilder.loadTexts:juniFileXferTable.setStatus(_B)
_JuniFileXferTableEntry_Object=MibTableRow
juniFileXferTableEntry=_JuniFileXferTableEntry_Object((1,3,6,1,4,1,4874,2,2,23,1,1,1))
juniFileXferTableEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:juniFileXferTableEntry.setStatus(_B)
class _JuniFileXferIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_JuniFileXferIndex_Type.__name__=_D
_JuniFileXferIndex_Object=MibTableColumn
juniFileXferIndex=_JuniFileXferIndex_Object((1,3,6,1,4,1,4874,2,2,23,1,1,1,1),_JuniFileXferIndex_Type())
juniFileXferIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:juniFileXferIndex.setStatus(_B)
class _JuniFileXferDirection_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('juniFileXferLocalToRemote',1),('juniFileXferRemoteToLocal',2)))
_JuniFileXferDirection_Type.__name__=_D
_JuniFileXferDirection_Object=MibTableColumn
juniFileXferDirection=_JuniFileXferDirection_Object((1,3,6,1,4,1,4874,2,2,23,1,1,1,2),_JuniFileXferDirection_Type())
juniFileXferDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFileXferDirection.setStatus(_B)
class _JuniFileXferFileType_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('juniFileXferSoftwareRelease',1),('juniFileXferSystemConfig',2),('juniFileXferRunningConfig',3),('juniFileXferSystemLog',4),('juniFileXferScript',5),('juniFileXferRebootHistory',6),('juniFileXferBulkStatistics',7)))
_JuniFileXferFileType_Type.__name__=_D
_JuniFileXferFileType_Object=MibTableColumn
juniFileXferFileType=_JuniFileXferFileType_Object((1,3,6,1,4,1,4874,2,2,23,1,1,1,3),_JuniFileXferFileType_Type())
juniFileXferFileType.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFileXferFileType.setStatus(_B)
class _JuniFileXferRemoteFileName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_JuniFileXferRemoteFileName_Type.__name__=_E
_JuniFileXferRemoteFileName_Object=MibTableColumn
juniFileXferRemoteFileName=_JuniFileXferRemoteFileName_Object((1,3,6,1,4,1,4874,2,2,23,1,1,1,4),_JuniFileXferRemoteFileName_Type())
juniFileXferRemoteFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFileXferRemoteFileName.setStatus(_B)
class _JuniFileXferRemoteUserName_Type(DisplayString):defaultValue=OctetString(_T);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_JuniFileXferRemoteUserName_Type.__name__=_E
_JuniFileXferRemoteUserName_Object=MibTableColumn
juniFileXferRemoteUserName=_JuniFileXferRemoteUserName_Object((1,3,6,1,4,1,4874,2,2,23,1,1,1,5),_JuniFileXferRemoteUserName_Type())
juniFileXferRemoteUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFileXferRemoteUserName.setStatus(_G)
class _JuniFileXferRemoteUserPassword_Type(OctetString):defaultValue=OctetString(_T);subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_JuniFileXferRemoteUserPassword_Type.__name__=_S
_JuniFileXferRemoteUserPassword_Object=MibTableColumn
juniFileXferRemoteUserPassword=_JuniFileXferRemoteUserPassword_Object((1,3,6,1,4,1,4874,2,2,23,1,1,1,6),_JuniFileXferRemoteUserPassword_Type())
juniFileXferRemoteUserPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFileXferRemoteUserPassword.setStatus(_G)
class _JuniFileXferLocalFileName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_JuniFileXferLocalFileName_Type.__name__=_E
_JuniFileXferLocalFileName_Object=MibTableColumn
juniFileXferLocalFileName=_JuniFileXferLocalFileName_Object((1,3,6,1,4,1,4874,2,2,23,1,1,1,7),_JuniFileXferLocalFileName_Type())
juniFileXferLocalFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFileXferLocalFileName.setStatus(_B)
class _JuniFileXferProtocol_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('juniFileXferFtp',1),('juniFileXferTftp',2)))
_JuniFileXferProtocol_Type.__name__=_D
_JuniFileXferProtocol_Object=MibTableColumn
juniFileXferProtocol=_JuniFileXferProtocol_Object((1,3,6,1,4,1,4874,2,2,23,1,1,1,8),_JuniFileXferProtocol_Type())
juniFileXferProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFileXferProtocol.setStatus(_B)
class _JuniFileXferStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('juniFileXferSuccessfulCompletion',1),('juniFileXferInProgress',2),('juniFileXferRemoteUnreachable',3),('juniFileXferUserAuthFailed',4),('juniFileXferFileNotFound',5),('juniFileXferFileTooBig',6),('juniFileXferFileIncompatible',7),('juniFileXferPended',8),('juniFileXferCopyRunningCfgFailed',9)))
_JuniFileXferStatus_Type.__name__=_D
_JuniFileXferStatus_Object=MibTableColumn
juniFileXferStatus=_JuniFileXferStatus_Object((1,3,6,1,4,1,4874,2,2,23,1,1,1,9),_JuniFileXferStatus_Type())
juniFileXferStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:juniFileXferStatus.setStatus(_B)
_JuniFileXferRowStatus_Type=RowStatus
_JuniFileXferRowStatus_Object=MibTableColumn
juniFileXferRowStatus=_JuniFileXferRowStatus_Object((1,3,6,1,4,1,4874,2,2,23,1,1,1,10),_JuniFileXferRowStatus_Type())
juniFileXferRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFileXferRowStatus.setStatus(_B)
_JuniFileXferTimeStamp_Type=TimeTicks
_JuniFileXferTimeStamp_Object=MibTableColumn
juniFileXferTimeStamp=_JuniFileXferTimeStamp_Object((1,3,6,1,4,1,4874,2,2,23,1,1,1,11),_JuniFileXferTimeStamp_Type())
juniFileXferTimeStamp.setMaxAccess(_J)
if mibBuilder.loadTexts:juniFileXferTimeStamp.setStatus(_B)
_JuniFileXferRouterName_Type=JuniName
_JuniFileXferRouterName_Object=MibTableColumn
juniFileXferRouterName=_JuniFileXferRouterName_Object((1,3,6,1,4,1,4874,2,2,23,1,1,1,12),_JuniFileXferRouterName_Type())
juniFileXferRouterName.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFileXferRouterName.setStatus(_B)
class _JuniFileXferTrapEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_JuniFileXferTrapEnabled_Type.__name__=_D
_JuniFileXferTrapEnabled_Object=MibScalar
juniFileXferTrapEnabled=_JuniFileXferTrapEnabled_Object((1,3,6,1,4,1,4874,2,2,23,1,2),_JuniFileXferTrapEnabled_Type())
juniFileXferTrapEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFileXferTrapEnabled.setStatus(_B)
_JuniFileXferNotifications_ObjectIdentity=ObjectIdentity
juniFileXferNotifications=_JuniFileXferNotifications_ObjectIdentity((1,3,6,1,4,1,4874,2,2,23,2))
_JuniFileXferNotifyPrefix_ObjectIdentity=ObjectIdentity
juniFileXferNotifyPrefix=_JuniFileXferNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,4874,2,2,23,2,0))
_JuniFileXferConformance_ObjectIdentity=ObjectIdentity
juniFileXferConformance=_JuniFileXferConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,23,4))
_JuniFileXferCompliances_ObjectIdentity=ObjectIdentity
juniFileXferCompliances=_JuniFileXferCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,23,4,1))
_JuniFileXferGroups_ObjectIdentity=ObjectIdentity
juniFileXferGroups=_JuniFileXferGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,23,4,2))
juniFileXferGroup1=ObjectGroup((1,3,6,1,4,1,4874,2,2,23,4,2,2))
juniFileXferGroup1.setObjects(*((_A,_F),(_A,_K),(_A,_L),(_A,_M),(_A,_U),(_A,_V),(_A,_N),(_A,_O),(_A,_H),(_A,_P),(_A,_I),(_A,_Q)))
if mibBuilder.loadTexts:juniFileXferGroup1.setStatus(_G)
juniFileXferGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,23,4,2,3))
juniFileXferGroup2.setObjects(*((_A,_F),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_H),(_A,_P),(_A,_I),(_A,_W),(_A,_Q)))
if mibBuilder.loadTexts:juniFileXferGroup2.setStatus(_B)
juniFileXferTrap=NotificationType((1,3,6,1,4,1,4874,2,2,23,2,0,1))
juniFileXferTrap.setObjects(*((_A,_H),(_A,_I)))
if mibBuilder.loadTexts:juniFileXferTrap.setStatus(_B)
juniFileXferTrapGroup=NotificationGroup((1,3,6,1,4,1,4874,2,2,23,4,2,4))
juniFileXferTrapGroup.setObjects((_A,_X))
if mibBuilder.loadTexts:juniFileXferTrapGroup.setStatus(_B)
juniFileXferCompliance1=ModuleCompliance((1,3,6,1,4,1,4874,2,2,23,4,1,2))
juniFileXferCompliance1.setObjects(*((_A,_Y),(_A,_R)))
if mibBuilder.loadTexts:juniFileXferCompliance1.setStatus(_G)
juniFileXferCompliance2=ModuleCompliance((1,3,6,1,4,1,4874,2,2,23,4,1,3))
juniFileXferCompliance2.setObjects(*((_A,_Z),(_A,_R)))
if mibBuilder.loadTexts:juniFileXferCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'juniFileXferMIB':juniFileXferMIB,'juniFileXferObjects':juniFileXferObjects,'juniFileXferTable':juniFileXferTable,'juniFileXferTableEntry':juniFileXferTableEntry,_F:juniFileXferIndex,_K:juniFileXferDirection,_L:juniFileXferFileType,_M:juniFileXferRemoteFileName,_U:juniFileXferRemoteUserName,_V:juniFileXferRemoteUserPassword,_N:juniFileXferLocalFileName,_O:juniFileXferProtocol,_H:juniFileXferStatus,_P:juniFileXferRowStatus,_I:juniFileXferTimeStamp,_W:juniFileXferRouterName,_Q:juniFileXferTrapEnabled,'juniFileXferNotifications':juniFileXferNotifications,'juniFileXferNotifyPrefix':juniFileXferNotifyPrefix,_X:juniFileXferTrap,'juniFileXferConformance':juniFileXferConformance,'juniFileXferCompliances':juniFileXferCompliances,'juniFileXferCompliance1':juniFileXferCompliance1,'juniFileXferCompliance2':juniFileXferCompliance2,'juniFileXferGroups':juniFileXferGroups,_Y:juniFileXferGroup1,_Z:juniFileXferGroup2,_R:juniFileXferTrapGroup})