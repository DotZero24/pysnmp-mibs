_A4='openflowLogGroupV1'
_A3='openflowDiagnosticsGroupV1'
_A2='openflowLogicalSwitchGroupV2'
_A1='openflowLogCreateOFDiagnostics'
_A0='openflowLogSubrack'
_z='openflowLogName'
_y='openflowDiagnosticsSubrack'
_x='openflowDiagnosticsConfigure'
_w='openflowDiagnosticsLogServerType'
_v='openflowDiagnosticsTcpPort'
_u='openflowDiagnosticsIpv4Addr'
_t='openflowDiagnosticsName'
_s='openflowLogicalSwitchOfVersion'
_r='openflowLogicalSwitchGetTracelogs'
_q='openflowLogicalSwitchAssociateCxn'
_p='openflowGenericCreateOFLS'
_o='openflowGenericSlot'
_n='openflowGenericSubrack'
_m='openflowGenericName'
_l='openflowConnectionSlot'
_k='openflowConnectionSubrack'
_j='openflowConnectionOfVersion'
_i='openflowConnectionRole'
_h='openflowConnectionState'
_g='openflowConnectionTcpPort'
_f='openflowConnectionIpv4Addr'
_e='openflowConnectionSwitchIdentity'
_d='openflowConnectionIdentity'
_c='openflowConnectionDescr'
_b='openflowConnectionName'
_a='openflowGeneralStateLastChangeTime'
_Z='openflowGeneralConfigLastChangeTime'
_Y='OctetString'
_X='openflowLogicalSwitchGroupV1'
_W='deprecated'
_V='openflowLogicalSwitchSlot'
_U='openflowLogicalSwitchSubrack'
_T='openflowLogicalSwitchDpId'
_S='openflowLogicalSwitchMacAddress'
_R='openflowLogicalSwitchIdentity'
_Q='openflowLogicalSwitchDescr'
_P='openflowLogicalSwitchName'
_O='openflowLogIndex'
_N='openflowDiagnosticsIndex'
_M='openflowGenericIndex'
_L='openflowConnectionIndex'
_K='read-write'
_J='openflowGenericGroupV1'
_I='openflowConnectionGroupV1'
_H='openflowGeneralGroupV1'
_G='openflowLogicalSwitchIndex'
_F='Integer32'
_E='read-create'
_D='Unsigned32'
_C='read-only'
_B='current'
_A='LUM-OPENFLOW-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_Y,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumModules,lumOpenflowMIB=mibBuilder.importSymbols('LUM-REG','lumModules','lumOpenflowMIB')
CommandString,MgmtNameString,SlotNumber,SubrackNumber=mibBuilder.importSymbols('LUM-TC','CommandString','MgmtNameString','SlotNumber','SubrackNumber')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
lumOpenflowMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,69))
if mibBuilder.loadTexts:lumOpenflowMIBModule.setRevisions(('2018-09-01 00:00','2017-06-15 00:00','2016-11-30 00:00'))
_LumOpenflowConfs_ObjectIdentity=ObjectIdentity
lumOpenflowConfs=_LumOpenflowConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,69,1))
_LumOpenflowGroups_ObjectIdentity=ObjectIdentity
lumOpenflowGroups=_LumOpenflowGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,69,1,1))
_LumOpenflowCompl_ObjectIdentity=ObjectIdentity
lumOpenflowCompl=_LumOpenflowCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,69,1,2))
_LumOpenflowMIBObjects_ObjectIdentity=ObjectIdentity
lumOpenflowMIBObjects=_LumOpenflowMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,69,2))
_OpenflowGeneral_ObjectIdentity=ObjectIdentity
openflowGeneral=_OpenflowGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,69,2,1))
_OpenflowGeneralConfigLastChangeTime_Type=DateAndTime
_OpenflowGeneralConfigLastChangeTime_Object=MibScalar
openflowGeneralConfigLastChangeTime=_OpenflowGeneralConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,69,2,1,1),_OpenflowGeneralConfigLastChangeTime_Type())
openflowGeneralConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:openflowGeneralConfigLastChangeTime.setStatus(_B)
_OpenflowGeneralStateLastChangeTime_Type=DateAndTime
_OpenflowGeneralStateLastChangeTime_Object=MibScalar
openflowGeneralStateLastChangeTime=_OpenflowGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,69,2,1,2),_OpenflowGeneralStateLastChangeTime_Type())
openflowGeneralStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:openflowGeneralStateLastChangeTime.setStatus(_B)
_OpenflowGeneralLogicalSwitchTableSize_Type=Unsigned32
_OpenflowGeneralLogicalSwitchTableSize_Object=MibScalar
openflowGeneralLogicalSwitchTableSize=_OpenflowGeneralLogicalSwitchTableSize_Object((1,3,6,1,4,1,8708,2,69,2,1,3),_OpenflowGeneralLogicalSwitchTableSize_Type())
openflowGeneralLogicalSwitchTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:openflowGeneralLogicalSwitchTableSize.setStatus(_B)
_OpenflowGeneralGenericTableSize_Type=Unsigned32
_OpenflowGeneralGenericTableSize_Object=MibScalar
openflowGeneralGenericTableSize=_OpenflowGeneralGenericTableSize_Object((1,3,6,1,4,1,8708,2,69,2,1,4),_OpenflowGeneralGenericTableSize_Type())
openflowGeneralGenericTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:openflowGeneralGenericTableSize.setStatus(_B)
_OpenflowGeneralConnectionTableSize_Type=Unsigned32
_OpenflowGeneralConnectionTableSize_Object=MibScalar
openflowGeneralConnectionTableSize=_OpenflowGeneralConnectionTableSize_Object((1,3,6,1,4,1,8708,2,69,2,1,5),_OpenflowGeneralConnectionTableSize_Type())
openflowGeneralConnectionTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:openflowGeneralConnectionTableSize.setStatus(_B)
_OpenflowGeneralDiagnosticsTableSize_Type=Unsigned32
_OpenflowGeneralDiagnosticsTableSize_Object=MibScalar
openflowGeneralDiagnosticsTableSize=_OpenflowGeneralDiagnosticsTableSize_Object((1,3,6,1,4,1,8708,2,69,2,1,6),_OpenflowGeneralDiagnosticsTableSize_Type())
openflowGeneralDiagnosticsTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:openflowGeneralDiagnosticsTableSize.setStatus(_B)
_OpenflowGeneralLogTableSize_Type=Unsigned32
_OpenflowGeneralLogTableSize_Object=MibScalar
openflowGeneralLogTableSize=_OpenflowGeneralLogTableSize_Object((1,3,6,1,4,1,8708,2,69,2,1,7),_OpenflowGeneralLogTableSize_Type())
openflowGeneralLogTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:openflowGeneralLogTableSize.setStatus(_B)
_OpenflowLogicalSwitchList_ObjectIdentity=ObjectIdentity
openflowLogicalSwitchList=_OpenflowLogicalSwitchList_ObjectIdentity((1,3,6,1,4,1,8708,2,69,2,2))
_OpenflowLogicalSwitchTable_Object=MibTable
openflowLogicalSwitchTable=_OpenflowLogicalSwitchTable_Object((1,3,6,1,4,1,8708,2,69,2,2,1))
if mibBuilder.loadTexts:openflowLogicalSwitchTable.setStatus(_B)
_OpenflowLogicalSwitchEntry_Object=MibTableRow
openflowLogicalSwitchEntry=_OpenflowLogicalSwitchEntry_Object((1,3,6,1,4,1,8708,2,69,2,2,1,1))
openflowLogicalSwitchEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:openflowLogicalSwitchEntry.setStatus(_B)
_OpenflowLogicalSwitchName_Type=MgmtNameString
_OpenflowLogicalSwitchName_Object=MibTableColumn
openflowLogicalSwitchName=_OpenflowLogicalSwitchName_Object((1,3,6,1,4,1,8708,2,69,2,2,1,1,1),_OpenflowLogicalSwitchName_Type())
openflowLogicalSwitchName.setMaxAccess(_C)
if mibBuilder.loadTexts:openflowLogicalSwitchName.setStatus(_B)
class _OpenflowLogicalSwitchIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OpenflowLogicalSwitchIndex_Type.__name__=_D
_OpenflowLogicalSwitchIndex_Object=MibTableColumn
openflowLogicalSwitchIndex=_OpenflowLogicalSwitchIndex_Object((1,3,6,1,4,1,8708,2,69,2,2,1,1,2),_OpenflowLogicalSwitchIndex_Type())
openflowLogicalSwitchIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:openflowLogicalSwitchIndex.setStatus(_B)
_OpenflowLogicalSwitchDescr_Type=DisplayString
_OpenflowLogicalSwitchDescr_Object=MibTableColumn
openflowLogicalSwitchDescr=_OpenflowLogicalSwitchDescr_Object((1,3,6,1,4,1,8708,2,69,2,2,1,1,3),_OpenflowLogicalSwitchDescr_Type())
openflowLogicalSwitchDescr.setMaxAccess(_K)
if mibBuilder.loadTexts:openflowLogicalSwitchDescr.setStatus(_B)
class _OpenflowLogicalSwitchIdentity_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_OpenflowLogicalSwitchIdentity_Type.__name__=_D
_OpenflowLogicalSwitchIdentity_Object=MibTableColumn
openflowLogicalSwitchIdentity=_OpenflowLogicalSwitchIdentity_Object((1,3,6,1,4,1,8708,2,69,2,2,1,1,4),_OpenflowLogicalSwitchIdentity_Type())
openflowLogicalSwitchIdentity.setMaxAccess(_C)
if mibBuilder.loadTexts:openflowLogicalSwitchIdentity.setStatus(_B)
class _OpenflowLogicalSwitchMacAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_OpenflowLogicalSwitchMacAddress_Type.__name__=_Y
_OpenflowLogicalSwitchMacAddress_Object=MibTableColumn
openflowLogicalSwitchMacAddress=_OpenflowLogicalSwitchMacAddress_Object((1,3,6,1,4,1,8708,2,69,2,2,1,1,5),_OpenflowLogicalSwitchMacAddress_Type())
openflowLogicalSwitchMacAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:openflowLogicalSwitchMacAddress.setStatus(_B)
_OpenflowLogicalSwitchDpId_Type=DisplayString
_OpenflowLogicalSwitchDpId_Object=MibTableColumn
openflowLogicalSwitchDpId=_OpenflowLogicalSwitchDpId_Object((1,3,6,1,4,1,8708,2,69,2,2,1,1,6),_OpenflowLogicalSwitchDpId_Type())
openflowLogicalSwitchDpId.setMaxAccess(_C)
if mibBuilder.loadTexts:openflowLogicalSwitchDpId.setStatus(_B)
_OpenflowLogicalSwitchAssociateCxn_Type=CommandString
_OpenflowLogicalSwitchAssociateCxn_Object=MibTableColumn
openflowLogicalSwitchAssociateCxn=_OpenflowLogicalSwitchAssociateCxn_Object((1,3,6,1,4,1,8708,2,69,2,2,1,1,7),_OpenflowLogicalSwitchAssociateCxn_Type())
openflowLogicalSwitchAssociateCxn.setMaxAccess(_C)
if mibBuilder.loadTexts:openflowLogicalSwitchAssociateCxn.setStatus(_B)
_OpenflowLogicalSwitchSubrack_Type=SubrackNumber
_OpenflowLogicalSwitchSubrack_Object=MibTableColumn
openflowLogicalSwitchSubrack=_OpenflowLogicalSwitchSubrack_Object((1,3,6,1,4,1,8708,2,69,2,2,1,1,8),_OpenflowLogicalSwitchSubrack_Type())
openflowLogicalSwitchSubrack.setMaxAccess(_E)
if mibBuilder.loadTexts:openflowLogicalSwitchSubrack.setStatus(_B)
_OpenflowLogicalSwitchSlot_Type=SlotNumber
_OpenflowLogicalSwitchSlot_Object=MibTableColumn
openflowLogicalSwitchSlot=_OpenflowLogicalSwitchSlot_Object((1,3,6,1,4,1,8708,2,69,2,2,1,1,9),_OpenflowLogicalSwitchSlot_Type())
openflowLogicalSwitchSlot.setMaxAccess(_E)
if mibBuilder.loadTexts:openflowLogicalSwitchSlot.setStatus(_B)
_OpenflowLogicalSwitchGetTracelogs_Type=CommandString
_OpenflowLogicalSwitchGetTracelogs_Object=MibTableColumn
openflowLogicalSwitchGetTracelogs=_OpenflowLogicalSwitchGetTracelogs_Object((1,3,6,1,4,1,8708,2,69,2,2,1,1,10),_OpenflowLogicalSwitchGetTracelogs_Type())
openflowLogicalSwitchGetTracelogs.setMaxAccess(_C)
if mibBuilder.loadTexts:openflowLogicalSwitchGetTracelogs.setStatus(_B)
_OpenflowLogicalSwitchOfVersion_Type=DisplayString
_OpenflowLogicalSwitchOfVersion_Object=MibTableColumn
openflowLogicalSwitchOfVersion=_OpenflowLogicalSwitchOfVersion_Object((1,3,6,1,4,1,8708,2,69,2,2,1,1,11),_OpenflowLogicalSwitchOfVersion_Type())
openflowLogicalSwitchOfVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:openflowLogicalSwitchOfVersion.setStatus(_B)
_OpenflowConnectionList_ObjectIdentity=ObjectIdentity
openflowConnectionList=_OpenflowConnectionList_ObjectIdentity((1,3,6,1,4,1,8708,2,69,2,3))
_OpenflowConnectionTable_Object=MibTable
openflowConnectionTable=_OpenflowConnectionTable_Object((1,3,6,1,4,1,8708,2,69,2,3,1))
if mibBuilder.loadTexts:openflowConnectionTable.setStatus(_B)
_OpenflowConnectionEntry_Object=MibTableRow
openflowConnectionEntry=_OpenflowConnectionEntry_Object((1,3,6,1,4,1,8708,2,69,2,3,1,1))
openflowConnectionEntry.setIndexNames((0,_A,_L))
if mibBuilder.loadTexts:openflowConnectionEntry.setStatus(_B)
_OpenflowConnectionName_Type=MgmtNameString
_OpenflowConnectionName_Object=MibTableColumn
openflowConnectionName=_OpenflowConnectionName_Object((1,3,6,1,4,1,8708,2,69,2,3,1,1,1),_OpenflowConnectionName_Type())
openflowConnectionName.setMaxAccess(_C)
if mibBuilder.loadTexts:openflowConnectionName.setStatus(_B)
class _OpenflowConnectionIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OpenflowConnectionIndex_Type.__name__=_D
_OpenflowConnectionIndex_Object=MibTableColumn
openflowConnectionIndex=_OpenflowConnectionIndex_Object((1,3,6,1,4,1,8708,2,69,2,3,1,1,2),_OpenflowConnectionIndex_Type())
openflowConnectionIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:openflowConnectionIndex.setStatus(_B)
_OpenflowConnectionDescr_Type=DisplayString
_OpenflowConnectionDescr_Object=MibTableColumn
openflowConnectionDescr=_OpenflowConnectionDescr_Object((1,3,6,1,4,1,8708,2,69,2,3,1,1,3),_OpenflowConnectionDescr_Type())
openflowConnectionDescr.setMaxAccess(_K)
if mibBuilder.loadTexts:openflowConnectionDescr.setStatus(_B)
class _OpenflowConnectionIdentity_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OpenflowConnectionIdentity_Type.__name__=_D
_OpenflowConnectionIdentity_Object=MibTableColumn
openflowConnectionIdentity=_OpenflowConnectionIdentity_Object((1,3,6,1,4,1,8708,2,69,2,3,1,1,4),_OpenflowConnectionIdentity_Type())
openflowConnectionIdentity.setMaxAccess(_C)
if mibBuilder.loadTexts:openflowConnectionIdentity.setStatus(_B)
class _OpenflowConnectionSwitchIdentity_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_OpenflowConnectionSwitchIdentity_Type.__name__=_D
_OpenflowConnectionSwitchIdentity_Object=MibTableColumn
openflowConnectionSwitchIdentity=_OpenflowConnectionSwitchIdentity_Object((1,3,6,1,4,1,8708,2,69,2,3,1,1,5),_OpenflowConnectionSwitchIdentity_Type())
openflowConnectionSwitchIdentity.setMaxAccess(_C)
if mibBuilder.loadTexts:openflowConnectionSwitchIdentity.setStatus(_B)
_OpenflowConnectionIpv4Addr_Type=IpAddress
_OpenflowConnectionIpv4Addr_Object=MibTableColumn
openflowConnectionIpv4Addr=_OpenflowConnectionIpv4Addr_Object((1,3,6,1,4,1,8708,2,69,2,3,1,1,6),_OpenflowConnectionIpv4Addr_Type())
openflowConnectionIpv4Addr.setMaxAccess(_E)
if mibBuilder.loadTexts:openflowConnectionIpv4Addr.setStatus(_B)
class _OpenflowConnectionTcpPort_Type(Unsigned32):defaultValue=6653;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_OpenflowConnectionTcpPort_Type.__name__=_D
_OpenflowConnectionTcpPort_Object=MibTableColumn
openflowConnectionTcpPort=_OpenflowConnectionTcpPort_Object((1,3,6,1,4,1,8708,2,69,2,3,1,1,7),_OpenflowConnectionTcpPort_Type())
openflowConnectionTcpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:openflowConnectionTcpPort.setStatus(_B)
class _OpenflowConnectionState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('disconnected',1),('connecting',2),('connected',3),('disconnecting',4)))
_OpenflowConnectionState_Type.__name__=_F
_OpenflowConnectionState_Object=MibTableColumn
openflowConnectionState=_OpenflowConnectionState_Object((1,3,6,1,4,1,8708,2,69,2,3,1,1,8),_OpenflowConnectionState_Type())
openflowConnectionState.setMaxAccess(_C)
if mibBuilder.loadTexts:openflowConnectionState.setStatus(_B)
class _OpenflowConnectionRole_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unknown',1),('equal',2),('master',3),('slave',4)))
_OpenflowConnectionRole_Type.__name__=_F
_OpenflowConnectionRole_Object=MibTableColumn
openflowConnectionRole=_OpenflowConnectionRole_Object((1,3,6,1,4,1,8708,2,69,2,3,1,1,9),_OpenflowConnectionRole_Type())
openflowConnectionRole.setMaxAccess(_C)
if mibBuilder.loadTexts:openflowConnectionRole.setStatus(_B)
_OpenflowConnectionOfVersion_Type=DisplayString
_OpenflowConnectionOfVersion_Object=MibTableColumn
openflowConnectionOfVersion=_OpenflowConnectionOfVersion_Object((1,3,6,1,4,1,8708,2,69,2,3,1,1,10),_OpenflowConnectionOfVersion_Type())
openflowConnectionOfVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:openflowConnectionOfVersion.setStatus(_B)
_OpenflowConnectionSubrack_Type=SubrackNumber
_OpenflowConnectionSubrack_Object=MibTableColumn
openflowConnectionSubrack=_OpenflowConnectionSubrack_Object((1,3,6,1,4,1,8708,2,69,2,3,1,1,11),_OpenflowConnectionSubrack_Type())
openflowConnectionSubrack.setMaxAccess(_E)
if mibBuilder.loadTexts:openflowConnectionSubrack.setStatus(_B)
_OpenflowConnectionSlot_Type=SlotNumber
_OpenflowConnectionSlot_Object=MibTableColumn
openflowConnectionSlot=_OpenflowConnectionSlot_Object((1,3,6,1,4,1,8708,2,69,2,3,1,1,12),_OpenflowConnectionSlot_Type())
openflowConnectionSlot.setMaxAccess(_E)
if mibBuilder.loadTexts:openflowConnectionSlot.setStatus(_B)
_OpenflowGenericList_ObjectIdentity=ObjectIdentity
openflowGenericList=_OpenflowGenericList_ObjectIdentity((1,3,6,1,4,1,8708,2,69,2,4))
_OpenflowGenericTable_Object=MibTable
openflowGenericTable=_OpenflowGenericTable_Object((1,3,6,1,4,1,8708,2,69,2,4,1))
if mibBuilder.loadTexts:openflowGenericTable.setStatus(_B)
_OpenflowGenericEntry_Object=MibTableRow
openflowGenericEntry=_OpenflowGenericEntry_Object((1,3,6,1,4,1,8708,2,69,2,4,1,1))
openflowGenericEntry.setIndexNames((0,_A,_M))
if mibBuilder.loadTexts:openflowGenericEntry.setStatus(_B)
class _OpenflowGenericIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OpenflowGenericIndex_Type.__name__=_D
_OpenflowGenericIndex_Object=MibTableColumn
openflowGenericIndex=_OpenflowGenericIndex_Object((1,3,6,1,4,1,8708,2,69,2,4,1,1,1),_OpenflowGenericIndex_Type())
openflowGenericIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:openflowGenericIndex.setStatus(_B)
_OpenflowGenericName_Type=MgmtNameString
_OpenflowGenericName_Object=MibTableColumn
openflowGenericName=_OpenflowGenericName_Object((1,3,6,1,4,1,8708,2,69,2,4,1,1,2),_OpenflowGenericName_Type())
openflowGenericName.setMaxAccess(_C)
if mibBuilder.loadTexts:openflowGenericName.setStatus(_B)
class _OpenflowGenericSubrack_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OpenflowGenericSubrack_Type.__name__=_D
_OpenflowGenericSubrack_Object=MibTableColumn
openflowGenericSubrack=_OpenflowGenericSubrack_Object((1,3,6,1,4,1,8708,2,69,2,4,1,1,3),_OpenflowGenericSubrack_Type())
openflowGenericSubrack.setMaxAccess(_C)
if mibBuilder.loadTexts:openflowGenericSubrack.setStatus(_B)
class _OpenflowGenericSlot_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OpenflowGenericSlot_Type.__name__=_D
_OpenflowGenericSlot_Object=MibTableColumn
openflowGenericSlot=_OpenflowGenericSlot_Object((1,3,6,1,4,1,8708,2,69,2,4,1,1,4),_OpenflowGenericSlot_Type())
openflowGenericSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:openflowGenericSlot.setStatus(_B)
_OpenflowGenericCreateOFLS_Type=CommandString
_OpenflowGenericCreateOFLS_Object=MibTableColumn
openflowGenericCreateOFLS=_OpenflowGenericCreateOFLS_Object((1,3,6,1,4,1,8708,2,69,2,4,1,1,5),_OpenflowGenericCreateOFLS_Type())
openflowGenericCreateOFLS.setMaxAccess(_C)
if mibBuilder.loadTexts:openflowGenericCreateOFLS.setStatus(_B)
_OpenflowDiagnosticsList_ObjectIdentity=ObjectIdentity
openflowDiagnosticsList=_OpenflowDiagnosticsList_ObjectIdentity((1,3,6,1,4,1,8708,2,69,2,5))
_OpenflowDiagnosticsTable_Object=MibTable
openflowDiagnosticsTable=_OpenflowDiagnosticsTable_Object((1,3,6,1,4,1,8708,2,69,2,5,1))
if mibBuilder.loadTexts:openflowDiagnosticsTable.setStatus(_B)
_OpenflowDiagnosticsEntry_Object=MibTableRow
openflowDiagnosticsEntry=_OpenflowDiagnosticsEntry_Object((1,3,6,1,4,1,8708,2,69,2,5,1,1))
openflowDiagnosticsEntry.setIndexNames((0,_A,_N))
if mibBuilder.loadTexts:openflowDiagnosticsEntry.setStatus(_B)
class _OpenflowDiagnosticsIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OpenflowDiagnosticsIndex_Type.__name__=_D
_OpenflowDiagnosticsIndex_Object=MibTableColumn
openflowDiagnosticsIndex=_OpenflowDiagnosticsIndex_Object((1,3,6,1,4,1,8708,2,69,2,5,1,1,1),_OpenflowDiagnosticsIndex_Type())
openflowDiagnosticsIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:openflowDiagnosticsIndex.setStatus(_B)
_OpenflowDiagnosticsName_Type=MgmtNameString
_OpenflowDiagnosticsName_Object=MibTableColumn
openflowDiagnosticsName=_OpenflowDiagnosticsName_Object((1,3,6,1,4,1,8708,2,69,2,5,1,1,2),_OpenflowDiagnosticsName_Type())
openflowDiagnosticsName.setMaxAccess(_C)
if mibBuilder.loadTexts:openflowDiagnosticsName.setStatus(_B)
_OpenflowDiagnosticsIpv4Addr_Type=IpAddress
_OpenflowDiagnosticsIpv4Addr_Object=MibTableColumn
openflowDiagnosticsIpv4Addr=_OpenflowDiagnosticsIpv4Addr_Object((1,3,6,1,4,1,8708,2,69,2,5,1,1,3),_OpenflowDiagnosticsIpv4Addr_Type())
openflowDiagnosticsIpv4Addr.setMaxAccess(_E)
if mibBuilder.loadTexts:openflowDiagnosticsIpv4Addr.setStatus(_B)
class _OpenflowDiagnosticsTcpPort_Type(Unsigned32):defaultValue=9999;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_OpenflowDiagnosticsTcpPort_Type.__name__=_D
_OpenflowDiagnosticsTcpPort_Object=MibTableColumn
openflowDiagnosticsTcpPort=_OpenflowDiagnosticsTcpPort_Object((1,3,6,1,4,1,8708,2,69,2,5,1,1,4),_OpenflowDiagnosticsTcpPort_Type())
openflowDiagnosticsTcpPort.setMaxAccess(_E)
if mibBuilder.loadTexts:openflowDiagnosticsTcpPort.setStatus(_B)
class _OpenflowDiagnosticsLogServerType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2147483647)));namedValues=NamedValues(*(('syslog',1),('notApplicable',2147483647)))
_OpenflowDiagnosticsLogServerType_Type.__name__=_F
_OpenflowDiagnosticsLogServerType_Object=MibTableColumn
openflowDiagnosticsLogServerType=_OpenflowDiagnosticsLogServerType_Object((1,3,6,1,4,1,8708,2,69,2,5,1,1,5),_OpenflowDiagnosticsLogServerType_Type())
openflowDiagnosticsLogServerType.setMaxAccess(_K)
if mibBuilder.loadTexts:openflowDiagnosticsLogServerType.setStatus(_B)
_OpenflowDiagnosticsConfigure_Type=CommandString
_OpenflowDiagnosticsConfigure_Object=MibTableColumn
openflowDiagnosticsConfigure=_OpenflowDiagnosticsConfigure_Object((1,3,6,1,4,1,8708,2,69,2,5,1,1,6),_OpenflowDiagnosticsConfigure_Type())
openflowDiagnosticsConfigure.setMaxAccess(_C)
if mibBuilder.loadTexts:openflowDiagnosticsConfigure.setStatus(_B)
_OpenflowDiagnosticsSubrack_Type=SubrackNumber
_OpenflowDiagnosticsSubrack_Object=MibTableColumn
openflowDiagnosticsSubrack=_OpenflowDiagnosticsSubrack_Object((1,3,6,1,4,1,8708,2,69,2,5,1,1,7),_OpenflowDiagnosticsSubrack_Type())
openflowDiagnosticsSubrack.setMaxAccess(_C)
if mibBuilder.loadTexts:openflowDiagnosticsSubrack.setStatus(_B)
_OpenflowLogList_ObjectIdentity=ObjectIdentity
openflowLogList=_OpenflowLogList_ObjectIdentity((1,3,6,1,4,1,8708,2,69,2,6))
_OpenflowLogTable_Object=MibTable
openflowLogTable=_OpenflowLogTable_Object((1,3,6,1,4,1,8708,2,69,2,6,1))
if mibBuilder.loadTexts:openflowLogTable.setStatus(_B)
_OpenflowLogEntry_Object=MibTableRow
openflowLogEntry=_OpenflowLogEntry_Object((1,3,6,1,4,1,8708,2,69,2,6,1,1))
openflowLogEntry.setIndexNames((0,_A,_O))
if mibBuilder.loadTexts:openflowLogEntry.setStatus(_B)
class _OpenflowLogIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OpenflowLogIndex_Type.__name__=_D
_OpenflowLogIndex_Object=MibTableColumn
openflowLogIndex=_OpenflowLogIndex_Object((1,3,6,1,4,1,8708,2,69,2,6,1,1,1),_OpenflowLogIndex_Type())
openflowLogIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:openflowLogIndex.setStatus(_B)
_OpenflowLogName_Type=MgmtNameString
_OpenflowLogName_Object=MibTableColumn
openflowLogName=_OpenflowLogName_Object((1,3,6,1,4,1,8708,2,69,2,6,1,1,2),_OpenflowLogName_Type())
openflowLogName.setMaxAccess(_C)
if mibBuilder.loadTexts:openflowLogName.setStatus(_B)
class _OpenflowLogSubrack_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OpenflowLogSubrack_Type.__name__=_D
_OpenflowLogSubrack_Object=MibTableColumn
openflowLogSubrack=_OpenflowLogSubrack_Object((1,3,6,1,4,1,8708,2,69,2,6,1,1,3),_OpenflowLogSubrack_Type())
openflowLogSubrack.setMaxAccess(_C)
if mibBuilder.loadTexts:openflowLogSubrack.setStatus(_B)
_OpenflowLogCreateOFDiagnostics_Type=CommandString
_OpenflowLogCreateOFDiagnostics_Object=MibTableColumn
openflowLogCreateOFDiagnostics=_OpenflowLogCreateOFDiagnostics_Object((1,3,6,1,4,1,8708,2,69,2,6,1,1,4),_OpenflowLogCreateOFDiagnostics_Type())
openflowLogCreateOFDiagnostics.setMaxAccess(_C)
if mibBuilder.loadTexts:openflowLogCreateOFDiagnostics.setStatus(_B)
openflowGeneralGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,69,1,1,1))
openflowGeneralGroupV1.setObjects(*((_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:openflowGeneralGroupV1.setStatus(_B)
openflowLogicalSwitchGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,69,1,1,2))
openflowLogicalSwitchGroupV1.setObjects(*((_A,_P),(_A,_G),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:openflowLogicalSwitchGroupV1.setStatus(_W)
openflowConnectionGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,69,1,1,3))
openflowConnectionGroupV1.setObjects(*((_A,_b),(_A,_L),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:openflowConnectionGroupV1.setStatus(_B)
openflowGenericGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,69,1,1,4))
openflowGenericGroupV1.setObjects(*((_A,_M),(_A,_m),(_A,_n),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:openflowGenericGroupV1.setStatus(_B)
openflowLogicalSwitchGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,69,1,1,5))
openflowLogicalSwitchGroupV2.setObjects(*((_A,_P),(_A,_G),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_q),(_A,_r),(_A,_s),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:openflowLogicalSwitchGroupV2.setStatus(_B)
openflowDiagnosticsGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,69,1,1,6))
openflowDiagnosticsGroupV1.setObjects(*((_A,_N),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y)))
if mibBuilder.loadTexts:openflowDiagnosticsGroupV1.setStatus(_B)
openflowLogGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,69,1,1,7))
openflowLogGroupV1.setObjects(*((_A,_O),(_A,_z),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:openflowLogGroupV1.setStatus(_B)
lumOpenflowComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,69,1,2,1))
lumOpenflowComplV1.setObjects(*((_A,_H),(_A,_X),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:lumOpenflowComplV1.setStatus(_W)
lumOpenflowComplV2=ModuleCompliance((1,3,6,1,4,1,8708,2,69,1,2,2))
lumOpenflowComplV2.setObjects(*((_A,_H),(_A,_X),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:lumOpenflowComplV2.setStatus(_W)
lumOpenflowComplV3=ModuleCompliance((1,3,6,1,4,1,8708,2,69,1,2,3))
lumOpenflowComplV3.setObjects(*((_A,_H),(_A,_A2),(_A,_I),(_A,_J),(_A,_A3),(_A,_A4)))
if mibBuilder.loadTexts:lumOpenflowComplV3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'lumOpenflowMIBModule':lumOpenflowMIBModule,'lumOpenflowConfs':lumOpenflowConfs,'lumOpenflowGroups':lumOpenflowGroups,_H:openflowGeneralGroupV1,_X:openflowLogicalSwitchGroupV1,_I:openflowConnectionGroupV1,_J:openflowGenericGroupV1,_A2:openflowLogicalSwitchGroupV2,_A3:openflowDiagnosticsGroupV1,_A4:openflowLogGroupV1,'lumOpenflowCompl':lumOpenflowCompl,'lumOpenflowComplV1':lumOpenflowComplV1,'lumOpenflowComplV2':lumOpenflowComplV2,'lumOpenflowComplV3':lumOpenflowComplV3,'lumOpenflowMIBObjects':lumOpenflowMIBObjects,'openflowGeneral':openflowGeneral,_Z:openflowGeneralConfigLastChangeTime,_a:openflowGeneralStateLastChangeTime,'openflowGeneralLogicalSwitchTableSize':openflowGeneralLogicalSwitchTableSize,'openflowGeneralGenericTableSize':openflowGeneralGenericTableSize,'openflowGeneralConnectionTableSize':openflowGeneralConnectionTableSize,'openflowGeneralDiagnosticsTableSize':openflowGeneralDiagnosticsTableSize,'openflowGeneralLogTableSize':openflowGeneralLogTableSize,'openflowLogicalSwitchList':openflowLogicalSwitchList,'openflowLogicalSwitchTable':openflowLogicalSwitchTable,'openflowLogicalSwitchEntry':openflowLogicalSwitchEntry,_P:openflowLogicalSwitchName,_G:openflowLogicalSwitchIndex,_Q:openflowLogicalSwitchDescr,_R:openflowLogicalSwitchIdentity,_S:openflowLogicalSwitchMacAddress,_T:openflowLogicalSwitchDpId,_q:openflowLogicalSwitchAssociateCxn,_U:openflowLogicalSwitchSubrack,_V:openflowLogicalSwitchSlot,_r:openflowLogicalSwitchGetTracelogs,_s:openflowLogicalSwitchOfVersion,'openflowConnectionList':openflowConnectionList,'openflowConnectionTable':openflowConnectionTable,'openflowConnectionEntry':openflowConnectionEntry,_b:openflowConnectionName,_L:openflowConnectionIndex,_c:openflowConnectionDescr,_d:openflowConnectionIdentity,_e:openflowConnectionSwitchIdentity,_f:openflowConnectionIpv4Addr,_g:openflowConnectionTcpPort,_h:openflowConnectionState,_i:openflowConnectionRole,_j:openflowConnectionOfVersion,_k:openflowConnectionSubrack,_l:openflowConnectionSlot,'openflowGenericList':openflowGenericList,'openflowGenericTable':openflowGenericTable,'openflowGenericEntry':openflowGenericEntry,_M:openflowGenericIndex,_m:openflowGenericName,_n:openflowGenericSubrack,_o:openflowGenericSlot,_p:openflowGenericCreateOFLS,'openflowDiagnosticsList':openflowDiagnosticsList,'openflowDiagnosticsTable':openflowDiagnosticsTable,'openflowDiagnosticsEntry':openflowDiagnosticsEntry,_N:openflowDiagnosticsIndex,_t:openflowDiagnosticsName,_u:openflowDiagnosticsIpv4Addr,_v:openflowDiagnosticsTcpPort,_w:openflowDiagnosticsLogServerType,_x:openflowDiagnosticsConfigure,_y:openflowDiagnosticsSubrack,'openflowLogList':openflowLogList,'openflowLogTable':openflowLogTable,'openflowLogEntry':openflowLogEntry,_O:openflowLogIndex,_z:openflowLogName,_A0:openflowLogSubrack,_A1:openflowLogCreateOFDiagnostics})