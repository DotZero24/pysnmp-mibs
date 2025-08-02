_M='rlCLIremoteCLIoutputRowPartNumber'
_L='rlCLIremoteCLIoutputRowIndex'
_K='read-create'
_J='rlCLIremoteCLIcommandPartNumber'
_I='rlCLIremoteCLIcommandIndex'
_H='DisplayString'
_G='not-accessible'
_F='EDGECORE-CLI-MIB'
_E='read-only'
_D='Unsigned32'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rnd,=mibBuilder.importSymbols('EDGECORE-MIB','rnd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','RowStatus','TextualConvention','TruthValue')
rlCli=ModuleIdentity((1,3,6,1,4,1,259,10,1,14,89,52))
if mibBuilder.loadTexts:rlCli.setRevisions(('2010-05-25 00:00','2007-01-02 00:00'))
_RlCliMibVersion_Type=Integer32
_RlCliMibVersion_Object=MibScalar
rlCliMibVersion=_RlCliMibVersion_Object((1,3,6,1,4,1,259,10,1,14,89,52,1),_RlCliMibVersion_Type())
rlCliMibVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:rlCliMibVersion.setStatus(_A)
class _RlCliPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RlCliPassword_Type.__name__=_H
_RlCliPassword_Object=MibScalar
rlCliPassword=_RlCliPassword_Object((1,3,6,1,4,1,259,10,1,14,89,52,2),_RlCliPassword_Type())
rlCliPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCliPassword.setStatus(_A)
class _RlCliTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,3600))
_RlCliTimer_Type.__name__=_C
_RlCliTimer_Object=MibScalar
rlCliTimer=_RlCliTimer_Object((1,3,6,1,4,1,259,10,1,14,89,52,3),_RlCliTimer_Type())
rlCliTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCliTimer.setStatus(_A)
_RlCliFileEnable_Type=TruthValue
_RlCliFileEnable_Object=MibScalar
rlCliFileEnable=_RlCliFileEnable_Object((1,3,6,1,4,1,259,10,1,14,89,52,4),_RlCliFileEnable_Type())
rlCliFileEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:rlCliFileEnable.setStatus(_A)
_RlCliFileEnableAfterReset_Type=TruthValue
_RlCliFileEnableAfterReset_Object=MibScalar
rlCliFileEnableAfterReset=_RlCliFileEnableAfterReset_Object((1,3,6,1,4,1,259,10,1,14,89,52,5),_RlCliFileEnableAfterReset_Type())
rlCliFileEnableAfterReset.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCliFileEnableAfterReset.setStatus(_A)
_RlCLIremoteCLIsupport_ObjectIdentity=ObjectIdentity
rlCLIremoteCLIsupport=_RlCLIremoteCLIsupport_ObjectIdentity((1,3,6,1,4,1,259,10,1,14,89,52,6))
class _RlCLIremoteCLIcommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('takeRemoteCLI',1),('releaseRemoteCLI',2),('applySentCLI',3),('deleteCommandsCLI',4),('setEchoModeCLI',5),('unsetEchoModeCLI',6)))
_RlCLIremoteCLIcommand_Type.__name__=_C
_RlCLIremoteCLIcommand_Object=MibScalar
rlCLIremoteCLIcommand=_RlCLIremoteCLIcommand_Object((1,3,6,1,4,1,259,10,1,14,89,52,6,1),_RlCLIremoteCLIcommand_Type())
rlCLIremoteCLIcommand.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCLIremoteCLIcommand.setStatus(_A)
class _RlCLIremoteCLIexecutionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('free',1),('notActive',2),('inProcess',3),('outputAvailable',4),('waitingForOutputRetrieval',5),('done',6)))
_RlCLIremoteCLIexecutionState_Type.__name__=_C
_RlCLIremoteCLIexecutionState_Object=MibScalar
rlCLIremoteCLIexecutionState=_RlCLIremoteCLIexecutionState_Object((1,3,6,1,4,1,259,10,1,14,89,52,6,2),_RlCLIremoteCLIexecutionState_Type())
rlCLIremoteCLIexecutionState.setMaxAccess(_E)
if mibBuilder.loadTexts:rlCLIremoteCLIexecutionState.setStatus(_A)
_RlCLIremoteCLIexecutionCommandIndex_Type=Unsigned32
_RlCLIremoteCLIexecutionCommandIndex_Object=MibScalar
rlCLIremoteCLIexecutionCommandIndex=_RlCLIremoteCLIexecutionCommandIndex_Object((1,3,6,1,4,1,259,10,1,14,89,52,6,3),_RlCLIremoteCLIexecutionCommandIndex_Type())
rlCLIremoteCLIexecutionCommandIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rlCLIremoteCLIexecutionCommandIndex.setStatus(_A)
class _RlCLIremoteCLImode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('deleteCLIOutputOnGet',1),('keepCLIOutputOnGet',2)))
_RlCLIremoteCLImode_Type.__name__=_C
_RlCLIremoteCLImode_Object=MibScalar
rlCLIremoteCLImode=_RlCLIremoteCLImode_Object((1,3,6,1,4,1,259,10,1,14,89,52,6,4),_RlCLIremoteCLImode_Type())
rlCLIremoteCLImode.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCLIremoteCLImode.setStatus(_A)
_RlCLIremoteCLIcommandsTable_Object=MibTable
rlCLIremoteCLIcommandsTable=_RlCLIremoteCLIcommandsTable_Object((1,3,6,1,4,1,259,10,1,14,89,52,6,5))
if mibBuilder.loadTexts:rlCLIremoteCLIcommandsTable.setStatus(_A)
_RlCLIremoteCLIcommandsEntry_Object=MibTableRow
rlCLIremoteCLIcommandsEntry=_RlCLIremoteCLIcommandsEntry_Object((1,3,6,1,4,1,259,10,1,14,89,52,6,5,1))
rlCLIremoteCLIcommandsEntry.setIndexNames((0,_F,_I),(0,_F,_J))
if mibBuilder.loadTexts:rlCLIremoteCLIcommandsEntry.setStatus(_A)
class _RlCLIremoteCLIcommandIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_RlCLIremoteCLIcommandIndex_Type.__name__=_D
_RlCLIremoteCLIcommandIndex_Object=MibTableColumn
rlCLIremoteCLIcommandIndex=_RlCLIremoteCLIcommandIndex_Object((1,3,6,1,4,1,259,10,1,14,89,52,6,5,1,1),_RlCLIremoteCLIcommandIndex_Type())
rlCLIremoteCLIcommandIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:rlCLIremoteCLIcommandIndex.setStatus(_A)
class _RlCLIremoteCLIcommandPartNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_RlCLIremoteCLIcommandPartNumber_Type.__name__=_D
_RlCLIremoteCLIcommandPartNumber_Object=MibTableColumn
rlCLIremoteCLIcommandPartNumber=_RlCLIremoteCLIcommandPartNumber_Object((1,3,6,1,4,1,259,10,1,14,89,52,6,5,1,2),_RlCLIremoteCLIcommandPartNumber_Type())
rlCLIremoteCLIcommandPartNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:rlCLIremoteCLIcommandPartNumber.setStatus(_A)
_RlCLIremoteCLIcommandPart_Type=OctetString
_RlCLIremoteCLIcommandPart_Object=MibTableColumn
rlCLIremoteCLIcommandPart=_RlCLIremoteCLIcommandPart_Object((1,3,6,1,4,1,259,10,1,14,89,52,6,5,1,3),_RlCLIremoteCLIcommandPart_Type())
rlCLIremoteCLIcommandPart.setMaxAccess(_K)
if mibBuilder.loadTexts:rlCLIremoteCLIcommandPart.setStatus(_A)
_RlCLIremoteCLIcommandStatus_Type=RowStatus
_RlCLIremoteCLIcommandStatus_Object=MibTableColumn
rlCLIremoteCLIcommandStatus=_RlCLIremoteCLIcommandStatus_Object((1,3,6,1,4,1,259,10,1,14,89,52,6,5,1,4),_RlCLIremoteCLIcommandStatus_Type())
rlCLIremoteCLIcommandStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:rlCLIremoteCLIcommandStatus.setStatus(_A)
_RlCLIremoteCLIoutputsTable_Object=MibTable
rlCLIremoteCLIoutputsTable=_RlCLIremoteCLIoutputsTable_Object((1,3,6,1,4,1,259,10,1,14,89,52,6,6))
if mibBuilder.loadTexts:rlCLIremoteCLIoutputsTable.setStatus(_A)
_RlCLIremoteCLIoutputsEntry_Object=MibTableRow
rlCLIremoteCLIoutputsEntry=_RlCLIremoteCLIoutputsEntry_Object((1,3,6,1,4,1,259,10,1,14,89,52,6,6,1))
rlCLIremoteCLIoutputsEntry.setIndexNames((0,_F,_L),(0,_F,_M))
if mibBuilder.loadTexts:rlCLIremoteCLIoutputsEntry.setStatus(_A)
class _RlCLIremoteCLIoutputRowIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_RlCLIremoteCLIoutputRowIndex_Type.__name__=_D
_RlCLIremoteCLIoutputRowIndex_Object=MibTableColumn
rlCLIremoteCLIoutputRowIndex=_RlCLIremoteCLIoutputRowIndex_Object((1,3,6,1,4,1,259,10,1,14,89,52,6,6,1,1),_RlCLIremoteCLIoutputRowIndex_Type())
rlCLIremoteCLIoutputRowIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:rlCLIremoteCLIoutputRowIndex.setStatus(_A)
class _RlCLIremoteCLIoutputRowPartNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_RlCLIremoteCLIoutputRowPartNumber_Type.__name__=_D
_RlCLIremoteCLIoutputRowPartNumber_Object=MibTableColumn
rlCLIremoteCLIoutputRowPartNumber=_RlCLIremoteCLIoutputRowPartNumber_Object((1,3,6,1,4,1,259,10,1,14,89,52,6,6,1,2),_RlCLIremoteCLIoutputRowPartNumber_Type())
rlCLIremoteCLIoutputRowPartNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:rlCLIremoteCLIoutputRowPartNumber.setStatus(_A)
_RlCLIremoteCLIoutputRowPart_Type=OctetString
_RlCLIremoteCLIoutputRowPart_Object=MibTableColumn
rlCLIremoteCLIoutputRowPart=_RlCLIremoteCLIoutputRowPart_Object((1,3,6,1,4,1,259,10,1,14,89,52,6,6,1,3),_RlCLIremoteCLIoutputRowPart_Type())
rlCLIremoteCLIoutputRowPart.setMaxAccess(_E)
if mibBuilder.loadTexts:rlCLIremoteCLIoutputRowPart.setStatus(_A)
_RlCLIremoteCLIoutputRowStatus_Type=RowStatus
_RlCLIremoteCLIoutputRowStatus_Object=MibTableColumn
rlCLIremoteCLIoutputRowStatus=_RlCLIremoteCLIoutputRowStatus_Object((1,3,6,1,4,1,259,10,1,14,89,52,6,6,1,4),_RlCLIremoteCLIoutputRowStatus_Type())
rlCLIremoteCLIoutputRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCLIremoteCLIoutputRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'rlCli':rlCli,'rlCliMibVersion':rlCliMibVersion,'rlCliPassword':rlCliPassword,'rlCliTimer':rlCliTimer,'rlCliFileEnable':rlCliFileEnable,'rlCliFileEnableAfterReset':rlCliFileEnableAfterReset,'rlCLIremoteCLIsupport':rlCLIremoteCLIsupport,'rlCLIremoteCLIcommand':rlCLIremoteCLIcommand,'rlCLIremoteCLIexecutionState':rlCLIremoteCLIexecutionState,'rlCLIremoteCLIexecutionCommandIndex':rlCLIremoteCLIexecutionCommandIndex,'rlCLIremoteCLImode':rlCLIremoteCLImode,'rlCLIremoteCLIcommandsTable':rlCLIremoteCLIcommandsTable,'rlCLIremoteCLIcommandsEntry':rlCLIremoteCLIcommandsEntry,_I:rlCLIremoteCLIcommandIndex,_J:rlCLIremoteCLIcommandPartNumber,'rlCLIremoteCLIcommandPart':rlCLIremoteCLIcommandPart,'rlCLIremoteCLIcommandStatus':rlCLIremoteCLIcommandStatus,'rlCLIremoteCLIoutputsTable':rlCLIremoteCLIoutputsTable,'rlCLIremoteCLIoutputsEntry':rlCLIremoteCLIoutputsEntry,_L:rlCLIremoteCLIoutputRowIndex,_M:rlCLIremoteCLIoutputRowPartNumber,'rlCLIremoteCLIoutputRowPart':rlCLIremoteCLIoutputRowPart,'rlCLIremoteCLIoutputRowStatus':rlCLIremoteCLIoutputRowStatus})