_A9='rdbmsSrvInfoDiskOutOfSpaces'
_A8='rdbmsRelActiveTime'
_A7='rdbmsSrvLimitedResourceDescription'
_A6='rdbmsSrvLimitedResourceFailures'
_A5='rdbmsSrvLimitedResourceHighwater'
_A4='rdbmsSrvLimitedResourceCurrent'
_A3='rdbmsSrvLimitedResourceLimit'
_A2='rdbmsSrvParamComment'
_A1='rdbmsSrvParamCurrValue'
_A0='rdbmsSrvInfoMaxInboundAssociations'
_z='rdbmsSrvInfoHighwaterInboundAssociations'
_y='rdbmsSrvInfoRequestSends'
_x='rdbmsSrvInfoRequestRecvs'
_w='rdbmsSrvInfoHandledRequests'
_v='rdbmsSrvInfoPageWrites'
_u='rdbmsSrvInfoPageReads'
_t='rdbmsSrvInfoLogicalWrites'
_s='rdbmsSrvInfoLogicalReads'
_r='rdbmsSrvInfoDiskWrites'
_q='rdbmsSrvInfoDiskReads'
_p='rdbmsSrvInfoFinishedTransactions'
_o='rdbmsSrvInfoStartupTime'
_n='rdbmsSrvContact'
_m='rdbmsSrvProductName'
_l='rdbmsSrvVendorName'
_k='rdbmsSrvPrivateMibOID'
_j='rdbmsDbLimitedResourceDescription'
_i='rdbmsDbLimitedResourceFailures'
_h='rdbmsDbLimitedResourceHighwater'
_g='rdbmsDbLimitedResourceCurrent'
_f='rdbmsDbLimitedResourceLimit'
_e='rdbmsDbParamComment'
_d='rdbmsDbParamCurrValue'
_c='rdbmsDbInfoLastBackup'
_b='rdbmsDbInfoSizeUsed'
_a='rdbmsDbInfoSizeAllocated'
_Z='rdbmsDbInfoSizeUnits'
_Y='rdbmsDbInfoVersion'
_X='rdbmsDbInfoProductName'
_W='rdbmsDbContact'
_V='rdbmsDbName'
_U='rdbmsDbVendorName'
_T='rdbmsDbPrivateMibOID'
_S='rdbmsSrvLimitedResourceName'
_R='rdbmsSrvParamSubIndex'
_Q='rdbmsSrvParamName'
_P='rdbmsDbLimitedResourceName'
_O='rdbmsDbParamSubIndex'
_N='rdbmsDbParamName'
_M='applGroups'
_L='rdbmsGroup'
_K='rdbmsRelState'
_J='DisplayString'
_I='rdbmsDbIndex'
_H='applIndex'
_G='not-accessible'
_F='NETWORK-SERVICES-MIB'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='RDBMS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
applGroups,applIndex=mibBuilder.importSymbols(_F,_M,_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
AutonomousType,DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType','DateAndTime',_J,'PhysAddress','TextualConvention')
rdbmsMIB=ModuleIdentity((1,3,6,1,2,1,39))
_RdbmsObjects_ObjectIdentity=ObjectIdentity
rdbmsObjects=_RdbmsObjects_ObjectIdentity((1,3,6,1,2,1,39,1))
_RdbmsDbTable_Object=MibTable
rdbmsDbTable=_RdbmsDbTable_Object((1,3,6,1,2,1,39,1,1))
if mibBuilder.loadTexts:rdbmsDbTable.setStatus(_A)
_RdbmsDbEntry_Object=MibTableRow
rdbmsDbEntry=_RdbmsDbEntry_Object((1,3,6,1,2,1,39,1,1,1))
rdbmsDbEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:rdbmsDbEntry.setStatus(_A)
class _RdbmsDbIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RdbmsDbIndex_Type.__name__=_D
_RdbmsDbIndex_Object=MibTableColumn
rdbmsDbIndex=_RdbmsDbIndex_Object((1,3,6,1,2,1,39,1,1,1,1),_RdbmsDbIndex_Type())
rdbmsDbIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:rdbmsDbIndex.setStatus(_A)
_RdbmsDbPrivateMibOID_Type=ObjectIdentifier
_RdbmsDbPrivateMibOID_Object=MibTableColumn
rdbmsDbPrivateMibOID=_RdbmsDbPrivateMibOID_Object((1,3,6,1,2,1,39,1,1,1,2),_RdbmsDbPrivateMibOID_Type())
rdbmsDbPrivateMibOID.setMaxAccess(_C)
if mibBuilder.loadTexts:rdbmsDbPrivateMibOID.setStatus(_A)
_RdbmsDbVendorName_Type=DisplayString
_RdbmsDbVendorName_Object=MibTableColumn
rdbmsDbVendorName=_RdbmsDbVendorName_Object((1,3,6,1,2,1,39,1,1,1,3),_RdbmsDbVendorName_Type())
rdbmsDbVendorName.setMaxAccess(_C)
if mibBuilder.loadTexts:rdbmsDbVendorName.setStatus(_A)
_RdbmsDbName_Type=DisplayString
_RdbmsDbName_Object=MibTableColumn
rdbmsDbName=_RdbmsDbName_Object((1,3,6,1,2,1,39,1,1,1,4),_RdbmsDbName_Type())
rdbmsDbName.setMaxAccess(_C)
if mibBuilder.loadTexts:rdbmsDbName.setStatus(_A)
_RdbmsDbContact_Type=DisplayString
_RdbmsDbContact_Object=MibTableColumn
rdbmsDbContact=_RdbmsDbContact_Object((1,3,6,1,2,1,39,1,1,1,5),_RdbmsDbContact_Type())
rdbmsDbContact.setMaxAccess(_E)
if mibBuilder.loadTexts:rdbmsDbContact.setStatus(_A)
_RdbmsDbInfoTable_Object=MibTable
rdbmsDbInfoTable=_RdbmsDbInfoTable_Object((1,3,6,1,2,1,39,1,2))
if mibBuilder.loadTexts:rdbmsDbInfoTable.setStatus(_A)
_RdbmsDbInfoEntry_Object=MibTableRow
rdbmsDbInfoEntry=_RdbmsDbInfoEntry_Object((1,3,6,1,2,1,39,1,2,1))
rdbmsDbInfoEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:rdbmsDbInfoEntry.setStatus(_A)
_RdbmsDbInfoProductName_Type=DisplayString
_RdbmsDbInfoProductName_Object=MibTableColumn
rdbmsDbInfoProductName=_RdbmsDbInfoProductName_Object((1,3,6,1,2,1,39,1,2,1,1),_RdbmsDbInfoProductName_Type())
rdbmsDbInfoProductName.setMaxAccess(_C)
if mibBuilder.loadTexts:rdbmsDbInfoProductName.setStatus(_A)
_RdbmsDbInfoVersion_Type=DisplayString
_RdbmsDbInfoVersion_Object=MibTableColumn
rdbmsDbInfoVersion=_RdbmsDbInfoVersion_Object((1,3,6,1,2,1,39,1,2,1,2),_RdbmsDbInfoVersion_Type())
rdbmsDbInfoVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:rdbmsDbInfoVersion.setStatus(_A)
class _RdbmsDbInfoSizeUnits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('bytes',1),('kbytes',2),('mbytes',3),('gbytes',4),('tbytes',5)))
_RdbmsDbInfoSizeUnits_Type.__name__=_D
_RdbmsDbInfoSizeUnits_Object=MibTableColumn
rdbmsDbInfoSizeUnits=_RdbmsDbInfoSizeUnits_Object((1,3,6,1,2,1,39,1,2,1,3),_RdbmsDbInfoSizeUnits_Type())
rdbmsDbInfoSizeUnits.setMaxAccess(_C)
if mibBuilder.loadTexts:rdbmsDbInfoSizeUnits.setStatus(_A)
class _RdbmsDbInfoSizeAllocated_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RdbmsDbInfoSizeAllocated_Type.__name__=_D
_RdbmsDbInfoSizeAllocated_Object=MibTableColumn
rdbmsDbInfoSizeAllocated=_RdbmsDbInfoSizeAllocated_Object((1,3,6,1,2,1,39,1,2,1,4),_RdbmsDbInfoSizeAllocated_Type())
rdbmsDbInfoSizeAllocated.setMaxAccess(_E)
if mibBuilder.loadTexts:rdbmsDbInfoSizeAllocated.setStatus(_A)
class _RdbmsDbInfoSizeUsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RdbmsDbInfoSizeUsed_Type.__name__=_D
_RdbmsDbInfoSizeUsed_Object=MibTableColumn
rdbmsDbInfoSizeUsed=_RdbmsDbInfoSizeUsed_Object((1,3,6,1,2,1,39,1,2,1,5),_RdbmsDbInfoSizeUsed_Type())
rdbmsDbInfoSizeUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:rdbmsDbInfoSizeUsed.setStatus(_A)
_RdbmsDbInfoLastBackup_Type=DateAndTime
_RdbmsDbInfoLastBackup_Object=MibTableColumn
rdbmsDbInfoLastBackup=_RdbmsDbInfoLastBackup_Object((1,3,6,1,2,1,39,1,2,1,6),_RdbmsDbInfoLastBackup_Type())
rdbmsDbInfoLastBackup.setMaxAccess(_C)
if mibBuilder.loadTexts:rdbmsDbInfoLastBackup.setStatus(_A)
_RdbmsDbParamTable_Object=MibTable
rdbmsDbParamTable=_RdbmsDbParamTable_Object((1,3,6,1,2,1,39,1,3))
if mibBuilder.loadTexts:rdbmsDbParamTable.setStatus(_A)
_RdbmsDbParamEntry_Object=MibTableRow
rdbmsDbParamEntry=_RdbmsDbParamEntry_Object((1,3,6,1,2,1,39,1,3,1))
rdbmsDbParamEntry.setIndexNames((0,_B,_I),(0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:rdbmsDbParamEntry.setStatus(_A)
class _RdbmsDbParamName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_RdbmsDbParamName_Type.__name__=_J
_RdbmsDbParamName_Object=MibTableColumn
rdbmsDbParamName=_RdbmsDbParamName_Object((1,3,6,1,2,1,39,1,3,1,1),_RdbmsDbParamName_Type())
rdbmsDbParamName.setMaxAccess(_G)
if mibBuilder.loadTexts:rdbmsDbParamName.setStatus(_A)
class _RdbmsDbParamSubIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RdbmsDbParamSubIndex_Type.__name__=_D
_RdbmsDbParamSubIndex_Object=MibTableColumn
rdbmsDbParamSubIndex=_RdbmsDbParamSubIndex_Object((1,3,6,1,2,1,39,1,3,1,2),_RdbmsDbParamSubIndex_Type())
rdbmsDbParamSubIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:rdbmsDbParamSubIndex.setStatus(_A)
_RdbmsDbParamID_Type=AutonomousType
_RdbmsDbParamID_Object=MibTableColumn
rdbmsDbParamID=_RdbmsDbParamID_Object((1,3,6,1,2,1,39,1,3,1,3),_RdbmsDbParamID_Type())
rdbmsDbParamID.setMaxAccess(_C)
if mibBuilder.loadTexts:rdbmsDbParamID.setStatus(_A)
_RdbmsDbParamCurrValue_Type=DisplayString
_RdbmsDbParamCurrValue_Object=MibTableColumn
rdbmsDbParamCurrValue=_RdbmsDbParamCurrValue_Object((1,3,6,1,2,1,39,1,3,1,4),_RdbmsDbParamCurrValue_Type())
rdbmsDbParamCurrValue.setMaxAccess(_E)
if mibBuilder.loadTexts:rdbmsDbParamCurrValue.setStatus(_A)
_RdbmsDbParamComment_Type=DisplayString
_RdbmsDbParamComment_Object=MibTableColumn
rdbmsDbParamComment=_RdbmsDbParamComment_Object((1,3,6,1,2,1,39,1,3,1,5),_RdbmsDbParamComment_Type())
rdbmsDbParamComment.setMaxAccess(_E)
if mibBuilder.loadTexts:rdbmsDbParamComment.setStatus(_A)
_RdbmsDbLimitedResourceTable_Object=MibTable
rdbmsDbLimitedResourceTable=_RdbmsDbLimitedResourceTable_Object((1,3,6,1,2,1,39,1,4))
if mibBuilder.loadTexts:rdbmsDbLimitedResourceTable.setStatus(_A)
_RdbmsDbLimitedResourceEntry_Object=MibTableRow
rdbmsDbLimitedResourceEntry=_RdbmsDbLimitedResourceEntry_Object((1,3,6,1,2,1,39,1,4,1))
rdbmsDbLimitedResourceEntry.setIndexNames((0,_B,_I),(0,_B,_P))
if mibBuilder.loadTexts:rdbmsDbLimitedResourceEntry.setStatus(_A)
_RdbmsDbLimitedResourceName_Type=DisplayString
_RdbmsDbLimitedResourceName_Object=MibTableColumn
rdbmsDbLimitedResourceName=_RdbmsDbLimitedResourceName_Object((1,3,6,1,2,1,39,1,4,1,1),_RdbmsDbLimitedResourceName_Type())
rdbmsDbLimitedResourceName.setMaxAccess(_G)
if mibBuilder.loadTexts:rdbmsDbLimitedResourceName.setStatus(_A)
_RdbmsDbLimitedResourceID_Type=AutonomousType
_RdbmsDbLimitedResourceID_Object=MibTableColumn
rdbmsDbLimitedResourceID=_RdbmsDbLimitedResourceID_Object((1,3,6,1,2,1,39,1,4,1,2),_RdbmsDbLimitedResourceID_Type())
rdbmsDbLimitedResourceID.setMaxAccess(_C)
if mibBuilder.loadTexts:rdbmsDbLimitedResourceID.setStatus(_A)
class _RdbmsDbLimitedResourceLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RdbmsDbLimitedResourceLimit_Type.__name__=_D
_RdbmsDbLimitedResourceLimit_Object=MibTableColumn
rdbmsDbLimitedResourceLimit=_RdbmsDbLimitedResourceLimit_Object((1,3,6,1,2,1,39,1,4,1,3),_RdbmsDbLimitedResourceLimit_Type())
rdbmsDbLimitedResourceLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:rdbmsDbLimitedResourceLimit.setStatus(_A)
class _RdbmsDbLimitedResourceCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RdbmsDbLimitedResourceCurrent_Type.__name__=_D
_RdbmsDbLimitedResourceCurrent_Object=MibTableColumn
rdbmsDbLimitedResourceCurrent=_RdbmsDbLimitedResourceCurrent_Object((1,3,6,1,2,1,39,1,4,1,4),_RdbmsDbLimitedResourceCurrent_Type())
rdbmsDbLimitedResourceCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:rdbmsDbLimitedResourceCurrent.setStatus(_A)
class _RdbmsDbLimitedResourceHighwater_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RdbmsDbLimitedResourceHighwater_Type.__name__=_D
_RdbmsDbLimitedResourceHighwater_Object=MibTableColumn
rdbmsDbLimitedResourceHighwater=_RdbmsDbLimitedResourceHighwater_Object((1,3,6,1,2,1,39,1,4,1,5),_RdbmsDbLimitedResourceHighwater_Type())
rdbmsDbLimitedResourceHighwater.setMaxAccess(_C)
if mibBuilder.loadTexts:rdbmsDbLimitedResourceHighwater.setStatus(_A)
_RdbmsDbLimitedResourceFailures_Type=Counter32
_RdbmsDbLimitedResourceFailures_Object=MibTableColumn
rdbmsDbLimitedResourceFailures=_RdbmsDbLimitedResourceFailures_Object((1,3,6,1,2,1,39,1,4,1,6),_RdbmsDbLimitedResourceFailures_Type())
rdbmsDbLimitedResourceFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:rdbmsDbLimitedResourceFailures.setStatus(_A)
_RdbmsDbLimitedResourceDescription_Type=DisplayString
_RdbmsDbLimitedResourceDescription_Object=MibTableColumn
rdbmsDbLimitedResourceDescription=_RdbmsDbLimitedResourceDescription_Object((1,3,6,1,2,1,39,1,4,1,7),_RdbmsDbLimitedResourceDescription_Type())
rdbmsDbLimitedResourceDescription.setMaxAccess(_E)
if mibBuilder.loadTexts:rdbmsDbLimitedResourceDescription.setStatus(_A)
_RdbmsSrvTable_Object=MibTable
rdbmsSrvTable=_RdbmsSrvTable_Object((1,3,6,1,2,1,39,1,5))
if mibBuilder.loadTexts:rdbmsSrvTable.setStatus(_A)
_RdbmsSrvEntry_Object=MibTableRow
rdbmsSrvEntry=_RdbmsSrvEntry_Object((1,3,6,1,2,1,39,1,5,1))
rdbmsSrvEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:rdbmsSrvEntry.setStatus(_A)
_RdbmsSrvPrivateMibOID_Type=ObjectIdentifier
_RdbmsSrvPrivateMibOID_Object=MibTableColumn
rdbmsSrvPrivateMibOID=_RdbmsSrvPrivateMibOID_Object((1,3,6,1,2,1,39,1,5,1,1),_RdbmsSrvPrivateMibOID_Type())
rdbmsSrvPrivateMibOID.setMaxAccess(_C)
if mibBuilder.loadTexts:rdbmsSrvPrivateMibOID.setStatus(_A)
_RdbmsSrvVendorName_Type=DisplayString
_RdbmsSrvVendorName_Object=MibTableColumn
rdbmsSrvVendorName=_RdbmsSrvVendorName_Object((1,3,6,1,2,1,39,1,5,1,2),_RdbmsSrvVendorName_Type())
rdbmsSrvVendorName.setMaxAccess(_C)
if mibBuilder.loadTexts:rdbmsSrvVendorName.setStatus(_A)
_RdbmsSrvProductName_Type=DisplayString
_RdbmsSrvProductName_Object=MibTableColumn
rdbmsSrvProductName=_RdbmsSrvProductName_Object((1,3,6,1,2,1,39,1,5,1,3),_RdbmsSrvProductName_Type())
rdbmsSrvProductName.setMaxAccess(_C)
if mibBuilder.loadTexts:rdbmsSrvProductName.setStatus(_A)
_RdbmsSrvContact_Type=DisplayString
_RdbmsSrvContact_Object=MibTableColumn
rdbmsSrvContact=_RdbmsSrvContact_Object((1,3,6,1,2,1,39,1,5,1,4),_RdbmsSrvContact_Type())
rdbmsSrvContact.setMaxAccess(_E)
if mibBuilder.loadTexts:rdbmsSrvContact.setStatus(_A)
_RdbmsSrvInfoTable_Object=MibTable
rdbmsSrvInfoTable=_RdbmsSrvInfoTable_Object((1,3,6,1,2,1,39,1,6))
if mibBuilder.loadTexts:rdbmsSrvInfoTable.setStatus(_A)
_RdbmsSrvInfoEntry_Object=MibTableRow
rdbmsSrvInfoEntry=_RdbmsSrvInfoEntry_Object((1,3,6,1,2,1,39,1,6,1))
rdbmsSrvInfoEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:rdbmsSrvInfoEntry.setStatus(_A)
_RdbmsSrvInfoStartupTime_Type=DateAndTime
_RdbmsSrvInfoStartupTime_Object=MibTableColumn
rdbmsSrvInfoStartupTime=_RdbmsSrvInfoStartupTime_Object((1,3,6,1,2,1,39,1,6,1,1),_RdbmsSrvInfoStartupTime_Type())
rdbmsSrvInfoStartupTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rdbmsSrvInfoStartupTime.setStatus(_A)
_RdbmsSrvInfoFinishedTransactions_Type=Gauge32
_RdbmsSrvInfoFinishedTransactions_Object=MibTableColumn
rdbmsSrvInfoFinishedTransactions=_RdbmsSrvInfoFinishedTransactions_Object((1,3,6,1,2,1,39,1,6,1,2),_RdbmsSrvInfoFinishedTransactions_Type())
rdbmsSrvInfoFinishedTransactions.setMaxAccess(_C)
if mibBuilder.loadTexts:rdbmsSrvInfoFinishedTransactions.setStatus(_A)
_RdbmsSrvInfoDiskReads_Type=Counter32
_RdbmsSrvInfoDiskReads_Object=MibTableColumn
rdbmsSrvInfoDiskReads=_RdbmsSrvInfoDiskReads_Object((1,3,6,1,2,1,39,1,6,1,3),_RdbmsSrvInfoDiskReads_Type())
rdbmsSrvInfoDiskReads.setMaxAccess(_C)
if mibBuilder.loadTexts:rdbmsSrvInfoDiskReads.setStatus(_A)
_RdbmsSrvInfoLogicalReads_Type=Counter32
_RdbmsSrvInfoLogicalReads_Object=MibTableColumn
rdbmsSrvInfoLogicalReads=_RdbmsSrvInfoLogicalReads_Object((1,3,6,1,2,1,39,1,6,1,4),_RdbmsSrvInfoLogicalReads_Type())
rdbmsSrvInfoLogicalReads.setMaxAccess(_C)
if mibBuilder.loadTexts:rdbmsSrvInfoLogicalReads.setStatus(_A)
_RdbmsSrvInfoDiskWrites_Type=Counter32
_RdbmsSrvInfoDiskWrites_Object=MibTableColumn
rdbmsSrvInfoDiskWrites=_RdbmsSrvInfoDiskWrites_Object((1,3,6,1,2,1,39,1,6,1,5),_RdbmsSrvInfoDiskWrites_Type())
rdbmsSrvInfoDiskWrites.setMaxAccess(_C)
if mibBuilder.loadTexts:rdbmsSrvInfoDiskWrites.setStatus(_A)
_RdbmsSrvInfoLogicalWrites_Type=Counter32
_RdbmsSrvInfoLogicalWrites_Object=MibTableColumn
rdbmsSrvInfoLogicalWrites=_RdbmsSrvInfoLogicalWrites_Object((1,3,6,1,2,1,39,1,6,1,6),_RdbmsSrvInfoLogicalWrites_Type())
rdbmsSrvInfoLogicalWrites.setMaxAccess(_C)
if mibBuilder.loadTexts:rdbmsSrvInfoLogicalWrites.setStatus(_A)
_RdbmsSrvInfoPageReads_Type=Counter32
_RdbmsSrvInfoPageReads_Object=MibTableColumn
rdbmsSrvInfoPageReads=_RdbmsSrvInfoPageReads_Object((1,3,6,1,2,1,39,1,6,1,7),_RdbmsSrvInfoPageReads_Type())
rdbmsSrvInfoPageReads.setMaxAccess(_C)
if mibBuilder.loadTexts:rdbmsSrvInfoPageReads.setStatus(_A)
_RdbmsSrvInfoPageWrites_Type=Counter32
_RdbmsSrvInfoPageWrites_Object=MibTableColumn
rdbmsSrvInfoPageWrites=_RdbmsSrvInfoPageWrites_Object((1,3,6,1,2,1,39,1,6,1,8),_RdbmsSrvInfoPageWrites_Type())
rdbmsSrvInfoPageWrites.setMaxAccess(_C)
if mibBuilder.loadTexts:rdbmsSrvInfoPageWrites.setStatus(_A)
_RdbmsSrvInfoDiskOutOfSpaces_Type=Counter32
_RdbmsSrvInfoDiskOutOfSpaces_Object=MibTableColumn
rdbmsSrvInfoDiskOutOfSpaces=_RdbmsSrvInfoDiskOutOfSpaces_Object((1,3,6,1,2,1,39,1,6,1,9),_RdbmsSrvInfoDiskOutOfSpaces_Type())
rdbmsSrvInfoDiskOutOfSpaces.setMaxAccess(_C)
if mibBuilder.loadTexts:rdbmsSrvInfoDiskOutOfSpaces.setStatus(_A)
_RdbmsSrvInfoHandledRequests_Type=Counter32
_RdbmsSrvInfoHandledRequests_Object=MibTableColumn
rdbmsSrvInfoHandledRequests=_RdbmsSrvInfoHandledRequests_Object((1,3,6,1,2,1,39,1,6,1,10),_RdbmsSrvInfoHandledRequests_Type())
rdbmsSrvInfoHandledRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:rdbmsSrvInfoHandledRequests.setStatus(_A)
_RdbmsSrvInfoRequestRecvs_Type=Counter32
_RdbmsSrvInfoRequestRecvs_Object=MibTableColumn
rdbmsSrvInfoRequestRecvs=_RdbmsSrvInfoRequestRecvs_Object((1,3,6,1,2,1,39,1,6,1,11),_RdbmsSrvInfoRequestRecvs_Type())
rdbmsSrvInfoRequestRecvs.setMaxAccess(_C)
if mibBuilder.loadTexts:rdbmsSrvInfoRequestRecvs.setStatus(_A)
_RdbmsSrvInfoRequestSends_Type=Counter32
_RdbmsSrvInfoRequestSends_Object=MibTableColumn
rdbmsSrvInfoRequestSends=_RdbmsSrvInfoRequestSends_Object((1,3,6,1,2,1,39,1,6,1,12),_RdbmsSrvInfoRequestSends_Type())
rdbmsSrvInfoRequestSends.setMaxAccess(_C)
if mibBuilder.loadTexts:rdbmsSrvInfoRequestSends.setStatus(_A)
_RdbmsSrvInfoHighwaterInboundAssociations_Type=Gauge32
_RdbmsSrvInfoHighwaterInboundAssociations_Object=MibTableColumn
rdbmsSrvInfoHighwaterInboundAssociations=_RdbmsSrvInfoHighwaterInboundAssociations_Object((1,3,6,1,2,1,39,1,6,1,13),_RdbmsSrvInfoHighwaterInboundAssociations_Type())
rdbmsSrvInfoHighwaterInboundAssociations.setMaxAccess(_C)
if mibBuilder.loadTexts:rdbmsSrvInfoHighwaterInboundAssociations.setStatus(_A)
_RdbmsSrvInfoMaxInboundAssociations_Type=Gauge32
_RdbmsSrvInfoMaxInboundAssociations_Object=MibTableColumn
rdbmsSrvInfoMaxInboundAssociations=_RdbmsSrvInfoMaxInboundAssociations_Object((1,3,6,1,2,1,39,1,6,1,14),_RdbmsSrvInfoMaxInboundAssociations_Type())
rdbmsSrvInfoMaxInboundAssociations.setMaxAccess(_E)
if mibBuilder.loadTexts:rdbmsSrvInfoMaxInboundAssociations.setStatus(_A)
_RdbmsSrvParamTable_Object=MibTable
rdbmsSrvParamTable=_RdbmsSrvParamTable_Object((1,3,6,1,2,1,39,1,7))
if mibBuilder.loadTexts:rdbmsSrvParamTable.setStatus(_A)
_RdbmsSrvParamEntry_Object=MibTableRow
rdbmsSrvParamEntry=_RdbmsSrvParamEntry_Object((1,3,6,1,2,1,39,1,7,1))
rdbmsSrvParamEntry.setIndexNames((0,_F,_H),(0,_B,_Q),(0,_B,_R))
if mibBuilder.loadTexts:rdbmsSrvParamEntry.setStatus(_A)
class _RdbmsSrvParamName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_RdbmsSrvParamName_Type.__name__=_J
_RdbmsSrvParamName_Object=MibTableColumn
rdbmsSrvParamName=_RdbmsSrvParamName_Object((1,3,6,1,2,1,39,1,7,1,1),_RdbmsSrvParamName_Type())
rdbmsSrvParamName.setMaxAccess(_G)
if mibBuilder.loadTexts:rdbmsSrvParamName.setStatus(_A)
class _RdbmsSrvParamSubIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RdbmsSrvParamSubIndex_Type.__name__=_D
_RdbmsSrvParamSubIndex_Object=MibTableColumn
rdbmsSrvParamSubIndex=_RdbmsSrvParamSubIndex_Object((1,3,6,1,2,1,39,1,7,1,2),_RdbmsSrvParamSubIndex_Type())
rdbmsSrvParamSubIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:rdbmsSrvParamSubIndex.setStatus(_A)
_RdbmsSrvParamID_Type=AutonomousType
_RdbmsSrvParamID_Object=MibTableColumn
rdbmsSrvParamID=_RdbmsSrvParamID_Object((1,3,6,1,2,1,39,1,7,1,3),_RdbmsSrvParamID_Type())
rdbmsSrvParamID.setMaxAccess(_C)
if mibBuilder.loadTexts:rdbmsSrvParamID.setStatus(_A)
_RdbmsSrvParamCurrValue_Type=DisplayString
_RdbmsSrvParamCurrValue_Object=MibTableColumn
rdbmsSrvParamCurrValue=_RdbmsSrvParamCurrValue_Object((1,3,6,1,2,1,39,1,7,1,4),_RdbmsSrvParamCurrValue_Type())
rdbmsSrvParamCurrValue.setMaxAccess(_E)
if mibBuilder.loadTexts:rdbmsSrvParamCurrValue.setStatus(_A)
_RdbmsSrvParamComment_Type=DisplayString
_RdbmsSrvParamComment_Object=MibTableColumn
rdbmsSrvParamComment=_RdbmsSrvParamComment_Object((1,3,6,1,2,1,39,1,7,1,5),_RdbmsSrvParamComment_Type())
rdbmsSrvParamComment.setMaxAccess(_E)
if mibBuilder.loadTexts:rdbmsSrvParamComment.setStatus(_A)
_RdbmsSrvLimitedResourceTable_Object=MibTable
rdbmsSrvLimitedResourceTable=_RdbmsSrvLimitedResourceTable_Object((1,3,6,1,2,1,39,1,8))
if mibBuilder.loadTexts:rdbmsSrvLimitedResourceTable.setStatus(_A)
_RdbmsSrvLimitedResourceEntry_Object=MibTableRow
rdbmsSrvLimitedResourceEntry=_RdbmsSrvLimitedResourceEntry_Object((1,3,6,1,2,1,39,1,8,1))
rdbmsSrvLimitedResourceEntry.setIndexNames((0,_F,_H),(0,_B,_S))
if mibBuilder.loadTexts:rdbmsSrvLimitedResourceEntry.setStatus(_A)
_RdbmsSrvLimitedResourceName_Type=DisplayString
_RdbmsSrvLimitedResourceName_Object=MibTableColumn
rdbmsSrvLimitedResourceName=_RdbmsSrvLimitedResourceName_Object((1,3,6,1,2,1,39,1,8,1,1),_RdbmsSrvLimitedResourceName_Type())
rdbmsSrvLimitedResourceName.setMaxAccess(_G)
if mibBuilder.loadTexts:rdbmsSrvLimitedResourceName.setStatus(_A)
_RdbmsSrvLimitedResourceID_Type=AutonomousType
_RdbmsSrvLimitedResourceID_Object=MibTableColumn
rdbmsSrvLimitedResourceID=_RdbmsSrvLimitedResourceID_Object((1,3,6,1,2,1,39,1,8,1,2),_RdbmsSrvLimitedResourceID_Type())
rdbmsSrvLimitedResourceID.setMaxAccess(_C)
if mibBuilder.loadTexts:rdbmsSrvLimitedResourceID.setStatus(_A)
class _RdbmsSrvLimitedResourceLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RdbmsSrvLimitedResourceLimit_Type.__name__=_D
_RdbmsSrvLimitedResourceLimit_Object=MibTableColumn
rdbmsSrvLimitedResourceLimit=_RdbmsSrvLimitedResourceLimit_Object((1,3,6,1,2,1,39,1,8,1,3),_RdbmsSrvLimitedResourceLimit_Type())
rdbmsSrvLimitedResourceLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:rdbmsSrvLimitedResourceLimit.setStatus(_A)
class _RdbmsSrvLimitedResourceCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RdbmsSrvLimitedResourceCurrent_Type.__name__=_D
_RdbmsSrvLimitedResourceCurrent_Object=MibTableColumn
rdbmsSrvLimitedResourceCurrent=_RdbmsSrvLimitedResourceCurrent_Object((1,3,6,1,2,1,39,1,8,1,4),_RdbmsSrvLimitedResourceCurrent_Type())
rdbmsSrvLimitedResourceCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:rdbmsSrvLimitedResourceCurrent.setStatus(_A)
class _RdbmsSrvLimitedResourceHighwater_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RdbmsSrvLimitedResourceHighwater_Type.__name__=_D
_RdbmsSrvLimitedResourceHighwater_Object=MibTableColumn
rdbmsSrvLimitedResourceHighwater=_RdbmsSrvLimitedResourceHighwater_Object((1,3,6,1,2,1,39,1,8,1,5),_RdbmsSrvLimitedResourceHighwater_Type())
rdbmsSrvLimitedResourceHighwater.setMaxAccess(_C)
if mibBuilder.loadTexts:rdbmsSrvLimitedResourceHighwater.setStatus(_A)
_RdbmsSrvLimitedResourceFailures_Type=Counter32
_RdbmsSrvLimitedResourceFailures_Object=MibTableColumn
rdbmsSrvLimitedResourceFailures=_RdbmsSrvLimitedResourceFailures_Object((1,3,6,1,2,1,39,1,8,1,6),_RdbmsSrvLimitedResourceFailures_Type())
rdbmsSrvLimitedResourceFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:rdbmsSrvLimitedResourceFailures.setStatus(_A)
_RdbmsSrvLimitedResourceDescription_Type=DisplayString
_RdbmsSrvLimitedResourceDescription_Object=MibTableColumn
rdbmsSrvLimitedResourceDescription=_RdbmsSrvLimitedResourceDescription_Object((1,3,6,1,2,1,39,1,8,1,7),_RdbmsSrvLimitedResourceDescription_Type())
rdbmsSrvLimitedResourceDescription.setMaxAccess(_E)
if mibBuilder.loadTexts:rdbmsSrvLimitedResourceDescription.setStatus(_A)
_RdbmsRelTable_Object=MibTable
rdbmsRelTable=_RdbmsRelTable_Object((1,3,6,1,2,1,39,1,9))
if mibBuilder.loadTexts:rdbmsRelTable.setStatus(_A)
_RdbmsRelEntry_Object=MibTableRow
rdbmsRelEntry=_RdbmsRelEntry_Object((1,3,6,1,2,1,39,1,9,1))
rdbmsRelEntry.setIndexNames((0,_B,_I),(0,_F,_H))
if mibBuilder.loadTexts:rdbmsRelEntry.setStatus(_A)
class _RdbmsRelState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),('active',2),('available',3),('restricted',4),('unavailable',5)))
_RdbmsRelState_Type.__name__=_D
_RdbmsRelState_Object=MibTableColumn
rdbmsRelState=_RdbmsRelState_Object((1,3,6,1,2,1,39,1,9,1,1),_RdbmsRelState_Type())
rdbmsRelState.setMaxAccess(_C)
if mibBuilder.loadTexts:rdbmsRelState.setStatus(_A)
_RdbmsRelActiveTime_Type=DateAndTime
_RdbmsRelActiveTime_Object=MibTableColumn
rdbmsRelActiveTime=_RdbmsRelActiveTime_Object((1,3,6,1,2,1,39,1,9,1,2),_RdbmsRelActiveTime_Type())
rdbmsRelActiveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rdbmsRelActiveTime.setStatus(_A)
_RdbmsWellKnownLimitedResources_ObjectIdentity=ObjectIdentity
rdbmsWellKnownLimitedResources=_RdbmsWellKnownLimitedResources_ObjectIdentity((1,3,6,1,2,1,39,1,10))
_RdbmsLogSpace_ObjectIdentity=ObjectIdentity
rdbmsLogSpace=_RdbmsLogSpace_ObjectIdentity((1,3,6,1,2,1,39,1,10,1))
if mibBuilder.loadTexts:rdbmsLogSpace.setStatus(_A)
_RdbmsTraps_ObjectIdentity=ObjectIdentity
rdbmsTraps=_RdbmsTraps_ObjectIdentity((1,3,6,1,2,1,39,2))
_RdbmsConformance_ObjectIdentity=ObjectIdentity
rdbmsConformance=_RdbmsConformance_ObjectIdentity((1,3,6,1,2,1,39,3))
_RdbmsCompliances_ObjectIdentity=ObjectIdentity
rdbmsCompliances=_RdbmsCompliances_ObjectIdentity((1,3,6,1,2,1,39,3,1))
_RdbmsGroups_ObjectIdentity=ObjectIdentity
rdbmsGroups=_RdbmsGroups_ObjectIdentity((1,3,6,1,2,1,39,3,2))
rdbmsGroup=ObjectGroup((1,3,6,1,2,1,39,3,2,1))
rdbmsGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_K),(_B,_A8)))
if mibBuilder.loadTexts:rdbmsGroup.setStatus(_A)
rdbmsStateChange=NotificationType((1,3,6,1,2,1,39,2,1))
rdbmsStateChange.setObjects((_B,_K))
if mibBuilder.loadTexts:rdbmsStateChange.setStatus(_A)
rdbmsOutOfSpace=NotificationType((1,3,6,1,2,1,39,2,2))
rdbmsOutOfSpace.setObjects((_B,_A9))
if mibBuilder.loadTexts:rdbmsOutOfSpace.setStatus(_A)
rdbmsCompliance=ModuleCompliance((1,3,6,1,2,1,39,3,1,1))
rdbmsCompliance.setObjects(*(('HOST-RESOURCES-MIB','hrSystem'),(_F,_M),(_B,_L),(_B,_L)))
if mibBuilder.loadTexts:rdbmsCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rdbmsMIB':rdbmsMIB,'rdbmsObjects':rdbmsObjects,'rdbmsDbTable':rdbmsDbTable,'rdbmsDbEntry':rdbmsDbEntry,_I:rdbmsDbIndex,_T:rdbmsDbPrivateMibOID,_U:rdbmsDbVendorName,_V:rdbmsDbName,_W:rdbmsDbContact,'rdbmsDbInfoTable':rdbmsDbInfoTable,'rdbmsDbInfoEntry':rdbmsDbInfoEntry,_X:rdbmsDbInfoProductName,_Y:rdbmsDbInfoVersion,_Z:rdbmsDbInfoSizeUnits,_a:rdbmsDbInfoSizeAllocated,_b:rdbmsDbInfoSizeUsed,_c:rdbmsDbInfoLastBackup,'rdbmsDbParamTable':rdbmsDbParamTable,'rdbmsDbParamEntry':rdbmsDbParamEntry,_N:rdbmsDbParamName,_O:rdbmsDbParamSubIndex,'rdbmsDbParamID':rdbmsDbParamID,_d:rdbmsDbParamCurrValue,_e:rdbmsDbParamComment,'rdbmsDbLimitedResourceTable':rdbmsDbLimitedResourceTable,'rdbmsDbLimitedResourceEntry':rdbmsDbLimitedResourceEntry,_P:rdbmsDbLimitedResourceName,'rdbmsDbLimitedResourceID':rdbmsDbLimitedResourceID,_f:rdbmsDbLimitedResourceLimit,_g:rdbmsDbLimitedResourceCurrent,_h:rdbmsDbLimitedResourceHighwater,_i:rdbmsDbLimitedResourceFailures,_j:rdbmsDbLimitedResourceDescription,'rdbmsSrvTable':rdbmsSrvTable,'rdbmsSrvEntry':rdbmsSrvEntry,_k:rdbmsSrvPrivateMibOID,_l:rdbmsSrvVendorName,_m:rdbmsSrvProductName,_n:rdbmsSrvContact,'rdbmsSrvInfoTable':rdbmsSrvInfoTable,'rdbmsSrvInfoEntry':rdbmsSrvInfoEntry,_o:rdbmsSrvInfoStartupTime,_p:rdbmsSrvInfoFinishedTransactions,_q:rdbmsSrvInfoDiskReads,_s:rdbmsSrvInfoLogicalReads,_r:rdbmsSrvInfoDiskWrites,_t:rdbmsSrvInfoLogicalWrites,_u:rdbmsSrvInfoPageReads,_v:rdbmsSrvInfoPageWrites,_A9:rdbmsSrvInfoDiskOutOfSpaces,_w:rdbmsSrvInfoHandledRequests,_x:rdbmsSrvInfoRequestRecvs,_y:rdbmsSrvInfoRequestSends,_z:rdbmsSrvInfoHighwaterInboundAssociations,_A0:rdbmsSrvInfoMaxInboundAssociations,'rdbmsSrvParamTable':rdbmsSrvParamTable,'rdbmsSrvParamEntry':rdbmsSrvParamEntry,_Q:rdbmsSrvParamName,_R:rdbmsSrvParamSubIndex,'rdbmsSrvParamID':rdbmsSrvParamID,_A1:rdbmsSrvParamCurrValue,_A2:rdbmsSrvParamComment,'rdbmsSrvLimitedResourceTable':rdbmsSrvLimitedResourceTable,'rdbmsSrvLimitedResourceEntry':rdbmsSrvLimitedResourceEntry,_S:rdbmsSrvLimitedResourceName,'rdbmsSrvLimitedResourceID':rdbmsSrvLimitedResourceID,_A3:rdbmsSrvLimitedResourceLimit,_A4:rdbmsSrvLimitedResourceCurrent,_A5:rdbmsSrvLimitedResourceHighwater,_A6:rdbmsSrvLimitedResourceFailures,_A7:rdbmsSrvLimitedResourceDescription,'rdbmsRelTable':rdbmsRelTable,'rdbmsRelEntry':rdbmsRelEntry,_K:rdbmsRelState,_A8:rdbmsRelActiveTime,'rdbmsWellKnownLimitedResources':rdbmsWellKnownLimitedResources,'rdbmsLogSpace':rdbmsLogSpace,'rdbmsTraps':rdbmsTraps,'rdbmsStateChange':rdbmsStateChange,'rdbmsOutOfSpace':rdbmsOutOfSpace,'rdbmsConformance':rdbmsConformance,'rdbmsCompliances':rdbmsCompliances,'rdbmsCompliance':rdbmsCompliance,'rdbmsGroups':rdbmsGroups,_L:rdbmsGroup})